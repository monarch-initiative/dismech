---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T17:50:23.693983'
end_time: '2026-08-26T18:01:48.346937'
duration_seconds: 684.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Glucocorticoid Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Familial_Glucocorticoid_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Glucocorticoid Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Glucocorticoid Deficiency** covering all of the
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
- **Disease Name:** Familial Glucocorticoid Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Glucocorticoid Deficiency** covering all of the
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


# Familial Glucocorticoid Deficiency: Disease Characteristics Research Report

## Executive summary

Familial glucocorticoid deficiency (FGD) is a rare, usually autosomal-recessive form of primary adrenal insufficiency characterized by deficient cortisol production despite markedly elevated adrenocorticotropic hormone (ACTH). In its classic form, mineralocorticoid secretion is preserved. The central clinical risks are hypoglycemia, seizures or hypoglycemic brain injury, infection-associated adrenal crisis, shock, and death if treatment is delayed. Hyperpigmentation is the most recognizable chronic sign.

The narrow, classical definition comprises **FGD type 1 due to biallelic MC2R variants** and **FGD type 2 due to biallelic MRAP variants**. Contemporary usage is broader and may include FGD-like disease caused by **NNT, TXNRD2**, and partial defects of **STAR** or **CYP11A1**. MCM4-associated syndromic adrenal insufficiency and AAAS-related Triple A syndrome are important phenocopies rather than uncomplicated isolated FGD. A 62-patient comparison found median presentation at 2.0 years for MC2R-FGD versus 0.08 years for MRAP-FGD. Recent research has particularly expanded recognition of mitochondrial redox disease: a 2023 human report linked NNT deficiency to progressive, irreversible germ-cell loss and emphasized fertility surveillance. No FGD-specific gene, RNA, or cell therapy—and no disease-specific interventional trial—was identified.

**Evidence scope.** Most evidence is aggregated disease-level evidence from cohorts, case series, and reviews, not individual EHR data. The strongest quantitative sources retrieved were a 62-person FGD1/FGD2 cohort, a 95-child Turkish PAI cohort, and a 155-person UK pediatric PAI cohort. Because the latter two include non-FGD genetic adrenal disorders, their percentages must not be interpreted as population prevalence of FGD.

---

## 1. Disease information

### Definition and classification

FGD is an inherited ACTH-resistance disorder in which adrenal cortisol synthesis is inadequate despite high ACTH. Classic biochemical disease consists of low or undetectable cortisol, very high ACTH, and absent overt mineralocorticoid deficiency. The defining distinction from generalized primary adrenal failure is therefore the relative preservation of the zona glomerulosa/renin–angiotensin–aldosterone axis. Partial STAR and CYP11A1 deficiencies may violate this simple distinction by also causing salt loss. (chung2010phenotypiccharacteristicsof pages 1-2, malikova2014novelinsightinto pages 7-8, guran2016rarecausesof pages 4-6)

A concise source statement is: **“Familial glucocorticoid deficiency is a rare autosomal recessive disorder characterized by isolated glucocorticoid deficiency due to ACTH resistance.”** This is a close rendering of the 2010 cohort abstract rather than a verbatim quotation longer than necessary. (chung2010phenotypiccharacteristicsof pages 1-2)

### Identifiers and synonyms

The following identifiers are suitable starting annotations but should be verified against the current release of each ontology before database ingestion:

- **Preferred label:** familial glucocorticoid deficiency.
- **Common synonyms:** FGD; hereditary adrenocortical unresponsiveness to ACTH; hereditary unresponsiveness to adrenocorticotropic hormone; familial ACTH resistance syndrome; glucocorticoid deficiency with normal mineralocorticoid activity.
- **OMIM:** FGD type 1/MC2R is commonly represented as **OMIM phenotype 202200**; FGD type 2/MRAP has a separate phenotype record. Exact current subtype record mappings should be verified directly in OMIM.
- **Orphanet:** commonly indexed under **ORPHA:361**; verify current hierarchy and subtype mappings.
- **MONDO:** a dedicated FGD concept is expected, but a stable MONDO identifier was not established from the retrieved primary literature; do not populate an unverified ID.
- **ICD-10-CM:** no reliably specific FGD code was identified. It is usually coded under primary adrenocortical insufficiency/other specified adrenocortical insufficiency rather than Addison autoimmune disease.
- **ICD-11, MeSH, SNOMED CT:** use the most specific current primary adrenal insufficiency/ACTH-resistance concept available; release-specific identifiers require direct terminology lookup.

These terminology statements are resource-level annotations, whereas the clinical and genetic claims below come from aggregated research cohorts.

---

## 2. Etiology

### Causal factors

FGD is principally **monogenic and germline**, not infectious, toxic, lifestyle-associated, or autoimmune. Biallelic loss-of-function variants impair one of three major biological modules:

1. **ACTH reception:** MC2R or its accessory/trafficking protein MRAP.
2. **Mitochondrial antioxidant defense:** NNT and TXNRD2.
3. **Early steroidogenesis:** partial STAR or CYP11A1 deficiency.

Additional syndromic disorders can generate an FGD-like phenotype, including MCM4 deficiency; AAAS-related Triple A syndrome causes ACTH-resistant adrenal insufficiency but should be separately classified when alacrima, achalasia, or neurologic disease is present. (malikova2014novelinsightinto pages 7-8, refaei2018familialglucocorticoiddeficiency pages 2-2, malikova2014novelinsightinto pages 11-12)

### Genetic risk

Risk is conferred by pathogenic or likely pathogenic variants on both alleles. Consanguinity and founder ancestry increase the probability of homozygosity. In the Turkish cohort, 80% of genetically diagnosed children were homozygous; among CYP11A1 cases, 8/9 were consanguineous. Regional recurrent variants included **MC2R c.560delT**, **CYP11A1 p.Arg451Trp**, and an **MRAP splice-region deletion**. (guran2016rarecausesof pages 6-7, guran2016rarecausesof pages 4-4, guran2016rarecausesof pages 4-6)

The UK cohort identified an ancestry-associated **MC2R p.Ser74Ile** founder variant in 20/30 MC2R cases, particularly among people of Irish or Scottish ancestry. These are diagnostic-enrichment observations, not population penetrance estimates. (buonocore2021geneticanalysisof pages 5-6, buonocore2021geneticanalysisof pages 11-12)

### Environmental, protective, and gene–environment factors

No environmental exposure is known to cause inherited FGD, and no validated protective allele, diet, exercise pattern, toxin avoidance strategy, or vaccine prevents the genotype. Environmental stressors nevertheless strongly modify **clinical expression**: fasting, vomiting, fever, trauma, surgery, and severe infection raise cortisol demand and may precipitate hypoglycemia or adrenal crisis. Thus, the clinically important gene–environment interaction is **fixed impaired cortisol reserve × acute physiological stress**. Early diagnosis, reliable hormone access, avoidance of prolonged fasting, and stress dosing are protective against manifestations, not against inheritance. Severe infections are repeatedly described among presenting features. (malikova2014novelinsightinto pages 7-8, refaei2018familialglucocorticoiddeficiency pages 2-2)

---

## 3. Phenotypes

