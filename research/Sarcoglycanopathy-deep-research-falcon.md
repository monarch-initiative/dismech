---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T16:33:22.315991'
end_time: '2026-08-26T16:43:19.954358'
duration_seconds: 597.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sarcoglycanopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Sarcoglycanopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sarcoglycanopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sarcoglycanopathy** covering all of the
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
- **Disease Name:** Sarcoglycanopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sarcoglycanopathy** covering all of the
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


# Sarcoglycanopathy: comprehensive disease-characteristics report

## Executive summary

Sarcoglycanopathy is a collective term for four autosomal-recessive muscular dystrophies caused by biallelic pathogenic variants in **SGCA, SGCB, SGCG,** or **SGCD**. Their products—α-, β-, γ-, and δ-sarcoglycan—form a transmembrane subcomplex of the dystrophin-associated protein complex (DAPC). Loss of one component commonly destabilizes the others, weakening the sarcolemma during contraction and initiating myofiber injury, inflammation, fibrosis, and fatty replacement. Clinical severity ranges from asymptomatic hyperCKemia or adult-onset limb-girdle weakness to a Duchenne-like childhood disorder with loss of walking in adolescence, respiratory failure, and dilated cardiomyopathy. Cognitive impairment is not characteristic. (barba2023modelingsarcoglycanopathyin pages 1-2, guimaraescosta2021clinicalcorrelationsand pages 1-3)

The most important recent clinical development is systemic **SGCB** replacement with bidridistrogene xeboparvovec. In a six-patient phase 1/2 study published January 4, 2024, mean β-sarcoglycan expression reached 36.2% and 62.1% of normal at day 60 in low- and high-dose cohorts, respectively, with preliminary motor improvements maintained through two years. The study was small, open-label, and nonrandomized, so efficacy remains provisional. (mendell2024genetherapywith pages 1-2, mendell2024genetherapywith pages 7-8)

| Current subtype / legacy name | Causal gene / protein | Inheritance | Hallmark severity / onset | Cardiac / respiratory notes | Key evidence / statistics |
|---|---|---|---|---|---|
| LGMDR3 / LGMD2D | **SGCA** / α-sarcoglycan | Autosomal recessive | In the 100-patient sarcoglycanopathy cohort, α-SG cases had later mean onset than γ-SG: **8.0 years**; phenotype is variable from severe childhood-onset to milder late-onset forms. Earlier onset predicts earlier loss of ambulation. (guimaraescosta2021clinicalcorrelationsand pages 1-3) | Dilated cardiomyopathy can occur across all sarcoglycanopathy subtypes; heart and respiratory surveillance are recommended. (guimaraescosta2021clinicalcorrelationsand pages 1-3, barba2023modelingsarcoglycanopathyin pages 1-2) | α-SG was one of the major subtypes in the 100-patient cohort (**41/100**). In the broader Dutch AR-LGMD/Miyoshi cohort, sarcoglycanopathies represented **67/244 (27%)** of cases. (guimaraescosta2021clinicalcorrelationsand pages 1-3) |
| LGMDR4 / LGMD2E | **SGCB** / β-sarcoglycan | Autosomal recessive | Often severe, but heterogeneous. In one 32-patient series, phenotypes were **15 severe, 12 mild, 5 unknown**; another multicenter cohort reported mean onset around **24.4 years** for β-SG cases represented there, highlighting variability and probable ascertainment effects. (semplicini2015clinicalandgenetic pages 2-3, guimaraescosta2021clinicalcorrelationsand pages 1-3) | Cardiac involvement is prominent: **63%** had cardiac involvement, **19%** dilated cardiomyopathy, **28%** rhythm abnormalities; **19%** required respiratory support. Constant surveillance is emphasized, especially for LGMDR4. (semplicini2015clinicalandgenetic pages 2-3, barba2023modelingsarcoglycanopathyin pages 1-2) | Estimated prevalence reported as **0.86 × 10⁻⁶**. First-in-human SGCB gene therapy trial enrolled **6** patients aged 4–15 years; Day-60 SGCB expression reached **36.2%** and **62.1%** of normal in low/high dose cohorts, respectively. (semplicini2015clinicalandgenetic pages 2-3, mendell2024genetherapywith pages 1-2, NCT03652259 chunk 1) |
| LGMDR5 / LGMD2C | **SGCG** / γ-sarcoglycan | Autosomal recessive | Typically earlier and more severe. In the 100-patient cohort, γ-SG cases had mean onset **5.5 years** and more frequent severe progression with early loss of ambulation. (guimaraescosta2021clinicalcorrelationsand pages 1-3) | Dilated cardiomyopathy occurred in all subtypes and was reported **especially in γ-SG patients**; respiratory problems needing ventilation are common in sarcoglycanopathy overall. (guimaraescosta2021clinicalcorrelationsand pages 1-3, barba2023modelingsarcoglycanopathyin pages 1-2) | In the French multicenter cohort, γ-SG was the largest subgroup (**54/100**); **>90%** carried the homozygous **c.525delT** frameshift variant, indicating a strong founder effect in some populations. (guimaraescosta2021clinicalcorrelationsand pages 1-3) |
| LGMDR6 / LGMD2F | **SGCD** / δ-sarcoglycan | Autosomal recessive | Ultra-rare and generally severe/rapidly progressive. In the largest international cohort, **60%** were wheelchair-bound from early teens with median loss of ambulation at **12.0 years**; distal weakness appeared early in **56.5%**. Absent sarcoglycan expression predicted earlier onset and ambulation loss. (alonsoperez2022clinicalandgenetic pages 1-1, alonsoperez2022clinicalandgenetic pages 2-3) | Cardiac involvement in **21.7%** (5/23); **17.4%** (4/23) required non-invasive ventilation. Surveillance is recommended, especially because cardiomyopathy can occur across sarcoglycanopathies. (alonsoperez2022clinicalandgenetic pages 1-1, barba2023modelingsarcoglycanopathyin pages 1-2) | Largest cohort identified **23** analyzed patients from **18 families** across **9 countries**; **87%** had consanguineous parents, supporting enrichment in consanguineous settings. Geographic concentration has been noted in Brazil. (alonsoperez2022clinicalandgenetic pages 2-3, guimaraescosta2021clinicalcorrelationsand pages 1-3) |


