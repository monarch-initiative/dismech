---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-24T16:52:25.437876'
end_time: '2026-09-24T16:55:57.690787'
duration_seconds: 212.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dyskeratosis Congenita Autosomal Recessive 2
  mondo_id: MONDO:0013519
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
  web_search_requests: 8
  num_turns: 19
  total_cost_usd: 1.2078378
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 15
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 2
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMC:PMC11601709
  - PMC:PMC12151239
  relevance_assessed: 8
  on_topic: 6
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 35
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 10
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0007441
    reported_labels:
    - Reticulated/lacy skin hyperpigmentation
    ontology_label: Hyperpigmented/hypopigmented macules
  - term_id: HP:0012126
    reported_labels:
    - neoplasm of stomach, approximate
    ontology_label: Stomach cancer
  - term_id: UBERON:0002107
    reported_labels:
    - fibrosis/cirrhosis documented
    ontology_label: liver
  - term_id: UBERON:0002048
    reported_labels:
    - fibrosis reported generally for DC/TBD, not confirmed NHP2-specific here
    ontology_label: lung
  - term_id: UBERON:0000473
    reported_labels:
    - atrophy documented
    ontology_label: testis
  labels_variant: 6
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
- **Disease Name:** Dyskeratosis Congenita Autosomal Recessive 2
- **MONDO ID:** MONDO:0013519 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dyskeratosis Congenita Autosomal Recessive 2** covering all of the
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

# Dyskeratosis Congenita, Autosomal Recessive 2 (DKCB2) — Research Report

**MONDO:0013519** | **OMIM #613987** | **Gene: NHP2** (HGNC:14377, NCBI Gene 55651, chr5q35.3, NM_017838) | **Also known as:** NOLA2-related dyskeratosis congenita; DKCB2

Given your background, I'm skipping the general explanation of AR inheritance mechanics, penetrance/expressivity concepts, and mosaicism, and leading with the disease-specific claims and their sources. This is an ultra-rare entity — worldwide, published cases number in the single digits to low teens — so several template sections below have thin or no NHP2-specific literature; I've flagged those rather than padding with generic dyskeratosis congenita (DC) content that isn't gene-specific.

---

## 1. Disease Identity

