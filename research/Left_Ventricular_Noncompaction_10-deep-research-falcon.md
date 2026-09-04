---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T21:03:20.169682'
end_time: '2026-08-17T21:17:14.671483'
duration_seconds: 834.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Left Ventricular Noncompaction 10
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
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
  path: Left_Ventricular_Noncompaction_10-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Left Ventricular Noncompaction 10
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Left Ventricular Noncompaction 10** covering all of the
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
- **Disease Name:** Left Ventricular Noncompaction 10
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Left Ventricular Noncompaction 10** covering all of the
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


# Left Ventricular Noncompaction 10 (LVNC10): Disease-Characteristics Research Report

## Executive summary and scope

**Left ventricular noncompaction 10 (LVNC10)** is the numbered, **MYBPC3-associated** form of left-ventricular noncompaction/hypertrabeculation. Its disease-specific identifier is **MONDO:0014163**; the broader LVNC concept is **MONDO:0018901**. Open Targets maps LVNC10 specifically to **MYBPC3** (myosin-binding protein C3; Ensembl ENSG00000134571) and links the association to primary-literature PMIDs including **20186049** and **27532257**. The historical variant underlying this numbered subtype is **MYBPC3 p.Arg820Trp (R820W)**, although its present ClinVar classification and transcript-specific HGVS expression should be rechecked at the time of clinical interpretation. (OpenTargets Search: left ventricular noncompaction-MYBPC3)

A crucial curation distinction is that **LVNC10 is a rare genetic disease entry, whereas left-ventricular hypertrabeculation is also a common, sometimes reversible imaging trait**. The 2023 ESC framework treats noncompaction as a dynamic trait found in healthy hearts, other cardiomyopathies, congenital disease, anemia, renal disease, pregnancy, and athletes rather than automatically as a separate cardiomyopathy. Consequently, morphology alone must not be equated with MYBPC3-related LVNC10. (grasso2024thenew2023 pages 1-2, walsh2023thetroublewith pages 1-2)

The evidence is predominantly aggregated disease-level information from families, referral cohorts, systematic reviews, and registries—not individual-patient EHR data. Subtype-specific epidemiology, penetrance, prognosis, and treatment-response estimates are unavailable; broad-LVNC evidence is identified as such below.

