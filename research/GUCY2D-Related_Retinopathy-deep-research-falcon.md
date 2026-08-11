---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-25T08:30:32.698804'
end_time: '2026-06-25T08:50:29.688344'
duration_seconds: 1196.99
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: GUCY2D-Related Retinopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 4
artifacts:
- filename: artifact-00.md
  path: GUCY2D-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: GUCY2D-Related_Retinopathy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: GUCY2D-Related_Retinopathy-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: artifact-03.md
  path: GUCY2D-Related_Retinopathy-deep-research-falcon_artifacts/artifact-03.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-03
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GUCY2D-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GUCY2D-Related Retinopathy** covering all of the
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
- **Disease Name:** GUCY2D-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GUCY2D-Related Retinopathy** covering all of the
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


# Comprehensive Research Report: GUCY2D-Related Retinopathy

---

## 1. Disease Information

### Overview

GUCY2D-related retinopathy is an umbrella term for inherited retinal dystrophies caused by pathogenic variants in the *GUCY2D* gene, which encodes retinal guanylate cyclase-1 (RetGC-1), an enzyme critical for cyclic GMP (cGMP) synthesis in photoreceptor cells (varela2022lebercongenitalamaurosisearlyonset pages 3-3, wong2025monogenicretinaldiseases pages 8-9). The disease manifests as two principal phenotypes depending on the inheritance pattern and type of mutation: (1) **Leber congenital amaurosis type 1 (LCA1)**, a severe congenital or early-onset retinal dystrophy caused by biallelic loss-of-function variants (autosomal recessive), and (2) **Cone-rod dystrophy type 6 (CORD6)**, a progressive cone-dominant degeneration caused by heterozygous gain-of-function variants (autosomal dominant) (gao2023phenotypiccharacterizationof pages 1-2, bouzia2020gucy2dassociatedlebercongenital pages 1-5, li2023cgmpsignalingin pages 4-5). GUCY2D mutations account for approximately 6–21% of all LCA cases and up to 25–40% of autosomal dominant cone-rod dystrophy cases worldwide (gong2024infantilenystagmussyndrome—associated pages 4-5, hahn2022thenaturalhistory pages 1-2).

### Key Identifiers

The following table summarizes the core disease identifiers and nomenclature for GUCY2D-related retinopathy:

| Identifier Type | Value/ID | Description |
|---|---|---|
| Disease name | GUCY2D-related retinopathy | Umbrella term covering retinal disease caused by pathogenic variants in **GUCY2D**; includes recessive early-onset disease and dominant cone/cone-rod dystrophy presentations (gao2023phenotypiccharacterizationof pages 1-2, bouzia2020gucy2dassociatedlebercongenital pages 1-5) |
| Gene symbol | GUCY2D | Human gene encoding retinal guanylate cyclase-1 / RetGC-1, critical for photoreceptor cGMP resynthesis during recovery after phototransduction (varela2022lebercongenitalamaurosisearlyonset pages 3-3, wong2025monogenicretinaldiseases pages 8-9) |
| OMIM (gene) | 600179 | **GUCY2D** gene entry; cited in recent reviews of GUCY2D-associated retinal disease (gao2023phenotypiccharacterizationof pages 1-2, varela2022lebercongenitalamaurosisearlyonset pages 3-3) |
| Ensembl gene ID | ENSG00000132518 | Ensembl identifier for **GUCY2D**; Open Targets links this target to LCA1, CORD6, and GUCY2D-related recessive retinopathy (OpenTargets Search: -GUCY2D) |
| Chromosomal location | 17p13.1 | Cytogenetic location of **GUCY2D** reported in genotype-phenotype reviews (huang2021leber’scongenitalamaurosis pages 5-6) |
| MONDO | MONDO_0100453 | **GUCY2D-related recessive retinopathy**; disease ontology entry corresponding to recessive GUCY2D-associated retinal disease (OpenTargets Search: -GUCY2D) |
| MONDO | MONDO_0008764 | **Leber congenital amaurosis 1 (LCA1)**; ontology disease entry associated with **GUCY2D** (OpenTargets Search: -GUCY2D) |
| MONDO | MONDO_0011143 | **cone-rod dystrophy 6 (CORD6)**; ontology disease entry associated with **GUCY2D** (OpenTargets Search: -GUCY2D) |
| OMIM (disease) | 204000 | **Leber congenital amaurosis 1 (LCA1)**; severe congenital/early infantile retinal dystrophy caused by biallelic loss-of-function **GUCY2D** variants (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 1-5) |
| OMIM (disease) | 601777 | **cone-rod dystrophy 6 (CORD6)**; autosomal dominant progressive cone/cone-rod dystrophy associated with heterozygous **GUCY2D** variants, often at codon 838 (gao2023phenotypiccharacterizationof pages 1-2, hahn2022thenaturalhistory pages 5-7) |
| Orphanet | Leber congenital amaurosis | Orphanet disease concept relevant to the recessive early-onset **GUCY2D** phenotype; recent reviews state **GUCY2D** accounts for ~6–21% of LCA cases (varela2022lebercongenitalamaurosisearlyonset pages 3-3, gong2024infantilenystagmussyndrome—associated pages 4-5) |
| Orphanet | Cone rod dystrophy | Orphanet disease concept relevant to the dominant **GUCY2D** phenotype; Open Targets maps cone rod dystrophy as Orphanet_1872 and associates **GUCY2D** with it (OpenTargets Search: -GUCY2D) |
| Inheritance pattern | Autosomal recessive | Typical for **GUCY2D-LCA / LCA1 / EOSRD**; usually caused by biallelic loss-of-function variants (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 1-5, li2023cgmpsignalingin pages 4-5) |
| Inheritance pattern | Autosomal dominant | Typical for **GUCY2D-associated cone dystrophy / cone-rod dystrophy (CORD6)**; often caused by gain-of-function variants, especially around codon 838 (gao2023phenotypiccharacterizationof pages 1-2, wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5) |
| Common synonym | GUCY2D-LCA | Common shorthand for autosomal recessive GUCY2D-associated Leber congenital amaurosis (bouzia2020gucy2dassociatedlebercongenital pages 1-5, boye2023preclinicalstudiesin pages 1-2) |
| Common synonym | LCA1 | Historic and commonly used synonym for GUCY2D-associated recessive congenital retinal dystrophy (varela2022lebercongenitalamaurosisearlyonset pages 3-3, NCT03920007 chunk 1) |
| Common synonym | CORD6 | Historic and commonly used synonym for autosomal dominant GUCY2D-associated cone-rod dystrophy (OpenTargets Search: -GUCY2D, hahn2022thenaturalhistory pages 1-2) |


*Table: This table compiles the core identifiers and nomenclature needed to index GUCY2D-related retinopathy in a disease knowledge base. It links the gene, major phenotype-specific disease entries, ontology terms, and inheritance patterns supported by the retrieved evidence.*

### Common Synonyms

- GUCY2D-LCA, LCA1, GUCY2D-associated Leber congenital amaurosis (bouzia2020gucy2dassociatedlebercongenital pages 1-5, NCT03920007 chunk 1)
- CORD6, GUCY2D-associated cone-rod dystrophy (OpenTargets Search: -GUCY2D, hahn2022thenaturalhistory pages 1-2)
- RetGC-1 deficiency (recessive form)
- GUCY2D-related recessive retinopathy (MONDO_0100453) (OpenTargets Search: -GUCY2D)
- Early-onset severe retinal dystrophy (EOSRD) when onset is after infancy but before age 5 (bouzia2020gucy2dassociatedlebercongenital pages 1-5)

### Information Sources

Information is derived from aggregated disease-level resources including OMIM, Orphanet, ClinVar, OpenTargets, and published cohort studies from tertiary referral centers.

---

## 2. Etiology

### Disease Causal Factors

GUCY2D-related retinopathy is a purely monogenic (Mendelian) disorder. The primary cause is pathogenic variation in the *GUCY2D* gene located on chromosome 17p13.1 (huang2021leber’scongenitalamaurosis pages 5-6). The gene encodes retinal guanylate cyclase-1 (RetGC-1/GC-E), which synthesizes cGMP—the intracellular second messenger essential for photoreceptor excitation and recovery during phototransduction (varela2022lebercongenitalamaurosisearlyonset pages 3-3, wong2025monogenicretinaldiseases pages 8-9).

### Genetic Risk Factors

- **Biallelic (homozygous or compound heterozygous) loss-of-function variants** in *GUCY2D* cause autosomal recessive LCA1/EOSRD. Null alleles (frameshift, nonsense, splice-site variants) account for approximately 88% of LCA-causing alleles (varela2022lebercongenitalamaurosisearlyonset pages 3-3).
- **Heterozygous gain-of-function missense variants**, particularly at codon 838 in exon 13, cause autosomal dominant CORD6. The most common CORD variant is c.2513G>A (p.Arg838His), found in 54.4% of CORD patients in one large cohort (hahn2022thenaturalhistory pages 5-7).
- Consanguinity plays a notable role, particularly in populations with high rates of consanguineous marriage; one Indian cohort reported consanguinity in 54% of LCA families (huang2021leber’scongenitalamaurosis pages 5-6).

