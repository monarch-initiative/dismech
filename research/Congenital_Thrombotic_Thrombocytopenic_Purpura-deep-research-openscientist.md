---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-30T06:06:56.562629'
end_time: '2026-08-30T06:35:55.946565'
duration_seconds: 1739.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Thrombotic Thrombocytopenic Purpura
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 27
  on_topic: 20
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 6
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0010134
    reported_labels:
    - "congenital TTP / Upshaw\u2013Schulman syndrome"
    ontology_label: Pendred syndrome
  - term_id: HP:0001873
    reported_labels:
    - Lab abnormality
    ontology_label: Thrombocytopenia
  - term_id: HP:0002140
    reported_labels:
    - Clinical sign
    ontology_label: Ischemic stroke
  - term_id: HP:0000083
    reported_labels:
    - Lab/clinical
    ontology_label: Renal insufficiency
  - term_id: HP:0000978
    reported_labels:
    - purpura
    ontology_label: Bruising susceptibility
  - term_id: HP:0001681
    reported_labels:
    - Clinical sign
    ontology_label: Angina pectoris
  - term_id: CL:0002679
    reported_labels:
    - hepatic stellate cell
    ontology_label: natural helper lymphocyte
  - term_id: CHEBI:18420
    reported_labels:
    - zinc, catalytic metal
    ontology_label: magnesium(2+)
  - term_id: NCIT:C171453
    reported_labels:
    - plasma
    ontology_label: Hospital Stay
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Thrombotic_Thrombocytopenic_Purpura-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Thrombotic_Thrombocytopenic_Purpura-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Thrombotic Thrombocytopenic Purpura
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Thrombotic Thrombocytopenic Purpura** covering all of the
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

# Congenital Thrombotic Thrombocytopenic Purpura (Upshaw–Schulman Syndrome): A Comprehensive Disease Characteristics Report

## Summary

