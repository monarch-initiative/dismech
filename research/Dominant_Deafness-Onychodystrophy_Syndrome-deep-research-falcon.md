---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-21T21:13:51.070603'
end_time: '2026-08-21T21:23:38.962371'
duration_seconds: 587.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dominant Deafness-Onychodystrophy Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dominant_Deafness-Onychodystrophy_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dominant Deafness-Onychodystrophy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dominant Deafness-Onychodystrophy Syndrome** covering all of the
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
- **Disease Name:** Dominant Deafness-Onychodystrophy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dominant Deafness-Onychodystrophy Syndrome** covering all of the
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


# Dominant Deafness–Onychodystrophy Syndrome (DDOD): Disease-Characteristics Research Report

**Scope.** This report summarizes evidence available through 2024, prioritizing primary human studies and recent mechanistic work. DDOD is exceptionally rare; consequently, many requested fields have no population-level data, standardized criteria, or disease-specific clinical trials. Frequencies from broader **ATP6V1B2-related cohorts** should not be interpreted as frequencies in narrowly defined classic DDOD.

| Domain | Best-supported finding | Suggested ontology terms | Evidence type/strength |
|---|---|---|---|
| Disease identity | Dominant Deafness-Onychodystrophy syndrome (DDOD) is a rare ATP6V1B2-related Mendelian syndrome defined classically by congenital sensorineural deafness with nail and distal digital anomalies; OMIM 124480. | OMIM 124480; dominant deafness-onychodystrophy syndrome | Human primary reports + review-level synthesis; strong for core identity (yuan2014denovomutation pages 1-3, beauregardlacroix2021doorssyndromeand pages 1-2, shaw2020exomereportnovel pages 7-9) |
| Causal gene/variant | The best-supported recurrent pathogenic variant for classic DDOD is heterozygous ATP6V1B2 c.1516C>T, p.Arg506* (also written p.R506* or p.Arg506X). | ATP6V1B2; nonsense variant; germline heterozygous | Human discovery and segregation evidence; strong (yuan2014denovomutation pages 1-3, li2021casereportexome pages 1-2) |
| Inheritance | Inheritance is autosomal dominant; early reports emphasized de novo occurrence, while later pedigrees established vertical transmission in affected parent-child pairs/families. | autosomal dominant inheritance; de novo mutation | Human genetic evidence; strong (yuan2014denovomutation pages 1-3, li2021casereportexome pages 1-2, beauregardlacroix2021doorssyndromeand pages 1-2) |
| Hearing phenotype | Hearing loss is typically congenital, bilateral, sensorineural, and severe/profound in reported classic DDOD cases. | HP:0000407 sensorineural hearing impairment; congenital hearing impairment; bilateral hearing impairment | Human clinical evidence; strong for core phenotype (yuan2014denovomutation pages 1-3, beauregardlacroix2021doorssyndromeand pages 1-2) |
| Nail phenotype | Onychodystrophy is a hallmark, ranging from dystrophic/hypoplastic nails to complete or partial anonychia of fingers and toes. | HP:0001597 abnormality of the nail; HP:0001798 anonychia | Human clinical evidence; strong (yuan2014denovomutation pages 1-3, li2021casereportexome pages 1-2) |
| Skeletal/digital phenotype | Distal digital anomalies commonly include brachydactyly, shortened fifth fingers, and distal/middle phalangeal hypoplasia or aplasia. | HP:0001156 brachydactyly; distal phalangeal aplasia/hypoplasia | Human clinical/radiographic evidence; strong (yuan2014denovomutation pages 1-3, li2021casereportexome pages 1-2) |
| Neurodevelopmental spectrum | Intellectual disability and seizures were initially considered absent from classic DDOD, but newer ATP6V1B2 cohort data support a broader phenotypic spectrum in which some carriers have developmental delay/intellectual disability and/or seizures. | HP:0001249 intellectual disability; HP:0001250 seizures | Human cohort and family evidence; moderate, with spectrum/ascertainment uncertainty (carpentieri2024dominantlyactingvariants pages 6-9, shaw2020exomereportnovel pages 7-9) |
| Differential diagnosis | Major differentials are TBC1D24-related DOORS syndrome and ATP6V1B2-related Zimmermann-Laband spectrum; presence of intellectual disability/seizures or gingival hyperplasia can shift classification away from classic DDOD. | DOORS syndrome; Zimmermann-Laband syndrome | Human comparative clinical genetics; moderate-strong (beauregardlacroix2021doorssyndromeand pages 1-2) |
| Molecular function | ATP6V1B2 encodes a V-ATPase V1 subunit involved in organelle proton transport and lysosomal/endolysosomal acidification. | vacuolar ATPase complex; lysosome acidification; autophagy; protein catabolic process in lysosome | Human/mammalian functional evidence; strong (yuan2014denovomutation pages 1-3, qiu2021syndromicdeafnessgene pages 7-9, shaw2020exomereportnovel pages 7-9) |
| Mechanism/pathophysiology | Mechanistic evidence converges on lysosomal/autophagic dysfunction, but directionality remains unsettled across studies: older work linked p.Arg506* to impaired lysosome acidification/hypoacidification, whereas 2024 data on additional dominant ATP6V1B2 variants found increased lysosomal acidity/hyperactive pump behavior with lysosomal storage/autophagy defects. | lysosomal dysfunction; autophagic flux defect; lysosomal storage; apoptosis | Human cells + animal models; moderate, with explicit mechanistic conflict/uncertainty (yuan2014denovomutation pages 1-3, qiu2021syndromicdeafnessgene pages 7-9, carpentieri2024dominantlyactingvariants pages 1-2, carpentieri2024dominantlyactingvariants pages 6-9, carpentieri2024dominantlyactingvariants pages 5-6) |
| Cellular/anatomical involvement | Disease-relevant structures include cochlear/spiral ganglion neurons, auditory nerve, hair cells, nails, and distal phalanges; some studies also implicate hippocampal circuitry in cognitive features. | spiral ganglion neuron; cochlea; nail; phalanx; hippocampus | Human phenotype plus animal mechanistic evidence; moderate (qiu2021syndromicdeafnessgene pages 7-9, zhao2019asubunitof pages 1-2) |
| Diagnostics | Diagnosis is supported by the combination of congenital bilateral SNHL plus nail/digital anomalies, with confirmation by exome or targeted ATP6V1B2 sequencing and segregation testing. Radiographs can document phalangeal defects; audiologic testing is central. | HP:0000407 sensorineural hearing impairment; HP:0001597 abnormality of the nail; molecular genetic testing | Human case-based evidence; moderate-strong (yuan2014denovomutation pages 1-3, beauregardlacroix2021doorssyndromeand pages 1-2, li2021casereportexome pages 1-2) |
| Treatment/management | Management is supportive. Published DDOD cases underwent cochlear implantation; hearing intervention is the main real-world treatment, with additional developmental/neurologic follow-up as needed. No disease-specific approved pharmacotherapy was identified. | cochlear implantation; supportive care; audiologic rehabilitation | Human case reports + animal preclinical suggestion only; moderate for supportive care, weak for disease-modifying therapy (yuan2014denovomutation pages 1-3, qiu2021syndromicdeafnessgene pages 7-9) |
| Epidemiology | Epidemiology is poorly defined; DDOD is ultra-rare and no reliable prevalence or incidence estimates were identified in the retrieved evidence. | rare disease | Evidence gap / disease-level inference; weak-direct (yuan2014denovomutation pages 1-3, beauregardlacroix2021doorssyndromeand pages 1-2) |
| Population genetics | Newly described dominant missense ATP6V1B2 variants in 2024 were reported absent from gnomAD in the cited study; classic p.Arg506* is recurrent but still rare. | absent from gnomAD; rare pathogenic variant | Human genetics evidence; moderate (carpentieri2024dominantlyactingvariants pages 5-6) |
| Model systems | Available models include Atp6v1b2 p.Arg506* mice, cochlear conditional mouse models, zebrafish knockdown, and patient/cell-based assays. Models recapitulate selected auditory, seizure, cognitive, lysosomal, and autophagy phenotypes, but not the full human syndrome consistently. | mouse model; zebrafish model; cellular model | Animal/in vitro evidence; strong for existence of models, moderate for fidelity (rousseau2023theatp6v1b2ddoddoorsassociated pages 1-2, zhao2019asubunitof pages 1-2, rousseau2023theatp6v1b2ddoddoorsassociated pages 10-12) |