*Table: This table summarizes the four canonical sarcoglycanopathy subtypes for knowledge-base use, linking nomenclature, gene/protein, inheritance, and major clinical distinctions. It highlights the strongest gathered quantitative evidence on onset, severity, and cardio-respiratory burden.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** sarcoglycanopathy; **MONDO:0016140**.
* **MeSH:** *Sarcoglycanopathies*, **D058088**; parent term *Muscular Dystrophies, Limb-Girdle*, D049288. (OpenTargets Search: sarcoglycanopathy, NCT04475926 chunk 2)
* **Orphanet umbrella concept:** qualitative or quantitative defects of sarcoglycan, **ORPHA:207052**. (OpenTargets Search: sarcoglycanopathy)
* **ICD:** ICD-10 does not provide a reliable gene-specific code; coding usually falls under muscular dystrophy (for example G71.0 in ICD-10-CM, depending on jurisdiction). ICD-11 should be recorded under the relevant inherited muscular-dystrophy category, with the molecular subtype represented separately.
* **Canonical subtypes:** LGMDR3 α-sarcoglycan-related (legacy LGMD2D), LGMDR4 β-sarcoglycan-related (LGMD2E), LGMDR5 γ-sarcoglycan-related (LGMD2C), and LGMDR6 δ-sarcoglycan-related (LGMD2F). (barba2023modelingsarcoglycanopathyin pages 1-2)
* **Common synonyms:** sarcoglycan muscular dystrophy, sarcoglycan-deficient muscular dystrophy, autosomal-recessive limb-girdle muscular dystrophy 3–6, α/β/γ/δ-sarcoglycanopathy, and severe childhood autosomal-recessive muscular dystrophy.

This report synthesizes **aggregated disease-level resources and published cohorts**, not individual EHR records. The strongest human datasets include a 100-patient multicenter series and subtype-specific cohorts; therefore, frequencies should not be interpreted as population-screening estimates. (alonsoperez2022clinicalandgenetic pages 1-1, guimaraescosta2021clinicalcorrelationsand pages 1-3)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

The primary cause is **germline biallelic loss of sarcoglycan function**. Approximately 67% of reported causal variants are missense variants, followed by frameshift and null alleles. Null/out-of-frame variants generally produce the greatest disruption of complex biogenesis. Missense proteins may misfold and be prematurely eliminated through endoplasmic-reticulum-associated degradation (ERAD). (barba2023modelingsarcoglycanopathyin pages 1-2)

### Risk factors

* **Genetic:** two pathogenic/likely pathogenic alleles in the same sarcoglycan gene; absent residual protein and onset before age 10 predict severe disease. (alonsoperez2022clinicalandgenetic pages 1-1, alonsoperez2022clinicalandgenetic pages 2-3)
* **Family history/consanguinity:** as expected for recessive disease, consanguinity increases the probability of homozygosity. In the international LGMDR6 cohort, 87% had consanguineous parents. (alonsoperez2022clinicalandgenetic pages 1-1)
* **Founder effects:** more than 90% of γ-sarcoglycan cases in one French/North-African-enriched cohort carried homozygous **SGCG c.525delT**. (guimaraescosta2021clinicalcorrelationsand pages 1-3)
* **Sex:** both sexes are affected; there is no established sex-specific penetrance.
* **Mechanical loading:** contraction is not the genetic cause, but repeated mechanical stress exposes sarcolemmal fragility. In knockout zebrafish, viscous-medium swimming accelerated phenotype appearance, providing experimental evidence of a load–genotype interaction. (barba2023modelingsarcoglycanopathyin pages 1-2)

No validated environmental toxin, infection, diet, smoking exposure, protective allele, or disease-preventing lifestyle factor has been established. Avoiding extreme eccentric or exhaustion exercise is prudent after diagnosis, but ordinary activity is not a cause. Evidence for specific modifier genes, epigenetic protective factors, or reproducible human G×E effects remains insufficient.

## 3. Phenotypes

### Core phenotype and suggested HPO annotations

