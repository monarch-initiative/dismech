---
provider: claude_code
model: claude-fable-5[1m], claude-haiku-4-5-20251001
cached: false
start_time: '2026-09-04T20:39:05.614053'
end_time: '2026-09-04T20:47:57.720993'
duration_seconds: 532.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Disability, X-linked, Syndromic 33
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
  - claude-fable-5[1m]
  - claude-haiku-4-5-20251001
  web_search_requests: 2
  num_turns: 25
  total_cost_usd: 3.394743
  session_id: e21eada7-f0ca-4ab0-ba42-07160799d7ed
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - mcp__pubmed__search_articles
  assistant_text_blocks: 11
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
citation_count: 13
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 32
  on_topic: 22
  validator_version: 0.2.1
term_validation:
  total_terms: 55
  verified: 54
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 3
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - "infancy; static \u2192 ID"
    ontology_label: Global developmental delay
  - term_id: HP:0001249
    reported_labels:
    - childhood; lifelong, largely stable
    ontology_label: Intellectual disability
  - term_id: HP:0000750
    reported_labels:
    - early childhood
    ontology_label: Delayed speech and language development
  - term_id: HP:0002079
    reported_labels:
    - congenital
    ontology_label: Hypoplasia of the corpus callosum
  - term_id: HP:0000365
    reported_labels:
    - childhood
    ontology_label: Hearing impairment
  - term_id: HP:0000486
    reported_labels:
    - childhood
    ontology_label: Strabismus
  - term_id: HP:0000252
    reported_labels:
    - congenital/postnatal
    ontology_label: Microcephaly
  - term_id: HP:0001382
    reported_labels:
    - childhood
    ontology_label: Joint hypermobility
  - term_id: HP:0000729
    reported_labels:
    - childhood
    ontology_label: Autistic behavior
  - term_id: HP:0000389
    reported_labels:
    - childhood, recurrent
    ontology_label: Chronic otitis media
  - term_id: HP:0001250
    reported_labels:
    - variable
    ontology_label: Seizure
  - term_id: HP:0001321
    reported_labels:
    - congenital
    ontology_label: Cerebellar hypoplasia
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability, X-linked, Syndromic 33
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability, X-linked, Syndromic 33** covering all of the
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

I'll research X-linked syndromic intellectual disability 33 (TAF1-related), using PubMed and web resources. First, let me load the research tools.

The cached JCI reference turned out to be a TAB2 paper — unrelated to this disease. Now searching PubMed for the TAF1/MRXS33 literature.

The PubMed MCP tools aren't permitted in this session, so I'll use web search and NCBI E-utilities via WebFetch instead.

OMIM #300966 confirmed. Now fetching abstracts for the 21 PubMed hits in two batches.

Key literature identified. Now pulling verbatim abstracts for the core papers and confirming ontology identifiers.

MONDO:0010500 confirmed. Now getting the OMIM clinical detail, PMC IDs for full-text access to the 2024 review, and a broader search for additional case reports.

Excellent — found the congenital heart defect paper (Morton 2020) and the open-access 2024 review. Fetching full-text detail from the review and the founding O'Rawe paper.

Now filling in the remaining core abstracts (Cheng 2019, Morton 2020, Okamoto 2020, Hurst 2018) and checking Orphanet.

One more round to capture the remaining abstracts verbatim (Okamoto sibling report, zebrafish and mouse model papers).

All core research is gathered. One quick identifier verification for the TAF1 gene record, then I'll write the report.

All research complete. Here is the comprehensive report.

---

# Research Report: Intellectual Disability, X-linked, Syndromic 33 (MRXS33; TAF1 Intellectual Disability Syndrome)

**Prepared:** 2026-09-04 · **Sources:** OMIM, PubMed/PMC (NCBI E-utilities), OLS/MONDO, HGNC, ClinVar/GTR listings. All PMIDs verified against PubMed during this session. Ontology IDs marked "(suggest)" are curation leads and must be re-verified against OLS/OAK before binding.

---

## 1. Disease Information

**Overview.** X-linked syndromic intellectual developmental disorder-33 (MRXS33), also called TAF1 intellectual disability syndrome or TAF1 syndrome, is an ultra-rare X-linked recessive neurodevelopmental disorder caused by hemizygous mutation of *TAF1* (TATA-box binding protein associated factor 1) at Xq13.1. Affected males show global developmental delay evolving into intellectual disability, generalized hypotonia, characteristic facial dysmorphism, a highly distinctive gluteal crease anomaly with sacral caudal remnant, variable neurologic features (hearing loss, strabismus, corpus callosum hypoplasia, seizures), and — in about half of individuals with damaging missense variants — congenital heart defects. The founding description is O'Rawe et al. 2015: *"We describe an X-linked genetic syndrome associated with mutations in TAF1 and manifesting with global developmental delay, intellectual disability (ID), characteristic facial dysmorphology, generalized hypotonia, and variable neurologic features"* (PMID:26637982, Am J Hum Genet, doi:10.1016/j.ajhg.2015.11.005).