### Environmental and Protective Factors

No environmental risk factors, protective factors, or gene-environment interactions have been identified for this purely genetic disorder. Disease expression is determined by the specific *GUCY2D* genotype.

### Modifier Genes

Potential modifier genes have been explored in familial studies. One investigation identified variants in *CACNG8*, *PAX2*, *RXRG*, *CCDC175*, *PDE4DIP*, and *LTF* as candidate modifiers that may contribute to intrafamilial phenotypic heterogeneity in GUCY2D-associated CORD (donato2022theimpactof pages 7-10).

---

## 3. Phenotypes

The phenotypic spectrum of GUCY2D-related retinopathy is summarized in the following table:

| Phenotype | HPO Term | HPO ID | Frequency | Onset | Phenotype Type |
|---|---|---|---|---|---|
| Severe visual impairment (LCA1) | Severe visual impairment | HP:0012378 | Very common; in one natural-history cohort 76% were severely visually impaired (hand movements or worse) (bouzia2020gucy2dassociatedlebercongenital pages 5-8); ~50% reported vision worse than counting fingers in review data (huang2021leber’scongenitalamaurosis pages 5-6) | Congenital/infancy | Symptom/functional deficit |
| Nystagmus (LCA1) | Nystagmus | HP:0000639 | Very common; reported in all patients in a 21-patient GUCY2D-LCA cohort (bouzia2020gucy2dassociatedlebercongenital pages 8-10) | Congenital/first 3 years | Clinical sign |
| Oculodigital sign / Franceschetti sign (LCA1) | Oculodigital sign | HP:0000658 | Common/characteristic; repeatedly reported in GUCY2D-LCA reviews and cohorts (bouzia2020gucy2dassociatedlebercongenital pages 1-5, huang2021leber’scongenitalamaurosis pages 5-6) | Infancy | Behavioral/clinical sign |
| Photophobia (LCA1) | Photophobia | HP:0000613 | Common/prominent in GUCY2D-LCA (varela2022lebercongenitalamaurosisearlyonset pages 3-3, huang2021leber’scongenitalamaurosis pages 5-6, gong2024infantilenystagmussyndrome—associated pages 4-5) | Infancy/early childhood | Symptom |
| Hyperopia (LCA1) | Hyperopia | HP:0000540 | Common; noted as a frequent refractive feature in GUCY2D-LCA/LCA reviews (gong2024infantilenystagmussyndrome—associated pages 4-5, huang2021leber’scongenitalamaurosis pages 1-2) | Childhood | Clinical finding/refractive abnormality |
| Absent or markedly diminished ERG (LCA1) | Abnormal electroretinogram | HP:0007703 | Very common; severe cone-rod dystrophy or severe photoreceptor dystrophy with undetectable or severely subnormal responses in most/all tested patients (bouzia2020gucy2dassociatedlebercongenital pages 10-14, bouzia2020gucy2dassociatedlebercongenital pages 8-10) | Congenital/infancy | Laboratory/functional abnormality |
| Preserved retinal structure despite severe dysfunction (LCA1) | Abnormality of the macula / preserved EZ with dysfunction* | HP:0007754* | Characteristic structural-functional dissociation; frequent in GUCY2D-LCA cohorts (bouzia2020gucy2dassociatedlebercongenital pages 10-14) | Childhood onward | Imaging/structural sign |
| Keratoconus (LCA1 complication) | Keratoconus | HP:0000563 | Uncommon but reported complication contributing to worse vision in some patients (bouzia2020gucy2dassociatedlebercongenital pages 8-10) | Later childhood/adolescence | Ocular complication |
| Early-onset cataract (LCA1 complication) | Juvenile cataract | HP:0000518 | Uncommon but reported in some GUCY2D-LCA patients as a cause of additional visual decline (bouzia2020gucy2dassociatedlebercongenital pages 8-10) | Childhood/adolescence | Ocular complication |
| Progressive vision loss (CORD6) | Progressive visual loss | HP:0000529 | Common/defining; adCORD shows progressive decline, with mean BCVA worsening ~0.022 logMAR/year (hahn2022thenaturalhistory pages 1-2) | Childhood/adolescence | Symptom/course feature |
| Color vision defects (CORD6) | Dyschromatopsia | HP:0000551 | Common; cone dysfunction and impaired color perception described across GUCY2D-CORD cohorts/kindreds (gao2023phenotypiccharacterizationof pages 1-2, donato2022theimpactof pages 7-10) | Childhood/adolescence | Symptom |
| Photophobia (CORD6) | Photophobia | HP:0000613 | Common in cone-dominant disease and reported in affected families (gao2023phenotypiccharacterizationof pages 1-2, donato2022theimpactof pages 7-10) | Childhood/adolescence | Symptom |
| Macular atrophy (CORD6) | Macular atrophy | HP:0007758 | Common in later disease; early granular macular changes progress to obvious macular atrophy (gao2023phenotypiccharacterizationof pages 1-2, gao2023phenotypiccharacterizationof pages 7-8) | Childhood/adolescence progressing in adulthood | Imaging/structural sign |
| Reduced cone responses / cone-rod dysfunction on ERG (CORD6) | Abnormal electroretinogram | HP:0007703 | Very common; reduced cone responses with relative rod preservation early, later rod involvement (gao2023phenotypiccharacterizationof pages 1-2, donato2022theimpactof pages 7-10) | Childhood/adolescence | Laboratory/functional abnormality |
| Reduced visual acuity (CORD6) | Decreased visual acuity | HP:0007663 | Common; variable early, progressive over time, can reach severe visual impairment by mid-late adulthood (gao2023phenotypiccharacterizationof pages 1-2, hahn2022thenaturalhistory pages 1-2, gao2023phenotypiccharacterizationof pages 7-8) | Childhood/adolescence | Symptom/functional deficit |
| Central scotoma (CORD6) | Central scotoma | HP:0000611 | Reported in affected family members with GUCY2D-CORD (donato2022theimpactof pages 7-10) | Childhood/adolescence | Symptom |
| Peripheral retinal pigmentary changes (CORD6) | Retinal pigment epithelial mottling / pigmentary retinopathy* | HP:0001100* | Reported in some affected kindreds with generalized pigmentary granularity and peripheral bone-spicule-like changes (donato2022theimpactof pages 7-10) | Adolescence/adulthood | Fundus sign |
| Severe visual impairment/blindness by adulthood (CORD6) | Blindness / severe visual impairment | HP:0000618 | Substantial long-term risk; 32% probability of blindness or severe visual impairment by age 40 in one cohort (hahn2022thenaturalhistory pages 1-2) | Mid-adulthood after childhood/adolescent onset | Outcome/functional deficit |


*Table: This table summarizes major phenotypes reported across GUCY2D-related recessive retinopathy/LCA1 and dominant CORD6, with suggested HPO mappings, onset patterns, and qualitative frequency information. It is useful for disease knowledge base curation and phenotype annotation.*

### LCA1 Phenotype (Recessive)

Patients with GUCY2D-LCA present within the first year to three years of life with severe visual impairment, nystagmus, oculodigital sign (Franceschetti sign), and prominent photophobia (bouzia2020gucy2dassociatedlebercongenital pages 1-5, huang2021leber’scongenitalamaurosis pages 5-6, bouzia2020gucy2dassociatedlebercongenital pages 8-10). Approximately 50% of patients have vision worse than counting fingers, and only about 25% achieve measurable Snellen visual acuity (huang2021leber’scongenitalamaurosis pages 5-6). Full-field electroretinography (ERG) shows severely reduced or extinguished responses affecting both rod and cone pathways (bouzia2020gucy2dassociatedlebercongenital pages 10-14, bouzia2020gucy2dassociatedlebercongenital pages 8-10). Hyperopia is the most common refractive error (gong2024infantilenystagmussyndrome—associated pages 4-5, huang2021leber’scongenitalamaurosis pages 1-2). A distinctive and diagnostically important feature of GUCY2D-LCA is a dissociation between retinal structure and function: optical coherence tomography (OCT) often reveals preserved ellipsoid zone (EZ) and relatively intact outer nuclear layer (ONL) centrally, despite profoundly reduced visual function (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 10-14). Complications include keratoconus and early-onset cataracts in some patients (bouzia2020gucy2dassociatedlebercongenital pages 8-10).

### CORD6 Phenotype (Dominant)

GUCY2D-associated CORD typically presents during childhood or adolescence with progressive loss of visual acuity, color vision defects (dyschromatopsia), photophobia, and central scotomas (gao2023phenotypiccharacterizationof pages 1-2, donato2022theimpactof pages 7-10, hahn2022thenaturalhistory pages 1-2). ERG shows reduced cone responses with relatively preserved rod responses early in the disease, with subsequent rod involvement (gao2023phenotypiccharacterizationof pages 1-2, donato2022theimpactof pages 7-10). Fundus examination reveals early granular retinal pigment epithelium (RPE) abnormalities progressing to macular atrophy in older patients (gao2023phenotypiccharacterizationof pages 1-2, gao2023phenotypiccharacterizationof pages 7-8). OCT demonstrates reduced retinal thickness, loss of outer retinal bands, and progressive retinal atrophy (gao2023phenotypiccharacterizationof pages 1-2, donato2022theimpactof pages 7-10).

