---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-10-31T16:55:11.287780'
end_time: '2026-10-31T16:59:04.047371'
duration_seconds: 232.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Marburg Virus Disease
  mondo_id: MONDO:0020500
  category: Infectious
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Green monkey disease; MHF; Marburg disease
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
  - claude-haiku-5-5
  - claude-opus-4-8
  - claude-opus-5-5
  num_turns: 2
  total_cost_usd: 0.546716
  session_id: 2ccff955-20d8-5bb4-8e86-b52d55e2a947
  stop_reason: end_turn
  assistant_text_blocks: 1
fell_back: true
requested_provider: openai
provider_attempts:
- provider: openai
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - PMID:25822829
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 73
  verified: 66
  not_found: 2
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.029
  labels_checked: 37
  labels_matching: 16
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: NCBITaxon:9407
    reported_labels:
    - Reservoir host:** **Egyptian rousette fruit bat, *Rousettus aegyptiacus
    ontology_label: Rousettus aegyptiacus
  - term_id: HP:0025145
    reported_labels:
    - "Chills \u2014 verify"
    ontology_label: Rigors
  - term_id: HP:0100737
    reported_labels:
    - "Pharyngitis \u2014 verify"
    ontology_label: Abnormal hard palate morphology
  - term_id: HP:0000525
    reported_labels:
    - "Conjunctivitis/injection \u2014 verify"
    ontology_label: Abnormality iris morphology
  - term_id: HP:0011877
    reported_labels:
    - "Gastrointestinal hemorrhage \u2014 verify"
    ontology_label: Increased mean platelet volume
  - term_id: UBERON:0002107
    reported_labels:
    - liver
    - Primary organs:** **liver
    ontology_label: liver
  - term_id: UBERON:0002113
    reported_labels:
    - kidney
    - Secondary involvement:** **kidney
    ontology_label: kidney
  - term_id: GO:0039712
    reported_labels:
    - verify
    ontology_label: obsolete induction by virus of host catalytic activity
  labels_variant: 13
  unresolved_terms:
  - HP:0003681
  - HP:0007498
  obsolete_terms:
  - term_id: GO:0039712
    ontology_label: obsolete induction by virus of host catalytic activity
  unresolvable_prefixes:
  - ORPHA
  - LOINC
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Marburg Virus Disease
- **MONDO ID:** MONDO:0020500 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Green monkey disease; MHF; Marburg disease
- **Category:** Infectious

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Marburg Virus Disease** covering all of the
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

I'll produce the research report now. Marburg Virus Disease is a legitimate, well-documented topic in the biomedical literature (WHO, CDC, and extensive peer-reviewed virology/clinical research), and a disease knowledge-base entry covering its clinical features, pathophysiology, epidemiology, diagnosis, treatment, and prevention is standard defensive/educational medical content. Below is a comprehensive narrative report.

A caution the dismech workflow demands up front: **the PMIDs below are provided as research leads and must each be re-fetched and snippet-verified (`just fetch-reference`, `just preflight-dr`) before any is written into a KB YAML entry.** Where I am not confident a specific PMID is correct, I say so rather than present a fabricated identifier as fact.

---

# Marburg Virus Disease — Disease Characteristics Research Report

**Target:** Marburg Virus Disease · **MONDO:0020500** · Category: Infectious

## Causal agent (not a host gene)

Marburg Virus Disease (MVD) is an acute, frequently fatal viral hemorrhagic fever. **It has no causal host gene** — the template's "Causal gene(s): not recorded" is correct and should remain so. The disease is caused by infection with **Marburg virus (MARV)** and the closely related **Ravn virus (RAVV)**, two members of the species *Orthomarburgvirus marburgense* (genus *Orthomarburgvirus*, formerly *Marburgvirus*), family **Filoviridae**, order *Mononegavirales* — the same family as *Ebolavirus*. The "genes" relevant to this entry are therefore the **seven viral genes** (3′-NP–VP35–VP40–GP–VP30–VP24–L-5′), not human genes. Any `genetic:` content should describe the viral genome and, where relevant, host **susceptibility/entry-factor** genes (notably *NPC1*), never a Mendelian causal gene.

---

## 1. Disease Information

**Overview.** MVD is a zoonotic filoviral hemorrhagic fever characterized by abrupt high fever, severe systemic illness, gastrointestinal and hemorrhagic manifestations, and multi-organ dysfunction with shock. Case-fatality ratios (CFR) across recorded outbreaks range from ~24% to ~90%, averaging roughly 50% (WHO). It was the **first filovirus ever recognized**, identified in 1967 after simultaneous outbreaks among laboratory workers in Marburg and Frankfurt (Germany) and Belgrade (then Yugoslavia) who handled tissues and cell cultures from African green monkeys (*Chlorocebus/Cercopithecus aethiops*) imported from Uganda (Siegert et al., 1967; Martini & Siegert, classic descriptions — PMIDs to verify).

