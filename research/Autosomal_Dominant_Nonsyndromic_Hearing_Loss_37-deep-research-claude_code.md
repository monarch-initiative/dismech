---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T01:47:53.739057'
end_time: '2026-09-04T01:53:36.341076'
duration_seconds: 342.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 37
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
  web_search_requests: 13
  num_turns: 27
  total_cost_usd: 1.3141330000000002
  session_id: 1d4c83ee-98b8-54c2-892b-3815ba752722
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 18
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 9
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 24
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0001846
    reported_labels:
    - confirm
    ontology_label: internal ear
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 37
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 37** covering all of the
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

I now have sufficient primary literature. Let me gather a bit more on treatment/prognosis specifics and ontology term candidates before compiling.

# Autosomal Dominant Nonsyndromic Hearing Loss 37 (DFNA37) — Research Report

## 1. Disease Information

**Overview.** DFNA37 (Deafness, Autosomal Dominant 37) is a rare form of autosomal dominant nonsyndromic sensorineural hearing loss (ADNSHL) caused by heterozygous, predominantly splice-altering variants in **COL11A1** (collagen type XI alpha 1 chain), mapping to the DFNA37 locus on chromosome **1p21.1**. It was first described in 2018 by Booth et al. in a four‑generation family of European descent, who identified a canonical splice‑acceptor variant (c.652‑2A>C) that causes exon 5 skipping ([Booth et al. 2019, *Genet Med*, PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/)). This discovery was notable because COL11A1 had previously been associated only with syndromic conditions (Stickler syndrome type II/STL2, Marshall syndrome, fibrochondrogenesis type 1), so DFNA37 **expanded the COL11A1 phenotypic spectrum to include isolated, nonsyndromic deafness** — i.e., hearing loss without the skeletal, craniofacial, or ocular features of Stickler/Marshall syndrome.

Since then, additional families/cases have been reported with different COL11A1 variants and a broader phenotypic range extending to prelingual-onset hearing loss (Rad et al. 2021, *Hum Mutat*, PMID:33169910; Ciorba et al. 2021, *J Int Adv Otol*, PMID:33605226).

