---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T22:13:52.919585'
end_time: '2026-08-19T22:23:26.817577'
duration_seconds: 573.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Scrub typhus
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Scrub_Typhus-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Scrub typhus
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Scrub typhus** covering all of the
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
- **Disease Name:** Scrub typhus
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Scrub typhus** covering all of the
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


# Scrub Typhus: Comprehensive Disease-Characteristics Report

## Executive summary

Scrub typhus is an acute, potentially fatal, mite-borne infection caused principally by the obligate intracellular bacterium *Orientia tsutsugamushi*. Humans are accidental dead-end hosts; larval trombiculid mites (“chiggers”), especially *Leptotrombidium* species, transmit infection, while small mammals—particularly rodents—support the enzootic cycle. Approximately 2 billion people live in at-risk regions and the commonly cited burden is about 1 million cases annually, although weak surveillance and non-standardized diagnostics make this estimate uncertain. The central lesion is disseminated infection of endothelial and mononuclear-phagocyte compartments, producing vasculitis-like endothelial dysfunction, capillary leak, inflammation, and potentially respiratory, hepatic, cardiovascular, renal, or neurologic failure. (lynnette2024scrubtyphusdiagnostics pages 1-2, adhikari2024editorialscrubtyphus pages 2-3, ravishankar2024rickettsialinfectionsprevalence pages 4-5)

The most consequential recent therapeutic development is the 2023 INTREST randomized trial: intravenous doxycycline plus azithromycin reduced a composite of death at day 28, persistent organ complications at day 7, or fever at day 5 to 33%, versus 47% with doxycycline and 48% with azithromycin alone. Mortality itself remained similar at 11–13%, so the benefit principally concerned earlier resolution of fever/organ complications rather than demonstrated survival benefit. (varghese2023intravenousdoxycyclineazithromycin pages 4-6, varghese2023intravenousdoxycyclineazithromycin pages 21-23, varghese2023intravenousdoxycyclineazithromycin pages 8-10)

The following table provides a knowledge-base-ready synopsis; details and evidentiary qualifications follow.