*Table: This table condenses the best-supported findings for Dominant Deafness-Onychodystrophy syndrome across human, cellular, and animal evidence. It is useful as a quick reference for core phenotype, causative genetics, mechanism, diagnostics, and current evidence gaps.*

## 1. Disease information

### Definition
Dominant deafness–onychodystrophy syndrome is a rare autosomal-dominant syndromic hearing-loss disorder classically characterized by **congenital severe/profound sensorineural hearing loss**, **onychodystrophy or anonychia**, and distal digital abnormalities such as brachydactyly or phalangeal hypoplasia/aplasia. The molecularly defined disorder is caused most consistently by heterozygous **ATP6V1B2 c.1516C>T (p.Arg506Ter/p.Arg506*)**. The original molecular study described three unrelated Chinese patients with severe congenital sensorineural hearing loss, absent or dystrophic nails, and fifth-finger middle-phalangeal aplasia, without inner-ear malformation or intellectual disability. (yuan2014denovomutation pages 1-3)

### Identifiers and synonyms

- **OMIM/MIM:** **124480**, “Deafness, congenital, and onychodystrophy, autosomal dominant.”
- **Causal-gene OMIM:** ATP6V1B2, **MIM 606939**. (beauregardlacroix2021doorssyndromeand pages 1-2)
- **Common synonyms:** dominant deafness–onychodystrophy syndrome; DDOD; autosomal dominant deafness and onychodystrophy; congenital deafness with onychodystrophy.
- **MONDO:** a stable disease-specific MONDO identifier was not established from the retrieved primary literature; this should be verified directly against the current MONDO release before database ingestion.
- **Orphanet, MeSH, ICD-10/ICD-11:** no disease-specific identifiers were established from the retrieved evidence. Clinically, hearing loss and congenital nail malformations may require component-level coding rather than a dedicated DDOD code.

This synthesis is derived from **aggregated disease-level resources and published case/family reports**, not individual EHR records.

### Important nosologic distinction
Classic DDOD was initially separated from **DOORS syndrome** because affected individuals lacked intellectual disability and seizures. DOORS—deafness, onychodystrophy, osteodystrophy, intellectual disability, and seizures—is commonly caused by biallelic **TBC1D24** variants. Later reports show that ATP6V1B2 p.Arg506* can produce overlapping DDOD/DOORS phenotypes, making the boundary a spectrum rather than an absolute molecular division. (yuan2014denovomutation pages 1-3, beauregardlacroix2021doorssyndromeand pages 1-2)

## 2. Etiology

### Causal factor
The primary cause is a **germline heterozygous pathogenic ATP6V1B2 variant**. The recurrent classic allele is **NM_001693.4:c.1516C>T, p.Arg506***, a nonsense variant truncating the final six amino acids of the B2 subunit of vacuolar H+-ATPase. Early cases arose de novo; subsequent mother–son and father–daughter segregation established genuine autosomal-dominant transmission. (yuan2014denovomutation pages 1-3, li2021casereportexome pages 1-2)