| Phenotype | Type, timing, course, and frequency | Suggested HPO term |
|---|---|---|
| Hyperpigmentation | Clinical sign caused by chronic ACTH/POMC peptide excess; often progressive and generalized. Common/characteristic, but no defensible pooled percentage was retrieved. Improves after adequate replacement. | **Hyperpigmentation of the skin — HP:0000953** |
| Hypoglycemia | Laboratory abnormality and acute manifestation, commonly neonatal or pediatric; episodic during fasting or illness and potentially severe. | **Hypoglycemia — HP:0001943** |
| Seizures | Acute neurologic sign, usually secondary to severe hypoglycemia; may produce lasting neurologic morbidity. | **Seizure — HP:0001250** |
| Low cortisol | Core laboratory abnormality; persistent without replacement and with low/attenuated cosyntropin response. | **Decreased circulating cortisol level — HP:0008163** |
| Elevated ACTH | Core laboratory abnormality reflecting loss of cortisol feedback and/or adrenal ACTH resistance. | **Increased circulating ACTH level — HP term should be release-verified** |
| Failure to thrive/poor weight gain | Pediatric sign; variable, chronic before diagnosis, and generally improves with treatment. | **Failure to thrive — HP:0001508** |
| Fatigue/weakness | Symptom of cortisol deficiency; nonspecific and variable. | **Fatigue — HP:0012378; Muscle weakness — HP:0001324** |
| Adrenal crisis, shock | Acute life-threatening complication during illness, vomiting, fasting, trauma, or missed treatment. | **Adrenal crisis / hypotension / shock — verify current specific HPO concepts** |
| Tall stature/accelerated linear growth | Particularly associated with untreated MC2R-FGD1; glucocorticoid treatment normalizes growth rate. | **Tall stature — HP:0000098; Accelerated linear growth — release-verify** |
| Normal electrolytes and preserved aldosterone | Important negative/biochemical characteristic in classic FGD; not an HPO abnormality. Salt wasting suggests broader steroidogenic disease or evolving mineralocorticoid impairment. | No disease phenotype term required |
| Gonadal dysfunction in NNT deficiency | Extra-adrenal, progressive phenotype: hypergonadotropic hypogonadism, testicular atrophy/TART, azoospermia, and germ-cell loss may emerge after puberty. | **Male infertility — HP:0003251; Azoospermia — HP:0000027; Hypergonadotropic hypogonadism — HP:0000817** |

### Age and genotype–phenotype data

In the 62-patient study, 40 patients had MC2R variants and 22 had MRAP variants. FGD1 presented at median age **2.0 years** (range 0.02–16), compared with **0.08 years** (birth–1.6 years) for FGD2. Mean/summary height SDS was **+1.75** in FGD1 versus **+0.12** in FGD2. The proposed explanation is that MC2R missense alleles frequently preserve partial activity, whereas MRAP nonsense or splice variants may abolish accessory-protein function. (chung2010phenotypiccharacteristicsof pages 1-2)

The same study linked FGD1 tall stature to prolonged ACTH excess and cortisol deficiency; glucocorticoid replacement normalized growth velocity. This is a genotype-associated clue, not a universal phenotype. (chung2010phenotypiccharacteristicsof pages 4-5)

### Quality of life

No FGD-specific EQ-5D, SF-36, PROMIS, or validated disease-specific quality-of-life dataset was retrieved. Expected burden includes lifelong multidose medication, fear of adrenal crisis, emergency planning, disrupted school/work during illness, neurologic disability after severe hypoglycemia, and—in NNT disease—fertility concerns. These impacts are clinically credible but have not been quantified specifically for FGD in the retrieved evidence.

---

## 4. Genetic and molecular information

The principal gene–phenotype evidence is summarized below.

| Gene or subtype | Core molecular defect | Typical clinical clues / extra-adrenal features | Key quantitative evidence |
|---|---|---|---|
| **MC2R / FGD type 1** | ACTH receptor defect causing adrenal ACTH resistance; many variants are missense with residual receptor function (chung2010phenotypiccharacteristicsof pages 1-2, chung2010phenotypiccharacteristicsof pages 4-5) | Isolated glucocorticoid deficiency with high ACTH, low/undetectable cortisol, usually preserved mineralocorticoid function; hyperpigmentation, hypoglycemia/seizures; later presentation and tall stature are characteristic clues (chung2010phenotypiccharacteristicsof pages 1-2, chung2010phenotypiccharacteristicsof pages 4-5) | In the 62-patient FGD cohort, **40/62** had MC2R variants; type 1 accounted for ~**25%** of all FGD, with median presentation age **2.0 y** (range **0.02–16**) and height SDS **+1.75** (chung2010phenotypiccharacteristicsof pages 1-2). In the UK pediatric PAI cohort, MC2R was **30/155 (19.4%)**; p.S74I occurred in **20/30** cases, consistent with an Irish/Scottish founder effect (buonocore2021geneticanalysisof pages 5-6, buonocore2021geneticanalysisof pages 1-2). |
| **MRAP / FGD type 2** | Defect of melanocortin 2 receptor accessory protein, impairing MC2R trafficking/function; variants often abolish protein (nonsense/splice) (chung2010phenotypiccharacteristicsof pages 1-2) | Similar biochemical picture to FGD1, but typically **earlier neonatal/infant presentation**; not associated with the tall-stature tendency seen in FGD1 (chung2010phenotypiccharacteristicsof pages 1-2, refaei2018familialglucocorticoiddeficiency pages 1-2) | In the 62-patient FGD cohort, **22/62** had MRAP variants; type 2 accounted for ~**20%** of all FGD, with median presentation age **0.08 y** (birth to **1.6 y**) and height SDS **+0.12** (chung2010phenotypiccharacteristicsof pages 1-2). In the Turkish nationwide pediatric PAI cohort, MRAP variants were found in **9/95** children; recurrent **c.IVS3ds±1delG** suggested a regional founder effect (guran2016rarecausesof pages 1-2, guran2016rarecausesof pages 4-6). |
| **NNT** | Mitochondrial inner-membrane defect impairing **NADPH** generation and antioxidant defense, increasing **ROS**-mediated cellular injury (malikova2014novelinsightinto pages 7-8, ferreux2023testicularimpairmentin pages 1-2, ferreux2023testicularimpairmentin pages 6-7) | Primary adrenal insufficiency/FGD-like disease; extra-adrenal clues can include progressive gonadal dysfunction. Reported manifestations include testicular adrenal rest tumor, Sertoli cell-only syndrome, hypergonadotropic hypogonadism, and azoospermia (ferreux2023testicularimpairmentin pages 1-2, ferreux2023testicularimpairmentin pages 6-7) | NNT variants were found in **7/95** children in the Turkish cohort and **6.5%** of the UK pediatric PAI cohort (guran2016rarecausesof pages 1-2, buonocore2021geneticanalysisof pages 2-3, buonocore2021geneticanalysisof pages 1-2). UK data note presentation usually between **6 months and 4 years** (buonocore2021geneticanalysisof pages 11-12). A 2023 case described a **35-year-old** man whose intensified glucocorticoids for **8 months** did **not** improve TART volume or sperm production (ferreux2023testicularimpairmentin pages 1-2). |
| **TXNRD2** | Mitochondrial thioredoxin reductase defect affecting redox homeostasis/ROS detoxification, mechanistically related to NNT-dependent antioxidant pathways (malikova2014novelinsightinto pages 11-12) | FGD-like/PAI presentation is reported, but specific phenotype details were limited in the gathered evidence; consider potential extra-adrenal oxidative-stress vulnerability (malikova2014novelinsightinto pages 11-12) | In the UK pediatric PAI cohort, TXNRD2 accounted for **4.5%** of genetically solved cases overall (**7/155**) (buonocore2021geneticanalysisof pages 1-2). The gathered evidence supports mechanism and cohort frequency, but detailed FGD-specific clinical quantitation was not retrieved (malikova2014novelinsightinto pages 11-12, buonocore2021geneticanalysisof pages 1-2). |
| **Partial STAR / partial CYP11A1 deficiency** | Partial loss of early steroidogenesis steps can mimic isolated glucocorticoid deficiency; CYP11A1 can be disrupted by missplicing, including variants initially predicted benign/synonymous (maharaj2019predictedbenignand pages 3-3, guran2016rarecausesof pages 4-6, buonocore2021geneticanalysisof pages 11-12) | Can present as FGD-like pediatric adrenal insufficiency; clinical clue in UK cohort was **childhood ketotic hypoglycemia**; some cases require mineralocorticoid replacement or show genital findings, so these are not always purely isolated FGD (guran2016rarecausesof pages 1-2, guran2016rarecausesof pages 4-6, buonocore2021geneticanalysisof pages 11-12) | In the Turkish cohort, CYP11A1 variants occurred in **9/95** children, all **9** carrying recurrent **p.R451W** from **8 unrelated families**; **6/9 (66%)** had salt-wasting and **8/9 (89%)** had consanguinity (guran2016rarecausesof pages 4-4, guran2016rarecausesof pages 4-6). In the UK cohort, CYP11A1 accounted for **7.7%** and STAR for **3.9%** of **155** cases (buonocore2021geneticanalysisof pages 1-2). |
| **MCM4** | DNA replication/repair-related defect associated with adrenal insufficiency rather than classic ACTH-receptor pathway failure (malikova2014novelinsightinto pages 7-8) | Important syndromic clue set includes **growth retardation** and **natural killer cell deficiency**; not classic isolated FGD, but may enter the differential in childhood adrenal insufficiency (buonocore2021geneticanalysisof pages 11-12) | Gathered evidence identifies MCM4 as reported in an Irish travelling community and as a cause of progressive PAI (malikova2014novelinsightinto pages 7-8). No robust frequency figures specific to MCM4 were retrieved in the gathered FGD-focused evidence. |
| **AAAS (Triple A syndrome) — differential / phenocopy** | Nuclear pore protein defect (ALADIN), causing ACTH-insensitive adrenal insufficiency but typically **syndromic**, not classic isolated FGD (buonocore2021geneticanalysisof pages 1-2) | Key differentiating clues are **alacrima** and **achalasia**, often with neurologic features; useful differential when ACTH-resistant adrenal insufficiency is suspected (refaei2018familialglucocorticoiddeficiency pages 2-2) | In the UK pediatric PAI cohort, AAAS accounted for **7.1%** (**11/155**) of genetically diagnosed cases (buonocore2021geneticanalysisof pages 1-2). Case-based differential guidance emphasizes excluding Triple A when alacrima/achalasia are present (refaei2018familialglucocorticoiddeficiency pages 2-2). |