| Domain | Compact knowledge-base summary | Suggested ontology mappings | Key evidence |
|---|---|---|---|
| Identity / identifiers | Scrub typhus is an acute febrile zoonotic infectious disease caused mainly by *Orientia tsutsugamushi*; also called tsutsugamushi disease. Humans are accidental dead-end hosts. ICD-10-CM code reported as **A75.3**. Disease-level information is derived from aggregated literature, surveillance, and clinical studies rather than individual EHRs in the cited sources. | **Suggested mappings:** ICD-10 **A75.3**; MeSH: scrub typhus / tsutsugamushi disease; MONDO: suggest mapping only after external ontology confirmation; NCIT: infectious disease / rickettsial-oriential infection terms if used locally | (lynnette2024scrubtyphusdiagnostics pages 1-2, adhikari2024editorialscrubtyphus pages 2-3, ravishankar2024rickettsialinfectionsprevalence pages 4-5) |
| Cause and transmission | Primary cause: infection with *O. tsutsugamushi* transmitted by larval trombiculid mites (chiggers), especially *Leptotrombidium* spp. Rodents are maintenance/reservoir hosts; humans acquire infection from mite bites in mite-infested habitats including farming/plantation settings. >20 genotypes reported in India. | **Suggested mappings:** CHEBI not central; UBERON skin for inoculation site; GO: pathogenesis, host cell invasion; CL: endothelial cell, monocyte, macrophage | (lynnette2024scrubtyphusdiagnostics pages 1-2, adhikari2024editorialscrubtyphus pages 2-3, ravishankar2024rickettsialinfectionsprevalence pages 4-5) |
| Incubation / course | Incubation typically **6–21 days**; illness usually begins as acute undifferentiated febrile illness. Without treatment, systemic manifestations often expand over the first 1–2 weeks and may progress to multiorgan dysfunction. In mouse intradermal model, fever emerged at 11–12 dpi and tissue burden peaked ~14 dpi, supporting acute then persistent phases. | **Suggested mappings:** HPO: Fever; HPO: Acute infectious disease course; UBERON: blood, lung, liver, kidney, brain, skin | (ravishankar2024rickettsialinfectionsprevalence pages 4-5, chaturvedi2025spatiotemporalepidemiologyand pages 7-8, lynnette2024scrubtyphusdiagnostics pages 1-2, liang2023braintranscriptomicsreveal pages 1-2) |
| Major phenotypes with frequencies | Common phenotype: fever/AUFI pooled prevalence **97%** in India meta-analysis. General symptoms such as headache/chills/myalgia/arthralgia occur in **33–56%**. Eschar pooled prevalence about **26%** in meta-analysis, though reviews note wide observed range **7–80%**. Hepatomegaly **46%** and hepatic dysfunction **44%** were reported in meta-analysis. Severe-trial complications: respiratory **62%**, hepatic **54%**, cardiovascular **42%**, renal **30%**, neurologic **20%**. Reported neurologic manifestations include meningitis/meningoencephalitis, tremor, delirium, hearing loss; respiratory disease includes interstitial pneumonia/ARDS; renal injury and myocarditis/arrhythmia are recognized complications. | **Suggested HPO terms:** Fever; Eschar; Headache; Myalgia; Rash; Lymphadenopathy; Hepatomegaly; Elevated hepatic transaminases; Acute kidney injury; Pneumonia; Acute respiratory distress syndrome; Myocarditis; Arrhythmia; Meningoencephalitis; Hearing impairment | (vashishtha2025scrubtyphusupdate pages 6-7, chaturvedi2025spatiotemporalepidemiologyand pages 7-8, varghese2023intravenousdoxycyclineazithromycin pages 4-6, varghese2023intravenousdoxycyclineazithromycin pages 21-23) |
| Key cell types and pathways | Targeted/involved cells include **endothelial cells**, **monocytes/macrophages**, dendritic cells, and in CNS disease **microglia**. Human monocytes showed >4,500 altered genes with type I IFN program, interferon-stimulated genes, apoptosis genes, and M1 polarization. Endothelial dual RNA-seq found strain-specific host responses: Karp induced **IL33-NOS3-FAS** anoikis-associated signaling, whereas UT176 induced **IL6**-dominant inflammatory response. Mouse brain RNA-seq showed IFN responses, defense response to bacteria, IL-6/JAK-STAT, TNF/NF-κB, immunoglobulin-mediated immunity, and BBB-disruption programs with microglial activation. | **Suggested GO terms:** inflammatory response; type I interferon signaling pathway; cytokine-mediated signaling pathway; apoptotic process; response to bacterium; IL-6-mediated signaling pathway; JAK-STAT cascade; TNF-mediated signaling pathway; blood-brain barrier maintenance/disruption. **Suggested CL terms:** endothelial cell, monocyte, macrophage, dendritic cell, microglial cell. **Suggested UBERON terms:** vascular endothelium, brain, skin, liver, lung | (mikagospodorz2020dualrnaseqof pages 9-9, tantibhedhyangkul2011orientiatsutsugamushistimulates pages 1-2, liang2023braintranscriptomicsreveal pages 1-2, lynnette2024scrubtyphusdiagnostics pages 1-2) |
| Diagnostics | Diagnosis is difficult when eschar is absent. Serology remains central: IFA is the most widely used reference method, but thresholds and antigen panels vary greatly by region. IgM/IgG serology and ELISA are widely used; immunochromatographic tests have about **~70% sensitivity** in one review context. PCR is most useful early and can be performed on blood/buffy coat and eschar material; editorial summary reported eschar PCR positivity **100%** and buffy-coat positivity **94%** in highlighted work. QuEST (NCT06675110) is evaluating insulated isothermal PCR against qPCR/IFA. | **Suggested mappings:** LOINC/local lab mappings for IgM ELISA, IFA, PCR; HPO/Lab terms: thrombocytopenia, transaminitis, hyperbilirubinemia, elevated creatinine | (lynnette2024scrubtyphusdiagnostics pages 1-2, adhikari2024editorialscrubtyphus pages 2-3, chaturvedi2025spatiotemporalepidemiologyand pages 2-3, NCT06675110 chunk 1) |
| Treatment | Standard therapy uses anti-rickettsial antibiotics, especially **doxycycline**; **azithromycin** is an important alternative, including in pregnancy. In the 2023 multicenter double-blind RCT for severe disease, IV doxycycline was **200 mg BID day 1 then 100 mg BID for 6 days**; IV azithromycin was **500 mg BID day 1 then 500 mg daily for 6 days**; combination used both. Combination therapy reduced the composite endpoint to **33%** vs **47%** with doxycycline and **48%** with azithromycin (risk differences **−13.3** and **−14.8** percentage points, respectively). Mortality at day 28 was similar (**11–13%**). | **Suggested NCIT terms:** Doxycycline; Azithromycin; Combination anti-infective therapy; Intravenous antibiotic therapy. **Suggested CHEBI:** doxycycline, azithromycin | (varghese2023intravenousdoxycyclineazithromycin pages 4-6, varghese2023intravenousdoxycyclineazithromycin pages 21-23, varghese2023intravenousdoxycyclineazithromycin pages 6-8, varghese2023intravenousdoxycyclineazithromycin pages 8-10) |
| Epidemiology | Endemic historically in the “tsutsugamushi triangle,” but current literature emphasizes broader geographic concern. About **2 billion** people are at risk and roughly **1 million** cases occur annually. In India, a 2025 systematic review identified **47,650** cumulative cases from 2003–2023 with **5%** case fatality among 35,243 cases analyzed. In South Korea, **95,601** patients were reported from 2013–2019 with spatial clustering associated with rodent suitability and local socioeconomic/environmental factors. | **Suggested mappings:** geographic/endemic disease annotations; One Health/vector-borne disease labels | (lynnette2024scrubtyphusdiagnostics pages 1-2, chaturvedi2025spatiotemporalepidemiologyand pages 2-3, adhikari2024editorialscrubtyphus pages 2-3) |
| Prognosis | Prognosis is highly treatment-sensitive: untreated or delayed diagnosis can progress to severe multiorgan disease. In severe hospitalized disease, 28-day mortality remained around **11–13%** in the 2023 RCT despite therapy. Prognostic burden is driven by respiratory, cardiovascular, renal, hepatic, and neurologic complications; delayed diagnosis and limited diagnostic access are recurring risk amplifiers in reviews. | **Suggested HPO terms:** Multiorgan failure; Shock; ARDS; Acute kidney injury; Encephalopathy. **Suggested NCIT:** Critical care / ICU support | (vashishtha2025scrubtyphusupdate pages 11-12, varghese2023intravenousdoxycyclineazithromycin pages 4-6, varghese2023intravenousdoxycyclineazithromycin pages 21-23, ravishankar2024rickettsialinfectionsprevalence pages 7-8) |
| Prevention | No licensed highly effective vaccine is currently available in the cited literature. Prevention focuses on avoiding chigger exposure, vector/reservoir control, environmental risk reduction, and early recognition/treatment. Public-health emphasis is on awareness, region-specific surveillance, and improved rapid diagnostics. | **Suggested NCIT/public health mappings:** Vector control; Health education; Personal protective measures; Early diagnosis | (vashishtha2025scrubtyphusupdate pages 11-12, adhikari2024editorialscrubtyphus pages 2-3, lynnette2024scrubtyphusdiagnostics pages 1-2) |
| Animal models / other species | Natural ecology involves rodents and chiggers, with human, rodent, and mite genotype-linkage studied in field cohorts. A C57BL/6 intradermal mouse model reproduces acute disease and persistent infection after ear inoculation, with mixed Th1/Th2 cytokine responses and prolonged tissue persistence to **84 dpi**. Additional model-development work includes nonhuman-primate transmission studies and newer humanized IFN-γ mouse approaches mentioned in the literature context. | **Suggested mappings:** NCBI Taxon for *O. tsutsugamushi* and rodent/chigger hosts; CL/UBERON as above for infected tissues | (NCT02876367 chunk 1, lynnette2024scrubtyphusdiagnostics pages 1-2, ravishankar2024rickettsialinfectionsprevalence pages 4-5, liang2023braintranscriptomicsreveal pages 1-2) |
| Genetics fields that are non-applicable or limited | **Mendelian inheritance, causal human disease genes, pathogenic germline variants, carrier frequency, anticipation, consanguinity, CMA/karyotype/FISH-based diagnosis:** generally **not applicable** because scrub typhus is an infectious disease, not a monogenic inherited disorder. **Host susceptibility genetics:** limited candidate-gene evidence only; an unobtainable 2013 study is noted in retrieved metadata for TLR2/TLR4/HSP70 SNPs, but this was not directly available for full evidence extraction here. Pathogen genomics, not host Mendelian genetics, is the main molecular genetics domain of relevance. | **Suggested mappings:** mark as “Not applicable” for inheritance fields; use pathogen-genomics annotations instead of human Mendelian fields | (tantibhedhyangkul2011orientiatsutsugamushistimulates pages 1-2, NCT03083197 chunk 1) |


*Table: This table condenses the most actionable scrub typhus facts for a disease knowledge base, including clinical, epidemiologic, mechanistic, diagnostic, and treatment domains. It also flags which classical human genetics fields are not applicable for this infectious disease and suggests ontology mappings without inventing uncertain IDs.*

## 1. Disease information

### Definition and names

Scrub typhus is an acute undifferentiated febrile illness caused mainly by *O. tsutsugamushi*. Synonyms include **tsutsugamushi disease**, **tsutsugamushi fever**, **mite-borne typhus**, and historically **Japanese river fever**. Despite its historical grouping with rickettsioses, the organism belongs to *Orientia*, not *Rickettsia*. A recent review describes it as a “vector-borne, zoonotic disease” that becomes diagnostically difficult when the characteristic eschar is absent. (lynnette2024scrubtyphusdiagnostics pages 1-2, chaturvedi2025spatiotemporalepidemiologyand pages 2-3)