**Key identifiers.**
- **MONDO:** MONDO:0020500 (Marburg hemorrhagic fever / Marburg virus disease).
- **ICD-10:** A98.3 ("Marburg virus disease"). **ICD-11:** 1D60.1 (Marburg virus disease) under viral haemorrhagic fevers.
- **MeSH:** D008379 "Marburg Virus Disease"; agent "Marburgvirus" (MeSH D008380).
- **Orphanet:** ORPHA:319218 (Marburg hemorrhagic fever) — verify code.
- **NCBITaxon:** Orthomarburgvirus marburgense / Marburg marburgvirus (NCBITaxon:3052505 / legacy 11269 for "Marburg marburgvirus" — verify against current NCBI Taxonomy, which was restructured when ICTV renamed the genus).
- **OMIM:** Not applicable (not a Mendelian disease).

**Synonyms.** Marburg hemorrhagic fever (MHF); Marburg disease; "green monkey disease" (historical, from the 1967 index exposure); Marburg virus disease (current WHO-preferred term).

**Data derivation.** Disease-level, aggregated resources (WHO outbreak reports, CDC, Orphanet, peer-reviewed outbreak case series). Not EHR/individual-patient derived; cohorts are small outbreak clusters.

---

## 2. Etiology

**Causal factor:** Infectious — MARV/RAVV (Filoviridae). This is the sole cause; there is no genetic etiology of the disease itself.

**Risk factors (exposure).**
- **Reservoir contact:** Entry into caves/mines inhabited by the **Egyptian rousette fruit bat, *Rousettus aegyptiacus*** (NCBITaxon:9407) — the confirmed natural reservoir (Towner et al., 2009, *PLoS Pathogens*, PMID:19649327 — verify). Classic cohorts: miners at Goroumbwala/Durba (DRC, 1998–2000) and tourists/workers at Python Cave, Maramagambo Forest, Uganda.
- **Occupational:** Mining, bat-exposed tourism/caving, healthcare work, laboratory handling of filoviruses (BSL-4).
- **Human-to-human:** Direct contact with blood, secretions, organs, or other bodily fluids of infected (living or dead) persons, and with contaminated surfaces/materials; nosocomial amplification and **unsafe burial practices** are major drivers.
- **Demographics:** All ages/sexes susceptible; occupational exposure skews adult male in mining clusters, but this reflects exposure, not biological susceptibility.

**Protective factors.** No proven host genetic protective variant is established for MVD specifically. By analogy to filovirus entry biology, loss-of-function in the entry receptor **NPC1** confers resistance in cell/animal models (homozygous *Npc1* null mice resist filovirus challenge; Carette et al., 2011, *Nature*, PMID:21866103 — verify), but no human protective allele is clinically demonstrated. Protection in practice is behavioral/public-health: avoiding bat-roost exposure, infection prevention and control (IPC), safe burials, and, in outbreaks, candidate vaccines (investigational).

**Gene–environment interactions.** Not characterized in humans beyond the receptor biology above. Host response genetics (interferon pathway, HLA) are plausibly relevant to outcome but not established — flag as a knowledge gap.

---

## 3. Phenotypes

Clinical course is typically **triphasic**: (1) generalization phase (days 1–4), (2) early organ phase (days 5–13), (3) late organ/convalescence or terminal phase. Frequencies below are approximate, drawn from outbreak case series (notably Angola 2004–05 and DRC 1998–2000) and WHO descriptions; outbreak-specific proportions vary widely and should be cited to the specific series.

**Generalization phase (abrupt onset):**
- **Fever, high** — near-universal. HP:0001945 (Fever).
- **Severe headache** — very frequent. HP:0002315 (Headache).
- **Severe malaise / prostration** — very frequent. HP:0003681 (fatigable; or HP:0025406 asthenia — verify).
- **Myalgia and arthralgia** — frequent. HP:0003326 (Myalgia); HP:0002829 (Arthralgia).
- **Chills/rigors** — frequent. HP:0025145 (Chills — verify).

**Gastrointestinal (days ~3–7):**
- **Watery diarrhea** (often severe, cholera-like, major fluid loss) — very frequent. HP:0002014 (Diarrhea).
- **Nausea and vomiting** — very frequent. HP:0002018 (Nausea); HP:0002013 (Vomiting).
- **Abdominal pain and cramping** — frequent. HP:0002027 (Abdominal pain).
- **Anorexia** — frequent. HP:0002039 (Anorexia).

**Mucocutaneous:**
- **Non-pruritic maculopapular rash** (~day 2–7, often trunk) — reported in a substantial minority to majority depending on series. HP:0000988 (Skin rash) / HP:0000509? — use HP:0007498 (Maculopapular exanthema — verify).
- **Pharyngitis/odynophagia, conjunctival injection** — frequent. HP:0100737 (Pharyngitis — verify); HP:0000525 (Conjunctivitis/injection — verify).
- **Characteristic "ghost-like" facies** — drawn, expressionless features with deep-set eyes (classic clinical description).