*Table: This table summarizes the main familial glucocorticoid deficiency genes and closely related differentials, highlighting mechanism, clinical clues, and quantitative cohort evidence. It is useful for linking genotype to phenotype and for prioritizing diagnostic testing.*

### Gene and variant interpretation

- **MC2R:** biallelic variants cause FGD1. Many are missense changes that impair ligand binding, signal transduction, folding, or surface expression. Approximately 40 distinct missense changes had been reported in the nationwide-cohort discussion. (guran2016rarecausesof pages 6-7)
- **MRAP:** biallelic nonsense, frameshift, or splice variants cause FGD2 by preventing normal MC2R trafficking and signaling. More complete functional loss explains, at least partly, earlier presentation. (chung2010phenotypiccharacteristicsof pages 1-2)
- **NNT:** recessive variants reduce mitochondrial NADPH generation and antioxidant capacity. NNT variants represented 6.5% of the 155-person UK unresolved-PAI cohort and seven patients in the Turkish cohort. (guran2016rarecausesof pages 1-2, buonocore2021geneticanalysisof pages 2-3, buonocore2021geneticanalysisof pages 1-2)
- **TXNRD2:** biallelic mitochondrial thioredoxin-reductase defects cause an oxidative-stress FGD phenotype; TXNRD2 accounted for 4.5% of the UK cohort. (malikova2014novelinsightinto pages 11-12, buonocore2021geneticanalysisof pages 1-2)
- **STAR/CYP11A1:** partial loss can preserve enough fetal gonadal steroidogenesis to avoid classic lipoid congenital adrenal hyperplasia while presenting later with an FGD-like picture. CYP11A1 p.Arg451Trp occurred in nine Turkish patients from eight families; six of nine had salt wasting, showing why these patients should not automatically be labeled as having strictly isolated FGD. (guran2016rarecausesof pages 4-4, guran2016rarecausesof pages 4-6)
- **CYP11A1 missplicing:** functional study showed that variants predicted benign or synonymous can disrupt RNA splicing. Therefore, apparently innocuous exonic variants require RNA/minigene assessment when phenotype and segregation support causality. (maharaj2019predictedbenignand pages 3-3)

The Turkish study found 43 deleterious variants: **24 missense, 7 nonsense, 5 frameshift, 3 in-frame deletion, 2 splice-site, and 2 whole-gene/exon deletions**; 22/43 (51%) were previously unreported. These figures describe a mixed pediatric PAI cohort, not FGD alone. (guran2016rarecausesof pages 4-4)

### Variant curation recommendations

All disease-causing variants are expected to be **germline**. Classification should follow ACMG/AMP criteria using segregation, rarity in ancestry-matched gnomAD data, predicted consequence, functional assays, and phenotype specificity. Exact gnomAD/TOPMed allele frequencies and ClinVar classifications must be retrieved variant by variant; cohort papers cannot substitute for current database records. Missense, nonsense, frameshift, splice, exon/gene deletion, and in-frame deletion classes are all documented. RNA evidence is especially important for CYP11A1. (guran2016rarecausesof pages 4-4, maharaj2019predictedbenignand pages 3-3)

### Modifiers, epigenetics, and chromosomal abnormalities

No validated modifier gene, protective allele, FGD-specific methylation signature, histone alteration, recurrent chromosomal rearrangement, or somatic driver was established. Large deletions should be considered if sequencing is negative, but karyotypic abnormalities are not a characteristic cause. No genetic anticipation has been reported.

---

## 5. Environmental information

FGD is not attributed to toxins, radiation, pollution, smoking, alcohol, diet, occupation, or infectious agents. Infection is a **trigger of decompensation**, not an etiologic agent. Lifestyle management centers on regular dosing, adequate intake during illness, avoidance of prolonged fasting, rapid treatment of vomiting or fever, and carrying emergency hydrocortisone. No zoonotic or transmissible component exists. (refaei2018familialglucocorticoiddeficiency pages 1-2, refaei2018familialglucocorticoiddeficiency pages 2-2)

---

## 6. Mechanism and pathophysiology

### Upstream causal chain: MC2R/MRAP disease

