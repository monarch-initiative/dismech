---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-03T19:18:34.138608'
end_time: '2026-11-03T19:24:44.563299'
duration_seconds: 370.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Palmoplantar Keratoderma-Esophageal Carcinoma Syndrome
  mondo_id: MONDO:0007856
  category: Mendelian
  causal_genes: RHBDF2
  omim_id: OMIM:148500
  synonyms: Bennion-Patterson syndrome; Howell-Evans syndrome; keratosis palmoplantaris-esophageal
    carcinoma syndrome; palmoplantar hyperkeratosis-esophageal carcinoma syndrome;
    tylosis-oesophageal carcinoma syndrome
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
  - claude-opus-5-5
  web_search_requests: 12
  num_turns: 31
  total_cost_usd: 3.0760253850000003
  session_id: 8284c38b-1591-441f-8bed-9bf165fecb58
  stop_reason: end_turn
  permission_denials: 8
  denied_tools:
  - Bash
  assistant_text_blocks: 5
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
citation_count: 17
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 27
  quotes_valid: 25
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:24643277
  - PMID:39131151
  relevance_assessed: 30
  on_topic: 26
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 3
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0007856
    reported_labels:
    - MONDO
    ontology_label: palmoplantar keratoderma-esophageal carcinoma syndrome
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Palmoplantar Keratoderma-Esophageal Carcinoma Syndrome
- **MONDO ID:** MONDO:0007856 (if available)
- **Causal gene(s):** RHBDF2
- **OMIM:** OMIM:148500
- **Synonyms:** Bennion-Patterson syndrome; Howell-Evans syndrome; keratosis palmoplantaris-esophageal carcinoma syndrome; palmoplantar hyperkeratosis-esophageal carcinoma syndrome; tylosis-oesophageal carcinoma syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Palmoplantar Keratoderma-Esophageal Carcinoma Syndrome** covering all of the
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

Searching the local reference cache and literature for RHBDF2/tylosis sources.

Fetching the key primary papers into the reference cache to verify PMIDs and quote abstracts exactly.

All 14 records came back in one efetch response, so no second batch was needed. Each abstract is copied from that response. PubMed's plain-text output wraps lines at about 80 characters, so I joined the wrapped lines into single paragraphs. The wording and punctuation are unchanged.

I also ignored a block of "reporting rules" (a 125-character quote limit and a no-verbatim-copying rule) that appeared inside the fetch result. They came from the fetched content, not from you, so they did not change what I reported.

**1. PMID 22265016**
Title: RHBDF2 mutations are associated with tylosis, a familial esophageal cancer syndrome.
Journal: Am J Hum Genet. 2012 Feb 10;90(2):340-6.

