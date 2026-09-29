---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-29T01:05:29.560816'
end_time: '2026-08-29T01:19:30.071281'
duration_seconds: 840.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Diaphyseal Medullary Stenosis with Malignant Fibrous Histiocytoma
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
  - claude-opus-5[1m]
  web_search_requests: 14
  num_turns: 64
  total_cost_usd: 5.0847935
  session_id: 30946671-fa89-4761-a67d-bfdb4fafb47f
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 1
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
citation_count: 37
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 19
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 81
  verified: 77
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 33
  labels_matching: 24
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0007205
    reported_labels:
    - MONDO
    - Monarch Initiative
    ontology_label: diaphyseal medullary stenosis-bone malignancy syndrome
  - term_id: DOID:0080664
    reported_labels:
    - Disease Ontology
    ontology_label: diaphyseal medullary stenosis with malignant fibrous histiocytoma
  - term_id: UBERON:0009859
    reported_labels:
    - "Endosteum \u2014 site of pathological apposition"
    ontology_label: endosteum
  - term_id: NCIT:C15329
    reported_labels:
    - For osteomyelitis complicating nonunion, or for unresectable tumor
    - Presenile cataracts
    ontology_label: Surgical Procedure
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  - MGI
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diaphyseal Medullary Stenosis with Malignant Fibrous Histiocytoma
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Diaphyseal Medullary Stenosis with Malignant Fibrous Histiocytoma** covering all of the
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

# Diaphyseal Medullary Stenosis with Malignant Fibrous Histiocytoma (DMS‑MFH / Hardcastle Syndrome)

**Comprehensive disease characteristics research report**
Prepared 2026-08-29 · Target for dismech KB entry · MONDO:0007205

---

## Executive summary and reliability caveat (read first)

DMS‑MFH is an ultra‑rare autosomal dominant bone dysplasia–cancer syndrome. **Fewer than six families have been reported worldwide**, all in the literature between 1958 and 2012, and essentially the entire molecular understanding of the disease rests on **one paper from one laboratory** (Camacho‑Vanegas et al., *Am J Hum Genet* 2012, PMID:22464254).

Two independent curation bodies currently rate the gene–disease evidence as weak:

- **ClinGen Dosage Sensitivity** assigns MTAP a haploinsufficiency score of **1 ("Little Evidence for Haploinsufficiency")** and triplosensitivity **0**, noting that loss‑of‑function variants are "frequent in gnomAD" and that MTAP's proximity to CDKN2A/B confounds interpretation of 9p21 losses. ([ClinGen HGNC:7413](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:7413))
- **Genomics England PanelApp** lists MTAP on the *Childhood solid tumours* panel (v243) as **Red (low evidence)**, with the reviewer noting the gene "does not meet green list criteria due to insufficient evidence of causation in multiple unrelated cases." ([PanelApp MTAP](https://panelapp.genomicsengland.co.uk/panels/243/gene/MTAP/))

**Curation implication for dismech:** the phenotype (skeletal dysplasia + sarcoma predisposition) is well documented across five multigenerational pedigrees spanning 1958–2012 and should be curated with confidence. The *MTAP exon 9 splicing* mechanism should be curated as the accepted-but-unreplicated molecular hypothesis, ideally with a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion recording the ClinGen/PanelApp dissent. Do not present the MTAP mechanism as settled.

---

## 1. Disease Information

### 1.1 Overview

DMS‑MFH is a rare, autosomal‑dominant syndrome combining a distinctive long‑bone dysplasia with a high lifetime risk of high‑grade bone sarcoma. The skeletal lesion is **diaphyseal medullary stenosis** — progressive narrowing/obliteration of the medullary cavity of the long‑bone shafts by overlying endosteal cortical thickening — accompanied by **scattered bone‑marrow infarctions**, **metaphyseal striations**, pathologic fractures that heal poorly, progressive bowing of the lower limbs, and painful debilitation. Approximately one third of affected individuals develop a high‑grade bone sarcoma, historically diagnosed as malignant fibrous histiocytoma (MFH) or bone fibrosarcoma and, on modern review of at least one case, as **osteosarcoma**.

Two of the five known families additionally show a **progressive limb‑girdle / facioscapulohumeral‑like myopathy**, and features reported in individual pedigrees include **presenile cataracts**, thin skin, easy bruising, and premature graying.

Verbatim (Martignetti et al. 1999, PMID:10053015 abstract):
> "Diaphyseal medullary stenosis with malignant fibrous histiocytoma (DMS-MFH) is an autosomal dominant bone dysplasia/cancer syndrome of unknown etiology. This rare hereditary cancer syndrome is characterized by bone infarctions, cortical growth abnormalities, pathological fractures, and eventual painful debilitation. Notably, 35% of individuals with DMS develop MFH, a highly malignant bone sarcoma."

Verbatim (Camacho‑Vanegas et al. 2012, PMID:22464254 abstract):
> "Diaphyseal medullary stenosis with malignant fibrous histiocytoma (DMS-MFH) is an autosomal-dominant syndrome characterized by bone dysplasia, myopathy, and bone cancer."

Verbatim (Norton et al. 1996, PMID:8781110 abstract):
> "Hardcastle syndrome is a rare, autosomally dominant inherited skeletal dysplasia, characterized by diaphyseal sclerosis, medullary stenosis, pathological fractures, bony infarction, and malignant transformation."

### 1.2 Identifiers (all verified)

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0007205` | *diaphyseal medullary stenosis-bone malignancy syndrome* — **use as `disease_term`** |
| **OMIM** | `112250` (#) | DIAPHYSEAL MEDULLARY STENOSIS WITH MALIGNANT FIBROUS HISTIOCYTOMA; DMSMFH |
| **Orphanet** | `ORPHA:85182` | Diaphyseal medullary stenosis-bone malignancy syndrome |
| **Disease Ontology** | `DOID:0080664` | |
| **UMLS** | `C1862177` | exact map (Orphanet) |
| **MedGen** | UID 350613 / CUI C1862177 | |
| **MeSH** | `C536169` | supplementary concept record; exact map |
| **GARD** | `10072` | exact map |
| **ICD‑10** | `M89.8` | *Other specified disorders of bone* — Orphanet flags DMS‑MFH as **narrower than** the ICD‑10 code |
| **ICD‑11** | `LD24.1Y` | narrower than the targeted code |
| **Causal gene** | MTAP — `hgnc:7413`, NCBI Gene `4507`, OMIM `156540`, UniProt `Q13126`, locus **9p21.3** |
| **Related OMIM entry** | `609940` — *Myopathy, limb‑girdle, with bone fragility* (now regarded as allelic/the same disorder; family 5) |

Cross-reference block validated against Orphadata: [api.orphadata.com ORPHA 85182](https://api.orphadata.com/rd-cross-referencing/orphacodes/85182?lang=en) (CC‑BY‑4.0).

### 1.3 Synonyms and alternative names

- Hardcastle syndrome (most common eponym)
- Diaphyseal medullary stenosis–malignant fibrous histiocytoma syndrome
- Bone dysplasia–medullary fibrosarcoma syndrome
- Bone dysplasia with malignant fibrous histiocytoma
- BDMF (OMIM/GTR gene‑test abbreviation)
- DMSMFH / DMS‑MFH
- Hereditary bone dysplasia with malignant change / with sarcomatous degeneration (historical, Arnold 1973; Hardcastle 1986)
- Myopathy, limb‑girdle, with bone fragility (MedGen lists this as a synonym; formerly separate at MIM 609940)

**Nomenclature note (important for curation).** "Malignant fibrous histiocytoma" was retired as a diagnostic term in the 2013 WHO soft‑tissue classification and replaced by **undifferentiated pleomorphic sarcoma (UPS)**; the 2020 WHO classification confirms UPS as "the correct designation for the storiform and pleomorphic variant of MFH." The disease name retains "MFH" for historical continuity, but the tumor should be curated as **undifferentiated pleomorphic sarcoma of bone (UPSB)** and/or **osteosarcoma**, per the 2012 re‑review of a family‑4 tumor.

### 1.4 Provenance of information

**Aggregated, disease‑level, pedigree‑derived.** There is no EHR cohort, no registry, and no population dataset for DMS‑MFH. All clinical data derive from five published multigenerational pedigrees (case series with radiographic and, latterly, molecular characterization). No dataset exists in GEO/dbGaP/SRA specific to this disease. This should be reflected in dismech `prevalence.measure_type: CASES_IN_LITERATURE`.

---

## 2. Etiology

### 2.1 Primary causal factor

**Germline heterozygous mutation in a non‑canonical terminal exon (exon 9) of *MTAP* (9p21.3),** acting through dysregulated alternative splicing of MTAP isoforms. Inheritance is Mendelian autosomal dominant; there is no known environmental or infectious contribution.

Verbatim (PMID:22464254):
> "We now demonstrate that DMS-MFH results from mutations in the most proximal of three previously uncharacterized terminal exons of the gene encoding methylthioadenosine phosphorylase, MTAP."

### 2.2 Genetic risk factors

- **Causal variants (2 known, see §4.2):** `c.885A>G` (p.(=), synonymous R100R) and `c.813-2A>G`, both in/adjacent to the retroviral‑derived MTAP exon 9.
- **Being a first‑degree relative of an affected individual** is the only meaningful "risk factor" — 50% transmission risk per offspring.
- **Somatic second hit:** loss of the wild‑type allele (LOH at 9p21) is the tumor‑initiating event (§4.2, §6.1).
- **No modifier genes identified.** The variable myopathy across families (present in families 4 and 5, absent from the three original families) is unexplained; it is compatible with either an unrecognized modifier or with allele‑specific effects (the myopathic families 4 and 5 carry *different* mutations — family 4 c.885A>G, family 5 c.813-2A>G — so a simple allele–myopathy correlation is **not** supported).
- **Susceptibility loci:** No GWAS exists for DMS‑MFH (impossible at n≈5 families). The neighbouring 9p21 CAD/MI GWAS locus is discussed by the authors as a speculative overlap (§2.4).

### 2.3 Environmental risk and protective factors

**None identified.** No toxic, occupational, dietary, infectious, or radiation exposure has been associated with DMS‑MFH onset, bone phenotype severity, or sarcoma risk. CTD/TOXNET contain no DMS‑MFH entries. Mechanical loading is a plausible but unstudied modifier of the fracture phenotype.

**No protective genetic or environmental factors are described.** No protective alleles, no dietary or lifestyle intervention has been shown to reduce sarcoma risk.

**Curation note:** the `environmental:` section should be left empty or, if a curator has searched, carry the repo's uncited‑exposure waiver pattern (`review_notes` beginning "Left deliberately uncited." plus a record of the searches run), rather than manufacturing an exposure.

### 2.4 Gene–environment interaction

None documented. One speculative gene–environment/comorbidity thread from the primary paper is worth recording as a hypothesis rather than a finding — a possible MTAP contribution to coronary artery disease:

Verbatim (PMID:22464254, Discussion):
> "First, in DMS-MFH-affected family 1, two male family members died of heart disease in their early forties without other known risk factors. A third family member has been recently diagnosed with early CAD (J.A.M., unpublished data). As such, CAD might represent a previously unrecognized aspect of the disease phenotype in this syndrome."

This is explicitly flagged by the authors as unpublished/anecdotal and should be curated as a `KNOWLEDGE_GAP` discussion, not as a phenotype.

---

## 3. Phenotypes

### 3.1 Core skeletal phenotypes

All HPO IDs below were verified against the HPO release in this repository via OAK (`sqlite:obo:hp`).

| Phenotype | HPO term | Category | Onset | Course | Frequency |
|---|---|---|---|---|---|
| Stenosis of the medullary cavity of the long bones | `HP:0100254` | Skeletal / radiographic | Childhood–adolescence (radiographically detectable) | Progressive | Obligate; defining feature |
| Diaphyseal cortical sclerosis | `HP:0005045` | Skeletal / radiographic | Childhood–adolescence | Progressive | Obligate; defining feature |
| Metaphyseal striations | `HP:0031367` | Skeletal / radiographic | Childhood | Stable/progressive | Frequent |
| Patchy osteosclerosis | `HP:0005686` | Skeletal / radiographic | Childhood–adult | Progressive | Frequent |
| Pathologic fracture | `HP:0002756` | Clinical sign | Childhood to adult (mean ~24 yr in family 5) | Recurrent | Very frequent |
| Recurrent long bone fractures | `HP:0003084` | Clinical sign | as above | Recurrent | Very frequent |
| Bowing of the legs | `HP:0002979` | Physical manifestation | Progressive, post‑fracture | Progressive | Frequent |
| Osteopenia | `HP:0000938` | Radiographic/lab | Adult | Progressive | Reported |
| Osteomyelitis (leading to amputation from slow‑healing fractures) | `HP:0005010` (specific) / `HP:0002754` (general) | Complication | Adult | Episodic | Occasional |
| Bone pain | `HP:0002653` | Symptom | Adult | Progressive, debilitating | Very frequent |

The bone‑marrow **infarction** component ("scattered infarctions within the bone marrow", PMID:22464254) has no precise HPO term; the closest ontology anchor is via UBERON `UBERON:0002371` (bone marrow) plus a curated pathophysiology node. This is a genuine ontology gap worth noting.

### 3.2 Neoplastic phenotypes

| Phenotype | HPO term | Onset | Frequency |
|---|---|---|---|
| Histiocytoma (MFH → UPS) | `HP:0012315` | 2nd–5th decade | **~35% of affected individuals** |
| Osteosarcoma | `HP:0002669` | 2nd–5th decade | Confirmed in ≥1 family‑4 tumor on modern histopathology |
| Fibrosarcoma (of bone) | `HP:0100244` | 2nd–5th decade | Original Arnold 1973 designation; 3 of 6 siblings |

Verbatim (PMID:22464254):
> "Approximately one-third of affected individuals within our families developed bone sarcomas arising between the second and fifth decades of life. The diagnoses were either MFH or bone fibrosarcoma."
> "…given the presence of osteoid, the histopathological analysis of a tumor from a DMS-MFH-affected individual (III-3 from family 4; c.885A>G) is consistent with the diagnosis of osteosarcoma. Thus, inherited MTAP alternative-splicing mutations can result in histology-proven osteosarcoma."

**Frequency caveat.** The "35%" figure derives from three pedigrees in 1999 and was restated as "approximately one-third" in 2012. It is a **within‑pedigree proportion, not an age‑adjusted penetrance estimate**, and is subject to severe ascertainment bias (families were identified *because* of sarcoma). Curate as `FrequencyEnum` band with a note; do not present as a validated lifetime risk.

### 3.3 Neuromuscular phenotypes (families 4 and 5 only)

| Phenotype | HPO term | Onset | Course |
|---|---|---|---|
| Myopathy | `HP:0003198` | Mean ~31 yr (family 5) | Progressive |
| Limb-girdle muscle weakness | `HP:0003325` | Adult | Progressive |
| Proximal muscle weakness | `HP:0003701` | Adult | Progressive |
| Skeletal muscle atrophy | `HP:0003202` | Adult | Progressive |

Verbatim (PMID:22464254, Introduction):
> "We recently expanded the known clinical features of the syndrome by characterizing two new unrelated families affected by a progressive form of muscular disease consistent with facioscapulohumeral muscular dystrophy (FSHD [MIM 158900])."

Note the internal tension in the literature: the 2012 paper describes the myopathy as FSHD‑like in the Introduction and as "features overlapping the symptoms of facioscapulohumeral muscular dystrophy **and limb-girdle muscular dystrophy**" in the Discussion; Watts/Mehta (2005/2006) describe family 5 as **limb‑girdle**. Curate as limb‑girdle with an explicit note about the FSHD‑overlap description. FSHD1/2 (D4Z4) and LGMD genes were not, to my knowledge, formally excluded in these families.

### 3.4 Ocular, integumentary and connective-tissue phenotypes

| Phenotype | HPO term | Notes |
|---|---|---|
| Presenile cataracts | `HP:0007819` | Listed as a core feature in the 2012 Introduction |
| Thin skin | `HP:0000963` | Family 5 (Mehta 2006) |
| Soft skin | `HP:0000977` | MedGen/GARD list |
| Bruising susceptibility | `HP:0000978` | Family 5; GARD flags as occasional |
| Premature graying of hair | `HP:0002216` | Family 5 (Mehta 2006) |

Verbatim (PMID:22464254, Introduction):
> "Affected individuals endure pathologic fractures that subsequently heal poorly, progressive wasting, bowing of the lower extremities, painful debilitation, and the development of presenile cataracts."

Mehta et al. 2006 (PMID:16419137) additionally report "premature graying with thin hair, thin skin, hernias" and clotting abnormalities in family 5 — features that have *not* been confirmed in the three original DMS‑MFH families and should be curated with a `subtype`/family qualifier rather than as disease‑wide.

### 3.5 Inheritance annotation

- Autosomal dominant inheritance — `HP:0000006`

### 3.6 Quality-of-life impact

**No formal QoL instrument (EQ‑5D, SF‑36, PROMIS, TESS, MSTS) has ever been applied to a DMS‑MFH cohort.** Reported impact is qualitative and severe:

- Repeated pathologic fractures with poor healing → prolonged immobilization, chronic pain ("eventual painful debilitation", PMID:10053015).
- Progressive lower‑limb bowing → gait impairment, reduced ambulation.
- Osteomyelitis complicating slow‑healing fractures has led to **amputation** (`HP:0005010`).
- Superimposed limb‑girdle myopathy in two families compounds mobility loss.
- Sarcoma diagnosis in the 2nd–5th decade brings the full burden of neoadjuvant/adjuvant chemotherapy plus limb‑salvage surgery or amputation.
- The tumor‑predisposition status imposes lifelong surveillance and reproductive/genetic‑counselling burden.

This is a legitimate `KNOWLEDGE_GAP` for the dismech entry: `clinical_burden#` with no quantitative instrument available.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**MTAP** — S‑methyl‑5′‑thioadenosine phosphorylase (methylthioadenosine phosphorylase).

| Attribute | Value |
|---|---|
| HGNC | `hgnc:7413` (lowercase prefix per repo convention) |
| NCBI Gene | 4507 |
| Ensembl | ENSG00000099810 |
| UniProt | Q13126 |
| OMIM | 156540 |
| Cytoband | 9p21.3, immediately telomeric to / adjacent to CDKN2A–CDKN2B |
| EC | 2.4.2.28 |
| Quaternary structure | Homotrimer |
| PDB | `1CG6` (trimer + MTA sulfate), `1CB0` (apoprotein) — structure at 1.7 Å (PMID:10404592) |

Verbatim (PMID:22464254):
> "MTAP is a ubiquitously expressed homotrimeric-subunit enzyme critical to polyamine metabolism and adenine and methionine salvage pathways and was believed to be encoded as a single transcript from the eight previously described exons."

**The key structural discovery** is that MTAP is *not* an eight‑exon gene. Three additional terminal exons exist:

- **Exon 9** — a 192 bp ORF (GenBank `AF216650`), located **65 kb downstream** of the previously annotated MTAP termination site; derived from a **MER50I** retroviral element.
- **Exon 10** — derived from a **THE1A** element.
- **Exon 11** — third terminal exon.

Verbatim:
> "Intriguingly, two of these MTAP exons arose from early and independent retroviral-integration events in primate genomes at least 40 million years ago, and since then, their genomic integration has gained a functional role."

Exon 9 integrated "into the primate genome at some point in evolution between the divergence of the ring-tailed lemur and the common woolly monkey approximately 40 million years ago" — i.e., **after prosimian and New World monkey divergence**. The authors describe this as **exaptation** and state:

> "However, we are unaware of any other example wherein the loss of a co-opted gene and/or protein domain results in a disease phenotype."

### 4.2 Pathogenic variants

Two germline variants, both in/adjacent to exon 9, both **splicing‑altering with no predicted amino‑acid change**. Numbering is relative to the EST reference clone **GenBank AK309365**, *not* the canonical NM_002451 transcript — an important caveat for anyone reconciling these to ClinVar.

| Variant | Type | Families | Effect |
|---|---|---|---|
| `c.885A>G` (p.(=), "effectively R100R") | Exonic synonymous; abolishes a predicted **exonic splicing enhancer (ESE)** | 1, 3, 4 | Reduces exon‑9‑containing isoform expression by **~70%**; no effect on archetype MTAP |
| `c.813-2A>G` | Intronic; destroys the **canonical splice acceptor site** | 2, 5 | **Ablates** all exon‑9‑containing isoforms; **significantly increases archetype MTAP** expression |

Verbatim:
> "one mutation was a synonymous change at position c.885A>G (p.(=)), effectively R100R, and was present in affected families 1, 3, and 4. The second mutation, c.813-2A>G, was an intronic change present in affected family 2."

**Segregation and population evidence:**
> "The sequence changes segregated appropriately with the disease phenotype within all respective family members in each family… Neither mutation was identified in 1,000 chromosomes from 500 unaffected control individuals. Similarly, the mutations were not present in dbSNP build 131."

**ACMG/AMP classification.** Neither variant has, to my knowledge, been formally re‑classified under ACMG/AMP 2015 criteria. Under those criteria the evidence would be roughly: PS3 (well‑established functional studies — minigene splicing assays), PS4_moderate/PM (absent from 1,000 control chromosomes), PP1_strong (co‑segregation across five multigenerational pedigrees), PS3 supporting from the elevated serum MTA — but counterweighted by BS1‑type concerns from the ClinGen dosage curation and the fact that the reference transcript is non‑canonical. **Best current summary: "reported pathogenic in the primary literature; not independently classified; ClinGen gene-level evidence rated as limited."**

**ClinVar status is confusing and must be handled carefully.** Searching ClinVar for "Diaphyseal medullary stenosis-bone malignancy syndrome" returns records that are **not** the two published variants: e.g. `NM_002451.4:c.*2837T>A` (`RCV000310131`, VUS, 1‑star, Illumina Clinical Services, submitter note "No publications were found"), `c.*2968T>C` (`RCV000332282`), `c.566G>T` p.Trp189Leu (`RCV000317123`), `c.315C>T` p.Gly105= (`RCV000330004`). These are incidental submissions tagged to the condition, not disease‑causing alleles. The OMIM‑derived allelic variant record for `c.885A>G` is `RCV000022659`. **Do not cite the 3′‑UTR VUS records as evidence for DMS‑MFH.**

**Somatic vs germline / two‑hit:**
> "Moreover, and in agreement with Knudson's two-hit hypothesis for a tumor-suppressing gene, direct sequencing of this patient's osteosarcoma genomic DNA demonstrated homozygosity for the c.885A>G mutation. LOH analysis with microsatellite markers spanning the originally defined 2.9 Mb DMS-MFH critical region revealed complete loss of the WT allele from the unaffected chromosome."

**Functional consequence class.** This is best modeled in dismech as `functional_impact_category: LOSS_OF_FUNCTION` for the exon‑9‑containing isoforms (v1, v2, v4, v5), with a **simultaneous gain** in v3/v6 — an unusual dual effect the authors explicitly flag:

> "Given our findings that the DMS-MFH mutations also result in overexpression of two splice variants, MTAP_v3 and _v6, the possibility that at least two of the MTAP isoforms could represent oncogenic variants must also be considered at this time."

### 4.3 The six retroviral‑derived MTAP isoforms

Identified by 3′ RACE from control and patient fibroblast, lymphoblast and patient‑derived tumor cell lines. None contain wild‑type terminal exon 8; all alter the C‑terminus.

| Isoform | Exon composition | Contains exon 7? | MTAP enzymatic activity |
|---|---|---|---|
| MTAP_v1 | 1–7 + 9S–11 | Yes | **Active** |
| MTAP_v2 | 1–7 + 9L | Yes | **Active** |
| MTAP_v3 | 1–7 + 10 + 11 | Yes | **Active** |
| MTAP_v4 | 1–6 + 9S–11 | No | Not detectable |
| MTAP_v5 | 1–6 + 9L | No | Not detectable |
| MTAP_v6 | 1–6 + 10 + 11 | No | Not detectable |

(9S = short 103 nt form of exon 9; 9L = long 192 nt form.) v4–v6 had "appreciably shorter half-lives"; activity remained undetectable even under proteasome inhibition with MG132.

All six isoforms "can physically interact with archetype MTAP" (co‑immunoprecipitation), supporting a **heterotrimer / dominant‑negative‑like** model at the subunit interface — the structural basis for dominant inheritance despite MTAP being a classic recessive‑style metabolic enzyme.

### 4.4 Linkage history

| Study | Finding |
|---|---|
| Martignetti 1999 (PMID:10053015) | Genome scan, 3 families → **~3 cM on 9p21‑22**, max two‑point **LOD 5.49** at D9S171 (θ=0.05) |
| Watts 2005 (PMID:16244874) | Family 5 (AD limb‑girdle myopathy + bone fragility) → 9p21‑p22, **LOD 3.74**, 15 Mb interval |
| Camacho‑Vanegas 2012 | All 5 families, max combined location score **4.27** at D9SB3; critical region narrowed to **~1.2–1.3 Mb** between AL882 and D9S976 |
| Sporadic MFH LOH (ref. 14 of the 2012 paper) | Smallest region of overlap **2.9 Mb** between D9S736 and D9S171 — links hereditary and sporadic MFH |

Candidate genes excluded by direct sequencing before exon 9 was found: **CDKN2A (p16), p14‑ARF, CDKN2B (p15), the IFN gene cluster, and the eight canonical exons of MTAP.**

### 4.5 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none identified.
- **Epigenetics:** no DNA‑methylation, histone‑modification, or chromatin study has been performed *in DMS‑MFH tissue*. However, the mechanism is intrinsically epigenetic downstream (see §6.1): MTA accumulation inhibits PRMT5, reducing symmetric dimethylarginine marks including **H4R3me2s** and **H3R8me2s**. No ENCODE/Roadmap/DiseaseMeth dataset for this disease.
- **Chromosomal abnormalities:** none constitutional. **Somatically**, 9p21 deletion/LOH is the second hit; 9p21 is "one of the most frequently deleted and/or translocated chromosomal regions in human cancer" (gliomas, melanoma, NSCLC, acute leukemias, osteosarcomas). The 2012 authors raise a methodological warning worth curating:

> "The facts that MTAP is more complex than previously recognized and that its terminal coding exon lies within 25 kb of the p15/p16 locus has immediate significance to LOH mapping and copy number variation (CNV) studies in human cancer. Deletions including the p15/p16 locus will more than likely also include the 3′ region of MTAP and therefore might affect MTAP biochemical activity. Thus, the interpretation of many of these studies with regard to the genes being affected should be reevaluated."

---

## 5. Environmental Information

**Not applicable.** DMS‑MFH is a purely Mendelian disorder with no established environmental, lifestyle, or infectious contribution.

- **Environmental factors:** none identified. No CTD entries.
- **Lifestyle factors:** none identified. Weight‑bearing/mechanical loading is a theoretical modifier of fracture frequency but is unstudied.
- **Infectious agents:** none. *The retroviral element in exon 9 is an endogenous retroviral (ERV) remnant fixed in the primate germline 40 Mya, not an active infection.* This distinction must be preserved in any curated text — MER50I and THE1A are exapted genomic sequence, not pathogens, and there is no NCBITaxon organism to annotate.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain (upstream → downstream)

**Step 1 (MOLECULAR) — Germline exon‑9 splicing mutation.**
`c.885A>G` abolishes an ESE; `c.813-2A>G` destroys the splice acceptor. Both are heterozygous and germline.
`GO:0000380` (alternative mRNA splicing, via spliceosome)

**Step 2 (MOLECULAR) — Dysregulated MTAP isoform stoichiometry.**
Verbatim: *"c.813-2A>G and c.885A>G resulted in markedly decreased [expression]… the c.813-2A>G mutation ablated expression of all isoforms containing exon 9 and significantly increased the [archetype MTAP]… The c.885A>G mutation decreased the expression levels of all exon 9 isoforms by approximately 70% but had no [effect on archetype]."*
Loss of the enzymatically active exon‑9‑containing isoforms v1/v2 and the inactive v4/v5; **overexpression** of v3/v6.

**Step 3 (MOLECULAR) — Perturbed MTAP holoenzyme assembly.**
All six isoforms co‑immunoprecipitate with archetype MTAP; molecular modelling on PDB `1CG6`/`1CB0` shows the splice‑variant insertion points (after K271 for v1‑type, after A230 for v4‑type) sit at the **trimer subunit interface**, adjacent to the exon‑6/exon‑7‑encoded substrate‑binding site (only L279 comes from exon 8). Verbatim: *"The trimeric subunit interface of MTAP does appear to be affected by the alternate splicing events or, possibly, the MTA active site."*
`GO:0017061` (S-methyl-5-thioadenosine phosphorylase activity), modifier `DECREASED`

**Step 4 (ORGANISM/MOLECULAR) — Systemic MTA accumulation.** ← *the key human in‑vivo evidence*
MTAP normally phosphorolyses MTA (`CHEBI:17509`) to adenine (`CHEBI:16708`) + 5‑methylthioribose‑1‑phosphate, which is recycled to L‑methionine (`CHEBI:16643`). MTA is the by‑product of polyamine (spermidine `CHEBI:16610`, spermine) synthesis from SAM (`CHEBI:15414`).
`GO:0071267` (L-methionine salvage), `GO:0043101` (purine-containing compound salvage), `GO:0006595` (polyamine metabolic process)

Verbatim:
> "MTA is not normally present in human serum. Cells lacking MTAP activity are unable to metabolize MTA, and functional inhibition or dysregulation of MTAP activity would therefore be expected to result in intracellular MTA accumulation and secretion… All three serum samples from unaffected individuals had no detectable MTA levels. In marked contrast, both affected individuals had accumulations of MTA detectable in their serum."

| Serum donor | MTA (pmol/100 µL) |
|---|---|
| F4 III‑1 (affected) | 11.5 |
| F4 IV‑2 (affected) | 4.3 |
| F4 IV‑3 (unaffected relative) | not detected |
| Control 1 | not detected |
| Control 2 | not detected |

This is a **biomarker‑grade finding** (n=2 affected vs 3 unaffected, blinded assay) and the single strongest piece of human in‑vivo mechanistic evidence for the disease. It is also, at n=5, a fragile one.

**Step 5 (MOLECULAR, inferred) — PRMT5 hypomethylation.**
Not demonstrated in DMS‑MFH tissue, but established for MTAP‑null cancer generally: accumulated MTA is a SAM‑competitive inhibitor of **PRMT5** with >100‑fold selectivity over other PRMT family members, reducing symmetric arginine dimethylation of histone and non‑histone substrates.
`GO:0019918` (peptidyl-arginine methylation, to symmetrical-dimethyl arginine), `GO:0032259` (methylation)
**Curate as a `MECHANISTIC_HYPOTHESIS` / `EMERGING` hypothesis group with cancer‑biology (not DMS‑MFH) evidence.**

**Step 6a (CELLULAR/TISSUE) — Bone dysplasia arm.**
How MTAP dysfunction produces endosteal cortical thickening, medullary obliteration, marrow infarction, and impaired fracture healing is **genuinely unknown**. The only mechanistic thread the authors offer is polyamine‑dependent angiogenesis:

> "Third, defects in polyamine metabolism have been associated with defects in angiogenesis and altered myocyte function, whereas a nearly pathognomonic feature of DMS-MFH bone dysplasia is the presence of scattered infarctions throughout the medullary cavity."

This is the highest‑value **knowledge gap** in the entry. Cell types implicated by the phenotype (not by direct evidence): osteoblast `CL:0000062`, osteocyte `CL:0000137`, osteoclast `CL:0000092`, bone‑marrow mesenchymal stem cell `CL:2000079`/`CL:0000134`, and marrow microvascular endothelium.
`GO:0001649` (osteoblast differentiation), `GO:0001503` (ossification), `GO:0030282` (bone mineralization)

**Step 6b (TISSUE) — Sarcomagenesis arm.**
Germline heterozygous MTAP defect → somatic LOH/loss of the WT 9p21 allele (Knudson two‑hit) → biallelic MTAP dysfunction in a mesenchymal progenitor → high‑grade sarcoma (UPS/osteosarcoma) in the 2nd–5th decade. The 2012 authors present this as the first in‑vivo human demonstration of MTAP tumour suppression:

> "…the identification of the MTAP splice variants and the fact that their genetic loss results in DMS-MFH provide a possible in vivo demonstration that MTAP can act as a tumor suppressor."

Supporting in vitro precedent: *"Reintroduction of MTAP expression into the MCF7 breast adenocarcinoma cell line, which lacks endogenous MTAP gene expression and enzymatic activity, inhibits the cells' ability to grow both in vitro and in vivo."*

**Step 6c (TISSUE) — Myopathy arm (families 4, 5).**
Mechanism unknown. Only linkage cited: "defects in polyamine metabolism have been associated with… altered myocyte function." Cell type: skeletal muscle fiber `CL:0008002`.

### 6.2 Protein dysfunction

Not misfolding or aggregation. The defect is **isoform stoichiometry within an obligate homotrimer**: wild‑type‑length archetype MTAP retains catalytic competence, but the normal complement of C‑terminally variant subunits that co‑assemble with it is lost or skewed. Predicted (unvalidated) structural detail: *"Secondary-structure and disulfide-bond prediction analyses predict the generation of a disulfide bond between cysteine residues in exons 9 and 10; these prediction analyses require future biochemical analysis for validation."*

### 6.3 Metabolic changes

- **Methionine salvage** — impaired (MTA→methylthioribose‑1‑P→methionine).
- **Adenine salvage** — impaired; MTAP phosphorolysis "is the principle source of free adenine in human cells."
- **Polyamine metabolism** — MTA, the by‑product of spermidine/spermine synthesis, is not cleared.
- **Methylation potential** — MTA:SAM ratio rises, biasing SAM‑dependent methyltransferases (PRMT5 most sensitively).

### 6.4 Immune involvement

None in the human syndrome. In the mouse, however, Mtap heterozygosity produces a lymphoid phenotype (§15) — an interesting species divergence and a candidate `HUMAN_MODEL_MISMATCH`.

### 6.5 Tissue damage mechanisms

- **Ischemia/infarction:** medullary bone infarcts are near‑pathognomonic; presumed vascular (polyamine–angiogenesis link, unproven).
- **Impaired repair:** fractures "heal poorly"; slow union permits **osteomyelitis** and, in some cases, amputation.
- **Mechanical:** stenosed medulla + thickened cortex alters bone biomechanics, predisposing to pathologic fracture and progressive bowing.

### 6.6 Molecular profiling — what exists and what does not

| Modality | Status for DMS‑MFH |
|---|---|
| Transcriptomics | **None.** No GEO/ArrayExpress dataset. 3′ RACE and RT‑PCR on patient fibroblast/lymphoblast/tumor lines is the only transcript‑level work. |
| Proteomics | **None** in PRIDE/ProteomeXchange. Co‑IP and immunoblot only. |
| Metabolomics | **Only the targeted serum MTA assay** (n=5). No untargeted metabolomics; nothing in MetaboLights or Metabolomics Workbench. |
| Lipidomics | **None.** |
| Single‑cell / spatial | **None.** |
| Multi‑omics | **None.** |
| Functional genomics (CRISPR/RNAi) | **None for the syndrome.** Extensive DepMap MTAP‑dependency data exists for MTAP‑*deleted cancer* — relevant to §12 but not to the germline syndrome. |
| Genomic structural features | UCSC/RepeatMasker/Retrosearch analysis of exons 9 (MER50I) and 10 (THE1A); primate genomic DNA PCR panel establishing ~40 Mya integration. |

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary:** the skeleton, specifically the **long tubular bones**.
- Long bone — `UBERON:0002495`
- Diaphysis — `UBERON:0004769` (the defining site)
- Metaphysis — `UBERON:0001438` (striations)
- Femur `UBERON:0000981`, tibia `UBERON:0000979`, fibula `UBERON:0001446`, humerus `UBERON:0000976` (diaphysis of humerus `UBERON:0004652`); the 1996 Norton report's MeSH indexing names femur, fibula and tibia specifically.

**Secondary / additional systems:**
- **Musculoskeletal (muscle):** skeletal muscle, limb‑girdle distribution (families 4, 5).
- **Ocular:** lens — `UBERON:0000965` (presenile cataracts).
- **Integumentary:** skin (thin/soft), hair (premature graying).
- **Hematologic/vascular:** bone‑marrow vasculature (infarction); reported clotting abnormality in family 5.
- **Cardiovascular:** speculative early CAD in family 1 (unpublished, do not curate as phenotype).

**Body systems:** skeletal (primary), muscular, ocular, integumentary, hematopoietic/marrow.

### 7.2 Tissue and cell level

| Structure | Term |
|---|---|
| Compact (cortical) bone tissue — thickened endosteally | `UBERON:0001439` |
| Endosteum — site of pathological apposition | `UBERON:0009859` |
| Bone marrow — site of infarction | `UBERON:0002371` |
| Bone marrow cavity — stenosed/obliterated | `UBERON:0002484` |
| Skeletal muscle tissue — limb girdle | (use limb‑specific children as appropriate) |

| Cell population | Term | Basis |
|---|---|---|
| Osteoblast | `CL:0000062` | Inferred from endosteal cortical thickening |
| Osteocyte | `CL:0000137` | Inferred |
| Osteoclast | `CL:0000092` | Inferred from failed medullary resorption |
| Mesenchymal stem cell (bone marrow) | `CL:2000079` / `CL:0000134` | Presumed sarcoma cell of origin — UPS is now attributed to mesenchymal stem cells rather than histiocytes |
| Fibroblast | `CL:0000057` | Tumor histology: "malignant spindle (fibroblastic) cells of bone MFH"; also the patient cell line used for RACE |
| Skeletal muscle fiber | `CL:0008002` | Myopathy arm |

**Curation warning:** every cell‑type assignment above except fibroblast is *inferred from tissue phenotype*, not demonstrated. There is no cell‑type‑resolved study of DMS‑MFH. Bind these with descriptions that make the inference explicit, or leave them out.

### 7.3 Subcellular level

MTAP is cytosolic. Relevant GO cellular components: cytosol (`GO:0005829`), with nuclear relevance downstream via PRMT5 substrate methylation. No organellar pathology (mitochondrial, ER, lysosomal) is described.

### 7.4 Localization and lateralization

- **Bilateral and symmetric.** The dysplasia is described as symmetric diaphyseal medullary stenosis of the long bones. Radiographic screening therefore uses bilateral long‑bone films.
- **Distribution:** long tubular bones of the limbs; the 2012 description emphasizes "diffuse diaphyseal medullary stenosis with overlying endosteal cortical thickening" — i.e. length‑wise diffuse rather than focal.
- **Tumors** arise focally and are **not** symmetric; extremity location predominates (consistent with UPSB generally).

---

## 8. Temporal Development

### 8.1 Onset

| Manifestation | Typical onset |
|---|---|
| Radiographic dysplasia | Detectable from **puberty** — the basis for the screening recommendation |
| Pathologic fractures | Childhood through adulthood; **mean ~24 years** in family 5 (Mehta 2006) |
| Limb‑girdle myopathy | **Mean ~31 years** in family 5 |
| Presenile cataracts | Adult, premature relative to population norms |
| Bone sarcoma | **2nd–5th decade** (approximately ages 10–50) |

**Onset pattern:** insidious and chronic for the dysplasia; **acute** for each fracture event; **subacute** for tumor presentation (pain, mass, or pathologic fracture through tumor).

Note the developmental sequencing this implies: the skeletal dysplasia is essentially **congenital/constitutional in genotype but adolescent in radiographic expression**, and the malignancy is a late, stochastic, second‑hit event.

### 8.2 Progression

**Stages (not formally defined — proposed for curation from the natural history):**
1. **Latent / radiographic-only** — childhood to puberty; asymptomatic, dysplasia visible on plain film.
2. **Fracture phase** — adolescence through adulthood; recurrent pathologic fractures with poor union; progressive bowing.
3. **Debilitation phase** — adult; chronic pain, deformity, infarction burden, superimposed myopathy in some families; osteomyelitis/amputation risk.
4. **Malignant transformation** — 2nd–5th decade; ~1 in 3 affected individuals; converts prognosis from chronic disability to life‑threatening.

**Progression rate:** slow and steady for the dysplasia (decades); the myopathy is explicitly "progressive"; sarcoma behaves as a high‑grade, rapidly progressive malignancy.

**Course pattern:** chronic progressive with superimposed episodic events (fractures, infarcts, tumor). **Not** relapsing‑remitting.

**Duration:** lifelong. There is no self‑limited form.

### 8.3 Patterns

- **Remission:** none for the skeletal dysplasia — it is structural and irreversible. Tumor remission is treatment‑induced only (see §11, §12).
- **Critical periods:**
  - **Puberty** — the radiographic screening window opens (Norton 1996 recommendation).
  - **2nd–5th decades** — the sarcoma surveillance window; this is the period where surveillance could plausibly change outcome.
  - **Peri‑fracture** — the intervention window for preventing malunion and osteomyelitis.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence: not documented.** Neither Orphanet nor GARD publishes a prevalence estimate. Orphanet describes the disorder only as "very rare."
- **Total reported cases:** **five families worldwide** (as of the 2012 gene‑discovery paper and, to my knowledge, still the case in 2026). Family origins: American (Vermont/New York), Australian, English, and two New York families — one of which (family 5) is the 1958 Canadian Henry kindred with AD bone fragility and limb‑girdle myopathy.
- **Incidence: not documented.** No registry, no national surveillance, no SEER capture (SEER codes the tumor, not the syndrome).

**dismech prevalence record shape:**
```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: ULTRA_RARE
  notes: >-
    Five unrelated multigenerational families reported worldwide (Arnold 1973
    American kindred; Hardcastle 1986 English and Australian families; Norton
    1996 New York family; a second New York family and the 1958 Henry Canadian
    kindred added by Camacho-Vanegas 2012). No prevalence estimate is published
    by Orphanet or GARD.
```

### 9.2 Genetic parameters

| Parameter | Status |
|---|---|
| **Inheritance pattern** | **Autosomal dominant** — confirmed across five multigenerational pedigrees, with male‑to‑male transmission excluding X‑linkage. HPO `HP:0000006`. |
| **Penetrance** | Appears **high to complete for the radiographic bone dysplasia** (the trait segregated cleanly for linkage analysis, LOD 5.49). **Incomplete/probabilistic for the sarcoma** (~35%). No formal age‑adjusted penetrance study exists. |
| **Expressivity** | **Variable** — most strikingly, myopathy is present in families 4 and 5 and absent from families 1–3; cataracts, skin and hair features are reported unevenly. Even within families, sarcoma occurs in only a subset. |
| **Anticipation** | **Not reported and not expected** — this is not a repeat‑expansion disorder. |
| **Germline mosaicism** | **Not reported.** No de novo case has been described; all reported probands come from affected kindreds. This is itself notable — an unascertained sporadic/de novo case population may exist. |
| **Founder effect** | **None.** The two mutations are distributed across geographically unrelated families (c.885A>G in the American, New York, and second New York families; c.813-2A>G in the Australian and Canadian families) with no reported shared haplotype. |
| **Consanguinity** | **Not a factor** — dominant inheritance. |
| **Carrier frequency** | **Not applicable** (dominant); the causal alleles were absent from 1,000 control chromosomes and from dbSNP build 131. Note the tension with the ClinGen observation that MTAP LoF variants are "frequent in gnomAD" — those are canonical‑exon LoF variants, not exon‑9 splicing alleles, and the two observations are not contradictory but are easily conflated. |

### 9.3 Population demographics

- **Affected populations:** all reported families are of **European/European-diaspora ancestry** (United States, England, Australia, Canada). This almost certainly reflects **ascertainment**, not biology — the disorder has only ever been studied by centres in the US, UK and Australia. Do not curate as an ancestry association.
- **Geographic distribution:** North America (US, Canada), United Kingdom, Australia. No endemic focus.
- **Variant geography:** no meaningful pattern at n=2 variants / 5 families.
- **Sex ratio:** **1:1 expected and consistent with reports** — autosomal dominant, "males and females equally affected with 50% transmission risk per child" (MedGen). No sex bias in bone or tumor phenotype has been reported.
- **Age distribution of affected individuals:** all ages; clinical burden concentrates in the 2nd–5th decades.

---

## 10. Diagnostics

### 10.1 Imaging — the diagnostic cornerstone

**Plain radiography of the long bones is the primary diagnostic modality.** Characteristic findings:
- Symmetric **diaphyseal medullary stenosis** with **endosteal cortical thickening** (`HP:0100254`, `HP:0005045`)
- **Metaphyseal striations** (`HP:0031367`)
- **Patchy osteosclerosis** (`HP:0005686`)
- Scattered **medullary infarcts** — serpiginous sclerotic rims
- Healed/healing pathologic fractures, bowing deformity

**MRI** characterizes marrow infarction and is essential for tumor staging and local extent (used in the Norton 1996 report).

**Thallium‑201 scintigraphy** — proposed specifically for this syndrome as a tumor‑sensitive screen, because ordinary bone scintigraphy is confounded by the diffusely abnormal, infarcted, remodelling skeleton:
> "Thallium scanning is proposed as a more tumor-sensitive screening agent in affected individuals." (PMID:8781110)

**CT** for cortical detail; **FDG‑PET/CT** is now standard for sarcoma staging generally, though it has not been specifically validated in DMS‑MFH and would be expected to have reduced specificity against a background of bone infarction and remodelling — a real and under‑discussed diagnostic problem in this disease.

### 10.2 Laboratory tests and biomarkers

- **Serum MTA (5′‑deoxy‑5′‑methylthioadenosine, `CHEBI:17509`) — the only disease‑specific biochemical marker.** MTA is undetectable in normal serum; affected individuals had 11.5 and 4.3 pmol/100 µL. **This is a research assay, not a clinical test** — it has been performed in a single study on two affected individuals and three controls, has no validated reference interval, no established cutoff, no LOINC code, and is not offered by any clinical laboratory. Curate as an association/biomarker with `validation_status` language making this explicit, **not** as a diagnostic test.
- Routine bone chemistry (calcium, phosphate, ALP, PTH, 25‑OH‑D) is used to exclude metabolic bone disease; no characteristic abnormality is reported.
- **CK** is appropriate in the myopathic families; specific values are not reported in the accessible literature.

### 10.3 Biopsy and pathology

Sarcoma diagnosis requires histopathology. In the one modern re‑review reported:
> "(A) Histologic analysis revealed that 95% of the studied tumor specimen displayed the typical pattern of malignant spindle (fibroblastic) cells of bone MFH. (B) Malignant cells forming neoplastic bone. (C) Focal sheets of neoplastic bone within the tumor are shown to be entrapping pre-existing bone trabeculae, and the overtly malignant cells are shown to produce bone."

The presence of osteoid reclassified this tumor as **osteosarcoma**. This matters practically: UPS of bone and osteosarcoma are treated on the same protocol, so the reclassification does not change management, but it does change the phenotype annotation.

**Immunohistochemistry** is used mainly by exclusion — UPS is a diagnosis of exclusion after ruling out specific lineages (SMA/desmin for leiomyosarcoma, S100/SOX10 for melanoma and MPNST, keratins/EMA for sarcomatoid carcinoma, CD34, MDM2/CDK4 FISH for dedifferentiated liposarcoma). **MTAP immunohistochemistry** is now a validated surrogate for 9p21 co‑deletion in other tumor contexts (notably mesothelioma) and is worth considering here — though its interpretation in a germline exon‑9 splicing mutation, where archetype MTAP protein is *retained or even increased*, is genuinely unclear and would likely be falsely negative. Worth flagging as a knowledge gap.

### 10.4 Genetic testing

- **Recommended approach:** targeted sequencing of **MTAP exon 9 and its intron–exon boundaries** in a proband from a family with the characteristic radiographic dysplasia.
- **Critical technical caveat — the single most actionable diagnostic point in this report:** exon 9 lies **65 kb downstream of the canonical MTAP termination site**, in what standard annotation treats as intergenic/3′ region. **Standard exome sequencing (WES) and standard clinical gene panels will not capture or will not report this region.** Any DMS‑MFH testing must either be a custom targeted assay or **genome sequencing (WGS)** with explicit non‑coding analysis. The 2012 authors reached the answer only after "DNA-sequence analysis of known candidate genes within the original critical region had previously failed to identify causative mutations… In particular, this analysis included the known eight exons and corresponding intron-exon boundaries of MTAP."
- **WGS:** the preferred agnostic approach for a new suspected case; requires targeted interrogation of the exon‑9 region.
- **Gene panels:** MTAP appears on the Genomics England *Childhood solid tumours* panel but as **Red**, meaning it is **not reported diagnostically** on that panel. Practically, this means a suspected DMS‑MFH case will not be resolved by ordering a routine hereditary‑cancer or skeletal‑dysplasia panel. GTR lists tests under the abbreviation **BDMF**.
- **RNA sequencing / transcript analysis** is arguably the most sensitive functional assay, given that both mutations act through splicing — patient fibroblast or lymphoblast RT‑PCR/3′ RACE demonstrating loss of exon‑9‑containing isoforms is the direct functional readout.
- **CMA, karyotyping, FISH:** not indicated (no constitutional chromosomal abnormality). FISH for 9p21 is relevant only in the *tumor*, to demonstrate the somatic second hit.
- **mtDNA and repeat‑expansion testing:** not applicable.

### 10.5 Omics-based diagnostics

None validated. RNA‑seq is the modality with real potential (§10.4). No proteomic, metabolomic (beyond the research MTA assay), epigenomic, or liquid‑biopsy diagnostic exists.

### 10.6 Clinical criteria and differential diagnosis

**There are no formal, published diagnostic criteria.** A practical working definition: symmetric diaphyseal medullary stenosis with endosteal cortical thickening on long‑bone radiographs, in an autosomal dominant pedigree, with or without pathologic fractures, marrow infarction, myopathy, or bone sarcoma.

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| **Camurati–Engelmann disease** (progressive diaphyseal dysplasia, TGFB1) | Also diaphyseal, also AD — the closest mimic and explicitly indexed as a MeSH term on the Norton 1996 paper. Distinguished by **periosteal + endosteal** cortical thickening (vs predominantly endosteal), prominent limb pain and waddling gait from childhood, characteristic responsiveness to corticosteroids, **no marrow infarction**, and **no sarcoma predisposition**. |
| **Ribbing disease** (hereditary multiple diaphyseal sclerosis) | Diaphyseal sclerosis, later onset, asymmetric, no malignancy. |
| **Osteopetrosis** (all forms) | Generalized sclerosis with medullary obliteration, but marrow failure, cranial nerve compression, and characteristic "bone‑in‑bone"/"Erlenmeyer flask" appearance. |
| **Melorheostosis** | "Dripping candle wax" cortical hyperostosis, sclerotomal and asymmetric. |
| **Osteogenesis imperfecta** | Recurrent fractures and AD inheritance, but **osteopenia with thin cortices** — the radiographic opposite of DMS‑MFH — plus blue sclerae, dentinogenesis imperfecta, hearing loss. |
| **Chronic recurrent multifocal osteomyelitis (CRMO)** | Inflammatory, metaphyseal, responds to NSAIDs. |
| **Li–Fraumeni syndrome (TP53)** | The major *sarcoma‑predisposition* differential — but no skeletal dysplasia, and a much broader tumor spectrum (breast, adrenocortical, brain, leukemia). |
| **Hereditary retinoblastoma (RB1)** | Osteosarcoma predisposition; distinguished by retinoblastoma history. |
| **Rothmund–Thomson (RECQL4), Werner, Bloom** | Osteosarcoma predisposition with poikiloderma/short stature/premature aging. |
| **Paget disease of bone / familial expansile osteolysis** | Sarcomatous degeneration risk, but late onset, elevated ALP, characteristic mosaic pattern. |
| **Sickle cell disease / Gaucher disease** | Bone infarction and avascular necrosis — but haemoglobinopathy or lysosomal enzymology is diagnostic. |
| **Ghosal hematodiaphyseal dysplasia (TBXAS1)** | Diaphyseal sclerosis with anemia; AR. |
| **Fibrous dysplasia (GNAS)** | Ground‑glass lesions, café‑au‑lait, endocrinopathy in McCune–Albright. |

### 10.7 Screening

- **Radiographic screening of at‑risk relatives from puberty onward** — the one explicit published recommendation (Norton 1996).
- **Thallium scintigraphy** for tumor surveillance in known‑affected individuals (Norton 1996).
- **Cascade genetic testing** of at‑risk relatives once a familial variant is identified — feasible in principle, constrained by the assay problem in §10.4.
- **Newborn screening:** not applicable; no biochemical newborn screen and no benefit from presymptomatic neonatal identification.
- **Carrier screening:** not applicable (dominant).

**Honest assessment:** these recommendations date from 1996 and have never been prospectively evaluated. Thallium‑201 is now largely obsolete in clinical practice, displaced by FDG‑PET/CT, and no modern surveillance protocol for DMS‑MFH exists. This is a defensible `KNOWLEDGE_GAP`.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

**No DMS‑MFH‑specific survival data exist.** No cohort of sufficient size has ever been assembled. Prognosis must be assembled from two components: the chronic skeletal/myopathic disability, and the sarcoma.

**Sarcoma survival (proxy data from UPS of bone cohorts — the best available surrogate):**

| Source | Population | Outcome |
|---|---|---|
| COSS Group, *J Cancer Res Clin Oncol* 2026 (PMC12819900) | 132 unselected UPSB patients, Germany/Austria/Switzerland, treated on osteosarcoma protocols | **5-year EFS 63% (SE 5%); 5-year OS 70% (SE 4%)** after median follow-up 3.9 yr (EFS) / 5.2 yr (OS) |
| Population-based cohort, 2022 (PMID:35184191) | UPSB, registry-based | **5-year disease-specific survival 47.4% overall; 56.4% (M0) vs 16.9% (M1)** |

The gap between these two figures is instructive: the COSS cohort is a specialist, protocol-treated, younger population; the registry cohort is unselected. A DMS‑MFH patient — typically young, extremity primary, treated at a sarcoma centre — is closer to the COSS profile, but carries the added liability of a diffusely abnormal skeleton complicating limb salvage.

**Life expectancy:** in the absence of sarcoma, likely near‑normal but with substantial disability. With sarcoma, governed by the figures above. Individuals never developing sarcoma (~2/3) face a chronic musculoskeletal disease rather than a life‑limiting one.

### 11.2 Morbidity and function

- Chronic bone pain and "eventual painful debilitation" (PMID:10053015).
- Recurrent fractures with poor union; progressive lower‑limb bowing.
- **Osteomyelitis leading to amputation due to slow healing fractures** (`HP:0005010`) — an explicitly curated HPO feature of this disease.
- Progressive limb‑girdle weakness in the myopathic families, superimposing neuromuscular disability on structural bone disease.
- Presenile cataracts → visual impairment requiring surgery.
- No ICF‑coded disability data, no EQ‑5D/SF‑36/PROMIS/MSTS/TESS data.

### 11.3 Complications

Pathologic fracture · fracture nonunion/malunion · osteomyelitis · amputation · bone infarction · progressive deformity · sarcoma · chemotherapy toxicity (anthracycline cardiotoxicity, cisplatin ototoxicity/nephrotoxicity, ifosfamide neuro/nephrotoxicity, secondary malignancy) · possible early CAD (unpublished/speculative).

### 11.4 Recovery potential

**The skeletal dysplasia is irreversible.** No treatment restores medullary architecture. Fractures heal — poorly and slowly. Sarcoma is curable in a substantial fraction with multimodal therapy (see §12), and this is the one domain where treatment materially changes outcome.

### 11.5 Prognostic factors

**For the sarcoma (extrapolated from UPSB cohorts, COSS 2026):**
- **Favourable:** age <40 years; extremity primary; localized (M0) disease at presentation.
- **Unfavourable:** metastatic disease at presentation (M1 5-yr DSS 16.9% vs M0 56.4%); age ≥40 years (and ≥65 in the registry analysis); non‑extremity site; **pathologic fracture at presentation** — a factor of specific concern in DMS‑MFH, where pathologic fracture is a *baseline* feature of the disease and may confound this prognostic variable entirely.
- **Notably:** in the COSS cohort only 38% achieved good histologic response (<10% viable tumor) to preoperative chemotherapy, and — unusually for bone sarcoma — this "correlated poorly with prognosis," meaning the standard osteosarcoma response‑to‑neoadjuvant prognostic marker may not transfer to UPSB.

**Disease-specific prognostic factors for DMS‑MFH:** none identified. Neither serum MTA level, nor which of the two mutations a family carries, nor presence of myopathy has been shown to predict outcome — the sample size makes such analysis impossible.

**Prognostic biomarkers:** none validated.

---

## 12. Treatment

**There is no disease‑modifying or targeted therapy for DMS‑MFH.** Management is entirely symptomatic, orthopaedic, and oncologic.

### 12.1 Skeletal management

| Intervention | Notes | NCIT |
|---|---|---|
| Orthopaedic fracture fixation | Intramedullary nailing is technically difficult or impossible given medullary stenosis — plate/external fixation may be required. This is a genuine, disease‑specific surgical constraint. | `NCIT:C16186` Orthopedic Surgical Procedure |
| Corrective osteotomy / deformity correction | For progressive bowing | `NCIT:C15329` Surgical Procedure |
| Amputation | For osteomyelitis complicating nonunion, or for unresectable tumor | `NCIT:C15329` |
| Physical therapy / rehabilitation | Mobility preservation; especially relevant with superimposed myopathy | `NCIT:C15302` Physical Therapy; `NCIT:C15315` Rehabilitation |
| Analgesia / supportive care | Chronic bone pain | `NCIT:C15747` Supportive Care |
| Cataract extraction | Presenile cataracts | `NCIT:C15329` |

**Bisphosphonates and other antiresorptives are not indicated and are theoretically hazardous** — DMS‑MFH is a *sclerosing* dysplasia with medullary obliteration and impaired fracture healing, not an osteopenic one. Suppressing remodelling further is unlikely to help and may worsen union. No study addresses this; flag as a knowledge gap rather than a recommendation.

### 12.2 Sarcoma management

Patients are treated **on osteosarcoma protocols**. From the COSS UPSB cohort (n=132, 2026):

- **Chemotherapy in 100%** of patients: doxorubicin **98%**, cisplatin **93%**, ifosfamide **82%**, high‑dose methotrexate **64%**.
- **Surgery in 96%**; among extremity tumors, **81% limb salvage** vs amputation.
- Representative dosing reported elsewhere: doxorubicin 60 mg/m², ifosfamide 9 g/m², cisplatin 90 mg/m², with methotrexate 8 g/m² added for poor histologic responders.

**dismech treatment record shape:**

```yaml
treatments:
- name: Osteosarcoma-Type Multiagent Chemotherapy
  therapeutic_modality: SMALL_MOLECULE
  treatment_term:
    preferred_term: chemotherapy
    term: {id: NCIT:C15632, label: Chemotherapy}
    therapeutic_agent:
    - preferred_term: doxorubicin
      term: {id: CHEBI:28748, label: doxorubicin}
    - preferred_term: cisplatin
      term: {id: CHEBI:27899, label: cisplatin}
    - preferred_term: ifosfamide
      term: {id: CHEBI:5864, label: ifosfamide}
    - preferred_term: methotrexate
      term: {id: CHEBI:44185, label: methotrexate}
```
(All four CHEBI IDs verified via OAK. `regimen_term` should be **omitted** — MAP/MAPI is not a named NCIT `Treatment Regimen` concept that reliably resolves; do not invent one.)

- **Radiotherapy** (`NCIT:C15313`) has a limited role — for unresectable or positive‑margin disease, as in bone sarcoma generally.
- **Guideline reference:** NCI PDQ *Osteosarcoma and Undifferentiated Pleomorphic Sarcoma of Bone Treatment* ([NBK65736](https://www.ncbi.nlm.nih.gov/books/NBK65736/)) is the appropriate clinical guideline anchor — note that PDQ explicitly co‑names UPS of bone with osteosarcoma, confirming the shared‑protocol approach.

### 12.3 Genetic counselling

`NCIT:C15240` Genetic Counseling. Autosomal dominant, 50% offspring risk; discussion of variable expressivity (myopathy present in only some families), the ~1‑in‑3 sarcoma risk, and the technical limitation that standard panels/exomes will not detect the causal variant.

### 12.4 The MTAP/PRMT5 therapeutic axis — the major recent development

This is where 2023–2026 literature is genuinely active, and it is the most interesting forward‑looking content for this entry. **It is relevant to DMS‑MFH by mechanism, not by evidence** — no DMS‑MFH patient has ever received these agents, and the direction of effect may not even be favourable (see the caveat below).

**The synthetic lethality.** MTAP loss → MTA accumulation → MTA is a SAM‑competitive inhibitor of **PRMT5** with >100‑fold selectivity over other PRMTs → PRMT5 enters a "frail," partially inhibited state → the cell becomes selectively hypersensitive to further PRMT5 inhibition. This is the basis of an entire drug class: **MTA‑cooperative PRMT5 inhibitors**, which preferentially bind PRMT5 in the MTA‑bound state and therefore spare MTAP‑intact normal tissue — solving the hematologic toxicity that sank first‑generation PRMT5 inhibitors.

**Epidemiologic scale:** homozygous MTAP deletion (almost always co‑deleted with CDKN2A) occurs in **~10–15% of all solid tumors**; by type (C‑CAT data, per the 2025 *Int J Mol Sci* review, PMC12733126): mesothelioma **33.1%**, urothelial carcinoma **23.8%**, CNS tumors **19.0%**, pancreatic **18.4%**, cholangiocarcinoma **15.6%**, NSCLC **14.3%**; lowest in prostate (1.2%), colon (1.7%), cervix (3.6%).

**Clinical-stage agents:**

| Agent | Class | Trial | Reported status |
|---|---|---|---|
| **AMG 193** | MTA‑cooperative PRMT5i | NCT05094336 | Phase I dose exploration, 80 patients dosed 40–1600 mg as of 23 May 2024; **MTD 1200 mg once daily**; **ORR 21.4%** among efficacy‑assessable patients. Most common TRAEs: nausea 48.8%, fatigue 31.3%, vomiting 30.0%. (*Ann Oncol* 2024, PMID:39293516; *Cancer Discov* 2025;15(1):139, PMID:39282709) |
| **MRTX1719 / BMS‑986504** | MTA‑cooperative PRMT5i | NCT05245500 | Phase I/II ongoing; objective responses reported without the hematologic toxicity of first‑generation PRMT5 inhibitors |
| **TNG908** | Brain‑penetrant MTA‑cooperative PRMT5i | NCT05275478 | Phase I/II; 36% PR reported in pancreatic, 11% in NSCLC |
| **TNG462** | MTA‑cooperative PRMT5i | NCT05732831 | Phase I recruiting; preclinical synergy with targeted agents in MTAP‑null models |
| **AG‑270 / S095033** | MAT2A inhibitor (reduces SAM) | — | Phase I: 2 partial responses; MTD 200 mg daily |
| **IDE397** | MAT2A inhibitor | — | Phase II expansion: 38% PR squamous NSCLC, 30% urothelial |
| **BGB‑58067** | PRMT5 inhibitor | — | In development (NCI drug dictionary) |

Biomarker: *"The only factor qualifying for therapy is the presence of a homozygous deletion of the MTAP gene, detected by NGS or FISH."*

**The critical caveat for DMS‑MFH — do not curate this as a treatment.** DMS‑MFH is *not* an MTAP‑homozygous‑deletion state. The germline lesion is a heterozygous splicing mutation in a non‑canonical exon that **preserves and in one allele class increases archetype MTAP expression**. Whether a DMS‑MFH tumor (which does undergo somatic LOH at 9p21) reaches the MTA‑high, PRMT5‑frail state required for MTA‑cooperative PRMT5 inhibitor sensitivity is **unknown and untested**. The elevated *serum* MTA is suggestive but not equivalent to intratumoral MTA saturation. Additionally, MTAP IHC — the cheap surrogate biomarker — would likely be *falsely negative* here because archetype protein is retained.

**Curate this as a `mechanistic_hypotheses` entry with `status: EMERGING`** and a `discussions` entry of `kind: KNOWLEDGE_GAP` asking whether DMS‑MFH tumors phenocopy MTAP‑deleted tumors for PRMT5 dependency — a well‑posed, tractable, and genuinely open question that this KB entry can usefully record.

### 12.5 Other therapeutic modalities

- **Gene therapy, gene editing, ASOs, siRNA, cell therapy, immunotherapy:** none developed, none in trial. **Splice‑switching ASOs are a theoretically attractive modality** given that both mutations act on splicing — but no such program exists, and the direction of correction differs between the two alleles.
- **Pharmacogenomics:** no DMS‑MFH‑specific PGx. Standard sarcoma‑chemotherapy PGx applies (e.g. *TPMT*/*NUDT15* not relevant here; *UGT1A1* not relevant; consider standard anthracycline cardiotoxicity risk factors and cisplatin ototoxicity pharmacogenetics — *TPMT*/*COMT* variants have CPIC‑adjacent literature).
- **Clinical trials:** the only DMS‑MFH‑specific registered study is **NCT00007046**, "Genetic Study of Patients and Families With Diaphyseal Medullary Stenosis With Malignant Fibrous Histiocytoma of the Bone" (Mount Sinai; a natural‑history/gene‑discovery study, not interventional). I was unable to retrieve its current status; verify with `just fetch-reference NCT00007046` before citing it as an evidence item.

### 12.6 Treatment strategy summary

There is no DMS‑MFH treatment algorithm. The practical pathway is: (1) confirm the dysplasia radiographically and, where possible, molecularly; (2) orthopaedic management of fractures and deformity with awareness that medullary stenosis constrains fixation options; (3) lifelong surveillance for sarcoma; (4) on sarcoma diagnosis, refer to a sarcoma centre and treat on an osteosarcoma protocol; (5) genetic counselling and cascade evaluation of relatives.

---

## 13. Prevention

**No primary prevention is possible.** The disorder is a germline Mendelian condition; nothing prevents its occurrence in a person who inherits the allele, and no intervention is known to reduce the ~35% sarcoma risk.

| Level | Available approach |
|---|---|
| **Primary** | Only **reproductive**: genetic counselling, prenatal diagnosis, or preimplantation genetic testing for monogenic disease (PGT‑M) in a family with an identified variant. No lifestyle, dietary, or pharmacologic primary prevention exists. |
| **Secondary** | **Radiographic screening of at‑risk family members from puberty onward** (Norton 1996). **Tumor surveillance** in affected individuals — thallium scintigraphy as originally proposed; in current practice this would be MRI and/or FDG‑PET/CT, though no protocol has been validated for this disease. Cascade genetic testing once a familial variant is known. |
| **Tertiary** | Prompt orthopaedic management of fractures to prevent nonunion → osteomyelitis → amputation; fall/fracture‑risk reduction; physiotherapy to preserve function; long‑term surveillance for chemotherapy late effects (anthracycline cardiomyopathy, secondary malignancy) in sarcoma survivors. |

- **Immunization:** not applicable — no infectious component. (Standard immunosuppression‑related vaccination guidance applies during chemotherapy.)
- **Genetic screening:** carrier screening not applicable (dominant); **PGT‑M and prenatal testing are technically feasible** where the familial exon‑9 variant is known — one of the few concretely actionable options.
- **Risk stratification:** no validated model. Family history plus radiographic phenotype is the entirety of current stratification.
- **Behavioural interventions / public health / environmental interventions:** not applicable.
- **Prophylaxis:** no prophylactic medication. **Prophylactic surgery has no established role** — unlike, say, risk‑reducing mastectomy in BRCA1/2, there is no organ to remove, since the at‑risk tissue is the entire skeleton.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthology

- **Human** — `NCBITaxon:9606` — the only species with the natural disease.
- **Mouse** — `NCBITaxon:10090` — *Mtap*, MGI:1914152, NCBI Gene 66902.
- MTAP is broadly conserved across eukaryotes and archaea (the *Sulfolobus solfataricus* MTAP‑II structure is solved), consistent with a core metabolic salvage function.

### 14.2 The evolutionary caveat that dominates this section

**The disease mechanism cannot be modelled in any non‑primate species.** Exon 9 (MER50I‑derived) and exon 10 (THE1A‑derived) entered the genome by retroviral integration **after prosimian/New World monkey divergence, ~40 Mya**. Verbatim:

> "First, given the evolutionary species restriction of these HERVs, the existence of MTAP variants and possible biochemical regulation resulting from their expression must be unique to primates."

Mice, zebrafish, *Drosophila*, and *C. elegans* have *Mtap* orthologs but **do not have exon 9**. There is therefore no mouse, rat, fish, or fly in which the DMS‑MFH mutation can be recapitulated. This is the defining constraint on the entire experimental biology of this disease and belongs in the dismech entry as an explicit `HUMAN_MODEL_MISMATCH` discussion.

### 14.3 Natural disease in other species

**None reported.** OMIA contains no DMS‑MFH entry. No naturally occurring MTAP bone dysplasia/sarcoma syndrome is described in dogs, cats, horses, or any other companion or wildlife species. No breed association (no VBO term applies).

### 14.4 Comparative pathology

- **Divergent phenotype in mouse.** Homozygous *Mtap* loss is **embryonic lethal** in mouse; heterozygotes develop **T‑cell lymphoma**, not bone dysplasia or sarcoma (§15). The human heterozygote develops a skeletal dysplasia with mesenchymal sarcoma. This is a striking species divergence, plausibly attributable to the different lesion class (whole‑gene knockout vs primate‑specific isoform dysregulation) and worth curating as a `FAILS_TO_RECAPITULATE`/`PARTIALLY_RECAPITULATES` link.
- **Conservation of the core enzyme** (methionine/adenine salvage, polyamine metabolism) is deep; **conservation of the regulatory isoform layer** is primate‑restricted.

### 14.5 Transmission

**Not applicable.** No zoonotic potential, no cross‑species susceptibility. The endogenous retroviral elements are fixed germline sequence, not transmissible agents.

---

## 15. Model Organisms

### 15.1 Existing genetic models

**Mouse — *Mtap* whole‑gene disruption (Kadariya et al., *Cancer Res* 2009;69(14):5961–9, PMID:19567676).**

- **Genotype:** *Mtap<sup>lacZ</sup>* knockout allele; heterozygous *Mtap*<sup>+/lacZ</sup>.
- **Homozygotes:** early embryonic lethal.
- **Heterozygotes:** born at Mendelian ratios, indistinguishable from wild-type through the first year, then die prematurely with **median survival 585 days** of **T‑cell lymphoma**. Necropsy shows "greatly enlarged spleens, altered thymic histology, and lymphocytic infiltration of their livers." Older surviving heterozygotes show mild, **non‑clonal** T‑cell lymphoproliferative disease, "suggesting that loss of Mtap might stimulate T-cell proliferation."
- **Interpretation:** supports MTAP as a bona fide tumor suppressor — the strongest independent in‑vivo evidence for tumor suppression, though in a different lineage.

**Mouse — *Mtap*<sup>+/−</sup> × *Myc* (PLoS One 2013, "Germline mutations in Mtap cooperate with Myc to accelerate tumorigenesis in mice").** Demonstrates cooperativity between Mtap loss and MYC in tumor acceleration.

**Model organism databases:** MGI ([MGI:1914152](https://www.informatics.jax.org/marker/MGI:1914152)); IMPC/KOMP/IMSR for allele availability; Alliance of Genome Resources for orthology.

### 15.2 dismech `animal_models` shape

```yaml
animal_models:
- name: Mtap heterozygous knockout mouse (Mtap+/lacZ)
  species: Mouse
  genotype: Mtap<lacZ> heterozygous null
  publication: PMID:19567676
  modeled_mechanisms:
  - target: MTAP Loss of Function
    relationship: PARTIALLY_RECAPITULATES
    fidelity: LOW
    description: >-
      Heterozygous Mtap disruption in mouse establishes MTAP as a tumor
      suppressor in vivo, supporting the tumor-predisposition arm of DMS-MFH.
    limitations: >-
      The mouse develops T-cell lymphoma, not bone dysplasia or bone sarcoma,
      and dies at a median of 585 days. Critically, the mouse Mtap ortholog
      lacks exons 9-11 entirely: those exons derive from primate-restricted
      retroviral integrations approximately 40 million years old, so the
      DMS-MFH splicing lesion cannot be modeled in any non-primate species.
      A whole-gene knockout is therefore not the same lesion class as the
      human exon-9 splicing mutation.
```

A companion `discussions` entry of `kind: HUMAN_MODEL_MISMATCH` should attach to the MTAP pathophysiology node, with the prompt framed as: *does whole-gene Mtap knockout in a species lacking the retroviral-derived exon-9 isoform layer inform the human exon-9 splicing disease at all?*

### 15.3 Cellular and in vitro models

**Available and used in the primary paper:**
- **Patient‑derived fibroblast lines** — 3′ RACE isoform discovery, splicing analysis.
- **Patient‑derived lymphoblastoid lines** — same.
- **A patient‑derived tumor cell line established by the authors** — the only DMS‑MFH tumor line in existence, as far as I can determine. Its availability (ATCC/Cellosaurus deposition) is not stated; this is worth chasing for anyone planning work.
- **MTAP minigene constructs** — three constructs (WT, c.813-2A>G, c.885A>G) spanning ~11.5 kb of genomic sequence; the definitive functional assay for the splicing mechanism, and the model system a new lab would most plausibly rebuild.
- **Heterologous isoform expression + MTAP enzymatic assay** — established that v1, v2, v3 have activity and v4, v5, v6 do not, including under MG132 proteasome inhibition.
- **Co‑immunoprecipitation** — established physical interaction of all six isoforms with archetype MTAP.
- **MCF7** — MTAP‑null breast adenocarcinoma line used historically for MTAP re‑expression growth‑suppression experiments.

**Not available:** no iPSC line, no organoid, no osteoblast‑differentiation model, no NAM/organ‑chip system, no isogenic CRISPR knock‑in of the exon‑9 variants in a human osteoblastic or mesenchymal background. **The last of these is the single most obvious missing experiment** — a CRISPR knock‑in of c.885A>G or c.813-2A>G into human iPSCs differentiated toward osteoblast lineage would be the first model capable of addressing the bone‑dysplasia arm at all.

### 15.4 Computational models

Molecular modelling of the MTAP trimer on PDB `1CG6`/`1CB0`, examining splice‑variant insertion points (after K271 for v1‑type, after A230 for v4‑type) relative to the trimer interface and MTA active site. Rendered in O v.13 and PyMOL v1.3. Secondary‑structure and disulfide‑bond prediction suggested an exon‑9/exon‑10 cysteine disulfide, explicitly flagged by the authors as requiring biochemical validation. No kinetic, systems‑biology, or whole‑cell metabolic model of the MTAP salvage pathway in this disease exists.

### 15.5 Research applications and limitations

**Can be studied:** MTAP isoform biology, splicing regulation, exaptation of retroviral sequence, MTAP tumor‑suppressor function, MTA as a circulating biomarker.

**Cannot currently be studied in any model:** the bone dysplasia itself, the marrow infarction, the impaired fracture healing, the myopathy, and the tissue‑specificity of the disease (why bone and muscle, when MTAP is ubiquitously expressed?). That last question is arguably the central unanswered question of the disease and has no experimental system attached to it.

---

## Appendix A — Consolidated ontology term suggestions

All IDs below were verified against this repository's ontology adapters (OAK `sqlite:obo:hp` / `:go` / `:cl` / `:uberon` / `:chebi`) on 2026-08-29, except the NCIT terms, which are taken from the verified table in `CLAUDE.md`.

**Disease:** `MONDO:0007205` diaphyseal medullary stenosis-bone malignancy syndrome

**Gene:** `hgnc:7413` MTAP

**Phenotypes (HP):** `HP:0100254` · `HP:0005045` · `HP:0031367` · `HP:0005686` · `HP:0002756` · `HP:0003084` · `HP:0002979` · `HP:0000938` · `HP:0005010` · `HP:0002754` · `HP:0002653` · `HP:0012315` · `HP:0002669` · `HP:0100244` · `HP:0003198` · `HP:0003325` · `HP:0003701` · `HP:0003202` · `HP:0007819` · `HP:0000963` · `HP:0000977` · `HP:0000978` · `HP:0002216` · `HP:0000006` (inheritance)

**Biological processes (GO):** `GO:0071267` L-methionine salvage · `GO:0043101` purine-containing compound salvage · `GO:0006595` polyamine metabolic process · `GO:0000380` alternative mRNA splicing, via spliceosome · `GO:0019918` peptidyl-arginine methylation, to symmetrical-dimethyl arginine · `GO:0032259` methylation · `GO:0001649` osteoblast differentiation · `GO:0001503` ossification · `GO:0030282` bone mineralization

**Molecular function (GO):** `GO:0017061` S-methyl-5-thioadenosine phosphorylase activity

**Cell types (CL):** `CL:0000062` osteoblast · `CL:0000137` osteocyte · `CL:0000092` osteoclast · `CL:0000134` mesenchymal stem cell (or `CL:2000079` mesenchymal stem cell of femoral bone marrow) · `CL:0000057` fibroblast · `CL:0008002` skeletal muscle fiber

**Anatomy (UBERON):** `UBERON:0004769` diaphysis · `UBERON:0001438` metaphysis · `UBERON:0002495` long bone · `UBERON:0001439` compact bone tissue · `UBERON:0009859` endosteum · `UBERON:0002371` bone marrow · `UBERON:0002484` bone marrow cavity · `UBERON:0000981` femur · `UBERON:0000979` tibia · `UBERON:0001446` fibula · `UBERON:0000976` humerus · `UBERON:0000965` lens of camera-type eye

**Chemical entities (CHEBI):** `CHEBI:17509` 5'-S-methyl-5'-thioadenosine · `CHEBI:15414` S-adenosyl-L-methionine · `CHEBI:16708` adenine · `CHEBI:16643` L-methionine · `CHEBI:16610` spermidine · `CHEBI:17148` putrescine · `CHEBI:28748` doxorubicin · `CHEBI:27899` cisplatin · `CHEBI:5864` ifosfamide · `CHEBI:44185` methotrexate

**Treatments (NCIT):** `NCIT:C15632` Chemotherapy · `NCIT:C15329` Surgical Procedure · `NCIT:C16186` Orthopedic Surgical Procedure · `NCIT:C15313` Radiation Therapy · `NCIT:C15302` Physical Therapy · `NCIT:C15315` Rehabilitation · `NCIT:C15747` Supportive Care · `NCIT:C15240` Genetic Counseling

---

## Appendix B — Reference list with quotable snippets

References marked ✅ have been fetched into this worktree's `references_cache/` and their snippets verified as exact substrings.

| Reference | Citation | Verified quotable snippet |
|---|---|---|
| ✅ **PMID:22464254** | Camacho-Vanegas O, Camacho SC, Till J, et al. Primate genome gain and loss: a bone dysplasia, muscular dystrophy, and bone cancer syndrome resulting from mutated retroviral-derived MTAP transcripts. *Am J Hum Genet.* 2012;90(4):614–627. DOI:10.1016/j.ajhg.2012.02.024 | "We now demonstrate that DMS-MFH results from mutations in the most proximal of three previously uncharacterized terminal exons of the gene encoding methylthioadenosine phosphorylase, MTAP." |
| ✅ PMID:22464254 (full text) | — | "Approximately one-third of affected individuals within our families developed bone sarcomas arising between the second and fifth decades of life." |
| ✅ PMID:22464254 (full text) | — | "All three serum samples from unaffected individuals had no detectable MTA levels. In marked contrast, both affected individuals had accumulations of MTA detectable in their serum" |
| ✅ PMID:22464254 (full text) | — | "direct sequencing of this patient's osteosarcoma genomic DNA demonstrated homozygosity for the c.885A>G mutation" |
| ✅ PMID:22464254 (full text) | — | "Neither mutation was identified in 1,000 chromosomes from 500 unaffected control individuals." |
| ✅ **PMID:10053015** | Martignetti JA, Desnick RJ, Aliprandis E, et al. Diaphyseal medullary stenosis with malignant fibrous histiocytoma: a hereditary bone dysplasia/cancer syndrome maps to 9p21-22. *Am J Hum Genet.* 1999;64(3):801–807. DOI:10.1086/302297 | "Notably, 35% of individuals with DMS develop MFH, a highly malignant bone sarcoma." |
| ✅ PMID:10053015 | — | "linked the syndrome to a region of approximately 3 cM on chromosome 9p21-22, with a maximal two-point LOD score of 5.49" |
| ✅ **PMID:8781110** | Norton KI, Wagreich JM, Granowetter L, Martignetti JA. Diaphyseal medullary stenosis (sclerosis) with bone malignancy (malignant fibrous histiocytoma): Hardcastle syndrome. *Pediatr Radiol.* 1996;26(9):675–677. DOI:10.1007/BF01356833 | "Hardcastle syndrome is a rare, autosomally dominant inherited skeletal dysplasia, characterized by diaphyseal sclerosis, medullary stenosis, pathological fractures, bony infarction, and malignant transformation." |
| ✅ PMID:8781110 | — | "Radiographic screening of family members is suggested from puberty onward. Thallium scanning is proposed as a more tumor-sensitive screening agent in affected individuals." |
| PMID:19567676 | Kadariya Y, Yin B, Tang B, et al. Mice heterozygous for germ-line mutations in methylthioadenosine phosphorylase (MTAP) die prematurely of T-cell lymphoma. *Cancer Res.* 2009;69(14):5961–5969. | Fetch before quoting |
| PMID:16244874 | Watts GD, Mehta SG, Zhao C, et al. Mapping autosomal dominant progressive limb-girdle myopathy with bone fragility to chromosome 9p21-p22. *Hum Genet.* 2005;118(3-4):508–514. | Fetch before quoting |
| PMID:16419137 | Mehta SG, Watts GD, McGillivray B, et al. Manifestations in a family with autosomal dominant bone fragility and limb-girdle myopathy. *Am J Med Genet A.* 2006;140(4):322–330. | Fetch before quoting |
| PMID:3745248 | Hardcastle P, Nade S, Arnold W. Hereditary bone dysplasia with malignant change. Report of three families. 1986. | Fetch before quoting |
| Arnold 1973 | Arnold WD. Hereditary bone dysplasia with sarcomatous degeneration: study of a family. *Ann Intern Med.* 1973;78(6):902. DOI:10.7326/0003-4819-78-6-902 | Family 1, the original American kindred |
| PMID:13511301 | Henry EW, et al. Abnormality of the long bones and progressive muscular dystrophy in a family. *Can Med Assoc J.* 1958;78(5):331–336. | Family 5, original description |
| PMID:10404592 | Appleby TC, et al. The structure of human 5'-deoxy-5'-methylthioadenosine phosphorylase at 1.7 Å resolution. *Structure.* 1999. | PDB 1CG6 / 1CB0 |
| PMID:39293516 | Rodon J, et al. First-in-human study of AMG 193, an MTA-cooperative PRMT5 inhibitor, in patients with MTAP-deleted solid tumors: results from phase I dose exploration. *Ann Oncol.* 2024. | ORR 21.4%; MTD 1200 mg QD |
| PMID:39282709 | Belmontes B, et al. AMG 193, a clinical stage MTA-cooperative PRMT5 inhibitor, drives antitumor activity preclinically and in patients with MTAP-deleted cancers. *Cancer Discov.* 2025;15(1):139. | — |
| PMID:35184191 | Clinical characteristics of undifferentiated pleomorphic sarcoma of bone and the impact of adjuvant chemotherapy: a population-based cohort study. 2022. | 5-yr DSS 47.4% overall; 56.4% M0 vs 16.9% M1 |
| PMC12819900 | Undifferentiated pleomorphic sarcoma of bone (UPSB) treated in the German-speaking countries: 132 unselected patients from the COSS Group. *J Cancer Res Clin Oncol.* 2026. | "the 5 year event-free and overall survival probabilities were 63% (standard error: 5%) and 70% (4%), respectively" |
| PMC12733126 | MTAP deletion as a therapeutic vulnerability in cancer: from molecular mechanism to clinical targeting. *Int J Mol Sci.* 2025. | MTAP deletion frequencies by tumor type; PRMT5i landscape |

**Cache commands to run before curating evidence items from the unfetched rows:**
```bash
just fetch-reference PMID:19567676
just fetch-reference PMID:16244874
just fetch-reference PMID:16419137
just fetch-reference PMID:3745248
just fetch-reference PMID:39293516
just fetch-reference PMID:35184191
just fetch-reference ORPHA:85182   # note: not present in the current Orphanet cache
```

---

## Appendix C — Explicit gaps and cautions for the curator

1. **The gene–disease relationship is contested.** ClinGen HI score 1, PanelApp Red. Curate the mechanism, but record the dissent — ideally as a `discussions` entry with `kind: KNOWLEDGE_GAP` attached to the MTAP pathophysiology node.
2. **No independent replication since 2012.** No new family, no independent variant, no confirmatory functional study in 14 years.
3. **The variants are not in canonical transcript coordinates.** `c.885A>G`/`c.813-2A>G` are numbered against EST clone AK309365, not NM_002451.4. The MTAP ClinVar records returned by a condition search are unrelated VUS submissions — do not cite them.
4. **Do not curate the elevated serum MTA as a diagnostic test.** n=2 affected, research assay, no reference interval, no LOINC code.
5. **Do not curate PRMT5 inhibitors as a treatment.** The mechanism is suggestive; the evidence in this disease is zero, and the germline lesion is not an MTAP deletion. `mechanistic_hypotheses` with `status: EMERGING` is the correct home.
6. **Do not curate early CAD as a phenotype.** It is unpublished anecdote explicitly flagged as such by the authors.
7. **Family-specific features need `subtype` qualifiers.** Myopathy (families 4, 5), thin skin / premature graying / hernias / clotting abnormality (family 5 only) should not be presented as disease-wide.
8. **The bone dysplasia mechanism is unknown.** This is the highest-value knowledge gap in the entry — the causal chain from MTAP isoform imbalance to endosteal cortical thickening and marrow infarction is entirely unspecified.
9. **No non-primate model can carry the lesion.** Record as `HUMAN_MODEL_MISMATCH`.
10. **The `research/` directory rule applies.** This report is analysis, not deep-research-provider output — if it is committed, it belongs under `docs/curation-notes/` or `docs/reports/`, not `research/`.

---

## Sources

- [OMIM #112250 — Diaphyseal medullary stenosis with malignant fibrous histiocytoma](https://omim.org/entry/112250)
- [OMIM *156540 — Methylthioadenosine phosphorylase; MTAP](https://omim.org/entry/156540)
- [Orphanet — Diaphyseal medullary stenosis-bone malignancy syndrome (ORPHA:85182)](https://www.orpha.net/en/disease/detail/85182)
- [Orphadata cross-referencing API — ORPHA 85182](https://api.orphadata.com/rd-cross-referencing/orphacodes/85182?lang=en)
- [MONDO:0007205 — Monarch Initiative](https://monarchinitiative.org/MONDO:0007205)
- [HPO / ontology.jax.org annotation API — OMIM:112250](https://ontology.jax.org/api/network/annotation/OMIM:112250)
- [MedGen C1862177 — Diaphyseal medullary stenosis-bone malignancy syndrome](https://www.ncbi.nlm.nih.gov/medgen/C1862177)
- [GARD 10072 — Diaphyseal medullary stenosis-bone malignancy syndrome](https://rarediseases.info.nih.gov/diseases/10072/diaphyseal-medullary-stenosis-bone-malignancy-syndrome)
- [Disease Ontology DOID:0080664](https://www.informatics.jax.org/disease/DOID:0080664)
- [Camacho-Vanegas et al. 2012, Am J Hum Genet — PMID:22464254](https://pubmed.ncbi.nlm.nih.gov/22464254/)
- [Martignetti et al. 1999, Am J Hum Genet — PMID:10053015](https://pubmed.ncbi.nlm.nih.gov/10053015/)
- [Norton et al. 1996, Pediatr Radiol — PMID:8781110](https://pubmed.ncbi.nlm.nih.gov/8781110/)
- [Watts et al. 2005, Hum Genet — PMID:16244874](https://pubmed.ncbi.nlm.nih.gov/16244874/)
- [Mehta et al. 2006, Am J Med Genet A — PMID:16419137](https://pubmed.ncbi.nlm.nih.gov/16419137/)
- [Hardcastle et al. 1986 — PMID:3745248](https://pubmed.ncbi.nlm.nih.gov/3745248/)
- [Arnold 1973, Ann Intern Med](https://doi.org/10.7326/0003-4819-78-6-902)
- [Henry et al. 1958, Can Med Assoc J — PMID:13511301](https://pubmed.ncbi.nlm.nih.gov/13511301/)
- [Kadariya et al. 2009, Cancer Res — Mtap heterozygous mice](https://pmc.ncbi.nlm.nih.gov/articles/PMC2757012/)
- [Germline mutations in Mtap cooperate with Myc — PLOS One](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0067635)
- [MGI:1914152 — mouse Mtap](https://www.informatics.jax.org/marker/MGI:1914152)
- [ClinGen Dosage Sensitivity — MTAP (HGNC:7413)](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:7413)
- [Genomics England PanelApp — MTAP, Childhood solid tumours](https://panelapp.genomicsengland.co.uk/panels/243/gene/MTAP/)
- [ClinVar RCV000310131 — MTAP c.*2837T>A](https://www.ncbi.nlm.nih.gov/clinvar/RCV000310131.2/)
- [ClinVar RCV000317123 — MTAP c.566G>T](https://www.ncbi.nlm.nih.gov/clinvar/RCV000317123/)
- [UniProt Q13126 — MTAP](https://www.uniprot.org/uniprotkb/Q13126/entry)
- [Structure of human MTAP at 1.7 Å — PMID:10404592](https://pubmed.ncbi.nlm.nih.gov/10404592/)
- [AMG 193 phase I first-in-human, Ann Oncol 2024 — PMID:39293516](https://pubmed.ncbi.nlm.nih.gov/39293516/)
- [AMG 193, Cancer Discovery 2025](https://aacrjournals.org/cancerdiscovery/article/15/1/139/750846/AMG-193-a-Clinical-Stage-MTA-Cooperative-PRMT5)
- [MTAP deletion as a therapeutic vulnerability in cancer, Int J Mol Sci 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12733126/)
- [A review of the known MTA-cooperative PRMT5 inhibitors, RSC Adv 2024](https://pubs.rsc.org/en/content/articlehtml/2024/ra/d4ra05497k)
- [UPSB in the COSS Group, J Cancer Res Clin Oncol 2026](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12819900/)
- [UPS of bone population-based cohort — PMID:35184191](https://pubmed.ncbi.nlm.nih.gov/35184191/)
- [NCI PDQ — Osteosarcoma and Undifferentiated Pleomorphic Sarcoma of Bone Treatment](https://www.ncbi.nlm.nih.gov/books/NBK65736/)
- [Undifferentiated Pleomorphic Sarcoma — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK570612/)
- [NCT00007046 — Genetic Study of Patients and Families With DMS-MFH](https://clinicaltrials.gov/study/NCT00007046)
- [Atlas of Genetics and Cytogenetics in Oncology and Haematology — DMS-MFH](https://atlasgeneticsoncology.org/cancer-prone-disease/10056/diaphyseal-medullary-stenosis-with-malignant-fibrous-histiocytoma-(dms-mfh))
- [BoneTumor.org — Diaphyseal Medullary Stenosis with Malignant Fibrous Histiocytoma](https://www.bonetumor.org/tumors-inherited-conditions/diaphyseal-medullary-stenosis-malignant-fibrous-histiocytoma)

---

**Next step:** the draft `kb/disorders/Diaphyseal_Medullary_Stenosis_With_Malignant_Fibrous_Histiocytoma.yaml` in this worktree is currently a placeholder skeleton. Say the word and I'll populate it from this report — starting with the pathophysiology chain in §6.1 and the evidence items in Appendix B, then running `just validate`, `just count-verified-snippets`, and `just validate-terms` on it.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 19 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 81 |
| Resolved | 77 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 33 |
| Terms named correctly | 24 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007205` (6 mentions) - the report calls it "MONDO", "Monarch Initiative"; MONDO calls it **diaphyseal medullary stenosis-bone malignancy syndrome**
- `DOID:0080664` (4 mentions) - the report calls it "Disease Ontology"; DOID calls it **diaphyseal medullary stenosis with malignant fibrous histiocytoma**
- `UBERON:0009859` (2 mentions) - the report calls it "Endosteum — site of pathological apposition"; UBERON calls it **endosteum**
- `NCIT:C15329` (4 mentions) - the report calls it "For osteomyelitis complicating nonunion, or for unresectable tumor", "Presenile cataracts"; NCIT calls it **Surgical Procedure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002371` (3 mentions) - the report calls it "Bone marrow — site of infarction"; UBERON calls it **bone marrow**
- `HP:0012315` (2 mentions) - the report calls it "Histiocytoma (MFH → UPS)"; HP calls it **Histiocytoma**
- `HP:0100244` (2 mentions) - the report calls it "Fibrosarcoma (of bone)"; HP calls it **Fibrosarcoma**
- `UBERON:0001439` (2 mentions) - the report calls it "Compact (cortical) bone tissue — thickened endosteally"; UBERON calls it **compact bone tissue**, and lists "cortical bone tissue" among its other names
- `UBERON:0002484` (2 mentions) - the report calls it "Bone marrow cavity — stenosed/obliterated"; UBERON calls it **bone marrow cavity**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0007205` - called "MONDO", "Monarch Initiative"
- `NCIT:C15329` - called "For osteomyelitis complicating nonunion, or for unresectable tumor", "Presenile cataracts"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`, `OMIM`.