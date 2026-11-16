---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-11-11T19:28:53.775067'
end_time: '2026-11-11T19:45:31.192136'
duration_seconds: 997.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Juvenile Xanthogranuloma
  mondo_id: MONDO:0015534
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: JXG
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
  - claude-opus-5
  web_search_requests: 24
  num_turns: 92
  total_cost_usd: 9.793975499999998
  session_id: cb25d2b1-8e16-4391-95e3-7b3981481a90
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 41
reference_validation:
  total_references: 47
  verified: 47
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 47
  on_topic: 36
  validator_version: 0.5.1
term_validation:
  total_terms: 55
  verified: 49
  not_found: 0
  obsolete: 1
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 6
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: DOID:4424
    reported_labels:
    - Disease Ontology
    ontology_label: juvenile xanthogranuloma
  - term_id: NCIT:C3451
    reported_labels:
    - NCIT
    ontology_label: Juvenile Xanthogranuloma
  - term_id: EFO:1000311
    reported_labels:
    - EFO
    ontology_label: obsolete_Juvenile Xanthogranuloma
  - term_id: GO:0070371
    reported_labels:
    - ERK output
    ontology_label: ERK1 and ERK2 cascade
  - term_id: GO:0070374
    reported_labels:
    - ERK activation
    ontology_label: positive regulation of ERK1 and ERK2 cascade
  - term_id: GO:0090077
    reported_labels:
    - Xanthomatization
    ontology_label: foam cell differentiation
  - term_id: GO:0010742
    reported_labels:
    - Xanthomatization (macrophage)
    ontology_label: macrophage derived foam cell differentiation
  labels_variant: 9
  obsolete_terms:
  - term_id: EFO:1000311
    ontology_label: obsolete_Juvenile Xanthogranuloma
    replaced_by: http://purl.obolibrary.org/obo/MONDO:0015534
  unresolvable_prefixes:
  - ORPHA
  - OMIA
  - EXT_ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Juvenile Xanthogranuloma
- **MONDO ID:** MONDO:0015534 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** JXG
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Juvenile Xanthogranuloma** covering all of the
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

# Juvenile Xanthogranuloma (MONDO:0015534) — Comprehensive Disease Characteristics Report

**Prepared:** 11 November 2026 · **Target entity:** `MONDO:0015534` juvenile xanthogranuloma (JXG) · **Intended use:** population of a DisMech disease knowledge-base entry

---

## 0. Scope note, and two things to settle before curating

**There is no germline causal gene for this disease, and the template header is correct to record none.** Juvenile xanthogranuloma is not a Mendelian disorder. It is a clonal histiocytic neoplasm driven by **somatic** alterations of the receptor-tyrosine-kinase → RAS → RAF → MEK → ERK (MAPK) axis acquired in a myeloid precursor. The recurrent somatic drivers named in the literature — these are the genes a curator will bind, all as `variant_origin: SOMATIC` — are **CSF1R**, **SYK** (as the `CLTC::SYK` fusion), **NTRK1** (as `TPM3::NTRK1` and `IRF2BP2::NTRK1` fusions), **ALK** (as `KIF5B::ALK`), **BRAF** (V600E), **MAP2K1**, **ARAF**, **NRAS**, **KRAS**, **MAPK1**, and **PDGFRB** (as `MRC1::PDGFRB`). Germline *NF1* and *PTPN11* act as **predisposing** RASopathy backgrounds, not as causal genes of JXG itself.

