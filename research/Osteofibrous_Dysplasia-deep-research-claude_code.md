---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-6[1m]
cached: false
start_time: '2026-10-13T09:54:48.350443'
end_time: '2026-10-13T09:59:38.667967'
duration_seconds: 290.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Osteofibrous Dysplasia
  mondo_id: MONDO:0011806
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
  - claude-opus-4-6[1m]
  web_search_requests: 15
  num_turns: 24
  total_cost_usd: 1.8051985000000002
  session_id: c589d242-7ed4-4045-b1c4-777895c58077
  stop_reason: end_turn
  assistant_text_blocks: 2
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
citation_count: 12
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 6
  quotes_unsupported: 8
  unsupported_quote_references:
  - PMID:26637977
  - PMID:38539216
  - PMID:41746735
  relevance_assessed: 11
  on_topic: 8
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 34
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 4
  labels_mismatched: 21
  mislabelled_terms:
  - term_id: MONDO:0011806
    reported_labels:
    - MONDO
    - Disease
    ontology_label: osteofibrous dysplasia
  - term_id: HP:0002979
    reported_labels:
    - Bowing of the legs
    - Phenotype
    ontology_label: Bowing of the legs
  - term_id: HP:0002653
    reported_labels:
    - Bone pain
    - Phenotype
    ontology_label: Bone pain
  - term_id: HP:0002757
    reported_labels:
    - Recurrent fractures
    - cortical thinning
    - Phenotype
    ontology_label: Recurrent fractures
  - term_id: HP:0006543
    reported_labels:
    - Pseudoarthrosis of long bones
    - Phenotype
    ontology_label: Cardiorespiratory arrest
  - term_id: GO:0048012
    reported_labels:
    - hepatocyte growth factor receptor signaling pathway
    - Biological process
    ontology_label: hepatocyte growth factor receptor signaling pathway
  - term_id: GO:0000165
    reported_labels:
    - MAPK cascade
    - Biological process
    ontology_label: MAPK cascade
  - term_id: GO:0006511
    reported_labels:
    - ubiquitin-dependent protein catabolic process
    - Biological process
    ontology_label: ubiquitin-dependent protein catabolic process
  - term_id: GO:0001649
    reported_labels:
    - osteoblast differentiation
    - Biological process
    ontology_label: osteoblast differentiation
  - term_id: GO:0030282
    reported_labels:
    - bone mineralization
    - Biological process
    ontology_label: bone mineralization
  - term_id: CL:0000062
    reported_labels:
    - osteoblast
    - Cell type
    ontology_label: osteoblast
  - term_id: CL:0000057
    reported_labels:
    - fibroblast
    - Cell type
    ontology_label: fibroblast
  - term_id: CL:0000092
    reported_labels:
    - osteoclast
    - Cell type
    ontology_label: osteoclast
  - term_id: UBERON:0000979
    reported_labels:
    - tibia
    - Anatomy
    ontology_label: tibia
  - term_id: UBERON:0001446
    reported_labels:
    - fibula
    - Anatomy
    ontology_label: fibula
  - term_id: UBERON:0002515
    reported_labels:
    - periosteum
    - Anatomy
    ontology_label: periosteum
  - term_id: HP:0000006
    reported_labels:
    - Pattern:** Autosomal dominant
    - Phenotype
    ontology_label: Autosomal dominant inheritance
  - term_id: NCIT:C15747
    reported_labels:
    - Supportive Care
    - Treatment
    ontology_label: Supportive Care
  - term_id: NCIT:C15329
    reported_labels:
    - Surgical Procedure
    - Treatment
    ontology_label: Surgical Procedure
  - term_id: NCIT:C15240
    reported_labels:
    - Genetic Counseling
    - Treatment
    ontology_label: Genetic Counseling
  - term_id: GO:0004714
    reported_labels:
    - Molecular function
    ontology_label: transmembrane receptor protein tyrosine kinase activity
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0014065
    ontology_label: obsolete phosphatidylinositol 3-kinase signaling
    replaced_by: GO:0043491
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Osteofibrous Dysplasia
- **MONDO ID:** MONDO:0011806 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Osteofibrous Dysplasia** covering all of the
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

Let me gather comprehensive information on Osteofibrous Dysplasia from multiple sources.

Now I have comprehensive information to compile the research report. Let me write it up.

---

# Comprehensive Research Report: Osteofibrous Dysplasia

## 1. Disease Information

### Overview

Osteofibrous dysplasia (OFD), also known as Kempson-Campanacci lesion or ossifying fibroma of long bones, is a rare, benign, self-limited fibro-osseous lesion that primarily affects the cortical bone of the anterior mid-shaft of the tibia in children. It is characterized by the replacement of normal cortical bone with fibrous tissue and immature woven bone lined by prominent osteoblasts. OFD accounts for approximately 0.2% of all primary bone tumors (PMID:38539216). The condition typically presents in infancy and early childhood with painless anterior tibial swelling or bowing, and it generally arrests or spontaneously regresses at skeletal maturity.

OFD was first described by Frangenheim in 1921 and later characterized as a distinct entity by Kempson (1966) and Campanacci (1976), whose names are eponymously attached to the lesion. The pathogenesis has been significantly clarified by the landmark discovery that germline mutations in the *MET* proto-oncogene, encoding a receptor tyrosine kinase, cause an autosomal dominant form of OFD (PMID:26637977).

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| MONDO | MONDO:0011806 |
| OMIM | 607278 (Osteofibrous Dysplasia, Susceptibility To; OSFD) |
| Orphanet | ORPHA:488265 |
| ICD-10 | M85.0 (Other fibrous dysplasia of bone) |
| ICD-11 | LD24.2Y |
| MeSH | C563276 |
| UMLS | C1709353 |
| GARD | 10887 |
| Gene (OMIM) | MET (*164860) |

### Synonyms

- Kempson-Campanacci lesion
- OFD / OSFD
- Ossifying fibroma of long bones
- Cortical fibrous dysplasia
- Osteofibrous dysplasia of bone
- Congenital fibrous defect of the tibia

### Information Sources

Information derives from aggregated disease-level resources (OMIM, Orphanet, published case series, and molecular genetics literature). No large-scale EHR-derived data are available given the extreme rarity of the condition.

---

## 2. Etiology

### Disease Causal Factors

