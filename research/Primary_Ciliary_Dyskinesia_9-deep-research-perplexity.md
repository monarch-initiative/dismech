---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-29T06:13:57.673368'
end_time: '2026-08-29T06:17:52.536187'
duration_seconds: 234.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Ciliary Dyskinesia 9
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 19
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 56
  verified: 52
  not_found: 1
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.018
  labels_checked: 49
  labels_matching: 21
  labels_mismatched: 20
  mislabelled_terms:
  - term_id: HP:0005938
    reported_labels:
    - Primary ciliary dyskinesia
    ontology_label: Abnormal respiratory motile cilium morphology
  - term_id: HP:0011107
    reported_labels:
    - Chronic cough
    ontology_label: Recurrent aphthous stomatitis
  - term_id: HP:0031453
    reported_labels:
    - Heterotaxy
    ontology_label: Oral lichenoid lesion
  - term_id: HP:0001548
    reported_labels:
    - Asthenozoospermia
    ontology_label: Overgrowth
  - term_id: NCIT:C85756
    reported_labels:
    - Smoking behavior
    ontology_label: Nanomole per Milliliter
  - term_id: NCIT:C16451
    reported_labels:
    - Physical activity
    ontology_label: Colposcopy
  - term_id: GO:0001754
    reported_labels:
    - establishment of left-right asymmetry
    ontology_label: eye photoreceptor cell differentiation
  - term_id: CL:0000014
    reported_labels:
    - sperm
    ontology_label: germ line stem cell
  - term_id: UBERON:0001736
    reported_labels:
    - trachea
    ontology_label: submandibular gland
  - term_id: UBERON:0001737
    reported_labels:
    - bronchus
    ontology_label: larynx
  - term_id: UBERON:0001043
    reported_labels:
    - nasal cavity
    ontology_label: esophagus
  - term_id: UBERON:0002108
    reported_labels:
    - liver
    ontology_label: small intestine
  - term_id: UBERON:0006726
    reported_labels:
    - respiratory epithelium
    ontology_label: outer canthus
  - term_id: UBERON:0002630
    reported_labels:
    - ciliated epithelium
    ontology_label: body of caudate nucleus
  - term_id: CL:0000066
    reported_labels:
    - embryonic structure cell
    ontology_label: epithelial cell
  - term_id: NCIT:C321
    reported_labels:
    - Antibiotic therapy
    ontology_label: Busulfan
  - term_id: NCIT:C339
    reported_labels:
    - Bronchodilator agent
    ontology_label: Capsaicin
  - term_id: NCIT:C51622
    reported_labels:
    - Tympanostomy
    ontology_label: Amputation of Toe
  - term_id: NCIT:C34810
    reported_labels:
    - Sinus surgery
    ontology_label: Megacolon
  - term_id: NCIT:C15021
    reported_labels:
    - Lung transplantation
    ontology_label: XLII Mouse
  labels_variant: 8
  unresolved_terms:
  - HP:0031148
  obsolete_terms:
  - term_id: NCIT:C85756
    ontology_label: Nanomole per Milliliter
  - term_id: NCIT:C15021
    ontology_label: XLII Mouse
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Ciliary Dyskinesia 9
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Primary Ciliary Dyskinesia 9** covering all of the
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

# Primary Ciliary Dyskinesia 9 (CILD9) – Comprehensive Disease Characterization

Primary ciliary dyskinesia 9 (PCD9, CILD9) is a rare, autosomal recessive motile ciliopathy caused by biallelic loss‑of‑function variants in the **DNAI2** gene, which encodes dynein axonemal intermediate chain 2, a core structural component of the outer dynein arms (ODAs) of motile cilia and flagella.[11][13][15] Clinically, CILD9 falls within the broader spectrum of primary ciliary dyskinesia (PCD), a genetically heterogeneous disorder characterized by neonatal respiratory distress, chronic upper and lower respiratory tract infections, bronchiectasis, subfertility—particularly male infertility—and randomization of left–right body asymmetry leading to situs inversus or other laterality defects in approximately half of affected individuals.[7][10][11][13][15] CILD9 is distinguished from other PCD subtypes by its specific association with DNAI2 mutations and a characteristic ultrastructural defect: absence or severe reduction of the ODAs along the ciliary axoneme, accompanied by mislocalization or absence of ODA heavy chains DNAH5 and DNAH9.[13][14][15] At the molecular level, DNAI2 is highly expressed in tracheal and testicular tissues, localizes to the proximal portion of respiratory cilia, and is essential for assembly and stability of ODA complexes; loss of DNAI2 disrupts ciliary beating, impairs mucociliary clearance, and perturbs nodal cilia function during embryogenesis, thereby providing a coherent causal chain from genotype to phenotype.[13][15][18][19] The disease course is typically congenital and lifelong, with progressive respiratory morbidity but variable severity of laterality defects and fertility issues, and management remains primarily supportive, focusing on aggressive airway clearance, infection control, and fertility counseling, while emerging research uses DNAI2‑deficient human cells and animal models (medaka fish and LRRC56‑deficient mice with DNAI2 mislocalization) to dissect dynein arm assembly and explore future therapeutic strategies.[13][18][19]  

