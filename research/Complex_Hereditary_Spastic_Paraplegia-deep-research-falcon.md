---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-01T20:34:35.059221'
end_time: '2026-07-01T20:52:05.577835'
duration_seconds: 1050.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Complex Hereditary Spastic Paraplegia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 68
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Complex_Hereditary_Spastic_Paraplegia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Complex_Hereditary_Spastic_Paraplegia-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Complex_Hereditary_Spastic_Paraplegia-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Complex Hereditary Spastic Paraplegia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Complex Hereditary Spastic Paraplegia** covering all of the
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
- **Disease Name:** Complex Hereditary Spastic Paraplegia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Complex Hereditary Spastic Paraplegia** covering all of the
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


# Comprehensive Research Report: Complex Hereditary Spastic Paraplegia

## 1. Disease Information

### Overview
Complex hereditary spastic paraplegia (complex HSP, also termed "complicated HSP") is a heterogeneous group of rare, inherited neurodegenerative disorders characterized by progressive lower-limb spasticity due to corticospinal tract degeneration, combined with additional neurological and non-neurological manifestations that distinguish it from "pure" or "uncomplicated" HSP (meyyazhagan2022thepuzzleof pages 1-2, meyyazhagan2022hereditaryspasticparaplegia pages 1-2). These additional features may include intellectual disability, seizures, dementia, cerebellar ataxia, peripheral neuropathy, optic atrophy, dysarthria, extrapyramidal disturbances, and skeletal deformities (meyyazhagan2022hereditaryspasticparaplegia pages 1-2). Complex HSP represents approximately 55% of HSP cases in some cohorts, highlighting its significant contribution to the overall HSP spectrum (amprosi2026naturalhistoryin pages 1-2).

### Key Identifiers
- **MONDO ID:** MONDO:0015150 (complex hereditary spastic paraplegia) (OpenTargets Search: hereditary spastic paraplegia)
- **MONDO ID (parent):** MONDO:0019064 (hereditary spastic paraplegia)
- **Orphanet:** ORPHA:100987 (complex hereditary spastic paraplegia)
- **ICD-10:** G11.4 (Hereditary spastic paraplegia)
- **ICD-11:** 8A60.1
- **MeSH:** D015419 (Spastic Paraplegia, Hereditary)

### Synonyms
Common synonyms include: complicated hereditary spastic paraplegia, complex HSP, complicated spastic paraplegia, HSP-plus, and complicated familial spastic paraplegia (meyyazhagan2022thepuzzleof pages 1-2, yu2023clinicalfeaturesand pages 1-2).

---

## 2. Etiology

### Disease Causal Factors
Complex HSP is caused primarily by monogenic mutations in genes affecting neuronal function, with over 90 genetic loci (designated SPG1–SPG83+) identified to date (meyyazhagan2022hereditaryspasticparaplegia pages 2-4, cipriano2025fluidbiomarkersin pages 1-2). The disorder is exclusively genetic in origin, with mutations in approximately 80 genes affecting diverse biochemical pathways including lipid droplet formation, endoplasmic reticulum (ER) shaping, axonal transport, endosome trafficking, and mitochondrial function (meyyazhagan2022thepuzzleof pages 1-2).

### Genetic Risk Factors
Complex forms of HSP are most commonly autosomal recessive (AR), in contrast to pure HSP which is more often autosomal dominant (AD) (fereshtehnejad2023movementdisordersin pages 4-5). In a systematic review and meta-analysis of 1,413 HSP cases with movement disorders, AR inheritance was present in 58.4% and AD in 31.4% (fereshtehnejad2023movementdisordersin pages 4-5). Consanguinity is a major risk factor, particularly for AR forms such as SPG11, where consanguinity odds ratio was 4.1 compared to SPG7 (fereshtehnejad2023movementdisordersin pages 5-6). In the MENA region, SPG11 (19.8%), FA2H (8.5%), and ZFYVE26 (7.7%) were the most frequently identified genes, with AR HSP with thin corpus callosum being common (meyyazhagan2022thepuzzleof pages 1-2).

### Environmental and Gene-Environment Interactions
Complex HSP is fundamentally a genetic disorder, and no specific environmental risk factors have been established as causal. However, environmental modifiers and gene-environment interactions remain poorly characterized. Lifestyle factors such as physical activity level may influence symptom severity and functional decline, but specific data are lacking.

---

## 3. Phenotypes

The following table summarizes the major phenotypic features of complex HSP with associated frequencies and HPO terms:

| Phenotype/Feature | Frequency (%) | HPO Term | Severity | Notes |
|---|---:|---|---|---|
| Lower limb spasticity | ~98% | HP:0001257 Spasticity; HP:0002061 Lower limb spasticity | Core; often progressive | Hallmark feature of complex HSP; in SPG15, lower-limb spasticity/pyramidal signs were nearly universal and typically progressed from distal to proximal involvement (saffari2023theclinicaland pages 3-5, saffari2023theclinicaland pages 1-2) |
| Cognitive impairment / decline | ~89%; progressive decline ~69% | HP:0100543 Cognitive impairment; HP:0001268 Mental deterioration | Moderate-severe; progressive in many | Common in SPG15 and other complex forms; may include learning disability and later decline (saffari2023theclinicaland pages 3-5, saffari2023theclinicaland pages 1-2) |
| Thin corpus callosum | ~100% in SPG15 cohort; classic for SPG11/SPG15 | HP:0002079 Thin corpus callosum | Imaging marker; often prominent | Highly characteristic neuroimaging feature of SPG15 and a major clue in SPG11/SPG15 diagnosis (saffari2023theclinicaland pages 3-5, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4) |
| Cerebellar ataxia | ~64% | HP:0001251 Ataxia | Moderate-severe | Common extrapyramidal/cerebellar manifestation in SPG15 and many complex genotypes (saffari2023theclinicaland pages 1-2, fereshtehnejad2023movementdisordersin pages 5-6) |
| Dysarthria | ~68% | HP:0001260 Dysarthria | Mild-moderate; progressive | Often accompanies cerebellar dysfunction and contributes to disability (saffari2023theclinicaland pages 3-5, saffari2023theclinicaland pages 6-8) |
| Developmental delay | ~68% | HP:0001263 Global developmental delay | Variable; often early-onset | Often precedes overt motor syndrome by years in early-onset complex HSP such as SPG15 and AP-4 deficiency disorders (saffari2023theclinicaland pages 3-5, saffari2023theclinicaland pages 1-2) |
| Peripheral neuropathy / polyneuropathy | ~38% | HP:0009830 Peripheral neuropathy | Variable | More frequent in some genotypes such as SPG11; nerve conduction studies may show sensorimotor polyneuropathy (saffari2023theclinicaland pages 3-5, fereshtehnejad2023movementdisordersin pages 5-6, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4) |
| Epilepsy / seizures | ~18% in pediatric complex HSP cohort; variable by genotype | HP:0001250 Seizure | Variable; can be severe | Seen in pediatric complex HSP and AP-4 deficiency/SPG50; not universal across all complex HSPs (ikeda2023geneticandclinical pages 3-4, awuah2024hereditaryspasticparaplegia pages 8-10) |
| Dystonia | ~11% | HP:0001332 Dystonia | Variable | Recognized movement-disorder component of complex HSP, especially selected genotypes (saffari2023theclinicaland pages 1-2, fereshtehnejad2023movementdisordersin pages 5-6) |
| Parkinsonism | ~16% | HP:0001300 Parkinsonism | Variable; usually minority feature | Reported in a subset of SPG15 and particularly enriched in some SPG11-related phenotypes (saffari2023theclinicaland pages 1-2, fereshtehnejad2023movementdisordersin pages 5-6) |
| Urinary dysfunction / neurogenic bladder | ~54% | HP:0000009 Functional urinary incontinence; HP:0000013 Hypoplasia of the bladder not appropriate; prefer HP:0000508 Neurogenic bladder | Moderate; progressive in many | Includes urgency/incontinence; common non-motor burden in complex HSP (saffari2023theclinicaland pages 3-5, saffari2023theclinicaland pages 1-2) |
| Upper limb spasticity | ~64% | HP:0001258 Spasticity of upper limbs | Moderate | Reflects spread beyond lower-limb-predominant syndrome in more advanced/complex disease (saffari2023theclinicaland pages 1-2, saffari2023theclinicaland pages 3-5) |
| Intellectual disability | ~76% in pediatric-onset complex HSP | HP:0001249 Intellectual disability | Moderate-severe | Particularly common in pediatric complex HSP cohorts and AP-4 deficiency disorders (ikeda2023geneticandclinical pages 3-4, dowling2024aavgenetherapy pages 1-2) |
| Scoliosis | ~21% | HP:0002650 Scoliosis | Mild-moderate | Orthopedic complication seen in complex HSP cohorts such as SPG15 (saffari2023theclinicaland pages 3-5) |
| Foot deformity | ~28% | HP:0001760 Pes planus / HP:0001761 Pes cavus / HP:0001824 Foot deformity | Mild-moderate | Deformities vary; relevant to gait impairment and rehabilitation planning (saffari2023theclinicaland pages 3-5) |
| Visual abnormalities / optic pathway involvement | Variable | HP:0000505 Visual impairment; HP:0000648 Optic atrophy | Variable | Optic atrophy/retinal abnormalities occur in some complex HSP forms; visual findings are genotype-dependent rather than universal (meyyazhagan2022hereditaryspasticparaplegia pages 1-2, fereshtehnejad2023movementdisordersin pages 5-6) |


*Table: This table summarizes major clinical and imaging features reported in complex hereditary spastic paraplegia, emphasizing frequencies from recent cohorts—especially SPG15 and pediatric-onset complex HSP. It is useful for phenotype-driven diagnosis, ontology mapping, and genotype-phenotype curation.*

