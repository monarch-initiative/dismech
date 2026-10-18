---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T15:43:36.121161'
end_time: '2026-09-23T15:51:23.709025'
duration_seconds: 467.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SUCLA2-Related Mitochondrial DNA Depletion Syndrome
  mondo_id: MONDO:0012791
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
  web_search_requests: 9
  num_turns: 27
  total_cost_usd: 1.7471592
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 3
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
citation_count: 39
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 14
  quotes_unsupported: 5
  unsupported_quote_references:
  - PMID:19666145
  - PMID:21295139
  - PMID:15877282
  - PMID:18392745
  - PMID:24659738
  relevance_assessed: 32
  on_topic: 26
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 26
  labels_matching: 17
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - Near-universal
    ontology_label: Global developmental delay
  - term_id: HP:0000407
    reported_labels:
    - Very common (a defining feature)
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0011968
    reported_labels:
    - Common
    ontology_label: Feeding difficulties
  - term_id: HP:0003202
    reported_labels:
    - Common
    ontology_label: Skeletal muscle atrophy
  - term_id: HP:0002490
    reported_labels:
    - basal ganglia signal abnormality context
    ontology_label: Increased CSF lactate
  - term_id: HP:0003348
    reported_labels:
    - Near-universal (defining biomarker)
    ontology_label: Hyperalaninemia
  - term_id: HP:0002151
    reported_labels:
    - Common but not obligate
    ontology_label: Increased circulating lactate concentration
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SUCLA2-Related Mitochondrial DNA Depletion Syndrome
- **MONDO ID:** MONDO:0012791 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SUCLA2-Related Mitochondrial DNA Depletion Syndrome** covering all of the
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

I'll research SUCLA2-Related Mitochondrial DNA Depletion Syndrome (MTDPS5, encephalomyopathic form with methylmalonic aciduria) and produce a comprehensive report. Let me start by loading web research tools and gathering primary literature.

I now have sufficient primary-literature coverage. Let me do one final round for the deoxynucleoside trial's SUCLA2-specific results and the recent NAD+/zebrafish mechanism paper full detail, then compose the report.

# Research Report: SUCLA2-Related Mitochondrial DNA Depletion Syndrome (MTDPS5, Encephalomyopathic Form with Methylmalonic Aciduria)

**Target identifiers:** MONDO:0012791 · OMIM #612073 (phenotype) / *603921 (gene) · ORPHA:1933 (shared with SUCLG1-MTDPS9) · Gene: SUCLA2, HGNC:11450, 13q14.2

---

## 1. Disease Information