DKCB2 is the biallelic-NHP2 subtype of dyskeratosis congenita / telomere biology disorder (DC/TBD). It was defined by Vulliamy et al. (PMID:18523010, *PNAS* 2008), who found compound-heterozygous or homozygous *NHP2* variants in 2 of 117 DC patients screened, both Turkish [OMIM #613987]. It sits within the broader DC/TBD nosology alongside the AD forms (*TERC*, *TERT*, *TINF2*, *RTEL1*, *PARN*, *ACD*) and the other AR/XL forms (*DKC1* X-linked; *NOP10*/DKCB1; *WRAP53*/TCAB1/DKCB3; biallelic *RTEL1*, *PARN*, *ACD*). GeneReviews treats DC and related TBDs as a single clinical spectrum ("Dyskeratosis Congenita and Related Telomere Biology Disorders," Savage & Niewisch, NBK22301) rather than splitting management guidance by causal gene — worth flagging for lump/split purposes: OMIM assigns *NHP2* its own phenotypic MIM (613987/DKCB2), but clinical practice does not distinguish it from other AR-TBD forms except by molecular diagnosis.

- **ICD-10:** Q82.8 (Other specified congenital malformations of skin) — not gene-specific; DC/TBD as a class has no dedicated ICD-10/11 code.
- **Orphanet:** ORPHA:1775 covers dyskeratosis congenita generically; I did not find an NHP2-specific ORPHA subtype code in this pass — worth verifying directly against Orphadata XML before binding `mappings.mondo_mappings`/ORPHA in a KB entry.
- **ClinGen gene-disease validity:** NHP2–dyskeratosis congenita is classified **Limited** by the ClinGen Syndromic Disorders GCEP, "at the higher end of the Limited classification point range, likely to change classification with one or two additional studies" (ClinGen Syndromic Disorders GCEP curation, cf. PMC11601709/PMC12151239, 2024). This is a materially weaker validity tier than *DKC1*, *TERT*, or *TINF2*, and reflects the very small published case count — worth surfacing explicitly if this goes into a KB entry rather than treating gene-disease validity as settled.

**Source basis:** the disease-level facts above come from a structured database (OMIM, ClinGen) plus the two primary case-series/functional papers below (PMID:18523010; the 2023 HMG functional paper) — I have not independently verified every detail against the primary PDFs (PNAS and PMC fetches were blocked by 403/CAPTCHA in this session; abstracts below are reconstructed from search-engine snippets, not read in full), so treat quoted fragments as leads to re-verify against the primary text before using them as curation snippets.

---

## 2. Etiology

**Causal factor:** Biallelic (homozygous or compound-heterozygous) loss-of-function or hypomorphic missense variants in *NHP2* (NOLA2). No environmental, infectious, or multifactorial contribution is described for this subtype — DC/TBD as a class is a monogenic telomere-maintenance disorder.

**Reported variants (all missense to date, consistent with an essential gene where complete loss is likely non-viable or embryonic-lethal, by analogy to the core-complex partner genes):**

| Variant | Zygosity | Source |
|---|---|---|
| p.Tyr139His (c.415T>C) | Homozygous, 22-y-old Turkish man | PMID:18523010; also OMIM #613987 |
| p.Val126Met (c.376G>A) | (second Turkish proband; ClinVar RCV000004502) | PMID:18523010 |
| p.Ala39Thr (c.115G>A) | Compound heterozygous | 2023 *Hum Mol Genet* functional paper (PMC10508036) |
| p.Thr44Met (c.131C>T) | Compound heterozygous (with A39T, above) | same |

**Functional mechanism of the variants:** V126M and Y139H "impaired association with NOP10, leading to major pre-RNP assembly defects with all H/ACA RNAs tested, including the H/ACA domain of hTR [TERC]" (search-derived summary of PMID:20008900, Trahan & Dragon, *Hum Mol Genet* 2010 — re-verify wording against primary text). A39T and T44M destabilize the NHP2 N-terminal domain via molecular-dynamics-demonstrated distortion of residues 33–41 (A39T) and residues 1–24 (T44M), driving proteasomal degradation of the mutant protein when competing with wild-type NHP2 for RNP incorporation, with consequent reduction in hTR levels and telomerase activity (2023 HMG paper, PMC10508036).

**Risk/protective/gene-environment factors:** No NHP2-specific modifier genes, environmental risk factors, or protective variants have been reported in the literature I could locate — this is a gap, not a documented absence, given how few cases exist to study. General TBD literature (not NHP2-specific) notes that even within families carrying an identical variant, disease severity varies considerably (per GeneReviews) — consistent with genetic-anticipation-type telomere-length inheritance effects seen across DC/TBD broadly, but this has not been specifically demonstrated for NHP2 pedigrees in the sources I found.

---

## 3. Phenotypes

The classic DC mucocutaneous triad plus multisystem stem-cell-exhaustion features, as reported for the ~4 published NHP2 patients (2 Vulliamy 2008; 1 index case in the 2023 HMG functional paper; a sibling pair in a 2025 case report, PMID:40352450, PMC12065628 — full text not retrievable in this session, only stub metadata confirmed).

| Phenotype | Suggested HP term | Notes |
|---|---|---|
| Nail dystrophy | HP:0008404 | Classic triad component |
| Reticulated/lacy skin hyperpigmentation | HP:0007441 | Classic triad component |
| Oral leukoplakia | HP:0002745 | Classic triad component |
| Progressive bone marrow failure / aplastic anemia | HP:0005528 | "Principal cause of mortality in DC patients" per GeneReviews (general DC/TBD claim) |
| Thrombocytopenia | HP:0001873 | Index Y139H patient |
| Myelodysplastic syndrome | HP:0002863 | 2023 HMG index case, age 38 |
| Premature graying of hair | HP:0002216 | GeneReviews general feature list |
| Testicular atrophy | HP:0000029 | Y139H patient (OMIM) |
| Growth delay | HP:0001510 | Y139H patient (OMIM: "growth ... retardation") |
| Intellectual disability | HP:0001249 | Y139H patient (OMIM: "mental retardation") |
| Hepatic fibrosis / cirrhosis | HP:0001394 | Y139H patient ("liver cirrhosis") |
| Intracranial calcification | HP:0002514 | Y139H patient |
| Recurrent/opportunistic infection | HP:0002719 | Y139H patient |
| Pulmonary fibrosis | HP:0002206 | General DC/TBD feature; not confirmed NHP2-specific in sources found |
| Gastric cancer | HP:0012126 (neoplasm of stomach, approximate) | 2023 HMG index case, age 38 |

**Frequencies:** with only ~4 published patients, no meaningful phenotype-frequency percentages can be derived for the NHP2 subtype specifically. The Y139H patient's phenotype (testicular atrophy, growth/intellectual impairment, intracranial calcification, opportunistic infection) is notably severe for an adult-diagnosed case (age 22) and approaches the Hoyeraal-Hreidarsson-syndrome end of the DC severity spectrum, though I did not find an explicit HH designation applied to this patient in the sources retrieved — flag rather than assert if curating.

**QoL data:** none specific to NHP2 located; general DC/TBD QoL literature was not pursued given the gene-level focus requested.

---

## 4. Genetic/Molecular Information

- **Gene:** NHP2 ribonucleoprotein (HGNC:14377; NCBI Gene 55651; chr5q35.3; aliases NOLA2, NHP2P, SPAG12, DKCB2).
- **Variant classification:** All reported variants are missense; ClinVar lists p.Val126Met (NM_017838.4:c.376G>A) as pathogenic for "Dyskeratosis congenita, autosomal recessive 2" (RCV000004502).
- **Functional impact category:** loss-of-function via protein destabilization/misfolding and impaired complex incorporation (not classic catalytic-site LOF) — `PARTIAL_LOSS_OF_FUNCTION` is likely the most accurate `FunctionalImpactEnum` value pending confirmation against the primary functional papers, since residual telomerase activity is reduced but not abolished in the biochemical assays described.
- **Population frequency:** no NHP2 pathogenic-variant carrier frequency or gnomAD allele-frequency data specific to these variants was retrieved in this pass — check gnomAD directly for p.Tyr139His/p.Val126Met/p.Ala39Thr/p.Thr44Met before citing a number.
- **Somatic vs. germline:** exclusively germline; DC/TBD is a constitutional disorder. (The secondary MDS/AML and squamous carcinomas that DC patients are predisposed to are separate somatic events arising in the germline-predisposed marrow/epithelium — keep these as distinct pathophysiology nodes/entries rather than folding them into the germline syndrome, consistent with design-decisions §3a.)
- **Epigenetics/structural variation:** none reported for this gene/subtype in the sources retrieved.

---

## 5. Environmental Information

No NHP2-specific environmental, lifestyle, or infectious contributory factors are reported. General DC/TBD clinical guidance (not NHP2-specific) advises avoiding additional telomere/marrow stressors (e.g., excess sun exposure given SCC risk, hepatotoxic exposures given fibrosis risk) but I did not find this stated as NHP2-specific literature — would need to be sourced from GeneReviews management sections rather than asserted as disease-specific etiology.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered), noting where each step is directly demonstrated vs. inferred:**