### Detailed Phenotypic Characteristics

**Age of Onset:** Complex HSP typically presents earlier than pure HSP. In a pediatric-onset Japanese cohort, the median age of onset for complex-type was 16 months (IQR 12–26 months) (ikeda2023geneticandclinical pages 3-4). For SPG15, symptom onset occurred at a median of 24 months with developmental symptoms preceding motor manifestations by several years (saffari2023theclinicaland pages 1-2, saffari2023theclinicaland pages 3-5). In adult-onset movement disorder cases, mean age of onset was 20.5 ± 16.0 years (fereshtehnejad2023movementdisordersin pages 4-5).

**Symptom Progression:** The disease is progressive, with spasticity initially affecting distal lower limbs before progressing proximally (saffari2023theclinicaland pages 1-2). In SPG15, loss of independent ambulation occurred at a mean age of 17 years, with wheelchair dependency developing by mean age 20 years (saffari2023theclinicaland pages 8-9). An Austrian natural history study demonstrated complicated HSP progresses faster than pure HSP (1.3 vs. 0.6 SPRS points/year; p < 0.001) (amprosi2026naturalhistoryin pages 1-2, amprosi2026naturalhistoryin pages 13-14).

**Quality of Life Impact:** Complex HSP significantly impairs quality of life, with modified Rankin Scale scores significantly higher in complex-type (3.5 ± 1.0) compared to pure-type HSP (2.1 ± 0.9; p < 0.001) (ikeda2023geneticandclinical pages 3-4). The progressive nature leads to walking cane or wheelchair dependence over time. In the Austrian cohort, 17.5% of patients were wheelchair-bound, while over 50% did not require assistive devices (amprosi2026naturalhistoryin pages 11-13). Although HSP does not typically reduce lifespan, it significantly impairs quality of life, particularly with more severe symptoms (awuah2024hereditaryspasticparaplegia pages 1-2). However, some complex forms such as SPG11 are associated with restricted life expectancy (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6).

---

## 4. Genetic/Molecular Information

### Causal Genes
The following table provides a comprehensive overview of the major genes associated with complex HSP:

| SPG designation / subtype | Gene | Protein | Typical inheritance | Key complex HSP clinical features | OMIM / phenotype note |
|---|---|---|---|---|---|
| SPG11 | **SPG11** | Spatacsin | AR | Early-onset progressive spastic paraplegia, thin corpus callosum, cognitive decline/intellectual disability, peripheral neuropathy, dysarthria, bladder dysfunction, ataxia/parkinsonism in some patients (vijayaraghavan2025roleofglial pages 2-3, meyyazhagan2022hereditaryspasticparaplegia pages 12-14, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 7-8, saffari2023theclinicaland pages 3-5) | Phenotype OMIM not established here from retrieved evidence; gene-disease association strongly supported (OpenTargets Search: hereditary spastic paraplegia, vijayaraghavan2025roleofglial pages 2-3) |
| SPG15 | **ZFYVE26** | Spastizin | AR | Early-childhood developmental delay, adolescent-onset progressive lower-limb spasticity, thin corpus callosum, “ears of the lynx” MRI sign, ataxia, dysarthria, cognitive decline, urinary dysfunction, peripheral neuropathy, dystonia/parkinsonism subset (saffari2023theclinicaland pages 1-2, saffari2023theclinicaland pages 6-8, saffari2023theclinicaland pages 3-5) | Phenotype OMIM not established here from retrieved evidence; gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG7 | **SPG7** | Paraplegin | AR (occasionally AD/digenic reported in broader literature, not established here) | Adult-onset or variable-onset spastic paraplegia, frequent cerebellar ataxia, optic/extraocular movement abnormalities, seizures or movement disorder features in some patients (meyyazhagan2022thepuzzleof pages 1-2, fereshtehnejad2023movementdisordersin pages 5-6) | Gene-disease association supported in Open Targets (OpenTargets Search: hereditary spastic paraplegia) |
| SPG20 | **SPART** | Spartin | AR | Complex HSP/Troyer syndrome phenotype with spastic paraplegia plus distal amyotrophy, dysarthria, developmental/cognitive involvement; lipid droplet turnover implicated (vijayaraghavan2025roleofglial pages 2-3) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG21 | **SPG21** | Maspardin | AR | Complex spastic paraplegia with cognitive impairment, extrapyramidal features, thin corpus callosum reported in broader HSP spectrum; intracellular trafficking defect (vijayaraghavan2025roleofglial pages 2-3, meyyazhagan2022hereditaryspasticparaplegia pages 12-14) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG35 | **FA2H** | Fatty acid 2-hydroxylase | AR | Complex HSP with spasticity, leukodystrophy/myelin involvement, dystonia/ataxia and cognitive features in some cases; myelin lipid synthesis defect (vijayaraghavan2025roleofglial pages 2-3, meyyazhagan2022hereditaryspasticparaplegia pages 12-14) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG39 | **PNPLA6** | Neuropathy target esterase / patatin-like phospholipase domain-containing protein 6 | AR | Complex HSP with spastic paraplegia plus ataxia, neuropathy, retinal/visual and endocrine/cognitive features across PNPLA6 spectrum; lipid regulation defect (vijayaraghavan2025roleofglial pages 2-3, fereshtehnejad2023movementdisordersin pages 5-6) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG47 | **AP4B1** | Adaptor related protein complex 4 subunit beta 1 | AR | Childhood-onset AP-4 deficiency syndrome with spastic paraplegia, global developmental delay, intellectual disability, epilepsy; preclinical gene replacement therapy in development (awuah2024hereditaryspasticparaplegia pages 8-10, wiseman2024preclinicaldevelopmentof pages 13-15) | Phenotype OMIM not established here from retrieved evidence |
| SPG50 | **AP4M1** | Adaptor related protein complex 4 subunit mu 1 | AR | Childhood-onset complex HSP with progressive spastic paraplegia, developmental delay, intellectual disability, secondary microcephaly, epilepsy; target of first individualized AAV therapy (dowling2024aavgenetherapy pages 1-2, chen2023intrathecalaav9ap4m1gene pages 1-2) | Phenotype OMIM not established here from retrieved evidence |
| SPG51 | **AP4E1** | Adaptor related protein complex 4 subunit epsilon 1 | AR | AP-4 deficiency syndrome with severe developmental delay, intellectual disability, early hypotonia evolving to spastic paraplegia, epilepsy (awuah2024hereditaryspasticparaplegia pages 8-10, wiseman2024preclinicaldevelopmentof pages 13-15) | Phenotype OMIM not established here from retrieved evidence |
| SPG52 | **AP4S1** | Adaptor related protein complex 4 subunit sigma 1 | AR | AP-4 deficiency syndrome with developmental delay, severe intellectual disability, childhood-onset complex spastic paraplegia, epilepsy (awuah2024hereditaryspasticparaplegia pages 8-10, wiseman2024preclinicaldevelopmentof pages 13-15) | Phenotype OMIM not established here from retrieved evidence |
| SPG1 | **L1CAM** | L1 cell adhesion molecule | X-linked | Complex spastic paraplegia with intellectual disability, hydrocephalus/corpus callosum abnormalities and other L1 syndrome manifestations; axon guidance/myelination effects (meyyazhagan2022hereditaryspasticparaplegia pages 12-14, awuah2024hereditaryspasticparaplegia pages 8-10) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG2 | **PLP1** | Proteolipid protein 1 | X-linked | Spastic paraplegia with dysmyelination spectrum, variable cognitive/visual features; abnormal myelin maintenance central to disease (vijayaraghavan2025roleofglial pages 2-3, awuah2024hereditaryspasticparaplegia pages 8-10) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG30 / KIF1A-associated HSP | **KIF1A** | Kinesin family member 1A | AD or AR depending on variant/context | Pediatric complex HSP with spastic paraplegia, developmental delay/intellectual disability, cerebellar signs, optic atrophy/neuropathy in some patients; common pediatric complex HSP gene (OpenTargets Search: hereditary spastic paraplegia, ikeda2023geneticandclinical pages 3-4) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG18 | **ERLIN2** | ER lipid raft associated 2 | AR | Early-onset complicated HSP with spasticity, intellectual disability, joint contractures or seizures reported in spectrum; ER-associated pathway defect (OpenTargets Search: hereditary spastic paraplegia) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG26 | **B4GALNT1** | Beta-1,4-N-acetyl-galactosaminyltransferase 1 | AR | Complex HSP with spasticity, cognitive impairment, cerebellar signs/neuropathy in reported spectrum; ganglioside biosynthesis defect (OpenTargets Search: hereditary spastic paraplegia) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG5A | **CYP7B1** | Cytochrome P450 7B1 | AR | Often pure HSP, but complicated cases can include ataxia/neuropathy; notable because disease-specific biochemical biomarkers (oxysterols) exist (meyyazhagan2022hereditaryspasticparaplegia pages 12-14, meyyazhagan2022thepuzzleof pages 11-12, cipriano2025fluidbiomarkersin pages 1-2) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG42 | **SLC33A1** | Acetyl-CoA transporter 1 | AD | Spastic paraplegia with variable complex manifestations; listed among established HSP genes (meyyazhagan2022hereditaryspasticparaplegia pages 4-6, meyyazhagan2022hereditaryspasticparaplegia pages 20-21) | Open Targets association noted for SPG4 locus-related data; phenotype details limited here (OpenTargets Search: hereditary spastic paraplegia) |
| SPG31 | **REEP1** | Receptor expression-enhancing protein 1 | AD | Usually pure HSP, but complicated phenotypes with neuropathy can occur; ER shaping defect shared with major HSP mechanisms (meyyazhagan2022thepuzzleof pages 1-2, meyyazhagan2022hereditaryspasticparaplegia pages 4-6, meyyazhagan2022hereditaryspasticparaplegia pages 14-16) | Established HSP gene; phenotype details from retrieved evidence are limited |
| SPG3A | **ATL1** | Atlastin-1 | AD | Usually early-onset pure HSP, but part of core mechanistic ER-network genes and occasional complex presentations reported (meyyazhagan2022thepuzzleof pages 1-2, meyyazhagan2022hereditaryspasticparaplegia pages 12-14, meyyazhagan2022hereditaryspasticparaplegia pages 14-16) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| SPG4 | **SPAST** | Spastin | AD | Most common AD HSP; generally pure but complex phenotypes exist, especially pediatric or severe cases; microtubule-severing/axonal transport defect (meyyazhagan2022thepuzzleof pages 1-2, meyyazhagan2022hereditaryspasticparaplegia pages 12-14, meyyazhagan2022thepuzzleof pages 12-14) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| Novel AR HSP (no SPG number specified here) | **AMFR** | Autocrine motility factor receptor / gp78 | AR | Pure or complex HSP with developmental delay, mild intellectual disability, progressive spasticity; lipid droplet accumulation and ER morphology defects in preclinical models (garg2024divingdeepzebrafish pages 5-6) | Newly described AR-HSP gene in retrieved evidence; OMIM phenotype not established here |
| Complex HSP spectrum | **ALDH18A1** | Delta-1-pyrroline-5-carboxylate synthase | AD or AR | Spastic paraplegia with variable developmental/cognitive and neuropathy features across inheritance contexts (OpenTargets Search: hereditary spastic paraplegia) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |
| Complex HSP spectrum | **ATP13A2** | Lysosomal P5-type ATPase | AR | Complex HSP with parkinsonism/cognitive features and lysosomal-autophagic dysfunction in some patients (OpenTargets Search: hereditary spastic paraplegia, awuah2024hereditaryspasticparaplegia pages 8-10) | Gene-disease association supported (OpenTargets Search: hereditary spastic paraplegia) |


