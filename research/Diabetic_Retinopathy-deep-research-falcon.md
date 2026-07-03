---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-16T15:45:24.567902'
end_time: '2026-06-16T16:07:27.177045'
duration_seconds: 1322.61
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: Diabetic Retinopathy
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
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: Diabetic_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: Diabetic_Retinopathy-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: "## Context ID: pqac-00000028 In the provided document (Section 12\
    \ of the ADA Standards of Care in Diabetes\u20142025), there is no specific figure\
    \ or table summarizi"
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diabetic Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Diabetic Retinopathy** covering all of the
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
- **Disease Name:** Diabetic Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Diabetic Retinopathy** covering all of the
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


## Comprehensive Disease Characteristics Report: Diabetic Retinopathy (DR)

### Executive summary (current understanding; 2023–2025 emphasis)
Diabetic retinopathy (DR) is a progressive, diabetes-related neurovascular/microvascular retinal disease that can be asymptomatic until advanced stages, and it remains a major cause of visual impairment and blindness. Contemporary management is built on systematic screening (increasingly via teleophthalmology and AI), risk-factor control (glycemia, blood pressure, lipids, kidney disease), and stage-specific ocular therapies (anti-VEGF for center-involving diabetic macular edema [DME] and/or selected DR indications; panretinal photocoagulation for high-risk proliferative DR [PDR]). Key mechanistic themes in recent literature emphasize oxidative stress/inflammation, blood–retinal barrier (BRB) breakdown, VEGF signaling, and the ANGPT2–Tie2 axis as important contributors and therapeutic targets. (srejovic2024molecularandcellular pages 1-3, wong2018guidelinesondiabetic pages 2-3, elsayed202512.retinopathyneuropathy pages 1-1)

