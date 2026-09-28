---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-25T19:51:53.002250'
end_time: '2026-08-25T20:07:36.201321'
duration_seconds: 943.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 101 (Varicella Zoster Virus-Specific)
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
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
  path: Immunodeficiency_101_Varicella_Zoster_Virus-specific-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 101 (Varicella Zoster Virus-Specific)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 101 (Varicella Zoster Virus-Specific)** covering all of the
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
- **Disease Name:** Immunodeficiency 101 (Varicella Zoster Virus-Specific)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 101 (Varicella Zoster Virus-Specific)** covering all of the
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


# Immunodeficiency 101 (Varicella-Zoster Virus–Specific): Disease Characteristics Report

## Executive summary and evidence limitations

**Immunodeficiency 101, varicella-zoster virus–specific** is best mapped to an ultra-rare, Mendelian, selective susceptibility to severe varicella-zoster virus (VZV) disease caused by a monoallelic **POLR3F** defect. The defining report described two monozygotic adult female twins with recurrent VZV-associated central nervous system (CNS) vasculitis and a heterozygous **POLR3F c.25C>T (p.Arg50Trp; R50W)** variant. Patient peripheral-blood mononuclear cells (PBMCs) had deficient responses to AT-rich DNA and increased VZV replication, connecting the genotype to impaired RNA polymerase III (Pol III) antiviral sensing. This is distinct from the broader group of Pol III–related VZV susceptibilities caused by **POLR3A, POLR3C,** or **POLR3E** variants. (cartertimofte2018varicellazosterviruscns pages 6-8, cartertimofte2018varicellazosterviruscns pages 4-5, ansari2021primaryandacquired pages 5-6)

The evidence base is exceptionally small: **two molecularly confirmed POLR3F-affected individuals from one family**. Consequently, phenotype frequencies, penetrance, prevalence, survival, treatment-response rates, sex ratio, and genotype–phenotype correlations cannot be estimated reliably. No clearly documented additional POLR3F-specific cases were found in the retrieved 2023–2024 literature. Most disease-specific evidence is therefore human case-level evidence supplemented by ex vivo PBMC studies and broader VZV/Pol III reviews.

