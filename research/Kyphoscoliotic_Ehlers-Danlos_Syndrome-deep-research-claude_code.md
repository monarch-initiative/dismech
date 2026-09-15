---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-15T21:18:15.840395'
end_time: '2026-09-15T21:23:17.878266'
duration_seconds: 302.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Kyphoscoliotic Ehlers-Danlos Syndrome
  mondo_id: MONDO:0016002
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
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 24
  total_cost_usd: 1.5827674000000005
  session_id: c3b3f1c9-a24d-5e2f-85c1-b82995c77b75
  stop_reason: end_turn
  assistant_text_blocks: 3
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
citation_count: 22
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 51
  verified: 46
  not_found: 0
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 42
  labels_matching: 21
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0100775
    reported_labels:
    - Umbilical hernia
    ontology_label: Dural ectasia
  - term_id: HP:0025214
    reported_labels:
    - Arterial dissection
    ontology_label: Triggered by heat
  - term_id: HP:0004349
    reported_labels:
    - Osteopenia
    ontology_label: Reduced bone mineral density
  - term_id: HP:0000023
    reported_labels:
    - Congenital contractures
    ontology_label: Inguinal hernia
  - term_id: HP:0000539
    reported_labels:
    - Refractive errors
    ontology_label: Abnormality of refraction
  - term_id: HP:0003198
    reported_labels:
    - Myopathy (mild, nonspecific histopathology)
    ontology_label: Myopathy
  - term_id: CL:0000057
    reported_labels:
    - "fibroblast \u2014 dermal fibroblasts are the principal cell studied biochemically"
    ontology_label: fibroblast
  - term_id: UBERON:0001846
    reported_labels:
    - cochlea, FKBP14 subtype
    ontology_label: internal ear
  - term_id: NCIT:C2231
    reported_labels:
    - Adrenergic beta-Antagonist
    ontology_label: Dofequidar Fumarate
  labels_variant: 12
  obsolete_terms:
  - term_id: HP:0005692
    ontology_label: obsolete Joint hyperflexibility
    replaced_by: HP:0001382
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  unresolvable_prefixes:
  - ORPHA
  - OMIA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kyphoscoliotic Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0016002 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Kyphoscoliotic Ehlers-Danlos Syndrome** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I'll research Kyphoscoliotic Ehlers-Danlos Syndrome using authoritative sources and compile the comprehensive report now.

I have enough authoritative data to compile a comprehensive report. Let me do a couple more targeted searches to round out treatment/prevention and MONDO/UBERON mapping, then write the final report.

# Comprehensive Research Report: Kyphoscoliotic Ehlers-Danlos Syndrome (kEDS)

## Executive Summary

