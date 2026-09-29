---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T19:02:20.739639'
end_time: '2026-08-28T19:15:41.437520'
duration_seconds: 800.7
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: short-rib thoracic dysplasia 21 without polydactyly (SRTD21, biallelic
    KIAA0753/MOONRAKER)
  mondo_id: MONDO:0030356
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
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0030356
    reported_labels:
    - if available
    ontology_label: short-rib thoracic dysplasia 21 without polydactyly
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Short-rib_Thoracic_Dysplasia_21_Without_Polydactyly-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** short-rib thoracic dysplasia 21 without polydactyly (SRTD21, biallelic KIAA0753/MOONRAKER)
- **MONDO ID:** MONDO:0030356 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **short-rib thoracic dysplasia 21 without polydactyly (SRTD21, biallelic KIAA0753/MOONRAKER)** covering all of the
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
- **Disease Name:** short-rib thoracic dysplasia 21 without polydactyly (SRTD21, biallelic KIAA0753/MOONRAKER)
- **MONDO ID:** MONDO:0030356 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **short-rib thoracic dysplasia 21 without polydactyly (SRTD21, biallelic KIAA0753/MOONRAKER)** covering all of the
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


# Short-rib thoracic dysplasia 21 without polydactyly (SRTD21)

## Executive summary

SRTD21 is an exceptionally rare, congenital, autosomal-recessive skeletal ciliopathy caused by biallelic pathogenic variants in **KIAA0753**, encoding the centrosomal protein **MOONRAKER/MNR**, also called **OFIP**. Its defining clinical pattern is a narrow, hypoplastic thorax with short ribs, shortened tubular bones, metaphyseal/pelvic abnormalities, and no polydactyly. Respiratory insufficiency is the principal immediate threat. The phenotype belongs to a wider **KIAA0753-related ciliopathy continuum** that can include Joubert syndrome (JS), oral-facial-digital syndrome, brain malformations, and—in noncanonical overlapping cases—polydactyly. Therefore, “SRTD21 without polydactyly” should not be treated as synonymous with every biallelic KIAA0753 disorder. The published human evidence remains a collection of small families and individual cases rather than a population-based natural-history cohort. (faudi2020anewcase pages 1-5, hammarsjo2017novelkiaa0753mutations pages 6-9, hammarsjo2017novelkiaa0753mutations pages 1-2)

| Domain | Summary | Evidence strength | Key citations |
|---|---|---|---|
| Identity / identifiers | **Disease:** short-rib thoracic dysplasia 21 without polydactyly (SRTD21), a **Mendelian skeletal ciliopathy** associated with **biallelic KIAA0753** variants. **Gene/protein aliases:** KIAA0753, **MOONRAKER (MNR)**, **OFIP**. **MONDO:** MONDO:0030356. **OMIM caution:** available evidence clearly supports **KIAA0753 as the causal gene** and a broader KIAA0753-related ciliopathy spectrum; disease/gene OMIM distinctions should be checked in OMIM directly rather than inferred here. | Strong for disease-gene identity; moderate for exact cross-database identifier harmonization | (faudi2020anewcase pages 1-5, faudi2020anewcase pages 5-9, inskeep2022geneticandphenotypic pages 1-2, kumar2021aciliopathycomplex pages 1-2) |
| Inheritance | **Autosomal recessive**; reported affected individuals carry **biallelic** variants (homozygous or compound heterozygous). Several skeletal cases occurred in **consanguineous** families, but non-consanguineous families are also reported. | Strong | (stephen2017mutationsinkiaa0753 pages 1-3, faudi2020anewcase pages 5-9, hammarsjo2017novelkiaa0753mutations pages 5-6, hammarsjo2021highdiagnosticyield pages 2-3) |
| Core phenotype | Congenital/prenatal **narrow thorax**, **short ribs**, **short limbs/short tubular bones**, **brachydactyly**, abnormal pelvis including **trident acetabula/ilia**, neonatal or infantile **respiratory distress**, severe short stature, and variable developmental delay/hypotonia. **Polydactyly is absent in the canonical SRTD21 designation**, although some broader KIAA0753-spectrum cases reported in later literature show overlap with other ciliopathy phenotypes. | Strong for skeletal-respiratory core; moderate for full spectrum boundaries | (faudi2020anewcase pages 1-5, faudi2020anewcase pages 5-9, hammarsjo2017novelkiaa0753mutations pages 5-6, hammarsjo2017novelkiaa0753mutations pages 6-9, hammarsjo2017novelkiaa0753mutations pages 1-2) |
| Variants | Recurrently reported skeletal-dysplasia variants are mostly **predicted loss-of-function/truncating** alleles, including **c.970C>T (p.Arg324\*)**, **c.943C>T (p.Gln315\*)**, and **c.1271del (p.Pro424Hisfs\*9)**; one family in a later skeletal ciliopathy cohort had **c.810C>T (synonymous, splice-affecting candidate)**. Reported gnomAD frequencies for some KIAA0753 ciliopathy alleles are extremely low, and homozygotes were not observed in cited reports. | Strong for recurrent truncating skeletal alleles; moderate for complete variant catalog | (faudi2020anewcase pages 5-9, inskeep2022geneticandphenotypic pages 7-8, hammarsjo2017novelkiaa0753mutations pages 5-6, hammarsjo2021highdiagnosticyield pages 2-3) |
| Mechanism / pathophysiology | KIAA0753/MNR is a **centrosome/pericentriolar satellite and distal centriole protein** required for **primary ciliogenesis**. It functions with **OFD1, FOPNL, and CEP90** in a distal centriole module that helps establish **distal appendages**, recruit **CEP83**, support **preciliary vesicle docking**, and regulate **centriole length**. Loss impairs ciliation and downstream **SHH** and some **WNT** signaling; growth-plate and cerebellar developmental defects are consistent downstream consequences. | Strong | (inskeep2022geneticandphenotypic pages 1-2, inskeep2022geneticandphenotypic pages 8-10, kumar2021aciliopathycomplex pages 7-9, borgne2022theevolutionaryconserved pages 1-2, kumar2021aciliopathycomplex pages 1-2, kumar2021aciliopathycomplex pages 13-16, chang2021cep120mediatedkiaa0753recruitment pages 1-2) |
| Diagnosis | Real-world diagnosis has relied on **prenatal ultrasound**, **fetal MRI/brain MRI**, **skeletal survey/radiographs**, and **exome or genome sequencing**. Suggestive imaging includes short femurs/limbs, narrow thorax, trident pelvis, metaphyseal changes, and in some allelic-spectrum cases **molar tooth sign** or other CNS anomalies. Functional follow-up in research settings has used patient fibroblasts, RNA/cDNA studies, and variant rescue assays. | Strong for sequencing + imaging; moderate for functional assays as clinical tools | (stephen2017mutationsinkiaa0753 pages 1-3, faudi2020anewcase pages 1-5, inskeep2022geneticandphenotypic pages 5-7, inskeep2022geneticandphenotypic pages 8-10, hammarsjo2021highdiagnosticyield pages 2-3) |
| Prognosis | **Highly variable.** Reported outcomes range from **fetal loss/neonatal death** or death in childhood from **respiratory failure/pulmonary complications** to survival into childhood with chronic respiratory disease, growth failure, hypotonia, developmental delay, and ongoing support needs. Long-term natural history, life expectancy, and population survival statistics are **not established**. | Moderate for variability; weak for long-term statistics | (faudi2020anewcase pages 1-5, faudi2020anewcase pages 5-9, inskeep2022geneticandphenotypic pages 7-8, hammarsjo2017novelkiaa0753mutations pages 5-6, hammarsjo2017novelkiaa0753mutations pages 2-4) |
| Treatment / management | **No disease-specific or disease-modifying therapy established.** Management is supportive and multidisciplinary: neonatal/childhood **respiratory support** (e.g., tracheostomy, ventilation, CPAP), **feeding support** including tube feeding/gastrostomy, developmental therapies, and surveillance for renal/hepatic/neurologic complications as indicated by phenotype. No relevant interventional clinical trial was identified in the cited evidence. | Moderate for supportive care; weak for formal guidelines | (faudi2020anewcase pages 1-5, faudi2020anewcase pages 5-9) |
| Prevention / screening | **No primary prevention** known for the disease biology. For at-risk families, prevention is mainly **genetic counseling**, **carrier testing**, **prenatal diagnosis** by targeted familial-variant testing or exome/genome sequencing, and potentially **preimplantation genetic testing** if the familial variants are known. Population screening recommendations are **not established**. | Moderate | (stephen2017mutationsinkiaa0753 pages 1-3, faudi2020anewcase pages 1-5, hammarsjo2021highdiagnosticyield pages 2-3) |
| Models / comparative evidence | Experimental systems include **patient fibroblasts**, **NIH3T3 and RPE1 KIAA0753/MNR loss-of-function cells**, **mouse embryos** lacking **Mnr** with defective ciliogenesis/Hedgehog-linked development, **zebrafish kiaa0753 nonsense mutants** with curved body and altered cartilage patterning, and **Paramecium/mammalian comparative ciliogenesis studies** for conserved distal appendage assembly. A naturally occurring veterinary KIAA0753 disease homolog is **not established**. | Strong for engineered models; weak for natural animal disease | (inskeep2022geneticandphenotypic pages 8-10, kumar2021aciliopathycomplex pages 1-2, chang2021cep120mediatedkiaa0753recruitment pages 1-2, hammarsjo2017novelkiaa0753mutations pages 5-6, hammarsjo2017novelkiaa0753mutations pages 6-9) |
| Unknown / not established | Population **prevalence**, **incidence**, **carrier frequency**, penetrance estimates, validated **modifier genes**, environmental risk/protective factors, biomarker-based monitoring, and disease-specific pharmacologic/gene/RNA/cell therapies are **not established** in the cited evidence. | Strong for absence of established evidence | (faudi2020anewcase pages 1-5, inskeep2022geneticandphenotypic pages 1-2, hammarsjo2021highdiagnosticyield pages 2-3) |