| Topic | Key finding | Evidence type | Key publication / DOI |
|---|---|---|---|
| Disease identity | Best-mapped entity is a Mendelian, selective susceptibility to severe VZV disease caused by monoallelic POLR3F deficiency; reported presentation is recurrent VZV CNS vasculitis/meningoencephalitis rather than broad combined immunodeficiency. No confirmed MONDO/OMIM identifier was established from retrieved sources. (cartertimofte2018varicellazosterviruscns pages 6-8, cartertimofte2018varicellazosterviruscns pages 4-5) | Human case report + review | Carter-Timofte et al., 2018, *Neurol Neuroimmunol Neuroinflamm*; DOI: https://doi.org/10.1212/NXI.0000000000000500 |
| Causal gene / variant | Causal gene: **POLR3F** (RNA polymerase III subunit F). Reported disease-associated variant: **c.25C>T, p.Arg50Trp (R50W)**, heterozygous; predicted damaging with CADD 25.8; biochemical work suggested preserved expression/solubility, implying functional rather than stability defect. (cartertimofte2018varicellazosterviruscns pages 4-5) | Human genetics + ex vivo functional follow-up | Carter-Timofte et al., 2018; DOI: https://doi.org/10.1212/NXI.0000000000000500 |
| Inheritance | Evidence supports **autosomal dominant / monoallelic susceptibility** with likely **incomplete penetrance**: the variant was present in both affected monozygotic twins and inherited from the father, who reportedly had a prior stroke possibly related to VZV vasculitis. (cartertimofte2018varicellazosterviruscns pages 4-5, cartertimofte2018rnapolymeraseiii pages 6-8) | Family segregation + expert review | Carter-Timofte et al., 2018; DOI: https://doi.org/10.1212/NXI.0000000000000500; Carter-Timofte et al., 2018 review; DOI: https://doi.org/10.1016/j.molmed.2018.07.009 |
| Reported patients | Confirmed POLR3F-specific cases in retrieved evidence: **2 monozygotic adult female twins**, both age 37 in review summaries, with recurrent VZV CNS vasculitis due to reactivation. No additional clearly documented POLR3F cases were identified in retrieved 2023–2024 literature. (cartertimofte2018varicellazosterviruscns pages 6-8, cartertimofte2018rnapolymeraseiii pages 6-8) | Human case report + review synthesis | Carter-Timofte et al., 2018; DOI: https://doi.org/10.1212/NXI.0000000000000500 |
| Core phenotype | Recurrent stroke-like CNS disease with **headache, dizziness, hemiparesis/sensory deficits**, CSF pleocytosis and intrathecal anti-VZV antibody production, and brain MRI ischemic lesions; one summary also notes myelitis and parietal/juxtacortical lesions. Patients reportedly had normal childhood varicella and no unusual susceptibility to other infections. (cartertimofte2018varicellazosterviruscns pages 6-8, cartertimofte2018varicellazosterviruscns pages 3-4, cartertimofte2018varicellazosterviruscns pages 4-5) | Human clinical phenotype | Carter-Timofte et al., 2018; DOI: https://doi.org/10.1212/NXI.0000000000000500 |
| Diagnostic findings | Supportive findings included **CSF pleocytosis**, **intrathecal VZV IgG production**, VZV CNS vasculitis-compatible MRI ischemic lesions, and normal routine immune workup (normal immunoglobulins, lymphocyte distribution/proliferation, HIV negative). Broader VZV vasculopathy literature emphasizes that CSF anti-VZV IgG is often more sensitive than PCR and that negative PCR does not exclude disease. (cartertimofte2018varicellazosterviruscns pages 6-8, cartertimofte2018varicellazosterviruscns pages 3-4, cartertimofte2018varicellazosterviruscns pages 4-5) | Human case report + disease review | Carter-Timofte et al., 2018; DOI: https://doi.org/10.1212/NXI.0000000000000500; Nagel & Bubak, 2018; DOI: https://doi.org/10.1093/infdis/jiy425 |
| Functional mechanism | POLR3F deficiency impairs **POL III sensing of AT-rich DNA** and downstream **RIG-I/MAVS/type I and III IFN** responses. Patient PBMCs showed reduced antiviral/inflammatory responses to **poly(dA:dT)** and **increased VZV replication/gene expression** versus controls. Reviews place POLR3F with POLR3A/C/E as Pol III subunits involved in human VZV susceptibility. (cartertimofte2018varicellazosterviruscns pages 6-8, ansari2021primaryandacquired pages 5-6, lata2021rnapolymeraseiii pages 21-22, cartertimofte2018rnapolymeraseiii pages 4-6, cartertimofte2018rnapolymeraseiii pages 6-8) | Human ex vivo immunology + mechanistic reviews | Carter-Timofte et al., 2018; DOI: https://doi.org/10.1212/NXI.0000000000000500; Lata et al., 2021; DOI: https://doi.org/10.3389/fmolb.2021.696438 |
| Acute treatment | In the reported family/case summaries, acute episodes were treated with **intravenous acyclovir 10 mg/kg three times daily for 14 days** plus **prednisolone 50 mg daily for 10 days**. Broader VZV vasculopathy reviews support IV acyclovir as standard acute therapy, with corticosteroids used as adjuncts in selected cases. (cartertimofte2018varicellazosterviruscns pages 3-4, ansari2021primaryandacquired pages 5-6) | Human case report + clinical review | Carter-Timofte et al., 2018; DOI: https://doi.org/10.1212/NXI.0000000000000500; Nagel & Bubak, 2018; DOI: https://doi.org/10.1093/infdis/jiy425 |
| Prophylaxis | Both twins reportedly received **acyclovir prophylaxis**; one twin had symptom recurrence/new white matter lesions after stopping prophylaxis. Expert review further suggested that individuals with POL III defects may benefit from **childhood varicella vaccination, adult zoster vaccination, and acyclovir prophylaxis after severe/recurrent VZV**, but these are opinion-based rather than trial-proven for POLR3F disease. (cartertimofte2018varicellazosterviruscns pages 6-8, cartertimofte2018rnapolymeraseiii pages 10-11) | Human case follow-up + expert opinion | Carter-Timofte et al., 2018; DOI: https://doi.org/10.1212/NXI.0000000000000500; Carter-Timofte et al., 2018 review; DOI: https://doi.org/10.1016/j.molmed.2018.07.009 |
| Epidemiology | **Unknown disease prevalence/incidence.** Retrieved evidence supports only a single affected family (2 confirmed twins). By contrast, the wider Pol III/VZV susceptibility literature includes additional non-POLR3F patients with POLR3A/C/E variants. Thus, POLR3F-related disease appears **ultra-rare**. (cartertimofte2018rnapolymeraseiii pages 6-8, lata2021rnapolymeraseiii pages 21-22, cartertimofte2018varicellazosterviruscns pages 4-5) | Case-based evidence + review synthesis | Carter-Timofte et al., 2018; DOI: https://doi.org/10.1212/NXI.0000000000000500; Lata et al., 2021; DOI: https://doi.org/10.3389/fmolb.2021.696438 |
| Major evidence gaps | No disease-specific prevalence estimates, natural-history cohort, penetrance study, controlled treatment trial, validated biomarker panel, or disease-specific animal model were identified. It remains unclear which cell types are decisive in vivo, whether POL III acts mainly in cytosolic DNA sensing versus nuclear RNA5SP14-related signaling, and how POLR3F defects influence latency/reactivation control. (cartertimofte2018rnapolymeraseiii pages 10-11, kennedy2021recentissuesin pages 8-9, cartertimofte2018varicellazosterviruscns pages 4-5) | Knowledge-gap synthesis from reviews + case report | Carter-Timofte et al., 2018 review; DOI: https://doi.org/10.1016/j.molmed.2018.07.009; Kennedy et al., 2021; DOI: https://doi.org/10.3390/v13102018 |


*Table: This table summarizes the highest-confidence evidence for Immunodeficiency 101 (VZV-specific), best mapped here to POLR3F-related selective susceptibility to severe VZV CNS disease. It highlights what is known from primary human cases and reviews, while clearly marking major unresolved gaps.*

## 1. Disease information

### Definition

This condition is an **inborn error of intrinsic/innate antiviral immunity** in which defective POLR3F-containing RNA polymerase III compromises recognition of the AT-rich VZV genome. Clinically, the reported phenotype is recurrent VZV reactivation in the CNS, causing meningoencephalitis/vasculitis, ischemic lesions, and stroke-like neurologic episodes despite an otherwise normal routine immune evaluation. The patients did not exhibit broad susceptibility to bacterial, fungal, or unrelated viral infections. (cartertimofte2018varicellazosterviruscns pages 1-2, cartertimofte2018varicellazosterviruscns pages 4-5)

### Names and identifiers

- **Preferred label:** Immunodeficiency 101, varicella-zoster virus–specific.
- **Useful synonyms:** POLR3F-related VZV susceptibility; POLR3F deficiency; RNA polymerase III deficiency due to POLR3F; selective susceptibility to severe VZV infection; VZV CNS vasculitis associated with POLR3F mutation.
- **Gene:** **POLR3F**, encoding RNA polymerase III subunit F/RPC6.
- **MONDO, OMIM phenotype, Orphanet:** a stable disease-level identifier could not be verified from the retrieved full-text sources; it should therefore not be inferred from the numbered disease label alone.
- **ICD-10/ICD-11:** no disease-specific code was identified. Component manifestations may be coded as hereditary immunodeficiency, viral encephalitis/meningitis, cerebral vasculitis, or VZV infection, depending on the coding system and confirmed presentation.
- **MeSH:** relevant concepts include *Immunologic Deficiency Syndromes*, *Herpesvirus 3, Human*, *Encephalitis, Viral*, and *Central Nervous System Vasculitis*.