### Identifiers

- **ICD-10/ICD-10-CM:** **A75.3**, Typhus fever due to *Rickettsia tsutsugamushi*; the legacy organism name persists in the label.
- **ICD-11:** classified under rickettsioses/other specified rickettsioses; the exact browser code should be validated against the current ICD-11 release before ingestion.
- **MeSH:** *Scrub Typhus*; entry terms include tsutsugamushi disease.
- **MONDO:** a scrub-typhus concept exists, but the exact numerical MONDO identifier was not recoverable from the retrieved primary literature and should be resolved directly through the current MONDO release rather than inferred.
- **OMIM/Orphanet:** no causal-disease entry is expected in the Mendelian-disease sense; this is an acquired infectious disease, not a monogenic disorder.

The evidence summarized here is **aggregated disease-level evidence** from reviews, cohorts, trials, and experimental studies—not patient-level EHR data.

## 2. Etiology, risk, and protective factors

### Cause and transmission

The immediate cause is inoculation of *Orientia* by an infected chigger. The principal agent is *O. tsutsugamushi*, a gram-negative, non-motile, non-capsulated, pleomorphic obligate intracellular bacterium. More than 20 genotypes have been described in India alone, and antigenic/genomic diversity is a major obstacle to universal serodiagnostics and vaccines. (chaturvedi2025spatiotemporalepidemiologyand pages 2-3, ravishankar2024rickettsialinfectionsprevalence pages 4-5)

Chiggers acquire and maintain *Orientia* within mite populations; rodents and other small mammals serve as feeding hosts and ecological reservoirs. Humans do not ordinarily transmit infection onward. Risk is therefore ecological rather than hereditary: agricultural work, paddy cultivation, plantations, brush or scrub vegetation, contact with mite-infested soil, and residence or travel in endemic rural landscapes increase exposure. Temperature, humidity, rainfall, rodent suitability, and season influence transmission. (adhikari2024editorialscrubtyphus pages 2-3, ravishankar2024rickettsialinfectionsprevalence pages 4-5, NCT02876367 chunk 1)

### Demographic and host risk

All ages can be affected. Exposure patterns often make farmers, field workers, military personnel, and rural residents overrepresented. Older age and comorbidity may worsen outcomes, but the retrieved evidence does not support a universal sex ratio. Pregnancy is clinically important because maternal infection can be severe and influences antibiotic selection.

### Genetic risk and gene–environment interaction

There are **no causal human genes, pathogenic germline variants, inheritance pattern, penetrance, carrier frequency, founder mutations, or chromosomal abnormalities**. Limited candidate-gene literature has examined immune-response loci such as **TLR2, TLR4, and HSP70**, but the relevant primary article was not available in full text during this retrieval; these associations should not be treated as validated clinical susceptibility markers. Exposure to infected mites overwhelmingly dominates risk, and no host genotype is used for diagnosis, prognosis, or treatment selection.

### Protective factors

Protection is primarily environmental and behavioral: avoiding mite habitats, using protective clothing and repellents, clearing vegetation around camps or dwellings, and prompt recognition and treatment. No reproducible protective human allele is established. Natural immunity is strain-limited and may be short-lived; antigenic heterogeneity limits cross-protection.

## 3. Phenotypes

The incubation period is usually **6–21 days**. Disease begins acutely with fever, headache, myalgia, chills, malaise, and sometimes cough or gastrointestinal symptoms. In an India meta-analysis, fever/AUFI had a pooled prevalence of **97%**, while headache, chills, myalgia, and arthralgia individually or collectively occurred in approximately **33–56%**. (ravishankar2024rickettsialinfectionsprevalence pages 4-5, chaturvedi2025spatiotemporalepidemiologyand pages 7-8)

### Principal phenotype annotations

- **Fever**—acute, nearly universal, variable severity; suggested HPO: *Fever*.
- **Eschar**—painless necrotic crust at the bite site, often hidden in axillae, groin, inframammary or genital regions. Pooled prevalence was about **26%** in the India analysis, whereas reports range from **7–80%** across populations. Absence does not exclude infection. Suggested HPO: *Eschar* or closest available necrotic-skin-lesion term. (vashishtha2025scrubtyphusupdate pages 6-7, chaturvedi2025spatiotemporalepidemiologyand pages 7-8)
- **Maculopapular rash**—often appears near the end of week 1 and spreads from trunk to limbs; variably present. Suggested HPO: *Maculopapular rash*.
- **Regional lymphadenopathy**—typically near the inoculation site; suggested HPO: *Lymphadenopathy*.
- **Hepatic disease**—hepatomegaly **46%** and hepatic dysfunction **44%** in the cited meta-analysis; transaminase elevation and hyperbilirubinemia are common laboratory abnormalities. Suggested HPO: *Hepatomegaly*, *Elevated hepatic transaminases*, *Hyperbilirubinemia*. (chaturvedi2025spatiotemporalepidemiologyand pages 7-8)
- **Respiratory disease**—interstitial pneumonitis, hypoxemia, pulmonary edema/capillary leak, and ARDS. Respiratory involvement occurred in **62%** of the severe-disease trial population. Suggested HPO: *Interstitial pulmonary disease*, *Hypoxemia*, *Acute respiratory distress syndrome*. (varghese2023intravenousdoxycyclineazithromycin pages 4-6)
- **Cardiovascular disease**—hypotension/shock, myocarditis, arrhythmia, heart failure, and occasionally myocardial infarction. Cardiovascular involvement occurred in **42%** of severe trial participants. Suggested HPO: *Hypotension*, *Myocarditis*, *Cardiac arrhythmia*, *Heart failure*. (adhikari2024editorialscrubtyphus pages 2-3, varghese2023intravenousdoxycyclineazithromycin pages 4-6)
- **Renal disease**—acute kidney injury from hypoperfusion, endothelial injury, inflammation, and multiorgan dysfunction; **30%** in the severe trial. Suggested HPO: *Acute kidney injury*, *Elevated serum creatinine*. (varghese2023intravenousdoxycyclineazithromycin pages 4-6)
- **Neurologic disease**—meningitis, meningoencephalitis, delirium, seizures, tremor, cerebellitis, hearing loss, or altered consciousness; **20%** had neurologic involvement in the severe trial. Suggested HPO: *Meningitis*, *Encephalitis*, *Seizure*, *Delirium*, *Tremor*, *Sensorineural hearing impairment*. (vashishtha2025scrubtyphusupdate pages 6-7, varghese2023intravenousdoxycyclineazithromycin pages 4-6)
- **Hematologic abnormalities**—thrombocytopenia and, in severe cases, coagulopathy; suggested HPO: *Thrombocytopenia*.

Phenotypes are acute and progressive when untreated rather than stable or lifelong. Quality-of-life studies using EQ-5D or SF-36 were not identified. During acute severe disease, ICU admission, ventilation, encephalopathy, and organ failure profoundly impair function; survivors treated promptly generally recover, although neurologic, auditory, renal, or cardiac sequelae may persist in a minority.

