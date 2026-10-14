---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-6[1m]
cached: false
start_time: '2026-10-09T20:15:30.081755'
end_time: '2026-10-09T20:21:54.688317'
duration_seconds: 384.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Parathyroid Gland Carcinoma
  mondo_id: MONDO:0012004
  category: Cancer
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
  - claude-opus-4-6[1m]
  web_search_requests: 13
  num_turns: 21
  total_cost_usd: 1.8738827499999997
  session_id: 04a6915c-5815-4b9c-a14b-123d343a169b
  stop_reason: end_turn
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
citation_count: 16
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 0
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:42577903
  relevance_assessed: 17
  on_topic: 14
  off_topic: 1
  off_topic_references:
  - PMID:38198197
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 54
  verified: 50
  not_found: 1
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.019
  labels_checked: 52
  labels_matching: 35
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: MONDO:0012004
    reported_labels:
    - MONDO
    - parathyroid gland carcinoma
    ontology_label: parathyroid gland carcinoma
  - term_id: HP:0100255
    reported_labels:
    - Osteitis fibrosa cystica
    ontology_label: Metaphyseal dysplasia
  - term_id: UBERON:0002048
    reported_labels:
    - "Lung \u2014 most common distant metastatic site"
    - lung
    ontology_label: lung
  - term_id: UBERON:0004765
    reported_labels:
    - "Bone/skeleton \u2014 metastatic deposits and PTH-mediated skeletal disease"
    ontology_label: skeletal element
  - term_id: UBERON:0002107
    reported_labels:
    - "Liver \u2014 distant metastasis"
    - liver
    ontology_label: liver
  - term_id: UBERON:0002113
    reported_labels:
    - "Kidney \u2014 nephrolithiasis, nephrocalcinosis"
    - kidney
    ontology_label: kidney
  - term_id: NCIT:C65509
    reported_labels:
    - Calcimimetic; enhances CaSR sensitivity
    - Cinacalcet Hydrochloride
    ontology_label: Eletriptan
  - term_id: NCIT:C65214
    reported_labels:
    - Anti-RANKL monoclonal antibody
    - Denosumab
    ontology_label: Acotiamide
  - term_id: CHEBI:77862
    reported_labels:
    - zoledronic acid
    ontology_label: gossypetin(1-)
  - term_id: CHEBI:3306
    reported_labels:
    - Osteoclast inhibitor (transient)
    ontology_label: calcitonin
  labels_variant: 7
  unresolved_terms:
  - UBERON:0016415
  obsolete_terms:
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  - term_id: GO:0098532
    ontology_label: obsolete histone H3-K27 trimethylation
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Parathyroid Gland Carcinoma
- **MONDO ID:** MONDO:0012004 (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Parathyroid Gland Carcinoma** covering all of the
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

Let me gather comprehensive research on Parathyroid Gland Carcinoma. I'll run multiple searches in parallel.

Now let me fetch some key full-text sources for additional detail.

Now I have comprehensive data. Let me compile the full research report.

---

# Comprehensive Research Report: Parathyroid Gland Carcinoma

---

## 1. Disease Information

### Overview

Parathyroid gland carcinoma (PC) is an exceptionally rare malignant neoplasm arising from the parathyroid glands, representing less than 0.005% of all malignancies worldwide and approximately 1% of primary hyperparathyroidism (PHPT) cases (PMID: 42694707). It is the rarest endocrine malignancy. Unlike benign parathyroid adenomas, PC is characterized by aggressive clinical behavior driven primarily by autonomous parathyroid hormone (PTH) overproduction leading to severe, often life-threatening hypercalcemia, as well as local invasion and potential for distant metastasis.

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| MONDO | MONDO:0012004 |
| OMIM | 608266 (CDC73-related) |
| Orphanet | ORPHA:143 |
| ICD-10 | C75.0 (Malignant neoplasm of parathyroid gland) |
| ICD-11 | 2F36 (Malignant neoplasms of parathyroid glands) |
| MeSH | D010282 (Parathyroid Neoplasms) |
| SEER | Parathyroid Gland Cancer |

### Synonyms

- Parathyroid carcinoma
- Parathyroid gland cancer
- Parathyroid adenocarcinoma
- Malignant neoplasm of parathyroid gland
- PRTC

---

## 2. Etiology

### Disease Causal Factors

Parathyroid carcinoma arises from a combination of genetic and, less commonly, environmental factors. The primary molecular driver is biallelic inactivation of the **CDC73** tumor suppressor gene (encoding parafibromin), occurring in approximately 70% of sporadic PC cases (PMID: 42196524). The disease follows a classic two-hit tumor suppressor model with loss of heterozygosity at 1q31.2 in 50–55% of sporadic cases.

### Genetic Risk Factors

**Germline predisposition syndromes:**

- **Hyperparathyroidism-Jaw Tumor Syndrome (HPT-JT)**: Autosomal dominant disorder caused by germline CDC73 mutations; 15–18% of HPT-JT patients develop parathyroid carcinoma (PMID: 42694707). CDC73 germline mutations are found in 50–75% of HPT-JT families.
- **Familial Isolated Primary Hyperparathyroidism (FIHP)**: ~8% harbor CDC73 germline variants; rare cases progress to PC.
- **MEN1 (Multiple Endocrine Neoplasia Type 1)**: Fewer than 15 PC cases reported in MEN1; 60% showed local invasion/metastasis.
- **MEN2A**: Only 3 metastatic PC cases reported in association with RET mutations.

**Sporadic disease**: 20–40% of apparently sporadic PC patients carry constitutional (germline) pathogenic CDC73 variants, indicating a hereditary component even in non-syndromic presentations (PMID: 42694707).

### Environmental Risk Factors

- **Prior neck irradiation**: Radiation-associated hyperparathyroidism has an average latent period of ~38 years. In radiation-exposed patients with PHPT, parathyroid carcinoma accounts for 4.3% of cases (PMID: 539600).
- **End-stage renal disease (ESRD)**: Chronic secondary/tertiary hyperparathyroidism from ESRD may rarely be complicated by PC, though causality is debated.
- **No established lifestyle risk factors** (diet, smoking, alcohol) specific to parathyroid carcinoma.

### Protective Factors

No established genetic or environmental protective factors specific to parathyroid carcinoma have been identified.

### Gene-Environment Interactions

The interaction between prior radiation exposure and CDC73 germline heterozygosity has not been formally studied, but both independently increase risk of parathyroid neoplasia.

---

## 3. Phenotypes

### Clinical Presentation

Parathyroid carcinoma typically presents between the 4th and 6th decades of life (mean age 45–62 years), which is younger than benign PHPT. The clinical phenotype is dominated by severe hypercalcemia and its systemic consequences.

| Phenotype | Description | Frequency | HPO Term |
|-----------|-------------|-----------|----------|
| **Hypercalcemia** | Serum calcium ≥14 mg/dL in 62% of carcinomas vs. 17% of atypical adenomas; PTH levels 3–10× upper limit of normal | Very frequent (>80%) | HP:0003072 (Hypercalcemia) |
| **Nephrolithiasis** | Kidney stone formation from chronic hypercalcemia and hypercalciuria | 30–60% | HP:0000787 (Nephrolithiasis) |
| **Nephrocalcinosis** | Calcium deposition in renal parenchyma | Variable | HP:0000121 (Nephrocalcinosis) |
| **Osteoporosis** | Reduced bone mineral density from excess PTH-mediated bone resorption | 40–60% | HP:0000939 (Osteoporosis) |
| **Osteitis fibrosa cystica** | Subperiosteal resorption, brown tumors, bone cysts from severe hyperparathyroidism | 10–30% | HP:0100255 (Osteitis fibrosa cystica) |
| **Pathological fractures** | Fractures from PTH-mediated skeletal demineralization | Variable | HP:0002756 (Pathologic fracture) |
| **Bone pain** | Musculoskeletal pain from osseous involvement | 30–50% | HP:0002653 (Bone pain) |
| **Palpable neck mass** | Neck mass distinguishing carcinoma from adenoma | 30–76% | HP:0100028 (Abnormality of the parathyroid gland) |
| **Muscle weakness** | Proximal myopathy from hypercalcemia | 20–40% | HP:0003325 (Limb-girdle muscle weakness) |
| **Fatigue** | Chronic fatigue from metabolic derangement | Common | HP:0012378 (Fatigue) |
| **Nausea/vomiting** | GI symptoms from hypercalcemia | 20–40% | HP:0002013 (Vomiting) |
| **Constipation** | GI dysmotility from hypercalcemia | Common | HP:0002019 (Constipation) |
| **Polyuria/polydipsia** | Nephrogenic diabetes insipidus from hypercalcemia | 20–40% | HP:0000103 (Polyuria) |
| **Neurocognitive symptoms** | Depression, confusion, psychosis, impaired concentration | Common | HP:0100543 (Cognitive impairment) |
| **Cardiac arrhythmias** | Shortened QT interval, arrhythmias from hypercalcemia | Variable | HP:0011675 (Arrhythmia) |
| **Hoarseness/dysphonia** | Recurrent laryngeal nerve invasion by tumor | 15–30% | HP:0001609 (Hoarseness) |
| **Elevated PTH** | Markedly elevated intact parathyroid hormone | Very frequent (>90%) | HP:0003165 (Elevated circulating parathyroid hormone level) |
| **Pancreatitis** | Acute pancreatitis triggered by severe hypercalcemia | Occasional | HP:0001733 (Pancreatitis) |
| **Peptic ulcer disease** | Increased gastric acid secretion from hypercalcemia | Occasional | HP:0004398 (Peptic ulcer) |

### Quality of Life Impact

The severe hypercalcemia significantly impairs quality of life, causing debilitating fatigue, neurocognitive impairment, depression, bone pain, GI disturbance, and recurrent renal stones. Refractory hypercalcemia is the leading cause of death, not tumor burden per se (PMID: 42577903).

---

## 4. Genetic/Molecular Information

### Causal Genes

#### CDC73 (Cell Division Cycle 73) — Primary Driver
- **HGNC**: hgnc:16783
- **Location**: Chromosome 1q31.2
- **Protein**: Parafibromin (531 amino acids)
- **Mutation frequency**: Somatic mutations in ~70% (40–100% range) of sporadic PC; germline in 20–40% of apparently sporadic cases (PMID: 42694707)
- **Variant types**: >75% are frameshift or nonsense mutations, concentrated in exons 1–7 (especially exons 1, 2, and 7)
- **Functional consequence**: Loss of function — biallelic inactivation via mutation + LOH
- **Somatic origin predominant**, with germline carrier state in syndromic/familial cases
- **Toxic gain of function**: Mutant parafibromin actively binds and destabilizes p53 mRNA, facilitating apoptosis evasion (PMID: 42196524)

> *"Biallelic somatic inactivation of the CDC73 gene has been reported in 40–60% of sporadic PCs"* (PMID: 42694707)

#### CCND1 (Cyclin D1)
- **HGNC**: hgnc:1582
- **Location**: Chromosome 11q13.3
- **Alteration**: Overexpression in 60–90% of PC; gene amplification in 29% (PMID: 42694707)
- **Function**: Drives G1/S cell cycle progression via CDK4/6; promotes chromosomal instability

#### MEN1
- **HGNC**: hgnc:7010
- **Location**: Chromosome 11q13
- **Protein**: Menin (610 amino acids)
- **Frequency**: Somatic alterations in 13–37% of sporadic PC; LOH at 11q13 in 40–50%

#### PRUNE2
- **HGNC**: hgnc:25209
- **Location**: Chromosome 9q21.2
- **Frequency**: Mutations in 18–20% of sporadic PC; rarely mutated in adenomas
- **Function**: Regulates cell differentiation and survival by suppression of RhoA activity

> *"Variants in PRUNE2 were associated with parathyroid carcinoma in 18% of cases studied"* (PMID: 42694707)

#### PI3K/AKT/mTOR Pathway Genes
- **PIK3CA**, **MTOR**, **PTEN**, **TSC1**, **TSC2**, **PIK3CB**: Collectively altered in 21–30% of PC via activating mutations; actionable variants in ~25% of samples
- Associated with substantially higher serum PTH and significantly shorter disease-free and overall survival (PMID: 42196524)

#### FLCN (Folliculin)
- **HGNC**: hgnc:27310
- Recurrent "hot spot" frameshift mutations; loss of tumor-suppressive function triggers pathological mTORC1 activation

#### Other Genes
- **POT1**: Mutations reported in PC cohorts (shelterin complex, telomere maintenance)
- **EZH2**: Amplification in ~60% of sporadic PC (vs. 20% in adenomas); catalyzes repressive H3K27me3
- **APC**: Promoter hypermethylation in >75% of PCs; loss of expression in 75% of PCs vs. 0% in adenomas

### Epigenetic Information

Epigenetic alterations are a hallmark of PC and serve both as pathogenic drivers and diagnostic biomarkers:

- **DNA methylation**: TET2 promoter hypermethylation abolishes TET2 expression; dense hypermethylation of CDKN2A, CDKN2B, and WT1 CpG islands silences critical tumor suppressors (PMID: 42196524)
- **5-hydroxymethylcytosine (5-hmC) depletion**: Near-complete global depletion of 5-hmC is an exclusive hallmark of malignant transformation; reported 100% sensitivity and 100% specificity for distinguishing PC from adenoma (requires multi-center validation) (PMID: 42196524)
- **Histone modifications**: EZH2 amplification (~60% of PCs) catalyzes repressive H3K27me3, silencing Wnt antagonists AXIN2 and HIC1; parafibromin itself interacts with SUV39H1 to induce H3K9 methylation
- **APC promoter 1A hypermethylation**: Occurs in ~75% of PCs, disrupting the β-catenin destruction complex

### Non-Coding RNA Dysregulation

- **Downregulated miRNAs**: miR-296, miR-139, miR-126*, miR-26b, miR-30b
- **Upregulated miRNAs**: miR-222, miR-503
- **Diagnostic utility**: Combined diagnostic index of miR-139 and miR-30b achieves AUC = 0.888
- **Liquid biopsy marker**: Circulating miR-342-3p diminished in PC serum
- **Long non-coding RNAs**: PVT1 upregulated, GLIS2-AS1 downregulated; serum BC200 elevated (93% sensitivity, 75% specificity), drops post-parathyroidectomy (PMID: 42196524)

---

## 5. Environmental Information

### Environmental Factors

- **Prior neck irradiation**: Established risk factor; latent period averages ~38 years. In radiation-exposed patients with PHPT, parathyroid carcinoma accounts for 4.3% of cases (PMID: 539600)
- **Chronic kidney disease/ESRD**: Prolonged secondary hyperparathyroidism may rarely predispose to malignant transformation, though direct causation remains uncertain

### Lifestyle Factors

No specific dietary, smoking, exercise, or alcohol-related risk factors have been established for PC.

### Infectious Agents

No infectious etiology is known for parathyroid carcinoma.

---

## 6. Mechanism / Pathophysiology

### Causal Chain

1. **Initiating lesion**: Biallelic inactivation of CDC73 (mutation + LOH) in a parathyroid chief cell → loss of nuclear parafibromin → (LEADS TO)
2. **Transcriptional dysregulation**: Loss of PAF1 complex scaffold function → impaired transcription elongation, mRNA processing, and epigenetic control → (LEADS TO)
3. **Apoptosis evasion**: Mutant parafibromin actively destabilizes p53 mRNA (toxic gain of function) → failure of p53-mediated cell death → (LEADS TO)
4. **Wnt/β-catenin pathway activation**: Loss of parafibromin's negative regulation of Wnt signaling + APC promoter hypermethylation (~75% of PCs) + EZH2 amplification repressing Wnt antagonists → accumulation of nuclear β-catenin → transcription of oncogenic targets (c-Myc, Cyclin D1) → (LEADS TO)
5. **Cell cycle dysregulation**: CCND1 overexpression/amplification (60–90% of PCs) → Cyclin D1–CDK4/6 hyperphosphorylation of RB1 → uncontrolled G1/S progression → (LEADS TO)
6. **Parallel pathway activation** (in ~20–30% of cases): Activating mutations in PIK3CA/MTOR/PTEN or FLCN inactivation → constitutive PI3K/AKT/mTOR signaling → enhanced cell growth, survival, and metabolic reprogramming → (LEADS TO)
7. **Epigenetic reprogramming**: TET2 silencing + global 5-hmC depletion + CDKN2A/2B methylation → loss of tumor suppressor expression and differentiation programs → (LEADS TO)
8. **Clonal expansion and autonomous PTH secretion**: Uncontrolled proliferation of parathyroid chief cells → formation of malignant parathyroid neoplasm → constitutive, unregulated PTH secretion → (LEADS TO)
9. **Severe hypercalcemia**: Excessive PTH drives: (a) osteoclast-mediated bone resorption → osteitis fibrosa cystica, osteoporosis, pathological fractures; (b) increased renal calcium reabsorption and 1,25(OH)₂D synthesis → hypercalciuria, nephrolithiasis, nephrocalcinosis; (c) GI, cardiovascular, and neurocognitive toxicity → (LEADS TO)
10. **Invasion and metastasis**: Capsular/vascular/perineural invasion → local recurrence (50–80%); distant metastasis to lungs, bone, liver (10–30%)

### Molecular Pathways

- **Wnt/β-catenin signaling**: Constitutively activated via parafibromin loss, APC silencing, and EZH2-mediated repression of AXIN2
  - GO: GO:0060070 (canonical Wnt signaling pathway)
- **PI3K/AKT/mTOR cascade**: Constitutively activated via PIK3CA/MTOR gain-of-function or PTEN/TSC1/TSC2 loss-of-function; ~48.5% of PCs classified as "high mTORC1"
  - GO: GO:0051896 (regulation of protein kinase B signaling)
- **Cyclin D1–CDK4/6–RB1 axis**: Cell cycle checkpoint bypass
  - GO: GO:0000082 (G1/S transition of mitotic cell cycle)
- **p53 pathway**: Disabled via mutant parafibromin-mediated p53 mRNA destabilization
  - GO: GO:0006915 (apoptotic process)

### Cellular Processes

- Evasion of apoptosis (mutant parafibromin destabilizes p53 mRNA)
- Cell cycle dysregulation (Cyclin D1–CDK4/6 hyperactivation)
- Epigenetic reprogramming (global 5-hmC depletion, TET2 silencing)
- Immune evasion — PCs are predominantly "immune-ignorant/immune-tolerant" with sparse lymphocyte infiltration, PD-L1 negativity, heavy CD163+ M2 macrophage infiltration, and severe CD8+ T cell depletion (PMID: 42196524)

### Cell Types Involved

| Cell Type | Role | CL Term |
|-----------|------|---------|
| Parathyroid chief cell | Cell of origin; PTH-producing | CL:0000446 (chief cell of parathyroid gland) |
| Osteoclast | Effector of PTH-driven bone resorption | CL:0000092 (osteoclast) |
| Osteoblast | Secondarily stimulated by PTH | CL:0000062 (osteoblast) |
| CD163+ tumor-associated macrophage | Immunosuppressive M2 macrophages in tumor microenvironment | CL:0000235 (macrophage) |
| CD8+ T cell | Depleted in tumor microenvironment | CL:0000625 (CD8-positive, alpha-beta T cell) |

### Biological Processes

| Process | GO Term |
|---------|---------|
| Parathyroid hormone secretion | GO:0035898 (parathyroid hormone secretion) |
| Canonical Wnt signaling pathway | GO:0060070 |
| Regulation of protein kinase B signaling | GO:0051896 |
| G1/S transition of mitotic cell cycle | GO:0000082 |
| Apoptotic process | GO:0006915 |
| Bone resorption | GO:0045453 |
| DNA methylation | GO:0006306 |
| Histone H3-K27 trimethylation | GO:0098532 |
| Response to calcium ion | GO:0051592 |

### Molecular Profiling

**Genomic studies**: A 2023 comprehensive genomic and transcriptomic profiling study (Nature Experimental & Molecular Medicine) sequenced 50 parathyroid tissues (12 carcinomas, 28 adenomas, 10 normals) and confirmed multiple two-hit mutation patterns in CDC73 converging to biallelic inactivation. WT1 was identified as a potential biomarker for CDC73-mutant PC (PMID: 36949199, Exp Mol Med 2023).

**PI3K/AKT/mTOR activation**: 48.5% of PC tumors classified as "high mTORC1"; PI3K/AKT/mTOR-mutated group showed significantly lower disease-free survival and overall survival (J Clin Endocrinol Metab, 2025).

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary**: Parathyroid glands (UBERON:0001132)
- **Secondary involvement**:
  - Thyroid gland — direct local invasion (UBERON:0002046)
  - Cervical lymph nodes — regional metastasis (UBERON:0016415)
  - Lung — most common distant metastatic site (UBERON:0002048)
  - Bone/skeleton — metastatic deposits and PTH-mediated skeletal disease (UBERON:0004765)
  - Liver — distant metastasis (UBERON:0002107)
  - Kidney — nephrolithiasis, nephrocalcinosis (UBERON:0002113)

### Tissue and Cell Level

- Parathyroid parenchyma (chief cells)
- Bone tissue — both cortical and trabecular (PTH-driven resorption)
- Renal tubular epithelium (calcium handling)
- Vascular endothelium and nerve sheaths (sites of invasion)

### Body Systems Involved

- Endocrine system
- Musculoskeletal system (bone resorption, fractures)
- Urinary/renal system (nephrolithiasis, renal insufficiency)
- Gastrointestinal system (nausea, constipation, pancreatitis, peptic ulcer)
- Cardiovascular system (arrhythmias, shortened QT)
- Nervous system (neurocognitive symptoms, recurrent laryngeal nerve invasion)

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: 4th–6th decade (mean 45–62 years); younger than benign PHPT
- **Onset pattern**: Insidious; typically presents with progressive symptoms of severe hyperparathyroidism

### Progression

- **Disease stages**: No universally adopted formal staging system; Shaha classification and AJCC/UICC standalone TNM categories are used in research settings
- **Disease course**: Progressive if untreated; recurrence rate 30–80% even after initial surgery, with median disease-free survival of ~80 months (PMID: 42485575)
- **Recurrence timing**: Most within 2–5 years, though late recurrences beyond 10 years are documented
- **Disease-free interval >36 months**: Associated with significantly better overall survival (p=0.02) (PMID: 42485575)

> *"Despite optimal surgical intervention, recurrence develops in 60% to 80% of patients"* (PMID: 42577903)

### Patterns

- No spontaneous remission
- Repeated recurrences common; each recurrence becomes progressively harder to treat surgically
- Death usually from uncontrolled hypercalcemia rather than tumor bulk

---

## 9. Inheritance and Population

### Epidemiology

**Incidence (annual)**:
- Worldwide: 3.5–5.7 per 10,000,000 persons (PMID: 42694707)
- US (SEER 1988–2003): Increased 60% from 3.58 to 5.73 per 10,000,000
- US (SEER 1973–2014): Rose from 2 to 13 per 10,000,000 by 2002, then stabilized
- Europe: 2–3 per 10,000,000 persons/year
- Finland (1955–2013): Increased from 1.42 to 10.4 per 10,000,000 persons/year
- Korea (2002–2017): 3.8 to 6.6 per 10,000,000 persons/year

**Prevalence**: Less than 0.005% of all cancers worldwide; accounts for <1% of PHPT cases

### Inheritance

- **Most cases sporadic** (~60–80%)
- **Autosomal dominant** inheritance in HPT-JT syndrome (CDC73 germline mutations)
- **Penetrance**: Incomplete; approximately 15% of HPT-JT patients develop PC
- **Sporadic cases**: 20–40% of apparently sporadic PC carry germline CDC73 variants

### Population Demographics

- **Sex ratio**: Approximately equal (unlike benign PHPT, which has a 3:1 female predominance). Some series report slight female predominance (53–61%), others equal distribution
- **Ethnicity**: Higher incidence in individuals of European descent (~75% of reported cases)
- **Age distribution**: Peak in 5th decade (range 17–80+)
- **Geographic variation**: Higher reported incidence in Japan and Italy, possibly due to diagnostic awareness; incidence increasing globally, likely reflecting improved detection

---

## 10. Diagnostics

### Clinical Tests

**Laboratory**:
- Serum calcium: Markedly elevated (≥14 mg/dL in 62% of PC vs. 17% atypical adenomas)
- Intact PTH: 3–10× upper limit of normal (typically >500 pg/mL)
- Alkaline phosphatase: Often elevated
- 24-hour urine calcium: Elevated
- Serum phosphate: Low
- 1,25-dihydroxyvitamin D: Elevated

**Imaging**:
- **Ultrasound**: PC tumors are larger (mean 3.5 cm vs. 1.9 cm for adenoma), irregular, lobulated, heterogeneous, with depth-to-width ratio ≥1
- **4D-CT**: Local invasion, cystic changes, slower contrast washout pattern compared to adenoma
- **99mTc-sestamibi scintigraphy**: Functional parathyroid imaging
- **18F-FDG PET/CT**: Emerging utility for metastatic disease surveillance
- **MRI**: Useful for evaluating local invasion

> *"No single imaging study can distinguish parathyroid carcinomas from adenomas"* (PMID: 42577903)

**Contraindication**: Fine-needle aspiration is "typically avoided...due to the risk of tumor seeding" (PMID: 42577903)

### Histopathology

Definitive diagnosis requires demonstration of:
- Capsular invasion
- Vascular invasion (angioinvasion)
- Perineural invasion
- Direct invasion into adjacent structures
- OR documented metastasis

Additional features: Trabecular growth pattern, broad fibrous bands, mitotic index >5/50 HPF, atypical nuclei, necrosis, thick fibrous capsule

### Immunohistochemistry Panel

| Marker | Sensitivity | Specificity | Notes |
|--------|-------------|-------------|-------|
| Parafibromin (loss) | 68% (pooled) | 95% (pooled) | Loss in 31–73% of PCs vs. 0–1% of adenomas; HR 3.26 for recurrence |
| Ki-67 (elevated >5%) | 45–60% | 93–96% | Elevated in 86% of PCs vs. 0% of adenomas in some series |
| PGP9.5 (strong staining) | 78% | 100% | Strong staining for PC/HRPT2 mutation |
| Galectin-3 | 45.4% | 90.2% | Overexpressed in malignancy |
| 5-hmC (loss) | 100% | 100% | Requires multi-center validation |
| E-cadherin (membranous loss) | 47.7% in PCs | — | vs. 18.6% in benign |
| EZH2 (nuclear positivity) | 31.8% in PCs | — | 0% in benign |

**Best panel performance**: Silva-Figueroa nomogram (parafibromin + RB + PGP9.5 + Ki-67 + Galectin-3): AUC = 0.849 (PMID: 42196524)

### Liquid Biopsy Markers

- Circulating **BC200 lncRNA**: 93% sensitivity, 75% specificity; drops post-resection
- Circulating **miR-342-3p**: Diminished in PC serum
- **Combined miR-139 + miR-30b**: AUC = 0.888 (PMID: 42196524)

### Genetic Testing

Germline CDC73 mutation testing recommended for all patients with PC, given 20–40% carry constitutional variants even in apparently sporadic cases. Comprehensive genomic profiling can identify actionable PI3K/AKT/mTOR pathway variants (~25% of cases).

### Differential Diagnosis

- Parathyroid adenoma (benign)
- Atypical parathyroid adenoma/neoplasm
- Parathyromatosis
- Thyroid carcinoma with parathyroid invasion
- Metastatic disease to parathyroid

---

## 11. Outcome/Prognosis

### Survival and Mortality

| Metric | Value | Source |
|--------|-------|-------|
| 5-year overall survival | 78–86% | PMID: 42694707 |
| 10-year overall survival | 49–77% | PMID: 42694707 |
| Median overall survival | 14.3 years | PMID: 42577903 |
| Metastatic disease 5-year survival | <50% | PMID: 42196524 |
| Metastatic disease median survival | 36 months | PMID: 42577903 |
| Disease-free interval | Median 80 months | PMID: 42485575 |
| Recurrence rate | 30–80% | PMID: 42577903 |

### Prognostic Factors

**Independent risk factors for mortality** (PMID: 42577903; PMID: 42485575):
- Tumor size >4 cm
- Age >40 years
- Male sex
- Distant metastatic spread
- Poorly differentiated histological grade
- Advanced tumor stage (T3 by Shaha or T2+ by AJCC/UICC)
- Positive surgical margins
- Loss of parafibromin expression (HR 3.26 for recurrence)
- Elevated Ki-67
- PI3K/AKT/mTOR pathway mutations (shorter DFS and OS)

**Favorable prognostic indicators**:
- Negative surgical margins: 100% recurrence-free survival at 5 and 10 years (PMID: 42577903)
- Disease-free interval >36 months (p=0.02)
- Treatment at high-volume endocrine centers

### Cause of Death

Mortality most often results from complications of uncontrolled hypercalcemia (renal failure, cardiac arrhythmia, skeletal catastrophe) rather than tumor burden itself (PMID: 42577903).

---

## 12. Treatment

### Surgery — Gold Standard

**En bloc resection** is the mainstay and only curative treatment:

> *"Excision of the affected parathyroid gland, an ipsilateral thyroid lobectomy, and removal of adjacent tissues if invasion is present"* (PMID: 42577903)

- En bloc resection achieves margin-free excision in ~82% vs. 17% with simple local excision
- Negative margins → 100% recurrence-free survival at 5 and 10 years
- Positive margins → ~50% local recurrence rate
- Prophylactic lymph node dissection is NOT recommended (lymph node metastases in only 6.5% overall)
- **Capsular rupture must be avoided** — can lead to parathyromatosis (tumor seeding)
- NCIT: NCIT:C15329 (Surgical Procedure)

### Medical Management of Hypercalcemia

| Agent | Mechanism | NCIT/CHEBI | Notes |
|-------|-----------|------------|-------|
| **Cinacalcet** | Calcimimetic; enhances CaSR sensitivity | NCIT:C65509 | Foundation of chronic management; does not reduce tumor size |
| **Denosumab** | Anti-RANKL monoclonal antibody | NCIT:C65214 | Effective in renal impairment; inhibits osteoclast maturation |
| **Bisphosphonates** (zoledronic acid, pamidronate) | Osteoclast inhibitors | CHEBI:77862 (zoledronic acid) | Temporary effect; palliative |
| **IV normal saline** | Volume expansion + calciuresis | — | Acute management |
| **Calcitonin** | Osteoclast inhibitor (transient) | CHEBI:3306 | Short-term bridge therapy |

### Adjuvant Radiation Therapy

While historically considered radioresistant, emerging data (SEER propensity-matched) support selective use:
- 10-year disease-specific survival: 90.3% with adjuvant RT vs. 72.2% without (p=0.02) (PMID: 42577903)
- Indicated for: positive margins, unresectable localized disease, multiple recurrences
- NCIT: NCIT:C15313 (Radiation Therapy)

### Chemotherapy

Conventional cytotoxic chemotherapy shows "minimal and inconsistent success" (PMID: 42577903). Not standard of care.
- **Temozolomide**: Achieved significant long-term clinical remission in advanced cases with high MGMT promoter methylation (PMID: 42196524)
- NCIT: NCIT:C15632 (Chemotherapy)

### Targeted Therapies (Emerging)

| Agent | Target | Evidence |
|-------|--------|----------|
| **Lenvatinib** | VEGFR/PDGFR/FGFR/RET TKI | Biochemical response, 9 months stabilization in metastatic PC (PMID: case report 2025) |
| **Surufatinib** | VEGFR/FGFR/CSF1R TKI | Disease stabilization in case reports |
| **Sorafenib** | Multi-kinase inhibitor | Controlled refractory hypercalcemia in metastatic cases |
| **Palbociclib** | CDK4/6 inhibitor | Strong tumor suppression in preclinical PC models targeting CCND1-CDK4/6-RB1 axis |
| **Pembrolizumab** | Anti-PD-1 checkpoint inhibitor | Potential in MSI-high/TMB-high PC; normalized calcium/PTH in one case with EBRT |
| **Everolimus/mTOR inhibitors** | mTORC1 | Rationale from ~48.5% of PCs classified as "high mTORC1" |

### Treatment Algorithm

1. **Initial**: En bloc resection with ipsilateral thyroid lobectomy
2. **Recurrence**: Repeat surgical resection when feasible (EEBR; 5-year OS ~59.6%)
3. **Unresectable/metastatic**: Cinacalcet ± denosumab for hypercalcemia control; consider lenvatinib, temozolomide, or pembrolizumab based on molecular profiling
4. **Palliative**: Aggressive IV hydration, bisphosphonates, calcitonin, dialysis for refractory hypercalcemia

### Clinical Trials

Limited clinical trial activity given disease rarity. No large randomized trials exist. Case reports and small series drive evidence for targeted therapies.

---

## 13. Prevention

### Primary Prevention

No established primary prevention strategies exist for parathyroid carcinoma.

### Secondary Prevention / Screening

- **Genetic screening**: Germline CDC73 mutation testing recommended for:
  - All patients with parathyroid carcinoma (20–40% carry germline variants)
  - Individuals with HPT-JT syndrome, FIHP, or family history of parathyroid malignancy
  - Patients with severe PHPT and elevated PTH at young age
- **Cascade screening**: First-degree relatives of CDC73 mutation carriers should be tested
- **Surveillance in mutation carriers**: Regular serum calcium and PTH monitoring

### Tertiary Prevention

- **Lifelong biochemical surveillance** post-surgery: Serial serum calcium and PTH (biochemical recurrence precedes radiographic detection)
- **Imaging surveillance**: Periodic neck ultrasound, 18F-FDG PET/CT for high-risk patients
- **Genetic counseling**: For patients and families with CDC73 mutations

> *"Patients require lifelong biochemical surveillance following surgery"* (PMID: 42577903)

---

## 14. Other Species / Natural Disease

### Comparative Biology

Parathyroid carcinoma is exceedingly rare in veterinary species with limited literature. Sporadic reports exist in:
- **Dogs** (NCBITaxon:9615): Primary hyperparathyroidism including rare carcinomas reported, predominantly in Keeshonds (familial predisposition)
- **Cats** (NCBITaxon:9685): Rare case reports of functional parathyroid carcinoma
- **Horses** (NCBITaxon:9796): Extremely rare case reports

No established orthologous CDC73 mutations have been characterized in naturally occurring veterinary PC.

---

## 15. Model Organisms

### Mouse Models

**Cdc73 knockout models** are the primary experimental system:

1. **Cdc73+/− heterozygous mice**: Develop parathyroid tumors with nuclear pleomorphism, fibrous septation, and increased galectin-3 expression consistent with atypical parathyroid adenomas from 9 months of age (PMID: 28288139)

2. **Cdc73L/L/PTH-Cre (parathyroid-specific conditional knockout)**: Phenotype is strain-dependent (PMID: 38198197, J Endocr Soc 2024):
   - On mixed B6/129/CD1 background: Homozygous knockouts showed decreased serum calcium and PTH with smaller parathyroid glands
   - On other backgrounds: No detectable abnormalities
   - *Limitation*: Strain-dependent phenotype complicates interpretation; does not fully recapitulate human PC

3. **Cdc73−/−/Pth-Cre uterine model**: Mice develop uterine tumors in addition to parathyroid lesions, modeling HPT-JT syndrome features

### Cell Line Models

- Primary human parathyroid cells quickly lose PTH secretion in culture
- Continuous human PC cell lines exist for molecular studies and drug testing, but cannot accurately recapitulate complex stromal and immune cell interactions (PMID: 42196524)
- *Preclinical models remain a persistent bottleneck* for therapeutic development

### Model Limitations

- No mouse model fully recapitulates the human metastatic PC phenotype
- Strain-dependent Cdc73 knockout phenotypes complicate translational studies
- Lack of immune-competent models limits immunotherapy research
- Cell lines lose PTH secretion and tissue architecture

---

## Summary of Key Ontology Terms

### Disease
- MONDO:0012004 — parathyroid gland carcinoma

### Phenotypes (HPO)
- HP:0003072 — Hypercalcemia
- HP:0003165 — Elevated circulating parathyroid hormone level
- HP:0000787 — Nephrolithiasis
- HP:0000121 — Nephrocalcinosis
- HP:0000939 — Osteoporosis
- HP:0100255 — Osteitis fibrosa cystica
- HP:0002756 — Pathologic fracture
- HP:0002653 — Bone pain
- HP:0100028 — Abnormality of the parathyroid gland
- HP:0001609 — Hoarseness
- HP:0012378 — Fatigue
- HP:0001324 — Muscle weakness
- HP:0011675 — Arrhythmia
- HP:0000103 — Polyuria
- HP:0002019 — Constipation
- HP:0002013 — Vomiting

### Genes (HGNC)
- hgnc:16783 — CDC73
- hgnc:1582 — CCND1
- hgnc:7010 — MEN1
- hgnc:25209 — PRUNE2
- hgnc:27310 — FLCN
- hgnc:8975 — PIK3CA
- hgnc:3942 — EZH2
- hgnc:583 — APC
- hgnc:9588 — PTEN

### Biological Processes (GO)
- GO:0035898 — parathyroid hormone secretion
- GO:0060070 — canonical Wnt signaling pathway
- GO:0051896 — regulation of protein kinase B signaling
- GO:0000082 — G1/S transition of mitotic cell cycle
- GO:0006915 — apoptotic process
- GO:0045453 — bone resorption

### Cell Types (CL)
- CL:0000446 — chief cell of parathyroid gland
- CL:0000092 — osteoclast

### Anatomy (UBERON)
- UBERON:0001132 — parathyroid gland
- UBERON:0002046 — thyroid gland
- UBERON:0002048 — lung
- UBERON:0002107 — liver
- UBERON:0002113 — kidney

### Treatments (NCIT)
- NCIT:C15329 — Surgical Procedure
- NCIT:C15986 — Pharmacotherapy
- NCIT:C15313 — Radiation Therapy
- NCIT:C65509 — Cinacalcet Hydrochloride
- NCIT:C65214 — Denosumab

---

## Key References

| PMID | Citation | Year |
|------|----------|------|
| 42196524 | Parathyroid Carcinoma: From Molecular Pathogenesis and Diagnostic Biomarkers to Targeted Therapeutics. *Int J Mol Sci* | 2025 |
| 42694707 | Parathyroid carcinoma: epidemiology and genetics. *Endocr Oncol* | 2026 |
| 42577903 | Critical Insights into Parathyroid Cancer. *J Cancer Sci Clin Ther* | 2026 |
| 42485575 | Prognostic factors and survival in parathyroid carcinoma: a 50-year single-center cohort study. *Arch Endocrinol Metab* | 2026 |
| 36949199 | Genomic and transcriptomic profiling reveal molecular characteristics of parathyroid carcinoma. *Exp Mol Med* | 2023 |
| 28288139 | Mice deleted for cell division cycle 73 gene develop parathyroid and uterine tumours. *Oncogene* | 2017 |
| 38198197 | Phenotype of Parathyroid-targeted Cdc73 Deletion in Mice Is Strain-Dependent. *J Endocr Soc* | 2024 |
| 39677927 | CDC73 c.1155-3A>G is a pathogenic variant causing aberrant splicing. *JBMR Plus* | 2024 |

---

Sources:
- [Parathyroid Carcinoma: From Molecular Pathogenesis to Targeted Therapeutics (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13208034/)
- [Parathyroid carcinoma: epidemiology and genetics (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13539412/)
- [Prognostic factors and survival: 50-year cohort study (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13390904/)
- [Critical Insights into Parathyroid Cancer (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13455704/)
- [Parathyroid carcinoma: New insights (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1521690X24001428)
- [Genomic and transcriptomic profiling of PC (Nature)](https://www.nature.com/articles/s12276-023-00968-4)
- [Phenotype of Parathyroid-targeted Cdc73 Deletion in Mice (JES)](https://academic.oup.com/jes/article/8/3/bvae006/7581885)
- [CDC73 c.1155-3A>G pathogenic variant (JBMR Plus)](https://academic.oup.com/jbmrplus/article/9/1/ziae149/7904795)
- [PI3K/AKT/mTOR in Parathyroid Carcinomas (JCEM)](https://academic.oup.com/jcem/article/110/10/2892/7961981)
- [Aberrant WNT/β-catenin signaling in parathyroid carcinoma (Springer)](https://link.springer.com/article/10.1186/1476-4598-9-294)
- [Parathyroid Cancer Treatment - NCI](https://www.cancer.gov/types/parathyroid/patient/parathyroid-treatment-pdq)
- [Lenvatinib in Metastatic Parathyroid Carcinoma (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12449643)
- [Pembrolizumab in MSI-unstable metastatic PC (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13008480/)
- [Parafibromin IHC panel for PC diagnosis (Springer)](https://link.springer.com/article/10.1007/s00268-014-2700-2)
- [Immunohistochemical Profile of Parathyroid Tumours (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9266566/)
- [Mice deleted for Cdc73 develop parathyroid tumours (Nature Oncogene)](https://www.nature.com/articles/onc201743)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 17 |
| On topic | 14 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42577903` *(abstract only)*: "typically avoided...due to the risk of tumor seeding"
  - closest text in source: "Long-term surveillance with serial biochemical monitoring is essential due to the risk of late recurrence"
- `PMID:42577903` *(abstract only)*: "minimal and inconsistent success"
  - Text part not found as substring: 'minimal and inconsistent success' (note: only abstract available for PMID:42577903, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:38198197` (1 mention) - Results of Gensingen Bracing in Patients With Adolescent Idiopathic Scoliosis: Retrospective Cross-Sectional Feasibility Study.
  - shared terms: year

Weighed against this report's own most characteristic terms: `parathyroid`, `carcinoma`, `tumor`, `cdc73`, `disease`, `mutation`, `cell`, `gland`, `year`, `pth`, `invasion`, `hypercalcemia`, `survival`, `bone`, `metastatic`, `recurrence`, `sporadic`, `parafibromin`, `calcium`, `primary`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 52 |
| Terms named correctly | 35 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012004` (2 mentions) - the report calls it "MONDO", "parathyroid gland carcinoma"; MONDO calls it **parathyroid gland carcinoma**
- `HP:0100255` (2 mentions) - the report calls it "Osteitis fibrosa cystica"; HP calls it **Metaphyseal dysplasia**
- `UBERON:0002048` (2 mentions) - the report calls it "Lung — most common distant metastatic site", "lung"; UBERON calls it **lung**
- `UBERON:0004765` (1 mention) - the report calls it "Bone/skeleton — metastatic deposits and PTH-mediated skeletal disease"; UBERON calls it **skeletal element**
- `UBERON:0002107` (2 mentions) - the report calls it "Liver — distant metastasis", "liver"; UBERON calls it **liver**
- `UBERON:0002113` (2 mentions) - the report calls it "Kidney — nephrolithiasis, nephrocalcinosis", "kidney"; UBERON calls it **kidney**
- `NCIT:C65509` (2 mentions) - the report calls it "Calcimimetic; enhances CaSR sensitivity", "Cinacalcet Hydrochloride"; NCIT calls it **Eletriptan**
- `NCIT:C65214` (2 mentions) - the report calls it "Anti-RANKL monoclonal antibody", "Denosumab"; NCIT calls it **Acotiamide**
- `CHEBI:77862` (1 mention) - the report calls it "zoledronic acid"; CHEBI calls it **gossypetin(1-)**
- `CHEBI:3306` (1 mention) - the report calls it "Osteoclast inhibitor (transient)"; CHEBI calls it **calcitonin**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0016415` (1 mention), reported as "Cervical lymph nodes — regional metastasis" - UBERON does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006306` (obsolete DNA methylation) (1 mention)
- `GO:0098532` (obsolete histone H3-K27 trimethylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000787` (2 mentions) - the report calls it "Nephrolithiasis"; HP calls it **Kidney stone**, and lists "Nephrolithiasis" among its other names
- `HP:0100028` (2 mentions) - the report calls it "Abnormality of the parathyroid gland"; HP calls it **Ectopic thyroid**, and lists "Abnormal thyroid location" among its other names
- `GO:0051896` (3 mentions) - the report calls it "regulation of protein kinase B signaling", "Regulation of protein kinase B signaling"; GO calls it **regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction**, and lists "regulation of protein kinase B signaling" among its other names
- `GO:0006306` (1 mention) - the report calls it "DNA methylation"; GO calls it **obsolete DNA methylation**
- `GO:0098532` (1 mention) - the report calls it "Histone H3-K27 trimethylation"; GO calls it **obsolete histone H3-K27 trimethylation**
- `UBERON:0001132` (2 mentions) - the report calls it "Primary**: Parathyroid glands", "parathyroid gland"; UBERON calls it **parathyroid gland**
- `UBERON:0002046` (2 mentions) - the report calls it "Thyroid gland — direct local invasion", "thyroid gland"; UBERON calls it **thyroid gland**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0012004` - called "MONDO", "parathyroid gland carcinoma"
- `GO:0060070` - called "canonical Wnt signaling pathway", "Canonical Wnt signaling pathway"
- `GO:0051896` - called "regulation of protein kinase B signaling", "Regulation of protein kinase B signaling"
- `GO:0006915` - called "apoptotic process", "Apoptotic process"
- `GO:0045453` - called "Bone resorption", "bone resorption"
- `UBERON:0001132` - called "Primary**: Parathyroid glands", "parathyroid gland"
- `UBERON:0002046` - called "Thyroid gland — direct local invasion", "thyroid gland"
- `UBERON:0002048` - called "Lung — most common distant metastatic site", "lung"
- `UBERON:0002107` - called "Liver — distant metastasis", "liver"
- `UBERON:0002113` - called "Kidney — nephrolithiasis, nephrocalcinosis", "kidney"
- `NCIT:C65509` - called "Calcimimetic; enhances CaSR sensitivity", "Cinacalcet Hydrochloride"
- `NCIT:C65214` - called "Anti-RANKL monoclonal antibody", "Denosumab"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.