1. Biallelic *NHP2* missense variants (p.Tyr139His, p.Val126Met — PMID:18523010; p.Ala39Thr, p.Thr44Met — PMC10508036) destabilize the NHP2 protein or impair its N-terminal domain conformation. *Demonstrated* by molecular-dynamics simulation and cell-based degradation assays for A39T/T44M.
2. This **leads to** impaired NHP2–NOP10 association and reduced/defective incorporation of NHP2 into the core H/ACA ribonucleoprotein complex (dyskerin–NOP10–NHP2–GAR1), with mutant protein undergoing proteasome-dependent degradation when competing against wild-type. *Demonstrated* (PMID:20008900; PMC10508036).
3. This **results in** defective assembly of H/ACA snoRNPs generally and, specifically, of the H/ACA domain of TERC (the telomerase RNA component), which depends on this same core complex for stability. *Demonstrated* for V126M/Y139H (PMID:20008900).
4. This **leads to** reduced steady-state TERC (hTR) levels — "patients with NHP2 mutations, in common with patients bearing dyskerin and NOP10 mutations, had short telomeres and low TERC levels" (PMID:18523010, paraphrased from search snippet — re-verify exact wording against primary text before quoting as a KB snippet).
5. Reduced TERC availability **results in** diminished assembly and activity of the telomerase holoenzyme (telomerase reverse transcriptase + TERC + accessory H/ACA proteins). *Demonstrated* directly for A39T/T44M via reduced telomerase activity assays (PMC10508036).
6. Insufficient telomerase activity **leads to** progressive, division-coupled telomere shortening, most consequential in high-turnover stem/progenitor compartments (hematopoietic stem cells, epidermal/mucosal basal keratinocytes, germ cells, alveolar and hepatic progenitor populations). *Inferred by extension from the general DC/TBD mechanism* — telomere length was not independently measured in the NHP2 cohort beyond "short" per the cited source.
7. Critically short telomeres **trigger** a persistent DNA-damage response, replicative senescence, and apoptosis in affected stem/progenitor pools, causing tissue-specific stem-cell exhaustion. *Inferred, extrapolated from the general DC/TBD literature rather than NHP2-specific data.*
8. Stem-cell exhaustion **manifests as**: (a) hematopoietic stem cell attrition → progressive trilineage bone marrow failure (thrombocytopenia documented in the index case); (b) epithelial stem-cell attrition → nail dystrophy, mucosal leukoplakia, skin pigmentation changes; (c) hepatic/pulmonary progenitor attrition → organ fibrosis (liver cirrhosis documented in the Y139H patient); (d) germline stem-cell attrition → testicular atrophy (documented).
9. **Branch — malignant transformation (distinct somatic process, not part of the germline mechanism above):** chronic replicative stress and genomic instability in the exhausted, telomere-crisis-prone marrow and epithelium **predisposes to** acquisition of somatic driver mutations, manifesting as myelodysplastic syndrome (documented in the 2023 index case) and, by extension from general DC biology, squamous cell carcinoma and AML. This should be modeled as a separate somatic pathophysiology branch downstream of the germline telomere-maintenance defect, per the germline/somatic separation convention.

