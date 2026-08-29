---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-08-26T22:35:36.436325'
end_time: '2026-08-26T22:35:36.441752'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Photosensitive Epilepsy
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
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Photosensitive_Epilepsy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Photosensitive Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Photosensitive Epilepsy** covering all of the
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
- **Disease Name:** Photosensitive Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Photosensitive Epilepsy** covering all of the
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


# Photosensitive Epilepsy: Disease Characteristics Research Report

## Executive summary

Photosensitive epilepsy (PSE) is not one uniform monogenic disorder. It is a visually provoked reflex epilepsy phenotype that occurs most often within genetic generalized epilepsies, but also in focal occipital epilepsy and several developmental or progressive epilepsy syndromes. Its objective biomarker is a photoparoxysmal response (PPR)—occipital or generalized epileptiform activity induced by intermittent photic stimulation (IPS), pattern stimulation, or comparable real-world visual stimuli. A person may have **pure PSE**, with only visually provoked seizures, or **epilepsy with photosensitivity**, in which visually provoked and spontaneous seizures coexist. PPR without clinical epilepsy can also occur and should not by itself be equated with epilepsy. (brazzo2010mechanismsofaltered pages 12-17, verrotti2012photosensitivityepidemiologygenetics pages 1-2, vaudano2017photosensitiveepilepsyis pages 1-2)

Recent research has reinforced a network model: abnormal visual-cortical excitability combines with deficient alpha-mediated inhibition and altered occipital–frontoparietal–sensorimotor/thalamic connectivity. The strongest routinely applicable diagnostic and pharmacodynamic tool remains standardized IPS-EEG. Recent innovations include virtual-reality stimulation, machine-learning PPR detection, network EEG analysis, and continued use of PPR suppression as a small-sample proof-of-principle platform for antiseizure drugs. (trenite2019suppressionofthe pages 1-2, timar2024functionalnetworkdynamics pages 1-3, moncada2023virtualrealityand pages 1-2)