1. Biallelic MC2R or MRAP loss impairs ACTH receptor surface expression or function in adrenal cortical cells.
2. ACTH-induced Gs–adenylyl cyclase–cAMP–PKA signaling falls.
3. Cholesterol mobilization and steroidogenic enzyme expression are insufficient.
4. Cortisol production declines.
5. Reduced glucocorticoid feedback increases hypothalamic CRH and pituitary ACTH.
6. ACTH/POMC-derived melanocortin activity produces hyperpigmentation, while cortisol deficiency causes fasting intolerance, hypoglycemia, poor stress response, and crisis. MRAP-null states generally manifest earlier than partially functional MC2R missense disease. (chung2010phenotypiccharacteristicsof pages 1-2, chung2010phenotypiccharacteristicsof pages 4-5)

**Suggested GO biological processes:** response to ACTH; cAMP-mediated signaling; steroid hormone biosynthetic process; glucocorticoid biosynthetic process; cholesterol transport; regulation of hormone secretion. Exact GO identifiers should be release-verified.

### Mitochondrial redox chain: NNT/TXNRD2 disease

NNT is an inner-mitochondrial-membrane enzyme that supplies NADPH. NADPH maintains glutathione and thioredoxin antioxidant systems. NNT loss lowers reducing capacity, permits chronic ROS excess, and promotes oxidative injury/apoptosis in highly steroidogenic adrenal cells. TXNRD2 affects the same antioxidant network downstream. (malikova2014novelinsightinto pages 7-8, malikova2014novelinsightinto pages 11-12, ferreux2023testicularimpairmentin pages 1-2)

The 2023 report states in its abstract that **“NNT encodes an inner mitochondrial membrane protein that produces large amounts of NADPH.”** It then links NNT deficiency to ROS imbalance and extra-adrenal gonadal damage. (ferreux2023testicularimpairmentin pages 1-2)

In the detailed analysis, NNT was estimated to supply about **50% of required mitochondrial NADPH**. Chronic ROS excess was proposed to cause progressive germ-cell degeneration. NNT-deficient mice showed testicular atrophy, smaller seminiferous tubules, increased degenerating and TUNEL-positive germ cells, and increased 8-OHdG, supporting—not proving—the human causal chain. (ferreux2023testicularimpairmentin pages 6-7)

**Suggested GO terms:** mitochondrial transmembrane transport; NADPH regeneration; cellular response to oxidative stress; glutathione metabolic process; thioredoxin-disulfide reductase activity; apoptotic process. **Cell Ontology suggestions:** adrenal cortical cell; steroid-producing cell; Leydig cell; Sertoli cell; male germ cell.

### Partial steroidogenesis defects

STAR moves cholesterol to the inner mitochondrial membrane; CYP11A1 converts cholesterol to pregnenolone. Partial loss restricts the first steps shared by all adrenal steroids. Because residual activity varies by tissue and developmental stage, patients may resemble isolated FGD or develop mineralocorticoid and gonadal abnormalities. CYP11A1 missplicing demonstrates that protein-coding prediction alone may miss the true mechanism. (maharaj2019predictedbenignand pages 3-3, guran2016rarecausesof pages 4-6, buonocore2021geneticanalysisof pages 11-12)

### Immune, tissue-damage, and omics findings

Classic FGD is not autoimmune or inflammatory. MCM4 disease may include natural-killer-cell deficiency, but that is a syndromic DNA-replication disorder rather than immune-mediated destruction of the adrenal. (malikova2014novelinsightinto pages 7-8, buonocore2021geneticanalysisof pages 11-12)

No robust FGD-specific patient transcriptome, proteome, metabolome, lipidome, single-cell atlas, spatial-transcriptomic dataset, or integrated multi-omics signature was found. Functional evidence presently comes mainly from receptor-expression studies, RNA-splicing assays, patient fibroblasts/cells, and genetically deficient animals.

---

## 7. Anatomical structures affected

- **Primary organ:** bilateral adrenal glands, especially steroidogenic cells of the adrenal cortex. Suggested anatomy: **adrenal gland — UBERON:0002369**; adrenal cortex and zona fasciculata terms should be release-verified.
- **Primary cell:** adrenal cortical/steroidogenic cell; suggested **CL:0002097 adrenal cortical cell** subject to ontology verification.
- **Subcellular compartments:** plasma membrane and secretory/signaling machinery for MC2R/MRAP; mitochondrion and inner mitochondrial membrane for NNT, TXNRD2, STAR, and CYP11A1; nuclear/DNA-replication machinery for MCM4.
- **Secondary organs:** brain in hypoglycemic seizures/injury; skin through ACTH-driven pigmentation; liver and systemic metabolism during hypoglycemia; testes in some NNT-deficient males.
- **NNT gonadal localization:** seminiferous tubules, germ cells, Sertoli-cell compartment, and possibly testicular adrenal-rest tissue. (ferreux2023testicularimpairmentin pages 1-2, ferreux2023testicularimpairmentin pages 6-7)
- **Lateralization:** adrenal dysfunction is systemic/bilateral. Testicular adrenal-rest tumors may be unilateral or bilateral; the 2023 patient had a right-sided lesion but bilateral Sertoli-cell-only pathology. (ferreux2023testicularimpairmentin pages 1-2)

Suggested GO cellular components include plasma membrane, receptor complex, mitochondrion, mitochondrial inner membrane, and nuclear pore complex for the AAAS differential.

---

## 8. Temporal development

FGD is genetically present from conception but clinically variable. MRAP-FGD commonly appears neonatally or in early infancy; MC2R-FGD may present from infancy through adolescence, with a reported upper range of 16 years. NNT disease generally presented between six months and four years in the UK experience. Partial STAR/CYP11A1 disease may appear in childhood with ketotic hypoglycemia. (chung2010phenotypiccharacteristicsof pages 1-2, buonocore2021geneticanalysisof pages 11-12)

The untreated course is chronic with episodic acute decompensation. There is no spontaneous remission of confirmed monogenic FGD. Five children in the broader UK unresolved-PAI cohort experienced resolution without an identified genetic cause, underscoring that transient adrenal insufficiency should not be misclassified as FGD. Genetic disease requires lifelong replacement. (buonocore2021geneticanalysisof pages 1-2)

Critical periods are the neonatal/infant period, intercurrent infection, prolonged fasting, surgery, and puberty in NNT disease. Puberty is a surveillance window for gonadal decline; in the 2023 case, testosterone remained stable until age 31 and then declined rapidly over three years. (ferreux2023testicularimpairmentin pages 6-7)

---

## 9. Inheritance and population

### Epidemiology

FGD is very rare, but no reliable population-wide prevalence, incidence, carrier frequency, sex ratio, or survival registry estimate was retrieved. Published percentages are referral-cohort proportions and should not be converted into cases per 100,000.

In the 62-patient FGD analysis, MC2R and MRAP defects were estimated to explain approximately **25% and 20% of FGD**, respectively. In 2014, about 70% of FGD was considered genetically explained, although subsequent sequencing has expanded the spectrum. (chung2010phenotypiccharacteristicsof pages 1-2, malikova2014novelinsightinto pages 7-8)

Among 95 Turkish children with unexplained PAI, sequencing diagnosed 77 (81%): MC2R 25, MRAP 9, NNT 7, CYP11A1 9, STAR 11, with additional non-FGD genes. Among 155 UK pediatric unresolved-PAI referrals, 103 (66.5%) received a diagnosis; MC2R was most frequent at 30/155 (19.4%). These are strong arguments for sequencing but not epidemiologic prevalence estimates. (guran2016rarecausesof pages 1-2, buonocore2021geneticanalysisof pages 1-2)

