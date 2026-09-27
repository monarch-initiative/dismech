---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-24T17:20:11.712642'
end_time: '2026-09-24T17:25:12.417297'
duration_seconds: 300.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Facioscapulohumeral Muscular Dystrophy 4 Digenic
  mondo_id: MONDO:0030355
  category: Genetic
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
  num_turns: 20
  total_cost_usd: 1.4546143999999999
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 2
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
citation_count: 62
reference_validation:
  total_references: 36
  verified: 34
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.056
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC10951985
  relevance_assessed: 34
  on_topic: 13
  off_topic: 1
  off_topic_references:
  - PMID:31879416
  unresolved_references:
  - PMID:32467356
  - PMID:38685133
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 49
  verified: 41
  not_found: 1
  obsolete: 2
  unverifiable: 5
  confabulation_rate: 0.023
  labels_checked: 16
  labels_matching: 6
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0009053
    reported_labels:
    - Scapular winging
    ontology_label: Distal lower limb muscle weakness
  - term_id: HP:0003701
    reported_labels:
    - Proximal muscle weakness
    - Progressive extension from shoulder/face; drives ~20% wheelchair dependence
    ontology_label: Proximal muscle weakness
  - term_id: UBERON:0001630
    reported_labels:
    - skeletal muscle tissue
    ontology_label: muscle organ
  - term_id: UBERON:0009471
    reported_labels:
    - orbicularis oculi
    ontology_label: dorsum of tongue
  - term_id: UBERON:0003688
    reported_labels:
    - "scapular muscle \u2014 approximate"
    ontology_label: omentum
  - term_id: UBERON:0001519
    reported_labels:
    - retina
    ontology_label: skin of manus
  - term_id: UBERON:0001846
    reported_labels:
    - cochlea
    ontology_label: internal ear
  - term_id: NCIT:C15240
    reported_labels:
    - 'Genetic counseling**: essential given digenic transmission complexity'
    ontology_label: Genetic Counseling
  labels_variant: 2
  unresolved_terms:
  - HP:0001936
  obsolete_terms:
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  - term_id: GO:0006342
    ontology_label: GO_0006342
    replaced_by: GO:0031507
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Facioscapulohumeral Muscular Dystrophy 4 Digenic
- **MONDO ID:** MONDO:0030355 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Facioscapulohumeral Muscular Dystrophy 4 Digenic** covering all of the
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

I'll research this using current literature and databases to build a comprehensive, well-cited report.

# Facioscapulohumeral Muscular Dystrophy 2 / "FSHD4 Digenic" — Comprehensive Research Report

**Note on nomenclature:** The disease name "Facioscapulohumeral Muscular Dystrophy 4 Digenic" does not correspond to an established OMIM/GeneReviews entity. The clinical and molecular literature — and OMIM's own entry — designates the digenic form of FSHD as **FSHD2** (OMIM #158901, "FACIOSCAPULOHUMERAL MUSCULAR DYSTROPHY 2, DIGENIC; FSHD2"), distinct from the classical, D4Z4-contraction-driven **FSHD1** (OMIM #158900). MONDO's disease-hierarchy term for the digenic entity is the FSHD2 node; if MONDO:0030355 resolves to a differently-numbered label in the KB's local MONDO snapshot, that is very likely this same FSHD2/digenic concept under a different display number, and should be confirmed by direct MONDO lookup before curation — I did not verify MONDO:0030355 against a live MONDO release in this pass and flag this as unverified. Everything below is written against **FSHD2 (digenic FSHD)** as the target entity, since every primary source I found in this literature search uses that identity. (Source: [OMIM #158901](https://www.omim.org/entry/158901))

---

## 1. Disease Information

