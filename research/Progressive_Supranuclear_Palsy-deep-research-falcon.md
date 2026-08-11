---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-05T14:50:28.342430'
end_time: '2026-06-05T15:13:56.294493'
duration_seconds: 1407.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Progressive Supranuclear Palsy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 73
artifact_count: 6
artifact_sources:
  edison_answer_artifacts: 6
artifacts:
- filename: artifact-00.md
  path: Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: artifact-03.md
  path: Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-03.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-03
- filename: artifact-04.md
  path: Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-04.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-04
- filename: artifact-05.md
  path: Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-05.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-05
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Supranuclear Palsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive Supranuclear Palsy** covering all of the
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
- **Disease Name:** Progressive Supranuclear Palsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive Supranuclear Palsy** covering all of the
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


## Comprehensive Research Report: Progressive Supranuclear Palsy (PSP)

### Scope and evidence basis
This report synthesizes clinical classification criteria, multi-omics and biomarker studies (prioritizing 2023–2024), and interventional/real-world evidence to populate a disease knowledge base entry for progressive supranuclear palsy. Evidence includes consensus diagnostic criteria, cohort studies using medical records and registries, large-scale whole-genome sequencing, transcriptomics/epigenomics/single-cell studies, and randomized trials. Citations are provided as context IDs. Where requested identifiers (e.g., OMIM, ICD-10, MeSH) were not present in the retrieved sources, this is explicitly stated.

---

## 1. Disease Information

### 1.1 Definition and overview
Progressive supranuclear palsy (PSP) is a neuropathologically defined, adult-onset, rapidly progressive neurodegenerative disorder in which abnormal tau aggregates (predominantly 4-repeat/4R tau) accumulate in neurons and glia, producing characteristic motor (postural instability, falls, akinesia), ocular motor, and cognitive/behavioral syndromes. Definite diagnosis remains neuropathologic, but research/clinical criteria have been revised to improve ante-mortem sensitivity for variant phenotypes. (hoglinger2017clinicaldiagnosisof pages 2-3, wise2024csfproteomicsin pages 1-2, whitney2024singlecelltranscriptomicand pages 1-2)

A widely recognized “classical” clinical phenotype is PSP–Richardson syndrome (PSP-RS), often featuring oculomotor dysfunction and early postural instability, with median survival reported as ~6.9 years in a contemporary biomarker cohort study. (wise2024csfproteomicsin pages 1-2)

### 1.2 Key identifiers and synonyms
A MONDO disease identifier is available via OpenTargets: **MONDO:0019037 (progressive supranuclear palsy)**. (OpenTargets Search: Progressive supranuclear palsy)

ICD coding in retrieved sources: **ICD-9 333.0** was used for case ascertainment in an Israeli health-provider cohort; authors noted nonspecificity requiring verification for externally coded diagnoses. ICD-10, MeSH, and OMIM numeric identifiers were not explicitly provided in the retrieved texts. (barer2023progressivesupranuclearpalsy’s pages 1-2)

Common synonyms/clinical labels include PSP-RS, PSP-P (parkinsonism), PSP-PGF (progressive gait freezing), PSP-SL (speech/language), PSP-F (frontal/behavioral), PSP-CBS, PSP-OM, PSP-PI, and others per MDS framework. (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2)

| Category | Term / Identifier | Code / Expansion | Notes | Source | URL / Year |
|---|---|---|---|---|---|
| Disease | Progressive supranuclear palsy | PSP | Primary disease name; sporadic 4R-tauopathy / neuropathologically defined disease entity (hoglinger2017clinicaldiagnosisof pages 2-3, whitney2024singlecelltranscriptomicand pages 1-2) | MDS criteria; Acta Neuropathol paper | https://doi.org/10.1002/mds.26987 (2017); https://doi.org/10.1007/s00401-024-02823-w (2024) |
| Ontology | MONDO | MONDO:0019037 | OpenTargets disease identifier for progressive supranuclear palsy (OpenTargets Search: Progressive supranuclear palsy) | OpenTargets | https://platform.opentargets.org/ (accessed via OpenTargets context; current) |
| Coding | ICD-9 | 333.0 | Used in Israeli cohort ascertainment; noted as nonspecific and externally verified in chart review (barer2023progressivesupranuclearpalsy’s pages 1-2) | Barer et al. | https://doi.org/10.1007/s00415-023-11714-1 (2023) |
| Coding | ICD-10 | Not explicitly reported in cited PSP papers retrieved here | No directly citable ICD-10 code was provided in the available contexts (barer2023progressivesupranuclearpalsy’s pages 1-2) | Available cited cohort literature | https://doi.org/10.1007/s00415-023-11714-1 (2023) |
| Historical / classic phenotype | Richardson syndrome | PSP-RS | Classical / most recognized phenotype; early falls and vertical gaze dysfunction emphasized across reviews and criteria (boxer2017advancesinprogressive pages 3-4, wise2024csfproteomicsin pages 1-2) | Boxer et al.; Wise et al. | https://doi.org/10.1016/S1474-4422(17)30157-6 (2017); https://doi.org/10.1212/WNL.0000000000209585 (2024) |
| Phenotype label | PSP-parkinsonism | PSP-P | Variant phenotype with parkinsonian presentation; listed in MDS-era phenotype frameworks (boxer2017advancesinprogressive pages 3-4, nasri2024phenotypicspectrumof pages 1-2) | Boxer et al.; Nasri et al. | https://doi.org/10.1016/S1474-4422(17)30157-6 (2017); https://doi.org/10.14802/jmd.23178 (2024) |
| Phenotype label | PSP with progressive gait freezing | PSP-PGF | Variant phenotype dominated by gait freezing / pure akinesia with gait freezing (boxer2017advancesinprogressive pages 3-4, nasri2024phenotypicspectrumof pages 1-2) | Boxer et al.; Nasri et al. | https://doi.org/10.1016/S1474-4422(17)30157-6 (2017); https://doi.org/10.14802/jmd.23178 (2024) |
| Phenotype label | PSP with speech/language disorder | PSP-SL | Variant overlapping with nonfluent/agrammatic PPA or apraxia of speech (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2) | MDS criteria paper; Nasri et al. | https://doi.org/10.1002/mds.26987 (2017); https://doi.org/10.14802/jmd.23178 (2024) |
| Phenotype label | PSP with frontal presentation | PSP-F | Frontal / behavioral-dysexecutive variant (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2) | MDS criteria paper; Nasri et al. | https://doi.org/10.1002/mds.26987 (2017); https://doi.org/10.14802/jmd.23178 (2024) |
| Phenotype label | PSP with corticobasal syndrome | PSP-CBS | Corticobasal syndrome presentation attributed to PSP pathology in some cases (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2) | MDS criteria paper; Nasri et al. | https://doi.org/10.1002/mds.26987 (2017); https://doi.org/10.14802/jmd.23178 (2024) |
| Phenotype label | PSP with ocular motor dysfunction | PSP-OM | Ocular motor–predominant presentation recognized in MDS spectrum (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2) | MDS criteria paper; Nasri et al. | https://doi.org/10.1002/mds.26987 (2017); https://doi.org/10.14802/jmd.23178 (2024) |
| Phenotype label | PSP with predominant postural instability | PSP-PI | Postural instability–predominant presentation recognized in MDS spectrum (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2) | MDS criteria paper; Nasri et al. | https://doi.org/10.1002/mds.26987 (2017); https://doi.org/10.14802/jmd.23178 (2024) |
| Related ontology labels | Classical progressive supranuclear palsy | Orphanet_240071 | Listed in OpenTargets association context as disease subtype label (OpenTargets Search: Progressive supranuclear palsy) | OpenTargets / Orphanet label | https://platform.opentargets.org/ (current) |
| Related ontology labels | Atypical progressive supranuclear palsy | Orphanet_99750 | Listed in OpenTargets association context as disease subtype label (OpenTargets Search: Progressive supranuclear palsy) | OpenTargets / Orphanet label | https://platform.opentargets.org/ (current) |
| Related ontology labels | Progressive supranuclear palsy-parkinsonism syndrome | MONDO:0009839 | Variant/parkinsonism-related disease label surfaced in OpenTargets context (OpenTargets Search: Progressive supranuclear palsy) | OpenTargets | https://platform.opentargets.org/ (current) |
| Inherited disease label | Supranuclear palsy, progressive, 1 | MONDO:0010997 | Separate inherited / gene-linked label associated with MAPT in OpenTargets context (OpenTargets Search: Progressive supranuclear palsy) | OpenTargets | https://platform.opentargets.org/ (current) |


*Table: This table compiles key standardized identifiers and commonly used clinical synonyms/phenotype labels for progressive supranuclear palsy. It is useful for mapping disease terminology across ontologies, coding systems, and clinical subtype literature.*

### 1.3 Evidence source type (patient-level vs aggregated)
PSP characterization is derived from both aggregated resources (e.g., OpenTargets ontology mapping) and aggregated cohort/trial/omics literature. Real-world evidence in this report includes retrospective medical-record abstraction across multiple care centers in the US/Canada and a large Israeli payer-provider database cohort. (nysetvold2024progressivesupranuclearpalsy pages 1-2, barer2023progressivesupranuclearpalsy’s pages 1-2)

---

## 2. Etiology

### 2.1 Primary causal factors
PSP is typically **sporadic**, with pathogenesis centered on **tau (MAPT) biology**, especially 4R tau accumulation and aggregation in vulnerable brain regions and cell types. (hoglinger2017clinicaldiagnosisof pages 2-3, whitney2024singlecelltranscriptomicand pages 1-2)

Rare familial PSP-like syndromes can occur with **MAPT mutations**, but most cases lack Mendelian inheritance; in MDS criteria, MAPT mutations are not an exclusion criterion but define inherited vs sporadic PSP. (hoglinger2017clinicaldiagnosisof pages 3-4)

### 2.2 Genetic risk factors (2023–2024 emphasis)
A 2024 whole-genome sequencing (WGS) case-control study (European ancestry) emphasized that prior array-GWAS were limited for rare variants and structural variants (SVs), and used WGS to analyze SNVs/indels/SVs at scale. (wang2024wholegenomesequencinganalysis pages 1-2)

Key genetic findings include:
- **MAPT 17q21.31 H1 haplotype** is the strongest known common risk factor; the WGS study reports an **estimated OR = 5.6** for H1 carriers. (wang2024wholegenomesequencinganalysis pages 1-2)
- WGS confirmed known loci (e.g., **MAPT, MOBP, STX6, SLCO1A2, DUSP10, SP1**) and identified novel common signals (**APOE, FCHO1/MAP1S, KIF13A, TRIM24, TNXB, ELOVL1**). (wang2024wholegenomesequencinganalysis pages 1-2)
- Notably, **APOE ε2** was observed as the **risk allele** in PSP (in contrast to Alzheimer’s disease). (wang2024wholegenomesequencinganalysis pages 1-2)
- Rare-variant association implicated **ZNF592**, and SV associations included seven common SVs in 17q21.31 and other loci (IGH, PCMT1, CYP2A13, SMCP), plus a burden of rare deletions/duplications in 17q21.31 (**P = 6.73 × 10^-3**). (wang2024wholegenomesequencinganalysis pages 1-2)