*Table: This table summarizes the major genes implicated in complex hereditary spastic paraplegia, highlighting inheritance, encoded proteins, and distinguishing clinical features. It is useful for comparing the most important SPG subtypes and related complex HSP genes across the heterogeneous disease spectrum.*

### Most Common Genetic Subtypes
In AD HSP (80% of North American and Northern European populations), SPG4/SPAST accounts for 40% of cases, SPG3A/ATL1 for 10%, SPG31/REEP1 for 10%, and SPG10/KIF5A for 3% (meyyazhagan2022hereditaryspasticparaplegia pages 12-14). Among AR forms, SPG11 and SPG15 are the most significant complex HSP subtypes, along with SPG35/FA2H, SPG45/C19orf12, and SPG7 (5–12% of AR cases) (meyyazhagan2022hereditaryspasticparaplegia pages 12-14). In a Chinese cohort, SPAST was the most common gene, followed by SPG11 and ATL1 (yu2023clinicalfeaturesand pages 1-2). In pediatric complex HSP, KIF1A variants were the most common cause (ikeda2023geneticandclinical pages 3-4).

### Pathogenic Variants
Pathogenic variants span multiple types including missense, frameshift, nonsense, splice-site, and structural variants (large deletions/duplications) (meyyazhagan2022hereditaryspasticparaplegia pages 4-6, meyyazhagan2022thepuzzleof pages 5-6). For SPG15, 45 distinct ZFYVE26 variants have been described, distributed across the protein structure without mutational hotspots (saffari2023theclinicaland pages 1-2). SPG4 variants include both point mutations and exon deletions detectable by MLPA (meyyazhagan2022thepuzzleof pages 5-6). Variant classification follows ACMG-AMP 2015 guidelines (saffari2023theclinicaland pages 13-13). All variants are germline in origin.

### Inheritance Patterns
Complex HSP follows all major Mendelian inheritance patterns: autosomal recessive (most common for complex forms), autosomal dominant, X-linked recessive (SPG1/L1CAM, SPG2/PLP1), and mitochondrial inheritance (meyyazhagan2022hereditaryspasticparaplegia pages 2-4, meyyazhagan2022hereditaryspasticparaplegia pages 12-14). Variable expressivity is characteristic, and penetrance varies by gene and variant.

---

## 5. Environmental Information

Complex HSP is not associated with established environmental risk factors, infectious agents, or specific lifestyle factors as causative agents. The disease is exclusively genetic in etiology. No gene-environment interactions have been validated, though physical activity and rehabilitation may influence functional outcomes.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways
The pathophysiology of complex HSP involves disruption of multiple interconnected cellular pathways (awuah2024hereditaryspasticparaplegia pages 1-2, meyyazhagan2022hereditaryspasticparaplegia pages 14-16):

**Endoplasmic Reticulum Morphogenesis and Membrane Trafficking:** Mutations in ER-associated proteins (spastin/SPG4, atlastin/SPG3A, REEP1/SPG31) disrupt ER tubular network formation and ER-microtubule relationships, which are critical for axonal maintenance (meyyazhagan2022hereditaryspasticparaplegia pages 14-16, meyyazhagan2022thepuzzleof pages 2-5). GO terms: GO:0030176 (ER tubular network organization); GO:0016197 (endosome transport).

**Autophagy-Lysosomal Pathway:** Spatacsin (SPG11) and spastizin (SPG15/ZFYVE26) are essential for autophagic lysosome reformation. Their dysfunction leads to impaired autophagosome-lysosome fusion and accumulation of lysosomal structures (awuah2024hereditaryspasticparaplegia pages 8-10, vijayaraghavan2025roleofglial pages 2-3). AP-4 complex mutations (SPG47, SPG50, SPG51, SPG52) cause mislocation of ATG9A, a key autophagy protein (wiseman2024preclinicaldevelopmentof pages 13-15). GO terms: GO:0006914 (autophagy); GO:0005764 (lysosome).

**Mitochondrial Dysfunction:** Loss of paraplegin/AFG3L2 complex impairs ATP production and increases vulnerability to reactive oxygen species (awuah2024hereditaryspasticparaplegia pages 2-4). Disrupted mitochondrial fission-fusion dynamics causes impaired axonal transport, oxidative phosphorylation deficiencies, and axonal degeneration (awuah2024hereditaryspasticparaplegia pages 2-4, meyyazhagan2022thepuzzleof pages 12-14). GO terms: GO:0005739 (mitochondrion); GO:0006119 (oxidative phosphorylation).

**Lipid Metabolism:** Defects in lipid droplet formation, cholesterol metabolism (CYP7B1/SPG5), fatty acid hydroxylation (FA2H/SPG35), and phospholipid regulation (PNPLA6/SPG39) compromise neuronal membrane integrity and myelin maintenance (meyyazhagan2022thepuzzleof pages 1-2, vijayaraghavan2025roleofglial pages 2-3, meyyazhagan2022thepuzzleof pages 11-12). AMFR mutations cause lipid droplet accumulation in neural stem cells (garg2024divingdeepzebrafish pages 5-6). GO terms: GO:0006629 (lipid metabolic process); GO:0005811 (lipid droplet).

**Axonal Transport and Microtubule Dynamics:** Spastin (SPG4) is a microtubule-severing enzyme; its dysfunction causes microtubule disorganization and impaired axonal transport (meyyazhagan2022hereditaryspasticparaplegia pages 14-16, meyyazhagan2022thepuzzleof pages 12-14). KIF1A and KIF5A mutations directly affect kinesin-mediated axonal transport (garg2024divingdeepzebrafish pages 5-6). GO terms: GO:0007018 (microtubule-based movement); GO:0008088 (axo-dendritic transport).

**Myelination Abnormalities:** PLP1 (SPG2) mutations and L1CAM (SPG1) mutations reduce myelin protein expression and impair oligodendrocyte function, limiting myelin maintenance of corticospinal neurons (awuah2024hereditaryspasticparaplegia pages 8-10). GO terms: GO:0042552 (myelination).

### Glial Cell Involvement
Recent research has revealed a non-cell-autonomous mechanism in HSP, with impaired lipid metabolism and reduced lipid droplets in HSP astrocytes contributing to axonal degeneration of cortical neurons (vijayaraghavan2025roleofglial pages 2-3). Reactive astrocytes produce both cytotoxic molecules (LCN2, IL-1β, TNF-α, nitric oxide) and neuroprotective factors (BDNF, NGF), while increased microgliosis and pro-inflammatory factors have been observed in HSP patient samples (vijayaraghavan2025roleofglial pages 2-3). CL terms: CL:0000127 (astrocyte); CL:0000129 (microglial cell); CL:0000540 (neuron).

### Causal Chain
The primary trigger is a germline genetic mutation → protein loss-of-function or dysfunction → disruption of one or more core cellular pathways (ER morphogenesis, autophagy, mitochondrial function, lipid metabolism, axonal transport) → selective vulnerability of long corticospinal tract axons due to their high metabolic demands → progressive axonal degeneration → neuronal dysfunction and cell death → clinical manifestation of progressive spasticity and additional neurological features (awuah2024hereditaryspasticparaplegia pages 1-2, meyyazhagan2022thepuzzleof pages 2-5).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** Central nervous system, specifically the corticospinal tracts (lateral columns of thoracic and cervical spinal cord) (UBERON:0002187)
- **Secondary:** Cerebellum (UBERON:0002037), cerebral cortex (UBERON:0000956), corpus callosum (UBERON:0002336), peripheral nerves (UBERON:0001021)
- **Body systems:** Nervous system (motor and sensory), musculoskeletal system, urinary system

