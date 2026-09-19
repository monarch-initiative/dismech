---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-18T03:04:29.476614'
end_time: '2026-09-18T03:08:40.914128'
duration_seconds: 251.44
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mast Cell Activation Syndrome
  mondo_id: MONDO:0100004
  category: Complex
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
  web_search_requests: 20
  num_turns: 25
  total_cost_usd: 1.4675869000000001
  session_id: c3b3f1c9-a24d-5e2f-85c1-b82995c77b75
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 47
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:38851398
  relevance_assessed: 27
  on_topic: 23
  off_topic: 1
  off_topic_references:
  - PMID:27571382
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 6
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0001060
    reported_labels:
    - basophil, for comparison
    ontology_label: hematopoietic oligopotent progenitor cell, lineage-negative
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mast Cell Activation Syndrome
- **MONDO ID:** MONDO:0100004 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Mast Cell Activation Syndrome** covering all of the
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

# Mast Cell Activation Syndrome (MCAS): Comprehensive Research Report

## 1. Disease Information

**Overview.** Mast cell activation syndrome (MCAS) is a clinical entity in which mast cells throughout the body release excessive and/or aberrant quantities of mediators (histamine, tryptase, prostaglandin D2, leukotrienes, heparin, and cytokines) in response to a wide range of physical, chemical, immunologic, and psychological triggers, producing recurrent, episodic, multisystem symptoms — without the mast-cell proliferation seen in mastocytosis (in most cases) [(PubMed)](https://pubmed.ncbi.nlm.nih.gov/23179866/). As the 2024 JACI review states: "Mast cell activation syndrome is a term applied to several clinical entities that have gained increased attention from patients and medical providers... there are many gaps in knowledge, resulting in confusion about this clinical syndrome. Whether MCAS is a primary syndrome or exists as a constellation of symptoms in the context of known inflammatory, allergic, or clonal disorders associated with systemic mast cell activation is not well understood" (Castells et al., *J Allergy Clin Immunol* 2024;154:255-263, PMID:38851398) [(JACI)](https://www.jacionline.org/article/S0091-6749(24)00569-4/fulltext).

**Key identifiers:**
- **MONDO:** MONDO:0100004
- **ICD-10-CM:** D89.4 "Mast cell activation syndrome and related disorders," with subcodes D89.40 (unspecified), D89.41 (monoclonal), D89.42 (idiopathic), D89.43 (secondary), D89.44 (hereditary alpha-tryptasemia), D89.49 (other specified) — codes effective since October 2016 [(icd10data.com)](https://www.icd10data.com/ICD10CM/Codes/D50-D89/D80-D89/D89-/D89.4)
- **MeSH/related terms:** Mastocytosis (D008415); "Mast Cell Activation" concept
- Not currently a distinct OMIM phenotype entry (hereditary alpha-tryptasemia, a genetic risk modifier, has its own OMIM entry, #618041)

**Synonyms:** MCAS; mast cell activation disorder (MCAD); systemic mast cell activation disease (MCAD, per the Molderings nomenclature); idiopathic mast cell activation syndrome; monoclonal mast cell activation syndrome (MMAS).

**Data provenance:** Most MCAS literature is aggregated disease-level (case series, retrospective cohorts, consensus/expert-opinion documents, and a handful of prospective tryptase/urinary-mediator studies), rather than large EHR/registry-based epidemiology; a recent claims-based study specifically examined rising ICD-10 "unspecified mast cell activation" (D89.40) coding trends in the US, illustrating an emerging EHR data source [(PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12439097/).

---

## 2. Etiology

### Disease causal factors
MCAS is fundamentally a **functional/mechanistic** disorder of mast cell reactivity rather than a single-gene Mendelian disease. It is now formally subclassified into five clinical phenotypes: **primary (clonal)** MCAS, driven by clonally aberrant mast cells bearing the somatic *KIT* D816V mutation and/or aberrant CD25 expression (usually a form of monoclonal MCAS or systemic mastocytosis); **secondary MCAS**, in which non-clonal mast cells are activated by an identifiable IgE- or non-IgE-mediated trigger (allergy, chronic infection, autoimmune/inflammatory disease); **combined** (clonal + secondary) MCAS; **hereditary alpha-tryptasemia (HαT)-associated** MCAS; and **idiopathic MCAS**, in which no clonal marker or trigger is found [(Sciencedirect/JACI-IP)](https://www.sciencedirect.com/science/article/pii/S2213219823013107).

### Genetic risk factors
- ***KIT* D816V** (somatic, activating tyrosine-kinase mutation) — the molecular hallmark of clonal mast cell disease; present in >90% of systemic mastocytosis but in a minority of MCAS cases. Ultrasensitive detection methods (e.g., SuperRCA, limit of detection 0.001% VAF) have raised detection of *KIT* D816V to **64% of patients with monoclonal MCAS and 55% of those with bone-marrow mastocytosis**, versus 0.01% VAF sensitivity of older ASO-qPCR assays [(ASH/Blood)](https://ashpublications.org/blood/article/146/22/2696/546736/Improved-diagnostic-screening-and-classification). *KIT* mutations have also been demonstrated in peripheral-blood leukocytes derived from hematopoietic stem cells, not only in mast cells [(ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1040842814001498).
- **Hereditary alpha-tryptasemia (HαT)** — an autosomal-dominant, highly penetrant germline trait from increased copy number of *TPSAB1* (encoding α-tryptase) on chromosome 16, present in **4–6% of the general (Caucasian) population**. Lyons et al. (*Nat Genet* 2016;48:1564-1569, PMID:27571382) described it as "a multisystem disorder associated with increased *TPSAB1* copy number," with basal serum tryptase elevated in proportion to α-tryptase-encoding copy number; associated features include systemic hypersensitivity reactions, flushing, pruritus, functional GI disease, connective-tissue abnormalities, and dysautonomia symptoms [(WebSearch synthesis of Nat Genet 2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13118244/). One extra germline *TPSAB1* copy accounts for ~80–90% of HαT cases. HαT is increasingly framed as a **genetic modifier** rather than a direct cause of MCAS, heightening mediator-symptom severity and anaphylaxis risk when co-occurring with clonal or secondary mast cell disease [(Frontiers Allergy 2025)](https://www.frontiersin.org/journals/allergy/articles/10.3389/falgy.2025.1600680/full).
- **Familial clustering:** Molderings et al. found systemic MCAD in **~46% of first-degree relatives** of index patients, versus ~17% background prevalence in the general German population, and proposed that mutated "operator/regulator" genes could predispose to somatic *KIT* mutation acquisition (Molderings, *J Hematol Oncol* 2011;4:10, PMID:21418662; Molderings 2013 familial study, PMID:24098785) [(PMC/PLOS ONE)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3787002/).
- Susceptibility-locus/GWAS-level data specific to non-clonal (idiopathic/secondary) MCAS are essentially absent from the current literature — this is flagged as a major knowledge gap.

### Environmental risk factors
Age and sex are not strongly disease-defining (MCAS is reported across the lifespan with a female predominance in most clinical series, mirroring other functional/mast-cell-related syndromes). Established environmental/behavioral triggers precipitating acute activation episodes (rather than causing the underlying susceptibility) include temperature extremes (heat/cold), humidity, sunlight, physical exertion, emotional/physical stress, infections (including COVID-19), alcohol, and specific drug classes (NSAIDs, opioids such as morphine/codeine, radiocontrast agents, some antibiotics) [(TMS)](https://tmsforacure.org/signs-symptoms-triggers/symptoms-and-triggers-of-mast-cell-activation/).

### Protective factors
No robust genetic protective variants have been reported specifically for MCAS. Avoidance-based lifestyle modification (trigger avoidance, controlled/graded exercise) is described as reducing episode frequency, though evidence quality is low (mostly expert opinion/case series).

### Gene-environment interactions
The clearest documented gene-environment interaction is **HαT × trigger exposure**: individuals with extra *TPSAB1* copies show amplified/more severe reactions to the same immunologic triggers (Hymenoptera venom, drugs, foods) compared with tryptase-normal individuals, consistent with a "modifier" model in which baseline mast-cell mediator reserve (driven by genotype) determines the magnitude of a triggered reaction [(Frontiers)](https://www.frontiersin.org/journals/allergy/articles/10.3389/falgy.2025.1600680/full).

---

## 3. Phenotypes

MCAS is defined by **episodic, recurrent symptoms involving ≥2 organ systems concurrently**, with improvement between episodes and (per consensus criteria) response to anti-mediator therapy [(JACI-IP)](https://www.jaci-inpractice.org/article/S2213-2198(19)30729-9/abstract).

**Dermatologic (cutaneous)** — flushing (suggested HP:0031372 Flushing), urticaria/hives (HP:0001025 Urticaria), pruritus (HP:0000989 Pruritus), angioedema (HP:0100785 Angioedema), dermatographism.

**Gastrointestinal** — abdominal pain/cramping (HP:0002027 Abdominal pain), nausea (HP:0002018 Nausea), vomiting (HP:0002013 Vomiting), diarrhea (HP:0002014 Diarrhea) and/or constipation (HP:0002019 Constipation), often alternating; gastroesophageal reflux (HP:0002020 Gastroesophageal reflux) — reported in up to 87.5% of HαT-associated MCAS cohorts [(PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13118244/); bloating, weight/appetite fluctuation.

**Cardiovascular** — palpitations (HP:0001962 Palpitations), tachycardia (HP:0001649 Tachycardia), hypotensive syncope (HP:0012ief Syncope, HP:0001278 Orthostatic hypotension), lightheadedness, chest discomfort; vascular anomalies (aneurysms, hemangiomas, telangiectasias) are reported in chronic case series but with weaker evidence [(Cleveland Clinic; EDS Clinic synthesis)](https://drtaniadempsey.com/clinical-manifestations-of-mast-cell-activation-syndrome-by-organ-systems/).

**Respiratory/naso-ocular** — wheezing (HP:0030828 Wheezing), dyspnea (HP:0002094 Dyspnea), nasal congestion, conjunctival injection.

**Neurologic/neuropsychiatric** — headache (HP:0002315 Headache), dizziness, "brain fog"/cognitive impairment, paresthesia, anxiety and depression — reported in ~62.5% of HαT-MCAS cases in one Greek case series [(PMC 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13118244/).

**Autonomic** — dysautonomia symptoms (~37.5% of the HαT cohort above), overlapping substantially with postural orthostatic tachycardia syndrome (POTS).

**Laboratory abnormalities** — event-related elevation of serum tryptase; elevated urinary N-methylhistamine and/or 11β-prostaglandin-F2α (metabolite of PGD2).

**Phenotype characteristics:** Onset is variable (childhood through adulthood, though most clinical series describe adult-onset or adult-diagnosed disease); severity ranges from mild chronic symptoms to anaphylaxis-grade reactions; course is classically **episodic/fluctuating** rather than steadily progressive, with baseline symptom resolution between flares as a diagnostic requirement [(Cleveland Clinic)](https://my.clevelandclinic.org/health/diseases/mast-cell-activation-syndrome).

**Quality-of-life impact:** Health-related quality of life is significantly worse in MCAS patients than in healthy controls, particularly in role-function and fatigue domains [(PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9336039/).

---

## 4. Genetic/Molecular Information

- **Somatic *KIT* D816V** (HGNC:6342, OMIM *164920): activating point mutation in the tyrosine kinase domain of KIT; gain-of-function, leading to ligand-independent receptor autophosphorylation and constitutive downstream signaling. Present in ~90% of systemic mastocytosis but variably in MCAS; clonality (per WHO criteria) also assessed by aberrant CD25/CD2 expression on marrow mast cells [(ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1081120621005135).
- **Germline *TPSAB1* copy-number gain** (chromosome 16p13.3): HGNC gene for α-tryptase; extra gene copies raise basal serum tryptase and modify mast-cell-disease severity — not itself pathogenic for neoplastic transformation but a clinically important modifier and confounder of tryptase-based MCAS diagnostic algorithms.
- **Variant classification:** *KIT* D816V is classified pathogenic/gain-of-function per ACMG-type frameworks in the myeloid neoplasm context (as in systemic mastocytosis); in isolated MCAS it is typically reported as a somatic finding of uncertain proliferative significance when found at very low variant allele frequency by ultrasensitive assays.
- **Allele frequency:** *TPSAB1* extra-copy trait (HαT) — population frequency ~4–6% in Caucasian cohorts (gnomAD-consistent estimates cited in HαT literature).
- **Somatic vs germline:** *KIT* D816V — somatic (acquired, hematopoietic); HαT *TPSAB1* duplication — germline (inherited, autosomal dominant, highly penetrant for elevated tryptase, incompletely penetrant for symptomatic disease).
- **Functional consequence:** *KIT* D816V = constitutive gain-of-function kinase activation (ligand-independent). HαT = dosage effect (increased transcription/translation of tryptase, not receptor signaling).
- **Modifier genes:** Molderings proposed heritable "operator/regulator" gene variants predisposing to acquisition of somatic *KIT* mutations in familial MCAD pedigrees, though specific loci remain unidentified [(ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1040842814001498).
- **Epigenetic information:** No well-replicated MCAS-specific DNA methylation/histone signature has been established in the literature surveyed; this is an open research gap explicitly noted by the 2024 JACI review.
- **Chromosomal abnormalities:** Not a defining feature of MCAS; large structural variants are relevant mainly to advanced/clonal mastocytosis rather than MCAS per se.

**Suggested bindings:** gene — hgnc:6342 (KIT); hgnc:12405-adjacent tryptase locus (TPSAB1, HGNC:12157); molecular function — GO term for protein tyrosine kinase activity (GO:0004713) with `modifier: GAIN_OF_FUNCTION`.

---

## 5. Environmental Information

**Environmental/toxic factors:** No specific toxin or pollutant has been causally linked to MCAS pathogenesis in controlled studies; environmental allergens (pollen, dander, mold) act as secondary-MCAS triggers via IgE-mediated sensitization rather than as etiologic agents of the syndrome itself.

**Lifestyle factors:** Alcohol consumption is a recurrent, well-documented trigger of acute mast-cell mediator release in MCAS patients; physical exertion has a described bidirectional relationship — both a trigger for reactions and, when graded/controlled, a potential therapeutic/conditioning tool [(patientpower.info)](https://www.patientpower.info/systemic-mastocytosis/mast-cell-activation-triggers).

**Infectious agents:** Acute infections (including COVID-19) and fever are recognized precipitants of symptom flares, presumably via cytokine-mediated mast-cell priming, though MCAS is not caused by a specific pathogen; this is distinct from infection-triggered secondary MCAS.

**Stress:** Emotional and physical stress (including pain itself) are consistently reported triggers, consistent with neuroimmune mast-cell activation via substance P/CRH-mediated pathways described in the broader mast-cell literature.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (illustrative, drawing on primary vs secondary/idiopathic MCAS):**

1. **Initiating lesion** — either (a) a somatic *KIT* D816V mutation arising in a hematopoietic/mast-cell progenitor (primary/clonal MCAS), (b) an IgE-sensitizing exposure or chronic inflammatory/autoimmune process (secondary MCAS), or (c) an unidentified intrinsic mast-cell hyperresponsiveness, potentially amplified by germline *TPSAB1* copy-number gain (idiopathic/HαT-associated MCAS) → **leads to** a population of mast cells with lowered activation threshold and/or increased releasable mediator reserve.
2. Mast-cell surface receptor engagement — classically **FcεRI cross-linking by allergen-bound IgE**, but also **IgE-independent pathways** (MRGPRX2 activation by basic secretagogues/drugs, complement anaphylatoxins C3a/C5a, physical stimuli, endotoxin, free radicals) — **leads to** intracellular signal transduction.
3. Downstream signaling cascades — **PI3K/Akt/mTOR, RAS/MAPK, and JAK/STAT pathways** amplify and coordinate the activation response [(PMC 2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13465963/) — **results in** cytoskeletal reorganization and granule trafficking toward the plasma membrane.
4. Degranulation and de novo mediator synthesis — release of **preformed granule contents (histamine, tryptase, heparin, chymase)** plus **newly synthesized lipid mediators (prostaglandin D2, cysteinyl leukotrienes)** and **cytokines/chemokines (TNF-α, IL-6, IL-13)** [(PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13465963/) — **leads to** local and systemic effects depending on the anatomic site of the activated mast cells.
5. End-organ effects — histamine and PGD2 → vasodilation/flushing and hypotension; histamine and leukotrienes → smooth-muscle contraction (bronchoconstriction, GI cramping); vascular permeability increase → urticaria/angioedema; autonomic nervous system engagement → tachycardia, presyncope, and dysautonomic symptoms — **culminating in** the multisystem, episodic clinical picture that defines MCAS.
6. In clonal/primary disease, this cascade is superimposed on a **persistently lower activation threshold conferred by constitutively active KIT signaling**, explaining the more severe, spontaneous, and treatment-refractory phenotype often seen in monoclonal MCAS/systemic mastocytosis versus purely reactive secondary/idiopathic disease. This branch point (clonal driver present vs absent) is inferred rather than fully mechanistically demonstrated in idiopathic MCAS, where the primary lesion remains unidentified — a point explicitly flagged as unresolved by Castells et al. 2024 [(JACI)](https://www.jacionline.org/article/S0091-6749(24)00569-4/fulltext).

**Detail by category:**
- **Molecular pathways:** FcεRI signaling; MRGPRX2 (non-IgE secretagogue receptor, relevant to drug-induced pseudoallergy); complement C3a/C5a receptors; KIT/stem-cell-factor axis (constitutively active in D816V-driven disease); PI3K/Akt/mTOR; RAS/MAPK; JAK/STAT.
- **Cellular processes:** Regulated exocytosis (degranulation), eicosanoid biosynthesis (COX/LOX pathway activation), cytokine transcription/secretion, cell migration/homing of mast-cell progenitors.
- **Protein dysfunction:** KIT receptor tyrosine kinase — ligand-independent constitutive activation via D816V substitution in the kinase domain (analogous mechanism to other activation-loop RTK mutations).
- **Immune involvement:** Both IgE-dependent (classic allergic) and IgE-independent innate activation routes contribute; chronic low-grade mast-cell-driven inflammation is proposed to underlie the "idiopathic" subgroup.
- **Tissue damage mechanisms:** Primarily functional (vasoactive/smooth-muscle) rather than destructive/fibrotic in most MCAS (contrasting with the tissue mast-cell infiltration and organ damage of aggressive systemic mastocytosis).
- **Advanced/omics data:** Ultrasensitive digital-PCR-based clonality assays (SuperRCA) represent the most notable recent molecular-profiling advance, improving detection of low-level *KIT* D816V clones in blood/marrow of MCAS patients [(ASH/Blood 2025)](https://ashpublications.org/blood/article/146/22/2696/546736/Improved-diagnostic-screening-and-classification); broad single-cell/spatial transcriptomic characterization of MCAS-specific (non-neoplastic) mast-cell populations has not yet been published at scale.

**Suggested GO/CL terms:** GO:0043303 (mast cell degranulation), GO:0033365 (protein localization to organelle — granule trafficking), GO:0002438 (acute inflammatory response to antigenic stimulus), CL:0000097 (mast cell), CL:0001060 (basophil, for comparison), GO:0004713 (protein tyrosine kinase activity, for KIT).

---

## 7. Anatomical Structures Affected

**Organ level:** No single primary organ — MCAS is inherently multisystemic. Skin (integumentary), gastrointestinal tract, cardiovascular system, respiratory tract, and nervous/autonomic system are all commonly involved; secondary/complication-level involvement can include the musculoskeletal system (via connective-tissue/EDS overlap) and reproductive tract (dysmenorrhea reported in some series).

**Tissue/cell level:** Mast cells (CL:0000097) reside in nearly all vascularized tissues but are especially dense at host-environment interfaces: skin dermis, gastrointestinal submucosa, and respiratory mucosa (UBERON:0002097 skin, UBERON:0001555 digestive tract, UBERON:0001004 respiratory system). Perivascular mast cells mediate cardiovascular symptoms; meningeal/dural mast cells have been proposed (though not firmly established) as contributors to neurologic symptoms.

**Subcellular level:** Secretory granules (GO:0042582 peroxisome — not applicable; correct term GO:0030141 secretory granule) store preformed histamine/tryptase/heparin; the endoplasmic reticulum and Golgi are involved in de novo eicosanoid and cytokine synthesis; plasma-membrane FcεRI and KIT receptors initiate signaling.

**Localization:** Symptoms are typically bilateral/systemic rather than lateralized, reflecting the diffuse tissue distribution of mast cells, though localized flares (e.g., unilateral flushing) can occur.

---

## 8. Temporal Development

**Onset:** MCAS can present at any age; most published clinical cohorts describe adult presentation or adult diagnosis, though pediatric HαT/MCAS case series exist [(PMC 2021)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8417938/). Onset pattern is typically **episodic/acute** at the level of individual flares, superimposed on a **chronic, often insidious** underlying predisposition.

**Progression:** Disease course is classically **non-linear and fluctuating** — periods of relative symptom quiescence punctuated by acute flares — rather than following a staged progressive model as in cancer. Primary (clonal) MCAS associated with advancing systemic mastocytosis can show true disease progression (increasing mast-cell burden), whereas idiopathic/secondary MCAS is generally described as a **chronic, stable-but-fluctuating** condition [(researve.com synthesis)](https://researve.com/articles/life-expectancy-mast-cell-activation-syndrome/).

**Patterns:** Spontaneous and treatment-induced symptomatic remission are both reported; no formalized MCAS-specific staging system exists (unlike systemic mastocytosis, which has WHO-defined subtypes: indolent, smoldering, aggressive, mast cell leukemia).

---

## 9. Inheritance and Population

**Epidemiology:** True population-level prevalence/incidence figures are contested. In a large single-center cohort of 703 patients referred for suspected mast-cell disorders, **idiopathic MCAS prevalence was 4.4%**, and recent systematic evaluations find that **<5% of patients referred for suspected MCAS actually meet strict consensus criteria** for primary or idiopathic MCAS after full workup [(JACI-IP 2023)](https://www.sciencedirect.com/science/article/pii/S2213219823013107). This contrasts with much higher, more speculative population estimates (up to double-digit percentages) sometimes cited in older/non-peer-reviewed sources — a discrepancy the field explicitly frames as "overdiagnosed or underdiagnosed?" [(JACI-IP 2024)](https://www.jaci-inpractice.org/article/S2213-2198(24)00065-5/fulltext). A recent claims-based study documented a **rapid rise in "unspecified" ICD-10 mast cell activation (D89.40) coding** in the US health system, suggesting increasing clinical recognition (and possible overuse of the unspecified code) rather than a true incidence surge [(PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12439097/).

**Inheritance pattern:** MCAS itself is not classically Mendelian. Where a genetic driver is identified: somatic *KIT* D816V (clonal MCAS) is acquired, not inherited; hereditary alpha-tryptasemia follows **autosomal dominant** inheritance with high penetrance for the biochemical trait (elevated tryptase) but variable/incomplete penetrance for symptomatic MCAS-like disease. Family-clustering data (Molderings) suggest a heritable predisposition to somatic *KIT* mutation acquisition in a subset of familial MCAD, but the operative gene(s) are unidentified [(PLOS ONE 2013, PMID:24098785)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0076241).

**Penetrance/expressivity:** HαT shows high penetrance for elevated basal tryptase but markedly variable clinical expressivity — many carriers are asymptomatic or mildly symptomatic, while others manifest severe multisystem disease, especially when combined with other mast-cell drivers.

**Carrier frequency:** HαT trait carrier frequency ~4–6% of Caucasian populations (gnomAD-based estimates in the HαT literature).

**Population demographics:** No strong ethnic/geographic enrichment has been robustly established for idiopathic MCAS; HαT copy-number variation frequency may differ by ancestry group, though comprehensive population-genetic surveys are limited. Female predominance is reported in most clinical MCAS series, consistent with the pattern seen in related functional syndromes (POTS, fibromyalgia) with which MCAS frequently co-occurs.

---

## 10. Diagnostics

**Consensus diagnostic criteria (Akin, Valent, Metcalfe, *J Allergy Clin Immunol* 2010;126:1099-1104, PMID:21035176)** — four criteria, all required:
1. "Episodic symptoms consistent with mast cell mediator release affecting two or more organ systems" (skin, GI, cardiovascular, respiratory, naso-ocular).
2. "A decrease in the frequency or severity; or resolution of symptoms with anti-mediator therapy" (H1/H2 antagonists, leukotriene antagonists, mast cell stabilizers).
3. "Evidence of an elevation in a validated urinary or serum marker of mast cell activation" — serum tryptase preferred, documented on ≥2 symptomatic occasions (or once if baseline tryptase >15 ng/mL).
4. "Primary (clonal) and secondary disorders of mast cell activation ruled out" [(PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3753019/).

**2019/consensus-2 refinement (Valent et al.)** formalized a quantitative acute-tryptase-rise formula: an event-related tryptase increase must meet or exceed **baseline tryptase (sBT) × 1.2 + 2 ng/mL** (i.e., 20% above baseline plus 2 ng/mL), measured within 4 hours of the event versus a baseline drawn ≥24 hours later [(De Gruyter "consensus-2")](https://www.degruyterbrill.com/document/doi/10.1515/dx-2020-0005/html).

**Laboratory/biomarker testing:**
- Serum tryptase (acute vs baseline, per above formula) — most specific validated marker.
- 24-hour urinary **N-methylhistamine** (histamine metabolite) and **11β-prostaglandin F2α / 2,3-dinor-11β-PGF2α** (PGD2 metabolite) — recommended when tryptase is unavailable or equivocal; in practice, urinary 11β-PGF2α is more frequently elevated than N-methylhistamine in idiopathic MCAS cohorts, and correlates with flushing/pruritus severity [(ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S2213219814002839). NSAID/aspirin use confounds PGF2α results and should be withheld (2 weeks for aspirin, 72 hours for NSAIDs) before collection [(Mayo Clinic Labs)](https://www.mayocliniclabs.com/test-catalog/overview/608378).

**Genetic testing:** Peripheral blood and/or bone marrow *KIT* D816V testing (standard or ultrasensitive digital PCR/SuperRCA) to distinguish clonal from non-clonal disease; *TPSAB1* copy-number analysis (droplet digital PCR) for HαT.

**Bone marrow evaluation:** Reserved for cases with elevated baseline tryptase, cytopenias, organomegaly, or other "B/C findings" suggestive of systemic mastocytosis — includes morphology, immunohistochemistry (CD117, CD25, CD2, tryptase), and molecular *KIT* testing.

**Differential diagnosis** (must be excluded before an idiopathic-MCAS label is assigned): hereditary/acquired angioedema, systemic mastocytosis, carcinoid syndrome, pheochromocytoma/paraganglioma, VIPoma, gastrinoma, medullary thyroid carcinoma, hyper-eosinophilic syndrome, aspirin-exacerbated respiratory disease, scombroid poisoning, inflammatory bowel disease, thyroid disease, and idiopathic anaphylaxis [(Merck Manual; PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10814166/). A 2024 review frames MCAS, anaphylaxis, and mastocytosis as "interrelated yet distinct conditions within the spectrum of mast cell activation disorders" [(PMC "Puzzling Mast Cell Trilogy")](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10647312/).

**Clinical criteria/screening:** No population screening program exists; diagnosis is exclusively clinical + biochemical + (when indicated) histopathologic/molecular, following the stepwise consensus algorithm above.

---

## 11. Outcome/Prognosis

MCAS is generally **not life-threatening in most non-clonal cases**, though anaphylaxis-grade episodes carry acute mortality risk, particularly when compounded by HαT or an underlying clonal disorder. Idiopathic and secondary MCAS typically follow a **chronic, fluctuating but non-progressive course**; primary (clonal) MCAS prognosis tracks the underlying mastocytosis subtype (indolent systemic mastocytosis has near-normal life expectancy, while advanced/aggressive variants carry significant morbidity/mortality) [(Rare Disease Advisor synthesis)](https://www.rarediseaseadvisor.com/hcp-resource/systemic-mastocytosis-life-expectancy/). Health-related quality of life is significantly reduced compared with healthy controls, most notably in fatigue and role-function domains [(PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9336039/). Prognostic factors favoring better outcomes include early diagnosis, trigger identification/avoidance, and adherence to stepwise anti-mediator therapy; comorbid anxiety, depression, and functional GI disease are described as compounding overall disease burden.

---

## 12. Treatment

**Pharmacotherapy — stepwise approach** (per multiple management reviews, e.g., Canadian practical approach, PMC 2025) [(PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12639879/):
1. **H1-antihistamines** (e.g., cetirizine, fexofenadine) — NCIT:C29699-class antihistamine agents; combined with **H2-antihistamines** (e.g., famotidine, ranitidine-class), since H2 receptors are present on mast cells and cardiovascular tissue, not just gastric parietal cells.
2. **Mast cell stabilizers** — oral **cromolyn sodium** (disodium cromoglycate) and **ketotifen**, added when antihistamines alone are insufficient, particularly for GI-predominant symptoms.
3. **Leukotriene receptor antagonists** (e.g., montelukast) for respiratory/GI symptoms mediated by cysteinyl leukotrienes.
4. **Aspirin** in carefully selected, monitored patients (for flushing/PGD2-mediated symptoms, with caution given aspirin's own trigger potential in a subset).
5. **Systemic corticosteroids** — reserved for severe, refractory cases due to known adverse-effect burden.
6. **Omalizumab** (anti-IgE monoclonal antibody, NCIT:C1974-class biologic) — for persistent or severe disease refractory to the above; case series document successful use even at low doses in idiopathic MCAS [(PMC 2019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6768441/).

**Targeted/clonal-disease-specific therapy** (for primary/clonal MCAS with confirmed *KIT* D816V):
- **Midostaurin** — multikinase/KIT inhibitor; improves quality of life and mediator-related symptoms and can temper IgE-mediated degranulation in advanced systemic mastocytosis.
- **Avapritinib** — selective KIT D816V inhibitor; FDA-approved for indolent and advanced systemic mastocytosis, with ~75% response rate among evaluable advanced-SM patients and marked reduction in mast-cell/disease burden [(Springer review, PMID:38217824)](https://link.springer.com/article/10.1007/s11882-023-01123-9). Long-term remission is not achieved in all patients despite disease-modifying activity.

**Emergency/anaphylaxis management:** Epinephrine auto-injector for anaphylaxis-grade reactions (standard of care, NCIT clinical-intervention terms for emergency pharmacotherapy).

**Supportive/behavioral:** Trigger identification and avoidance counseling; dietary modification for histamine-sensitive individuals (evidence quality low-moderate); psychological support for comorbid anxiety/depression; physical therapy/graded exercise where tolerated, given exercise's dual trigger/therapeutic role.

**Experimental/investigational:** Ongoing clinical trials of additional KIT inhibitors and biologics targeting mast-cell activation pathways (search ClinicalTrials.gov/WHO ICTRP for current NCT identifiers; specific trial numbers were not extracted in this pass and should be verified via `just fetch-reference` against ClinicalTrials.gov before KB entry).

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy, generic action) with `therapeutic_agent` bound to CHEBI for cetirizine/famotidine/cromolyn/montelukast/omalizumab-class biologics, and NCIT:C20401 (Monoclonal Antibody) for omalizumab's drug-class binding.

---

## 13. Prevention

**Primary prevention:** No vaccine or established primary-prevention strategy exists, since the syndrome largely reflects a fixed genetic/immunologic predisposition (clonal, HαT, or idiopathic hyperresponsiveness). Trigger avoidance (temperature extremes, alcohol, specific drugs/NSAIDs, known allergens) functions as the closest analog to primary prevention of acute episodes.

**Secondary prevention:** Early recognition and biochemical confirmation (tryptase/urinary-mediator testing) to initiate anti-mediator therapy before symptom chronification; screening first-degree relatives of patients with confirmed HαT or familial MCAD, given the elevated familial recurrence risk documented by Molderings et al.

**Tertiary prevention:** Structured anti-mediator regimens and (in clonal disease) KIT-targeted therapy to prevent progression to more severe/aggressive mast-cell disease and to reduce anaphylaxis recurrence.

**Genetic counseling:** Relevant for HαT (autosomal dominant, 50% transmission risk to offspring) and for families with clustering systemic MCAD, though formal genetic-counseling protocols specific to MCAS are not yet standardized in professional-society guidelines.

**Prophylaxis:** Premedication protocols (antihistamines ± corticosteroids) before procedures, surgery, or contrast administration in known MCAS/mastocytosis patients are widely used clinically, paralleling premedication practice in mastocytosis, though MCAS-specific trial evidence is limited.

---

## 14. Other Species / Natural Disease

Human MCAS as defined by consensus criteria (episodic multisystem mediator-release symptoms without obligate clonal proliferation) does **not have a well-characterized directly orthologous naturally occurring veterinary disease** in the literature surveyed. The closest veterinary analogs are:
- **Canine and feline mast cell tumors (mastocytoma)** — a neoplastic, KIT-mutation-associated disease of skin/subcutis, mechanistically related to clonal mast-cell proliferation (parallel to human mastocytosis) but not a functional-activation syndrome per se; canine mastocytoma is a well-studied *KIT*-mutation model (internal tandem duplications in exon 11, distinct from human D816V) used in comparative oncology.
- Anaphylactic/allergic reactions with mast-cell mediator release occur across essentially all mammalian species studied (rodent, canine, feline, equine), but a discrete "MCAS-equivalent" clinical syndrome has not been formally described outside humans in the sources reviewed here.

**Taxonomy:** NCBITaxon:9606 (Homo sapiens) is the only species with a formally defined MCAS diagnostic entity to date.

---

## 15. Model Organisms

**Mouse models:** No single validated "MCAS mouse model" exists because MCAS is fundamentally a functional/clinical syndrome rather than a defined molecular lesion in most cases. Relevant model systems instead target **mast-cell biology and clonal disease components**:
- **Mast-cell-deficient strains** (*Kit^W-sh/W-sh*, on C57BL/6 or BALB/c background) — used to dissect the necessity of mast cells in allergic/inflammatory phenotypes by comparing responses with and without mast cells; BALB/c-*Kit^W-sh/W-sh* mice retain near-wild-type airway hyperresponsiveness in some allergic-asthma models, illustrating strong background-strain dependence of mast-cell contribution [(Lab Invest 2019)](https://www.nature.com/articles/s41374-019-0354-2). These mice carry confounding hematologic abnormalities (splenomegaly, myeloid/megakaryocytic hyperplasia, neutrophilia) that limit direct translational inference [(ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1074761311004614).
- **Humanized *KIT* D816V xenograft models** — e.g., a luciferase-monitored humanized in vivo model of KIT D816V+ advanced systemic mastocytosis, used to test KIT-inhibitor efficacy (avapritinib, midostaurin, nintedanib, CDK4/6 inhibitors) preclinically [(PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5347747/); [(PMC CDK4/6 synergy study)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9264943/).
- **Murine anaphylaxis/allergy models** (passive systemic anaphylaxis, IgE-mediated airway/skin challenge) — used broadly to study IgE-FcεRI-driven mast-cell degranulation mechanisms relevant to secondary MCAS, reviewed comprehensively in a 2026 PMC article on "Insights Into Complex Murine Models of Allergy and Anaphylaxis" [(PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12716187/).

**Model characteristics/limitations:** Mast-cell-deficient mice recapitulate loss-of-mast-cell-function phenotypes but do not model the **gain-of-function/hyperresponsive** state that defines MCAS; humanized KIT D816V models capture clonal-disease drug pharmacodynamics but not the broader idiopathic/secondary MCAS phenotype space (no clonal lesion). No zebrafish, *Drosophila*, or *C. elegans* model is applicable, since mast cells are a mammalian-specific (vertebrate innate-immune) cell type. In vitro human models — **LAD2 and HMC-1 human mast-cell lines**, and **iPSC-derived mast cells** — are used for mechanistic and drug-screening studies of degranulation pathways (FcεRI, MRGPRX2, KIT signaling) relevant to MCAS, though these were not exhaustively re-verified with individual PMIDs in this search pass.

**Research applications:** Current model systems are best suited to (a) testing KIT-targeted therapeutics for clonal disease, and (b) dissecting IgE/FcεRI and MRGPRX2 degranulation pathways relevant to secondary MCAS; a validated in vivo model specifically recapitulating "idiopathic hyperresponsive mast cell" disease remains an unmet need, consistent with the mechanistic knowledge gaps flagged by Castells et al. 2024.

---

## Key Ontology-Term Suggestions Summary

| Category | Suggested term(s) |
|---|---|
| Disease | MONDO:0100004 (mast cell activation syndrome) |
| Gene (somatic driver) | hgnc:6342 (KIT) |
| Gene (modifier) | HGNC gene for TPSAB1 (tryptase alpha/beta 1) |
| Cell type | CL:0000097 (mast cell) |
| Biological process | GO:0043303 (mast cell degranulation); GO:0002438 (acute inflammatory response to antigen) |
| Anatomy | UBERON:0002097 (skin); UBERON:0001555 (digestive tract); UBERON:0001004 (respiratory system) |
| Phenotypes (HP) | HP:0031372 (Flushing); HP:0001025 (Urticaria); HP:0100785 (Angioedema); HP:0002027 (Abdominal pain); HP:0001649 (Tachycardia); HP:0001278 (Orthostatic hypotension); HP:0002315 (Headache) |
| Chemicals (CHEBI) | histamine, tryptase (protein, not CHEBI), prostaglandin D2, cysteinyl leukotrienes, heparin |
| Treatment (NCIT) | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent bindings (antihistamines, cromolyn, omalizumab, KIT inhibitors) |

---

## Important Caveats / Gaps for Curation

1. **Controversy is a defining feature of this literature** — recent papers explicitly frame MCAS as both "overdiagnosed and underdiagnosed," with true idiopathic-MCAS prevalence (~4–5% of referred patients) far lower than popular/patient-facing sources suggest. Any KB entry should distinguish consensus-criteria-confirmed MCAS from broader "mast cell activation" symptom complexes.
2. **HαT should likely be modeled as a genetic modifier/risk-factor entry (or Inheritance block) rather than folded indistinguishably into MCAS pathophysiology**, given its own OMIM/ICD-10 identity (D89.44) and modifier (not causal) role.
3. Several claims above (EDS/POTS/MCAS "trifecta" prevalence, familial recurrence percentages, quality-of-life effect sizes) come from single cohort studies or narrative reviews rather than large replicated datasets — flag with `directness: INDIRECT` or appropriate evidence grading during curation, and verify exact PMIDs/snippets via `just fetch-reference` before use, per repository policy, since this report's citations were compiled from search-engine summaries rather than direct abstract verification for every source.
4. No clinical-trial NCT identifiers were confirmed in this pass; verify via ClinicalTrials.gov directly before adding `clinical_trials:` entries.

**Sources:**
- [Mast Cell Activation Syndrome: Tools for Diagnosis and Differential Diagnosis (JACI-IP 2019)](https://www.jaci-inpractice.org/article/S2213-2198(19)30729-9/abstract)
- [Selecting the Right Criteria and Proper Classification to Diagnose MCAS: A Critical Review (JACI-IP 2021)](https://www.jaci-inpractice.org/article/S2213-2198(21)00676-0/fulltext)
- [Diagnosis of mast cell activation syndrome: a global "consensus-2"](https://www.degruyterbrill.com/document/doi/10.1515/dx-2020-0005/html)
- [Improved diagnostic screening and classification of clonal mast cell diseases by ultrasensitive KIT p.D816V detection (Blood, ASH)](https://ashpublications.org/blood/article/146/22/2696/546736/Improved-diagnostic-screening-and-classification)
- [Prevalence of KIT D816V in anaphylaxis or systemic mast cell activation (JACI)](https://www.jacionline.org/article/S0091-6749(25)01040-1/fulltext)
- [Emerging Insights into Hereditary Alpha-Tryptasemia in the Context of Mast Cell Disorders: A Greek Case Series (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13118244/)
- [Hereditary alpha-tryptasemia and monoclonal mast cell disorders (Frontiers Allergy 2025)](https://www.frontiersin.org/journals/allergy/articles/10.3389/falgy.2025.1600680/full)
- [Pathophysiological Drivers of Mast Cell Activation Syndrome and Implications for Treatment (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13465963/)
- [Mastocytosis and Mast Cell Activation Disorders: Clearing the Air (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8540348/)
- [Diagnosis and management of mast cell activation syndrome (MCAS) in Canada: a practical approach (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12639879/)
- [Mast Cell Activation Syndrome and Mastocytosis: Initial Treatment Options and Long-Term Management (PubMed)](https://pubmed.ncbi.nlm.nih.gov/30961835/)
- [Successful treatment of idiopathic MCAS with low-dose Omalizumab (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6768441/)
- [Low Prevalence of Idiopathic Mast Cell Activation Syndrome Among 703 Patients With Suspected Mast Cell Disorders (JACI-IP 2023)](https://www.jaci-inpractice.org/article/S2213-2198(23)01310-7/fulltext)
- [Mast cell activation syndrome: Current understanding and research needs (JACI 2024, PMID:38851398)](https://www.jacionline.org/article/S0091-6749(24)00569-4/fulltext)
- [Rapid rise in unspecified mast cell activation diagnosis code usage in the United States (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12439097/)
- [Dilemma of Mast Cell Activation Syndrome: Overdiagnosed or Underdiagnosed? (JACI-IP 2024)](https://www.jaci-inpractice.org/article/S2213-2198(24)00065-5/fulltext)
- [Mast Cell Activation Syndrome: Proposed Diagnostic Criteria (Akin, Valent, Metcalfe 2010, PMID:21035176) (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3753019/)
- [Mast cell activation syndrome: a review (PubMed, PMID:23179866)](https://pubmed.ncbi.nlm.nih.gov/23179866/)
- [Beyond Confirmed MCAS: Approaching Patients With Dysautonomia and Related Conditions (JACI-IP)](https://www.sciencedirect.com/science/article/abs/pii/S2213219824002812)
- [Prevalence of mast cell activation disorders and hereditary alpha tryptasemia among patients with POTS and EDS: A systematic review](https://www.sciencedirect.com/science/article/abs/pii/S1081120625001589)
- [Mast Cell Activation Syndrome: Improved Identification by Combined Determinations of Serum Tryptase and 24-Hour Urine 11β-Prostaglandin2α (JACI-IP)](https://www.sciencedirect.com/science/article/abs/pii/S2213219814002839)
- [Biomarkers in the diagnosis of mast cell activation (Curr Opin Allergy Clin Immunol 2025)](https://journals.lww.com/co-allergy/fulltext/2025/02000/biomarkers_in_the_diagnosis_of_mast_cell.5.aspx)
- [The genetic basis of mast cell activation disease - looking through a glass darkly (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1040842814001498)
- [Familial Occurrence of Systemic Mast Cell Activation Disease (PLOS ONE / PMC, PMID:24098785)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0076241)
- [Mast cell activation disease: a concise practical guide for diagnostic workup and therapeutic options (Molderings et al., J Hematol Oncol 2011, PMID:21418662)](https://pubmed.ncbi.nlm.nih.gov/21418662/)
- [Mast Cell–Targeting Therapies in Mast Cell Activation Syndromes (Curr Allergy Asthma Rep, PMID:38217824)](https://link.springer.com/article/10.1007/s11882-023-01123-9)
- [Avapritinib reduces symptoms and mast cell burden in systemic mastocytosis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12442258/)
- [CDK4/CDK6 Inhibitors Synergize with Midostaurin, Avapritinib, and Nintedanib in KIT D816V+ Neoplastic Mast Cells (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9264943/)
- [A new humanized in vivo model of KIT D816V+ advanced systemic mastocytosis monitored using a secreted luciferase (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5347747/)
- [Development of multiple features of antigen-induced asthma pathology in BALB/c-KitW-sh/W-sh mice (Lab Invest 2019)](https://www.nature.com/articles/s41374-019-0354-2)
- [Mast Cell Deficiency, A Game of Kit and Mouse (Immunity, ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1074761311004614)
- [Insights Into Complex Murine Models of Allergy and Anaphylaxis (PMC 2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12716187/)
- [A Puzzling Mast Cell Trilogy: Anaphylaxis, MCAS, and Mastocytosis (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10647312/)
- [Challenges in Drug and Hymenoptera Venom Hypersensitivity Diagnosis and Management in Mastocytosis (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10814166/)
- [Health-related quality of life and health literacy in patients with systemic mastocytosis and MCAS (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9336039/)
- [2026 ICD-10-CM Diagnosis Code D89.4: Mast cell activation syndrome and related disorders](https://www.icd10data.com/ICD10CM/Codes/D50-D89/D80-D89/D89-/D89.4)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 27 |
| On topic | 23 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:38851398` *(abstract only)*: "Mast cell activation syndrome is a term applied to several clinical entities that have gained increased attention from patients and medical providers... there are many gaps in knowledge, resulting in confusion about this clinical syndrome. Whether MCAS is a primary syndrome or exists as a constellation of symptoms in the context of known inflammatory, allergic, or clonal disorders associated with systemic mast cell activation is not well understood"
  - closest text in source: "Whether MCAS is a primary syndrome or exists as a constellation of symptoms in the context of known inflammatory, allergic, or clonal disorders associated with systemic mast cell activation is not well understood"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:27571382` (1 mention) - Colloidal Synthesis of Uniform-Sized Molybdenum Disulfide Nanosheets for Wafer-Scale Flexible Nonvolatile Memory.
  - shared terms: none

Weighed against this report's own most characteristic terms: `mcas`, `cell`, `mast`, `disease`, `clonal`, `mastocytosis`, `systemic`, `kit`, `syndrome`, `activation`, `symptom`, `idiopathic`, `tryptase`, `secondary`, `clinical`, `mast-cell`, `d816v`, `primary`, `patient`, `trigger`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 10 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0001060` (1 mention) - the report calls it "basophil, for comparison"; CL calls it **hematopoietic oligopotent progenitor cell, lineage-negative**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004713` (2 mentions) - the report calls it "protein tyrosine kinase activity, for KIT"; GO calls it **protein tyrosine kinase activity**
- `GO:0033365` (1 mention) - the report calls it "protein localization to organelle — granule trafficking"; GO calls it **protein localization to organelle**
- `NCIT:C15986` (2 mentions) - the report calls it "Pharmacotherapy, generic action", "Pharmacotherapy"; NCIT calls it **Pharmacotherapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15986` - called "Pharmacotherapy, generic action", "Pharmacotherapy"