| Domain | LVNC10-specific fact | Broad LVNC / contextual evidence | Suggested ontology terms | Key citation(s) |
|---|---|---|---|---|
| Identity / identifiers | **Left Ventricular Noncompaction 10 (LVNC10)**; disease-specific MONDO: **0014163**; subtype linked to **MYBPC3** | Broad **left ventricular noncompaction** MONDO: **0018901**; phenotype/trait remains conceptually debated across cardiomyopathies | MONDO:0014163; MONDO:0018901 | (OpenTargets Search: left ventricular noncompaction-MYBPC3, walsh2023thetroublewith pages 1-2) |
| Synonyms / naming | Numbered subtype name: **Left ventricular noncompaction 10** | LVNC, left ventricular non-compaction, left ventricular hypertrabeculation/noncompaction; recent ESC framing treats LV non-compaction as a **dynamic trait** rather than always a distinct cardiomyopathy | HPO phenotype label suggestion: Left ventricular noncompaction cardiomyopathy | (grasso2024thenew2023 pages 1-2, walsh2023thetroublewith pages 1-2) |
| Data granularity | Evidence is primarily **aggregated disease-level** and family/cohort literature, not EHR-derived in the retrieved sources | Large cohorts, reviews, and registries dominate current evidence | — | (sedaghathamedani2017clinicalgeneticsand pages 1-2, NCT06024759 chunk 1) |
| Causal gene | **MYBPC3** (myosin binding protein C3) is the mapped causal gene for LVNC10 | MYBPC3 is one of several recurrent LVNC-associated genes; most validated LVNC genes overlap with HCM/DCM architecture | HGNC gene symbol: MYBPC3; Ensembl: ENSG00000134571 | (OpenTargets Search: left ventricular noncompaction-MYBPC3, mazzarotto2021systematiclargescaleassessment pages 1-2) |
| Canonical historical variant | Historical human association includes **p.Arg820Trp / R820W** in **MYBPC3** for LVNC10; **current variant classification should be checked in ClinVar before reuse** | MYBPC3 disease can also involve truncating, missense, de novo, deletion, and biallelic combinations with severe phenotypes | HGVS protein suggestion: p.Arg820Trp | (OpenTargets Search: left ventricular noncompaction-MYBPC3, kolokotronis2019biallelicmutationin pages 7-9) |
| Inheritance | Most consistent expectation for LVNC10 due to MYBPC3 is **autosomal dominant** with **variable expressivity** and **incomplete penetrance**; severe early disease may occur with **biallelic/compound heterozygous** states | Broad LVNC familial transmission is often AD, but X-linked and maternal patterns also occur in other genetic forms | HPO inheritance term suggestion: Autosomal dominant inheritance | (sedaghathamedani2017clinicalgeneticsand pages 1-2, kolokotronis2019biallelicmutationin pages 1-2, kolokotronis2019biallelicmutationin pages 7-9) |
| Principal phenotypes | MYBPC3-related LVNC10 is expected to feature LV noncompaction/hypertrabeculation and may overlap with HCM/DCM phenotypes | Heart failure, ventricular dysfunction, arrhythmia, thromboembolism, sudden cardiac death risk, and ECG abnormalities are recurrent LVNC manifestations | HPO suggestions: Left ventricular noncompaction cardiomyopathy; Arrhythmia; Ventricular tachycardia; Heart failure; Reduced ejection fraction; Sudden cardiac death | (sedaghathamedani2017clinicalgeneticsand pages 1-2, arbustini2014leftventricularnoncompaction pages 1-2, fitzsimons2024electrophysiologicalphenotypingof pages 1-3) |
| Age at onset / course | **Variable**; can be childhood or adult-onset in heterozygous disease; **early severe onset** reported with biallelic MYBPC3 states | Pediatric to adult presentation occurs broadly; prognosis is heterogeneous | HPO onset suggestions: Childhood onset; Adult onset; Infantile onset (for severe cases) | (kolokotronis2019biallelicmutationin pages 1-2, fitzsimons2024electrophysiologicalphenotypingof pages 1-3) |
| Anatomy | Primary structure affected: **left ventricular myocardium**, especially **apical/trabecular endocardial** regions with noncompacted and compacted layers | Broad LVNC definitions emphasize prominent trabeculae, deep recesses, thin compacted layer | UBERON suggestions: left ventricle; ventricular myocardium; endocardium | (arbustini2014leftventricularnoncompaction pages 1-2, mazzarotto2021systematiclargescaleassessment pages 1-2, fitzsimons2024electrophysiologicalphenotypingof pages 1-3) |
| Cell type | Disease-relevant cell type is primarily **cardiomyocyte** | Arrhythmic manifestations imply conduction-system involvement as secondary physiology | CL suggestion: cardiomyocyte | (kolokotronis2019biallelicmutationin pages 1-2, fitzsimons2024electrophysiologicalphenotypingof pages 8-10) |
| Mechanism | MYBPC3-associated mechanism is most consistent with **sarcomeric dysfunction / haploinsufficiency / protein instability**; severe biallelic cases showed marked reduction of MYBPC3 protein in tissue | LVNC broadly reflects overlap of sarcomeric cardiomyopathy biology with abnormal trabeculation/compaction; modifier and developmental influences likely | GO suggestions: sarcomere organization; cardiac muscle contraction; regulation of cardiac muscle cell contraction; ventricular cardiac muscle tissue morphogenesis | (kolokotronis2019biallelicmutationin pages 1-2, kolokotronis2019biallelicmutationin pages 7-9, mazzarotto2021systematiclargescaleassessment pages 1-2) |
| Pathophysiology chain | MYBPC3 variant → altered sarcomeric protein dosage/function → impaired contractile mechanics / myocardial architecture → excessive trabeculation or noncompaction phenotype ± systolic dysfunction/arrhythmia | Broad LVNC may represent either a distinct developmental/noncompaction mechanism or a phenotypic expression of other cardiomyopathies | GO suggestions as above | (kolokotronis2019biallelicmutationin pages 1-2, mazzarotto2021systematiclargescaleassessment pages 1-2, walsh2023thetroublewith pages 1-2) |
| Diagnostics | No LVNC10-only diagnostic test identified; diagnosis relies on **clinical imaging + cardiogenetics** | Echo and CMR use NC/C ratio-based criteria; overdiagnosis is a major issue, especially when relying on morphology alone | HPO suggestion: Abnormal left ventricular morphology | (grasso2024thenew2023 pages 1-2, mazzarotto2021systematiclargescaleassessment pages 1-2, walsh2023thetroublewith pages 1-2) |
| Imaging criteria | LVNC10 uses the same imaging framework as LVNC generally | Typical thresholds cited in retrieved sources: NC/C ratio **>2 to 2.3**; CMR may label up to **15%** of healthy individuals by ratio criteria alone | — | (mazzarotto2021systematiclargescaleassessment pages 1-2, walsh2023thetroublewith pages 1-2, mahendran2024emerginghallmarksof pages 6-10) |
| Genetic testing | Recommended practical approach: cardiomyopathy gene panel including **MYBPC3**; consider exome/genome in unresolved or syndromic/early severe cases | Genetic testing is most useful for diagnosis clarification, family screening, and differential diagnosis rather than proving morphology alone is pathologic | — | (grasso2024thenew2023 pages 1-2, mazzarotto2021systematiclargescaleassessment pages 1-2, NCT06024759 chunk 1) |
| Differential diagnosis | Distinguish LVNC10 from HCM/DCM with secondary hypertrabeculation, athlete’s heart, pregnancy-related trabeculation, anemia/sickle-cell-associated trabeculation, congenital heart disease, and syndromic cardiomyopathy | ESC 2023 explicitly frames LV non-compaction as a trait that can occur in many settings | — | (grasso2024thenew2023 pages 1-2, walsh2023thetroublewith pages 1-2, NCT02568072 chunk 1) |
| Prognosis | No LVNC10-specific survival estimate identified | Prognosis in LVNC depends more on ventricular dysfunction, arrhythmia burden, fibrosis/genotype context than trabeculation extent alone; LVNC cohort had more cardiovascular events than age-matched nonischemic DCM in one study | HPO suggestions: Sudden cardiac death; Thromboembolism | (sedaghathamedani2017clinicalgeneticsand pages 1-2, walsh2023thetroublewith pages 1-2, fitzsimons2024electrophysiologicalphenotypingof pages 1-3) |
| Treatment categories | No LVNC10 genotype-specific approved therapy identified | Treat according to phenotype: guideline-directed heart failure therapy, arrhythmia surveillance/management, anticoagulation when indicated, ICD/CRT in selected patients, transplant in end-stage disease | NCIT suggestions: Heart Failure Therapy; Anticoagulation Therapy; Implantable Cardioverter-Defibrillator; Cardiac Resynchronization Therapy; Heart Transplantation | (kolokotronis2019biallelicmutationin pages 1-2, mahendran2024emerginghallmarksof pages 6-10, NCT06024759 chunk 1) |
| Prevention / screening | **Cascade family screening** and genetic counseling are relevant for MYBPC3-related disease | Registry studies are actively evaluating mutation status, strain, PVC burden, NSVT, and ICD outcomes in LVNC | — | (NCT06024759 chunk 1, grasso2024thenew2023 pages 1-2) |
| Real-world implementation | No LVNC10-specific interventional trial identified | Active observational registry: **NCT06024759** (recruiting; target n=500) studying genetics, LV strain, PVC burden, NSVT, ICD predictors; broader nonischemic cardiomyopathy registry **NCT06607471** also includes LVNC | NCT terms may be mapped separately in a trial table | (NCT06024759 chunk 1, NCT06607471 chunk 23) |
| Evidence gaps | No retrieved LVNC10-specific prevalence/incidence, penetrance estimate, protective variants, environmental triggers, epigenomic signature, single-cell/spatial profile, validated biomarker, or targeted MYBPC3-LVNC therapy | Broad LVNC evidence is heterogeneous and often confounded by phenocopies and imaging overdiagnosis | — | (grasso2024thenew2023 pages 1-2, walsh2023thetroublewith pages 1-2) |


