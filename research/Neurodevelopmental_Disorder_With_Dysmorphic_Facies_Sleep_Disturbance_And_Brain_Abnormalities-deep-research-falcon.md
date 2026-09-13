---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-15T08:34:56.690237'
end_time: '2026-08-15T08:44:16.778247'
duration_seconds: 560.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder With Dysmorphic Facies, Sleep Disturbance,
    and Brain Abnormalities
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 4
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Neurodevelopmental_Disorder_With_Dysmorphic_Facies_Sleep_Disturbance_And_Brain_Abnormalities-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Dysmorphic Facies, Sleep Disturbance, and Brain Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Dysmorphic Facies, Sleep Disturbance, and Brain Abnormalities** covering all of the
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
- **Disease Name:** Neurodevelopmental Disorder With Dysmorphic Facies, Sleep Disturbance, and Brain Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Dysmorphic Facies, Sleep Disturbance, and Brain Abnormalities** covering all of the
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


# Neurodevelopmental Disorder With Dysmorphic Facies, Sleep Disturbance, and Brain Abnormalities

## Executive summary

This is an ultra-rare, dominantly inherited **KAT5-related chromatinopathy** characterized by developmental delay/intellectual disability, severe circadian/sleep disturbance, epilepsy, short stature, behavioral abnormalities, recognizable facial dysmorphism, and structural brain abnormalities—particularly corpus-callosum defects and cerebellar atrophy. The defining evidence remains a 2020 report of only **three unrelated individuals**; therefore, every apparent frequency below is provisional and should not be treated as a population estimate. The causal variants were heterozygous, de novo missense substitutions that impaired the histone-acetyltransferase activity of KAT5-containing NuA4/TIP60 complexes. No disease-specific natural-history study, clinical guideline, prevalence estimate, clinical trial, or disease-modifying treatment was identified through 2024. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 6-7, humbert2020denovokat5 pages 1-2)

**Foundational source:** Humbert J, et al. *American Journal of Human Genetics*. Published online **20 August 2020**; issue date **3 September 2020**. PMID **32822602**. DOI/URL: https://doi.org/10.1016/j.ajhg.2020.08.002. The abstract concludes: **“dominant missense KAT5 variants cause histone acetylation deficiency with transcriptional dysregulation of multiple genes.”** (humbert2020denovokat5 pages 1-2)

---

## 1. Disease information

### Definition and identifiers

- **Preferred name:** Neurodevelopmental disorder with dysmorphic facies, sleep disturbance, and brain abnormalities.
- **MONDO:** **MONDO:0030852**.
- **Causal gene:** **KAT5**, lysine acetyltransferase 5, formerly **TIP60/HTATIP**; OMIM gene **MIM *601409**.
- **Synonyms suitable for indexing:** *KAT5-related neurodevelopmental disorder*, *KAT5-related chromatinopathy*, *TIP60-related neurodevelopmental syndrome*, and the primary-paper description, *syndrome with recognizable facial dysmorphisms, cerebellar atrophy, sleep disturbance, and epilepsy*.
- **OMIM disease number:** not reliably established from the retrieved primary text; do not infer one from the KAT5 gene MIM number.
- **Orphanet, MeSH, ICD-10/ICD-11:** no disease-specific identifier was identified. Coding will generally use broader categories for genetic neurodevelopmental disorder, intellectual disability, epilepsy, sleep disorder, and congenital malformations.

Open Targets assigns the principal association to KAT5 (score 0.697; evidence ultimately referencing PMID 32822602). A weaker RNASEH2C association appears in that database, but the defining human cohort and functional evidence concern **KAT5**; RNASEH2C should not presently be annotated as an independently established second cause of this named syndrome. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies, sleep disturbance, and brain abnormalities)

### Evidence provenance

The evidence is **patient-level clinical and experimental research aggregated into a three-person disease description**, not an EHR-derived population analysis. One individual had previously appeared in a Smith–Magenis-like exome cohort; two additional cases were connected through GeneMatcher. (humbert2020denovokat5 pages 6-7, humbert2020denovokat5 pages 1-2)

---

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is a **germline heterozygous de novo KAT5 missense variant** affecting a functionally constrained residue. All three substitutions impaired KAT5 acetyltransferase function. The likely disease mechanism is a dominant deleterious effect of catalytically defective protein incorporated into an otherwise intact NuA4/TIP60 complex, rather than simple haploinsufficiency. The authors described the biochemical outcome as partial loss of function but noted that ordinary KAT5 haploinsufficiency may not be sufficient for disease. (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 6-7)

### Risk factors

- **Genetic:** a pathogenic missense alteration in a critical KAT5 chromodomain or catalytic/acetyl-CoA-binding region is the only demonstrated risk factor.
- **Family history:** absent in the three families because every variant was de novo. Affected individuals would nevertheless have an expected 50% transmission probability under autosomal-dominant inheritance, subject to reproductive fitness and penetrance.
- **Parental age, sex, ancestry, environmental exposure, infection, toxin, diet, or lifestyle:** no association established.
- **Modifiers, protective alleles, founder effects, or anticipation:** none reported.
- **Gene–environment interaction:** no disease-specific evidence. Although acetylation depends metabolically on acetyl-CoA, extrapolating dietary or metabolic modification to this syndrome would be unsupported.