* **Progressive proximal weakness**—pelvic before or with shoulder-girdle involvement; difficulty running, climbing stairs, rising from the floor, and frequent falls. Suggested terms: **HP:0003324** (generalized muscle weakness), **HP:0008994** (proximal muscle weakness), **HP:0003560** (muscular dystrophy).
* **Axial weakness and contractures** are frequent; suggested **HP:0003701** (proximal muscle weakness), **HP:0001371** (flexion contracture), and **HP:0003306** (spinal rigidity), where applicable. (guimaraescosta2021clinicalcorrelationsand pages 1-3)
* **Calf hypertrophy**, scapular winging, lumbar lordosis, waddling gait, and Gowers sign are common dystrophic manifestations; suggested **HP:0008981**, **HP:0003691**, **HP:0002937**, **HP:0002515**, and **HP:0003391**, respectively.
* **HyperCKemia:** frequently marked and may precede weakness; **HP:0003236**. CK can decline late as muscle mass is lost, so a falling CK is not necessarily improvement.
* **Loss of ambulation:** **HP:0002355**. At mean 22.9-year follow-up, 65.3% of a 100-patient cohort were wheelchair-dependent; six had died. (guimaraescosta2021clinicalcorrelationsand pages 1-3)
* **Respiratory muscle weakness/restrictive ventilatory defect:** **HP:0002747**, **HP:0002093**. Thirty of 100 patients in the multicenter cohort were ventilated. In LGMDR6, 17.4% required non-invasive ventilation. (alonsoperez2022clinicalandgenetic pages 1-1, guimaraescosta2021clinicalcorrelationsand pages 1-3)
* **Dilated cardiomyopathy and rhythm disturbance:** **HP:0001644**, **HP:0011675**, **HP:0010987**. Cardiac disease can occur in every subtype. In a 32-person LGMDR4 cohort, 63% had cardiac involvement, including DCM in 19% and rhythm abnormalities in 28%. (semplicini2015clinicalandgenetic pages 2-3)
* **Distal weakness:** usually secondary but can appear early, particularly in LGMDR6, where it occurred in 56.5%. **HP:0002460**. (alonsoperez2022clinicalandgenetic pages 1-1)
* **Cognition:** intellectual disability is not a characteristic phenotype; the 2023 model review states, “Cognitive impairment has never been reported.” (barba2023modelingsarcoglycanopathyin pages 1-2)

Onset is usually insidious in childhood, but expression is highly variable. In the 100-patient cohort, median/mean reported onset differed substantially: γ-SG 5.5 years, α-SG 8 years, and β-SG 24.4 years. These figures are cohort-dependent and do not imply that β-sarcoglycanopathy is usually benign. (guimaraescosta2021clinicalcorrelationsand pages 1-3)

### Quality of life

Weakness progressively limits mobility, self-care, education/employment, community participation, and independence; ventilation and cardiomyopathy add treatment burden. Disease-specific EQ-5D/SF-36 reference values and per-phenotype utilities are not well established. Current prospective studies instead emphasize NSAD, PUL, timed motor tests, FVC, and wearable mobility measures. (NCT04475926 chunk 1, NCT05876780 chunk 1)

## 4. Genetic and molecular information

| Subtype | Gene/protein | Useful identifiers | Typical molecular consequence |
|---|---|---|---|
| LGMDR3/2D | **SGCA**, α-SG | HGNC:6615; OMIM gene 600119; phenotype 253600 | Usually loss/reduction or mislocalization of α-SG; secondary complex deficiency |
| LGMDR4/2E | **SGCB**, β-SG | HGNC:10806; OMIM gene 600900; phenotype 604286 | Loss of β-SG and destabilization of associated SGs |
| LGMDR5/2C | **SGCG**, γ-SG | HGNC:10809; OMIM gene 608896; phenotype 253700 | Loss of γ-SG; severe founder-associated disease is common in some populations |
| LGMDR6/2F | **SGCD**, δ-SG | HGNC:10807; OMIM gene 601411; phenotype 601287 | Loss/misfolding of δ-SG; skeletal and cardiac membrane dysfunction |

Open Targets independently identifies SGCA, SGCB, SGCG, and SGCD as the four leading sarcoglycanopathy-associated targets. (OpenTargets Search: sarcoglycanopathy)

Variants include missense, nonsense, frameshift, canonical splice, exon-level deletion/duplication, and rarer structural alleles. They are **constitutional germline**, not somatic. Most act through loss of function, abnormal folding/trafficking, ERAD, or failure to assemble the tetramer; gain-of-function and dominant-negative mechanisms are not established as the canonical cause. Variant interpretation should use ACMG/AMP criteria, segregation, population frequency, phenotype, RNA studies where relevant, and muscle protein expression. A VUS alone does not establish diagnosis.

Population allele frequencies must be reported **variant by variant** from the current gnomAD release; no single meaningful frequency applies to a gene. Pathogenic alleles are individually rare, while founder variants can be locally enriched. No recurrent aneuploidy, translocation, anticipation mechanism, or characteristic epigenetic lesion defines the disease. Germline mosaicism is theoretically possible but is not a major documented mechanism.

## 5. Environmental, lifestyle, and infectious information

There is no evidence that sarcoglycanopathy is caused by toxins, radiation, pollution, occupation, diet, alcohol, smoking, or infection. Exercise modifies mechanical demand on vulnerable muscle: individualized low-to-moderate aerobic and submaximal activity is generally favored, whereas unaccustomed high-intensity eccentric exercise may increase injury. Respiratory vaccination, nutrition, and weight management prevent complications rather than the inherited disease itself. The condition is noninfectious and nontransmissible.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic defect:** biallelic SGCA/B/G/D variant.
2. **Protein defect:** absent, unstable, misfolded, or mistargeted sarcoglycan; secondary loss of interacting partners.
3. **Complex failure:** reduced sarcoglycan–sarcospan/DAPC function at the sarcolemma.
4. **Biomechanical injury:** contraction-induced membrane instability and abnormal permeability.
5. **Downstream responses:** ionic dysregulation, myofiber necrosis, damage-associated signaling, immune-cell recruitment, repeated regeneration, oxidative/mitochondrial stress.
6. **Tissue remodeling:** fibrosis and adipose replacement reduce contractile tissue.
7. **Clinical output:** progressive skeletal weakness, respiratory restriction, and—depending on genotype—cardiomyopathy/arrhythmia. (barba2023modelingsarcoglycanopathyin pages 1-2, barba2023modelingsarcoglycanopathyin pages 6-9)