*Table: This table provides a compact knowledge-base style summary of SRTD21 caused by biallelic KIAA0753 variants, covering identity, phenotype, mechanism, diagnosis, prognosis, management, prevention, and model systems. It also flags where evidence is strong versus where key aspects remain not established.*

## 1. Disease information

### Definition and nomenclature

SRTD21 is a developmental disorder of the skeleton caused by defective primary-cilium formation and signaling. The core manifestations—thoracic hypoplasia, short ribs, and short tubular bones—overlap Jeune asphyxiating thoracic dystrophy and the historical short-rib polydactyly syndromes. A 2020 case was explicitly described as a **KIAA0753-related variant of Jeune asphyxiating thoracic dystrophy** and fulfilled Jeune radiographic criteria while lacking both polydactyly and the molar-tooth sign. (faudi2020anewcase pages 1-5, faudi2020anewcase pages 5-9)

Suggested identifiers and names are:

- **MONDO:** MONDO:0030356, as supplied in the target specification.
- **Disease name:** short-rib thoracic dysplasia 21 without polydactyly; **SRTD21**.
- **Gene:** **KIAA0753**, aliases **MNR/MOONRAKER** and **OFIP**; the literature places the locus at 17p13.1 and describes a 19-exon gene encoding a 967-amino-acid, approximately 115-kDa protein. (faudi2020anewcase pages 5-9)
- **OMIM:** the reviewed literature cites **KIAA0753-related disease/gene entry 617112**. Because gene and phenotype numbers are easily conflated, the current disease-specific number should be verified directly in OMIM before database ingestion. (faudi2020anewcase pages 1-5)
- **Orphanet, MeSH, ICD-10/ICD-11:** no specific SRTD21 code was established in the retrieved primary literature. Clinically, broader skeletal-dysplasia/short-rib thoracic-dysplasia coding may be necessary.
- **Alternative labels:** KIAA0753-related skeletal ciliopathy; KIAA0753-related short-rib skeletal dysplasia; KIAA0753-related Jeune/asphyxiating thoracic dystrophy.

The evidence is **aggregated disease-level literature derived from deeply phenotyped individual patients and families**, not EHR-scale data. By 2017 four skeletal cases had been reported; the 2020 report called its subject the eighth known KIAA0753 case overall and fifth short-rib skeletal-dysplasia case. Subsequent reports broadened the allelic spectrum, so historical counts are publication-date dependent. (faudi2020anewcase pages 1-5, hammarsjo2017novelkiaa0753mutations pages 5-6)

## 2. Etiology, risk, and protective factors

The necessary causal factor is **biallelic germline KIAA0753 dysfunction**. Homozygous and compound-heterozygous truncating alleles segregate with disease, patient tissue shows deficient KIAA0753/ciliation, engineered loss abolishes ciliogenesis, and wild-type—but not patient-variant—KIAA0753 partially rescues ciliation. This provides human genetic plus functional evidence for loss of function. (inskeep2022geneticandphenotypic pages 8-10, hammarsjo2017novelkiaa0753mutations pages 5-6)

Established genetic risk is having two pathogenic alleles. Consanguinity was present in several initial skeletal families, but affected children also occurred in unrelated, nonconsanguineous families; consanguinity increases the probability of homozygosity but is not required. (stephen2017mutationsinkiaa0753 pages 3-5, faudi2020anewcase pages 5-9, hammarsjo2017novelkiaa0753mutations pages 6-9)

No reproducible susceptibility loci, validated modifier genes, protective variants, environmental triggers, infectious causes, toxic exposures, diet/lifestyle effects, or gene–environment interactions are established. Inskeep and colleagues found no simple genotype–phenotype correlation and proposed unidentified genetic or environmental modifiers as an explanation for marked variability; this is a hypothesis, not demonstrated G×E evidence. (inskeep2022geneticandphenotypic pages 10-11)