| Domain | Evidence-backed finding | Suggested ontology terms/IDs | Evidence type/strength |
|---|---|---|---|
| Disease definition / PPR | Photosensitive epilepsy (PSE) is a reflex epilepsy/EEG trait in which flickering light or patterned visual stimuli provoke epileptiform activity; the EEG hallmark is the photoparoxysmal response (PPR), ranging from occipital to generalized spike-wave activity. Pure PSE (only visually induced seizures) should be distinguished from epilepsy with photosensitivity (spontaneous + visually provoked seizures). (brazzo2010mechanismsofaltered pages 12-17, verrotti2012photosensitivityepidemiologygenetics pages 1-2, vaudano2017photosensitiveepilepsyis pages 1-2) | MONDO:0015643 photosensitive epilepsy; MeSH: Epilepsy, Reflex; HPO: Photoparoxysmal response, Reflex seizure, Photosensitivity | Human clinical reviews + human EEG-fMRI background evidence; moderate-strong |
| Major phenotypes | Common seizure phenotypes include generalized tonic-clonic, myoclonic, absence, eyelid myoclonia, and less often focal occipital seizures; in a 2023 pediatric cohort, IPS induced electroclinical seizures in 41.94% and EEG-only discharge in 58.06%. (brazzo2010mechanismsofaltered pages 12-17, zhang2023electroclinicalcharacteristicsof pages 1-2, zhang2023electroclinicalcharacteristicsof pages 2-3) | HPO: Generalized tonic-clonic seizure; Myoclonic seizure; Absence seizure; Eyelid myoclonia; Occipital seizure | Human cohort + reviews; strong for seizure spectrum |
| Age / sex pattern | Onset is usually in childhood/adolescence, often around puberty, with female predominance; the Chinese pediatric cohort reported mean onset 7.8 ± 3.28 years and male:female ratio 1:3.43. (brazzo2010mechanismsofaltered pages 12-17, verrotti2012photosensitivityepidemiologygenetics pages 1-2, zhang2023electroclinicalcharacteristicsof pages 1-2) | HPO: Childhood onset; Adolescent onset; Female predominance | Human cohort + reviews; moderate-strong |
| Triggers / provoking factors | Highest IPS sensitivity is typically around 10–20 Hz; triggers include sunlight flicker, television/screens, video games, LED/light flashes, and patterns; eye-closure sensitivity is prominent in many patients. (trenite2021theimportanceof pages 17-19, zhang2023electroclinicalcharacteristicsof pages 1-2, zhang2023electroclinicalcharacteristicsof pages 2-3, NCT04076410 chunk 1) | HPO: Seizure triggered by flickering light; Eye closure sensitivity; Environmental exposure terms for flashing light/pattern stimulation | Human cohort, trial protocol, reviews; strong |
| Anatomy / systems affected | Primary system: central nervous system, especially visual cortex/occipital cortex with spread to parietal, frontal, sensorimotor, cingulate, supplementary motor, and thalamic networks. (timar2024functionalnetworkdynamics pages 1-3, vaudano2017photosensitiveepilepsyis pages 1-2) | UBERON: brain; occipital lobe / visual cortex; thalamus; anterior cingulate cortex; supplementary motor area | Human EEG-fMRI/network studies; moderate |
| Cell types | Evidence most strongly implicates cortical excitatory-inhibitory microcircuits and thalamocortical neurons; syndrome-associated literature also points to interneuron dysfunction in broader generalized epilepsy biology. (vaudano2017photosensitiveepilepsyis pages 1-2, scheffer2024developmentalandepileptic pages 19-21) | CL: glutamatergic neuron; GABAergic interneuron; thalamic relay neuron | Indirect human mechanistic inference + broader epilepsy evidence; moderate/indirect |
| Core mechanism | Current model favors abnormal visual-network excitability plus impaired inhibitory control rather than a purely local occipital trigger. PSE patients show altered 3–4 Hz connectivity and reduced alpha-related inhibition of visual/sensorimotor networks at rest. (timar2024functionalnetworkdynamics pages 1-3, vaudano2017photosensitiveepilepsyis pages 1-2) | GO: regulation of membrane potential; synaptic transmission, GABAergic; visual perception; neuronal network synchronization; thalamocortical signaling | Human EEG-fMRI + scalp EEG network study; moderate-strong |
| Upstream/downstream pathophysiology | Upstream: genetically influenced susceptibility and visually evoked cortical-thalamocortical hyperexcitability. Downstream: PPR propagation from occipital to distributed frontoparietal/sensorimotor networks, producing myoclonus, absence, or generalized convulsions. (timar2024functionalnetworkdynamics pages 1-3, vaudano2017photosensitiveepilepsyis pages 1-2) | GO: sensory stimulus response; action potential propagation; seizure; neuron-neuron synaptic transmission | Human mechanistic studies + reviews; moderate |
| Genetics | PSE is genetically heterogeneous. Evidence supports susceptibility and syndrome association rather than a single universal causal gene. CHD2 is repeatedly highlighted; photosensitivity also occurs in SCN1A-related Dravet syndrome and in broader epilepsy gene contexts including GABRA1/GABRG2 and SYNGAP1. (vaudano2017photosensitiveepilepsyis pages 1-2, scheffer2024developmentalandepileptic pages 19-21) | Gene terms: CHD2, SCN1A, GABRA1, GABRG2, SYNGAP1; MONDO-linked syndrome annotation as applicable | Human genetic review/primer evidence; moderate, heterogeneous |
| Inheritance | Inheritance is usually complex or syndrome-specific; familial aggregation is recognized, but penetrance/expressivity depend on the underlying epilepsy syndrome or susceptibility background. (brazzo2010mechanismsofaltered pages 12-17, verrotti2012photosensitivityepidemiologygenetics pages 1-2, vaudano2017photosensitiveepilepsyis pages 1-2) | HPO: Family history of seizures; inheritance term often multifactorial/variable | Reviews + limited cohort observations; moderate |
| Diagnostics | Standard diagnosis relies on EEG with intermittent photic stimulation (IPS), often across eye-open, eyes-closed, and eye-closure conditions, with quantification by standardized photosensitivity range (SPR). Differential diagnosis includes migraine/headache disorders, nonepileptic visual discomfort, and focal occipital epilepsies/syndromes. (verrotti2012photosensitivityepidemiologygenetics pages 1-2, zhang2023electroclinicalcharacteristicsof pages 2-3, moncada2023virtualrealityand pages 1-2) | LOINC/EEG term names; HPO: Abnormal EEG with generalized spike-wave complexes; Photoparoxysmal response | Human clinical practice/review + protocol evidence; strong |
| Treatment | Broad-spectrum ASMs are standard; valproate and levetiracetam are repeatedly reported as effective/common choices. In a proof-of-principle trial, cenobamate partially or completely suppressed PPR in most evaluable patients at 250–400 mg. (trenite2019suppressionofthe pages 1-2, zhang2023electroclinicalcharacteristicsof pages 1-2) | NCIT: Valproic Acid; Levetiracetam; Cenobamate; Anticonvulsant therapy | Human cohort + interventional study; moderate for PPR suppression, weaker for long-term seizure control |
| Prevention / non-pharmacologic management | Trigger avoidance is central: reduce exposure to flicker/patterns/screens, use monocular occlusion in acute exposure, and consider protective tinted lenses. A lens protocol cites prior Z1 lens abolition of PPRs in 75.9% of 610 patients. (verrotti2012photosensitivityepidemiologygenetics pages 1-2, trenite2021theimportanceof pages 17-19, NCT04076410 chunk 1) | NCIT/intervention terms: Protective eyewear; Behavioral avoidance; Patient education | Review + clinical trial protocol citing prior large series; moderate |
| Epidemiology | Photosensitivity is reported in about 5–10% of epilepsy overall, but much higher in some syndromes (for example JME, Dravet syndrome). In the 2023 single-center Chinese pediatric sample, PSE represented 7.79% of children with epilepsy. (brazzo2010mechanismsofaltered pages 12-17, timar2024functionalnetworkdynamics pages 1-3, zhang2023electroclinicalcharacteristicsof pages 1-2, vaudano2017photosensitiveepilepsyis pages 1-2) | Epidemiology descriptors only | Human cohort + reviews; moderate |
| Recent developments (2023–2024) | Recent work includes a 2023 pediatric electroclinical cohort, 2023 VR/ML work on automated PPR detection, and a 2024 network study showing frequency- and type-dependent connectivity abnormalities; these advances mainly refine diagnosis/biomarkers rather than establish new disease-specific therapies. (timar2024functionalnetworkdynamics pages 1-3, zhang2023electroclinicalcharacteristicsof pages 1-2, moncada2023virtualrealityand pages 1-2) | Diagnostic biomarker terms; EEG-based digital biomarker | Recent human cohort/computational/preprint evidence; emerging |
| Models / comparative biology | Useful but indirect models include photosensitive baboon and chicken models, plus zebrafish/mouse epilepsy systems for mechanistic and antiseizure screening work; model translation to human PSE remains incomplete. (brazzo2010mechanismsofaltered pages 12-17) | NCBI Taxon terms as applicable; model organism annotation | Preclinical/indirect evidence; limited |
| Major evidence gaps | No single definitive causal gene for all PSE; limited validated biomarkers beyond IPS-EEG/PPR; sparse data on quality of life, long-term prognosis, protective genetic factors, and PSE-specific omics (single-cell, spatial transcriptomic, proteomic, metabolomic, epigenomic) or chromosomal abnormalities. (verrotti2012photosensitivityepidemiologygenetics pages 1-2, timar2024functionalnetworkdynamics pages 1-3, scheffer2024developmentalandepileptic pages 19-21, moncada2023virtualrealityand pages 1-2) | Knowledge gap annotation; no robust ontology ID needed | Evidence gap synthesis; strong confidence in absence/scarcity of data |


