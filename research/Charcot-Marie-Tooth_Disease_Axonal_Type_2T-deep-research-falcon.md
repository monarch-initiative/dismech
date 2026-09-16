---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T16:00:30.812731'
end_time: '2026-08-27T16:11:17.249342'
duration_seconds: 646.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth disease, axonal, type 2T
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Charcot-Marie-Tooth_Disease_Axonal_Type_2T-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth disease, axonal, type 2T
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease, axonal, type 2T** covering all of the
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
- **Disease Name:** Charcot-Marie-Tooth disease, axonal, type 2T
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease, axonal, type 2T** covering all of the
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


# Charcot–Marie–Tooth disease, axonal, type 2T (CMT2T)

## Executive summary

CMT2T is a rare, late-onset, length-dependent axonal sensorimotor polyneuropathy caused definitively by **biallelic pathogenic variants in MME**, encoding the cell-surface zinc metalloprotease neprilysin (NEP/CD10). The strongest evidence supports autosomal-recessive loss of function. Monoallelic MME variants should not automatically be labeled CMT2T: their relationship to neuropathy remains incompletely penetrant, risk-associated, or uncertain. The principal 2024 advance was an Italian 32-patient study that refined onset, severity, electrophysiology, and genotype–phenotype relationships; a Chinese report expanded the biallelic variant and motor-predominant phenotypic spectrum. There is no approved disease-modifying or MME-specific treatment.