OFD is a **genetically determined disorder of periosteal osteogenesis**. The primary cause in familial cases is heterozygous germline mutation in the *MET* gene (7q31.2), which encodes the hepatocyte growth factor (HGF) receptor, a receptor tyrosine kinase. Gray et al. (2015) demonstrated that "germline mutations in MET, encoding a receptor tyrosine kinase, segregate with an autosomal-dominant form of OFD in three families and a mutation in a fourth affected subject from a simplex family with bilateral disease" (PMID:26637977).

In sporadic unilateral cases, somatic *MET* mutations affecting the same functional domain (exon 14/juxtamembrane region) have been identified. Additionally, cytogenetic studies have revealed clonal trisomies (chromosomes 7, 8, 12, and 22), suggesting a neoplastic component in some cases (PMID:8156503).

### Risk Factors

**Genetic risk factors:**
- Heterozygous germline *MET* mutations causing exon 14 skipping (autosomal dominant inheritance with incomplete penetrance)
- Somatic *MET* exon 14 mutations (e.g., Y1003S) in sporadic disease
- Trisomies of chromosomes 7, 8, 12, and/or 22 (PMID:8156503)
- A case report identified novel *CDK12* and *DDR2* mutations in a neonatal OFD patient (PMC9982453)

**Environmental/demographic risk factors:**
- Age: Childhood onset (median age ~9.5 years; 43.8% diagnosed before age 6) (PMID:38539216)
- Sex: Males slightly more commonly affected than females in most series
- No known environmental exposures, toxins, or infectious agents contribute to disease

### Protective Factors

No specific genetic or environmental protective factors have been identified for OFD.

### Gene-Environment Interactions

No gene-environment interactions have been documented for OFD. The disease appears to be entirely determined by genetic factors affecting *MET* receptor signaling.

---

## 3. Phenotypes

### Clinical Phenotypes

| Phenotype | HPO Term | Frequency | Onset | Severity |
|-----------|----------|-----------|-------|----------|
| Anterior tibial bowing | HP:0002979 (Bowing of the legs) | ~13% at presentation | Infancy/childhood | Mild to moderate |
| Painless tibial swelling/mass | HP:0002797 (Abnormality of the tibial metaphysis) / HP:0100555 (Asymmetric growth) | ~37% asymptomatic/incidental | Infancy/childhood | Variable |
| Bone pain | HP:0002653 (Bone pain) | ~31% | Childhood | Mild to moderate |
| Pathologic fractures | HP:0002757 (Recurrent fractures) | ~19% | Childhood | Moderate to severe |
| Pseudarthrosis of lower limb | HP:0006543 (Pseudoarthrosis of long bones) | Subset of fracture patients | Childhood | Severe |
| Fibular lesions | HP:0002992 (Abnormality of tibia morphology) | ~3.8% fibula only; tibial+fibular common in neonates | Neonatal/childhood | Variable |
| Radiolucent cortical lesion | HP:0002757 (cortical thinning) | ~100% | All ages | Variable |
| Delayed fracture healing | HP:0002757 / HP:0006443 (Abnormality of long bone morphology) | Common with fractures | Childhood | Moderate |

**Key phenotype characteristics:**

- **Age of onset:** Typically presents in infancy or early childhood (usually <10 years). Neonatal presentation has been documented (PMID:38539216).
- **Progression:** Self-limited in most cases; "lesions usually disappear and do not cause problems in adulthood" (PMID:38539216). Up to 25% of cases spontaneously regress at puberty.
- **Distribution:** 85% monostotic (single bone involvement), ~5% polyostotic. The anterior cortex of the tibial diaphysis is the classic location.
- **Quality of life impact:** In most cases, minimal long-term impact. Significant morbidity occurs in patients with pathologic fractures, persistent pseudarthrosis, or progressive deformity requiring multiple surgeries.

### Histopathological Phenotypes

- **Zonal architecture:** "Spindle-shaped fibroblast-like cells in the center of the lesions that are progressively replaced with peripherally located, more differentiated cells from the osteoblastic lineage" (PMID:38539216)
- **Osteoblastic rimming of woven bone:** The hallmark histologic feature; "woven bone trabeculae with osteoblastic rimming are seen against bland fibroblastic stroma with storiform pattern" (PMID:38539216)
- **Scattered cytokeratin-positive epithelial cells:** Demonstrable on immunostaining but not visible on H&E; links OFD to the adamantinoma spectrum

---

## 4. Genetic/Molecular Information

### Causal Gene

**MET** (MET proto-oncogene, receptor tyrosine kinase)
- **HGNC:** hgnc:7029
- **OMIM:** *164860
- **Chromosomal location:** 7q31.2
- **Protein:** Hepatocyte growth factor receptor (c-Met)

### Pathogenic Variants

Gray et al. (2015) identified the molecular basis of OFD:

> "Mutations identified in all families with dominant inheritance and in the one simplex subject with bilateral disease abolished the splice inclusion of exon 14 in MET transcripts, which resulted in a MET receptor (MET^Δ14) lacking a cytoplasmic juxtamembrane domain." (PMID:26637977)

**Specific variants documented:**

| Variant | Type | Origin | Effect |
|---------|------|--------|--------|
| 26-bp deletion in *MET* (intron 13–exon 14 junction) | Splice-site deletion | Germline (AD family) | Exon 14 skipping; loss of juxtamembrane domain |
| Other splice-site mutations abolishing exon 14 inclusion | Splice-site | Germline (multiple families) | Exon 14 skipping |
| Y1003S (c.3008A>C) | Missense (somatic) | Somatic (unilateral OFD) | Loss of CBL binding site; MET receptor stabilization |
| c.3028+1G>T | Splice-site | Germline | Exon 14 skipping (ClinVar: RCV000210870) |
| p.His1094Arg | Missense | Germline | Reported in ClinVar (Variation ID 13887) |

**Variant classification:** Pathogenic (ACMG criteria)

**Functional consequences:**
- **Gain-of-function:** All documented mutations stabilize the MET receptor by preventing its ubiquitin-mediated degradation. "Loss of the CBL pY1003 docking site in OFD leads to reduced receptor internalization and degradation, stabilizing the MET receptor and conferring a gain-of-function to the protein" (PMID:26637977).
- The exon 14-encoded juxtamembrane domain normally contains the Y1003 residue where the E3 ubiquitin ligase CBL docks to promote receptor internalization and proteasomal degradation.

