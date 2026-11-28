---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-27T23:10:27.185800'
end_time: '2026-11-27T23:13:07.088750'
duration_seconds: 159.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pleural Empyema
  mondo_id: MONDO:0018667
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: pleural empyema (disease)
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
  web_search_requests: 16
  num_turns: 22
  total_cost_usd: 0.9642681
  session_id: 54ea8055-e6e7-4675-aee1-c9d386812480
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 21
  retrieval_calls: 17
  assistant_text_blocks: 2
citation_count: 34
reference_validation:
  total_references: 21
  verified: 20
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.048
  quotes_checked: 3
  quotes_valid: 1
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMC:PMC4466426
  - PMC:PMC5142452
  quotes_not_checkable: 3
  relevance_assessed: 20
  on_topic: 14
  unresolved_references:
  - PMC:PMC4896893
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 46
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 17
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 3
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0018667
    reported_labels:
    - MONDO
    ontology_label: pleural empyema
  - term_id: HP:0002094
    reported_labels:
    - Symptom
    ontology_label: Dyspnea
  - term_id: HP:0012735
    reported_labels:
    - Symptom
    ontology_label: Cough
  - term_id: HP:0000975
    reported_labels:
    - Symptom
    ontology_label: Hyperhidrosis
  - term_id: HP:0002202
    reported_labels:
    - Sign / imaging
    ontology_label: Pleural effusion
  - term_id: HP:0100587
    reported_labels:
    - Pleural empyema; verify the term
    ontology_label: Abnormal preputium morphology
  - term_id: HP:0025330
    reported_labels:
    - verify
    ontology_label: Downgaze palsy
  - term_id: HP:0001824
    reported_labels:
    - Symptom
    ontology_label: Weight loss
  labels_variant: 3
  service_unreachable: 15
  obsolescence_unchecked: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pleural Empyema
- **MONDO ID:** MONDO:0018667 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** pleural empyema (disease)
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pleural Empyema** covering all of the
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

Still gathering sources: five searches done (MIST2, RAPID, microbiology, BTS 2023, epidemiology). Next I'm covering pathophysiology, animal models, children and vaccines, and surgery.

# Pleural Empyema (MONDO:0018667): Disease Characteristics Report

**How I read the request:** Pleural empyema is an acquired infectious disease, not a Mendelian one. The template lists no causal gene, and I found no evidence of one. **No causal gene applies.** Sections 4 and 9 that ask about genetics are marked not applicable. Where a PubMed ID (PMID) came up in my searches I cite it; otherwise I cite the URL or DOI. PubMed's E-utilities could not be queried directly in this session, so PMIDs are given only where a search surfaced them. All quotes are taken from search-result excerpts, not from full texts I read.

---

## 1. Disease Information