| Knowledge-base field | Charcot-Marie-Tooth disease type 2T summary |
|---|---|
| Identity / identifiers | **Disease:** Charcot-Marie-Tooth disease type 2T (CMT2T); **MONDO:** MONDO:0044640; **OMIM:** 617017 reported in disease history/literature context as the recessive MME-related axonal CMT entity; **causal gene:** **MME** (membrane metalloendopeptidase; neprilysin), **Ensembl:** ENSG00000196549. Disease-level information here is derived from aggregated literature cohorts and curated disease-gene resources, not individual EHR datasets. (OpenTargets Search: Charcot-Marie-Tooth disease type 2T-MME, higuchi2016mutationsinmme pages 1-2, geroldi2024clinicalandgenetic pages 1-2) |
| Definition | Late-onset inherited peripheral neuropathy within the axonal CMT spectrum caused **definitively by biallelic loss-of-function or other pathogenic MME variants**, producing a predominantly length-dependent motor greater than sensory axonal neuropathy affecting lower limbs first. Monoallelic/heterozygous MME-associated neuropathy remains a separate **uncertain** category with incomplete penetrance or risk-factor status rather than definitive CMT2T. (higuchi2016mutationsinmme pages 1-2, lupo2018characterisingthephenotype pages 9-9, geroldi2024clinicalandgenetic pages 1-2) |
| Inheritance | **Definitive CMT2T:** autosomal recessive, supported by segregation of **biallelic** MME variants in Japanese, Spanish, Italian, and Chinese families. **Monoallelic MME:** not sufficient for definitive disease assignment in the strongest early cohorts; later European/North American/Italian data support possible age-dependent penetrance or neuropathy risk, but causality is unresolved. (higuchi2016mutationsinmme pages 1-2, lupo2018characterisingthephenotype pages 9-9, lupo2018characterisingthephenotype pages 2-3, geroldi2024clinicalandgenetic pages 14-14, geroldi2024clinicalandgenetic pages 1-2) |
| Onset / temporal development | Typically **adult/late onset**, usually **5th-6th decade**. Japanese report: late-onset axonal neuropathy across 10 patients. Spanish cohort: onset **35-73 years**, median **44**. Italian 2024 cohort: onset **24-75 years**, mean **54.7**, median **55**; biallelic onset earlier than monoallelic after exclusion of likely benign variants (**49.6 vs 61.4 years, p=0.0099** in study comparison groups). Course is **slowly progressive**, chronic, lifelong; biallelic cases appear more likely to worsen more rapidly after >10 years disease duration. Suggested HPO mapping: *Adult onset* / *Late onset* / *Progressive peripheral neuropathy* (suggested mappings). (higuchi2016mutationsinmme pages 1-2, lupo2018characterisingthephenotype pages 1-2, geroldi2024clinicalandgenetic pages 2-4, geroldi2024clinicalandgenetic pages 14-14, geroldi2024clinicalandgenetic pages 1-2) |
| Core phenotype (clinical) | Typical features: distal lower-limb weakness and atrophy, gait impairment/steppage gait, foot muscle wasting, reduced/absent ankle reflexes, later distal upper-limb involvement, mild-to-moderate sensory loss, paresthesia/tingling, neuropathic pain in some patients, cramps and contractures in some cohorts. Italian 2024: motor-onset in **53%**, sensory in **25%**, mixed in **22%**; **69%** had moderate-severe lower-limb weakness; **91%** abnormal lower-limb reflexes; about **2/3** mild-moderate touch loss; **62%** reduced pinprick; **63%** reduced light touch. Suggested HPO terms: distal muscle weakness, lower-limb amyotrophy, steppage gait/abnormal gait, foot drop, areflexia/hyporeflexia, distal sensory impairment, paresthesia, neuropathic pain, muscle cramps, pes cavus if present (suggested mappings; exact IDs not asserted). (higuchi2016mutationsinmme pages 1-2, lupo2018characterisingthephenotype pages 9-9, lupo2018characterisingthephenotype pages 1-2, geroldi2024clinicalandgenetic pages 2-4) |
| Electrophysiology / pathology | Usually **axonal sensorimotor neuropathy** with upper-limb MNCV typically in the axonal/intermediate range and markedly reduced distal CMAPs, especially in legs; lower-extremity responses may be absent in advanced cases. Italian 2024: **78%** had axonal motor-sensory polyneuropathy; upper-limb MNCV **31-68 m/s**, mean **52**. Spanish cohort noted chronic neurogenic denervation and peripheral nerve hyperexcitability in a subset. Japanese sural biopsies showed marked loss of large myelinated fibers, thin myelin sheaths, and fiber clustering, without onion bulbs or inflammation; NEP immunostaining was absent or reduced. Suggested ontology mappings: axonal neuropathy, chronic denervation on EMG, reduced CMAP, absent SNAP/CMAP in distal legs, sural nerve fiber loss (suggested mappings). (higuchi2016mutationsinmme pages 10-11, lupo2018characterisingthephenotype pages 9-9, lupo2018characterisingthephenotype pages 2-3, geroldi2024clinicalandgenetic pages 5-8) |
| Genetics / pathogenic variants | Disease gene is **MME**. Reported pathogenic variant classes include nonsense, frameshift, canonical splice, in-frame deletion, and missense. Foundational Japanese examples include **c.661C>T (p.Gln221*)**, **c.1231_1233delTGT (p.Cys411del)**, **c.1861T>C (p.Cys621Arg)**, splice variants including **c.654+1G>A** and **c.439-2T>A**. Chinese 2024 report: **c.2122A>T (p.K708*)** homozygous pathogenic variant; and **c.1342C>T (p.R448*)** plus **c.2071_2072delinsTT (p.A691L)** compound heterozygous genotype. Italian 2024 classified variants by ACMG as **8 pathogenic, 13 likely pathogenic, 10 VUS, 1 likely benign** and provided non-Finnish European frequencies for several alleles, with many loss-of-function alleles absent or ultra-rare in gnomAD NFE. Germline origin is implied; no somatic role established. (higuchi2016mutationsinmme pages 10-11, higuchi2016mutationsinmme pages 5-8, zhang2024anovelvariant pages 2-4, zhang2024anovelvariant pages 1-2, geroldi2024clinicalandgenetic pages 10-11, geroldi2024clinicalandgenetic pages 11-12) |
| Mechanism / pathophysiology | Best-supported mechanism is **MME/neprilysin loss of function** in the peripheral nervous system, probably disrupting neuropeptide homeostasis and axon-Schwann cell biology, leading to a length-dependent axonopathy. Japanese study showed absent or markedly reduced NEP protein in sural nerve and higher expression in myelin sheaths than axons, supporting relevance to Schwann-cell/myelin-associated compartments despite primarily axonal clinical disease. Italian 2024 concluded many variants are predicted to trigger **nonsense-mediated decay (NMD)**; missense effects may alter local H-bonds/steric interactions. Mechanistic certainty remains moderate because no disease-specific transcriptomic/proteomic/metabolomic signature has been established. Suggested GO terms: peptide catabolic process, metallopeptidase activity, neuron projection maintenance, axon ensheathment/axon-Schwann cell interaction, peripheral nervous system development (suggested mappings). (higuchi2016mutationsinmme pages 10-11, higuchi2016mutationsinmme pages 11-13, lupo2018characterisingthephenotype pages 8-9, geroldi2024clinicalandgenetic pages 12-14) |
| Anatomy / cell types / subcellular localization | **Primary structures:** peripheral nerves, especially long nerves to lower limbs; sural nerve is pathologically documented. **Tissues/cells:** peripheral axons and myelinating Schwann cells are the main implicated cell populations. **Subcellular/protein localization:** NEP is a cell-surface zinc-dependent metalloprotease and exists predominantly as a homodimer on the cell surface. Suggested anatomical/cell ontology mappings: peripheral nerve, sural nerve, lower limb musculature, axon, myelinating Schwann cell; suggested GO cellular component: plasma membrane/cell surface. (higuchi2016mutationsinmme pages 10-11, zhang2024anovelvariant pages 1-2, geroldi2024clinicalandgenetic pages 1-2) |
| Diagnosis | Real-world diagnosis relies on clinical pattern recognition of late-onset length-dependent axonal neuropathy, **NCS/EMG**, exclusion of acquired neuropathy causes, and **molecular confirmation of MME variants** by targeted neuropathy panel, Sanger confirmation, or broader NGS approaches. Italian cohort used referral-center routine CMT diagnostics plus laboratory exclusion workup; Chinese 2024 used targeted neuromuscular NGS. Biopsy is supportive but not required when genetics is definitive. Suggested differential diagnoses: other late-onset hereditary axonal neuropathies, distal hereditary motor neuropathy, RFC1-related CANVAS/sensory neuropathy, acquired axonal neuropathies, and CIDP mimics when electrophysiology is atypical. Broader CMT evidence supports targeted NGS panels first, with WES/WGS for unsolved cases. (zhang2024anovelvariant pages 1-2, geroldi2024clinicalandgenetic pages 2-4, grado2025charcotmarietoothdiseasea pages 3-4, grado2025charcotmarietoothdiseasea pages 1-3) |
| Management | **No MME-specific approved therapy.** Current care is symptomatic/supportive as for CMT: physical therapy, occupational therapy, exercise/strength and balance work, orthoses, fall prevention, pain/cramp management, and orthopedic/foot interventions when indicated. Evidence for these interventions is largely **CMT-general**, not CMT2T-specific. No dedicated CMT2T interventional trial was identified in the provided evidence. (nair2023clinicaltrialsin pages 2-4, grado2025charcotmarietoothdiseasea pages 3-4, grado2025charcotmarietoothdiseasea pages 1-3) |
| Prognosis / outcomes | Available data suggest **mild-to-moderate but progressive disability**, predominantly affecting ambulation and lower-limb function. Italian 2024 mean **CMTES 10** (range **1-21**); disease severity correlates more with duration, and biallelic disease appears more severe after >10 years. CNS involvement appears minimal: no obvious cognitive impairment in major cohorts, and Japanese patients lacked clear Alzheimer/dementia evidence. Life expectancy, disease-specific mortality, and robust survival statistics are **not established** for CMT2T. (higuchi2016mutationsinmme pages 11-13, geroldi2024clinicalandgenetic pages 2-4, geroldi2024clinicalandgenetic pages 5-8) |
| Epidemiology / population | CMT2T is **rare** and no population prevalence/incidence specific to CMT2T was established in the provided evidence. Foundational evidence suggests MME was a relatively frequent cause of **adult-onset autosomal recessive CMT2 in Japan**; Spanish authors also found biallelic MME among their more common late-onset recessive axonal neuropathy diagnoses. Italian 2024 assembled **32 patients** from four centers, supporting recognition across Europe. Sex distribution in the Italian cohort was near-even (**18 male, 14 female**). No validated carrier-frequency estimate for disease-causing biallelic CMT2T was identified here. (higuchi2016mutationsinmme pages 1-2, lupo2018characterisingthephenotype pages 9-9, geroldi2024clinicalandgenetic pages 2-4) |
| Recent 2024 evidence | **Italian cohort (2024):** largest disease-focused update in provided evidence, 32 patients; refined phenotype, ACMG variant classes, onset distribution, and stronger evidence that biallelic cases progress faster with longer duration. **Chinese case report (2024):** added novel homozygous **p.K708*** and further support for late-onset recessive MME-related dHMN/CMT2 overlap with prominent motor axonal impairment and slight sensory involvement. These are the most relevant 2024 disease-specific developments in the supplied sources. (geroldi2024clinicalandgenetic pages 2-4, geroldi2024clinicalandgenetic pages 14-14, zhang2024anovelvariant pages 2-4, zhang2024anovelvariant pages 1-2) |
| Monoallelic MME-associated neuropathy status | **Not equivalent to definitive CMT2T.** Strong earlier cohorts found healthy heterozygous relatives older than affected recessive cases and concluded heterozygous variants did not segregate convincingly with disease. Later studies propose heterozygous variants may be incompletely penetrant or act as risk factors, possibly requiring a second genetic/environmental hit. Knowledge-base curation should therefore separate: **(1) definitive biallelic recessive CMT2T** from **(2) uncertain monoallelic MME-associated late-onset axonal neuropathy/risk state**. (lupo2018characterisingthephenotype pages 9-9, lupo2018characterisingthephenotype pages 8-9, geroldi2024clinicalandgenetic pages 14-14, geroldi2024clinicalandgenetic pages 1-2) |
| Prevention / counseling | No primary prevention exists for the neuropathy itself. Recommended measures are **genetic counseling**, family segregation testing, carrier testing in relatives when a familial pathogenic variant is known, and reproductive counseling. Accurate distinction between biallelic disease and heterozygous uncertain findings is especially important for counseling. (lupo2018characterisingthephenotype pages 9-9, nair2023clinicaltrialsin pages 2-4) |
| Evidence gaps | Disease-specific gaps include: uncertain **OMIM/MONDO cross-mapping verification beyond provided contexts**; limited prevalence/incidence data; no established penetrance estimates; no validated disease-specific biomarkers; no transcriptomic/proteomic/metabolomic signature; no proven modifier genes or gene-environment interactions; no established renal/CNS complication frequency; no MME-targeted therapy or CMT2T-specific trial; limited animal/model-organism evidence that recapitulates peripheral neuropathy despite NEP biology. (higuchi2016mutationsinmme pages 11-13, lupo2018characterisingthephenotype pages 8-9, geroldi2024clinicalandgenetic pages 14-14, geroldi2024clinicalandgenetic pages 12-14) |


