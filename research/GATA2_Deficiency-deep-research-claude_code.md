---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-31T19:54:37.652982'
end_time: '2026-08-31T20:00:33.783239'
duration_seconds: 356.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: GATA2 Deficiency
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
  - claude-sonnet-5
  web_search_requests: 20
  num_turns: 28
  total_cost_usd: 1.6028183999999996
  session_id: 70de5b01-cdc4-5635-9abb-0681d0e2fde9
  stop_reason: end_turn
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
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 49
  verified: 45
  not_found: 1
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.022
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0032223
    reported_labels:
    - CMML term if bound; else NCIT
    ontology_label: Blood group
  - term_id: HP:0032101
    reported_labels:
    - Recurrent atypical mycobacterial infections, if available
    ontology_label: Unusual infection
  - term_id: HP:0002090
    reported_labels:
    - recurrent fungal infection group
    ontology_label: Pneumonia
  - term_id: HP:0012125
    reported_labels:
    - HPV-related neoplasia; or map via NCIT
    ontology_label: Prostate cancer
  - term_id: HP:0005506
    reported_labels:
    - bone marrow hypocellularity
    ontology_label: Chronic myelogenous leukemia
  labels_variant: 2
  unresolved_terms:
  - UBERON:0000132
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GATA2 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GATA2 Deficiency** covering all of the
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

I'll research GATA2 Deficiency now, gathering primary literature citations across the required domains.

I now have sufficient primary-literature coverage across all required domains. Writing the full comprehensive report.

# GATA2 Deficiency — Comprehensive Research Report

*(Prepared for dismech curation. Per project convention, germline predisposition is treated separately from the somatic myeloid malignancies it predisposes to — see §6 and the note in §2. Basic genetics concepts (penetrance, mosaicism, haploinsufficiency mechanics) are not re-explained here per user context; the report leads with disease-specific claims and citations.)*

---

## 1. Disease Information

**Overview.** GATA2 deficiency (GATA2 deficiency syndrome, G2DS) is an autosomal dominant disorder caused by heterozygous germline pathogenic variants in *GATA2*, a master hematopoietic zinc-finger transcription factor. A single genetic lesion produces a syndrome that was originally described as four apparently separate entities before their shared molecular cause was recognized: **MonoMAC syndrome** (monocytopenia with *Mycobacterium avium* complex infection), **DCML deficiency** (dendritic cell, monocyte, B- and NK-lymphoid deficiency), **Emberger syndrome** (primary lymphedema with MDS), and **familial MDS/AML**. Spinner et al. (Blood 2014, PMID:24227816) established that these are one disorder: *"Haploinsufficiency of the hematopoietic transcription factor GATA2 underlies monocytopenia and mycobacterial infections; dendritic cell, monocyte, B, and natural killer (NK) lymphoid deficiency; familial myelodysplastic syndromes (MDS)/acute myeloid leukemia (AML); and Emberger syndrome."* This is a curatorial **lump call already made in the field** — current nomenclature (Calvo & Hickstein, Blood 2023;141(13):1524–1532, PMID:36455197, "The spectrum of GATA2 deficiency syndrome") treats MonoMAC/DCML/Emberger/familial MDS-AML as phenotypic variation on one genetic lesion rather than genuinely distinct diseases, which should be reflected as `has_subtypes` or historical-synonym framing rather than separate dismech entries.

**Key identifiers:**
- **Gene:** *GATA2*, HGNC:4173, OMIM *137295, chromosome 3q21.3
- **OMIM phenotypes:** Immunodeficiency 21 (MonoMAC) #614172; Emberger syndrome #614038; MDS predisposition (germline GATA2 mutation) #614286; AML predisposition citing GATA2 under #601626
- **MONDO:** MONDO:0013607 (GATA2 deficiency)
- **Orphanet:** ORPHA:228423 (GATA2 deficiency spectrum)
- **ICD-10:** D72.8 (other specified disorders of white blood cells) — no dedicated ICD-10/11 code exists
- **MeSH:** overlapping entries under primary immunodeficiency/MDS headings; no single dedicated MeSH descriptor

**Synonyms:** MonoMAC syndrome; DCML deficiency; Emberger syndrome; familial MDS/AML with GATA2 mutation; NK cell deficiency (GATA2-related); MGN syndrome (monocytopenia and mycobacterial infection).

**Evidence base:** Predominantly aggregated disease-level cohort data — the NIH natural history cohort (Spinner 2014, n=57, PMID:24227816), a French/Belgian multicenter cohort of 79 patients (Haematologica), and registry-based pediatric HSCT series (EWOG-MDS, n=65) — supplemented by individual case reports for rarer manifestations (interstitial lung disease, Hodgkin lymphoma). This is not primarily an EHR-derived phenotype.

---

## 2. Etiology