### Quality of Life Impact

Both phenotypes cause significant impact on daily functioning. LCA1 patients experience profound lifelong visual disability typically from infancy, while CORD6 patients face progressive visual decline culminating in severe visual impairment during mid-to-late adulthood (hahn2022thenaturalhistory pages 1-2, bouzia2020gucy2dassociatedlebercongenital pages 5-8).

---

## 4. Genetic/Molecular Information

### Causal Gene

**GUCY2D** (guanylate cyclase 2D, retinal)
- HGNC symbol: GUCY2D
- OMIM gene: 600179
- Ensembl: ENSG00000132518
- Chromosomal location: 17p13.1 (OpenTargets Search: -GUCY2D, huang2021leber’scongenitalamaurosis pages 5-6)
- Protein product: Retinal guanylate cyclase-1 (RetGC-1/GC-E)

RetGC-1 is responsible for over 70% of cGMP production in photoreceptors and is expressed in both rod and cone outer segments, with higher expression in cones (huang2021leber’scongenitalamaurosis pages 5-6, li2023cgmpsignalingin pages 2-4). Its activity is regulated by guanylate cyclase activating proteins (GCAPs) in a calcium-dependent manner (li2023cgmpsignalingin pages 2-4).

### Pathogenic Variants

Over 248 variants in *GUCY2D* have been identified as causing autosomal recessive LCA/EOSRD, while approximately 30 variants are linked to autosomal dominant CORD (gong2024infantilenystagmussyndrome—associated pages 4-5). In one large natural history study of LCA patients, variant types included: missense (71.4%), nonsense (31.4%), and frameshift (7.1%) mutations (hahn2022thenaturalhistory pages 5-7). Additional variant types include in-frame deletions and splice-site variants (bouzia2020gucy2dassociatedlebercongenital pages 16-20).

Notable recessive (LCA1) variants include:
- c.1694T>C (p.Phe565Ser)—recurrent in LCA cohorts (hahn2022thenaturalhistory pages 5-7)
- c.2302C>T (p.Arg768Trp)—found in compound heterozygotes (hahn2022thenaturalhistory pages 5-7, areblom2023adescriptionof pages 9-10)
- c.1343C>A (p.Ser448*)—nonsense variant (bouzia2020gucy2dassociatedlebercongenital pages 16-20)
- c.901_908delCTTCGCAG—frameshift variant (bouzia2020gucy2dassociatedlebercongenital pages 16-20)

Notable dominant (CORD6) variants:
- c.2513G>A (p.Arg838His)—most common CORD variant, found in 54.4% of patients in one cohort (hahn2022thenaturalhistory pages 5-7)
- c.2512C>T (p.Arg838Cys)—recurrent CORD variant (gao2023phenotypiccharacterizationof pages 1-2)
- c.2513G>C (p.Arg838Pro)—identified as a causative CORD variant (donato2022theimpactof pages 10-11)

### Functional Consequences

- **Loss-of-function** (recessive): Null or severely damaging alleles abolish or markedly reduce RetGC-1 catalytic activity, impairing cGMP resynthesis after phototransduction. Complete loss of RetGC-1 catalytic ability consistently results in congenital blindness (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 13-14).
- **Gain-of-function** (dominant): Missense variants at codon 838 alter the calcium sensitivity of RetGC-1, making the enzyme abnormally active or excessively sensitive to GCAP regulation. This produces elevated cGMP levels that keep CNG channels constitutively open, increasing Na⁺ and Ca²⁺ influx and triggering apoptotic photoreceptor death (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5).

### Genotype-Phenotype Correlations

Variants in exon 2 (extracellular domain) of *GUCY2D* are associated with milder LCA phenotypes and better-preserved visual acuity over time (bouzia2020gucy2dassociatedlebercongenital pages 10-14). For CORD, variants cluster predominantly at codon 838 in exon 13, with up to 87% of CORD patients carrying the two most prevalent variants at this position (hahn2022thenaturalhistory pages 5-7, hahn2022thenaturalhistory pages 1-2).

### RD3 as a Related Gene

RD3 (RD3 regulator of GUCY2D; OMIM gene for RD3) is a protein that regulates GUCY2D trafficking and function. Mutations in *RD3* can also cause LCA, mechanistically linked through RetGC-1 dysfunction (OpenTargets Search: -GUCY2D).

---

## 5. Environmental Information

GUCY2D-related retinopathy is a purely genetic disorder with no known environmental, lifestyle, or infectious contributing factors. No environmental or lifestyle modifications have been identified that alter disease risk or progression.

---

## 6. Mechanism / Pathophysiology

The pathophysiology of GUCY2D-related retinopathy is comprehensively compared between the two major disease mechanisms in the following table:

| Feature | Loss-of-Function (LCA1) | Gain-of-Function (CORD6) |
|---|---|---|
| Typical inheritance | Autosomal recessive; usually biallelic GUCY2D variants causing GUCY2D-LCA/LCA1 (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 1-5, li2023cgmpsignalingin pages 4-5) | Autosomal dominant; usually heterozygous GUCY2D variants causing cone/cone-rod dystrophy, classically CORD6 (gao2023phenotypiccharacterizationof pages 1-2, wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5) |
| Typical mutation classes | Null or severely damaging alleles predominate: nonsense, frameshift, splice-site, and severe missense variants that abolish or markedly reduce RetGC-1 activity (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5, bouzia2020gucy2dassociatedlebercongenital pages 16-20) | Mostly missense variants, strongly enriched in exon 13/codon 838 hotspot, altering GCAP-mediated regulation rather than eliminating protein expression (wong2025monogenicretinaldiseases pages 8-9, hahn2022thenaturalhistory pages 5-7, donato2022theimpactof pages 10-11) |
| RetGC-1 enzyme function | RetGC-1/RETGC-1 (retinal guanylate cyclase-1) is absent or catalytically impaired, so cGMP cannot be adequately regenerated after phototransduction (varela2022lebercongenitalamaurosisearlyonset pages 3-3, li2023cgmpsignalingin pages 13-14, li2023cgmpsignalingin pages 2-4) | RetGC-1 is present but dysregulated, remaining excessively active or overly sensitive to GCAP control, causing excessive cGMP synthesis (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 13-14) |
| GCAP regulation | Normal Ca2+-dependent GCAP control is ineffective because enzyme activity is too low/absent to respond appropriately; recovery phase of phototransduction fails (li2023cgmpsignalingin pages 13-14, li2023cgmpsignalingin pages 2-4) | GCAP-dependent regulation is shifted abnormally; mutant RetGC-1 shows enhanced sensitivity or altered Ca2+ set-point, driving cyclase activity when it should be suppressed (li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 13-14, li2023cgmpsignalingin pages 11-13) |
| Primary biochemical defect | Failure of cGMP resynthesis in outer segments after light response (varela2022lebercongenitalamaurosisearlyonset pages 3-3, wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 2-4) | Excess cGMP production and dysregulated cGMP signaling in darkness/recovery (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 11-13) |
| cGMP level consequence | cGMP becomes insufficient for normal reopening of cyclic nucleotide-gated channels; photoreceptors remain functionally silent/blind (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 13-14) | cGMP becomes abnormally elevated, promoting sustained channel opening and toxic signaling (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 11-13) |
| CNG channel status | CNG channels fail to reopen normally because cGMP is not adequately restored; phototransduction recovery is impaired (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 2-4) | CNG channels remain abnormally open or overactive due to high cGMP (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5) |
| Calcium homeostasis | Abnormal signaling with impaired normal Ca2+-dependent recovery; severe dysfunction results from failure to restore the dark state (li2023cgmpsignalingin pages 13-14, li2023cgmpsignalingin pages 2-4) | Excess Na+ and Ca2+ influx through persistently open CNG channels causes Ca2+ overload and homeostatic failure (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 11-13) |
| Downstream cellular consequences | Severe photoreceptor dysfunction with markedly reduced or absent signaling despite relative anatomic preservation early in disease; blindness reflects failure of phototransduction rather than immediate cell loss (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 10-14) | Chronic cGMP/PKG activation, Ca2+ overload, calpain activation, ER stress, and downstream death pathways drive progressive cone-predominant degeneration (li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 11-13) |
| Predominant photoreceptor effect | Congenital severe cone-rod or severe photoreceptor dysfunction; rods and cones both affected functionally, but central retinal structure may remain preserved for years (bouzia2020gucy2dassociatedlebercongenital pages 1-5, bouzia2020gucy2dassociatedlebercongenital pages 10-14) | Cone-dominant degeneration first, with later rod involvement; progressive cone dystrophy or cone-rod dystrophy phenotype (gao2023phenotypiccharacterizationof pages 1-2, wong2025monogenicretinaldiseases pages 8-9, hahn2022thenaturalhistory pages 1-2) |
| Clinical phenotype | Leber congenital amaurosis 1 / early-onset severe retinal dystrophy with profound visual loss, nystagmus, photophobia, extinguished or severely reduced ERG (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 1-5, bouzia2020gucy2dassociatedlebercongenital pages 8-10) | Progressive cone dystrophy / cone-rod dystrophy with reduced visual acuity, dyschromatopsia, photophobia, macular atrophy, abnormal cone ERG and later rod involvement (gao2023phenotypiccharacterizationof pages 1-2, donato2022theimpactof pages 7-10, hahn2022thenaturalhistory pages 1-2) |
| Age at onset | Congenital or infancy; usually first year or first 3 years of life (bouzia2020gucy2dassociatedlebercongenital pages 1-5, huang2021leber’scongenitalamaurosis pages 5-6, bouzia2020gucy2dassociatedlebercongenital pages 8-10) | Childhood to adolescence, often around the second decade, with later progressive decline (gao2023phenotypiccharacterizationof pages 1-2, hahn2022thenaturalhistory pages 1-2) |
| Disease course | Severe but often relatively stable visual function over time in many cohorts, despite profound impairment from infancy (bouzia2020gucy2dassociatedlebercongenital pages 10-14, bouzia2020gucy2dassociatedlebercongenital pages 8-10) | Clearly progressive, with worsening BCVA over time and substantial risk of severe visual impairment by adulthood (hahn2022thenaturalhistory pages 1-2, gao2023phenotypiccharacterizationof pages 7-8) |
| Structural preservation | Distinctive structure-function dissociation: OCT often shows preserved ellipsoid zone/outer nuclear layer centrally despite very poor vision and ERG (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 10-14) | Structural degeneration becomes more apparent over time, including reduced retinal thickness, loss of outer retinal bands, and macular atrophy (gao2023phenotypiccharacterizationof pages 1-2, donato2022theimpactof pages 7-10, gao2023phenotypiccharacterizationof pages 7-8) |
| Why gene augmentation is attractive | Strong rationale because disease is usually due to insufficient gene product/activity and many patients retain central photoreceptors structurally (varela2022lebercongenitalamaurosisearlyonset pages 3-3, boye2023preclinicalstudiesin pages 1-2) | Gene augmentation alone is less straightforward because dominant toxicity/dysregulation must be suppressed or corrected, not just supplemented (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5) |
| Suggested GO terms | GO:0007602 phototransduction; GO:0006171 cGMP biosynthetic process; GO:0050896 response to stimulus; GO:0006816 calcium ion transport; GO:0007601 visual perception (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 2-4) | GO:0007602 phototransduction; GO:0006171 cGMP biosynthetic process; GO:0051480 regulation of cytosolic calcium ion concentration; GO:0030168 platelet-derived growth factor receptor signaling?* not specific; GO:0097190 apoptotic signaling pathway; GO:0034976 response to endoplasmic reticulum stress (li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 11-13) |
| Suggested pathway labels | Reactome/KEGG-relevant concepts: Phototransduction cascade; cyclic GMP signaling in photoreceptors; recovery phase of phototransduction (varela2022lebercongenitalamaurosisearlyonset pages 3-3, wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 2-4) | Reactome/KEGG-relevant concepts: Phototransduction cascade; cGMP-PKG signaling; calcium-overload/stress-linked degeneration pathways downstream of abnormal phototransduction (li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 11-13) |