Mechanistically, MAPT haplotype effects are supported by transcriptomic evidence: a 2024 post-mortem bulk RNA-seq study found increased total tau mRNA and increased proportion of 4R transcripts in PSP brain regions, with 4R tau mRNA levels associated with the H1 haplotype, consistent with a causal role for altered splicing/expression. (ressler2024mapthaplotypeassociatedtranscriptomic pages 1-2)

| Factor / locus | Risk role in PSP | Key quantitative finding | Study design / cohort | Sample size | Year | DOI / URL | Citation |
|---|---|---|---|---:|---:|---|---|
| MAPT 17q21.31 H1/H2 haplotype region | Strongest common genetic risk locus | H1 haplotype associated with PSP risk; estimated OR = 5.6 | Whole-genome sequencing (WGS) case-control study in European ancestry PSP | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| MAPT H1 haplotype | Candidate mechanistic driver via altered tau isoform expression | 4R tau mRNA significantly associated with H1 haplotype in temporal cortex; total tau and 4R tau transcripts increased in PSP cerebellum | Bulk RNA-seq of post-mortem brain tissue with haplotype-dependent expression/splicing analyses | 84 PSP; 77 controls | 2024 | https://doi.org/10.1186/s40478-024-01839-3 | (ressler2024mapthaplotypeassociatedtranscriptomic pages 1-2) |
| MAPT | Confirmed common susceptibility locus | Reconfirmed among common SNV/indel loci in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| MOBP | Confirmed common susceptibility locus; implicates oligodendrocytes/myelin biology | Confirmed in WGS; prior association reproduced | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| STX6 | Confirmed common susceptibility locus | Confirmed in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| SLCO1A2 | Confirmed common susceptibility locus | Confirmed in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| DUSP10 | Confirmed common susceptibility locus | Confirmed in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| SP1 | Confirmed common susceptibility locus | Confirmed in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| APOE locus | Novel common susceptibility signal | Novel signal identified in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| APOE ε2 allele | Risk allele in PSP | In contrast to Alzheimer disease, APOE ε2 observed as the risk allele in PSP | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| APOE ε4 allele | Potential modifier of phenotype, not core GWAS risk in cited cohort | Earlier parkinsonism onset (p = 0.038), earlier oculomotor dysfunction trend (p = 0.052), more altered cognitive profile | Cross-sectional clinical phenotype study with APOE genotyping | 112 PSP | 2024 | https://doi.org/10.14802/jmd.23178 | (nasri2024phenotypicspectrumof pages 1-2) |
| FCHO1/MAP1S | Novel common susceptibility signal | Newly uncovered in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| KIF13A | Novel common susceptibility signal | Newly uncovered in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| TRIM24 | Novel common susceptibility signal | Newly uncovered in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| TNXB | Novel common susceptibility signal | Newly uncovered in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| ELOVL1 | Novel common susceptibility signal | Newly uncovered in WGS | WGS case-control | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| ZNF592 | Rare-variant association | Significant association in rare SNV/indel analysis | WGS rare-variant analysis | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| Structural variants in 17q21.31 | Structural genetic risk architecture at major PSP locus | Seven common SVs associated with PSP in H1/H2 region and other loci | WGS SV association analysis | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| IGH | SV-associated locus | Common SV association reported | WGS SV analysis | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| PCMT1 | SV-associated locus | Common SV association reported | WGS SV analysis | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| CYP2A13 | SV-associated locus | Common SV association reported | WGS SV analysis | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| SMCP | SV-associated locus | Common SV association reported | WGS SV analysis | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| Rare deletions/duplications in H1/H2 region | Additional structural burden at major locus | Burden of rare deletions/duplications in 17q21.31: P = 6.73 × 10^-3 | WGS SV burden analysis | 1,718 cases; 2,944 controls | 2024 | https://doi.org/10.1186/s13024-024-00747-3 | (wang2024wholegenomesequencinganalysis pages 1-2) |
| EIF2AK3, LRRK2, RUNX2 | Previously reported PSP risk loci referenced in recent mechanistic/genetic studies | Not primary new WGS findings in cited paper, but repeatedly cited as established PSP-associated loci | Background from recent single-cell / review literature | Not applicable | 2024 | https://doi.org/10.1007/s00401-024-02823-w ; https://doi.org/10.1007/s40120-024-00614-9 | (whitney2024singlecelltranscriptomicand pages 1-2, dunning2024pharmacotherapiesforthe pages 3-4) |


*Table: This table summarizes the main genetic risk factors and loci implicated in progressive supranuclear palsy, emphasizing the 2024 WGS study and related transcriptomic evidence. It is useful for quickly mapping confirmed loci, novel signals, structural variation findings, and effect estimates such as the MAPT H1 haplotype odds ratio.*

### 2.3 Environmental risk/protective factors and gene–environment interactions
No high-quality, PSP-specific environmental risk factors, protective factors, or gene–environment interactions were identified within the retrieved evidence set for this run. This should be treated as **insufficient evidence in the current retrieval**, not as evidence of absence.

---

## 3. Phenotypes

### 3.1 Core clinical domains and spectrum
The 2017 MDS-PSP criteria identify **four functional domains** as clinical predictors: **ocular motor dysfunction, postural instability, akinesia, and cognitive dysfunction**, with features contributing different diagnostic certainty levels (probable, possible, suggestive). (hoglinger2017clinicaldiagnosisof pages 2-3)

Variant clinical presentations beyond PSP-RS are common in autopsy series, motivating the criteria revision. (hoglinger2017clinicaldiagnosisof pages 2-3)

### 3.2 Phenotype frequencies and timelines (recent cohort evidence)
- In a 2024 Tunisian cohort recategorized by MDS-PSP phenotypes (n=112), the distribution included PSP-RS (48), PSP-cortical (34; e.g., PSP-CBS 17.6%, PSP-F 9.4%, PSP-SL 8.2%), and PSP-subcortical (30; PSP-P 11.6%, PSP-PI 8.0%, PSP-OM 2.7%, PSP-PGF 1.8%, PSP-C 1.8%, PSP-PLS 0.9%). (nasri2024phenotypicspectrumof pages 1-2)
- In a 2024 US/Canada medical-record real-world study (n=72), **falls** were documented in **79.2%** before diagnosis and **97.2%** during the course; among those with onset dates documented, median onset was **2.0 years before diagnosis** for first fall, **1.2 years** for unsteady gait/gait impairment, and **0.8 years** for mobility problems. (nysetvold2024progressivesupranuclearpalsy pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 2-4)

### 3.3 HPO term suggestions
A practical mapping of major PSP symptoms to HPO labels is provided below.

| Clinical feature | Suggested HPO term | Phenotype group(s) | Frequency / statistic from cohorts | Evidence |
|---|---|---|---|---|
| Vertical supranuclear gaze palsy / slow vertical saccades | **Vertical supranuclear gaze palsy** (HPO label); **Slow saccadic eye movements** (HPO label) | PSP-RS, PSP-OM | Vertical supranuclear gaze palsy is the classic defining sign of PSP; MDS criteria note ocular motor dysfunction as 1 of 4 core domains. In the Tunisian phenotype cohort, PSP-OM represented **2.7%** of all PSP cases; PSP-RS remained the most common phenotype group (48/112). (hoglinger2017clinicaldiagnosisof pages 2-3, nasri2024phenotypicspectrumof pages 1-2) | (hoglinger2017clinicaldiagnosisof pages 2-3, nasri2024phenotypicspectrumof pages 1-2) |
| Postural instability | **Postural instability** (HPO label) | PSP-RS, PSP-PI | MDS criteria identify postural instability as a core diagnostic domain. In the Tunisian cohort, PSP-PI accounted for **8.0%** of cases; in real-world records, **68.1%** had unsteady gait/gait impairment documented before diagnosis, with median onset **1.2 years before diagnosis**. (hoglinger2017clinicaldiagnosisof pages 2-3, nasri2024phenotypicspectrumof pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 2-4) | (hoglinger2017clinicaldiagnosisof pages 2-3, nasri2024phenotypicspectrumof pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 2-4) |
| Recurrent falls | **Frequent falls** (HPO label); **Recurrent falls** (HPO label) | PSP-RS, PSP-PI | In the US/Canada real-world cohort, falling was documented in **79.2%** before diagnosis and **97.2%** across the disease course; median time to first fall was **2.0 years before diagnosis**. Falls are central to Richardson syndrome and MDS/NINDS-SPSP-style criteria. (nysetvold2024progressivesupranuclearpalsy pages 2-4, nysetvold2024progressivesupranuclearpalsy pages 1-2, hoglinger2017clinicaldiagnosisof pages 2-3) | (nysetvold2024progressivesupranuclearpalsy pages 2-4, nysetvold2024progressivesupranuclearpalsy pages 1-2, hoglinger2017clinicaldiagnosisof pages 2-3) |
| Gait freezing / progressive gait freezing | **Freezing of gait** (HPO label) | PSP-PGF | PSP-PGF is an established variant in the MDS spectrum. In the Tunisian cohort, PSP-PGF represented **1.8%** of all PSP cases. Real-world records showed mobility problems in **51.4%** before diagnosis, with median onset **0.8 years before diagnosis**. (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 1-2) | (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 1-2) |
| Akinesia / bradykinesia / rigidity | **Bradykinesia** (HPO label); **Akinetic-rigid parkinsonism** (HPO label); **Rigidity** (HPO label) | PSP-RS, PSP-P | PSP-RS patients in the Tunisian cohort had more **akinetic-rigid and levodopa-resistant parkinsonism** (**p = 0.006**), while PSP-P made up **11.6%** of cases. PSP pathology/clinical descriptions consistently include akinesia and rigidity as key motor manifestations. (nasri2024phenotypicspectrumof pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 1-2, dam2021safetyandefficacy pages 1-6) | (nasri2024phenotypicspectrumof pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 1-2, dam2021safetyandefficacy pages 1-6) |
| Dysphagia | **Dysphagia** (HPO label) | PSP-RS, advanced PSP across phenotypes | Dysphagia is highlighted as an additional symptom emerging with progression in PSP-RS and contributes materially to disease burden and supportive-care needs. No cohort percentage was provided in the retrieved contexts, but it is repeatedly cited as a common progressive feature. (dam2021safetyandefficacy pages 1-6, barer2023progressivesupranuclearpalsy’s pages 1-2) | (dam2021safetyandefficacy pages 1-6, barer2023progressivesupranuclearpalsy’s pages 1-2) |
| Dysarthria | **Dysarthria** (HPO label) | PSP-RS, PSP-SL | Dysarthria is a common speech/bulbar manifestation of PSP and contributes to healthcare utilization and speech-therapy needs. No specific frequency was given in the retrieved cohort excerpts. (barer2023progressivesupranuclearpalsy’s pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 1-2) | (barer2023progressivesupranuclearpalsy’s pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 1-2) |
| Cognitive decline / dementia | **Cognitive impairment** (HPO label); **Dementia** (HPO label) | PSP-RS, PSP-F, PSP-SL, cortical PSP | Cognitive dysfunction is one of the 4 MDS core domains. In longitudinal follow-up, annual decline was faster in Richardson syndrome than variants on **MMSE: -1.8 vs -0.9/year** and **ACE-R: -5.3 vs -3.0/year**. PSP-cortical phenotypes showed greater cognitive alteration than PSP-subcortical phenotypes. (hoglinger2017clinicaldiagnosisof pages 2-3, street2021clinicalprogressionof pages 1-2, nasri2024phenotypicspectrumof pages 1-2) | (hoglinger2017clinicaldiagnosisof pages 2-3, street2021clinicalprogressionof pages 1-2, nasri2024phenotypicspectrumof pages 1-2) |
| Frontal behavioral changes / dysexecutive syndrome | **Behavioral abnormality** (HPO label); **Executive dysfunction** (HPO label); **Frontal lobe syndrome** (HPO label) | PSP-F | PSP with frontal presentation is a recognized MDS phenotype. In the Tunisian cohort, PSP-F accounted for **9.4%** of all cases; APOE ε4 carriers had more altered cognitive profiles. (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2) | (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2) |
| Speech/language impairment: nonfluent aphasia / apraxia of speech | **Nonfluent aphasia** (HPO label); **Apraxia of speech** (HPO label); **Speech impairment** (HPO label) | PSP-SL | PSP-SL is an established MDS phenotype overlapping with nonfluent/agrammatic PPA and apraxia of speech. In the Tunisian cohort, PSP-SL represented **8.2%** of all cases. (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2) | (hoglinger2017clinicaldiagnosisof pages 3-4, nasri2024phenotypicspectrumof pages 1-2) |
| Depression | **Depression** (HPO label) | Non-motor across phenotypes | In the FMT PSP-RS trial, depression improved significantly after treatment as a secondary outcome. In the US/Canada medical-record cohort, depression was a common comorbidity; the paper’s snippet cites **44.4%** comorbidity prevalence. (tian2023efficacyoffaecal pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 1-2) | (tian2023efficacyoffaecal pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 1-2) |
| Anxiety | **Anxiety** (HPO label) | Non-motor across phenotypes | Anxiety improved significantly in the FMT PSP-RS trial after 3-cycle intervention and remained improved for many participants at follow-up. No baseline prevalence percentage was provided in the retrieved snippets. (tian2023efficacyoffaecal pages 1-2) | (tian2023efficacyoffaecal pages 1-2) |
| Constipation | **Constipation** (HPO label) | Non-motor across phenotypes | GI dysfunction is frequent in PSP-RS; the FMT trial notes that **more than 80%** of PSP patients experience GI symptoms and reported significant improvement in constipation after FMT. (tian2023efficacyoffaecal pages 1-2) | (tian2023efficacyoffaecal pages 1-2) |
| Ocular motor dysfunction (broader category) | **Abnormality of eye movement** (HPO label) | PSP-RS, PSP-OM | Ocular motor dysfunction is one of the four MDS core functional domains and is especially relevant in PSP-RS and PSP-OM. In the Tunisian cohort, PSP-OM was **2.7%** of cases; APOE ε4 carriers had earlier oculomotor dysfunction (**p = 0.052**). (hoglinger2017clinicaldiagnosisof pages 2-3, nasri2024phenotypicspectrumof pages 1-2) | (hoglinger2017clinicaldiagnosisof pages 2-3, nasri2024phenotypicspectrumof pages 1-2) |


