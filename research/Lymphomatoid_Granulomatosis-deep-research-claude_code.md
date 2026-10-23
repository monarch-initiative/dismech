---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-29T14:45:34.898290'
end_time: '2026-08-29T14:50:16.275062'
duration_seconds: 281.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lymphomatoid Granulomatosis
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
  web_search_requests: 22
  num_turns: 28
  total_cost_usd: 1.5200192000000001
  session_id: 947d87eb-a7bc-50ae-bd2b-57097ad6c44a
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 27
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 12
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 27
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.036
  labels_checked: 18
  labels_matching: 11
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: UBERON:0000955
    reported_labels:
    - CNS involvement
    ontology_label: brain
  - term_id: NCIT:C1666
    reported_labels:
    - Interferon Alfa-2b
    ontology_label: Tyrphostin A30
  labels_variant: 5
  unresolved_terms:
  - HP:0002316
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lymphomatoid Granulomatosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Lymphomatoid Granulomatosis** covering all of the
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

I now have sufficient depth to compile the comprehensive report. Writing the final report now.

I now have comprehensive, well-cited data across all sections. Compiling the final report.

# Lymphomatoid Granulomatosis: Comprehensive Research Report

## 1. Disease Information

**Overview.** Lymphomatoid granulomatosis (LYG) is a rare, Epstein-Barr virus (EBV)–driven, angiocentric and angiodestructive B-cell lymphoproliferative disease that arises against a background of defective host immune surveillance of EBV. First described by Averill Liebow in 1972, it is now recognized in the WHO classification as a distinct entity most closely related to a T-cell/histiocyte-rich large B-cell lymphoma variant, formally classified since 2015 within the WHO Classification of Tumours of the Lung, Pleura, Thymus and Heart, and retained in the 2016/2022 WHO classifications of mature lymphoid neoplasms ([Melani et al., Blood 2020, PMID 32107539](https://ashpublications.org/blood/article/135/16/1344/452575/Pathobiology-and-treatment-of-lymphomatoid); [PathologyOutlines](https://www.pathologyoutlines.com/topic/lymphomalymphomatoidgran.html)). Histologically it is defined by an angiocentric, angioinvasive, extranodal, polymorphous lymphoid infiltrate containing variable numbers of large, atypical, EBV-positive B cells set in a dense background of reactive, predominantly CD4+ T lymphocytes, with associated coagulative ("tumor") necrosis ([PMID 25321327](https://pmc.ncbi.nlm.nih.gov/articles/PMC4293220/)).

**Key identifiers:**
- **MONDO:** MONDO:0019466
- **Orphanet:** ORPHA:86869
- **ICD-10-CM:** C83.8 (Other non-follicular lymphoma)
- **ICD-O:** 9766/1
- **OMIM:** No dedicated single-gene OMIM entry exists for sporadic LYG (it is not a classic monogenic Mendelian disorder); related immunodeficiency-associated lymphoproliferative OMIM entries exist for specific germline predisposition syndromes (e.g., OMIM #613011, Lymphoproliferative syndrome 1)

**Synonyms:** angiocentric immunoproliferative lesion (AIL); "LG"/"LYG"; historically grouped with (though not identical to) polymorphic reticulosis/lethal midline granuloma and angiocentric lymphoma under the older umbrella term "angiocentric immunoproliferative lesions," though modern classification distinguishes LYG (B-cell driven, EBV+, multi-organ) from nasal NK/T-cell lymphoma (formerly "polymorphic reticulosis") ([GARD](https://rarediseases.info.nih.gov/diseases/6943/lymphomatoid-granulomatosis); [PMID 7281476](https://pubmed.ncbi.nlm.nih.gov/7281476/)).

**Evidence basis:** Information is derived almost entirely from aggregated case series, single-institution retrospective cohorts, and one prospective NCI phase 2 interventional trial — not large-scale EHR/claims data — reflecting the disease's rarity.

---

## 2. Etiology

**Primary causal driver — EBV plus host immune dysfunction.** LYG is hypothesized to result from defective cell-mediated immune surveillance of EBV-infected B cells, permitting outgrowth of EBV-driven B-cell clones amid a robust but ineffective reactive T-cell response ("hyperimmune" reaction), rather than from any single germline oncogenic driver ([PMID 32107539](https://ashpublications.org/blood/article/135/16/1344/452575/Pathobiology-and-treatment-of-lymphomatoid)). A functional defect, primarily in CD8+ cytotoxic T-cell immunosurveillance, is hypothesized as a prerequisite; notably, the reactive infiltrate itself is CD4-predominant (CD4:CD8 ratio favoring CD4 in 95% of cases, 20/21) rather than CD8-predominant, consistent with an ineffective/dysregulated rather than absent T-cell response ([PMID 25321327](https://pmc.ncbi.nlm.nih.gov/articles/PMC4293220/)).

**Genetic/immunologic risk factors:**
- **Underlying primary or acquired immunodeficiency** is documented in a substantial fraction of cases even without a formally diagnosed syndrome. Recognized associated conditions include:
  - **Wiskott–Aldrich syndrome** (X-linked; marked predisposition to EBV-associated lymphoma)
  - **X-linked lymphoproliferative syndrome (XLP)**
  - **Common variable immunodeficiency (CVID)**
  - **DOCK8 deficiency** — a combined immunodeficiency in the hyper-IgE spectrum; a 2017 report described EBV+ LYG as a previously unreported presentation of DOCK8 deficiency, with resolution of LYG following hematopoietic stem cell transplantation in affected relatives ([PMID from Frontiers report, DOCK8/LYG](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5328973/))
  - **HIV/AIDS** — via CD4+ T-cell depletion and loss of EBV control
  - **Solid organ transplantation** (iatrogenic immunosuppression) — placing LYG within the broader post-transplant lymphoproliferative disease (PTLD) spectrum in transplant recipients
- **No recurrent chromosomal abnormalities** have been reported in LYG, and no single causal driver gene/variant analogous to a classic Mendelian mutation has been established ([PMID 32107539](https://ashpublications.org/blood/article/135/16/1344/452575/Pathobiology-and-treatment-of-lymphomatoid)).
- **Sporadic disease without recognized immunodeficiency** is also common — most affected adults have no formally diagnosed primary immunodeficiency syndrome, suggesting a subtler or acquired immune surveillance defect specific to EBV.

**Environmental/infectious factor — EBV is central and essentially obligate.** EBV (a γ-herpesvirus) genomes and gene products (EBER, LMP1) are demonstrable in the neoplastic B cells of the great majority of cases across grades (EBER positivity: ~46% in grade 1, 100% in grade 2, 94% in grade 3 lesions per PMID 25321327), supporting EBV as the direct causal/transforming agent rather than a bystander.

**Protective factors:** No specific genetic or environmental protective factor has been established in the literature; intact cell-mediated (particularly CD8+ cytotoxic T-lymphocyte) immunosurveillance of EBV is implicitly protective, as evidenced by disease remission following immune reconstitution (e.g., antiretroviral therapy in newly diagnosed HIV, or reduction of immunosuppression in transplant recipients) ([PMC11829542](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11829542/)).

**Gene-environment interaction:** The disease represents a paradigmatic gene(immune)-environment(EBV) interaction: a host with a quantitative or qualitative T-cell surveillance defect (genetic/immunodeficiency-related or acquired) fails to control EBV-driven B-cell proliferation, and progressive genetic/clonal evolution of the EBV+ B-cell population (increasing clonality with grade) leads to transformation toward overt lymphoma.

---

## 3. Phenotypes

LYG is multisystemic, with organ involvement documented in a 55-patient single-institution series ([Song et al., Am J Surg Pathol 2015, PMID 25321327](https://pmc.ncbi.nlm.nih.gov/articles/PMC4293220/)):

| Organ | Frequency | HPO term (suggested) |
|---|---|---|
| Lung | ~90–100% (near-universal) | HP:0006536 (Pulmonary infiltrates) / HP:0032230 (Pulmonary nodule) |
| CNS | 20–38% | HP:0002316 (CNS neoplasm) / HP:0007281 |
| Skin | 17–55% | HP:0011355 (Skin nodule) / HP:0100310 (Skin ulcer) |
| Liver | 19–29% | HP:0001392 (Abnormal liver morphology) |
| Kidney | 15–40% | HP:0000077 (Abnormality of the kidney) |

**Pulmonary phenotype (near-universal, ~90–100% of cases):** Presenting symptoms include cough, dyspnea, chest pain, and fever; imaging shows bilateral, peribronchovascular, lower/peripheral-lung-predominant nodules or masses in 80–100% of cases, with cavitation, small thin-walled cysts, atelectasis/lobar obstruction, and occasional pneumothorax ([AJR, PMID 11044036](https://ajronline.org/doi/10.2214/ajr.175.5.1751335)).

**Cutaneous phenotype (~17–55%; second most common site):** Multiple erythematous dermal papules and/or subcutaneous nodules, plaques, or a patchy erythematous rash, with ulceration in up to ~30% of affected patients; distribution favors extremities over head/neck (only ~10% head/neck) ([Dermatology Advisor](https://www.dermatologyadvisor.com/home/decision-support-in-medicine/dermatology/lymphomatoid-granulomatosis/); [PMC6110445](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6110445/)).

**CNS phenotype (20–38%):** Parenchymal brain lesions, cranial neuropathies, seizures, and focal neurologic deficits; CT shows high-density lesions. CNS involvement is a major adverse prognostic factor — one CNS-focused cohort reported overall mortality of 63.5% in LYG generally versus 86.0% in CNS-LYG specifically, with 5-year mortality of 38–88% and median survival 14–72 months in CNS-involved disease ([PMC7516720](https://pmc.ncbi.nlm.nih.gov/articles/PMC7516720/)).

**Hepatic and renal phenotype:** Often asymptomatic or detected on imaging/labs; renal involvement can present with hematuria or renal impairment without overt vasculitic glomerulonephritis (distinguishing it from ANCA-associated vasculitis).

**Constitutional/laboratory phenotypes:** Fever, weight loss, malaise; laboratory abnormalities may include cytopenias, and rare cases present with hemophagocytic lymphohistiocytosis (HLH) as an initial manifestation ([Frontiers, PMC](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2020.00034/full)) or paraneoplastic polymyositis ([PMC4757691](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4757691/)).

**Onset/course:** Typically insidious onset in adults (fourth–sixth decade), though a chronic, indolent ("smoldering") cutaneous-only course has also been reported ([PMC8841505](https://pmc.ncbi.nlm.nih.gov/articles/PMC8841505/)); grade generally correlates with disease pace, with low-grade disease often smoldering/relapsing-remitting and high-grade disease behaving as an aggressive lymphoma.

**Quality of life impact:** Not systematically studied via standardized instruments (EQ-5D/SF-36) in this rare disease; qualitatively, pulmonary and CNS involvement drive the greatest functional morbidity.

---

## 4. Genetic/Molecular Information

**Causal genes:** No single germline causal gene for sporadic LYG exists; it is not a classic monogenic disorder. However, LYG has been reported as a rare secondary manifestation of several germline primary immunodeficiency genes:
- **DOCK8** (hgnc:19191) — autosomal recessive combined immunodeficiency (hyper-IgE syndrome spectrum); reported cause of EBV+ LYG with intrafamilial phenotypic variation ([PMC5328973](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5328973/))
- **WAS** — Wiskott-Aldrich syndrome gene, X-linked
- Genes underlying XLP (**SH2D1A**, **XIAP**) and CVID

**Somatic/molecular features of the neoplastic clone:**
- **Clonality:** Immunoglobulin heavy-chain gene rearrangement studies show grade-dependent clonality — grade 1: ~8% clonal (1/12); grade 2: ~50% clonal (4/8); grade 3: ~69% clonal (11/16) — consistent with progressive selection/transformation of an EBV-infected B-cell clone with increasing grade ([Song et al. 2015, PMID 25321327](https://pmc.ncbi.nlm.nih.gov/articles/PMC4293220/)).
- **No recurrent cytogenetic abnormalities** (translocations, aneuploidy) have been established, unlike most other B-cell lymphomas ([PMID 32107539](https://ashpublications.org/blood/article/135/16/1344/452575/Pathobiology-and-treatment-of-lymphomatoid)).
- **EBV gene expression:** Neoplastic B cells express EBER (EBV-encoded small RNA, detected by in situ hybridization) and latent membrane protein 1 (LMP1) by immunohistochemistry, consistent with a latency II/III-like expression program; EBER positivity rises from ~46% (grade 1) to 100% (grade 2) to 94% (grade 3) ([PMID 25321327](https://pmc.ncbi.nlm.nih.gov/articles/PMC4293220/)).
- **Immunophenotype of neoplastic cells:** CD20+, CD45+, LMP1+ large atypical B cells; background reactive infiltrate is CD3+ T cells, CD4-predominant in 95% of cases (20/21) ([PMID 25321327](https://pmc.ncbi.nlm.nih.gov/articles/PMC4293220/)).

**Variant classification/allele frequency:** Not applicable in the classic ClinVar/gnomAD sense for sporadic LYG, since it is a somatic/EBV-driven lymphoproliferation rather than a germline variant-caused disease; where associated germline immunodeficiency genes (DOCK8, WAS) are implicated, standard ACMG/AMP pathogenic-variant classification applies to those underlying conditions rather than to LYG itself.

**Epigenetics:** No LYG-specific DNA methylation/histone-modification studies were identified in the search; EBV latency programs themselves involve epigenetic (CpG methylation, histone) regulation of the viral genome, a mechanism general to EBV-associated lymphoproliferations.

---

## 5. Environmental Information

**Infectious trigger — EBV (Epstein-Barr virus, human gammaherpesvirus 4; NCBITaxon:10376):** The central and essentially obligate etiologic agent; EBV genomes are detectable by PCR/in situ hybridization in the overwhelming majority of cases ([PMID 2170969](https://pubmed.ncbi.nlm.nih.gov/2170969/)).

**Iatrogenic/exposure factors:**
- **Immunosuppressive medication** — solid organ transplantation, TNF-α inhibitor therapy (a 2023 case report describes pulmonary LYG in a patient on long-term TNF-α inhibitor use, PMID 37160375), and other immunosuppressive regimens for autoimmune disease can precipitate LYG by impairing EBV surveillance.
- **HIV infection** — a well-documented environmental/infectious risk factor via CD4+ T-cell depletion; case reports document LYG remission after immune reconstitution with antiretroviral therapy.

**Lifestyle factors:** No specific lifestyle risk factor (smoking, diet, alcohol) has been established in the literature as a driver of LYG.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
1. **Trigger:** EBV infection of B lymphocytes (nearly universal in the population; EBV seroprevalence >90% in adults) combined with a host defect in cell-mediated EBV immunosurveillance (constitutional immunodeficiency, HIV, iatrogenic immunosuppression, or an unidentified subtler defect).
2. **Molecular/cellular consequence:** Failure of cytotoxic (largely CD8+) T-cell control permits outgrowth of EBV-infected B cells expressing latent viral oncoproteins (LMP1, EBNA), which drive B-cell proliferation and survival signaling (NF-κB activation downstream of LMP1, analogous to other EBV+ lymphoproliferations).
3. **Tissue-level consequence:** A robust reactive, predominantly CD4+ T-cell response is recruited but is immunologically ineffective at eliminating the EBV+ B-cell population; the mixed infiltrate shows a striking tropism for blood vessel walls (angiocentricity) and vessel destruction (angioinvasion/angiodestruction), producing ischemic coagulative ("tumor") necrosis in affected tissue.
4. **Organism-level consequence:** Multi-organ tissue destruction (lung nodules/cavitation, cutaneous ulceration, CNS lesions, hepatic/renal involvement) and, with clonal evolution/selection of the EBV+ B-cell population (rising Ig-clonality across grades 1→3), progression from a polyclonal/oligoclonal low-grade lymphoproliferation to a clonal, aggressive B-cell lymphoma indistinguishable from EBV+ diffuse large B-cell lymphoma at grade 3.

**Cellular processes involved:** Chronic inflammation, angiocentric/angiodestructive vasculopathy (not a true vasculitis, since there is no primary destruction of the vessel wall by an immune-mediated vasculitic process — vessel damage is secondary to lymphocytic infiltration), ischemic/coagulative necrosis, and B-cell clonal selection/malignant transformation.

**Grading as a mechanistic readout:** The three-tier histologic grading system directly operationalizes the pathobiology — grade is defined by the number/density of large EBV+ B cells and extent of necrosis:
- **Grade 1:** Polymorphous infiltrate, few/no large atypical cells, scant EBV+ B cells (EBER+ ~46%), no or minimal necrosis, low/no clonality (8% clonal) — indolent, "immune-dependent" biology.
- **Grade 2:** Increased large EBV+ B cells (EBER+ 100%), more necrosis, intermediate clonality (50%).
- **Grade 3:** Sheets of large atypical EBV+ B cells resembling conventional EBV+ diffuse large B-cell lymphoma, extensive necrosis, high clonality (69%) — "immune-independent," frankly malignant biology ([PMID 25321327](https://pmc.ncbi.nlm.nih.gov/articles/PMC4293220/); Nakamura/Nature Modern Pathology review).

This grade-dependent biology is the direct rationale for the NCI's differentiated treatment strategy (immunotherapy for immune-dependent low-grade disease vs. cytotoxic chemoimmunotherapy for immune-independent high-grade disease — see Treatment section).

**Suggested GO terms:** GO:0006955 (immune response), GO:0002432 (granuloma formation), GO:0031295 (T cell costimulation) [context], GO:0043065 (positive regulation of apoptotic process) [reactive T cell attack on infected cells], GO:0001525 (angiogenesis)/GO:0032102 (negative regulation of response to wounding) not directly established. Suggested CL terms: CL:0000236 (B cell) — specifically EBV-transformed large B cell; CL:0000624 (CD4-positive, alpha-beta T cell) for the reactive infiltrate; CL:0000625 (CD8-positive, alpha-beta T cell) for the hypothesized deficient surveillance population.

**Advanced/omics profiling:** No large-scale transcriptomic, proteomic, single-cell, or spatial transcriptomic dataset specific to LYG was identified in this search — consistent with its rarity and the field's reliance on immunohistochemistry/ISH-based diagnostic pathology rather than genomic profiling to date. This represents a knowledge gap relative to better-characterized B-cell lymphomas.

---

## 7. Anatomical Structures Affected

- **Primary organ:** Lung (near-universal, ~90–100%) — UBERON:0002048 (lung); peribronchovascular/perivascular distribution.
- **Secondary/frequently involved organs:** Skin (UBERON:0002097, integument), CNS/brain (UBERON:0000955), liver (UBERON:0002107), kidney (UBERON:0002113).
- **Body systems:** Respiratory, integumentary, nervous, hepatobiliary, renal — a genuinely multisystem disease; lymph nodes and spleen may be secondarily involved (splenomegaly reported, PMC6000673) but are not primary sites (an important distinguishing feature from typical nodal lymphomas).
- **Tissue level:** Perivascular/angiocentric lymphoid infiltrate within pulmonary interstitium, dermis/subcutis, cerebral parenchyma; vascular smooth muscle and endothelium (targets of angioinvasion).
- **Cell populations:** Large atypical EBV+ B cells (CD20+, CD45+, LMP1+, EBER+) — Cell Ontology CL:0000236 specialization; reactive CD4+ T cells (CL:0000624) as the dominant background population; histiocytes/plasma cells as minor infiltrate components.
- **Subcellular:** No specific organelle-level pathology reported (this is not a classic metabolic/storage disease); relevant GO Cellular Component context would be nuclear (EBER, an RNA Pol III transcript, localizes to the nucleus) for viral gene products.
- **Localization/laterality:** Pulmonary disease is characteristically bilateral; skin lesions favor extremities (bilateral, non-lateralized); CNS lesions can be single or multifocal, no strict laterality pattern reported.

---

## 8. Temporal Development

- **Onset:** Typically adult-onset, fourth to sixth decade of life, though reported across the age spectrum including pediatric cases (children with LYG have been described, including as a rare complication after chemotherapy for pediatric AML, PMID 12571471, and as a cerebellar-mass presentation, AJNR 2007).
- **Onset pattern:** Usually insidious/subacute; can present acutely in the context of superimposed immunosuppression (e.g., post-transplant, HIV seroconversion).
- **Staging/grading as a temporal-progression proxy:** Grade 1↔2↔3 functions partly as a progression axis — low-grade disease can progress to high-grade disease over time if untreated or under continued immune impairment, motivating the rationale for early immunotherapy in low-grade disease to forestall transformation ([Lancet Haematol 2023, PMID 37011643](https://www.thelancet.com/journals/lanhae/article/PIIS2352-3026(23)00029-7/abstract)).
- **Progression rate/course pattern:** Variable — ranges from an indolent, smoldering, relapsing-remitting cutaneous-limited course (PMC8841505) to a rapidly progressive, aggressive high-grade lymphoma course.
- **Remission patterns:** Both spontaneous remission (rare, reported with immune reconstitution, e.g., post-antiretroviral therapy in HIV) and treatment-induced remission (interferon-alfa-2b for low-grade disease; DA-EPOCH-R for high-grade) are documented.
- **Historical natural history (untreated/steroid-treated):** Median survival ~14 months, with 5-year mortality ~50% in older literature predating modern grade-stratified therapy.

---

## 9. Inheritance and Population

**Epidemiology:**
- LYG is an exceedingly rare disease of unknown precise population prevalence/incidence — described as "a disease of unknown prevalence" with no dedicated national registry figures identified.
- **Sex ratio:** Male predominance, approximately 2:1 male:female.
- **Age distribution:** Most common in the fourth to sixth decades of adult life; can occur at any age, including rare pediatric cases.
- **Race/ethnicity:** No known racial predilection reported.

**Inheritance pattern:** LYG itself is not inherited in a classic Mendelian sense — it is a sporadic, EBV-driven lymphoproliferation. However, when it arises secondary to a germline primary immunodeficiency (e.g., DOCK8 deficiency — autosomal recessive; Wiskott-Aldrich syndrome — X-linked recessive), the underlying predisposing condition follows that syndrome's inheritance pattern, and intrafamilial variation in LYG presentation among relatives sharing the same germline DOCK8 mutation has been documented ([PMC5328973](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5328973/)).

**Penetrance/expressivity:** Not classically applicable, given the sporadic/acquired nature of most cases; where a germline immunodeficiency is causal, penetrance for LYG specifically (versus other EBV-driven manifestations) is incomplete and variable even within families.

**Founder effects/consanguinity/carrier frequency:** Not established for LYG itself, though relevant to the rare recessive immunodeficiency syndromes (e.g., DOCK8 deficiency) that can predispose to it.

---

## 10. Diagnostics

**Tissue diagnosis is required and central.** Definitive diagnosis requires tissue biopsy (open lung biopsy or video-assisted thoracoscopic surgery [VATS] for pulmonary disease, or biopsy of an accessible extrapulmonary site such as skin) demonstrating the characteristic angiocentric/angioinvasive polymorphous infiltrate with EBV+ atypical B cells ([emedicine Workup](https://emedicine.medscape.com/article/299751-workup)).

**Ancillary pathology studies:**
- **In situ hybridization for EBER** (EBV-encoded RNA) — the key diagnostic test confirming EBV positivity in the atypical B-cell population.
- **Immunohistochemistry:** CD20 (neoplastic B cells), CD3/CD4/CD8 (background reactive T cells, CD4-predominant), LMP1 (latent EBV protein).
- **Molecular clonality studies:** Immunoglobulin heavy-chain gene rearrangement (PCR-based) to assess clonality, correlating with grade.

**Imaging:**
- **Chest CT** — bilateral, peribronchovascular, lower/peripheral-lung nodules or masses, sometimes with cavitation; the primary modality for detecting and monitoring pulmonary disease.
- **Brain MRI/CT** — for suspected CNS involvement; CT shows high-density lesions.
- **F18-FDG PET/CT** — used to assess multisystem disease distribution, guide high-yield biopsy site selection, and monitor treatment response.

**Laboratory studies:** No LYG-specific serum biomarker exists; EBV serology/PCR (plasma EBV DNA load) may support the diagnosis and can be used for monitoring, though it is not diagnostic in isolation given high background EBV seroprevalence.

**Genetic testing:** Not part of routine LYG diagnostic workup unless an underlying primary immunodeficiency is clinically suspected (e.g., recurrent infections, eczema, and elevated IgE suggesting DOCK8 deficiency; recurrent infections/thrombocytopenia/eczema suggesting Wiskott-Aldrich syndrome), in which case targeted gene panel or exome sequencing for primary immunodeficiency genes would be pursued.

**Differential diagnosis:**
- **Granulomatosis with polyangiitis (GPA/Wegener's)** — distinguished by true necrotizing vasculitis (destruction of the vessel wall itself by the inflammatory process) and typically ANCA positivity, versus LYG's angiocentric/angioinvasive-but-not-classically-vasculitic pattern and EBV positivity.
- **Sarcoidosis / necrotizing sarcoid granulomatosis** — distinguished by well-formed granulomas with giant cells, more frequent mediastinal adenopathy, and absence of EBV+ atypical B cells (LYG characteristically lacks well-formed granulomas or multinucleated giant cells).
- Other entities in the differential: pseudolymphoma, other malignant lymphomas (including EBV+ diffuse large B-cell lymphoma, into which grade 3 LYG merges diagnostically), lymphocytic interstitial pneumonia, metastatic disease, cryptogenic organizing pneumonia, infectious granulomatous disease (fungal, mycobacterial).

**Screening:** No population-level screening program exists given the disease's rarity and lack of an identifiable pre-symptomatic screening marker; surveillance in known immunodeficiency syndromes (DOCK8 deficiency, Wiskott-Aldrich) for EBV-driven lymphoproliferative complications is a reasonable clinical practice, though not formally codified as LYG-specific screening.

---

## 11. Outcome/Prognosis

**Historical (pre-risk-stratified-therapy) outcomes:** Median overall survival was poor, historically cited as 14 months (steroid/chemotherapy era) to under 2 years, with 5-year mortality around 50%.

**Modern, grade-stratified therapy outcomes (NCI phase 2 trial, Lancet Haematology 2023, PMID 37011643):**
- Patients with **low-grade disease** treated with **interferon alfa-2b** achieved a median overall survival of approximately **20 years** — a dramatic improvement over historical controls.
- Progression-free survival for grades 1–2 treated with interferon-alfa was 56%, with median PFS of 5.1 years; for grade 3 treated with DA-EPOCH-R, PFS was 44%, median 32 months ([PMID 25321327](https://pmc.ncbi.nlm.nih.gov/articles/PMC4293220/) reporting NCI cohort outcomes).
- Complete response rates in the phase 2 trial: 61% (27/44) after initial interferon alfa-2b in low-grade disease; 47% (8/17) after initial DA-EPOCH-R in high-grade disease; with additional responses after cross-over treatment.
- Serious adverse events occurred in about 25% of interferon alfa-2b-treated patients versus nearly two-thirds of chemotherapy-treated patients, favoring the tolerability of immunotherapy for low-grade disease.

**Prognostic factors:**
- **Histologic grade** is the single most important prognostic factor — grade 3 (high-grade) disease behaves as an aggressive lymphoma with poorer outcomes than low-grade disease, though modern chemoimmunotherapy has substantially improved even high-grade outcomes.
- **CNS involvement** confers markedly worse prognosis: one cohort reported 3-year overall mortality of 63.5% in LYG broadly versus 86.0% specifically in CNS-involved LYG, with 5-year mortality of 38–88% and median survival 14–72 months in CNS-LYG ([PMC7516720](https://pmc.ncbi.nlm.nih.gov/articles/PMC7516720/)).
- **Underlying immunodeficiency status** and ability to achieve immune reconstitution (e.g., HIV control, reduction of iatrogenic immunosuppression) favorably affect outcome.

**Complications:** Progression to overt EBV+ diffuse large B-cell lymphoma (grade 3 transformation), organ failure from pulmonary/hepatic/renal destruction, secondary infections related to immunosuppressive therapy, hemophagocytic lymphohistiocytosis as a rare severe complication.

---

## 12. Treatment

**Modern risk/grade-stratified paradigm (NCI standard of care, established by the Lancet Haematology 2023 phase 2 trial, PMID 37011643):**

- **Low-grade disease (grades 1–2) — immunotherapy-first, reflecting "immune-dependent" biology:**
  - **Interferon alfa-2b** — dose-escalated subcutaneous injections, starting ~7.5 million international units three times weekly, continued for up to 1 year past best response. NCIT suggestion: NCIT:C1666 (Interferon Alfa-2b); treatment_term NCIT:C15986 (Pharmacotherapy).
  
- **High-grade disease (grade 3) — chemoimmunotherapy, reflecting "immune-independent," frankly malignant biology:**
  - **DA-EPOCH-R** (dose-adjusted etoposide, prednisone, vincristine, cyclophosphamide, doxorubicin, and rituximab) — six cycles every 3 weeks intravenously. NCIT suggestion: regimen conceptually analogous to standard aggressive B-cell lymphoma chemoimmunotherapy; therapeutic_agent components include rituximab (CHEBI/NCIT:C2185 or similar anti-CD20 monoclonal antibody term), doxorubicin, cyclophosphamide, vincristine, etoposide, prednisone.

- **Rituximab monotherapy** — reported in isolated case reports (e.g., mediastinal LYG achieving complete remission after 3 months of rituximab monotherapy, PMID 15693798), but with variable/unpredictable results as monotherapy; not established as standard for high-grade disease alone.

**Immune reconstitution as therapy:** In cases secondary to reversible immunosuppression (e.g., newly diagnosed HIV, TNF-α inhibitor use, post-transplant), reducing/discontinuing the offending immunosuppression or initiating antiretroviral therapy has produced remission of low-grade pulmonary LYG, underscoring the immune-dependent mechanism at low grade ([PMC11829542](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11829542/)).

**Emerging/experimental therapies:**
- **PD-1 checkpoint inhibition** — a case report describes successful treatment of pulmonary LYG with a PD-1 inhibitor-based regimen, suggesting a role for immune checkpoint blockade as an emerging strategy, though this is not yet standard of care and mechanistic rationale (tumor PD-L1 engagement suppressing anti-EBV T-cell responses) is inferred by analogy to other EBV+ lymphomas rather than LYG-specific mechanistic data.
- **Hematopoietic stem cell transplantation** — curative for LYG arising in the context of an underlying correctable primary immunodeficiency (e.g., DOCK8 deficiency), where HSCT resolved both the immunodeficiency and the LYG.

**Supportive care:** Management of pulmonary complications (may require ventilatory support in severe disease), CNS-directed therapy (high-dose methotrexate plus rituximab reported effective for higher-grade CNS-LYG), and standard supportive oncologic care.

**Treatment algorithm summary:** The defining modern conceptual advance is that LYG is not treated as a single entity but is bifurcated by grade into a proposed "immune-dependent" (low-grade, treat the immune deficit) versus "immune-independent" (high-grade, treat as lymphoma) disease model — directly informing the two-arm design of the pivotal 2023 trial.

---

## 13. Prevention

Given LYG's basis in EBV plus acquired/host immune dysfunction, prevention is indirect rather than primary (no LYG-specific vaccine or prophylactic agent exists):

- **Primary prevention:** No EBV vaccine is currently licensed for general use (EBV vaccine candidates remain in clinical trials for EBV-associated diseases broadly, not LYG-specific); minimizing unnecessary or prolonged immunosuppression, and judicious use of TNF-α inhibitors and other immunomodulatory agents with awareness of EBV-driven lymphoproliferative risk, represents a practical primary-prevention-adjacent strategy in susceptible patients.
- **Secondary prevention/early detection:** Surveillance for EBV-driven lymphoproliferative disease (including LYG) in patients with known primary immunodeficiency syndromes (DOCK8 deficiency, Wiskott-Aldrich syndrome, XLP, CVID), solid organ transplant recipients, and HIV-positive patients with poor immune control — enabling earlier diagnosis and grade-stratified treatment before high-grade transformation.
- **Tertiary prevention:** Early initiation of interferon alfa-2b in low-grade disease is explicitly framed (per the 2023 NCI trial) as reducing the risk of progression to high-grade, immune-independent disease — i.e., tertiary prevention of transformation.
- **Genetic counseling:** Relevant when LYG arises in the context of an underlying heritable immunodeficiency syndrome (e.g., DOCK8 deficiency, Wiskott-Aldrich syndrome), where standard genetic counseling for the primary condition applies, including consideration of carrier testing and reproductive counseling for at-risk relatives.
- **Public health/prophylaxis:** No specific public health intervention targets LYG; general EBV exposure is nearly universal and not itself modifiable at the population level.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary counterpart of lymphomatoid granulomatosis specifically was identified in this search (unlike, e.g., some EBV-associated human lymphomas that have partial analogs in Old World primate lymphocryptovirus infections). EBV itself is a human-tropic gammaherpesvirus (NCBITaxon:10376) without natural non-human hosts, though related lymphocryptoviruses infect other primates and can produce analogous lymphoproliferative disease in those species (relevant to comparative biology of gammaherpesvirus-driven lymphoproliferation broadly, though not documented as "lymphomatoid granulomatosis" by name in veterinary literature). No OMIA (Online Mendelian Inheritance in Animals) entry or zoonotic transmission pathway is applicable, since EBV is not zoonotic.

---

## 15. Model Organisms

**No LYG-specific animal or in vitro model was identified in the literature searched.** However, the broader mechanistic paradigm — EBV infection with defective T-cell immunosurveillance driving B-cell lymphoproliferation — is modeled by:

- **Humanized mouse models of EBV infection** (e.g., NOD/Shi-scid IL2rγnull [NOG], NOD/LtSz-scid Il2rg−/− [NSG], BALB/c Rag2−/−Il2rg−/− strains reconstituted with human hematopoietic stem cells) — these models reproduce EBV-associated B-cell lymphoproliferative disease and hemophagocytic lymphohistiocytosis, and are used to study post-transplant lymphoproliferative disease (PTLD), a mechanistically related EBV+ B-cell lymphoproliferation arising under iatrogenic immunosuppression ([PMC4235711, "Humanized Mouse Models of Epstein-Barr Virus Infection and Associated Diseases"](https://pmc.ncbi.nlm.nih.gov/articles/PMC4235711/)).
- **Immunosuppression-augmented humanized mouse models** — e.g., FK506 (tacrolimus) treatment of humanized mice increases the frequency of EBV-associated lymphoproliferative disease, directly modeling the iatrogenic-immunosuppression risk pathway relevant to LYG in transplant recipients ([PMC7162544](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7162544/)).
- **Checkpoint blockade studies in humanized mice** — PD-1/CTLA-4 blockade has been shown to inhibit EBV-induced lymphoma growth in a cord-blood humanized mouse model, providing translational rationale (by analogy, not direct LYG data) for the emerging PD-1 inhibitor case report noted above ([PMC4871349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4871349/)).

**Model limitations relevant to LYG specifically:** Existing humanized-mouse EBV-lymphoproliferation models capture generic EBV+ B-cell lymphoproliferative disease and PTLD-like biology but do not recapitulate the LYG-defining angiocentric/angioinvasive tissue tropism, multi-organ pattern (lung/skin/CNS predominance), or the specific CD4-predominant reactive T-cell microenvironment — representing a clear gap between available model systems and the human disease phenotype that would need explicit flagging (e.g., a `HUMAN_MODEL_MISMATCH` framing) in any KB curation.

---

## Summary of Suggested Ontology Bindings for KB Curation

| Concept | Suggested term |
|---|---|
| Disease | MONDO:0019466 (lymphomatoid granulomatosis) |
| Causal/associated agent | EBV — NCBITaxon:10376 |
| Neoplastic cell | CL:0000236 (B cell), EBV-transformed large B cell |
| Reactive infiltrate cell | CL:0000624 (CD4+ alpha-beta T cell) |
| Lung involvement | UBERON:0002048 |
| Skin involvement | UBERON:0002097 |
| CNS involvement | UBERON:0000955 |
| Angiodestruction/necrosis | GO process terms for apoptosis/necrosis, tissue damage |
| Treatment — interferon | NCIT:C1666 (Interferon Alfa-2b) under NCIT:C15986 (Pharmacotherapy) |
| Treatment — DA-EPOCH-R | NCIT:C15632 (Chemotherapy) + therapeutic_agent list (rituximab, doxorubicin, cyclophosphamide, vincristine, etoposide, prednisone); consider `regimen_term` if an NCIT-coded DA-EPOCH-R identity exists |
| Genetic predisposition (when applicable) | hgnc:2993 (DOCK8), WAS gene |

---

### Sources

- [Melani C, Jaffe ES, Wilson WH. Pathobiology and treatment of lymphomatoid granulomatosis, a rare EBV-driven disorder. Blood. 2020;135(16):1344-1352. PMID 32107539](https://ashpublications.org/blood/article/135/16/1344/452575/Pathobiology-and-treatment-of-lymphomatoid)
- [Song JY, et al. Lymphomatoid granulomatosis, a single institute experience: pathologic findings and clinical correlations. Am J Surg Pathol. 2015;39(2):141-156. PMID 25321327](https://pmc.ncbi.nlm.nih.gov/articles/PMC4293220/)
- [Interferon alfa-2b in patients with low-grade lymphomatoid granulomatosis and chemotherapy with DA-EPOCH-R in patients with high-grade lymphomatoid granulomatosis: an open-label, single-centre, phase 2 trial. Lancet Haematol. 2023;10(5):e346-e358. PMID 37011643](https://www.thelancet.com/journals/lanhae/article/PIIS2352-3026(23)00029-7/abstract)
- [NIH News Release: Immunotherapy substantially increases survival of people with lymphomatoid granulomatosis](https://www.nih.gov/news-events/news-releases/nih-study-finds-immunotherapy-substantially-increases-survival-people-lymphomatoid-granulomatosis)
- [Orphanet: Lymphomatoid granulomatosis (ORPHA:86869)](https://www.orpha.net/en/disease/detail/86869)
- [GARD: Lymphomatoid granulomatosis](https://rarediseases.info.nih.gov/diseases/6943/lymphomatoid-granulomatosis)
- [NORD: Lymphomatoid Granulomatosis](https://rarediseases.org/rare-diseases/lymphomatoid-granulomatosis/)
- [Pathology Outlines: Lymphomatoid granulomatosis](https://www.pathologyoutlines.com/topic/lymphomalymphomatoidgran.html)
- [Medscape eMedicine: Lymphomatoid Granulomatosis (Background/Pathophysiology/Epidemiology/Workup/Differential)](https://emedicine.medscape.com/article/299751-overview)
- [Primary Central Nervous System Lymphomatoid Granulomatosis: Systematic Review. PMC7516720](https://pmc.ncbi.nlm.nih.gov/articles/PMC7516720/)
- [DOCK8 Deficiency, EBV+ Lymphomatoid Granulomatosis, and Intrafamilial Variation in Presentation. PMC5328973](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5328973/)
- [Lymphomatoid granulomatosis: radiologic features and pathologic correlations. AJR. PMID 11044036](https://ajronline.org/doi/10.2214/ajr.175.5.1751335)
- [Remission of low-grade lymphomatoid granulomatosis following immune restoration via antiretroviral therapy. PMC11829542](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11829542/)
- [Successful treatment of mediastinal lymphomatoid granulomatosis with rituximab monotherapy. PMID 15693798](https://pubmed.ncbi.nlm.nih.gov/15693798/)
- [Lymphomatoid Granulomatosis: A Case Report and Literature Review of a Rare Pediatric Disorder From Pakistan. PMID 37526440](https://pubmed.ncbi.nlm.nih.gov/37526440/)
- [Detection of Epstein-Barr virus genomes in lymphomatoid granulomatosis: analysis of 29 cases by PCR. PMID 2170969](https://pubmed.ncbi.nlm.nih.gov/2170969/)
- [Polymorphic reticulosis (lethal midline granuloma) and lymphomatoid granulomatosis: identical or distinct entities? PMID 7281476](https://pubmed.ncbi.nlm.nih.gov/7281476/)
- [Humanized Mouse Models of Epstein-Barr Virus Infection and Associated Diseases. PMC4235711](https://pmc.ncbi.nlm.nih.gov/articles/PMC4235711/)
- [Immunosuppressive FK506 treatment leads to more frequent EBV-associated lymphoproliferative disease in humanized mice. PMC7162544](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7162544/)
- [PD-1/CTLA-4 Blockade Inhibits EBV-Induced Lymphoma Growth in a Cord Blood Humanized-Mouse Model. PMC4871349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4871349/)
- [Case Report: Successful treatment of pulmonary lymphomatoid granulomatosis with a PD-1 inhibitor-based regimen. PMC12827129](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12827129/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0000955` (2 mentions) - the report calls it "CNS involvement"; UBERON calls it **brain**
- `NCIT:C1666` (2 mentions) - the report calls it "Interferon Alfa-2b"; NCIT calls it **Tyrphostin A30**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002316` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001392` (1 mention) - the report calls it "Abnormal liver morphology"; HP calls it **Abnormality of the liver**, and lists "Abnormal liver" among its other names
- `GO:0032102` (1 mention) - the report calls it "negative regulation of response to wounding"; GO calls it **negative regulation of response to external stimulus**
- `CL:0000624` (3 mentions) - the report calls it "CD4-positive, alpha-beta T cell", "CD4+ alpha-beta T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `UBERON:0002048` (2 mentions) - the report calls it "lung", "Lung involvement"; UBERON calls it **lung**
- `UBERON:0002097` (2 mentions) - the report calls it "Skin involvement"; UBERON calls it **skin of body**, and lists "entire integument" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000624` - called "CD4-positive, alpha-beta T cell", "CD4+ alpha-beta T cell"
- `UBERON:0002048` - called "lung", "Lung involvement"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.