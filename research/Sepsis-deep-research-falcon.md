---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-15T11:38:15.318499'
end_time: '2026-09-15T11:51:33.161847'
duration_seconds: 797.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sepsis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 48
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Sepsis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sepsis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sepsis** covering all of the
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
- **Disease Name:** Sepsis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sepsis** covering all of the
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


# Sepsis: Comprehensive Disease-Characteristics Report

## Executive summary

Sepsis is an acute, life-threatening syndrome in which infection triggers a dysregulated host response and new organ dysfunction. It is not synonymous with infection, bacteremia, or systemic inflammatory response syndrome (SIRS). Under Sepsis-3, adult clinical operationalization is suspected/documented infection plus an acute increase in Sequential Organ Failure Assessment (SOFA) score of at least 2 points. Septic shock is the higher-risk subset requiring vasopressors to maintain mean arterial pressure (MAP) at least 65 mmHg and having lactate above 2 mmol/L despite adequate volume resuscitation. Reported mortality is approximately 15–25% for sepsis and 30–50% for septic shock, varying substantially by case mix and health-system capacity (hotchkiss2016sepsisandseptic pages 1-2).

Sepsis is a complex, heterogeneous syndrome rather than a Mendelian disease. Its biology comprises simultaneously evolving pathogen burden, innate inflammatory activation, endothelial and microvascular injury, coagulation/complement activation, metabolic dysfunction, and immune suppression. This heterogeneity explains why rapid antimicrobials, source control, and physiologic support remain more successful than non-stratified immunomodulation (hotchkiss2016sepsisandseptic pages 5-6, hotchkiss2016sepsisandseptic pages 9-10, sebastian2025sepsisandpostsepsis pages 8-10).

## 1. Disease information

### Definition, names, and identifiers

**Preferred name:** sepsis. **Synonyms/related terms:** septicemia/septicaemia, blood poisoning, systemic infection, severe sepsis, septic shock, infection-associated organ dysfunction. “Septicemia” and “blood poisoning” are imprecise legacy terms; bacteremia may be absent, and “severe sepsis” is redundant under Sepsis-3.

Key suggested identifiers are:

- **MeSH:** Sepsis, D018805.
- **ICD-10-CM:** A40.- streptococcal sepsis; A41.- other sepsis; A41.9 unspecified-organism sepsis; R65.20 severe sepsis without shock; R65.21 severe sepsis with septic shock. Coding rules require the underlying infection/organism and acute organ dysfunction where applicable.
- **ICD-11:** sepsis without versus with septic shock concepts should be verified against the implementation’s current release.
- **MONDO:** retrieved disease-level mappings include **MONDO:0005229**, bacterial infectious disease with sepsis, and **MONDO:1040015**, infectious disease with sepsis. A general “sepsis” MONDO identifier should be release-verified rather than inferred from the Open Targets HPO-derived entry (OpenTargets Search: sepsis).
- **OMIM/Orphanet:** not applicable as a single inherited or rare disease entity. Rare monogenic immunodeficiencies can predispose to invasive infection and sepsis, but are distinct diagnoses.

Sepsis knowledge comes from both **individual-level data**—EHR-derived vital signs, laboratory results, cultures, medications and outcomes—and **aggregated resources**, including registries, administrative claims, cohorts, trials, guidelines and ontologies. Definition and coding variation materially alter estimated incidence (ljungstrom2019incidencesofcommunity pages 12-13, hotchkiss2016sepsisandseptic pages 1-2).

## 2. Etiology, risk, and protective factors

### Causal factors and infectious agents

The necessary upstream trigger is infection, most often pneumonia, urinary infection, intra-abdominal infection, bloodstream/device infection, or skin/soft-tissue infection. Bacteria predominate, but fungi, viruses and parasites can cause the syndrome. In one small cohort represented in a systematic-review evidence table, isolates were 48.7% Gram-negative, 31.6% Gram-positive and 14.5% fungal; this is illustrative rather than globally representative. Another cohort’s sources were urinary 30.4%, abdominal 26.6%, pulmonary 25.3%, other 6.3% and undetermined 11.4% (hodgsonUnknownyeararticletitlehealthrelated pages 15-16).

Typical agents include *Escherichia coli*, *Klebsiella pneumoniae*, *Pseudomonas aeruginosa*, *Staphylococcus aureus*, streptococci, enterococci, anaerobes, *Candida* spp., influenza virus and SARS-CoV-2. Pathogen distribution depends on age, site, community versus hospital acquisition, geography, immune status and antimicrobial exposure. Culture negativity—reported in up to 30%—does not exclude sepsis (hotchkiss2016sepsisandseptic pages 12-13).

### Host and environmental risk factors

Major risks include neonatal or advanced age, male sex in some older populations, frailty, diabetes, chronic kidney/liver/lung disease, cancer, immunosuppression, pregnancy/postpartum states, major surgery, trauma or burns, invasive devices, hospitalization, prior antimicrobials and resistant-organism exposure. In a Swedish population study, incidence increased more than forty-fold from the youngest to oldest groups; median age was 78 years, and men aged at least 85 had approximately 70% higher severe-sepsis incidence than women of similar age (ljungstrom2019incidencesofcommunity pages 12-13).

Environmental and health-system modifiers include sanitation, vaccination coverage, crowding, air pollution insofar as it increases respiratory disease, occupational injury, access to primary and obstetric care, delayed recognition, antimicrobial resistance, and limited laboratory/ICU capacity. Smoking, hazardous alcohol use, malnutrition, inactivity and obesity influence infection, cardiopulmonary reserve or recovery, but are neither necessary nor sufficient causes.

**Protective factors** are mainly infection prevention and physiological reserve: age-appropriate vaccination, hand hygiene, safe surgery/childbirth, catheter bundles, antimicrobial stewardship, prompt treatment of localized infection, nutrition, mobility and chronic-disease control. No validated common “protective allele” is used clinically.

### Gene–environment interaction

Host genotype affects pathogen recognition and cytokine, leukocyte, endothelial and coagulation responses, but effect size depends on organism, infection site, ancestry, antimicrobial susceptibility, treatment timing and comorbidity. Examples include a TLR4 haplotype associated with acquisition in Han Chinese (OR 1.59), CD14 rs2569190 with septic shock (OR 1.72), TREM1 rs2234246 with shock (OR 3.10), and TREM1 rs5743661 with 30-day mortality after Gram-positive sepsis (OR 4.88); inconsistent replication prevents clinical use (giamarellosbourboulis2016theroleof pages 4-5). This context dependence is a genuine gene–environment interaction problem, not evidence of deterministic inheritance (sutherland2009benchtobedsidereviewassociation pages 1-2).

## 3. Phenotypes

Sepsis may occur at any age. Onset is usually acute over hours to days; severity and manifestations fluctuate with infection source, host reserve and treatment.

- **Constitutional signs:** fever (HP:0001945), hypothermia (HP:0002045), chills, malaise and weakness. Temperature can be normal, especially in neonates, older or immunosuppressed patients.
- **Cardiovascular signs:** tachycardia (HP:0001649), hypotension (HP:0002615), delayed capillary refill, mottling, vasoplegia and shock; myocardial depression may affect both ventricles, and mild troponin elevation is common but nonspecific (hotchkiss2016sepsisandseptic pages 9-10).
- **Respiratory:** tachypnea (HP:0002789), hypoxemia (HP:0012418), pulmonary edema and ARDS. Alveolar-capillary injury lowers compliance and gas exchange. In the Swedish study, 78% of Sepsis-3 cases qualified through respiratory dysfunction alone, illustrating the sensitivity of epidemiology to oxygen-based SOFA classification (ljungstrom2019incidencesofcommunity pages 12-13, hotchkiss2016sepsisandseptic pages 9-10).
- **Neurologic/behavioral:** altered consciousness, delirium (HP:0031258), agitation, somnolence and encephalopathy (HP:0001298). Long-term cognitive, anxiety, depressive and post-traumatic symptoms may persist.
- **Renal:** oliguria (HP:0100520), rising creatinine, electrolyte/acid-base abnormalities and AKI.
- **Hematologic/coagulation:** thrombocytopenia (HP:0001873), prolonged coagulation tests, microthrombosis, bleeding and disseminated intravascular coagulation (HP:0001928 broadly).
- **Hepatic/metabolic:** hyperbilirubinemia (HP:0002904), cholestasis, hypoglycemia or hyperglycemia, metabolic acidosis and hyperlactatemia.
- **Gastrointestinal/musculoskeletal:** ileus, feeding intolerance, catabolism, ICU-acquired weakness and lean-tissue loss.