### Protective factors

No genetic or environmental factor has been shown to prevent disease or reduce penetrance. Standard developmental, seizure, and sleep care may reduce morbidity but is tertiary management, not primary prevention.

---

## 3. Phenotypes

The phenotype table below reproduces the patient-level evidence. Frequencies are fractions of three and have extremely wide uncertainty.

| Feature/category | Individual 1 | Individual 2 | Individual 3 | Cohort frequency |
|---|---|---|---|---|
| Age/sex | 29-30-year-old female (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | 13-year-old male (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 3-6) | 18-month-old to 2-year-old male (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | 3/3 reported (humbert2020denovokat5 pages 7-8) |
| Exact KAT5 HGVS variant | c.158G>A (p.Arg53His), de novo (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 3-6) | c.1105T>A (p.Cys369Ser), de novo (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | c.1237T>G (p.Ser413Ala), de novo (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | 3/3 with heterozygous de novo missense variants (humbert2020denovokat5 pages 1-2) |
| Microcephaly | No (head circumference 55 cm, 73rd centile) (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | Yes; HC 50 cm, 1st centile, -2.6 SD (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 3-6) | Yes; congenital microcephaly, HC 44.5 cm, <1st centile, -2.2 SD (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | 2/3 (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 6-7) |
| DD/ID and IQ | Intellectual disability; IQ 40 at age 29; expressive language ~8-year level, receptive 4-5-year level (humbert2020denovokat5 pages 2-3) | Intellectual disability; nonverbal; IQ 20-30 (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 3-6) | Severe developmental delay (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | 3/3 (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 1-2) |
| Sleep disorder | Since early childhood: early sleep offset, 1-2 nighttime awakenings, increased daytime naps; diary with early morning awakening, 2 daytime naps, nocturnal awakenings; elevated daytime salivary melatonin (humbert2020denovokat5 pages 2-3) | Severe sleep disorder with sleep onset delay and night waking (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 3-6) | Important sleep disorder with night waking and sleep onset delay; improved by nighttime clonidine (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 6-7) | 3/3 (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 1-2) |
| Seizures | Adult-onset seizures (humbert2020denovokat5 pages 2-3) | Generalized tonic-clonic seizures (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 3-6) | Generalized myoclonic seizures (humbert2020denovokat5 pages 2-3) | 3/3 (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 1-2) |
| Brain MRI / CNS findings | Partial agenesis of corpus callosum (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | Global progressive cerebellar atrophy (vermis > hemispheres); corpus callosum dysgenesis (short, thickened, hypoplasia of rostrum and splenium); small anterior pituitary gland (humbert2020denovokat5 pages 3-6) | Polymicrogyria of right sylvian fissure; cystic dilation of 4th ventricle; inferior cerebellar vermis atrophy (humbert2020denovokat5 pages 2-3) | Corpus callosum anomaly 2/3; cerebellar atrophy 2/3; polymicrogyria 1/3 (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 6-7) |
| Behavior | Behavioral problems, perseverative speech, disruptive behavior, attention deficit disorder/ADHD, poor language function (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 7-8) | Disruptive behavior, hyperactivity/ADHD, multiple stereotypies (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 7-8) | Behavioral difficulties with tantrums and head banging; disruptive behaviors (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | 3/3 disruptive/behavioral issues (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 6-7) |
| Stature / growth | Moderately short, about -1.95 SD (cohort summary); exact height NR (humbert2020denovokat5 pages 6-7) | Moderately short, about -2.1 SD; GH deficiency diagnosed at age 2 and treated with GH injections (humbert2020denovokat5 pages 6-7, humbert2020denovokat5 pages 3-6) | Short stature; height 71.1 cm, <1st centile, -2.9 SD at 16 months (humbert2020denovokat5 pages 2-3) | 3/3 moderately short (humbert2020denovokat5 pages 6-7, humbert2020denovokat5 pages 1-2) |
| Genitourinary | Frequent/recurrent urinary tract infections (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 7-8) | Unilateral cryptorchidism; horseshoe kidney; bilateral vesico-ureteral reflux (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 7-8) | Hypospadias and bilateral cryptorchidism (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 7-8) | 3/3 (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 6-7) |
| Cardiac | NR / no congenital heart defect reported (humbert2020denovokat5 pages 7-8) | NR / no congenital heart defect reported (humbert2020denovokat5 pages 7-8) | Perimembranous ventricular septal defect; dysplastic pulmonary valve with supravalvular and valvular stenosis (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 7-8) | 1/3 (humbert2020denovokat5 pages 7-8) |
| Orofacial | NR (humbert2020denovokat5 pages 7-8) | Unilateral cleft lip and palate (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 6-7) | High-arched palate with submucous cleft palate (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 6-7) | 2/3 (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 6-7) |
| Ocular | Severe myopia; almond-shaped eyes (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 7-8) | Strabismus and hypermetropia (humbert2020denovokat5 pages 7-8) | Epiblepharon (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3) | 3/3 ocular anomaly (humbert2020denovokat5 pages 7-8) |
| Recognizable facial findings | Round face, flat facial profile, prognathism, down-slanting corners of mouth, low-set ears, depressed nasal bridge, almond-shaped eyes (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 7-8) | Prognathism, lateral thinning of eyebrows, macrostomia, thick lower lip, bulbous asymmetric nose, prominent chin (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 7-8) | Round face, flat facial profile, epicanthal folds, down-slanting corners of mouth, upturned nose, depressed nasal bridge (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 7-8) | Round face/flat profile 2/3; down-slanting mouth corners 2/3; depressed nasal bridge 2/3; prognathism 2/3 (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 6-7) |


*Table: This table summarizes patient-level clinical and genetic findings for the three individuals with KAT5-related syndrome reported by Humbert et al. 2020. It is useful for quickly comparing core phenotypes, MRI findings, and variant details across the cohort.*

### Core phenotype interpretation and suggested HPO terms

- **Global developmental delay / intellectual disability — 3/3:** congenital/early-childhood onset, moderate-to-severe or severe, apparently lifelong. Suggested HPO: **Global developmental delay (HP:0001263)**, **Intellectual disability (HP:0001249)**, **Severe intellectual disability (HP:0010864)**, **Absent speech (HP:0001344)** where applicable. Daily impact is profound: one adolescent was nonverbal, and the adult had IQ 40 with markedly reduced receptive and expressive language. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3)
- **Sleep disturbance — 3/3:** early-childhood onset where documented; night waking in all, sleep-onset delay in two, daytime sleepiness/napping and early sleep offset in one. Suggested HPO: **Sleep disturbance (HP:0002360)**, **Difficulty falling asleep (HP:0031354)**, **Abnormality of circadian rhythm** and **Daytime somnolence**. The adult’s diary documented bedtime 20:30, awakenings around 23:00 and 01:00, waking at 05:30–06:30, and two daytime naps; mean daytime salivary melatonin was 46 pg/mL from two samples. This disrupts patient and caregiver functioning, but no validated QoL instrument was reported. (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 2-3)
- **Epilepsy — 3/3:** generalized tonic-clonic, generalized myoclonic, or unspecified adult-onset seizures. Suggested HPO: **Seizure (HP:0001250)**, **Generalized tonic-clonic seizure (HP:0002069)**, **Myoclonic seizure (HP:0032794)**. EEG details and response rates were not reported. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3)
- **Behavioral/neuropsychiatric abnormalities — 3/3:** ADHD/hyperactivity, disruptive behavior, stereotypies, perseveration, tantrums, and head banging. Suggested HPO: **Abnormal behavior (HP:0000708)**, **Attention deficit hyperactivity disorder (HP:0007018)**, **Stereotypy (HP:0000733)**, **Self-injurious behavior (HP:0100716)**, **Aggressive behavior (HP:0000718)**. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3)
- **Short stature — 3/3:** approximately −1.95, −2.1, and −2.9 SD; one patient had diagnosed growth-hormone deficiency. Suggested HPO: **Short stature (HP:0004322)** and, when measured, **Growth hormone deficiency (HP:0000824)**. (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 6-7)
- **Microcephaly — 2/3:** congenital in the infant; absent in the adult. Suggested HPO: **Microcephaly (HP:0000252)**, **Congenital microcephaly (HP:0011451)**. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3)
- **Brain malformations — 3/3:** corpus-callosum abnormality 2/3, cerebellar atrophy 2/3, focal polymicrogyria 1/3, fourth-ventricle cystic dilation 1/3, small anterior pituitary 1/3. Suggested HPO: **Agenesis of corpus callosum (HP:0001274)**, **Abnormal corpus callosum morphology (HP:0001273)**, **Cerebellar atrophy (HP:0001272)**, **Polymicrogyria (HP:0002126)**, and **Pituitary hypoplasia (HP:0010628)**. (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 7-8)
- **Dysmorphism:** round/flat facial profile, depressed nasal bridge, downturned mouth corners, and prognathism each occurred in at least two individuals. Orofacial clefting occurred in 2/3. Suggested HPO includes **Round face (HP:0000311)**, **Flat face (HP:0012368)**, **Depressed nasal bridge (HP:0005280)**, **Downturned corners of mouth (HP:0002714)**, **Prognathism (HP:0000303)**, **Cleft lip (HP:0410030)**, **Cleft palate (HP:0000175)**, and **Submucous cleft hard palate (HP:0011812)**. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 6-7)
- **Genitourinary involvement — 3/3:** urinary infections, horseshoe kidney, vesicoureteral reflux, cryptorchidism, and hypospadias. Suggested HPO: **Horseshoe kidney (HP:0000085)**, **Vesicoureteral reflux (HP:0000076)**, **Cryptorchidism (HP:0000028)**, **Hypospadias (HP:0000047)**. (humbert2020denovokat5 pages 7-8)
- **Other variable findings:** congenital heart disease 1/3, ocular abnormalities 3/3, kyphoscoliosis and brachydactyly in the adult, and hearing hypersensitivity. These are currently associated rather than defining manifestations. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3)

No formal phenotype progression scale, laboratory signature, patient-reported outcome, EQ-5D, SF-36, or PROMIS study exists.

---

## 4. Genetic and molecular information

### Gene and protein

**KAT5** encodes the catalytic lysine acetyltransferase of the nuclear **NuA4/TIP60-p400 complex**, which includes TRRAP, EP400, and ING3. KAT5 acetylates histones H4 and H2A/H2A.Z/H2A.X and selected non-histone proteins, contributing to transcription, chromatin remodeling, DNA double-strand-break repair, apoptosis, chromosome segregation, stem-cell maintenance, and proliferation. (humbert2020denovokat5 pages 1-2)

### Reported pathogenic variants

All use **NM_006388.3**:

1. **c.158G>A, p.Arg53His** — chromodomain; de novo; absent from gnomAD; CADD 32.
2. **c.1105T>A, p.Cys369Ser** — near the acetyl-CoA-binding/catalytic region and a residue required for MYST-family catalysis and autoacetylation; de novo; absent from gnomAD; CADD 27.
3. **c.1237T>G, p.Ser413Ala** — acetyl-CoA-binding domain; de novo; absent from gnomAD; CADD 26.

All affected residues were invariant down to yeast Esa1. The variants were absent from more than 100,000 aggregated controls and were predicted damaging by multiple algorithms. KAT5 showed missense constraint (gnomAD v2.1.1 observed/expected 0.44, 90% CI 0.39–0.51; Z=3.61), whereas its loss-of-function constraint was less compelling (pLI 0.09; o/e 0.26, 90% CI 0.15–0.47). (humbert2020denovokat5 pages 3-6)

The paper predates routine disease-specific ClinGen curation, and the retrieved evidence does not supply current ClinVar assertion counts. For knowledge-base purposes, these three variants have strong disease-level evidence—de novo occurrence, phenotype concordance, population absence, conserved/domain location, and abnormal functional assays—but a current ACMG classification should be checked directly in ClinVar or reassessed by a diagnostic laboratory.

### Functional consequence

Variant proteins still assembled into full stoichiometric NuA4/TIP60 complexes. However, all had reduced acetyltransferase activity. p.Cys369Ser could not acetylate free histones or chromatin; p.Arg53His and p.Ser413Ala were predominantly defective on chromatin. The defect particularly affected nucleosomal histone-H4-tail acetylation while some H2A acetylation remained. This supports catalytic deficiency and a possible dominant-negative or dominant-interfering mechanism, not failure of complex assembly. (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 6-7)

### Chromosomal and epigenetic findings

No pathogenic deletion, duplication, inversion, translocation, aneuploidy, repeat expansion, mitochondrial variant, or somatic variant was reported. No validated DNA-methylation episignature exists. The demonstrated epigenetic defect is deficient histone acetylation and downstream transcriptional dysregulation. Modifier genes are unknown.

---

## 5. Environmental, lifestyle, and infectious information

No toxin, radiation, pollution, occupational exposure, maternal illness, infection, diet, smoking, alcohol, or exercise association has been reported. The condition is congenital and monogenic. Environmental factors may modify sleep, seizures, learning, and general health, but none has been demonstrated to alter penetrance or the primary molecular lesion. Infectious causation and zoonotic transmission are not applicable.

---

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream trigger:** a de novo missense variant alters the KAT5 chromodomain or catalytic/acetyl-CoA-binding region.
2. **Protein-complex effect:** mutant KAT5 enters an otherwise normally assembled NuA4/TIP60 complex.
3. **Primary biochemical defect:** reduced/abolished lysine-acetyltransferase activity, especially nucleosomal H4-tail acetylation.
4. **Chromatin/transcription consequence:** disturbed chromatin-dependent gene regulation and altered developmental/circadian transcription.
5. **Measured patient-cell signature:** **LHX9** and **KIRREL3** were consistently downregulated; **GFPT2, PER1, and HDAC4** were upregulated in fibroblasts from individuals 2 and 3. PER1 and HDAC4 loci had previously been identified as NuA4/TIP60-bound regions. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 6-7)
6. **Plausible downstream manifestations:** altered neuronal differentiation and synapse formation contribute to ID/epilepsy/brain malformation; disturbed PER1/BMAL1 circadian regulation contributes to abnormal sleep; impaired developmental gene expression contributes to craniofacial, growth, cardiac, and genitourinary malformations. These links are biologically plausible but not all were directly demonstrated in patient neurons. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 1-2)

KIRREL3 participates in hippocampal mossy-fiber synapse development. LHX9 contributes to thalamic neuronal differentiation and hypocretin-neuron specification/survival; Lhx9-null mice have profound hypersomnolence. KAT5 also acetylates BMAL1 and regulates the mammalian circadian clock, while Drosophila studies link Tip60 to learning, memory, and sleep through axonal growth in pacemaker cells. (humbert2020denovokat5 pages 7-8)

### Suggested ontology annotations

- **GO biological process:** histone acetylation; chromatin organization; regulation of transcription by RNA polymerase II; DNA double-strand-break repair; regulation of circadian rhythm; neural development; synapse organization; regulation of apoptosis; chromosome segregation.
- **GO molecular function:** histone acetyltransferase activity; lysine N-acetyltransferase activity; acetyl-CoA binding; chromatin binding.
- **GO cellular component:** nucleus; nucleoplasm; NuA4 histone acetyltransferase complex/TIP60 complex; chromatin.
- **Candidate cell types (CL):** neural stem cell, radial glial cell, neuron, cerebral cortical neuron, cerebellar neuron, hippocampal neuron, hypothalamic hypocretin/orexin neuron, and pituitary endocrine cell. These are mechanistically plausible targets, not proven by human single-cell data.

### Omics and advanced technologies

- **Transcriptomics:** bulk RNA-seq of primary fibroblasts from two patients versus six controls, with RT-qPCR validation; GEO **GSE154199**. (humbert2020denovokat5 pages 8-9, humbert2020denovokat5 pages 2-3)
- **Proteomics:** mass spectrometry was used to assess NuA4/TIP60 complex assembly, not to define a systemic disease proteome.
- **Single-cell, spatial transcriptomics, metabolomics, lipidomics, patient-derived neural organoids, iPSC neurons, CRISPR disease screens, and multi-omics integration:** no disease-specific study identified through 2024.
- **Immune, metabolic, oxidative-stress, fibrosis, or tissue-necrosis mechanisms:** not established as central disease mechanisms.

---

## 7. Anatomical structures affected

### Organ and system level

- **Primary:** central nervous system—cerebral cortex, corpus callosum, cerebellum/vermis, circadian/sleep networks, and possibly anterior pituitary.
- **Secondary/variable:** craniofacial structures and palate, kidneys/urinary tract, male genital tract, eyes, skeleton, heart, and auditory system.

### Suggested UBERON/localization terms

Brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), corpus callosum (**UBERON:0002336**), cerebellum (**UBERON:0002037**), cerebellar vermis, hypothalamus (**UBERON:0001898**), pituitary gland (**UBERON:0000007**), kidney (**UBERON:0002113**), heart (**UBERON:0000948**), palate, eye, and urinary bladder/ureter. Focal polymicrogyria involved the **right Sylvian fissure**, establishing unilateral localization in that patient; other CNS abnormalities were midline or bilateral/global. (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 2-3)

