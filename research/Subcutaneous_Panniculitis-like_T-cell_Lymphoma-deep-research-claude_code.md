---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-29T14:45:33.047789'
end_time: '2026-08-29T14:48:59.369706'
duration_seconds: 206.32
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Subcutaneous Panniculitis-like T-cell Lymphoma
  mondo_id: ''
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
  web_search_requests: 12
  num_turns: 14
  total_cost_usd: 1.0324836000000002
  session_id: 947d87eb-a7bc-50ae-bd2b-57097ad6c44a
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 44
reference_validation:
  total_references: 25
  verified: 24
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.04
  relevance_assessed: 24
  on_topic: 14
  unresolved_references:
  - DOI:10.1182/bloodadvances.2021004562/476947/Genetic-profiles-of-subcutaneous-panniculitis-like
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 33
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 13
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0031477
    reported_labels:
    - Subcutaneous nodule
    ontology_label: obsolete Abnormal mitral valve morphology
  - term_id: HP:0012156
    reported_labels:
    - Elevated serum ferritin, closest available; consider laboratory abnormality
      mapping
    ontology_label: Hemophagocytosis
  - term_id: HP:0002716
    reported_labels:
    - Uncommon (helps distinguish from nodal PTCL)
    ontology_label: Lymphadenopathy
  - term_id: HP:0004325
    reported_labels:
    - Variable
    ontology_label: Decreased body weight
  - term_id: HP:0005517
    reported_labels:
    - Hemophagocytosis
    ontology_label: T-cell lymphoma/leukemia
  labels_variant: 2
  obsolete_terms:
  - term_id: HP:0031477
    ontology_label: obsolete Abnormal mitral valve morphology
    replaced_by: HP:0001633
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Subcutaneous Panniculitis-like T-cell Lymphoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Subcutaneous Panniculitis-like T-cell Lymphoma** covering all of the
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

# Subcutaneous Panniculitis-like T-cell Lymphoma (SPTCL): Comprehensive Research Report

## 1. Disease Information