**Hemorrhagic manifestations (days ~5–7 onward; marker of severe disease):**
- **Bleeding — GI (hematemesis, melena), petechiae/ecchymoses, bleeding from venipuncture sites, gingival, vaginal** — frequent in fatal cases. HP:0001892 (Abnormal bleeding) / HP:0011877 (Gastrointestinal hemorrhage — verify); HP:0000421 (Epistaxis); HP:0000978 (Bruising susceptibility/ecchymoses).
- **Disseminated intravascular coagulation (DIC)** — in severe disease.

**Hematologic/laboratory abnormalities:**
- **Thrombocytopenia** — frequent. HP:0001873. LOINC:777-3 (Platelets).
- **Early leukopenia / lymphopenia**, later neutrophilia with left shift. HP:0001882 (Leukopenia); HP:0001888 (Lymphopenia). LOINC:6690-2 (WBC).
- **Marked transaminase elevation (AST often > ALT)** — frequent, reflecting hepatocellular injury. HP:0002910 (Elevated hepatic transaminase). LOINC:1920-8 (AST).
- **Coagulopathy:** prolonged PT/PTT, elevated D-dimer, hypofibrinogenemia.
- **Renal:** elevated creatinine/BUN, proteinuria, oliguria → AKI. HP:0012100 (Abnormal circulating creatinine); HP:0000083 (Renal insufficiency).
- **Electrolyte/metabolic:** hypokalemia, hyponatremia, metabolic acidosis (from fluid losses).
- **Pancreatitis** (elevated amylase) in some.

**Neurological (later phase, often poor-prognosis):**
- **Confusion, irritability, agitation, encephalopathy/delirium** — frequent in severe disease. HP:0001289 (Confusion — verify); HP:0002353 (EEG abnormality if documented).
- **Seizures, coma** — terminal.

**Cardiovascular / terminal:**
- **Hypotension and shock** (distributive + hypovolemic), multi-organ failure — the usual proximate cause of death. HP:0001635/HP:0002615 (Hypotension — verify).

**Age of onset:** Acute, within 2–21 days of exposure (any age). **Severity:** severe/life-threatening. **Progression:** rapid (illness to death often within 8–9 days of symptom onset in fatal cases). **Quality-of-life impact:** profound acute incapacitation; survivors may have prolonged convalescence (see §11 sequelae).

---

## 4. Genetic / Molecular Information (viral)

**Genome.** ~19 kb negative-sense, non-segmented, single-stranded RNA. Seven genes in fixed order: **NP** (nucleoprotein), **VP35** (polymerase cofactor; type I IFN antagonist), **VP40** (matrix protein; budding, and also an IFN antagonist via Jak/STAT), **GP** (the single surface glycoprotein; mediates attachment and entry), **VP30** (transcription activator), **VP24** (minor matrix/assembly; distinct from Ebola VP24 in IFN strategy), **L** (RNA-dependent RNA polymerase). (Review: Feldmann & Geisbert, *Lancet* 2011, PMID:21084112 — covers filoviral HF generally; verify.)

**Entry biology / host factors.**
- **GP** is the sole envelope protein; it is cleaved by host cathepsins in the endosome to expose the receptor-binding domain.
- **Intracellular receptor: NPC1 (Niemann-Pick C1)** — essential for filovirus membrane fusion (Carette et al., 2011, PMID:21866103; Côté et al., 2011, *Nature*, PMID:21866101 — verify).
- **Attachment factors:** C-type lectins (DC-SIGN, L-SIGN), TIM-1, Axl, and others facilitate uptake, especially in macrophages/dendritic cells.

**Variant/strain notes.** Not a "pathogenic variant" disease in the human-genetics sense. Relevant diversity is **viral lineage**: MARV (multiple variants — e.g., Musoke, Popp, Angola, Ozolin) vs. RAVV. The **Angola variant** was associated with the exceptionally high CFR (~90%) in 2004–05. These are properly encoded as infectious-agent subtypes (NCBITaxon-bound), not host alleles.

**Epigenetics / chromosomal abnormalities:** Not applicable (viral disease).

---

## 5. Environmental Information

- **Infectious agent:** MARV/RAVV (Filoviridae). Primary classification axis for this entry.
- **Reservoir/vector ecology:** *Rousettus aegyptiacus* (Egyptian rousette fruit bat) is the maintenance host; seasonal pulses of viral shedding in juvenile bats correlate with human spillover risk (Amman et al., 2012, *PLoS Pathogens*, PMID:23055920 — verify). Primates (including humans) are incidental dead-end–to–amplifying hosts.
- **Environmental exposure:** cave/mine microenvironments with high bat density; handling bushmeat; nosocomial environments lacking IPC.
- **Lifestyle/occupational:** mining, caving/tourism, hunting, healthcare, funerary practices.
- No chemical/toxicant or pollution etiology. ECTO/ENVO terms could capture "exposure to bat-inhabited cave environment" if a `environmental:` node is desired, but ECTO coverage should be searched before binding (per dismech-terms discipline; do not fabricate an ECTO CURIE).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating infection → death)