**Second, less-established mechanistic thread — ribosome biogenesis:** because NHP2/dyskerin/NOP10/GAR1 form the core machinery for essentially *all* box H/ACA snoRNPs (not only the telomerase-associated one), and box H/ACA snoRNPs guide pseudouridylation of ribosomal RNA, some literature frames DC as having a partial ribosomopathy component alongside the telomere defect. I did not find this explicitly demonstrated for the NHP2 subtype specifically in this pass (it is more thoroughly documented for *DKC1*-associated X-linked DC); flag as a plausible but unconfirmed-for-NHP2 mechanistic branch rather than asserting it.

**Suggested GO terms:** telomerase activity (GO:0003720), telomere maintenance via telomerase (GO:0007004), box H/ACA snoRNP assembly (GO:0031120), pseudouridine synthesis (GO:0001522), telomerase RNA stabilization (no precise GO term confirmed — verify via OAK before binding).

**Suggested cell types (CL):** hematopoietic stem cell (CL:0000037), epidermal keratinocyte (CL:0000312), basal cell of epidermis, hepatocyte/hepatic stellate cell (fibrosis), spermatogonial stem cell.

---

## 7. Anatomical Structures Affected

- **Primary organs:** bone marrow (UBERON:0002371), skin/nail unit (UBERON:0001003 epidermis; nail plate), oral mucosa (UBERON:0003729).
- **Secondary/complication organs:** liver (UBERON:0002107 — fibrosis/cirrhosis documented), lung (UBERON:0002048 — fibrosis reported generally for DC/TBD, not confirmed NHP2-specific here), testis (UBERON:0000473 — atrophy documented), CNS (intracranial calcification documented in one patient).
- **Body systems:** hematologic, integumentary, hepatic, reproductive (male), and — per general DC/TBD biology rather than NHP2-specific confirmation — respiratory and skeletal (osteoporosis).
- **Subcellular:** nucleolus (site of H/ACA snoRNP assembly), Cajal bodies (TCAB1/WRAP53-mediated telomerase trafficking — relevant to the pathway family though not NHP2 itself specifically), telomeres (chromosome ends).

---

## 8. Temporal Development

