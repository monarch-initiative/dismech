---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-31T19:54:48.384267'
end_time: '2026-08-31T19:59:42.898798'
duration_seconds: 294.51
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Rhabdoid Tumor Predisposition Syndrome 2
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
  web_search_requests: 16
  num_turns: 22
  total_cost_usd: 1.2743475999999998
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
citation_count: 22
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 13
  off_topic: 1
  off_topic_references:
  - PMC:PMC2868905
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 14
  verified: 12
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 9
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0031065
    ontology_label: obsolete positive regulation of histone deacetylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rhabdoid Tumor Predisposition Syndrome 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Rhabdoid Tumor Predisposition Syndrome 2** covering all of the
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

# Rhabdoid Tumor Predisposition Syndrome 2 (RTPS2) — Research Report

**Scope note (lump/split):** This report covers the germline cancer-predisposition syndrome RTPS2 (OMIM #613325), caused by heterozygous germline loss-of-function *SMARCA4* variants. It deliberately separates RTPS2 from the *somatic* tumor types it predisposes to — small cell carcinoma of the ovary, hypercalcemic type (SCCOHT), atypical teratoid/rhabdoid tumor (AT/RT), and extracranial malignant rhabdoid tumor (eMRT) — and from a *biallelic-somatic-only* entity, SMARCA4-deficient thoracic sarcoma/NSCLC, which the literature explicitly excludes from the germline syndrome (no germline mutations reported; strongly smoking-associated) ([Journal of Thoracic Oncology](https://www.jto.org/article/S1556-0864(19)33643-3/fulltext)). It is also allelic to, but clinically distinct from, Coffin-Siris syndrome 4 (SMARCA4-related), a developmental disorder driven predominantly by missense/dominant-negative variants rather than truncating loss-of-function.

---

## 1. Disease Information

**Identifiers:** OMIM #613325 (RTPS2) ([OMIM](https://omim.org/entry/613325)); MONDO:0013224; Gene: *SMARCA4* (HGNC:11100), chr19p13.2, transcript NM_001128849.3 (36 exons per GeneReviews) / NM_003072.5 (ClinVar convention); Allelic locus OMIM *603254 (SMARCA4). GeneReviews chapter: "Rhabdoid Tumor Predisposition Syndrome" (covers both RTPS1/*SMARCB1* and RTPS2/*SMARCA4*) ([NCBI Bookshelf NBK469816](https://www.ncbi.nlm.nih.gov/sites/books/NBK469816/)). NCI PDQ Genetics summary is split into RTPS1 and RTPS2 (PDQ RTPS2, [NBK613400](https://www.ncbi.nlm.nih.gov/books/NBK613400/)).

**Overview:** RTPS2 is an autosomal dominant cancer-predisposition syndrome caused by heterozygous germline loss-of-function variants in *SMARCA4*, encoding BRG1, the mutually-exclusive catalytic ATPase subunit of the BAF (SWI/SNF) chromatin-remodeling complex. It is the minor genetic subtype of rhabdoid tumor predisposition syndrome, accounting for roughly 5–15% of germline-confirmed RTPS cases against 85–95% for RTPS1/*SMARCB1* (GeneReviews); in the EU-RHAB registry's 90 germline-confirmed cases, 6 carried *SMARCA4* variants (~6.7%) (PDQ RTPS2). Unlike RTPS1, RTPS2 shows incomplete penetrance and a distinct associated tumor spectrum dominated by SCCOHT rather than infantile AT/RT/eMRT.

**Synonyms:** BRG1-related rhabdoid tumor predisposition; familial rhabdoid tumor (SMARCA4-related).

**Evidence base:** Predominantly aggregated disease-level resources — GeneReviews, OMIM, PDQ, ClinGen — built from case series and registries (EU-RHAB), not large-scale EHR cohorts, reflecting the rarity of the condition.

---

## 2. Etiology

**Causal factor:** Heterozygous germline loss-of-function *SMARCA4* variants (nonsense, frameshift, canonical splice-site, whole/partial gene deletion) predisposing to tumors that arise on somatic biallelic inactivation (loss of the wild-type allele or a second somatic truncating hit) — the discovery family (2 German sisters, early-onset fatal rhabdoid tumors) carried germline p.Arg1189* with tumor-restricted somatic second-hit inactivation (Schneppenheim et al. 2010, *Am J Hum Genet* 86:279–284, PMID:[20137775](https://pubmed.ncbi.nlm.nih.gov/20137775/)).

**Genetic risk factors:** The germline variant itself is the dominant risk factor. No common susceptibility loci or modifier-gene data specific to RTPS2 were identified in this search; modifier genetics are essentially uncharacterized for this rare syndrome. Variant type (truncating vs. missense) is the key genotype-phenotype determinant separating RTPS2/cancer risk from Coffin-Siris syndrome 4 (missense, dominant-negative) — "truncating mutations in the SMARCA4 gene typically lead to rhabdoid tumor predisposition syndrome (RTPS), whereas missense mutations are typically associated with Coffin-Siris syndrome," though this is not an absolute rule, as haploinsufficient missense/splice alleles can also cause milder CSS phenotypes (PMC5601212, PMC10897839-adjacent literature).

**Environmental/lifestyle factors:** None established for the germline syndrome. This is explicitly distinguished from the biallelic-somatic SMARCA4-deficient thoracic sarcoma/NSCLC entity, which is strongly smoking-associated (85.7% smokers, 98.1% male, median age 48) and carries no reported germline mutations (JTO 2019/2020 series, [PMC10875988](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10875988/)) — this is a mechanistically related but etiologically separate somatic cancer, not a manifestation of RTPS2.

**Gene-environment interaction:** No data identified specific to RTPS2.

---

## 3. Phenotypes

RTPS2 itself is a cancer-predisposition state; the "phenotype" is chiefly tumor occurrence, though pediatric framing matters because age of onset differs sharply by tumor type:

| Tumor / finding | HPO suggestion | Onset | Notes / citation |
|---|---|---|---|
| SCCOHT | HP:0100615 (Ovarian neoplasm) / consider a more specific rhabdoid-tumor term if curating | Adolescent–young adult; median 23.9 y (range infancy–56 y) | Most characteristic RTPS2 tumor in females (GeneReviews; PDQ RTPS2) |
| Paraneoplastic hypercalcemia | HP:0003072 (Hypercalcemia) | Concurrent with SCCOHT | Present in up to two-thirds of SCCOHT cases (search synthesis of SCCOHT literature) |
| AT/RT | HP:0030692 or a rhabdoid-tumor-specific term | Younger age than SMARCB1-AT/RT reported for SMARCA4-mutant cases | Rare in RTPS2 vs. RTPS1; molecularly distinct subgroup ([Acta Neuropathol 2020](https://link.springer.com/article/10.1007/s00401-020-02250-7)) |
| Extracranial malignant rhabdoid tumor (eMRT) | — | Variable | Sites: head/neck, paravertebral muscles, liver, bladder, mediastinum, retroperitoneum, pelvis, heart (GeneReviews) |
| SMARCA4-deficient undifferentiated uterine sarcoma | — | Adult | Allelic with SCCOHT in some kindreds (GeneReviews; ScienceDirect Gynecol Oncol 2019 family study) |
| Neuroblastoma | HP:0009830-adjacent (neural crest tumor) | Pediatric | 11 documented cases with germline *SMARCA4* variants (PDQ RTPS2) |

**Severity/progression:** All associated malignancies (SCCOHT, AT/RT, eMRT) are aggressive, high-grade, rapidly progressive tumors requiring urgent multimodal treatment.

**Quality of life:** Not separately characterized for RTPS2; dominated by the morbidity/mortality of the associated malignancies and, in survivors, the burden of intensive multimodal therapy and lifelong surveillance imaging (see §8, §13).

---

## 4. Genetic/Molecular Information

**Causal gene:** *SMARCA4* / HGNC:11100 / OMIM *603254, chr19p13.2. Protein: SMARCA4/BRG1, catalytic ATPase subunit of the BAF (SWI/SNF) complex, mutually exclusive with its paralog SMARCA2 (BRM) within complex assembly.

**Variant spectrum:** GeneReviews: "Reported disease-causing variants include nonsense and splice site variants and intragenic deletions that predict inactivation." Sequence analysis detects a substantial fraction of cases and gene-targeted deletion/duplication analysis is required for the remainder (GeneReviews cites illustrative yields of 4/9 vs 5/9 in a small series, underscoring that both testing modalities are needed).

**Somatic second hit:** Tumor tissue in RTPS2 carriers shows biallelic inactivation via a somatic truncating mutation and/or loss of the wild-type allele in addition to the germline variant — directly demonstrated in the founding family (Schneppenheim 2010, PMID:20137775) and in SCCOHT cohorts, where immunohistochemical loss of nuclear SMARCA4/BRG1 staining was found in 38/40 tumors overall (Witkowski et al. 2014, *Nat Genet* 46:438–443, PMID:[24658002](https://pubmed.ncbi.nlm.nih.gov/24658002/)). A companion paper, Ramos et al. 2014, PMID:[24658001](https://pubmed.ncbi.nlm.nih.gov/24658001/), independently reported frequent inactivating germline and somatic *SMARCA4* mutations in SCCOHT.

**Functional consequence:** Loss of function / haploinsufficiency. "SMARCA4 acts as a haploinsufficient tumor suppressor" with roughly half-normal protein dosage in heterozygous-mutant cells sufficing to produce phenotype in the developmental (Coffin-Siris) context, consistent with a dosage-sensitive gene ([PMC5601212](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5601212/)). It is strongly loss-of-function-constrained in population data (high pLI/low LOEUF category genes of this class), consistent with its essential developmental role (see §6, embryonic lethality data), though this search did not return the exact gnomAD pLI value.

**Allelic disorders:**
- RTPS1 — *SMARCB1*, OMIM #609322 (>85% of RTPS; near-complete, early penetrance; mostly de novo).
- Coffin-Siris syndrome 4 — *SMARCA4*, developmental disorder (missense/dominant-negative, not typically truncating); no established rhabdoid-tumor risk, but overlap cases exist (see below).
- SMARCA4-related developmental eye anomalies — an emerging phenotypic extension of the SMARCA4 loss-of-function spectrum (Chesneau et al. 2026, *Clin Genet*, [10.1111/cge.70143](https://onlinelibrary.wiley.com/doi/10.1111/cge.70143)).
- A documented overlap kindred shows a single inactivating *SMARCA4* variant causing concomitant Coffin-Siris phenotype, microphthalmia, AND SCCOHT in different family members — evidence that the CSS/cancer-risk boundary is not absolute at the genotype level ([PMC5601212](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5601212/)).

**Epigenetics:** SWI/SNF (BAF) loss produces genome-wide chromatin remodeling: collapse of enhancer accessibility at differentiation/developmental loci coupled with gain of accessibility/activity at pro-tumorigenic enhancers — described as a "two-step" enhancer dysregulation process in rhabdoid tumor biology ([PMC10931202](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10931202/)). AT/RT with *SMARCA4* mutation shows a distinct DNA methylation/transcriptomic signature from SMARCB1-deficient AT/RT, supporting classification as a separate molecular subgroup (Acta Neuropathologica 2020, [10.1007/s00401-020-02250-7](https://link.springer.com/article/10.1007/s00401-020-02250-7)).

**Chromosomal abnormalities:** Intragenic deletions are a recognized mechanism (detected by deletion/duplication analysis); large-scale aneuploidy is not a defining feature of the germline syndrome itself (as opposed to somatic tumor genomes, which are often otherwise "quiet"/low-mutation-burden, characteristic of rhabdoid tumors generally).

---

## 5. Environmental Information

No established environmental, lifestyle, or infectious contributing factor for RTPS2 germline predisposition. As noted in §2, smoking is strongly associated with the mechanistically related but etiologically distinct *somatic-only* SMARCA4-deficient thoracic sarcoma/NSCLC entity — this should not be conflated with RTPS2 cancer risk.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, germline pathway):**

1. A heterozygous germline loss-of-function *SMARCA4* variant (nonsense, frameshift, splice-site, or intragenic deletion) is inherited or arises de novo, reducing functional BRG1/SMARCA4 ATPase dosage in all cells (demonstrated: Schneppenheim 2010, PMID:20137775).
2. In a susceptible tissue (ovarian/genital ridge lineage for SCCOHT; neural/renal/soft-tissue progenitors for AT/RT and eMRT), a somatic second hit — truncating mutation or loss of the remaining wild-type allele — leads to biallelic *SMARCA4* inactivation and loss of BAF-complex ATPase activity, demonstrated by IHC loss of nuclear SMARCA4/BRG1 staining in tumor tissue (38/40 tumors in Witkowski et al. 2014, PMID:24658002).
3. Loss of the BAF ATPase leads to genome-wide redistribution of chromatin accessibility: collapse of enhancers driving lineage-differentiation programs and gain of accessibility/activity at enhancers driving proliferative, pro-tumorigenic transcriptional programs — this enhancer-dysregulation step is inferred primarily from SMARCB1-null rhabdoid tumor models and extrapolated to SMARCA4-null tumors, which show a related but molecularly distinguishable epigenomic signature ([PMC10931202](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10931202/); Acta Neuropathologica 2020).
4. Loss of BAF-complex antagonism of Polycomb Repressive Complex 2 (PRC2) results in unopposed EZH2-mediated H3K27 trimethylation, silencing residual tumor-suppressor/differentiation loci — this creates an oncogenic dependency on EZH2 itself ("BAF-PRC2 balance" model), which is the mechanistic basis for EZH2-inhibitor efficacy in these tumors ([Mol Cancer Ther 2017, doi:10.1158/1535-7163.mct-16-0678](https://doi.org/10.1158/1535-7163.mct-16-0678)).
5. Downstream of BAF-complex dysfunction, SMARCA4-determined loss of cyclin D1 expression creates a druggable dependency on CDK4/6 for cell-cycle progression in SCCOHT (Xue et al. 2019, *Nat Commun*, [10.1038/s41467-018-06958-9](https://www.nature.com/articles/s41467-018-06958-9)) — a parallel downstream branch from the same initiating chromatin lesion.
6. The resulting dysregulated transcriptional program (interacting with p16-Rb, Wnt/β-catenin, sonic hedgehog, Polycomb, MYC, and Aurora-A pathways per GeneReviews) drives loss of differentiation and unchecked proliferation, culminating clinically in aggressive, undifferentiated, high-grade malignancy — SCCOHT, AT/RT, or eMRT depending on the tissue of the somatic second hit.

**Molecular pathways:** BAF/SWI/SNF chromatin remodeling; PRC2/EZH2 (antagonistic partner complex); cyclin D1–CDK4/6 cell-cycle axis; Wnt/β-catenin; sonic hedgehog; p16-Rb; MYC; Aurora-A (GeneReviews summary of SWI/SNF pathway interactions).

**Cellular processes:** Loss of cellular differentiation programs, epigenetic silencing of tumor-suppressor loci, cell-cycle dysregulation via cyclin D1 deficiency, super-enhancer hijacking of oncogenic programs.

**Protein dysfunction:** Complete or near-complete loss of BRG1/SMARCA4 nuclear protein expression in tumor tissue (loss-of-function via truncation/degradation), used diagnostically by IHC (GeneReviews; §10).

**Suggested GO terms:** GO:0006338 (chromatin remodeling), GO:0016514 (SWI/SNF complex), GO:0031065 (positive regulation of histone deacetylation — for PRC2/EZH2 crosstalk context), GO:0000122 (negative regulation of transcription by RNA polymerase II). Suggested CL terms depend on tumor type: for SCCOHT, cell-of-origin remains debated (possible germ-cell origin, noted in the PDQ fertility-counseling discussion); for AT/RT/eMRT, primitive neuroectodermal/mesenchymal progenitor populations are implicated but not resolved to a single CL term in this search.

**Molecular profiling:** DNA methylation and transcriptomic profiling distinguish SMARCA4-mutant AT/RT as a separate molecular subgroup from SMARCB1-mutant AT/RT (Acta Neuropathologica 2020). Rhabdoid tumors generally (including SMARCA4-driven cases) are characterized by an otherwise remarkably low somatic mutation burden outside the driver SWI/SNF-gene event — a hallmark supporting a "pure epigenetic driver" oncogenesis model, though this specific point was not independently re-verified with a fresh citation in this search pass.

---

## 7. Anatomical Structures Affected

- **Organ level:** Ovary (SCCOHT — most characteristic RTPS2 manifestation); uterus (SMARCA4-deficient undifferentiated uterine sarcoma); CNS (AT/RT, less common in RTPS2 than RTPS1); and extracranial soft tissue/visceral sites for eMRT — head and neck, paravertebral muscles, liver, urinary bladder, mediastinum, retroperitoneum, pelvis, and heart (GeneReviews). Adrenal/sympathetic chain involvement occurs via the neuroblastoma association (PDQ RTPS2).
- **Body systems:** Reproductive (ovary/uterus), central nervous system, musculoskeletal/soft tissue, hepatobiliary, genitourinary, cardiac.
- **Tissue/cell level:** Undifferentiated/rhabdoid morphology tumor cells characterize all associated malignancies; loss of SMARCA4/BRG1 nuclear expression is the shared immunohistochemical signature (GeneReviews; Witkowski 2014).
- **Subcellular level:** Nuclear — the BAF/SWI/SNF complex operates on chromatin within the nucleus; GO Cellular Component GO:0016514 (SWI/SNF complex) and GO:0005654 (nucleoplasm) are relevant.
- **Localization:** SCCOHT frequently bilateral in reported cases (e.g., a bilateral case in a teenager with germline *SMARCA4* mutation, PMID:[26230154](https://pubmed.ncbi.nlm.nih.gov/26230154/)); eMRT sites are typically unilateral/focal at presentation but with a marked propensity for synchronous/metachronous multifocal tumors in RTPS generally.

---

## 8. Temporal Development

**Onset (RTPS2-specific, contrasted with RTPS1):** RTPS2-associated malignancies show a markedly different age distribution from RTPS1. SCCOHT typically presents in adolescence/young adulthood (median 23.9 years, range infancy to 56 years) rather than infancy (PDQ RTPS2, sourced from Slovenia-cohort epidemiology). This stands in contrast to the classic RTPS statistic that >70% of RTPS overall (dominated by RTPS1/SMARCB1 cases) present before 12 months of age (GeneReviews) — a statistic that should not be mechanically applied to RTPS2, where AT/RT and SCCOHT onset skews later, though SMARCA4-mutant AT/RT is still reported at "younger age" than SMARCB1-mutant AT/RT within the AT/RT subgroup specifically (search synthesis of AT/RT literature).

**Progression:** All associated tumors are rapidly progressive and high-grade at diagnosis. SCCOHT is FIGO-staged; overall survival is 51% for FIGO stage I versus 24% for stage II–IV (PDQ RTPS2), reflecting a steep stage-dependent prognosis gradient typical of an aggressive undifferentiated malignancy.

**Course pattern:** Not relapsing-remitting — these are acute, aggressive primary malignancies requiring immediate multimodal intervention; recurrence/relapse (rather than remission-relapse cycling) is the dominant late-course concern.

**Critical periods:** The lifelong surveillance protocol (GeneReviews; §13) is stratified precisely around age-dependent risk windows: intensive imaging in the first 5 years of life (when AT/RT/eMRT risk, inherited from the wider RTPS spectrum, is highest even in SMARCA4 carriers) transitioning to lifelong biannual pelvic/abdominal ultrasound after puberty for SCCOHT surveillance in female carriers.

---

## 9. Inheritance and Population

**Inheritance pattern:** Autosomal dominant, *SMARCA4*, 19p13.2 (OMIM #613325).

**Penetrance:** Incomplete — the defining genetic-counseling contrast with RTPS1. In the founding kindred, the father was an unaffected heterozygous carrier of the same germline truncating variant (R1189X = p.Arg1189*) transmitted to his affected daughters (Schneppenheim et al. 2010, PMID:20137775). GeneReviews states that most individuals with SMARCA4-related RTPS "inherited a disease-causing variant from a parent without a history of a rhabdoid tumor or SCCOHT" — the inverse of the RTPS1 pattern, where variants are typically de novo with near-complete penetrance by age 5.

**Epidemiology:**
- *SMARCA4* accounts for ~5–15% of germline-confirmed RTPS overall (GeneReviews); EU-RHAB registry: 6/90 germline-confirmed RTPS cases (~6.7%) (PDQ RTPS2).
- Up to 40–43% of SCCOHT cases (a rare, mostly-sporadic ovarian cancer) carry a *germline* SMARCA4 variant, i.e., represent RTPS2 rather than isolated somatic disease (search synthesis; PDQ RTPS2 gives ~40%).
- SCCOHT incidence estimated at 0.12 per million per year (Slovenia national data, PDQ RTPS2) — reflecting the extreme rarity of both the tumor and the underlying syndrome.
- SMARCA4 mutations (germline + somatic combined) account for up to ~2% of AT/RT overall (search synthesis of AT/RT literature); up to 35% of rhabdoid tumors broadly (SMARCB1 + SMARCA4 combined) carry a germline mutation, associated with younger age and worse prognosis regardless of which gene is affected.
- AT/RT overall incidence: 1.4 per million (Germany), 1–3% of pediatric CNS tumors (search synthesis).

**Population/demographic data:** No ethnicity-specific founder effect, consanguinity association, or geographic clustering was identified for *SMARCA4*-RTPS2 in this search (contrast with some other pediatric cancer syndromes). Sex distribution is inherently skewed toward the tumor type: SCCOHT is female-exclusive by organ (ovary); AT/RT/eMRT occur in both sexes.

**Mosaicism:** GeneReviews notes reduced but nonzero risk to sibs of an affected proband whose parents test negative, attributable to possible germline mosaicism, "though less common than in SMARCB1 families" — i.e., germline mosaicism is a recognized but less prominent mechanism in RTPS2 than RTPS1.

---

## 10. Diagnostics

**Diagnostic criteria (GeneReviews):** RTPS2 diagnosis is established by identification of a heterozygous germline loss-of-function *SMARCA4* variant by molecular testing, in the context of an SMARCA4-deficient tumor and/or a family history of rhabdoid tumor/SCCOHT/multiple SMARCA4-deficient tumors.

**Germline testing recommended when:** an SMARCA4-deficient tumor is found with either a family history of rhabdoid tumor OR a family history of nonspecific early-childhood (age <5 years) cancer (GeneReviews).

**Molecular methods:** Sequence analysis of *SMARCA4* plus gene-targeted deletion/duplication analysis (both required — GeneReviews' illustrative small-series yields of 4/9 vs 5/9 detections by each method show neither modality alone is sufficient).

**Tumor-tissue IHC:** Loss of nuclear SMARCA4 (BRG1) staining is a key diagnostic adjunct for SMARCA4-deficient tumors — distinguished from the SMARCB1 (INI1) immunostain used for RTPS1-associated tumors; rare tumors retain SMARCB1 (INI1) but lose SMARCA4 (BRG1), confirming the second, molecularly distinct rhabdoid-tumor driver pathway (PMID:[21566516](https://pubmed.ncbi.nlm.nih.gov/21566516/), "Nonsense mutation and inactivation of SMARCA4 (BRG1) in an atypical teratoid/rhabdoid tumor showing retained SMARCB1 (INI1) expression").

**Imaging:** Ultrasound (abdominal, pelvic, neck) and MRI (brain/spine, whole-body) are the primary surveillance and diagnostic-workup imaging modalities (§13).

**Differential diagnosis (GeneReviews):**
- RTPS1 (*SMARCB1*) — the majority genetic subtype, distinguished by gene and by near-complete early penetrance.
- Li-Fraumeni syndrome (*TP53*) — SMARCB1/SMARCA4-deficient malignant brain tumors can occur with complex copy-number alterations and germline *TP53* variants, a described mimicker/overlap scenario.
- KBG syndrome (*ANKRD11*) — includes paratesticular rhabdoid tumor as a recognized association.
- BAP1 tumor predisposition syndrome — associated with rhabdoid-subtype high-grade meningioma.
- DICER1 tumor predisposition — risk of embryonal rhabdomyosarcoma, a histologic mimic.

**Screening/carrier testing:** Once a familial variant is identified, prenatal testing and preimplantation genetic testing are stated as technically possible (GeneReviews), though this is presented alongside — not in place of — genetic counseling given incomplete penetrance.

---

## 11. Outcome/Prognosis

**SCCOHT:** Overall survival 51% for FIGO stage I disease, dropping to 24% for stage II–IV (PDQ RTPS2) — among the most aggressive gynecologic malignancies in young women, historically associated with median survival well under two years in advanced-stage disease (general SCCOHT literature synthesis; specific historical median-survival figure not independently re-verified with a fresh PMID in this pass and should be sourced directly before KB entry if a precise number is needed).

**AT/RT:** SMARCA4-mutant AT/RT is associated with "younger age and an inferior prognosis in comparison to SMARCB1 mutated cases" (search synthesis of AT/RT molecular-subgroup literature, Acta Neuropathologica 2020 and related). Germline-mutated rhabdoid tumors broadly (either gene) carry a worse prognosis than somatic-only cases (search synthesis).

**Prognostic factors:** Tumor stage (SCCOHT FIGO stage), age at diagnosis (younger = worse for AT/RT), germline vs. somatic-only status (germline = worse), and DNA methylation subgroup (an independent predictor of AT/RT overall survival per EU-RHAB registry data, Frühwald et al., cited in PMC9100752/related EU-RHAB literature).

**Complications:** Paraneoplastic hypercalcemia is a recognized SCCOHT complication requiring independent management. Long-term morbidity in survivors reflects intensive multimodal therapy (surgical, chemotherapeutic, and in some protocols radiotherapeutic) exposure at a young age.

---

## 12. Treatment

**General approach:** Intensive multimodal therapy combining surgery, chemotherapy, and (in appropriate cases) radiotherapy is standard for RTPS2-associated malignancies (GeneReviews). NCIT: NCI Thesaurus term suggestions — NCIT:C15329 (Surgical Procedure), NCIT:C15632 (Chemotherapy), NCIT:C15313 (Radiation Therapy).

**SCCOHT-specific:** Aggressive cytoreductive surgery (including bilateral salpingo-oophorectomy where appropriate) combined with high-dose alkylator-based chemotherapy regimens, in some protocols with autologous stem cell rescue (general SCCOHT treatment literature synthesis).

**Targeted/precision approaches — EZH2 inhibition (tazemetostat):**
- Mechanistic rationale: BAF-complex loss creates an oncogenic dependency on the antagonist PRC2/EZH2 complex; tazemetostat is a selective, oral EZH2 inhibitor with preclinical activity in both INI1(SMARCB1)-negative and SMARCA4-negative models (Mol Cancer Ther 2017, doi:10.1158/1535-7163.mct-16-0678; Mol Cancer Ther 2018 HDAC-EZH2 synergy paper).
- Adult phase 2 trial (NCT02601950): tazemetostat 800 mg BID in adults with INI1-negative malignant rhabdoid tumors, confirmed by histology and IHC.
- Pediatric MATCH trial (NCT03213665 / APEC1621C): tazemetostat in pediatric patients with tumors harboring EZH2 alterations or loss of SMARCB1/SMARCA4; 20 patients enrolled (median age 5 y), predominantly AT/RT (n=8) and malignant rhabdoid tumor (n=4); 6-month PFS 35%, 6-month OS 45% (Mayo Clinic/JNCI publication, APEC1621C results).
- Combination trial (NCT05407441 / Dana-Farber "TAZNI"): Phase I/II tazemetostat + nivolumab + ipilimumab for children with SMARCB1- or SMARCA4-deficient tumors (malignant rhabdoid tumor, AT/RT, epithelioid sarcoma, chordoma).

**CDK4/6 inhibition:** SMARCA4-determined cyclin D1 deficiency creates a druggable dependency on CDK4/6 in SCCOHT, providing a distinct targeted-therapy rationale from EZH2 inhibition (Xue et al. 2019, *Nat Commun*, [10.1038/s41467-018-06958-9](https://www.nature.com/articles/s41467-018-06958-9)); NCIT drug-class suggestion for this modality is not standardized in this search and would need per-agent NCIT lookup (e.g., palbociclib/ribociclib class terms).

**HDAC inhibitor combination:** HDAC inhibitors synergize with EZH2 catalytic inhibitors to enhance antitumor activity in SCCOHT preclinical models (Mol Cancer Ther 2018, [aacrjournals.org/mct/article/17/12/2767](https://aacrjournals.org/mct/article/17/12/2767/273071/Histone-Deacetylase-Inhibitors-Synergize-with)).

**Fertility considerations:** Egg/ovarian tissue banking may be considered before risk-reducing surgery, though the possible germ-cell origin of SCCOHT introduces uncertainty into the safety of this approach in mutation carriers (PDQ RTPS2 discussion).

**Immunotherapy:** Checkpoint-inhibitor combinations (nivolumab/ipilimumab) are being trialed in combination with EZH2 inhibition rather than as monotherapy in this tumor class (NCT05407441).

---

## 13. Prevention

**Risk-reducing surgery:** Prophylactic risk-reducing bilateral salpingo-oophorectomy "may be discussed following the end of family planning" in women with confirmed SMARCA4-related RTPS2, given the high lifetime risk of SCCOHT — GeneReviews explicitly frames this as requiring an interdisciplinary approach with genetic counseling given medical and ethical complexity (not a blanket recommendation).

**Surveillance protocol (GeneReviews, RTPS2-specific, age-stratified):**
- Birth–6 months: monthly clinical exam; abdominal and neck ultrasound; head ultrasound or brain/spine MRI.
- 7–18 months: every 2–3 months, clinical/neurologic exam plus abdominal/neck ultrasound.
- 19 months–5 years: every 3 months, clinical exam, ultrasound, and brain/spine MRI.
- After age 5 years: clinical exam every 6 months; annual whole-body MRI.
- Females specifically: abdominal and pelvic ultrasound every 6 months, continuing lifelong, for SCCOHT surveillance.

(The PDQ summary independently corroborates a broadly similar schedule: craniospinal imaging every 4–6 weeks initially then quarterly for children under 5, quarterly clinical exam/abdominal ultrasound to age 5, and lifelong 6-monthly pelvic/abdominal ultrasound in females.)

**Genetic counseling:** Recommended for any individual/family with a personal or family history of SCCOHT or rhabdoid tumor; cascade testing of at-risk relatives is recommended once a familial variant is identified (PDQ RTPS2). Because penetrance is incomplete and many carriers are asymptomatic parents, counseling framing differs materially from RTPS1 — carrier identification does not imply near-certain future disease, but does trigger the surveillance protocol above.

**Prenatal/preimplantation options:** Technically available once the familial variant is known (GeneReviews), to be discussed within formal genetic counseling given incomplete penetrance.

---

## 14. Other Species / Natural Disease

No naturally occurring companion-animal or wildlife rhabdoid tumor syndrome specifically attributed to *SMARCA4* germline loss was identified in this search (contrast with some other pediatric cancer-predisposition genes that have recognized veterinary correlates). The *SMARCA4* gene itself is broadly conserved across mammals (orthologous to mouse *Smarca4*/*Brg1*; NCBI Gene), which underpins its use in mouse modeling (§15) rather than natural veterinary disease.