*Table: This table maps common progressive supranuclear palsy phenotypes and core symptoms to suggested HPO terms, while adding quantitative cohort data where available. It is useful for phenotype annotation in a disease knowledge base and for harmonizing clinical features across PSP subtypes.*

### 3.4 Quality of life impact
Direct QoL instrument data (e.g., EQ-5D, SF-36) were not extracted from the retrieved primary evidence in this run; however, real-world evidence indicates extensive supportive-care and assistive-device needs (see Treatments/Applications section), which reflect substantial functional impairment burden. (nysetvold2024progressivesupranuclearpalsy pages 1-2)

---

## 4. Genetic/Molecular Information

### 4.1 Major genes and loci
Key genes/loci supported by contemporary WGS and/or prior GWAS replication include **MAPT, MOBP, STX6, SLCO1A2, DUSP10, SP1**, with novel signals including **APOE** and others. (wang2024wholegenomesequencinganalysis pages 1-2)

### 4.2 Pathogenic variants (rare familial PSP and related syndromes)
The retrieved MDS criteria explicitly note that **MAPT rare variants (mutations)** are not an exclusion criterion but indicate inherited PSP; MDS criteria also note that MAPT H2 homozygosity is not an exclusion but makes PSP less likely. (hoglinger2017clinicaldiagnosisof pages 3-4)

A complete ClinVar/gnomAD-level catalog (variant nomenclature and allele frequencies) was not obtained in this run.

### 4.3 Epigenetic information
An epigenome-wide DNA methylation comparison in frontal lobe white matter across parkinsonian disorders identified shared and disease-relevant pathway dysregulation including Wnt signaling, ER stress, mitochondrial processes, RNA interference, and endosomal transport. (murthy2024dnamethylationpatterns pages 1-2)

---

## 5. Environmental Information

No PSP-specific infectious/toxic/lifestyle drivers were identified within the retrieved sources for this run. Gastrointestinal dysfunction is frequent in PSP and is being therapeutically targeted (FMT trial), but this does not establish a causal environmental etiology. (tian2023efficacyoffaecal pages 1-2)

---

## 6. Mechanism / Pathophysiology (Current Understanding, 2023–2024 emphasis)

### 6.1 Causal chain (high-level)
Genetic predisposition (notably MAPT H1 haplotype and additional risk loci including stress-pathway genes such as EIF2AK3/PERK) appears to bias tau expression/splicing toward 4R isoforms. This supports a cellular environment prone to tau misfolding/aggregation and spread. Subsequent downstream cascades include ER stress/integrated stress response activation, synaptic/axon guidance and trafficking pathway dysregulation, and neuroinflammatory activation, culminating in region- and cell-type-specific degeneration and clinical syndromes. (wang2024wholegenomesequencinganalysis pages 1-2, ressler2024mapthaplotypeassociatedtranscriptomic pages 1-2, whitney2024singlecelltranscriptomicand pages 1-2, wise2024csfproteomicsin pages 1-2)

### 6.2 Cell types, pathways, and regions (ontology-ready)
A structured mechanism table with CL/GO/UBERON suggestions is provided.

| Mechanism summary | Upstream trigger / risk | Key evidence / quantitative result | Primary cell types (CL suggestion) | Affected anatomical regions (UBERON suggestion) | GO biological process term suggestions | Evidence source DOI / year |
|---|---|---|---|---|---|---|
| 4R tau accumulation and aggregation in neurons and glia drives PSP neurodegeneration through hyperphosphorylated tau inclusions, impaired proteostasis, and cell-to-cell seeding | Sporadic PSP biology; MAPT-linked 4R tau predisposition; tau seeding/propagation | PSP is neuropathologically defined by aggregated 4R tau in neurons, astrocytes, and oligodendrocytes; tau inclusions include neurofibrillary tangles, tufted astrocytes, and coiled bodies; MAPT expression is preserved in all 3 cell types with tau aggregates, supporting ongoing local tau production that can feed aggregation/seeding (hoglinger2017clinicaldiagnosisof pages 2-3, whitney2024singlecelltranscriptomicand pages 1-2, forrest2023cellspecificmaptgene pages 1-2) | neuron (CL:0000540); astrocyte (CL:0000127); oligodendrocyte (CL:0000128) | subthalamic nucleus (UBERON:0001906); globus pallidus (UBERON:0002427); midbrain (UBERON:0001891); cerebellum (UBERON:0002037) | protein phosphorylation (GO:0006468); protein aggregation (GO:0070207); microtubule cytoskeleton organization (GO:0000226); neuron death (GO:0070997) | 10.1002/mds.26987 (2017); 10.1007/s00401-024-02823-w (2024); 10.1007/s00401-023-02604-x (2023) |
| MAPT haplotype-associated increase in 4R tau mRNA likely acts upstream of tau aggregation | 17q21.31 inversion / MAPT H1 haplotype; structural variation around MAPT/KANSL1 | H1 haplotype is the strongest common genetic risk with OR ~5.6; bulk RNA-seq showed increased total tau and 4R tau transcripts in PSP cerebellum and increased 4R tau reads in temporal cortex; 4R tau mRNA levels were significantly associated with H1 in temporal cortex, supporting an upstream splicing/expression mechanism (wang2024wholegenomesequencinganalysis pages 1-2, ressler2024mapthaplotypeassociatedtranscriptomic pages 1-2) | excitatory/inhibitory neuron (CL:0000540); astrocyte (CL:0000127); oligodendrocyte (CL:0000128) | cerebellum (UBERON:0002037); temporal cortex (UBERON:0016529); midbrain (UBERON:0001891) | regulation of mRNA splicing, via spliceosome (GO:0048024); RNA processing (GO:0006396); regulation of gene expression (GO:0010468) | 10.1186/s13024-024-00747-3 (2024); 10.1186/s40478-024-01839-3 (2024) |
| Integrated stress response / EIF2 signaling and PERK(EIF2AK3) activation links tau burden to maladaptive stress signaling and downstream apoptosis/autophagy failure | Genetic risk at EIF2AK3; chronic proteotoxic and ER stress induced by tau pathology | Single-nucleus RNA-seq of 50,708 nuclei from PSP diencephalon identified EIF2 signaling activated across vulnerable cell types; activated eIF2α positively correlated with tau pathology burden in subthalamic nucleus and thalamus and colocalized with p-tau-positive neurons and ALDH1L1-positive astrocytes; GWAS had already implicated EIF2AK3/PERK as a PSP risk locus (whitney2024singlecelltranscriptomicand pages 12-14, whitney2024singlecelltranscriptomicand pages 1-2) | neuron (CL:0000540); astrocyte (CL:0000127); oligodendrocyte (CL:0000128); microglial cell (CL:0000129) | subthalamic nucleus (UBERON:0001906); thalamus (UBERON:0001897); globus pallidus (UBERON:0002427); visual cortex / occipital cortex as relatively spared comparator (UBERON:0001870) | integrated stress response signaling (GO:0034976-related); response to endoplasmic reticulum stress (GO:0034976); translational initiation (GO:0006413); regulation of apoptotic process (GO:0042981); autophagy (GO:0006914) | 10.1007/s00401-024-02823-w (2024) |
| Axon-guidance, synaptic, vesicle-cytoskeletal, and cytokine-signaling modules are dysregulated in PSP CSF, consistent with circuit dysfunction downstream of tauopathy | Tau-mediated network degeneration and synaptic/axonal injury | SOMAmer CSF proteomics found 155/5,026, 959/7,595, and 321/5,026 differentially expressed SOMAmers across original, validation, and neuropathology-confirmed cohorts; three coexpression modules implicated synaptic function/JAK-STAT (beta = -0.044, corrected p = 0.002), vesicle-cytoskeletal trafficking (beta = 0.039, p = 0.007), and cytokine-cytokine receptor interaction (beta = -0.032, p = 0.035); axon guidance was the top dysregulated pathway across cohorts and an axon-guidance panel gave AUC 0.924/0.815/0.932 (wise2024csfproteomicsin pages 1-2) | neuron (CL:0000540); synapse-associated neuronal populations; astrocyte (CL:0000127) | dorsal midbrain (UBERON:0001891); globus pallidus (UBERON:0002427); subthalamic nucleus (UBERON:0001906) | axon guidance (GO:0007411); synapse organization (GO:0050808); vesicle-mediated transport (GO:0016192); JAK-STAT cascade (GO:0007259); cytokine-mediated signaling pathway (GO:0019221) | 10.1212/WNL.0000000000209585 (2024) |
| Complement/C4A-associated oligodendrocyte activation suggests glial and myelin-related mechanisms in PSP | PSP GWAS risk architecture; oligodendrocyte-specific regulatory effects; complement dysregulation | Integrative genetics/transcriptomics/histology work implicated glial activation, oligodendrocyte-specific epigenomic/eQTL effects at many loci, elevated C4A expression, and histologic colocalization of tau aggregates with C4 complement in oligodendrocytes; this supports complement-associated oligodendroglial pathology as part of etiopathogenesis (farrell2024genetictranscriptomichistological pages 4-7) | oligodendrocyte (CL:0000128); astrocyte (CL:0000127); microglial cell (CL:0000129) | white matter (UBERON:0002316); globus pallidus (UBERON:0002427); brainstem (UBERON:0002298) | complement activation (GO:0006956); gliogenesis (GO:0042063); myelination (GO:0042552); regulation of immune response (GO:0050776) | 10.1101/2023.11.09.565552 (2024 preprint) |
| White-matter DNA methylation changes implicate Wnt signaling, ER stress, mitochondrial dysfunction, RNA interference, and endosomal transport as convergent downstream molecular programs | Epigenetic dysregulation in parkinsonian white matter; shared but PSP-relevant white-matter pathology | EPIC-array profiling of frontal lobe white matter from PSP (n = 16) and controls identified co-methylation signatures affecting Wnt signaling, signal transduction, endoplasmic reticulum stress, mitochondrial processes, RNA interference, and endosomal transport; PSP white matter showed disease-specific and shared alterations relevant to neurodegeneration (murthy2024dnamethylationpatterns pages 1-2) | oligodendrocyte (CL:0000128); astrocyte (CL:0000127); microglial cell (CL:0000129) | frontal lobe white matter (UBERON suggestion: frontal lobe UBERON:0001870 + white matter UBERON:0002316); cerebrum white matter (UBERON:0002316) | Wnt signaling pathway (GO:0016055); response to endoplasmic reticulum stress (GO:0034976); mitochondrial ATP synthesis coupled electron transport (GO:0042775); endosomal transport (GO:0016197); RNA interference (GO:0016246) | 10.1007/s00401-024-02764-4 (2024) |
| Neuroinflammatory markers galectin-10 and CTLA-4 track clinical severity, indicating immune activation as a disease-modifying downstream process | Tau-triggered glial/immune activation; inflammatory remodeling of CSF proteome | In CSF proteomics, galectin-10 and CTLA-4 correlated with PSP Rating Scale scores across cohorts; inflammatory and cytokine-cytokine receptor interaction modules were also identified, supporting ongoing neuroimmune involvement in disease progression (wise2024csfproteomicsin pages 1-2) | microglial cell (CL:0000129); astrocyte (CL:0000127); infiltrating immune cell / T cell (CL:0000084 suggestion) | CSF-reflective pathology from subthalamic nucleus (UBERON:0001906), globus pallidus (UBERON:0002427), and dorsal midbrain (UBERON:0001891) | inflammatory response (GO:0006954); cytokine-mediated signaling pathway (GO:0019221); regulation of immune system process (GO:0002682) | 10.1212/WNL.0000000000209585 (2024) |