## 3. Phenotypes

Frequencies below are qualitative because ascertainment is sparse and phenotype definitions changed across reports.

- **Thoracic hypoplasia/narrow chest and short ribs**—congenital, usually severe, sometimes fetal-lethal; suggested HPO: *Narrow chest* **HP:0000774**, *Short ribs* **HP:0000773**, *Thoracic hypoplasia* **HP:0005257**. This is the principal SRTD21 feature and causes restrictive respiratory disease. (faudi2020anewcase pages 1-5, hammarsjo2017novelkiaa0753mutations pages 6-9)
- **Short limbs/tubular bones, rhizomelia or acromesomelia, severe short stature**—prenatal or congenital, persistent; HPO suggestions: *Short limb* HP:0009826, *Rhizomelia* HP:0008905, *Disproportionate short stature* HP:0003498. One surviving child measured −5.5 SD at four years. (faudi2020anewcase pages 1-5)
- **Metaphyseal and pelvic dysplasia**—trident acetabula/ilia, broad or flared metaphyses, short/bowed tubular bones, cone-shaped epiphyses, pectus deformity, and short metacarpals; HPO: *Metaphyseal dysplasia* HP:0100255, *Trident acetabulum* HP:0003170, *Bowing of long bones* HP:0006487. (hammarsjo2017novelkiaa0753mutations pages 2-4, hammarsjo2017novelkiaa0753mutations pages 4-5)
- **Brachydactyly and contractures**—congenital, variable; HPO: *Brachydactyly* HP:0001156 and *Flexion contracture* HP:0001371. **Polydactyly is absent in canonical SRTD21**, although it occurs in broader KIAA0753 JS/OFD overlap. (faudi2020anewcase pages 5-9, hammarsjo2017novelkiaa0753mutations pages 6-9)
- **Respiratory insufficiency**—neonatal respiratory distress, pulmonary hypoplasia, recurrent acute respiratory decompensation, chronic lung disease, atelectasis, and ventilatory dependence; HPO: *Neonatal respiratory distress* HP:0002643, *Pulmonary hypoplasia* HP:0002089, *Respiratory insufficiency* HP:0002093. Severity ranges from chronic CPAP need to neonatal/childhood death. (faudi2020anewcase pages 1-5, inskeep2022geneticandphenotypic pages 7-8, hammarsjo2017novelkiaa0753mutations pages 2-4)
- **Hypotonia and developmental delay**—variable, evident in infancy; HPO: *Generalized hypotonia* HP:0001290, *Global developmental delay* HP:0001263, *Delayed speech and language development* HP:0000750. These may reflect CNS ciliopathy, prolonged critical illness, or both. (faudi2020anewcase pages 1-5, hammarsjo2017novelkiaa0753mutations pages 2-4)
- **CNS abnormalities**—variable and not required for narrowly defined SRTD21: ventriculomegaly, corpus-callosum hypoplasia/agenesis, cerebellar vermis dysplasia, molar-tooth sign in overlap cases, cervical canal/craniovertebral-junction stenosis, and seizures. Suggested HPO: HP:0002119, HP:0002079, HP:0001320, HP:0002419, and HP:0001250. The 2020 SRTD21-like child had no molar-tooth sign but had occipitocervical narrowing and an arachnoid cyst. (faudi2020anewcase pages 5-9, hammarsjo2017novelkiaa0753mutations pages 2-4)
- **Craniofacial findings**—macrocephaly or prominent forehead, depressed/broad nasal bridge, anteverted nares, long philtrum, widely spaced teeth, large mouth, micrognathia, and low-set ears; individually variable. (faudi2020anewcase pages 1-5, hammarsjo2017novelkiaa0753mutations pages 5-6)
- **Other variable findings:** feeding difficulty; hepatomegaly; micropenis, hypospadias, or cryptorchidism; dental hypoplasia. Renal ultrasound/function and fundus examination were normal in the detailed 2020 survivor, although renal/hepatic disease remains biologically plausible in a ciliopathy and should be monitored. (faudi2020anewcase pages 5-9, inskeep2022geneticandphenotypic pages 7-8)

No EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study exists. Nevertheless, reported tracheostomy, nocturnal CPAP or continuous ventilation, tube feeding, delayed walking and speech, repeated intensive-care admissions, and assistive communication indicate major effects on mobility, communication, schooling, caregiver burden, and daily living. (faudi2020anewcase pages 1-5, inskeep2022geneticandphenotypic pages 5-7)

## 4. Genetic and molecular information

**KIAA0753** is the established causal gene. Reported SRTD/skel­etal alleles include:

- homozygous **NM_014804.3:c.970C>T, p.(Arg324Ter)** in three patients from two families;
- compound heterozygous **c.943C>T, p.(Gln315Ter)** and **c.1271del, p.(Pro424HisfsTer9)** in a severely affected fetus;
- homozygous **c.943C>T, p.(Gln315Ter)** in the 2020 survivor (ClinVar ID 428615);
- compound heterozygous **c.943C>T, p.(Gln315Ter)** and **c.2656C>T, p.(Arg886Ter)** in an infant who died at two weeks;
- a homozygous synonymous **c.810C>T, p.(=)** allele reported in two deceased siblings and investigated as splice-disrupting. (faudi2020anewcase pages 5-9, inskeep2022geneticandphenotypic pages 7-8, hammarsjo2017novelkiaa0753mutations pages 5-6, hammarsjo2021highdiagnosticyield pages 2-3)

Broader KIAA0753 ciliopathy alleles include **c.769A>G, p.(Arg257Gly)** plus **c.2359-1G>C, p.(Lys787_Gln789del)** in two JS siblings and **c.1891A>T, p.(Lys631Ter)** plus a frameshifting splice allele in OFD. These are relevant differential/allelic-spectrum evidence but should not automatically be annotated as SRTD21 variants. (stephen2017mutationsinkiaa0753 pages 6-8, faudi2020anewcase pages 5-9)

Where reported, alleles were absent or extremely rare in gnomAD and had no observed homozygotes. Examples from the expanded ciliopathy cohort include frequencies of 2.14×10⁻⁵ and 2.86×10⁻⁵ for p.Gln315Ter and p.Arg886Ter, respectively. (inskeep2022geneticandphenotypic pages 7-8)

Variants are **germline**, not somatic. Most skeletal alleles are nonsense, frameshift, or splice-disrupting loss-of-function variants. Five of six tested variant constructs generated truncated proteins, whereas p.Gln315Ter was below Western-blot detection; all six failed to rescue ciliation. A simple rule that truncating variants cause skeletal disease while distal missense variants cause JS was proposed in 2020, but the larger 2022 series found no robust genotype–phenotype correlation. (faudi2020anewcase pages 5-9, inskeep2022geneticandphenotypic pages 8-10, inskeep2022geneticandphenotypic pages 10-11)

