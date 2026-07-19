---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-08T11:54:42.261427'
end_time: '2026-07-08T12:25:29.368734'
duration_seconds: 1847.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glioma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 76
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 4
artifacts:
- filename: artifact-00.md
  path: Glioma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Glioma-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Glioma-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: artifact-03.md
  path: Glioma-deep-research-falcon_artifacts/artifact-03.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-03
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glioma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Glioma** covering all of the
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
- **Disease Name:** Glioma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Glioma** covering all of the
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


# Glioma (Cancer) — Disease Characteristics Research Report (WHO CNS5 / 2023–2024 prioritized)

## 1. Disease information

### 1.1 Overview / definition
Glioma is an umbrella term for primary central nervous system (CNS) tumors with glial or glial‑precursor lineage features; modern classification is based on *integrated diagnosis* combining histopathology with molecular alterations rather than morphology alone. (osborn2022the2021world pages 1-3, mcnamara20222021whoclassification pages 1-6)

In WHO CNS5 (5th edition, published 2021), **adult-type diffuse gliomas** were simplified into three principal, molecularly defined types: **(i) astrocytoma, IDH-mutant; (ii) oligodendroglioma, IDH-mutant and 1p/19q-codeleted; (iii) glioblastoma, IDH-wildtype**, with grading embedded within type (“within-type grading”). (reuss2023updatesonthe pages 1-2, mcnamara20222021whoclassification pages 6-9, osborn2022the2021world pages 1-3)

WHO CNS5 also emphasizes **layered reporting**, where the “integrated diagnosis” is presented as the top line, followed by histologic diagnosis, WHO grade, and the key molecular information supporting the classification. (osborn2022the2021world pages 1-3)