*Table: This table summarizes major molecular and cellular mechanisms implicated in progressive supranuclear palsy, linking genetic risk, tau biology, stress signaling, white-matter epigenetics, and neuroinflammation to vulnerable cell types and brain regions. It is useful for knowledge-base annotation because it also suggests ontology terms for cells, anatomy, and biological processes.*

Key recent mechanistic developments include:
- **Single-nucleus RNA-seq** (50,708 nuclei) in PSP diencephalon demonstrated **EIF2 signaling activation** across vulnerable cell types; activated eIF2α correlated with tau burden and localized to p-tau+ neurons and ALDH1L1+ astrocytes by multiplex imaging, supporting integrated stress response failure as a mechanistic component. (whitney2024singlecelltranscriptomicand pages 1-2, whitney2024singlecelltranscriptomicand pages 12-14)
- **CSF proteomics** (SomaScan) identified convergent downregulation of **axon guidance** and other modules (synaptic/JAK-STAT, vesicle-cytoskeletal trafficking, cytokine signaling) with high AUC discrimination panels, implicating circuit-level dysfunction consistent with axonal/synaptic pathology. (wise2024csfproteomicsin pages 1-2)
- A **MAPT expression** study using RNAscope + AT8 and snRNA-seq found MAPT transcripts in neurons, astrocytes, and oligodendrocytes and preserved expression in cells with tau aggregates, supporting ongoing local tau supply for aggregation/seeding and motivating dual therapeutic approaches. (forrest2023cellspecificmaptgene pages 1-2)

---

## 7. Anatomical Structures Affected

PSP pathology and biomarker studies emphasize subcortical and brainstem structures with additional cortical involvement depending on phenotype. Key regions include the **subthalamic nucleus, globus pallidus, dorsal midbrain**, and cerebellar/diencephalic structures, with clinical variants reflecting differing neuroanatomic distributions of pathology. (wise2024csfproteomicsin pages 1-2, whitney2024singlecelltranscriptomicand pages 1-2)

Cell types prominently implicated include **neurons, astrocytes, and oligodendrocytes**, consistent across neuropathology, transcriptomics, and genetic findings highlighting oligodendrocyte/myelin biology. (whitney2024singlecelltranscriptomicand pages 1-2, wang2024wholegenomesequencinganalysis pages 1-2)

---

## 8. Temporal Development

PSP typically begins after age 60 in many series, with diagnosis often delayed due to early symptom overlap with Parkinson’s disease and other atypical parkinsonisms. (jang2024biomarkerdiscoveryin pages 1-2, hoglinger2017clinicaldiagnosisof pages 2-3)