*Table: This table compares the two major molecular mechanisms of GUCY2D-related retinopathy: recessive loss-of-function causing LCA1 and dominant gain-of-function causing CORD6. It is useful for linking genotype to biochemical dysfunction, retinal physiology, and clinical phenotype.*

### Molecular Pathways

RetGC-1 is a central enzyme in the phototransduction recovery cascade. In normal photoreceptors, light activation triggers a signaling cascade (rhodopsin → transducin → phosphodiesterase 6) that hydrolyzes cGMP, causing CNG channel closure and hyperpolarization. During recovery, RetGC-1 resynthesizes cGMP under GCAP-mediated calcium regulation, reopening CNG channels and restoring the dark state (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 2-4).

### Loss-of-Function Mechanism (LCA1)

When RetGC-1 is absent or catalytically impaired, cGMP cannot be regenerated after light-induced hydrolysis. CNG channels fail to reopen, and photoreceptors remain in a permanently hyperpolarized, functionally silent state. Despite this severe functional deficit, photoreceptor cells may remain structurally intact for prolonged periods—a phenomenon termed "structure-function dissociation"—because the cells are not actively dying but rather dysfunctional (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 10-14, li2023cgmpsignalingin pages 13-14).

### Gain-of-Function Mechanism (CORD6)

Dominant mutations alter the calcium-sensitivity of RetGC-1 regulation by GCAPs, causing the enzyme to remain excessively active even at normal or elevated intracellular calcium levels. This results in pathological cGMP accumulation, persistent opening of CNG channels, excessive Na⁺/Ca²⁺ influx, and activation of downstream death pathways including cGMP/PKG signaling, endoplasmic reticulum stress, calpain activation, and Ca²⁺-mediated apoptosis (wong2025monogenicretinaldiseases pages 8-9, li2023cgmpsignalingin pages 4-5, li2023cgmpsignalingin pages 11-13).

### Relevant Ontology Terms

- **GO Biological Processes**: GO:0007602 (phototransduction); GO:0006171 (cGMP biosynthetic process); GO:0007601 (visual perception); GO:0006816 (calcium ion transport); GO:0097190 (apoptotic signaling pathway)
- **GO Cellular Component**: GO:0001750 (photoreceptor outer segment)
- **Cell types (CL)**: CL:0000604 (retinal rod cell); CL:0000573 (retinal cone cell); CL:0002586 (retinal pigment epithelial cell)
- **KEGG/Reactome**: Phototransduction cascade; Visual cycle; cGMP-PKG signaling pathway

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary**: Eye (retina)—specifically the neurosensory retina containing photoreceptor cells
- **Body system**: Nervous system (visual pathway)
- **UBERON**: UBERON:0000966 (retina); UBERON:0000019 (camera-type eye)

### Tissue and Cell Level
- **Photoreceptor outer segments**: Primary site of RetGC-1 expression and cGMP synthesis (huang2021leber’scongenitalamaurosis pages 5-6, li2023cgmpsignalingin pages 2-4)
- **Cone photoreceptors** (CL:0000573): Preferentially affected in CORD6; RetGC-1 is expressed at higher levels in cones (huang2021leber’scongenitalamaurosis pages 5-6, wong2025monogenicretinaldiseases pages 8-9)
- **Rod photoreceptors** (CL:0000604): Also affected in LCA1 (both rods and cones dysfunctional); secondary involvement in advanced CORD6
- **Retinal pigment epithelium** (CL:0002586): Secondary changes including RPE mottling and atrophy (bouzia2020gucy2dassociatedlebercongenital pages 14-16, donato2022theimpactof pages 7-10)
- **Macula** (UBERON:0000053): Central macular structure particularly important in disease; preserved centrally in early LCA1 but progressively atrophied in CORD6

### Subcellular Level
- Photoreceptor outer segment disc membranes (site of RetGC-1 localization)
- CNG channels on outer segment plasma membrane
- GO Cellular Component: GO:0001750 (photoreceptor outer segment)

---

## 8. Temporal Development

### Onset

**LCA1 (Recessive)**: Congenital or early infantile onset, typically within the first year of life. All patients in one cohort developed nystagmus and marked visual acuity reduction within the first three years (bouzia2020gucy2dassociatedlebercongenital pages 1-5, bouzia2020gucy2dassociatedlebercongenital pages 8-10). The onset pattern is congenital/insidious with severe visual impairment apparent from birth or early infancy.

**CORD6 (Dominant)**: Childhood to adolescent onset, typically around the second decade of life, with progressive decline thereafter (hahn2022thenaturalhistory pages 1-2). The onset is subacute to insidious with gradual deterioration of central and color vision.

### Progression

**LCA1**: Despite severe congenital impairment, the disease course is relatively stable in most patients. Serial ERG recordings show lack of deterioration, and OCT imaging demonstrates minimal structural progression over follow-up periods of 2–13.3 years (bouzia2020gucy2dassociatedlebercongenital pages 10-14, bouzia2020gucy2dassociatedlebercongenital pages 8-10). However, some patients experience additional visual decline due to complications such as keratoconus or early-onset cataracts (bouzia2020gucy2dassociatedlebercongenital pages 8-10).

**CORD6**: Clearly progressive disease with annual BCVA worsening of approximately 0.022 logMAR per year. There is a 32% probability of blindness or severe visual impairment by age 40 (hahn2022thenaturalhistory pages 1-2). Structural degeneration on imaging becomes more apparent over time with progressive macular atrophy (gao2023phenotypiccharacterizationof pages 1-2, gao2023phenotypiccharacterizationof pages 7-8).

### Disease Duration