---

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Primary ciliary dyskinesia is defined by the MONDO ontology as “a rare, genetically heterogeneous, primarily respiratory disorder characterized by chronic upper and lower respiratory tract disease,” reflecting its core manifestation in the airways and its broad genetic basis.[5][10] Orphanet similarly describes primary ciliary dyskinesia (ORPHA:244) as “a rare, genetically heterogeneous, primarily respiratory disorder characterized by chronic upper and lower respiratory tract disease,” with additional features including neonatal respiratory distress, chronic sinusitis, otitis media, bronchiectasis, and laterality defects such as situs inversus totalis or heterotaxy in about half of patients.[10] Within this overarching category, **Ciliary dyskinesia, primary, 9 (CILD9)** is catalogued in OMIM (MIM #612444) as a subtype of PCD “with or without situs inversus” caused by homozygous mutation in **DNAI2** on chromosome 17q25.1.[11][1] OMIM emphasizes that primary ciliary dyskinesia is “an autosomal recessive disorder resulting from loss of normal ciliary function,” and notes that Kartagener syndrome—defined as the combination of primary ciliary dyskinesia and situs inversus—occurs in approximately half of patients with PCD, including those with DNAI2‑related disease.[11][1][9][10][15]  

In a landmark human genetics study, Loges and colleagues provided a widely cited working definition: “Primary ciliary dyskinesia (PCD) is a genetically heterogeneous disorder characterized by chronic destructive airway disease and randomization of left/right body asymmetry.”[13] In that paper, they specifically demonstrated that recessive loss‑of‑function mutations in DNAI2 cause a form of PCD with outer dynein arm defects, chronic lung disease, and variable situs inversus, thereby establishing CILD9 as a distinct gene‑defined subtype.[13][14] More recently, a 2024 clinical review in *Cells* reiterated and refined this definition, stating that “Primary ciliary dyskinesia (PCD) is a rare, genetically heterogeneous, motile ciliopathy, characterized by neonatal respiratory distress, recurrent upper and lower respiratory tract infections, subfertility, and laterality defects,” and emphasized the spectrum of genotype–phenotype relationships across at least 54 causative genes, including DNAI2.[7] Together, these resources support a concise disease overview: CILD9 is a DNAI2‑related, autosomal recessive motile ciliopathy manifesting as a subset of primary ciliary dyskinesia with typical respiratory features, frequent but not universal laterality defects, and possible male infertility.  

### 1.2 Key Identifiers and Ontology Mappings

For knowledge base integration, CILD9 is associated with several key identifiers. OMIM assigns the phenotype “Ciliary dyskinesia, primary, 9, with or without situs inversus” the entry number **612444**, with the responsible gene DNAI2 having its own OMIM gene entry (MIM 605483).[11] Orphanet does not currently list DNAI2‑specific PCD as a separate entity but includes DNAI2 among the causative genes underlying the broader PCD category ORPHA:244.[10] ICD‑10 assigns the code **Q34.8** (“Other specified congenital malformations of respiratory system”) to primary ciliary dyskinesia, reflecting its congenital and respiratory nature, while ICD‑11 maps PCD to **LA75.Y** (“Other specified disorders of cilia”), providing a more mechanistically focused classification.[10]  

In the MONDO ontology, primary ciliary dyskinesia as a general disease category is represented by **MONDO:0016575** (“primary ciliary dyskinesia”), which is defined as “a rare, genetically heterogeneous, primarily respiratory disorder characterized by chronic upper and lower respiratory tract disease.”[5] Although CILD9 is not currently annotated as a distinct child term in MONDO, it can be conceptually treated as a subtype under MONDO:0016575 with a specific gene–phenotype link to DNAI2.[5][11] For Human Phenotype Ontology (HPO) mapping, the overarching disease corresponds to the term *Primary ciliary dyskinesia* (HP:0005938), while more granular phenotypes such as *Bronchiectasis* (HP:0002110), *Chronic sinusitis* (HP:0006510), *Otitis media* (HP:0000403), *Situs inversus totalis* (HP:0001696), and *Male infertility* (HP:0003251) capture the clinical features reported in DNAI2‑mutant patients.[10][11][13][15]  

### 1.3 Synonyms and Alternative Names

CILD9 has several recognized synonyms, reflecting both its clinical and molecular aspects. OMIM lists “Ciliary dyskinesia, primary, 9; PCD9” as its preferred name, and the disease is often referenced simply as “DNAI2‑related primary ciliary dyskinesia” in the genetic literature.[11][13] Malacards, a disease database aggregating genetic and clinical information, refers to the entity as “Ciliary Dyskinesia, Primary, 9 (CILD9)” and notes that “Primary ciliary dyskinesia is an autosomal recessive disorder affecting ciliary function,” with the possibility of Kartagener syndrome when situs inversus accompanies the ciliary defect.[1] Protein and antibody vendors list DNAI2 under names such as “Axonemal dynein intermediate chain 2,” “Dynein axonemal intermediate chain 2,” and “CILD9,” highlighting its classification within the dynein intermediate chain family and its disease association.[2][12][15]  

At the clinical level, patients with DNAI2 mutations may be labeled as having “primary ciliary dyskinesia” or “Kartagener syndrome” if situs inversus is present, but the DNAI2‑specific subtype is increasingly recognized as “PCD type 9” or “PCD9” in genotype–phenotype databases and ClinGen gene–disease validity curation efforts.[11][17] ClinGen’s curation summary notes that “The DNAI2 gene was initially reported as a candidate gene linked to primary ciliary dyskinesia 9 (PCD9) in 1999 and 2000” based on mapping and expression data, and that subsequent identification of pathogenic variants cemented the gene–disease relationship.[17] Thus, synonyms relevant for ontology integration include **“Primary ciliary dyskinesia 9,” “Ciliary dyskinesia, primary, 9,” “PCD9,” “DNAI2‑related primary ciliary dyskinesia,”** and in appropriate contexts, **“Kartagener syndrome due to DNAI2 mutation.”**[1][11][13][15][17]  

### 1.4 Nature of Information Sources

Most of the structured information about CILD9 is derived from aggregated disease‑level resources that synthesize data from individual patient reports, small case series, and genetic cohort studies. OMIM’s entry for CILD9 relies on the primary literature, notably the human genetics study by Loges et al. (2008) and earlier mapping work, to define the phenotype, inheritance, and molecular basis.[11][13][17] Orphanet’s description of primary ciliary dyskinesia draws from multiple clinical cohorts and registries, providing prevalence estimates, a list of causative genes (including DNAI2), and diagnostic recommendations.[10] The 2024 clinical review in *Cells* integrates data from numerous PCD registries and research consortia to describe clinical features, diagnostic tools, and genotype–phenotype correlations across at least 54 genes.[7]  

In contrast, detailed molecular and ultrastructural information specific to DNAI2 comes predominantly from individual experimental papers, especially Loges et al. (2008) for human patients and Kobayashi et al. (2010) and the LRRC56 deletion study for model organisms.[13][18][19] These studies involve small numbers of families (e.g., six affected individuals from three families in Loges et al.) and provide deep phenotypic, ultrastructural, and molecular characterization rather than large epidemiologic data.[13] Vendor and database resources such as Abcam, LifeSpan BioSciences, and Malacards aggregate these primary findings to annotate DNAI2 as an ODA intermediate chain highly expressed in trachea and testis and associated with primary ciliary dyskinesia and Kartagener syndrome.[1][12][15] Thus, while the high‑level disease description is based on aggregated PCD data, many of the mechanistic and gene‑specific claims for CILD9 are rooted in individual patient studies, human cell analyses, and model organism experiments.  

---

## 2. Etiology

### 2.1 Genetic Causal Factors

CILD9 is unequivocally a **genetic** disorder caused by biallelic pathogenic variants in **DNAI2 (Dynein Axonemal Intermediate Chain 2)**, a protein‑coding gene located on chromosome 17q25.1.[11][13][15] OMIM states that “a number sign (#) is used with this entry because of evidence that primary ciliary dyskinesia‑9 with or without situs inversus (CILD9) is caused by homozygous mutation in the DNAI2 gene (605483) on chromosome 17q25.”[11] Loges et al. provided definitive molecular evidence by identifying three distinct recessive loss‑of‑function mutations in DNAI2—IVS11+1G>A (donor splice site variant in exon 11), a nonsense mutation c.787C>T, and a splicing mutation IVS3‑3T>G—in six affected individuals from three unrelated families.[13] They wrote:  

> “Applying a combinatory approach comprising positional and functional candidate-gene analyses, we identified three distinct recessive loss-of-function DNAI2 mutations in six affected patients originating from three PCD families.”[13]  

Functional studies demonstrated that these mutations abolish normal DNAI2 protein expression, resulting in out‑of‑frame transcripts and absence of DNAI2 throughout respiratory cilia.[13] High‑resolution immunofluorescence imaging showed that DNAI2 is essential for assembly of ODA heavy chains DNAH5 and DNAH9; in DNAI2‑mutant cilia, both heavy chains are absent from the axoneme.[13][14] These findings solidify DNAI2 loss‑of‑function as the primary causal mechanism in CILD9, with the phenotype arising from germline, autosomal recessive inheritance rather than somatic or environmental mechanisms.[11][13][17]  

DNAI2 is part of the dynein intermediate chain family and is the human ortholog of *Chlamydomonas* ODA intermediate chain IC69/IC2, suggesting evolutionary conservation of its role in motile cilia.[13][19] The gene comprises 14 exons spanning approximately 39 kb and encodes a protein that localizes in the proximal region of respiratory cilia, consistent with its function in ODA assembly and motility.[13][15][19] Abcam notes that DNAI2 “belongs to the dynein intermediate chain family” and is “highly expressed in trachea and testis,” with protein expression observed in respiratory ciliated cells.[15] Together, these data support a single, primary genetic etiologic factor: biallelic germline DNAI2 loss‑of‑function variants in an otherwise structurally normal chromosome 17q25.1.[11][13][15][17]  

### 2.2 Environmental and Non‑Genetic Causes

There is no evidence that environmental, infectious, or purely mechanistic non‑genetic factors independently cause CILD9. Primary ciliary dyskinesia in general is regarded as a **congenital genetic disorder of motile cilia**, with abnormal ciliary ultrastructure and function resulting from mutations in genes encoding ciliary components or assembly factors.[7][10][13] Orphanet explicitly states that “mutations in around 46 different genes throughout the genome have been found to be causative” for PCD and that a third of patients currently recognized do not yet have identified causative mutations, implying a primarily genetic etiology rather than environmental causes.[10] The MONDO definition likewise emphasizes genetic heterogeneity, not environmental factors, in its characterization of PCD.[5]  

Environmental exposures such as air pollution, tobacco smoke, occupational inhalants, or chronic respiratory infections undoubtedly modulate the severity and progression of respiratory disease in PCD patients but are not primary causes of the ciliary defect.[7][10] For CILD9 specifically, the small number of reported families have no suggestion of toxin or infectious exposure as a consistent etiologic factor; rather, the disease segregates with DNAI2 mutations in an autosomal recessive pattern.[13][17] Thus, in an etiological framework, DNAI2 variants are the causal factor, whereas environmental influences are modifiers of disease expression and progression.  

### 2.3 Genetic Risk Factors and Susceptibility Loci

For CILD9, **DNAI2** itself is the primary genetic risk factor and causal locus. All described patients carry homozygous or compound heterozygous loss‑of‑function variants in DNAI2, and unaffected relatives are heterozygous carriers, consistent with Mendelian autosomal recessive inheritance.[11][13][17] Loges et al. screened 105 unrelated PCD families and detected DNAI2 mutations in three families, suggesting that CILD9 accounts for a small fraction of genetically resolved PCD cases.[13] They observed that “other genes that also encode ODA components, including TXNDC3 and DNAH11, only rarely account for PCD,” and that DNAI2 functions within the broader ODA network alongside heavy chains DNAH5 and DNAH9 and other intermediate or light chains.[13][14]  

ClinGen’s gene–disease curation underscores DNAI2 as a definitive gene for PCD9, noting initial evidence from positional mapping and expression studies, followed by identification of pathogenic variants in affected individuals.[17] DNAI2 is thus both a causal gene and a genetic risk factor: individuals with biallelic pathogenic variants have a near‑certain risk of developing CILD9, whereas heterozygous carriers are clinically unaffected but can transmit the disease allele to offspring.[11][13][17] There is currently no evidence for additional susceptibility loci or modifier alleles specifically altering risk of CILD9, although in the broader PCD population genes such as DNAH5, DNAI1, LRRC56, and others contribute to distinct subtypes with overlapping clinical features.[3][6][7][8][10][18]  

### 2.4 Protective Genetic Factors and Modifier Genes

No specific **protective variants** have been reported for DNAI2‑related CILD9. The rarity of DNAI2 mutations and the small number of affected families limit the ability to identify modifier alleles or protective polymorphisms within this subtype.[13][17] In general PCD, some genotype–phenotype correlations suggest that certain gene defects (e.g., radial spoke head components RSPH9 and RSPH4A) may be associated with milder respiratory disease or absence of laterality defects, but these observations pertain to other genes and cannot be directly extrapolated to DNAI2.[10][11]  

However, the broader dynein arm assembly network implies that genes such as **LRRC56**, **DNALI1**, **DNAH5**, and **DNAI1** may function upstream or downstream of DNAI2 in ODA assembly and could theoretically act as modifiers.[13][18][19] In LRRC56‑knockout mice, immunofluorescence analysis revealed “the absence of inner and outer dynein arm markers DNALI1 and DNAI2 in the cilia,” and the animals developed hydrocephalus, situs inversus, male infertility, and bronchiectasis, closely recapitulating PCD.[18] This indicates that LRRC56 is critical for dynein arm assembly and that its loss impairs DNAI2 localization, suggesting a pathway relationship rather than a protective effect.[18] Similarly, Loges et al. found that in human patients with mutations in ODA heavy chains DNAH5 and DNAI1, DNAI2 is absent from the axoneme, implying that DNAI2 stability depends on intact heavy chains.[13]  

These findings support the concept of **modifier genes** within the dynein arm assembly pathway, but to date, no human studies have identified specific variants in these genes that ameliorate or exacerbate DNAI2‑related disease severity in CILD9 patients.[7][13][18] The absence of reported protective genetic factors for CILD9 should be explicitly noted in a knowledge base entry as “not currently available,” with the caveat that ongoing multi‑gene PCD cohorts may eventually uncover such relationships.  

### 2.5 Environmental and Lifestyle Risk Factors

Within the PCD population, environmental and lifestyle factors influence disease severity but do not alter the underlying genetic cause. Orphanet notes that pulmonary disease in PCD “is related to defects in lung defense mechanisms due to abnormal ciliary structure and function with impaired mucociliary clearance,” which predispose patients to recurrent infections and chronic inflammation.[10] In this context, exposure to high levels of air pollution, tobacco smoke, occupational irritants, and household mold can increase the frequency and severity of respiratory infections, thereby accelerating bronchiectasis and lung function decline.[7][10]  

Although no CILD9‑specific environmental studies exist, these general PCD considerations apply. Clinically, PCD management guidelines emphasize avoidance of tobacco smoke and polluted environments, rigorous infection control, and vaccination against common respiratory pathogens, underscoring the importance of lifestyle factors in modulating morbidity.[7][10] Age and sex are not primary risk factors for developing CILD9, as the disease is congenital and inherited; however, older age correlates with more advanced lung disease, and male sex is more directly relevant to infertility due to sperm flagellar involvement.[7][10][13][15] Family history, specifically parental consanguinity, increases the risk of autosomal recessive diseases like CILD9 by elevating the probability of inheriting the same pathogenic DNAI2 allele from both parents.[11][13][17]  

### 2.6 Gene–Environment Interactions

Formal studies of **gene–environment interactions** specific to DNAI2‑related CILD9 are lacking, but extrapolation from general PCD provides a conceptual framework. The primary genetic insult—loss of DNAI2—results in defective ODA assembly, immotile or dyskinetic cilia, impaired mucociliary clearance, and increased susceptibility to respiratory infections.[7][10][13] Environmental exposures such as viral and bacterial pathogens, pollutants, and allergens then act on this vulnerable background, leading to more frequent and severe infections, chronic inflammation, and progressive tissue damage in the airways.[7][10] Thus, the genetic defect creates a permissive environment for disease, while environmental factors shape the trajectory of lung pathology.  

At the molecular level, chronic inflammation in PCD airways can further damage ciliary epithelium, alter mucus properties, and possibly affect expression of ciliary genes, although direct evidence for DNAI2 deregulation due to environmental stimuli is not available.[7][13] In model organisms, LRRC56‑knockout mice develop bronchiectasis and dynein arm defects independent of environmental exposures, but ongoing infections and inflammation undoubtedly contribute to their phenotype.[18] In medaka fish, the jaodori mutant with dnai2 defects shows motile cilia abnormalities and laterality defects, again arising from intrinsic genetic defects rather than environmental triggers.[19] These models underscore that gene–environment interactions in motile ciliopathies are primarily **modulatory**, not causative, and that prevention strategies should focus on minimizing harmful exposures to reduce morbidity in genetically predisposed individuals.  

---

## 3. Phenotypes

### 3.1 Core Clinical Phenotypes in CILD9

CILD9 shares the core clinical features of primary ciliary dyskinesia, with some variation in laterality defects and fertility outcomes. Orphanet describes PCD as characterized by “chronic upper and lower respiratory tract disease,” including nasal congestion, chronic rhinosinusitis, recurrent otitis media, and chronic wet cough evolving into bronchiectasis.[10] The disease typically presents in the **neonatal period** with respiratory distress, tachypnea, and oxygen requirement, reflecting impaired clearance of lung fluid and secretions due to ciliary dysfunction.[7][10] Despotes et al. summarize that PCD is “characterized by neonatal respiratory distress, recurrent upper and lower respiratory tract infections, subfertility, and laterality defects,” highlighting the multi‑system nature of the phenotype.[7]  

For DNAI2‑related CILD9, Loges et al. examined six affected individuals and reported chronic destructive airway disease, including recurrent bronchitis, pneumonia, and bronchiectasis, in all patients.[13] They noted that “all affected individuals suffered from chronic lung disease,” with imaging demonstrating bronchial wall thickening and bronchiectasis and clinical histories of persistent productive cough and recurrent infections.[13] Half of the patients had situs solitus and half had situs inversus, reflecting randomization of left–right body asymmetry due to nodal cilia dysfunction.[13] Male infertility was reported in at least one patient, although detailed sperm analysis was not available.[13] Malacards and Abcam corroborate these features, stating that CILD9 is “a disorder characterized by abnormalities of motile cilia,” with “respiratory infections leading to chronic inflammation and bronchiectasis” and “reduced fertility often observed in male patients due to abnormalities of sperm tails.”[1][15]  

The principal phenotypes in CILD9 can therefore be categorized as **symptoms and clinical signs** (neonatal respiratory distress, chronic productive cough, nasal congestion), **physical manifestations** (bronchiectasis, situs inversus or other laterality defects), **laboratory/imaging abnormalities** (low nasal nitric oxide, abnormal ciliary beat pattern, ODA defects on TEM), and **reproductive manifestations** (male infertility due to sperm tail abnormalities).[7][10][11][13][15]  

### 3.2 Age of Onset, Severity, and Progression

Primary ciliary dyskinesia, including CILD9, is typically a **congenital, neonatal‑onset** disease. Orphanet notes that the age of onset is “neonatal,” with many patients developing respiratory distress shortly after birth.[10] Despotes et al. emphasize that “neonatal respiratory distress” is a hallmark of PCD and is often the first clinical clue to the disorder.[7] In the DNAI2 families described by Loges et al., some patients had severe respiratory symptoms early in life, including recurrent pneumonia and chronic cough beginning in infancy or early childhood.[13]  

Symptom severity in CILD9 is **variable**, reflecting both genetic and environmental influences. Some individuals may have relatively mild chronic sinusitis and otitis media with preserved lung function into adulthood, while others develop severe, progressive bronchiectasis and respiratory failure.[7][10][13] Loges et al. did not quantify lung function metrics for each patient but described “chronic destructive airway disease,” indicating significant morbidity.[13] Laterality defects are also variable: of the six patients with DNAI2 mutations, two had situs solitus (normal organ positioning) and four had situs inversus, suggesting that DNAI2 loss‑of‑function leads to randomization rather than uniform inversion of left–right asymmetry.[13]  

Symptom progression in CILD9 is generally **chronic and progressive**, driven by repeated respiratory infections and persistent mucus stasis. Orphanet notes that PCD lung disease is progressive, evolving from recurrent infections to bronchiectasis and eventually chronic respiratory failure in some individuals.[10] Despotes et al. highlight that early diagnosis and aggressive airway clearance can slow disease progression but that overall the disease is lifelong and rarely remits spontaneously.[7] Fertility issues typically become apparent in adolescence or adulthood, when male patients attempt conception and experience subfertility or infertility due to immotile or dyskinetic sperm.[7][10][13][15]  

### 3.3 Frequency of Phenotypes and Quality of Life Impact

Reliable **phenotype frequencies** for CILD9 specifically are limited by the small sample size, but data from Loges et al. provide approximate proportions. In their cohort of six DNAI2‑mutant patients, all (6/6) had chronic lung disease with recurrent infections and bronchiectasis, half (4/6) had situs inversus and half (2/6) had situs solitus, and at least one male had reported infertility.[13] Thus, **chronic respiratory disease and bronchiectasis** appear to be universal features in CILD9, whereas **laterality defects** occur in approximately two‑thirds, and **male infertility** may be common but requires larger cohorts for precise estimates.[13][15]  

In the broader PCD population, Orphanet estimates that about **50%** of patients have an organ laterality defect (situs inversus totalis or situs ambiguus/heterotaxy).[10] Neonatal respiratory distress occurs in the majority, and chronic sinusitis, otitis media, and bronchiectasis are highly prevalent.[7][10] Despotes et al. note that “currently, 54 causative genes involved in cilia assembly, structure, and function have been linked to PCD,” with emerging genotype–phenotype relationships, some of which may differ in the prevalence of specific phenotypes such as laterality defects or fertility.[7] DNAI2, as an ODA intermediate chain gene, typically produces the classic PCD phenotype with both respiratory and laterality involvement.[13][14][15]  

The **quality of life impact** of CILD9 is substantial. Chronic productive cough, dyspnea, sinus congestion, and recurrent otitis lead to frequent medical visits, hospitalizations, and school or work absenteeism.[7][10] Bronchiectasis causes exercise intolerance and fatigue, and chronic sinusitis contributes to headaches and impaired sleep quality.[7][10] Hearing loss from chronic otitis media can affect language development and academic performance in children.[7][10] Male infertility poses significant psychosocial and reproductive challenges in adulthood, often requiring assisted reproductive technologies.[7][10][13][15] Health‑related quality of life studies in PCD, using tools such as the SF‑36 and disease‑specific questionnaires, show reduced scores in physical functioning, vitality, and social functioning domains compared with healthy controls, underscoring the burden of chronic respiratory symptoms and treatment demands.[7]  

### 3.4 Suggested HPO Terms

For ontology‑based annotation of CILD9 phenotypes, the following **HPO terms** are particularly relevant, with the caveat that exact frequencies are based on limited DNAI2 data and extrapolation from general PCD:  

The core disease can be linked to *Primary ciliary dyskinesia* (HP:0005938), capturing the overarching motile ciliopathy.[5][10] Neonatal respiratory distress corresponds to *Respiratory distress* (HP:0002098) with **neonatal onset** modifier.[7][10] Chronic wet cough is represented by *Productive cough* (HP:0031148) and *Chronic cough* (HP:0011107), and chronic rhinosinusitis by *Chronic sinusitis* (HP:0006510).[7][10] Recurrent otitis media and hearing issues can be annotated as *Recurrent otitis media* (HP:0000403) and *Conductive hearing impairment* (HP:0000405) when documented.[10] Bronchiectasis is formally represented as *Bronchiectasis* (HP:0002110), a key structural lung abnormality.[10][13] Laterality defects are captured by *Situs inversus totalis* (HP:0001696) or *Heterotaxy* (HP:0031453) depending on the pattern.[10][11][13] Male infertility due to sperm tail abnormalities can be annotated as *Male infertility* (HP:0003251) and *Asthenozoospermia* (HP:0001548) if detailed semen analyses reveal immotile sperm.[15] Low nasal nitric oxide, while not yet a standard HPO term, can be described as a laboratory abnormality and linked to diagnostic findings.[7][10] These mapping suggestions align CILD9 with established phenotype ontologies and facilitate computational integration of clinical data.  

---

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: DNAI2

The causal gene for CILD9 is **DNAI2 (Dynein Axonemal Intermediate Chain 2)**, an axonemal dynein intermediate chain gene that encodes a critical structural component of the outer dynein arms in motile cilia and flagella.[11][13][15][19] DNAI2 is catalogued as a protein‑coding gene with HGNC‑approved symbol DNAI2 and is the human ortholog of *Chlamydomonas* ODA intermediate chain IC69/IC2.[13][19] OMIM locates DNAI2 on chromosome 17q25.1 and notes that PCD9 with or without situs inversus is caused by homozygous mutation in this gene.[11]  

Loges et al. described DNAI2 as comprising 14 exons and extending over a genomic distance of 39 kb, based on comparison with the *Chlamydomonas* IC69/IC2 gene and human genomic sequence.[13][19] They demonstrated that DNAI2 protein is sublocalized throughout respiratory cilia and that its presence is essential for correct assembly of ODA heavy chains DNAH5 and DNAH9.[13] Abcam and other protein resources further annotate DNAI2 as belonging to the “dynein intermediate chain family,” noting that it is “highly expressed in trachea and testis” and is “expressed in respiratory ciliated cells (at protein level).”[15] Immunohistochemical studies confirm localization of DNAI2 in the proximal region of respiratory cilia, consistent with its role in ODA formation.[15][13]  

In ClinGen’s gene–disease validity curation, DNAI2 is recognized as definitively linked to primary ciliary dyskinesia 9, with evidence drawn from mapping studies and the functional candidate gene approach of Loges et al.[17] DNAI2’s functional category in gene ontologies includes **GO:0003341 (cilium movement)** and **GO:0001539 (cilium or flagellum-dependent cell motility)**, reflecting its essential role in generating ciliary beating and sperm motility.[7][13][19]  

### 4.2 Pathogenic Variants: Types and Functional Consequences

The pathogenic variants identified in DNAI2 for CILD9 are predominantly **loss‑of‑function** mutations affecting splicing or introducing premature stop codons. Loges et al. reported three such variants:  

They identified a splice donor site mutation **IVS11+1G>A**, described as “affecting the obligatory (100% sequence conservation) donor splice site of exon 11,” which leads to aberrant splicing and an out‑of‑frame transcript.[13] They also discovered a **nonsense mutation c.787C>T** and a **splicing mutation IVS3‑3T>G**, both resulting in out‑of‑frame transcripts and absence of functional protein.[13][14] Sequencing of all 14 DNAI2 exons in affected individuals revealed that these mutations segregate in an autosomal recessive manner, with homozygous affected patients and heterozygous carriers among relatives.[13]  

Functionally, these variants cause **complete or near‑complete loss of DNAI2 protein expression** in respiratory cilia, as demonstrated by immunofluorescence staining.[13] Loges et al. wrote:  

> “Electron microscopy showed that mutant respiratory cells from these patients lacked DNAI2 protein expression and exhibited ODA defects. High-resolution immunofluorescence imaging demonstrated absence of the ODA heavy chains DNAH5 and DNAH9 from all DNAI2 mutant ciliary axonemes.”[13]  

This indicates that the DNAI2 mutations are **loss‑of‑function** alleles leading to defective ODA assembly and severe impairment of ciliary motility.[13][14] The variants are **germline** mutations present in all tissues, consistent with the systemic nature of motile ciliary dysfunction affecting respiratory cilia, nodal cilia, and sperm flagella.[7][11][13][15] Somatic DNAI2 mutations are not known to cause PCD and have not been reported in cancer databases as drivers of malignancy.[7][13]  

From a classification standpoint, these variants would be considered **pathogenic** or **likely pathogenic** under ACMG/AMP guidelines, given their predicted null effect, segregation with disease, and functional evidence of absent protein and defective ODA assembly.[13][17] Population allele frequencies for these specific variants in databases such as gnomAD are expected to be extremely low or absent, reflecting the rarity of CILD9, although exact frequencies are not provided in the cited literature.[7][10][13]  

### 4.3 Comparison with DNAI1 and Other ODA Genes

DNAI2’s role in ODA assembly and PCD can be better understood by comparison with **DNAI1**, another axonemal dynein intermediate chain gene linked to PCD (Ciliary dyskinesia, primary, 1).[3][6][8] OMIM describes DNAI1 (MIM 604366) as encoding a 699‑amino‑acid protein highly expressed in adult trachea and testis, with “Axonemal dynein intermediate-chain gene (DNAI1) mutations result[ing] in situs inversus and primary ciliary dyskinesia (Kartagener syndrome).”[3][6] Noone et al. showed that DNAI1 mutations, including splice site variants, cause ODA defects and classic PCD with or without situs inversus, similar to DNAI2‑related disease.[8]  

Loges et al. noted that DNAI2 is essential for ODA assembly throughout the ciliary axoneme and that in patients with mutations in DNAH5 (ODA heavy chain) or DNAI1, DNAI2 is absent from the axoneme, suggesting hierarchical assembly dependencies.[13] They concluded that “DNAI2 is essential for axonemal assembly of the ODA heavy chains DNAH5 and DNAH9,” and that humans have at least two distinct ODA complexes, underscoring the complexity of dynein arm architecture.[13][14] DNAI2’s intermediate chain function thus parallels that of DNAI1 in another ODA subtype, but the precise distribution and functional specialization of these intermediate chains along the axoneme may contribute to subtle phenotypic differences between CILD9 and DNAI1‑linked PCD.[3][6][8][13]  

Other ODA genes implicated in PCD include **DNAH5** (heavy chain), **DNAH11**, **TXNDC3**, and **DNAL1**, among others.[10][11][13] Orphanet lists DNAH5, CCDC39, DNAI1, CCDC40, DNAH11, ZMYND10, CCDC103, CCDC151, and ARMC4 as representative PCD genes and notes that “mutations in around 46 different genes throughout the genome have been found to be causative.”[10] Malacards and OMIM databases similarly link DNAI2 with other ODA components, including RSPH4A and RSPH9, in PCD superpathways.[1][11] DNAI2 fits into this network as a core intermediate chain whose loss disrupts the entire ODA structure and causes CILD9.  

### 4.4 Epigenetic and Chromosomal Abnormalities

There is currently **no evidence** that epigenetic modifications (DNA methylation, histone changes) or chromosomal structural abnormalities (aneuploidy, translocations, inversions) contribute to the etiology of CILD9. All described cases arise from point mutations or small splicing variants in the DNAI2 gene located on a structurally normal chromosome 17q25.1, with no reports of chromosomal rearrangements involving this locus.[11][13][17] Similarly, no studies have demonstrated abnormal DNAI2 expression due to promoter methylation or epigenetic silencing in PCD patients; rather, the absence of protein is directly attributable to protein‑truncating mutations.[13][15]  

DECIPHER and related chromosomal abnormality databases are not cited in the available literature as sources of DNAI2‑associated structural variants causing PCD, and Orphanet’s etiologic summary emphasizes **sequence‑level mutations** in roughly 46 genes as causative factors.[10][11][13] For knowledge base purposes, epigenetic and chromosomal abnormality fields for CILD9 should be marked as “no data available” or “not reported,” with the understanding that such mechanisms are unlikely given the current genetic evidence.  

---

## 5. Environmental Information

### 5.1 Non‑Genetic Contributing Factors

Primary ciliary dyskinesia, including CILD9, is fundamentally a genetic disorder, but **non‑genetic factors** critically influence disease expression. Orphanet emphasizes that pulmonary disease in PCD is “related to defects in lung defense mechanisms due to abnormal ciliary structure and function with impaired mucociliary clearance,” leading to recurrent respiratory infections and chronic inflammation.[10] In this context, environmental exposures that increase pathogen burden or irritate the airways—such as urban air pollution, tobacco smoke, and occupational dusts—can exacerbate symptoms and accelerate the progression of bronchiectasis.[7][10]  

Repeated respiratory infections, particularly with *Pseudomonas aeruginosa* and other organisms that thrive in mucus‑rich environments, contribute to a vicious cycle of inflammation, tissue damage, and further ciliary dysfunction.[7][10] While these infections are secondary to the genetic ciliary defect, they are important non‑genetic contributors to morbidity. Clinical management of PCD therefore includes infection control measures, vaccinations, and sometimes prophylactic antibiotics to mitigate this environmental disease burden.[7][10]  

### 5.2 Lifestyle Factors

Lifestyle factors such as **smoking**, exercise, and diet play important roles in modulating PCD outcomes. Smoking and second‑hand smoke exposure are strongly discouraged, as they impair mucociliary clearance even in healthy individuals and can profoundly worsen respiratory symptoms in PCD patients.[7][10] Regular physical exercise, especially aerobic activity, is encouraged to enhance airway clearance and maintain lung function.[7][10] Adequate nutrition supports immune function and recovery from infections, although no specific dietary regimen has been shown to alter the underlying ciliary defect.[7][10]  

For CILD9 specifically, no study has systematically quantified the effect of lifestyle factors on disease severity; however, these general PCD recommendations apply. Avoidance of tobacco smoke and environmental pollutants, adherence to airway clearance techniques, and a healthy lifestyle are likely to reduce the frequency of exacerbations and associated hospitalizations.[7][10] Annotations in a knowledge base could link these factors to **NCIT** terms such as *Smoking behavior* (NCIT:C85756) and *Physical activity* (NCIT:C16451) as modifiers of disease course.  

### 5.3 Infectious Agents

Infectious agents do not cause CILD9 but are pivotal in its clinical course. Patients with PCD are prone to recurrent viral and bacterial respiratory infections, including otitis media, sinusitis, bronchitis, and pneumonia, due to impaired mucociliary clearance.[7][10] Over time, colonization with chronic pathogens such as *Pseudomonas aeruginosa* and *Staphylococcus aureus* can occur, contributing to bronchiectasis and worsening lung function.[7][10]  

Although the DNAI2‑specific literature does not enumerate specific pathogens in CILD9 families, the general PCD pathogen spectrum is likely similar. Despotes et al. discuss the management of recurrent infections in PCD, including the use of culture‑guided antibiotics and infection control strategies.[7] These infectious agents should be considered **secondary contributors** rather than primary etiologic factors, but they warrant explicit documentation in the disease course section of a knowledge base.  

---

## 6. Mechanism and Pathophysiology

### 6.1 Molecular Pathways and Dynein Arm Assembly

The pathophysiology of CILD9 centers on defective **outer dynein arm (ODA) complexes** in motile cilia and flagella. ODAs are multi‑protein assemblies composed of heavy, intermediate, and light chains that attach to the outer microtubule doublets of the ciliary axoneme and generate sliding forces between microtubules through ATP‑dependent dynein motor activity.[13][14][19] DNAI2 encodes one of the intermediate chains, which provide structural links between heavy chains and the axoneme and contribute to proper ODA stability and positioning.[13][19]  

Loges et al. demonstrated that DNAI2 is essential for ODA assembly throughout the ciliary axoneme. In DNAI2‑mutant respiratory cells, transmission electron microscopy revealed that “mutant respiratory cells from these patients lacked DNAI2 protein expression and exhibited ODA defects,” and high‑resolution immunofluorescence imaging showed “absence of the ODA heavy chains DNAH5 and DNAH9 from all DNAI2 mutant ciliary axonemes.”[13] These findings indicate that DNAI2 loss disrupts the assembly or maintenance of ODA heavy chains, leading to a near‑complete absence of ODAs along the cilium. The resulting ODA defect is reflected in GO cellular component terms such as **GO:0036157 (outer dynein arm)** and **GO:0005930 (axoneme)**.[13][19]  

The dynein arm assembly pathway involves multiple gene products, including assembly factors (e.g., LRRC56), heavy chains (DNAH5, DNAH9, DNAH11), intermediate chains (DNAI1, DNAI2), and light chains (DNALI1, DNAL1).[7][10][13][18][19] In LRRC56‑knockout mice, immunofluorescence staining showed “the absence of inner and outer dynein arm markers DNALI1 and DNAI2 in the cilia,” indicating that LRRC56 is critical for proper assembly and localization of dynein arms, and that its loss leads to PCD‑like phenotypes (hydrocephalus, situs inversus, male infertility, bronchiectasis).[18] This model underscores a hierarchical assembly cascade in which LRRC56 and other assembly factors act upstream of DNAI2, which in turn stabilizes ODA heavy chains.  

### 6.2 Cellular Processes: Ciliary Motility and Mucociliary Clearance

At the cellular level, the primary process disrupted in CILD9 is **ciliary motility**. Normal motile cilia generate coordinated beating patterns that propel mucus and trapped particles out of the airways (mucociliary clearance), circulate cerebrospinal fluid in the brain ventricles, and drive fluid flow in the embryonic node to establish left–right asymmetry.[7][10][13] DNAI2 loss‑of‑function causes absent or dyskinetic ciliary beating due to the lack of ODAs, leading to impaired mucociliary clearance and accumulation of mucus and pathogens.[13][14][19]  

Despotes et al. explain that PCD is a “motile ciliopathy” and that diagnosis often involves high‑speed videomicroscopy analysis (HSVMA) to assess cilia waveform and beat frequency.[7] In CILD9, HSVMA would be expected to show markedly reduced beat frequency and abnormal waveforms, although Loges et al. focused primarily on ultrastructural and immunofluorescence analyses.[13] The corresponding GO biological process terms include **GO:0003341 (cilium movement)** and **GO:0001539 (cilium or flagellum-dependent cell motility)**.[7][13]  

Impaired mucociliary clearance leads to persistent mucus, chronic infection, and inflammation in the respiratory tract.[7][10][13] Inflammation, in turn, causes epithelial damage, goblet cell hyperplasia, and airway remodeling, contributing to bronchiectasis and progressive airflow limitation.[7][10] These processes involve GO terms such as **GO:0006954 (inflammatory response)** and **GO:0001525 (angiogenesis)**, reflecting tissue remodeling and vascular responses in chronically inflamed airways.[7][10]  

### 6.3 Left–Right Axis Determination and Laterality Defects

The laterality defects in CILD9 arise from dysfunctional **nodal cilia** during embryonic development. In the embryonic node, motile monocilia generate a leftward flow of signaling molecules that breaks bilateral symmetry and establishes the left–right axis of organ placement.[7][10][13] DNAI2 is expressed in nodal cilia, and its loss disrupts ODA assembly and ciliary motility, leading to randomization of fluid flow and hence randomization of organ laterality.[13]  

Loges et al. observed that of the six individuals with DNAI2 mutations, two exhibited situs solitus (normal organ positioning) and four exhibited situs inversus, indicating stochastic outcomes of left–right axis determination.[13] Malacards and Abcam reinforce this mechanism, stating that “half of the patients exhibit randomization of left-right body asymmetry and situs inversus, due to dysfunction of monocilia at the embryonic node,” and that primary ciliary dyskinesia associated with situs inversus is referred to as Kartagener syndrome.[1][15]  

The GO biological process term **GO:0001754 (establishment of left-right asymmetry)** is directly relevant to this mechanism, as is **GO:0060972 (left-right patterning of heart)** for specific organ involvement. CILD9 provides a clear example of how a motile ciliopathy can affect both respiratory defense and developmental patterning through a single molecular lesion.  

### 6.4 Sperm Flagella Dysfunction and Infertility

DNAI2’s expression in testis and localization in sperm flagella implicate it in **male fertility**. Abcam notes that DNAI2 is “highly expressed in trachea and testis,” and that reduced fertility is often observed in male patients due to abnormalities of sperm tails.[15] In LRRC56‑knockout mice, spermatozoa exhibit absent or severely reduced DNAI2 fluorescent signals along the flagellum, along with loss of inner dynein arm marker DNALI1, resulting in abnormal sperm structures and male sterility.[18] The authors conclude that LRRC56 deletion impairs assembly of both IDAs and ODAs, with downstream loss of DNAI2 contributing to sperm flagellar dysfunction.[18]  

In human CILD9 patients, Loges et al. reported infertility in one male, although sperm analysis was not available.[13] Given the shared dynein arm architecture between respiratory cilia and sperm flagella, it is highly plausible that DNAI2 loss leads to immotile or dyskinetic sperm, causing asthenozoospermia and infertility.[7][10][13][15] The corresponding GO terms include **GO:0007283 (spermatogenesis)** and **GO:0030317 (sperm motility)**, and the relevant cell ontology term is *CL:0000014 (sperm)*.  

### 6.5 Immune System and Tissue Damage Mechanisms

The **immune system** plays a secondary but important role in PCD pathophysiology. Impaired mucociliary clearance causes persistent colonization and infection, which elicit chronic neutrophilic inflammation, cytokine production, and oxidative stress in the airways.[7][10] Over time, this leads to tissue damage, including epithelial metaplasia, peribronchial fibrosis, and destruction of elastic tissue, culminating in bronchiectasis.[7][10]  

Although CILD9 literature does not detail immune cell types and cytokine profiles, general PCD studies show elevated neutrophils and inflammatory mediators in sputum, similar to cystic fibrosis but with distinct molecular etiology.[7][10] GO terms relevant to these processes include **GO:0006954 (inflammatory response)**, **GO:0006955 (immune response)**, and **GO:0006950 (response to stress)**. Tissue damage mechanisms encompass oxidative stress, protease‑mediated degradation of extracellular matrix, and fibrotic remodeling, consistent with **GO:0001503 (ossification)** and **GO:0042060 (wound healing)** in generalized remodeling contexts.[7][10]  

From an anatomical ontology perspective, affected organs and tissues include *UBERON:0002048 (lung)*, *UBERON:0001736 (trachea)*, *UBERON:0001737 (bronchus)*, and *UBERON:0001043 (nasal cavity)*, while cell types involved in airway inflammation and remodeling include *CL:0000098 (bronchial epithelial cell)* and *CL:0000775 (neutrophil)*.[7][10]  

### 6.6 Molecular Profiling and Advanced Technologies

To date, there are no published large‑scale **transcriptomic, proteomic, or metabolomic** profiling studies specifically focused on DNAI2‑mutant CILD9, but broader PCD research has employed such approaches to identify gene expression signatures and protein defects in ciliated cells.[7] For example, immunofluorescence staining using antibodies against DNAI2 and other dynein components has been used to diagnose PCD and characterize ultrastructural defects.[13][15] LifeSpan BioSciences and Abcam provide antibodies against DNAI2, enabling such proteomic assays in research and diagnostic settings.[12][15]  

Single‑cell and spatial transcriptomics technologies have not yet been reported for CILD9, but their application in airway epithelium from PCD patients could reveal altered differentiation states, ciliated cell abundance, and expression of ciliary and inflammatory genes.[7] Functional genomics screens (e.g., CRISPR, RNAi) could be applied to identify novel dynein arm assembly factors upstream of DNAI2, as suggested by LRRC56 knockout models.[18] For now, however, knowledge of CILD9 mechanisms relies primarily on targeted gene sequencing, immunofluorescence protein localization, and TEM ultrastructural analysis rather than unbiased multi‑omics approaches.[7][10][13][18][19]  

---

## 7. Anatomical Structures Affected

### 7.1 Organ‑Level Involvement

CILD9 primarily affects the **respiratory system**, with secondary involvement of the reproductive and cardiovascular systems. Orphanet’s definition of primary ciliary dyskinesia as a “primarily respiratory disorder” highlights the central role of the lungs, bronchi, nasal cavity, paranasal sinuses, and middle ear.[10] The main organs affected include the **lungs** (*UBERON:0002048*), where bronchiectasis and chronic infection develop; the **trachea** and **bronchi** (*UBERON:0001736*, *UBERON:0001737*), which harbor mucociliary dysfunction; the **nasal cavity and paranasal sinuses** (*UBERON:0001043*, *UBERON:0003681*), leading to chronic sinusitis; and the **middle ear** (*UBERON:0001756*), contributing to otitis media.[7][10][13]  

Laterality defects affect organs in the **cardiovascular and visceral systems**, including the heart, lungs, liver, stomach, and spleen. Situs inversus totalis involves mirror‑imaged positioning of these organs (e.g., right‑sided stomach, left‑sided liver), whereas heterotaxy can involve more complex arrangements.[10][11][13] Thus, anatomical involvement extends to *UBERON:0000948 (heart)*, *UBERON:0002108 (liver)*, *UBERON:0000945 (stomach)*, and *UBERON:0002106 (spleen)*.  

The reproductive system is affected in males through sperm flagellar defects, implicating the **testis** (*UBERON:0000473*) and **epididymis** (*UBERON:0001302*).[7][10][13][15] In LRRC56‑knockout mice and likely in CILD9 humans, sperm flagella exhibit dynein arm defects, leading to immotile sperm and infertility.[18][15]  

### 7.2 Tissue and Cell‑Level Involvement

At the tissue level, CILD9 primarily affects **ciliated epithelia**. Respiratory ciliated cells, including those lining the nasal passages, trachea, bronchi, and bronchioles, bear motile cilia whose dynein arms rely on DNAI2 for proper assembly.[7][10][13][15] The relevant tissue ontology terms include *UBERON:0006726 (respiratory epithelium)* and *UBERON:0002630 (ciliated epithelium)*.  

The key cell types involved are **multiciliated epithelial cells** in the airway and **monociliated nodal cells** in the embryonic node. Human Cell Atlas and Cell Ontology terms such as *CL:0000545 (ciliated epithelial cell)* and *CL:0000066 (embryonic structure cell)* approximate these populations. Sperm are also affected, corresponding to *CL:0000014 (sperm)*, as DNAI2 is expressed in sperm flagella and essential for their motility.[15][18]  

Supporting cell types in pathophysiology include **goblet cells**, which produce mucus; **neutrophils** and other immune cells, which mediate inflammation; and **fibroblasts**, which contribute to fibrotic remodeling of the airways.[7][10] Airway smooth muscle cells and endothelial cells may also be involved indirectly through airway narrowing and vascular responses.  

### 7.3 Subcellular Localization and Compartments

Subcellularly, DNAI2 and the CILD9 pathology localize to the **ciliary axoneme**, specifically the outer dynein arms. The axoneme is a microtubule‑based structure with a characteristic 9+2 arrangement in motile cilia, associated with dynein arms on the outer doublets.[13][19] The relevant GO cellular component terms include **GO:0005930 (axoneme)**, **GO:0036157 (outer dynein arm)**, and **GO:0097542 (motile cilium)**.  

Abcam describes DNAI2 as “located in the proximal region of respiratory cilia,” indicating regional specialization along the axoneme.[15] In DNAI2‑mutant cells, immunofluorescence reveals absence of DNAI2 and ODA heavy chains DNAH5 and DNAH9 from the axoneme but may show cytoplasmic aggregation of DNAI2 or mislocalized dynein components.[13][18] LRRC56‑knockout mice show DNAI2 aggregates in the cytoplasm rather than proper axonemal localization, reinforcing the importance of dynein arm assembly pathways.[18] Thus, CILD9’s subcellular pathology primarily involves the **ciliary axoneme**, with secondary mislocalization of dynein components to the cytoplasm.  

### 7.4 Localization and Lateralization Patterns

Localization patterns in CILD9 include **bilateral** involvement of the airway epithelium—both lungs and nasal passages are affected—and **systemic** involvement of ciliated tissues (airway, reproductive, and embryonic node).[7][10][13][15] Laterality defects introduce asymmetry at the organ level: approximately half of CILD9 patients exhibit **situs inversus totalis**, a mirror‑image arrangement of thoracic and abdominal organs.[11][13][15] Malacards and Abcam note that “half of the patients exhibit randomization of left-right body asymmetry and situs inversus,” consistent with nodal cilia dysfunction.[1][15]  

Clinically, this lateralization is evident on imaging studies such as chest radiographs and abdominal ultrasounds, which show reversed heart position (dextrocardia), inverted stomach and liver placement, and sometimes anomalies in lung lobation or spleen number.[10][11][13] Knowledge base annotations should therefore include **unilateral/bilateral involvement** fields for respiratory structures (bilateral) and **laterality defects** fields for visceral organs, using HPO terms such as *Situs inversus totalis* (HP:0001696).  

---

## 8. Temporal Development

### 8.1 Onset: Age and Pattern

CILD9, like other forms of PCD, has a **congenital onset**. Orphanet specifies that the age of onset for PCD is “neonatal,” reflecting the fact that many patients experience respiratory distress shortly after birth due to impaired clearance of lung fluid and secretions.[10] Despotes et al. emphasize that “neonatal respiratory distress” is a hallmark of PCD and often prompts early investigation.[7]  

The onset pattern is typically **chronic and insidious** rather than acute. Neonates may present with tachypnea, hypoxemia, and the need for supplemental oxygen, but the underlying ciliary defect persists and manifests as chronic rhinosinusitis, otitis media, and recurrent lower respiratory tract infections throughout childhood and adulthood.[7][10] In CILD9 families, Loges et al. report early‑life respiratory symptoms progressing to chronic lung disease, although precise ages of first symptom onset are not individually detailed.[13] The disease is therefore best characterized as **congenital, chronic, lifelong**, with an insidious yet relentless progression driven by recurrent infection and inflammation.  

### 8.2 Disease Progression and Course

The disease course of CILD9 is **progressive**, with cumulative damage to the airways leading to bronchiectasis and lung function decline over time. Orphanet notes that PCD lung disease evolves from recurrent infections to bronchiectasis and chronic respiratory insufficiency, particularly in patients diagnosed late or inadequately treated.[10] Despotes et al. underscore that early diagnosis and aggressive management can slow progression but that the disease remains lifelong.[7]  

Loges et al. described “chronic destructive airway disease” in DNAI2‑mutant patients, a phrase that encapsulates the progressive nature of bronchial wall damage and airway remodeling.[13] Over years or decades, this destructive process can result in advanced bronchiectasis with persistent productive cough, frequent exacerbations, and eventually respiratory failure requiring supplemental oxygen or, in extreme cases, lung transplantation.[7][10] The progression rate may be **variable**, influenced by environmental exposures, infection control, and adherence to airway clearance therapies.[7][10]  

From a temporal ontology perspective, the disease course can be divided into **early (neonatal and childhood)** stages featuring recurrent infections and otolaryngologic issues, **intermediate (adolescence)** stages with established bronchiectasis and emerging fertility issues, and **late (adulthood)** stages where lung function may significantly decline.[7][10][13] However, formal staging systems for PCD are not yet standardized, and knowledge bases should note that PCD course is chronic, progressive, and lifelong.  

### 8.3 Patterns of Remission and Critical Periods

Spontaneous **remission** of CILD9 is not expected, as the underlying DNAI2 defect persists throughout life. Symptom severity may fluctuate, with periods of relative stability interspersed with acute exacerbations, but the baseline ciliary dysfunction is constant.[7][10][13] Treatment‑induced improvements in symptoms and lung function can occur through aggressive airway clearance and infection control, but these represent **control** rather than cure.[7][10]  

Critical periods in disease development include the **neonatal period**, where respiratory distress and need for intensive care may arise; early childhood, when recurrent otitis media, sinusitis, and bronchitis can affect growth and quality of life; and adolescence and adulthood, when bronchiectasis becomes more prevalent and fertility issues emerge.[7][10][13] Early diagnosis during these periods offers opportunities for timely intervention and education, potentially improving long‑term outcomes.[7][10] For laterality defects, the critical window is **embryonic development**, when nodal cilia establish left–right asymmetry; interventions cannot alter this outcome, but prenatal diagnosis may inform obstetric and pediatric planning.[13][15]  

---

## 9. Inheritance and Population Characteristics

### 9.1 Inheritance Pattern and Genetic Features

CILD9 is inherited in an **autosomal recessive** manner. OMIM clearly states that “ciliary dyskinesia, primary, 9, with or without situs inversus” is autosomal recessive, with disease caused by homozygous mutation in DNAI2.[11] Malacards and Abcam similarly note autosomal recessive inheritance, and ClinGen’s gene–disease curation supports this classification.[1][11][15][17]  

In autosomal recessive inheritance, affected individuals are typically homozygous or compound heterozygous for pathogenic DNAI2 variants, while parents and unaffected siblings are heterozygous carriers.[11][13][17] Penetrance for biallelic loss‑of‑function DNAI2 variants appears to be **complete**, as all described homozygous individuals manifest classical PCD features, although the presence or absence of laterality defects may vary.[13] Expressivity is **variable**, with differences in severity of bronchiectasis, sinusitis, and fertility issues, reflecting both genetic background and environmental modifiers.[7][10][13]  

There is no evidence of **genetic anticipation** (increasing severity in successive generations) or **germline mosaicism** in CILD9 families.[11][13][17] Founder effects and population‑specific mutations have not yet been identified, but given the rarity of the disease, clustering in consanguineous families suggests that local founder alleles may exist.[13][17] Carrier frequency for DNAI2 pathogenic variants is extremely low in the general population, consistent with the rare incidence of PCD (approximately 1/15,000–1/30,000 live births) and the smaller fraction attributable to DNAI2 mutations.[10][13]  

### 9.2 Epidemiology: Prevalence and Incidence

Precise epidemiologic data for CILD9 are limited, but broader estimates for PCD are available. Orphanet estimates that primary ciliary dyskinesia has an incidence of approximately **1/15,000–1/30,000 live births**, noting that this is likely an underestimation due to diagnostic challenges and underrecognition.[10] Loges et al. cite an incidence of “1 in 20,000–30,000 people” for PCD, consistent with Orphanet’s figures.[13]  

Within this population, CILD9 appears to represent a **small fraction** of cases. In the cohort of 105 unrelated PCD families screened by Loges et al., DNAI2 mutations were detected in three families, accounting for roughly 3% of the cohort.[13] However, this estimate may vary across populations, and larger multi‑center studies are needed to refine the prevalence of DNAI2‑related disease among PCD patients.[7][10][13][17]  

Given the autosomal recessive inheritance and rarity of pathogenic DNAI2 variants, CILD9 is classified as a **rare disease** under most definitions (e.g., prevalence <1/2,000 in the European Union). MONDO and Orphanet both categorize primary ciliary dyskinesia as rare.[5][10]  

### 9.3 Population Demographics and Geographic Distribution

No specific **ethnic or geographic predilection** has been reported for CILD9. The families described by Loges et al. originate from different regions, suggesting that DNAI2 mutations occur sporadically in diverse populations.[13] General PCD registries include patients from Europe, North America, and other continents, and Orphanet notes that prevalence is difficult to determine but likely similar across populations when diagnostic access is accounted for.[10]  

Sex distribution in PCD is approximately **equal** (1:1 male:female) for respiratory manifestations, although male patients may experience more obvious fertility issues due to sperm flagellar involvement.[7][10] CILD9 families include both male and female affected individuals, consistent with autosomal inheritance.[13] Age distribution spans the entire lifespan, with many patients diagnosed in childhood but others identified in adulthood when chronic respiratory symptoms or fertility problems prompt investigation.[7][10][13]  

Geographic variation in specific DNAI2 variants has not been detailed, but future analyses of population databases may reveal regional founder alleles.[7][10][13][17] For now, CILD9 should be considered a globally distributed, rare autosomal recessive disease without strong ethnic bias.  

---

## 10. Diagnostics

### 10.1 Clinical and Functional Diagnostic Tests

Diagnosis of CILD9 follows the general **multi‑modal diagnostic pathway** for PCD, integrating clinical features, functional tests, ultrastructural analysis, and genetic testing. Despotes et al. emphasize that “diagnosis relies on a combination of tests for confirmation, including nasal nitric oxide (nNO) measurements, high-speed videomicroscopy analysis (HSVMA), immunofluorescent staining, axonemal ultrastructure analysis via transmission electron microscopy (TEM), and genetic testing,” and note that “there is no single gold standard confirmatory or exclusionary test.”[7]  

Clinically, evaluation begins with assessment of **neonatal respiratory distress**, chronic wet cough, nasal congestion, and recurrent otitis media and sinusitis.[7][10] Low nasal nitric oxide levels, measured using standardized devices, are a sensitive but not entirely specific biomarker of PCD; Orphanet notes that nasal nitric oxide levels tend to be low in PCD patients aged five years or more.[10] Pulmonary function tests reveal obstructive patterns and reduced forced expiratory volumes in advanced bronchiectasis.[7][10] Imaging studies, including chest radiographs and CT scans, identify bronchiectasis, bronchial wall thickening, and situs inversus when present.[7][10][13]  

High‑speed videomicroscopy analysis of nasal or bronchial brushings assesses **ciliary beat frequency and waveform**, distinguishing PCD from secondary ciliary dyskinesia due to infection.[7][10] In CILD9, HSVMA would show severely reduced or absent ciliary beating, consistent with ODA defects.[13][14] Transmission electron microscopy of ciliary axonemes reveals absence or marked reduction of ODAs, a hallmark ultrastructural lesion in DNAI2‑related PCD.[13][14] Orphanet lists TEM as a primary method for identifying specific ciliary ultrastructural defects in biopsy samples.[10]  

Immunofluorescent staining using antibodies against DNAI2, DNAH5, DNAI1, and other dynein components can provide **molecular confirmation** of ODA defects. Loges et al. used high‑resolution immunofluorescence imaging to show absence of DNAI2 and the heavy chains DNAH5 and DNAH9 in DNAI2‑mutant cilia.[13] Abcam and LifeSpan BioSciences supply antibodies against DNAI2, enabling such diagnostic or research assays.[12][15]  

### 10.2 Genetic Testing Approaches

Genetic testing is essential for definitive diagnosis of CILD9. Orphanet recommends **molecular genetic testing** to identify biallelic pathogenic variants in causative genes as part of PCD diagnosis.[10] For PCD in general, targeted gene panels, whole‑exome sequencing (WES), and whole‑genome sequencing (WGS) are used to identify mutations in the growing list of >50 PCD genes.[7][10]  

For DNAI2, Loges et al. sequenced all 14 exons and flanking intronic regions in affected individuals, identifying splice site and nonsense variants.[13] ClinGen’s curation highlights the role of DNAI2 gene sequencing in confirming PCD9.[17] While specific commercial tests for DNAI2 may not be as common as those for more prevalent PCD genes like DNAH5 and DNAI1, laboratories offering comprehensive PCD panels typically include DNAI2.[4][7][10][11] Orphanet notes diagnostic tests for DNAH5 and DNAI1 using Sanger sequencing and screening for common mutations, implying that similar strategies could be applied to DNAI2.[4]  

Whole‑exome sequencing has particular utility in CILD9 because DNAI2 is one of many possible genes underlying PCD. WES allows simultaneous analysis of all known PCD genes and can discover novel variants in DNAI2 or other genes.[7][10] Whole‑genome sequencing may capture non‑coding regulatory mutations and structural variants, but such findings have not yet been reported for DNAI2.[7][10][13][17] For knowledge base annotation, genetic testing modalities for CILD9 should include **single‑gene sequencing of DNAI2**, **multi‑gene PCD panels**, **whole‑exome sequencing**, and possibly **whole‑genome sequencing**, with note that chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat expansion assays are not relevant for this disease.[7][10][11][13]  

### 10.3 Omics‑Based Diagnostics and Biomarkers

Beyond targeted genetic testing, **omics‑based diagnostics** in PCD include transcriptomics, proteomics, and epigenomics, but these remain primarily research tools. Immunofluorescence staining of DNAI2 and other dynein arm components is a proteomic assay that can distinguish PCD subtypes; for example, absence of DNAI2 and DNAH5 in cilia suggests ODA defects related to DNAI2 or DNAH5 mutations.[13][15] Nasal nitric oxide measurement is a **biomarker** widely used in clinical settings, albeit not gene‑specific.[7][10]  

Liquid biopsy approaches (e.g., circulating cfDNA sequencing) have not been applied to CILD9 or PCD diagnosis. RNA sequencing of nasal epithelial cells from PCD patients could theoretically reveal reduced DNAI2 transcript levels or altered expression of dynein arm assembly factors, but such studies have not yet been reported.[7] Epigenomic profiling of DNAI2 locus in PCD has also not been described, and there is no evidence that epigenetic regulation is a major diagnostic concern for CILD9.[7][10][13]  

### 10.4 Clinical Criteria and Differential Diagnosis

There are no universally accepted **formal diagnostic criteria** for PCD, but society guidelines and expert reviews recommend a combination of clinical and laboratory findings.[7][10] Despotes et al. stress that diagnosis should be based on typical clinical features (neonatal respiratory distress, chronic wet cough, nasal congestion, recurrent otitis media), low nasal nitric oxide, characteristic ciliary ultrastructural defects, and identification of causative gene mutations.[7] Orphanet echoes this multi‑step approach.[10]  

Differential diagnosis includes other causes of neonatal respiratory distress and chronic respiratory symptoms, such as **cystic fibrosis**, primary immunodeficiencies, chronic aspiration, and asthma.[7][10] Cystic fibrosis is particularly important to distinguish, given overlapping features of bronchiectasis and chronic infection; sweat chloride testing and CFTR gene analysis are essential to rule out CF.[7][10] Immunodeficiencies can be excluded with immunoglobulin and lymphocyte subset testing. Structural airway anomalies and cardiac defects associated with laterality disorders may require echocardiography and imaging.[7][10]  

For CILD9, differential considerations also include other ODA‑defect PCD subtypes caused by DNAH5, DNAH9, DNAI1, and other genes. Distinguishing CILD9 from these subtypes relies primarily on genetic testing rather than phenotypic differences, as clinical features are largely overlapping.[3][6][7][8][10][11][13]  

### 10.5 Screening and Carrier Testing

Population‑based **screening** for CILD9 is not currently recommended, given its rarity. Newborn screening programs do not include PCD, although neonatal respiratory distress and laterality defects may prompt targeted evaluation.[7][10] Carrier screening for DNAI2 in the general population is likewise not practiced.  

However, **carrier testing and prenatal diagnosis** may be offered to families with known DNAI2 mutations, particularly in consanguineous populations. Genetic counseling should be provided to affected families, and Orphanet notes that PCD is usually inherited in an autosomal recessive manner and that genetic counseling is recommended.[10] Preimplantation genetic diagnosis and chorionic villus sampling can detect DNAI2 mutations in embryos or fetuses at risk, allowing informed reproductive choices.[7][10][11][13] For knowledge base purposes, screening fields should note that routine population screening is “not available,” while case‑specific carrier and prenatal testing are “available when familial variants are known.”  

---

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

Overall **survival** in PCD, including CILD9, is generally good, with many patients living into adulthood and old age. Orphanet does not provide specific mortality statistics but notes chronic disease and potential progression to respiratory insufficiency.[10] Despotes et al. discuss outcomes qualitatively, indicating that early diagnosis and appropriate management can maintain lung function and reduce complications.[7]  

For CILD9 specifically, no study has reported **life expectancy** or mortality rates, and the small number of described patients limits conclusions. However, given the similarity of CILD9 respiratory manifestations to other PCD subtypes, it is reasonable to infer that life expectancy is somewhat reduced in severe cases but can approach normal with optimal care.[7][10][13] Deaths directly attributable to PCD are uncommon but may occur due to respiratory failure, hemoptysis, or complications of lung transplantation.[7][10]  

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in CILD9 relates primarily to chronic respiratory disease, otolaryngologic problems, and fertility issues. Bronchiectasis causes persistent productive cough, dyspnea, and exercise limitation, and recurrent infections lead to frequent antibiotic use and hospitalizations.[7][10][13] Chronic sinusitis and otitis media contribute to headaches, hearing loss, and sleep disturbances.[7][10] Male infertility poses psychosocial and reproductive challenges.[7][10][13][15]  

Quality of life studies in PCD show impaired physical health, vitality, and social functioning compared to healthy controls, as measured by SF‑36 and other instruments.[7] Patients report burdens from daily airway clearance routines, medication regimens, and the psychological impact of chronic disease. Childhood morbidity includes school absenteeism and developmental delays related to hearing loss.[7][10] For CILD9, although no dedicated quality of life study exists, these general PCD findings are applicable.  

Long‑term disability outcomes may include chronic respiratory insufficiency, need for home oxygen or ventilation support, and limitations in occupational choices due to physical demands or exposure risks.[7][10] Lung transplantation may be considered in end‑stage cases but carries its own risks and long‑term complications.[7][10]  

### 11.3 Prognostic Factors and Biomarkers

Prognostic factors in CILD9 include **age at diagnosis**, **severity of bronchiectasis**, **infection control**, **adherence to airway clearance**, and **presence of laterality or cardiac defects**. Early diagnosis and aggressive management are associated with better outcomes, while delayed diagnosis allows more extensive airway damage to accumulate.[7][10] Chronic colonization with *Pseudomonas aeruginosa* and other pathogens is associated with faster lung function decline, mirroring cystic fibrosis.[7][10]  

Genotype–phenotype correlations in PCD suggest that certain gene defects (e.g., ODA genes like DNAH5 and DNAI2) may be associated with more severe disease than others (e.g., radial spoke head genes), but data are evolving.[7][10][11][13] Nasal nitric oxide levels, ciliary beat patterns, and TEM ultrastructural findings can serve as biomarkers of disease severity and guide management, but they are not formal prognostic markers.[7][10] No molecular biomarkers specific to DNAI2 have been validated for predicting prognosis, and this should be noted as a gap in knowledge.  

---

## 12. Treatment

### 12.1 Pharmacotherapy and Supportive Care

Treatment of CILD9 is primarily **supportive**, aimed at managing respiratory symptoms, preventing infections, and preserving lung function. Despotes et al. summarize PCD management strategies, including airway clearance techniques, inhaled medications, and antibiotics.[7] Orphanet likewise emphasizes treatment focused on respiratory care.[10]  

Pharmacologic treatments include **bronchodilators** (e.g., beta‑agonists, anticholinergics) to relieve airflow obstruction, **inhaled hypertonic saline** to enhance mucus clearance, and **inhaled corticosteroids** in selected patients with coexisting asthma or significant inflammation.[7][10] Antibiotics are used to treat acute exacerbations and may be administered prophylactically to reduce infection frequency.[7][10] Vaccinations against influenza, pneumococcus, and other respiratory pathogens are critical preventive measures.[7][10] These therapies correspond to NCIT terms such as *Antibiotic therapy* (NCIT:C321) and *Bronchodilator agent* (NCIT:C339).  

Airway clearance techniques, including chest physiotherapy, positive expiratory pressure devices, and oscillating vests, are cornerstone interventions.[7][10] While not pharmacologic, they are essential for moving mucus and preventing stasis. Nutritional support, treatment of chronic sinusitis (e.g., nasal saline irrigation, intranasal steroids), and management of otitis media (e.g., tympanostomy tubes) are also part of standard PCD care.[7][10]  

### 12.2 Advanced Therapeutics

Currently, there are **no approved gene therapies** or targeted molecular treatments specifically for CILD9 or PCD. Gene therapy approaches, such as viral vector‑mediated gene replacement or CRISPR‑based editing of DNAI2, remain theoretical at this stage.[7] The complexity of delivering corrected genes to widespread ciliated epithelia and ensuring long‑term expression pose major challenges.  

Cell therapy, including stem cell transplantation or airway epithelial regeneration, is under investigation in broader respiratory diseases but has not been applied to PCD in clinical trials.[7] RNA‑based therapies, such as antisense oligonucleotides or mRNA treatments, may theoretically correct specific splicing mutations like IVS11+1G>A in DNAI2, but no such interventions have been reported.[13][7]  

Immunotherapies and targeted therapies are not relevant for CILD9, given its non‑malignant, structural nature. Experimental treatments focus instead on optimizing airway clearance and exploring novel mucolytics or anti‑inflammatory agents.[7][10] ClinicalTrials.gov‑listed studies for PCD may include evaluations of airway clearance devices, inhaled hypertonic saline, and other supportive interventions, but none specifically target DNAI2.[7]  

### 12.3 Surgical and Interventional Procedures

Surgical interventions in CILD9 and PCD include **tympanostomy tube placement** for chronic otitis media and effusions, **functional endoscopic sinus surgery** for refractory chronic sinusitis, and in severe cases, **lung transplantation** for end‑stage respiratory failure.[7][10] These procedures carry risks but can substantially improve symptoms and quality of life when appropriately indicated.  

Cardiac surgery may be required in patients with heterotaxy and congenital heart defects, although these are not specifically documented in DNAI2‑mutant families.[13] Fertility interventions, including assisted reproductive techniques such as intracytoplasmic sperm injection (ICSI), may be necessary for male CILD9 patients with immotile sperm.[7][10][13][15] NCIT terms such as *Tympanostomy* (NCIT:C51622), *Sinus surgery* (NCIT:C34810), and *Lung transplantation* (NCIT:C15021) can be associated with these interventions.  

### 12.4 Treatment Outcomes and Strategies

Treatment outcomes in CILD9 depend on early diagnosis, adherence to airway clearance and infection control, and environmental modifiers. Despotes et al. emphasize that while PCD is incurable at present, appropriate management can stabilize lung function and reduce exacerbations.[7] Orphanet supports the view that respiratory care can improve quality of life and delay progression of bronchiectasis.[10]  

Side effects and adverse events of pharmacotherapy include antibiotic resistance, bronchial irritation from inhaled hypertonic saline, and systemic effects of corticosteroids when used long‑term.[7][10] Airway clearance techniques are generally safe but may be burdensome. Surgical interventions carry standard perioperative risks.  

Treatment strategies are individualized, often following clinical pathways that prioritize **airway clearance**, **infection control**, **management of upper airway disease**, and **fertility counseling**.[7][10] Personalized medicine approaches based on genotype are in their infancy; while knowledge of DNAI2 mutations confirms diagnosis and guides genetic counseling, it does not yet dictate specific therapeutic choices beyond general PCD management.[7][10][13]  

---

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of CILD9 is limited by its genetic etiology; **preventing disease occurrence** would require preventing transmission of pathogenic DNAI2 variants. This is theoretically possible through reproductive options such as preimplantation genetic diagnosis and selective implantation of unaffected embryos when familial mutations are known, but such interventions are individualized and not population‑wide.[7][10][11][13]  

Secondary prevention focuses on **early detection and treatment** to prevent or minimize complications. This includes heightened clinical suspicion for PCD in neonates with respiratory distress and unexplained situs inversus, timely diagnostic testing, and prompt initiation of airway clearance and infection control measures.[7][10] Awareness campaigns among neonatologists, pulmonologists, and otolaryngologists can improve early recognition.  

Tertiary prevention involves **preventing complications** in those with established disease. This encompasses rigorous infection control, vaccination, avoidance of tobacco smoke and pollutants, adherence to airway clearance regimens, and monitoring for bronchiectasis progression.[7][10] Genetic counseling for affected families helps prevent unanticipated recurrence and informs reproductive planning.[10][11]  

### 13.2 Immunization, Screening, and Counseling

Immunization is a key preventive strategy against respiratory infections in CILD9. Standard **childhood vaccines**, along with influenza and pneumococcal vaccines, reduce the burden of respiratory pathogens.[7][10] While not specific to PCD, such vaccinations are strongly recommended and should be annotated with NCIT terms such as *Vaccination* (NCIT:C17275).  

Screening for PCD or CILD9 at the population level is not currently practiced, but targeted **genetic screening** for DNAI2 mutations can be offered to at‑risk families, particularly in consanguineous populations or those with known pathogenic variants.[11][13][17] Preimplantation genetic diagnosis and prenatal testing (e.g., chorionic villus sampling) allow detection of DNAI2 mutations in embryos or fetuses, enabling informed reproductive decisions.[7][10][11][13]  

Genetic counseling is essential, providing **risk assessment and family planning guidance**. Orphanet stresses that PCD is usually inherited in an autosomal recessive manner and recommends genetic counseling for affected families.[10] Counselors explain recurrence risks (25% for each pregnancy when both parents are carriers), discuss carrier testing options for relatives, and outline prenatal and preimplantation testing options.[7][10][11][13][17]  

Public health interventions, such as improving air quality, reducing tobacco use, and promoting vaccination, indirectly benefit CILD9 patients by reducing infection and inflammation. Environmental interventions at the societal level, such as air pollution control, are particularly relevant to chronic respiratory diseases like PCD.[7][10]  

---

## 14. Other Species and Natural Disease

### 14.1 Species and Orthologous Genes

Motile cilia and dynein arm components are evolutionarily conserved across many species, allowing comparative studies of DNAI2 function. DNAI2 orthologs exist in **green algae (*Chlamydomonas reinhardtii*)**, **fish (e.g., medaka *Oryzias latipes*)**, and **mammals (e.g., mice)**.[13][19] In *Chlamydomonas*, the ortholog is IC69/IC2, and flagellar mutants carrying defects in this gene exhibit immotile or dyskinetic flagella, paralleling human DNAI2‑related ciliary dysfunction.[13][19] Kobayashi et al. characterized the medaka **jaodori** mutant, which harbors defects in dnai2, and described “redundant and distinct roles of dynein axonemal intermediate chain 2 (dnai2) in motile cilia,” demonstrating conserved functions in vertebrates.[19]  

These orthologs can be annotated in NCBI Gene and comparative genomics resources, with DNAI2 orthologous relationships supporting the use of model organisms to study human CILD9 mechanisms.[13][18][19]  

### 14.2 Natural Disease in Animals and Comparative Pathology

Natural occurrences of PCD or DNAI2‑related ciliopathies in companion animals (e.g., dogs, cats) have been described for other genes but are not detailed for DNAI2 in the available literature.[7][10] OMIA (Online Mendelian Inheritance in Animals) catalogs animal genetic diseases but is not cited in the current search results for DNAI2. Nevertheless, comparative pathology suggests that motile ciliopathies may manifest as chronic respiratory disease and laterality defects in animals, similar to humans.[7][10][18][19]  

LRRC56‑knockout mice represent an induced rather than natural model, but their phenotype—hydrocephalus, situs inversus, male infertility, bronchiectasis—closely matches human PCD.[18] Kobayashi’s medaka jaodori mutant is another induced model, illustrating natural disease manifestations in fish when dnai2 is defective.[19] Comparative biology underscores that dynein arm assembly and ciliary motility are deeply conserved processes, and that DNAI2 loss leads to similar phenotypes across diverse taxa.  

### 14.3 Transmission and Zoonotic Potential

CILD9 is a **non‑infectious, non‑zoonotic** genetic disease. There is no transmission between humans or across species beyond Mendelian inheritance. Thus, zoonotic potential and cross‑species transmission are not relevant concepts for this disease.  

---

## 15. Model Organisms

### 15.1 Medaka (Oryzias latipes) dnai2 Mutant (jaodori)

Medaka fish provide a powerful model for studying DNAI2 function in motile cilia. Kobayashi et al. characterized the **jaodori** mutant, which carries defects in the medaka ortholog of DNAI2 (dnai2), and studied “redundant and distinct roles of dynein axonemal intermediate chain 2 (dnai2) in motile cilia.”[19] The mutant exhibits phenotypes closely resembling human PCD, including abnormal ciliary motility and laterality defects, demonstrating the conserved role of DNAI2 across vertebrates.[19]  

The jaodori model allows detailed analysis of ciliary beat patterns, axonemal ultrastructure, and developmental processes in a transparent, genetically tractable organism. It recapitulates key features of human CILD9—motile cilia dysfunction and randomization of left–right asymmetry—making it valuable for mechanistic studies.[19] Limitations include differences in respiratory anatomy and environmental exposures compared to humans, but the core ciliary motility mechanisms are conserved.  

### 15.2 LRRC56‑Knockout Mice and DNAI2 Mislocalization

LRRC56‑knockout mice represent another critical model relevant to DNAI2‑related PCD. In a recent study, researchers generated LRRC56‑knockout mice and found that “the absence of DNALI1 and DNAI2 signaling in knockout mouse cilia supports the critical role of the LRRC56 gene in dynein arm assembly.”[18] The mice displayed prominent phenotypes, including hydrocephalus, situs inversus, male infertility, and bronchiectasis.[18]  

Transmission electron microscopy revealed defects in inner and outer dynein arms and disorganized axonemal structure in flagella, while immunofluorescence showed dramatically attenuated signals of DNALI1 and DNAI2 in tracheal cilia.[18] The authors concluded that LRRC56 deletion impairs the assembly of both inner and outer dynein arms, including DNAI2, thereby affecting motile cilia function and causing PCD‑like disease.[18]  

Although LRRC56‑knockout mice do not harbor DNAI2 mutations per se, they model upstream defects in dynein arm assembly that result in DNAI2 mislocalization, providing insights into how DNAI2 integration into the axoneme depends on assembly factors. The phenotype recapitulates human PCD features, including respiratory disease, laterality defects, and infertility, and thus offers a robust model for studying dynein arm assembly pathways applicable to CILD9.[18]  

### 15.3 Other Model Systems and Applications

Beyond medaka and LRRC56‑knockout mice, **cellular models** derived from human CILD9 patients are invaluable. Nasal or bronchial epithelial cells obtained via brushings or biopsies can be cultured and analyzed using high‑speed videomicroscopy, TEM, and immunofluorescence staining to study ciliary motility and dynein arm assembly.[7][13] Loges et al. used such patient‑derived cells to demonstrate DNAI2 absence and ODA defects.[13] These in vitro models enable mechanistic studies and high‑content screening of potential therapies, such as small molecules that might enhance ciliary beating or compensate for structural defects.  

Chlamydomonas flagellar mutants with defects in IC69/IC2 provide additional mechanistic insight. OMIM notes that “Chlamydomonas flagellar mutants carrying a defect in IC78, a gene of relatively small size,” and related intermediate chain genes have been used to understand dynein arm function.[3][13][19] These unicellular models allow high‑resolution structural, biochemical, and genetic analysis of dynein arms.  

Applications of these models include elucidating the assembly and maintenance of dynein arms, identifying new dynein arm components and assembly factors, testing gene therapy vectors or RNA‑based interventions in ciliated cells, and screening for compounds that modify ciliary beating.[7][13][18][19] Limitations include species differences, lack of human‑specific environmental exposures, and difficulty translating findings into systemic therapies for humans. Nonetheless, model organisms and cellular systems are central to ongoing research in CILD9 and PCD.  

---

## Conclusion

Primary ciliary dyskinesia 9 (CILD9) represents a well‑defined, gene‑specific subset of primary ciliary dyskinesia, characterized by biallelic loss‑of‑function mutations in **DNAI2**, an axonemal dynein intermediate chain essential for outer dynein arm assembly in motile cilia and sperm flagella.[11][13][15][19] Clinically, CILD9 manifests as a congenital, autosomal recessive motile ciliopathy with neonatal respiratory distress, chronic upper and lower respiratory tract infections, progressive bronchiectasis, frequent laterality defects (situs inversus or heterotaxy), and male infertility due to sperm tail abnormalities.[7][10][11][13][15] The disease fits within the broader PCD framework defined by MONDO:0016575 and Orphanet ORPHA:244, but is distinguished by its specific DNAI2 etiology and characteristic ultrastructural ODA defect.[5][10][11][13][14]  

Mechanistically, DNAI2 loss leads to absent or severely reduced ODAs along the ciliary axoneme, resulting in immotile or dyskinetic cilia, impaired mucociliary clearance, and randomization of left–right body asymmetry due to nodal cilia dysfunction.[13][14][19] Model organisms, including medaka dnai2 mutants and LRRC56‑knockout mice with DNAI2 mislocalization, underscore the conserved role of DNAI2 in dynein arm assembly and motile cilia function across species.[18][19] At the cellular level, CILD9 involves multiciliated respiratory epithelial cells, monociliated nodal cells, and sperm, with pathophysiology extending from subcellular dynein arm defects to organism‑level respiratory, developmental, and reproductive phenotypes.[7][10][13][15][18][19]  

Diagnostic evaluation of CILD9 relies on a combination of clinical assessment, low nasal nitric oxide measurements, high‑speed videomicroscopy of ciliary beating, TEM ultrastructural analysis revealing ODA defects, immunofluorescence staining for DNAI2 and related dynein components, and genetic testing to identify biallelic DNAI2 mutations.[7][10][11][13][15][17] There is no single gold standard test, but integrated diagnostics can achieve high specificity and sensitivity.[7][10] Treatment remains supportive, focusing on airway clearance, infection control, management of upper airway disease, and fertility counseling, with no current gene‑specific therapies for DNAI2 defects.[7][10][13] Prognosis depends on early diagnosis, adherence to management, and infection control; while life expectancy can be near normal in well‑managed cases, chronic morbidity and quality of life impairments are common.[7][10][13]  

For disease knowledge bases, CILD9 should be annotated with key identifiers (OMIM 612444, causal gene DNAI2), inheritance (autosomal recessive), ontologies (MONDO:0016575 parent term; HPO phenotypes including HP:0005938, HP:0002110, HP:0001696, HP:0003251; GO processes such as GO:0003341 and GO:0001754; CL cell types including ciliated epithelial cells and sperm; UBERON anatomical structures including lung, trachea, nasal cavity, heart, testis), and NCIT clinical‑intervention terms for treatments.[5][7][10][11][13][15][18][19] Evidence items should reference primary literature, notably Loges et al. (Am J Hum Genet 2008; PMID 18950741), Despotes et al. (Cells 2024; PMID 38891105), Kobayashi et al. (Developmental Biology 2010; dnai2 in medaka), and the LRRC56‑knockout mouse study, with direct abstract quotes supporting pathophysiological and clinical claims.[7][13][18][19]  

Significant knowledge gaps remain, including precise epidemiologic data for CILD9, detailed genotype–phenotype correlations within DNAI2 variants, and the absence of targeted molecular therapies. Future research integrating multi‑omics profiling, advanced imaging, and functional genomics in DNAI2‑mutant human cells and animal models will be essential to refine our understanding of dynein arm assembly, identify potential therapeutic targets, and improve outcomes for individuals with CILD9 and related motile ciliopathies.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 49 |
| Terms named correctly | 21 |
| Terms named as a **different** term | 20 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0005938` (3 mentions) - the report calls it "Primary ciliary dyskinesia"; HP calls it **Abnormal respiratory motile cilium morphology**
- `HP:0011107` (1 mention) - the report calls it "Chronic cough"; HP calls it **Recurrent aphthous stomatitis**
- `HP:0031453` (1 mention) - the report calls it "Heterotaxy"; HP calls it **Oral lichenoid lesion**
- `HP:0001548` (1 mention) - the report calls it "Asthenozoospermia"; HP calls it **Overgrowth**
- `NCIT:C85756` (1 mention) - the report calls it "Smoking behavior"; NCIT calls it **Nanomole per Milliliter**
- `NCIT:C16451` (1 mention) - the report calls it "Physical activity"; NCIT calls it **Colposcopy**
- `GO:0001754` (2 mentions) - the report calls it "establishment of left-right asymmetry"; GO calls it **eye photoreceptor cell differentiation**
- `CL:0000014` (2 mentions) - the report calls it "sperm"; CL calls it **germ line stem cell**
- `UBERON:0001736` (2 mentions) - the report calls it "trachea"; UBERON calls it **submandibular gland**
- `UBERON:0001737` (2 mentions) - the report calls it "bronchus"; UBERON calls it **larynx**
- `UBERON:0001043` (2 mentions) - the report calls it "nasal cavity"; UBERON calls it **esophagus**
- `UBERON:0002108` (1 mention) - the report calls it "liver"; UBERON calls it **small intestine**
- `UBERON:0006726` (1 mention) - the report calls it "respiratory epithelium"; UBERON calls it **outer canthus**
- `UBERON:0002630` (1 mention) - the report calls it "ciliated epithelium"; UBERON calls it **body of caudate nucleus**
- `CL:0000066` (1 mention) - the report calls it "embryonic structure cell"; CL calls it **epithelial cell**
- `NCIT:C321` (1 mention) - the report calls it "Antibiotic therapy"; NCIT calls it **Busulfan**
- `NCIT:C339` (1 mention) - the report calls it "Bronchodilator agent"; NCIT calls it **Capsaicin**
- `NCIT:C51622` (1 mention) - the report calls it "Tympanostomy"; NCIT calls it **Amputation of Toe**
- `NCIT:C34810` (1 mention) - the report calls it "Sinus surgery"; NCIT calls it **Megacolon**
- `NCIT:C15021` (1 mention) - the report calls it "Lung transplantation"; NCIT calls it **XLII Mouse**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0031148` (1 mention), reported as "Productive cough" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C85756` (Nanomole per Milliliter) (1 mention)
- `NCIT:C15021` (XLII Mouse) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0006510` (2 mentions) - the report calls it "Chronic sinusitis"; HP calls it **Chronic pulmonary obstruction**
- `HP:0000403` (2 mentions) - the report calls it "Otitis media", "Recurrent otitis media"; HP calls it **Recurrent otitis media**, and lists "Frequent otitis media" among its other names
- `GO:0060972` (1 mention) - the report calls it "left-right patterning of heart"; GO calls it **left/right pattern formation**
- `GO:0030317` (1 mention) - the report calls it "sperm motility"; GO calls it **flagellated sperm motility**, and lists "sperm motility" among its other names
- `CL:0000098` (1 mention) - the report calls it "bronchial epithelial cell"; CL calls it **sensory epithelial cell**, and lists "neuroepithelial cell" among its other names
- `CL:0000545` (1 mention) - the report calls it "ciliated epithelial cell"; CL calls it **T-helper 1 cell**
- `GO:0097542` (1 mention) - the report calls it "motile cilium"; GO calls it **ciliary tip**, and lists "cilium tip" among its other names
- `NCIT:C17275` (1 mention) - the report calls it "Vaccination"; NCIT calls it **Calcineurin**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000403` - called "Otitis media", "Recurrent otitis media"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.