### Subcellular level

The primary compartment is nuclear chromatin and the NuA4/TIP60 complex. No disease-specific mitochondrial, lysosomal, ER, or membrane lesion has been shown.

---

## 8. Temporal development and natural history

The disorder is congenital/developmental and chronic lifelong. Short stature, microcephaly, malformations, and developmental delay appear in infancy or childhood. Sleep problems were present from early childhood in the adult, and severe sleep disturbance was already evident in the infant. Epilepsy timing is variable: infancy/childhood in two patients, adult onset in one. (humbert2020denovokat5 pages 2-3)

Cerebellar atrophy was explicitly **progressive** in the 13-year-old; whether all patients undergo neurodegeneration is unknown. Intellectual and behavioral problems persisted into adulthood, but the adult retained some developmental acquisition and expressive speech. No formal stages, remission pattern, critical therapeutic window, regression frequency, or longitudinal rate has been established. Early childhood is nevertheless a practical intervention window for developmental, communication, sleep, seizure, hearing, and vision services.

---

## 9. Inheritance, penetrance, and population

- **Pattern:** autosomal dominant; all three known variants were de novo.
- **Penetrance:** appears high for these three functionally damaging missense variants, but cannot be quantified from three ascertained cases.
- **Expressivity:** variable—microcephaly, cerebellar atrophy, corpus-callosum abnormality, clefting, heart disease, and seizure onset differed among patients.
- **Sex:** one female and two males; no inference about sex ratio is possible.
- **Prevalence/incidence:** unknown; no population registry or epidemiologic estimate exists. Only three defining cases were available in the retrieved literature.
- **Geography/ancestry:** no enrichment or founder variant established.
- **Consanguinity/carrier frequency:** not relevant to the observed de novo dominant cases; carrier frequency is unknown and expected to be extremely low.
- **Germline mosaicism:** not reported. Counseling should retain a small recurrence risk from possible parental gonadal mosaicism despite negative parental blood testing.
- **Anticipation:** not applicable; no repeat expansion.