Kyphoscoliotic Ehlers-Danlos syndrome (kEDS) is a rare autosomal recessive heritable connective tissue disorder classified in Group 7 ("collagen spatial structure and cross-linking defects") of the 2017 International EDS Classification (Malfait et al., 2017, *Am J Med Genet C Semin Med Genet* 175:8-26, PMID not fully captured in search but DOI: 10.1002/ajmg.c.31552). It is genetically heterogeneous, with **two molecularly distinct but clinically overlapping subtypes**: **kEDS-PLOD1** (formerly EDS type VIA, OMIM #225400) caused by biallelic *PLOD1* variants, and **kEDS-FKBP14** (formerly EDS type VIB, OMIM #614557) caused by biallelic *FKBP14* variants. Both converge on defective collagen post-translational modification/folding, producing congenital hypotonia, progressive kyphoscoliosis, joint hypermobility, skin fragility, and a risk of life-threatening arterial rupture.

---

## 1. Disease Information

**Overview:** kEDS is a rare, genetically heterogeneous, autosomal recessive disorder of collagen biosynthesis. It presents at birth with severe muscular hypotonia, generalized joint hypermobility with recurrent dislocations, and congenital or early-onset kyphoscoliosis that is often rapidly progressive. Skin is soft, hyperextensible, and fragile (atrophic scarring, easy bruising), and there is risk of ocular globe (scleral) fragility and, in adulthood, spontaneous rupture/dissection of medium-sized arteries. Intelligence is typically normal.

**Key Identifiers:**
- **MONDO:** MONDO:0016002 (Ehlers-Danlos syndrome, kyphoscoliotic type 1 / EDS type VIA / oculoscoliotic type), grouped with the FKBP14-related subtype under the umbrella "kyphoscoliotic EDS"
- **OMIM:** #225400 (EDSKSCL1, PLOD1-related) and #614557 (EDSKSCL2, FKBP14-related)
- **Orphanet:** ORPHA:1900 (kEDS due to lysyl hydroxylase 1 deficiency), ORPHA:300179 (kEDS due to FKBP22/FKBP14 deficiency)
- **Genes/HGNC:** *PLOD1* (HGNC gene, chromosome 1p36.22); *FKBP14* (HGNC gene, chromosome 7p14.3)
- **Prior nomenclature:** EDS type VI, EDS type VIA/VIB, "oculoscoliotic type" EDS (Berlin/Villefranche nosologies)

**Synonyms:** Ehlers-Danlos syndrome, kyphoscoliotic type; EDS VI; EDS VIA (PLOD1) / EDS VIB (FKBP14); lysyl hydroxylase deficiency; oculoscoliotic EDS.

**Data source note:** This body of knowledge is derived almost entirely from aggregated case reports and small case series (individual patients, n=1–23 per cohort) rather than large population-level registries, reflecting the rarity of the condition; the largest cohorts are the FKBP14 natural-history study of 17 patients (Giunta et al., *Genet Med* 2018, PMC5763155) and the PLOD1 series analyzed across ~94 published individuals cited in GeneReviews.

Source: [PLOD1-Related Kyphoscoliotic Ehlers-Danlos Syndrome – GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [FKBP14 Kyphoscoliotic Ehlers-Danlos Syndrome – GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK541503/); [OMIM #225400](https://www.omim.org/entry/225400); [OMIM #614557](https://www.omim.org/entry/614557)

---

## 2. Etiology

### Disease Causal Factors
kEDS is purely **genetic/monogenic**, autosomal recessive, with two known causal genes:
- **PLOD1** (~most cases): encodes lysyl hydroxylase 1 (LH1/PLOD1), which hydroxylates lysyl residues in the collagen triple helix.
- **FKBP14**: encodes FKBP22, an ER-resident peptidyl-prolyl cis-trans isomerase (PPIase) that acts as a collagen chaperone (types III, VI, X).

Both loss-of-function mechanisms converge on defective collagen fibril assembly/cross-linking, producing a phenotypically overlapping but molecularly distinct disease.

### Risk Factors
- **Genetic:** Biallelic (homozygous or compound heterozygous) pathogenic variants in *PLOD1* or *FKBP14* are necessary and sufficient. Consanguinity substantially raises risk given the recessive, often founder-driven allele pool (see Section 9).
- **No established environmental/infectious/lifestyle causal risk factors** — this is a purely Mendelian condition; environmental exposures (mechanical trauma, pregnancy, high-impact activity) act as **modifiers/precipitants of complications** (fractures, vascular rupture, globe rupture) rather than causal risk factors for the underlying disease.
- **Modifier genes:** No confirmed modifier loci; phenotypic variability is attributed largely to residual enzyme activity from different allele combinations and partial compensation by paralogous enzymes (LH2/PLOD2, LH3/PLOD3 for PLOD1; unknown compensators for FKBP14).

### Protective Factors
No genetic or environmental protective factors are established in the literature reviewed.

### Gene-Environment Interactions
Not formally studied; the clinically relevant interaction is mechanical — connective tissue that is structurally weakened by defective cross-linking is disproportionately vulnerable to mechanical stress (trauma, childbirth, high-impact exercise, hypertension-driven arterial wall stress), which precipitates the organ-specific complications (globe rupture, arterial dissection, joint dislocation) rather than initiating the underlying molecular lesion.

Source: [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/)

---

## 3. Phenotypes

### PLOD1-kEDS (n≈94 published individuals, cumulative literature)

| Phenotype | HPO term (suggested) | Frequency | Onset |
|---|---|---|---|
| Congenital muscular hypotonia | HP:0001290 (Generalized hypotonia) | 100% | Birth |
| Kyphoscoliosis (congenital/early-onset, often progressive) | HP:0002751 (Kyphoscoliosis) | 95% | Infancy, worsening through childhood |
| Skin hyperextensibility/fragility, atrophic scarring | HP:0000974 (Hyperextensible skin); HP:0000978 (Bruising susceptibility) | 97% | Infancy onward |
| Generalized joint hypermobility, recurrent dislocations/subluxations | HP:0001382 (Joint hypermobility) | ~30% recurrent dislocations | Childhood |
| Ocular abnormality (blue sclerae, refractive error, scleral/globe fragility) | HP:0000592 (Blue sclerae); HP:0000587 (Keratoglobus) | 45% | Variable; globe rupture risk lifelong |
| Congenital or acquired clubfoot | HP:0001762 (Talipes equinovarus) | ~20-25% | Congenital |
| Hernias (umbilical/inguinal) | HP:0100775 (Umbilical hernia) | ~15% | Childhood |
| Gross motor developmental delay | HP:0001270 | ~60% | Infancy |
| Arterial rupture/dissection (medium-sized arteries, aorta) | HP:0025214 (Arterial dissection) | ~30% (adults) | Adulthood, life-threatening |
| Osteopenia | HP:0004349 | Common | Adolescence onward |

### FKBP14-kEDS (cohort n=23, Giunta et al. 2018/GeneReviews)

| Phenotype | HPO term (suggested) | Frequency |
|---|---|---|
| Congenital hypotonia/weakness (improves in childhood) | HP:0001252 (Hypotonia) | 23/23 |
| Small-joint hypermobility | HP:0005692 | 23/23 |
| Large-joint hypermobility | HP:0001382 | 21/23 |
| Foot deformities | HP:0001760 | 23/23 |
| Congenital contractures | HP:0000023 | 7/23 |
| Refractive errors | HP:0000539 | ~2/3 |
| Blue sclerae | HP:0000592 | ~1/3 |
| Hernias | HP:0002664/HP:0100775 | 11/23 |
| Bifid uvula ± cleft palate | HP:0000193 (Bifid uvula) | 7/23 |
| Sensorineural hearing loss | HP:0000407 | ~50% |
| Conductive hearing loss | HP:0000405 | ~18-25% |
| Myopathy (mild, nonspecific histopathology) | HP:0003198 | Frequent |
| Aortic/arterial rupture, dissection, pseudoaneurysm | HP:0002647 | Occasional |

**Severity/Progression:** In both subtypes, kyphoscoliosis is often rapidly progressive in early childhood and frequently refractory to bracing, necessitating early surgical stabilization. Motor function trajectory differs somewhat by subtype: FKBP14-kEDS patients typically show improving hypotonia and achieve independent ambulation by age 2–4, with a possible **decline in motor function in adulthood** while retaining independence in activities of daily living. PLOD1-kEDS patients typically walk by age 2.

**Quality of life impact:** No disease-specific validated QoL instrument data were identified in the literature searched; morbidity is dominated by progressive spinal deformity (restrictive lung disease risk), chronic joint instability/pain, visual impairment from ocular fragility/refractive error, and (for FKBP14) hearing impairment — each independently affecting daily functioning, mobility, and educational/occupational participation.

Source: [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/); [Phenotypic variability of EDS VIA (PMC3135503)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3135503/); [Giunta et al. 2018 cohort, Genetics in Medicine](https://www.nature.com/articles/gim201770)

---

## 4. Genetic/Molecular Information

### Causal Genes
- **PLOD1** — procollagen-lysine, 2-oxoglutarate 5-dioxygenase 1 (lysyl hydroxylase 1, LH1). Chromosome 1p36.22. OMIM gene entry *153454.
- **FKBP14** — FK506-binding protein 14 (FKBP22). Chromosome 7p14.3.

### Pathogenic Variants — PLOD1
- **Variant types:** missense, nonsense, splice-site, small indels, and a **common recurrent 8.9-kb intragenic duplication (exons 10–16)** generated by Alu-Alu recombination in introns 9 and 16 — this single structural variant accounts for ~30% of pathogenic alleles across 73 studied families, making PLOD1-kEDS one of the examples where structural variant testing (deletion/duplication analysis) is essential alongside sequencing.
- Sequence analysis alone detects ~67% of variants; deletion/duplication analysis detects the remaining ~33% (dominated by the 8.9-kb duplication).
- **Recurrent alleles in specific populations:** c.955C>T (p.Arg319Ter), prevalent in Arab populations; c.1533C>G (p.Tyr511Ter), third most common reported variant.
- **Functional consequence:** loss-of-function, producing reduced/absent LH1 enzymatic activity (confirmed on Western blot showing decreased PLOD1 protein).

### Pathogenic Variants — FKBP14
- **c.362dupC** (frameshift, p.Glu122ArgfsTer7) — the dominant founder allele, accounting for **~70% of disease alleles**, shown to share a common haplotype across unrelated affected individuals, consistent with a single ancestral founder event.
- **p.Met48Lys** (missense) — located near the PPIase catalytic active site; structural/functional studies indicate partial loss of isomerase activity (PMC6965642).
- **p.Glu191del** — the only reported in-frame deletion variant.
- Predominantly loss-of-function/null mechanism.

### Variant Classification & Population Frequency
Pathogenic/likely pathogenic classifications for both genes are catalogued in ClinVar (e.g., multiple PLOD1 splice and missense variants linked to "Ehlers-Danlos syndrome, kyphoscoliotic type 1"). Population allele-frequency queries specific to PLOD1/FKBP14 pathogenic alleles were not resolved via general gnomAD searches in this session; given the estimated disease incidence of ~1:100,000 live births and full penetrance under Hardy-Weinberg assumptions, an approximate combined carrier frequency on the order of 1:150–1:160 would be expected for kEDS overall (rough estimate; not a directly sourced figure — recommend confirming against gnomAD v4 directly before curation).

### Modifier Genes
None confirmed. Phenotypic variability in PLOD1-kEDS is proposed to reflect residual LH1 activity and partial functional compensation by the paralogous enzymes LH2 (PLOD2) and LH3 (PLOD3), based on mouse-model biochemistry (see Section 15).

### Epigenetic Information
No disease-specific epigenetic (DNA methylation/histone) studies were identified for kEDS in this search.

### Chromosomal Abnormalities
kEDS is caused by intragenic sequence/structural variants, not whole-chromosome/large segmental aneuploidies; no karyotype-level abnormality is part of the disease definition.

Source: [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/); [UniProt Q02809 (PLOD1)](https://www.uniprot.org/uniprotkb/Q02809/entry); [Baumann et al. 2012, PMC3276673](https://pmc.ncbi.nlm.nih.gov/articles/PMC3276673/); [Met48Lys FKBP22 study, PMC6965642](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6965642/)

---

## 5. Environmental Information

kEDS has **no known environmental, infectious, or toxin-mediated causal factors** — it is a fully penetrant monogenic recessive disease. Environmental/lifestyle factors are relevant only as **triggers of complications** in genetically affected individuals:
- **Mechanical trauma** (even trivial) → corneal/scleral rupture, joint dislocation, arterial rupture.
- **High-impact/contact sports, heavy lifting, joint-stressing activity** (gymnastics, long-distance running) → explicitly counseled against per GeneReviews management guidance, due to joint instability and vascular fragility.
- **Pregnancy** → mechanical/hemodynamic stress increases risk of miscarriage, premature rupture of membranes, and arterial rupture; high-risk perinatology management is recommended for delivery.
- **Hypertension** → accelerates arterial wall stress in a structurally weakened vasculature; blood pressure control and consideration of beta-blockade for aortic dilatation are standard preventive measures.
- **Diagnostic arteriography** is specifically listed as an activity/procedure to avoid except for identification of life-threatening bleeding, given catheter-induced vessel fragility risk.

No infectious agents are implicated in either etiology or as disease triggers.

Source: [GeneReviews PLOD1-kEDS Management](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS Management](https://www.ncbi.nlm.nih.gov/books/NBK541503/)

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain — PLOD1-kEDS

1. **Biallelic loss-of-function variants in *PLOD1*** (missense/nonsense/splice/indel, or the recurrent 8.9-kb Alu-mediated exon 10–16 duplication) → **leads to** markedly reduced or absent lysyl hydroxylase 1 (LH1) enzyme protein/activity in the endoplasmic reticulum (confirmed by reduced protein on Western blot).
2. Loss of LH1 activity → **results in** failure to hydroxylate specific lysyl residues within -Xaa-Lys-Gly- motifs of the collagen triple helix (fibrillar collagens I, III, and others).
3. Underhydroxylation of helical lysines → **leads to** deficient glycosylation of the resulting hydroxylysine residues and, critically, **failure to form mature hydroxylysine-derived pyridinoline (HP) collagen cross-links**; cross-linking instead proceeds via the aberrant, mechanically inferior lysyl-pyridinoline (LP) pathway. This shift is directly measurable: the urinary deoxypyridinoline:pyridinoline (Dpyr:Pyr) ratio rises from a normal ~0.2 to ~6.0 in affected individuals — the diagnostic biochemical hallmark of PLOD1-kEDS.
4. Defective/abnormal collagen cross-linking → **results in** reduced tensile strength and mechanical instability of collagen fibrils in the extracellular matrix (ECM) of connective tissues throughout the body (this step is directly demonstrated biochemically; the downstream tissue-level consequences below are inferred from the clinical phenotype and are consistent with, but not fully mechanistically dissected by, direct human tissue biomechanical studies).
5. Mechanically weakened ECM in **skeletal muscle and fascia** → **leads to** congenital hypotonia and gross motor delay (inferred).
6. Mechanically weakened ECM in **spinal ligaments, intervertebral discs, and paraspinal connective tissue** → **leads to** congenital/early-onset, often rapidly progressive kyphoscoliosis (inferred from clinical pattern; not shown at the histologic level in the sources reviewed).
7. Mechanically weakened ECM in **joint capsules/ligaments** → **leads to** generalized joint hypermobility and recurrent dislocation/subluxation.
8. Mechanically weakened ECM in **dermis** → **leads to** hyperextensible, fragile, easily bruised skin with atrophic ("cigarette-paper") scarring.
9. Mechanically weakened ECM in **the sclera/ocular globe wall** → **leads to** scleral fragility, predisposing to spontaneous or trauma-induced globe rupture, and to refractive error/microcornea from altered corneal biomechanics.
10. Mechanically weakened ECM in **the arterial media/adventitia of medium-sized arteries and the aorta** → **leads to** (in a subset of ~30% of adults) spontaneous arterial aneurysm, dissection, or rupture — the principal life-threatening complication.
11. In severe, progressive kyphoscoliosis (branch from step 6) → **leads to** restrictive pulmonary physiology → **leads to** recurrent pneumonia and, eventually, cor pulmonale/cardiac failure in severely affected adults.

### Ordered Causal Chain — FKBP14-kEDS

1. **Biallelic loss-of-function variants in *FKBP14*** (most commonly the founder c.362dupC frameshift, or missense/in-frame deletion variants) → **leads to** deficiency of the ER-resident chaperone protein FKBP22, a peptidyl-prolyl cis-trans isomerase (PPIase).
2. Loss of FKBP22 PPIase/chaperone activity → **results in** impaired folding of the triple helix of **procollagen type III** (its principal substrate) and disrupted interaction with **collagens VI and X**, while biosynthesis and secretion of collagens I, III, and V per se remain grossly normal — i.e., the defect is primarily one of **folding fidelity and matrix organization**, not synthesis.
3. Defective procollagen folding → **leads to** ER stress with **marked ER cisternal enlargement and accumulation of flocculent material** in dermal fibroblasts (documented ultrastructurally).
4. Impaired collagen III/VI folding and secretion → **results in** disarray of extracellular matrix architecture: disorganized collagen I/III/VI networks, fibronectin, tenascins, and thrombospondin, together with **loss of the principal collagen/fibronectin cell-surface receptors α2β1 and α5β1 integrin** — disrupting normal cell-matrix adhesion signaling.
5. Disorganized ECM/impaired cell-matrix adhesion in **skeletal muscle connective tissue and the muscle fiber environment** → **leads to** the myopathic component of the disease (nonspecific myopathic changes on histopathology, with normal or mildly elevated creatine kinase), and to congenital hypotonia/weakness.
6. Disorganized ECM (largely mirroring the PLOD1 pathway downstream) in **paraspinal tissue, joints, dermis, sclera, and arterial wall** → **leads to** progressive scoliosis, joint hypermobility, hyperelastic skin, ocular fragility, and (occasionally) arterial rupture/dissection, aortic root pathology, and valve insufficiency, by the same general mechanical-weakness logic as steps 6–10 above for PLOD1-kEDS.
7. Collagen VI/III network disruption specifically within the **inner ear/cochlear connective tissue** → **leads to** sensorineural hearing impairment in roughly half of patients (mechanism at the level of cochlear microstructure is not established in the literature identified; this step is inferred from the tissue tropism of the affected collagens and the empirical clinical association, not from direct otopathologic study).

### Molecular Pathways / Cellular Processes / Protein Dysfunction
- **Pathway:** Collagen biosynthesis and post-translational modification (hydroxylation, cross-linking, chaperone-assisted folding) within the rough ER — GO:0032964 (collagen biosynthetic process), GO:0030199 (collagen fibril organization), GO:0018216 (peptidyl-proline hydroxylation), GO:0006457 (protein folding).
- **Protein dysfunction:** PLOD1 — loss-of-function enzymatic deficiency (an ER-membrane-bound homodimer using Fe²⁺ and ascorbate cofactors; functions within a PLOD1–P3H3–P3H4 hydroxylation complex). FKBP14 — loss-of-function chaperone/isomerase deficiency (211-amino-acid protein with signal peptide, PPIase catalytic domain, two EF-hand calcium-binding domains).
- **Cellular process:** ER stress / disrupted secretory pathway trafficking of misfolded/underhydroxylated procollagen (most clearly shown for FKBP14).
- **Tissue damage mechanism:** Mechanical failure of ECM under normal physiologic and mechanical loading (not primary inflammatory, oxidative, or ischemic injury).
- **Immune involvement:** None established; kEDS is not an autoimmune or inflammatory disease.

### Suggested Ontology Terms
- **GO (molecular function):** GO:0031545 (peptidyl-proline dioxygenase activity, LH1) / GO:0003755 (peptidyl-prolyl cis-trans isomerase activity, FKBP14)
- **GO (biological process):** GO:0032964 (collagen biosynthetic process), GO:0030199 (collagen fibril organization), GO:0018216 (peptidyl-proline hydroxylation)
- **GO (cellular component):** GO:0005788 (endoplasmic reticulum lumen), GO:0005789 (ER membrane)
- **CL (cell types):** CL:0000057 (fibroblast — dermal fibroblasts are the principal cell studied biochemically); CL:0000188 (skeletal muscle cell/myocyte); CL:0000192 (smooth muscle cell, arterial media)

### Molecular Profiling
Transcriptome profiling of primary skin fibroblasts has revealed **distinct molecular signatures between PLOD1- and FKBP14-kEDS**, indicating the two genetically-defined subtypes are not simply interchangeable at the transcriptomic level despite convergent clinical phenotypes (PMC6678841). No single-cell, spatial transcriptomic, proteomic, or CRISPR functional-genomics screen datasets specific to kEDS were identified in this search.

Source: [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/); [Transcriptome profiling PLOD1 vs FKBP14, PMC6678841](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6678841/); [UniProt Q02809](https://www.uniprot.org/uniprotkb/Q02809/entry); [FKBP14 mutation original description, Baumann et al. 2012, PMC3276673](https://pmc.ncbi.nlm.nih.gov/articles/PMC3276673/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** integument (skin), musculoskeletal system (spine, joints, muscle), eye (sclera/cornea), vasculature (medium-sized arteries, aorta)
- **Secondary/complication-driven:** respiratory system (restrictive lung disease secondary to kyphoscoliosis), cardiac system (cor pulmonale, valve insufficiency in FKBP14-kEDS), ear (cochlea/middle ear in FKBP14-kEDS), gastrointestinal system (hernias)
- **Body systems:** integumentary, musculoskeletal, ophthalmologic, cardiovascular, respiratory (secondary), auditory (FKBP14 subtype only)

**Tissue/cell level:**
- Dermal connective tissue (dysplastic collagen fibrils; CL:0000057 fibroblast)
- Paraspinal ligamentous/fascial connective tissue
- Joint capsule/ligament connective tissue
- Skeletal muscle interstitial connective tissue and myofibers (myopathy, FKBP14 especially)
- Scleral/corneal stroma (CL type: keratocyte)
- Arterial tunica media/adventitia (CL:0000192 smooth muscle cell)
- Cochlear/inner-ear connective tissue structures (FKBP14)

**Subcellular level:**
- Endoplasmic reticulum (site of collagen hydroxylation/folding defect — GO:0005788/GO:0005789); extracellular matrix / collagen fibril (GO:0062023 collagen-containing extracellular matrix)

**Localization:**
- Systemic/generalized connective tissue involvement rather than focal; no strict lateralization, though joint dislocations and scoliosis curves may present asymmetrically.

**Suggested UBERON terms:** UBERON:0002097 (skin), UBERON:0001630 (muscle organ), UBERON:0001130 (vertebral column), UBERON:0000970 (eye), UBERON:0001981 (blood vessel), UBERON:0000948 (heart), UBERON:0001846 (cochlea, FKBP14 subtype).

Source: synthesized from [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/) and [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/)

---

## 8. Temporal Development

**Onset:** Congenital (present at or shortly after birth) for the cardinal features — hypotonia and kyphoscoliosis/scoliosis. Onset pattern is best characterized as **congenital with early progressive course**, rather than acute or insidious in the adult-onset sense.

**Progression:**
- Kyphoscoliosis: moderate at birth, becoming **moderate to severe during childhood**; often **rapidly progressive and refractory to bracing**, frequently requiring early surgical intervention (growing rods, spinal fusion) rather than conservative management.
- Hypotonia: in FKBP14-kEDS specifically, congenital hypotonia/weakness characteristically **improves during childhood**, with most children achieving independent ambulation between ages 2–4 years; a **decline in motor function may re-emerge in adulthood**.
- Vascular risk (arterial rupture/dissection): emerges predominantly in **adulthood** (~30% lifetime risk in PLOD1-kEDS), though pediatric and adolescent cases have been reported.
- Ocular fragility: lifelong risk, precipitated by trauma.
- Hearing loss (FKBP14): may present at birth, in early infancy, or later in life — variable onset timing.

**Disease course pattern:** Chronic and generally **progressive** for the skeletal and vascular manifestations; the muscular/motor component in FKBP14-kEDS is unusual in following a partially **U-shaped** course (improvement in childhood, decline in adulthood). No remission is described; this is a structural, non-inflammatory connective tissue disorder.

**Disease duration:** Chronic, lifelong. Documented adult survival exists (e.g., one FKBP14-kEDS patient reported alive at age 53), though formal life-expectancy/actuarial data are lacking for both subtypes — see Section 11.

**Critical periods:** Early childhood is the critical intervention window for spinal deformity (curve progression is most rapid and most amenable to surgical stabilization before severe restrictive pulmonary compromise develops); adulthood is the critical surveillance window for arterial complications.

Source: [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/); [Giunta et al. 2018 natural history, Genet Med](https://www.nature.com/articles/gim201770); [FKBP14-kEDS surgical spine case report, 2025, PMC12689754](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12689754/)

---

## 9. Inheritance and Population

**Epidemiology:**
- **PLOD1-kEDS:** exact prevalence unknown; incidence estimated at **~1:100,000 live births** (reasonable estimate per GeneReviews, not derived from a formal population screening study). Geographic clustering has been observed in **Turkey, the Middle East, and Greece**, though no clear racial/ethnic prevalence differential otherwise.
- **FKBP14-kEDS:** rarer still; Orphanet lists point prevalence as **<1/1,000,000 worldwide**; only ~30 individuals were documented in the literature as of the ~2019 GeneReviews synthesis, growing to a natural-history cohort of 17 well-characterized patients (Giunta et al. 2018) plus additional individually reported cases since.

**Inheritance pattern:** Autosomal recessive for both subtypes, with **100% penetrance** as reported by GeneReviews (i.e., biallelic pathogenic variant carriers are expected to manifest the phenotype, though severity varies).

**Expressivity:** Variable — phenotypic severity (especially skeletal deformity severity, vascular event risk, hearing loss presence/degree) differs meaningfully between individuals and appears to correlate at least partly with the specific allele combination/residual enzyme activity, particularly documented for PLOD1 ("Phenotypic variability of the kyphoscoliotic type of EDS," PMC3135503).

**Genetic anticipation:** Not applicable/not reported — not a repeat-expansion disorder.

**Germline mosaicism:** Not specifically reported in the sources reviewed for either gene.

**Founder effects:**
- PLOD1: the 8.9-kb Alu-mediated intragenic duplication (exons 10–16) is a **recurrent** structural variant (~30% of alleles across studied families) — consistent with a mutational hotspot rather than a single-population founder effect; c.955C>T (p.Arg319Ter) is specifically noted as prevalent in **Arab populations**.
- FKBP14: c.362dupC is a **bona fide founder allele**, present on a shared haplotype in essentially all molecularly solved cases and accounting for ~70% of disease alleles.

**Consanguinity:** As with any rare autosomal recessive disorder, parental consanguinity substantially elevates recurrence risk in affected families/populations, though a formal consanguinity-rate statistic specific to kEDS was not retrieved in this search.

**Carrier frequency:** Not directly retrieved from gnomAD in this session; can be approximated from disease incidence (~1:100,000, full penetrance) as roughly 1:150–1:160 carriers for PLOD1-kEDS under Hardy-Weinberg assumptions — this figure should be verified directly against gnomAD population data before use as a curated claim.

**Recurrence risk:** For carrier × carrier parental matings, each pregnancy carries the standard Mendelian recessive risk: 25% affected, 50% carrier, 25% unaffected.

**Population demographics:** No formal sex-ratio skew is reported (autosomal, not sex-linked); age distribution spans neonatal diagnosis through documented adult survivors into the sixth decade.

Source: [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/); [Orphanet FKBP22-deficiency kEDS](https://www.orpha.net/en/disease/detail/300179); [Giunta et al. 2018, Genet Med](https://www.nature.com/articles/gim201770); [Phenotypic variability of EDS VIA, PMC3135503](https://pmc.ncbi.nlm.nih.gov/articles/PMC3135503/)

---

## 10. Diagnostics

### Clinical Diagnostic Criteria (2017 International Classification)
Minimal diagnostic criteria for kEDS (both molecular subtypes) per the 2017 nosology: **congenital muscular hypotonia AND congenital/early-onset kyphoscoliosis**, PLUS **either generalized joint hypermobility OR three minor criteria**. Definitive diagnosis requires molecular confirmation of biallelic pathogenic variants.

### Laboratory / Biochemical Tests
- **Urinary Dpyr:Pyr ratio (deoxypyridinoline:pyridinoline cross-link ratio)** measured by HPLC — the diagnostic biomarker specific to PLOD1-kEDS. Normal ratio ≈0.2; PLOD1-kEDS ratio ≈6.0. This test is **normal in FKBP14-kEDS**, making it a useful biochemical discriminator between the two molecular subtypes when genetic testing is pending or ambiguous.
- LH1 enzyme activity assay in cultured fibroblasts (historical confirmatory method, largely supplanted by molecular testing).
- Creatine kinase: normal or only mildly elevated in FKBP14-kEDS myopathy (helps distinguish from primary muscular dystrophies).

### Genetic Testing
- **Gene-targeted sequence analysis** of PLOD1 (detects ~67% of variants) or FKBP14, followed by **deletion/duplication analysis** for structural variants (detects remaining ~33% of PLOD1 alleles, dominated by the recurrent 8.9-kb duplication; ~70% of FKBP14 alleles are the single c.362dupC founder variant, generally detectable by sequencing).
- **Multigene connective-tissue-disorder panels** including PLOD1, FKBP14, and overlapping genes (COL1A1/2, COL3A1, COL5A1/2, COL12A1, ZNF469, B4GALT7, etc.) are appropriate first-line given phenotypic overlap.
- **Exome/genome sequencing** reserved for atypical presentations or when panel testing is non-diagnostic.
- **Chromosomal microarray/karyotype/FISH:** not primary diagnostic modalities for kEDS (a sequence/structural-variant-level disease, not a chromosomal disorder), though CMA can detect the larger PLOD1 structural duplication in some assay designs.

### Imaging / Functional Testing
- Spine radiography/MRI for kyphoscoliosis characterization and surgical planning.
- Echocardiography and vascular imaging (CT/MR angiography of aorta and medium-sized arteries) for cardiovascular surveillance (see Section 12).
- Pulmonary function testing for restrictive disease in severe spinal deformity.
- Audiometry (FKBP14 subtype) for hearing loss characterization.
- Ophthalmologic exam (slit lamp, refraction) for globe fragility/refractive error surveillance.

### Biopsy/Histopathology
- Muscle biopsy in FKBP14-kEDS: nonspecific mild myopathic changes with increased fiber-diameter variation; not required for diagnosis but supports the myopathic phenotype.
- Skin/fibroblast ultrastructural studies (electron microscopy): show ER cisternal enlargement with flocculent material in FKBP14-kEDS fibroblast cultures — largely a research rather than routine clinical diagnostic tool.

### Differential Diagnosis
| Condition | Distinguishing features |
|---|---|
| Classic EDS (COL5A1/2, COL1A1) | Absence of congenital hypotonia; simple scoliosis rather than kyphoscoliosis pattern |
| Vascular EDS (COL3A1) | Autosomal dominant; intestinal/uterine rupture more prominent; distinct vascular event profile |
| PLOD1-kEDS vs FKBP14-kEDS | Hearing impairment and myopathy favor FKBP14; elevated urinary Dpyr:Pyr ratio is specific to PLOD1 (normal in FKBP14) |
| Musculocontractural EDS (CHST14/DSE) | Adducted thumbs/clubfeet, characteristic craniofacial features, GI/genitourinary manifestations |
| Spondylodysplastic EDS | Progressive short stature; primary skeletal dysplasia; dysplastic teeth |
| Myopathic EDS (COL12A1) | Severe progressive scoliosis with prominent myopathy on biopsy |
| Collagen VI disorders (Bethlem myopathy/Ullrich CMD) | Absent skin hyperelasticity, bruising, hearing impairment, cardiovascular involvement |
| Congenital myopathies (non-EDS) | Normal skin texture; absent characteristic velvety/hyperextensible skin |
| Larsen syndrome | A documented real-world diagnostic pitfall: FKBP14-kEDS has been misdiagnosed as Larsen syndrome (PMID 37433679) |
| Brittle cornea syndrome (ZNF469, PRDM5) | Corneal rupture more characteristic than scleral rupture (kEDS shows the reverse pattern) |

**Biochemically**, all differential diagnoses show **normal lysyl hydroxylase activity/normal Dpyr:Pyr ratio**, distinguishing them from PLOD1-kEDS specifically.

### Screening
No population-based newborn or carrier screening program specific to kEDS was identified; given the severity and recessive inheritance, **carrier screening/cascade testing in known founder populations and genetic counseling for consanguineous families** are the practical prevention-adjacent measures (see Section 13).

Source: [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/); [FKBP14-kEDS misdiagnosed as Larsen syndrome, PMID 37433679](https://pubmed.ncbi.nlm.nih.gov/37433679/); [Ocular manifestations of EDS](https://eyewiki.org/Ehlers-Danlos_Syndrome)

---

## 11. Outcome/Prognosis

**Survival/Mortality:** No formal actuarial life-table or 5-/10-year survival statistics specific to kEDS were identified — this reflects the disease's rarity and the case-report-dominated literature. GeneReviews states life span "may be normal," but this is qualified by substantial risk of **life-threatening arterial rupture/dissection** in adulthood (~30% of PLOD1-kEDS adults) as the principal mortality driver; a fatal case of superior mesenteric artery aneurysm rupture with aortic involvement in a 15-year-old was reported as recently as 2025 despite emergency hybrid surgical/endovascular intervention (PMID 41613374), illustrating that mortality risk is not confined to older adulthood. For FKBP14-kEDS, survival into the sixth decade has been documented (one patient alive at age 53), but the literature explicitly notes adults are likely **underrecognized** due to historically limited access to genetic testing, biasing available prognosis data toward pediatric presentations.

**Morbidity/Function:**
- Severe kyphoscoliosis drives restrictive lung disease, recurrent pneumonia, and eventual cardiac strain/failure in the most severely affected adults.
- Chronic joint instability and recurrent dislocation contribute to long-term disability and pain.
- Progressive myopathy/motor decline is specifically described in adult FKBP14-kEDS, though patients generally retain independence in activities of daily living and ambulation.
- Ocular complications (globe rupture, refractive error, keratoconus/keratoglobus in severe cases) can cause permanent visual impairment.
- Sensorineural/conductive hearing loss (FKBP14) contributes to communication and developmental morbidity if unaddressed.

**Complications:** Arterial aneurysm/dissection/rupture (aorta, superior mesenteric artery, carotid, celiac arteries documented), scleral/globe rupture, recurrent joint dislocation, hernias, osteopenia/fracture risk, restrictive pulmonary disease, subdural hygroma (reported in FKBP14-kEDS), cardiac valve insufficiency (FKBP14-kEDS).

**Prognostic factors:** Severity of skeletal deformity at presentation, presence/burden of vascular disease, specific genotype (residual enzyme activity), and access to early multidisciplinary surgical/orthopedic intervention appear to be the principal determinants of long-term outcome, though this is inferred from the qualitative case-series literature rather than formally modeled prognostic scoring.

**Recovery potential:** Not a remitting disease; management is aimed at preventing/mitigating complications rather than reversing the underlying connective tissue defect (though see Section 12 for the theoretical basis of targeted therapies under investigation).

Source: [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/); [kEDS-PLOD1 fatal SMA aneurysm/aortic rupture case, PMID 41613374](https://pubmed.ncbi.nlm.nih.gov/41613374/); [Severe PLOD1-kEDS with multiple arterial/venous complications, PMC9969762](https://pmc.ncbi.nlm.nih.gov/articles/PMC9969762/)

---

## 12. Treatment

There is **no disease-modifying or curative pharmacotherapy** for kEDS; management is multidisciplinary, surveillance-driven, and focused on prevention/treatment of complications.

### Pharmacotherapy
- **Beta-blockers** — considered for aortic root dilatation (extrapolated from vascular EDS management experience rather than kEDS-specific trial data); suggested NCIT term: NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` class NCIT:C2231 (Adrenergic beta-Antagonist).
- **Antihypertensive management** generally, to reduce arterial wall shear stress.
- **Bisphosphonates/denosumab** — used off-label for osteopenia/low bone mineral density management in EDS broadly, including presumably kEDS, though data are drawn from general EDS skeletal-fragility literature rather than kEDS-specific trials; bisphosphonates show reasonable efficacy for vertebral (but not long-bone) fracture prevention, with medication-related osteonecrosis of the jaw (MRONJ) as a recognized risk.
- Analgesics/pain management for chronic joint pain (non-specific, standard-of-care).

### Surgical/Interventional
- **Spinal surgery** (posterior spinal fusion, growing-rod constructs, cervical corpectomy/fusion for cervical kyphosis with myelopathy) is frequently required, as **conservative bracing is often ineffective against the rapidly progressive kyphoscoliosis** characteristic of kEDS. Case series of posterior spinal fusion (3 adolescents) report satisfactory curve correction with no major intra-/postoperative complications when performed after failed conservative management; more complex multi-stage surgical courses (including occipitocervical fusion, growing rods, corpectomy) have been reported for severe early-onset cases. Suggested NCIT terms: NCIT:C15329 (Surgical Procedure); more specifically spinal fusion procedures.
- **Endovascular/hybrid surgical repair** for arterial aneurysm/rupture (documented in a fatal SMA aneurysm/aortic rupture case combining laparotomy hemostasis with stent-graft placement).
- **Hernia repair** as clinically indicated.
- **Cataract/retinal laser treatment** for ophthalmologic complications.

### Supportive/Rehabilitative
- Physical therapy targeting shoulder-girdle and core strengthening; **swimming** specifically recommended as a lower-impact strengthening activity.
- Occupational therapy for motor dysfunction, particularly addressing the adult motor decline seen in FKBP14-kEDS.
- Orthopedic bracing for joint instability (adjunctive, not curative for the spine).
- Protective equipment during activity.
- Standard management of hearing impairment (hearing aids/audiologic support, FKBP14 subtype), cleft palate, and refractive error.

### Experimental/Investigational
No kEDS-specific gene therapy, RNA-based therapy, or targeted molecular therapeutic was identified as being in active clinical trials in this search. Given the loss-of-function, enzyme/chaperone-deficiency mechanism, **gene replacement or enzyme augmentation strategies remain theoretically plausible avenues** analogous to other collagen-modifying enzymopathies, but no ClinicalTrials.gov-registered program specific to PLOD1 or FKBP14 was surfaced in this search session — this is a genuine literature gap rather than a negative-trial finding, and should be verified directly against ClinicalTrials.gov/WHO ICTRP before being asserted as a settled absence.

### Activities/Agents to Avoid
Joint-stressing sports (gymnastics, long-distance running), contact/collision sports (particularly with known aortic aneurysm), heavy lifting, and diagnostic arteriography except when necessary to localize life-threatening hemorrhage.

### Surveillance Schedule (synthesized from GeneReviews for both subtypes)
- Blood pressure at every visit
- Annual (or every 1–3 year, subtype-dependent) orthopedic, ophthalmologic, and audiologic evaluation
- Echocardiography (± cardiac MRI) every 2–5 years, beginning around age 5
- CT/MR angiography of the aorta and medium-sized arteries beginning in young adulthood (or earlier per clinical suspicion)
- DXA bone density assessment beginning around age 10–12
- Annual hernia screening
- Neurodevelopmental assessment at each visit through adolescence (FKBP14-kEDS)

Source: [GeneReviews PLOD1-kEDS Management](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS Management](https://www.ncbi.nlm.nih.gov/books/NBK541503/); [Posterior spinal fusion in kEDS, PMID 21667916](https://pubmed.ncbi.nlm.nih.gov/21667916/); [Surgical management of spinal deformity in FKBP14-kEDS, 2025, PMC12689754](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12689754/); [Skeletal fragility in EDS](https://www.researchgate.net/publication/329694626_Skeletal_fragility_an_emerging_complication_of_Ehlers-Danlos_syndrome)

---

## 13. Prevention

**Primary prevention:** Not possible to prevent occurrence of a fully penetrant autosomal recessive Mendelian disease through lifestyle/behavioral means; the only true primary-prevention lever is **reproductive genetic counseling and carrier/preimplantation genetic testing** in at-risk families (known carrier couples, consanguineous unions, or families with a previously affected child).

**Secondary prevention (early detection):**
- Prenatal diagnosis via chorionic villus sampling/amniocentesis with targeted molecular testing is possible once familial pathogenic variants are known.
- Early clinical recognition in the neonatal period (congenital hypotonia + kyphoscoliosis) enables prompt genetic confirmation and initiation of surveillance before major complications (especially vascular) develop.
- No population-based newborn screening program exists for kEDS (it is not part of standard newborn metabolic/genetic screening panels).

**Tertiary prevention (preventing complications in affected individuals):** This is where essentially all "prevention" activity in kEDS actually concentrates, and it overlaps substantially with Section 12's surveillance/avoidance recommendations:
- Blood pressure control and consideration of beta-blockade to reduce arterial wall stress.
- Avoidance of high-impact/contact activities and heavy lifting to reduce joint dislocation and vascular rupture risk.
- Avoidance of diagnostic arteriography except when essential.
- Scheduled vascular imaging surveillance to detect aneurysmal change before rupture.
- Early orthopedic surgical intervention for progressive kyphoscoliosis to forestall restrictive pulmonary disease.
- Protective eyewear/activity modification to reduce ocular trauma risk given scleral fragility.
- High-risk perinatology-center delivery planning for affected pregnant women, given elevated risk of membrane rupture, miscarriage, and arterial rupture during pregnancy/delivery.

**Genetic counseling:** Central to family planning in known-carrier families; recurrence risk counseling follows standard autosomal recessive Mendelian principles (25% affected per pregnancy for two carrier parents).

**Immunization:** Not applicable — kEDS is not an infectious or vaccine-preventable condition.

**Public health/environmental interventions:** Not applicable given the purely genetic etiology.

Source: [GeneReviews PLOD1-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK1462/); [GeneReviews FKBP14-kEDS](https://www.ncbi.nlm.nih.gov/books/NBK541503/)

---

## 14. Other Species / Natural Disease

**Taxonomy:** *Homo sapiens* (NCBITaxon:9606) is the primary species of interest, but a **naturally occurring PLOD1-related disease homolog exists in the domestic horse (*Equus caballus*, NCBITaxon:9796)**.

**Equine homolog — Warmblood Fragile Foal Syndrome (WFFS):** This is cataloged in OMIA as **OMIA:001982-9796 — "kyphoscoliotic Ehlers-Danlos syndrome (kEDS), PLOD1-related"** in the domestic horse. WFFS type 1 is caused by a recessive **PLOD1 missense variant (c.2032G>A)** and produces a lethal/severely debilitating neonatal foal phenotype with extreme skin and connective tissue fragility, closely paralleling the human PLOD1-kEDS mechanism (lysyl hydroxylase deficiency → defective collagen cross-linking). This is directly relevant as a **naturally occurring, non-engineered large-animal disease model** with high face validity for the human condition, distinct from the laboratory Plod1-knockout mouse (Section 15). Population genetics work has examined WFFS carrier allele frequency in warmblood breeds and (a related PLOD1 variant) in Thoroughbreds, where the allele was found to have low frequency and no association with catastrophic musculoskeletal breakdown.

**Gene orthologs:** PLOD1 and FKBP14 are broadly conserved across vertebrates (mouse *Plod1*/*Fkbp14*, zebrafish *plod1a/plod1b*), consistent with their fundamental, evolutionarily conserved role in collagen biosynthesis; comparative pathology across these species centers on collagen fibril cross-linking defects rather than kEDS-specific study, given the equine WFFS system is the closest natural phenocopy identified.

**Transmission:** Not applicable — kEDS and WFFS are both purely genetic, non-communicable, non-zoonotic conditions.

Source: [OMIA:001982-9796 — kEDS PLOD1-related in the domestic horse](https://omia.org/OMIA001982/9796/); [WFFS PLOD1 c.2032G>A allele frequency in Thoroughbreds, PMC7062577](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7062577/)

---

## 15. Model Organisms

### Mouse — *Plod1*⁻ᐟ⁻ (PLOD1 knockout)
The principal genetic mouse model for PLOD1-kEDS.
- **Phenotype recapitulation:** **Partial.** *Plod1*⁻ᐟ⁻ mice show **muscle hypotonia and aortic ruptures**, recapitulating two of the most clinically significant human features (hypotonia, vascular rupture). However, they **lack the characteristic kyphoscoliosis** seen in humans, and **skin hyperextensibility/fragility is absent** despite detectable ultrastructural collagen alterations in skin tissue.
- **Biochemical basis for the mismatch:** Tissue-specific residual hydroxylysine content differs substantially between the mouse model and human disease — *Plod1*⁻ᐟ⁻ mice retain ~22% (skin) to as little as ~14% loss (up to 86% decrease in lung) of total hydroxylysine, compared with an estimated ~95% reduction (to ~5% residual) in affected humans — attributed to **partial functional compensation by the paralogous enzymes LH2 (PLOD2) and LH3 (PLOD3)** in mice, which appears less complete or tissue-distributed differently than in humans. This quantitative difference in residual enzyme/cross-link activity is the leading proposed explanation for why the mouse spares the spine and skin phenotypes.
- **Model limitations:** The absence of kyphoscoliosis (the defining orthopedic hallmark) and skin fragility limits the model's utility for studying the spinal and dermatologic components of disease, though it remains valuable for studying the vascular and muscular phenotypes and for testing potential therapeutic cross-link-restoration strategies.
- **A newer CRISPR/Cas9-generated mouse model of EDS** has also been reported (2021/2022) as part of a broader effort to build more faithful genomic-editing-based EDS models, though the specific gene target/subtype recapitulated by that model was not fully resolved in this search and should be checked against the primary source before citation.

### Zebrafish
No PLOD1- or FKBP14-specific zebrafish kEDS model was identified in this search. Related work exists on the paralogous enzyme **PLOD2 (LH2)** in zebrafish dermal wound healing/collagen telopeptide cross-linking (relevant to fibrosis biology generally, not kEDS specifically), and on zebrafish type I collagen mutants recapitulating human type I collagenopathies (a different, non-kEDS disease class) — these are adjacent, not direct, model systems.

### Other Systems
- **Patient-derived dermal fibroblast cultures** are the dominant *in vitro* system used in the literature reviewed, supporting: LH1 enzyme activity assays, urinary/tissue cross-link biochemistry, transcriptome profiling distinguishing PLOD1- from FKBP14-kEDS molecular signatures, and ultrastructural (electron microscopy) characterization of ER stress and ECM disorganization in FKBP14-kEDS.
- No iPSC-derived organoid, CRISPR functional-genomics screen, or invertebrate (*Drosophila*/*C. elegans*) model specific to kEDS was identified in this search.

### Applications
The *Plod1*⁻ᐟ⁻ mouse in particular supports research into the vascular-rupture mechanism and muscle hypotonia and could plausibly serve as a platform for testing cross-link-restoring or gene-replacement therapeutic strategies, though its incomplete phenotypic penetrance (no spine/skin phenotype) means spinal and dermatologic disease mechanisms require either the equine WFFS natural model or direct human tissue/cell studies.

Source: [Animal Models of Ehlers–Danlos Syndromes: Phenotype, Pathogenesis, and Translational Potential (review), PMC8547655](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8547655/); [OMIA:001982-9796 equine WFFS](https://omia.org/OMIA001982/9796/); [Transcriptome profiling of PLOD1 vs FKBP14 fibroblasts, PMC6678841](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6678841/); [New CRISPR-generated EDS mouse model, PMC8713987](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8713987/)

---

## Notes on Evidence Gaps and Curation Caveats

For downstream curation into a dismech-style knowledge base, the following points warrant explicit flagging rather than confident assertion:

1. **PLOD1/FKBP14 gnomAD-derived carrier frequency** was not directly retrieved from the gnomAD browser in this session (only general gnomAD methodology was surfaced) — this should be queried directly at gnomad.broadinstitute.org before citing a specific number.
2. **Life-expectancy/survival statistics** are not formally established in the literature for either subtype; "life span may be normal" (GeneReviews) is a qualitative, not actuarial, statement and should not be curated as a quantitative prognosis claim without a supporting cohort study.
3. **Cochlear pathophysiology mechanism** for FKBP14-kEDS hearing loss is inferred from collagen VI/III tissue tropism, not directly demonstrated by otopathologic study in the sources reviewed — mark as inferred/mechanistic hypothesis rather than established fact if curated into a causal pathograph.
4. **Gene therapy/experimental therapeutics** — no active kEDS-specific clinical trial was surfaced; this is a search-session finding, not a confirmed negative, and should be re-verified against ClinicalTrials.gov/WHO ICTRP directly.
5. The Orphanet page for ORPHA:1900 could not be fetched directly (access-restricted); prevalence/epidemiology claims attributed to Orphanet in this report come from secondary citation via search-result synthesis and should be cross-checked against the primary Orphanet record before formal citation.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 3 |
| Terms whose name was checked | 42 |
| Terms named correctly | 21 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100775` (2 mentions) - the report calls it "Umbilical hernia"; HP calls it **Dural ectasia**
- `HP:0025214` (1 mention) - the report calls it "Arterial dissection"; HP calls it **Triggered by heat**
- `HP:0004349` (1 mention) - the report calls it "Osteopenia"; HP calls it **Reduced bone mineral density**
- `HP:0000023` (1 mention) - the report calls it "Congenital contractures"; HP calls it **Inguinal hernia**
- `HP:0000539` (1 mention) - the report calls it "Refractive errors"; HP calls it **Abnormality of refraction**
- `HP:0003198` (1 mention) - the report calls it "Myopathy (mild, nonspecific histopathology)"; HP calls it **Myopathy**
- `CL:0000057` (2 mentions) - the report calls it "fibroblast — dermal fibroblasts are the principal cell studied biochemically"; CL calls it **fibroblast**
- `UBERON:0001846` (1 mention) - the report calls it "cochlea, FKBP14 subtype"; UBERON calls it **internal ear**
- `NCIT:C2231` (1 mention) - the report calls it "Adrenergic beta-Antagonist"; NCIT calls it **Dofequidar Fumarate**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005692` (obsolete Joint hyperflexibility) (1 mention) - replaced by `HP:0001382`
- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0016002` (1 mention) - the report calls it "Ehlers-Danlos syndrome, kyphoscoliotic type 1 / EDS type VIA / oculoscoliotic type"; MONDO calls it **Ehlers-Danlos syndrome, kyphoscoliotic type 1**
- `HP:0001382` (2 mentions) - the report calls it "Joint hypermobility", "Large-joint hypermobility"; HP calls it **Joint hypermobility**
- `HP:0001270` (1 mention) - the report calls it "Gross motor developmental delay"; HP calls it **Motor delay**, and lists "Motor developmental delay" among its other names
- `HP:0005692` (1 mention) - the report calls it "Small-joint hypermobility"; HP calls it **obsolete Joint hyperflexibility**
- `HP:0002647` (1 mention) - the report calls it "Aortic/arterial rupture, dissection, pseudoaneurysm"; HP calls it **Aortic dissection**
- `GO:0018216` (2 mentions) - the report calls it "peptidyl-proline hydroxylation"; GO calls it **peptidyl-arginine methylation**
- `GO:0031545` (1 mention) - the report calls it "peptidyl-proline dioxygenase activity, LH1"; GO calls it **peptidyl-proline 4-dioxygenase activity**
- `GO:0003755` (1 mention) - the report calls it "peptidyl-prolyl cis-trans isomerase activity, FKBP14"; GO calls it **peptidyl-prolyl cis-trans isomerase activity**
- `GO:0005789` (2 mentions) - the report calls it "ER membrane"; GO calls it **endoplasmic reticulum membrane**, and lists "ER membrane" among its other names
- `CL:0000188` (1 mention) - the report calls it "skeletal muscle cell/myocyte"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `CL:0000192` (2 mentions) - the report calls it "smooth muscle cell, arterial media"; CL calls it **smooth muscle cell**
- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001382` - called "Joint hypermobility", "Large-joint hypermobility"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIA`.