---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-29T00:10:21.799437'
end_time: '2026-09-29T00:15:21.110965'
duration_seconds: 299.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Propofol Infusion Syndrome
  mondo_id: ''
  category: Environmental
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
  web_search_requests: 21
  num_turns: 22
  total_cost_usd: 1.7055694
  session_id: c924ba15-d543-482e-9539-0c12ece615c8
  stop_reason: end_turn
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
citation_count: 31
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 25
  on_topic: 21
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 40
  verified: 35
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 26
  labels_matching: 20
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:1001603
    reported_labels:
    - kidney proximal tubule epithelial cell, relevant to myoglobin-mediated AKI
    ontology_label: lung macrophage
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0055114
    ontology_label: obsolete oxidation-reduction process
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Propofol Infusion Syndrome
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Propofol Infusion Syndrome** covering all of the
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

# Propofol Infusion Syndrome (PRIS): Comprehensive Research Report

## 1. Disease Information

### Overview
Propofol infusion syndrome (PRIS, also called propofol-related infusion syndrome) is a rare but frequently fatal drug-toxicity syndrome that develops in patients receiving prolonged, high-dose infusions of propofol (2,6-diisopropylphenol), the short-acting intravenous sedative-hypnotic agent used ubiquitously in anesthesia and intensive care sedation. It is characterized by the abrupt onset of severe metabolic acidosis, rhabdomyolysis/myoglobinuria, hyperkalemia, hyperlipidemia, hepatomegaly with fatty liver infiltration, acute kidney injury, and cardiovascular collapse — classically progressing to refractory bradyarrhythmia and asystole ([MeSH D000072736](https://meshb.nlm.nih.gov/record/ui?ui=D000072736); [Wikipedia summary](https://en.wikipedia.org/wiki/Propofol_infusion_syndrome)).

The syndrome was first described by Bray in 1998 in a case series of critically ill children (Bray RJ, "Propofol infusion syndrome in children," *Paediatr Anaesth* 1998), in whom 12 of 15 reported children died after prolonged high-dose propofol sedation with the constellation of refractory bradycardia, lipemic plasma, hepatomegaly, metabolic acidosis, rhabdomyolysis, and myoglobinuria. Although first recognized in the pediatric ICU population, PRIS is now well documented in adults, particularly in neurocritical care (traumatic brain injury, refractory/super-refractory status epilepticus) ([Bray 1998, summarized in PMC8660594](https://pmc.ncbi.nlm.nih.gov/articles/PMC8660594/); [BJA Education review](https://www.bjaed.org/article/S1743-1816(17)30024-0/fulltext)).

A widely used operational definition (Bray-derived) is: **acute refractory bradycardia progressing to asystole**, occurring in the presence of at least one of: metabolic acidosis (base deficit >10 mmol/L), rhabdomyolysis/myoglobinuria, lipemic plasma or fatty liver enlargement — typically associated with propofol infusion rates >4 mg/kg/h for >48 hours, though cases have been reported outside these thresholds.

### Key Identifiers
| Resource | Identifier / Status |
|---|---|
| MeSH | `D000072736` — "Propofol Infusion Syndrome" |
| MONDO | **No MONDO term currently exists.** A dismech GitHub issue (#13101, "Curate propofol infusion syndrome, which has no MONDO term") documents this gap explicitly — the condition fits MONDO's usual disease-entity criteria (known etiology, named phenotype constellation, dose/time-course relationship, resolution on drug withdrawal) but has not yet been minted. |
| OMIM | No OMIM entry — PRIS is an acquired, drug-induced toxidrome rather than a Mendelian disease, though it can *unmask* an underlying Mendelian mitochondrial disorder (see Etiology, below). |
| Orphanet | No dedicated Orphanet entry identified in this search. |
| ICD-10/11 | No dedicated code identified; typically coded under adverse-effect/poisoning codes (e.g., T41 anesthetic poisoning) combined with the resulting organ dysfunction codes rather than a single disease code. |
| Synonyms | Propofol-related infusion syndrome; PRIS; "propofol infusion 'syndrome'" (the scare quotes in some literature reflecting debate over whether it is a single unified syndrome or a spectrum of overlapping mitochondrial toxicities) |

Nearly all available data derive from **aggregated case reports/case series and observational cohort studies** rather than large prospective trials, given the rarity and unpredictability of onset; the largest prospective multicenter incidence study enrolled 1,017 adult ICU patients (Roberts RJ et al., *Crit Care* 2009; PMC2784401), and the largest structured literature synthesis pooled 153 published case reports from 1990–2014 (Krajčová A et al., *Crit Care* 2015, PMID: [26558513](https://pubmed.ncbi.nlm.nih.gov/26558513/)).

---

## 2. Etiology

### Disease Causal Factor
PRIS is fundamentally an **environmental/iatrogenic drug-toxicity syndrome** — the sole necessary causal exposure is prolonged, high-dose intravenous propofol infusion. There is no infectious or intrinsically genetic causation, though genetic background strongly modulates susceptibility (see below).

### Risk Factors

**Dose/duration (the dominant modifiable risk factor):**
- Infusion rate >4 mg/kg/h (some sources cite >5 mg/kg/h) sustained for >48 hours is the classically cited threshold. One case-control analysis found the odds ratio for PRIS increased 1.93-fold for every 1 mg/kg/h increment in mean propofol dose above 4 mg/kg/h.
- However, PRIS is not strictly dose- or duration-dependent: cases have been documented after as little as 3–5 hours of high-dose infusion, and at doses as low as 1.4 mg/kg/h ([BJA Education review](https://www.bjaed.org/article/S1743-1816(17)30024-0/fulltext); [Drug Safety/Deranged Physiology summaries](https://derangedphysiology.com/main/required-reading/environmental-injuries-and-toxicology/Chapter-512/propofol-infusion-syndrome)).

**Patient/clinical risk factors:**
- Critical illness/severe systemic inflammatory state (sepsis)
- Severe traumatic brain injury and other acute neurological injury — risk approximately doubles at infusion rates >5 mg/kg/h in this population
- Refractory or super-refractory status epilepticus requiring prolonged high-dose propofol
- Carbohydrate depletion / low carbohydrate-to-lipid caloric ratio (inadequate glucose delivery forces reliance on fatty-acid oxidation, which propofol itself impairs)
- Concomitant high-dose exogenous catecholamines (vasopressors) and/or glucocorticoids — these are hypothesized "priming" factors that potentiate skeletal/cardiac muscle protein catabolism and mitochondrial stress
- Young age (children/adolescents historically over-represented, though risk is now well established in adults)
- Male sex has been associated with higher mortality risk in some cohorts

**Genetic risk factors:**
- **Underlying primary mitochondrial disease or fatty-acid β-oxidation disorders are the clearest genetic susceptibility factor.** Multiple case reports describe propofol "unmasking" previously unrecognized mitochondrial disease:
  - A MELAS (mitochondrial encephalomyopathy, lactic acidosis, and stroke-like episodes) patient carrying the m.3271T>C variant in *MT-TL1* developed severe PRIS-pattern lactic acidosis and rhabdomyolysis (Shimizu et al., *Acute Med Surg* 2020, [10.1002/ams2.473](https://onlinelibrary.wiley.com/doi/10.1002/ams2.473)).
  - A case report described PRIS heralding an undiagnosed mitochondrial disease (*Neurology* 2014, PMID: [24491974](https://pubmed.ncbi.nlm.nih.gov/24491974)).
  - A case discusses a *POLG* mitochondrial DNA polymerase mutation in the context of PRIS management ([e-jnc.org case report](https://www.e-jnc.org/journal/view.php?number=378)).
  - Review literature states explicitly: "Mitochondrial disorders are prone to propofol infusion syndrome" (PMC7774597) and "predisposition to mitochondrial dysfunction caused by genetic mutations promotes cell death and caspase activation induced by propofol" (Finsterer & Frank, *J Child Neurol* 2016).
  - Pre-existing inborn errors of fatty-acid β-oxidation (e.g., carnitine-acylcarnitine translocase deficiency, carnitine palmitoyltransferase deficiencies) are a recognized contraindication/relative contraindication to propofol infusion, since propofol itself inhibits the same pathway these patients already have impaired (narrative review, *Medicine* 2022).

### Protective Factors
No genetic or pharmacological protective factors are established. The principal "protective" strategy is behavioral/procedural: adherence to dose/duration limits, adequate carbohydrate provision, use of alternative or adjunctive sedatives (dexmedetomidine, benzodiazepines, barbiturates) to permit propofol-sparing regimens, and vigilant biochemical monitoring (see Prevention, §13).

### Gene-Environment Interaction
The core gene-environment interaction is between **constitutional mitochondrial/fatty-acid-oxidation reserve capacity** (genetic) and **exogenous mitochondrial toxin exposure plus metabolic stress from critical illness** (environmental): a patient with normal but limited FAO/ETC reserve who is additionally stressed by sepsis, catecholamine excess, and carbohydrate starvation can be tipped into overt PRIS by an inhibitory drug load that would be tolerated in a metabolically unstressed individual — and a patient with a subclinical primary mitochondrial disorder can decompensate catastrophically at doses/durations that are otherwise considered "safe."

---

## 3. Phenotypes

| Phenotype | Type | Frequency in pooled case data | Suggested HPO term |
|---|---|---|---|
| Refractory sinus bradycardia progressing to asystole/cardiac arrest | Clinical sign (cardiac) | Defining/near-universal in classic PRIS | HP:0001688 (Sinus bradycardia); HP:0004943 (Asystole is not a direct HPO term — consider HP:0001677 Coronary artery atherosclerosis is wrong; use HP:0011675 Arrhythmia as broader term) |
| Metabolic (lactic) acidosis | Laboratory abnormality | ~62% in one 21-patient RSE cohort; near-universal across pooled reviews | HP:0001942 (Metabolic acidosis) / HP:0002151 (Hyperlactic acidemia) |
| Rhabdomyolysis / myoglobinuria | Laboratory abnormality / clinical sign | ~42% (RSE cohort); a hallmark finding | HP:0003201 (Rhabdomyolysis) |
| Hyperkalemia | Laboratory abnormality | More frequent in adults than children | HP:0002153 (Hyperkalemia) |
| Hyperlipidemia / lipemic plasma | Laboratory abnormality | ~33% (RSE cohort); more common in children | HP:0003077 (Hyperlipidemia) / HP:0003146 (Hypertriglyceridemia) |
| Hepatomegaly / fatty liver | Physical/imaging sign | More frequent in children than adults; independently associated with pediatric mortality | HP:0002240 (Hepatomegaly) |
| Acute kidney injury | Laboratory/clinical sign | ~38% (RSE cohort) | HP:0001919 (Acute kidney injury) |
| Brugada-pattern ECG changes (down-sloping ST elevation V1–V3) | Clinical sign (electrophysiological) | Reported subset; strongly predicts imminent sudden death | No precise HPO term for acquired Brugada pattern; consider HP:0011675 (Arrhythmia) with notes |
| Elevated hepatic transaminases | Laboratory abnormality | ~28% (RSE cohort) | HP:0002910 (Elevated hepatic transaminase) |
| Cardiomyopathy / myocardial dysfunction | Clinical/imaging sign | Documented on echocardiography and at autopsy (sustained mitochondrial damage in cardiomyocytes, PMC8905003) | HP:0001638 (Cardiomyopathy) |
| Fever | Clinical sign | More frequent in children; independently associated with pediatric mortality | HP:0001945 (Fever) |
| Elevated creatine kinase | Laboratory abnormality | CK >10,000 U/L typical at diagnosis; CK <5,000 U/L marks a low-risk population | (No dedicated HPO term; typically captured as a biomarker/lab value rather than HPO) |

**Age of onset:** Not congenital — this is an acquired, drug-exposure-triggered syndrome. Onset is typically 1–6 days after initiation of high-dose propofol (median ~3 days in the Roberts et al. 2009 prospective cohort), though onset as early as 3–5 hours has been reported in some cases.

**Severity and progression:** Highly variable — from subclinical biochemical derangement (rising CK/triglycerides/lactate, "pre-PRIS") to fulminant multi-organ failure and sudden cardiac death within hours once the Brugada-pattern ECG change appears. Course is typically rapidly progressive once overt, but is potentially reversible with immediate propofol discontinuation and aggressive supportive care if caught early.

**Clinical presentation differs by age group** (Hemphill S et al., structured literature review, *Br J Anaesth* 2019 [S0007091219300108](https://www.bjanaesthesia.org.uk/article/S0007-0912(19)30010-8/fulltext)):
- **Children:** lipemia, fever, and hepatomegaly occur more frequently; fever and hepatomegaly are independently associated with mortality.
- **Adults:** rhabdomyolysis and hyperkalemia are more frequent; ECG changes, hypotension, hyperkalemia, traumatic brain injury, and mean infusion rate >5 mg/kg/h are independently associated with mortality.

**Quality of life impact:** No formal QoL instrument data exist for PRIS specifically, given its acute, often fatal, ICU-confined course; survivors' quality-of-life burden derives from sequelae of the organ injuries sustained (post-AKI renal impairment, post-rhabdomyolysis compartment syndrome/contracture, hypoxic-ischemic sequelae of cardiac arrest, or unmasked chronic mitochondrial disease).

---

## 4. Genetic/Molecular Information

PRIS itself has **no single causal gene** — it is not a Mendelian disorder. However, the molecular basis of susceptibility and of the toxic mechanism strongly implicates specific gene products:

- ***CPT1A/CPT2* (carnitine palmitoyltransferase 1 and 2, HGNC:2328 / HGNC:2330):** Propofol directly inhibits carnitine palmitoyltransferase I, the outer mitochondrial membrane enzyme that transfers long-chain fatty acyl groups onto carnitine for mitochondrial import — the rate-limiting step of fatty-acid β-oxidation (Wolf A et al., *Lancet* 2001, "Impaired fatty acid oxidation in propofol infusion syndrome," PMID: [11558490](https://pubmed.ncbi.nlm.nih.gov/11558490/)). Patients with primary CPT1/CPT2 deficiency or carnitine-acylcarnitine translocase (*SLC25A20*) deficiency are at markedly elevated iatrogenic risk if given propofol.
- **Mitochondrial DNA / nuclear mitochondrial genes (*MT-TL1*, *POLG*, and the broader primary mitochondrial disease gene set):** case reports document PRIS unmasking MELAS (m.3271T>C in *MT-TL1*) and *POLG*-related mitochondrial disease, establishing these as susceptibility loci in the sense that carriers are markedly more vulnerable to overt PRIS at "standard" propofol doses.
- **Electron transport chain complex I and III subunit genes:** propofol targets Complexes I and III directly, inducing a metabolic switch from oxidative phosphorylation to glycolysis and triggering cell death in an ETC-dependent manner (bioRxiv/PLOS ONE mechanistic study, [10.1371/journal.pone.0192796](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0192796)).
- ***SCN5A* (cardiac sodium channel, HGNC:10593):** mechanistically relevant to the Brugada-pattern ECG phenotype — propofol has demonstrated cardiac sodium-channel-blocking properties, and the acquired Brugada pattern in PRIS is attributed to pharmacological blockade of the same sodium current that is genetically reduced in congenital Brugada syndrome (PMC9200599; PMC1474111).

**Variant classification / population frequency:** Not applicable in the standard ACMG/ClinVar sense, since PRIS is not itself a variant-caused disease; the relevant variants (in *MT-TL1*, *POLG*, *CPT1A/CPT2*, *SLC25A20*) are catalogued under their respective primary mitochondrial/FAO disorder entries in ClinVar/OMIM rather than under PRIS.

**Functional consequence summary:** The convergent molecular lesion is **loss of mitochondrial fatty-acid oxidative capacity plus impaired electron transport chain flux**, producing an energetic mismatch — cells (especially cardiac and skeletal myocytes, which are highly oxidative-metabolism-dependent) cannot meet ATP demand through either fat or, ultimately, carbohydrate oxidation, precipitating necrosis.

**Epigenetic information:** No epigenetic mechanism has been established for PRIS; this is an acute pharmacotoxic/bioenergetic process rather than a chromatin-level disease.

**Chromosomal abnormalities:** Not applicable.

---

## 5. Environmental Information

Propofol itself is the environmental/exposure agent — this is the paradigm case of an **iatrogenic drug-toxicity environmental disease**:

- **Chemical entity:** Propofol, 2,6-diisopropylphenol (**CHEBI:44915**), an intravenous general anesthetic/sedative-hypnotic formulated in a lipid emulsion (soybean oil, egg lecithin, glycerol).
- **Exposure route:** Continuous intravenous infusion (as opposed to bolus induction dosing, which does not carry meaningful PRIS risk).
- **Co-exposures that potentiate toxicity:** concurrent exogenous catecholamine infusion (vasopressors), concurrent glucocorticoid administration, and the lipid emulsion vehicle itself contributing to the exogenous fat load layered onto endogenous stress-driven lipolysis.
- **Lifestyle/nutritional factor:** inadequate carbohydrate (glucose) provision during critical illness is a specifically implicated modifiable environmental contributor, since carbohydrate starvation forces greater reliance on the very fatty-acid oxidation pathway propofol inhibits.
- **Infectious agents:** Not a direct cause, but sepsis (as a systemic inflammatory/catecholamine-driving state) is a well-documented risk-amplifying comorbid condition; propofol has also been shown experimentally to increase morbidity/mortality in a rat model of sepsis (*Crit Care* 2015, [10.1186/s13054-015-0751-x](https://link.springer.com/article/10.1186/s13054-015-0751-x)), suggesting a bidirectional interaction between septic physiology and propofol toxicity rather than sepsis being a purely passive risk marker.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, from exposure to clinical manifestation)

1. **Prolonged, high-dose intravenous propofol infusion** delivers sustained tissue concentrations of 2,6-diisopropylphenol to skeletal and cardiac myocytes and hepatocytes, sufficient to reach mitochondrial toxic thresholds — *leads to* (2).
2. **Propofol directly inhibits carnitine palmitoyltransferase I** at the outer mitochondrial membrane, blocking the transfer of long-chain fatty acyl groups onto carnitine — *results in* impaired entry of long-chain fatty acids into the mitochondrial matrix for β-oxidation (demonstrated in human skeletal muscle homogenates at propofol concentrations below those needed to impair the electron transport chain directly, indicating this is an independent, upstream lesion) — *leads to* (3).
3. In parallel, **propofol directly inhibits electron flux through Complexes I and III of the mitochondrial electron transport chain**, with coenzyme Q identified experimentally as a principal site of interaction — *leads to* (4a) and (4b) as parallel branches.
   - **(4a) Impaired oxidative phosphorylation:** reduced maximal ETC capacity and reduced ATP synthesis capacity, demonstrated directly in cultured human skeletal muscle cells at plasma concentrations achieved in sedated ICU patients (Vanlander/Ferrari-line studies; PMID: [29240609](https://pubmed.ncbi.nlm.nih.gov/29240609/); PMID: [31584947](https://pubmed.ncbi.nlm.nih.gov/31584947/)) — *forces* a compensatory metabolic switch toward glycolysis, which is inadequate to meet the energy demands of highly oxidative tissues (cardiac and skeletal muscle) — *leads to* (5).
   - **(4b) Reactive oxygen species generation and mitochondrial membrane depolarization:** at higher concentrations, propofol causes sustained mitochondrial membrane potential depolarization and mild oxidative-phosphorylation uncoupling, with increased ROS production and activation of the mitochondrial (intrinsic) apoptotic pathway (caspase activation) — *leads to* (5) in parallel.
4. **Fatty-acid oxidation blockade (from step 2), superimposed on a critical-illness state of carbohydrate depletion and stress-driven lipolysis (high catecholamines/glucocorticoids providing an exogenous fat/lipid load that cannot be productively oxidized)** — *results in* accumulation of toxic lipid intermediates (elevated malonylcarnitine and C5-acylcarnitine species have been documented biochemically) and progressive **energy failure**: an imbalance between cellular energy demand and the cell's capacity to generate ATP via either fat or carbohydrate substrate.
5. **Energy failure in highly oxidative-metabolism-dependent tissues (cardiac myocytes, skeletal myocytes, hepatocytes) causes cellular necrosis and, via the apoptotic pathway from step 4b, programmed cell death** — this is the convergence point of the two upstream branches — *leads to*, by tissue:
   - **Skeletal muscle:** myocyte necrosis → **rhabdomyolysis**, myoglobinuria, and consequent **acute kidney injury** (myoglobin-mediated tubular injury) and **hyperkalemia** (potassium release from necrotic myocytes).
   - **Cardiac muscle:** myocyte necrosis and mitochondrial damage (documented histologically as "sustained mitochondrial damage in cardiomyocytes" in fatal human PRIS cases, PMC8905003) → impaired contractility (**cardiomyopathy**) and, via propofol's independent cardiac sodium-channel-blocking action, **acquired Brugada-pattern ECG changes** (down-sloping ST-segment elevation in V1–V3) → electrical instability → **ventricular arrhythmia/fibrillation and refractory bradyarrhythmia progressing to asystole**, the terminal and most lethal manifestation.
   - **Hepatocytes:** impaired fat handling and mitochondrial injury → **hepatomegaly with fatty infiltration (steatosis)** and elevated transaminases.
   - **Systemic:** the combination of unoxidized circulating lipid and the propofol lipid-emulsion vehicle itself → **hyperlipidemia/lipemic plasma**; accumulating unmetabolized organic acids and lactate from the failed oxidative pathway → **severe metabolic (lactic) acidosis**.
6. Where the patient carries an **underlying primary mitochondrial disease or fatty-acid oxidation defect** (genetic branch point, from Etiology §2), baseline ETC/FAO reserve is already reduced, so the same propofol exposure produces steps 2–5 at markedly lower doses/durations, or "unmasks" a previously subclinical disease — this is an alternative entry point into the same downstream cascade rather than a separate mechanism.

### Molecular pathways
Fatty-acid β-oxidation pathway (carnitine shuttle: CPT1 → CACT → CPT2); mitochondrial electron transport chain (Complexes I, II/CoQ, III, IV, ATP synthase); intrinsic (mitochondrial) apoptosis pathway (cytochrome c release, caspase-9/-3 activation).

### Cellular processes
Apoptosis (mitochondrial/intrinsic pathway), necrosis, a Warburg-like metabolic switch from oxidative phosphorylation to glycolysis, oxidative stress (ROS accumulation).

### Protein dysfunction
CPT1 catalytic inhibition (competitive/direct enzymatic inhibition by propofol, not a structural mutation); Complex I and III functional inhibition at the level of electron transfer, with coenzyme Q implicated as an interaction site.

### Biochemical abnormalities
Elevated malonylcarnitine and C5-acylcarnitine (biomarkers of impaired FAO); lactic acidosis; hyperkalemia; hypertriglyceridemia; elevated CK, myoglobin, troponin T.

### Molecular/experimental model evidence
- Human skeletal muscle cell culture studies show dose-dependent inhibition of exogenous fatty-acid oxidation and reduced maximal ETC capacity at clinically achieved propofol concentrations, and that noradrenaline exposure worsens propofol-induced mitochondrial dysfunction in the same cell system (PMC9643307) — direct mechanistic support for the catecholamine risk-factor observation in §2.
- A murine skeletal-muscle-injury model and an isolated-perfused newborn mouse heart model (relevant to pediatric PRIS) both recapitulate propofol-dose-dependent bioenergetic failure and cardiotoxicity (PMC6712282; PMC9350423; *Pediatr Res* 2022, [10.1038/s41390-022-01985-1](https://www.nature.com/articles/s41390-022-01985-1)).
- A rabbit PRIS model demonstrated a survival/organ-injury benefit from coenzyme Q10 supplementation (PMC10584382), consistent with CoQ being a direct molecular interaction site in the ETC inhibition mechanism.

### Suggested GO / CL / UBERON terms
- GO:0006635 (fatty acid beta-oxidation), GO:0022904 (respiratory electron transport chain), GO:0006119 (oxidative phosphorylation), GO:0006915 (apoptotic process), GO:0055114 (oxidation-reduction process)
- CL:0000746 (cardiac muscle cell), CL:0000188 (skeletal muscle fiber), CL:0000182 (hepatocyte), CL:1001603 (kidney proximal tubule epithelial cell, relevant to myoglobin-mediated AKI)
- UBERON:0001133 (cardiac muscle tissue), UBERON:0001134 (skeletal muscle tissue), UBERON:0002107 (liver), UBERON:0002113 (kidney)

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Heart (conduction system and myocardium), skeletal muscle (generalized), liver.
**Organ level (secondary/complications):** Kidneys (myoglobin-mediated acute tubular injury), and — where cardiac arrest occurs — brain (hypoxic-ischemic injury) as a downstream complication rather than a primary target.
**Body systems involved:** Cardiovascular, musculoskeletal (muscle), hepatic, renal, and metabolic/endocrine (lipid and acid-base homeostasis).

**Tissue/cell level:**
- Cardiac muscle tissue → cardiomyocytes (CL:0000746) and the cardiac conduction system (relevant to the Brugada-pattern sodium-channel mechanism).
- Skeletal muscle tissue → skeletal myofibers (CL:0000188).
- Liver parenchyma → hepatocytes (CL:0000182), with steatotic change.
- Renal tubular epithelium → proximal tubule cells, injured secondarily by filtered myoglobin.

**Subcellular level:** Mitochondria are the central subcellular compartment implicated — specifically the inner mitochondrial membrane (electron transport chain complexes I and III, and the carnitine shuttle machinery at the outer/inner membrane interface). Relevant GO Cellular Component terms: GO:0005743 (mitochondrial inner membrane), GO:0005739 (mitochondrion).

**Localization:** Systemic/multi-organ rather than lateralized or site-specific; the cardiac lesion is specifically localized to the conduction system and right ventricular outflow tract region electrophysiologically (the anatomic substrate of the Brugada ECG pattern), though no gross structural cardiac abnormality is required (a purely functional/electrophysiological phenotype in most cases).

---

## 8. Temporal Development

**Onset:** Acquired, not congenital; onset is tied entirely to duration/dose of propofol exposure rather than to a developmental stage. Reported latency from infusion initiation to overt syndrome ranges from as little as 3–5 hours (rare, high-dose cases) to a median of ~3 days (range 1–6 days) in the largest prospective adult cohort (Roberts et al. 2009), with classical teaching citing >48 hours of infusion as the higher-risk window.

**Onset pattern:** Acute to subacute — biochemical derangement (rising CK, triglycerides, lactate — sometimes termed "pre-PRIS") may precede the overt clinical syndrome by hours to a day or more, offering a window for early detection, but once the cardiac phenotype (Brugada-pattern ECG, refractory bradyarrhythmia) manifests, progression to death can occur within hours.

**Disease stages:** Informally staged as (a) subclinical/biochemical (isolated rise in CK/triglycerides/lactate), (b) overt PRIS (multi-organ derangement without terminal arrhythmia), and (c) fulminant/terminal PRIS (Brugada-pattern ECG, refractory arrhythmia, cardiac arrest) — this is a practical clinical staging derived from the biomarker/ECG literature rather than a formally codified staging system.

**Progression rate:** Highly variable, but the terminal cardiac phase is characteristically rapid — once ST-segment changes appear, patients have been reported to progress to fatal ventricular fibrillation/electrical storm within hours.

**Disease course pattern:** Not relapsing-remitting; it is a self-limited toxic exposure syndrome in the sense that removing the causal agent (stopping propofol) halts further toxin delivery, but established organ injury (rhabdomyolysis, AKI, cardiac injury) follows its own resolution timeline, and cardiac arrest, once it occurs, is frequently fatal despite maximal support.

**Remission:** Resolution of the Brugada-pattern ECG and biochemical derangement has been documented following propofol discontinuation and supportive care in surviving patients (e.g., "Recovery following propofol-associated Brugada electrocardiogram," PMID: [19821933](https://pubmed.ncbi.nlm.nih.gov/19821933/)) — remission is treatment(withdrawal)-induced rather than spontaneous while exposure continues.

**Critical period for intervention:** The subclinical biochemical phase (rising CK, triglycerides, and lactate in a patient on high-dose/prolonged propofol) represents the key window in which discontinuing propofol can prevent progression to the fulminant, often-fatal cardiac phase — this is the rationale behind biomarker-based surveillance protocols (§10, §13).

---

## 9. Inheritance and Population

**Inheritance pattern:** Not applicable — PRIS is an acquired toxic syndrome, not a heritable disease. (The *predisposing* primary mitochondrial/FAO disorders that can lower the toxicity threshold follow their own inheritance patterns — autosomal recessive for most FAO disorders such as CPT1/CPT2/CACT deficiency, and maternal/mitochondrial inheritance for mtDNA point mutations such as the MELAS-associated *MT-TL1* variant.)

**Epidemiology:**
- Incidence in a prospective multicenter cohort of 1,017 critically ill adults: **1.1%**, with onset at a median of 3 days after propofol initiation (Roberts RJ et al. 2009, PMC2784401).
- Other cohorts report incidence figures ranging from **2.9% to 4.1%** depending on population and case ascertainment strictness.
- Among 1,139 patients with *suspected* PRIS pooled across the literature, 342 (30%) had a fatal outcome; among the 153 published case reports specifically analyzed by Krajčová et al. (2015), **78/153 (51%) were fatal**.
- Reported case-fatality rates vary widely by cohort (33%, 36.8%, and up to 48% in some series), reflecting differences in case definition, ascertainment bias toward more severe reported cases, and era of treatment (earlier reports predate widespread biomarker surveillance and ECMO/CRRT rescue availability).

**Population demographics:**
- No strong evidence for ethnic or geographic predilection specific to PRIS itself — risk tracks with propofol utilization patterns (ICU sedation practice) rather than population genetics, except insofar as populations with higher carrier frequency of primary mitochondrial/FAO disorders would be expected to have elevated background susceptibility.
- **Age distribution:** originally described in children (the Bray 1998 index series), now well documented across the age spectrum in adults, with particular concentration in neurocritical care populations (TBI, refractory status epilepticus).
- **Sex ratio:** male sex has been associated with increased mortality risk in pooled case analyses, though this may partly reflect underlying case-mix (trauma and status epilepticus populations skew male in some cohorts) rather than an intrinsic biological sex effect.
- **Mortality is independently associated with age ≤18 years** in pooled analyses (Fong JJ et al., "Predictors of mortality in patients with suspected propofol infusion syndrome," PMID: [18664783](https://pubmed.ncbi.nlm.nih.gov/18664783/)), alongside male sex, vasopressor use, cardiac symptoms, metabolic acidosis, renal failure, hypotension, rhabdomyolysis, and dyslipidemia.

---

## 10. Diagnostics

There is no single confirmatory test; diagnosis is **clinical and biochemical**, based on the temporal association with propofol exposure plus the characteristic constellation of findings, after excluding alternative explanations.

**Laboratory tests / biomarkers:**
- **Creatine kinase (CK):** central surveillance marker. CK >10,000 U/L is typical at diagnosis of overt PRIS; a cutoff <5,000 U/L identifies a low-risk population. Rising CK over 24–48 hours of infusion, in the absence of other muscle pathology, should raise suspicion.
- **Serum lactate:** unexplained/rising metabolic (lactic) acidosis is a core diagnostic feature and an early warning sign.
- **Triglycerides:** rising triglyceride levels have been proposed as a reliable early biomarker of impending PRIS, reflecting both impaired lipid clearance/oxidation and the propofol lipid-emulsion vehicle load.
- **Troponin T** and **myoglobin**: elevated in cases with cardiac and skeletal muscle involvement respectively.
- **Malonylcarnitine and C5-acylcarnitine species**: research-level biomarkers of impaired fatty-acid oxidation, elevated in PRIS (Wolf et al. 2001).
- Arterial blood gas for base deficit/pH.

**Electrophysiology:** Continuous or serial 12-lead ECG monitoring for the **Brugada-pattern ECG** (down-sloping ST-segment elevation in leads V1–V3) is a critical diagnostic and prognostic tool — its appearance is a harbinger of imminent, often fatal, ventricular arrhythmia and should prompt emergency propofol discontinuation (Vernooy K et al., PMC1474111).

**Imaging:** Echocardiography to assess for new cardiomyopathy/reduced ejection fraction; abdominal imaging or clinical exam for hepatomegaly.

**Genetic testing:** Not part of routine acute diagnosis, but should be considered *after* an episode of unexpectedly severe or low-dose-triggered PRIS, to evaluate for an underlying primary mitochondrial disease or fatty-acid oxidation disorder (targeted mitochondrial gene panel or exome sequencing, plasma acylcarnitine profile, and urine organic acids), particularly in pediatric survivors or in cases with a personal/family history suggestive of mitochondrial disease.

**Differential diagnosis:** Malignant hyperthermia (also produces hyperthermia, rhabdomyolysis, acidosis, but is triggered by volatile anesthetics/succinylcholine and driven by *RYR1*-mediated calcium dysregulation rather than mitochondrial FAO/ETC inhibition), serotonin syndrome, neuroleptic malignant syndrome, sepsis/septic cardiomyopathy (which can coexist with and confound PRIS diagnosis), and primary cardiac arrhythmic syndromes (congenital Brugada syndrome, which can also be pharmacologically unmasked by other agents).

**Screening:** No population screening applies (acquired condition); the analogous "screening" practice is routine, protocolized biochemical surveillance (CK, triglycerides, lactate, arterial blood gas) in any patient receiving propofol >48 hours or at doses >4 mg/kg/h, per multiple society/expert guidance summarized in the anesthesia/critical care literature.

---

## 11. Outcome/Prognosis

**Mortality:** Case-fatality rates in the published literature range from ~30% to ~51% depending on cohort (see §9); in a focused refractory-status-epilepticus PRIS cohort, mortality was 66% (13/21 patients). Historically (Bray 1998 index series) mortality was 12/15 (80%), reflecting both the severity of index cases and the absence at that time of modern rescue therapies (CRRT, ECMO).

**Prognostic factors for mortality:**
- **Adults:** ECG changes (especially Brugada pattern), hypotension, hyperkalemia, traumatic brain injury, and mean propofol infusion rate >5 mg/kg/h.
- **Children:** fever and hepatomegaly.
- **Across ages:** age ≤18 years, male sex, vasopressor requirement, cardiac symptoms, metabolic acidosis, renal failure, hypotension, rhabdomyolysis, and dyslipidemia (Fong et al., PMID: [18664783](https://pubmed.ncbi.nlm.nih.gov/18664783/)).

**Complications:** Cardiac arrest/sudden death (via ventricular fibrillation/refractory bradyarrhythmia); acute kidney injury requiring renal replacement therapy; hepatic dysfunction; compartment syndrome from rhabdomyolysis; and, in survivors of cardiac arrest, hypoxic-ischemic brain injury as a secondary complication.

**Recovery potential:** With early recognition (biochemical surveillance catching the "pre-PRIS" phase) and immediate propofol discontinuation plus aggressive supportive/rescue therapy, biochemical and ECG abnormalities can fully resolve and patients can recover without lasting organ dysfunction. Case reports document dramatic recovery of cardiac function (e.g., LVEF improving from severely reduced to 35–40% and normal RV function) after ECMO support, with successful weaning. Conversely, once refractory ventricular arrhythmia/electrical storm develops, mortality is very high despite maximal intervention.

**Prognostic biomarkers:** Persistently or acutely rising CK, triglycerides, and lactate, and especially the appearance of the Brugada-pattern ECG, are the strongest available predictors of imminent deterioration and should trigger escalation of care.

---

## 12. Treatment

There is no drug-specific antidote; management is **immediate cessation of the causal exposure plus problem-driven, organ-supportive critical care.**

### Core management
- **Immediate discontinuation of the propofol infusion** — the single most important intervention, and the only intervention that halts further mechanistic progression (removes the causal toxin).
- **Substitution with alternative sedation** (benzodiazepines, dexmedetomidine, barbiturates, or volatile-agent sedation in refractory status epilepticus) to maintain the clinical goal the propofol had been serving (sedation, seizure control) without continued mitochondrial toxin exposure.

### Organ/problem-directed supportive care
- **Hemodynamic/rhythm support:** vasopressor/inotropic support for cardiovascular collapse (used cautiously, given catecholamines are themselves a risk-amplifying factor); temporary cardiac pacing for refractory bradyarrhythmia.
- **Renal replacement therapy:** continuous renal replacement therapy (CRRT) or intermittent hemodialysis for rhabdomyolysis-associated acute kidney injury and for refractory hyperkalemia — case reports document instances where CRRT failed to control potassium and transition to intermittent hemodialysis achieved rapid correction.
- **Extracorporeal life support (ECMO):** veno-arterial ECMO has been used successfully as rescue therapy in refractory cardiogenic shock/cardiac arrest due to PRIS, in both adults and children, including combined with CRRT and therapeutic plasma exchange in a pediatric refractory-status-epilepticus case (PMC10613782); documented dramatic myocardial recovery over ~5 days of support in at least one case report (PMC3850887).
- **Correction of metabolic derangements:** aggressive correction of acidosis and hyperkalemia; carbohydrate/glucose supplementation to reduce reliance on the impaired fatty-acid oxidation pathway.
- **Investigational/adjunctive:** coenzyme Q10 supplementation improved survival and reduced organ injury in an experimental rabbit PRIS model (PMC10584382), consistent with CoQ's role as a direct molecular target in the ETC inhibition mechanism, but this remains experimental rather than a standard clinical therapy.

### Pharmacogenomics
No established PharmGKB/CPIC gene-drug pairing exists for propofol dosing with respect to PRIS risk specifically, though patients with known primary FAO or mitochondrial disorders are managed with propofol avoidance or extreme caution as a matter of clinical practice rather than formal pharmacogenomic guideline.

### NCIT treatment term suggestions
- `NCIT:C49236` Therapeutic Procedure (general)
- Hemodialysis/renal replacement therapy — relevant NCIT dialysis/CRRT terms
- `NCIT:C15747` Supportive Care
- ECMO — relevant NCIT extracorporeal circulation term

### Experimental treatments
No registered clinical trials were identified specifically targeting PRIS treatment (as opposed to prevention-focused propofol dosing trials); management remains guideline/expert-consensus and case-report-derived rather than trial-validated.

---

## 13. Prevention

**Primary prevention (avoiding the causal exposure/dose):**
- Limit propofol infusion to **<4 mg/kg/h** where clinically feasible, and avoid sustained infusions **beyond 48 hours** at high doses; use the lowest effective dose and shortest necessary duration.
- Favor **propofol-sparing, multimodal sedation strategies** — combining lower-dose propofol with adjuncts such as dexmedetomidine, benzodiazepines, or opioids to reduce cumulative propofol exposure, particularly in high-risk populations (TBI, refractory status epilepticus, pediatric patients).
- Ensure **adequate carbohydrate (glucose) provision** during critical illness/prolonged sedation to reduce forced reliance on the fatty-acid oxidation pathway that propofol impairs.
- Use caution with **concomitant catecholamine and glucocorticoid administration** in patients on high-dose propofol, recognizing the mechanistic synergy demonstrated experimentally (noradrenaline potentiates propofol-induced mitochondrial dysfunction in human skeletal muscle cells).
- **Avoid propofol entirely, or use with extreme caution and specialist input, in patients with known or suspected primary mitochondrial disease or fatty-acid β-oxidation disorders** — a pharmacogenetically informed avoidance strategy rather than dose modification.

**Secondary prevention (early detection):**
- Protocolized **serial biochemical monitoring** (arterial blood gas/lactate, CK, triglycerides) for any patient receiving propofol infusion >48 hours or at doses approaching/exceeding 4 mg/kg/h, to catch the "pre-PRIS" biochemical phase before cardiac decompensation.
- Continuous or serial **ECG monitoring** for early detection of the Brugada-pattern change, which should trigger immediate drug discontinuation.

**Tertiary prevention:** Prompt discontinuation and organ-supportive care at first biochemical or electrophysiological sign, as above, to prevent progression to fulminant, often-fatal cardiac collapse.

**Genetic counseling:** Relevant not for PRIS itself but for family members of a patient found, via a PRIS episode, to carry a primary mitochondrial or FAO disorder — standard genetic counseling for the underlying Mendelian/mitochondrial condition applies once identified.

**Public health/institutional measures:** Institutional sedation protocols and pharmacy/ICU guidelines capping propofol dose/duration, mandating biomarker surveillance, and specifying escalation triggers represent the practical "prophylaxis" infrastructure described across the clinical review literature (Fudickar A, Bein B, "The propofol infusion 'syndrome' in intensive care unit: from pathophysiology to prophylaxis and treatment," PMID: [18652104](https://pubmed.ncbi.nlm.nih.gov/18652104/)).

---

## 14. Other Species / Natural Disease

PRIS is not a naturally occurring veterinary disease entity in the sense of a spontaneously arising condition, but it is a recognized **iatrogenic risk in veterinary anesthesia/sedation practice** wherever propofol is used for prolonged infusion sedation in companion or laboratory animals, by direct pharmacological analogy to the human syndrome — no dedicated veterinary literature specific to spontaneous PRIS case series was surfaced in this search, and this section is best understood through the experimental-model lens in §15 rather than as natural disease.

**Taxonomy of species used in experimental modeling:** rat (*Rattus norvegicus*, NCBITaxon:10116), mouse (*Mus musculus*, NCBITaxon:10090), rabbit (*Oryctolagus cuniculus*, NCBITaxon:9986) — see §15.

**Comparative biology:** The core molecular targets (CPT1, mitochondrial Complexes I/III, coenzyme Q) are highly conserved across mammals, which is why rodent and rabbit models recapitulate the human bioenergetic lesion faithfully at the mitochondrial/cellular level, even though whole-organism experimental PRIS models are engineered (via deliberate high-dose infusion) rather than naturally occurring.

**Zoonotic potential:** Not applicable — this is a pharmacotoxic, not an infectious, condition.

---

## 15. Model Organisms

| Model | Species/system | What it captures | Fidelity notes |
|---|---|---|---|
| Isolated-perfused newborn mouse heart | *Mus musculus* (ex vivo) | Acute propofol-induced cardiotoxicity — ECG, ventricular contractile force, oxygen extraction measured over 30 min toxic-dose exposure; a proposed ex-vivo model relevant specifically to **pediatric** PRIS (PMC9350423) | High fidelity for the acute cardiac electromechanical phenotype in the developing heart; does not capture the full multi-organ (renal/hepatic) syndrome |
| Newborn murine cardiac mitochondria (in vitro) | *Mus musculus* | Mitochondrial respiration, membrane potential, and respiratory chain complex kinetics directly exposed to propofol/Intralipid (*Pediatr Res* 2022) | Isolates the mitochondrial mechanism cleanly from whole-organ/systemic confounders |
| Murine skeletal muscle injury model | *Mus musculus* (in vivo) | Basic mechanistic study of PRIS-associated skeletal muscle injury (PMC6712282) | Captures the rhabdomyolysis-relevant skeletal muscle arm of the syndrome |
| Rat model of sepsis + propofol | *Rattus norvegicus* (in vivo) | Demonstrates propofol increases morbidity/mortality in the setting of sepsis, mechanistically supporting the clinical sepsis risk-factor association (*Crit Care* 2015) | Models the gene-environment-like interaction between a systemic inflammatory state and propofol toxicity, though this is an environment-environment interaction rather than a genetic one |
| Rat isolated mitochondria / respiratory chain studies | *Rattus norvegicus* (ex vivo) | Identified coenzyme Q as the principal electron-transport-chain interaction site for propofol | Mechanistic, subcellular-level model |
| Rabbit PRIS model | *Oryctolagus cuniculus* (in vivo) | Whole-animal PRIS induction with survival and organ-injury endpoints; used to test coenzyme Q10 as a rescue therapy (PMC10584382) | Closest available whole-organism model to the clinical multi-organ syndrome; supports a translational candidate therapy |
| Human primary skeletal muscle cell culture | *Homo sapiens* (in vitro, primary cells) | Direct demonstration of clinically-relevant-concentration propofol inhibiting fatty-acid oxidation and reducing ETC spare capacity and ATP synthesis; also used to show noradrenaline potentiates the mitochondrial injury (PMID: [29240609](https://pubmed.ncbi.nlm.nih.gov/29240609/); PMC9643307) | Highest translational relevance since it uses human tissue directly, though it cannot capture the whole-organism cardiac/renal phenotype |

**Model limitations common across the set:** most models are acute/short-duration exposures (30 minutes to hours) rather than the 48-hour-plus infusions characteristic of clinical PRIS, and none fully recapitulates the combined multi-organ syndrome (cardiac + renal + hepatic + metabolic) simultaneously in a single system — each model instead isolates one mechanistic or organ-specific arm of the human disease.

**Research applications:** These models collectively support (a) the mitochondrial FAO/ETC inhibition mechanism, (b) the catecholamine-potentiation and sepsis-potentiation risk-factor mechanisms, (c) age-specific (developing heart) vulnerability, and (d) candidate rescue therapies (coenzyme Q10) — directly informing the pathophysiology and prevention/treatment sections above.

---

## Summary of Key Ontology Term Suggestions for KB Curation

- **CHEBI:** `CHEBI:44915` (propofol)
- **GO (Biological Process):** GO:0006635 (fatty acid beta-oxidation), GO:0022904 (respiratory electron transport chain), GO:0006119 (oxidative phosphorylation), GO:0006915 (apoptotic process)
- **GO (Cellular Component):** GO:0005743 (mitochondrial inner membrane), GO:0005739 (mitochondrion)
- **CL:** CL:0000746 (cardiac muscle cell), CL:0000188 (skeletal muscle fiber), CL:0000182 (hepatocyte)
- **UBERON:** UBERON:0001133 (cardiac muscle tissue), UBERON:0001134 (skeletal muscle tissue), UBERON:0002107 (liver), UBERON:0002113 (kidney)
- **HP:** HP:0001942 (Metabolic acidosis), HP:0003201 (Rhabdomyolysis), HP:0002153 (Hyperkalemia), HP:0003077 (Hyperlipidemia), HP:0002240 (Hepatomegaly), HP:0001919 (Acute kidney injury), HP:0001638 (Cardiomyopathy), HP:0001688 (Sinus bradycardia), HP:0001945 (Fever)
- **HGNC (mechanistically relevant, not causal):** CPT1A (HGNC:2328), CPT2 (HGNC:2330), SLC25A20 (carnitine-acylcarnitine translocase), SCN5A (HGNC:10593), POLG (HGNC:9179)
- **MONDO:** none currently exists (documented gap, dismech issue #13101)

---

## Key Cited Sources

- Bray RJ. Propofol infusion syndrome in children. *Paediatr Anaesth*. 1998. (index description; summarized in [PMC8660594](https://pmc.ncbi.nlm.nih.gov/articles/PMC8660594/))
- Vasile B, Rasulo F, Candiani A, Latronico N. The pathophysiology of propofol infusion syndrome: a simple name for a complex syndrome. *Intensive Care Med*. 2003;29(9):1417-25. PMID: [12904852](https://pubmed.ncbi.nlm.nih.gov/12904852/)
- Wolf A, Weir P, Segar P, Stone J, Shield J. Impaired fatty acid oxidation in propofol infusion syndrome. *Lancet*. 2001. PMID: [11558490](https://pubmed.ncbi.nlm.nih.gov/11558490/)
- Kam PC, Cardone D. Propofol infusion syndrome. *Anaesthesia*. 2007. PMID: [17567345](https://pubmed.ncbi.nlm.nih.gov/17567345/)
- Fudickar A, Bein B. The propofol infusion "syndrome" in intensive care unit: from pathophysiology to prophylaxis and treatment. PMID: [18652104](https://pubmed.ncbi.nlm.nih.gov/18652104/)
- Roberts RJ, et al. Incidence of propofol-related infusion syndrome in critically ill adults: a prospective, multicenter study. *Crit Care*. 2009. [PMC2784401](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2784401/)
- Fong JJ, et al. Predictors of mortality in patients with suspected propofol infusion syndrome. PMID: [18664783](https://pubmed.ncbi.nlm.nih.gov/18664783/)
- Vernooy K, et al. Electrocardiographic changes predicting sudden death in propofol-related infusion syndrome. [PMC1474111](https://pmc.ncbi.nlm.nih.gov/articles/PMC1474111/)
- Mirrakhimov AE, et al. Propofol Infusion Syndrome in Adults: A Clinical Update. *Crit Care Res Pract*. 2015. [PMC4410753](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4410753/)
- Krajčová A, Waldauf P, Anděl M, Duška F. Propofol infusion syndrome: a structured review of experimental studies and 153 published case reports. *Crit Care*. 2015;19:398. PMID: [26558513](https://pubmed.ncbi.nlm.nih.gov/26558513/)
- Hemphill S, et al. Propofol infusion syndrome: a structured literature review and analysis of published case reports. *Br J Anaesth*. 2019. [S0007091219300108](https://www.bjanaesthesia.org.uk/article/S0007-0912(19)30010-8/fulltext)
- Finsterer J, Frank M. Propofol Is Mitochondrion-Toxic and May Unmask a Mitochondrial Disorder. *J Child Neurol*. 2016.
- Shimizu K, et al. Propofol infusion syndrome complicated with MELAS: a case report. *Acute Med Surg*. 2020. [10.1002/ams2.473](https://onlinelibrary.wiley.com/doi/10.1002/ams2.473)
- Case report: PRIS heralding a mitochondrial disease. *Neurology*. 2014. PMID: [24491974](https://pubmed.ncbi.nlm.nih.gov/24491974)
- Sustained mitochondrial damage in cardiomyocytes in patients with severe PRIS (case report). [PMC8905003](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8905003/)
- Effects of Propofol on Cellular Bioenergetics in Human Skeletal Muscle Cells. *Crit Care Med*. PMID: [29240609](https://pubmed.ncbi.nlm.nih.gov/29240609/)
- Kinetic characteristics of propofol-induced inhibition of electron-transfer chain and fatty acid oxidation. PMID: [31584947](https://pubmed.ncbi.nlm.nih.gov/31584947/)
- Effect of noradrenaline on propofol-induced mitochondrial dysfunction in human skeletal muscle cells. [PMC9643307](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9643307/)
- Propofol increases morbidity and mortality in a rat model of sepsis. *Crit Care*. 2015. [10.1186/s13054-015-0751-x](https://link.springer.com/article/10.1186/s13054-015-0751-x)
- Modeling propofol-induced cardiotoxicity in the isolated-perfused newborn mouse heart. [PMC9350423](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9350423/)
- Propofol toxicity in the developing mouse heart mitochondria. *Pediatr Res*. 2022. [10.1038/s41390-022-01985-1](https://www.nature.com/articles/s41390-022-01985-1)
- Effects of coenzyme Q10 in a propofol infusion syndrome model of rabbits. [PMC10584382](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10584382/)
- Propofol-Related Infusion Syndrome in a Child With Refractory Status Epilepticus: ECMO/CRRT/TPE resuscitation. [PMC10613782](https://pmc.ncbi.nlm.nih.gov/articles/PMC10613782/)
- Propofol infusion syndrome resuscitation with extracorporeal life support (case report). [PMC3850887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3850887/)
- MeSH Browser entry D000072736. [meshb.nlm.nih.gov](https://meshb.nlm.nih.gov/record/ui?ui=D000072736)
- dismech GitHub issue #13101, "Curate propofol infusion syndrome, which has no MONDO term." [github.com/monarch-initiative/dismech/issues/13101](https://github.com/monarch-initiative/dismech/issues/13101)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 26 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:1001603` (1 mention) - the report calls it "kidney proximal tubule epithelial cell, relevant to myoglobin-mediated AKI"; CL calls it **lung macrophage**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0055114` (obsolete oxidation-reduction process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002910` (1 mention) - the report calls it "Elevated hepatic transaminase"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated transaminases" among its other names
- `GO:0055114` (1 mention) - the report calls it "oxidation-reduction process"; GO calls it **obsolete oxidation-reduction process**
- `CL:0000746` (3 mentions) - the report calls it "cardiac muscle cell", "Cardiac muscle tissue → cardiomyocytes"; CL calls it **cardiac muscle cell**, and lists "cardiac muscle fiber" among its other names
- `CL:0000188` (3 mentions) - the report calls it "skeletal muscle fiber", "Skeletal muscle tissue → skeletal myofibers"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `CL:0000182` (3 mentions) - the report calls it "hepatocyte", "Liver parenchyma → hepatocytes"; CL calls it **hepatocyte**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000746` - called "cardiac muscle cell", "Cardiac muscle tissue → cardiomyocytes"
- `CL:0000188` - called "skeletal muscle fiber", "Skeletal muscle tissue → skeletal myofibers"
- `CL:0000182` - called "hepatocyte", "Liver parenchyma → hepatocytes"