**Overview:** Subcutaneous panniculitis-like T-cell lymphoma (SPTCL) is a rare, primary cutaneous peripheral T-cell lymphoma composed of clonal cytotoxic **αβ CD8+ T cells** that infiltrate subcutaneous adipose tissue, mimicking inflammatory panniculitis both clinically and histologically. It accounts for <1% of all non-Hodgkin lymphomas and <1% of peripheral T-cell lymphomas ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK538517/); [Clinical Dermatology Review 2024](https://journals.lww.com/cddr/fulltext/2024/08040/subcutaneous_panniculitis_like_t_cell_lymphoma.10.aspx)). It was formally distinguished from the more aggressive **primary cutaneous γδ T-cell lymphoma** in the 2008 WHO-EORTC classification revision — the term SPTCL is now restricted to the αβ-phenotype entity, which carries a comparatively indolent course ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK538517/); [PathologyOutlines](https://www.pathologyoutlines.com/topic/lymphomanonBsubcutaneouspan.html)).

**Key identifiers:**
- **OMIM**: [#618398](https://www.omim.org/entry/618398) — "T-CELL LYMPHOMA, SUBCUTANEOUS PANNICULITIS-LIKE; SPTCL" (notably listed with a germline genetic basis via *HAVCR2*)
- **Orphanet**: [ORPHA:86884](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=86884)
- **MONDO**: MONDO:0019475
- **ICD-10-CM**: [C86.3](https://www.icd10data.com/ICD10CM/Codes/C00-D49/C81-C96/C86-/C86.3) — "Subcutaneous panniculitis-like T-cell lymphoma"
- **MeSH**: Lymphoma, T-Cell, Cutaneous (subcutaneous panniculitis-like subtype)

**Synonyms:** SPTCL; subcutaneous panniculitic T-cell lymphoma; panniculitis-like T-cell lymphoma (older/broader usage, now split into SPTCL [αβ] and primary cutaneous γδ T-cell lymphoma).

**Evidence basis:** The literature is predominantly aggregated case series, retrospective cohorts (EORTC Cutaneous Lymphoma Group, French/Japanese/Korean/Chinese multicenter cohorts), and case reports; there is no large prospective trial or population-based registry (e.g., no dedicated SEER coding stratum), so most epidemiologic and outcome figures derive from pooled single- or multi-center series rather than individual EHR-level aggregation.

## 2. Etiology

**Disease causal factors:** SPTCL arises from clonal expansion of cytotoxic αβ T cells homing to subcutaneous fat. A major mechanistic driver identified over the last decade is **germline loss-of-function mutation in *HAVCR2*** (encoding the immune checkpoint receptor TIM-3), found in roughly half to 85% of cases depending on cohort/ancestry ([Nat Genet 2018](https://www.nature.com/articles/s41588-018-0251-4); [Blood Adv 2019](https://ashpublications.org/bloodadvances/article/3/4/588/246752/Frequent-germline-mutations-of-HAVCR2-in-sporadic)).

**Genetic risk factors:**
- ***HAVCR2* (TIM-3) germline variants**, most notably **c.245A>G (p.Tyr82Cys)** — enriched in patients of East Asian and Polynesian ancestry on a shared founder haplotype — and **c.291A>G (p.Ile97Met)**, more common in European-ancestry patients. Both cause TIM-3 protein misfolding and loss of plasma-membrane expression ([Nat Genet 2018](https://www.nature.com/articles/s41588-018-0251-4)).
- A 2024 Japanese cohort (Okamura et al., *Cancer Science*) found **HAVCR2^Y82C in 51.0%** of patients, associated with younger age of onset, HLH development, and shorter relapse-free survival; **TET2** recurrent mutations were also identified, while **UNC13D, PIAS3, KMT2D** mutations were enriched in HAVCR2-wild-type cases ([Cancer Sci 2024](https://onlinelibrary.wiley.com/doi/10.1111/cas.16345); [PMC11531942](https://pmc.ncbi.nlm.nih.gov/articles/PMC11531942/)).
- HAVCR2^Y82C tumors show transcriptional enrichment for **IL6-JAK-STAT3** and **TNF-α/NF-κB** signaling.
- Homozygous/biallelic HAVCR2 mutation has been documented even in pediatric sporadic (non-familial) SPTCL ([PMID 34398459](https://pubmed.ncbi.nlm.nih.gov/34398459/)).

**Environmental/associated risk factors:** No specific infectious, occupational, or toxin exposure is established as causal. **Autoimmune disease co-occurs in ~20% of cases**, most notably **systemic lupus erythematosus (SLE)**, at a rate exceeding background population prevalence — some patients present on a histologic/clinical continuum with lupus erythematosus panniculitis (LEP) ([Clinical Dermatology Review 2024](https://journals.lww.com/cddr/fulltext/2024/08040/subcutaneous_panniculitis_like_t_cell_lymphoma.10.aspx); molecular overlap study [PMID 33966586](https://pubmed.ncbi.nlm.nih.gov/33966586/)).

**Protective factors:** None specifically established in the literature.

**Gene-environment interaction:** The prevailing model is that germline HAVCR2 loss-of-function lowers the threshold for macrophage/dendritic-cell inflammasome activation (see Mechanism, below); a superimposed trigger (infection, immune stimulation) is hypothesized to precipitate the hyperinflammatory/HLH phenotype, though a specific triggering exposure has not been consistently identified.

## 3. Phenotypes

| Phenotype | Type | Frequency/Notes | Suggested HP term |
|---|---|---|---|
| Subcutaneous nodules/plaques | Physical sign | Cardinal finding; typically multiple, on extremities and trunk | HP:0031477 (Subcutaneous nodule) |
| Erythematous skin lesions | Sign | Common | HP:0010783 (Erythema) |
| Painless (or occasionally tender) lesions | Symptom | Variable; usually painless but can be tender/pruritic | — |
| Fever | Symptom | Common, especially with HLH | HP:0001945 (Fever) |
| Hepatosplenomegaly | Sign | Seen with HLH complication | HP:0001433 / HP:0001744 |
| Pancytopenia/bicytopenia | Lab abnormality | ~72.7% of HLH-complicated cases (general HLH cohort data) | HP:0001873 (Thrombocytopenia), HP:0001899 (Leukopenia), HP:0001903 (Anemia) |
| Hyperferritinemia | Lab abnormality | ~95% of HLH-complicated cases | HP:0012156 (Elevated serum ferritin, closest available; consider laboratory abnormality mapping) |
| Hypertriglyceridemia | Lab abnormality | ~52.5% of HLH cases | HP:0002155 (Hypertriglyceridemia) |
| Hypofibrinogenemia | Lab abnormality | ~30.8% of HLH cases | HP:0011900 (or related coagulation abnormality term) |
| Lymphadenopathy | Sign | Uncommon (helps distinguish from nodal PTCL) | HP:0002716 |
| Weight loss/B symptoms | Symptom | Variable | HP:0004325 |
| Hemophagocytic lymphohistiocytosis (HLH) | Complication/syndrome | 15–20% of cases; major prognostic determinant | HP:0005517 (Hemophagocytosis) |

**Onset:** Median age of presentation is reported variably across cohorts — roughly 30–46 years depending on series, with a female predominance; **~20% of cases occur in patients <20 years old**, including infants ([Dove Medical Press pediatric case series](https://www.dovepress.com/subcutaneous-panniculitis-like-t-cell-lymphoma-in-children-two-case-re-peer-reviewed-fulltext-article-CCID); [PMC5660631](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5660631/) — 8-month-old infant case).

**Progression/course:** Classically indolent, relapsing-remitting cutaneous disease without extracutaneous spread in most cases; a minority develop **HLH**, which is associated with rapid deterioration and markedly worse prognosis. Upper-extremity involvement has been reported as an independent poor-prognostic clinical feature (EORTC study, [Blood 2008;111:838](https://ashpublications.org/blood/article/111/2/838/103709/Subcutaneous-panniculitis-like-T-cell-lymphoma)).

**Quality of life impact:** Not systematically studied with validated instruments (EQ-5D/SF-36) in the literature reviewed; morbidity is driven primarily by recurrent cutaneous lesions and, in the HLH subset, systemic multi-organ dysfunction.

## 4. Genetic/Molecular Information

**Causal/predisposition gene:**
- ***HAVCR2*** (hgnc:18437; encodes TIM-3), 5q33.3. Germline biallelic (homozygous or compound heterozygous) or, in some series, monoallelic loss-of-function variants are strongly associated with SPTCL, particularly the HLH-complicated phenotype. OMIM entry #618398 frames SPTCL as having a defined germline genetic contribution via HAVCR2.

**Key variants:**
- **c.245A>G, p.Tyr82Cys (Y82C)** — founder variant in East Asian/Polynesian populations; most frequently reported pathogenic allele (up to ~51% of an all-Japanese cohort) ([Cancer Sci 2024](https://onlinelibrary.wiley.com/doi/10.1111/cas.16345)).
- **c.291A>G, p.Ile97Met (I97M)** — predominant in European-ancestry patients ([Nat Genet 2018](https://www.nature.com/articles/s41588-018-0251-4)).
- Both are **missense, loss-of-function** variants causing protein misfolding and failure of TIM-3 surface trafficking (functionally near-null alleles).
- **Zygosity:** Homozygous or compound heterozygous germline genotypes correlate with more severe/HLH phenotypes; heterozygous carriage alone appears insufficient in some models, consistent with recessive inheritance for the HLH-prone phenotype, though case reports of a single confirmed homozygous 14-year-old female patient exist ([PMID 34398459](https://pubmed.ncbi.nlm.nih.gov/34398459/)).
- **Somatic co-mutations**: recurrent somatic *TET2* mutations (epigenetic regulator); *UNC13D*, *PIAS3*, *KMT2D* mutations enriched in HAVCR2-wild-type tumors, suggesting at least partially distinct molecular subgroups ([PMC11531942](https://pmc.ncbi.nlm.nih.gov/articles/PMC11531942/)).
- Enrichment of **IL6-JAK-STAT3** and **TNF-α/NF-κB** transcriptional signatures in HAVCR2-mutant tumors provides rationale for JAK-inhibitor therapy (see Treatment).

**Variant classification:** HAVCR2 Y82C and I97M are generally reported as pathogenic/likely pathogenic loss-of-function alleles per functional (protein misfolding/trafficking) assays; population frequency in gnomAD is low but the Y82C founder allele shows regional enrichment in East Asian/Pacific populations.

**Somatic vs. germline:** The disease-defining HAVCR2 variants are **germline** (present in non-tumor tissue), distinguishing the genetic mechanism of SPTCL from typical somatically-driven lymphomas; additional somatic mutations (TET2, etc.) likely cooperate in clonal T-cell transformation.

**Epigenetics:** Limited direct data; TET2 (a DNA-demethylation enzyme) recurrent mutation implicates epigenetic dysregulation as a contributing somatic event, analogous to its role in other T-cell lymphomas (e.g., AITL, PTCL-NOS).

**Chromosomal abnormalities:** No recurrent SPTCL-specific translocation or aneuploidy has been established as a defining feature; TCR gene rearrangement (clonal) is used diagnostically rather than as a structural chromosomal marker.

**Suggested gene/ontology terms:** HGNC gene: `hgnc:18437` (HAVCR2); GO biological process candidates: "negative regulation of inflammasome activation" (custom/at present no single precise GO ID exists but see GO:0043525-adjacent processes for regulation of neuron apoptosis is irrelevant — better: GO:0032621 "interleukin-18 production," GO:0032621/GO:0002218 "activation of innate immune response").

## 5. Environmental Information

No specific toxin, occupational, radiation, dietary, or lifestyle exposure has been established as causally linked to SPTCL in the literature surveyed. No infectious agent (viral, bacterial, fungal, or parasitic) has been consistently implicated as an etiologic trigger, in contrast to some other T/NK-cell lymphomas (e.g., EBV in extranodal NK/T-cell lymphoma). One differential-diagnosis pitfall paper does note a peripheral T-cell lymphoma NOS case with HAVCR2 compound heterozygous mutation that was **EBV-positive**, but this represents a related/overlapping entity rather than an established SPTCL trigger ([PMC9539911](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9539911/)). No established gene-environment interaction data exist beyond the hypothesis that an unidentified inflammatory trigger unmasks HLH in HAVCR2-deficient hosts.

## 6. Mechanism / Pathophysiology

**Causal chain (proposed model):**
1. **Germline HAVCR2 loss-of-function** → TIM-3 protein misfolds and fails to reach the macrophage/dendritic-cell/T-cell plasma membrane.
2. **Loss of TIM-3 inhibitory signaling** on macrophages/dendritic cells removes a brake on the **TLR–NF-κB pathway**, ATP release, K+ efflux, and reactive oxygen species (ROS) production ([Frontiers Immunology case report](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1271324/full)).
3. This lowers the threshold for **NLRP3 inflammasome activation**, driving excess IL-1β/IL-18 production and macrophage hyperactivation — mechanistically linking TIM-3 deficiency to both the panniculitic tissue infiltrate and, when uncontrolled, systemic **hemophagocytic lymphohistiocytosis**.
4. In parallel, clonal cytotoxic **αβ CD8+ T cells** (perforin/granzyme B/TIA-1–expressing) infiltrate and "rim" individual adipocytes within the subcutaneous fat lobule, driving adipocyte apoptosis, karyorrhexis, and fat necrosis — the histologic hallmark ("rimming").
5. Somatic cooperating mutations (TET2 and others) and enrichment of **IL-6/JAK/STAT3** and **TNF-α/NF-κB** signaling programs are proposed to support clonal T-cell survival/expansion.

**Cellular processes:** Cytotoxic T-cell–mediated apoptosis of adipocytes; macrophage/histiocyte hyperactivation and hemophagocytosis (engulfment of erythrocytes, leukocytes, platelets, and their precursors) in the HLH-complicated subset; chronic granulomatous-pattern fat necrosis.

**Protein dysfunction:** TIM-3 (HAVCR2 product) misfolding/loss of surface expression is the central molecular lesion identified to date; this is a loss-of-function immune-checkpoint defect rather than a classic oncogenic driver mutation.

**Immune system involvement:** Central to pathogenesis — SPTCL sits at the intersection of lymphomagenesis and autoinflammation/autoimmunity, given (a) the ~20% co-occurrence with autoimmune disease (especially SLE), (b) the checkpoint-deficiency mechanism causing innate immune hyperactivation, and (c) the frequent secondary HLH.

**Tissue damage mechanisms:** Direct cytotoxic T-cell killing of adipocytes; secondary necroinflammatory fat necrosis; in HLH, systemic cytokine-storm–mediated multi-organ injury (hepatic, marrow, splenic).

**Suggested GO/CL terms:**
- GO:0097191 (extrinsic apoptotic signaling pathway) / GO:0001909 (leukocyte-mediated cytotoxicity)
- GO:0002218 (activation of innate immune response); GO:0032621 (interleukin-18 production)
- CL:0000625 (CD8-positive, alpha-beta T cell); CL:0000913 (effector memory CD8-positive, alpha-beta T cell); CL:0000439 (professional antigen-presenting cell) for macrophages/dendritic cells involved in NLRP3-driven hyperinflammation
- CL:0000136 (fat cell/adipocyte) as the injured target cell population

**Molecular profiling:** RNA-sequencing/whole-exome sequencing studies (discovery cohorts of ~8 patients plus larger validation cohorts) have characterized the HAVCR2-mutant transcriptional signature (IL6-JAK-STAT3, TNF-NF-κB pathway enrichment) ([PMC11531942](https://pmc.ncbi.nlm.nih.gov/articles/PMC11531942/); [Blood Adv 2021, PMID 34535012](https://pubmed.ncbi.nlm.nih.gov/34535012/)). No large-scale single-cell, spatial transcriptomic, or proteomic datasets specific to SPTCL were identified in this search.

## 7. Anatomical Structures Affected

- **Primary organ/tissue:** Subcutaneous adipose tissue (panniculus), most often of the **extremities (especially lower legs/thighs) and trunk**; face is less commonly involved.
- **Secondary involvement (HLH-complicated disease):** Liver, spleen, bone marrow (hemophagocytosis), lymph nodes (uncommon primary involvement — nodal disease is atypical and should prompt reconsideration of the diagnosis).
- **Tissue/cell level:** Subcutaneous fat lobules; cytotoxic CD8+ αβ T lymphocytes infiltrating and rimming individual adipocytes; histiocytes/macrophages (hemophagocytosis in marrow/spleen/liver when HLH supervenes).
- **Subcellular level:** Plasma membrane trafficking defect of TIM-3 (HAVCR2 product) in macrophages/dendritic cells/T cells; cytotoxic granule (perforin/granzyme B) machinery in the neoplastic T cells.
- **Suggested UBERON terms:** UBERON:0002190 (subcutaneous adipose tissue); UBERON:0002107 (liver); UBERON:0002106 (spleen); UBERON:0002371 (bone marrow).
- **Laterality:** Typically bilateral, multifocal nodules rather than strictly unilateral disease.

## 8. Temporal Development

- **Onset:** Can occur across the age spectrum, from infancy to older adulthood; median onset reported between ~30–46 years across cohorts, with ~20% of cases in patients <20 years old.
- **Onset pattern:** Typically insidious — gradual appearance of subcutaneous nodules over weeks to months; HLH, when it develops, can have an acute/subacute onset superimposed on chronic cutaneous disease.
- **Progression:** Chronic, relapsing-remitting cutaneous course in most patients (indolent, "stable/fluctuating" pattern) without extracutaneous dissemination; a subset (15–20%) develops HLH, which follows a rapidly progressive, life-threatening course.
- **Remission:** Spontaneous resolution of individual nodules can occur, but disease-free cure without treatment is not the norm; treatment-induced remission (immunosuppressive therapy achieving complete response in up to 85% of treated patients in some series) is well documented.
- **Disease duration:** Chronic, often lifelong tendency to relapse in the non-HLH subset; HLH episodes are acute, life-threatening events requiring urgent intervention.

## 9. Inheritance and Population

**Epidemiology:** SPTCL is exceedingly rare — accounting for <1% of all peripheral T-cell lymphomas and <1% of non-Hodgkin lymphomas overall. No dedicated national/SEER-level incidence figure specific to SPTCL was identified; it is generally described only through case-series aggregation.

**Inheritance pattern (genetic subset):** Where germline biallelic *HAVCR2* loss-of-function is present, the pattern is consistent with **autosomal recessive** predisposition to the HLH-complicated phenotype (homozygous or compound heterozygous genotype associated with more severe disease); however, most reported cases are considered clinically **sporadic** even when the causal germline variant is identified (i.e., "sporadic" at the clinical-family level but molecularly germline/heritable) ([Blood Adv 2019](https://ashpublications.org/bloodadvances/article/3/4/588/246752/Frequent-germline-mutations-of-HAVCR2-in-sporadic)).

**Penetrance/expressivity:** Incompletely characterized; not all HAVCR2-mutant carriers develop SPTCL or HLH, implying incomplete penetrance and a likely requirement for additional somatic or environmental cooperating factors.

**Founder effect:** The HAVCR2 **p.Tyr82Cys (Y82C)** variant occurs on a shared founder haplotype in patients of **East Asian and Polynesian ancestry**; p.Ile97Met is more prevalent in patients of **European ancestry** — a clear population-genetic/geographic stratification ([Nat Genet 2018](https://www.nature.com/articles/s41588-018-0251-4)).

**Demographics:** Reports consistently note a **female predominance**. Pediatric and adolescent presentation is well documented (~20% of cases <20 years).

## 10. Diagnostics

**Histopathology (gold standard):** Deep incisional/excisional skin biopsy (not superficial punch) showing **lobular panniculitis with atypical lymphocytes "rimming" individual adipocytes**, karyorrhexis, fat necrosis, and cytophagic histiocytes (fat/lymphocyte engulfment by benign histiocytes — "beanbag cells") without epidermal involvement ([PathologyOutlines](https://www.pathologyoutlines.com/topic/lymphomanonBsubcutaneouspan.html); [PMC2965923](https://pmc.ncbi.nlm.nih.gov/articles/PMC2965923/)).

**Immunohistochemistry:** Neoplastic cells are **CD3+, CD8+, βF1+ (αβ TCR), CD4−, CD56−, CD30−**, with expression of cytotoxic markers **TIA-1, granzyme B, perforin**. An elevated **Ki-67 proliferation index** ("Ki-67 hotspots") among CD8+ rimming lymphocytes helps distinguish SPTCL from lupus panniculitis ([PMID 26796503](https://pubmed.ncbi.nlm.nih.gov/26796503/); [PMID 29742552](https://pubmed.ncbi.nlm.nih.gov/29742552/)).

**Molecular/genetic testing:** Clonal **TCR gene rearrangement** (T-cell receptor gamma/beta) by PCR supports diagnosis. Germline **HAVCR2** sequencing (Sanger or targeted NGS panel) is increasingly used, especially in cases with HLH or pediatric presentation, given the high mutation prevalence.

**Differential diagnosis — SPTCL vs. lupus erythematosus panniculitis (LEP):** LEP favors epidermal changes, reactive lymphoid follicles with germinal centers, mixed infiltrate with plasma cells, CD123+ plasmacytoid dendritic cell clusters, polyclonal TCR rearrangement, and low Ki-67; SPTCL favors monomorphous CD8+ rimming infiltrate, high Ki-67 "hotspots," and clonal TCR rearrangement. LEP and SPTCL can overlap and coexist in the same patient, and molecular studies of ~208 genes have shown genuine overlap cases exist on a disease spectrum ([PMID 33966586](https://pubmed.ncbi.nlm.nih.gov/33966586/); [PMID 26796503](https://pubmed.ncbi.nlm.nih.gov/26796503/)).

**Differential diagnosis — SPTCL vs. primary cutaneous γδ T-cell lymphoma:** γδ phenotype (rather than αβ) predicts a much more aggressive course with frequent HLH, ulceration, and extracutaneous spread; distinguishing requires TCR-δ/βF1 immunostaining. Increased reactive γδ T cells within an otherwise αβ SPTCL is a described diagnostic pitfall ([MD Anderson publication](https://mdanderson.elsevierpure.com/en/publications/subcutaneous-panniculitis-like-t-cell-lymphoma-with-increased-gd-/)).

**Imaging:** ¹⁸F-FDG PET/CT is used for staging and to assess extracutaneous involvement/treatment response ([Frontiers Oncology, 11 patients](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.650822/full)).

**HLH work-up:** When SPTCL is diagnosed, screen for HLH using the **HLH-2004 criteria** (≥5 of 8): fever, splenomegaly, cytopenia in ≥2 lineages, hypertriglyceridemia and/or hypofibrinogenemia, hemophagocytosis on marrow/spleen/node biopsy, low/absent NK-cell cytotoxicity, hyperferritinemia, elevated soluble CD25 (sIL-2R).

**Staging:** Cutaneous lymphoma TNMB (tumor, node, metastasis, blood) staging is applied per NCCN Cutaneous Lymphomas guidelines to define disease burden and guide skin-directed vs. systemic therapy selection.

## 11. Outcome/Prognosis

**Survival:** Overall prognosis is favorable for the αβ (SPTCL proper) phenotype, with reported **5-year overall survival of 85–91%** and 3-year OS around 85.2% in some cohorts ([PMC8523605](https://pmc.ncbi.nlm.nih.gov/articles/PMC8523605/); EORTC study [Blood 2008;111:838](https://ashpublications.org/blood/article/111/2/838/103709/Subcutaneous-panniculitis-like-T-cell-lymphoma)).

**HLH impact:** HLH complicates **15–20%** of cases and is the single most important adverse prognostic factor, reducing 5-year OS to roughly **46%**. HAVCR2-mutant (especially Y82C) cases show higher HLH incidence, greater HLH severity, and shorter relapse-free survival.

**Other adverse prognostic factors:** Upper-extremity lesion location has been associated with worse outcome (EORTC study).

**Recurrence:** Cutaneous relapse is common even after complete response to immunosuppressive therapy; ongoing surveillance is required.

**Cause of death (when it occurs):** Predominantly related to uncontrolled HLH/multi-organ failure or infection, rather than direct tumor-related organ failure from cutaneous disease itself.

## 12. Treatment

**First-line (non-HLH disease):** **Immunosuppressive therapy** — systemic corticosteroids, alone or combined with **low-dose methotrexate** or **cyclosporine A** — is now generally preferred over cytotoxic polychemotherapy for uncomplicated disease, achieving complete response in up to 85% of treated patients in some cohorts. A French cohort found **complete remission in 81.2%** with immunosuppressive drugs vs. only **28.5%** with polychemotherapy, and progression in 6.2% vs. 42.8% respectively ([Acta Derm Venereol](https://www.medicaljournals.se/acta/content/html/10.2340/00015555-2543)). Sustained CR rates were broadly comparable between chemotherapy (64%) and immunosuppressive therapy (55%) in another analysis.

- Treatment_term: **NCIT:C15986** (Pharmacotherapy) with `therapeutic_agent` bound to CHEBI terms for prednisone/prednisolone, methotrexate (CHEBI:44185), and ciclosporin (CHEBI:4031). Cyclosporine has also been proposed as upfront therapy even in aggressive-feature disease ([PMC12778365](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12778365/)).

**Radiotherapy:** Used for localized/solitary lesions (NCIT:C15313, Radiation Therapy).

**Chemotherapy:** Multiagent regimens (e.g., CHOP-based) reserved for patients with HLH at presentation, or who progress on/are refractory to immunosuppressive therapy (NCIT:C15632, Chemotherapy). Pralatrexate has shown a significant response in a case of HLH-complicated SPTCL ([PMC12593427](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12593427/)).

**HLH-directed therapy:** **Ruxolitinib** (JAK1/2 inhibitor) has demonstrated efficacy in SPTCL-associated HLH, mechanistically rational given the IL6-JAK-STAT3 pathway enrichment in HAVCR2-mutant disease ([Blood Adv 2020](https://ashpublications.org/bloodadvances/article/4/7/1383/454297/Efficacy-of-ruxolitinib-in-subcutaneous)). Etoposide-containing HLH-directed regimens (e.g., HLH-94/HLH-2004-style, or CHOEP) have been used in severe/refractory HLH cases, sometimes bridging to **autologous hematopoietic stem cell transplantation** ([PMID 23995110](https://pubmed.ncbi.nlm.nih.gov/23995110/) — BFM-NHL/ALL-90 regimen plus autologous PBSCT).

**Surgical/reconstructive:** Dermal matrix (e.g., Integra®) reconstruction has been reported for extensive cutaneous defects in a multimodal management case ([MDPI](https://www.mdpi.com/2079-9721/13/7/201)).

**Experimental/novel:** Emapalumab (anti-IFN-γ monoclonal antibody, approved for primary HLH) is mechanistically plausible for HLH-complicated SPTCL given interferon-driven macrophage activation, though this search did not surface SPTCL-specific published outcomes data for it.

**Treatment algorithm summary:**
| Clinical scenario | Preferred approach |
|---|---|
| Uncomplicated cutaneous SPTCL | Corticosteroids ± methotrexate/cyclosporine (immunosuppressive-first) |
| Localized/solitary lesion | Radiotherapy |
| Refractory to immunosuppression | Multiagent chemotherapy |
| SPTCL + HLH | Chemotherapy/HLH-directed regimen ± ruxolitinib; consider stem cell transplant in severe/refractory cases |

## 13. Prevention

No established primary prevention strategy exists, as no modifiable environmental or infectious trigger has been identified. **Secondary prevention/early detection** centers on prompt deep biopsy of persistent subcutaneous nodules to avoid diagnostic delay (frequently misdiagnosed initially as benign panniculitis, cellulitis, or lupus panniculitis) and on proactive HLH surveillance (ferritin, triglycerides, fibrinogen, CBC) in confirmed SPTCL patients, particularly those with known HAVCR2 mutations, to enable rapid initiation of HLH-directed therapy. **Genetic counseling** may be considered for families with a germline HAVCR2 variant, given the (incompletely penetrant) autosomal-recessive-pattern association with HLH-complicated disease, though no formal cascade-screening guideline was identified in this search. No vaccine or prophylactic pharmacologic strategy is described.

## 14. Other Species / Natural Disease

No naturally occurring veterinary correlate of SPTCL specifically was identified in this search (unlike some other lymphoma subtypes with described companion-animal analogs in OMIA). TIM-3 (Havcr2) biology has been studied in **mouse models**: conditional deletion of TIM-3 in murine dendritic cells leads to ROS accumulation and NLRP3 inflammasome activation, and murine Tim-3-deficiency models have been used to demonstrate loss of the TLR–NF-κB inhibitory brake in macrophages, mechanistically recapitulating the human hyperinflammatory phenotype ([Frontiers Immunology](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1271324/full)). These are gene-function models of the HAVCR2 pathway rather than spontaneous SPTCL-mimicking disease models. Orthologous gene: mouse *Havcr2* (Tim-3), NCBI Gene.

## 15. Model Organisms

- **Genetic (knockout/conditional) mouse models:** Tim-3 (Havcr2) conditional knockout mice, particularly dendritic-cell– and macrophage-specific deletion models, recapitulate loss of TIM-3–mediated inhibition of TLR-NF-κB signaling and NLRP3 inflammasome hyperactivation — informative for the HLH/hyperinflammatory arm of SPTCL pathophysiology, but these are gene-pathway models rather than tumor-forming SPTCL models.
- **Limitations:** No described mouse model recapitulates the full clonal cytotoxic-T-cell lymphomagenesis phenotype of human SPTCL; existing models address only the innate-immune/inflammasome consequence of TIM-3 loss, not lymphoma development itself.
- **Cell-line/in vitro models:** Patient-derived macrophages from HAVCR2-mutant HLH-SPTCL patients have been used ex vivo to demonstrate lowered inflammasome activation thresholds and increased inflammatory cytokine release, providing direct human functional validation complementing the mouse data.
- No organoid, iPSC-derived, or zebrafish SPTCL models were identified in this search.

---

## Summary Table: Suggested Ontology Bindings

| Domain | Suggested term |
|---|---|
| Disease | MONDO:0019475; OMIM:618398; ORPHA:86884; ICD-10: C86.3 |
| Causal gene | hgnc:18437 (HAVCR2) |
| Cell type | CL:0000625 (CD8+ αβ T cell); CL:0000136 (adipocyte); CL:0000235 (macrophage) |
| Anatomy | UBERON:0002190 (subcutaneous adipose tissue); UBERON:0002106 (spleen); UBERON:0002107 (liver) |
| Key phenotype | HP:0031477 (subcutaneous nodule); HP:0001945 (fever); HP:0005517 (hemophagocytosis); HP:0002155 (hypertriglyceridemia) |
| Treatment agent | CHEBI:4031 (ciclosporin); CHEBI:44185 (methotrexate); NCIT:C15986 (Pharmacotherapy); NCIT:C15632 (Chemotherapy); NCIT:C15313 (Radiation Therapy) |

---

### Sources
- [Subcutaneous Panniculitis-like T-cell Lymphoma – Clinical Dermatology Review (2024)](https://journals.lww.com/cddr/fulltext/2024/08040/subcutaneous_panniculitis_like_t_cell_lymphoma.10.aspx)
- [Subcutaneous Panniculitis-Like T-cell Lymphoma – StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK538517/)
- [Pathophysiology and current treatments for SPTCL: an updated review – PubMed](https://pubmed.ncbi.nlm.nih.gov/35509196/)
- [Diagnosis and treatment of SPTCL: A systematic literature review – ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1658387621000510)
- [Germline HAVCR2 mutations altering TIM-3 characterize SPTCL with HLH – Nature Genetics (2018)](https://www.nature.com/articles/s41588-018-0251-4)
- [Frequent germline mutations of HAVCR2 in sporadic SPTCL – Blood Advances](https://ashpublications.org/bloodadvances/article/3/4/588/246752/Frequent-germline-mutations-of-HAVCR2-in-sporadic)
- [HAVCR2 mutations are associated with severe hemophagocytic syndrome in SPTCL – Blood](https://ashpublications.org/blood/article/135/13/1058/440986/HAVCR2-mutations-are-associated-with-severe)
- [SPTCL in a 14-year-old female homozygous for HAVCR2 mutation – PubMed](https://pubmed.ncbi.nlm.nih.gov/34398459/)
- [Genetic profiles of SPTCL and clinicopathological impact of HAVCR2 mutations – Blood Advances](https://ashpublications.org/bloodadvances/article/doi/10.1182/bloodadvances.2021004562/476947/Genetic-profiles-of-subcutaneous-panniculitis-like)
- [Genetic profiles and clinical features in SPTCL – Cancer Science (2024)](https://onlinelibrary.wiley.com/doi/10.1111/cas.16345) / [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11531942/)
- [TIM-3 deficiency presenting with two clonally unrelated SPTCL/HLH episodes – PubMed](https://pubmed.ncbi.nlm.nih.gov/32285995/)
- [Novel germline HAVCR2 compound heterozygous mutation, EBV-positive PTCL-NOS – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9539911/)
- [SPTCL: definition, classification, and prognostic factors – EORTC study, Blood (2008)](https://ashpublications.org/blood/article/111/2/838/103709/Subcutaneous-panniculitis-like-T-cell-lymphoma)
- [SPTCL: Clinical features, therapeutic approach, and outcome in 16 patients – ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0190962218320486)
- [SPTCL Clinical Features and Outcomes from a Single Tertiary Center – PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8523605/)
- [SPTCL: Immunosuppressive Drugs Induce Better Response than Polychemotherapy – Acta Dermato-Venereologica](https://www.medicaljournals.se/acta/content/html/10.2340/00015555-2543)
- [A Case of Pediatric SPTCL Successfully Treated with Immunosuppressive Therapy – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12384592/)
- [Ciclosporin as upfront therapy in SPTCL – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12778365/)
- [Efficacy of ruxolitinib in SPTCL and HLH – Blood Advances](https://ashpublications.org/bloodadvances/article/4/7/1383/454297/Efficacy-of-ruxolitinib-in-subcutaneous)
- [SPTCL complicated by HLH: response to pralatrexate – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12593427/)
- [SPTCL with HLH treated with BFM-NHL/ALL-90 and autologous PBSCT – PubMed](https://pubmed.ncbi.nlm.nih.gov/23995110/)
- [Diagnostic Challenge and Multimodal Management with Integra® Dermal Matrix – MDPI](https://www.mdpi.com/2079-9721/13/7/201)
- [Useful Parameters for Distinguishing SPTCL From Lupus Erythematosus Panniculitis – PubMed](https://pubmed.ncbi.nlm.nih.gov/26796503/)
- [SPTCL Versus LEP: Distinction by Periadipocytic Cell Proliferation Index – PubMed](https://pubmed.ncbi.nlm.nih.gov/29742552/)
- [SPTCL, lupus erythematosus profundus, and overlapping cases: 208-gene molecular characterization – PubMed](https://pubmed.ncbi.nlm.nih.gov/33966586/)
- [SPTCL With Increased γδ T Cells: A Diagnostic Pitfall – MD Anderson](https://mdanderson.elsevierpure.com/en/publications/subcutaneous-panniculitis-like-t-cell-lymphoma-with-increased-gd-/)
- [Pathology Outlines: SPTCL](https://www.pathologyoutlines.com/topic/lymphomanonBsubcutaneouspan.html)
- [Report of Eleven Patients of SPTCL: Clinicopathologic Features, PET/CT Findings and Outcome – Frontiers Oncology](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.650822/full)
- [OMIM #618398 – T-CELL LYMPHOMA, SUBCUTANEOUS PANNICULITIS-LIKE](https://www.omim.org/entry/618398)
- [Orphanet: SPTCL (ORPHA:86884)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=86884)
- [ICD-10-CM C86.3](https://www.icd10data.com/ICD10CM/Codes/C00-D49/C81-C96/C86-/C86.3)
- [GARD – SPTCL](https://rarediseases.info.nih.gov/diseases/10193/subcutaneous-panniculitis-like-t-cell-lymphoma)
- [Case Report: HAVCR2 mutation-associated HLH – Frontiers Immunology](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1271324/full) / [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10701531/)
- [Subcutaneous panniculitis-like T-cell lymphoma in children: case series – Dove Medical Press](https://www.dovepress.com/subcutaneous-panniculitis-like-t-cell-lymphoma-in-children-two-case-re-peer-reviewed-fulltext-article-CCID)
- [SPTCL Presenting as Local Inflammation of a Thigh in an 8-Month-Old Child – PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5660631/)
- [NCCN Guidelines: Cutaneous Lymphomas](https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1549)
- [Mycosis Fungoides, Sézary Syndrome, and Cutaneous B-Cell Lymphomas: 2025 Update](https://onlinelibrary.wiley.com/doi/10.1002/ajh.27735) / [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12326239/)
- [Subcutaneous Panniculitis-like T-Cell Lymphoma – NEJM Clinical Image](https://www.nejm.org/doi/full/10.1056/NEJMicm2503203)
- [HLH-2004: Diagnostic and therapeutic guidelines for HLH – PubMed](https://pubmed.ncbi.nlm.nih.gov/16937360/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 14 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1182/bloodadvances.2021004562/476947/Genetic-profiles-of-subcutaneous-panniculitis-like` (2 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031477` (2 mentions) - the report calls it "Subcutaneous nodule"; HP calls it **obsolete Abnormal mitral valve morphology**
- `HP:0012156` (1 mention) - the report calls it "Elevated serum ferritin, closest available; consider laboratory abnormality mapping"; HP calls it **Hemophagocytosis**
- `HP:0002716` (1 mention) - the report calls it "Uncommon (helps distinguish from nodal PTCL)"; HP calls it **Lymphadenopathy**
- `HP:0004325` (1 mention) - the report calls it "Variable"; HP calls it **Decreased body weight**
- `HP:0005517` (2 mentions) - the report calls it "Hemophagocytosis"; HP calls it **T-cell lymphoma/leukemia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0031477` (obsolete Abnormal mitral valve morphology) (2 mentions) - replaced by `HP:0001633`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000439` (1 mention) - the report calls it "professional antigen-presenting cell"; CL calls it **prolactin secreting cell**
- `CL:0000136` (2 mentions) - the report calls it "fat cell/adipocyte"; CL calls it **adipocyte**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.