---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T01:20:59.483472'
end_time: '2026-09-04T01:25:12.302729'
duration_seconds: 252.82
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: IFNAR2 Deficiency
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
  web_search_requests: 17
  num_turns: 24
  total_cost_usd: 1.2214398
  session_id: 1d4c83ee-98b8-54c2-892b-3815ba752722
  stop_reason: end_turn
  assistant_text_blocks: 2
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:35442417
  relevance_assessed: 13
  on_topic: 10
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 39
  not_found: 1
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.025
  labels_checked: 28
  labels_matching: 20
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0025143
    reported_labels:
    - Lethargy
    ontology_label: Chills
  - term_id: HP:0025047
    reported_labels:
    - Maculopapular rash
    ontology_label: Abnormal brain choline level by MRS
  labels_variant: 6
  unresolved_terms:
  - HP:0002264
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IFNAR2 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IFNAR2 Deficiency** covering all of the
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

I now have enough comprehensive, well-sourced material to write the full report.

I have sufficient sourced material to compile the comprehensive report now.

# IFNAR2 Deficiency (Immunodeficiency-45, IMD45): Comprehensive Research Report

## 1. Disease Information

### Overview
IFNAR2 deficiency is a rare, life-threatening autosomal recessive (and, per one recently described dominant-negative allele family in COVID-19, potentially oligogenic/dominant-modifying) primary immunodeficiency of the innate immune system caused by biallelic loss-of-function variants in *IFNAR2*, the gene encoding the high-affinity subunit of the type I interferon (IFN-α/β/ω) receptor. Loss of IFNAR2 abolishes cellular responsiveness to all type I interferons, leaving affected individuals unable to mount an antiviral interferon-stimulated gene (ISG) response. Clinically, the disorder is characterized by an essentially normal phenotype until exposure to a virus — whether wild-type (influenza, SARS-CoV-2) or live-attenuated vaccine strain (measles-mumps-rubella [MMR], yellow fever) — at which point patients can develop fulminant, often fatal, viral disease: encephalitis/meningoencephalitis, hemophagocytic lymphohistiocytosis (HLH), viscerotropic disease, or severe pneumonia (Duncan et al. 2015; Bastard et al. 2022; Hernandez et al. 2020).

> "Autosomal recessive deficiency of the IFNAR2 chain of the human type I IFN receptor abolishes cellular responses to IFN-α, -β, and -ω, underlies severe viral diseases, and is globally very rare, except for IFNAR2 deficiency in the Arctic." (Bastard et al. 2022, *J Exp Med*, PMID:35442417)

### Key Identifiers
| Resource | Identifier |
|---|---|
| Gene (HGNC) | IFNAR2, HGNC:5433 |
| OMIM gene | *602376 — Interferon-alpha, -beta, and -omega receptor 2 |
| OMIM phenotype | #616669 — Immunodeficiency 45 (IMD45) *(note: search results also referenced #614889, which corresponds to IMD28/ISG15 deficiency — verify the correct OMIM phenotype MIM number, 616669, directly before curation; there is some inconsistency across secondary sources)* |
| Orphanet | Listed as a major genetic susceptibility factor for "Primary immunodeficiency with post-measles-mumps-rubella vaccine viral infection" (ORPHA:431166) |
| Gene location | Chromosome 21q22.11 |
| Inheritance | Autosomal recessive (biallelic null/loss-of-function) |
| NCBI Gene / Ensembl | IFNAR2 |

### Synonyms
- Type I interferon receptor 2 deficiency
- IFN-α/β receptor subunit 2 deficiency
- Interferon alpha/beta receptor chain 2 deficiency
- IMD45 (Immunodeficiency 45)
- Complete IFNAR2 deficiency (vs. the milder, common hypomorphic/partial deficiencies seen as COVID-19 severity risk variants)

### Data Source Character
Nearly all clinical knowledge derives from **individual patient case reports and small case series** (single families, or clustered founder-variant cohorts in the Canadian/Greenlandic/Alaskan Arctic and Inuit populations), rather than large aggregated disease-level registries — this is a genuinely ultra-rare monogenic disorder. Population-level genomic data (gnomAD, biobank cohorts) contribute allele-frequency and severe-COVID-19-association evidence for common hypomorphic *IFNAR2* variants, which is a related but distinct body of evidence from the complete/biallelic-null Mendelian disease.

---

## 2. Etiology

### Disease Causal Factors
IFNAR2 deficiency is a **monogenic, purely genetic** disorder: biallelic (homozygous or compound heterozygous) loss-of-function variants in *IFNAR2* that abolish or markedly impair surface expression/function of the IFNAR2 receptor chain. The disease is fundamentally one of **gene-environment interaction**: the genetic lesion is clinically silent until a viral trigger (wild-type virus or live-attenuated vaccine) is encountered, at which point uncontrolled viral replication precipitates the phenotype.

### Genetic Risk Factors
Reported pathogenic variants include:

| Variant | Type | Population/Case | Source |
|---|---|---|---|
| Homozygous mutation (index case) rendering cells IFN-α/β-unresponsive | Loss-of-function | UK child, fatal post-MMR encephalitis (Duncan et al. 2015) | PMID (STM 2015, 7(307):307ra154, DOI:10.1126/scitranslmed.aac4227) |
| c.234delT (p.Leu79Ter, rs1310889473) + c.555_559delAAAAG (p.Ile185MetfsTer12, rs1312285586) | Compound heterozygous frameshift/nonsense | Caucasian boy, post-MMR HLH | PMID:33193576 (Hernandez et al. 2020, *Front Genet*) |
| c.157T>C, p.Ser53Pro (NM_207585.2) | Homozygous missense — founder variant | 5 patients, Greenland/Canada/Alaska (Inuit ancestry); MAF 0.034 in Inuit reference cohort, 0.026 (23/448 heterozygous carriers, no homozygotes) in unpublished Greenlandic WGS | PMID:35442417 (Bastard et al. 2022, *J Exp Med*) |
| Homozygous missense (VUS) | Missense | 10-month-old female, severe post-measles-vaccine reaction, viremia/meningoencephalitis/multi-organ failure | *J Clin Immunol* 2024/2025;45:30, DOI:10.1007/s10875-024-01814-6 |
| c.157T>C, p.Ser53Pro (same founder allele) | Homozygous | 13-month-old Inuit boy, northern Quebec — post-vaccination drug-resistant infantile epileptic spasms (West syndrome) | *Seizure — Eur J Epilepsy* 2022, PMID/DOI S1059-1311(22)00175-3 |
| Rare stop-gain variant (NM_000874:exon9:c.C966A, p.Y322X) and other predicted LOF *IFNAR2* variants | Heterozygous/burden-tested | COVID-19 severity cohort (ODYSSEY phase 3) | PMID:34273592 / PMC8279933 (Smieszek et al. 2021) |

**Mechanistic consequence of key variants:** The Ser53Pro substitution "prevented cell surface expression of IFNAR2 protein, small amounts of which persisted intracellularly in an aberrantly glycosylated state" (Bastard et al. 2022). The frameshift/nonsense compound-heterozygous variants are predicted to cause "complete lack of the protein" (Hernandez et al. 2020, PMID:33193576).

**Common (non-Mendelian) genetic risk modifiers:** Independent of the rare Mendelian disease, common *IFNAR2* polymorphisms (rs2236757, rs3153, rs1051393, rs2834158) have been associated with COVID-19 mortality risk in hospitalized cohorts, and soluble IFNAR2 plasma levels differ between survivors and non-survivors (Rodrigues et al. 2022, PMID:35967349, *Front Immunol*). This is a distinct, quantitative-trait/complex-disease association layer, not equivalent to biallelic loss-of-function.

### Environmental / Triggering Risk Factors
- **Live-attenuated viral vaccination** — MMR (measles, mumps, rubella components) and yellow fever vaccine (YFV) are the dominant identified triggers, causing meningoencephalitis, HLH, or viscerotropic disease.
- **Wild-type viral infection** — influenza and SARS-CoV-2 (COVID-19) have caused life-threatening disease in IFNAR2-deficient patients.
- Bastard et al. (2022) also reported IFNAR1/IFNAR2 deficiency and neutralizing type I IFN autoantibodies together accounting for "more than half the cases of life-threatening yellow fever vaccine-associated disease" in a broader cohort (related autoantibody-mediated phenocopy — see below).

### Protective Factors
No specific genetic or environmental protective factor has been documented for the rare biallelic-null disease; heterozygous carriers (parents, siblings) are consistently reported as asymptomatic, "without history of major infection or hyperinflammatory episodes, nor vaccination reactions" (Hernandez et al. 2020), consistent with recessive inheritance and adequate residual function from a single normal allele.

### Gene-Environment Interactions
This disease is a paradigm case of gene-environment interaction in inborn errors of immunity: the genotype is necessary but not sufficient — clinical disease requires viral (wild-type or vaccine-strain) exposure as the precipitating "second hit." This is analogous to, and mechanistically continuous with, the broader class of "inborn errors of type I IFN immunity" (which also includes IFNAR1, STAT1, STAT2, TYK2, IRF7, IRF9 deficiencies, and autoantibody-mediated type I IFN neutralization) recognized as a unifying mechanism for severe/critical viral pneumonia including COVID-19, influenza, and adverse reactions to live vaccines (Zhang et al.; Bastard et al., multiple JEM papers 2019–2022).

---

## 3. Phenotypes

### Symptoms, Signs, and Manifestations (by clinical context)

**Post-live-vaccine reactions:**
- Fever, lethargy, irritability (HP:0025143 lethargy)
- Myoclonic movements / seizures, evolving in one case to infantile epileptic spasms syndrome (West syndrome) — drug-resistant
- Cervical lymphadenopathy
- Maculopapular rash
- Meningoencephalitis / fatal encephalitis
- Multi-organ failure
- Viscerotropic disease (yellow-fever vaccine): hepatic dysfunction, coagulopathy

**HLH-associated laboratory/clinical findings** (from the compound-heterozygous frameshift case, PMID:33193576):
- Hyperferritinemia (4008 μg/L)
- Transaminitis: AST 360 U/L, ALT 550 U/L
- Elevated LDH: 3155 U/L
- Hypertriglyceridemia: 338 mg/dL
- Hypofibrinogenemia: 92.2 mg/dL
- Progressive cytopenias

**Wild-type viral infection:**
- Life-threatening/critical COVID-19 pneumonia
- Life-threatening influenza