1. **Mucosal/percutaneous exposure to MARV** (bat-contaminated environment or infected human fluids) **leads to** viral deposition at the portal of entry.
2. **GP-mediated attachment** to dendritic cells, monocytes, and macrophages (via DC-SIGN/TIM-1/Axl), followed by endosomal uptake, cathepsin cleavage of GP, and **NPC1-dependent fusion**, **results in** productive infection of these first-responder myeloid cells (the primary targets). *(Well demonstrated in vitro and NHP models.)*
3. Infected macrophages/DCs **release large amounts of proinflammatory mediators** (TNF-α, IL-1β, IL-6, IL-8, IFN response chemokines, nitric oxide, reactive oxygen species) — a **dysregulated "cytokine storm."**
4. In parallel, viral **VP35 and VP40 antagonize type I interferon** (VP35 blocks RIG-I/IRF3 signaling; VP40 impairs Jak/STAT), **leading to** failure of early antiviral control and **unchecked systemic viral replication** with spread to liver, spleen, lymphoid tissue, adrenal glands, and endothelium. *(Demonstrated.)*
5. High cytokine levels and direct infection of **dendritic cells impair their maturation/antigen presentation**, **leading to** defective adaptive immune priming.
6. **Massive "bystander" apoptosis of lymphocytes** (which are *not* themselves productively infected) **results in** profound lymphopenia and immune collapse, **leading to** inability to clear virus. *(Demonstrated; mechanism of bystander death — Fas/TNF, mediator-driven — partly inferred.)*
7. Infection and cytokine action on **vascular endothelium**, together with viral GP effects, **lead to** endothelial activation and increased vascular permeability → **plasma leak, hypovolemia, hypotension.**
8. Infected macrophages express **tissue factor**, and endothelial injury plus consumption of clotting factors **lead to disseminated intravascular coagulation (DIC)** → simultaneous thrombosis and **hemorrhage**, compounded by thrombocytopenia. *(Tissue-factor mechanism shown in filovirus NHP models.)*
9. **Direct hepatocellular infection and necrosis** (steatosis, councilman-like bodies) **result in** coagulation-factor deficiency and rising transaminases, **worsening** the coagulopathy.
10. **Adrenal cortical infection/necrosis** impairs catecholamine/steroid responses, **contributing to** refractory hypotension.
11. The convergence of **plasma leak + DIC + hepatic/adrenal failure + fluid/electrolyte loss from GI disease** **leads to** distributive/hypovolemic shock and **multi-organ failure**, the usual proximate cause of death (often day 8–9).

**Branch:** In survivors, timely **adaptive immunity (early, robust IgG and T-cell response)** and lower peak viremia **lead to** viral clearance and recovery; delayed/absent antibody response tracks with fatal outcome. (Reviews: Feldmann & Geisbert 2011, PMID:21084112; Mehedi et al. on filovirus biology; Messaoudi et al., *Nat Rev Microbiol* 2015 on filovirus pathogenesis, PMID:25822829 — verify.)

### Category checklist mapped to GO/CL/UBERON

- **Molecular pathways:** type I interferon antagonism (GO:0032480 negative regulation of type I interferon production — verify); RIG-I signaling suppression; coagulation cascade activation (GO:0007596 blood coagulation); inflammatory cytokine signaling (GO:0006954 inflammatory response).
- **Cellular processes:** apoptosis of lymphocytes (GO:0006915 apoptotic process / GO:0097194 execution phase of apoptosis); macrophage/DC activation (GO:0042116 macrophage activation); viral entry (GO:0046718 viral entry into host cell); viral budding (GO:0046755).
- **Protein dysfunction (viral effectors):** VP35 dsRNA sequestration; VP40 matrix/budding; GP receptor binding (UniProt entries for MARV GP, VP35, VP40, L).
- **Immune involvement:** innate immune evasion + maladaptive hyperinflammation + adaptive immune suppression.
- **Tissue-damage mechanisms:** direct cytopathic infection (hepatocytes, endothelium), immune-mediated injury, ischemia from DIC, oxidative/nitrosative stress.
- **Cell types (CL):** macrophage **CL:0000235**; monocyte **CL:0000576**; dendritic cell **CL:0000451**; hepatocyte **CL:0000182**; endothelial cell **CL:0000115**; T lymphocyte **CL:0000084** (bystander apoptosis).
- **Anatomic/cellular compartments:** endosome/lysosome (NPC1; GO:0005764 lysosome; GO:0005768 endosome), plasma membrane (budding).

---

## 7. Anatomical Structures Affected