Real-world data show a multi-year prodrome before diagnosis, with falls and gait impairment commonly preceding formal diagnosis by ~1–2 years (median values among those with onset dates documented). (nysetvold2024progressivesupranuclearpalsy pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Recent biomarker and review sources report PSP-RS prevalence in the **2.3–10.6 per 100,000** range, with broader PSP prevalence estimates up to ~18 per 100,000 in some population studies. (wise2024csfproteomicsin pages 1-2, boxer2017advancesinprogressive pages 1-2)

### 9.2 Inheritance
PSP is predominantly **sporadic**, with rare familial MAPT mutation-associated PSP-like syndromes. MDS criteria incorporate genetic findings into exclusion/context decisions and distinguish inherited vs sporadic PSP when MAPT mutations are present. (hoglinger2017clinicaldiagnosisof pages 3-4, whitney2024singlecelltranscriptomicand pages 1-2)

### 9.3 Prognosis and natural history
- Median survival estimates include **~6.9 years** in PSP-RS (biomarker cohort) and **median 7.3 years after symptom onset** in the gosuranemab PASSPORT trial report. (wise2024csfproteomicsin pages 1-2, dam2021safetyandefficacy pages 1-6)
- In a representative UK cohort (n=227), survival was longer in variant phenotypes than Richardson’s syndrome (**7.3 vs 5.6 years**, P=0.02), and annual cognitive decline differed by phenotype (MMSE -1.8 vs -0.9/year; ACE-R -5.3 vs -3.0/year). (street2021clinicalprogressionof pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria (authoritative)
The **2017 Movement Disorder Society (MDS) criteria** were developed to improve early and variant-phenotype sensitivity relative to NINDS-SPSP criteria, while maintaining specificity. They incorporate mandatory inclusion/exclusion criteria and define diagnostic certainty categories (probable, possible, suggestive) based on combinations of features across four functional domains. (hoglinger2017clinicaldiagnosisof pages 2-3)

Key excerpted features include:
- NINDS-SPSP “probable” PSP requires vertical supranuclear gaze palsy plus postural instability and falls within 1 year, but sensitivity is limited early and for variants. (hoglinger2017clinicaldiagnosisof pages 2-3)
- MDS-PSP criteria incorporate imaging/laboratory/genetic context; for example, in PSP-CBS, CSF constellations typical of AD (elevated total/p-tau plus reduced Aβ42) or amyloid PET are used to exclude primary AD pathology. (hoglinger2017clinicaldiagnosisof pages 3-4)

### 10.2 Biomarkers and imaging (2024 priority)
A structured biomarker summary is provided below.

| Biomarker / diagnostic feature | Modality / specimen | Intended use | Key quantitative finding | Source (DOI / year) |
|---|---|---|---|---|
| Neurofilament light chain (NfL) | CSF and plasma | Prognosis; supportive differential diagnosis | NfL concentrations are reported to be **2–5× higher in PSP CSF** than in healthy controls and PD; similar plasma elevation reported, but specificity remains limited (jang2024biomarkerdiscoveryin pages 1-2) | 10.1186/s12014-024-09507-3 / 2024 |
| CSF p-tau181 | CSF | Prognosis / disease monitoring | **Low CSF p-tau181** has been associated with **faster clinical progression** in PSP, but sensitivity/specificity are limited (wise2024csfproteomicsin pages 1-2) | 10.1212/WNL.0000000000209585 / 2024 |
| Axon-guidance protein panel | CSF SOMAmer proteomics | Diagnostic discrimination | Axon-guidance proteins discriminated PSP vs controls with **AUC 0.924** (original cohort), **0.815** (validation), and **0.932** (neuropathology-confirmed cohort); top dysregulated pathway across cohorts (wise2024csfproteomicsin pages 1-2) | 10.1212/WNL.0000000000209585 / 2024 |
| Galectin-10 (CLC) and CTLA-4 | CSF SOMAmer proteomics | Severity / progression correlation | Two inflammatory proteins, **galectin-10** and **CTLA-4**, correlated with **PSP Rating Scale** severity across cohorts (wise2024csfproteomicsin pages 1-2) | 10.1212/WNL.0000000000209585 / 2024 |
| ATP6AP2 | CSF TMT mass-spectrometry proteomics | Diagnostic discrimination | **ATP6AP2 reduced in PSP** and had the highest classification performance with **AUC 0.922** for PSP vs PD/HC (jang2024biomarkerdiscoveryin pages 1-2) | 10.1186/s12014-024-09507-3 / 2024 |
| Additional CSF proteomic candidates | CSF TMT mass-spectrometry proteomics | Diagnostic panel development | Other top candidates included **NEFM, EFEMP2, LAMP2, CHST12, FAT2, B4GALT1, LCAT, CBLN3, FSTL5, ATP6AP1, GGH**; pathways enriched for **cell adhesion, cholesterol metabolism, glycan biosynthesis** (jang2024biomarkerdiscoveryin pages 1-2) | 10.1186/s12014-024-09507-3 / 2024 |
| Serum p-tau396 | Serum ELISA / SIMOA-based pilot biomarker study | Clinical staging / severity tracking | Of six serum tau species tested, **only p-tau396 was detectable**; it was **higher in PSP and PD vs controls** but overlapped between PSP and PD, and **strongly correlated with disease severity in PSP** (cristiani2024serumtauspecies pages 1-2) | 10.3390/diagnostics14232746 / 2024 |
| Serum tau species panel (t-tau, 4R-tau, tau aggregates, p-tau202, p-tau231, p-tau396) | Serum | Exploratory differential diagnosis | Most serum tau species were **undetectable or too low for ELISA**, arguing against current routine serum tau-species discrimination of PSP vs PD except possible staging value for p-tau396 (cristiani2024serumtauspecies pages 1-2) | 10.3390/diagnostics14232746 / 2024 |
| 18F-PI-2620 tau-PET | Tau PET | In vivo tau pathology; diagnostic enrichment; progression staging | In probable PSP-RS, **subcortical tau uptake** was associated with **higher NfL and NfL/t-tau**, lower GFAP-related ratios, **reduced brain volume**, and **worse executive function**; patients showed higher fluid biomarker levels than controls (dilcher2024linkingpi2620taupet pages 1-5) | 10.1101/2024.10.14.24315486 / 2024 |
| NfL/t-tau ratio with PI-2620 tau-PET | Plasma/CSF + tau PET | Trial biomarker / disease monitoring | Biomarker ratios showed strong patient-control separation; reported **NfL/t-tau 98.9% (95% CI 96.16%–100%)** in comparative analysis and correlated with tau-PET burden (dilcher2024linkingpi2620taupet pages 1-5) | 10.1101/2024.10.14.24315486 / 2024 |
| MRI midbrain and superior cerebellar peduncle atrophy | Structural MRI | Supportive diagnosis / differential diagnosis | **Midbrain** and **superior cerebellar peduncle atrophy** help differentiate PSP-RS; classic **“hummingbird”** and **“morning glory”** signs have **100% specificity but limited sensitivity** (boxer2017advancesinprogressive pages 4-5) | 10.1016/S1474-4422(17)30157-6 / 2017 |
| MRI / imaging supportive findings in MDS criteria | Imaging | Supportive diagnosis; exclusion of mimics | MDS criteria include imaging as supportive and exclusionary context; relevant structural abnormalities and severe leukoencephalopathy are exclusionary, underscoring MRI’s role in ruling out mimics (hoglinger2017clinicaldiagnosisof pages 2-3, hoglinger2017clinicaldiagnosisof pages 3-4) | 10.1002/mds.26987 / 2017 |


*Table: This table summarizes key fluid and imaging biomarkers for progressive supranuclear palsy, including diagnostic and prognostic use cases, quantitative findings, and source citations. It is useful for comparing emerging 2024 proteomic and tau-PET markers with established MRI and CSF indicators.*

Highlights include:
- CSF mass-spectrometry proteomics identified ATP6AP2 as a strong discriminator (AUC 0.922) and enriched pathways (cell adhesion, cholesterol metabolism, glycan biosynthesis). (jang2024biomarkerdiscoveryin pages 1-2)
- SomaScan CSF proteomics identified axon-guidance pathway protein panels with AUC up to 0.932 and inflammatory correlates of severity. (wise2024csfproteomicsin pages 1-2)
- 18F-PI-2620 tau PET was associated with fluid biomarker ratios and cognition/atrophy in probable PSP-RS (preprint evidence). (dilcher2024linkingpi2620taupet pages 1-5)

---

## 11. Outcome / Prognosis

PSP has rapid progression with substantial disability burden and limited disease-modifying options; survival is typically on the order of 5–8 years from symptom onset depending on phenotype and cohort. (dam2021safetyandefficacy pages 1-6, street2021clinicalprogressionof pages 1-2)

Real-world studies show high healthcare utilization, including near-universal medication and imaging use, high assistive-device and supportive-care use, and increasing costs over time. (nysetvold2024progressivesupranuclearpalsy pages 1-2, barer2023progressivesupranuclearpalsy’s pages 1-2)

---

## 12. Treatment

### 12.1 Symptomatic and supportive care (real-world implementation)
Real-world care pathways rely heavily on symptomatic management and supportive services. In a US/Canada medical-record cohort, the most widely used resources (≥85% of participants at some point) were medications (100%), imaging (99%), assistive devices (90%), supportive care (86%), and surgeries/procedures (85%). (nysetvold2024progressivesupranuclearpalsy pages 1-2)

In an Israeli payer-provider cohort, symptomatic therapies listed include levodopa/dopamine agonists/amantadine for motor symptoms (often mild/transient benefit), sleep and ocular symptom treatments, constipation management, antidepressants, and botulinum toxin for selected dystonia/sialorrhea syndromes; multidisciplinary therapy (physical, speech, occupational, social work) is emphasized. (barer2023progressivesupranuclearpalsy’s pages 1-2)

Suggested MAXO terms (labels): monoclonal antibody therapy; fecal microbiota transplantation; physical therapy; speech therapy; occupational therapy; assistive device use; supportive care.

### 12.2 Disease-modifying and experimental therapies (trials)
A consolidated trial table (including pipeline trials) is provided.

| Intervention / study | Class / mechanism | Trial ID | Phase | Status | Sample size | Key endpoint / quantitative result | URL | Citation |
|---|---|---|---|---|---:|---|---|---|
| Gosuranemab (PASSPORT) | Anti-tau monoclonal antibody targeting N-terminal tau | NCT03068468 | Phase 2 | Completed; open-label extension discontinued after lack of efficacy | 486 dosed (321 gosuranemab, 165 placebo) | Primary endpoint not met at week 52: adjusted mean PSP Rating Scale (PSPRS) change 10.4 vs 10.6, *P*=0.85; strong target engagement in CSF unbound N-terminal tau: -98% with gosuranemab vs +11% with placebo; AE and death rates similar between groups | https://clinicaltrials.gov/study/NCT03068468 ; https://doi.org/10.1038/s41591-021-01455-x | (dam2021safetyandefficacy pages 1-6) |
| Tilavonemab / ABBV-8E12 (ARISE) | Anti-tau monoclonal antibody binding N-terminus of human tau | NCT02985879 | Phase 2 | Terminated early for futility | 377 treated / analyzed (126 2000 mg, 125 4000 mg, 126 placebo) | Primary endpoint: change in PSPRS at week 52; no benefit vs placebo. Between-group difference vs placebo: 2000 mg 0.0 (95% CI -2.6 to 2.6), *p*>0.99; 4000 mg 1.0 (95% CI -1.6 to 3.6), *p*=0.46; similar safety profile across groups | https://clinicaltrials.gov/study/NCT02985879 ; https://doi.org/10.1016/S1474-4422(20)30489-0 | (hoglinger2021safetyandefficacy pages 1-2, hoglinger2021safetyandefficacy pages 6-7) |
| Faecal microbiota transplantation (FMT) in PSP-RS | Microbiome-directed therapy / fecal microbiota transplantation | ChiCTR-2100045397 | Phase 2 | Completed | 68 randomized | Primary outcome at week 16: PSPRS improved from 40.1 to 36.9 in FMT group vs 40.1 to 41.7 in placebo; treatment benefit 4.3 (95% CI 3.2-5.4), *P*<0.0001; also improved constipation, depression, and anxiety | https://www.chictr.org.cn/showproj.html?proj=124265 ; https://doi.org/10.1016/j.eclinm.2023.101888 | (tian2023efficacyoffaecal pages 1-2) |
| NIO752 | Investigational disease-modifying therapy for PSP (mechanism not specified in retrieved trial context) | NCT07498426 | Phase 3 | Recruiting | 300 planned | Efficacy study in PSP; primary endpoint not provided in retrieved trial summary | https://clinicaltrials.gov/study/NCT07498426 | (OpenTargets Search: Progressive supranuclear palsy) |
| AADvac1 | Active tau immunotherapy / anti-tau vaccine | NCT07217665 | Phase 2 | Not yet recruiting | 146 planned | PSP platform trial regimen A; endpoint not provided in retrieved trial summary | https://clinicaltrials.gov/study/NCT07217665 | (OpenTargets Search: Progressive supranuclear palsy, boxer2017advancesinprogressive pages 8-9) |
| LM11A-31 | Small-molecule neuroprotective candidate (p75NTR modulator; mechanism not detailed in retrieved context) | NCT07264283 | Phase 2 | Not yet recruiting | 147 planned | PSP platform trial regimen B; endpoint not provided in retrieved trial summary | https://clinicaltrials.gov/study/NCT07264283 | (OpenTargets Search: Progressive supranuclear palsy) |
| FNP-223 | Investigational disease-modifying therapy for PSP | NCT06355531 | Phase 2 | Active, not recruiting | 241 planned | Study to assess efficacy, safety, and pharmacokinetics to slow PSP progression; primary endpoint not provided in retrieved trial summary | https://clinicaltrials.gov/study/NCT06355531 | (OpenTargets Search: Progressive supranuclear palsy) |
| Syde® digital endpoints study | Digital monitoring / observational endpoint feasibility study | NCT07389018 | Observational | Not yet recruiting | 30 planned | Feasibility of digital endpoints for monitoring PSP-Richardson syndrome | https://clinicaltrials.gov/study/NCT07389018 | (OpenTargets Search: Progressive supranuclear palsy) |
| Art therapy in PSP | Supportive / non-pharmacologic intervention | NCT06588673 | Not applicable | Active, not recruiting | 10 planned | Interventional supportive-care study; endpoint not provided in retrieved trial summary | https://clinicaltrials.gov/study/NCT06588673 | (OpenTargets Search: Progressive supranuclear palsy) |
| GV1001 subcutaneous | Investigational peptide therapy | NCT05819658 | Phase 2 | Completed | 78 planned | Treatment study in PSP; endpoint/results not provided in retrieved trial summary | https://clinicaltrials.gov/study/NCT05819658 | (OpenTargets Search: Progressive supranuclear palsy) |
| GV1001 extension | Extension study for prior GV1001 PSP trial completers | NCT06235775 | Phase 2 | Completed | 67 planned | Extension study; endpoint/results not provided in retrieved trial summary | https://clinicaltrials.gov/study/NCT06235775 | (OpenTargets Search: Progressive supranuclear palsy) |
| TPN-101 | Investigational therapy | NCT04993768 | Phase 2a | Completed | 42 planned | Phase 2a study in PSP; endpoint/results not provided in retrieved trial summary | https://clinicaltrials.gov/study/NCT04993768 | (OpenTargets Search: Progressive supranuclear palsy) |
| RT001 | Investigational therapy | NCT04937530 | Phase 2 | Unknown | 40 planned | PSP treatment study; endpoint/results not provided in retrieved trial summary | https://clinicaltrials.gov/study/NCT04937530 | (OpenTargets Search: Progressive supranuclear palsy) |
| Real-world care utilization cohort (US/Canada) | Retrospective observational real-world management study | Not a trial | Observational | Published | 72 | Median onset before diagnosis: first fall 2.0 years, unsteady gait/gait impairment 1.2 years, mobility problems 0.8 years; healthcare resources used at some point: medications 100%, imaging 99%, assistive devices 90%, supportive care 86%, surgeries/procedures 85% | https://doi.org/10.1186/s13023-024-03168-z | (nysetvold2024progressivesupranuclearpalsy pages 1-2, nysetvold2024progressivesupranuclearpalsy pages 2-4) |
| Real-world economic burden cohort (Israel) | Retrospective healthcare utilization / cost study | Not a trial | Observational | Published | 88 PSP, 264 matched controls | Annual direct costs rose from US$8,910 in year before diagnosis to US$21,637 in year 5 and US$36,693 in year 10; costs about 2-fold higher than controls in year prior diagnosis and ~1.5-fold higher in year after diagnosis | https://doi.org/10.1007/s00415-023-11714-1 | (barer2023progressivesupranuclearpalsy’s pages 1-2, barer2023progressivesupranuclearpalsy’s pages 4-5) |


*Table: This table summarizes interventional PSP studies with reported outcomes, active pipeline trials from retrieved ClinicalTrials.gov results, and real-world management/cost studies. It is useful for quickly comparing therapeutic classes, trial status, quantitative efficacy signals, and care burden.*

Key completed disease-modifying trial outcomes:
- **Gosuranemab (NCT03068468)**: no clinical benefit (PSPRS change 10.4 vs 10.6 at week 52; P=0.85) despite strong CSF N-terminal tau target engagement (-98%). (dam2021safetyandefficacy pages 1-6)
- **Tilavonemab/ABBV-8E12 (NCT02985879)**: terminated for futility; no PSPRS benefit at week 52 vs placebo. (hoglinger2021safetyandefficacy pages 1-2)

Notable 2023–2024 development:
- **FMT in PSP-RS** (ChiCTR-2100045397): phase 2 single-center trial showed improvement in PSPRS at week 16 and sustained nonmotor symptom improvements, providing a provocative but as-yet single-center signal requiring replication. (tian2023efficacyoffaecal pages 1-2)

---

## 13. Prevention

No primary prevention or proven protective factors were identified in the retrieved evidence set. Current best-supported “prevention” is tertiary: reducing falls and aspiration risk, managing dysphagia/constipation/mood symptoms, and implementing assistive devices and supportive therapies early. (nysetvold2024progressivesupranuclearpalsy pages 1-2, barer2023progressivesupranuclearpalsy’s pages 1-2)

Earlier detection is being advanced via MDS criteria adoption and emerging biomarkers (CSF proteomic panels, tau PET, NfL-based staging/prognosis). (hoglinger2017clinicaldiagnosisof pages 2-3, wise2024csfproteomicsin pages 1-2)

---

## 14. Other Species / Natural Disease

No naturally occurring PSP-equivalent disease in non-human species was identified in the retrieved sources for this run.

---

## 15. Model Organisms and Experimental Models (2023–2024)

A major current limitation is that conventional iPSC-derived neurons express low 4R tau, hindering modeling of 4R tauopathies such as PSP. A 2024 Cell study reports engineered hiPSC-derived neuronal lines expressing 4R tau (and 4R P301S) that develop progressive tau inclusions after seeding and enable CRISPRi screens identifying modifiers of tau propagation, supporting human-relevant target discovery platforms. (bravo2024humanipsc4r pages 1-3)

Human tissue-based mechanistic mapping supports glial involvement: MAPT transcripts were detected and preserved in neurons, astrocytes, and oligodendrocytes with tau aggregates in PSP, motivating combined approaches (reduce MAPT expression plus remove misfolded tau). (forrest2023cellspecificmaptgene pages 1-2)

---

## Expert opinion / analysis (authoritative synthesis)

Two overarching themes emerge from authoritative and recent sources:
1) PSP is best conceptualized as a spectrum of clinical phenotypes underpinned by a shared 4R tau neuropathology; therefore, diagnostic frameworks and biomarkers must capture early and variant presentations rather than only PSP-RS. This is the central rationale of the 2017 MDS criteria revision. (hoglinger2017clinicaldiagnosisof pages 2-3, boxer2017advancesinprogressive pages 1-2)
2) The lack of clinical efficacy in anti-tau antibody trials despite strong CSF target engagement implies that either the targeted tau species/compartment is not causally dominant, the intervention timing is too late, or pharmacology does not adequately address intracellular pathology and downstream stress/inflammatory cascades. This motivates: (i) better pharmacodynamic and disease-biology biomarkers, and (ii) multi-target approaches addressing upstream splicing/expression (MAPT), intracellular proteostasis/ISR, and neuroimmune pathways. (dam2021safetyandefficacy pages 1-6, whitney2024singlecelltranscriptomicand pages 1-2, wise2024csfproteomicsin pages 1-2)