**Somatic vs. germline:**
- Familial OFD (bilateral or multifocal): germline *MET* mutations
- Sporadic unilateral OFD: somatic *MET* mutations in some cases; a somatic Y1003S mutation was identified in 1 of 20 sporadic samples analyzed (PMID:26637977)

### Additional Genomic Findings (2026)

Hung et al. (2026) performed targeted next-generation sequencing and whole-genome SNP arrays on 10 tumors (3 classic adamantinomas, 5 OFDs, 2 OFD-like adamantinomas). In the 5 OFDs:

> "KMT2A p.C2441F, KMT2D p.S1040P, PHOX2B p.G213D, and RIF1 deletion were each present in 1 case; no additional copy number/single-nucleotide variants were identified." (PMID:42379271)

This study concluded: "classic adamantinomas and OFD might be genetically distinct," as classic adamantinomas harbored multiple copy number gains (chromosomes 7, 8, 10, 12, 19) while OFDs did not.

### Cytogenetic Abnormalities

Clonal chromosomal trisomies (chromosomes 7, 8, 12, and 22) have been demonstrated in some OFD cases, suggesting "a clonal and possibly neoplastic origin for osteofibrous dysplasia" (PMID:8156503). Notably, trisomy 7 involves the chromosome harboring the *MET* gene.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been implicated in the pathogenesis of OFD. The disease is entirely attributable to genetic lesions in the *MET* signaling pathway.

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Ordered Mechanistic Steps)

1. **Initiating lesion — MET exon 14 loss (germline or somatic):** Mutations abolish regulated inclusion of *MET* exon 14, producing a receptor lacking the cytoplasmic juxtamembrane domain (MET^Δ14), OR somatic missense mutation (Y1003S) directly eliminates the CBL binding site → **leads to**

2. **MET receptor stabilization and gain of function:** Loss of the CBL E3 ubiquitin ligase docking site (Y1003) prevents normal HGF-induced receptor internalization and proteasomal degradation. The mature MET protein is stabilized on the cell surface → **results in**

3. **Prolonged activation of downstream RAS-MAPK and PI3K-AKT signaling:** The stabilized MET receptor sustains ligand-dependent activation of downstream signaling cascades, particularly the RAS/MAPK (ERK1/2) pathway. "MetΔJMD cells demonstrated delayed ERK pathway normalization after hepatocyte growth factor stimulation" (PMID:41746735) → **leads to**

4. **Impaired osteoblastic differentiation of periosteal progenitor cells:** Hyperactive MAPK signaling retards the differentiation of skeletal progenitor cells into mature osteoblasts. "Forced induction of this exon-exclusion event retarded osteoblastic differentiation in vitro and inhibited bone-matrix mineralization" (PMID:26637977). Expression of osteogenic genes (IBSP, RUNX2, OSX, OCN, DMP1) is suppressed (PMID:41746735) → **results in**

5. **Defective periosteal osteogenesis and cortical bone formation:** The periosteum, which normally contributes to cortical bone repair and maintenance, produces immature woven bone rather than mature lamellar bone. This creates the characteristic fibro-osseous lesion with zonal architecture → **leads to**

6. **Radiolucent cortical lesion with tibial bowing:** The fibro-osseous tissue replaces normal cortical bone in the anterior tibial diaphysis, causing cortical thinning, expansion, and anterior bowing → **predisposes to**

7. **Pathologic fracture with delayed healing (pseudarthrosis):** Weakened cortical bone is susceptible to fracture, and the same defect in osteoblast differentiation impairs fracture repair. "Fracture repair was delayed in MetΔ15-HET mice, with decreased bone formation observed 2-week postfracture" (PMID:39042586)

### Molecular Pathways

- **HGF/MET receptor tyrosine kinase signaling** (GO:0048012 — hepatocyte growth factor receptor signaling pathway)
- **RAS-MAPK/ERK signaling cascade** (GO:0000165 — MAPK cascade): The primary downstream effector pathway; hyperactivation retards osteoblast differentiation
- **PI3K-AKT signaling pathway** (GO:0014065 — phosphatidylinositol 3-kinase signaling): Also sustained by MET stabilization
- **Ubiquitin-proteasome pathway** (GO:0006511 — ubiquitin-dependent protein catabolic process): CBL-mediated MET receptor degradation is disrupted

### Cellular Processes

- **Osteoblast differentiation** (GO:0001649 — osteoblast differentiation): Retarded by MET gain-of-function
- **Bone mineralization** (GO:0030282 — bone mineralization): Inhibited
- **Receptor internalization** (GO:0031623 — receptor internalization): Impaired for MET
- **Protein ubiquitination** (GO:0016567 — protein ubiquitination): CBL-mediated MET ubiquitination is disrupted

### Cell Types Involved

| Cell Type | CL Term | Role |
|-----------|---------|------|
| Osteoblast | CL:0000062 (osteoblast) | Differentiation is impaired; rimming osteoblasts are a histologic hallmark |
| Skeletal/periosteal progenitor cell | CL:0007010 (progenitor cell of endochondral bone) | Primary cell population affected; impaired differentiation |
| Fibroblast | CL:0000057 (fibroblast) | Proliferating spindle-shaped cells form the fibrous stroma |
| Osteoclast | CL:0000092 (osteoclast) | Present at lesion margins; involved in bone remodeling |

### Protein Dysfunction

The MET receptor (UniProt: P08581) normally undergoes regulated exon skipping of exon 14 during embryonic development. In OFD, constitutive loss of the juxtamembrane domain eliminates the Y1003 docking site for the CBL E3 ubiquitin ligase. This prevents normal ligand-stimulated receptor downregulation, leading to prolonged surface expression and sustained downstream signaling. The result is a ligand-dependent gain-of-function rather than constitutive activation.

### Relationship to RASopathies

OFD has recently been classified as a **skeletal RASopathy** due to its mechanism of aberrant RAS-MAPK pathway activation downstream of MET. This classification was supported by the therapeutic response to MEK inhibition (PMID:41746735), placing OFD alongside neurofibromatosis type 1 (NF1) tibial pseudarthrosis as another skeletal RASopathy with impaired osteogenesis driven by MAPK hyperactivation.

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary:** Bone, specifically the tibial diaphysis (anterior cortex)
- **Secondary:** Fibula (concurrent tibial-fibular involvement is common in neonatal cases); rare involvement of ulna, radius, femur, humerus, rib, ischium, tarsals, metatarsals, vertebrae, and capitate has been reported (PMID:38539216)
- **Body system:** Musculoskeletal system