*Table: This compact table summarizes evidence-backed findings for a photosensitive epilepsy knowledge-base entry, including disease definition, phenotypes, mechanisms, genetics, diagnostics, treatment, epidemiology, and key gaps. It is designed for ontology-aware curation while avoiding overstatement where evidence is limited or indirect.*

## 1. Disease information

### Definition and terminology

**Photosensitivity** is the neurophysiological tendency for visual stimulation to evoke epileptiform EEG activity. **PSE** is diagnosed when this susceptibility is clinically situated within epilepsy, especially when seizures are reproducibly provoked by flicker or patterns. The PPR is generally stimulus-independent epileptiform activity—occipital spikes, posterior spread, or generalized spike/polyspike-wave—rather than the normal, stimulus-locked photic-driving response. PPR is commonly graded from Waltz type 1 (occipital spikes) through type 4 (generalized spike/polyspike-wave); types 3–4 are most clinically associated with epilepsy. A photomyoclonic response, consisting of frontally dominant muscle artifact time-locked to flashes, is a non-cerebral response and an important diagnostic distinction. (brazzo2010mechanismsofaltered pages 12-17, zhang2023electroclinicalcharacteristicsof pages 2-3, moncada2023virtualrealityand pages 1-2)

**Synonyms/related labels:** photogenic epilepsy, photic-induced epilepsy, visually sensitive epilepsy, visually provoked seizures, visual reflex epilepsy, epilepsy with photosensitivity, pure photosensitive epilepsy, photosensitive occipital lobe epilepsy, and video-game epilepsy. “Jeavons syndrome” is now usually termed **epilepsy with eyelid myoclonia** and is a related syndrome rather than a synonym for all PSE.

### Identifiers

- **MONDO:** MONDO:0015643, *photosensitive epilepsy*. Open Targets recognizes this disease entry but currently returns no associated targets, supporting the conclusion that there is no single universally assigned molecular target. (OpenTargets Search: photosensitive epilepsy)
- **MeSH:** *Epilepsy, Reflex*, D020195; broader *Epilepsy*, D004827. (NCT00784212 chunk 1)
- **ICD-10:** no dedicated PSE code; coding generally falls under G40 epilepsy categories, selected according to focal/generalized syndrome and intractability.
- **ICD-11:** classify under the underlying epilepsy type/reflex-seizure context; no uniquely validated PSE code was established in the retrieved evidence.
- **OMIM/Orphanet:** no single disease-level entry adequately represents all PSE. OMIM entries apply to an underlying monogenic syndrome, where present.
- **Suggested SNOMED/HPO concepts:** photosensitive epilepsy; reflex seizure; photoparoxysmal response; seizure triggered by flickering light.

This report synthesizes **aggregated disease-level resources, published cohorts, mechanistic imaging studies, and trial registries**, not individual EHR records.

## 2. Etiology and risk/protective factors

### Causal and susceptibility factors

PSE usually reflects **genetically influenced network susceptibility plus a visual exposure**. In isolated/common PSE, inheritance is complex and no single causal gene explains most cases. In syndromic disease, a pathogenic variant may cause the broader epilepsy syndrome, with photosensitivity as one variably penetrant feature. Reviews report onset usually before 20 years, a puberty-related peak, female excess, and familial aggregation. (brazzo2010mechanismsofaltered pages 12-17, verrotti2012photosensitivityepidemiologygenetics pages 1-2, vaudano2017photosensitiveepilepsyis pages 1-2)

Relevant genes include:

- **CHD2:** the most consistently emphasized gene for photosensitivity; rare/de novo pathogenic variants cause CHD2-related developmental and epileptic encephalopathy, often with myoclonic and visually sensitive seizures. Human data also show enrichment of rare CHD2 variants among photosensitive epilepsy cases. (vaudano2017photosensitiveepilepsyis pages 1-2, scheffer2024developmentalandepileptic pages 19-21)
- **SCN1A:** pathogenic germline variants cause Dravet syndrome and related epilepsies; approximately 40% of Dravet patients may show photosensitivity, sometimes early in infancy. Photosensitivity is a syndrome feature, not evidence that SCN1A causes ordinary isolated PSE. (brazzo2010mechanismsofaltered pages 12-17, trenite2026howandwhen pages 9-12, scheffer2024developmentalandepileptic pages 19-21)
- **SYNGAP1, GABRA1, GABRG2** and other epilepsy genes can occur in disorders with photosensitivity, but current evidence does not justify treating them as universal PSE genes.
- Historical linkage signals include **6p21, 7q32, and 16p13**, but linkage has not yielded a clinically definitive common causal allele.

For a patient with isolated PSE and no developmental disorder, labeling a rare variant as pathogenic requires standard ACMG/AMP evidence; PPR association alone is insufficient. No recurrent variant, protective allele, carrier frequency, founder mutation, anticipation, or germline-mosaicism rate is established for PSE as a single entity.

### Environmental and lifestyle risk factors

Provocative exposures include high-contrast flicker, television/computer/mobile displays, video games, LED/strobe lighting, sunlight interrupted by trees or railings, reflected sunlight on water or snow, and striped/grating/checkerboard patterns. Red stimulation around 600–700 nm is particularly provocative in susceptible individuals. The most sensitive frequencies commonly lie around 10–20 Hz, although the clinically relevant range is broader and individual-specific. Sleep deprivation, stress, alcohol, medication nonadherence, and prolonged/intense exposure can lower seizure threshold but are **precipitants**, not causes of inherited photosensitivity. (trenite2021theimportanceof pages 17-19, NCT00609245 chunk 1, zhang2023electroclinicalcharacteristicsof pages 1-2, NCT04076410 chunk 1)

### Protective factors and gene–environment interaction