*Table: This table summarizes subtype-specific facts for Left Ventricular Noncompaction 10 alongside broader LVNC context needed for interpretation. It is designed as a compact curation aid for identifiers, mechanisms, phenotypes, diagnostics, treatment categories, and major evidence gaps.*

## 1. Disease information

### Definition

LVNC is morphologically characterized by prominent LV trabeculae, deep intertrabecular recesses communicating with the ventricular cavity, and a relatively thin compacted myocardial layer. A modern formulation requires excessive trabeculation **plus clinically meaningful myocardial disease**, such as ventricular dysfunction, fibrosis, arrhythmia, or a pathogenic genotype, rather than an imaging ratio alone. (arbustini2014leftventricularnoncompaction pages 1-2, mazzarotto2021systematiclargescaleassessment pages 1-2, walsh2023thetroublewith pages 1-2)

**Direct source quotation (Walsh, published 29 November 2023):** “Excessive trabeculation of the cardiac left ventricular wall is a complex phenotypic substrate associated with various physiological and pathological processes.” The same review concludes that uncertainty remains over whether hypertrabeculation causes disease or constitutes a distinct LVNC cardiomyopathy. DOI: https://doi.org/10.1007/s12265-023-10459-6. (walsh2023thetroublewith pages 1-2)

### Identifiers and synonyms

- **MONDO:** LVNC10, **MONDO:0014163**; broad LVNC, **MONDO:0018901**.
- **OMIM:** LVNC10 is historically indexed as **OMIM 615396**. The disease number should not be confused with the MYBPC3 gene record.
- **MeSH:** *Isolated Noncompaction of the Ventricular Myocardium*, **D056830**. (NCT01470014 chunk 1)
- **ICD-10/ICD-11:** No retrieved evidence established a unique subtype-specific LVNC10 code. In practice it is generally coded under cardiomyopathy/other cardiomyopathy categories, with local coding-system variation.
- **Synonyms:** left ventricular noncompaction 10; LVNC10; MYBPC3-related left ventricular noncompaction; noncompaction cardiomyopathy due to MYBPC3. Broader terms include LVNC, left ventricular non-compaction cardiomyopathy, isolated ventricular myocardial noncompaction, spongy myocardium, and left ventricular hypertrabeculation.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factor

LVNC10 is a **germline genetic sarcomeric cardiomyopathy** caused by disease-associated variation in **MYBPC3**, which encodes cardiac myosin-binding protein C. Open Targets reports five supporting association items and an LVNC10–MYBPC3 score of approximately 0.797. (OpenTargets Search: left ventricular noncompaction-MYBPC3)

The historic p.Arg820Trp association is important for disease nomenclature, but MYBPC3 produces a broad allelic spectrum: missense, truncating, splice-altering, whole-gene deletion, and compound-heterozygous states can yield HCM, DCM, LVNC, or overlapping phenotypes. Therefore, **MYBPC3 genotype does not uniquely predict LVNC morphology**. Large-scale analysis of 840 LVNC cases and 125,748 gnomAD controls found extensive genetic overlap between LVNC, HCM, and DCM. (mazzarotto2021systematiclargescaleassessment pages 1-2)

### Genetic risk and modifiers

- Most clinically recognized MYBPC3 cardiomyopathy is autosomal dominant, with incomplete, often age-dependent penetrance and variable expressivity.
- A second pathogenic allele can markedly increase severity. In a human cardiac-tissue study, a de novo **p.Ser858Arg** allele in trans with deletion of the entire MYBPC3 gene caused severe early cardiomyopathy with LVNC, approximately **80% lower protein** and approximately **50% lower transcript** than controls. (kolokotronis2019biallelicmutationin pages 1-2, kolokotronis2019biallelicmutationin pages 7-9)
- Broad LVNC polygenic architecture may modify morphology. A UK Biobank GWAS of **18,096 participants** identified 16 loci, including TTN, TNNT2, PLN, MTSS1, and GOSR2; segmental SNP heritability was estimated at **20–25%**. MIB1 loss-of-function variants have also been proposed as modifiers in patients carrying TTN truncating variants. These observations are not specific to LVNC10. (walsh2023thetroublewith pages 11-13)

### Environmental and lifestyle factors

No toxin, infection, diet, smoking pattern, alcohol exposure, occupation, or medication has been shown to cause LVNC10. Likewise, no validated genetic or environmental protective factor has been identified.

Hemodynamic loading can, however, **induce or amplify the hypertrabeculation phenotype** and thereby confound diagnosis. Increased trabeculation has been documented with athletic training, pregnancy, and chronic anemia. In cited observational data, athletes had more hypertrabeculation than controls (**18.3% versus 7.0%**), and 8.1% met conventional echocardiographic LVNC criteria. During pregnancy, 25.4% developed increased trabeculation and 7.8% met Chin and Jenni criteria; prevalence was higher in Black than White women (**46% versus 13%, p=0.0003**). These are physiologic remodeling data, not evidence that exercise or pregnancy causes inherited LVNC10. (NCT02568072 chunk 1, NCT02568072 chunk 2)

**Interpretive gene–environment model:** an MYBPC3 variant may create a susceptible sarcomeric substrate, while developmental, polygenic, and loading conditions alter penetrance or the degree of trabeculation. Direct LVNC10-specific interaction studies are absent.

## 3. Phenotypes

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| LV noncompaction/hypertrabeculation | Imaging/structural sign; usually apical and mid-ventricular; severity variable | **HP:0011664**, Left ventricular noncompaction cardiomyopathy |
| Cardiomyopathy overlap | HCM, DCM, or mixed morphology; congenital through adult onset | Hypertrophic cardiomyopathy; Dilated cardiomyopathy |
| LV systolic dysfunction | Clinical/imaging sign; may be absent, progressive, or severe | Reduced left ventricular ejection fraction |
| Heart failure | Dyspnea, fatigue, exercise intolerance, edema, growth compromise in children; variable progression | Heart failure; Exercise intolerance; Dyspnea |
| Arrhythmia/conduction disease | PVCs, VT/VF, bradycardia, AV block, WPW; episodic and potentially fatal | Arrhythmia; Ventricular tachycardia; Wolff–Parkinson–White syndrome; Atrioventricular block |
| Thromboembolism | Stroke/systemic embolism, particularly with LV dysfunction, atrial fibrillation, or intracardiac thrombus | Thromboembolism; Stroke |
| Sudden cardiac death | Uncommon but major severe outcome, associated with malignant arrhythmia and dysfunction | Sudden cardiac death |