### Tissue and Cell Level

- **Tissue:** Cortical bone, periosteum, bone marrow (rarely involved)
- **Cell types:** Periosteal progenitor cells (CL:0007010), osteoblasts (CL:0000062), fibroblasts (CL:0000057)

### Anatomical Localization

- **UBERON:** UBERON:0000979 (tibia); UBERON:0001446 (fibula); UBERON:0002515 (periosteum)
- **Specific site:** Anterior cortex of the tibial diaphysis (mid-shaft)
- **Lateralization:** Most cases are unilateral; bilateral disease occurs in familial/germline cases

---

## 8. Temporal Development

### Onset

- **Typical age of onset:** Infancy to early childhood (median ~9.5 years; many diagnosed before age 6; neonatal cases have been documented)
- **Onset pattern:** Insidious; usually presents as painless swelling or incidental radiographic finding
- Suggested HPO onset term: HP:0011463 (Childhood onset) or HP:0003593 (Infantile onset)

### Progression

- **Disease course:** Self-limited in most cases
- **Phases:**
  - **Active phase (childhood):** Lesions may slowly enlarge, causing progressive bowing, cortical thinning, and predisposing to pathologic fracture
  - **Quiescent/regression phase (puberty/skeletal maturity):** Lesions typically arrest and may spontaneously regress. Up to 25% regress at puberty (PMID:38539216)
  - **Adulthood:** "Lesions usually disappear and do not cause problems in adulthood" (PMID:38539216)
- **Duration:** Chronic during childhood; self-resolving in most patients

### Patterns

- **Spontaneous regression:** Documented, particularly at puberty; one case showed near-complete regression within 1.5 months after biopsy (PMID:23774157)
- **Critical period:** The growth phase of childhood is the vulnerable period; surgical intervention should be "delayed for as long as possible" until skeletal maturity when possible (PMID:38539216)

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** Extremely rare; no precise population-based prevalence estimate exists. OFD accounts for approximately 0.2% of all primary bone tumors (PMID:38539216)
- **Prevalence class:** ULTRA_RARE / NOT_YET_DOCUMENTED

### Inheritance

- **Pattern:** Autosomal dominant (HP:0000006) with incomplete penetrance
- **Penetrance:** Incomplete; one unaffected individual carried the causative *MET* mutation in a 4-generation family (PMID:26637977)
- **Expressivity:** Variable; familial cases may show bilateral disease, while sporadic cases are typically unilateral

### Population Demographics

- **Sex ratio:** Slight male predominance in most series, though some report female predilection (PMID:38539216)
- **Age distribution:** Predominantly childhood/adolescent; median age 9.5 years
- **Geographic distribution:** No known ethnic or geographic predilection; cases reported worldwide
- **Ethnic distribution:** No founder effects or population-specific variants reported

---

## 10. Diagnostics

### Clinical Tests

**Imaging:**
- **Radiography (primary modality):** Anterior eccentric, intracortical, lytic/lucent lesion of the tibial diaphysis with sclerotic borders. Cortical expansion and anterior tibial bowing are common. Five radiographic subtypes have been described: ground-glass, cystic, insect phagocytic, towel-gourd ladle, and sclerotic (PMID:38539216).
- **CT:** Superior for evaluating cortical involvement, periosteal reaction, matrix mineralization, and pathologic fractures.
- **MRI:** Demonstrates "bubbly appearance and lobular loculations with well-circumscribed sclerotic edges," with "intermediate to high on T2WI and intermediate on T1WI" signal characteristics (PMID:38539216). Critical for distinguishing OFD from adamantinoma: extension into the medullary canal or soft tissues suggests adamantinoma.

**Biopsy and histopathology:**
- **Open biopsy** is recommended (large tissue samples to avoid misdiagnosis).
- **Characteristic findings:** Loose storiform fibrovascular stroma with woven bone trabeculae showing prominent osteoblastic rimming; zonal architecture
- **Immunohistochemistry:** Scattered cytokeratin-positive (CK7, CK19, CK14) epithelial cells may be present; keratin expression links OFD to the adamantinoma spectrum
- **Key negative:** GNAS mutation absent (distinguishes from fibrous dysplasia)

### Genetic Testing

- Targeted sequencing of *MET* exon 14 and surrounding splice sites
- Recommended in familial/bilateral cases
- ClinVar lists pathogenic/likely pathogenic *MET* variants for OFD

### Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Fibrous dysplasia** | Lacks osteoblastic rimming; GNAS mutations present; medullary-based; ground-glass matrix |
| **Classic adamantinoma** | Prominent epithelial component on H&E; cortical AND medullary involvement; soft tissue extension; multiple chromosomal gains (7, 8, 10, 12, 19) (PMID:42379271) |
| **OFD-like adamantinoma** | Tumor clusters visible on light microscopy and/or cytokeratin/p40 immunostaining; intermediate between OFD and classic adamantinoma |
| **Non-ossifying fibroma** | Eccentric metaphyseal location; no osteoblastic rimming |
| **Aneurysmal bone cyst** | Blood-filled spaces; more aggressive appearance |
| **Osteoid osteoma** | Nidus with surrounding sclerosis; pain relieved by NSAIDs |

---

## 11. Outcome/Prognosis

### Survival and Mortality

- **Life expectancy:** Normal; OFD is a benign, self-limited condition with excellent prognosis
- **Mortality:** No disease-specific mortality reported
- **Malignant transformation:** Rare; isolated reports of progression to osteosarcoma have been documented but are exceptional (PMID:38539216)

### Morbidity

- **Primary morbidity:** Pathologic fractures (19% of cases) with significantly delayed healing; progressive tibial bowing and deformity during childhood
- **Pseudarthrosis:** A subset of fracture patients develop persistent non-union requiring multiple surgical interventions; this was the primary target of MEK inhibitor therapy (PMID:41746735)
- **Recurrence after surgery:** ~25% after curettage; lower with extra-periosteal wide excision (PMID:38539216)

### Prognostic Factors

- **Favorable:** Older age at presentation, monostotic disease, lesion stability on serial imaging, proximity to skeletal maturity
- **Unfavorable:** Neonatal onset, polyostotic disease, progressive enlargement, pathologic fractures, bilateral involvement

---

## 12. Treatment

### Conservative Management

