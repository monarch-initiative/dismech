---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:50:40.404873'
end_time: '2026-07-05T19:10:32.636586'
duration_seconds: 1192.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pertussis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 50
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Pertussis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Pertussis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Pertussis-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pertussis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pertussis** covering all of the
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
- **Disease Name:** Pertussis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pertussis** covering all of the
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


# Comprehensive Disease Research Report: Pertussis (Whooping Cough)

---

## 1. Disease Information

### Overview

Pertussis, commonly known as whooping cough, is an acute, highly contagious respiratory infection caused by the Gram-negative coccobacillus bacterium *Bordetella pertussis* (NCBI Taxonomy: NCBITaxon:520) (colak2023bordetellapertussisand pages 1-2, ifill2023lipidamodifications pages 18-25). The disease is characterized by severe paroxysmal coughing episodes followed by a characteristic inspiratory "whoop," which can result in apnea, cyanosis, and post-tussive vomiting (chamorro2023bordetellabronchisepticaand pages 2-3). Pertussis is particularly dangerous in neonates and young infants, in whom it can cause brain damage and death (colak2023bordetellapertussisand pages 1-2). *B. pertussis* is an obligate human pathogen with no known environmental reservoir (ifill2023lipidamodifications pages 18-25).

### Key Identifiers

The following table provides a comprehensive reference for all disease identifiers and ontology terms:

| Ontology/Database | Term/Code | Description |
|---|---|---|
| MONDO | MONDO:0005077 | Pertussis; MONDO disease identifier for whooping cough/pertussis (OpenTargets Search: pertussis,whooping cough) |
| ICD-10-CM | A37.0 | Whooping cough due to *Bordetella pertussis* |
| ICD-10-CM | A37.1 | Whooping cough due to *Bordetella parapertussis* |
| ICD-10-CM | A37.8 | Whooping cough due to other *Bordetella* species |
| ICD-10-CM | A37.9 | Whooping cough, unspecified species |
| ICD-11 | 1C12 | Pertussis / whooping cough (ICD-11 category for pertussis) |
| MeSH | D014917 | Whooping Cough; MeSH descriptor for pertussis |
| HPO | HP:0031247 | Whooping cough; characteristic paroxysmal inspiratory “whoop” phenotype |
| HPO | HP:0012735 | Cough; core symptom in catarrhal and paroxysmal stages (chamorro2023bordetellabronchisepticaand pages 2-3, ifill2023lipidamodifications pages 18-25) |
| HPO | HP:0002360 | Sleep disturbance; clinically relevant consequence of prolonged nocturnal paroxysmal coughing |
| HPO | HP:0002094 | Dyspnea; breathing difficulty during coughing episodes/apnea-cyanosis events (chamorro2023bordetellabronchisepticaand pages 2-3) |
| HPO | HP:0012418 | Hypoxemia; may accompany severe infant disease with apnea/cyanosis |
| HPO | HP:0002105 | Apnea; common severe manifestation in infants (chamorro2023bordetellabronchisepticaand pages 2-3) |
| HPO | HP:0000961 | Cyanosis; may occur during severe paroxysms (chamorro2023bordetellabronchisepticaand pages 2-3) |
| HPO | HP:0033847 | Posttussive vomiting; classic pertussis-associated symptom (chamorro2023bordetellabronchisepticaand pages 2-3) |
| HPO | HP:0001250 | Seizure; severe complication reported in pertussis (ernst2022novelstrategiesto pages 1-2) |
| HPO | HP:0001252 | Muscular hypotonia; potential feature during severe infant illness |
| HPO | HP:0001945 | Fever; usually low-grade in early catarrhal stage (ifill2023lipidamodifications pages 18-25) |
| HPO | HP:0012378 | Fatigue; common functional burden during prolonged illness |
| HPO | HP:0002205 | Pneumonia; important complication, especially in infants (ernst2022novelstrategiesto pages 1-2, regan2023maternalpertussisvaccination pages 5-6) |
| HPO | HP:0001875 | Neutropenia/altered leukocyte phenotype not typical; avoid overannotation unless case-specific |
| HPO | HP:0001974 | Leukocytosis; severe pertussis-associated laboratory abnormality linked to PT effects (ernst2022novelstrategiesto pages 1-2) |
| GO Biological Process | GO:0044419 | Interspecies interaction between organisms; broad host-pathogen interaction category |
| GO Biological Process | GO:0009617 | Response to bacterium; host response relevant to *B. pertussis* infection |
| GO Biological Process | GO:0050900 | Leukocyte migration; pertussis toxin alters chemokine signaling and neutrophil recruitment (chamorro2023bordetellabronchisepticaand pages 16-18, ernst2022novelstrategiesto pages 12-13) |
| GO Biological Process | GO:0001817 | Regulation of cytokine production; LOS, FHA, PT, and T3SS modulate cytokine responses (chamorro2023bordetellabronchisepticaand pages 13-15, chamorro2023bordetellabronchisepticaand pages 18-20, chamorro2023bordetellabronchisepticaand pages 16-18) |
| GO Biological Process | GO:0071621 | Granulocyte chemotaxis; relevant to neutrophil trafficking impaired by PT |
| GO Biological Process | GO:0032609 | Interferon-gamma production; central to Th1 immunity against pertussis (chamorro2023bordetellabronchisepticaand pages 23-25, chamorro2023bordetellabronchisepticaand pages 11-13) |
| GO Biological Process | GO:0032740 | Positive regulation of interleukin-17 production; key Th17-associated protective response (chamorro2023bordetellabronchisepticaand pages 23-25, caulfield2023generatingenhancedmucosal pages 3-4, church2025nasalimmunizationwith pages 14-15) |
| GO Biological Process | GO:0002250 | Adaptive immune response; humoral and cellular immunity required for clearance (chamorro2023bordetellabronchisepticaand pages 23-25, chamorro2023bordetellabronchisepticaand pages 11-13) |
| GO Biological Process | GO:0002449 | Lymphocyte mediated immunity; includes Th1/Th17 responses critical in pertussis |
| GO Biological Process | GO:0071723 | Cellular response to lipopolysaccharide; relevant to LOS/TLR4 signaling (chamorro2023bordetellabronchisepticaand pages 16-18) |
| UBERON | UBERON:0001004 | Respiratory system; primary affected body system |
| UBERON | UBERON:0002048 | Lung; major site of lower respiratory complications |
| UBERON | UBERON:0001737 | Larynx; contributes to inspiratory whoop physiology |
| UBERON | UBERON:0003126 | Trachea; important site of ciliated epithelial colonization/damage (colak2023bordetellapertussisand pages 1-2) |
| UBERON | UBERON:0002185 | Bronchus; major colonization site for *B. pertussis* (colak2023bordetellapertussisand pages 1-2) |
| UBERON | UBERON:0001706 | Nasopharynx; relevant site of colonization and transmission |
| UBERON | UBERON:0001728 | Nasal cavity; key mucosal site targeted by next-generation vaccines (chamorro2023bordetellabronchisepticaand pages 23-25, rudi2024useofmucosally pages 10-13) |
| UBERON | UBERON:0006075 | Ciliated epithelium of tracheobronchial tree; target of adhesins and TCT-mediated injury |
| CL | CL:0000895 | Macrophage; target of ACT and FHA-mediated immunomodulation (chamorro2023bordetellabronchisepticaand pages 13-15, chamorro2023bordetellabronchisepticaand pages 16-18) |
| CL | CL:0000097 | Mast cell; relevant to airway inflammation and mucosal responses |
| CL | CL:0000775 | Neutrophil; key effector cell whose recruitment is impaired by PT (chamorro2023bordetellabronchisepticaand pages 16-18, ernst2022novelstrategiesto pages 12-13) |
| CL | CL:0000451 | Dendritic cell; involved in Th1/Th17 priming (chamorro2023bordetellabronchisepticaand pages 16-18, chamorro2023bordetellabronchisepticaand pages 13-15) |
| CL | CL:0000624 | CD4-positive, alpha-beta T cell; source of Th1/Th17 and TRM responses (chamorro2023bordetellabronchisepticaand pages 23-25, caulfield2023generatingenhancedmucosal pages 3-4, church2025nasalimmunizationwith pages 14-15) |
| MAXO | MAXO:0001001 | Antibiotic administration; overarching treatment class for pertussis therapy |
| MAXO | MAXO:0000474 | Vaccination; primary preventive intervention |
| MAXO | MAXO:0000260 | Maternal vaccination; used in pregnancy to protect young infants (regan2023maternalpertussisvaccination pages 1-2, regan2023maternalpertussisvaccination pages 7-8) |
| MAXO | MAXO:0000127 | Supportive care; hydration, oxygen, monitoring, respiratory support when severe (chamorro2023bordetellabronchisepticaand pages 2-3) |
| MAXO | MAXO:0000058 | Intensive care management; relevant for critical infant pertussis |
| MAXO | MAXO:0000014 | Mechanical ventilation; severe respiratory failure support |
| CHEBI | CHEBI:2955 | Azithromycin; first-line macrolide used for treatment/post-exposure prophylaxis (ernst2022novelstrategiesto pages 2-5, chamorro2023bordetellabronchisepticaand pages 2-3) |
| CHEBI | CHEBI:42355 | Clarithromycin; macrolide option for pertussis treatment (ernst2022novelstrategiesto pages 2-5) |
| CHEBI | CHEBI:42355? | Erythromycin; classic first-line macrolide for pertussis treatment, also studied against MRBp (ernst2022novelstrategiesto pages 2-5, jiang2024theeffectof pages 1-5, jiang2024theeffectof pages 8-10) |
| CHEBI | CHEBI:8345 | Sulfamethoxazole; component of TMP-SMX alternative therapy when macrolides cannot be used |
| CHEBI | CHEBI:45924 | Trimethoprim; component of TMP-SMX alternative therapy |
| CHEBI | CHEBI:33281 | Oxygen; supportive treatment for hypoxemia/apnea in severe disease |
| NCBI Taxonomy | NCBITaxon:520 | *Bordetella pertussis*; primary infectious agent causing classic pertussis |
| Open Targets / Disease Ontology context | No associated targets reported | Open Targets search found pertussis under MONDO but no disease-target associations, consistent with pathogen-driven rather than host monogenic etiology (OpenTargets Search: pertussis,whooping cough) |


