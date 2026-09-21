---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-05T22:41:44.384871'
end_time: '2026-09-05T22:45:35.291763'
duration_seconds: 230.91
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Autosomal Recessive Spinocerebellar Ataxia 16
  mondo_id: MONDO:0014339
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
  num_turns: 25
  total_cost_usd: 1.257498
  session_id: 28a59a35-8a3c-518f-811c-4b7c8eab38f6
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 12
reference_validation:
  total_references: 14
  verified: 13
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.071
  relevance_assessed: 13
  on_topic: 12
  off_topic: 1
  off_topic_references:
  - PMID:32778825
  unresolved_references:
  - PMID:23847347
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 48
  verified: 44
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 31
  labels_matching: 19
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0014339
    reported_labels:
    - if available
    ontology_label: autosomal recessive spinocerebellar ataxia 16
  - term_id: CL:0000032
    reported_labels:
    - "cerebellar granule cell / granule neuron progenitor equivalent \u2014 verify\
      \ exact CL ID for GNP"
    ontology_label: neuroplacodal cell
  - term_id: CL:0000057
    reported_labels:
    - fibroblast, for the in vitro patient-derived model
    ontology_label: fibroblast
  - term_id: UBERON:0002140
    reported_labels:
    - cerebellar cortex
    ontology_label: parabigeminal nucleus
  - term_id: UBERON:0002020
    reported_labels:
    - "Purkinje layer \u2014 verify exact ID"
    ontology_label: gray matter
  - term_id: UBERON:0000006
    reported_labels:
    - "islet of Langerhans \u2014 only if endocrine subphenotype curated"
    ontology_label: islet of Langerhans
  - term_id: UBERON:0000959
    reported_labels:
    - spinal cord, for the subset with cord involvement
    ontology_label: optic chiasma
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0071556
    ontology_label: obsolete integral component of lumenal side of endoplasmic reticulum
      membrane
    replaced_by: GO:0098553
  - term_id: GO:0051082
    ontology_label: obsolete unfolded protein binding
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Spinocerebellar Ataxia 16
- **MONDO ID:** MONDO:0014339 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Spinocerebellar Ataxia 16** covering all of the
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

I'll research this thoroughly using web search and fetch tools to gather accurate, citable information on SCAR16 (STUB1-related ataxia).

I now have sufficient primary-literature grounding to compile the comprehensive report.

# Autosomal Recessive Spinocerebellar Ataxia 16 (SCAR16) — Research Report

## 1. Disease Information