There is no validated genetic protective variant. Environmental protection consists of reducing retinal input or stimulus intensity: increasing viewing distance, reducing screen size/brightness/contrast, avoiding provocative content, maintaining ambient room lighting, taking breaks, and rapidly covering **one eye** rather than merely closing both eyes. Monocular occlusion reduces binocular cortical summation. Blue/red-attenuating lenses can reduce PPR. The Z1 lens reportedly abolished PPR in 75.9% of 610 tested patients, although this is an electrophysiological endpoint and the very dark lens has practical limitations. (trenite2021theimportanceof pages 17-19, NCT04076410 chunk 1)

The central gene–environment chain is: inherited or syndrome-specific network vulnerability → exposure within the individual’s spatial, chromatic, luminance, and frequency sensitivity range → excessive visual-cortical synchronization → propagation to distributed seizure networks.

## 3. Phenotypes

Clinical expression is episodic and ranges from EEG-only PPR to eyelid flutter, eyelid myoclonia, myoclonic jerks, absences, focal visual seizures, and generalized tonic–clonic seizures. Visual aura, headache, nausea, or impaired awareness can accompany events. Generalized tonic–clonic seizures are commonly reported as the most consequential phenotype. Self-induction—waving fingers before the eyes, seeking sunlight, or repeatedly closing the eyes—occurs particularly in epilepsy with eyelid myoclonia or “sunflower” phenotypes. (brazzo2010mechanismsofaltered pages 12-17, trenite2021theimportanceof pages 17-19)

A 2023 single-center Chinese pediatric cohort provides recent quantitative data: PSE constituted 31/398 epilepsy cases (7.79%); mean onset was 7.84 ± 3.28 years; 24/31 were female; IPS induced an electroclinical seizure in 13/31 (41.94%) and EEG-only discharge in 18/31 (58.06%). Eye-closure IPS was positive in 83.87%, versus 41.94% with eyes open and 35.48% with eyes continuously closed. Thirty of 31 had epilepsy with photosensitivity and only one had pure PSE; 28/31 had spontaneous interictal epileptiform discharges. Imaging was normal in all 23 imaged patients. (zhang2023electroclinicalcharacteristicsof pages 1-2, zhang2023electroclinicalcharacteristicsof pages 2-3)

> Exact abstract quote: “The highest range of frequency sensitivity of the IPS test for the induction of EEG epileptic discharge or electroclinical seizures was within 10–20 Hz.” — Zhang et al., published 9 March 2023, DOI: https://doi.org/10.3389/fped.2023.994817. (zhang2023electroclinicalcharacteristicsof pages 1-2)

Suggested HPO annotations include **Generalized tonic-clonic seizure**, **Myoclonic seizure**, **Absence seizure**, **Eyelid myoclonia**, **Focal visual seizure/visual aura**, **Abnormal EEG**, **Generalized spike-and-wave**, **Photoparoxysmal response**, **Seizure triggered by flickering light**, **Eye-closure sensitivity**, and **Childhood/adolescent onset**. Exact current HPO identifiers should be verified against the release used by the knowledge base.

**Quality of life:** trigger avoidance can restrict screen use, education, employment, driving, entertainment, and social participation and can produce anticipatory anxiety. Direct PSE-specific EQ-5D/SF-36 estimates are sparse. The ongoing lens study explicitly measures adherence, autonomy, seizure frequency, tolerability, and perceived quality-of-life improvement, illustrating the present evidence gap. (NCT04076410 chunk 1)

## 4. Genetic and molecular information

PSE is best curated as a **phenotype with heterogeneous genetic architecture**. CHD2 has the most direct association, whereas SCN1A, SYNGAP1, GABRA1/GABRG2, and other genes generally define syndromes in which photosensitivity is one manifestation. The Open Targets disease record has no assigned targets for MONDO:0015643. (OpenTargets Search: photosensitive epilepsy, vaudano2017photosensitiveepilepsyis pages 1-2)

For syndromic testing, variants may be germline de novo or inherited and may include missense, nonsense, frameshift, splice, copy-number, or other loss-of-function changes; functional direction must be determined gene by gene. For example, SCN1A disorders include both loss- and gain-of-function spectra with different treatment implications. No characteristic somatic mutation, chromosomal rearrangement, methylation signature, pathogenic repeat expansion, or population allele frequency defines PSE itself. (scheffer2024developmentalandepileptic pages 19-21)

**Modifier genes and epigenetics:** plausible but unvalidated at clinically actionable PSE-specific levels. Hormonal/developmental effects are suggested by the female and pubertal peak, but a defined endocrine mechanism or epigenetic signature is lacking.

## 5. Environmental information

PSE is not caused by infection, toxin, pollution, radiation injury, smoking, or diet in the usual sense. Its disease-relevant environmental exposure is **visual stimulation**. Artificial media are important real-world exposures: the 1997 Pokémon broadcast reportedly provoked seizures in 685 Japanese children and drove broadcast-safety standards. (zhang2023electroclinicalcharacteristicsof pages 1-2)

Lifestyle management should prioritize regular sleep, ASM adherence, moderation/avoidance of alcohol where relevant, safe screen practices, and individualized recognition of trigger frequencies and patterns. No vaccine, antimicrobial intervention, or infectious-agent annotation is applicable.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream susceptibility:** genetically and developmentally influenced imbalance of excitation and inhibition in visual and generalized epilepsy networks.
2. **Sensory entrainment:** flicker/pattern input activates retinal–geniculate–occipital pathways; provocative frequencies efficiently synchronize cortical populations.
3. **Failure of inhibition:** reduced alpha-related inhibition and altered GABAergic control allow excessive occipital synchronization.
4. **Network recruitment:** pathological 3–4 Hz spike/polyspike-wave activity propagates through parietal, frontal, anterior, sensorimotor, cingulate, supplementary motor, and thalamocortical networks.
5. **Clinical manifestation:** limited propagation produces occipital symptoms or EEG-only PPR; wider recruitment produces eyelid myoclonia, myoclonus, absence, impaired awareness, or bilateral tonic–clonic seizure. (timar2024functionalnetworkdynamics pages 1-3, vaudano2017photosensitiveepilepsyis pages 1-2)