*Table: This table compiles key disease identifiers and ontology mappings relevant to pertussis, spanning diagnosis, phenotypes, anatomy, biology, treatments, and drugs. It is useful as a quick reference for disease knowledge base curation and ontology annotation.*

### Synonyms and Alternative Names

Common synonyms include: whooping cough, 100-day cough, tussis convulsiva, and Bordetella pertussis infection.

### Data Source

Information is derived from aggregated disease-level resources including WHO surveillance data, CDC reports, systematic reviews, and peer-reviewed literature, rather than individual patient EHR data.

---

## 2. Etiology

### Disease Causal Factors

Pertussis is caused exclusively by infection with *Bordetella pertussis*, a small Gram-negative coccobacillus (0.8 µm × 0.4 µm) that colonizes the ciliated epithelium of the trachea and bronchi (colak2023bordetellapertussisand pages 1-2, ifill2023lipidamodifications pages 18-25). Transmission occurs via respiratory droplets through sneezing and severe coughing, with possible transmission from asymptomatic individuals (chamorro2023bordetellabronchisepticaand pages 2-3). The pathogen produces a variety of antigenic compounds that individually or simultaneously damage host cells (colak2023bordetellapertussisand pages 1-2).

### Risk Factors

**Age:** Infants under one year are at the highest risk of severe disease and mortality, with approximately 3% mortality in neonates (ifill2023lipidamodifications pages 18-25). Among infants under 6 months, 12.9% of pertussis cases required hospital admission, 4.8% required ICU admission, and 1.6% resulted in death in an Australian cohort study (regan2023maternalpertussisvaccination pages 5-6).

**Vaccination status:** Unvaccinated individuals face the highest risk for infection, hospitalization, and death (wang2025resurgenceofpertussis pages 5-7). Waning vaccine immunity, particularly from acellular pertussis vaccines, leaves adolescents and adults susceptible to infection and capable of transmitting the pathogen to vulnerable infants (wang2025resurgenceofpertussis pages 2-4, caulfield2023generatingenhancedmucosal pages 4-5).

**Environmental/behavioral:** Household contact with infected individuals, lack of maternal vaccination during pregnancy, and low community vaccine coverage are important risk factors (wang2025resurgenceofpertussis pages 5-7).

### Protective Factors

**Vaccination:** Both whole-cell (wP) and acellular (aP) pertussis vaccines significantly reduce disease incidence and severity. Natural infection provides 4–20 years of immunity (wang2025resurgenceofpertussis pages 4-5).

**Maternal vaccination:** Maternal Tdap vaccination at approximately 28 weeks' gestation provides 70.4% effectiveness in infants under 2 months and 65.1% effectiveness in infants under 6 months against notified pertussis infection (regan2023maternalpertussisvaccination pages 5-6, regan2023maternalpertussisvaccination pages 1-2).

---

## 3. Phenotypes

### Clinical Stages and Symptoms

Pertussis progresses through three classic stages spanning up to 12 weeks (ifill2023lipidamodifications pages 18-25):

**Catarrhal stage (1–2 weeks):** Presents with mild respiratory symptoms resembling a common cold, including rhinorrhea, mild cough, and low-grade fever (HP:0001945). This is the most infectious period (ifill2023lipidamodifications pages 18-25).

**Paroxysmal stage (up to 8 weeks):** Characterized by intense paroxysmal coughing episodes (HP:0012735) followed by the inspiratory "whoop" (HP:0031247), post-tussive vomiting (HP:0033847), apnea (HP:0002105), and cyanosis (HP:0000961) (chamorro2023bordetellabronchisepticaand pages 2-3, ifill2023lipidamodifications pages 18-25).

**Convalescent stage (average 4 weeks):** Gradual reduction in cough intensity and frequency, though symptoms may persist for months depending on disease severity and comorbidities (ifill2023lipidamodifications pages 18-25).

### Severity by Age

In children, pertussis is typically life-threatening and severe. Teenagers and adults present with milder disease, ranging from asymptomatic carriage to chronic persistent cough (chamorro2023bordetellabronchisepticaand pages 2-3). Severe complications including seizures (HP:0001250), encephalopathy, and pneumonia (HP:0002205) can occur across age groups but are most common in infants (ernst2022novelstrategiesto pages 1-2).

### Laboratory Abnormalities

Leukocytosis (HP:0001974) is a hallmark laboratory finding, particularly in severe infant disease, and is strongly associated with pertussis toxin activity and poor outcomes (ernst2022novelstrategiesto pages 1-2).

### Quality of Life Impact

Pertussis causes significant functional impairment during the paroxysmal stage, with prolonged nocturnal coughing causing sleep disturbance (HP:0002360), exhaustion, rib fractures in adults, and inability to perform daily activities for weeks.

---

## 4. Genetic/Molecular Information

### Pathogen Genomics (Not Host Genetics)

Pertussis is an infectious disease; causal human genetic variants are not applicable. However, pathogen evolution plays a critical role in disease dynamics.

**Pathogen genetic evolution:** The transition from ptxP1 to ptxP3 allele in the pertussis toxin promoter has been identified as a major evolutionary event, resulting in increased toxin production and enhanced respiratory tract colonization (wang2025resurgenceofpertussis pages 2-4). Pertactin (PRN) deletions and variations, as well as filamentous hemagglutinin (FHA) loss, represent vaccine-driven selection events in circulating strains (wang2025resurgenceofpertussis pages 2-4, chamorro2023bordetellabronchisepticaand pages 33-33). Additionally, fimbriae 2 (FIM2)-negative and pertactin-negative strains have been identified in France and other countries (chamorro2023bordetellabronchisepticaand pages 2-3).

**Macrolide resistance:** Macrolide-resistant *B. pertussis* (MRBp) strains have emerged globally, with prevalence exceeding 95% of isolates in China and up to 50% in Chinese hospital settings (jiang2024theeffectof pages 8-10, chamorro2023bordetellabronchisepticaand pages 2-3). Resistance rates remain negligible in the USA, UK, and Finland (chamorro2023bordetellabronchisepticaand pages 2-3).

---

## 5. Environmental Information

### Infectious Agent

*Bordetella pertussis* is the sole causative agent. It belongs to the genus *Bordetella*, which comprises 16 species. Related species include *B. parapertussis* (can cause milder whooping cough) and *B. bronchiseptica* (primarily a veterinary pathogen) (chamorro2023bordetellabronchisepticaand pages 2-3).

### Transmission Dynamics

Pertussis is transmitted via airborne respiratory droplets from sneezing and coughing. It is highly contagious, with secondary attack rates of up to 80–90% in susceptible household contacts. Adults and adolescents with waning immunity serve as the primary reservoir for transmission to vulnerable infants (ifill2023lipidamodifications pages 18-25, chamorro2023bordetellabronchisepticaand pages 2-3).