**Overview.** SUCLA2-related mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (MTDPS5) is an autosomal recessive disorder caused by biallelic pathogenic variants in *SUCLA2*, encoding the β-subunit of the ADP-forming (A) isoform of succinyl-CoA synthetase/ligase (SUCL), a Krebs-cycle enzyme. Loss of SUCL function secondarily depletes mitochondrial DNA (mtDNA) copy number, producing a severe infantile encephalomyopathy. The disease-defining biochemical signature — described as "mildly elevated methylmalonic acid and C4-dicarboxylic carnitine concentrations in body fluids in association with variable lactic acidosis" (Carrozzo et al. 2007, *Brain*, [PMID:17301081](https://pubmed.ncbi.nlm.nih.gov/17301081/)) — distinguishes this entity from classic methylmalonic acidemias (MMUT, MMAA/B/etc.) despite the shared metabolite.

**Key identifiers:**
- OMIM phenotype #612073 "Mitochondrial DNA depletion syndrome 5 (encephalomyopathic type)"; gene OMIM *603921
- MONDO:0012791
- ORPHA:1933 (shared code covering both SUCLA2- and SUCLG1-caused encephalomyopathic MDS with methylmalonic aciduria; note the sibling entity **MTDPS9**, OMIM #245400, is the SUCLG1-specific form — see Differential Diagnosis)
- GeneReviews chapter: El-Hattab AW, Scaglia F, "SUCLA2-Related Mitochondrial DNA Depletion Syndrome, Encephalomyopathic Form with Methylmalonic Aciduria" ([PMID:20301762](https://pubmed.ncbi.nlm.nih.gov/20301762/), NBK6803)
- MeSH/synonyms: "SUCLA2 deficiency," "deafness-dystonia syndrome (SUCLA2-related)," "mild methylmalonic aciduria with Leigh-like encephalomyopathy"
- ICD-10-CM: no dedicated code; falls under E88.49 (other mitochondrial metabolic disorders)
- HGNC:11450; UniProt Q9P2R7; chromosome 13q14.2, ~60 kb, 13 exons, 463-aa protein

**Evidence provenance note.** Virtually all clinical/epidemiologic data below derive from aggregated case-series (largest: 71 patients across SUCLA2+SUCLG1, [PMID:26475597](https://pubmed.ncbi.nlm.nih.gov/26475597/)) rather than a prospective disease registry or large-scale EHR resource — this is a founder-population/ultra-rare disease literature, so denominators are small and ascertainment is clinic-based.

---

## 2. Etiology

**Causal factor:** Biallelic loss-of-function or hypomorphic variants in *SUCLA2* (13q14.2), autosomal recessive. First established by Elpeleg et al. 2005 (*Am J Hum Genet*, [PMID:15877282](https://pubmed.ncbi.nlm.nih.gov/15877282/)), who found "markedly decreased succinyl-CoA synthetase activity" in muscle mitochondria of two siblings with encephalomyopathy and mtDNA depletion, and proposed that "a defect in the last step of mitochondrial dNTP salvage is a novel cause of the mtDNA depletion syndrome." Confirmed independently and expanded the same year in two companion *Brain* papers: Ostergaard et al. ([PMID:17287286](https://pubmed.ncbi.nlm.nih.gov/17287286/), 12 Faroese/Scandinavian patients) and Carrozzo et al. ([PMID:17301081](https://pubmed.ncbi.nlm.nih.gov/17301081/), 14 patients/11 families, including non-Faroese Italian/other European ancestry).

**Genetic risk factors:**
- Homozygous or compound-heterozygous *SUCLA2* variants (missense, nonsense, splice-site, frameshift, and at least one intragenic deletion — [PMID:26409464](https://pubmed.ncbi.nlm.nih.gov/26409464/)).
- Founder mutation: a homozygous splice-site variant in the Faroe Islands population, carrier frequency 1:33, allele frequency 2%, disease incidence 1:1700 in that population — "a high incidence of 1 in 1700 in the Faroe Islands due to a founder effect" ([PMID:17287286](https://pubmed.ncbi.nlm.nih.gov/17287286/); consistent figures in [PMID:19666145](https://pubmed.ncbi.nlm.nih.gov/19666145/), 16 Faroese children with this homozygous splice-site allele).
- Recurrent non-Faroese alleles reported multiple times independently include p.Arg284Cys (≥4 patients of Italian/Caucasian ancestry per [PMID:28749033](https://pubmed.ncbi.nlm.nih.gov/28749033/)) and p.Arg407Trp/Leu at a mutational hotspot associated with a distinctly milder, non-progressive phenotype ([PMID:33231368](https://pubmed.ncbi.nlm.nih.gov/33231368/)).
- Compound heterozygosity with a contiguous 13q14 deletion spanning *SUCLA2* and *RB1* has produced combined mitochondrial encephalomyopathy plus retinoblastoma in two families ([PMID:24986829](https://pubmed.ncbi.nlm.nih.gov/24986829/)) — a mechanistically unrelated but genomically contiguous double diagnosis worth flagging for dismech's cancer-predisposition adjacency (13q14 deletion syndrome / RB1).
- One kindred with concurrent trisomy 21 and homozygous SUCLA2 p.Arg284Cys showed a more severe phenotype than either condition alone ([PMID:28749033](https://pubmed.ncbi.nlm.nih.gov/28749033/)) — reported as an interaction, single-family evidence.

**Environmental/modifying factors:** None established as disease-causing; this is a purely monogenic mitochondrial-maintenance disorder. Consanguinity is a recognized risk factor for homozygosity in non-founder populations (e.g., the consanguineous Iranian cousins in [PMID:23759946](https://pubmed.ncbi.nlm.nih.gov/23759946/); the consanguineous family in [PMID:27651038](https://pubmed.ncbi.nlm.nih.gov/27651038/)).

**Protective factors:** None specifically identified for disease risk. Therapeutically, succinate bypasses the enzymatic block in at least one case ("succinate supplementation circumvents the Krebs cycle block," [PMID:33231368](https://pubmed.ncbi.nlm.nih.gov/33231368/)) — see Treatment.

**Gene–environment interaction:** Not applicable in the classic sense; the closest analog is genetic background modifying severity via residual protein/enzyme activity (see Mechanism, genotype-phenotype correlation) rather than an exogenous exposure.

---

## 3. Phenotypes

The core clinical triad, stated repeatedly across the literature: **"early hypotonia, progressive dystonia and sensori-neural deafness"** ([PMID:19666145](https://pubmed.ncbi.nlm.nih.gov/19666145/)).

| Phenotype | Type | Onset/course | Frequency (qualitative) | Suggested HP term |
|---|---|---|---|---|
| Severe muscular hypotonia | Sign | Neonatal–early infancy; often progressive to areflexia | Near-universal | HP:0001252 (Hypotonia) |
| Global developmental delay / profound motor delay | Sign | Infancy, progressive | Near-universal | HP:0001263 |
| Progressive dystonia / hyperkinetic-dystonic movement disorder | Sign | Onset ~12–14 months, progressive | Very common | HP:0001332 (Dystonia); HP:0002072 (Chorea) may co-occur |
| Sensorineural hearing loss | Sign | Progressive, often profound | Very common (a defining feature) | HP:0000407 |
| Failure to thrive / postnatal growth retardation | Sign | Infancy onward | Common | HP:0001508 / HP:0008897 |
| Feeding difficulties | Sign | Infancy | Common | HP:0011968 |
| Muscular atrophy | Sign | Progressive | Common | HP:0003202 |
| External ophthalmoplegia | Sign | Variable | Reported subset | HP:0000544 |
| Leigh-like basal ganglia lesions (putamen/caudate T2 hyperintensity, atrophy) on MRI | Imaging | Progressive | Common where imaged | HP:0002490 (basal ganglia signal abnormality context) |
| Epilepsy/seizures | Sign | Variable, more frequent in SUCLA2 than SUCLG1 cohort | Reported in a substantial minority | HP:0001250 |
| Scoliosis | Sign | Later | Reported | HP:0002650 |
| Elevated blood/urine methylmalonic acid | Lab abnormality | Present from infancy, mild/moderate | Near-universal (defining biomarker) | HP:0003348 |
| Elevated C4-dicarboxylic (methylmalonyl-/succinyl-) carnitine | Lab abnormality | Present from infancy | Near-universal | — |
| Elevated lactate (blood/CSF), variable | Lab abnormality | Variable | Common but not obligate | HP:0002151 |
| Elevated urinary 3-hydroxyisovaleric acid | Lab abnormality | — | Described as "a novel biochemical feature" ([PMID:19666145](https://pubmed.ncbi.nlm.nih.gov/19666145/)) | — |
| Elevated succinylcarnitine (in lieu of methylmalonic aciduria in some kindreds) | Lab abnormality | — | Reported in an atypical family ([PMID:23759946](https://pubmed.ncbi.nlm.nih.gov/23759946/)) | — |

**Severity/progression heterogeneity is a load-bearing theme in this literature, not a footnote:**
- Same genotype (p.Arg284Cys), discordant severity between a Down-syndrome-comorbid proband and his typical-karyotype sibling ([PMID:28749033](https://pubmed.ncbi.nlm.nih.gov/28749033/)).
- Identical compound-heterozygous genotype in siblings, divergent courses — one developed frank Leigh syndrome with GI dysfunction, the other did not; mtDNA was *not* depleted in either, and PDH/ETC deficiencies were tissue-restricted to skeletal muscle, sparing fibroblasts ([PMID:27913098](https://pubmed.ncbi.nlm.nih.gov/27913098/)) — direct evidence that mtDNA depletion is not obligatory for the clinical phenotype in every genotype.
- A p.Arg407Trp allele produces a **non-progressive** deafness + myoclonic-dystonic movement disorder that is "unchanging from childhood" into the fourth decade of life — a markedly more benign allelic variant than the classic infantile-lethal presentation ([PMID:33231368](https://pubmed.ncbi.nlm.nih.gov/33231368/)).
- A milder, slowly progressive phenotype (p.Asp333Gly) was predicted computationally to "reduce the activity of the otherwise functional enzyme" rather than abolish it ([PMID:24986829](https://pubmed.ncbi.nlm.nih.gov/24986829/)).

**Quality of life:** No disease-specific EQ-5D/SF-36/PROMIS data were located in this search; QOL impact is described only narratively (profound motor and communicative disability from combined dystonia/deafness/developmental delay). This is a genuine evidence gap, not an omission — flag as `SOURCE_UNSPECIFIED` if curated.

---

## 4. Genetic/Molecular Information

**Causal gene:** *SUCLA2* (HGNC:11450, chr13q14.2, NM_003850, OMIM *603921), encoding the β-subunit of the ATP-specific (A-SUCL, "SCS-A") isoform of succinyl-CoA synthetase.

**Variant spectrum:** Missense (e.g., p.Arg284Cys, p.Arg407Trp/Leu, p.Asp333Gly, p.Met329Val, p.Asp251Asn), nonsense (p.Arg412*, [PMID:39070054](https://pubmed.ncbi.nlm.nih.gov/39070054/)), splice-site (the Faroese founder allele), frameshift/indel, and at least one intragenic deletion ([PMID:26409464](https://pubmed.ncbi.nlm.nih.gov/26409464/)). A contiguous-gene 13q14 deletion encompassing both *SUCLA2* and *RB1* has also been reported in compound heterozygosity with a SUCLA2 point mutation ([PMID:24986829](https://pubmed.ncbi.nlm.nih.gov/24986829/)).

**Variant classification:** Per ClinVar, individual variants are classified largely Pathogenic/Likely Pathogenic under ACMG/AMP criteria (e.g., NM_003850.3(SUCLA2):c.1220G>T p.Arg407Leu — [ClinVar RCV000818177](https://www.ncbi.nlm.nih.gov/clinvar/RCV000818177/)); curate against ClinVar/ClinGen directly rather than from this narrative.

**Allele frequency:** The Faroese founder splice-site allele is present at ~2% in that isolated population (carrier frequency 1:33), giving a locally calculated homozygote incidence around 1:2500–1:1700 depending on the source ([PMID:17287286](https://pubmed.ncbi.nlm.nih.gov/17287286/), [PMID:19666145](https://pubmed.ncbi.nlm.nih.gov/19666145/)) — an order of magnitude above gnomAD's expected population-wide rare-disease frequency, consistent with founder-effect enrichment. Outside the Faroe Islands, individual pathogenic alleles are each documented in only single-digit numbers of families; gnomAD-wide population allele frequencies for the recurrent non-Faroese alleles were not directly retrieved in this pass and should be verified per-variant in gnomAD/ClinVar at curation time.

**Origin:** Germline in all reported cases (this is a classic recessive Mendelian mitochondrial-maintenance disorder, not somatic).

**Functional consequence — genotype/severity correlation:** Western blot data across the SUCLG1/SUCLA2 heterodimer axis show that loss of one partner subunit destabilizes the other: "in the absence of SUCLG1 protein, no SUCLA2 protein is found" ([PMID:20693550](https://pubmed.ncbi.nlm.nih.gov/20693550/)), and conversely a SUCLG1 point mutation caused "no detectable levels of SUCLG1, while SUCLA2 and SUCLG2 protein expressions were largely reduced" with SUCLG2 mislocalization away from the mitochondrial network ([PMID:30470562](https://pubmed.ncbi.nlm.nih.gov/30470562/)). Residual protein amount tracks with phenotype severity ([PMID:20693550](https://pubmed.ncbi.nlm.nih.gov/20693550/) title itself: "The severity of phenotype linked to SUCLG1 mutations could be correlated with residual amount of SUCLG1 protein"). At the individual-variant level, p.Met329Val produces "reduced amount of the SUCLA2 protein, impaired production of mitochondrial ATP, and enhanced production of reactive oxygen species" ([PMID:24659738](https://pubmed.ncbi.nlm.nih.gov/24659738/)).

**Modifier genes:** *SUCLG2* (the alternative, GTP-forming SCS-β subunit gene, which forms a paralogous heterodimer with SUCLG1) is the principal candidate modifier — in patient fibroblasts, SUCLA2 loss alone left "normal mtDNA content and normal NDPK activity," but shRNA knockdown of *SUCLG2* in the same cells caused significant mtDNA depletion, "suggest[ing] SUCLG2 plays a more critical role than SUCLA2 in mtDNA maintenance, potentially explaining tissue-specific disease manifestations" ([PMID:21295139](https://pubmed.ncbi.nlm.nih.gov/21295139/)). This is a genuinely important, somewhat counterintuitive mechanistic finding for the pathophysiology write-up: fibroblasts from SUCLA2-null patients can have preserved mtDNA content in vitro even as brain/muscle in vivo show profound depletion, implying SUCLG2 compensation is tissue-restricted (consistent with the neuron-exclusive SUCLA2 expression data below).

**Epigenetics:** No disease-specific epigenetic (methylation/histone) literature was identified for SUCLA2-MDS in this search.

**Chromosomal abnormalities:** The 13q14 SUCLA2/RB1 contiguous deletion above is the only structural-variant mechanism documented.

---

## 5. Environmental Information

No established environmental, toxic, occupational, or infectious contributing factors — this is a purely monogenic disease. No lifestyle-factor literature applies. Not relevant to curate an `environmental:` block beyond a note explaining its absence.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, with inference flagged)

1. **Biallelic SUCLA2 loss-of-function variant** → loss of, or markedly reduced, the β-subunit of ADP-forming succinyl-CoA synthetase (A-SUCL/SCS-A). *Directly demonstrated*: enzyme activity assays in patient muscle mitochondria show "markedly decreased succinyl-CoA synthetase activity" ([PMID:15877282](https://pubmed.ncbi.nlm.nih.gov/15877282/)).
2. **Loss of SCS-A protein/activity destabilizes its heterodimeric partner and physically-associated complex.** SCS-A normally forms a tight physical complex with mitochondrial nucleoside diphosphate kinase (NDPK/NME4); *demonstrated in vitro*: "Succinyl-CoA synthase... disrupts its tight interaction with mitochondrial nucleoside diphosphate kinase, thereby compromising mitochondrial DNA synthesis" (mechanism reviewed across [PMID:15877282](https://pubmed.ncbi.nlm.nih.gov/15877282/), [PMID:18392745](https://pubmed.ncbi.nlm.nih.gov/18392745/)).
3. **Branch A — dNTP salvage pathway failure** → loss of the SCS–NDPK complex compromises the terminal step of the mitochondrial deoxyribonucleotide (dNTP) salvage pathway, causing depletion of the mitochondrial dNTP pool needed for mtDNA replication. This is presented as the leading mechanistic hypothesis ("a defect in the last step of mitochondrial dNTP salvage," [PMID:15877282](https://pubmed.ncbi.nlm.nih.gov/15877282/)) but is *tissue- and context-dependent*, not universal — patient fibroblasts can show normal mtDNA and normal NDPK activity despite SUCLA2 loss ([PMID:21295139](https://pubmed.ncbi.nlm.nih.gov/21295139/)), implicating compensation by the paralogous SUCLG2-containing complex outside brain/muscle.
4. **Branch B — direct TCA-cycle/substrate-level phosphorylation deficit** → loss of succinyl-CoA↔succinate/ATP(GTP) interconversion directly reduces mitochondrial substrate-level phosphorylation capacity, independent of any mtDNA effect. *Directly demonstrated* as a parallel/alternative mechanism: siblings with identical compound-heterozygous genotype showed tissue-specific (skeletal-muscle-restricted) secondary deficiencies of pyruvate dehydrogenase complex and electron transport chain enzymes **"without mitochondrial DNA depletion"** ([PMID:27913098](https://pubmed.ncbi.nlm.nih.gov/27913098/)) — i.e., mtDNA depletion is not obligatory for the clinical phenotype in every genotype/tissue combination, and OXPHOS/PDH dysfunction can arise from loss of substrate flux and/or secondary ROS/succinylation effects rather than solely from reduced mtDNA copy number.
5. **(Both branches converge on) mtDNA depletion in affected tissues** (brain, muscle) → reduced synthesis of mtDNA-encoded OXPHOS subunits → combined respiratory chain deficiency. *Directly demonstrated* by mtDNA quantification in muscle/brain of affected patients across multiple series ([PMID:17287286](https://pubmed.ncbi.nlm.nih.gov/17287286/), [PMID:39070054](https://pubmed.ncbi.nlm.nih.gov/39070054/) — reduced blood mtDNA content in both siblings).
6. **Cell-autonomous vulnerability is concentrated in neurons.** *SUCLA2* (the A-isoform β-subunit) shows **exclusive neuronal expression** in human cerebral cortex — "A-SUCL-β immunoreactivity in surgical human cortical tissue samples was present exclusively in neurons," co-localizing >99% with mitochondrial ATP synthase, and was "absent in glial cells" ([PMID:24085565](https://pubmed.ncbi.nlm.nih.gov/24085565/); confirmed independently in [PMID:25370487](https://pubmed.ncbi.nlm.nih.gov/25370487/), which further shows SUCLG2 is restricted to cerebral vasculature rather than glia, implying glial cells use an alternative, non-SCL-dependent route to bypass matrix substrate-level phosphorylation). This is a strong candidate mechanistic explanation for the striking selectivity of basal-ganglia/neuronal injury on MRI despite ubiquitous mitochondrial expression of the gene.
7. **Combined bioenergetic failure (ATP synthesis capacity loss) in high-energy-demand tissues** — neurons (especially basal ganglia circuitry), skeletal muscle, cochlear hair cells/auditory pathway → the clinical triad of dystonia/basal ganglia injury, hypotonia/myopathy, and sensorineural deafness. This final step is *inferred* from the convergence of tissue distribution, enzyme deficiency, and imaging/clinical correlation rather than directly imaged as a single causal experiment.
8. **A newly proposed additional branch (2026, zebrafish model, mechanistically downstream/parallel):** loss of Sucla2 causes **succinyl-CoA accumulation and consequent hypersuccinylation** of mitochondrial proteins, which consumes the enzymatic cofactor NAD⁺ and propagates respiratory chain dysfunction; NAD⁺ precursor supplementation, acting partly via the NAD⁺-dependent desuccinylase Sirt5, "restores NAD+ levels and improves locomotion and survival" in the model ([PMID:41574612](https://pubmed.ncbi.nlm.nih.gov/41574612/)). This reframes part of the pathology as a protein-hypersuccinylation/NAD⁺-depletion mechanism rather than purely a dNTP/mtDNA-copy-number problem — evidence source is **model organism (zebrafish), not yet shown in human SUCLA2 patients** (a `HUMAN_MODEL_MISMATCH`-shaped gap if curated in dismech).

### Category detail

- **Molecular pathway:** TCA cycle (Krebs cycle) substrate-level phosphorylation step (succinyl-CoA + ADP/GDP + Pi ⇌ succinate + ATP/GTP); secondarily, mitochondrial dNTP salvage pathway (NDPK-dependent). Suggested GO terms: GO:0006099 (tricarboxylic acid cycle), GO:0006265-adjacent — more precisely GO:0004775 (succinate-CoA ligase (ADP-forming) activity), GO:0009142 (nucleoside triphosphate biosynthetic process), GO:0032042 (mitochondrial DNA metabolic process).
- **Cellular process:** impaired oxidative phosphorylation / ATP generation; secondary generation of reactive oxygen species ([PMID:24659738](https://pubmed.ncbi.nlm.nih.gov/24659738/)); protein hypersuccinylation with perturbed neuronal transcription/metabolism, shown specifically in a forebrain-conditional mouse knockout ("Loss of succinyl-CoA synthetase in mouse forebrain results in hypersuccinylation with perturbed neuronal transcription and metabolism," [PMID:37819759](https://pubmed.ncbi.nlm.nih.gov/37819759/)).
- **Protein dysfunction:** loss-of-function/reduced abundance of SCS-A β-subunit; obligate heterodimer destabilization of the α-subunit partner (encoded by *SUCLG1*) and secondary effects on the paralogous GTP-forming complex (*SUCLG2*).
- **Metabolic changes:** TCA cycle flux impairment; elevated methylmalonic acid and C4-dicarboxylic (methylmalonyl-/succinyl-) carnitine — proposed to arise from propionate/methylmalonyl-CoA pathway backup secondary to reduced succinyl-CoA turnover; variable lactic acidosis; elevated 3-hydroxyisovaleric acid.
- **Immune system:** not implicated.
- **Tissue damage mechanism:** oxidative stress (ROS) and bioenergetic failure rather than inflammatory or fibrotic mechanisms; germ-cell mitochondrial injury has also been shown mechanistically in a mouse spermatocyte knockdown model (apoptosis via mitochondrial membrane potential loss, [PMID:27766610](https://pubmed.ncbi.nlm.nih.gov/27766610/)) — not a clinical disease feature but supports the general "high-ATP-demand cell type is selectively vulnerable" theme.
- **Biochemical abnormality:** succinyl-CoA synthetase (ADP-forming) enzymatic deficiency, confirmed by both classical spectrophotometric assay and a newer LC-MS/MS enzyme assay ([PMID:27913098](https://pubmed.ncbi.nlm.nih.gov/27913098/)).
- **Cell types/anatomical convergence:** cortical/basal ganglia neurons (GO/CL: neuron, CL:0000540), skeletal myocytes, cochlear/auditory pathway cells.

### Suggested cell-type / process ontology terms
- CL:0000540 (neuron) — SUCLA2-exclusive expression compartment in cortex
- CL:0000187 (muscle cell) / CL:0000188 (skeletal muscle myoblast lineage)
- GO:0004775 (succinate-CoA ligase (ADP-forming) activity)
- GO:0006099 (tricarboxylic acid cycle)
- GO:0032042 (mitochondrial DNA metabolic process)
- GO:0006974 / GO:0034599 (oxidative stress response) — secondary ROS phenotype

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** central nervous system (basal ganglia — putamen and caudate nucleus preferentially; cerebral cortex; cerebellum in some), skeletal muscle, inner ear/cochlea (sensorineural hearing).
- **Organ level (secondary/variable):** eyes (external ophthalmoplegia in a subset), skeletal system (scoliosis), gastrointestinal tract (feeding difficulty, and frank GI dysfunction in the Leigh-syndrome-presenting sibling of [PMID:27913098](https://pubmed.ncbi.nlm.nih.gov/27913098/)).
- **Body systems:** nervous, musculoskeletal, auditory/sensory, less commonly ophthalmologic and GI.
- **Tissue/cell level:** neurons (basal ganglia/cortex — the *exclusively* SUCLA2-expressing cell type in brain, [PMID:24085565](https://pubmed.ncbi.nlm.nih.gov/24085565/)); skeletal myofibers (tissue-restricted OXPHOS/PDH deficiency shown specifically in muscle but not fibroblasts, [PMID:27913098](https://pubmed.ncbi.nlm.nih.gov/27913098/)); cochlear hair cells/auditory neurons (inferred from the deafness phenotype, not directly biopsied in the cited literature).
- **Subcellular level:** mitochondrial matrix (site of the SCS heterodimer and TCA cycle), mitochondrial nucleoid (site of mtDNA replication affected by dNTP pool depletion). GO Cellular Component: GO:0005759 (mitochondrial matrix), GO:0042645 (mitochondrial nucleoid).
- **Localization/laterality:** bilateral, symmetric basal ganglia involvement typical of Leigh-like imaging; bilateral sensorineural hearing loss.
- Suggested UBERON terms: UBERON:0001874 (putamen), UBERON:0001873 (caudate nucleus), UBERON:0001351 (auditory system structures — refine to cochlea UBERON:0000411), UBERON:0001134 (skeletal muscle tissue).

---

## 8. Temporal Development

- **Onset:** neonatal to early infantile; hypotonia typically from birth or the first months of life. Progressive neurologic deterioration is described as beginning "from the age of 12 to 14 months" in the encephalomyopathic (typical/severe) phenotype description synthesized from GeneReviews/OMIM sources above.
- **Onset pattern:** insidious/progressive rather than acute, though episodic metabolic decompensation (lactic acidosis exacerbations) can occur.
- **Progression:** Generally a progressive, non-remitting neurodegenerative course in the classic severe form — muscular atrophy and dystonia worsen over the first years of life. However, genotype-dependent exceptions exist: the p.Arg407Trp allele produces a **static, non-progressive** course from childhood into the fourth decade ([PMID:33231368](https://pubmed.ncbi.nlm.nih.gov/33231368/)), and p.Asp333Gly produces "slowly progressive" disease ([PMID:24986829](https://pubmed.ncbi.nlm.nih.gov/24986829/)) — so progression rate is explicitly genotype-heterogeneous, not a fixed disease parameter.
- **Course pattern:** chronic progressive in the majority; a minority static/non-progressive.
- **Critical periods:** the first 1–2 years of life represent the period of most rapid neurologic decline in the typical form; this is also the practical window for any disease-modifying intervention (e.g., the deoxynucleoside trials below explicitly target early treatment).

---

## 9. Inheritance and Population

- **Epidemiology:** No global point-prevalence/incidence figure exists for the general population — this is an ultra-rare disease outside the founder population. In the **Faroe Islands**, incidence is **1:1700**, carrier frequency **1:33**, mutant allele frequency **2%** ([PMID:17287286](https://pubmed.ncbi.nlm.nih.gov/17287286/)); some accounts cite an estimated homozygote frequency of 1:2500 from the same allele-frequency data ([earlier WebSearch summary](https://academic.oup.com/brain/article/130/3/862/281743), consistent with — though not identical to — the directly reported 1:1700 clinical incidence; the discrepancy likely reflects ascertainment vs. Hardy-Weinberg calculation and should be resolved against the primary source text at curation time rather than averaged).
- **Inheritance pattern:** Autosomal recessive.
- **Penetrance:** Effectively complete for the biallelic pathogenic genotype in reported cases, though expressivity (severity/progression) varies substantially by allele (see Phenotypes/Mechanism).
- **Expressivity:** Markedly variable — from infantile-lethal encephalomyopathy to a static adult-persisting deafness-dystonia syndrome, tracked to specific alleles (p.Arg407Trp/Leu vs. the Faroese splice allele vs. null alleles).
- **Genetic anticipation:** Not described — not a repeat-expansion disorder.
- **Germline mosaicism:** Not specifically reported in the literature surveyed.
- **Founder effect:** Documented and well-characterized in the Faroe Islands (splice-site allele, common ancestor traced across 8 studied families, [WebSearch summary of PMID:17301081](https://academic.oup.com/brain/article/130/3/862/281743)).
- **Consanguinity:** A recurring feature of non-Faroese case reports (e.g., [PMID:23759946](https://pubmed.ncbi.nlm.nih.gov/23759946/) — first-cousin parents; [PMID:27651038](https://pubmed.ncbi.nlm.nih.gov/27651038/) — consanguineous parents), consistent with a rare AR disorder outside the founder population.
- **Carrier frequency:** 1:33 in the Faroe Islands specifically; not established elsewhere (would require gnomAD-based estimation per allele, not done in this pass).
- **Population demographics:** Reported case ancestries include Faroese/Scandinavian (the founder cluster), Italian, other European/Caucasian, Portuguese, Chinese, Iranian, Hispanic, Turkish, Lebanese, and other populations — i.e., globally distributed but each non-Faroese cluster is its own private/recurrent allele rather than a shared worldwide founder variant.
- **Sex ratio:** No sex predilection reported (autosomal recessive; consistent across all cited case series).
- **Age distribution:** Concentrated in infancy/early childhood at diagnosis, consistent with the onset pattern above; survivors into adulthood are described only for the milder allelic subset.

---

## 10. Diagnostics

**Laboratory/biochemical tests (first-line, non-invasive):**
- Plasma and urine methylmalonic acid (mildly-moderately elevated — the defining feature that distinguishes this from classical methylmalonic acidemia, where levels are far higher)
- Plasma acylcarnitine profile: elevated C4-dicarboxylic carnitine (methylmalonyl-/succinylcarnitine)
- Urine organic acids: elevated 3-hydroxyisovaleric acid ("a novel biochemical feature," [PMID:19666145](https://pubmed.ncbi.nlm.nih.gov/19666145/))
- Plasma/CSF lactate (variably elevated)
- The Morava et al. series explicitly recommends **direct genetic sequencing rather than invasive muscle biopsy** for diagnosis once this biochemical pattern is recognized ([PMID:19666145](https://pubmed.ncbi.nlm.nih.gov/19666145/)) — a practical diagnostic-pathway point worth preserving verbatim in curation.

**Enzyme/functional assays:** Succinyl-CoA synthetase activity assay in muscle mitochondria (classical spectrophotometric method, [PMID:15877282](https://pubmed.ncbi.nlm.nih.gov/15877282/)); a newer LC-MS/MS-based SUCL activity assay has since been developed and validated ([PMID:27913098](https://pubmed.ncbi.nlm.nih.gov/27913098/)).

**mtDNA copy number quantification:** qPCR-based mtDNA/nDNA ratio in muscle, and in some cases blood ([PMID:39070054](https://pubmed.ncbi.nlm.nih.gov/39070054/) documents reduced *blood* mtDNA content in both affected siblings — relevant because muscle biopsy is invasive and blood-based mtDNA quantification is a less-invasive alternative, though it is **not universally reduced** in this disease — see [PMID:27913098](https://pubmed.ncbi.nlm.nih.gov/27913098/), where affected siblings had normal muscle mtDNA content despite the clinical phenotype).

**Genetic testing:**
- Single-gene *SUCLA2* sequencing or targeted panel (mitochondrial DNA depletion syndrome panels routinely include SUCLA2, SUCLG1, POLG, TK2, DGUOK, RRM2B, MPV17, TYMP, C10orf2/TWNK, MGME1, FBXL4)
- Whole-exome sequencing has been diagnostic in multiple case reports where phenotype was atypical (e.g., [PMID:23010432](https://pubmed.ncbi.nlm.nih.gov/23010432/) — "next-generation technologies, particularly exome-sequencing, are user friendly, powerful means for the identification of disease genes in genetically and clinically heterogeneous inherited conditions, such as mitochondrial disorders")
- Chromosomal microarray indicated when a contiguous-deletion mechanism (13q14, SUCLA2/RB1) is suspected

**Imaging:** Brain MRI showing "demyelination and central and cortical atrophy, including atrophy of the basal ganglia" ([PMID:17287286](https://pubmed.ncbi.nlm.nih.gov/17287286/)); T2-hyperintensity of putamen/caudate — Leigh-syndrome-like pattern. MR spectroscopy may show cortical/ventricular lactate peaks even when structural MRI is normal ([PMID:27651038](https://pubmed.ncbi.nlm.nih.gov/27651038/): "brain MRI was normal while ¹H-MRS showed lactate peaks"; and note the 2026 case report explicitly titled "Normal neuroimaging in an infant with SUCLA2-related mitochondrial DNA depletion syndrome type 5," PMID 42741765 — underscoring that normal MRI does not exclude the diagnosis).

**Muscle biopsy/histopathology:** Respiratory chain enzyme activities (combined deficiency pattern), and secondary PDH deficiency in a tissue-restricted manner in some genotypes — but biopsy is now positioned as confirmatory/mechanistic rather than the primary diagnostic step, per the sequencing-first recommendation above.

**Differential diagnosis — mitochondrial DNA depletion syndromes (MDS) by clinical subtype** (per [PMID:28215579](https://pubmed.ncbi.nlm.nih.gov/28215579/) and general MDS nosology):

| Subtype | Genes | Key distinguishing features |
|---|---|---|
| **Encephalomyopathic with methylmalonic aciduria (this entry)** | SUCLA2 (MTDPS5), SUCLG1 (MTDPS9) | Deafness-dystonia triad, mild methylmalonic aciduria/C4-DC-carnitine; SUCLG1 form is more severe/earlier lethal, with hypertrophic cardiomyopathy and liver involvement essentially exclusive to SUCLG1 ([PMID:26475597](https://pubmed.ncbi.nlm.nih.gov/26475597/)) |
| Myopathic | TK2, RRM2B (severe infantile form) | Onset <2 years, hypotonia/weakness predominant, less prominent basal ganglia/deafness triad |
| Hepatocerebral | DGUOK, MPV17, POLG, TWNK/C10orf2 | Early liver failure/cholestasis, often fatal <1 year (MPV17); POLG additionally causes Alpers-Huttenlocher phenotype |
| Encephalomyopathic (other) | RRM2B | Hypotonia, tubulopathy, seizures, respiratory distress, diarrhea, severe neonatal lactic acidosis |

**Critical head-to-head data (same cohort, direct comparison):** In the largest published series (71 patients: 50 SUCLA2, 21 SUCLG1, [PMID:26475597](https://pubmed.ncbi.nlm.nih.gov/26475597/)):
- "Significantly longer survival in patients with SUCLA2 mutations compared to SUCLG1 mutations" — median survival 20 years (SUCLA2) vs. 20 months (SUCLG1)
- "Hypertrophic cardiomyopathy and liver involvement was exclusively found in patients with SUCLG1 mutations"
- Epilepsy substantially more frequent in SUCLA2 patients

This is the single most important lump/split-relevant and prognosis-relevant finding in the literature and should anchor the SUCLA2-vs-SUCLG1 distinction in any KB curation (note dismech's convention: keep SUCLA2-MDS5 and SUCLG1-MDS9 as **separate germline entries** per the lump/split framework, given the genuinely divergent gene, prognosis, and organ-involvement profile despite the shared ORPHA code and overlapping biochemical phenotype).

**Screening:** No population newborn-screening program was identified for SUCLA2-MDS specifically (methylmalonic acid elevation on newborn screening acylcarnitine profiles is nonspecific and would trigger workup for classical methylmalonic acidemia first). Targeted carrier screening in the Faroe Islands would be feasible given the single founder allele and known carrier frequency, though no specific program was documented in this search; Carrozzo et al. 2007 explicitly note the Faroese allele frequency data make "preventive measures" feasible ([PMID:17301081](https://pubmed.ncbi.nlm.nih.gov/17301081/) abstract synthesis).

---

## 11. Outcome/Prognosis

- **Survival:** Median survival is reported as **age 20 years** for SUCLA2-mutant patients specifically, versus 20 months for SUCLG1 ([PMID:26475597](https://pubmed.ncbi.nlm.nih.gov/26475597/)); a separate GeneReviews-derived figure states approximately **30% of affected individuals die during childhood** ([PMID:20301762](https://pubmed.ncbi.nlm.nih.gov/20301762/) synthesis). These two figures describe overlapping but distinct populations/methodologies (cohort survival curve vs. childhood mortality fraction) and should be cited separately rather than merged.
- **Disease course:** Progressive in the typical/severe form; static in the p.Arg407Trp allelic subset (persisting into the fourth decade essentially unchanged, [PMID:33231368](https://pubmed.ncbi.nlm.nih.gov/33231368/)).
- **Complications:** Scoliosis, epilepsy (more frequent in SUCLA2 than SUCLG1), secondary feeding/growth failure, and — in the Leigh-syndrome-presenting subset — GI dysfunction ([PMID:27913098](https://pubmed.ncbi.nlm.nih.gov/27913098/)).
- **Recovery potential:** No spontaneous recovery reported; treatment (below) is aimed at slowing progression/improving function rather than reversing established injury, though early case reports describe symptomatic improvement with specific interventions (CoQ10, succinate).
- **Prognostic factors:** Gene (SUCLA2 vs. SUCLG1) is the single strongest documented prognostic discriminator; specific allele (null/severe vs. p.Arg407Trp/Leu-type hypomorphic) is the second; residual protein amount by Western blot correlates with severity at the SUCLG1 locus specifically ([PMID:20693550](https://pubmed.ncbi.nlm.nih.gov/20693550/)) and plausibly generalizes to SUCLA2 though this was not directly quantified in the sources reviewed.
- **Prognostic biomarkers:** No validated molecular prognostic biomarker beyond genotype was identified; the deoxynucleoside trial below used an unspecified "biomarker of mitochondrial dysfunction" that "normalized in three of five elevated cases" as a treatment-response (not baseline prognostic) marker ([PMID:40175578](https://pubmed.ncbi.nlm.nih.gov/40175578/)).

---

## 12. Treatment

There is **no approved disease-specific therapy**; management is predominantly supportive, with several small-scale/case-level pharmacologic interventions reported and one open-label multi-gene trial.

**Supportive care (NCIT-suggestible):**
- Developmental/physical/occupational therapy — NCIT:C15302 (Physical Therapy), NCIT:C15315 (Rehabilitation)
- Seizure management (standard antiepileptic pharmacotherapy) — NCIT:C15986 (Pharmacotherapy)
- Hearing intervention (hearing aids/cochlear implantation as needed for the sensorineural component) — NCIT:C15329 (Surgical Procedure) if implantation, device concept flagged separately per dismech's device-vs-action convention
- Nutritional support/feeding intervention for failure to thrive — [PMID:19666145](https://pubmed.ncbi.nlm.nih.gov/19666145/) explicitly "suggest[s] nutritional intervention may benefit patients" — NCIT:C15447 (Dietary Intervention) or NCIT:C15433 (Nutritional Support), per-case judgment
- Surveillance for scoliosis, growth, and development per GeneReviews management recommendations

**Pharmacotherapy (small-scale/case-level evidence):**
- **Coenzyme Q10 (CoQ10):** In a single case, "escalating doses of CoQ10 up to 2000 mg daily were associated with improvement of muscle weakness and stabilization of the disease course" ([PMID:27651038](https://pubmed.ncbi.nlm.nih.gov/27651038/)) — single-patient observational evidence, not a controlled trial.
- **Succinate supplementation:** In the p.Arg407Trp allele patient, "succinate supplementation circumvents the Krebs cycle block," though neurologic manifestations persisted ([PMID:33231368](https://pubmed.ncbi.nlm.nih.gov/33231368/)) — mechanistically rational (bypasses the enzymatic step) but only partially effective and single-patient evidence.
- **Antioxidant therapy:** Proposed but not trialed in the cited source, based on the demonstrated ROS-elevation mechanism with the p.Met329Val allele ("findings...suggest antioxidant therapies may benefit disease progression," [PMID:24659738](https://pubmed.ncbi.nlm.nih.gov/24659738/)) — a mechanistic hypothesis, not a treatment result.
- **NAD⁺ precursor supplementation:** Restored NAD⁺ levels and "improve[d] locomotion and survival" in a zebrafish *sucla2* mutant model via the Sirt5 desuccinylation axis ([PMID:41574612](https://pubmed.ncbi.nlm.nih.gov/41574612/)) — **model-organism evidence only**, not yet tested in human SUCLA2 patients; a clear `MODEL_SYSTEM_EXTRAPOLATION`/`HUMAN_MODEL_MISMATCH` candidate if curated.

**Investigational/trial-level evidence — deoxynucleoside therapy:**
- ClinicalTrials.gov **NCT04802707** ("Deoxynucleosides Pyrimidines as Treatment for Mitochondrial Depletion Syndrome," McGill University Health Centre) enrolled pediatric patients with pathogenic variants in POLG, C10orf2/TWNK, RRM2B, MPV17, **SUCLA2**, SUCLG1, or FBXL4 for open-label deoxycytidine/deoxythymidine treatment.
- Published sub-study results ([PMID:40175578](https://pubmed.ncbi.nlm.nih.gov/40175578/), *J Neurol* 2025): 8 participants with variants in FBXL4, SUCLG1, SUCLA2, or RRM2B; "clinical scores improved at 1-month and 6-month assessments, and a biomarker of mitochondrial dysfunction normalized in three of five elevated cases." Authors conclude: **"these data suggest deoxycytidine/deoxythymidine is a safe and therapeutically promising intervention for a broad range of mitochondrial DNA depletion disorders."** This is the strongest available (though still small-n, open-label, non-SUCLA2-specific-subgroup-reported) treatment evidence for this disease category, and directly mechanistically relevant given the dNTP-salvage-pathway hypothesis above (supplying exogenous deoxynucleosides is a rational bypass strategy analogous to the established rationale in TK2- and RRM2B-related MDS).
- Note: the companion long-term/POLG-specific trial report ([PMID:42296640](https://pubmed.ncbi.nlm.nih.gov/42296640/)) is **POLG-exclusive** and should not be cited as SUCLA2 evidence.

**Gene/cell/RNA-based therapy, surgical/interventional, immunotherapy, targeted therapy:** No SUCLA2-disease-specific programs identified in this search (unlike some other MDS genes, e.g., DGUOK/TK2 gene-therapy programs exist but were not found for SUCLA2 specifically).

**Treatment algorithm:** No published formal clinical pathway/algorithm specific to SUCLA2-MDS; management follows general mitochondrial disease supportive-care guidelines (e.g., Mitochondrial Medicine Society consensus recommendations, not individually re-verified here) plus the emerging deoxynucleoside option under trial.

---

## 13. Prevention

- **Primary prevention:** Carrier screening / genetic counseling in the Faroe Islands is feasible given the known single founder allele and 1:33 carrier frequency; Carrozzo et al. 2007 explicitly frame the Faroese allele-frequency data as enabling "preventive measures" ([PMID:17301081](https://pubmed.ncbi.nlm.nih.gov/17301081/)). No population-wide newborn or carrier screening program specific to SUCLA2 was documented outside this framing.
- **Secondary prevention:** Prenatal diagnosis and preimplantation genetic testing are procedurally available for known-carrier couples (standard practice for any characterized AR disorder), though no SUCLA2-specific PGT/prenatal-diagnosis case series was identified in this search.
- **Tertiary prevention:** Surveillance protocols per GeneReviews (growth, development, scoliosis monitoring; hearing surveillance; seizure monitoring) aim to catch and manage complications early rather than prevent primary disease onset.
- **Genetic counseling:** Standard autosomal recessive counseling — 25% recurrence risk per pregnancy for carrier couples, carrier testing available for at-risk relatives once the familial variant(s) are known; particularly actionable in the Faroese founder population given the single recurrent allele.
- **Public health/environmental/behavioral prevention:** Not applicable (no environmental risk factor exists to modify).

---

## 14. Other Species / Natural Disease

No naturally-occurring veterinary/companion-animal SUCLA2-deficiency disease was identified in this search (no OMIA entry surfaced). The disease is currently known only in humans; all non-human data come from engineered models (below), not spontaneous animal disease.

**Orthologous gene:** Mouse *Sucla2* (NCBI Gene, chromosome 14 in mouse per the Wikipedia gene-location data retrieved above); zebrafish *sucla2* ortholog used in the 2026 NAD⁺/Sirt5 study.

---

## 15. Model Organisms

| Model | Type | Genotype | Key phenotype | Fidelity/limitation notes | Reference |
|---|---|---|---|---|---|
| Whole-body *Sucla2*⁻/⁻ mouse | Constitutive knockout | Homozygous null | **Embryonic/perinatal lethal** — "whole-body KO of Sucla2 is a lethal phenotype in mice" | Precludes study of the postnatal human phenotype directly; necessitates conditional models | Referenced context in [PMC11634519](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11634519) / [PMID:39482887](https://pubmed.ncbi.nlm.nih.gov/39482887/) discussion |
| *Sucla2*⁺/⁻ and *Suclg2*⁺/⁻ heterozygote mice | Transgenic, germline heterozygous | Single-allele loss | Tissue/age-dependent decrease in Sucla2 expression and ATP-forming SCS activity; compensatory rebound of cardiac Suclg2 expression/GTP-forming activity; mtDNA content moderately decreased; blood carnitine esters elevated; bioenergetic differences from WT only became apparent under submaximal pharmacologic SCS inhibition | Models a milder/subclinical state; illustrates the SUCLG2-compensation mechanism in vivo, paralleling the fibroblast data of [PMID:21295139](https://pubmed.ncbi.nlm.nih.gov/21295139/) | "Two transgenic mouse models for β-subunit components of succinate-CoA ligase yielding pleiotropic metabolic alterations," [PMC5126846](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5126846) |
| Skeletal-muscle-specific conditional *Sucla2* knockout (Cre-lox, human skeletal actin promoter) | Conditional/tissue-restricted knockout | Muscle-restricted null | Severe growth failure (44% of WT body weight by weaning), reduced grip strength, exercise intolerance; **muscle-type-specific** effect — slow-twitch soleus showed "40% less specific tetanic force" while fast-twitch muscle was relatively spared | Directly models the myopathic component of human disease with good apparent face validity for muscle-fiber-type selectivity; does not model the neurologic/auditory components | [PMID:39482887](https://pubmed.ncbi.nlm.nih.gov/39482887/), *J Cachexia Sarcopenia Muscle* 2024 |
| Forebrain-specific conditional *Sucla2* knockout | Conditional/tissue-restricted knockout | Forebrain-restricted null (postnatal) | Hypersuccinylation of mitochondrial/neuronal proteins with "perturbed neuronal transcription and metabolism"; survivable into adulthood unlike whole-body KO | Directly relevant to the CNS component of disease and to the protein-succinylation mechanistic hypothesis; whether it recapitulates the specific basal-ganglia/dystonia phenotype was not detailed in the abstract retrieved | [PMID:37819759](https://pubmed.ncbi.nlm.nih.gov/37819759/), 2023 |
| Zebrafish *sucla2* mutant | Genetic (presumably CRISPR/mutagenesis-derived) whole-organism model | Loss-of-function | Locomotor defects and reduced survival; bioenergetic failure driven by succinyl-CoA-excess-induced NAD⁺ depletion; rescued by NAD⁺ precursor supplementation and implicates Sirt5 desuccinylase activity | Establishes a therapeutically tractable, orally-supplementable mechanism (NAD⁺ precursors) not yet tested in human SUCLA2 patients — treat as **model-system extrapolation**, not clinical evidence, until translated | [PMID:41574612](https://pubmed.ncbi.nlm.nih.gov/41574612/), *JCI Insight* 2026 |
| Mouse GC2 spermatocyte cell line / testis Sucla2 knockdown | Cell-line/tissue knockdown (not a disease model per se) | shRNA knockdown | Apoptosis, reduced mitochondrial membrane potential, decreased ATP, elevated ROS | Demonstrates general cell-autonomous consequences of Sucla2 loss in a high-ATP-demand cell type; not a model of the clinical neurologic/muscular/auditory phenotype | [PMID:27766610](https://pubmed.ncbi.nlm.nih.gov/27766610/) |
| Patient-derived fibroblasts (human, not an animal model but the key in-vitro system) | Primary patient cells ± shRNA SUCLG2 knockdown | SUCLA2-null patient cells, with/without secondary SUCLG2 knockdown | SUCLA2 loss alone: normal mtDNA/NDPK activity; SUCLG2 knockdown superimposed: significant mtDNA depletion | Central to establishing the SUCLG2-compensation/tissue-selectivity mechanism; limitation is that fibroblasts may not recapitulate neuron- or myocyte-specific vulnerability | [PMID:21295139](https://pubmed.ncbi.nlm.nih.gov/21295139/) |

**Model-organism research applications:** the conditional mouse models (muscle- and forebrain-specific) exist specifically because the whole-body knockout is embryonic lethal, and they are being used to dissect tissue-specific mechanisms (fiber-type-selective bioenergetic failure in muscle; hypersuccinylation/transcriptional dysregulation in forebrain) that map onto the two most clinically prominent affected tissues (muscle, CNS) — though neither model yet reproduces the auditory/deafness component of the human triad, which remains an unmodeled gap.

---

## Summary of Key Evidence Gaps (for curation planning)

1. **No formal QOL instrument data** (EQ-5D/SF-36/PROMIS) specific to this disease.
2. **No population-wide (non-Faroese) prevalence/incidence estimate** — only founder-population and case-series data exist.
3. **NAD⁺/Sirt5 mechanism and rescue is zebrafish-only** — a clear `HUMAN_MODEL_MISMATCH` candidate, not yet tested in patients.
4. **CoQ10 and succinate-supplementation "treatment" evidence is single-case**, not controlled-trial evidence.
5. **The deoxynucleoside trial ([PMID:40175578](https://pubmed.ncbi.nlm.nih.gov/40175578/)) pools SUCLA2 with FBXL4/SUCLG1/RRM2B** — gene-specific (SUCLA2-only) efficacy has not been separately reported and should not be over-attributed.
6. **No auditory-system-specific animal model** exists despite deafness being a defining clinical feature.
7. **Exact ORPHA:1933 vs. MONDO:0012791 scope alignment** (ORPHA:1933 appears to cover both SUCLA2- and SUCLG1-caused disease as a combined phenotype code, while MTDPS9/OMIM #245400 is the SUCLG1-specific phenotype entry) should be explicitly reconciled against Orphanet's own gene-disease table at curation time rather than assumed from this search.

---

### Sources
- [SUCLA2-Related Mitochondrial DNA Depletion Syndrome, Encephalomyopathic Form with Methylmalonic Aciduria - GeneReviews®](https://www.ncbi.nlm.nih.gov/books/NBK6803/) (PMID:20301762)
- [Entry - #612073 - OMIM](https://omim.org/entry/612073)
- [Entry - *603921 - OMIM](https://www.omim.org/entry/603921)
- [Carrozzo et al. 2007, Brain, PMID:17301081](https://pubmed.ncbi.nlm.nih.gov/17301081/)
- [Ostergaard et al. 2007, Brain, PMID:17287286](https://pubmed.ncbi.nlm.nih.gov/17287286/)
- [Elpeleg et al. 2005, Am J Hum Genet, PMID:15877282](https://pubmed.ncbi.nlm.nih.gov/15877282/)
- [Morava et al. 2009, Mitochondrion, PMID:19666145](https://pubmed.ncbi.nlm.nih.gov/19666145/)
- [Carrozzo et al. 2016, J Inherit Metab Dis, PMID:26475597](https://pubmed.ncbi.nlm.nih.gov/26475597/)
- [Miller et al. 2011, BBA, PMID:21295139](https://pubmed.ncbi.nlm.nih.gov/21295139/)
- [Dobolyi et al. 2015, Brain Struct Funct, PMID:24085565](https://pubmed.ncbi.nlm.nih.gov/24085565/)
- [Dobolyi et al. 2015, J Bioenerg Biomembr, PMID:25370487](https://pubmed.ncbi.nlm.nih.gov/25370487/)
- [Huang et al. 2017, Mol Genet Metab, PMID:27913098](https://pubmed.ncbi.nlm.nih.gov/27913098/)
- [Alkhater et al. 2021, Ann Clin Transl Neurol, PMID:33231368](https://pubmed.ncbi.nlm.nih.gov/33231368/)
- [Nogueira et al. 2015, J Child Neurol, PMID:24659738](https://pubmed.ncbi.nlm.nih.gov/24659738/)
- [Garone et al. 2017, J Child Neurol, PMID:27651038](https://pubmed.ncbi.nlm.nih.gov/27651038/)
- [Maas et al. 2016, JIMD Reports, PMID:26409464](https://pubmed.ncbi.nlm.nih.gov/26409464/)
- [Matilainen et al. 2015, Eur J Hum Genet, PMID:24986829](https://pubmed.ncbi.nlm.nih.gov/24986829/)
- [Couser et al. 2017, Am J Med Genet A, PMID:28749033](https://pubmed.ncbi.nlm.nih.gov/28749033/)
- [Rouzier et al. 2010, J Med Genet, PMID:20693550](https://pubmed.ncbi.nlm.nih.gov/20693550/)
- [Chinopoulos et al. 2019, Mol Genet Metab, PMID:30470562](https://pubmed.ncbi.nlm.nih.gov/30470562/)
- [Zhang et al. 2024, Frontiers in Neurology, PMID:39070054](https://pubmed.ncbi.nlm.nih.gov/39070054/)
- [Lancaster et al. 2024, J Cachexia Sarcopenia Muscle, PMID:39482887](https://pubmed.ncbi.nlm.nih.gov/39482887/)
- [Forebrain Sucla2 KO, PMID:37819759](https://pubmed.ncbi.nlm.nih.gov/37819759/)
- [Richard et al. 2026, JCI Insight, PMID:41574612](https://pubmed.ncbi.nlm.nih.gov/41574612/)
- [Two transgenic mouse models, PMC5126846](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5126846)
- [El-Hattab et al. 2017, BBA Mol Basis Dis, PMID:28215579](https://pubmed.ncbi.nlm.nih.gov/28215579/)
- [Berrahmoune et al. 2025, J Neurol, PMID:40175578](https://pubmed.ncbi.nlm.nih.gov/40175578/)
- [ClinicalTrials.gov NCT04802707](https://classic.clinicaltrials.gov/ct2/show/NCT04802707)
- [Orphanet: ORPHA:1933](https://www.orpha.net/en/disease/detail/1933)
- [SUCLA2 - Wikipedia](https://en.wikipedia.org/wiki/SUCLA2)
- [Jaberi et al. 2013, J Hum Genet, PMID:23759946](https://pubmed.ncbi.nlm.nih.gov/23759946/)
- [Lamperti et al. 2012, Mol Genet Metab, PMID:23010432](https://pubmed.ncbi.nlm.nih.gov/23010432/)
- [Huang et al. 2016, Folia Histochem Cytobiol, PMID:27766610](https://pubmed.ncbi.nlm.nih.gov/27766610/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 5 |
| References weighed for topical relevance | 32 |
| On topic | 26 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

4 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:19666145` *(abstract only)*: "a high incidence of 1 in 1700 in the Faroe Islands due to a founder effect"
  - closest text in source: "We describe the clinical course and biochemical phenotype in 16 children from the Faroe Islands with a homozygous SUCLA2 splice site mutation"
- `PMID:21295139` *(abstract only)*: "suggest[ing] SUCLG2 plays a more critical role than SUCLA2 in mtDNA maintenance, potentially explaining tissue-specific disease manifestations"
  - closest text in source: "This suggests that, SUCLG2, to a higher degree than SUCLA2, is crucial for mtDNA maintenance and that mitochondrial NDPK is involved"
- `PMID:15877282`: "Succinyl-CoA synthase... disrupts its tight interaction with mitochondrial nucleoside diphosphate kinase, thereby compromising mitochondrial DNA synthesis"
  - closest text in source: "Succinyl-CoA synthetase is invariably in a complex with mitochondrial nucleotide diphosphate kinase; hence, we propose that a defect in the last step of mitochondrial dNTP salvage is a novel cause of the mtDNA depletion syndrome"
- `PMID:18392745` *(abstract only)*: "Succinyl-CoA synthase... disrupts its tight interaction with mitochondrial nucleoside diphosphate kinase, thereby compromising mitochondrial DNA synthesis"
  - closest text in source: "The mtDNA depletion may be explained by the interaction of succinate-CoA ligase with nucleoside diphosphate kinase, which is involved in mitochondrial nucleotide metabolism."
- `PMID:24659738` *(abstract only)*: "findings...suggest antioxidant therapies may benefit disease progression,"
  - closest text in source: "Expanding the array of SUCLA2 mutations, we suggested that reactive oxygen species scavengers are likely to impact on disease prognosis."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 26 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (1 mention) - the report calls it "Near-universal"; HP calls it **Global developmental delay**
- `HP:0000407` (1 mention) - the report calls it "Very common (a defining feature)"; HP calls it **Sensorineural hearing impairment**
- `HP:0011968` (1 mention) - the report calls it "Common"; HP calls it **Feeding difficulties**
- `HP:0003202` (1 mention) - the report calls it "Common"; HP calls it **Skeletal muscle atrophy**
- `HP:0002490` (1 mention) - the report calls it "basal ganglia signal abnormality context"; HP calls it **Increased CSF lactate**
- `HP:0003348` (1 mention) - the report calls it "Near-universal (defining biomarker)"; HP calls it **Hyperalaninemia**
- `HP:0002151` (1 mention) - the report calls it "Common but not obligate"; HP calls it **Increased circulating lactate concentration**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000188` (1 mention) - the report calls it "skeletal muscle myoblast lineage"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `GO:0034599` (1 mention) - the report calls it "oxidative stress response"; GO calls it **cellular response to oxidative stress**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.