---

## 10. Diagnostics

### Recommended clinical work-up

There are no formal diagnostic criteria. Suspect the disorder in a person with syndromic DD/ID plus severe night waking or circadian disturbance, epilepsy, short stature, characteristic facial morphology, and corpus-callosum/cerebellar abnormalities.

1. **Genomic testing:** trio exome or genome sequencing with CNV calling is preferred. All established diagnoses were made by exome sequencing and confirmed as de novo. A comprehensive neurodevelopmental/epilepsy/chromatinopathy panel that includes **KAT5** is reasonable. Sanger confirmation and parental testing should establish segregation. (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 2-3)
2. **Variant interpretation:** prioritize rare heterozygous missense variants in the chromodomain or MYST catalytic/acetyl-CoA-binding region, especially conserved residues. Population absence alone is insufficient; de novo status, phenotype, domain location, and functional evidence are important.
3. **CMA/karyotype/FISH:** useful if a chromosomal disorder remains in the differential, but these methods will generally miss the known single-nucleotide KAT5 variants.
4. **Repeat-expansion, mitochondrial, or somatic testing:** not specifically indicated unless the broader phenotype suggests another diagnosis.
5. **RNA/epigenetic testing:** fibroblast RNA-seq is research-level; PER1/LHX9/KIRREL3 expression is not validated as a clinical biomarker. No methylation episignature is established.