**Disease causal factor:** Monogenic. Heterozygous germline pathogenic *GATA2* variants are necessary and sufficient; there is no reported environmental or infectious primary cause. (Note the important **genocopy distinction** for dismech: somatic 3q26/*MECOM* rearrangements — inv(3)(q21q26), t(3;3)(q21;q26) — hijack the distal *GATA2* hematopoietic enhancer (G2DHE) to drive *EVI1* overexpression while silencing *GATA2* on the rearranged allele in **sporadic AML**; this is a somatic leukemia mechanism that convergently reduces GATA2 dosage and should NOT be modeled as the same pathophysiology node as germline GATA2 deficiency, even though both produce "GATA2 haploinsufficiency" biochemically. (Atlas Genet Cytogenet Oncol Haematol; Blood 2020;136(2):224, "Atypical 3q26/MECOM rearrangements genocopy inv(3)/t(3;3) in acute myeloid leukemia.")

**Genetic risk factors:**
- ~50% de novo variants; remainder inherited from an affected or (rarely) mosaic/asymptomatic parent (Homan et al., Hum Mutat 2021, PMID:34387894, "GATA2 deficiency syndrome: A decade of discovery" — confirms de novo variants in "24 individuals... among over 480 individuals with germline GATA2 pathogenic or likely pathogenic variants" in the aggregate literature).
- Variant classes: (1) missense variants clustering in the C-terminal zinc finger (ZF2) DNA-binding domain, notably the recurrent hotspot **R396Q**; (2) null variants (nonsense, frameshift, splice-site, whole-gene deletion); (3) ~10% noncoding variants disrupting the **intron-4 −77/+9.5-equivalent human enhancer** (the "EBOX-GATA-ETS" element) or the distal hematopoietic enhancer region, causing regulatory haploinsufficiency without coding change (PDQ GATA2 Deficiency Syndrome, NCBI Bookshelf NBK606140).
- No pathogenic *GATA2* variants are present in gnomAD population databases, consistent with high penetrance and reproductive/somatic selection against germline carriage in the general population.
- Genotype-phenotype correlation: **null variants associate more strongly with viral infection susceptibility and lymphedema** than missense variants (Spinner 2014, PMID:24227816); the PDQ summary states lymphedema specifically "is associated with GATA2 null pathogenic variants."

**Modifier/susceptibility factors — somatic events, not germline risk factors:** Progression to MDS/AML is driven by acquired somatic lesions superimposed on the germline haploinsufficient marrow: monosomy 7 (70–80% of pediatric MDS cases, 20–40% of adult cases), trisomy 8 (20–40% of adults), der(1;7) translocation, and somatic mutations in *ASXL1*, *STAG2*, *SETBP1*, and *RUNX1*. STAG2 mutation frequency and trisomy 8 both increase with age (PDQ summary; Blood 2023 review).

**Protective factors:** None specific to germline variant type are established. No population-level protective allele has been reported (consistent with gnomAD absence of the pathogenic alleles).

**Environmental risk modifiers / gene-environment interaction:** Not a primary environmental disease. The immunodeficiency component determines *which* pathogens cause disease (nontuberculous mycobacteria, HPV, EBV, fungi) rather than environmental exposure causing the underlying lesion — this is host-susceptibility, not classic gene-environment interaction.

---

## 3. Phenotypes

Frequencies below are from the NIH cohort (Spinner et al., Blood 2014, n=57, PMID:24227816) unless noted; onset/course descriptors are qualitative syntheses from the same source and the 2023 Blood review.

| Phenotype | Frequency | HPO suggestion |
|---|---|---|
| Myelodysplastic syndrome | 84% (of those with hematologic disease); 75% of all symptomatic carriers develop myeloid malignancy overall | HP:0002863 Myelodysplasia |
| Acute myeloid leukemia | 14% | HP:0004808 Acute myeloid leukemia |
| Chronic myelomonocytic leukemia | 8% | HP:0032223 (CMML term if bound; else NCIT) |
| Monocytopenia | Near-universal (defining feature) | HP:0001099 Monocytopenia |
| B-lymphopenia | Near-universal | HP:0010976 B lymphocytopenia |
| NK-lymphopenia / NK cell deficiency | Near-universal, with impaired NK cytotoxicity | HP:0040218 Natural killer cell deficiency (or closest HPO) |
| Dendritic cell deficiency | Near-universal (defining "DCML" feature) | free-text / immunophenotype, no dedicated HPO |
| Severe viral infections (HSV, VZV, EBV, HPV) | 70% | HP:0002960 Recurrent viral infections |
| Disseminated nontuberculous mycobacterial infection | 53% | HP:0032101 (Recurrent atypical mycobacterial infections, if available) |
| Invasive fungal infection | 16% | HP:0002090 (recurrent fungal infection group) |
| Diffusion defect (lung) | 79% | HP:0006536 Reduced DLCO |
| Ventilatory defect | 63% | HP:0002088 Abnormal lung function |
| Pulmonary alveolar proteinosis | 18% (up to ~50% of adults in some series) | HP:0006517 Pulmonary alveolar proteinosis |
| Pulmonary arterial hypertension | 9% | HP:0002092 Pulmonary hypertension |
| Warts (cutaneous/anogenital HPV) | 53% | HP:0200043 Verrucae |
| HPV-positive tumors (cervical/anal/vulvar dysplasia and carcinoma) | 35% | HP:0012125 (HPV-related neoplasia; or map via NCIT) |
| Panniculitis | 30% | HP:0012286 Panniculitis |
| EBV-positive tumors | 4% (includes reported Hodgkin lymphoma cases) | — |
| Sensorineural hearing loss (congenital) | 76% in some series; part of constitutional ~50% cluster | HP:0000407 Sensorineural hearing loss |
| Lymphedema | 11% (up to ~30% in other cohorts) | HP:0001004 Lymphedema |
| Venous thrombosis | 25% | HP:0004936 Venous thrombosis |
| Miscarriage | 33% (women of reproductive age) | HP:0005268 Recurrent miscarriage |
| Hypothyroidism | 14% | HP:0000821 Hypothyroidism |
| Hypocellular/dysplastic bone marrow with atypical megakaryocytes | 92% (bone marrow finding) | HP:0005506 (bone marrow hypocellularity) |
| Inverted CD4:CD8 T-cell ratio | Common | — |
| Hydrocele, urogenital malformation | Part of constitutional cluster (~50%) | HP:0000034 Hydrocele; relevant UGT terms |
| ADHD-spectrum disorders | Reported in constitutional cluster | HP:0007018 Attention deficit hyperactivity disorder |

**Onset/course:** Median age of clinical onset ~18–20 years (range 0–78), with the constellation typically emerging in **late childhood through early adulthood** rather than infancy — pediatric presentation is usually cytopenia/MDS or infection-driven rather than the constitutional (deafness/lymphedema) features, which are congenital but often noted retrospectively. Median age of myeloid neoplasm diagnosis is bimodal — ~12 years in pediatric-onset disease vs. ~35 years in adult-onset (PDQ NBK606140) — a distinction directly relevant to the dismech pediatric-framing convention: **pediatric GATA2-MDS is disproportionately monosomy-7-driven (70–80% vs. 20–40% in adults)** and behaves as a more aggressive, faster-progressing entity than adult-onset GATA2-MDS, arguing for treating pediatric vs. adult progression as distinguishable `progression` phases rather than a single undifferentiated course. Course is progressive and highly variable in tempo, even within families sharing an identical variant — some carriers remain asymptomatic lifelong. Lifetime penetrance is estimated at **>80% by age 60** across the aggregate literature (~90% cited in some cohorts).

**Quality of life:** Not separately quantified with EQ-5D/SF-36 instruments in the literature identified; QoL burden is described narratively (chronic infection burden, HSCT-related morbidity, malignancy anxiety) rather than measured with standardized instruments.

---

## 4. Genetic/Molecular Information

**Causal gene:** *GATA2* (HGNC:4173, NCBI Gene 2624, OMIM *137295), chromosome 3q21.3. Six zinc-finger-transcription-factor exons; two zinc fingers (ZF1 N-terminal, ZF2 C-terminal DNA-binding).

**Variant classification and type:**
- **Missense** — the single largest reported class; in one series "19 different missense mutations were identified in 24 probands and 14 relatives (46%)." Cluster predominantly in ZF2. Recurrent hotspot **p.R396Q** is the subject of a dedicated 2024/2025 knock-in mouse model (below).
- **Null variants** — nonsense, frameshift, canonical splice-site, whole-gene deletion, and even some synonymous variants shown to disrupt splicing.
- **Regulatory/noncoding** — ~10% of cases: point substitutions or small indels in the intron-4 enhancer element (variously termed the −77/G2DHE/"EBOX-GATA-ETS" enhancer, human ortholog of the mouse **+9.5 kb enhancer**), and tandem duplications.
- **Functional impact category:** predominantly **loss-of-function / haploinsufficiency**; ZF2 missense variants can also act as partial loss-of-function or, in some reports, weakly dominant-negative on DNA binding, but there is no established gain-of-function class in the germline deficiency syndrome (contrast with somatic *GATA2* zinc-finger mutations reported in a minority of AML, which is a distinct oncogenic context, not germline deficiency).

**Population frequency:** Pathogenic *GATA2* variants are absent from gnomAD — consistent with high penetrance for severe, reproductively/medically consequential disease and largely de novo/small-pedigree transmission rather than population-level carrier frequency.

**Somatic (acquired) lesions on the germline background — the genetic path to MDS/AML:**
- Monosomy 7: 70–80% of pediatric GATA2-MDS; 20–40% of adult cases; in the original NIH cohort 16% had monosomy 7 and 24% trisomy 8 at any point, rising with disease evolution.
- der(1;7) unbalanced translocation.
- Somatic driver mutations: *ASXL1*, *STAG2*, *SETBP1*, *RUNX1* (STAG2 and trisomy 8 frequency increase with age).
- Clinical decision rule with direct diagnostic utility: **"up to 72% of adolescents with an MDS diagnosis and monosomy 7 carry germline GATA2 pathogenic variants"** (PDQ NBK606140) — monosomy-7 pediatric MDS should trigger germline *GATA2* testing.

**Distinguish from somatic 3q26/MECOM AML (see §2):** In sporadic inv(3)/t(3;3) AML, a *cis* enhancer-hijacking event silences *GATA2* on one allele while activating *MECOM* (*EVI1*) — mechanistically convergent on GATA2 haploinsufficiency but a **different disease with a different genetic architecture** (somatic structural rearrangement, no germline predisposition, distinct prognosis) and should not be curated under the germline GATA2 deficiency entry.

**Epigenetics:** A 2024 preprint/2025 published mechanistic study (PMID:38887897, "GATA2 heterozygosity causes an epigenetic feedback mechanism resulting in myeloid and erythroid dysplasia") proposes that GATA2 haploinsufficiency triggers a self-reinforcing epigenetic state (histone trimethylation changes reported in pediatric MDS marrow, PMC10705137) that entrenches dysplastic differentiation independent of additional mutation — relevant to modeling a `biological_scale: MOLECULAR` epigenetic node upstream of the cellular dysplasia node.

**Chromosomal abnormalities:** Not a primary chromosomal disorder; the relevant chromosomal abnormalities (monosomy 7, trisomy 8, der(1;7)) are all **acquired somatic events** in evolving marrow, not constitutional karyotype anomalies.

---

## 5. Environmental Information

GATA2 deficiency has no established environmental, dietary, or lifestyle causal factor — this is a purely monogenic host-susceptibility disorder. The "environmental" dimension of the disease is instead about **which pathogens the immunodeficiency renders the host susceptible to**, i.e., infectious triggers acting on a genetically primed innate/adaptive immune defect rather than independent causal exposures:

- **Nontuberculous mycobacteria** (*M. avium* complex predominantly, also *M. kansasii* — PMC6489290 case report) — the defining infection of "MonoMAC."
- **Human papillomavirus** — extensive cutaneous and anogenital disease, with malignant transformation risk (35% HPV-positive tumors).
- **Epstein-Barr virus** — EBV-driven lymphoproliferative disease and reported Hodgkin lymphoma (PMC12719254, case report of siblings).
- **Herpesviruses** (HSV, VZV) and disseminated fungal pathogens (*Histoplasma capsulatum* specifically implicated given the monocyte/macrophage defect).

No occupational, toxin, radiation, or dietary exposure is reported as a disease modifier in the identified literature; this section should largely be left unpopulated in a KB entry beyond the infectious-trigger framing above (which functionally belongs with the phenotype/pathophysiology sections as infection-driven complications of the immunodeficiency, not `environmental[]` causal exposures in the dismech schema sense).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous germline *GATA2* pathogenic variant (coding loss-of-function, ZF2 missense, or enhancer disruption) **leads to** ~50% reduction in functional GATA2 transcription-factor dosage in hematopoietic stem and progenitor cells (HSPCs) — GATA2 haploinsufficiency.
2. Reduced GATA2 dosage **disrupts** the GATA2–FLI1–TAL1/SCL recursive regulatory triad and downstream target activation (e.g., *HOXB4*), which normally governs HSC specification, quiescence, and self-renewal — this **results in** impaired HSC homeostasis: aged/stressed Gata2-haploinsufficient HSCs show reduced self-renewal capacity and a myeloid-biased, proliferative shift rather than maintained quiescence (Blood Advances 2021, PMID pending verification; Gata2 haploinsufficiency mouse studies).
3. Loss of the stem-cell "gatekeeper" function **leads to** a preleukemic state: single-cell transcriptomic studies of patient HSPCs (Blood Advances, "Sequencing of RNA in single cells...") show dysregulated apoptosis/cell-cycle/quiescence genes, increased erythroid/megakaryocytic priming, and decreased lymphoid priming — an early, cell-intrinsic bias toward the myeloid-dysplastic phenotype **before** any acquired somatic mutation.
4. Concurrently, GATA2 haploinsufficiency in **non-stem lineages results in** disproportionate, near-complete loss of monocytes, B-cell precursors, NK cells, and circulating/tissue dendritic cells, with relative sparing of T cells — this is a lineage-selective, dosage-sensitive effect rather than pan-hematopoietic failure, consistent with GATA2's role in "activating pro-fate targets... in granulocyte-macrophage progenitors and... repressing alternative-fate genes... in dendritic-cell progenitors."
5. The monocyte/dendritic-cell/NK deficiency **leads to** the clinical immunodeficiency phenotype: susceptibility to nontuberculous mycobacteria and *Histoplasma* (intramacrophagic pathogens, reflecting monocyte/macrophage dysfunction), HPV (reflecting NK/DC-mediated antiviral surveillance loss), and EBV/herpesvirus disease.
6. In the lung, insufficient monocyte-derived alveolar macrophage reconstitution **results in** defective pulmonary surfactant clearance, manifesting as pulmonary alveolar proteinosis and diffusion/ventilatory defects — mechanistically analogous to (but genetically distinct from) CSF2RA-related hereditary PAP, since here the defect is upstream monocyte/macrophage supply rather than GM-CSF receptor signaling itself.
7. Independently, in lymphatic endothelial cells, GATA2 haploinsufficiency **disrupts** direct transcriptional activation of *PROX1* and *FOXC2* (GATA2 binds regulatory elements in the *PROX1* promoter) and of the GATA2 target *miR-126*, which is required for VE-cadherin/claudin-5 junctional integrity — this **leads to** dysmorphic, incompetent lymphatic and lymphovenous valves, producing the lymphedema phenotype in a subset (more penetrant with null variants) (PMC6857586, "GATA2 controls lymphatic endothelial cell junctional integrity and lymphovenous valve morphogenesis through miR-126"; Blood 2012;119(5):1283, original description of lymphedema-MDS GATA2 link).
8. Over years, the haploinsufficient, epigenetically primed marrow **acquires** somatic second hits — most consequentially monosomy 7, but also trisomy 8, der(1;7), and mutations in *ASXL1*/*STAG2*/*SETBP1*/*RUNX1* — which **result in** clonal evolution to myelodysplastic syndrome and, in a subset, transformation to AML or CMML. This step is the somatic-mutation-driven branch and is the appropriate place for a `conforms_to` link to a myeloid-malignancy/clonal-evolution module rather than modeling AML as germline-caused per se.
9. Branch: in a minority, chronic marrow failure and dysplasia proceed to **bone marrow failure** independent of overt leukemic transformation, distinguishable histologically from idiopathic aplastic anemia by hypocellularity with reticulin fibrosis and atypical megakaryocytes in 92% of marrows (Blood 2015;125(1):56, "GATA2 deficiency-associated bone marrow disorder differs from idiopathic aplastic anemia").

### Molecular pathways
GATA2 operates in a **recursively autoregulated triad with FLI1 and TAL1/SCL**, each binding the others' enhancers, at the apex of the HSC transcriptional network; it acts upstream of *RUNX1* via the +23 enhancer (GATA2/FLI1/SCL complex assembly) and directly transactivates *HOXB4*. GO terms: **GO:0030099** (myeloid cell differentiation), **GO:0002520** (immune system development), **GO:0060716** (labyrinthine layer blood vessel development – lymphatic analog), **GO:0001945** (lymph vessel development).

### Cellular processes and cell types
Affected cell types (CL terms): hematopoietic stem cell (**CL:0000037**), common myeloid progenitor, monocyte (**CL:0000576**), classical/plasmacytoid dendritic cell (**CL:0000451**/**CL:0000784**), natural killer cell (**CL:0000623**), B lymphocyte precursor (**CL:0000816**), alveolar macrophage (**CL:0000583**), lymphatic endothelial cell (**CL:0002138**).

### Protein dysfunction
Predominantly **loss-of-function** at the protein level (reduced/absent functional protein from the mutant allele, or reduced transcription from a disrupted enhancer) rather than protein misfolding/aggregation. ZF2 missense variants impair sequence-specific DNA binding at GATA motifs without necessarily eliminating protein expression.

### Advanced/omics findings (2023–2025)
- **Single-cell transcriptomics** of patient HSPCs shows constrained gene correlation networks and myeloid-biased priming preceding overt MDS (Blood Advances, cited above).
- A 2024/2025 **Gata2^R396Q/+ knock-in mouse** (Leukemia, 2024, "Modeling GATA2 deficiency in mice") recapitulates HSC functional decline, lineage-fate bias, and an accelerated-aging transcriptional signature in HSPCs, but — notably — **does not spontaneously develop marked immunodeficiency or MDS/AML**, indicating the germline lesion alone is necessary but not sufficient and that additional (likely somatic) drivers are required for full disease. This is directly relevant to a dismech `HUMAN_MODEL_MISMATCH` discussion: the mouse model recapitulates the preleukemic HSC phenotype (`RECAPITULATES`, `MODERATE` fidelity) but `FAILS_TO_RECAPITULATE` the leukemic/immunodeficiency endpoints.
- A 2025 CRISPR-engineered isogenic human HSPC model (*Leukemia*, "CRISPR-engineered human GATA2 deficiency model uncovers mitotic dysfunction and premature aging in HSPCs") shows mitotic dysfunction and premature cellular aging as a proximate mechanism linking haploinsufficiency to HSC exhaustion — an `IN_VITRO`-graded mechanistic link.
- A 2025 study (Blood Cancer Journal, "GATA2 mutated allele specific expression is associated with a hyporesponsive state of HSC") reports **allele-specific expression skewing** toward the mutant allele in some patients, correlating with an HSC hyporesponsive/exhausted state — a genotype-severity modifier worth flagging as a `mechanistic_hypotheses` candidate (status: EMERGING) rather than established.

---

## 7. Anatomical Structures Affected

- **Organ/system level:** Bone marrow/hematopoietic system (primary); immune system (monocyte/DC/NK/B compartments); lymphatic vasculature; lung (parenchyma/alveolar macrophage compartment); inner ear (cochlea, sensorineural); reproductive/urogenital system (miscarriage, urogenital malformation); thyroid (hypothyroidism); skin (warts, panniculitis); vascular system (venous thrombosis).
- **UBERON suggestions:** bone marrow (UBERON:0002371), lymphatic vessel (UBERON:0001473), lymphovenous valve region, lung alveolus (UBERON:0002299), cochlea (UBERON:0000132), thyroid gland (UBERON:0002046).
- **Tissue/cell level:** hematopoietic stem/progenitor compartment (bone marrow niche), lymphatic endothelium (valve-forming LECs specifically), alveolar macrophage/type II pneumocyte-adjacent monocyte-derived population, cochlear sensory epithelium (mechanism not detailed in identified literature — noted gap).
- **Subcellular:** GO Cellular Component — nucleus (site of GATA2 transcriptional activity, GO:0005634); mitochondria implicated in the "increased mitochondrial mass/activity" preleukemic transition described above.
- **Localization/laterality:** Lymphedema and hearing loss are typically **bilateral**; no lateralization pattern reported.

---

## 8. Temporal Development

- **Onset:** Constitutional features (congenital sensorineural deafness, lymphedema when present, urogenital anomalies) are present from birth/early childhood but often recognized only retrospectively after a hematologic/infectious diagnosis. Symptomatic hematologic/immunologic disease has a **median clinical onset ~18–20 years**, with a bimodal split: pediatric-onset myeloid neoplasm (median age ~12) skews toward monosomy-7-driven, more aggressive MDS, while adult-onset disease (median age ~35) has a broader genetic and clinical spectrum.
- **Progression:** Chronic, generally **progressive** — cytopenias evolve toward dysplasia, then MDS, with a subset transforming to AML/CMML. Course is highly variable in tempo, including intrafamilial variability among carriers of an identical variant; some remain lifelong asymptomatic (partial/incomplete penetrance).
- **Disease stages:** Refractory cytopenia of childhood (RCC) → MDS with excess blasts → AML, tracked with standard pediatric/adult MDS staging (WHO/EWOG-MDS criteria) rather than a GATA2-specific staging system; monosomy-7 status is the dominant prognostic stratifier at each stage.
- **Remission/critical periods:** No spontaneous remission pattern reported for the hematologic component; HSCT is the only means of durable remission/cure (see §12). The "critical period" for intervention is framed clinically as **before irreversible organ damage** (established pulmonary fibrosis/PAP, advanced MDS/monosomy 7) — i.e., earlier HSCT in patients with RCC and normal karyotype yields markedly better outcomes than delayed transplant after monosomy-7 evolution.

---

## 9. Inheritance and Population

- **Epidemiology:** GATA2 deficiency accounts for **~7% of pediatric MDS and ~0.5% of adult MDS** (PDQ NBK606140) — making it one of the most common single-gene predispositions to pediatric MDS specifically, though the disorder overall remains ultra-rare in the general population (no pathogenic alleles present in gnomAD).
- **Inheritance pattern:** Autosomal dominant, de novo in roughly half of probands, otherwise inherited from an affected (or occasionally minimally symptomatic) parent.
- **Penetrance:** Estimated **>80% by age 60** in aggregate cohorts (some series cite ~90%); notably **incomplete and age-dependent** — a meaningful fraction of adult carriers remain hematologically/immunologically asymptomatic well into adulthood, which is directly relevant to genetic-counseling framing for asymptomatic relatives identified by cascade testing.
- **Expressivity:** Markedly variable, including within families sharing an identical variant — siblings/parent-child pairs with the same mutation can present decades apart or with different organ-system emphasis (hematologic vs. lymphatic vs. pulmonary).
- **Germline mosaicism / founder effects:** Not prominently reported as a recurring theme in the literature identified (most non-inherited cases are simple de novo, not parental mosaicism); no specific population founder variant has been described — pathogenic variants are private/family-specific, consistent with absence from gnomAD.
- **Consanguinity:** Not implicated (autosomal dominant, not recessive).
- **Population demographics:** No strong reported ethnic/geographic enrichment; case series are drawn from North American and European cohorts (NIH, French/Belgian) without a described differential prevalence by ancestry. Sex ratio is not reported as skewed; reproductive-age women show a notably high miscarriage rate (33%), relevant to counseling but not to differential incidence by sex.

---

## 10. Diagnostics

**Genetic testing:**
- First-line: targeted *GATA2* sequencing (including intron-4 enhancer region and copy-number analysis for whole-gene deletion) via NGS full-gene panels (e.g., Mayo Clinic Labs "GATAS" full gene analysis) — germline confirmation requires testing a non-hematopoietic tissue (cultured skin fibroblasts) when a hematologic malignancy is already present, to distinguish germline from somatic *GATA2* involvement, and parental testing to establish de novo status.
- **Diagnostic trigger rule:** monosomy 7 in a young MDS patient should prompt germline *GATA2* testing (up to 72% of monosomy-7 pediatric MDS carries a germline *GATA2* variant).
- Testing is also indicated for family members being evaluated as potential HSCT donors, given the risk of transplanting a mutation-carrying graft (see §12).

**Laboratory/immunophenotyping:** Peripheral blood flow cytometry showing profound monocytopenia, B-lymphopenia, NK-lymphopenia, and dendritic cell deficiency with relative T-cell preservation and inverted CD4:CD8 ratio is a strong clinical pattern-recognition diagnostic clue predating genetic confirmation.

**Bone marrow evaluation:** Hypocellular marrow with reticulin fibrosis and atypical megakaryocytes (92% of cases) distinguishes GATA2-associated marrow failure from idiopathic aplastic anemia; cytogenetics (monosomy 7, trisomy 8) and somatic NGS panel (*ASXL1*, *STAG2*, *SETBP1*, *RUNX1*) for clonal evolution monitoring.

**Imaging/functional testing:** Pulmonary function testing (DLCO, spirometry) for the diffusion/ventilatory defects seen in the majority of patients; high-resolution CT for PAP or interstitial lung disease (a 2025 case report series documents "early-onset and progressive interstitial lung disease" as a GATA2 presentation, PMC12012643).

**Differential diagnosis:** Other inherited bone marrow failure/MDS-predisposition syndromes should be excluded or co-considered — SAMD9/SAMD9L syndromes, *RUNX1* familial platelet disorder, *ANKRD26*-related thrombocytopenia, *DDX41*-related MDS/AML, *SRP72*-related BMF, telomere biology disorders (dyskeratosis congenita), Fanconi anemia, and *ELANE*-related severe congenital neutropenia — each has a distinct genetic/phenotypic signature but overlapping marrow-failure presentation.

**Screening (established carriers):** Periodic CBC/immune-status monitoring; **yearly bone marrow evaluation with cytogenetics and somatic variant testing**; HPV-related cancer screening (cervical/anal); avoidance of G-CSF (theoretical clonal-evolution risk).

---

## 11. Outcome/Prognosis

**Malignancy risk:** 75–80% lifetime risk of developing myeloid malignancy among symptomatic carriers; "80% of patients aged 40 having developed MDS/AML" in some cohort framings. MDS is the first hematologic diagnosis in 75% of malignancy cases, with AML developing in a further ~9–14% and CMML in ~8%.

**Survival without treatment:** Not separately quantified as an untreated natural-history survival curve in the identified literature (nearly all symptomatic patients proceed to HSCT); mortality risk is driven by both infectious complications (disseminated NTM, invasive fungal disease) pre-transplant and by malignant transformation.

**Prognostic stratifiers:** Karyotype at the time of transplant is the dominant prognostic factor — refractory cytopenia of childhood (RCC) with a **normal karyotype** carries excellent HSCT outcomes (DFS ~90%), while RCC with **monosomy 7** is markedly worse (DFS ~67%); advanced MDS/AML at transplant and monosomy 7 both independently associate with worse post-HSCT outcome.

**HSCT outcomes (pooled/registry data):**
- EWOG-MDS pediatric registry (n=65 with germline GATA2 mutation): 5-year overall survival 75%, disease-free survival 70%; treatment failure attributable roughly equally to non-relapse mortality and relapse (Bone Marrow Transplantation 2021, PMC8563415).
- French/Belgian adult+pediatric series (n=67): long-term outcome analysis (British Journal of Haematology, cited above) — outcomes vary by disease stage at transplant, consistent with the karyotype-stratified pattern above.
- Reported adult overall survival figures by indication in the PDQ synthesis: 54% (MDS/AML or immunodeficiency, general), 66% (children, MDS, monosomy 7), 88% (children, RCC, normal karyotype), 86% (young adults, immunodeficiency-predominant indication).

**Complications:** Chronic infection burden pre-transplant (NTM, fungal, HPV-driven neoplasia), post-HSCT graft-versus-host disease (not reported as increased over baseline in this population), and the specific transplant-related hazard of **donor-derived MDS/AML when a related donor is an unrecognized mutation carrier** — underscoring the requirement for donor germline testing in familial transplant.

**Recovery potential:** Successful HSCT reverses the cellular immunodeficiency phenotype (monocyte/B/NK reconstitution), resolves infection susceptibility, and eliminates the ongoing risk of leukemic transformation from the native marrow — i.e., HSCT is curative for the hematologic/immunologic disease, though it does not reverse pre-existing structural organ damage (established lymphedema, pulmonary fibrosis) accrued before transplant, which is the rationale for early referral.

---

## 12. Treatment

**Curative therapy:** **Allogeneic hematopoietic stem cell transplantation (HSCT)** is the only curative treatment and is recommended for essentially all symptomatic patients — nearly all individuals with GATA2-related MDS eventually undergo HSCT. NCIT: **NCIT:C15431** (Hematopoietic Cell Transplantation) as `therapeutic_modality: CELL_THERAPY`.
- **Timing:** should occur **before irreversible organ damage** — i.e., before advanced MDS/monosomy-7 evolution and before established pulmonary or lymphatic structural damage, given the strong karyotype-at-transplant prognostic effect described in §11.
- **Indications:** recurrent infections, transfusion dependency, or clonal evolution to myeloid malignancy.
- **Conditioning:** individually tailored; both myeloablative and reduced-intensity/nonmyeloablative regimens have been reported (a busulfan-based regimen is specifically described in one series, PMID:29412158); a 2025 registered trial (NCT05907746) is evaluating **briquilimab (anti-CD117 antibody)–based conditioning** as a lower-toxicity alternative — relevant as an emerging/experimental regimen.
- **Donor selection caveat:** mandatory germline *GATA2* testing of related potential donors, given reported donor-derived MDS/AML when an unrecognized carrier relative was used as donor.

**Pharmacotherapy / supportive care:**
- **Prophylactic azithromycin** (empiric, for NTM prevention) — CHEBI azithromycin; `treatment_term`: NCIT:C15986 Pharmacotherapy, `therapeutic_agent`: azithromycin.
- Antifungal prophylaxis in patients with severe cellular immunodeficiency.
- **Interferon-alfa** has in vitro/small-series support for improving NK-cell cytotoxicity, considered for refractory HPV or herpesvirus disease.
- **HPV vaccination** is empirically recommended early, given the marked HPV susceptibility (NCIT:C15346 Vaccination).
- **G-CSF is avoided** due to theoretical clonal-evolution risk in a genetically primed marrow.

**Experimental/advanced therapeutics (2025):**
- **CRISPR-Cas9 allele-specific gene correction** in autologous HSPCs using rAAV6-mediated homology-directed repair has been reported as a proof-of-concept therapeutic strategy (*Molecular Therapy*, 2025, PMID:40739756) — positions autologous gene-corrected HSCT as a prospective alternative to allogeneic transplant, avoiding GVHD/donor-search barriers; still preclinical/early-phase, not standard of care.
- Briquilimab-conditioned HSCT trial (NCT05907746), ongoing.

**No consensus clinical practice guideline yet exists** for GATA2 deficiency management — surveillance and treatment intensity remain individually tailored, per the 2023 Blood review and the PMC10000430 clinical-spectrum review.

---

## 13. Prevention

- **Primary prevention:** Not applicable to the germline lesion itself (no modifiable risk factor); HPV vaccination functions as primary prevention against the downstream HPV-driven malignancy risk specifically.
- **Secondary prevention/screening:** Structured surveillance in known carriers — periodic CBC/immune monitoring, annual bone marrow evaluation with cytogenetics/NGS for clonal evolution, HPV-related cancer screening (cervical/anal cytology) — functions as early detection of transformation to enable earlier, better-outcome HSCT.
- **Genetic counseling:** Autosomal dominant inheritance with incomplete, age-dependent penetrance and highly variable expressivity should be explicitly communicated to families — an asymptomatic parent may still be a carrier, and cascade testing of first-degree relatives (including potential HSCT donors) is clinically actionable. No formal prenatal/preimplantation genetic testing protocol specific to *GATA2* was identified in the literature searched, though the general NGS-based testing infrastructure (used for other monogenic PGT indications) is technically applicable; this should be flagged as an inferred extrapolation, not a documented GATA2-specific practice.
- **Prophylaxis:** Azithromycin (NTM) and antifungal prophylaxis in immunodeficient carriers function as tertiary/complication prevention rather than disease prevention per se.
- **Public health:** No population screening program exists (ultra-rare, gnomAD-absent alleles); this is managed entirely through clinical/familial ascertainment, not newborn or population screening.

---

## 14. Other Species / Natural Disease

**No naturally occurring GATA2-deficiency-like disease has been identified in this search in companion animals, livestock, or wildlife** (no OMIA entry or veterinary case series located) — this section should record an explicit "not found" rather than a fabricated cross-species claim. This is consistent with the pattern that most engineered animal work on *GATA2* is laboratory-model-driven (mouse, zebrafish) rather than a naturally arising veterinary phenocopy.

**Orthology:** *Gata2* is highly conserved; mouse ortholog Gata2 (MGI:95662), zebrafish has two paralogs **gata2a** and **gata2b** (from a teleost genome duplication) with partially divergent functions (see §15).

---

## 15. Model Organisms

- **Mouse — full knockout:** *Gata2*-null mice are **embryonic lethal at E10.5** due to failure of definitive hematopoiesis, establishing GATA2 as essential (not merely modulatory) for HSC generation — this is a full-null lethality that cannot model the human heterozygous-viable disease directly.
- **Mouse — heterozygous/haploinsufficient models:** *Gata2^+/−* and conditional (*Vav-Cre;Gata2^fl/+*) mice are viable and recapitulate **HSC functional decline under proliferative/aging stress** — reduced self-renewal, myeloid bias, and (in a 2025 Blood Advances study) leukemia arising specifically in the context of bone marrow failure with somatic aberrations, increased Myc-target expression, and genomic instability (PMID:40138552) — a `RECAPITULATES`/`MODERATE`-to-`HIGH` fidelity model for the preleukemic HSC phenotype specifically.
- **Mouse — Gata2^R396Q/+ knock-in (patient-hotspot variant):** recapitulates aberrant lineage-fate decisions and an accelerated-HSC-aging transcriptional signature but **does not spontaneously develop marked immunodeficiency or MDS/AML** — explicitly noted by the authors as requiring "additional drivers" for full disease (*Leukemia*, 2024). This is a clean `HUMAN_MODEL_MISMATCH` candidate: model recapitulates the HSC-intrinsic lesion but fails to recapitulate the clinical leukemic/immunodeficient endpoint, implying non-cell-intrinsic or additional-somatic-hit requirements not yet captured by the germline mutation alone.
- **+9.5 enhancer mouse models:** Deletion/mutation of the conserved *Gata2* +9.5 kb enhancer disrupts adult HSC self-renewal and T-cell differentiation, modeling the human noncoding-enhancer-variant patient subset specifically (as opposed to coding variants).
- **Zebrafish:** Two paralogs, *gata2a* and *gata2b*; *gata2b* is specifically required for hematopoietic stem/progenitor cell emergence from hemogenic endothelium. Complete loss of *gata2b* is **nonlethal** (unlike mouse full knockout) and produces **neutropenia**, making zebrafish a genetically tractable system for adult/definitive hematopoiesis phenotyping that mouse full-knockout lethality precludes. A dedicated zebrafish **MonoMAC model** (bioRxiv, "A zebrafish model for MonoMAC syndrome") identifies an earlier developmental role for *gata2* in hemogenic-endothelium programming than previously appreciated in mammalian systems — a fidelity caveat, since this developmental-window emphasis may not map directly onto human postnatal-onset disease.
- **Human iPSC/CRISPR-engineered isogenic HSPC models (2025):** Allele-specific CRISPR-Cas9 correction and CRISPR-engineered heterozygous-knockout human HSPC models directly recapitulate mitotic dysfunction and premature cellular aging (*Leukemia*, 2025) — the highest-fidelity in vitro human model currently reported, though still IN_VITRO rather than whole-organism.

**Limitations across models:** No model to date spontaneously reproduces the full human triad of (1) selective monocyte/DC/NK/B lymphoid deficiency, (2) lymphatic valve/lymphedema phenotype, and (3) progression to overt MDS/AML from a single germline lesion without additional engineered somatic hits — each model system captures a subset (HSC-intrinsic aging/exhaustion in mouse/human HSPC models; hemogenic-endothelium/HSPC-emergence biology in zebrafish; lymphatic valve morphogenesis in Gata2-conditional lymphatic-endothelial-specific mouse deletion) rather than the integrated clinical syndrome.

---

## Summary of Suggested Ontology Bindings

| Category | Suggested terms |
|---|---|
| MONDO | MONDO:0013607 (GATA2 deficiency) |
| Genes | hgnc:4173 (GATA2) |
| Key HP terms | HP:0001099 Monocytopenia; HP:0010976 B lymphocytopenia; HP:0002863 Myelodysplasia; HP:0004808 Acute myeloid leukemia; HP:0006517 Pulmonary alveolar proteinosis; HP:0001004 Lymphedema; HP:0000407 Sensorineural hearing loss; HP:0200043 Verrucae; HP:0002960 Recurrent viral infections; HP:0005268 Recurrent miscarriage; HP:0012286 Panniculitis; HP:0004936 Venous thrombosis |
| GO (biological process) | GO:0030099 myeloid cell differentiation; GO:0001945 lymph vessel development; GO:0002520 immune system development |
| CL (cell types) | CL:0000037 HSC; CL:0000576 monocyte; CL:0000451/CL:0000784 dendritic cell; CL:0000623 NK cell; CL:0000816 B lymphoblast; CL:0000583 alveolar macrophage; CL:0002138 lymphatic endothelial cell |
| UBERON | UBERON:0002371 bone marrow; UBERON:0001473 lymphatic vessel; UBERON:0002299 lung alveolus; UBERON:0000132 cochlea |
| Treatment NCIT | NCIT:C15431 Hematopoietic Cell Transplantation; NCIT:C15986 Pharmacotherapy; NCIT:C15346 Vaccination |
| Therapeutic agents (CHEBI) | azithromycin |

---

## Key Sources

- Spinner MA, et al. "GATA2 deficiency: a protean disorder of hematopoiesis, lymphatics, and immunity." *Blood.* 2014;123(6):809–821. PMID:24227816.
- Calvo KR, Hickstein DD. "The spectrum of GATA2 deficiency syndrome." *Blood.* 2023;141(13):1524–1532. PMID:36455197.
- Homan CC, et al. "GATA2 deficiency syndrome: A decade of discovery." *Hum Mutat.* 2021. PMID:34387894.
- GATA2 Deficiency Syndrome (PDQ®) — NCI/PDQ Cancer Information Summaries, NCBI Bookshelf NBK606140.
- "GATA2 deficiency-associated bone marrow disorder differs from idiopathic aplastic anemia." *Blood.* 2015;125(1):56.
- "Loss-of-function germline GATA2 mutations in patients with MDS/AML or MonoMAC syndrome and primary lymphedema..." *Blood.* 2012;119(5):1283.
- Hematopoietic stem cell transplantation in children and adolescents with GATA2-related MDS (EWOG-MDS registry). *Bone Marrow Transplant.* 2021. PMC8563415.
- "GATA2 controls lymphatic endothelial cell junctional integrity and lymphovenous valve morphogenesis through miR-126." PMC6857586.
- Atypical 3q26/MECOM rearrangements genocopy inv(3)/t(3;3) in AML. *Blood.* 2020;136(2):224.
- "Modeling GATA2 deficiency in mice: the R396Q mutation disrupts normal hematopoiesis." *Leukemia.* 2024.
- "CRISPR-engineered human GATA2 deficiency model uncovers mitotic dysfunction and premature aging in HSPCs." *Leukemia.* 2025.
- "Treatment of GATA2 deficiency by allele-specific CRISPR-Cas9-directed gene correction in hematopoietic stem cells." *Molecular Therapy.* 2025. PMID:40739756.
- "Hematological phenotypes in GATA2 deficiency syndrome arise from aging, maladaptation to proliferation, and somatic events." *Blood Advances.* 2025. PMID:40138552.
- "GATA2 mutated allele specific expression is associated with a hyporesponsive state of HSC in GATA2 deficiency syndrome." *Blood Cancer J.* 2025.
- OMIM #614172 (Immunodeficiency 21/MonoMAC), #614038 (Emberger syndrome), #614286 (MDS predisposition), *137295 (GATA2).
- Orphanet ORPHA:228423; MONDO:0013607.

**Note on verification status:** Several PMIDs above were confirmed directly from PubMed search-result metadata; article content for OMIM entries and some full-text sources could not be directly fetched (403/404 responses) and their content here is reconstructed from search-result snippets — treat OMIM clinical-synopsis details as leads requiring direct OMIM confirmation before use in a KB `evidence` snippet, per dismech's exact-quote requirement.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032223` (1 mention) - the report calls it "CMML term if bound; else NCIT"; HP calls it **Blood group**
- `HP:0032101` (1 mention) - the report calls it "Recurrent atypical mycobacterial infections, if available"; HP calls it **Unusual infection**
- `HP:0002090` (1 mention) - the report calls it "recurrent fungal infection group"; HP calls it **Pneumonia**
- `HP:0012125` (1 mention) - the report calls it "HPV-related neoplasia; or map via NCIT"; HP calls it **Prostate cancer**
- `HP:0005506` (1 mention) - the report calls it "bone marrow hypocellularity"; HP calls it **Chronic myelogenous leukemia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0000132` (2 mentions) - UBERON does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0013607` (3 mentions) - the report calls it "GATA2 deficiency"; MONDO calls it **monocytopenia with susceptibility to infections**, and lists "immunodeficiency 21" among its other names
- `UBERON:0002371` (2 mentions) - the report calls it "UBERON suggestions:** bone marrow"; UBERON calls it **bone marrow**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.