| Domain | Key finding | Source (first author year) | Publication date (month/year) | Identifier (PMID if available in text; else DOI) | URL |
|---|---|---|---|---|---|
| Definition/Classification | DR is described as a “highly specific neurovascular complication” of both type 1 and type 2 diabetes; prevalence relates strongly to diabetes duration and glycemic control. (elsayed202512.retinopathyneuropathy pages 1-1) | ElSayed 2025 | 12/2025 | 10.2337/dc25-s012 | https://doi.org/10.2337/dc25-s012 |
| Definition/Classification | ICO defines DR as “the most common specific microvascular complication of DM,” progressing from NPDR to vision-threatening PDR and DME. (wong2018guidelinesondiabetic pages 2-3, wong2018guidelinesondiabetic pages 1-2) | Wong 2018 | 05/2018 | 10.1016/j.ophtha.2018.04.007 | https://doi.org/10.1016/j.ophtha.2018.04.007 |
| Staging/Phenotypes | ICO DME classification: no DME; nonecenter-involving DME = retinal thickening in the macula not involving the central 1 mm subfield; center-involving DME = retinal thickening involving the central 1 mm subfield. (wong2018guidelinesondiabetic pages 2-3, wong2018guidelinesondiabetic pages 7-9) | Wong 2018 | 05/2018 | 10.1016/j.ophtha.2018.04.007 | https://doi.org/10.1016/j.ophtha.2018.04.007 |
| Staging/Phenotypes | Early DR is often asymptomatic; advanced DR/DME may be present even without visual symptoms. NPDR lacks neovascularization; PDR is the most advanced ischemia-driven stage. (wong2018guidelinesondiabetic pages 3-5, wong2018guidelinesondiabetic pages 2-3) | Wong 2018 | 05/2018 | 10.1016/j.ophtha.2018.04.007 | https://doi.org/10.1016/j.ophtha.2018.04.007 |
| Epidemiology/Burden | Global blindness due to DR increased 326.0% from 1990 to 2021; age-standardized prevalence rate rose from 7.59 to 15.28 per 100,000 population. (meng2025globalregionaland pages 1-2) | Meng 2025 | 08/2025 | 10.1007/s40123-025-01230-y | https://doi.org/10.1007/s40123-025-01230-y |
| Epidemiology/Burden | ICO summary estimate: ~1 in 3 people with diabetes has DR, and ~1 in 10 has PDR or DME. (wong2018guidelinesondiabetic pages 1-2) | Wong 2018 | 05/2018 | 10.1016/j.ophtha.2018.04.007 | https://doi.org/10.1016/j.ophtha.2018.04.007 |
| Epidemiology/Burden | Ethiopia systematic review/meta-analysis: pooled DR prevalence 24.35% (95% CI 18.88–29.83), summarized as “one in four” patients with diabetes affected. (wondmeneh2024prevalenceofdiabetic pages 1-2, wondmeneh2024prevalenceofdiabetic pages 12-15) | Wondmeneh 2024 | 11/2024 | 10.1038/s41598-024-78596-9 | https://doi.org/10.1038/s41598-024-78596-9 |
| Risk factors | Ethiopia meta-analysis identified diabetes duration ≥10 years (AOR 4.36), hypertension (AOR 2.54), poor glycemic control (AOR 3.83), and positive proteinuria (AHR 1.55) as DR risk factors. (wondmeneh2024prevalenceofdiabetic pages 1-2, wondmeneh2024prevalenceofdiabetic pages 12-15) | Wondmeneh 2024 | 11/2024 | 10.1038/s41598-024-78596-9 | https://doi.org/10.1038/s41598-024-78596-9 |
| Risk factors | ADA notes modifiable risk factors including chronic hyperglycemia, nephropathy, hypertension, and dyslipidemia; recommends achieving glycemic, blood pressure, and lipid targets to reduce risk/slow progression. (elsayed202512.retinopathyneuropathy pages 1-1) | ElSayed 2025 | 12/2025 | 10.2337/dc25-s012 | https://doi.org/10.2337/dc25-s012 |
| Screening/Diagnostics | ADA 2025: initial dilated comprehensive eye exam within 5 years after diagnosis for type 1 diabetes; at diagnosis for type 2 diabetes. Follow-up generally annual if none/mild retinopathy; every 1–2 years may be considered after normal exams and if glycemic indicators are at goal. (elsayed202512.retinopathyneuropathy pages 2-3, elsayed202512.retinopathyneuropathy pages 1-2, elsayed202512.retinopathyneuropathy media 6876c524) | ElSayed 2025 | 12/2025 | 10.2337/dc25-s012 | https://doi.org/10.2337/dc25-s012 |
| Screening/Diagnostics | ADA 2025 endorses validated retinal photography programs, remote reading, and FDA-approved AI platforms (AEYE-DS, EyeArt, LumineticsCore) where appropriate; abnormal/ungradable images require in-person eye examination. (elsayed202512.retinopathyneuropathy pages 2-3, elsayed202512.retinopathyneuropathy pages 1-2) | ElSayed 2025 | 12/2025 | 10.2337/dc25-s012 | https://doi.org/10.2337/dc25-s012 |
| Screening/Diagnostics | ICO high-resource follow-up intervals: no apparent DR or mild NPDR without DME re-exam in 1–2 years; moderate NPDR in 3–6 months; PDR in <1 month. Center-involving DME follow-up/treatment interval 1–3 months. (wong2018guidelinesondiabetic pages 7-9) | Wong 2018 | 05/2018 | 10.1016/j.ophtha.2018.04.007 | https://doi.org/10.1016/j.ophtha.2018.04.007 |
| Real-world implementation/AI screening | Smartphone-based handheld fundus camera for DR/DME screening: referable DR sensitivity 0.906, specificity 0.808; DR classification agreement 73.18% (weighted kappa 0.808); macular edema agreement 88.48% (kappa 0.809). (wong2018guidelinesondiabetic pages 1-2) | de Oliveira 2023 | 05/2023 | 10.1007/s00592-023-02105-z | https://doi.org/10.1007/s00592-023-02105-z |
| Real-world implementation/AI screening | Autonomous AI system for more-than-mild DR and vision-threatening DR achieved mtmDR sensitivity 96%/specificity 88% and vtDR sensitivity 97%/specificity 90%; >97% of eyes gradable without physician oversight in most cases. (wong2018guidelinesondiabetic pages 1-2) | Ipp 2021 | 11/2021 | 10.1001/jamanetworkopen.2021.34254 | https://doi.org/10.1001/jamanetworkopen.2021.34254 |
| Mechanisms/Pathways | Core pathogenic chain: hyperglycemia activates polyol, AGE, PKC, and hexosamine pathways → ROS/oxidative stress, mitochondrial dysfunction, endothelial/pericyte injury, BRB breakdown, ischemia, and neovascularization. (gomezjimenez2025modulationofoxidative pages 7-8, toma2026oxidativestressin pages 1-2, roy2025pathophysiologicalmechanismsof pages 23-24, srejovic2024molecularandcellular pages 3-4) | Gómez-Jiménez 2025; Toma 2026; Roy 2025 | 07/2025; 03/2026; 07/2025 | 10.3390/antiox14070875; 10.3390/antiox15040425; 10.3390/medsci13030087 | https://doi.org/10.3390/antiox14070875 |
| Mechanisms/Pathways | VEGF is a central driver of abnormal neovascularization; ANGPT2–Tie2 dysregulation contributes to pericyte loss, inflammation, and neovascularization. (srejovic2024molecularandcellular pages 1-3) | Srejovic 2024 | 11/2024 | 10.3390/ijms252111850 | https://doi.org/10.3390/ijms252111850 |
| Mechanisms/Pathways | Persistent inflammatory milieu includes TNF-α, IL-1β/IL-1, and IL-6; microglial activation and NF-κB/TLR signaling promote BRB breakdown and neovascularization. (srejovic2024molecularandcellular pages 1-3, srejovic2024molecularandcellular pages 3-4) | Srejovic 2024 | 11/2024 | 10.3390/ijms252111850 | https://doi.org/10.3390/ijms252111850 |
| Mechanisms/Pathways | Oxidative stress/NLRP3 axis: ROS is a major upstream driver; NLRP3 inflammasome is highlighted as a hotspot, and downstream IL-1β/IL-18 production with pyroptotic Müller cell death has been described. (gomezjimenez2025modulationofoxidative pages 7-8, du2024globalresearchtrends pages 1-2) | Gómez-Jiménez 2025; Du 2024 | 07/2025; 08/2024 | 10.3390/antiox14070875; 10.3389/fendo.2024.1428411 | https://doi.org/10.3390/antiox14070875 |
| Treatments | ADA 2025: promptly refer any DME, moderate-or-worse NPDR, or any PDR to an ophthalmologist experienced in DR management; panretinal laser photocoagulation indicated for high-risk PDR and some severe NPDR. (elsayed202512.retinopathyneuropathy pages 2-3) | ElSayed 2025 | 12/2025 | 10.2337/dc25-s012 | https://doi.org/10.2337/dc25-s012 |
| Treatments | For center-involved DME, anti-VEGF is more effective than laser monotherapy; commonly used agents include bevacizumab, ranibizumab, aflibercept (2 mg and 8 mg), brolucizumab, and faricimab. (elsayed202512.retinopathyneuropathy pages 3-4) | ElSayed 2025 | 12/2025 | 10.2337/dc25-s012 | https://doi.org/10.2337/dc25-s012 |
| Treatments | Pivotal anti-VEGF DME trial outcomes: ≥15 ETDRS-letter gain ranged 18.1%–44.8%; CMT reductions ranged 183.1–294 µm across studies. Ranibizumab RISE/RIDE: ~40–44% gained ≥15 letters vs 20% sham, with CMT reduction about −261 to −269 µm; aflibercept trials showed mean gains ~10.5–13.3 letters and CMT reductions ~−169 to −200 µm. (cheema2024diabeticmacularedema pages 5-7, aldokhail2024outcomesofantivegf pages 1-2, aldokhail2024outcomesofantivegf pages 4-5) | Cheema 2024; Aldokhail 2024 | 01/2024; 12/2024 | 10.7759/cureus.52676; 10.2147/OPTH.S489114 | https://doi.org/10.7759/cureus.52676 |
| Treatments | Long-term DME treatment burden: randomized trials reported mean BCVA gains of ~6–13 ETDRS letters with roughly 7–12 intravitreal injections; frequent injections/monitoring contribute to poorer real-world outcomes versus trials. (nakao2024antivegftherapyfor pages 1-2) | Nakao 2024 | 07/2024 | 10.1007/s00417-024-06558-y | https://doi.org/10.1007/s00417-024-06558-y |
| Treatments | Anti-VEGF vs panretinal photocoagulation meta-analysis in DR: anti-VEGF slightly better for BCVA up to 2 years (mean difference −0.089 logMAR, about 3.6 ETDRS letters), reduced macular edema (RR 0.29, 95% CI 0.18–0.49) and vitreous hemorrhage (RR 0.77, 95% CI 0.61–0.99); benefit judged small and possibly not clinically meaningful. (wong2018guidelinesondiabetic pages 1-2) | Simmonds 2024 | 12/2024 | 10.3310/pcgv5709 | https://doi.org/10.3310/pcgv5709 |


*Table: This table compiles high-yield, evidence-backed facts on diabetic retinopathy across definition, burden, risk factors, screening, mechanisms, treatment, and AI-enabled implementation. It is useful as a quick reference for populating a structured disease knowledge base with recent, cited findings.*

---

## 1. Disease Information

### 1.1 What is the disease?
The American Diabetes Association (ADA) Standards of Care describes DR as “a highly specific neurovascular complication of both type 1 and type 2 diabetes,” whose prevalence is strongly linked to diabetes duration and glycemic control. (elsayed202512.retinopathyneuropathy pages 1-1)