### Mendelian properties

- **Inheritance:** autosomal recessive for classic MC2R/MRAP FGD and most expanded FGD genes.
- **Recurrence risk:** for two confirmed heterozygous parents, each pregnancy has 25% affected, 50% carrier, and 25% unaffected/noncarrier probability.
- **Penetrance:** appears high for clearly damaging biallelic variants but has not been quantified uniformly; age and severity vary.
- **Expressivity:** variable, especially for missense or hypomorphic alleles and partial STAR/CYP11A1 disease.
- **Anticipation:** not expected or reported.
- **Mosaicism:** no established FGD-specific germline-mosaicism rate; residual recurrence risk after an apparently de novo finding should be discussed conventionally.
- **Founder effects:** MC2R p.Ser74Ile in Irish/Scottish ancestry and regional Turkish CYP11A1/MRAP variants are documented examples. (guran2016rarecausesof pages 6-7, buonocore2021geneticanalysisof pages 5-6)
- **Sex:** both sexes are genetically susceptible. Sex-specific consequences arise from gonadal steroidogenic involvement, particularly NNT-associated male infertility.

---

## 10. Diagnostics

### Clinical and biochemical pathway

1. **Suspect FGD** in a neonate or child with hyperpigmentation, recurrent fasting/illness hypoglycemia, unexplained seizures, failure to thrive, shock, or family history.
2. Before steroids if clinically safe, measure serum cortisol and plasma ACTH, glucose, sodium, potassium, bicarbonate, renin, and aldosterone. Do not delay emergency treatment to obtain testing.
3. Typical classic FGD: very low cortisol, markedly elevated ACTH, normal electrolytes, and preserved renin/aldosterone. Normal 17-hydroxyprogesterone and androgens help distinguish 21-hydroxylase deficiency. (refaei2018familialglucocorticoiddeficiency pages 1-2, refaei2018familialglucocorticoiddeficiency pages 2-2)
4. If basal results are equivocal, perform a standard ACTH/cosyntropin stimulation test; an attenuated cortisol response supports primary adrenal insufficiency. (maharaj2019predictedbenignand pages 3-3)
5. Assess mineralocorticoid function repeatedly because partial steroidogenic defects may salt-waste and some children receive fludrocortisone initially.
6. Evaluate differential diagnoses and proceed to molecular testing.

No imaging, biopsy, EEG, EMG, or adrenal histopathology is required routinely. Imaging is directed by differential diagnosis or complications—for example, testicular ultrasonography in postpubertal NNT deficiency. (ferreux2023testicularimpairmentin pages 1-2, ferreux2023testicularimpairmentin pages 6-7)

### Genetic testing strategy

A practical first-line test is a **next-generation sequencing pediatric PAI/ACTH-resistance panel** including at least MC2R, MRAP, NNT, TXNRD2, STAR, CYP11A1, AAAS, MCM4 and broader PAI genes such as NR0B1, ABCD1, NR5A1, SAMD9, SGPL1, and CDKN1C. Copy-number calling should be included. The Turkish study achieved an 81% yield with targeted NGS, while the UK series demonstrated that NGS improves yield where many genes overlap phenotypically. (guran2016rarecausesof pages 1-2, buonocore2021geneticanalysisof pages 1-2)

Population-specific single-variant testing may be economical when ancestry and phenotype strongly indicate a founder allele; three recurrent variants would have diagnosed 26% of families in the Turkish cohort. This should not replace panel analysis after a negative result. (guran2016rarecausesof pages 6-7)

If panel testing is negative, use trio WES or WGS, with reanalysis, deletion/duplication analysis, deep-intronic interrogation, and RNA studies. RNA sequencing or targeted transcript analysis is particularly useful for possible CYP11A1 splice variants. CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion assays are not routine unless another phenotype indicates them. (maharaj2019predictedbenignand pages 3-3)

### Differential diagnosis

Important alternatives include congenital adrenal hyperplasia; autoimmune Addison disease; X-linked adrenoleukodystrophy; NR0B1-related adrenal hypoplasia; Triple A syndrome; MIRAGE syndrome; mitochondrial and metabolic disease; infection/hemorrhage; and secondary/tertiary adrenal insufficiency. Alacrima and achalasia point toward AAAS; neurologic deterioration can suggest Triple A or adrenoleukodystrophy; genital anomalies, salt wasting, or gonadal dysfunction suggest a broader steroidogenic defect. (refaei2018familialglucocorticoiddeficiency pages 2-2, guran2016rarecausesof pages 1-2, buonocore2021geneticanalysisof pages 1-2)

### Screening

FGD is not part of routine newborn screening. Once a familial genotype is known, cascade testing, carrier testing, prenatal diagnosis, and preimplantation genetic testing are technically feasible. Biochemical testing should accompany predictive testing where age-dependent presentation remains possible.

---

## 11. Outcome and prognosis

Untreated FGD can cause recurrent adrenal crises, hypoglycemic seizures, irreversible neurologic injury, shock, and death. Early diagnosis and reliable glucocorticoid replacement generally produce a favorable endocrine prognosis, reverse hyperpigmentation, normalize growth velocity, and prevent most crises. (chung2010phenotypiccharacteristicsof pages 4-5, refaei2018familialglucocorticoiddeficiency pages 1-2, refaei2018familialglucocorticoiddeficiency pages 2-2)

No valid FGD-specific 5-year survival, 10-year survival, life-expectancy, mortality-rate, disability, or quality-of-life statistic was found. Prognosis is driven by age at diagnosis, severity and duration of hypoglycemia, treatment adherence, emergency preparedness, access to injectable hydrocortisone, and genotype-specific extra-adrenal disease.

NNT deficiency may carry a distinct fertility prognosis despite well-controlled adrenal disease. In the 35-year-old man reported in 2023, eight months of intensified glucocorticoid treatment neither reduced the testicular adrenal-rest tumor nor restored sperm production; bilateral Sertoli-cell-only syndrome indicated irreversible germ-cell loss. The authors called this the first direct evidence of complete germ-line loss in an azoospermic NNT-deficient man. (ferreux2023testicularimpairmentin pages 1-2)

---

## 12. Treatment

### Standard pharmacotherapy

**Hydrocortisone** is first-line lifelong replacement in children because it replaces deficient cortisol and has less growth-suppressive potency than long-acting glucocorticoids. A reported maintenance regimen was approximately **10 mg/m²/day**, divided through the day and individualized clinically. Adequate therapy improves pigmentation and suppresses excessive ACTH, although complete ACTH normalization should not be pursued at the cost of glucocorticoid overtreatment. (refaei2018familialglucocorticoiddeficiency pages 1-2)

Suggested annotations:

- Hydrocortisone: **CHEBI:17650**; NCIt concepts for hydrocortisone/glucocorticoid replacement should be release-verified.
- Fludrocortisone: NCIt drug concept should be verified; indicated only for documented mineralocorticoid deficiency, salt wasting, or persistently abnormal renin/electrolytes.

Seven MC2R patients in the UK cohort initially received mineralocorticoid, and three later discontinued it after the molecular diagnosis clarified classic FGD physiology. This illustrates a real-world benefit of genotype-guided management. (buonocore2021geneticanalysisof pages 5-6)

### Stress and emergency treatment