No validated modifier gene, disease-specific epigenetic signature, recurrent pathogenic chromosomal rearrangement, or large-scale KIAA0753 structural variant has been established.

## 5. Environmental information

No toxin, radiation, pollution, occupational exposure, smoking, alcohol, diet, exercise pattern, or infectious agent causes or triggers SRTD21. Lifestyle modification cannot prevent an embryo with biallelic pathogenic variants from developing the disorder. Environmental factors may influence respiratory complications or general health, but this has not been studied specifically.

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. **Biallelic loss of functional KIAA0753/MNR** impairs a centrosomal/distal-centriolar scaffold.
2. MNR normally recruits **OFD1, FOPNL, and CEP90** at the distal centriole. CEP90 then recruits **CEP83** and supports construction of distal appendages required for basal-body membrane docking. (borgne2022theevolutionaryconserved pages 1-2, kumar2021aciliopathycomplex pages 13-16)
3. MNR loss also prevents normal removal of CP110/CEP97, reduces IFT88 and Myosin-Va-positive preciliary-vesicle recruitment, prevents vesicle docking, and dysregulates centriole length through failure to recruit OFD1. Approximately 30% of MNR-null RPE1 cells had hyperelongated centrioles. (kumar2021aciliopathycomplex pages 7-9)
4. Consequently, primary-cilium assembly fails or is markedly reduced. KIAA0753-null NIH3T3 cells had essentially no cilia; wild-type transfection raised ciliation from 4.4% to 28.5%, whereas six patient alleles yielded only 3.0–7.8%. Patient fibroblasts showed about a 50% reduction: approximately 15% versus 40% ciliated without stimulation and 30% versus 60% after serum starvation. (inskeep2022geneticandphenotypic pages 8-10)
5. Loss of the primary cilium disrupts developmental signal transduction. KIAA0753-null cells did not induce **GLI1** after Smoothened-agonist stimulation; patient fibroblast RNA-seq showed a blunted SHH response and failed normal **AXIN2** induction after WNT3A. (inskeep2022geneticandphenotypic pages 8-10)
6. In fetal growth plate, impaired ciliary signaling disrupts chondrocyte organization: the affected fetus had an abnormal proliferative zone and broad hypertrophic zone. This plausibly causes short/bowed bones, metaphyseal dysplasia, ribs too short to expand the thorax, pulmonary hypoplasia, and respiratory failure. (hammarsjo2017novelkiaa0753mutations pages 5-6, hammarsjo2017novelkiaa0753mutations pages 9-10)
7. In the cerebellum, CEP120-dependent recruitment of KIAA0753 to centrioles is required for granule-neuron progenitors to exit the germinal zone and differentiate. Disruption retains Ki67-positive/Tuj1-negative progenitors and provides a mechanistic route to heterotopia and vermian hypoplasia in JS-overlap disease. (chang2021cep120mediatedkiaa0753recruitment pages 1-2, chang2021cep120mediatedkiaa0753recruitment pages 10-12)

Suggested ontology annotations include **GO:0060271 cilium assembly**, **GO:0030030 cell projection organization**, **GO:0007099 centriole replication**, **GO:0097547 proximal/distal centriole-associated processes**, **GO:0007224 smoothened signaling pathway**, and **GO:0016055 Wnt signaling pathway**. Cellular-component terms include **GO:0005813 centrosome**, **GO:0005814 centriole**, **GO:0036064 ciliary basal body**, **GO:0097542 ciliary tip/appendage-related compartment**, and **GO:0043596 nuclear replication fork only if specifically justified—not as a disease annotation**.

Relevant cell types include growth-plate **chondrocytes** (CL:0000138), fibroblasts (CL:0000057), cerebellar granule-neuron progenitors and granule neurons, respiratory epithelial cells, and renal tubular epithelial cells. Direct disease evidence is strongest for chondrocytes and experimental fibroblasts; respiratory/renal cell involvement is inferred from anatomy and general ciliopathy biology.

### Molecular profiling and advanced technologies

Patient-fibroblast bulk RNA-seq demonstrated abnormal SHH/WNT response. Proteomics and super-resolution microscopy defined the DISCO complex, but no SRTD21 patient-tissue proteome was identified. No disease-specific metabolomic, lipidomic, methylomic, single-cell, spatial-transcriptomic, organoid, or multi-omics dataset was found. CRISPR knockout/rescue experiments constitute the strongest functional-genomics evidence. (inskeep2022geneticandphenotypic pages 8-10, kumar2021aciliopathycomplex pages 1-2)

## 7. Anatomical structures affected

Primary sites are the developing appendicular and axial skeleton—ribs, thoracic cage, long bones, metaphyses, growth plates, pelvis/acetabula, vertebrae, hands, and feet—and secondarily the lungs because the small thorax constrains development and ventilation. Suggested UBERON concepts include thoracic cage, rib, long bone, growth plate cartilage, pelvis, vertebral column, lung, and primary cilium/basal body at the subcellular level. (faudi2020anewcase pages 1-5, hammarsjo2017novelkiaa0753mutations pages 4-5)

Variable secondary involvement includes cerebellar vermis/brainstem, corpus callosum, cerebral ventricles, craniovertebral junction, pituitary, liver, kidney, eye, and external genitalia. Skeletal disease is generally bilateral and symmetric; no consistent lateralization is established. (faudi2020anewcase pages 5-9, inskeep2022geneticandphenotypic pages 7-8, hammarsjo2017novelkiaa0753mutations pages 2-4)

## 8. Temporal development

Onset is **prenatal/congenital**. Prenatal ultrasound may show short femora/long bones, narrow thorax, growth restriction, ventriculomegaly, or cerebellar abnormalities. Respiratory distress commonly begins at birth or in the neonatal period. (faudi2020anewcase pages 1-5, inskeep2022geneticandphenotypic pages 5-7)

There is no validated staging system. A practical course is: prenatal skeletal malformation; neonatal respiratory-risk phase; childhood chronic skeletal, pulmonary, feeding, and neurodevelopmental morbidity among survivors. Severity ranges from termination/fetal lethality or neonatal death to survival beyond childhood. Skeletal short stature and developmental impairment are lifelong; pulmonary support requirements may improve, persist, or prove fatal. No remission pattern is known. The prenatal and early neonatal periods are critical for diagnosis, delivery planning, and respiratory intervention. (faudi2020anewcase pages 1-5, inskeep2022geneticandphenotypic pages 7-8, hammarsjo2017novelkiaa0753mutations pages 2-4)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed heterozygous parents, each pregnancy has a theoretical 25% affected, 50% carrier, and 25% unaffected/noncarrier probability. Both sexes are affected. Penetrance for genuinely biallelic severe loss-of-function genotypes appears high, but cannot be estimated formally; expressivity is markedly variable. Anticipation is not expected, and germline mosaicism has not been demonstrated. (stephen2017mutationsinkiaa0753 pages 3-5, hammarsjo2017novelkiaa0753mutations pages 5-6)