The International Council of Ophthalmology (ICO) guideline describes DR as “the most common specific microvascular complication of DM,” progressing from milder nonproliferative diabetic retinopathy (NPDR) to vision-threatening proliferative diabetic retinopathy (PDR) and diabetic macular edema (DME). (wong2018guidelinesondiabetic pages 2-3)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
Within the tool-accessible corpus retrieved for this report, explicit ontology identifiers (MONDO ID, MeSH ID, ICD-10/ICD-11 codes, OMIM, Orphanet) were not available as citable evidence; therefore, they cannot be verified here and should be populated from external ontology resources (e.g., MONDO, MeSH, ICD-10/ICD-11 browsers). (No in-corpus evidence)

### 1.3 Synonyms and alternative names
Common clinical terms in guidelines and recent literature include:
- Diabetic retinopathy (DR) (wong2018guidelinesondiabetic pages 2-3)
- Nonproliferative diabetic retinopathy (NPDR) (wong2018guidelinesondiabetic pages 2-3, elsayed202512.retinopathyneuropathy pages 2-3)
- Proliferative diabetic retinopathy (PDR) (wong2018guidelinesondiabetic pages 2-3, elsayed202512.retinopathyneuropathy pages 2-3)
- Diabetic macular edema (DME) (wong2018guidelinesondiabetic pages 2-3)
- Clinically significant macular edema (CSME; classic ETDRS term) (elsayed202512.retinopathyneuropathy pages 3-4)

### 1.4 Evidence source type
This report is derived from aggregated disease-level resources (international guidelines, systematic reviews, meta-analyses, epidemiologic studies, and clinical trial registry records) rather than individual-patient EHR-derived phenotypes. (wondmeneh2024prevalenceofdiabetic pages 12-15, wong2018guidelinesondiabetic pages 2-3, elsayed202512.retinopathyneuropathy pages 1-1, NCT02471651 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
The etiologic driver is chronic diabetes-associated metabolic dysregulation (particularly hyperglycemia) leading to neurovascular retinal injury through oxidative stress and inflammatory pathways. Mechanistic reviews synthesize the cascade: hyperglycemia activates metabolic pathways (e.g., AGE formation, PKC activation), promoting ROS generation and inflammatory signaling, damaging pericytes/endothelial cells and destabilizing the BRB, which contributes to macular edema, ischemia, and neovascularization. (gomezjimenez2025modulationofoxidative pages 7-8, srejovic2024molecularandcellular pages 1-3, srejovic2024molecularandcellular pages 3-4)

### 2.2 Risk factors (human epidemiology)
**ADA (risk-factor framing):** DR prevalence relates strongly to diabetes duration and glycemic control, with additional associated factors including chronic hyperglycemia, nephropathy, hypertension, and dyslipidemia. (elsayed202512.retinopathyneuropathy pages 1-1)

**Recent meta-analysis (Ethiopia, 2024):** pooled DR prevalence in adults with diabetes was 24.35% (95% CI: 18.88–29.83), with key risk factors:
- Diabetes duration ≥10 years: AOR 4.36
- Hypertension: AOR 2.54
- Poor glycemic control: AOR 3.83
- Positive proteinuria: AHR 1.55
(wondmeneh2024prevalenceofdiabetic pages 1-2, wondmeneh2024prevalenceofdiabetic pages 12-15)

### 2.3 Protective factors
Direct evidence for protective genetic variants or protective exposures was not captured in the retrieved corpus. The ADA/ICO guidelines emphasize risk reduction via achieving glycemic, blood pressure, and lipid targets, which functionally serve as protective measures against onset/progression. (wong2018guidelinesondiabetic pages 2-3, elsayed202512.retinopathyneuropathy pages 1-1)

### 2.4 Gene–environment interactions
Not explicitly quantified in the retrieved corpus. Mechanistic syntheses support an interaction model in which systemic metabolic exposures (hyperglycemia, dyslipidemia, hypertension) modulate inflammatory/oxidative pathways and vascular signaling (e.g., VEGF), which in turn shape disease expression. (gomezjimenez2025modulationofoxidative pages 7-8, srejovic2024molecularandcellular pages 1-3)

---

## 3. Phenotypes (clinical manifestations)

### 3.1 Core phenotypes and staging (ICO clinical taxonomy)
ICO describes DR microvascular lesions including “microaneurysms, intraretinal hemorrhages, venous beading…, intraretinal microvascular abnormalities, hard exudates…, and retinal neovascularization.” It also highlights that early DR is often asymptomatic and that advanced DR/DME can exist without visual symptoms. (wong2018guidelinesondiabetic pages 3-5)

**DR staging terms:**
- No apparent DR → mild/moderate/severe NPDR → PDR (wong2018guidelinesondiabetic pages 2-3)
- Key distinction: “Eyes with NPDR have not yet developed neovascularization.” (wong2018guidelinesondiabetic pages 3-5)

**DME phenotypes and subtypes:**
ICO DME classification is explicitly defined by central macular involvement:
- Nonecenter-involving DME: macular thickening not involving central 1 mm subfield
- Center-involving DME: thickening involving central 1 mm subfield
(wong2018guidelinesondiabetic pages 2-3)

**CSME definition (ETDRS term used in ADA 2025):** “retinal edema located at or threatening the macular center.” (elsayed202512.retinopathyneuropathy pages 3-4)

### 3.2 Suggested HPO terms (non-exhaustive; to be validated against HPO)
Because explicit HPO IDs are not provided in the retrieved sources, the following are suggested concept-level mappings:
- Decreased visual acuity; visual impairment (supported by burden statements and DME context) (elsayed202512.retinopathyneuropathy pages 3-4, elsayed202512.retinopathyneuropathy pages 1-1)
- Retinal hemorrhage / intraretinal hemorrhage; microaneurysm; retinal neovascularization (ICO lesion descriptions) (wong2018guidelinesondiabetic pages 3-5)
- Macular edema / retinal edema (DME/CSME definitions) (elsayed202512.retinopathyneuropathy pages 3-4, wong2018guidelinesondiabetic pages 2-3)

### 3.3 Quality of life impact
ADA notes population-level functional consequences: in the U.S., ~12% of adults with diabetes have some level of vision impairment, and diabetes increases risk of chronic vision loss and functional decline. (elsayed202512.retinopathyneuropathy pages 3-4)

---

## 4. Genetic / Molecular Information

### 4.1 Genetic architecture (current evidence availability)
The retrieved evidence set does not provide validated causal germline variants or a curated list of DR causal genes with OMIM IDs; DR is generally treated as a complex complication with multifactorial etiology in this corpus. (No in-corpus variant evidence)

### 4.2 Disease–target associations (Open Targets)
Open Targets identifies disease–target associations for “diabetic retinopathy,” including VEGFA and PGF (among others such as ANGPT2 and NR3C1), with evidence including clinical-stage associations and literature links. (OpenTargets Search: diabetic retinopathy)

**Interpretation:** These targets align with established therapeutic biology (anti-VEGF agents; emerging Ang-2/Tie2 biology), but Open Targets associations are not equivalent to confirmed causal germline genetics. (OpenTargets Search: diabetic retinopathy, srejovic2024molecularandcellular pages 1-3)

### 4.3 Epigenetics / metabolic memory
Mechanistic reviews describe persistent oxidative/inflammatory signaling and “metabolic memory” concepts, where prior hyperglycemic exposure can sustain downstream pathology even after improved glycemia. (gomezjimenez2025modulationofoxidative pages 7-8)

---

## 5. Environmental Information

### 5.1 Non-genetic contributing factors (lifestyle/clinical)
Key modifiable systemic exposures emphasized in guidelines and epidemiology include chronic hyperglycemia, hypertension, dyslipidemia, and nephropathy/proteinuria. (wondmeneh2024prevalenceofdiabetic pages 1-2, elsayed202512.retinopathyneuropathy pages 1-1)

### 5.2 Infectious agents
Not applicable based on retrieved evidence. (No in-corpus evidence)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (integrated model)
A coherent causal chain supported across mechanistic reviews is:
1) Diabetes-associated hyperglycemia and metabolic dysregulation
2) Activation of oxidative stress and inflammatory pathways (ROS generation; NF-κB signaling)
3) Retinal vascular dysfunction (pericyte/endothelial injury; tight junction disruption)
4) BRB breakdown → increased vascular permeability → macular edema (DME)
5) Capillary closure/ischemia → pro-angiogenic signaling (VEGF) → neovascularization (PDR)
(gomezjimenez2025modulationofoxidative pages 7-8, srejovic2024molecularandcellular pages 1-3, srejovic2024molecularandcellular pages 3-4)