### Baseline phenotyping after diagnosis

Brain MRI with attention to cerebellum, corpus callosum, cortical malformation, fourth ventricle, and pituitary; EEG and seizure assessment; formal developmental, speech-language, behavioral, and sleep evaluation; growth and endocrine testing including IGF-1/GH-axis evaluation if growth failure is present; renal ultrasound and urinalysis/UTI history; echocardiogram; ophthalmology, audiology, palate/feeding evaluation; and urologic examination in males.

### Differential diagnosis

- **Smith–Magenis syndrome/RAI1:** overlapping inverted circadian phenotype and facial/behavioral findings, but KAT5 cases showed seizures and genitourinary anomalies in all three and cerebellar/CNS malformations not typical of Smith–Magenis. (humbert2020denovokat5 pages 6-7)
- **KAT6A, KAT6B, KAT8, HDAC4, MBD5, KDM5B, MECP2, EHMT1, KMT2C, HDAC8, TRRAP-related disorders:** overlapping chromatinopathy, ID, sleep, seizure, growth, and malformation phenotypes. KAT6A overlap includes ID, microcephaly, epilepsy, and sleep disturbance; KAT6B overlap includes genital and corpus-callosum anomalies and cleft palate. (humbert2020denovokat5 pages 8-9)
- Other polymicrogyria/cerebellar atrophy syndromes and genetic epileptic encephalopathies should be excluded by broad sequencing.

