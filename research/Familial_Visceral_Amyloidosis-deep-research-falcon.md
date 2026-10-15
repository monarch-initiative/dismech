---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T16:54:46.655710'
end_time: '2026-08-28T17:07:40.192421'
duration_seconds: 773.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Visceral Amyloidosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 19
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Familial_Visceral_Amyloidosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Visceral Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Visceral Amyloidosis** covering all of the
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
- **Disease Name:** Familial Visceral Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Visceral Amyloidosis** covering all of the
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


# Familial Visceral Amyloidosis: Disease-Characteristics Report

## Executive summary and curation warning

**Familial visceral amyloidosis (FVA; MONDO:0007099)** is best treated as a **legacy umbrella concept**, not as one molecularly uniform disorder. Current protein-based nomenclature divides it into hereditary systemic amyloidoses according to the fibril precursor—principally fibrinogen Aα-chain (**AFib; FGA**), apolipoprotein A-I (**AApoAI; APOA1**), lysozyme (**ALys; LYZ**), apolipoprotein A-II (**AApoAII; APOA2**), and exceptionally β2-microglobulin (**AB2M; B2M**). Open Targets associates the exact MONDO entity with FGA, APOA1, LYZ, APOA2, and B2M. Hereditary transthyretin amyloidosis should be represented separately rather than automatically merged into this entry. (OpenTargets Search: familial visceral amyloidosis)

The unifying lesion is extracellular deposition of insoluble, cross-β-sheet-rich fibrils derived from a circulating mutant protein. Organ tropism and prognosis are strongly protein- and variant-dependent: AFib and AApoAII are predominantly renal; AApoAI commonly affects kidney, liver, and heart; ALys may be gastrointestinal, renal, or hepatic; and B2M p.Asp76Asn causes visceral disease distinct from dialysis-related β2-microglobulin amyloidosis. The disease-level record should therefore point to molecular subtype records rather than assign one phenotype frequency or prognosis to all FVA.