The 2023 primary zebrafish paper states that SGs form a tetramer in the DAPC, which “plays a key role in protecting sarcolemma from stress deriving from muscle contraction.” It also showed that a δ-SG missense protein was an ERAD substrate, supporting misfolding and premature degradation as a distinct upstream mechanism. (barba2023modelingsarcoglycanopathyin pages 1-2)

Adult sgcd-null zebrafish developed disorganized fibers, myofibrillar fragmentation, hypercontracted fibers, inflammatory L-plastin-positive cells, fibrosis, adipose replacement, and progressively abnormal mitochondria. These findings support inflammation, fibrosis, and mitochondrial injury as downstream—not initiating—processes. (barba2023modelingsarcoglycanopathyin pages 6-9)

**Suggested GO terms:** sarcolemma organization (GO:0042383), muscle contraction (GO:0006936), regulation of membrane integrity, protein quality control/ERAD (GO:0036503), inflammatory response (GO:0006954), muscle-cell apoptosis/necrosis, extracellular-matrix organization (GO:0030198), and muscle-organ development (GO:0007517). Suggested cellular components include **sarcolemma (GO:0042383)** and dystrophin-associated glycoprotein complex. Suggested cell types: skeletal-muscle fiber/myocyte (**CL:0000188**), cardiomyocyte (**CL:0000746**), satellite cell (**CL:0000596**), fibroblast (**CL:0000057**), and macrophage (**CL:0000235**).

Disease-specific human single-cell, spatial-transcriptomic, metabolomic, lipidomic, and epigenomic signatures are not yet mature enough for routine knowledge-base assertions. Available molecular profiling is dominated by biopsy protein expression and preclinical histology.

## 7. Anatomical structures affected

* **Primary organ/tissue:** bilateral skeletal muscle, especially pelvic-girdle, thigh, shoulder-girdle, axial, and respiratory muscles. Suggested UBERON: skeletal muscle organ **UBERON:0001630**, diaphragm **UBERON:0001103**, heart **UBERON:0000948**.
* **Secondary/variable:** myocardium and cardiac conduction system; diaphragm/intercostal muscles; tendons and joints through contracture; spine through lordosis/scoliosis.
* **Cellular target:** multinucleated skeletal myofibers and cardiomyocytes; macrophages and fibroblasts participate secondarily.
* **Subcellular localization:** sarcolemma/DAPC; ER and proteasome become relevant for misfolded variants; mitochondria show downstream injury. (barba2023modelingsarcoglycanopathyin pages 6-9, barba2023modelingsarcoglycanopathyin pages 1-2)
* **Lateralization:** usually symmetric; marked unilateral disease is atypical and should prompt reconsideration.

## 8. Temporal development

The disorder is chronic, lifelong, and usually progressive rather than episodic or relapsing. Early disease features running difficulty, Gowers maneuver, stair-climbing difficulty, hyperCKemia, and calf enlargement. Intermediate disease brings contractures, axial/upper-limb weakness, and declining timed function. Advanced disease includes loss of ambulation, restrictive respiratory insufficiency, and possible cardiomyopathy.

Age at onset is the strongest repeatedly observed clinical predictor. In the 100-person study, younger onset independently predicted severity and time to loss of ambulation; absent biopsy protein also predicted earlier loss of walking. (guimaraescosta2021clinicalcorrelationsand pages 1-3) LGMDR6 illustrates the severe end: 60% were wheelchair-bound in the early teens, at median age 12. (alonsoperez2022clinicalandgenetic pages 1-1)

There is no spontaneous remission. The critical therapeutic window is probably before extensive fibrofatty replacement, because gene replacement can restore protein but cannot readily replace lost contractile tissue. This is a biologically strong inference rather than a proven age cutoff.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed carrier parents, each pregnancy has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability. Penetrance of clearly deleterious biallelic genotypes is generally high but may be age-dependent; expressivity is markedly variable. Anticipation is not expected.

Sarcoglycanopathies are ultra-rare, and incidence is not reliably quantified. A β-sarcoglycanopathy series cited an estimated prevalence of **0.86 per million**. In a Dutch clinically ascertained cohort, sarcoglycanopathies constituted 67/244 (27%) of molecularly diagnosed AR-LGMD/Miyoshi cases; this is a diagnostic mix, not population prevalence. (semplicini2015clinicalandgenetic pages 2-3, guimaraescosta2021clinicalcorrelationsand pages 1-3)

Geographic enrichment differs: α-SG is prominent in Europe, γ-SG in North Africa, β-SG occurs worldwide, and reported δ-SG cases have been concentrated in Brazil. These patterns reflect founder alleles, ascertainment, and consanguinity rather than ethnic restriction. (guimaraescosta2021clinicalcorrelationsand pages 1-3) Both sexes are affected approximately equally.

## 10. Diagnostics

### Recommended approach