---

## 6. Mechanism / Pathophysiology

### Virulence Factors

The following table summarizes the major virulence determinants of *B. pertussis*:

| Virulence factor | Molecular weight | Function / mechanism | Role in pathogenesis | Vaccine relevance |
|---|---:|---|---|---|
| Pertussis toxin (PT) | ~117 kDa | AB-type exotoxin with S1 enzymatic subunit and S2-S5 binding subunits; ADP-ribosylates inhibitory Gα proteins, disrupting GPCR signaling and downstream cAMP regulation (colak2023bordetellapertussisand pages 2-3, ernst2022novelstrategiesto pages 1-2) | Major B. pertussis-specific toxin; promotes respiratory colonization, suppresses chemokine release and neutrophil recruitment, delays antibody-mediated clearance, and is associated with leukocytosis, hyperinsulinemia, histamine sensitization, and severe disease/poor outcomes (chamorro2023bordetellabronchisepticaand pages 16-18, chamorro2023bordetellabronchisepticaand pages 15-16, ernst2022novelstrategiesto pages 1-2, ernst2022novelstrategiesto pages 12-13) | Core antigen in acellular pertussis vaccines; major correlate/target of vaccine-induced antibodies; also a target for next-generation therapeutics and live-attenuated vaccine detoxification strategies such as BPZE1 (chamorro2023bordetellabronchisepticaand pages 20-22, colak2023bordetellapertussisand pages 3-5, ernst2022novelstrategiesto pages 2-5, chamorro2023bordetellabronchisepticaand pages 23-25) |
| Adenylate cyclase toxin (ACT/CyaA, AC-Hly) | Not specified in retrieved evidence | Toxin that enters/acts on phagocytes and elevates intracellular cAMP; inhibits phagocytosis and opsonization, induces macrophage apoptosis, has hemolytic/cytotoxic activity, and can disrupt epithelial tight junctions (colak2023bordetellapertussisand pages 2-3, chamorro2023bordetellabronchisepticaand pages 16-18, ernst2022novelstrategiesto pages 1-2) | Protects bacteria from innate immune killing, impairs neutrophil, dendritic-cell, and macrophage function, and contributes to invasion/persistence in the respiratory tract (colak2023bordetellapertussisand pages 2-3, chamorro2023bordetellabronchisepticaand pages 16-18, ernst2022novelstrategiesto pages 1-2) | Not a standard component of current acellular vaccines, but an important candidate antigen/target for next-generation vaccines and antibody-based protection strategies (chamorro2023bordetellabronchisepticaand pages 23-25, colak2023bordetellapertussisand pages 3-5) |
| Filamentous hemagglutinin (FHA) | ~220 kDa | Filamentous surface adhesin mediating attachment to ciliated respiratory epithelium; also modulates host responses by inhibiting NF-κB signaling in macrophages and epithelial cells (chamorro2023bordetellabronchisepticaand pages 13-15, colak2023bordetellapertussisand pages 2-3, chamorro2023bordetellabronchisepticaand pages 15-16) | Critical for initiation of colonization and tight adhesion in the upper airway; suppresses early inflammation and cell recruitment, aiding persistence (chamorro2023bordetellabronchisepticaand pages 13-15, chamorro2023bordetellabronchisepticaand pages 15-16) | Common antigen in acellular vaccines and serologic assays; antigen loss/variation has been implicated in pathogen adaptation and vaccine-pressure discussions (chamorro2023bordetellabronchisepticaand pages 20-22, wang2025resurgenceofpertussis pages 10-11) |
| Pertactin (PRN) | ~69 kDa | Outer-membrane autotransporter adhesin enabling attachment to host cells; contributes to membrane interactions and resistance to host clearance (colak2023bordetellapertussisand pages 2-3, ifill2023lipidamodifications pages 225-228, chamorro2023bordetellabronchisepticaand pages 15-16) | Supports adherence, inflammation, cell recruitment, shedding/transmission, and resistance to neutrophil-mediated clearance (ifill2023lipidamodifications pages 225-228, chamorro2023bordetellabronchisepticaand pages 15-16) | Major antigen in many acellular vaccines; pertactin-deficient strains are a key example of vaccine-driven evolution and resurgence-associated adaptation (chamorro2023bordetellabronchisepticaand pages 20-22, wang2025resurgenceofpertussis pages 2-4, caulfield2023generatingenhancedmucosal pages 4-5, chamorro2023bordetellabronchisepticaand pages 33-33) |
| Fimbriae (FIM2/FIM3) | Not specified in retrieved evidence | Surface appendages mediating initial interactions with respiratory epithelial cells and contributing to tight adhesion with FHA (chamorro2023bordetellabronchisepticaand pages 13-15, chamorro2023bordetellabronchisepticaand pages 15-16) | Help establish colonization of ciliated airway surfaces and support persistence in the respiratory tract (chamorro2023bordetellabronchisepticaand pages 13-15, chamorro2023bordetellabronchisepticaand pages 15-16) | Included in some multicomponent acellular vaccines; fimbrial variation/negative strains have been described among circulating isolates (chamorro2023bordetellabronchisepticaand pages 20-22, chamorro2023bordetellabronchisepticaand pages 2-3) |
| Tracheal cytotoxin (TCT) | Not specified in retrieved evidence | Peptidoglycan-derived cytotoxin that damages ciliated respiratory cells and disrupts epithelial/tight-junction integrity (chamorro2023bordetellabronchisepticaand pages 13-15, ernst2022novelstrategiesto pages 1-2) | Causes ciliary injury and epithelial damage, promoting local tissue dysfunction and aiding colonization/pathology in the airway (chamorro2023bordetellabronchisepticaand pages 13-15, ernst2022novelstrategiesto pages 1-2) | Not part of licensed acellular vaccines; detoxification/inactivation of TCT is part of the attenuation strategy for BPZE1 live vaccine development (chamorro2023bordetellabronchisepticaand pages 23-25) |
| Dermonecrotic toxin (DNT) | Not specified in retrieved evidence | Toxin associated with tissue injury; interacts functionally with TCT and LOS and contributes to virulence programs regulated by BvgAS (colak2023bordetellapertussisand pages 2-3) | Contributes to respiratory tract tissue damage and overall virulence (colak2023bordetellapertussisand pages 2-3) | Not a standard antigen in current acellular vaccines; inactivated in BPZE1 as part of live-attenuated vaccine design (chamorro2023bordetellabronchisepticaand pages 23-25) |
| Lipooligosaccharide (LOS) | Not specified in retrieved evidence | Endotoxin-like outer-membrane glycolipid; activates TLR4 and cytokine release (including IL-8 and TNF-α), though with weaker stimulation than B. bronchiseptica LPS; terminal trisaccharide contributes to defense evasion (chamorro2023bordetellabronchisepticaand pages 18-20, chamorro2023bordetellabronchisepticaand pages 16-18) | Required for efficient nasal colonization in mice; shapes inflammatory tone and neutrophil recruitment, contributing to colonization and persistence while limiting clearance (chamorro2023bordetellabronchisepticaand pages 18-20, chamorro2023bordetellabronchisepticaand pages 16-18) | Not used as a purified routine vaccine antigen, but naturally present in OMV-based vaccine platforms where it contributes adjuvanticity/immunogenicity (colak2023bordetellapertussisand pages 1-2, colak2023bordetellapertussisand pages 9-10) |
| Type III secretion system (T3SS) | Multi-protein apparatus; no single MW | Secretion apparatus that injects effectors such as BteA and modulates host signaling, including VIP/VPAC2 pathways; suppresses IFN-γ responses and promotes persistence (chamorro2023bordetellabronchisepticaand pages 13-15, chamorro2023bordetellabronchisepticaand pages 18-20, first2023bordetellaspp.utilize pages 1-2) | Supports immune evasion, lower-respiratory colonization, persistence, and lung pathology modulation (chamorro2023bordetellabronchisepticaand pages 13-15, chamorro2023bordetellabronchisepticaand pages 18-20, first2023bordetellaspp.utilize pages 1-2) | Not a component of current vaccines but a potential therapeutic and next-generation vaccine target because of its role in immune manipulation and persistence (chamorro2023bordetellabronchisepticaand pages 23-25, first2023bordetellaspp.utilize pages 1-2) |


*Table: This table summarizes the major Bordetella pertussis virulence determinants, their known mechanisms, roles in disease, and relevance to current or emerging vaccine strategies. It is useful for linking pathogenesis to diagnostics, therapeutic targeting, and vaccine design.*