| Subtype | Inheritance / representative variants | Dominant organs and phenotype | Natural-history statistics | Definitive diagnosis | Treatment / evidence gaps |
|---|---|---|---|---|---|
| Familial visceral amyloidosis (MONDO:0007099) | Legacy/umbrella Mendelian systemic amyloidosis concept rather than a single molecular disease; associated targets include **FGA, APOA1, LYZ, APOA2, B2M** (OpenTargets Search: familial visceral amyloidosis) | Multivisceral amyloid deposition, but organ tropism differs strongly by subtype: kidney-predominant in AFib and many AApoAII cases; kidney/liver/heart in AApoAI; GI-predominant or renal/hepatic in ALys; visceral non-musculoskeletal pattern in hereditary B2M D76N (OpenTargets Search: familial visceral amyloidosis, stoppini2015systemicamyloidosislessons pages 1-2) | No unified epidemiology or prognosis for the umbrella entity; evidence must be interpreted at subtype level (OpenTargets Search: familial visceral amyloidosis) | Requires amyloid confirmation and subtype assignment; mass-spectrometry typing plus germline sequencing are central because hereditary cases may be misdiagnosed as AL (OpenTargets Search: familial visceral amyloidosis) | No umbrella-specific therapy; management is subtype- and organ-specific, and evidence is sparse outside AFib and AApoAI transplant series (OpenTargets Search: familial visceral amyloidosis, cohen2024prognosticmarkersand pages 194-199) |
| AFib / FGA | Usually autosomal dominant; representative variants include **E526V/p.Glu545Val**, **R554L**, and frameshift variants such as **c.1673del (p.Lys558Argfs*10)** and **c.1639delA (p.Arg547Glyfs*21)** (he2025clinicalmanifestationsdiagnosis pages 1-2, escaleira2022fibrinogenaalphachain pages 14-17) | Predominantly renal amyloidosis with proteinuria, edema, hypertension, progressive CKD/ESKD; extra-renal liver/cardiac involvement can occur but is less prominent/variable (he2025clinicalmanifestationsdiagnosis pages 1-2, escaleira2022fibrinogenaalphachain pages 14-17) | In 32 French patients, median diagnosis age **51.5 y**; proteinuria **93%**, hypertension **83%**, kidney failure **68%**; kidney disease onset averaged **57 y** for E526V, **45 y** for R554L, **24.5 y** for frameshifts. In a 46-case review, **21.7%** reached ESRD/RRT within 1 year and **39.1%** within 1–5 years (he2025clinicalmanifestationsdiagnosis pages 1-2) | Renal biopsy with Congo red-positive deposits, proteomic typing/mass spectrometry, and **FGA** sequencing; careful review needed because private frameshifts can complicate typing (he2025clinicalmanifestationsdiagnosis pages 1-2) | Supportive antiproteinuric/antihypertensive care; dialysis for ESKD. **Kidney transplant** viable especially for E526V; recurrence after KT lower in E526V than non-E526V (**22% vs 83%**, P=0.03). **Liver-kidney transplant** may be preferred for frameshift/non-E526V disease; no recurrence observed after LKT in the French series. No approved subtype-specific drug therapy identified (he2025clinicalmanifestationsdiagnosis pages 1-2) |
| AApoAI / APOA1 | Usually autosomal dominant; heterogeneous mutations including common **Gly26Arg** and novel **c.251T>C** (Leu→Pro in mature ApoA-I); 2024 report suggests a possible **autosomal recessive** cardiac form with **p.Leu202Arg** in one homozygous patient (cohen2024prognosticmarkersand pages 194-199, yagi2024theapoa1p.leu202arg pages 1-3, moutafi2019anewgenetic pages 1-2) | Kidneys, liver, and heart are major targets; phenotype depends partly on variant. Can present with slowly progressive renal disease, hepatomegaly, infiltrative liver disease, hypogonadism, and less often cardiac amyloidosis (cohen2024prognosticmarkersand pages 194-199, yagi2024theapoa1p.leu202arg pages 1-3, moutafi2019anewgenetic pages 1-2) | UK cohort: **57 patients**, **14 APOA1 mutations**; median presentation age **43 y**; median delay to referral **3 y**. Organ involvement: kidneys **81%**, liver **67%**, heart **28%**. For renal disease, median creatinine **159 µmol/L**, median proteinuria **0.3 g/24 h**, median time from diagnosis to ESRD **15.0 y** (95% CI **10.0–20.0**). Renal amyloidosis was universal with **Gly26Arg (n=28)** (cohen2024prognosticmarkersand pages 194-199) | Tissue biopsy with Congo red; immunoelectron microscopy or LMD/LC-MS/MS for amyloid typing; germline **APOA1** sequencing for confirmation, especially in atypical liver/cardiac presentations (yagi2024theapoa1p.leu202arg pages 1-3, moutafi2019anewgenetic pages 1-2) | Transplant outcomes are relatively favorable: in the UK cohort, **18** underwent renal transplantation, including **5 LKT** and **2 HKT**; median renal allograft survival **22.0 y** (13.0–31.0). Liver transplantation led to regression of amyloid on serial SAP scintigraphy in all 4 imaged cases. No approved APOA1-targeted pharmacologic/gene-silencing therapy identified (cohen2024prognosticmarkersand pages 194-199) |
| ALys / LYZ | Autosomal dominant hereditary systemic non-neuropathic amyloidosis; representative variants include **Asp67His** and **p.Trp82Arg** (OpenTargets Search: familial visceral amyloidosis) | Heterogeneous phenotype with gastrointestinal, renal, and hepatic involvement; one 9-member family with **p.Trp82Arg** had predominantly mild upper-GI symptoms and some inflammatory-bowel-disease-like colitis without other organ involvement (OpenTargets Search: familial visceral amyloidosis) | In the reported family, **9** affected members carried heterozygous **p.Trp82Arg**; **8/9** had nonspecific upper-GI symptoms and **3/9** had rectocolic inflammation suggestive of inflammatory bowel disease. Older evidence notes some **Asp67His** and APOA1 Gly26Arg cases show slowly progressive renal impairment (OpenTargets Search: familial visceral amyloidosis) | Histologic confirmation of amyloid plus targeted **LYZ** mutation testing when GI disease is atypical/treatment-resistant and familial; subtype confirmation is important because hereditary amyloidosis may be mistaken for AL (OpenTargets Search: familial visceral amyloidosis) | No established disease-modifying drug therapy identified in gathered evidence. Management appears supportive and organ-directed; evidence for transplantation or systematic outcome data is limited in the gathered set (OpenTargets Search: familial visceral amyloidosis) |
| AApoAII / APOA2 | Hereditary systemic amyloidosis due to stop-codon mutations creating a **21-amino-acid C-terminal extension**; representative variants include **Stop78Ser** and **Stop78Arg** (chabert2019atransgenicmouse pages 1-2) | Primarily renal amyloidosis/proteinuria progressing to nephrotic syndrome and CKD; human kindreds also show systemic involvement, while the transgenic model developed renal, liver, heart, and spleen amyloid (chabert2019atransgenicmouse pages 1-2) | Human report: proteinuria noted at **42 y** in a **46-year-old** man with glomerular amyloid and heterozygous stop-codon mutation. Model-derived human summary in Chabert notes ~**70%** of patients develop nephrotic syndrome progressing to CKD/ESRD, but subtype-specific human cohorts remain very small (chabert2019atransgenicmouse pages 1-2) | Renal biopsy with amyloid typing plus **APOA2** sequencing; mechanism is supported by demonstration of variant plasma apoA-II carrying a C-terminal extension (chabert2019atransgenicmouse pages 1-2) | No approved subtype-specific drug therapy identified. Evidence base is limited to rare kindreds/case reports and one transgenic model; transplant and long-term human outcome data are sparse in the gathered evidence (chabert2019atransgenicmouse pages 1-2) |
| AB2M / B2M | Very rare hereditary systemic amyloidosis due to **D76N**; distinct from dialysis-related wild-type β2-microglobulin amyloidosis (stoppini2015systemicamyloidosislessons pages 1-2) | Multivisceral involvement including **liver, kidney, heart**; notably **spares bones and ligaments**, unlike dialysis-related β2M amyloidosis (stoppini2015systemicamyloidosislessons pages 1-2) | Quantitative natural-history data were not found in the gathered evidence. Main established point is that hereditary **D76N** has a different tissue tropism from dialysis-related β2M disease (stoppini2015systemicamyloidosislessons pages 1-2) | Amyloid typing plus **B2M** sequencing are required to distinguish hereditary D76N disease from dialysis-related β2M amyloidosis; deposits in D76N reportedly lacked wild-type and N-terminally truncated β2M species seen in dialysis-related amyloid (stoppini2015systemicamyloidosislessons pages 1-2) | No established subtype-specific therapy or trial evidence identified in the gathered set. Evidence is limited to rare-family and mechanistic literature; prognosis and optimal intervention remain poorly defined (stoppini2015systemicamyloidosislessons pages 1-2) |


*Table: This table summarizes familial visceral amyloidosis as a legacy umbrella entity and breaks down the main non-TTR hereditary subtypes by genotype, phenotype, natural history, diagnosis, and management evidence. It is useful for knowledge-base curation because prognosis and treatment differ substantially by subtype rather than by the umbrella term.*

## 1. Disease information

### Definition and synonyms