1. **Clinical suspicion:** symmetric proximal weakness, Gowers sign, calf enlargement, contractures, markedly elevated CK, recessive pedigree, or incidental hyperCKemia.
2. **Baseline laboratory testing:** serum CK, AST/ALT, LDH, aldolase where available; muscle-derived transaminase elevation should not automatically be labeled hepatic disease.
3. **Molecular confirmation:** an NGS neuromuscular/LGMD panel containing **SGCA, SGCB, SGCG, SGCD**, with deletion/duplication analysis. WES or WGS is appropriate if panel testing is negative, the phenotype is atypical, or structural/noncoding variation is suspected. A Dutch study using sequential targeted testing, panels, and WES achieved diagnoses in 57/60 families with available DNA. (guimaraescosta2021clinicalcorrelationsand pages 1-3)
4. **RNA analysis:** useful for uncertain splice variants; muscle RNA may be necessary.
5. **Muscle biopsy:** now usually second-line, but valuable when genetics is unresolved or functional validation is needed. Histology is dystrophic, with necrosis/regeneration and fibrofatty change. Immunohistochemistry or Western blot should assess all four sarcoglycans because secondary deficiency can obscure which gene is primary. Residual expression has prognostic value. (alonsoperez2022clinicalandgenetic pages 1-1, semplicini2015clinicalandgenetic pages 2-3)
6. **Cardiac assessment:** ECG, echocardiography, and ambulatory rhythm monitoring; cardiac MRI when indicated.
7. **Respiratory assessment:** seated and supine FVC, maximal inspiratory/expiratory pressures, peak cough flow, nocturnal oximetry/capnography or sleep study when symptoms or declining function warrant.
8. **Functional/imaging biomarkers:** NSAD, PUL 2.0, 10- and 100-m walk/run, rise-from-floor, stair climb, TUG, and quantitative muscle MRI fat fraction. These are being implemented in prospective natural-history and gene-therapy studies. (NCT04475926 chunk 1, NCT05876780 chunk 1, NCT06246513 chunk 1)

CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are not first-line unless another diagnosis is suspected. Differential diagnoses include dystrophinopathy, FKRP-related disease, calpainopathy, dysferlinopathy, anoctaminopathy, dystroglycanopathy, Pompe disease, spinal muscular atrophy, congenital myopathy, and inflammatory myopathy.

Cascade testing should be offered to relatives after identifying familial variants. Population newborn screening is not standard; CK-first newborn approaches remain investigational. Carrier, prenatal, and preimplantation genetic testing are feasible once familial pathogenic variants are known.

## 11. Outcome and prognosis

Prognosis is determined chiefly by age at onset, residual sarcoglycan expression, genotype, and cardiac/respiratory involvement. In the 100-person cohort, 65.3% were wheelchair-bound after mean follow-up of 22.9 years, 30 required ventilation, and six died. (guimaraescosta2021clinicalcorrelationsand pages 1-3) In LGMDR4, CK, pulmonary function, and left-ventricular function declined in parallel with age, and ejection fraction was the strongest independent progression variable in one 26-patient analysis. (semplicini2015clinicalandgenetic pages 2-3)

No robust universal 5- or 10-year survival estimate exists. Severe childhood disease can cause major disability by adolescence and premature death from respiratory failure or cardiomyopathy; mild patients may remain ambulant into late adulthood. Recovery of established weakness is uncommon with supportive care, but complications can be delayed or treated. Formal sarcoglycanopathy-specific EQ-5D, SF-36, and PROMIS benchmarks remain a research gap.

## 12. Treatment and current applications

### Present standard of care

No gene-specific drug is yet established as routine curative therapy. Management is multidisciplinary:

* individualized physical and occupational therapy, stretching, orthoses, mobility aids, seating, and contracture prevention;
* low-to-moderate, non-exhaustive activity; avoid prolonged immobilization and excessive eccentric loading;
* respiratory physiotherapy, assisted cough, non-invasive ventilation, and prompt treatment of infections;
* standard guideline-directed cardiomyopathy/arrhythmia therapy—commonly ACE inhibitor/ARB/ARNI, β-blocker, mineralocorticoid antagonist, and device therapy when clinically indicated;
* nutrition, bone health, pain management, psychosocial support, anesthesia planning, and orthopedic intervention for function-threatening contracture or scoliosis.

Suggested NCIt intervention concepts include physical therapy, occupational therapy, noninvasive positive-pressure ventilation, assisted coughing, genetic counseling, AAV gene therapy, prednisone, and cardiac transplantation. Drug-level pharmacogenomic guidance specific to sarcoglycanopathy is unavailable.

### Pharmacotherapy

Glucocorticoids are not supported by the same evidence base as in Duchenne dystrophy. A small exploratory study of 19 genetically heterogeneous LGMD patients receiving weekly prednisone for 24 weeks found acceptable safety, reduced CK, and a trend toward motor improvement; it does not establish efficacy for sarcoglycanopathy. (andrea2024molecularmechanismsand pages 18-19)

### Gene and molecular therapy

**Bidridistrogene xeboparvovec (SRP-9003; scAAVrh74.MHCK7.hSGCB).** Six children aged 4–15 years received one IV dose: 1.85×10^13 vg/kg (n=3) or 7.41×10^13 vg/kg (n=3). Day-60 mean β-SG expression was 36.2% and 62.1% of normal; β-SG-positive fibers were 51% and 72%. At year 2, expression remained 54.0% and 60.3%, and year-1 NSAD improved by 5.7 and 4.0 points. (mendell2024genetherapywith pages 1-2, mendell2024genetherapywith pages 3-4, mendell2024genetherapywith pages 4-5)

The abstract reports: “The 2-year safety and efficacy of bidridistrogene xeboparvovec support clinical development advancement. Further studies are necessary to confirm the long-term safety and efficacy.” Vomiting occurred in 4/6, increased GGT in 3/6, and one patient developed AAV-related hepatitis requiring four days of hospitalization; serious events resolved with standard therapy. PMID **38177855**; published online **2024-01-04**; https://doi.org/10.1038/s41591-023-02730-9. (mendell2024genetherapywith pages 1-2, mendell2024genetherapywith pages 9-10, mendell2024genetherapywith pages 3-4, NCT03652259 chunk 1)

Key caveats are the tiny sample, open-label/nonrandomized design, post-hoc functional analysis, and unmatched natural-history comparators. (mendell2024genetherapywith pages 7-8)

**Active development:**