## 4. Genetic and molecular information

### Human genetics

Classical disease-genetics fields are **not applicable**: no causal HGNC gene, OMIM gene, ACMG-classified pathogenic variant, germline/somatic distinction, allele frequency, modifier gene, chromosomal abnormality, or clinically actionable pharmacogenomic marker defines scrub typhus. WES, WGS, panels, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing have no role in routine diagnosis.

### Pathogen genomics

*O. tsutsugamushi* has an unusually repetitive, rearranged genome with poor strain-to-strain gene-order collinearity. Dual RNA-seq indicated that virulence differences between Karp and UT176 strains related substantially to **differential expression**, not simply gene presence or absence. The Karp strain induced an IL33–NOS3–FAS-associated anoikis program in endothelial cells, whereas UT176 produced a more IL6-dominant response. The experiment used a high multiplicity of infection (~30:1), limiting direct physiological extrapolation. (mikagospodorz2020dualrnaseqof pages 9-9)

The ongoing START trial incorporates whole-genome sequencing of isolates to relate genotype to clearance, relapse, and antimicrobial susceptibility—an example of pathogen precision medicine rather than inherited human genetics. (NCT03083197 chunk 1)

## 5. Environmental and infectious-agent information

The infectious agent is *Orientia*, transmitted through chigger-infested environments. Farming, scrub vegetation, forest edges, soil contact, rainfall, humidity, temperature, and rodent abundance shape risk. A One Health framework is therefore appropriate. Tobacco, alcohol, diet, and exercise are not established causal factors, although nutritional status and comorbidity could influence severity nonspecifically. (adhikari2024editorialscrubtyphus pages 2-3, ravishankar2024rickettsialinfectionsprevalence pages 4-5)

The traditional “tsutsugamushi triangle” extends broadly from northern Asia/Japan through South and Southeast Asia to northern Australia, but recent literature emphasizes transmission or *Orientia*-like organisms beyond this historical boundary. This changing geography may reflect improved detection, travel, land-use change, vector-range shifts, climate, and genuine emergence. (vashishtha2025scrubtyphusupdate pages 11-12, lynnette2024scrubtyphusdiagnostics pages 1-2, adhikari2024editorialscrubtyphus pages 2-3)

## 6. Mechanism and pathophysiology

### Causal chain

**Chigger bite → dermal inoculation and eschar → intracellular invasion/replication → lymphatic and hematogenous dissemination → endothelial and mononuclear-phagocyte infection → interferon- and cytokine-rich inflammation plus endothelial dysfunction → capillary leak, microvascular injury, tissue hypoxia, and organ-specific inflammation → pneumonitis/ARDS, hepatitis, myocarditis/shock, AKI, meningoencephalitis, or multiorgan failure.**

### Cells and pathways

*Orientia* preferentially infects **endothelial cells**, but dendritic cells, monocytes, and macrophages are also involved. Suggested Cell Ontology mappings are endothelial cell, monocyte, macrophage, dendritic cell, and microglial cell; suggested GO biological processes include *response to bacterium*, *inflammatory response*, *type I interferon signaling*, *cytokine-mediated signaling*, *apoptotic process*, *leukocyte activation*, and *regulation of vascular permeability*. (lynnette2024scrubtyphusdiagnostics pages 1-2, tantibhedhyangkul2011orientiatsutsugamushistimulates pages 1-2)

**Human/in-vitro transcriptomics:** Infection altered more than **4,500 genes** in healthy-donor monocytes, upregulating type-I-interferon and interferon-stimulated genes, M1-polarization features, and apoptosis-related genes. Patient mononuclear cells showed **613 upregulated genes**, including interferon-related signatures. The authors’ abstract concluded that “interferon-mediated activation of monocytes and their subsequent polarization into an M1 phenotype appear critical.” (tantibhedhyangkul2011orientiatsutsugamushistimulates pages 1-2)

**Endothelial dual RNA-seq:** Karp-infected HUVECs showed IL33 approximately **5.1 log-fold** higher than UT176-infected cells and activation of IL33–NOS3–FAS-associated anoikis, while UT176 favored IL6-mediated inflammation. Mouse validation linked these strain-specific programs to relative virulence. (mikagospodorz2020dualrnaseqof pages 9-9)

**Neuropathogenesis—mouse and in-vitro evidence:** The 2023 brain RNA-seq study found enrichment of IFN responses, defense against bacteria, immunoglobulin-mediated immunity, **IL-6/JAK–STAT**, and **TNF/NF-κB** signaling, accompanied by blood–brain-barrier-disruption genes and activated, cytokine-producing microglia. Its abstract states that the work highlights “excessive IFN responses, microglial activation, and BBB dysregulation.” These results are mechanistically persuasive but remain predominantly murine and require human CNS validation. (liang2023braintranscriptomicsreveal pages 1-2)

No consistent disease-specific epigenomic, lipidomic, or clinically validated metabolomic signature was identified. Single-cell and spatial-transcriptomic evidence remains limited. No CRISPR-based host-dependency screen has yet produced an actionable therapeutic target in the retrieved evidence.

## 7. Anatomical structures affected

The **skin** is the inoculation site and eschar location. Dissemination affects vascular endothelium throughout the body. Major secondary organs are the **lungs, liver, heart, kidneys, brain/meninges, spleen, lymph nodes, and bone marrow/blood**. Suggested UBERON mappings include skin, blood vessel endothelium, lung, liver, heart, kidney, brain, meninges, spleen, and lymph node. No characteristic lateralization exists. (vashishtha2025scrubtyphusupdate pages 6-7, varghese2023intravenousdoxycyclineazithromycin pages 4-6)

At the subcellular level, *Orientia* is cytosolic after host-cell entry and escape from its vacuole; bacterial ribosomes are pharmacologic targets. No primary human mitochondrial, lysosomal, nuclear, or ER genetic defect underlies disease.

## 8. Temporal development

Onset may occur in children or adults and is **acute**, not congenital. After 6–21 days of incubation, fever and systemic symptoms begin; rash may emerge near the end of week 1. Untreated disease can broaden during week 2 into pulmonary, neurologic, cardiac, renal, or hepatic complications. (vashishtha2025scrubtyphusupdate pages 6-7, ravishankar2024rickettsialinfectionsprevalence pages 4-5)

The clinically important intervention window is early febrile illness, before organ dysfunction. PCR is most useful during early bacteremia; serologic sensitivity rises later. Effective antibiotics typically produce defervescence over the following days. Relapse or persistent infection can occur, but chronic symptomatic lifelong disease is not the usual course. In an intradermally infected mouse model, viable organisms or the 47-kDa target remained detectable in organs through **84 days**, showing biological persistence even after acute illness; human significance remains incompletely defined.

## 9. Inheritance and population epidemiology

There is no Mendelian inheritance, penetrance, expressivity, anticipation, germline mosaicism, founder effect, or carrier state. Population differences principally reflect ecology, occupation, surveillance, healthcare access, and circulating strain/vector distributions.