---

## 15. Model Organisms

**Mouse — germline null:** *Smarca4/Brg1*-null mice die during the peri-implantation stage; blastocyst outgrowth studies show neither the inner cell mass nor trophectoderm survives, and Brg1 is required for Cdx2-mediated repression of Oct4 in blastocysts, with knockout leading to ectopic pluripotency-factor expression and failure of both trophectoderm and ICM outgrowth (Bultman et al., "A Brg1 null mutation in the mouse reveals functional differences among mammalian SWI/SNF complexes," PMID:[11163203](https://pubmed.ncbi.nlm.nih.gov/11163203/); [PMC2868905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2868905/)). This establishes *Smarca4* as essential for pre-implantation development, consistent with it being a haploinsufficient dosage-sensitive gene in humans (§4).

**Mouse — heterozygous/conditional models:** BRG1 (heterozygous or lineage-conditional loss) protects against ovarian cysts, uterine tumors, and mammary tumors "in a lineage-specific manner," directly modeling the reproductive-tract tumor spectrum relevant to SCCOHT/uterine sarcoma ([PMC3283619](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3283619/)). Tissue-specific conditional Smarca4-knockout approaches (e.g., P0-Cre::Smarca4^fl/fl targeting neural crest lineages, paralleling the Smarcb1/Nf2 conditional strategy used to dissect schwannoma vs. rhabdoid tumor origin, [PMC5563506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5563506/)) are used to probe cell-of-origin and tumor-type specificity, and show phenotypic changes (body weight, clinical symptoms) in the affected lineage.

**Newer transgenic models:** A newly generated transgenic SMARCA4-deficient mouse model produces prominent neuromuscular weakness and limb paralysis rather than a clean rhabdoid-tumor phenocopy (PMID:[36582072](https://pubmed.ncbi.nlm.nih.gov/36582072/)) — an important **model-fidelity caveat**: this line highlights that global or broadly-targeted Smarca4 loss in mice produces severe non-oncogenic phenotypes (neuromuscular) that can complicate its use as a clean tumor model, distinct from the human RTPS2 presentation; tissue-restricted conditional approaches remain necessary to isolate tumor phenotypes from confounding developmental/neuromuscular toxicity.

**In vitro models:** The SCCOHT cell line BIN-67 (dual SMARCA2/SMARCA4-null) is the principal cell-based model used to establish the EZH2 synthetic-lethality and CDK4/6-dependency findings described in §6 and §12 (Mol Cancer Ther 2017; Nat Commun 2019).

**Model limitations:** No model discussed in this search fully recapitulates the incomplete-penetrance, later-onset (adolescent/adult), SCCOHT-predominant human RTPS2 phenotype — mouse germline nulls are embryonic lethal, and conditional/heterozygous models to date better capture reproductive-tract tumor susceptibility (ovarian/uterine/mammary) or neuromuscular toxicity than they do a clean, penetrance-matched SCCOHT or AT/RT phenocopy.

---

## Summary of Key Citations

| Claim | Citation |
|---|---|
| RTPS2 discovery, R1189X, reduced penetrance | Schneppenheim et al. 2010, *Am J Hum Genet* 86:279–284, PMID:[20137775](https://pubmed.ncbi.nlm.nih.gov/20137775/) |
| Germline/somatic SMARCA4 in SCCOHT | Witkowski et al. 2014, *Nat Genet* 46:438–443, PMID:[24658002](https://pubmed.ncbi.nlm.nih.gov/24658002/) |
| Frequent inactivating germline+somatic SMARCA4 in SCCOHT | Ramos et al. 2014, PMID:[24658001](https://pubmed.ncbi.nlm.nih.gov/24658001/) |
| GeneReviews chapter (RTPS1+RTPS2) | [NBK469816](https://www.ncbi.nlm.nih.gov/sites/books/NBK469816/) |
| PDQ RTPS2 summary | [NBK613400](https://www.ncbi.nlm.nih.gov/books/NBK613400/) |
| OMIM #613325 | [omim.org/entry/613325](https://omim.org/entry/613325) |
| AT/RT SMARCA4 molecular subgroup | *Acta Neuropathologica* 2020, [10.1007/s00401-020-02250-7](https://link.springer.com/article/10.1007/s00401-020-02250-7) |
| EZH2 synthetic lethality in SMARCA4-deficient SCCOHT | *Mol Cancer Ther* 2017, [10.1158/1535-7163.mct-16-0678](https://doi.org/10.1158/1535-7163.mct-16-0678) |
| CDK4/6 dependency via cyclin D1 loss | *Nat Commun* 2019, [10.1038/s41467-018-06958-9](https://www.nature.com/articles/s41467-018-06958-9) |
| Pediatric MATCH tazemetostat (APEC1621C) | NCT03213665, JNCI 2023 |
| SMARCA4-deficient thoracic sarcoma/NSCLC as smoking-related, non-germline entity | *J Thorac Oncol* 2019/2020, [PMC10875988](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10875988/) |
| Smarca4/Brg1 germline-null peri-implantation lethality | Bultman et al., PMID:[11163203](https://pubmed.ncbi.nlm.nih.gov/11163203/) |
| Coffin-Siris/SCCOHT overlap kindred | [PMC5601212](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5601212/) |

**Gaps flagged for curator follow-up rather than filled by inference:** exact gnomAD pLI/LOEUF value for *SMARCA4*; a directly-sourced historical median-survival figure for advanced SCCOHT (only stage-stratified OS percentages were retrieved); a specific CL ontology term for SCCOHT/AT/RT cell-of-origin (genuinely unresolved in the primary literature, not merely unsearched); and any zebrafish or Drosophila *Smarca4*-ortholog rhabdoid-tumor model (none surfaced in this search pass).

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 13 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC2868905` (3 mentions) - Brg1 is required for Cdx2-mediated repression of Oct4 expression in mouse blastocysts.
  - shared terms: brg1, gene

Weighed against this report's own most characteristic terms: `tumor`, `rtps2`, `smarca4`, `sccoht`, `germline`, `rhabdoid`, `pdq`, `variant`, `loss`, `rtps1`, `mutation`, `smarca4-deficient`, `associated`, `brg1`, `smarcb1`, `age`, `gene`, `cancer`, `syndrome`, `distinct`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0031065` (obsolete positive regulation of histone deacetylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0031065` (1 mention) - the report calls it "positive regulation of histone deacetylation — for PRC2/EZH2 crosstalk context"; GO calls it **obsolete positive regulation of histone deacetylation**

12 of 14 terms resolved to a current term; the rest could not be looked up either way.