The 2024 pediatric systematic review searched 4,531 records and analyzed **57 cases** from prenatal life through age 18. It reported frequent conduction abnormalities, including Mobitz II and WPW; 9% displayed WPW, and 46% of mapped arrhythmias originated near the apex. Diagnostic methods were inconsistent in 66% of cases. These percentages reflect a selected case literature and should not be treated as population frequencies. DOI: https://doi.org/10.14814/phy2.16029. (fitzsimons2024electrophysiologicalphenotypingof pages 7-8, fitzsimons2024electrophysiologicalphenotypingof pages 1-3)

**Direct abstract quotation (accepted 12 April 2024):** the review found “abnormal left ventricular, atrioventricular node, and interventricular septal patterns, and specifically a high incidence of Mobitz type II and Wolff–Parkinson–White waveforms.” (fitzsimons2024electrophysiologicalphenotypingof pages 1-3)

Quality of life is impaired principally by heart-failure symptoms, exercise restriction, recurrent surveillance, arrhythmia anxiety, ICD shocks, embolic events, and hospitalization. No LVNC10-specific EQ-5D, SF-36, or PROMIS dataset was identified.

## 4. Genetic and molecular information

### Gene and variants

- **Gene:** MYBPC3; approved name *myosin binding protein C3*; Ensembl **ENSG00000134571**. (OpenTargets Search: left ventricular noncompaction-MYBPC3)
- **Origin:** germline; somatic MYBPC3 disease is not established.
- **Historical LVNC10 allele:** p.Arg820Trp/R820W. PMID **20186049** is among the primary references linked to the MYBPC3–LVNC10 association. (OpenTargets Search: left ventricular noncompaction-MYBPC3)
- **Variant interpretation:** clinical classification must use transcript-correct HGVS, ClinVar/ClinGen evidence, ancestry-matched frequency, segregation, phenotype, and ACMG/AMP criteria. The old numbered disease assignment alone is insufficient to classify an allele as pathogenic.
- **Population frequency:** no reliable subtype-specific allele frequency was recovered. A genuinely penetrant severe dominant allele should be rare in gnomAD; exact variant frequencies should be retrieved directly from the current gnomAD release.

### Functional consequences

MYBPC3 loss-of-function commonly acts through **haploinsufficiency**; missense alleles may impair protein stability, sarcomeric incorporation, or myosin/actin regulation. In the severe biallelic LVNC case, only about **20% of normal MYBPC3 protein** remained in diseased myocardium. Histology showed cardiomyocyte misalignment, cytoplasmic vacuolization, and extensive fibrosis. (kolokotronis2019biallelicmutationin pages 1-2, kolokotronis2019biallelicmutationin pages 7-9)

No reproducible LVNC10-specific epigenetic alteration, chromosomal rearrangement, methylation signature, or validated modifier gene has been established. Whole-gene MYBPC3 deletion can contribute to severe biallelic disease, so copy-number analysis is clinically relevant in selected cases. (kolokotronis2019biallelicmutationin pages 7-9)

## 5. Environmental information

Environmental exposures are best understood as **phenocopy or expression modifiers**, not primary causes of LVNC10. High preload/afterload in pregnancy, endurance exercise, and chronic anemia can produce reversible or persistent hypertrabeculation. The completed MARATHON study, NCT02568072, prospectively examined 120 healthy first-time marathon runners with echocardiography and CMR; its registry notes that no remodeling was observed from baseline to post-marathon time points. (NCT02568072 chunk 1, NCT02568072 chunk 2)

No infectious agent, zoonosis, radiation exposure, pollutant, or occupational toxicant is implicated. Ordinary cardiovascular-health measures remain advisable but are not proven to prevent the genetic disease.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream germline event:** pathogenic MYBPC3 variation alters the quantity, stability, or function of cardiac myosin-binding protein C.
2. **Sarcomeric defect:** impaired thick-filament regulation and sarcomere organization perturb cardiomyocyte force generation, relaxation, and mechanosensing.
3. **Developmental/remodeling consequence:** altered myocardial growth and contractile signaling may bias the balance between compact and trabecular layers or cause hypertrabeculation as a secondary cardiomyopathy phenotype.
4. **Tissue remodeling:** cardiomyocyte disarray, stretch, cell injury, and fibrosis impair systolic/diastolic function.
5. **Clinical outputs:** heart failure, conduction heterogeneity, re-entry/ventricular arrhythmia, stasis in deep recesses, thromboembolism, and sudden death.

Human genetic data argue against one universal “failure of embryonic compaction” mechanism. The 840-case study concluded that LVNC has “substantial genetic overlap” with HCM/DCM, although truncating MYH7, ACTN2, and PRDM16 variants and selected RYR2/HCN4 variants define more LVNC- or arrhythmia-specific etiologies. MYH7 truncating variants were **20-fold enriched** in LVNC cases. These findings contextualize, but do not redefine, MYBPC3-associated LVNC10. (mazzarotto2021systematiclargescaleassessment pages 1-2)

### Suggested ontology annotations

- **GO biological process:** sarcomere organization; cardiac muscle contraction; regulation of cardiac muscle contraction; ventricular cardiac muscle tissue morphogenesis; cardiac muscle cell development; response to mechanical stimulus.
- **GO cellular component:** sarcomere, A band, myosin filament, cardiac myofibril.
- **Cell Ontology:** cardiomyocyte; ventricular cardiac muscle cell; cardiac conduction cell where electrophysiologic disease is documented.
- **Downstream processes:** fibrosis, abnormal impulse propagation, and hemodynamic stasis. Immune activation is not an established primary LVNC10 mechanism.

### Molecular profiling and advanced technology