---

## Key statistics (recent and high-value)
- Prevalence: PSP-RS 2.3–10.6 per 100,000 (wise2024csfproteomicsin pages 1-2); broader PSP up to ~18 per 100,000 in some studies (boxer2017advancesinprogressive pages 1-2).
- Survival: PSP-RS median survival 6.9 years (wise2024csfproteomicsin pages 1-2); death within median 7.3 years after symptom onset in PASSPORT report (dam2021safetyandefficacy pages 1-6).
- Real-world prediagnosis timing: first fall median 2.0 years before diagnosis; gait impairment 1.2 years; mobility problems 0.8 years (nysetvold2024progressivesupranuclearpalsy pages 1-2).
- Genetics: MAPT H1 haplotype OR ~5.6 (wang2024wholegenomesequencinganalysis pages 1-2); SV burden P=6.73×10^-3 (wang2024wholegenomesequencinganalysis pages 1-2).
- Biomarkers: ATP6AP2 AUC 0.922 in CSF proteomics (jang2024biomarkerdiscoveryin pages 1-2); axon-guidance CSF panel AUC up to 0.932 (wise2024csfproteomicsin pages 1-2).
- Trial outcomes: gosuranemab PSPRS 10.4 vs 10.6 at 52 weeks, P=0.85, with CSF N-term tau -98% (dam2021safetyandefficacy pages 1-6); tilavonemab no PSPRS benefit (hoglinger2021safetyandefficacy pages 1-2); FMT benefit 4.3 PSPRS points at week 16 (tian2023efficacyoffaecal pages 1-2).
- Healthcare costs: annual direct costs rose to US$21,637 at year 5 and US$36,693 at year 10 vs US$8,910 pre-diagnosis (barer2023progressivesupranuclearpalsy’s pages 1-2).

---

## Limitations of this report (data availability)
- OMIM, MeSH, ICD-10, and Orphanet numeric identifiers were not explicitly retrievable in the provided texts beyond MONDO and Orphanet subtype labels surfaced via OpenTargets.
- Variant-level details (ClinVar classifications, allele frequencies) and PSP-specific environmental risk/protective factors were not captured in this retrieval.
- Some biomarker and imaging findings (e.g., PI-2620 tau PET linkage) were available as preprint evidence.


References

1. (hoglinger2017clinicaldiagnosisof pages 2-3): Günter U. Höglinger, Gesine Respondek, Maria Stamelou, Carolin Kurz, Keith A. Josephs, Anthony E. Lang, Brit Mollenhauer, Ulrich Müller, Christer Nilsson, Jennifer L. Whitwell, Thomas Arzberger, Elisabet Englund, Ellen Gelpi, Armin Giese, David J. Irwin, Wassilios G. Meissner, Alexander Pantelyat, Alex Rajput, John C. van Swieten, Claire Troakes, Angelo Antonini, Kailash P. Bhatia, Yvette Bordelon, Yaroslau Compta, Jean-Christophe Corvol, Carlo Colosimo, Dennis W. Dickson, Richard Dodel, Leslie Ferguson, Murray Grossman, Jan Kassubek, Florian Krismer, Johannes Levin, Stefan Lorenzl, Huw R. Morris, Peter Nestor, Wolfgang H. Oertel, Werner Poewe, Gil Rabinovici, James B. Rowe, Gerard D. Schellenberg, Klaus Seppi, Thilo van Eimeren, Gregor K. Wenning, Adam L. Boxer, Lawrence I. Golbe, and Irene Litvan. Clinical diagnosis of progressive supranuclear palsy: the movement disorder society criteria. Movement Disorders, 32:853-864, Jun 2017. URL: https://doi.org/10.1002/mds.26987, doi:10.1002/mds.26987. This article has 2649 citations and is from a highest quality peer-reviewed journal.

2. (wise2024csfproteomicsin pages 1-2): Amy Wise, Jingyao Li, Mai Yamakawa, Joseph Loureiro, Brant Peterson, Kathleen Worringer, Rajeev Sivasankaran, Jose-Alberto Palma, Laura Mitic, Hilary W. Heuer, Argentina Lario-Lago, Adam M. Staffaroni, Annie Clark, Jack Taylor, Peter A. Ljubenkov, Lawren Vandevrede, Lea T. Grinberg, Salvatore Spina, William W. Seeley, Bruce L. Miller, Bradley F. Boeve, Bradford C. Dickerson, Murray Grossman, Irene Litvan, Alexander Pantelyat, Maria Carmela Tartaglia, Zihan Zhang, Anne-Marie A. Wills, Jessica Rexach, Julio C. Rojas, and Adam L. Boxer. Csf proteomics in patients with progressive supranuclear palsy. Neurology, Aug 2024. URL: https://doi.org/10.1212/wnl.0000000000209585, doi:10.1212/wnl.0000000000209585. This article has 15 citations and is from a highest quality peer-reviewed journal.

3. (whitney2024singlecelltranscriptomicand pages 1-2): Kristen Whitney, Won-Min Song, Abhijeet Sharma, Diana K. Dangoor, Kurt Farrell, Margaret M. Krassner, Hadley W. Ressler, Thomas D. Christie, Shrishtee Kandoi, Ruth H. Walker, Melissa J. Nirenberg, Steven J. Frucht, Giulietta M. Riboldi, Bin Zhang, Ana C. Pereira, and John F. Crary. Single-cell transcriptomic and neuropathologic analysis reveals dysregulation of the integrated stress response in progressive supranuclear palsy. Acta Neuropathologica, Dec 2024. URL: https://doi.org/10.1007/s00401-024-02823-w, doi:10.1007/s00401-024-02823-w. This article has 15 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: Progressive supranuclear palsy): Open Targets Query (Progressive supranuclear palsy, 9 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (barer2023progressivesupranuclearpalsy’s pages 1-2): Yael Barer, Raanan Cohen, Meital Grabarnik-John, Xiaolan Ye, Jorge Zamudio, Tanya Gurevich, and Gabriel Chodick. Progressive supranuclear palsy’s economical burden: the use and costs of healthcare resources in a large health provider in israel. Journal of Neurology, 270:3770-3778, Apr 2023. URL: https://doi.org/10.1007/s00415-023-11714-1, doi:10.1007/s00415-023-11714-1. This article has 2 citations and is from a domain leading peer-reviewed journal.