A human EEG-fMRI study of 44 epilepsy patients and 16 controls found greater resting alpha power, smaller alpha-related BOLD decreases in occipital, sensorimotor, anterior cingulate, and supplementary motor cortices, and abnormal connectivity with visual thalamus only in photosensitive epilepsy. The authors concluded that the difference “consists of a decreased alpha-related inhibition of the visual cortex and sensory-motor networks at rest.” Published 20 February 2017; DOI: https://doi.org/10.1093/brain/awx009. (vaudano2017photosensitiveepilepsyis pages 1-2)

A December 2024 preprint analyzing 45 PSE patients found maximal pathological power at 10–20 Hz stimulation, with hypoconnected centroparietal and hyperconnected anterior/anterior–posterior regions in the 3–4 Hz PPR band. Importantly, visual evoked responses were mostly unchanged outside type 4, suggesting that visual-cortex hyperexcitability alone is not sufficient; abnormal large-scale connectivity facilitates propagation. DOI: https://doi.org/10.1101/2024.12.21.24319242. This is emerging, not yet definitive peer-reviewed evidence. (timar2024functionalnetworkdynamics pages 1-3)

> Exact abstract conclusion: “PSE is a network effect modulated by hyperconnected anterior and anterio-posterior regions, accompanied by a hyperexcitable visual cortex.” (timar2024functionalnetworkdynamics pages 1-3)

Suggested annotations: **GO—visual perception; response to light stimulus; regulation of membrane potential; neuron–neuron synaptic transmission; GABAergic synaptic transmission; regulation of neuronal synaptic plasticity; neural-network synchronization. CL—glutamatergic neuron, GABAergic interneuron, cortical neuron, thalamic relay neuron.** No established PSE-specific immune, inflammatory, apoptotic, fibrotic, ischemic, or neurodegenerative mechanism exists, except where an underlying progressive syndrome supplies one.

### Molecular profiling and advanced technologies

No replicated PSE-specific transcriptomic, proteomic, metabolomic, lipidomic, methylomic, single-cell, spatial-transcriptomic, or CRISPR-screen signature is clinically validated. Current advanced profiling is principally systems-level EEG, EEG-fMRI, connectivity analysis, and digital biomarkers. A VR/ML platform under study at Burgos University Hospital integrates programmable VR stimulation, EEG, and automated analysis. (moncada2023virtualrealityand pages 1-2)

> Exact abstract quote: “This system is currently in study with subjects at Burgos University Hospital, Spain.” Published in the 2023 journal volume; DOI: https://doi.org/10.1007/s00521-022-06940-z. (moncada2023virtualrealityand pages 1-2)

## 7. Anatomical structures affected

The primary organ is the **brain/CNS**. The principal initiating tissue is nervous tissue in the bilateral occipital/visual cortex, but PSE is a network disorder rather than a structural occipital lesion. Relevant sites include primary and associative visual cortex, posterior parietal cortex, frontal/premotor cortex, sensorimotor cortex, anterior cingulate, supplementary motor area, pulvinar/posterior thalamus, and other thalamocortical circuitry. In focal photosensitive occipital epilepsy, occipital onset can remain focal or secondarily generalize. Routine MRI is commonly normal. (timar2024functionalnetworkdynamics pages 1-3, zhang2023electroclinicalcharacteristicsof pages 2-3, vaudano2017photosensitiveepilepsyis pages 1-2)

Suggested UBERON terms: **brain, cerebral cortex, occipital lobe, visual cortex, parietal lobe, frontal lobe, motor cortex, anterior cingulate cortex, thalamus, pulvinar nucleus**. Suggested GO cellular components: **neuron projection, axon, dendrite, glutamatergic synapse, GABAergic synapse, voltage-gated ion-channel complex**. There is no characteristic lateralized lesion; generalized PPR is bilateral.

## 8. Temporal development

Typical onset is pediatric or adolescent, commonly around puberty. Reviews cite an approximate 8–19-year onset range and peak near age 12; the recent pediatric cohort showed onset from 1 to 13.92 years. Adult-onset and persistence beyond 50 occur but are less common and warrant careful assessment for focal/acquired epilepsy and medication effects. (brazzo2010mechanismsofaltered pages 12-17, verrotti2012photosensitivityepidemiologygenetics pages 1-2, zhang2023electroclinicalcharacteristicsof pages 2-3)

The course is episodic and exposure-dependent, not continuously progressive in isolated PSE. Photosensitivity may diminish or disappear between ages 20 and 30, but persistence is common enough that medication withdrawal should not be based on age alone. Family history, broader epilepsy syndrome, persistent wide PPR range, spontaneous seizures, and early PPR in disorders such as Dravet syndrome may indicate less favorable outcome. Relapse after ASM withdrawal may approach 50% in selected literature cited by the lens trial. (trenite2021theimportanceof pages 17-19, zhang2023electroclinicalcharacteristicsof pages 2-3, NCT04076410 chunk 1)

## 9. Inheritance and population

Across epilepsy populations, photosensitivity is commonly estimated near **5%**, with some sources using 5–10%; estimates vary with age, syndrome mix, IPS protocol, geography, and whether EEG-only PPR is included. It occurs in approximately 15% of generalized epilepsies in older syntheses and can be substantially higher in juvenile myoclonic epilepsy, Dravet syndrome, absence epilepsies, and progressive myoclonic epilepsies. A 2024 network report states that PSE affects about 5% of epilepsy patients worldwide; the 2023 pediatric specialty-center estimate was 7.79%, while that paper’s review cited 10–20% among children with epilepsy. These are not population incidence estimates and should not be conflated. (brazzo2010mechanismsofaltered pages 12-17, timar2024functionalnetworkdynamics pages 1-3, zhang2023electroclinicalcharacteristicsof pages 1-2)