- **Primary organs:** **liver** (UBERON:0002107) — hepatocellular necrosis/steatosis; **spleen** (UBERON:0002106) and **lymphoid tissue** (UBERON:0000479) — lymphoid depletion; **vascular endothelium** (UBERON:0001986 endothelium / UBERON:0000115 lung? — use vasculature UBERON:0002049) — systemic leak.
- **Secondary involvement:** **kidney** (UBERON:0002113) — AKI; **adrenal gland** (UBERON:0002369) — cortical necrosis; **gastrointestinal tract** (UBERON:0001555) — fluid loss, bleeding; **pancreas** (UBERON:0001264); **central nervous system / brain** (UBERON:0000955) — encephalopathy; **testis/gonads** (UBERON:0000473) — viral persistence (immune-privileged sites, relevant to late relapse/sexual transmission by analogy to Ebola; data for Marburg more limited).
- **Body systems:** hematologic/coagulation, hepatobiliary, cardiovascular, renal, GI, CNS, immune, endocrine.
- **Tissue/cell level:** mononuclear phagocytes, hepatocytes, endothelial cells, lymphocytes (see §6).
- **Subcellular:** endosome–lysosome (entry), plasma membrane (budding), cytoplasmic inclusion bodies (viral replication factories; GO:0039712 — verify).
- **Lateralization:** Not applicable (systemic).

---

## 8. Temporal Development

- **Incubation:** 2–21 days (commonly 5–10). (WHO.)
- **Onset:** acute/abrupt.
- **Course/stages:** generalization (d1–4) → early organ phase with hemorrhage and neurologic signs (d5–13) → convalescence *or* terminal multi-organ failure/shock. Fatal outcomes typically **day 8–9** after onset.
- **Progression rate:** rapid.
- **Duration:** self-limited in survivors (acute), followed by a **prolonged convalescence** (weeks–months) with asthenia, and documented **sequelae and viral persistence** in immune-privileged sites.
- **Critical intervention window:** early aggressive supportive care (fluids/electrolytes) during the first days markedly affects survival; late presentation with hemorrhage/shock carries high mortality.

---

## 9. Inheritance and Population (Epidemiology)

**Inheritance:** Not applicable (infectious). Transmission is zoonotic (bat→human) then human-to-human; no vertical Mendelian inheritance.

**Epidemiology.** Sporadic outbreaks, predominantly sub-Saharan Africa. Notable events:
- **1967** Germany/Yugoslavia (index; 31 cases, 7 deaths) — imported monkeys.
- **1975** South Africa/Zimbabwe traveler cluster.
- **1980, 1987** Kenya (sporadic, incl. RAVV).
- **1998–2000** DRC (Durba/Watsa, mining; ~154 cases, ~83% CFR).
- **2004–2005** **Angola (Uíge)** — largest historical outbreak: ~252 cases, 227 deaths (**~90% CFR**) (Towner et al., 2006, *J Virol*, PMID:16731931 — verify).
- **2007, 2008, 2012, 2014, 2017** Uganda (several; miners, cave tourism; RAVV and MARV).
- **2008** imported cases to Netherlands and USA (cave tourists, Uganda).
- **2022** Ghana (first; 3 cases).
- **2023** **Equatorial Guinea** and **Tanzania** (first outbreaks in each).
- **2024** **Rwanda** (notably high healthcare-worker involvement).
- **2025** **Tanzania** (further outbreak).

(Outbreak list per WHO Disease Outbreak News; exact case/death counts should be cited to the specific WHO report or primary paper.)

- **Prevalence/incidence:** no endemic steady-state prevalence; disease is outbreak-driven; cumulative recorded cases across history are in the low thousands.
- **CFR:** ~24–90% depending on outbreak, variant, and care; WHO cites an average around 50%.
- **Geographic distribution:** reservoir range of *R. aegyptiacus* across sub-Saharan Africa (and parts of N. Africa/Middle East); human outbreaks concentrated in East/Central Africa, with imported cases possible anywhere.
- **Sex/age:** no intrinsic sex predisposition; apparent skews reflect occupational exposure.

---

## 10. Diagnostics

**Biosafety:** Live-virus work requires **BSL-4**; clinical specimens handled with strict precautions.

- **Molecular:** **RT-PCR / real-time RT-PCR** for MARV RNA — primary acute diagnostic (highest sensitivity in early viremia). Metagenomic/NGS used for novel-variant identification.
- **Antigen detection:** antigen-capture **ELISA**.
- **Serology:** **IgM** (early) and **IgG** (later/convalescent) ELISA; seroconversion supports diagnosis/recovery.
- **Virus isolation:** cell culture (Vero E6), electron microscopy showing filamentous virions — reference/confirmatory, BSL-4.
- **Immunohistochemistry:** on post-mortem tissue (skin, liver) — useful where blood sampling is unsafe.
- **Supportive labs:** CBC (thrombocytopenia, lymphopenia→neutrophilia), LFTs (AST≫ALT), coagulation (prolonged PT/PTT, high D-dimer, low fibrinogen), renal panel, electrolytes.
- **Clinical criteria:** case definitions are **epidemiologic + clinical + laboratory** (WHO/CDC VHF case definitions); no DSM/scoring system. 
- **Differential diagnosis:** Ebola virus disease (requires lab differentiation), Lassa fever, Crimean-Congo HF, Rift Valley fever, **severe falciparum malaria** (critical early mimic — always test), typhoid, leptospirosis, rickettsioses, meningococcemia, severe bacterial sepsis, dengue, yellow fever, acute viral hepatitis.
- **Genetic/omics diagnostics:** host genetic testing not relevant; viral genomic sequencing is used for outbreak tracing.
- **Screening:** no population screening; **contact tracing with 21-day symptom/temperature monitoring** is the operational "screening" tool in outbreaks.