Subtype-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, and CRISPR-screen signatures were not identified. The strongest human molecular evidence is diseased cardiac tissue showing reduced MYBPC3 transcript/protein and structural disorganization. Broad-LVNC mitochondrial bioenergetics is an active research area, but it should not be imported as an established LVNC10 mechanism. (kolokotronis2019biallelicmutationin pages 7-9, mahendran2024emerginghallmarksof pages 6-10)

## 7. Anatomical structures affected

- **Primary organ/system:** heart/cardiovascular system.
- **Primary site:** LV myocardium, especially apical and mid-inferolateral endocardial regions.
- **Layers:** thick trabecular/noncompacted endocardial layer over a thinner compact epicardial layer; deep recesses communicate with the LV cavity, not the coronary circulation.
- **Tissues/cells:** cardiac muscle tissue and ventricular cardiomyocytes; conduction tissue is functionally involved in arrhythmic cases.
- **Subcellular structures:** sarcomere, thick filament, A band, myofibril.
- **Secondary organs:** brain and systemic organs may be injured by embolism; lungs, liver, and kidneys may be affected secondarily by advanced heart failure.
- **Lateralization:** left-sided by definition, although biventricular hypertrabeculation may occur in broader disease.
- **Suggested UBERON:** heart, left ventricle, myocardium, ventricular myocardium, endocardium.

## 8. Temporal development

Onset ranges from prenatal/infantile to late adulthood. Heterozygous MYBPC3 disease may remain asymptomatic for years because penetrance is incomplete and age dependent. Biallelic disease can present in infancy or childhood with rapidly progressive heart failure and transplantation. (kolokotronis2019biallelicmutationin pages 1-2)

Course categories include:

- stable asymptomatic morphology with preserved EF;
- slowly progressive HCM/DCM phenotype;
- episodic arrhythmia or embolism;
- advanced systolic failure requiring ICD/CRT, mechanical support, or transplantation.

Morphologic hypertrabeculation may regress when loading conditions normalize, especially after pregnancy; that reversibility supports an acquired trait rather than inherited LVNC10 in many imaging-positive individuals. In one reviewed pregnancy series, 73% showed complete postpartum resolution. (arbustini2014leftventricularnoncompaction pages 1-2)

## 9. Inheritance and population

### Inheritance

The expected LVNC10 pattern is **autosomal dominant**, with variable expressivity and incomplete/age-dependent penetrance. Broad LVNC also includes X-linked, recessive, and mitochondrial disorders; those inheritance modes should not be assigned to LVNC10 without a second diagnosis. (sedaghathamedani2017clinicalgeneticsand pages 1-2)

No validated anticipation, common germline mosaicism rate, LVNC10 founder effect, carrier frequency, consanguinity effect, or sex ratio was identified. The R820W allele is notable in Ragdoll cats but this does not establish a human founder effect.

### Epidemiology

A trustworthy incidence or prevalence for **genetically confirmed LVNC10** is unavailable. Historical estimates for clinically diagnosed isolated LVNC were **0.05–0.24%**, but imaging criteria substantially inflate apparent prevalence. Eight percent of healthy controls met at least one echocardiographic criterion in one study, while Petersen CMR criteria labeled 25.7% of one low-risk multiethnic cohort. More conservative modern summaries note that up to 15% of apparently healthy people exceed an NC/C threshold on sensitive CMR. (NCT02568072 chunk 1, mazzarotto2021systematiclargescaleassessment pages 1-2, walsh2023thetroublewith pages 1-2)

Pediatric LVNC has been estimated at approximately **2% of children with known congenital heart disease**, while about 12% of diagnosed LVNC patients in one series had additional congenital heart disease. These broad-LVNC figures are not LVNC10 prevalence estimates. (fitzsimons2024electrophysiologicalphenotypingof pages 1-3)

## 10. Diagnostics

### Clinical pathway

1. **History and pedigree:** heart failure, syncope, palpitations, embolism, sudden death, HCM/DCM, and neuromuscular/syndromic disease over at least three generations.
2. **Examination and baseline testing:** ECG, echocardiography, ambulatory rhythm monitoring, and laboratory evaluation for secondary cardiomyopathy; natriuretic peptides and troponin assess severity but are not specific.
3. **CMR:** quantify function and morphology and identify late gadolinium enhancement/fibrosis or thrombus.
4. **Genetics:** counseling followed by a curated cardiomyopathy panel including MYBPC3; test the familial variant in relatives when pathogenic/likely pathogenic.
5. **Extended testing:** deletion/duplication analysis, WES/WGS, and mitochondrial analysis when panel-negative, syndromic, or severe early-onset disease suggests another cause.

### Imaging criteria and limitations

Common echocardiographic criteria include a two-layered myocardium, deep perfused recesses, and an end-systolic NC/C ratio **>2**. CMR commonly uses an end-diastolic NC/C ratio **>2.3** or trabeculated-mass/fractal measures. No criterion is a gold standard, and methods differ by imaging plane and cardiac phase. (mahendran2024emerginghallmarksof pages 6-10, mazzarotto2021systematiclargescaleassessment pages 1-2)

The central diagnostic safeguard is to require concordance among **morphology, ventricular function, tissue characterization, ECG/rhythm findings, family history, and genotype**. The 2023 ESC interpretation explicitly calls LV noncompaction a dynamic trait, while advanced imaging and genetics are essential components of cardiomyopathy workup. DOI: https://doi.org/10.1093/eurheartjsupp/suae002; published April 2024. (grasso2024thenew2023 pages 1-2)

### Differential diagnosis

- physiologic trabeculation in athletes or pregnancy;
- ancestry-associated normal variation;
- HCM or DCM with secondary hypertrabeculation;
- athlete’s heart;
- chronic anemia/sickle-cell remodeling;
- congenital heart disease;
- endocardial fibroelastosis, apical HCM, thrombus, or prominent papillary muscles;
- arrhythmogenic forms due to HCN4 or RYR2;
- syndromic/metabolic disease, including TAFAZZIN/Barth syndrome, LAMP2/Danon disease, mitochondrial disease, and neuromuscular disorders.

### Screening

Population or newborn screening is not recommended. First-degree relatives should receive genetic counseling and phenotype screening with ECG and echocardiography; variant-positive relatives require age-appropriate longitudinal surveillance. A negative familial-variant test can usually release a relative from genotype-driven surveillance, provided the familial variant is securely pathogenic and no independent clinical abnormality exists.