The 2021 WES study analyzed **542 individuals in 166 congenital-hearing-loss families** and identified p.Arg506* in two independent multigenerational DDOD families. This was the first direct demonstration of vertical transmission of classic ATP6V1B2-related DDOD. The same study noted high ATP6V1B2 loss-of-function constraint, reported as pLI 0.99. (li2021casereportexome pages 1-2)

### Genetic risk factors
- A heterozygous pathogenic allele confers high disease risk under an autosomal-dominant model.
- Family history is relevant, although de novo occurrence means a negative history does not exclude DDOD.
- Broader ATP6V1B2-related disease also results from dominant missense variants, often producing Zimmermann–Laband-like or neurodevelopmental phenotypes rather than classic DDOD. Six de novo variants reported in 2024—p.Tyr328His, p.Tyr328Cys, p.Ala332Val, p.Glu374Gln, p.Gln376Lys, and p.Gln376Arg—were absent from gnomAD. (carpentieri2024dominantlyactingvariants pages 6-9, carpentieri2024dominantlyactingvariants pages 5-6)

### Environmental, infectious, and lifestyle risk factors
No environmental toxin, infection, diet, occupation, smoking behavior, sex-specific exposure, or lifestyle factor has been shown to cause DDOD. Ordinary acquired causes of hearing loss may add to disability but are not established etiologic components.

### Protective factors and gene–environment interaction
No protective ATP6V1B2 allele, modifier gene, lifestyle factor, or validated gene–environment interaction has been reported. Avoiding preventable ototoxic/noise injury is prudent hearing conservation, but it does not prevent the congenital syndrome.

## 3. Phenotypes

### Core phenotype

| Manifestation | Type and characteristics | Suggested HPO annotation |
|---|---|---|
| Sensorineural hearing loss | Clinical sign; typically congenital, bilateral, severe/profound; deafness was present in all 20 evaluable ATP6V1B2 subjects in a broader 2024 cohort, although that cohort was not limited to classic DDOD. | **HP:0000407** Sensorineural hearing impairment; congenital/bilateral/severe qualifiers |
| Onychodystrophy/nail hypoplasia | Physical manifestation; congenital and generally stable; ranges from small/dystrophic nails to absent fingernails or toenails. | **HP:0001597** Abnormality of the nail; nail hypoplasia |
| Anonychia | Physical manifestation; complete or digit-specific nail absence. In one family, first- and fifth-fingernails were absent; toenails 1–2 were absent and 3–5 hypoplastic. | **HP:0001798** Anonychia |
| Brachydactyly/short fifth finger | Physical sign; congenital and nonprogressive. | **HP:0001156** Brachydactyly; short fifth finger |
| Phalangeal hypoplasia/aplasia | Radiographic/physical finding, commonly distal or middle phalanges. | Hypoplasia/aplasia of phalanges; absent distal phalanx |
| Intellectual disability/developmental delay | Historically absent in classic DDOD, but variably present across the ATP6V1B2 p.Arg506*/broader disease spectrum. | **HP:0001249** Intellectual disability; global developmental delay |
| Seizures/epilepsy | Not part of the narrow historical definition, but reported in ATP6V1B2-associated overlapping phenotypes. | **HP:0001250** Seizure |
| Gingival enlargement | More characteristic of Zimmermann–Laband-spectrum ATP6V1B2 disease than classic DDOD. | Gingival overgrowth |

The 2024 ATP6V1B2 cohort found nail/skeletal hypoplasia or aplasia in **20/20**, facial features in **18/20 (90%)**, developmental delay/intellectual disability in **8/20 (40%)**, and seizures in **7/20 (35%)**. These statistics demonstrate the expanding **ATP6V1B2 spectrum**, not necessarily classic-DDOD penetrance. (carpentieri2024dominantlyactingvariants pages 6-9, carpentieri2024dominantlyactingvariants pages 5-6)

A separate seven-member family carrying a non-p.Arg506* ATP6V1B2 missense allele had epilepsy in **7/7**, intellectual disability in **4/7**, mild nail findings in **4/7**, postural tremor in **4/7**, and mild gingival enlargement in **3/7**; seizure onset ranged from early childhood to 16 years. This family is better classified as broader ATP6V1B2-related neurodevelopmental disease than archetypal DDOD. (shaw2020exomereportnovel pages 7-9)

### Onset, severity, progression, and quality of life
- **Onset:** hearing and nail/digital abnormalities are congenital; neurologic features, when present, may emerge in childhood.
- **Course:** nail and skeletal malformations are structurally stable. Human evidence is insufficient to decide whether DDOD hearing loss is universally stable or progressive. Mouse models show early hidden hearing loss followed by later threshold loss, but extrapolation to humans is uncertain. (qiu2021syndromicdeafnessgene pages 7-9)
- **Quality of life:** no DDOD-specific EQ-5D, SF-36, PROMIS, language, or participation cohort was identified. Severe congenital deafness can impair language acquisition, education, communication, and social participation. Hand/nail abnormalities are usually less functionally limiting but may affect fine-motor tasks, protection of fingertips, and appearance.

## 4. Genetic and molecular information

### Causal gene
- **Gene:** ATP6V1B2, encoding V-type proton ATPase subunit B2.
- **Variant most specific to classic DDOD:** c.1516C>T, **p.Arg506Ter**.
- **Origin:** germline heterozygous; either de novo or inherited.
- **Class:** nonsense/truncating.
- **Population frequency:** no reliable allele frequency was supplied for p.Arg506* in the retrieved evidence; the allele is exceptionally rare. Several newer dominant missense variants were absent from gnomAD. (carpentieri2024dominantlyactingvariants pages 5-6)

The original paper found the same de novo variant in three unrelated patients and showed conservation of residues 506–511. Structural modeling predicted loss of a Tyr504–Asp507 hydrogen bond. (yuan2014denovomutation pages 1-3)

### Pathogenic classification and mechanism
Published reports describe p.Arg506* as pathogenic. The mechanism should **not** be reduced uncritically to simple haploinsufficiency:

1. ATP6V1B2 is loss-of-function constrained.
2. The truncated protein can be expressed and incorporated sufficiently to perturb complex behavior.
3. Earlier studies showed weakened B2–V1E interaction and impaired lysosome acidification despite retained V-ATPase assembly. (zhao2019asubunitof pages 1-2, yuan2014denovomutation pages 1-3)
4. The 2024 study instead concluded that dominant ATP6V1B2/ATP6V1C1 alleles can produce **gain-of-function/hyperactive proton-pump behavior**, increased lysosomal acidity, abnormal lysosomal morphology, defective autophagic flux, and cholesterol/ceramide storage. (carpentieri2024dominantlyactingvariants pages 1-2, carpentieri2024dominantlyactingvariants pages 6-9, carpentieri2024dominantlyactingvariants pages 5-6)

Thus, the current expert interpretation is **dominant dysregulation of V-ATPase and endolysosomal homeostasis**, with allele- and assay-dependent directionality, rather than a settled universal loss-of-function model.

### Modifier, epigenetic, and chromosomal evidence
No validated modifier genes, methylation signature, histone alteration, recurrent copy-number variant, translocation, inversion, or aneuploidy specific to DDOD has been reported. Additional TJP2 and KIF11 variants occurred in the 2021 families, but causative modification of DDOD severity was not established. (li2021casereportexome pages 1-2)

## 5. Environmental information

DDOD is not infectious and has no demonstrated toxicologic, occupational, dietary, alcohol, smoking, radiation, or pollution cause. No pathogen or zoonotic transmission applies. Environmental hearing hazards can worsen residual auditory function but are nonspecific secondary exposures.

## 6. Mechanism and pathophysiology

### Normal molecular role
V-ATPase is a multisubunit ATP-driven proton pump that acidifies lysosomes, endosomes, and synaptic vesicles. Acidic luminal pH is required for endocytic degradation, lysosomal hydrolase activity, vesicle trafficking, and autophagic turnover. ATP6V1B2 encodes the B2 subunit of the peripheral V1 ATP-hydrolytic sector. (shaw2020exomereportnovel pages 7-9, rousseau2023theatp6v1b2ddoddoorsassociated pages 1-2)

### Proposed causal chain

**Germline dominant ATP6V1B2 variant** → altered B2 structure/subunit interaction and V-ATPase proton transport → abnormal endolysosomal pH and lysosomal organization → impaired autophagic flux and substrate clearance → abnormal mitochondria, apoptosis, and/or altered developmental signaling → injury to auditory neurons/hair-cell circuitry and developmental defects of nails/phalanges → congenital deafness, onychodystrophy, and digital anomalies. In susceptible alleles/individuals, neuronal and synaptic dysfunction may additionally produce intellectual disability, behavioral abnormalities, and seizures. (zhao2019asubunitof pages 1-2, qiu2021syndromicdeafnessgene pages 7-9, carpentieri2024dominantlyactingvariants pages 1-2)

### Auditory mechanism
In p.Arg506* mice, auditory-pathway abnormalities included auditory-nerve demyelination, subsequent fiber and spiral-ganglion-neuron loss, increased cleaved caspase-3, reduced Bcl-2, accumulated autolysosomes, and abnormal mitochondria. Hair cells upregulated **Atp6v1b1**, suggesting partial genetic compensation. This may explain why some mouse models have milder auditory disease than humans. (qiu2021syndromicdeafnessgene pages 7-9)

### Neurologic mechanism
Mouse studies implicate hippocampal CA1 dysfunction and altered brain connectivity in cognitive/behavioral findings. The 2023 heterozygous p.Arg506* model showed interictal epileptic activity and increased seizure susceptibility, supporting a direct neuronal consequence of the allele. (zhao2019asubunitof pages 1-2, rousseau2023theatp6v1b2ddoddoorsassociated pages 10-12)

### Suggested ontology annotations
- **GO biological processes:** lysosomal acidification; proton transmembrane transport; autophagy; autophagosome–lysosome fusion; lysosomal substrate catabolism; regulation of neuron apoptotic process; auditory receptor-cell development.
- **GO cellular components:** V-type ATPase complex; lysosomal membrane; endosome; synaptic vesicle; autophagosome; mitochondrion.
- **Cell Ontology terms:** cochlear inner/outer hair cell; spiral ganglion neuron; auditory neuron; Schwann cell; nail matrix keratinocyte; osteoblast/chondrocyte. The latter nail/skeletal cell assignments are biologically plausible but not directly demonstrated in DDOD-specific single-cell experiments.

### Metabolism, immunity, and molecular profiling
Cholesterol and ceramide accumulation in patient-derived cells provides limited lipid-storage evidence. No disease-specific systemic metabolomic signature, immune mechanism, chronic inflammation, autoimmunity, transcriptomic atlas, proteomic biomarker, single-cell dataset, spatial transcriptomic study, or integrated multi-omics analysis was identified through 2024. (carpentieri2024dominantlyactingvariants pages 6-9, carpentieri2024dominantlyactingvariants pages 5-6)

## 7. Anatomical structures affected

### Primary structures
- **Inner ear/auditory system:** cochlea, organ of Corti/hair-cell circuitry, spiral ganglion, auditory nerve; hearing loss is typically bilateral.
- **Nail apparatus:** fingernails and toenails, including nail plate/matrix.
- **Appendicular skeleton:** distal and sometimes middle phalanges, especially fifth fingers.

### Secondary/variable structures
The central nervous system, particularly hippocampal and seizure-generating networks, may be involved in the broader ATP6V1B2 spectrum. Gingiva and craniofacial structures are more prominent in Zimmermann–Laband-like phenotypes. (carpentieri2024dominantlyactingvariants pages 6-9, shaw2020exomereportnovel pages 7-9, zhao2019asubunitof pages 1-2)