### Screening

No newborn or population screening program exists. Cascade testing is appropriate if an affected person reproduces or if parental mosaicism is suspected. Prenatal or preimplantation testing becomes technically possible once the familial pathogenic variant is known.

---

## 11. Outcome and prognosis

Survival, life expectancy, mortality, and 5- or 10-year survival have not been measured. Survival to approximately 30 years in one patient shows that childhood lethality is not obligatory. Major morbidity comprises lifelong cognitive/communication disability, disrupted sleep, epilepsy, behavioral dysregulation, growth impairment, and multisystem congenital anomalies. (humbert2020denovokat5 pages 7-8, humbert2020denovokat5 pages 2-3)

Recovery to typical neurodevelopment is not expected from current evidence, but symptom improvement is possible. No prognostic biomarker is validated. Potential prognostic features requiring study include residual acetyltransferase activity, variant domain, extent of cortical/cerebellar malformation, epilepsy burden, and severity of circadian disruption.

---

## 12. Treatment and real-world implementation

### Current strategy

There is **no approved KAT5-directed or disease-modifying therapy**. Care is individualized and multidisciplinary:

- **Sleep:** sleep hygiene, circadian/sleep-specialist assessment, and monitoring for apnea or other secondary causes. Nighttime **clonidine** improved sleep-onset delay in one child; daytime dosing caused sleepiness. This is single-patient evidence, not a response rate or guideline. Suggested NCIT concepts: *Clonidine* and *Sleep Disorder Treatment*. (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 6-7)
- **Epilepsy:** seizure-type-guided antiseizure medication and rescue planning. No KAT5-specific drug or comparative response data exist. Suggested NCIT: *Anticonvulsant Therapy*.
- **Behavior:** behavioral intervention and child psychiatry; one child received **risperidone**, but efficacy and adverse effects were not reported. Suggested NCIT: *Behavioral Therapy*, *Risperidone*.
- **Development:** early physical, occupational, speech-language, feeding, and augmentative/alternative communication services. Suggested NCIT: *Physical Therapy*, *Occupational Therapy*, *Speech Therapy*.
- **Growth/endocrine:** treat documented endocrine deficiency; one patient received growth-hormone injections for GH deficiency, without reported outcome. Suggested NCIT: *Growth Hormone Replacement Therapy*. (humbert2020denovokat5 pages 3-6)
- **Organ-specific care:** standard management for cleft palate/lip, reflux or renal anomalies, cryptorchidism/hypospadias, cardiac defects, scoliosis, myopia/strabismus, and hearing abnormalities.

### Experimental therapy and pharmacogenomics

No KAT5-syndrome gene therapy, CRISPR therapy, RNA therapy, cell therapy, targeted epigenetic treatment, or disease-specific clinical trial was identified. No pharmacogenomic association is known. Because KAT5 is essential and has broad roles in DNA repair, transcription, apoptosis, and proliferation, nonspecific acetyltransferase or deacetylase manipulation could have substantial off-target and oncologic risks; cancer-directed KAT5 inhibitors should not be extrapolated to congenital KAT5 catalytic deficiency. (humbert2020denovokat5 pages 1-2)

---

## 13. Prevention

Primary prevention by lifestyle modification, vaccination, environmental control, or prophylactic medication is not applicable. Relevant measures are:

- **Genetic counseling:** explain the usually de novo dominant mechanism, low but non-zero sibling recurrence risk from possible gonadal mosaicism, and potential 50% transmission risk from an affected heterozygous individual.
- **Reproductive options:** targeted prenatal diagnosis or preimplantation genetic testing after identifying the familial pathogenic variant.
- **Secondary/tertiary prevention:** early genomic diagnosis; early developmental intervention; seizure treatment and safety planning; sleep management; surveillance for cerebellar progression, growth/endocrine dysfunction, renal/urinary complications, vision/hearing problems, scoliosis, and cardiac disease.

No immunization or public-health intervention is disease specific.

---

## 14. Other species and natural disease