Both phenotypes represent chronic, lifelong conditions. LCA1 is a congenital disease with lifelong severe visual impairment. CORD6 is a progressive degenerative disease culminating in severe visual impairment during mid-to-late adulthood (hahn2022thenaturalhistory pages 1-2).

---

## 9. Inheritance and Population

### Inheritance Patterns

- **Autosomal recessive (AR)**: LCA1/EOSRD, caused by biallelic loss-of-function *GUCY2D* variants (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 1-5)
- **Autosomal dominant (AD)**: CORD6/cone dystrophy, caused by heterozygous gain-of-function variants (gao2023phenotypiccharacterizationof pages 1-2, wong2025monogenicretinaldiseases pages 8-9)

### Epidemiology

LCA as a group has an estimated prevalence of approximately 1:33,000–80,000 births and is responsible for approximately 20% of childhood blindness (varela2022lebercongenitalamaurosisearlyonset pages 3-3). GUCY2D variants account for 6–21% of all LCA cases, making it one of the most commonly affected genes (varela2022lebercongenitalamaurosisearlyonset pages 3-3, huang2021leber’scongenitalamaurosis pages 5-6, gong2024infantilenystagmussyndrome—associated pages 4-5, hahn2022thenaturalhistory pages 1-2). In an Indian cohort, GUCY2D was the most common causative gene at 20% of cases (huang2021leber’scongenitalamaurosis pages 5-6). GUCY2D accounts for up to 25–40% of all autosomal dominant cone-rod dystrophy cases (wong2025monogenicretinaldiseases pages 8-9, gong2024infantilenystagmussyndrome—associated pages 4-5, hahn2022thenaturalhistory pages 1-2).

### Population Demographics

- Autosomal recessive inheritance is seen in approximately 94% of LCA cases (huang2021leber’scongenitalamaurosis pages 5-6)
- No specific ethnic predisposition has been definitively established, though consanguinity significantly increases the risk of autosomal recessive forms
- The sex ratio is approximately equal (huang2021leber’scongenitalamaurosis pages 5-6)

---

## 10. Diagnostics

### Clinical Tests

**Electroretinography (ERG)**: The gold-standard functional test. In LCA1, full-field ERG shows severely reduced or undetectable dark-adapted (scotopic) and light-adapted (photopic) responses (bouzia2020gucy2dassociatedlebercongenital pages 10-14, bouzia2020gucy2dassociatedlebercongenital pages 8-10). In CORD6, ERG demonstrates reduced cone responses with initially preserved rod responses (gao2023phenotypiccharacterizationof pages 1-2, donato2022theimpactof pages 7-10). ERG testing follows ISCEV standards using gold foil corneal electrodes (bouzia2020gucy2dassociatedlebercongenital pages 5-8).

**Optical Coherence Tomography (OCT)**: Spectral-domain OCT reveals the characteristic structure-function dissociation in LCA1, with preserved ellipsoid zone (EZ) and external limiting membrane (ELM) despite severe visual impairment (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 10-14, hahn2022thenaturalhistory pages 1-2). In CORD6, OCT shows progressive retinal thinning, loss of outer retinal bands, and macular atrophy (gao2023phenotypiccharacterizationof pages 1-2, gao2023phenotypiccharacterizationof pages 7-8). EZ and ELM integrity on OCT correlate significantly with visual acuity outcomes (hahn2022thenaturalhistory pages 1-2).

**Fundus Autofluorescence (FAF)**: Variable patterns from normal appearance to central and mid-peripheral hypoautofluorescence with variable hyperautofluorescent foci (bouzia2020gucy2dassociatedlebercongenital pages 14-16).

**Fundus Photography**: In LCA1, fundi may appear near-normal early in life. In CORD6, progressive RPE granularity and macular atrophy are characteristic (gao2023phenotypiccharacterizationof pages 1-2, gao2023phenotypiccharacterizationof pages 7-8).

### Genetic Testing

Molecular confirmation is essential and typically employs:
- **Targeted next-generation sequencing (NGS) panels** of inherited retinal dystrophy genes (bouzia2020gucy2dassociatedlebercongenital pages 5-8)
- **Whole exome sequencing (WES)** for cases not resolved by panels (bouzia2020gucy2dassociatedlebercongenital pages 5-8)
- **Whole genome sequencing (WGS)** for comprehensive analysis (bouzia2020gucy2dassociatedlebercongenital pages 5-8)
- **Sanger sequencing** for validation and segregation analysis (bouzia2020gucy2dassociatedlebercongenital pages 5-8)
- Variants are classified per ACMG/AMP guidelines and cross-referenced with ClinVar (huang2021leber’scongenitalamaurosis pages 5-6)

### Differential Diagnosis

GUCY2D-LCA must be distinguished from other forms of LCA caused by different genes (RPE65, CEP290, CRB1, RDH12, AIPL1, etc.). The relatively preserved retinal structure on OCT despite severe functional impairment is a distinguishing feature of GUCY2D-LCA compared to other LCA subtypes that show extensive early photoreceptor loss (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 10-14).

---

## 11. Outcome/Prognosis

### LCA1 Prognosis

Visual acuity in GUCY2D-LCA is profoundly reduced from infancy but remains relatively stable over time, with 76% of patients severely visually impaired (hand movements or worse) and only 24% able to record visual acuity on standard charts (bouzia2020gucy2dassociatedlebercongenital pages 5-8). Despite the severe functional deficit, the relatively preserved retinal structure suggests a therapeutic window for gene therapy intervention (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 10-14). Life expectancy is not reduced in non-syndromic cases.

### CORD6 Prognosis

GUCY2D-associated CORD shows clearly progressive visual decline with a mean annual worsening of approximately 0.022 logMAR. The disease results in a 32% probability of blindness or severe visual impairment by age 40, culminating in severe visual impairment during mid-to-late adulthood (hahn2022thenaturalhistory pages 1-2).

### Prognostic Factors

Genotype-phenotype correlations serve as prognostic indicators: patients with missense variants in exon 2 (extracellular domain) demonstrate milder LCA phenotypes with better-preserved visual acuity over time (bouzia2020gucy2dassociatedlebercongenital pages 10-14). Residual cone-photoreceptor vision correlates with the biochemical properties of specific mutations (bouzia2020gucy2dassociatedlebercongenital pages 14-16).

---

## 12. Treatment

The following table summarizes current and experimental therapies:

| Therapy/Product | Type | NCT Number | Phase | Sponsor | Status | Route of Administration | Key Results | MAXO term |
|---|---|---|---|---|---|---|---|---|
| ATSN-101 | Gene augmentation; AAV-based GUCY2D replacement therapy | NCT03920007 | Phase I/II | Atsena Therapeutics Inc. | Active, not recruiting; 15 participants | Unilateral subretinal injection | Reported early efficacy/safety signals in GUCY2D-LCA; mean improvement 20.3 dB, and 3/6 treated patients reached the maximum MLMT score; trial eligibility requires biallelic GUCY2D variants and identifiable central photoreceptor structure on OCT (saripalli2026genetherapyand pages 2-4, wong2025monogenicretinaldiseases pages 21-21, NCT03920007 chunk 1, NCT03920007 chunk 2) | MAXO: gene therapy; subretinal gene delivery |
| SAR439483 | Gene augmentation; AAV-based GUCY2D replacement therapy | NCT03920007 | Phase I/II | Originally described in development with Sanofi/Atsena-associated program reporting | Ongoing in published 2022 review; current registry entry active, not recruiting | Subretinal injection | Preclinical studies in knockout mice improved ERG responses; developed to restore guanylate cyclase 2D expression in GUCY2D-LCA, a condition considered favorable for gene therapy because of relative preservation of central photoreceptor structure (varela2022lebercongenitalamaurosisearlyonset pages 3-3, boye2023preclinicalstudiesin pages 1-2, bouzia2020gucy2dassociatedlebercongenital pages 10-14) | MAXO: gene therapy; subretinal gene delivery |
| AAV5-hGRK1-GUCY2D (preclinical program underlying ATSN-101) | Preclinical gene augmentation | Not applicable | Preclinical | Atsena/Boye group preclinical development | Preclinical support completed | Subretinal injection | In GCDKO mice, high-dose treatment produced sustained statistically significant improvement in photopic and scotopic retinal function for at least 3 months; dose-ranging in cynomolgus monkeys and biodistribution/toxicology studies in rats and nonhuman primates supported clinical translation (boye2023preclinicalstudiesin pages 1-2, boye2023preclinicalstudiesin pages 16-16) | MAXO: gene therapy |
| AAV-GC1 / RetGC1 replacement in animal models | Preclinical gene augmentation | Not applicable | Preclinical | Academic preclinical studies | Preclinical | Ocular gene delivery (subretinal in mouse studies; lentiviral expression in avian model) | Long-term cone preservation and improved visual function reported in guanylate cyclase-1 knockout mouse models; avian childhood-blindness model showed restored vision after retinal guanylate cyclase-1 expression (bouzia2020gucy2dassociatedlebercongenital pages 14-16) | MAXO: gene therapy |
| CRISPR-based GUCY2D editing approaches | Experimental genome editing concept | None identified for active human GUCY2D retinopathy trial in retrieved evidence | Preclinical/conceptual | Academic/preclinical | Preclinical only | Viral delivery to retina discussed conceptually | Reviews cite successful editing/knockout of GUCY2D coding sequence in mouse and macaque photoreceptors as proof-of-platform for retinal genome editing, but no active disease-specific therapeutic clinical trial for GUCY2D retinopathy was retrieved here (gong2024infantilenystagmussyndrome—associated pages 11-12, varela2022lebercongenitalamaurosisearlyonset pages 3-3) | MAXO: genome editing therapy |
| Low-vision rehabilitation | Supportive care | Not applicable | Standard supportive care | Clinical care programs | In use | Noninvasive rehabilitation | Important current management because many patients have profound, often lifelong visual impairment even when retinal structure is partially preserved; supportive measures remain standard while gene therapy access is limited (bouzia2020gucy2dassociatedlebercongenital pages 5-8, hahn2022thenaturalhistory pages 1-2, varela2022lebercongenitalamaurosisearlyonset pages 3-3) | MAXO: low vision rehabilitation |
| Orientation and mobility training | Supportive/rehabilitative care | Not applicable | Standard supportive care | Vision rehabilitation services | In use | Behavioral/rehabilitative intervention | Used to improve independent functioning and safety in severe congenital or progressive visual impairment typical of GUCY2D-LCA and advanced CORD (bouzia2020gucy2dassociatedlebercongenital pages 5-8, hahn2022thenaturalhistory pages 1-2) | MAXO: orientation and mobility training |
| Genetic counseling | Supportive/preventive care | Not applicable | Standard of care | Genetics/ophthalmic genetics services | In use | Counseling | Essential for confirming autosomal recessive risk in LCA1, autosomal dominant risk in CORD6, family planning, cascade testing, and clinical-trial eligibility assessment (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 1-5, hahn2022thenaturalhistory pages 1-2, bouzia2020gucy2dassociatedlebercongenital pages 5-8) | MAXO: genetic counseling |