### Suggested anatomical ontology terms
- **UBERON:** cochlea; organ of Corti; spiral ganglion; auditory nerve; nail; distal phalanx; middle phalanx; hippocampus.
- **GO cellular components:** lysosome, endosome, autophagosome, synaptic vesicle, V-type ATPase complex.
- **Lateralization:** hearing loss is generally bilateral; nail/digital involvement may be symmetric but varies by digit.

## 8. Temporal development

DDOD begins during embryonic/fetal development. Hearing impairment and nail/digital abnormalities are apparent at birth or recognized in infancy. It is a lifelong chronic disorder rather than an episodic disease. There is no validated staging system.

The critical clinical period is early infancy and childhood, when delayed identification of profound hearing loss can compromise language development. Newborn hearing detection, rapid diagnostic audiology, and early auditory rehabilitation therefore represent the major actionable window. Neurologic surveillance should continue through childhood because seizures or developmental problems may emerge beyond the neonatal period in broader ATP6V1B2 disease. Human longitudinal natural-history data remain insufficient to quantify progression.

## 9. Inheritance and population

### Inheritance
- **Mode:** autosomal dominant.
- **Recurrence:** an affected heterozygous individual theoretically has a 50% probability of transmitting the variant in each pregnancy.
- **De novo disease:** common in initial reports; parental testing is important.
- **Penetrance:** apparently high for hearing/nail manifestations in classic reported families, but exact penetrance is unknown.
- **Expressivity:** variable, especially for intellectual disability, epilepsy, gingival abnormalities, and skeletal severity. p.Arg506* can produce DDOD or overlapping DOORS-like disease. (beauregardlacroix2021doorssyndromeand pages 1-2, rousseau2023theatp6v1b2ddoddoorsassociated pages 10-12)
- **Anticipation:** not reported.
- **Founder effect:** not demonstrated.
- **Consanguinity:** not relevant to the dominant mechanism, although relevant to recessive TBC1D24-DOORS differential diagnosis.
- **Germline mosaicism:** not documented, but a low residual recurrence risk after an apparently de novo variant is standard counseling practice.

### Epidemiology
No reliable prevalence, incidence, carrier frequency, sex ratio, ethnic enrichment, or geographic distribution estimate exists. Published patients include Chinese, European, and other ancestries; this supports worldwide potential rather than a defined endemic population. The small number of reports is consistent with **ultra-rarity**, but publication counts cannot be converted into prevalence.

## 10. Diagnostics

### Clinical assessment
1. **Audiology:** newborn hearing screening followed by diagnostic auditory brainstem response, otoacoustic emissions, tympanometry, and age-appropriate pure-tone/speech audiometry.
2. **Physical examination:** document each nail, digit length, distal phalanges, gingiva, craniofacial features, growth, and neurologic development.
3. **Radiography:** hand/foot radiographs can establish distal or middle phalangeal hypoplasia/aplasia.
4. **Neurologic evaluation:** developmental testing and EEG when seizures, regression, or suspicious episodes occur.
5. **Imaging:** temporal-bone CT/MRI is useful for cochlear-implant planning and excluding structural causes; the original DDOD cases had no inner-ear malformation. (yuan2014denovomutation pages 1-3)

### Molecular testing
A practical strategy is:

- A comprehensive **syndromic hearing-loss panel** including ATP6V1B2 and TBC1D24, with copy-number analysis where validated.
- Targeted ATP6V1B2 sequencing when the phenotype is highly characteristic.
- Trio WES/WGS when panel testing is negative or the phenotype includes epilepsy, intellectual disability, gingival enlargement, or atypical skeletal findings.
- Confirm candidate variants and familial segregation by Sanger sequencing or equivalent orthogonal testing.

WES successfully identified p.Arg506* and segregating alleles in two families. WGS may detect noncoding or structural causes but has no demonstrated DDOD-specific incremental yield. CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not first-line for a classic phenotype unless additional findings suggest another disorder. (li2021casereportexome pages 1-2, beauregardlacroix2021doorssyndromeand pages 1-2)

### Differential diagnosis

- **TBC1D24-related DOORS:** usually autosomal recessive; profound deafness, nail/phalangeal abnormalities, osteodystrophy, intellectual disability, and seizures.
- **ATP6V1B2-related Zimmermann–Laband syndrome:** gingival enlargement, bulbous/soft distal digits, hypoplastic nails/distal phalanges, characteristic face, and variable intellectual disability/epilepsy.
- **ATP6V1B2-associated DDOD/DOORS overlap:** molecularly and clinically continuous with classic DDOD.
- **Coffin–Siris syndrome:** hypoplastic/absent fifth fingernails/distal phalanges plus developmental disability, but a different chromatin-remodeling etiology.
- Other syndromic deafness/nail disorders and acquired congenital hearing-loss causes should be considered according to examination and family history.

No consensus society diagnostic criteria, biochemical enzyme assay, circulating biomarker, biopsy signature, or validated omics diagnostic exists.

## 11. Outcome and prognosis

There are no 5- or 10-year survival estimates, disease-specific mortality rates, or formal prognostic models. Classic DDOD is not known to shorten life expectancy. A reported ATP6V1B2 p.Arg506* patient with a broader DOORS-like presentation lived to 72 years, showing that long survival is possible, although a single case cannot define prognosis. (beauregardlacroix2021doorssyndromeand pages 1-2)

The principal morbidity is lifelong auditory disability and its effect on spoken-language development. Nail and phalangeal abnormalities are permanent. Prognosis for communication depends on severity, age at intervention, auditory-nerve integrity, developmental status, rehabilitation, and access to sign/spoken-language support. Neurologic prognosis is more variable in individuals with epilepsy or intellectual disability. No validated prognostic biomarker is available.