### 1.2 Key identifiers (available from retrieved sources)
* **WHO classification standard**: WHO Classification of Tumors of the Central Nervous System, 5th edition (WHO CNS5), summarized in *Neuro-Oncology* (June 2021; DOI: https://doi.org/10.1093/neuonc/noab106). (reuss2023updatesonthe pages 1-2)
* **MONDO ID**: Not retrieved from the tool evidence in this run (therefore not asserted).
* **ICD/MeSH/OMIM/Orphanet**: Not retrieved from the tool evidence in this run (therefore not asserted).

### 1.3 Synonyms / alternative names
Key terminology changes affect how older literature maps onto WHO CNS5. Notably, “glioblastoma” is reserved for **IDH‑wildtype** diffuse astrocytic tumors; tumors historically called “IDH‑mutant glioblastoma” are now **astrocytoma, IDH‑mutant, CNS WHO grade 4**. (reuss2023updatesonthe pages 1-2, mcnamara20222021whoclassification pages 6-9)

| Concept | Common synonyms / legacy terms | Key defining features (short) | Primary authoritative source (URL + year) |
|---|---|---|---|
| Glioma (broad) | Glial tumor; glial neoplasm; diffuse glioma (when infiltrative subset is intended) | Broad umbrella for primary CNS tumors arising from glial or glial-precursor lineages; current WHO CNS5 diagnosis is integrated, combining histology with molecular features rather than morphology alone (osborn2022the2021world pages 1-3, mcnamara20222021whoclassification pages 1-6) | Louis et al., *The 2021 WHO Classification of Tumors of the Central Nervous System: a summary* — https://doi.org/10.1093/neuonc/noab106 (2021) |
| Adult-type diffuse glioma | Adult diffuse glioma; infiltrating adult glioma; diffuse astrocytic/oligodendroglial tumor | WHO CNS5 simplifies adult diffuse gliomas into 3 molecularly defined types: astrocytoma, IDH-mutant; oligodendroglioma, IDH-mutant and 1p/19q-codeleted; glioblastoma, IDH-wildtype. Uses integrated/layered diagnosis and molecular grading (mcnamara20222021whoclassification pages 6-9, osborn2022the2021world pages 1-3) | McNamara et al., *2021 WHO classification of tumours of the central nervous system: a review for the neuroradiologist* — https://doi.org/10.1007/s00234-022-03008-6 (2022) |
| Astrocytoma, IDH-mutant | Diffuse astrocytoma, IDH-mutant; anaplastic astrocytoma, IDH-mutant; legacy “IDH-mutant glioblastoma” now grade 4 astrocytoma | Defined by IDH1 or IDH2 mutation with astrocytic lineage; typically supported by ATRX loss/mutation and TP53 alteration or absence of 1p/19q codeletion; graded CNS WHO 2–4, and CDKN2A/B homozygous deletion can justify grade 4 (reuss2023updatesonthe pages 1-2, mcnamara20222021whoclassification pages 6-9, antonelli2022adulttypediffuse pages 1-2) | Reuss, *Updates on the WHO diagnosis of IDH-mutant glioma* — https://doi.org/10.1007/s11060-023-04250-5 (2023) |
| Oligodendroglioma, IDH-mutant and 1p/19q-codeleted | Oligodendroglioma, IDH-mutant, 1p/19q-codeleted; anaplastic oligodendroglioma (legacy grade-based term) | Diffusely infiltrating glioma defined by both IDH mutation and whole-arm 1p/19q codeletion; often associated with TERT promoter, CIC, and FUBP1 alterations; graded CNS WHO 2–3 (reuss2023updatesonthe pages 1-2, gue2024the2021world pages 19-21) | Louis et al., *The 2021 WHO Classification of Tumors of the Central Nervous System: a summary* — https://doi.org/10.1093/neuonc/noab106 (2021) |
| Glioblastoma, IDH-wildtype | GBM; primary glioblastoma; glioblastoma multiforme (older term) | In WHO CNS5, the term “glioblastoma” is reserved for adult diffuse astrocytic glioma that is IDH-wildtype; diagnosis may be made by classic histology or by molecular features such as TERT promoter mutation, EGFR amplification, or combined whole chromosome 7 gain / whole chromosome 10 loss (+7/−10) even without necrosis or microvascular proliferation (mcnamara20222021whoclassification pages 6-9, osborn2022the2021world pages 1-3, mcnamara20222021whoclassification pages 1-6) | Osborn et al., *The 2021 World Health Organization Classification of Tumors of the Central Nervous System: What Neuroradiologists Need to Know* — https://doi.org/10.3174/ajnr.45-12.s15 (2022) |


*Table: This table summarizes key WHO CNS5 glioma concepts, including current terminology, common legacy names, and the molecular features that define each entity. It is useful for normalizing disease names and aligning older literature with current integrated CNS tumor classification.*

### 1.4 Evidence provenance
This report primarily synthesizes **aggregated disease-level resources** (WHO CNS5, CBTRUS population registry report) and **cohort/registry studies**, plus selected clinical guidelines and trials. (reuss2023updatesonthe pages 1-2, price2024cbtrusstatisticalreport pages 2-3, hainfellner2024glioblastomainthe pages 1-3)

## 2. Etiology

### 2.1 Causal factors (mechanistic / genetic)
WHO CNS5 frames adult diffuse glioma causation and taxonomy around canonical molecular alterations. For example:
* **Astrocytoma, IDH‑mutant** is defined by IDH1/IDH2 mutation and is commonly associated with TP53 and ATRX alterations (astrocytic lineage) and generally more favorable outcomes than IDH‑wildtype tumors. (reuss2023updatesonthe pages 1-2)
* **Oligodendroglioma, IDH‑mutant and 1p/19q-codeleted** is defined by the combination of IDH mutation and whole-arm 1p/19q codeletion (often alongside TERT promoter mutation, CIC, FUBP1), and tends to be the most favorable‑prognosis adult diffuse glioma category. (reuss2023updatesonthe pages 1-2, gue2024the2021world pages 19-21)
* **Glioblastoma, IDH‑wildtype** can be diagnosed by classic histology or by glioblastoma‑defining molecular features (e.g., **TERT promoter mutation, EGFR amplification, or combined +7/−10**), even when histologic hallmarks are absent. (mcnamara20222021whoclassification pages 6-9, osborn2022the2021world pages 1-3)

### 2.2 Risk factors
#### 2.2.1 Genetic predisposition (germline)
A 2023 single-institution paired tumor/normal sequencing series of **152 adult-type diffuse glioma patients** reported **pathogenic germline variants in 9.8% (15/152)**, with higher prevalence in **glioblastoma, IDH‑wildtype (13.1%)** than in IDH‑mutant astrocytoma (7.1%) or oligodendroglioma (3.8%). (mcdonald2023prevalenceofpathogenic pages 1-2, mcdonald2023prevalenceofpathogenic pages 5-7)

Most frequent germline pathogenic variants in that cohort were **BRCA2, MUTYH, and CHEK2 (each 20% of pathogenic variants)**, with additional variants in BRCA1, ATM, NF1, MSH2, MSH3. (mcdonald2023prevalenceofpathogenic pages 1-2, mcdonald2023prevalenceofpathogenic pages 5-7)

**Implementation gap:** only **40%** of patients with pathogenic germline variants were referred to genetics, despite potential implications for surveillance and family cascade testing. (mcdonald2023prevalenceofpathogenic pages 2-3, mcdonald2023prevalenceofpathogenic pages 5-7)

For pediatric CNS tumors (including glioma subtypes within the broader category), an AACR Cancer Predisposition Working Group update states that germline predisposition incidence “continues to grow” and that **~50%** of patients may be the **first in a family** identified to have a predisposition; identification enables **cascade testing** and **early tumor surveillance** and can impact management. (hansford2024updateoncancer pages 1-2)

#### 2.2.2 Environmental / lifestyle
No high-quality, specific environmental or protective factors were retrieved with tool evidence in this run; therefore, none are asserted.

### 2.3 Protective factors
No evidence was retrieved in this run for protective factors in glioma risk; therefore, none are asserted.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was retrieved in this run; therefore, none are asserted.

## 3. Phenotypes

### 3.1 Common clinical phenotypes (symptoms/signs) and QoL impact
Clinical guideline evidence emphasizes that neurologic symptoms can substantially impair quality of life in high-grade glioma. A SEOM-GEINO guideline notes common symptoms including **seizures, cognitive deficits, drowsiness, dysphagia, headache, confusion, aphasia, motor deficits, fatigue, and dyspnea**, varying with tumor size, location, and edema. (segura2023seomgeinoclinicalguidelines pages 2-4)

Supportive care priorities include management of brain edema (e.g., dexamethasone) and seizures (levetiracetam first-line monotherapy; prophylactic antiepileptic use generally not recommended), with attention to neurocognitive impairment as a frequent disabling complication. (segura2023seomgeinoclinicalguidelines pages 7-8, segura2023seomgeinoclinicalguidelines pages 8-9)

### 3.2 Suggested HPO terms (non-exhaustive; mapping guidance)
* Seizures — **HP:0001250**
* Headache — **HP:0002315**
* Aphasia — **HP:0002381**
* Cognitive impairment — **HP:0100543**
* Fatigue — **HP:0012378**
* Motor weakness — **HP:0001324**
* Dysphagia — **HP:0002015**

(These HPO IDs are provided as standard ontology mappings; this run did not retrieve HPO source documents, so they are presented as ontology suggestions rather than evidence-derived claims.)

## 4. Genetic / molecular information

### 4.1 Core disease-defining genes and alterations (adult-type diffuse gliomas)
WHO CNS5/related reviews emphasize the following diagnostic anchors:
* **IDH1/IDH2 mutations** define IDH-mutant astrocytoma and oligodendroglioma categories; TP53/ATRX alterations support astrocytic lineage, while 1p/19q codeletion supports oligodendroglial lineage. (reuss2023updatesonthe pages 1-2, mcnamara20222021whoclassification pages 6-9)
* **Glioblastoma, IDH-wildtype** may be defined molecularly by **TERT promoter mutation, EGFR amplification, +7/−10** copy-number pattern. (mcnamara20222021whoclassification pages 6-9)

### 4.2 Epigenetics and methylation profiling
DNA methylation profiling is increasingly important for CNS tumor diagnosis and subgrouping. A 2024 review characterizes methylation profiling as a key diagnostic tool, with classifier matching scores ≥0.9 in ~**50–65%** of samples and “diagnostic impact” in **~10–20%** of cases. (bertero2024molecularneuropathologyan pages 3-4)

### 4.3 Multi-omics and functional genomics (recent developments)
In pediatric low-grade glioma diagnostics, a 2023 international registry analysis (LOGGIC) reported that adding **RNA-seq** increased driver detection from **75% to 97%** (121/125), with **27/125 (22%)** having drivers detected only by RNA-seq (22 actionable), supporting routine RNA-seq integration when standard approaches are unrevealing. (hardin2023loggiccorebioclinical pages 1-2, hardin2023loggiccorebioclinical pages 3-5)

## 5. Environmental information
No high-confidence environmental toxin/lifestyle/infectious causal evidence was retrieved in this run for glioma; therefore, no specific environmental claims are made.

## 6. Mechanism / pathophysiology

### 6.1 Core mechanistic concepts (WHO CNS5 perspective)
WHO CNS5 frames glioma biology around canonical molecular alterations and their downstream phenotypes. Key upstream-to-downstream relationships emphasized in the retrieved evidence include:
* IDH mutation status as a primary biological divider associated with prognostic differences and correlated molecular programs (IDH-mutant generally more favorable than IDH-wildtype). (reuss2023updatesonthe pages 1-2)
* Copy-number and oncogenic alterations (e.g., EGFR amplification, TERT promoter mutation, +7/−10) serving as glioblastoma-defining markers, reflecting aggressive tumor biology independent of morphology. (mcnamara20222021whoclassification pages 6-9)

### 6.2 Suggested GO biological process terms (examples; ontology suggestions)
* Cell proliferation — **GO:0008283**
* DNA repair — **GO:0006281**
* Regulation of cell cycle — **GO:0051726**
* Angiogenesis — **GO:0001525**

(Provided as ontology suggestions; GO source documents were not retrieved in this run.)

### 6.3 Suggested Cell Ontology (CL) terms (examples; ontology suggestions)
* Astrocyte — **CL:0000127**
* Oligodendrocyte — **CL:0000128**
* Microglial cell — **CL:0000129**

## 7. Anatomical structures affected
Gliomas are CNS tumors affecting brain and spinal cord structures; adult diffuse gliomas are typically infiltrative within brain parenchyma. Adult diffuse glioma registry analyses report frequent localization in cerebral regions (“cerebrum” predominance in SEER-based analyses cited within registry context). (zhao2024emergingtrendsin pages 11-14)

**Suggested UBERON terms (examples; ontology suggestions):**
* Brain — **UBERON:0000955**
* Cerebrum — **UBERON:0001869**

## 8. Temporal development

### 8.1 Onset
In a Belgian population registry cohort of adult-type diffuse glioma (2017–2019), median age at diagnosis was **64 years**, consistent with adult-onset predominance for diffuse adult-type gliomas in population data. (pinson2024epidemiologyandsurvival pages 1-2)

### 8.2 Progression
Diffuse gliomas are infiltrative and often recur/progress despite therapy; WHO CNS5 emphasizes molecular classification and grading to better predict progression risk. (mcnamara20222021whoclassification pages 6-9, osborn2022the2021world pages 1-3)

## 9. Inheritance and population

### 9.1 Epidemiology (recent)
The **CBTRUS Statistical Report (US; diagnosed 2017–2021; published Oct 2024)** reports:
* Gliomas accounted for **22.9%** of all primary brain/CNS tumors.
* Glioblastoma accounted for **14.0% of all tumors** and **51.5% of malignant tumors**.
* Malignant brain/CNS tumor incidence: **6.89 per 100,000** overall; **8.06 per 100,000 in males** vs **5.84 per 100,000 in females**.
* Malignant brain/CNS tumor mortality: **4.41 per 100,000**, with **87,053 deaths** during 2017–2021.
* 5-year relative survival for malignant brain/CNS tumors overall: **35.7%**.
(price2024cbtrusstatisticalreport pages 2-3)

A Belgian national cancer registry analysis of **adult-type diffuse gliomas (2017–2019; published Aug 2024)** estimated an age-standardized incidence rate of **8.55 per 100,000 person-years** for diffuse adult-type glioma and **6.72 per 100,000 person-years** for grade 4 lesions. (pinson2024epidemiologyandsurvival pages 1-2)

| Dataset / population | Location / diagnosis years | Key epidemiology statistics | Key survival statistics | Source |
|---|---|---|---|---|
| CBTRUS Statistical Report: all primary brain and other CNS tumors, with glioma-relevant subset | United States; diagnosed 2017-2021 | Gliomas accounted for **22.9%** of all primary brain/CNS tumors. Glioblastoma accounted for **14.0% of all tumors** and **51.5% of all malignant tumors**. Overall malignant brain/CNS tumor incidence was **6.89 per 100,000**; by sex, **8.06 per 100,000 in males** vs **5.84 per 100,000 in females**. Malignant brain/CNS tumor mortality was **4.41 per 100,000** (average annual mortality), with **87,053 deaths** during 2017-2021. (price2024cbtrusstatisticalreport pages 2-3) | **5-year relative survival for malignant brain/CNS tumors: 35.7%**. (price2024cbtrusstatisticalreport pages 2-3) | Price et al., *Neuro-Oncology* 2024, published Oct 2024. https://doi.org/10.1093/neuonc/noae145 |
| Belgian population-based adult-type diffuse glioma registry | Belgium; diagnosed 2017-2019 | **2,233** adult-type diffuse gliomas identified; **40.1% female**; median age **64 years**. Age-standardized incidence rate (ASR) for diffuse adult-type glioma: **8.55 per 100,000 person-years**. ASR for grade 4 lesions: **6.72 per 100,000 person-years**. (pinson2024epidemiologyandsurvival pages 1-2, pinson2024epidemiologyandsurvival pages 3-4) | **Median OS 9.3 months** for IDH-wildtype glioblastoma; **25.9 months** for grade 4 IDH-mutant astrocytoma. **3-year survival**: IDH-mutant astrocytoma grade 2 **86.0%**, grade 3 **75.7%**; IDH-wildtype astrocytoma grade 2 **31.6%**, grade 3 **5.7%**; oligodendroglioma grade 2 **93.4%**, grade 3 **64.2%**; grade 4 lesions overall **6.5%**. (pinson2024epidemiologyandsurvival pages 1-2, pinson2024epidemiologyandsurvival pages 3-4) | Pinson et al., *Neuro-Oncology* 2024, published Aug 2024. https://doi.org/10.1093/neuonc/noad158 |
| Belgian registry contextual comparison with prior US glioblastoma incidence estimate | Belgium study citing US data; US comparator largely 2015-2019 | Study notes CBTRUS-reported glioblastoma ASR in the US population of **3.26 per 100,000 person-years**. (pinson2024epidemiologyandsurvival pages 4-6) | Provides context that real-world glioblastoma outcomes remain poor relative to molecularly favorable diffuse glioma subtypes. (pinson2024epidemiologyandsurvival pages 4-6) | Pinson et al., *Neuro-Oncology* 2024. https://doi.org/10.1093/neuonc/noad158 |


*Table: This table compiles recent population-level glioma epidemiology and survival figures from the 2024 CBTRUS report and a 2024 Belgian molecular-era registry. It is useful for contrasting broad U.S. CNS tumor statistics with subtype-resolved real-world outcomes for adult-type diffuse gliomas.*

### 9.2 Inheritance patterns
Most adult diffuse gliomas are sporadic, but a clinically meaningful minority show germline pathogenic variants; a 2023 cohort found ~**10%** with pathogenic germline variants (see Etiology). (mcdonald2023prevalenceofpathogenic pages 1-2)

## 10. Diagnostics

WHO CNS5-era diagnostic practice is integrated and multi-assay. Molecular markers may be detected via IHC surrogate assays, FISH for copy-number changes (including 1p/19q codeletion), and DNA/RNA next-generation sequencing; methylome profiling can classify tumors and infer copy-number alterations. (osborn2022the2021world pages 1-3)

Methylation profiling and NGS are described as core parts of the evolving molecular neuropathology toolbox, with methylation profiling “critical” for complex cases and for subgrouping heterogeneous entities; targeted sequencing is practical for routine diagnostics and may reveal targets for emerging therapies. (bertero2024molecularneuropathologyan pages 1-3, bertero2024molecularneuropathologyan pages 3-4)

Liquid biopsy remains investigational. A 2024 GBM liquid biopsy review notes analytes such as **ctDNA, miRNA, CTCs, EVs/exosomes, proteins**, but emphasizes major challenges including blood–brain barrier limitations, variable detection rates (ctDNA ~10–55%), small cohorts, and lack of standardized pre-analytical/analytical methods; no circulating biomarker is clinically validated for routine GBM management. (seyhan2024circulatingliquidbiopsy pages 48-49, seyhan2024circulatingliquidbiopsy pages 1-2)

For CSF cfDNA in glioma, a 2024 review reports NGS detection of tumor-specific mutations in **70% of glioma cases**, **82.5%** in brainstem glioma with targeted panels, and **97.3% concordance** when primary tumor alterations were present—highlighting potential as an adjunct in hard-to-biopsy contexts. (otsuji2024liquidbiopsyfor pages 12-14)

| Modality | What it detects | Typical use case | Key limitations | Recent evidence/examples with year + URL |
|---|---|---|---|---|
| MRI (standard structural MRI; advanced MRI adjuncts) | Tumor location, size, contrast enhancement, edema, mass effect; supports response/progression assessment | First-line detection, surgical planning, longitudinal monitoring, distinguishing enhancing vs non-enhancing disease | Limited specificity for molecular subtype; may not reliably distinguish progression from treatment effect/pseudoprogression | Standard imaging remains central in WHO-era glioma workup; radiologists integrate imaging with molecular classification (2022, https://doi.org/10.3174/ajnr.45-12.s15) (osborn2022the2021world pages 1-3) |
| Histopathology + immunohistochemistry (IHC) | Morphology plus surrogate protein markers such as IDH1 R132H, ATRX loss, p53 overexpression, H3K27M, BRAF V600E | Core tissue diagnosis after biopsy/resection; rapid subtype orientation and grading support | Sampling bias, interobserver variability, limited sensitivity for non-canonical mutations/fusions; cannot alone resolve all integrated diagnoses | WHO CNS5 layered diagnosis still relies on histology/IHC alongside molecular data (2022, https://doi.org/10.3174/ajnr.45-12.s15) (osborn2022the2021world pages 1-3) |
| FISH | 1p/19q codeletion, EGFR amplification, CDKN2A/B deletion and other copy-number events | Confirm oligodendroglioma-defining 1p/19q status; support glioblastoma-defining alterations when needed | Target-limited assay; may miss genome-wide context or complex chromosomal architecture | FISH remains part of the molecular toolbox for diffuse glioma classification in WHO CNS5 practice (2022, https://doi.org/10.3174/ajnr.45-12.s15) (osborn2022the2021world pages 1-3) |
| DNA NGS panels | SNVs/indels in genes such as IDH1/2, TP53, ATRX, TERT promoter, H3 genes; some copy-number calls depending on panel | Practical routine molecular workup for adult and pediatric gliomas; diagnosis, prognostication, and actionable target finding | Panel content constrains discovery; may miss fusions/structural events; lower utility for epigenetic subgrouping | Targeted DNA sequencing is described as the most practical routine approach and can detect diagnostically relevant alterations in >50% of CNS tumors (2024, https://doi.org/10.1007/s00428-023-03632-4) (bertero2024molecularneuropathologyan pages 3-4, bertero2024molecularneuropathologyan pages 1-3) |
| RNA-seq | Gene fusions, splice variants, expressed rearrangements; can reveal hidden drivers such as FGFR1 ITD and rare kinase fusions | Especially valuable in pediatric low-grade glioma and fusion-driven tumors when panel/IHC are unrevealing | Requires high-quality nucleic acid/bioinformatics; less commonly informative in adult diffuse glioma; tissue handling constraints | In LOGGIC pLGG, adding RNA-seq raised driver detection from 75% to 97%; 27/125 cases had drivers found only by RNA-seq and 22 were actionable (2023, https://doi.org/10.1093/neuonc/noad078) (hardin2023loggiccorebioclinical pages 3-5, hardin2023loggiccorebioclinical pages 1-2) |
| DNA methylation profiling (classifier) | Tumor-class methylome signature plus genome-wide copy-number profile; can refine subtype, resolve ambiguous cases, and support grading/class assignment | Difficult/ambiguous cases, novel entities, subclassification, integrated diagnosis under WHO CNS5 | Not all samples achieve high-confidence match; specialized platforms/classifiers required; interpretation expertise needed | Described as a critical/most impactful diagnostic tool; match scores ≥0.9 in ~50-65% of samples with diagnostic impact in ~10-20% of cases (2024, https://doi.org/10.1007/s00428-023-03632-4); DKFZ classifier v12.5 added >10 novel methylation classes (2023, https://doi.org/10.1007/s10014-022-00446-1) (bertero2024molecularneuropathologyan pages 3-4, bertero2024molecularneuropathologyan pages 1-3, komori2023updateofthe pages 1-2) |
| CSF ctDNA liquid biopsy | Tumor-derived mutations/copy-number alterations in CSF cfDNA; can reflect IDH1, TERT, TP53, PTEN and other glioma alterations | Adjunct when biopsy is risky, deep/brainstem lesions, postoperative monitoring, molecular follow-up | Blood-brain barrier limits blood sensitivity; CSF acquisition is invasive; no standardization; not a replacement for tissue diagnosis | Reviews emphasize ctDNA/CTCs/miRNA/EVs as promising but limited by BBB and lack of standardized workflows (2024, https://doi.org/10.3390/ijms25147974; 2024, https://doi.org/10.3390/cancers16051009). Reported CSF cfDNA mutation detection includes 70% in gliomas, 82.5% in brainstem glioma, and 97.3% concordance when tumor alterations are present (2024, https://doi.org/10.3390/cancers16051009) (seyhan2024circulatingliquidbiopsy pages 48-49, seyhan2024circulatingliquidbiopsy pages 49-51, seyhan2024circulatingliquidbiopsy pages 1-2, otsuji2024liquidbiopsyfor pages 12-14) |


*Table: This table summarizes the main current diagnostic modalities used in glioma care, what each modality detects, where it is most useful, and key limitations. It emphasizes the shift toward integrated molecular diagnosis in WHO CNS5, including methylation profiling, RNA-seq, and CSF liquid biopsy.*

## 11. Outcome / prognosis

### 11.1 High-grade glioma / glioblastoma prognosis
A 2023 high-grade glioma guideline states glioblastoma has a grim prognosis with **median overall survival ~15 months** and **5-year survival 5–10%**. (segura2023seomgeinoclinicalguidelines pages 1-2)

In real-world Austrian population data (2014–2018; published Aug 2024), median OS for 1,420 glioblastoma patients was **11.6 months** overall and **16.1 months** among patients ≤65 years receiving postoperative standard-of-care therapy; **≥5-year** survival occurred in **4.9%** of those with ≥5-year follow-up. (hainfellner2024glioblastomainthe pages 1-3)

### 11.2 Prognostic stratification by molecular subtype (real-world molecular era)
A Belgian registry study (2017–2019) showed marked survival differences by molecular subtype: **median OS 9.3 months** for IDH‑wildtype glioblastoma vs **25.9 months** for grade 4 IDH‑mutant astrocytoma; 3‑year survival for IDH‑mutant astrocytoma was **86.0% (grade 2)** and **75.7% (grade 3)**. (pinson2024epidemiologyandsurvival pages 1-2)

## 12. Treatment

### 12.1 Standard of care (adult high-grade glioma / glioblastoma)
Guidelines emphasize multimodal treatment with **maximal safe resection**, **radiotherapy**, and **temozolomide-based chemotherapy** (Stupp regimen). (segura2023seomgeinoclinicalguidelines pages 4-5, segura2023seomgeinoclinicalguidelines pages 2-4)

### 12.2 Device-based therapy: Tumor Treating Fields (TTFields)
A 2023 systematic review/meta-analysis of real-world TTFields studies found improved OS when TTFields was added to standard chemoradiotherapy (pooled **HR 0.63**, 95% CI 0.53–0.75), with pooled median OS **22.6 months** (TTFields) vs **17.4 months** (no TTFields). (ballo2023associationoftumor pages 1-2)

A 2024 global post-marketing safety surveillance analysis (>25,000 treated CNS malignancy patients) reported most common TTFields-related adverse events were localized scalp reactions: beneath-array skin reaction **43%**, tingling **14%**, warmth **12%**, with **no TTFields-related systemic adverse events** reported. (mrugala2024globalpost‑marketingsafety pages 1-2)

### 12.3 Precision therapy for IDH-mutant grade 2 glioma: vorasidenib (INDIGO)
The phase 3 INDIGO trial (NEJM, Aug 2023; DOI: https://doi.org/10.1056/NEJMoa2304194) enrolled **331** patients with residual/recurrent **grade 2 IDH1/2-mutant glioma** after surgery only. Vorasidenib significantly improved median imaging-based PFS (**27.7 vs 11.1 months**, HR **0.39**) and delayed time to next intervention (HR **0.26**). (mellinghoff2023vorasidenibinidh1 pages 1-3)

Safety: grade ≥3 alanine aminotransferase elevation occurred in ~**9.6–10%** of vorasidenib patients vs 0% placebo in trial reporting. (mellinghoff2023vorasidenibinidh1 pages 1-3, ruda2024idhinhibitionin pages 6-7)

ClinicalTrials.gov identifier: **NCT04164901**. (mellinghoff2023vorasidenibinidh1 pages 1-3)

### 12.4 Supportive care
Guidelines highlight dexamethasone for edema (preferred dose range **4–16 mg/day**) and seizure management with levetiracetam as first-line monotherapy for patients with seizures. (segura2023seomgeinoclinicalguidelines pages 7-8)

| Intervention | Indication/subtype | Evidence type | Key efficacy outcomes | Key safety/QoL points | Source with URL and year | MAXO term suggestion |
|---|---|---|---|---|---|---|
| Stupp regimen (maximal safe resection + radiotherapy + concomitant/adjuvant temozolomide) | Newly diagnosed glioblastoma / adult high-grade glioma | Guideline + real-world registry | Standard of care; guideline cites median OS ~15 months and 5-year survival 5-10% for GBM; in Austrian real-world cohort, median OS 11.6 months overall, 16.1 months in patients ≤65 years receiving postoperative standard-of-care therapy (segura2023seomgeinoclinicalguidelines pages 1-2, segura2023seomgeinoclinicalguidelines pages 4-5, hainfellner2024glioblastomainthe pages 1-3) | Extent of resection is prognostic; symptoms affecting QoL include seizures, cognitive deficits, headache, aphasia, motor deficits, fatigue; postoperative therapy started at median 31 days in Austrian practice (segura2023seomgeinoclinicalguidelines pages 2-4, hainfellner2024glioblastomainthe pages 1-3) | SEOM-GEINO guideline 2023: https://doi.org/10.1007/s12094-023-03245-y; Austrian registry 2024: https://doi.org/10.1007/s11060-024-04808-x (segura2023seomgeinoclinicalguidelines pages 2-4, hainfellner2024glioblastomainthe pages 1-3, segura2023seomgeinoclinicalguidelines pages 4-5) | MAXO: surgical resection; radiotherapy; temozolomide treatment; combined chemoradiotherapy |
| Tumor Treating Fields (TTFields) + standard of care / maintenance temozolomide | Newly diagnosed glioblastoma after chemoradiation; considered when available | Systematic review/meta-analysis + post-marketing surveillance + post-approval real-world study | Meta-analysis: OS HR 0.63 (95% CI 0.53-0.75) vs SOC alone; pooled median OS 22.6 vs 17.4 months; 2-year OS 46.8% vs 32.3%; higher adherence (≥75%) associated with longer survival (ballo2023associationoftumor pages 1-2, ballo2023associationoftumor pages 5-6) | Most common treatment-related AEs: beneath-array skin reactions 43%, tingling 14%, warmth 12%; no TTFields-related systemic AEs in >25,000-patient surveillance; Japanese post-approval study found local skin reactions in 60%, mostly mild-moderate (mrugala2024globalpost‑marketingsafety pages 1-2, nishikawa2023safetyandefficacy pages 1-2) | Meta-analysis 2023: https://doi.org/10.1007/s11060-023-04348-w; global surveillance 2024: https://doi.org/10.1007/s11060-024-04682-7; Japanese post-approval 2023: https://doi.org/10.1093/jjco/hyad001 (mrugala2024globalpost‑marketingsafety pages 1-2, ballo2023associationoftumor pages 1-2, nishikawa2023safetyandefficacy pages 1-2, ballo2023associationoftumor pages 5-6) | MAXO: tumor treating fields therapy; adjuvant device-based therapy |
| Vorasidenib | Residual or recurrent grade 2 IDH1/2-mutant astrocytoma or oligodendroglioma after surgery only | Phase 3 randomized trial (INDIGO) + approval summary | INDIGO: median imaging-based PFS 27.7 vs 11.1 months; HR for progression/death 0.39; time to next intervention HR 0.26; 18-month freedom from next intervention 85.6% vs 47.4% (mellinghoff2023vorasidenibinidh1 pages 1-3, lamb2024vorasidenibfirstapproval pages 4-5) | Grade ≥3 AEs more frequent with vorasidenib; grade ≥3 ALT elevation 9.6-10%; common AEs include elevated liver enzymes, fatigue, headache, diarrhea, nausea, dizziness; HRQoL reportedly maintained over ~13 months (mellinghoff2023vorasidenibinidh1 pages 1-3, lamb2024vorasidenibfirstapproval pages 4-5, ruda2024idhinhibitionin pages 6-7) | NEJM 2023: https://doi.org/10.1056/NEJMoa2304194; approval review 2024: https://doi.org/10.1007/s40265-024-02097-2 (mellinghoff2023vorasidenibinidh1 pages 1-3, lamb2024vorasidenibfirstapproval pages 4-5, ruda2024idhinhibitionin pages 6-7) | MAXO: IDH inhibitor therapy; targeted small-molecule therapy |
| Supportive care: dexamethasone | Symptomatic brain edema/increased intracranial pressure in high-grade glioma | Guideline/expert consensus | Improves mass-effect/edema-related symptoms; integral adjunct to oncologic therapy rather than disease-modifying treatment (segura2023seomgeinoclinicalguidelines pages 7-8) | Preferred dose range 4-16 mg/day; used to relieve edema-related neurologic symptoms and maintain function/QoL (segura2023seomgeinoclinicalguidelines pages 7-8) | SEOM-GEINO guideline 2023: https://doi.org/10.1007/s12094-023-03245-y (segura2023seomgeinoclinicalguidelines pages 7-8) | MAXO: corticosteroid therapy; cerebral edema management |
| Supportive care: levetiracetam | Seizure management in glioma/high-grade glioma | Guideline/expert consensus | Recommended as first-line antiepileptic monotherapy for patients with seizures; prophylactic AED use is not generally recommended (segura2023seomgeinoclinicalguidelines pages 7-8) | Supports seizure control and QoL; neurocognitive impairment is common and AED-related cognitive effects may require dose adjustment or agent substitution (segura2023seomgeinoclinicalguidelines pages 7-8, segura2023seomgeinoclinicalguidelines pages 8-9) | SEOM-GEINO guideline 2023: https://doi.org/10.1007/s12094-023-03245-y (segura2023seomgeinoclinicalguidelines pages 7-8, segura2023seomgeinoclinicalguidelines pages 8-9) | MAXO: anticonvulsant treatment; seizure management |


*Table: This table summarizes current glioma treatments and real-world implementation evidence, including standard chemoradiotherapy, TTFields, vorasidenib, and supportive care. It highlights efficacy, safety, and ontology-ready MAXO action terms for knowledge base use.*

## 13. Prevention
No population screening or primary prevention strategies were retrieved with tool evidence in this run. Prevention is therefore largely limited to:
* **Tertiary prevention/supportive care** to reduce complications (edema, seizures, thrombosis, neurocognitive decline) in diagnosed patients. (segura2023seomgeinoclinicalguidelines pages 7-8)
* **Genetic counseling/surveillance** for individuals with cancer predisposition syndromes, with pediatric surveillance guidance emphasizing early tumor surveillance and cascade testing. (hansford2024updateoncancer pages 1-2)

## 14. Other species / natural disease
Naturally occurring canine gliomas are used in comparative oncology. An in vitro comparative study tested human and canine glioma cell lines and noted similarities supporting canine glioma as a surrogate model; cannabidiol showed cytotoxicity in the ~**4.9–8.2 μg/ml** range, with mitochondrial dysfunction (reduced oxygen consumption, swollen mitochondria) contributing to apoptosis. (gross2021cannabidiolinducesapoptosis pages 1-2)

## 15. Model organisms
This run retrieved limited explicit model-organism methodology evidence beyond the comparative canine in vitro model above; thus, additional statements about specific GEMMs/PDX/organoid resources are not asserted.

## Expert opinions / authoritative analyses (selected)
* WHO CNS5 expert summaries emphasize that molecular diagnostics are central to classification while histology and immunohistochemistry remain essential, and that integrated diagnoses and layered reporting improve reproducibility and clinical relevance. (reuss2023updatesonthe pages 1-2, osborn2022the2021world pages 1-3)
* Molecular neuropathology reviews in 2024 frame DNA methylation profiling and DNA/RNA NGS as an “essential and evolving toolbox” for diagnosis and management, enabling tumor subgrouping and supporting targeted therapy selection. (bertero2024molecularneuropathologyan pages 1-3)

## Visual evidence note
Attempts were made to retrieve a WHO CNS5 classification figure/table and a CBTRUS survival table using the image retrieval tool, but the tool failed to fetch images from available text chunks in this run; therefore, no figure/table image citations are provided.



References

1. (osborn2022the2021world pages 1-3): A.G. Osborn, D.N. Louis, T.Y. Poussaint, L.L. Linscott, and K.L. Salzman. The 2021 world health organization classification of tumors of the central nervous system: what neuroradiologists need to know. American Journal of Neuroradiology, 45:S15-S24, Jun 2022. URL: https://doi.org/10.3174/ajnr.45-12.s15, doi:10.3174/ajnr.45-12.s15. This article has 265 citations and is from a peer-reviewed journal.

2. (mcnamara20222021whoclassification pages 1-6): Cillian McNamara, Kshitij Mankad, Stefanie Thust, Luke Dixon, Clara Limback-Stanic, Felice D’Arco, Thomas S. Jacques, and Ulrike Löbel. 2021 who classification of tumours of the central nervous system: a review for the neuroradiologist. Neuroradiology, 64:1919-1950, Jul 2022. URL: https://doi.org/10.1007/s00234-022-03008-6, doi:10.1007/s00234-022-03008-6. This article has 123 citations and is from a peer-reviewed journal.

3. (reuss2023updatesonthe pages 1-2): David.E. Reuss. Updates on the who diagnosis of idh-mutant glioma. Journal of Neuro-Oncology, 162:461-469, Jan 2023. URL: https://doi.org/10.1007/s11060-023-04250-5, doi:10.1007/s11060-023-04250-5. This article has 80 citations and is from a peer-reviewed journal.

4. (mcnamara20222021whoclassification pages 6-9): Cillian McNamara, Kshitij Mankad, Stefanie Thust, Luke Dixon, Clara Limback-Stanic, Felice D’Arco, Thomas S. Jacques, and Ulrike Löbel. 2021 who classification of tumours of the central nervous system: a review for the neuroradiologist. Neuroradiology, 64:1919-1950, Jul 2022. URL: https://doi.org/10.1007/s00234-022-03008-6, doi:10.1007/s00234-022-03008-6. This article has 123 citations and is from a peer-reviewed journal.

5. (antonelli2022adulttypediffuse pages 1-2): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 80 citations.

6. (gue2024the2021world pages 19-21): Racine Gue and Dhairya A. Lakhani. The 2021 world health organization central nervous system tumor classification: the spectrum of diffuse gliomas. Biomedicines, 12:1349, Jun 2024. URL: https://doi.org/10.3390/biomedicines12061349, doi:10.3390/biomedicines12061349. This article has 21 citations.

7. (price2024cbtrusstatisticalreport pages 2-3): Mackenzie Price, Christine Ballard, Julia Benedetti, Corey Neff, Gino Cioffi, Kristin A Waite, Carol Kruchko, Jill S Barnholtz-Sloan, and Quinn T Ostrom. Cbtrus statistical report: primary brain and other central nervous system tumors diagnosed in the united states in 2017-2021. Neuro-oncology, 26 Supplement_6:vi1-vi85, Oct 2024. URL: https://doi.org/10.1093/neuonc/noae145, doi:10.1093/neuonc/noae145. This article has 587 citations and is from a domain leading peer-reviewed journal.

8. (hainfellner2024glioblastomainthe pages 1-3): Andreas Hainfellner, Martin Borkovec, Lukas Seebrecht, Magdalena Neuhauser, Thomas Roetzer-Pejrimovsky, Lisa Greutter, Birgit Surböck, Andrea Hager-Seifert, Doris Gorka-vom Hof, Tadeja Urbanic-Purkart, Martin Stultschnig, Clemens Cijan, Franz Würtz, Bernadette Calabek-Wohinz, Josef Pichler, Isolde Höllmüller, Annette Leibetseder, Serge Weis, Waltraud Kleindienst, Michael Seiberl, Lara Bieler, Constantin Hecker, Christoph Schwartz, Sarah Iglseder, Johanna Heugenhauser, Martha Nowosielski, Claudius Thomé, Patrizia Moser, Markus Hoffermann, Karin Loibnegger, Karin Dieckmann, Matthias Tomschik, Georg Widhalm, Karl Rössler, Christine Marosi, Adelheid Wöhrer, Johannes A. Hainfellner, and Stefan Oberndorfer. Glioblastoma in the real-world setting: patterns of care and outcome in the austrian population. Journal of Neuro-Oncology, 170:407-418, Aug 2024. URL: https://doi.org/10.1007/s11060-024-04808-x, doi:10.1007/s11060-024-04808-x. This article has 7 citations and is from a peer-reviewed journal.

9. (mcdonald2023prevalenceofpathogenic pages 1-2): Malcolm F McDonald, Lyndsey L Prather, Cassandra R Helfer, Ethan B Ludmir, Alfredo E Echeverria, Shlomit Yust-Katz, Akash J Patel, Benjamin Deneen, Ganesh Rao, Ali Jalali, Shweta U Dhar, Chris I Amos, and Jacob J Mandel. Prevalence of pathogenic germline variants in adult-type diffuse glioma. Neuro-oncology practice, 10 5:482-490, Jun 2023. URL: https://doi.org/10.1093/nop/npad033, doi:10.1093/nop/npad033. This article has 9 citations and is from a peer-reviewed journal.

10. (mcdonald2023prevalenceofpathogenic pages 5-7): Malcolm F McDonald, Lyndsey L Prather, Cassandra R Helfer, Ethan B Ludmir, Alfredo E Echeverria, Shlomit Yust-Katz, Akash J Patel, Benjamin Deneen, Ganesh Rao, Ali Jalali, Shweta U Dhar, Chris I Amos, and Jacob J Mandel. Prevalence of pathogenic germline variants in adult-type diffuse glioma. Neuro-oncology practice, 10 5:482-490, Jun 2023. URL: https://doi.org/10.1093/nop/npad033, doi:10.1093/nop/npad033. This article has 9 citations and is from a peer-reviewed journal.

11. (mcdonald2023prevalenceofpathogenic pages 2-3): Malcolm F McDonald, Lyndsey L Prather, Cassandra R Helfer, Ethan B Ludmir, Alfredo E Echeverria, Shlomit Yust-Katz, Akash J Patel, Benjamin Deneen, Ganesh Rao, Ali Jalali, Shweta U Dhar, Chris I Amos, and Jacob J Mandel. Prevalence of pathogenic germline variants in adult-type diffuse glioma. Neuro-oncology practice, 10 5:482-490, Jun 2023. URL: https://doi.org/10.1093/nop/npad033, doi:10.1093/nop/npad033. This article has 9 citations and is from a peer-reviewed journal.

12. (hansford2024updateoncancer pages 1-2): Jordan R. Hansford, Anirban Das, Rose B. McGee, Yoshiko Nakano, Jack Brzezinski, Sarah R. Scollon, Surya P. Rednam, Jaclyn Schienda, Orli Michaeli, Sun Young Kim, Mary-Louise C. Greer, Rosanna Weksberg, Douglas R. Stewart, William D. Foulkes, Uri Tabori, Kristian W. Pajtler, Stefan M. Pfister, Garrett M. Brodeur, and Junne Kamihara. Update on cancer predisposition syndromes and surveillance guidelines for childhood brain tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2342-2350, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-4033, doi:10.1158/1078-0432.ccr-23-4033. This article has 62 citations.

13. (segura2023seomgeinoclinicalguidelines pages 2-4): Pedro Pérez Segura, Noelia Vilariño Quintela, María Martínez García, Sonia del Barco Berrón, Regina Gironés Sarrió, Jesús García Gómez, Almudena García Castaño, Luis Miguel Navarro Martín, Oscar Gallego Rubio, and Estela Pineda Losada. Seom-geino clinical guidelines for high-grade gliomas of adulthood (2022). Clinical & Translational Oncology, 25:2634-2646, Aug 2023. URL: https://doi.org/10.1007/s12094-023-03245-y, doi:10.1007/s12094-023-03245-y. This article has 46 citations and is from a peer-reviewed journal.

14. (segura2023seomgeinoclinicalguidelines pages 7-8): Pedro Pérez Segura, Noelia Vilariño Quintela, María Martínez García, Sonia del Barco Berrón, Regina Gironés Sarrió, Jesús García Gómez, Almudena García Castaño, Luis Miguel Navarro Martín, Oscar Gallego Rubio, and Estela Pineda Losada. Seom-geino clinical guidelines for high-grade gliomas of adulthood (2022). Clinical & Translational Oncology, 25:2634-2646, Aug 2023. URL: https://doi.org/10.1007/s12094-023-03245-y, doi:10.1007/s12094-023-03245-y. This article has 46 citations and is from a peer-reviewed journal.

15. (segura2023seomgeinoclinicalguidelines pages 8-9): Pedro Pérez Segura, Noelia Vilariño Quintela, María Martínez García, Sonia del Barco Berrón, Regina Gironés Sarrió, Jesús García Gómez, Almudena García Castaño, Luis Miguel Navarro Martín, Oscar Gallego Rubio, and Estela Pineda Losada. Seom-geino clinical guidelines for high-grade gliomas of adulthood (2022). Clinical & Translational Oncology, 25:2634-2646, Aug 2023. URL: https://doi.org/10.1007/s12094-023-03245-y, doi:10.1007/s12094-023-03245-y. This article has 46 citations and is from a peer-reviewed journal.

16. (bertero2024molecularneuropathologyan pages 3-4): Luca Bertero, Luca Mangherini, Alessia Andrea Ricci, Paola Cassoni, and Felix Sahm. Molecular neuropathology: an essential and evolving toolbox for the diagnosis and clinical management of central nervous system tumors. Virchows Archiv, 484:181-194, Sep 2024. URL: https://doi.org/10.1007/s00428-023-03632-4, doi:10.1007/s00428-023-03632-4. This article has 25 citations and is from a peer-reviewed journal.

17. (hardin2023loggiccorebioclinical pages 1-2): Emily C Hardin, Simone Schmid, Alexander Sommerkamp, Carina Bodden, Anna-Elisa Heipertz, Philipp Sievers, Andrea Wittmann, Till Milde, Stefan M Pfister, Andreas von Deimling, Svea Horn, Nina A Herz, Michèle Simon, Ashwyn A Perera, Amedeo Azizi, Ofelia Cruz, Sarah Curry, An Van Damme, Miklos Garami, Darren Hargrave, Antonis Kattamis, Barbara Faganel Kotnik, Päivi Lähteenmäki, Katrin Scheinemann, Antoinette Y N Schouten-van Meeteren, Astrid Sehested, Elisabetta Viscardi, Ole Mikal Wormdal, Michal Zapotocky, David S Ziegler, Arend Koch, Pablo Hernáiz Driever, Olaf Witt, David Capper, Felix Sahm, David T W Jones, and Cornelis M van Tilburg. Loggic core bioclinical data bank: added clinical value of rna-seq in an international molecular diagnostic registry for pediatric low-grade glioma patients. Neuro-oncology, 25:2087-2097, Apr 2023. URL: https://doi.org/10.1093/neuonc/noad078, doi:10.1093/neuonc/noad078. This article has 33 citations and is from a domain leading peer-reviewed journal.

18. (hardin2023loggiccorebioclinical pages 3-5): Emily C Hardin, Simone Schmid, Alexander Sommerkamp, Carina Bodden, Anna-Elisa Heipertz, Philipp Sievers, Andrea Wittmann, Till Milde, Stefan M Pfister, Andreas von Deimling, Svea Horn, Nina A Herz, Michèle Simon, Ashwyn A Perera, Amedeo Azizi, Ofelia Cruz, Sarah Curry, An Van Damme, Miklos Garami, Darren Hargrave, Antonis Kattamis, Barbara Faganel Kotnik, Päivi Lähteenmäki, Katrin Scheinemann, Antoinette Y N Schouten-van Meeteren, Astrid Sehested, Elisabetta Viscardi, Ole Mikal Wormdal, Michal Zapotocky, David S Ziegler, Arend Koch, Pablo Hernáiz Driever, Olaf Witt, David Capper, Felix Sahm, David T W Jones, and Cornelis M van Tilburg. Loggic core bioclinical data bank: added clinical value of rna-seq in an international molecular diagnostic registry for pediatric low-grade glioma patients. Neuro-oncology, 25:2087-2097, Apr 2023. URL: https://doi.org/10.1093/neuonc/noad078, doi:10.1093/neuonc/noad078. This article has 33 citations and is from a domain leading peer-reviewed journal.

19. (zhao2024emergingtrendsin pages 11-14): Yuxin Zhao, Zihan Xu, Yong Zhang, Ying Liu, Ming Ye, Rui Chen, Zhongyu Cao, Hong Zhou, and Yang Zhou. Emerging trends in glioma incidence and prognostic factors: a comprehensive analysis of the united states (2000-2018). Unknown journal, Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3913327/v1, doi:10.21203/rs.3.rs-3913327/v1.

20. (pinson2024epidemiologyandsurvival pages 1-2): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 28 citations and is from a domain leading peer-reviewed journal.

21. (pinson2024epidemiologyandsurvival pages 3-4): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 28 citations and is from a domain leading peer-reviewed journal.

22. (pinson2024epidemiologyandsurvival pages 4-6): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 28 citations and is from a domain leading peer-reviewed journal.

23. (bertero2024molecularneuropathologyan pages 1-3): Luca Bertero, Luca Mangherini, Alessia Andrea Ricci, Paola Cassoni, and Felix Sahm. Molecular neuropathology: an essential and evolving toolbox for the diagnosis and clinical management of central nervous system tumors. Virchows Archiv, 484:181-194, Sep 2024. URL: https://doi.org/10.1007/s00428-023-03632-4, doi:10.1007/s00428-023-03632-4. This article has 25 citations and is from a peer-reviewed journal.

24. (seyhan2024circulatingliquidbiopsy pages 48-49): Attila A. Seyhan. Circulating liquid biopsy biomarkers in glioblastoma: advances and challenges. International Journal of Molecular Sciences, 25:7974, Jul 2024. URL: https://doi.org/10.3390/ijms25147974, doi:10.3390/ijms25147974. This article has 76 citations.

25. (seyhan2024circulatingliquidbiopsy pages 1-2): Attila A. Seyhan. Circulating liquid biopsy biomarkers in glioblastoma: advances and challenges. International Journal of Molecular Sciences, 25:7974, Jul 2024. URL: https://doi.org/10.3390/ijms25147974, doi:10.3390/ijms25147974. This article has 76 citations.

26. (otsuji2024liquidbiopsyfor pages 12-14): Ryosuke Otsuji, Yutaka Fujioka, Nobuhiro Hata, Daisuke Kuga, Ryusuke Hatae, Yuhei Sangatsuda, Akira Nakamizo, Masahiro Mizoguchi, and Koji Yoshimoto. Liquid biopsy for glioma using cell-free dna in cerebrospinal fluid. Cancers, 16:1009, Feb 2024. URL: https://doi.org/10.3390/cancers16051009, doi:10.3390/cancers16051009. This article has 36 citations.

27. (komori2023updateofthe pages 1-2): Takashi Komori. Update of the 2021 who classification of tumors of the central nervous system: adult diffuse gliomas. Brain Tumor Pathology, 40:1-3, Dec 2023. URL: https://doi.org/10.1007/s10014-022-00446-1, doi:10.1007/s10014-022-00446-1. This article has 13 citations and is from a peer-reviewed journal.

28. (seyhan2024circulatingliquidbiopsy pages 49-51): Attila A. Seyhan. Circulating liquid biopsy biomarkers in glioblastoma: advances and challenges. International Journal of Molecular Sciences, 25:7974, Jul 2024. URL: https://doi.org/10.3390/ijms25147974, doi:10.3390/ijms25147974. This article has 76 citations.

29. (segura2023seomgeinoclinicalguidelines pages 1-2): Pedro Pérez Segura, Noelia Vilariño Quintela, María Martínez García, Sonia del Barco Berrón, Regina Gironés Sarrió, Jesús García Gómez, Almudena García Castaño, Luis Miguel Navarro Martín, Oscar Gallego Rubio, and Estela Pineda Losada. Seom-geino clinical guidelines for high-grade gliomas of adulthood (2022). Clinical & Translational Oncology, 25:2634-2646, Aug 2023. URL: https://doi.org/10.1007/s12094-023-03245-y, doi:10.1007/s12094-023-03245-y. This article has 46 citations and is from a peer-reviewed journal.

30. (segura2023seomgeinoclinicalguidelines pages 4-5): Pedro Pérez Segura, Noelia Vilariño Quintela, María Martínez García, Sonia del Barco Berrón, Regina Gironés Sarrió, Jesús García Gómez, Almudena García Castaño, Luis Miguel Navarro Martín, Oscar Gallego Rubio, and Estela Pineda Losada. Seom-geino clinical guidelines for high-grade gliomas of adulthood (2022). Clinical & Translational Oncology, 25:2634-2646, Aug 2023. URL: https://doi.org/10.1007/s12094-023-03245-y, doi:10.1007/s12094-023-03245-y. This article has 46 citations and is from a peer-reviewed journal.

31. (ballo2023associationoftumor pages 1-2): Matthew T. Ballo, Patrick Conlon, Gitit Lavy-Shahaf, Adrian Kinzel, Josef Vymazal, and Aaron M. Rulseh. Association of tumor treating fields (ttfields) therapy with survival in newly diagnosed glioblastoma: a systematic review and meta-analysis. Journal of Neuro-Oncology, 164:1-9, Jul 2023. URL: https://doi.org/10.1007/s11060-023-04348-w, doi:10.1007/s11060-023-04348-w. This article has 94 citations and is from a peer-reviewed journal.

32. (mrugala2024globalpost‑marketingsafety pages 1-2): Maciej M. Mrugala, Wenyin Shi, Fabio Iwomoto, Rimas V. Lukas, Joshua D. Palmer, John H. Suh, and Martin Glas. Global post‑marketing safety surveillance of tumor treating fields (ttfields) therapy in over 25,000 patients with cns malignancies treated between 2011–2022. Journal of Neuro-Oncology, 169:25-38, Jun 2024. URL: https://doi.org/10.1007/s11060-024-04682-7, doi:10.1007/s11060-024-04682-7. This article has 25 citations and is from a peer-reviewed journal.

33. (mellinghoff2023vorasidenibinidh1 pages 1-3): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 884 citations and is from a highest quality peer-reviewed journal.

34. (ruda2024idhinhibitionin pages 6-7): Roberta Rudà, Craig Horbinski, Martin van den Bent, Matthias Preusser, and Riccardo Soffietti. Idh inhibition in gliomas: from preclinical models to clinical trials. Nature Reviews Neurology, 20:395-407, May 2024. URL: https://doi.org/10.1038/s41582-024-00967-7, doi:10.1038/s41582-024-00967-7. This article has 100 citations and is from a highest quality peer-reviewed journal.

35. (ballo2023associationoftumor pages 5-6): Matthew T. Ballo, Patrick Conlon, Gitit Lavy-Shahaf, Adrian Kinzel, Josef Vymazal, and Aaron M. Rulseh. Association of tumor treating fields (ttfields) therapy with survival in newly diagnosed glioblastoma: a systematic review and meta-analysis. Journal of Neuro-Oncology, 164:1-9, Jul 2023. URL: https://doi.org/10.1007/s11060-023-04348-w, doi:10.1007/s11060-023-04348-w. This article has 94 citations and is from a peer-reviewed journal.

36. (nishikawa2023safetyandefficacy pages 1-2): Ryo Nishikawa, Fumiyuki Yamasaki, Yoshiki Arakawa, Yoshihiro Muragaki, Yoshitaka Narita, Shota Tanaka, Shigeru Yamaguchi, Akitake Mukasa, and Masayuki Kanamori. Safety and efficacy of tumour-treating fields (ttfields) therapy for newly diagnosed glioblastoma in japanese patients using the novo-ttf system: a prospective post-approval study. Japanese Journal of Clinical Oncology, 53:371-377, Jan 2023. URL: https://doi.org/10.1093/jjco/hyad001, doi:10.1093/jjco/hyad001. This article has 26 citations and is from a peer-reviewed journal.

37. (lamb2024vorasidenibfirstapproval pages 4-5): Yvette N. Lamb. Vorasidenib: first approval. Drugs, 84:1325-1331, Oct 2024. URL: https://doi.org/10.1007/s40265-024-02097-2, doi:10.1007/s40265-024-02097-2. This article has 42 citations and is from a domain leading peer-reviewed journal.

38. (gross2021cannabidiolinducesapoptosis pages 1-2): Chase Gross, Dominique A. Ramirez, Stephanie McGrath, and Daniel L. Gustafson. Cannabidiol induces apoptosis and perturbs mitochondrial function in human and canine glioma cells. Frontiers in Pharmacology, Aug 2021. URL: https://doi.org/10.3389/fphar.2021.725136, doi:10.3389/fphar.2021.725136. This article has 73 citations.

## Artifacts

- [Edison artifact artifact-00](Glioma-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Glioma-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Glioma-deep-research-falcon_artifacts/artifact-02.md)
- [Edison artifact artifact-03](Glioma-deep-research-falcon_artifacts/artifact-03.md)