* **NCT05876780:** phase 1 SRP-9003 study in ambulatory and nonambulatory LGMDR4, six participants, with day-60 and month-24 protein endpoints and five-year follow-up. (NCT05876780 chunk 1)
* **NCT06246513/EMERGENE:** multinational phase 3, 17 participants, single SRP-9003 infusion plus prophylactic prednisone; primary day-60 β-SG-positive-fiber endpoint, with NSAD/PUL and safety through month 60. Trial began January 15, 2024. (NCT06246513 chunk 1)
* **NCT05973630:** ATA-200, an AAV vector carrying human **SGCG**, phase 1 for ambulant children with LGMDR5; four participants receive 1.0×10^14 vg/kg IV with five-year follow-up. (NCT05973630 chunk 1)
* **NCT04475926/Journey:** prospective natural history, 205 participants across LGMDR3–5 and calpainopathy, measuring NSAD, PUL, timed function, ROM, and FVC for up to five years. (NCT04475926 chunk 1)

Earlier isolated-limb SGCA transfer produced only modest expression and inconsistent function. Preclinical AAV-SGCA/SGCG studies improved protein expression, histology, force, motor function, and CK in knockout mice. Exon skipping for selected SGCG variants and mesoangioblast therapy remain preclinical. (andrea2024molecularmechanismsand pages 18-19)

## 13. Prevention

Primary prevention by lifestyle or vaccination is impossible because the initiating defect is inherited. Reproductive prevention options include carrier testing, partner testing, cascade screening, preimplantation genetic testing, chorionic-villus sampling, and amniocentesis after counseling. Secondary prevention consists of early molecular diagnosis and presymptomatic cardiac/respiratory surveillance. Tertiary prevention includes stretching, safe activity, vaccinations, airway clearance, timely ventilation, cardioprotective therapy, fall prevention, and avoidance of prolonged immobility. There is no disease-specific vaccine or preventive medication.

## 14. Other species and natural disease

Orthologous sarcoglycan disease occurs naturally in several mammals. The best-established comparative systems include δ-sarcoglycan-deficient Syrian hamsters with cardiomyopathy and muscular dystrophy and naturally occurring canine sarcoglycan deficiencies. Their pathology supports evolutionary conservation of DAPC-mediated membrane stabilization. Veterinary disease is inherited and nonzoonotic; there is no cross-species transmission. Relevant taxa include **Mus musculus** (NCBI Taxon 10090), **Danio rerio** (7955), **Mesocricetus auratus** (10036), and **Canis lupus familiaris** (9615). Breed-specific assertions should be linked to OMIA/VBO records rather than generalized across dogs.

## 15. Model organisms and experimental systems

* **Mouse:** Sgca, Sgcb, Sgcg, and Sgcd knockout models reproduce progressive skeletal dystrophy. β-, γ-, and δ-SG-null mice develop dilated or hypertrophic cardiomyopathy, whereas α-SG-null mice generally do not—an important limitation and genotype-specific strength. (barba2023modelingsarcoglycanopathyin pages 1-2)
* **Zebrafish:** CRISPR sgcb−/− and sgcd−/− lines progress from mild larval impairment to adult myopathy and cardiac disease. The models reproduce fiber disarray, inflammation, fibrosis, adipose replacement, and mitochondrial injury and permit high-throughput drug screening. Mechanical challenge accelerates phenotype onset. Published **2023-08-11**; https://doi.org/10.3390/ijms241612707. (barba2023modelingsarcoglycanopathyin pages 6-9, barba2023modelingsarcoglycanopathyin pages 1-2)
* **Hamster:** naturally occurring δ-SG deficiency is particularly useful for cardiomyopathy and systemic therapy studies.
* **Cellular systems:** patient myoblasts, engineered myotubes, and heterologous expression systems are used for trafficking, ERAD, proteasome rescue, splice assays, and AAV construct validation. Mature human iPSC-derived skeletal-muscle/cardiac models and organoids are promising but not yet standardized diagnostic platforms.

The principal model limitation is that disease tempo, immune response to AAV, body size, and cardiac penetrance differ from humans. Consequently, successful rescue in rodents or fish is necessary but not sufficient evidence of clinical efficacy.

## Evidence appraisal and principal gaps

The strongest evidence is human cohort evidence for natural history and a 2024 peer-reviewed first-in-human SGCB trial. Mechanistic evidence is mainly model-organism and in vitro evidence. Major unresolved areas include precise population incidence, standardized quality-of-life utilities, validated circulating biomarkers beyond CK, human modifier genes, disease-specific single-cell/multi-omics maps, optimal exercise prescriptions, long-term AAV durability and safety, and therapies for patients with advanced fibrofatty replacement. The most authoritative current interpretation is therefore that sarcoglycanopathy is molecularly well defined but clinically heterogeneous, and that early genotype confirmation plus lifelong cardiac and respiratory surveillance remains essential while gene-replacement efficacy is being confirmed.

References

1. (barba2023modelingsarcoglycanopathyin pages 1-2): Francesco Dalla Barba, Michela Soardi, Leila Mouhib, Giovanni Risato, Eylem Emek Akyürek, Tyrone Lucon-Xiccato, Martina Scano, Alberto Benetollo, Roberta Sacchetto, Isabelle Richard, Francesco Argenton, Cristiano Bertolucci, Marcello Carotti, and Dorianna Sandonà. Modeling sarcoglycanopathy in danio rerio. Aug 2023. URL: https://doi.org/10.3390/ijms241612707, doi:10.3390/ijms241612707. This article has 7 citations.