Females predominate, particularly during adolescence: reported ratios range around 1.5–2 females per male, with 24 females to 7 males (3.43:1) in the recent Chinese cohort. No robust annual incidence per 100,000, ethnic-specific carrier frequency, consanguinity effect, or universal penetrance estimate is available. Inheritance is multifactorial for ordinary PSE and follows the underlying syndrome—often autosomal dominant/de novo—for monogenic cases. Expressivity and penetrance are variable. (brazzo2010mechanismsofaltered pages 12-17, verrotti2012photosensitivityepidemiologygenetics pages 1-2, zhang2023electroclinicalcharacteristicsof pages 1-2)

## 10. Diagnostics

### Standard clinical approach

Diagnosis requires: (1) detailed seizure history linked to visual exposure; (2) syndrome classification; and (3) EEG with standardized IPS, generally testing eye closure, eyes closed, and eyes open. Pattern stimulation is useful if patterned images are suspected. IPS proceeds through ascending and descending standard frequencies and stops promptly when generalized PPR emerges. The **standardized photosensitivity range (SPR)** is the number/range of flash frequencies evoking PPR and serves as a reproducible quantitative biomarker. (NCT00609245 chunk 1, NCT03686033 chunk 1, zhang2023electroclinicalcharacteristicsof pages 2-3)

The 2023 study used 1–60 Hz IPS, 10-second trains separated by at least seven seconds, and terminated stimulation when PPR appeared to reduce seizure risk. Clinical laboratories should follow current IFCN/ILAE-compatible protocols rather than reproduce research settings without safeguards. (timar2024functionalnetworkdynamics pages 1-3, zhang2023electroclinicalcharacteristicsof pages 2-3)

MRI is indicated when focal onset, abnormal examination, developmental regression, or acquired pathology is suspected, but isolated/genetic PSE commonly has normal structural imaging. There is no diagnostic blood, urine, CSF, biopsy, PET, proteomic, or metabolomic biomarker. (zhang2023electroclinicalcharacteristicsof pages 2-3)

### Genetic testing

Genetic testing is not mandatory for otherwise typical isolated PSE. Use an epilepsy multigene panel or exome/genome sequencing when onset is infantile, seizures are drug-resistant, development is abnormal/regressing, dysmorphism or movement disorder exists, family history is strong, or a syndrome such as CHD2-, SCN1A-, or SYNGAP1-related epilepsy is suspected. Trio testing improves de novo-variant interpretation. CMA is appropriate for developmental disability/congenital anomalies; mitochondrial, repeat-expansion, or single-gene testing should be phenotype-driven. No newborn or general-population screening program exists.

### Differential diagnosis

Rule out normal photic driving/photomyoclonic response, migraine aura, photophobia without epilepsy, syncope, psychogenic nonepileptic events, tics/stereotypies, retinal disease, and focal structural occipital epilepsy. Migraine visual symptoms usually evolve more slowly and last longer; epileptic visual phenomena tend to be brief, stereotyped, and may progress to impaired awareness or motor seizure. A PPR in an asymptomatic person indicates susceptibility, not automatically epilepsy. (verrotti2012photosensitivityepidemiologygenetics pages 1-2, moncada2023virtualrealityand pages 1-2)

## 11. Outcome and prognosis

Isolated PSE generally has a favorable survival outlook and is not known to reduce life expectancy independently. There are no credible PSE-specific 5- or 10-year survival statistics. Mortality and SUDEP risk are governed principally by the underlying epilepsy, especially ongoing generalized tonic–clonic seizures, nocturnal seizures, drug resistance, and adherence—not photosensitivity alone.

Morbidity includes injury during provoked seizures, driving restrictions, educational/occupational limitations, anxiety, avoidance behavior, and adverse effects of ASMs. Photosensitivity may remit in early adulthood, but spontaneous epilepsy may persist after PPR disappears. Conversely, PPR can remain without frequent real-world seizures. A wide or persistent SPR and clinical symptoms during IPS imply greater daily-life seizure likelihood. (trenite2021theimportanceof pages 17-19, zhang2023electroclinicalcharacteristicsof pages 2-3)

## 12. Treatment

### Management algorithm

1. Classify the underlying epilepsy and distinguish EEG-only PPR from clinically significant visually provoked seizures.
2. Educate regarding triggers and emergency monocular occlusion.
3. If events are rare and exclusively avoidable, environmental control may suffice.
4. If spontaneous seizures coexist, exposures cannot be reliably avoided, or events include impaired awareness/generalized convulsions, use an ASM appropriate to the entire syndrome.
5. Reassess clinical seizures and, when useful, SPR/PPR; do not infer long-term seizure freedom solely from acute PPR suppression.

**Valproate** is historically the most effective broad-spectrum option for generalized photosensitive epilepsies; it increases inhibitory tone and has multiple ion-channel effects. Its major limitations are teratogenicity, weight/metabolic effects, tremor, and other toxicity, making it inappropriate or tightly restricted for many people who could become pregnant. **Levetiracetam** (SV2A ligand) is frequently used and avoids teratogenic risk to the same degree, though behavioral adverse effects occur. Lamotrigine, topiramate, brivaracetam, and syndrome-specific therapies may be considered. Sodium-channel blockers can aggravate myoclonus or absence in some generalized epilepsies, so treatment must follow syndrome—not simply the presence of PPR. In the 2023 cohort, valproate and levetiracetam were the common effective mono/combination therapies, but the observational design does not establish comparative efficacy. (NCT00401648 chunk 1, zhang2023electroclinicalcharacteristicsof pages 1-2)

**Cenobamate evidence:** in a six-patient phase 2a proof-of-principle study, 250 mg yielded complete PPR suppression in 1/4 and partial suppression in 4/4; 400 mg yielded complete suppression in 1/4 and partial suppression in 2/4. Exposure of 201–400 μg·h/mL produced partial suppression in 4/6 (66%); common adverse events were dizziness and somnolence. This was Class III evidence for acute PPR suppression, not a long-term PSE effectiveness trial. Published August 2019; DOI: https://doi.org/10.1212/WNL.0000000000007894; NCT00616148. (trenite2019suppressionofthe pages 1-2)

