---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-28T20:16:22.012027'
end_time: '2026-08-28T20:33:16.606721'
duration_seconds: 1014.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 11A (Zellweger)
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 9
  num_turns: 50
  total_cost_usd: 5.046248500000002
  session_id: 4eb6a956-666d-4e4b-b731-bd377292ca66
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 52
reference_validation:
  total_references: 49
  verified: 49
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 49
  on_topic: 32
  validator_version: 0.2.1
term_validation:
  total_terms: 106
  verified: 99
  not_found: 0
  obsolete: 1
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 70
  labels_matching: 46
  labels_mismatched: 17
  mislabelled_terms:
  - term_id: MONDO:0013949
    reported_labels:
    - MONDO
    ontology_label: peroxisome biogenesis disorder 11A (Zellweger)
  - term_id: DOID:0080485
    reported_labels:
    - DOID
    ontology_label: peroxisome biogenesis disorder 11A
  - term_id: HP:0002104
    reported_labels:
    - Apnea
    - a proximate cause of neonatal death
    ontology_label: Apnea
  - term_id: HP:0002421
    reported_labels:
    - verify
    ontology_label: Poor head control
  - term_id: HP:0000934
    reported_labels:
    - verify
    ontology_label: Chondrocalcinosis
  - term_id: HP:0002269
    reported_labels:
    - verify
    ontology_label: Abnormality of neuronal migration
  - term_id: HP:0034512
    reported_labels:
    - verify
    ontology_label: Transitional-cell carcinoma of the ureter
  - term_id: GO:0018882
    reported_labels:
    - verify
    ontology_label: obsolete (+)-camphor metabolic process
  - term_id: UBERON:0001474
    reported_labels:
    - Skeleton
    ontology_label: bone element
  - term_id: UBERON:0010363
    reported_labels:
    - verify
    ontology_label: endochondral element
  - term_id: UBERON:0001091
    reported_labels:
    - verify
    ontology_label: calcareous tooth
  - term_id: CL:0000120
    reported_labels:
    - verify
    ontology_label: granule cell
  - term_id: CL:0000850
    reported_labels:
    - verify
    ontology_label: serotonergic neuron
  - term_id: CL:0000210
    reported_labels:
    - verify
    ontology_label: photoreceptor cell
  - term_id: NCIT:C15329
    reported_labels:
    - ZSD cataracts; early surgery where feasible
    ontology_label: Surgical Procedure
  - term_id: NCIT:C15747
    reported_labels:
    - Enamel hypoplasia in *"nearly all patients
    ontology_label: Supportive Care
  - term_id: NCBITaxon:4903
    reported_labels:
    - verify
    ontology_label: Williopsis jadinii
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0018882
    ontology_label: obsolete (+)-camphor metabolic process
  unresolvable_prefixes:
  - NC_000002.12
  - ORPHA
  - OMIM
  - LOINC
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 11A (Zellweger)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 11A (Zellweger)** covering all of the
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

# Research Report: Peroxisome Biogenesis Disorder 11A (Zellweger) — PBD11A / PEX13-Related Zellweger Syndrome

**Prepared:** 2026-08-28 · **Target:** `kb/disorders/Peroxisome_Biogenesis_Disorder_11A_Zellweger.yaml` · **MONDO:0013949**

> **Scope caveat, stated up front.** PBD11A is an ultra-rare disorder. Fewer than ~25 PEX13-mutant individuals across the *entire* Zellweger spectrum had been reported worldwide as of 2024 (Su et al. 2024, PMID:37962062: *"PEX13 gene variants are rare causes of ZSDs, with only 21 cases reported worldwide and none in China."*). Almost every quantitative claim below (prevalence, frequency, survival, treatment response, QoL) derives from **Zellweger spectrum disorder (ZSD) as a whole**, not from PEX13-specific cohorts, and is labelled as such. PEX13-specific evidence is limited to ~9 published pedigrees plus ClinVar submissions. Where I could not verify something, I say so rather than interpolating.
>
> **Ontology CURIEs below are leads, not bindings.** Only the HPO set in §3 was retrieved from an authoritative annotation source. Every other suggested CURIE must be run through `just validate-terms` before it enters YAML, per the repo's ontology term contract.

---

## 1. Disease Information

### Overview

Peroxisome biogenesis disorder 11A (Zellweger) is the **severe, neonatal-lethal end of the PEX13-deficient Zellweger spectrum**. PEX13 encodes an integral peroxisomal membrane protein whose cytosolically exposed SH3 domain, together with PEX14, constitutes the **docking module** at which cargo-loaded PEX5 (PTS1 receptor) and PEX7 (PTS2 receptor) arrive at the peroxisomal membrane. Biallelic loss of PEX13 function collapses peroxisomal matrix-protein import; the membrane remnant persists as an empty "peroxisomal ghost," and every peroxisomal matrix enzyme activity — very-long-chain fatty acid (VLCFA) β-oxidation, plasmalogen synthesis, phytanic acid α-oxidation, bile-acid side-chain oxidation, glyoxylate detoxification — fails simultaneously.

Clinically this produces the classical Zellweger phenotype: profound neonatal hypotonia, seizures, inability to feed, characteristic craniofacial dysmorphism, neuronal migration defects (polymicrogyria/pachygyria), hepatic dysfunction, renal cortical cysts, and chondrodysplasia punctata, with death typically in the first year of life.

**Nosological note on the numbering.** The OMIM series number ("11A") and the historical complementation-group number ("CG13" in the US series / "group H" in the Japanese series) do **not** match, and this is a recurring source of curation error. PEX13 is peroxin *13*; PBD complementation group *13*; OMIM PBD series *11*. All three refer to the same gene.

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0013949` | peroxisome biogenesis disorder 11A (Zellweger) |
| **OMIM** | `#614883` | PEROXISOME BIOGENESIS DISORDER 11A (ZELLWEGER); PBD11A |
| **OMIM (gene)** | `*601789` | PEROXISOME BIOGENESIS FACTOR 13; PEX13 |
| **DOID** | `DOID:0080485` | |
| **UMLS** | `C3554000` | |
| **MedGen** | `766914` | |
| **GARD** | `0015874` | |
| **HGNC** | `hgnc:8855` | PEX13 (lowercase prefix is canonical in this repo) |
| **NCBI Gene** | `5194` | 2p15, NC_000002.12:61,017,719–61,051,989 |
| **UniProt** | `Q92968` | Peroxisomal membrane protein PEX13 / Peroxin-13, 403 aa |
| **RefSeq transcript** | `NM_002618.4` | canonical for HGVS in ClinVar |

**Allied/parent identifiers (not exact matches — do NOT bind as `exactMatch`):**

| Resource | ID | Concept | Suggested predicate |
|---|---|---|---|
| Orphanet | `ORPHA:912` | Zellweger syndrome | `skos:broadMatch` |
| Orphanet | `ORPHA:79189` | Peroxisome biogenesis disorder (ZSD group) | `skos:broadMatch` |
| ICD-10-CM | `E71.510` | Zellweger syndrome | `skos:broadMatch` |
| ICD-11 | `5C57.0` | Zellweger syndrome | `skos:broadMatch` |
| MeSH | `D015211` | Zellweger Syndrome | `skos:broadMatch` |
| MONDO | `MONDO:0013951` (verify) | peroxisome biogenesis disorder 11B | sibling; PEX13, milder end |

*The MONDO record for `MONDO:0013949` carries **no** Orphanet or MeSH xref — Orphanet does not split ZS by PEX gene. Do not manufacture one.*

### Synonyms and alternative names

- PBD11A
- Peroxisome biogenesis disorder, complementation group 13 (CG13)
- Peroxisome biogenesis disorder, complementation group H (Japanese series designation)
- PEX13-related Zellweger syndrome
- Cerebrohepatorenal syndrome, PEX13 type (historical; "cerebrohepatorenal syndrome of Zellweger" is the pre-molecular name)
- Zellweger syndrome, PEX13-deficient

### Provenance of the information

**Aggregated disease-level**, not patient-level. There is no EHR-derived cohort for PBD11A — the population is far too small. Sources are: (a) individual case reports and small pedigree series with functional follow-up; (b) ZSD-wide natural-history registries (`NCT01668186`, n=244) and caregiver surveys (`NCT03440905`, n=92; Bose et al. 2020, PMID:33335840); (c) ClinVar/gnomAD variant aggregation; (d) mouse and zebrafish `Pex13` models, which are unusually informative here because a full and a brain-restricted mouse knockout both exist.

---

## 2. Etiology

### 2.1 Disease causal factors

**Monogenic, autosomal recessive, fully penetrant.** The sole cause is biallelic loss-of-function of **PEX13** (2p15). There is no environmental, infectious, or multifactorial contribution to *causation*. The disease is a pure inborn error of organelle biogenesis.

The causal chain is unusually short and well established:

```
biallelic PEX13 LoF
  → loss/destabilization of the PEX13–PEX14 docking complex
  → failure of PEX5 (PTS1) and PEX7 (PTS2) cargo delivery
  → collapse of peroxisomal matrix protein import ("peroxisomal ghosts")
  → simultaneous failure of ALL peroxisomal matrix enzyme functions
  → VLCFA accumulation + plasmalogen deficiency + bile-acid intermediate accumulation
    + phytanic/pristanic accumulation + hyperoxaluria + pipecolic acidemia
  → multiorgan disease
```

> **Liu et al. 1999, Am J Hum Genet 65(3):621-34, PMID:10441568 —** *"PEX13 encodes a peroxisomal membrane protein with a cytoplasmically exposed SH3 domain, and we find that expression of human PEX13 restores peroxisomal matrix-protein import in cells from patient PBD222. … Taken together, these results provide strong evidence that mutations in PEX13 are responsible for disease in patient PBD222 and, by extension, in complementation group 13 of the PBDs."*

> **Shimozawa et al. 1999, Hum Mol Genet 8(6):1077-83, PMID:10332040 —** *"A severe phenotype of a ZS patient (H-02) was homozygous for a nonsense mutation, W234ter, which results in the loss of not only the SH3 domain but also the putative transmembrane domain of Pex13p."*

### 2.2 Risk factors

**Genetic (causal, not "risk"):**
- Two pathogenic PEX13 alleles. See §4 for the variant catalogue.
- **Consanguinity is the dominant genetic risk context.** Of the reported PEX13 pedigrees, a striking proportion are consanguineous: Su 2024 (Chinese, consanguineous, homozygous c.493G>C); Dong 2024 (Chinese, consanguineous, same allele); Al-Dirbashi 2009 (Saudi, homozygous 147-kb deletion and homozygous 14-bp deletion in two families); Borgia 2022 families D and E (both Iranian, both homozygous). Suggested HPO/context: HP:0000007 autosomal recessive inheritance.
- **Founder/recurrent alleles.** `c.880C>T; p.Arg294Trp` recurred in **three of five** families in Borgia et al. 2022 (Italian, Pakistani-Canadian, Iraqi) — the strongest candidate for a recurrent PEX13 allele, though a founder haplotype was not formally demonstrated across those three ancestries. `c.493G>C; p.Ala165Pro` has now been reported twice, both in China (Su 2024; Dong 2024) — a possible Chinese founder allele.

**Environmental:** **None known.** No toxin, exposure, maternal factor, infection, or lifestyle variable has been shown to cause or modify PBD11A onset. Advanced parental age is not implicated (this is not a de novo–driven disease). Sex is not a risk factor (autosomal).

*One important negative to curate explicitly:* the severe end of the Zellweger spectrum has **no known environmental trigger**, unlike, e.g., the milder ZSD phenotypes where dietary phytanic acid load modulates a downstream metabolite (see §5).

### 2.3 Protective factors

- **Genetic:** No protective allele or modifier is documented in humans. The only mechanistically "protective" genotype class is **residual-function alleles** — a hypomorphic missense that preserves partial import shifts the phenotype toward PBD11B rather than PBD11A. The paradigm is `p.Ile326Thr`, a *temperature-sensitive* SH3 allele: > *"This mutant PEX13 cDNA expression in a PEX13-defective CHO mutant showed I326T to be a TS mutation and thus suggested that Pex13p with the I326T mutation in the SH3 domain is stable at 30 degrees C but is somewhat unstable at 37 degrees C."* (PMID:10332040)
  This is not "protection" in the epidemiological sense; it is allelic dosage. It matters clinically because temperature-sensitive alleles are the subgroup in whom peroxisome-biogenesis–stimulating compounds are expected to work (Klouwer 2015, PMID:26627182: greatest benefit expected *"in patients whose fibroblasts showed temperature sensitivity"*).
- **Environmental/dietary:** None established as protective. DHA supplementation was hypothesized to be protective and **failed** in a randomized trial (§12).

### 2.4 Gene–environment interactions

Essentially absent for PBD11A. The one genuine G×E axis across ZSD is **dietary phytanic acid** (dairy, ruminant fat, fish): patients cannot α-oxidize it, so intake maps directly onto plasma phytanate. But Klouwer et al. 2015 explicitly caution that restriction is warranted only when *"levels are extremely high"*, because *"sufficient intake of calories is more decisive"* — in the severe neonatal phenotype, caloric adequacy dominates. Curate this as a treatment/dietary consideration, not as a disease-modifying gene–environment interaction.

A second, weaker axis: **oxidative stress load**. Pex13-deficient cells show elevated mitochondrial superoxide, and antioxidant treatment rescued the phenotype *in vitro* (PMID:27514574) — implying, but not demonstrating, that pro-oxidant environmental exposures could aggravate. **No human data.** Curate as `KNOWLEDGE_GAP`, not as an environmental factor.