The Y139H patient presented at age 22 (Vulliamy 2008); the 2023 HMG index case presented in adulthood (age 38) with MDS and gastric cancer as the presenting/index features rather than classic pediatric mucocutaneous triad. This is notable: **unlike the more common AD (*TERT*, *TINF2*) and X-linked (*DKC1*) forms, which often present in childhood, the published NHP2 cases skew toward later-childhood/adult presentation**, though the n is far too small (~4 patients) to generalize a typical age-of-onset or progression pattern. No formal staging system exists for DC/TBD; general GeneReviews guidance frames it as a progressive, generally non-remitting stem-cell-exhaustion disorder with bone marrow failure as the dominant driver of mortality across the DC/TBD class as a whole.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (biallelic *NHP2* variants required); HP:0000007.
- **Prevalence:** DC/TBD overall is estimated at roughly 1:1,000,000; **NHP2 pathogenic variants account for less than 1% of all dyskeratosis congenita cases** (GeneReviews, NBK22301) — making DKCB2 one of the rarest molecularly defined DC subtypes. No NHP2-specific incidence/prevalence figure exists; `prevalence_class: ULTRA_RARE` / `NOT_YET_DOCUMENTED` with `measure_type: CASES_IN_LITERATURE` would be the honest framing for a KB entry given only ~4 published cases.
- **Population/ancestry:** the two founding cases were Turkish (Vulliamy 2008); no founder-effect or specific-population enrichment has been established from this small case count — a shared ancestry between the two original probands raises consanguinity as a plausible but unconfirmed factor (not stated explicitly as consanguineous in the retrieved abstract fragments — verify against full text).
- **Sex ratio, geographic distribution:** insufficient case count to characterize.
- **Penetrance/expressivity:** general DC/TBD literature (GeneReviews) states penetrance "varies considerably, even within families with identical variants" — this is a class-level statement, not one independently demonstrated for NHP2 pedigrees specifically in the sources found.

---

## 10. Diagnostics