*Table: This table summarizes the current therapeutic landscape for GUCY2D-related retinopathy, spanning active clinical gene therapy, preclinical programs, experimental genome editing concepts, and standard supportive care. It is useful for quickly comparing trial status, delivery route, reported outcomes, and knowledge-base-ready intervention terms.*

### Gene Therapy (ATSN-101)

The most advanced therapeutic intervention is **ATSN-101**, an AAV5-based gene augmentation therapy using the GRK1 promoter to deliver the human *GUCY2D* transgene via unilateral subretinal injection (boye2023preclinicalstudiesin pages 1-2, gong2024infantilenystagmussyndrome—associated pages 11-12). The Phase I/II clinical trial (NCT03920007), sponsored by Atsena Therapeutics Inc., enrolled 15 participants with biallelic *GUCY2D* mutations and is currently active but not recruiting (NCT03920007 chunk 1). Preliminary results report a mean improvement of 20.3 dB on full-field stimulus testing, with 3 of 6 treated patients reaching the maximum score on the Multi-Luminance Mobility Test (MLMT), and no serious adverse effects reported (saripalli2026genetherapyand pages 2-4). A separate publication in *The Lancet* (2024) described this as a multicentre, open-label, unilateral dose escalation study demonstrating safety and efficacy signals (wong2025monogenicretinaldiseases pages 21-21). The study completion date is estimated for May 2027, with estimated first results submission by September 2025 (NCT03920007 chunk 1).

GUCY2D-LCA is considered particularly favorable for gene therapy because of the characteristic preservation of central photoreceptor structure despite severe functional impairment, providing viable cellular targets for gene replacement (varela2022lebercongenitalamaurosisearlyonset pages 3-3).

### Preclinical Gene Therapy

Preclinical studies in GCDKO (guanylate cyclase 1/2 double knockout) mice demonstrated sustained and statistically significant improvements in both photopic (cone) and scotopic (rod) retinal function at 3 months post-injection with high-dose AAV5-hGRK1-GUCY2D (boye2023preclinicalstudiesin pages 1-2). Dose-ranging studies in cynomolgus monkeys established minimum effective doses, and GLP biodistribution and toxicology studies in rats and non-human primates supported clinical translation (boye2023preclinicalstudiesin pages 1-2). An avian model of childhood blindness also demonstrated vision restoration after lentiviral expression of RetGC-1 (bouzia2020gucy2dassociatedlebercongenital pages 14-16).

### CRISPR/Genome Editing

Successful knockout of the *GUCY2D* coding sequence in mouse and macaque photoreceptors has been demonstrated as proof-of-platform for retinal genome editing, though no disease-specific CRISPR clinical trial for GUCY2D retinopathy is currently active (gong2024infantilenystagmussyndrome—associated pages 11-12).

### Supportive Care

Current standard management includes low-vision rehabilitation, orientation and mobility training, educational support, and genetic counseling (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 5-8). MAXO terms: MAXO:0000015 (genetic counseling); MAXO:0001001 (gene therapy).

---

## 13. Prevention

### Primary Prevention

As a purely genetic disorder, primary prevention centers on:
- **Genetic counseling** (MAXO:0000015): Risk assessment, carrier identification, and family planning guidance for autosomal recessive (LCA1) and autosomal dominant (CORD6) inheritance patterns (varela2022lebercongenitalamaurosisearlyonset pages 3-3, bouzia2020gucy2dassociatedlebercongenital pages 1-5)
- **Carrier screening**: Relevant for consanguineous couples in populations with high carrier frequency
- **Preimplantation genetic diagnosis (PGD)** and **prenatal testing**: Available for families with known pathogenic variants

### Secondary Prevention

- **Early genetic diagnosis** through NGS panels enables timely identification and enrollment in clinical trials (huang2021leber’scongenitalamaurosis pages 5-6)
- **Cascade genetic testing** of family members to identify at-risk individuals (hahn2022thenaturalhistory pages 1-2)

### Tertiary Prevention

- **Gene therapy** (when available) aims to restore RetGC-1 function before irreversible photoreceptor loss (boye2023preclinicalstudiesin pages 1-2, varela2022lebercongenitalamaurosisearlyonset pages 3-3)
- **Low-vision aids** and rehabilitation to maximize functional vision (bouzia2020gucy2dassociatedlebercongenital pages 5-8)

---

## 14. Other Species / Natural Disease

### Comparative Biology

The mouse orthologue of *GUCY2D* is *Gucy2e*, with *Gucy2f* encoding the paralogous RetGC-2. The GCDKO (GC1/GC2 double knockout) mouse, carrying disruptions in both *Gucy2e* and *Gucy2f*, recapitulates the human LCA1 phenotype with loss of rod and cone photoreceptor function and has been the primary preclinical model for gene therapy development (boye2023preclinicalstudiesin pages 1-2). An avian (chicken) model of RetGC-1 deficiency has also been used to demonstrate vision restoration through gene therapy (bouzia2020gucy2dassociatedlebercongenital pages 14-16).

A recent publication (2025) describes a naturally occurring GUCY2D-associated retinopathy in **German Spitz dogs**, representing a veterinary comparative model (unobtained reference: Guareschi et al., Vet Sci 2025).

---

## 15. Model Organisms

### Mouse Models

- **GCDKO (GC1/GC2 double knockout)**: Carries disruptions in *Gucy2e* and *Gucy2f*; shows complete loss of rod and cone function with progressive photoreceptor degeneration. Gene therapy with AAV5-hGRK1-GUCY2D restores both scotopic and photopic retinal function (boye2023preclinicalstudiesin pages 1-2).
- **GC1 single knockout mice**: Used for studying cone arrestin translocation and testing AAV-GC1 gene therapy approaches (bouzia2020gucy2dassociatedlebercongenital pages 14-16).
- **Gucy2d-Cre knock-in mice**: Created via CRISPR/Cas9 for studying cellular expression patterns; show *Gucy2d* expression in spinal dorsal horn neurons in addition to retinal expression, though knockout mice do not exhibit altered behavioral responses under naïve conditions (OpenTargets Search: -GUCY2D).

### Avian Models

Chicken models of RetGC-1 deficiency have demonstrated successful lentiviral gene replacement therapy restoring vision, providing proof-of-concept for mammalian translation (bouzia2020gucy2dassociatedlebercongenital pages 14-16).

### Non-Human Primates

Cynomolgus monkeys (*Macaca fascicularis*) have been used for dose-ranging studies, biodistribution assessment, and toxicology evaluation of AAV5-hGRK1-GUCY2D in support of the ATSN-101 clinical trial (boye2023preclinicalstudiesin pages 1-2).

### Model Limitations

Mouse models have anatomical differences from the human retina (smaller eye, rod-dominant retina with no true macula), which limits direct translation of dosing parameters. Non-human primate models provide better anatomical correspondence but cannot model the disease phenotype since they have wild-type GUCY2D. The GCDKO mouse involves knockout of both RetGC isoforms rather than *Gucy2e* alone, creating a more severe phenotype than most human GUCY2D-LCA patients (boye2023preclinicalstudiesin pages 1-2).

