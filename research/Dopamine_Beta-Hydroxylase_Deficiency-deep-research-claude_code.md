---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-23T21:10:07.495003'
end_time: '2026-10-23T21:18:57.511714'
duration_seconds: 530.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Dopamine Beta-Hydroxylase Deficiency
  mondo_id: MONDO:0009123
  category: Mendelian
  causal_genes: DBH
  omim_id: OMIM:223360
  synonyms: noradrenaline deficiency; norepinephrine deficiency; orthostatic hypotension
    1, due to DBH deficiency
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
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 37
  total_cost_usd: 3.348947899999999
  session_id: 170116fc-6aec-4dea-b99d-afeacc981b5c
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 3
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 7
reference_validation:
  total_references: 57
  verified: 57
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 36
  quotes_valid: 33
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:33034372
  - PMID:7715704
  - PMID:10051631
  relevance_assessed: 57
  on_topic: 42
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 82
  verified: 79
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: UBERON:0004237
    reported_labels:
    - arterial/arteriolar smooth muscle (arteriolar smooth-muscle hypertrophy at autopsy)
    ontology_label: blood vessel smooth muscle
  - term_id: UBERON:0001826
    reported_labels:
    - "nasal mucosa (stuffiness \u2014 loss of vasoconstrictor tone)"
    ontology_label: nasal cavity mucosa
  - term_id: UBERON:0002371
    reported_labels:
    - bone marrow (sympathetic innervation; anemia hypothesis)
    ontology_label: bone marrow
  labels_variant: 4
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dopamine Beta-Hydroxylase Deficiency
- **MONDO ID:** MONDO:0009123 (if available)
- **Causal gene(s):** DBH
- **OMIM:** OMIM:223360
- **Synonyms:** noradrenaline deficiency; norepinephrine deficiency; orthostatic hypotension 1, due to DBH deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Dopamine Beta-Hydroxylase Deficiency** covering all of the
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

I'm collecting primary-literature PMIDs for DBH deficiency from PubMed. The report comes after that.

The local reference cache already holds many DBH-deficiency abstracts, so I'm reading them for exact quotes.

I'll continue with the research report now, writing up what I've gathered from the local reference cache and PubMed.

# Dopamine Beta-Hydroxylase Deficiency — Comprehensive Research Report

**Target:** Dopamine beta-hydroxylase (DBH) deficiency · **MONDO:0009123** (orthostatic hypotension 1) · **OMIM:223360** · **Causal gene: DBH** (dopamine beta-hydroxylase, EC 1.14.17.1, chromosome 9q34, `hgnc:2689`)

This report concerns the **DBH**-caused disorder, not the phenotypically similar `CYB561`-caused orthostatic hypotension 2 (OMIM 618182), which must be excluded in differential diagnosis (see §10). All identifiers and gene attributions below follow the identifiers given in the brief.

---

## 1. Disease Information

DBH deficiency is an extremely rare autosomal recessive neurometabolic disorder of catecholamine biosynthesis in which the enzyme converting dopamine to norepinephrine is absent or non-functional. The result is a **selective, isolated sympathetic noradrenergic failure in a structurally normal sympathetic nervous system**, with intact parasympathetic and sympathetic cholinergic function (hence normal sweating).

> "DBH‐deficiency leads to a selective and functional noradrenergic failure of a structurally normal sympathetic nervous system." (PMID:33034372)

> "Dopamine beta-hydroxylase (DBH) deficiency is characterized by lack of sympathetic noradrenergic function resulting in profound deficits in autonomic regulation of cardiovascular function (orthostatic hypotension) and other autonomic dysfunction (ptosis, nasal stuffiness, sleep difficulties, and impaired ejaculation in males)." (GeneReviews, PMID:20301647)

**Identifiers**
| Resource | Value |
|---|---|
| MONDO | MONDO:0009123 (label: *orthostatic hypotension 1*) |
| OMIM | 223360 (ORTHOSTATIC HYPOTENSION 1; ORTHYP1); gene OMIM 609312 |
| Orphanet | ORPHA:230 (a dedicated Orphanet review exists: PMID:16722595, *Orphanet J Rare Dis* 2006) |
| HGNC | `hgnc:2689` (DBH) |
| EC | 1.14.17.1 |
| MedGen | C4746777 |
| Enzyme/analyte CHEBI | dopamine CHEBI:18243; (R)-noradrenaline CHEBI:72587 / noradrenaline CHEBI:33569; adrenaline CHEBI:28918; droxidopa CHEBI:135309; L-ascorbate CHEBI:38290; copper(2+) CHEBI:29036 |

**Synonyms:** DBH deficiency; DβH deficiency; norepinephrine deficiency; noradrenaline deficiency; congenital dopamine-beta-hydroxylase deficiency; orthostatic hypotension 1.

**Evidence provenance:** disease-level aggregated resources (OMIM, Orphanet, GeneReviews) plus a **pooled individual-patient literature review with a 10-patient chart-reviewed cohort** — Wassenberg et al. 2021 (PMID:33034372) is the single most authoritative individual-patient source and the backbone of this report. No EHR-scale or registry data exist.

---

## 2. Etiology

**Causal factor:** biallelic (homozygous or compound heterozygous) pathogenic variants in *DBH*, abolishing DBH enzymatic activity. DBH is a copper- and ascorbate-dependent monooxygenase localized in the lumen of (nor)adrenergic neurosecretory vesicles; it is expressed in central and peripheral noradrenergic neurons, the retina, and adrenal chromaffin cells (PMID:33034372).

**Genetic risk:** entirely monogenic/Mendelian; no susceptibility loci or established modifier genes. No genotype–phenotype correlation could be established:

> "Due to small sample size and relatively large number of variants, no phenotype/genotype correlations can be made." (PMID:33034372)

**Important non-causal confounder:** the regulatory variant **−1021C>T** causes *plasma DBH pseudodeficiency* in ~4% of healthy people, with normal norepinephrine. This is a diagnostic trap, not a disease allele:

> "plasma DBH enzyme activity is absent in 4 % of the healthy population due to a specific variant (−1021C>T) of the DBH gene, leading to pseudodeficiency with normal levels of plasma norepinephrine." (PMID:33034372)

**Environmental risk factors:** none cause the disease. Environmental factors act as **symptom triggers/exacerbators**, which is how they should be modelled (see §5): heat, upright posture, strenuous exercise, dehydration, large meals, alcohol, and intercurrent infection. GeneReviews explicitly lists these as circumstances to avoid (PMID:20301647).

**Protective factors:** none genetic. The only modifiable protective exposures are avoidance behaviours (supine/seated posture, hydration, heat avoidance) and, in the murine system, maternal catecholamine supply across the placenta (see §15).

**Gene–environment interaction:** the defining interaction is **genotype × orthostatic/thermal/metabolic stress**. Patients are near-normotensive supine (mean 109/68 mmHg) and profoundly hypotensive upright — the lesion is only expressed when the sympathetic noradrenergic reflex is demanded. Similarly, hypoglycaemia is unmasked by fasting/illness because the counter-regulatory adrenomedullary epinephrine response is absent.

---

## 3. Phenotypes

Two frequency sources exist. Wassenberg 2021 (n=25, PMID:33034372) is the better-powered individual-patient series; Robertson 1991 as tabulated by Orphanet (PMID:16722595, Table 2) gives an older n≈6 frequency table. Both are given — **do not merge them into one percentage.**

### Cardinal features

| Phenotype | HPO suggestion | Frequency | Source |
|---|---|---|---|
| Severe (neurogenic) orthostatic hypotension | HP:0001278 Orthostatic hypotension | **25/25 (100%)** | PMID:33034372 |
| Eyelid ptosis (may be unilateral/asymmetric) | HP:0000508 Ptosis | **18/20 described (90%)**; 67% in older table | PMID:33034372; PMID:16722595 |
| Exercise intolerance | HP:0003546 Exercise intolerance | majority (reduced standing time/exercise capacity) | PMID:33034372, PMID:16722595 |
| Syncope / presyncope | HP:0001279 Syncope | majority | PMID:33034372 |
| Nasal stuffiness / chronic nasal congestion | HP:0001742 Nasal congestion | ~50% | PMID:16722595 |
| Nocturia | HP:0000017 Nocturia | 3 patients reported; 67% in older table | PMID:33034372; PMID:16722595 |
| Miosis (small, light/accommodation-reactive pupils) | HP:0000616 Miosis | present incl. 2 patients without ptosis | PMID:33034372; PMID:16722595 |
| Impaired ejaculation / retrograde ejaculation, erectile dysfunction | HP:0012875 Abnormal ejaculation; HP:0000822-adjacent | 3/5 males described; 100% in older table | PMID:33034372; PMID:16722595 |
| Intermittent diarrhea | HP:0002254-adjacent / HP:0002028 Chronic diarrhea | reported, unsystematic | PMID:33034372 |