Approximately **2 billion** people are considered at risk and roughly **1 million annual cases** are commonly cited. These are modeled/legacy estimates rather than complete surveillance counts. (lynnette2024scrubtyphusdiagnostics pages 1-2)

A 2025 systematic review covering India from 2003–2023 identified **47,650 cases** and a **5% case-fatality rate among 35,243 evaluable cases**, with notable increases after 2010 and peaks in 2019 and 2022. Although published in 2025, its observation window supplies recent 2023 epidemiology. (chaturvedi2025spatiotemporalepidemiologyand pages 2-3)

A completed South India cohort enrolled **32,566** people across approximately 40 villages and monitored symptomatic, serologic, and complicated infections through two seasons, while also trapping rodents to characterize spatial-temporal risk. (NCT04506944 chunk 1, NCT04506944 chunk 2)

## 10. Diagnostics

### Clinical suspicion and criteria

Suspect scrub typhus in an endemic-area resident or traveler with acute fever, headache/myalgia, thrombocytopenia or transaminitis, an eschar, or unexplained pulmonary, neurologic, renal, cardiac, or hepatic dysfunction. The eschar is highly informative but not invariably present and may be concealed. There is no universally standardized clinical case definition.

### Laboratory methods

1. **PCR/qPCR:** detects *Orientia* DNA and is most useful early, before antibiotics reduce bacteremia. Eschar material can remain highly productive; one recent editorial summarized **100% positivity in eschar samples and 94% in buffy coat** in highlighted work. Targets include 47-kDa, 56-kDa/TSA, and other conserved loci; claims of “100% detection” for individual target sets should not be generalized across settings. (ravishankar2024rickettsialinfectionsprevalence pages 7-8, adhikari2024editorialscrubtyphus pages 2-3)
2. **IgM ELISA:** practical and widely implemented; becomes more useful after antibodies develop. Endemic-background antibodies and locally inappropriate cutoffs can cause false positives.
3. **Indirect immunofluorescence assay:** commonly treated as a reference serologic method, but dependence on subjective interpretation, paired sera, antigen panels, and locally validated cutoffs limits standardization. Prototype Karp/Gilliam/Kato antigens may miss local diversity. (lynnette2024scrubtyphusdiagnostics pages 1-2, chaturvedi2025spatiotemporalepidemiologyand pages 2-3)
4. **Rapid immunochromatographic tests:** useful near the point of care but variable; one review cited approximately **70% sensitivity**. (chaturvedi2025spatiotemporalepidemiologyand pages 2-3)
5. **Weil–Felix:** inexpensive but insufficiently sensitive/specific and should not be preferred where validated ELISA/PCR is available; nevertheless, it accounted for about **61%** of tests in the India literature synthesis, illustrating a real-world implementation gap. (chaturvedi2025spatiotemporalepidemiologyand pages 7-8)
6. **Metagenomic sequencing:** potentially useful in atypical or diagnostically unresolved cases, but cost and infrastructure preclude routine use.

QuEST (**NCT06675110**) enrolled **345** participants in Thailand beginning July 17, 2024 to compare insulated isothermal PCR with qPCR/IFA, directly addressing decentralized rapid molecular diagnosis. (NCT06675110 chunk 1)

Imaging, ECG/echocardiography, EEG, CSF examination, renal/liver tests, and chest imaging assess complications rather than establish etiology. Biopsy is rarely necessary; pathology may show endothelial infection, perivascular inflammation, interstitial pneumonitis, and focal necrosis.

### Differential diagnosis and screening

Differentials include dengue, malaria, leptospirosis, enteric fever, murine/spotted-fever rickettsioses, hantavirus, viral hepatitis, influenza/COVID-19, bacterial sepsis, and meningoencephalitis. No population, newborn, carrier, prenatal, or genetic screening is indicated. Targeted fever surveillance in endemic seasons is the appropriate public-health analogue.

## 11. Outcome and prognosis

Early appropriate antibiotics usually produce full recovery. Delay permits multiorgan dysfunction and increases ICU use and death. In severe trial participants, organ involvement was respiratory **62%**, hepatic **54%**, cardiovascular **42%**, renal **30%**, and neurologic **20%**. Trial-defined severe disease included hypoxemia/infiltrates, bilirubin >2 mg/dL, creatinine >2 mg/dL, hypotension/myocarditis/arrhythmia, seizures or meningoencephalitis, or profound thrombocytopenia. (varghese2023intravenousdoxycyclineazithromycin pages 4-6, varghese2023intravenousdoxycyclineazithromycin pages 21-23)

Despite treatment, 28-day mortality in INTREST was **11% with doxycycline, 12% with azithromycin, and 13% with combination therapy**. Thus, combination therapy improved the composite recovery endpoint but did not establish lower mortality. Adverse prognostic features include delayed therapy, shock, ARDS, myocarditis, AKI, encephalopathy, high organism burden, and multiple-organ involvement. (varghese2023intravenousdoxycyclineazithromycin pages 10-11, varghese2023intravenousdoxycyclineazithromycin pages 21-23)

Five- or ten-year survival metrics are not meaningful for this acute infection. Standardized long-term disability and quality-of-life data are sparse.

## 12. Treatment

### Uncomplicated disease

**Doxycycline** is the conventional first-line agent; **azithromycin** is an effective alternative and is generally favored in pregnancy. Chloramphenicol is effective but limited by marrow toxicity and pregnancy/infant concerns. Rifampicin can be active but should be used cautiously where tuberculosis is prevalent because monotherapy can select rifampicin resistance. Fluoroquinolones are not dependable first-line agents. Supportive management includes oxygen/ventilation, hemodynamic support, renal replacement where needed, seizure management, and correction of fluid/electrolyte disturbances. (ravishankar2024rickettsialinfectionsprevalence pages 7-8, chaturvedi2025spatiotemporalepidemiologyand pages 2-3)

### Severe disease: high-quality randomized evidence

INTREST was a multicenter, double-blind RCT in **794 modified-intention-to-treat patients aged ≥15 years** with at least one involved organ system. Regimens were:

- IV doxycycline **200 mg twice on day 1, then 100 mg twice daily for 6 days**;
- IV azithromycin **500 mg twice on day 1, then 500 mg daily for 6 days**;
- both regimens together for 7 days. (varghese2023intravenousdoxycyclineazithromycin pages 6-8)

The primary composite occurred in **33%** with combination therapy versus **47%** with doxycycline (risk difference −13.3 percentage points; 95% CI −21.6 to −5.1; *P*=0.002) and **48%** with azithromycin (−14.8 points; 95% CI −23.1 to −6.5; *P*<0.001). Monotherapies did not differ (*P*=0.73). The abstract’s conclusion was: “Combination therapy with intravenous doxycycline and azithromycin was a better therapeutic option.” (varghese2023intravenousdoxycyclineazithromycin pages 4-6)

