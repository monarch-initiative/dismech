---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T20:11:53.360204'
end_time: '2026-10-14T20:13:13.428450'
duration_seconds: 80.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Primary Ciliary Dyskinesia 3
  mondo_id: MONDO:0012085
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 1
  num_turns: 13
  total_cost_usd: 0.7830870999999999
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 3
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 2
  validator_version: 0.3.0
term_validation:
  total_terms: 3
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012085
    reported_labels:
    - verified in the repo
    ontology_label: primary ciliary dyskinesia 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Ciliary Dyskinesia 3
- **MONDO ID:** MONDO:0012085 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Primary Ciliary Dyskinesia 3** covering all of the
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

I'll start by checking the repo for an existing entry or stub and loading the web tools to verify the gene and identifiers.

I'm pulling the cached abstracts for the key DNAH5 papers so the report's quotes are exact.

# Research report: Primary Ciliary Dyskinesia 3 (CILD3, DNAH5-related PCD)

## Verification status

Web access was limited in this session: PubMed pages were blocked, and only one search returned usable results. I checked the following against repository sources:

- **MONDO:0012085** is "primary ciliary dyskinesia 3". It is already used in `kb/disorders/Primary_Ciliary_Dyskinesia_3.yaml`.
- **The causal gene is DNAH5, `hgnc:2950`.** The ClinGen row in `kb/genes/ingest/clingen_gene_validity.tsv` reads `DNAH5 | primary ciliary dyskinesia 3 | MONDO:0012085 | AR | Definitive | 2022-01-07 | Motile Ciliopathy GCEP | CGGV:assertion_4390dba1-012d-4e08-a841-ffc08ebdc737-2022-01-07T190607.723Z`.
- **Two papers were read in `references_cache/`:** PMID:11788826 and PMID:16627867. Their quotes below are exact.
- **Search result consistent with the above:** OMIM 608644 is PCD caused by DNAH5 mutation. The DNAH5 gene entry is OMIM 603335. This came from secondary sources only, not omim.org.

Everything else is background knowledge and is marked **[unverified]**. That includes every ontology CURIE except MONDO:0012085 and hgnc:2950. Per repo policy, look each one up before binding it.

A KB entry already exists. It is a minimal stub with only the description, `disease_term` and parent. This report is intended to enrich it.

---

## 1. Disease information

**Overview.** Primary ciliary dyskinesia 3 is the PCD subtype caused by biallelic loss-of-function variants in DNAH5. DNAH5 encodes an outer dynein arm (ODA) heavy chain of motile cilia. The disease is a motile ciliopathy. It features chronic sino-pulmonary disease from impaired mucociliary clearance, randomized left-right body asymmetry, and male infertility.

**Identifiers**
- MONDO:0012085 (verified in the repo).
- OMIM 608644 (CILD3), with the DNAH5 gene entry at 603335. These are consistent across secondary sources but not checked on omim.org.
- Parent PCD phenotypic series: OMIM 242650. The Olbrich 2002 abstract (PMID:11788826) cites "PCD, MIM 242650".
- Orphanet, ICD-10/11 and MeSH IDs: not verified. The generic Kartagener syndrome / PCD terms would apply.

**Synonyms.** CILD3; ciliary dyskinesia, primary, 3; DNAH5-related PCD; Kartagener syndrome when situs inversus is present. **[unverified]**

**Data source.** This is an aggregated, disease-level description from the literature and databases, not EHR-derived.

## 2. Etiology

- **Cause:** purely genetic. Autosomal recessive biallelic DNAH5 variants. The ClinGen Motile Ciliopathy GCEP classifies the DNAH5–PCD3 relationship as Definitive (verified in the repo).
- **Genetic risk factors:** the causal variants only. Modifier genes are not established.
- **Environmental risk and protective factors:** none define the disease. Environmental exposures such as tobacco smoke and respiratory infections worsen lung disease but do not cause it.
- **Gene–environment interactions:** none established in the sources I could verify.

## 3. Phenotypes

Frequencies below are qualitative. They are from background knowledge unless a quote is given. **[unverified]** HPO CURIEs need lookup.

| Phenotype | Notes | Suggested HPO label |
|---|---|---|
| Chronic wet cough, recurrent lower respiratory infections | Neonatal or childhood onset, very frequent | Recurrent respiratory infections; Chronic productive cough |
| Neonatal respiratory distress | Often present in term infants | Neonatal respiratory distress |
| Bronchiectasis | Progressive, develops in childhood and adulthood | Bronchiectasis |
| Chronic rhinosinusitis, nasal polyps | Very frequent | Chronic sinusitis |
| Recurrent otitis media, conductive hearing loss | Childhood | Recurrent otitis media; Conductive hearing impairment |
| Situs inversus totalis | About half of patients, from randomized laterality | Situs inversus totalis |
| Heterotaxy, congenital heart disease | Minority | Heterotaxy |
| Male infertility (sperm immotility) | Frequent | Asthenozoospermia |
| Reduced female fertility; ectopic pregnancy | Occasional | — |