### Tissue and Cell Level
- **Tissues:** White matter tracts (corticospinal tracts, posterior columns), cerebral and cerebellar white matter, myelin
- **Cell types:** Upper motor neurons (CL:0000540), corticospinal projection neurons, oligodendrocytes (CL:0000128), astrocytes (CL:0000127), microglial cells (CL:0000129)
- **Subcellular:** Endoplasmic reticulum (GO:0005783), mitochondria (GO:0005739), lysosomes (GO:0005764), autophagosomes (GO:0005776), microtubules (GO:0005874), lipid droplets (GO:0005811)

### Localization
Neurodegeneration is bilateral and symmetric, with greatest severity in the lumbar and thoracic spinal cord regions affecting the longest descending axons (vijayaraghavan2025roleofglial pages 2-3).

---

## 8. Temporal Development

### Onset
Complex HSP typically has an earlier onset than pure HSP. In pediatric cohorts, median onset is 16–24 months (ikeda2023geneticandclinical pages 3-4, saffari2023theclinicaland pages 1-2). Onset patterns include congenital/neonatal, infantile, childhood, adolescent, and adult, with some subtypes (SPG7) presenting predominantly in adulthood (fereshtehnejad2023movementdisordersin pages 5-6). Onset is typically insidious and chronic.

### Progression
Disease progression is chronic and progressive. Mean annual SPRS progression is 0.9 points overall, with complicated HSP progressing at 1.3 points/year vs. 0.6 points/year for pure HSP (amprosi2026naturalhistoryin pages 1-2, amprosi2026naturalhistoryin pages 13-14). For SPG15, wheelchair dependency develops by a mean age of 20 years (saffari2023theclinicaland pages 8-9). The disease course is progressive without remission; gait impairment, cognitive decline, and autonomic dysfunction worsen over time (saffari2023theclinicaland pages 1-2, saffari2023theclinicaland pages 8-9). Significant diagnostic delay exists (median 14.4 years in SPG15) (saffari2023theclinicaland pages 3-5).

---

## 9. Inheritance and Population

### Epidemiology
Global HSP prevalence ranges from 0.1 to 9.6 per 100,000, with most estimates between 1 and 5 per 100,000 (meyyazhagan2022thepuzzleof pages 1-2, yu2023clinicalfeaturesand pages 1-2, meyyazhagan2022hereditaryspasticparaplegia pages 1-2). Prevalence varies by geographic region, with higher rates reported in some European populations.

### Inheritance Patterns
- Autosomal dominant: ~75–80% of registered HSP cases in Northern Europe and North America (predominantly pure forms) (meyyazhagan2022hereditaryspasticparaplegia pages 2-4, meyyazhagan2022hereditaryspasticparaplegia pages 12-14)
- Autosomal recessive: Most complex HSP forms; predominant in consanguineous populations (meyyazhagan2022hereditaryspasticparaplegia pages 12-14, fereshtehnejad2023movementdisordersin pages 4-5)
- X-linked recessive: SPG1 (L1CAM), SPG2 (PLP1) (meyyazhagan2022hereditaryspasticparaplegia pages 12-14)
- Mitochondrial: Rare forms (meyyazhagan2022hereditaryspasticparaplegia pages 2-4)

### Population Demographics
AR complex HSP is more common in populations with high rates of consanguinity, such as the MENA region (meyyazhagan2022thepuzzleof pages 1-2). The male:female ratio in one Austrian cohort was approximately 64.3% male (amprosi2026naturalhistoryin pages 1-2). Approximately 40% of HSP cases present as sporadic forms without family history (meyyazhagan2022hereditaryspasticparaplegia pages 1-2).

### Founder Effects
Specific variants show geographic clustering; SPG11 is the most common AR HSP gene in Iran and Tunisia (meyyazhagan2022thepuzzleof pages 1-2). Genetic diversity and distinct variant spectra have been reported in African, Asian, and European populations (meyyazhagan2022hereditaryspasticparaplegia pages 12-14).

---

## 10. Diagnostics

### Clinical Tests
- **Laboratory tests:** Routine blood tests, serum homocysteine analysis; oxysterol levels (25- and 27-hydroxycholesterol) for SPG5 (chen2022geneticoriginof pages 1-2, meyyazhagan2022thepuzzleof pages 11-12)
- **Electrophysiology:** Nerve conduction studies and EMG (revealing sensorimotor polyneuropathy in some forms), somatosensory evoked potentials (chen2022geneticoriginof pages 1-2, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4)
- **Neuroimaging:** Brain MRI showing thin corpus callosum (hallmark of SPG11/SPG15), periventricular white matter changes, "ears of the lynx" sign (T2-FLAIR hyperintensity in forceps minor), cerebellar and cortical atrophy (saffari2023theclinicaland pages 3-5, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4, chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6). Spinal cord MRI may show thinning (meyyazhagan2022thepuzzleof pages 5-6).
- **Biomarkers:** Neurofilament light chain (NfL) in plasma and CSF shows significant elevation in HSP patients and correlates inversely with age in SPG15 (saffari2023theclinicaland pages 1-2, cipriano2025fluidbiomarkersin pages 1-2, cipriano2025fluidbiomarkersin pages 12-14). GFAP, brain-derived tau, and sTREM2 are emerging biomarkers reflecting neurodegeneration and glial activation (cipriano2025fluidbiomarkersin pages 12-14).

### Genetic Testing
- **Recommended approach:** Next-generation sequencing (NGS) gene panels targeting HSP-associated genes, with MLPA for detection of exon deletions/duplications (especially for SPAST/SPG4) (meyyazhagan2022thepuzzleof pages 5-6)
- **Whole exome/genome sequencing:** Employed when targeted panels are uninformative or phenotype is atypical (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6)
- **Diagnostic yield:** 45% in pure-type and 81% in complex-type pediatric-onset HSP by comprehensive genetic testing (ikeda2023geneticandclinical pages 3-4); overall genetic diagnostic rate of 35–54% across cohorts (yu2023clinicalfeaturesand pages 1-2, amprosi2026naturalhistoryin pages 1-2)
- **Variant interpretation:** ACMG-AMP 2015 guidelines with tools such as VarSome and InterVar (saffari2023theclinicaland pages 13-13)

### Clinical Criteria
Diagnosis requires bilateral lower-limb spasticity with hyperreflexia and extensor plantar responses, without acquired causes, confirmed by at least two neurologists (chen2022geneticoriginof pages 1-2). Differential diagnosis includes cerebral palsy, ALS, leukodystrophy, hereditary ataxias, vitamin B12/copper deficiency, and arteriovenous fistulas (meyyazhagan2022thepuzzleof pages 5-6).

---

## 11. Outcome/Prognosis

### Survival and Morbidity
HSP generally does not reduce lifespan in pure forms, but complex forms—particularly SPG11—may be associated with restricted life expectancy (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6, awuah2024hereditaryspasticparaplegia pages 1-2). The primary morbidity is progressive disability: 17.5% of patients in one cohort were wheelchair-bound, and 33% of SPG15 patients were unable to walk independently (amprosi2026naturalhistoryin pages 11-13, saffari2023theclinicaland pages 3-5).

### Disease Severity Measures
Mean baseline SPRS score was 18.2 points in an Austrian cohort (consistent with European cohorts of 17.4–19.9) (amprosi2026naturalhistoryin pages 11-13). Complex HSP patients show higher SPRS scores (27.4 ± 8.9 vs. 16.7 ± 8.6 for pure HSP), indicating greater neurological impairment (siow2023outcomemeasuresand pages 2-3). In SPG15, mean SPRS was 25.2 ± 13.3 (saffari2023theclinicaland pages 6-8).

### Prognostic Factors
Earlier disease onset correlates with longer diagnostic delay and disease duration but is associated with a lower risk of independent ambulation loss (yu2023clinicalfeaturesand pages 1-2). Disease duration is the strongest predictor of SPRS progression (amprosi2026naturalhistoryin pages 13-14). NfL levels may serve as prognostic biomarkers, showing correlation with disease activity (cipriano2025fluidbiomarkersin pages 12-14).

---

## 12. Treatment

### Pharmacotherapy (MAXO:0000058 – pharmacotherapy)
- **Antispasticity agents:** Baclofen (oral and intrathecal), tizanidine, and oxybutynin (meyyazhagan2022hereditaryspasticparaplegia pages 16-18). Intrathecal baclofen (ITB) demonstrated sustained improvement in spasticity for 2–3 years followed by stable ambulatory function for 4–5 years (awuah2024hereditaryspasticparaplegia pages 12-13).
- **Botulinum toxin type A:** Multiple open-label studies demonstrate improvement in motor and non-motor symptoms, with improved gait velocity at follow-up (meyyazhagan2022hereditaryspasticparaplegia pages 25-25, meyyazhagan2022thepuzzleof pages 6-9). MAXO:0000087 (botulinum toxin injection).
- **Dalfampridine:** A potassium channel blocker explored in a pilot trial (NCT05613114) (meyyazhagan2022hereditaryspasticparaplegia pages 25-25).
- **Levodopa:** Explored for parkinsonism features, particularly in SPG7 and SPG11, though evidence remains limited (awuah2024hereditaryspasticparaplegia pages 12-13).

### Rehabilitation (MAXO:0000011 – physical therapy)
- **Physical therapy:** Core management approach including stretching, balance training, and strengthening exercises (meyyazhagan2022thepuzzleof pages 6-9)
- **Robot-assisted gait training:** Shows promise for improving gait velocity (meyyazhagan2022thepuzzleof pages 14-15)
- **Hydrotherapy and electrostimulation:** Potential to increase lower extremity strength and decrease spasticity (meyyazhagan2022thepuzzleof pages 14-15)
- **Ankle-foot orthoses:** For mobility improvement (meyyazhagan2022hereditaryspasticparaplegia pages 16-18)