Bacterial-DNA clearance was faster with combination therapy than doxycycline alone (HR **1.33**, 95% CI 1.09–1.62). Grade ≥3 adverse events occurred in approximately **8–11%** and were broadly similar across groups. The trial excluded children and pregnant patients, limiting direct generalization. DOI: **10.1056/NEJMoa2208449**, published March 2023; Clinical Trials Registry–India **CTRI/2018/08/015159**. (varghese2023intravenousdoxycyclineazithromycin pages 10-11)

Suggested NCIT annotations: doxycycline treatment, azithromycin treatment, combination antimicrobial therapy, intravenous administration, supportive care, mechanical ventilation, renal replacement therapy.

### Experimental/current studies

- **START, NCT03083197:** 177 participants; 7-day doxycycline versus 3-day doxycycline versus 3-day azithromycin; outcomes include fever clearance, relapse, PK/PD, MIC, WGS, and immune responses; active, not recruiting. (NCT03083197 chunk 1)
- **NCT07513103:** 27 adults; IV tigecycline (100-mg loading dose, then 50 mg every 12 hours for 5 days) versus oral doxycycline 100 mg every 12 hours for 7 days; completed January 2025, but definitive efficacy results were unavailable. (NCT07513103 chunk 1)
- **NCT00351182:** 92 adults with mild/moderate disease; five days of telithromycin 800 mg/day versus doxycycline 200 mg/day; completed. Telithromycin is not a routine preferred option. (NCT00351182 chunk 1)

There is no role for gene, cell, RNA, or immune-checkpoint therapy.

## 13. Prevention

No licensed broadly effective vaccine is available. Primary prevention comprises long trousers and sleeves, boots, repellents, avoidance of sitting directly on infested ground, vegetation management, and targeted vector-control measures. Because chiggers and small mammals occupy complex ecosystems, broad rodent eradication or indiscriminate insecticide use is unlikely to be sustainable.

Secondary prevention is rapid case recognition, regionally validated testing, and prompt empiric treatment when clinical suspicion is high. Tertiary prevention is early monitoring and treatment of hypoxemia, shock, renal failure, myocarditis, thrombocytopenia, and CNS disease. Routine antibiotic prophylaxis is not recommended for general populations, and there is no genetic counseling indication. (vashishtha2025scrubtyphusupdate pages 11-12, adhikari2024editorialscrubtyphus pages 2-3)

Vaccine development is hampered by marked strain diversity and incompletely durable heterologous immunity. Conserved antigens, multivalent constructs, and T-cell-focused strategies remain research priorities rather than current implementations.

## 14. Other species and natural disease

The natural cycle involves trombiculid mites and small mammals, especially rodents and shrews. Mites are both vectors and long-term maintenance hosts; mammals provide blood meals and ecological amplification. Humans are accidental hosts and scrub typhus is therefore zoonotic/vector-borne, but not normally transmitted directly from rodents or person to person. (lynnette2024scrubtyphusdiagnostics pages 1-2, NCT02876367 chunk 1)

Field study NCT02876367 enrolled approximately **1,200** participants and linked human, rodent, and mite *Orientia* genotypes to habitats using sequencing. This provides a real-world One Health implementation for identifying key hosts, vectors, and intervention sites. (NCT02876367 chunk 1)

Clinically recognized natural disease is chiefly human; overt scrub-typhus-like illness in domestic animal breeds is not well established. VBO breed annotation and orthologous human causal genes are therefore not applicable. NCBI Taxonomy identifiers should be assigned directly from current taxonomy records for *O. tsutsugamushi*, individual *Leptotrombidium* species, and locally sampled rodent species.

## 15. Model organisms

### Mouse models

Intradermal inoculation of C57BL/6 mice more closely approximates natural cutaneous entry than intraperitoneal or intravenous challenge. After ear inoculation with **6×10⁴ organisms**, mice developed fever at days 11–12, hypothermia/weight loss at days 14–19, and peak bacteremia, tissue burden, and pathology near day 14. Cytokines included CCL2, CCL3, IL-10, IL-6, IL-12, IFN-γ, CCL5, IL-1, TNF-α, and GM-CSF; organisms remained detectable through day 84. The model supports studies of acute disease, persistence, immunity, and vaccines, but it does not consistently reproduce the human eschar and differs in immune kinetics.

The 2023 severe-mouse model with brain RNA-seq recapitulates neuroinflammation, microglial activation, and BBB dysregulation, making it useful for neurologic pathogenesis but not a substitute for human CNS tissue evidence. (liang2023braintranscriptomicsreveal pages 1-2)

### Nonhuman primates and cellular systems

Nonhuman primates can model eschar, fever, lymphadenopathy, and immune responses more faithfully, but cost, ethics, and limited availability constrain use. HUVEC/endothelial cultures, primary monocytes/macrophages, dendritic cells, and microglia permit mechanistic and drug studies. Their limitations include high experimental inocula, absent tissue architecture, and inability to reproduce systemic vascular disease. (mikagospodorz2020dualrnaseqof pages 9-9, tantibhedhyangkul2011orientiatsutsugamushistimulates pages 1-2)

## Recent developments and expert interpretation

1. **Therapy:** The 2023 INTREST RCT is practice-changing for severe disease: dual IV doxycycline–azithromycin accelerates recovery compared with either alone, although equal mortality cautions against claiming a survival advantage. (varghese2023intravenousdoxycyclineazithromycin pages 10-11, varghese2023intravenousdoxycyclineazithromycin pages 4-6)
2. **Mechanisms:** The 2023 mouse brain-transcriptomics study links severe neurologic disease to excessive IFN activity, microglia, IL-6/JAK–STAT, TNF/NF-κB, and BBB disruption. This supplies testable mechanisms but not yet validated therapeutic targets. (liang2023braintranscriptomicsreveal pages 1-2)
3. **Diagnostics:** The 2024 diagnostic literature emphasizes a stage-adapted strategy—PCR early, serology later—and locally validated antigen panels/cutoffs. QuEST represents current implementation research on field-compatible iiPCR. (lynnette2024scrubtyphusdiagnostics pages 1-2, NCT06675110 chunk 1)
4. **Epidemiology:** Current authoritative opinion favors a One Health, spatially targeted response incorporating rainfall, temperature, land use, rodents, mites, and healthcare access rather than treating scrub typhus solely as a clinical rickettsiosis. (adhikari2024editorialscrubtyphus pages 2-3, NCT04506944 chunk 1)

## Evidence and identifier caveats

PMIDs were requested, but the retrieved full-text records supplied DOIs and registry identifiers more consistently than PMIDs. To prevent database contamination, PMIDs not explicitly available in the evidence were not guessed. Exact MONDO, HPO, GO, CL, UBERON, CHEBI, and NCIT numerical identifiers likewise require validation against the current ontology releases; the report therefore supplies defensible term labels and only the independently supported ICD-10 code. Frequencies vary sharply by geography, case definition, disease severity, test timing, and referral setting; severe-hospital cohorts must not be used as population prevalence estimates.

References