### 6.2 Key pathways and molecular mediators
- **VEGF** is described as a central driver of abnormal neovascularization and a major therapeutic target in retinal vascular disease, including DR. (srejovic2024molecularandcellular pages 1-3)
- **ANGPT2–Tie2 axis:** “Interaction between angiopoietin 2 and the Tie2 receptor results in aberrant Tie2 signaling, resulting in loss of pericytes, neovascularization, and inflammation.” (srejovic2024molecularandcellular pages 1-3)
- **Inflammatory cytokines and microglia:** Increased TNF-α, IL-1β, and IL-6 and microglial activation contribute to a persistent inflammatory milieu promoting BRB breakdown and neovascularization. (srejovic2024molecularandcellular pages 1-3)
- **Oxidative stress/ROS:** Oxidative stress is repeatedly positioned as a central driver connecting metabolic dysregulation to retinal injury and neurovascular dysfunction; NLRP3 inflammasome and autophagy appear as research hotspots. (gomezjimenez2025modulationofoxidative pages 7-8, du2024globalresearchtrends pages 1-2)

### 6.3 Cell types and ontology suggestions
**Cell types (suggested CL concepts; IDs not available in corpus):**
- Retinal pericytes (pericyte loss emphasized) (srejovic2024molecularandcellular pages 1-3)
- Retinal vascular endothelial cells (vascular dysfunction; BRB breakdown) (srejovic2024molecularandcellular pages 1-3, srejovic2024molecularandcellular pages 3-4)
- Microglia (activation; inflammatory milieu) (srejovic2024molecularandcellular pages 1-3)
- Müller glia (implicated in inflammasome/pyroptosis pathways in mechanistic review synthesis) (gomezjimenez2025modulationofoxidative pages 7-8)

**GO biological process concepts (suggested):** angiogenesis, inflammatory response, response to oxidative stress, regulation of vascular permeability, cytokine-mediated signaling pathway. (gomezjimenez2025modulationofoxidative pages 7-8, srejovic2024molecularandcellular pages 1-3)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue localization
Primary affected structure is the retina, including the macula (DME) and retinal vasculature (NPDR/PDR). BRB components are explicitly discussed (inner BRB via retinal vascular endothelium; outer BRB via RPE in general retinal vascular disease frameworks). (srejovic2024molecularandcellular pages 1-3, wong2018guidelinesondiabetic pages 2-3)

**Suggested UBERON concepts (IDs not available in corpus):** retina; macula; retinal blood vessel; vitreous body (relevant to vitreous hemorrhage and tractional detachment risk in PDR context). (wong2018guidelinesondiabetic pages 3-5, simmonds2024antivegfdrugscompared pages 25-27)

### 7.2 Laterality
DR is typically bilateral (diabetes-related systemic exposure), but explicit laterality assertions were not provided in the retrieved corpus. (No in-corpus evidence)

---

## 8. Temporal Development

### 8.1 Onset pattern
ICO emphasizes that DR “develops over time” and that early disease may be asymptomatic, supporting an insidious onset. (wong2018guidelinesondiabetic pages 2-3, wong2018guidelinesondiabetic pages 3-5)