No population prevalence, annual incidence, carrier frequency, sex ratio, geographic clustering, or validated founder effect is available. Initial families had Iranian, Indian, Italian, French, Welsh-Croatian, and German backgrounds, arguing against restriction to one ancestry. Recurrent p.Arg324Ter in consanguineous families could reflect local ancestry but is not a proven founder allele. (faudi2020anewcase pages 5-9)

## 10. Diagnostics

Diagnosis integrates:

1. **Prenatal imaging:** ultrasound for short long bones, small thorax, polyhydramnios and CNS malformations; fetal MRI when posterior-fossa or brainstem disease is suspected.
2. **Postnatal skeletal survey:** short/broad ribs, narrow thorax, shortened/bowed tubular bones, metaphyseal irregularity/flaring, trident ilia/acetabula, and brachydactyly.
3. **Brain and spine MRI:** assess molar-tooth sign, vermis/corpus-callosum abnormalities, ventriculomegaly, and craniocervical stenosis.
4. **Molecular testing:** a skeletal-ciliopathy/skeletal-dysplasia panel including **KIAA0753**, trio WES, or WGS, followed by segregation. CNV and RNA/cDNA analysis should be considered when only one allele is found or a synonymous/deep-intronic splice variant is suspected. Combined sequencing, CNV, and RNA analysis achieved a 90% diagnosis rate in a 34-person skeletal-ciliopathy cohort, although that statistic is not specific to SRTD21. (hammarsjo2021highdiagnosticyield pages 2-3)

WES identified the homozygous p.Gln315Ter case after a normal 46,XY karyotype. CMA, karyotype, and FISH can exclude alternative chromosomal disorders but do not directly test most KIAA0753 variants. Mitochondrial and repeat-expansion tests are not indicated. Patient-fibroblast ciliation, RNA-seq, or rescue assays are research-level tools for difficult variants rather than standard diagnostic criteria. (faudi2020anewcase pages 1-5, inskeep2022geneticandphenotypic pages 8-10)

Differential diagnoses include other SRTDs/Jeune syndromes due to **DYNC2H1, DYNC2LI1, WDR34, WDR35, WDR60, IFT80, IFT140, IFT172, TTC21B, TCTEX1D2, CEP120, INTU, NEK1, C2CD3**, Ellis–van Creveld syndrome (**EVC/EVC2**), cranioectodermal dysplasia, and KIAA0753-related JS/OFD. Absence of polydactyly does not identify KIAA0753 by itself; molecular confirmation is required. (faudi2020anewcase pages 1-5)

There is no population or newborn screening. Cascade carrier testing is appropriate after familial variants are established.

## 11. Outcome and prognosis

No five- or ten-year survival estimates, life-expectancy tables, mortality rate, validated prognostic model, or prognostic biomarker exists. Published outcomes include fetal lethality, death at two weeks from pulmonary hypertension, death at seven years from respiratory failure, and survival to four years with chronic lung disease, nocturnal CPAP, recurrent intensive-care admissions, severe short stature, and developmental delay. Thoracic size, pulmonary hypoplasia, neonatal respiratory requirement, pulmonary hypertension, and associated CNS disease are plausible prognostic factors, but none has been formally validated. (faudi2020anewcase pages 1-5, inskeep2022geneticandphenotypic pages 7-8, hammarsjo2017novelkiaa0753mutations pages 2-4)

Potential complications include restrictive respiratory failure, recurrent pulmonary decompensation, atelectasis/chronic lung disease, feeding failure, growth failure, orthopedic deformity/contracture, craniocervical stenosis, and developmental disability. Renal, hepatic, retinal, and endocrine surveillance is reasonable because of the broader allelic spectrum, but these complications are not uniformly present in SRTD21. (faudi2020anewcase pages 5-9)

## 12. Treatment and current applications

There is no approved disease-modifying drug, pharmacogenomic strategy, gene therapy, CRISPR therapy, RNA therapy, cell therapy, or targeted SHH/WNT treatment. No relevant interventional clinical trial was identified.

Real-world care is multidisciplinary and phenotype-directed:

- neonatal respiratory stabilization, ventilation, tracheostomy when necessary, nocturnal noninvasive ventilation/CPAP, treatment of wheeze/infections, and pulmonary-hypertension assessment;
- nutritional and swallowing assessment, gastrostomy or tube feeding when required;
- physical, occupational, speech, developmental, and augmentative-communication therapies;
- orthopedic monitoring of limb deformity, contractures, spine, and mobility;
- neurosurgical review for symptomatic cervical/foramen-magnum stenosis;
- periodic renal function/ultrasound, liver tests/ultrasound, ophthalmology, hearing, neurologic/developmental, and endocrine assessment when clinically indicated.

A reported child required tracheostomy and feeding tube at two months, later decannulated at 21 months, but continued nocturnal CPAP and inhaled corticosteroids for chronic pulmonary disease. This is case-specific evidence, not a treatment algorithm or response rate. (faudi2020anewcase pages 1-5, faudi2020anewcase pages 5-9)

Suggested NCIT intervention concepts include **Mechanical Ventilation**, **Tracheostomy**, **Continuous Positive Airway Pressure**, **Gastrostomy**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, and **Genetic Counseling**; exact NCIT codes should be validated in the current NCI Thesaurus release.

## 13. Prevention

There is no lifestyle, vaccine, drug, or environmental primary prevention. Prevention options are reproductive:

- carrier and cascade testing in relatives;
- preconception genetic counseling;
- targeted prenatal testing by chorionic-villus sampling or amniocentesis when familial variants are known;
- prenatal ultrasound/fetal MRI for early structural detection;
- preimplantation genetic testing for monogenic disease (PGT-M).

Tertiary prevention consists of early respiratory planning, nutritional support, rehabilitation, and surveillance to reduce complications. Counseling must emphasize variable expressivity: the same gene can produce lethal skeletal disease, viable SRTD, JS, or OFD-overlap phenotypes. (inskeep2022geneticandphenotypic pages 10-11, faudi2020anewcase pages 1-5)

## 14. Other species and natural disease

No naturally occurring companion-animal, livestock, or wildlife syndrome definitively homologous to human SRTD21 was identified; therefore breed ontology, veterinary prevalence, zoonotic potential, and cross-species transmission are not applicable. KIAA0753 function is evolutionarily conserved, but this is comparative biology rather than infectious transmission.

## 15. Model organisms