Phenotype frequency cannot be represented by one universal percentage because cohorts use different definitions and infection sources. Severity ranges from reversible single-organ dysfunction to rapidly progressive multiorgan failure. Per-phenotype quality-of-life effects include impaired mobility/self-care from weakness, inability to work, cognitive and emotional disability after encephalopathy/delirium, and chronic dialysis or dyspnea after organ injury. In a 2023 German claims study of 7,370 previously employed working-age survivors, 69.2% returned to work by six months and 76.9% by 12 months; at one year, 9.8% remained on sick leave and 13.3% had retired early (DOI: https://doi.org/10.3389/fmed.2023.1187809; published May 2023) (fleischmannstruzek2023returntowork pages 8-8).

## 4. Genetic and molecular information

### Disease architecture

There is **no single causal sepsis gene**, characteristic chromosomal abnormality, Mendelian inheritance, penetrance, anticipation, carrier frequency, founder mutation or germline-mosaicism framework. Sepsis susceptibility and outcomes are multifactorial and polygenic. Consequently, ClinVar-style “pathogenic/likely pathogenic” classification is generally inappropriate for common sepsis-associated variants; they are susceptibility or prognostic associations. Somatic clonal hematopoiesis genes such as TET2/SRSF2 are emerging disease modifiers, not causes of sepsis. Open Targets associations also prominently include adrenergic receptors and F8 because of therapeutic/clinical evidence; these should not be mislabeled causal genes (OpenTargets Search: sepsis).

### Variant evidence

A GWAS of 832 septic-shock patients identified 139 death-associated SNPs at 5% FDR. Candidate loci included **CYP11B2/PTPN11** for early death and **FER, CISH, MAPKAPK3** for late death. The top regulatory candidate, **rs143356980**, lies near **CISH** in a monocyte/T-cell super-enhancer; CRISPR deletion and reporter assays supported enhancer function, with the T allele reducing activity relative to C. However, the reported very large multilocus early/late death-risk estimates require independent replication (DOI: https://doi.org/10.3390/ijms22115852; published May 2021) (rosier2021geneticpredispositionto pages 16-18, rosier2021geneticpredispositionto pages 1-2).

The FER rs4957796-C allele has an approximately 20% European frequency and was associated with lower mortality in pneumonia-related sepsis in one study but not replicated for 28-day mortality in another. TNF rs1800629 and TLR4 Asp299Gly/Thr399Ile are classic inconsistent candidate associations (rosier2021geneticpredispositionto pages 1-2, sutherland2009benchtobedsidereviewassociation pages 1-2).

### Epigenetics and testing

Stimulus- and cell-specific chromatin accessibility, DNA methylation, histone modifications and trained immunity/tolerance can sustain immune reprogramming. CISH enhancer effects illustrate regulatory genetics, but not a diagnostic epigenetic lesion. Sepsis-related epigenomics remains investigational; cfDNA methylation is being tested as a tissue-of-origin and immune-injury biomarker (NCT06817408) (NCT06817408 chunk 1).

Routine WGS, WES, panels, CMA, karyotype, FISH, mtDNA or repeat-expansion testing is **not recommended for sepsis itself**. Genetic evaluation is appropriate only when recurrent/unusual infection suggests an underlying inborn error of immunity, metabolic disorder or other independent diagnosis. Current associations lack replication, ancestry generalizability and incremental clinical utility beyond age, comorbidity and physiological severity (sutherland2009benchtobedsidereviewassociation pages 1-2, sutherland2009benchtobedsidereviewassociation pages 6-7).

## 5. Environmental information

Sepsis is not directly caused by a toxin or radiation in the usual disease definition. Relevant exposures operate by increasing infection or reducing reserve: contaminated water/food, poor sanitation, healthcare-associated resistant organisms, wounds/trauma, invasive devices, occupational exposure to pathogens, malnutrition, smoke/air pollution and limited healthcare access. Antibiotic exposure selects resistant microbiota and changes empiric-treatment adequacy. LPS is a bacterial PAMP and experimental trigger, not usually a standalone environmental cause of human sepsis.

Lifestyle modification reduces background infection and comorbidity risk but cannot reliably prevent all sepsis. Smoking cessation, moderated alcohol use, physical activity, adequate protein/calorie intake, oral health, skin/foot care in diabetes, and adherence to chronic-disease therapy are reasonable population measures.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Trigger/upstream sensing:** local or disseminated microbes release PAMPs; injured cells release DAMPs. TLRs, NOD-like receptors, dectins, RAGE and nucleic-acid sensors activate NF-κB, AP-1 and IRF3/7 (GO:0045087 innate immune response; GO:0002224 TLR signaling) (hotchkiss2016sepsisandseptic pages 5-6).
2. **Mediator amplification:** macrophages, monocytes, dendritic cells, neutrophils and endothelium produce TNF, IL-1, IL-6, chemokines and interferons (GO:0019221). Complement C3a/C4a/C5a amplifies leukocyte recruitment and injury (GO:0006956) (vella2025cytokinesinsepsis pages 10-11).
3. **Barrier/coagulation failure:** activated endothelium becomes adhesive, permeable and procoagulant; platelets, fibrin and neutrophils generate immunothrombi. Capillary leak causes edema, while microvascular flow heterogeneity and thrombosis impair oxygen/nutrient delivery (GO:0007596; GO:0030168) (hotchkiss2016sepsisandseptic pages 9-10).
4. **Cell/tissue injury:** ROS, proteases, extracellular histones, complement, mitochondrial dysfunction, apoptosis and inflammatory cell death injure parenchyma. NETs capture organisms but expose histones/proteases that damage endothelium (GO:0140725) (vella2025cytokinesinsepsis pages 10-11).
5. **Organ manifestations:** alveolar-capillary leak → hypoxemia/ARDS; vasodilation, leak and cardiodepression → hypotension; microvascular/metabolic tubular stress → AKI; BBB/neuroimmune dysfunction → delirium; cholestasis/hypoxia → bilirubin rise; platelet/coagulation consumption → thrombocytopenia/DIC (hotchkiss2016sepsisandseptic pages 9-10).
6. **Concurrent immune suppression:** T/B/dendritic-cell apoptosis, lymphopenia, reduced monocyte MHC-II/HLA-DR, PD-1/PD-L1 signaling, regulatory/TH2 skewing and IL-10/TGF-β impair pathogen clearance and predispose to secondary infection. In human sepsis, stimulated lymphocyte pro-inflammatory/TH1 cytokine production was reported below 10% of non-septic controls; persistent lymphopenia predicts mortality (hotchkiss2016sepsisandseptic pages 5-6).
7. **Recovery or persistence:** successful source control and organ support permit resolution; otherwise persistent inflammation, immunosuppression and catabolism produce chronic critical illness/post-sepsis syndrome.

### Molecular profiling and advanced technologies

Bulk transcriptomics has defined immune-response endotypes. Pneumonia-associated **SRS1** is relatively immunosuppressed and high-risk versus **SRS2**; an IFNγ/CXCL9-driven endotype may represent about 20% of cases and is now being therapeutically selected in EMBRACE. Eleven-gene host-response panels can distinguish sepsis from sterile inflammation in research settings, but endotypes are platform- and cohort-dependent (sebastian2025sepsisandpostsepsis pages 8-10).

Proteomics, metabolomics and lipidomics repeatedly implicate complement/coagulation, extracellular matrix, leukocyte migration, amino-acid depletion, mitochondrial/bioenergetic dysfunction and altered lipid mediators. A 2024 pilot proteomics study found 174 differentially expressed proteins and proposed plasma SPP1/osteopontin as a diagnostic/prognostic candidate, but its discovery sample—22 patients and 10 controls—is too small for implementation.

Single-cell RNA/ATAC and spatial methods increasingly resolve monocyte, neutrophil, lymphocyte and organ-parenchymal states hidden by bulk blood measurements. As of 2024, these approaches are primarily mechanistic and stratification tools, not standard diagnostics. Liquid-biopsy cfDNA epigenomics is being prospectively evaluated in 1,000 participants to infer tissue/cell injury and immune exhaustion (NCT06817408) (NCT06817408 chunk 1).

Suggested cell terms include neutrophil CL:0000775, monocyte CL:0000576, macrophage CL:0000235, dendritic cell CL:0000451, T cell CL:0000084, B cell CL:0000236, platelet CL:0000233 and endothelial cell CL:0000115. Relevant compartments are plasma membrane GO:0005886, extracellular region GO:0005576 and mitochondrion GO:0005739.

## 7. Anatomical structures affected

Sepsis is systemic and has no lateralization. Frequent **primary sites** are lung, urinary tract/kidney, abdomen, bloodstream/device, skin/soft tissue and CNS. **Secondary injury** affects lung (UBERON:0002048), kidney (UBERON:0002113), liver (UBERON:0002107), heart (UBERON:0000948), brain (UBERON:0000955), blood (UBERON:0000178), gastrointestinal barrier and skeletal muscle. The key cross-organ tissue is vascular endothelium, including glycocalyx and microcirculation. Relevant subcellular compartments include membrane PRR complexes, cytosolic inflammasomes, nucleus/chromatin, mitochondria, ER and lysosome/autophagy machinery.

## 8. Temporal development

Onset can be neonatal, pediatric, adult or geriatric. The usual pattern is **acute**, sometimes fulminant within hours. A practical trajectory is: localized infection → early systemic response and evolving organ dysfunction → established sepsis → septic shock/multiorgan dysfunction → recovery, death or chronic critical illness. These are trajectories, not formal cancer-like stages.

The crucial intervention window is at suspicion/recognition: obtain cultures without material delay, begin appropriate antimicrobials, control the source and restore perfusion. Progression rate is highly variable. Resolution may occur over days; organ recovery can take weeks to months. Recurrent infection, rehospitalization, weakness and neurocognitive/psychiatric sequelae can persist for years. Treatment-induced remission is better described as infection resolution and organ recovery; “spontaneous remission” is not a useful sepsis construct.

## 9. Inheritance and population epidemiology

Sepsis has multifactorial/polygenic susceptibility with variable, context-dependent expression—not AD, AR, X-linked or mitochondrial inheritance. There is no clinically defined penetrance, anticipation or carrier state.

A widely cited modeled global estimate for 2017 is approximately **48.9 million cases**, incidence **677.5 per 100,000**, and about **11 million deaths**, roughly one in five deaths worldwide. Estimates include sepsis as an intermediate mechanism in many underlying diseases and are definition/model dependent. A prospective Swedish study found community-onset Sepsis-3 incidence of **838/100,000/year**, versus **276/100,000/year** for older severe-sepsis criteria; bacteremia occurred in 13% of suspected cases and had incidence 203/100,000/year (DOI: https://doi.org/10.1371/journal.pone.0225700; published December 2019) (ljungstrom2019incidencesofcommunity pages 12-13).

Burden is highest at the extremes of age and disproportionately affects low- and middle-income regions. Sex effects vary; male excess is often reported in older adults. Geographic variation reflects infectious-disease ecology, vaccination, maternal/neonatal care, antimicrobial resistance, coding, recognition and ICU access.

## 10. Diagnostics

### Clinical criteria and differential diagnosis

Sepsis is a **clinical syndrome**, not confirmed by one assay. Identify suspected infection and acute organ dysfunction using history, examination, trends and SOFA components: respiratory oxygenation, platelets, bilirubin, MAP/vasopressors, Glasgow Coma Scale, creatinine/urine output. qSOFA—altered mentation, respiratory rate ≥22/min and systolic pressure ≤100 mmHg—is prognostic but insufficiently sensitive for screening. The 2021 SSC strongly recommends against qSOFA alone; SIRS, NEWS or MEWS may be used within structured programs. Performance-improvement programs were associated with lower mortality in 50 observational studies (OR 0.66, 95% CI 0.61–0.72), while randomized screening evidence did not itself show mortality benefit (RR 0.90, 95% CI 0.51–1.58) (evans2021survivingsepsiscampaign pages 1-2).

Obtain at least two blood-culture sets and source specimens before antimicrobials when this causes no harmful delay. CBC/differential, CMP, bilirubin, creatinine, coagulation tests, blood gas and serial lactate characterize organ dysfunction. Urinalysis/culture, respiratory testing, CSF, joint fluid or surgical specimens are source-dependent. Ultrasound, radiography, CT, MRI, echocardiography and ECG locate infection or assess organ failure; imaging should not delay stabilization.

Differentials include uncomplicated infection, noninfectious SIRS after trauma/surgery/pancreatitis, hemorrhagic/cardiogenic/obstructive shock, adrenal crisis, anaphylaxis, toxicologic syndromes, pulmonary embolism, cytokine-release/HLH-like states and thrombotic microangiopathy.

### Biomarkers and omics

Lactate is useful for severity and resuscitation trends but is neither specific for sepsis nor a pure tissue-hypoxia marker. CRP and procalcitonin (PCT) support context-dependent probability and stewardship; PCT should not independently rule sepsis in/out. PCT-guided discontinuation can reduce antibiotic exposure, whereas initiation remains clinical (hotchkiss2016sepsisandseptic pages 12-13).

Presepsin, soluble TREM-1, IL-6, endothelial/glycocalyx markers, cell-free DNA, miRNAs and transcriptomic classifiers remain adjunctive/investigational. Monocyte distribution width (MDW) is automatically generated with some CBC analyzers; a 2,200-person prospective study is evaluating a cutoff of 20, but uses Sepsis-2 adjudication, limiting direct Sepsis-3 translation (NCT06267742) (NCT06267742 chunk 1).

There is no asymptomatic population or newborn “sepsis screening” test. Screening is continuous risk surveillance in symptomatic/high-risk patients. Genetic testing is not a routine diagnostic pathway.

## 11. Outcome and prognosis

Short-term prognosis is driven by age/frailty, comorbidities, source and pathogen, antimicrobial adequacy, lactate/shock, number and duration of failed organs and response to treatment. Approximate mortality is 15–25% in sepsis and 30–50% in septic shock (hotchkiss2016sepsisandseptic pages 1-2). In an oncologic ICU cohort, mortality was 37% overall and 68% for Sepsis-3 septic shock; SOFA outperformed qSOFA and SIRS for hospital-death discrimination.

A falling SOFA is favorable. In one derivation/validation analysis, less than a 25% fall by day 7 was associated with markedly increased death risk (OR 14.87), while day-7 ΔSOFA had AUROC 0.84 in the derivation cohort.

Survivors face new disability, cognitive impairment, depression/anxiety/PTSD, recurrent infection, cardiovascular events, kidney disease, muscle wasting and reduced HRQoL. Five- or ten-year “sepsis survival rates” are not stable disease constants because underlying illness and acute severity dominate. Rehabilitation, medication reconciliation and physical/cognitive/emotional follow-up are therefore part of sepsis care, not optional extras (fleischmannstruzek2023returntowork pages 8-8, hodgsonUnknownyeararticletitlehealthrelated pages 73-74).

## 12. Treatment and real-world implementation

### Immediate algorithm

1. Recognize sepsis as a medical emergency; measure lactate, obtain cultures and assess SOFA.
2. Give empiric IV antimicrobials promptly—within 1 hour for septic shock/high-likelihood sepsis—chosen by source, local resistance, prior exposure, allergy, renal/hepatic function and PK/PD. Narrow when microbiology and clinical response permit. Risks include allergy, nephrotoxicity, *C. difficile*, microbiome injury and resistance (hotchkiss2016sepsisandseptic pages 12-13).
3. Achieve source control—drain abscess, debride infected tissue, relieve obstruction or remove infected devices—as soon as practical.
4. For hypoperfusion/shock, use crystalloid with repeated dynamic reassessment. The historical initial 30 mL/kg recommendation is weak, not a mandate; balanced crystalloids are generally favored over 0.9% saline. Avoid persistent positive balance and fluid-accumulation organ injury.
5. Use **norepinephrine** first-line to target MAP near 65 mmHg; starting peripherally through an appropriate proximal vein is preferable to delaying for central access. Add vasopressin, then epinephrine when needed. Individualize MAP upward in selected chronic-hypertension patients.
6. Consider IV hydrocortisone for ongoing vasopressor-dependent shock. It generally accelerates shock reversal; hyperglycemia, hypernatremia and neuromuscular weakness are relevant harms.

The 2021 SSC provides the authoritative adult framework (published October 2021; DOI: https://doi.org/10.1007/s00134-021-06506-y) (evans2021survivingsepsiscampaign pages 1-2). A 2023 expert summary emphasizes the changes: balanced fluid over saline, steroids for persistent vasopressor need, peripheral vasopressor initiation, and downgrade of fixed 30 mL/kg from strong to weak.

### Organ support and supportive care

Use lung-protective ventilation for ARDS, conservative oxygen targets after stabilization, prone positioning for severe ARDS, sedation minimization and spontaneous awakening/breathing protocols. Apply standard indications for RRT rather than prophylactic early dialysis. Use restrictive RBC transfusion thresholds in stable adults, venous-thromboembolism and stress-ulcer prophylaxis when indicated, insulin protocols avoiding hypoglycemia, early enteral nutrition as tolerated, pressure-injury prevention and early mobilization. Surgery is etiologic only when required for source control.

No gene, cell, RNA or broadly targeted immunotherapy is approved specifically for routine sepsis. Activated protein C was withdrawn; routine high-dose steroids, IV vitamin C cocktails, immunoglobulin, polymyxin-B hemoperfusion, cytokine adsorption and checkpoint therapy are not standard outside selected indications/trials.

### Precision and experimental therapy

Current development emphasizes **treatable endotypes**, not one universal immunomodulator. EMBRACE (NCT06694701; Phase 2, 75 participants, active-not-recruiting in the retrieved registry) selects IFNγ/CXCL9-high patients without monocyte-HLA-DR immunoparalysis for emapalumab, exemplifying biomarker-directed immunotherapy (NCT06694701 chunk 2). MODIFY (NCT05909683; Phase 3, 190 participants) evaluates PCT- and molecular-guided antibiotic decisions (NCT05909683 chunk 2). Additional active programs include:

- **NCT06817408**, 1,000-person cfDNA epigenomics/tissue-injury cohort (NCT06817408 chunk 1).
- **NCT06267742**, 2,200-person MDW diagnostic validation (NCT06267742 chunk 1).
- **NCT03929159**, 150-person plasma/PBMC miRNA outcome cohort (NCT03929159 chunk 1).
- **NCT03226158**, 160-child microbial cell-free DNA sequencing cohort for impending bloodstream infection (NCT03226158 chunk 1).

Suggested NCIt annotations include Anti-Infective Therapy, Source-Control Procedure/Drainage, Fluid Therapy, Norepinephrine Therapy, Vasopressor Therapy, Hydrocortisone, Mechanical Ventilation, Renal Replacement Therapy, Physical Therapy and Rehabilitation.

## 13. Prevention

**Primary prevention:** vaccination against influenza, COVID-19, pneumococcus, meningococcus, *Haemophilus influenzae* type b and other age/risk-appropriate infections; clean water/sanitation; maternal/neonatal infection prevention; hand hygiene; sterile procedural technique; catheter/ventilator/surgical-site bundles; wound and chronic-disease care; smoking cessation; nutrition; antimicrobial stewardship.

**Secondary prevention:** public/professional education about infection plus confusion, dyspnea, hypotension, oliguria or mottling; risk-based EHR surveillance; prompt evaluation, cultures, antimicrobials and source control. There is no recommended population biomarker or genetic screening program.

**Tertiary prevention:** minimize iatrogenic complications, de-escalate antimicrobials, prevent thrombosis/pressure injury/delirium, mobilize early, vaccinate before/after discharge as appropriate, and provide post-sepsis physical, cognitive, psychological and social follow-up. SSC added strong recommendations for discharge information, medication reconciliation, shared planning and referral for deficits.

## 14. Other species and natural disease

Naturally occurring sepsis occurs in companion and production animals, including dogs (**NCBI Taxon 9615**), cats (9685), horses (9796), cattle (9913), pigs (9823) and sheep (9940). Common settings include canine peritonitis/pyometra, equine colic and neonatal foal sepsis, bovine mastitis/metritis and neonatal calf sepsis. These are clinically and economically important, but pathogen distributions, hemodynamics and treatment constraints differ by species. Sepsis itself is not generally “transmitted” cross-species; zoonotic pathogens may cross species and then cause sepsis in the infected host.

No sepsis-specific breed ontology association or conserved causal gene is established. Orthologous TLR, cytokine, complement, coagulation and adrenergic pathways are conserved, enabling comparative research, but the retrieved evidence set did not support reliable breed-specific VBO annotations or veterinary incidence estimates.

## 15. Model organisms

**CLP:** surgical polymicrobial peritonitis in mouse/rat; reproduces leukopenia, thrombocytopenia, hypotension, cytokine elevation, organ dysfunction and later immune paralysis. It is widely considered the most comprehensive model but varies with ligation length, needle size, punctures, operator, fluids and antibiotics (kannan2024mousemodelsof pages 1-3, cai2023advancesinrodent pages 4-5).

**Cecal slurry:** standardized donor fecal material injected intraperitoneally; avoids surgery, is scalable and useful in neonatal mice, but varies by donor microbiome and batch (kannan2024mousemodelsof pages 11-12).

**Live-pathogen models:** *E. coli*, *Pseudomonas*, *S. aureus*, *Klebsiella*, pneumococcus, streptococci or *Candida* permit pathogen-specific immunity and antimicrobial testing. Artificial IV/IP routes can bypass the natural infection site; pneumonia models better reproduce local-to-systemic progression. Candida models reproduce kidney injury, shock, thrombocytopenia and PD-1/PD-L1 upregulation (cai2023advancesinrodent pages 2-4).

**LPS/endotoxemia:** rapid, reproducible TLR4 inflammation, but no replicating infection and incomplete biphasic human disease. Specific-pathogen-free mice require approximately 250–500-fold more LPS than humans for comparable responses (kannan2024mousemodelsof pages 11-12).

**Two-hit models** combine trauma/hemorrhage/ischemia with infection and may model clinical complexity, but protocols are poorly standardized. Humanized NSG mice recreate aspects of human immunity but have incomplete reconstitution. “Dirty” mice have adult-human-like immune experience and more severe CLP/LPS responses, improving some realism while reducing standardization (cai2023advancesinrodent pages 6-8, cai2023advancesinrodent pages 8-9).

The central translational limitation is that young, inbred, SPF rodents exposed to a synchronized insult do not reproduce older, comorbid, genetically and microbiologically heterogeneous patients receiving antibiotics, surgery and ICU support. Accordingly, 2023–2024 experts recommend matching the model to the question, using both sexes/ages and supportive care, standardizing severity, and validating across multiple models before clinical translation (DOIs: https://doi.org/10.3390/ijms24119578, published May 2023; https://doi.org/10.1002/cpz1.997, published March 2024) (kannan2024mousemodelsof pages 1-3, cai2023advancesinrodent pages 1-2).

## Ontology and knowledge-base mapping

The following compact mapping distinguishes verified identifiers from suggested terms needing current-release validation.

| Domain | Preferred concept / identifier | Suggested ontology terms / codes | Practical note |
|---|---|---|---|
| Disease | Sepsis | **MeSH:** Sepsis (D018805); **ICD-10-CM:** A41.9, Sepsis, unspecified organism; **ICD-11 candidates:** 1G40, sepsis without septic shock; 1G41, sepsis with septic shock; **MONDO:** general sepsis identifier requires release-level verification | Sepsis is infection-associated, life-threatening organ dysfunction caused by a dysregulated host response; do not equate it with uncomplicated infection, bacteremia, or SIRS (hotchkiss2016sepsisandseptic pages 1-2, evans2021survivingsepsiscampaign pages 1-2). |
| Disease subtype | Bacterial infectious disease with sepsis | **MONDO:** MONDO:0005229 (verified in retrieved Open Targets mapping) | A narrower concept than all-cause sepsis; sepsis may also be viral, fungal, or parasitic (OpenTargets Search: sepsis). |
| Disease subtype | Infectious disease with sepsis | **MONDO:** MONDO:1040015 (verified in retrieved Open Targets mapping) | Broad infection-with-sepsis concept found in Open Targets; confirm intended hierarchy before production use (OpenTargets Search: sepsis). |
| Disease severity | Septic shock | **ICD-10-CM:** R65.21; **ICD-11 candidate:** 1G41; **SNOMED CT:** use current-release “Septic shock” concept | Clinical subset with vasopressor-dependent hypotension and elevated lactate despite adequate volume resuscitation; substantially higher mortality than sepsis without shock (hotchkiss2016sepsisandseptic pages 1-2, vasques2018septicshock3vs pages 7-7). |
| Phenotype | Fever or hypothermia | **HPO:** Fever (HP:0001945); Hypothermia (HP:0002045) | Variable and episodic acute signs; absence of fever does not exclude sepsis. Temperature responses depend on host age, severity, and environment (hotchkiss2016sepsisandseptic pages 1-2, bakoush2023…classification pages 8-10). |
| Phenotype | Tachycardia and hypotension | **HPO:** Tachycardia (HP:0001649); Hypotension (HP:0002615) | Cardiovascular manifestations range from compensated tachycardia to vasoplegia, myocardial depression, and shock (hotchkiss2016sepsisandseptic pages 9-10). |
| Phenotype | Tachypnea, hypoxemia, respiratory failure | **HPO:** Tachypnea (HP:0002789); Hypoxemia (HP:0012418); Respiratory failure (term; verify current HPO identifier) | Alveolar–capillary injury causes noncardiogenic edema, impaired compliance, and reduced gas exchange; respiratory dysfunction commonly contributes to SOFA-defined sepsis (ljungstrom2019incidencesofcommunity pages 12-13, hotchkiss2016sepsisandseptic pages 9-10). |
| Phenotype | Altered consciousness, delirium, encephalopathy | **HPO:** Delirium (HP:0031258); Encephalopathy (HP:0001298); Altered mental status (term; verify current HPO identifier) | May be an early sign or sepsis-associated encephalopathy; exclude CNS infection, structural lesions, drugs, metabolic disease, and primary neurologic causes (hotchkiss2016sepsisandseptic pages 9-10). |
| Phenotype | Oliguria and acute kidney injury | **HPO:** Oliguria (HP:0100520); Acute kidney injury (term; verify current HPO identifier) | Dynamic organ dysfunction assessed using urine output and creatinine; may require renal replacement therapy in severe cases (hotchkiss2016sepsisandseptic pages 9-10, NCT06817408 chunk 1). |
| Phenotype | Thrombocytopenia and coagulopathy | **HPO:** Thrombocytopenia (HP:0001873); Abnormality of coagulation (HP:0001928); Disseminated intravascular coagulation (term; verify current HPO identifier) | Reflects platelet consumption, coagulation activation, endothelial injury, and—in severe disease—DIC (hotchkiss2016sepsisandseptic pages 9-10, bakoush2023…classification pages 8-10). |
| Phenotype | Hyperbilirubinemia and hepatic dysfunction | **HPO:** Hyperbilirubinemia (HP:0002904); Abnormal liver function (term; verify current HPO identifier) | SOFA hepatic dysfunction is bilirubin-based; mechanisms include cholestasis, inflammation, hypoxia, and shock (hotchkiss2016sepsisandseptic pages 9-10). |
| Laboratory phenotype | Hyperlactatemia | **HPO:** Increased circulating lactate concentration (term; verify current HPO identifier); **LOINC:** use specimen/method-specific lactate code | Lactate supports severity assessment and resuscitation monitoring but is neither sepsis-specific nor a pure measure of tissue hypoxia (vasques2018septicshock3vs pages 7-7, oczkowski2022survivingsepsiscampaign pages 7-8). |
| Organ | Lung | **UBERON:** lung (UBERON:0002048) | Frequent infection source and target of secondary injury; manifestations include pneumonia, hypoxemia, and ARDS (ljungstrom2019incidencesofcommunity pages 12-13, hotchkiss2016sepsisandseptic pages 9-10). |
| Organ | Kidney | **UBERON:** kidney (UBERON:0002113) | Sepsis-associated AKI involves microcirculatory, inflammatory, endothelial, and metabolic injury rather than hypoperfusion alone (hotchkiss2016sepsisandseptic pages 9-10). |
| Organ | Liver | **UBERON:** liver (UBERON:0002107) | Hepatic dysfunction may present with cholestasis, hyperbilirubinemia, impaired clearance, or hypoxic hepatitis (hotchkiss2016sepsisandseptic pages 9-10). |
| Organ | Heart | **UBERON:** heart (UBERON:0000948) | Sepsis-induced cardiomyopathy can affect both ventricles; mild troponin elevation is common but nonspecific (hotchkiss2016sepsisandseptic pages 9-10). |
| Organ | Brain | **UBERON:** brain (UBERON:0000955) | Neuroinflammation, blood–brain-barrier dysfunction, microglial activation, and systemic metabolic disturbances contribute to encephalopathy and long-term cognitive deficits (hotchkiss2016sepsisandseptic pages 1-2, hotchkiss2016sepsisandseptic pages 9-10). |
| System/tissue | Blood and vascular endothelium | **UBERON:** blood (UBERON:0000178); vasculature (term; verify site-specific UBERON code) | Endothelial activation converts an anticoagulant surface into a proadhesive, procoagulant interface and promotes capillary leak and immunothrombosis (hotchkiss2016sepsisandseptic pages 9-10). |
| Cell type | Neutrophil | **CL:** neutrophil (CL:0000775) | Performs phagocytosis and NET formation; dysregulated NETs trap pathogens but can damage endothelium and amplify thrombosis and inflammation (vella2025cytokinesinsepsis pages 10-11, bakoush2023…classification pages 8-10). |
| Cell type | Monocyte | **CL:** monocyte (CL:0000576) | Key pathogen-sensing and antigen-presenting cell; reduced monocyte HLA-DR is used experimentally to define sepsis-induced immunoparalysis (hotchkiss2016sepsisandseptic pages 5-6, NCT06694701 chunk 2). |
| Cell type | Macrophage | **CL:** macrophage (CL:0000235) | Produces inflammatory cytokines after PRR activation; later polarization and uptake of apoptotic cells can increase IL-10 and TGF-β and suppress immunity (hotchkiss2016sepsisandseptic pages 5-6, vella2025cytokinesinsepsis pages 10-11). |
| Cell type | Dendritic cell | **CL:** dendritic cell (CL:0000451) | Apoptotic depletion and impaired antigen presentation contribute to immunosuppression (hotchkiss2016sepsisandseptic pages 5-6). |
| Cell type | T lymphocyte | **CL:** T cell (CL:0000084) | Lymphopenia, apoptosis, PD-1 expression, TH2/regulatory skewing, and functional exhaustion are associated with persistent immune dysfunction (hotchkiss2016sepsisandseptic pages 5-6). |
| Cell type | B lymphocyte | **CL:** B cell (CL:0000236) | Sepsis-associated apoptosis reduces adaptive immune-cell numbers and may impair subsequent antimicrobial immunity (hotchkiss2016sepsisandseptic pages 5-6). |
| Cell type | Platelet | **CL:** platelet (CL:0000233) | Platelets link coagulation to innate immunity through fibrin binding, P-selectin-mediated leukocyte recruitment, and microthrombus formation (hotchkiss2016sepsisandseptic pages 9-10). |
| Cell type | Endothelial cell | **CL:** endothelial cell (CL:0000115) | Central effector of permeability, leukocyte adhesion, vasoplegia, coagulation activation, and microvascular organ injury (vella2025cytokinesinsepsis pages 10-11, hotchkiss2016sepsisandseptic pages 9-10). |
| Mechanism | Pattern-recognition receptor signaling | **GO-BP:** innate immune response (GO:0045087); inflammatory response (GO:0006954); Toll-like receptor signaling pathway (GO:0002224) | PAMPs and DAMPs activate TLRs, NOD proteins, dectins, RAGE, and RNA sensors, converging on NF-κB, AP-1, and IRFs (hotchkiss2016sepsisandseptic pages 5-6). |
| Mechanism | Cytokine production and signaling | **GO-BP:** cytokine-mediated signaling pathway (GO:0019221); positive regulation of cytokine production (GO:0001819) | TNF, IL-1, IL-6, chemokines, and interferons drive systemic inflammation, while IL-10 and TGF-β contribute to compensatory immunosuppression (hotchkiss2016sepsisandseptic pages 5-6, bakoush2023…classification pages 8-10). |
| Mechanism | Complement activation | **GO-BP:** complement activation (GO:0006956) | C3a, C4a, and particularly C5a amplify inflammation, alter neutrophil function, and can promote immune-cell apoptosis (vella2025cytokinesinsepsis pages 10-11, hotchkiss2016sepsisandseptic pages 17-18). |
| Mechanism | Coagulation and immunothrombosis | **GO-BP:** blood coagulation (GO:0007596); platelet activation (GO:0030168) | Inflammation, endothelial activation, platelets, fibrin, and leukocytes generate microvascular thrombi; excessive activation may progress to consumptive coagulopathy or DIC (hotchkiss2016sepsisandseptic pages 9-10, bakoush2023…classification pages 8-10). |
| Mechanism | Programmed cell death | **GO-BP:** apoptotic process (GO:0006915); pyroptosis (GO:0070269) | Human autopsy and experimental evidence support lymphocyte and dendritic-cell apoptosis as drivers of immunosuppression; pyroptosis is a plausible inflammatory mechanism but requires evidence-specific annotation (hotchkiss2016sepsisandseptic pages 5-6). |
| Mechanism | Neutrophil extracellular-trap formation | **GO-BP:** neutrophil extracellular trap formation (GO:0140725) | NETs support antimicrobial defense but expose histones and proteases that injure endothelium and amplify cytokine signaling (vella2025cytokinesinsepsis pages 10-11). |
| Mechanism | Mitochondrial/metabolic dysfunction | **GO-BP:** cellular response to oxidative stress (GO:0034599); cellular respiration (GO:0045333); **GO-CC:** mitochondrion (GO:0005739) | Bioenergetic failure, oxidative stress, and metabolic reprogramming may cause organ dysfunction despite restored macrocirculation; many candidate signatures remain investigational (sebastian2025sepsisandpostsepsis pages 8-10, cai2023advancesinrodent pages 8-9). |
| Mechanism | Immune suppression/exhaustion | **GO-BP:** negative regulation of immune response (GO:0050777); regulation of T-cell apoptotic process (suggested term) | PD-1/PD-L1 signaling, reduced MHC-II/HLA-DR, lymphocyte apoptosis, impaired cytokine production, and regulatory-cell expansion can coexist with inflammation (hotchkiss2016sepsisandseptic pages 5-6). |
| Subcellular site | Plasma membrane and extracellular compartment | **GO-CC:** plasma membrane (GO:0005886); extracellular region (GO:0005576) | PRRs, adhesion molecules, complement, cytokines, coagulation proteins, and NET components act across these compartments (hotchkiss2016sepsisandseptic pages 5-6, vella2025cytokinesinsepsis pages 10-11, hotchkiss2016sepsisandseptic pages 9-10). |
| Chemical | Lipopolysaccharide | **ChEBI:** lipopolysaccharide (CHEBI:16412) | Gram-negative PAMP and experimental endotoxemia trigger; LPS models are reproducible but do not reproduce live, heterogeneous human infection (kannan2024mousemodelsof pages 11-12, cai2023advancesinrodent pages 4-5). |
| Chemical/biomarker | Lactate | **ChEBI:** lactate (CHEBI:24996) | Measure specimen-specific blood lactate clinically; elevation has multiple causes, including adrenergic glycolysis, impaired clearance, and hypoperfusion (vasques2018septicshock3vs pages 7-7, oczkowski2022survivingsepsiscampaign pages 7-8). |
| Chemical/intervention | Norepinephrine | **ChEBI:** noradrenaline (CHEBI:18357); **NCIt suggested term:** Norepinephrine | Preferred first-line vasopressor in septic shock; receptor-target associations in Open Targets reflect therapeutic biology rather than causal sepsis genes (OpenTargets Search: sepsis, oczkowski2022survivingsepsiscampaign pages 7-8). |
| Chemical/intervention | Vasopressin | **ChEBI:** vasopressin (verify current ChEBI identifier); **NCIt suggested term:** Vasopressin | Common adjunct to norepinephrine when escalating vasopressor support; not a pathogen-directed therapy (vasques2018septicshock3vs pages 7-7, oczkowski2022survivingsepsiscampaign pages 7-8). |
| Chemical/intervention | Hydrocortisone | **ChEBI:** hydrocortisone (CHEBI:17650); **NCIt suggested term:** Hydrocortisone | Suggested for septic shock with an ongoing vasopressor requirement; annotate as adjunctive corticosteroid therapy, not general sepsis monotherapy (oczkowski2022survivingsepsiscampaign pages 7-8). |
| Intervention | Broad-spectrum antimicrobial therapy | **NCIt suggested terms:** Antibiotic Therapy; Anti-Infective Therapy; Antimicrobial Treatment | Start promptly after appropriate cultures when this does not cause harmful delay; select empirically by source, resistance risk, prior exposure, and local ecology, then de-escalate when possible (hotchkiss2016sepsisandseptic pages 12-13). |
| Intervention | Source control | **NCIt suggested terms:** Surgical Procedure; Drainage Procedure; Device Removal | Drain infected collections, debride necrotic tissue, relieve obstruction, or remove infected devices as soon as medically and logistically practical (hotchkiss2016sepsisandseptic pages 12-13). |
| Intervention | Intravenous crystalloid resuscitation | **NCIt suggested terms:** Fluid Therapy; Intravenous Infusion; Crystalloid Solution | Initial resuscitation is individualized; balanced crystalloids are generally preferred, and repeated reassessment is needed to avoid fluid accumulation and organ edema (oczkowski2022survivingsepsiscampaign pages 7-8). |
| Intervention | Vasopressor therapy | **NCIt suggested terms:** Vasopressor Therapy; Norepinephrine Therapy | Used to restore perfusion pressure when hypotension persists during/after initial fluid resuscitation; peripheral initiation may avoid harmful delay while central access is arranged (oczkowski2022survivingsepsiscampaign pages 7-8). |
| Intervention | Mechanical ventilation / ARDS care | **NCIt suggested terms:** Mechanical Ventilation; Lung Protective Ventilation | Use lung-protective ventilation for sepsis-associated ARDS; ventilatory support treats organ failure but not the infectious trigger (hotchkiss2016sepsisandseptic pages 9-10, oczkowski2022survivingsepsiscampaign pages 7-8). |
| Intervention | Renal replacement therapy | **NCIt suggested term:** Renal Replacement Therapy | Reserved for standard urgent indications or severe persistent AKI; trials evaluate need and timing as outcomes rather than establishing sepsis-specific dialysis criteria (oczkowski2022survivingsepsiscampaign pages 7-8, NCT06817408 chunk 1). |
| Intervention | Post-sepsis rehabilitation and follow-up | **NCIt suggested terms:** Rehabilitation; Physical Therapy; Occupational Therapy; Cognitive Assessment | Assess physical, cognitive, emotional, medication, social, and economic needs after discharge; long-term disability and failure to return to work are common (fleischmannstruzek2023returntowork pages 8-8, hodgsonUnknownyeararticletitlehealthrelated pages 73-74). |


*Table: Compact knowledge-base mappings for sepsis disease concepts, phenotypes, anatomy, cells, mechanisms, chemicals, and interventions. Verified identifiers are distinguished from suggested terms or codes requiring release-level validation.*

## Evidence-quality and expert interpretation

The strongest evidence supports Sepsis-3/SOFA characterization, rapid infection treatment/source control and individualized organ support. Epidemiologic estimates are definition-sensitive. Biomarkers should augment rather than replace bedside judgment. Genetic, epigenetic, single-cell and multi-omics findings are biologically informative but mostly not clinically validated. The most credible precision-medicine direction is prospective enrichment of trials by reproducible immune/endothelial/metabolic endotypes rather than retrospective subgroup claims.

Direct abstract wording supporting the central concept includes: **“sepsis [is] life-threatening organ dysfunction caused by a dysregulated host response to infection”** in the SSC/Sepsis-3 framework (evans2021survivingsepsiscampaign pages 1-2). Recent model experts similarly emphasize that **“human sepsis is a complex disease that manifests with a diverse range of phenotypes and inherent variability,”** explaining why no single model or targeted drug captures the syndrome (kannan2024mousemodelsof pages 1-3).

### Key cited publications and URLs

- Hotchkiss RS et al. *Sepsis and septic shock*. Nature Reviews Disease Primers. Published June 30, 2016. https://doi.org/10.1038/nrdp.2016.45 (hotchkiss2016sepsisandseptic pages 1-2)
- Evans L et al. *Surviving Sepsis Campaign: International Guidelines 2021*. Published October 2021. https://doi.org/10.1007/s00134-021-06506-y (evans2021survivingsepsiscampaign pages 1-2)
- Ljungström L et al. Population incidence study. Published December 2019. https://doi.org/10.1371/journal.pone.0225700 (ljungstrom2019incidencesofcommunity pages 12-13)
- Rosier F et al. CISH-enhancer GWAS/functional study. Published May 2021. https://doi.org/10.3390/ijms22115852 (rosier2021geneticpredispositionto pages 16-18)
- Cai L et al. Rodent-model review. Published May 2023. https://doi.org/10.3390/ijms24119578 (cai2023advancesinrodent pages 4-5)
- Kannan SK et al. Mouse-model protocols. Published March 2024. https://doi.org/10.1002/cpz1.997 (kannan2024mousemodelsof pages 1-3)
- Fleischmann-Struzek C et al. Return-to-work outcomes. Published May 2023. https://doi.org/10.3389/fmed.2023.1187809 (fleischmannstruzek2023returntowork pages 8-8)

PMIDs were included where available in the retrieved records; many full-text excerpts supplied DOI but not PMID. The foundational Sepsis-3 consensus is Singer et al., JAMA 2016, DOI https://doi.org/10.1001/jama.2016.0287; PMID **26903338**.

References

1. (hotchkiss2016sepsisandseptic pages 1-2): Richard S. Hotchkiss, Lyle L. Moldawer, Steven M. Opal, Konrad Reinhart, Isaiah R. Turnbull, and Jean-Louis Vincent. Sepsis and septic shock. Nature Reviews Disease Primers, Jun 2016. URL: https://doi.org/10.1038/nrdp.2016.45, doi:10.1038/nrdp.2016.45. This article has 2186 citations.

2. (hotchkiss2016sepsisandseptic pages 5-6): Richard S. Hotchkiss, Lyle L. Moldawer, Steven M. Opal, Konrad Reinhart, Isaiah R. Turnbull, and Jean-Louis Vincent. Sepsis and septic shock. Nature Reviews Disease Primers, Jun 2016. URL: https://doi.org/10.1038/nrdp.2016.45, doi:10.1038/nrdp.2016.45. This article has 2186 citations.

3. (hotchkiss2016sepsisandseptic pages 9-10): Richard S. Hotchkiss, Lyle L. Moldawer, Steven M. Opal, Konrad Reinhart, Isaiah R. Turnbull, and Jean-Louis Vincent. Sepsis and septic shock. Nature Reviews Disease Primers, Jun 2016. URL: https://doi.org/10.1038/nrdp.2016.45, doi:10.1038/nrdp.2016.45. This article has 2186 citations.

4. (sebastian2025sepsisandpostsepsis pages 8-10): Jhan Sebastian, Saavedra Torres, Francisco Javier Tamayo-Giraldo, Alejandro Bejarano-Zuleta, H. Nati-Castillo, Diego A. Quintero, M. Ospina-Mejía, Camila Salazar-Santoliva, Isaac A. Suárez-Sangucho, E. Ortiz-Prado, J. Izquierdo-Condoy, Georgia Damoraki, Feng Shen, Gaweł Sołowski, Torres Jss, FJ Tamayo-Giraldo, H. Nati-Castillo, DA Quintero, M. Ospina-Mejía, Izquierdo-Condoy, Tamayo-Giraldo Torres, Quintero Nati-Castillo, and Izquierdo-Condoy. This. Sepsis and post-sepsis syndrome: a multisystem challenge requiring comprehensive care and management—a review. Frontiers in Medicine, Apr 2025. URL: https://doi.org/10.3389/fmed.2025.1560737, doi:10.3389/fmed.2025.1560737. This article has 61 citations.

5. (OpenTargets Search: sepsis): Open Targets Query (sepsis, 15 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (ljungstrom2019incidencesofcommunity pages 12-13): Lars Ljungström, Rune Andersson, and Gunnar Jacobsson. Incidences of community onset severe sepsis, sepsis-3 sepsis, and bacteremia in sweden – a prospective population-based study. PLOS ONE, 14(12):e0225700, Dec 2019. URL: https://doi.org/10.1371/journal.pone.0225700, doi:10.1371/journal.pone.0225700. This article has 73 citations and is from a peer-reviewed journal.

7. (hodgsonUnknownyeararticletitlehealthrelated pages 15-16): CL Hodgson. Article title: health-related quality of life of adult sepsis survivors following critical illness: a systematic review journal name: critical care medicine sheraya de …. Unknown journal, Unknown year.

8. (hotchkiss2016sepsisandseptic pages 12-13): Richard S. Hotchkiss, Lyle L. Moldawer, Steven M. Opal, Konrad Reinhart, Isaiah R. Turnbull, and Jean-Louis Vincent. Sepsis and septic shock. Nature Reviews Disease Primers, Jun 2016. URL: https://doi.org/10.1038/nrdp.2016.45, doi:10.1038/nrdp.2016.45. This article has 2186 citations.

9. (giamarellosbourboulis2016theroleof pages 4-5): Evangelos J. Giamarellos-Bourboulis and Steven M. Opal. The role of genetics and antibodies in sepsis. Annals of translational medicine, 4 17:328, Sep 2016. URL: https://doi.org/10.21037/atm.2016.08.63, doi:10.21037/atm.2016.08.63. This article has 48 citations.

10. (sutherland2009benchtobedsidereviewassociation pages 1-2): Ainsley M Sutherland and Keith R Walley. Bench-to-bedside review: association of genetic variation with sepsis. Critical Care, 13:210-210, Apr 2009. URL: https://doi.org/10.1186/cc7702, doi:10.1186/cc7702. This article has 141 citations and is from a highest quality peer-reviewed journal.

11. (fleischmannstruzek2023returntowork pages 8-8): Carolin Fleischmann-Struzek, Bianka Ditscheid, Norman Rose, Melissa Spoden, Lisa Wedekind, Peter Schlattmann, Christian Günster, Konrad Reinhart, Christiane S. Hartog, and Antje Freytag. Return to work after sepsis—a german population-based health claims study. Frontiers in Medicine, May 2023. URL: https://doi.org/10.3389/fmed.2023.1187809, doi:10.3389/fmed.2023.1187809. This article has 16 citations.

12. (rosier2021geneticpredispositionto pages 16-18): Florian Rosier, Audrey Brisebarre, Claire Dupuis, Sabrina Baaklini, Denis Puthier, Christine Brun, Lydie C. Pradel, Pascal Rihet, and Didier Payen. Genetic predisposition to the mortality in septic shock patients: from gwas to the identification of a regulatory variant modulating the activity of a cish enhancer. International Journal of Molecular Sciences, 22(11):5852, May 2021. URL: https://doi.org/10.3390/ijms22115852, doi:10.3390/ijms22115852. This article has 26 citations.

13. (rosier2021geneticpredispositionto pages 1-2): Florian Rosier, Audrey Brisebarre, Claire Dupuis, Sabrina Baaklini, Denis Puthier, Christine Brun, Lydie C. Pradel, Pascal Rihet, and Didier Payen. Genetic predisposition to the mortality in septic shock patients: from gwas to the identification of a regulatory variant modulating the activity of a cish enhancer. International Journal of Molecular Sciences, 22(11):5852, May 2021. URL: https://doi.org/10.3390/ijms22115852, doi:10.3390/ijms22115852. This article has 26 citations.

14. (NCT06817408 chunk 1): Aadel A. Chaudhuri. Dynamics of Organ Damage and Immune Exhaustion During Sepsis. Mayo Clinic. 2025. ClinicalTrials.gov Identifier: NCT06817408

15. (sutherland2009benchtobedsidereviewassociation pages 6-7): Ainsley M Sutherland and Keith R Walley. Bench-to-bedside review: association of genetic variation with sepsis. Critical Care, 13:210-210, Apr 2009. URL: https://doi.org/10.1186/cc7702, doi:10.1186/cc7702. This article has 141 citations and is from a highest quality peer-reviewed journal.

16. (vella2025cytokinesinsepsis pages 10-11): Roberta Vella, Diego Panci, Francesco Carini, Ginevra Malta, Salvatore Vieni, Sabrina David, Giuseppe Davide Albano, Maria Puntarello, Stefania Zerbo, and Antonina Argo. Cytokines in sepsis: a critical review of the literature on systemic inflammation and multiple organ dysfunction. Frontiers in Immunology, Nov 2025. URL: https://doi.org/10.3389/fimmu.2025.1682306, doi:10.3389/fimmu.2025.1682306. This article has 44 citations and is from a peer-reviewed journal.

17. (evans2021survivingsepsiscampaign pages 1-2): Laura Evans, A. Rhodes, W. Alhazzani, M. Antonelli, C. Coopersmith, C. French, F. Machado, L. McIntyre, M. Ostermann, H. Prescott, C. Schorr, S. Simpson, W. Wiersinga, F. Alshamsi, D. Angus, Y. Arabi, Luciano Azevedo, R. Beale, G. Beilman, E. Belley‐Cote, L. Burry, M. Cecconi, J. Centofanti, Angel O Coz Yataco, J. D. De Waele, R. Dellinger, Kent Doi, Bin Du, E. Estenssoro, R. Ferrer, C. Gomersall, C. Hodgson, M. Møller, T. Iwashyna, Shevin T. Jacob, R. Kleinpell, M. Klompas, Y. Koh, Anand Kumar, A. Kwizera, S. Lobo, H. Masur, S. Mcgloughlin, S. Mehta, Y. Mehta, M. Mer, M. Nunnally, S. Oczkowski, T. Osborn, E. Papathanassoglou, A. Perner, M. Puskarich, J. Roberts, W. Schweickert, Maureen A. Seckel, J. Sevransky, C. Sprung, T. Welte, J. Zimmerman, and Mitchell M. Levy. Surviving sepsis campaign: international guidelines for management of sepsis and septic shock 2021. Intensive Care Medicine, 47:1181-1247, Oct 2021. URL: https://doi.org/10.1007/s00134-021-06506-y, doi:10.1007/s00134-021-06506-y. This article has 10381 citations and is from a highest quality peer-reviewed journal.

18. (NCT06267742 chunk 1):  Clinical Trial to Evaluate MDW for Early Detection of Sepsis. Beckman Coulter, Inc.. 2022. ClinicalTrials.gov Identifier: NCT06267742

19. (hodgsonUnknownyeararticletitlehealthrelated pages 73-74): CL Hodgson. Article title: health-related quality of life of adult sepsis survivors following critical illness: a systematic review journal name: critical care medicine sheraya de …. Unknown journal, Unknown year.

20. (NCT06694701 chunk 2):  Emapalumab Treatment For Anticipated Clinical Benefit In Sepsis Driven By The Interferon-Gamma Endotype (The EMBRACE Trial). Hellenic Institute for the Study of Sepsis. 2025. ClinicalTrials.gov Identifier: NCT06694701

21. (NCT05909683 chunk 2):  Assessing the Procalcitonin-guidance and Molecular-guided Diagnosis for Therapy of Severe Infections (the MODIFY Trial). Hellenic Institute for the Study of Sepsis. 2023. ClinicalTrials.gov Identifier: NCT05909683

22. (NCT03929159 chunk 1):  Correlating MicroRNA Changes With Sepsis Outcomes. M.D. Anderson Cancer Center. 2019. ClinicalTrials.gov Identifier: NCT03929159

23. (NCT03226158 chunk 1):  Next Generation Pathogen Sequencing for Prediction of Adverse Events. St. Jude Children's Research Hospital. 2017. ClinicalTrials.gov Identifier: NCT03226158

24. (kannan2024mousemodelsof pages 1-3): Shravan Kumar Kannan, Caleb Y. Kim, Mohammad Heidarian, Roger R. Berton, Isaac J. Jensen, Thomas S. Griffith, and Vladimir P. Badovinac. Mouse models of sepsis. Current Protocols, Mar 2024. URL: https://doi.org/10.1002/cpz1.997, doi:10.1002/cpz1.997. This article has 37 citations and is from a peer-reviewed journal.

25. (cai2023advancesinrodent pages 4-5): Lun Cai, Elizabeth Rodgers, Nick Schoenmann, and Raghavan Pillai Raju. Advances in rodent experimental models of sepsis. International Journal of Molecular Sciences, 24:9578, May 2023. URL: https://doi.org/10.3390/ijms24119578, doi:10.3390/ijms24119578. This article has 76 citations.

26. (kannan2024mousemodelsof pages 11-12): Shravan Kumar Kannan, Caleb Y. Kim, Mohammad Heidarian, Roger R. Berton, Isaac J. Jensen, Thomas S. Griffith, and Vladimir P. Badovinac. Mouse models of sepsis. Current Protocols, Mar 2024. URL: https://doi.org/10.1002/cpz1.997, doi:10.1002/cpz1.997. This article has 37 citations and is from a peer-reviewed journal.

27. (cai2023advancesinrodent pages 2-4): Lun Cai, Elizabeth Rodgers, Nick Schoenmann, and Raghavan Pillai Raju. Advances in rodent experimental models of sepsis. International Journal of Molecular Sciences, 24:9578, May 2023. URL: https://doi.org/10.3390/ijms24119578, doi:10.3390/ijms24119578. This article has 76 citations.

28. (cai2023advancesinrodent pages 6-8): Lun Cai, Elizabeth Rodgers, Nick Schoenmann, and Raghavan Pillai Raju. Advances in rodent experimental models of sepsis. International Journal of Molecular Sciences, 24:9578, May 2023. URL: https://doi.org/10.3390/ijms24119578, doi:10.3390/ijms24119578. This article has 76 citations.

29. (cai2023advancesinrodent pages 8-9): Lun Cai, Elizabeth Rodgers, Nick Schoenmann, and Raghavan Pillai Raju. Advances in rodent experimental models of sepsis. International Journal of Molecular Sciences, 24:9578, May 2023. URL: https://doi.org/10.3390/ijms24119578, doi:10.3390/ijms24119578. This article has 76 citations.

30. (cai2023advancesinrodent pages 1-2): Lun Cai, Elizabeth Rodgers, Nick Schoenmann, and Raghavan Pillai Raju. Advances in rodent experimental models of sepsis. International Journal of Molecular Sciences, 24:9578, May 2023. URL: https://doi.org/10.3390/ijms24119578, doi:10.3390/ijms24119578. This article has 76 citations.

31. (vasques2018septicshock3vs pages 7-7): Francesco Vasques, Eleonora Duscio, Federica Romitti, Iacopo Pasticci, Pietro Caironi, Jennifer Meessen, Roberto Latini, Massimo Cressoni, Luigi Camporota, Antonio Pesenti, Roberto Fumagalli, Michael Quintel, and Luciano Gattinoni. Septic shock-3 vs 2: an analysis of the albios study. Critical Care, Sep 2018. URL: https://doi.org/10.1186/s13054-018-2169-8, doi:10.1186/s13054-018-2169-8. This article has 30 citations and is from a highest quality peer-reviewed journal.

32. (bakoush2023…classification pages 8-10): FB Al Bakoush, AE Azab, and R Yahya. … , classification, risk factors, causative organisms, pathophysiology, prognosis, clinical manifestations, complications, systemic examination, and treatment. Unknown journal, 2023.

33. (oczkowski2022survivingsepsiscampaign pages 7-8): Simon Oczkowski, Fayez Alshamsi, Emilie Belley-Cote, John E. Centofanti, Morten Hylander Møller, Mark E. Nunnaly, and Waleed Alhazzani. Surviving sepsis campaign guidelines 2021: highlights for the practicing clinician. Polish archives of internal medicine, Jul 2022. URL: https://doi.org/10.20452/pamw.16290, doi:10.20452/pamw.16290. This article has 148 citations.

34. (hotchkiss2016sepsisandseptic pages 17-18): Richard S. Hotchkiss, Lyle L. Moldawer, Steven M. Opal, Konrad Reinhart, Isaiah R. Turnbull, and Jean-Louis Vincent. Sepsis and septic shock. Nature Reviews Disease Primers, Jun 2016. URL: https://doi.org/10.1038/nrdp.2016.45, doi:10.1038/nrdp.2016.45. This article has 2186 citations.

## Artifacts

- [Edison artifact artifact-00](Sepsis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
