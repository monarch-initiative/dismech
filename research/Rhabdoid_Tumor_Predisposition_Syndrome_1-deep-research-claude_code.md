---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-31T19:54:48.384252'
end_time: '2026-08-31T20:00:10.985122'
duration_seconds: 322.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Rhabdoid Tumor Predisposition Syndrome 1
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
  web_search_requests: 14
  num_turns: 17
  total_cost_usd: 1.2214964
  session_id: 70de5b01-cdc4-5635-9abb-0681d0e2fde9
  stop_reason: end_turn
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 26
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 16
  verified: 13
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 8
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0016569
    ontology_label: obsolete covalent chromatin modification
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rhabdoid Tumor Predisposition Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Rhabdoid Tumor Predisposition Syndrome 1** covering all of the
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

# Rhabdoid Tumor Predisposition Syndrome 1 (RTPS1): Comprehensive Research Report

## 1. Disease Information

**Overview.** Rhabdoid tumor predisposition syndrome 1 (RTPS1) is an autosomal dominant, highly penetrant childhood cancer predisposition syndrome caused by heterozygous germline loss-of-function variants in **SMARCB1** (a core subunit of the SWI/SNF/BAF chromatin-remodeling complex), predisposing to malignant rhabdoid tumors of the CNS (atypical teratoid/rhabdoid tumor, AT/RT), kidney (rhabdoid tumor of the kidney, RTK), and extrarenal/extracranial soft-tissue sites, typically presenting in infancy. RTPS2 is the allelic-locus counterpart caused by germline **SMARCA4** variants and is kept distinct below (design-decisions §3a: germline predisposition syndrome vs. the somatic tumors it predisposes to — RTPS1 is the constitutional condition; AT/RT, RTK, and MRT are its component neoplasms, each with their own somatic biology).

**Key identifiers:**
- OMIM #609322 — RHABDOID TUMOR PREDISPOSITION SYNDROME 1; RTPS1 ([omim.org/entry/609322](https://omim.org/entry/609322))
- Gene: SMARCB1, OMIM *601607, HGNC:11103, chromosome 22q11.23
- RTPS2 (allelic/distinct locus): OMIM #613325, gene SMARCA4, 19p13.2 — cited here only for contrast, not as RTPS1 content
- GeneReviews: "Rhabdoid Tumor Predisposition Syndrome" (Bourdeaut F, Fréneaux P, Thebaud E, et al., updated periodically), NCBI Bookshelf NBK469816 — covers both RTPS1 and RTPS2 under one review
- Orphanet: ORPHA231108, "Rhabdoid tumor predisposition syndrome" (umbrella term for RTPS1/RTPS2); MONDO:0016473. I did not find an Orphanet/MONDO identifier specific to RTPS1 alone in this search pass — flag this as unresolved rather than guessing a CURIE.
- Related/component-tumor identifiers (do not conflate with the germline syndrome itself): Rhabdoid tumor, ORPHA69077 / MONDO:0002728 / ICD-10 C49.9; Atypical teratoid rhabdoid tumor, ORPHA99966 / MONDO:0020560 / ICD-11 2A00.1Y
- NCI PDQ: "Rhabdoid Tumor Predisposition Syndrome Type 1" (NBK602739, cancer.gov/publications/pdq/information-summaries/genetics/rtps1-hp-pdq)

**Synonyms:** Rhabdoid predisposition syndrome 1; RTPS1; INI1-related rhabdoid predisposition; SMARCB1-related rhabdoid predisposition; (historically) malignant rhabdoid tumor predisposition syndrome.