- **Zebrafish (*Danio rerio*, NCBI Taxon 7955):** homozygous nonsense *kiaa0753* mutants developed curved bodies, altered cranial cartilage patterning, significantly shortened cranial measurements (11 mutants versus 14 controls; five of six reported measurements p<0.01), and lethality beyond the first week. This model recapitulates ciliary and cartilage-development defects but not the complete human thoracic phenotype. (hammarsjo2017novelkiaa0753mutations pages 5-6, hammarsjo2017novelkiaa0753mutations pages 6-9)
- **Mouse (*Mus musculus*, Taxon 10090):** Mnr-null embryos showed defective neural-tube ciliogenesis and developmental/Hedgehog abnormalities. In vivo cerebellar electroporation established that centriolar KIAA0753 is required for timely differentiation and germinal-zone exit of granule-neuron progenitors. These models are mechanistically strong but incompletely model human SRTD survival and skeletal natural history. (kumar2021aciliopathycomplex pages 7-9, chang2021cep120mediatedkiaa0753recruitment pages 1-2, chang2021cep120mediatedkiaa0753recruitment pages 10-12)
- **Cellular models:** CRISPR KIAA0753-null NIH3T3 fibroblasts, MNR-null human RPE1 cells, patient dermal fibroblasts, and variant-rescue assays quantify ciliation, centriole morphology, and SHH/WNT signaling. (inskeep2022geneticandphenotypic pages 8-10, kumar2021aciliopathycomplex pages 7-9)
- **Paramecium:** comparative knockdown/localization studies demonstrate conserved CEP90–FOPNL–OFD1 distal-appendage and basal-body docking biology; mammals additionally require MNR upstream. This is valuable for organelle assembly but does not model human skeletal disease. (borgne2022theevolutionaryconserved pages 1-2)

## Key primary sources and recent-research assessment

The foundational SRTD21 study is Hammarsjö et al., **“Novel KIAA0753 mutations extend the phenotype of skeletal ciliopathies,” published November 2017**, *Scientific Reports*, DOI/URL: https://doi.org/10.1038/s41598-017-15442-1. Its abstract states: “We report biallelic pathogenic variants in KIAA0753 in four patients with short-rib type skeletal dysplasia,” and documents growth-plate and zebrafish cartilage abnormalities. (hammarsjo2017novelkiaa0753mutations pages 5-6, hammarsjo2017novelkiaa0753mutations pages 1-2)

Faudi et al., **published April 2020**, *European Journal of Medical Genetics*, DOI/URL: https://doi.org/10.1016/j.ejmg.2019.103823, provided the detailed viable p.Gln315Ter homozygote and stated that the case “illustrates how ciliopathies due to mutations in a single gene may present as apparently distinct syndromes.” (faudi2020anewcase pages 1-5)

Inskeep et al., accepted August 2021 and published in the 2022 volume of *American Journal of Medical Genetics A*, DOI/URL: https://doi.org/10.1002/ajmg.a.62497, added four individuals and functional rescue/RNA-seq data. Its abstract reports that “Ablation of KIAA0753 in vitro blocks primary ciliogenesis and SHH pathway activity” and that patient fibroblasts show abnormal SHH and WNT signaling. (inskeep2022geneticandphenotypic pages 1-2)

Kumar et al., **published July 2021**, *Journal of Cell Biology*, DOI/URL: https://doi.org/10.1083/jcb.202011133, defined the DISCO complex and concluded that it supports ciliogenesis by “restraining centriole length and assembling distal appendages.” (kumar2021aciliopathycomplex pages 1-2)

Le Borgne et al., **published September 7, 2022**, *PLOS Biology*, DOI/URL: https://doi.org/10.1371/journal.pbio.3001782, independently placed MNR upstream of OFD1/FOPNL/CEP90 and distal-appendage proteins. (borgne2022theevolutionaryconserved pages 1-2)

No 2023–2024 primary clinical natural-history study specific to SRTD21 was retrieved. Thus, despite the requested recency priority, the most authoritative disease-specific evidence remains the 2017–2022 primary literature. The major unresolved needs are a curated international registry, standardized phenotyping, definitive prevalence/carrier estimates, longitudinal respiratory and renal/hepatic outcomes, robust genotype–phenotype analysis, and therapeutic studies.

References

1. (faudi2020anewcase pages 1-5): Emilien Faudi, Elise Brischoux-Boucher, Céline Huber, Thibaud Dabudyk, Marion Lenoir, Geneviève Baujat, Caroline Michot, Lionel Van Maldergem, Valérie Cormier-Daire, and Juliette Piard. A new case of kiaa0753-related variant of jeune asphyxiating thoracic dystrophy. European Journal of Medical Genetics, 63:103823, Apr 2020. URL: https://doi.org/10.1016/j.ejmg.2019.103823, doi:10.1016/j.ejmg.2019.103823. This article has 11 citations and is from a peer-reviewed journal.

2. (hammarsjo2017novelkiaa0753mutations pages 6-9): A. Hammarsjö, Zheng Wang, Raquel Vaz, F. Taylan, M. Sedghi, K. Girisha, D. Chitayat, K. Neethukrishna, Patrick Shannon, Ruth Godoy, K. Gowrishankar, A. Lindstrand, Jafar Nasiri, M. Baktashian, Phillip T Newton, L. Guo, Wolfgang Hofmeister, M. Pettersson, A. Chagin, Gen Nishimura, Li Yan, Naomichi Matsumoto, Ann Nordgren, Noriko Miyake, G. Grigelioniene, and S. Ikegawa. Novel kiaa0753 mutations extend the phenotype of skeletal ciliopathies. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-15442-1, doi:10.1038/s41598-017-15442-1. This article has 41 citations and is from a peer-reviewed journal.

3. (hammarsjo2017novelkiaa0753mutations pages 1-2): A. Hammarsjö, Zheng Wang, Raquel Vaz, F. Taylan, M. Sedghi, K. Girisha, D. Chitayat, K. Neethukrishna, Patrick Shannon, Ruth Godoy, K. Gowrishankar, A. Lindstrand, Jafar Nasiri, M. Baktashian, Phillip T Newton, L. Guo, Wolfgang Hofmeister, M. Pettersson, A. Chagin, Gen Nishimura, Li Yan, Naomichi Matsumoto, Ann Nordgren, Noriko Miyake, G. Grigelioniene, and S. Ikegawa. Novel kiaa0753 mutations extend the phenotype of skeletal ciliopathies. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-15442-1, doi:10.1038/s41598-017-15442-1. This article has 41 citations and is from a peer-reviewed journal.

4. (faudi2020anewcase pages 5-9): Emilien Faudi, Elise Brischoux-Boucher, Céline Huber, Thibaud Dabudyk, Marion Lenoir, Geneviève Baujat, Caroline Michot, Lionel Van Maldergem, Valérie Cormier-Daire, and Juliette Piard. A new case of kiaa0753-related variant of jeune asphyxiating thoracic dystrophy. European Journal of Medical Genetics, 63:103823, Apr 2020. URL: https://doi.org/10.1016/j.ejmg.2019.103823, doi:10.1016/j.ejmg.2019.103823. This article has 11 citations and is from a peer-reviewed journal.