- **Observation:** Recommended for asymptomatic patients or those with small, stable lesions. The self-limiting nature of OFD supports watchful waiting, especially in young children (PMID:38539216).
- **Bracing:** External bracing to prevent fracture and minimize deformity during the growth phase.
- **NCIT:** NCIT:C15747 (Supportive Care)

### Surgical Interventions

- **Curettage with bone grafting:** Acceptable in older patients with stable lesions, but carries a 25% recurrence rate (PMID:38539216)
  - NCIT: NCIT:C15329 (Surgical Procedure)
- **Extra-periosteal ("shark-bite") resection:** Most widely used surgical technique for progressive lesions
- **Wide/en bloc excision:** Preferred for growing lesions due to concern for malignant transformation; may require reconstruction with bone graft or vascularized fibula graft
- **Corrective osteotomy with intramedullary nailing:** For significant tibial bowing deformity
- **Timing:** Surgery should be delayed until skeletal maturity when possible; early surgery in growing children has higher recurrence rates

### Pharmacotherapy (Emerging)

**MEK inhibitor — Mirdametinib (PD-0325901):**

This represents a landmark therapeutic advance for OFD. Kannu and colleagues (2025/2026) demonstrated:

> "Inhibition of MAPK signaling with MEK inhibitors restored osteogenic differentiation of mouse Met^ΔJMD skeletal progenitor cells and promoted the activation of transcriptional signatures associated with skeletal development and osteoblast differentiation in pseudarthrosis-derived primary cells from patients with osteofibrous dysplasia." (PMID:41746735)

A pediatric patient with OFD and 3 years of persistent pseudarthrosis (after six failed surgeries) achieved fracture union after treatment with mirdametinib combined with surgical intervention.

- NCIT: NCIT:C15986 (Pharmacotherapy)
- Therapeutic modality: SMALL_MOLECULE
- This positions OFD as a skeletal RASopathy amenable to targeted pathway inhibition

### Treatment Strategy

1. **First-line:** Observation with serial imaging for asymptomatic/stable lesions
2. **For progressive deformity or fracture:** Bracing; surgical correction if needed, delayed to skeletal maturity when possible
3. **For persistent pseudarthrosis:** Consideration of MEK inhibitor therapy (mirdametinib) based on emerging evidence (PMID:41746735)
4. **Long-term follow-up:** Recommended to monitor for recurrence and the rare possibility of malignant transformation

---

## 13. Prevention

### Genetic Counseling

- Autosomal dominant inheritance with incomplete penetrance warrants genetic counseling for affected families
- *MET* exon 14 sequencing can identify at-risk family members
- Prenatal genetic diagnosis is technically feasible but rarely pursued given the benign nature of the disease
- NCIT: NCIT:C15240 (Genetic Counseling)

### Screening

- No population-based screening programs exist
- Cascade screening of family members (clinical and radiographic) is appropriate when a germline *MET* mutation is identified

### Prevention Strategies

- No primary prevention exists
- Secondary prevention: Early radiographic surveillance in children of affected parents to detect lesions before fracture
- Tertiary prevention: Bracing and activity modification to prevent pathologic fractures; avoidance of premature surgery to reduce recurrence risk

---

## 14. Other Species / Natural Disease

No naturally occurring ortholog of osteofibrous dysplasia has been reported in domestic or wild animal species.

---

## 15. Model Organisms

### Mouse Models

**MetΔ15-HET mouse (heterozygous Met exon 15 skipping):**
- **Species:** Mouse (*Mus musculus*, NCBITaxon:10090)
- **Generation:** CRISPR/Cas9-targeted splice donor of murine *Met* exon 15 (equivalent to human exon 14)
- **Phenotype:**
  - No gross skeletal defects at baseline
  - "Fracture repair was delayed in MetΔ15-HET mice, with decreased bone formation observed 2-week postfracture" (PMID:39042586)
  - RNA-seq revealed aberrant MET-related signaling in murine osteoblasts
- **Phenotype recapitulation:** PARTIAL — the model recapitulates delayed fracture healing but does not reproduce the spontaneous cortical lesions seen in human OFD
- **Limitations:** Mice do not develop the characteristic tibial fibro-osseous lesions spontaneously; the fracture phenotype requires experimental induction
- **Source:** Hong et al., FASEB J, 2024 (PMID:39042586)

**MetΔJMD conditional mouse (Kannu lab):**
- **Phenotype:** Impaired osteogenic differentiation of periosteal progenitor cells in vitro; increased cortical porosity and reduced bone stiffness in vivo
- **Applications:** Used to demonstrate that MEK inhibitors restore osteogenic differentiation; provided preclinical basis for mirdametinib therapy (PMID:41746735)
- **Key finding:** Conditional *Met* deletion enhanced osteogenic differentiation, indicating bidirectional regulation of osteogenesis by MET

### In Vitro Models

- Primary periosteal osteoblast cultures from OFD patients
- Pseudarthrosis-derived primary cells from OFD patients (used in mirdametinib study) (PMID:41746735)
- Forced MET exon 14 exclusion in osteoblast cell lines (PMID:26637977)

---

## Key References

| PMID | Citation | Key Contribution |
|------|----------|-----------------|
| **26637977** | Gray MJ et al. Am J Hum Genet. 2015;97(4):491-498. | Landmark identification of *MET* exon 14 skipping mutations as cause of OFD |
| **39042586** | Hong G et al. FASEB J. 2024;38(14):e23816. | MetΔ15-HET mouse model showing delayed fracture repair |
| **41746735** | (Kannu lab). J Clin Invest. 2025/2026. | MEK inhibitor mirdametinib promotes fracture healing in OFD; first targeted therapy |
| **42379271** | Hung YP et al. Mod Pathol. 2026. | Genomic characterization distinguishing OFD from adamantinoma |
| **38539216** | Liu R et al. J Orthop Surg Res. 2024;19:204. | Comprehensive narrative review of OFD |
| **34742490** | Nascimento AF et al. Surg Pathol Clin. 2021;14(4):675-687. | OFD and adamantinoma spectrum review |
| **8156503** | Bridge JA et al. Cancer. 1994;73(6):1746-1752. | Clonal chromosomal abnormalities in OFD |
| **23774157** | (Campanacci case). 2013. | Spontaneous post-bioptic regression of OFD |

---

## Ontology Term Summary