Other PPR-model studies include completed brivaracetam phase 2 (NCT00401648; n=20), valproate phase 4 (NCT00609245; n=13), and the AMPA/kainate antagonist selurampanel/BGG492 phase 2 (NCT00784212; n=13; associated PMID **25963722**). These studies demonstrate pharmacodynamic effects but are too small to define routine long-term treatment algorithms. (NCT00401648 chunk 1, NCT00609245 chunk 1, NCT00784212 chunk 1)

**Recent/experimental activity:**

- **NPT 2042**, 160 or 240 mg, completed a randomized quadruple-masked phase 1 crossover PPR study in five adults (NCT06525649; started 21 August 2024, completed 26 June 2025); no outcome results were available in the retrieved record. (NCT06525649 chunk 1)
- Inhaled CBD **RLS103** (4/8 mg) was terminated for poor enrollment after only two participants (NCT05678881), illustrating the feasibility limitations of this rare biomarker population. (NCT05678881 chunk 1)
- E2082 phase 2 enrolled eight and was terminated after safety review (NCT03686033). (NCT03686033 chunk 1)
- A pediatric lens study, NCT04076410, compares four new spectral lenses with Z1; its registry status was unknown after a last known active-not-recruiting state, with estimated completion in January 2026. (NCT04076410 chunk 1)

No gene, cell, RNA, immune, or surgical therapy is approved specifically for isolated PSE. Surgery is relevant only if a discrete focal epileptogenic lesion exists. Suggested NCIT intervention concepts: **Anticonvulsant Therapy, Valproic Acid, Levetiracetam, Brivaracetam, Cenobamate, Cannabidiol, Protective Eyewear, Patient Education**.

## 13. Prevention

**Primary prevention of genetic susceptibility is unavailable.** Public-health prevention can reduce provoked events through broadcast, game, web-animation, nightclub/strobe, and workplace-lighting standards controlling flash frequency, luminance contrast, red saturation, patterned area, and screen coverage. The Pokémon event demonstrates the potential population impact of unsafe content. (zhang2023electroclinicalcharacteristicsof pages 1-2)

**Secondary prevention** consists of early recognition, standardized IPS-EEG in appropriately selected patients, syndrome diagnosis, and genetic evaluation where developmental or severe disease suggests a monogenic cause. Routine screening of asymptomatic people is not recommended.

**Tertiary prevention** includes individualized trigger avoidance, adherence, adequate sleep, responsible alcohol use, protective lenses, seizure first-aid planning, and control of generalized tonic–clonic seizures. During unexpected exposure, turn away and cover one eye with the palm; simply squeezing both eyes shut can retain flicker transmission and may itself provoke eye-closure-sensitive PPR. (trenite2021theimportanceof pages 17-19, NCT04076410 chunk 1)

Genetic counseling should explain heterogeneous inheritance and avoid assigning Mendelian recurrence risk without a molecular diagnosis. If a pathogenic syndrome-causing variant is found, cascade, prenatal, or preimplantation testing can be discussed according to that disorder.

## 14. Other species and natural disease

Naturally photosensitive epilepsy-like phenotypes are best documented in **Papio papio** baboons (NCBI Taxonomy: *Papio papio*) and photosensitive chicken lines, historically including Fayoumi-derived strains. Baboons develop generalized epileptiform responses and seizures to photic stimulation and are valuable for generalized network physiology and pharmacology. Chicken models provide strong reflex photosensitivity but differ substantially from human cortical organization. Neither condition is zoonotic or transmissible. (brazzo2010mechanismsofaltered pages 12-17)

Domestic dogs and cats may have reflex seizures, but there is insufficient evidence to define a common veterinary analogue of human PSE or to assign a validated VBO breed term. Comparative orthologue annotations should be attached to the specific modeled gene—such as **Chd2/CHD2** or **Scn1a/SCN1A**—rather than to PSE globally.

## 15. Model organisms

Relevant systems include genetic generalized epilepsy in baboons; photosensitive chicken strains; zebrafish and mouse models of CHD2-, SCN1A-, GABA-receptor-, or other syndrome-associated epilepsies; and acute chemoconvulsant models. Zebrafish permit high-throughput behavioral/electrophysiological drug screening, while mice permit cell-type and circuit manipulation. BRD2-haploinsufficient mice, for example, show reduced GABAergic neuronal populations and sex-specific seizure susceptibility, but they are an indirect generalized-epilepsy model rather than a validated model of human PSE. (vaudano2017photosensitiveepilepsyis pages 1-2, scheffer2024developmentalandepileptic pages 19-21)

Key limitations are species-specific visual systems, stimulation paradigms, developmental timing, and failure to reproduce the full human combination of PPR, subjective visual symptoms, spontaneous seizures, and psychosocial burden. Models are therefore most suitable for studying excitation–inhibition balance, visual-network propagation, gene function, and initial ASM screening—not for directly predicting clinical effectiveness.

## Evidence appraisal and knowledge gaps

The strongest current evidence concerns the electroclinical phenotype, standardized IPS-EEG, age/sex distribution, visual triggers, and network physiology. Major gaps are population incidence, prospective natural history, PSE-specific quality-of-life measures, protective genetics, validated molecular biomarkers, comparative long-term ASM trials, and disease-specific omics. Recent 2023–2024 work improves pediatric characterization and network/digital biomarker analysis but has not produced a new disease-specific standard therapy. The 2024 connectivity work remains a preprint and should be curated accordingly. (timar2024functionalnetworkdynamics pages 1-3, zhang2023electroclinicalcharacteristicsof pages 1-2, moncada2023virtualrealityand pages 1-2)

Finally, most medication studies use **acute PPR/SPR suppression as a surrogate endpoint**. This model is sensitive and valuable for early drug development, but acute electrophysiological suppression must not be represented as equivalent to durable prevention of spontaneous or real-world visually provoked seizures. (NCT00609245 chunk 1, trenite2019suppressionofthe pages 1-2)