FVA comprises inherited protein-misfolding disorders in which germline variants render normally soluble plasma proteins amyloidogenic, causing systemic—especially visceral—deposition and progressive organ dysfunction. Appropriate synonyms include **familial visceral amyloidosis**, **hereditary visceral amyloidosis**, **hereditary non-neuropathic systemic amyloidosis**, and, more broadly but less precisely, **hereditary systemic amyloidosis**.

**Recommended identifier:** MONDO:0007099. A single reliable umbrella-level OMIM, Orphanet, MeSH, ICD-10, or ICD-11 identifier was not established from the retrieved evidence. Those systems generally code amyloidosis broadly or classify individual molecular forms. Do not infer unsupported cross-mappings; retain subtype-specific OMIM/Orphanet identifiers where independently verified.

This report is based on **aggregated disease-level literature**, including cohorts, systematic reviews, kindreds, case reports, pathology series, and experimental models—not individual EHR data.

### Evidence-source distinction

* **Human clinical:** strongest for AFib and AApoAI natural history and transplantation.
* **Human family/case evidence:** predominant for ALys, AApoAII, and hereditary B2M.
* **Model organism:** a human APOA2 Stop78Ser transgenic mouse reproduces systemic disease.
* **In vitro/structural:** supports variant destabilization, proteolytic fragmentation, and fibrillogenesis, but does not establish clinical penetrance by itself.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

The primary cause is a **germline amyloidogenic variant** in a secreted protein gene. Most established forms are autosomal dominant. Disease results from a toxic gain of protein aggregation rather than simple loss of normal protein function. Relevant genes retrieved for MONDO:0007099 are **FGA, APOA1, LYZ, APOA2, and B2M**. (OpenTargets Search: familial visceral amyloidosis)

Representative causal variants include:

* **FGA:** p.Glu545Val in current HGVS numbering, historically called E526V in the mature-chain convention; p.Arg554Leu; and C-terminal frameshifts such as c.1673del, p.Lys558Argfs*10. Variant class strongly influences age and progression. (he2025clinicalmanifestationsdiagnosis pages 1-2, escaleira2022fibrinogenaalphachain pages 14-17)
* **APOA1:** numerous predominantly heterozygous missense/indel variants, including p.Gly26Arg and a reported c.251T>C leucine-to-proline substitution. A 2024 report identified homozygous p.Leu202Arg in isolated cardiac amyloidosis, suggesting a possible recessive mechanism for that allele; one case does not establish general recessive inheritance. (cohen2024prognosticmarkersand pages 194-199, yagi2024theapoa1p.leu202arg pages 1-3, moutafi2019anewgenetic pages 1-2)
* **LYZ:** heterozygous variants including p.Asp67His and p.Trp82Arg. (OpenTargets Search: familial visceral amyloidosis)
* **APOA2:** stop-loss variants such as Stop78Ser and Stop78Arg create an abnormal 21-residue C-terminal extension. (chabert2019atransgenicmouse pages 1-2)
* **B2M:** p.Asp76Asn (D76N), an exceptionally rare familial systemic form distinct from wild-type dialysis-related amyloidosis. (stoppini2015systemicamyloidosislessons pages 1-2)

### Risk and modifier factors

The principal risk factors are carriage of a causal allele, increasing age, family history, and subtype-specific variant severity. In AFib, frameshift variants generally cause earlier, more aggressive renal disease than p.Glu545Val. In a 46-case review, women had earlier onset than men, although the biological basis and generalizability are uncertain. (he2025clinicalmanifestationsdiagnosis pages 1-2)

Founder or regional enrichment is plausible for FGA p.Glu545Val: shared haplotypes occur among Portuguese and Brazilian families, and this variant is especially relevant in parts of Europe. AFib is described as the most common hereditary renal amyloidosis in the United Kingdom/Europe, excluding ATTR. (escaleira2022fibrinogenaalphachain pages 14-17)

No validated modifier genes, protective alleles, epigenetic determinants, or reproducible environmental exposures were established. Normal fibrinogen concentration does not exclude AFib because amyloidogenicity reflects variant structure rather than overproduction. (escaleira2022fibrinogenaalphachain pages 14-17)

### Environmental and protective factors

No toxin, infection, smoking pattern, diet, alcohol exposure, occupation, or radiation exposure is known to cause these Mendelian forms. Renal function, blood pressure, coexisting diabetes, and age may influence organ reserve and observed progression but are not primary causes. There is no proven diet, supplement, exercise program, or drug that prevents fibril formation in asymptomatic carriers.

The clearest gene–environment interaction is **B2M context dependence**: wild-type β2-microglobulin produces dialysis-related, predominantly osteoarticular amyloidosis after prolonged renal replacement therapy, whereas germline D76N produces multivisceral amyloid without requiring dialysis and spares bones and ligaments. (stoppini2015systemicamyloidosislessons pages 1-2)

## 3. Phenotypes

### AFib/FGA

AFib usually presents in adulthood with proteinuria, edema, hypertension, progressive chronic kidney disease, and ultimately kidney failure. In a 32-patient French series, median diagnosis age was 51.5 years; proteinuria occurred in 93%, hypertension in 83%, and kidney failure in 68%. Average renal-disease onset was 57 years for E526V, 45 years for R554L, and 24.5 years for frameshift variants. (he2025clinicalmanifestationsdiagnosis pages 1-2)

A systematic review of 46 cases found proteinuria in all patients; 21.7% reached ESRD or renal replacement therapy within one year, 39.1% within one to five years, and only 8.7% remained free of ESRD/RRT beyond five years. Thus severity ranges from slowly progressive p.Glu545Val disease to rapidly progressive frameshift disease. (he2025clinicalmanifestationsdiagnosis pages 1-2)