NCIT/LOINC: RT-PCR for Marburg (LOINC codes exist for filovirus RNA — must be looked up, not typed); NCIT procedure terms for serologic testing / molecular diagnostic assay as applicable.

---

## 11. Outcome / Prognosis

- **Mortality:** CFR ~24–90% (variant- and care-dependent); Angola variant historically highest.
- **Prognostic factors (poorer):** high peak viremia / high viral load; marked transaminase and creatinine elevation; pronounced hemorrhage and DIC; neurologic involvement; shock; delayed or absent antibody response; late presentation and limited supportive care. (Early robust IgG response and lower viremia favor survival.)
- **Proximate cause of death:** multi-organ failure with hypovolemic/distributive shock, often with DIC-related hemorrhage.
- **Survivor sequelae / convalescence:** prolonged asthenia, myalgia, arthralgia; reported **uveitis/ocular inflammation, hepatitis, orchitis, myelitis, psychosis, and recurrent/prolonged symptoms**; **viral persistence** in immune-privileged sites (eye, testis, CNS) is described for filoviruses and raises concern for late relapse and possible sexual transmission (better characterized for Ebola; Marburg data more limited — flag as knowledge gap).
- **QoL tools:** no MVD-specific instrument; generic (EQ-5D/SF-36) would apply to survivor studies, which are sparse.

---

## 12. Treatment

**No specific antiviral or monoclonal antibody is approved for MVD.** Management is primarily supportive, with investigational specific therapeutics.

- **Supportive care (mainstay, outcome-determining):** aggressive IV fluid and electrolyte repletion; correction of hypovolemia/shock; management of coagulopathy (platelets, FFP as indicated); renal replacement if AKI; oxygenation/ventilatory support; empiric treatment of co-infections (e.g., malaria, bacterial sepsis); symptom control (antipyretics, antiemetics, analgesia). NCIT: supportive care **NCIT:C15747**; fluid/electrolyte therapy; pharmacotherapy **NCIT:C15986**.
- **Investigational specific therapeutics:**
  - **Remdesivir (GS-5734)** and **galidesivir (BCX4430)** — nucleoside analog antivirals with activity against filoviruses in NHP models (Warren et al. on BCX4430, *Nature* 2014, PMID:24284631 — verify).
  - **Monoclonal antibodies** targeting MARV GP (e.g., MR191 and related; Mire/Geisbert NHP protection studies — PMIDs to verify).
  - **Favipiravir** — broad RNA-virus activity, evaluated for filoviruses (evidence weaker/mixed).
  - NCIT therapeutic modality terms: antiviral pharmacotherapy; monoclonal antibody **NCIT:C20401** (as `therapeutic_agent` on a pharmacotherapy action).
- **Pharmacogenomics:** not applicable.
- **Experimental/clinical trials:** platform/outbreak trials (e.g., WHO-coordinated), and vaccine efficacy work; NCT identifiers must be fetched from ClinicalTrials.gov before citing.
- **Adverse events / response rates:** no established efficacy benchmarks for MVD specifically; data extrapolated from Ebola and NHP studies.

---

## 13. Prevention

- **Primary prevention:**
  - **Vaccines (investigational, none licensed for MVD):** recombinant **VSV-based (VSVΔG-MARV-GP)**, **chimpanzee adenovirus (ChAd3-MARV)**, DNA, and MVA-based candidates; several advanced to Phase 1/2, with accelerated evaluation during the 2023–2025 outbreaks (WHO/CEPI-supported). Cite specific trials by NCT after verification.
  - **Exposure avoidance:** no unprotected entry into bat-inhabited mines/caves; avoid bushmeat/sick-or-dead primates; bat-population and mine-access controls.
- **Secondary prevention / outbreak control:** rapid case identification and isolation; **contact tracing with 21-day monitoring**; strict **IPC** in healthcare settings (PPE, patient isolation); **safe and dignified burials**; laboratory biosafety.
- **Tertiary prevention:** early supportive care to prevent progression to shock/organ failure; management of survivor sequelae and persistence (ophthalmologic follow-up; counseling on possible persistence).
- **Public health:** surveillance, community engagement/health education, cross-border coordination, ring/targeted vaccination strategies if a vaccine becomes deployable.
- **Prophylaxis:** post-exposure monoclonal antibody or antiviral prophylaxis is investigational only.

NCIT: vaccination **NCIT:C15346**; genetic counseling not applicable.

---

## 14. Other Species / Natural Disease