### BvgAS Two-Component Regulatory System

All major virulence factors are regulated by the BvgAS two-component system, comprising the sensor kinase BvgS and response regulator BvgA. This system functions as a molecular rheostat controlling virulence gene expression across three phenotypic phases: Bvg+ (virulent, virulence-activated genes expressed), Bvg- (avirulent), and Bvgi (intermediate) (chamorro2023bordetellabronchisepticaand pages 13-15, colak2023bordetellapertussisand pages 2-3). Phosphorylated BvgA activates transcription of genes encoding adhesins (FHA, FIM, PRN), toxins (PT, ACT, DNT), and the T3SS (colak2023bordetellapertussisand pages 2-3).

### Pertussis Toxin (PT) – Central Virulence Factor

PT is a 117-kDa AB-type exotoxin with unique importance in pertussis pathogenesis. The S1 subunit ADP-ribosylates inhibitory Gαi subunits of G-protein coupled receptors, disrupting cAMP signaling in target cells (ernst2022novelstrategiesto pages 1-2). PT inhibits chemokine release and neutrophil recruitment, delays antibody-mediated bacterial clearance, enables intracellular macrophage infection, and produces systemic effects including leukocytosis, hyperinsulinemia, and histamine sensitivity (chamorro2023bordetellabronchisepticaand pages 16-18, chamorro2023bordetellabronchisepticaand pages 15-16). PT is uniquely expressed in *B. pertussis*; related species carry the gene but cannot transcribe it due to promoter mutations (chamorro2023bordetellabronchisepticaand pages 15-16).

### Adenylate Cyclase Toxin (ACT/CyaA)

ACT enters phagocytes and elevates intracellular cAMP, inhibiting phagocytosis and opsonization, inducing macrophage apoptosis, and disrupting epithelial tight junctions (chamorro2023bordetellabronchisepticaand pages 16-18, ernst2022novelstrategiesto pages 1-2).

### Type III Secretion System (T3SS)

The T3SS injects effector proteins (including BteA) into host cells and modulates VIP/VPAC2 signaling pathways, promoting lower respiratory tract colonization and persistence (first2023bordetellaspp.utilize pages 1-2). VPAC2-deficient mice showed decreased bacterial burden, and VPAC2 antagonists decreased lung pathology in mouse models, suggesting this pathway as a potential therapeutic target (first2023bordetellaspp.utilize pages 1-2).

### Immune Response and Evasion

*B. pertussis* initially induces IL-10 production and suppresses IFN-γ responses, creating an immunosuppressive state (chamorro2023bordetellabronchisepticaand pages 13-15). Optimal protective immunity requires coordinated Th1 (IFN-γ) and Th17 (IL-17) cellular responses (chamorro2023bordetellabronchisepticaand pages 23-25, chamorro2023bordetellabronchisepticaand pages 11-13). Tissue-resident memory (TRM) CD4+ T cells in nasal tissue expand IL-17+ responses upon secondary infection, recruiting Siglec F+ neutrophils for pathogen clearance (caulfield2023generatingenhancedmucosal pages 3-4). IgA antibodies produced during natural infection can reduce bacterial adherence to ciliated epithelium (caulfield2023generatingenhancedmucosal pages 3-4). B. pertussis-specific IgG antibodies appear 4–6 weeks post-infection when bacteria are nearly cleared (chamorro2023bordetellabronchisepticaand pages 11-13).

---

## 7. Anatomical Structures Affected

**Primary organ:** Respiratory system (UBERON:0001004), specifically the trachea (UBERON:0003126) and bronchi (UBERON:0002185), where *B. pertussis* attaches to ciliated epithelium (colak2023bordetellapertussisand pages 1-2).

**Upper respiratory tract:** Nasopharynx (UBERON:0001706) and nasal cavity (UBERON:0001728) are important colonization and transmission sites (chamorro2023bordetellabronchisepticaand pages 23-25).

**Secondary involvement:** Lungs (UBERON:0002048) in cases complicated by pneumonia; central nervous system in cases of encephalopathy.

**Cell types targeted:** Ciliated respiratory epithelial cells (primary colonization target), macrophages (CL:0000895; targeted by ACT and FHA), neutrophils (CL:0000775; recruitment impaired by PT), dendritic cells (CL:0000451; targeted by ACT), and CD4+ T cells (CL:0000624; critical for Th1/Th17 protective responses) (chamorro2023bordetellabronchisepticaand pages 13-15, chamorro2023bordetellabronchisepticaand pages 16-18).

---

## 8. Temporal Development

### Onset

Pertussis can occur at any age but is most severe in neonates and infants under 6 months. The incubation period is 7–10 days. Onset is typically insidious, with the catarrhal stage mimicking a common cold (ifill2023lipidamodifications pages 18-25).

### Progression

The disease follows a predictable three-stage course over up to 12 weeks: catarrhal (1–2 weeks) → paroxysmal (up to 8 weeks) → convalescent (average 4 weeks) (ifill2023lipidamodifications pages 18-25). The disease is self-limited but may last several months in severe cases.

### Patterns

Pertussis exhibits an endemic pattern with epidemic peaks every 3–5 years (colak2023bordetellapertussisand pages 1-2). The 2023–2024 global resurgence has been particularly dramatic, with Europe experiencing an increase from 4.7 to 104.4 cases per million between 2022 and 2023 (wang2025resurgenceofpertussis pages 1-2).

---

## 9. Inheritance and Population

### Epidemiology

**Global burden:** Approximately 24.1 million pertussis cases and 160,700 deaths occur annually worldwide in children younger than 5 years (ifill2023lipidamodifications pages 18-25, ernst2022novelstrategiesto pages 1-2). The WHO recorded 151,074 notified cases in 2018 despite 86% global vaccination coverage, making pertussis the worst-controlled childhood vaccine-preventable disease (chamorro2023bordetellabronchisepticaand pages 2-3). The global incidence rate was approximately 23.6 cases per million in 2023 (wang2025resurgenceofpertussis pages 2-4).

**2023–2024 resurgence:** Large-scale global outbreaks have been reported since 2023, with significant increases in the United Kingdom, France, Denmark, the United States, Australia, and multiple low- and middle-income countries including China, Afghanistan, and Indonesia (wang2025resurgenceofpertussis pages 1-2). Contributing factors include genetic mutations in *B. pertussis*, waning vaccine immunity, COVID-19 pandemic disruptions to vaccination programs, disease cyclicity, and improved diagnostic awareness (wang2025resurgenceofpertussis pages 1-2, wang2025resurgenceofpertussis pages 8-9).

**Age distribution:** The age profile has shifted from predominantly infants and young children to now including significant disease burden in adolescents and adults, with patients aged ≥14 years accounting for 67% of total incidence in some surveys (colak2023bordetellapertussisand pages 1-2). Adolescents aged 10–19 years showed the highest incidence in six European countries during the 2023–2024 resurgence (wang2025resurgenceofpertussis pages 2-4).

**Inheritance:** Not applicable (infectious disease, not a genetic disorder).

---

## 10. Diagnostics

### Clinical Criteria

Clinical diagnosis is the starting point, based on characteristic paroxysmal cough lasting ≥2 weeks, post-tussive vomiting, and inspiratory whoop. Pertussis is commonly underdiagnosed in adults due to milder or atypical clinical presentations (chamorro2023bordetellabronchisepticaand pages 2-3, wang2025resurgenceofpertussis pages 8-9).

### Laboratory Tests

**PCR assays:** The fastest and most sensitive method for laboratory confirmation. Various target genes are used to differentiate *Bordetella* species, including IS481, IS1001, hIS1001, IS1002, ptxS1, ptxA-Pr, fla, and BP3385 (chamorro2023bordetellabronchisepticaand pages 5-7).

**Microbiological culture:** Highly specific but lower sensitivity and time-consuming. Allows colony subtyping and antimicrobial susceptibility testing (chamorro2023bordetellabronchisepticaand pages 5-7).

**Serology:** Detects specific antibodies (anti-PT IgG, anti-FHA) with high sensitivity and specificity, but appears positive late in infection. Useful for retrospective diagnosis in adults (chamorro2023bordetellabronchisepticaand pages 5-7).

### Laboratory Abnormalities

Marked leukocytosis (white blood cell count >20,000/µL) with lymphocyte predominance is a characteristic finding in severe infant pertussis and is directly attributable to pertussis toxin effects on leukocyte trafficking (ernst2022novelstrategiesto pages 1-2).

---

## 11. Outcome/Prognosis

### Mortality