**Blood-pressure quantification (untreated, within 3 min of standing):** standing mean **72/49 mmHg** (systolic range 44–115); mean orthostatic fall **58 mmHg systolic / 38 mmHg diastolic**; supine <135/90 mmHg in all (mean 109/68). (PMID:33034372) This is the key severity statistic for the entry.

### Neonatal / perinatal
> "First symptoms often start during a complicated perinatal period with hypotension, muscle hypotonia, hypothermia and hypoglycemia." (PMID:16722595)

HPO: HP:0002017-adjacent vomiting (HP:0002013), HP:0001944 Dehydration, HP:0002045 Hypothermia, HP:0001943 Hypoglycemia, HP:0001252 Hypotonia. Prematurity and low birth weight in 5/14 with neonatal data; childhood hypoglycaemia in 4 (PMID:33034372). GeneReviews notes the diagnosis is sometimes made fortuitously during a neonatal hypoglycaemia work-up.

### Newly characterized systemic triad (the 2021 contribution)
> "Impaired kidney function and anemia were present in all Dutch patients, hypomagnesaemia in 5 out of 10." (PMID:33034372)

- **Decreased eGFR** — HP:0012213 Reduced glomerular filtration rate; all Dutch patients (7 mildly, 4 moderately, 1 moderately–severely decreased).
- **Anemia**, usually mild, normocytic (MCV normal in 10/10) — HP:0001903 Anemia; mean Hb below reference in 12/14.
- **Hypomagnesemia** with increased fractional magnesium excretion (5.0–15.1%; normal 2–4%) — HP:0002917 Hypomagnesemia; renal magnesium wasting HP:0500152-adjacent.
- Mild thrombocytopenia in 4 patients (HP:0001873).

### Misdiagnosis-relevant phenotypes
Three patients were initially diagnosed with and treated for **epilepsy**; seizures occurred only on standing with normal interictal EEG (PMID:33034372). Robertson 1991: "The hypotension may be so severe that clonic seizures supervene." (PMID:1677640) HPO: HP:0001250 Seizure — but note these are hypotension-induced, i.e. a *sequela* of orthostatic hypotension in the pathograph, not an independent CNS phenotype.

### Skeletal/dysmorphic (non-systematically described)
Brachydactyly/short hands or feet (n=7, HP:0001156), high-arched palate (n=6, HP:0000218), joint hyperlaxity (HP:0001382, 50% in the older table), hypotonic skeletal muscles, weak facial musculature, sluggish tendon reflexes (PMID:33034372, PMID:16722595). Coloboma and additional dysmorphism in one patient were attributed to a **concomitant mosaic 11p13 deletion** (PAX6/WT1), not to DBH deficiency (PMID:20186791) — a caution against over-attribution.

### Notably spared
- **Cognition is normal** — IQ mean 106 (range 98–119) on formal testing in 5 patients; normal in 16/18 described (PMID:33034372, PMID:21471955). Jepma 2011 found largely spared neurocognition with a temporal-attention deficit off medication, smaller total brain volume, and absent task-evoked pupil dilation.
- **Sweating is normal** (sympathetic cholinergic) — the clearest demonstration that the failure is noradrenergic-selective (PMID:33034372); the sympathetic skin response is preserved (PMID:9651662).
- **Olfaction is relatively intact** (PMID:21282592).
- Sleep: cyclic REM preserved, increased slow-wave sleep; REM increases on DOPS (PMID:2355243, PMID:1811317) — "a modulatory or permissive role for noradrenaline in REM sleep mechanisms."
- Cerebral MRI structurally normal (PMID:33034372).

### Quality of life
No validated instrument (EQ-5D/SF-36) has been applied. Reported impact is severe and largely reversible on treatment:
> "a great and continuous improvement in overall functioning was reported by all patients, for example, becoming able to work‐full time and to do sports." (PMID:33034372)
Residual fatigue and persistent mild ptosis were reported under treatment. The **Orthostatic Hypotension Questionnaire** is recommended by the authors as the structured outcome measure to adopt.

### Novel/rare presentation
A 2025 case report describes the youngest diagnosis to date: a 26-week premature newborn with recurrent syncope from **high-grade AV block and sinus node dysfunction** (asystole up to 10 s) who received a pacemaker; homozygous c.339+2T>C; after L-DOPS, 0% pacing rate (PMID:40951656). The authors propose a Bezold–Jarisch reflex mechanism and cite *Dbh* knockout conduction-tissue abnormalities. **This is a single case; bradyarrhythmia should not be curated as a general phenotype.**

---

## 4. Genetic/Molecular Information

**Causal gene:** *DBH*, 9q34, 12 exons; reference sequences **NM_000787.4** (DNA) / **NP_000778.3** (protein). GO annotations for the product: `GO:0004500` dopamine beta-monooxygenase activity; `GO:0042421` norepinephrine biosynthetic process; `GO:0030667` secretory granule membrane / `GO:0034774` secretory granule lumen; `GO:0005507` copper ion binding.

**The ten pathogenic variants reported to date** (PMID:33034372, Table 1):

| # | Location | DNA (NM_000787.4) | Protein (NP_000778.3) | First reported |
|---|---|---|---|---|
| 1 | Intron 1 | **c.339+2T>C** (= IVS1+2T>C) | none (splicing) | Kim 2002 (PMID:11857564) |
| 2 | Exon 1 | c.301G>A | p.(Val101Met)* | Kim 2002 |
| 3 | Exon 2 | c.342C>A | p.(Asp114Glu) | Kim 2002 |
| 4 | Exon 3 | c.617del | p.(Glu206Glyfs*82) | Deinum |
| 5 | Exon 4 | c.806G>T | p.(Cys269Phe) | Deinum |
| 6 | Exon 6 | c.1033G>A | p.(Asp345Asn)* | Kim 2002 |
| 7 | Exon 6 | c.1085C>A | p.(Ala362Glu) | Kim 2002 |
| 8 | Intron 8 | c.1374+2_1374+20del | none (splicing) | Deinum |
| 9 | Exon 9 | c.1409_1410delinsTG | p.(Thr470Met) | Bartoletti-Stella (PMID:26410747) |
| 10 | Exon 11 | c.1667A>G | p.(Tyr556Cys) | Deinum |

\* c.301G>A has only been described in cis-adjacent/trans configuration with c.1033G>A, and "one of the two may not be pathogenic" (PMID:33034372) — a VUS caution worth recording.

**Founder/common allele:** c.339+2T>C is the dominant allele —
> "The most frequently reported pathogenic variant (19 patients total, seven homozygous) is the intronic mutation c.339+2T>C (also reported as IVS1+2T>C) leading to aberrant splicing." (PMID:33034372)

Zabetian et al. 2003 (PMID:14598346) published a revised allele-frequency estimate and haplotype analysis of IVS1+2T>C in African- and European-Americans — the appropriate citation for carrier frequency, and the haplotype data bear on a founder effect. **Note the older Orphanet table (PMID:16722595) uses legacy nucleotide numbering** (C-1021T, G259A/V87M, C300A/D100E, G991A/D331N) which maps to the same variants under a different transcript; always curate with the NM_000787.4 coordinates above.

**Functional consequence — loss of function, by two distinct molecular routes.** Kim et al. 2011 (PMID:21209083) is the mechanistic reference:
> "a pharmacological chaperone, glycerol, significantly rescued defective trafficking of mutant DBH proteins"

- **c.339+2T>C** → aberrant mRNA splicing, premature stop codon, **no detectable DBH protein**.
- **Missense alleles** → the protein is made but **retained in the endoplasmic reticulum** (`GO:0005783`), i.e. a trafficking/folding defect rather than a catalytic one. This is the mechanistically interesting split: two different proteostatic lesions converging on absent vesicular enzyme, and it makes DBH deficiency a candidate for pharmacological-chaperone rescue (demonstrated in vitro only).

