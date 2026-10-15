---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-01T10:47:28.306519'
end_time: '2026-10-01T10:53:10.057900'
duration_seconds: 341.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spastic Paraplegia 91, Autosomal Dominant, With or Without Cerebellar
    Ataxia
  mondo_id: MONDO:0957813
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
  - claude-opus-5-5
  web_search_requests: 4
  num_turns: 20
  total_cost_usd: 2.2695846000000004
  session_id: 5a3cfba5-2292-488f-87a7-26111239334f
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  - Write
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
citation_count: 8
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:36331550
  relevance_assessed: 19
  on_topic: 14
  off_topic: 1
  off_topic_references:
  - PMID:17331725
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 58
  verified: 58
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 6
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0957813
    reported_labels:
    - MONDO
    ontology_label: spastic paraplegia 91, autosomal dominant, with or without cerebellar
      ataxia
  - term_id: DOID:0070643
    reported_labels:
    - Disease Ontology
    ontology_label: hereditary spastic paraplegia 91
  - term_id: HP:0002500
    reported_labels:
    - verify
    ontology_label: Abnormal cerebral white matter morphology
  - term_id: GO:0098794
    reported_labels:
    - verify
    ontology_label: postsynapse
  - term_id: CL:2000062
    reported_labels:
    - verify
    ontology_label: placental villus capillary endothelial cell
  - term_id: UBERON:0002707
    reported_labels:
    - verify
    ontology_label: corticospinal tract
  - term_id: HP:0000006
    reported_labels:
    - verify
    ontology_label: Autosomal dominant inheritance
  - term_id: NCIT:C15986
    reported_labels:
    - Antiseizure medication
    - Bladder management (antimuscarinics)
    ontology_label: Pharmacotherapy
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spastic Paraplegia 91, Autosomal Dominant, With or Without Cerebellar Ataxia
- **MONDO ID:** MONDO:0957813 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spastic Paraplegia 91, Autosomal Dominant, With or Without Cerebellar Ataxia** covering all of the
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

I'm pulling the SPTAN1/SPG91 literature from Europe PMC so the report can cite verified PMIDs and abstracts.

Core literature is gathered; I'm checking one more model-organism citation (zebrafish αII-spectrin) and then I'll write the report.

# SPG91 (autosomal dominant spastic paraplegia 91, with or without cerebellar ataxia, caused by SPTAN1): research report for the dismech entry

**Target:** MONDO:0957813 · OMIM #620538 · Gene: *SPTAN1* (9q34.11)
**Prepared:** 2026-10-01

**How the evidence was checked.** I took the PMIDs, titles and abstract quotes in this report from Europe PMC and MedGen records fetched while writing it. I did **not** look up the ontology CURIEs (HPO, GO, CL, UBERON, NCIT, HGNC). They are leads only. Under the repo's "every CURIE is read from a source" rule, check each one with `runoak` or `just validate-terms` before binding it. I have marked them "(verify)".

---

## 1. Disease information

**Overview.** MedGen carries the OMIM definition for SPG91, quoted here in full:

> "Autosomal dominant spastic paraplegia-91 with or without cerebellar ataxia (SPG91) is a highly variable neurologic disorder characterized by early-onset gait abnormalities due to spastic paraplegia of the lower limbs, sometimes with cerebellar ataxia. The age at onset is highly variable (congenital to young adult), although most patients have symptom onset in the first decade. Some patients present with a spastic paraplegia-predominant phenotype with significant pyramidal signs, whereas others present with an ataxic-predominant phenotype. In addition, although most patients have a more 'pure' phenotype restricted to gait abnormalities without additional features, others have a more 'complicated' phenotype with additional features such as sensory abnormalities, peripheral neuropathy, optic neuropathy, developmental delay, variably impaired intellectual development, and seizures. Many have normal brain imaging, but cerebellar atrophy may be observed in those with prominent cerebellar ataxia." ([MedGen C1846222 → concept 1846222](https://www.ncbi.nlm.nih.gov/medgen/1846222))

**Identifiers**

| Resource | ID | Notes |
|---|---|---|
| MONDO | MONDO:0957813 | Confirmed on MedGen |
| OMIM (phenotype) | 620538 | Confirmed on MedGen |
| OMIM (gene) | 182810 (*SPTAN1*) | From memory, verify |
| Disease Ontology | DOID:0070643 | Found by search ([DO](https://disease-ontology.org/term/DOID:0070643)) |
| MedGen | 1846222 | |
| Orphanet | No dedicated ORPHA code found | Falls under the generic HSP / AD-HSP groupings. `just fetch-reference ORPHA:<n>` would need a specific code. |
| ICD-10-CM / ICD-11 | Only generic codes | G11.4 (hereditary spastic paraplegia) and ICD-11 8A62 / 8B44-type HSP codes. Neither is specific to SPG91. Verify before use. |
| MalaCards | spastic_paraplegia_91_… | ([MalaCards](https://www.malacards.org/card/spastic_paraplegia_91_autosomal_dominant_with_or_without_cerebellar_ataxia)) |

**Synonyms:** SPG91; spastic paraplegia 91; SPTAN1-related hereditary spastic paraplegia; SPTAN1-related spastic ataxia.

**Where the data come from:** cohort and case-series reports pooled through international consortia (sequencing datasets, the 100,000 Genomes Project, DECIPHER, GeneMatcher), plus disease-level resources (OMIM, MedGen). There are no EHR-derived data.

**Allelic disorders of *SPTAN1*** matter for lumping and splitting, because they are separate MONDO/OMIM entities:
- **DEE5 / EIEE5.** Dominant-negative in-frame variants in the C-terminal α20–α21 region.
  > "Dominant-negative mutations in alpha-II spectrin cause West syndrome with severe cerebral hypomyelination, spastic quadriplegia, and developmental delay" (title, PMID:20493457)
- **Autosomal dominant distal hereditary motor neuropathy.** Caused by nonsense variants and NMD (PMID:31332438; PMID:33578420).
- **Proposed autosomal recessive HSP.** Biallelic missense variants (PMID:31515523; PMID:34526651). This is distinct from SPG91, which is dominant.
- **Distal myopathy.** Haploinsufficiency through a 9q34 deletion (PMID:40999194).

---

## 2. Etiology

- **Cause:** a heterozygous (monoallelic) germline variant in *SPTAN1*, the gene for non-erythrocytic αII-spectrin (fodrin). Variants are either inherited dominantly or arise de novo.
- **Key evidence:**
  - Van de Vondel et al., 2022, Mov Disord (PMID:35150594):
    > "We describe 22 patients from 14 families with five novel SPTAN1 variants… We furthermore report a recurrent missense mutation (p.Arg19Trp) in 15 patients with spastic paraplegia from seven families with a dominant inheritance pattern in four and a de novo origin in one case."
  - Morsy et al., 2023, Genet Med (PMID:36331550), a case-control burden test:
    > "Statistically significant enrichment of rare (minor allele frequency < 1 × 10^-5) probably damaging SPTAN1 variants was identified in families with hereditary ataxia (HA) or hereditary spastic paraplegia (HSP) (12/1142 cases vs 52/23,847 controls, p = 2.8 × 10^-5)."
- **Environmental, protective and gene–environment factors:** none reported. Not applicable for a monogenic neurodegenerative disorder.
- **Modifiers:** none identified. Penetrance and expressivity vary within families (see §9), which suggests modifiers that have not been characterised.

---

## 3. Phenotypes

Frequencies are approximate. They come from about 25 published SPG91-spectrum patients:
- Van de Vondel 2022: 15 patients with p.Arg19Trp HSP and 6 with ataxia.
- Morsy 2023: 10 with HSP/HA.
- Lan 2025: 2 with p.Arg19Trp, plus a pooled review of the literature.

The cohorts overlap partly. All evidence is HUMAN_CLINICAL.

| Phenotype | HPO (verify) | Frequency / notes | Key source |
|---|---|---|---|
| Spastic paraplegia (lower limb) | HP:0001258 Spastic paraplegia | Core feature, near-universal in the HSP-predominant group | PMID:35150594, PMID:40397273 |
| Spastic gait | HP:0002064 | Common | MedGen HPO list |
| Babinski sign / pyramidal signs / hyperreflexia | HP:0003487; HP:0007256 Abnormal pyramidal sign; HP:0001347 | Common | Morsy patient 1 (hyperreflexia, ankle clonus) |
| Lower limb weakness (proximal and distal) | HP:0007340 / HP:0008944 / HP:0009053 | Frequent | MedGen |
| Cerebellar ataxia | HP:0001251 Ataxia | ~30% of p.Arg19Trp carriers; defining in the ataxic-predominant group (Lys2083del, Arg1098Cys, Arg1624Cys, exon 25–27 deletion, c.3519+2T>G) | PMID:40397273 ("30% with cerebellar ataxia"); PMID:35150594 |
| Cerebellar atrophy (MRI) | HP:0001272 | Mainly in ataxia-predominant patients; vermis-predominant in one | PMID:36331550 |
| Sensorimotor / axonal peripheral neuropathy | HP:0003477 Peripheral axonal neuropathy | ~35% of p.Arg19Trp carriers | PMID:40397273: "35% of the combined patients with sensory‒motor polyneuropathy" |
| Impaired vibration sense | HP:0002495 | Occasional | Morsy patient 2 |
| Optic neuropathy | HP:0001138 | Occasional | MedGen/OMIM |
| Nystagmus / ophthalmoparesis (vertical) | HP:0000639; HP:0000597 | Occasional; vertical ophthalmoparesis in 2 ataxic patients | PMID:36331550 |
| Dysarthria | HP:0001260 | Occasional | MedGen |
| Intellectual disability / developmental delay / learning disability | HP:0001249; HP:0001263 | Minority (complicated forms, e.g. p.Arg1624Cys, p.Arg2124Cys) | PMID:35150594; PMID:36331550 |
| Seizures | HP:0001250 | Minority | PMID:35150594 |
| Bladder dysfunction | HP:0000009 Functional abnormality of the bladder | Occasional | Morsy patient 1 |
| Pes cavus, scoliosis, amyotrophy | HP:0001761; HP:0002650; HP:0003202 | Occasional | MedGen; Morsy |
| Tremor, dystonia, myoclonus, paroxysmal dyskinesia | HP:0001337; HP:0001332; HP:0001336; HP:0007166 | Rare | MedGen; Morsy patient 6 |
| Subcortical white-matter hyperintensities | HP:0002500 (verify) | Rare (p.Arg2124Cys) | PMID:36331550 |

**Onset:** congenital to young adult, mostly in the first decade. In the p.Arg19Trp series, onset was typically in childhood or adolescence (Morsy patient 1 at age 8).

**Course:** slowly progressive. The quality-of-life burden comes from impaired mobility and walking aids. **No EQ-5D or SF-36 data have been published.**

---

## 4. Genetic and molecular information

- **Gene:** *SPTAN1*, spectrin alpha, non-erythrocytic 1. HGNC `hgnc:11273` (verify), NCBI Gene 6709 (verify), UniProt Q13813 (verify). Located at 9q34.11.
- **Protein:** αII-spectrin, about 2,472 aa. It has an N-terminal partial repeat (α0) that forms the α/β tetramerization site, 20 spectrin repeats (three-helix bundles), an SH3 domain, a calpain/caspase-cleavage region in repeat α10, and C-terminal EF-hands. The heterodimer nucleation site is in α20–α21.

**Variants reported in SPG91**

| Variant | Type | Phenotype | Origin | Source |
|---|---|---|---|---|
| c.55C>T p.(Arg19Trp) | missense, recurrent hotspot | Pure or complex HSP ± neuropathy ± ataxia | AD (multiple families), de novo | PMID:35150594, 36331550, 40397273 |
| p.(Lys2083del) | in-frame deletion, recurrent (4 patients) | Cerebellar ataxia | de novo | PMID:35150594 |
| p.(Arg1098Cys) | missense | Ataxia | de novo | PMID:35150594 |
| p.(Arg1624Cys) | missense | Ataxia + ID + epilepsy | de novo | PMID:35150594 |
| p.(Gln2205Pro) | missense | Complex spastic-ataxic | de novo | PMID:35150594 |
| p.(Arg2124Cys) | missense | Complex HSP with learning disability and seizures | sporadic | PMID:36331550 |
| p.(Ser2448Phe) | missense | Complex HSP, cerebellar atrophy | unknown | PMID:36331550 |
| Exons 25–27 in-frame deletion | structural | Pure late-adult ataxia | sporadic | PMID:36331550 |
| c.3519+2T>G | splice | Pure ataxia | sporadic | PMID:36331550 |

- **ACMG classification:** check ClinVar for current classifications. p.Arg19Trp is expected to be Pathogenic or Likely Pathogenic given recurrence and segregation. **I did not verify ClinVar records here.**
- **Population frequency:** the disease-associated variants are absent or ultra-rare in gnomAD. Morsy's enrichment threshold was MAF < 1×10⁻⁵.
- **Variant origin:** germline throughout. There is no somatic role.
- **Functional consequence:** probably dominant-negative or structurally disruptive for the missense and in-frame alleles, not simple loss of function.
  - Van de Vondel (PMID:35150594):
    > "mutated amino acids are located at crucial interlinking positions, interconnecting the three-helix bundle of a spectrin repeat… disruption of the interlinking of spectrin helices could be a key feature of the pathomechanism."
  - Morsy (PMID:36331550):
    > "Variant p.(Arg19Trp) had the most deleterious effect on protein structure. This variant is located within the N-terminal tetramerization domain and results in steric clashes with 2 leucine residues in the beta chain." (full text)
  - Lan 2025 (PMID:40397273), computational: p.Arg19Trp is "predicted to perturb the stability of αII/β spectrin heterotetramerization but did not destabilize the tetramerization domain of αII-spectrin."
  - Truncating alleles are linked mainly to hereditary motor neuropathy (via NMD, PMID:31332438) or to mild developmental delay (Morsy), not to SPG91.
  - For the dismech `genetic_context`, a reasonable choice is `functional_impact_category: DOMINANT_NEGATIVE`, with `directness: INDIRECT` because the support is modelling only, or leave the category unasserted. Neither dominant-negative action nor haploinsufficiency has been shown experimentally for the SPG91 alleles specifically.
- **Genotype–phenotype pattern:**
  - p.Arg19Trp, in the N-terminal tetramerization site, gives HSP.
  - Mid-rod and C-terminal in-frame or missense variants give ataxia.
  - In-frame variants at the α20–21 nucleation site give DEE5 (PMID:29050398).
- **Epigenetic or chromosomal changes:** none specific to SPG91. Contiguous 9q34 deletions including *SPTAN1* and *STXBP1* cause encephalopathy or myopathy, which are separate conditions.
- **ClinGen / GenCC:** I did not confirm any gene-disease validity curation specifically for SPG91. Run `just list-gene-validity` and check the ClinGen cache. Leave `gene_disease_validity` absent unless a CGGV record is found.

---

## 5. Environmental information

There are no environmental, lifestyle or infectious factors. Not applicable.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **A heterozygous *SPTAN1* missense or in-frame variant** alters αII-spectrin. Examples are p.Arg19Trp at the α0 tetramerization site and mid-rod variants that break the links between spectrin repeats.
   - This **leads to** destabilised α/β spectrin assembly: heterotetramer formation for Arg19Trp, and repeat folding for rod variants.
   - *Evidence is computational or modelling only* (PMID:35150594, PMID:40397273, PMID:36331550).
2. **Mutant αII-spectrin incorporates into αII/β heterodimers and tetramers** and probably acts dominant-negatively. **This results in** abnormal spectrin aggregation or redistribution.
   - In SPG91 patient fibroblasts, Morsy found "Irregular αII-spectrin aggregation… in fibroblasts derived from 2 patients with p.(Arg19Trp) and p.(Glu2207del) variants" (PMID:36331550; IN_VITRO).
   - The dominant-negative mechanism is better shown for DEE5 alleles (PMID:20493457; PMID:29337302). For SPG91 it is *inferred*.
3. **Disruption of the membrane-associated periodic skeleton (MPS)** in long axons, built from actin, spectrin and ankyrin. **This leads to:**
   - **Branch A, nodes of Ranvier and AIS:** voltage-gated sodium channel and ankyrin-G clustering is lost at nodes, paranodes and the axon initial segment (mouse and zebrafish: PMID:29038240, PMID:29038243, PMID:17331725; DEE5 neurons: PMID:20493457).
   - **Branch B, mechanical vulnerability of axons:** large-diameter myelinated axons cannot withstand the mechanical forces of limb movement. Huang 2017 (PMID:29038243): αII-spectrin-deficient sensory neurons show "severe ataxia due to preferential degeneration of large-diameter myelinated axons."
   - **Branch C, calpain sensitivity:** spectrin cleavage is accelerated. In Sptan1 p.R1098Q mice, the human Arg1098 position, this leads to progressive ataxia and neurodegeneration (PMID:33790315). This is *model-organism evidence at a residue mutated (R1098C) in a human ataxia patient*.
4. **Length-dependent axonal degeneration of corticospinal tract axons**, the longest CNS axons. **This results in** upper motor neuron signs: spastic paraplegia, hyperreflexia and Babinski sign. *This step is inferred from the HSP pathology paradigm. No SPG91 neuropathology exists.*
5. **Degeneration of cerebellar neurons, Purkinje cells, or their afferents** results in cerebellar ataxia and cerebellar atrophy on MRI. *Inferred from MRI and from mouse models (PMID:29038240 widespread neurodegeneration; PMID:33790315).*
6. **Peripheral sensory and motor axon degeneration** results in sensorimotor axonal polyneuropathy (~35% of p.Arg19Trp carriers) and impaired vibration sense.
7. **Less often, developmental effects on the cortex** (dendrite and AIS development, inhibitory synapses; PMID:29337302) result in ID and seizures in "complicated" cases.

### Ontology leads (verify every CURIE)

- **GO biological processes:**
  - actin cytoskeleton organization, GO:0030036
  - axon initial segment / node of Ranvier assembly (search `l~node of Ranvier`, `l~axon initial segment`)
  - axonogenesis, GO:0007409
  - clustering of voltage-gated sodium channels, GO:0045162
  - neuron projection maintenance, GO:1990535
  - axonal degeneration / axon degeneration, GO:0098794 (verify)
- **GO molecular functions:** structural constituent of cytoskeleton, GO:0005200; actin binding, GO:0003779; calmodulin binding, GO:0005516.
- **GO cellular components:** spectrin, GO:0008091; cortical cytoskeleton; node of Ranvier, GO:0033268; axon initial segment, GO:0043194; paranode region of axon, GO:0033270.
- **CL cell types:** upper motor neuron, CL:2000062 (verify); pyramidal neuron, CL:0000598; Purkinje cell, CL:0000121; sensory neuron, CL:0000101; motor neuron, CL:0000100.
- **UBERON sites:** lateral corticospinal tract / corticospinal tract, UBERON:0002707 (verify); cerebellum, UBERON:0002037; spinal cord, UBERON:0002240; peripheral nerve, UBERON:0001021; optic nerve, UBERON:0000941.
- **Biological scale tags:** step 1 MOLECULAR; steps 2–3 CELLULAR; steps 4–6 TISSUE; phenotypes ORGANISM.

### Related dismech modules

Check `just list-modules axon`. Likely candidates are a length-dependent axonopathy/HSP corticospinal module and `peripheral_axonal_degeneration`.

### Molecular profiling

No transcriptomic, proteomic, metabolomic, single-cell or CRISPR-screen data are available for SPG91.

---

## 7. Anatomical structures affected

- **Primary:** corticospinal tracts (upper motor neurons); cerebellum (vermis atrophy in ataxic cases).
- **Secondary:** peripheral nerves (sensorimotor axonal neuropathy); optic nerve (optic neuropathy); cerebral cortex in complicated forms (seizures, ID; subcortical white-matter changes reported once).
- **System:** nervous system.
- **Subcellular:** axonal membrane periodic skeleton, nodes of Ranvier, paranodes, axon initial segment.
- **Distribution:** bilateral and symmetric. Lower limbs are affected before upper limbs.

---

## 8. Temporal development

- **Onset:** congenital to young adult, mostly first decade (OMIM). One pure-ataxia patient was evaluated at 72; the age of onset was not stated.
- **Onset pattern:** insidious.
- **Course:** chronic, slowly progressive, lifelong. There are no formal stages, no remission, and no natural-history registry.
- **Critical periods:** developmental effects of the spectrin skeleton (AIS formation) suggest an early window. This is speculative for SPG91.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant, HP:0000006 (verify). De novo occurrence is frequent, especially in ataxia-predominant cases (4 of 6 ataxia patients de novo in PMID:35150594).
- **Penetrance and expressivity:**
  - Expressivity is variable: pure HSP, HSP with neuropathy or ataxia, and complicated forms all occur with the same p.Arg19Trp variant.
  - Incomplete penetrance has been described for *SPTAN1* truncating HMN alleles ("Variable penetrance was noted", PMID:31332438). For SPG91 alleles, penetrance has not been quantified.
- **Anticipation:** none (not a repeat expansion).
- **Founder effects:** none documented. p.Arg19Trp recurs across unrelated families of different ancestries (European, Taiwanese in Lan 2025), which is consistent with a mutational hotspot (CpG C>T).
- **Prevalence:** unknown. Fewer than about 50 published patients means ultra-rare. In dismech terms: `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE` or `NOT_YET_DOCUMENTED`.
  - As a proxy for yield, Morsy found 12 of 1,142 HA/HSP index families carried rare damaging *SPTAN1* variants, about 1%.
- **Sex ratio:** no bias expected (autosomal). The published cases include both sexes.

---

## 10. Diagnostics

- **Genetic testing is the only way to diagnose SPG91.** Use an HSP/ataxia multigene panel or exome/genome sequencing. *SPTAN1* is on PanelApp HSP, ataxia and neuropathy panels ([Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/entities/SPTAN1); [PanelApp Australia](https://panelapp-aus.org/panels/271/gene/SPTAN1/)).
  - Copy-number analysis (exome CNV calling or CMA) can detect intragenic deletions such as the exons 25–27 deletion.
  - Splice variants may need RNA studies.
- **Imaging:** brain MRI is often normal. It may show cerebellar (vermian) atrophy in ataxic cases. Spinal MRI is used to exclude structural mimics.
- **Electrophysiology:** NCS/EMG to detect axonal sensorimotor neuropathy. Motor evoked potentials can show corticospinal involvement (generic HSP practice).
- **Other tests:** optic coherence tomography or visual evoked potentials if optic neuropathy is suspected. EEG if seizures occur.
- **Biomarkers:** none. Fibroblast αII-spectrin aggregation is a research readout only.
- **Differential diagnosis:**
  - Other AD-HSPs (SPAST/SPG4, ATL1/SPG3A, KIF5A/SPG10, REEP1/SPG31)
  - Spastic ataxias (SACS/ARSACS, SPAX genes, SCA3/ATXN3, SCA1)
  - *SPTBN2* (SCA5)
  - Leukodystrophies
  - Cerebral palsy mimics (*SPTAN1* appears in genetic cerebral-palsy-like cohorts)
  - Structural myelopathy
  - B12 or copper deficiency
- **Screening:** cascade testing of relatives. No newborn or population screening exists.

---

## 11. Outcome and prognosis

- **Life expectancy:** not reported. It is presumably normal in pure forms, since patients are documented at 40–72 years.
- **Morbidity:** progressive gait disability and need for walking aids. Neuropathy, bladder dysfunction, and in complicated cases seizures and ID.
- **Prognostic factors:** possibly genotype (p.Arg19Trp gives HSP; de novo mid-rod variants give ataxia, sometimes with ID or epilepsy). No validated prognostic markers.
- **Quality-of-life data:** none.

---

## 12. Treatment

There is no disease-modifying therapy. Management is the standard symptomatic care for HSP and ataxia.

| Intervention | NCIT (verify) | Notes |
|---|---|---|
| Physical therapy / gait training | NCIT:C15302 Physical Therapy; `therapeutic_modality: BEHAVIORAL` | Mainstay |
| Oral antispasticity pharmacotherapy (baclofen, tizanidine) | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` baclofen CHEBI:2972 (verify), tizanidine (verify) | Generic HSP practice. No SPG91-specific evidence. |
| Botulinum toxin injection | NCIT:C15986 + botulinum toxin agent (verify) | Focal spasticity |
| Intrathecal baclofen | — | Severe cases (generic) |
| Antiseizure medication | NCIT:C15986 | For complicated forms |
| Orthoses / walking aids | `DEVICE` (no NCIT action term) | |
| Occupational therapy | NCIT:C121351 | |
| Bladder management (antimuscarinics) | NCIT:C15986 | |
| Genetic counseling | NCIT:C15240 | |

- **Experimental:** D-aspartate improved motility in *sptan1*-null zebrafish (Lu et al. 2025, PMID:39988451: "supplementation with the amino acid D-aspartate improved motility in sptan1-null zebrafish, supporting its use for α-II spectrin-associated motor dysfunction"). This is preclinical, in a loss-of-function model, and no human trial exists. A caregiver survey of *SPTAN1* families exists (PMID:40261672) but is mainly about the neurodevelopmental phenotypes.
- **Clinical trials:** none found specific to SPG91 or *SPTAN1*.
- **Gene, RNA or cell therapy:** none. Allele-specific knockdown of dominant-negative alleles is a theoretical option.
- **Pharmacogenomics:** not applicable.

---

## 13. Prevention

- **Primary:** none.
- **Reproductive options:** genetic counseling. The recurrence risk is 50% for offspring of an affected parent. For apparently de novo cases, the recurrence risk is low but not zero because of possible germline mosaicism. Prenatal or preimplantation testing is possible once the familial variant is known.
- **Tertiary:** prevent contractures, falls and urinary complications through physiotherapy, orthoses and bladder care.

---

## 14. Other species and natural disease

- I found no naturally occurring *SPTAN1* spastic paraplegia in animals. No OMIA entry was identified.
- αII-spectrin is highly conserved across vertebrates. Orthologs:
  - mouse *Sptan1* (NCBI Gene 20740, verify)
  - zebrafish *sptan1*
  - *Drosophila* α-Spec

---

## 15. Model organisms

| Model | Genotype | Recapitulation | Limitations | Source |
|---|---|---|---|---|
| Mouse, CNS conditional KO (Nestin-cre; Sptan1f/f) | Null | AIS loss, seizures, cortical lamination defects, widespread neurodegeneration, death before 1 month | Null allele; more severe than the heterozygous human disease; models DEE more than HSP | PMID:29038240 |
| Mouse, sensory-neuron KO (Avil-cre; Sptan1f/f) | Null in DRG neurons | Ataxia from preferential degeneration of large-diameter myelinated axons; node and paranode disruption | Peripheral only; no corticospinal involvement | PMID:29038243 |
| Mouse, Sptan1 p.R1098Q knock-in (heterozygous) | Point mutation at the human Arg1098 residue (human R1098C causes ataxia) | Progressive ataxia, accelerated calpain cleavage of spectrin, axonal and dendritic disruption, neurodegeneration; memory deficits and seizures (PMID:36831804) | Different substitution (Gln vs Cys); spasticity not reported | PMID:33790315, PMID:36831804 |
| Rat, in utero CRISPR deletion / overexpression of human mutants | Somatic KO or overexpression | Dendritic and axonal defects, AIS loss | DEE5-focused | PMID:29337302 |
| Zebrafish *αII-spn* mutant | Loss of function | Nodes of Ranvier fail to assemble; Na⁺ channel clusters disrupted | Developmental; loss of function rather than dominant-negative | PMID:17331725 |
| Zebrafish *sptan1*-null + variant rescue | Loss of function | Motility defect, Nav mislocalization; D-aspartate rescue | Patient variants not SPG91 alleles | PMID:39988451 |
| Patient fibroblasts (p.Arg19Trp, p.Glu2207del) | Heterozygous | Irregular αII-spectrin aggregation | Non-neuronal | PMID:36331550 |
| Patient iPSC-derived neurons (DEE5 alleles) | Heterozygous | Spectrin aggregation, developmental defects | DEE5, not SPG91 | PMID:29337302 |

- **Model gap:** no model carrying an SPG91 allele (e.g. p.Arg19Trp knock-in) or iPSC-derived corticospinal motor neurons from an SPG91 patient has been reported.
- **Mismatch:** null and conditional KO models over-represent developmental and epileptic features compared with the human dominant-allele disease. This could be recorded as a `HUMAN_MODEL_MISMATCH` discussion.

---

## Key citations (Europe PMC verified)

| PMID | Reference | Role |
|---|---|---|
| 35150594 | Van de Vondel L et al. *Mov Disord* 2022. De Novo and Dominantly Inherited SPTAN1 Mutations Cause Spastic Paraplegia and Cerebellar Ataxia. | Defining cohort |
| 36331550 | Morsy H et al. *Genet Med* 2023. Expanding SPTAN1 monoallelic variant associated disorders… | Enrichment, 10 HSP/HA patients, fibroblasts. Open access: [PMC10620943](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620943/) |
| 40397273 | Lan SC et al. *Mol Biol Rep* 2025. Recurrent SPTAN1 mutation causing SPG91. | p.Arg19Trp genotype–phenotype |
| 39988451 | Lu PN et al. *Clin Genet* 2025. | LoF variants, zebrafish, D-aspartate |
| 41338915 | Roshwanth AR et al. *BMJ Case Rep* 2025. Novel SPTAN1 variant mimicking HSP. | Case report; abstract not retrieved |
| 31332438 | Beijer D et al. *Brain* 2019. | Allelic HMN, NMD |
| 33578420 | Dong HL et al. *Brain* 2021. | Allelic HMN |
| 31515523; 34526651 | Leveille 2019; Xie 2022, *J Hum Genet* | Proposed AR-HSP |
| 20493457 | Saitsu H et al. *AJHG* 2010 | Dominant-negative DEE5 |
| 29050398 | Syrbe S et al. *Brain* 2017 | SPTAN1 phenotype and domain map |
| 29337302 | Wang Y et al. *JCI* 2018 | Neurodevelopment, dominant-negative mechanism |
| 29038240; 29038243 | Huang CY et al. *J Neurosci* 2017 | Mouse models |
| 33790315; 36831804 | Miazek 2021; Zalas 2023 | R1098Q mouse |
| 17331725 | Voas MG et al. *Curr Biol* 2007 | Zebrafish nodes of Ranvier |
| 40999194 | Van de Vondel L et al. *EJHG* 2026 | 9q34 deletion, distal myopathy |

---

## Gaps for the entry

- **Not established:** prevalence; ClinGen/GenCC validity; neuropathology; any SPG91-allele model; experimental proof of the dominant-negative versus haploinsufficiency mechanism for p.Arg19Trp; quality-of-life data.
- **Curation risk, Named Entity Confusion:** do not import DEE5, HMN or AR-HSP evidence as SPG91 phenotypes. Use it only as mechanistic, gene-level support, with `directness: INDIRECT`.
- **Next steps:**
  - Run `just fetch-reference PMID:35150594` and `just fetch-reference PMID:36331550` (and the others) before quoting.
  - Run `just preflight-dr <report> MONDO:0957813`.
  - Validate every CURIE above.

Sources:
- [MedGen 1846222](https://www.ncbi.nlm.nih.gov/medgen/1846222)
- [MalaCards SPG91](https://www.malacards.org/card/spastic_paraplegia_91_autosomal_dominant_with_or_without_cerebellar_ataxia)
- [Disease Ontology DOID:0070643](https://disease-ontology.org/term/DOID:0070643)
- [Morsy et al. 2023, PMC10620943](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620943/)
- [Genomics England PanelApp SPTAN1](https://panelapp.genomicsengland.co.uk/panels/entities/SPTAN1)
- [PanelApp Australia SPTAN1](https://panelapp-aus.org/panels/271/gene/SPTAN1/)
- [Gene Table of Neuromuscular Disorders ref 35150594](https://www.musclegenetable.fr/4DACTION/disease_cherche_ref/1304_35150594)
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search) (abstract retrieval for all PMIDs above)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 14 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:36331550`: "Irregular αII-spectrin aggregation… in fibroblasts derived from 2 patients with p.(Arg19Trp) and p.(Glu2207del) variants"
  - closest text in source: "Irregular αII-spectrin aggregation was noted in fibroblasts derived from 2 patients with p.(Arg19Trp) and p.(Glu2207del) variants"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:17331725` (2 mentions) - alphaII-spectrin is essential for assembly of the nodes of Ranvier in myelinated axons.
  - shared terms: spectrin

Weighed against this report's own most characteristic terms: `sptan1`, `spg91`, `ataxia`, `hsp`, `variant`, `patient`, `arg19trp`, `motor`, `spastic`, `verify`, `gene`, `seizure`, `cerebellar`, `morsy`, `neuropathy`, `phenotype`, `paraplegia`, `dominant-negative`, `ii-spectrin`, `spectrin`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 58 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957813` (3 mentions) - the report calls it "MONDO"; MONDO calls it **spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia**
- `DOID:0070643` (5 mentions) - the report calls it "Disease Ontology"; DOID calls it **hereditary spastic paraplegia 91**
- `HP:0002500` (1 mention) - the report calls it "verify"; HP calls it **Abnormal cerebral white matter morphology**
- `GO:0098794` (1 mention) - the report calls it "verify"; GO calls it **postsynapse**
- `CL:2000062` (1 mention) - the report calls it "verify"; CL calls it **placental villus capillary endothelial cell**
- `UBERON:0002707` (1 mention) - the report calls it "verify"; UBERON calls it **corticospinal tract**
- `HP:0000006` (1 mention) - the report calls it "verify"; HP calls it **Autosomal dominant inheritance**
- `NCIT:C15986` (4 mentions) - the report calls it "Antiseizure medication", "Bladder management (antimuscarinics)"; NCIT calls it **Pharmacotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001272` (1 mention) - the report calls it "Cerebellar atrophy (MRI)"; HP calls it **Cerebellar atrophy**
- `HP:0002495` (1 mention) - the report calls it "Impaired vibration sense"; HP calls it **Impaired vibratory sensation**, and lists "Impaired vibratory sense" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15986` - called "Antiseizure medication", "Bladder management (antimuscarinics)"