The source is **aggregated disease-level interpretation derived primarily from two individual patients**, not an EHR cohort or population registry.

### Foundational evidence

Carter-Timofte et al., “Varicella-zoster virus CNS vasculitis and RNA polymerase III gene mutation in identical twins,” *Neurology: Neuroimmunology & Neuroinflammation*, volume 5, published November 2018, DOI: [10.1212/NXI.0000000000000500](https://doi.org/10.1212/NXI.0000000000000500). PMID was not available in the retrieved text and is not supplied here to avoid an unverified identifier. (cartertimofte2018varicellazosterviruscns pages 6-8)

A direct abstract statement is: **“The identified R50W POLR3F mutation is predicted by bioinformatics to be damaging, and when tested in functional assays, patient PBMCs exhibited impaired antiviral and inflammatory responses to the POL III agonist poly(dA:dT) and increased viral replication compared with controls.”** (cartertimofte2018varicellazosterviruscns pages 1-2)

## 2. Etiology, risk factors, and protective factors

### Causal factors

The proximal inherited cause is the heterozygous **POLR3F p.Arg50Trp** variant. The necessary infectious trigger is exposure to and subsequent latency/reactivation of **VZV**, a human alphaherpesvirus. Both twins reportedly had ordinary childhood varicella; their severe phenotype emerged later during viral reactivation rather than during primary infection. (cartertimofte2018varicellazosterviruscns pages 3-4, cartertimofte2018varicellazosterviruscns pages 4-5)

### Genetic risk

The reported variant was inherited from the father, who had a previous stroke that the authors considered possibly compatible with VZV CNS vasculitis. This segregation supports autosomal-dominant susceptibility but does not establish complete penetrance. The variant had a reported CADD score of **25.8**, above the cited significance threshold of 13, and was predicted damaging. Its expression and solubility were not materially altered, favoring impaired molecular function rather than protein instability. (cartertimofte2018varicellazosterviruscns pages 4-5)

Other genes—**POLR3A, POLR3C,** and **POLR3E**—cause related Pol III–dependent VZV susceptibility, but they should not be recorded as causal genes for the narrowly defined POLR3F-specific entity. Across the wider syndrome, VZV-associated Pol III variants map mainly near DNA-binding/initiation or catalytic regions, unlike many biallelic variants causing POLR3-related hypomyelinating leukodystrophy. (lata2021rnapolymeraseiii pages 21-22, cartertimofte2018rnapolymeraseiii pages 6-8)

### Environmental and acquired modifiers

VZV infection is indispensable. General factors that impair VZV control—aging, HIV, hematologic disease, transplantation, immunosuppressive drugs, and T/NK-cell deficiencies—can independently increase severe VZV risk, but none was demonstrated as causal in the twins. Their immunoglobulins, lymphocyte distribution/proliferation, and HIV testing were normal. (kennedy2021recentissuesin pages 8-9, cartertimofte2018varicellazosterviruscns pages 4-5)

No disease-specific evidence supports smoking, diet, alcohol, exercise, occupational exposure, toxins, radiation, sex, or ancestry as modifiers.

### Protective factors and gene–environment interaction

Antiviral prophylaxis appeared protective in the reported family: both twins received acyclovir prophylaxis, and one developed recurrent symptoms and new white-matter lesions after discontinuation. Expert review—not controlled trial evidence—suggests varicella vaccination in childhood, recombinant zoster vaccination in adulthood, and antiviral prophylaxis after severe or recurrent CNS disease. (cartertimofte2018varicellazosterviruscns pages 6-8, cartertimofte2018rnapolymeraseiii pages 10-11)

The causal interaction is: **monoallelic POLR3F dysfunction + latent/reactivating VZV → inadequate AT-rich DNA sensing → deficient interferon response → excessive viral replication → CNS arterial infection/inflammation and ischemia**. Ordinary VZV exposure is therefore usually benign in the population but becomes pathogenic in the genetically susceptible host. (cartertimofte2018rnapolymeraseiii pages 6-8, ansari2021primaryandacquired pages 5-6)

## 3. Phenotypes

Because only two twins are confirmed, “2/2” means occurrence in the index family, not a generalizable population frequency.

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Recurrent CNS vasculitis | Clinical diagnosis/sign; adult onset, severe, episodic/relapsing; reported in 2/2 | Cerebral vasculitis; Recurrent meningitis |
| Headache and dizziness | Symptoms during attacks; recurrent and variable | Headache (HP:0002315); Vertigo (HP:0002321) |
| Focal neurologic deficits | Hemiparesis, sensory deficits/paresthesias and stroke-like attacks | Hemiparesis (HP:0001269); Paresthesia (HP:0003401) |
| Cerebral ischemic lesions | MRI abnormality; recurrent/new lesions possible | Cerebral ischemia (HP:0002637); Abnormal brain MRI |
| Myelitis | MRI/clinical manifestation described in one twin, spanning approximately C6–T2 | Myelitis (HP:0012198) |
| CSF pleocytosis | Laboratory abnormality during CNS attacks | CSF pleocytosis (HP:0012227) |
| Intrathecal anti-VZV IgG production | Disease-supporting laboratory biomarker | No highly specific HPO term; use abnormal CSF immunoglobulin/positive pathogen-specific intrathecal antibody |
| Selective severe VZV susceptibility | Immunologic phenotype without broad recurrent infection | Recurrent viral infections (HP:0004429), qualified as VZV-specific |

The reported clinical picture included headache, dizziness, neurologic deficits, CSF pleocytosis with intrathecal VZV antibody production, and ischemic brain lesions. One summary reports paraventricular parietal and bilateral juxtacortical lesions and cervical–upper thoracic myelitis. (cartertimofte2018varicellazosterviruscns pages 1-2, cartertimofte2018varicellazosterviruscns pages 3-4)

Quality-of-life instruments were not administered. Nevertheless, recurrent stroke-like events, hospitalization, neurologic impairment, repeated lumbar puncture/imaging, and chronic antiviral use imply potentially major functional and psychosocial burden. Quantified EQ-5D, SF-36, PROMIS, educational, employment, and caregiver outcomes are unavailable.

## 4. Genetic and molecular information

### Causal gene and variant

- **Gene:** POLR3F.
- **Protein:** RNA polymerase III subunit F/RPC6, part of the Pol III initiation-associated peripheral subcomplex.
- **Reported variant:** **c.25C>T, p.Arg50Trp (R50W)**, heterozygous and germline.
- **Variant class:** missense, monoallelic.
- **Functional interpretation:** loss/hypomorphic impairment of antiviral DNA sensing is supported; a dominant-negative mechanism was not established.
- **Computational evidence:** CADD 25.8 and damaging predictions.
- **Protein studies:** mutant abundance/solubility was reportedly preserved, suggesting altered ligand recognition, initiation, or enzyme activity rather than degradation. (cartertimofte2018varicellazosterviruscns pages 4-5)

The primary paper called the variant novel. A precise modern gnomAD allele count, rsID, ClinVar accession, ACMG/AMP classification, HGNC ID, and transcript version were not established by the retrieved evidence. It should not automatically be labeled “pathogenic” in a clinical database without checking current ClinVar/ClinGen submissions and transcript-specific HGVS normalization. The case data provide strong phenotype, segregation, computational, and functional support but remain limited to one family.

### Broader allelic and mechanistic context

Heterozygous VZV-susceptibility variants reported in the larger Pol III group include POLR3A M307V, R437Q, R582C and Q707R; POLR3C L11F, R84Q and R438G; POLR3E T275M; and POLR3F R50W. POLR3F R50W was associated specifically with adult reactivation and CNS vasculitis, whereas POLR3A/C variants also caused childhood encephalitis, cerebellitis, or pneumonitis during primary infection. (cartertimofte2018rnapolymeraseiii pages 6-8)

No validated POLR3F modifier gene, protective allele, founder mutation, germline mosaicism, anticipation, somatic mutation, copy-number abnormality, translocation, inversion, or aneuploidy has been reported for this phenotype. No disease-specific methylation, histone, chromatin, or imprinting abnormality is known.

## 5. Environmental and infectious information

The direct non-genetic agent is **varicella-zoster virus** (human alphaherpesvirus 3; NCBI Taxonomy identification should be attached at the pathogen record level). Primary infection produces varicella; lifelong latency is established in sensory, cranial, and autonomic ganglionic neurons; reactivation can produce zoster or neurologic disease. The POLR3F cases represent neurologic reactivation, potentially without reliance on a contemporaneous typical rash. (kennedy2021recentissuesin pages 8-9, cartertimofte2018rnapolymeraseiii pages 1-2)

No toxin, pollutant, radiation, dietary, occupational, smoking, alcohol, or exercise association is known. Immunosuppression and aging are important general VZV modifiers but were not defining features of these patients.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Trigger:** latent VZV reactivates and viral AT-rich DNA becomes available to intracellular sensing.
2. **Upstream lesion:** POLR3F p.Arg50Trp impairs the cytoplasmic antiviral function of the 17-subunit RNA polymerase III complex.
3. **Normal pathway:** Pol III transcribes AT-rich DNA into **5′-triphosphorylated RNA**, which activates **RIG-I**, then **MAVS**, IRF/NF-κB signaling, and type I/III interferon production.
4. **Patient-cell defect:** poly(dA:dT)-induced antiviral and inflammatory responses, including IFN-β and TNF-α, are reduced; VZV gene expression/replication rises.
5. **Tissue consequence:** inadequate viral restriction permits infection and inflammation involving CNS tissue and cerebral arterial walls.
6. **Clinical consequence:** vasculopathy, vessel narrowing/ischemia, headache, sensory or motor deficits, and recurrent stroke-like episodes. (cartertimofte2018rnapolymeraseiii pages 4-6, cartertimofte2018rnapolymeraseiii pages 6-8, ansari2021primaryandacquired pages 5-6)

Nuclear Pol III normally transcribes tRNAs, 5S rRNA, U6 snRNA, and other small RNAs. In VZV-susceptibility patients, housekeeping transcription such as 5S rRNA production was preserved, helping explain the narrow infectious phenotype and distinguishing it from biallelic POLR3-related leukodystrophy. (lata2021rnapolymeraseiii pages 21-22, cartertimofte2018rnapolymeraseiii pages 4-6)

### Cells, tissues, and ontology suggestions

**Experimentally studied:** PBMCs, including mixed lymphoid and myeloid populations. **Biologically plausible but not directly proven in the twins:** monocytes/macrophages, cerebral endothelial or vascular smooth-muscle cells, neurons, microglia, astrocytes, and dermal fibroblasts. Reviews explicitly identify the decisive in-vivo cell type and the site at which Pol III controls latency/reactivation as unresolved. (kennedy2021recentissuesin pages 8-9, cartertimofte2018rnapolymeraseiii pages 10-11)

Suggested GO biological processes include:

- cytoplasmic pattern-recognition receptor signaling pathway in response to virus;
- defense response to virus (GO:0051607);
- type I interferon production (GO:0032606);
- response to type I interferon (GO:0034340);
- RNA polymerase III transcription;
- negative regulation of viral genome replication;
- RIG-I signaling pathway;
- inflammatory response and regulation of cytokine production.

Suggested cellular components include **cytosol (GO:0005829)**, **nucleus (GO:0005634)**, RNA polymerase III complex, and mitochondrial outer membrane/MAVS signaling platform. Suggested CL mappings include peripheral-blood mononuclear cell, monocyte (CL:0000576), T cell (CL:0000084), B cell (CL:0000236), natural killer cell (CL:0000623), neuron (CL:0000540), microglial cell (CL:0000129), astrocyte (CL:0000127), and vascular endothelial cell. These are knowledge-base mappings, not all directly demonstrated disease cell types.

### Molecular profiling and advanced technologies

Disease-specific bulk or single-cell transcriptomics, spatial transcriptomics, proteomics, metabolomics, lipidomics, epigenomics, and multi-omics datasets were not found. The available molecular profile consists principally of targeted cytokine measurements and VZV gene-expression/replication assays in patient PBMCs. No disease-specific CRISPR screen or patient-derived iPSC/organoid model was identified.

Recent structural work on human Pol III supports the broader interpretation that viral-sensing variants are situated near DNA-interacting regions, whereas neurodevelopmental variants tend to affect enzyme stability or biogenesis. This provides structural plausibility but is not a POLR3F-p.Arg50Trp clinical validation by itself. (lata2021rnapolymeraseiii pages 21-22, lata2021rnapolymeraseiii pages 10-11)

## 7. Anatomical structures affected

- **Primary system:** nervous system.
- **Organs:** brain and spinal cord; meninges may be involved through meningoencephalitic disease.
- **Vascular structures:** intracranial/cerebral arteries affected by VZV vasculopathy.
- **Sites reported:** parietal periventricular/paraventricular and juxtacortical cerebral white matter; cervical-to-upper-thoracic spinal cord, approximately C6–T2, in one patient.
- **Secondary structures in VZV biology:** dorsal-root, cranial, and autonomic ganglia harbor latent virus.
- **Lateralization:** neurologic deficits can be unilateral, but imaging lesions may be bilateral or multifocal. (kennedy2021recentissuesin pages 8-9, cartertimofte2018varicellazosterviruscns pages 3-4)

Suggested UBERON mappings include brain (UBERON:0000955), spinal cord (UBERON:0002240), central nervous system (UBERON:0001017), cerebral artery, cerebral white matter, meninges, dorsal-root ganglion, and blood-vessel wall. At the subcellular level, both cytosolic immune sensing and nuclear housekeeping Pol III functions are relevant.

## 8. Temporal development

The twins had uncomplicated primary varicella in childhood and developed recurrent CNS disease in adulthood. Review summaries describe both as 37-year-old women; patient-level summaries indicate initial presentations at approximately 25 and 35 years, reflecting differing episode histories or ages at first documented presentation. The disorder should therefore be modeled as **genetic from conception but clinically latent until VZV reactivation**, with variable adult onset. (cartertimofte2018rnapolymeraseiii pages 6-8, cartertimofte2018varicellazosterviruscns pages 3-4)

The clinical course is acute-to-subacute during each neurologic attack but lifelong and relapsing at the susceptibility level. Remission can follow antiviral treatment, while stopping prophylaxis may permit recurrence. No formal disease stages, median recurrence interval, critical developmental window, or long-term natural-history curve has been established. (cartertimofte2018varicellazosterviruscns pages 6-8)

## 9. Inheritance and population

### Inheritance

The best-supported model is **autosomal dominant/monoallelic susceptibility with incomplete or context-dependent penetrance**. Both monozygotic twins inherited the allele from their father; his possible VZV-related stroke suggests expression but is not a molecularly confirmed third case. Because VZV exposure/reactivation and additional immune factors are required, penetrance is likely infection- and age-dependent. (cartertimofte2018varicellazosterviruscns pages 4-5)

There is no evidence for anticipation, a founder effect, consanguinity dependence, or a sex-limited phenotype. The occurrence in female twins cannot establish a female predominance.

### Epidemiology

- **Confirmed disease-specific patients:** 2.
- **Families:** 1.
- **Prevalence/incidence:** unknown; no registry or population estimate.
- **Carrier frequency:** unknown.
- **Geographic/ancestral distribution:** insufficiently reported.
- **Sex ratio:** indeterminate.

The condition is appropriately classified as **ultra-rare**, but a numerical prevalence per 100,000 cannot be justified.

## 10. Diagnostics

### Clinical recognition

Consider the disorder in an otherwise healthy person with recurrent or unusually severe VZV meningoencephalitis, CNS vasculopathy, myelitis, ischemic stroke, pneumonitis, or disseminated disease—particularly with normal routine immune testing or a family history of similar neurologic events. Recurrent VZV CNS disease is a stronger warning sign than uncomplicated zoster.

### Acute VZV/CNS evaluation

Recommended evaluation is phenotype-driven and includes:

1. Brain MRI with diffusion-weighted and vascular imaging; spinal MRI if myelopathy is present.
2. Lumbar puncture with cell count, protein/glucose, VZV PCR, and paired serum/CSF anti-VZV IgG to demonstrate intrathecal synthesis.
3. Recognition that **negative CSF VZV PCR does not exclude vasculopathy**; intrathecal anti-VZV IgG may remain positive and can be more sensitive in protracted disease. The affected twin had pleocytosis and intrathecal VZV IgG despite negative PCR. (cartertimofte2018varicellazosterviruscns pages 3-4)
4. Baseline immune assessment: complete blood count/differential, quantitative immunoglobulins, lymphocyte subsets and proliferation, HIV testing, and evaluation for acquired immunosuppression. These tests were normal in the reported patients. (cartertimofte2018varicellazosterviruscns pages 4-5)

### Genetic testing

- **Preferred approach:** an inborn-error-of-immunity or severe viral-infection panel containing **POLR3F, POLR3A, POLR3C, POLR3E**, and relevant differential genes; alternatively WES/WGS.
- **Confirmation:** Sanger or orthogonal confirmation, parental testing, segregation analysis, transcript-specific HGVS normalization, and current ClinVar/gnomAD review.
- **Functional support:** PBMC stimulation with poly(dA:dT), measurement of IFN-β/type I or III IFN and inflammatory cytokines, and VZV replication/gene-expression assays. These remain specialized research tests rather than standardized clinical diagnostics. (cartertimofte2018varicellazosterviruscns pages 6-8, ansari2021primaryandacquired pages 5-6)
- **CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing:** low expected yield for an isolated missense disorder unless another phenotype suggests a structural or mitochondrial diagnosis.
- **RNA sequencing:** not validated diagnostically for p.Arg50Trp; it may help evaluate splice or expression variants in unsolved cases.

### Differential diagnosis

Important alternatives include acquired immunosuppression/HIV; hematologic malignancy or transplantation; anti-type-I-IFN autoantibodies; broad T/NK-cell defects such as GATA2, DOCK2, DOCK8, STK4, MAGT1, CXCR4, STAT1/STAT3/STAT5B-associated disorders; TLR3-pathway defects; other Pol III subunit defects; antiphospholipid or primary autoimmune vasculitis; atherosclerotic/dissection-related stroke; multiple sclerosis and other inflammatory myelitis; HSV encephalitis; and non-VZV infectious vasculopathies. Broader immunodeficiencies usually produce additional infections or characteristic immunologic abnormalities, whereas POLR3F disease was narrowly VZV-specific. (kennedy2021recentissuesin pages 8-9, ansari2021primaryandacquired pages 21-22, ansari2021primaryandacquired pages 24-25, ansari2021primaryandacquired pages 22-23)

No newborn or population screening is indicated. Once a familial pathogenic/likely pathogenic variant is established, cascade testing is reasonable with careful counseling about uncertain penetrance.

## 11. Outcome and prognosis

Disease-specific survival, mortality, life expectancy, and five- or ten-year outcomes are unknown. Both reported patients survived recurrent attacks and received prophylaxis, but ischemic lesions and recurring neurologic deficits indicate a risk of cumulative disability. One twin developed renewed symptoms and new white-matter lesions after stopping prophylaxis. (cartertimofte2018varicellazosterviruscns pages 6-8)

Prognosis probably depends on rapid antiviral treatment, recurrence prevention, lesion burden and location, presence of large-vessel vasculopathy or myelitis, and residual motor/cognitive deficits. These are clinically plausible factors rather than validated POLR3F prognostic models. No prognostic biomarker beyond virologic activity, CSF inflammation, and imaging has been validated.

## 12. Treatment

### Acute disease

In the reported family, treatment included **intravenous acyclovir 10 mg/kg every eight hours for 14 days** and **prednisolone 50 mg/day for 10 days**. This targets viral replication and presumed arterial inflammation, respectively. (cartertimofte2018varicellazosterviruscns pages 3-4)

Suggested NCIt mappings include **Acyclovir (NCIt drug concept)**, antiviral therapy, corticosteroid therapy, and supportive care. Renal function and hydration should be monitored during intravenous acyclovir; dose adjustment is required for kidney impairment. Steroids should not replace antiviral therapy and should be individualized because disease-specific controlled evidence is absent.

### Long-term strategy

Both twins received suppressive acyclovir. Expert review recommends considering acyclovir prophylaxis after severe or recurrent CNS disease and age-appropriate varicella/zoster immunization in Pol III defects. The recurrence observed after prophylaxis discontinuation supports continued suppression in this family, but optimal drug, dose, and duration are unknown. (cartertimofte2018varicellazosterviruscns pages 6-8, cartertimofte2018rnapolymeraseiii pages 10-11)

### Experimental and precision therapies

No POLR3F-specific interventional trial, gene therapy, gene editing, RNA therapy, hematopoietic stem-cell transplantation protocol, or adoptive VZV-specific T-cell trial was identified. Interferon therapy has been proposed more broadly for selected IFN-pathway defects, and IFN-α/IFN-γ inhibit VZV in vitro, but this is not established treatment for POLR3F deficiency. (ansari2021primaryandacquired pages 10-11)

A rational current algorithm is: **suspected VZV CNS disease → collect CSF and imaging promptly without delaying IV acyclovir → consider adjunct corticosteroid for vasculopathy → confirm intrathecal VZV immunity/PCR → investigate immune and genetic causes → institute individualized long-term antiviral suppression and rehabilitation**.

## 13. Prevention

### Primary prevention

Preventing primary VZV infection through routine varicella vaccination is biologically attractive, but the safety and efficacy of live-attenuated varicella vaccine in a known POLR3F carrier have not been studied. Decisions should be made with clinical immunology and infectious-disease specialists after assessing immune competence. Expert review also advocates adult zoster vaccination, especially a non-live recombinant subunit vaccine, although direct POLR3F data are unavailable. (cartertimofte2018rnapolymeraseiii pages 10-11)

### Secondary and tertiary prevention

- Educate carriers to seek urgent care for headache, focal deficits, altered consciousness, myelopathic symptoms, or zoster-associated neurologic symptoms.
- Use rapid CSF/imaging evaluation and early antiviral treatment.
- Consider long-term acyclovir/valacyclovir suppression after recurrent CNS disease.
- Monitor renal toxicity and antiviral adherence.
- Use physical, occupational, speech, visual, or neuropsychological rehabilitation according to residual deficits.
- Offer cascade genetic testing and counseling to adult relatives once variant pathogenicity is clinically accepted.

Prenatal or preimplantation testing is technically possible for a known familial variant, but uncertain penetrance and a potentially preventable/treatable infectious phenotype require nuanced counseling. No population carrier-screening program is justified.

## 14. Other species and natural disease

VZV is highly human-restricted; no naturally occurring veterinary counterpart of human POLR3F-specific VZV immunodeficiency was identified. Therefore, breed ontology entries, veterinary prevalence, zoonotic transmission, and natural cross-species disease are not applicable.

Simian varicella virus in rhesus macaques resembles human primary and reactivated VZV disease and has demonstrated an important role for CD4 T-cell immunity, but it is an analog infection rather than a natural POLR3F-deficiency model. Small-animal VZV inoculation can establish ganglionic infection without faithfully reproducing human rash or the full neurologic syndrome. Human tissue xenografts in SCID mice and simian varicella models are useful for VZV neurotropism, latency, and immunity research. These systems do not yet recapitulate the human POLR3F p.Arg50Trp genotype. (cartertimofte2018rnapolymeraseiii pages 10-11)

POLR3F and the Pol III machinery are evolutionarily conserved, but specific ortholog identifiers and a naturally occurring orthologous animal syndrome were not established by the retrieved evidence.

## 15. Model organisms and experimental models

### Available models

- **Patient PBMCs:** the most disease-specific model; they reproduce deficient poly(dA:dT)-induced cytokine responses and increased VZV replication. Strength: direct human genotype–phenotype relevance. Limitation: mixed circulating cells do not reproduce neurons, ganglia, cerebral arteries, or tissue-resident immunity. (cartertimofte2018varicellazosterviruscns pages 6-8, ansari2021primaryandacquired pages 5-6)
- **Recombinant/expression assays:** mutant POLR3F expression and solubility can be compared with wild type. Strength: tests protein stability; limitation: does not capture the intact tissue response. (cartertimofte2018varicellazosterviruscns pages 4-5)
- **SCID-human xenografts:** human skin or neural tissue implanted in immunodeficient mice supports VZV pathogenesis studies. Strength: human-tissue tropism; limitation: lacks an intact human immune system and has not been engineered for p.Arg50Trp.
- **Rhesus macaque/simian varicella virus:** reproduces key features of primary infection, latency, and reactivation. Strength: intact primate immunity; limitation: different virus and no reported POLR3F disease genotype.
- **Standard small animals:** limited because human VZV is species-restricted and generally fails to reproduce the complete human phenotype.

### Needed next-generation models

Priority models include CRISPR knock-in of **POLR3F p.Arg50Trp** in human iPSCs differentiated into neurons, microglia, astrocytes, and cerebral endothelial cells; vascular organoids combining these cell types; isogenic rescue lines; and a conditional knock-in mammalian model challenged with an appropriate alphaherpesvirus. Single-cell transcriptomics and spatial profiling across infected neurovascular units could determine which cells fail to mount Pol III–RIG-I–MAVS interferon responses.

## Recent developments, expert assessment, and knowledge gaps

Research in 2023 broadened host-genetic investigation of severe alphaherpesvirus disease: WES of **17 patients** with HSV- or VZV-induced acute retinal necrosis identified **50 potentially disease-associated variants in 16/17**, concentrated in innate/adaptive immunity, autophagy, and apoptosis pathways. This does not establish new POLR3F cases, but it supports systematic genomic evaluation of unusually severe, tissue-restricted VZV disease. The study was published October 2023, DOI: [10.3389/fnmol.2023.1253040](https://doi.org/10.3389/fnmol.2023.1253040).

The most defensible current expert interpretation is that Pol III has a nonredundant role in human VZV defense, but several central questions remain unresolved: the decisive in-vivo cell type; whether cytosolic viral-DNA transcription or nuclear RNA-derived signaling predominates; how POLR3F controls neuronal latency and reactivation; whether p.Arg50Trp is fully penetrant; and which prophylactic regimen is optimal. Reviews explicitly note that POLR3-mutant patients have a narrow VZV phenotype and propose vaccination and antiviral prophylaxis, while acknowledging the absence of disease-specific trials. (cartertimofte2018rnapolymeraseiii pages 10-11)

Accordingly, the knowledge-base entry should mark the **gene–disease relationship as supported by one segregating family plus functional human-cell evidence**, not as a mature disorder with established epidemiology or consensus guidelines. Variant classification, MONDO/OMIM identifiers, transcript HGVS, and current population frequency should be rechecked directly in ClinVar, ClinGen, OMIM, HGNC, and gnomAD before production release.

References

1. (cartertimofte2018varicellazosterviruscns pages 6-8): Madalina E. Carter-Timofte, Anders F. Hansen, Maibritt Mardahl, Sébastien Fribourg, Franck Rapaport, Shen-Ying Zhang, Jean-Laurent Casanova, Søren R. Paludan, Mette Christiansen, Carsten S. Larsen, and Trine H. Mogensen. Varicella-zoster virus cns vasculitis and rna polymerase iii gene mutation in identical twins. Neurology Neuroimmunology &amp; Neuroinflammation, Nov 2018. URL: https://doi.org/10.1212/nxi.0000000000000500, doi:10.1212/nxi.0000000000000500. This article has 66 citations.

2. (cartertimofte2018varicellazosterviruscns pages 4-5): Madalina E. Carter-Timofte, Anders F. Hansen, Maibritt Mardahl, Sébastien Fribourg, Franck Rapaport, Shen-Ying Zhang, Jean-Laurent Casanova, Søren R. Paludan, Mette Christiansen, Carsten S. Larsen, and Trine H. Mogensen. Varicella-zoster virus cns vasculitis and rna polymerase iii gene mutation in identical twins. Neurology Neuroimmunology &amp; Neuroinflammation, Nov 2018. URL: https://doi.org/10.1212/nxi.0000000000000500, doi:10.1212/nxi.0000000000000500. This article has 66 citations.

3. (ansari2021primaryandacquired pages 5-6): Rahila Ansari, Lindsey B Rosen, Andrea Lisco, Don Gilden, Steven M Holland, Christa S Zerbe, Robert A Bonomo, and Jeffrey I Cohen. Primary and acquired immunodeficiencies associated with severe varicella-zoster infections. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America, 73:e2705-e2712, Aug 2021. URL: https://doi.org/10.1093/cid/ciaa1274, doi:10.1093/cid/ciaa1274. This article has 59 citations.

4. (cartertimofte2018rnapolymeraseiii pages 6-8): Madalina E. Carter-Timofte, Søren R. Paludan, and Trine H. Mogensen. Rna polymerase iii as a gatekeeper to prevent severe vzv infections. Trends in molecular medicine, 24 10:904-915, Oct 2018. URL: https://doi.org/10.1016/j.molmed.2018.07.009, doi:10.1016/j.molmed.2018.07.009. This article has 52 citations and is from a domain leading peer-reviewed journal.

5. (cartertimofte2018varicellazosterviruscns pages 3-4): Madalina E. Carter-Timofte, Anders F. Hansen, Maibritt Mardahl, Sébastien Fribourg, Franck Rapaport, Shen-Ying Zhang, Jean-Laurent Casanova, Søren R. Paludan, Mette Christiansen, Carsten S. Larsen, and Trine H. Mogensen. Varicella-zoster virus cns vasculitis and rna polymerase iii gene mutation in identical twins. Neurology Neuroimmunology &amp; Neuroinflammation, Nov 2018. URL: https://doi.org/10.1212/nxi.0000000000000500, doi:10.1212/nxi.0000000000000500. This article has 66 citations.

6. (lata2021rnapolymeraseiii pages 21-22): Elisabeth Lata, Karine Choquet, Francis Sagliocco, Bernard Brais, Geneviève Bernard, and Martin Teichmann. Rna polymerase iii subunit mutations in genetic diseases. Frontiers in Molecular Biosciences, Jul 2021. URL: https://doi.org/10.3389/fmolb.2021.696438, doi:10.3389/fmolb.2021.696438. This article has 86 citations.

7. (cartertimofte2018rnapolymeraseiii pages 4-6): Madalina E. Carter-Timofte, Søren R. Paludan, and Trine H. Mogensen. Rna polymerase iii as a gatekeeper to prevent severe vzv infections. Trends in molecular medicine, 24 10:904-915, Oct 2018. URL: https://doi.org/10.1016/j.molmed.2018.07.009, doi:10.1016/j.molmed.2018.07.009. This article has 52 citations and is from a domain leading peer-reviewed journal.

8. (cartertimofte2018rnapolymeraseiii pages 10-11): Madalina E. Carter-Timofte, Søren R. Paludan, and Trine H. Mogensen. Rna polymerase iii as a gatekeeper to prevent severe vzv infections. Trends in molecular medicine, 24 10:904-915, Oct 2018. URL: https://doi.org/10.1016/j.molmed.2018.07.009, doi:10.1016/j.molmed.2018.07.009. This article has 52 citations and is from a domain leading peer-reviewed journal.

9. (kennedy2021recentissuesin pages 8-9): Peter Kennedy, Trine Mogensen, and Randall Cohrs. Recent issues in varicella-zoster virus latency. Viruses, 13:2018, Oct 2021. URL: https://doi.org/10.3390/v13102018, doi:10.3390/v13102018. This article has 83 citations.

10. (cartertimofte2018varicellazosterviruscns pages 1-2): Madalina E. Carter-Timofte, Anders F. Hansen, Maibritt Mardahl, Sébastien Fribourg, Franck Rapaport, Shen-Ying Zhang, Jean-Laurent Casanova, Søren R. Paludan, Mette Christiansen, Carsten S. Larsen, and Trine H. Mogensen. Varicella-zoster virus cns vasculitis and rna polymerase iii gene mutation in identical twins. Neurology Neuroimmunology &amp; Neuroinflammation, Nov 2018. URL: https://doi.org/10.1212/nxi.0000000000000500, doi:10.1212/nxi.0000000000000500. This article has 66 citations.

11. (cartertimofte2018rnapolymeraseiii pages 1-2): Madalina E. Carter-Timofte, Søren R. Paludan, and Trine H. Mogensen. Rna polymerase iii as a gatekeeper to prevent severe vzv infections. Trends in molecular medicine, 24 10:904-915, Oct 2018. URL: https://doi.org/10.1016/j.molmed.2018.07.009, doi:10.1016/j.molmed.2018.07.009. This article has 52 citations and is from a domain leading peer-reviewed journal.

12. (lata2021rnapolymeraseiii pages 10-11): Elisabeth Lata, Karine Choquet, Francis Sagliocco, Bernard Brais, Geneviève Bernard, and Martin Teichmann. Rna polymerase iii subunit mutations in genetic diseases. Frontiers in Molecular Biosciences, Jul 2021. URL: https://doi.org/10.3389/fmolb.2021.696438, doi:10.3389/fmolb.2021.696438. This article has 86 citations.

13. (ansari2021primaryandacquired pages 21-22): Rahila Ansari, Lindsey B Rosen, Andrea Lisco, Don Gilden, Steven M Holland, Christa S Zerbe, Robert A Bonomo, and Jeffrey I Cohen. Primary and acquired immunodeficiencies associated with severe varicella-zoster infections. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America, 73:e2705-e2712, Aug 2021. URL: https://doi.org/10.1093/cid/ciaa1274, doi:10.1093/cid/ciaa1274. This article has 59 citations.

14. (ansari2021primaryandacquired pages 24-25): Rahila Ansari, Lindsey B Rosen, Andrea Lisco, Don Gilden, Steven M Holland, Christa S Zerbe, Robert A Bonomo, and Jeffrey I Cohen. Primary and acquired immunodeficiencies associated with severe varicella-zoster infections. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America, 73:e2705-e2712, Aug 2021. URL: https://doi.org/10.1093/cid/ciaa1274, doi:10.1093/cid/ciaa1274. This article has 59 citations.

15. (ansari2021primaryandacquired pages 22-23): Rahila Ansari, Lindsey B Rosen, Andrea Lisco, Don Gilden, Steven M Holland, Christa S Zerbe, Robert A Bonomo, and Jeffrey I Cohen. Primary and acquired immunodeficiencies associated with severe varicella-zoster infections. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America, 73:e2705-e2712, Aug 2021. URL: https://doi.org/10.1093/cid/ciaa1274, doi:10.1093/cid/ciaa1274. This article has 59 citations.

16. (ansari2021primaryandacquired pages 10-11): Rahila Ansari, Lindsey B Rosen, Andrea Lisco, Don Gilden, Steven M Holland, Christa S Zerbe, Robert A Bonomo, and Jeffrey I Cohen. Primary and acquired immunodeficiencies associated with severe varicella-zoster infections. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America, 73:e2705-e2712, Aug 2021. URL: https://doi.org/10.1093/cid/ciaa1274, doi:10.1093/cid/ciaa1274. This article has 59 citations.

## Artifacts

- [Edison artifact artifact-00](Immunodeficiency_101_Varicella_Zoster_Virus-specific-deep-research-falcon_artifacts/artifact-00.md)

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