### Advanced Therapeutics: Gene Therapy
A landmark single-patient phase 1 clinical trial of AAV gene therapy for SPG50 (AP4M1 gene replacement) was reported in 2024. An adeno-associated virus vector carrying the AP4M1 gene was administered intrathecally to a 4-year-old patient, showing good tolerability with no serious adverse events at 12 months and preliminary evidence of disease stabilization (dowling2024aavgenetherapy pages 1-2). Preclinical studies in Ap4m1-knockout mice demonstrated age- and dose-dependent therapeutic effects (chen2023intrathecalaav9ap4m1gene pages 1-2). Gene replacement therapy for SPG47 (AP4B1) has completed IND-enabling studies with acceptable safety profiles in nonhuman primates (wiseman2024preclinicaldevelopmentof pages 13-15). Additional experimental approaches include spastin recovery through preventing neddylation-dependent degradation, and mRNA-based therapies for SPG5 (awuah2024hereditaryspasticparaplegia pages 20-20).

### Surgical Interventions (MAXO:0000004 – surgical procedure)
- **Selective dorsal rhizotomy:** Explored in children with limited evidence (meyyazhagan2022thepuzzleof pages 6-9)
- **Spinal cord stimulation:** Under investigation (NCT05196178)

### Neuromodulation
Repetitive transcranial magnetic stimulation and transcutaneous spinal direct current stimulation have been explored with mixed results (awuah2024hereditaryspasticparaplegia pages 20-20, awuah2024hereditaryspasticparaplegia pages 19-20).

### Clinical Trials
The following table summarizes active and recent clinical trials in HSP:

| NCT Number | Trial Title/Focus | Status | Phase | Type | Enrollment | Sponsor |
|---|---|---|---|---|---:|---|
| NCT03981276 | Phenotypes, Biomarkers and Pathophysiology in Hereditary Spastic Paraplegias and Related Disorders | Recruiting | Not provided | Observational | 2000 | University Hospital Tuebingen (OpenTargets Search: hereditary spastic paraplegia) |
| NCT04712812 | Registry and Natural History Study for Early Onset Hereditary Spastic Paraplegia | Recruiting | Not provided | Observational | 700 | Boston Children's Hospital (OpenTargets Search: hereditary spastic paraplegia) |
| NCT06553976 | Spastic Paraplegia - Centers of Excellence Research Network (SP-CERN) | Recruiting | Not provided | Observational | 100 | Boston Children's Hospital (OpenTargets Search: hereditary spastic paraplegia) |
| NCT05354622 | Hereditary Spastic Paraplegia Genomic Sequencing Initiative (HSPseq) | Recruiting | Not provided | Observational | 200 | Boston Children's Hospital (OpenTargets Search: hereditary spastic paraplegia) |
| NCT03961906 | Physiotherapy in Hereditary Spastic Paraplegia | Completed | Phase 2 | Interventional | 53 | University Hospital Tuebingen (OpenTargets Search: hereditary spastic paraplegia) |
| NCT04180098 | Improving Gait Adaptability in Hereditary Spastic Paraplegia | Completed | NA | Interventional | 36 | Radboud University Medical Center (OpenTargets Search: hereditary spastic paraplegia) |
| NCT05613114 | Effect of Dalfampridine in Patients With Hereditary Spastic Paraplegia | Completed | NA | Interventional | 8 | European University of Lefke (OpenTargets Search: hereditary spastic paraplegia) |
| NCT06068700 | AAV gene therapy for SPG50 | Phase 1 / not verified in retrieved trial list; related single-patient phase 1 study reported separately | Phase 1 | Interventional | Not provided | Not established from retrieved trial registry output; related publication describes individualized AP4M1 gene therapy for SPG50 (dowling2024aavgenetherapy pages 1-2) |
| NCT05196178 | Spinal Cord Stimulation Therapy for Hereditary Spastic Paraplegias Patients | Unknown | NA | Interventional | 12 | Xuanwu Hospital, Beijing (OpenTargets Search: hereditary spastic paraplegia) |
| NCT06728787 | Robot-assisted Walking Treatment in Hereditary Spastic Paraplegia (HSP) | Recruiting | Not provided | Observational | 50 | IRCCS Eugenio Medea (OpenTargets Search: hereditary spastic paraplegia) |


*Table: This table summarizes active and recent clinical studies in hereditary spastic paraplegia, including observational natural-history efforts, rehabilitation trials, and emerging gene therapy. It is useful for identifying current trial readiness and intervention development across the HSP field.*

The Spastic Paraplegia–Centers of Excellence Research Network (SP-CERN) has been established across 11 US institutions to promote clinical trial readiness through standardized clinical assessments, biorepository development, and natural history data collection (OpenTargets Search: hereditary spastic paraplegia).

---

## 13. Prevention

### Primary Prevention
No primary prevention strategies exist for complex HSP given its monogenic genetic etiology. Risk reduction focuses on genetic counseling and family planning.

### Genetic Counseling and Screening (MAXO:0000015 – genetic counseling)
- **Carrier screening:** Relevant for AR forms, particularly in consanguineous populations
- **Prenatal testing:** Available when the familial variant is known
- **Preimplantation genetic diagnosis:** An option for families with known pathogenic variants
- **Cascade genetic testing:** Recommended for at-risk family members

### Tertiary Prevention
Management of complications through regular physiotherapy, assistive devices, and symptomatic medications can delay functional decline and improve quality of life (meyyazhagan2022thepuzzleof pages 6-9, amprosi2026naturalhistoryin pages 11-13).

---

## 14. Other Species / Natural Disease

Complex HSP is a human-specific clinical entity. No naturally occurring disease equivalent has been described in animals. However, loss-of-function mutations in orthologous genes cause motor phenotypes in model organisms (see Section 15).

---

## 15. Model Organisms

### Mouse Models
Mouse models have been created for multiple HSP genes but frequently fail to fully recapitulate human motor phenotypes (damiani2024pluripotentstemcells pages 2-3, damiani2024pluripotentstemcells pages 1-2). ZFYVE26 knockout mice develop late-onset spastic paraplegia and cerebellar ataxia with neurodegeneration features at 16 months (garg2023zebrafishasa pages 25-28). Spastin knockout mice show gait abnormalities and disrupted anterograde mitochondrial transport (garg2023zebrafishasa pages 25-28). Ap4m1-KO mice treated with AAV9/AP4M1 showed age- and dose-dependent therapeutic benefits, validating gene therapy approaches (chen2023intrathecalaav9ap4m1gene pages 1-2). CRISPR-Cas9 knock-in rat models display progressive motor deficits, corpus callosum thinning, and hind limb spasticity (damiani2024pluripotentstemcells pages 6-7).

### Zebrafish Models (NCBI Taxon: 7955)
Over 40 zebrafish studies have been published on HSP research (garg2024divingdeepzebrafish pages 5-6). While zebrafish lack a corticospinal tract, they demonstrate key pathological features including impaired locomotion, disrupted motor axon growth, and axonal transport defects (garg2024divingdeepzebrafish pages 5-6). Spastizin mutant zebrafish show M-cell degeneration, axon demyelination, and impaired locomotion (garg2023zebrafishasa pages 25-28). AMFR-deficient zebrafish exhibit altered touch-evoked escape response and motor neuron branching defects, which were rescued by FDA-approved statins (garg2024divingdeepzebrafish pages 5-6). Zebrafish are valued for high-throughput drug screening and optical transparency during development (garg2023zebrafishasa pages 25-28).

### Drosophila Models (NCBI Taxon: 7227)
Eighteen orthologous SPG genes have been identified in Drosophila, including SPAST, ATL1, and SPG7 (vivarelli2025wingsofdiscovery pages 5-7). Loss of spas (Drosophila spastin ortholog) causes progressive movement defects, neuronal apoptosis, and immobility (vivarelli2025wingsofdiscovery pages 5-7). KIF5A mutation models faithfully reproduced axonal transport impairment, axonal swellings, and motor deficits (vivarelli2025wingsofdiscovery pages 19-20). Drosophila offers genetic tractability, rapid life cycle, and neuromuscular junction assays for phenotypic evaluation (vivarelli2025wingsofdiscovery pages 3-5).

### iPSC Models
Patient-derived induced pluripotent stem cells have emerged as the most promising human cellular model for HSP (damiani2024pluripotentstemcells pages 1-2). iPSC-derived neurons faithfully mimic HSP in vitro, displaying morphological and molecular properties relevant to disease including mitochondrial dysfunction and axonal degeneration (damiani2024pluripotentstemcells pages 1-2, vivarelli2025wingsofdiscovery pages 19-20). iPSC-derived astrocytes from HSP patients show impaired lipid metabolism and reduced lipid droplet size (vijayaraghavan2025roleofglial pages 2-3). Three-dimensional organoid structures from iPSCs offer improved complexity for disease modeling and personalized medicine approaches (damiani2024pluripotentstemcells pages 6-7).

### Integrated Approach
A complementary multi-model strategy has been advocated: Drosophila for high-speed genetic analysis, mice for behavioral and systemic validation, zebrafish for high-throughput drug screening, and human iPSC cultures for mechanistic studies in the patient's genetic background (vivarelli2025wingsofdiscovery pages 19-20).

---

## Summary

Complex hereditary spastic paraplegia is a genetically heterogeneous group of Mendelian neurodegenerative disorders characterized by progressive corticospinal tract degeneration with additional neurological features. Over 90 genetic loci have been identified, with SPG11, SPG15, SPG7, and AP-4 complex genes (SPG47, SPG50, SPG51, SPG52) representing the most significant complex HSP subtypes. The pathophysiology involves convergent disruption of ER morphogenesis, autophagy-lysosomal pathways, mitochondrial function, lipid metabolism, and axonal transport. Disease management remains primarily symptomatic, but the field is entering a transformative era with the first AAV gene therapy clinical trial for SPG50 demonstrating safety and preliminary efficacy. Large-scale natural history studies and research networks such as SP-CERN are building clinical trial readiness across the HSP community. Fluid biomarkers including neurofilament light chain show promise for disease monitoring and clinical trial endpoints.