**Evidence base character:** Information below is derived overwhelmingly from **aggregated disease-level resources** — case-series registries (European Rhabdoid Registry, Children's Oncology Group [COG] trials), literature reviews, and structured databases (OMIM, GeneReviews, ClinVar) — rather than large-scale EHR data, reflecting the rarity of the condition (single-digit-per-million annual incidence, see §9).

---

## 2. Etiology

**Disease-causal factor:** Monogenic — heterozygous germline pathogenic loss-of-function variant in **SMARCB1** (RTPS1). This is a Mendelian cancer predisposition syndrome; there is no meaningful environmental or infectious causal contribution to the germline lesion itself. Skipping penetrance/mosaicism mechanics per your standing context, but flagging the specific data points:

**Genetic risk factors:**
- Germline SMARCB1 loss-of-function variants (truncating point mutations, whole/partial gene deletions, splice variants) — the causal lesion.
- Constitutional structural rearrangements are a documented, non-trivial minority mechanism: constitutional 22q11.23 deletions encompassing SMARCB1 (PMID:21412926) and **constitutional balanced translocations involving SMARCB1** as a rare RTPS1 mechanism, reported 2023 (PMID:37548271) — worth flagging for CMA/karyotype-negative-by-sequencing cases.
- **Modifier/second-hit factor:** somatic inactivation of the remaining wild-type SMARCB1 allele (commonly via monosomy 22 or focal LOH) is required for tumorigenesis — the classic tumor-suppressor two-hit mechanism, noted without re-deriving it.
- **Genotype-severity correlation (important, not just background):** RTPS1-causing variants cluster in exons 2–9 and are predominantly truncating (nonsense, frameshift, splice, whole/partial-gene deletion) (PMID:24933152, PMID:21108436). This is mechanistically and clinically distinct from the **non-truncating, hypomorphic** variants (missense, in-frame, or hotspot changes at the gene's 5′/3′ ends — e.g., c.41C>A p.Pro14His in ~10% and the 3′UTR c.*82C>T in ~27% of schwannomatosis cases) that cause **SMARCB1-related schwannomatosis** rather than RTPS1 — see §9 and §10 for how this drives differential surveillance.

**Environmental risk factors:** None established as disease-causal for RTPS1 itself (this is a germline predisposition, not a somatically-triggered sporadic tumor). Post-diagnosis, DNA-damaging exposures (radiation, chemotherapy, UV, tobacco) are flagged as **secondary-malignancy risk factors** in RTPS1 carriers, per GeneReviews management guidance, not as causes of the primary syndrome.

**Protective factors:** None reported in the literature for RTPS1 carriers specifically. RTPS2 (SMARCA4) shows incomplete penetrance, implying unidentified modifiers, but no specific protective allele or exposure has been characterized for either gene.

**Gene-environment interaction:** Not established for RTPS1; the condition is driven by a highly penetrant monogenic first hit plus a stochastic somatic second hit rather than by exposure-dependent risk modulation.

---

## 3. Phenotypes

Framed per your instruction to keep germline-syndrome and somatic-tumor content separate: the "phenotype" of RTPS1 *as a cancer predisposition syndrome* is the pattern and timing of tumor development, not a set of dysmorphic/developmental features (contrast Coffin-Siris syndrome below, which does carry a distinct dysmorphic phenotype from non-truncating SMARCB1 variants).

| Phenotype | Type | Onset | Frequency | Notes / HPO suggestion |
|---|---|---|---|---|
| Atypical teratoid/rhabdoid tumor (AT/RT), CNS | Neoplasm | Median 4–7 months in RTPS1 vs. ~18 months sporadic (PMC12062526) | ~65% of RTPS1-associated tumors are CNS; >50% of CNS tumors are cerebellar/posterior fossa (GeneReviews) | HP:0030066 (Neoplasm of the central nervous system); consider MONDO:0020560 for the tumor entity itself |
| Rhabdoid tumor of the kidney (RTK) | Neoplasm | Infancy | ~9% of RTPS1 tumors (PMC12062526) | HP:0009726 (Renal neoplasm) |
| Extrarenal/extracranial malignant rhabdoid tumor (soft tissue, liver, mediastinum, retroperitoneum, pelvis, heart, head/neck) | Neoplasm | Infancy | ~26% of RTPS1 tumors | HP:0002664 (Neoplasm) as generic parent; site-specific HP terms per location |
| Synchronous/metachronous multifocal tumors | Disease-course feature | >70% present before 12 months with synchronous disease (GeneReviews) | >70% | Not itself an HP-codable "phenotype" but a defining disease-course claim |
| Congenital/perinatal presentation | Onset timing | Within first 28 days of life in a subset | Documented but not separately quantified in sources reviewed | HP:0003577 (Congenital onset) |

**Severity/progression:** Uniformly aggressive at presentation — "more than 70% of individuals with RTPS present before age 12 months with synchronous tumors that exhibit aggressive clinical behavior" (GeneReviews, NBK469816). The European Rhabdoid Registry reports 84.5% of RTPS patients experience tumor progression during follow-up, with 48% progressing while actively on chemotherapy (cited in PMC12062526; I have not independently verified the registry primary publication in this pass — flagging as a secondary-source claim, a lead rather than confirmed primary citation).

**Quality of life:** No RTPS1-specific EQ-5D/SF-36/PROMIS data were located in this search pass; QoL literature in this space is dominated by general pediatric-oncology intensive-therapy morbidity data rather than RTPS1-stratified instruments. This is a gap, not a null finding — say so rather than substitute adjacent pediatric-oncology QoL literature as if RTPS1-specific.

---

## 4. Genetic/Molecular Information

**Causal gene:** SMARCB1 (HGNC:11103, NCBI Gene 6598, Ensembl ENSG00000099956), OMIM *601607, chromosome 22q11.23. Protein: SMARCB1/INI1/SNF5/BAF47, a core, non-catalytic subunit of the SWI/SNF (BAF) ATP-dependent chromatin-remodeling complex.

**Variant classification (ACMG/AMP via ClinGen/ClinVar):** RTPS1-causing variants are classified pathogenic/likely pathogenic when predicted to cause loss of function. ClinVar entries include, e.g., NM_003073.5(SMARCB1):c.986+1G>A (splice-donor) and c.628+13C>T, both submitted against "Rhabdoid tumor predisposition syndrome 1" (ClinVar RCV000008489.3, RCV000407869).

**Variant type/spectrum:**
- Nonsense, frameshift, canonical splice-site variants — dominant mechanism.
- Whole-gene and single/multi-exon deletions — clinically important: gene-targeted deletion/duplication analysis detects an *additional* ~51% of probands beyond the ~49% found by sequence analysis alone (GeneReviews), meaning sequencing-only panels will miss roughly half of RTPS1 cases. This has direct implications for the KB's genetic-testing/diagnostics content — flag deletion/duplication analysis as non-optional in any RTPS1-focused definitions/diagnostics block.
- Constitutional 22q11.23 microdeletion and balanced translocation mechanisms (PMID:21412926, PMID:37548271) — rarer, but real, and would be missed by exome/panel sequencing without CMA/karyotype.

**Allele frequency:** SMARCB1 is under strong population-level constraint against loss-of-function variation (consistent with its essential developmental role and haploinsufficiency mechanism), but I was unable to retrieve an exact current gnomAD pLI/LOEUF value in this search pass — do not fabricate a number; if a precise constraint metric is needed for the KB entry, pull it directly from the gnomAD browser (gnomad.broadinstitute.org) rather than from this report.

**Somatic vs. germline origin:** Germline SMARCB1 variants define RTPS1 by definition; the same gene is very frequently biallelically inactivated **somatically** in sporadic (non-syndromic) rhabdoid tumors — SMARCB1 immunohistochemical loss (absence of INI1 nuclear staining) is the diagnostic hallmark of rhabdoid tumors regardless of germline status. Germline SMARCB1 variants are found in roughly **25–35% of all newly diagnosed rhabdoid tumor patients** (GeneReviews), rising to **~55% in those diagnosed before 6 months of age** (PMC12062526) — a strong argument for near-universal germline testing in infantile-onset cases, which is exactly what current surveillance guidance reflects (§10).

**Functional consequence:** Loss of function / haploinsufficiency at the germline level; complete biallelic loss (protein-null) at the tumor level, detected by absent INI1 immunostaining.

**Modifier genes:** No validated modifier genes for RTPS1 severity/penetrance were identified in this pass, distinct from RTPS2 (SMARCA4), where incomplete penetrance is well documented but mechanistically unexplained.

**Epigenetic information:** Central to pathophysiology — see §6. SMARCB1 loss produces a genome-wide chromatin redistribution rather than a simple loss of enzymatic activity (mechanism detailed below), and the resulting rhabdoid tumors — and specifically AT/RT — are stratified into three epigenetically distinct molecular subgroups (ATRT-TYR, ATRT-SHH, ATRT-MYC) defined by DNA methylation and transcriptional signature despite near-identical underlying SMARCB1 genetics (Ho et al., consensus reinvestigation, *Neuro-Oncology* 2020; academic.oup.com/neuro-oncology/article/22/5/613/5691191). This is a case where **genetic homogeneity masks profound epigenetic heterogeneity** — worth flagging explicitly in a KB `biological_scale: MOLECULAR` node distinct from the syndrome-level genetic node.

**Chromosomal abnormalities:** Monosomy 22 and focal 22q11.23 LOH are the dominant somatic "second hit" mechanisms in tumors; germline 22q11.23 deletions/translocations are a rarer constitutional first-hit mechanism (above).

---

## 5. Environmental Information

Not applicable as a causal contributor to RTPS1 (monogenic germline syndrome). No infectious agent, toxin, or lifestyle factor is implicated in causing SMARCB1 germline loss-of-function variants or in triggering the somatic second hit specifically in RTPS1 carriers, based on the literature retrieved. Post-treatment exposure-avoidance guidance (radiation, tobacco, UV, chemotherapy) targets **secondary/therapy-related malignancy risk in survivors**, not primary RTPS1 causation — this belongs in a treatment/survivorship node, not an `environmental[]` causal-mechanism node, if curated in dismech.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (RTPS1 → AT/RT, as the flagship manifestation; parallel chain applies to RTK/extrarenal MRT with organ-specific cell-of-origin substituted):**

1. Heterozygous germline SMARCB1 loss-of-function variant (nonsense/frameshift/splice/deletion) → **reduces SMARCB1 gene dosage in every cell**, establishing the first hit (constitutional, present from conception; inferred as clonally neutral in most tissues until step 2).
2. Somatic inactivation of the remaining wild-type SMARCB1 allele in a susceptible progenitor cell (commonly via monosomy 22 or focal LOH) → **leads to** complete biallelic SMARCB1 loss in that cell lineage — the second hit, demonstrated by IHC-null INI1 staining in tumor tissue.
3. Complete SMARCB1 loss **does not destroy** overall SWI/SNF (BAF) complex structural integrity, but **destabilizes its chromatin occupancy** — the complex is redistributed away from gene promoters and typical enhancers and toward aberrant occupancy of super-enhancers (mechanistic claim from chromatin-profiling studies discussed in the SWI/SNF-mechanism literature retrieved; this is an *inferred mechanistic model* built from ChIP-seq/ATAC-seq studies, not a single definitive human-tissue demonstration).
4. Aberrant SWI/SNF occupancy at super-enhancers → **drives** activation of oncogenic transcriptional programs and **promotes** proliferation while simultaneously **blocking** lineage differentiation — the combined proliferation-plus-differentiation-block signature characteristic of rhabdoid tumor cells.
5. In parallel, loss of residual SWI/SNF antagonism → **leaves Polycomb Repressive Complex 2 (PRC2)/EZH2 activity unopposed** → PRC2 **represses differentiation-gene programs** genome-wide (this branch is the mechanistic rationale for EZH2-inhibitor therapy, §12; PMID:24853101, "Mechanisms by which SMARCB1 loss drives rhabdoid tumor growth").
6. The combined block-in-differentiation-plus-driven-proliferation state in a susceptible progenitor (neural crest-derived for CNS/peripheral rhabdoid tumors per murine lineage-tracing, PMID:28824165; renal progenitor for RTK) → **results in** clonal expansion into a histologically rhabdoid, clinically aggressive malignant tumor.
7. Because the germline first hit is present in **every cell**, and because susceptible progenitor populations are broadly distributed and abundant specifically during early embryonic/fetal development, the probability of an early independent second hit occurring in *multiple* susceptible cells is elevated relative to sporadic (non-germline) rhabdoid tumor → **explains** the RTPS1-defining clinical pattern of very early onset and frequent synchronous/multifocal disease (an inference bridging molecular mechanism to the clinical epidemiology in §3/§9, not a directly demonstrated single-study claim).

**Branch point — AT/RT molecular subgrouping:** Downstream of step 4/5, AT/RT tumors resolve into three DNA-methylation-defined molecular subgroups despite shared SMARCB1-null status (Torchia et al. foundational classification; consensus reinvestigation Ho et al., *Neuro-Oncology* 2020, academic.oup.com/neuro-oncology/article/22/5/613/5691191):
- **ATRT-TYR** — typically infratentorial/posterior fossa, congenital/very early infantile onset, associated with **better overall survival**, and uniquely shows tumor-infiltrating NK-cell and CD4+ T-cell populations not seen in the other two subgroups (immune-microenvironment branch).
- **ATRT-SHH** — enriched for supratentorial location, further resolved into SHH-1A (median onset ~18 months, 88% supratentorial), SHH-1B (median ~107 months — notably older, atypical for AT/RT), and SHH-2 (median ~13 months, 93% infratentorial/pineal-region) subclusters; associated with **inferior outcomes**, largely attributable to elevated metastatic risk.
- **ATRT-MYC** — supratentorial, universally sensitive in vitro to multi-targeted tyrosine kinase inhibitors, representing a distinct therapeutic-vulnerability branch.

**Molecular pathways:** SWI/SNF (BAF) chromatin remodeling complex (core subunit loss); Polycomb Repressive Complex 2 / EZH2-mediated H3K27 trimethylation (unopposed following SWI/SNF loss); SHH pathway activation (ATRT-SHH subgroup); MYC pathway activation (ATRT-MYC subgroup).

**Cellular processes:** Blocked cellular differentiation; dysregulated cell-cycle progression/proliferation; in ATRT-TYR, an immune-infiltrated tumor microenvironment (NK/CD4+ T-cell).

**Protein dysfunction:** Complete loss of SMARCB1 protein (not misfolding/aggregation) — a null/loss-of-expression mechanism, confirmed diagnostically by absent INI1 nuclear immunostaining.

**Suggested ontology terms:**
- GO (biological process): GO:0006338 (chromatin remodeling); GO:0016569 (covalent chromatin modification); consider a specific SWI/SNF complex assembly/positioning term if curating at that granularity.
- GO (cellular component): GO:0016514 (SWI/SNF complex).
- GO (molecular function): consider PRC2/EZH2 methyltransferase activity term for the differentiation-repression branch.
- CL (cell type): neural-crest-derived progenitor terms for CNS/peripheral rhabdoid tumor cell-of-origin (per murine lineage tracing); renal progenitor terms for RTK — I did not resolve exact CL CURIEs in this pass and would defer to the dismech-terms skill/OAK lookup before binding.
- UBERON: cerebellum/posterior fossa (AT/RT predominant site); kidney (RTK).

**Molecular profiling:** DNA methylation array profiling is the field-standard tool for ATRT subgroup assignment (rather than transcriptomics alone), reflecting the epigenetics-dominant biology described above. Single-cell/spatial transcriptomic characterization of the ATRT-TYR immune microenvironment is an active area (referenced generally in the molecular-landscape reviews retrieved; I did not pull a specific single-cell-atlas primary paper in this pass).

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: CNS (predominantly cerebellum/posterior fossa, >50% of CNS cases; supratentorial in the ATRT-SHH/MYC subgroups), kidney.
- Secondary/other primary sites: head and neck, paravertebral muscle, liver, bladder, mediastinum, retroperitoneum, pelvis, heart (extrarenal/extracranial rhabdoid tumor sites, per GeneReviews).
- Body systems: nervous system, renal/urinary system, and — in the extrarenal category — essentially any soft-tissue compartment.

**Tissue/cell level:** Rhabdoid tumor cells are characterized histologically by eccentric nuclei, prominent nucleoli, and eosinophilic cytoplasmic inclusions (classic "rhabdoid" morphology); cell of origin is inferred as neural-crest-derived progenitor for CNS/peripheral tumors based on murine lineage-tracing models (PMID:28824165) and renal progenitor for RTK.

**Subcellular level:** SMARCB1/SWI/SNF complex function is nuclear (chromatin-bound); the pathophysiology is a nuclear chromatin-regulatory defect (GO Cellular Component: nucleus/chromatin; SWI/SNF complex, GO:0016514) rather than a cytoplasmic or organellar process.

**Localization:** No consistent laterality pattern reported; AT/RT posterior-fossa tumors are often midline/cerebellar rather than lateralized.

---

## 8. Temporal Development

**Onset:** Congenital to early infantile — median age 4–7 months for RTPS1-associated tumors versus ~18 months for sporadic rhabdoid tumors (PMC12062526); a subset present within the first 28 days of life (congenital). Onset pattern is acute/aggressive rather than insidious.

**Progression:** Rapid and aggressive by nature — European Rhabdoid Registry data (as summarized secondarily in PMC12062526) report 84.5% of RTPS patients experience progression during follow-up, with 48% progressing on active chemotherapy; 91% of relapses in the ACNS0333 COG trial cohort occurred within 2 years of enrollment (PMID:32105509). Disease course is not relapsing-remitting but progressive/refractory in a large fraction of cases.

**Patterns:** No spontaneous remission pattern is described; remission is treatment-induced only, and durable remission remains a minority outcome (see §11 survival figures). The literature explicitly frames early infancy (birth–5 years) as the **critical surveillance window**, after which tumor risk "dramatically decreases" (GeneReviews) — the basis for surveillance protocols tapering after age 5 (§10).

---

## 9. Inheritance and Population

**Epidemiology:** Rhabdoid tumors overall are rare — annual incidence in children under 1 year: AT/RT ~8.1 per million, extracranial MRT ~5 per million, dropping to 0.6–2.2 per million at ages 1–4 years (GeneReviews). AT/RT constitutes <2–3% of all pediatric CNS tumors. RTPS1-attributable fraction: ~25–35% of newly diagnosed rhabdoid tumor patients overall, rising to ~55% of those diagnosed under 6 months of age (PMC12062526).

**Inheritance pattern:** Autosomal dominant. The large majority of RTPS1 cases are **de novo**; germline variants can arise on either the maternal or paternal allele. Inherited transmission from an unaffected or undiagnosed late-onset parent is reported but rare.

**Penetrance:** High — "penetrance of SMARCB1-related RTPS may be extremely high (>90% by age 5 years)," per GeneReviews, with the caveat (stated explicitly in the source, not my own hedge) that this estimate may be inflated by ascertainment bias absent systematic population-level screening. This contrasts with RTPS2 (SMARCA4), where penetrance is explicitly incomplete — flagging this distinction because it directly changes surveillance and counseling guidance between the two genes (do not extrapolate SMARCA4 penetrance data onto SMARCB1 carriers or vice versa).

**Expressivity:** Variable — "the types of RTPS-related tumors vary among family members with the same disease-causing variant" (GeneReviews), i.e., intrafamilial heterogeneity in tumor site/type even with an identical germline variant.

**Germline mosaicism:** Documented in SMARCB1-related RTPS1 and estimated to account for **up to half of families with multiple affected siblings** where parental testing is otherwise negative (GeneReviews) — directly relevant to recurrence-risk counseling when parental blood testing is uninformative.

**Founder effects / consanguinity / carrier frequency:** No RTPS1-specific founder populations, consanguinity association, or general-population carrier-frequency estimate was identified in this search pass; given the near-uniform de novo origin and high penetrance (functionally incompatible with silent carriage at meaningful population frequency), a meaningful "carrier frequency" concept does not straightforwardly apply the way it would for a recessive condition.

**Population demographics:** No specific ethnic/geographic enrichment was identified in the sources reviewed; the condition appears panethnic, consistent with its predominantly de novo mutational origin. Sex ratio was not reported as skewed in the sources reviewed.

---

## 10. Diagnostics

**Diagnostic criteria (GeneReviews):** Diagnosis is established in a proband who has (a) a rhabdoid tumor and/or a family history of rhabdoid tumor and/or multiple SMARCB1-deficient tumors (synchronous or metachronous), **and** (b) identification of a disease-causing germline variant in SMARCB1 by molecular genetic testing.

**Suggestive clinical features prompting testing:** congenital presentation or onset within the first 28 days of life; rhabdoid tumor diagnosed under 12 months of age; advanced-stage disease at diagnosis; synchronous/multiple primary rhabdoid tumors; family history of rhabdoid tumor or SCCOHT (the latter specific to SMARCA4/RTPS2).

**Laboratory/pathology:** Immunohistochemical loss of SMARCB1 (INI1) nuclear staining in tumor tissue is the pathognomonic tumor-level finding (present regardless of germline vs. purely somatic origin) — this is a tumor-diagnostic test, not itself proof of germline RTPS1 status.

**Molecular genetic testing:**
- Sequence analysis detects ~49% of RTPS1 probands; gene-targeted deletion/duplication analysis detects an **additional** ~51% (GeneReviews) — reinforcing that copy-number analysis is not optional.
- Multigene panel testing (SMARCB1, SMARCA4, and related genes) is an alternative first-line approach.
- Constitutional karyotype/CMA is indicated when a 22q11.23 structural rearrangement (deletion or balanced translocation) is suspected and not captured by sequencing (PMID:37548271, PMID:21412926).

**Whole-body MRI at diagnosis:** Recommended for **all** individuals regardless of age at initial RTPS1 diagnosis (GeneReviews) to detect synchronous occult tumors.

**Surveillance protocol** (SIOPE Host Genome Working Group consensus, Foulkes et al., summarized in GeneReviews and PMC8484234):

| Age | Recommended surveillance |
|---|---|
| Birth–6 months | Monthly (or at least every 2–3 months) clinical + neurologic exam; abdominal + neck ultrasound; head ultrasound or brain/spine MRI, or whole-body MRI |
| 7–18 months | Every 2–3 months clinical/neurologic exam + abdominal/neck ultrasound; consider brain/spine MRI |
| 19 months–5 years | Every 3 months clinical/neurologic exam + abdominal/neck ultrasound + brain/spine MRI |
| >5 years | Every 6 months clinical/neurologic exam; annual whole-body MRI (tumor risk "dramatically decreases" after age 5, per source language) |

An earlier/alternative formulation of the same 2017 expert consensus (Foulkes et al., *Clin Cancer Res* 2017, aacrjournals.org/clincancerres/article/23/12/e62/80076) specifies brain MRI every 3 months to age 5, abdominal ultrasound every 3 months **with no upper age limit**, and annual whole-body MRI from age 5 onward. **Critically: screening is explicitly not recommended for carriers of a germline missense SMARCB1 variant**, because that genotype tracks with schwannomatosis/Coffin-Siris rather than malignant RTPS1 risk (§4/§9 genotype-phenotype correlation) — this is a case where genotype, not just carrier status, should gate surveillance intensity in any curated definition/algorithm.

**Differential diagnosis (key discriminators — same locus, different disease):**
- **SMARCB1-related schwannomatosis** — non-truncating (missense/hotspot) variants, adult-onset benign cranial/peripheral schwannomas and meningiomas, **not** RTPS1. Co-occurrence of schwannomatosis and RTPS1 in the same family has been reported (PMC6081224) but reflects distinct variant classes, not the same clinical entity.
- **Coffin-Siris syndrome** (and the Coffin-Siris/Nicolaides-Baraitser intermediate phenotype) — developmental/dysmorphic syndrome from missense or in-frame SMARCB1 (or other BAF-complex-gene) variants, without rhabdoid tumor predisposition.
- **RTPS2** (SMARCA4) — allelic-locus counterpart; earlier onset, more aggressive, incomplete penetrance, additional SCCOHT risk.
- **Li-Fraumeni syndrome (TP53)** — broader cancer spectrum; rare co-occurrence of TP53-mutant SMARCB1/SMARCA4-deficient tumors reported.
- **KBG syndrome (ANKRD11)** — developmental/skeletal syndrome with a rare reported paratesticular rhabdoid tumor association.
- **BAP1 tumor predisposition syndrome, DICER1 tumor predisposition** — distinguished by absence of clinical/family history of rhabdoid tumor specifically.

**Screening for asymptomatic at-risk relatives:** Molecular testing for the known familial SMARCB1 variant clarifies at-risk relative status; when neither parent tests positive, germline mosaicism remains a live possibility and does not exclude recurrence risk in future pregnancies. Prenatal testing and preimplantation genetic testing are available once a familial variant is identified; because RTPS1 tumors can arise prenatally, high-resolution prenatal ultrasound is recommended when a fetus is known to carry the familial variant (GeneReviews).

---

## 11. Outcome/Prognosis

**Survival:** Overall 5-year survival for rhabdoid tumor generally is reported **below 30%** (PMC12062526), with RTPS1 (germline) cases carrying a **worse prognosis than sporadic (non-germline) rhabdoid tumor**, though long-term survivors are reported (GeneReviews, qualitative statement — exact RTPS1-vs-sporadic hazard ratio was not retrieved in this pass).

**Landmark trial outcome data (ACNS0333, COG phase III/II, PMID:32105509, *J Clin Oncol* 2020):** In 65 evaluable AT/RT patients treated with induction chemotherapy → 3 cycles of high-dose consolidation chemotherapy with stem-cell rescue (thiotepa, carboplatin) → focal 3D-conformal radiotherapy, **4-year event-free survival was 37% (95% CI 25–49%) and overall survival 43% (95% CI 31–55%)** — a substantial improvement over historical POG9233/4 + CCG9921 cohorts, which achieved only 6.4% 24-month EFS. 91% of relapses occurred within 2 years of enrollment. Note this trial cohort mixes germline and non-germline AT/RT; it is not an RTPS1-exclusive outcome figure, and that distinction should be preserved in any KB citation.

**Prognostic stratifiers reported:**
- Age at diagnosis and localized vs. metastatic/synchronous disease at presentation — localized disease receiving multimodal therapy achieves substantially better outcomes (~46.8% 5-year OS cited in PMC12062526) than synchronous/multifocal presentation.
- Concurrent AT/RT plus extrarenal tumor: only ~13% overall survival despite aggressive therapy (PMC12062526) — the single worst-prognosis stratum identified in this pass.
- Molecular subgroup within AT/RT specifically: ATRT-TYR (better OS) vs. ATRT-SHH (inferior OS, driven by metastatic risk) vs. ATRT-MYC (intermediate, distinguished more by drug sensitivity than baseline prognosis) — DNA-methylation subgrouping was reported to carry **no additional prognostic significance within the ATRT-SHH subgroup specifically** in a clinical-trial-cohort re-analysis (PMC10412479), a useful negative finding worth preserving rather than over-generalizing subgroup-prognosis claims.
- SMARCA4 (RTPS2) vs. SMARCB1 (RTPS1) germline status: SMARCA4-mutated AT/RT is associated with younger age, higher germline mutation frequency, and inferior prognosis relative to SMARCB1-mutated cases — again, keep this as a RTPS1-vs-RTPS2 contrast, not folded into RTPS1's own outcome figures.

**Complications:** Intensive multimodal therapy (surgery + high-dose chemotherapy + radiotherapy) in infants carries a high rate of treatment-related secondary complications (GeneReviews, qualitative), motivating the "risk-reducing" strategy discussion in §12 (deferring/replacing radiotherapy, proton therapy, earlier targeted-agent use).

---

## 12. Treatment

**Standard multimodal chemoradiotherapy (COG regimen, ACNS0333):** surgical resection + 2 cycles induction chemotherapy (cisplatin, cyclophosphamide, etoposide, vincristine, methotrexate) + 3 cycles high-dose consolidation chemotherapy with autologous stem-cell rescue (thiotepa, carboplatin) + focal 3D-conformal radiotherapy (pre- or post-consolidation) (PMID:32105509). Suggested NCIT terms: NCIT:C15632 (Chemotherapy), NCIT:C15313 (Radiation Therapy), NCIT:C15329 (Surgical Procedure); NCIT:C15431 or transplantation-specific term for stem-cell rescue.

**Risk-reducing strategy discussion (RTPS1-specific consideration, per GeneReviews):** given the very young age at diagnosis and secondary-malignancy/neurotoxicity risk of radiotherapy in infants, guidance explicitly raises **postponing or replacing radiotherapy with high-dose chemotherapy or proton-beam therapy**, and using targeted therapy concomitantly with or before standard chemotherapy — framed as an active area of clinical judgment rather than a settled protocol.

**EZH2 inhibition (tazemetostat/Tazverik):** Mechanistically rationalized by the unopposed-PRC2 branch of pathophysiology (§6, step 5). FDA granted **accelerated approval in January 2020** for epithelioid sarcoma (age ≥16) and **June 2020** for relapsed/refractory EZH2-mutant follicular lymphoma (neither indication is rhabdoid-tumor-specific). A dedicated pediatric trial in **INI1(SMARCB1)-negative tumors** (NCT02601937) enrolled dose-expansion cohorts of ~20 AT/RT and ~20 MRT/RTK/rhabdoid-feature patients; **efficacy was limited — only a subset of intracranial AT/RT patients showed objective response, while extracranial rhabdoid tumors were essentially uniformly resistant.** **Important currency note for this KB entry:** as of August 2026, Ipsen has voluntarily withdrawn the FDA indications for tazemetostat in follicular lymphoma and epithelioid sarcoma; I did not find confirmation in this pass of whether this withdrawal affects the separate pediatric INI1-negative-tumor development pathway specifically — flag as needing a fresh check before citing tazemetostat as an available agent, rather than asserting current availability.

**Other emerging/investigational agents cited across sources (treat as investigational, not standard of care):** HDAC inhibitors (vorinostat), CDK4/6 inhibitors (palbociclib, abemaciclib), PARP inhibitors, PD-1/PD-L1 checkpoint inhibitors, CAR-T cell approaches, and multi-targeted tyrosine kinase inhibitors (rationalized specifically for the ATRT-MYC subgroup's demonstrated in vitro sensitivity) and NOTCH inhibitors (rationalized for a subset of ATRT-SHH). None of these have RTPS1/AT/RT-specific regulatory approval based on sources reviewed here.

**RTPS2-specific risk-reduction (contrast only, not RTPS1 content):** prophylactic risk-reducing bilateral salpingo-oophorectomy after family planning is discussed for SMARCA4/RTPS2 carriers given SCCOHT risk — this does **not** apply to RTPS1/SMARCB1 carriers and should not be cross-applied.

**Survivorship exposure guidance:** limit DNA-damaging exposures (radiation including diagnostic CT, tobacco, UV, further chemotherapy) post-treatment to reduce secondary-malignancy risk in RTPS1 survivors (GeneReviews).

---

## 13. Prevention

**Primary prevention:** Not applicable in the vaccination/exposure-avoidance sense — RTPS1 is a germline monogenic condition with no known modifiable environmental trigger.

**Secondary prevention / early detection:** The entire clinical-management apparatus for RTPS1 is essentially a secondary-prevention (early-detection) framework — see the structured surveillance protocol in §10, which functions as population-level early detection within the known-carrier population rather than population screening.

**Genetic screening:** Cascade testing of at-risk relatives once a familial SMARCB1 variant is identified; prenatal testing and preimplantation genetic testing available for known familial variants (§10). Newborn screening in the population-wide sense does not apply (RTPS1 is not on standard newborn metabolic/genetic screening panels; detection is via targeted familial cascade testing or diagnostic workup of an index tumor).

**Genetic counseling:** Central to management — clarifying at-risk relative status, explaining the up-to-50%-of-multiplex-families germline-mosaicism possibility when parental testing is negative, and coordinating prenatal/preimplantation options (§9, §10).

**Tertiary prevention:** Exposure-avoidance guidance in survivors to reduce secondary/therapy-related malignancy risk (§12).

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal rhabdoid tumor or SMARCB1-deficient disease was identified in this search pass (I did not query OMIA directly; if this is needed for the KB's animal-models section, an OMIA-specific search should be run before asserting absence). All animal data retrieved in this pass are **engineered laboratory models** (below), not naturally occurring disease in another species.

**Orthologous gene:** Smarcb1 (mouse, MGI:1917258) is the standard ortholog used in modeling.

---

## 15. Model Organisms

**Mouse — conditional/tissue-specific Smarcb1 knockout:** Neural-crest-specific Smarcb1 inactivation is sufficient to initiate rhabdoid-like tumorigenesis in cranial nerves and meninges, reproducing typical histologic and molecular features of human rhabdoid tumors (Vitte et al., *Nat Commun* 2017, PMID:28824165, "Timing of Smarcb1 and Nf2 inactivation determines schwannoma versus rhabdoid tumor development"). This study's central finding — directly relevant to the RTPS1/schwannomatosis distinction in §4/§9/§10 — is that the **developmental timing** of Smarcb1 loss (early vs. late in the neural-crest lineage), not just the variant class, determines whether the resulting tumor is a malignant rhabdoid tumor or a benign schwannoma; this nuances but does not replace the truncating-vs-missense genotype-phenotype rule as the dominant clinical predictor.

**Broader validation:** Smarcb1 has been functionally validated as a bona fide tumor suppressor in mouse models — germline/conditional Smarcb1 inactivation is reported to produce rapid, highly penetrant tumor development (cited generally across the SWI/SNF-mechanism literature retrieved in this pass). I was not able to independently pin an exact primary PMID for the foundational Smarcb1+/− mouse tumor-suppressor validation studies in this search pass (I recall this line of work, associated with the Roberts laboratory, from general background knowledge, but per your attribution standard I am not asserting an unverified PMID — this citation should be confirmed directly against PubMed before being written into a KB evidence block).

**Model characteristics:** The neural-crest-lineage conditional model recapitulates cranial-nerve/meningeal rhabdoid tumor histology and molecular profile with apparent high fidelity for that anatomic compartment; it does not, on the evidence retrieved here, establish an equally validated model for renal (RTK) or hepatic/extracranial rhabdoid tumor sites, which would need separate lineage-specific conditional models to claim the same fidelity — flag as a gap rather than assume generalization across all RTPS1 tumor sites.

**Applications:** These models are used to dissect (a) the SMARCB1-loss → SWI/SNF redistribution → oncogenic-transcription mechanism (§6), (b) the developmental-timing/cell-of-origin determinant of rhabdoid-tumor-vs-schwannoma phenotype, and (c) preclinical testing of EZH2 inhibitors and other targeted agents against the PRC2-unopposed mechanistic branch.

**Resources:** MGI (Smarcb1 mouse strains, conditional/floxed alleles); IMPC/KOMP for knockout allele availability — not independently queried in this pass.

---

## Summary of Notable Evidence Gaps (flagged per attribution standard rather than smoothed over)

- No RTPS1-specific ORPHA/MONDO CURIE distinct from the general "Rhabdoid tumor predisposition syndrome" umbrella term (ORPHA231108/MONDO:0016473) was resolved in this pass.
- No current gnomAD pLI/LOEUF constraint value for SMARCB1 was retrieved — needs a direct gnomAD browser pull.
- The foundational Smarcb1+/− mouse tumor-suppressor-validation PMID could not be independently confirmed in this pass and should not be cited without verification.
- RTPS1-specific (as opposed to general pediatric-oncology) quality-of-life instrument data were not located.
- The European Rhabdoid Registry progression statistics (84.5%/48%) were retrieved only via a secondary review source (PMC12062526) and not traced to the registry's own primary publication in this pass.
- Whether the August 2026 Ipsen withdrawal of tazemetostat's follicular-lymphoma/epithelioid-sarcoma indications affects the separate pediatric INI1-negative-tumor program was not resolved and needs a fresh check before this report is used to populate a treatments block.

---

## Sources

- [OMIM #609322 — RHABDOID TUMOR PREDISPOSITION SYNDROME 1](https://omim.org/entry/609322)
- [Rhabdoid Tumor Predisposition Syndrome — GeneReviews (NBK469816)](https://www.ncbi.nlm.nih.gov/sites/books/NBK469816/)
- [Rhabdoid Tumor Predisposition Syndrome Type 1 (PDQ®) — NCI (NBK602739)](https://www.ncbi.nlm.nih.gov/books/NBK602739/)
- [Rhabdoid Tumor Predisposition Syndrome: A Comprehensive Review of Genetics, Clinical Manifestations, and Management (PMC12062526)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12062526/)
- [Rhabdoid Tumor Predisposition Syndrome: From Clinical Suspicion to General Management (PMC7937887)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7937887/)
- [Current recommendations for clinical surveillance and genetic testing in rhabdoid tumor predisposition: SIOPE Host Genome Working Group (PMC8484234)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8484234/)
- [Cancer Surveillance in Gorlin Syndrome and Rhabdoid Tumor Predisposition Syndrome — Clin Cancer Res (Foulkes et al.)](https://aacrjournals.org/clincancerres/article/23/12/e62/80076)
- [Rhabdoid tumor predisposition syndrome: a historical review of treatments and outcomes — PubMed](https://pubmed.ncbi.nlm.nih.gov/38553892/)
- [Efficacy of High-Dose Chemotherapy and 3D Conformal Radiation for AT/RT — COG ACNS0333, JCO 2020 — PubMed](https://pubmed.ncbi.nlm.nih.gov/32105509/)
- [Mechanisms by which SMARCB1 loss drives rhabdoid tumor growth — PubMed](https://pubmed.ncbi.nlm.nih.gov/24853101/)
- [Timing of Smarcb1 and Nf2 inactivation determines schwannoma versus rhabdoid tumor development — Nature Communications](https://www.nature.com/articles/s41467-017-00346-5)
- [SMARCB1 mutations in schwannomatosis and genotype correlations with rhabdoid tumors — PubMed](https://pubmed.ncbi.nlm.nih.gov/24933152/)
- [Premature termination of SMARCB1 translation... schwannomatosis vs rhabdoid tumors — PubMed](https://pubmed.ncbi.nlm.nih.gov/24740647/)
- [Co-occurrence of schwannomatosis and rhabdoid tumor predisposition syndrome 1 (PMC6081224)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6081224/)
- [Constitutional balanced translocations involving SMARCB1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/37548271/)
- [Congenital anomalies and rhabdoid tumor associated with 22q11 germline deletion — PubMed](https://pubmed.ncbi.nlm.nih.gov/21412926/)
- [Molecular subgrouping of atypical teratoid/rhabdoid tumors — reinvestigation and current consensus — Neuro-Oncology](https://academic.oup.com/neuro-oncology/article/22/5/613/5691191)
- [Current Molecular and Clinical Landscape of ATRT — The Link to Future Therapies (PMC10712249)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10712249/)
- [DNA-methylation subgroups carry no prognostic significance in ATRT-SHH clinical trial cohorts (PMC10412479)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10412479/)
- [Atypical teratoid/rhabdoid tumoroids reveal subgroup-specific drug vulnerabilities — Oncogene](https://www.nature.com/articles/s41388-023-02681-y)
- [Tazverik (Tazemetostat) FDA approval history — AHDB](https://www.ahdbonline.com/issues/2020/august-2020-vol-13-payers-guide/tazverik-tazemetostat-first-fda-approved-treatment-specifically-for-patients-with-epithelioid-sarcoma)
- [FDA indications for tazemetostat voluntarily withdrawn — OncLive](https://www.onclive.com/view/fda-indications-for-tazemetostat-in-r-r-follicular-lymphoma-and-epithelioid-sarcoma-are-voluntarily-withdrawn)
- [EZH2 Inhibitor Tazemetostat in Pediatric Subjects With Relapsed or Refractory INI1-Negative Tumors — NCT02601937 SAP](https://cdn.clinicaltrials.gov/large-docs/37/NCT02601937/SAP_001.pdf)
- [Orphanet: Rhabdoid tumor predisposition syndrome (ORPHA231108)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=231108)
- [Orphanet: Atypical teratoid rhabdoid tumor (ORPHA99966)](https://www.orpha.net/en/disease/detail/99966)
- [Malignant Rhabdoid Tumor and Related Pediatric Tumors: Multimodality Imaging Review — RadioGraphics](https://pubs.rsna.org/doi/abs/10.1148/rg.240015)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016569` (obsolete covalent chromatin modification) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016569` (1 mention) - the report calls it "covalent chromatin modification"; GO calls it **obsolete covalent chromatin modification**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.

13 of 16 terms resolved to a current term; the rest could not be looked up either way.