| Domain | Term ID | Label |
|--------|---------|-------|
| Disease | MONDO:0011806 | osteofibrous dysplasia |
| Gene | hgnc:7029 | MET |
| Molecular function | GO:0004714 | transmembrane receptor protein tyrosine kinase activity |
| Biological process | GO:0048012 | hepatocyte growth factor receptor signaling pathway |
| Biological process | GO:0001649 | osteoblast differentiation |
| Biological process | GO:0030282 | bone mineralization |
| Biological process | GO:0000165 | MAPK cascade |
| Biological process | GO:0006511 | ubiquitin-dependent protein catabolic process |
| Cell type | CL:0000062 | osteoblast |
| Cell type | CL:0000057 | fibroblast |
| Cell type | CL:0000092 | osteoclast |
| Anatomy | UBERON:0000979 | tibia |
| Anatomy | UBERON:0001446 | fibula |
| Anatomy | UBERON:0002515 | periosteum |
| Phenotype | HP:0002979 | Bowing of the legs |
| Phenotype | HP:0002653 | Bone pain |
| Phenotype | HP:0002757 | Recurrent fractures |
| Phenotype | HP:0006543 | Pseudoarthrosis |
| Phenotype | HP:0000006 | Autosomal dominant inheritance |
| Treatment | NCIT:C15329 | Surgical Procedure |
| Treatment | NCIT:C15986 | Pharmacotherapy |
| Treatment | NCIT:C15747 | Supportive Care |
| Treatment | NCIT:C15240 | Genetic Counseling |

---