---

## 3. Phenotypes

### 3.1 Authoritative HPO annotation set for OMIM:614883

Retrieved from the HPO annotation API (`ontology.jax.org/api/network/annotation/OMIM:614883`). **21 terms, no frequency or onset metadata attached** — this is the complete curated set for PBD11A specifically, and its thinness reflects the tiny case count.

| HP ID | Term | Suggested `category` |
|---|---|---|
| HP:0006829 | Severe muscular hypotonia | Neurologic |
| HP:0008947 | Floppy infant | Neurologic |
| HP:0001250 | Seizure | Neurologic |
| HP:0001263 | Global developmental delay | Neurodevelopmental |
| HP:0001339 | Lissencephaly | Neurologic / Structural brain |
| HP:0002126 | Polymicrogyria | Neurologic / Structural brain |
| HP:0003429 | CNS hypomyelination | Neurologic / White matter |
| HP:0002104 | Apnea | Respiratory |
| HP:0002910 | Elevated circulating hepatic transaminase concentration | Laboratory / Hepatic |
| HP:0001410 | Decreased liver function | Hepatic |
| HP:0000107 | Renal cyst | Renal |
| HP:0005562 | Multiple renal cysts | Renal |
| HP:0001508 | Failure to thrive | Growth |
| HP:0000260 | Wide anterior fontanel | Craniofacial |
| HP:0000239 | Large fontanelles | Craniofacial |
| HP:0000348 | High forehead | Craniofacial |
| HP:0000325 | Triangular face | Craniofacial |
| HP:0100729 | Large face | Craniofacial |
| HP:0000463 | Anteverted nares | Craniofacial |
| HP:0005280 | Depressed nasal bridge | Craniofacial |
| HP:0000007 | Autosomal recessive inheritance | (inheritance, not phenotype) |

### 3.2 Additional ZSD-severe-end phenotypes documented in PEX13 patients specifically

These come from the published PEX13 pedigrees and should be curated with the PEX13 citation attached, not the generic ZSD one.

| Phenotype | Suggested HP term | PEX13 evidence |
|---|---|---|
| Neonatal seizures (onset within hours) | HP:0032807 (Neonatal seizure — **verify**) | Borgia 2022 family D: seizures within hours of birth; *"myoclonic and tonic seizures"*, EEG *"multifocal sharp waves"* |
| Cortical malformation, parietal | HP:0002126 / HP:0002536 (verify) | Borgia 2022 family D: *"bilateral malformation of cortical development in parietal lobes, with a polymicrogyria-like appearance"* |
| Head lag / axial hypotonia | HP:0002421 (verify) | Borgia 2022 family D: *"severely hypotonic with head lag"* |
| Hepatic dysfunction / cholestasis | HP:0001392, HP:0001396 | Su 2024: *"severe hypotonia, seizures, hepatic dysfunction, failure to thrive, and dysmorphic features"* |
| Sensorineural hearing impairment | HP:0000407 | Borgia 2022 families A, C, E |
| Progressive visual failure / retinopathy | HP:0000505, HP:0000510 | Borgia 2022 family A (severe myopia, decreasing acuity); family E (*"cherry-red spot of the macula"*, *"visual fixation and gaze impairment"*) |
| Spastic tetraparesis | HP:0002510 | Borgia 2022 families A, C — **milder (PBD11B-range) individuals** |
| Cerebellar atrophy / vermian hypoplasia | HP:0001272, HP:0002335 (verify) | Borgia 2022 family B: *"extensive cerebellar atrophy and pontine/vermian hypoplasia"* |
| Diffuse hypomyelination | HP:0007younger — use **HP:0003429** | Borgia 2022 family B: *"diffuse hypomyelination"* |
| Feeding difficulties | HP:0011968 | Borgia 2022 family B |
| Chondrodysplasia punctata | HP:0000934 (verify) | OMIM PBD11A clinical description; classical ZS feature |
| Neuronal migration defect | HP:0002269 (verify) | Maxwell 2003 mouse: *"disordered lamination in the cerebral cortex, consistent with a neuronal migration defect"* |
| Elevated VLCFA | HP:0034512 (verify) | Su 2024: *"elevated levels of very long-chain fatty acids (VLCFA), phytanic acid, and pipecolic acid"* |

### 3.3 Phenotype characteristics

**Age of onset.** For PBD11A specifically: **congenital to neonatal.** Borgia family D had seizures within hours of birth; Al-Dirbashi's two Saudi infants presented with *"severe neonatal-onset hypotonia, seizures, hepatic dysfunction"* and died within the first months. Su's patient presented in infancy and died at 14 months. Suggested `OnsetDescriptor.onset_category`: `CONGENITAL_ONSET` / `NEONATAL_ONSET`.

**Severity.** Severe by definition — PBD11A *is* the severity stratum. Individuals with the same gene but hypomorphic alleles (p.Arg294Trp, p.Ile326Thr) fall into PBD11B and can present at 3 years, 10 years, or later (Borgia families A and C: onset at 36 months and at ages 3 and 10 respectively).

**Progression.** In PBD11A: **progressive and rapidly fatal**, dominated by failure to thrive, refractory seizures, and hepatic decompensation. In PEX13-related PBD11B, the course is a **slowly progressive leukodystrophy with spasticity** — Borgia's family C brothers were wheelchair-dependent at ages 7 and 16 respectively, with *"bilateral hyperintensity within the posterior periventricular white matter … and thinning of the corpus callosum"*. This bimodality is the key genotype-driven phenotype split in PEX13 and should be modelled with `has_subtypes` or as two sibling entries.

**Frequency among affected individuals — for PBD11A specifically, the n is too small to quantify.** Hypotonia, seizures, developmental arrest, and hepatic involvement are effectively universal in the reported severe cases. For ZSD-wide frequencies use the caregiver-survey data (Bose 2020, PMID:33335840), which is the largest such dataset and explicitly argues that prior literature **undercounted**:

> *"Perception of disease severity and prevalence of various symptoms were greater in responses from caregivers of deceased individuals."* Combined seizure prevalence **53%**; adrenal insufficiency **45%** — both *"nearly twice as high"* as previous reports. n = 54 living + 25 deceased individuals. Conclusion: *"previous reports may be underreporting the true prevalence of several symptoms in ZSD."*

Other ZSD-wide frequency anchors (Klouwer 2015, PMID:26627182): sensorineural deafness *"almost always present"*; enamel hypoplasia *"in nearly all patients"*; renal calcium oxalate stones **83%**; primary adrenal insufficiency **7/24 (29%)** with **4/7 asymptomatic** (Berendse 2014, PMID:25179809).

### 3.4 Quality of life impact

No PBD11A-specific QoL instrument data exists. ZSD-wide:

- `NCT03440905` "Proxy-Reported Symptoms and Quality of Life Survey in Zellweger Spectrum Disorders" (n=92, completed 2018) is the relevant instrument study.
- **Klouwer et al. 2018 ZSD severity score** (Clin Genet 93(3):613-621, PMID:28857144) is the validated disease-specific severity instrument: n=30, evaluates **14 organs**, median score 9 (range 6–19), median age 16 years. *"The ZSD severity score was significantly correlated with all 5 domains of the CAP"* (Capacity Profile), strongest with the **sensory domain (r = 0.8971, P < 0.0001)**. Notably, **no correlation between age and severity score** — arguing the severity is set by genotype, not accrued over time.
- For PBD11A, functional status is effectively "total care, non-verbal, non-ambulatory, tube-fed, for the duration of a life measured in months." Klouwer 2015 describes the spectrum-wide functional range as *"completely independent to 24 h care"*; PBD11A occupies only the latter pole.
- Dietary/feeding burden is quantified in Bose et al. 2025 (Nutrients, PMID:40290032): of 21 ZSD subjects aged 1–33, **ten of 21 were enterally fed**; fiber intake ran at *"about 50% of DRI"*.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**PEX13** — peroxisomal biogenesis factor 13. `hgnc:8855` · NCBI Gene 5194 · OMIM `*601789` · 2p15 · NC_000002.12:61,017,719–61,051,989 · canonical transcript `NM_002618.4` · UniProt `Q92968`, 403 aa.

Aliases carried by NCBI Gene: **NALD, PBD11A, PBD11B, ZWS** — note that the gene record itself carries both the severe and mild OMIM designations, which is why a naive gene-symbol lookup will not disambiguate PBD11A from PBD11B.

**Protein architecture (UniProt Q92968):**
- N-terminal cytosolic region containing a **KPWE motif at residues 10–13** that binds **PEX7** (the PTS2 receptor) — this is why PEX13 loss abolishes *both* PTS1 and PTS2 import, not just PTS1.
- Three transmembrane helices: **135–155, 175–192, 234–254**.
- C-terminal cytosolic **SH3 domain, residues 272–336**, which binds **PEX14** and PEX5.
- Additional interactors: PEX19 (membrane-protein targeting), CEP19.

The functional consequence of the domain layout is directly relevant to genotype–phenotype: a nonsense variant at codon 234 (`p.Trp234Ter`) truncates *before* the third transmembrane helix and the entire SH3 domain — hence the severe PBD11A phenotype — whereas SH3-domain missense variants (I326T, R294W) leave the membrane anchor intact and may retain partial activity.

### 4.2 Pathogenic variant catalogue

ClinVar contains **79 records for PEX13 classified pathogenic or likely pathogenic** (eutils query, retrieved 2026-08-28). The published, functionally characterised alleles:

| cDNA (`NM_002618.4`) | Protein | Type | Phenotype assignment | Zygosity / ancestry | Reference |
|---|---|---|---|---|---|
| `c.702G>A` | `p.Trp234Ter` | Nonsense | **PBD11A — severe ZS** | Homozygous (patient H-02) | Shimozawa 1999, PMID:10332040; ClinVar RCV000008142 |
| ~147 kb genomic deletion spanning whole gene | (null) | **Structural / whole-gene deletion** | **PBD11A — classical ZS** | Homozygous, Saudi | Al-Dirbashi 2009, PMID:19449432 |
| 14-bp out-of-frame deletion | `p.Gly36AspfsTer61` | Frameshift | **PBD11A — classical ZS** | Homozygous, Saudi | Al-Dirbashi 2009, PMID:19449432 |
| `c.938G>T` (verify) | `p.Trp313Gly` | Missense (SH3) | **PBD11A-range ZSD**, died 31 months | Homozygous, Turkish | Krause 2013, PMID:23716570 |
| `c.938G>A` | `p.Trp313Ter` | Nonsense | **PBD11A** — seizures within hours, died 20 months | Homozygous, Iranian | Borgia 2022, PMID:35854306 (family D) |
| `c.493G>C` | `p.Ala165Pro` | Missense | **PBD11A** — died 14 months | Homozygous, Chinese (consanguineous) | Su 2024, PMID:37962062; Dong 2024, PMID:38527511 |
| `c.970G>C` | `p.Gly324Arg` | Missense (SH3) | Severe/intermediate — died 3 years | Homozygous, Iranian | Borgia 2022 (family E) |
| `c.260A>G` | `p.Asn87Ser` | Missense | Submitted against **PBD11A** | — | ClinVar RCV000274515 |
| `c.880C>T` | `p.Arg294Trp` | Missense | **PBD11B-range** — later onset leukodystrophy/spasticity | Recurrent: hom. and comp. het. in 3/5 families | Borgia 2022 (families A, B, C) |
| `c.573_574delTT` | `p.Tyr192GlnfsTer14` | Frameshift | in trans with R294W | Compound het., Italian | Borgia 2022 (family A) |
| partial gene deletion | — | Structural | in trans with R294W | Compound het., Iraqi | Borgia 2022 (family C) |
| `c.977T>C` (verify) | `p.Ile326Thr` | Missense (SH3), **temperature-sensitive** | **PBD11B — NALD** | Homozygous (patient H-01) | Shimozawa 1999, PMID:10332040 |

**Variant classification.** Nonsense, frameshift, and whole-gene-deletion alleles are unambiguously ACMG PVS1-eligible. The missense alleles carry functional evidence (PS3) from complementation and interaction assays — this is a gene where functional work has been done for essentially every published missense.

**Allele frequency.** All published pathogenic PEX13 alleles are absent or ultra-rare in gnomAD. I was **unable to retrieve PEX13 constraint metrics (pLI/LOEUF/o/e)** — the gnomAD gene page is JavaScript-rendered and returned no data to the fetcher. Do not assert a pLI value for PEX13 without pulling it from the gnomAD API or a downloaded constraint table. Note that a recessive, embryonically-non-essential gene like PEX13 is not expected to be LoF-constrained, so a low pLI would be uninformative rather than reassuring.

**Somatic vs germline.** **Germline only.** PBD11A is not a somatic disease; there is no COSMIC/TCGA relevance to disease causation. (Separately, PEX13 appears as a *prognostic expression biomarker* in tumour datasets — Dong 2023, Oncol Lett, PMID:37920431 — but that is unrelated to PBD11A and must not be conflated with it.)

### 4.3 Functional consequences

**Loss of function**, with a specific mechanistic twist: PEX13 **homo-oligomerizes**, so certain missense alleles act by disrupting self-association rather than by destabilizing the protein outright.

> **Krause et al. 2013, Hum Mol Genet 22(19):3844-57, PMID:23716570 —** *"Here, we report for the first time that human PEX13 interacts with itself in peroxisomes in living cells. We demonstrate that the import of PTS1 (peroxisomal targeting signal 1) proteins is specifically disrupted when homooligomerization of PEX13 is interrupted. Live cell FRET microscopy in living cells as well as co-immunoprecipitation experiments reveal that the highly conserved W313 residue is important for self-association of PEX13 but is not required for interaction with PEX14, a well-established interaction partner at the peroxisomal membrane."*