---

## Summary

GUCY2D-related retinopathy represents a well-characterized spectrum of inherited retinal diseases ranging from congenital blindness (LCA1) to progressive cone-rod degeneration (CORD6), unified by dysfunction of the retinal guanylate cyclase-1 enzyme central to photoreceptor cGMP signaling. The disease is notable for the structure-function dissociation in the recessive form, where photoreceptors remain anatomically intact despite functional silence, creating a favorable therapeutic window for gene replacement therapy. The Phase I/II ATSN-101 clinical trial (NCT03920007) represents the most advanced therapeutic intervention, with preliminary results demonstrating safety and efficacy in restoring visual function in patients with decades-long congenital blindness. Continued development of gene therapy and potential genome editing approaches holds promise for transforming outcomes in this otherwise untreatable condition.

References

1. (varela2022lebercongenitalamaurosisearlyonset pages 3-3): Malena Daich Varela, Thales Antonio Cabral de Guimaraes, Michalis Georgiou, and Michel Michaelides. Leber congenital amaurosis/early-onset severe retinal dystrophy: current management and clinical trials. The British Journal of Ophthalmology, 106:445-451, Mar 2022. URL: https://doi.org/10.1136/bjophthalmol-2020-318483, doi:10.1136/bjophthalmol-2020-318483. This article has 97 citations.

2. (wong2025monogenicretinaldiseases pages 8-9): Wendy M. Wong and Omar A. Mahroo. Monogenic retinal diseases associated with genes encoding phototransduction proteins: a review. Clinical & Experimental Ophthalmology, 53:260-280, Feb 2025. URL: https://doi.org/10.1111/ceo.14511, doi:10.1111/ceo.14511. This article has 20 citations and is from a peer-reviewed journal.

3. (gao2023phenotypiccharacterizationof pages 1-2): Yunxia Gao, Xiang Ren, Hong Lin, Kang Li, Lirong Xiao, Xiaoyue Wang, Zhibing Zeng, Ruijin Ran, Yunhan Tao, Yu Lin, Xiangyu Fu, Naihong Yan, and Ming Zhang. Phenotypic characterization of autosomal dominant progressive cone dystrophies associated with a heterozygous variant c.2512c&gt;t of gucy2d gene in a large kindred. Eye, 37:2461-2469, Dec 2023. URL: https://doi.org/10.1038/s41433-022-02355-1, doi:10.1038/s41433-022-02355-1. This article has 1 citations and is from a peer-reviewed journal.

4. (bouzia2020gucy2dassociatedlebercongenital pages 1-5): Zaina Bouzia, Michalis Georgiou, Sarah Hull, Anthony G. Robson, Kaoru Fujinami, Tryfon Rotsos, Nikolas Pontikos, Gavin Arno, Andrew R. Webster, Alison J. Hardcastle, Alessia Fiorentino, and Michel Michaelides. Gucy2d-associated leber congenital amaurosis: a retrospective natural history study in preparation for trials of novel therapies. American Journal of Ophthalmology, 210:59-70, Feb 2020. URL: https://doi.org/10.1016/j.ajo.2019.10.019, doi:10.1016/j.ajo.2019.10.019. This article has 62 citations and is from a domain leading peer-reviewed journal.

5. (li2023cgmpsignalingin pages 4-5): Shujuan Li, Hongwei Ma, Fan Yang, and Xi-Qin Ding. Cgmp signaling in photoreceptor degeneration. International Journal of Molecular Sciences, 24:11200, Jul 2023. URL: https://doi.org/10.3390/ijms241311200, doi:10.3390/ijms241311200. This article has 36 citations.

6. (gong2024infantilenystagmussyndrome—associated pages 4-5): Xiaoming Gong and Richard W. Hertle. Infantile nystagmus syndrome—associated inherited retinal diseases: perspectives from gene therapy clinical trials. Life, 14:1356, Oct 2024. URL: https://doi.org/10.3390/life14111356, doi:10.3390/life14111356. This article has 2 citations.

7. (hahn2022thenaturalhistory pages 1-2): Leo C. Hahn, Michalis Georgiou, Hind Almushattat, Mary J. van Schooneveld, Emanuel R. de Carvalho, Nieneke L. Wesseling, Jacoline B. ten Brink, Ralph J. Florijn, Birgit I. Lissenberg-Witte, Ine Strubbe, Caroline van Cauwenbergh, Julie de Zaeytijd, Sophie Walraedt, Elfride de Baere, Rajarshi Mukherjee, Martin McKibbin, Magda A. Meester-Smoor, Alberta A.H.J. Thiadens, Saoud Al-Khuzaei, Engin Akyol, Andrew J. Lotery, Maria M. van Genderen, Jeannette Ossewaarde-van Norel, L. Ingeborgh van den Born, Carel B. Hoyng, Caroline C.W. Klaver, Susan M. Downes, Arthur A. Bergen, Bart P. Leroy, Michel Michaelides, and Camiel J.F. Boon. The natural history of leber congenital amaurosis and cone–rod dystrophy associated with variants in the gucy2d gene. Aug 2022. URL: https://doi.org/10.1016/j.oret.2022.03.008, doi:10.1016/j.oret.2022.03.008. This article has 25 citations and is from a peer-reviewed journal.