No naturally occurring veterinary analogue, affected breed, zoonotic potential, or cross-species transmissibility has been reported. KAT5/Tip60/Esa1 function is evolutionarily conserved from yeast to mammals; the three human altered residues are conserved down to yeast Esa1. This conservation supports pathogenicity and the fundamental role of chromatin acetylation but does not constitute natural animal disease. (humbert2020denovokat5 pages 3-6)

Suggested taxa for comparative annotation include *Homo sapiens* (**NCBI Taxon 9606**), *Mus musculus* (**10090**), *Drosophila melanogaster* (**7227**), and *Saccharomyces cerevisiae* (**4932**).

---

## 15. Model organisms and experimental models

### Human cellular models

The strongest direct models were:

- Genome-edited **K562** cells expressing tagged wild-type or patient-variant KAT5 from the AAVS1 locus, used to purify native NuA4/TIP60 complexes and quantify histone/chromatin acetylation.
- Primary patient **fibroblasts** from two individuals, used for bulk RNA-seq and RT-qPCR. These captured transcriptional consequences but not neuron- or cerebellum-specific biology. (humbert2020denovokat5 pages 2-3, humbert2020denovokat5 pages 6-7)

### Mouse

Homozygous **Kat5 knockout is embryonic lethal**, demonstrating essential developmental function. Heterozygous knockout mice were reported as essentially normal in development, growth, and fertility, including IMPC phenotyping. This is an important limitation: simple murine haploinsufficiency does not reproduce the human syndrome and supports modeling the exact human missense alleles rather than a heterozygous null. Lhx9-null mice provide indirect support for the sleep pathway through profound hypersomnolence. (humbert2020denovokat5 pages 6-7, humbert2020denovokat5 pages 9-10)

### Drosophila and yeast

Drosophila Tip60 studies support roles in learning, memory, and sleep regulation through pacemaker-cell axonal growth, but no retrieved fly model carried one of the three human variants. Yeast Esa1 provides structural/catalytic conservation; the residue corresponding to human Cys369 is critical for MYST-family catalysis. (humbert2020denovokat5 pages 3-6, humbert2020denovokat5 pages 7-8)

### Priority future models

Exact-variant knock-in mice or zebrafish, patient-derived iPSC cortical and cerebellar neurons, hypothalamic circadian neurons, cerebral/cerebellar organoids, and rescue experiments restoring KAT5 activity are needed. Such models should assess H4 acetylation, chromatin accessibility, circadian oscillation, neuronal differentiation, synaptogenesis, seizure susceptibility, and cerebellar development.

---

## Evidence appraisal and 2023–2024 update

The disease-specific evidence base did **not materially expand in the retrieved 2023–2024 literature**. Recent chromatinopathy reviews emphasize that germline variants in epigenetic regulators can produce recognizable developmental syndromes and that episignatures are increasingly useful diagnostic biomarkers, but no validated KAT5 episignature, expanded KAT5 cohort, natural-history analysis, or targeted treatment was found. Accordingly, the 2020 three-patient primary report remains authoritative, and percentages such as “100% sleep disturbance” or “67% cerebellar atrophy” should always be stored with **n=3** and low confidence. (bukowskaolech2024chromatinopathiesinsightin pages 3-4, humbert2020denovokat5 pages 7-8)

### Key exact abstract quotation

> “All three individuals have cerebral malformations, seizures, global developmental delay or intellectual disability, and severe sleep disturbance.” The same abstract reports that variant complexes “decrease or abolish” histone-H4-tail acetylation and that patient fibroblasts had upregulated **PER1**, consistent with the sleep phenotype. (humbert2020denovokat5 pages 1-2)

This disease entry should therefore be treated as **well-supported at the gene–mechanism level but very immature at the epidemiologic, natural-history, prognostic, and therapeutic levels**.

References

1. (humbert2020denovokat5 pages 7-8): Jonathan Humbert, Smrithi Salian, Periklis Makrythanasis, Gabrielle Lemire, Justine Rousseau, Sophie Ehresmann, Thomas Garcia, Rami Alasiri, Armand Bottani, Sylviane Hanquinet, Erin Beaver, Jennifer Heeley, Ann C.M. Smith, Seth I. Berger, Stylianos E. Antonarakis, Xiang-Jiao Yang, Jacques Côté, and Philippe M. Campeau. De novo kat5 variants cause a syndrome with recognizable facial dysmorphisms, cerebellar atrophy, sleep disturbance, and epilepsy. The American Journal of Human Genetics, 107:564-574, Sep 2020. URL: https://doi.org/10.1016/j.ajhg.2020.08.002, doi:10.1016/j.ajhg.2020.08.002. This article has 52 citations.

2. (humbert2020denovokat5 pages 6-7): Jonathan Humbert, Smrithi Salian, Periklis Makrythanasis, Gabrielle Lemire, Justine Rousseau, Sophie Ehresmann, Thomas Garcia, Rami Alasiri, Armand Bottani, Sylviane Hanquinet, Erin Beaver, Jennifer Heeley, Ann C.M. Smith, Seth I. Berger, Stylianos E. Antonarakis, Xiang-Jiao Yang, Jacques Côté, and Philippe M. Campeau. De novo kat5 variants cause a syndrome with recognizable facial dysmorphisms, cerebellar atrophy, sleep disturbance, and epilepsy. The American Journal of Human Genetics, 107:564-574, Sep 2020. URL: https://doi.org/10.1016/j.ajhg.2020.08.002, doi:10.1016/j.ajhg.2020.08.002. This article has 52 citations.