2. (guimaraescosta2021clinicalcorrelationsand pages 1-3): R. Guimarães-Costa, G. Fernández-Eulate, K. Wahbi, F. Leturcq, E. Malfatti, A. Béhin, S. Leonard-Louis, I. Desguerre, C. Barnerias, Marie-Christine Nouguès, A. Isapof, B. Estournet‐Mathiaud, S. Quijano-roy, A. Fayssoil, D. Orlikowski, B. Fauroux, I. Richard, C. Semplicini, N. Romero, G. Querin, B. Eymard, P. Laforêt, and T. Stojkovic. Clinical correlations and long‐term follow‐up in 100 patients with sarcoglycanopathies. Nov 2021. URL: https://doi.org/10.1111/ene.14592, doi:10.1111/ene.14592. This article has 33 citations and is from a domain leading peer-reviewed journal.

3. (mendell2024genetherapywith pages 1-2): Jerry R. Mendell, Eric R. Pozsgai, Sarah Lewis, Danielle A. Griffin, Linda P. Lowes, Lindsay N. Alfano, Kelly J. Lehman, Kathleen Church, Natalie F. Reash, Megan A. Iammarino, Brenna Sabo, Rachael Potter, Sarah Neuhaus, Xiaoxi Li, Herb Stevenson, and Louise R. Rodino-Klapac. Gene therapy with bidridistrogene xeboparvovec for limb-girdle muscular dystrophy type 2e/r4: phase 1/2 trial results. Nature Medicine, 30:199-206, Jan 2024. URL: https://doi.org/10.1038/s41591-023-02730-9, doi:10.1038/s41591-023-02730-9. This article has 33 citations and is from a highest quality peer-reviewed journal.

4. (mendell2024genetherapywith pages 7-8): Jerry R. Mendell, Eric R. Pozsgai, Sarah Lewis, Danielle A. Griffin, Linda P. Lowes, Lindsay N. Alfano, Kelly J. Lehman, Kathleen Church, Natalie F. Reash, Megan A. Iammarino, Brenna Sabo, Rachael Potter, Sarah Neuhaus, Xiaoxi Li, Herb Stevenson, and Louise R. Rodino-Klapac. Gene therapy with bidridistrogene xeboparvovec for limb-girdle muscular dystrophy type 2e/r4: phase 1/2 trial results. Nature Medicine, 30:199-206, Jan 2024. URL: https://doi.org/10.1038/s41591-023-02730-9, doi:10.1038/s41591-023-02730-9. This article has 33 citations and is from a highest quality peer-reviewed journal.

5. (semplicini2015clinicalandgenetic pages 2-3): Claudio Semplicini, John Vissing, Julia R. Dahlqvist, Tanya Stojkovic, Luca Bello, Nanna Witting, Morten Duno, France Leturcq, Cinzia Bertolin, Paola D'Ambrosio, Bruno Eymard, Corrado Angelini, Luisa Politano, Pascal Laforêt, and Elena Pegoraro. Clinical and genetic spectrum in limb-girdle muscular dystrophy type 2e. Neurology, 84:1772-1781, Apr 2015. URL: https://doi.org/10.1212/wnl.0000000000001519, doi:10.1212/wnl.0000000000001519. This article has 85 citations and is from a highest quality peer-reviewed journal.

6. (NCT03652259 chunk 1):  Gene Delivery Clinical Trial of SRP-9003 (Bidridistrogene Xeboparvovec) for Participants With Limb-Girdle Muscular Dystrophy, Type 2E (LGMD2E) (Beta-Sarcoglycan Deficiency). Sarepta Therapeutics, Inc.. 2018. ClinicalTrials.gov Identifier: NCT03652259

7. (alonsoperez2022clinicalandgenetic pages 1-1): Jorge Alonso-Pérez, Lidia González-Quereda, Claudio Bruno, Chiara Panicucci, Afagh Alavi, Shahriar Nafissi, Yalda Nilipour, Edmar Zanoteli, Lucas Michielon de Augusto Isihi, Béla Melegh, Kinga Hadzsiev, Nuria Muelas, Juan J Vílchez, Mario Emilio Dourado, Naz Kadem, Gultekin Kutluk, Muhammad Umair, Muhammad Younus, Elena Pegorano, Luca Bello, Thomas O Crawford, Xavier Suárez-Calvet, Ana Töpf, Michela Guglieri, Chiara Marini-Bettolo, Pia Gallano, Volker Straub, and Jordi Díaz-Manera. Clinical and genetic spectrum of a large cohort of patients with δ-sarcoglycan muscular dystrophy. Brain, 145:596-606, Sep 2022. URL: https://doi.org/10.1093/brain/awab301, doi:10.1093/brain/awab301. This article has 34 citations and is from a highest quality peer-reviewed journal.

8. (alonsoperez2022clinicalandgenetic pages 2-3): Jorge Alonso-Pérez, Lidia González-Quereda, Claudio Bruno, Chiara Panicucci, Afagh Alavi, Shahriar Nafissi, Yalda Nilipour, Edmar Zanoteli, Lucas Michielon de Augusto Isihi, Béla Melegh, Kinga Hadzsiev, Nuria Muelas, Juan J Vílchez, Mario Emilio Dourado, Naz Kadem, Gultekin Kutluk, Muhammad Umair, Muhammad Younus, Elena Pegorano, Luca Bello, Thomas O Crawford, Xavier Suárez-Calvet, Ana Töpf, Michela Guglieri, Chiara Marini-Bettolo, Pia Gallano, Volker Straub, and Jordi Díaz-Manera. Clinical and genetic spectrum of a large cohort of patients with δ-sarcoglycan muscular dystrophy. Brain, 145:596-606, Sep 2022. URL: https://doi.org/10.1093/brain/awab301, doi:10.1093/brain/awab301. This article has 34 citations and is from a highest quality peer-reviewed journal.