Neonates experience the most severe disease with approximately 3% mortality (ifill2023lipidamodifications pages 18-25). Globally, approximately 160,700 pertussis-related deaths occur annually in children under 5 years (ifill2023lipidamodifications pages 18-25, ernst2022novelstrategiesto pages 1-2). Mortality rates are substantially lower in adolescents and adults. In an Australian cohort, 1.6% of pertussis cases in infants under 6 months resulted in death (regan2023maternalpertussisvaccination pages 5-6).

### Complications

Severe complications include pneumonia (HP:0002205), encephalopathy, seizures (HP:0001250), apnea (HP:0002105), and pulmonary hypertension, particularly in infants (ernst2022novelstrategiesto pages 1-2). Hyperleukocytosis is a prognostic marker for severe disease and poor outcomes (ernst2022novelstrategiesto pages 1-2).

### Prognostic Factors

Age (younger age = worse prognosis), vaccination status, pertussis toxin levels (PT is strongly associated with severe symptoms and poor outcomes; strains lacking PT cause only mild symptoms), and degree of leukocytosis are key prognostic indicators (ernst2022novelstrategiesto pages 1-2).

---

## 12. Treatment

### Pharmacotherapy

**Macrolide antibiotics** are the first-line treatment (MAXO:0001001): azithromycin (CHEBI:2955), clarithromycin, and erythromycin. However, antibiotics only reduce symptoms if administered within the first two weeks of infection (during the catarrhal stage), which rarely occurs due to late diagnosis. Antibiotics eliminate *B. pertussis* and prevent transmission but have limited therapeutic benefit after the paroxysmal stage begins (ernst2022novelstrategiesto pages 2-5, chamorro2023bordetellabronchisepticaand pages 2-3).

**Macrolide resistance** is an emerging concern: over 95% of prevailing *B. pertussis* isolates in China are macrolide-resistant, though rates remain negligible in Western countries (jiang2024theeffectof pages 8-10, chamorro2023bordetellabronchisepticaand pages 2-3). Sub-inhibitory concentrations of erythromycin may still reduce virulence of MRBp by affecting the BvgAS regulatory system, biofilm formation, and virulence factor expression (jiang2024theeffectof pages 1-5, jiang2024theeffectof pages 8-10).

**Alternative agents:** Trimethoprim-sulfamethoxazole (TMP-SMX) when macrolides are contraindicated.

### Supportive Care

Supportive care (MAXO:0000127) includes hydration, oxygen supplementation for hypoxemia, and monitoring. Severe infant cases may require intensive care (MAXO:0000058) and mechanical ventilation (MAXO:0000014) (chamorro2023bordetellabronchisepticaand pages 2-3).

### Novel Therapeutic Approaches

**Pertussis toxin inhibitors:** Multiple pharmacological strategies are under investigation, including chaperone inhibitors, human peptides (defensins), small molecule inhibitors, and humanized neutralizing antibodies targeting PT (ernst2022novelstrategiesto pages 2-5).

**VPAC2 antagonists:** Preclinical research demonstrates that VPAC2 antagonists decrease lung pathology in mouse models, targeting the VIP/VPAC2 signaling pathway exploited by *Bordetella* through the T3SS (first2023bordetellaspp.utilize pages 1-2).

**Intravenous pertussis immune globulin:** Evaluated in a Phase 3 trial (NCT00004422) for severe childhood pertussis infection.

---

## 13. Prevention

### Primary Prevention – Vaccination

Vaccination (MAXO:0000474) remains the cornerstone of pertussis prevention. Two main vaccine types are in use:

| Vaccine Type | Components | Immune Response Profile (Th1/Th2/Th17) | Duration of Protection | Advantages | Limitations | Current Use |
|---|---|---|---|---|---|---|
| Whole-cell pertussis vaccine (wP/DTwP) | Killed whole *B. pertussis* cells, typically combined with diphtheria and tetanus toxoids | Stronger Th1/Th17-polarized cellular immunity; more balanced humoral/cellular response than acellular vaccines (chamorro2023bordetellabronchisepticaand pages 20-22, colak2023bordetellapertussisand pages 9-10, colak2023bordetellapertussisand pages 3-5, chamorro2023bordetellabronchisepticaand pages 23-25) | Longer than acellular vaccines; cited protection roughly 7-20 years after natural infection and generally more durable priming than aP (chamorro2023bordetellabronchisepticaand pages 20-22, wang2025resurgenceofpertussis pages 4-5) | Better durability; stronger mucosal-relevant cellular priming; associated with lower later pertussis risk when used for priming (chamorro2023bordetellabronchisepticaand pages 20-22, chamorro2023bordetellabronchisepticaand pages 23-25, church2025nasalimmunizationwith pages 14-15) | Higher reactogenicity, historically including fever and neurologic adverse reactions; less acceptable in many high-income settings (chamorro2023bordetellabronchisepticaand pages 23-25, colak2023bordetellapertussisand pages 3-5) | Still widely used in many low- and middle-income countries in DTwP-containing EPI schedules (wang2025resurgenceofpertussis pages 5-7, wang2025resurgenceofpertussis pages 4-5) |
| Acellular pertussis vaccine (aP/DTaP) | Purified 1-5 antigens, commonly PT, FHA, PRN, FIM2/FIM3, combined with diphtheria/tetanus toxoids | More Th2-skewed, especially with alum adjuvant; less effective induction of Th1/Th17 and mucosal memory than wP (chamorro2023bordetellabronchisepticaand pages 23-25, chamorro2023bordetellabronchisepticaand pages 20-22, colak2023bordetellapertussisand pages 1-2, colak2023bordetellapertussisand pages 3-5, caulfield2023generatingenhancedmucosal pages 4-5) | Waning immunity is substantial; efficacy cited around 85% after 6 doses with decline of ~11.7% annually; protection often 4-12 years (chamorro2023bordetellabronchisepticaand pages 20-22, wang2025resurgenceofpertussis pages 5-7) | Lower reactogenicity; safer and better tolerated; standard product in many high-income countries (chamorro2023bordetellabronchisepticaand pages 20-22, colak2023bordetellapertussisand pages 3-5, wang2025resurgenceofpertussis pages 4-5) | Rapid waning; does not reliably prevent nasal colonization or transmission; may contribute to vaccine-driven selection of antigen-deficient strains such as PRN-negative isolates (chamorro2023bordetellabronchisepticaand pages 23-25, colak2023bordetellapertussisand pages 1-2, caulfield2023generatingenhancedmucosal pages 4-5, chamorro2023bordetellabronchisepticaand pages 33-33) | Routine infant immunization in many high-income countries, usually as DTaP-containing combination vaccines (chamorro2023bordetellabronchisepticaand pages 20-22, wang2025resurgenceofpertussis pages 5-7, wang2025resurgenceofpertussis pages 4-5) |
| Tdap booster | Reduced-antigen acellular booster containing tetanus toxoid, reduced diphtheria toxoid, and acellular pertussis antigens | Booster humoral response but still based on acellular platform; protection remains less durable than wP-primed immunity (chamorro2023bordetellabronchisepticaand pages 20-22, wang2025resurgenceofpertussis pages 5-7) | Initial effectiveness about 85%, decreasing by ~12% annually in cited review evidence (wang2025resurgenceofpertussis pages 5-7) | Useful for adolescent/adult boosting and maternal immunization; reduces infant risk via transplacental antibody transfer during pregnancy (wang2025resurgenceofpertussis pages 5-7, regan2023maternalpertussisvaccination pages 1-2, regan2023maternalpertussisvaccination pages 6-7) | Waning protection; does not fully solve transmission or colonization; repeated boosting may be needed (wang2025resurgenceofpertussis pages 5-7, caulfield2023generatingenhancedmucosal pages 4-5) | Used for childhood/adolescent boosters, adult boosters in some countries, and maternal vaccination in pregnancy (chamorro2023bordetellabronchisepticaand pages 20-22, wang2025resurgenceofpertussis pages 5-7, regan2023maternalpertussisvaccination pages 1-2) |
| OMV-based vaccines | Outer membrane vesicles containing native immunogenic structures including toxins, adhesins, and LPS/LOS-associated components | More balanced response than aP; induces innate plus adaptive immunity and broader IgG subclass patterns resembling wP more than aP (colak2023bordetellapertussisand pages 1-2, colak2023bordetellapertussisand pages 9-10, colak2023bordetellapertussisand pages 11-12) | Not yet established in humans; promising preclinical durability and protection in animal/preclinical studies (colak2023bordetellapertussisand pages 1-2, colak2023bordetellapertussisand pages 9-10) | Native antigen presentation; potentially equivalent bacterial protection with milder inflammatory responses than wP; promising next-generation platform (colak2023bordetellapertussisand pages 1-2, colak2023bordetellapertussisand pages 9-10) | Manufacturing standardization challenges related to strain choice, culture conditions, extraction, and purification; no established routine human use yet (colak2023bordetellapertussisand pages 1-2, colak2023bordetellapertussisand pages 9-10) | Experimental/preclinical development; not standard of care (colak2023bordetellapertussisand pages 1-2, colak2023bordetellapertussisand pages 9-10, colak2023bordetellapertussisand pages 11-12) |
| BPZE1 live attenuated vaccine | Live attenuated *B. pertussis* strain with inactivated major toxins including PT, TCT, and DNT | Induces IgG, IgA, memory B cells, and a Th1-type response; broader antibody specificity and mucosal-relevant immunity than standard aP vaccines (chamorro2023bordetellabronchisepticaand pages 23-25) | Human duration still under study; preclinical single-dose protection reported in mice (chamorro2023bordetellabronchisepticaand pages 23-25) | Nasal administration; potential to induce mucosal immunity and improve protection against infection/transmission, not just disease (chamorro2023bordetellabronchisepticaand pages 23-25) | Investigational; efficacy, long-term durability, and broader deployment remain under evaluation (chamorro2023bordetellabronchisepticaand pages 23-25) | In clinical development; phase 2b cited with controlled human infection work (NCT05461131) (chamorro2023bordetellabronchisepticaand pages 23-25) |
| Intranasal mucosal vaccines | Intranasally delivered aP formulations, live attenuated candidates, or other adjuvanted mucosal platforms | Designed to induce local IgA, IL-17, Th1/Th17 responses, and tissue-resident memory CD4+ T cells in respiratory mucosa (chamorro2023bordetellabronchisepticaand pages 23-25, caulfield2023generatingenhancedmucosal pages 3-4, church2025nasalimmunizationwith pages 14-15, rudi2024useofmucosally pages 10-13) | Human durability not yet fully defined; concept aims for stronger and more persistent anti-colonization immunity than injectable aP (chamorro2023bordetellabronchisepticaand pages 23-25, church2025nasalimmunizationwith pages 14-15) | Best aligned with infection site; may prevent nasal colonization and transmission while also protecting against disease (chamorro2023bordetellabronchisepticaand pages 23-25, chamorro2023bordetellabronchisepticaand pages 25-27) | Mostly investigational; formulation, adjuvant, and safety optimization remain active research areas (chamorro2023bordetellabronchisepticaand pages 23-25, colak2023bordetellapertussisand pages 11-12, church2025nasalimmunizationwith pages 14-15) | Experimental/clinical development; not yet routine public-health use (chamorro2023bordetellabronchisepticaand pages 23-25, colak2023bordetellapertussisand pages 11-12, church2025nasalimmunizationwith pages 14-15) |