Suggested HPO terms: **Proteinuria (HP:0000093), nephrotic syndrome (HP:0000100), chronic kidney disease (HP:0012622), end-stage renal disease (HP:0003774), edema (HP:0000969), hypertension (HP:0000822)**, and amyloidosis (HP:0011034). Quality-of-life effects include dialysis dependence, transplantation, fatigue, edema, medication burden, and reduced physical function; subtype-specific EQ-5D/SF-36 data were not found.

### AApoAI/APOA1

AApoAI has variable adult onset and variant-dependent kidney, liver, or cardiac disease. In the UK National Amyloidosis Centre cohort of 57 patients carrying 14 APOA1 mutations, median presentation age was 43 years; kidney, liver, and heart involvement occurred in 81%, 67%, and 28%, respectively. Renal involvement was universal among 28 p.Gly26Arg carriers. Median protein excretion was only 0.3 g/day despite renal amyloid, an important distinction from many AL/AA presentations. (cohen2024prognosticmarkersand pages 194-199)

Clinical manifestations include slowly progressive renal impairment, hepatomegaly, abnormal liver enzymes, infiltrative hepatic disease, cardiomyopathy, and occasional gonadal/endocrine involvement. One novel-variant case developed hepatomegaly followed by primary hypogonadism. (moutafi2019anewgenetic pages 1-2)

A 2024 homozygous p.Leu202Arg case developed heart failure beginning at 52 years, needed a pacemaker at 58, and at 69 had ejection fraction 40%, interventricular septal thickness 13 mm, BNP 154 pg/mL, and HDL-C 35 mg/dL; his heterozygous brother was clinically unaffected. (yagi2024theapoa1p.leu202arg pages 1-3)

Suggested HPO: **Hepatomegaly (HP:0002240), elevated hepatic transaminases (HP:0002910), cardiomyopathy (HP:0001638), heart failure (HP:0001635), left-ventricular hypertrophy (HP:0001712), conduction abnormality (HP:0001678), hypogonadism (HP:0000135)**, plus the renal terms above.

### ALys/LYZ

ALys is a rare systemic, usually non-neuropathic amyloidosis with heterogeneous gastrointestinal, renal, and hepatic manifestations. In a nine-member p.Trp82Arg family, all affected individuals had predominantly gastrointestinal disease: 8/9 had nonspecific upper-GI symptoms and 3/9 had rectocolic inflammation resembling inflammatory bowel disease; no other amyloid organ involvement was found. (OpenTargets Search: familial visceral amyloidosis)

Suggested HPO: **Abdominal pain (HP:0002027), chronic diarrhea (HP:0002014), gastritis (HP:0005268), inflammatory bowel disease (HP:0002037), gastrointestinal amyloidosis**, proteinuria, renal insufficiency, and hepatomegaly. Frequencies should not be generalized beyond the p.Trp82Arg kindred.

### AApoAII/APOA2

Human AApoAII generally causes proteinuria, glomerular amyloid, nephrotic syndrome, progressive CKD, and ESRD. A Stop78Ser proband developed proteinuria at 42 and was evaluated at 46. The abnormal stop-loss protein had a 21-amino-acid C-terminal extension, directly implicating the extension in amyloidogenesis. Model-informed summaries estimate nephrotic progression in approximately 70% of patients, but this estimate derives from very small kindreds and should be marked low confidence. (chabert2019atransgenicmouse pages 1-2)

### AB2M/B2M

D76N β2-microglobulin amyloidosis affects liver, kidney, heart, and other viscera but notably spares the bones and ligaments commonly involved in dialysis-related β2-microglobulin amyloidosis. Reliable phenotype frequencies and age distributions are unavailable because reported families are extremely few. (stoppini2015systemicamyloidosislessons pages 1-2)

## 4. Genetic and molecular information

These are **germline**, usually heterozygous variants. Somatic mutation, chromosomal aneuploidy, translocation, repeat expansion, and mitochondrial inheritance are not established causes. Most reported variants are missense, stop-loss, deletion/insertion, or frameshift alleles. Population frequencies are generally compatible with rarity; exact gnomAD frequencies were not available in the retrieved evidence and should be queried variant-by-variant before curation.

Functional consequence is a **neomorphic/toxic gain of aggregation**: altered stability, proteolytic susceptibility, charge, hydrophobic exposure, or C-terminal sequence permits self-assembly. APOA2 stop-loss alleles add 21 residues; FGA frameshifts replace the normal C terminus; APOA1 fibrils frequently contain N-terminal fragments; D76N changes β2-microglobulin stability and tissue tropism. (chabert2019atransgenicmouse pages 1-2, stoppini2015systemicamyloidosislessons pages 1-2, moutafi2019anewgenetic pages 1-2)

Variant classification must be performed independently under ACMG/AMP criteria. The 2024 APOA1 p.Leu202Arg report classified the allele as likely pathogenic and reported CADD Phred 29.4, but segregation was limited and the proposed recessive mechanism remains provisional. (yagi2024theapoa1p.leu202arg pages 1-3)

No reproducible modifier gene, disease-specific DNA-methylation signature, histone alteration, or large chromosomal abnormality was established.

## 5. Environmental information