## 12. Treatment

### Current real-world management
There is no approved disease-modifying therapy. Care is multidisciplinary and supportive:

- **Hearing aids** where usable residual hearing exists.
- **Cochlear implantation** for severe/profound bilateral sensorineural loss after standard candidacy evaluation. The original three probands underwent unilateral implantation between ages 2 and 18 years. (yuan2014denovomutation pages 1-3)
- **Auditory-verbal, speech-language, educational, and sign-language support**, individualized to family goals and developmental profile.
- **Nail/hand care:** protection from trauma, dermatology/podiatry management, occupational therapy if fine-motor limitations occur.
- **Seizure treatment:** standard antiseizure therapy based on seizure type; no ATP6V1B2-specific pharmacogenomic recommendation exists.
- **Developmental services:** early intervention, neuropsychological assessment, and school accommodations.

Suggested NCIT concepts include **Cochlear Implantation**, **Hearing Aid**, **Speech and Language Therapy**, **Occupational Therapy**, **Genetic Counseling**, and **Supportive Care**.

### Treatment outcomes and limitations
Cochlear implants are functional in reported DDOD patients, but one study noted unsatisfactory language rehabilitation despite functioning devices, raising concern for unrecognized cognitive or central auditory involvement. This is case-based evidence, not a response-rate estimate. (zhao2019asubunitof pages 1-2)

### Experimental treatments
In mice, the apoptosis inhibitor **BIP-V5** improved auditory phenotypic/pathologic outcomes in only two treated mutant animals; this is exploratory preclinical evidence and not a clinical recommendation. (qiu2021syndromicdeafnessgene pages 7-9)

The 2023 p.Arg506* mouse is proposed for drug screening, but no DDOD-specific human interventional trial was identified. No validated gene therapy, CRISPR therapy, antisense oligonucleotide, RNA therapy, cell therapy, or immune therapy had entered clinical use through 2024. (rousseau2023theatp6v1b2ddoddoorsassociated pages 1-2, rousseau2023theatp6v1b2ddoddoorsassociated pages 10-12)

## 13. Prevention

### Primary prevention
The phenotype cannot be prevented through vaccination, diet, or lifestyle modification. Reproductive options after molecular diagnosis include genetic counseling, prenatal diagnosis, and preimplantation genetic testing where legally and ethically available.

### Secondary prevention/early detection
- Universal newborn hearing screening.
- Prompt diagnostic audiology after failed screening.
- Cascade testing of first-degree relatives once a familial ATP6V1B2 variant is known.
- Developmental and seizure surveillance in variant-positive children.

### Tertiary prevention
Early hearing intervention, communication access, educational support, hearing conservation, avoidance of unnecessary ototoxic exposure, and prompt epilepsy treatment can reduce secondary disability. There is no vaccine, chemoprophylaxis, or population carrier-screening recommendation specific to DDOD.

## 14. Other species and natural disease

No naturally occurring veterinary DDOD equivalent was identified in companion animals, livestock, or wildlife, and there is no zoonotic potential. ATP6V1B2 function is evolutionarily conserved, as illustrated by conservation of the human protein’s terminal residues and phenotypes after experimental perturbation in mouse and zebrafish. (yuan2014denovomutation pages 1-3, zhao2019asubunitof pages 1-2)

Relevant experimental taxa are **Mus musculus** (NCBI Taxonomy 10090) and **Danio rerio** (7955). Breed-specific VBO annotations are not applicable to the reported engineered models.

## 15. Model organisms and research systems

### Mouse
- **Atp6v1b2 p.Arg506* knock-in/transgenic models:** reproduce selected cognitive, auditory, behavioral, and seizure phenotypes.
- The 2023 heterozygous model—genetically analogous to patients—showed locomotor hyperactivity, reduced anxiety-associated behavior, interictal epileptic activity, and reduced pentylenetetrazol seizure threshold. Homozygotes were also viable in this engineered context and showed stronger abnormalities. (rousseau2023theatp6v1b2ddoddoorsassociated pages 10-12, rousseau2023theatp6v1b2ddoddoorsassociated pages 1-2)
- An auditory model showed hidden hearing loss early and later-onset threshold loss, with spiral-ganglion degeneration and autophagy/apoptosis abnormalities. (qiu2021syndromicdeafnessgene pages 7-9)
- A prior knock-in study found cognitive abnormalities but normal hearing/cochlear morphology, illustrating model- and protocol-dependent phenotypic fidelity. (zhao2019asubunitof pages 1-2)
- Complete loss of Atp6v1b2 is embryonically lethal, emphasizing that null models and human terminal truncation are not equivalent. (rousseau2023theatp6v1b2ddoddoorsassociated pages 1-2)

### Zebrafish
Atp6v1b2 knockdown produced multisystem developmental abnormalities and has been used to investigate developmental and neurologic consequences. Its limitations include transient knockdown, species differences in auditory anatomy, and imperfect modeling of heterozygous p.Arg506*. (zhao2019asubunitof pages 1-2)

### Cellular systems
Patient fibroblasts and transfected mammalian cells have been used to measure lysosomal pH, V-ATPase-subunit interaction, lysosomal morphology/localization, autophagic flux, and cholesterol/ceramide storage. These systems are mechanistically informative but do not reproduce cochlear architecture, nail development, or organism-level neurodevelopment. (carpentieri2024dominantlyactingvariants pages 1-2, carpentieri2024dominantlyactingvariants pages 6-9, carpentieri2024dominantlyactingvariants pages 5-6)

### Advanced-technology gap
No DDOD-specific organoid, iPSC-derived cochlear model, single-cell or spatial transcriptomic atlas, CRISPR screen, comprehensive proteome/metabolome/lipidome, or integrated multi-omics study was identified through 2024. The principal current platforms remain engineered mice, zebrafish perturbation, and patient-derived fibroblasts.

