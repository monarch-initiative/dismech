---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T21:44:38.477991'
end_time: '2026-09-23T21:49:16.622226'
duration_seconds: 278.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Leber Congenital Amaurosis 9
  mondo_id: MONDO:0012056
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
  web_search_requests: 13
  num_turns: 19
  total_cost_usd: 1.305799
  session_id: 45ce5f1a-6721-5dd9-af0a-cb3620796386
  stop_reason: end_turn
  assistant_text_blocks: 2
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
citation_count: 20
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:22842230
  relevance_assessed: 12
  on_topic: 11
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 48
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 31
  labels_matching: 13
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0012056
    reported_labels:
    - MONDO
    ontology_label: Leber congenital amaurosis 9
  - term_id: HP:0000639
    reported_labels:
    - Nystagmus (often roving/searching)
    ontology_label: Nystagmus
  - term_id: HP:0009466
    reported_labels:
    - Abnormal pupillary function
    ontology_label: Radial deviation of finger
  - term_id: HP:0000640
    reported_labels:
    - Oculodigital sign (eye poking/pressing)
    ontology_label: Gaze-evoked nystagmus
  - term_id: HP:0000546
    reported_labels:
    - Abnormal electroretinogram
    ontology_label: Retinal degeneration
  - term_id: HP:0000539
    reported_labels:
    - High hyperopia (less prominent than some other LCA genes)
    ontology_label: Abnormality of refraction
  - term_id: CL:0002588
    reported_labels:
    - retinal rod cell
    ontology_label: smooth muscle cell of the umbilical vein
  - term_id: CL:0011020
    reported_labels:
    - retinal bipolar neuron
    ontology_label: neural progenitor cell
  - term_id: UBERON:0001782
    reported_labels:
    - macula lutea
    ontology_label: pigmented layer of retina
  - term_id: UBERON:0001769
    reported_labels:
    - optic nerve
    ontology_label: iris
  - term_id: UBERON:0002450
    reported_labels:
    - retinal pigment epithelium
    ontology_label: decidua
  - term_id: NCIT:C15238
    reported_labels:
    - "Gene Therapy \u2014 for the preclinical AAV-NMNAT1 approach"
    ontology_label: Gene Therapy
  labels_variant: 6
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leber Congenital Amaurosis 9
- **MONDO ID:** MONDO:0012056 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber Congenital Amaurosis 9** covering all of the
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

I'll research Leber Congenital Amaurosis 9 (LCA9, NMNAT1-associated) using web search and authoritative sources, then compile the comprehensive report.

I now have sufficient depth across all sections. Compiling the full research report.

# Leber Congenital Amaurosis 9 (LCA9) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Leber congenital amaurosis 9 (LCA9) is an autosomal recessive, non-syndromic, early-onset severe retinal dystrophy caused by biallelic pathogenic variants in *NMNAT1* (nicotinamide nucleotide adenylyltransferase 1, chromosome 1p36.22). It is one of >27 genetically distinct forms of Leber congenital amaurosis (LCA), the most severe inherited photoreceptor-neuron degeneration causing congenital or infantile blindness [OMIM:608553; MalaCards]. LCA9 was first described in 2012 by three independent groups using exome/homozygosity-mapping approaches that identified *NMNAT1* as a novel retinal-disease gene, notable because it encodes a ubiquitously expressed NAD⁺-biosynthetic enzyme rather than a classic phototransduction or ciliary-transport protein [PMID:22842227, PMID:22842230, PMID:22842231].

**Key identifiers:**
- **MONDO:** MONDO:0012056
- **OMIM (phenotype):** #608553 (LEBER CONGENITAL AMAUROSIS 9; LCA9)
- **OMIM (gene):** *608700 (NICOTINAMIDE NUCLEOTIDE ADENYLYLTRANSFERASE 1; NMNAT1)
- **Orphanet:** ORPHA:65 (Leber congenital amaurosis, general entry cross-referencing NMNAT1)
- **HGNC:** HGNC:17877 (gene symbol NMNAT1)
- **Gene location:** 1p36.22 (a 5-exon gene encoding a 280-residue protein) [GeneCards; OMIM:608700]
- **GeneCC/ClinGen:** classified as a definitive autosomal recessive gene-disease relationship for LCA9 [thegencc.org/genes/HGNC:17877]

**Synonyms/alternative names:** LCA9; NMNAT1-related Leber congenital amaurosis; NMNAT1-associated retinal degeneration; NMNAT1-related retinopathy (the broader label used when the phenotype is cone-rod dystrophy rather than classic LCA).

**Nature of the evidence base.** Data derive almost entirely from aggregated disease-level resources — case series and cohort studies pooling molecularly confirmed families (largest combined cohort: 158 patients/129 families) [PMID:34837036], case reports, OMIM curation, and mouse-model mechanistic studies — rather than large-scale EHR/claims data, reflecting the rarity of the condition.