References

1. (meyyazhagan2022thepuzzleof pages 1-2): Arun Meyyazhagan, Haripriya Kuchi Bhotla, Manikantan Pappuswamy, and Antonio Orlacchio. The puzzle of hereditary spastic paraplegia: from epidemiology to treatment. International Journal of Molecular Sciences, 23:7665, Jul 2022. URL: https://doi.org/10.3390/ijms23147665, doi:10.3390/ijms23147665. This article has 60 citations.

2. (meyyazhagan2022hereditaryspasticparaplegia pages 1-2): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 192 citations.

3. (amprosi2026naturalhistoryin pages 1-2): Matthias Amprosi, Elisabetta Indelicato, Andreas Eigentler, Daniel Boesch, Josef Fritz, Wolfgang Nachbauer, and Sylvia Boesch. Natural history in hereditary spastic paraplegias: real-world data from an austrian cohort. Journal of Neurology, Jan 2026. URL: https://doi.org/10.1007/s00415-025-13606-y, doi:10.1007/s00415-025-13606-y. This article has 0 citations and is from a domain leading peer-reviewed journal.

4. (OpenTargets Search: hereditary spastic paraplegia): Open Targets Query (hereditary spastic paraplegia, 32 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (yu2023clinicalfeaturesand pages 1-2): Weiyi Yu, Ji He, Xiangyi Liu, Jieying Wu, Xiying Cai, Yingshuang Zhang, Xiaoxuan Liu, and Dongsheng Fan. Clinical features and genetic spectrum of chinese patients with hereditary spastic paraplegia: a 14-year study. Frontiers in Genetics, Feb 2023. URL: https://doi.org/10.3389/fgene.2023.1085442, doi:10.3389/fgene.2023.1085442. This article has 7 citations and is from a peer-reviewed journal.

6. (meyyazhagan2022hereditaryspasticparaplegia pages 2-4): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 192 citations.

7. (cipriano2025fluidbiomarkersin pages 1-2): Lorenzo Cipriano, Nunzio Setola, Melissa Barghigiani, and Filippo Maria Santorelli. Fluid biomarkers in hereditary spastic paraplegia: a narrative review and integrative framework for complex neurodegenerative mechanisms. Genes, 16:1189, Oct 2025. URL: https://doi.org/10.3390/genes16101189, doi:10.3390/genes16101189. This article has 2 citations.

8. (fereshtehnejad2023movementdisordersin pages 4-5): Seyed-Mohammad Fereshtehnejad, Philip A. Saleh, Lais M. Oliveira, Neha Patel, Suvorit Bhowmick, Gerard Saranza, and Lorraine V. Kalia. Movement disorders in hereditary spastic paraplegia (hsp): a systematic review and individual participant data meta-analysis. Neurological Sciences, 44:947-959, Nov 2023. URL: https://doi.org/10.1007/s10072-022-06516-8, doi:10.1007/s10072-022-06516-8. This article has 18 citations and is from a peer-reviewed journal.

9. (fereshtehnejad2023movementdisordersin pages 5-6): Seyed-Mohammad Fereshtehnejad, Philip A. Saleh, Lais M. Oliveira, Neha Patel, Suvorit Bhowmick, Gerard Saranza, and Lorraine V. Kalia. Movement disorders in hereditary spastic paraplegia (hsp): a systematic review and individual participant data meta-analysis. Neurological Sciences, 44:947-959, Nov 2023. URL: https://doi.org/10.1007/s10072-022-06516-8, doi:10.1007/s10072-022-06516-8. This article has 18 citations and is from a peer-reviewed journal.

10. (saffari2023theclinicaland pages 3-5): Afshin Saffari, Melanie Kellner, Catherine Jordan, Helena Rosengarten, Alisa Mo, Bo Zhang, Oleksandr Strelko, Sonja Neuser, Marie Y Davis, Nobuaki Yoshikura, Naonobu Futamura, Tomoya Takeuchi, Shin Nabatame, Hiroyuki Ishiura, Shoji Tsuji, Huda Shujaa Aldeen, Elisa Cali, Clarissa Rocca, Henry Houlden, Stephanie Efthymiou, Birgit Assmann, Grace Yoon, Bianca A Trombetta, Pia Kivisäkk, Florian Eichler, Haitian Nan, Yoshihisa Takiyama, Alessandra Tessa, Filippo M Santorelli, Mustafa Sahin, Craig Blackstone, Edward Yang, Rebecca Schüle, and Darius Ebrahimi-Fakhari. The clinical and molecular spectrum of zfyve26-associated hereditary spastic paraplegia: spg15. Brain : a journal of neurology, 146:2003-2015, Oct 2023. URL: https://doi.org/10.1093/brain/awac391, doi:10.1093/brain/awac391. This article has 25 citations.

11. (saffari2023theclinicaland pages 1-2): Afshin Saffari, Melanie Kellner, Catherine Jordan, Helena Rosengarten, Alisa Mo, Bo Zhang, Oleksandr Strelko, Sonja Neuser, Marie Y Davis, Nobuaki Yoshikura, Naonobu Futamura, Tomoya Takeuchi, Shin Nabatame, Hiroyuki Ishiura, Shoji Tsuji, Huda Shujaa Aldeen, Elisa Cali, Clarissa Rocca, Henry Houlden, Stephanie Efthymiou, Birgit Assmann, Grace Yoon, Bianca A Trombetta, Pia Kivisäkk, Florian Eichler, Haitian Nan, Yoshihisa Takiyama, Alessandra Tessa, Filippo M Santorelli, Mustafa Sahin, Craig Blackstone, Edward Yang, Rebecca Schüle, and Darius Ebrahimi-Fakhari. The clinical and molecular spectrum of zfyve26-associated hereditary spastic paraplegia: spg15. Brain : a journal of neurology, 146:2003-2015, Oct 2023. URL: https://doi.org/10.1093/brain/awac391, doi:10.1093/brain/awac391. This article has 25 citations.

12. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 4-6): Justyna Chojdak-Łukasiewicz, Katarzyna Sulima, Anna Zimny, Marta Waliszewska-Prosół, and Sławomir Budrewicz. Hereditary spastic paraplegia type 11—clinical, genetic and neuroimaging characteristics. International Journal of Molecular Sciences, 24:17530, Dec 2023. URL: https://doi.org/10.3390/ijms242417530, doi:10.3390/ijms242417530. This article has 8 citations.

13. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 2-4): Justyna Chojdak-Łukasiewicz, Katarzyna Sulima, Anna Zimny, Marta Waliszewska-Prosół, and Sławomir Budrewicz. Hereditary spastic paraplegia type 11—clinical, genetic and neuroimaging characteristics. International Journal of Molecular Sciences, 24:17530, Dec 2023. URL: https://doi.org/10.3390/ijms242417530, doi:10.3390/ijms242417530. This article has 8 citations.

14. (saffari2023theclinicaland pages 6-8): Afshin Saffari, Melanie Kellner, Catherine Jordan, Helena Rosengarten, Alisa Mo, Bo Zhang, Oleksandr Strelko, Sonja Neuser, Marie Y Davis, Nobuaki Yoshikura, Naonobu Futamura, Tomoya Takeuchi, Shin Nabatame, Hiroyuki Ishiura, Shoji Tsuji, Huda Shujaa Aldeen, Elisa Cali, Clarissa Rocca, Henry Houlden, Stephanie Efthymiou, Birgit Assmann, Grace Yoon, Bianca A Trombetta, Pia Kivisäkk, Florian Eichler, Haitian Nan, Yoshihisa Takiyama, Alessandra Tessa, Filippo M Santorelli, Mustafa Sahin, Craig Blackstone, Edward Yang, Rebecca Schüle, and Darius Ebrahimi-Fakhari. The clinical and molecular spectrum of zfyve26-associated hereditary spastic paraplegia: spg15. Brain : a journal of neurology, 146:2003-2015, Oct 2023. URL: https://doi.org/10.1093/brain/awac391, doi:10.1093/brain/awac391. This article has 25 citations.

15. (ikeda2023geneticandclinical pages 3-4): Azusa Ikeda, Tatsuro Kumaki, Yu Tsuyusaki, Megumi Tsuji, Yumi Enomoto, Atsushi Fujita, Hirotomo Saitsu, Naomichi Matsumoto, Kenji Kurosawa, and Tomohide Goto. Genetic and clinical features of pediatric-onset hereditary spastic paraplegia: a single-center study in japan. Frontiers in Neurology, May 2023. URL: https://doi.org/10.3389/fneur.2023.1085228, doi:10.3389/fneur.2023.1085228. This article has 6 citations and is from a peer-reviewed journal.

16. (awuah2024hereditaryspasticparaplegia pages 8-10): Wireko Andrew Awuah, Joecelyn Kirani Tan, Anastasiia D Shkodina, Tomas Ferreira, Favour Tope Adebusoye, Adele Mazzoleni, Jack Wellington, Lian David, Ellie Chilcott, Helen Huang, Toufik Abdul-Rahman, Vallabh Shet, Oday Atallah, Jacob Kalmanovich, Riaz Jiffry, Divine Elizabeth Madhu, Kateryna Sikora, Oleksii Kmyta, and Mykhailo Yu Delva. Hereditary spastic paraplegia: novel insights into the pathogenesis and management. SAGE Open Medicine, Dec 2024. URL: https://doi.org/10.1177/20503121231221941, doi:10.1177/20503121231221941. This article has 31 citations.