## 11. Outcome and prognosis

No LVNC10-specific five- or ten-year survival estimate exists. In a human LVNC cohort of 95 patients followed for a median **61 months**, LVNC was associated with more cardiovascular events than age-matched nonischemic DCM (**hazard ratio 2.481, p=0.002**); nuclear-envelope/RBM20 genotypes were especially adverse. This is broad-LVNC evidence and may reflect referral severity. (sedaghathamedani2017clinicalgeneticsand pages 1-2)

Conversely, morphology alone has weak prognostic value. In MESA, excessive trabeculation did not predict deterioration in LV volume or function over **10 years**; in DCM cohorts, NC/C mass or length did not predict event-free survival over median **3.4 years**. Preserved EF and otherwise normal apical architecture were associated with survival comparable to the general population. (walsh2023thetroublewith pages 1-2, fitzsimons2024electrophysiologicalphenotypingof pages 1-3)

Important adverse prognostic factors are reduced EF, ventricular dilation, heart-failure symptoms, myocardial fibrosis/LGE, ventricular arrhythmia, syncope, family history of sudden death, intracardiac thrombus/embolism, and high-risk genetic context. Major morbidities are heart failure, hospitalization, stroke, arrhythmia, device implantation, and transplantation. Validated LVNC10-specific prognostic biomarkers and quality-of-life estimates are lacking.

## 12. Treatment

There is **no approved disease-modifying or MYBPC3-directed treatment specifically for LVNC10**. Management follows the expressed cardiomyopathy phenotype:

- **Heart failure:** guideline-directed therapy for reduced EF—typically an ARNI/ACE inhibitor/ARB, evidence-based beta blocker, mineralocorticoid-receptor antagonist, and SGLT2 inhibitor as tolerated; diuretics for congestion.
- **Arrhythmias:** beta blockade or appropriate antiarrhythmic therapy, ambulatory monitoring, electrophysiology evaluation, and catheter ablation for suitable tachyarrhythmias.
- **ICD:** standard primary- or secondary-prevention indications based on EF, documented VT/VF, syncope, genotype/fibrosis, and overall risk—not trabeculation alone.
- **CRT:** standard electrical/mechanical dyssynchrony indications; individual severe pediatric cases have benefited, but this is not LVNC10-specific evidence. (mahendran2024emerginghallmarksof pages 6-10)
- **Anticoagulation:** indicated for atrial fibrillation, documented LV thrombus, previous systemic embolism, or other standard high-risk settings. Routine anticoagulation solely for trabeculation remains unsupported.
- **Advanced failure:** mechanical circulatory support and heart transplantation. Severe biallelic MYBPC3 LVNC has required transplantation. (kolokotronis2019biallelicmutationin pages 1-2)
- **Exercise:** individualized advice based on EF, arrhythmia, symptoms, fibrosis, and family history; morphology alone should not automatically disqualify an asymptomatic athlete.

Suggested NCIT intervention concepts include heart-failure therapy, anticoagulation therapy, catheter ablation, implantable cardioverter-defibrillator, cardiac resynchronization therapy, ventricular-assist device therapy, and heart transplantation. No LVNC10 pharmacogenomic rule or combination regimen has been validated.

### Trials and real-world implementation

- **NCT06024759**, *Predictors of Risk in Left Ventricular Non-Compaction*: recruiting observational adult registry, target **500**, started 1 September 2023, estimated completion 1 August 2033. It examines genetic mutations, LV strain, PVC burden, NSVT, LV dysfunction, and predictors of ICD implantation. https://clinicaltrials.gov/study/NCT06024759 (NCT06024759 chunk 1)
- **NCT06607471:** recruiting large nonischemic-cardiomyopathy registry that includes LVNC and tracks death, arrhythmia, AV block, transplantation, end-stage failure, and ventricular dysfunction over as long as 30 years. (NCT06607471 chunk 23)
- **NCT01470014:** completed prospective CT diagnostic study, actual enrollment **39**. https://clinicaltrials.gov/study/NCT01470014 (NCT01470014 chunk 1)
- **NCT02568072 (MARATHON):** completed prospective physiologic-remodeling study, actual enrollment **120**. https://clinicaltrials.gov/study/NCT02568072 (NCT02568072 chunk 1, NCT02568072 chunk 2)

No interventional gene, RNA, cell, CRISPR, or MYBPC3-targeted LVNC10 trial was identified.

## 13. Prevention

### Primary prevention

Inherited LVNC10 cannot currently be prevented by lifestyle, medication, or immunization. Reproductive options after counseling include prenatal diagnosis and preimplantation genetic testing for a known familial pathogenic variant, with attention to incomplete penetrance and variable expressivity.

### Secondary prevention

- cascade genetic and clinical screening;
- periodic ECG, echocardiography, and rhythm monitoring in at-risk relatives;
- CMR when echo is equivocal or fibrosis/thrombus assessment is needed;
- early treatment of ventricular dysfunction and clinically important arrhythmia.

### Tertiary prevention

Optimize heart-failure therapy, control arrhythmias, anticoagulate for established indications, use ICD/CRT according to risk, and manage exercise and pregnancy through specialist cardiogenetic care. There is no LVNC-specific vaccine, chemoprophylaxis, or public-health environmental intervention.

## 14. Other species and natural disease

The **MYBPC3 R820W** allele is naturally associated with hypertrophic cardiomyopathy and cardiac death in Ragdoll cats; the homologous feline protein change is commonly reported as R820W/R818W depending on sequence convention. This provides comparative evidence for conserved MYBPC3 sarcomeric pathogenicity, but feline disease is principally HCM and is **not a validated natural model of human LVNC10**. A 2024 feline review identifies MYBPC3 R818W and A31P as pathogenic HCM variants. DOI: https://doi.org/10.3390/cimb46080517. No zoonotic transmission is possible because LVNC10 is inherited, not infectious.

Suggested taxonomy: *Homo sapiens* NCBI Taxon 9606; *Felis catus* NCBI Taxon 9685. A verified VBO identifier for Ragdoll was not recovered.