Borgia et al. extended this to the recurrent R294W allele by computational docking: the variant *"drives the formation of aberrant dimers incapable of exposing as efficiently the residues responsible for its binding with PEX14"*, i.e. R294W permits dimerization but into a conformation that **occludes the PEX14 binding site** — a *misassembly* rather than *non-assembly* mechanism. For p.Gly324Arg: *"Computational predictions showed that the folding of PEX13 is affected"* and the mutant appears *"unable to form the expected complex with PEX14 and PEX5."*

This gives a defensible three-tier mechanism model to curate:
1. **Null alleles** (W234ter, whole-gene deletion, frameshift) → no docking complex → PBD11A.
2. **Oligomerization-disrupting missense** (W313G) → docking complex present but non-functional for PTS1 import → PBD11A-range.
3. **Destabilizing/hypomorphic missense** (I326T, R294W) → residual import → PBD11B.

There is **no evidence for gain-of-function or dominant-negative** PEX13 alleles in humans. Carriers are unaffected. Use `functional_impact_category: LOSS_OF_FUNCTION` on `GeneticContext`; use `modifier: DECREASED` on the affected `biological_processes` descriptors — **not** `LOSS_OF_FUNCTION` as a `modifier`, per the repo's GOF/LOF slot decision tree, unless you are specifically claiming a process has escaped regulatory constraint (it has not; it has simply stopped).

### 4.4 Modifier genes

**None identified.** Borgia's family B (homozygous R294W, profound congenital hypotonia) vs. families A and C (R294W compound het., onset at 3–10 years) shows real phenotypic variability that is **not** explained by the PEX13 genotype alone — a legitimate `KNOWLEDGE_GAP` and a candidate site for a `HUMAN_MODEL_MISMATCH`/modifier discussion. Note that a homozygote being *more* severe than compound heterozygotes for the same allele is at least internally consistent; the unexplained part is the 3-vs-10-year onset difference between two brothers in family C carrying identical genotypes — pointing to a modifier or stochastic effect.

### 4.5 Epigenetics

**No PBD11A-specific epigenetic data.** No methylation episignature has been reported for any ZSD. Plasmalogen deficiency has downstream effects on membrane lipid rafts and signalling, but nothing has been mapped to chromatin. Curate as not available.

### 4.6 Chromosomal abnormalities

One genuinely relevant finding: **Al-Dirbashi et al. 2009 reported the first PEX13 structural variant** — a genomic rearrangement producing a **147 kb deletion spanning the whole of PEX13**, in a homozygous state:

> *"One patient had a genomic rearrangement resulting in a 147 kb deletion that spans the whole of PEX13, while the other had an out-of-frame deletion of 14 bp. This represents the first report of a PEX13 deletion and suggests that further work is needed to examine the frequency of PEX13 mutations among Arab patients with peroxisomal biogenesis disorders."*

**Curation-critical implication:** exome/panel sequencing that does not call CNVs will miss this class of allele. A PBD11A entry should record that **CMA or CNV-aware analysis is required** to exclude PEX13 as a cause (see §10).

**Caution — a real Named Entity Confusion trap here.** PEX13 sits at 2p15, inside the **2p16.1-p15 microdeletion/microduplication syndrome** interval. Several papers in a PEX13 literature search (Ręka 2024 PMID:39050773; Chen 2018 PMID:30122582; Mimouni-Bloch 2015 PMID:26278498; Wang 2023 PMID:37937284) describe 2p15 CNV syndromes involving **XPO1/USP34**, and are about intellectual disability or pulmonary hypertension — **not** about peroxisome biogenesis. Do not cite them for PBD11A.

---

## 5. Environmental Information

- **Environmental factors:** None causal. No toxin, radiation, pollutant, or occupational exposure contributes to PBD11A. Curate the section as intentionally empty, or use the repo's `review_notes:` waiver convention if an exposure entry is created and cannot be cited.
- **Lifestyle factors:** Not applicable to a congenital neonatal-lethal disorder. The one *dietary* variable with a mechanistic link is **phytanic acid intake** (dairy fat, ruminant meat, certain fish), which the patient cannot α-oxidize — but this is a *treatment/management* consideration (§12), and Klouwer 2015 warns against reflexive restriction because caloric adequacy matters more.
- **Infectious agents:** None. PBD11A is not infectious, is not triggered by infection, and has no known pathogen association.

One item that could be mistaken for an infection/immune interaction and should be handled carefully: **Fazi et al. 2022** (Front Pediatr 10:852943, PMID:35402347) report a case of Zellweger syndrome with **agammaglobulinemia detected on newborn screening for primary immunodeficiency**, in whom *"No mutations causative of inborn error of immunity (humoral defect) were detected"* on exome. They hypothesise a link via the **NF-κB pathway, crucial for B-cell survival**, and conclude: *"Further studies are required to confirm this hypothesis."* This is n=1, hypothesis-generating, and **not PEX13-specific** — if curated at all it belongs as a `KNOWLEDGE_GAP` discussion, not as an established immune phenotype.

---

## 6. Mechanism / Pathophysiology

### 6.1 The proximal defect — docking-complex failure

PEX13 and PEX14 form the **peroxisomal docking complex**. The current structural model, revised substantially in 2023, is not a static pore but a **transient, phase-separated channel**:

> **Ravindran et al. 2023, Nature 617(7961):608-615, PMID:37165185 —** Pex13 *"undergoes liquid-liquid phase separation (LLPS) with Pex5-cargo"*, forming transient transport channels rather than a fixed pore; the process depends on intrinsically disordered regions acting as molecular adhesion points.