Environmental, lifestyle, and infectious-agent fields are **not applicable as primary etiology**. Chronic inflammation causes AA amyloidosis and monoclonal plasma-cell disease causes AL amyloidosis, but these are differential diagnoses—not triggers for FVA. Long-term dialysis is causally relevant to acquired wild-type β2-microglobulin amyloidosis but not required for inherited D76N disease. (stoppini2015systemicamyloidosislessons pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream germline variant** in a secreted protein gene.
2. Hepatic or other physiological synthesis and release of the mutant precursor into blood.
3. Variant-dependent destabilization, abnormal proteolysis, or altered intermolecular interactions.
4. Oligomerization and formation of cross-β amyloid fibrils, often with serum amyloid P component and extracellular-matrix glycosaminoglycans.
5. Extracellular deposition in glomerular mesangium/capillary walls, interstitium, vessels, myocardium, liver, spleen, or GI wall.
6. Mechanical distortion, microvascular dysfunction, cellular stress, and impaired filtration/contractility/organ architecture.
7. Proteinuria, nephrotic syndrome, CKD/ESRD, restrictive or hypertrophic cardiac disease, hepatomegaly, or GI dysfunction.

D76N deposits lack the wild-type and N-terminally truncated β2-microglobulin species typical of dialysis-related deposits, supporting a distinct molecular assembly and explaining divergent visceral versus osteoarticular tropism. (stoppini2015systemicamyloidosislessons pages 1-2)

### Suggested ontology annotations

**GO biological process:** protein folding; protein misfolding; amyloid fibril formation; protein aggregation; extracellular-matrix organization; response to unfolded protein; glomerular filtration; lipid transport for APOA1/APOA2; fibrinogen complex biology for FGA.

**GO cellular component:** extracellular region, extracellular space, amyloid fibril, blood microparticle, high-density lipoprotein particle, fibrinogen complex.

**Cell Ontology suggestions:** hepatocyte (major source for FGA and apolipoproteins), kidney glomerular endothelial cell, podocyte, mesangial cell, cardiomyocyte, vascular endothelial cell, intestinal epithelial cell, macrophage. Amyloid is extracellular; these cells are sources, neighbors, or functionally injured populations rather than necessarily intracellular deposit-bearing cells.

No validated disease-specific single-cell atlas, spatial-transcriptomic signature, lipidomic/metabolomic diagnostic profile, CRISPR screen, or integrated multi-omics dataset was identified. Contemporary proteomics is clinically important for deposit typing rather than population-level molecular profiling.

## 7. Anatomy

**Primary organs:** kidney/glomerulus (AFib, AApoAII, many AApoAI/ALys cases), liver (AApoAI, ALys, B2M), heart/myocardium and conduction system (selected APOA1 variants and B2M), gastrointestinal tract (some LYZ variants), spleen and vasculature.

Suggested UBERON mappings: kidney, renal glomerulus, liver, heart, myocardium, gastrointestinal tract, stomach, colon, spleen, blood vessel, peripheral nerve, and testis where clinically involved. Lateralization is not relevant: systemic deposition is diffuse rather than unilateral.

Histologically, renal amyloid may occupy glomerular mesangium and subendothelial areas and may extend to vessels and tubulointerstitium. Amyloid fibrils are randomly arranged, approximately 8–12 nm in one AFib renal series, and show Congo-red positivity with apple-green birefringence under polarized light.

## 8. Temporal development

Onset is usually **insidious and adult**, with marked genotype dependence. AFib frameshifts can begin in adolescence or young adulthood; p.Glu545Val commonly presents later. AApoAI median presentation was 43 years, but cardiac p.Leu202Arg disease began at 52. (he2025clinicalmanifestationsdiagnosis pages 1-2, cohen2024prognosticmarkersand pages 194-199, yagi2024theapoa1p.leu202arg pages 1-3)

The course is chronic and progressive rather than episodic. A practical staging framework is:

1. asymptomatic carrier;
2. biomarker abnormality—proteinuria, reduced eGFR, abnormal liver tests, BNP/troponin rise;
3. clinically apparent single-organ amyloidosis;
4. multiorgan or advanced organ dysfunction;
5. ESRD, advanced heart failure, or transplant requirement.

Spontaneous remission is not documented. Removing the major hepatic source by liver transplantation can stop precursor production and permit partial deposit regression, but timing before irreversible organ failure is critical. AApoAI renal disease progressed to ESRD over a median 15 years, whereas many AFib cases progressed within five years. (he2025clinicalmanifestationsdiagnosis pages 1-2, cohen2024prognosticmarkersand pages 194-199)

## 9. Inheritance and population

Most forms are **autosomal dominant with age-dependent, incomplete penetrance and variable expressivity**. The homozygous APOA1 p.Leu202Arg report is a possible autosomal-recessive exception. No evidence supports anticipation, repeat expansion, or a systematic role for germline mosaicism. Consanguinity is relevant only to rare recessive hypotheses such as p.Leu202Arg. (yagi2024theapoa1p.leu202arg pages 1-3)

Reliable global incidence, prevalence, carrier frequency, sex ratio, and mortality rate for MONDO:0007099 are unavailable. The combined hereditary non-TTR forms are ultra-rare. AFib represented approximately 1.3% of renal amyloidosis cases in one Mayo Clinic context, but regional founder effects can produce much higher local proportions. (he2025clinicalmanifestationsdiagnosis pages 1-2)

AFib p.Glu545Val is enriched in European populations and has Portuguese/Brazilian founder haplotypes. A broader estimate that inherited forms account for roughly 10% of systemic amyloidosis is not specific to this MONDO entity and should not be entered as FVA prevalence. (escaleira2022fibrinogenaalphachain pages 14-17)

## 10. Diagnostics

### Recommended workflow

1. **Recognize the organ syndrome:** unexplained familial proteinuria/CKD, low-proteinuria renal dysfunction, hepatomegaly, infiltrative liver disease, cardiomyopathy, or familial refractory GI disease.
2. **Exclude common mimics:** serum and urine immunofixation plus serum free-light chains for AL; inflammatory evaluation for AA; TTR-focused imaging/genotyping when ATTR is suspected.
3. **Confirm amyloid:** biopsy affected tissue, or a lower-risk site where appropriate, with Congo-red staining and polarized-light birefringence. Electron microscopy may show nonbranching fibrils.
4. **Type the fibril protein:** laser-capture microdissection with LC-MS/MS is preferred where available; immunohistochemistry/immunoelectron microscopy can support typing but may be limited by antibody specificity.
5. **Confirm germline cause:** sequence the proteomically implicated gene and perform segregation/cascade testing. A broader hereditary-amyloidosis panel is appropriate if typing is equivocal or the phenotype is atypical.
6. **Stage organ disease:** urine protein, creatinine/eGFR, blood pressure, liver tests, ECG, echocardiography, cardiac MRI, BNP/NT-proBNP and troponin; GI endoscopy/biopsy when indicated.

The AFib review states directly: **“The diagnosis of this disease is primarily based on renal biopsy, mass spectrometry, and molecular gene detection.”** (publication online 2024; issue 2025; DOI below). (he2025clinicalmanifestationsdiagnosis pages 1-2)

Proteomics is essential because a coincidental monoclonal gammopathy can lead to erroneous AL diagnosis. The fibril protein—not merely the presence of a germline variant—must match the deposits. WES/WGS can identify unusual alleles but does not replace tissue typing. CMA, karyotyping, FISH, mtDNA analysis, and repeat-expansion tests are not routine.

### Differential diagnosis

AL amyloidosis; AA amyloidosis; ATTRv/ATTRwt; ALECT2; hereditary gelsolin/cystatin-C/apolipoprotein-C amyloidoses; diabetic and hypertensive nephropathy; membranous nephropathy; hereditary nephrotic syndromes; hypertrophic cardiomyopathy; storage disease; inflammatory bowel disease; and infiltrative liver disease.

### Screening

Population or newborn screening is not justified. **Cascade testing** of adult relatives after identification of a familial pathogenic variant is appropriate with genetic counseling. Baseline and periodic renal, cardiac, hepatic, and symptom-directed surveillance should begin before the family’s earliest usual onset. Exact surveillance intervals are not validated for these ultra-rare subtypes.

## 11. Outcome and prognosis

Prognosis is determined mainly by precursor, variant, organ involvement, renal stage, and cardiac disease. No unified five- or ten-year survival statistic exists.

* **AFib:** often progresses to ESRD; frameshifts and R554L are more aggressive than p.Glu545Val. In the 46-case synthesis, 60.8% reached ESRD/RRT within five years. (he2025clinicalmanifestationsdiagnosis pages 1-2)
* **AApoAI:** usually slower. Median time from diagnosis to ESRD was 15.0 years (95% CI 10.0–20.0). (cohen2024prognosticmarkersand pages 194-199)
* **ALys:** may remain organ-restricted and mild, as in the p.Trp82Arg GI family, but other variants cause severe renal/hepatic disease.
* **AApoAII:** substantial risk of nephrotic syndrome and ESRD, but estimates are imprecise.
* **B2M D76N:** prognosis is poorly quantified; cardiac and multivisceral involvement can be serious.

Disability arises from edema, fatigue, dietary and medication restrictions, dialysis, transplant complications, heart failure, arrhythmia, GI symptoms, and endocrine dysfunction. Validated FVA-specific patient-reported outcome datasets were not found.

## 12. Treatment

### General strategy

There is no approved umbrella-level pharmacotherapy and no established FGA-, APOA1-, LYZ-, APOA2-, or B2M-directed stabilizer, siRNA, ASO, or gene-editing therapy. ATTR drugs such as tafamidis, patisiran, vutrisiran, and inotersen should **not** be extrapolated to these proteins.

Supportive management includes renin–angiotensin-system blockade when tolerated, individualized SGLT2 inhibition in CKD, diuretics for edema/heart failure, blood-pressure control, avoidance of nephrotoxins, nutritional support, dialysis, arrhythmia management, and multidisciplinary amyloidosis follow-up. Evidence is largely observational.

Suggested NCIT intervention concepts: **Kidney Transplantation, Liver Transplantation, Combined Liver and Kidney Transplantation, Hemodialysis, Antihypertensive Therapy, Diuretic Therapy, Genetic Counseling**, and supportive care. Exact NCIT codes should be validated against the current NCIT release.

### Transplantation

For AFib, kidney transplantation is reasonable, especially for p.Glu545Val, but recurrence is expected because the liver continues producing mutant fibrinogen. In the French series, graft recurrence was lower for E526V than non-E526V variants (22% versus 83%; P=0.03), and graft loss occurred less often (33% versus 100%). No recurrence was seen after combined liver–kidney transplantation, supporting source-organ replacement for aggressive frameshift disease. (he2025clinicalmanifestationsdiagnosis pages 1-2)

For AApoAI, transplantation outcomes were encouraging. Among 57 patients, 18 underwent renal transplantation, including five combined liver–kidney and two heart–kidney procedures. Median renal allograft survival was 22 years; all four patients with serial serum amyloid-P scintigraphy after liver transplantation showed amyloid regression. (cohen2024prognosticmarkersand pages 194-199)

For ALys, AApoAII, and hereditary B2M, transplantation decisions are case-specific; robust comparative outcome data are absent.

### Trials and recent therapeutic development

The ClinicalTrials.gov search retrieved ATTR-focused or mixed-amyloidosis studies but no clearly subtype-specific interventional trial for FGA, APOA1, LYZ, APOA2, or hereditary B2M. This is an important negative finding: advanced RNA and CRISPR programs in ATTR do not yet represent real-world treatment for FVA.

## 13. Prevention

Primary prevention of spontaneous disease is not possible after inheriting a causal allele. Actionable measures are genetic counseling, cascade testing, informed reproductive planning, prenatal diagnosis, and preimplantation genetic testing where legally and ethically available. Secondary prevention consists of presymptomatic organ surveillance and early referral before irreversible CKD or cardiomyopathy. Tertiary prevention includes blood-pressure/proteinuria management, early transplant assessment, vaccination appropriate for CKD/transplant candidates, infection prevention, and cardiovascular risk management.

There is no vaccine, chemoprophylaxis, or validated behavioral intervention that prevents mutant-protein amyloid deposition.

## 14. Other species and natural disease

No well-established, naturally occurring veterinary disease that is directly homologous to human FGA-, LYZ-, or B2M-associated FVA was identified. Amyloidosis occurs widely in animals, but animal AA, AL, endocrine, and age-associated amyloidoses should not be conflated with this human Mendelian umbrella. APOA2-related amyloid occurs naturally in senescence-accelerated mouse strains, although its mechanism differs from human stop-loss AApoAII disease. Zoonotic transmission is not applicable.

Relevant taxonomy suggestions: **Homo sapiens—NCBI Taxon 9606; Mus musculus—10090**. No VBO breed mapping is applicable.

## 15. Model organisms

The strongest disease-specific model is a **transgenic Mus musculus expressing human APOA2 Stop78Ser** at physiological levels. All mice developed systemic amyloidosis; glomerular renal amyloid and renal insufficiency were prominent, with liver, heart, and spleen involvement. Deposits began at two months in high-expressing animals, renal insufficiency appeared after six months, and death began from six months. Full-length mature Stop78Ser ApoA-II was recovered as the fibril protein. (chabert2019atransgenicmouse pages 1-2)

This model reproduces early-onset, multiorgan human AApoAII and permits testing of fibrillogenesis, biomarkers, precursor suppression, and clearance therapies. Limitations include transgene-expression effects, accelerated disease, species-specific proteostasis and ApoA-II biology, and incomplete representation of human heterozygous, late-onset disease.

Cell-free recombinant-protein systems and cultured-cell assays are useful for measuring stability, proteolysis, lipid binding, oligomerization, and fibril formation, but they do not reproduce organ tropism, circulation, extracellular matrix, or immune clearance. No mature organoid, iPSC, zebrafish, Drosophila, or CRISPR-screen platform specific to the full FVA umbrella was identified.

## Recent developments, 2023–2024

1. **Expanded APOA1 inheritance:** the August 2024 homozygous p.Leu202Arg cardiac case raises the possibility that selected APOA1 alleles act recessively, contrary to the usual dominant model. This remains hypothesis-generating because evidence is from one patient. DOI: https://doi.org/10.1038/s41439-024-00288-7. (yagi2024theapoa1p.leu202arg pages 1-3)
2. **Improved proteomic typing:** 2024 work evaluated DIA, FAIMS, de-novo/error-tolerant sequence searches, and MALDI imaging to accelerate and improve amyloid protein/variant identification. These methods are promising diagnostic refinements, not yet replacements for validated LMD–LC-MS/MS workflows.
3. **Updated AFib synthesis:** a systematic search updated through November 2023 quantified rapid progression and reinforced the biopsy–mass-spectrometry–sequencing triad. The article was published online in October 2024 and in a 2025 issue. (he2025clinicalmanifestationsdiagnosis pages 1-2)
4. **Nomenclature:** the International Society of Amyloidosis issued a 2024 protein-based nomenclature update, reinforcing that “familial visceral amyloidosis” should be decomposed by fibril precursor rather than treated as one phenotype.

## Selected exact abstract quotations

* AFib review: **“AFib amyloidosis progresses rapidly.”** (he2025clinicalmanifestationsdiagnosis pages 1-2)
* AApoAI cohort: **“AApoAI amyloidosis is a slowly progressive disease that is challenging to diagnose.”** (cohen2024prognosticmarkersand pages 194-199)
* APOA1 2024 case: **“ApoA-I amyloidosis is an extremely rare form of systemic amyloidosis that commonly involves the heart, kidneys, and liver.”** (yagi2024theapoa1p.leu202arg pages 1-3)
* B2M review: **“Its genetic variant D76N causes a very rare form of familial systemic amyloidosis.”** (stoppini2015systemicamyloidosislessons pages 1-2)
* APOA2 model: **“A transgenic mouse model reproduces human hereditary systemic amyloidosis.”** (chabert2019atransgenicmouse pages 1-2)

## Key publications and identifiers

* He et al. *Clinical manifestations, diagnosis and treatment of hereditary fibrinogen Aα-chain renal amyloidosis.* Online October 2024/issue 2025. DOI: https://doi.org/10.1007/s11255-024-04236-w. (he2025clinicalmanifestationsdiagnosis pages 1-2)
* Meyer et al. *Organ Transplantation in Hereditary Fibrinogen A α-Chain Amyloidosis.* September 2020. DOI: https://doi.org/10.1053/j.ajkd.2020.02.445.
* Stangou et al. *Hereditary fibrinogen A alpha-chain amyloidosis.* April 2010. DOI: https://doi.org/10.1182/blood-2009-06-223792.
* Cohen et al. *The experience of hereditary apolipoprotein A-I amyloidosis at the UK National Amyloidosis Centre.* May 2022. DOI: https://doi.org/10.1080/13506129.2022.2070741. (cohen2024prognosticmarkersand pages 194-199)
* Yagi et al. *The APOA1 p.Leu202Arg variant potentially causes autosomal recessive cardiac amyloidosis.* August 2024. DOI: https://doi.org/10.1038/s41439-024-00288-7. (yagi2024theapoa1p.leu202arg pages 1-3)
* Moutafi et al. *A new genetic variant of hereditary apolipoprotein A-I amyloidosis.* January 2019. DOI: https://doi.org/10.1186/s12881-019-0755-5. (moutafi2019anewgenetic pages 1-2)
* Jean et al. *A new family with hereditary lysozyme amyloidosis…* September 2014. DOI: https://doi.org/10.1186/1471-230X-14-159.
* Yazaki et al. *Renal amyloidosis caused by a novel stop-codon mutation in APOA2.* November 2001. DOI: https://doi.org/10.1046/j.1523-1755.2001.00024.x.
* Chabert et al. *A transgenic mouse model reproduces human hereditary systemic amyloidosis.* September 2019. DOI: https://doi.org/10.1016/j.kint.2019.03.013. (chabert2019atransgenicmouse pages 1-2)
* Stoppini and Bellotti. *Systemic Amyloidosis: Lessons from β2-Microglobulin.* April 2015. DOI: https://doi.org/10.1074/jbc.R115.639799. (stoppini2015systemicamyloidosislessons pages 1-2)
* Landmark FGA association: PMID **8097946**; additional FGA evidence indexed under PMIDs **19073821, 23551149, 29142973**. LYZ evidence includes PMIDs **8464497, 11849445, 12360495, 15745733, 16523055, 20301373, 21988333**; APOA1 evidence includes PMIDs **12050338, 16925563, 21820994, 26515634, 27240838, 27604308, 32022753**; hereditary B2M includes PMID **22693999**. These PMID associations are database-level links and should be checked against the full article before attaching them to individual variant assertions. (OpenTargets Search: familial visceral amyloidosis)

## Knowledge gaps and confidence assessment

**High confidence:** umbrella status; causal genes; autosomal-dominant inheritance for most forms; renal predominance of AFib; genotype-dependent AFib progression; AApoAI organ distribution and transplant outcomes; requirement for tissue typing plus molecular confirmation.

**Moderate confidence:** precise organ tropism of individual rare APOA1/LYZ/APOA2 variants and benefit of source-organ transplantation outside larger AFib/AApoAI series.

**Low or unavailable:** global prevalence/incidence, penetrance estimates, carrier frequencies, sex ratio, unified survival, protective factors, modifier genes, pharmacogenomics, epigenetics, disease-specific omics signatures, validated quality-of-life statistics, natural veterinary homologues, and interventional-trial efficacy. These fields should be stored as **not established**, not as negative biological findings.

References

1. (OpenTargets Search: familial visceral amyloidosis): Open Targets Query (familial visceral amyloidosis, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (stoppini2015systemicamyloidosislessons pages 1-2): Monica Stoppini and Vittorio Bellotti. Systemic amyloidosis: lessons from β2-microglobulin. Apr 2015. URL: https://doi.org/10.1074/jbc.r115.639799, doi:10.1074/jbc.r115.639799. This article has 115 citations and is from a domain leading peer-reviewed journal.

3. (cohen2024prognosticmarkersand pages 194-199): OC Cohen. Prognostic markers and management strategies in systemic amyloidosis. Unknown journal, 2024.

4. (he2025clinicalmanifestationsdiagnosis pages 1-2): Linying He, Jiahui Zhou, Miner Wang, Jianxiang Chen, Chang Liu, Jiazhen Shi, Yanxia Rui, and Henglan Wu. Clinical manifestations, diagnosis and treatment of hereditary fibrinogen aα-chain renal amyloidosis: one case report and systematic review. International Urology and Nephrology, 57:517-533, Oct 2025. URL: https://doi.org/10.1007/s11255-024-04236-w, doi:10.1007/s11255-024-04236-w. This article has 1 citations and is from a peer-reviewed journal.

5. (escaleira2022fibrinogenaalphachain pages 14-17): JPR da Cruz Escaleira. Fibrinogen a alpha-chain amyloidosis: the landscape of dialysis and kidney transplantation in patients with the fga p. glu545val variant and portuguese ancestry. Unknown journal, 2022.

6. (yagi2024theapoa1p.leu202arg pages 1-3): Shusuke Yagi, Ryosuke Miyamoto, Masayoshi Tasaki, Hiroyuki Morino, Ryuji Otani, Muneyuki Kadota, Takayuki Ise, Hiroki Yamazaki, Kenya Kusunose, Koji Yamaguchi, Hirotsugu Yamada, Takeshi Soeki, Tetsuzo Wakatsuki, Daiju Fukuda, Mitsuharu Ueda, and Masataka Sata. The apoa1 p.leu202arg variant potentially causes autosomal recessive cardiac amyloidosis. Human Genome Variation, Aug 2024. URL: https://doi.org/10.1038/s41439-024-00288-7, doi:10.1038/s41439-024-00288-7. This article has 3 citations.

7. (moutafi2019anewgenetic pages 1-2): Myrto Moutafi, Dimitrios C. Ziogas, Spyros Michopoulos, Tina Bagratuni, Vassiliki Vasileiou, Laura Verga, Giampaolo Merlini, Giovanni Palladini, Charis Matsouka, Meletios A. Dimopoulos, and Efstathios Kastritis. A new genetic variant of hereditary apolipoprotein a-i amyloidosis: a case-report followed by discussion of diagnostic challenges and therapeutic options. BMC Medical Genetics, Jan 2019. URL: https://doi.org/10.1186/s12881-019-0755-5, doi:10.1186/s12881-019-0755-5. This article has 18 citations and is from a peer-reviewed journal.

8. (chabert2019atransgenicmouse pages 1-2): Michèle Chabert, Xavier Rousset, Magali Colombat, Michel Lacasa, Hermine Kakanakou, Mathilde Bourderioux, Pierre Brousset, Odile Burlet-Schiltz, Juris J. Liepnieks, Barbara Kluve-Beckerman, Gilles Lambert, François P. Châtelet, Merrill D. Benson, and Athina D. Kalopissis. A transgenic mouse model reproduces human hereditary systemic amyloidosis. Kidney international, 96:628-641, Sep 2019. URL: https://doi.org/10.1016/j.kint.2019.03.013, doi:10.1016/j.kint.2019.03.013. This article has 2 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Familial_Visceral_Amyloidosis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.