5. (inskeep2022geneticandphenotypic pages 1-2): Katherine A. Inskeep, Yuri A. Zarate, Danielle Monteil, Jurgen Spranger, Dan Doherty, Rolf W. Stottmann, and K. Nicole Weaver. Genetic and phenotypic heterogeneity in kiaa0753‐related ciliopathies. American Journal of Medical Genetics Part A, 188:104-115, Sep 2022. URL: https://doi.org/10.1002/ajmg.a.62497, doi:10.1002/ajmg.a.62497. This article has 8 citations.

6. (kumar2021aciliopathycomplex pages 1-2): Dhivya Kumar, Addison Rains, Vicente Herranz-Pérez, Quanlong Lu, Xiaoyu Shi, Danielle L. Swaney, Erica Stevenson, Nevan J. Krogan, Bo Huang, Christopher Westlake, Jose Manuel Garcia-Verdugo, Bradley K. Yoder, and Jeremy F. Reiter. A ciliopathy complex builds distal appendages to initiate ciliogenesis. Journal of Cell Biology, Jul 2021. URL: https://doi.org/10.1083/jcb.202011133, doi:10.1083/jcb.202011133. This article has 57 citations and is from a highest quality peer-reviewed journal.

7. (stephen2017mutationsinkiaa0753 pages 1-3): Joshi Stephen, Thierry Vilboux, Luhe Mian, Chulaluck Kuptanon, Courtney M. Sinclair, Deniz Yildirimli, Dawn M. Maynard, Joy Bryant, Roxanne Fischer, Meghana Vemulapalli, James C. Mullikin, Marjan Huizing, William A. Gahl, May Christine V. Malicdan, and Meral Gunay-Aygun. Mutations in kiaa0753 cause joubert syndrome associated with growth hormone deficiency. Human Genetics, 136:399-408, Feb 2017. URL: https://doi.org/10.1007/s00439-017-1765-z, doi:10.1007/s00439-017-1765-z. This article has 50 citations and is from a peer-reviewed journal.

8. (hammarsjo2017novelkiaa0753mutations pages 5-6): A. Hammarsjö, Zheng Wang, Raquel Vaz, F. Taylan, M. Sedghi, K. Girisha, D. Chitayat, K. Neethukrishna, Patrick Shannon, Ruth Godoy, K. Gowrishankar, A. Lindstrand, Jafar Nasiri, M. Baktashian, Phillip T Newton, L. Guo, Wolfgang Hofmeister, M. Pettersson, A. Chagin, Gen Nishimura, Li Yan, Naomichi Matsumoto, Ann Nordgren, Noriko Miyake, G. Grigelioniene, and S. Ikegawa. Novel kiaa0753 mutations extend the phenotype of skeletal ciliopathies. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-15442-1, doi:10.1038/s41598-017-15442-1. This article has 41 citations and is from a peer-reviewed journal.

9. (hammarsjo2021highdiagnosticyield pages 2-3): Anna Hammarsjö, Maria Pettersson, David Chitayat, Atsuhiko Handa, Britt-Marie Anderlid, Marco Bartocci, Donald Basel, Dominyka Batkovskyte, Ana Beleza-Meireles, Peter Conner, Jesper Eisfeldt, Katta M. Girisha, Brian Hon-Yin Chung, Eva Horemuzova, Hironobu Hyodo, Liene Korņejeva, Kristina Lagerstedt-Robinson, Angela E. Lin, Måns Magnusson, Shahida Moosa, Shalini S. Nayak, Daniel Nilsson, Hirofumi Ohashi, Naoko Ohashi-Fukuda, Henrik Stranneheim, Fulya Taylan, Rasa Traberg, Ulrika Voss, Valtteri Wirta, Ann Nordgren, Gen Nishimura, Anna Lindstrand, and Giedre Grigelioniene. High diagnostic yield in skeletal ciliopathies using massively parallel genome sequencing, structural variant screening and rna analyses. Journal of Human Genetics, 66:995-1008, Apr 2021. URL: https://doi.org/10.1038/s10038-021-00925-x, doi:10.1038/s10038-021-00925-x. This article has 41 citations and is from a peer-reviewed journal.

10. (inskeep2022geneticandphenotypic pages 7-8): Katherine A. Inskeep, Yuri A. Zarate, Danielle Monteil, Jurgen Spranger, Dan Doherty, Rolf W. Stottmann, and K. Nicole Weaver. Genetic and phenotypic heterogeneity in kiaa0753‐related ciliopathies. American Journal of Medical Genetics Part A, 188:104-115, Sep 2022. URL: https://doi.org/10.1002/ajmg.a.62497, doi:10.1002/ajmg.a.62497. This article has 8 citations.

11. (inskeep2022geneticandphenotypic pages 8-10): Katherine A. Inskeep, Yuri A. Zarate, Danielle Monteil, Jurgen Spranger, Dan Doherty, Rolf W. Stottmann, and K. Nicole Weaver. Genetic and phenotypic heterogeneity in kiaa0753‐related ciliopathies. American Journal of Medical Genetics Part A, 188:104-115, Sep 2022. URL: https://doi.org/10.1002/ajmg.a.62497, doi:10.1002/ajmg.a.62497. This article has 8 citations.

12. (kumar2021aciliopathycomplex pages 7-9): Dhivya Kumar, Addison Rains, Vicente Herranz-Pérez, Quanlong Lu, Xiaoyu Shi, Danielle L. Swaney, Erica Stevenson, Nevan J. Krogan, Bo Huang, Christopher Westlake, Jose Manuel Garcia-Verdugo, Bradley K. Yoder, and Jeremy F. Reiter. A ciliopathy complex builds distal appendages to initiate ciliogenesis. Journal of Cell Biology, Jul 2021. URL: https://doi.org/10.1083/jcb.202011133, doi:10.1083/jcb.202011133. This article has 57 citations and is from a highest quality peer-reviewed journal.

13. (borgne2022theevolutionaryconserved pages 1-2): Pierrick Le Borgne, Logan Greibill, Marine Hélène Laporte, Michel Lemullois, Khaled Bouhouche, Mebarek Temagoult, Olivier Rosnet, Maeva Le Guennec, Laurent Lignières, Guillaume Chevreux, France Koll, Virginie Hamel, Paul Guichard, and Anne-Marie Tassin. The evolutionary conserved proteins cep90, fopnl, and ofd1 recruit centriolar distal appendage proteins to initiate their assembly. PLOS Biology, 20:e3001782, Sep 2022. URL: https://doi.org/10.1371/journal.pbio.3001782, doi:10.1371/journal.pbio.3001782. This article has 27 citations and is from a highest quality peer-reviewed journal.

14. (kumar2021aciliopathycomplex pages 13-16): Dhivya Kumar, Addison Rains, Vicente Herranz-Pérez, Quanlong Lu, Xiaoyu Shi, Danielle L. Swaney, Erica Stevenson, Nevan J. Krogan, Bo Huang, Christopher Westlake, Jose Manuel Garcia-Verdugo, Bradley K. Yoder, and Jeremy F. Reiter. A ciliopathy complex builds distal appendages to initiate ciliogenesis. Journal of Cell Biology, Jul 2021. URL: https://doi.org/10.1083/jcb.202011133, doi:10.1083/jcb.202011133. This article has 57 citations and is from a highest quality peer-reviewed journal.