### Phenotype Characteristics
- **Age of onset:** Typically infancy to early childhood (10 months–2 years in the reported cases), coinciding with the standard MMR vaccination schedule (12 months) or first serious wild-type viral exposure. The disorder is otherwise clinically silent (asymptomatic at baseline).
- **Severity:** Highly severe/life-threatening at presentation — several index cases were fatal (the original Duncan et al. index patient died; a sibling case was also affected).
- **Progression:** Acute, fulminant onset following the triggering exposure; not a chronic progressive disease between triggering events.
- **Frequency among affected individuals:** Based on the small number of reported kindreds (fewer than ~10 published families/individuals worldwide as complete biallelic deficiency, plus the Arctic founder-variant cluster of 5 patients), most reported patients present with either (a) post-live-vaccine encephalitis/HLH, or (b) life-threatening wild-type viral disease (influenza, COVID-19).

### Suggested HPO Terms
- HP:0002383 — Encephalitis (or HP:0002264 Meningoencephalitis)
- HP:0005537 — Hemophagocytosis / HP:0001744 Splenomegaly / features of HLH
- HP:0001945 — Fever
- HP:0002014 — Diarrhea (nonspecific, if present)
- HP:0002133 — Status epilepticus / HP:0032792 Infantile spasms
- HP:0025143 — Lethargy
- HP:0025047 — Maculopapular rash
- HP:0002240 — Hepatomegaly
- HP:0001945 — Recurrent/severe viral infections — consider HP:0002718 (Recurrent infections) or HP:0004429 (susceptibility to viral infections, if available in HPO)
- HP:0011024 — Abnormality of the gastrointestinal system (viscerotropic disease)
- HP:0011893 — Abnormal leukocyte count / cytopenias

### Quality of Life Impact
Not formally studied via standardized instruments (no EQ-5D/SF-36 data identified) given disease rarity; qualitatively, survivors of severe episodes (e.g., the epileptic-spasms case) face long-term neurodevelopmental sequelae from drug-resistant epilepsy, while patients successfully treated for HLH (e.g., the compound-heterozygous case managed with corticosteroids) have been reported as developing normally at follow-up (4 years old, "in good general condition," normal growth) (PMID:33193576).

---

## 4. Genetic / Molecular Information

### Causal Gene
- **IFNAR2** (HGNC:5433), chromosome 21q22.11, OMIM *602376. Encodes the high-affinity ligand-binding subunit of the type I interferon receptor.