## Key recent developments and expert interpretation

1. **2023:** heterozygous p.Arg506* mice established that one mutant allele is sufficient to increase seizure susceptibility, strengthening the biological basis for epilepsy within the ATP6V1B2 spectrum. The abstract states that “both heterozygous (like patients) and homozygous mice have reduced seizure thresholds to pentylenetetrazol.” (rousseau2023theatp6v1b2ddoddoorsassociated pages 10-12, rousseau2023theatp6v1b2ddoddoorsassociated pages 1-2)
2. **2024:** a 20-person ATP6V1B2 series quantified broad phenotypic variability and connected dominant ATP6V1B2/ATP6V1C1 variants to altered lysosome morphology, increased acidity, defective autophagic flux, and lipid storage. This supports classifying these conditions as disorders of lysosomal homeostasis. (carpentieri2024dominantlyactingvariants pages 1-2, carpentieri2024dominantlyactingvariants pages 6-9, carpentieri2024dominantlyactingvariants pages 5-6)
3. **Current expert synthesis:** p.Arg506* remains the allele most strongly linked to classic DDOD, but DDOD, ATP6V1B2-related DOORS, and Zimmermann–Laband presentations overlap. Classification should therefore record both the named phenotype and the broader **ATP6V1B2-related disorder** umbrella, with patient-level annotations for hearing, nails/phalanges, neurodevelopment, seizures, and gingiva. (beauregardlacroix2021doorssyndromeand pages 1-2)

## Principal evidence gaps

Reliable prevalence, penetrance, longitudinal hearing trajectories, cochlear-implant response rates, quality-of-life measurements, genotype-specific prognosis, modifier genes, epigenetic signatures, validated biomarkers, treatment guidelines, and disease-modifying clinical trials are unavailable. The most important research needs are a multinational natural-history registry, standardized audiologic/developmental outcomes, allele-resolved functional studies, cochlear/nail-relevant human cell models, and prospective evaluation of auditory intervention.

References

1. (yuan2014denovomutation pages 1-3): Yongyi Yuan, Jianguo Zhang, Qing Chang, Jin Zeng, Feng Xin, Jianjun Wang, Qingyan Zhu, Jing Wu, Jingqiao Lu, Weiwei Guo, Xukun Yan, Hui Jiang, Binfei Zhou, Qi Li, Xue Gao, Huijun Yuan, Shiming Yang, Dongyi Han, Zixu Mao, Ping Chen, Xi Lin, and Pu Dai. De novo mutation in atp6v1b2 impairs lysosome acidification and causes dominant deafness-onychodystrophy syndrome. Cell Research, 24:1370-1373, Jun 2014. URL: https://doi.org/10.1038/cr.2014.77, doi:10.1038/cr.2014.77. This article has 103 citations and is from a domain leading peer-reviewed journal.

2. (beauregardlacroix2021doorssyndromeand pages 1-2): Eliane Beauregard-Lacroix, Guillermo Pacheco-Cuellar, Norbert F. Ajeawung, Jessica Tardif, Klaus Dieterich, Tabib Dabir, Dina Vind-Kezunovic, Susan M. White, Denes Zadori, Claudia Castiglioni, Lisbeth Tranebjærg, Pernille Mathiesen Tørring, Ed Blair, Marzena Wisniewska, Maria Vittoria Camurri, Yolande van Bever, Sirinart Molidperee, Juliet Taylor, Alexandre Dionne-Laporte, Sanjay M. Sisodiya, Raoul C.M. Hennekam, and Philippe M. Campeau. Doors syndrome and a recurrent truncating atp6v1b2 variant. Genetics in Medicine, 23:149-154, Jan 2021. URL: https://doi.org/10.1038/s41436-020-00950-9, doi:10.1038/s41436-020-00950-9. This article has 40 citations and is from a highest quality peer-reviewed journal.

3. (shaw2020exomereportnovel pages 7-9): Marie Shaw, Anna Winczewska-Wiktor, Magdalena Badura-Stronka, Sunita Koirala, Alison Gardner, Łukasz Kuszel, Piotr Kowal, Barbara Steinborn, Monika Starczewska, Sarah Garry, Ingrid E. Scheffer, Samuel F. Berkovic, and Jozef Gecz. Exome report: novel mutation in atp6v1b2 segregating with autosomal dominant epilepsy, intellectual disability and mild gingival and nail abnormalities. European journal of medical genetics, 63:103799, Apr 2020. URL: https://doi.org/10.1016/j.ejmg.2019.103799, doi:10.1016/j.ejmg.2019.103799. This article has 26 citations and is from a peer-reviewed journal.

4. (li2021casereportexome pages 1-2): Yuan Li, Jianjun Xiong, Yi Zhang, Lin Xu, Jianyun Liu, and Tao Cai. Case report: exome sequencing identified variants in three candidate genes from two families with hearing loss, onychodystrophy, and epilepsy. Frontiers in Genetics, Nov 2021. URL: https://doi.org/10.3389/fgene.2021.728020, doi:10.3389/fgene.2021.728020. This article has 13 citations and is from a peer-reviewed journal.

5. (carpentieri2024dominantlyactingvariants pages 6-9): Giovanna Carpentieri, Serena Cecchetti, Gianfranco Bocchinfuso, Francesca Clementina Radio, Chiara Leoni, Roberta Onesimo, Paolo Calligari, Agostina Pietrantoni, Andrea Ciolfi, Marco Ferilli, Cristina Calderan, Gerarda Cappuccio, Simone Martinelli, Elena Messina, Viviana Caputo, Ulrike Hüffmeier, Cyril Mignot, Stéphane Auvin, Yline Capri, Charles Marques Lourenco, Bianca E. Russell, Ahna Neustad, Nicola Brunetti Pierri, Boris Keren, André Reis, Julie S. Cohen, Alexis Heidlebaugh, Clay Smith, Christian T. Thiel, Leonardo Salviati, Giuseppe Zampino, Philippe M. Campeau, Lorenzo Stella, Marco Tartaglia, and Elisabetta Flex. Dominantly acting variants in atp6v1c1 and atp6v1b2 cause a multisystem phenotypic spectrum by altering lysosomal and/or autophagosome function. Oct 2024. URL: https://doi.org/10.1016/j.xhgg.2024.100349, doi:10.1016/j.xhgg.2024.100349. This article has 14 citations and is from a peer-reviewed journal.