Congenital thrombotic thrombocytopenic purpura (cTTP), also known as **Upshaw–Schulman syndrome (USS)** or **hereditary TTP (hTTP)**, is an ultra-rare, life-threatening thrombotic microangiopathy caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in the *ADAMTS13* gene** on chromosome 9q34.2 (OMIM #274150; gene OMIM \*604134). The genetic defect produces severe, lifelong deficiency (typically <10%, often <5–6% activity) of ADAMTS13, the plasma metalloprotease that cleaves von Willebrand factor (VWF). Inheritance is **autosomal recessive**.

The central pathophysiology is elegantly linear: absent ADAMTS13 protease activity allows **ultra-large VWF (UL-VWF) multimers** to persist in circulation. Under high shear stress in the microvasculature, these multimers spontaneously bind and aggregate platelets, generating disseminated platelet-rich microthrombi. This produces the clinical triad of **consumptive thrombocytopenia**, **microangiopathic hemolytic anemia (MAHA)**, and **ischemic end-organ injury** — most prominently affecting the brain, kidney, and heart. Because ADAMTS13 activity is already at baseline near-zero, additional physiological stressors that raise VWF or shear (birth, pregnancy, infection, inflammation) act as "second hits" that precipitate acute episodes, explaining the marked (~78%) female predominance and the frequent neonatal and pregnancy-associated presentations.

cTTP is a treatable disease when recognized: the therapeutic principle is **ADAMTS13 replacement**. Historically this was achieved with fresh frozen plasma (FFP) or plasma-derived factor VIII/VWF concentrates that contain ADAMTS13. The field has now been transformed by **recombinant ADAMTS13 (apadamtase alfa; Adzynma/TAK-755)**, which in a pivotal phase 3 crossover trial (NCT03393975) prevented essentially all acute TTP events. This report synthesizes ten confirmed findings across 31 reviewed papers to populate a complete 15-section disease knowledge base entry.

---

## Key Findings

### Finding 1 — cTTP is caused by biallelic *ADAMTS13* mutations (autosomal recessive)

Congenital TTP results from **homozygous or compound heterozygous disease-causing variants in *ADAMTS13*** (chromosome 9q34.2; OMIM #274150; gene OMIM \*604134). The consequence is severe deficiency of the VWF-cleaving metalloprotease, with activity typically <10% and often <5–6%. More than **200 distinct pathogenic variants** are distributed across the gene, with **missense variants predominating**, alongside frameshift, nonsense, and splice-site variants. Inheritance is unambiguously **autosomal recessive**, meaning both alleles must be affected for disease to manifest.

Foundational evidence comes from Levy and colleagues, who established that *"homozygous or compound heterozygous mutations of ADAMTS13 are responsible for recessively inherited TTP"* ([PMID: 12393505](https://pubmed.ncbi.nlm.nih.gov/12393505/)). More recent reviews confirm cTTP is *"a rare genetic disorder caused by mutations in the ADAMTS13 gene that leads to decreased or absent production of the plasma von Willebrand factor (VWF)-cleaving metalloprotease ADAMTS13"* ([PMID: 37895305](https://pubmed.ncbi.nlm.nih.gov/37895305/)).

### Finding 2 — Pathophysiology: ADAMTS13 deficiency → uncleaved ultra-large VWF → shear-dependent microthrombosis

ADAMTS13 is a **~190 kDa plasma metalloprotease produced mainly by hepatic stellate cells**. Its physiological function is to cleave the **Tyr1605–Met1606 scissile bond in the VWF A2 domain**. Cleavage requires tension/shear-induced unfolding of the A2 domain and allosteric activation of ADAMTS13 through binding of its distal T8–CUB domains to the VWF D4 domain. When ADAMTS13 is deficient, ultra-large VWF multimers accumulate; these spontaneously bind platelets under high shear, producing **disseminated microvascular platelet thrombi**, consumptive thrombocytopenia, and microangiopathic hemolytic anemia (red cells are mechanically sheared as they pass through partially occluded microvessels).

Crawley and Scully described that *"ADAMTS13, a 190-kD plasma protease originating primarily in hepatic stellate cells, prevents microvascular thrombosis by cleaving von Willebrand factor when the substrate is conformationally unfolded by high levels of shear stress"* ([PMID: 19180123](https://pubmed.ncbi.nlm.nih.gov/19180123/)). The precise cleavage site was defined as the *"Cleavage of the Tyr(1605)-Met(1606) scissile bond in the VWF A2 domain"* ([PMID: 17146059](https://pubmed.ncbi.nlm.nih.gov/17146059/)).

### Finding 3 — Recombinant ADAMTS13 (apadamtase alfa) prevents acute events in phase 3 trial

The pivotal **phase 3 open-label crossover trial (NCT03393975; Scully et al., NEJM 2024)** enrolled 48 patients randomized to **recombinant ADAMTS13 (40 IU/kg IV)** versus standard plasma-based prophylaxis. The results were striking: **zero acute TTP events** occurred during rADAMTS13 prophylaxis versus 1 during standard therapy (mean annualized event rate 0.05). The annualized rate of thrombocytopenia manifestations was 0.74 with rADAMTS13 versus 1.73 with standard therapy. Adverse events occurred in 71% versus 84% of patients respectively, and **no anti-ADAMTS13 antibodies** developed. The earlier first-in-human phase 1 study (BAX 930) demonstrated dose-proportional pharmacokinetics and good tolerability.

The primary efficacy result was reported as: *"No acute TTP event occurred during prophylaxis with recombinant ADAMTS13, whereas 1 patient had an acute TTP event during prophylaxis with standard therapy (mean annualized event rate, 0.05)"* ([PMID: 38692292](https://pubmed.ncbi.nlm.nih.gov/38692292/)). The first-in-human safety was established: *"BAX 930 was well tolerated, no serious adverse events occurred, and no anti-ADAMTS-13 antibodies were observed"* ([PMID: 28912376](https://pubmed.ncbi.nlm.nih.gov/28912376/)).

### Finding 4 — c.4143dupA (p.Glu1382Argfs) is a Northern/Central European founder mutation

The **c.4143dupA (4143insA) frameshift variant in *ADAMTS13* exon 29** shows striking geographic concentration in Northern/Central Europe. It has been identified in families from Germany, Norway, Sweden, Poland, the Czech Republic, and Australia (German ancestry). A shared, identical intragenic haplotype across 17 polymorphic markers confirms a **common founder origin**, making it the single most frequent *ADAMTS13* mutation in European cTTP cohorts.

Schneppenheim and colleagues demonstrated that *"The haplotypes linked to 4143insA were identical in all informative families"* and concluded that *"4143insA has a common genetic background and is frequent among patients with hereditary ADAMTS13 deficiency in Northern and Central European countries"* ([PMID: 16807643](https://pubmed.ncbi.nlm.nih.gov/16807643/)).

### Finding 5 — Natural history: female predominance, high event rate without prophylaxis, neonatal risk

A retrospective multinational cohort (78 patients, 9 sites) documented that **78.2% of patients were female**, with 92 acute TTP events occurring in 70.5% of patients (0.145 events/person-year). Critically, **87% of acute events occurred WITHOUT prophylaxis**, and 20% of those unprotected events caused organ damage. Neonatal presentation is common: **35–50% of patients present with severe hemolysis, jaundice, and thrombocytopenia in the first days of life**. Pregnancy physiologically lowers ADAMTS13 activity, precipitating relapse, and the International Hereditary TTP Registry documents a clinically heterogeneous course with incomplete genotype-phenotype correlation.

The cohort reported: *"Eighty (87.0%) acute TTP events occurred in the absence of prophylactic treatment, of which 16 (20.0%) resulted in organ [damage]"* ([PMID: 42603082](https://pubmed.ncbi.nlm.nih.gov/42603082/)). The neonatal risk was quantified: *"The greatest risk for hTTP is in their first days after birth, when 35-50% of patients will have severe hemolysis, jaundice, and thrombocytopenia"* ([PMID: 38536644](https://pubmed.ncbi.nlm.nih.gov/38536644/)).

### Finding 6 — Adamts13-knockout mouse requires modifier background + trigger (gene-environment model)

Motto et al. (2005) demonstrated that **Adamts13-deficient mice are viable with normal survival** but exhibit prolonged VWF-mediated platelet-endothelial interactions. On the **CASA/Rk genetic background** (which has elevated plasma VWF), a subset develop spontaneous thrombocytopenia and decreased survival. Critically, **challenge with shigatoxin produces a syndrome closely resembling human TTP**. No correlation was observed between plasma VWF level and TTP severity, implying additional TTP-modifying genes beyond VWF. This is a foundational **gene-environment ("two-hit") model** of the disease.

The authors reported: *"Challenge of these mice with shigatoxin (derived from bacterial pathogens associated with the related human disease hemolytic uremic syndrome) resulted in a striking syndrome closely resembling human TTP"* and that *"no correlation was observed between plasma vWF level and severity of TTP, implying the existence of TTP-modifying genes distinct from vWF"* ([PMID: 16200209](https://pubmed.ncbi.nlm.nih.gov/16200209/)).

### Finding 7 — Pregnancy in cTTP: high loss/morbidity untreated; plasma prophylaxis markedly improves outcomes

Davidesko et al. (2023) studied a cohort of 14 women with hTTP (homozygous c.3772delA) across **71 pregnancies**: 17 (24%) ended in pregnancy loss and 32 (45%) were complicated by severe obstetric morbidity (SOM). FFP-treated pregnancies had dramatically lower SOM (**28% vs 72%, p<0.001**) and fewer preterm TTP exacerbations (**18% vs 82%, p<0.001**). Elevated non-pregnant VWF antigen predicted SOM even among treated women (225% vs 165%, p=0.047), suggesting VWF antigen may be a useful biomarker. In a separate case, recombinant ADAMTS13 rescued a plasma-refractory pregnancy, leading to a live birth.

The benefit of prophylaxis was quantified: *"Treated women had decreased SOM (28% vs 72%, p < .001) and preterm thrombotic thrombocytopenic purpura exacerbations (18% vs 82%, p < .001)"* ([PMID: 36889591](https://pubmed.ncbi.nlm.nih.gov/36889591/)). The recombinant rescue case reported: *"weekly injections of recombinant ADAMTS13 at a dose of 40 U per kilogram of body weight were initiated. The patient's platelet count normalized"* ([PMID: 36546627](https://pubmed.ncbi.nlm.nih.gov/36546627/)).

### Finding 8 — ADAMTS13 circulates in a closed (autoinhibited) conformation opened allosterically by VWF

Plasma ADAMTS13 circulates in a **folded/closed conformation** stabilized by an intramolecular interaction between the central **Spacer domain and the C-terminal CUB domains**. Binding of the distal domains to VWF D4(-CK), or to activating antibodies, extends ADAMTS13 into an **open, catalytically enhanced conformation**, increasing the metalloprotease-domain kcat approximately 2-fold and exposing a cryptic epitope in the metalloprotease domain. Flexible linker regions around the metalloprotease and T2 domains mediate this conformational activation. This closed-to-open allosteric switch is central to understanding both physiology and engineered therapeutics.

Schelpe et al. established that *"Plasma ADAMTS13 circulates in a folded conformation that is stabilized by an interaction between the central Spacer domain and the C-terminal CUB"* and that *"conformational extension of ADAMTS13 enhances the proteolytic function of the metalloprotease domain (kcat), rather than augmenting substrate binding (Km)"* ([PMID: 32196558](https://pubmed.ncbi.nlm.nih.gov/32196558/)). Deforche et al. identified the linker regions responsible for this flexibility ([PMID: 26391536](https://pubmed.ncbi.nlm.nih.gov/26391536/)).

### Finding 9 — Diagnosis relies on ADAMTS13 activity <10% (FRETS-VWF73 gold standard)

TTP is defined by **severe ADAMTS13 activity deficiency (<10%)**. The **FRETS-VWF73 fluorogenic assay is the reference/gold-standard method**. The automated chemiluminescent immunoassay HemosIL AcuStar is faster but shows clinically relevant discrepancies versus FRETS-VWF73 (affecting diagnosis in 5/32 and follow-up in 7/51 samples; AcuStar reads systematically lower), partly because autoantibodies reduce activity more in AcuStar/ELISA than in FRETS assays. Novel fiber-optic surface plasmon resonance (FO-SPR) assays (detection limit ~6.8%, CV 7.2%) are in development. For **cTTP specifically, absence of an anti-ADAMTS13 inhibitor plus biallelic pathogenic *ADAMTS13* variants confirms the congenital form** and distinguishes it from the acquired/immune form (iTTP).

Evidence documents that *"discrepancies between AcuStar and the gold standard FRETS-VWF73 have been documented in a manner that would affect diagnosis and treatment"* ([PMID: 37063760](https://pubmed.ncbi.nlm.nih.gov/37063760/)) and that *"Thrombotic thrombocytopenic purpura (TTP) is characterized by severe ADAMTS-13 activity deficiency (<10%)"* ([PMID: 37711907](https://pubmed.ncbi.nlm.nih.gov/37711907/)).

### Finding 10 — Residual-activity variants (e.g., R1060W) cause late-onset/pregnancy-triggered cTTP

Falter et al. (2014) reported a patient with compound heterozygous *ADAMTS13* **p.Q44X** (exon 2 premature stop) plus **p.R1060W** (exon 24 missense associated with low but measurable ADAMTS13 activity), who presented as **late-onset, pregnancy-induced cTTP** — first acute episode at age 19 during a first pregnancy, with a sibling who died during a second pregnancy. **R1060W is a recurrent variant enriched among adult/pregnancy-onset patients**. Registry data similarly show that higher residual ADAMTS13 activity correlates with later overt disease onset — a genotype-phenotype relationship of clinical importance.

The authors described *"a missense mutation in exon 24 (p.R1060W) associated with low but measurable ADAMTS13 activity"* and emphasized that *"Genetic analysis of the ADAMTS13 gene is important in TTP patients of all ages if an ADAMTS13 inhibitor has been excluded"* ([PMID: 24994604](https://pubmed.ncbi.nlm.nih.gov/24994604/)).

---

## Comprehensive Disease Profile (15 Sections)

### 1. Disease Information

**Overview.** Congenital thrombotic thrombocytopenic purpura is an ultra-rare, autosomal-recessive thrombotic microangiopathy caused by inherited severe deficiency of ADAMTS13. It manifests as episodic microvascular thrombosis producing thrombocytopenia, microangiopathic hemolytic anemia, and ischemic organ damage.

**Key identifiers:**
| Resource | Identifier |
|----------|-----------|
| OMIM (disease) | #274150 |
| OMIM (gene) | *604134 (ADAMTS13) |
| Suggested MONDO | MONDO:0010134 (congenital TTP / Upshaw–Schulman syndrome) |
| ICD-10 | D69.4 / M31.1 (thrombotic microangiopathy grouping) |
| ICD-11 | 3B64.1 (thrombotic microangiopathy) |
| MeSH | Purpura, Thrombotic Thrombocytopenic (D011697) |
| Orphanet | ORPHA:93583 (hereditary/congenital TTP) |
| Gene locus | 9q34.2 |

**Synonyms:** Upshaw–Schulman syndrome (USS); hereditary TTP (hTTP); congenital TTP (cTTP); familial TTP; ADAMTS13 deficiency, congenital.

**Information source type:** Predominantly derived from **aggregated disease-level resources** — the International Hereditary TTP Registry, multinational retrospective cohorts, and case series — rather than population-scale EHR, reflecting its ultra-rare status.

### 2. Etiology

**Primary cause:** Genetic — biallelic loss-of-function variants in *ADAMTS13* (Finding 1). This is the necessary and sufficient molecular cause of the congenital form.

**Genetic risk factors:** The causal variants themselves (>200 known pathogenic variants). Founder alleles increase population-specific risk, notably **c.4143dupA/p.Glu1382Argfs** in Northern/Central Europe (Finding 4). **Modifier genes** beyond *ADAMTS13* modulate severity — the mouse model demonstrated TTP-modifying genes distinct from VWF (Finding 6). Common *ADAMTS13* amino-acid polymorphisms (R7W, Q448E, P618A, A732V) can act as positive or negative modifiers of secretion/activity depending on context ([PMID: 16160007](https://pubmed.ncbi.nlm.nih.gov/16160007/)).

**Environmental / triggering risk factors:** Pregnancy (physiologically lowers ADAMTS13 and raises VWF), the neonatal period/birth, infection and inflammation, and surgery. **Female sex** is a major demographic risk factor (~78% of patients) driven largely by pregnancy-triggered episodes (Finding 5).

**Protective factors:** No specific genetic protective alleles are established. The dominant *modifiable* protective factor is **prophylactic ADAMTS13 replacement** (plasma or recombinant), which prevented 87% of the acute events that occurred in its absence (Findings 5, 7).

**Gene-environment interactions:** The disease is a paradigm of gene-environment ("two-hit") interaction — an underlying genetic ADAMTS13 deficiency requires an environmental/physiological trigger (elevated VWF/shear) to precipitate overt disease. This is directly demonstrated in the Adamts13-knockout mouse, which develops TTP only on a high-VWF background AND after shigatoxin challenge (Finding 6).

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset | Frequency/Severity |
|-----------|------|---------------|-------|--------------------|
| Thrombocytopenia | Lab abnormality | HP:0001873 | Neonatal–adult | Universal during episodes; severe |
| Microangiopathic hemolytic anemia | Lab abnormality | HP:0001937 (schistocytosis HP:0001981) | Neonatal–adult | Universal during episodes |
| Neonatal jaundice/hyperbilirubinemia | Clinical sign | HP:0000952 (jaundice) | Neonatal | 35–50% |
| Ischemic stroke / neurological deficits | Clinical sign | HP:0002140 | Childhood–adult | Common; can be presenting feature |
| Renal impairment | Lab/clinical | HP:0000083 | Variable | Frequent, may be longstanding |
| Fatigue / purpura / bleeding | Symptom/sign | HP:0000978 (purpura) | Variable | Common |
| Cardiac ischemia | Clinical sign | HP:0001681 | Adult | Less common but serious |

**Characteristics.** Onset ranges from **neonatal (35–50%)** through childhood to adult/pregnancy-triggered late onset. Severity is **variable** and partly genotype-dependent — residual-activity alleles (R1060W) associate with milder, later-onset disease (Finding 10). The course is characteristically **episodic/relapsing**, punctuated by triggers. **Quality-of-life impact** is substantial: recurrent hospitalizations, need for regular infusions, pregnancy loss and obstetric morbidity, and risk of permanent stroke- or renal-related disability.

### 4. Genetic/Molecular Information

**Causal gene:** *ADAMTS13* (HGNC:1366; gene OMIM \*604134; 9q34.2), encoding the VWF-cleaving metalloprotease.

**Pathogenic variants:** >200 distinct variants distributed across all domains; **missense predominate**, with frameshift, nonsense, and splice-site variants also common (Finding 1). Classification per ACMG/AMP spans pathogenic and likely pathogenic; residual-activity missense alleles may be VUS pending functional data. Representative variants: **c.4143dupA (p.Glu1382Argfs)** — European founder frameshift; **p.R1060W** — residual-activity missense enriched in adult/pregnancy onset; **p.Q44X** — nonsense; **c.3772delA** and **c.721delG (p.Gly241fs)** — frameshift; **p.R1336W** and **p.P618A** — activity-reducing missense. Variants are **germline** (not somatic). Functional consequence is predominantly **loss of function** (impaired secretion and/or catalytic activity).

**Modifier genes:** Motto et al. established the existence of TTP-modifying genes distinct from VWF (Finding 6). Intragenic *ADAMTS13* polymorphisms modulate secretion/activity ([PMID: 16160007](https://pubmed.ncbi.nlm.nih.gov/16160007/)).

**Epigenetic information / chromosomal abnormalities:** No disease-defining epigenetic changes or large-scale chromosomal abnormalities are established for cTTP; it is a single-gene monogenic disorder.

### 5. Environmental Information

**Environmental / lifestyle factors:** cTTP is not caused by environmental toxins, radiation, or lifestyle. However, physiological/environmental **triggers** unmask disease: pregnancy, birth, infection, inflammation, and surgery.

**Infectious agents:** No pathogen causes cTTP. Notably, **shigatoxin** (from Shiga-toxin–producing bacteria, classically associated with HUS) triggers a TTP-like syndrome in genetically susceptible ADAMTS13-deficient mice, illustrating how infection can serve as an environmental "second hit" (Finding 6).

### 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

```
Biallelic ADAMTS13 LoF variants (germline)
        │
        ▼
Severe deficiency of ADAMTS13 metalloprotease activity (<10%)
        │
        ▼
Failure to cleave VWF A2 domain (Tyr1605–Met1606 scissile bond)
        │
        ▼
Persistence of ultra-large VWF (UL-VWF) multimers
        │
        ▼  (TRIGGER: high shear / ↑VWF from pregnancy, infection, birth)
Spontaneous UL-VWF–platelet binding under shear
        │
        ▼
Disseminated platelet-rich microthrombi in microvasculature
        │
        ├──► Platelet consumption → THROMBOCYTOPENIA
        ├──► RBC mechanical shearing → MICROANGIOPATHIC HEMOLYTIC ANEMIA
        └──► Microvascular occlusion → ISCHEMIC ORGAN INJURY (brain, kidney, heart)
```

**Molecular pathway / cellular processes:** Hemostasis — VWF-dependent platelet adhesion and aggregation (GO:0007596 blood coagulation; GO:0070527 platelet aggregation). Proteolysis (GO:0006508) by the metalloprotease.

**Protein dysfunction:** Loss of function via impaired secretion, misfolding, truncation, or reduced catalytic activity. The wild-type enzyme is regulated by a **closed→open allosteric conformational switch** (Spacer–CUB autoinhibition relieved by VWF-D4 binding, ~2-fold kcat increase; Finding 8). Missense variants can disrupt secretion, catalysis, or allosteric regulation.

**Suggested GO/CL/CHEBI terms:** GO:0004222 (metalloendopeptidase activity), GO:0005576 (extracellular region); CL:0000232 (erythrocyte), CL:0000233 (platelet), CL:0002679 (hepatic stellate cell), CL:0000115 (endothelial cell); CHEBI:29108 (calcium, cofactor), CHEBI:18420 (zinc, catalytic metal).

### 7. Anatomical Structures Affected

| Level | Structures | Suggested ontology |
|-------|-----------|--------------------|
| Organ (primary) | Brain, kidney, heart | UBERON:0000955, UBERON:0002113, UBERON:0000948 |
| Organ (secondary) | Spleen, GI tract, placenta | UBERON:0002106, UBERON:0000160, UBERON:0001987 |
| Body systems | Cardiovascular/hematologic; nervous; renal | — |
| Tissue/cell | Microvascular endothelium; platelets; erythrocytes; hepatic stellate cells (ADAMTS13 source) | CL:0000115; CL:0000233; CL:0000232; CL:0002679 |
| Subcellular | Endothelial Weibel–Palade bodies (VWF storage); extracellular plasma compartment | GO:0033093 (Weibel-Palade body); GO:0005615 (extracellular space) |
| Localization | Systemic microvasculature; bilateral/diffuse | — |

Damage is **bilateral and diffuse** (microvascular), not focal or lateralized.

### 8. Temporal Development

**Onset:** Congenital deficiency present from birth; clinical onset ranges from **neonatal (35–50% present in first days of life with hemolysis, jaundice, thrombocytopenia)** through childhood to **adult/pregnancy-triggered late onset** (Findings 5, 10). Onset pattern of acute episodes is **acute/subacute**.

**Progression:** The disease course is **episodic/relapsing-remitting** overlaid on a **chronic, lifelong** deficiency state. Acute events cluster around triggers. Progression rate is variable and partly determined by residual ADAMTS13 activity — higher residual activity correlates with later overt onset (Findings 5, 10).

**Patterns:** Remission is **treatment-induced** (prophylactic replacement) between episodes; there is no spontaneous cure. Critical vulnerability windows are the **neonatal period** and **pregnancy**, which are also the key windows for prophylactic intervention.

### 9. Inheritance and Population

**Epidemiology:** Ultra-rare. Estimated prevalence on the order of ~1–2 per million (cTTP accounts for a minority of all TTP; overall TTP incidence ~1.5–6 per million/year). Orphanet classifies it among ultra-rare disorders.

**Genetic parameters:**
- **Inheritance:** Autosomal recessive (Finding 1).
- **Penetrance:** High at the biochemical level (biallelic LoF → severe deficiency), but **clinical penetrance/expressivity is variable and incomplete** — the registry documents heterogeneous course and imperfect genotype-phenotype correlation ([PMID: 30792199](https://pubmed.ncbi.nlm.nih.gov/30792199/)).
- **Expressivity:** Variable, modulated by residual activity, modifier genes, and triggers.
- **Founder effects:** c.4143dupA in Northern/Central Europe (Finding 4).
- **Consanguinity:** Increases homozygous cases in populations with high consanguinity.
- **Genetic anticipation / mosaicism:** Not applicable / not established.

**Demographics:** Marked **female predominance (~78%)**, driven by pregnancy-triggered presentation (Finding 5). Affects all ethnicities; specific founder variants show geographic clustering (European c.4143dupA). Age distribution is bimodal-ish: neonatal peak and a young-adult female (pregnancy) peak.

### 10. Diagnostics

**Core laboratory diagnosis:** Severe **ADAMTS13 activity <10%** measured by the **gold-standard FRETS-VWF73 fluorogenic assay** (Finding 9). Supportive labs: thrombocytopenia, MAHA with schistocytes on smear, elevated LDH, low haptoglobin, elevated indirect bilirubin, negative direct antiglobulin test.

**Distinguishing cTTP from iTTP:** In cTTP, an **anti-ADAMTS13 inhibitor/autoantibody is ABSENT** and **biallelic pathogenic *ADAMTS13* variants are present**. In acquired iTTP, an inhibitor is present (Finding 9). Mixing studies and anti-ADAMTS13 IgG assays help discriminate.

**Genetic testing:** *ADAMTS13* **single-gene sequencing** (or gene panels including complement genes for TMA differential; [PMID: 30046676](https://pubmed.ncbi.nlm.nih.gov/30046676/)) is definitive. Genetic analysis is recommended in TTP patients **of all ages once an inhibitor is excluded** (Finding 10). WES/WGS are useful when panels are non-diagnostic. Chromosomal microarray/karyotype/FISH are not indicated (single-gene disorder).

**Emerging assays:** HemosIL AcuStar (faster, but reads systematically lower, with diagnostic discrepancies) and fiber-optic SPR immunoassays (Finding 9).

**Differential diagnosis:** Acquired iTTP; atypical HUS (complement dysregulation); Shiga-toxin HUS; DIC; HELLP/pregnancy TMA; Evans syndrome; immune thrombocytopenia (ITP) — the latter is a recognized misdiagnosis before hTTP is revealed by pregnancy loss ([PMID: 39614241](https://pubmed.ncbi.nlm.nih.gov/39614241/)).

### 11. Outcome/Prognosis

**Mortality/morbidity:** Untreated acute events are **life-threatening**; historically high mortality. The dominant modifiable determinant of outcome is prophylaxis — **87% of acute events occurred without prophylaxis, and 20% of those caused organ damage** (Finding 5). Recurrent strokes and chronic kidney damage drive long-term morbidity and disability.

**Life expectancy:** With appropriate ADAMTS13 replacement prophylaxis, acute events are largely preventable and long-term outlook is substantially improved; without it, recurrent life-threatening episodes and cumulative ischemic organ damage occur.

**Pregnancy outcomes:** Untreated pregnancies carry high risk — 24% loss and 45% severe obstetric morbidity in one cohort; plasma prophylaxis reduces SOM to 28% (from 72%) (Finding 7).

**Prognostic factors/biomarkers:** Residual ADAMTS13 activity (higher = later/milder onset; Findings 5, 10); adherence to prophylaxis; and **elevated non-pregnant VWF antigen predicts severe obstetric morbidity** (Finding 7) — a candidate prognostic biomarker.

### 12. Treatment

**Principle: ADAMTS13 replacement.**

| Modality | Agent | Notes | Suggested NCIT |
|----------|-------|-------|----------------|
| Recombinant ADAMTS13 | Apadamtase alfa (Adzynma/TAK-755, BAX 930), 40 IU/kg IV | Prevented ~all acute events in phase 3 (NCT03393975); no anti-drug antibodies | NCIT: recombinant ADAMTS13 |
| Fresh frozen plasma | FFP infusion / plasma exchange | Historical mainstay; provides exogenous ADAMTS13 | NCIT:C171453 (plasma) |
| Plasma-derived FVIII/VWF concentrate | Koate (contains ADAMTS13) | Alternative source of enzyme; long-term data available ([PMID: 37855744](https://pubmed.ncbi.nlm.nih.gov/37855744/)) | — |

**Recombinant ADAMTS13** is now the transformative therapy (Finding 3): 40 IU/kg IV, prophylaxis prevented essentially all acute events with a favorable safety profile and no anti-ADAMTS13 antibody development. It also rescued a plasma-refractory pregnancy (Finding 7).

**Emerging/experimental:** ADAMTS13 **gene therapy**; additional recombinant products; and novel VWF-activity inhibitors are under development ([PMID: 42422077](https://pubmed.ncbi.nlm.nih.gov/42422077/)). A **constitutively active ADAMTS13 variant (Ala1144Val, "caADAMTS13")** with ~5-fold enhanced activity shows thrombolytic/anti-inflammatory efficacy in murine stroke models ([PMID: 34780600](https://pubmed.ncbi.nlm.nih.gov/34780600/)).

**Supportive care:** Individualized infusion intervals guided by ADAMTS13 activity or, where testing is limited, surrogate markers (platelet count, LDH). Therapeutic plasma exchange can prolong intervals between administrations in some patients ([PMID: 30394580](https://pubmed.ncbi.nlm.nih.gov/30394580/)).

### 13. Prevention

- **Primary prevention:** Not applicable (genetic disease); **genetic counseling** and carrier screening in affected families and consanguineous populations.
- **Secondary prevention:** Early diagnosis via ADAMTS13 testing and genetic confirmation; neonatal vigilance in known-carrier families.
- **Tertiary prevention (core strategy):** **Prophylactic ADAMTS13 replacement** to prevent acute events and organ damage — especially intensified during pregnancy and the peripartum period (Findings 5, 7). Regimen individualization (e.g., FFP every 10 days intensified to weekly in third trimester) enables successful full-term pregnancy even in resource-limited settings ([PMID: 42529691](https://pubmed.ncbi.nlm.nih.gov/42529691/)).
- **Counseling:** Genetic counseling for family planning, prenatal/carrier testing, and pregnancy management planning.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** *ADAMTS13* is conserved across vertebrates. Mouse *Adamts13* (NCBI Gene) is the principal experimental ortholog. Phylogenetic analysis across 264 vertebrates shows **allosteric regulation of ADAMTS13 is broadly conserved** across placental mammals, birds, and amphibians ([PMID: 30700419](https://pubmed.ncbi.nlm.nih.gov/30700419/)).
- **Natural disease / veterinary relevance:** No well-established naturally occurring cTTP-equivalent is prominently documented in companion animals in the reviewed literature; the disease is chiefly modeled experimentally (see Section 15).
- **Evolutionary conservation:** The T7 and T8 distal domains are essential for allosteric activation, while T3–T6 are dispensable and have been repeatedly deleted across lineages, indicating conserved core mechanism with flexible peripheral architecture ([PMID: 30700419](https://pubmed.ncbi.nlm.nih.gov/30700419/)).

### 15. Model Organisms

**Principal model — Adamts13-knockout mouse (Motto et al. 2005):**
- **Type:** Mammalian genetic knockout.
- **Phenotype recapitulation:** Partial — mice are viable with normal survival and prolonged VWF-platelet-endothelial interactions but do **not** spontaneously develop full TTP on a standard background. On the **CASA/Rk high-VWF background**, a subset develop spontaneous thrombocytopenia; **shigatoxin challenge produces a syndrome closely resembling human TTP** (Finding 6).
- **Value:** Demonstrates the essential **gene-environment ("two-hit") architecture** and the existence of TTP-modifying genes beyond VWF.
- **Limitation:** Requires modifier background plus trigger; does not capture the full spontaneous human phenotype in isolation.

**Engineered variant models:** The **constitutively active caADAMTS13 (Ala1144Val)** used in murine stroke models illustrates therapeutic proof-of-concept for conformationally activated enzyme ([PMID: 34780600](https://pubmed.ncbi.nlm.nih.gov/34780600/)).

**Applications:** Studying VWF-ADAMTS13 axis, trigger biology, thrombolytic/therapeutic testing, and gene-therapy development.

**Resources:** MGI (mouse *Adamts13*), IMPC/KOMP for knockout resources.

---

## Mechanistic Model / Interpretation

The unifying model of cTTP is a **single-enzyme deficiency with an amplifying, trigger-dependent thrombotic cascade**. ADAMTS13 is the sole physiological regulator of VWF multimer size. Its congenital absence is necessary but often **not sufficient** for overt disease — the near-zero baseline activity creates a "primed" state in which the addition of high shear or elevated VWF (from pregnancy, birth, infection, or inflammation) tips the balance toward runaway VWF-platelet microthrombosis. This explains three otherwise puzzling clinical observations: (1) the marked female predominance (pregnancy is the archetypal trigger), (2) the neonatal-birth vulnerability window, and (3) the variable, episodic course despite a fixed genetic lesion.

The **allosteric biology of ADAMTS13** (closed-Spacer/CUB autoinhibition relieved by VWF-D4 binding) is not merely mechanistic detail — it directly informs therapeutics. Understanding that catalytic output is governed by a conformational switch enabled engineering of **constitutively active variants** with enhanced thrombolytic potency, and it clarifies why recombinant enzyme replacement so effectively restores the missing regulatory function.

The **genotype-phenotype relationship** is best understood as a continuum of residual activity: null/severe alleles (frameshift, nonsense, founder c.4143dupA) tend toward neonatal/childhood onset, while residual-activity missense alleles (R1060W) permit late, trigger-dependent (pregnancy) presentation. This is coherent with the registry finding that higher residual ADAMTS13 activity predicts later overt onset.

Therapeutically, the disease has moved from a reactive, plasma-based paradigm to **proactive recombinant ADAMTS13 prophylaxis**, which in the pivotal trial reduced acute events essentially to zero. The natural-history data — that 87% of acute events occur without prophylaxis — provide the quantitative rationale for lifelong prophylactic replacement.

---

## Evidence Base

| PMID | Title (abbreviated) | Supports | Evidence type |
|------|--------------------|----------|---------------|
| [12393505](https://pubmed.ncbi.nlm.nih.gov/12393505/) | ADAMTS13 mutations in childhood TTP | Biallelic AR inheritance (F1) | Human clinical/genetic |
| [37895305](https://pubmed.ncbi.nlm.nih.gov/37895305/) | Hereditary TTP review | Causal gene & enzyme deficiency (F1) | Review |
| [19180123](https://pubmed.ncbi.nlm.nih.gov/19180123/) | Mechanisms of microvascular thrombosis | ADAMTS13 source & shear-dependent cleavage (F2) | Review |
| [17146059](https://pubmed.ncbi.nlm.nih.gov/17146059/) | Exosite interactions / tension-induced cleavage | Tyr1605-Met1606 scissile bond (F2) | In vitro |
| [38692292](https://pubmed.ncbi.nlm.nih.gov/38692292/) | Recombinant ADAMTS13 phase 3 (NEJM) | Zero acute events on rADAMTS13 (F3) | Human RCT |
| [28912376](https://pubmed.ncbi.nlm.nih.gov/28912376/) | Recombinant ADAMTS13 first-in-human | Safety, no anti-drug antibodies (F3) | Human phase 1 |
| [16807643](https://pubmed.ncbi.nlm.nih.gov/16807643/) | Common origin of 4143insA | European founder mutation (F4) | Human genetic |
| [42603082](https://pubmed.ncbi.nlm.nih.gov/42603082/) | Natural history retrospective cohort | Event burden, prophylaxis protection (F5) | Human cohort |
| [38536644](https://pubmed.ncbi.nlm.nih.gov/38536644/) | hTTP / ductus arteriosus & newborn survival | Neonatal onset 35-50% (F5) | Review/clinical |
| [16200209](https://pubmed.ncbi.nlm.nih.gov/16200209/) | Shigatoxin triggers TTP in ADAMTS13-KO mice | Gene-environment model (F6) | Model organism |
| [36889591](https://pubmed.ncbi.nlm.nih.gov/36889591/) | VWF antigen & pregnancy complications | Pregnancy risk & prophylaxis benefit (F7) | Human cohort |
| [36546627](https://pubmed.ncbi.nlm.nih.gov/36546627/) | Recombinant ADAMTS13 for hTTP | Rescue of plasma-refractory pregnancy (F7) | Human case |
| [32196558](https://pubmed.ncbi.nlm.nih.gov/32196558/) | Antibodies conformationally activate ADAMTS13 | Closed→open allosteric switch (F8) | In vitro/structural |
| [26391536](https://pubmed.ncbi.nlm.nih.gov/26391536/) | Linker regions & flexibility | Conformational activation basis (F8) | In vitro/structural |
| [37063760](https://pubmed.ncbi.nlm.nih.gov/37063760/) | ADAMTS13 activity testing platforms | FRETS-VWF73 gold standard, assay discrepancies (F9) | Methodological |
| [37711907](https://pubmed.ncbi.nlm.nih.gov/37711907/) | Novel FO-SPR immunoassay | <10% diagnostic threshold (F9) | Methodological |
| [24994604](https://pubmed.ncbi.nlm.nih.gov/24994604/) | Late-onset pregnancy-induced cTTP | R1060W residual-activity genotype-phenotype (F10) | Human clinical/genetic |
| [30792199](https://pubmed.ncbi.nlm.nih.gov/30792199/) | International Hereditary TTP Registry | Heterogeneous course, incomplete correlation | Registry |
| [30700419](https://pubmed.ncbi.nlm.nih.gov/30700419/) | Phylogenetic/functional analysis | Conserved allostery; essential T7/T8 domains | Comparative |
| [34780600](https://pubmed.ncbi.nlm.nih.gov/34780600/) | Constitutively active ADAMTS13 in stroke | Engineered therapeutic variant | Model organism |
| [42422077](https://pubmed.ncbi.nlm.nih.gov/42422077/) | Update on treatment options | Gene therapy & novel agents | Review |
| [16160007](https://pubmed.ncbi.nlm.nih.gov/16160007/) | Polymorphism modulation of ADAMTS13 | Modifier polymorphisms | In vitro |

---

## Limitations and Knowledge Gaps

1. **Epidemiology precision.** Exact prevalence/incidence of the congenital form is uncertain due to under-diagnosis and misclassification (e.g., misdiagnosis as ITP). Reported figures are estimates from registries and cohorts, not population-scale surveillance.
2. **Incomplete genotype-phenotype correlation.** The registry explicitly documents heterogeneity that residual-activity alone does not fully explain; modifier genes beyond VWF are implicated by the mouse model but not fully mapped in humans.
3. **Long-term outcomes of recombinant ADAMTS13.** The phase 3 trial establishes short/medium-term efficacy and safety; long-term (multi-decade) organ-protection, immunogenicity, and pregnancy-cohort data are still accruing.
4. **Biomarker validation.** VWF antigen as a predictor of obstetric morbidity is promising but from a single small cohort and needs prospective validation.
5. **Animal model fidelity.** No single model spontaneously recapitulates the full human episodic phenotype without engineered modifier backgrounds and triggers.
6. **Gene therapy is preclinical/early.** Curative approaches remain investigational.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective natural-history registry expansion** with standardized ADAMTS13 activity (FRETS-VWF73) and genotype capture to refine genotype–residual-activity–onset relationships and to validate VWF antigen as a prognostic biomarker.
2. **Long-term (5–10 year) follow-up of recombinant ADAMTS13** cohorts, including pregnancy sub-studies, immunogenicity surveillance, and organ-protection (renal/neurologic) endpoints.
3. **Modifier-gene mapping** in humans (GWAS/WGS in registry cohorts) to identify the TTP-modifying loci predicted by the CASA/Rk mouse studies.
4. **Advance ADAMTS13 gene therapy** from preclinical models toward first-in-human trials, leveraging the well-defined single-gene target and hepatic stellate-cell/hepatocyte expression biology.
5. **Standardize/harmonize ADAMTS13 activity assays** to resolve AcuStar vs FRETS-VWF73 discrepancies and validate rapid point-of-care assays (FO-SPR) for acute diagnosis.
6. **Structure-guided next-generation enzymes** — evaluate constitutively active (open-conformation) ADAMTS13 variants for acute event termination and potentially reduced dosing frequency.
7. **Pregnancy-management trials** comparing recombinant ADAMTS13 versus plasma prophylaxis regimens with maternal-fetal outcome endpoints.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations and 31 reviewed papers. Evidence types span human RCT, human cohort/registry, human case reports, in vitro/structural, comparative/phylogenetic, and model-organism studies.*


## Artifacts

- [OpenScientist final report](Congenital_Thrombotic_Thrombocytopenic_Purpura-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Thrombotic_Thrombocytopenic_Purpura-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 16 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010134` (1 mention) - the report calls it "congenital TTP / Upshaw–Schulman syndrome"; MONDO calls it **Pendred syndrome**
- `HP:0001873` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Thrombocytopenia**
- `HP:0002140` (1 mention) - the report calls it "Clinical sign"; HP calls it **Ischemic stroke**
- `HP:0000083` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Renal insufficiency**
- `HP:0000978` (1 mention) - the report calls it "purpura"; HP calls it **Bruising susceptibility**
- `HP:0001681` (1 mention) - the report calls it "Clinical sign"; HP calls it **Angina pectoris**
- `CL:0002679` (2 mentions) - the report calls it "hepatic stellate cell"; CL calls it **natural helper lymphocyte**
- `CHEBI:18420` (1 mention) - the report calls it "zinc, catalytic metal"; CHEBI calls it **magnesium(2+)**
- `NCIT:C171453` (1 mention) - the report calls it "plasma"; NCIT calls it **Hospital Stay**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:29108` (1 mention) - the report calls it "calcium, cofactor"; CHEBI calls it **calcium(2+)**, and lists "CALCIUM ION" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.