**Key identifiers:**
- **OMIM:** #618533 — DEAFNESS, AUTOSOMAL DOMINANT 37; DFNA37 (phenotype); gene entry COL11A1 *120280 ([omim.org/entry/618533](https://www.omim.org/entry/618533))
- **MONDO:** MONDO:0032802 — hearing loss, autosomal dominant 37 ([monarchinitiative.org](https://beta.monarchinitiative.org/MONDO:0032802))
- **MedGen:** C4760307 (UID 1676950) ([ncbi.nlm.nih.gov/medgen/C4760307](https://www.ncbi.nlm.nih.gov/medgen/C4760307))
- **Gene:** COL11A1, HGNC:2186, chromosome 1p21.1
- **Orphanet:** DFNA-type nonsyndromic hearing loss entries generally cross-reference COL11A1-related deafness under the broader "Autosomal dominant nonsyndromic sensorineural hearing loss" grouping (specific ORPHA code for DFNA37 not separately confirmed in this search)
- **ICD-10/11:** No disease-specific code; would fall under H90.5 (sensorineural hearing loss, unspecified) at the ICD-10 level since ICD does not code individual DFNA loci
- **Synonyms:** DFNA37; Deafness, Autosomal Dominant 37; Hearing loss, autosomal dominant 37; ADNSHL-COL11A1

**Data source type:** Information is derived from **aggregated disease-level resources** (OMIM, MedGen, MalaCards, Monarch/MONDO) and from a small number of **published family/cohort case series** (individual pedigrees with segregation analysis) rather than large-scale EHR data — consistent with the rarity of this specific locus.

Sources: [OMIM #618533](https://www.omim.org/entry/618533) · [MedGen C4760307](https://www.ncbi.nlm.nih.gov/medgen/C4760307) · [MalaCards DFNA37](https://www.malacards.org/card/deafness_autosomal_dominant_37) · [PMC6431578 (Booth 2019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/)

---

## 2. Etiology

### Disease Causal Factors
DFNA37 is a **monogenic, purely genetic** disorder. There is no known infectious, autoimmune, or acquired etiology; all reported cases result from a heterozygous pathogenic/likely pathogenic variant in **COL11A1**.

### Genetic Risk Factors
- **Causal variant (index family):** c.652‑2A>C (NM_080629.2; genomic chr1:103,496,802 T>G), a canonical splice‑acceptor variant in intron 4, novel and absent from population databases (1000 Genomes, ExAC, gnomAD) at the time of publication, segregating with hearing loss across 48 genotyped members of a 4‑generation family (PMID:30245514).
- **Additional causal variants (subsequent reports):**
  - **c.652‑1G>C** — a different substitution at the *same* intron 4 canonical acceptor splice site as the index family, but producing a distinct splicing outcome, identified in a German family with **prelingual** ADNSHL (Rad et al. 2021, *Hum Mutat* 42:25‑30, PMID:33169910).
  - **c.4338+2T>C** — a splice-donor variant identified as a **de novo** occurrence in a second German family/individual, also prelingual ADNSHL (same study, PMID:33169910).
  - A **novel missense variant** in COL11A1 reported in a 6‑year‑old boy with bilateral moderate‑to‑severe down‑sloping sensorineural hearing loss (Ciorba et al. 2021, *J Int Adv Otol*, PMID:33605226) — described as the "third worldwide case" of DFNA37‑type nonsyndromic hearing loss.
- **Genomic location/mapping:** Genome‑wide linkage analysis in the original family localized the locus to chromosome 1p21 with a LOD score of 8.29; SNP‑chip fine mapping narrowed the interval to 8.4 Mb between markers rs724480 and rs6667402 (PMID:30245514).
- **Zygosity/mode:** All reported pathogenic DFNA37 variants are **heterozygous**, consistent with autosomal dominant inheritance and haploinsufficiency/dominant-negative mechanisms typical of collagen disorders.
- **Susceptibility/modifier loci:** None reported specific to DFNA37; the broader ADNSHL literature notes that presbycusis-associated aging effects are corrected for statistically (ISO 7029 norms) in progression analyses but are not themselves genetic risk factors for this condition.

### Environmental Risk Factors
No environmental, occupational, or lifestyle risk factors have been reported as causal or contributory for DFNA37 specifically; the discovery family had no history of noise exposure, ototoxic drug use, or infection implicated in the phenotype (PMID:30245514). As with any progressive SNHL, ordinary age-related and noise-related hearing decline may be superimposed but is not part of the disease definition, and studies specifically correct audiometric data for presbycusis to isolate the genetic effect.

### Protective Factors
None reported. No protective genetic variants or environmental protective factors are described in the literature for COL11A1-related DFNA37.

### Gene-Environment Interactions
Not established. Because this is a rare monogenic disorder with a clear autosomal dominant Mendelian pattern, gene-environment interaction has not been a focus of study; the DFNA37 literature treats progression as intrinsic to the collagen defect, with correction for age/presbycusis rather than modeling of external exposures.

Sources: [PMID:30245514 / PMC6431578](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [PMID:33169910 (Rad et al. 2021)](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24136) · [PMID:33605226 (Ciorba et al. 2021)](https://www.advancedotology.org/index.php/pub/article/view/1376)

---

## 3. Phenotypes

### Primary phenotype: Sensorineural hearing loss
- **Type:** Clinical sign / audiometric abnormality (laboratory-style objective measurement via pure-tone audiometry)
- **Suggested HPO term:** HP:0000407 (Sensorineural hearing impairment) as the general term; more specifically **HP:0008619 (Bilateral sensorineural hearing impairment)** and **HP:0000505/HP:0008780** family terms for progressive forms; **HP:0000408 (Progressive sensorineural hearing impairment; also indexed as HP:0001730/related concept "Progressive sensorineural hearing impairment," MedGen C1843156)**

**Onset:**
- The **index (Booth 2019) family** showed a **postlingual**, early‑onset presentation, with a measurable **congenital component of 12–23 dB** (i.e., mild threshold elevation present from birth/early childhood even before clear progression is documented) (PMID:30245514).
- Subsequent families (Rad et al. 2021) demonstrate **prelingual onset** with variants at the same (c.652‑1G>C) or a different (c.4338+2T>C) splice site, indicating **clinical/genotypic heterogeneity** — DFNA37 spans a spectrum from prelingual to postlingual onset depending on variant and splicing efficiency (PMID:33169910).
- Ciorba et al. (2021) described a young child (age 6) already manifesting moderate-to-severe loss, again consistent with early/prelingual onset in some variant carriers (PMID:33605226).

**Severity and progression:**
- Original family: **mild-to-moderate** bilateral sensorineural hearing loss.
- Annual threshold deterioration (ATD) ranged **0.2–0.8 dB/year**, with statistically significant progression at **5 of 7 tested frequencies** (0.25, 0.5, 1, 4, and 8 kHz); progression at 2 kHz was significantly slower than at other frequencies (PMID:30245514).
- Ciorba et al. case: **moderate-to-severe**, down-sloping configuration (PMID:33605226) — indicating that phenotypic severity varies by variant, consistent with a genotype-splicing-efficiency relationship proposed by Booth et al. (the c.652‑2A>C variant behaves as a "leaky" splice site, allowing some normally spliced transcript and correlating with milder/variable severity).

**Audiogram configuration:**
- **U‑shaped (mid‑frequency)** pattern in younger affected individuals, evolving to **flat or gently downsloping** by ~40 years of age (PMID:30245514). This mid-frequency pattern resembles that seen in other DFNA loci affecting the tectorial membrane, specifically **DFNA8/12 (TECTA)** and **DFNA13 (COL11A2)**.

**Frequency among affected individuals:** As an autosomal dominant Mendelian trait with apparent high/complete penetrance, essentially all heterozygous carriers in reported pedigrees manifest hearing loss (48/48 genotyped carriers in the index family showed segregation with phenotype), though exact numeric penetrance was not formally calculated (PMID:30245514).

**Absence of syndromic features:** A key negative/differentiating finding — affected individuals had **normal craniofacial features**, **normal long bones on radiograph**, and **no ocular abnormalities or cleft palate**, distinguishing DFNA37 from Stickler syndrome type II and Marshall syndrome, both of which are caused by other classes of COL11A1 mutation (PMID:30245514).

**Quality of life impact:** Not specifically quantified in the primary literature (no EQ-5D/SF-36 data identified for DFNA37 specifically); as with other progressive mild-to-moderate ADNSHL, expected impacts include difficulty with speech discrimination in noise, potential need for hearing aids, and educational/social impact if onset is prelingual, but disease-specific QOL instrument data were not found in this search.

**Suggested HPO terms:**
- HP:0000407 — Sensorineural hearing impairment
- HP:0008619 — Bilateral sensorineural hearing impairment
- HP:0000408 / progressive-hearing-impairment concept (MedGen C1843156) — Progressive sensorineural hearing impairment
- Consider a mid-frequency/U-shaped audiogram qualifier if a dedicated HPO term for "cookie-bite"/U-shaped audiogram configuration is used elsewhere in the KB (as for TECTA/COL11A2 entries) — note: exact HPO CURIE for "U-shaped audiogram" was not independently verified in this search and should be confirmed against the local HPO cache before binding.

Sources: [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [PMID:33169910](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24136) · [PMID:33605226](https://www.advancedotology.org/index.php/pub/article/view/1376) · [MedGen C1843156 (Progressive sensorineural hearing impairment)](https://www.ncbi.nlm.nih.gov/medgen/335894)

---

## 4. Genetic/Molecular Information

**Causal gene:** COL11A1 (Collagen Type XI Alpha 1 Chain), HGNC:2186, OMIM *120280, chromosome 1p21.1.

**Pathogenic variants identified (DFNA37):**

| Variant (NM_080629.2 or NM_001854) | Type | Consequence | Family/Report |
|---|---|---|---|
| c.652‑2A>C | Splice acceptor (intron 4) | Exon 5 skipping; in-frame deletion of residues 218–260 in N-propeptide | Booth et al. 2019, PMID:30245514 |
| c.652‑1G>C | Splice acceptor (intron 4, same site, different substitution) | Distinct splicing outcome from c.652-2A>C | Rad et al. 2021, PMID:33169910 |
| c.4338+2T>C | Splice donor | De novo; prelingual ADNSHL | Rad et al. 2021, PMID:33169910 |
| Novel missense variant (exact HGVS not resolved in this search) | Missense | Moderate-to-severe, down-sloping SNHL, age 6 | Ciorba et al. 2021, PMID:33605226 |

**Variant classification:** The c.652‑2A>C variant is classified as pathogenic based on: absence from population databases, high conservation, segregation with disease across 48 family members, and functional confirmation of aberrant splicing by minigene assay (PMID:30245514). ClinVar records this variant under accession **RCV000824676**, cross-referenced to **rs747787770**.

**Functional consequence:** In vitro minigene splicing assays (wild-type and mutant exon 5 + ~120 bp flanking intronic sequence cloned into pET01, transfected into COS7 and HEK293 cells) confirmed that c.652‑2A>C causes **exon 5 skipping**, producing a transcript encoding a protein lacking residues 218–260 of the **N-terminal propeptide domain**. The authors propose this is a **"leaky" splice site** — it reduces but does not abolish normal splicing, allowing partial expression of correctly spliced transcript, which may explain phenotypic variability among carriers (PMID:30245514). This is consistent with a **haploinsufficiency/partial loss-of-function** mechanism rather than a classic dominant-negative structural collagen defect (contrast with glycine-substitution COL11A1 variants causing Stickler/Marshall syndromes, which act via a dominant-negative triple-helix disruption mechanism).

**Protein domain affected:** The N-propeptide domain (encoded partly by exon 5) regulates fibril diameter/shape during collagen assembly. Loss of residues 218–260 may disrupt (a) a heparan sulfate–binding motif (residues ~147–152) and (b) critical cysteine residues at positions 236 and 243, potentially impairing propeptide folding or fibril-regulatory function (PMID:30245514).

**Allele frequency:** Not present in 1000 Genomes, ExAC, or gnomAD at time of publication (PMID:30245514) — consistent with a rare, family-specific, highly penetrant dominant variant rather than a common susceptibility allele.

**Somatic vs. germline:** All reported variants are **germline**; the c.4338+2T>C variant in the Rad et al. 2021 report arose **de novo**.

**Modifier genes:** None specifically established for DFNA37.

**Epigenetic information:** No epigenetic (DNA methylation/histone) mechanism has been reported for DFNA37; the disease mechanism is a cis-acting splice-site defect at the DNA/pre-mRNA level.

**Chromosomal abnormalities:** None — DFNA37 is caused by point/single-nucleotide splice-site or missense variants, not by large structural rearrangements, aneuploidy, or copy-number changes.

**Suggested gene/protein ontology terms:**
- Gene: hgnc:2186 (COL11A1)
- GO Molecular Function: extracellular matrix structural constituent (GO:0005201)
- GO Biological Process: **collagen fibril organization (GO:0030199)** — "any process that determines the size and arrangement of collagen fibrils within an extracellular matrix"; also **extracellular matrix organization (GO:0030198)**
- GO Cellular Component: collagen type XI trimer / extracellular matrix (specific GO CC term for type XI collagen trimer should be confirmed against local cache, e.g., GO:0005584 collagen type I trimer analog structure — the precise type XI equivalent should be validated via OAK before curation)

Sources: [OMIM *120280 COL11A1](https://omim.org/entry/120280) · [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [PMID:33169910](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24136) · [ClinVar VCV/RCV000824676](https://www.ncbi.nlm.nih.gov/clinvar/variation/39776/)

---

## 5. Environmental Information

No environmental factors (toxins, radiation, occupational exposures), lifestyle factors, or infectious agents have been implicated as causal or contributory to DFNA37 in the literature reviewed. This is a purely monogenic, autosomal dominant collagenopathy affecting the inner ear extracellular matrix. As is standard in ADNSHL natural-history studies, audiometric progression is statistically corrected for **age-related presbycusis** (using ISO 7029 norms) to isolate the genetic contribution, but presbycusis itself is not considered part of the DFNA37 disease mechanism (PMID:30245514).

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from molecular lesion to clinical manifestation)

1. A heterozygous splice-site variant in COL11A1 (e.g., c.652‑2A>C at the intron 4 canonical acceptor site) **disrupts normal pre-mRNA splicing**, acting as a "leaky" (partially functional) splice site (PMID:30245514).
2. This **leads to** skipping of exon 5 in a fraction of COL11A1 transcripts, **producing** an in-frame deletion of residues 218–260 within the **N-terminal propeptide domain** of the pro-α1(XI) collagen chain, alongside continued expression of some normally spliced (wild-type) transcript from the same allele (partial, not complete, loss of normal transcript) (PMID:30245514).
3. The truncated N-propeptide **is inferred to impair** the propeptide's normal role in regulating collagen fibril diameter/shape during assembly — potentially via loss of a heparan sulfate–binding motif and disruption of cysteine residues (236, 243) needed for correct propeptide folding — though the precise biochemical consequence on the mutant chain itself was not directly assayed at the protein level in the cited studies (inferred from domain structure-function knowledge, not demonstrated biochemically for this specific truncation) (PMID:30245514).
4. The altered pro-α1(XI) chains **assemble** (or fail to properly assemble) into **heterotrimeric type XI collagen molecules** together with normal α2(XI)/α1(XI) and other collagen partners; type XI collagen is a minor fibril-forming collagen that nucleates and regulates the diameter of type II collagen fibrils in cartilage and in specialized ECM structures such as the inner-ear tectorial membrane (PMID:30245514; GeneCards COL11A1).
5. In the cochlea, this **leads to** disorganized or abnormally regulated collagen fibrils within the **tectorial membrane (TM)** — the acellular gelatinous structure overlying the organ of Corti, which is normally anchored at its medial edge to the interdental cells of the spiral limbus and contains type II, V, IX, and XI collagens plus α- and β-tectorin (PMID:30245514; Tectorins crosslink type II collagen paper, PMC4805521).
6. Structural/mechanical compromise of the tectorial membrane **impairs** its normal biomechanical coupling to the stereocilia of outer hair cells, which is required for efficient mechanotransduction of sound-induced basilar-membrane motion into hair-cell depolarization (mechanistic inference drawn from the analogous, better-characterized COL11A2 (DFNA13) and TECTA (DFNA8/12) tectorial-membrane disorders, which the DFNA37 audiogram phenotype closely resembles) (PMID:30245514).
7. This **results in** progressive, predominantly mid-frequency sensorineural hearing loss (U-shaped/gently downsloping audiogram), reflecting frequency-place-dependent vulnerability of the tectorial membrane–hair cell interface along the cochlear spiral, with a congenital baseline threshold elevation plus slow further deterioration (0.2–0.8 dB/year) over subsequent decades (PMID:30245514).
8. **Branch point — variant-dependent severity:** Different COL11A1 splice/missense variants (c.652‑1G>C, c.4338+2T>C, and missense changes) produce differing splicing efficiencies and residual normal-transcript ratios, which is proposed to **explain** the clinical spectrum from prelingual (more severe, e.g., de novo c.4338+2T>C) to postlingual/adult-progressive (milder, "leaky" c.652‑2A>C) presentations observed across families (PMID:33169910; PMID:30245514) — this branching is **inferred from correlating variant class with reported onset age across published families**, not from a single mechanistic dose-response experiment.

### Category detail

- **Molecular pathways:** Collagen fibrillogenesis / extracellular matrix (ECM) assembly pathway; no canonical signaling cascade (Wnt/MAPK/PI3K) is implicated — this is a **structural ECM protein disorder**, not a signaling disorder. KEGG/Reactome pathway: "Collagen biosynthesis and modifying enzymes" / "Collagen chain trimerization" (Reactome) are the relevant generic pathway entries for COL11A1.
- **Cellular processes:** Impaired extracellular matrix organization and collagen fibril assembly (GO:0030199) in the tectorial membrane; no reported apoptosis, autophagy, or cell-cycle dysregulation in the hearing-loss (non-syndromic) presentation, in contrast to the growth-plate chondrocyte pathology seen in Stickler/Marshall syndrome caused by other COL11A1 variant classes.
- **Protein dysfunction:** Partial loss-of-function via aberrant splicing generating a truncated N-propeptide (haploinsufficiency-leaning mechanism for the leaky splice variants); missense variants presumably act via altered propeptide structure or triple-helix assembly, though the exact functional assay data for the Ciorba et al. missense variant were not available in this search.
- **Metabolic changes:** None reported; this is a structural ECM disorder without a primary metabolic derangement.
- **Immune system involvement:** None reported.
- **Tissue damage mechanisms:** Disorganization of collagen fibrils within the tectorial membrane ECM (mechanical/structural derangement) rather than oxidative stress, ischemia, fibrosis, or necrosis.
- **Biochemical abnormalities:** Defective N-propeptide processing/heparan-sulfate-binding-motif disruption affecting collagen fibril diameter regulation (inferred; not directly biochemically demonstrated in the cited human studies).
- **Epigenetic changes:** None reported.
- **Molecular profiling:** No transcriptomic, proteomic, metabolomic, or single-cell/spatial data specific to human DFNA37 inner-ear tissue were identified (human temporal bone/cochlear tissue is inherently difficult to sample); mouse cochlear expression data exist (see Model Organisms, section 15) showing Col11a1/Col11a2 mRNA localized to the **greater epithelial ridge**, the primary source of tectorial membrane collagen mRNA during development (McGuirt et al., PMID:15141750).

**Suggested GO/CL terms for this mechanism:**
- GO:0030199 — collagen fibril organization
- GO:0030198 — extracellular matrix organization
- CL term for interdental cells of the spiral limbus (specific CL CURIE should be validated via OAK before binding)
- CL:0000601 (auditory hair cell) / CL:0000855 (sensory hair cell) as the downstream mechanotransduction cell type affected indirectly

Sources: [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [PMID:33169910](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24136) · [Tectorins crosslink type II collagen fibrils, PMC4805521](https://pmc.ncbi.nlm.nih.gov/articles/PMC4805521/) · [McGuirt et al. PMID:15141750](https://pubmed.ncbi.nlm.nih.gov/15141750/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Inner ear (cochlea) — specifically the auditory sensory apparatus.
- No secondary organ involvement is reported in the nonsyndromic DFNA37 phenotype (distinguishing it from the syndromic COL11A1 disorders, which also affect the skeletal system, eyes, and craniofacial structures).
- **Body system:** Auditory/sensory system only, in the nonsyndromic form.

**Tissue and cell level:**
- **Tectorial membrane** — the primary structurally affected tissue; an acellular, collagen (types II, V, IX, XI)- and tectorin-rich extracellular matrix structure overlying the organ of Corti.
- **Interdental cells** of the spiral limbus / greater epithelial ridge — the source of Col11a1/Col11a2 mRNA and the anchoring point of the tectorial membrane medially.
- **Organ of Corti** (sensory epithelium), including outer and inner hair cells, indirectly affected via loss of normal mechanical coupling to the tectorial membrane.
- Suggested Cell Ontology terms: interdental cell (CL term to be confirmed), auditory hair cell (CL:0000601), outer hair cell of Corti's organ (CL:0000598 if applicable — confirm CURIE), inner hair cell of Corti's organ (CL:0000589 if applicable — confirm CURIE).

**Subcellular level:**
- Extracellular (matrix) localization — type XI collagen is a secreted, extracellular structural protein; relevant GO Cellular Component terms include the collagen fibril / extracellular matrix compartment rather than an intracellular organelle (no mitochondrial, nuclear, ER, or lysosomal primary pathology reported).

**Localization:**
- Suggested UBERON terms: tectorial membrane (UBERON term to be confirmed against local cache), cochlea (UBERON:0001844), organ of Corti (UBERON:0001846 — confirm), spiral limbus (UBERON term to be confirmed).
- **Laterality:** Bilateral in all reported cases (PMID:30245514; PMID:33605226).

Sources: [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [PMC4805521 (tectorins/collagen)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4805521/)

---

## 8. Temporal Development

**Onset:**
- Variable across reported families/variants: **congenital/prelingual** in some (Rad et al. 2021, de novo c.4338+2T>C and c.652‑1G>C families; Ciorba et al. 2021, age-6 case) versus **early-onset postlingual** in the index family (c.652‑2A>C), which showed a measurable congenital threshold elevation (12–23 dB) with subsequent slow progression (PMID:30245514; PMID:33169910).
- **Onset pattern:** Insidious/gradual rather than acute or episodic.

**Progression:**
- **Chronic, slowly progressive** sensorineural hearing loss.
- Annual threshold deterioration of **0.2–0.8 dB/year**, statistically significant at 5 of 7 tested frequencies (0.25–1, 4, 8 kHz), with the 2 kHz frequency progressing significantly more slowly than others (PMID:30245514).
- Audiogram configuration evolves over time: **U-shaped/mid-frequency pattern up to ~40 years**, becoming **flat or gently downsloping** with advancing age (PMID:30245514).
- **Course pattern:** Progressive, not relapsing-remitting or episodic; lifelong/chronic — no spontaneous remission reported.

**Patterns:**
- No remission (spontaneous or treatment-induced) has been documented; this is a structural, progressive disorder.
- No specific "critical period" or intervention window is defined in the literature beyond the general principle (applicable to all pediatric SNHL) that early identification and habilitation during the critical language-acquisition period is important when onset is prelingual.

Sources: [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [PMID:33169910](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24136)

---

## 9. Inheritance and Population

**Epidemiology:**
- DFNA37 is an **extremely rare** cause of ADNSHL; as of this search, it has been reported in only a handful of families/individuals worldwide (the original 4-generation family, two German families from Rad et al. 2021, and at least one additional case from Ciorba et al. 2021, described by its authors as the "third worldwide case"). No population-level prevalence or incidence estimate specific to DFNA37 was identified.
- For context: **ADNSHL as a category** accounts for roughly **~20% of hereditary nonsyndromic hearing loss cases** (with autosomal recessive forms being more common overall), and **more than 60 genes** have been implicated across all DFNA loci — COL11A1/DFNA37 is one of these many genes, and its specific contribution to the overall ADNSHL mutation spectrum was not quantified in the sources found.

**Inheritance pattern:** **Autosomal dominant**, confirmed by multi-generation segregation analysis (48 genotyped members of the index family) and by occurrence of de novo variants in at least one additional family (PMID:30245514; PMID:33169910).

**Penetrance:** Appears **high/complete** in reported families — all genotyped heterozygous carriers manifested hearing loss in the index pedigree — though no formal penetrance percentage was calculated or published.

**Expressivity:** **Variable**, both within and across families/variants — ranging from prelingual moderate-to-severe loss (de novo c.4338+2T>C; missense case) to early-onset mild postlingual loss with slow progression (c.652‑2A>C). The authors propose that differential splicing efficiency ("leaky" vs. more complete exon skipping) underlies this variable expressivity (PMID:30245514; PMID:33169910).

**Genetic anticipation:** Not reported/not applicable — DFNA37 variants are point/splice-site mutations, not repeat expansions, so anticipation is not expected and was not described.

**Germline mosaicism:** Not specifically reported for DFNA37, though the occurrence of a de novo variant (c.4338+2T>C) in one family raises the general possibility of parental germline mosaicism in future genetic counseling discussions (not directly documented as observed in these reports).

**Founder effects:** Not established; each family reported to date carries a distinct or at least separately ascertained variant (only the c.652‑2A>C/c.652‑1G>C pair share the exact same nucleotide position but differ in substitution and splicing outcome), arguing against a single founder mutation and more consistent with private/recurrent mutations at a mutation-prone splice site.

**Consanguinity:** Not reported as relevant (autosomal dominant, not recessive, disorder).

**Carrier frequency:** Not applicable in the classic AR sense; as a rare AD disorder, "carrier" frequency equates to allele frequency, which is effectively private/family-specific and absent from large population databases (gnomAD, 1000 Genomes, ExAC) for the reported variants (PMID:30245514).

**Population demographics:**
- Reported families are of **European descent** (index family) and **German** ancestry (Rad et al. 2021 families); the Ciorba et al. case's ancestry was not specified in available search results.
- No specific ethnic enrichment, geographic endemicity, or sex-ratio skew has been reported; hearing loss affected both sexes in the pedigrees described (consistent with autosomal, non-sex-linked inheritance).
- Age distribution: affected individuals identified from childhood (age 6 in Ciorba et al.) through multiple adult generations in the original pedigree.

Sources: [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [PMID:33169910](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24136) · [PMID:33605226](https://www.advancedotology.org/index.php/pub/article/view/1376) · general ADNSHL prevalence figures per MedlinePlus Genetics, Nonsyndromic hearing loss overview

---

## 10. Diagnostics

**Clinical tests:**
- **Pure-tone audiometry** across 0.25–8 kHz is the primary diagnostic/monitoring tool; serial audiograms are used to document progression and configuration (U-shaped/mid-frequency evolving to flat or downsloping) (PMID:30245514).
- **Age-related typical audiograms (ARTA)** were constructed and thresholds corrected for predicted presbycusis using **ISO 7029** norms to isolate genetic progression from normal aging (PMID:30245514).
- No disease-specific biomarker, imaging, or biopsy finding has been reported — temporal bone imaging (CT/MRI) was not highlighted as diagnostically distinctive in the sources reviewed, consistent with a purely biochemical/ECM-level (not gross structural) cochlear abnormality.
- Standard audiological workup (otoscopy, tympanometry to exclude conductive component, ABR in young children) would be part of routine clinical evaluation, though not specifically detailed for DFNA37 in these sources.

**Genetic testing:**
- **Overall approach:** Because ADNSHL is genetically heterogeneous (60+ genes), the standard of care is a **multi-gene hearing-loss panel** or **exome sequencing**, as used to identify the causal variant in each of the reported DFNA37 families/cases (exome sequencing in Booth et al. 2019; presumably targeted panel/exome approaches in the subsequent case reports).
- **Whole exome sequencing (WES):** Was the method used to identify c.652‑2A>C in the index family (average 114× coverage, Agilent SureSelect Human All Exon v5, Illumina HiSeq 2000; variant calling with GATK/SAMtools; annotation against dbNSFP v2.0, 1000 Genomes, ExAC, gnomAD) (PMID:30245514).
- **Gene panels:** COL11A1 is included in comprehensive hereditary hearing loss gene panels (e.g., OtoSCOPE-type panels) alongside the 60+ other known ADNSHL genes; specific panel names were not detailed in the sources reviewed.
- **Single-gene testing:** Reasonable once a family history/audiometric phenotype (mid-frequency/U-shaped, progressive, autosomal dominant) raises specific suspicion, or for targeted segregation analysis/cascade testing once a family's causal variant is known.
- **Chromosomal microarray/karyotyping/FISH/mitochondrial DNA/repeat expansion testing:** Not applicable — DFNA37 is caused by single-nucleotide/small splice-site or missense changes, not by chromosomal rearrangements, mitochondrial variants, or repeat expansions.
- **Functional splice validation:** In vitro **minigene splicing assays** (exon-trapping) were used to confirm the pathogenicity of splice-site variants, both in the original DFNA37 paper and noted as a general approach for COL11A1/COL11A2 intronic variant interpretation in Stickler syndrome and OSMED (PMC7766184, "Exon-Trapping Assay Improves Clinical Interpretation of COL11A1 and COL11A2 Intronic Variants").

**Omics-based diagnostics:** No RNA-seq, proteomics, metabolomics, epigenomics, or liquid biopsy approach has been reported as part of DFNA37 diagnosis; minigene/exon-trapping splicing assays are the main functional confirmatory tool used.

**Clinical criteria / differential diagnosis:**
- Diagnosis rests on: (1) autosomal dominant pedigree with progressive bilateral SNHL, (2) mid-frequency/U-shaped-to-flat audiogram configuration, (3) **absence** of syndromic features (normal skeletal survey, normal ocular exam, no cleft palate) to exclude Stickler syndrome type II / Marshall syndrome, and (4) confirmatory molecular genetic testing identifying a COL11A1 variant.
- **Differential diagnosis** should include other DFNA loci producing a similar mid-frequency audiogram pattern — specifically **DFNA8/12 (TECTA)** and **DFNA13 (COL11A2)** — both of which the DFNA37 audiogram closely resembles (PMID:30245514), as well as Stickler syndrome type II/Marshall syndrome (also COL11A1-caused, but syndromic) and other genes on comprehensive hearing-loss panels.

**Screening:** No disease-specific population screening program exists for DFNA37; it would be detected incidentally through standard newborn hearing screening (if prelingual) or through evaluation of progressive childhood/adult-onset hearing loss with genetic testing, followed by cascade/segregation testing of at-risk relatives in a known family.

Sources: [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [PMC7766184 (exon-trapping assay)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7766184/)

---

## 11. Outcome/Prognosis

**Survival and mortality:** DFNA37 is an isolated (nonsyndromic) sensory disorder with **no effect on survival or life expectancy** — it is not associated with mortality, and no survival/mortality data are relevant or reported.

**Morbidity and function:**
- Primary morbidity is **auditory**: progressive, bilateral hearing impairment ranging from mild to moderate-to-severe depending on variant, with functional consequences for speech perception (particularly if prelingual onset affects language acquisition) and potential need for amplification.
- No disease-specific quality-of-life instrument data (EQ-5D, SF-36, PROMIS) were identified for DFNA37.

**Disease course / complications:** No secondary organ complications (renal, cardiac, ocular, skeletal) are reported in the nonsyndromic DFNA37 phenotype, distinguishing its prognosis favorably from the syndromic COL11A1 disorders (Stickler/Marshall syndrome), which carry additional risks of retinal detachment, myopia-related complications, and skeletal/joint disease.

**Recovery potential:** As a structural, progressive ECM disorder, spontaneous recovery is not expected; management is supportive (amplification/habilitation) rather than curative, though hearing aids can substantially restore functional hearing for the mild-to-moderate range typical of this condition.

**Prognostic factors:**
- **Variant type/splicing efficiency** appears to be the key prognostic factor identified to date: "leaky" splice variants (e.g., c.652‑2A>C) are associated with milder, later (postlingual) onset, while more complete loss-of-function or de novo variants (c.4338+2T>C) are associated with prelingual, more severe presentations (PMID:30245514; PMID:33169910).
- Age is a prognostic factor for audiogram shape (U-shaped in youth transitioning to flat/downsloping with age) but this reflects natural progression of the underlying genetic lesion rather than a modifiable factor.

**Prognostic biomarkers:** None established beyond the causal genotype itself; no circulating biomarker is used to predict DFNA37 course.

Sources: [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [PMID:33169910](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24136)

---

## 12. Treatment

No DFNA37-specific interventional trials, targeted molecular therapies, or gene therapies have been reported; management follows the **general standard of care for progressive sensorineural hearing loss**.

**Supportive and rehabilitative (mainstay of management):**
- **Hearing aids** are the primary intervention for the mild-to-moderate hearing loss typical of this condition, customized to age and severity.
  - Suggested NCIT term: NCIT:C15302 (not exact — hearing-aid-specific NCIT device term should be located via OAK; per this repo's convention, device terms are bound via `qualifiers` alongside a clinical-action `treatment_term`, e.g., NCIT:C49236 Therapeutic Procedure or a rehabilitation action term)
- **Cochlear implantation** would be considered only if/when hearing loss progresses to severe-to-profound levels (not typical for most reported DFNA37 cases, which remain mild-to-moderate, though the Ciorba et al. case reached moderate-to-severe).
  - Suggested NCIT term for the surgical action: NCIT:C15329 (Surgical Procedure), with the device concept carried via `qualifiers` (NCIT:C16830 Medical Device predicate + specific cochlear implant device term), per this repository's established convention for device-vs-action binding.
- **Aural habilitation / speech-language therapy**, particularly important if onset is prelingual, to support speech and language development.
  - Suggested NCIT term: NCIT:C159273 (Speech Therapy) or NCIT:C15302 (Physical Therapy) analog for auditory habilitation, and NCIT:C15240 (Genetic Counseling) for family counseling.
- **American Sign Language exposure/education**, offered per family preference, as part of comprehensive habilitation for hearing loss generally (per GeneReviews Genetic Hearing Loss Overview).

**Pharmacotherapy:** No drug therapy is indicated or reported; this is a structural ECM disorder without an identified pharmacological target or approved medication.

**Advanced therapeutics (gene therapy, RNA-based therapy, cell therapy):** None reported or in clinical development specifically for COL11A1-related DFNA37 in the sources reviewed. (The broader hereditary hearing loss field has emerging inner-ear gene therapy research, e.g., for OTOF-related deafness, but no COL11A1-specific program was identified.)

**Surveillance:** Regular (at least annual) audiometric monitoring is the standard recommendation for progressive hereditary SNHL generally, to track threshold changes and adjust amplification as needed (per GeneReviews Genetic Hearing Loss Overview; not DFNA37-specific but generally applicable).

**Genetic counseling:** Recommended for affected families given autosomal dominant inheritance with high penetrance — 50% recurrence risk for offspring of an affected individual; prenatal/preimplantation testing could theoretically be offered but was not specifically discussed in the DFNA37 literature reviewed.

**Experimental treatments:** No DFNA37-specific clinical trials (NCT identifiers) were identified in this search.

**Treatment outcomes:** No disease-specific response-rate or outcome data (e.g., cochlear implant performance data specific to COL11A1 genotype) were found, in contrast to some other hearing-loss genes (e.g., GJB2, TMPRSS3) where genotype-specific cochlear implant outcome data exist.

Sources: [GeneReviews Genetic Hearing Loss Overview, NBK1434](https://www.ncbi.nlm.nih.gov/books/NBK1434/) · [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/)

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense — DFNA37 is a germline genetic disorder and cannot be prevented through risk-factor modification or vaccination.

**Secondary prevention (early detection):**
- **Newborn hearing screening** (universal in many countries) would detect prelingual-onset cases (as reported for the de novo/more severe variants).
- Serial audiometric monitoring in at-risk (known carrier) family members enables early detection of postlingual-onset progression, allowing timely initiation of amplification and habilitation.

**Genetic screening:**
- **Cascade/segregation testing** of at-risk relatives once a family's causal COL11A1 variant is identified, as performed in the original 48-member pedigree (PMID:30245514).
- **Carrier/predictive testing, prenatal testing, or preimplantation genetic diagnosis (PGD)** could be offered to at-risk families given the autosomal dominant, highly penetrant inheritance pattern, though this was not specifically discussed as having been performed in the reviewed case reports.

**Risk stratification:** Family history plus genotype (specific COL11A1 variant/splicing efficiency) may help stratify expected severity/onset (prelingual vs. postlingual) for genetic counseling purposes, based on the genotype-phenotype correlation proposed by Booth et al. and Rad et al.

**Counseling:** Genetic counseling is indicated to discuss the ~50% recurrence risk to offspring, variable expressivity (severity/onset cannot be precisely predicted even within a family), and reproductive options.

**Public health / environmental / prophylaxis:** Not applicable — no environmental exposure or infectious trigger has been identified to target for public-health-level prevention, and no prophylactic medication exists.

Sources: [PMID:30245514](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/)

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring DFNA37-equivalent disease (a heterozygous COL11A1 splice-site mutation causing isolated progressive SNHL) has been specifically reported in a non-human species in the sources reviewed. However, COL11A1-related disease (in a different allelic/phenotypic form — the recessive **chondrodysplasia (cho)** mutation) is well documented in mouse (see Model Organisms, below).

**Breed:** Not applicable — no veterinary/companion-animal breed-specific COL11A1 hearing-loss disorder was identified in this search (contrast with COL11A2/DFNA13, which has better-characterized mouse models, or with other deafness genes that do have OMIA veterinary entries).

**Gene orthology:** Col11a1 is highly conserved across mammals; the mouse ortholog (Col11a1, chromosome 3) is the basis of the cho mouse model (NCBI Gene mouse Col11a1).

**Natural disease relevance:** Not established for DFNA37 specifically in companion animals or wildlife; COL11A1-related skeletal disease (chondrodysplasia) is a recognized veterinary genetics research model rather than a spontaneously occurring clinical veterinary diagnosis.

**Comparative biology / evolutionary conservation:** The cochlear expression pattern of Col11a1/Col11a2 (localized to the greater epithelial ridge/interdental cells, the developmental source of tectorial membrane collagen) is conserved between mouse and the inferred human mechanism, supporting cross-species relevance of the mouse chondrodysplasia model for understanding human COL11A1-related hearing loss mechanisms (McGuirt et al., PMID:15141750).

**Transmission:** Not applicable — DFNA37 is a non-communicable, purely genetic disorder with no zoonotic or cross-species transmission relevance.

Sources: [PMID:15141750 (McGuirt et al., Col11a1/Col11a2 cochlear expression)](https://pubmed.ncbi.nlm.nih.gov/15141750/)

---

## 15. Model Organisms

**Primary model: Mouse (*Mus musculus*), Col11a1 chondrodysplasia (*cho*) mutant**
- **Model type:** Naturally occurring/spontaneous recessive mutant mouse line (not a DFNA37-specific engineered model, but the principal model organism for Col11a1 loss-of-function in the ear).
- **Genetic basis:** The *cho* mutation is a **deletion of a cytidine residue ~570 nucleotides downstream of the translation initiation codon** in Col11a1 mRNA, mapping to mouse chromosome 3 in the syntenic region of human COL11A1 (Li et al. 1995, cited in search results).
- **Zygosity and phenotype:**
  - **Homozygous (cho/cho)** mice die perinatally from severe chondrodysplasia (skeletal/cartilage defect) but also show **underdevelopment of the organ of Corti in the lower (basal) cochlear turn** and marked hearing loss on auditory brainstem response (ABR) testing, with ultrastructural cochlear abnormalities (PubMed 1952599, "Ultrastructural changes of cochlea in mice with hereditary chondrodysplasia (cho/cho)").
  - **Heterozygous (cho/+)** mice — a viable, adult model relevant to the dominant human disease — show **auditory dysfunction associated with Col11a1 haploinsufficiency**, as specifically studied in "Auditory function associated with Col11a1 haploinsufficiency in chondrodysplasia (cho) mice" (search result identified; full PMID not resolved in this search but should be confirmed, likely McGuirt/Smith-adjacent PubMed entry from the same research group).
- **Model characteristics — phenotype recapitulation:** The cho/+ (heterozygous) mouse recapitulates the **dosage-sensitive, dominant** nature of human COL11A1-related hearing loss reasonably well, since human DFNA37 is also heterozygous and at least partly haploinsufficiency-driven (leaky splice variants). However, the cho allele is a frameshift/null-type mutation rather than the specific splice-altering or missense alleles found in human DFNA37 families, so it models **Col11a1 dosage reduction generally** rather than the precise molecular lesion (exon 5 skipping, N-propeptide truncation) described in the human disease.
- **Model limitations:** The homozygous cho/cho phenotype is grossly abnormal and perinatal-lethal (a much more severe, syndromic-like skeletal phenotype not seen in human DFNA37, which is nonsyndromic), so only the **heterozygous** state is the appropriate comparator for the human dominant, nonsyndromic disease; even then, the precise variant-specific splicing mechanism (leaky partial exon skipping) of the human DFNA37 alleles is not replicated by the cho frameshift allele.

**Complementary model: Col11a2 knockout mouse (paralogous gene, same collagen heterotrimer)**
- Both homozygous and heterozygous **Col11a2** knockout mice show hearing loss due to **disorganized collagen fibrils in the tectorial membrane**, visualized by electron microscopy — directly supporting the proposed shared tectorial-membrane collagen-organization mechanism for DFNA37 (COL11A1) and DFNA13 (COL11A2), even though this specific model targets the paralogous gene rather than COL11A1 itself.

**Applications:** These mouse models support study of (a) Col11a1/Col11a2 developmental expression in the cochlea (localized to the greater epithelial ridge, the source of tectorial membrane collagen mRNA), (b) structural consequences of collagen XI dosage/organization defects on the tectorial membrane, and (c) correlation of genotype (null vs. partial loss-of-function) with hearing phenotype severity — directly relevant to interpreting human genotype-phenotype correlations proposed for DFNA37.

**Resources:** MGI (Mouse Genome Informatics) carries the Col11a1 cho allele and associated phenotype records; IMPC/KOMP-generated conditional/humanized Col11a1 alleles were not specifically identified in this search but may exist in current mouse resource databases.

Sources: [McGuirt et al., PMID:15141750](https://pubmed.ncbi.nlm.nih.gov/15141750/) · ["Ultrastructural changes of cochlea in cho/cho mice," PMID:1952599](https://pubmed.ncbi.nlm.nih.gov/1952599/) · ["Auditory function associated with Col11a1 haploinsufficiency in chondrodysplasia (cho) mice"](https://www.researchgate.net/publication/10951553_Auditory_function_associated_with_Col11a1_haploinsufficiency_in_chondrodysplasia_cho_mice) · [OMIM *120280 COL11A1](https://omim.org/entry/120280)

---

## Summary of Evidence Gaps

- No formal population prevalence/incidence figure exists for DFNA37 specifically (only a handful of reported families/individuals worldwide as of the literature identified).
- No DFNA37-specific quality-of-life data, cochlear implant outcome data, or clinical trial (NCT) exists.
- The exact biochemical/protein-level consequence of the truncated N-propeptide (heparan-sulfate binding, cysteine disruption) is inferred from domain structure-function reasoning in the primary paper, not directly demonstrated by protein-level functional assay.
- The heterozygous cho/+ mouse model's precise correspondence to specific human DFNA37 splice alleles (rather than to Col11a1 haploinsufficiency in general) has not been directly tested.
- Exact HPO CURIEs for "U-shaped/mid-frequency audiogram" and precise UBERON/CL CURIEs for tectorial membrane, interdental cells, and spiral limbus should be confirmed via OAK lookup before binding in the knowledge base, as this research pass relied on web search/fetch rather than direct ontology queries.

---

## Full Source List

- [OMIM #618533 — DEAFNESS, AUTOSOMAL DOMINANT 37; DFNA37](https://www.omim.org/entry/618533)
- [OMIM *120280 — COLLAGEN, TYPE XI, ALPHA-1; COL11A1](https://omim.org/entry/120280)
- [MedGen C4760307 — Hearing loss, autosomal dominant 37](https://www.ncbi.nlm.nih.gov/medgen/C4760307)
- [MalaCards — Deafness, Autosomal Dominant 37 (DFNA37)](https://www.malacards.org/card/deafness_autosomal_dominant_37)
- [Monarch Initiative — MONDO:0032802](https://beta.monarchinitiative.org/MONDO:0032802)
- Booth KT, Askew JW, Talebizadeh Z, et al. "Splice-altering variant in COL11A1 as a cause of nonsyndromic hearing loss DFNA37." *Genet Med.* 2019;21(4):948–954. PMID:30245514. [PMC6431578](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431578/) · [Nature/GIM](https://www.nature.com/articles/s41436-018-0285-0)
- Rad A, Schade-Mann T, Gamerdinger P, et al. "Aberrant COL11A1 splicing causes prelingual autosomal dominant nonsyndromic hearing loss in the DFNA37 locus." *Hum Mutat.* 2021;42(1):25–30. PMID:33169910. [Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24136)
- Ciorba A, et al. "Non-Syndromic Sensorineural Prelingual and Postlingual Hearing Loss due to COL11A1 Gene Mutation." *J Int Adv Otol.* 2021. PMID:33605226. [Journal site](https://www.advancedotology.org/index.php/pub/article/view/1376)
- McGuirt WT, et al. "Col11a1 and Col11a2 mRNA expression in the developing mouse cochlea: implications for the correlation of hearing loss phenotype with mutant type XI collagen genotype." PMID:15141750.
- "Ultrastructural changes of cochlea in mice with hereditary chondrodysplasia (cho/cho)." PMID:1952599.
- "Auditory function associated with Col11a1 haploinsufficiency in chondrodysplasia (cho) mice." [ResearchGate](https://www.researchgate.net/publication/10951553_Auditory_function_associated_with_Col11a1_haploinsufficiency_in_chondrodysplasia_cho_mice)
- "Tectorins crosslink type II collagen fibrils and connect the tectorial membrane to the spiral limbus." [PMC4805521](https://pmc.ncbi.nlm.nih.gov/articles/PMC4805521/)
- ClinVar VCV000039776 (c.652‑2A>C). [ncbi.nlm.nih.gov/clinvar/variation/39776](https://www.ncbi.nlm.nih.gov/clinvar/variation/39776/)
- GeneReviews — Genetic Hearing Loss Overview. [NBK1434](https://www.ncbi.nlm.nih.gov/books/NBK1434/)
- GO:0030199 — collagen fibril organization. [AmiGO](https://amigo.geneontology.org/amigo/term/GO:0030199)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001846` (1 mention) - the report calls it "confirm"; UBERON calls it **internal ear**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005201` (1 mention) - the report calls it "GO Molecular Function: extracellular matrix structural constituent"; GO calls it **extracellular matrix structural constituent**
- `GO:0030199` (6 mentions) - the report calls it "GO Biological Process: **collagen fibril organization", "collagen fibril organization"; GO calls it **collagen fibril organization**
- `CL:0000601` (2 mentions) - the report calls it "auditory hair cell"; CL calls it **cochlear outer hair cell**
- `NCIT:C159273` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Speech Language Therapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0030199` - called "GO Biological Process: **collagen fibril organization", "collagen fibril organization"