3. (humbert2020denovokat5 pages 1-2): Jonathan Humbert, Smrithi Salian, Periklis Makrythanasis, Gabrielle Lemire, Justine Rousseau, Sophie Ehresmann, Thomas Garcia, Rami Alasiri, Armand Bottani, Sylviane Hanquinet, Erin Beaver, Jennifer Heeley, Ann C.M. Smith, Seth I. Berger, Stylianos E. Antonarakis, Xiang-Jiao Yang, Jacques Côté, and Philippe M. Campeau. De novo kat5 variants cause a syndrome with recognizable facial dysmorphisms, cerebellar atrophy, sleep disturbance, and epilepsy. The American Journal of Human Genetics, 107:564-574, Sep 2020. URL: https://doi.org/10.1016/j.ajhg.2020.08.002, doi:10.1016/j.ajhg.2020.08.002. This article has 52 citations.

4. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies, sleep disturbance, and brain abnormalities): Open Targets Query (Neurodevelopmental disorder with dysmorphic facies, sleep disturbance, and brain abnormalities, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (humbert2020denovokat5 pages 3-6): Jonathan Humbert, Smrithi Salian, Periklis Makrythanasis, Gabrielle Lemire, Justine Rousseau, Sophie Ehresmann, Thomas Garcia, Rami Alasiri, Armand Bottani, Sylviane Hanquinet, Erin Beaver, Jennifer Heeley, Ann C.M. Smith, Seth I. Berger, Stylianos E. Antonarakis, Xiang-Jiao Yang, Jacques Côté, and Philippe M. Campeau. De novo kat5 variants cause a syndrome with recognizable facial dysmorphisms, cerebellar atrophy, sleep disturbance, and epilepsy. The American Journal of Human Genetics, 107:564-574, Sep 2020. URL: https://doi.org/10.1016/j.ajhg.2020.08.002, doi:10.1016/j.ajhg.2020.08.002. This article has 52 citations.

6. (humbert2020denovokat5 pages 2-3): Jonathan Humbert, Smrithi Salian, Periklis Makrythanasis, Gabrielle Lemire, Justine Rousseau, Sophie Ehresmann, Thomas Garcia, Rami Alasiri, Armand Bottani, Sylviane Hanquinet, Erin Beaver, Jennifer Heeley, Ann C.M. Smith, Seth I. Berger, Stylianos E. Antonarakis, Xiang-Jiao Yang, Jacques Côté, and Philippe M. Campeau. De novo kat5 variants cause a syndrome with recognizable facial dysmorphisms, cerebellar atrophy, sleep disturbance, and epilepsy. The American Journal of Human Genetics, 107:564-574, Sep 2020. URL: https://doi.org/10.1016/j.ajhg.2020.08.002, doi:10.1016/j.ajhg.2020.08.002. This article has 52 citations.

7. (humbert2020denovokat5 pages 8-9): Jonathan Humbert, Smrithi Salian, Periklis Makrythanasis, Gabrielle Lemire, Justine Rousseau, Sophie Ehresmann, Thomas Garcia, Rami Alasiri, Armand Bottani, Sylviane Hanquinet, Erin Beaver, Jennifer Heeley, Ann C.M. Smith, Seth I. Berger, Stylianos E. Antonarakis, Xiang-Jiao Yang, Jacques Côté, and Philippe M. Campeau. De novo kat5 variants cause a syndrome with recognizable facial dysmorphisms, cerebellar atrophy, sleep disturbance, and epilepsy. The American Journal of Human Genetics, 107:564-574, Sep 2020. URL: https://doi.org/10.1016/j.ajhg.2020.08.002, doi:10.1016/j.ajhg.2020.08.002. This article has 52 citations.

8. (humbert2020denovokat5 pages 9-10): Jonathan Humbert, Smrithi Salian, Periklis Makrythanasis, Gabrielle Lemire, Justine Rousseau, Sophie Ehresmann, Thomas Garcia, Rami Alasiri, Armand Bottani, Sylviane Hanquinet, Erin Beaver, Jennifer Heeley, Ann C.M. Smith, Seth I. Berger, Stylianos E. Antonarakis, Xiang-Jiao Yang, Jacques Côté, and Philippe M. Campeau. De novo kat5 variants cause a syndrome with recognizable facial dysmorphisms, cerebellar atrophy, sleep disturbance, and epilepsy. The American Journal of Human Genetics, 107:564-574, Sep 2020. URL: https://doi.org/10.1016/j.ajhg.2020.08.002, doi:10.1016/j.ajhg.2020.08.002. This article has 52 citations.

9. (bukowskaolech2024chromatinopathiesinsightin pages 3-4): Ewelina Bukowska-Olech, Aleksandra Majchrzak-Celińska, Marta Przyborska, and Aleksander Jamsheer. Chromatinopathies: insight in clinical aspects and underlying epigenetic changes. Journal of Applied Genetics, 65:287-301, Jan 2024. URL: https://doi.org/10.1007/s13353-023-00824-1, doi:10.1007/s13353-023-00824-1. This article has 25 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Neurodevelopmental_Disorder_With_Dysmorphic_Facies_Sleep_Disturbance_And_Brain_Abnormalities-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.