17. (dowling2024aavgenetherapy pages 1-2): James J. Dowling, Terry Pirovolakis, Keshini Devakandan, Ana Stosic, Mia Pidsadny, Elisa Nigro, Mustafa Sahin, Darius Ebrahimi-Fakhari, Souad Messahel, Ganapathy Varadarajan, Benjamin M. Greenberg, Xin Chen, Berge A. Minassian, Ronald Cohn, Carsten G. Bonnemann, and Steven J. Gray. Aav gene therapy for hereditary spastic paraplegia type 50: a phase 1 trial in a single patient. Nature Medicine, 30:1882-1887, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03078-4, doi:10.1038/s41591-024-03078-4. This article has 40 citations and is from a highest quality peer-reviewed journal.

18. (saffari2023theclinicaland pages 8-9): Afshin Saffari, Melanie Kellner, Catherine Jordan, Helena Rosengarten, Alisa Mo, Bo Zhang, Oleksandr Strelko, Sonja Neuser, Marie Y Davis, Nobuaki Yoshikura, Naonobu Futamura, Tomoya Takeuchi, Shin Nabatame, Hiroyuki Ishiura, Shoji Tsuji, Huda Shujaa Aldeen, Elisa Cali, Clarissa Rocca, Henry Houlden, Stephanie Efthymiou, Birgit Assmann, Grace Yoon, Bianca A Trombetta, Pia Kivisäkk, Florian Eichler, Haitian Nan, Yoshihisa Takiyama, Alessandra Tessa, Filippo M Santorelli, Mustafa Sahin, Craig Blackstone, Edward Yang, Rebecca Schüle, and Darius Ebrahimi-Fakhari. The clinical and molecular spectrum of zfyve26-associated hereditary spastic paraplegia: spg15. Brain : a journal of neurology, 146:2003-2015, Oct 2023. URL: https://doi.org/10.1093/brain/awac391, doi:10.1093/brain/awac391. This article has 25 citations.

19. (amprosi2026naturalhistoryin pages 13-14): Matthias Amprosi, Elisabetta Indelicato, Andreas Eigentler, Daniel Boesch, Josef Fritz, Wolfgang Nachbauer, and Sylvia Boesch. Natural history in hereditary spastic paraplegias: real-world data from an austrian cohort. Journal of Neurology, Jan 2026. URL: https://doi.org/10.1007/s00415-025-13606-y, doi:10.1007/s00415-025-13606-y. This article has 0 citations and is from a domain leading peer-reviewed journal.

20. (amprosi2026naturalhistoryin pages 11-13): Matthias Amprosi, Elisabetta Indelicato, Andreas Eigentler, Daniel Boesch, Josef Fritz, Wolfgang Nachbauer, and Sylvia Boesch. Natural history in hereditary spastic paraplegias: real-world data from an austrian cohort. Journal of Neurology, Jan 2026. URL: https://doi.org/10.1007/s00415-025-13606-y, doi:10.1007/s00415-025-13606-y. This article has 0 citations and is from a domain leading peer-reviewed journal.

21. (awuah2024hereditaryspasticparaplegia pages 1-2): Wireko Andrew Awuah, Joecelyn Kirani Tan, Anastasiia D Shkodina, Tomas Ferreira, Favour Tope Adebusoye, Adele Mazzoleni, Jack Wellington, Lian David, Ellie Chilcott, Helen Huang, Toufik Abdul-Rahman, Vallabh Shet, Oday Atallah, Jacob Kalmanovich, Riaz Jiffry, Divine Elizabeth Madhu, Kateryna Sikora, Oleksii Kmyta, and Mykhailo Yu Delva. Hereditary spastic paraplegia: novel insights into the pathogenesis and management. SAGE Open Medicine, Dec 2024. URL: https://doi.org/10.1177/20503121231221941, doi:10.1177/20503121231221941. This article has 31 citations.

22. (vijayaraghavan2025roleofglial pages 2-3): Manaswini Vijayaraghavan, Sarvika Periyapalayam Murali, Gitika Thakur, and Xue-Jun Li. Role of glial cells in motor neuron degeneration in hereditary spastic paraplegias. Frontiers in Cellular Neuroscience, Apr 2025. URL: https://doi.org/10.3389/fncel.2025.1553658, doi:10.3389/fncel.2025.1553658. This article has 3 citations.

23. (meyyazhagan2022hereditaryspasticparaplegia pages 12-14): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 192 citations.

24. (chojdakłukasiewicz2023hereditaryspasticparaplegia pages 7-8): Justyna Chojdak-Łukasiewicz, Katarzyna Sulima, Anna Zimny, Marta Waliszewska-Prosół, and Sławomir Budrewicz. Hereditary spastic paraplegia type 11—clinical, genetic and neuroimaging characteristics. International Journal of Molecular Sciences, 24:17530, Dec 2023. URL: https://doi.org/10.3390/ijms242417530, doi:10.3390/ijms242417530. This article has 8 citations.

25. (wiseman2024preclinicaldevelopmentof pages 13-15): Jessica P Wiseman, Joseph M Scarrott, João Alves-Cruzeiro, Afshin Saffari, Cedric Böger, Evangelia Karyka, Emily Dawes, Alexandra K Davies, Paolo M Marchi, Emily Graves, Fiona Fernandes, Zih-Liang Yang, Ian Coldicott, Jennifer Hirst, Christopher P Webster, J Robin Highley, Neil Hackett, Adrienn Angyal, Thushan de Silva, Adrian Higginbottom, Pamela J Shaw, Laura Ferraiuolo, Darius Ebrahimi-Fakhari, and Mimoun Azzouz. Pre-clinical development of ap4b1 gene replacement therapy for hereditary spastic paraplegia type 47. EMBO Molecular Medicine, 16:2882-2917, Oct 2024. URL: https://doi.org/10.1038/s44321-024-00148-5, doi:10.1038/s44321-024-00148-5. This article has 14 citations and is from a highest quality peer-reviewed journal.

26. (chen2023intrathecalaav9ap4m1gene pages 1-2): Xin Chen, Thomas Dong, Yuhui Hu, Raffaella De Pace, Rafael Mattera, Kathrin Eberhardt, Marvin Ziegler, Terry Pirovolakis, Mustafa Sahin, Juan S. Bonifacino, Darius Ebrahimi-Fakhari, and Steven J. Gray. Intrathecal aav9/ap4m1 gene therapy for hereditary spastic paraplegia 50 shows safety and efficacy in preclinical studies. Journal of Clinical Investigation, May 2023. URL: https://doi.org/10.1172/jci164575, doi:10.1172/jci164575. This article has 54 citations and is from a highest quality peer-reviewed journal.

27. (meyyazhagan2022thepuzzleof pages 11-12): Arun Meyyazhagan, Haripriya Kuchi Bhotla, Manikantan Pappuswamy, and Antonio Orlacchio. The puzzle of hereditary spastic paraplegia: from epidemiology to treatment. International Journal of Molecular Sciences, 23:7665, Jul 2022. URL: https://doi.org/10.3390/ijms23147665, doi:10.3390/ijms23147665. This article has 60 citations.

28. (meyyazhagan2022hereditaryspasticparaplegia pages 4-6): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 192 citations.

29. (meyyazhagan2022hereditaryspasticparaplegia pages 20-21): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 192 citations.

30. (meyyazhagan2022hereditaryspasticparaplegia pages 14-16): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 192 citations.

31. (meyyazhagan2022thepuzzleof pages 12-14): Arun Meyyazhagan, Haripriya Kuchi Bhotla, Manikantan Pappuswamy, and Antonio Orlacchio. The puzzle of hereditary spastic paraplegia: from epidemiology to treatment. International Journal of Molecular Sciences, 23:7665, Jul 2022. URL: https://doi.org/10.3390/ijms23147665, doi:10.3390/ijms23147665. This article has 60 citations.

32. (garg2024divingdeepzebrafish pages 5-6): Vranda Garg and Bart R. H. Geurten. Diving deep: zebrafish models in motor neuron degeneration research. Frontiers in Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnins.2024.1424025, doi:10.3389/fnins.2024.1424025. This article has 10 citations and is from a peer-reviewed journal.

33. (meyyazhagan2022thepuzzleof pages 5-6): Arun Meyyazhagan, Haripriya Kuchi Bhotla, Manikantan Pappuswamy, and Antonio Orlacchio. The puzzle of hereditary spastic paraplegia: from epidemiology to treatment. International Journal of Molecular Sciences, 23:7665, Jul 2022. URL: https://doi.org/10.3390/ijms23147665, doi:10.3390/ijms23147665. This article has 60 citations.

34. (saffari2023theclinicaland pages 13-13): Afshin Saffari, Melanie Kellner, Catherine Jordan, Helena Rosengarten, Alisa Mo, Bo Zhang, Oleksandr Strelko, Sonja Neuser, Marie Y Davis, Nobuaki Yoshikura, Naonobu Futamura, Tomoya Takeuchi, Shin Nabatame, Hiroyuki Ishiura, Shoji Tsuji, Huda Shujaa Aldeen, Elisa Cali, Clarissa Rocca, Henry Houlden, Stephanie Efthymiou, Birgit Assmann, Grace Yoon, Bianca A Trombetta, Pia Kivisäkk, Florian Eichler, Haitian Nan, Yoshihisa Takiyama, Alessandra Tessa, Filippo M Santorelli, Mustafa Sahin, Craig Blackstone, Edward Yang, Rebecca Schüle, and Darius Ebrahimi-Fakhari. The clinical and molecular spectrum of zfyve26-associated hereditary spastic paraplegia: spg15. Brain : a journal of neurology, 146:2003-2015, Oct 2023. URL: https://doi.org/10.1093/brain/awac391, doi:10.1093/brain/awac391. This article has 25 citations.