*Table: This compact table summarizes the current evidence base for Charcot-Marie-Tooth disease type 2T, emphasizing definitive biallelic MME-related recessive disease versus uncertain monoallelic MME-associated neuropathy. It is designed to support structured curation of identifiers, phenotype, mechanism, diagnosis, management, prognosis, and evidence gaps.*

## 1. Disease information

**Definition.** CMT2T is an inherited peripheral neuropathy in the axonal CMT2 group. It typically begins in adulthood with distal lower-limb weakness, wasting, and gait impairment, followed by sensory loss and sometimes upper-limb involvement. Nerve conduction studies show primarily axonal rather than uniformly demyelinating disease.

**Identifiers and names**

- **MONDO:** MONDO:0044640.
- **OMIM phenotype:** commonly indexed as **CMT2T, 617017**; this cross-reference should be verified directly in OMIM before production ingestion.
- **Causal gene:** **MME**, Ensembl **ENSG00000196549**; the Open Targets CMT2T association contains human genetic evidence linked to PMID **26991897**. (OpenTargets Search: Charcot-Marie-Tooth disease type 2T-MME)
- **Synonyms:** Charcot–Marie–Tooth disease type 2T; CMT2T; autosomal-recessive CMT2T; MME-related axonal neuropathy; late-onset recessive CMT2. “MME-related distal hereditary motor neuropathy” describes an overlapping motor-predominant phenotype but is not always clinically identical.
- No disease-specific ICD-10, ICD-11, or MeSH code was established in the retrieved evidence; broader hereditary motor and sensory neuropathy/polyneuropathy codes are generally required.

The evidence summarized here is aggregated from disease cohorts, families, and curated disease–gene resources—not individual EHR records.

## 2. Etiology and risk/protective factors

### Causal factor

The established cause is **germline biallelic pathogenic MME variation**. The original Japanese study found 10 affected individuals among 303 unrelated inherited-neuropathy cases and showed a consistent late-onset axonal motor-sensory phenotype. Patient nerve demonstrated absent or reduced NEP, supporting loss of function rather than a purely statistical association. (higuchi2016mutationsinmme pages 10-11, higuchi2016mutationsinmme pages 1-2)