**Identifiers.**
| Resource | ID |
|---|---|
| OMIM (phenotype) | **#300966** — INTELLECTUAL DEVELOPMENTAL DISORDER, X-LINKED, SYNDROMIC 33; MRXS33 ([omim.org/entry/300966](https://www.omim.org/entry/300966)) |
| MONDO | **MONDO:0010500** — "intellectual disability, X-linked, syndromic 33" (verified via OLS this session) |
| OMIM (gene) | 313650 (*TAF1*) |
| UMLS / GTR | C4225418 ([GTR condition page](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4225418/)) |
| Orphanet | No dedicated ORPHA entry found (falls under non-specific syndromic ID groupings; searched this session) |
| ICD-10/ICD-11 | No disease-specific code; coded under intellectual disability (F70–F79 / 6A00) plus malformation codes |

**Synonyms.** MRXS33; TAF1 syndrome; TAF1/MRXS33 intellectual disability syndrome; TAF1-related neurodevelopmental disorder. Note: **Abidi syndrome** (historically a distinct XLID lumped at Xq12-q21) was recently shown to be TAF1-related — Han et al. 2026 found segregating TAF1 variants in the original Abidi syndrome family with functional impact (PMID:42548218).

**Data derivation.** All knowledge is aggregated from case series and family reports (~50–70 families cumulatively across O'Rawe 2015 [11 families], Cheng 2019 [27 additional families], Morton 2020 [26 individuals with damaging missense variants], plus single-family reports). No registry, EHR-derived cohort, or natural history study exists.

---

## 2. Etiology

**Causal factor: monogenic.** Hemizygous *TAF1* variants in males: missense SNVs (the large majority), rare splice-site variants, a start-loss (p.Met1?, Abidi syndrome family; PMID:42548218), and ~0.42 Mb Xq13.1 **duplications** encompassing *TAF1* (two families in O'Rawe 2015; these produce phenotypic overlap *"but they also demonstrated a severe neurodegeneration phenotype"*; PMID:26637982). No null (complete loss-of-function) hemizygous variants have been reported in living males; mouse data suggest nullizygosity is embryonic-lethal: *"We discovered that Taf1 deletion in male mice was embryonically lethal, which may explain why no null variants have been identified in humans"* (Crombie et al. 2024, Dis Model Mech; PMID:38804708).

**Genetic risk factors.** Being male and hemizygous; having a carrier mother (roughly half of reported variants are maternally inherited, half de novo — Morton 2020 found 14 de novo vs 12 maternally inherited damaging missense variants; PMID:32396742). Modifier genes: none identified. Susceptibility loci: none (fully penetrant Mendelian in males, so far as reported).

**Environmental risk/protective factors.** None known; no environmental contribution to causation has been reported. **Protective factor (females):** skewed X-chromosome inactivation silencing the mutant allele protects heterozygous carriers — *"female carriers of TAF1 mutations and duplications demonstrate highly skewed inactivation (99:1)"* (O'Rawe 2015 full text, PMID:26637982); conversely, extreme skewing toward the mutant allele can produce affected females (Vianna 2020: *"XLID-potentially related variants were identified in five patients with extreme XCI skewing, including four single nucleotide variants in NLGN4X, HDAC8, TAF1, and USP9X genes"*; PMID:32564284).

**Gene–environment interaction.** None documented.

---

## 3. Phenotypes

Frequencies below are from the founding 14-proband series (O'Rawe 2015 full text; PMID:26637982) unless noted; Cheng 2019 (PMID:31646703) added *"brain morphological abnormalities, seizures, hearing loss, and heart malformations"* as *"prominent among previously unreported effects."* Suggested HP terms need OLS verification before binding.

| Phenotype | Type | Freq (O'Rawe) | Onset / course | HP suggestion |
|---|---|---|---|---|
| Global developmental delay | clinical sign | 14/14 | infancy; static → ID | HP:0001263 |
| Intellectual disability | clinical sign | 14/14 | childhood; lifelong, largely stable | HP:0001249 |
| Delayed speech and language | clinical sign | 13/14 | early childhood | HP:0000750 |
| Generalized hypotonia | sign | 13/14 | neonatal/infantile | HP:0001290 (generalized hypotonia) |
| Unusual gluteal crease with **sacral caudal remnant** / sacral dimple | physical | 12/14 | congenital; *"spine MRI showed no major underlying defects"* | HP:0000960 (sacral dimple); no precise HP for caudal remnant — keep free-text preferred_term |
| Oral-pharyngeal dysphagia | sign | 11/14 | infancy | HP:0200136 (oral-pharyngeal dysphagia) |
| Hypoplasia of corpus callosum (MRI) | imaging | 11/14 | congenital | HP:0002079 |
| Hearing impairment | sensory | 10/14 | childhood | HP:0000365 |
| Strabismus | sign | 10/14 | childhood | HP:0000486 |
| Microcephaly | physical | 10/14 | congenital/postnatal | HP:0000252 |
| Joint hypermobility | sign | 10/14 | childhood | HP:0001382 |
| Autistic behaviors / ASD | behavioral | 10/14 | childhood | HP:0000729 |
| Chronic otitis media | sign | 9/14 | childhood, recurrent | HP:0000389 |
| Facial gestalt: prominent supraorbital ridges, downslanted palpebral fissures, deep-set eyes, **sagging cheeks**, long philtrum, low-set protruding ears, long face, high palate, pointed chin, anteverted nares | physical | majority | congenital | HP:0000336, HP:0000494, HP:0000490, HP:0000343, HP:0000369/HP:0000411, HP:0000276, HP:0000218, HP:0000307, HP:0000463 |
| Intrauterine and/or postnatal growth retardation | physical | "most" (OMIM description) | prenatal/infancy | HP:0001511, HP:0008897 |
| Seizures | sign | subset (Cheng 2019) | variable | HP:0001250 |
| Congenital heart defects (ASD, VSD, coarctation, pulmonary stenosis, tetralogy of Fallot) | physical | **50% (13/26)** of damaging-missense carriers (Morton 2020) | congenital | HP:0001631, HP:0001629, HP:0001680, HP:0001642, HP:0001636 |
| Spastic diplegia, dystonic movements, tremor | sign | variable/subset | childhood | HP:0001264, HP:0001332, HP:0001337 |
| Cerebellar hypoplasia | imaging | single cases (Hurst 2018) | congenital | HP:0001321 |
| Progressive neurodegeneration, death from cardiopulmonary insufficiency | course | duplication families only | childhood, progressive | — |

**Quality of life.** No formal QoL instrument (EQ-5D/PROMIS) study exists. Functionally dominant burdens: communication impairment (speech delay near-universal), feeding difficulty in infancy (dysphagia in ~79%), conductive/sensorineural hearing loss requiring intervention, and lifelong support needs from ID. This is a gap to record as such.

---

## 4. Genetic/Molecular Information

**Gene.** *TAF1* — TATA-box binding protein associated factor 1; **HGNC:11535** (dismech form `hgnc:11535`); Xq13.1; NCBI Gene 6872; Ensembl ENSG00000147133; UniProt P21675; OMIM gene 313650 (verified via HGNC REST this session). Encodes the largest subunit (1,873 aa, ~250 kDa) of the general transcription factor TFIID complex (Crombie review, PMID:39323550).

**Pathogenic variants.** From O'Rawe 2015 (numbering per that paper's transcript): p.Ile1337Thr (maternal), p.Cys807Arg (de novo), p.Arg1246Trp (de novo), p.Ile505Asn (de novo), a splice variant producing p.Arg1228Ilefs\*16 (maternal), p.Asn1517His (de novo), p.Arg1431His (de novo), p.Pro596Ser (maternal), p.Asp976His (de novo), plus two ~0.42 Mb Xq13.1 duplications (PMID:26637982). **Caution on numbering:** ClinVar records the same missense variants under NM_004606.5 with shifted residue numbers (e.g., [p.Ile1317Thr, RCV000203524](https://www.ncbi.nlm.nih.gov/clinvar/RCV000203524.5/); [p.Arg1226Trp, RCV000203515](https://www.ncbi.nlm.nih.gov/clinvar/RCV000203515/); [p.Lys1556Glu, RCV001027762](https://www.ncbi.nlm.nih.gov/clinvar/RCV001027762/)) — a curation trap; always anchor to a stated transcript. Cheng 2019 added 27 families of largely missense variants and emphasized *"the challenges for determining the pathogenicity of inherited missense variants, particularly for genes mapping to chromosome X"* (PMID:31646703). Han 2026 added p.Met1? and p.Gln1429Pro (Abidi syndrome and a second XLID family; PMID:42548218). Li 2024 reported c.2233T>G segregating in a Chinese XLID pedigree (PMID:38684296). Recurrent site: p.Arg1170Cys *"has been reported in four separate XLID studies"* (Crombie review, PMID:39323550).

- **Classification:** ClinVar holds pathogenic/likely pathogenic and VUS assertions; many inherited missense variants remain contested (the central theme of PMID:31646703).
- **Variant classes:** missense ≫ splice-site > start-loss; duplications (CNV); **no truncating/null variants in males** — consistent with essentiality (PMID:38804708).
- **Origin:** germline; de novo and maternally inherited in roughly equal measure (PMID:32396742). Somatic *TAF1* mutations occur in cancers (e.g., gastric/colorectal frameshifts, PMID:27571988) but are unrelated to MRXS33.
- **Population frequency:** pathogenic variants absent/ultra-rare in gnomAD; gene is strongly constrained against LoF (inferred; verify constraint metrics at gnomAD during curation).
- **Functional consequence:** partial loss of function / hypomorphic missense effects on TFIID assembly and partner binding (TAF7-interface variants p.Cys807Arg, p.Pro596Ser, p.Asp976His, p.Arg1246Trp *"map to conserved domains critical for TAF1–TAF7 binding"*; p.Cys807Arg *"would destabilize the triple-barrel fold"* — O'Rawe full text). Duplications act by dosage increase with a distinct, degenerative phenotype.

**Modifier genes.** None known. **Epigenetics.** X-inactivation state is the decisive epigenetic modifier in females (99:1 skewing in asymptomatic carriers, PMID:26637982; 90:10 skew detected by RNA-seq in a carrier mother, PMID:32714589). **Chromosomal abnormalities.** The Xq13.1 microduplications above; detectable by CMA/DECIPHER.

**Allelic but distinct disorder.** X-linked dystonia-parkinsonism (XDP/DYT3, OMIM 314250) is caused not by coding variants but by a ~2.6 kb SVA-F retrotransposon insertion in *TAF1* intron 32, whose (CCCTCT)n hexameric repeat length inversely correlates with age of onset (Bragg 2017, PNAS; PMID:29229810). Keep XDP as a separate disease entry; it is mechanistic context, not MRXS33.

---

## 5. Environmental Information

Not applicable: no environmental, lifestyle, or infectious contributors to causation are documented for this Mendelian disorder. (Record as an explicit negative in the KB rather than leaving blank.)

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered; inferential steps flagged):**

1. Hemizygous *TAF1* missense/splice variant (or Xq13.1 duplication) **leads to** altered TAF1 protein function or dosage — demonstrated at the structural level for TAF7-interface and bromodomain residues (PMID:26637982; PMID:39323550).
2. Altered TAF1 **results in** impaired TFIID scaffold assembly/promoter engagement and dysregulated RNA polymerase II transcription initiation — TAF1 *"functions as a scaffold, contributing to the assembly and maintaining the structural integrity of TFIID"* (PMID:39323550); reduced RAP74 (GTF2F1) phosphorylation in patient lymphoblasts (PMID:42548218) supports a general-transcription-machinery defect (mechanistic step partly inferred; the once-reported intrinsic kinase/HAT/ubiquitination activities of TAF1 *"could not be reproduced by others and much of the related work…has been retracted"* — PMID:39323550).
3. Transcriptional dysregulation **leads to** downregulation of specific neurodevelopmental gene programs — patient RNA-seq showed 213 differentially expressed genes (179 down), with *"a significant enrichment of genes regulated by E-box proteins"* (PMID:26637982); zebrafish knockout transcriptomes were *"enriched for genes associated with neurodevelopmental processes"* (PMID:31341187); patient-variant cells showed differential expression of *"neuronal ion channel genes"* and *"the TAF1 variant may impair neuronal differentiation and cell proliferation"* (PMID:32714589).
4. Disrupted neurodevelopmental transcription **results in** abnormal brain development — microcephaly, corpus callosum hypoplasia, cerebellar hypoplasia in patients (PMID:26637982; PMID:32714589); in rat, *"Deletion of TAF1 lead to a hypoplasia and loss of the Purkinje cells"* with *"loss of pre-synaptic CaV3.1"* T-type calcium channels driving *"irregular cerebellar output"* (PMID:31344492) (model-organism evidence; human confirmation at circuit level absent — a HUMAN_MODEL_MISMATCH candidate).
5. Abnormal brain development and neuronal dysfunction **lead to** the clinical phenotype: global developmental delay → intellectual disability ± ASD, hypotonia, motor abnormalities (PMID:26637982; PMID:31646703).
6. **Branch (cardiac):** the same transcriptional insufficiency in cardiogenesis **results in** congenital heart defects in ~50% of damaging-missense carriers (PMID:32396742); supported by zebrafish *taf1/taf5* mutants phenocopying *"cardiac and craniofacial abnormalities…through perturbations in metabolism"* (PMID:37746814) and by TAF1 bromodomain inhibition in cardiomyocytes altering mitochondrial/proliferation/differentiation gene programs (PMID:36958711).
7. **Branch (dosage-increase):** *TAF1* duplication **leads to** a severe, progressive neurodegenerative course rather than static ID (PMID:26637982) — direction of dosage effect matters; mechanism unknown.
8. **Downstream signaling correlate (model-only, inferred):** TAF1 loss in rat **results in** depressed BDNF/AKT/GSK3β signaling; the T-type channel enhancer SAK3 *"restored the Brain-derived neurotrophic factor/protein kinase B/Glycogen Synthase Kinase 3 Beta (BDNF/AKT/GSK3β) signaling axis"* (PMID:33359140).

**Annotations for curation:** TFIID complex (GO:0005669, suggest); RNA Pol II transcription initiation (GO:0006367, suggest); TBP binding via TAND domain; double bromodomain reading of acetylated histones (*"acetylated, butyrylated and crotonylated lysines"*, PMID:39323550); zinc-knuckle DNA binding for promoter occupancy (PMID:29545534). Cell types: Purkinje cell (CL:0000121, suggest), cardiomyocyte, neural progenitors. Biological scale: MOLECULAR (TFIID dysfunction) → CELLULAR (impaired neuronal differentiation) → TISSUE (CC/cerebellar hypoplasia, septal defects) → ORGANISM (ID, CHD).

---

## 7. Anatomical Structures Affected

- **Primary:** brain (UBERON:0000955) — cerebral cortex, corpus callosum (UBERON:0002336), cerebellum (UBERON:0002037; Purkinje layer in models).
- **Cardiac:** heart (UBERON:0000948) — atrial/ventricular septa, outflow tract (ToF, coarctation, pulmonic stenosis) (PMID:32396742).
- **Craniofacial skeleton and ears:** facial dysmorphism; middle ear (chronic otitis media); cochlea/auditory pathway (hearing impairment).
- **Musculoskeletal/other:** generalized skeletal muscle hypotonia, joints (hypermobility), sacrococcygeal region (gluteal crease anomaly/sacral caudal remnant), oropharynx (dysphagia), eyes (strabismus, deep-set eyes).
- **Subcellular:** nucleus — TFIID at RNA Pol II core promoters (GO:0005634 / GO:0005669, suggest).
- **Lateralization:** findings are bilateral/midline; no lateralized pattern reported.

---

## 8. Temporal Development

- **Onset:** congenital/infantile. IUGR in a subset; hypotonia and feeding difficulty neonatally; developmental delay evident in the first year; per Cheng 2019 the syndrome *"present[s] early in life with hypotonia, facial dysmorphia, and developmental delay that evolved into intellectual disability (ID) and/or autism spectrum disorder (ASD)"* (PMID:31646703).
- **Progression:** for SNV cases, largely **static** ID (non-degenerative); motor milestones delayed but attained variably. **Exception:** Xq13.1 duplication cases show *"severe and progressive neurodegeneration"* (PMID:26637982).
- **Course pattern:** chronic lifelong; seizures episodic in the affected subset.
- **Critical periods:** embryonic (cardiogenesis; CHD is congenital) and early postnatal neurodevelopment — in rat, Taf1 knockdown at P0 produced *"a stronger phenotype…compared with at three weeks after birth"* (model evidence; PMID:39323550 review of AAV-miRNA work), suggesting an early postnatal vulnerability window.
- **Remission:** not applicable.

---

## 9. Inheritance and Population

- **Prevalence/incidence:** unknown; ultra-rare. Cumulative literature ≈ 50–70 families worldwide (11 families PMID:26637982; +27 families PMID:31646703; 26 individuals in CHD cohorts PMID:32396742 with overlap unclear; plus single-family reports PMID:30805980, PMID:38684296, PMID:42548218, PMID:31341187). For dismech `prevalence_class`: qualitative `ULTRA_RARE` / `CASES_IN_LITERATURE`.
- **Inheritance:** X-linked recessive. De novo and maternally inherited variants both common. All 14 O'Rawe probands male; *"All of the mutations reported here, including the duplications, are de novo or co-segregate with phenotype in affected males"* (PMID:26637982 full text).
- **Penetrance:** apparently complete in hemizygous males for reported pathogenic variants; **incomplete in females**, governed by XCI. Carrier mothers typically asymptomatic with 99:1 skewing (PMID:26637982); rare symptomatic females have extreme skewing toward the mutant X (PMID:32564284) or carry variants plus cardiac/developmental findings (Crombie review, PMID:39323550).
- **Expressivity:** variable — *"considerable pleiotropy and clinical variability"* (PMID:31646703).
- **Anticipation / germline mosaicism / founder effects / consanguinity:** none reported. (XDP's Panay founder effect belongs to the allelic disorder, not MRXS33.)
- **Carrier frequency:** not established; too rare.
- **Demographics:** male-predominant (M≫F); families reported from North America, Europe, Japan (PMID:30805980), China (PMID:38684296), Turkey, Brazil — no ethnic clustering.

---

## 10. Diagnostics

- **Primary modality: molecular genetic testing.** Trio WES/WGS is the effective route (genotype-first identification dominates the literature: PMID:31646703; WGS + RNA-seq resolved a case where *"the genome sequence data failed to implicate a candidate gene"* — PMID:32714589). *TAF1* is on XLID multigene panels (GTR; GenCC has PanelApp Australia submissions).
- **CMA:** detects the Xq13.1 duplications (DECIPHER-class CNVs) (PMID:26637982).
- **Adjunct omics:** RNA-seq of blood can reveal skewed XCI and support variant interpretation (PMID:32714589).
- **XCI studies:** informative for carrier-female counseling (PMID:26637982; PMID:32564284).
- **Ancillary clinical work-up:** brain MRI (CC hypoplasia, cerebellar hypoplasia), echocardiography (given 50% CHD in damaging-missense carriers — PMID:32396742), audiology, ophthalmology, EEG if seizures, swallow evaluation, spine MRI for the sacral anomaly (typically normal underlying anatomy — PMID:26637982).
- **Biomarkers:** none validated for MRXS33. (Reduced RAP74 phosphorylation is a research assay — PMID:42548218.)
- **Diagnostic criteria:** none published; diagnosis is molecular plus phenotype fit.
- **Differential diagnosis:** Cornelia de Lange–like syndromes — *"Causative variants in additional genes, such as ANKRD11, EP300, AFF4, TAF1, and BRD4, can cause a CdLS-like phenotype"* (PMID:37377026; also PMID:35842780); Dubowitz syndrome phenocopies (de novo TAF1 among alternative diagnoses — PMID:33098347); other XLID syndromes (PMID:25644381); XDP in adults is clinically and mechanistically distinct.
- **Newborn/carrier screening:** not performed; cascade carrier testing of mothers/female relatives after proband diagnosis.

---

## 11. Outcome / Prognosis

- **Survival:** no systematic data. Missense-variant males generally survive into at least adolescence/adulthood in reported families (multigenerational pedigrees exist — five-generation family in PMID:31341187; Abidi syndrome family PMID:42548218). One death from *"cardiopulmonary insufficiency"* in a duplication case (PMID:26637982).
- **Morbidity/function:** lifelong intellectual disability with communication impairment; ASD in a majority of the founding series; hearing loss and chronic otitis media add communication burden; CHD subset carries surgical morbidity.
- **Prognostic factors:** variant class is the clearest — **duplication → progressive neurodegenerative course; missense → static ID** (PMID:26637982). CHD presence and severity drive early morbidity (PMID:32396742). In females, XCI ratio predicts expression (PMID:32564284).
- **Recovery potential:** none for the ID; developmental gains occur with age and therapy but no formal natural-history quantification exists.
- **QoL measures:** no published EQ-5D/SF-36/PROMIS data — record as a knowledge gap.

---

## 12. Treatment

No disease-modifying therapy exists; management is supportive and multidisciplinary. NCIT suggestions per dismech convention (verify reachability from NCIT:C25218):

| Intervention | Basis | NCIT suggestion |
|---|---|---|
| Early developmental intervention; special education | standard of care for syndromic ID | Rehabilitation NCIT:C15315 |
| Speech therapy | near-universal speech delay | Speech Therapy NCIT:C159273 |
| Physical / occupational therapy | hypotonia, motor delay | Physical Therapy NCIT:C15302; Occupational Therapy NCIT:C121351 |
| Feeding therapy ± gastrostomy in severe dysphagia | dysphagia 11/14 | Supportive Care NCIT:C15747 |
| Hearing management: tympanostomy for chronic otitis media, hearing aids | hearing impairment 10/14 | Surgical Procedure NCIT:C15329 + device qualifier pattern |
| Strabismus management | strabismus 10/14 | Therapeutic Procedure NCIT:C49236 |
| Antiseizure medication where epilepsy present | seizures (PMID:31646703) | Pharmacotherapy NCIT:C15986 |
| Congenital heart defect repair | CHD in 50% of damaging-missense carriers (PMID:32396742) | Surgical Procedure NCIT:C15329 |
| Genetic counseling for family | X-linked recessive risk | Genetic Counseling NCIT:C15240 |

**Experimental (preclinical only).** The T-type Ca²⁺ channel enhancer **SAK3** in the rat Taf1-editing model: *"Oral administration of SAK3 (0.25 mg/kg, p.o.) significantly rescued the behavior abnormalities in beam walking test and open field test caused by TAF1 gene editing"* and *"restored the excitatory post synaptic current (sEPSCs) in TAF1 edited Purkinje cells"* (PMID:32622085); it also *"restored the…BDNF/AKT/GSK3β signaling axis"* (PMID:33359140). Evidence_source: MODEL_ORGANISM; no human trials. **No MRXS33 clinical trials found** on the standard registries during this research pass (worth re-checking ClinicalTrials.gov at curation time). Pharmacogenomics: none.

---

## 13. Prevention

- **Primary prevention:** none possible (genetic).
- **Genetic counseling:** X-linked recessive recurrence risk — 50% of sons of carrier mothers affected, 50% of daughters carriers; de novo cases carry low recurrence risk (germline mosaicism not excluded). NSGC/ACMG-standard cascade testing of maternal female relatives; XCI testing refines female risk discussion (PMID:26637982).
- **Reproductive options:** prenatal diagnosis and preimplantation genetic testing once the familial variant is known (standard practice for XLID; no disease-specific guideline exists).
- **Secondary/tertiary:** early echocardiogram and audiology after diagnosis to pre-empt CHD and hearing/language complications; otitis media surveillance.
- **Population screening/immunization/public health:** not applicable.

---

## 14. Other Species / Natural Disease

- **Natural disease:** no naturally occurring TAF1-deficiency disease is documented in companion animals or wildlife (no OMIA phene found in this research pass — verify at curation).
- **Orthologs:** *TAF1* is deeply conserved — mouse *Taf1*, rat *Taf1*, zebrafish *taf1*, Drosophila *Taf1*, and yeast *TAF1/Bdf1* function is conserved down to fungi (yeast Bdf1/TAF1 conserved roles in homologous recombination — PMID:34056863; yeast Taf1 promoter biology — PMID:32182349). The neuron-specific microexon 34′ (N-TAF1) *"incorporates the same microexon"* across species (PMID:39323550).
- **Comparative note:** embryonic lethality of complete loss is shared across zebrafish (PMID:31341187) and mouse (PMID:38804708), arguing for strong evolutionary constraint of the TFIID scaffold role.
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

| Model | System | Key findings | Fidelity notes |
|---|---|---|---|
| **Zebrafish taf1 KO/knockdown** (Gudmundsson 2019, PMID:31341187) | CRISPR null + morpholino | Null = embryonic lethal; *"intact taf1 is essential for embryonic development"*; transcriptome *"enrichment for genes associated with neurodevelopmental processes"*; morphant microencephaly (reduced optic tectum) rescued by human wild-type *TAF1* mRNA | Recapitulates microcephaly/neurodevelopmental axis; null state has no human counterpart |
| **Zebrafish taf1/taf5 mutants** (Leid 2023, PMID:37746814) | CRISPR | *"defects…phenocopied by mutations in taf1 and taf5"* — cardiac and craniofacial abnormalities via metabolic gene misregulation | Supports the CHD branch; metabolism link not shown in humans |
| **Rat Taf1 CRISPR editing** (Janakiraman 2019, PMID:31344492) | Postnatal intracerebroventricular CRISPR | *"behavioral deficits at both the neonatal and juvenile stages"*; Purkinje cell hypoplasia/loss; loss of presynaptic CaV3.1; abnormal cerebellar output | Regional/postnatal editing, not germline hemizygous missense — supraphysiological lesion; useful for cerebellar mechanism and SAK3 pharmacology (PMID:32622085, PMID:33359140) |
| **Mouse Taf1 KO** (Crombie 2024, PMID:38804708) | Ubiquitous knockout | Male null embryonic-lethal (E3.5→E9.5 window); heterozygous females: *"significant increase in weight…and reduced movement"* | Explains absence of human null males; het female phenotype only partially parallels human carrier females |
| **Patient-variant cell models** (Hurst 2018, PMID:32714589) | SH-SY5Y (WT vs TAF1 deletion vs p.Ser1600Gly) | Differential expression of *"neuronal ion channel genes"*; *"may impair neuronal differentiation and cell proliferation"* | IN_VITRO; neuroblastoma line, not patient iPSC-derived neurons |
| **Patient lymphoblasts** (Han 2026, PMID:42548218) | LCLs with p.Met1?/p.Gln1429Pro | *"reduced phosphorylation of RAP74"* | Human-derived IN_VITRO mechanistic readout |
| **iPSC (XDP context)** (D'Ignazio 2022, PMID:35868859) | Female-carrier iPSC | TAF1 expression variation relevant to neostriatal vulnerability | XDP, not MRXS33 — do not conflate |

**Resources:** MGI/IMPC for *Taf1* mouse alleles; ZFIN for *taf1* zebrafish lines; SFARI Gene lists TAF1 as an autism candidate ([gene.sfari.org](https://gene.sfari.org/database/human-gene/TAF1)).

---

## Key Citations (PMID · first author · year · contribution)

- **26637982** O'Rawe 2015, Am J Hum Genet — founding description, 14 males/11 families, phenotype frequencies, XCI 99:1, E-box transcriptome signature (doi:10.1016/j.ajhg.2015.11.005)
- **31646703** Cheng 2019, Hum Mutat — +27 families; seizures, hearing loss, heart malformations, brain morphological abnormalities; pathogenicity challenges (doi:10.1002/humu.23936)
- **32396742** Morton 2020, Circ Genom Precis Med — CHD in 50% (13/26) of damaging missense carriers
- **39323550** Crombie 2024, R Soc Open Sci — comprehensive TAF1 review; retracted enzymatic-activity literature flagged (doi:10.1098/rsos.240790)
- **38804708** Crombie 2024, Dis Model Mech — Taf1 KO mouse; male embryonic lethality
- **31341187** Gudmundsson 2019, Sci Rep — zebrafish knockout; human mRNA rescue
- **37746814** Leid 2023, Biol Open — zebrafish taf1/taf5 cardiac/craniofacial phenocopy
- **31344492 / 32622085 / 33359140** Janakiraman 2019/2020, Dhanalakshmi 2021, Neurobiol Dis — rat model; Purkinje/CaV3.1; SAK3 rescue; BDNF/AKT/GSK3β
- **32714589** Hurst 2018, Neuronal Signal — p.Ser1600Gly; WGS+RNA-seq diagnostics; ion-channel gene dysregulation
- **42548218** Han 2026, Am J Med Genet A — Abidi syndrome is TAF1-related; reduced RAP74 phosphorylation
- **32564284** Vianna 2020, Mol Neurobiol — affected females via extreme XCI skewing
- **30805980** Okamoto 2020 · **38684296** Li 2024 · **25644381** Hu 2016 — additional families/cohorts
- **37377026** Kaur 2023 · **35842780** Coursimault 2022 · **33098347** Dyment 2021 — CdLS-like/Dubowitz differential diagnosis
- **29229810** Bragg 2017, PNAS — XDP SVA hexameric repeat (allelic disorder context)
- **36958711** Leigh 2023, BBA Mol Basis Dis — TAF1 bromodomain inhibition and CHD epigenetics

**Curation caveats for this report:** (1) all snippets above must be re-verified against `references_cache` after `just fetch-reference` — several were extracted through an intermediary summarization step; (2) variant residue numbering differs between O'Rawe 2015 and ClinVar NM_004606.5 records; (3) all suggested HP/GO/CL/UBERON/NCIT IDs require OLS verification; (4) the modified `references_cache/DOI_10.1172_jci152297.md` in this worktree is a TAB2 cardiomyopathy paper unrelated to this disease.

Sources:
- [OMIM #300966 — MRXS33](https://www.omim.org/entry/300966)
- [ClinVar RCV000203524 — TAF1 p.Ile1317Thr](https://www.ncbi.nlm.nih.gov/clinvar/RCV000203524.5/)
- [ClinVar RCV000203515 — TAF1 p.Arg1226Trp](https://www.ncbi.nlm.nih.gov/clinvar/RCV000203515/)
- [ClinVar RCV001027762 — TAF1 p.Lys1556Glu](https://www.ncbi.nlm.nih.gov/clinvar/RCV001027762/)
- [GTR condition C4225418](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4225418/)
- [GenCC — TAF1 / MRXS33 (PanelApp Australia)](https://thegencc.org/submissions/SGC-121454.1)
- [NORD MONDO disease page](https://rarediseases.org/mondo-disease/intellectual-disability-x-linked-syndromic-33/)
- [Crombie 2024 review — Royal Society Open Science](https://royalsocietypublishing.org/rsos/article/11/9/240790/92804/The-roles-of-TAF1-in-neuroscience-and-beyondThe)
- [O'Rawe 2015 — PMC4678794](https://pmc.ncbi.nlm.nih.gov/articles/PMC4678794/)
- [Morton 2020 — PMC7329268](https://pmc.ncbi.nlm.nih.gov/articles/PMC7329268/)
- [Hurst 2018 — PMC7373232](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7373232/)
- [Gudmundsson 2019 — Scientific Reports](https://www.nature.com/articles/s41598-019-46632-8)
- [SFARI Gene — TAF1](https://gene.sfari.org/database/human-gene/TAF1)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 32 |
| On topic | 22 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (1 mention) - the report calls it "infancy; static → ID"; HP calls it **Global developmental delay**
- `HP:0001249` (1 mention) - the report calls it "childhood; lifelong, largely stable"; HP calls it **Intellectual disability**
- `HP:0000750` (1 mention) - the report calls it "early childhood"; HP calls it **Delayed speech and language development**
- `HP:0002079` (1 mention) - the report calls it "congenital"; HP calls it **Hypoplasia of the corpus callosum**
- `HP:0000365` (1 mention) - the report calls it "childhood"; HP calls it **Hearing impairment**
- `HP:0000486` (1 mention) - the report calls it "childhood"; HP calls it **Strabismus**
- `HP:0000252` (1 mention) - the report calls it "congenital/postnatal"; HP calls it **Microcephaly**
- `HP:0001382` (1 mention) - the report calls it "childhood"; HP calls it **Joint hypermobility**
- `HP:0000729` (1 mention) - the report calls it "childhood"; HP calls it **Autistic behavior**
- `HP:0000389` (1 mention) - the report calls it "childhood, recurrent"; HP calls it **Chronic otitis media**
- `HP:0001250` (1 mention) - the report calls it "variable"; HP calls it **Seizure**
- `HP:0001321` (1 mention) - the report calls it "congenital"; HP calls it **Cerebellar hypoplasia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000955` (1 mention) - the report calls it "Primary:** brain"; UBERON calls it **brain**
- `UBERON:0000948` (1 mention) - the report calls it "Cardiac:** heart"; UBERON calls it **heart**, and lists "chambered heart" among its other names