Sources: [OMIM #608553](https://omim.org/entry/608553) | [NORD/MONDO summary](https://rarediseases.org/mondo-disease/leber-congenital-amaurosis-9/) | [MalaCards LCA9](https://www.malacards.org/card/leber_congenital_amaurosis_9) | [GeneCC NMNAT1](https://thegencc.org/genes/HGNC:17877)

---

## 2. Etiology

**Disease causal factor.** LCA9 is purely monogenic/Mendelian: biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic missense variants in *NMNAT1* are necessary and sufficient to cause disease. There is no known environmental, infectious, or complex-multifactorial contribution to LCA9 itself (distinguishing it from age-related retinal degenerations).

**Genetic risk factors.**
- **Causal variants:** >80 distinct biallelic pathogenic *NMNAT1* variants have been reported across >129 families, spanning missense (67.5%), frameshift indel (8.8%), nonsense (7.5%), splice-site (6.3%), gross indel (6.3%), and start-loss/stop-loss/regulatory variants (3.8%) [PMID:34837036].
- **Founder/recurrent alleles:**
  - **c.769G>A (p.Glu257Lys, E257K)** is the single most common allele, found on ~24.8–48.8% of mutant alleles across cohorts and reported in up to 70% of LCA9 index cases in some series; haplotype analysis of European-descent carriers confirms a shared ancestral haplotype consistent with a **founder mutation** [OMIM:608553; PMID:29674119].
  - **c.709C>T (p.Arg237Cys, R237C)** is the predominant allele in Asian populations (found in up to 85.7% of detected Asian alleles) [PMID:34837036].
  - **c.25G>A (p.Val9Met, V9M)** — an early-reported LCA9 allele affecting a highly conserved residue, absent from 501 controls and public databases at the time of discovery.
- **Modifier/penetrance consideration:** p.E257K is unusually common in the general population (gnomAD European non-Finnish allele frequency ~0.122%, overall ~0.07%) and is enriched in a heterozygous state in LCA cohorts (0.94%) versus Caucasian controls (0.18%); homozygous individuals without phenotype have been reported, so E257K behaves as a **hypomorphic allele with reduced/variable penetrance** rather than a fully penetrant null allele [PMID:29674119].

**Risk factors summary table:**
| Factor type | Detail |
|---|---|
| Genetic (causal) | Biallelic *NMNAT1* pathogenic variants (missense predominates) |
| Genetic (susceptibility) | Homozygosity for hypomorphic E257K (reduced penetrance) |
| Environmental | None established |
| Demographic | Consanguinity increases likelihood of biallelic rare variant homozygosity in non-founder populations |

**Protective factors.** No specific protective genetic or environmental factors are established for LCA9. At the mechanistic level, genetic or pharmacologic depletion/inhibition of SARM1 (see Mechanism, below) rescues photoreceptor death in *Nmnat1*-mutant mice, identifying SARM1 loss-of-function as a hypothetical protective modifier, though this is model-organism evidence, not a documented human protective variant [PMID: eLife 62027 / PMC7591247].

**Gene-environment interactions.** None reported; LCA9 pathogenesis is intrinsic to photoreceptor NAD⁺ homeostasis and is not known to be modulated by external exposures.

Sources: [OMIM #608553](https://omim.org/entry/608553) | [NMNAT1 E257K variant PMID:29674119](https://pubmed.ncbi.nlm.nih.gov/29674119/) | [PMC9674661 (genetic spectrum)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674661/)

---

## 3. Phenotypes

LCA9 phenotypes fall into three clinical-sign categories: clinical signs/physical findings (the overwhelming majority), electrophysiological/laboratory abnormalities (ERG), and imaging findings (OCT/fundus). Data are aggregated from cohort/case-series literature (n=158 combined) rather than individual EHR mining [PMID:34837036].

| Phenotype | HPO term (suggested) | Onset | Frequency | Severity/course |
|---|---|---|---|---|
| Severe congenital/infantile visual impairment | HP:0000505 (Visual impairment) / HP:0000618 (Blindness) | Birth–12 months (92% present within first year; range birth–11 years) | ~92–100% | Severe, essentially stable from infancy but with progressive structural loss |
| Nystagmus (often roving/searching) | HP:0000639 | Typically noted at or shortly after birth | Very common (majority of cohort) | Persistent |
| Sluggish/absent pupillary light reflex | HP:0009466 (Abnormal pupillary function) | Congenital | Common | — |
| Oculodigital sign (eye poking/pressing) | HP:0000640 | Infancy | Reported in a subset | Behavioral compensatory sign |
| Macular coloboma / "pseudocoloboma" (disciform macular atrophy) | HP:0008062 (Atrophic macular degeneration) or HP:0007754 (Macular dystrophy) | Congenital–early infancy, enlarges with age | 66.7–100% of eyes imaged | Progressive enlargement; hallmark of LCA9 |
| Generalized tapetoretinal (chorioretinal) degeneration | HP:0000556 / HP:0000580 | By ~12 years of age (all 9 authors'-cohort patients) | 100% by age 12 | Progressive, sparing far periphery relatively |
| Attenuated retinal vessels | HP:0007843 | Progressive | Common | — |
| Optic disc pallor / early-onset optic atrophy | HP:0000648 (Optic atrophy) | Early-onset, unusual for typical LCA | Frequent, a distinguishing LCA9 feature | Progressive |
| Undetectable/severely reduced full-field ERG (rod and cone) | HP:0000546 (Abnormal electroretinogram) | Congenital | Extinguished or severely reduced in nearly all tested | Non-progressive floor effect (already extinguished at baseline) |
| Photophobia | HP:0000613 | Variable | Reported subset | — |
| High hyperopia (less prominent than some other LCA genes) | HP:0000539 | — | Variable | — |

**Phenotype spectrum/severity gradient (genotype-dependent):** Truncating variants (frameshift, nonsense) are uniformly associated with the classic severe LCA phenotype; certain milder, computationally-predicted-benign missense variants (e.g., p.Glu91Lys, p.Asn167Ser, and even some E257K genotypes) are instead associated with a **milder cone-rod dystrophy (CORD)** phenotype with later onset and better preserved vision — a genotype-phenotype correlation reported in 5–6 of 129 families [PMID:34837036; PMID:29674119 (E257K "mild retinal degeneration phenotype")].

**Distinctive feature — "macular coloboma."** Patients with NMNAT1 mutations exhibit a peculiar retinal finding termed macular coloboma: an atrophic lesion in the central retina with a pigmented border, signifying complete loss of neural tissue in the fovea (photoreceptors, bipolar cells, and ganglion cells), often attributed to a congenital failure of foveal formation rather than a purely degenerative process [OMIM:608553; PMC9674661].

**Visual acuity:** 89.5% (102/114) of evaluable patients had visual acuity ≤0.05 Snellen equivalent (legal blindness); a small minority in the milder/CORD spectrum retain measurable acuity up to ~0.20 [PMID:34837036].

**Quality of life impact.** No LCA9-specific EQ-5D/SF-36 data were identified in the literature searched; qualitatively, LCA9 causes profound early-life visual disability requiring lifelong low-vision support, mobility training, and educational accommodation, consistent with the broader LCA/early-onset severe retinal dystrophy literature (no syndromic systemic involvement is reported, unlike some other LCA subtypes with CNS or renal comorbidity).

Sources: [PMC9674661 – Clinical features and genetic spectrum of NMNAT1-associated retinal degeneration](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674661/) | [OMIM Clinical Synopsis #608553](https://omim.org/clinicalSynopsis/608553) | [PMID:29674119](https://pubmed.ncbi.nlm.nih.gov/29674119/)

---

## 4. Genetic/Molecular Information

**Causal gene.** *NMNAT1* (HGNC:17877; OMIM *608700), chromosome 1p36.22, 5 exons, encoding a 280-amino-acid, ~139 kDa (as homotetramer by gel filtration) nuclear enzyme.

**Gene/protein function.** NMNAT1 (nicotinamide mononucleotide adenylyltransferase 1) catalyzes the terminal, rate-limiting step of NAD⁺ biosynthesis (condensation of NMN + ATP → NAD⁺ + PPi) in the nuclear compartment. Beyond its catalytic role, NMNAT1 has a described chaperone-like neuroprotective function against neuronal-activity-induced degeneration, and its NAD⁺-generating activity supports nuclear deacetylase (sirtuin) activity implicated in neuroprotection [Nature Genetics PMID:22842230; Wikipedia/GeneCards NMNAT1].

**Protein structure.** Contains a conserved N-terminal adenylyltransferase motif, an N-terminal nuclear localization signal, an N-glycosylation site, and several potential transmembrane regions. The catalytic active site includes the signature **GxFxPx[H/T]xxH** motif essential for NMNAT activity, plus an **ISSTxxR** motif and the pyridine-ring-stacking residue **Trp169**.

**Variant classification (ACMG/AMP, per ClinVar/literature):**
- The great majority of reported LCA9 alleles are classified Pathogenic/Likely Pathogenic in ClinVar (e.g., RCV000030763, RCV001256639, RCV001256654).
- p.Glu257Lys (E257K) sits close to the pathogenic/benign boundary given its population frequency and incompletely penetrant homozygous state — an important VUS-adjacent caution for curators (see gnomAD data below).

**Variant type spectrum** (n=80 biallelic variants across 129 families) [PMID:34837036]:
- Missense: 67.5% (54/80) — the dominant class, unusual among LCA genes where truncating variants often predominate; consistent with NMNAT1 being an essential, ubiquitously required enzyme where complete null alleles may be embryonic-lethal or cause a more severe/different phenotype.
- Frameshift indel: 8.8%
- Nonsense: 7.5%
- Splicing: 6.3%
- Gross indel (including a genomic deletion reported in ClinVar, NC_000001.11:g.(?_9972074)_(9972188_?)del): 6.3%
- Start-loss/stop-loss/regulatory (including a 5′UTR variant c.-69C>T): 3.8%

**Population/allele frequency (gnomAD):**
- p.E257K (c.769G>A): overall ~0.07% (196/282,064 alleles); European non-Finnish ~0.122% (157/128,844) — high for a purportedly fully penetrant recessive allele, supporting its hypomorphic/reduced-penetrance status.
- Other individual pathogenic variants are typically ultra-rare (e.g., one variant at allele count 1/593,448 in gnomAD exomes), consistent with a private/founder mutational spectrum outside the E257K and R237C hotspots.

**Somatic vs. germline.** LCA9 is exclusively a germline autosomal recessive disease; no somatic *NMNAT1* variation is implicated.

**Functional consequences.** Functional/biochemical assays of LCA9-associated mutant proteins show (a) reduced NAD⁺-biosynthetic enzymatic activity and/or (b) impaired protein folding/stability, particularly under cell-stress conditions — i.e., a combination of partial loss-of-function and protein destabilization rather than a uniform null mechanism. Notably, "in many cases, LCA9-associated mutant NMNAT1 proteins retain enzymatic activity and other biochemical functions, but appear to be less stable under conditions associated with cell stress" [PMID:22842230; ScienceDirect "Characterization of Leber Congenital Amaurosis-associated NMNAT1 Mutants"].

**Modifier genes.** *SARM1* functions as a genetic modifier/downstream effector: loss of NMNAT1 activity de-represses SARM1 NADase activity, and SARM1 depletion rescues photoreceptor death in *Nmnat1*-mutant mice (see Mechanism section) — establishing SARM1 as the principal known modifier of LCA9 pathogenesis at the mechanistic level, though no human *SARM1* modifier-variant data are yet reported [eLife PMID for PMC7591247].

**Epigenetic information.** A cell-biology study ("Roles of Nmnat1 in the survival of retinal progenitors through the regulation of pro-apoptotic gene expression via histone acetylation," *Cell Death & Disease*) shows Nmnat1 regulates pro-apoptotic gene expression via histone acetylation in retinal progenitors — an NAD⁺-dependent sirtuin/deacetylase-linked epigenetic mechanism connecting NMNAT1 loss to apoptotic gene de-repression during retinal development [Nature/Cell Death Dis].

**Chromosomal abnormalities.** No recurrent large chromosomal rearrangement (aneuploidy, translocation) is described for LCA9; disease is caused by intragenic sequence variants and occasional small deletions.

**Suggested ontology terms:** HGNC:17877 (NMNAT1); GO:0000309 (nicotinamide-nucleotide adenylyltransferase activity); GO:0019677 (NAD catabolic process, for SARM1); GO:0009435 (NAD biosynthetic process).

Sources: [OMIM *608700](https://omim.org/entry/608700) | [PMID:22842230 Nature Genetics](https://www.nature.com/articles/ng.2357) | [PMC9674661](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674661/) | [ClinVar entries](https://www.ncbi.nlm.nih.gov/clinvar/RCV000030763/)

---

## 5. Environmental Information

No environmental, lifestyle, toxin, radiation, or infectious contributors to LCA9 pathogenesis are documented — it is a purely monogenic recessive disorder with disease onset determined by genotype rather than exposure. No infectious agents are implicated. This section is not applicable beyond noting general supportive-care/lifestyle considerations relevant to visual disability management (UV protection, low-vision aids), which are supportive rather than etiological.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic *NMNAT1* variants** (most commonly missense, e.g., E257K, R237C, V9M) → reduce NMNAT1 catalytic NAD⁺-biosynthetic activity and/or destabilize the folded protein, especially under cellular stress [PMID:22842230].
2. Reduced/unstable NMNAT1 activity → **local depletion of nuclear/retinal NAD⁺** within photoreceptors, demonstrated directly in a mouse model showing retina-specific NAD⁺ decrease accompanied by increased poly(ADP-ribose) accumulation [PMID:33709122].
3. NAD⁺ depletion/NMNAT1 insufficiency → **loss of inhibitory constraint on SARM1** (sterile alpha and TIR motif–containing 1), the central NADase "executioner" of programmed axon/neurite destruction — this step is **directly demonstrated** in mouse models (not merely inferred): "the essential function of NMNAT1 in photoreceptors is to inhibit SARM1" [eLife/PMC7591247].
4. Activated SARM1 → **catastrophic local NAD⁺ hydrolysis** within the photoreceptor, triggering a self-amplifying degenerative cascade mechanistically analogous to Wallerian axon degeneration (where loss of the paralogous enzyme NMNAT2 similarly de-represses SARM1 in axons) — establishing that **photoreceptor neurodegeneration in LCA9 shares a deep mechanistic parallel with the pathological axon-degeneration pathway** [PMID/PMC7591247].
5. SARM1-driven NAD⁺ catastrophe → **photoreceptor cell death** (rod and cone), demonstrated by extinguished/severely reduced ERG responses in patients and confirmed causally in mice, where genetic *Sarm1* deletion or depletion **rescues** photoreceptor survival and retinal structure/function despite ongoing NMNAT1 deficiency [eLife 62027].
6. Concurrently/upstream in development: NMNAT1 normally supports **retinal progenitor cell survival** via NAD⁺-dependent histone-acetylation-mediated repression of pro-apoptotic gene expression; NMNAT1 loss de-represses these apoptotic programs during retinal development, contributing to the **congenital failure of foveal formation** manifesting as the characteristic "macular coloboma"/pseudocoloboma (this branch is partly inferred from developmental-biology and histopathology correlation rather than direct human mechanistic proof) [Cell Death & Disease; OMIM #608553].
7. Combined developmental (branch 6) and degenerative (branches 1–5) insults → the clinical picture of **congenital/infantile severe vision loss with progressive generalized tapetoretinal degeneration, disciform macular atrophy, and early optic atrophy** characteristic of LCA9.
8. Because NMNAT1 has ubiquitous tissue expression yet LCA9 patients show **no extra-ocular systemic disease**, photoreceptors are inferred to have exceptional vulnerability to reduced NMNAT1 function — likely reflecting their unusually high metabolic/NAD⁺ demand and dependence on the nuclear NMNAT1 isoform specifically (versus cytoplasmic NMNAT2/mitochondrial NMNAT3 in other tissues), a point noted but not fully mechanistically resolved in the literature [PMID:22842230].

### Detail by category

- **Molecular pathway:** NAD⁺ salvage/biosynthesis pathway (nicotinamide → NMN → NAD⁺, catalyzed terminally by NMNAT1); intersects with the SARM1-mediated programmed axon-death pathway (a Toll/interleukin-1 receptor [TIR]-domain NADase pathway) and with sirtuin/histone-deacetylase signaling downstream of NAD⁺ availability.
- **Cellular processes:** Programmed cell death (regulated, SARM1-dependent, mechanistically related to Wallerian degeneration rather than classical caspase apoptosis in the mature-degeneration phase); apoptosis of retinal progenitors during development (histone-acetylation-mediated); failure of foveal morphogenesis.
- **Protein dysfunction:** Combination of catalytic loss-of-function and conformational/stability defects (protein less stable under cell stress) rather than simple absence of protein.
- **Metabolic changes:** Local, tissue-specific (retinal) depletion of NAD⁺; accumulation of poly(ADP-ribose) (PAR), consistent with PARP-pathway NAD⁺ consumption compounding the deficit.
- **Tissue damage mechanism:** SARM1-driven NAD⁺ catastrophe — a distinct, non-classical neurodegenerative mechanism (not oxidative-stress-driven per se, though PAR/NAD⁺ dysregulation has downstream oxidative-stress-adjacent consequences).
- **Molecular profiling:** Direct retinal NAD⁺ quantification and PAR immunodetection have been performed in the *Nmnat1*-mutant mouse retina (targeted metabolomics rather than unbiased omics) [PMID:33709122]. No published human single-cell/spatial transcriptomic or proteomic dataset specific to LCA9 retina was identified in this search (expected given the rarity of post-mortem human LCA9 ocular tissue).
- **Advanced technologies:** No CRISPR/RNAi functional-genomics screen specific to *NMNAT1* in photoreceptors was identified; conditional (photoreceptor-specific) genetic deletion in mice has been used to establish cell-autonomous requirement of NMNAT1 within photoreceptors.

**Suggested GO terms:** GO:0009435 (NAD biosynthetic process), GO:0009116 (nucleoside metabolic process), GO:0006915 (apoptotic process), GO:1901030 (positive regulation of mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway, if applicable to SARM1), GO:0097237 (cellular response to toxic substance, PAR-related), GO:0070212 (protein poly-ADP-ribosylation).
**Suggested CL terms:** CL:0000210 (photoreceptor cell), CL:0000287 (eye photoreceptor cell), CL:0002586 (retinal cone cell), CL:0002588 (retinal rod cell), CL:0011020 (retinal bipolar neuron), CL:0000740 (retinal ganglion cell).

Sources: [PMID:22842230 – NMNAT1 mutations, new disease pathway](https://www.nature.com/articles/ng.2357) | [eLife 62027 – SARM1 depletion rescues NMNAT1-dependent photoreceptor death](https://elifesciences.org/articles/62027) | [PMID:33709122 – Mutant Nmnat1 leads to retina-specific NAD+ decrease](https://pubmed.ncbi.nlm.nih.gov/33709122/) | [Cell Death & Disease – Nmnat1 histone acetylation](https://www.nature.com/articles/s41419-018-0907-0)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Eye — specifically the neurosensory retina and optic nerve.
- **Body system:** Visual system (special sense organs); no other organ systems are affected — patients have normal general physical and mental/systemic health, distinguishing LCA9 from syndromic LCA subtypes (e.g., CEP290-associated Joubert/ciliopathy overlap, ALMS1-associated Alström syndrome) [MalaCards; OMIM Clinical Synopsis].

**Tissue and cell level:**
- Neurosensory retina — all major neural layers affected: photoreceptor layer (rods and cones), bipolar cell layer, and ganglion cell layer, especially within the macula/fovea (complete loss of these layers within the coloboma-like lesion).
- Retinal pigment epithelium (RPE) — secondary pigmentary changes.
- Optic nerve — early-onset optic atrophy (unusual among LCA genes, a relative distinguishing feature of LCA9).
- Retinal vasculature — attenuation of retinal vessels.

**Cell types (Cell Ontology):**
- CL:0000210 photoreceptor cell (both CL:0002586 cone and CL:0002588 rod, both affected — "extinguished" combined rod-cone ERG in most patients)
- CL:0011020 retinal bipolar neuron
- CL:0000740 retinal ganglion cell
- CL:0002586/CL:0002588 specifically lost within the foveal coloboma lesion
- Retinal pigment epithelial cell (CL:0002586-adjacent; UBERON pigment epithelium)

**Subcellular level:** Nucleus (site of NMNAT1 catalytic activity; GO:0005634 nucleus), specifically nuclear NAD⁺ pools; secondarily, the photoreceptor outer segment/synaptic terminal machinery that depends on adequate NAD⁺ supply for survival signaling (GO:0005634 nucleus, GO:0005886 plasma membrane for transmembrane-region–containing isoforms).

**Localization:**
- Central retina (macula/fovea) — primary site of the characteristic coloboma-like atrophic lesion.
- Posterior pole and mid-periphery — generalized tapetoretinal degeneration developing by ~age 12.
- Far peripheral retina — relatively spared/milder changes.
- **Lateralization:** Bilateral and symmetric (as with essentially all LCA subtypes).

**Suggested UBERON terms:** UBERON:0000966 (retina), UBERON:0001782 (macula lutea), UBERON:0001760 (fovea centralis), UBERON:0001769 (optic nerve), UBERON:0002450 (retinal pigment epithelium).

Sources: [OMIM Clinical Synopsis #608553](https://omim.org/clinicalSynopsis/608553) | [PMC9674661](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674661/)

---

## 8. Temporal Development

**Onset:**
- Congenital to infantile — 92% of patients present within the first year of life (range: birth to 11 years, with rare later-onset milder/CORD presentations) [PMID:34837036].
- Onset pattern: acute-appearing at birth/early infancy from the caregiver's perspective (nystagmus, poor visual pursuit noted early), though the underlying process likely begins prenatally given the developmental component (failure of foveal formation).

**Progression:**
- **Structural progression is well documented:** the macular coloboma/disciform atrophic lesion enlarges with age; generalized tapetoretinal degeneration develops and is essentially universal by age 12 in the authors'-cohort data; retinal pigmentation around the macula progresses with age; optic atrophy is progressive.
- **Functional (ERG) findings are often already at floor (extinguished) from early presentation**, so ERG itself shows limited further "progression" once severely abnormal, though residual cone function in milder/CORD-spectrum patients can decline over time.
- **Disease course pattern:** Progressive rather than stable or episodic — distinguishing it from disease courses with plateau phases seen in some other LCA genotypes (e.g., RPE65, where a therapeutic window before severe photoreceptor loss underlies gene-therapy eligibility).
- **Disease duration:** Chronic, lifelong; no spontaneous remission described.

**Patterns:**
- No remission (spontaneous or treatment-induced) is described; there is currently no approved disease-modifying therapy for LCA9 to assess treatment-induced modification of the natural history.
- **Critical periods:** The apparent developmental component (foveal formation failure) suggests a prenatal/perinatal critical window for foveal maturation is already compromised before any postnatal intervention could occur, which is mechanistically important for gene-therapy timing considerations (unlike RPE65-LCA, where the retina is structurally near-normal at birth and amenable to early intervention).

Sources: [PMID:34837036 – Yi et al. 2021, Eye](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674661/) | [OMIM #608553](https://omim.org/entry/608553)

---

## 9. Inheritance and Population

**Epidemiology.**
- LCA overall (all genetic subtypes combined) has an estimated prevalence/incidence of approximately 1 in 30,000 to 1 in 81,000 births; one figure specifically cited for LCA overall is ~1 in 80,000 [search result summary citing OMIM-adjacent sources]. LCA9 (NMNAT1) is one of the rarer LCA subtypes; NMNAT1 was estimated to account for a modest fraction of molecularly solved LCA cases historically (single-digit percentage in most unselected cohorts), with the E257K founder allele inflating apparent frequency in European-ancestry cohorts specifically.
- No dedicated national/GBD-level prevalence estimate specific to LCA9 (as distinct from LCA overall) was identified in the sources reviewed — expected for an ultra-rare single-gene subtype; curators should record this as "insufficient disease-specific epidemiologic data; LCA9 estimated as a minority subtype of the ~1:30,000–1:81,000 LCA aggregate."

**Inheritance pattern.** Autosomal recessive (both alleles must carry a pathogenic *NMNAT1* variant). LCA overall is predominantly AR, though two other LCA genes (IMPDH1, OTX2) cause dominant disease and CRX can be AD or AR — NMNAT1/LCA9 itself is exclusively AR [MedlinePlus/GeneReviews-derived search summary].

**Penetrance.** For most biallelic LCA9 genotypes, penetrance is essentially complete (severe congenital phenotype). The notable exception is **homozygous E257K**, for which reduced/incomplete penetrance is documented — some homozygous individuals are reported without an overt LCA phenotype, and the milder CORD phenotype associated with certain missense combinations (including some involving E257K) further indicates variable expressivity [PMID:29674119].

**Expressivity.** Variable — ranging from classic severe congenital LCA (truncating variants) to milder cone-rod dystrophy with later onset and better-preserved acuity (select missense genotypes), demonstrating a genotype-driven variable-expressivity spectrum rather than genotype-independent stochastic variability.

**Genetic anticipation.** Not applicable/not reported (LCA9 is not a repeat-expansion disorder).

**Germline mosaicism.** Not specifically documented for *NMNAT1* in the sources reviewed, though it remains a theoretical consideration relevant to recurrence-risk counseling in any autosomal recessive condition with an apparently unaffected heterozygous parent (standard AR recurrence logic, not LCA9-specific mosaicism evidence).

**Founder effects.** The E257K allele is a well-documented **founder mutation** in individuals of European descent, confirmed by shared-haplotype analysis. R237C is the population-specific recurrent/hotspot allele in Asian cohorts, though founder-haplotype confirmation for R237C specifically was not detailed in the sources reviewed.

**Consanguinity.** As with most AR LCA subtypes, consanguineous unions increase the likelihood of biallelic rare *NMNAT1* variant homozygosity, particularly for non-founder private variants; several reported LCA9 families (e.g., Iranian, Pakistani cohorts) were identified via homozygosity mapping in consanguineous pedigrees [PMC11496044; PMC11728111].

**Carrier frequency.** Population carrier frequency for E257K alone is estimated at ~0.18% in Caucasian controls (gnomAD-consistent), i.e., roughly 1 in ~550 in European-ancestry populations carry this single allele — though because E257K is hypomorphic/incompletely penetrant, this carrier frequency substantially overestimates true biallelic-disease genetic prevalence via simple Hardy-Weinberg extrapolation, a caution curators should note explicitly.

**Population demographics.**
- **Affected populations:** LCA9 cases have been reported across European (E257K founder), Middle Eastern/Arabian (E257K also reported), East Asian (R237C hotspot; Chinese cohort in PMID:34837036), Iranian, and Pakistani (consanguineous families) populations — indicating global distribution with population-specific recurrent-allele hotspots rather than restriction to a single ethnic group.
- **Geographic distribution:** No endemic clustering beyond the founder-allele frequency differences noted above.
- **Sex ratio:** Consistent with autosomal recessive inheritance — no sex bias reported (male:female ≈ 1:1).
- **Age distribution:** By definition skewed toward pediatric/young-adult diagnosis given congenital onset, though affected individuals are followed into adulthood as a chronic lifelong condition.

Sources: [PMID:34837036 combined cohort](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674661/) | [PMID:29674119 E257K penetrance](https://pubmed.ncbi.nlm.nih.gov/29674119/) | [PMC11496044 Iranian cohort](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11496044/) | [PMC11728111 Pakistani cohort](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11728111/)

---

## 10. Diagnostics

**Clinical tests:**
- **Electroretinography (ERG):** Central to diagnosis — full-field ERG is undetectable or markedly diminished/extinguished for both rod and cone responses in classic LCA9; this is the key functional test distinguishing LCA from other causes of infantile visual impairment (cortical visual impairment, congenital nystagmus, optic nerve hypoplasia), since LCA is essentially the only entity in the "connatal blindness" differential with an absent/severely abnormal ERG.
- **Fundus examination/fundus photography:** Reveals the disciform/nummular macular atrophy ("pseudocoloboma"), attenuated vessels, and progressive pigmentary tapetoretinal degeneration.
- **Optical coherence tomography (OCT):** Demonstrates loss of the outer retina within the macular atrophic region and diffuse retinal atrophy in surrounding areas; a key structural biomarker for both diagnosis and (in a therapeutic-trial context) monitoring of residual retinal structure.
- **Visual evoked potential (VEP):** Used adjunctively in the broader LCA diagnostic workup to help distinguish retinal from cortical causes of infantile blindness (general LCA practice; not NMNAT1-specific in the sources reviewed).

**Biopsy/pathology:** Not part of standard clinical diagnosis (retina is imaged, not biopsied); histopathologic descriptions of the coloboma-like lesion derive from clinical OCT/imaging correlation and comparative animal-model histology rather than routine human biopsy.

**Genetic testing (primary route to definitive LCA9 diagnosis):**
- Given the genetic heterogeneity of LCA (>27 genes), the standard approach is a **multi-gene retinal dystrophy/LCA panel** or **exome sequencing** (given ≥75% of LCA cases are now molecularly solvable) rather than single-gene *NMNAT1* testing as a first step, reserving targeted *NMNAT1* sequencing for cases with a suggestive phenotype (macular coloboma + early optic atrophy) or known population-specific founder-allele screening (e.g., targeted E257K testing in European-ancestry patients, R237C in East Asian patients).
- Whole-exome sequencing (WES) and whole-genome sequencing (WGS) are both used, particularly for cases where panel testing is uninformative or where consanguinity suggests homozygosity mapping could be informative.
- Chromosomal microarray/karyotype/FISH: not indicated for NMNAT1-driven LCA9 specifically (no recurrent structural chromosomal etiology).
- Molecular confirmation is essential for prognostic counseling (LCA9 lacks syndromic extra-ocular risk unlike some other LCA genes) and for determining eligibility for any future gene-specific therapy or clinical trial.

**Clinical diagnostic criteria/differential diagnosis:** LCA is diagnosed on the combination of (1) severe visual impairment from birth/early infancy, (2) nystagmus, (3) sluggish/absent pupillary responses, and (4) an undetectable or severely abnormal full-field ERG. Differential diagnoses to exclude include congenital stationary night blindness, achromatopsia, cortical visual impairment, congenital motor nystagmus without retinal disease, optic nerve hypoplasia, and other early-onset retinal dystrophies (specific gene assignment then relies on molecular testing, since fundus phenotypes overlap substantially across LCA genes — though the macular-coloboma-plus-early-optic-atrophy combination is a relatively distinguishing clinical clue for NMNAT1).

**Screening.** No population-based newborn screening program specifically targets LCA/LCA9 (it is not detected by standard metabolic newborn screening panels); diagnosis relies on clinical recognition of infantile visual impairment/nystagmus prompting ophthalmologic and subsequent genetic referral. Carrier screening and prenatal/preimplantation genetic testing are available on a familial basis once a proband's causative variants are identified, and are particularly relevant in populations/families with known consanguinity or the E257K founder allele.

**Suggested LOINC/NCIT context:** Full-field ERG (LOINC concept for electroretinography), OCT imaging codes; NCIT:C15709-type genetic-testing procedure terms for exome sequencing.

Sources: [PMC9674661](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674661/) | general LCA diagnostic framework from [EyeWiki](https://eyewiki.org/Leber_Congenital_Amaurosis) and search-derived GeneReviews summary

---

## 11. Outcome/Prognosis

**Survival/mortality.** LCA9 is not associated with reduced life expectancy or systemic mortality — patients have normal general physical and mental health outside the visual system; mortality data specific to LCA9 are not a meaningful metric for this ocular-limited, non-syndromic disorder.

**Morbidity/function.**
- Profound, essentially lifelong visual disability: 89.5% of evaluable patients have visual acuity ≤0.05 Snellen (legal blindness), with the majority progressing to severe generalized tapetoretinal degeneration by age 12.
- Functional impact: dependence on low-vision rehabilitation, mobility training (cane/guide-dog training in adulthood), Braille/assistive-technology literacy education, and psychosocial support; no LCA9-specific validated quality-of-life instrument data were identified.

**Disease course/complications.**
- Progressive enlargement of the macular atrophic lesion and worsening peripheral tapetoretinal degeneration over the first one to two decades of life.
- Early-onset optic atrophy is a relatively distinguishing complication of NMNAT1-driven disease compared with several other LCA genotypes, and may reflect combined retinal ganglion cell loss plus a possible direct optic-nerve component of NMNAT1 deficiency.
- No systemic/extra-ocular complications reported (again distinguishing LCA9 from syndromic LCA subtypes).
- **Recovery potential:** None with current standard of care (no disease-modifying or curative treatment approved); recovery potential from any future intervention would depend heavily on the degree of residual retinal structure/photoreceptor survival at the time of treatment, and the described early/congenital component of foveal-formation failure is a significant prognostic caveat for any anatomically-restorative gene therapy approach.

**Prognostic factors.**
- **Genotype** is the dominant identified prognostic factor: truncating variants track with the most severe classic-LCA phenotype, while certain hypomorphic missense genotypes (including some E257K combinations) track with milder cone-rod dystrophy and better-preserved acuity — making genotype a directly actionable prognostic biomarker in this disease [PMID:34837036].
- No independent biomarker beyond genotype (e.g., no validated blood/serum prognostic biomarker) was identified in the literature reviewed.

Sources: [PMC9674661](https://pmc.ncbi.nlm.nih.gov/articles/PMC9674661/) | [PMID:29674119](https://pubmed.ncbi.nlm.nih.gov/29674119/)

---

## 12. Treatment

**Current standard of care.** There is currently **no FDA/EMA-approved disease-specific therapy for LCA9**; management is exclusively supportive:
- **Supportive care:** Low-vision aids, magnification devices, mobility/orientation training, and educational support services (special education resources for visually impaired children).
- **Rehabilitation:** Occupational therapy for adaptive living skills; orientation and mobility (O&M) training.
- **Genetic counseling:** Recurrence-risk counseling for parents (25% recurrence risk per pregnancy for AR inheritance), carrier testing for at-risk relatives, and reproductive options (prenatal diagnosis, preimplantation genetic testing) once the family's causative *NMNAT1* variants are known.
- **UV/light protection:** Standard general retinal-dystrophy advice (sunglasses), though no NMNAT1-specific evidence base for this was identified.

**Investigational/preclinical therapeutics (not yet in human trials, per the literature reviewed):**
- **AAV gene augmentation therapy:** Subretinal delivery of AAV vectors carrying wild-type human *NMNAT1* has been shown to **preserve retinal structure and function** in the *Nmnat1*-mutant mouse model of LCA9 — the leading preclinical translational strategy for this gene [PMID:32775493, ScienceDirect Mol Ther Methods Clin Dev]. As of the sources reviewed (search conducted September 2026), **no NMNAT1-specific AAV gene-therapy clinical trial was identified as actively recruiting or completed on ClinicalTrials.gov** — this contrasts with several other LCA genes (RPE65 [approved: voretigene neparvovec/Luxturna], CEP290, GUCY2D, LCA5, AIPL1) that have or have had gene-therapy trials. This is an important, explicit evidence gap: **absence of an active human trial for NMNAT1 gene therapy, not merely absence of information**, per the searches performed.
- **SARM1 inhibition:** Genetic *Sarm1* depletion rescues NMNAT1-dependent photoreceptor death and preserves retinal structure/function in mice, nominating SARM1 as a **therapeutic target** (pharmacologic SARM1 inhibitors are in development broadly for neurodegeneration, including patented NADase-inhibitor compounds, but no NMNAT1/LCA9-specific human clinical application was identified) [eLife 62027; USPTO patents on SARM1 NADase inhibitors].
- **NAD⁺ repletion (nicotinamide riboside, NR):** Systemic NR supplementation increases retinal NAD⁺ and is protective in multiple mouse models of retinal degeneration (including light-induced retinopathy models), suppressing microglial activation and photoreceptor damage — a NAD⁺-precursor pharmacologic strategy directly conceptually relevant to NMNAT1 deficiency, though the specific efficacy of NR in an *Nmnat1*-mutant (LCA9) mouse model specifically versus other retinal-degeneration models was not confirmed as tested in the sources reviewed and requires direct verification before being cited as LCA9-specific evidence [PMC11980955; bioRxiv "Systemic Treatment with Nicotinamide Riboside is Protective in Three Mouse Models of Retinal Degeneration"].

**Pharmacogenomics.** Not applicable — no approved pharmacotherapy exists to have pharmacogenomic considerations for LCA9 specifically.

**Experimental treatments in clinical trials.** None identified with an NCT identifier specifically for NMNAT1/LCA9 in the searches performed; broader LCA gene-therapy trials identified (NCT02781480 general LCA gene therapy trial, NCT06088992 "LIGHT" trial, NCT01208389 RPE65 follow-on trial) were not confirmed to include NMNAT1-genotype patients and should be verified individually before citation in a curation entry.

**Suggested NCIT terms:** NCIT:C15238 (Gene Therapy — for the preclinical AAV-NMNAT1 approach), NCIT:C15240 (Genetic Counseling), NCIT:C15302 (Physical Therapy — general low-vision/O&M context), NCIT:C15747 (Supportive Care).

Sources: [PMID:32775493 – AAV gene therapy preserves retinal structure in NMNAT1 mouse model](https://pubmed.ncbi.nlm.nih.gov/32775493/) | [eLife 62027 – SARM1 depletion rescues photoreceptor death](https://elifesciences.org/articles/62027) | [Retina Today – Top IRDs to Watch: LCA (2025)](https://retinatoday.com/articles/2025-july-aug/top-irds-to-watch-leber-congenital-amaurosis) | [PMC11980955 – Nicotinamide riboside retinal protection](https://pmc.ncbi.nlm.nih.gov/articles/PMC11980955/)

---

## 13. Prevention

**Primary prevention.** No means of preventing *NMNAT1* mutation occurrence exists (germline mutation); primary "prevention" of an affected birth is achieved only through reproductive genetic counseling and prenatal/preimplantation genetic testing once a family's causal variants are known — not through modifiable risk-factor reduction, since there are no environmental risk factors.

**Secondary prevention.** No population-level screening program for LCA9 exists (not on standard newborn screening panels). Early clinical recognition of infantile nystagmus/poor visual behavior prompting rapid ophthalmologic and genetic evaluation is the practical "secondary prevention" equivalent, enabling earlier low-vision intervention and family counseling (though it does not alter the underlying degenerative course given the absence of disease-modifying therapy).

**Tertiary prevention.** Management of complications through comprehensive low-vision rehabilitation, monitoring for progression of macular atrophy and optic atrophy via serial OCT/fundus imaging, and psychosocial/educational support to minimize functional disability.

**Immunization.** Not applicable.

**Screening/early detection:**
- **Carrier screening:** Targeted *NMNAT1* carrier testing (e.g., for E257K in European-ancestry individuals, R237C in East Asian individuals) can be offered in expanded carrier-screening panels or to at-risk relatives of a known proband, though *NMNAT1* is not typically included in general population pan-ethnic expanded carrier screens outside dedicated inherited-retinal-disease panels.
- **Genetic screening for reproductive planning:** Preimplantation genetic testing (PGT-M) and prenatal diagnosis (chorionic villus sampling/amniocentesis with targeted variant testing) are available once parental variants are identified.
- **Risk stratification:** Consanguinity and known founder-allele carrier status (E257K, R237C) in the relevant ancestral populations are the principal risk-stratification signals used clinically.

**Behavioral interventions.** Not applicable (no modifiable behavioral risk factor).

**Genetic counseling.** Central to LCA9 prevention/family-planning practice: recurrence-risk counseling (25% per pregnancy for unaffected carrier parents), discussion of variable expressivity/reduced penetrance particularly for E257K-containing genotypes (important for accurate risk communication, since homozygous E257K does not guarantee a penetrant phenotype), and coordination of prenatal/preimplantation testing options.

**Public health/environmental interventions.** Not applicable (no environmental risk factor to mitigate).

**Prophylaxis.** No pharmacologic prophylaxis is established; the preclinical NAD⁺-repletion (nicotinamide riboside) and SARM1-inhibition strategies described in Section 12 are investigational and not validated as human prophylactic interventions.

Sources: as cited above; general genetic-counseling framework consistent with standard AR inherited-retinal-disease practice (ACMG/NSGC guidance, not individually re-cited here as no LCA9-specific guideline document was retrieved in this search).

---

## 14. Other Species / Natural Disease

**Taxonomy/orthology:**
- Mouse *Nmnat1* ortholog: **MGI:1913704** (nicotinamide nucleotide adenylyltransferase 1), NCBI Taxon:10090 (*Mus musculus*).
- Human: NCBI Taxon:9606.

**Naturally occurring disease in other species.** No naturally occurring (spontaneous) canine, feline, or other companion-animal *NMNAT1*-associated retinal degeneration was identified in the sources reviewed (unlike, e.g., RPE65 disease, which has a well-characterized naturally occurring Briard-dog model). No OMIA entry for a spontaneous NMNAT1 veterinary phenotype was surfaced in this search; if none exists, LCA9 modeling relies entirely on **engineered/induced** rather than **naturally occurring** animal disease.

**Comparative biology.** The core disease mechanism — NAD⁺-biosynthesis-enzyme loss de-repressing SARM1-mediated programmed neurite/cell destruction — is evolutionarily conserved and directly parallels the well-established Wallerian axon-degeneration pathway (NMNAT2/SARM1 in peripheral axons), indicating strong mechanistic conservation across neuronal cell types and, implicitly, across mammalian species, even though no spontaneous non-human disease has been documented.

**Zoonotic potential / cross-species susceptibility.** Not applicable — LCA9 is a non-infectious, purely genetic disorder with no zoonotic dimension.

Sources: [MGI:1913704](https://www.informatics.jax.org/marker/MGI:1913704)

---

## 15. Model Organisms

**Mouse models (the dominant experimental system for LCA9):**
- **Conditional/engineered *Nmnat1*-deficient mice** (both widespread adult-inducible depletion and photoreceptor-specific conditional knockout models) have been used to establish (a) that photoreceptors are exquisitely vulnerable to NMNAT1 loss compared with other tissues despite its ubiquitous expression, (b) that NMNAT1 is required cell-autonomously within the photoreceptor (via conditional deletion), and (c) that these models faithfully mirror the selective photoreceptor loss seen in human LCA9 [PMID:22842230 and related mechanistic follow-ups].
- **Point-mutant "LCA9-model" mice** carrying disease-relevant missense alleles have been used to demonstrate retina-specific NAD⁺ decline and poly(ADP-ribose) accumulation, directly linking genotype to the proposed NAD⁺-depletion mechanism [PMID:33709122].
- **Sarm1-knockout / Sarm1-depleted crosses onto the *Nmnat1*-mutant background** demonstrate that genetic ablation of SARM1 rescues photoreceptor survival and retinal structure/function despite persistent NMNAT1 deficiency — the single most important mechanistic/therapeutic-target-validating model in the field [eLife 62027/PMC7591247].
- **AAV-NMNAT1 gene-augmentation-treated *Nmnat1*-mutant mice** show preserved retinal structure and function following subretinal AAV delivery of wild-type human *NMNAT1*, the principal translational proof-of-concept model for a future human gene therapy [PMID:32775493].
- A note on nomenclature: the widely used **rd9** mouse retinal-degeneration allele is a distinct, X-linked *Rpgr*-associated model (unrelated to *Nmnat1*/LCA9) — searches for an "Rd9–NMNAT1" connection did not surface a validated link, and curators should **not** conflate rd9 with an NMNAT1 model; no evidence of such a link was found despite a targeted search.

**Model characteristics:**
- **Phenotype recapitulation:** High fidelity for the core degenerative phenotype — selective, progressive photoreceptor loss, retinal NAD⁺ depletion, and SARM1-dependence are all reproduced. However, whether existing mouse models recapitulate the human-distinctive **macular coloboma/foveal-formation-failure** phenotype is intrinsically limited, because **mice lack a fovea** — this is a structural/comparative-anatomy limitation, not merely an unresolved research question, and should be flagged explicitly as a **HUMAN_MODEL_MISMATCH**-type caveat for any pathophysiology node modeling the foveal-coloboma phenotype from mouse data.
- **Model limitations:** Afoveate murine retinal anatomy limits translational inference specifically for the macular/foveal component of the human phenotype; systemic/extra-retinal consequences of NMNAT1 loss (if any) may also differ between global versus photoreceptor-conditional mouse models and the human ubiquitous-but-retina-restricted phenotype.

**Zebrafish/invertebrate/other models.** No *NMNAT1*-specific zebrafish knockdown or *Drosophila*/*C. elegans nmnat*-ortholog retinal-degeneration model directly modeling human LCA9 was identified in the searches performed (zebrafish *nmnat* biology has been studied in other contexts, e.g., mouse *Nmnat2* in retinal explants, but a dedicated NMNAT1/LCA9 zebrafish disease model was not surfaced) — this should be recorded as an explicit **absence of evidence** rather than assumed non-existence, since a more exhaustive literature search (e.g., via ZFIN directly) could not be completed within this session.

**Cellular/iPSC models.** No human iPSC-derived retinal organoid model specific to *NMNAT1*/LCA9 was identified in the sources reviewed in this session; this represents a plausible but unconfirmed gap that would benefit from a dedicated follow-up search (e.g., via GEO/Human Cell Atlas/Cellosaurus).

**Research applications.** Current mouse models have primarily been used to (1) establish the SARM1-dependent mechanism, (2) validate NAD⁺-repletion and SARM1-inhibition as therapeutic strategies, and (3) demonstrate proof-of-concept AAV gene-augmentation efficacy — i.e., mechanistic dissection and preclinical therapeutic validation, rather than natural-history/longitudinal-progression modeling (given the mouse's afoveate limitation for the human-defining macular phenotype).

**Resources.** MGI (Mouse Genome Informatics) — MGI:1913704 for gene-level mouse data and associated allele/phenotype records.

Sources: [PMID:22842230](https://www.nature.com/articles/ng.2357) | [eLife 62027](https://elifesciences.org/articles/62027) | [PMID:33709122](https://pubmed.ncbi.nlm.nih.gov/33709122/) | [PMID:32775493](https://pubmed.ncbi.nlm.nih.gov/32775493/) | [MGI:1913704](https://www.informatics.jax.org/marker/MGI:1913704)

---

## Summary Table: Key Identifiers for KB Entry

| Field | Value |
|---|---|
| Disease name | Leber Congenital Amaurosis 9 |
| MONDO | MONDO:0012056 |
| OMIM phenotype | #608553 |
| OMIM gene | *608700 |
| Orphanet | ORPHA:65 (general LCA entry) |
| Causal gene | NMNAT1 (HGNC:17877), 1p36.22 |
| Inheritance | Autosomal recessive |
| Key founder allele (EU) | c.769G>A p.Glu257Lys (hypomorphic, reduced penetrance) |
| Key hotspot allele (Asia) | c.709C>T p.Arg237Cys |
| Hallmark phenotype | Congenital nystagmus + extinguished ERG + macular coloboma ("pseudocoloboma") + early optic atrophy |
| Core mechanism | NMNAT1 loss → local NAD⁺ depletion → SARM1 de-repression → SARM1-driven photoreceptor death (Wallerian-degeneration-like pathway) |
| Approved therapy | None (supportive care only); AAV-NMNAT1 gene therapy and SARM1 inhibition are preclinical (mouse) only |

---

## Notable Evidence Gaps (flagged explicitly per instructions)

1. **No confirmed active human clinical trial for NMNAT1-specific gene therapy** was located — this is a documented absence, not an unsearched topic.
2. **GeneReviews full-text access was blocked** (CAPTCHA) during this session; the NMNAT1-specific management/surveillance recommendations that GeneReviews' "Nonsyndromic LCA/EOSRD Overview" chapter would normally provide should be independently verified against that source (NCBI Bookshelf NBK531510) before final KB entry, as this report's diagnostic/management content was reconstructed from secondary search-result summaries rather than the primary chapter text.
3. **OMIM full clinical synopsis page was blocked** (HTTP 403); synopsis details above are drawn from search-engine-returned excerpts rather than the complete OMIM record and should be re-verified directly against omim.org before citation with a `reference: OMIM:608553` evidence item.
4. Population-level LCA9-specific prevalence (distinct from aggregate LCA prevalence) was **not found** and should be recorded as `NOT_YET_DOCUMENTED` rather than estimated.
5. No naturally-occurring veterinary/OMIA model and no confirmed NMNAT1-specific zebrafish or iPSC/organoid model were located in this search session; absence should be treated as an evidence gap pending a more targeted follow-up search rather than definitive non-existence.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 12 |
| On topic | 11 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:22842230`: "in many cases, LCA9-associated mutant NMNAT1 proteins retain enzymatic activity and other biochemical functions, but appear to be less stable under conditions associated with cell stress"
  - closest text in source: "To further examine the impact of these mutations on enzymatic activity, we performed in vitro assays using affinity-purified wild-type and mutant NMNAT1 proteins"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 31 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012056` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Leber congenital amaurosis 9**
- `HP:0000639` (1 mention) - the report calls it "Nystagmus (often roving/searching)"; HP calls it **Nystagmus**
- `HP:0009466` (1 mention) - the report calls it "Abnormal pupillary function"; HP calls it **Radial deviation of finger**
- `HP:0000640` (1 mention) - the report calls it "Oculodigital sign (eye poking/pressing)"; HP calls it **Gaze-evoked nystagmus**
- `HP:0000546` (1 mention) - the report calls it "Abnormal electroretinogram"; HP calls it **Retinal degeneration**
- `HP:0000539` (1 mention) - the report calls it "High hyperopia (less prominent than some other LCA genes)"; HP calls it **Abnormality of refraction**
- `CL:0002588` (3 mentions) - the report calls it "retinal rod cell"; CL calls it **smooth muscle cell of the umbilical vein**
- `CL:0011020` (2 mentions) - the report calls it "retinal bipolar neuron"; CL calls it **neural progenitor cell**
- `UBERON:0001782` (1 mention) - the report calls it "macula lutea"; UBERON calls it **pigmented layer of retina**
- `UBERON:0001769` (1 mention) - the report calls it "optic nerve"; UBERON calls it **iris**
- `UBERON:0002450` (1 mention) - the report calls it "retinal pigment epithelium"; UBERON calls it **decidua**
- `NCIT:C15238` (1 mention) - the report calls it "Gene Therapy — for the preclinical AAV-NMNAT1 approach"; NCIT calls it **Gene Therapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007843` (1 mention) - the report calls it "Attenuated retinal vessels"; HP calls it **Attenuation of retinal blood vessels**
- `GO:0019677` (1 mention) - the report calls it "NAD catabolic process, for SARM1"; GO calls it **NAD+ catabolic process**
- `GO:0097237` (1 mention) - the report calls it "cellular response to toxic substance, PAR-related"; GO calls it **cellular response to toxic substance**
- `CL:0002586` (4 mentions) - the report calls it "retinal cone cell"; CL calls it **retinal pigment epithelial cell**
- `UBERON:0001760` (1 mention) - the report calls it "fovea centralis"; UBERON calls it **frontal sinus**
- `NCIT:C15302` (1 mention) - the report calls it "Physical Therapy — general low-vision/O&M context"; NCIT calls it **Physical Therapy**, and lists "Physical Therapeutics" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `ORPHA:65` - called "Leber congenital amaurosis, general entry cross-referencing NMNAT1", "general LCA entry"
- `HGNC:17877` - called "gene symbol NMNAT1", "NMNAT1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`, `Taxon`.