The foundational paper’s central conclusion was: **“Mutations in MME cause an autosomal-recessive Charcot–Marie–Tooth disease type 2.”** It was published in *Annals of Neurology* in March 2016, DOI [10.1002/ana.24612](https://doi.org/10.1002/ana.24612), PMID **26991897**. (higuchi2016mutationsinmme pages 10-11, higuchi2016mutationsinmme pages 1-2)

### Genetic risk

- Highest-confidence risk: two pathogenic/likely pathogenic alleles in trans or a homozygous pathogenic allele.
- Family history may be absent because inheritance is recessive and onset is late.
- Consanguinity was present in several original Japanese families; other families were non-consanguineous. Unaffected heterozygous relatives supported recessive segregation. (higuchi2016mutationsinmme pages 5-8)
- **Monoallelic variants:** Spanish investigators found no convincing disease segregation and observed healthy older heterozygous loss-of-function carriers. The 2024 Italian study instead considered monoallelic variants possible incompletely penetrant risk alleles. These observations are not equivalent: biallelic causality is established, whereas monoallelic causality remains unsettled. (lupo2018characterisingthephenotype pages 9-9, lupo2018characterisingthephenotype pages 8-9, geroldi2024clinicalandgenetic pages 14-14)

No validated modifier gene, protective allele, anticipation, or germline-mosaicism estimate has been reported. Carrier frequency and penetrance cannot presently be quantified reliably.

### Environmental and gene–environment factors

No environmental exposure, infection, diet, smoking behavior, or occupational factor is known to cause CMT2T. Acquired neuropathy factors—diabetes, alcohol, vitamin deficiency, renal disease, neurotoxic chemotherapy—may plausibly add disability but have not been demonstrated as CMT2T-specific interactions. The Italian cohort excluded common acquired causes; 23.5% had autoimmune comorbidity, but this did not correlate with onset, inheritance, or severity. The suggestion that a second genetic or environmental event might help monoallelic variants manifest remains a hypothesis. (geroldi2024clinicalandgenetic pages 14-14, geroldi2024clinicalandgenetic pages 5-8)

No disease-specific protective factor is established. Avoiding neurotoxic exposures is prudent clinical practice, not proven primary prevention.

## 3. Phenotypes

The phenotype is usually symmetric, length-dependent, motor-predominant initially, and slowly progressive.

| Manifestation | Characteristics and frequency | Suggested HPO term |
|---|---|---|
| Distal lower-limb weakness | Typical presenting sign; 69% had moderate–severe lower-limb weakness in the 2024 Italian cohort | Distal muscle weakness; lower-limb muscle weakness |
| Gait impairment/steppage gait | Most common motor-onset feature; falls may occur | Abnormal gait; steppage gait; foot drop |
| Distal amyotrophy | Feet, tibialis anterior, gastrocnemius; hands later in some patients | Distal amyotrophy; lower-limb muscle atrophy |
| Hyporeflexia/areflexia | Lower-limb reflexes abnormal in 91%; upper-limb reflexes abnormal in 56% in the Italian cohort | Hyporeflexia; absent Achilles reflex |
| Sensory loss | Develops or becomes disabling later; approximately two-thirds had mild–moderate touch loss, 62% reduced pinprick and 63% reduced light touch | Distal sensory impairment; reduced pain sensation |
| Paresthesia/neuropathic pain | Common sensory-onset complaints, but exact CMT2T-wide prevalence is unknown | Paresthesia; neuropathic pain |
| Cramps/contractures | Particularly noted in the Spanish series; frequency not robustly quantified | Muscle cramps; joint contracture |
| Upper-limb involvement | Usually later and milder; 81% of Italian patients had normal or only mild upper-limb weakness | Distal upper-limb weakness |

In the 2024 Italian cohort, onset was motor in **53%**, sensory in **25%**, and mixed in **22%**; mean CMT Examination Score was **10** (range 1–21). (geroldi2024clinicalandgenetic pages 2-4)

A 2024 Chinese motor-predominant report illustrates phenotypic overlap with dHMN. Its two probands developed symptoms at 58 and 51 years, respectively, with steppage gait, distal weakness, and lower-leg wasting; sensory examination was normal or nearly normal. The abstract states: **“Prominently axonal impairment of motor nerves and slight involvement of sensory nerves were observed.”** Published in *BMC Medical Genomics* 17:223, DOI [10.1186/s12920-024-01996-3](https://doi.org/10.1186/s12920-024-01996-3). (zhang2024anovelvariant pages 2-4, zhang2024anovelvariant pages 1-2)

**Quality of life.** No CMT2T-specific EQ-5D, SF-36, PROMIS, or quality-of-life dataset was found. Expected burdens include impaired walking, falls, orthotic use, reduced independence, pain, and hand dysfunction, but quantitative estimates from general CMT must not be assigned directly to CMT2T.

## 4. Genetic and molecular information

### Gene and protein

- **MME** encodes membrane metalloendopeptidase/neprilysin, also known as NEP or CD10.
- NEP is a zinc-dependent, membrane-bound peptidase, predominantly a cell-surface homodimer, that cleaves multiple bioactive peptides and participates in neuropeptide regulation. (zhang2024anovelvariant pages 1-2, geroldi2024clinicalandgenetic pages 1-2)
- Variant origin is germline. No somatic disease mechanism is recognized.

### Pathogenic variants

Reported classes include nonsense, frameshift, splice-altering, missense, deletion, and in-frame deletion variants. Foundational examples include **c.661C>T (p.Gln221Ter), c.1231_1233delTGT (p.Cys411del), c.1861T>C (p.Cys621Arg), c.654+1G>A**, and **c.439-2T>A**. (higuchi2016mutationsinmme pages 5-8)

The 2024 Chinese study reported:

- Homozygous **c.2122A>T (p.Lys708Ter)**, ACMG pathogenic, absent from ExAC and 1000 Genomes in the authors’ analysis; four affected sisters carried the homozygous variant.
- Compound heterozygous **c.1342C>T (p.Arg448Ter)** and **c.2071_2072delinsTT (p.Ala691Leu)**. (zhang2024anovelvariant pages 2-4, zhang2024anovelvariant pages 1-2)

The 2024 Italian study observed 21 different variants among 32 included patients and classified patient findings as **8 pathogenic, 13 likely pathogenic, 10 VUS, and 1 likely benign** under ACMG criteria. Thirteen patients had biallelic variants, 18 monoallelic variants, and one had two variants of unresolved phase. Many loss-of-function alleles were absent or extremely rare in gnomAD non-Finnish Europeans. Frequencies shown in the study ranged from zero to low fractions of a percent; **p.Gly224/225Ala**, at approximately 0.19% with atypical presentation, was considered a likely benign exemplar. (geroldi2024clinicalandgenetic pages 5-8, geroldi2024clinicalandgenetic pages 8-10, geroldi2024clinicalandgenetic pages 10-11, geroldi2024clinicalandgenetic pages 11-12)

Truncating and several splice variants are predicted to undergo nonsense-mediated decay. Missense variants may disrupt hydrogen bonds or create steric clashes, but the Italian study performed no RNA analysis or NEP dosage, so those effects remain computational. (geroldi2024clinicalandgenetic pages 8-10, geroldi2024clinicalandgenetic pages 12-14)

No recurrent chromosomal abnormality, pathogenic epigenetic signature, or validated modifier gene is known.

## 5. Environmental information

CMT2T is not infectious, toxic, radiation-induced, or lifestyle-caused. No pathogen or zoonotic route applies. Environmental evaluation is diagnostically important chiefly to exclude competing causes of late-onset axonal neuropathy. No controlled data demonstrate that diet, exercise, alcohol abstinence, or smoking cessation alters the molecular onset of MME-related disease.

## 6. Mechanism and pathophysiology

### Evidence-supported causal chain

1. **Upstream trigger:** biallelic pathogenic MME variants.
2. **Protein consequence:** nonsense-mediated decay, unstable/abnormal NEP, or loss of catalytic protein; absent or reduced NEP was demonstrated in patient sural nerve.
3. **Cellular consequence:** impaired extracellular peptide turnover/neuropeptide homeostasis at the peripheral-nerve cell surface, with probable disruption of axon–Schwann-cell trophic interactions.
4. **Tissue consequence:** length-dependent loss of large myelinated fibers and axonal degeneration, followed by chronic denervation and incomplete reinnervation.
5. **Clinical consequence:** distal weakness and wasting, gait impairment, areflexia, and progressive sensory loss.

Human sural biopsies showed markedly reduced large myelinated-fiber density, thin myelin sheaths, and fiber clustering without inflammatory infiltrates or onion bulbs. NEP staining was absent in one patient and reduced in another; western blot found no detectable NEP in the former. NEP appeared more abundant in myelin sheaths than axons, implicating myelinating Schwann cells even though the electrophysiologic phenotype is predominantly axonal. (higuchi2016mutationsinmme pages 10-11, higuchi2016mutationsinmme pages 11-13)

The precise pathogenic peptide substrate is unknown. MME also degrades amyloid-β, but major cohorts found no consistent cognitive impairment, dementia, or excess amyloid signal; therefore amyloid accumulation is not an established mediator of peripheral neuropathy. (higuchi2016mutationsinmme pages 1-2, higuchi2016mutationsinmme pages 11-13, geroldi2024clinicalandgenetic pages 5-8)

**Suggested GO annotations:** metallopeptidase activity; peptide catabolic process; regulation of neuropeptide signaling; plasma membrane; neuron projection maintenance; axon ensheathment; peripheral nervous system development. **Suggested Cell Ontology concepts:** myelinating Schwann cell and peripheral-neuron axon. These are mechanistic curation suggestions, not all experimentally validated CMT2T-specific annotations.

No CMT2T-specific transcriptomic, single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, CRISPR-screen, or integrated multi-omics signature has been established.

## 7. Anatomical structures affected

The primary system is the **peripheral nervous system**, especially long motor and sensory nerves to the feet and lower legs. Distal muscles are secondarily denervated. Sural nerve pathology provides direct tissue evidence. Upper limbs are generally affected later. Findings are usually bilateral and approximately symmetric.

Suggested mappings include peripheral nerve, sural nerve, tibial nerve, peroneal/fibular nerve, lower-limb skeletal muscle, peripheral axon, neuromuscular junction, and myelinating Schwann cell. At the subcellular level, the most relevant compartment is the **plasma membrane/cell surface**, where NEP resides. No consistent primary brain, spinal cord, cardiac, respiratory, or gastrointestinal involvement is established.

## 8. Temporal development

Onset is chronic and insidious rather than acute. The Spanish series reported onset from **35–73 years**, median **44**. The 2024 Italian study reported **24–75 years**, mean **54.7**, median **55**, with mean disease duration 10.6 years. After excluding likely benign variants, onset differed between study-defined groups at **49.6 versus 61.4 years** (p=0.0099), while the overall analysis placed typical onset in the fifth to sixth decades. (lupo2018characterisingthephenotype pages 1-2, geroldi2024clinicalandgenetic pages 2-4)

Progression is lifelong and usually slow. In the Italian cohort, CMTES increased from a mean of 8 in patients with less than 10 years’ disease to 13 after more than 10 years (p=0.044); biallelic cases appeared more severe after longer duration. No remission pattern or discrete end stage is recognized. (geroldi2024clinicalandgenetic pages 2-4, geroldi2024clinicalandgenetic pages 12-14)

## 9. Inheritance and population

CMT2T is **autosomal recessive**. Affected persons generally carry homozygous or compound-heterozygous pathogenic MME variants. Each sibling of an affected person whose parents are both carriers has, conventionally, a 25% probability of being affected, 50% of being an unaffected carrier, and 25% of inheriting neither familial allele.

Penetrance for clearly pathogenic biallelic genotypes appears high by late adulthood, but sample sizes are too small for a formal estimate. Expressivity varies from motor-predominant dHMN-like neuropathy to sensorimotor CMT2. Anticipation is not expected. No established founder variant or geographic hotspot was demonstrated.

Subtype-specific prevalence and incidence are unknown. In the Japanese discovery cohort, MME was considered an important and possibly the most frequent identified cause of adult-onset recessive CMT2, but that is a referral-cohort observation, not population prevalence. The Italian cohort included 18 males and 14 females, offering no evidence of sex bias. (higuchi2016mutationsinmme pages 1-2, geroldi2024clinicalandgenetic pages 2-4)

## 10. Diagnostics

### Recommended workflow

1. Document late-onset, slowly progressive, length-dependent distal weakness, wasting, reflex loss, and sensory findings.
2. Perform **NCS/EMG**. Axonal disease is indicated primarily by reduced CMAP/SNAP amplitudes with relatively preserved velocities; upper-limb MNCV above approximately 38 m/s traditionally supports CMT2, although intermediate values occur.
3. Exclude acquired causes with glucose/HbA1c, B12/folate, thyroid, renal/hepatic, paraprotein, medication/toxin, inflammatory, and other clinically directed testing.
4. Use a comprehensive inherited-neuropathy panel including **MME**, with deletion/duplication and splice-region coverage where possible. Confirm variants and phase by parental/family testing.
5. If unresolved, use WES or preferably WGS with copy-number, structural-variant, mitochondrial, and repeat-expansion analysis. RNA studies may clarify splice variants.

The Italian cohort found axonal sensorimotor polyneuropathy in **78%**; upper-limb MNCV ranged **31–68 m/s** (mean 52), illustrating that occasional intermediate-range results do not exclude CMT2T. (geroldi2024clinicalandgenetic pages 5-8)

Nerve biopsy is not routinely necessary after molecular confirmation, but can show primary axonal loss without inflammation or onion-bulb formation. MRI may document length-dependent fatty muscle replacement but is not diagnostic. There is no validated circulating CMT2T biomarker.

**Differential diagnosis:** other genetic CMT2/dHMN forms, especially SORD-, MFN2-, MPZ-, NEFL-, HSPB1-, GARS1-, and RFC1-related disease; diabetic, toxic, nutritional, paraproteinemic, renal, and immune neuropathies; motor-neuron disease when sensory findings are minimal; and CIDP when slowing is disproportionate. The dHMN/CMT2 boundary is particularly porous because slight sensory involvement may be electrophysiologic rather than clinically obvious. (zhang2024anovelvariant pages 1-2, geroldi2024clinicalandgenetic pages 8-10)

Cascade testing is appropriate after identifying familial pathogenic alleles. CMT2T is not part of routine newborn screening, and late onset limits the value of predictive testing in minors absent a direct medical benefit.

## 11. Outcome and prognosis

CMT2T generally causes mild-to-moderate but progressive morbidity, chiefly impaired walking, falls, foot deformity, orthotic dependence, and later hand limitations. The 2024 Italian mean CMTES was 10, but scores ranged from 1 to 21. (geroldi2024clinicalandgenetic pages 2-4)

Recovery of already lost axons is limited; rehabilitation can improve safety and functional compensation but is not curative. No CMT2T-specific mortality rate, survival curve, or life-expectancy decrement is available. Major cohorts did not demonstrate consistent cognitive decline or Alzheimer disease. Renal failure/nephrotic syndrome was absent in eight assessable original patients, although two had mild proteinuria; this is insufficient to define renal risk. (higuchi2016mutationsinmme pages 11-13)

Potential prognostic factors are disease duration, biallelic status, baseline lower-limb weakness, and possibly variant class, but none has been prospectively validated. NCS values did not track the greater clinical severity of longer-duration biallelic disease in the Italian cohort. (geroldi2024clinicalandgenetic pages 14-14, geroldi2024clinicalandgenetic pages 12-14)

## 12. Treatment and current applications

There is **no approved MME-directed or CMT2T disease-modifying therapy**. Real-world management is multidisciplinary and extrapolated from broader CMT practice:

- Physiotherapy: individualized aerobic conditioning, submaximal strengthening, stretching, balance and fall-prevention work.
- Occupational therapy: hand function, energy conservation, home/work adaptation.
- Orthoses: ankle–foot orthoses, insoles, supportive footwear; canes or other walking aids as needed.
- Symptom treatment: guideline-based neuropathic-pain therapy, cramp management, sleep and fatigue assessment.
- Orthopedic intervention: tendon balancing, osteotomy, arthrodesis, or other correction for painful/progressive cavovarus deformity after specialist assessment.
- Avoid unnecessary immobilization and review potentially neurotoxic drugs individually.

Suggested NCIt intervention concepts include physical therapy, occupational therapy, orthotic device, exercise therapy, pain management, genetic counseling, and orthopedic surgery.

A 2023 analysis of 286 registered CMT studies found 50% procedural, 23% drug, 15% device, and 11% physical-therapy interventions in its abstract-level accounting; 91% were academic. This documents broad CMT research activity, not CMT2T efficacy. DOI [10.3389/fneur.2023.1251885](https://doi.org/10.3389/fneur.2023.1251885), published September 2023. (nair2023clinicaltrialsin pages 2-4)

Gene replacement, RNA therapy, and genome editing are conceptually relevant to recessive loss of function, but no dedicated CMT2T clinical trial or validated preclinical rescue was identified. Restoring NEP requires caution because it processes many vasoactive and neuroactive peptides. AAV-mediated NEP expression has been proposed, not established as a treatment. (higuchi2016mutationsinmme pages 11-13)

## 13. Prevention

Primary lifestyle prevention is unavailable because the disorder is Mendelian. Relevant measures are:

- **Genetic counseling** and segregation testing.
- Carrier testing for adult relatives when familial variants are known.
- Reproductive options including prenatal diagnosis and preimplantation genetic testing, subject to local law and informed preference.
- Early neurologic assessment of at-risk adults, followed by orthotic and rehabilitation intervention when weakness appears.
- Tertiary prevention of falls, contractures, pressure injury, pain, and avoidable deconditioning.

Counseling must distinguish definitive biallelic disease from uncertain monoallelic findings; labeling an isolated heterozygous VUS as causal can produce incorrect recurrence-risk advice. (lupo2018characterisingthephenotype pages 9-9, lupo2018characterisingthephenotype pages 8-9)

No vaccine, antimicrobial prophylaxis, population-screening program, or preventive medication applies.

## 14. Other species and natural disease

No naturally occurring MME-related CMT2T counterpart was identified in companion animals, livestock, or wildlife. There is no zoonotic potential or cross-species transmission. MME orthologs and NEP peptide-cleaving function are conserved, but conservation alone does not establish homologous natural disease. Species, breed/VBO, incidence, and veterinary-treatment fields should therefore be recorded as **not established**.

## 15. Model organisms

NEP-deficient mice are biologically relevant to MME loss, but published summaries report **no obvious motor abnormality or peripheral-nerve degeneration**, despite effects on amyloid biology. They therefore do not faithfully recapitulate human late-onset CMT2T and may require aging, quantitative electrophysiology, injury, or sensitizing genetic/environmental backgrounds to reveal a phenotype. (lupo2018characterisingthephenotype pages 8-9)

No validated CMT2T-specific knock-in mouse, rat, zebrafish, Drosophila, *C. elegans*, patient-iPSC motor-neuron/Schwann-cell coculture, organoid, or neuromuscular assembloid was found. Priority models would include patient-derived iPSC sensory and motor neurons cocultured with Schwann cells, CRISPR-corrected isogenic controls, and aged biallelic knock-in models. Outcomes should include NEP abundance/activity, peptide profiles, axonal transport, neurite survival, myelination, CMAP/SNAP amplitudes, and distal muscle denervation.

## Evidence appraisal and key gaps

The biallelic MME–CMT2T relationship is supported by human segregation, repeated international cohorts, rare damaging alleles, and direct loss of NEP in patient nerve. The disease’s downstream biochemical mechanism remains much less certain. The monoallelic association is controversial and should be curated separately. Major unresolved fields are subtype prevalence/incidence, penetrance, carrier frequency, longitudinal progression, validated biomarkers, quality of life, modifiers, gene–environment interactions, multi-omics, faithful models, and targeted treatment.

The strongest recent study states: **“CMT2T has been definitively defined as a late-onset neuropathy, with a typical onset in the fifth to sixth decades of life and a more rapidly progressing worsening for biallelic patients.”** The study was received 22 May 2024, accepted 22 August 2024, and published in *Journal of the Peripheral Nervous System* 29:472–486, DOI [10.1111/jns.12657](https://doi.org/10.1111/jns.12657). (geroldi2024clinicalandgenetic pages 1-2, geroldi2024clinicalandgenetic pages 12-14)

References

1. (OpenTargets Search: Charcot-Marie-Tooth disease type 2T-MME): Open Targets Query (Charcot-Marie-Tooth disease type 2T-MME, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (higuchi2016mutationsinmme pages 1-2): Yujiro Higuchi, Akihiro Hashiguchi, Junhui Yuan, Akiko Yoshimura, Jun Mitsui, Hiroyuki Ishiura, Masaki Tanaka, Satoshi Ishihara, Hajime Tanabe, Satoshi Nozuma, Yuji Okamoto, Eiji Matsuura, Ryuichi Ohkubo, Saeko Inamizu, Wataru Shiraishi, Ryo Yamasaki, Yasumasa Ohyagi, Jun‐ichi Kira, Yasushi Oya, Hayato Yabe, Noriko Nishikawa, Shinsuke Tobisawa, Nozomu Matsuda, Masayuki Masuda, Chiharu Kugimoto, Kazuhiro Fukushima, Satoshi Yano, Jun Yoshimura, Koichiro Doi, Masanori Nakagawa, Shinichi Morishita, Shoji Tsuji, and Hiroshi Takashima. Mutations in mme cause an autosomal‐recessive charcot–marie–tooth disease type 2. Annals of Neurology, 79:659-672, Mar 2016. URL: https://doi.org/10.1002/ana.24612, doi:10.1002/ana.24612. This article has 128 citations and is from a highest quality peer-reviewed journal.

3. (geroldi2024clinicalandgenetic pages 1-2): Alessandro Geroldi, Andrea La Barbera, Alessia Mammi, Paola Origone, Andrea Gaudio, Clarissa Ponti, Francesca Sanguineri, Sabrina Matà, Martina Sperti, Ilaria Carboni, Emilia Bellone, Fabio Gotta, Chiara Gemelli, Sara Massucco, Guglielmino Valeria, Lucio Marinelli, Marina Grandis, Giulia Bisogni, Mario Sabatelli, Giuseppe Piscosquito, Gabriella Esposito, Angelo Schenone, Fiore Manganelli, Paola Mandich, Stefano Tozza, and Marco Luigetti. Clinical and genetic features of cmt2t in italian patients confirm the importance of mme pathogenic variants in idiopathic, late‐onset axonal neuropathies. Journal of the Peripheral Nervous System, 29:472-486, Sep 2024. URL: https://doi.org/10.1111/jns.12657, doi:10.1111/jns.12657. This article has 2 citations and is from a peer-reviewed journal.

4. (lupo2018characterisingthephenotype pages 9-9): Vincenzo Lupo, Marina Frasquet, Ana Sánchez-Monteagudo, Ana Lara Pelayo-Negro, Tania García-Sobrino, María José Sedano, Julio Pardo, Mercedes Misiego, Jorge García-García, María Jesús Sobrido, María Dolores Martínez-Rubio, María José Chumillas, Juan Jesús Vílchez, Juan Francisco Vázquez-Costa, Carmen Espinós, and Teresa Sevilla. Characterising the phenotype and mode of inheritance of patients with inherited peripheral neuropathies carrying mme mutations. Journal of Medical Genetics, 55:814-823, Nov 2018. URL: https://doi.org/10.1136/jmedgenet-2018-105650, doi:10.1136/jmedgenet-2018-105650. This article has 29 citations and is from a domain leading peer-reviewed journal.

5. (lupo2018characterisingthephenotype pages 2-3): Vincenzo Lupo, Marina Frasquet, Ana Sánchez-Monteagudo, Ana Lara Pelayo-Negro, Tania García-Sobrino, María José Sedano, Julio Pardo, Mercedes Misiego, Jorge García-García, María Jesús Sobrido, María Dolores Martínez-Rubio, María José Chumillas, Juan Jesús Vílchez, Juan Francisco Vázquez-Costa, Carmen Espinós, and Teresa Sevilla. Characterising the phenotype and mode of inheritance of patients with inherited peripheral neuropathies carrying mme mutations. Journal of Medical Genetics, 55:814-823, Nov 2018. URL: https://doi.org/10.1136/jmedgenet-2018-105650, doi:10.1136/jmedgenet-2018-105650. This article has 29 citations and is from a domain leading peer-reviewed journal.

6. (geroldi2024clinicalandgenetic pages 14-14): Alessandro Geroldi, Andrea La Barbera, Alessia Mammi, Paola Origone, Andrea Gaudio, Clarissa Ponti, Francesca Sanguineri, Sabrina Matà, Martina Sperti, Ilaria Carboni, Emilia Bellone, Fabio Gotta, Chiara Gemelli, Sara Massucco, Guglielmino Valeria, Lucio Marinelli, Marina Grandis, Giulia Bisogni, Mario Sabatelli, Giuseppe Piscosquito, Gabriella Esposito, Angelo Schenone, Fiore Manganelli, Paola Mandich, Stefano Tozza, and Marco Luigetti. Clinical and genetic features of cmt2t in italian patients confirm the importance of mme pathogenic variants in idiopathic, late‐onset axonal neuropathies. Journal of the Peripheral Nervous System, 29:472-486, Sep 2024. URL: https://doi.org/10.1111/jns.12657, doi:10.1111/jns.12657. This article has 2 citations and is from a peer-reviewed journal.

7. (lupo2018characterisingthephenotype pages 1-2): Vincenzo Lupo, Marina Frasquet, Ana Sánchez-Monteagudo, Ana Lara Pelayo-Negro, Tania García-Sobrino, María José Sedano, Julio Pardo, Mercedes Misiego, Jorge García-García, María Jesús Sobrido, María Dolores Martínez-Rubio, María José Chumillas, Juan Jesús Vílchez, Juan Francisco Vázquez-Costa, Carmen Espinós, and Teresa Sevilla. Characterising the phenotype and mode of inheritance of patients with inherited peripheral neuropathies carrying mme mutations. Journal of Medical Genetics, 55:814-823, Nov 2018. URL: https://doi.org/10.1136/jmedgenet-2018-105650, doi:10.1136/jmedgenet-2018-105650. This article has 29 citations and is from a domain leading peer-reviewed journal.

8. (geroldi2024clinicalandgenetic pages 2-4): Alessandro Geroldi, Andrea La Barbera, Alessia Mammi, Paola Origone, Andrea Gaudio, Clarissa Ponti, Francesca Sanguineri, Sabrina Matà, Martina Sperti, Ilaria Carboni, Emilia Bellone, Fabio Gotta, Chiara Gemelli, Sara Massucco, Guglielmino Valeria, Lucio Marinelli, Marina Grandis, Giulia Bisogni, Mario Sabatelli, Giuseppe Piscosquito, Gabriella Esposito, Angelo Schenone, Fiore Manganelli, Paola Mandich, Stefano Tozza, and Marco Luigetti. Clinical and genetic features of cmt2t in italian patients confirm the importance of mme pathogenic variants in idiopathic, late‐onset axonal neuropathies. Journal of the Peripheral Nervous System, 29:472-486, Sep 2024. URL: https://doi.org/10.1111/jns.12657, doi:10.1111/jns.12657. This article has 2 citations and is from a peer-reviewed journal.

9. (higuchi2016mutationsinmme pages 10-11): Yujiro Higuchi, Akihiro Hashiguchi, Junhui Yuan, Akiko Yoshimura, Jun Mitsui, Hiroyuki Ishiura, Masaki Tanaka, Satoshi Ishihara, Hajime Tanabe, Satoshi Nozuma, Yuji Okamoto, Eiji Matsuura, Ryuichi Ohkubo, Saeko Inamizu, Wataru Shiraishi, Ryo Yamasaki, Yasumasa Ohyagi, Jun‐ichi Kira, Yasushi Oya, Hayato Yabe, Noriko Nishikawa, Shinsuke Tobisawa, Nozomu Matsuda, Masayuki Masuda, Chiharu Kugimoto, Kazuhiro Fukushima, Satoshi Yano, Jun Yoshimura, Koichiro Doi, Masanori Nakagawa, Shinichi Morishita, Shoji Tsuji, and Hiroshi Takashima. Mutations in mme cause an autosomal‐recessive charcot–marie–tooth disease type 2. Annals of Neurology, 79:659-672, Mar 2016. URL: https://doi.org/10.1002/ana.24612, doi:10.1002/ana.24612. This article has 128 citations and is from a highest quality peer-reviewed journal.

10. (geroldi2024clinicalandgenetic pages 5-8): Alessandro Geroldi, Andrea La Barbera, Alessia Mammi, Paola Origone, Andrea Gaudio, Clarissa Ponti, Francesca Sanguineri, Sabrina Matà, Martina Sperti, Ilaria Carboni, Emilia Bellone, Fabio Gotta, Chiara Gemelli, Sara Massucco, Guglielmino Valeria, Lucio Marinelli, Marina Grandis, Giulia Bisogni, Mario Sabatelli, Giuseppe Piscosquito, Gabriella Esposito, Angelo Schenone, Fiore Manganelli, Paola Mandich, Stefano Tozza, and Marco Luigetti. Clinical and genetic features of cmt2t in italian patients confirm the importance of mme pathogenic variants in idiopathic, late‐onset axonal neuropathies. Journal of the Peripheral Nervous System, 29:472-486, Sep 2024. URL: https://doi.org/10.1111/jns.12657, doi:10.1111/jns.12657. This article has 2 citations and is from a peer-reviewed journal.

11. (higuchi2016mutationsinmme pages 5-8): Yujiro Higuchi, Akihiro Hashiguchi, Junhui Yuan, Akiko Yoshimura, Jun Mitsui, Hiroyuki Ishiura, Masaki Tanaka, Satoshi Ishihara, Hajime Tanabe, Satoshi Nozuma, Yuji Okamoto, Eiji Matsuura, Ryuichi Ohkubo, Saeko Inamizu, Wataru Shiraishi, Ryo Yamasaki, Yasumasa Ohyagi, Jun‐ichi Kira, Yasushi Oya, Hayato Yabe, Noriko Nishikawa, Shinsuke Tobisawa, Nozomu Matsuda, Masayuki Masuda, Chiharu Kugimoto, Kazuhiro Fukushima, Satoshi Yano, Jun Yoshimura, Koichiro Doi, Masanori Nakagawa, Shinichi Morishita, Shoji Tsuji, and Hiroshi Takashima. Mutations in mme cause an autosomal‐recessive charcot–marie–tooth disease type 2. Annals of Neurology, 79:659-672, Mar 2016. URL: https://doi.org/10.1002/ana.24612, doi:10.1002/ana.24612. This article has 128 citations and is from a highest quality peer-reviewed journal.

12. (zhang2024anovelvariant pages 2-4): Bentuo Zhang, Qiang Gang, Lingchao Meng, Zhenyu Li, Xujun Chu, Haohao Wu, Junsu Yang, Baogang Huang, and Kang Du. A novel variant of biallelic mme gene associated with autosomal recessive late-onset distal hereditary motor neuropathy in chinese families. BMC Medical Genomics, Sep 2024. URL: https://doi.org/10.1186/s12920-024-01996-3, doi:10.1186/s12920-024-01996-3. This article has 0 citations and is from a peer-reviewed journal.

13. (zhang2024anovelvariant pages 1-2): Bentuo Zhang, Qiang Gang, Lingchao Meng, Zhenyu Li, Xujun Chu, Haohao Wu, Junsu Yang, Baogang Huang, and Kang Du. A novel variant of biallelic mme gene associated with autosomal recessive late-onset distal hereditary motor neuropathy in chinese families. BMC Medical Genomics, Sep 2024. URL: https://doi.org/10.1186/s12920-024-01996-3, doi:10.1186/s12920-024-01996-3. This article has 0 citations and is from a peer-reviewed journal.

14. (geroldi2024clinicalandgenetic pages 10-11): Alessandro Geroldi, Andrea La Barbera, Alessia Mammi, Paola Origone, Andrea Gaudio, Clarissa Ponti, Francesca Sanguineri, Sabrina Matà, Martina Sperti, Ilaria Carboni, Emilia Bellone, Fabio Gotta, Chiara Gemelli, Sara Massucco, Guglielmino Valeria, Lucio Marinelli, Marina Grandis, Giulia Bisogni, Mario Sabatelli, Giuseppe Piscosquito, Gabriella Esposito, Angelo Schenone, Fiore Manganelli, Paola Mandich, Stefano Tozza, and Marco Luigetti. Clinical and genetic features of cmt2t in italian patients confirm the importance of mme pathogenic variants in idiopathic, late‐onset axonal neuropathies. Journal of the Peripheral Nervous System, 29:472-486, Sep 2024. URL: https://doi.org/10.1111/jns.12657, doi:10.1111/jns.12657. This article has 2 citations and is from a peer-reviewed journal.

15. (geroldi2024clinicalandgenetic pages 11-12): Alessandro Geroldi, Andrea La Barbera, Alessia Mammi, Paola Origone, Andrea Gaudio, Clarissa Ponti, Francesca Sanguineri, Sabrina Matà, Martina Sperti, Ilaria Carboni, Emilia Bellone, Fabio Gotta, Chiara Gemelli, Sara Massucco, Guglielmino Valeria, Lucio Marinelli, Marina Grandis, Giulia Bisogni, Mario Sabatelli, Giuseppe Piscosquito, Gabriella Esposito, Angelo Schenone, Fiore Manganelli, Paola Mandich, Stefano Tozza, and Marco Luigetti. Clinical and genetic features of cmt2t in italian patients confirm the importance of mme pathogenic variants in idiopathic, late‐onset axonal neuropathies. Journal of the Peripheral Nervous System, 29:472-486, Sep 2024. URL: https://doi.org/10.1111/jns.12657, doi:10.1111/jns.12657. This article has 2 citations and is from a peer-reviewed journal.

16. (higuchi2016mutationsinmme pages 11-13): Yujiro Higuchi, Akihiro Hashiguchi, Junhui Yuan, Akiko Yoshimura, Jun Mitsui, Hiroyuki Ishiura, Masaki Tanaka, Satoshi Ishihara, Hajime Tanabe, Satoshi Nozuma, Yuji Okamoto, Eiji Matsuura, Ryuichi Ohkubo, Saeko Inamizu, Wataru Shiraishi, Ryo Yamasaki, Yasumasa Ohyagi, Jun‐ichi Kira, Yasushi Oya, Hayato Yabe, Noriko Nishikawa, Shinsuke Tobisawa, Nozomu Matsuda, Masayuki Masuda, Chiharu Kugimoto, Kazuhiro Fukushima, Satoshi Yano, Jun Yoshimura, Koichiro Doi, Masanori Nakagawa, Shinichi Morishita, Shoji Tsuji, and Hiroshi Takashima. Mutations in mme cause an autosomal‐recessive charcot–marie–tooth disease type 2. Annals of Neurology, 79:659-672, Mar 2016. URL: https://doi.org/10.1002/ana.24612, doi:10.1002/ana.24612. This article has 128 citations and is from a highest quality peer-reviewed journal.

17. (lupo2018characterisingthephenotype pages 8-9): Vincenzo Lupo, Marina Frasquet, Ana Sánchez-Monteagudo, Ana Lara Pelayo-Negro, Tania García-Sobrino, María José Sedano, Julio Pardo, Mercedes Misiego, Jorge García-García, María Jesús Sobrido, María Dolores Martínez-Rubio, María José Chumillas, Juan Jesús Vílchez, Juan Francisco Vázquez-Costa, Carmen Espinós, and Teresa Sevilla. Characterising the phenotype and mode of inheritance of patients with inherited peripheral neuropathies carrying mme mutations. Journal of Medical Genetics, 55:814-823, Nov 2018. URL: https://doi.org/10.1136/jmedgenet-2018-105650, doi:10.1136/jmedgenet-2018-105650. This article has 29 citations and is from a domain leading peer-reviewed journal.

18. (geroldi2024clinicalandgenetic pages 12-14): Alessandro Geroldi, Andrea La Barbera, Alessia Mammi, Paola Origone, Andrea Gaudio, Clarissa Ponti, Francesca Sanguineri, Sabrina Matà, Martina Sperti, Ilaria Carboni, Emilia Bellone, Fabio Gotta, Chiara Gemelli, Sara Massucco, Guglielmino Valeria, Lucio Marinelli, Marina Grandis, Giulia Bisogni, Mario Sabatelli, Giuseppe Piscosquito, Gabriella Esposito, Angelo Schenone, Fiore Manganelli, Paola Mandich, Stefano Tozza, and Marco Luigetti. Clinical and genetic features of cmt2t in italian patients confirm the importance of mme pathogenic variants in idiopathic, late‐onset axonal neuropathies. Journal of the Peripheral Nervous System, 29:472-486, Sep 2024. URL: https://doi.org/10.1111/jns.12657, doi:10.1111/jns.12657. This article has 2 citations and is from a peer-reviewed journal.

19. (grado2025charcotmarietoothdiseasea pages 3-4): Amedeo De Grado, Marina Serio, Paola Saveri, Chiara Pisciotta, and Davide Pareyson. Charcot-marie-tooth disease: a review of clinical developments and its management - what’s new in 2025? Expert Review of Neurotherapeutics, 25:427-442, Feb 2025. URL: https://doi.org/10.1080/14737175.2025.2470980, doi:10.1080/14737175.2025.2470980. This article has 27 citations and is from a peer-reviewed journal.

20. (grado2025charcotmarietoothdiseasea pages 1-3): Amedeo De Grado, Marina Serio, Paola Saveri, Chiara Pisciotta, and Davide Pareyson. Charcot-marie-tooth disease: a review of clinical developments and its management - what’s new in 2025? Expert Review of Neurotherapeutics, 25:427-442, Feb 2025. URL: https://doi.org/10.1080/14737175.2025.2470980, doi:10.1080/14737175.2025.2470980. This article has 27 citations and is from a peer-reviewed journal.

21. (nair2023clinicaltrialsin pages 2-4): Malavika A. Nair, Zhiyv Niu, Nicholas N. Madigan, Alexander Y. Shin, Jeffrey S. Brault, Nathan P. Staff, and Christopher J. Klein. Clinical trials in charcot-marie-tooth disorders: a retrospective and preclinical assessment. Frontiers in Neurology, Sep 2023. URL: https://doi.org/10.3389/fneur.2023.1251885, doi:10.3389/fneur.2023.1251885. This article has 7 citations and is from a peer-reviewed journal.

22. (geroldi2024clinicalandgenetic pages 8-10): Alessandro Geroldi, Andrea La Barbera, Alessia Mammi, Paola Origone, Andrea Gaudio, Clarissa Ponti, Francesca Sanguineri, Sabrina Matà, Martina Sperti, Ilaria Carboni, Emilia Bellone, Fabio Gotta, Chiara Gemelli, Sara Massucco, Guglielmino Valeria, Lucio Marinelli, Marina Grandis, Giulia Bisogni, Mario Sabatelli, Giuseppe Piscosquito, Gabriella Esposito, Angelo Schenone, Fiore Manganelli, Paola Mandich, Stefano Tozza, and Marco Luigetti. Clinical and genetic features of cmt2t in italian patients confirm the importance of mme pathogenic variants in idiopathic, late‐onset axonal neuropathies. Journal of the Peripheral Nervous System, 29:472-486, Sep 2024. URL: https://doi.org/10.1111/jns.12657, doi:10.1111/jns.12657. This article has 2 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Charcot-Marie-Tooth_Disease_Axonal_Type_2T-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.