### 8.2 Progression
ICO explicitly frames progression from NPDR to PDR/DME and notes that PDR is an angiogenic response to extensive ischemia from capillary closure, consistent with stepwise worsening in untreated disease. (wong2018guidelinesondiabetic pages 2-3)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent statistics)
- **Global burden of blindness due to DR (1990–2021):** number of people blind due to DR increased 326.0%, and age-standardized prevalence rate rose from 7.59 to 15.28 per 100,000 population. (Meng et al., 2025; https://doi.org/10.1007/s40123-025-01230-y) (meng2025globalregionaland pages 1-2)
- **Ethiopia (systematic review/meta-analysis, 2024):** pooled DR prevalence 24.35% (95% CI: 18.88–29.83), summarized as “one in four” people with diabetes. (Wondmeneh & Mohammed, 2024; https://doi.org/10.1038/s41598-024-78596-9) (wondmeneh2024prevalenceofdiabetic pages 1-2, wondmeneh2024prevalenceofdiabetic pages 12-15)
- **ICO contextual estimate (global):** “approximately 1 in 3 persons with DM has DR, and 1 in 10 has PDR or DME.” (Wong et al., 2018; https://doi.org/10.1016/j.ophtha.2018.04.007) (wong2018guidelinesondiabetic pages 1-2)

### 9.2 Inheritance pattern
Not applicable as a monogenic inheritance pattern in this evidence set; DR is treated as a complex complication. (No in-corpus evidence)

---

## 10. Diagnostics

### 10.1 Screening and diagnostic modalities (guideline-based)
**ADA Standards of Care (2025):**
- Initial eye exam timing:
  - Type 1 diabetes: “within 5 years after the diagnosis of diabetes” (dilated, comprehensive). (elsayed202512.retinopathyneuropathy pages 2-3)
  - Type 2 diabetes: “at the time of diagnosis.” (elsayed202512.retinopathyneuropathy pages 2-3)
- Follow-up:
  - Generally annual for none/mild retinopathy; “screening every 1–2 years may be considered” in selected low-risk scenarios after normal exams and if glycemic indicators are at goal. (elsayed202512.retinopathyneuropathy pages 1-2)
- Implementation: validated retinal photography programs with trained readers; FDA-approved autonomous AI systems may be used where appropriate (e.g., EyeArt, LumineticsCore, AEYE-DS), but abnormal/ungradable images require in-person eye examination. (elsayed202512.retinopathyneuropathy pages 1-2)

**Image evidence:** the ADA recommendations box summarizing these screening statements is available as a cropped guideline image. (elsayed202512.retinopathyneuropathy media 6876c524)

**ICO (resource-stratified) follow-up intervals (high-resource example):**
- No apparent DR or mild NPDR (no DME): re-examination in 1–2 years
- Moderate NPDR: 3–6 months
- PDR: <1 month
and DME classification into center-involving vs nonecenter-involving by clinical findings and OCT (if available). (wong2018guidelinesondiabetic pages 7-9, wong2018guidelinesondiabetic pages 2-3)

### 10.2 Differential diagnosis
Not extracted from the retrieved corpus. (No in-corpus evidence)

### 10.3 Omics-based diagnostics
Not supported by direct evidence in the retrieved corpus (though mechanistic reviews discuss biomarkers conceptually). (toma2026oxidativestressin pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Vision loss and blindness
- ADA states DR is “the most frequent cause of new cases of blindness among adults aged 20–74 years in developed countries.” (elsayed202512.retinopathyneuropathy pages 1-1)
- Global DR-related blindness burden has increased substantially over recent decades (1990–2021). (meng2025globalregionaland pages 1-2)

### 11.2 Prognostic factors
Systemic risk-factor control (glycemia, blood pressure, lipids) is positioned as central to slowing progression, and more frequent ophthalmologic follow-up is required when retinopathy is progressing or in the presence of DME/advanced disease. (elsayed202512.retinopathyneuropathy pages 2-3, elsayed202512.retinopathyneuropathy pages 1-1)

---

## 12. Treatment

### 12.1 Standard-of-care ocular treatments
- **Anti-VEGF therapy** is a cornerstone for DME, particularly center-involving DME, and is supported as more effective than laser monotherapy for center-involved DME in ADA discussion. (elsayed202512.retinopathyneuropathy pages 3-4)
- **Panretinal photocoagulation (PRP)** remains indicated for high-risk PDR (and selected severe NPDR) to reduce risk of vision loss. (elsayed202512.retinopathyneuropathy pages 2-3)

### 12.2 Quantitative treatment outcomes (recent syntheses)
**Anti-VEGF in DME (systematic review, 2024):** proportion gaining ≥15 ETDRS letters ranged 18.1%–44.8%, with central macular thickness reductions commonly in the range of 183.1–294 µm (across DME/RVO cohorts). (Aldokhail et al., 2024; https://doi.org/10.2147/OPTH.S489114) (aldokhail2024outcomesofantivegf pages 1-2)

**Trial-based outcomes summarized in 2024 review:** ranibizumab RISE/RIDE reported 40–44% gaining ≥15 ETDRS letters vs 20% with sham at 3 years, with CMT reductions about −261 to −269 μm. (Cheema & Cheema, 2024; https://doi.org/10.7759/cureus.52676) (cheema2024diabeticmacularedema pages 5-7)

**Real-world implementation challenge:** a 2024 review emphasizes that trial vision gains depend on frequent injections/monitoring and that real-world outcomes are often poorer because maintaining frequent injection schedules is difficult. (Nakao et al., 2024; https://doi.org/10.1007/s00417-024-06558-y) (nakao2024antivegftherapyfor pages 1-2)

**Anti-VEGF vs PRP in DR (Health Technology Assessment, 2024):** network meta-analysis across 14 RCTs found anti-VEGF “slightly better” than PRP for BCVA up to 2 years (mean difference −0.089 logMAR ≈ 3.6 ETDRS letters) and reduced macular edema (RR 0.29; 95% CI 0.18–0.49) and vitreous hemorrhage (RR 0.77; 95% CI 0.61–0.99); authors concluded the BCVA benefit is small and may not be clinically meaningful. (Simmonds et al., 2024; https://doi.org/10.3310/pcgv5709) (wong2018guidelinesondiabetic pages 1-2)

### 12.3 Systemic therapies and risk-factor modification
ICO and ADA emphasize maintenance of glycemic control and management of hypertension and dyslipidemia as core strategies to reduce risk and slow progression. (wong2018guidelinesondiabetic pages 2-3, elsayed202512.retinopathyneuropathy pages 1-1)

### 12.4 Examples of recent/ongoing/illustrative clinical trials (ClinicalTrials.gov)
- **NCT06662994 (2025; Phase 4; Recruiting):** high-dose aflibercept 8 mg in central-involving DME after prior vitrectomy, using a treat–extend–stop protocol; outcomes include visual acuity and OCT thickness over 12 months. (https://clinicaltrials.gov/study/NCT06662994) (NCT06662994 chunk 2, NCT06662994 chunk 1)
- **NCT02471651 (2015; Phase 4; Completed):** dexamethasone intravitreal implant (Ozurdex 0.7 mg) vs continued monthly anti-VEGF for persistent DME after prior anti-VEGF; primary endpoint central 1 mm subfield thickness change. (https://clinicaltrials.gov/study/NCT02471651) (NCT02471651 chunk 1)
- **NCT07144865 (2024; Completed; phase not specified in excerpt):** evaluates biological changes in fibrovascular membranes in PDR following faricimab injection (relevant to dual-pathway anti-VEGF/Ang-2 strategies). (https://clinicaltrials.gov/study/NCT07144865) (NCT07144865 chunk 2)

### 12.5 MAXO suggestions (concept-level; IDs not available in corpus)
- Intravitreal injection of anti-VEGF agent (elsayed202512.retinopathyneuropathy pages 3-4)
- Panretinal photocoagulation (elsayed202512.retinopathyneuropathy pages 2-3)
- Focal/grid laser photocoagulation (macular edema context) (elsayed202512.retinopathyneuropathy pages 3-4)
- Vitrectomy (vision-threatening complications context in ICO) (wong2018guidelinesondiabetic pages 1-2)

---

## 13. Prevention

**Primary/secondary prevention framing:** DR is preventable and progression-reducible through systemic risk-factor control and systematic screening programs.
- ICO explicitly states that “Vision loss from DR can be prevented with broad-level public health strategies,” and both ICO and ADA emphasize glycemic and cardiovascular risk control. (wong2018guidelinesondiabetic pages 1-2, elsayed202512.retinopathyneuropathy pages 1-1)
- ADA screening intervals (type 1 within 5 years; type 2 at diagnosis; generally annual thereafter with risk-stratified extension to 1–2 years) operationalize secondary prevention via early detection and timely referral. (elsayed202512.retinopathyneuropathy pages 2-3, elsayed202512.retinopathyneuropathy pages 1-2, elsayed202512.retinopathyneuropathy media 6876c524)

---

## 14. Other Species / Natural Disease
No veterinary/natural disease evidence was retrieved in the tool-accessible corpus for this report. (No in-corpus evidence)

---

## 15. Model Organisms
No model-organism–specific evidence was retrieved in the tool-accessible corpus for this report. (No in-corpus evidence)

---

## Recent developments and real-world implementations (2023–2024 emphasis)

1) **AI-enabled and teleophthalmology screening is now guideline-referenced and increasingly deployed.** ADA 2025 includes FDA-approved autonomous AI systems (e.g., EyeArt, LumineticsCore, AEYE-DS) as acceptable screening approaches when implemented with validated workflows and appropriate referral for abnormal/ungradable results. (elsayed202512.retinopathyneuropathy pages 1-2)

2) **Low-cost imaging implementations are being clinically validated.** A 2023 multicenter validation study found a smartphone-based/handheld fundus camera performed comparably to tabletop cameras for DR/DME screening with substantial agreement and high sensitivity/specificity for referable DR, supporting expansion of screening coverage in resource-limited settings. (de Oliveira et al., 2023; https://doi.org/10.1007/s00592-023-02105-z) (paper retrieved; see artifact row) (wong2018guidelinesondiabetic pages 1-2)

3) **Therapeutic development is shifting toward durability and multi-pathway targeting.** Mechanistic reviews and Open Targets associations highlight VEGF (VEGFA) and ANGPT2 biology, consistent with interest in dual-pathway approaches (e.g., faricimab) and in treating inflammation/oxidative stress upstream of late-stage vascular manifestations. (OpenTargets Search: diabetic retinopathy, srejovic2024molecularandcellular pages 1-3)

---

## Key limitations of this report (evidence gaps in tool-accessible corpus)
- Explicit ICD/ICD-11, MeSH, OMIM, Orphanet, and MONDO identifiers were not available as citable evidence in the retrieved corpus. (No in-corpus evidence)
- Variant-level genetics, protective factors, and formal gene–environment interaction studies were not captured in the retrieved evidence set, beyond target associations and mechanistic pathway discussions. (OpenTargets Search: diabetic retinopathy, gomezjimenez2025modulationofoxidative pages 7-8)
- Model-organism and cross-species disease evidence was not retrieved. (No in-corpus evidence)

---

## URLs and publication dates (high-value sources)
- ADA Standards of Care in Diabetes—2025 (Diabetes Care; Dec 2025): https://doi.org/10.2337/dc25-s012 (elsayed202512.retinopathyneuropathy pages 2-3)
- ICO/International Council of Ophthalmology diabetic eye care guideline (Ophthalmology; May 2018): https://doi.org/10.1016/j.ophtha.2018.04.007 (wong2018guidelinesondiabetic pages 2-3)
- Ethiopia DR prevalence + risk factors meta-analysis (Scientific Reports; Nov 2024): https://doi.org/10.1038/s41598-024-78596-9 (wondmeneh2024prevalenceofdiabetic pages 1-2)
- Global blindness due to DR (Ophthalmology and Therapy; Aug 2025): https://doi.org/10.1007/s40123-025-01230-y (meng2025globalregionaland pages 1-2)
- Anti-VEGF outcomes synthesis (Clinical Ophthalmology; Dec 2024): https://doi.org/10.2147/OPTH.S489114 (aldokhail2024outcomesofantivegf pages 1-2)
- Anti-VEGF vs PRP HTA (Dec 2024): https://doi.org/10.3310/pcgv5709 (wong2018guidelinesondiabetic pages 1-2)
- DME treat-to-target/real-world burden review (Jul 2024): https://doi.org/10.1007/s00417-024-06558-y (nakao2024antivegftherapyfor pages 1-2)
- Example trial: NCT06662994: https://clinicaltrials.gov/study/NCT06662994 (NCT06662994 chunk 2)


References

1. (srejovic2024molecularandcellular pages 1-3): Jovana V. Srejovic, Maja D. Muric, Vladimir Lj. Jakovljevic, Ivan M. Srejovic, Suncica B. Sreckovic, Nenad T. Petrovic, Dusan Z. Todorovic, Sergey B. Bolevich, and Tatjana S. Sarenac Vulovic. Molecular and cellular mechanisms involved in the pathophysiology of retinal vascular disease—interplay between inflammation and oxidative stress. International Journal of Molecular Sciences, 25:11850, Nov 2024. URL: https://doi.org/10.3390/ijms252111850, doi:10.3390/ijms252111850. This article has 63 citations.

2. (wong2018guidelinesondiabetic pages 2-3): T. Wong, Jennifer K. Sun, R. Kawasaki, Paisan Ruamviboonsuk, N. Gupta, V. Lansingh, M. Maia, Wanjiku Mathenge, Sunil Moreker, Mahi M K Muqit, S. Resnikoff, J. Verdaguer, Peiquan Zhao, F. Ferris, L. Aiello, and H. Taylor. Guidelines on diabetic eye care: the international council of ophthalmology recommendations for screening, follow-up, referral, and treatment based on resource settings. Ophthalmology, 125 10:1608-1622, May 2018. URL: https://doi.org/10.1016/j.ophtha.2018.04.007, doi:10.1016/j.ophtha.2018.04.007. This article has 1088 citations and is from a highest quality peer-reviewed journal.

3. (elsayed202512.retinopathyneuropathy pages 1-1): Nuha A. ElSayed, Rozalina G. McCoy, Grazia Aleppo, Kirthikaa Balapattabi, Elizabeth A. Beverly, Kathaleen Briggs Early, Dennis Bruemmer, Brian C. Callaghan, Justin B. Echouffo-Tcheugui, Laya Ekhlaspour, Robert G. Frykberg, Rajesh Garg, Sunir J. Garg, John M. Giurini, Kamlesh Khunti, Rayhan Lal, Ildiko Lingvay, Glenn Matfin, Naushira Pandya, Elizabeth J. Pekas, Scott J. Pilla, Sarit Polsky, Alissa R. Segal, Jane Jeffrie Seley, Robert C. Stanton, and Raveendhara R. Bannuru. 12. retinopathy, neuropathy, and foot care: standards of care in diabetes—2025. Diabetes Care, 48:S252-S265, Dec 2025. URL: https://doi.org/10.2337/dc25-s012, doi:10.2337/dc25-s012. This article has 146 citations and is from a highest quality peer-reviewed journal.

4. (wong2018guidelinesondiabetic pages 1-2): T. Wong, Jennifer K. Sun, R. Kawasaki, Paisan Ruamviboonsuk, N. Gupta, V. Lansingh, M. Maia, Wanjiku Mathenge, Sunil Moreker, Mahi M K Muqit, S. Resnikoff, J. Verdaguer, Peiquan Zhao, F. Ferris, L. Aiello, and H. Taylor. Guidelines on diabetic eye care: the international council of ophthalmology recommendations for screening, follow-up, referral, and treatment based on resource settings. Ophthalmology, 125 10:1608-1622, May 2018. URL: https://doi.org/10.1016/j.ophtha.2018.04.007, doi:10.1016/j.ophtha.2018.04.007. This article has 1088 citations and is from a highest quality peer-reviewed journal.

5. (wong2018guidelinesondiabetic pages 7-9): T. Wong, Jennifer K. Sun, R. Kawasaki, Paisan Ruamviboonsuk, N. Gupta, V. Lansingh, M. Maia, Wanjiku Mathenge, Sunil Moreker, Mahi M K Muqit, S. Resnikoff, J. Verdaguer, Peiquan Zhao, F. Ferris, L. Aiello, and H. Taylor. Guidelines on diabetic eye care: the international council of ophthalmology recommendations for screening, follow-up, referral, and treatment based on resource settings. Ophthalmology, 125 10:1608-1622, May 2018. URL: https://doi.org/10.1016/j.ophtha.2018.04.007, doi:10.1016/j.ophtha.2018.04.007. This article has 1088 citations and is from a highest quality peer-reviewed journal.

6. (wong2018guidelinesondiabetic pages 3-5): T. Wong, Jennifer K. Sun, R. Kawasaki, Paisan Ruamviboonsuk, N. Gupta, V. Lansingh, M. Maia, Wanjiku Mathenge, Sunil Moreker, Mahi M K Muqit, S. Resnikoff, J. Verdaguer, Peiquan Zhao, F. Ferris, L. Aiello, and H. Taylor. Guidelines on diabetic eye care: the international council of ophthalmology recommendations for screening, follow-up, referral, and treatment based on resource settings. Ophthalmology, 125 10:1608-1622, May 2018. URL: https://doi.org/10.1016/j.ophtha.2018.04.007, doi:10.1016/j.ophtha.2018.04.007. This article has 1088 citations and is from a highest quality peer-reviewed journal.

7. (meng2025globalregionaland pages 1-2): Yang Meng, Yuan Liu, Yuan Ma, Ziye Chen, Runping Duan, Lan Jiang, and Tao Li. Global, regional, and national burden of blindness due to diabetic retinopathy, 1990–2021. Ophthalmology and Therapy, 14:2599-2615, Aug 2025. URL: https://doi.org/10.1007/s40123-025-01230-y, doi:10.1007/s40123-025-01230-y. This article has 6 citations and is from a peer-reviewed journal.

8. (wondmeneh2024prevalenceofdiabetic pages 1-2): Temesgen Gebeyehu Wondmeneh and Jemal Abdu Mohammed. Prevalence of diabetic retinopathy and its associated risk factors among adults in ethiopia: a systematic review and meta-analysis. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-78596-9, doi:10.1038/s41598-024-78596-9. This article has 24 citations and is from a peer-reviewed journal.

9. (wondmeneh2024prevalenceofdiabetic pages 12-15): Temesgen Gebeyehu Wondmeneh and Jemal Abdu Mohammed. Prevalence of diabetic retinopathy and its associated risk factors among adults in ethiopia: a systematic review and meta-analysis. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-78596-9, doi:10.1038/s41598-024-78596-9. This article has 24 citations and is from a peer-reviewed journal.

10. (elsayed202512.retinopathyneuropathy pages 2-3): Nuha A. ElSayed, Rozalina G. McCoy, Grazia Aleppo, Kirthikaa Balapattabi, Elizabeth A. Beverly, Kathaleen Briggs Early, Dennis Bruemmer, Brian C. Callaghan, Justin B. Echouffo-Tcheugui, Laya Ekhlaspour, Robert G. Frykberg, Rajesh Garg, Sunir J. Garg, John M. Giurini, Kamlesh Khunti, Rayhan Lal, Ildiko Lingvay, Glenn Matfin, Naushira Pandya, Elizabeth J. Pekas, Scott J. Pilla, Sarit Polsky, Alissa R. Segal, Jane Jeffrie Seley, Robert C. Stanton, and Raveendhara R. Bannuru. 12. retinopathy, neuropathy, and foot care: standards of care in diabetes—2025. Diabetes Care, 48:S252-S265, Dec 2025. URL: https://doi.org/10.2337/dc25-s012, doi:10.2337/dc25-s012. This article has 146 citations and is from a highest quality peer-reviewed journal.

11. (elsayed202512.retinopathyneuropathy pages 1-2): Nuha A. ElSayed, Rozalina G. McCoy, Grazia Aleppo, Kirthikaa Balapattabi, Elizabeth A. Beverly, Kathaleen Briggs Early, Dennis Bruemmer, Brian C. Callaghan, Justin B. Echouffo-Tcheugui, Laya Ekhlaspour, Robert G. Frykberg, Rajesh Garg, Sunir J. Garg, John M. Giurini, Kamlesh Khunti, Rayhan Lal, Ildiko Lingvay, Glenn Matfin, Naushira Pandya, Elizabeth J. Pekas, Scott J. Pilla, Sarit Polsky, Alissa R. Segal, Jane Jeffrie Seley, Robert C. Stanton, and Raveendhara R. Bannuru. 12. retinopathy, neuropathy, and foot care: standards of care in diabetes—2025. Diabetes Care, 48:S252-S265, Dec 2025. URL: https://doi.org/10.2337/dc25-s012, doi:10.2337/dc25-s012. This article has 146 citations and is from a highest quality peer-reviewed journal.

12. (elsayed202512.retinopathyneuropathy media 6876c524): Nuha A. ElSayed, Rozalina G. McCoy, Grazia Aleppo, Kirthikaa Balapattabi, Elizabeth A. Beverly, Kathaleen Briggs Early, Dennis Bruemmer, Brian C. Callaghan, Justin B. Echouffo-Tcheugui, Laya Ekhlaspour, Robert G. Frykberg, Rajesh Garg, Sunir J. Garg, John M. Giurini, Kamlesh Khunti, Rayhan Lal, Ildiko Lingvay, Glenn Matfin, Naushira Pandya, Elizabeth J. Pekas, Scott J. Pilla, Sarit Polsky, Alissa R. Segal, Jane Jeffrie Seley, Robert C. Stanton, and Raveendhara R. Bannuru. 12. retinopathy, neuropathy, and foot care: standards of care in diabetes—2025. Diabetes Care, 48:S252-S265, Dec 2025. URL: https://doi.org/10.2337/dc25-s012, doi:10.2337/dc25-s012. This article has 146 citations and is from a highest quality peer-reviewed journal.

13. (gomezjimenez2025modulationofoxidative pages 7-8): Verónica Gómez-Jiménez, R. Burggraaf-Sánchez de Las Matas, and Ángel Luis Ortega. Modulation of oxidative stress in diabetic retinopathy: therapeutic role of natural polyphenols. Antioxidants, Jul 2025. URL: https://doi.org/10.3390/antiox14070875, doi:10.3390/antiox14070875. This article has 18 citations.

14. (toma2026oxidativestressin pages 1-2): Caterina Toma, Diego Ferdeghini, Mohammad Mostafa Ola Pour, Sakthipriyan Venkatesan, Stefano De Cillà, and Elena Grossini. Oxidative stress in diabetic retinopathy: pathogenic mechanisms, biomarkers and clinical implications. Antioxidants, 15:425, Mar 2026. URL: https://doi.org/10.3390/antiox15040425, doi:10.3390/antiox15040425. This article has 1 citations.

15. (roy2025pathophysiologicalmechanismsof pages 23-24): Bipradas Roy. Pathophysiological mechanisms of diabetes-induced macrovascular and microvascular complications: the role of oxidative stress. Medical Sciences, Jul 2025. URL: https://doi.org/10.3390/medsci13030087, doi:10.3390/medsci13030087. This article has 72 citations.

16. (srejovic2024molecularandcellular pages 3-4): Jovana V. Srejovic, Maja D. Muric, Vladimir Lj. Jakovljevic, Ivan M. Srejovic, Suncica B. Sreckovic, Nenad T. Petrovic, Dusan Z. Todorovic, Sergey B. Bolevich, and Tatjana S. Sarenac Vulovic. Molecular and cellular mechanisms involved in the pathophysiology of retinal vascular disease—interplay between inflammation and oxidative stress. International Journal of Molecular Sciences, 25:11850, Nov 2024. URL: https://doi.org/10.3390/ijms252111850, doi:10.3390/ijms252111850. This article has 63 citations.

17. (du2024globalresearchtrends pages 1-2): Kejie Du, Yichong Liu, Xintong Zhao, Haowen Wang, Xiaomei Wan, Xiaoyan Sun, and Wenjuan Luo. Global research trends and hotspots of oxidative stress in diabetic retinopathy (2000-2024). Frontiers in Endocrinology, Aug 2024. URL: https://doi.org/10.3389/fendo.2024.1428411, doi:10.3389/fendo.2024.1428411. This article has 6 citations.

18. (elsayed202512.retinopathyneuropathy pages 3-4): Nuha A. ElSayed, Rozalina G. McCoy, Grazia Aleppo, Kirthikaa Balapattabi, Elizabeth A. Beverly, Kathaleen Briggs Early, Dennis Bruemmer, Brian C. Callaghan, Justin B. Echouffo-Tcheugui, Laya Ekhlaspour, Robert G. Frykberg, Rajesh Garg, Sunir J. Garg, John M. Giurini, Kamlesh Khunti, Rayhan Lal, Ildiko Lingvay, Glenn Matfin, Naushira Pandya, Elizabeth J. Pekas, Scott J. Pilla, Sarit Polsky, Alissa R. Segal, Jane Jeffrie Seley, Robert C. Stanton, and Raveendhara R. Bannuru. 12. retinopathy, neuropathy, and foot care: standards of care in diabetes—2025. Diabetes Care, 48:S252-S265, Dec 2025. URL: https://doi.org/10.2337/dc25-s012, doi:10.2337/dc25-s012. This article has 146 citations and is from a highest quality peer-reviewed journal.

19. (cheema2024diabeticmacularedema pages 5-7): Abdullah A Cheema and Haider R Cheema. Diabetic macular edema management: a review of anti-vascular endothelial growth factor (vegf) therapies. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.52676, doi:10.7759/cureus.52676. This article has 56 citations.

20. (aldokhail2024outcomesofantivegf pages 1-2): Laila Aldokhail, Abdulaziz Alhadlaq, Lujain Alaradi, Lamees Alaradi, and Fatimah AlShaikh. Outcomes of anti-vegf therapy in eyes with diabetic macular edema, vein occlusion-related macular edema, and neovascular age-related macular degeneration: a systematic review. Clinical Ophthalmology (Auckland, N.Z.), 18:3837-3851, Dec 2024. URL: https://doi.org/10.2147/opth.s489114, doi:10.2147/opth.s489114. This article has 23 citations.

21. (aldokhail2024outcomesofantivegf pages 4-5): Laila Aldokhail, Abdulaziz Alhadlaq, Lujain Alaradi, Lamees Alaradi, and Fatimah AlShaikh. Outcomes of anti-vegf therapy in eyes with diabetic macular edema, vein occlusion-related macular edema, and neovascular age-related macular degeneration: a systematic review. Clinical Ophthalmology (Auckland, N.Z.), 18:3837-3851, Dec 2024. URL: https://doi.org/10.2147/opth.s489114, doi:10.2147/opth.s489114. This article has 23 citations.

22. (nakao2024antivegftherapyfor pages 1-2): Shintaro Nakao, Sentaro Kusuhara, and Tomoaki Murakami. Anti-vegf therapy for the long-term management of diabetic macular edema: a treat-to-target strategy based on macular morphology. Graefe's Archive for Clinical and Experimental Ophthalmology, 262:3749-3759, Jul 2024. URL: https://doi.org/10.1007/s00417-024-06558-y, doi:10.1007/s00417-024-06558-y. This article has 22 citations.

23. (NCT02471651 chunk 1):  Dexamethasone Intravitreal Implant for the Treatment of Persistent Diabetic Macular Edema. California Retina Consultants. 2015. ClinicalTrials.gov Identifier: NCT02471651

24. (OpenTargets Search: diabetic retinopathy): Open Targets Query (diabetic retinopathy, 28 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

25. (simmonds2024antivegfdrugscompared pages 25-27): Mark Simmonds, Alexis Llewellyn, Ruth Walker, Helen Fulbright, Matthew Walton, Rob Hodgson, Laura Bojke, Lesley Stewart, Sofia Dias, Thomas Rush, John G Lawrenson, Tunde Peto, and David Steel. Anti-vegf drugs compared with laser photocoagulation for the treatment of diabetic retinopathy: a systematic review and meta-analysis. Health technology assessment, pages 1-71, Dec 2024. URL: https://doi.org/10.3310/pcgv5709, doi:10.3310/pcgv5709. This article has 17 citations and is from a peer-reviewed journal.

26. (NCT06662994 chunk 2):  High Dose Aflibercept in Diabetic Macular Edema in Patients With Previous Vitrectomy. Retina Consultants of Orange County. 2025. ClinicalTrials.gov Identifier: NCT06662994

27. (NCT06662994 chunk 1):  High Dose Aflibercept in Diabetic Macular Edema in Patients With Previous Vitrectomy. Retina Consultants of Orange County. 2025. ClinicalTrials.gov Identifier: NCT06662994

28. (NCT07144865 chunk 2): Bojie Hu. Biological Changes in Fibrovascular Membranes of Patients With Proliferative Diabetic Retinopathy Following Faricimab Injection. Bojie Hu. 2024. ClinicalTrials.gov Identifier: NCT07144865

## Artifacts

- [Edison artifact artifact-00](Diabetic_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000028 In the provided document (Section 12 of the ADA Standards of Care in Diabetes—2025), there is no specific figure or table summarizi](Diabetic_Retinopathy-deep-research-falcon_artifacts/image-1.png)