6. (qiu2021syndromicdeafnessgene pages 7-9): Shiwei Qiu, Weihao Zhao, Xue Gao, Dapeng Li, Weiqian Wang, Bo Gao, Weiju Han, Shiming Yang, Pu Dai, Peng Cao, and Yongyi Yuan. Syndromic deafness gene atp6v1b2 controls degeneration of spiral ganglion neurons through modulating proton flux. Frontiers in Cell and Developmental Biology, Oct 2021. URL: https://doi.org/10.3389/fcell.2021.742714, doi:10.3389/fcell.2021.742714. This article has 17 citations.

7. (carpentieri2024dominantlyactingvariants pages 1-2): Giovanna Carpentieri, Serena Cecchetti, Gianfranco Bocchinfuso, Francesca Clementina Radio, Chiara Leoni, Roberta Onesimo, Paolo Calligari, Agostina Pietrantoni, Andrea Ciolfi, Marco Ferilli, Cristina Calderan, Gerarda Cappuccio, Simone Martinelli, Elena Messina, Viviana Caputo, Ulrike Hüffmeier, Cyril Mignot, Stéphane Auvin, Yline Capri, Charles Marques Lourenco, Bianca E. Russell, Ahna Neustad, Nicola Brunetti Pierri, Boris Keren, André Reis, Julie S. Cohen, Alexis Heidlebaugh, Clay Smith, Christian T. Thiel, Leonardo Salviati, Giuseppe Zampino, Philippe M. Campeau, Lorenzo Stella, Marco Tartaglia, and Elisabetta Flex. Dominantly acting variants in atp6v1c1 and atp6v1b2 cause a multisystem phenotypic spectrum by altering lysosomal and/or autophagosome function. Oct 2024. URL: https://doi.org/10.1016/j.xhgg.2024.100349, doi:10.1016/j.xhgg.2024.100349. This article has 14 citations and is from a peer-reviewed journal.

8. (carpentieri2024dominantlyactingvariants pages 5-6): Giovanna Carpentieri, Serena Cecchetti, Gianfranco Bocchinfuso, Francesca Clementina Radio, Chiara Leoni, Roberta Onesimo, Paolo Calligari, Agostina Pietrantoni, Andrea Ciolfi, Marco Ferilli, Cristina Calderan, Gerarda Cappuccio, Simone Martinelli, Elena Messina, Viviana Caputo, Ulrike Hüffmeier, Cyril Mignot, Stéphane Auvin, Yline Capri, Charles Marques Lourenco, Bianca E. Russell, Ahna Neustad, Nicola Brunetti Pierri, Boris Keren, André Reis, Julie S. Cohen, Alexis Heidlebaugh, Clay Smith, Christian T. Thiel, Leonardo Salviati, Giuseppe Zampino, Philippe M. Campeau, Lorenzo Stella, Marco Tartaglia, and Elisabetta Flex. Dominantly acting variants in atp6v1c1 and atp6v1b2 cause a multisystem phenotypic spectrum by altering lysosomal and/or autophagosome function. Oct 2024. URL: https://doi.org/10.1016/j.xhgg.2024.100349, doi:10.1016/j.xhgg.2024.100349. This article has 14 citations and is from a peer-reviewed journal.

9. (zhao2019asubunitof pages 1-2): Weihao Zhao, Xue Gao, Shiwei Qiu, Bo Gao, Song Gao, Xin Zhang, Dongyang Kang, Weiju Han, Pu Dai, and Yongyi Yuan. A subunit of v-atpases, atp6v1b2, underlies the pathology of intellectual disability. EBioMedicine, 45:408-421, Jul 2019. URL: https://doi.org/10.1016/j.ebiom.2019.06.035, doi:10.1016/j.ebiom.2019.06.035. This article has 44 citations and is from a peer-reviewed journal.

10. (rousseau2023theatp6v1b2ddoddoorsassociated pages 1-2): Justine Rousseau, Samuel Boris Tene Tadoum, Marisol Lavertu Jolin, Thi Tuyet Mai Nguyen, Norbert Fonya Ajeawung, Ann M. Flenniken, Lauryl M. J. Nutter, Igor Vukobradovic, Elsa Rossignol, and Philippe M. Campeau. The atp6v1b2 ddod/doors-associated p.arg506* variant causes hyperactivity and seizures in mice. Genes, 14:1538, Jul 2023. URL: https://doi.org/10.3390/genes14081538, doi:10.3390/genes14081538. This article has 7 citations.

11. (rousseau2023theatp6v1b2ddoddoorsassociated pages 10-12): Justine Rousseau, Samuel Boris Tene Tadoum, Marisol Lavertu Jolin, Thi Tuyet Mai Nguyen, Norbert Fonya Ajeawung, Ann M. Flenniken, Lauryl M. J. Nutter, Igor Vukobradovic, Elsa Rossignol, and Philippe M. Campeau. The atp6v1b2 ddod/doors-associated p.arg506* variant causes hyperactivity and seizures in mice. Genes, 14:1538, Jul 2023. URL: https://doi.org/10.3390/genes14081538, doi:10.3390/genes14081538. This article has 7 citations.

## Artifacts

- [Edison artifact artifact-00](Dominant_Deafness-Onychodystrophy_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.