1. (lynnette2024scrubtyphusdiagnostics pages 1-2): S. Cheryl Lynnette, Trishna Bora, Susmitha Perumalla, G. Karthick, Babban Jee, Gaurav Batra, M. Biswal, S. A. Khan, and J. A. J. Prakash. Scrub typhus diagnostics: the present and the future. Zoonoses, Jan 2024. URL: https://doi.org/10.15212/zoonoses-2023-0028, doi:10.15212/zoonoses-2023-0028. This article has 4 citations.

2. (adhikari2024editorialscrubtyphus pages 2-3): Prabhat Adhikari, Archana Shrestha, Suzanne M. Donovan, and Janak Koirala. Editorial: scrub typhus & its changing dynamics. Frontiers in Tropical Diseases, Nov 2024. URL: https://doi.org/10.3389/fitd.2024.1511950, doi:10.3389/fitd.2024.1511950. This article has 2 citations.

3. (ravishankar2024rickettsialinfectionsprevalence pages 4-5): Vigneshwaran Ravishankar, Shridhar Narayanan, and Radha Krishan Shandil. Rickettsial infections: prevalence and diagnosis of scrub typhus in india. Frontiers in Tropical Diseases, Sep 2024. URL: https://doi.org/10.3389/fitd.2024.1433013, doi:10.3389/fitd.2024.1433013. This article has 11 citations.

4. (varghese2023intravenousdoxycyclineazithromycin pages 4-6): George M. Varghese, Divya Dayanand, Karthik Gunasekaran, Debasree Kundu, Mukta Wyawahare, Navneet Sharma, Dhruva Chaudhry, Sanjay K. Mahajan, Kavitha Saravu, Blessed W. Aruldhas, Binu S. Mathew, Roshini G. Nair, Nalini Newbigging, Aswathy Mathew, Kundavaram P.P. Abhilash, Manisha Biswal, Ann H. Prasad, Anand Zachariah, Ramya Iyadurai, Samuel G. Hansdak, Sowmya Sathyendra, Thambu D. Sudarsanam, John A.J. Prakash, Abi Manesh, Alladi Mohan, Joel Tarning, Stuart D. Blacksell, Pimnara Peerawaranun, Naomi Waithira, Mavuto Mukaka, Phaik Yeong Cheah, John V. Peter, Ooriapadickal C. Abraham, and Nicholas P.J. Day. Intravenous doxycycline, azithromycin, or both for severe scrub typhus. The New England journal of medicine, 388 9:792-803, Mar 2023. URL: https://doi.org/10.1056/nejmoa2208449, doi:10.1056/nejmoa2208449. This article has 125 citations and is from a highest quality peer-reviewed journal.

5. (varghese2023intravenousdoxycyclineazithromycin pages 21-23): George M. Varghese, Divya Dayanand, Karthik Gunasekaran, Debasree Kundu, Mukta Wyawahare, Navneet Sharma, Dhruva Chaudhry, Sanjay K. Mahajan, Kavitha Saravu, Blessed W. Aruldhas, Binu S. Mathew, Roshini G. Nair, Nalini Newbigging, Aswathy Mathew, Kundavaram P.P. Abhilash, Manisha Biswal, Ann H. Prasad, Anand Zachariah, Ramya Iyadurai, Samuel G. Hansdak, Sowmya Sathyendra, Thambu D. Sudarsanam, John A.J. Prakash, Abi Manesh, Alladi Mohan, Joel Tarning, Stuart D. Blacksell, Pimnara Peerawaranun, Naomi Waithira, Mavuto Mukaka, Phaik Yeong Cheah, John V. Peter, Ooriapadickal C. Abraham, and Nicholas P.J. Day. Intravenous doxycycline, azithromycin, or both for severe scrub typhus. The New England journal of medicine, 388 9:792-803, Mar 2023. URL: https://doi.org/10.1056/nejmoa2208449, doi:10.1056/nejmoa2208449. This article has 125 citations and is from a highest quality peer-reviewed journal.

6. (varghese2023intravenousdoxycyclineazithromycin pages 8-10): George M. Varghese, Divya Dayanand, Karthik Gunasekaran, Debasree Kundu, Mukta Wyawahare, Navneet Sharma, Dhruva Chaudhry, Sanjay K. Mahajan, Kavitha Saravu, Blessed W. Aruldhas, Binu S. Mathew, Roshini G. Nair, Nalini Newbigging, Aswathy Mathew, Kundavaram P.P. Abhilash, Manisha Biswal, Ann H. Prasad, Anand Zachariah, Ramya Iyadurai, Samuel G. Hansdak, Sowmya Sathyendra, Thambu D. Sudarsanam, John A.J. Prakash, Abi Manesh, Alladi Mohan, Joel Tarning, Stuart D. Blacksell, Pimnara Peerawaranun, Naomi Waithira, Mavuto Mukaka, Phaik Yeong Cheah, John V. Peter, Ooriapadickal C. Abraham, and Nicholas P.J. Day. Intravenous doxycycline, azithromycin, or both for severe scrub typhus. The New England journal of medicine, 388 9:792-803, Mar 2023. URL: https://doi.org/10.1056/nejmoa2208449, doi:10.1056/nejmoa2208449. This article has 125 citations and is from a highest quality peer-reviewed journal.

7. (chaturvedi2025spatiotemporalepidemiologyand pages 7-8): Rini Chaturvedi, S. Hussain, Hayavadhan Sampath, M. Rahi, B. R. Mirdha, and Amit Sharma. Spatiotemporal epidemiology and clinical manifestations of two decades of scrub typhus in india: a systematic review and meta-analysis. BMJ Global Health, Aug 2025. URL: https://doi.org/10.1136/bmjgh-2025-018998, doi:10.1136/bmjgh-2025-018998. This article has 10 citations and is from a peer-reviewed journal.

8. (liang2023braintranscriptomicsreveal pages 1-2): Yuejin Liang, Aditi, Florence Onyoni, Hui Wang, Casey Gonzales, Piyanate Sunyakumthorn, Ping Wu, Parimal Samir, and Lynn Soong. Brain transcriptomics reveal the activation of neuroinflammation pathways during acute orientia tsutsugamushi infection in mice. Frontiers in Immunology, Jun 2023. URL: https://doi.org/10.3389/fimmu.2023.1194881, doi:10.3389/fimmu.2023.1194881. This article has 16 citations and is from a peer-reviewed journal.

9. (vashishtha2025scrubtyphusupdate pages 6-7): Ankur Vashishtha, Vivek Kumar, Gautam Panwar, Gaurav Kausik, Samaniya Baig, Prigya Sharma, and Rajesh Yadav. Scrub typhus update: a re‑emerging global threat beyond the tsutsugamushi triangle and the physiological ramifications of scrub typhus infection (review). World Academy of Sciences Journal, Feb 2025. URL: https://doi.org/10.3892/wasj.2025.322, doi:10.3892/wasj.2025.322. This article has 15 citations.