6. (hoglinger2017clinicaldiagnosisof pages 3-4): Günter U. Höglinger, Gesine Respondek, Maria Stamelou, Carolin Kurz, Keith A. Josephs, Anthony E. Lang, Brit Mollenhauer, Ulrich Müller, Christer Nilsson, Jennifer L. Whitwell, Thomas Arzberger, Elisabet Englund, Ellen Gelpi, Armin Giese, David J. Irwin, Wassilios G. Meissner, Alexander Pantelyat, Alex Rajput, John C. van Swieten, Claire Troakes, Angelo Antonini, Kailash P. Bhatia, Yvette Bordelon, Yaroslau Compta, Jean-Christophe Corvol, Carlo Colosimo, Dennis W. Dickson, Richard Dodel, Leslie Ferguson, Murray Grossman, Jan Kassubek, Florian Krismer, Johannes Levin, Stefan Lorenzl, Huw R. Morris, Peter Nestor, Wolfgang H. Oertel, Werner Poewe, Gil Rabinovici, James B. Rowe, Gerard D. Schellenberg, Klaus Seppi, Thilo van Eimeren, Gregor K. Wenning, Adam L. Boxer, Lawrence I. Golbe, and Irene Litvan. Clinical diagnosis of progressive supranuclear palsy: the movement disorder society criteria. Movement Disorders, 32:853-864, Jun 2017. URL: https://doi.org/10.1002/mds.26987, doi:10.1002/mds.26987. This article has 2649 citations and is from a highest quality peer-reviewed journal.

7. (nasri2024phenotypicspectrumof pages 1-2): Amina Nasri, Ikram Sghaier, Anis Neji, Alya Gharbi, Youssef Abida, Saloua Mrabet, Amina Gargouri, Mouna Ben Djebara, Imen Kacem, and Riadh Gouider. Phenotypic spectrum of progressive supranuclear palsy: clinical study and apolipoprotein e effect. Journal of Movement Disorders, 17:158-170, Apr 2024. URL: https://doi.org/10.14802/jmd.23178, doi:10.14802/jmd.23178. This article has 13 citations and is from a peer-reviewed journal.

8. (boxer2017advancesinprogressive pages 3-4): Adam L Boxer, Jin-Tai Yu, Lawrence I Golbe, Irene Litvan, Anthony E Lang, and Günter U Höglinger. Advances in progressive supranuclear palsy: new diagnostic criteria, biomarkers, and therapeutic approaches. Jul 2017. URL: https://doi.org/10.1016/s1474-4422(17)30157-6, doi:10.1016/s1474-4422(17)30157-6. This article has 515 citations and is from a highest quality peer-reviewed journal.

9. (nysetvold2024progressivesupranuclearpalsy pages 1-2): Ella Nysetvold, Lauren N. Lopez, Ashley N. Cogell, Henrik Fryk, Nelson D. Pace, Sara Snell Taylor, Joyce Rhoden, Caitlin A. Nichols, Demetris Pillas, Alexander Klein, Teresa Gasalla, and Anna Scowcroft. Progressive supranuclear palsy (psp) disease progression, management, and healthcare resource utilization: a retrospective observational study in the us and canada. Orphanet Journal of Rare Diseases, May 2024. URL: https://doi.org/10.1186/s13023-024-03168-z, doi:10.1186/s13023-024-03168-z. This article has 9 citations and is from a peer-reviewed journal.

10. (wang2024wholegenomesequencinganalysis pages 1-2): Hui Wang, Timothy S. Chang, Beth A. Dombroski, Po-Liang Cheng, Vishakha Patil, Leopoldo Valiente-Banuet, Kurt Farrell, Catriona Mclean, Laura Molina-Porcel, Alex Rajput, Peter Paul De Deyn, Nathalie Le Bastard, Marla Gearing, Laura Donker Kaat, John C. Van Swieten, Elise Dopper, Bernardino F. Ghetti, Kathy L. Newell, Claire Troakes, Justo G. de Yébenes, Alberto Rábano-Gutierrez, Tina Meller, Wolfgang H. Oertel, Gesine Respondek, Maria Stamelou, Thomas Arzberger, Sigrun Roeber, Ulrich Müller, Franziska Hopfner, Pau Pastor, Alexis Brice, Alexandra Durr, Isabelle Le Ber, Thomas G. Beach, Geidy E. Serrano, Lili-Naz Hazrati, Irene Litvan, Rosa Rademakers, Owen A. Ross, Douglas Galasko, Adam L. Boxer, Bruce L. Miller, Willian W. Seeley, Vivanna M. Van Deerlin, Edward B. Lee, Charles L. White, Huw Morris, Rohan de Silva, John F. Crary, Alison M. Goate, Jeffrey S. Friedman, Yuk Yee Leung, Giovanni Coppola, Adam C. Naj, Li-San Wang, Clifton Dalgard, Dennis W. Dickson, Günter U. Höglinger, Gerard D. Schellenberg, Daniel H. Geschwind, and Wan-Ping Lee. Whole-genome sequencing analysis reveals new susceptibility loci and structural variants associated with progressive supranuclear palsy. Molecular Neurodegeneration, Aug 2024. URL: https://doi.org/10.1186/s13024-024-00747-3, doi:10.1186/s13024-024-00747-3. This article has 38 citations and is from a highest quality peer-reviewed journal.

11. (ressler2024mapthaplotypeassociatedtranscriptomic pages 1-2): Hadley W. Ressler, Jack Humphrey, Ricardo A. Vialle, Bergan Babrowicz, Shrishtee Kandoi, Towfique Raj, Dennis W. Dickson, Nilüfer Ertekin-Taner, John F. Crary, and Kurt Farrell. Mapt haplotype-associated transcriptomic changes in progressive supranuclear palsy. Acta Neuropathologica Communications, Aug 2024. URL: https://doi.org/10.1186/s40478-024-01839-3, doi:10.1186/s40478-024-01839-3. This article has 12 citations and is from a peer-reviewed journal.

12. (dunning2024pharmacotherapiesforthe pages 3-4): Elise E. Dunning, Boris Decourt, Nasser H. Zawia, Holly A. Shill, and Marwan N. Sabbagh. Pharmacotherapies for the treatment of progressive supranuclear palsy: a narrative review. Neurology and Therapy, 13:975-1013, May 2024. URL: https://doi.org/10.1007/s40120-024-00614-9, doi:10.1007/s40120-024-00614-9. This article has 9 citations and is from a domain leading peer-reviewed journal.

13. (nysetvold2024progressivesupranuclearpalsy pages 2-4): Ella Nysetvold, Lauren N. Lopez, Ashley N. Cogell, Henrik Fryk, Nelson D. Pace, Sara Snell Taylor, Joyce Rhoden, Caitlin A. Nichols, Demetris Pillas, Alexander Klein, Teresa Gasalla, and Anna Scowcroft. Progressive supranuclear palsy (psp) disease progression, management, and healthcare resource utilization: a retrospective observational study in the us and canada. Orphanet Journal of Rare Diseases, May 2024. URL: https://doi.org/10.1186/s13023-024-03168-z, doi:10.1186/s13023-024-03168-z. This article has 9 citations and is from a peer-reviewed journal.

14. (dam2021safetyandefficacy pages 1-6): Tien Dam, Adam L. Boxer, Lawrence I. Golbe, Günter U. Höglinger, Huw R. Morris, Irene Litvan, Anthony E. Lang, Jean-Christophe Corvol, Ikuko Aiba, Michael Grundman, Lili Yang, Beth Tidemann-Miller, Joseph Kupferman, Kristine Harper, Kubra Kamisoglu, Michael J. Wald, Danielle L. Graham, Liz Gedney, John O’Gorman, and Samantha Budd Haeberlein. Safety and efficacy of anti-tau monoclonal antibody gosuranemab in progressive supranuclear palsy: a phase 2, randomized, placebo-controlled trial. Nature Medicine, 27:1451-1457, Aug 2021. URL: https://doi.org/10.1038/s41591-021-01455-x, doi:10.1038/s41591-021-01455-x. This article has 162 citations and is from a highest quality peer-reviewed journal.

15. (street2021clinicalprogressionof pages 1-2): Duncan Street, Maura Malpetti, Timothy Rittman, Boyd C P Ghosh, Alexander G Murley, Ian Coyle-Gilchrist, Luca Passamonti, and James B Rowe. Clinical progression of progressive supranuclear palsy: impact of trials bias and phenotype variants. Brain Communications, Sep 2021. URL: https://doi.org/10.1093/braincomms/fcab206, doi:10.1093/braincomms/fcab206. This article has 35 citations and is from a peer-reviewed journal.

16. (tian2023efficacyoffaecal pages 1-2): Haiyan Tian, Jiuqi Wang, Renyi Feng, Rui Zhang, Han Liu, Chi Qin, Lin Meng, Yongkang Chen, Yu Fu, Dongxiao Liang, Xin Yuan, Yanping Zhai, Qingyong Zhu, Lingjing Jin, Junfang Teng, Xuebing Ding, and Xuejing Wang. Efficacy of faecal microbiota transplantation in patients with progressive supranuclear palsy-richardson's syndrome: a phase 2, single centre, randomised clinical trial. Apr 2023. URL: https://doi.org/10.1016/j.eclinm.2023.101888, doi:10.1016/j.eclinm.2023.101888. This article has 31 citations and is from a peer-reviewed journal.

17. (murthy2024dnamethylationpatterns pages 1-2): Megha Murthy, Katherine Fodder, Yasuo Miki, Naiomi Rambarack, Eduardo De Pablo Fernandez, Lasse Pihlstrøm, Jonathan Mill, Thomas T. Warner, Tammaryn Lashley, and Conceição Bettencourt. Dna methylation patterns in the frontal lobe white matter of multiple system atrophy, parkinson’s disease, and progressive supranuclear palsy: a cross-comparative investigation. Acta Neuropathologica, Jul 2024. URL: https://doi.org/10.1007/s00401-024-02764-4, doi:10.1007/s00401-024-02764-4. This article has 14 citations and is from a highest quality peer-reviewed journal.

18. (forrest2023cellspecificmaptgene pages 1-2): Shelley L. Forrest, Seojin Lee, Nasna Nassir, Ivan Martinez-Valbuena, Valerie Sackmann, Jun Li, Awab Ahmed, Maria Carmela Tartaglia, Lars M. Ittner, Anthony E. Lang, Mohammed Uddin, and Gabor G. Kovacs. Cell-specific mapt gene expression is preserved in neuronal and glial tau cytopathologies in progressive supranuclear palsy. Acta Neuropathologica, 146:395-414, Jun 2023. URL: https://doi.org/10.1007/s00401-023-02604-x, doi:10.1007/s00401-023-02604-x. This article has 45 citations and is from a highest quality peer-reviewed journal.