9. (OpenTargets Search: sarcoglycanopathy): Open Targets Query (sarcoglycanopathy, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (NCT04475926 chunk 2):  A Study of the Natural History of Participants With LGMD2E/R4, LGMD2D/R3, LGMD2C/R5, and LGMD2A/R1 ≥ 4 Years of Age, Who Are Managed in Routine Clinical Practice. Sarepta Therapeutics, Inc.. 2021. ClinicalTrials.gov Identifier: NCT04475926

11. (NCT04475926 chunk 1):  A Study of the Natural History of Participants With LGMD2E/R4, LGMD2D/R3, LGMD2C/R5, and LGMD2A/R1 ≥ 4 Years of Age, Who Are Managed in Routine Clinical Practice. Sarepta Therapeutics, Inc.. 2021. ClinicalTrials.gov Identifier: NCT04475926

12. (NCT05876780 chunk 1):  A Gene Transfer Single Dose Study to Evaluate the Safety, Tolerability and Efficacy of SRP-9003 in Non-Ambulatory and Ambulatory Participants With Limb Girdle Muscular Dystrophy, Type 2E/R4 (Beta-Sarcoglycan [β-SG] Deficiency). Sarepta Therapeutics, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05876780

13. (barba2023modelingsarcoglycanopathyin pages 6-9): Francesco Dalla Barba, Michela Soardi, Leila Mouhib, Giovanni Risato, Eylem Emek Akyürek, Tyrone Lucon-Xiccato, Martina Scano, Alberto Benetollo, Roberta Sacchetto, Isabelle Richard, Francesco Argenton, Cristiano Bertolucci, Marcello Carotti, and Dorianna Sandonà. Modeling sarcoglycanopathy in danio rerio. Aug 2023. URL: https://doi.org/10.3390/ijms241612707, doi:10.3390/ijms241612707. This article has 7 citations.

14. (NCT06246513 chunk 1):  A Trial to Learn More About an Experimental Gene Therapy Called Bidridistrogene Xeboparvovec (SRP-9003) as a Possible Treatment for Limb Girdle Muscular Dystrophy 2E/R4. Sarepta Therapeutics, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06246513

15. (andrea2024molecularmechanismsand pages 18-19): Zambon Alberto Andrea, Falzone Yuri Matteo, Bolino Alessandra, and Previtali Stefano Carlo. Molecular mechanisms and therapeutic strategies for neuromuscular diseases. Cellular and Molecular Life Sciences: CMLS, Apr 2024. URL: https://doi.org/10.1007/s00018-024-05229-9, doi:10.1007/s00018-024-05229-9. This article has 23 citations.

16. (mendell2024genetherapywith pages 3-4): Jerry R. Mendell, Eric R. Pozsgai, Sarah Lewis, Danielle A. Griffin, Linda P. Lowes, Lindsay N. Alfano, Kelly J. Lehman, Kathleen Church, Natalie F. Reash, Megan A. Iammarino, Brenna Sabo, Rachael Potter, Sarah Neuhaus, Xiaoxi Li, Herb Stevenson, and Louise R. Rodino-Klapac. Gene therapy with bidridistrogene xeboparvovec for limb-girdle muscular dystrophy type 2e/r4: phase 1/2 trial results. Nature Medicine, 30:199-206, Jan 2024. URL: https://doi.org/10.1038/s41591-023-02730-9, doi:10.1038/s41591-023-02730-9. This article has 33 citations and is from a highest quality peer-reviewed journal.

17. (mendell2024genetherapywith pages 4-5): Jerry R. Mendell, Eric R. Pozsgai, Sarah Lewis, Danielle A. Griffin, Linda P. Lowes, Lindsay N. Alfano, Kelly J. Lehman, Kathleen Church, Natalie F. Reash, Megan A. Iammarino, Brenna Sabo, Rachael Potter, Sarah Neuhaus, Xiaoxi Li, Herb Stevenson, and Louise R. Rodino-Klapac. Gene therapy with bidridistrogene xeboparvovec for limb-girdle muscular dystrophy type 2e/r4: phase 1/2 trial results. Nature Medicine, 30:199-206, Jan 2024. URL: https://doi.org/10.1038/s41591-023-02730-9, doi:10.1038/s41591-023-02730-9. This article has 33 citations and is from a highest quality peer-reviewed journal.

18. (mendell2024genetherapywith pages 9-10): Jerry R. Mendell, Eric R. Pozsgai, Sarah Lewis, Danielle A. Griffin, Linda P. Lowes, Lindsay N. Alfano, Kelly J. Lehman, Kathleen Church, Natalie F. Reash, Megan A. Iammarino, Brenna Sabo, Rachael Potter, Sarah Neuhaus, Xiaoxi Li, Herb Stevenson, and Louise R. Rodino-Klapac. Gene therapy with bidridistrogene xeboparvovec for limb-girdle muscular dystrophy type 2e/r4: phase 1/2 trial results. Nature Medicine, 30:199-206, Jan 2024. URL: https://doi.org/10.1038/s41591-023-02730-9, doi:10.1038/s41591-023-02730-9. This article has 33 citations and is from a highest quality peer-reviewed journal.

19. (NCT05973630 chunk 1):  ATA-200 Gene Therapy Trial in Patients With LGMDR5. Atamyo Therapeutics. 2025. ClinicalTrials.gov Identifier: NCT05973630

## Artifacts

- [Edison artifact artifact-00](Sarcoglycanopathy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.