*Table: This table compares established and emerging pertussis vaccine platforms across composition, immune profile, durability, strengths, and limitations. It is useful for understanding why current acellular vaccines reduce severe disease yet incompletely prevent transmission, and why mucosal and live-attenuated approaches are being pursued.*

### Vaccination Schedule

The WHO recommends primary DTaP/DTwP vaccination starting at 6 weeks of age, with subsequent doses at 10–14 weeks and 14–18 weeks, followed by a booster dose in the second year of life. Tdap boosters are recommended for adolescents. Maternal Tdap vaccination (MAXO:0000260) during the third trimester (optimal at 28–32 weeks' gestation) is recommended by the WHO since 2015 to protect newborns through transplacental antibody transfer (wang2025resurgenceofpertussis pages 5-7).

### Maternal Vaccination Effectiveness

In a population-based cohort study of 279,418 mother–infant pairs in Australia, maternal dTpa vaccination near 28 weeks' gestation provided 70.4% effectiveness (95% CI: 50.5–82.3) among infants under 2 months, declining to 43.3% (95% CI: 6.8–65.6) at 7–8 months, with protection becoming non-significant after 8 months of age (regan2023maternalpertussisvaccination pages 1-2, regan2023maternalpertussisvaccination pages 6-7).

### Waning Immunity Challenge

Acellular pertussis vaccine efficacy is approximately 85% after 6 doses but decreases by approximately 11.7% annually, with protection lasting 4–12 years compared to 7–20 years for natural infection (chamorro2023bordetellabronchisepticaand pages 20-22). The COVID-19 pandemic further disrupted vaccination coverage, contributing to the 2023–2024 global resurgence (wang2025resurgenceofpertussis pages 1-2).

### Next-Generation Vaccine Strategies

**BPZE1 live attenuated vaccine:** Attenuated by inactivating genes encoding PT, TCT, and DNT. A single nasal dose provides complete protection in mice. In humans, it induces specific IgG, IgA, and memory B cells with a Th1 phenotype. Currently in Phase 2b clinical trials (NCT05461131) using a controlled human infection model (chamorro2023bordetellabronchisepticaand pages 23-25).

**OMV-based vaccines:** Outer membrane vesicles carry native immunogenic structures and trigger both innate and adaptive immune responses. They show promising results in animal models with broader IgG subclass responses than acellular vaccines (colak2023bordetellapertussisand pages 1-2, colak2023bordetellapertussisand pages 9-10).

**Intranasal mucosal vaccines:** Designed to induce local IgA, IL-17, and tissue-resident memory CD4+ T cells at the site of infection, potentially preventing both colonization and transmission (chamorro2023bordetellabronchisepticaand pages 23-25, caulfield2023generatingenhancedmucosal pages 3-4).

### Post-Exposure Prophylaxis

Macrolide antibiotics (particularly azithromycin) are recommended for close contacts of confirmed cases, regardless of vaccination status.

---

## 14. Other Species / Natural Disease

### Comparative Biology

*B. pertussis* is exclusively a human pathogen with no known natural animal reservoir (ifill2023lipidamodifications pages 18-25). However, the closely related *B. bronchiseptica* (NCBITaxon:518) causes respiratory infections across a wide range of mammals, including the canine infectious respiratory disease complex (CIRDC) in dogs (chamorro2023bordetellabronchisepticaand pages 2-3). *B. bronchiseptica* is increasingly implicated in zoonotic human infections and serves as an important comparative model for understanding *Bordetella* pathogenesis (chamorro2023bordetellabronchisepticaand pages 2-3).

### Cross-Species Considerations

While *B. pertussis* infection is restricted to humans, the genus *Bordetella* includes species with zoonotic potential. *B. bronchiseptica* can be transmitted from animals to humans, particularly immunocompromised individuals (chamorro2023bordetellabronchisepticaand pages 2-3).

---

## 15. Model Organisms

### Mouse Models

Mouse models (Mus musculus, NCBITaxon:10090) are widely used for pertussis research, though *B. pertussis* requires much higher bacterial doses to establish infection in mice compared to natural human infection, representing a major limitation (chamorro2023bordetellabronchisepticaand pages 11-13). Mouse models have been valuable for studying nasal cavity infection, catarrhal-stage upper respiratory tract dynamics, neonatal disease with PT-mediated pathology, and vaccine-induced immune responses (caulfield2023generatingenhancedmucosal pages 5-6, caulfield2023generatingenhancedmucosal pages 6-7). VPAC2-knockout mice have been used to demonstrate the role of VIP/VPAC2 signaling in *Bordetella* colonization (first2023bordetellaspp.utilize pages 1-2).

### Baboon (Nonhuman Primate) Models

The baboon model (Papio sp.) provides superior recapitulation of human disease, exhibiting many similarities to human infection in terms of pathogenesis and immune responses (chamorro2023bordetellabronchisepticaand pages 11-13). In baboons, *B. pertussis* infection induces IL-17 secretion and generates long-lasting Th17 and Th1 immune responses persisting at least 24 months (chamorro2023bordetellabronchisepticaand pages 11-13). Baboon studies have been critical for demonstrating that injectable vaccines prevent disease but fail to prevent nasal colonization and transmission, whereas intranasal vaccines can prevent both (chamorro2023bordetellabronchisepticaand pages 25-27).

### *B. bronchiseptica* as Comparative Model

*B. bronchiseptica* naturally colonizes multiple mammalian hosts including mice, rats, swine, and dogs, and serves as a comparative model for understanding *Bordetella* pathogenesis when *B. pertussis* host restriction limits experimentation (chamorro2023bordetellabronchisepticaand pages 11-13).

---

## 16. Active Clinical Trials

Several clinical trials are currently recruiting or active:

- **NCT06827470:** Establishing a Controlled Human Infection Model (CHIM) of pertactin-deficient *B. pertussis* at Dalhousie University, Canada (Phase 1, recruiting, n=60) (NCT06827470 chunk 2)
- **NCT06803524:** 10-year follow-up after single-dose acellular pertussis vaccination at Mahidol University, Thailand (Phase 4, recruiting, n=126) (NCT06803524 chunk 3)
- **NCT05897879:** Impact of bacterial expression and immune response in severity of pertussis at Institut Pasteur (recruiting, n=210)
- **NCT07097012:** Concurrent versus sequential administration of Tdap and RSV vaccines in pregnancy, Canadian Immunization Research Network (Phase 4, recruiting, n=60)
- **NCT06946499:** Phase II/III study of a fully liquid hexavalent DTwP-HepB-IPV-Hib vaccine by LG Chem (recruiting, n=1186)
- **NCT07112144:** Phase III clinical trial of a cell-free DPT combined vaccine by Changchun BCHT Biotechnology (recruiting, n=1650)

---

## Summary

Pertussis remains one of the least controlled vaccine-preventable diseases worldwide despite decades of immunization efforts (chamorro2023bordetellabronchisepticaand pages 2-3). The 2023–2024 global resurgence, driven by waning acellular vaccine immunity, pathogen evolution (ptxP3 allele expansion, pertactin-deficient strains), COVID-19-related vaccination disruptions, and natural disease cyclicity, underscores the urgent need for improved vaccination strategies (wang2025resurgenceofpertussis pages 2-4, wang2025resurgenceofpertussis pages 1-2). Current research priorities include development of mucosal vaccines that can prevent both disease and transmission, controlled human infection models to define correlates of protection, and novel therapeutics targeting pertussis toxin and host-pathogen signaling pathways (chamorro2023bordetellabronchisepticaand pages 23-25, ernst2022novelstrategiesto pages 2-5, first2023bordetellaspp.utilize pages 1-2, NCT06827470 chunk 2).

References

1. (colak2023bordetellapertussisand pages 1-2): Çiğdem Yılmaz Çolak and Burcu Emine Tefon Öztürk. Bordetella pertussis and outer membrane vesicles. Pathogens and Global Health, 117:342-355, Sep 2023. URL: https://doi.org/10.1080/20477724.2022.2117937, doi:10.1080/20477724.2022.2117937. This article has 13 citations and is from a peer-reviewed journal.

2. (ifill2023lipidamodifications pages 18-25): Gyles Anderson Ifill. Lipid a modifications in bordetella pertussis : regulation and function of the lgm locus. Text, Jan 2023. URL: https://doi.org/10.14288/1.0406206, doi:10.14288/1.0406206. This article has 0 citations and is from a peer-reviewed journal.

3. (chamorro2023bordetellabronchisepticaand pages 2-3): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: pertussis,whooping cough): Open Targets Query (pertussis,whooping cough, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (ernst2022novelstrategiesto pages 1-2): Katharina Ernst. Novel strategies to inhibit pertussis toxin. Toxins, 14:187, Mar 2022. URL: https://doi.org/10.3390/toxins14030187, doi:10.3390/toxins14030187. This article has 29 citations.

6. (regan2023maternalpertussisvaccination pages 5-6): Annette K. Regan, Hannah C. Moore, Michael J. Binks, Lisa McHugh, Christopher C. Blyth, Gavin Pereira, Karin Lust, Mohinder Sarna, Ross Andrews, Damien Foo, Paul V. Effler, Stephen Lambert, and Paul Van Buynder. Maternal pertussis vaccination, infant immunization, and risk of pertussis. Pediatrics, Oct 2023. URL: https://doi.org/10.1542/peds.2023-062664, doi:10.1542/peds.2023-062664. This article has 56 citations and is from a highest quality peer-reviewed journal.

7. (chamorro2023bordetellabronchisepticaand pages 16-18): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

8. (ernst2022novelstrategiesto pages 12-13): Katharina Ernst. Novel strategies to inhibit pertussis toxin. Toxins, 14:187, Mar 2022. URL: https://doi.org/10.3390/toxins14030187, doi:10.3390/toxins14030187. This article has 29 citations.

9. (chamorro2023bordetellabronchisepticaand pages 13-15): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

10. (chamorro2023bordetellabronchisepticaand pages 18-20): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

11. (chamorro2023bordetellabronchisepticaand pages 23-25): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

12. (chamorro2023bordetellabronchisepticaand pages 11-13): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

13. (caulfield2023generatingenhancedmucosal pages 3-4): Amanda D. Caulfield, Maiya Callender, and Eric T. Harvill. Generating enhanced mucosal immunity against bordetella pertussis: current challenges and new directions. Frontiers in Immunology, Feb 2023. URL: https://doi.org/10.3389/fimmu.2023.1126107, doi:10.3389/fimmu.2023.1126107. This article has 13 citations and is from a peer-reviewed journal.

14. (church2025nasalimmunizationwith pages 14-15): Alison Hofmann Church, Soman N. Abraham, Herman F. Staats, and Brandi T. Johnson-Weaver. Nasal immunization with compound 48/80-adjuvanted acellular pertussis vaccines is an effective strategy to induce pertussis-specific systemic and mucosal immunity. Clinical and Experimental Vaccine Research, 14:246-260, Apr 2025. URL: https://doi.org/10.7774/cevr.2025.14.e23, doi:10.7774/cevr.2025.14.e23. This article has 1 citations.

15. (rudi2024useofmucosally pages 10-13): E. Rudi, E. Gaillard, D. Bottero, and D. Hozbor. Use of mucosally administered outer membrane vesicles derived from bordetella pertussis to diminish nasal bacterial colonization. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.11.584448, doi:10.1101/2024.03.11.584448. This article has 0 citations.

16. (regan2023maternalpertussisvaccination pages 1-2): Annette K. Regan, Hannah C. Moore, Michael J. Binks, Lisa McHugh, Christopher C. Blyth, Gavin Pereira, Karin Lust, Mohinder Sarna, Ross Andrews, Damien Foo, Paul V. Effler, Stephen Lambert, and Paul Van Buynder. Maternal pertussis vaccination, infant immunization, and risk of pertussis. Pediatrics, Oct 2023. URL: https://doi.org/10.1542/peds.2023-062664, doi:10.1542/peds.2023-062664. This article has 56 citations and is from a highest quality peer-reviewed journal.

17. (regan2023maternalpertussisvaccination pages 7-8): Annette K. Regan, Hannah C. Moore, Michael J. Binks, Lisa McHugh, Christopher C. Blyth, Gavin Pereira, Karin Lust, Mohinder Sarna, Ross Andrews, Damien Foo, Paul V. Effler, Stephen Lambert, and Paul Van Buynder. Maternal pertussis vaccination, infant immunization, and risk of pertussis. Pediatrics, Oct 2023. URL: https://doi.org/10.1542/peds.2023-062664, doi:10.1542/peds.2023-062664. This article has 56 citations and is from a highest quality peer-reviewed journal.

18. (ernst2022novelstrategiesto pages 2-5): Katharina Ernst. Novel strategies to inhibit pertussis toxin. Toxins, 14:187, Mar 2022. URL: https://doi.org/10.3390/toxins14030187, doi:10.3390/toxins14030187. This article has 29 citations.

19. (jiang2024theeffectof pages 1-5): Kaichong Jiang, Yang Luan, Wei Wang, Da Xue, Shuyue Tang, Xiaokang Peng, Xiaoguai Liu, and Zengguo Wang. The effect of erythromycin in macrolide-resistant bordetella pertussis: inhibitory on growth, toxin expression, and virulence. Unknown journal, Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3933379/v1, doi:10.21203/rs.3.rs-3933379/v1.

20. (jiang2024theeffectof pages 8-10): Kaichong Jiang, Yang Luan, Wei Wang, Da Xue, Shuyue Tang, Xiaokang Peng, Xiaoguai Liu, and Zengguo Wang. The effect of erythromycin in macrolide-resistant bordetella pertussis: inhibitory on growth, toxin expression, and virulence. Unknown journal, Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3933379/v1, doi:10.21203/rs.3.rs-3933379/v1.

21. (wang2025resurgenceofpertussis pages 5-7): Sijia Wang, Shimo Zhang, and Jue Liu. Resurgence of pertussis: epidemiological trends, contributing factors, challenges, and recommendations for vaccination and surveillance. Human Vaccines & Immunotherapeutics, Jun 2025. URL: https://doi.org/10.1080/21645515.2025.2513729, doi:10.1080/21645515.2025.2513729. This article has 56 citations and is from a peer-reviewed journal.

22. (wang2025resurgenceofpertussis pages 2-4): Sijia Wang, Shimo Zhang, and Jue Liu. Resurgence of pertussis: epidemiological trends, contributing factors, challenges, and recommendations for vaccination and surveillance. Human Vaccines & Immunotherapeutics, Jun 2025. URL: https://doi.org/10.1080/21645515.2025.2513729, doi:10.1080/21645515.2025.2513729. This article has 56 citations and is from a peer-reviewed journal.

23. (caulfield2023generatingenhancedmucosal pages 4-5): Amanda D. Caulfield, Maiya Callender, and Eric T. Harvill. Generating enhanced mucosal immunity against bordetella pertussis: current challenges and new directions. Frontiers in Immunology, Feb 2023. URL: https://doi.org/10.3389/fimmu.2023.1126107, doi:10.3389/fimmu.2023.1126107. This article has 13 citations and is from a peer-reviewed journal.

24. (wang2025resurgenceofpertussis pages 4-5): Sijia Wang, Shimo Zhang, and Jue Liu. Resurgence of pertussis: epidemiological trends, contributing factors, challenges, and recommendations for vaccination and surveillance. Human Vaccines & Immunotherapeutics, Jun 2025. URL: https://doi.org/10.1080/21645515.2025.2513729, doi:10.1080/21645515.2025.2513729. This article has 56 citations and is from a peer-reviewed journal.

25. (chamorro2023bordetellabronchisepticaand pages 33-33): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

26. (colak2023bordetellapertussisand pages 2-3): Çiğdem Yılmaz Çolak and Burcu Emine Tefon Öztürk. Bordetella pertussis and outer membrane vesicles. Pathogens and Global Health, 117:342-355, Sep 2023. URL: https://doi.org/10.1080/20477724.2022.2117937, doi:10.1080/20477724.2022.2117937. This article has 13 citations and is from a peer-reviewed journal.

27. (chamorro2023bordetellabronchisepticaand pages 15-16): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

28. (chamorro2023bordetellabronchisepticaand pages 20-22): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

29. (colak2023bordetellapertussisand pages 3-5): Çiğdem Yılmaz Çolak and Burcu Emine Tefon Öztürk. Bordetella pertussis and outer membrane vesicles. Pathogens and Global Health, 117:342-355, Sep 2023. URL: https://doi.org/10.1080/20477724.2022.2117937, doi:10.1080/20477724.2022.2117937. This article has 13 citations and is from a peer-reviewed journal.

30. (wang2025resurgenceofpertussis pages 10-11): Sijia Wang, Shimo Zhang, and Jue Liu. Resurgence of pertussis: epidemiological trends, contributing factors, challenges, and recommendations for vaccination and surveillance. Human Vaccines & Immunotherapeutics, Jun 2025. URL: https://doi.org/10.1080/21645515.2025.2513729, doi:10.1080/21645515.2025.2513729. This article has 56 citations and is from a peer-reviewed journal.

31. (ifill2023lipidamodifications pages 225-228): Gyles Anderson Ifill. Lipid a modifications in bordetella pertussis : regulation and function of the lgm locus. Text, Jan 2023. URL: https://doi.org/10.14288/1.0406206, doi:10.14288/1.0406206. This article has 0 citations and is from a peer-reviewed journal.

32. (colak2023bordetellapertussisand pages 9-10): Çiğdem Yılmaz Çolak and Burcu Emine Tefon Öztürk. Bordetella pertussis and outer membrane vesicles. Pathogens and Global Health, 117:342-355, Sep 2023. URL: https://doi.org/10.1080/20477724.2022.2117937, doi:10.1080/20477724.2022.2117937. This article has 13 citations and is from a peer-reviewed journal.

33. (first2023bordetellaspp.utilize pages 1-2): Nicholas J. First, Jose Pedreira-Lopez, Manuel R. F. San-Silvestre, Katelyn M. Parrish, Xiao-Hong Lu, and Monica C. Gestal. Bordetella spp. utilize the type 3 secretion system to manipulate the vip/vpac2 signaling and promote colonization and persistence of the three classical bordetella in the lower respiratory tract. Frontiers in Cellular and Infection Microbiology, Mar 2023. URL: https://doi.org/10.3389/fcimb.2023.1111502, doi:10.3389/fcimb.2023.1111502. This article has 9 citations.

34. (wang2025resurgenceofpertussis pages 1-2): Sijia Wang, Shimo Zhang, and Jue Liu. Resurgence of pertussis: epidemiological trends, contributing factors, challenges, and recommendations for vaccination and surveillance. Human Vaccines & Immunotherapeutics, Jun 2025. URL: https://doi.org/10.1080/21645515.2025.2513729, doi:10.1080/21645515.2025.2513729. This article has 56 citations and is from a peer-reviewed journal.

35. (wang2025resurgenceofpertussis pages 8-9): Sijia Wang, Shimo Zhang, and Jue Liu. Resurgence of pertussis: epidemiological trends, contributing factors, challenges, and recommendations for vaccination and surveillance. Human Vaccines & Immunotherapeutics, Jun 2025. URL: https://doi.org/10.1080/21645515.2025.2513729, doi:10.1080/21645515.2025.2513729. This article has 56 citations and is from a peer-reviewed journal.

36. (chamorro2023bordetellabronchisepticaand pages 5-7): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

37. (regan2023maternalpertussisvaccination pages 6-7): Annette K. Regan, Hannah C. Moore, Michael J. Binks, Lisa McHugh, Christopher C. Blyth, Gavin Pereira, Karin Lust, Mohinder Sarna, Ross Andrews, Damien Foo, Paul V. Effler, Stephen Lambert, and Paul Van Buynder. Maternal pertussis vaccination, infant immunization, and risk of pertussis. Pediatrics, Oct 2023. URL: https://doi.org/10.1542/peds.2023-062664, doi:10.1542/peds.2023-062664. This article has 56 citations and is from a highest quality peer-reviewed journal.

38. (colak2023bordetellapertussisand pages 11-12): Çiğdem Yılmaz Çolak and Burcu Emine Tefon Öztürk. Bordetella pertussis and outer membrane vesicles. Pathogens and Global Health, 117:342-355, Sep 2023. URL: https://doi.org/10.1080/20477724.2022.2117937, doi:10.1080/20477724.2022.2117937. This article has 13 citations and is from a peer-reviewed journal.

39. (chamorro2023bordetellabronchisepticaand pages 25-27): Beatriz Miguelena Chamorro, Karelle De Luca, Gokul Swaminathan, Stéphanie Longet, Egbert Mundt, and Stéphane Paul. Bordetella bronchiseptica and bordetella pertussis: similarities and differences in infection, immuno-modulation, and vaccine considerations. Clinical Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1128/cmr.00164-22, doi:10.1128/cmr.00164-22. This article has 72 citations and is from a highest quality peer-reviewed journal.

40. (caulfield2023generatingenhancedmucosal pages 5-6): Amanda D. Caulfield, Maiya Callender, and Eric T. Harvill. Generating enhanced mucosal immunity against bordetella pertussis: current challenges and new directions. Frontiers in Immunology, Feb 2023. URL: https://doi.org/10.3389/fimmu.2023.1126107, doi:10.3389/fimmu.2023.1126107. This article has 13 citations and is from a peer-reviewed journal.

41. (caulfield2023generatingenhancedmucosal pages 6-7): Amanda D. Caulfield, Maiya Callender, and Eric T. Harvill. Generating enhanced mucosal immunity against bordetella pertussis: current challenges and new directions. Frontiers in Immunology, Feb 2023. URL: https://doi.org/10.3389/fimmu.2023.1126107, doi:10.3389/fimmu.2023.1126107. This article has 13 citations and is from a peer-reviewed journal.

42. (NCT06827470 chunk 2):  Establishing a Controlled Human Infection Model of Pertactin-deficient Bordetella Pertussis. Dalhousie University. 2025. ClinicalTrials.gov Identifier: NCT06827470

43. (NCT06803524 chunk 3): Punnee Pitisuttithum. 10-year Follow-up After a Single Dose Acellular Pertussis Vaccination. Mahidol University. 2025. ClinicalTrials.gov Identifier: NCT06803524

## Artifacts

- [Edison artifact artifact-00](Pertussis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Pertussis-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Pertussis-deep-research-falcon_artifacts/artifact-02.md)