## 15. Model organisms and experimental systems

- **Human cardiac tissue:** strongest LVNC10-relevant mechanistic system; biallelic MYBPC3 disease demonstrated protein depletion, transcript reduction, cardiomyocyte disarray, vacuolization, and fibrosis. Limitation: end-stage tissue cannot separate primary developmental changes from secondary remodeling. (kolokotronis2019biallelicmutationin pages 7-9)
- **Mybpc3 knockout/knock-in mice:** widely used HCM models reproduce haploinsufficiency, hypertrophy, contractile dysfunction, and proteostasis abnormalities. Autophagy activation improved cardiomyopathy in one targeted knock-in model, but this is preclinical HCM evidence—not proof of efficacy or phenotype reversal in LVNC10.
- **Cellular/iPSC systems:** patient-specific iPSC cardiomyocytes are suitable for sarcomere assembly, calcium handling, contractility, and allele-correction studies, but no retrieved LVNC10-specific validated organoid or iPSC therapeutic dataset was found.
- **Developmental LVNC models:** mouse, zebrafish, and other models manipulating Notch/neuregulin, endocardial–myocardial signaling, mitochondrial function, or sarcomeric genes illuminate trabeculation. Their limitation is that developmental noncompaction may not reproduce adult MYBPC3 cardiomyopathy with secondary hypertrabeculation.

Relevant resources include MGI, IMPC, IMSR/MMRRC, ZFIN, Cellosaurus, and the Alliance of Genome Resources.

## Evidence-quality assessment and knowledge-base cautions

1. **High confidence:** LVNC10–MYBPC3 association and MONDO:0014163; MYBPC3 is a causal cardiomyopathy gene. (OpenTargets Search: left ventricular noncompaction-MYBPC3)
2. **Moderate confidence:** MYBPC3 dosage/protein instability can produce severe LVNC morphology, especially in biallelic disease. (kolokotronis2019biallelicmutationin pages 1-2, kolokotronis2019biallelicmutationin pages 7-9)
3. **Limited subtype-specific evidence:** penetrance, prevalence, sex ratio, natural history, survival, treatment response, and quality of life.
4. **Do not infer disease from morphology alone:** up to 15% of apparently healthy people can exceed sensitive CMR NC/C thresholds, and physiologic remodeling may be reversible. (mazzarotto2021systematiclargescaleassessment pages 1-2, walsh2023thetroublewith pages 1-2)
5. **Variant-level caution:** the historic p.Arg820Trp/R820W association should be curated using current ClinVar/ClinGen and population-frequency evidence before being labeled pathogenic in a patient.
6. **Unavailable/not established:** specific protective alleles; toxins or infections; LVNC10 epigenetic, single-cell, spatial, proteomic, metabolomic, or lipidomic signatures; validated circulating biomarkers; genotype-specific pharmacotherapy; gene/RNA/cell therapy; and subtype-specific interventional trials.

References