**Supporting quote (PMID:11788826):** "Primary ciliary dyskinesia (PCD, MIM 242650) is characterized by recurrent infections of the respiratory tract due to reduced mucociliary clearance and by sperm immobility. Half of the affected offspring have situs inversus (reversed organs), which results from randomization of left-right (LR) asymmetry."

**Quality of life:** no verified data. Chronic cough and sinus disease are the main burdens.

## 4. Genetic and molecular information

- **Gene:** DNAH5, `hgnc:2950`, chromosome 5p15.
- **Variants:** mostly loss-of-function. Hornef et al. (PMID:16627867) found in 30 families "33 novel (12 nonsense, 8 frameshift, 5 splicing, and 8 missense mutations) and two known DNAH5 mutations."
- **Hotspots:** "We observed clustering of mutations within five exons harboring 27 mutant alleles (52%) of the 52 detected mutant alleles."
- **Founder variant:** in North America, "6 (32%) of 19 PCD families with DNAH5 mutations from North America carry the novel founder mutation 10815delT."
- **Share of PCD:** "In a preselected subpopulation with documented outer dynein arm defects (n = 47), DNAH5 mutations were identified in 53% of patients." DNAH5 is commonly cited as the most frequently mutated PCD gene, at roughly 15–21% of all PCD. This figure comes from a secondary search snippet.
- **Gene identification:** Olbrich et al. 2002 (PMID:11788826) reported that "Sequence analysis in individuals with PCD with randomization of LR asymmetry identified mutations resulting in non-functional DNAH5 proteins."
- **Origin:** germline.
- **Epigenetic and chromosomal abnormalities:** none known. Large deletions and copy-number variants are described in some cases **[unverified]**.
- **Allele frequencies:** not checked in gnomAD.

## 5. Environmental information

No disease-defining environmental factors. Airway pollutants and tobacco smoke are aggravating factors. Infectious agents act as complications, not causes. Common colonizers include *Haemophilus influenzae*, *Pseudomonas aeruginosa* and nontuberculous mycobacteria **[unverified]**.

## 6. Mechanism and pathophysiology

**Causal chain**
1. Biallelic DNAH5 variants, mostly nonsense, frameshift or splice, abolish or truncate the ODA heavy chain.
2. Mutant DNAH5 is absent from the axoneme or mislocalized. Hornef et al. reported "mislocalization of mutant DNAH5 and accumulation at the microtubule organizing centers. Mutant DNAH5 was absent throughout the ciliary axoneme in seven patients."
3. Outer dynein arms fail to assemble. "Electron microscopic analyses in 22 patients with PCD with mutations invariably detected outer dynein arm ciliary defects."
4. Without ODAs, motile cilia beat abnormally or are immotile. Ciliary beat frequency is reduced and the cilia are stiff or immotile **[unverified, inferred from mechanism]**.
5. **Branch A, airway:** impaired mucociliary clearance leads to mucus retention, then recurrent infection and inflammation. This leads to bronchiectasis and chronic rhinosinusitis and otitis media. This step is inferred, not directly demonstrated in the verified papers.
6. **Branch B, embryonic node:** nodal motile cilia fail to generate leftward flow. This leads to randomized left-right asymmetry, with situs inversus in about half of cases. Olbrich et al. state this "results from randomization of left-right (LR) asymmetry."
7. **Branch C, reproductive tract:** immotile sperm flagella lead to male infertility. Dysfunctional cilia in the fallopian tube and ependyma are proposed to reduce female fertility and to cause rare hydrocephalus **[unverified]**.

**Pathway and process details**
- Axonemal dynein ATPase activity drives microtubule sliding and ciliary beat.
- Suggested GO terms, to be verified: cilium movement (`GO:0003341`), outer dynein arm (`GO:0036157`), axonemal dynein complex assembly, determination of left/right symmetry.
- Suggested CL terms, to be verified: ciliated columnar epithelial cell, respiratory epithelial cell, spermatozoon, node cell.
- Omics and immune involvement: not verified.

## 7. Anatomical structures affected

- **Primary:** lower and upper airways (trachea, bronchi, nose, paranasal sinuses), middle ear and Eustachian tube, the embryonic node (laterality), sperm flagella, and the fallopian tube.
- **Secondary:** heart and viscera (laterality defects).
- **Subcellular:** the ciliary axoneme, specifically the outer dynein arm.
- **Lateralization:** symmetric organ disease. Laterality defects are bilateral/global (situs solitus or inversus).