Consistent with absent rather than catalytically dead enzyme, DBH immunoreactivity is undetectable in plasma and CSF (PMID:8143425): "suggests absent enzyme (rather than a catalytically defective enzyme) as the origin of the disorder". Autopsy in one patient showed absent DBH immunoreactivity in the ventrolateral medulla (PMID:33034372, citing PMID:16830134 — *Dopamine beta-hydroxylase deficiency involves the central autonomic network*).

**Somatic vs germline:** germline. **Chromosomal abnormalities:** not a mechanism; one patient carried an incidental mosaic 11p13 deletion (PMID:20186791). **Epigenetics:** no DNA-methylation or chromatin mechanism reported — record as a knowledge gap, not as absent.

**Allele frequency:** gnomAD should be consulted directly for current c.339+2T>C frequency; the citable published estimate is Zabetian 2003 (PMID:14598346). Do not write a gnomAD number from memory.

---

## 5. Environmental Information

No environmental agent causes DBH deficiency. Environmental factors belong in the entry as `environmental[]` entries with `environmental_effect: EXACERBATES` linked via `influences_mechanisms` to the orthostatic-hypotension node:

- **Heat / hot environments** — ECTO/XCO candidate: exposure to high temperature. GeneReviews: untreated individuals "should avoid hot environments, strenuous exercise, standing motionless, and dehydration" (PMID:20301647).
- **Upright posture / prolonged standing** — the proximate trigger; mechanistically the orthostatic gravitational challenge.
- **Strenuous exercise** — Smith 1995 (PMID:7602525, PMID:7796074): in DBH deficiency "plasma noradrenaline and adrenaline were undetectable, but plasma dopamine was elevated" during supine exercise, with BP falling to a lower level on standing after exercise.
- **Large meals and alcohol** — presyncopal symptoms "may worsen in hot environments or after heavy meals or alcohol ingestion" (PMID:20301647). Note Mathias 1991 (PMID:1940947) found food had *minimal* BP effect in DBH deficiency unlike MSA/PAF — so postprandial worsening is symptom-level, and the two sources should be curated as distinct claims rather than harmonized.
- **Dehydration / volume depletion.**
- **Nephrotoxic drugs** — to be avoided given baseline renal impairment (PMID:20301647).
- **Intercurrent viral infection** — precipitated the syncopal/bradycardic episodes in the newborn case (PMID:40951656).
- **Drugs to note:** ephedrine caused *paradoxical hypotension* (PMID:2795065); clonidine produces a paradoxical pressor response and tyramine no pressor response (PMID:16722595) — these are pharmacological *diagnostic* probes as well as hazards. One patient's symptoms began after starting **olanzapine** (PMID:33034372).