During febrile illness, significant injury, surgery, or systemic stress, hydrocortisone must be increased according to an adrenal-insufficiency sick-day protocol. One case report instructed doubling the dose with temperature above 38.5°C. Vomiting, severe weakness, altered consciousness, hypoglycemia, or shock requires immediate parenteral hydrocortisone, glucose as needed, isotonic fluid resuscitation, and emergency assessment. Families need injection training, an emergency card/medical alert, and medication supplies at home and school. (refaei2018familialglucocorticoiddeficiency pages 2-2)

### Genotype-specific supportive care

- **NNT:** monitor puberty, gonadotropins, testosterone/estradiol as appropriate, semen analysis, and testicular ultrasound. Discuss sperm cryopreservation or testicular sperm extraction early, before progressive loss. (ferreux2023testicularimpairmentin pages 1-2, ferreux2023testicularimpairmentin pages 6-7)
- **Partial STAR/CYP11A1:** monitor renin, aldosterone, electrolytes, puberty, genital development, and fertility; add mineralocorticoid when indicated. (guran2016rarecausesof pages 1-2, guran2016rarecausesof pages 4-6)
- **MCM4/AAAS phenocopies:** provide syndrome-specific immune, neurologic, gastrointestinal, or ophthalmic surveillance.

### Advanced and experimental treatments

No approved gene therapy, CRISPR treatment, RNA therapy, cell therapy, immunotherapy, or surgery corrects classic FGD. Surgery is not a treatment for adrenal ACTH resistance. Modified-release hydrocortisone and continuous subcutaneous infusion are being studied or used in broader adrenal insufficiency, but disease-specific efficacy in FGD is unproven.

The ClinicalTrials.gov search found adrenal-insufficiency formulation or replacement studies, but **no FGD-specific interventional study**. Therefore, trials such as NCT06435481 (pediatric oral hydrocortisone formulations) are indirect and should not be presented as FGD trials.

---

## 13. Prevention

**Primary prevention:** there is no lifestyle or immunization strategy that prevents an inherited biallelic disorder. Reproductive options include carrier testing of relatives, genetic counseling, prenatal diagnosis, and preimplantation genetic testing.

**Secondary prevention:** cascade testing and early biochemical assessment of at-risk siblings can detect disease before severe hypoglycemia or crisis. Molecular diagnosis also supports presymptomatic testing and personalized mineralocorticoid decisions. (guran2016rarecausesof pages 1-2)

**Tertiary prevention:** daily replacement, sick-day dosing, avoidance of prolonged fasting, immediate management of vomiting, emergency injectable hydrocortisone, medical identification, school/work action plans, and perioperative steroid coverage prevent crisis and neurologic injury. In NNT disease, puberty-onward fertility monitoring and early cryopreservation seek to prevent irreversible reproductive loss. (refaei2018familialglucocorticoiddeficiency pages 2-2, ferreux2023testicularimpairmentin pages 1-2, ferreux2023testicularimpairmentin pages 6-7)

Routine vaccination should follow standard schedules; vaccines do not prevent FGD, although fever after vaccination may require ordinary sick-day management.

---

## 14. Other species and natural disease

No well-established naturally occurring companion-animal or wildlife disorder directly equivalent to human FGD was identified in the retrieved evidence. Accordingly, no defensible OMIA, breed/VBO, veterinary incidence, or zoonotic annotation can be supplied. FGD is not infectious and has no zoonotic transmission.

The relevant genes and mitochondrial redox systems are evolutionarily conserved. **Mus musculus** (NCBI Taxonomy **10090**) is the best-supported comparative species in the retrieved literature. Ortholog-specific NCBI Gene identifiers should be obtained directly from NCBI rather than inferred from the clinical papers.

---

## 15. Model organisms and experimental systems

### NNT-deficient mouse

NNT-deficient mice provide mechanistic support for gonadal oxidative injury. Reported findings include testicular atrophy, reduced seminiferous-tubule diameter, increased germ-cell degeneration, increased TUNEL-positive cells, and elevated 8-hydroxy-2′-deoxyguanosine. This model supports the NADPH–ROS–germ-cell-death chain observed in the 2023 human case. It does not fully establish the frequency or reversibility of human infertility. (ferreux2023testicularimpairmentin pages 6-7)

### Cellular and in-vitro systems

- MC2R/MRAP expression systems assess receptor trafficking, surface expression, ACTH binding, and cAMP signaling.
- Patient fibroblasts or engineered cells can assess mitochondrial ROS, NADPH-dependent antioxidant function, and apoptosis in NNT/TXNRD2 disease.
- Minigene and RNA assays are especially informative for CYP11A1 variants predicted to be benign or synonymous. (maharaj2019predictedbenignand pages 3-3)

No validated FGD adrenal organoid, patient-derived iPSC adrenal model, zebrafish disease model, or CRISPR screening platform was established from the retrieved literature. These remain promising research approaches rather than current clinical implementations.

---

## Recent developments and expert interpretation