19. (whitney2024singlecelltranscriptomicand pages 12-14): Kristen Whitney, Won-Min Song, Abhijeet Sharma, Diana K. Dangoor, Kurt Farrell, Margaret M. Krassner, Hadley W. Ressler, Thomas D. Christie, Shrishtee Kandoi, Ruth H. Walker, Melissa J. Nirenberg, Steven J. Frucht, Giulietta M. Riboldi, Bin Zhang, Ana C. Pereira, and John F. Crary. Single-cell transcriptomic and neuropathologic analysis reveals dysregulation of the integrated stress response in progressive supranuclear palsy. Acta Neuropathologica, Dec 2024. URL: https://doi.org/10.1007/s00401-024-02823-w, doi:10.1007/s00401-024-02823-w. This article has 15 citations and is from a highest quality peer-reviewed journal.

20. (farrell2024genetictranscriptomichistological pages 4-7): Kurt Farrell, Jack Humphrey, Timothy Chang, Yi Zhao, Yuk Yee Leung, Pavel P Kuksa, Vishakha Patil, Wan-Ping Lee, Amanda B. Kuzma, Otto Valladares, Laura B. Cantwell, Hui Wang, Ashvin Ravi, Claudia De Sanctis, Natalia Han, Thomas D. Christie, Kristen Whitney, Margaret M. Krassner, Hadley Walsh, SoongHo Kim, Diana Dangoor, Megan A. Iida, Alicia Casella, Ruth H. Walker, Melissa J. Nirenberg, Alan E. Renton, Bergan Babrowicz, Giovanni Coppola, Towfique Raj, Günter U. Höglinger, Lawrence I. Golbe, Huw R. Morris, John Hardy, Tamas Revesz, Tom T. Warner, Zane Jaunmuktane, Kin Y. Mok, Rosa Rademakers, Dennis W. Dickson, Owen A. Ross, Li-San Wang, Alison Goate, Gerard Schellenberg, Daniel H. Geschwind, John F. Crary, and Adam Naj. Genetic, transcriptomic, histological, and biochemical analysis of progressive supranuclear palsy implicates glial activation and novel risk genes. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.11.09.565552, doi:10.1101/2023.11.09.565552. This article has 58 citations.

21. (jang2024biomarkerdiscoveryin pages 1-2): Yura Jang, Sungtaek Oh, Anna J. Hall, Zhen Zhang, Thomas F. Tropea, Alice Chen-Plotkin, Liana S. Rosenthal, Ted M. Dawson, Chan Hyun Na, and Alexander Y. Pantelyat. Biomarker discovery in progressive supranuclear palsy from human cerebrospinal fluid. Clinical Proteomics, Sep 2024. URL: https://doi.org/10.1186/s12014-024-09507-3, doi:10.1186/s12014-024-09507-3. This article has 9 citations and is from a peer-reviewed journal.

22. (boxer2017advancesinprogressive pages 1-2): Adam L Boxer, Jin-Tai Yu, Lawrence I Golbe, Irene Litvan, Anthony E Lang, and Günter U Höglinger. Advances in progressive supranuclear palsy: new diagnostic criteria, biomarkers, and therapeutic approaches. Jul 2017. URL: https://doi.org/10.1016/s1474-4422(17)30157-6, doi:10.1016/s1474-4422(17)30157-6. This article has 515 citations and is from a highest quality peer-reviewed journal.

23. (cristiani2024serumtauspecies pages 1-2): Costanza Maria Cristiani, Luana Scaramuzzino, Elvira Immacolata Parrotta, Giovanni Cuda, Aldo Quattrone, and Andrea Quattrone. Serum tau species in progressive supranuclear palsy: a pilot study. Diagnostics, 14:2746, Dec 2024. URL: https://doi.org/10.3390/diagnostics14232746, doi:10.3390/diagnostics14232746. This article has 2 citations.

24. (dilcher2024linkingpi2620taupet pages 1-5): Roxane Dilcher, Charles B. Malpas, William T. O’Brien, Stuart J. McDonald, Craig Despott, Kelly Bertram, Matthew P. Pase, Meng Law, Terence J. O’Brien, and Lucy Vivash. Linking pi-2620 tau-pet, fluid biomarkers, mri, and cognition to advance diagnostics for progressive supranuclear palsy. MedRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.14.24315486, doi:10.1101/2024.10.14.24315486. This article has 2 citations.

25. (boxer2017advancesinprogressive pages 4-5): Adam L Boxer, Jin-Tai Yu, Lawrence I Golbe, Irene Litvan, Anthony E Lang, and Günter U Höglinger. Advances in progressive supranuclear palsy: new diagnostic criteria, biomarkers, and therapeutic approaches. Jul 2017. URL: https://doi.org/10.1016/s1474-4422(17)30157-6, doi:10.1016/s1474-4422(17)30157-6. This article has 515 citations and is from a highest quality peer-reviewed journal.

26. (hoglinger2021safetyandefficacy pages 1-2): Günter U Höglinger, Irene Litvan, Nuno Mendonca, Deli Wang, Hui Zheng, Beatrice Rendenbach-Mueller, Hoi-Kei Lon, Ziyi Jin, Nahome Fisseha, Kumar Budur, Michael Gold, Davis Ryman, Hana Florian, Anwar Ahmed, Ikuko Aiba, Alberto Albanese, Kelly Bertram, Yvette Bordelon, James Bower, Jared Brosch, Daniel Claassen, Carlo Colosimo, Jean-Christophe Corvol, Paola Cudia, Antonio Daniele, Luc Defebvre, Erika Driver-Dunckley, Antoine Duquette, Roberto Eleopra, Alexandre Eusebio, Victor Fung, David Geldmacher, Lawrence Golbe, Francisco Grandas, Deborah Hall, Taku Hatano, Günter U Höglinger, Lawrence Honig, Jennifer Hui, Diana Kerwin, Akio Kikuchi, Thomas Kimber, Takashi Kimura, Rajeev Kumar, Irene Litvan, Peter Ljubenkov, Stefan Lorenzl, Albert Ludolph, Zoltan Mari, Nikolaus McFarland, Wassilios Meissner, Pablo Mir Rivera, Hidek Mochizuki, John Morgan, Renato Munhoz, Noriko Nishikawa, John O`Sullivan, Tomoko Oeda, Hideki Oizumi, Osamu Onodera, Fabienne Ory-Magne, Elizabeth Peckham, Ronald Postuma, Aldo Quattrone, Joseph Quinn, Stefano Ruggieri, Justyna Sarna, Paul E Schulz, John Slevin, Michele Tagliati, Daryl Wile, Zbigniew Wszolek, Tao Xie, and Theresa Zesiewicz. Safety and efficacy of tilavonemab in progressive supranuclear palsy: a phase 2, randomised, placebo-controlled trial. The Lancet Neurology, 20:182-192, Mar 2021. URL: https://doi.org/10.1016/s1474-4422(20)30489-0, doi:10.1016/s1474-4422(20)30489-0. This article has 171 citations and is from a highest quality peer-reviewed journal.

27. (hoglinger2021safetyandefficacy pages 6-7): Günter U Höglinger, Irene Litvan, Nuno Mendonca, Deli Wang, Hui Zheng, Beatrice Rendenbach-Mueller, Hoi-Kei Lon, Ziyi Jin, Nahome Fisseha, Kumar Budur, Michael Gold, Davis Ryman, Hana Florian, Anwar Ahmed, Ikuko Aiba, Alberto Albanese, Kelly Bertram, Yvette Bordelon, James Bower, Jared Brosch, Daniel Claassen, Carlo Colosimo, Jean-Christophe Corvol, Paola Cudia, Antonio Daniele, Luc Defebvre, Erika Driver-Dunckley, Antoine Duquette, Roberto Eleopra, Alexandre Eusebio, Victor Fung, David Geldmacher, Lawrence Golbe, Francisco Grandas, Deborah Hall, Taku Hatano, Günter U Höglinger, Lawrence Honig, Jennifer Hui, Diana Kerwin, Akio Kikuchi, Thomas Kimber, Takashi Kimura, Rajeev Kumar, Irene Litvan, Peter Ljubenkov, Stefan Lorenzl, Albert Ludolph, Zoltan Mari, Nikolaus McFarland, Wassilios Meissner, Pablo Mir Rivera, Hidek Mochizuki, John Morgan, Renato Munhoz, Noriko Nishikawa, John O`Sullivan, Tomoko Oeda, Hideki Oizumi, Osamu Onodera, Fabienne Ory-Magne, Elizabeth Peckham, Ronald Postuma, Aldo Quattrone, Joseph Quinn, Stefano Ruggieri, Justyna Sarna, Paul E Schulz, John Slevin, Michele Tagliati, Daryl Wile, Zbigniew Wszolek, Tao Xie, and Theresa Zesiewicz. Safety and efficacy of tilavonemab in progressive supranuclear palsy: a phase 2, randomised, placebo-controlled trial. The Lancet Neurology, 20:182-192, Mar 2021. URL: https://doi.org/10.1016/s1474-4422(20)30489-0, doi:10.1016/s1474-4422(20)30489-0. This article has 171 citations and is from a highest quality peer-reviewed journal.

28. (boxer2017advancesinprogressive pages 8-9): Adam L Boxer, Jin-Tai Yu, Lawrence I Golbe, Irene Litvan, Anthony E Lang, and Günter U Höglinger. Advances in progressive supranuclear palsy: new diagnostic criteria, biomarkers, and therapeutic approaches. Jul 2017. URL: https://doi.org/10.1016/s1474-4422(17)30157-6, doi:10.1016/s1474-4422(17)30157-6. This article has 515 citations and is from a highest quality peer-reviewed journal.

29. (barer2023progressivesupranuclearpalsy’s pages 4-5): Yael Barer, Raanan Cohen, Meital Grabarnik-John, Xiaolan Ye, Jorge Zamudio, Tanya Gurevich, and Gabriel Chodick. Progressive supranuclear palsy’s economical burden: the use and costs of healthcare resources in a large health provider in israel. Journal of Neurology, 270:3770-3778, Apr 2023. URL: https://doi.org/10.1007/s00415-023-11714-1, doi:10.1007/s00415-023-11714-1. This article has 2 citations and is from a domain leading peer-reviewed journal.

30. (bravo2024humanipsc4r pages 1-3): Celeste Parra Bravo, A. Giani, Jesus Madero Perez, Zeping Zhao, Yuansong Wan, Avi J. Samelson, M. Wong, Alessandro Evangelisti, Ethan Cordes, Li Fan, Pearly Ye, Daphne Zhu, Tatyana Pozner, Maria Mercedes, Tark Patel, Allan Yarahmady, G. Carling, Fredrik H. Sterky, Virginia M. Y. Lee, Edward B. Lee, M. DeTure, Dennis W. Dickson, Manu Sharma, S. Mok, Wenjie Luo, Mingrui Zhao, M. Kampmann, Shiaoching Gong, and Li Gan. Human ipsc 4r tauopathy model uncovers modifiers of tau propagation. Cell, 187:2446-2464.e22, Mar 2024. URL: https://doi.org/10.1016/j.cell.2024.03.015, doi:10.1016/j.cell.2024.03.015. This article has 76 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-02.md)
- [Edison artifact artifact-03](Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-03.md)
- [Edison artifact artifact-04](Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-04.md)
- [Edison artifact artifact-05](Progressive_Supranuclear_Palsy-deep-research-falcon_artifacts/artifact-05.md)