10. (mikagospodorz2020dualrnaseqof pages 9-9): Bozena Mika-Gospodorz, Suparat Giengkam, Alexander J. Westermann, Jantana Wongsantichon, Willow Kion-Crosby, Suthida Chuenklin, Loo Chien Wang, Piyanate Sunyakumthorn, Radoslaw M. Sobota, Selvakumar Subbian, Jörg Vogel, Lars Barquist, and Jeanne Salje. Dual rna-seq of orientia tsutsugamushi informs on host-pathogen interactions for this neglected intracellular human pathogen. Nature Communications, Jul 2020. URL: https://doi.org/10.1038/s41467-020-17094-8, doi:10.1038/s41467-020-17094-8. This article has 67 citations and is from a highest quality peer-reviewed journal.

11. (tantibhedhyangkul2011orientiatsutsugamushistimulates pages 1-2): Wiwit Tantibhedhyangkul, Thanavadee Prachason, Duangdao Waywa, Adil El Filali, Eric Ghigo, Wanna Thongnoppakhun, Didier Raoult, Yupin Suputtamongkol, Christian Capo, Chanin Limwongse, and Jean-Louis Mege. Orientia tsutsugamushi stimulates an original gene expression program in monocytes: relationship with gene expression in patients with scrub typhus. PLoS Neglected Tropical Diseases, 5:e1028, May 2011. URL: https://doi.org/10.1371/journal.pntd.0001028, doi:10.1371/journal.pntd.0001028. This article has 85 citations and is from a domain leading peer-reviewed journal.

12. (chaturvedi2025spatiotemporalepidemiologyand pages 2-3): Rini Chaturvedi, S. Hussain, Hayavadhan Sampath, M. Rahi, B. R. Mirdha, and Amit Sharma. Spatiotemporal epidemiology and clinical manifestations of two decades of scrub typhus in india: a systematic review and meta-analysis. BMJ Global Health, Aug 2025. URL: https://doi.org/10.1136/bmjgh-2025-018998, doi:10.1136/bmjgh-2025-018998. This article has 10 citations and is from a peer-reviewed journal.

13. (NCT06675110 chunk 1):  QuEST - Quick and Easy Scrub Typhus Diagnostic Tools. University of Oxford. 2024. ClinicalTrials.gov Identifier: NCT06675110

14. (varghese2023intravenousdoxycyclineazithromycin pages 6-8): George M. Varghese, Divya Dayanand, Karthik Gunasekaran, Debasree Kundu, Mukta Wyawahare, Navneet Sharma, Dhruva Chaudhry, Sanjay K. Mahajan, Kavitha Saravu, Blessed W. Aruldhas, Binu S. Mathew, Roshini G. Nair, Nalini Newbigging, Aswathy Mathew, Kundavaram P.P. Abhilash, Manisha Biswal, Ann H. Prasad, Anand Zachariah, Ramya Iyadurai, Samuel G. Hansdak, Sowmya Sathyendra, Thambu D. Sudarsanam, John A.J. Prakash, Abi Manesh, Alladi Mohan, Joel Tarning, Stuart D. Blacksell, Pimnara Peerawaranun, Naomi Waithira, Mavuto Mukaka, Phaik Yeong Cheah, John V. Peter, Ooriapadickal C. Abraham, and Nicholas P.J. Day. Intravenous doxycycline, azithromycin, or both for severe scrub typhus. The New England journal of medicine, 388 9:792-803, Mar 2023. URL: https://doi.org/10.1056/nejmoa2208449, doi:10.1056/nejmoa2208449. This article has 125 citations and is from a highest quality peer-reviewed journal.

15. (vashishtha2025scrubtyphusupdate pages 11-12): Ankur Vashishtha, Vivek Kumar, Gautam Panwar, Gaurav Kausik, Samaniya Baig, Prigya Sharma, and Rajesh Yadav. Scrub typhus update: a re‑emerging global threat beyond the tsutsugamushi triangle and the physiological ramifications of scrub typhus infection (review). World Academy of Sciences Journal, Feb 2025. URL: https://doi.org/10.3892/wasj.2025.322, doi:10.3892/wasj.2025.322. This article has 15 citations.

16. (ravishankar2024rickettsialinfectionsprevalence pages 7-8): Vigneshwaran Ravishankar, Shridhar Narayanan, and Radha Krishan Shandil. Rickettsial infections: prevalence and diagnosis of scrub typhus in india. Frontiers in Tropical Diseases, Sep 2024. URL: https://doi.org/10.3389/fitd.2024.1433013, doi:10.3389/fitd.2024.1433013. This article has 11 citations.

17. (NCT02876367 chunk 1):  The Clinical Epidemiology of Scrub Typhus in Humans, Chiggers and Rodents. University of Oxford. 2016. ClinicalTrials.gov Identifier: NCT02876367

18. (NCT03083197 chunk 1):  Scrub Typhus Antibiotic Resistance Trial. University of Oxford. 2017. ClinicalTrials.gov Identifier: NCT03083197

19. (NCT04506944 chunk 1):  The Epidemiology of Rickettsial Infections in South India: Cohort Study. London School of Hygiene and Tropical Medicine. 2020. ClinicalTrials.gov Identifier: NCT04506944

20. (NCT04506944 chunk 2):  The Epidemiology of Rickettsial Infections in South India: Cohort Study. London School of Hygiene and Tropical Medicine. 2020. ClinicalTrials.gov Identifier: NCT04506944

21. (varghese2023intravenousdoxycyclineazithromycin pages 10-11): George M. Varghese, Divya Dayanand, Karthik Gunasekaran, Debasree Kundu, Mukta Wyawahare, Navneet Sharma, Dhruva Chaudhry, Sanjay K. Mahajan, Kavitha Saravu, Blessed W. Aruldhas, Binu S. Mathew, Roshini G. Nair, Nalini Newbigging, Aswathy Mathew, Kundavaram P.P. Abhilash, Manisha Biswal, Ann H. Prasad, Anand Zachariah, Ramya Iyadurai, Samuel G. Hansdak, Sowmya Sathyendra, Thambu D. Sudarsanam, John A.J. Prakash, Abi Manesh, Alladi Mohan, Joel Tarning, Stuart D. Blacksell, Pimnara Peerawaranun, Naomi Waithira, Mavuto Mukaka, Phaik Yeong Cheah, John V. Peter, Ooriapadickal C. Abraham, and Nicholas P.J. Day. Intravenous doxycycline, azithromycin, or both for severe scrub typhus. The New England journal of medicine, 388 9:792-803, Mar 2023. URL: https://doi.org/10.1056/nejmoa2208449, doi:10.1056/nejmoa2208449. This article has 125 citations and is from a highest quality peer-reviewed journal.

22. (NCT07513103 chunk 1): Jin Soo Lee. Clinical Effectiveness of Tigecycline for Scrub Typhus.. Jin Soo Lee. 2022. ClinicalTrials.gov Identifier: NCT07513103

23. (NCT00351182 chunk 1): Dong-Min Kim. Controlled Trial: 5-day Course of Telithromycin Versus Doxycycline for the Treatment of Mild to Moderate Scrub Typhus. Dong-Min Kim. 2005. ClinicalTrials.gov Identifier: NCT00351182

## Artifacts

- [Edison artifact artifact-00](Scrub_Typhus-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.