15. (chang2021cep120mediatedkiaa0753recruitment pages 1-2): Chia-Hsiang Chang, Ting-Yu Chen, I-Ling Lu, Rong-Bin Li, Jhih-Jie Tsai, Pin-Yeh Lin, and Tang K. Tang. Cep120-mediated kiaa0753 recruitment onto centrioles is required for timely neuronal differentiation and germinal zone exit in the developing cerebellum. Genes & Development, 35:1445-1460, Oct 2021. URL: https://doi.org/10.1101/gad.348636.121, doi:10.1101/gad.348636.121. This article has 9 citations and is from a highest quality peer-reviewed journal.

16. (inskeep2022geneticandphenotypic pages 5-7): Katherine A. Inskeep, Yuri A. Zarate, Danielle Monteil, Jurgen Spranger, Dan Doherty, Rolf W. Stottmann, and K. Nicole Weaver. Genetic and phenotypic heterogeneity in kiaa0753‐related ciliopathies. American Journal of Medical Genetics Part A, 188:104-115, Sep 2022. URL: https://doi.org/10.1002/ajmg.a.62497, doi:10.1002/ajmg.a.62497. This article has 8 citations.

17. (hammarsjo2017novelkiaa0753mutations pages 2-4): A. Hammarsjö, Zheng Wang, Raquel Vaz, F. Taylan, M. Sedghi, K. Girisha, D. Chitayat, K. Neethukrishna, Patrick Shannon, Ruth Godoy, K. Gowrishankar, A. Lindstrand, Jafar Nasiri, M. Baktashian, Phillip T Newton, L. Guo, Wolfgang Hofmeister, M. Pettersson, A. Chagin, Gen Nishimura, Li Yan, Naomichi Matsumoto, Ann Nordgren, Noriko Miyake, G. Grigelioniene, and S. Ikegawa. Novel kiaa0753 mutations extend the phenotype of skeletal ciliopathies. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-15442-1, doi:10.1038/s41598-017-15442-1. This article has 41 citations and is from a peer-reviewed journal.

18. (stephen2017mutationsinkiaa0753 pages 3-5): Joshi Stephen, Thierry Vilboux, Luhe Mian, Chulaluck Kuptanon, Courtney M. Sinclair, Deniz Yildirimli, Dawn M. Maynard, Joy Bryant, Roxanne Fischer, Meghana Vemulapalli, James C. Mullikin, Marjan Huizing, William A. Gahl, May Christine V. Malicdan, and Meral Gunay-Aygun. Mutations in kiaa0753 cause joubert syndrome associated with growth hormone deficiency. Human Genetics, 136:399-408, Feb 2017. URL: https://doi.org/10.1007/s00439-017-1765-z, doi:10.1007/s00439-017-1765-z. This article has 50 citations and is from a peer-reviewed journal.

19. (inskeep2022geneticandphenotypic pages 10-11): Katherine A. Inskeep, Yuri A. Zarate, Danielle Monteil, Jurgen Spranger, Dan Doherty, Rolf W. Stottmann, and K. Nicole Weaver. Genetic and phenotypic heterogeneity in kiaa0753‐related ciliopathies. American Journal of Medical Genetics Part A, 188:104-115, Sep 2022. URL: https://doi.org/10.1002/ajmg.a.62497, doi:10.1002/ajmg.a.62497. This article has 8 citations.

20. (hammarsjo2017novelkiaa0753mutations pages 4-5): A. Hammarsjö, Zheng Wang, Raquel Vaz, F. Taylan, M. Sedghi, K. Girisha, D. Chitayat, K. Neethukrishna, Patrick Shannon, Ruth Godoy, K. Gowrishankar, A. Lindstrand, Jafar Nasiri, M. Baktashian, Phillip T Newton, L. Guo, Wolfgang Hofmeister, M. Pettersson, A. Chagin, Gen Nishimura, Li Yan, Naomichi Matsumoto, Ann Nordgren, Noriko Miyake, G. Grigelioniene, and S. Ikegawa. Novel kiaa0753 mutations extend the phenotype of skeletal ciliopathies. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-15442-1, doi:10.1038/s41598-017-15442-1. This article has 41 citations and is from a peer-reviewed journal.

21. (stephen2017mutationsinkiaa0753 pages 6-8): Joshi Stephen, Thierry Vilboux, Luhe Mian, Chulaluck Kuptanon, Courtney M. Sinclair, Deniz Yildirimli, Dawn M. Maynard, Joy Bryant, Roxanne Fischer, Meghana Vemulapalli, James C. Mullikin, Marjan Huizing, William A. Gahl, May Christine V. Malicdan, and Meral Gunay-Aygun. Mutations in kiaa0753 cause joubert syndrome associated with growth hormone deficiency. Human Genetics, 136:399-408, Feb 2017. URL: https://doi.org/10.1007/s00439-017-1765-z, doi:10.1007/s00439-017-1765-z. This article has 50 citations and is from a peer-reviewed journal.

22. (hammarsjo2017novelkiaa0753mutations pages 9-10): A. Hammarsjö, Zheng Wang, Raquel Vaz, F. Taylan, M. Sedghi, K. Girisha, D. Chitayat, K. Neethukrishna, Patrick Shannon, Ruth Godoy, K. Gowrishankar, A. Lindstrand, Jafar Nasiri, M. Baktashian, Phillip T Newton, L. Guo, Wolfgang Hofmeister, M. Pettersson, A. Chagin, Gen Nishimura, Li Yan, Naomichi Matsumoto, Ann Nordgren, Noriko Miyake, G. Grigelioniene, and S. Ikegawa. Novel kiaa0753 mutations extend the phenotype of skeletal ciliopathies. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-15442-1, doi:10.1038/s41598-017-15442-1. This article has 41 citations and is from a peer-reviewed journal.

23. (chang2021cep120mediatedkiaa0753recruitment pages 10-12): Chia-Hsiang Chang, Ting-Yu Chen, I-Ling Lu, Rong-Bin Li, Jhih-Jie Tsai, Pin-Yeh Lin, and Tang K. Tang. Cep120-mediated kiaa0753 recruitment onto centrioles is required for timely neuronal differentiation and germinal zone exit in the developing cerebellum. Genes & Development, 35:1445-1460, Oct 2021. URL: https://doi.org/10.1101/gad.348636.121, doi:10.1101/gad.348636.121. This article has 9 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Short-rib_Thoracic_Dysplasia_21_Without_Polydactyly-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030356` (3 mentions) - the report calls it "if available"; MONDO calls it **short-rib thoracic dysplasia 21 without polydactyly**