- **Reservoir host:** **Egyptian rousette fruit bat, *Rousettus aegyptiacus*** (NCBITaxon:9407) — persistently infected, generally without overt disease; experimental infection studied (Amman, Schuh et al.).
- **Nonhuman primates:** African green monkeys (*Chlorocebus aethiops*, legacy *Cercopithecus aethiops*) — the 1967 index amplifying host; **rhesus** (*Macaca mulatta*, NCBITaxon:9544) and **cynomolgus macaques** (*Macaca fascicularis*, NCBITaxon:9541) develop lethal, human-like disease and are the key challenge models.
- **Zoonotic potential:** high; spillover from bats drives all human outbreaks.
- **Natural disease in companion animals/wildlife:** not a recognized veterinary clinical disease outside primates; pigs and other species have been probed experimentally for filoviruses but Marburg is not a notable domestic-animal pathogen. OMIA has no Mendelian analog (not applicable).
- **Comparative/evolutionary:** mechanisms (NPC1 entry, IFN antagonism) are conserved across filoviruses; cross-species susceptibility tracks NPC1 orthologs.

---

## 15. Model Organisms

- **Nonhuman primate (gold standard):** cynomolgus and rhesus macaques recapitulate the full human syndrome — fever, viremia, coagulopathy/DIC, hepatic injury, hemorrhage, lethality — and are the pivotal models for therapeutics/vaccines (Geisbert, Hensley, Mire laboratories). **Strength:** high fidelity. **Limitation:** cost, BSL-4, ethical/throughput constraints; uniformly lethal challenge may not mirror the survivable spectrum of human disease.
- **Rodent models:** wild-type mice/guinea pigs resist unadapted MARV; **mouse- and guinea-pig–adapted MARV** strains, and **immunodeficient (e.g., IFN-receptor knockout, STAT1-KO) and humanized mice** support lethal infection for screening. **Limitation:** adaptation changes virulence determinants; immunodeficient models lack intact immune pathogenesis — partial fidelity.
- **In vitro:** Vero E6 and human macrophage/DC/hepatocyte/endothelial cultures for entry, replication, and innate-immune-antagonism studies; NPC1-knockout cell lines demonstrate entry dependence.
- **Reservoir model:** experimentally infected *R. aegyptiacus* colonies for transmission/ecology.
- **Resources:** BEI Resources / reference labs (CDC, USAMRIID, PHAC, Bernhard Nocht Institute); model data via PubMed (MGI/ZFIN not applicable to a viral pathogen).

Model-link fidelity for a dismech entry: NHP challenge = **RECAPITULATES** (HIGH fidelity) for the systemic hemorrhagic syndrome; adapted-rodent/immunodeficient = **PARTIALLY_RECAPITULATES** (MODERATE/LOW; note species-adaptation and immune-deficiency divergences).

---

## Key ontology-term summary (leads — verify every CURIE before binding)

- **Agent (NCBITaxon):** Orthomarburgvirus marburgense / Marburg marburgvirus (verify current taxid); reservoir *Rousettus aegyptiacus* NCBITaxon:9407; NHP models NCBITaxon:9544, 9541.
- **Cell types (CL):** CL:0000235 macrophage; CL:0000576 monocyte; CL:0000451 dendritic cell; CL:0000182 hepatocyte; CL:0000115 endothelial cell; CL:0000084 T cell.
- **Anatomy (UBERON):** UBERON:0002107 liver; UBERON:0002106 spleen; UBERON:0002113 kidney; UBERON:0002369 adrenal gland; UBERON:0002049 vasculature; UBERON:0000955 brain.
- **Processes (GO):** GO:0006954 inflammatory response; GO:0006915 apoptotic process; GO:0046718 viral entry into host cell; GO:0007596 blood coagulation; type I IFN negative regulation (verify exact GO id).
- **Phenotypes (HP):** HP:0001945 Fever; HP:0002014 Diarrhea; HP:0002013 Vomiting; HP:0001873 Thrombocytopenia; HP:0002910 Elevated hepatic transaminase; HP:0001888 Lymphopenia; HP:0000421 Epistaxis; HP:0002615 Hypotension (verify); HP:0002315 Headache; HP:0003326 Myalgia.
- **Treatments (NCIT):** NCIT:C15747 Supportive Care; NCIT:C15986 Pharmacotherapy; NCIT:C20401 Monoclonal Antibody; NCIT:C15346 Vaccination.

---

## Priority citations to fetch and verify (leads, not yet validated)

- WHO Marburg virus disease fact sheet and Disease Outbreak News (authoritative for CFR, outbreaks, transmission) — not a PMID; cite as WHO with retrieval date.
- Towner JS et al., *PLoS Pathog* 2009 — *R. aegyptiacus* reservoir (candidate **PMID:19649327**).
- Carette JE et al., *Nature* 2011 — NPC1 as filovirus entry receptor (candidate **PMID:21866103**); Côté M et al., *Nature* 2011 (candidate **PMID:21866101**).
- Towner JS et al., *J Virol* 2006 — Angola variant/outbreak (candidate **PMID:16731931**).
- Amman BR et al., *PLoS Pathog* 2012 — seasonal bat shedding and spillover (candidate **PMID:23055920**).
- Feldmann H, Geisbert TW, *Lancet* 2011 — filoviral hemorrhagic fever pathogenesis review (candidate **PMID:21084112**).
- Messaoudi I et al., *Nat Rev Microbiol* 2015 — filovirus pathogenesis (candidate **PMID:25822829**).
- Warren TK et al., *Nature* 2014 — BCX4430/galidesivir NHP protection (candidate **PMID:24284631**).