**Overview.** Pleural empyema is pus in the pleural space. Disease Ontology describes it as an "accumulation of pus in the pleural cavity", usually from pneumonia or a lung abscess spreading into that space, with cough, fever, chest pain, sweating and shortness of breath ([DOID:3798](https://disease-ontology.org/term/DOID:3798/owl)). MeSH defines it as "suppurative inflammation of the pleural space" ([MeSH D016724](https://meshb.nlm.nih.gov/record/ui?ui=D016724)). It is the far end of the spectrum of pleural infection, which runs from simple parapneumonic effusion through complicated effusion to frank pus.

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0018667 |
| MeSH | D016724 "Empyema, Pleural" ([NLM](https://meshb.nlm.nih.gov/record/ui?ui=D016724)) |
| Disease Ontology | DOID:3798 ([DO](https://disease-ontology.org/term/DOID:3798/owl); [MGI](https://www.informatics.jax.org/disease/DOID:3798)) |
| ICD-10(-CM) | J86 (pyothorax), via the DO cross-reference |
| ICD-9-CM | 510.9 (DO cross-reference) |
| UMLS/MedGen | C0014013 ([MedGen](https://ncbi.nlm.nih.gov/medgen/C0014013)) |
| OMIM / Orphanet | None. It is not a rare genetic disease |

**Synonyms:** pyothorax, thoracic empyema ("Empyema, Thoracic" in MeSH), pleural empyema (disease), purulent pleurisy, and pleural infection (the broader term used in the literature).

**Source type:** Everything here comes from aggregated disease-level resources: guidelines, trials, cohorts and administrative datasets.

## 2. Etiology

- **Cause:** bacterial invasion of the pleural space. The main routes are:
  - spread from pneumonia (parapneumonic, the most common route);
  - iatrogenic or post-surgical infection;
  - trauma;
  - oesophageal rupture;
  - spread of infection from below the diaphragm, or through the blood.
- **Risk factors in adults:** "immunosuppression, diabetes, poor oral hygiene, gastro-oesophageal reflux, alcohol excess and intravenous drug use are known to independently predict increased risk of progression of pneumonia to pleural infection" ([PMC4953430](https://pmc.ncbi.nlm.nih.gov/articles/PMC4953430); [PMC4466426](https://pmc.ncbi.nlm.nih.gov/articles/PMC4466426)).
  - Anaerobic infection usually follows aspiration or poor oral hygiene.
  - Some patients have no identifiable risk factor.
  - Comorbidity is common: a systematic review found a median comorbidity prevalence of 72% ([Hassan et al. 2021, IJGM](https://www.dovepress.com/recent-insights-into-the-management-of-pleural-infection-peer-reviewed-fulltext-article-IJGM)).
- **Age:** incidence is skewed toward older adults ([Cargill et al. 2019, ERJ Open, PMC6860993](https://pmc.ncbi.nlm.nih.gov/articles/PMC6860993)). There is a second peak in young children.
- **Genetic risk factors:** none established. I retrieved no GWAS, ClinVar or ClinGen associations. Primary immunodeficiencies predispose to pyogenic infection in general, but I retrieved no empyema-specific data on them.
- **Protective factors:**
  - Pneumococcal conjugate vaccination lowered empyema hospitalisations in US children ([PMID 27832918](https://pubmed.ncbi.nlm.nih.gov/27832918/)).
  - Prompt antibiotic treatment of pneumonia is protective (inferred).
- **Gene–environment interactions:** none described in the sources.

## 3. Phenotypes

The sources gave no per-symptom frequency data, so frequencies are qualitative.

| Phenotype | Type | HPO suggestion | Notes |
|---|---|---|---|
| Fever | Sign | HP:0001945 | Common ([DOID:3798](https://disease-ontology.org/term/DOID:3798/owl)) |
| Pleuritic chest pain | Symptom | HP:0033771 (Pleuritic chest pain) / HP:0100749 | Common |
| Dyspnoea | Symptom | HP:0002094 | Common |
| Cough | Symptom | HP:0012735 | Common |
| Sweating / night sweats | Symptom | HP:0000975 | Frequent |
| Pleural effusion | Sign / imaging | HP:0002202 | Present by definition |
| Pleural empyema | Sign | HP:0100587 (Pleural empyema; verify the term) | Present by definition |
| Pleural thickening / fibrothorax | Imaging | HP:0025330 (verify) | In the organising stage |
| Pleural fluid acidosis (pH ≤7.2) | Laboratory | (no exact term; suggest a new term) | Strongly associated ([BTS 2023 table, PMC10790177](https://pmc.ncbi.nlm.nih.gov/articles/PMC10790177/table/TB2)) |
| Low pleural glucose / high LDH | Laboratory | — | Sign of complicated effusion |
| Raised CRP, leukocytosis | Laboratory | HP:0011227, HP:0001974 | Common |
| Weight loss | Symptom | HP:0001824 | Seen with subacute anaerobic disease |
| Sepsis | Sign | HP:0100806 | Seen in severe cases |

**Onset and course:** onset is acute or subacute. Anaerobic infections often run a more indolent course. Severity ranges from moderate to severe.

**Quality of life:** in MIST-3, the EQ-5D-5L utility index rose from 0.35 at baseline to 0.83 at 2 months in the intrapleural-enzyme arm. That is a severe acute quality-of-life burden that largely recovers ([MIST-3, PMC10765402](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10765402/)).

## 4. Genetic/Molecular Information

**Not applicable.** No causal genes, pathogenic variants, modifier genes, epigenetic signatures or chromosomal abnormalities have been described for human empyema in the sources I retrieved.

The host genes that matter here have been studied only in mouse models (Section 15):
- **SERPINE1 / PAI-1** (HGNC:8583). PAI-1-deficient mice "died within 4 days, had increased pleural inflammation" ([Tucker et al. 2016, PMC4896893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4896893/)).
- **PLAUR / uPAR** (HGNC:9053). uPAR-knockout mice "were protected from S. pneumoniae-mediated decrements in lung function" ([Logan et al. 2021, Sci Rep](https://www.nature.com/articles/s41598-021-99520-5.pdf)).

## 5. Environmental Information

**Lifestyle factors:** alcohol excess, intravenous drug use, poor dental hygiene and aspiration risk (Section 2). I retrieved no occupational or toxic exposures.

**Infectious agents.** 16S rRNA next-generation sequencing of 243 pleural fluid samples from the PILOT cohort (the TORPIDS study) found the following ([Kanellakis et al., Lancet Microbe 2022, PMC8967721](https://pmc.ncbi.nlm.nih.gov/articles/PMC8967721/)):
- "Pleural infection was predominately polymicrobial (192 [79%] of 243 samples), with mixed anaerobes and other Gram-negative bacteria dominating community-acquired polymicrobial infection."
- *Streptococcus pneumoniae* (NCBITaxon:1313) dominated monomicrobial infection.
- Survival was better when anaerobes were present (HR 0.46) and when the *Streptococcus anginosus* group (NCBITaxon:1328, the milleri group) was present (HR 0.43).
- Survival was worse when *Staphylococcus aureus* (NCBITaxon:1280) or Enterobacteriaceae dominated.

Other studies agree:
- Norwegian and Mayo Clinic series found that *S. intermedius* (NCBITaxon:1338) and *Fusobacterium nucleatum* (NCBITaxon:851), both oral bacteria, dominate community-acquired disease ([PMC10474564](https://pmc.ncbi.nlm.nih.gov/articles/PMC10474564); [PMID 16840746](https://www.pubmed.gov/16840746/)).
- A combined culture and sequencing study of 434 infections found about 50% of community-acquired cases were streptococcal and 20% included anaerobes.

**Paediatric pathogens:** after PCV13, *S. pneumoniae* serotype 3 became the leading pneumococcal cause in Germany ([PMID 31735502](https://pubmed.ncbi.nlm.nih.gov/31735502/)), Portugal ([EID 2018](https://wwwnc.cdc.gov/eid/article/24/7/18-0029_article)) and Australia ([Thorax](https://thorax.bmj.com/content/76/5/487.full)).

## 6. Mechanism / Pathophysiology

**Causal chain** (from reviews: [PMC8286963](https://pmc.ncbi.nlm.nih.gov/articles/PMC8286963); [NBK534297](https://www.ncbi.nlm.nih.gov/books/NBK534297/); [PMC4466426](https://pmc.ncbi.nlm.nih.gov/articles/PMC4466426); [Tucker 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4896893/)):

1. Bacterial pneumonia, or another source (surgery, trauma, oesophageal rupture, spread through the blood), **leads to** inflammation of the visceral pleura next to the infection.
2. Inflammation of the visceral pleura **results in** "increased permeability of the cells lining the pleural membrane", with "proinflammatory mediators, such as TNFα, IL6, and IL8" driving exudate formation. This is the **exudative stage**: sterile, clear, neutrophil-rich fluid.
3. If the infection is not controlled, bacteria invade the pleural space, which "further enhances the inflammatory response and **leads to** the activation of the coagulation cascade, which in turn promotes fibrin deposition".
   - Branch 3a: suppressed fibrinolysis. High pleural PAI-1 inhibits tPA and uPA, so fibrin persists. High pleural PAI-1 "is associated with loculation risk" ([Komissarov, PMC5142452](https://pmc.ncbi.nlm.nih.gov/articles/PMC5142452)).
   - Branch 3b: neutrophil recruitment and bacterial metabolism **lead to** glucose consumption, lactic acid and CO₂ production, and so to low pH and glucose and high LDH. This is the **fibrinopurulent stage**.
4. Fibrin septation **results in** loculation. Loculation hampers drainage, and neutrophil-extracellular DNA together with cellular debris makes the pus more viscous. Breaking down this DNA is the inferred rationale for using DNase.
5. If the infection persists, fibroblasts turn the fibrin membranes into "a thick nonelastic pleural peel" (TGF-β is implicated). This is the **organising stage**.
6. The pleural peel **leads to** a trapped lung, restrictive lung function and fibrothorax. Alternatively, systemic spread **leads to** sepsis and death.

**Coverage of the checklist**

| Aspect | Findings |
|---|---|
| Pathways | Innate cytokine signalling (TNF, IL-6, IL-8); coagulation cascade; plasminogen activation system (PAI-1/uPA/uPAR); TGF-β-driven fibrosis |
| Suggested GO terms | inflammatory response GO:0006954; neutrophil chemotaxis GO:0030593; blood coagulation GO:0007596; fibrinolysis GO:0042730; negative regulation of fibrinolysis GO:0051918; neutrophil extracellular trap formation GO:0140645; extracellular matrix organization GO:0030198; fibroblast proliferation GO:0048144 |
| Suggested CL terms | mesothelial cell CL:0000077; neutrophil CL:0000775; macrophage CL:0000235; fibroblast CL:0000057 |
| Metabolic changes | Anaerobic glycolysis and lactate accumulation (CHEBI:24996 lactate; CHEBI:17234 glucose) in the pleural fluid |
| Molecular profiling | Microbiome profiling by 16S sequencing (Section 5). I retrieved no single-cell, spatial or proteomic datasets |

## 7. Anatomical Structures Affected

- **Primary site:** pleural cavity (UBERON:0002402), visceral pleura (UBERON:0002401) and parietal pleura (UBERON:0002400).
- **Adjacent and secondary sites:**
  - lung (UBERON:0002048);
  - chest wall (empyema necessitans);
  - systemic involvement through sepsis.
- **Body system:** respiratory.
- **Tissue level:** mesothelium (UBERON:0000042) and serous membrane connective tissue.
- **Subcellular level:** the extracellular space (GO:0005615) is where fibrin and NET DNA accumulate.
- **Laterality:** usually unilateral, on the same side as the pneumonia.

## 8. Temporal Development

- **Onset:** acute to subacute.
- **Stages:** the three stages (exudative, then fibrinopurulent, then organising) develop over days to weeks. One source says the exudative stage lasts "roughly 2 to 5 days" from the onset of pneumonia, while others describe progression within hours without treatment ([PMC8286963](https://pmc.ncbi.nlm.nih.gov/articles/PMC8286963)).
- **Course:** self-limited with treatment. Becoming chronic means progression to fibrothorax.
- **Critical window:** early drainage, before organisation sets in. MIST-3 tested intervention within about 24 hours of standard care failing ([PMC10765402](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10765402/)).

## 9. Inheritance and Population

**Inheritance:** not applicable. The disease is acquired, and there is no penetrance, anticipation, founder effect or carrier frequency to report.

**Incidence**
- United States, 1996–2008: parapneumonic empyema hospitalisations rose from 3.04 to 5.98 per 100,000, a 2.0-fold increase. Over the period there were about 157,094 hospitalisations, 18,200 of them in 2008 alone. Staphylococcal empyema rose 3.3-fold and non-pneumococcal streptococcal empyema 1.9-fold ([Grijalva et al., Thorax 2011, PMID 21617169](https://www.pubmed.gov/21617169/); [PMC4820002](https://pmc.ncbi.nlm.nih.gov/articles/PMC4820002)).
- US children under 5: rates rose 2.81-fold, from 3.7 to 10.3 per 100,000, between 1996–98 and 2005–07 (before PCV13).
- Western countries in the 2010s: 6.7–9.9 per 100,000, nearly double the rate of the previous decade ([Hassan et al. 2021](https://www.dovepress.com/recent-insights-into-the-management-of-pleural-infection-peer-reviewed-fulltext-article-IJGM)).
- Current trend: incidence "is increasing across the Western World", and the reason, particularly among older people, is unclear (Elsheikh et al., Breathe 2024).

**Demographics**
- Mean age at diagnosis is 58–63 years in Europe, North America and Australia.
- Men are reported to be affected more often, but I retrieved no exact sex ratio.

## 10. Diagnostics

**Pleural fluid analysis.** The BTS 2023 thresholds ([PMC10790177 table](https://pmc.ncbi.nlm.nih.gov/articles/PMC10790177/table/TB2)) are:

| Finding | Likelihood of pleural infection | Action |
|---|---|---|
| pH ≤7.2 | High | Insert a chest drain |
| pH 7.2–7.4 | Intermediate | Check LDH and glucose |
| pH ≥7.4 | Low | No drainage needed |
| Pus | Diagnostic | Drain |

Malignancy and other inflammatory causes can also push the pH below 7.2.

**Microbiology:** send ≥25 mL of fluid, ideally 50 mL, in both plain and blood-culture bottles ([BTS 2023](https://thorax.bmj.com/content/78/11/1143)). 16S and next-generation sequencing pick up many organisms that culture misses (Section 5).

**Imaging**
- Ultrasound shows septations and loculation.
- Contrast CT shows the "split pleura" sign.
- BTS advises against PET-CT. It recommends CT follow-up if symptoms persist, to exclude occult malignancy.

**Genetic testing:** not applicable.

**Differential diagnosis:** malignant effusion, tuberculous pleuritis, rheumatoid pleurisy and lung abscess.

## 11. Outcome/Prognosis

- **Mortality** (PILOT, n=542): 10% at 3 months and 19% at 12 months ([Corcoran et al., ERJ 2020;56:2000130](https://publications.ersnet.org/content/erj/56/5/2000130)).
- **US in-hospital case fatality:** 8.0% in 1996 and 7.2% in 2008 ([PMC4820002](https://pmc.ncbi.nlm.nih.gov/articles/PMC4820002)).
- **RAPID score** (Renal function, Age, Purulence, Infection source, Dietary factors):
  - 3-month mortality by risk group was 2.3% for low risk (score 0–2), 9.2% for medium (3–4) and 29.3% for high (5–7).
  - Discrimination (C-statistic) was 0.78 at 3 months.
- **Microbiological prognostic factors:** *S. aureus* or Enterobacteriaceae dominance predicts worse outcome; anaerobes predict better outcome ([TORPIDS](https://pmc.ncbi.nlm.nih.gov/articles/PMC8967721/)).
- **Complications:** trapped lung or fibrothorax, bronchopleural fistula, empyema necessitans, sepsis, and the need for surgery.

## 12. Treatment

**Antibiotics** (NCIT: Antibiotic Therapy). These should cover anaerobes in community-acquired disease. In a rabbit empyema study, penicillin and metronidazole reached equilibrium with infected pleural fluid fastest ([Chest 2000, qxmd 10858410](https://www.qxmd.com/r/10858410)).

**Chest tube drainage** (NCIT: Thoracostomy). BTS favours a small-bore tube, noting that tubes larger than 14F may cause more pain.

**Intrapleural therapy**
- **Streptokinase, MIST1** (n=454): death or surgery occurred in 31% with streptokinase versus 27% with placebo (RR 1.14, P=0.43), with more adverse events on streptokinase. The authors concluded that "intrapleural streptokinase does not improve mortality, the rate of surgery, or the length of the hospital stay" ([Maskell et al., NEJM 2005;352:865, DOI 10.1056/NEJMoa042473](https://discovery-pp.ucl.ac.uk/id/eprint/6764/1/6764.pdf)).
- **tPA plus DNase, MIST2** (n=210, 2×2 factorial): radiographic opacity fell by about 29.5% with the combination versus 17.2% with placebo. The combination also reduced surgical referral and length of stay, while neither agent alone beat placebo ([Rahman et al., NEJM 2011;365:518, PMID 21830966](https://mdedge.com/content/combined-tpa/dnase-benefits-pleural-infection-patients)).
- **BTS 2023:** recommends against single-agent tPA or DNase ([Thorax 78:1143](https://thorax.bmj.com/content/78/11/1143)).
- Suggested NCIT terms: Alteplase; Dornase Alfa.

**Surgery** (VATS or thoracotomy decortication)
- **Cochrane review** (8 RCTs, n=391): no difference in mortality, but VATS shortened hospital stay ([Redden et al. 2017, CD010651](https://www.cochrane.org/CD010651)).
- **MIST-3 feasibility RCT** (60 randomised, ISRCTN18192121):
  - median time to intervention was 1.0 day for enzyme therapy versus 3.5 days for VATS;
  - length of stay was about 7 days in both intervention arms versus 10 days with standard care;
  - EQ-5D improved more with enzyme therapy ([PMC10765402](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10765402/)).

**Pharmacogenomics, gene therapy and cell therapy:** not applicable.

**Treatment sequence:**
1. antibiotics;
2. drainage if the fluid is purulent or pH ≤7.2;
3. tPA/DNase if drainage fails;
4. surgery, or as an early alternative to step 3, as being tested in MIST-3.

## 13. Prevention

- **Primary prevention:** pneumococcal conjugate vaccines. In the US, empyema hospitalisations fell after PCV13 ([PMID 27832918](https://pubmed.ncbi.nlm.nih.gov/27832918/)). Serotype 19A was essentially eliminated in Mexican surveillance ([PMC6448099](https://pmc.ncbi.nlm.nih.gov/articles/PMC6448099)). PCV13 works less well against serotype 3, which has become a growing share of remaining cases ([PMID 31735502](https://pubmed.ncbi.nlm.nih.gov/31735502/)).
- **Secondary prevention:** early pleural sampling in pneumonia with effusion.
- **Tertiary prevention:** RAPID-based risk stratification, and timely drainage to prevent organisation.
- **Behavioural measures:** dental hygiene and reducing alcohol and injection-drug use. These are inferred from the risk factors; no trials were retrieved.
- **Genetic counselling:** not applicable.

## 14. Other Species / Natural Disease

**Cats** (*Felis catus*, NCBITaxon:9685), where the disease is called feline pyothorax:
- In an Australian series of 27 cases, 78% had a "mixed anaerobic bacterial infection of oropharyngeal origin" ([PMID 16055006](https://pubmed.ncbi.nlm.nih.gov/16055006/)).
- Common organisms include *Pasteurella multocida* (NCBITaxon:747), *Fusobacterium*, *Bacteroides* and *Actinomyces*.
- Survival to discharge is 46–78% in reported series, and mortality is highest in the first 48 hours ([PMC8406089](https://pmc.ncbi.nlm.nih.gov/articles/PMC8406089); [PMC10229369](https://pmc.ncbi.nlm.nih.gov/articles/PMC10229369)).

**Dogs** (NCBITaxon:9615) also get pyothorax.

**Comparative biology:** the oral-anaerobic, polymicrobial pattern seen in cats resembles human community-acquired disease. Pyothorax is not zoonotic in itself.

**Genetics:** no OMIA or breed entries were retrieved.

## 15. Model Organisms

| Model | Induction | Recapitulation | Source |
|---|---|---|---|
| Rabbit (NCBITaxon:9986), *P. multocida* or *S. pneumoniae* | Intrapleural bacteria | Adhesions visible on ultrasound, fibrinous pleural coating, fibrinopurulent effusion; used to test fibrinolytic dose response | [PMC5142452](https://pmc.ncbi.nlm.nih.gov/articles/PMC5142452) |
| Rabbit, chemical injury | Tetracycline or turpentine | Sterile pleural injury; pleural fluid acidosis and low glucose (Sahn's turpentine model) | same |
| Mouse (C57BL/6J), *S. pneumoniae* D39 | Intrapleural infection | Empyema by 24 h, lung restriction, and pleural fibrosis persisting up to 14 days | [Tucker 2016, PMC4896893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4896893/) |
| Mouse knockouts | *Serpine1*⁻/⁻ (PAI-1), *Plaur*⁻/⁻ (uPAR) | PAI-1 loss: more inflammation and early death. uPAR loss: protected lung function | Tucker 2016; [Logan 2021](https://www.nature.com/articles/s41598-021-99520-5.pdf) |

**Limitations:**
- These models are mostly monomicrobial, unlike typical human disease.
- They use young, healthy animals without comorbidities.
- Earlier mouse models killed the animals within about 48 hours.

**Resources:** MGI ([DOID:3798](https://www.informatics.jax.org/disease/DOID:3798)).

---

**Gaps:**
- PMIDs could not be retrieved for several key papers, including MIST1, MIST-3, BTS 2023 and TORPIDS; DOIs and URLs are given instead.
- There are no data on human genetic susceptibility, no omics datasets beyond microbiome sequencing, and no HPO frequency data per symptom.
- HPO IDs marked "verify" should be checked against the ontology before use.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 2 |
| Quoted claims with nothing to check against | 3 |
| References weighed for topical relevance | 20 |
| On topic | 14 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMC:PMC4896893` (6 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC4466426`: "immunosuppression, diabetes, poor oral hygiene, gastro-oesophageal reflux, alcohol excess and intravenous drug use are known to independently predict increased risk of progression of pneumonia to pleural infection"
  - closest text in source: "Independent risk factors for the development of empyema include diabetes, immunosuppression, gastro-esophageal reflux disease, alcohol and intravenous drug abuse, aspiration, and poor oral hygiene (18)"
- `PMC:PMC5142452` *(abstract only)*: "is associated with loculation risk"
  - closest text in source: "Similar to human EMP, rabbits with EMP accumulated sizable, 20- to 40-ml fibrinopurulent pleural effusions associated with extensive intrapleural organization, significantly increased pleural thickness, suppression of fibrinolytic and plasminogen-activating activities, and accumulation of high levels of plasminogen activator inhibitor 1, plasminogen, and extracellular DNA"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMC:PMC4953430`: "immunosuppression, diabetes, poor oral hygiene, gastro-oesophageal reflux, alcohol excess and intravenous drug use are known to independently predict increased risk of progression of pneumonia to pleural infection"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC4896893`: "died within 4 days, had increased pleural inflammation"
  - Reference did not resolve, so the quote could not be checked
- `DOI:10.1056/NEJMoa042473`: "intrapleural streptokinase does not improve mortality, the rate of surgery, or the length of the hospital stay"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 17 |
| Terms whose name was checked | 14 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018667` (2 mentions) - the report calls it "MONDO"; MONDO calls it **pleural empyema**
- `HP:0002094` (1 mention) - the report calls it "Symptom"; HP calls it **Dyspnea**
- `HP:0012735` (1 mention) - the report calls it "Symptom"; HP calls it **Cough**
- `HP:0000975` (1 mention) - the report calls it "Symptom"; HP calls it **Hyperhidrosis**
- `HP:0002202` (1 mention) - the report calls it "Sign / imaging"; HP calls it **Pleural effusion**
- `HP:0100587` (1 mention) - the report calls it "Pleural empyema; verify the term"; HP calls it **Abnormal preputium morphology**
- `HP:0025330` (1 mention) - the report calls it "verify"; HP calls it **Downgaze palsy**
- `HP:0001824` (1 mention) - the report calls it "Symptom"; HP calls it **Weight loss**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1280` (1 mention) - the report calls it "Staphylococcus aureus", "Survival was worse when *Staphylococcus aureus"; NCBITaxon calls it **Staphylococcus aureus**
- `NCBITaxon:1338` (1 mention) - the report calls it "S. intermedius"; NCBITaxon calls it **Streptococcus intermedius**
- `UBERON:0002402` (1 mention) - the report calls it "Primary site:** pleural cavity"; UBERON calls it **pleural cavity**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:1280` - called "Staphylococcus aureus", "Survival was worse when *Staphylococcus aureus"
- `NCBITaxon:747` - called "Pasteurella multocida", "Common organisms include *Pasteurella multocida"

### Terms the ontology service could not be reached for

15 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0001945` (1 mention)
- `HP:0033771` (1 mention)
- `HP:0011227` (1 mention)
- `HP:0100806` (1 mention)
- `NCBITaxon:851` (1 mention)
- `GO:0007596` (1 mention)
- `GO:0042730` (1 mention)
- `GO:0048144` (1 mention)
- `CL:0000077` (1 mention)
- `CL:0000235` (1 mention)
- `CL:0000057` (1 mention)
- `UBERON:0000042` (1 mention)
- `GO:0005615` (1 mention)
- `NCBITaxon:747` (1 mention)
- `NCBITaxon:9615` (1 mention)

### Terms whose obsolescence could not be checked

8 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `DOID:3798` (11 mentions)
- `HP:0002094` (1 mention)
- `HP:0001974` (1 mention)
- `NCBITaxon:1313` (1 mention)
- `NCBITaxon:1280` (1 mention)
- `GO:0030198` (1 mention)
- `CHEBI:24996` (1 mention)
- `UBERON:0002402` (1 mention)