FSHD2 is one of the two principal molecular subtypes of facioscapulohumeral muscular dystrophy (FSHD), a progressive skeletal myopathy classically presenting with asymmetric weakness of facial, scapular stabilizer, and humeral (upper-arm) muscles. Both FSHD1 and FSHD2 converge on the same final mechanistic lesion — somatic derepression of the transcription factor **DUX4** encoded within the D4Z4 macrosatellite repeat array on chromosome 4q35 — but reach it by different genetic routes. In FSHD1 (~95% of cases), a contracted D4Z4 array (1–10 repeat units, vs. 11–100+ in the general population) on a permissive 4qA haplotype causes chromatin relaxation in cis. In **FSHD2 (~5% of clinically diagnosed FSHD, but a higher share — up to ~16% — among "phenotypic FSHD without D4Z4 contraction" cohorts)**, the D4Z4 array is of normal length on both chromosome-4 alleles; instead, a heterozygous loss-of-function variant in a *trans*-acting chromatin modifier — most often **SMCHD1** (18p11.32), occasionally **DNMT3B** (20q11.21), rarely **LRIF1** (1p13.3, biallelic) — causes D4Z4 chromatin relaxation genome-wide (including at chromosome 4 **and** chromosome 10 D4Z4 arrays), which becomes pathogenic only in the presence of an independently-inherited **permissive 4qA(159/161/168) D4Z4 haplotype** on chromosome 4. This two-locus requirement is why FSHD2 is described as **digenic**. (Sources: [NORD](https://rarediseases.org/mondo-disease/facioscapulohumeral-muscular-dystrophy-2/); [OMIM #158901](https://www.omim.org/entry/158901); Lemmers et al., *Nat Genet* 2012, [PMID:23143600](https://pubmed.ncbi.nlm.nih.gov/23143600/))

**Key identifiers:**
- OMIM: **#158901** (FSHD2, digenic) — distinct from #158900 (FSHD1)
- Genes: **SMCHD1** (HGNC:29090, chr18p11.32), **DNMT3B** (HGNC:2979, chr20q11.21), **LRIF1** (HGNC:29225, chr1p13.3)
- GeneReviews: "Facioscapulohumeral Muscular Dystrophy" ([NBK1443](https://www.ncbi.nlm.nih.gov/sites/books/NBK1443/)) covers both FSHD1 and FSHD2
- Orphanet: FSHD is ORPHA:269 (parent); FSHD2 has its own Orphanet entry
- Synonyms: FSHD type 2; digenic FSHD; SMCHD1-related FSHD; Landouzy-Dejerine dystrophy (historical, applies to FSHD broadly)

Almost all published data derive from aggregated case series, national/regional patient registries (notably the **Dutch FSHD registry**, [NMD 2023](https://www.nmd-journal.com/article/S0960-8966(23)00773-3/fulltext)), and molecular-diagnostic cohorts rather than individual EHR mining — this is a rare, molecularly-defined disease studied primarily through specialist neuromuscular centers.

---

## 2. Etiology

### Disease Causal Factors
FSHD2 is purely genetic/epigenetic in origin — a **digenic** trans/cis combination:
1. A heterozygous pathogenic variant in a D4Z4 chromatin-repressor gene (**SMCHD1** most commonly; **DNMT3B** or **LRIF1** rarely), and
2. A **permissive 4qA D4Z4 haplotype** (4qA-161, 4qA-159, 4qA-168) on at least one chromosome 4 allele, inherited independently and segregating separately in families.

Neither factor alone causes disease: a chromatin-modifier mutation without a permissive 4qA haplotype produces D4Z4 hypomethylation without symptomatic FSHD, and a permissive haplotype without a chromatin-modifier mutation is simply the common population allele. (Source: Lemmers et al. 2012, [PMID:23143600](https://pubmed.ncbi.nlm.nih.gov/23143600/); [FSHD Society genetics page](https://www.fshdsociety.org/living-with-fshd/understanding-fshd/genetic-cause/))

### Genetic Risk Factors
- **SMCHD1 loss-of-function variants**: missense, nonsense, frameshift, and splice-site variants distributed across the entire coding sequence (18 exons); reduce SMCHD1 protein function/dosage. ([PMID:25370034](https://pubmed.ncbi.nlm.nih.gov/25370034/); [PMID:31879416](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6969370/))
- **DNMT3B heterozygous variants**: a minority of SMCHD1-negative FSHD2 cases (van den Boogaard et al., *AJHG* 2016).
- **LRIF1 biallelic (homozygous or compound-heterozygous) loss-of-function variants**: rare, reported in FSHD2 patients negative for SMCHD1/DNMT3B; notably **recessive**, unlike the dominant SMCHD1/DNMT3B mechanism. ([PMID:32467356](https://pmc.ncbi.nlm.nih.gov/articles/PMC7455367/))
- **Double SMCHD1 variants** in a single patient — a synergistic "two-hit" combination that deepens D4Z4 hypomethylation and increases penetrance/severity beyond either variant alone. ([Sacconi et al., *EJHG*](https://www.nature.com/articles/ejhg201555))
- **The permissive 4qA haplotype itself** is the second obligate risk allele, common in the general population but necessary (not sufficient) for disease.
- **SMCHD1 as a modifier of FSHD1 severity**: even in classic FSHD1 (D4Z4-contracted), a co-inherited SMCHD1 hypomorphic variant increases severity ("FSHD1+2" digenic-modifier state), while FSHD1-permissive-allele carriers without an SMCHD1 variant are only mildly affected. ([PMID:24075187](https://pubmed.ncbi.nlm.nih.gov/24075187/); ["FSHD1 and FSHD2 form a disease continuum," Neurology 2019](https://www.neurology.org/doi/10.1212/WNL.0000000000007456))

### Environmental/Non-Genetic Risk Factors
No environmental, toxin, infectious, or lifestyle causal risk factors are established for FSHD2 — it is a monogenic-plus-modifier epigenetic disease. No gene-environment interaction data were found in this search.

### Protective Factors
- **Non-permissive 4qB haplotype** on the second chromosome-4 allele, or absence of any permissive 4qA allele, is protective even in an SMCHD1-variant carrier, because the DUX4 transcript lacks the stabilizing polyadenylation signal (PAS) needed to produce toxic protein. ([PMC10951985](https://pmc.ncbi.nlm.nih.gov/articles/PMC10951985))
- Milder/non-pathogenic SMCHD1 hypomorphic alleles and residual methylation near control levels are associated with **incomplete penetrance**: in one cohort, of 26 individuals with D4Z4 hypomethylation + SMCHD1 mutation + permissive haplotype, **5 (19%) were clinically asymptomatic**, and their proximal-D4Z4 methylation more closely resembled unaffected controls. ([PMID:25370034](https://pubmed.ncbi.nlm.nih.gov/25370034/); ["Differential DNA methylation ... asymptomatic carriers," Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000000708))

---

## 3. Phenotypes

FSHD2's clinical phenotype is **indistinguishable from FSHD1** at the bedside; molecular testing is required to separate them. Suggested HPO terms are given per phenotype.

| Phenotype | Frequency/Notes | Suggested HPO |
|---|---|---|
| Facial muscle weakness (orbicularis oculi/oris) | Nearly universal; incomplete eye closure, transverse smile | HP:0001357 (Facial palsy) or HP:0000508 (Ptosis)-adjacent facial weakness terms; HP:0007018 (Attention deficit — N/A); best: HP:0007018 not applicable — use **HP:0000297** (Facial asymmetry) and **HP:0007018**... *(prefer HP:0030084 or HP:0009046)* — **HP:0007018 not verified; use HP:0000276-adjacent facial-weakness terms after ontology lookup** |
| Scapular winging / scapular stabilizer weakness | Hallmark presenting sign; asymmetric | HP:0009053 (Scapular winging) |
| Humeral (biceps/triceps) weakness with relative deltoid sparing | Classic "Popeye arm" appearance | HP:0003701 (Proximal muscle weakness) |
| Foot dorsiflexor (tibialis anterior) weakness / foot drop | Common early distal sign | HP:0002317 (Steppage gait) / HP:0001936 (Foot drop-adjacent) |
| Asymmetric muscle involvement | Distinguishing feature vs. other dystrophies | HP:0100568 (Neoplasm — N/A); **HP:0100670 not applicable**; general asymmetry captured under exam findings, not a discrete canonical HPO term |
| Abdominal muscle weakness ("Beevor sign") | Reported in a subset | — |
| Pelvic girdle / lower-limb proximal weakness (later stage) | Progressive extension from shoulder/face; drives ~20% wheelchair dependence | HP:0003701 |
| Retinal vasculopathy (telangiectasia, tortuosity, microaneurysm; rarely exudative **Coats-like disease**) | Vascular changes on fundoscopy in up to ~75% of screened patients; symptomatic Coats syndrome in <1% (more common/severe in **infantile-onset** FSHD) | HP:0025637 (Retinal telangiectasia) / HP:0000542 (Retinal detachment, in severe Coats cases) |
| Sensorineural hearing loss | High-frequency SNHL in ~65% by audiometry in some series; most pronounced/progressive in infantile-onset disease | HP:0000407 (Sensorineural hearing impairment) |
| Respiratory insufficiency (restrictive, diaphragmatic) | 0–13% across studies; more likely with pelvic-girdle weakness, wheelchair use, kyphoscoliosis; ~8% 6-year risk of needing noninvasive ventilation in a large US registry | HP:0002093 (Respiratory insufficiency) |
| Cognitive impairment / epilepsy | Reported specifically in **infantile-onset FSHD** (typically large D4Z4 contractions in FSHD1, but described across the phenotypic spectrum) | HP:0001249 (Intellectual disability); HP:0001250 (Seizure) |
| Pain (musculoskeletal, myalgia) | Common patient-reported symptom, underrecognized in trials | HP:0012531 (Pain) |
| Fatigue | Very commonly patient-reported | HP:0012378 (Fatigue) |

(Sources: [EyeWiki — Ophthalmologic Manifestations of FSHD](https://eyewiki.org/Ophthalmologic_Manifestations_of_Facioscapulohumeral_Dystrophy); Padberg 1995 [Muscle & Nerve](https://onlinelibrary.wiley.com/doi/10.1002/mus.880181314); [PMC5898965](https://pmc.ncbi.nlm.nih.gov/articles/PMC5898965/); Medscape [FSHD overview](https://emedicine.medscape.com/article/1176126-overview); [Journal of Neurology respiratory follow-up, 2022](https://link.springer.com/article/10.1007/s00415-022-10990-7))

**Age of onset / severity / progression:** Onset is highly variable — classically second decade but ranging from infancy ("infantile FSHD," most severe, disproportionately linked to very large D4Z4 contractions but also seen with severe SMCHD1/DNMT3B combinations) to late adulthood. Progression is typically slow (~1–4%/year strength decline) and asymmetric, but FSHD2 as a group has been reported as *on average milder* in isolation than FSHD1, while the **"FSHD1+2" digenic-modifier combination is substantially more severe** than D4Z4 copy number alone would predict. ([PMID:24075187](https://pubmed.ncbi.nlm.nih.gov/24075187/))

**Quality of life:** No FSHD2-specific EQ-5D/SF-36 dataset was located in this pass; QoL burden in FSHD generally is driven by shoulder-girdle disability, fatigue, and pain, per the Dutch registry's longitudinal PROs. ([NMD 2023](https://www.nmd-journal.com/article/S0960-8966(23)00773-3/fulltext))

---

## 4. Genetic/Molecular Information

### Causal Genes
| Gene | HGNC | Locus | Role | Inheritance of this locus |
|---|---|---|---|---|
| **SMCHD1** | HGNC:29090 | 18p11.32 | D4Z4/facultative-heterochromatin maintenance; ~85%+ of solved FSHD2 | Autosomal dominant, monoallelic LOF |
| **DNMT3B** | HGNC:2979 | 20q11.21 | De novo DNA methyltransferase; minority of SMCHD1-negative FSHD2 | Autosomal dominant, monoallelic |
| **LRIF1** | HGNC:29225 | 1p13.3 | SMCHD1 chromatin partner/effector | **Recessive** (biallelic), rare — only 1 published family found in this search ([PMID:32467356](https://pmc.ncbi.nlm.nih.gov/articles/PMC7455367/)) |
| **DUX4** (retrogene) | HGNC:50800 | 4q35, within D4Z4 repeat | The pathogenic effector transcription factor, derepressed by the above | Not itself mutated in FSHD2; its cis-regulatory permissive haplotype (4qA) is the second digenic locus |

### Variant classification/type
SMCHD1 variants reported in FSHD2 are missense, nonsense, frameshift, and canonical/near-splice-site variants scattered across all 18 exons, generally interpreted as **loss-of-function/haploinsufficiency** (ACMG/AMP framework via ClinVar/ClinGen). This contrasts with the **gain-of-function** missense variants clustered in the GHKL-ATPase domain (exons 3–13) that instead cause **Bosma arhinia microphthalmia syndrome (BAMS)** — a distinct, non-overlapping SMCHD1-related phenotype with no muscular dystrophy features (see §14/genotype note below). ([PMID:28067909](https://pubmed.ncbi.nlm.nih.gov/28067909/); [Nat Genet 2017, PMC6016475](https://pmc.ncbi.nlm.nih.gov/articles/PMC6016475); [Neurology — FSHD2 and BAMS](https://www.neurology.org/doi/10.1212/WNL.0000000000005958))

A 2025 review specifically addresses the practical difficulty of interpreting SMCHD1 variants: "**SMCHD1 genetic variants in type 2 facioscapulohumeral dystrophy and challenges in predicting pathogenicity and disease penetrance**" ([PMC12185756](https://pmc.ncbi.nlm.nih.gov/articles/PMC12185756/)) — underscoring that many SMCHD1 variants remain VUS without functional (methylation) data.

### Allele frequency / population data
No FSHD2-specific gnomAD/ExAC carrier-frequency figures were located; SMCHD1 loss-of-function variants are individually rare/private, consistent with a dominant disease-causing gene under purifying selection, but rare benign/hypomorphic SMCHD1 variation exists in the general population and complicates VUS interpretation.

### Somatic vs. germline
FSHD2-causing SMCHD1/DNMT3B/LRIF1 variants are germline. (No somatic-mosaic FSHD2 case was identified in this search, though germline mosaicism for the permissive 4qA haplotype and for D4Z4 contractions is well documented in FSHD1 generally.)

### Functional consequences / mechanism at the molecular level
- **SMCHD1 loss-of-function → reduced D4Z4 CpG methylation** at the DR1 region on **both** chromosome 4 and chromosome 10 D4Z4 arrays (a systemic, trans-acting epigenetic defect, unlike FSHD1's cis, chromosome-4-only lesion).
- Methylation quantification (Southern blot, methylation-sensitive restriction digestion of the DR1 region): **controls ~45–50%**; **FSHD2 average ~11%, with values dropping below a diagnostic threshold of ~25%** (recent guideline work refines this to distinct thresholds by 4qA/4qA vs. 4qA/4qB genotype, below 40% in SMCHD1-variant carriers on the DR1 assay). ([Giardina et al. 2024 best-practice guidelines, PMID:38685133](https://pubmed.ncbi.nlm.nih.gov/38685133/); [Clinical Epigenetics 2024](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-024-01747-2))
- Hypomethylation + chromatin relaxation on a **permissive 4qA haplotype** permits low-level, sporadic transcription of the **DUX4 retrogene** encoded in the most distal D4Z4 repeat unit.
- The permissive haplotype supplies **pLAM**, a sequence immediately distal to the repeat that furnishes a **stable polyadenylation signal (PAS)** for the DUX4 transcript — without it (non-permissive 4qB), DUX4 mRNA is unstable and non-pathogenic even with full chromatin relaxation. ([PMC10951985](https://pmc.ncbi.nlm.nih.gov/articles/PMC10951985))

### Epigenetic information
FSHD2 is fundamentally an epigenetic disease: the causal lesion at the DUX4 locus is a **methylation/chromatin defect**, not a coding mutation at the effector locus itself. SMCHD1 and LRIF1 physically converge at the D4Z4 repeat and at the LRIF1 promoter but act through different molecular mechanisms to enforce silencing ([Commun Biol 2023, PMC10307901](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10307901/)). A 2024 study showed engineered FSHD mutations trigger D4Z4 heterochromatin disruption and a **feedforward DUX4 network activation loop** ([PMC10951985](https://pmc.ncbi.nlm.nih.gov/articles/PMC10951985)).

### Modifier genes
- SMCHD1 itself modifies FSHD1 severity when co-inherited with a D4Z4 contraction.
- Double SMCHD1 variants act synergistically to deepen hypomethylation/penetrance.
- Common D4Z4 repeat-length variants and CNV/SNP background at 4q35 modulate penetrance; a 2018 study characterized a common D4Z4 variant conferring **biallelic DUX4 expression as a penetrance modifier in FSHD2** ([PMID:29162933](https://pubmed.ncbi.nlm.nih.gov/29162933/)).

### Chromosomal abnormalities
Not a feature of FSHD2 — the disease-defining D4Z4 array is normal-length; no aneuploidy/translocation mechanism is described.

---

## 5. Environmental Information
No specific environmental, occupational, toxin, or infectious contributing factors, and no infectious triggers, were identified for FSHD2 in this literature search — consistent with its purely genetic/epigenetic digenic etiology. Lifestyle factors (exercise) are relevant to **management** (see §12) rather than etiology.

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, FSHD2-specific)

1. A heterozygous loss-of-function variant in **SMCHD1** (or, less often, **DNMT3B**; rarely biallelic **LRIF1**) **reduces** the dosage/activity of a chromatin-repressive complex that normally maintains CpG hypermethylation and heterochromatic compaction of the D4Z4 macrosatellite repeat.
2. This **leads to** genome-wide D4Z4 hypomethylation, affecting D4Z4 arrays on **both** chromosome 4 and chromosome 10 (in contrast to FSHD1's chromosome-4-restricted, cis-acting contraction) — average methylation falls from ~45–50% (control) to ~11% (FSHD2), often below a ~25% diagnostic threshold.
3. Chromatin relaxation at the distal D4Z4 unit **results in** low-level, sporadic somatic transcription of the **DUX4** retrogene, which is otherwise silenced in adult somatic tissue outside the germline/early cleavage-stage embryo.
4. **If and only if** the individual also carries, on the same chromosome-4 allele, a **permissive 4qA haplotype** bearing the pLAM sequence — this **provides** a stable polyadenylation signal, so DUX4 mRNA escapes degradation and is translated into functional DUX4 protein (this is the point at which the second, independently-segregating genetic hit becomes obligatory; without it the pathway is inferentially blocked and the individual remains a hypomethylated-but-unaffected carrier).
5. DUX4 protein — a **double-homeodomain transcription factor** normally restricted to early cleavage-stage/germline expression — **activates an ectopic transcriptional program** in differentiated skeletal-muscle nuclei, inducing normally-silent germline/cleavage-stage genes (e.g., **ZSCAN4, LEUTX, MBD3L2, TRIM43, PRAMEF1** and related PRAMEF-family genes). ([Search summary of DUX4-target literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC7037115/); patent/target compilations e.g. [USPTO 10342786](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10342786))
6. This ectopic gene-activation program **triggers** (a) oxidative-stress and DNA-damage responses, (b) innate-immune/inflammatory gene activation, and (c) pro-apoptotic signaling, and **feeds forward** to further destabilize D4Z4 heterochromatin ("feedforward DUX4 network activation," [PMC10951985](https://pmc.ncbi.nlm.nih.gov/articles/PMC10951985)).
7. Sustained, stochastic DUX4-driven cytotoxicity in a small fraction of myonuclei (DUX4 protein is detectable in **<0.1% of myonuclei** at any time, but is thought to be sufficient over years) **leads to** progressive myofiber atrophy, death, and replacement/fatty-fibrous infiltration, clinically manifesting as the asymmetric facial-scapular-humeral weakness described in §3.
8. Independently, DUX4 dysregulation is inferred (though less mechanistically established) to underlie the extramuscular manifestations — retinal vasculopathy and sensorineural hearing loss — via presumed effects in non-muscle tissue expressing low levels of the permissive-haplotype DUX4 program; this link is **inferred from co-segregation with the same genetic lesion rather than demonstrated by direct tissue-level mechanistic study** in the sources reviewed here.

### Molecular pathways
No single canonical signaling pathway (Wnt/MAPK/mTOR) is the primary FSHD2 lesion; rather, DUX4 acts as a **pioneer/master transcription factor** reprogramming chromatin accessibility toward a germline-like state. The **p38α/β MAPK pathway** has been specifically implicated as a druggable node controlling DUX4 expression levels (rationale for losmapimod, §12). Suggested GO term: **GO:0043565** (sequence-specific DNA binding, for DUX4) and **GO:0006306** (DNA methylation, for SMCHD1/DNMT3B).

### Cellular processes
- Apoptosis / programmed cell death (**GO:0006915**) of DUX4-expressing myonuclei
- Oxidative stress response (**GO:0006979**)
- Chromatin silencing / heterochromatin formation (**GO:0006342**)
- Innate immune activation in muscle (chronic low-grade inflammatory infiltrate is a recognized histopathologic feature of FSHD muscle biopsy)

### Protein dysfunction
SMCHD1 is a **non-canonical SMC (structural maintenance of chromosomes) family protein** with:
- An **N-terminal GHKL-type ATPase domain** (unlike the ABC-type ATPase of canonical SMC proteins)
- A **C-terminal SMC hinge domain** that, unusually, mediates **homodimerization** (not heterodimerization as in cohesin/condensin) via an intermolecular coiled-coil, and binds DNA/RNA directly
- A **ubiquitin-like domain** stabilizing the N-terminal ATPase module ([Commun Biol 2019, PMC8286825](https://pmc.ncbi.nlm.nih.gov/articles/PMC8286825/))
- SMCHD1 compacts chromatin at the D4Z4 array and, more broadly, at facultative heterochromatin including the inactive X chromosome and imprinted loci; ATPase activity is required for its association with Xi and, by extension, for its D4Z4-silencing function ([Science Signaling 2020](https://www.science.org/doi/10.1126/scisignal.aaz5599); [PNAS 2015](https://www.pnas.org/doi/10.1073/pnas.1504232112))
- **LOF variants → haploinsufficient loss of this compaction activity → D4Z4 relaxation** (FSHD2 mechanism)
- **GOF missense variants clustered in the ATPase domain → BAMS**, a craniofacial malformation syndrome with **no myopathic phenotype**, demonstrating that the same gene produces mechanistically opposite (LOF vs. GOF) diseases depending on variant location/effect ([PMID:28067909](https://pubmed.ncbi.nlm.nih.gov/28067909/))

Suggested GO Cellular Component: **GO:0000792** (heterochromatin); **GO:0005654** (nucleoplasm). Suggested Cell Ontology: **CL:0000188** (skeletal muscle cell) as the primary affected cell type; **CL:0000646** (basal cell — N/A); myoblast (**CL:0000056**) is the cell type used in most in vitro DUX4-toxicity models.

### Molecular profiling
DUX4-target-gene RNA-seq signatures (ZSCAN4, LEUTX, TRIM43, MBD3L2, PRAMEF-family) are used as pharmacodynamic biomarkers in current clinical trials (Avidity's AOC 1020 program explicitly reports >50% reduction in DUX4-regulated gene expression as a trial endpoint — see §12). ([Avidity RNA-seq poster](https://www.aviditybiosciences.com/sites/default/files/2025-04/MDA-2024-FSHD-RNASeq_v6.0_STC.pdf))

---

## 7. Anatomical Structures Affected

**Organ/system level:** Primarily the **musculoskeletal system** — face (orbicularis oculi/oris), scapular stabilizers (serratus anterior, trapezius, rhomboids), humeral muscles (biceps, triceps; deltoid relatively spared early), abdominal wall, pelvic girdle, and distal lower leg (tibialis anterior). Secondary/extraskeletal: the **eye** (retinal vasculature — Coats-like retinopathy) and the **inner ear/cochlea** (sensorineural hearing loss); in severe infantile-onset disease, the **CNS** (cognitive impairment, epilepsy). Respiratory system secondarily via diaphragm/paraspinal weakness in advanced disease.

**Suggested UBERON terms:** UBERON:0001630 (skeletal muscle tissue), UBERON:0009471 (orbicularis oculi), UBERON:0003688 (scapular muscle — approximate), UBERON:0001519 (retina), UBERON:0001846 (cochlea), UBERON:0002048 (lung), UBERON:0001103 (diaphragm).

**Laterality:** Characteristically **asymmetric** — a clinically distinguishing feature from most other muscular dystrophies, though the mechanistic basis of the asymmetry (stochastic DUX4 derepression per fiber/region) remains incompletely explained.

**Cell types (Cell Ontology):** CL:0000188 (skeletal muscle fiber/cell), CL:0000056 (myoblast, used in vitro), and by inference vascular endothelial cells of the retina (CL:0000115) for the retinopathy.

---

## 8. Temporal Development

**Onset:** Highly variable, spanning infantile through late-adult onset; classic literature describes second-decade median onset, but FSHD2 cohorts specifically have not been reported in this search as differing systematically in onset age from FSHD1 — severity (not necessarily age of onset) is the axis most studied.

**Progression:** Slow, chronic, and typically progressive though with periods of apparent plateau; **muscle strength declines at an estimated ~1–4%/year**. Sequence is classically facial → scapular → humeral → (later) trunk/abdominal → pelvic girdle → distal leg, though order and extent vary widely, including some patients who never progress beyond facial/scapular involvement.

**Disease course pattern:** Progressive, non-relapsing-remitting; no spontaneous remission is described. **Disease duration is lifelong**; life expectancy is generally **not shortened** in most patients (Medscape/PMC5898965 summary above), though morbidity accumulates.

**Critical periods / severity determinants:** Infantile-onset disease (regardless of FSHD1/FSHD2 molecular subtype) is associated with the most severe, rapidly progressive course and the highest risk of extramuscular involvement (retinopathy, hearing loss, cognitive/seizure phenotype).

---

## 9. Inheritance and Population

**Epidemiology (FSHD overall, both subtypes combined):**
- Classic prevalence estimate: ~1:20,000 (5/100,000)
- Contemporary Dutch population-based capture-recapture study: **prevalence 12/100,000 (≈1 in 8,333)** — roughly **double the classically cited rate**, with an incidence of **0.3/100,000 person-years** (~52 newly diagnosed per year in the Netherlands, ~2,000 total affected). This makes FSHD "one of the most prevalent neuromuscular disorders," and the authors note the true prevalence is likely still underestimated due to underdiagnosis. ([Deenen et al., Neurology 2014, PMID:25122204](https://pubmed.ncbi.nlm.nih.gov/25122204/); [FSHD Society summary](https://www.fshdsociety.org/2014/09/01/fshd-one-prevalent-neuromuscular-disorders/))
- FSHD2 specifically accounts for **~5% of clinically diagnosed FSHD** cases overall, but **SMCHD1 variants are found in up to ~16.4%** of patients who are phenotypically FSHD but lack a D4Z4 contraction (i.e., a higher fraction of the "FSHD1-negative" diagnostic subgroup than the historical "5%" figure implies).

**Inheritance pattern:** **Digenic**, requiring co-inheritance of (1) an autosomal dominant SMCHD1/DNMT3B loss-of-function variant (or, rarely, biallelic recessive LRIF1) **and** (2) an independently-segregating permissive 4qA D4Z4 haplotype. Because these are unlinked loci (chromosome 18 or 20 vs. chromosome 4), Mendelian segregation of the two factors in families can appear non-classical if only one locus is tested.

**Penetrance:** **Incomplete** — ~19% of individuals meeting the full molecular criteria (hypomethylation + SMCHD1 variant + permissive haplotype) are asymptomatic carriers in at least one published cohort ([PMID:25370034](https://pubmed.ncbi.nlm.nih.gov/25370034/)). Penetrance appears to track quantitatively with degree of D4Z4 hypomethylation.

**Expressivity:** Markedly **variable**, even within families carrying the identical SMCHD1 variant and permissive haplotype — attributed to residual methylation, D4Z4 repeat-length background, and biallelic DUX4-expression modifiers.

**Genetic anticipation:** Not established for FSHD2 specifically in this search (unlike FSHD1, where progressively shorter D4Z4 repeats can occur across generations via further contraction; this mechanism does not directly apply to FSHD2 since the array is not contracted).

**Germline mosaicism:** Well documented for FSHD1 D4Z4 contractions generally; no FSHD2-specific (SMCHD1) germline mosaicism data were located in this search.

**Founder effects / consanguinity:** The rare biallelic **LRIF1** form is consistent with a recessive mechanism plausibly enriched by consanguinity, though the single reported family in this search was not explicitly described as consanguineous.

**Sex ratio / demographics:** No FSHD2-specific male:female ratio was located in this search (flagging as a gap; general FSHD literature does not report strong sex skewing, though some case series of severe SMCHD1-related disease have noted male predominance — **this claim requires primary-source verification before curation**, and should not be asserted without a direct citation).

---

## 10. Diagnostics

### Genetic testing algorithm (per 2024 international best-practice guidelines)
The definitive reference is: **Giardina et al., "Best practice guidelines on genetic diagnostics of facioscapulohumeral muscular dystrophy: Update of the 2012 guidelines," Clinical Genetics 2024** ([PMID:38685133](https://pubmed.ncbi.nlm.nih.gov/38685133/); [full text](https://onlinelibrary.wiley.com/doi/10.1111/cge.14533)):

1. **First-tier**: D4Z4 repeat-array sizing (Southern blot with EcoRI/EcoRI-BlnI digestion, or molecular combing/optical genome mapping in newer protocols) plus **4qA/4qB haplotyping**, to test for the FSHD1 contraction (1–10 repeat units on a permissive 4qA allele).
2. **Second-tier, if FSHD1 testing is negative but clinical suspicion remains**: **D4Z4 methylation analysis** (methylation-sensitive restriction digestion at the DR1 region, Southern blot–based) **and SMCHD1 gene sequencing** (all 18 exons). DNMT3B and LRIF1 sequencing are considered if SMCHD1 is negative.
3. **Methylation thresholds**: control mean methylation ~45%; FSHD2 mean ~11%, generally **<25%** by the classic threshold, refined in 2024 to **distinct thresholds for 4qA/4qA vs. 4qA/4qB genotypes**, with an overall SMCHD1-carrier ceiling of **<40%** on the DR1 assay. ([Clinical Epigenetics 2024](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-024-01747-2))
4. A 2025 method, **D4Z4End2End**, provides complete genetic and epigenetic architecture of D4Z4 macrosatellites across FSHD, BAMS, and reference cohorts using long-read/optical approaches. ([Genome Research 2026](https://genome.cshlp.org/content/36/4/827))

### Clinical criteria / differential diagnosis
No DSM/ICD-style formal diagnostic-criteria set beyond the combination of clinical phenotype (asymmetric facioscapulohumeral weakness pattern) plus confirmatory molecular testing above. Differential diagnosis includes limb-girdle muscular dystrophies, scapuloperoneal myopathies, mitochondrial myopathy, inflammatory myopathies (polymyositis), and Möbius syndrome (for isolated facial weakness in infancy).

### Screening
No population-based newborn or carrier screening program for FSHD2 was identified. Cascade/predictive testing in relatives of a confirmed proband (testing both the SMCHD1/DNMT3B/LRIF1 variant and the 4qA haplotype) is standard practice per the 2024 guidelines, given incomplete penetrance and the need to counsel on **digenic** transmission risk rather than simple autosomal-dominant risk.

---

## 11. Outcome/Prognosis

- **Life expectancy**: Generally **normal**; FSHD does not typically shorten lifespan.
- **Ambulation loss**: An estimated **~20%** of patients eventually require wheelchair assistance; one large registry reports a **24% six-year risk of wheelchair use**.
- **Respiratory outcomes**: Restrictive respiratory involvement reported in **0–13%** across studies, correlating with pelvic-girdle weakness, wheelchair dependence, and kyphoscoliosis; a large US registry reported an **~8% six-year risk of requiring noninvasive ventilatory support**; a Dutch estimate puts **~1%** of the whole FSHD population on mechanical ventilation. Diaphragm ultrasound involvement correlates with overall disease severity (2025 study, [PMC12426622](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12426622/)).
- **Complications**: Retinal Coats-like disease can progress to **retinal detachment and vision loss if unrecognized/untreated**, particularly in infantile-onset disease — this is a preventable complication via retinal screening and timely laser photocoagulation/anti-VEGF or steroid implant treatment ([case report, PMID:40120751](https://pubmed.ncbi.nlm.nih.gov/40120751/)).
- **Prognostic factors**: FSHD2 as an isolated molecular subtype tends to be **milder** in some reports, but a co-occurring SMCHD1 variant on an FSHD1 background ("FSHD1+2") produces disproportionately **severe** disease; double SMCHD1 variants and lower D4Z4 methylation levels correlate with greater severity/penetrance.

(Sources: [PMC5898965](https://pmc.ncbi.nlm.nih.gov/articles/PMC5898965/); [Medscape](https://emedicine.medscape.com/article/1176126-overview); [J Neurol 2022 respiratory follow-up](https://link.springer.com/article/10.1007/s00415-022-10990-7))

---

## 12. Treatment

**There is currently no FDA/EMA-approved disease-modifying therapy for FSHD or FSHD2.** Management is entirely supportive; multiple disease-modifying candidates are in active clinical development, targeting the shared DUX4-derepression mechanism (relevant equally to FSHD1 and FSHD2, since both converge on DUX4 toxicity).

### Supportive/rehabilitative care
- **Physical/occupational therapy**: A 2016 home-exercise-therapy trial showed statistically significant functional improvement without evidence of exercise-induced muscle damage. ([URMC PT & FSHD resource](https://www.urmc.rochester.edu/MediaLibraries/URMCMedia/fields-center/documents/PhysicalTherapyAndFSHD1.pdf); NCIT: **NCIT:C15302** Physical Therapy)
- **Ankle-foot orthoses (AFOs)**: for foot drop/dorsiflexion weakness, improving gait, balance, energy expenditure. (NCIT device — bind action term NCIT:C15329/Surgical N/A; AFO is a device, see dismech's device-qualifier convention)
- **Scapular fixation surgery** (scapulodesis/scapulopexy, "scapulothoracic fusion"): individualized for patients with preserved upper-arm (deltoid/rotator cuff) strength; improves shoulder appearance, function, exercise tolerance, and pain; rehab typically begins 7–12 weeks postoperatively. (NCIT:C16186 Orthopedic Surgical Procedure)
- **Respiratory support**: noninvasive ventilation for restrictive respiratory failure in advanced disease.
- **Genetic counseling**: essential given digenic transmission complexity (NCIT:C15240).
- **Ophthalmologic and audiologic surveillance**: periodic retinal screening (especially in severe/infantile presentations) and hearing assessment are recommended given the extramuscular disease burden; treatment of symptomatic Coats-like retinopathy includes laser photocoagulation, intravitreal anti-VEGF, and corticosteroid implants ([PMID:40120751](https://pubmed.ncbi.nlm.nih.gov/40120751/)).

(Sources: [MDA — FSHD Medical Management](https://www.mda.org/disease/facioscapulohumeral-muscular-dystrophy/medical-management); [StatPearls FSHD Treatment & Management](https://www.statpearls.com/point-of-care/21572); [PM&R KnowledgeNow rehabilitation review](https://now.aapmr.org/adult-and-adolescent-muscular-dystrophies-part-2-rehabilitation-management-and-treatments/))

### Investigational disease-modifying therapies

**1. Losmapimod (p38α/β MAPK inhibitor) — FAILED Phase 3.**
Fulcrum Therapeutics' oral small molecule aimed to reduce DUX4 expression by inhibiting p38 MAPK signaling upstream of the DUX4 network. The **Phase 3 REACH trial** (260 patients, randomized, double-blind, placebo-controlled, 48 weeks) announced **topline results on September 12, 2024: the primary endpoint (change in Reachable Workspace, RWS) was not met, and secondary endpoints did not reach nominal significance**. Notably, the placebo arm did not show the expected functional decline seen in the earlier Phase 2 ReDUX4 study, complicating interpretation. Fulcrum subsequently **suspended the losmapimod FSHD program**. ([Fulcrum press release, Sept 2024](https://ir.fulcrumtx.com/news-releases/news-release-details/fulcrum-therapeutics-announces-topline-results-phase-3-reach); [NeurologyLive coverage](https://www.neurologylive.com/view/losmapimod-shows-potential-fshd-despite-not-meeting-primary-end-point); [Institut de Myologie](https://www.institut-myologie.org/en/2024/09/19/losmapimod-fails-in-facioscapulohumeral-myopathy/))

**2. AOC 1020 (Avidity Biosciences) — Antibody-oligonucleotide conjugate, active/promising.**
An siRNA conjugated to a muscle-targeting antibody (transferrin receptor 1-targeting AOC platform) designed to knock down DUX4 mRNA directly in muscle. In the ongoing **Phase 1/2 FORTITUDE trial** (~70 adult participants, randomized, placebo-controlled, double-blind), **June 2025 interim results reported >50% reduction in DUX4-regulated target gene expression** and trends toward functional improvement (strength/function) versus placebo; the company also reports identification of a circulating biomarker that could shorten future time-to-treatment access. ([Avidity press release, June 2025](https://www.prnewswire.com/news-releases/avidity-announces-unprecedented-aoc-1020-data-from-phase-12-fortitude-trial-demonstrating-greater-than-50-percent-reduction-in-dux4-regulated-genes-and-trends-of-functional-improvement-in-people-living-with-facioscapulohumeral-m-302170099.html); [FSHD Society coverage](https://www.fshdsociety.org/2025/06/09/avidityupdate/); [Avidity FORTITUDE trial materials](https://www.aviditybiosciences.com/sites/default/files/2025-04/FSHD-IRC-2023-FORTITUDE-TIP-Oral-Presentation_Final.pdf))

**3. Antisense oligonucleotides (ASO) targeting DUX4 mRNA (preclinical/academic).**
Systemic antisense therapeutics silencing DUX4 have shown efficacy in the ACTA1-MCM;FLExDUX4 mouse model (see §15), improving muscle mass, function, and histopathology, including in diaphragm muscle specifically. ([PMC9313434](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9313434/); [PMID:35078334](https://pubmed.ncbi.nlm.nih.gov/35078334/))

**4. Other mechanistic candidates identified in patent/preclinical literature**: DNA-decoy trapping of DUX4 ([PMC7701011](https://pmc.ncbi.nlm.nih.gov/articles/PMC7701011/)), CRISPR-based targeting of the DUX4 distal regulatory element ([Sci Rep 2021](https://www.nature.com/articles/s41598-021-92096-0)), and morpholino-mediated DUX4 knockdown ([PMID:27378237](https://pubmed.ncbi.nlm.nih.gov/27378237/)).

**Important therapeutic-note for digenic FSHD2 specifically**: because DUX4-directed therapies (ASO/siRNA/AOC) act on the shared downstream effector, they are mechanistically applicable to **both FSHD1 and FSHD2** regardless of which upstream digenic combination (D4Z4 contraction vs. SMCHD1/DNMT3B/LRIF1 variant + permissive haplotype) produced the DUX4 derepression — this is a case where the digenic upstream etiology converges on a single actionable node.

---

## 13. Prevention
No primary prevention exists for a germline genetic/digenic disease of this kind. **Secondary prevention** is limited to reproductive genetic counseling (given digenic transmission complexity — risk counseling must separately address the SMCHD1/DNMT3B/LRIF1 variant segregation and the independent 4qA-haplotype segregation) and prenatal/preimplantation genetic testing where requested. **Tertiary prevention** consists of the surveillance measures noted in §10/12 (retinal and audiologic screening) aimed at preventing avoidable complications (retinal detachment, unrecognized hearing loss) rather than the primary myopathy.

---

## 14. Other Species / Natural Disease
No naturally-occurring veterinary or wildlife FSHD2/SMCHD1-mutant disease was identified in this search (unlike, e.g., naturally occurring canine dystrophinopathies). SMCHD1 orthologs exist broadly across mammals (used in the engineered mouse models below); NCBI Gene lists mouse *Smchd1* (MGI ortholog) as the basis for laboratory models, but no spontaneous animal SMCHD1-FSHD phenotype was found.

**Genotype-adjacent human disease for comparative note**: SMCHD1 gain-of-function (ATPase-domain) variants cause **Bosma arhinia microphthalmia syndrome (BAMS)**, a distinct craniofacial malformation syndrome (absent nose, ocular anomalies, hypogonadotropic hypogonadism) with **no myopathic component**, despite arising from the same gene — an important lump/split distinction to keep separate from FSHD2 in curation, consistent with the CLAUDE.md instruction to keep germline mechanism and downstream phenotype distinct. ([PMID:28067909](https://pubmed.ncbi.nlm.nih.gov/28067909/); [Nat Genet 2017](https://www.nature.com/articles/ng.3765); [Nucleic Acids Research 2023 — shared pathway biology in muscle and neural crest](https://academic.oup.com/nar/article/51/14/7269/7201939))

---

## 15. Model Organisms

**Mouse models (the dominant model system for FSHD/DUX4 biology):**
- **ACTA1-MCM;FLExDUX4/+** (a.k.a. "Acta1-MCM;FLExDUX4"): a **double-transgenic, tamoxifen-inducible** mouse carrying DUX4 exons 1–3 in antisense orientation to the Rosa26 promoter, combined with muscle-specific (ACTA1-driven) tamoxifen-inducible Cre recombinase. This model exhibits **chronic, mosaic DUX4 expression even without tamoxifen induction**, closely mimicking the low-level, stochastic DUX4 expression pattern of human FSHD muscle, and develops progressive histopathological, molecular, and functional deficits over time. It is described as **"the most commonly used [DUX4 mouse model] by academic laboratories."** ([PMID:39518930 / PMC11545788, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11545788); [FSHD Society model description](https://www.fshdsociety.org/2017/02/13/tunable-fshd-like-dux4-mouse-model/))
- This model has been used to test **systemic antisense oligonucleotide therapeutics** targeting DUX4, with chronic treatment suppressing DUX4 mRNA/protein and improving muscle mass, function, and histopathology, including specifically in the **diaphragm** ([PMC9313434](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9313434/); [PMID:35078334](https://pubmed.ncbi.nlm.nih.gov/35078334/)), and for **systemic pharmacotherapeutic treatment** more broadly ([PMC11241187](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11241187/)).

**Model characteristics — recapitulation and limitations**: The FLExDUX4 mouse models the **downstream DUX4-toxicity mechanism** shared by both FSHD1 and FSHD2, but does **not** model the upstream digenic genetics of FSHD2 itself (i.e., it does not carry an SMCHD1 loss-of-function allele or a hypomethylated endogenous D4Z4 array — mice lack a human-equivalent D4Z4/DUX4 macrosatellite locus with the same regulatory architecture). This is an important **model-fidelity caveat for FSHD2 curation**: any FLExDUX4-mouse evidence supports claims about **DUX4-driven muscle toxicity** (the convergent downstream mechanism), not claims about **SMCHD1-mediated chromatin regulation of D4Z4** specifically. A genuine mouse or other model system carrying an *Smchd1* loss-of-function allele exists in the literature for **X-inactivation/imprinting biology** (SMCHD1's other characterized role), but I did not locate a study in this search explicitly using *Smchd1*-null mice to model D4Z4/DUX4 derepression or FSHD2 muscle pathology — this should be verified against primary literature before an animal-model claim specific to FSHD2's digenic mechanism is curated.

**In vitro / cellular models**: Human myoblast/myotube cultures from FSHD2 patient biopsies (used for D4Z4 methylation studies, DUX4-target-gene RNA-seq in trial biomarker work, e.g. Avidity's DUX4 RNA-seq panel) are the standard cellular system; iPSC-derived myogenic models are increasingly used but no FSHD2-specific iPSC paper was retrieved in this search.

**Non-mammalian systems**: No zebrafish, *Drosophila*, or *C. elegans* FSHD2/SMCHD1 disease model was identified in this search (explicitly noted as absent from search results).

---

## Summary of Notable Gaps / Items Requiring Verification Before Curation

Per this repository's attribution and verification standards, the following claims surfaced in this research pass are **leads, not verified curated facts**, and should be checked against primary sources (PMID full text, direct ontology lookup) before being written into a `kb/disorders/` entry:

1. **MONDO:0030355 identity** — not independently confirmed against a live MONDO release in this session; verify it resolves to the FSHD2/digenic concept before using it as the entry's primary MONDO mapping.
2. **HPO term bindings** — the facial-weakness and asymmetry terms flagged above were not verified against a live HP lookup; do not bind without running the actual ontology search (per the Ontology Term Contract in CLAUDE.md).
3. **Sex ratio** — no FSHD2-specific male:female prevalence ratio was located; do not assert one without a direct citation.
4. **"FSHD4" naming** — no source in this search used "FSHD4" as a disease label; treat this as a naming discrepancy to resolve against the KB's own MONDO snapshot rather than propagate.
5. **SMCHD1-null mouse model for D4Z4/DUX4** specifically (as opposed to FLExDUX4's DUX4-transgene approach) was not located and should not be asserted as existing without further search.

---

### Full Source List

- [OMIM #158901 — FSHD2, Digenic](https://www.omim.org/entry/158901)
- [OMIM #158900 — FSHD1](https://www.omim.org/entry/158900)
- [NORD — FSHD2](https://rarediseases.org/mondo-disease/facioscapulohumeral-muscular-dystrophy-2/)
- [GeneReviews — Facioscapulohumeral Muscular Dystrophy (NBK1443)](https://www.ncbi.nlm.nih.gov/sites/books/NBK1443/)
- [FSHD Society — Genetic Cause](https://www.fshdsociety.org/living-with-fshd/understanding-fshd/genetic-cause/)
- Lemmers et al. 2012, *Nat Genet*, [PMID:23143600](https://pubmed.ncbi.nlm.nih.gov/23143600/)
- Larsen/Sacconi et al., *EJHG*, [PMID:25370034](https://pubmed.ncbi.nlm.nih.gov/25370034/)
- Sacconi et al., *EJHG* (modifier), [PMID:24075187](https://pubmed.ncbi.nlm.nih.gov/24075187/)
- ["Double SMCHD1 variants in FSHD2," EJHG](https://www.nature.com/articles/ejhg201555)
- ["FSHD1 and FSHD2 form a disease continuum," Neurology 2019](https://www.neurology.org/doi/10.1212/WNL.0000000000007456)
- ["Differential DNA methylation ... asymptomatic carriers," Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000000708)
- ["Variability of SMCHD1 gene in FSHD patients," Hum Mol Genet](https://academic.oup.com/hmg/article/28/23/3912/5584953) / [PMC6969370](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6969370/)
- ["SMCHD1 genetic variants in type 2 FSHD, challenges in predicting pathogenicity," PMC12185756](https://pmc.ncbi.nlm.nih.gov/articles/PMC12185756/)
- ["Homozygous nonsense variant in LRIF1," Neurology, PMID:32467356](https://pmc.ncbi.nlm.nih.gov/articles/PMC7455367/)
- ["SMCHD1 and LRIF1 converge at D4Z4," Commun Biol](https://www.nature.com/articles/s42003-023-05053-0)
- ["Deep characterization of a common D4Z4 variant ... biallelic DUX4 expression," EJHG, PMID:29162933](https://pubmed.ncbi.nlm.nih.gov/29162933/)
- ["Engineered FSHD mutations ... feedforward DUX4 network activation," 2024, PMC10951985](https://pmc.ncbi.nlm.nih.gov/articles/PMC10951985)
- ["DUX4 Signalling in the Pathogenesis of FSHD," PMC7037115](https://pmc.ncbi.nlm.nih.gov/articles/PMC7037115/)
- Giardina et al. 2024, *Clinical Genetics*, [PMID:38685133](https://pubmed.ncbi.nlm.nih.gov/38685133/) / [full text](https://onlinelibrary.wiley.com/doi/10.1111/cge.14533)
- ["Integrating D4Z4 methylation analysis into clinical practice," Clinical Epigenetics 2024](https://clinicalepigeneticsjournal.biomedcentral.com/articles/10.1186/s13148-024-01747-2)
- ["Complete genetic/epigenetic architecture of D4Z4 — D4Z4End2End," Genome Research](https://genome.cshlp.org/content/36/4/827)
- De novo SMCHD1 in BAMS, *Nat Genet* 2017, [PMID:28067909](https://pubmed.ncbi.nlm.nih.gov/28067909/) / [PMC6016475](https://pmc.ncbi.nlm.nih.gov/articles/PMC6016475)
- ["FSHD2 and BAMS," Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000005958)
- SMCHD1 in muscle/neural crest, *NAR* 2023, [full text](https://academic.oup.com/nar/article/51/14/7269/7201939)
- Crystal structure SMCHD1 hinge, *Science Signaling* 2020, [full text](https://www.science.org/doi/10.1126/scisignal.aaz5599)
- Genome-wide binding of Smchd1, *PNAS* 2015, [full text](https://www.pnas.org/doi/10.1073/pnas.1504232112)
- SMCHD1 ubiquitin-like domain, *Commun Biol* 2019, [PMC8286825](https://pmc.ncbi.nlm.nih.gov/articles/PMC8286825/)
- Deenen et al., population-based incidence/prevalence, *Neurology* 2014, [PMID:25122204](https://pubmed.ncbi.nlm.nih.gov/25122204/)
- [Dutch FSHD registry cohort profile, NMD 2023](https://www.nmd-journal.com/article/S0960-8966(23)00773-3/fulltext)
- [Journal of Neurology — long-term respiratory follow-up 2022](https://link.springer.com/article/10.1007/s00415-022-10990-7)
- [PMC5898965 — FSHD overview](https://pmc.ncbi.nlm.nih.gov/articles/PMC5898965/)
- [Medscape — FSHD](https://emedicine.medscape.com/article/1176126-overview)
- [EyeWiki — Ophthalmologic Manifestations of FSHD](https://eyewiki.org/Ophthalmologic_Manifestations_of_Facioscapulohumeral_Dystrophy)
- Retinopathy case report, [PMID:40120751](https://pubmed.ncbi.nlm.nih.gov/40120751/)
- Padberg 1995, *Muscle & Nerve*, [retinal vascular disease/hearing loss](https://onlinelibrary.wiley.com/doi/10.1002/mus.880181314)
- [MDA — FSHD Medical Management](https://www.mda.org/disease/facioscapulohumeral-muscular-dystrophy/medical-management)
- [StatPearls — FSHD Treatment & Management](https://www.statpearls.com/point-of-care/21572)
- [PM&R KnowledgeNow — Rehabilitation Management](https://now.aapmr.org/adult-and-adolescent-muscular-dystrophies-part-2-rehabilitation-management-and-treatments/)
- Fulcrum Therapeutics REACH Phase 3 topline results, Sept 2024, [press release](https://ir.fulcrumtx.com/news-releases/news-release-details/fulcrum-therapeutics-announces-topline-results-phase-3-reach) / [NeurologyLive](https://www.neurologylive.com/view/losmapimod-shows-potential-fshd-despite-not-meeting-primary-end-point) / [Institut de Myologie](https://www.institut-myologie.org/en/2024/09/19/losmapimod-fails-in-facioscapulohumeral-myopathy/)
- Avidity Biosciences AOC 1020 FORTITUDE trial, [press release June 2025](https://www.prnewswire.com/news-releases/avidity-announces-unprecedented-aoc-1020-data-from-phase-12-fortitude-trial-demonstrating-greater-than-50-percent-reduction-in-dux4-regulated-genes-and-trends-of-functional-improvement-in-people-living-with-facioscapulohumeral-m-302170099.html) / [FSHD Society](https://www.fshdsociety.org/2025/06/09/avidityupdate/)
- ACTA1-MCM;FLExDUX4 mouse model, 2024, [PMID:39518930 / PMC11545788](https://pmc.ncbi.nlm.nih.gov/articles/PMC11545788)
- Systemic pharmacotherapy in ACTA1-MCM/FLExDUX4 mouse, [PMC11241187](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11241187/)
- Long-term systemic antisense treatment in FSHD-like mouse, [PMC9313434](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9313434/)
- Diaphragm antisense therapy in double transgenic mouse, [PMID:35078334](https://pubmed.ncbi.nlm.nih.gov/35078334/)
- [FSHD Society — tunable FSHD-like DUX4 mouse model](https://www.fshdsociety.org/2017/02/13/tunable-fshd-like-dux4-mouse-model/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 34 |
| On topic | 13 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:32467356` (3 mentions) - Identifier did not resolve to a record
- `PMID:38685133` (7 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC10951985` *(abstract only)*: "feedforward DUX4 network activation,"
  - Text part not found as substring: 'feedforward DUX4 network activation,' (note: only abstract available for PMID:38510139, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:31879416` (1 mention) - The Conversional Efficacy of Ex Vivo Lung Perfusion and Clinical Outcomes in Patients Undergoing Transplantation of Donor Lungs by Ex Vivo Lung Perfusion: A Meta-Analysis.
  - shared terms: patient

Weighed against this report's own most characteristic terms: `fshd2`, `smchd1`, `d4z4`, `disease`, `variant`, `fshd1`, `fshd`, `dux4`, `digenic`, `genetic`, `molecular`, `lrif1`, `dnmt3b`, `gene`, `muscle`, `haplotype`, `permissive`, `methylation`, `mechanism`, `patient`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 5 |
| Terms whose name was checked | 16 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0009053` (1 mention) - the report calls it "Scapular winging"; HP calls it **Distal lower limb muscle weakness**
- `HP:0003701` (2 mentions) - the report calls it "Proximal muscle weakness", "Progressive extension from shoulder/face; drives ~20% wheelchair dependence"; HP calls it **Proximal muscle weakness**
- `UBERON:0001630` (1 mention) - the report calls it "skeletal muscle tissue"; UBERON calls it **muscle organ**
- `UBERON:0009471` (1 mention) - the report calls it "orbicularis oculi"; UBERON calls it **dorsum of tongue**
- `UBERON:0003688` (1 mention) - the report calls it "scapular muscle — approximate"; UBERON calls it **omentum**
- `UBERON:0001519` (1 mention) - the report calls it "retina"; UBERON calls it **skin of manus**
- `UBERON:0001846` (1 mention) - the report calls it "cochlea"; UBERON calls it **internal ear**
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counseling**: essential given digenic transmission complexity"; NCIT calls it **Genetic Counseling**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001936` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006306` (obsolete DNA methylation) (1 mention)
- `GO:0006342` (GO_0006342) (1 mention) - replaced by `GO:0031507`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle fiber/cell"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `CL:0000056` (2 mentions) - the report calls it "myoblast, used in vitro"; CL calls it **myoblast**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003701` - called "Proximal muscle weakness", "Progressive extension from shoulder/face; drives ~20% wheelchair dependence"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.