Suggested UBERON terms are lung, bronchus, nasal cavity, paranasal sinus, middle ear, fallopian tube, and sperm flagellum. All need lookup.

## 8. Temporal development

- **Onset:** neonatal or early childhood, often with neonatal respiratory distress and daily wet cough from infancy.
- **Course:** chronic and lifelong. Lung function declines slowly. Bronchiectasis develops with age.
- **Remission:** none.
- **Staging systems:** none established.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (ClinGen row, verified; HP term for autosomal recessive inheritance, to be looked up).
- **Penetrance:** appears complete for the respiratory phenotype. Laterality is variable (about 50% situs inversus).
- **Founder variant:** 10815delT in North American families (PMID:16627867).
- **PCD prevalence:** roughly 1 in 10,000–20,000 **[unverified]**. DNAH5-specific prevalence is not verified.
- **Consanguinity:** increases the rate of homozygous cases **[unverified]**.
- **Sex ratio:** equal for disease. Infertility is more evident in males.

## 10. Diagnostics

Confirmed from verified sources: transmission electron microscopy shows ODA defects, and immunofluorescence shows DNAH5 mislocalization or absence.

The rest is standard practice and **[unverified]**:
- Nasal nitric oxide, which is very low in PCD.
- High-speed video microscopy of ciliary beat.
- Genetic testing by PCD gene panel or exome sequencing. DNAH5 is a large gene, so full coding coverage matters.
- Chest CT for bronchiectasis and situs.
- Semen analysis and audiometry.
- Differential diagnosis: cystic fibrosis, immunodeficiency, and other motile ciliopathies.
- Screening: none by newborn screening. Situs inversus with neonatal respiratory distress should prompt PCD evaluation.

## 11. Prognosis

Survival is generally near normal with good care. Lung function declines slowly and bronchiectasis can cause respiratory failure in some patients. Transplantation is rarely needed. I have no verified quantitative survival data for the DNAH5 subtype.

## 12. Treatment

There are no approved disease-modifying drugs and no verified trial identifiers. Management is supportive and **[unverified]**:
- Airway clearance physiotherapy (NCIT supportive care or physical therapy terms).
- Prompt antibiotics for exacerbations, and sometimes prophylactic macrolide.
- Vaccination.
- ENT care, including hearing aids, with caution about tympanostomy tubes.
- Fertility support through ICSI.
- Experimental approaches include gene therapy and read-through approaches. These are not clinically established for DNAH5.

## 13. Prevention

Prevention is limited to genetic counseling, carrier testing and prenatal or preimplantation diagnosis for families with known DNAH5 variants. Tertiary prevention covers vaccination, avoiding smoke, and early treatment of infections. **[unverified]**

## 14. Other species

Naturally occurring PCD is known in dogs and other mammals. DNAH5 orthologs are conserved. I did not verify OMIA entries or breed ontology terms.

## 15. Model organisms

Mouse *Dnahc5*/*Dnah5* mutants have randomized laterality and ciliary defects **[unverified; I believe Ibañez-Tallon et al., 2002, PMID:11809718, but I could not retrieve the abstract and the paper was not in the local cache]**. Zebrafish and *Chlamydomonas* ODA models are also used. I did not verify fidelity details.

---

## Suggested next steps for curation

1. Run `just validate-terms` on every CURIE above that you decide to bind.
2. Fetch further references with `just fetch-reference`. I could not run that command in this session because of a permission prompt.
3. Curate against GeneReviews "Primary Ciliary Dyskinesia" as the baseline. Check it with `just check-genereviews`.
4. Existing PCD research files in `research/` (Falcon and Cyberian Codex PCD reports) may cover shared mechanisms.

## Sources

- Olbrich H et al. 2002, Nat Genet. PMID:11788826 (read from `references_cache/PMID_11788826.md`)
- Hornef N et al. 2006, Am J Respir Crit Care Med. PMID:16627867 (read from `references_cache/PMID_16627867.md`)
- ClinGen gene–disease validity row via `kb/genes/ingest/clingen_gene_validity.tsv`
- [DNAH5 (Wikipedia)](https://en.wikipedia.org/wiki/DNAH5)
- [Genomics England PanelApp: DNAH5, respiratory ciliopathies](https://panelapp.genomicsengland.co.uk/panels/550/gene/DNAH5)
- [NCBI Gene 1767](https://www.ncbi.nlm.nih.gov/gene/1767)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012085` (4 mentions) - the report calls it "verified in the repo"; MONDO calls it **primary ciliary dyskinesia 3**