### Gene/Protein Structure
- IFNAR2 encodes a **487-residue type II cytokine-receptor-family transmembrane protein** with an N-terminal extracellular ligand-binding domain composed of **two fibronectin type III (FnIII)-like subdomains** (in contrast to IFNAR1's four FnIII repeats), a single transmembrane domain, and a cytoplasmic tail.
- IFNAR2 constitutively associates with **STAT2** via its cytoplasmic domain (STAT2-binding site within the C-terminal ~110 amino acids); STAT2 recruits STAT1 upon activation.

### Variant Classification / Types
- Nonsense (p.Leu79Ter), frameshift (p.Ile185MetfsTer12), and missense (p.Ser53Pro) variants have all been reported causing complete loss of IFNAR2 surface expression.
- All confirmed pathogenic variants for the complete Mendelian disease are recessive (require biallelic hit — homozygous or compound heterozygous).
- Population databases (gnomAD): the frameshift variants are extremely rare (allele frequencies 0.000004–0.000016); the Ser53Pro founder variant is essentially absent from global gnomAD but reaches MAF 0.026–0.034 in Arctic Inuit reference populations — a striking example of a population-specific founder allele with major clinical relevance in that population.

### Functional Consequences (mechanistically demonstrated)
- **Loss of cell-surface IFNAR2 expression** on patient leukocytes (flow cytometry) — confirmed across multiple case reports.
- **Abolished STAT1 phosphorylation** upon IFN-α stimulation of monocytes, while IFN-γ (type II)-induced STAT1 phosphorylation remains intact — confirms selective type I IFN pathway defect with preserved type II (IFN-γ) signaling.
- **Failure to induce type I interferon-stimulated genes** (ISGs) — IFI27, IFI44L, CXCL10, ISG15, RSAD2, SIGLEC1 all fail to be induced upon ex vivo IFN-α stimulation of whole blood.
- **No CXCL10 chemokine production** upon IFN-α stimulation of PBMCs (IFN-γ-induced CXCL10 normal).
- **NK cell dysfunction:** patient NK cells fail to upregulate CD107a degranulation marker upon IFN-α pre-incubation (~3-fold increase seen in controls/parents, absent in patient), and fail to show the normal IFN-α-mediated *suppression* of intracellular IFN-γ production — proposed as a mechanistic link between IFNAR2 loss and HLH development via NK cell dysregulation.
- **In vitro increased vulnerability to multiple viruses** — patient cells show enhanced viral replication/susceptibility compared to controls.
- Reconstitution of patient cells with wild-type IFNAR2 restores IFN-α/β responsiveness and antiviral control (Duncan et al. 2015), functionally confirming causality.

### Modifier Genes / Related Disease Mechanisms (phenocopies)
IFNAR2 deficiency sits within a broader group of "inborn errors of type I IFN immunity" with overlapping phenotypes, useful for differential diagnosis and pathway context:
- **IFNAR1** deficiency (its receptor-partner subunit) — clinically near-identical phenotype (HLH, encephalitis, severe COVID-19/influenza, adverse vaccine reactions); a common Polynesian/Pacific founder loss-of-function allele has been characterized (PMC9026234).
- **STAT2** deficiency — complete deficiency causes similar inflammatory viral disease (PMC10266780); a distinct STAT2 gain-of-function/loss-of-negative-regulation form causes a type I interferonopathy.
- **STAT1**, **TYK2**, **IRF7**, **IRF9** deficiencies — related type I/III IFN pathway inborn errors.
- **Autoantibodies neutralizing type I IFN** — a phenocopy mechanism (not genetic) producing an equivalent functional block, notably implicated in adult critical COVID-19 and yellow-fever-vaccine-associated disease.

### Epigenetics / Chromosomal Abnormalities
No epigenetic regulation studies or chromosomal structural abnormalities (aneuploidy, translocation) have been reported specific to IFNAR2 deficiency; the gene lies in the cytokine-receptor gene cluster on 21q22.11 alongside IFNAR1, IL10RB, IFNGR2, and IL10RB, all part of the ancestral interferon-receptor cluster on chromosome 21.

---

## 5. Environmental Information

- **Live-attenuated viral vaccines** (MMR, yellow fever) are the principal, well-documented environmental trigger precipitating fulminant disease in genetically susceptible individuals — this is the dominant "environmental factor" for this disorder rather than toxins or occupational exposures.
- **Wild-type respiratory/systemic viruses**: influenza virus and SARS-CoV-2 are documented triggers of life-threatening disease.
- No infectious *co-trigger*, toxin, or lifestyle/dietary risk factor has been reported; this is not a disease with a classical toxicological or occupational-exposure etiology axis — its "environmental" dimension is essentially virological.
- **Infectious agents directly relevant:** measles virus (vaccine strain), mumps virus (vaccine strain), rubella virus (vaccine strain), yellow fever virus (vaccine strain 17D), influenza A virus, SARS-CoV-2.

---

## 6. Mechanism / Pathophysiology

### Causal Chain (ordered)

1. Biallelic loss-of-function variant in *IFNAR2* (nonsense, frameshift, or a destabilizing missense such as p.Ser53Pro) **leads to** absent or non-functional IFNAR2 protein, either through nonsense-mediated decay/truncation or failure of the mutant protein to traffic to the cell surface (retained intracellularly in an aberrantly glycosylated state for Ser53Pro).
2. Absent surface IFNAR2 **results in** failure to form a functional IFNAR1–IFNAR2 heterodimeric type I interferon receptor complex upon IFN-α/β/ω binding.
3. Without receptor dimerization, the receptor-associated Janus kinases — TYK2 (bound to IFNAR1) and JAK1 (bound to IFNAR2) — **fail to be recruited/cross-phosphorylate**; because STAT2 is constitutively docked on the IFNAR2 cytoplasmic tail (via its C-terminal ~110 aa), loss of IFNAR2 specifically eliminates the STAT2 docking site required for downstream signaling. (Demonstrated experimentally: this is inferred from the receptor biology and is directly supported by loss of STAT1 phosphorylation in patient cells.)
4. This **leads to** absent STAT1/STAT2 phosphorylation and failure of ISGF3 (STAT1–STAT2–IRF9) complex formation and nuclear translocation — directly demonstrated by absent STAT1 phosphorylation upon IFN-α stimulation of patient monocytes, while IFN-γ→STAT1 phosphorylation (a JAK1/JAK2, IFNGR-dependent, IFNAR-independent pathway) remains intact, confirming pathway selectivity.
5. Failure of ISGF3 formation **results in** failure to transactivate interferon-stimulated response elements (ISREs), demonstrated as absent induction of ISGs (IFI27, IFI44L, CXCL10, ISG15, RSAD2, SIGLEC1) and absent CXCL10 protein secretion upon ex vivo IFN-α challenge.
6. Loss of the cell-intrinsic antiviral ISG program **leads to** unrestrained viral replication in infected cells upon exposure to IFN-sensitive viruses — demonstrated in vitro as increased viral susceptibility of patient cells and functionally rescued by IFNAR2 reconstitution (Duncan et al. 2015).
7. In parallel, loss of IFN-α signaling in **NK cells** specifically **abolishes** the normal IFN-α-induced upregulation of degranulation (CD107a) and the normal IFN-α-mediated *suppression* of NK-cell IFN-γ production — this dysregulated, unrestrained NK-cell IFN-γ output is proposed (branch point) to **drive** the macrophage-activation/hyperinflammatory state that manifests as hemophagocytic lymphohistiocytosis (HLH) in a subset of patients — this branch is mechanistically plausible and evidence-supported at the cellular level but the causal link to clinical HLH onset remains partly inferential.
8. Unrestrained viral replication (branch A) and/or NK-cell-driven hyperinflammation (branch B) together **culminate in** the clinical syndromes observed: fulminant viral encephalitis/meningoencephalitis, viscerotropic disease, HLH with multi-organ dysfunction, or severe/critical viral pneumonia (influenza, COVID-19), depending on the triggering virus, tissue tropism, and host inflammatory response.

### Molecular Pathways
- **Type I interferon / JAK-STAT signaling (ISGF3 pathway)**: IFNAR1–IFNAR2 → TYK2/JAK1 → STAT1/STAT2 → ISGF3 (with IRF9) → ISRE-driven ISG transcription. This is the central, disrupted pathway. (KEGG: hsa04630 Jak-STAT signaling pathway; Reactome: Interferon alpha/beta signaling, R-HSA-909733.)

### Cellular Processes
- Antiviral restriction-factor induction (failure)
- NK cell cytotoxic degranulation regulation (failure of IFN-α-mediated enhancement)
- NK cell cytokine (IFN-γ) output regulation (failure of IFN-α-mediated suppression) — implicated in HLH pathogenesis
- Monocyte/macrophage activation — secondary hyperinflammatory state in HLH

### Protein Dysfunction
- Loss-of-function via truncation (nonsense/frameshift) or via a folding/trafficking defect that traps mutant protein intracellularly (Ser53Pro missense) — a form of "hypomorphic/complete LOF via mislocalization" rather than catalytic-site disruption, since IFNAR2 itself has no enzymatic activity but serves as a scaffold/docking subunit.

### Immune System Involvement
This is fundamentally an **innate antiviral immunodeficiency** with a **secondary hyperinflammatory (HLH-like) phenotype** — an unusual combination in which immunodeficiency and immune dysregulation coexist, mediated respectively by loss of direct antiviral ISG induction and by NK-cell dysregulation.

### Suggested GO Terms
- GO:0038196 — interferon-alpha-beta receptor complex / GO:0004905 type I interferon receptor activity
- GO:0060337 — type I interferon-mediated signaling pathway
- GO:0060333 — interferon-gamma-mediated signaling pathway (preserved, contrast)
- GO:0007259 — cell surface receptor signaling pathway via JAK-STAT
- GO:0032481 — positive regulation of type I interferon production
- GO:0002323 — natural killer cell activation involved in immune response
- GO:0001916 — positive regulation of T cell mediated cytotoxicity (NK degranulation context — CL/GO adjacent)

### Suggested CL Terms
- CL:0000576 — monocyte
- CL:0000623 — natural killer cell
- CL:0000542 — lymphocyte
- CL:0000235 — macrophage (HLH effector)

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Central nervous system (encephalitis/meningoencephalitis — the dominant severe presentation), liver (transaminitis, viscerotropic hepatic involvement, hepatomegaly), spleen (HLH-associated splenomegaly, reported elsewhere in interferonopathy literature), bone marrow/hematopoietic system (cytopenias, hemophagocytosis), respiratory system (viral pneumonia in influenza/COVID-19 presentations).
- **Secondary/systemic:** Multi-organ failure in severe cases (viscerotropic yellow-fever disease, fulminant HLH).
- **Body systems involved:** Immune system (primary defect), nervous system, hepatobiliary system, hematologic system, respiratory system.
- **Tissue/cell level:** Leukocytes broadly (monocytes, NK cells, lymphocytes) fail to express surface IFNAR2 and fail to respond to type I IFN — this is a systemic, hematopoietic-lineage-wide receptor defect, not tissue-restricted.
- **Subcellular level:** Plasma membrane (absent receptor localization); for Ser53Pro, intracellular retention (likely ER/Golgi, aberrant glycosylation) rather than normal trafficking to the cell surface — GO Cellular Component: GO:0005886 (plasma membrane), GO:0005783 (endoplasmic reticulum, for the trafficking-defective mutant).
- **UBERON suggestions:** UBERON:0000955 (brain), UBERON:0002107 (liver), UBERON:0002106 (spleen), UBERON:0002371 (bone marrow), UBERON:0002048 (lung).
- **Localization:** No lateralization; systemic/multi-organ, virus-tropism-dependent.

---

## 8. Temporal Development

- **Onset:** Infancy/early childhood, precipitated by the routine vaccination schedule (MMR typically given ~12 months) or first severe wild-type viral exposure. The disease itself is congenital (genetic), but clinical onset is event-triggered rather than present at birth.
- **Onset pattern:** Acute/fulminant following the triggering exposure — days after vaccination in the classic cases (e.g., "5 days after MMR vaccination").
- **Progression:** Rapid, severe deterioration once triggered (encephalitis, HLH, multi-organ failure over days).
- **Disease course pattern:** Episodic/event-triggered rather than continuously progressive — between triggering viral exposures patients are reported as clinically well. However, a single severe episode can leave lasting sequelae (e.g., drug-resistant epilepsy/infantile spasms following an encephalopathic episode).
- **Critical periods:** The period surrounding live-vaccine administration is a recognized critical window of vulnerability; this underlies proposals for **pre-vaccination genetic screening** in populations with known founder alleles (e.g., Arctic Inuit communities) or in infants with a family history of severe vaccine reactions.
- **Remission:** With prompt recognition and treatment (e.g., corticosteroids for HLH), patients can recover and remain well; the compound-heterozygous HLH case was reported in good health and normally growing at 4 years follow-up, having subsequently tolerated additional infections (febrile seizure, influenza A/HSV coinfection) without HLH recurrence.

---

## 9. Inheritance and Population

### Epidemiology
- Extremely rare globally; fewer than ten published kindreds/individuals with confirmed complete biallelic IFNAR2 deficiency as of the most recent literature identified (2015–2025).
- **Notable exception — Arctic/Inuit founder effect:** the p.Ser53Pro allele reaches a minor allele frequency of ~0.026–0.034 in Inuit reference populations from Greenland/Canada/Alaska, making IFNAR2 deficiency a locally non-negligible cause of severe pediatric viral/vaccine-associated disease in this population, with an estimated homozygote (affected) frequency on the order of 1 in ~1,000–2,000 in Inuit communities based on Hardy-Weinberg expectation from the reported carrier frequency (this is an approximation derived from the reported allele frequency, not a directly reported incidence figure, and should be validated against the primary source before use as a curated statistic).

### Inheritance Pattern
- **Autosomal recessive** for the complete/Mendelian disease (biallelic homozygous or compound heterozygous loss-of-function).
- Common hypomorphic *IFNAR2* variants associated with COVID-19 severity behave as complex-trait risk alleles (not simple recessive Mendelian disease).

### Penetrance / Expressivity
- Penetrance for severe disease is **incomplete and exposure-dependent**: genotype alone does not predict a clinical event; a specific viral (or live-vaccine) exposure is required to trigger disease. Among the founder-variant homozygotes ascertained through clinical presentation, expressivity varies (encephalitis vs. HLH vs. epileptic spasms vs. severe COVID-19/influenza), indicating pleiotropic/variable expressivity depending on the triggering pathogen and host factors.
- No reported genetic anticipation, germline mosaicism, or imprinting phenomena.

### Founder Effects / Consanguinity
- Strong, well-documented **founder effect** for p.Ser53Pro in circumpolar Inuit populations (Greenland, Arctic Canada, Alaska).
- Consanguinity is not specifically emphasized in the literature relative to the founder-population homozygosity mechanism, though standard recessive-disease logic (increased homozygosity risk with shared ancestry) applies.

### Population Demographics
- Affected populations: Reported cases span European/Caucasian (index UK case), and importantly Inuit/circumpolar Arctic populations (Greenland, northern Quebec/Canada, Alaska) where the founder allele is common.
- No formal sex-ratio or age-distribution registry data exists given the rarity and case-report-based evidence base.

---

## 10. Diagnostics

### Laboratory / Functional Tests
- **Flow cytometry** for IFNAR2 surface expression on leukocytes (monocytes, lymphocytes) — absent or markedly reduced in affected patients; this is a key functional screening assay.
- **STAT1 phosphorylation assay** (phospho-flow or immunoblot) after ex vivo IFN-α stimulation of PBMCs/monocytes — absent in patients, normal after IFN-γ stimulation (differentiates type I from type II IFN pathway defects — critical for distinguishing IFNAR1/IFNAR2/STAT2/TYK2 defects from IFNGR/STAT1-only defects).
- **ISG induction assay** — qPCR for IFI27, IFI44L, CXCL10, ISG15, RSAD2, SIGLEC1 transcripts after ex vivo IFN-α stimulation of whole blood; failure to induce is diagnostic.
- **CXCL10 (IP-10) protein assay** (ELISA/Luminex) after IFN-α stimulation of PBMCs.
- **NK cell functional assays**: CD107a degranulation assay with/without IFN-α pre-incubation; intracellular IFN-γ staining.
- **HLH-directed labs** when clinically indicated: ferritin, triglycerides, fibrinogen, soluble CD25 (sIL-2R), AST/ALT/LDH, cytopenia panel — per HLH-2004 diagnostic criteria.

### Genetic Testing
- **Targeted single-gene sequencing** of *IFNAR2*, or more commonly, ascertainment through **broader gene panels** for primary immunodeficiency, HLH-associated genes, or (as in the epileptic-spasms case) a "comprehensive developmental disorders gene panel."
- **Whole exome/genome sequencing** — used in most reported cases, given the initially unclear differential diagnosis (encephalitis, HLH, or epilepsy of unknown cause).
- **Population/founder screening** — proposed pre-vaccination genetic screening for the p.Ser53Pro allele has been suggested for Arctic Inuit populations given the relatively high carrier frequency and severe/fatal consequences of missed diagnosis before live-vaccine administration.
- Standard variant interpretation follows ACMG/AMP criteria; the 2024 measles-vaccine case report specifically flagged its causal variant as a **Variant of Uncertain Significance (VUS)** pending confirmatory functional studies, illustrating that not every case yields an unambiguous ClinVar "pathogenic" classification without functional workup.

### Clinical/Differential Diagnosis
- Differential diagnosis for the acute presentation includes other inborn errors of type I/III IFN immunity (IFNAR1, STAT1, STAT2, TYK2, IRF7, IRF9 deficiencies), primary HLH (perforin pathway defects: PRF1, UNC13D, STX11, STXBP2), and autoantibody-mediated type I IFN neutralization (an important phenocopy, especially in adults with critical COVID-19 or yellow-fever vaccine-associated disease) — anti-IFN autoantibody testing should be considered as a parallel or alternative diagnostic pathway when genetic testing is negative.
- Standard HLH-2004 clinical criteria apply for the hyperinflammatory phenotype.

### Screening
- No newborn screening program currently exists for IFNAR2 deficiency; targeted carrier/pre-vaccination screening has been proposed specifically for high-risk founder populations (Arctic Inuit) and for infants with a family history of severe vaccine reactions, paralleling published clinical guidance for the analogous IFNAR1 Oceania founder allele ("Guideline for the Diagnosis and Management of Heritable IFNAR1 Deficiency in Oceania," PMID cited in search but exact number should be verified against PubMed directly).

---

## 11. Outcome / Prognosis

- **Mortality:** Case-fatality is substantial among reported index cases — the original 2015 index patient died of fatal encephalitis; other reported patients have died from viscerotropic yellow-fever-vaccine disease or fulminant viral disease. No formal population-level mortality rate exists given the small numbers.
- **Morbidity:** Survivors can have significant long-term morbidity — e.g., drug-resistant infantile epileptic spasms/West syndrome with attendant neurodevelopmental impairment following a post-vaccination encephalopathic episode.
- **Recovery potential with treatment:** Prompt recognition and immunosuppressive treatment of the HLH phenotype (e.g., high-dose corticosteroids) has achieved good outcomes in at least one reported case, with the patient healthy and developing normally at 4-year follow-up and subsequently tolerating further infections without recurrence — suggesting that outcome is highly dependent on early recognition and supportive/immunomodulatory management of the hyperinflammatory complication, even though the underlying antiviral defect is not itself correctable outside of gene/receptor reconstitution research settings.
- **Prognostic factors:** Speed of diagnosis/treatment initiation for HLH; specific triggering virus and organ tropism (CNS involvement carries the worst prognosis); possibly variant type (complete null vs. partial/hypomorphic), though this has not been systematically studied given the small case numbers.

---

## 12. Treatment

- **No disease-specific curative therapy exists.** Management is reactive/supportive, directed at the triggering viral infection and any resulting hyperinflammatory (HLH) complication, since IFNAR2 loss cannot currently be pharmacologically corrected.
- **HLH-directed immunosuppression:** IV methylprednisolone pulse therapy (30 mg/kg/day × 3 days) followed by tapering high-dose glucocorticoids (2 mg/kg) achieved clinical improvement in the reported compound-heterozygous case (NCIT:C2977 Corticosteroid; NCIT:C15632 or NCIT:C15986 for broader HLH-directed chemo-immunotherapy such as etoposide-based HLH-94/HLH-2004 protocols in more severe cases, though etoposide use was not specifically reported in the identified cases).
- **Antimicrobial/antiviral supportive therapy** for subsequent infections (e.g., standard antimicrobial therapy for febrile seizure and combined influenza A/HSV infection in the same patient, without recurrence of HLH).
- **Avoidance of live-attenuated vaccines** is the central preventive/management principle once the diagnosis is established or strongly suspected (family history, founder-population ancestry) — i.e., contraindicating MMR and yellow fever vaccines, and considering alternative protection strategies (e.g., passive immunoprophylaxis, isolation/exposure precautions) for measles/rubella/mumps/yellow-fever risk.
- **No approved gene therapy, cell therapy, or receptor-reconstitution therapy** exists for this condition in humans; Duncan et al. (2015) demonstrated **experimental reconstitution of patient cells with wild-type IFNAR2** in vitro restores antiviral responsiveness, establishing proof-of-concept for a gene-replacement approach, but this remains a research-only finding, not a clinical therapy (NCIT:C15238 Gene Therapy would be the relevant NCIT term for any future translational approach).
- **Hematopoietic stem cell transplantation (HSCT)** has been used for other severe inborn errors of type I IFN immunity/HLH-associated primary immunodeficiencies in general practice, though it was not specifically reported as used in the identified IFNAR2 case reports; it represents a plausible but unconfirmed option for refractory/recurrent cases (NCIT:C15431 Hematopoietic Cell Transplantation).
- **Genetic counseling** (NCIT:C15240) is indicated for families, especially in founder populations, given the autosomal recessive inheritance and the severity of the phenotype.

---

## 13. Prevention

- **Primary prevention:** The principal actionable primary-prevention strategy identified in the literature is **avoidance of live-attenuated viral vaccines** (MMR, yellow fever) in known or suspected IFNAR2-deficient individuals — analogous published guidance exists for IFNAR1 deficiency ("Guideline for the Diagnosis and Management of Heritable IFNAR1 Deficiency in Oceania").
- **Pre-vaccination genetic screening** in high-risk founder populations (Arctic Inuit communities carrying p.Ser53Pro) has been explicitly proposed by the primary literature as a means to identify at-risk infants before routine MMR administration.
- **Secondary prevention:** Early recognition of post-vaccination or post-infection fever/lethargy/rash in at-risk families, with rapid clinical evaluation for encephalitis/HLH, to enable prompt immunomodulatory treatment.
- **Genetic counseling** for families of affected individuals and for carrier identification in founder populations.
- **No vaccine (for the disease itself, obviously not applicable) or chemoprophylactic agent** exists; general public-health measures (standard infection control) apply but are not disease-specific.

---

## 14. Other Species / Natural Disease

- No naturally occurring veterinary/companion-animal disease analog of IFNAR2 deficiency has been identified in the literature reviewed (no OMIA entries surfaced in this search).
- **Orthology:** Mouse ortholog *Ifnar2* (MGI:1098243), located on mouse chromosome 16, is the standard model-organism counterpart used extensively in engineered (not naturally occurring) knockout studies (see Model Organisms, below).
- **Comparative biology:** The IFNAR1/IFNAR2 receptor system and downstream JAK-STAT (ISGF3) signaling pathway is deeply conserved across mammals, supporting strong translational relevance of mouse knockout data, though mice differ from humans in interferon subtype repertoire and some aspects of receptor biology.

---

## 15. Model Organisms

- **Ifnar2 knockout mice (Ifnar2⁻/⁻)** are a long-established and widely used model (MGI:1098243; e.g., commercially available strains such as Cyagen's C57BL/6NCya-Ifnar2^em1/Cya). Reported phenotypes include:
  - Defects in NK cell, CD4+ and CD8+ T cell, and B cell responses to induced/transplanted tumors, viruses, and dsDNA challenge.
  - Diminished secretion of both type I and (secondarily) type II interferons.
  - Altered/differential susceptibility to post-influenza bacterial superinfection compared with Ifnar1⁻/⁻ mice, indicating that despite forming an obligate heterodimer, the two receptor chains are not perfectly functionally redundant in every downstream context — a nuance relevant to interpreting human IFNAR1 vs. IFNAR2 deficiency phenotypic overlap/differences.
  - Broadly recapitulates loss of antiviral, antiproliferative, antiangiogenic, and immunomodulatory type-I-IFN-dependent responses.
- **Humanized IFNAR mouse models**: an "extracellular humanized IFNAR immunocompetent mouse model" has been developed for analysis of human IFN-α and its subtypes (PMID:37994664; PMC10810641), useful for testing human-specific interferon pharmacology and potentially for future receptor-reconstitution/gene-therapy proof-of-concept work.
- **Ifnar1⁻/Ifnar2⁻ double and single knockouts** are broadly used across virology as standard "type I IFN receptor knockout" models for high-consequence/BSL3-4 pathogens (e.g., flaviviruses, alphaviruses) precisely because they phenocopy the profound susceptibility to IFN-sensitive viruses seen in human patients — directly modeling the "increased vulnerability to multiple viruses" phenotype documented in human patient cells.
- No induced/environmental (non-genetic) animal models specific to this disease were identified; all model-organism evidence is from targeted genetic (knockout/humanized) engineering, not spontaneous natural disease.

---

## Summary of Key Primary Literature (PMIDs / DOIs)

| Citation | PMID / DOI | Contribution |
|---|---|---|
| Duncan CJA et al., *Sci Transl Med* 2015;7(307):307ra154 | DOI:10.1126/scitranslmed.aac4227 | Index human IFNAR2 deficiency report; fatal post-MMR encephalitis; functional reconstitution rescue |
| Hernandez N et al., *Front Genet* 2020 | PMID:33193576 | Compound heterozygous frameshift variants; HLH post-MMR; detailed STAT1/ISG/NK functional workup; corticosteroid treatment and favorable outcome |
| Bastard P et al., *J Exp Med* 2022;219(6):e20212427 | PMID:35442417 | Arctic/Inuit founder variant p.Ser53Pro; 5 patients; population allele-frequency data; life-threatening COVID-19/influenza/vaccine-associated disease |
| Seizure–Eur J Epilepsy 2022 | DOI:10.1016/j.seizure.2022.06.013 (S1059-1311(22)00175-3) | Same founder variant; post-vaccination drug-resistant infantile epileptic spasms |
| *J Clin Immunol* 2024/2025;45:30 | DOI:10.1007/s10875-024-01814-6 | Homozygous VUS; severe post-measles-vaccine reaction with viremia/meningoencephalitis/multi-organ failure; literature review |
| Smieszek SP et al., *EBioMedicine*/PMC8279933, 2021 | PMID:34273592 | Rare/common LOF *IFNAR2* variant burden association with severe COVID-19 |
| Rodrigues Prestes TR et al. (or similar), *Front Immunol* 2022 | PMID:35967349 | Common *IFNAR2* variants and soluble IFNAR2 levels associated with COVID-19 mortality |
| Bastard P et al. (yellow fever vaccine cohort) | (French National Reference Center series; JEM-adjacent) | IFNAR1/IFNAR2 deficiency and anti-IFN autoantibodies together account for >half of life-threatening yellow-fever-vaccine-associated disease |

**Note on curation caveats:** OMIM phenotype MIM numbering for IMD45 should be independently confirmed directly at omim.org (this session's OMIM WebFetch calls failed due to a proxy connectivity error, so identifiers above rely on secondary-source search snippets and carry residual uncertainty — particularly the #614889 vs. #616669 MIM number discrepancy, which must be resolved against the primary OMIM record before being written into a knowledge-base entry). Similarly, several PMIDs above (e.g., for the Rockefeller *J Exp Med* Arctic paper, PMC9026249) were resolved via secondary aggregator search snippets rather than direct primary-source fetch; both should be verified against PubMed/PMC directly during KB curation, per this repository's evidence-verification workflow (`just fetch-reference`, `just validate-kb-references`).

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 13 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:35442417`: "Autosomal recessive deficiency of the IFNAR2 chain of the human type I IFN receptor abolishes cellular responses to IFN-α, -β, and -ω, underlies severe viral diseases, and is globally very rare, except for IFNAR2 deficiency in the Arctic."
  - closest text in source: "Patients with autosomal recessive (AR) deficiency of IFNAR2 and subsequently IFNAR1 were first recognized by their susceptibility to severe viral diseases precipitated by the exposure to live-attenuated viral vaccines (LAV)—specifically, the measles, mumps, and rubella (MMR) and yellow fever vaccines (Bastard et al., 2021b; Duncan et al., 2015; Gothe et al., 2020; Hernandez et al., 2019; Passarelli et al., 2020)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 28 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025143` (2 mentions) - the report calls it "Lethargy"; HP calls it **Chills**
- `HP:0025047` (1 mention) - the report calls it "Maculopapular rash"; HP calls it **Abnormal brain choline level by MRS**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002264` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002383` (1 mention) - the report calls it "Encephalitis"; HP calls it **Infectious encephalitis**
- `HP:0002718` (1 mention) - the report calls it "Recurrent infections"; HP calls it **Recurrent bacterial infections**, and lists "Recurrent pyogenic infections" among its other names
- `HP:0004429` (1 mention) - the report calls it "susceptibility to viral infections, if available in HPO"; HP calls it **Recurrent viral infections**
- `HP:0011024` (1 mention) - the report calls it "Abnormality of the gastrointestinal system"; HP calls it **Abnormality of the gastrointestinal tract**
- `HP:0011893` (1 mention) - the report calls it "Abnormal leukocyte count / cytopenias"; HP calls it **Abnormal leukocyte count**
- `GO:0005783` (1 mention) - the report calls it "endoplasmic reticulum, for the trafficking-defective mutant"; GO calls it **endoplasmic reticulum**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:1098243` - called "Ifnar2", "Orthology:** Mouse ortholog *Ifnar2"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.