References

1. (brazzo2010mechanismsofaltered pages 12-17): Mechanisms of altered cortical excitability in photosensitive epilepsy This article has 1 citations.

2. (verrotti2012photosensitivityepidemiologygenetics pages 1-2): Alberto Verrotti, Francesca Beccaria, Federica Fiori, Alessandra Montagnini, and Giuseppe Capovilla. Photosensitivity: epidemiology, genetics, clinical manifestations, assessment, and management. Epileptic Disorders, 14:349-362, Dec 2012. URL: https://doi.org/10.1684/epd.2012.0539, doi:10.1684/epd.2012.0539. This article has 77 citations and is from a peer-reviewed journal.

3. (vaudano2017photosensitiveepilepsyis pages 1-2): Anna Elisabetta Vaudano, Andrea Ruggieri, Pietro Avanzini, Giuliana Gessaroli, Gaetano Cantalupo, Antonietta Coppola, Sanjay M. Sisodiya, and Stefano Meletti. Photosensitive epilepsy is associated with reduced inhibition of alpha rhythm generating networks. Brain, 140:981–997, Apr 2017. URL: https://doi.org/10.1093/brain/awx009, doi:10.1093/brain/awx009. This article has 72 citations and is from a highest quality peer-reviewed journal.

4. (trenite2019suppressionofthe pages 1-2): Dorothee G.A. Kasteleijn- Nolst Trenite, Bree D. DiVentura, John R. Pollard, Gregory L. Krauss, Sarah Mizne, and Jacqueline A. French. Suppression of the photoparoxysmal response in photosensitive epilepsy with cenobamate (ykp3089). Neurology, 93:e559-e567, Aug 2019. URL: https://doi.org/10.1212/wnl.0000000000007894, doi:10.1212/wnl.0000000000007894. This article has 61 citations and is from a highest quality peer-reviewed journal.

5. (timar2024functionalnetworkdynamics pages 1-3): Lili Timar, Sina Deplazes, Julia Bothmann, Roland Renzel, Debora Ledergerber, Tena Dubcek, and Lukas Imbach. Functional network dynamics in photosensitive epilepsy depend on stimulation frequency and photosensitivity type. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.21.24319242, doi:10.1101/2024.12.21.24319242. This article has 0 citations.

6. (moncada2023virtualrealityand pages 1-2): Fernando Moncada, Sofía Martín, Víctor M. González, Víctor M. Álvarez, Beatriz García-López, Ana Isabel Gómez-Menéndez, and José R. Villar. Virtual reality and machine learning in the automatic photoparoxysmal response detection. Neural Computing and Applications, 35:5643-5659, Jan 2023. URL: https://doi.org/10.1007/s00521-022-06940-z, doi:10.1007/s00521-022-06940-z. This article has 30 citations and is from a peer-reviewed journal.

7. (zhang2023electroclinicalcharacteristicsof pages 1-2): Bo Zhang, Tianyu Chen, Xiaosheng Hao, Meiying Xin, and Jianmin Liang. Electroclinical characteristics of photosensitive epilepsy: a retrospective study of 31 chinese children and literature review. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.994817, doi:10.3389/fped.2023.994817. This article has 4 citations.

8. (zhang2023electroclinicalcharacteristicsof pages 2-3): Bo Zhang, Tianyu Chen, Xiaosheng Hao, Meiying Xin, and Jianmin Liang. Electroclinical characteristics of photosensitive epilepsy: a retrospective study of 31 chinese children and literature review. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.994817, doi:10.3389/fped.2023.994817. This article has 4 citations.

9. (trenite2021theimportanceof pages 17-19): The Importance of Photosensitivity for Epilepsy This article has 7 citations.

10. (NCT04076410 chunk 1): Ana Checa-Ros, MD, PhD. Efficacy of Lenses in Abolishing Photoparoxysmal Responses. Aston University. 2021. ClinicalTrials.gov Identifier: NCT04076410

11. (scheffer2024developmentalandepileptic pages 19-21): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 167 citations.

12. (OpenTargets Search: photosensitive epilepsy): Open Targets Query (photosensitive epilepsy, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

13. (NCT00784212 chunk 1):  Effect of BGG492 on EEG in Patients With Photosensitive Epilepsy. Novartis Pharmaceuticals. 2008. ClinicalTrials.gov Identifier: NCT00784212

14. (trenite2026howandwhen pages 9-12): Dorothee Kasteleijn-Nolst Trenite and Boulenouar Mesraoua. How and When to Treat Visually-Evoked Seizures. IntechOpen, May 2026. URL: https://doi.org/10.5772/intechopen.1015299, doi:10.5772/intechopen.1015299. This article has 0 citations.

15. (NCT00609245 chunk 1): Bassel Abou-Khalil. Effect of Valproic Acid Concentration on Photic Response. Vanderbilt University Medical Center. 2007. ClinicalTrials.gov Identifier: NCT00609245

16. (NCT03686033 chunk 1):  A Study to Evaluate the Pharmacodynamic Activity of E2082 in Adult Participants With Photosensitive Epilepsy. Eisai Inc.. 2018. ClinicalTrials.gov Identifier: NCT03686033

17. (NCT00401648 chunk 1):  Effect of Brivaracetam in Photosensitive Epileptic Subjects. UCB Pharma. 2002. ClinicalTrials.gov Identifier: NCT00401648

18. (NCT06525649 chunk 1):  A Double Blind, Randomized, Cross-over Study Examining the Suppression of the Photoparoxysmal EEG Response With NPT 2042. NeuroPro Therapeutics, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06525649

19. (NCT05678881 chunk 1):  Safety, Tolerability, and Efficacy of RLS103 in a Clinical Model of Photosensitive Epilepsy. Receptor Life Sciences. 2022. ClinicalTrials.gov Identifier: NCT05678881

## Artifacts

- [Edison artifact artifact-00](Photosensitive_Epilepsy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.