Sources:
- [Gray MJ et al. (2015) - MET mutations cause OFD (PMID:26637977)](https://pubmed.ncbi.nlm.nih.gov/26637977)
- [Hong G et al. (2024) - Mouse model of MET-related OFD (PMID:39042586)](https://pubmed.ncbi.nlm.nih.gov/39042586)
- [Liu R et al. (2024) - OFD narrative review (PMID:38539216)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10967096/)
- [Hung YP et al. (2026) - Genomic characterization of OFD and adamantinoma (PMID:42379271)](https://pubmed.ncbi.nlm.nih.gov/42379271)
- [MEK inhibitor mirdametinib in OFD (PMID:41746735)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13132394/)
- [Nascimento AF et al. (2021) - OFD and adamantinoma review (PMID:34742490)](https://pubmed.ncbi.nlm.nih.gov/34742490)
- [Bridge JA et al. (1994) - Chromosomal abnormalities in OFD (PMID:8156503)](https://pubmed.ncbi.nlm.nih.gov/8156503)
- [OMIM #607278 - Osteofibrous Dysplasia](https://www.omim.org/entry/607278)
- [Orphanet: Osteofibrous Dysplasia (ORPHA:488265)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=488265)
- [StatPearls: Osteofibrous Dysplasia](https://www.ncbi.nlm.nih.gov/sites/books/NBK563281/)
- [Monarch Initiative: MONDO:0011806](https://monarchinitiative.org/MONDO:0011806)
- [Pathology Outlines: Osteofibrous Dysplasia](https://www.pathologyoutlines.com/topic/boneosteofibrousdysplasia.html)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 8 |
| References weighed for topical relevance | 11 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

4 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:26637977` *(abstract only)*: "germline mutations in MET, encoding a receptor tyrosine kinase, segregate with an autosomal-dominant form of OFD in three families and a mutation in a fourth affected subject from a simplex family with bilateral disease"
  - closest text in source: "We identified germline mutations in MET, encoding a receptor tyrosine kinase, that segregate with an autosomal-dominant form of OFD in three families and a mutation in a fourth affected subject from a simplex family and with bilateral disease"
- `PMID:38539216`: "lesions usually disappear and do not cause problems in adulthood"
  - closest text in source: "Clinical observation is an alternative conservative treatment method for asymptomatic and mildly symptomatic patients, while surgical intervention is usually indicated for larger lesions accompanied by more obvious deformities or functional problems caused by the pathological fracture"
- `PMID:38539216`: "Spindle-shaped fibroblast-like cells in the center of the lesions that are progressively replaced with peripherally located, more differentiated cells from the osteoblastic lineage"
  - closest text in source: "Table 2Differentiation of OFD from adamantinoma and fibrous dysplasiaItemsOFDADFDAge (years)10 ~ 20OFD-like AD: 10 ~ 20Classic AD: 30 ~ 40Dedifferentiated AD: ~2010 ~ 30 [65]NatureBenignBiphasicBenignCommon location(1) Tibia and/or fibula(2) Arising within the anterior cortex of the diaphyseal [4, 23](1) Tibia and/or fibula, followed in the humerus, ulna, and radius(2) Almost exclusively in the anterior cortex of the diaphysis [62](1) Femur and craniofacial bones(2) Arising within the medullary canal [62]Clinical presentation(1) Pain (25%~50%) or painless(2) Bony deformities (bowing)(3) Pathologic fractures [4, 23](1) Pain and swelling (19%)(2) A palpable mass(3) Bony deformities(4) Pathologic fractures (16%~23%) [66, 67](1) Swelling (56.7%)(2) Pain or tenderness (35.6%)(3) Pathological fracture (14.4%)(4) Limping (7.8%)(5) Maine cafe ´-au-lait spots [65, 68]Imaging findings(1) A single or multiple, variably sized, sharply marginated radiolucencies within the cortex of the tibia or fibula, with a surrounding sclerotic rim(2) An anterior bowing deformity or pathologic fracture may be observed(3) Soft tissue extension is not present, and intramedullary involvement is unusual(4) A CT scan and MRI are useful for confirming the intracortical location of the lesion [69](1) OFD-like AD: Like OFD(2) Classic AD and dedifferentiated AD: a) Well-demarcated, lobulated, radiolucent lesion within cortical bone, imparting a “soap bubble” appearance b) Skip lesions and/or multicentric lesions involving the tibia and/or fibula may be present c) May breach the cortex, extending into the medullary cavity or adjacent soft tissues d) A CT scan and MRI are useful for documenting multifocality, cortical destruction, and soft tissue extension [69](1) The healthy bone is replaced with a more radiolucent, ‘‘ground-glass’’ appearing pattern, with no visible trabecular pattern(2) The periosteal surface is smooth and nonreactive(3) Shepherd’s crook deformity [65]Cross features(1) exclusively intracortical lesion with a tan-gray, solid cut surface and a gritty consistency(2) The perioseum is intact, and the surrounding cortical bone is usually sclerotic and thickened(3) Intramedullary involvement is not typically seen [69](1) Solid, well-demarcated, lobulated lesions, with tan-white cut surfaces(2) Centered within the cortex with variable involvement of the medullary space or extraperiosteal soft tissue [69](1) A well-circumscribed, tangrey mass that is dense and variably fibrous with a gritty quality(2) May be prominent cyst formation(3) A glassier, blue-tinged appearance may be found in cases with chondroid metaplasiaMicroscopic features(1) A loose storiform, fibrovascular stroma, and woven bony trabeculae with osteoblastic rimming [70](2) individual keratin-immunoreactive cells can be detected(1) OFD-like AD: widely scattered, clearly visible small epithelial nests(2) Classic AD: a predominant epithelial component, embedded in an inconspicuous OFD-like bland spindled or fibro-osseous stroma"
- `PMID:38539216`: "woven bone trabeculae with osteoblastic rimming are seen against bland fibroblastic stroma with storiform pattern"
  - closest text in source: "Additionally, osteoid or chondroid matrix may be identified in the dedifferentiated foci [71](1) It is composed of a bland fibrous stromal proliferation admixed with randomly distributed woven bone(2) Keratin-immunoreactive stromal cells are never observed(3) Nodules of benign hyaline cartilage may be present(4) A key feature is the conspicuous absence of osteoblastic rimmingImmunohistochemical featuresEpidermal growth factor receptor was not detected [48]Epidermal growth factor receptor was detected [48]Immunohistochemistry serves no purpose in the diagnosis of FD other than to rule out the possibility of a malignant lesion with a pertinent historyGenetic studiesTrisomies of chromosome 7, 8 and 12 [46, 47](1) Trisomies of chromosome 7, 8 and 12(2) extra copies of 19 and/or 21 [46, 47](3) KMT2D mutations [72](4) P53 mutations [17](5) The chromatin remodeling-related gene histone-lysine N-methyltransferase 2D was “recurrently altered” [72](1) GNAS mutations [47](2) Gs-alpha mutations [47]OFD, osteofibrous dysplasia; AD, adamantinoma; FD, fibrous dysplasia; CT, computed tomography; MRI, magnetic resonance imaging; KMT2D, lysine (K)-specific methyltransferase 2D; P53, tumor protein p53; GNAS, guanine nucleotide-binding protein/a-subunit gene, alpha stimulating activity polypeptide 1 Differentiation of OFD from adamantinoma and fibrous dysplasia OFD-like AD: 10 ~ 20 Classic AD: 30 ~ 40 Dedifferentiated AD: ~20 (1) Tibia and/or fibula (2) Arising within the anterior cortex of the diaphyseal [4, 23] (1) Tibia and/or fibula, followed in the humerus, ulna, and radius (2) Almost exclusively in the anterior cortex of the diaphysis [62] (1) Femur and craniofacial bones (2) Arising within the medullary canal [62] (1) Pain (25%~50%) or painless (2) Bony deformities (bowing) (3) Pathologic fractures [4, 23] (1) Pain and swelling (19%) (2) A palpable mass (3) Bony deformities (4) Pathologic fractures (16%~23%) [66, 67] (1) Swelling (56.7%) (2) Pain or tenderness (35.6%) (3) Pathological fracture (14.4%) (4) Limping (7.8%) (5) Maine cafe ´-au-lait spots [65, 68] (1) A single or multiple, variably sized, sharply marginated radiolucencies within the cortex of the tibia or fibula, with a surrounding sclerotic rim (2) An anterior bowing deformity or pathologic fracture may be observed (3) Soft tissue extension is not present, and intramedullary involvement is unusual (4) A CT scan and MRI are useful for confirming the intracortical location of the lesion [69] (1) OFD-like AD: Like OFD (2) Classic AD and dedifferentiated AD: a) Well-demarcated, lobulated, radiolucent lesion within cortical bone, imparting a “soap bubble” appearance b) Skip lesions and/or multicentric lesions involving the tibia and/or fibula may be present c) May breach the cortex, extending into the medullary cavity or adjacent soft tissues d) A CT scan and MRI are useful for documenting multifocality, cortical destruction, and soft tissue extension [69] (1) The healthy bone is replaced with a more radiolucent, ‘‘ground-glass’’ appearing pattern, with no visible trabecular pattern (2) The periosteal surface is smooth and nonreactive (3) Shepherd’s crook deformity [65] (1) exclusively intracortical lesion with a tan-gray, solid cut surface and a gritty consistency (2) The perioseum is intact, and the surrounding cortical bone is usually sclerotic and thickened (3) Intramedullary involvement is not typically seen [69] (1) Solid, well-demarcated, lobulated lesions, with tan-white cut surfaces (2) Centered within the cortex with variable involvement of the medullary space or extraperiosteal soft tissue [69] (1) A well-circumscribed, tangrey mass that is dense and variably fibrous with a gritty quality (2) May be prominent cyst formation (3) A glassier, blue-tinged appearance may be found in cases with chondroid metaplasia (1) A loose storiform, fibrovascular stroma, and woven bony trabeculae with osteoblastic rimming [70] (2) individual keratin-immunoreactive cells can be detected (1) OFD-like AD: widely scattered, clearly visible small epithelial nests (2) Classic AD: a predominant epithelial component, embedded in an inconspicuous OFD-like bland spindled or fibro-osseous stroma"
- `PMID:26637977` *(abstract only)*: "Loss of the CBL pY1003 docking site in OFD leads to reduced receptor internalization and degradation, stabilizing the MET receptor and conferring a gain-of-function to the protein"
  - closest text in source: "In an additional subject with unilateral OFD, we identified a somatic MET mutation, also affecting exon 14, that substituted a tyrosine residue critical for MET receptor turnover and, as in the case of the MET(Δ14) mutations, had a stabilizing effect on the mature protein"
- `PMID:41746735` *(abstract only)*: "MetΔJMD cells demonstrated delayed ERK pathway normalization after hepatocyte growth factor stimulation"
  - closest text in source: "Inhibition of MAPK signaling with MEK inhibitors restored osteogenic differentiation of mouse MetΔJMD skeletal progenitor cells and promoted the activation of transcriptional signatures associated with skeletal development and osteoblast differentiation in pseudarthrosis-derived primary cells from patients with OFD"
- `PMID:38539216`: "Lesions usually disappear and do not cause problems in adulthood"
  - closest text in source: "Clinical observation is an alternative conservative treatment method for asymptomatic and mildly symptomatic patients, while surgical intervention is usually indicated for larger lesions accompanied by more obvious deformities or functional problems caused by the pathological fracture"
- `PMID:41746735` *(abstract only)*: "Inhibition of MAPK signaling with MEK inhibitors restored osteogenic differentiation of mouse Met^ΔJMD skeletal progenitor cells and promoted the activation of transcriptional signatures associated with skeletal development and osteoblast differentiation in pseudarthrosis-derived primary cells from patients with osteofibrous dysplasia."
  - closest text in source: "Inhibition of MAPK signaling with MEK inhibitors restored osteogenic differentiation of mouse MetΔJMD skeletal progenitor cells and promoted the activation of transcriptional signatures associated with skeletal development and osteoblast differentiation in pseudarthrosis-derived primary cells from patients with OFD"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 29 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 21 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011806` (5 mentions) - the report calls it "MONDO", "Disease"; MONDO calls it **osteofibrous dysplasia**
- `HP:0002979` (2 mentions) - the report calls it "Bowing of the legs", "Phenotype"; HP calls it **Bowing of the legs**
- `HP:0002653` (2 mentions) - the report calls it "Bone pain", "Phenotype"; HP calls it **Bone pain**
- `HP:0002757` (4 mentions) - the report calls it "Recurrent fractures", "cortical thinning", "Phenotype"; HP calls it **Recurrent fractures**
- `HP:0006543` (2 mentions) - the report calls it "Pseudoarthrosis of long bones", "Phenotype"; HP calls it **Cardiorespiratory arrest**
- `GO:0048012` (2 mentions) - the report calls it "hepatocyte growth factor receptor signaling pathway", "Biological process"; GO calls it **hepatocyte growth factor receptor signaling pathway**
- `GO:0000165` (2 mentions) - the report calls it "MAPK cascade", "Biological process"; GO calls it **MAPK cascade**
- `GO:0006511` (2 mentions) - the report calls it "ubiquitin-dependent protein catabolic process", "Biological process"; GO calls it **ubiquitin-dependent protein catabolic process**
- `GO:0001649` (2 mentions) - the report calls it "osteoblast differentiation", "Biological process"; GO calls it **osteoblast differentiation**
- `GO:0030282` (2 mentions) - the report calls it "bone mineralization", "Biological process"; GO calls it **bone mineralization**
- `CL:0000062` (3 mentions) - the report calls it "osteoblast", "Cell type"; CL calls it **osteoblast**
- `CL:0000057` (3 mentions) - the report calls it "fibroblast", "Cell type"; CL calls it **fibroblast**
- `CL:0000092` (2 mentions) - the report calls it "osteoclast", "Cell type"; CL calls it **osteoclast**
- `UBERON:0000979` (2 mentions) - the report calls it "tibia", "Anatomy"; UBERON calls it **tibia**
- `UBERON:0001446` (2 mentions) - the report calls it "fibula", "Anatomy"; UBERON calls it **fibula**
- `UBERON:0002515` (2 mentions) - the report calls it "periosteum", "Anatomy"; UBERON calls it **periosteum**
- `HP:0000006` (2 mentions) - the report calls it "Pattern:** Autosomal dominant", "Phenotype"; HP calls it **Autosomal dominant inheritance**
- `NCIT:C15747` (2 mentions) - the report calls it "Supportive Care", "Treatment"; NCIT calls it **Supportive Care**
- `NCIT:C15329` (2 mentions) - the report calls it "Surgical Procedure", "Treatment"; NCIT calls it **Surgical Procedure**
- `NCIT:C15240` (2 mentions) - the report calls it "Genetic Counseling", "Treatment"; NCIT calls it **Genetic Counseling**
- `GO:0004714` (1 mention) - the report calls it "Molecular function"; GO calls it **transmembrane receptor protein tyrosine kinase activity**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0014065` (obsolete phosphatidylinositol 3-kinase signaling) (1 mention) - replaced by `GO:0043491`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002992` (1 mention) - the report calls it "Abnormality of tibia morphology"; HP calls it **Abnormal tibia morphology**, and lists "Abnormality of tibia morphology" among its other names
- `GO:0014065` (1 mention) - the report calls it "phosphatidylinositol 3-kinase signaling"; GO calls it **obsolete phosphatidylinositol 3-kinase signaling**
- `CL:0007010` (2 mentions) - the report calls it "progenitor cell of endochondral bone", "Cell types:** Periosteal progenitor cells"; CL calls it **preosteoblast**, and lists "osteoprogenitor cell" among its other names
- `NCIT:C15986` (2 mentions) - the report calls it "Pharmacotherapy", "Treatment"; NCIT calls it **Pharmacotherapy**, and lists "Pharmacological Treatment" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0011806` - called "MONDO", "Disease"
- `HP:0002979` - called "Bowing of the legs", "Phenotype"
- `HP:0002653` - called "Bone pain", "Phenotype"
- `HP:0002757` - called "Recurrent fractures", "cortical thinning", "Phenotype"
- `HP:0006543` - called "Pseudoarthrosis of long bones", "Phenotype"
- `GO:0048012` - called "hepatocyte growth factor receptor signaling pathway", "Biological process"
- `GO:0000165` - called "MAPK cascade", "Biological process"
- `GO:0006511` - called "ubiquitin-dependent protein catabolic process", "Biological process"
- `GO:0001649` - called "osteoblast differentiation", "Biological process"
- `GO:0030282` - called "bone mineralization", "Biological process"
- `CL:0000062` - called "osteoblast", "Cell type"
- `CL:0007010` - called "progenitor cell of endochondral bone", "Cell types:** Periosteal progenitor cells"
- `CL:0000057` - called "fibroblast", "Cell type"
- `CL:0000092` - called "osteoclast", "Cell type"
- `UBERON:0000979` - called "tibia", "Anatomy"
- `UBERON:0001446` - called "fibula", "Anatomy"
- `UBERON:0002515` - called "periosteum", "Anatomy"
- `HP:0000006` - called "Pattern:** Autosomal dominant", "Phenotype"
- `NCIT:C15747` - called "Supportive Care", "Treatment"
- `NCIT:C15329` - called "Surgical Procedure", "Treatment"
- `NCIT:C15986` - called "Pharmacotherapy", "Treatment"
- `NCIT:C15240` - called "Genetic Counseling", "Treatment"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.