**Not-available / knowledge-gap flags for curation:**
- No human host causal or protective gene established (NPC1 resistance is model/cell-based only).
- Human-specific data on Marburg viral persistence in immune-privileged sites and late relapse are limited (largely extrapolated from Ebola).
- Prognostic biomarker thresholds are not standardized for MVD specifically.
- No licensed vaccine or specific therapeutic as of the knowledge cutoff; trial NCT identifiers must be pulled live from ClinicalTrials.gov.

---

If you want, I can now (a) run `just fetch-reference` on the candidate PMIDs above to confirm which resolve correctly and capture exact abstract snippets, or (b) scaffold this into a `kb/disorders/Marburg_Virus_Disease.yaml` draft (as an infectious-disease entry with `infectious_agent`, `transmission`, and `agent_life_cycle` per the infectious-disease granularity ladder) with only verified evidence attached. Tell me which, and I'll proceed with tool-backed verification before anything lands in the KB.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:25822829` (2 mentions) - Associations between DSM-5 section III personality traits and the Minnesota Multiphasic Personality Inventory 2-Restructured Form (MMPI-2-RF) scales in a psychiatric patient sample.
  - shared terms: human

Weighed against this report's own most characteristic terms: `disease`, `viral`, `verify`, `marburg`, `outbreak`, `cell`, `marv`, `host`, `human`, `fever`, `virus`, `model`, `exposure`, `shock`, `reservoir`, `aegyptiacus`, `infection`, `filovirus`, `response`, `fluid`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 73 |
| Resolved | 66 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 37 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 13 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCBITaxon:9407` (3 mentions) - the report calls it "Reservoir host:** **Egyptian rousette fruit bat, *Rousettus aegyptiacus"; NCBITaxon calls it **Rousettus aegyptiacus**
- `HP:0025145` (1 mention) - the report calls it "Chills — verify"; HP calls it **Rigors**
- `HP:0100737` (1 mention) - the report calls it "Pharyngitis — verify"; HP calls it **Abnormal hard palate morphology**
- `HP:0000525` (1 mention) - the report calls it "Conjunctivitis/injection — verify"; HP calls it **Abnormality iris morphology**
- `HP:0011877` (1 mention) - the report calls it "Gastrointestinal hemorrhage — verify"; HP calls it **Increased mean platelet volume**
- `UBERON:0002107` (2 mentions) - the report calls it "liver", "Primary organs:** **liver"; UBERON calls it **liver**
- `UBERON:0002113` (2 mentions) - the report calls it "kidney", "Secondary involvement:** **kidney"; UBERON calls it **kidney**
- `GO:0039712` (1 mention) - the report calls it "verify"; GO calls it **obsolete induction by virus of host catalytic activity**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003681` (1 mention) - HP does not contain this term
- `HP:0007498` (1 mention), reported as "Maculopapular exanthema — verify" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0039712` (obsolete induction by virus of host catalytic activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0020500` (2 mentions) - the report calls it "Marburg hemorrhagic fever / Marburg virus disease"; MONDO calls it **Marburg hemorrhagic fever**
- `HP:0000978` (1 mention) - the report calls it "Bruising susceptibility/ecchymoses"; HP calls it **Bruising susceptibility**
- `HP:0001882` (1 mention) - the report calls it "Leukopenia"; HP calls it **Decreased total leukocyte count**, and lists "Leukopenia" among its other names
- `HP:0001888` (2 mentions) - the report calls it "Lymphopenia"; HP calls it **Decreased total lymphocyte count**, and lists "Lymphopenia" among its other names
- `HP:0002910` (2 mentions) - the report calls it "Elevated hepatic transaminase"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated transaminases" among its other names
- `HP:0012100` (1 mention) - the report calls it "Abnormal circulating creatinine"; HP calls it **Abnormal circulating creatinine concentration**, and lists "Abnormal circulating creatinine level" among its other names
- `HP:0001289` (1 mention) - the report calls it "Confusion — verify"; HP calls it **Confusion**
- `HP:0002353` (1 mention) - the report calls it "EEG abnormality if documented"; HP calls it **EEG abnormality**, and lists "EEG abnormalities" among its other names
- `HP:0002615` (2 mentions) - the report calls it "Hypotension — verify"; HP calls it **Hypotension**
- `UBERON:0000479` (1 mention) - the report calls it "lymphoid tissue"; UBERON calls it **tissue**, and lists "simple tissue" among its other names
- `UBERON:0001555` (1 mention) - the report calls it "gastrointestinal tract"; UBERON calls it **digestive tract**
- `UBERON:0000955` (2 mentions) - the report calls it "central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names
- `UBERON:0000473` (1 mention) - the report calls it "testis/gonads"; UBERON calls it **testis**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002107` - called "liver", "Primary organs:** **liver"
- `UBERON:0002113` - called "kidney", "Secondary involvement:** **kidney"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `LOINC`.