The classical model (UniProt/Q92968) describes the PEX13–PEX14 complex forming *"a large import pore (~9 nm diameter)"* permitting import of fully folded, even oligomeric, cargo. Both models agree on the essential point for disease: **PEX13 is the obligatory receiving station**, and both PTS1 (via PEX5) and PTS2 (via PEX7, bound to PEX13's KPWE motif) traffic through it.

A 2025 cryo-EM structure of the trypanosomal import complex (Sonani et al., Nat Commun, PMID:41381475) *"unveils conformational heterogeneity"* — consistent with the dynamic-channel model.

PEX13 also participates in **PEX5 recycling/export**: chemically monoubiquitinated PEX5 binds docking *and* export machinery components (Hagmann et al. 2018, Sci Rep, PMID:30375424). This is the link to the pexophagy mechanism below.

### 6.2 Proposed pathophysiology node chain

A node-by-node structure suitable for the `pathophysiology:` block:

| # | Node | `biological_scale` | Key GO/CL/UBERON leads |
|---|---|---|---|
| 1 | Biallelic PEX13 loss of function | MOLECULAR | `hgnc:8855` |
| 2 | Disrupted PEX13 homo-oligomerization / PEX13–PEX14 docking complex | MOLECULAR | GO:0005778 peroxisomal membrane; GO:0005515 protein binding |
| 3 | Failure of PTS1 (PEX5) and PTS2 (PEX7) cargo delivery | MOLECULAR | GO:0016558 protein import into peroxisome matrix (`modifier: DECREASED`) |
| 4 | Collapse of peroxisomal matrix protein import → "peroxisomal ghosts" | CELLULAR | GO:0007031 peroxisome organization; GO:0005777 peroxisome |
| 5a | Failure of peroxisomal β-oxidation → VLCFA accumulation | MOLECULAR | GO:0006635 fatty acid beta-oxidation; GO:0000038 very long-chain fatty acid metabolic process |
| 5b | Failure of ether-lipid synthesis → plasmalogen deficiency | MOLECULAR | GO:0008611 ether lipid biosynthetic process |
| 5c | Failure of α-oxidation → phytanic/pristanic accumulation | MOLECULAR | GO:0018882 (verify) phytanate catabolism |
| 5d | Failure of bile-acid side-chain oxidation → DHCA/THCA accumulation | MOLECULAR | GO:0006699 bile acid biosynthetic process |
| 5e | Loss of peroxisomal glyoxylate detoxification → hyperoxaluria | MOLECULAR | GO:0046487 glyoxylate metabolic process |
| 6 | Secondary mitochondrial dysfunction and oxidative stress | CELLULAR | GO:0006979 response to oxidative stress; GO:0005739 mitochondrion |
| 7 | Enhanced pexophagy / loss of residual peroxisomes | CELLULAR | GO:0000425 pexophagy |
| 8 | Impaired neurogenesis, neuronal migration, gliosis | TISSUE | GO:0001764 neuron migration; CL:0000047 neural stem cell; CL:0000127 astrocyte |
| 9 | Hypomyelination / leukodystrophy | TISSUE | GO:0042552 myelination; CL:0000128 oligodendrocyte; UBERON:0002316 white matter |
| 10 | Cortical dysplasia (polymicrogyria/pachygyria) | TISSUE | UBERON:0000956 cerebral cortex |
| 11 | Cholestatic liver disease → fibrosis/cirrhosis | TISSUE | UBERON:0002107 liver; CL:0000182 hepatocyte |
| 12 | Multiorgan failure, neonatal death | ORGANISM | — |

### 6.3 Secondary mitochondrial dysfunction — a PEX13-specific finding

This is the most distinctive mechanistic contribution of the PEX13 literature and deserves its own node with the Borgia and Rahim citations attached.

> **Borgia et al. 2022, Orphanet J Rare Dis 17(1):286, PMID:35854306 —** *"Studies on muscle tissues and patient-derived fibroblasts revealed biochemical alterations of mitochondrial function and identified mislocalised mitochondria and a reduced number of peroxisomes with abnormal PEX13 concentration."* And in the conclusion: *"...also highlight a variety of disease mechanisms contributing to PEX13-related clinical phenotypes, including the emerging contribution of secondary mitochondrial dysfunction to the pathophysiology of ZSDs."*

Their specific observations: muscle biopsy showed *"uneven distribution of mitochondria including patchy or reticular patterns and areas devoid of oxidative staining"*; muscle COX activity 1.59 (normal 1.80–2.45); fibroblasts showed *"decreased MitoTracker accumulation"* and, under stress, *"the percentage of mitochondria that are mislocalized in the outer cytoplasmic region … is markedly increased."*

The mouse model corroborates this independently:

> **Rahim et al. 2016, Neuroscience 334:201-213, PMID:27514574 —** brain-restricted PEX13-deficient mice showed an *"expanded and morphologically modified brain mitochondrial population"*; PEX13-deficient fibroblasts showed *"increased levels of mitochondrial superoxide and membrane depolarization"* which **antioxidant treatment rescued**; and significant oxidative damage evident through *"products of lipid and DNA oxidation"* in neurons and glia.

Curate this as an explicit node with a causal edge from the peroxisomal defect, and note the *in vitro* antioxidant rescue as an untested therapeutic hypothesis (`evidence_source: IN_VITRO`).

### 6.4 Pexophagy — PEX13 as a brake on peroxisome destruction

A second PEX13-specific mechanism, and one that has already been taken to clinical trial (`NCT03856866`, §12):

> **Demers et al. 2023, Autophagy 19(6):1781-1802, PMID:36541703 —** *"Using gene editing and quantitative fluorescence microscopy on culture cells and a zebrafish model system, we found that PEX13, a component of the peroxisomal matrix import system, is required to prevent the degradation of otherwise healthy peroxisomes. The loss of PEX13 caused an accumulation of ubiquitinated PEX5 on peroxisomes and an increase in peroxisome-dependent reactive oxygen species that coalesce to induce pexophagy."*

This is mechanistically important because it creates a **feed-forward loop**: PEX13 loss → ubiquitinated PEX5 stalls on the membrane → ROS rises → pexophagy → the residual peroxisomes a hypomorphic allele might have preserved are destroyed anyway. It is the rationale for the hydroxychloroquine trial (autophagy inhibition to *preserve* residual peroxisomes).

PEX13 additionally has a **peroxisome-independent** role in selective autophagy generally — Lee et al. 2017 (EMBO Rep 18(1):48-60, PMID:27827795) found PEX13 *"required for selective autophagy"* of viruses and damaged mitochondria, with disease-associated mutations showing **defective mitophagy**. This provides a second, independent route from PEX13 mutation to mitochondrial pathology and should be curated as an alternative/complementary `hypothesis_group`.

### 6.5 Neurodevelopmental mechanism (mouse-derived; flag translational validity)

> **Rahim et al. 2018, Mol Cell Neurosci 88:16-32, PMID:29187321 —** brain-restricted PEX13 inactivation produced *"enlarged lateral ventricles and aberrant cortical, hippocampal and hypothalamic organization"*, with significant reduction in neural progenitor proliferation, migration, and differentiation from E12.5 through P3; **reactive gliosis starting at E14.5**; and increased cell death.

> **Rahim et al. 2014, Neuroscience 274:229-41, PMID:24881576 —** PEX13 brain mutants showed decreased **tryptophan hydroxylase-2** (rate-limiting for serotonin synthesis), with *"dysmorphic 5-HT-positive neurons, abnormal distribution of 5-HT neurons, and dystrophic serotonergic axons"*, plus increased apoptosis and reactive gliosis in the raphe nuclei.

> **Müller et al. 2011, Dis Model Mech 4(1):104-19, PMID:20959636 —** Nestin-Cre brain-restricted Pex13 mutants show *"abnormal cerebellum formation, reactive gliosis and oxidative stress"*, with defects in cerebellar fissure and cortical layer formation, granule cell migration, and Purkinje cell layer development. Critically: **plasmalogen content reduced but VLCFA normal** in the mutant brain — a dissociation arguing plasmalogen deficiency, not VLCFA accumulation, drives the CNS phenotype.

**Curate the serotonergic finding as `HUMAN_MODEL_MISMATCH`, not as human pathophysiology.** Central serotonergic deficiency has never been demonstrated in a human ZSD brain; it is a mouse finding of clear mechanistic interest with unestablished translational validity.

### 6.6 Hepatic and iron mechanism

> **Rishi et al. 2020, Biochim Biophys Acta Mol Basis Dis 1866(10):165882, PMID:32565019 —** hepatocyte-specific Pex13 deletion led to *"decreased hepcidin expression"* via increased SMAD7 signalling and ER stress, *"establishing a novel connection between peroxisomal function and iron regulation."* This is a candidate explanation for iron dysregulation in ZSD liver disease and is currently mouse-only.

### 6.7 Lipid-metabolic consequences

> **Vinoy et al. 2026, Biosci Rep, PMID:41860470 —** loss of PEX13/PEX14 *"altered the expression of genes involved in lipid sensing, fatty acid uptake, synthesis, and oxidation"*, contributing to hepatic fatty acid accumulation and potential liver disease.

### 6.8 Immune involvement

Not an immune-mediated disease. See the §5 caveat regarding the single agammaglobulinemia case report.

### 6.9 Molecular profiling / advanced technologies

- **Transcriptomics:** No PBD11A patient transcriptome dataset located. GEO search for PEX13-specific ZSD is unproductive. The 2026 Vinoy paper provides PEX13/PEX14-loss expression data (system unspecified in the abstract; verify before citing as human).
- **Proteomics:** Lotz-Havla et al. 2021 (J Proteome Res, PMID:34383492) performed an **iBRET screen of the ABCD1 peroxisomal network with mutation-induced network perturbations** — the closest thing to a peroxisomal interactome resource; useful for the PEX13 interaction map but centred on ABCD1.
- **Metabolomics/lipidomics:** The diagnostic biomarker panel (§10) *is* the metabolomic signature. Reference: Jaspers/Vaz et al., J Lipid Res 2024 (PMC10910329) — plasma C24:0- and C26:0-LPC as reliable peroxisomal β-oxidation-disorder biomarkers with *"superior diagnostic accuracy compared with conventional VLCFA biomarkers."*
- **Single-cell / spatial:** None for PBD11A.
- **Functional genomics screens:** No PEX13-focused CRISPR screen located; DepMap PEX13 dependency is not disease-relevant.

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:**
| Organ / system | UBERON lead | Manifestation |
|---|---|---|
| Brain | UBERON:0000955 | neuronal migration defect, hypotonia, seizures |
| Cerebral cortex | UBERON:0000956 | polymicrogyria, pachygyria, disordered lamination |
| Cerebral white matter | UBERON:0002316 | hypomyelination, leukodystrophy |
| Cerebellum | UBERON:0002037 | atrophy, granule-cell migration defect, vermian hypoplasia |
| Liver | UBERON:0002107 | hepatomegaly, cholestasis, fibrosis, coagulopathy |
| Kidney | UBERON:0002113 | renal cortical cysts, hyperoxaluria, calcium oxalate stones |
| Eye / retina | UBERON:0000970 / UBERON:0000966 | retinopathy, cataract, glaucoma, cherry-red spot |
| Inner ear | UBERON:0001846 | sensorineural hearing loss |
| Skeleton | UBERON:0001474 | chondrodysplasia punctata (calcific stippling) |
| Adrenal gland | UBERON:0002369 | primary adrenal insufficiency |
| Craniofacial skeleton | UBERON:0010363 (verify) | high forehead, large fontanelles, flat nasal bridge |
| Teeth | UBERON:0001091 (verify) | enamel hypoplasia (*"nearly all patients"*) |

The "cerebrohepatorenal" triad in the disease's historical name is exactly right: brain, liver, kidney.

**Secondary:** peripheral nerve (demyelinating neuropathy — Borgia family C: *"uniform demyelination"* on NCS); skeletal muscle (mitochondrial abnormalities on biopsy); haematologic (coagulopathy from hepatic synthetic failure and vitamin K malabsorption); respiratory (apnea, HP:0002104 — a proximate cause of neonatal death).

### Tissue and cell level

| Cell type | CL lead | Involvement |
|---|---|---|
| Neuron | CL:0000540 | migration failure, degeneration |
| Neural stem/progenitor cell | CL:0000047 | reduced proliferation, migration, differentiation (mouse) |
| Astrocyte | CL:0000127 | reactive gliosis from E14.5 (mouse) |
| Microglial cell | CL:0000129 | reactive inflammatory gliosis |
| Oligodendrocyte | CL:0000128 | hypomyelination |
| Purkinje cell | CL:0000121 | abnormal layer formation (mouse) |
| Cerebellar granule cell | CL:0000120 (verify) | migration defect (mouse) |
| Serotonergic neuron | CL:0000850 (verify) | reduced TPH2, dystrophic axons (**mouse only**) |
| Hepatocyte | CL:0000182 | cholestasis, ER stress, hepcidin suppression |
| Retinal photoreceptor | CL:0000210 (verify) | retinopathy |
| Skin fibroblast | CL:0000057 | the standard diagnostic/functional cell; import-defective |

### Subcellular level

| Compartment | GO CC lead | Role |
|---|---|---|
| Peroxisome | GO:0005777 | the primary affected organelle; present as empty "ghosts" |
| Peroxisomal membrane | GO:0005778 | site of PEX13; intact even when matrix import fails |
| Peroxisomal matrix | GO:0005782 | depleted of enzymes |
| Mitochondrion | GO:0005739 | secondary dysfunction, mislocalization, superoxide |
| Endoplasmic reticulum | GO:0005783 | ER stress in hepatocytes; also a source of pre-peroxisomal vesicles |
| Cytosol | GO:0005829 | mislocalized peroxisomal matrix enzymes |

**A crucial diagnostic point to curate:** the peroxisomal *membrane* is preserved. `PMP70`-positive structures are present; it is the matrix content that is missing. Borgia et al. quantified exactly this: *"ZSD patients display fewer PMP70-positive peroxisomes and severely impaired expression of PEX13-positive peroxisomes"*, and *"ZSD patients display enlarged PEX13-positive peroxisomes, while the size of overall PMP70-positive peroxisomes is not affected."*

### Localization / lateralization

**Bilateral and symmetric** throughout. Borgia's MRI descriptions are consistently bilateral: *"bilateral hyperintensity within the posterior periventricular white matter"*; *"bilateral malformation of cortical development in parietal lobes."* There is no asymmetric or unilateral variant of PBD11A. Suggested descriptor: bilateral, symmetric, posterior-predominant for the white-matter changes.

---

## 8. Temporal Development

### Onset

- **Typical age of onset for PBD11A: congenital / neonatal.** Seizures within hours of birth (Borgia family D); profound hypotonia from birth; inability to feed.
- **Onset pattern:** the neurodevelopmental lesion is **prenatal** (neuronal migration occurs in the second trimester and is already abnormal at birth), so the "onset" is really the point of clinical recognition rather than of pathogenesis. Presentation is acute-at-birth and then chronically progressive.
- Prenatal manifestations documented across ZSD: intrauterine growth retardation (reproduced in the mouse — Maxwell 2003: *"intrauterine growth retardation, severe hypotonia, failure to feed, and neonatal death"*), reduced fetal movement, polyhydramnios.

### Progression

**Stages (severe PBD11A):**
1. **Neonatal** (0–1 mo): hypotonia, seizures, feeding failure, dysmorphism, jaundice.
2. **Infantile** (1–12 mo): failure to thrive, no developmental progress, hepatic dysfunction, progressive hearing/vision loss, apnea.
3. **Terminal** (typically <12 mo, occasionally to 2–3 y): hepatic decompensation, refractory seizures, respiratory failure.

**Rate:** rapid. **Course:** progressive, non-remitting. **Duration:** lifelong but short.

Observed PEX13-specific survival: Al-Dirbashi 2009 — *"death within the first months"*; Krause 2013 — died at **31 months**; Borgia family D — died at **20 months**; Borgia family E — died at **3 years**; Su 2024 — *"The patient died at the age of 14 months."*

Note that these PEX13 severe cases skew *slightly* longer-lived than the textbook "<1 year" for classical ZS. With n≈5, this is not a defensible claim of PEX13-specific longevity — but it is worth recording as an observation with a `KNOWLEDGE_GAP`.

Klouwer 2015's spectrum-wide staging, for reference on the milder PEX13 (PBD11B) end: neonatal-infantile — *"Survival is usually not beyond the first year of life"*; childhood — *"Most patients die before adolescence"*, with *"progressive leukodystrophy"* and *"loss of acquired skills"*; adolescent-adult — *"usually slowly progressive, although the disease may remain stable for (many) years."*

### Patterns

- **Remission:** none, spontaneous or treatment-induced. No therapy alters the natural history of PBD11A.
- **Critical periods:** The therapeutically meaningful one is **prenatal neuronal migration** (~gestational weeks 12–24). Cortical dysplasia is fixed before birth, which is the fundamental reason no postnatal therapy can restore neurological function in PBD11A — a point worth stating explicitly in the entry, because it bounds what any future gene or enzyme therapy could achieve. Postnatally, the actionable windows are hepatic (cholic acid before advanced fibrosis) and sensory (hearing/vision support), not neurological.
- **Notable absence of anticipation:** and, per Klouwer 2018, **no correlation between age and severity score** across the spectrum — severity is genotype-set.

---

## 9. Inheritance and Population

### Epidemiology

**PBD11A-specific figures do not exist.** Fewer than ~10 severe PEX13 pedigrees are published. All numbers below are for ZSD as a whole and must be labelled that way.

| Measure | Value | Population | Source |
|---|---|---|---|
| Birth prevalence, all ZSD | ~1 in 50,000 | North America / US | Orphanet ORPHA:912; HRSA newborn screening |
| Birth prevalence, all ZSD | ~1 in 500,000 | Japan | Orphanet |
| Birth prevalence, all ZSD | ~1 in 12,000 | Saguenay–Lac-St-Jean, Québec | Orphanet (founder effect) |
| Birth incidence, all PEX genes | 1 in 50,000 – 1 in 83,000 | US | cited in Malone et al. 2025, PMID:40519747 |
| Birth incidence, **PEX1-mediated only**, core model | ~1 in 245,000 | US | Malone et al. 2025 |
| Birth incidence, **PEX1-mediated only**, expanded model | ~1 in 114,000 | US | Malone et al. 2025 |

**PEX13's share.** PEX1 alone accounts for ~60–70% of ZSD; PEX13 is among the rarest causal genes — Al-Dirbashi 2009: *"Mutations in PEX13 … are among the least common causes of peroxisomal biogenesis disorders with only three mutations reported so far."* Combining the ~1:50,000 ZSD figure with PEX13's estimated <2% share gives an order-of-magnitude PBD11A birth prevalence of roughly **1 in 2–5 million** — this is my arithmetic, not a published figure, and should be recorded as an estimate with that caveat, or omitted.

For a `Prevalence` record, the defensible entry is:
```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: ULTRA_RARE
  notes: >-
    Fewer than 25 individuals with biallelic PEX13 variants across the whole
    Zellweger spectrum had been reported worldwide as of 2024; the severe
    (PBD11A) subset is fewer than 10. No population-based estimate exists.
```
with the Su 2024 quote (*"only 21 cases reported worldwide and none in China"*) as evidence.

### Genetic epidemiology

- **Inheritance:** autosomal recessive (HP:0000007). Every published PEX13 pedigree is consistent with AR; carrier parents are unaffected.
- **Penetrance:** complete for biallelic null genotypes. No unaffected biallelic-null individual has been reported.
- **Expressivity:** **variable, and substantially so** — the same gene spans neonatal-lethal ZS (PBD11A) and adult-ambulatory leukodystrophy (PBD11B). Within a single genotype, family C's brothers (identical compound-heterozygous genotype) had onset at 3 and 10 years respectively.
- **Anticipation:** none — not a repeat-expansion disorder.
- **Germline mosaicism:** no reported instance in PEX13; recurrence-risk counselling should still note the general possibility.
- **Founder effects:** the Saguenay–Lac-St-Jean ZSD cluster (~1/12,000) is a **PEX1**-driven founder effect, not PEX13 — do not attribute it to PBD11A. Candidate PEX13 recurrent alleles: `p.Arg294Trp` (3/5 families, mixed ancestry) and `p.Ala165Pro` (2 Chinese families).
- **Consanguinity:** central. Most PEX13 pedigrees are consanguineous; Al-Dirbashi explicitly called for study of *"the frequency of PEX13 mutations among Arab patients with peroxisomal biogenesis disorders."*
- **Carrier frequency:** not established for PEX13. The methodology to derive it — Hardy-Weinberg modelling over >1.2 million genomes from TOPMed, All of Us, UK Biobank and gnomAD — is laid out in Malone et al. 2025 for PEX1 and has not been applied to PEX13.

### Population demographics

- **Ancestry of reported cases:** Saudi (×2 families), Turkish, Iranian (×2), Iraqi, Italian, Pakistani-Canadian, Chinese (×2), plus the original Japanese-series (group H) and US-series (CG13) patients. No ancestry group is established as over-represented beyond what consanguinity rates predict.
- **Geographic distribution:** worldwide, no endemic focus. Reporting is biased toward centres with peroxisomal-disorder expertise (Amsterdam UMC, Kennedy Krieger, Gifu/Kyushu, Griffith University).
- **Sex ratio:** **1:1**, autosomal recessive. Published PEX13 cases include both sexes.
- **Age distribution of affected individuals:** for PBD11A, essentially all prevalent cases are under 3 years old, because the disease is fatal in infancy. Prevalence at any moment is therefore approximately equal to annual births.

---

## 10. Diagnostics

### 10.1 Biochemical / laboratory testing — the diagnostic backbone

Biochemistry, not sequencing, is the entry point. From Klouwer et al. 2015 (PMID:26627182), the ZSD panel:

| Analyte | Direction in PBD11A | Specimen | LOINC lead |
|---|---|---|---|
| **C26:0 (hexacosanoic acid)** | ↑ | Plasma | verify |
| **C24:0/C22:0 and C26:0/C22:0 ratios** | ↑ | Plasma | verify |
| **C26:0-lysophosphatidylcholine (C26:0-LPC)** | ↑ | Dried blood spot / plasma | verify |
| **Plasmalogens** | ↓ | Erythrocytes | verify |
| **Phytanic acid** | ↑ | Plasma | verify |
| **Pristanic acid** | ↑ | Plasma | verify |
| **DHCA / THCA** (di- and trihydroxycholestanoic acid) | ↑ | Plasma | verify |
| **Pipecolic acid** | ↑ | Plasma | verify |
| **Oxalic acid** | ↑ | Urine | verify |
| Transaminases (AST/ALT) | ↑ | Serum | LOINC:1920-8 / LOINC:1742-6 |
| Coagulation (PT/INR) | ↑ | Plasma | verify |

Su 2024's patient is the canonical PEX13 biochemical profile: *"Serum analysis revealed elevated levels of very long-chain fatty acids (VLCFA), phytanic acid, and pipecolic acid."*

**Two essential caveats that must be curated as such:**

1. **Normal biochemistry does not exclude PEX13 disease.** Klouwer 2015: *"relatively mild ZSD patients may have (near) normal biochemical tests in plasma and urine."* This is not hypothetical for PEX13 — in Borgia 2022, **family C's two brothers had entirely normal VLCFA, phytanic acid, and pipecolic acid**, and families A and B had only *"minimally altered"* / *"marginal elevation"* of C26:0 with a **normal** C26:0/C22:0 ratio in family B. Had these families been screened biochemically alone, PEX13 disease would have been missed. For **severe PBD11A**, however, biochemistry is reliably grossly abnormal.
2. **C24:0/C26:0-LPC outperforms conventional VLCFA.** MS/MS of plasma C24:0- and C26:0-LPC gives *"superior diagnostic accuracy compared with conventional VLCFA biomarkers"* (J Lipid Res 2024, PMC10910329).

### 10.2 Imaging

- **Brain MRI** is the highest-yield imaging study. PBD11A pattern: cortical malformation (polymicrogyria/pachygyria, perisylvian-predominant), germinolytic cysts, delayed/absent myelination. PEX13-documented: *"bilateral malformation of cortical development in parietal lobes, with a polymicrogyria-like appearance"* (Borgia family D); *"diffuse hypomyelination"*, *"extensive cerebellar atrophy and pontine/vermian hypoplasia"* (family B); *"bilateral hyperintensity within the posterior periventricular white matter … and thinning of the corpus callosum"* (family C — the milder leukodystrophy pattern).
- **Abdominal ultrasound:** hepatomegaly, renal cortical cysts (HP:0000107 / HP:0005562), nephrocalcinosis/calculi.
- **Skeletal radiography:** patellar and long-bone epiphyseal stippling (chondrodysplasia punctata) — a classical and near-pathognomonic neonatal ZS finding.

### 10.3 Electrophysiology and functional testing

- **EEG:** *"multifocal sharp waves"* (Borgia family D); burst-suppression in the most severe neonates.
- **ABR / audiometry:** sensorineural hearing loss, near-universal in ZSD; annual evaluation recommended.
- **ERG:** severely attenuated/extinguished; retinopathy is progressive. `NCT06190626` is an active prospective natural-history study of ZSD retinopathy (n=30, recruiting through 2029).
- **Nerve conduction studies:** *"uniform demyelination"* in the milder PEX13 phenotype (Borgia family C) — relevant to PBD11B, less so to PBD11A where neuropathy is masked by the CNS disease.
- **Synacthen (ACTH stimulation) test:** mandatory. Berendse 2014: *"Systematic evaluation of adrenal function, through a Synacthen test, should be included in clinical management"*; 7/24 had primary adrenal insufficiency and **4 of those 7 were asymptomatic**.

### 10.4 Biopsy / pathology

- **Liver biopsy:** cholestasis, periportal inflammation, bridging fibrosis progressing to cirrhosis (documented longitudinally in a ZSD patient by Heubi & Bishop 2018, PMID:30519152). Peroxisomes absent or reduced on catalase immunostaining/EM.
- **Skin fibroblast culture** is the diagnostic workhorse for functional confirmation: immunofluorescence for catalase (cytosolic rather than punctate) and PMP70 (punctate membrane ghosts present). Historically, **complementation analysis** in fibroblasts assigned patients to CG13/group H before sequencing was routine — this is how both Shimozawa's and Al-Dirbashi's patients were localized to PEX13.
- **Muscle biopsy** (not routine): Borgia found *"uneven distribution of mitochondria including patchy or reticular patterns and areas devoid of oxidative staining"*, COX 1.59 (normal 1.80–2.45). Worth noting because a ZSD patient biopsied for suspected mitochondrial disease can produce a misleading mitochondrial-myopathy read.

### 10.5 Genetic testing

**Recommended approach:** abnormal peroxisomal biochemistry → **PEX-gene panel or WES/WGS** → confirm biallelic PEX13 variants by Sanger → segregate in parents. Su 2024's patient was *"identified by whole exome sequencing and validated by Sanger sequencing"*, the current standard route.

| Modality | Utility for PBD11A |
|---|---|
| **WES** | High. First-line in practice; identified the Su and most Borgia cases. |
| **WGS** | High; adds non-coding and CNV resolution. `NCT02699190` (LeukoSEQ) evaluated WGS as first-line for leukodystrophies. |
| **PEX gene panel** | High; the targeted equivalent. Must include all ~13 PEX genes plus single-enzyme β-oxidation genes for differential. |
| **Single-gene PEX13 testing** | Only justified for targeted familial-variant or carrier testing. |
| **CMA / CNV analysis** | **Necessary, not optional.** The 147-kb whole-gene PEX13 deletion (Al-Dirbashi 2009) and the partial deletion in Borgia family C are invisible to standard exome variant calling. A "negative" PEX13 exome in a biochemically confirmed patient requires CNV-aware reanalysis. |
| **Karyotype / FISH** | Not indicated. |
| **mtDNA testing** | Not indicated for PBD11A — but see the muscle-biopsy caveat above; a ZSD patient may be worked up for mitochondrial disease first. |
| **Repeat expansion testing** | Not applicable. |

### 10.6 Omics-based diagnostics

Metabolomics *is* the primary diagnostic (§10.1). RNA-seq has a role in resolving splice-affecting VUS but no PEX13-specific published application. Proteomics, epigenomics, and liquid biopsy: not applicable.

### 10.7 Clinical criteria and differential diagnosis

There is no formal consensus diagnostic criteria set (no DSM/ICD-style checklist); diagnosis is biochemical + molecular. GeneReviews "Zellweger Spectrum Disorder" (Steinberg, Raymond, Braverman, Moser; PMID:20301621, updated 2020-10-29) is the operative clinical reference.

**Differential diagnosis and the distinguishing feature:**

| Condition | How to distinguish |
|---|---|
| Other PBD-ZSD genes (PEX1/2/3/5/6/10/12/14/16/19/26) | Biochemically **identical**. Only sequencing or complementation separates them. PEX1 accounts for the majority. |
| **Single peroxisomal enzyme deficiencies** — D-bifunctional protein (HSD17B4), ACOX1 deficiency | ↑ VLCFA but **normal plasmalogens** and normal peroxisome number/morphology on fibroblast IF. Critically, the DHA trial excluded 2 of 50 enrolees on exactly this basis. |
| **Rhizomelic chondrodysplasia punctata** (PEX7, GNPAT, AGPS) | Plasmalogens ↓ and phytanic ↑ but **VLCFA normal** (PTS2-only defect). Rhizomelia is the clinical clue. |
| **X-linked adrenoleukodystrophy** (ABCD1) | ↑VLCFA and ↑C26:0-LPC, but X-linked, normal plasmalogens, no neonatal dysmorphism/migration defect. This is the single most consequential distinction because C26:0-LPC newborn screening is *for* X-ALD and catches ZSD incidentally. |
| Congenital muscular dystrophy / cobblestone lissencephaly (dystroglycanopathies) | Overlapping cortical malformation + hypotonia; distinguished by normal peroxisomal biochemistry and ↑CK. |
| Non-syndromic polymicrogyria, Walker-Warburg | Normal peroxisomal panel |
| Neonatal cholestasis of other cause (biliary atresia, Alagille) | Normal VLCFA/plasmalogens |
| Prader-Willi syndrome | Neonatal hypotonia and feeding failure overlap; distinguished by methylation testing and absent dysmorphic/migration features |
| **2p15 microdeletion syndrome** | Involves the PEX13 locus but the phenotype is ID/dysmorphism from XPO1/USP34, **not** peroxisomal. Peroxisomal biochemistry is normal. |

### 10.8 Screening

- **Newborn screening.** Zellweger spectrum disorder is listed as a **secondary/incidental target** on the HRSA newborn screening condition list, detected through **C26:0-LPC** measurement in dried blood spots on the X-ALD panel. Reference values: *"In normal newborn dried blood spot specimens, C26:0-LPC was 0.09±0.03 μmol/l whole blood, while in peroxisomal biogenesis disorder patients (including X-ALD), C26:0-LPC was 1.13±0.67 μmol/l whole blood."* California added X-ALD to its panel in 2016 (two-tier: C26:0-LPC → ABCD1 sequencing); a report of "other genetic conditions" identified through X-ALD NBS documented **seven individuals diagnosed with ZSD due to biallelic PEX variants** (PMC11275617). Method reference: Hubbard/Turgeon et al., improved negative-ion-mode HPLC-ESI-MS/MS for C26:0-LPC in DBS, PMID:22503909.
  - **This is a genuinely important curation point:** ZSD, including PBD11A, is increasingly detected *presymptomatically* as an incidental finding of X-ALD screening, not by clinical suspicion. That changes the diagnostic pathway described in most older reviews.
- **Carrier screening:** PEX13 appears on expanded carrier screening panels; no population-specific programme exists. Highest yield in consanguineous families and in families with a prior affected child.
- **Cascade screening:** offer targeted variant testing to at-risk relatives and reproductive partners once the family's two alleles are known.
- **Prenatal:** see §13.

---

## 11. Outcome / Prognosis

### Survival and mortality

- **PBD11A is uniformly fatal.** No survivor is reported. Documented PEX13-severe survival: death within the first months (Al-Dirbashi 2009, ×2); 14 months (Su 2024); 20 months (Borgia family D); 31 months (Krause 2013); 3 years (Borgia family E).
- OMIM's PBD11A description: children *"do not show any significant development and usually die in the first year of life."*
- Klouwer 2015 for the severe stratum: *"Prognosis is poor and survival is usually not beyond the first year of life."*
- **Disease-specific mortality is effectively 100%.** Proximate causes: respiratory failure/apnea, aspiration, refractory seizures, hepatic failure with coagulopathy, sepsis.
- 5-year and 10-year survival: **~0%** for PBD11A. (For the milder PEX13 phenotype, PBD11B, survival into adulthood occurs — Borgia's family C individuals were alive at 19 and 23.)

### Morbidity and function

- Universal, profound, global disability: non-verbal, non-ambulatory, no meaningful developmental progress, total care dependency, enteral feeding.
- **No disease-specific QoL instrument for PBD11A.** The validated tool for the spectrum is the **ZSD severity score** (Klouwer 2018, PMID:28857144): 14 organs, median 9 (range 6–19), correlated with all 5 CAP domains, strongest with the sensory domain (r=0.8971, P<0.0001). PBD11A patients would sit at the top of that range.
- `NCT03440905` (proxy-reported symptoms and QoL, n=92) is the reference dataset for caregiver-reported burden.

### Complications

Hepatic: cholestasis → fibrosis → cirrhosis → portal hypertension. In one long-followed ZSD patient on cholic acid to age 19, the endpoint was *"clinical cirrhosis, severe portal hypertension, worsening jaundice"* and **hepatocellular carcinoma** (Heubi & Bishop 2018, PMID:30519152) — a complication that only becomes visible in patients who live long enough, i.e. not in PBD11A, but worth recording for the gene as a whole.
Renal: hyperoxaluria → calcium oxalate stones (83% in ZSD) → nephrocalcinosis.
Endocrine: primary adrenal insufficiency (29–45%), **frequently asymptomatic** and therefore a preventable cause of crisis and death.
Haematologic: vitamin-K-dependent coagulopathy, intracranial haemorrhage risk.
Sensory: progressive blindness and deafness.
Nutritional: fat-soluble vitamin (A, D, E, K) deficiency; failure to thrive.
Dental: enamel hypoplasia (*"nearly all patients"*).

### Recovery potential

**None.** The cortical malformation is prenatally fixed. No intervention restores peroxisome biogenesis in a null genotype.

### Prognostic factors

1. **Genotype is the dominant prognostic factor.** Null/null (nonsense, frameshift, whole-gene deletion) → PBD11A → death in infancy. Hypomorphic missense, especially SH3-domain temperature-sensitive alleles → PBD11B → survival to adolescence or adulthood.
2. **Residual peroxisomal function in fibroblasts** — Liu 1999's NALD patient was distinguished from ZS by exactly this: *"residual matrix-protein import can be detected in cells from patient PBD222, consistent with the relatively mild phenotypes of the patient."*
3. **Degree of biochemical abnormality**: Klouwer 2018 found *"Multiple peroxisomal biochemical parameters showed significant correlation with severity score."*
4. **Presence and severity of liver disease** — the main determinant of survival among those who survive infancy, and the one modifiable axis (§12).
5. **Temperature-sensitive fibroblast phenotype** is the specific predictor of response to peroxisome-biogenesis-stimulating agents.

**Prognostic biomarkers:** plasma C26:0/C26:0-LPC, erythrocyte plasmalogen levels, DHCA/THCA. No validated molecular prognostic panel exists.

---

## 12. Treatment

**There is no curative or disease-modifying therapy for PBD11A.** Klouwer 2015: *"There is currently no curative therapy, but supportive care is available."* Everything below is supportive, and the evidence base is weak-to-absent for the severe phenotype specifically.

### 12.1 Pharmacotherapy

**Cholic acid (Cholbam®)** — the only FDA-approved drug with a ZSD indication.
- FDA approval **17 March 2015** (NDA 205750), *"as an adjunct to standard of care for peroxisomal disorders including Zellweger spectrum disorders in patients with evidence of liver disease, based on improvements in liver function."*
- Mechanism: down-regulates cholesterol 7α-hydroxylase (the rate-limiting step of bile-acid synthesis), *"inhibit[ing] the production and accumulation of hepatotoxic and cholestatic bile acid precursors"* (i.e. DHCA/THCA).
- Best evidence: **Berendse et al. 2016, J Inherit Metab Dis 39(6):859-868, PMID:27469511** — open-label pretest–posttest, **n=19**, 2.5 years pre-intervention longitudinal follow-up, 9 months oral cholic acid, measurements at baseline/4/12/36 weeks. *"[B]ile acid synthesis decreased in the majority of patients"* and *"[r]educed levels of bile acid intermediates were found in plasma."* **Critically: the advanced-liver-disease subgroup (n=4) showed increased plasma transaminases, bilirubin and cholic acid.** Conclusion: *"Oral cholic acid therapy can be used in the majority of patients with a ZSD"* but caution is required *"in patients with advanced liver disease due to possible hepatotoxic effects."*
- Klouwer 2015's assessment remains apt: FDA approval established safety, but *"efficiency should be demonstrated in large clinical trials."* Ongoing registry: `NCT03115086` (REPLACE Registry for Cholbam, n=55, active, through 2039).
- NCIT: `NCIT:C15986` Pharmacotherapy; `therapeutic_agent` → `CHEBI:16359` cholic acid (verify) or the NCIT drug term.

**Hydrocortisone / cortisone replacement** for confirmed primary adrenal insufficiency. Klouwer 2015 stresses treating **only confirmed** insufficiency (abnormal Synacthen), because supplementation is *"associated with severe side effects, such as growth suppression and osteoporosis"* — while also insisting *"All ZSD patients need to be screened for adrenal insufficiency."* This tension is worth curating explicitly as it is the single most actionable item in ZSD care.

**Antiseizure medications** — standard agents; no ZSD-specific regimen. Seizures in PBD11A are frequently refractory.

**Fat-soluble vitamin supplementation** — A, D, E for documented deficiency; **vitamin K for coagulopathy** (`NCIT:C15433` Nutritional Support; note the CLAUDE.md warning **not** to tag nutritional supplementation as `BEHAVIORAL`).

**Oral citrate** for hyperoxaluria, with adequate fluid intake, plus **yearly hyperoxaluria screening**.

**Pharmacogenomics:** no PharmGKB/CPIC guidance applicable to PBD11A.

### 12.2 Advanced therapeutics

**None available.** No gene therapy, gene editing, ASO, siRNA, mRNA, cell therapy, or protein-replacement product exists or is in trial for PEX13 or any ZSD. This is a meaningful negative to record.

Conceptual barriers specific to this disease, worth stating in the entry: (a) the cortical malformation is prenatally fixed, so postnatal gene delivery cannot restore neurological function; (b) the target is an *integral membrane protein of an organelle that must be assembled*, not a secreted enzyme amenable to cross-correction — so the hepatic-directed AAV strategies that work for other metabolic diseases do not transfer straightforwardly.

**Allogeneic HSCT** appears in `NCT02171104` (MT2013-31, Phase 2, n=149, active) which lists Zellweger among eligible metabolic disorders. There is **no evidence of benefit in ZSD**, and the mechanistic rationale (cross-correction) does not obviously apply. Do not curate HSCT as an established ZSD treatment.

### 12.3 Experimental treatments (with NCT identifiers)

| NCT | Title | Phase | Status | n | Relevance |
|---|---|---|---|---|---|
| `NCT03856866` | Hydroxychloroquine Administration for Reduction of Pexophagy | Phase 2 | **Completed** (2019-01-11 → 2020-05-05) | **3** | Directly tests the Demers/Lee pexophagy mechanism (§6.4): inhibit autophagy to preserve residual peroxisomes. n=3; **no published results located** — flag as a knowledge gap. |
| `NCT01838941` | Betaine and Peroxisome Biogenesis Disorders | Phase 3 | Completed (2013–2015) | 12 | Betaine as a chemical chaperone/methyl donor. **No published results located.** |
| `NCT01668186` | Longitudinal Natural History Study of Patients With PBD | Observational | Recruiting → 2031 | 244 | The principal natural-history resource. |
| `NCT06190626` | Longitudinal Prospective Natural History Study of Retinopathy in ZSD | Observational | Recruiting → 2029 | 30 | Retinal endpoints for future trials. |
| `NCT00007020` | Compassionate Treatment … With Cholic Acid | Phase 3 | Completed | 85 | The historical cholic acid dataset supporting FDA approval. |
| `NCT00004442` | Study of Bile Acids in Patients With Peroxisomal Disorders | N/A | **Terminated** | 25 | CDCA/cholic/ursodiol. |
| `NCT03440905` | Proxy-Reported Symptoms and QoL Survey in ZSD | Observational | Completed | 92 | QoL instrument. |
| `NCT03047369` | Myelin Disorders Biorepository Project | Observational | Recruiting | 12,000 | Biorepository. |

**A negative result that must be curated as a negative:**

> **Paker et al. 2010, Neurology 75(9):826-830, PMID:20805528 — "Docosahexaenoic acid therapy in peroxisomal diseases: results of a double-blind, randomized trial."** Randomized, double-blind, placebo-controlled, single centre; DHA 100 mg/kg/day. 50 enrolled; 2 excluded (single-enzyme β-oxidation defects); 34 returned for follow-up; **9 died during the trial of their disorder**; 5 lost to follow-up. **There was no difference in outcomes between treated and untreated groups in biochemical function, electroretinogram, or growth.**

Klouwer 2015 concurs: DHA *"leads to increased DHA levels in plasma, but no improvement of visual function and growth."* Curate DHA with `supports: REFUTE` against any efficacy claim. This is exactly the kind of well-designed negative trial whose absence from a KB entry lets a refuted therapy keep circulating.

**Plasmalogen precursor replacement (batyl alcohol / alkylglycerols):** case reports of improvement, but Klouwer 2015 is blunt — *"never studied systematically."* Curate as unproven.

**Peroxisome-biogenesis-stimulating compounds:** trials ongoing per Klouwer 2015; *"greatest beneficial effect expected in patients whose fibroblasts showed temperature sensitivity"* — i.e. a genotype-stratified strategy that would apply to `p.Ile326Thr`-type PEX13 alleles (PBD11B), **not** to PBD11A null genotypes.

**Antioxidants:** mechanistically motivated by the mitochondrial superoxide rescue in PEX13-deficient fibroblasts (PMID:27514574). *In vitro* only; **no human trial**. Curate as a hypothesis with `evidence_source: IN_VITRO`.

### 12.4 Surgical, interventional, supportive, rehabilitative

| Intervention | Detail | NCIT lead |
|---|---|---|
| Gastrostomy | For inadequate caloric intake — Klouwer's first-line nutritional recommendation | `NCIT:C15329` Surgical Procedure |
| Cataract extraction | ZSD cataracts; early surgery where feasible | `NCIT:C15329` |
| Hearing aids / **cochlear implant** | Klouwer 2015 explicitly: *"Hearing aids, cochlear implant"*; annual audiology | `NCIT:C15747` Supportive Care (no reliable NCIT device term) |
| Corrective lenses | For severe myopia (Borgia family A) | — |
| Scoliosis surgery | Documented in Borgia family C (age 13) — relevant to longer-surviving PEX13 patients | `NCIT:C16186` Orthopedic Surgical Procedure |
| Dental care | Enamel hypoplasia in *"nearly all patients"* | `NCIT:C15747` |
| Physical / occupational / speech therapy | Standard for severe global delay | `NCIT:C15302`, `NCIT:C121351`, `NCIT:C159273` |
| Palliative care | The realistic frame for PBD11A | `NCIT:C15747` Supportive Care |
| Genetic counselling | See §13 | `NCIT:C15240` |

**Dietary:** gastrostomy feeding as above; **phytanic acid restriction only when levels are extremely high** (Klouwer: *"sufficient intake of calories is more decisive"*). Feasibility of dietary assessment in this population is established (Bose 2025, PMID:40290032: 21 subjects, 24-h recall vs 3-day records *"highly correlated for all nutrients (r² = 0.998, p < 0.0001)"*; fiber *"about 50% of DRI"*).

### 12.5 Treatment strategy

There is **no published treatment algorithm specific to PBD11A**. Klouwer et al. 2015 is the de facto management guideline for the spectrum and is organised by organ system, which maps cleanly onto a `treatments:` block. The practical algorithm for PBD11A:

1. Confirm diagnosis biochemically + molecularly.
2. Baseline: liver function + coagulation, **Synacthen test**, audiology, ophthalmology, renal ultrasound + urine oxalate, EEG.
3. Treat what is treatable: adrenal insufficiency (if confirmed), coagulopathy (vitamin K), seizures, nutrition (gastrostomy), fat-soluble vitamins, hyperoxaluria (citrate + fluids).
4. Consider cholic acid **if** there is liver disease **and not** advanced liver disease.
5. Annual surveillance: audiology, ophthalmology, hyperoxaluria, adrenal function, liver.
6. Genetic counselling and reproductive planning for the family.
7. Palliative care integration, given the prognosis.

**Personalized medicine:** the only genotype-guided decision currently available is **fibroblast temperature-sensitivity testing** to identify candidates for biogenesis-stimulating compounds — applicable to hypomorphic PEX13 alleles, not to PBD11A.

---

## 13. Prevention

### Primary prevention

Not preventable in an affected fetus — the disease is determined at conception. Prevention operates entirely at the **reproductive** level:

- **Genetic counselling** (`NCIT:C15240`): 25% recurrence risk per pregnancy for carrier couples; carrier testing for at-risk relatives; discussion of consanguinity-associated risk. This is the single highest-yield preventive intervention given how many PEX13 pedigrees are consanguineous.
- **Preimplantation genetic testing for monogenic disease (PGT-M)** — available once both familial alleles are known.
- **Prenatal diagnosis** — CVS or amniocentesis with (a) targeted variant testing when the familial alleles are known, and/or (b) biochemical assay in cultured amniocytes/chorionic villi (VLCFA, plasmalogen synthesis, DHAP-AT activity), the historical method still useful when the molecular diagnosis is incomplete.
- **Expanded carrier screening** before conception, particularly in consanguineous couples and in populations where a recurrent allele has been described.

### Secondary prevention

- **Newborn screening.** ZSD is detected as a secondary target of C26:0-LPC-based X-ALD newborn screening (§10.8). For PBD11A this does not change outcome — the neurological damage is prenatal — but it does enable earlier adrenal and hepatic surveillance, avoids a diagnostic odyssey, and informs reproductive counselling for the next pregnancy. Do not overstate its benefit for the severe phenotype.
- **Cascade screening** of relatives once a proband is identified.

### Tertiary prevention (preventing complications)

This is where the actionable clinical content sits, and it should be curated as such:

| Complication | Preventive action | Evidence |
|---|---|---|
| Adrenal crisis | **Annual Synacthen testing**; treat confirmed insufficiency | Berendse 2014, PMID:25179809 — 7/24 affected, **4/7 asymptomatic** |
| Intracranial/GI haemorrhage | Vitamin K supplementation, coagulation monitoring | Klouwer 2015 |
| Nephrolithiasis / nephrocalcinosis | **Yearly hyperoxaluria screening**, oral citrate, adequate fluids | Klouwer 2015 (83% stone prevalence) |
| Progressive liver disease | Cholic acid (if not advanced), fat-soluble vitamins, monitoring for fibrosis | Berendse 2016, PMID:27469511 |
| Aspiration / malnutrition | Gastrostomy, swallow assessment | Klouwer 2015 |
| Sensory deprivation compounding developmental delay | Annual audiology and ophthalmology, hearing aids/CI, cataract surgery | Klouwer 2015 |
| Dental disease | Dental referral for enamel hypoplasia | Klouwer 2015 |

### Immunization

Standard childhood immunization schedule; no ZSD-specific contraindication or additional vaccine is indicated. Live-vaccine caution applies only if the patient is on immunosuppressive doses of corticosteroid for adrenal replacement (replacement doses are not immunosuppressive).

### Public health / environmental interventions

Not applicable — no environmental component. The only population-level lever is **consanguinity-informed genetic counselling and carrier screening programmes** in populations with high consanguinity rates, which is precisely what Al-Dirbashi et al. called for regarding Arab populations.

---

## 14. Other Species / Natural Disease

**No naturally occurring PEX13-deficient disease is documented in any non-human species.** OMIA has no PEX13 entry that I could locate. This is a genuine negative to record — unlike, for example, canine SOD1 degenerative myelopathy for ALS, there is no spontaneous veterinary model of PBD11A.

### Taxonomy and orthology

| Species | NCBI Taxon | Gene | Notes |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | PEX13, Gene 5194 | |
| *Mus musculus* | NCBITaxon:10090 | Pex13 | Engineered models only (§15) |
| *Danio rerio* | NCBITaxon:7955 | pex13 | Engineered; used in Demers 2023 pexophagy work |
| *Saccharomyces cerevisiae* | NCBITaxon:4932 | PEX13 | The organism in which peroxin function was originally defined |
| *Hansenula polymorpha* | NCBITaxon:4903 (verify) | PEX13 | Thomas 2018, PMID:29924881 — PEX13 required for Aat2p peroxisomal targeting |
| *Arabidopsis thaliana* | NCBITaxon:3702 | PEX13 | Woodward 2014, PMID:25008153 — *"A viable Arabidopsis pex13 missense allele confers severe peroxisomal defects"* |
| *Magnaporthe oryzae* | NCBITaxon:318829 | MoPEX13 | Wang 2019, PMID:30905264 — Δmopex13 nonpathogenic; peroxisomal docking required for fungal virulence |
| *Trypanosoma brucei* | NCBITaxon:5691 | Pex13.1 / **Pex13.2** | Uniquely has **two** Pex13 paralogues (Crowe 2020, PMID:32075879); glycosome biogenesis; a drug target |

**Breed (VBO):** not applicable — no affected breed exists.

### Comparative biology

PEX13's role in matrix-protein docking is **conserved across the entire eukaryotic domain** — yeast, plants, filamentous fungi, kinetoplastids, fish, and mammals all require it for peroxisome/glycosome matrix import. Liu et al. 1999 exploited this directly: *"This mutation attenuated the activity of human PEX13, and an analogous mutation in yeast PEX13 also reduced its activity"* — cross-species functional conservation used as evidence of pathogenicity in a human patient. That is a legitimate and citable use of comparative biology as evidence.

Divergences worth noting: trypanosomes' duplication into Pex13.1/Pex13.2 with subfunctionalization; and *Arabidopsis* pex13 nulls being embryonic-lethal while a missense allele is viable.

**Zoonotic potential / cross-species transmission:** not applicable — a Mendelian disorder.

---

## 15. Model Organisms

PEX13 is unusually well served by mouse genetics, largely through Denis Crane's group at Griffith University, who built a conditional allele and then interrogated the CNS phenotype in depth. Both models should be curated as `animal_models:` with `modeled_mechanisms` links.

### 15.1 Constitutive Pex13 knockout mouse — the PBD11A model

**Maxwell et al. 2003, Mol Cell Biol 23(16):5947-57, PMID:12897163.** *loxP*-modified Pex13 crossed to a ubiquitous Cre.

> *"The mutant pups exhibited many of the clinical features of Zellweger syndrome patients, including intrauterine growth retardation, severe hypotonia, failure to feed, and neonatal death. These animals lacked morphologically intact peroxisomes and showed deficient import of matrix proteins containing either type 1 or type 2 targeting signals. Biochemical analyses of tissue and cultured skin fibroblasts from these animals indicated severe impairment of peroxisomal fatty acid oxidation and plasmalogen synthesis. The brains of these animals showed disordered lamination in the cerebral cortex, consistent with a neuronal migration defect. Thus, Pex13(-/-) mice reproduce many of the features of Zellweger syndrome and PEX13 deficiency in humans."*

**Suggested `ModelMechanismLink` set:**
- → *Collapse of Peroxisomal Matrix Protein Import*: `RECAPITULATES`, fidelity `HIGH`. Readouts: PTS1 and PTS2 import (DECREASED); intact peroxisomes (ABOLISHED).
- → *Failure of peroxisomal β-oxidation* / *plasmalogen deficiency*: `RECAPITULATES`, fidelity `HIGH`.
- → *Cortical dysplasia / neuronal migration defect*: `RECAPITULATES`, fidelity `MODERATE` — mouse shows disordered lamination but not the human polymicrogyria pattern precisely.
- → *Neonatal lethality*: `RECAPITULATES`, fidelity `HIGH`.
- `limitations`: neonatal lethality precludes study of postnatal progression, liver fibrosis, sensory loss, and any long-term therapeutic endpoint. This is exactly why the conditional model below was built.

### 15.2 Brain-restricted (Nestin-Cre) Pex13 conditional knockout — the neuropathogenesis model

**Müller et al. 2011, Dis Model Mech 4(1):104-19, PMID:20959636** — *"PEX13 deficiency in mouse brain as a model of Zellweger syndrome: abnormal cerebellum formation, reactive gliosis and oxidative stress."* Nestin-Cre drives Cre in neuronal-lineage cells. Mutants **survive into the postnatal period, most dying by P35**, with survival inversely related to litter size and weaning body weight. Defects in reflex and motor development correlate with impaired cerebellar fissure and cortical layer formation, granule cell migration, and Purkinje cell layer development.

**The single most important finding for mechanism curation:** *"The impact on peroxisomal metabolism in the mutant brain is mixed: plasmalogen content is reduced, but very-long-chain fatty acids are normal."* This dissociates the two canonical peroxisomal metabolites and argues the CNS phenotype tracks **plasmalogen deficiency**, not VLCFA accumulation.

Subsequent work on the same model:

| Study | PMID | Finding |
|---|---|---|
| Rahim 2014, *Neuroscience* 274:229-41 | 24881576 | Central serotonergic deficiency: reduced TPH2, *"dysmorphic 5-HT-positive neurons, abnormal distribution of 5-HT neurons, and dystrophic serotonergic axons"*; raphe apoptosis and gliosis |
| Rahim 2016, *Neuroscience* 334:201-213 | 27514574 | *"expanded and morphologically modified brain mitochondrial population"*; fibroblasts show *"increased levels of mitochondrial superoxide and membrane depolarization"*, **rescued by antioxidant**; lipid and DNA oxidation products in neurons and glia |
| Rahim 2018, *Mol Cell Neurosci* 88:16-32 | 29187321 | *"enlarged lateral ventricles and aberrant cortical, hippocampal and hypothalamic organization"*; reduced neural progenitor proliferation/migration/differentiation E12.5→P3; **reactive gliosis from E14.5**; increased cell death |

**`modeled_mechanisms` guidance:** link this model to *Impaired neurogenesis / neuronal migration*, *Secondary mitochondrial dysfunction and oxidative stress*, and *Hypomyelination*. For the **serotonergic** node use `relationship: RECAPITULATES` **but** pair it with a `HUMAN_MODEL_MISMATCH` discussion — no human ZSD brain has been shown to have a serotonergic deficit. For **VLCFA in brain**, the appropriate relationship is `FAILS_TO_RECAPITULATE` (brain VLCFA normal in the mouse while elevated in human plasma) — a substantive negative claim, so it requires both `limitations` and `evidence` per the repo's rule.

### 15.3 Hepatocyte-specific Pex13 knockout

**Rishi et al. 2020, PMID:32565019** — liver-restricted deletion produced *"decreased hepcidin expression"* through increased SMAD7 signalling and ER stress, *"establishing a novel connection between peroxisomal function and iron regulation."* Link to a hepatic node; fidelity `MODERATE`; the iron phenotype has **not** been confirmed in human ZSD — another `HUMAN_MODEL_MISMATCH` candidate.

### 15.4 Zebrafish

**Demers et al. 2023, Autophagy 19(6):1781-1802, PMID:36541703** used *"gene editing and quantitative fluorescence microscopy on culture cells and a zebrafish model system"* to establish PEX13 as a pexophagy brake. This is the model system underpinning the hydroxychloroquine trial (`NCT03856866`). Curate as `animal_models:` (zebrafish is an animal — **not** `experimental_models:`), linked to the *Enhanced pexophagy* node with `relationship: PERTURBS`.

### 15.5 Cellular and in vitro systems

| System | Use | Reference |
|---|---|---|
| **Patient skin fibroblasts** | The diagnostic and functional workhorse: catalase/PMP70 immunofluorescence, complementation, temperature-sensitivity testing, mitochondrial phenotyping | Liu 1999; Shimozawa 1999; Krause 2013; Borgia 2022 |
| **PEX13-defective CHO mutant (ZP-series)** | Complementation assay used to demonstrate I326T temperature sensitivity | Shimozawa 1999, PMID:10332040 |
| **Live-cell FRET / co-IP in mammalian cells** | Established PEX13 homo-oligomerization and mapped W313's role | Krause 2013, PMID:23716570 |
| **CRISPR-edited cell lines** | Pexophagy and selective-autophagy work | Demers 2023; Lee 2017 |
| **Yeast (*S. cerevisiae*, *H. polymorpha*)** | Original peroxin genetics; the platform on which "an analogous mutation in yeast PEX13 also reduced its activity" was shown | Liu 1999; Thomas 2018 |
| **In vitro reconstitution / LLPS** | The 2023 phase-separation channel model | Ravindran 2023, PMID:37165185 |

**Note on the repo's `experimental_models:` vs `animal_models:` split:** fibroblasts, CHO cells, and edited cell lines go in `experimental_models:`; mouse and zebrafish go in `animal_models:`. Both now reach the pathograph through `ModelMechanismLink`, so the older `experimental_model_type: OTHER` workaround for animals is not needed.

### 15.6 Model limitations (aggregate)

1. **The constitutive KO dies neonatally**, so it cannot model progressive liver disease, sensory loss, adrenal insufficiency, or any long-term therapeutic endpoint.
2. **The brain-restricted model has normal brain VLCFA**, so it cannot test VLCFA-lowering strategies for CNS disease.
3. **No mouse carries a human PEX13 missense allele.** Every published human missense (R294W, W313G, I326T, A165P, G324R) has been characterized in cells or *in silico*, never in an animal. There is no model of the *hypomorphic/temperature-sensitive* genotype class — which is precisely the class that biogenesis-stimulating therapy would target. This is a concrete, nameable gap.
4. **No naturally occurring animal disease** exists for comparative pathology.
5. Human-specific neurodevelopmental features (outer radial glia, gyral complexity) are absent in mouse, limiting the fidelity of any cortical-malformation readout.

### 15.7 Model databases

MGI (Pex13, conditional and null alleles), IMPC, IMSR, ZFIN (pex13), SGD (*PEX13*), TAIR (*Arabidopsis PEX13*), Alliance of Genome Resources, Cellosaurus (CHO ZP-series peroxisome-deficient lines).

---

## Curation Notes for the dismech Entry

A few things I'd flag before this becomes YAML:

1. **The `parents:` field currently says `Peroxisome Biogenesis Disorder`.** Given that `Zellweger_Spectrum_Disorders.yaml`, `Peroxisome_Biogenesis_Disorder_1B.yaml`, `Peroxisome_Biogenesis_Disorder_3A_Zellweger.yaml`, and `Peroxisome_Biogenesis_Disorder_4B.yaml` all already exist in `kb/disorders/`, check the parent choice and cross-entry consistency against those before committing — and consider whether a `kb/groupings/` record for the PEX-gene-stratified ZSD entries is warranted.
2. **Every CURIE in this report except the §3.1 HPO block is unvalidated.** Run `just validate-terms` and fix or drop rather than binding a plausible-looking ID. The CHEBI metabolite terms and several HP terms I marked "verify" are the highest-risk.
3. **Snippets:** the fully verbatim abstracts I retrieved are Liu 1999 (PMID:10441568), Shimozawa 1999 (PMID:10332040), Al-Dirbashi 2009 (PMID:19449432), Maxwell 2003 (PMID:12897163), Borgia 2022 (PMID:35854306), Demers 2023 (PMID:36541703), Krause 2013 (PMID:23716570), and Su 2024 (PMID:37962062) — those quotes should validate directly. Quotes from the other PMIDs came through a summarizing fetcher with a quote-length cap; **re-fetch via `just fetch-reference` and re-verify each before use.**
4. **Named Entity Confusion risk is real for this gene** in two directions: the 2p15 microdeletion literature (XPO1/USP34, not peroxisomal) and the PEX13-as-tumour-biomarker literature. Both surface in a naive PEX13 search. Run `just preflight-dr` before ingesting any deep-research output for this disease.
5. **`evidence_source` discipline:** most of the mechanistic depth here is `MODEL_ORGANISM` (Crane-lab mice) or `IN_VITRO` (fibroblast/CHO complementation). The human clinical layer is thin — 9 pedigrees. Don't let mouse evidence carry a human phenotype claim.

---

## Sources

**Primary literature (PEX13-specific)**
- [Liu Y et al. PEX13 is mutated in complementation group 13 of the peroxisome-biogenesis disorders. Am J Hum Genet. 1999;65(3):621-34. PMID:10441568](https://pubmed.ncbi.nlm.nih.gov/10441568/)
- [Shimozawa N et al. Nonsense and temperature-sensitive mutations in PEX13 are the cause of complementation group H of peroxisome biogenesis disorders. Hum Mol Genet. 1999;8(6):1077-83. PMID:10332040](https://pubmed.ncbi.nlm.nih.gov/10332040/)
- [Maxwell M et al. Pex13 inactivation in the mouse disrupts peroxisome biogenesis and leads to a Zellweger syndrome phenotype. Mol Cell Biol. 2003;23(16):5947-57. PMID:12897163](https://pubmed.ncbi.nlm.nih.gov/12897163/)
- [Al-Dirbashi OY et al. Zellweger syndrome caused by PEX13 deficiency: report of two novel mutations. Am J Med Genet A. 2009;149A(6):1219-23. PMID:19449432](https://pubmed.ncbi.nlm.nih.gov/19449432/)
- [Müller CC et al. PEX13 deficiency in mouse brain as a model of Zellweger syndrome. Dis Model Mech. 2011;4(1):104-19. PMID:20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/)
- [Krause C et al. Functional analysis of PEX13 mutation in a Zellweger syndrome spectrum patient reveals novel homooligomerization of PEX13. Hum Mol Genet. 2013;22(19):3844-57. PMID:23716570](https://pubmed.ncbi.nlm.nih.gov/23716570/)
- [Rahim RS et al. Central serotonergic neuron deficiency in a mouse model of Zellweger syndrome. Neuroscience. 2014;274:229-41. PMID:24881576](https://pubmed.ncbi.nlm.nih.gov/24881576/)
- [Rahim RS et al. Mitochondrial changes and oxidative stress in a mouse model of Zellweger syndrome neuropathogenesis. Neuroscience. 2016;334:201-13. PMID:27514574](https://pubmed.ncbi.nlm.nih.gov/27514574/)
- [Lee MY et al. Peroxisomal protein PEX13 functions in selective autophagy. EMBO Rep. 2017;18(1):48-60. PMID:27827795](https://pubmed.ncbi.nlm.nih.gov/27827795/)
- [Rahim RS et al. Impaired neurogenesis and associated gliosis in mouse brain with PEX13 deficiency. Mol Cell Neurosci. 2018;88:16-32. PMID:29187321](https://pubmed.ncbi.nlm.nih.gov/29187321/)
- [Rishi G et al. Hepatocyte-specific deletion of peroxisomal protein PEX13 results in disrupted iron homeostasis. Biochim Biophys Acta Mol Basis Dis. 2020;1866(10):165882. PMID:32565019](https://pubmed.ncbi.nlm.nih.gov/32565019/)
- [Borgia P et al. Genotype-phenotype correlations and disease mechanisms in PEX13-related Zellweger spectrum disorders. Orphanet J Rare Dis. 2022;17(1):286. PMID:35854306](https://pmc.ncbi.nlm.nih.gov/articles/PMC9295491/)
- [Demers ND et al. PEX13 prevents pexophagy by regulating ubiquitinated PEX5 and peroxisomal ROS. Autophagy. 2023;19(6):1781-802. PMID:36541703](https://pubmed.ncbi.nlm.nih.gov/36541703/)
- [Ravindran R et al. Peroxisome biogenesis initiated by protein phase separation. Nature. 2023;617(7961):608-15. PMID:37165185](https://pubmed.ncbi.nlm.nih.gov/37165185/)
- [Su L et al. Severe Zellweger spectrum disorder due to a novel missense variant in the PEX13 gene. Mol Genet Genomic Med. 2024;12(1):e2315. PMID:37962062](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.2315)
- [Dong SS et al. A case of Zellweger syndrome caused by PEX13 gene variation. Zhonghua Er Ke Za Zhi. 2024;62(4):376-8. PMID:38527511](https://pubmed.ncbi.nlm.nih.gov/38527511/)
- [Vinoy N et al. Loss of peroxisomal membrane proteins PEX13 and PEX14 disrupts fatty acid oxidation and drives lipid imbalance. Biosci Rep. 2026. PMID:41860470](https://pubmed.ncbi.nlm.nih.gov/41860470/)

**Zellweger spectrum — clinical, epidemiologic, therapeutic**
- [Steinberg SJ, Raymond GV, Braverman NE, Moser AB. Zellweger Spectrum Disorder. GeneReviews. Updated 2020-10-29. PMID:20301621](https://www.ncbi.nlm.nih.gov/books/NBK1448/)
- [Klouwer FCC et al. Zellweger spectrum disorders: clinical overview and management approach. Orphanet J Rare Dis. 2015;10:151. PMID:26627182](https://pmc.ncbi.nlm.nih.gov/articles/PMC4666198/)
- [Braverman NE et al. Peroxisome biogenesis disorders in the Zellweger spectrum. Mol Genet Metab. 2016;117(3):313-21. PMID:26750748](https://pubmed.ncbi.nlm.nih.gov/26750748/)
- [Berendse K et al. High prevalence of primary adrenal insufficiency in Zellweger spectrum disorders. Orphanet J Rare Dis. 2014;9:133. PMID:25179809](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4164755/)
- [Berendse K et al. Cholic acid therapy in Zellweger spectrum disorders. J Inherit Metab Dis. 2016;39(6):859-68. PMID:27469511](https://pubmed.ncbi.nlm.nih.gov/27469511/)
- [Klouwer FCC et al. Development and validation of a severity scoring system for Zellweger spectrum disorders. Clin Genet. 2018;93(3):613-21. PMID:28857144](https://pubmed.ncbi.nlm.nih.gov/28857144/)
- [Paker AM et al. Docosahexaenoic acid therapy in peroxisomal diseases: results of a double-blind, randomized trial. Neurology. 2010;75(9):826-30. PMID:20805528](https://n.neurology.org/content/75/9/826)
- [Heubi JE, Bishop WP. Long-Term Cholic Acid Treatment in a Patient with Zellweger Spectrum Disorder. Case Rep Gastroenterol. 2018;12(3):661-70. PMID:30519152](https://pubmed.ncbi.nlm.nih.gov/30519152/)
- [Bose M et al. Zellweger spectrum disorder: A cross-sectional study of symptom prevalence using input from family caregivers. Mol Genet Metab Rep. 2020;25:100694. PMID:33335840](https://www.sciencedirect.com/science/article/pii/S2214426920301403)
- [Bose M et al. Comparison of Caregiver-Reported Dietary Intake Methods in Zellweger Spectrum Disorder. Nutrients. 2025;17(6):989. PMID:40290032](https://pubmed.ncbi.nlm.nih.gov/40290032/)
- [Malone KE et al. Estimation of PEX1-mediated Zellweger spectrum disorder births and population prevalence by population genetics modeling. Genet Med Open. 2025;3:103431. PMID:40519747](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12166394/)
- [Fazi C et al. Case Report: Zellweger Syndrome and Humoral Immunodeficiency. Front Pediatr. 2022;10:852943. PMID:35402347](https://pubmed.ncbi.nlm.nih.gov/35402347/)
- [Plasma C24:0- and C26:0-lysophosphatidylcholines are reliable biomarkers for the diagnosis of peroxisomal β-oxidation disorders. J Lipid Res. 2024.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10910329/)
- [Improved analysis of C26:0-lysophosphatidylcholine in dried-blood spots for X-ALD newborn screening. PMID:22503909](https://pubmed.ncbi.nlm.nih.gov/22503909/)
- [Newborn Screening for X-ALD: Biochemical, Molecular, and Clinical Characteristics of Other Genetic Conditions. PMC11275617](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11275617/)

**Databases and reference resources**
- [OMIM #614883 — Peroxisome Biogenesis Disorder 11A (Zellweger)](https://omim.org/entry/614883) · [OMIM *601789 — PEX13](https://www.omim.org/entry/601789) · [OMIM #614885 — PBD11B](https://omim.org/entry/614885)
- [Orphanet: Zellweger syndrome (ORPHA:912)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=912)
- [HPO annotations for OMIM:614883](https://ontology.jax.org/api/network/annotation/OMIM:614883)
- [ClinVar RCV000008142 — PEX13 c.702G>A (p.Trp234Ter), PBD11A](https://www.ncbi.nlm.nih.gov/clinvar/RCV000008142/) · [ClinVar RCV000274515 — PEX13 c.260A>G (p.Asn87Ser), PBD11A](https://www.ncbi.nlm.nih.gov/clinvar/RCV000274515/)
- [UniProt Q92968 — Peroxisomal membrane protein PEX13](https://rest.uniprot.org/uniprotkb/Q92968.txt) · [NCBI Gene 5194 — PEX13](https://www.ncbi.nlm.nih.gov/gene/5194)
- [HRSA Newborn Screening — Zellweger Spectrum Disorder](https://newbornscreening.hrsa.gov/conditions/zellweger-spectrum-disorder) · [StatPearls — Zellweger Spectrum Disorder](https://www.ncbi.nlm.nih.gov/books/NBK560676/) · [NORD — Zellweger Spectrum Disorders](https://rarediseases.org/rare-diseases/zellweger-spectrum-disorders/)
- [FDA Cholbam approval package, NDA 205750 (2015-03-17)](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2015/205750Orig1s000Approv.pdf)
- ClinicalTrials.gov: [NCT01668186](https://clinicaltrials.gov/study/NCT01668186) · [NCT03856866](https://clinicaltrials.gov/study/NCT03856866) · [NCT01838941](https://clinicaltrials.gov/study/NCT01838941) · [NCT06190626](https://clinicaltrials.gov/study/NCT06190626) · [NCT03440905](https://clinicaltrials.gov/study/NCT03440905) · [NCT03115086](https://clinicaltrials.gov/study/NCT03115086)
- [ICD-10-CM E71.510 — Zellweger syndrome](https://www.icd10data.com/ICD10CM/Codes/E00-E89/E70-E88/E71-/E71.510)

---

**Next step:** the highest-value single action is to run `just fetch-reference` over the ~20 PMIDs above so the snippets are cache-verified before any of this goes into the YAML — several of my quotes came through a fetcher with a quote-length cap and need re-verification. Say the word and I'll do that pass and report which snippets survive.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 49 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 49 |
| On topic | 32 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 106 |
| Resolved | 99 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 6 |
| Terms whose name was checked | 70 |
| Terms named correctly | 46 |
| Terms named as a **different** term | 17 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013949` (3 mentions) - the report calls it "MONDO"; MONDO calls it **peroxisome biogenesis disorder 11A (Zellweger)**
- `DOID:0080485` (1 mention) - the report calls it "DOID"; DOID calls it **peroxisome biogenesis disorder 11A**
- `HP:0002104` (2 mentions) - the report calls it "Apnea", "a proximate cause of neonatal death"; HP calls it **Apnea**
- `HP:0002421` (1 mention) - the report calls it "verify"; HP calls it **Poor head control**
- `HP:0000934` (1 mention) - the report calls it "verify"; HP calls it **Chondrocalcinosis**
- `HP:0002269` (1 mention) - the report calls it "verify"; HP calls it **Abnormality of neuronal migration**
- `HP:0034512` (1 mention) - the report calls it "verify"; HP calls it **Transitional-cell carcinoma of the ureter**
- `GO:0018882` (1 mention) - the report calls it "verify"; GO calls it **obsolete (+)-camphor metabolic process**
- `UBERON:0001474` (1 mention) - the report calls it "Skeleton"; UBERON calls it **bone element**
- `UBERON:0010363` (1 mention) - the report calls it "verify"; UBERON calls it **endochondral element**
- `UBERON:0001091` (1 mention) - the report calls it "verify"; UBERON calls it **calcareous tooth**
- `CL:0000120` (1 mention) - the report calls it "verify"; CL calls it **granule cell**
- `CL:0000850` (1 mention) - the report calls it "verify"; CL calls it **serotonergic neuron**
- `CL:0000210` (1 mention) - the report calls it "verify"; CL calls it **photoreceptor cell**
- `NCIT:C15329` (2 mentions) - the report calls it "ZSD cataracts; early surgery where feasible"; NCIT calls it **Surgical Procedure**
- `NCIT:C15747` (3 mentions) - the report calls it "Enamel hypoplasia in *"nearly all patients"; NCIT calls it **Supportive Care**
- `NCBITaxon:4903` (1 mention) - the report calls it "verify"; NCBITaxon calls it **Williopsis jadinii**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0018882` (obsolete (+)-camphor metabolic process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0032807` (1 mention) - the report calls it "Neonatal seizure — **verify"; HP calls it **Neonatal seizure**
- `HP:0002510` (1 mention) - the report calls it "Spastic tetraparesis"; HP calls it **Spastic tetraplegia**
- `CL:0000047` (2 mentions) - the report calls it "Neural stem/progenitor cell"; CL calls it **neural stem cell**
- `UBERON:0002316` (2 mentions) - the report calls it "Cerebral white matter"; UBERON calls it **white matter**, and lists "neuronal white matter" among its other names
- `UBERON:0001846` (1 mention) - the report calls it "Inner ear"; UBERON calls it **internal ear**, and lists "inner ear" among its other names
- `CL:0000057` (1 mention) - the report calls it "Skin fibroblast"; CL calls it **fibroblast**
- `NCBITaxon:318829` (1 mention) - the report calls it "Magnaporthe oryzae"; NCBITaxon calls it **Pyricularia oryzae**, and lists "Magnaporthe oryzae" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000007` - called "Autosomal recessive inheritance", "Inheritance:** autosomal recessive"
- `HP:0002104` - called "Apnea", "a proximate cause of neonatal death"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `NC_000002.12`, `ORPHA`, `OMIM`, `LOINC`.