35. (meyyazhagan2022thepuzzleof pages 2-5): Arun Meyyazhagan, Haripriya Kuchi Bhotla, Manikantan Pappuswamy, and Antonio Orlacchio. The puzzle of hereditary spastic paraplegia: from epidemiology to treatment. International Journal of Molecular Sciences, 23:7665, Jul 2022. URL: https://doi.org/10.3390/ijms23147665, doi:10.3390/ijms23147665. This article has 60 citations.

36. (awuah2024hereditaryspasticparaplegia pages 2-4): Wireko Andrew Awuah, Joecelyn Kirani Tan, Anastasiia D Shkodina, Tomas Ferreira, Favour Tope Adebusoye, Adele Mazzoleni, Jack Wellington, Lian David, Ellie Chilcott, Helen Huang, Toufik Abdul-Rahman, Vallabh Shet, Oday Atallah, Jacob Kalmanovich, Riaz Jiffry, Divine Elizabeth Madhu, Kateryna Sikora, Oleksii Kmyta, and Mykhailo Yu Delva. Hereditary spastic paraplegia: novel insights into the pathogenesis and management. SAGE Open Medicine, Dec 2024. URL: https://doi.org/10.1177/20503121231221941, doi:10.1177/20503121231221941. This article has 31 citations.

37. (chen2022geneticoriginof pages 1-2): Jiann-Nan Chen, Zhe Zhao, Hong-rui Shen, Qi Bing, Nan Li, Xuan Guo, and Jing Hu. Genetic origin of patients having spastic paraplegia with or without other neurologic manifestations. BMC Neurology, May 2022. URL: https://doi.org/10.1186/s12883-022-02708-z, doi:10.1186/s12883-022-02708-z. This article has 10 citations and is from a peer-reviewed journal.

38. (cipriano2025fluidbiomarkersin pages 12-14): Lorenzo Cipriano, Nunzio Setola, Melissa Barghigiani, and Filippo Maria Santorelli. Fluid biomarkers in hereditary spastic paraplegia: a narrative review and integrative framework for complex neurodegenerative mechanisms. Genes, 16:1189, Oct 2025. URL: https://doi.org/10.3390/genes16101189, doi:10.3390/genes16101189. This article has 2 citations.

39. (siow2023outcomemeasuresand pages 2-3): Sue-Faye Siow, Dennis Yeow, Laura I. Rudaks, Fangzhi Jia, Gautam Wali, Carolyn M. Sue, and Kishore R. Kumar. Outcome measures and biomarkers for clinical trials in hereditary spastic paraplegia: a scoping review. Genes, 14:1756, Sep 2023. URL: https://doi.org/10.3390/genes14091756, doi:10.3390/genes14091756. This article has 18 citations.

40. (meyyazhagan2022hereditaryspasticparaplegia pages 16-18): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 192 citations.

41. (awuah2024hereditaryspasticparaplegia pages 12-13): Wireko Andrew Awuah, Joecelyn Kirani Tan, Anastasiia D Shkodina, Tomas Ferreira, Favour Tope Adebusoye, Adele Mazzoleni, Jack Wellington, Lian David, Ellie Chilcott, Helen Huang, Toufik Abdul-Rahman, Vallabh Shet, Oday Atallah, Jacob Kalmanovich, Riaz Jiffry, Divine Elizabeth Madhu, Kateryna Sikora, Oleksii Kmyta, and Mykhailo Yu Delva. Hereditary spastic paraplegia: novel insights into the pathogenesis and management. SAGE Open Medicine, Dec 2024. URL: https://doi.org/10.1177/20503121231221941, doi:10.1177/20503121231221941. This article has 31 citations.

42. (meyyazhagan2022hereditaryspasticparaplegia pages 25-25): Arun Meyyazhagan and Antonio Orlacchio. Hereditary spastic paraplegia: an update. International Journal of Molecular Sciences, 23:1697, Feb 2022. URL: https://doi.org/10.3390/ijms23031697, doi:10.3390/ijms23031697. This article has 192 citations.

43. (meyyazhagan2022thepuzzleof pages 6-9): Arun Meyyazhagan, Haripriya Kuchi Bhotla, Manikantan Pappuswamy, and Antonio Orlacchio. The puzzle of hereditary spastic paraplegia: from epidemiology to treatment. International Journal of Molecular Sciences, 23:7665, Jul 2022. URL: https://doi.org/10.3390/ijms23147665, doi:10.3390/ijms23147665. This article has 60 citations.

44. (meyyazhagan2022thepuzzleof pages 14-15): Arun Meyyazhagan, Haripriya Kuchi Bhotla, Manikantan Pappuswamy, and Antonio Orlacchio. The puzzle of hereditary spastic paraplegia: from epidemiology to treatment. International Journal of Molecular Sciences, 23:7665, Jul 2022. URL: https://doi.org/10.3390/ijms23147665, doi:10.3390/ijms23147665. This article has 60 citations.

45. (awuah2024hereditaryspasticparaplegia pages 20-20): Wireko Andrew Awuah, Joecelyn Kirani Tan, Anastasiia D Shkodina, Tomas Ferreira, Favour Tope Adebusoye, Adele Mazzoleni, Jack Wellington, Lian David, Ellie Chilcott, Helen Huang, Toufik Abdul-Rahman, Vallabh Shet, Oday Atallah, Jacob Kalmanovich, Riaz Jiffry, Divine Elizabeth Madhu, Kateryna Sikora, Oleksii Kmyta, and Mykhailo Yu Delva. Hereditary spastic paraplegia: novel insights into the pathogenesis and management. SAGE Open Medicine, Dec 2024. URL: https://doi.org/10.1177/20503121231221941, doi:10.1177/20503121231221941. This article has 31 citations.

46. (awuah2024hereditaryspasticparaplegia pages 19-20): Wireko Andrew Awuah, Joecelyn Kirani Tan, Anastasiia D Shkodina, Tomas Ferreira, Favour Tope Adebusoye, Adele Mazzoleni, Jack Wellington, Lian David, Ellie Chilcott, Helen Huang, Toufik Abdul-Rahman, Vallabh Shet, Oday Atallah, Jacob Kalmanovich, Riaz Jiffry, Divine Elizabeth Madhu, Kateryna Sikora, Oleksii Kmyta, and Mykhailo Yu Delva. Hereditary spastic paraplegia: novel insights into the pathogenesis and management. SAGE Open Medicine, Dec 2024. URL: https://doi.org/10.1177/20503121231221941, doi:10.1177/20503121231221941. This article has 31 citations.

47. (damiani2024pluripotentstemcells pages 2-3): Devid Damiani, Matteo Baggiani, Stefania Della Vecchia, Valentina Naef, and Filippo Maria Santorelli. Pluripotent stem cells as a preclinical cellular model for studying hereditary spastic paraplegias. International Journal of Molecular Sciences, 25:2615, Feb 2024. URL: https://doi.org/10.3390/ijms25052615, doi:10.3390/ijms25052615. This article has 11 citations.

48. (damiani2024pluripotentstemcells pages 1-2): Devid Damiani, Matteo Baggiani, Stefania Della Vecchia, Valentina Naef, and Filippo Maria Santorelli. Pluripotent stem cells as a preclinical cellular model for studying hereditary spastic paraplegias. International Journal of Molecular Sciences, 25:2615, Feb 2024. URL: https://doi.org/10.3390/ijms25052615, doi:10.3390/ijms25052615. This article has 11 citations.

49. (garg2023zebrafishasa pages 25-28): Vranda Garg. Zebrafish as a model for hereditary spastic paraplegia. ArXiv, 2023. URL: https://doi.org/10.53846/goediss-9965, doi:10.53846/goediss-9965. This article has 0 citations.

50. (damiani2024pluripotentstemcells pages 6-7): Devid Damiani, Matteo Baggiani, Stefania Della Vecchia, Valentina Naef, and Filippo Maria Santorelli. Pluripotent stem cells as a preclinical cellular model for studying hereditary spastic paraplegias. International Journal of Molecular Sciences, 25:2615, Feb 2024. URL: https://doi.org/10.3390/ijms25052615, doi:10.3390/ijms25052615. This article has 11 citations.

51. (vivarelli2025wingsofdiscovery pages 5-7): Rachele Vivarelli, Chiara Vantaggiato, Maria Teresa Bassi, Filippo Maria Santorelli, and Maria Marchese. Wings of discovery: using drosophila to decode hereditary spastic paraplegia and ataxias. Cells, 14:1466, Sep 2025. URL: https://doi.org/10.3390/cells14181466, doi:10.3390/cells14181466. This article has 1 citations.

52. (vivarelli2025wingsofdiscovery pages 19-20): Rachele Vivarelli, Chiara Vantaggiato, Maria Teresa Bassi, Filippo Maria Santorelli, and Maria Marchese. Wings of discovery: using drosophila to decode hereditary spastic paraplegia and ataxias. Cells, 14:1466, Sep 2025. URL: https://doi.org/10.3390/cells14181466, doi:10.3390/cells14181466. This article has 1 citations.

53. (vivarelli2025wingsofdiscovery pages 3-5): Rachele Vivarelli, Chiara Vantaggiato, Maria Teresa Bassi, Filippo Maria Santorelli, and Maria Marchese. Wings of discovery: using drosophila to decode hereditary spastic paraplegia and ataxias. Cells, 14:1466, Sep 2025. URL: https://doi.org/10.3390/cells14181466, doi:10.3390/cells14181466. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Complex_Hereditary_Spastic_Paraplegia-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Complex_Hereditary_Spastic_Paraplegia-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Complex_Hereditary_Spastic_Paraplegia-deep-research-falcon_artifacts/artifact-02.md)