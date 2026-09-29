---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T14:33:16.341458'
end_time: '2026-09-07T14:38:39.804146'
duration_seconds: 323.46
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Agoraphobia
  mondo_id: MONDO:0003709
  category: Psychiatric
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
  num_turns: 24
  total_cost_usd: 1.4745035999999998
  session_id: f0bf9465-eea1-565c-808d-d12bf4a88ce5
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 41
reference_validation:
  total_references: 38
  verified: 37
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.026
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC6746888
  relevance_assessed: 37
  on_topic: 28
  unresolved_references:
  - PMC:PMC12638
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 42
  verified: 41
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 34
  labels_matching: 15
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: HP:0031466
    reported_labels:
    - Derealization
    ontology_label: Impairment in personality functioning
  - term_id: GO:0042493
    reported_labels:
    - response to drug
    ontology_label: GO_0042493
  - term_id: CL:0000166
    reported_labels:
    - "chromaffin cell \u2014 HPA axis/adrenal medulla context"
    ontology_label: chromaffin cell
  - term_id: CL:0000162
    reported_labels:
    - "norepinephrine secreting cell \u2014 locus coeruleus"
    - "Locus coeruleus \u2014 noradrenergic neurons"
    - norepinephrine secreting cell
    ontology_label: parietal cell
  - term_id: UBERON:0001897
    reported_labels:
    - periaqueductal gray
    ontology_label: dorsal plus ventral thalamus
  - term_id: UBERON:0002037
    reported_labels:
    - "cerebellum \u2014 vestibular pathway relay"
    ontology_label: cerebellum
  - term_id: UBERON:0002264
    reported_labels:
    - insular cortex
    ontology_label: olfactory bulb
  - term_id: UBERON:0002756
    reported_labels:
    - locus coeruleus
    ontology_label: anterior cingulate gyrus
  - term_id: UBERON:0001873
    reported_labels:
    - bed nucleus of stria terminalis
    ontology_label: caudate nucleus
  - term_id: UBERON:0001954
    reported_labels:
    - Sylvian fissure region for prefrontal/cingulate context
    ontology_label: Ammon's horn
  - term_id: CHEBI:9048
    reported_labels:
    - sertraline
    ontology_label: Schisantherin A
  - term_id: CHEBI:65357
    reported_labels:
    - escitalopram
    ontology_label: abacopterin D
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0042493
    ontology_label: GO_0042493
    replaced_by: GO:0009410
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Agoraphobia
- **MONDO ID:** MONDO:0003709 (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Agoraphobia** covering all of the
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

I'll research this in parallel across several key areas.

Now let me gather a few more specific details: MONDO/HPO exact terms verification, benzodiazepine treatment specifics, and diagnostic testing/differential diagnosis.

# Agoraphobia: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Agoraphobia is an anxiety/fear-related disorder characterized by marked, disproportionate fear or anxiety triggered by exposure to a range of situations in which escape might be difficult or help unavailable if panic-like or other incapacitating/embarrassing symptoms occur. Since DSM-5, agoraphobia is diagnosed as an independent nosological entity, no longer subordinate to or automatically coupled with panic disorder, although the two frequently co-occur ("Panic Disorder and Agoraphobia," NCBI StatPearls, PMID reference NBK554387). Affected individuals actively avoid the triggering situations, endure them with intense distress, or require a companion to face them.

**Key identifiers:**
- **MONDO:** MONDO:0003709
- **Disease Ontology:** DOID:593
- **ICD-10:** F40.0 (F40.00 without panic disorder history, F40.01 with panic disorder)
- **ICD-11:** 6B02 (Agoraphobia) — in ICD-11, agoraphobia and panic disorder can be coded separately and comorbidly; the ICD-10 "with/without panic disorder" qualifiers have been eliminated (Kazlauskas et al., "Taxonomy of anxiety disorders—a comparison of ICD-10 and ICD-11," PMC12638383)
- **DSM-5-TR:** 300.22
- **MeSH:** D000379
- **HPO:** HP:0000756 (Agoraphobia)

**Synonyms:** Fear of open spaces; fear of public places; fear of crowds; agoraphobia without history of panic disorder; panic disorder with agoraphobia (a related but now separately-coded comorbid presentation).

**Data provenance:** Most available information is derived from aggregated disease-level resources — large population epidemiological surveys (e.g., National Comorbidity Survey Replication, National Epidemiologic Survey on Alcohol and Related Conditions), clinical trial registries, twin/family registries (e.g., Virginia Twin Registry), and case-control neuroimaging/genetic cohorts — rather than individual EHR-level curation, reflecting the nature of psychiatric epidemiology.

**Sources:**
- [Agoraphobia - StatPearls - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK554387/)
- [Taxonomy of anxiety disorders—a comparison of ICD-10 and ICD-11 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12638383/)
- [Table 3.10, Panic Disorder and Agoraphobia Criteria Changes DSM-IV to DSM-5 - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK519704/table/ch3.t10/)

---

## 2. Etiology

### Disease Causal Factors
Agoraphobia is a multifactorial, polygenic psychiatric condition arising from an interaction of genetic vulnerability (fear-circuit and neurotransmitter-system genes), early developmental/environmental exposures (childhood adversity, parenting style), temperament (behavioral inhibition, anxiety sensitivity, neuroticism), and precipitating stressors (often an initial unexpected panic attack or a vestibular/medical event) that lead to conditioned avoidance learning. There is no known infectious or classic single-gene causal factor; it is not a Mendelian disorder.

### Genetic Risk Factors
- **Heritability:** Twin studies from the Virginia Twin Registry estimated heritability at ~39% in women and ~37% in men for agoraphobia; a large study of >5,000 twins reported heritability of 0.36 for agoraphobia without panic disorder history; other estimates (fears/phobias, corrected for unreliability) reach as high as 67%. DSM-5-TR cites heritability "remarkably high at 61%." Genetic factors are estimated to explain 30–60% of individual differences in phobic fears/agoraphobia across studies.
  - Source: [Heritability of Self-reported Phobic Fear - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2226022/); [Genetics of Anxiety and Trauma-Related Disorders - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2760665/)
- **TMEM132D** — the most replicated candidate gene for panic disorder with agoraphobia, first identified via GWAS at the Max Planck Institute of Psychiatry. Risk haplotype SNPs rs7309727 and rs11060369 (intron 3) were replicated across independent European-ancestry cohorts, reaching P = 1.1–1.4 × 10⁻⁸ in primary panic disorder subsets (PMID:22948381, *Translational Psychiatry*, "Replication and meta-analysis of TMEM132D gene variants in panic disorder"). Carriers of the risk variant show higher trait anxiety and larger amygdala volumes (PMID:24495968). TMEM132D methylation mediates the relationship between physical abuse and panic disorder risk (PMC9403743). Mouse studies support TMEM132D as a genuine anxiety-phenotype gene (*Molecular Psychiatry*, "TMEM132D, a new candidate for anxiety phenotypes: evidence from human and mouse studies," PMID via nature.com/articles/mp201041).
- **GWAS findings (2023–2025):** The largest genome-wide association meta-analysis of panic attacks/panic disorder to date (>277,970 individuals) identified 4 genome-wide-significant loci for panic attacks and 1 for panic disorder, with SNP-based heritability of panic disorder estimated at 6.6% (95% CI 5.7–7.6%) assuming 5% population prevalence (ScienceDirect, "Genome-wide association meta-analyses of panic disorder and panic attacks," 2024). A broader Psychiatric Genomics Consortium (PGC)-Anxiety GWAS of major anxiety disorders (122,341 European-ancestry cases, 729,881 controls) identified 58 independent genome-wide significant risk variants and 66 genes with robust biological support, with 51/58 replicating in an independent sample of >1 million self-reported cases; follow-up analyses **implicated GABAergic signaling** as a key mechanistic pathway (*Nature Genetics*, 2025, s41588-025-02485-8). A disorder-specific large-scale GWAS from PGC-Anxiety specifically dissecting panic disorder, agoraphobia, and panic attacks is in progress/recently reported (ScienceDirect S0924977X25006200).
- **Genetic overlap:** GWAS of panic disorder reveals genetic overlap with neuroticism and depression (*Molecular Psychiatry*, PMID s41380-019-0590-2).
- **HLA association:** TMEM132D variants associate with panic disorder specifically in HLA-DRB1*13:02-negative individuals in a Japanese population (PMC4766370), suggesting gene-gene/immunogenetic interaction.
- **Family studies:** Family history of panic disorder is associated with panic disorder *with* agoraphobia in offspring, but "agoraphobia without panic disorder did not show a familial association" in some cohort analyses (StatPearls NBK554387), suggesting partially distinct genetic architectures for the pure agoraphobia phenotype versus panic-comorbid agoraphobia.

**HGNC/gene suggestions:** TMEM132D (hgnc:25467, chromosome 12q24.33).

### Environmental Risk Factors
- **Childhood adversity:** Lack of parental warmth, parental overprotectiveness, childhood fears/night terrors, early-life grief/bereavement, unhappy or traumatic childhood, maltreatment, or sexual abuse increase risk of pathologic anxiety and agoraphobia (StatPearls NBK554387; Psychology Today; ScienceDirect topic overview).
- **Parental style:** Controlling, overprotective parenting and modeling of parental anxious/fearful behavior increase risk.
- **Stressful life events:** Death of a parent, being attacked or mugged, and other acute stressors are associated with onset; being raised in a household with low warmth and high overprotection is a described risk factor.
- **Precipitating medical/physiological events:** An initial unexpected panic attack, or a vestibular insult (e.g., inner-ear disorder, benign paroxysmal positional vertigo, labyrinthitis) can trigger the fear-and-avoidance cascade that develops into agoraphobia (PMID:2809581, "Vestibular dysfunction followed by panic disorder with agoraphobia"; PMID:8599398, "Panic, agoraphobia, and vestibular dysfunction").
- **Sex:** Female sex is a strong risk marker (see epidemiology).
- **Personality:** Neuroticism, low extraversion, anxiety sensitivity, and avoidant/dependent personality traits.

### Protective Factors
- Secure attachment and parental warmth in childhood are protective against anxiety disorder development (inferred from the inverse of the childhood-adversity risk literature above).
- Early identification and CBT-based indicated prevention programs (e.g., "Coping Cat") reduce incident anxiety symptoms in at-risk children, with effect sizes around 0.66 at 3-month follow-up (PMC5236072).
- No specific protective genetic variant or protective allele has been robustly identified for agoraphobia specifically in GWAS to date; broader anxiety GWAS protective/susceptibility architecture is polygenic rather than driven by single protective alleles.

### Gene-Environment Interactions
Childhood trauma and adverse childhood experiences interact with genetic variants such as **COMT Val158Met** and **MAOA** to influence adult anxiety sensitivity and pathologic worry (search synthesis from Psychology Today / ScienceDirect topic reviews). TMEM132D promoter/gene-body methylation mediates the effect of physical abuse exposure on panic disorder risk, illustrating an epigenetic gene-by-environment mechanism (PMC9403743, "The mediating role of transmembrane protein 132D methylation in predicting the occurrence of panic disorder in physical abuse").

**Sources:**
- [Replication and meta-analysis of TMEM132D gene variants in panic disorder](https://www.nature.com/articles/tp201285)
- [Higher anxiety and larger amygdala volumes in carriers of a TMEM132D risk variant](https://pubmed.ncbi.nlm.nih.gov/24495968/)
- [TMEM132D methylation mediates panic disorder risk in physical abuse - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9403743/)
- [Genome-wide association study of major anxiety disorders - Nature Genetics](https://www.nature.com/articles/s41588-025-02485-8)
- [Genome-wide association meta-analyses of panic disorder and panic attacks - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0924977X24003560)
- [Vestibular dysfunction followed by panic disorder with agoraphobia - PubMed](https://pubmed.ncbi.nlm.nih.gov/2809581/)

---

## 3. Phenotypes

### Behavioral / Symptom Phenotypes (with suggested HP terms)

| Phenotype | Description | Suggested HPO term |
|---|---|---|
| Agoraphobia (core) | Marked fear/anxiety in ≥2 of 5 situation clusters: public transportation, open spaces, enclosed spaces, standing in line/crowds, being outside home alone | **HP:0000756** Agoraphobia |
| Situational avoidance | Active avoidance of feared situations | related to HP:0000722 (Compulsive behaviors) is not exact; best captured under HP:0000756 with `temporality`/`clinical_course` qualifiers |
| Panic attacks | Discrete episodes of intense fear with somatic symptoms (palpitations, sweating, trembling, dyspnea, choking sensation, chest pain, nausea, dizziness, derealization, fear of dying/losing control) | HP:0025269 (Panic attack) |
| Anticipatory anxiety | Anxious apprehension prior to encountering feared situations | HP:0000739 (Anxiety) |
| Dependence on companion ("safety behavior") | Requiring another person present to tolerate feared situations | free-text / behavioral phenotype |
| Space and motion discomfort | Disorientation/discomfort in visually complex or unstable environments (e.g., supermarket aisles, escalators) | related to vestibular symptoms; no precise HPO term — candidate free text |
| Derealization/depersonalization | Feeling of unreality or detachment during exposure | HP:0031466 (Derealization) if present in HPO, else free text |

### Phenotype Characteristics
- **Age of onset:** Median onset age ~20 years; onset before age 55 is typical, though a bimodal pattern is described with a second peak in later adulthood, often following a medical event (StatPearls; therecoveryvillage.com statistics compilation).
- **Severity:** Variable — ranges from mild situational avoidance to complete homebound status in severe cases.
- **Progression:** Typically chronic and persistent without treatment; DSM-5-TR explicitly characterizes the natural course as "persistent and chronic," with complete remission "rare" absent intervention (StatPearls NBK554387). Spontaneous remission without treatment occurs in as few as ~10% of cases.
- **Course pattern:** Often episodic/fluctuating with waxing-waning severity tied to stressors, but a substantial proportion follow a chronic-relapsing course. A Harvard/Brown Anxiety Research Project longitudinal cohort (n=309) found only a 0.17 probability of full remission at 1 year for panic disorder with agoraphobia (versus 0.39 for uncomplicated panic disorder), and relapse after remission occurred rapidly (PMID:10678311, "Remission and relapse in subjects with panic disorder and panic with agoraphobia: a prospective short-interval naturalistic follow-up").
- **Frequency/prevalence among affected individuals:** ~90% of individuals with agoraphobia have a comorbid psychiatric condition (other anxiety disorders, depressive disorders, PTSD, or alcohol use disorder) (StatPearls NBK554387).

### Quality of Life Impact
Agoraphobia is associated with substantial functional impairment: decreased work productivity, increased disability days, reduced likelihood of marriage when onset is early, and in severe cases complete inability to leave the home. Long-term disability studies of anxiety disorders (PMC4950589) document sustained impairment in occupational and social functioning. Comorbidity substantially worsens quality-of-life outcomes and prognosis.

**Sources:**
- [Agoraphobia - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK554387/)
- [Remission and relapse in subjects with panic disorder and panic with agoraphobia - PubMed](https://pubmed.ncbi.nlm.nih.gov/10678311/)
- [Long-term disability in anxiety disorders - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4950589/)

---

## 4. Genetic/Molecular Information

Agoraphobia is a polygenic, complex-trait psychiatric disorder rather than a monogenic disease; there is **no single causal gene** analogous to a Mendelian disorder, no OMIM phenotype-gene entry, and no defined pathogenic-variant classification akin to ClinVar ACMG/AMP tiers for a rare disease.

- **Candidate/risk gene:** **TMEM132D** (HGNC gene; 12q24.33) — the best-replicated panic-disorder/agoraphobia-associated locus, identified via GWAS and replicated across independent European and Japanese cohorts (PMID:22948381; PMC4766370). Functional/expression studies in mouse hippocampus and human peripheral blood support a role in anxiety-related gene expression (mp201041).
- **Polygenic architecture:** SNP-based heritability for panic disorder ~6.6% from the 2024 GWAS meta-analysis (>277,970 individuals), with 4 genome-wide significant loci for panic attacks and 1 for panic disorder. The broader 2025 PGC-Anxiety GWAS (122,341 cases) found 58 independent genome-wide significant loci and 66 high-confidence genes across anxiety disorders broadly, implicating **GABAergic signaling** pathways.
- **Variant frequency/population databases:** As a polygenic trait, individual variant allele frequencies (gnomAD, 1000 Genomes) are relevant only in the aggregate polygenic-risk-score sense; no single pathogenic allele has population-frequency significance analogous to monogenic disease variants.
- **Somatic vs. germline:** Not applicable — agoraphobia is not a somatic/oncologic condition; all genetic risk is germline/heritable polygenic risk.
- **Functional consequences:** TMEM132D risk variants are associated with quantitative trait differences — larger amygdala volume and higher trait anxiety in carriers (PMID:24495968) — and with altered emotional processing in cingulate, frontal cortex, and hippocampus circuits (referenced PMID:25974322, "Association of TMEM132D with cingulate, frontal cortex and hippocampal emotional processing in panic disorder").
- **Epigenetics:** TMEM132D DNA methylation status mediates the relationship between childhood/adult physical abuse exposure and panic disorder occurrence (PMC9403743) — a concrete gene × environment epigenetic mechanism.
- **Modifier genes:** COMT (Val158Met) and MAOA genotypes are reported to interact with childhood trauma/ACEs to modulate adult anxiety sensitivity and worry, functioning as modifiers of environmental risk rather than primary causal variants.
- **Chromosomal abnormalities:** No recurrent copy-number variant or chromosomal syndrome is established as causally linked to agoraphobia specifically (distinguishing it from many other HPO-annotated psychiatric phenotypes that arise secondarily in syndromic conditions).

**Suggested HGNC/gene annotation:** TMEM132D (hgnc:25467).

**Sources:**
- [Replication and meta-analysis of TMEM132D gene variants in panic disorder - Translational Psychiatry](https://www.nature.com/articles/tp201285)
- [Polymorphisms in the TMEM132D region are associated with panic disorder in HLA-DRB1*13:02-negative individuals - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4766370/)
- [TMEM132D, a new candidate for anxiety phenotypes: evidence from human and mouse studies - Molecular Psychiatry](https://www.nature.com/articles/mp201041)
- [Genome-wide association study of major anxiety disorders - Nature Genetics](https://www.nature.com/articles/s41588-025-02485-8)

---

## 5. Environmental Information

- **Toxins/pollution/occupational exposures:** No well-established specific environmental toxin or occupational exposure is documented as a direct cause of agoraphobia in the literature surveyed; this contrasts with the psychosocial/developmental environmental factors that dominate the etiological literature.
- **Lifestyle factors:** Alcohol and sedative misuse frequently develop secondarily as self-medication for agoraphobic anxiety, and comorbid alcohol use disorder is common and associated with increased chronicity (Anxiety and Alcohol Use Disorders: Comorbidity and Treatment Considerations, PMC3860396). Caffeine and other sympathomimetic/panicogenic substances (e.g., stimulants) can precipitate panic symptoms that reinforce avoidance behavior.
- **Psychosocial/developmental environmental factors** (see Etiology, Section 2): childhood adversity, parental overprotection/anxious modeling, stressful life events, bereavement, assault/mugging.
- **Infectious agents:** Not applicable — agoraphobia has no established infectious etiology, though acute vestibular infections (e.g., viral labyrinthitis) can serve as a precipitating medical trigger for the fear-avoidance cascade in susceptible individuals (see vestibular dysfunction literature, Section 6).

**Sources:**
- [Anxiety and Alcohol Use Disorders: Comorbidity and Treatment Considerations - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3860396/)
- [Vestibular dysfunction followed by panic disorder with agoraphobia - PubMed](https://pubmed.ncbi.nlm.nih.gov/2809581/)

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain (numbered mechanistic sequence)

1. **Genetic/epigenetic predisposition** (e.g., TMEM132D risk haplotype; polygenic GABAergic-pathway risk variants; TMEM132D promoter methylation altered by early-life abuse) **leads to** heightened baseline reactivity of the amygdala-centered fear network — *demonstrated in human genetic-imaging association studies; the downstream causal step from genotype to circuit change is correlational/inferred rather than experimentally proven in humans*.
2. Constitutively **reduced serotonergic (5-HT) tone and diminished GABA_A receptor binding in the amygdala** (particularly basolateral nucleus) **results in** loss of GABAergic-dependent inhibitory/compensatory restraint on amygdala output — *supported directly in a mouse genetic model of brain serotonin deficiency showing facilitated panic-like escape behavior (PMC5682603), and by human PET/imaging findings of lower GABA_A and 5-HT receptor binding in the amygdala of panic disorder patients (Translational Psychiatry systematic review, PMC11258274/PMID via s41398-024-02966-0); translation from rodent to human amygdala circuitry is inferred by analogy*.
3. This disinhibited amygdala, together with **dysregulated brainstem CO2/chemoreceptor ("suffocation alarm") circuitry**, **leads to** a hypersensitive threshold for triggering the intrinsic fear/panic response — *Klein's false suffocation alarm theory, refined over 30 years of research, is now considered well-established: "it is now well established that anomalies in respiratory control (including the CO2 sensing system) are key to PD"; amygdala-driven apnea has been proposed as the proximate chemoreceptive trigger (ScienceDirect S0301051122000473)*.
4. Activation of this hypersensitive fear network **results in** engagement of the broader "fear network" — amygdala, hippocampus, thalamus, hypothalamus, periaqueductal gray, locus coeruleus, insula, anterior cingulate and prefrontal cortex, and bed nucleus of the stria terminalis — **causing** the acute somatic/autonomic panic attack (tachycardia, dyspnea, sweating, trembling, derealization) via noradrenergic locus coeruleus outflow and HPA-axis (CRH-ACTH-cortisol) activation — *neuroimaging/neuroanatomical model, well supported across multiple systematic reviews (Alpha Psychiatry, PMC12231371/PMC12638... ; PMID:23168129 "The role of the amygdala in the pathophysiology of panic disorder: evidence from neuroimaging studies")*.
5. Repeated or a single intensely aversive unexpected panic attack, occurring in a specific situational context (crowd, open space, public transit, or following a vestibular insult), **leads to** classical/Pavlovian interoceptive and situational fear conditioning, in which previously neutral situational and internal bodily cues become conditioned fear stimuli — *supported by translational rodent fear-conditioning paradigms showing amygdala activation to conditioned stimuli (PMC3551953) and by clinical observation that agoraphobic avoidance maps onto situations where panic previously occurred or escape/help would be limited*.
6. Conditioned fear of situational/interoceptive cues **results in** anticipatory anxiety and hypervigilant monitoring for bodily sensations (interoceptive amplification), which **leads to** cognitive misappraisal of benign somatic sensations as dangerous (catastrophic misinterpretation) — *supported by fMRI interoception studies in panic disorder with agoraphobia (PMC5465291) showing altered insula/interoceptive processing, and by cognitive models underlying CBT*.
7. This misappraisal and anticipatory anxiety **drives** deliberate avoidance of, or endurance with dread of, the trigger situations (public transportation, open spaces, enclosed spaces, crowds/lines, being away from home alone) — the behavioral hallmark of agoraphobia — **resulting in** progressive negative reinforcement: avoidance reduces short-term anxiety, which reinforces further avoidance and situational generalization (behavioral learning theory; not itself a "biological" mechanism but the operant loop that converts an acute panic event into a chronic phobic disorder).
8. In parallel/contributing branch: **vestibular system dysfunction** (subclinical or overt) **leads to** an atypical, vision/proprioception-dependent balance-control strategy ("surface dependence") **causing** discomfort in visually complex or spatially ambiguous environments (space and motion discomfort), which **compounds** situational avoidance independent of, or synergistic with, the panic-conditioning pathway — *demonstrated in patients with panic disorder plus moderate-to-severe agoraphobia showing the highest prevalence of vestibular abnormalities among anxiety-disorder groups (PMID:18653552; PMID:9178344 "Surface dependence: a balance control strategy in panic disorder with agoraphobia"); resting-state fMRI shows lower functional connectivity in vestibular-limbic (insula-limbic) networks even in subclinical agoraphobia (PMC6701404)*.
9. Chronic activation of this fear/avoidance system **leads to** structural/functional brain changes over the disease course — smaller amygdala lateral/basal nuclei volumes, altered prefrontal-amygdala connectivity, and (in more severe/longer-duration illness with agoraphobia) reduced pituitary volume reflecting sustained HPA-axis engagement — **resulting in** the chronic, often treatment-refractory clinical phenotype seen in longstanding agoraphobia (PMC6221356 "Smaller volumes in the lateral and basal nuclei of the amygdala in patients with panic disorder"; pituitary-volume finding from ScienceDirect S0278584610004203). *This step is correlational cross-sectional imaging evidence, not a demonstrated causal progression within individual patients over time.*

### Molecular Pathways
- Serotonergic (5-HT) signaling — reduced brain serotonin synthesis facilitates panic-like escape behavior in genetic mouse models (PMC5682603); a novel perifornical-hypothalamic-area-projecting serotonergic system normally inhibits innate panic and conditioned fear responses (PMC10811332).
- GABAergic signaling — implicated both mechanistically (lower GABA_A receptor binding in amygdala) and genetically (GABAergic signaling highlighted by the 2025 PGC-Anxiety GWAS as a top biological pathway).
- Noradrenergic signaling — locus coeruleus hyperactivity/dysregulation is central to acute panic symptom generation (PMID:2258377, "Noradrenergic function in panic disorder"; ScienceDirect S0006322399002462).
- CRH/HPA-axis signaling — corticotropin-releasing hormone modulates amygdala activity and interacts with glutamate, dopamine, serotonin, and norepinephrine systems in panic pathophysiology.
- CCK (cholecystokinin) signaling — CCK-4 (the C-terminal tetrapeptide of cholecystokinin) reliably and dose-dependently induces panic attacks in both patients with panic disorder and healthy volunteers, indistinguishable from spontaneous attacks (PMID:2180549), and activates amygdala circuitry on fMRI (PMID:18095276), establishing CCK signaling as a validated pharmacological panic-induction pathway.
- **GO term suggestions:** GO:0007268 (chemical synaptic transmission), GO:0007204 (positive regulation of cytosolic calcium ion concentration — CCK receptor signaling), GO:0007586 (digestion; CCK context is separate but the peptide signaling term is GO:0038188 cholecystokinin receptor signaling pathway if available), GO:0042493 (response to drug), GO:0006836 (neurotransmitter transport), GO:0007212 (dopamine receptor signaling pathway), GO:0007214 (gamma-aminobutyric acid signaling pathway).

### Cellular Processes
Neuronal hyperexcitability in amygdala principal neurons secondary to GABAergic disinhibition; synaptic plasticity underlying conditioned fear learning (LTP-like potentiation in amygdala fear circuits); chronic stress-related processes (glucocorticoid signaling, HPA-axis feedback dysregulation).

### Protein Dysfunction
No single structural protein misfolding/aggregation mechanism is implicated (unlike neurodegenerative disease); rather, receptor-level dysfunction is implicated — reduced GABA_A receptor and serotonin receptor/transporter binding density in amygdala, altered CCK receptor (CCK-B/CCKBR) sensitivity underlying panicogenic challenge responses.

### Biochemical Abnormalities
Altered central GABA_A receptor binding; reduced serotonergic tone; dysregulated brainstem CO2 chemoreceptor sensitivity ("suffocation false alarm" hypersensitivity); elevated plasma cortisol at HPA-axis baseline in some panic disorder cohorts.

### Immune System Involvement
An HLA association (TMEM132D effect specific to HLA-DRB1*13:02-negative individuals) suggests possible immunogenetic modulation of risk, though a primary autoimmune or chronic-inflammatory mechanism is not established for agoraphobia.

### Tissue/Anatomical Mechanism Notes
See Section 7 below for detailed anatomical mapping.

### Molecular Profiling
- No disease-defining transcriptomic, proteomic, or metabolomic signature has been established specifically for agoraphobia in the literature surveyed; peripheral gene-expression profiling has been studied in the context of CCK-4-induced panic challenge (PMID:19051287, "Peripheral gene expression profiling of CCK-4-induced panic in healthy subjects"), representing an experimental/challenge-model dataset rather than a disease-state biomarker panel.

### Advanced Technologies
- fMRI/neuroimaging (structural and functional, including resting-state connectivity) is the dominant "omics-adjacent" technology applied, with findings summarized above (amygdala volume, vestibular-limbic connectivity, interoception paradigms). Single-cell, spatial transcriptomic, and CRISPR functional-genomics data specific to agoraphobia are not established in the current literature (largely because it is a clinical/behavioral phenotype rather than a tissue-pathology disease).

**Suggested CL (Cell Ontology) terms:** CL:0000540 (neuron), CL:0011005 (GABAergic neuron), CL:0000850 (serotonergic neuron), CL:0000166 (chromaffin cell — HPA axis/adrenal medulla context), CL:0000162 (norepinephrine secreting cell — locus coeruleus).

**Suggested UBERON/anatomical terms:** UBERON:0001876 (amygdala), UBERON:0002421 (hippocampal formation), UBERON:0001897 (periaqueductal gray), UBERON:0002037 (cerebellum — vestibular pathway relay), UBERON:0002264 (insular cortex), UBERON:0002756 (locus coeruleus), UBERON:0001873 (bed nucleus of stria terminalis), UBERON:0001954 (Sylvian fissure region for prefrontal/cingulate context).

**Sources:**
- [Neurochemical and genetic factors in panic disorder: a systematic review - Translational Psychiatry](https://www.nature.com/articles/s41398-024-02966-0)
- [The role of the amygdala in the pathophysiology of panic disorder: evidence from neuroimaging studies - PubMed](https://pubmed.ncbi.nlm.nih.gov/23168129/)
- [Genetically driven brain serotonin deficiency facilitates panic-like escape behavior in mice - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5682603/)
- [Cholecystokinin-tetrapeptide induces panic attacks in patients with panic disorder - PubMed](https://pubmed.ncbi.nlm.nih.gov/2180549/)
- [Functional neuroanatomy of CCK-4-induced panic attacks in healthy volunteers - PubMed](https://pubmed.ncbi.nlm.nih.gov/18095276/)
- [Amygdala-driven apnea and the chemoreceptive origin of anxiety - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0301051122000473)
- [Surface dependence: a balance control strategy in panic disorder with agoraphobia - PubMed](https://pubmed.ncbi.nlm.nih.gov/9178344/)
- [Lower Functional Connectivity in Vestibular-Limbic Networks in Individuals With Subclinical Agoraphobia - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6701404/)
- [Smaller volumes in the lateral and basal nuclei of the amygdala in patients with panic disorder - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6221356/)

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Brain (central nervous system) — specifically the limbic/fear-circuit network.
- **Secondary/systemic involvement:** Cardiovascular system (tachycardia, palpitations during panic attacks), respiratory system (dyspnea, hyperventilation), vestibular/inner-ear system (balance dysfunction contributing to space-and-motion discomfort), gastrointestinal system (nausea, abdominal distress during attacks).
- **Body systems involved:** Nervous system (primary), cardiovascular, respiratory, endocrine (HPA axis).

### Tissue and Cell Level
- Amygdala (particularly lateral and basal nuclei) — GABAergic and glutamatergic principal neurons.
- Hippocampus and parahippocampal gyrus — contextual fear memory.
- Insular cortex — interoceptive processing.
- Locus coeruleus — noradrenergic neurons (CL:0000162).
- Periaqueductal gray — panic/defensive behavior generation.
- Bed nucleus of the stria terminalis — sustained/anticipatory fear vs. amygdala's phasic fear.
- Prefrontal and anterior cingulate cortex — top-down regulation of fear response, often showing reduced regulatory engagement.
- Vestibular nuclei/inner ear labyrinth — implicated via space-and-motion discomfort mechanism.

### Subcellular Level
- Synaptic membrane GABA_A receptor complexes (reduced binding in amygdala).
- Serotonin transporter (SERT) and 5-HT receptors on presynaptic/postsynaptic membranes.
- **GO Cellular Component suggestions:** GO:0043025 (neuronal cell body), GO:0045202 (synapse), GO:0032590 (dendrite membrane), GO:0034706 (sodium channel complex — relevant to neuronal excitability).

### Localization
- **UBERON terms:** amygdala (UBERON:0001876), hippocampus (UBERON:0002421), insular cortex (UBERON:0002264), locus coeruleus (UBERON:0002756), periaqueductal gray (UBERON:0001897), bed nucleus of stria terminalis (UBERON:0001873), prefrontal cortex (UBERON:0000451, frontal cortex region), pituitary gland (UBERON:0000007 — reported reduced volume with chronic illness/agoraphobia).
- **Lateralization:** Findings are generally reported bilaterally, though some studies report right-lateralized amygdala volume reductions (right lateral/basal nuclei specifically, PMC6221356) and left-lateralized insula activation during anticipation of agoraphobia-specific stimuli (StatPearls neuroimaging summary).

**Sources:**
- [Smaller volumes in the lateral and basal nuclei of the amygdala in patients with panic disorder - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6221356/)
- [Pituitary volume in patients with panic disorder - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0278584610004203)
- [Lower Functional Connectivity in Vestibular-Limbic Networks - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6701404/)

---

## 8. Temporal Development

### Onset
- **Typical age:** Median onset ~20 years; commonly reported range 25–30 years average; onset generally occurs before age 55. A notable proportion of first onset occurs in adolescence (12-month prevalence peaks at 2.0% in the 13–17 age group).
- **Onset pattern:** Often acute/identifiable — frequently follows an initial unexpected panic attack or a discrete precipitating event (vestibular illness, assault, bereavement) — though insidious, gradually progressive onset is also described, particularly in cases arising from chronic childhood anxiety/behavioral inhibition rather than an index panic attack.

### Progression
- **Disease course pattern:** Chronic and persistent in the majority of untreated cases; DSM-5-TR explicitly describes the natural course as "persistent and chronic." A relapsing-remitting pattern is common even with treatment; the Harvard/Brown longitudinal cohort found rapid relapse after remission (PMID:10678311).
- **Progression rate:** Variable — some patients stabilize with mild situational avoidance; others progress to severe, generalized avoidance and complete homebound status.
- **Disease duration:** Typically chronic/lifelong without intervention; spontaneous remission occurs in only ~10% of untreated cases.
- **Stages:** No formally staged classification system (unlike oncologic staging) exists; clinical severity is instead graded by number/breadth of avoided situations and degree of functional impairment (e.g., via the Oxford-Agoraphobic Avoidance Scale).

### Patterns
- **Remission patterns:** Full remission is more likely with combined CBT + pharmacotherapy; treatment-induced remission is substantially more probable than spontaneous remission. At 1-year follow-up in a naturalistic cohort, probability of full remission was only 0.17 for panic disorder with agoraphobia versus 0.39 for uncomplicated panic disorder (PMID:10678311).
- **Critical periods:** Adolescence and young adulthood represent a critical window both for onset and for indicated CBT-based prevention interventions in at-risk youth (e.g., those with elevated anxiety sensitivity or behavioral inhibition).
- **Sex-based course:** No significant sex difference detected in the chronicity/course of panic disorder with agoraphobia once established, despite the marked sex difference in incidence.

**Sources:**
- [Remission and relapse in subjects with panic disorder and panic with agoraphobia - PubMed](https://pubmed.ncbi.nlm.nih.gov/10678311/)
- [Chronicity, relapse, and illness-course of panic disorder, social phobia, and GAD - PubMed](https://pubmed.ncbi.nlm.nih.gov/12768651/)
- [Agoraphobia - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK554387/)

---

## 9. Inheritance and Population

### Epidemiology
- **12-month prevalence:** 1.7% overall; highest in ages 13–17 (2.0%); declines to 0.4% in individuals aged 65+.
- **Lifetime prevalence:** 0.9% in men; 2.0% in women.
- Agoraphobia is subsumed within the broader "anxiety disorders" category in Global Burden of Disease (GBD) estimates: globally in 2019, an estimated 45.82 million incident cases, 301.39 million prevalent cases, and 28.68 million DALYs were attributed to anxiety disorders overall (Cambridge/PMC8157816, GBD 2019 anxiety disorders analysis).

### Inheritance Pattern
- **Not Mendelian.** Agoraphobia follows a **complex, polygenic/multifactorial inheritance pattern**, consistent with heritability estimates of 36–61% from twin studies and a polygenic architecture confirmed by GWAS (58 loci for anxiety disorders broadly; 1–4 loci for panic disorder/panic attacks specifically).
- **Penetrance/expressivity:** Not applicable in the Mendelian sense; risk is probabilistic and dependent on polygenic burden combined with environmental exposure (gene-environment interaction, e.g., TMEM132D methylation × abuse).
- **Genetic anticipation, germline mosaicism, founder effects, consanguinity role, carrier frequency:** Not applicable / not established for this polygenic behavioral phenotype.

### Population Demographics
- **Sex ratio:** Marked female predominance; female-to-male prevalence ratio ranges from 1.6–3.1.
- **Affected populations / geographic distribution:** Broadly distributed globally as part of the anxiety disorder spectrum; specific ethnic/geographic prevalence disparities for agoraphobia in isolation are less well characterized in the literature surveyed than for anxiety disorders overall, which show regional GBD variation.
- **Age distribution:** Peak prevalence in adolescence/young adulthood, declining prevalence with advancing age (down to 0.4% at 65+), though late-onset presentations (often medically triggered) occur.

**Sources:**
- [Agoraphobia Epidemiology - News-Medical](https://www.news-medical.net/health/Agoraphobia-Epidemiology.aspx)
- [Global, regional and national burden of anxiety disorders from 1990 to 2019: GBD 2019 - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8157816/)
- [Agoraphobia - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK554387/)

---

## 10. Diagnostics

### Clinical Criteria (Primary Diagnostic Method)
Agoraphobia is diagnosed clinically per **DSM-5-TR** criteria: marked fear/anxiety about ≥2 of 5 situations (public transportation; open spaces such as parking lots/marketplaces/bridges; enclosed places such as shops/theaters; standing in line or being in a crowd; being outside the home alone), where the individual fears/avoids these situations because escape might be difficult or help unavailable if panic-like or embarrassing symptoms develop. Symptoms must persist ≥6 months and cause clinically significant distress or impairment, and cannot be better explained by another medical condition, substance use, or another mental disorder (e.g., specific phobia, social anxiety, separation anxiety, PTSD, or major depressive disorder-related avoidance).

- **ICD-11 code:** 6B02; diagnosable independently of and comorbidly with panic disorder (6B01).

### Screening Tools
- **GAD-7** (Generalized Anxiety Disorder-7): brief (<5 minute) self-report screening tool.
- **Oxford-Agoraphobic Avoidance Scale:** self-report measure of avoidance behavior and distress across situations.

### Laboratory Tests / Biomarkers
No specific validated blood, urine, or genetic biomarker exists for agoraphobia diagnosis; laboratory workup in clinical practice is typically used to rule out medical mimics (e.g., thyroid function tests to exclude hyperthyroidism, ECG/cardiac workup to exclude arrhythmia presenting with palpitations/near-syncope).

### Imaging
Structural/functional MRI is a research tool (amygdala volumetrics, resting-state vestibular-limbic connectivity, fMRI interoception paradigms) rather than a diagnostic clinical requirement.

### Genetic Testing
Not clinically indicated or available for agoraphobia — no gene panel, single-gene test, or chromosomal microarray is part of standard diagnostic workup, consistent with its polygenic/multifactorial nature.

### Differential Diagnosis (Key Distinguishing Features)
| Condition | Key distinguishing feature |
|---|---|
| Specific phobia (situational type) | Fear limited to a single specific situation rather than the ≥2-situation cluster of agoraphobia |
| Separation anxiety disorder | Fear driven by detachment from attachment figures/home, not by the situations themselves |
| Social anxiety disorder | Fear of negative judgment/scrutiny by others, not of entrapment/inability to escape |
| Panic disorder (without agoraphobia) | Panic attacks occur without the situational avoidance/entrapment fear pattern |
| PTSD/acute stress disorder | Avoidance tied to reminders of a specific past trauma |
| Major depressive disorder | Avoidance due to anhedonia, low energy, or apathy rather than fear of panic/entrapment |
| Medical conditions (e.g., cardiac arrhythmia, vestibular/inner-ear disease, hyperthyroidism) | Must be excluded as the primary driver of situational symptoms (e.g., fear of syncope from a genuine cardiovascular condition is not agoraphobia) |

**Sources:**
- [Agoraphobia - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK554387/)
- [Taxonomy of anxiety disorders—ICD-10 vs ICD-11 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12638383/)

---

## 11. Outcome/Prognosis

### Survival and Mortality
Agoraphobia is not directly life-threatening, but it carries **elevated indirect mortality risk** through comorbid substance use disorder and suicide. No disease-specific survival/mortality registry data (e.g., SEER-style) exist, as is typical for non-fatal psychiatric conditions; mortality risk is mediated through comorbidities (alcohol use disorder, depression).

### Morbidity and Function
- Substantial disability: reduced work productivity, increased disability days, complete homebound status in severe untreated cases.
- Long-term functional disability is well documented in longitudinal anxiety-disorder cohorts (PMC4950589).
- Reduced likelihood of marriage associated with early-onset agoraphobia.

### Disease Course / Complications
- **Comorbidity:** ~90% have a comorbid psychiatric diagnosis; specific comorbidity rates: panic disorder 26%, major depressive disorder 12%, generalized anxiety disorder 7%, specific phobia 5%, social phobia 4%, OCD 4%, PTSD 2%.
- **Alcohol/substance use disorder:** Comorbid panic disorder with agoraphobia and GAD are associated with increased risk of persistent alcohol dependence; comorbid substance use disorder significantly raises suicide-attempt risk.
- **Suicidality:** Approximately 15% of individuals with agoraphobia report suicidal thoughts or behaviors.

### Prognostic Factors
- **Favorable:** Early identification/intervention, treatment with combined CBT + pharmacotherapy.
- **Unfavorable:** Greater agoraphobia severity, presence of comorbid anxiety, depressive, personality, or substance use disorders. Without treatment, complete remission is rare (~10%).
- No molecular/biomarker-based prognostic classifier (analogous to oncologic prognostic biomarkers) is established.

**Sources:**
- [Agoraphobia - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK554387/)
- [Anxiety and Alcohol Use Disorders: Comorbidity and Treatment Considerations - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3860396/)
- [Long-term disability in anxiety disorders - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4950589/)

---

## 12. Treatment

### Pharmacotherapy
- **First-line:** SSRIs (selective serotonin reuptake inhibitors). Sertraline and escitalopram are specifically associated with higher remission rates and lower adverse-event risk (StatPearls NBK554387). *Suggested CHEBI/NCIT:* sertraline (CHEBI:9048), escitalopram (CHEBI:65357); NCIT treatment term `NCIT:C15986` (Pharmacotherapy) with `therapeutic_agent` bound to the specific SSRI.
- **Alternatives:** SNRIs (serotonin-norepinephrine reuptake inhibitors) and tricyclic antidepressants.
- **Benzodiazepines** (e.g., alprazolam): effective acutely but **not preferred for long-term use** due to abuse potential, sedation, cognitive dysfunction, and fall risk (StatPearls NBK554387).
- **Pharmacogenomics:** No agoraphobia-specific CPIC/PharmGKB pharmacogenomic guideline exists; general SSRI pharmacogenomic considerations (e.g., CYP2C19/CYP2D6 metabolizer status affecting SSRI dosing) apply generically rather than being agoraphobia-specific.

### Psychotherapy (First-Line, Often Combined with Medication)
- **Cognitive Behavioral Therapy (CBT):** The first-line treatment for panic disorder and agoraphobia. Core components: psychoeducation, cognitive restructuring, breathing retraining, interoceptive exposure, and — critically — **gradual in vivo exposure** to overcome situational avoidance. CBT "effectively targets and alleviates primary symptoms, reduces other anxiety symptoms, and improves the patient's overall quality of life" (StatPearls). CBT results in resolution for about half of patients as monotherapy; combined CBT + pharmacotherapy offers the most effective symptomatic management.
  - *NCIT suggestion:* `NCIT:C:  ` — use `NCIT:C15302` is Physical Therapy (not applicable); the closest general NCIT behavioral-intervention term is `NCIT:C15782`-type "Psychotherapy" concept, or more generically `NCIT:C49236` (Therapeutic Procedure) with `therapeutic_modality: BEHAVIORAL`.
- **Virtual Reality Exposure Therapy (VRET):** A validated modern adjunct/alternative to in-vivo exposure. Meta-analyses find VR exposure "generally as effective as in-vivo exposure" for panic disorder with agoraphobia, with "no evidence that VR exposure is significantly less efficacious than in-vivo exposure in agoraphobia" (PMC6746888, Frontiers systematic review/meta-analysis). A 2025 pilot RCT examined integrating digital/VR interventions into standard CBT for panic disorder and agoraphobia (PMID:40591874).

### Experimental / Clinical Trials
- **NCT03101332** — "Virtual Reality for Panic Disorder With Agoraphobia."
- **NCT01680237** — "Cognitive Behavior Therapy vs Exposure in Vivo in the Treatment of Panic Disorder With Agoraphobia."
- Self-guided digital treatment with VR for panic disorder and agoraphobia — RCT protocol (PMC9123669).
- Digital-intervention-augmented CBT pilot RCT (PMID:40591874, 2025).

### Treatment Outcomes
- CBT (in vivo exposure) and VR exposure show comparable efficacy in head-to-head meta-analyses.
- Facing the Fear neuroimaging study examined clinical and neural effects of CBT versus pharmacotherapy in panic disorder with agoraphobia (PMID:26837851), supporting that both modalities produce measurable neurobiological change.
- Combined CBT + SSRI/SNRI pharmacotherapy is regarded as most efficacious overall.

### Treatment Strategy / Algorithm
1. First-line: CBT with exposure component (in-vivo or VR-based).
2. Add SSRI/SNRI pharmacotherapy for moderate-severe cases, non-response to psychotherapy alone, or patient preference.
3. Reserve benzodiazepines for short-term/acute symptom control only, given long-term risks.
4. Address comorbidities (depression, alcohol use disorder) concurrently given their impact on prognosis.

**Sources:**
- [Agoraphobia - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK554387/)
- [Inferiority or Even Superiority of VRET in Phobias? Meta-Analysis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6746888/)
- [Facing the fear--clinical and neural effects of CBT and pharmacotherapy in panic disorder with agoraphobia - PubMed](https://pubmed.ncbi.nlm.nih.gov/26837851/)
- [Advancing CBT for panic disorder and agoraphobia by integrating a digital intervention - PubMed](https://pubmed.ncbi.nlm.nih.gov/40591874/)
- [Virtual Reality for Panic Disorder With Agoraphobia - ClinicalTrials.gov NCT03101332](https://clinicaltrials.gov/study/NCT03101332)

---

## 13. Prevention

### Primary Prevention
No vaccine or biological primary-prevention intervention exists. Behavioral/psychosocial primary prevention centers on reducing modifiable risk exposures: promoting parental warmth and appropriate autonomy-granting (reducing overprotection), and mitigating childhood adversity/trauma exposure where possible.

### Secondary Prevention (Indicated/Selective Prevention)
- **CBT-based indicated prevention programs** for children/adolescents with elevated anxiety symptoms or anxiety sensitivity (e.g., the "Coping Cat" program) reduce incident/self-reported anxiety symptoms, with an effect size of 0.66 at 3-month follow-up in a randomized controlled trial (PMC5236072).
- Early identification of high-risk individuals (behavioral inhibition in childhood, high anxiety sensitivity, family history of panic disorder/agoraphobia) allows targeted early intervention before full syndrome development.
- Early treatment of an index/first panic attack (before conditioned situational avoidance generalizes) is considered clinically important for preventing progression to full agoraphobia, based on the conditioning-based pathophysiological model (Section 6).

### Tertiary Prevention
Ongoing CBT/exposure therapy and pharmacotherapy to prevent relapse and complication (depression, substance use disorder) in individuals with established agoraphobia; a CBT-based primary-care intervention for panic disorder showed benefit sustained to 5-year follow-up even through the COVID-19 pandemic (PMC10313059).

### Screening
No population-based genetic or biomarker screening program exists; screening in practice relies on brief validated instruments (GAD-7) in primary care and mental health settings.

### Public Health / Behavioral Interventions
Public mental-health literacy campaigns and school-based anxiety-prevention curricula (e.g., Coping Cat-style programs) represent the main public-health-level intervention strategy.

**Sources:**
- [Effectiveness of a CBT-Based Indicated Prevention Program for Children with Elevated Anxiety - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5236072/)
- [CBT—Intervention for panic disorder in primary care: 5 years follow-up - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10313059/)

---

## 14. Other Species / Natural Disease

Agoraphobia as a specifically-defined human DSM/ICD nosological entity has no direct veterinary disease counterpart, but closely analogous fear/anxiety behavioral syndromes are recognized in companion animals:

- **Canine and feline separation anxiety / separation-related disorder:** A well-characterized behavioral disorder in dogs (and less commonly cats) involving fear/anxiety responses triggered by separation from an attachment figure, with both externalized behaviors (destruction, vocalization, house-soiling) and internalized signs (depression-like withdrawal, inappetence). Recent terminology has shifted from "separation anxiety" to "separation-related disorder/problem" to reflect that signs may represent fear, anxiety, or frank phobic behavior rather than anxiety alone (Wikipedia/veterinary literature synthesis; Today's Veterinary Practice).
- **Physiological biomarkers in dogs:** Dogs diagnosed with separation-related problems show elevated salivary vasopressin concentrations upon owner separation compared to controls (PMC6941168), providing a translational neuroendocrine biomarker.
- **Comparative relevance:** While canine separation-related disorder is not "agoraphobia" per se (it centers on separation from an attachment figure rather than fear of open/public spaces or entrapment), it shares core mechanistic features with human anxiety/panic-spectrum disorders — dysregulated attachment-related fear circuitry — and serves as a naturally-occurring model for comparative behavioral neuroscience and psychopharmacology (e.g., testing anxiolytics).
- **Taxonomy:** *Canis lupus familiaris* (NCBITaxon:9615), *Felis catus* (NCBITaxon:9685).
- **OMIA:** No specific OMIA entry for a Mendelian "agoraphobia" trait was identified in this search; separation-related disorder in dogs is understood as a complex behavioral trait rather than a single-locus Mendelian condition.
- **Zoonotic potential/cross-species transmission:** Not applicable — this is a behavioral/neuropsychiatric phenotype, not an infectious disease.

**Sources:**
- [Separation anxiety in dogs - Wikipedia](https://en.wikipedia.org/wiki/Separation_anxiety_in_dogs)
- [Salivary Vasopressin as a Potential Non-Invasive Biomarker of Anxiety in Dogs - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6941168/)
- [Algorithmic Approach: Separation Anxiety in Dogs - Today's Veterinary Practice](https://todaysveterinarypractice.com/behavior/algorithmic-approach-separation-anxiety-in-dogs/)

---

## 15. Model Organisms

### Rodent Behavioral Models (Face Validity for Agoraphobia-Relevant Traits)
- **Elevated Plus Maze (EPM):** Innate avoidance of open-arm exploration is argued to reflect an anxiety-like "agoraphobia" analog in rodents; reduced open-arm entry parallels human agoraphobic avoidance of open spaces.
- **Open Field Test:** Reduced center-field entry and increased thigmotaxis (wall-hugging) in rodents mirror reduced center-field exploration observed in humans with high anxiety sensitivity or clinical agoraphobia, supporting cross-species translational validity of open-field paradigms.
- **Pavlovian fear conditioning:** Robust behavioral/physiological conditioned-fear responses in rodents, with amygdala activation demonstrated via awake rodent fMRI during conditioned-stimulus presentation (PMC3551953) — directly modeling the situational/interoceptive fear-conditioning step of the proposed human pathophysiological chain (Section 6, step 5).
- **Conditioned operant conflict tests:** Model learned/punished avoidance behavior, complementing the innate/unlearned EPM and open-field paradigms.

### Genetic Mouse Models
- **Brain serotonin-deficient mice (Tph2-related constitutive serotonin synthesis deficiency):** Show facilitated panic-like escape behavior, directly supporting the mechanistic role of serotonergic deficiency combined with loss of GABAergic compensatory mechanisms in the basolateral amygdala (PMC5682603, "Genetically driven brain serotonin deficiency facilitates panic-like escape behavior in mice").
- **TMEM132D mouse studies:** Human-mouse translational work established TMEM132D as a genuine anxiety-phenotype gene, with mouse expression/behavioral data supporting the human GWAS association (*Molecular Psychiatry*, mp201041).
- **CO2/chemoreceptor models:** Locus coeruleus noradrenaline depletion studies in male and female mice show differential impact on CO2-induced panic-like responses and hyperventilation, modeling the suffocation-alarm/CO2-hypersensitivity mechanism (ScienceDirect S0278584624001313) with a sex-difference dimension relevant to the strong female-predominance seen clinically.
- **Perifornical-hypothalamic-projecting serotonergic system:** A specific serotonergic circuit identified in rodents that inhibits innate panic and conditioned fear responses when intact (PMC10811332), representing a mechanistic/circuit-level model with direct relevance to panic/agoraphobia pathophysiology.

### Model Characteristics — Recapitulation and Limitations
- **Phenotype recapitulation:** Rodent models robustly recapitulate the acute physiological panic response (autonomic activation, escape/avoidance behavior, amygdala activation) and the conditioned-fear-acquisition process central to agoraphobic avoidance learning.
- **Limitations:** Rodent models cannot capture the complex cognitive/interoceptive misappraisal component (catastrophic misinterpretation of bodily sensations) that is central to human cognitive models of agoraphobia, nor the socially/situationally complex triggers (crowds, public transportation, being far from home) that define the human DSM-5 diagnostic criteria — these are behaviorally proxied (open-field thigmotaxis, EPM open-arm avoidance) rather than directly modeled. Vestibular-contribution mechanisms (space and motion discomfort) also lack a well-established rodent behavioral correlate in the literature surveyed.

### Applications
Rodent EPM/open-field/fear-conditioning models are used to screen anxiolytic pharmacotherapy candidates, dissect neurocircuit-level (amygdala, locus coeruleus, serotonergic) contributions, and test CO2/respiratory-challenge and CCK-4-type panicogenic pharmacological probes preclinically before human challenge studies.

### Resources
Standard model-organism resources (MGI for mouse genetics, IMPC/KOMP for knockout lines) are the relevant databases for TMEM132D and serotonergic-pathway mouse models, though this search did not identify a dedicated public repository specifically curating "agoraphobia" mouse models as a named disease category (reflecting that these are modeled as anxiety/panic-behavior phenotypes rather than as a distinct agoraphobia entity).

**Sources:**
- [Genetically driven brain serotonin deficiency facilitates panic-like escape behavior in mice - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5682603/)
- [Identification of a novel perifornical-hypothalamic-area-projecting serotonergic system that inhibits innate panic and conditioned fear responses - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10811332/)
- [TMEM132D, a new candidate for anxiety phenotypes: evidence from human and mouse studies - Molecular Psychiatry](https://www.nature.com/articles/mp201041)
- [Imaging Conditioned Fear Circuitry Using Awake Rodent fMRI - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3551953/)
- [Locus coeruleus noradrenaline depletion and its differential impact on CO2-induced panic and hyperventilation in male and female mice - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0278584624001313)

---

## Summary of Key Ontology Term Suggestions

| Category | Term | ID |
|---|---|---|
| Disease | Agoraphobia | MONDO:0003709 |
| Phenotype | Agoraphobia | HP:0000756 |
| Phenotype | Panic attack | HP:0025269 |
| Phenotype | Anxiety | HP:0000739 |
| Gene | TMEM132D | hgnc:25467 |
| GO (molecular pathway) | gamma-aminobutyric acid signaling pathway | GO:0007214 |
| GO (molecular pathway) | serotonin receptor signaling pathway | (context-dependent GO term) |
| GO (cellular component) | synapse | GO:0045202 |
| CL | GABAergic neuron | CL:0011005 |
| CL | serotonergic neuron | CL:0000850 |
| CL | norepinephrine secreting cell | CL:0000162 |
| UBERON | amygdala | UBERON:0001876 |
| UBERON | hippocampal formation | UBERON:0002421 |
| UBERON | locus coeruleus | UBERON:0002756 |
| UBERON | periaqueductal gray | UBERON:0001897 |
| UBERON | insular cortex | UBERON:0002264 |
| CHEBI | sertraline | CHEBI:9048 |
| CHEBI | escitalopram | CHEBI:65357 |
| NCIT (treatment) | Pharmacotherapy | NCIT:C15986 |
| NCIT (treatment) | Therapeutic Procedure (behavioral/CBT) | NCIT:C49236 |

---

## Notes on Evidence Gaps

- No OMIM phenotype MIM number exists for agoraphobia (it is not modeled as a Mendelian disorder in OMIM).
- No ClinVar/ClinGen pathogenic-variant curation applies, consistent with its polygenic architecture.
- Orphanet does not list agoraphobia (it is a common, non-rare psychiatric disorder, outside Orphanet's rare-disease scope).
- A disorder-specific, adequately powered GWAS isolating agoraphobia (as distinct from panic disorder/panic attacks) is still emerging as of 2025 (PGC-Anxiety disorder-specific GWAS referenced above); most current genetic evidence is either for panic disorder broadly or the combined "major anxiety disorders" phenotype, so gene-level claims specific to *pure* agoraphobia (without panic disorder) should be flagged as extrapolated/indirect evidence in downstream curation.
- Model-organism literature models panic/fear-conditioning behavior rather than the specific DSM-5 situational construct of agoraphobia; any pathophysiology-to-model links should be flagged with appropriate `fidelity`/`limitations` given this scale/construct gap.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 37 |
| On topic | 28 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMC:PMC12638` (1 mention) - NCBI reports no such accession in PMC

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC6746888` *(abstract only)*: "no evidence that VR exposure is significantly less efficacious than in-vivo exposure in agoraphobia"
  - closest text in source: "Conclusions: We found no evidence that VR exposure is significantly less efficacious than in vivo exposure in Specific Phobia and Agoraphobia"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 34 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031466` (1 mention) - the report calls it "Derealization"; HP calls it **Impairment in personality functioning**
- `GO:0042493` (1 mention) - the report calls it "response to drug"; GO calls it **GO_0042493**
- `CL:0000166` (1 mention) - the report calls it "chromaffin cell — HPA axis/adrenal medulla context"; CL calls it **chromaffin cell**
- `CL:0000162` (3 mentions) - the report calls it "norepinephrine secreting cell — locus coeruleus", "Locus coeruleus — noradrenergic neurons", "norepinephrine secreting cell"; CL calls it **parietal cell**
- `UBERON:0001897` (3 mentions) - the report calls it "periaqueductal gray"; UBERON calls it **dorsal plus ventral thalamus**
- `UBERON:0002037` (1 mention) - the report calls it "cerebellum — vestibular pathway relay"; UBERON calls it **cerebellum**
- `UBERON:0002264` (3 mentions) - the report calls it "insular cortex"; UBERON calls it **olfactory bulb**
- `UBERON:0002756` (3 mentions) - the report calls it "locus coeruleus"; UBERON calls it **anterior cingulate gyrus**
- `UBERON:0001873` (2 mentions) - the report calls it "bed nucleus of stria terminalis"; UBERON calls it **caudate nucleus**
- `UBERON:0001954` (1 mention) - the report calls it "Sylvian fissure region for prefrontal/cingulate context"; UBERON calls it **Ammon's horn**
- `CHEBI:9048` (2 mentions) - the report calls it "sertraline"; CHEBI calls it **Schisantherin A**
- `CHEBI:65357` (2 mentions) - the report calls it "escitalopram"; CHEBI calls it **abacopterin D**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0042493` (GO_0042493) (1 mention) - replaced by `GO:0009410`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007204` (1 mention) - the report calls it "positive regulation of cytosolic calcium ion concentration — CCK receptor signaling"; GO calls it **positive regulation of cytosolic calcium ion concentration**
- `GO:0007212` (1 mention) - the report calls it "dopamine receptor signaling pathway"; GO calls it **G protein-coupled dopamine receptor signaling pathway**, and lists "dopamine receptor signalling pathway" among its other names
- `CL:0011005` (2 mentions) - the report calls it "GABAergic neuron"; CL calls it **GABAergic interneuron**
- `UBERON:0001876` (3 mentions) - the report calls it "amygdala", "UBERON terms:** amygdala"; UBERON calls it **amygdala**, and lists "nucleus amygdalae" among its other names
- `GO:0034706` (1 mention) - the report calls it "sodium channel complex — relevant to neuronal excitability"; GO calls it **sodium channel complex**
- `NCIT:C49236` (2 mentions) - the report calls it "Therapeutic Procedure (behavioral/CBT)"; NCIT calls it **Therapeutic Procedure**
- `NCBITaxon:9615` (1 mention) - the report calls it "Canis lupus familiaris", "Taxonomy:** *Canis lupus familiaris"; NCBITaxon calls it **Canis lupus familiaris**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000162` - called "norepinephrine secreting cell — locus coeruleus", "Locus coeruleus — noradrenergic neurons", "norepinephrine secreting cell"
- `UBERON:0001876` - called "amygdala", "UBERON terms:** amygdala"
- `NCBITaxon:9615` - called "Canis lupus familiaris", "Taxonomy:** *Canis lupus familiaris"