1. (OpenTargets Search: left ventricular noncompaction-MYBPC3): Open Targets Query (left ventricular noncompaction-MYBPC3, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (grasso2024thenew2023 pages 1-2): Maurizia Grasso, Davide Bondavalli, Viviana Vilardo, Claudia Cavaliere, Ilaria Gatti, Alessandro Di Toro, Lorenzo Giuliani, Mario Urtis, Michela Ferrari, Barbara Cattadori, Alessandra Serio, Carlo Pellegrini, and Eloisa Arbustini. The new 2023 esc guidelines for the management of cardiomyopathies: a guiding path for cardiologist decisions. European Heart Journal Supplements : Journal of the European Society of Cardiology, 26:i1-i5, Apr 2024. URL: https://doi.org/10.1093/eurheartjsupp/suae002, doi:10.1093/eurheartjsupp/suae002. This article has 18 citations.

3. (walsh2023thetroublewith pages 1-2): Roddy Walsh. The trouble with trabeculation: how genetics can help to unravel a complex and controversial phenotype. Journal of cardiovascular translational research, 16:1310-1324, Nov 2023. URL: https://doi.org/10.1007/s12265-023-10459-6, doi:10.1007/s12265-023-10459-6. This article has 11 citations and is from a peer-reviewed journal.

4. (sedaghathamedani2017clinicalgeneticsand pages 1-2): Farbod Sedaghat-Hamedani, Jan Haas, Feng Zhu, Christian Geier, Elham Kayvanpour, Martin Liss, Alan Lai, Karen Frese, Regina Pribe-Wolferts, Ali Amr, Daniel Tian Li, Omid Shirvani Samani, Avisha Carstensen, Diana Martins Bordalo, Marion Müller, Christine Fischer, Jing Shao, Jing Wang, Ming Nie, Li Yuan, Sabine Haßfeld, Christine Schwartz, Min Zhou, Zihua Zhou, Yanwen Shu, Min Wang, Kai Huang, Qiutang Zeng, Longxian Cheng, Tobias Fehlmann, Philipp Ehlermann, Andreas Keller, Christoph Dieterich, Katrin Streckfuß-Bömeke, Yuhua Liao, Michael Gotthardt, Hugo A Katus, and Benjamin Meder. Clinical genetics and outcome of left ventricular non-compaction cardiomyopathy. European Heart Journal, 38:3449–3460, Dec 2017. URL: https://doi.org/10.1093/eurheartj/ehx545, doi:10.1093/eurheartj/ehx545. This article has 280 citations and is from a highest quality peer-reviewed journal.

5. (NCT06024759 chunk 1):  Predictors of Risk in Left Ventricular Non-Compaction. London Health Sciences Centre Research Institute OR Lawson Research Institute of St. Joseph's. 2023. ClinicalTrials.gov Identifier: NCT06024759

6. (mazzarotto2021systematiclargescaleassessment pages 1-2): Francesco Mazzarotto, Megan H. Hawley, Matteo Beltrami, Leander Beekman, Antonio de Marvao, Kathryn A. McGurk, Ben Statton, Beatrice Boschi, Francesca Girolami, Angharad M. Roberts, Elisabeth M. Lodder, Mona Allouba, Soha Romeih, Yasmine Aguib, A. John Baksi, Antonis Pantazis, Sanjay K. Prasad, Elisabetta Cerbai, Magdi H. Yacoub, Declan P. O’Regan, Stuart A. Cook, James S. Ware, Birgit Funke, Iacopo Olivotto, Connie R. Bezzina, Paul J.R. Barton, and Roddy Walsh. Systematic large-scale assessment of the genetic architecture of left ventricular noncompaction reveals diverse etiologies. Genetics in Medicine, 23:856-864, May 2021. URL: https://doi.org/10.1038/s41436-020-01049-x, doi:10.1038/s41436-020-01049-x. This article has 96 citations and is from a highest quality peer-reviewed journal.

7. (kolokotronis2019biallelicmutationin pages 7-9): Konstantinos Kolokotronis, Jirko Kühnisch, Eva Klopocki, Josephine Dartsch, Simone Rost, Cathleen Huculak, Giulia Mearini, Stefan Störk, Lucie Carrier, Sabine Klaassen, and Brenda Gerull. Biallelic mutation in myh7 and mybpc3 leads to severe cardiomyopathy with left ventricular noncompaction phenotype. Human Mutation, 40:1101-1114, Aug 2019. URL: https://doi.org/10.1002/humu.23757, doi:10.1002/humu.23757. This article has 46 citations and is from a domain leading peer-reviewed journal.

8. (kolokotronis2019biallelicmutationin pages 1-2): Konstantinos Kolokotronis, Jirko Kühnisch, Eva Klopocki, Josephine Dartsch, Simone Rost, Cathleen Huculak, Giulia Mearini, Stefan Störk, Lucie Carrier, Sabine Klaassen, and Brenda Gerull. Biallelic mutation in myh7 and mybpc3 leads to severe cardiomyopathy with left ventricular noncompaction phenotype. Human Mutation, 40:1101-1114, Aug 2019. URL: https://doi.org/10.1002/humu.23757, doi:10.1002/humu.23757. This article has 46 citations and is from a domain leading peer-reviewed journal.

9. (arbustini2014leftventricularnoncompaction pages 1-2): Eloisa Arbustini, Frank Weidemann, and Jennifer L. Hall. Left ventricular noncompaction: a distinct cardiomyopathy or a trait shared by different cardiac diseases? Journal of the American College of Cardiology, 64 17:1840-50, Oct 2014. URL: https://doi.org/10.1016/j.jacc.2014.08.030, doi:10.1016/j.jacc.2014.08.030. This article has 324 citations and is from a highest quality peer-reviewed journal.

10. (fitzsimons2024electrophysiologicalphenotypingof pages 1-3): Lindsey A. Fitzsimons, Delanie M. Kneeland‐Barber, Gracie C. Hannigan, David A. Karpe, Lyman Wu, Michael Colon, Jess Randall, and Kerry L. Tucker. Electrophysiological phenotyping of left ventricular noncompaction cardiomyopathy in pediatric populations: a systematic review. Physiological Reports, Apr 2024. URL: https://doi.org/10.14814/phy2.16029, doi:10.14814/phy2.16029. This article has 3 citations and is from a peer-reviewed journal.

11. (fitzsimons2024electrophysiologicalphenotypingof pages 8-10): Lindsey A. Fitzsimons, Delanie M. Kneeland‐Barber, Gracie C. Hannigan, David A. Karpe, Lyman Wu, Michael Colon, Jess Randall, and Kerry L. Tucker. Electrophysiological phenotyping of left ventricular noncompaction cardiomyopathy in pediatric populations: a systematic review. Physiological Reports, Apr 2024. URL: https://doi.org/10.14814/phy2.16029, doi:10.14814/phy2.16029. This article has 3 citations and is from a peer-reviewed journal.

12. (mahendran2024emerginghallmarksof pages 6-10): Gowthami Mahendran and Margaret A. Schwarz. Emerging hallmarks of mitochondrial biochemistry in cardiac trabecular morphogenesis and left ventricular noncompaction (lvnc). New Insights on Cardiomyopathy, Feb 2024. URL: https://doi.org/10.5772/intechopen.109098, doi:10.5772/intechopen.109098. This article has 3 citations.

13. (NCT02568072 chunk 1):  Training-induced Increased Left Ventricular Trabeculation. St George's, University of London. 2015. ClinicalTrials.gov Identifier: NCT02568072

14. (NCT06607471 chunk 23): Giovanni Peretto. Multimodal and Multidisciplinary Approach to Optimize Diagnostic, Prognostic, and Therapeutic Management of Patients with Non-ischemic Cardiomyopathies and Arrhythmogenic-inflammatory Phenotypes: a Multicenter, Observational, Retrospective and Prospective Registry Study.. Scientific Institute San Raffaele. 2018. ClinicalTrials.gov Identifier: NCT06607471

15. (NCT01470014 chunk 1):  Cardiac Computed Tomography: Characteristics of Isolated Left Ventricular Non-compaction. University of Zurich. 2011. ClinicalTrials.gov Identifier: NCT01470014

16. (walsh2023thetroublewith pages 11-13): Roddy Walsh. The trouble with trabeculation: how genetics can help to unravel a complex and controversial phenotype. Journal of cardiovascular translational research, 16:1310-1324, Nov 2023. URL: https://doi.org/10.1007/s12265-023-10459-6, doi:10.1007/s12265-023-10459-6. This article has 11 citations and is from a peer-reviewed journal.

17. (NCT02568072 chunk 2):  Training-induced Increased Left Ventricular Trabeculation. St George's, University of London. 2015. ClinicalTrials.gov Identifier: NCT02568072

18. (fitzsimons2024electrophysiologicalphenotypingof pages 7-8): Lindsey A. Fitzsimons, Delanie M. Kneeland‐Barber, Gracie C. Hannigan, David A. Karpe, Lyman Wu, Michael Colon, Jess Randall, and Kerry L. Tucker. Electrophysiological phenotyping of left ventricular noncompaction cardiomyopathy in pediatric populations: a systematic review. Physiological Reports, Apr 2024. URL: https://doi.org/10.14814/phy2.16029, doi:10.14814/phy2.16029. This article has 3 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Left_Ventricular_Noncompaction_10-deep-research-falcon_artifacts/artifact-00.md)

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