**Infectious agents:** none. (Relevant only in the mouse model, where NE deficiency impairs Th1 immunity to *Listeria monocytogenes* and *Mycobacterium tuberculosis* — PMID:10051631.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic *DBH* variants** (c.339+2T>C splice, or missense) → **absent functional DBH protein in noradrenergic secretory vesicles** — by aberrant splicing with premature stop (no protein) *or* by ER retention of folded-defective protein (PMID:21209083, in vitro). [demonstrated]
2. Absent vesicular dopamine beta-monooxygenase activity (`GO:0004500`) → **block of the dopamine → norepinephrine conversion step** of catecholamine biosynthesis (`GO:0042421`) in sympathetic nerve terminals, central noradrenergic neurons, and adrenal chromaffin cells. [demonstrated]
3. That block **leads to** two simultaneous consequences, and the pathograph branches here:
   - **3a.** **Absent norepinephrine**, and therefore absent epinephrine (PNMT has no substrate) — undetectable in plasma, urine, and CSF (PMID:2880016). [demonstrated]
   - **3b.** **Accumulation of dopamine** proximal to the block — 5–10-fold elevated in plasma per GeneReviews; 7–12× plasma, 4× urine, 20× CSF in the index case (PMID:2880016). Tyrosine hydroxylase appears to be induced, since L-DOPA is also elevated (PMID:3291893). [demonstrated; TH induction inferred]
4. Dopamine is packaged and released from structurally intact noradrenergic terminals, so it **acts as a false neurotransmitter**: > "Dopamine acts as a false neurotransmitter in their noradrenergic neurons." (PMID:1677640) Physiological and pharmacological stimuli of sympathetic release raise plasma **dopamine instead of** norepinephrine (PMID:2880016). Intrasynaptic dopamine concentrations appear to approximate plasma concentrations (PMID:3291893, inferred from dopamine-antagonist pressor response). [demonstrated]
5. **Branch A — cardiovascular (the dominant branch).** Absent norepinephrine at vascular α1-adrenergic receptors, with sympathetic *nerve traffic intact* (microneurography shows abundant, normally reflex-regulated activity — PMID:2295511) → **failure of reflex vasoconstriction and of the cardiac sympathetic response on standing** → **profound neurogenic orthostatic hypotension** (fall 58/38 mmHg) → cerebral hypoperfusion → **presyncope, syncope, exercise intolerance, hypotension-induced clonic seizures**. Dopamine acting at vascular D1 receptors is vasodilatory, so the false transmitter plausibly *worsens* the hypotension rather than merely failing to help. Cerebral autoregulation itself is preserved (PMID:2795065), and residual leg vasoconstriction is not abolished (PMID:21127209) — the deficit is of adrenergic reflex gain, not of vascular capacity. Chronic denervation produces **adrenergic receptor supersensitivity** (PMID:16722595), which is why exogenous precursor works so well. [demonstrated]
6. **Branch B — adrenomedullary/metabolic.** Absent adrenal epinephrine → loss of counter-regulatory glycogenolysis/lipolysis and thermogenesis → **neonatal and childhood hypoglycaemia, hypothermia** (PMID:1677640, PMID:16722595). A separate metabolic finding is **hyperinsulinemia and insulin resistance**, which persisted after droxidopa restored norepinephrine (PMID:27778639) — mechanism unresolved. [demonstrated; mechanism of insulin resistance unresolved]
7. **Branch C — renal (mechanism contested; curate as a hypothesis, not a fact).** All patients have reduced eGFR. The authors explicitly *reject* their own first hypothesis of hypoperfusion, because a kidney biopsy showed only discrete fibrosis and "renal hypoxia would cause clear histological abnormalities"; supine hypertension, the usual culprit in autonomic failure, is absent in DBH deficiency. Their preferred hypothesis is **dopamine autotoxicity in proximal tubular cells**:
   > "A potential damaging factor to the kidneys, which is quite unique to patients with DBH‐deficiency, is the very high level of dopamine intracellularly in the proximal tubular cells. In high concentrations, dopamine and intermediate dopamine metabolites are thought to be autotoxic, possibly because of increased radical oxygen species production." (PMID:33034372)
   This predicts — and explains — only partial renal recovery on treatment, since dopamine stays elevated. [hypothesis; the competing hypoperfusion explanation is argued against on histological grounds]
8. **Branch D — haematopoietic (mechanism unknown).** Mild normocytic anemia in most patients, including those with only mildly reduced eGFR, so erythropoietin deficiency is insufficient. Proposed: loss of **adrenergic sympathetic innervation of bone marrow**, which normally mobilizes haematopoietic stem cells and maintains their marrow–blood trafficking. The paper states plainly: "The precise mechanism of anemia in DBH‐deficiency and why it does not resolve completely with treatment in most patients is unknown." [hypothesis]
9. **Branch E — renal magnesium wasting.** Hypomagnesemia with raised fractional magnesium excretion; distal-tubular magnesium handling implicated. "The precise pathophysiology, clinical significance and optimal treatment strategy of hypomagnesaemia in patients with DBH‐deficiency needs further investigation." [knowledge gap]
10. **Branch F — endocrine/reproductive.** High dopamine **inhibits prolactin secretion** → hypoprolactinemia (PMID:3291893) → **failed lactation** (no successful lactation has been described). Separately, reduced female fertility is hypothesized from oocyte DBH expression — oocyte-derived norepinephrine may regulate follicular development, and high dopamine may raise ROS in follicular cells. [prolactin link demonstrated; fertility mechanism explicitly hypothetical]
11. **Branch G — ocular.** Loss of sympathetic (noradrenergic) innervation of Müller's superior tarsal muscle → **ptosis**; loss of iris dilator tone → **miosis**. This is effectively a bilateral pharmacological Horner's syndrome; two DBH-deficiency patients featured in a bilateral Horner's series (PMID:9886450), and redilatation lag was the sensitive sign. Phillips 2013 (PMID:23622564) found marked orthostatic falls in **intraocular pressure** alongside mean arterial pressure in three children, proposing orthostatic IOP as an early screening tool. [demonstrated]
12. **Branch H — CNS, notable for what does *not* happen.** Despite absent central norepinephrine, cognition, olfaction, and sleep architecture are largely preserved. Jepma 2011's interpretation: > "The largely spared neurocognitive function in DβH-deficient patients suggests that other neuromodulators have taken over" (PMID:21471955). This compensation is the key **HUMAN_MODEL_MISMATCH**-adjacent open question, since *Dbh*−/− mice have pronounced behavioural abnormalities. [demonstrated absence; compensation mechanism inferred]

### Bypass (why treatment works)
Droxidopa (L-threo-3,4-dihydroxyphenylserine) is decarboxylated to norepinephrine by **aromatic L-amino acid decarboxylase (AADC/DDC)**, bypassing the DBH step entirely (PMID:26092297: "converted to norepinephrine by the enzyme aromatic L-amino acid decarboxylase"). This is a pathograph-relevant intervention point at step 3a, not at step 1–2.

### Ontology suggestions for the pathograph
- Processes: `GO:0042421` norepinephrine biosynthetic process; `GO:0042418` epinephrine biosynthetic process; `GO:0042416` dopamine biosynthetic process; `GO:0004500` dopamine beta-monooxygenase activity (molecular function); `GO:0006936`/vasoconstriction `GO:0042310`; `GO:0008217` regulation of systemic arterial blood pressure; `GO:0034103` regulation of tissue remodeling; ROS `GO:0072593`.
- Cell types: `CL:0000540`-adjacent **noradrenergic neuron** (`CL:0011110` noradrenergic neuron where available); sympathetic noradrenergic neuron; **chromaffin cell** `CL:0000166`; **kidney proximal convoluted tubule epithelial cell** `CL:0002306`; locus coeruleus neuron; vascular smooth muscle cell `CL:0000359`; oocyte `CL:0000023`.
- Compartments: `GO:0030667` secretory granule membrane; `GO:0034774` secretory granule lumen; `GO:0005783` endoplasmic reticulum (mutant retention).
- Chemicals: dopamine CHEBI:18243; noradrenaline CHEBI:33569; adrenaline CHEBI:28918; L-DOPA CHEBI:15765; droxidopa CHEBI:135309; magnesium(2+) CHEBI:18420.

**Molecular profiling:** no transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial, or CRISPR-screen dataset specific to human DBH deficiency was identified. The disease's "omics" layer is **targeted catecholamine metabolomics** (plasma/urine/CSF catecholamines and metabolites), which is diagnostic rather than discovery-scale. Record as a genuine gap rather than searching further for a dataset to attach.

---

## 7. Anatomical Structures Affected

**Body systems:** autonomic (sympathetic noradrenergic) nervous system — primary; cardiovascular, renal, endocrine, haematopoietic, ocular/adnexal, reproductive — secondary.

| Level | Structure | UBERON / CL |
|---|---|---|
| System | sympathetic nervous system | UBERON:0013686 / UBERON:0000013-adjacent |
| Organ | adrenal medulla | UBERON:0001235 |
| Organ | kidney (proximal tubule) | UBERON:0002113 / UBERON:0001287 |
| Organ | heart; cardiac conduction system; sinoatrial & AV node | UBERON:0000948; UBERON:0004146; UBERON:0002351 / UBERON:0002494 |
| Organ/region | brain — ventrolateral medulla (absent DBH immunoreactivity at autopsy, PMID:33034372/16830134); locus coeruleus | UBERON:0002028-adjacent; UBERON:0001890 |
| Tissue | arterial/arteriolar smooth muscle (arteriolar smooth-muscle hypertrophy at autopsy) | UBERON:0004237 |
| Tissue | superior tarsal muscle / upper eyelid (ptosis); iris dilator | UBERON:0001711; UBERON:0001769 |
| Tissue | nasal mucosa (stuffiness — loss of vasoconstrictor tone) | UBERON:0001826 |
| Tissue | bone marrow (sympathetic innervation; anemia hypothesis) | UBERON:0002371 |
| Tissue | retina (DBH-expressing) | UBERON:0000966 |
| Cell | noradrenergic neuron; chromaffin cell; proximal tubule epithelial cell | see §6 |
| Subcellular | neurosecretory/secretory granule lumen; ER (mutant retention) | GO:0034774; GO:0005783 |

**Lateralization:** systemic/bilateral, with the notable exception that **ptosis may be unilateral or asymmetric** (PMID:33034372) — worth curating explicitly, since bilateral symmetry would be the naive expectation for a biosynthetic enzymopathy.

**Autopsy findings (one patient, PMID:33034372):** isolated microfoci of cortical gliosis; cardiac arteriolar smooth-muscle hypertrophy; dispersed fibrosis of the cardiac conduction system; sclerotic renal glomeruli. The conduction-system fibrosis is the structural correlate the authors linked to a possible fatal dysrhythmia.

---

## 8. Temporal Development

- **Onset:** the enzyme defect is congenital — "Although DBH deficiency is present from birth, the diagnosis is often not generally recognized until late childhood" (PMID:20301647). Orthostatic complaints began in **early childhood (1–4 y) in 18/25**, at school age (4–12 y) in 4, and in early adulthood in 2 (PMID:33034372). HPO onset: HP:0003623 Neonatal onset / HP:0011463 Childhood onset (the perinatal presentation is HP:0003623).
- **Pattern:** chronic, lifelong, non-remitting at the enzymatic level; symptomatically **episodic/postural** (attacks precipitated by standing, heat, exertion) on a progressive background.
- **Progression:** "Orthostatic symptoms became more severe during adolescence in 11 patients" (PMID:33034372); Orphanet: "Symptoms usually worsen progressively during late adolescence and early adulthood" (PMID:16722595). Robertson: survivors "sometimes cope relatively well until late childhood when overwhelming orthostatic hypotension profoundly limits their activities" (PMID:1677640).
- **Stages, usable as a `progression:` block:** (i) perinatal crisis phase — vomiting, dehydration, hypotension, hypothermia, hypoglycaemia, repeated hospitalization; (ii) childhood — reduced exercise capacity, ptosis, hypoglycaemia, often attributed to something else; (iii) adolescent/young-adult deterioration — profound orthostatic hypotension, syncope, exercise intolerance; (iv) treated steady state — sustained symptomatic benefit with residual orthostatic hypotension and persistent renal/haematological/magnesium abnormalities.
- **Diagnostic delay is a defining temporal feature:** median age at diagnosis **24 years (range 13–73)** (PMID:33034372). Monnens 2022 (PMID:35202494) is devoted to explaining the delay and arguing for earlier treatment.
- **Remission:** none spontaneous. Treatment-induced symptomatic remission is near-immediate and sustained — "L-DOPS leads to an almost immediate and sustained clinical response" (PMID:33034372), with follow-up to 21 years (median 13).
- **Critical period:** the perinatal period (crisis mortality risk, and in mice outright lethality — §15) and, per Monnens, childhood, where early L-DOPS is advocated.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive — HP:0000007. Sib risk 25% affected / 50% carrier / 25% unaffected non-carrier (PMID:20301647, PMID:16722595).
- **Prevalence:** formally unknown. Orphanet 2006: "The prevalence of DbetaH deficiency is unknown" (PMID:16722595). The 2025 case report gives an estimate of **fewer than 1 in 1,000,000** (PMID:40951656) — appropriate for `prevalence_class: BELOW_1_IN_1000000` with `measure_type: POINT_PREVALENCE`, cited to that source and flagged as an estimate.
- **Reported cases (the better figure for this disease):** **25 patients from 20 families worldwide**, 15 female, as of the 2021 review (PMID:33034372) — curate as `measure_type: CASES_IN_LITERATURE`. Ten of the 25 were Dutch. Earlier counts: ~12 (PMID:15240410, 2004), ~15 (c. 2010), ~25 (MedlinePlus, 2021).
- **Sex ratio:** 15 F : 10 M among the 25 (PMID:33034372) — no evidence of true sex bias in a sample this size; do not assert one.
- **Penetrance / expressivity:** biallelic loss appears fully penetrant for orthostatic hypotension (25/25). Expressivity is variable for everything else — and one patient (pt 23) had **normal plasma and urinary epinephrine and normal metanephrine** despite pathogenic variants, absent DBH activity, and a classical phenotype, which the authors leave unexplained. That single discrepant case is the honest caveat against writing "undetectable epinephrine in all patients."
- **Geography / founder effect:** marked ascertainment in the **Netherlands** (10/25) and the USA (first descriptions 1986–87 in both countries). Whether the Dutch concentration reflects a founder allele or expert-centre ascertainment is not settled by the sources; Zabetian 2003 (PMID:14598346) provides the haplotype analysis of IVS1+2T>C in African- and European-Americans needed to address it. Do not assert a Dutch founder effect without that check.
- **Consanguinity:** seven of 19 genotyped patients were homozygous for c.339+2T>C, which is suggestive, but the reviews do not report consanguinity rates — record as unstated.
- **Carrier frequency:** cite Zabetian 2003 / gnomAD; **do not estimate from the 4% plasma-DBH-pseudodeficiency figure**, which is a different variant (−1021C>T) and not a disease allele.
- **An under-ascertainment argument worth recording:** Orphanet reasons that because *Dbh* deficiency is lethal in mouse embryos or shortly after birth, "the prevalence of the disorder may be higher than expected," noting a history of spontaneous abortions and stillbirths in parents of affected patients (PMID:16722595). This is an inference from a model organism to human prevalence — cite it as such (`directness: INDIRECT`), not as a measured figure.

---

## 10. Diagnostics

### The diagnostic triad (GeneReviews, PMID:20301647)
> "The diagnosis of DBH deficiency is established in a proband with profound neurogenic orthostatic hypotension, minimal or absent plasma concentrations of norepinephrine and epinephrine, a five- to tenfold elevation of plasma dopamine, and biallelic pathogenic variants in DBH identified by molecular genetic testing."

Wassenberg's equivalent formulation: severe young-onset orthostatic hypotension + undetectable NE/E with raised dopamine + pathogenic *DBH* variants (PMID:33034372).

### Laboratory
- **Plasma catecholamines — the first ancillary test.** "In patients with a clinical suspicion of DBH‐deficiency, measurement of plasma catecholamines is the first ancillary diagnostic test." (PMID:33034372) Observed: NE decreased in 24/24 (extremely low in 20); E decreased in 21/22; dopamine increased in all (extremely high in 12). NE and E stay extremely low on standing while dopamine rises further.
- **The pathognomonic ratio:** "The diagnosis is established by the observation of severe orthostatic hypotension in a patient whose plasma norepinephrine/dopamine ratio is much less than one." (PMID:1677640)
- **Plasma DBH enzyme activity** — absent/severely decreased in 18/18 tested, and absent in CSF in 3/3. But it is **not sufficient alone** because of 4% pseudodeficiency (−1021C>T) (PMID:33034372, PMID:15495941, PMID:16722595).
- **Urine and CSF catecholamines** mirror plasma but are **not required**: "It is not necessary to test catecholamines in urine and cerebrospinal fluid for the diagnosis of DBH‐deficiency." (PMID:33034372)
- **Metabolites:** NE/E metabolites (normetanephrine, metanephrine, MHPG, VMA) absent/low; dopamine metabolites (HVA) raised; L-DOPA elevated (PMID:3291893, PMID:2880016).
- **Routine chemistry to obtain at baseline and on follow-up:** creatinine/eGFR, haemoglobin and indices, platelets, serum **magnesium** and fractional magnesium excretion, potassium, sodium, glucose (PMID:33034372, PMID:20301647).

**LOINC suggestions** — bind only after verifying each code and its Long Common Name against the cache/authority (see the LOINC rules): norepinephrine, epinephrine, dopamine in plasma and in 24-h urine; metanephrines; magnesium [Moles/volume] in serum; creatinine; eGFR; haemoglobin. **Do not write LOINC codes from memory for this entry** — the identity codes need `just loinc-seed-cache` before commit.

### Physiological / functional
- Supine-to-standing BP within 3 min (the definitional measurement; OH = fall ≥20 systolic or ≥10 diastolic) — tilt-table testing where needed.
- Autonomic reflex battery showing **isolated sympathetic adrenergic failure with intact cholinergic function**: no BP rise in Valsalva phase IV, isometric handgrip, or cold exposure; **normal sweating** and normal sympathetic skin response (PMID:16722595, PMID:9651662).
- **Pharmacological probes:** absent pressor response to **tyramine**; paradoxical BP *rise* with **clonidine**; paradoxical hypotension with **ephedrine** (PMID:16722595, PMID:2795065); adrenergic receptor supersensitivity on challenge.
- **Microneurography** — abundant, normally regulated sympathetic nerve traffic, proving the nerves are intact and the transmitter is wrong (PMID:2295511, PMID:27237083).
- **Skin biopsy plus microneurography** proposed as adjunct diagnostics: "skin biopsy and microneurography may help to increase the diagnosis" (PMID:27237083).
- **Orthostatic intraocular pressure + MAP** proposed as a paediatric screening tool in children presenting with ptosis (PMID:23622564).
- **Pupillometry:** absent/abnormally small task-evoked pupil dilation (PMID:21471955); redilatation lag for bilateral Horner's (PMID:9886450).
- EEG (normal interictal, in the misdiagnosed-epilepsy patients), Holter/ECG where bradyarrhythmia is suspected (PMID:40951656), cerebral MRI (structurally normal), EMG/NCS (normal unless a second disorder coexists).

### Genetic testing
Single-gene *DBH* sequencing is the targeted test; the causal variant set is small and c.339+2T>C alone accounts for most alleles, so **targeted sequencing of *DBH* (NM_000787.4), including intronic splice regions**, is the primary approach. Exome/genome sequencing has in practice been the route to diagnosis in atypical cases and in patients with a second, confounding disorder (PMID:26410747, PMID:27237083). CMA/karyotype are not indicated for DBH deficiency itself, but CMA was what explained the extra dysmorphic features in the mosaic 11p13 patient (PMID:20186791) — i.e. consider it when the phenotype exceeds what DBH deficiency explains. Mitochondrial and repeat-expansion testing: not applicable. Carrier testing and prenatal/preimplantation testing are available once familial variants are known (PMID:20301647). Note that in 2006 molecular testing was research-only (PMID:16722595); it is now clinical.

### Differential diagnosis
| Condition | Discriminator |
|---|---|
| **CYB561 deficiency / orthostatic hypotension 2** (PMID:29343526) | **Clinically very similar but plasma dopamine is NORMAL** with severely reduced NE/E; DBH activity normal; no *DBH* mutation. "The CYB561 protein defect leads to a shortage of ascorbate" — i.e. cofactor failure rather than enzyme absence, producing *functional* DBH deficiency. This is the single most important differential and the reason plasma dopamine must be measured, not just NE. |
| Pure autonomic failure, MSA, Parkinson disease with nOH | Later onset, additional neurological signs, parasympathetic/cholinergic involvement, supine hypertension; olfaction worse in PAF (PMID:21282592); pupils less often affected in MSA (PMID:16966943) |
| Familial dysautonomia | Excluded by typical intradermal-histamine flare, normal tearing/taste/smell, intact corneal and deep tendon reflexes, absence of Ashkenazi Jewish ancestry (PMID:16722595) |
| Menkes disease (ATP7A, copper) | Excluded by absence of profound intellectual disability and hypopigmentation (PMID:16722595); note the mechanistic kinship — DBH is a copper enzyme, and DBH deficiency has been discussed in the context of copper-transporter mutations (PMID:9327848) |
| Volume depletion, drug-induced hypotension, amyloidosis, Guillain–Barré, paraneoplastic/toxic neuropathy, Fabry disease | Per the differential list in PMID:33034372 |
| Epilepsy | Seizures only on standing, normal interictal EEG (PMID:33034372) |
| Congenital/acquired ptosis, myasthenia | Ptosis plus orthostatic BP drop; measure standing BP (PMID:23622564, PMID:35202494) |

**Screening:** no newborn screening exists, and DBH deficiency is not on any NBS panel. GeneReviews supports cascade carrier testing in at-risk relatives once variants are known. One patient in the series was diagnosed at 40 **because of a positive family history**, was asymptomatic by report, had severe OH on measurement, and improved on treatment (PMID:33034372) — a strong argument for family screening.

---

## 11. Outcome / Prognosis

- **Life expectancy:** not formally quantified. "Little is known about prognosis." (PMID:16722595) No survival curve, 5-/10-year survival, or mortality rate exists for this disease — state this rather than inventing a figure.
- **Deaths reported in the 25-patient series (PMID:33034372):** one fatal case at age 28 after up to 4 years of L-DOPS, with severe phenotype and frequent childhood syncope; autopsy showed cortical gliosis microfoci, cardiac arteriolar smooth-muscle hypertrophy, conduction-system fibrosis, and sclerotic glomeruli, and "the authors felt that his early death might have resulted from cardiac dysrhythmia." Three further deaths from an earlier review (age 20, suspected suicide; ages 57 and 63, suspected natural causes); one Dutch patient died at 60 of urogenital cancer. So long survival into the sixth and seventh decades is documented, alongside one early death — the honest summary is "variable, with reported survival to at least the seventh decade."
- **Morbidity, untreated:** "Limitation in standing tolerance, limited ability to exercise and traumatic morbidity related to falls and syncope may represent later evolution." (PMID:16722595) Plus hypotension-induced seizures, repeated perinatal hospitalization, and the misdiagnosis burden (median 24 years to diagnosis, including anti-epileptic treatment in three patients).
- **Complications:** chronic kidney impairment; anemia; hypomagnesemia; falls/trauma; hypoglycaemia; failed lactation; possible reduced female fertility; hyperinsulinemia/insulin resistance (PMID:27778639); rarely bradyarrhythmia (PMID:40951656).
- **Recovery potential with treatment — the central prognostic fact, and it is partial.**
  > "Treatment of DBH‐deficiency with L‐DOPS greatly improves quality of life and exercise intolerance. However, catecholamine levels, kidney function, anemia, and hypomagnesaemia do not or only partially respond to treatment. Furthermore, ptosis often does not disappear, and blood pressure does not normalize; many patients still have (less pronounced) orthostatic hypotension on office measurements." (PMID:33034372)

  Quantitatively: all 7 patients with analysable measurements still met OH criteria on treatment, with mean falls reduced from 58/38 to **38/21 mmHg**. Plasma NE became detectable in 11/13 but reached normal in only 2; epinephrine stayed undetectable in 9; dopamine fell in all 12 measured but stayed above normal in 10. Renal function improved in only 3 patients; haemoglobin rose in 4; serum magnesium rose significantly (0.60 → 0.67 mmol/L, P = .019).
- **Prognostic factors:** severity and age at onset of syncope (the fatal case had frequent syncope from early childhood); baseline eGFR; delay to diagnosis and treatment (the explicit argument of PMID:35202494 for early L-DOPS). No validated prognostic biomarker exists; the authors nominate routine biochemistry plus the orthostatic hypotension questionnaire as the parameters to follow, and raise 24-h BP monitoring targeting restoration of the nocturnal dip as an unresolved question.

---

## 12. Treatment

### Targeted therapy — droxidopa (L-threo-DOPS, L-DOPS)
The defining therapeutic fact about this disease is that it is **treatable by precursor bypass**: droxidopa is decarboxylated by AADC to norepinephrine, needing no DBH.

> "Administration of L-threo-3,4-dihydroxyphenylserine (droxidopa) restores plasma norepinephrine concentration and alleviates orthostatic hypotension and other symptoms of abnormal cardiovascular regulation." (PMID:20301647)

Original demonstration — a single-blind placebo-controlled trial in two patients (PMID:2890806):
> "Dose-dependent increases in blood pressure were obtained over the range 150-600 mg."
with MAP rising 33 and 19 mmHg at 600 mg, tightly correlated with plasma norepinephrine (r = 0.995 and 0.88), urinary norepinephrine rising from undetectable to 338 and 511 µg/24 h, increased standing time, and no side effects. Confirmed independently the same year (PMID:2890807: "DOPS switched on the production of noradrenaline and reduced the excessive production of dopamine") and over 6–12 months (PMID:3149290). Thompson 1995 reported "dramatic clinical improvement with resolution of the orthostatic symptoms" (PMID:8801271).

**Dosing (PMID:33034372, following FDA schedules):** adults start **100 mg two to three times daily**, titrate on clinical response to a maximum of **1800 mg/day in three doses**; "in our experience, more than 1200 mg per day is rarely needed." The **last dose must be >4 hours before bedtime to avoid nocturnal hypertension**. Children: start **2 mg/kg/day in 2–3 doses**, increasing to **5–10 mg/kg/day**, with BP and side-effect monitoring. Observed cohort doses: 400–1800 mg/day in 2–3 doses, stable over years. Temporary dose increases during illness or hot weather are useful (personal observation). One adolescent developed mild hypertension on 100 mg b.i.d. and was reduced to 75 mg b.i.d. with adequate response — i.e. titrate down as readily as up.

**Tolerability:** "L‐DOPS is excellently tolerated in patients with DBH‐deficiency." The only side effect recorded in the Dutch cohort was possible increased nightmares in one patient. Across the broader nOH population (not DBH-specific), the long-term open-label NOH303 study (n=102, up to 12 months) found droxidopa "generally well tolerated and provided durable improvements in nOH signs and symptoms", with falls, UTI and headache the commonest adverse events (PMID:27636856); pooled NNT for symptom improvement was below 10 with NNH 23–302 (PMID:27538531); supine hypertension is the monitoring priority (PMID:25559422).

**Regulatory status:** FDA-approved for symptomatic neurogenic orthostatic hypotension in adults, with DBH deficiency named in the indication (PMID:28604565, PMID:30090842-adjacent reviews). But: "in many countries including the Netherlands L‐DOPS is not registered and should be prescribed off‐label or for compassionate use" — the Dutch cohort imported it from Sumitomo (Japan) under compassionate use. Access, not efficacy, is the practical obstacle.

**NCIT suggestions.** Treatment action: `NCIT:C15986` Pharmacotherapy. Therapeutic agent: droxidopa (verify the NCIT/CHEBI identifier by lookup before binding — droxidopa is CHEBI:135309; the NCIT agent code must be read from NCIT, not recalled). `therapeutic_modality: SMALL_MOLECULE`. Dosing interval: `dosing_interval: two to three times daily` with `dosing_interval_days: 0.5` or omitted — prefer omitting rather than forcing a sub-daily interval into a day-denominated slot.

### Less effective / supportive
- **Fludrocortisone** and **midodrine**: "Other treatment options for orthostatic hypotension (fludrocortisone, midodrine) are not as effective as droxidopa" (PMID:20301647). NCIT: `NCIT:C15986` with the respective agents. Earlier empirical mineralocorticoid and adrenergic-agonist therapies had only mild effects (PMID:16722595).
- **Non-pharmacological:** avoid heat, strenuous exercise, motionless standing, dehydration; avoid nephrotoxic drugs (PMID:20301647). Behavioural/physical counter-measures → `therapeutic_modality: BEHAVIORAL`.
- **Surgical correction of ptosis as needed** (PMID:20301647) — `NCIT:C15329` Surgical Procedure (ophthalmic/ptosis repair), `therapeutic_modality: SURGERY`. Note ptosis persists under L-DOPS in most patients, which is why surgery remains on the list.
- **Standard treatment for nasal stuffiness and reduced kidney function** (PMID:20301647).
- **Pacemaker** — in the single newborn bradyarrhythmia case; notably the device showed **0% pacing after L-DOPS**, and the authors concluded pacing "might have been avoidable" (PMID:40951656). Curate as a case-specific intervention with that caveat, not as a recommended therapy.

### Surveillance (PMID:20301647)
Annual review of droxidopa efficacy and adverse events; BUN/creatinine every two years or more often if renal function is declining; plasma magnesium and potassium every two years; referral to an autonomic specialist before surgery or pregnancy.

### Pregnancy and peripartum
Routine BP monitoring during pregnancy and delivery with droxidopa dose adjustment; extra doses may be needed during delivery and adjustment post partum (PMID:20301647). Wassenberg: healthy pregnancy and delivery are possible before and during treatment, and "with the limited data at hand continuing L‐DOPS during pregnancy appears safe and desirable"; three Dutch women had difficulty conceiving, and **lactation has never been successful**. An elective caesarean under combined spinal-epidural anaesthesia is documented with uncomplicated recovery (PMID:12180590) — the citable anaesthetic-management reference.

### Pharmacogenomics, advanced therapeutics, trials
- **Pharmacogenomics:** none established. The disease-causing gene is itself the pharmacologic context — droxidopa works *because* it bypasses the defective gene product, which is genotype-independent.
- **Gene therapy, cell therapy, RNA therapy, gene editing:** none for DBH deficiency. The nearest adjacent work is AAV gene therapy in a Menkes mouse model (PMID:30090842), a different copper-related disease.
- **Pharmacological chaperone — the one unexploited mechanistic lead.** Glycerol rescued trafficking of ER-retained mutant DBH in vitro (PMID:21209083). This is an in-vitro result in a heterologous system with no animal or human follow-up; record it as an experimental direction, not a therapy.
- **Clinical trials:** NCT00889135 (Vanderbilt, long-term L-DOPS expanded access, explicitly including DBH deficiency) and NCT00738062 (Chelsea Therapeutics NOH303, open-label, PAF/DBH deficiency/non-diabetic neuropathy — published as PMID:27636856). Both should be verified against ClinicalTrials.gov with `just fetch-reference` before curation, and their `status` re-checked with `just clinicaltrials-status-audit`, since these records are old.
- **Clinical trials are unlikely to be feasible:** "Because of the extreme rarity of this disorder, clinical trials to determine optimum treatment strategy in DBH‐deficiency seem hard to effectuate." (PMID:33034372)

---

## 13. Prevention

- **Primary prevention:** impossible — the disorder is congenital and monogenic. The only primary-prevention lever is **reproductive**: genetic counselling, carrier testing of at-risk relatives, and prenatal or preimplantation genetic testing once the familial variants are known (PMID:20301647).
- **Secondary prevention (early detection):** no newborn or population screening programme exists. The realistic routes are (i) **cascade testing in families** — one patient was found at 40 via family history, asymptomatic by report but with severe OH and a treatment response (PMID:33034372); (ii) **measuring standing blood pressure in any child with unexplained ptosis**, the explicit recommendation of PMID:23622564 and the thrust of PMID:35202494; (iii) considering a genetic cause early in any child with true orthostatic hypotension, which is rare in childhood (PMID:33034372); (iv) considering DBH deficiency in neonatal hypoglycaemia work-up (PMID:20301647, PMID:40951656).
- **Tertiary prevention (preventing complications) — this is where most of the action is:** early and sustained droxidopa; avoidance of heat, motionless standing, strenuous exercise, dehydration, heavy meals and alcohol; avoidance of nephrotoxic drugs; dosing timed to avoid nocturnal hypertension; periodic renal, haematological and electrolyte surveillance; pre-operative and pre-pregnancy autonomic referral; fall-risk management.
- **Immunization / public health / environmental interventions:** not applicable. (No infectious or environmental aetiology.)
- **Prophylaxis:** no prophylactic medication beyond maintenance droxidopa. Temporary dose escalation during illness or hot weather functions as situational prophylaxis.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** human — `NCBITaxon:9606`. Model species: house mouse `NCBITaxon:10090`.
- **Orthologous genes:** mouse *Dbh* (NCBI Gene 13166; MGI:94864); rat *Dbh* (NCBI Gene 29740). The human gene is NCBI Gene 1621.
- **Natural disease in other species:** **no naturally occurring DBH deficiency has been reported in any companion animal, livestock species, or wildlife population.** No OMIA entry for the condition was identified, and no breed association exists — so there is no VBO term to assign. Everything known outside humans comes from engineered mouse lines (§15). State this as a genuine absence of natural disease rather than leaving the section implicitly open.
- **Comparative biology — and a major species divergence.** The enzyme and the pathway are deeply conserved, but the *consequence of losing it* is not:
  - **In mice, loss is largely embryonic-lethal**; in humans it is compatible with survival to the seventh decade. Orphanet draws the inference that human prevalence may therefore be underestimated (PMID:16722595).
  - **In mice, the CNS phenotype is prominent** (maternal behaviour, learning, antidepressant sensitivity); **in humans the CNS is remarkably spared** (normal IQ, intact olfaction, preserved sleep cycling) — the "other neuromodulators have taken over" interpretation (PMID:21471955). This is a textbook `HUMAN_MODEL_MISMATCH` and should be curated as one.
  - Evolutionary conservation is best cited from the Alliance of Genome Resources / HomoloGene rather than asserted.
- **Transmission / zoonotic potential:** not applicable — a non-transmissible inherited enzymopathy.

---

## 15. Model Organisms

### The *Dbh* knockout mouse (the principal model)
**Line:** *Dbh*−/− (targeted disruption), Thomas, Matsumoto & Palmiter, *Nature* 374:643–646, 1995 (**PMID:7715704**, "Noradrenaline is essential for mouse fetal development"). Mice cannot make norepinephrine or epinephrine and **produce dopamine as the terminal catecholamine instead** — the exact biochemical architecture of the human disease.

**Phenotype recapitulation and its limits:**
- **Embryonic lethality** — most homozygous embryos die in utero, apparently of cardiovascular failure, resembling tyrosine-hydroxylase-null embryos (PMID:7715704; compare the TH knockout, PMID:7715703, where ~90% die between E11.5 and E15.5). Survival of *Dbh*−/− embryos in heterozygous dams depends on maternal catecholamines crossing the placenta; in homozygous dams all embryos die. **This is the key divergence from human disease and the reason the model is hard to use.**
- **Pharmacological rescue is the standard husbandry protocol:** maternal L-threo-DOPS during gestation prevents the deaths, after which mutants "develop into viable adults without further intervention" (PMID:7715704; the rescue protocol as applied is described in PMID:10051631: "Mice were rescued during prenatal development by treatment with l-threo-3,4,dihydroxyphenylserine"). Note this means essentially every adult *Dbh*−/− mouse studied has had a pharmacologically altered developmental history — a real confound to record as a model limitation.
- **Altered metabolism, thermoregulation, cardiovascular tone** (PMID:9139828, *Nature* 1997, thermoregulatory and metabolic phenotypes).
- **Impaired maternal behaviour** (PMID:9393852, *Cell* 1997) and broader behavioural/learning roles for NE (PMID:9189272).
- **Sweat response:** "Norepinephrine facilitates the development of the murine sweat response but is not essential" (PMID:9151744) — interesting beside the preserved (cholinergic) sweating in human patients.
- **Impaired Th1 cellular immunity** — normal immune development under specific-pathogen-free conditions but increased susceptibility to *Listeria monocytogenes* and *M. tuberculosis*, extreme thymic involution, reduced IFN-γ/TNF-α and increased IL-10, and reduced IgG2a responses (PMID:10051631). 32% of *Dbh*−/− mice died during adolescence in non-SPF housing, and those deaths stopped under SPF conditions. **No corresponding immunodeficiency is described in human patients** — another model/human divergence worth recording rather than transferring.
- **DOPS restores plasma noradrenaline and reverses behavioural abnormalities** in the mouse, and restores antidepressant sensitivity (cited in PMID:16722595) — the model's main pharmacological validation of the human treatment.
- **Cardiac conduction:** *Dbh*+ catecholaminergic cardiomyocytes contribute to cardiac conduction structure and function, with conduction abnormalities (prolonged refractory periods, lower Wenckebach and 2:1 conduction rates at slower heart rates) in *Dbh* knockouts (Sun T et al., *Nat Commun* 2023, **PMID:38016975**, as described in PMID:40951656). This is the mechanistic basis offered for the human newborn bradyarrhythmia case — a developmental rather than a purely neurotransmitter role for DBH, and currently the most interesting open question in the biology.

### Humanized model
**Human *DBH* BAC transgenesis in *Dbh* knockout mice** (Cubells et al., *PLoS One* 2016, **PMID:27148966**): the human BAC transgene "restored normal catecholamine levels to the peripheral organs and brain of" the knockouts and rescued embryonic lethality, growth delay and ptosis. The rs1611115 (−1021C>T) promoter variant had no effect on mRNA levels in this system. This is the appropriate model for testing human *DBH* alleles in vivo, and the negative rs1611115 result is a useful counterweight to over-reading that variant.

### Cellular / in vitro
Heterologous expression of mutant human DBH established the two-route loss of function and the glycerol chaperone rescue (PMID:21209083). No iPSC, organoid, or patient-derived neuronal model of DBH deficiency was identified — a real gap, and the obvious next non-animal model system given that the lesion is a proteostatic one.

### Other species / induced models
- **Rat:** DSP-4 chemical lesioning of locus coeruleus noradrenergic projections (PMID:22754504) models *noradrenergic denervation* but not DBH deficiency — the enzyme is intact and the lesion is anatomical. Do not curate as a disease model.
- **Arsenicosis** lowers serum DBH activity with reduced ascorbate and copper in exposed humans (PMID:24711750) — an acquired, partial, cofactor-level reduction, mechanistically adjacent to CYB561 deficiency, and **not** a model of the Mendelian disease.
- No zebrafish, Drosophila, or C. elegans model of this disease was identified.

### Resources
MGI (mouse *Dbh*, MGI:94864), IMSR/MMRRC for line availability, Alliance of Genome Resources for orthology and phenotype comparison, RGD for the rat gene.

### Suggested `modeled_mechanisms` framing for the KB
| Model | Target node | relationship | fidelity | model_scale | Key limitation |
|---|---|---|---|---|---|
| *Dbh*−/− mouse (PMID:7715704) | Absent norepinephrine biosynthesis | RECAPITULATES | HIGH | MOLECULAR | Embryonic lethality absent in humans; all adults DOPS-rescued in utero |
| *Dbh*−/− mouse | Orthostatic/cardiovascular failure | PARTIALLY_RECAPITULATES | MODERATE | ORGANISM | Quadrupedal posture — no orthostatic challenge comparable to human upright stance (`PROXY_QUANTITY` / `BOUNDARY_OMISSION`) |
| *Dbh*−/− mouse (PMID:10051631) | — | FAILS_TO_RECAPITULATE for human immune phenotype | LOW | ORGANISM | Th1 immunodeficiency has no human counterpart; requires `limitations` + evidence |
| Human *DBH* BAC × *Dbh*−/− (PMID:27148966) | Human allele function, ptosis | RECAPITULATES | MODERATE | ORGANISM | Transgene copy number/regulatory context differs from endogenous locus |
| Heterologous mutant DBH expression (PMID:21209083) | Mutant DBH ER retention | RECAPITULATES | MODERATE | MOLECULAR | Non-neuronal cell background; no secretory-vesicle compartment (`BOUNDARY_OMISSION`) |
| *Dbh* KO conduction studies (PMID:38016975) | Cardiac conduction development | PARTIALLY_RECAPITULATES | UNKNOWN | TISSUE | Single human case; developmental role not shown in patients |

---

## Curation notes and cautions

1. **Two frequency tables exist and must not be merged.** Wassenberg 2021 (n=25, PMID:33034372) and the Robertson-1991-derived table in Orphanet (PMID:16722595, n≈6) give different percentages for ptosis (90% vs 67%), nocturia, and impaired ejaculation (3/5 males vs 100%). Curate each with its own source and population.
2. **The 4% figure is not a carrier frequency.** It is the prevalence of *plasma DBH pseudodeficiency* from −1021C>T in healthy people with normal norepinephrine. Using it as a carrier or prevalence figure would be a serious error, and it sits adjacent to the real diagnostic text in both reviews.
3. **Verify every CURIE by lookup before binding.** The HPO, GO, CL, UBERON, CHEBI, NCIT and LOINC terms above are *suggestions from this report* and must be resolved against the ontologies in the same step they are written. In particular: the LOINC codes were deliberately not written out; the NCIT droxidopa agent code was deliberately not written out; `CL:0011110` (noradrenergic neuron) and the ventrolateral-medulla UBERON term need confirmation. Bind nothing from this report without a lookup.
4. **One cached reference is not about this disease.** `references_cache/PMID_30090842.md` is a Menkes-disease AAV gene-therapy paper that mentions DBH; it matched a text grep. Do not cite it as DBH-deficiency evidence.
5. **Nomenclature divergence between sources.** Orphanet's variant table (PMID:16722595) uses legacy numbering (G259A/V87M etc.); Wassenberg's uses NM_000787.4 (c.301G>A/p.Val101Met etc.). Curate the NM_000787.4 forms and treat the older strings as the same variants under a different transcript — do not list them as additional distinct variants.
6. **Deliberately not asserted here:** a gnomAD allele frequency for c.339+2T>C (needs a live gnomAD lookup); a Dutch founder effect (needs Zabetian 2003 haplotype data read directly); a consanguinity rate (unreported); a survival or mortality rate (does not exist); an epigenetic mechanism (none reported); a LOINC code (needs cache seeding). Each of these is a gap with a stated reason, which is more useful than a plausible number.
7. **`ORPHA:230`, `CGGV:` and `GEO:` citation opportunities.** Orphanet is already citable as a structured source (`just fetch-reference ORPHA:230`) for prevalence class and the phenotype table; check ClinGen for a *DBH*–DBH-deficiency gene-disease validity assertion (`just list-gene-validity`) and copy the tier rather than assigning one. No disease-specific GEO dataset was identified.

**Sources (web):** [GeneReviews NBK1474](https://www.ncbi.nlm.nih.gov/books/NBK1474/) · [MedlinePlus Genetics: DBH deficiency](https://medlineplus.gov/genetics/condition/dopamine-beta-hydroxylase-deficiency) · [OMIM 223360](https://www.ncbi.nlm.nih.gov/omim/223360) · [Vanderbilt Autonomic Dysfunction Center](https://www.vumc.org/autonomic-dysfunction-center/dopamine-beta-hydroxylase-deficiency) · [Thomas 1995, Nature 374:643](https://www.doi.org/10.1038/374643A0) · [NCT00889135](https://clinicaltrials.gov/study/NCT00889135) · [NCT00738062](https://clinicaltrials.gov/study/NCT00738062)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 57 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 36 |
| Quoted claims found in source | 33 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 57 |
| On topic | 42 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:33034372`: "A potential damaging factor to the kidneys, which is quite unique to patients with DBH‐deficiency, is the very high level of dopamine intracellularly in the proximal tubular cells. In high concentrations, dopamine and intermediate dopamine metabolites are thought to be autotoxic, possibly because of increased radical oxygen species production."
  - closest text in source: "A potential damaging factor to the kidneys, which is quite unique to patients with DBH‐deficiency, is the very high level of dopamine intracellularly in the proximal tubular cells"
- `PMID:7715704` *(abstract only)*: "develop into viable adults without further intervention"
  - Text part not found as substring: 'develop into viable adults without further intervention' (note: only abstract available for PMID:7715704, full text may contain this excerpt)
- `PMID:10051631`: "develop into viable adults without further intervention"
  - closest text in source: "The number of viable organisms administered was confirmed by culturing serial dilutions on trypticase soy agar (TSA, Becton-Dickinson)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 82 |
| Resolved | 79 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0004237` (1 mention) - the report calls it "arterial/arteriolar smooth muscle (arteriolar smooth-muscle hypertrophy at autopsy)"; UBERON calls it **blood vessel smooth muscle**
- `UBERON:0001826` (1 mention) - the report calls it "nasal mucosa (stuffiness — loss of vasoconstrictor tone)"; UBERON calls it **nasal cavity mucosa**
- `UBERON:0002371` (1 mention) - the report calls it "bone marrow (sympathetic innervation; anemia hypothesis)"; UBERON calls it **bone marrow**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0009123` (2 mentions) - the report calls it "label: *orthostatic hypotension 1"; MONDO calls it **orthostatic hypotension 1**
- `HP:0001873` (1 mention) - the report calls it "Mild thrombocytopenia in 4 patients"; HP calls it **Thrombocytopenia**
- `UBERON:0001235` (1 mention) - the report calls it "adrenal medulla"; UBERON calls it **adrenal cortex**
- `UBERON:0000966` (1 mention) - the report calls it "retina (DBH-expressing)"; UBERON calls it **retina**, and lists "retinas" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.