**Overview.** Autosomal recessive spinocerebellar ataxia 16 (SCAR16) is a progressive, degenerative disorder of the cerebellum caused by biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic variants in **STUB1** (STIP1 homology and U-box-containing protein 1), which encodes **CHIP** (Carboxyl terminus of Hsc70-Interacting Protein), a dual-function co-chaperone/E3 ubiquitin ligase central to cellular protein quality control. Patients present with progressive gait and limb ataxia, dysarthria, and cerebellar atrophy on MRI, frequently accompanied by cognitive decline, hyperreflexia, and — in a subset — hypogonadotropic hypogonadism (historically overlapping with "Gordon-Holmes syndrome" when ataxia co-occurs with hypogonadism). Onset is most often in the teens to young adulthood, though infantile and later adult-onset cases are reported (Shi et al., *PLoS One* 2013, PMID:23847347; Synofzik et al., *Orphanet J Rare Dis* 2014, PMID:25258038; OMIM #615768).

**Key identifiers:**
- **OMIM:** #615768 (SCAR16; gene locus STUB1, *606614)
- **Related dominant disorder:** SCA48 (OMIM #618093) — heterozygous STUB1 variants
- **Orphanet:** ORPHA:412057 — "Autosomal recessive cerebellar ataxia due to STUB1 deficiency"
- **MONDO:** MONDO:0014339
- **Gene (HGNC):** STUB1, hgnc:17208; chromosome 16p13.3
- **Disease Ontology:** DOID:0080029
- **GARD (NIH/GARD):** 17689

**Synonyms:** SCAR16; Spinocerebellar ataxia, autosomal recessive, 16; Autosomal recessive cerebellar ataxia due to STUB1 deficiency; CHIP deficiency ataxia; historically overlapping with "Ataxia-hypogonadism syndrome"/Gordon-Holmes syndrome when hypogonadism is present.

**Data source type:** Information is derived from **aggregated disease-level resources** — case series and cohort studies pooling multiple unrelated families (Chinese, French, Dutch, Italian, and other cohorts) rather than a single large natural-history registry. The largest cohort to date (Roux et al., *Genet Med* 2020, PMID:32778825) is a multicenter ascertainment of 440 index cerebellar ataxia cases, of which 50 carried STUB1 variants (both mono- and bi-allelic).

## 2. Etiology

**Disease Causal Factors.** SCAR16 is a monogenic, purely genetic disorder: biallelic pathogenic variants in STUB1 are both necessary and sufficient to cause disease. No infectious or environmental cause is implicated in causation, though environmental/lifestyle factors may modulate symptom severity or age-related decline (see below).

**Genetic risk factors:**
- Homozygous or compound heterozygous missense, nonsense, frameshift, and splice-site variants spanning all three CHIP functional domains (TPR, coiled-coil, U-box) are pathogenic. More than 30 distinct STUB1 variants have been reported in SCAR16 (search result synthesis from PMC8497888).
- The seminal report (Shi et al. 2013, PMID:23847347) identified STUB1 mutations by linkage analysis and whole-exome sequencing in a Chinese family, then confirmed additional mutations in a cohort of 36 ataxia families and 196 sporadic ataxia patients.
- **Mutation-specific heterogeneity:** Synofzik et al. (PMID:25258038) reported a homozygous p.Asn65Ser (TPR domain) variant in three siblings with an atypical "accelerated aging" phenotype (diabetes, alopecia, uveitis, ulcerative colitis) without hypogonadism, and compound heterozygous p.Glu28Lys/p.Lys144Ter in an adult-onset patient with secondary infertility from hypogonadotropism preceding ataxia — establishing that clinical presentation depends on which CHIP domain is affected.
- Madrigal et al. (*J Biol Chem* 2019, PMID:31619515) found that U-box domain mutations, which severely impair E3 ubiquitin ligase activity, correlate strongly with cognitive dysfunction (found in ~94% of U-box-mutant cases in their cohort), while TPR/coiled-coil domain mutations (which impair HSP70/HSC70 binding) correlate with increased tendon reflex but less cognitive involvement.
- **Digenic modulation:** STUB1 variants can interact with TBP polyglutamine expansions to modulate penetrance/expressivity of SCA17/SCA48 (ScienceDirect, S1098360021011175), illustrating gene-gene interaction in the STUB1-associated ataxia spectrum.

**Environmental/lifestyle risk factors:** None specifically established as disease-causing; general supportive-care literature for ataxia (fall risk, deconditioning) applies but is not STUB1-specific.

**Protective factors:** No specific genetic or environmental protective variants/factors have been reported for STUB1-related disease in the literature reviewed.

**Gene-environment interactions:** Not established; this is a purely monogenic, fully genetically-determined recessive disorder as currently understood.

## 3. Phenotypes

Suggested HPO term bindings are given per phenotype.

| Phenotype | Type | Onset/Course | Frequency (cohort-derived) | Suggested HPO |
|---|---|---|---|---|
| Progressive gait ataxia | Sign | Teens–young adulthood typical (range: infancy to older adult); progressive | Core/universal feature | HP:0002066 (Gait ataxia) |
| Limb/appendicular ataxia, dysmetria | Sign | Progressive | Very frequent | HP:0002070 (Limb ataxia) / HP:0001310 (Dysmetria) |
| Dysarthria | Sign | Progressive | Frequent | HP:0001260 (Dysarthria) |
| Cerebellar atrophy (MRI) | Imaging finding | Present from diagnosis, progresses | Nearly universal | HP:0001272 (Cerebellar atrophy) |
| Cognitive dysfunction/decline | Behavioral/cognitive | Variable onset, progressive | ~71% in Madrigal et al. cohort (PMID:31619515); "frequent cause of predominant cognitive impairment" per Roux et al. (PMID:32778825) | HP:0001268 (Mental deterioration) / HP:0100543 (Cognitive impairment) |
| Hyperreflexia / increased tendon reflex | Sign | Present variably | ~75% (Madrigal et al.) | HP:0001347 (Hyperreflexia) |
| Hypogonadotropic hypogonadism / secondary infertility | Endocrine/lab | Can precede ataxia onset by years | ~17% (Madrigal et al.); higher in some cohorts (historic "Gordon-Holmes" overlap) | HP:0000044 (Hypogonadotropic hypogonadism) |
| Peripheral/sensory neuropathy | Sign | Variable | Reported in subset | HP:0007141 (Sensory neuropathy) |
| Nystagmus / abnormal eye movements | Sign | Variable | Reported | HP:0000639 (Nystagmus) |
| Accelerated-aging features (diabetes, alopecia, uveitis, ulcerative colitis) | Sign/lab | Reported in one TPR-domain (p.Asn65Ser) family | Rare, mutation-specific | HP:0007495 (Premature skin wrinkling) as proxy; no single HPO term for "accelerated aging" syndrome — consider HP:0000969 (edema)-type per-symptom terms individually |
| Epilepsy/seizures | Sign | Reported in some cases (Gordon-Holmes spectrum) | Uncommon | HP:0001250 (Seizure) |
| Chorea/dystonia/other movement disorder | Sign | Reported | Uncommon | HP:0002072 (Chorea) |
| Pyramidal signs (spasticity) | Sign | Reported | Subset | HP:0007256 (Progressive pyramidal tract signs) |

**Progression/severity note:** Roux et al. (PMID:32778825) explicitly report that "age at onset and severity were remarkably variable," and Madrigal et al. found that severity of ataxia (SARA score) did **not** correlate with age of onset — an atypical feature relative to many other SCAs, where earlier onset usually predicts faster/more severe course. This decoupling is attributed to domain-specific mechanistic effects (U-box vs. TPR/CC mutations) rather than a simple dose-severity relationship.

**Quality of life impact:** No disease-specific EQ-5D/SF-36 data were identified in the literature reviewed; QoL impact is inferred from the general ataxia/cognitive-decline burden and from case reports of progressive disability requiring multidisciplinary care (GARD summary).

## 4. Genetic/Molecular Information

**Causal gene:** STUB1 (HGNC:17208; OMIM *607207 — note: OMIM assigns STUB1 the number 607207 in most current records, cross-check locally), chromosome 16p13.3, encoding CHIP protein (UniProt Q9UNE7).

**Variant landscape:**
- Missense (e.g., p.Glu28Lys, p.Asn65Ser, p.Lys145Gln, p.Met211Ile, p.Ser236Thr, p.Thr246Met — characterized structurally by Heuer et al., PMID:28396517), nonsense (p.Lys144Ter), frameshift, and splice-site variants are reported across the TPR, coiled-coil, and U-box domains.
- **ClinVar** entries include NM_005861.4(STUB1):c.737C>T (p.Thr246Met), classified in association with SCAR16.
- **Variant classification:** Per ACMG/AMP framework, functional/structural studies (Heuer et al. 2017) support pathogenicity assignment for the six studied variants by demonstrating altered dimerization, α-helical content, aggregation propensity, and degradation rate relative to wild-type CHIP.
- **Functional consequences:**
  - TPR-domain variants (e.g., p.Asn65Ser, p.Glu28Lys) impair substrate (HSP70/HSC70) binding; Shi et al. (PMID:25258038 cohort) found "the p.Asn65Ser substitution impairs CHIP's ability to ubiquitinate HSC70 in vitro, despite being able to self-ubiquitinate."
  - U-box domain variants (e.g., p.Thr246Met) directly impair E3 ubiquitin ligase catalytic activity.
  - CHIP protein levels are "strongly reduced in vivo in patients' fibroblasts compared to controls," indicating that reduced protein stability/abundance is an additional disease mechanism beyond catalytic impairment (PMID:25258038).
  - Overall mechanism: **loss of function** (partial or complete) of CHIP's co-chaperone and/or E3 ubiquitin ligase activities.
- **Somatic vs. germline:** Germline only; no somatic/cancer association established for SCAR16 (note CHIP has separate oncology literature as a tumor-suppressor-adjacent regulator, not relevant to this Mendelian ataxia).
- **Allele frequency:** No specific gnomAD carrier-frequency statistic for SCAR16-causing STUB1 alleles was retrievable in this search; STUB1 pathogenic variants are individually rare/private, consistent with an ultra-rare recessive disorder (search efforts did not surface a pooled carrier frequency — flag as **not available/needs direct gnomAD query**).

**Modifier genes:** TBP (polyglutamine repeat) has been reported in digenic interaction with STUB1 variants modulating penetrance of the overlapping SCA17/SCA48 spectrum (ScienceDirect S1098360021011175) — relevant primarily to the dominant SCA48 side of the STUB1 disease spectrum but illustrative of oligogenic modulation.

**Epigenetic information:** No STUB1/SCAR16-specific epigenetic (DNA methylation/histone) studies were identified.

**Chromosomal abnormalities:** Not applicable — SCAR16 is caused by point/small indel variants, not large chromosomal rearrangements. One case report describes **maternal uniparental isodisomy** of chromosome 16 unmasking a homozygous STUB1 variant in a patient presenting with Gordon-Holmes syndrome phenotype (ResearchGate/PMID search result), an important non-classical inheritance mechanism to note for genetic counseling.

**Suggested gene/molecular ontology terms:** HGNC gene symbol STUB1 (hgnc:17208 lowercase form for dismech); GO:0004842 (ubiquitin-protein transferase activity); GO:0051087 (chaperone binding); GO:0030544 (Hsp70 protein binding); GO:0016567 (protein ubiquitination); GO:0006515 (protein quality control for misfolded or incompletely synthesized proteins) — GO:0071556 is a closer modern term (protein quality control for misfolded or incompletely synthesized proteins is GO:0006515 in some releases; verify current GO ID at curation time).

## 5. Environmental Information

No specific environmental toxin, occupational exposure, or lifestyle factor has been identified as a cause or trigger of SCAR16 in the literature surveyed. This is consistent with SCAR16 being a fully penetrant monogenic recessive disorder once biallelic pathogenic STUB1 variants are present. General deconditioning/fall-risk considerations relevant to any progressive ataxia apply but are not disease-mechanistically specific.

**Infectious agents:** None implicated.

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from molecular lesion to clinical phenotype):**

1. Biallelic pathogenic variants in STUB1 **result in** reduced or absent function of CHIP, acting through two distinguishable, domain-dependent sub-mechanisms:
   1a. TPR-domain variants (e.g., p.Asn65Ser, p.Glu28Lys) **impair** CHIP's binding to HSP70/HSC70 chaperones, reducing co-chaperone function (demonstrated in vitro, PMID:25258038).
   1b. U-box domain variants (e.g., p.Thr246Met) **directly impair** the E3 ubiquitin ligase catalytic activity of CHIP (demonstrated in vitro, PMID:28396517; PMID:31619515).
2. Impaired chaperone binding and/or ubiquitin ligase activity **leads to** reduced ubiquitination of misfolded/damaged client proteins (including HSP70 itself and other CHIP substrates), and in some variants, reduced CHIP protein stability/abundance in patient fibroblasts (**demonstrated**, PMID:25258038).
3. Reduced client-protein ubiquitination **results in** decreased proteasomal degradation of misfolded proteins, i.e., failure of the protein quality-control/proteostasis network (**inferred from biochemical data + downstream cellular phenotypes**; general CHIP biology, GO:0006515/GO:0016567).
4. Chronic proteostasis failure **leads to** accumulation of damaged/misfolded proteins and dysregulated heat-shock response, shown to differ between patient fibroblasts and iPSC-derived neurons (Nordlie et al., PMC7578354) — indicating **cell-type-specific vulnerability**, with neurons (particularly cerebellar) more susceptible.
5. In model systems, loss of CHIP function **causes** disruption of cerebellar granule neuron progenitor (GNP) differentiation and migration during cerebellar development: CHIP knockdown delays GNP migration in the inner external granule layer, while CHIP overexpression causes GNP retention in the outer EGL (electroporation studies in mouse cerebellum, *J Biomed Sci* 2021 line of work) — an **inferred developmental contribution**, distinct from adult neurodegeneration.
6. In STUB1 knockout mouse models, loss of CHIP function **results in** widespread neurodegeneration, with particularly pronounced **Purkinje cell loss** throughout the cerebellum, reproducing ataxic gait and cognitive impairment analogous to SCAR16 patients (**demonstrated in model organism**, search-synthesized from mouse knockout literature).
7. Neurodegeneration concentrated in cerebellar Purkinje and granule cell populations, with variable brainstem/spinal cord involvement, **leads to** the clinical triad of progressive gait/limb ataxia, dysarthria, and oculomotor abnormalities.
8. Independently, in a subset of patients (branch point), CHIP dysfunction in the hypothalamic-pituitary axis **is associated with** hypogonadotropic hypogonadism/secondary infertility — the precise cellular mechanism in the neuroendocrine axis is **not fully elucidated** and is inferred from clinical co-occurrence rather than demonstrated at the cellular level.
9. In parallel, more severe/complete loss of ubiquitin ligase activity (U-box mutations) **correlates with and is proposed to cause** cortical/subcortical involvement manifesting as cognitive decline, while partial loss of chaperone-binding function (TPR/CC mutations) **correlates with** pyramidal tract involvement (hyperreflexia) — this genotype-phenotype correlation is **inferred from cohort statistics** (Madrigal et al., PMID:31619515: "cognitive dysfunction, ancestry, and increased tendon reflex together explain 54% of ataxia severity variation"), not from direct causal proof of the branch mechanism.

**Molecular pathways:** Ubiquitin-proteasome system (KEGG: ko04120 Ubiquitin-mediated proteolysis); HSP70/HSC70 chaperone-cochaperone network; heat-shock response signaling (differentially affected in fibroblasts vs. iPSC-neurons per PMC7578354).

**Cellular processes:** Protein quality control, chaperone-assisted protein folding, ubiquitin-dependent protein catabolic process (GO:0006511), proteostasis, cerebellar granule neuron progenitor proliferation/migration/differentiation, Purkinje cell survival/maintenance.

**Protein dysfunction:** CHIP is a **loss-of-function** disease mechanism at the protein level — reduced catalytic (E3 ligase) activity, reduced substrate (HSP70/HSC70) binding affinity, altered dimerization/oligomerization, increased aggregation propensity (notably p.Thr246Met), and reduced overall protein stability/steady-state abundance (Heuer et al. PMID:28396517; Synofzik PMID:25258038).

**Tissue damage mechanism:** Neurodegeneration via failed proteostasis — chronic accumulation of misfolded/damaged proteins in neurons, particularly cerebellar Purkinje cells, leading to cell loss and cerebellar atrophy visible on MRI.

**Model system caveats:** The dissociation between severity and age-of-onset seen clinically, and the domain-specific mechanistic split (chaperone-binding vs. ligase-catalytic defects), means that a single unified molecular mechanism for "the" SCAR16 phenotype is not established — this is an area of **ongoing mechanistic uncertainty** appropriate for a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` framing when curated (e.g., the precise cellular basis of hypogonadism, and whether developmental GNP effects vs. adult neurodegeneration predominates in human disease, are unresolved).

**Suggested GO terms:** GO:0004842 (ubiquitin-protein transferase activity), GO:0016567 (protein ubiquitination), GO:0051082 (unfolded protein binding), GO:0030544 (Hsp70 protein binding), GO:0006986 (response to unfolded protein), GO:0022900 (electron transport chain — not directly relevant, omit), GO:0021551 (central nervous system morphogenesis) for developmental angle.
**Suggested CL terms:** CL:0000121 (Purkinje cell), CL:0000032 (cerebellar granule cell / granule neuron progenitor equivalent — verify exact CL ID for GNP), CL:0000540 (neuron), CL:0000057 (fibroblast, for the in vitro patient-derived model).

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Cerebellum (cortex and, per some reports, deep nuclei); variable brainstem and spinal cord involvement.
- **Secondary/associated:** Hypothalamic-pituitary axis (hypogonadotropic hypogonadism); peripheral nerves (sensory neuropathy in a subset); in the "accelerated aging" phenotype family, skin (alopecia), eye (uveitis), pancreas (diabetes), and colon (ulcerative colitis) were reported — likely reflecting broader tissue vulnerability to proteostasis failure in that specific TPR-domain genotype rather than a universal SCAR16 feature.
- **Body systems:** Nervous system (primary); endocrine system (secondary, subset); integumentary, ocular, gastrointestinal (rare, genotype-specific).

**Tissue/cell level:**
- Cerebellar cortex: Purkinje cell layer (major degeneration target per mouse knockout data), granule cell layer/external granule layer (developmental GNP effects).
- Patient-derived fibroblasts and iPSC-derived neurons used as in vitro disease models (PMC7578354).

**Subcellular level (GO Cellular Component):** Cytoplasm/cytosol (CHIP is predominantly cytosolic; GO:0005737), proteasome complex interaction (GO:0000502), unfolded protein response machinery.

**Localization:** Bilateral, symmetric cerebellar atrophy (as opposed to unilateral/asymmetric focal lesions) is the typical imaging pattern.

**Suggested UBERON terms:** UBERON:0002037 (cerebellum), UBERON:0002037 subregions e.g. UBERON:0002140 (cerebellar cortex), UBERON:0002020 (Purkinje layer — verify exact ID), UBERON:0000955 (brain), UBERON:0000006 (islet of Langerhans — only if endocrine subphenotype curated), UBERON:0000959 (spinal cord, for the subset with cord involvement).

## 8. Temporal Development

**Onset:** Highly variable — infantile/early childhood cases, teenage-onset (most common per OMIM description), and adult-onset (including one report of hypogonadism preceding ataxia by ~8 years, onset of infertility at age 25 and ataxia at 33, PMID:25258038) are all documented. Median age of onset across cohorts has been cited around 17 years, though ranges from months to older adulthood are reported.

**Progression:** Chronic, progressive course. Roux et al. explicitly note "age at onset and severity were remarkably variable" across the largest reported cohort. Madrigal et al. found ataxia severity (SARA) does **not** correlate with age of onset, distinguishing SCAR16 from many polyglutamine SCAs where earlier onset predicts faster decline — this argues for **domain-specific mechanistic drivers of severity** rather than a simple dose-time relationship.

**Disease course pattern:** Progressive rather than episodic or relapsing-remitting; no spontaneous remission is described. Some families (e.g., the p.Asn65Ser kindred) show a phenotype resembling progressive multisystem/accelerated-aging decline.

**Critical periods:** The cerebellar granule neuron progenitor migration/differentiation defects observed in CHIP-manipulation mouse studies suggest a possible **developmental window** contribution (perinatal cerebellar development) layered on top of ongoing adult neurodegeneration — this dual developmental+degenerative model is an area for further clarification.

## 9. Inheritance and Population

**Epidemiology:** SCAR16 is an ultra-rare disorder. No population-level prevalence/incidence estimate (cases per 100,000) was retrievable from Orphanet or other registries in this search; Orphanet lists it as a very rare disease without a quantified prevalence class (consistent with **prevalence_class: NOT_YET_DOCUMENTED** in dismech terms). It has been reported in Chinese, French, Italian, Dutch, and other European-ancestry families, indicating no single predominant geographic/ethnic cluster, though individual causal variants may show founder effects within specific pedigrees/populations (not confirmed at a population-scale founder-mutation level from the sources reviewed).

**Inheritance pattern:** Autosomal recessive (biallelic — homozygous or compound heterozygous STUB1 variants). Note the closely related, allelic disorder **SCA48 (OMIM #618093)** is autosomal **dominant**, caused by heterozygous STUB1 variants — Madrigal et al. and the PMC8199271 study show that dominant and recessive STUB1 variants can produce **overlapping/indistinguishable in vitro biochemical defects**, so dosage/zygosity rather than qualitatively distinct variant classes may partly determine dominant vs. recessive inheritance — an important nuance for genetic counseling.

**Penetrance:** Believed to be high/complete for biallelic pathogenic variants, though modified by variant-specific severity (domain effect) and possibly digenic interaction with TBP repeat length in overlapping phenotypes.

**Expressivity:** Highly variable, both within and between kindreds — as documented by the divergent p.Asn65Ser ("accelerated aging," no hypogonadism) versus p.Glu28Lys/p.Lys144Ter (hypogonadism preceding ataxia) presentations in the same original cohort (PMID:25258038).

**Genetic anticipation:** Not established/reported for STUB1-SCAR16 (this is not a repeat-expansion disorder in its recessive form, unlike many dominant SCAs).

**Germline mosaicism:** Not specifically reported.

**Founder effects:** Not confirmed at a defined population level in the sources reviewed; individual pathogenic alleles have recurred across specific families/cohorts (Chinese cohort in Shi et al. 2013) suggesting possible local enrichment, but a formal founder-haplotype study was not identified.

**Consanguinity:** Relevant — as an autosomal recessive disorder, homozygosity for STUB1 variants is more likely to be ascertained in consanguineous or genetically isolated families (as in the original Chinese kindred identified by linkage analysis, PMID:23847347).

**Carrier frequency:** Not established/available from the sources searched (would require direct gnomAD gene-page query at curation time).

**Sex ratio:** No sex-skew is reported; the hypogonadism phenotype affects both sexes (reported as infertility in a male in the PMID:25258038 kindred; also case reports of female hypogonadotropic hypogonadism with ataxia in the STUB1 spectrum, e.g., a 2023 Endocrines journal case).

## 10. Diagnostics

**Genetic testing:**
- **First-tier approach:** Given phenotypic overlap with many other recessive/dominant ataxias, **gene panel testing** for hereditary ataxia (including STUB1) or **whole-exome/genome sequencing** is the recommended diagnostic strategy, especially once common repeat-expansion ataxias (SCA1/2/3/6/7, Friedreich ataxia) have been excluded.
- Original discovery approach combined **linkage analysis + whole-exome sequencing** in an index family (PMID:23847347), followed by targeted Sanger sequencing of STUB1 in ataxia cohorts.
- **Single-gene testing** of STUB1 is reasonable when hypogonadism/infertility co-occurs with ataxia (raising suspicion for the historic "Gordon-Holmes" / STUB1 phenotype) or when accelerated-aging-like multisystem features are present.
- Chromosomal microarray/uniparental disomy testing may be relevant given the reported case of maternal UPD16 unmasking a homozygous STUB1 variant.

**Clinical tests:**
- **Brain MRI:** cerebellar atrophy (cortical, sometimes with brainstem involvement) — key imaging finding.
- **Endocrine labs:** LH, FSH, testosterone/estradiol for suspected hypogonadotropic hypogonadism.
- **Neurophysiology:** Nerve conduction studies if peripheral neuropathy suspected.
- **Cognitive assessment:** Formal neuropsychological testing given the high frequency of cognitive dysfunction (Roux et al. describe STUB1 as "a frequent cause of predominant cognitive impairment" among ataxia cohorts).
- **SARA (Scale for Assessment and Rating of Ataxia):** used as the standard severity/progression metric in cohort studies (e.g., Madrigal et al.).

**Differential diagnosis:** Other recessive ataxias (Friedreich ataxia, ataxia-telangiectasia, ARSACS, other SCARs), and the allelic dominant SCA48; ataxia-hypogonadism syndromes of other genetic causes (e.g., RNF216-related Gordon-Holmes syndrome, which is a genetically distinct but phenotypically overlapping entity — important not to conflate RNF216-Gordon-Holmes with STUB1-SCAR16 despite historical naming overlap).

**Screening:** No population newborn-screening or carrier-screening program is established for this ultra-rare disorder; genetic counseling and cascade testing are recommended in affected families.

## 11. Outcome/Prognosis

No formal survival/mortality statistics were identified; SCAR16 is generally understood as a progressive but not directly life-shortening cerebellar disorder (unlike some other recessive ataxias with cardiac/respiratory complications). Morbidity accrues from progressive gait impairment (fall risk, loss of independent ambulation over time), dysarthria/dysphagia, cognitive decline, and — in a subset — infertility from hypogonadotropic hypogonadism. No specific prognostic biomarker beyond genotype (mutation domain: U-box vs. TPR/CC) has been validated to predict severity trajectory, though the Madrigal et al. cohort-level statistical model (cognitive dysfunction + ancestry + hyperreflexia explaining 54% of severity variance) represents an early prognostic framework.

## 12. Treatment

**No disease-modifying or FDA-approved therapy exists for SCAR16.** Management is supportive/symptomatic:
- **Rehabilitation:** Physical therapy (gait/balance training), occupational therapy, and speech-language therapy for dysarthria/dysphagia (NCIT:C15302 Physical Therapy; NCIT:C159273 Speech Therapy; NCIT:C121351 Occupational Therapy) — standard-of-care extrapolated from general ataxia management guidelines rather than SCAR16-specific trials.
- **Endocrine replacement:** Hormone replacement therapy for hypogonadotropic hypogonadism where present (NCIT:C15986 Pharmacotherapy category), managed by endocrinology.
- **Genetic counseling:** NCIT:C15240 (Genetic Counseling) for at-risk family members given autosomal recessive inheritance.
- **No gene therapy, RNA-based therapy, or targeted small-molecule therapy** has reached clinical trials specific to STUB1/SCAR16 in the literature/registries searched. The Madrigal et al. (PMID:31619515) authors propose a **precision-medicine hypothesis** — for TPR/CC-domain (chaperone-binding-impaired) mutations, therapeutically blocking residual mutant CHIP-HSP70 interaction might help; for U-box-domain (ligase-impaired) mutations with cognitive involvement, small-molecule chaperones preventing mutant CHIP oligomerization/aggregation are proposed — but these remain **preclinical/theoretical**, with no cited clinical trial (ClinicalTrials.gov search did not surface an active STUB1/SCAR16-specific interventional trial).
- **Pharmacogenomics:** Not applicable/reported.

## 13. Prevention

No primary prevention exists beyond genetic counseling and reproductive options (carrier testing, prenatal diagnosis, or preimplantation genetic diagnosis) in families with a known pathogenic STUB1 allele, given the autosomal recessive inheritance and identifiable causal variant once a proband is diagnosed. No screening program, immunization, or environmental/behavioral risk-reduction strategy is applicable, as this is a fully genetically determined disorder with no known modifiable environmental trigger.

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal STUB1-ataxia disease was identified in this search (no OMIA entry surfaced). STUB1 is broadly conserved across vertebrates; comparative/orthology resources (NCBI Gene, Alliance of Genome Resources) would list mouse *Stub1* (MGI ortholog) and zebrafish *stub1* as the relevant orthologs used in the model-organism studies below. No zoonotic or cross-species transmission is relevant, as this is a non-infectious monogenic disorder.

## 15. Model Organisms

- **Mouse — STUB1/Chip knockout:** Homozygous Stub1-knockout mice display ataxia and cognitive impairment recapitulating core SCAR16 features, with histological evidence of neuronal loss throughout the cerebellum, especially pronounced Purkinje cell loss, compared to wild-type controls (search-synthesized from the mouse-knockout literature identified). This model supports a **RECAPITULATES**-level relationship for the ataxic/Purkinje-degeneration phenotype, though the model's translational fidelity for the human hypogonadism and cognitive-domain-specific phenotypes is less clearly established (candidate `PARTIALLY_RECAPITULATES` or `UNKNOWN` fidelity pending direct literature check of the primary knockout paper).
- **Mouse — cerebellar granule neuron progenitor electroporation studies (*J Biomed Sci* 2021-adjacent work):** CHIP knockdown/overexpression manipulation in mouse cerebellar GNPs via in utero/postnatal electroporation shows CHIP dosage affects GNP migration and cell-cycle exit in the external granule layer — informative for a **developmental mechanism** hypothesis, distinguishable from the adult-onset neurodegeneration model above (`model_scale: CELLULAR`, target likely a developmental precursor of the "Purkinje/granule cell loss" node — upward extrapolation caveat needed if cited against an adult degeneration phenotype).
- **Zebrafish — Chip U-box truncation mutant** (Frontiers in Molecular Neuroscience 2021, PMID:34630034): A zebrafish mutant truncating the Chip U-box domain shows reduced Purkinje cell body number/size, abnormal Purkinje dendritic organization, decreased 26S proteasome activity in brain, and behavioral changes. stub1 mRNA is enriched in the zebrafish cerebellum (Purkinje and granule layers), supporting conserved tissue-specific expression relevant to the human phenotype. This model directly demonstrates a **RECAPITULATES** relationship for U-box-domain loss-of-function → Purkinje cell/proteasome pathology, with `model_scale` spanning CELLULAR (proteasome activity, dendritic morphology) to TISSUE (Purkinje layer organization).
- **In vitro human models:** Patient-derived fibroblasts (multiple studies, e.g., PMID:25258038, PMC7578354) show reduced CHIP protein levels and altered heat-shock response; iPSC-derived neurons (PMC7578354) show that CHIP mutations affect the heat-shock response **differently** in fibroblasts versus iPSC-neurons — an important **HUMAN_MODEL_MISMATCH**-type caveat, since fibroblast phenotypes may not fully predict neuronal (disease-relevant tissue) behavior.
- **Recombinant protein / biophysical studies:** Heuer et al. (PMID:28396517) performed in vitro biochemical/biophysical characterization (dimerization, secondary structure, aggregation, degradation kinetics) of six patient-derived CHIP variants expressed recombinantly — a COMPUTATIONAL/biochemical (IN_VITRO) evidence source establishing structure-function correlations for E28K, N65S, K145Q, M211I, S236T, and T246M.

---

## Summary of Key PMIDs for Evidence Curation

| PMID | Citation focus |
|---|---|
| 23847347 | Shi et al. 2013, *PLoS One* — original STUB1/CHIP discovery as SCAR16 cause |
| 25258038 | Synofzik et al. 2014, *Orphanet J Rare Dis* — mutation-specific clinical heterogeneity, accelerated-aging phenotype, hypogonadism |
| 28396517 | Heuer et al. 2017, *Biosci Rep* — in vitro structural characterization of 6 CHIP variants |
| 31619515 | Madrigal et al. 2019, *J Biol Chem* — domain-specific genotype-phenotype correlation, cognitive dysfunction vs. hyperreflexia |
| 32778825 | Roux et al. 2020, *Genet Med* — 440-case cohort, 50 STUB1-positive, cognitive impairment emphasis |
| 34070858 | PMC8199271 — dominant (SCA48) vs. recessive (SCAR16) STUB1 variants share biochemical defects |
| 34630034 | Zebrafish Chip U-box truncation model — Purkinje neuron and proteasome pathology |
| (PMC7578354) | CHIP mutations differentially affect heat-shock response in fibroblasts vs. iPSC-neurons |

**Notes on evidence gaps for curation:** Population prevalence/incidence figures, formal gnomAD carrier-frequency data, and any active interventional clinical trial specific to STUB1/SCAR16 were **not found** in this search and should be marked as `NOT_YET_DOCUMENTED` / absent rather than inferred. The precise cellular mechanism linking CHIP dysfunction to hypogonadotropic hypogonadism remains unestablished and is a good candidate for a `KNOWLEDGE_GAP` discussion entry.

Sources:
- [OMIM #615768 — SCAR16](https://www.omim.org/entry/615768)
- [OMIM #618093 — SCA48](https://www.omim.org/entry/618093)
- [Orphanet ORPHA:412057](https://www.orpha.net/en/disease/detail/412057)
- [GARD — Autosomal recessive spinocerebellar ataxia 16](https://rarediseases.info.nih.gov/diseases/17689/autosomal-recessive-spinocerebellar-ataxia-16)
- [Shi et al. 2013 PLoS One (PMID:23847347), via ClinVar/PMC context](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5408658/)
- [Synofzik et al. 2014, Orphanet J Rare Dis (PMID:25258038)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4181732/)
- [Heuer et al. 2017, Biosci Rep (PMID:28396517)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5408658/)
- [Madrigal et al. 2019, J Biol Chem (PMID:31619515)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6916485/)
- [Roux et al. 2020, Genet Med — STUB1 in cerebellar ataxia cohort](https://www.nature.com/articles/s41436-020-0899-x)
- [PMC8199271 — Dominant vs recessive STUB1 variant functional overlap (PMID:34070858)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8199271/)
- [Frontiers in Molecular Neuroscience — zebrafish Chip U-box model (PMID:34630034)](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2021.723912/full)
- [CHIP mutations affect heat shock response differently in fibroblasts vs iPSC-neurons](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7578354/)
- [ClinVar — STUB1 c.737C>T p.Thr246Met](https://www.ncbi.nlm.nih.gov/clinvar/RCV000115001/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 12 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:23847347` (5 mentions) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:32778825` (3 mentions) - The role of exome sequencing in newborn screening for inborn errors of metabolism.
  - shared terms: none

Weighed against this report's own most characteristic terms: `ataxia`, `scar16`, `stub1`, `hypogonadism`, `variant`, `recessive`, `phenotype`, `disorder`, `cerebellar`, `chip`, `cognitive`, `cohort`, `madrigal`, `hypogonadotropic`, `disease`, `identified`, `mutation`, `severity`, `u-box`, `relevant`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 31 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014339` (2 mentions) - the report calls it "if available"; MONDO calls it **autosomal recessive spinocerebellar ataxia 16**
- `CL:0000032` (1 mention) - the report calls it "cerebellar granule cell / granule neuron progenitor equivalent — verify exact CL ID for GNP"; CL calls it **neuroplacodal cell**
- `CL:0000057` (1 mention) - the report calls it "fibroblast, for the in vitro patient-derived model"; CL calls it **fibroblast**
- `UBERON:0002140` (1 mention) - the report calls it "cerebellar cortex"; UBERON calls it **parabigeminal nucleus**
- `UBERON:0002020` (1 mention) - the report calls it "Purkinje layer — verify exact ID"; UBERON calls it **gray matter**
- `UBERON:0000006` (1 mention) - the report calls it "islet of Langerhans — only if endocrine subphenotype curated"; UBERON calls it **islet of Langerhans**
- `UBERON:0000959` (1 mention) - the report calls it "spinal cord, for the subset with cord involvement"; UBERON calls it **optic chiasma**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0071556` (obsolete integral component of lumenal side of endoplasmic reticulum membrane) (1 mention) - replaced by `GO:0098553`
- `GO:0051082` (obsolete unfolded protein binding) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007141` (1 mention) - the report calls it "Sensory neuropathy"; HP calls it **Sensorimotor neuropathy**
- `HP:0007256` (1 mention) - the report calls it "Progressive pyramidal tract signs"; HP calls it **Abnormal pyramidal sign**, and lists "Pyramidal tract signs" among its other names
- `GO:0051087` (1 mention) - the report calls it "chaperone binding"; GO calls it **protein-folding chaperone binding**, and lists "chaperone binding" among its other names
- `GO:0051082` (1 mention) - the report calls it "unfolded protein binding"; GO calls it **obsolete unfolded protein binding**
- `GO:0022900` (1 mention) - the report calls it "electron transport chain — not directly relevant, omit"; GO calls it **electron transport chain**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