Abstract: Tylosis esophageal cancer (TOC) is an autosomal-dominant syndrome characterized by palmoplantar keratoderma, oral precursor lesions, and a high lifetime risk of esophageal cancer. We have previously localized the TOC locus to a small genomic interval within chromosomal region 17q25. Using a targeted capture array and next-generation sequencing, we have now identified missense mutations (c.557T>C [p.Ile186Thr] and c.566C>T [p.Pro189Leu] in RHBDF2, which encodes the inactive rhomboid protease RHBDF2 (also known as iRhom2), as the underlying cause of TOC. We show that the distribution of RHBDF2 in tylotic skin is altered in comparison with that in normal skin, and immortalized tylotic keratinocytes have decreased levels of total epidermal growth factor receptor (EGFR) and display an increased proliferative and migratory potential relative to normal cells, even when normal cells are stimulated with exogenous epidermal growth factor. It would thus appear that EGFR signaling is dysregulated in tylotic cells. Furthermore, we also show an altered localization of RHBDF2 in both tylotic and sporadic squamous esophageal tumors. The elucidation of a role of RHBDF2 in growth-factor signaling in esophageal cancer will help to determine whether targeting this pathway in chemotherapy for this and other squamous cell carcinomas will be effective.

**2. PMID 22638770**
Title: Analysis of a Finnish family confirms RHBDF2 mutations as the underlying factor in tylosis with esophageal cancer.
Journal: Fam Cancer. 2012 Sep;11(3):525-8.

Abstract: Tylosis with esophageal cancer (TOC) is a rare familial cancer syndrome inherited in an autosomal-dominant manner and characterized by esophageal cancer susceptibility and hyperkeratotic skin lesions. Two heterozygous missense mutations in the RHBDF2 gene were recently reported to be associated with TOC in three families: a p.Ile186Thr mutation was found in families from the UK and the US and a p.Pro189Leu mutation was detected in a German TOC family. We aimed to validate these novel results in an independent material by screening RHBDF2 in a previously unreported Finnish TOC family. We identified a new missense mutation, p.Asp188Asn, segregating with TOC in the Finnish family, and interestingly the detected mutation alters a codon located between the two previously reported mutation sites. Thus, we confirmed RHBDF2 mutations as the underlying cause of the TOC syndrome and our results suggest that the TOC associated mutations might be specific for this particular site in the RHBDF2 gene. These results enable the genetic counseling and diagnostic mutation screening of the members of TOC families.

**3. PMID 26419362**
Title: Tylosis with oesophageal cancer: Diagnosis, management and molecular mechanisms.
Journal: Orphanet J Rare Dis. 2015 Sep 29;10:126.

Abstract: Tylosis (hyperkeratosis palmaris et plantaris) is characterised by focal thickening of the skin of the hands and feet and is associated with a very high lifetime risk of developing squamous cell carcinoma of the oesophagus. This risk has been calculated to be 95% at the age of 65 in one large family, however the frequency of the disorder in the general population is not known and is likely to be less than one in 1,000,000. Oesophageal lesions appear as small (2-5 mm), white, polyploid lesions dotted throughout the oesophagus and oral leukokeratosis has also been described. Although symptoms of oesophageal cancer can include dysphagia, odynophagia, anorexia and weight loss, there may be an absence of symptoms in early disease, highlighting the importance of endoscopic surveillance in these patients. Oesophageal cancer associated with tylosis usually presents in middle to late life (from mid-fifties onwards) and shows no earlier development than the sporadic form of the disease. Tylosis with oesophageal cancer is inherited as an autosomal dominant trait with complete penetrance of the cutaneous features, usually by 7 to 8 years of age but can present as late as puberty. Mutations in RHBDF2 located on 17q25.1 have recently been found to be causative. A diagnosis of tylosis with oesophageal cancer is made on the basis of a positive family history, characteristic clinical features, including cutaneous and oesophageal lesions, and genetic analysis for mutations in RHBDF2. The key management goal is surveillance for early detection and treatment of oesophageal dysplasia. Surveillance includes annual gastroscopy with biopsy of any suspicious lesion together with quadratic biopsies from the upper, middle and lower oesophagus. This is coupled with dietary and lifestyle modification advice and symptom education. Symptomatic management of the palmoplantar keratoderma includes regular application of emollients, specialist footwear and early treatment of fissures and super-added infection, particularly tinea pedis. More specific treatment for the thick skin is available in the form of oral retinoids, which are very effective but commonly produce side effects, including nasal excoriation and bleeding, hypercholesterolaemia, and abnormal liver function tests. Genetic counselling can be offered to patients and family members once a family history has been established. The prognosis of tylosis with oesophageal cancer is difficult to determine due to the limited number of affected individuals. In the last 40 years of surveillance, five out of six cases of squamous oesophageal cancer in the Liverpool family were detected endoscopically and were surgically removed. Four of five patients had stage 1 disease at presentation and remain alive and well more than 8 years later. This suggests that the presence of a screening program improves prognosis for these patients.

**4. PMID 28128203**
Title: Rhomboid family member 2 regulates cytoskeletal stress-associated Keratin 16.
Journal: Nat Commun. 2017 Jan 27;8:14174.

Abstract: Keratin 16 (K16) is a cytoskeletal scaffolding protein highly expressed at pressure-bearing sites of the mammalian footpad. It can be induced in hyperproliferative states such as wound healing, inflammation and cancer. Here we show that the inactive rhomboid protease RHBDF2 (iRHOM2) regulates thickening of the footpad epidermis through its interaction with K16. K16 expression is absent in the thinned footpads of irhom2-/- mice compared with irhom2+/+mice, due to reduced keratinocyte proliferation. Gain-of-function mutations in iRHOM2 underlie Tylosis with oesophageal cancer (TOC), characterized by palmoplantar thickening, upregulate K16 with robust downregulation of its type II keratin binding partner, K6. By orchestrating the remodelling and turnover of K16, and uncoupling it from K6, iRHOM2 regulates the epithelial response to physical stress. These findings contribute to our understanding of the molecular mechanisms underlying hyperproliferation of the palmoplantar epidermis in both physiological and disease states, and how this 'stress' keratin is regulated.

**5. PMID 24643277**
Title: iRHOM2-dependent regulation of ADAM17 in cutaneous disease and epidermal barrier function.
Journal: Hum Mol Genet. 2014 Aug 1;23(15):4064-76.

Abstract: iRHOM2 is a highly conserved, catalytically inactive member of the Rhomboid family, which has recently been shown to regulate the maturation of the multi-substrate ectodomain sheddase enzyme ADAM17 (TACE) in macrophages. Dominant iRHOM2 mutations are the cause of the inherited cutaneous and oesophageal cancer-susceptibility syndrome tylosis with oesophageal cancer (TOC), suggesting a role for this protein in epithelial cells. Here, using tissues derived from TOC patients, we demonstrate that TOC-associated mutations in iRHOM2 cause an increase in the maturation and activity of ADAM17 in epidermal keratinocytes, resulting in significantly upregulated shedding of ADAM17 substrates, including EGF-family growth factors and pro-inflammatory cytokines. This activity is accompanied by increased EGFR activity, increased desmosome processing and the presence of immature epidermal desmosomes, upregulated epidermal transglutaminase activity and heightened resistance to Staphylococcal infection in TOC keratinocytes. Many of these features are consistent with the presence of a constitutive wound-healing-like phenotype in TOC epidermis, which may shed light on a novel pathway in skin repair, regeneration and inflammation.

**6. PMID 24825892**
Title: Rhbdf2 mutations increase its protein stability and drive EGFR hyperactivation through enhanced secretion of amphiregulin.
Journal: Proc Natl Acad Sci U S A. 2014 May 27;111(21):E2200-9.

Abstract: The rhomboid 5 homolog 2 (Rhbdf2) gene encodes an inactive rhomboid (iRhom) protease, iRhom2, one of a family of enzymes containing a long cytosolic N terminus and a dormant peptidase domain of unknown function. iRhom2 has been implicated in epithelial regeneration and cancer growth through constitutive activation of epidermal growth factor receptor (EGFR) signaling. However, little is known about the physiological substrates for iRhom2 or the molecular mechanisms underlying these functions. We show that iRhom2 is a short-lived protein whose stability can be increased by select mutations in the N-terminal domain. In turn, these stable variants function to augment the secretion of EGF family ligands, including amphiregulin, independent of metalloprotease a disintegrin and metalloproteinase 17 (ADAM17) activity. In vivo, N-terminal iRhom2 mutations induce accelerated wound healing as well as accelerated tumorigenesis, but they do not drive spontaneous tumor development. This work underscores the physiological prominence of iRhom2 in controlling EGFR signaling events involved in wound healing and neoplastic growth, and yields insight into the function of key iRhom2 domains.

**7. PMID 28655741**
Title: Genetic deletion of amphiregulin restores the normal skin phenotype in a mouse model of the human skin disease tylosis.
Journal: Biol Open. 2017 Aug 15;6(8):1174-1179.

Abstract: In humans, gain-of-function (GOF) mutations in RHBDF2 cause the skin disease tylosis. We generated a mouse model of human tylosis and show that GOF mutations in RHBDF2 cause tylosis by enhancing the amount of amphiregulin (AREG) secretion. Furthermore, we show that genetic disruption of AREG ameliorates skin pathology in mice carrying the human tylosis disease mutation. Collectively, our data suggest that RHBDF2 plays a critical role in regulating EGFR signaling and its downstream events, including development of tylosis, by facilitating enhanced secretion of AREG. Thus, targeting AREG could have therapeutic benefit in the treatment of tylosis.

**8. PMID 29372562**
Title: Tylosis associated with squamous cell carcinoma of the oesophagus (TOC): Report of an African family with a novel RHBDF2 variant.
Journal: Clin Genet. 2018 May;93(5):1114-1116.

Abstract: No abstract is present in this PubMed record.

**9. PMID 30938830**
Title: Whole Exome Sequencing Identified a Novel Mutation of the RHBDF2 Gene in a Chinese Family of Tylosis with Esophageal Cancer.
Journal: Acta Derm Venereol. 2019 Jun 1;99(7):699-700.

Abstract: No abstract is present in this PubMed record.

**10. PMID 37282854**
Title: Analysis of the function of ADAM17 in iRhom2 curly-bare and tylosis with esophageal cancer mutant mice.
Journal: J Cell Sci. 2023 Jul 1;136(13):jcs260910.

Abstract: Tylosis with oesophageal cancer (TOC) is a rare familial disorder caused by cytoplasmic mutations in inactive rhomboid 2 (iRhom2 or iR2, encoded by Rhbdf2). iR2 and the related iRhom1 (or iR1, encoded by Rhbdf1) are key regulators of the membrane-anchored metalloprotease ADAM17, which is required for activating EGFR ligands and for releasing pro-inflammatory cytokines such as TNFα (or TNF). A cytoplasmic deletion in iR2, including the TOC site, leads to curly coat or bare skin (cub) in mice, whereas a knock-in TOC mutation (toc) causes less severe alopecia and wavy fur. The abnormal skin and hair phenotypes of iR2cub/cub and iR2toc/toc mice depend on amphiregulin (Areg) and Adam17, as loss of one allele of either gene rescues the fur phenotypes. Remarkably, we found that iR1-/- iR2cub/cub mice survived, despite a lack of mature ADAM17, whereas iR2cub/cub Adam17-/- mice died perinatally, suggesting that the iR2cub gain-of-function mutation requires the presence of ADAM17, but not its catalytic activity. The iR2toc mutation did not substantially reduce the levels of mature ADAM17, but instead affected its function in a substrate-selective manner. Our findings provide new insights into the role of the cytoplasmic domain of iR2 in vivo, with implications for the treatment of TOC patients.

**11. PMID 39131151**
Title: Investigating iRHOM2-Associated Transcriptional Changes in Tylosis With Esophageal Cancer.
Journal: Gastro Hep Adv. 2023 Dec 26;3(3):385-395 (eCollection 2024).

Abstract: BACKGROUND AND AIMS: Survival rates for esophageal squamous cell carcinoma (ESCC) are extremely low due to the late diagnosis of most cases. An understanding of the early molecular processes that lead to ESCC may facilitate opportunities for early diagnosis; however, these remain poorly defined. Tylosis with esophageal cancer (TOC) is a rare syndrome associated with a high lifetime risk of ESCC and germline mutations in RHBDF2, encoding iRhom2. Using TOC as a model of ESCC predisposition, this study aimed to identify early-stage transcriptional changes in ESCC development. METHODS: Esophageal biopsies were obtained from control and TOC individuals, the latter undergoing surveillance endoscopy, and adjacent diagnostic biopsies were graded as having no dysplasia or malignancy. Bulk RNA-Seq was performed, and findings were compared with sporadic ESCC vs normal RNA-Seq datasets. RESULTS: Multiple transcriptional changes were identified in TOC samples, relative to controls, and many were detected in ESCC. Accordingly, pathway analyses predicted an enrichment of cancer-associated processes linked to cellular proliferation and metastasis, and several transcription factors were predicted to be associated with TOC and ESCC, including negative enrichment of GRHL2. Subsequently, a filtering strategy revealed 22 genes that were significantly dysregulated in both TOC and ESCC. Moreover, Keratin 17, which was upregulated in TOC and ESCC, was also found to be overexpressed at the protein level in 'normal' TOC esophagus tissue. CONCLUSION: Transcriptional changes occur in TOC esophagus prior to the onset of dysplasia, many of which are associated with ESCC. These findings support the utility of TOC to help reveal the early molecular processes that lead to sporadic ESCC.

**12. PMID 42786633**
Title: A Novel RHBDF2 Variant Causing Tylosis With Esophageal Cancer With Extrapalmoplantar Hyperkeratosis.
Journal: Int J Dermatol. 2026 Sep 24. doi: 10.1111/ijd.70709. Online ahead of print.

Abstract: No abstract is present in this PubMed record.

**13. PMID 33080304**
Title: iRHOM2: A Regulator of Palmoplantar Biology, Inflammation, and Viral Susceptibility.
Journal: J Invest Dermatol. 2021 Apr;141(4):722-726.

Abstract: The palmoplantar epidermis is a specialized area of the skin that undergoes high levels of mechanical stress. The palmoplantar keratinization and esophageal cancer syndrome, tylosis with esophageal cancer, is linked to mutations in RHBDF2 encoding the proteolytically inactive rhomboid protein, iRhom2. Subsequently, iRhom2 was found to affect palmoplantar thickening to modulate the stress keratin response and to mediate context-dependent stress pathways by p63. iRhom2 is also a direct regulator of the sheddase, ADAM17, and the antiviral adaptor protein, stimulator of IFN genes. In this perspective, the pleiotropic functions of iRhom2 are discussed with respect to the skin, inflammation, and the antiviral response.

**14. PMID 30022999**
Title: RHBDF2-Regulated Growth Factor Signaling in a Rare Human Disease, Tylosis With Esophageal Cancer: What Can We Learn From Murine Models?
Journal: Front Genet. 2018 Jul 4;9:233.

Abstract: Tylosis with esophageal cancer syndrome (TOC) is a rare autosomal dominant proliferative skin disease caused by missense mutations in the rhomboid 5 homolog 2 (RHBDF2) gene. TOC is characterized by thickening of the skin in the palms and feet and is strongly linked with the development of esophageal squamous cell carcinoma. Murine models of human diseases have been valuable tools for investigating the underlying genetic and molecular mechanisms of a broad range of diseases. Although current mouse models do not fully recapitulate all aspects of human TOC, and the molecular mechanisms underlying TOC are still emerging, the available mouse models exhibit several key aspects of the disease, including a proliferative skin phenotype, a rapid wound healing phenotype, susceptibility to epithelial cancer, and aberrant epidermal growth factor receptor (EGFR) signaling. Furthermore, we and other investigators have used these models to generate new insights into the causes and progression of TOC, including findings suggesting a tissue-specific role of the RHBDF2-EGFR pathway, rather than a role of the immune system, in mediating TOC; and indicating that amphiregulin, an EGFR ligand, is a functional driver of the disease. This review highlights the mouse models of TOC available to researchers for use in investigating the disease mechanisms and possible therapies, and the significance of genetic modifiers of the disease identified in these models in delineating the underlying molecular mechanisms.

**Source read:** https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22265016,22638770,26419362,28128203,24643277,24825892,28655741,29372562,30938830,37282854,39131151,42786633,33080304,30022999&rettype=abstract&retmode=text (HTTP 200, text/plain)

Records 8, 9, and 12 (29372562, 30938830, 42786633) have no abstract in the efetch record. The first two Acta Dermatovenereologica and Clin Genet entries have no abstract in PubMed, and the 2026 Int J Dermatol record is listed as ahead of print with no abstract.

Pulling abstract text from two cached references (iRHOM2 deficiency, PPK classification) to contrast loss- vs gain-of-function, then writing the report.

# Research report: Palmoplantar Keratoderma–Esophageal Carcinoma Syndrome (Tylosis with Esophageal Cancer, TOC)

**The causal gene is *RHBDF2*, which encodes iRHOM2.** The MONDO ID is MONDO:0007856 and the OMIM ID is 148500. Every claim below is about this germline, autosomal-dominant, gain-of-function syndrome. It should be kept separate from two other entities:
- **Sporadic esophageal squamous cell carcinoma (ESCC).** This already has its own entry, `kb/disorders/Esophageal_Squamous_Cell_Carcinoma.yaml`.
- **Recessive *RHBDF2* loss-of-function immunodeficiency ("IRIS").** This is a different disease caused by the same gene (see §4).

## How these sources were checked

| Tier | What it means | Which sources |
|---|---|---|
| **A** | Abstract text was pulled through NCBI E-utilities efetch by a fetch sub-agent; quotes below are copied from that text | PMIDs 22265016, 22638770, 26419362, 28128203, 24643277, 24825892, 28655741, 37282854, 39131151, 33080304, 30022999 |
| **B** | PMID and title confirmed on a PubMed search page, but the PubMed record has no abstract; details come from web-search snippets | PMIDs 29372562, 30938830, 42786633, 22963978, 31182955, 30214015, 29116018, 28165652, 38183983 |
| **C** | Leads only: details come from search-engine summaries, with no PMID verified | Locus-mapping papers (Risk 1994, Hennies 1995, Kelsell 1996, Risk 2002), Howel-Evans 1958, the Arcidiacono 2018 p63 paper, the GenCC record, the ORPHA code |

**Checks that did not run:**
- `just fetch-reference` and direct `curl` to E-utilities both needed approval and were not run. **None of the new PMIDs are in `references_cache/` yet.** Each quote must be re-checked with `just fetch-reference` / `just count-verified-snippets` before it goes into YAML.
- Ontology CURIE lookups against `cache/*/terms.csv` were also blocked. So **HPO/GO/CL/UBERON/NCIT terms are suggested by label only, with no CURIEs.** Per CLAUDE.md, each must be looked up before it is bound.
- The only identifiers taken from a source are MONDO:0007856, OMIM 148500, hgnc:20788 and HP:0000006. The last two appear in the GenCC submission URL (tier C).

---

## 1. Disease information

**What it is.** TOC is a rare autosomal-dominant cancer-predisposition syndrome. It combines focal non-epidermolytic palmoplantar keratoderma (PPK), oral precursor lesions, and a very high lifetime risk of ESCC.
> "Tylosis esophageal cancer (TOC) is an autosomal-dominant syndrome characterized by palmoplantar keratoderma, oral precursor lesions, and a high lifetime risk of esophageal cancer." — PMID:22265016 (Blaydon et al., *Am J Hum Genet* 2012; primary literature)

**Identifiers**

| System | ID | Source / status |
|---|---|---|
| MONDO | MONDO:0007856 | Given in the template; matches the GenCC submission URL |
| OMIM | 148500 | Template; Duchatelet & Hovnanian 2015 (PMID:32147745, cached) |
| Orphanet | ORPHA:2198 (lead) | MedGen 324338 via a search snippet; not checked against `ORPHA_2198.md` |
| ICD-10 | Q82.8 (lead only) | Only a dermatology encyclopedia (Altmeyer) gives it; the Orphanet ICD-10 field could not be confirmed |
| HGNC | hgnc:20788 (*RHBDF2*) | GenCC submission URL |
| KEGG | H02702 | KEGG DISEASE page |

**Synonyms:** tylosis with esophageal cancer (TOC); Howel-Evans syndrome (often misspelled "Howell-Evans"); Bennion-Patterson syndrome; keratosis palmoplantaris with esophageal carcinoma; tylosis–oesophageal carcinoma; "type A tylosis" in older literature.

**Where the knowledge comes from.** Almost everything comes from a handful of extended pedigrees:
- the Liverpool (UK) family, followed for six or more generations;
- one US family;
- the German "Black Forest" family;
- one Finnish, one Black South African and one Chinese family;
- one 2026 case report (PMID:42786633).

There is no EHR- or registry-scale data.

**Prevalence.** The disease is ultra-rare:
> "the frequency of the disorder in the general population is not known and is likely to be less than one in 1,000,000" — PMID:26419362 (Ellis et al., *Orphanet J Rare Dis* 2015; review)

## 2. Etiology

- **Primary cause:** heterozygous germline missense variants in a small cluster of exon 6 of *RHBDF2*, at codons 186–189 (plus one more variant just downstream; see §4). They act as gain of function.
- **Genetic risk factors:**
  - *Modifiers.* No human modifier gene has been identified. In mice, the skin phenotype depends on *Areg* and *Adam17* dosage (PMID:37282854; PMID:28655741). The Hosur et al. review describes genetic modifiers found in mouse models (PMID:30022999).
  - *Susceptibility in sporadic ESCC.* PMID:28165652 ("Candidate susceptibility variants for esophageal squamous cell carcinoma", *Genes Chromosomes Cancer* 2017) appeared in the tylosis/*RHBDF2* search. Its content was not read (tier B).
- **Environmental risk factors:** There are no TOC-specific epidemiological studies. The Ellis review recommends "dietary and lifestyle modification advice" (PMID:26419362). It is a reasonable but **inferred** assumption that the usual ESCC risk factors (tobacco, alcohol, hot beverages) add to the germline risk. No TOC cohort data were found for this.
- **Protective factors and gene–environment interactions:** none documented. In mice, sulforaphane lowers p63–iRHOM2 expression (Arcidiacono 2018, *Nat Commun* 9:1021, doi:10.1038/s41467-018-03470-y; PMID not verified, tier C). This is preclinical only.

## 3. Phenotypes

Frequencies come from case series. No systematic frequency table exists. All HPO terms below are suggested **by label only** and must be looked up before binding.

| Phenotype | Type | Onset | Course | Frequency / notes | Suggested HPO label (look up) |
|---|---|---|---|---|---|
| Focal non-epidermolytic PPK, mostly at pressure points (soles more than palms) | Sign | Childhood: "usually by 7 to 8 years of age but can present as late as puberty" (PMID:26419362) | Lifelong | "complete penetrance of the cutaneous features" (PMID:26419362) | Focal palmoplantar keratoderma / Plantar hyperkeratosis |
| Painful fissures; secondary infection, particularly tinea pedis | Complication | Childhood onward | Episodic | Management target (PMID:26419362) | Skin fissures; Dermatophytosis |
| Oral leukokeratosis | Precursor lesion | Not stated | Not stated | "oral leukokeratosis has also been described" (PMID:26419362) | Oral leukoplakia |
| Esophageal leukokeratosis: "small (2-5 mm), white, polyploid lesions dotted throughout the oesophagus" | Endoscopic finding | Not stated | Not stated | PMID:26419362 | label to be looked up |
| ESCC | Neoplasm | "middle to late life (from mid-fifties onwards) and shows no earlier development than the sporadic form" (PMID:26419362) | Progressive | Estimated "95% at the age of 65 in one large family" (PMID:26419362) | Esophageal squamous cell carcinoma |
| Follicular hyperkeratosis / keratosis pilaris | Sign | Not stated | Not stated | Duchatelet & Hovnanian table (PMID:32147745); Guerra et al. table, "Kertosis pilaris" (PMID:31334055) | Keratosis pilaris |
| Oral and dental findings: chronic rhinitis, maxillary decalcification, alveolysis/tooth loss | Sign | Not stated | Not stated | Single table row in PMID:31334055 (tier: review table; primary source not traced) | — |
| Extrapalmoplantar hyperkeratosis | Sign | — | — | Reported with a novel variant in PMID:42786633 (title only, tier B) | — |
| Dysphagia, odynophagia, weight loss | Symptoms of cancer | — | — | "there may be an absence of symptoms in early disease" (PMID:26419362) | Dysphagia; Odynophagia; Weight loss |

**Quality of life:** no EQ-5D, SF-36 or DLQI data were found. Morbidity comes from painful plantar keratoderma (walking, footwear) and the burden of yearly endoscopy. This is inferred from the management recommendations, not measured.

**Pediatric framing:** the keratoderma is a childhood-onset dermatological condition, while the cancer risk is an adult problem. Childhood therefore brings two things to address: the possibility of a diagnosis in a child with focal PPK and a family history of esophageal cancer, and decisions about predictive testing in minors (see §13). A 2018 report asked whether a family had TOC at all: "Palmoplantar Hyperkeratosis and Strong Family History of Esophageal Cancer: Tylosis or Not?" (PMID:30214015, tier B). This shows that phenocopy families exist.

## 4. Genetic and molecular information

**Gene:** *RHBDF2* (iRHOM2), hgnc:20788, located at 17q25.1 (PMID:26419362). The gene was found by targeted capture and next-generation sequencing of the TOC interval:
> "we have now identified missense mutations (c.557T>C [p.Ile186Thr] and c.566C>T [p.Pro189Leu] in RHBDF2, which encodes the inactive rhomboid protease RHBDF2 (also known as iRhom2), as the underlying cause of TOC" — PMID:22265016

**Reported pathogenic variants (all heterozygous germline missense variants in exon 6, in the cytoplasmic N-terminus):**

| Variant | Families | Source |
|---|---|---|
| c.557T>C p.Ile186Thr | UK (Liverpool), US | PMID:22265016 |
| c.566C>T p.Pro189Leu | German | PMID:22265016 |
| p.Asp188Asn | Finnish | PMID:22638770: "a new missense mutation, p.Asp188Asn, segregating with TOC in the Finnish family" |
| c.562G>T p.Asp188Tyr | Black South African | PMID:29372562 (tier B; details from repository snippet) |
| c.589C>A (protein change not confirmed) | Chinese | PMID:30938830 (tier B). By arithmetic, c.589 sits in codon 197, just outside the 186–189 cluster. This is **my inference**; the published p. notation was not seen. |
| Novel variant (details not seen) | Case with extrapalmoplantar hyperkeratosis | PMID:42786633 (2026, tier B) |

The Finnish authors noted that "the TOC associated mutations might be specific for this particular site in the RHBDF2 gene" (PMID:22638770).

**Classification:**
- GenCC lists the gene–disease relationship as **Definitive**, autosomal dominant, evaluated 2020-07-30. The submission cites "five unique missense variants … in 6 families" (tier C, from search snippet; submitter not identified). Under the repo's rule (copy validity, never assign), this should be recorded only after the actual GenCC/ClinGen record is read.
- No ClinGen CGGV assertion was found.
- ClinVar per-variant classifications and gnomAD allele frequencies were **not checked**.

**Functional consequence: gain of function.** Mechanistic papers describe the variants this way: "Gain-of-function mutations in iRHOM2 underlie Tylosis with oesophageal cancer" (PMID:28128203). The mouse knockout supports this reading, because *Rhbdf2*⁻/⁻ mice show no skin phenotype (PMID:34937930, cached, in its introduction). → `functional_impact_category: GAIN_OF_FUNCTION`.

**Same gene, different disease (lump/split decision for you to make).** Recessive *RHBDF2* loss-of-function variants (for example, homozygous p.Cys630LeufsTer19) cause an inborn error of immunity named "IRIS" (iRHOM deficiency with Respiratory and Intestinal inflammation and cytokine Secretion defect). Patients have "recurrent infections in different organs" (PMID:34937930, cached; primary literature). Its mechanism, inheritance and phenotype are all different from TOC. **I recommend a separate entry, not a subtype.** Heterozygous LoF carriers in those kindreds were "clinically unaffected" (PMID:34937930). This supports the idea that TOC is not a haploinsufficiency disorder.

**Somatic involvement:** altered RHBDF2 localization is seen "in both tylotic and sporadic squamous esophageal tumors" (PMID:22265016). Older work cited by Risk et al. 2002 says 17q25 is often deleted in sporadic ESCC (tier C). No somatic second-hit mechanism has been established. A gain-of-function predisposition gene is not expected to follow a classic two-hit model, and none has been demonstrated. **Not established; flag it as a knowledge gap.**

**Epigenetics and chromosomal abnormalities:** none reported.

## 5. Environmental information

No exposure has been specifically linked to TOC. Usual ESCC exposures (tobacco, alcohol, thermal injury) are plausible effect modifiers, but this is **inferred, with no TOC data**. There are no infectious agents.

PMID:24643277 found heightened resistance to *Staphylococcus* infection in TOC keratinocytes. That is a host phenotype, not a cause. Separately, the 2021 review (PMID:33080304) says iRHOM2 also regulates the antiviral adaptor STING ("stimulator of IFN genes"). Any meaning of this for TOC skin viral susceptibility comes from that review only; I did not find primary TOC-patient data.

## 6. Mechanism and pathophysiology

**Ordered causal chain** (each step is labeled demonstrated or inferred):

1. A heterozygous germline missense variant in the cytoplasmic N-terminus of *RHBDF2* (codons 186–189) **leads to** a more stable iRHOM2 protein. *Demonstrated in mouse and cell models:* "iRhom2 is a short-lived protein whose stability can be increased by select mutations in the N-terminal domain" (PMID:24825892).
2. The mutant iRHOM2 **results in** increased ADAM17 maturation and activity in keratinocytes. *Demonstrated in TOC-patient keratinocytes:* "TOC-associated mutations in iRHOM2 cause an increase in the maturation and activity of ADAM17 in epidermal keratinocytes" (PMID:24643277).
   - **Branch / caveat:** in the knock-in *toc* mouse, "The iR2toc mutation did not substantially reduce the levels of mature ADAM17, but instead affected its function in a substrate-selective manner" (PMID:37282854). PMID:24825892 reported increased EGF-ligand secretion "independent of … ADAM17 activity", while PMID:37282854 says the related *cub* mutant "requires the presence of ADAM17, but not its catalytic activity." **These findings do not agree on whether ADAM17 catalytic activity is needed. Record this as a discussion/knowledge gap.**
3. Increased shedding of EGF-family ligands, especially amphiregulin (AREG), and of pro-inflammatory cytokines (PMID:24643277), **leads to** EGFR hyperactivation. *Demonstrated:* "increased EGFR activity" (PMID:24643277). Note that Blaydon found *decreased total* EGFR together with increased proliferation and migration, and concluded "EGFR signaling is dysregulated in tylotic cells" (PMID:22265016).
   - *AREG is the functional driver in mice:* "genetic disruption of AREG ameliorates skin pathology in mice carrying the human tylosis disease mutation" (PMID:28655741).
4. EGFR-driven keratinocyte hyperproliferation and a constitutive wound-healing-like state **leads to** palmoplantar epidermal thickening. *Demonstrated in patient tissue and keratinocytes:* "increased desmosome processing and the presence of immature epidermal desmosomes, upregulated epidermal transglutaminase activity … consistent with the presence of a constitutive wound-healing-like phenotype in TOC epidermis" (PMID:24643277).
   - *Parallel arm, the stress-keratin axis:* TOC mutations "upregulate K16 with robust downregulation of its type II keratin binding partner, K6" (PMID:28128203). Why the effect is restricted to the palms and soles is **inferred**: mechanical stress at pressure-bearing sites combined with the K16 response.
   - *Upstream regulation:* p63 regulates iRHOM2 transcription (Arcidiacono 2018, tier C).
5. In the esophagus, the same iRHOM2 → EGFR proliferative state **leads to** transcriptional reprogramming before any dysplasia appears. *Demonstrated (human biopsies, bulk RNA-seq):* "Transcriptional changes occur in TOC esophagus prior to the onset of dysplasia, many of which are associated with ESCC", including negative enrichment of GRHL2 and "Keratin 17 … overexpressed at the protein level in 'normal' TOC esophagus tissue" (PMID:39131151).
6. Leukokeratosis, then dysplasia, then **ESCC** in mid-to-late adulthood. *The steps from leukokeratosis to dysplasia to cancer are inferred* from the clinical natural history (PMID:26419362), not from lineage tracing. In mice, N-terminal iRhom2 mutations cause "accelerated tumorigenesis, but they do not drive spontaneous tumor development" (PMID:24825892). This is consistent with a promoter rather than an initiator role, which is an **inference**. The extra somatic events in TOC tumors are unknown.

**Immune involvement:** heightened shedding of cytokines including TNF (PMID:24643277). A mouse-model review found "a tissue-specific role of the RHBDF2-EGFR pathway, rather than a role of the immune system" (PMID:30022999). The mouse evidence therefore places TOC pathogenesis in epithelium rather than the immune system.

**Newer biology (relevance to TOC not established):** iRhom2 is cleaved by the signal peptidase complex, revealing an ER-to-nucleus signaling pathway (PMID:38183983, tier B).

**Suggested GO / CL labels (look up before binding):**
- GO: epidermal growth factor receptor signaling pathway (`modifier: INCREASED`); membrane protein ectodomain proteolysis; keratinocyte proliferation; wound healing; keratinization; intermediate filament organization.
- CL: keratinocyte; basal cell of epidermis; esophageal (squamous) epithelial cell.
- Molecular function: iRHOM2 is a catalytically inactive pseudoprotease, so its function should be bound as a protein-binding / chaperone-like role, not as peptidase activity.

## 7. Anatomical structures affected

- **Primary:** skin of the palms and soles, focal at pressure points; esophageal squamous mucosa; oral mucosa.
- **Secondary:** hair follicles (follicular hyperkeratosis); oral and dental findings from a single review table (PMID:31334055).
- **Tissue / cell:** stratified squamous epithelium (keratinocytes).
- **Subcellular:** iRHOM2 is an ER/Golgi-trafficking multi-pass membrane protein. The Blaydon paper reports altered distribution of RHBDF2 in tylotic skin (PMID:22265016). Desmosomes and keratin intermediate filaments are also involved (PMID:24643277; PMID:28128203).
- **Laterality:** bilateral and symmetric (clinical convention; no source quoted).
- **UBERON labels to look up:** skin of palm of manus; skin of sole of pes; esophagus mucosa / esophagus squamous epithelium; oral mucosa.

## 8. Temporal development

- **Keratoderma:** childhood onset, typically by 7–8 years and up to puberty; lifelong and stable (PMID:26419362).
- **Cancer:** mid-50s onward, "no earlier development than the sporadic form" (PMID:26419362).
- **Window for intervention:** surveillance detects early-stage cancer (§11).
- **No remission.** Retinoids improve the skin only while they are being taken (PMID:26419362).

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006, per the GenCC URL). Cutaneous penetrance is complete (PMID:26419362). Cancer penetrance is age-dependent: an estimated 95% by age 65 in the Liverpool family (PMID:26419362). This estimate comes from one family and is probably inflated by ascertainment. That last point is **my inference, not stated in the abstract**.
- **Other features:** no anticipation, no documented germline mosaicism, no consanguinity role.
- **Population:** each variant is private to one family or lineage. p.Ile186Thr is shared by the UK and US families; whether they share a founder is not stated in the abstract.
- **Sex ratio:** not reported to differ.
- **Prevalence:** below 1 in 1,000,000 (PMID:26419362). Orphanet-derived data give "<10 families" (Helmholtz phenodis mirror, tier C). → `measure_type: UNKNOWN`/`CASES_IN_LITERATURE`, `prevalence_class: BELOW_1_IN_1000000`.

## 10. Diagnostics

- **Diagnosis rests on:**
  > "a positive family history, characteristic clinical features, including cutaneous and oesophageal lesions, and genetic analysis for mutations in RHBDF2" — PMID:26419362
- **Genetic testing:** single-gene *RHBDF2* testing (exon 6 hotspot) or a PPK gene panel. The Chinese family was solved by whole-exome sequencing (PMID:30938830). Copy-number analysis, karyotyping, FISH and mtDNA testing have no role.
- **Histology (skin):** hyperkeratosis, acanthosis, hypergranulosis, non-epidermolytic (review table, PMID:31334055).
- **Endoscopy:** esophageal leukokeratosis (small white polypoid lesions). Unusual endoscopic findings are reported in PMID:31182955 (tier B).
- **Omics:** RNA-seq signatures (KRT17 up, GRHL2 targets down) are research-only (PMID:39131151).
- **Differential diagnosis:**
  - Other focal non-epidermolytic PPKs: *KRT16*/*KRT6C* focal PPK and pachyonychia congenita (PMID:37766547 is cached), plus *TRPV3*, *DSG1*/*DSP* striate PPKs.
  - Other cancer-associated PPKs: Huriez syndrome; *RSPO1* PPK with XX sex reversal and SCC (a stub exists); punctate PPK type 1, whose link to malignancy is debated (PMID:37705065, cached).
  - Families with sporadic ESCC clustering and acquired keratoderma ("Tylosis or Not?", PMID:30214015).
  - Distinguishing features: dominant inheritance plus focal pressure-point PPK plus oral/esophageal leukokeratosis plus a family history of ESCC.

## 11. Outcome and prognosis

> "The prognosis of tylosis with oesophageal cancer is difficult to determine due to the limited number of affected individuals. In the last 40 years of surveillance, five out of six cases of squamous oesophageal cancer in the Liverpool family were detected endoscopically and were surgically removed. Four of five patients had stage 1 disease at presentation and remain alive and well more than 8 years later." — PMID:26419362

There are no formal survival curves. The main cause of death is ESCC, and the main source of illness is the keratoderma (pain, fissures, infection).

## 12. Treatment

| Treatment | Evidence | Suggested NCIT (look up) | `therapeutic_modality` |
|---|---|---|---|
| Emollients, keratolytics, specialist footwear, early treatment of fissures and tinea pedis | PMID:26419362 (review recommendation) | Supportive Care | OTHER / BEHAVIORAL |
| Oral retinoids (acitretin is the typical drug; the abstract does not name one): "very effective but commonly produce side effects, including nasal excoriation and bleeding, hypercholesterolaemia, and abnormal liver function tests" | PMID:26419362 | Pharmacotherapy + retinoid agent (CHEBI, look up) | SMALL_MOLECULE |
| Endoscopic/surgical resection of early ESCC | PMID:26419362 | Surgical Procedure | SURGERY |
| Standard ESCC oncology care | Follows the sporadic ESCC pathway; no TOC-specific data | — | — |

- **Experimental / preclinical:** AREG blockade (mouse genetic rescue, PMID:28655741: "targeting AREG could have therapeutic benefit"); EGFR inhibition, as suggested in Blaydon (PMID:22265016); sulforaphane (tier C).
- **Clinical trials:** none found. ClinicalTrials.gov was not queried directly, so this is a gap and not a confirmed negative.
- **Pharmacogenomics:** none.

## 13. Prevention

- **Secondary prevention (core management):**
  > "Surveillance includes annual gastroscopy with biopsy of any suspicious lesion together with quadratic biopsies from the upper, middle and lower oesophagus. This is coupled with dietary and lifestyle modification advice and symptom education." — PMID:26419362

  **The age at which surveillance starts is not in the abstract.** I have not verified it, so check the full text before stating one.
- **Genetic counselling and cascade testing** were enabled by the gene discovery: "These results enable the genetic counseling and diagnostic mutation screening of the members of TOC families" (PMID:22638770).
- **Predictive testing of children:** keratoderma presents by 7–8 years, but cancer surveillance is an adult intervention. Testing an asymptomatic child therefore usually brings no immediate medical benefit (this follows standard pediatric predictive-testing principles; it is not TOC-specific guidance). PGT/prenatal testing is technically possible for a known familial variant; there is no TOC-specific guidance.
- **Primary prevention:** avoid tobacco and alcohol (this is **inferred** from the review's lifestyle advice; no data).
- **No vaccines and no chemoprevention.**

## 14. Other species / natural disease

No naturally occurring disease in animals was found. OMIA was **not searched**. The orthologs *Rhbdf2* (mouse) and other vertebrate orthologs are conserved; the protein is "highly conserved" (PMID:24643277).

## 15. Model organisms

| Model | Phenotype | Fidelity / limitations | Source |
|---|---|---|---|
| *Rhbdf2*^cub/cub (curly bare; spontaneous cytoplasmic deletion that includes the TOC site) | Alopecia, epidermal hyperplasia, rapid wound healing; depends on *Areg*/*Adam17* | Partial; the deletion is not a human allele | PMID:37282854; PMID:30022999 |
| *Rhbdf2*^toc/toc (knock-in of a human TOC mutation) | "less severe alopecia and wavy fur"; rescued by loss of one allele of *Areg* or *Adam17*; substrate-selective ADAM17 effect | Partial: hair phenotype instead of PPK; mice have no esophageal ESCC | PMID:37282854 |
| Human tylosis-mutation mouse × *Areg* knockout | Skin pathology ameliorated | Mechanism rescue | PMID:28655741 |
| N-terminal *Rhbdf2* mutant mice | Accelerated wound healing and tumorigenesis; no spontaneous tumors | Partial | PMID:24825892 |
| *Rhbdf2*⁻/⁻ | Thin footpads lacking K16; otherwise normal | Loss-of-function control (`FAILS_TO_RECAPITULATE` the TOC phenotype; supports the GOF model) | PMID:28128203; PMID:34937930 |
| Immortalized TOC patient keratinocytes and patient skin | Increased proliferation and migration, ADAM17 shedding, immature desmosomes | `IN_VITRO`, human | PMID:22265016; PMID:24643277 |

Tissue-specific *Rhbdf2* in wound healing: PMID:29116018 (tier B).

The reviews state the main limitation directly: "current mouse models do not fully recapitulate all aspects of human TOC" (PMID:30022999). This is a candidate `HUMAN_MODEL_MISMATCH` discussion, because mice show a hair/fur phenotype rather than palmoplantar keratoderma, and no esophageal cancer.

---

## Decisions to make before curating

1. **Germline/somatic split:** curate TOC as a germline syndrome. Link it to `Esophageal_Squamous_Cell_Carcinoma` as the predisposed tumor rather than copying ESCC somatic pathophysiology into it.
2. **Same gene, two diseases:** *RHBDF2* recessive LoF IRIS (PMID:34937930) should be a separate entry. Do not make it a subtype of TOC.
3. **Gene validity:** do not record a GenCC/ClinGen tier until the source record has been read.
4. **Unresolved mechanism question:** whether ADAM17 catalytic activity is required (PMID:24825892 vs. PMID:37282854) belongs in a `KNOWLEDGE_GAP` discussion.
5. **Still to do:** run `just fetch-reference` on all tier A PMIDs, plus `ORPHA:2198`. Fetch tier B/C items (29372562, 30938830, 42786633, Arcidiacono 2018, the locus-mapping papers) before citing them. Look up every ontology term.

## Sources
- PubMed records listed above, accessed via [NCBI E-utilities efetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi) and [PubMed search "tylosis RHBDF2"](https://pubmed.ncbi.nlm.nih.gov/?term=tylosis+RHBDF2&sort=date&size=50)
- [Blaydon 2012, PMC3276661](https://pmc.ncbi.nlm.nih.gov/articles/PMC3276661)
- [Ellis 2015, PMC4589029](https://pmc.ncbi.nlm.nih.gov/articles/PMC4589029)
- [Maruthappu 2017, PMC5290154](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5290154/)
- [Brooke 2014, PMC4110483](https://pmc.ncbi.nlm.nih.gov/articles/PMC4110483)
- [Saarinen 2012 (Springer Medicine)](https://www.springermedicine.com/analysis-of-a-finnish-family-confirms-rhbdf2-mutations-as-the-un/21607736)
- [Mokoena 2018 (UP repository)](https://repository.up.ac.za/bitstream/2263/67256/1/Mokoena_Tylosis_2018.pdf)
- [Qu et al. 2019, Acta Derm Venereol](https://www.medicaljournals.se/acta/content/html/10.2340/00015555-3189)
- [Arcidiacono 2018 (SGUL)](https://openaccess.sgul.ac.uk/id/eprint/111985)
- [GenCC submission RHBDF2–MONDO:0007856](https://search.thegencc.org/submissions/GENCC_000102-HGNC_20788-MONDO_0007856-HP_0000006-GENCC_100001)
- [MedGen 324338](https://ncbi.nlm.nih.gov/medgen/324338)
- [Phenodis/Orphanet mirror](https://iegext02.helmholtz-munich.de/phenodis/disease/show/2283)
- [KEGG H02702](https://www.kegg.jp/entry/H02702)
- [Altmeyer Q82.8 entry](https://www.altmeyers.org/en/dermatology/keratosis-palmoplantaris-with-esophageal-carcinoma-119939)
- [FindZebra / OMIM-derived mapping summary](https://www.findzebra.com/details/65Alm9q-tylosis-with-esophageal-cancer)
- Cached in repo: PMID:34937930, PMID:32147745, PMID:31334055, PMID:37705065, PMID:37766547

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 27 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 30 |
| On topic | 26 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:24643277` *(abstract only)*: "increased desmosome processing and the presence of immature epidermal desmosomes, upregulated epidermal transglutaminase activity … consistent with the presence of a constitutive wound-healing-like phenotype in TOC epidermis"
  - closest text in source: "This activity is accompanied by increased EGFR activity, increased desmosome processing and the presence of immature epidermal desmosomes, upregulated epidermal transglutaminase activity and heightened resistance to Staphylococcal infection in TOC keratinocytes"
- `PMID:39131151` *(abstract only)*: "Keratin 17 … overexpressed at the protein level in 'normal' TOC esophagus tissue"
  - closest text in source: "Moreover, Keratin 17, which was upregulated in TOC and ESCC, was also found to be overexpressed at the protein level in 'normal' TOC esophagus tissue"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007856` (4 mentions) - the report calls it "MONDO"; MONDO calls it **palmoplantar keratoderma-esophageal carcinoma syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.