**Two deliberate exclusions, stated up front** (per this project's standing content fences):

- **(a) ALK-inhibitor clinical and trial evidence is omitted.** `ALK` rearrangement is reported as a *molecular finding* in histiocytic lesions with JXG morphology and is included below as such, because that is cytogenetic/diagnostic data. The corresponding **therapeutic** evidence — crizotinib and other ALK-inhibitor response data in ALK-rearranged histiocytosis (reported in Durham et al. 2019, PMID:31768065, and in the ALK-positive histiocytosis series) — is **left out of this report and must not be added to the KB entry**. A curator writing the `treatments:` block should note that the targeted-therapy section is incomplete for this reason.
- **(b)** No chromosomal-lesion evidence on 1p36, 11q, 17q or chromothripsis is included. (This is not a limitation in practice — see §4, where copy-number change is shown to be *non-recurrent* in JXG.)

**Identifier discrepancy to resolve before binding.** The research template header gives `ORPHA:158014`. MONDO's own cross-reference for `MONDO:0015534` is **`ORPHA:158000`** (retrieved from OLS4, 11 Nov 2026). Use MONDO's xref, and verify at binding time.

---

## 1. Disease Information

### 1.1 Overview

Juvenile xanthogranuloma is the most common **non-Langerhans cell histiocytosis (non-LCH)** of childhood: a clonal proliferation of monocyte/macrophage-derived histiocytes that typically forms solitary, self-limited, yellow-orange cutaneous papules or nodules in infants, but which can rarely involve the eye, soft tissue, liver, spleen, lung, bone, bone marrow and central nervous system, with appreciable morbidity and occasional death.

MONDO's definition (retrieved from OLS4):

> "A benign histiocytic tumor that occurs during childhood; it is distinct from Langerhans cell histiocytosis. It is characterized by the presence of lipid-laden, foamy histiocytes and Touton-type giant cells in the dermis."

That definition is accurate for the classic cutaneous lesion but is now **partly outdated in two respects**, both of which matter for curation:

1. **"Benign" understates the systemic variant.** JXG is classified by WHO (5th edition, 2022) among histiocytic/dendritic cell **neoplasms**, and the Kemps et al. 2024 *Blood* study calls it flatly a "histiocytic neoplasm" (PMID:39316650). Systemic JXG carries a 5–10% mortality.
2. **Touton giant cells are not obligate.** Kemps et al. found that "Tumors with CLTC::SYK fusions generally lacked Touton giant cells but exhibited many other histologic features of JXG and concordant methylation profiles" (PMID:39316650).

### 1.2 Classification

| System | Placement |
|---|---|
| **Histiocyte Society revised classification, 2016** (Emile et al., *Blood* 127:2672–2681, **PMID:26966089**) | Group **"C"** — cutaneous and mucocutaneous histiocytoses → **xanthogranuloma (XG) family**, alongside adult xanthogranuloma (AXG), solitary reticulohistiocytoma, benign cephalic histiocytosis, generalized eruptive histiocytosis, progressive nodular histiocytosis and xanthoma disseminatum |
| **WHO Classification of Haematolymphoid Tumours, 5th ed. (2022)** | Histiocytic/dendritic cell neoplasms; unchanged from the revised 4th edition |
| **Histiocyte Society non-LCH blueprint, 2025** (Haematologica 110:2603–2619, **PMID:41178439**) | XG family; the blueprint explicitly reopens the boundary question (see §10.4) |

Emile et al. abstract (verbatim, PMID:26966089):

> "This revised classification system consists of 5 groups of diseases: (1) Langerhans-related, (2) cutaneous and mucocutaneous, and (3) malignant histiocytoses as well as (4) Rosai-Dorfman disease and (5) hemophagocytic lymphohistiocytosis and macrophage activation syndrome."

### 1.3 Key identifiers

Retrieved from the OLS4 MONDO record for `MONDO:0015534` on 11 Nov 2026 (all **verified in this session**):

| Resource | Identifier |
|---|---|
| Mondo | **MONDO:0015534** (`juvenile xanthogranuloma`) |
| Orphanet | **ORPHA:158000** |
| UMLS | C0043324 |
| MeSH | **D014972** (*Xanthogranuloma, Juvenile*) |
| ICD-11 | 98595592 (foundation ID) |
| Disease Ontology | DOID:4424 |
| NCIT | **NCIT:C3451** |
| SNOMED CT | 400204000 |
| EFO | EFO:1000311 |
| MedGen | 12179 |
| GARD | 0020020 |
| NANDO | 2200037 |
| **OMIM** | **None.** JXG has no OMIM phenotype entry — it is not a Mendelian disease |

*Not verified in this session, flagged for lookup before binding:* ICD-10 is conventionally **D76.3** ("Other histiocytosis syndromes"); the ICD-O morphology code for JXG is cited variously in the literature and should be read from the WHO blue book rather than from a secondary source.

### 1.4 Synonyms

Juvenile xanthogranuloma; **JXG**; nevoxanthoendothelioma (historical, obsolete — the lesion is not endothelial); juvenile giant cell granuloma (historical). Note that **"adult xanthogranuloma" (AXG)** is a separate member of the same XG family and should not be collapsed into this entry; the recommended handling is a sibling entry or an explicit note (see §8.1).

### 1.5 Evidence provenance

All content below is **aggregated disease-level literature** — case series, registry studies, systematic reviews and molecular cohorts. No EHR-derived or individual-patient data sources were used. Two registry-scale denominators exist (the Kiel Pediatric Tumor Registry and the Dutch Nationwide Pathology Databank); everything else is hospital case series.

---

## 2. Etiology

### 2.1 Primary cause

**A somatic activating kinase alteration in a myeloid (monocyte–macrophage lineage) precursor.** This replaces the older textbook view that JXG is a reactive granulomatous macrophage response to non-specific injury (trauma, viral infection). That older model persists in secondary sources and should be recorded in the entry as a **superseded hypothesis**, not as current etiology.

Three independent lines of evidence establish the neoplastic model:

1. **Clonality.** X-chromosome inactivation (HUMARA) analysis shows JXG histiocytes to be clonal rather than polyclonal-reactive.
2. **Recurrent, mutually targetable driver alterations.** Kemps et al. 2024 (**PMID:39316650**), verbatim: *"Targetable kinase alterations were detected in 16 of 16 children and 1 of 5 adults."*
3. **Therapeutic dependency.** Lesions regress on MAPK-pathway inhibition (Diamond et al. 2019, **PMID:30867592**; dabrafenib responses in BRAF V600E systemic JXG, **PMID:39177799**).

**There is no established environmental or infectious cause.** No toxin, exposure, radiation source, drug, diet, occupation or pathogen has been linked to JXG in any controlled study. A curator should record this as an explicit negative, and — if an `environmental:` block is wanted at all — use the project's `review_notes` waiver convention rather than inventing an exposure.

### 2.2 Genetic risk factors

| Factor | Nature | Evidence |
|---|---|---|
| **Germline *NF1* pathogenic variant (neurofibromatosis type 1)** | Strongest recognized predisposition. Secondary sources report JXG in up to ~10% of children with NF1; the magnitude varies widely across series | Zvulunov 1995 (PMID:7632061); systematic review PMID:37422708 |
| **Germline *PTPN11* pathogenic variant (Noonan syndrome)** | Reported predisposition; mechanistically coherent as a RASopathy | Ali et al. 2021, *Am J Med Genet A* (**PMID:34032360**) |
| **Somatic MAPK driver (acquired, not inherited)** | The disease-causing event itself, not a risk factor | §4 |

Ali et al. 2021, verbatim (PMID:34032360):

> "A RASopathy that is known to be associated with JXG is neurofibromatosis type 1 (NF1). JXG in NF1 has also been reported in association with a juvenile myelomonocytic leukemia (JMML). As RASopathies, both NS and NF1 have an increased incidence of JMML. ... In understanding the common underlying pathogenetic dysregulation of the Ras/MAPK pathway in both NS and NF1, this report suggests a possible molecular association for why NS individuals may be predisposed to JXG."

### 2.3 Demographic risk factors

- **Age:** overwhelmingly the first two years of life — 71.0% diagnosed within the first year, 34.5% congenital (Kiel registry, **PMID:15613853**).
- **Sex:** male predominance, modest. Kiel M:F **1.4:1** (PMID:15613853); systemic JXG systematic review **61% male** (PMID:36779547). Secondary dermatology sources quote ratios up to 7:1 for multiple-lesion disease; treat these as unreplicated.
- **Ancestry/geography:** **no racial predilection** found in the largest Asian cohort (Wee et al. 2022, **PMID:34820973**, 147 children). No endemic geography. No founder effect — none is possible for a somatic disease.

### 2.4 Protective factors

**None identified.** No genetic protective variant, dietary factor, or exposure has been reported to reduce JXG risk. This is an expected negative for a sporadic somatic neoplasm of infancy and should be recorded as such.

### 2.5 Gene–environment interaction

**No evidence of any.** The only established interaction is **gene–gene**: a germline RASopathy allele (*NF1*, *PTPN11*) plus a second somatic MAPK hit, which is a two-hit genetic model rather than a GxE one. Kobal et al. 2025 (**PMID:40373196**) is the cleanest demonstration that the "second hit" can be shared across two diseases in one patient — see §4.5.

---

## 3. Phenotypes

### 3.1 Cutaneous phenotypes (the defining presentation)

| Phenotype | Frequency | Onset | Course | HPO candidate |
|---|---|---|---|---|
| Solitary cutaneous papule/nodule, yellow-orange | **67%** (Dehner, n=174) / **81.0%** (Kiel, n=129) / **76.2%** (Wee, n=147) | Infancy; 1/3 congenital | Self-limited; involutes over 1–6 yr | *No exact HP term* — see §3.6 |
| Multiple ("agminated"/disseminated) cutaneous lesions | 7% (Dehner); ~24% (Wee) | Earlier onset than solitary | Self-limited | — |
| Subcutaneous mass (deep, no overlying colour) | 16% (Dehner) | Infancy | May persist longer | — |
| Giant JXG (>2 cm), plaque-type, clustered, lichenoid, keratotic, pedunculated, linear variants | Rare, individually | Variable | Larger lesions may ulcerate | — |
| Post-involutional atrophy / anetoderma / hyperpigmentation | Common sequel of congenital & giant lesions | After involution | Permanent | HP:0000953 (hyperpigmentation; **unverified**) |

**Site distribution:** head and neck most common (**44.2%** in Wee et al., PMID:34820973), then trunk, limbs; also hands, feet, anogenital skin, oral cavity, tongue, subungual.

**Severity and quality-of-life impact:** for solitary cutaneous disease, **minimal** — lesions are asymptomatic, and the burden is cosmetic/parental anxiety plus (in facial or periocular lesions) a biopsy decision. No disease-specific PRO instrument exists for JXG; no EQ-5D/SF-36/PROMIS data were found. This is a genuine evidence gap, not an omission.

### 3.2 Ocular phenotypes

Ocular JXG is the single most consequential extracutaneous manifestation because it threatens vision in a pre-verbal child.

**Frequency:** quoted between **0.3% and 10%** of children with cutaneous JXG across sources, most commonly ~0.5%. Notably, Wee et al. (147 Asian children) found **no ophthalmologic complications at all** (PMID:34820973), which is why that group argued against routine screening.

Samara et al. 2015, *Ophthalmology* (**PMID:26189188**), 30 patients / 31 eyes / 32 tumours, median age **15 months**:

| Finding | Frequency |
|---|---|
| **Iris** involvement | **68%** |
| Eye redness at presentation | **12/30 (40%)** |
| **Hyphema** at presentation | **4/30 (13%)** |
| Conjunctiva, eyelid, choroid, orbit | remainder |

Verbatim (PMID:26189188): *"Eye redness (12/30, 40%) and hyphema (4/30, 13%) were the most common presenting symptoms."* and *"Tumor regression was achieved in all cases, without recurrence."*

JXG is widely described as **the most frequent cause of spontaneous hyphema in children**. The downstream chain is: iris infiltration → spontaneous hyphema → **secondary glaucoma** → amblyopia/blindness if untreated.

| Phenotype | HPO candidate | Verified? |
|---|---|---|
| Hyphema | **HP:0011886** Hyphema ("Bleeding in the anterior chamber of the eye") | ✅ verified via OLS4 |
| Glaucoma (secondary) | HP:0000501 Glaucoma | ✗ not verified this session |
| Iris mass / abnormal iris morphology | HP:0000525 or narrower | ✗ |

### 3.3 Systemic / visceral phenotypes

**Frequency of systemic disease:** ~**4–5%** of JXG patients (Dehner 5%, PMID:12717244; Kiel 3.9%, PMID:15613853).

Organ involvement — three independent datasets, which disagree in informative ways:

| Site | Freyer 1996, n=36 (PMID:8765620) | Zou 2023 systematic review, n=159 (PMID:36779547) | Beijing single-centre, n=10 (PMID:34178890) |
|---|---|---|---|
| CNS | 8 | **40.9%** (most common) | **60%** |
| Liver (± spleen) | 8 | **31.4%** | 30% |
| Subcutaneous soft tissue | **12** (most common) | — | — |
| Lung | 6 | — | 50% |
| Bone | — | — | 40% |
| Eye | — | — | 20% |
| Endocrine | — | — | 20% |
| Haematological | — | — | 20% |

The discrepancy is **referral bias, and should be curated as such**: Freyer's series came through a pathology consultation practice and is dominated by soft-tissue masses; the systematic review and the haematology-centre series are dominated by CNS and liver because those are the patients referred to oncologists. Do not present any single column as "the" frequency.

**CNS phenotypes in detail** — Serrallach et al. 2022, *AJNR* (**PMID:36265894**), 14 children:

- Lesion sites: pons (6), **infundibulum (6)**, cerebellar grey matter (5), corpus callosum (3), pituitary gland (3), hypothalamus (3), optic chiasm (2), midbrain (2), leptomeninges (1).
- Clinical, verbatim: *"Patients presented with a wide variety of different symptoms, including headache, seizure, ataxia, strabismus, hearing loss, facial paresis, and diabetes insipidus."*
- **Central diabetes insipidus** is the most important permanent sequela — it was the main permanent sequela in 3/10 patients in the Beijing series (PMID:34178890). HPO: **HP:0000863** Central diabetes insipidus (✅ verified via OLS4); parent **HP:0000873** Diabetes insipidus (✅ verified).

**Haematological / inflammatory phenotypes** — Zhao et al. 2024, *Ann Hematol* (**PMID:39177799**), 17 children with systemic JXG, 5 complicated by HLH, verbatim:

> "All sJXG-HLH patients had intermittent fever, rash, hepatosplenomegaly, cytopenia and high levels of soluble CD25, but interferon-γ was almost normal. Patients with sJXG-HLH had a younger diagnosis age (P = 0.035) and were more likely to have skin, liver, and spleen involvement than those without HLH (P = 0.029, P = 0.003, P = 0.003, respectively)."

Note the **normal interferon-γ** — that is a mechanistically meaningful negative, distinguishing JXG-associated HLH from primary HLH, and is worth a dedicated evidence item.

**Severe hypercalcemia** is a recognized and occasionally fatal complication; Dehner's three fatal cases involved hepatic complications and severe hypercalcemia (PMID:12717244). The mechanism is not established in JXG specifically (macrophage 1α-hydroxylase activity is the usual inference from other granulomatous diseases) — curate as **inferred**, not demonstrated.

### 3.4 Phenotype onset, progression and severity summary

| Axis | Value |
|---|---|
| Onset | **Congenital** in 34.5% (PMID:15613853); 71.0% within the first year; median age at onset 5–15.5 months across series; median 9 months for systemic disease (PMID:36779547) |
| Progression | Cutaneous: **self-limited, spontaneously regressing**. Systemic: variable — progressive, stable, or spontaneously regressing (even in fusion-driven cases, see §4.3) |
| Severity | Cutaneous: mild. Ocular: moderate–severe (sight-threatening). Systemic CNS/hepatic: severe, potentially fatal |

### 3.5 Phenotype frequencies suitable for the `phenotypes:` block

Because JXG has **no OMIM entry**, there is no HPOA-derived frequency annotation to copy. Every frequency in this report must be curated from the primary series, with the series named in the evidence `explanation` (e.g. "81.0% of the 129-patient Kiel Pediatric Tumor Registry cohort").

### 3.6 Ontology gap worth reporting upstream

**HPO has no term for a xanthogranuloma or for a cutaneous histiocytic lesion of this type.** Verified against OLS4 (11 Nov 2026): a search of HP for "xanthogranuloma" returns only `HP:0033761` *Xanthogranulomatous pyelonephritis* and `HP:0032646` *Renal interstitial xanthogranulomatous inflammation* — both renal and neither applicable.

The nearest usable terms are:

| Term | Verified | Suitability |
|---|---|---|
| **HP:0100727** Histiocytosis | ✅ | Correct but **coarse** — would need a `coarse_binding_basis`, most plausibly `NO_HPO_TERM` |
| HP:0000991 Xanthomatosis ("Multiple xanthomas (xanthomata) in the skin. Xanthomas are yellowish, firm, lipid-laden nodules.") | ✅ | **Do not use.** A xanthogranuloma is not a xanthoma — the lipid loading is secondary to a histiocytic proliferation, not to a lipid disorder. Binding here would assert the wrong pathology |
| HP:0034621/0034623/0034625/0034627/0034629 (hepatic / splenic / brain / bone-marrow / bone xanthomatosis) | ✅ | Same objection; these describe lipid deposition |

**Recommendation:** bind the lesion phenotype to `HP:0100727` with `coarse_binding_basis: NO_HPO_TERM` and a `preferred_term` of "Cutaneous juvenile xanthogranuloma", and file an HPO term request for a xanthogranuloma concept under the histiocytosis branch.

---

## 4. Genetic / Molecular Information

### 4.1 The headline: the driver landscape depends on where the disease is

This is the single most important molecular fact for a curator, and it is recent. **Solitary cutaneous JXG is genomically quiet; extracutaneous and systemic JXG is kinase-driven essentially 100% of the time.**

Paxton et al. 2017, *Modern Pathology* (**PMID:28752840**), 21 archived cases on molecular inversion probe array, verbatim:

> "Four cases (19%) showed acquired, clonal alterations. ... Only two of 19 solitary juvenile xanthogranulomas showed abnormal genomic profiles ... No recurrent abnormalities were observed among these cases. The presence of non-recurrent copy number alterations in a subset of samples implies that copy number changes are unlikely driving pathogenesis in juvenile xanthogranuloma, but may be acquired during disease progression."

Kemps et al. 2024, *Blood* (**PMID:39316650**), 16 children with extracutaneous JXG + 5 adults with CNS/soft-tissue xanthogranuloma, sequenced through the Dutch Nationwide Pathology Databank:

> "Targetable kinase alterations were detected in 16 of 16 children and 1 of 5 adults. Alterations included CLTC::SYK fusions in 6 children and CSF1R mutations in 7 others; all below 2 years of age with soft tissue tumors. One child had a CSF1R mutation and MRC1::PDGFRB fusion. ... BRAFV600E was detected in 1 child and 1 adult with CNS-xanthogranulomas; both responded to BRAF inhibition. Finally, a TPM3::NTRK1 fusion or MAP2K1 deletion was detected in 2 children with systemic JXG who experienced spontaneous disease regression."

### 4.2 Recurrent somatic alterations — consolidated

| Gene (HGNC) | Alteration | Frequency / context | Source |
|---|---|---|---|
| **CSF1R** | Activating point mutations | 7/16 children with extracutaneous JXG; all <2 yr with soft-tissue tumours | PMID:39316650; PMID:31768065 |
| **SYK** | **`CLTC::SYK`** fusion | 6/16 children with extracutaneous JXG | PMID:39316650 |
| **NTRK1** | **`TPM3::NTRK1`** (n=3), **`IRF2BP2::NTRK1`** (n=2), 1 unknown partner | **6/21 (28.6%)** of xanthogranulomas | Schlögl et al. 2025, *Am J Surg Pathol* (**PMID:40235191**) |
| **ALK** | **`KIF5B::ALK`** fusion | 4/28 (14%) on IHC screen of JXG-morphology lesions; all systemic | Sakamoto et al. 2026, *Virchows Arch* (**PMID:41968182**) |
| **BRAF** | **V600E** point mutation | 3 pediatric intracranial/cranial JXG; 1 child + 1 adult CNS-XG; a subset of systemic JXG | Techavichit et al. 2017 (**PMID:28504206**); PMID:39316650; PMID:39177799 |
| **MAP2K1** (MEK1) | Activating mutations; also intragenic **deletion** | Recurrent in BRAF-WT non-LCH; MAP2K1 deletion in 1 systemic JXG | PMID:26566875; PMID:39316650 |
| **ARAF** | Activating mutations | Recurrent in BRAF-WT non-LCH | PMID:26566875 |
| **NRAS**, **KRAS** | Activating mutations | Reported in systemic JXG | PMID:26566875; PMID:37736360 |
| **MAPK1** (ERK2) | Activating mutation | 1 aggressive disseminated JXG (*Oncotarget* case report) | DOI:10.18632/oncotarget.17521 |
| **PDGFRB** | **`MRC1::PDGFRB`** fusion | 1 child (co-occurring with a CSF1R mutation) | PMID:39316650 |
| **PTPN11** | Somatic p.D76N (`c.226G>A`) | 1 child, shared clone with JMML | Kobal et al. 2025 (**PMID:40373196**) |

Diamond et al. 2016, *Cancer Discovery* (**PMID:26566875**), the foundational survey:

> "...recurrent kinase fusions involving BRAF, ALK, and NTRK1, as well as recurrent, activating MAP2K1 and ARAF mutations" [were identified] in BRAF(V600E)-wild-type non-LCH.

A secondary summary of a systemic-JXG sequencing cohort (Xu et al. 2023, *Pediatric Investigation*, **PMID:37736360**) reports **MAP2K1 in 27%, KRAS in 18%, NRAS in 18%**. **Caveat:** Europe PMC returns no abstract for this record (it is indexed with publication type "Editorial"), so these figures come from a secondary report and **must be re-read against the primary article before they are quoted in an evidence snippet**.

### 4.3 Variant classification, origin and functional consequence

- **Origin: somatic in every case.** `variant_origin: SOMATIC`. No germline JXG-causing variant exists.
- **Functional consequence: gain of function, uniformly.** `functional_impact_category: GAIN_OF_FUNCTION`. Fusions act by constitutive kinase dimerization/activation (`CLTC::SYK`, `KIF5B::ALK`, `TPM3::NTRK1` all contribute oligomerization domains from the 5′ partner); point mutations act by relieving autoinhibition (CSF1R, BRAF V600E, MAP2K1, ARAF) or by impairing GTP hydrolysis (NRAS, KRAS).
- **Note one apparent exception:** the **MAP2K1 intragenic deletion** reported by Kemps et al. is an *activating* deletion (in-frame loss of the negative-regulatory region), not a loss of function. Diamond et al. 2019 verified this class experimentally: *"the characterization of the mutations that we identified in these patients confirmed that the MAPK-pathway mutations were activating"* (PMID:30867592).
- **ACMG/AMP classification does not apply.** These are somatic oncogenic variants; use AMP/ASCO/CAP somatic tiering (Tier I/II) if a tiering statement is wanted.
- **Population allele frequency: not applicable.** gnomAD frequencies are meaningless for somatic drivers; do not populate that field.
- **COSMIC/cBioPortal** are the right somatic references; COSMIC carries the BRAF V600E, NRAS/KRAS and MAP2K1 hotspots.

### 4.4 Copy number and chromosomal abnormalities

Non-recurrent and probably not pathogenic (Paxton et al., PMID:28752840): trisomy 5 and 17 in one diffuse-cutaneous lesion, 5q LOH in a second lesion from the same patient, 1q and 11q gain in one solitary case, a 7.2 Mb 3p loss in another. **No recurrent karyotypic lesion defines JXG.** Karyotyping and chromosomal microarray therefore have **no diagnostic role** in this disease.

### 4.5 Modifier genes and the germline background

The germline RASopathy background is best read as a **priming event** rather than a modifier. The clearest single piece of evidence is Kobal et al. 2025, *Clin Exp Dermatol* (**PMID:40373196**), verbatim:

> "Skin biopsy confirmed JXG, and exome sequencing revealed a somatic PTPN11 (c.226G>A) variant in both peripheral blood (32.6%) and skin lesions (27.2%). ... Two weeks later, the patient developed overt JMML and was successfully treated with chemotherapy and bone marrow transplantation. The shared mutation supports a clonal relationship between JXG and JMML. ... [this] represents the second documented case of clonally related, sequential JXG and JMML."

This is the mechanistic key to the NF1–JXG–JMML triad (§9.4): the JXG histiocytes and the leukaemic myelomonocytic clone **are the same clone**, which places the cell of origin upstream, in a haematopoietic progenitor.

### 4.6 Epigenetics

- **DNA methylation profiling is diagnostically informative.** Kemps et al.: *"Tumors with CLTC::SYK fusions generally lacked Touton giant cells but exhibited many other histologic features of JXG and concordant methylation profiles"* (PMID:39316650) — i.e. methylation class assignment rescued the diagnosis where morphology failed.
- No disease-defining methylation or histone-modification lesion has been reported. No ENCODE/Roadmap/DiseaseMeth resource covers JXG.

### 4.7 Proteomic / functional-genomic findings

Kemps et al. performed **multispectral immunofluorescence** on CLTC::SYK lesions, with results that map directly onto pathophysiology nodes:

> "...phosphorylated-spleen tyrosine kinase expression was localized to CD163+ histiocytes; tumors with CLTC::SYK fusions also demonstrated mTOR activation, cyclin D1 expression, and variable phosphorylated-extracellular signal-regulated kinase expression."

Note the "**variable** pERK" — this is the evidentiary basis for treating the SYK→PI3K/mTOR arm as a **parallel** mechanism branch rather than as another route into ERK. No transcriptomic, metabolomic, lipidomic, single-cell or spatial dataset specific to JXG was found in GEO/ArrayExpress/MetaboLights. **That is a real gap** — notable given that the lesion is defined by lipid-laden macrophages and has never, as far as this search found, been lipidomically profiled.

---

## 5. Environmental Information

**No environmental, lifestyle or infectious etiology is established.**

- **Environmental factors:** none. No CTD, TOXNET or EPA association. The historical suggestion that trauma or "non-specific injury" triggers a reactive macrophage response is a **hypothesis of exclusion from the pre-molecular era**, now superseded by the clonality and driver-mutation data in §4. It should appear in the entry, if at all, as a refuted or superseded hypothesis with `supports: REFUTE` against the clonality evidence — not as an `environmental:` record.
- **Lifestyle factors:** none. Not applicable — this is a disease of infants.
- **Infectious agents:** none. Viral triggering has been speculated and never demonstrated. No NCBI Taxonomy entity should be bound.

**Curation guidance:** leave `environmental:` empty and record the search in `review_notes` using the project's `Left deliberately uncited.` waiver convention, naming the databases queried (CTD, TOXNET, PubMed exposure terms) and what they returned.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain

**Step 1 — Initiating lesion.** A **somatic activating alteration of a receptor tyrosine kinase or of the RAS–RAF–MEK–ERK cascade** arises in a myeloid precursor of the monocyte–macrophage lineage. *Demonstrated* (PMID:39316650, 16/16 children; PMID:26566875). The specific lesion is one of: a **CSF1R** activating point mutation; a kinase fusion (**`CLTC::SYK`**, **`TPM3::NTRK1`**, **`IRF2BP2::NTRK1`**, **`KIF5B::ALK`**, **`MRC1::PDGFRB`**); or a MAPK-cascade point mutation (**BRAF V600E**, **MAP2K1**, **ARAF**, **NRAS**, **KRAS**, **MAPK1**, **PTPN11**).

**Step 2 — Constitutive kinase activation.** The alteration **leads to** ligand-independent, constitutive kinase activity. For CSF1R this is autonomous M-CSF-receptor signalling; for the fusions, the 5′ partner supplies an oligomerization domain that forces kinase dimerization and autophosphorylation. *Demonstrated for the point mutations* (PMID:30867592: *"the characterization of the mutations that we identified in these patients confirmed that the MAPK-pathway mutations were activating"*); *inferred by homology for several of the fusion partners.*

**Step 3 — Branch point: two effector arms.**

- **3a (canonical, majority) — ERK1/2 activation.** Constitutive upstream signal **results in** sustained ERK1 and ERK2 phosphorylation. *Demonstrated at the level of therapeutic dependency*: cobimetinib produced an 89% overall response rate across histiocytoses regardless of genotype (PMID:30867592), which the authors frame as proof of ERK dependency.
- **3b (CLTC::SYK lesions) — mTOR/cyclin D1 arm.** SYK activation **leads to** mTOR pathway activation and cyclin D1 expression, with only *variable* pERK. *Demonstrated by multispectral immunofluorescence in situ* (PMID:39316650). This branch is why `CLTC::SYK` JXG should not be modelled as a plain MAPK node.

**Step 4 — Clonal expansion and lineage commitment.** Sustained ERK (3a) or mTOR/cyclin D1 (3b) signalling **results in** proliferation and survival of the mutated precursor and biases its differentiation toward a **dermal/interstitial macrophage–dendritic phenotype**: CD68⁺, CD163⁺, CD14⁺, factor XIIIa⁺, fascin⁺, stabilin-1⁺, and critically **CD1a⁻ / langerin(CD207)⁻**, i.e. *not* a Langerhans cell. *Demonstrated phenotypically* (PMID:12717244; PMID:15613853; PMID:34178890); *the differentiation-bias step itself is inferred* by analogy with the "misguided myeloid differentiation" model of LCH.

**Step 5 — Branch point: depth of the cell of origin determines disease extent.** If the alteration arises in a **late, skin-committed precursor**, the clone **leads to** disease confined to the dermis (the 80–95% cutaneous-only majority). If it arises in an **earlier haematopoietic progenitor**, the clone seeds multiple organs and **results in** systemic JXG — and, when the progenitor is early enough, a concurrent myeloid neoplasm. *This step is inferred from the LCH literature but has one direct demonstration in JXG*: the shared `PTPN11 c.226G>A` clone in blood (VAF 32.6%) and skin (27.2%) preceding overt JMML by two weeks (PMID:40373196).

**Step 6 — Tissue accumulation.** The clone **accumulates** in the dermis and, in systemic disease, in subcutaneous soft tissue, liver, spleen, lung, bone, bone marrow, eye (chiefly iris) and CNS (chiefly infundibulum, pons, cerebellum). *Demonstrated* (PMID:8765620; PMID:36779547; PMID:36265894).

**Step 7 — Xanthomatization and giant-cell formation.** Within the lesion, lesional histiocytes take up lipid and **become** foamy/xanthomatized cells; cell–cell fusion **generates** **Touton giant cells** — a ring of nuclei around central eosinophilic cytoplasm with a peripheral foamy rim. *Demonstrated histologically* (PMID:12717244: *"Touton giant cells"* appeared consistently in skin lesions but were reduced or absent in deeper tissues). **The trigger for lipid uptake and for fusion is not established** — this is the least-understood step in the chain and should be curated as a knowledge gap, not as a mechanism. The histological staging of Janssen & Harms (early → classic → transitional, PMID:15613853) is the morphological record of this step running to completion.

**Step 8 — Clinical manifestation, by site.** Lesional mass and local inflammation **produce**:
- *Skin*: yellow-orange papule/nodule (the colour **is** the lipid in step 7).
- *Iris*: iris mass → **spontaneous hyphema** → raised IOP → **secondary glaucoma** → amblyopia/visual loss. *Demonstrated* (PMID:26189188).
- *Liver/spleen*: hepatosplenomegaly, cytopenias, cholestasis, liver failure.
- *CNS (infundibulum/pituitary)*: **central diabetes insipidus**; elsewhere seizures, ataxia, cranial neuropathy, raised ICP. *Demonstrated* (PMID:36265894; PMID:34178890).
- *Systemic macrophage activation*: **HLH** — fever, cytopenias, high soluble CD25, with **near-normal interferon-γ** (PMID:39177799), which distinguishes it mechanistically from primary HLH.
- *Hypercalcemia*: fatal in at least one reported case (PMID:12717244). Mechanism **inferred** (macrophage 1α-hydroxylase activity), not demonstrated in JXG.

**Step 9 — Spontaneous regression (the step that makes JXG unusual).** In most patients the lesion involutes. **The mechanism is unknown.** It is *not* simply that the lesion lacked a driver: Kemps et al. documented spontaneous regression in **1 of 6** `CLTC::SYK`-fusion cases and **2 of 7** CSF1R-mutant cases, and in two systemic cases carrying a `TPM3::NTRK1` fusion or a MAP2K1 deletion (PMID:39316650). A bona-fide kinase-driven neoplasm regressing without treatment is the most interesting open question in this disease, and the authors draw the clinical conclusion explicitly: *"underscoring that treatment is not always necessary."* Curate as a `KNOWLEDGE_GAP` discussion.

### 6.2 Molecular pathways

| Pathway | Role | GO candidate | Verified? |
|---|---|---|---|
| MAPK/ERK cascade | **Central driver** | **GO:0000165** MAPK cascade; **GO:0070371** ERK1 and ERK2 cascade; **GO:0070374** positive regulation of ERK1 and ERK2 cascade | ✅ all three verified via OLS4 |
| RTK signalling (CSF1R, NTRK1, ALK, PDGFRB) | Upstream initiating node | GO:0007169 transmembrane receptor protein tyrosine kinase signaling pathway | ✗ |
| RAS signal transduction | Transducer | GO:0007265 Ras protein signal transduction | ✗ |
| PI3K–AKT–mTOR | Parallel arm in `CLTC::SYK` lesions | GO:0031929 TOR signaling | ✗ |
| Cell-cycle entry (cyclin D1) | Proliferative output | GO:0045737 positive regulation of cyclin-dependent protein serine/threonine kinase activity | ✗ |
| Foam-cell formation | Lesion phenotype | **GO:0090077** foam cell differentiation; **GO:0010742** macrophage derived foam cell differentiation | ✅ both verified via OLS4 |
| Macrophage activation | Lesion phenotype / HLH | GO:0042116 macrophage activation | ✗ |

**GO gap:** there is **no GO term for multinucleated-giant-cell formation by macrophage fusion**. Verified: an OLS4 GO search for "multinucleate cell formation" returns only `GO:0072674` *multinuclear osteoclast differentiation* and unrelated fungal/muscle terms. Touton giant cell formation therefore cannot currently be bound to a GO process; record it in `preferred_term` with no `term:` and note the gap.

### 6.3 Cellular processes, protein dysfunction, metabolism, immunity

- **Cellular processes:** clonal proliferation, impaired apoptosis, aberrant macrophage/dendritic differentiation, lipid loading, cell–cell fusion, granuloma-like tissue organization.
- **Protein dysfunction:** constitutive kinase activity. For the fusions, a chimeric protein in which the N-terminal partner's oligomerization domain replaces the receptor's regulatory/extracellular region. UniProt entries relevant: CSF1R (P07333), SYK (P43405), NTRK1 (P04629), ALK (Q9UM73), BRAF (P15056), MAP2K1 (Q02750), PTPN11 (Q06124). *These accessions were written from knowledge and are flagged as unverified — read them from UniProt before binding.*
- **Metabolic changes:** intracellular lipid accumulation in lesional histiocytes. **Crucially, this is a consequence, not a cause** — JXG is *not* a lipid-storage or dyslipidaemic disorder, and serum lipids are normal. Mis-modelling this as a metabolic disease is the single most likely curation error for this entry.
- **Immune involvement:** no autoimmunity, no immunodeficiency. The immune phenotype is a **neoplastic macrophage** one, with secondary macrophage-activation syndrome/HLH in a minority.
- **Tissue damage mechanism:** mass effect and infiltration, not oxidative stress, ischaemia or fibrosis. In the iris, mechanical/vascular disruption of fragile neovessels produces hyphema.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary:** skin (dermis), overwhelmingly. **Secondary / systemic:** subcutaneous soft tissue; eye (iris » conjunctiva, eyelid, choroid, orbit); central nervous system (infundibulum, pituitary, hypothalamus, pons, cerebellum, corpus callosum, optic chiasm, leptomeninges); liver; spleen; lung; bone; bone marrow; lymph node; kidney/retroperitoneum; oral cavity and tongue; rarely heart, pericardium, gonad, adrenal.

**Body systems:** integumentary (primary); ophthalmic; central nervous; hepatobiliary; haematopoietic/reticuloendothelial; respiratory; skeletal; endocrine (via pituitary infiltration).

### 7.2 Tissue and cell level

| Level | Entity | Ontology candidate | Verified? |
|---|---|---|---|
| Tissue | Dermis | **UBERON:0002067** dermis | ✅ OLS4 |
| Tissue | Skin | UBERON:0002097 skin of body | ✗ |
| Tissue | Subcutaneous tissue | UBERON:0002190 subcutaneous adipose tissue | ✗ |
| Organ | Iris | **UBERON:0001769** iris | ✅ OLS4 |
| Organ | Liver / spleen / lung / CNS / pituitary | UBERON:0002107 / 0002106 / 0002048 / 0001017 / 0000007 | ✗ |
| Cell | Macrophage (lesional histiocyte) | **CL:0000235** macrophage | ✅ OLS4 |
| Cell | Foam cell | **CL:0000891** foam cell; **CL:0000517** macrophage derived foam cell | ✅ OLS4 |
| Cell | Touton / multinucleated giant cell | **CL:0000647** multinucleated giant cell | ✅ OLS4 |
| Cell | Monocyte / dendritic-cell precursor | CL:0000576 monocyte; CL:0000451 dendritic cell | ✗ |

**Cell Ontology gap:** there is **no CL term for a dermal macrophage** (verified: an OLS4 CL search for "dermal macrophage" returns `numFound: 0`), and **none for a Touton giant cell** specifically. `CL:0000647` *multinucleated giant cell* is the closest available and is the right binding, with "Touton giant cell" in `preferred_term`.

**Cell of origin.** Derived from the pathograph per the project's convention: the origin node is the one carrying the somatic `genetic_context`, and its `cell_types` give the cell of origin. For JXG that is a **monocyte–macrophage lineage precursor** — and the `PTPN11` clonality case (PMID:40373196) places it, at least in the systemic/JMML-associated form, in a **haematopoietic progenitor** upstream of both the histiocyte and the myelomonocytic leukaemic clone. For cutaneous-only disease the cell of origin is unresolved; do not assert one.

### 7.3 Subcellular

No compartment-specific pathology. The relevant GO cellular components are those of the drivers: plasma membrane (CSF1R, ALK, NTRK1, PDGFRB), cytosol (SYK, BRAF, MAP2K1, ARAF, PTPN11), and the lipid droplets of the xanthomatized histiocyte (GO:0005811 lipid droplet — **unverified**).

### 7.4 Localization and laterality

Cutaneous lesions are **asymmetric and randomly distributed**, with head-and-neck predominance (44.2%, PMID:34820973). Ocular JXG is characteristically **unilateral**; bilateral cases are reported but rare. CNS disease may be unifocal (5/14) or multifocal (8/14, plus 1 with leptomeningeal spread) (PMID:36265894).

---

## 8. Temporal Development

### 8.1 Onset

| Parameter | Value | Source |
|---|---|---|
| Congenital (present at birth) | **34.5%** | PMID:15613853 |
| Diagnosed within first year | **71.0%** | PMID:15613853 |
| Presenting before age 2 | **69.4%** | PMID:34820973 |
| Mean age at diagnosis | 22.4 months (median 5 months, range 0–244) | PMID:15613853 |
| Median age at onset | 15.5 months | PMID:34820973 |
| Median age, systemic disease | **9 months** | PMID:36779547 |
| Median age, systemic disease (older series) | 0.3 years | PMID:8765620 |
| Median age, ocular disease | **15 months** | PMID:26189188 |
| Adult-onset | ~10% of all xanthogranulomas (secondary sources); adult XG is a **separate XG-family entity** | DermNet; PMID:26966089 |

**Onset pattern:** insidious; a painless papule noticed by a parent. Systemic disease may present acutely with hepatosplenomegaly, cytopenias, or a neurological deficit.

### 8.2 Progression and course

- **Cutaneous JXG: self-limited and spontaneously regressing.** Spontaneous resolution documented in **57.7%** of the 147-child Asian cohort, with a **mean duration to resolution of 18.8 months** — and, importantly, *"The proportion and speed of resolution did not differ in children with single or multiple lesions"* (PMID:34820973). Other series report involution over 1–5 years or 3–6 years. Residual atrophy, anetoderma or hyperpigmentation is common after congenital and giant lesions.
- **Systemic JXG: variable.** Progressive, stable, or spontaneously regressing. Kemps et al. document regression even in fusion-driven systemic disease (PMID:39316650).
- **Adult xanthogranuloma: persistent.** Lesions are less likely to resolve spontaneously than in children.
- **Relapse after excision is uncommon:** 7.0% in the Kiel cohort, which also recorded *"even complete involution after incomplete resection"* (PMID:15613853).

### 8.3 Stages

There is **no clinical staging system** for JXG. The only staged framework is **histological**, from Janssen & Harms (PMID:15613853): early JXG (EJXG, 27.1%) → classic JXG (CJXG, 47.2%) → transitional JXG (TJXG, 16.0%), with combined patterns in 9.7%. This maps onto the dermoscopic evolution (§10.1) and onto step 7 of the causal chain.

For KB purposes, the clinically meaningful axis is **extent**, not stage: cutaneous-solitary → cutaneous-multiple → extracutaneous-single-site → systemic/multisystem.

### 8.4 Critical periods

- **The first two years of life** is when essentially all disease arises and when ocular JXG threatens vision — hence the screening debate in §10.5.
- **The window for amblyopia prevention** in ocular JXG is the same window, which is why delayed recognition of a red eye or spontaneous hyphema in an infant is the main avoidable harm in this disease.
- **In NF1 with multiple JXG**, the period of JMML risk is early childhood; JXG typically precedes or coincides with the leukaemia diagnosis.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Value | Source |
|---|---|---|
| Relative frequency among paediatric tumours | **0.52%** (129/24,600 over 35 years) | Kiel Pediatric Tumor Registry, PMID:15613853 |
| Estimated incidence | ~**1 per 1,000,000** children (≈0.1/100,000) — widely regarded as an **underestimate** because most lesions are diagnosed clinically and never biopsied | DermNet, secondary |
| Proportion with systemic disease | **4–5%** | PMID:12717244; PMID:15613853 |
| Proportion with ocular disease | **0.3–10%**, usually quoted ~0.5%; **0%** in a 147-child Asian cohort | PMID:34820973; secondary |

**Honest statement for the KB:** there is **no population-based incidence figure** for JXG from any cancer registry, SEER, GBD or national surveillance system. The ~1/1,000,000 figure circulates through review articles without a primary denominator behind it. Curate it as `measure_type: UNKNOWN` with `prevalence_class: ULTRA_RARE` and the caveat in `notes`, or omit the number and curate the Kiel relative frequency (0.52% of a defined registry) instead, which *is* primary.

### 9.2 Inheritance

**Not inherited.** JXG is a sporadic somatic neoplasm. Do not populate an `inheritance:` block with a Mendelian mode. Penetrance, expressivity, anticipation, germline mosaicism, founder effects, consanguinity and carrier frequency are **all not applicable**.

Two qualifications:

1. **`HP:0001442` (Typified by somatic mosaicism) should not be bound.** JXG is a post-natal clonal neoplasm, not a developmental mosaic disorder. The project's `somatic-mosaicism` skill draws exactly this line; JXG falls on the neoplasm side.
2. **The predisposing germline conditions are inherited.** NF1 and Noonan syndrome are autosomal dominant. That inheritance belongs in *their* entries, not this one — reference them via the `genetic:` block with `relationship_type: SUSCEPTIBILITY` or `PREDISPOSES`, not as JXG's own inheritance.

### 9.3 Population demographics

- **Sex:** M:F **1.4:1** (Kiel, PMID:15613853); **61% male** in systemic JXG (PMID:36779547); **53.1% male** in the Asian cohort (PMID:34820973); **4:1 male** in one 10-patient systemic series (PMID:34178890). The consistent direction is a mild male excess; the high ratios come from small series.
- **Ancestry:** *"There was no racial predilection"* (PMID:34820973). No population-specific variant or geographic clustering exists — as expected for somatic disease.
- **Geography:** worldwide, no endemic area.
- **Age distribution:** see §8.1.

### 9.4 The NF1 – JXG – JMML association, and the controversy around it

This is the most clinically consequential association in the disease, **and the literature genuinely disagrees.** The entry must represent both sides.

**For a real association:**

Zvulunov et al. 1995, *Arch Dermatol* (**PMID:7632061**), verbatim:

> "A concomitant finding of JCML and JXG in children with NF represents a true association, rather than a coincidence."

with the quantitative claim that the triple association occurred *"30-fold to 40-fold higher than that expected"* and that children with NF and JXG have *"a 20-fold to 32-fold higher risk for JCML."*

The 2023 systematic review (**PMID:37422708**; 62 articles 1966–2017, 177 patients) adds: JMML was the leukaemia subtype in **86.7%** of NF1 patients with both JXG and leukaemia versus **55.1%** of those without JXG (**P = 0.024**); JXGs in the triple-association group were **larger** (mean 8.5 mm vs 4.3 mm, **P = 0.011**) and **earlier** (mean 0.6 years). NF1 itself confers a 300–350-fold increased JMML risk.

And the mechanism is now demonstrated at clone level (PMID:40373196, §4.5).

**Against routine screening:**

Liy-Wong et al. 2017, *JAAD* (**PMID:28189268**), a matched case-control study, verbatim:

> "Juvenile xanthogranulomas do not appear to confer an increased risk for malignancy in children with NF-1."

(JXG in 4/14 (28.5%) cases vs 6/29 (21%) controls; OR 1.5; the authors note small numbers and retrospective design.)

Wee et al. 2022 (**PMID:34820973**), verbatim:

> "Unless clinically indicated, the results from our study does not support routine screening for juvenile myelomonocytic leukemia, eye or systemic complications, even in the setting of multiple cutaneous JXGs."

**Resolution for curation:** the two positions are less contradictory than they look. The older literature measures the risk of **JMML given NF1 + JXG** (a large relative risk on a very small absolute base); the newer studies measure the **yield of screening an unselected JXG population** (near zero). Curate both, as separate claims with separate evidence, and state the distinction in `notes`. Do **not** average them.

---

## 10. Diagnostics

### 10.1 Clinical and dermoscopic

**Dermoscopy** is the highest-yield non-invasive test and is near-characteristic. The **"setting sun" sign** — a yellow-orange central area with an erythematous/peripheral halo and branched linear telangiectasias — plus **"clouds of pale-yellow globules"** (present in 81.8% in one series), a subtle pigment network, and whitish streaks. The appearance evolves with the histological stage: the setting-sun pattern is constant in early and developed lesions, while yellow globules become more prominent in the late regressive stage as cells become more xanthomatized. The Histiocyte Society blueprint endorses it: *"dermoscopy (a non-invasive skin imaging tool) can aid in diagnosis, revealing a 'setting sun' appearance with a red-yellow center and an erythematous halo"* (PMID:41178439).

### 10.2 Histopathology and immunohistochemistry — the diagnostic gold standard

**Histology:** a dense dermal (or deeper) infiltrate of mononuclear histiocytes, admixed lymphocytes and eosinophils, with foamy/xanthomatized cells and **Touton giant cells** — nuclei in a wreath around central eosinophilic cytoplasm, with a peripheral foamy rim. Dehner: *"Touton giant cells"* were consistent in skin lesions but *"reduced or absent in deeper tissues"* (PMID:12717244). Kemps: `CLTC::SYK` tumours *"generally lacked Touton giant cells"* (PMID:39316650). **Absence of Touton cells does not exclude JXG.**

**Immunophenotype** — the decisive test, because it separates JXG from LCH:

| Marker | JXG | LCH |
|---|---|---|
| CD68 | **+** | + |
| CD163 | **+** | − |
| CD14 | **+** | − |
| Factor XIIIa | **+** (99% in the Kiel cohort) | − |
| Fascin | **+** | variable |
| Stabilin-1 | **+** | − |
| Vimentin | **+** | + |
| **CD1a** | **−** (0/18 in one series; "generally negative" in 129 Kiel cases) | **+** |
| **Langerin / CD207** | **−** | **+** |
| S100 | usually − (positive in <20%) | **+** |

Dehner 2003, verbatim (PMID:12717244): cells were *"uniformly positive for vimentin, CD68, and factor XIIIa while negative for S-100 and CD1a, supporting classification of JXG as a dendritic cell-related histiocytic disorder."*

Beijing systemic series (PMID:34178890): *"CD68/CD163, Fascin and Factor XIIIa positive lesional histiocytes in all 10 patients"*; langerin and CD1a negative in all.

**Add to the panel for extracutaneous or systemic disease (new, 2026):** Sakamoto et al. (**PMID:41968182**) validated an IHC-first screening strategy — **ALK, pan-TRK and BRAF V600E (VE1) immunohistochemistry**, with FISH/NGS confirmation. Verbatim:

> "Six of 28 patients (21%) were positive on IHC (ALK, n = 4; pan-TRK, n = 2), all of whom had systemic disease, representing 46% of systemic cases. All IHC-positive cases were confirmed by FISH."

and

> "These findings demonstrate that IHC-based screening followed by confirmatory FISH provides a rapid and cost-effective strategy for identifying cases of non-LCH with JXG morphology harboring actionable kinase alterations."

This is the most practically actionable recent finding in the disease and belongs in the `diagnosis:` block.

### 10.3 Imaging

**Ultrasound** (the appropriate first-line for a cutaneous or subcutaneous mass in an infant): a **hypoechoic**, well-defined, regularly-shaped mass; colour/power Doppler shows scattered internal and peripheral vascularity (a 2011–2025 retrospective series, PMID:41899058, DOI:10.3390/jcm15062134).

**MRI of soft-tissue/head-and-neck JXG** (11 cases, *J Pediatr Hematol Oncol* 2024): mildly hyperintense or isointense on T1 in 8/9; **hypointense on T2 in 7/10**; **low ADC in 7/9**; enhancement in 7/7. The T2-hypointensity with restricted diffusion is a useful discriminator.

**MRI of CNS JXG** — Serrallach et al. 2022 (PMID:36265894), 14 children:
- T1 isointense to cortex in 7/12, hyperintense in 4/12; T2 isointense 5/13 or hyperintense 4/13
- *"Almost all xanthogranulomas showed avid contrast enhancement"* (13/14 marked)
- Restricted diffusion in 7/10; perilesional oedema in 11/13; mean maximum diameter 2.2 cm (0.8–4.8)
- Hyperdense on CT **without calcification**; loss of the pituitary bright spot in all 3 with infundibular involvement
- The authors warn of *"heterogeneous neuroimaging appearances"* that mimic primary brain neoplasm, lymphoma, leukaemia, other histiocytoses, infection and granulomatous disease — **biopsy is required**.

### 10.4 Molecular diagnostics

| Test | Role |
|---|---|
| **BRAF V600E** (IHC VE1 or PCR/NGS) | Identifies the dabrafenib-eligible subset; the one marker with a proven, replicated therapeutic consequence |
| **Pan-TRK IHC → NTRK FISH/RNA-NGS** | Detects the ~29% NTRK1-fusion subset (PMID:40235191) |
| **ALK IHC → FISH** | Detects the ALK-rearranged subset; see §0(a) for the treatment-evidence exclusion |
| **Targeted DNA+RNA NGS panel** | The definitive test for extracutaneous/systemic disease; must cover `CSF1R`, `SYK`, `NTRK1/2/3`, `ALK`, `BRAF`, `MAP2K1`, `ARAF`, `NRAS`, `KRAS`, `MAPK1`, `PDGFRB`, `PTPN11`, and must include **fusion detection** — a DNA-only panel will miss `CLTC::SYK`, which is the commonest driver in infant soft-tissue JXG |
| **DNA methylation profiling** | Useful where morphology is ambiguous (PMID:39316650) |
| **Germline testing** | Only where NF1 or a RASopathy is clinically suspected |
| **Karyotype / CMA / FISH for aneuploidy** | **No role** (§4.4) |
| **WGS/WES** | Research; WES on paired blood and lesion is what demonstrated the JXG–JMML shared clone (PMID:40373196) |

Schlögl et al. draw the practical conclusion (PMID:40235191):

> "This finding places JXG in the category of proliferative diseases with one of the highest frequencies of NTRK gene rearrangements. Therefore, NTRK gene fusions should be included in a gene panel test for difficult-to-treat JXG."

### 10.5 Laboratory and staging work-up

No diagnostic blood test exists. For **multiple or systemic disease**: FBC with differential and film (for JMML), liver and renal function, calcium (**hypercalcemia can be fatal**), coagulation, ferritin/triglycerides/fibrinogen/soluble CD25 if HLH is suspected, abdominal ultrasound, skeletal survey or MRI, brain MRI.

**Ophthalmological examination** is the point of genuine disagreement:
- Conventional advice: slit-lamp examination for any child with **≥2 cutaneous lesions**, lesions appearing before age 2, a unilateral red eye, or ocular symptoms.
- Wee et al. 2022 found **no** ocular complications in 147 children and argue against routine screening (PMID:34820973).
- The pragmatic reading: screening yield is low, but the harm prevented (amblyopia, glaucoma, blindness in a pre-verbal child) is high and the test is cheap. Curate both positions.

**Clinical criteria:** there are **no consensus diagnostic criteria** for JXG, no DSM/ICD operational definition and no society guideline. Diagnosis is clinicopathological. This is itself a Histiocyte Society research priority (PMID:41178439).

### 10.6 Differential diagnosis

| Presentation | Differentials | Discriminator |
|---|---|---|
| Solitary papule/nodule | Solitary mastocytoma; Spitz nevus; benign cephalic histiocytosis; dermatofibroma; molluscum contagiosum | Darier's sign (mastocytoma); dermoscopy; CD117/tryptase vs CD68/FXIIIa |
| Multiple lesions | **Langerhans cell histiocytosis**; generalized eruptive histiocytosis; xanthoma disseminatum; multicentric reticulohistiocytosis; xanthomas of hyperlipidaemia | **CD1a/langerin** (+ in LCH, − in JXG); normal serum lipids in JXG |
| Extracutaneous/systemic mass | **Erdheim–Chester disease**; **ALK-positive histiocytosis**; Rosai–Dorfman disease; histiocytic sarcoma; malignant soft-tissue tumour | Methylation class; fusion/mutation profile; S100/OCT2 (RDD) |
| Histiocyte-rich pleomorphic mastocytoma | Can mimic both JXG and LCH | Mast-cell markers |

The Histiocyte Society blueprint flags the hardest boundary (PMID:41178439):

> "lesions with xanthogranulomatous morphology - typically associated with JXG, AXG, or ECD - are not pathognomonic of a single disease"

and

> "Mutational profiling alone cannot differentiate ECD from other XG family diseases, since MAPK mutations have been reported in isolated JXG/AXG as well."

It goes further, posing an open question that should be recorded as a knowledge gap in the entry:

> "Whether all JXG/AXG in extracutaneous sites or with more than one skin lesion need to be reclassified as atypical phenotypes of ECD or presumptive evidence/precursor lesions of ECD requires further exploration."

### 10.7 Screening

No newborn, carrier, cascade or population screening exists or is indicated. The only screening questions are **within-patient** (ophthalmological, and JMML surveillance in NF1), both covered above.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

| Population | Outcome |
|---|---|
| **Cutaneous-only JXG** | Essentially **100% survival**; self-limited; no disease-specific mortality |
| **Systemic JXG, systematic review (n=159)** | At last follow-up: *"93 patients (58.5%) were alive with no disease, 56 (35.2%) were alive with disease, and 10 (6.3%) were dead of disease"* (PMID:36779547) |
| **Systemic JXG, overall mortality (literature consensus)** | **5–10%** |
| **Infantile systemic JXG with liver involvement** | **35.2%** fatal (secondary source; the highest-risk subgroup) |
| **Kiel registry (n=129, mostly cutaneous)** | 1 of 5 patients with widespread congenital systemic disease died at 34 days; *"a generally favorable prognosis with a low relapse rate (7.0%)"* (PMID:15613853) |
| **Beijing systemic series (n=10)** | 9/10 survived; 1 died of respiratory failure from pulmonary infection (PMID:34178890) |

**Causes of death:** progressive CNS disease; **liver failure**; refractory hypercalcemia; HLH; treatment-related infection.

**Life expectancy** is normal for cutaneous disease. No actuarial data exist for systemic disease.

### 11.2 Morbidity, disability and quality of life

- **Permanent sequelae in systemic disease:** 3/10 in the Beijing series, *"mainly central diabetes insipidus"* (PMID:34178890); the systematic review similarly identifies CNS and ocular sequelae as the main permanent morbidity.
- **Ocular:** with modern management, excellent — Samara et al. report *"visual acuity was stable or improved (18/19 patients, 95%)"* and IOP controlled long-term without medication in 14/21 (74%), **with no enucleations** (PMID:26189188). Untreated or late-presenting disease still causes glaucoma and blindness.
- **Cutaneous:** cosmetic only — residual atrophy, anetoderma, hyperpigmentation.
- **QoL instruments:** none validated for JXG. No EQ-5D, SF-36 or PROMIS data were found. Record as a gap.

### 11.3 Prognostic factors

| Factor | Direction | Evidence |
|---|---|---|
| **Splenic involvement** | **Worse** — significantly higher risk of death | Systemic JXG cohort, secondary report of PMID:34178890 / PMID:39177799 lineage |
| **Liver involvement** | Worse (liver failure is a leading cause of death) | PMID:36779547 |
| Younger age at diagnosis | Worse (associated with HLH complication) | PMID:39177799 |
| Cutaneous-only, solitary | Excellent | PMID:15613853; PMID:34820973 |
| **Concurrent HLH** | **Possibly neutral** — *"There was no significant difference in the overall survival and progression-free survival between sJXG patients without and with HLH (P = 0.12 and P = 0.46)"* (PMID:39177799) | PMID:39177799 |
| **BRAF V600E** | Actionable — predicts dabrafenib response | PMID:39177799; PMID:39316650 |
| `CLTC::SYK` / `CSF1R` / `NTRK1` fusion | **Not automatically adverse** — spontaneous regression occurred in several | PMID:39316650 |

**No validated prognostic model, risk score or prognostic biomarker exists.** Splenic and hepatic involvement are the two findings with the most consistent adverse signal.

---

## 12. Treatment

> **Scope reminder:** ALK-inhibitor clinical and trial evidence is deliberately omitted from this section (§0a). A KB entry built from this report will therefore be **incomplete for ALK-rearranged histiocytic lesions with JXG morphology**, and should say so.

### 12.1 Cutaneous-only JXG — observation

**Observation is the standard of care.** Most lesions involute (57.7% documented spontaneous resolution, mean 18.8 months, PMID:34820973). There is no established treatment regimen for cutaneous non-LCH, and none is needed. Options where a lesion is symptomatic, ulcerating, functionally obstructive, or cosmetically significant: **surgical excision** (curative; the Kiel group recorded involution even after *incomplete* resection, PMID:15613853), intralesional corticosteroid, cryotherapy, CO₂ laser.

| Intervention | NCIT candidate | Verified? |
|---|---|---|
| Observation / watchful waiting | — (consider NCIT:C15747 Supportive Care, or omit) | ✗ |
| Surgical excision | NCIT:C15329 Surgical Procedure | from CLAUDE.md term list |
| Pharmacotherapy (steroid, etc.) | NCIT:C15986 Pharmacotherapy | from CLAUDE.md term list |

### 12.2 Ocular JXG — topical/periocular corticosteroid first

Samara et al. 2015 (PMID:26189188): *"The iris lesion was treated with topical (18/21, 86%) and/or periocular (4/21, 19%) corticosteroids"*, with **regression in all cases and no recurrence**. Second-line, for corticosteroid-refractory disease: **intraocular bevacizumab** (2 children, PMID:24767830); historically low-dose external-beam radiotherapy, now largely avoided in infants. Glaucoma is managed on its own merits.

### 12.3 Systemic JXG — chemotherapy

**LCH-based regimens are the backbone**, with modest and honestly-reported response rates:

Zhao et al. 2024 (PMID:39177799), verbatim:

> "The treatment of sJXG varied, including Langerhans cell histiocytosis (LCH)-based chemotherapy and targeted therapy. The overall response rate of sJXG for first-line and second-line chemotherapy was 50.0% (5/10) and 50% (4/8), respectively. ... Therefore, LCH-based chemotherapy could serve as an effective treatment for sJXG patients"

Beijing series (PMID:34178890): first-line response **40%**, second-line **66.7%**.

Agents used across series: **vinblastine + prednisone** (LCH-I/II/III backbone), **cytarabine**, **cladribine (2-CdA)**, **methotrexate/6-mercaptopurine** maintenance. **Corticosteroids and/or ruxolitinib** are used to control the hyperinflammatory state when HLH supervenes (PMID:39177799).

Zou et al. 2023 give the field's honest verdict (PMID:36779547):

> "there is no standard therapy for SJXG and clinicians should choose individualized therapy modalities."

### 12.4 Targeted therapy

| Target | Agent | Evidence | Term candidates |
|---|---|---|---|
| **BRAF V600E** | **Dabrafenib** | *"Patients with BRAF V600E mutation showed a response to dabrafenib"* (PMID:39177799); *"BRAFV600E was detected in 1 child and 1 adult with CNS-xanthogranulomas; both responded to BRAF inhibition"* (PMID:39316650) | **CHEBI:75045** dabrafenib ✅; **NCIT:C82386** Dabrafenib ✅ |
| **MEK1/2 (genotype-agnostic)** | **Cobimetinib** | Diamond et al. 2019, *Nature* (PMID:30867592), proof-of-concept trial in 18 patients with histiocytoses: *"the overall response rate was 89% (90% confidence interval of 73-100). Responses were durable, with no acquired resistance to date. At one year, 100% of responses were ongoing and 94% of patients remained progression-free. Cobimetinib treatment was efficacious regardless of genotype, and responses were observed in patients with ARAF, BRAF, RAF1, NRAS, KRAS, MEK1 ... and MEK2 ... mutations."* **Caveat: this trial enrolled histiocytoses broadly, not JXG specifically** — cite it as indirect for JXG (`directness: INDIRECT`) | **CHEBI:90851** cobimetinib ✅; **NCIT:C68923** Cobimetinib ✅ |
| **MEK1/2** | **Trametinib** | Used in paediatric histiocytosis practice; no JXG-specific trial | **CHEBI:75998** trametinib ✅; **NCIT:C77908** Trametinib ✅ |
| **ARAF** | RAF inhibition (sorafenib) | Clinical responses in ARAF-mutant non-LCH (PMID:26566875) | — |
| **NTRK1 fusion** | **TRK inhibitors (larotrectinib, entrectinib)** | **Proposed, not yet demonstrated in JXG.** Schlögl et al.: *"Given the potential of NTRK gene fusions as a therapeutic target, NTRK inhibitors may represent a novel effective treatment for JXG with a challenging clinical course"* (PMID:40235191). This is a **hypothesis**, and must be curated as one — not as a treatment with evidence | — |
| **SYK (`CLTC::SYK`)** | SYK inhibitors; mTOR inhibitors | **Hypothesis only.** Kemps et al. demonstrated pSYK, mTOR activation and cyclin D1 in situ, which is a rationale, not a result (PMID:39316650) | — |
| **ALK fusion** | *excluded — see §0(a)* | — | — |
| **mTOR** | **Sirolimus (oral)** | Two paediatric JXG cases (PMID:38444069); also topical rapamycin in two paediatric non-LCH cases | — |

### 12.5 Treatment algorithm (synthesized; no formal guideline exists)

1. **Solitary cutaneous lesion, asymptomatic** → observe. No investigations unless clinically indicated.
2. **≥2 cutaneous lesions, or onset <2 years** → clinical examination, consider ophthalmological review, FBC; observe.
3. **Ocular involvement** → topical ± periocular corticosteroid; manage IOP; bevacizumab or further measures if refractory.
4. **Extracutaneous mass, resectable, non-critical site** → excision; often curative. Consider observation alone — spontaneous regression occurs even in kinase-driven lesions.
5. **Systemic/multisystem, symptomatic or organ-threatening** → **molecular profiling with a DNA+RNA fusion-capable panel, before committing to therapy**, then:
   - BRAF V600E → BRAF inhibitor
   - Other MAPK alteration → MEK inhibitor
   - NTRK1 fusion → TRK inhibitor (investigational)
   - No actionable alteration, or urgent disease → LCH-based chemotherapy
6. **HLH supervening** → corticosteroids ± ruxolitinib for the hyperinflammatory state, alongside disease-directed therapy.
7. **NF1 + multiple JXG** → maintain awareness for JMML (FBC/film), with the screening caveat of §9.4.

### 12.6 Adverse events and pharmacogenomics

Standard class toxicities apply (MEK inhibitors: rash, diarrhoea, retinopathy, cardiomyopathy, raised CK; BRAF inhibitors: pyrexia, arthralgia, cutaneous squamous neoplasms; vinblastine: neuropathy, myelosuppression; cytarabine/cladribine: myelosuppression, immunosuppression). **No JXG-specific toxicity data and no pharmacogenomic (PharmGKB/CPIC) guidance exist for this disease.**

### 12.7 Clinical trials

No trial recruits JXG specifically. JXG patients are eligible for **histiocytosis basket trials** — the cobimetinib study (PMID:30867592) is the template, and tumour-agnostic TRK-inhibitor and RET/other kinase-inhibitor baskets are the natural homes for fusion-positive cases. The Histiocyte Society blueprint identifies *"Limited clinical trial data due to rarity"* as a core gap and calls for collaborative trial infrastructure (PMID:41178439).

---

## 13. Prevention

**There is no primary prevention for juvenile xanthogranuloma, and none is biologically plausible** — the disease arises from a sporadic somatic mutation with no known exogenous cause.

| Level | Applicable? | Content |
|---|---|---|
| **Primary prevention** | **No** | No modifiable risk factor; no vaccine; no chemoprophylaxis |
| **Secondary prevention (early detection)** | **Partially** | (i) **Ophthalmological examination** in young children with multiple cutaneous JXG — to detect iris disease before hyphema, glaucoma and amblyopia. Contested yield (§10.5). (ii) **FBC/blood film surveillance for JMML** in children with NF1 and JXG — also contested (§9.4) |
| **Tertiary prevention (preventing complications)** | **Yes — this is where prevention actually operates** | Prompt corticosteroid treatment of iris JXG prevents glaucoma and visual loss (PMID:26189188); monitoring and treating hypercalcemia prevents a documented cause of death (PMID:12717244); recognizing HLH early permits corticosteroid/ruxolitinib control (PMID:39177799); endocrine replacement for infundibular disease manages central DI |
| **Immunization** | Not applicable | No infectious component |
| **Population screening** | No | No newborn, carrier or population screening |
| **Genetic screening / PGD / prenatal testing** | **Not applicable to JXG itself** | JXG is somatic. Genetic counselling applies only to the **predisposing germline conditions** (NF1, Noonan syndrome), where standard autosomal-dominant counselling, cascade testing and reproductive options apply — and that counselling belongs in those entries |
| **Behavioural / public-health / environmental intervention** | Not applicable | — |

**Counselling content for families** (the practical "prevention" deliverable): most cutaneous lesions resolve spontaneously over 1–6 years without scarring; no lifestyle change is required; seek review for a red eye, eye rubbing, or any new systemic symptom; in NF1, report pallor, bruising or unexplained fever.

---

## 14. Other Species / Natural Disease

**No naturally occurring animal homologue of juvenile xanthogranuloma is recognized**, and no OMIA entry exists for it. This section is largely a negative, and should be curated as one.

| Item | Finding |
|---|---|
| **Taxonomy** | Human only (`NCBITaxon:9606`). No species is a natural host for this entity |
| **OMIA** | **No OMIA entry for juvenile xanthogranuloma.** The nearest OMIA record is `OMIA:000620` *Histiocytosis, malignant*, present for dog (`OMIA:000620-9615`, *Canis lupus familiaris*) and cat (`OMIA:000620-9685`, *Felis catus*) — **a different disease**, not a JXG model |
| **Breed (VBO)** | Not applicable; no breed predisposition to a JXG-like lesion is recorded |
| **Orthologous genes** | The drivers are deeply conserved: *Csf1r*, *Syk*, *Ntrk1*, *Alk*, *Braf*, *Map2k1*, *Araf*, *Nras*, *Kras*, *Ptpn11* all have mouse orthologs. Per the project's MOD-first rule, a mouse gene in an `animal_models[].genes` block takes its **`MGI:`** identifier, not `hgnc:` — read each from the Alliance before binding |
| **Natural disease in animals** | **Xanthogranulomas** *sensu lato* occur in animals — canine **ocular surface xanthogranuloma** (17-case clinicopathological series, *Vet Ophthalmol* 2020) and feline cutaneous xanthogranuloma (eyelid case reports) — but these are **lipid-laden macrophage lesions, not the JXG entity**, and they are typically associated with hyperlipidaemia. Do **not** curate them as animal models of JXG |
| **Comparative pathology** | Canine histiocytic disorders (cutaneous/systemic histiocytosis, histiocytic sarcoma) are well-characterized and have cell lines and xenograft models (PMID:34907644), but they correspond to **malignant** histiocytosis, i.e. the "M" group of the 2016 classification, not the "C" group |
| **Zoonotic potential / cross-species transmission** | **None.** Not an infectious disease |

---

## 15. Model Organisms

**This is the largest and most striking evidence gap in the disease.** No published mouse, rat, zebrafish, *Drosophila* or *C. elegans* model of juvenile xanthogranuloma was found. No JXG cell line exists in ATCC or Cellosaurus. No JXG organoid or iPSC-derived system was found.

| Model class | Status |
|---|---|
| Genetically engineered mouse (knock-in of `Csf1r`, `Braf V600E`, `Map2k1`, or a `Clathrin–Syk` fusion in a myeloid lineage) | **None reported for JXG.** Lineage-restricted `BRAF V600E` mice exist for LCH/ECD and are the obvious template |
| Patient-derived xenograft | **None.** The nearest precedent is Erdheim–Chester disease, where mutated CD34⁺ cells from patients formed disease-characteristic histiocytic lesions in xenografted mice — a directly transferable design |
| Cell line | **None.** Canine histiocytic-sarcoma and LCH lines exist (PMID:34907644), but model a different entity |
| Organoid / iPSC | **None** |
| Induced model | **None** |

**What a model would need to recapitulate**, for anyone designing one: (i) a somatic, lineage-restricted kinase activation in a monocyte–macrophage precursor; (ii) dermis-tropic accumulation of CD68⁺/CD163⁺/FXIIIa⁺/CD1a⁻ histiocytes; (iii) progressive xanthomatization and Touton giant-cell formation; and — the hard part — (iv) **spontaneous regression**, which no existing oncogene-driven histiocytosis model reproduces.

**Resources for a future model:** MGI, IMPC, KOMP, IMSR for the driver alleles; the Alliance of Genome Resources for orthology. Record `modeled_mechanisms` with `relationship: FAILS_TO_RECAPITULATE` and appropriate `divergences` for any LCH/ECD model cited by analogy — a `BRAF V600E` histiocytosis model cited for JXG is at minimum a `BOUNDARY_OMISSION` (no JXG-specific driver) and a `POPULATION_MISMATCH` (adult/LCH biology standing in for infant dermal disease).

---

## Appendix A — Ontology term candidates

Terms marked ✅ were resolved against **OLS4 on 11 November 2026** in the course of writing this report. Terms marked ✗ were written from knowledge and are **leads only** — read each from the ontology before binding, per the project's "every CURIE is read from a source in the same step it is written" rule.

| Slot | Concept | CURIE | Label | Verified |
|---|---|---|---|---|
| `disease_term` | Juvenile xanthogranuloma | **MONDO:0015534** | juvenile xanthogranuloma | ✅ |
| `mappings` | Orphanet | **ORPHA:158000** | — | ✅ (as MONDO xref) |
| `mappings` | NCIT | **NCIT:C3451** | — | ✅ (as MONDO xref) |
| `cell_types` | Lesional histiocyte | **CL:0000235** | macrophage | ✅ |
| `cell_types` | Foamy histiocyte | **CL:0000891** | foam cell | ✅ |
| `cell_types` | Foamy histiocyte (macrophage-derived) | **CL:0000517** | macrophage derived foam cell | ✅ |
| `cell_types` | Touton giant cell | **CL:0000647** | multinucleated giant cell | ✅ *(no Touton-specific term exists)* |
| `biological_processes` | MAPK driver | **GO:0000165** | MAPK cascade | ✅ |
| `biological_processes` | ERK output | **GO:0070371** | ERK1 and ERK2 cascade | ✅ |
| `biological_processes` | ERK activation | **GO:0070374** | positive regulation of ERK1 and ERK2 cascade | ✅ |
| `biological_processes` | Xanthomatization | **GO:0090077** | foam cell differentiation | ✅ |
| `biological_processes` | Xanthomatization (macrophage) | **GO:0010742** | macrophage derived foam cell differentiation | ✅ |
| Anatomy | Dermis | **UBERON:0002067** | dermis | ✅ |
| Anatomy | Iris | **UBERON:0001769** | iris | ✅ |
| `phenotypes` | Histiocytic infiltration (coarse) | **HP:0100727** | Histiocytosis | ✅ — needs `coarse_binding_basis: NO_HPO_TERM` |
| `phenotypes` | Hyphema | **HP:0011886** | Hyphema | ✅ |
| `phenotypes` | Central DI | **HP:0000863** | Central diabetes insipidus | ✅ |
| `phenotypes` | Diabetes insipidus (parent) | **HP:0000873** | Diabetes insipidus | ✅ |
| `therapeutic_agent` | Dabrafenib | **CHEBI:75045** / **NCIT:C82386** | dabrafenib / Dabrafenib | ✅ |
| `therapeutic_agent` | Cobimetinib | **CHEBI:90851** / **NCIT:C68923** | cobimetinib / Cobimetinib | ✅ |
| `therapeutic_agent` | Trametinib | **CHEBI:75998** / **NCIT:C77908** | trametinib / Trametinib | ✅ |
| `phenotypes` | Glaucoma | HP:0000501 | Glaucoma | ✗ |
| `phenotypes` | Hepatosplenomegaly | HP:0001433 | Hepatosplenomegaly | ✗ |
| Anatomy | Skin / liver / spleen / lung / CNS | UBERON:0002097 / 0002107 / 0002106 / 0002048 / 0001017 | — | ✗ |
| `treatment_term` | Surgical procedure / pharmacotherapy / chemotherapy / supportive care | NCIT:C15329 / C15986 / C15632 / C15747 | — | from the repo's own NCIT list, not re-verified |

**Do not bind** `HP:0000991` *Xanthomatosis* or its organ-specific children to JXG lesions — they assert lipid deposition, which is the wrong pathology (§3.6).

---

## Appendix B — Evidence inventory, by strength

**Primary cohorts and registries (strongest):**
- PMID:15613853 — Janssen & Harms 2005, *Am J Surg Pathol*, Kiel Pediatric Tumor Registry, n=129
- PMID:12717244 — Dehner 2003, *Am J Surg Pathol*, n=174
- PMID:34820973 — Wee et al. 2022, *Dermatol Ther*, n=147 Asian children
- PMID:39316650 — Kemps et al. 2024, *Blood*, Dutch Nationwide Pathology Databank, n=21

**Systematic reviews:**
- PMID:36779547 — Zou et al. 2023, *Pediatr Blood Cancer*, 103 articles / 159 patients
- PMID:37422708 — NF1/JXG/leukaemia systematic review, 62 articles / 177 patients

**Molecular (recent, high-value):**
- PMID:40235191 (NTRK1 fusions, 2025) · PMID:41968182 (IHC kinase screening, 2026) · PMID:26566875 (Diamond 2016) · PMID:31768065 (Durham 2019, CSF1R) · PMID:28752840 (copy number) · PMID:28504206 (BRAF V600E, CNS) · PMID:40373196 (PTPN11 clonal JXG–JMML) · PMID:34032360 (Noonan)

**Therapeutic:**
- PMID:30867592 (Diamond 2019, *Nature*, cobimetinib — **indirect** for JXG) · PMID:39177799 (sJXG + HLH, dabrafenib) · PMID:34178890 (sJXG chemotherapy) · PMID:26189188 (ocular corticosteroids) · PMID:24767830 (bevacizumab) · PMID:38444069 (sirolimus) · PMID:18338395 (Stover 2008)

**Classification and framing:**
- PMID:26966089 (Emile 2016) · PMID:41178439 (Histiocyte Society blueprint 2025)

**Imaging:**
- PMID:36265894 (CNS MRI, n=14) · PMID:41899058 (ultrasound, 2011–2025)

**Flagged as needing primary verification before quotation:** PMID:37736360 (Xu 2023, the MAP2K1 27% / KRAS 18% / NRAS 18% figures — Europe PMC returns no abstract for this record).

---

## Appendix C — Curation watch-list

1. **Do not model JXG as a metabolic or lipid-storage disease.** The lipid is downstream of the histiocytic proliferation; serum lipids are normal.
2. **Do not populate an `inheritance:` block** with a Mendelian mode, and do not bind `HP:0001442`.
3. **Do not bind xanthoma HP terms** to JXG lesions.
4. **Represent the NF1/JMML screening controversy on both sides** (§9.4), with separate evidence items.
5. **Grade the cobimetinib trial `directness: INDIRECT`** — it enrolled histiocytoses broadly, not JXG.
6. **Curate NTRK- and SYK-inhibitor use as hypotheses**, not as treatments with evidence.
7. **The `environmental:` block should be empty**, with a recorded `Left deliberately uncited.` waiver naming the searches run.
8. **Say in the PR body what §0 leaves out** (ALK-inhibitor therapeutic evidence), so the gap is visible to the next curator.
9. **Spontaneous regression of a kinase-driven neoplasm** is the entry's best `KNOWLEDGE_GAP` discussion — attach it to the regression node with `proposed_experiments`.
10. **No animal model and no cell line exist.** Leave `animal_models:` and `experimental_models:` empty rather than importing LCH/ECD models by analogy; if one is cited, use `FAILS_TO_RECAPITULATE` with typed `divergences`.

---

## Sources

- [Revised classification of histiocytoses and neoplasms of the macrophage-dendritic cell lineages (Emile et al., Blood 2016)](https://ashpublications.org/blood/article/127/22/2672/35156/Revised-classification-of-histiocytoses-and)
- [Recurrent CLTC::SYK fusions and CSF1R mutations in juvenile xanthogranuloma of soft tissue (Kemps et al., Blood 2024)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:39316650&resultType=core&format=json)
- [NTRK1 Gene Fusions Are Frequent in Juvenile Xanthogranuloma (Schlögl et al., Am J Surg Pathol 2025)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12258803/)
- [Immunohistochemistry-Based Screening for Targetable Kinase Alterations in Non-LCH with JXG morphology (Sakamoto et al., Virchows Arch 2026)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41968182&resultType=core&format=json)
- [Diverse and Targetable Kinase Alterations Drive Histiocytic Neoplasms (Diamond et al., Cancer Discov 2016)](https://doi.org/10.1158/2159-8290.Cd-15-0913)
- [Activating mutations in CSF1R and additional receptor tyrosine kinases in histiocytic neoplasms (Durham et al., Nat Med 2019)](https://pubmed.ncbi.nlm.nih.gov/31768065/)
- [Efficacy of MEK inhibition in patients with histiocytic neoplasms (Diamond et al., Nature 2019)](https://pubmed.ncbi.nlm.nih.gov/30867592/)
- [Genetic evaluation of juvenile xanthogranuloma (Paxton et al., Mod Pathol 2017)](https://www.nature.com/articles/modpathol201750)
- [Juvenile xanthogranulomas in the first two decades of life (Dehner, Am J Surg Pathol 2003)](https://pubmed.ncbi.nlm.nih.gov/12717244/)
- [Juvenile xanthogranuloma in childhood and adolescence: Kiel Pediatric Tumor Registry (Janssen & Harms, Am J Surg Pathol 2005)](https://pubmed.ncbi.nlm.nih.gov/15613853/)
- [Juvenile xanthogranulomas in Asian children (Wee et al., Dermatol Ther 2022)](https://onlinelibrary.wiley.com/doi/10.1111/dth.15224)
- [Systemic juvenile xanthogranuloma: A systematic review (Zou et al., Pediatr Blood Cancer 2023)](https://onlinelibrary.wiley.com/doi/full/10.1002/pbc.30232)
- [Clinical features and outcomes of 17 children with systemic JXG including five with HLH (Zhao et al., Ann Hematol 2024)](https://pubmed.ncbi.nlm.nih.gov/39177799/)
- [Clinical Analysis of Pediatric Systemic Juvenile Xanthogranulomas (Front Pediatr 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8222597/)
- [Juvenile xanthogranuloma: forms of systemic disease and their clinical implications (Freyer et al., J Pediatr 1996)](https://pubmed.ncbi.nlm.nih.gov/8765620/)
- [Juvenile Xanthogranuloma Involving the Eye and Ocular Adnexa (Samara et al., Ophthalmology 2015)](https://pubmed.ncbi.nlm.nih.gov/26189188/)
- [Neuroimaging in Pediatric Patients with Juvenile Xanthogranuloma of the CNS (Serrallach et al., AJNR 2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9731252/)
- [Juvenile xanthogranuloma, neurofibromatosis, and juvenile chronic myelogenous leukemia: world statistical analysis (Zvulunov et al., Arch Dermatol 1995)](https://pubmed.ncbi.nlm.nih.gov/7632061/)
- [The association between JXG in NF1 patients and the development of leukemia: a systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10774451)
- [The relationship between NF1, juvenile xanthogranuloma, and malignancy (Liy-Wong et al., JAAD 2017)](https://pubmed.ncbi.nlm.nih.gov/28189268/)
- [Clonal relationship between JXG and JMML: insights from a PTPN11 missense variant (Kobal et al., Clin Exp Dermatol 2025)](https://pubmed.ncbi.nlm.nih.gov/40373196/)
- [Juvenile Xanthogranuloma in Noonan Syndrome (Ali et al., Am J Med Genet A 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8446294/)
- [BRAF V600E mutation in pediatric intracranial and cranial juvenile xanthogranuloma (Techavichit et al., Hum Pathol 2017)](https://www.sciencedirect.com/science/article/abs/pii/S0046817717301569)
- [NTRK expression is common in xanthogranuloma and is associated with the solitary variant (Umphress et al., J Cutan Pathol 2023)](https://onlinelibrary.wiley.com/doi/full/10.1111/cup.14510)
- [Histiocyte Society blueprint for non-Langerhans cell histiocytosis research (Haematologica 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12580693/)
- [The 5th edition of the WHO Classification of Haematolymphoid Tumours: Myeloid and Histiocytic/Dendritic Neoplasms](https://pmc.ncbi.nlm.nih.gov/articles/PMC9252913/)
- [A Retrospective Study of the Ultrasound Imaging Characteristics of Juvenile Xanthogranuloma (J Clin Med 2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13027259/)
- [Juvenile Xanthogranuloma of the Head and Neck: Imaging Findings in 11 Cases (J Pediatr Hematol Oncol 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11268553/)
- [Oral sirolimus for the treatment of juvenile xanthogranuloma (Pediatr Dermatol 2024)](https://pubmed.ncbi.nlm.nih.gov/38444069/)
- [Successful treatment of juvenile xanthogranuloma using bevacizumab (J AAPOS 2014)](https://pubmed.ncbi.nlm.nih.gov/24767830/)
- [Treatment of juvenile xanthogranuloma (Stover et al., Pediatr Blood Cancer 2008)](https://pubmed.ncbi.nlm.nih.gov/18338395/)
- [ALK-positive histiocytosis: an expanded clinicopathologic spectrum and frequent presence of KIF5B-ALK fusion (Mod Pathol 2019)](https://www.nature.com/articles/s41379-018-0168-6)
- [Juvenile xanthogranuloma — DermNet NZ](https://dermnetnz.org/topics/juvenile-xanthogranuloma)
- [Juvenile Xanthogranuloma — StatPearls, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK526103/)
- [A clinicopathological study of 17 cases of ocular surface xanthogranuloma in dogs (Vet Ophthalmol 2020)](https://onlinelibrary.wiley.com/doi/10.1111/vop.12711)
- [OMIA:000620 Histiocytosis, malignant](https://omia.org/OMIA000620/)
- [Cell lines and xenograft mouse models of canine systemic histiocytosis and disseminated histiocytic sarcoma (Vet Comp Oncol 2022)](https://pubmed.ncbi.nlm.nih.gov/34907644/)
- [Is the setting sun dermoscopic pattern specific to juvenile xanthogranuloma? (JAAD)](https://www.jaad.org/article/S0190-9622(17)32608-7/fulltext)
- [Structural correlations between dermoscopic and histopathological features of juvenile xanthogranuloma](https://pubmed.ncbi.nlm.nih.gov/20698915/)
- [Activating MAPK1 (ERK2) mutation in an aggressive case of disseminated juvenile xanthogranuloma (Oncotarget 2017)](https://doi.org/10.18632/oncotarget.17521)
- [EMBL-EBI Ontology Lookup Service (OLS4) — MONDO, HP, GO, CL, UBERON, CHEBI, NCIT term verification](https://www.ebi.ac.uk/ols4/)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 47 |
| On topic | 36 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 22 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:4424` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **juvenile xanthogranuloma**
- `NCIT:C3451` (2 mentions) - the report calls it "NCIT"; NCIT calls it **Juvenile Xanthogranuloma**
- `EFO:1000311` (1 mention) - the report calls it "EFO"; EFO calls it **obsolete_Juvenile Xanthogranuloma**
- `GO:0070371` (2 mentions) - the report calls it "ERK output"; GO calls it **ERK1 and ERK2 cascade**
- `GO:0070374` (2 mentions) - the report calls it "ERK activation"; GO calls it **positive regulation of ERK1 and ERK2 cascade**
- `GO:0090077` (2 mentions) - the report calls it "Xanthomatization"; GO calls it **foam cell differentiation**
- `GO:0010742` (2 mentions) - the report calls it "Xanthomatization (macrophage)"; GO calls it **macrophage derived foam cell differentiation**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `EFO:1000311` (obsolete_Juvenile Xanthogranuloma) (1 mention) - replaced by `http://purl.obolibrary.org/obo/MONDO:0015534`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000953` (1 mention) - the report calls it "hyperpigmentation; **unverified"; HP calls it **Hyperpigmentation of the skin**, and lists "Skin hyperpigmentation" among its other names
- `HP:0000863` (2 mentions) - the report calls it "Central DI"; HP calls it **Central diabetes insipidus**
- `HP:0000873` (2 mentions) - the report calls it "Diabetes insipidus (parent)"; HP calls it **Diabetes insipidus**
- `HP:0100727` (3 mentions) - the report calls it "Histiocytic infiltration (coarse)"; HP calls it **Histiocytosis**
- `GO:0000165` (2 mentions) - the report calls it "MAPK driver"; GO calls it **MAPK cascade**
- `CL:0000235` (2 mentions) - the report calls it "Lesional histiocyte"; CL calls it **macrophage**, and lists "histiocyte" among its other names
- `CL:0000891` (2 mentions) - the report calls it "Foamy histiocyte"; CL calls it **foam cell**
- `CL:0000517` (2 mentions) - the report calls it "Foamy histiocyte (macrophage-derived)"; CL calls it **macrophage derived foam cell**
- `CL:0000647` (3 mentions) - the report calls it "Touton giant cell"; CL calls it **multinucleated giant cell**, and lists "multinucleate giant cell" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIA`, `EXT_ID`.