- **Primary diagnostic test (class-level, per GeneReviews, applies to NHP2 as to other DC/TBD genes):** lymphocyte telomere length by flow-FISH, showing values below the 1st percentile for age, combined with either clinical diagnostic criteria or biallelic pathogenic *NHP2* variants on molecular testing.
- **Molecular testing:** multigene DC/TBD panel or exome sequencing; "sequence analysis has detected pathogenic variants in all studied NHP2 families" (GeneReviews) — i.e., no large structural variants have been reported for this gene in the DC context.
- **Laboratory:** low TERC levels have been demonstrated biochemically in NHP2 patients specifically (PMID:18523010), which is a distinguishing molecular signature shared with *DKC1*- and *NOP10*-associated disease (all three encode core H/ACA RNP components) but not with *TERT*/*TINF2*/*RTEL1*-associated disease (where TERC itself is not depleted).
- **Differential diagnosis:** the other 8+ molecularly defined DC/TBD genes; Fanconi anemia (bone marrow failure + some overlapping congenital features — distinguish via chromosome breakage/DEB testing and telomere length, which is normal in FA); Hoyeraal-Hreidarsson syndrome (severe end of the DC/TBD spectrum — the Y139H patient's phenotype approaches this).
- **Screening:** no population or newborn screening program exists for DC/TBD; family cascade testing is appropriate once a proband's biallelic *NHP2* variants are identified, given AR inheritance and the implied ~25% recurrence risk in future sibs of carrier parents.

---

## 11. Outcome/Prognosis

Insufficient NHP2-specific cohort data exists for survival statistics. Class-level DC/TBD data (GeneReviews) states bone marrow failure is the principal cause of mortality; solid-organ (pulmonary fibrosis, hepatic disease) and secondary-malignancy (MDS/AML, SCC) complications are the other major drivers of morbidity/mortality across DC/TBD broadly. Within the NHP2 case reports specifically: the 2023 index patient developed both MDS and gastric adenocarcinoma by age 38 — a data point consistent with, but not proof of, the general DC malignancy-predisposition pattern extending to this subtype.

---

## 12. Treatment

No NHP2-specific treatment trial or outcome data exists; management follows general DC/TBD guidance (GeneReviews):

- **Hematopoietic cell transplantation** (NCIT:C15431) — the only curative approach for bone marrow failure; DC/TBD patients require reduced-intensity/fludarabine-based conditioning given radiosensitivity and organ fragility (class-level guidance, not NHP2-specific confirmation found).
- **Androgens** (e.g., danazol, oxymetholone; NCIT:C15986 Pharmacotherapy + CHEBI therapeutic_agent) — used off-label to stimulate hematopoiesis when transplant is not immediately available/suitable, per class-level DC/TBD guidance.
- **Supportive/surveillance care:** per GeneReviews — annual CBC and marrow evaluation, monthly self skin/mucosal exams plus annual dermatology and otolaryngology exams (SCC surveillance), pulmonary function testing from ~age 8, semi-annual dental evaluation.
- **Genetic counseling** (NCIT:C15240) — appropriate given AR inheritance and availability of molecular carrier/prenatal testing once the familial variants are known.
- No gene therapy, RNA-based therapy, or targeted molecular therapy specific to NHP2/telomerase restoration has reached clinical trials for this subtype; I found no registered NCT trial specific to NHP2-DC in this pass (would need a direct ClinicalTrials.gov search restricted to "NHP2" or "dyskeratosis congenita" to confirm absence rather than asserting it from a general search).

---

## 13. Prevention

No primary prevention exists (germline monogenic disorder). Secondary prevention is carrier/prenatal testing and preimplantation genetic diagnosis once familial variants are identified, per standard AR-disorder genetic counseling practice — not NHP2-specific literature. Tertiary prevention is the surveillance program under Diagnostics/Treatment above (cancer screening, pulmonary monitoring) aimed at early detection of DC/TBD complications.

---

## 14. Other Species / Natural Disease

No naturally occurring NHP2-associated disease in non-human species was located in this search pass (no OMIA entry found for NHP2/DKCB2-equivalent veterinary disease). *NHP2* is broadly conserved (ortholog present across vertebrates given its essential role in H/ACA snoRNP biology and ribosome synthesis), but disease-causing biallelic variants have only been reported in humans.

---

## 15. Model Organisms

- **Mouse:** *Nhp2* (MGI:1098547), chromosome 11 (syntenic band 11B1.3), human ortholog confirmed. I did not find a published disease-modeling *Nhp2* knockout/knock-in mouse paper specific to DC phenotype recapitulation in this search pass — this is a notable gap relative to the *Terc−/−*, *Dkc1* hypomorphic, and *Tinf2* mouse models that are well-characterized in the DC/TBD literature. Given *Nhp2*'s essential role in ribosome biogenesis generally (not just telomerase), a complete knockout is plausibly embryonic lethal, which may explain why disease-modeling has favored patient-variant knock-in approaches or has simply not yet been published for this gene — this is my inference, not a sourced claim, and should be verified directly (e.g., via MGI phenotype records or IMPC) before use.
- **Cellular models:** patient-derived and engineered cell lines expressing mutant NHP2 (A39T, T44M) were used directly in the 2023 functional study (PMC10508036) to demonstrate reduced telomerase activity and hTR levels — this is the strongest "model system" evidence available for this subtype, though it is a cellular/in-vitro model rather than an organismal one, and fidelity to the whole-organism human phenotype (marrow failure, organ fibrosis) is not established by this data alone.

---

## Summary of Confidence and Gaps

This is a genuinely thin literature — roughly 4 published patients across 3 papers spanning 2008–2025, and a ClinGen validity classification of only **Limited**. The strongest, most directly sourced claims are the gene identity, the specific variants, and the H/ACA RNP-assembly/TERC-depletion mechanism (PMID:18523010; PMID:20008900; PMC10508036). The weakest are anything requiring cohort-level statistics (prevalence, penetrance, age-of-onset distribution, treatment response rates) and the model-organism section, where I found no NHP2-specific animal model. Several PubMed/PMC/PNAS full-text fetches were blocked (403/CAPTCHA) in this session, so quoted fragments above are reconstructed from search-engine result snippets rather than read directly from primary text — before using any of these as a KB `snippet:`, re-fetch the primary source (`just fetch-reference PMID:18523010` etc.) and re-verify the exact quoted substring.

**Sources consulted:**
- [OMIM #613987 — Dyskeratosis Congenita, Autosomal Recessive 2](https://omim.org/entry/613987)
- [OMIM *606470 — NHP2 Ribonucleoprotein](https://omim.org/entry/606470)
- [PubMed 18523010 — Vulliamy et al., "Mutations in the telomerase component NHP2 cause the premature ageing syndrome dyskeratosis congenita," PNAS 2008](https://pubmed.ncbi.nlm.nih.gov/18523010/)
- [PNAS full text (fetch blocked, HTTP 403)](https://www.pnas.org/doi/10.1073/pnas.0800042105)
- [PubMed 20008900 — Trahan & Dragon, "Effects of dyskeratosis congenita mutations in dyskerin, NHP2 and NOP10 on assembly of H/ACA pre-RNPs," Hum Mol Genet 2010](https://pubmed.ncbi.nlm.nih.gov/20008900/)
- [PMC10508036 — "Novel pathological variants of NHP2 affect N-terminal domain flexibility, protein stability, H/ACA RNP complex formation and telomerase activity," Hum Mol Genet 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10508036/)
- [PubMed 40352450 / PMC12065628 — "Siblings with a Homozygous Variant in the NHP2 Gene: A Case Report and Review of Literature," 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12065628/)
- [GeneReviews NBK22301 — Savage & Niewisch, "Dyskeratosis Congenita and Related Telomere Biology Disorders"](https://www.ncbi.nlm.nih.gov/sites/books/NBK22301/)
- [ClinGen — NHP2 curation results (MONDO:0013519)](https://search.clinicalgenome.org/kb/conditions/MONDO:0013519/by-gene)
- [ClinGen Syndromic Disorders GCEP — 111 gene-disease relationships (PMC11601709/PMC12151239, 2024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11601709/)
- [ClinVar RCV000004502 — NHP2 c.376G>A (p.Val126Met)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000004502.3/)
- [NIH GTR — Dyskeratosis congenita, autosomal recessive 2](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3151441/)
- [MGI — Nhp2 mouse gene detail (MGI:1098547)](https://www.informatics.jax.org/marker/MGI:1098547)
- [GeneCards — NHP2](https://www.genecards.org/card/NHP2)
- [Orphanet — Dyskeratosis congenita (ORPHA:1775)](https://www.orpha.net/en/disease/detail/1775?name=Dyskeratosis+congenita&mode=name)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC11601709` *(abstract only)*: "at the higher end of the Limited classification point range, likely to change classification with one or two additional studies"
  - closest text in source: "A full review of 111 GDRs for 100 genes followed, with 78 classified as Definitive, 9 as Strong, 15 as Moderate, and 9 as Limited highlighting where further data are needed"
- `PMC:PMC12151239` *(abstract only)*: "at the higher end of the Limited classification point range, likely to change classification with one or two additional studies"
  - closest text in source: "A full review of 111 GDRs for 100 genes followed, with 78 classified as Definitive, 9 as Strong, 15 as Moderate, and 9 as Limited, highlighting cases in which further data are needed"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 21 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0007441` (1 mention) - the report calls it "Reticulated/lacy skin hyperpigmentation"; HP calls it **Hyperpigmented/hypopigmented macules**
- `HP:0012126` (1 mention) - the report calls it "neoplasm of stomach, approximate"; HP calls it **Stomach cancer**
- `UBERON:0002107` (1 mention) - the report calls it "fibrosis/cirrhosis documented"; UBERON calls it **liver**
- `UBERON:0002048` (1 mention) - the report calls it "fibrosis reported generally for DC/TBD, not confirmed NHP2-specific here"; UBERON calls it **lung**
- `UBERON:0000473` (1 mention) - the report calls it "atrophy documented"; UBERON calls it **testis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0005528` (1 mention) - the report calls it "Progressive bone marrow failure / aplastic anemia"; HP calls it **Bone marrow hypocellularity**, and lists "Bone marrow failure" among its other names
- `HP:0002863` (1 mention) - the report calls it "Myelodysplastic syndrome"; HP calls it **Myelodysplasia**, and lists "Myelodysplastic syndrome" among its other names
- `HP:0001394` (1 mention) - the report calls it "Hepatic fibrosis / cirrhosis"; HP calls it **Cirrhosis**, and lists "Hepatic cirrhosis" among its other names
- `HP:0002514` (1 mention) - the report calls it "Intracranial calcification"; HP calls it **Cerebral calcification**
- `HP:0002719` (1 mention) - the report calls it "Recurrent/opportunistic infection"; HP calls it **Recurrent infections**
- `UBERON:0002371` (1 mention) - the report calls it "Primary organs:** bone marrow"; UBERON calls it **bone marrow**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:1098547` - called "Nhp2", "Mouse:** *Nhp2"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.