The most clinically important recent evidence retrieved was Ferreux et al., published **March 2023**, DOI [10.1186/s12610-022-00176-6](https://doi.org/10.1186/s12610-022-00176-6). Its central conclusion was that NNT-associated disease may not remain adrenal-limited: progressive oxidative injury can destroy the male germ line even while adrenal replacement is adequate, so fertility surveillance should begin at puberty and preservation should be considered in early adulthood. (ferreux2023testicularimpairmentin pages 1-2, ferreux2023testicularimpairmentin pages 6-7)

No equally substantive FGD-specific 2024 cohort or therapeutic study was recovered. Thus, the current evidence base remains anchored by the **May 2010** FGD1/FGD2 phenotype study, DOI [10.1111/j.1365-2265.2009.03663.x](https://doi.org/10.1111/j.1365-2265.2009.03663.x); the **January 2016** Turkish nationwide cohort, DOI [10.1210/jc.2015-3250](https://doi.org/10.1210/jc.2015-3250); the **October 2019** CYP11A1 functional study, DOI [10.1210/js.2018-00130](https://doi.org/10.1210/js.2018-00130); and the **May 2021** UK 25-year genetic study, DOI [10.1210/jendso/bvab086](https://doi.org/10.1210/jendso/bvab086). (chung2010phenotypiccharacteristicsof pages 1-2, guran2016rarecausesof pages 1-2, maharaj2019predictedbenignand pages 3-3, buonocore2021geneticanalysisof pages 1-2)

Expert interpretation from these cohorts is consistent: phenotype alone can suggest a gene—very early onset for MRAP, tall stature for MC2R, ketotic hypoglycemia for partial STAR/CYP11A1, and postpubertal gonadal disease for NNT—but overlapping presentations make multigene sequencing essential. Molecular diagnosis is not merely descriptive: it guides mineralocorticoid use, anticipatory surveillance, reproductive counseling, and presymptomatic family testing. (guran2016rarecausesof pages 1-2, buonocore2021geneticanalysisof pages 11-12, buonocore2021geneticanalysisof pages 2-3)

## Evidence limitations

1. FGD is so rare that phenotype frequencies, penetrance, population prevalence, mortality, and quality of life remain poorly quantified.
2. Large sequencing cohorts combine classical FGD with broader pediatric primary adrenal insufficiency; their gene percentages are referral-cohort statistics.
3. Some requested identifiers, HGNC IDs, current ClinVar assertions, gnomAD frequencies, and ontology codes were not present in the retrieved primary literature and require direct, release-specific database validation.
4. Direct abstract quotations were limited to short passages to preserve accuracy; PMIDs were not exposed in the retrieved records, so DOI URLs are supplied rather than guessed PMIDs.
5. Disease-specific advanced-omics, natural-animal-disease, and interventional-trial evidence is currently absent or insufficient.

References

1. (chung2010phenotypiccharacteristicsof pages 1-2): Teng‐Teng L. L. Chung, Li F. Chan, Louise A. Metherell, and Adrian J. L. Clark. Phenotypic characteristics of familial glucocorticoid deficiency (fgd) type 1 and 2. Clinical Endocrinology, 72:589-594, May 2010. URL: https://doi.org/10.1111/j.1365-2265.2009.03663.x, doi:10.1111/j.1365-2265.2009.03663.x. This article has 110 citations and is from a peer-reviewed journal.

2. (malikova2014novelinsightinto pages 7-8): Jana Malikova and Christa Flück. Novel insight into etiology, diagnosis and management of primary adrenal insufficiency. Hormone Research in Paediatrics, 82:145-157, Aug 2014. URL: https://doi.org/10.1159/000363107, doi:10.1159/000363107. This article has 73 citations and is from a peer-reviewed journal.

3. (guran2016rarecausesof pages 4-6): Tulay Guran, Federica Buonocore, Nurcin Saka, Mehmet Nuri Ozbek, Zehra Aycan, Abdullah Bereket, Firdevs Bas, Sukran Darcan, Aysun Bideci, Ayla Guven, Korcan Demir, Aysehan Akinci, Muammer Buyukinan, Banu Kucukemre Aydin, Serap Turan, Sebahat Yilmaz Agladioglu, Zeynep Atay, Zehra Yavas Abali, Omer Tarim, Gonul Catli, Bilgin Yuksel, Teoman Akcay, Metin Yildiz, Samim Ozen, Esra Doger, Huseyin Demirbilek, Ahmet Ucar, Emregul Isik, Bayram Ozhan, Semih Bolu, Ilker Tolga Ozgen, Jenifer P. Suntharalingham, and John C. Achermann. Rare causes of primary adrenal insufficiency: genetic and clinical characterization of a large nationwide cohort. The Journal of Clinical Endocrinology &amp; Metabolism, 101:284-292, Jan 2016. URL: https://doi.org/10.1210/jc.2015-3250, doi:10.1210/jc.2015-3250. This article has 223 citations.

4. (refaei2018familialglucocorticoiddeficiency pages 2-2): A. Refaei, Amer O. Al-Ali, M. Soeid, N. A. Jurayyan, B. Alenazi, and Taleb Ra. Familial glucocorticoid deficiency presenting as progressive hyperpigmentation: a case report. journal of Clinical Case Reports, 8:1-2, May 2018. URL: https://doi.org/10.4172/2165-7920.10001120, doi:10.4172/2165-7920.10001120. This article has 0 citations.

5. (malikova2014novelinsightinto pages 11-12): Jana Malikova and Christa Flück. Novel insight into etiology, diagnosis and management of primary adrenal insufficiency. Hormone Research in Paediatrics, 82:145-157, Aug 2014. URL: https://doi.org/10.1159/000363107, doi:10.1159/000363107. This article has 73 citations and is from a peer-reviewed journal.

6. (guran2016rarecausesof pages 6-7): Tulay Guran, Federica Buonocore, Nurcin Saka, Mehmet Nuri Ozbek, Zehra Aycan, Abdullah Bereket, Firdevs Bas, Sukran Darcan, Aysun Bideci, Ayla Guven, Korcan Demir, Aysehan Akinci, Muammer Buyukinan, Banu Kucukemre Aydin, Serap Turan, Sebahat Yilmaz Agladioglu, Zeynep Atay, Zehra Yavas Abali, Omer Tarim, Gonul Catli, Bilgin Yuksel, Teoman Akcay, Metin Yildiz, Samim Ozen, Esra Doger, Huseyin Demirbilek, Ahmet Ucar, Emregul Isik, Bayram Ozhan, Semih Bolu, Ilker Tolga Ozgen, Jenifer P. Suntharalingham, and John C. Achermann. Rare causes of primary adrenal insufficiency: genetic and clinical characterization of a large nationwide cohort. The Journal of Clinical Endocrinology &amp; Metabolism, 101:284-292, Jan 2016. URL: https://doi.org/10.1210/jc.2015-3250, doi:10.1210/jc.2015-3250. This article has 223 citations.

7. (guran2016rarecausesof pages 4-4): Tulay Guran, Federica Buonocore, Nurcin Saka, Mehmet Nuri Ozbek, Zehra Aycan, Abdullah Bereket, Firdevs Bas, Sukran Darcan, Aysun Bideci, Ayla Guven, Korcan Demir, Aysehan Akinci, Muammer Buyukinan, Banu Kucukemre Aydin, Serap Turan, Sebahat Yilmaz Agladioglu, Zeynep Atay, Zehra Yavas Abali, Omer Tarim, Gonul Catli, Bilgin Yuksel, Teoman Akcay, Metin Yildiz, Samim Ozen, Esra Doger, Huseyin Demirbilek, Ahmet Ucar, Emregul Isik, Bayram Ozhan, Semih Bolu, Ilker Tolga Ozgen, Jenifer P. Suntharalingham, and John C. Achermann. Rare causes of primary adrenal insufficiency: genetic and clinical characterization of a large nationwide cohort. The Journal of Clinical Endocrinology &amp; Metabolism, 101:284-292, Jan 2016. URL: https://doi.org/10.1210/jc.2015-3250, doi:10.1210/jc.2015-3250. This article has 223 citations.

8. (buonocore2021geneticanalysisof pages 5-6): Federica Buonocore, Avinaash Maharaj, Younus Qamar, Katrin Koehler, Jenifer P Suntharalingham, Li F Chan, Bruno Ferraz-de-Souza, Claire R Hughes, Lin Lin, Rathi Prasad, Jeremy Allgrove, Edward T Andrews, Charles R Buchanan, Tim D Cheetham, Elizabeth C Crowne, Justin H Davies, John W Gregory, Peter C Hindmarsh, Tony Hulse, Nils P Krone, Pratik Shah, M Guftar Shaikh, Catherine Roberts, Peter E Clayton, Mehul T Dattani, N Simon Thomas, Angela Huebner, Adrian J Clark, Louise A Metherell, and John C Achermann. Genetic analysis of pediatric primary adrenal insufficiency of unknown etiology: 25 years’ experience in the uk. Journal of the Endocrine Society, May 2021. URL: https://doi.org/10.1210/jendso/bvab086, doi:10.1210/jendso/bvab086. This article has 66 citations and is from a peer-reviewed journal.

9. (buonocore2021geneticanalysisof pages 11-12): Federica Buonocore, Avinaash Maharaj, Younus Qamar, Katrin Koehler, Jenifer P Suntharalingham, Li F Chan, Bruno Ferraz-de-Souza, Claire R Hughes, Lin Lin, Rathi Prasad, Jeremy Allgrove, Edward T Andrews, Charles R Buchanan, Tim D Cheetham, Elizabeth C Crowne, Justin H Davies, John W Gregory, Peter C Hindmarsh, Tony Hulse, Nils P Krone, Pratik Shah, M Guftar Shaikh, Catherine Roberts, Peter E Clayton, Mehul T Dattani, N Simon Thomas, Angela Huebner, Adrian J Clark, Louise A Metherell, and John C Achermann. Genetic analysis of pediatric primary adrenal insufficiency of unknown etiology: 25 years’ experience in the uk. Journal of the Endocrine Society, May 2021. URL: https://doi.org/10.1210/jendso/bvab086, doi:10.1210/jendso/bvab086. This article has 66 citations and is from a peer-reviewed journal.

10. (chung2010phenotypiccharacteristicsof pages 4-5): Teng‐Teng L. L. Chung, Li F. Chan, Louise A. Metherell, and Adrian J. L. Clark. Phenotypic characteristics of familial glucocorticoid deficiency (fgd) type 1 and 2. Clinical Endocrinology, 72:589-594, May 2010. URL: https://doi.org/10.1111/j.1365-2265.2009.03663.x, doi:10.1111/j.1365-2265.2009.03663.x. This article has 110 citations and is from a peer-reviewed journal.

11. (buonocore2021geneticanalysisof pages 1-2): Federica Buonocore, Avinaash Maharaj, Younus Qamar, Katrin Koehler, Jenifer P Suntharalingham, Li F Chan, Bruno Ferraz-de-Souza, Claire R Hughes, Lin Lin, Rathi Prasad, Jeremy Allgrove, Edward T Andrews, Charles R Buchanan, Tim D Cheetham, Elizabeth C Crowne, Justin H Davies, John W Gregory, Peter C Hindmarsh, Tony Hulse, Nils P Krone, Pratik Shah, M Guftar Shaikh, Catherine Roberts, Peter E Clayton, Mehul T Dattani, N Simon Thomas, Angela Huebner, Adrian J Clark, Louise A Metherell, and John C Achermann. Genetic analysis of pediatric primary adrenal insufficiency of unknown etiology: 25 years’ experience in the uk. Journal of the Endocrine Society, May 2021. URL: https://doi.org/10.1210/jendso/bvab086, doi:10.1210/jendso/bvab086. This article has 66 citations and is from a peer-reviewed journal.

12. (refaei2018familialglucocorticoiddeficiency pages 1-2): A. Refaei, Amer O. Al-Ali, M. Soeid, N. A. Jurayyan, B. Alenazi, and Taleb Ra. Familial glucocorticoid deficiency presenting as progressive hyperpigmentation: a case report. journal of Clinical Case Reports, 8:1-2, May 2018. URL: https://doi.org/10.4172/2165-7920.10001120, doi:10.4172/2165-7920.10001120. This article has 0 citations.

13. (guran2016rarecausesof pages 1-2): Tulay Guran, Federica Buonocore, Nurcin Saka, Mehmet Nuri Ozbek, Zehra Aycan, Abdullah Bereket, Firdevs Bas, Sukran Darcan, Aysun Bideci, Ayla Guven, Korcan Demir, Aysehan Akinci, Muammer Buyukinan, Banu Kucukemre Aydin, Serap Turan, Sebahat Yilmaz Agladioglu, Zeynep Atay, Zehra Yavas Abali, Omer Tarim, Gonul Catli, Bilgin Yuksel, Teoman Akcay, Metin Yildiz, Samim Ozen, Esra Doger, Huseyin Demirbilek, Ahmet Ucar, Emregul Isik, Bayram Ozhan, Semih Bolu, Ilker Tolga Ozgen, Jenifer P. Suntharalingham, and John C. Achermann. Rare causes of primary adrenal insufficiency: genetic and clinical characterization of a large nationwide cohort. The Journal of Clinical Endocrinology &amp; Metabolism, 101:284-292, Jan 2016. URL: https://doi.org/10.1210/jc.2015-3250, doi:10.1210/jc.2015-3250. This article has 223 citations.

14. (ferreux2023testicularimpairmentin pages 1-2): Lucile Ferreux, Yasmine Boumerdassi, Emmanuel Dulioust, Xavier Bertagna, Florence Roucher-Boulez, Mathilde Bourdon, Nicolas Thiounn, and Catherine Patrat. Testicular impairment in primary adrenal insufficiency caused by nicotinamide nucleotide transhydrogenase (nnt) deficiency - a case report: implication of oxidative stress and importance of fertility preservation. Basic and Clinical Andrology, Mar 2023. URL: https://doi.org/10.1186/s12610-022-00176-6, doi:10.1186/s12610-022-00176-6. This article has 3 citations.

15. (ferreux2023testicularimpairmentin pages 6-7): Lucile Ferreux, Yasmine Boumerdassi, Emmanuel Dulioust, Xavier Bertagna, Florence Roucher-Boulez, Mathilde Bourdon, Nicolas Thiounn, and Catherine Patrat. Testicular impairment in primary adrenal insufficiency caused by nicotinamide nucleotide transhydrogenase (nnt) deficiency - a case report: implication of oxidative stress and importance of fertility preservation. Basic and Clinical Andrology, Mar 2023. URL: https://doi.org/10.1186/s12610-022-00176-6, doi:10.1186/s12610-022-00176-6. This article has 3 citations.

16. (buonocore2021geneticanalysisof pages 2-3): Federica Buonocore, Avinaash Maharaj, Younus Qamar, Katrin Koehler, Jenifer P Suntharalingham, Li F Chan, Bruno Ferraz-de-Souza, Claire R Hughes, Lin Lin, Rathi Prasad, Jeremy Allgrove, Edward T Andrews, Charles R Buchanan, Tim D Cheetham, Elizabeth C Crowne, Justin H Davies, John W Gregory, Peter C Hindmarsh, Tony Hulse, Nils P Krone, Pratik Shah, M Guftar Shaikh, Catherine Roberts, Peter E Clayton, Mehul T Dattani, N Simon Thomas, Angela Huebner, Adrian J Clark, Louise A Metherell, and John C Achermann. Genetic analysis of pediatric primary adrenal insufficiency of unknown etiology: 25 years’ experience in the uk. Journal of the Endocrine Society, May 2021. URL: https://doi.org/10.1210/jendso/bvab086, doi:10.1210/jendso/bvab086. This article has 66 citations and is from a peer-reviewed journal.

17. (maharaj2019predictedbenignand pages 3-3): A. Maharaj, Federica Buonocore, E. Meimaridou, G. Ruiz-Babot, L. Guasti, Hwei-Ming Peng, Cameron P Capper, Neikelyn Burgos-Tirado, R. Prasad, C. Hughes, Ashwini Maudhoo, E. Crowne, T. Cheetham, C. Brain, Jenifer P. Suntharalingham, Niccolò Striglioni, B. Yuksel, F. Gurbuz, Sangay Gupta, R. Lindsay, R. Couch, H. Spoudeas, T. Guran, S. Johnson, D. Fowler, L. Conwell, A. McInerney-Leo, D. Drui, B. Cariou, J. López-Siguero, M. Harris, E. Duncan, P. Hindmarsh, R. Auchus, M. Donaldson, J. Achermann, and L. Metherell. Predicted benign and synonymous variants in cyp11a1 cause primary adrenal insufficiency through missplicing. Journal of the Endocrine Society, 3:201-221, Oct 2019. URL: https://doi.org/10.1210/js.2018-00130, doi:10.1210/js.2018-00130. This article has 30 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Familial_Glucocorticoid_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.