8. (OpenTargets Search: -GUCY2D): Open Targets Query (-GUCY2D, 45 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (huang2021leber’scongenitalamaurosis pages 5-6): Chu-Hsuan Huang, Chung-May Yang, Chang-Hao Yang, Yu-Chih Hou, and Ta-Ching Chen. Leber’s congenital amaurosis: current concepts of genotype-phenotype correlations. Genes, 12:1261, Aug 2021. URL: https://doi.org/10.3390/genes12081261, doi:10.3390/genes12081261. This article has 114 citations.

10. (hahn2022thenaturalhistory pages 5-7): Leo C. Hahn, Michalis Georgiou, Hind Almushattat, Mary J. van Schooneveld, Emanuel R. de Carvalho, Nieneke L. Wesseling, Jacoline B. ten Brink, Ralph J. Florijn, Birgit I. Lissenberg-Witte, Ine Strubbe, Caroline van Cauwenbergh, Julie de Zaeytijd, Sophie Walraedt, Elfride de Baere, Rajarshi Mukherjee, Martin McKibbin, Magda A. Meester-Smoor, Alberta A.H.J. Thiadens, Saoud Al-Khuzaei, Engin Akyol, Andrew J. Lotery, Maria M. van Genderen, Jeannette Ossewaarde-van Norel, L. Ingeborgh van den Born, Carel B. Hoyng, Caroline C.W. Klaver, Susan M. Downes, Arthur A. Bergen, Bart P. Leroy, Michel Michaelides, and Camiel J.F. Boon. The natural history of leber congenital amaurosis and cone–rod dystrophy associated with variants in the gucy2d gene. Aug 2022. URL: https://doi.org/10.1016/j.oret.2022.03.008, doi:10.1016/j.oret.2022.03.008. This article has 25 citations and is from a peer-reviewed journal.

11. (boye2023preclinicalstudiesin pages 1-2): Sanford L. Boye, Catherine O’Riordan, James Morris, Michael Lukason, David Compton, Rena Baek, Dana M. Elmore, James.J. Peterson, Diego Fajardo, K. Tyler McCullough, Abraham Scaria, Alison McVie-Wylie, and Shannon E. Boye. Preclinical studies in support of phase i/ii clinical trials to treat gucy2d-associated leber congenital amaurosis. Mar 2023. URL: https://doi.org/10.1016/j.omtm.2022.12.007, doi:10.1016/j.omtm.2022.12.007. This article has 10 citations.

12. (NCT03920007 chunk 1):  Study of Subretinally Injected ATSN-101 Administered in Patients With Leber Congenital Amaurosis Caused by Biallelic Mutations in GUCY2D. Atsena Therapeutics Inc.. 2019. ClinicalTrials.gov Identifier: NCT03920007

13. (donato2022theimpactof pages 7-10): Luigi Donato, Simona Alibrandi, Concetta Scimone, Carmela Rinaldi, Angela Dascola, Alessandro Calamuneri, Rosalia D’Angelo, and Antonina Sidoti. The impact of modifier genes on cone-rod dystrophy heterogeneity: an explorative familial pilot study and a hypothesis on neurotransmission impairment. PLOS ONE, 17:e0278857, Dec 2022. URL: https://doi.org/10.1371/journal.pone.0278857, doi:10.1371/journal.pone.0278857. This article has 51 citations and is from a peer-reviewed journal.

14. (bouzia2020gucy2dassociatedlebercongenital pages 5-8): Zaina Bouzia, Michalis Georgiou, Sarah Hull, Anthony G. Robson, Kaoru Fujinami, Tryfon Rotsos, Nikolas Pontikos, Gavin Arno, Andrew R. Webster, Alison J. Hardcastle, Alessia Fiorentino, and Michel Michaelides. Gucy2d-associated leber congenital amaurosis: a retrospective natural history study in preparation for trials of novel therapies. American Journal of Ophthalmology, 210:59-70, Feb 2020. URL: https://doi.org/10.1016/j.ajo.2019.10.019, doi:10.1016/j.ajo.2019.10.019. This article has 62 citations and is from a domain leading peer-reviewed journal.

15. (bouzia2020gucy2dassociatedlebercongenital pages 8-10): Zaina Bouzia, Michalis Georgiou, Sarah Hull, Anthony G. Robson, Kaoru Fujinami, Tryfon Rotsos, Nikolas Pontikos, Gavin Arno, Andrew R. Webster, Alison J. Hardcastle, Alessia Fiorentino, and Michel Michaelides. Gucy2d-associated leber congenital amaurosis: a retrospective natural history study in preparation for trials of novel therapies. American Journal of Ophthalmology, 210:59-70, Feb 2020. URL: https://doi.org/10.1016/j.ajo.2019.10.019, doi:10.1016/j.ajo.2019.10.019. This article has 62 citations and is from a domain leading peer-reviewed journal.

16. (huang2021leber’scongenitalamaurosis pages 1-2): Chu-Hsuan Huang, Chung-May Yang, Chang-Hao Yang, Yu-Chih Hou, and Ta-Ching Chen. Leber’s congenital amaurosis: current concepts of genotype-phenotype correlations. Genes, 12:1261, Aug 2021. URL: https://doi.org/10.3390/genes12081261, doi:10.3390/genes12081261. This article has 114 citations.

17. (bouzia2020gucy2dassociatedlebercongenital pages 10-14): Zaina Bouzia, Michalis Georgiou, Sarah Hull, Anthony G. Robson, Kaoru Fujinami, Tryfon Rotsos, Nikolas Pontikos, Gavin Arno, Andrew R. Webster, Alison J. Hardcastle, Alessia Fiorentino, and Michel Michaelides. Gucy2d-associated leber congenital amaurosis: a retrospective natural history study in preparation for trials of novel therapies. American Journal of Ophthalmology, 210:59-70, Feb 2020. URL: https://doi.org/10.1016/j.ajo.2019.10.019, doi:10.1016/j.ajo.2019.10.019. This article has 62 citations and is from a domain leading peer-reviewed journal.

18. (gao2023phenotypiccharacterizationof pages 7-8): Yunxia Gao, Xiang Ren, Hong Lin, Kang Li, Lirong Xiao, Xiaoyue Wang, Zhibing Zeng, Ruijin Ran, Yunhan Tao, Yu Lin, Xiangyu Fu, Naihong Yan, and Ming Zhang. Phenotypic characterization of autosomal dominant progressive cone dystrophies associated with a heterozygous variant c.2512c&gt;t of gucy2d gene in a large kindred. Eye, 37:2461-2469, Dec 2023. URL: https://doi.org/10.1038/s41433-022-02355-1, doi:10.1038/s41433-022-02355-1. This article has 1 citations and is from a peer-reviewed journal.

19. (li2023cgmpsignalingin pages 2-4): Shujuan Li, Hongwei Ma, Fan Yang, and Xi-Qin Ding. Cgmp signaling in photoreceptor degeneration. International Journal of Molecular Sciences, 24:11200, Jul 2023. URL: https://doi.org/10.3390/ijms241311200, doi:10.3390/ijms241311200. This article has 36 citations.

20. (bouzia2020gucy2dassociatedlebercongenital pages 16-20): Zaina Bouzia, Michalis Georgiou, Sarah Hull, Anthony G. Robson, Kaoru Fujinami, Tryfon Rotsos, Nikolas Pontikos, Gavin Arno, Andrew R. Webster, Alison J. Hardcastle, Alessia Fiorentino, and Michel Michaelides. Gucy2d-associated leber congenital amaurosis: a retrospective natural history study in preparation for trials of novel therapies. American Journal of Ophthalmology, 210:59-70, Feb 2020. URL: https://doi.org/10.1016/j.ajo.2019.10.019, doi:10.1016/j.ajo.2019.10.019. This article has 62 citations and is from a domain leading peer-reviewed journal.

21. (areblom2023adescriptionof pages 9-10): Maria Areblom, Sten Kjellström, Sten Andréasson, Anders Öhberg, Lotta Gränse, and Ulrika Kjellström. A description of the yield of genetic reinvestigation in patients with inherited retinal dystrophies and previous inconclusive genetic testing. Genes, 14:1413, Jul 2023. URL: https://doi.org/10.3390/genes14071413, doi:10.3390/genes14071413. This article has 7 citations.

22. (donato2022theimpactof pages 10-11): Luigi Donato, Simona Alibrandi, Concetta Scimone, Carmela Rinaldi, Angela Dascola, Alessandro Calamuneri, Rosalia D’Angelo, and Antonina Sidoti. The impact of modifier genes on cone-rod dystrophy heterogeneity: an explorative familial pilot study and a hypothesis on neurotransmission impairment. PLOS ONE, 17:e0278857, Dec 2022. URL: https://doi.org/10.1371/journal.pone.0278857, doi:10.1371/journal.pone.0278857. This article has 51 citations and is from a peer-reviewed journal.

23. (li2023cgmpsignalingin pages 13-14): Shujuan Li, Hongwei Ma, Fan Yang, and Xi-Qin Ding. Cgmp signaling in photoreceptor degeneration. International Journal of Molecular Sciences, 24:11200, Jul 2023. URL: https://doi.org/10.3390/ijms241311200, doi:10.3390/ijms241311200. This article has 36 citations.

24. (li2023cgmpsignalingin pages 11-13): Shujuan Li, Hongwei Ma, Fan Yang, and Xi-Qin Ding. Cgmp signaling in photoreceptor degeneration. International Journal of Molecular Sciences, 24:11200, Jul 2023. URL: https://doi.org/10.3390/ijms241311200, doi:10.3390/ijms241311200. This article has 36 citations.

25. (bouzia2020gucy2dassociatedlebercongenital pages 14-16): Zaina Bouzia, Michalis Georgiou, Sarah Hull, Anthony G. Robson, Kaoru Fujinami, Tryfon Rotsos, Nikolas Pontikos, Gavin Arno, Andrew R. Webster, Alison J. Hardcastle, Alessia Fiorentino, and Michel Michaelides. Gucy2d-associated leber congenital amaurosis: a retrospective natural history study in preparation for trials of novel therapies. American Journal of Ophthalmology, 210:59-70, Feb 2020. URL: https://doi.org/10.1016/j.ajo.2019.10.019, doi:10.1016/j.ajo.2019.10.019. This article has 62 citations and is from a domain leading peer-reviewed journal.

26. (saripalli2026genetherapyand pages 2-4): Karthik Saripalli. Gene therapy and leber congenital amaurosis: a review of treatments and clinical trials. American Journal of Student Research, pages 143-151, Jan 2026. URL: https://doi.org/10.70251/hyjr2348.41143151, doi:10.70251/hyjr2348.41143151. This article has 0 citations.

27. (wong2025monogenicretinaldiseases pages 21-21): Wendy M. Wong and Omar A. Mahroo. Monogenic retinal diseases associated with genes encoding phototransduction proteins: a review. Clinical & Experimental Ophthalmology, 53:260-280, Feb 2025. URL: https://doi.org/10.1111/ceo.14511, doi:10.1111/ceo.14511. This article has 20 citations and is from a peer-reviewed journal.

28. (NCT03920007 chunk 2):  Study of Subretinally Injected ATSN-101 Administered in Patients With Leber Congenital Amaurosis Caused by Biallelic Mutations in GUCY2D. Atsena Therapeutics Inc.. 2019. ClinicalTrials.gov Identifier: NCT03920007

29. (boye2023preclinicalstudiesin pages 16-16): Sanford L. Boye, Catherine O’Riordan, James Morris, Michael Lukason, David Compton, Rena Baek, Dana M. Elmore, James.J. Peterson, Diego Fajardo, K. Tyler McCullough, Abraham Scaria, Alison McVie-Wylie, and Shannon E. Boye. Preclinical studies in support of phase i/ii clinical trials to treat gucy2d-associated leber congenital amaurosis. Mar 2023. URL: https://doi.org/10.1016/j.omtm.2022.12.007, doi:10.1016/j.omtm.2022.12.007. This article has 10 citations.

30. (gong2024infantilenystagmussyndrome—associated pages 11-12): Xiaoming Gong and Richard W. Hertle. Infantile nystagmus syndrome—associated inherited retinal diseases: perspectives from gene therapy clinical trials. Life, 14:1356, Oct 2024. URL: https://doi.org/10.3390/life14111356, doi:10.3390/life14111356. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](GUCY2D-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](GUCY2D-Related_Retinopathy-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](GUCY2D-Related_Retinopathy-deep-research-falcon_artifacts/artifact-02.md)
- [Edison artifact artifact-03](GUCY2D-Related_Retinopathy-deep-research-falcon_artifacts/artifact-03.md)