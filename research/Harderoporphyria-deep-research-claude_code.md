---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-28T17:50:02.505998'
end_time: '2026-08-28T17:55:22.714914'
duration_seconds: 320.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Harderoporphyria
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
  web_search_requests: 15
  num_turns: 28
  total_cost_usd: 1.3341604000000005
  session_id: 40266a89-d5b8-58dd-bcb1-55fbf52a2db7
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 25
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 16
  on_topic: 7
  off_topic: 3
  off_topic_references:
  - PMID:1733615
  - PMID:629747
  - PMID:14633981
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 32
  verified: 29
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 12
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0032263
    reported_labels:
    - Coproporphyrinuria
    ontology_label: Increased blood pressure
  - term_id: UBERON:0001155
    reported_labels:
    - liver
    ontology_label: colon
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0070265
    ontology_label: obsolete necrotic cell death
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Harderoporphyria
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Harderoporphyria** covering all of the
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

# Harderoporphyria: Comprehensive Research Report

## 1. Disease Information

**Overview.** Harderoporphyria (HARPO) is an extremely rare, autosomal recessive, erythropoietic (hematologically dominant) variant of hereditary coproporphyria (HCP). It is caused by biallelic (homozygous or compound heterozygous) pathogenic variants in *CPOX*, the gene encoding coproporphyrinogen oxidase (coproporphyrinogen-III oxidase, CPOX/CPO), the sixth enzyme of the heme biosynthetic pathway. Unlike classic heterozygous HCP — an autosomal dominant acute hepatic porphyria with neurovisceral attacks — harderoporphyria presents in the neonatal period with severe hemolytic anemia, jaundice, hepatosplenomegaly, and cutaneous photosensitivity, and is biochemically defined by massive fecal excretion of the tricarboxylic porphyrin **harderoporphyrin**, an intermediate normally present only in trace amounts ([Wikipedia](https://en.wikipedia.org/wiki/Harderoporphyria); [OMIM #618892](https://omim.org/entry/618892); Nordmann et al. 1983, PMID pending/[JCI](https://www.jci.org/articles/view/111039)).

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (disease) | **#618892** — Harderoporphyria; HARPO |
| OMIM (related, allelic disorder) | #121300 — Coproporphyria, Hereditary (HCP) |
| OMIM (gene) | *612732 — Coproporphyrinogen Oxidase; CPOX |
| Orphanet | **ORPHA:659672** (Harderoporphyria); gene page [Orphanet CPOX](https://www.orpha.net/en/disease/gene/CPOX) |
| MeSH | C562816 |
| SNOMED CT | 238056003 |
| ICD-10-CM | E80.29 (Other porphyria) — no disease-specific code exists; harderoporphyria and HCP are both subsumed under the "other porphyria" E80.2x block ([ICD10Data](https://www.icd10data.com/ICD10CM/Codes/E00-E89/E70-E88/E80-/E80.29)) |
| Gene (HGNC) | CPOX, HGNC:2321, chromosome **3q11.2** (some sources cite 3q12) |
| MONDO | Not yet independently confirmed in this search pass — flag for direct MONDO lookup during curation |

**Synonyms:** Harderoporphyria; Homozygous hereditary coproporphyria (a related but non-identical term, since not all homozygous/biallelic *CPOX* genotypes produce the harderoporphyrin-excess phenotype); erythropoietic variant of hereditary coproporphyria.

**Evidence basis:** All published knowledge derives from **individual case reports and small case series** (fewer than a dozen kindreds described worldwide since 1983) rather than large aggregated cohorts or registries — a defining feature of this ultra-rare disorder that should be reflected in curation confidence levels.

Sources: [Wikipedia: Harderoporphyria](https://en.wikipedia.org/wiki/Harderoporphyria); [OMIM #618892](https://omim.org/entry/618892); [OMIM *612732](https://omim.org/entry/612732); [Orphanet CPOX gene page](https://www.orpha.net/en/disease/gene/CPOX)

---

## 2. Etiology

### 2a. Disease Causal Factors — Genetic
Harderoporphyria is caused **exclusively** by biallelic loss-of-function/altered-function variants in *CPOX*. It is a purely monogenic, enzymopathic disorder — there is no known environmental or infectious primary cause, although environmental porphyrinogenic triggers modulate expressivity (see below).

### 2b. Genetic Risk Factors

- **The defining genotype-phenotype rule**: Missense variants restricted to five amino acid residues encoded by **exon 6, positions D400–K404** of CPOX, when present in the homozygous state or compound heterozygous with a "null" (loss-of-function) allele, produce the harderoporphyria phenotype rather than classic acute HCP. This is described in the literature as **"the first known metabolic disorder in which the clinical expression of disease (acute hepatic vs. erythropoietic) depended on the location and type of mutation within the same gene"** (Schmitt et al. 2005, *Hum Mol Genet* 14:3089–3098; summarized via [OMIM #618892](https://omim.org/entry/618892)).
- **K404E** (c.1210A>G, p.Lys404Glu; rs121917868) is the most recurrently reported harderoporphyria-associated allele: all five patients from three families in the founding literature carried K404E in homozygosity or compound heterozygosity with a null *CPOX* allele. Enzymatic expression studies (K404E mutant CPOX expressed in *E. coli*) showed the Michaelis constant (Km) for the mutant enzyme was ~10-fold higher than wild type, implicating Lys404 in substrate binding, together with reduced catalytic activity and premature release of the harderoporphyrinogen intermediate (search synthesis of Schmitt et al. 2005; [Nordmann et al. 1983, JCI](https://www.jci.org/articles/view/111039)).
- **H327R** — a second, distinct missense variant reported causing harderoporphyria via homozygosity, described in "Harderoporphyria due to homozygosity for coproporphyrinogen oxidase missense mutation H327R" ([PubMed 21103937](https://pubmed.ncbi.nlm.nih.gov/21103937/); also indexed at [Springer/JIMD](https://link.springer.com/article/10.1007/s10545-010-9237-9)).
- A four-amino-acid in-frame deletion in the same D400–K404 hot-region has also been reported, again "a region of the enzyme mutated in 7 of the 8 previously reported cases" of harderoporphyria, in a patient with compound heterozygous *CPOX* mutations and lifelong photosensitivity ([Frank/ScienceDirect case report, PMID 30828546](https://www.sciencedirect.com/science/article/pii/S2214426918301484)).
- **Population frequency of K404E**: reported in gnomAD at an allele frequency of approximately **0.009%**, consistent with extreme rarity of the harderoporphyria phenotype (which requires two hits) even though heterozygous carriers of K404E are essentially asymptomatic HCP carriers.
- **Contrast with typical HCP variants**: heterozygous pathogenic variants distributed across all seven *CPOX* exons cause classic autosomal-dominant HCP with reduced penetrance; missense, nonsense, splice-site, and small deletion/insertion variants are all represented (GeneReviews: [Hereditary Coproporphyria](https://www.ncbi.nlm.nih.gov/books/NBK114807/), citing Lamoril et al. 2001, PMID 11309681, "no genotype-phenotype correlation exists" for classic HCP severity — in contrast to the sharp genotype-phenotype rule that specifically produces harderoporphyria).
- **Consanguinity / homozygosity mechanism**: Because two hits are needed, harderoporphyria arises typically in the setting of (a) parental consanguinity producing true homozygosity for a hot-region allele, or (b) compound heterozygosity for a hot-region missense allele plus an unrelated null allele inherited from the other, typically unaffected or mildly HCP-affected, parent. In the founding Nordmann family, both parents showed only mild biochemical abnormalities (lymphocyte CPOX activity ~50% of normal, consistent with heterozygous HCP carrier status), while the three affected children had lymphocyte CPOX activity reduced to ~10% of control.

### 2c. Environmental / Modifying Risk Factors
As in all hepatic porphyrias, **porphyrinogenic triggers** exacerbate biochemical and clinical expression, although the literature specific to harderoporphyria emphasizes that neither abdominal pain nor neuropsychiatric acute attacks are typically observed in the classic neonatal harderoporphyria presentation (unlike HCP). Recognized triggers relevant to the broader HCP/CPOX-deficiency spectrum (applicable especially to heterozygous relatives and to milder harderoporphyria variants) include:
- Cytochrome P450-inducing/porphyrinogenic drugs (barbiturates, certain anticonvulsants, sulfonamides, estrogens/progestogens)
- Fasting/caloric restriction
- Alcohol
- Intercurrent infection and physiological stress
- Hormonal factors (menstrual cycle, pregnancy) in the classic-HCP spectrum
- **Light exposure**, specifically the Soret-band (~400–410 nm) and near-visible wavelengths that photoactivate accumulated porphyrins in skin and red cells, driving the photosensitivity and hemolysis; avoidance of light <510 nm has been reported to reduce cutaneous manifestations, anemia, and splenomegaly in erythropoietic porphyrias generally.

### 2d. Protective Factors
No specific genetic or environmental protective factors for harderoporphyria are described in the literature; this reflects both its rarity and its being a loss-of-function enzymopathy rather than a susceptibility trait. Reduced penetrance of the underlying heterozygous HCP genotype (documented in classic HCP) is presumed but not specifically quantified for the harderoporphyria compound state.

### 2e. Gene-Environment Interaction
The core gene-environment relationship is that heme-pathway-inducing drugs and metabolic stress amplify hepatic ALAS1 activity and pathway flux through the partially deficient CPOX enzyme, increasing intermediate accumulation (harderoporphyrinogen/harderoporphyrin, coproporphyrinogen) in both hepatic (classic HCP-like) and erythroid (harderoporphyria-specific) compartments; light then photoactivates the accumulated erythroid/cutaneous porphyrins to produce hemolysis and skin damage.

Sources: [OMIM #618892](https://omim.org/entry/618892); [Nordmann et al. 1983](https://www.jci.org/articles/view/111039); [PubMed 21103937](https://pubmed.ncbi.nlm.nih.gov/21103937/); [GeneReviews HCP](https://www.ncbi.nlm.nih.gov/books/NBK114807/); [ScienceDirect case report](https://www.sciencedirect.com/science/article/pii/S2214426918301484)

---

## 3. Phenotypes

| Phenotype | Type | Onset | Frequency/Notes | Suggested HPO term |
|---|---|---|---|---|
| Severe hemolytic anemia | Laboratory abnormality / hematologic sign | Neonatal | Core, near-universal feature across reported cases | HP:0001878 (Hemolytic anemia); consider HP:0004804 (early-onset) qualifier |
| Neonatal jaundice | Clinical sign | Birth / first days of life | Presenting feature in essentially all reported neonates | HP:0000952 (Jaundice) |
| Hepatosplenomegaly | Physical sign | Neonatal/infantile, chronic | Reported consistently, secondary to chronic hemolysis and extramedullary erythropoiesis | HP:0001433 (Hepatosplenomegaly) |
| Cutaneous photosensitivity | Symptom/sign | Can present neonatally or emerge later; described as lifelong in at least one case | Skin fragility/blistering in light-exposed areas, similar to other cutaneous porphyrias | HP:0000992 (Cutaneous photosensitivity) |
| Bullae / skin fragility | Physical sign | Variable | Overlaps with the ~20% of classic HCP patients who develop bullous photosensitivity | HP:0000988 (Skin lesion) / HP:0032169 (bullae, if separately modeled) |
| Elevated erythrocyte protoporphyrin | Laboratory abnormality | Present from neonatal period | Reported increased in erythrocytes in the founding cases | HP:0025230 (or closest available porphyrin-elevation term; verify against enum) |
| Markedly elevated fecal harderoporphyrin | Laboratory abnormality | Present from birth | Pathognomonic biochemical signature — >60% of total fecal porphyrin in affected homozygotes vs. <20% in unaffected/heterozygous carriers | No dedicated HPO term identified; capture as biochemical marker rather than HPO phenotype |
| Elevated urinary coproporphyrin | Laboratory abnormality | Present from birth | Large amount of coproporphyrin found in urine in addition to fecal harderoporphyrin | HP:0032263 (Coproporphyrinuria) if present in enum, else free text |
| Markedly decreased lymphocyte/erythrocyte CPOX activity | Laboratory abnormality | Constitutional | ~10% of normal in affected homozygotes (vs. ~50% in heterozygous HCP carriers/parents) | No direct HPO enzyme-activity term; model as biochemical finding |

**Absence of classic acute HCP features:** A clinically important negative finding repeatedly emphasized in the literature is that **harderoporphyria patients do not exhibit the abdominal pain or neuropsychiatric/neurovisceral attacks** characteristic of classic acute hepatic HCP, distinguishing the erythropoietic/hematologic clinical gestalt of harderoporphyria from its allelic, dominantly inherited counterpart.

**Severity/progression:** Severity is described as variable but generally significant enough to require close neonatal hematologic monitoring; some patients require red cell transfusion support for hemolytic anemia (inferred by analogy with related erythropoietic porphyrias — see Treatment section; direct harderoporphyria-specific transfusion data were not found in this pass and should be verified against the primary case reports before citation).

**Quality of life impact:** Not separately quantified in available literature (no disease-specific EQ-5D/SF-36 data identified); QoL burden can be inferred as substantial in the neonatal/infantile period due to anemia and photosensitivity, but this should be flagged as an evidence gap rather than asserted numerically.

Sources: [Wikipedia: Harderoporphyria](https://en.wikipedia.org/wiki/Harderoporphyria); [Nordmann et al. 1983](https://www.jci.org/articles/view/111039); case-report synthesis of "Neonatal Hemolytic Anemia Due to Inherited Harderoporphyria" ([ASH Blood 91:1453, 1998](https://ashpublications.org/blood/article/91/4/1453/139523/Neonatal-Hemolytic-Anemia-Due-to-Inherited); [PubMed 9454777](https://pubmed.ncbi.nlm.nih.gov/9454777/))

---

## 4. Genetic/Molecular Information

- **Causal gene:** *CPOX* (coproporphyrinogen oxidase), HGNC:2321, OMIM *612732, chromosome 3q11.2 (also cited as 3q12 in some resources — reconcile against Ensembl/NCBI Gene during curation).
- **Protein:** Coproporphyrinogen-III oxidase (CPOX/CPO), a homodimeric, oxygen-dependent mitochondrial intermembrane-space enzyme (EC 1.3.3.3).
- **Enzymatic reaction:** CPOX catalyzes the **sequential oxidative decarboxylation** of the 2- and 4-propionate side chains of coproporphyrinogen III to vinyl groups, producing protoporphyrinogen IX. The reaction proceeds via an obligate **tricarboxylic intermediate, harderoporphyrinogen** (2-vinyl-4,6,7-tripropionate porphyrinogen): the 4-propionate group cannot be attacked until the 2-propionate group has already been decarboxylated. Mechanistic studies suggest both decarboxylations occur at the same active site, which becomes transiently inaccessible after the first decarboxylation, requiring substrate/intermediate rotation before the second decarboxylation can proceed (summarized from enzymology literature, e.g. [PubMed 629747](https://pubmed.ncbi.nlm.nih.gov/629747/); [ScienceDirect topic overview](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/coproporphyrinogen-oxidase)).
- **Structural basis of the harderoporphyria mutations:** Crystal structures of CPOX orthologs (human and yeast Hem13p) show a central seven-stranded antiparallel β-sheet flanked by helices, with a deep, conserved active-site cleft that adopts open and closed conformations via an ~8 Å helix movement upon substrate binding — closing over the substrate to protect the reactive intermediate from inappropriate oxidation and to position it for the second decarboxylation step. Harderoporphyria-associated missense variants (K404E, H327R, and the D400–K404 hot-region deletion) are proposed to destabilize this closed conformation or the substrate-binding geometry specifically at the point where harderoporphyrinogen would normally be retained for its second decarboxylation — causing **premature release of harderoporphyrinogen/harderoporphyrin** rather than complete conversion to protoporphyrinogen IX. This structural hypothesis explains why only this narrow residue window produces the erythropoietic/harderoporphyrin-excess phenotype rather than simple loss of total enzyme activity (synthesis of Schmitt et al. 2005 and CPOX crystallography literature, e.g. [PubMed 14633981](https://pubmed.ncbi.nlm.nih.gov/14633981/); [JBC Hem13p structure](https://www.jbc.org/article/S0021-9258(20)72951-0/fulltext)).
- **Variant classification (ACMG/ClinVar):** K404E (c.1210A>G / rs121917868) is classified **Pathogenic** in ClinVar, with functional/enzymatic data (elevated Km, reduced Vmax) supporting pathogenicity. H327R and the D400–K404 in-frame deletion are reported pathogenic missense/deletion variants specific to harderoporphyria case reports.
- **Zygosity requirement:** Harderoporphyria requires **homozygosity or compound heterozygosity** for a hot-region (D400–K404) missense allele, generally paired with a null (loss-of-function) allele on the other chromosome — i.e., biallelic *CPOX* involvement, contrasted with the single heterozygous hit sufficient for classic dominant HCP.
- **Modifier genes:** None specifically documented for harderoporphyria. In the broader porphyria literature, digenic/oligogenic interactions (e.g., co-inheritance of *CPOX* with *ALAD* or *PPOX* variants) have been described to modulate phenotype severity in HCP generally (GeneReviews, citing Hasegawa et al. 2017, PMID 28349448), but no harderoporphyria-specific digenic modifier has been reported in this search pass.
- **Epigenetics:** No disease-specific epigenetic (DNA methylation/histone) data were identified for harderoporphyria or CPOX deficiency.
- **Chromosomal abnormalities:** None reported; harderoporphyria is caused by point mutations/small indels, not large structural chromosomal rearrangements.
- **Somatic vs. germline:** Exclusively germline; harderoporphyria is a congenital, constitutional Mendelian disorder.

**Suggested ontology terms:** Gene: `hgnc:2321` (CPOX); relevant GO molecular function: `GO:0004109` (coproporphyrinogen oxidase activity); relevant GO biological process: `GO:0006783` (heme biosynthetic process) / `GO:0033013` (tetrapyrrole metabolic process).

Sources: [OMIM *612732](https://omim.org/entry/612732); [GeneReviews HCP](https://www.ncbi.nlm.nih.gov/books/NBK114807/); [ClinVar VCV000000453](https://www.ncbi.nlm.nih.gov/clinvar/variation/453/); [PubMed 14633981](https://pubmed.ncbi.nlm.nih.gov/14633981/)

---

## 5. Environmental Information

Harderoporphyria has no independent environmental, infectious, or lifestyle causal factor — it is a purely monogenic disorder — but disease *expression* is environmentally modulated:

- **Light exposure** is the dominant environmental modifier, driving the cutaneous photosensitivity component and likely contributing to porphyrin-mediated hemolysis via phototoxic damage to circulating erythrocytes carrying excess porphyrin. Avoidance of visible light in the ~400–510 nm range is the mainstay non-pharmacologic intervention across the erythropoietic porphyria spectrum.
- **Porphyrinogenic drugs/xenobiotics** (CYP450 inducers such as certain barbiturates, sulfonamide antibiotics, and hormonal agents) can, by analogy with classic HCP, increase hepatic heme-pathway flux and porphyrin precursor/intermediate accumulation, though harderoporphyria's dominant lesion is erythroid rather than hepatic and direct harderoporphyria-specific drug-trigger case data were not identified in this pass.
- **Fasting/caloric restriction and intercurrent illness** are recognized triggers for acute exacerbation in the broader HCP disease family.
- **No infectious agent** is implicated in pathogenesis.

Sources: General porphyria trigger literature via [GeneReviews HCP](https://www.ncbi.nlm.nih.gov/books/NBK114807/); erythropoietic porphyria light-avoidance data via general erythropoietic protoporphyria/CEP literature ([How I treat EPP/XLP, ASH Blood 141:2921](https://ashpublications.org/blood/article/141/24/2921/494865/How-I-treat-erythropoietic-protoporphyria-and-X))

---

## 6. Mechanism / Pathophysiology

### Causal chain (upstream → downstream)

1. **Molecular trigger (upstream):** Biallelic *CPOX* variants concentrated in exon 6 residues D400–K404 (e.g., K404E, H327R) impair the enzyme's ability to complete the second oxidative decarboxylation step of coproporphyrinogen III metabolism, and/or destabilize the closed, substrate-protective active-site conformation.
2. **Enzymatic consequence:** The reaction stalls after the first decarboxylation, and the intermediate **harderoporphyrinogen is released prematurely** from the active site rather than undergoing the second decarboxylation to protoporphyrinogen IX. Kinetic studies show markedly increased Km (reduced substrate affinity) and reduced Vmax for mutant enzyme.
3. **Biochemical accumulation:** Harderoporphyrinogen (and its oxidized product, harderoporphyrin) plus coproporphyrinogen/coproporphyrin accumulate — disproportionately in the **erythroid compartment**, where high heme-pathway flux during erythropoiesis exposes the partially defective enzyme to saturating substrate concentrations, in contrast to the lower flux in hepatocytes of classic (heterozygous) HCP. This tissue-specific flux difference is the proposed mechanistic explanation for why the harderoporphyria genotype manifests primarily as an erythropoietic/hematologic disease rather than a hepatic/neurovisceral one.
4. **Cellular consequence — hemolysis:** Accumulated porphyrins in developing and circulating erythrocytes are photoreactive; upon light exposure they generate reactive oxygen species that damage the erythrocyte membrane, producing chronic hemolysis, jaundice, and compensatory extramedullary erythropoiesis (hepatosplenomegaly).
5. **Cellular/tissue consequence — cutaneous photosensitivity:** The same photoactivation mechanism operating in dermal capillaries and skin-resident porphyrin deposits produces the light-triggered skin fragility/blistering phenotype, analogous to (but biochemically distinct from) other cutaneous porphyrias such as congenital erythropoietic porphyria and erythropoietic protoporphyria.
6. **Organismal outcome:** Chronic hemolytic anemia with neonatal jaundice, hepatosplenomegaly from extramedullary hematopoiesis and reticuloendothelial porphyrin/hemolysis burden, and lifelong photosensitivity, generally **without** the acute neurovisceral (abdominal pain, neuropathy, psychiatric) attacks that define classic hepatic HCP — reflecting the relatively preserved hepatic ALA/PBG handling in harderoporphyria compared to the erythroid-dominant porphyrin burden.

### Molecular pathway
Heme biosynthesis (KEGG hsa00860 / Reactome heme biosynthesis pathway): Glycine + succinyl-CoA → ALA (ALAS1/ALAS2) → PBG (ALAD) → hydroxymethylbilane (HMBS) → uroporphyrinogen III (UROS) → coproporphyrinogen III (UROD) → **[CPOX, defective step]** → protoporphyrinogen IX → protoporphyrin IX (PPOX) → heme (FECH, with iron insertion).

### Cell types and tissues involved
- Erythroid precursors / developing erythrocytes (primary site of pathological porphyrin accumulation) — consider CL:0000038 (erythroid progenitor cell) / CL:0000232 (erythrocyte)
- Hepatocytes (secondary/lesser contribution relative to classic HCP) — UBERON:0001155 liver structures
- Reticuloendothelial system / spleen macrophages (hemolysis clearance, splenomegaly) — UBERON:0002106 spleen
- Skin (keratinocytes, dermal vasculature) — site of phototoxic injury — UBERON:0002097 skin

### Suggested GO terms
- GO:0004109 coproporphyrinogen oxidase activity (molecular function, defective)
- GO:0006783 heme biosynthetic process (biological process, disrupted)
- GO:0006979 response to oxidative stress (downstream, in phototoxic hemolysis)
- GO:0006915 apoptotic process / GO:0070265 necrotic cell death (candidate downstream erythrocyte injury processes, not yet specifically documented for harderoporphyria)

### Omics / advanced technologies
No transcriptomic, proteomic, metabolomic, single-cell, or spatial data specific to harderoporphyria patients or models were identified in this search — an evidence gap typical of an ultra-rare Mendelian disease with fewer than a dozen published cases. Metabolomic characterization is effectively limited to targeted porphyrin fractionation (fecal harderoporphyrin, urinary coproporphyrin, erythrocyte protoporphyrin) reported in the founding case series.

Sources: [Nordmann et al. 1983](https://www.jci.org/articles/view/111039); Schmitt et al. 2005 (*Hum Mol Genet* 14:3089–3098, summarized via [OMIM #618892](https://omim.org/entry/618892)); [PubMed 629747](https://pubmed.ncbi.nlm.nih.gov/629747/) (decarboxylation sequence mechanism); [PubMed 14633981](https://pubmed.ncbi.nlm.nih.gov/14633981/) (crystal structure)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Bone marrow/erythroid tissue (site of porphyrin overproduction), skin (photosensitivity), liver and spleen (secondary — hepatosplenomegaly from hemolysis and extramedullary erythropoiesis)
- **Secondary/complications:** Biliary system (increased bilirubin turnover from hemolysis); potential iron-overload target organs if chronic transfusion is required (liver, heart, endocrine organs) — inferred from general chronic-hemolysis/transfusion management principles, not harderoporphyria-specific data
- **Body systems:** Hematologic/hematopoietic system (primary); integumentary system (photosensitivity); hepatobiliary system (secondary)

**Tissue and cell level:**
- Erythroid lineage cells (proerythroblasts through mature erythrocytes) — CL:0000765 (erythroblast), CL:0000232 (erythrocyte)
- Hepatocytes — CL:0000182
- Splenic reticuloendothelial macrophages — CL:0000235 (macrophage)
- Epidermal keratinocytes and dermal microvasculature (photosensitivity target) — CL:0000312 (keratinocyte)

**Subcellular level:**
- Mitochondria — CPOX is localized to the mitochondrial intermembrane space, where the terminal three steps of heme synthesis (CPOX, PPOX, FECH) occur; GO Cellular Component: GO:0005758 (mitochondrial intermembrane space)
- Cytosol — earlier heme pathway steps (ALAD through UROD) occur in the cytosol before substrate re-enters mitochondria for the CPOX step

**Localization:** Systemic/hematologic (not focal); cutaneous manifestations are typically distributed over light-exposed skin (face, dorsal hands), consistent with other photosensitive porphyrias — bilateral, light-exposure-dependent rather than laterality-defined.

Suggested UBERON terms: UBERON:0002371 (bone marrow), UBERON:0000178 (blood), UBERON:0002097 (skin), UBERON:0002106 (spleen), UBERON:0001155 (liver).

---

## 8. Temporal Development

- **Onset:** Congenital/neonatal. The hallmark presentation across essentially all reported cases is severe jaundice and hemolytic anemia **at birth or within the first days of life**. Photosensitivity may be present from early infancy or, in at least one reported case, persist as "lifelong photosensitivity" into adulthood.
- **Onset pattern:** Acute at birth (hemolytic/jaundice component), with a chronic, persistent course thereafter for the photosensitivity and biochemical porphyrin-excess phenotype.
- **Progression/course:** Described as a chronic, lifelong biochemical abnormality (elevated harderoporphyrin/coproporphyrin excretion, reduced CPOX activity) with a hematologic component that may stabilize after the neonatal period but with persistent photosensitivity. No formal staging system exists for this disease given its rarity.
- **Progression rate:** Not systematically quantified across a cohort; case reports describe chronic hemolytic anemia as an ongoing feature beyond the neonatal period rather than a self-limited neonatal event alone.
- **Remission patterns:** Not established; no natural-history or registry data were identified describing spontaneous remission.
- **Critical periods:** The neonatal period is clinically critical both for diagnosis (distinguishing harderoporphyria from other causes of neonatal hemolytic anemia and jaundice, e.g., thalassemia, hemolytic disease of the newborn, G6PD deficiency, other porphyrias) and for management of hyperbilirubinemia risk (kernicterus).

Sources: [Nordmann et al. 1983](https://www.jci.org/articles/view/111039); [ASH Blood 91:1453 (1998)](https://ashpublications.org/blood/article/91/4/1453/139523/Neonatal-Hemolytic-Anemia-Due-to-Inherited); [ScienceDirect lifelong photosensitivity case](https://www.sciencedirect.com/science/article/pii/S2214426918301484)

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (biallelic *CPOX* variants), in contrast to the autosomal dominant, reduced-penetrance inheritance of classic HCP caused by heterozygous *CPOX* variants. This makes CPOX one of relatively few genes in which **different zygosity states produce clinically and biochemically distinct named disorders** in the same locus.
- **Penetrance:** Full/high penetrance is implied for the harderoporphyria neonatal phenotype in the reported cases (all documented biallelic D400–K404-region carriers presented with disease), though the very small number of published cases limits confident penetrance estimation. By contrast, heterozygous HCP (the "carrier" state in most harderoporphyria kindreds) shows well-documented **reduced penetrance** (GeneReviews, citing Whatley et al. 2009, PMID 19460837, and Blake et al. 1992, PMID 1733615).
- **Expressivity:** Variable within the erythropoietic/hepatic spectrum depending on exact genotype (D400–K404 hot-region variant vs. variants elsewhere in the gene), which is the central genotype-phenotype finding of this disease.
- **Genetic anticipation:** Not applicable — harderoporphyria is not a repeat-expansion disorder.
- **Germline mosaicism:** Not specifically reported for CPOX/harderoporphyria in this search pass.
- **Founder effects:** Not documented for harderoporphyria specifically; K404E and H327R have each been reported in only a small number of unrelated families, insufficient to establish founder-population data confidently.
- **Consanguinity:** Plausible risk-elevating factor for true homozygosity (as opposed to compound heterozygosity) given the rarity of individual pathogenic alleles, though the founding Nordmann family history was not explicitly confirmed as consanguineous in the retrieved summary — verify against primary source before asserting in curation.
- **Carrier frequency:** Not independently established for harderoporphyria; heterozygous HCP carrier frequency (from which harderoporphyria compound heterozygotes/homozygotes arise) is not precisely quantified in general population; K404E allele frequency itself is approximately 0.009% in gnomAD.

**Population demographics:**
- **Prevalence:** Harderoporphyria is described in the literature as having **"fewer than 10 cases reported worldwide"**, making formal prevalence/incidence estimation essentially impossible; it is likely underdiagnosed given its atypical (non-classic-porphyria) presentation as neonatal hemolytic anemia, which is more commonly worked up for thalassemia, hemolytic disease of the newborn, or red cell enzymopathies before porphyria is considered.
- **Geographic distribution:** No specific endemic region identified; reported cases span multiple, geographically dispersed families (originally described in a French kindred by Nordmann et al.).
- **Sex ratio:** No sex predilection has been reported for harderoporphyria itself (autosomal recessive, non-sex-linked); note this contrasts with classic HCP, where clinical attacks (in the general HCP/AIP acute-porphyria literature) are more frequent in women due to hormonal triggers, but this hormonal-attack pattern is not the dominant harderoporphyria presentation.
- **Age distribution:** Neonatal/infantile predominance at diagnosis, given the characteristic presentation.

Sources: [Wikipedia: Harderoporphyria](https://en.wikipedia.org/wiki/Harderoporphyria); [OMIM #618892](https://omim.org/entry/618892); [GeneReviews HCP](https://www.ncbi.nlm.nih.gov/books/NBK114807/)

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Fecal porphyrin fractionation** — the key diagnostic test: demonstration that **harderoporphyrin constitutes the majority (>60%) of total fecal porphyrin**, versus <20% in unaffected individuals and heterozygous HCP carriers. This is the biochemical signature that distinguishes harderoporphyria from classic HCP (where COPRO >> PROTO with 60–95% coproporphyrin isomer-III predominance, but without harderoporphyrin excess).
- **Urinary porphyrin analysis** — elevated coproporphyrin excretion.
- **Erythrocyte protoporphyrin** — elevated, reflecting the erythroid-dominant lesion.
- **Lymphocyte/erythrocyte coproporphyrinogen oxidase enzyme activity assay** — markedly reduced (~10% of normal) in affected homozygotes/compound heterozygotes vs. ~50% in heterozygous HCP carriers (parents); this quantitative distinction supports zygosity inference even before molecular confirmation.
- **Urinary porphobilinogen (PBG) and ALA** — the classic marker for acute hepatic porphyria attacks (elevated in acute HCP attacks); relevant for excluding/assessing an acute hepatic component, though harderoporphyria itself is not characterized by the acute neurovisceral attacks that make PBG the primary diagnostic marker in classic HCP.
- **Complete blood count, reticulocyte count, bilirubin (direct/indirect), haptoglobin, LDH** — standard hemolysis work-up, essential to the differential diagnosis of neonatal hemolytic anemia.

**Genetic testing:**
- **CPOX sequence analysis (single-gene test or targeted porphyria gene panel)** is the definitive diagnostic approach, given that sequence analysis detects ~97% of pathogenic *CPOX* variants (GeneReviews); deletion/duplication analysis captures additional cases not found by sequencing alone.
- **Targeted variant testing** for known harderoporphyria hot-region alleles (K404E, H327R) can be used once family segregation is suspected.
- Whole exome/genome sequencing is a reasonable approach in an undiagnosed neonate with hemolytic anemia of unclear etiology, particularly when initial hemoglobinopathy/enzymopathy work-up is unrevealing.

**Imaging:** Not disease-specific; abdominal ultrasound may document hepatosplenomegaly as part of the general hemolysis work-up.

**Biopsy/histopathology:** Not a primary diagnostic modality for harderoporphyria; no disease-specific histopathological signature was identified in this search.

**Differential diagnosis** (drawing on the neonatal hemolytic anemia and porphyria literatures):
- Thalassemia syndromes and other hemoglobinopathies
- Hemolytic disease of the newborn (Rh/ABO incompatibility)
- Red cell membrane and enzyme defects (hereditary spherocytosis, G6PD deficiency, pyruvate kinase deficiency)
- Congenital erythropoietic porphyria (Günther disease) — also presents with neonatal hemolysis and severe photosensitivity, but distinguished biochemically by uroporphyrin/coproporphyrin I isomer excess rather than harderoporphyrin
- Classic (heterozygous) hereditary coproporphyria and other acute hepatic porphyrias (variegate porphyria, acute intermittent porphyria) — distinguished by absence of the acute neurovisceral attack pattern and by the specific harderoporphyrin excess
- Neonatal-onset hereditary coproporphyria (a related but distinct entity reported with massive coproporphyrin elevation, cutaneous blistering, and hemolytic anemia without harderoporphyrin predominance — see [PMC5740044](https://pmc.ncbi.nlm.nih.gov/articles/PMC5740044/))

**Screening:** No population-based or newborn screening program exists for harderoporphyria given its extreme rarity; diagnosis relies on clinical suspicion in a neonate with unexplained hemolytic anemia plus family history of CPOX mutations/HCP, followed by targeted biochemical and molecular testing. Cascade/carrier testing in relatives of an index case is appropriate once a pathogenic variant is identified, consistent with general recessive-disorder genetic counseling practice.

Sources: [Nordmann et al. 1983](https://www.jci.org/articles/view/111039); [GeneReviews HCP](https://www.ncbi.nlm.nih.gov/books/NBK114807/); [PMC5740044](https://pmc.ncbi.nlm.nih.gov/articles/PMC5740044/)

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No formal survival statistics exist given the extremely small number of reported cases; the disease is not generally described as immediately life-threatening if recognized and supported through the neonatal period, though severe unrecognized neonatal hyperbilirubinemia/hemolysis in any etiology carries a risk of kernicterus if untreated.
- **Morbidity:** Chronic hemolytic anemia and lifelong photosensitivity represent the principal ongoing morbidity; hepatosplenomegaly from chronic hemolysis/extramedullary hematopoiesis is a secondary morbidity.
- **Complications:** By analogy with other chronic hemolytic/porphyric conditions — risk of gallstones (pigment stones from chronic hemolysis), potential need for chronic transfusion with associated iron-overload risk if severe, and skin damage/scarring from recurrent phototoxic injury. These are inferred from general hemolytic-anemia and erythropoietic-porphyria management literature rather than harderoporphyria-specific outcome data, and should be flagged as extrapolated rather than directly evidenced.
- **Recovery potential:** Case reports describe long-term survival with supportive management (implied by case reports following patients into later childhood/adulthood, e.g., the "lifelong photosensitivity" case), suggesting a chronic but non-fatal natural history when appropriately managed, though this is based on a handful of published cases rather than systematic outcome data.
- **Prognostic factors:** Not systematically studied; presumably genotype (which specific hot-region variant, and whether compound heterozygous with a null allele vs. true homozygous) and degree of residual CPOX activity influence severity, mirroring the genotype-driven mechanism that defines the disease category itself.

**Evidence gap note:** This section is the weakest-evidenced area in the literature for this disease; curators should represent prognosis claims with appropriately hedged confidence given the case-report-only evidence base.

---

## 12. Treatment

No disease-specific, evidence-based treatment guideline or clinical trial exists for harderoporphyria (consistent with its status as an ultra-rare, case-report-only disease). Management is supportive and extrapolated from general practice in erythropoietic/hemolytic porphyrias and neonatal hemolytic anemia:

**Supportive/symptomatic care:**
- **Photoprotection** — strict avoidance of sunlight/blue-violet light (<510 nm), protective clothing, opaque/broad-spectrum sunscreens, window-glass filtering — mainstay for the cutaneous photosensitivity and porphyrin-driven hemolysis component, by direct analogy with erythropoietic protoporphyria and congenital erythropoietic porphyria management (NCIT candidate: NCIT:C15747 Supportive Care; behavioral/lifestyle modality).
- **Management of neonatal hyperbilirubinemia** — standard phototherapy/exchange transfusion protocols as clinically indicated for jaundice, with the caveat that porphyria-associated photosensitivity requires careful wavelength selection to avoid worsening porphyrin photoactivation (a clinically important nuance versus standard neonatal jaundice phototherapy).
- **Red blood cell transfusion** — supportive management of severe/symptomatic hemolytic anemia, as used across erythropoietic porphyrias generally to correct anemia and, at higher chronic-transfusion intensity, to suppress endogenous erythropoiesis and thereby reduce porphyrin overproduction — though this carries iron-overload risk requiring chelation if used chronically. Direct harderoporphyria-specific transfusion-dependency data were not confirmed in this search pass.
- **Splenectomy** — reported as "variably successful" for hemolysis/hypersplenism in erythropoietic porphyrias broadly; no harderoporphyria-specific outcome data identified.
- **Avoidance of porphyrinogenic drug triggers** (barbiturates, certain sulfonamides, other CYP450 inducers) — standard precaution extrapolated from HCP/acute-porphyria management, applicable to the hepatic/coproporphyrin component of the disease.
- **Genetic counseling** — for parents/family members given autosomal recessive inheritance, including carrier testing of relatives and reproductive counseling (NCIT:C15240 Genetic Counseling).

**Pharmacotherapy (extrapolated from HCP, not harderoporphyria-specific):**
- **Hematin/hemin (Panhematin)** — the standard treatment for acute attacks in classic HCP, given intravenously to suppress hepatic ALAS1 via negative feedback; relevant primarily if a harderoporphyria patient develops a superimposed acute hepatic-type attack, though this is not the typical harderoporphyria clinical pattern (NCIT:C15986 Pharmacotherapy; therapeutic_agent consideration: hemin, CHEBI-bindable).
- **Givosiran** (an ALAS1-directed siRNA, FDA-approved 2019 for recurrent acute hepatic porphyria attacks) — approved for classic acute hepatic porphyrias including HCP with ≥4 attacks/year; **not established for harderoporphyria**, whose clinical pattern is erythropoietic/hemolytic rather than acute-attack-driven, so applicability is speculative rather than evidenced (therapeutic_modality candidate: SIRNA; NCIT term to be verified).
- **Intravenous glucose/carbohydrate loading** — standard adjunct during any acute hepatic-type exacerbation, by suppressing ALAS1 induction.

**Experimental/investigational:** No harderoporphyria-specific clinical trials (NCT-registered) were identified in this search. Curators should check ClinicalTrials.gov directly for any porphyria-basket trials that might include biallelic CPOX-deficiency patients before asserting a negative.

**Curative options:** No curative therapy (e.g., gene therapy, hematopoietic stem cell transplantation) has been reported for harderoporphyria specifically, though HSCT is the established curative approach for the mechanistically related congenital erythropoietic porphyria, and could be a reasonable extrapolated future direction worth flagging as a knowledge gap rather than an established treatment.

Sources: [GeneReviews HCP](https://www.ncbi.nlm.nih.gov/books/NBK114807/) (hematin/givosiran management of classic HCP attacks); general erythropoietic-porphyria management literature ([ASH Blood 141:2921, How I treat EPP/XLP](https://ashpublications.org/blood/article/141/24/2921/494865/How-I-treat-erythropoietic-protoporphyria-and-X); [PMC10170564, CEP management](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10170564/))

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (Mendelian recessive genetic disorder); the closest analog is **preconception/prenatal genetic counseling and carrier screening** in families with a known harderoporphyria proband or CPOX pathogenic variant, given the autosomal recessive inheritance and identifiable causal alleles.
- **Secondary prevention:** Early recognition of neonatal hemolytic anemia/jaundice with appropriate porphyrin work-up in at-risk families (known CPOX carrier parents) could enable earlier diagnosis and photoprotective/supportive intervention, though no formal newborn screening protocol exists.
- **Tertiary prevention:** Trigger avoidance (light exposure, porphyrinogenic drugs, fasting) to reduce the frequency/severity of hemolytic and cutaneous exacerbations in a diagnosed patient — standard practice extrapolated from the broader porphyria management literature.
- **Genetic counseling:** Recommended for parents of an affected child (both obligate heterozygous HCP carriers) regarding 25% recurrence risk in future pregnancies (autosomal recessive), and for extended family members regarding carrier status and reproductive risk, especially relevant in consanguineous kindreds.
- **Prenatal/preimplantation testing:** Feasible in principle once the familial CPOX variants are known (standard molecular prenatal diagnosis/PGD approach for a known biallelic Mendelian disorder), though no harderoporphyria-specific prenatal diagnosis case was identified in this search.
- **Public health measures:** Not applicable — this is not an environmentally or infectiously mediated disease amenable to population-level public health intervention.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring harderoporphyria (biallelic CPOX hot-region variant) has been reported in a non-human species in this search pass.
- **Related naturally occurring CPOX-deficiency phenotype — the Nakano mouse cataract model:** A hypomorphic *Cpox* mutation was identified as the cause of hereditary cataract in the classic **Nakano (nctam) mouse** strain, an unexpected connection between a heme-pathway enzyme defect and lens cataractogenesis (PMID 23631845), distinct from — but genetically related to — the human harderoporphyria/HCP disease spectrum via the same gene.
- **BALB.NCT-Cpox^nct mouse model of hereditary coproporphyria:** Derived from the Nakano cataract allele backcrossed onto BALB/c, this mouse is **homozygous for a p.R380L CPOX substitution** retaining only ~15% of wild-type enzyme activity. It shows drastically increased blood and hepatic coproporphyrin from a young age, excessive urinary coproporphyrin and porphyrin-precursor excretion, neuromuscular symptoms, and (in female mice specifically) hypertension — recapitulating features of human HCP. This is described as filling a prior gap, since **no prior animal model had jointly reproduced the causal gene mutation, reduced CPOX enzyme activity, porphyrin accumulation, and clinical symptoms of HCP** together ([PMC10036863](https://ncbi.nlm.nih.gov/pmc/articles/PMC10036863); [PubMed 36967721](https://pubmed.ncbi.nlm.nih.gov/36967721/)). Because this model is homozygous (not restricted to the D400–K404 hot region) it is best characterized as an HCP model rather than a harderoporphyria-specific (harderoporphyrin-excess) model — an important nuance for curation, since it does not reproduce the disease-defining harderoporphyrin-predominant biochemical signature.
- **ENU mutagenesis mouse model of HCP:** A separate ENU-induced mouse model of hereditary coproporphyria has also been reported (PMID 28600349), independent of the Nakano-derived strain, further supporting Cpox-deficient mice as a tractable system for studying HCP-spectrum biology, again without specific confirmation of harderoporphyrin-predominant biochemistry.
- **Comparative biology:** The heme biosynthetic pathway, including CPOX, is highly conserved from yeast (*Saccharomyces cerevisiae* Hem13p, whose crystal structure has informed human CPOX active-site models) through mammals, supporting cross-species mechanistic inference, though no species other than mouse (via the two models above) has a documented naturally occurring or induced Cpox-deficiency phenotype relevant to this KB.
- **Zoonotic potential / transmission:** Not applicable — harderoporphyria is a non-communicable, purely genetic disorder.

Sources: [PMC10036863 / BALB.NCT-Cpoxnct model](https://ncbi.nlm.nih.gov/pmc/articles/PMC10036863); [PubMed 23631845, Nakano cataract Cpox mutation](https://pubmed.ncbi.nlm.nih.gov/23631845/); [PubMed 28600349, ENU mutagenesis HCP mouse model](https://pubmed.ncbi.nlm.nih.gov/28600349/)

---

## 15. Model Organisms

| Model | Species | Genotype | Fidelity to human disease | Key findings | Reference |
|---|---|---|---|---|---|
| BALB.NCT-Cpox^nct | Mouse (*Mus musculus*, BALB/c background) | Homozygous p.R380L *Cpox* hypomorphic missense (G→T substitution), ~15% residual enzyme activity | **Recapitulates classic HCP** (elevated blood/liver coproporphyrin, urinary coproporphyrin and precursor excretion, neuromuscular symptoms, sex-specific hypertension in females) — does **not** specifically model the harderoporphyrin-predominant biochemistry that defines harderoporphyria, since the R380L substitution lies outside the human D400–K404 hot region | First mouse model to jointly reproduce causal gene defect, reduced enzyme activity, porphyrin accumulation, and clinical HCP-like symptoms | [PMC10036863](https://ncbi.nlm.nih.gov/pmc/articles/PMC10036863); [PubMed 36967721](https://pubmed.ncbi.nlm.nih.gov/36967721/) |
| Nakano (nctam) cataract mouse | Mouse | Hypomorphic *Cpox* mutation (progenitor strain for BALB.NCT-Cpox^nct) | Originally characterized for a cataract phenotype, not primarily a porphyria model | Established the cataract–CPOX genetic link that led to the HCP mouse model above | [PubMed 23631845](https://pubmed.ncbi.nlm.nih.gov/23631845/) |
| ENU-mutagenesis Cpox mouse | Mouse | ENU-induced *Cpox* variant | HCP-like phenotype from forward-genetics screen | Independent confirmation that murine Cpox loss-of-function reproduces coproporphyria-relevant biology | [PubMed 28600349](https://pubmed.ncbi.nlm.nih.gov/28600349/) |
| *E. coli* recombinant expression system | Bacterial (in vitro/computational biochemistry) | Human CPOX cDNA (wild-type and K404E mutant) expressed heterologously | Not a whole-organism disease model, but the definitive functional evidence establishing K404E pathogenicity | Demonstrated ~10-fold increased Km and reduced activity for K404E vs. wild-type CPOX, directly linking the mutation to defective substrate binding | Schmitt et al. 2005, *Hum Mol Genet* 14:3089–3098 (via [OMIM #618892](https://omim.org/entry/618892)) |

**Key gap:** No published mouse (or other organism) model specifically carries a homozygous or compound-heterozygous D400–K404-region variant reproducing the harderoporphyrin-excess, erythropoietic-dominant human harderoporphyria phenotype — all current murine CPOX-deficiency models more closely recapitulate classic hepatic HCP biochemistry. This represents a genuine modeling gap worth flagging explicitly in a `HUMAN_MODEL_MISMATCH`-type knowledge-gap annotation if this disease is curated into the dismech KB, since existing Cpox-mutant mice are informative for the broader CPOX-deficiency mechanism but do not validate the specific structural/kinetic hypothesis (premature harderoporphyrinogen release) proposed for the D400–K404 hot-region human variants.

Sources: as cited per row above.

---

## Summary of Key Evidence Gaps for Curation

1. **Prognosis/outcome data** are essentially absent beyond individual case follow-up — no survival statistics, no quality-of-life instruments applied.
2. **No harderoporphyria-specific treatment trial or guideline exists**; all therapeutic recommendations are extrapolated from classic HCP or other erythropoietic porphyrias and should be curated with appropriately qualified evidence_source/confidence.
3. **No animal model precisely recapitulates the harderoporphyrin-excess biochemical signature** that defines this disease as distinct from ordinary homozygous HCP — existing Cpox-mutant mice model the broader HCP phenotype.
4. **MONDO ID was not independently confirmed** in this research pass and should be verified directly (e.g., via MONDO/OLS lookup) before curation.
5. **Transfusion-dependency, splenectomy outcomes, and QoL data specific to harderoporphyria patients** were not confirmed in primary sources during this pass — the supportive-care recommendations above are extrapolated from related erythropoietic porphyrias and should be flagged as such, or verified against the primary case reports (Nordmann 1983; Lamoril et al. 1998, *Blood* 91:1453; the H327R case report, PMID 21103937; and the compound-heterozygous lifelong-photosensitivity case report, PMID 30828546) before being asserted as harderoporphyria-specific findings with full confidence.

---

### Sources (consolidated)

- [Harderoporphyria — Wikipedia](https://en.wikipedia.org/wiki/Harderoporphyria)
- [OMIM #618892 — Harderoporphyria; HARPO](https://omim.org/entry/618892)
- [OMIM #121300 — Coproporphyria, Hereditary; HCP](https://omim.org/entry/121300)
- [OMIM *612732 — Coproporphyrinogen Oxidase; CPOX](https://omim.org/entry/612732)
- [Orphanet — CPOX-coproporphyrinogen oxidase](https://www.orpha.net/en/disease/gene/CPOX)
- [Nordmann Y, et al. Harderoporphyria: a variant hereditary coproporphyria. J Clin Invest. 1983](https://www.jci.org/articles/view/111039)
- [Lamoril J, et al. Neonatal hemolytic anemia due to inherited harderoporphyria: clinical characteristics and molecular basis. Blood. 1998;91(4):1453](https://ashpublications.org/blood/article/91/4/1453/139523/Neonatal-Hemolytic-Anemia-Due-to-Inherited) / [PubMed 9454777](https://pubmed.ncbi.nlm.nih.gov/9454777/)
- [Harderoporphyria due to homozygosity for CPOX missense mutation H327R — PubMed 21103937](https://pubmed.ncbi.nlm.nih.gov/21103937/)
- [Harderoporphyria: case of lifelong photosensitivity with compound heterozygous CPOX mutations — ScienceDirect / PubMed 30828546](https://www.sciencedirect.com/science/article/pii/S2214426918301484)
- [Neonatal-Onset Hereditary Coproporphyria: A New Variant of HCP — PMC5740044](https://pmc.ncbi.nlm.nih.gov/articles/PMC5740044/)
- [Hereditary Coproporphyria — GeneReviews®, NCBI Bookshelf NBK114807](https://www.ncbi.nlm.nih.gov/books/NBK114807/)
- [ClinVar Variation 453 (K404E)](https://www.ncbi.nlm.nih.gov/clinvar/variation/453/)
- [BALB.NCT-Cpoxnct is a unique mouse model of hereditary coproporphyria — PMC10036863](https://ncbi.nlm.nih.gov/pmc/articles/PMC10036863) / [PubMed 36967721](https://pubmed.ncbi.nlm.nih.gov/36967721/)
- [Hereditary cataract of the Nakano mouse: hypomorphic Cpox mutation — PubMed 23631845](https://pubmed.ncbi.nlm.nih.gov/23631845/)
- [A mouse model of hereditary coproporphyria from ENU mutagenesis screen — PubMed 28600349](https://pubmed.ncbi.nlm.nih.gov/28600349/)
- [Crystal structure of coproporphyrinogen III oxidase — PubMed 14633981](https://pubmed.ncbi.nlm.nih.gov/14633981/)
- [Crystal structure of the oxygen-dependent CPOX (Hem13p) of S. cerevisiae — JBC](https://www.jbc.org/article/S0021-9258(20)72951-0/fulltext)
- [Factors determining sequence of oxidative decarboxylation by CPOX — PubMed 629747](https://pubmed.ncbi.nlm.nih.gov/629747/)
- [ICD-10-CM E80.29 — Other porphyria](https://www.icd10data.com/ICD10CM/Codes/E00-E89/E70-E88/E80-/E80.29)
- [How I treat erythropoietic protoporphyria and X-linked protoporphyria — ASH Blood 141:2921](https://ashpublications.org/blood/article/141/24/2921/494865/How-I-treat-erythropoietic-protoporphyria-and-X)
- [Very Early Diagnosis and Management of Congenital Erythropoietic Porphyria — PMC10170564](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10170564/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 7 |
| Off topic | 3 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:1733615` (1 mention) - Fecal coproporphyrin isomers in hereditary coproporphyria.
  - shared terms: porphyrin
- `PMID:629747` (4 mentions) - Factors determining the sequence of oxidative decarboxylation of the 2- and 4-propionate substituents of coproporphyrinogen III by coproporphyrinogen oxidase in rat liver.
  - shared terms: none
- `PMID:14633981` (5 mentions) - Crystal structure of coproporphyrinogen III oxidase reveals cofactor geometry of Radical SAM enzymes.
  - shared terms: none

Weighed against this report's own most characteristic terms: `harderoporphyria`, `hcp`, `cpox`, `classic`, `disease`, `porphyrin`, `variant`, `erythropoietic`, `photosensitivity`, `heterozygous`, `hepatic`, `neonatal`, `anemia`, `hemolysis`, `hemolytic`, `porphyria`, `phenotype`, `activity`, `genetic`, `harderoporphyria-specific`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032263` (1 mention) - the report calls it "Coproporphyrinuria"; HP calls it **Increased blood pressure**
- `UBERON:0001155` (2 mentions) - the report calls it "liver"; UBERON calls it **colon**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002097` (2 mentions) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.