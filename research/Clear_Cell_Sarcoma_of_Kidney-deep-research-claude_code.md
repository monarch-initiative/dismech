---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-10-28T18:35:49.771068'
end_time: '2026-10-28T19:00:56.766268'
duration_seconds: 1507.0
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Clear Cell Sarcoma of Kidney
  mondo_id: MONDO:0005006
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: CCSK; childhood clear cell sarcoma of the kidney; childhood kidney clear
    cell sarcoma; childhood renal clear cell sarcoma; clear cell sarcoma - kidney;
    clear cell sarcoma of the kidney; kidney clear cell sarcoma; paediatric kidney
    clear cell sarcoma
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
  web_search_requests: 36
  num_turns: 133
  total_cost_usd: 20.005220250000004
  session_id: 3332cf38-402f-4ed5-a70a-cc78d1093358
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 36
reference_validation:
  total_references: 76
  verified: 76
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 33
  quotes_valid: 23
  quotes_unsupported: 10
  unsupported_quote_references:
  - PMID:29485128
  - PMID:26158413
  - PMID:24937667
  - PMID:38396300
  - PMID:30917048
  - PMID:16299227
  relevance_assessed: 76
  on_topic: 57
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 106
  verified: 99
  not_found: 0
  obsolete: 3
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0005006
    reported_labels:
    - Mondo
    ontology_label: clear cell sarcoma of kidney
  - term_id: NCIT:C4264
    reported_labels:
    - NCIT
    ontology_label: Clear Cell Sarcoma of the Kidney
  - term_id: DOID:4880
    reported_labels:
    - DOID
    ontology_label: kidney clear cell sarcoma
  - term_id: EFO:0000350
    reported_labels:
    - EFO
    ontology_label: obsolete_clear cell sarcoma of the kidney
  obsolete_terms:
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  - term_id: EFO:0000350
    ontology_label: obsolete_clear cell sarcoma of the kidney
    replaced_by: http://purl.obolibrary.org/obo/MONDO:0005006
  - term_id: NCIT:C16722
    ontology_label: Immunohistochemistry
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  - OMIA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Clear Cell Sarcoma of Kidney
- **MONDO ID:** MONDO:0005006 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** CCSK; childhood clear cell sarcoma of the kidney; childhood kidney clear cell sarcoma; childhood renal clear cell sarcoma; clear cell sarcoma - kidney; clear cell sarcoma of the kidney; kidney clear cell sarcoma; paediatric kidney clear cell sarcoma
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Clear Cell Sarcoma of Kidney** covering all of the
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

# Comprehensive Research Report: Clear Cell Sarcoma of the Kidney (CCSK)

**Target disease:** Clear cell sarcoma of kidney
**MONDO:** `MONDO:0005006` (label: *clear cell sarcoma of kidney*)
**Causal gene (somatic):** **BCOR** (`hgnc:20893`, BCL6 corepressor, Xp11.4) — recurrent in-frame **internal tandem duplication (ITD) of exon 15**, present in ~85–90% of cases. Minority alternatives: **YWHAE::NUTM2B/E** fusion from t(10;17)(q22;p13) (~10–12%) and **BCOR::CCNB3** fusion (rare).
**Report date:** 28 October 2026

---

## Provenance and verification notes (read first)

1. **CCSK is a somatic-driver paediatric sarcoma, not a Mendelian disorder.** The BCOR ITD is acquired: Roy et al. showed "*Identical ITD mutations are found in primary and relapsed tumour pairs but not in adjacent normal kidney or blood*" (PMID:26573325). There is **no recognised germline predisposition syndrome** for CCSK. Sections of this template that presuppose inheritance (penetrance, carrier frequency, anticipation, consanguinity, prenatal/carrier screening) are **not applicable** and are marked as such rather than filled speculatively.
2. **The disease name does not name its gene.** The name "clear cell sarcoma of *kidney*" collides with two unrelated entities that must not be conflated during curation: (a) **clear cell sarcoma of soft tissue / of tendons and aponeuroses**, driven by *EWSR1::ATF1*; and (b) **clear cell renal cell carcinoma**, a *VHL*-driven adult epithelial carcinoma. Several search hits for "clear cell sarcoma kidney" return one of these. All content below is anchored to `MONDO:0005006` / `NCIT:C4264`.
3. **Quote discipline.** Text shown in quotation marks below was returned inside quotation marks by the retrieval step from the cited abstract. Where my retrieval returned a *summary* of an abstract rather than its full text, I have written the content as paraphrase and said so. **Before any of these strings is used as a dismech `snippet:`, it must be re-verified against a freshly fetched `references_cache/PMID_*.md`** (`just fetch-reference PMID:…`, then `just count-verified-snippets`). I have not fetched any reference into the cache in this session.
4. **Every ontology CURIE below was looked up in this session** — against `cache/<prefix>/terms.csv` in this checkout, the EBI OLS4 API, or the HGNC REST API — and is reported with the label the authority returned. Two lookups failed usefully and are recorded: `GO:0006306` *DNA methylation* is **obsolete** (do not bind it), and there is **no GO biological-process term for histone H2AK119 monoubiquitination** (only the molecular function `GO:0140862`). `NCIT:C4264` is not yet in this checkout's NCIT cache and was resolved via OLS4.

---

## 1. Disease Information

### Overview

Clear cell sarcoma of the kidney (CCSK) is a rare, aggressive malignant **mesenchymal** (non-epithelial, non-blastemal) renal neoplasm of early childhood. It is conventionally described as the **second most common renal malignancy of childhood after Wilms tumour**, accounting for roughly **2–5% of paediatric renal tumours** (PMID:26573325, PMID:22579455). A SEER analysis ranked it **third by incidence among all paediatric renal tumours** (PMID:34095035) — both statements appear in the literature and the discrepancy reflects whether benign/borderline entities (congenital mesoblastic nephroma) and renal cell carcinoma are counted.

The tumour was historically known as "**bone-metastasising renal tumour of childhood**", and was separated from Wilms tumour by Beckwith and Palmer in 1978 on the basis of its distinctive histology and relapse pattern. It is characterised by a **unilateral, unicentric** mass centred on the **renal medulla**, a tendency to **vascular invasion**, and a propensity for **late relapse to bone and, in the modern treatment era, especially to brain**.

MONDO's own definition (retrieved from OLS4, identical to the NCIT definition plus the BCOR clause):

> "A rare pediatric sarcoma affecting the kidney. It is characterized by the presence of epithelioid or spindle cells forming cords or nests, separated by fibrovascular septa. It is associated with internal tandem duplications in the BCOR gene. It metastasizes to lung, bone, brain and soft tissue."

### Key identifiers

| Resource | Identifier | Label |
|---|---|---|
| **Mondo** | `MONDO:0005006` | clear cell sarcoma of kidney |
| **NCIT** | `NCIT:C4264` | Clear Cell Sarcoma of the Kidney |
| **Orphanet** | `ORPHA:457246` | Clear cell sarcoma of kidney |
| **ICD-O-3 morphology** | 8964/3 | Clear cell sarcoma of kidney |
| **ICD-10** | C64 | Malignant neoplasm of kidney, except renal pelvis |
| **ICD-11** | 2C90.Y + XH0765 | Other specified malignant neoplasms of kidney, except renal pelvis + clear cell sarcoma of kidney (morphology) |
| **UMLS** | C0334488 | — |
| **DOID** | DOID:4880 | — |
| **EFO** | EFO:0000350 | — |
| **MedGen** | 90791 | — |
| **GARD** | 0021905 | — |
| **OncoTree** | CCSK | — |
| **OMIM** | *none* | No OMIM disease entry (somatic tumour). The gene has `OMIM:300485` BCL6 COREPRESSOR; BCOR |

All Mondo xrefs above were retrieved from the OLS4 MONDO record for `MONDO_0005006` in this session.

**MeSH:** There is **no dedicated MeSH descriptor for CCSK**. It indexes under *Kidney Neoplasms* (D007680) and *Sarcoma, Clear Cell* / *Sarcoma* (D012509). I could not find a CCSK-specific MeSH heading; do not invent one.

### Synonyms

CCSK (abbreviation); childhood clear cell sarcoma of the kidney; childhood kidney clear cell sarcoma; childhood renal clear cell sarcoma; clear cell sarcoma of the kidney; kidney clear cell sarcoma; paediatric/pediatric kidney clear cell sarcoma; paediatric/pediatric renal clear cell sarcoma; renal clear cell sarcoma. Historical: **bone-metastasising renal tumour of childhood**. (MONDO + NCIT synonym sets, retrieved via OLS4.)

### Evidence provenance type

**Aggregated disease-level**, not EHR/individual-patient. The authoritative sources are (i) central-pathology-reviewed cooperative-group cohorts — NWTS 1–5 (PMID:10632483, PMID:14752069, PMID:30255545), COG AREN03B2/AREN0321 (PMID:38396300), SIOP 93-01/2001 (PMID:23880476); (ii) population registries — SEER (PMID:34095035); and (iii) molecular case series. No EHR-derived phenotype profile exists for CCSK, so **no `kb/phenotype_distributions/` entry should be assembled from this report**.

---

## 2. Etiology

### Disease causal factors

CCSK is a **genetically driven somatic neoplasm with a strikingly quiet genome**. Three mutually exclusive driver classes account for ~88–100% of cases depending on cohort and assay:

1. **BCOR exon 15 internal tandem duplication (ITD)** — the dominant driver.
   - Ueno-Yokohata et al. (PMID:26098867, *Nat Genet* 2015), verbatim abstract: "*We identified internal tandem duplications in the BCOR gene (BCL6 corepressor) affecting the C terminus in 100% (20/20) of CCSK tumors but in none (0/193) of the other pediatric renal tumors. CCSK tumors expressed only an aberrant BCOR allele, indicating a close correlation between BCOR aberration and CCSK tumorigenesis.*"
   - Roy et al. (PMID:26573325, *Nat Commun* 2015), verbatim: "*…somatic internal tandem duplications (ITDs) clustering in the C terminus of BCOR in 23 of 27 (85%) pediatric clear cell sarcomas of the kidney (CCSK) from two independent cohorts.*"
   - Astolfi et al. (PMID:26516930, *Oncotarget* 2015), verbatim: "*Three different in-frame ITD in exon15 of BCOR, were detected. The presence of the ITD was confirmed on tumor DNA and cDNA, and resulted in overexpression of BCOR.*"
   - Independent confirmation: 10/11 (90.9%) by NGS (PMID:28833375); 34/39 (87.18%) by PCR/FISH/Sanger (PMID:36563883).
2. **YWHAE::NUTM2B/E fusion** from **t(10;17)(q22;p13)** — ~10–12%.
   - O'Meara et al. (PMID:22294382, *J Pathol* 2012) mapped the breakpoints to 17p13.3 and 10q22.3 and reported "*an in-frame fusion transcript of ∼3 kb, incorporating exons 1-5 of YWHAE and exons 2-7 of FAM22*" (FAM22B/FAM22E = NUTM2B/NUTM2E), found in 6/50 (12%) additional CCSKs.
3. **BCOR::CCNB3 fusion** — rare. First reported in a kidney presenting as CCSK by Wong et al. (PMID:28833375); further cases reported (e.g. PMID:36533315).

**Mutual exclusivity is established.** Karlsson et al. (PMID:26493387) concluded that the "*YWHAE–NUTM2B/E fusion and the BCOR ITD are mutually exclusive events and activated different downstream signaling systems*"; Zhang et al. (PMID:36563883) confirmed "*BCOR ITD, YWHAE rearrangement and BCOR-CCNB3 were mutually exclusive*" in 39 cases.

**A "double-negative" subset persists.** Kenny et al. (PMID:27000436, *J Pathol* 2016) analysed 159 CCSKs, confirmed mutual exclusivity, and found that **11.8% carried neither alteration** by their assays, "*raising the possibility of distinct aetiologies for subsets of CCSK*", with associated clinical differences. Zhang et al. likewise reported 3/39 (7.69%) with none of the three. Some double-negative cases are resolved by newer assays detecting **long spliced ITDs** (PMID:35836306) or by *BCOR::MAML3* (PMID:39871307); others are reclassified on review (e.g. malignant solitary fibrous tumour — see §10).

**Secondary/cooperating lesion — TP53.** Zhang et al. (PMID:36563883, *Hum Pathol* 2023), verbatim: "*25.64% of the cohort acquired TP53 aberration (10/39, 3 with both copy number deletion and point mutation, 6 with deletion only, and 1 with mutation only), all of which were associated with BCOR ITD… Patients with both BCOR ITD and TP53 deletion had the poorest prognosis.*" TP53 (`hgnc:11998`) is therefore a **cooperating somatic lesion and candidate prognostic marker**, not a second driver class.

**Epigenetic co-lesion — TCF21 silencing.** See §4 and §6.

### Risk factors

**Genetic risk factors**
- **Causal somatic variants**: as above. These are tumour-restricted.
- **Germline susceptibility loci**: **none identified.** Gooskens et al. (PMID:26158413) found "*No recurrent segmental chromosomal copy number changes or somatic variants (single nucleotide or small insertion/deletion)*" beyond the fusion case; Fiore et al. (PMID:36835166) performed WES on nine BCOR-ITD CCSKs and reported "*No significant recurrents of somatic or germline mutations other than BCOR-ITD were identified among the evaluated samples*", confirming "*this tumor carries a low mutational burden*".
- **Modifier genes**: none established.
- **Relationship to germline BCOR disease — important and frequently muddled.** Germline **loss-of-function** BCOR variants cause **oculofaciocardiodental (OFCD) syndrome** / syndromic microphthalmia 2 (`OMIM:300166`), X-linked dominant with male lethality. CCSK has **not been reported as a feature of OFCD**, and the CCSK lesion is a *different kind of allele* (an in-frame duplication within PUFD, with retained/over-expressed protein) rather than a truncation. Note honestly: a single OFCD patient with T-cell lymphoma has been reported and reviews raise the possibility of a modest cancer risk in OFCD, but there is **no evidence of CCSK predisposition**, and absence of reports is not the same as demonstrated absence of risk. Do not curate a germline predisposition claim.

**Environmental risk factors**
**No established environmental, occupational, dietary, radiation, or infectious risk factor** has been identified for CCSK. The only reproducible demographic risk associations are host-constitutional:
- **Male sex** — SEER incidence rate ratio **3** for boys (PMID:34095035); M:F ≈ **2:1** in NWTS (PMID:10632483); 64% male in SIOP (PMID:23880476); 69% male on NWTS-5 (PMID:30255545).
- **Age under 4 years** — SEER incidence rate ratio **21** for children ≤4 years (PMID:34095035).
- **Family history** — no familial clustering reported.

This is a genuine negative and should be curated as such rather than left blank. Any dismech `environmental:` entry for CCSK should carry the `review_notes:` waiver sentinel (`Left deliberately uncited.` followed by ≥20 words naming the searches run), because no quotable exposure evidence exists.

### Protective factors

**None identified** — genetic or environmental. There are no protective alleles, no dietary/lifestyle exposures, and no chemopreventive strategies reported for CCSK. Given its early-childhood onset and somatic-driver biology, primary prevention is not a meaningful concept (see §13).

### Gene–environment interactions

**None described.** No GxE analyses exist for CCSK; the cohort sizes (largest molecular series 159 tumours) are far below what such analysis would require.

---

## 3. Phenotypes

CCSK's clinical phenotype is that of a large unilateral renal mass in a toddler. Frequencies below are drawn from the clinicopathological series cited; **where a precise frequency is not published I say so rather than estimate one.**

### Presenting features (symptoms and clinical signs)

| Phenotype | HPO suggestion (verified) | Frequency | Source |
|---|---|---|---|
| Palpable abdominal mass | `HP:0031500` Abdominal mass | **Most common presentation; usual presenting sign** | PMID:22579455, PMID:30917048, PMID:41644425 |
| Abdominal distension | `HP:0003270` Abdominal distention | Common; frequency not quantified | PMID:22579455 |
| Abdominal pain | `HP:0002027` Abdominal pain | Common; frequency not quantified | PMID:22579455 |
| Flank pain | `HP:0030157` Flank pain | Reported | PMID:22579455 |
| Haematuria | `HP:0000790` Hematuria | A usual presenting sign; frequency not quantified | PMID:22579455, PMID:30917048 |
| Hypertension | `HP:0000822` Hypertension | Reported | PMID:22579455 |
| Anaemia | `HP:0001903` Anemia | Reported | PMID:22579455 |
| Pallor | `HP:0000980` Pallor | Reported | PMID:22579455 |
| Fatigue | `HP:0012378` Fatigue | Reported | PMID:22579455 |
| Fever | `HP:0001945` Fever | Occasional, low-grade | PMID:22579455 |
| Vomiting | `HP:0002013` Vomiting | Reported | PMID:22579455 |
| Weight loss | `HP:0001824` Weight loss | Reported | PMID:22579455 |
| Hydronephrosis (from pelvic compression) | `HP:0000126` Hydronephrosis | Radiological finding | case-report literature, e.g. PMID:42016619 |
| Renal neoplasm (the lesion itself) | `HP:0009726` Renal neoplasm | 100% by definition | — |
| Sarcoma (histological class) | `HP:0100242` Sarcoma | 100% by definition | — |

### Metastatic and relapse phenotypes

| Phenotype | HPO suggestion (verified) | Frequency | Source |
|---|---|---|---|
| Distant metastasis at diagnosis (stage IV) | — | **~4–15%**: 7.6% (10/132, AREN0321, PMID:38396300); 7% (SIOP, PMID:23880476); 6.5% (7/108, NWTS-5, PMID:30255545); 15% (8/54, Shanghai, PMID:38980838); 14% with distant metastasis in SEER (PMID:34095035) | multiple |
| Brain metastasis / CNS relapse | `HP:0030692` Brain neoplasm | **Most common relapse site in the modern era.** 13/35 relapse sites in SIOP/AIEOP (PMID:24937667); 12/23 recurrences on NWTS-5 (PMID:30255545); 9/15 (60%) relapses on AREN0321/AREN03B2 (PMID:38396300) | multiple |
| Bone metastasis / bone pain / pathological fracture | `HP:0010622` Neoplasm of the skeletal system; `HP:0002653` Bone pain; `HP:0002756` Pathologic fracture | Historically the signature site ("bone-metastasising renal tumour of childhood"); 5/35 relapses (PMID:24937667); 3/15 (PMID:38396300); bone involvement in 9.6% in a renal-sarcoma cohort (PMID:41509607) | multiple |
| Lung metastasis | `HP:0002113` Pulmonary infiltrates (imperfect; HPO has no clean "pulmonary metastasis" term — flag as `NO_HPO_TERM` if bound coarsely) | 7/35 relapses (PMID:24937667); 1/15 (PMID:38396300); 6/8 stage IV sites (PMID:38980838) | multiple |
| Lymph-node involvement | `HP:0002716` (not verified — do not bind without lookup) | Common in stage III; lymph node metastasis 1/7 in YWHAE-rearranged series (PMID:41644425) | PMID:41644425 |
| Inferior vena cava thrombus | — (no verified HPO term found) | **6/54 (11%)**, an adverse prognostic factor (EFS 41.7%, p=0.028) | PMID:38980838 |
| Tumour rupture | — | 5/54 (9%); **independent adverse factor (HR 5.9, p=0.01)** | PMID:38980838 |
| Headache / seizure (from CNS relapse) | `HP:0002315` Headache; `HP:0001250` Seizure | Secondary to brain relapse; not quantified | PMID:22579455 |
| Lethargy | `HP:0001254` Lethargy | Reported | PMID:22579455 |

Rare/unusual metastatic sites reported include scalp, neck, nasopharynx, axilla, orbit and epidural space (reviewed in PMID:22579455); a stage IV case with intra-orbital and cervical nodal disease is in PMID:38980838.

### Phenotype characteristics

- **Age of onset:** **early childhood**, peak **2–4 years**. Mean age at diagnosis in the NWTS series was **36 months (range 2 months – 14 years)** (PMID:10632483); median 2.6 years in SIOP (PMID:23880476); median **22 months** on NWTS-5 (PMID:30255545); median **37 months** in the Shanghai cohort (PMID:38980838); mean 2.0 years in the YWHAE-rearranged series (PMID:41644425). **Neonatal** cases exist (e.g. PMC4420453). **Adult cases are genuine but exceptional** — a reported adult series had mean age 34.5 years (range 16–70), with a 62-year-old among the oldest (PMC6823942); the molecular status (BCOR ITD, YWHAE fusion, TCF21 methylation) of adult CCSK is **largely uncharacterised**, which is itself a knowledge gap.
- **Severity:** **severe** — a malignant neoplasm requiring trimodal therapy. Worse than favourable-histology Wilms tumour stage-for-stage.
- **Progression:** **progressive** if untreated; after treatment the natural history is one of **remission with risk of late relapse**. On NWTS-5, "*Twenty of the 23 disease-related events occurred within three years of initial treatment*" (PMID:30255545) and on AREN0321/AREN03B2 "*Fourteen relapses (93.3%) occurred within 3 years of diagnosis*" (PMID:38396300) — so the classic "late relapse" reputation has been compressed by modern therapy, as Aldera & Pillay note: improved chemotherapy has reduced late relapses and **brain now surpasses bone** as the commonest relapse site (PMID:30917048).
- **Onset pattern:** **subacute to insidious** — the mass is typically found by a carer or on examination rather than presenting acutely, with the caveat that rupture, IVC thrombus or pathological fracture can be an acute presentation.
- **Laterality:** **unilateral and unicentric**. Argani et al. found no case of multicentric origin among 351 (PMID:10632483); bilateral CCSK is extraordinary (a single first-reported case in *J Pediatr Surg*). Only 1/351 was associated with perilobar nephrogenic rests and none with intralobar rests (PMID:10632483) — a meaningful contrast with Wilms tumour.

### Quality-of-life impact

**No CCSK-specific QoL instrument data exist.** No EQ-5D, SF-36, PROMIS or PedsQL study of CCSK survivors was found. The relevant burden is therefore inferred from the treatment, not measured in this disease: nephrectomy (single-kidney status), **anthracycline cardiotoxicity**, abdominal/flank irradiation in a child under 4 (growth, gonadal and renal consequences), alkylator-related gonadotoxicity, and the neurocognitive consequences of CNS relapse and its treatment. One review explicitly flags that CCSK regimens "*rely on doxorubicin, which is associated with side effects of cardiotoxicity, nephrotoxicity, and fertility risks*" (treatment-rationale literature, PMID:29485128 context). **Curate this as a knowledge gap (`kind: KNOWLEDGE_GAP`) rather than as phenotype content.**

---

## 4. Genetic / Molecular Information

### Causal genes

| Gene | HGNC (dismech lowercase form) | Locus | Role in CCSK | OMIM gene |
|---|---|---|---|---|
| **BCOR** | `hgnc:20893` | Xp11.4 | Exon 15 in-frame ITD in PUFD domain; ~85–90% | `OMIM:300485` |
| **YWHAE** | `hgnc:12851` | 17p13.3 | 5′ partner of t(10;17) fusion; ~10–12% | — |
| **NUTM2B** | `hgnc:23445` | 10q22.3 | 3′ fusion partner (= FAM22B) | — |
| **NUTM2E** | `hgnc:23448` | 10q22 | alternative 3′ partner (= FAM22E) | — |
| **CCNB3** | `hgnc:18709` | Xp11.22 | 3′ partner in rare *BCOR::CCNB3* | — |
| **MAML3** | `hgnc:16272` | 4q31.1 | 3′ partner in rare *BCOR::MAML3* (assay target, PMID:39871307) | — |
| **TP53** | `hgnc:11998` | 17p13.1 | Cooperating deletion/mutation in ~26%, all on a BCOR-ITD background | — |
| **TCF21** | `hgnc:11632` | 6q23.2 | Epigenetically silenced candidate tumour suppressor | — |

Mechanistic partners of BCOR in PRC1.1: **PCGF1** `hgnc:17615`, **KDM2B** `hgnc:13610`, **RNF2** (RING1B) `hgnc:10061`, **BCL6** `hgnc:1001`. Downstream/profiling genes: **CCND1** `hgnc:1582`, **EZH2** `hgnc:3527`, **FGF3** `hgnc:3681`, **VEGFA** `hgnc:12680`, **SPP1** `hgnc:11255`, **ADM** `hgnc:259`, **JUND** `hgnc:6206`, **NTRK3** `hgnc:8033`, **EGFR** `hgnc:3236`, **KIT** `hgnc:6342`, **NGFR** `hgnc:7809`, **SATB2** `hgnc:21637`, **TLE1** `hgnc:11837`, **BCL2** `hgnc:990`, **NCAM1** `hgnc:7656`, **PITX1** `hgnc:9004`, **WNT11** `hgnc:12776`, **GATA6** `hgnc:4174`. (All resolved via HGNC REST or `cache/hgnc/terms.csv` in this session.)

### Pathogenic variants

**Variant type/class — BCOR ITD.** An **in-frame internal tandem duplication** in the 3′ portion of the **last exon (exon 15)**, encoding the **PUFD domain** (PCGF Ub-like fold discriminator). Reported duplication sizes:
- Astolfi et al.: "*the ITDs lead to the insertion of 96, 90, and 113 nucleotides in the 3' end of exon 15 of BCOR*", all in-frame, inserting **30–38 amino acids** into PUFD (PMID:26516930).
- Across the broader BCOR-ITD tumour family, duplications insert **20–40 residues** within PUFD, mapping specifically to the **N- or C-terminal β-strands / disordered PUFD termini** (PMID:32628469).

**Variant classification.** These are **somatic oncogenic driver alterations** in a tumour. The ACMG/AMP germline framework does **not** apply; the appropriate framework is AMP/ASCO/CAP somatic tiering, where BCOR ITD in a paediatric renal mesenchymal tumour is a **Tier I diagnostic** biomarker (defining a WHO entity) with no current therapeutic tier. ClinVar is not the right resource; **COSMIC / cBioPortal / OncoKB** are.

**Allele frequency in population databases.** **Not applicable** — somatic, tumour-restricted. gnomAD, 1000 Genomes, TOPMed and dbSNP have no CCSK-relevant entry. Do **not** curate an allele frequency.

**Somatic vs germline.** **Somatic, definitively.** "*Identical ITD mutations are found in primary and relapsed tumour pairs but not in adjacent normal kidney or blood*" (PMID:26573325). ITD acquisition appears to be an **early, clonal, truncal event** — present in all samples analysed and conserved between primary and relapse.

**Functional consequences — unresolved and worth curating as a hypothesis, not a fact.** Three observations must be held together:
1. **The mutant protein is over-expressed, not lost.** "*Mutant BCOR transcripts and proteins are markedly upregulated in ITD-positive tumours*" (PMID:26573325); "*resulted in overexpression of BCOR*" (PMID:26516930); "*CCSK tumors expressed only an aberrant BCOR allele*" (PMID:26098867). In the one *BCOR::CCNB3* CCSK, BCOR expression was **markedly** elevated versus the lower elevation in ITD cases (PMID:28833375).
2. **Structural work predicts loss of PRC1.1 assembly.** The PUFD termini are disordered and become ordered on PCGF1 binding, which then licenses KDM2B association; tumour ITDs map to exactly those termini, and binding studies indicate "*the ITD would disrupt PRC1.1 assembly, suggesting loss of the ability to assemble PRC1.1 is a critical molecular event driving tumorigenesis*" (PMID:32628469, paraphrased from retrieval).
3. **A 2025 cell-based study contradicts the simple disassembly model.** Dhoondia et al. (PMID:40646718, *Genetics* 2025) engineered BCOR-ITD into mouse ES cells and found BCOR-ITD **retained** robust PCGF1 interaction and intact vPRC1.1 composition — "*All vPRC1.1 components were among the top 3% of enriched proteins, unexpectedly detecting no major shifts in the composition of vPRC1.1 associated with ITD mutants*" — with H2AK119ub unaffected and only 32 up / 83 down differentially expressed genes at day 6 of neural differentiation, versus 344 up for a truncating BCOR mutant. Their conclusion: "*BCOR-ITD may largely retain wildtype function, but with increased susceptibility to synergistic stress on the Polycomb pathway*", unmasked only on PRC2 inhibition.

So the honest summary is: **the ITD is best described as a hypomorphic / context-dependent partial loss-of-function allele of a PRC1.1 scaffold, with a possible neomorphic component, and the loss-of-function-versus-gain-of-function question is open.** In dismech terms this is an entry for `mechanistic_hypotheses` with `status: EMERGING`, plus a `HUMAN_MODEL_MISMATCH` discussion (the mES/NSC models are not renal and give discordant answers), **not** a settled `functional_impact_category`. If one value must be chosen for the ITD, `PARTIAL_LOSS_OF_FUNCTION` is better supported than `LOSS_OF_FUNCTION` or `GAIN_OF_FUNCTION`.

**Functional consequence — YWHAE::NUTM2B/E.** An in-frame fusion of YWHAE exons 1–5 (14-3-3ε, a phosphoserine-binding adaptor) to NUTM2B/E exons 2–7 (PMID:22294382). Karlsson et al. showed it "*activated different downstream signaling systems*" from the ITD (PMID:26493387), i.e. it is a convergent-phenotype but mechanistically distinct driver. Clinically, no fusion-positive case presented as stage I and tumour cellularity was significantly higher in fusion-positive cases (PMID:22294382); Gooskens et al. found fusion-positive patients were notably young (median 10 months) with small tumour volumes but advanced stage, yet concluded "*the current study did not identify an explicit clinical phenotype*" (PMID:26542179, n=7). A 2026 Chinese series of 7 YWHAE-rearranged CCSKs reported morphological heterogeneity and high aggressiveness, 5/7 stage III and 2/7 stage IV (PMID:41644425).

### Modifier genes

**None established.** **TP53** aberration is better described as a **cooperating somatic lesion / prognostic modifier** (PMID:36563883) than a germline modifier.

### Epigenetic information

This is one of the most informative axes in CCSK.

1. **TCF21 promoter hypermethylation with loss of the lncRNA TARID.** Gooskens et al. (PMID:26158413, *Oncotarget* 2015), verbatim abstract: "*Integrated analysis of expression and methylation data identified promoter hypermethylation and low expression of the tumor suppressor gene TCF21 (Pod-1/capsulin/epicardin) in all CCSKs except the case with t(10;17)(q22;p13). TARID, the long noncoding RNA responsible for demethylating TCF21, was virtually undetectable in most CCSKs… The presence of significant hypermethylation of TCF21, a transcription factor known to be active early in renal development, supports the hypothesis that hypermethylation of TCF21 and/or decreased TARID expression lies within the pathogenic pathway of most CCSKs.*"
   Functional follow-up (PMID:29080283, *Mol Oncol* 2017): decitabine treatment of hypermethylated 786-O cells raised endogenous *TCF21*; re-expression reduced colony size and cut migration by ~59%, raised E-cadherin and markedly reduced vimentin — "*Re-expression of TCF21 in 786-O cells results in a trend toward decreased cell proliferation (not significant) and significantly decreased migration compared with mock-transfected 786-O cells.*" **Caveat to carry into curation:** 786-O is a clear cell *renal cell carcinoma* line, not CCSK — this is a `MODEL_SYSTEM_EXTRAPOLATION`-grade result, and the relevant dismech link would need a `PROXY_QUANTITY` / `SPECIES_MISMATCH`-adjacent divergence note.
2. **A distinct DNA methylation class.** Pediatric BCOR-altered tumours from soft tissue and kidney classify into the methylation class "**BCOR-altered sarcoma family**" with optimal calibrated scores (22/24 molecularly confirmed PMMTI/UND and CCSK), while brain BCOR-ITD tumours match the CNS classifier **HG-NET BCOR** (PMID:36853789, *Mod Pathol* 2023, DOI 10.1016/j.modpat.2022.100039). Methylation profiling is therefore an informative **diagnostic** tool for CCSK.
3. **Polycomb-target derepression.** Roy et al.: "*Transcriptome analysis of ITD-positive CCSKs reveals enrichment for PRC2-regulated genes and similarity to undifferentiated sarcomas harbouring BCOR-CCNB3 fusions*" (PMID:26573325). BCOR-ITD-positive CCSK shows upregulation of PRC2-target, homeobox and developmental gene programmes.

### Chromosomal abnormalities

- **t(10;17)(q22;p13)** → YWHAE::NUTM2B/E (PMID:22294382). A three-way variant **t(10;17;14)(q22.1;p13.3;q24)** has been reported, and **del(14q)** / 14q24 involvement appears in the older cytogenetic literature.
- **Otherwise the karyotype is quiet.** "*No recurrent segmental chromosomal copy number changes…were identified*" (PMID:26158413). The main recurrent copy-number event subsequently found is **TP53 deletion (17p13.1)** in ~23% (9/39 with deletion) (PMID:36563883) — note this is cytogenetically adjacent to the YWHAE breakpoint at 17p13.3 but a distinct event.
- CCSK is **not** a chromosomal-microarray-diagnosable disease: CMA/karyotype have no routine role (see §10).

---

## 5. Environmental Information

- **Environmental factors:** **none identified.** No toxicant, radiation, pollutant or occupational (parental) exposure has been linked to CCSK. CTD/TOXNET/EPA searches return nothing CCSK-specific.
- **Lifestyle factors:** **not applicable** — the patients are toddlers. No maternal or parental lifestyle association has been reported.
- **Infectious agents:** **none.** CCSK has no viral or microbial aetiology; no NCBITaxon-bound infectious agent should be curated, and the §3e infectious-disease granularity ladder does not apply.

This section's content is a *negative result*, and the correct dismech encoding is a documented waiver, not an empty `environmental:` block.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

The chain below runs from initiating lesion to clinical manifestation. **Steps 1–3 and 9–12 are well evidenced; steps 4–8 are partly or wholly inferred, and each is flagged.** The chain branches at the top into three mutually exclusive initiating lesions that converge on a shared transcriptional/epigenetic phenotype.

**Branch A — BCOR ITD (~85–90% of cases)**

1. **A somatic in-frame internal tandem duplication arises in exon 15 of *BCOR* (Xp11.4) in a renal mesenchymal cell**, inserting 30–38 amino acids into the PUFD domain. *Demonstrated* (PMID:26098867, PMID:26573325, PMID:26516930). The lesion is truncal and clonal: identical in primary and relapse, absent from adjacent normal kidney and blood (PMID:26573325).
2. **This leads to selective expression of the mutant allele and marked over-accumulation of mutant BCOR transcript and protein.** *Demonstrated* (PMID:26098867: "*CCSK tumors expressed only an aberrant BCOR allele*"; PMID:26573325: "*Mutant BCOR transcripts and proteins are markedly upregulated*").
3. **The duplicated PUFD termini perturb the BCOR–PCGF1–KDM2B interface of the non-canonical Polycomb repressive complex 1.1 (PRC1.1 / BCOR complex), the H2AK119-monoubiquitinating module that maintains repression at developmental loci.** *Partly demonstrated, partly contested.* Structural/binding work predicts disrupted assembly (PMID:32628469); a 2025 mES knock-in study found assembly and H2AK119ub preserved, with the defect emerging only under PRC2 stress (PMID:40646718). **State this as a contested step.**
4. **The perturbed PRC1.1 results in reduced Polycomb-mediated repression at PRC2-co-regulated developmental loci — homeobox and lineage-specification genes.** *Inferred from expression data rather than directly measured in CCSK tissue.* Supporting: PRC2-regulated gene-set enrichment in ITD-positive CCSK (PMID:26573325); derepression of *PITX1*, *WNT11* and *GATA6* in BCOR-ITD neural stem cells (PMID:33920124); aberrant *Hox* expression in BCOR truncation mutants (PMID:40646718).
5. **In parallel, and whether upstream or downstream is unknown, the *TCF21* promoter becomes hypermethylated and the lncRNA *TARID* — required to demethylate it — is lost, silencing a transcription factor active early in renal development.** *Demonstrated as a co-occurrence; causal position unresolved.* "*promoter hypermethylation and low expression of the tumor suppressor gene TCF21… in all CCSKs except the case with t(10;17)*" (PMID:26158413). Note the exclusion: the one fusion-positive tumour was *not* TCF21-methylated, which argues that TCF21 silencing tracks with the BCOR-ITD branch specifically.
6. **TCF21 loss results in a more mesenchymal, more migratory cell state** (vimentin up, E-cadherin down, migration increased ~2.4-fold on re-expression reversal). *Demonstrated in a surrogate renal line (786-O), not in CCSK cells* — `MODEL_SYSTEM_EXTRAPOLATION` (PMID:29080283).
7. **Steps 4–6 together lock a primitive renal mesenchymal cell out of differentiation and into self-renewal, producing the undifferentiated, cord-and-nest morphology of CCSK.** *Inferred.* Supported by the demonstrated growth and invasion advantage conferred by BCOR-ITD in neural stem cells (PMID:33920124) and by the tumour's own transcriptional neural/primitive signature (PMID:16299227).
8. **Cell-cycle entry is sustained, with cyclin D1 (CCND1) strongly and diffusely over-expressed.** *Demonstrated at protein level* — strong diffuse nuclear cyclin D1 in 61% (11/18) of CCSK (PMID:34673711) and verified as "*strong, diffuse cyclin D1 (CCND1) immunoreactivity in CCSKs*" (PMID:28833375). Whether this is a direct Polycomb-target consequence or indirect is **not established**.
9. **Concurrently, a neural/neuroectodermal-like transcriptional programme is upregulated and the Sonic hedgehog and PI3K–AKT pathways are activated.** *Demonstrated at transcript and protein level.* Cutcliffe et al. profiled 14 CCSKs against 15 Wilms tumours and 3 fetal kidneys and found four categories of differentially expressed genes — neural markers, sonic hedgehog pathway members, PI3K/AKT pathway components, and known therapeutic targets — with protein-level confirmation and increased CD117 (KIT) and EGFR in multiple cases (PMID:16299227, paraphrased from retrieval).
10. **In a subset (~26%), a cooperating TP53 deletion and/or mutation is acquired on the BCOR-ITD background, removing the p53 checkpoint.** *Demonstrated* (PMID:36563883). This step is **not required** for tumour formation and marks the poorest-prognosis group.
11. **In tumours that become metastatic, a MAPK- and angiogenesis-weighted programme is superimposed — FGF3, VEGFA, SPP1, ADM and JUND are over-expressed, with significant over-representation of MAPK signalling (p < 0.0001).** *Demonstrated by WES/WTS on 6 localised vs 3 metastatic BCOR-ITD CCSKs* (PMID:36835166). Functionally, "*FGF3 is able to promote cell migration, with the highest migration induction on cells carrying the BCOR-ITD*" in a CRISPR BCOR-ITD HEK-293 model — so **FGF3 → increased migration is demonstrated, but in a non-renal-mesenchymal surrogate cell**.
12. **The tumour enlarges as a unicentric medullary mass with a characteristic fine, regularly spaced fibrovascular capillary network, invades renal vasculature, and disseminates preferentially to brain, bone and lung, with a strong tendency to relapse within 3 years.** *Demonstrated clinically* (PMID:10632483, PMID:24937667, PMID:30255545, PMID:38396300).

**Branch B — YWHAE::NUTM2B/E (~10–12%)**
1′. t(10;17)(q22;p13) juxtaposes *YWHAE* exons 1–5 (14-3-3ε phosphoserine adaptor) to *NUTM2B/E* exons 2–7, producing a ~3 kb in-frame chimeric transcript (PMID:22294382). → 2′. **This activates downstream signalling distinct from the BCOR-ITD branch** (PMID:26493387) and, notably, **does not involve TCF21 hypermethylation** (PMID:26158413). → 3′. Converges on step 12 with higher tumour cellularity, younger age, smaller volume but higher stage (PMID:22294382, PMID:26542179, PMID:41644425). **The intervening mechanistic steps of this branch are essentially uncharacterised — this is the single largest mechanistic gap in CCSK.**

**Branch C — BCOR::CCNB3 or BCOR::MAML3 (rare)**
1″. A BCOR fusion drives **very high BCOR over-expression** (markedly higher than ITD cases, PMID:28833375), converging on the same BCOR-altered transcriptional/methylation class (PMID:36853789).

### Category-by-category detail

**Molecular pathways**
- **Polycomb / PRC1.1 (non-canonical PRC1) chromatin repression** — the core lesion. GO: `GO:0140261` **BCOR complex** (OLS4 definition: "*A protein-containing complex that monoubiquitinates histone H2A on K119, thus it facilitates the maintenance of the transcriptionally repressive state of some genes, such as BCL6*"; synonyms include *PRC1.1 complex*, *non-canonical BCOR-PRC1.1 complex*). Also `GO:0035102` PRC1 complex. Molecular function: `GO:0140862` **histone H2AK119 ubiquitin ligase activity** — note there is **no GO BP term** for this reaction, so bind the MF, not an invented process.
- **PRC2 crosstalk** — PRC2-regulated gene sets are enriched in ITD-positive CCSK (PMID:26573325) and PRC2 inhibition unmasks the BCOR-ITD phenotype (PMID:40646718).
- **Sonic hedgehog** — `GO:0007224` smoothened signaling pathway (PMID:16299227).
- **PI3K–AKT** — `GO:0043491` phosphatidylinositol 3-kinase/protein kinase B signal transduction (PMID:16299227).
- **MAPK** — `GO:0000165` MAPK cascade; significantly over-represented in metastatic CCSK, p < 0.0001 (PMID:36835166).
- **FGF/FGFR** — `GO:0008543` fibroblast growth factor receptor signaling pathway (FGF3, PMID:36835166).
- **VEGF/angiogenesis** — `GO:0048010` vascular endothelial growth factor receptor signaling pathway; `GO:0001525` angiogenesis (VEGFA, ADM; PMID:36835166). KEGG/Reactome anchors: hsa04010 (MAPK), hsa04151 (PI3K-Akt), hsa04340 (Hedgehog), hsa04370 (VEGF).

**Cellular processes**
- Negative regulation of transcription — `GO:0000122` negative regulation of transcription by RNA polymerase II (the function BCOR/PRC1.1 performs and which the ITD perturbs).
- Epigenetic gene silencing — `GO:0045814` **negative regulation of gene expression, epigenetic** (OLS4 definition explicitly covers "*the cytosine DNA methylation*"): the right binding for TCF21 promoter hypermethylation. **Do not use the obsolete `GO:0006306`.**
- Chromatin organisation / remodelling — `GO:0006325`, `GO:0006338`.
- Blocked mesenchymal differentiation — `GO:0048762` mesenchymal cell differentiation (with `modifier: DECREASED`).
- Proliferation — `GO:0008283` cell population proliferation (`modifier: INCREASED`).
- Migration/invasion — `GO:0016477` cell migration, `GO:0030335` positive regulation of cell migration (FGF3-driven, PMID:36835166).
- Mesenchymal state — `GO:0001837` epithelial to mesenchymal transition is **the wrong term for the tumour itself** (CCSK is mesenchymal from the outset); it applies only to the TCF21 surrogate-line experiment in an epithelial RCC line (PMID:29080283). Flagging this because binding `GO:0001837` to a CCSK pathophysiology node with a fibroblast/mesenchymal `cell_types` annotation would trip `just check-logical-rules`.
- Renal development context — `GO:0001822` kidney development, `GO:0001656` metanephros development (TCF21's normal role).

**Protein dysfunction**
BCOR is a large (1,721 aa in the long isoform) scaffolding corepressor with no catalytic activity of its own: it bridges BCL6 at the N-terminus to the PCGF1–RNF2 catalytic core and KDM2B via the C-terminal PUFD. The ITD is **not a misfolding or aggregation lesion** — it is an insertion into a protein–protein interaction interface whose termini are intrinsically disordered until partner-bound (PMID:32628469). UniProt: BCOR Q6W2J9; PCGF1 Q9BSM1; KDM2B Q8NHM5; RNF2 Q99496; YWHAE P62258. No PDB structure of a BCOR-ITD complex exists; the NMR work in PMID:32628469 is on wild-type PUFD. **AlphaFold predictions of the ITD are not published and should not be cited as if they were.**

**Metabolic changes**
**None characterised.** No metabolomics, lipidomics or energy-metabolism study of CCSK was found. HMDB/MetaboLights/Metabolomics Workbench have no CCSK dataset. This is a clean knowledge gap.

**Immune system involvement**
**Essentially uncharacterised.** No tumour-immune microenvironment study, no TMB-based immunotherapy rationale (and the low mutational burden — PMID:36835166 — predicts poor checkpoint-inhibitor candidacy). There is no autoimmune or immunodeficiency component. Do not curate an immune mechanism.

**Tissue damage mechanisms**
Damage is **mass-effect and invasion**, not a degenerative or inflammatory process: renal parenchymal replacement (the tumour "*markedly distorting or nearly completely replacing the kidney*", PMID:10632483), pelvic compression → hydronephrosis, vascular invasion → IVC thrombus, capsular breach/rupture → peritoneal seeding, and haematogenous embolisation to brain/bone/lung. Gross necrosis and cyst formation are characteristic and **tumour necrosis was one of four independent prognostic factors** in the NWTS multivariate analysis (PMID:10632483).

**Biochemical abnormalities**
No enzyme deficiency, receptor defect or ion-channel defect. **No CCSK-specific serum biochemical abnormality or circulating biomarker exists** (see §10).

**Molecular profiling summary**
- **Transcriptomics:** CCSK vs Wilms vs fetal kidney (PMID:16299227); PRC2-target enrichment and similarity to BCOR-CCNB3 sarcoma (PMID:26573325); WTS driver discovery (PMID:26516930); metastatic vs localised signature (PMID:36835166). GEO is the right repository to search for the underlying series; **I did not verify specific GSE accessions in this session and none should be curated from this report without running `just verify-datasets`.**
- **Proteomics:** none published. PRIDE/ProteomeXchange — nothing CCSK-specific found.
- **Metabolomics / lipidomics:** none.
- **Epigenomics:** 450K/EPIC methylation classification (PMID:36853789); integrated methylation + expression (PMID:26158413).
- **Genomics:** WES showing low TMB and no recurrent second hit (PMID:26158413, PMID:36835166).
- **Single-cell / spatial transcriptomics:** **no CCSK single-cell or spatial dataset found.** Paediatric renal tumour single-cell reference-mapping work exists (e.g. *Nat Commun* 2021, single-cell-derived mRNA signals across human kidney tumours) but CCSK's cell of origin has not been resolved this way. Major gap.
- **Functional genomics screens:** **no CCSK line in DepMap**; no published CRISPR or RNAi screen in a CCSK model. This follows directly from the absence of established CCSK cell lines (§15).

**Cell types and cell of origin (derived, not asserted)**
The cell of origin is **unresolved**. Candidates proposed in the literature include renomedullary interstitial cells, non-organ-specific mesenchymal cells, blastemal cap cells, primitive renal mesenchymal cells, and — on the strength of the expression data — "*a renal mesenchymal cell that shows a wide variety of neural markers*" susceptible to alterations seen in neuroectodermal and neuronal tumours (PMID:16299227). Verified CL candidates for a `cell_types` annotation on the origin node: `CL:0008019` mesenchymal cell, `CL:0000134` mesenchymal stem cell, `CL:1000692` kidney interstitial fibroblast, `CL:0000669` pericyte, `CL:1000497` kidney cell. **Bind conservatively — `CL:0008019` mesenchymal cell is the defensible choice, with the specific candidates recorded in `notes:`.** Per dismech's cancer-cell-of-origin convention, the origin is derived from the node carrying `genetic_context: {variant_origin: SOMATIC, functional_impact_category: …}` — so mark the BCOR ITD node as the origin node and bind its `cell_types` there. Note that marking it means the exposure rule is suppressed, which is correct here (there is no initiating exposure).

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary organ: kidney** — `UBERON:0002113` kidney. **Unilateral, unicentric.** When an epicentre could be determined, the **renal medulla** was the commonest location, and no multicentric case was found among 351 (PMID:10632483) — `UBERON:0000362` renal medulla. Cortex is secondarily involved by expansion: `UBERON:0001225` cortex of kidney.
- **Secondary / metastatic organs:**
  - `UBERON:0000955` brain — commonest relapse site in the modern era (PMID:30255545, PMID:38396300, PMID:24937667).
  - `UBERON:0001474` bone element / `UBERON:0002481` bone tissue / `UBERON:0001434` skeletal system — the historical signature site.
  - `UBERON:0002048` lung.
  - `UBERON:0000029` lymph node — regional (renal hilar, para-aortic) involvement defines stage III.
  - `UBERON:0002107` liver.
  - `UBERON:0001224` renal pelvis — compressed, causing hydronephrosis.
  - `UBERON:0001072` inferior vena cava — tumour thrombus in ~11% (PMID:38980838).
  - `UBERON:0002358` peritoneum — after rupture or capsular breach.
  - Soft tissue and unusual sites (scalp, neck, nasopharynx, axilla, orbit, epidural space) (PMID:22579455).
- **Body systems:** renal/urinary (primary); musculoskeletal, nervous and respiratory (metastatic); cardiovascular (vascular invasion, IVC thrombus, and treatment-related anthracycline cardiotoxicity).

### Tissue and cell level
- **Tissue type: connective/mesenchymal.** CCSK is a malignant mesenchymal neoplasm of undifferentiated cells in cords and nests separated by fine fibrovascular septa with abundant extracellular matrix.
- **The vascular architecture is diagnostic**, not incidental: "*nests of tumor cells are separated by regularly-spaced, fine fibrovascular septa*", classically described as a "chicken-wire" capillary network. Endothelium (`CL:0000115` — **not verified in this session, look it up before binding**) and pericytes (`CL:0000669`, verified) are the septal constituents.
- **Target cell population:** see cell-of-origin above.

### Subcellular level
- **Nucleus / chromatin** is the compartment where the lesion acts. GO CC: `GO:0140261` BCOR complex; `GO:0035102` PRC1 complex. (`GO:0005634` nucleus and `GO:0000785` chromatin were **not** verified in this session — look them up before binding.)
- **Cytoplasm** is where 14-3-3ε (YWHAE) normally acts as a phosphoserine adaptor; the fusion's localisation is uncharacterised.

### Localisation and lateralisation
**Unilateral** — either kidney; no reported side predilection. **Unicentric**; **bilateral disease is extraordinary** (a single case report) and, unlike Wilms tumour (~5% bilateral), bilaterality should prompt re-review of the diagnosis. CCSK is **not** associated with nephroblastomatosis: 1/351 had perilobar nephrogenic rests, none intralobar (PMID:10632483).

---

## 8. Temporal Development

### Onset
- **Age:** paediatric, peak **2–4 years**; mean 36 months, range 2 months – 14 years in NWTS (PMID:10632483). Neonatal and adult cases exist but are exceptional.
- **Pattern:** **subacute/insidious** — an enlarging abdominal mass. Acute presentations occur via rupture, haemorrhage, IVC thrombus or pathological fracture.

### Progression
- **Staging:** CCSK is staged on the **COG/NWTS renal tumour staging system** (the same system used for Wilms tumour) in North America, and the **SIOP post-chemotherapy staging system** in Europe. Stage, in both, is the dominant prognostic variable. **Published stage distributions (note how they differ by group, because SIOP stages after preoperative chemotherapy):**

| Cohort | I | II | III | IV | Source |
|---|---|---|---|---|---|
| COG AREN0321/AREN03B2 (n=132) | 7.6% | 36% | 49% | 7.6% | PMID:38396300 |
| SIOP 93-01/2001 (n=191) | 42% | 23% | 28% | 7% | PMID:23880476 |
| NWTS-5 (n=108) | 11% (12) | 41% (44) | 42% (45) | 6.5% (7) | PMID:30255545 |
| Shanghai (n=54) | 16% | 30% | 39% | 15% | PMID:38980838 |

  The large stage-I difference between SIOP and COG series is a **direct consequence of preoperative chemotherapy downstaging** and must not be read as a biological difference.
- **Progression rate:** rapid if untreated; after treatment the course is defined by relapse timing.
- **Course pattern:** **treated remission with risk of relapse**, not chronic progressive disease. Relapse within 3 years in the overwhelming majority: 20/23 events (PMID:30255545); "*Fourteen relapses (93.3%) occurred within 3 years of diagnosis*" (PMID:38396300). Median time to relapse **17 months** in the SIOP/AIEOP relapse study (PMID:24937667).
- **Duration:** not a lifelong chronic disease. Either cured (the majority) or fatal, usually within a few years of relapse.

### Patterns
- **Remission:** **treatment-induced only.** No spontaneous regression is reported for CCSK (in explicit contrast to stage 4S neuroblastoma or infantile fibrosarcoma-adjacent entities). After relapse, "*Fifty-nine percent achieved second complete remission, though 68% of these developed subsequent relapse*" (PMID:24937667).
- **Critical periods / windows for intervention:** (i) **complete initial resection with lymph-node sampling** — this is what permits radiotherapy omission in stage I (PMID:38396300, PMID:22658515); (ii) **the first 3 years after diagnosis**, when essentially all relapses occur, which defines the surveillance window; (iii) **brain imaging at diagnosis and in post-treatment surveillance** (PMID:38396300).

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence:** age-adjusted **0.205 per million** children (SEER, 0–19 years, 2000–2017), "*which remained stable for years*" (PMID:34095035). Expressed as cases per 100,000 per year this is **0.0205/100,000/year**, i.e. in dismech terms `measure_type: ANNUAL_INCIDENCE`, `rate_per_100000: 0.0205`, `rate_denominator: POPULATION_PER_YEAR`, `prevalence_class: BELOW_1_IN_1000000`. **Use the SEER paper's own figure; do not convert loosely.**
- **Proportion of paediatric renal tumours:** ~**2–5%** (PMID:26573325, PMID:22579455); ranked **third** by SEER incidence among paediatric renal tumours (PMID:34095035) while conventionally called the **second most common renal malignancy** of childhood.
- **Prevalence:** Orphanet does not publish a prevalence class for ORPHA:457246. Because CCSK is an acute-onset curable-or-fatal childhood cancer, **point prevalence is not an informative measure** and should be left as `NOT_YET_DOCUMENTED` rather than estimated.

### Genetic etiology parameters
| Parameter | Status |
|---|---|
| Inheritance pattern | **Not applicable — somatic.** Do not curate an `inheritance:` block with a Mendelian HPO mode-of-inheritance term. If an inheritance statement is wanted at all, the honest encoding is *somatic*, and `HP:0001442` (typified by somatic mosaicism) is **the wrong term** — that is for post-zygotic constitutional mosaicism, not for a tumour-restricted driver mutation. |
| Penetrance | Not applicable |
| Expressivity | Not applicable |
| Genetic anticipation | Not applicable |
| Germline mosaicism | Not reported; not applicable |
| Founder effects | None |
| Consanguinity | No role reported |
| Carrier frequency | Not applicable |

### Population demographics
- **Sex:** **male predominance.** IRR 3 for boys (PMID:34095035); M:F ≈ 2:1 (PMID:10632483); 64% male (PMID:23880476); 69% male (PMID:30255545); 37:17 ≈ 2.2:1 (PMID:38980838). **A sex bias in an Xp11.4-driven tumour is biologically interesting and, as far as I can find, unexplained** — the ITD is somatic, so X-inactivation/hemizygosity arguments have not been worked out in print. Worth recording as a knowledge gap rather than explained away.
- **Age:** IRR **21** for ≤4 years vs older children (PMID:34095035).
- **Ethnicity/ancestry:** the SEER analysis concluded "*Incidence of CCSK may not be ethnically various*" (PMID:34095035), i.e. **no established ancestry-specific difference**, on limited evidence. NWTS-5 enrolled 63% Caucasian patients (PMID:30255545) — that is a cohort composition, not an incidence ratio, and must not be reported as one. **Do not curate a HANCESTRO-bound `population_effects` claim; there is no source-stated ancestry difference.**
- **Geography:** worldwide; no endemic area. Cohorts exist from North America, Europe, China, Egypt, Austria. There is **no reported geographic distribution of specific variants**.

---

## 10. Diagnostics

### Clinical tests
- **Laboratory tests:** **no diagnostic laboratory abnormality.** Baseline FBC (anaemia), renal function, LDH and urinalysis (haematuria) are obtained as part of a renal-mass workup but none is specific. There is **no serum or urinary tumour marker** for CCSK. I found no CCSK-specific LOINC-coded diagnostic measurement; **do not invent one** — if a `diagnosis[].measurements` block is curated it should hold only generic analytes, and each LOINC code must be seeded via `just loinc-seed-cache` before use.
- **Biomarkers:** the diagnostic biomarkers are **tissue-based, not circulating** — BCOR ITD / YWHAE::NUTM2 / BCOR::CCNB3 by molecular testing, and BCOR + cyclin D1 by IHC. No FDA-listed biomarker.
- **Imaging:** ultrasound then contrast CT or MRI of the abdomen. **Imaging cannot distinguish CCSK from Wilms tumour** — findings are a large heterogeneous solid-cystic hetero-enhancing renal mass with necrosis, a claw sign confirming renal origin, and often hydronephrosis from pelvic compression; histology after nephrectomy is required. CT radiomics has been explored to discriminate CCSK from Wilms tumour (PMC10768092) but is not clinical practice. **Staging imaging specific to CCSK:** on NWTS-5, "*Staging consisted of CT scans of chest, abdomen, pelvis, bone scan, skeletal survey, and CT or MRI of the head*" (PMID:30255545). On AREN0321/AREN03B2 patients "*were required to undergo bone scan and MRI of the brain for staging at diagnosis and end of therapy*", and that study's authors concluded that brain imaging at diagnosis and in surveillance matters while "*routine interval nuclear medicine imaging for bone recurrences may not be needed*" (PMID:38396300). ¹⁸F-FDG PET/CT has been reported in single cases (PMID:38377388), not established.
  **Brain MRI surveillance is deliberately not universal**, and the arithmetic is worth preserving because it is a good example of a rational negative recommendation: relapse occurs in ~16% of patients and ~41% of relapses are in brain, so universal surveillance MRI would be screening everyone to detect brain relapse in ~7% — the SIOP position is that brain MRI is of value on suspicion of brain relapse in an individual patient and as workup when relapse is found elsewhere (PMID:29485128 / SIOP relapse analysis).
- **Functional tests / electrophysiology:** no diagnostic role. **Echocardiography is required for anthracycline monitoring**, which is a treatment-toxicity surveillance test, not a diagnostic one.
- **Biopsy / histopathology — the diagnostic cornerstone.**
  - **Gross:** large, often tan/grey, mucoid, with necrotic foci and cyst formation; frequently replacing most of the kidney; epicentre in the medulla (PMID:10632483).
  - **Microscopic:** classic pattern is plump ovoid cells with monomorphic nuclei, fine (sometimes vesicular) chromatin and inconspicuous nucleoli, arranged in cords/trabeculae/nests separated by **regularly spaced fine fibrovascular septa with thin-walled capillaries**, in abundant sclerotic extracellular matrix. The cells are **not actually clear** in most cases — the name is historical and refers to a nuclear/cytoplasmic appearance that is often absent, which is a recurring source of misdiagnosis.
  - **Nine histological patterns** were codified by Argani et al. (PMID:10632483): **classic, myxoid, sclerosing, cellular, epithelioid, palisading, spindle, storiform, anaplastic**. This histological promiscuity is why CCSK "*frequently mimics other pediatric renal tumors, causing misdiagnosis*" (PMID:30917048), and why anaplasia in a needle biopsy can obscure the diagnosis entirely (PMID:42522467).
- **Immunohistochemistry:**
  - **Positive:** **BCOR** (nuclear), **cyclin D1** (nuclear), vimentin, BCL2, CD56 (NCAM1), TLE1, SATB2, p75-NGFR.
  - **Negative:** cytokeratin, WT1, desmin, S100, CD34, EMA, MIC2/CD99 (PMID:10638490→correctly PMID:10632483 for vimentin+/cytokeratin−/MIC2−).
  - **Quantified performance:** "*strong, diffuse nuclear immunoreactivity for cyclin D1 and BCOR was noted in 61% (n=11/18) and 83% (n=15/18)*" of CCSK respectively, with significantly less or no reactivity in Wilms tumour, malignant rhabdoid tumour and congenital mesoblastic nephroma (PMID:34673711). Kao et al.: "*all SBRCTs with BCOR-MAML3 and BCOR-CCNB3 fusions, as well as most with BCOR ITD (93%), and all CCSKs showed strong and diffuse nuclear BCOR immunoreactivity*", making BCOR "*a highly sensitive marker*" (PMID:27428733).
  - **Two important cautions.** (i) **BCOR IHC is antibody-clone dependent and not reliably positive in ITD-positive tumours** — Wong et al. found positivity in 4/11 (36%) or 8/11 (72%) depending on clone, and concluded BCOR IHC "*cannot be used as a diagnostic immunohistochemical stain to identify BCOR ITD cases*" (PMID:28833375). (ii) **BCOR IHC is not specific** — renal **malignant solitary fibrous tumour** is "*a close mimic of clear cell sarcoma of kidney*", showing strong BCOR immunoreactivity **without** BCOR genetic alteration; STAT6 positivity resolves it, and the distinction matters because CCSK carries a specific chemotherapy protocol (PMID:30864973). The summary judgement in the literature is that cyclin D1 is sensitive but imperfectly specific and BCOR is neither perfectly sensitive nor specific — concurrent diffuse nuclear positivity for both is what supports the diagnosis.

### Genetic testing
- **Recommended approach:** this is **somatic tumour testing**, not germline diagnostics. Confirm the driver on tumour tissue.
- **The practical assay:** RT-PCR / fragment analysis for BCOR exon 15 ITD; RT-PCR or FISH for YWHAE rearrangement; RT-PCR/FISH for BCOR::CCNB3. A validated multiplex is now published: Zhang et al. developed "*a Universal Fluorescence Multiplex PCR-based assay that assessed BCOR ITDs, BCOR::CCNB3, BCOR::MAML3 and YWHAE::NUTM2 fusions simultaneously*", achieving **93% sensitivity and 100% specificity** across 43 tumours (PMID:39871307, *Diagn Pathol* 2025). Targeted RNA sequencing is an alternative (*J Mol Diagn* 2021, DOI 10.1016/j.jmoldx.2021.06.006). **Watch for long spliced ITDs**, which standard assays miss (PMID:35836306) — a plausible explanation for part of the double-negative fraction.
- **WGS/WES:** low yield for diagnosis given the quiet genome (PMID:26158413, PMID:36835166); valuable for research and for the double-negative subset.
- **Gene panels / single-gene testing:** a paediatric sarcoma fusion panel including BCOR, YWHAE, CCNB3, MAML3 is the appropriate panel. **No germline panel is indicated.**
- **CMA / karyotyping / FISH:** CMA and karyotype have **no routine diagnostic role** (no recurrent copy-number signature). FISH is useful for YWHAE and BCOR rearrangement. **TP53 FISH/sequencing is a research/prognostic test, not standard.**
- **mtDNA testing, repeat-expansion testing:** **not applicable.**

### Omics-based diagnostics
- **DNA methylation classification is the one omics modality with demonstrated diagnostic utility**: CCSK and soft-tissue BCOR-altered sarcomas fall into the "BCOR-altered sarcoma family" methylation class, brain ones into HG-NET BCOR, and the authors conclude methylation profiling "*is an informative diagnostic tool*" (PMID:36853789). A broader paediatric soft-tissue/bone sarcoma methylation classifier has since been published (PMID:39567898).
- **RNA-seq:** used for fusion/ITD detection (above).
- **Proteomics, metabolomics, liquid biopsy:** **no established role; no published data.** There is no ctDNA assay for CCSK.

### Clinical criteria
- **Diagnosis is histopathological with molecular confirmation**, made on a nephrectomy specimen (COG) or on post-chemotherapy nephrectomy with pre-treatment biopsy (SIOP). There is no clinical/imaging criterion set and no scoring instrument. **Central pathology review is standard in both cooperative groups** and is how all the reference cohorts were assembled — a point worth preserving, because CCSK's nine morphological patterns make single-observer diagnosis unreliable.
- **Differential diagnosis, with the discriminating feature:**

| Entity | Discriminator |
|---|---|
| **Wilms tumour (favourable histology)** | WT1 positive; triphasic blastemal/epithelial/stromal; no BCOR ITD (0/193 non-CCSK paediatric renal tumours, PMID:26098867); cyclin D1/BCOR negative or weak |
| **Malignant rhabdoid tumour of kidney** | SMARCB1/INI1 loss by IHC; younger, more aggressive |
| **Congenital mesoblastic nephroma (cellular)** | *ETV6::NTRK3* fusion / t(12;15); neonatal; cyclin D1/BCOR low |
| **Metanephric stromal tumour** | *ALK* alterations in a subset; bland, onion-skin perivascular cuffing |
| **Synovial sarcoma (renal)** | *SS18::SSX* fusion — **note TLE1 is positive in both**, so TLE1 does not discriminate (PMID:25888919 reports a case resolved by genetics) |
| **Renal malignant solitary fibrous tumour** | **STAT6 positive; BCOR-positive by IHC but BCOR-wild-type genetically** — the trap (PMID:30864973) |
| **Ewing sarcoma of kidney** | *EWSR1* fusion; CD99 diffuse membranous; older patients, 37% metastatic at presentation (PMID:41509607) |
| **BCOR-CCNB3 sarcoma (primary bone/soft tissue)** | Same gene family; site and age differ — and a kidney-presenting case *is* classified as CCSK (PMID:28833375) |
| **Primitive myxoid mesenchymal tumour of infancy (PMMTI)** | Shares BCOR ITD and a "very similar transcriptional signature" — plausibly the soft-tissue equivalent of CCSK (PMID:36853789) |
| **Clear cell renal cell carcinoma** | Adult; epithelial; PAX8/CK positive; VHL |
| **Clear cell sarcoma of soft tissue** | *EWSR1::ATF1*; melanocytic markers; not renal |

### Screening
- **No screening programme exists and none is indicated.** There is no newborn screening, no carrier screening, no cascade screening — because there is no germline lesion. Risk stratification is **post-diagnosis** (stage, age, necrosis, rupture, IVC thrombus, TP53 status), not pre-diagnosis.

---

## 11. Outcome / Prognosis

### Survival and mortality

| Cohort | 5-year EFS | 5-year OS | Notes |
|---|---|---|---|
| NWTS 1–4 (n=182 with follow-up) | — | **69%** overall; stage I **98%** | PMID:10632483 |
| NWTS-5 (n=108) | **79%** (95% CI 71–88) | **90%** (95% CI 84–96) | median follow-up 9.7 y; PMID:30255545 |
| SIOP 93-01/2001 (n=191) | **79%** | **86%** | PMID:23880476 |
| COG AREN0321 (n=82) | **82.7%** (4-y; 95% CI 74.8–91.4) | — | PMID:38396300 |
| COG AREN03B2 only (n=117) | **89.6%** (4-y; 95% CI 81.3–98.7) | — | PMID:38396300 |
| SEER (0–19 y) | — | **87%** | vs 90% for Wilms unmatched; **86% vs 95%** propensity-matched; PMID:34095035 |
| Shanghai NWTS-strategy (n=54) | **82.4 ± 5.4%** | **88.1 ± 4.6%** | PMID:38980838 |
| Multicentre renal sarcoma cohort | — | **92.6%** (4-y OS for CCSK) | best outcome among renal sarcoma types; PMID:41509607 |

**By stage (5-year EFS unless stated):**

| Stage | NWTS-5 (PMID:30255545) | COG AREN0321/03B2, 4-y EFS / OS (PMID:38396300) | Shanghai (PMID:38980838) |
|---|---|---|---|
| I | **100%** | 90% / 100% | 100% |
| II | **88%** | 93.4% / 97.9% | 93.8% |
| III | **73%** | 82.8% / 93.8% | 71.1% |
| IV | **29%** | 58.3% / 77.8% | 68.6% |

The stage IV figure is the headline problem: it ranges from 29% (NWTS-5, no carboplatin) to ~58–69% (carboplatin era), and the COG authors' own verdict is that stage IV patients "*appeared to benefit from a carboplatin-containing regimen, though their outcomes remain unsatisfactory*" (PMID:38396300).

**Life expectancy:** survivors of localised CCSK have near-normal life expectancy subject to late treatment effects. **Untreated CCSK is uniformly fatal.** The historical comparison that quantifies treatment benefit: addition of doxorubicin improved 6-year event-free survival from **25% to 64%** in the NWTS experience.

**Disease-specific mortality:** stage I–II mortality 10.1% (14/138) versus stage IV 66.7% (22/33) in a pooled published-patient analysis (PMID:36186639).

### Morbidity and function
- **Morbidity** is driven by treatment: single kidney after radical nephrectomy, **anthracycline cardiotoxicity**, flank/abdominal radiotherapy in a child <4 years (musculoskeletal growth, renal, gonadal), alkylator and etoposide exposure (gonadotoxicity, second-malignancy risk), and the sequelae of CNS relapse and its treatment.
- **Disability outcomes:** no ICF-coded or registry-based disability data specific to CCSK.
- **Quality of life:** **no CCSK-specific QoL measurement published** (see §3). This is a real and curatable gap.

### Disease course and complications
- Tumour rupture, IVC/atrial tumour thrombus (an occasional surgical emergency, PMC9428440), hydronephrosis, haemorrhage, and metastatic complications (pathological fracture, raised intracranial pressure, seizures).
- **Recovery potential:** high for stage I–II with full trimodal therapy; **poor after relapse.** "*5-year event-free survival (EFS) after relapse was 18% (95% CI: 4%-32%), and 5-year overall survival (OS) was 26%*" (PMID:24937667); 22.9% 5-year OS post-relapse in a pooled analysis (PMID:36186639). Long-term survival after relapse is possible with intensive multimodal salvage — the Austrian series is titled for exactly that (PMID:33438324) and 4/8 relapsing Shanghai patients achieved second CR with intensive multimodal therapy (PMID:38980838).

### Prognostic factors
**Established (multivariate, NWTS, PMID:10632483):** four independent factors — **doxorubicin treatment, stage, age at diagnosis, and tumour necrosis.**
**Confirmed/added since:**
- **Stage** — the dominant factor in every cohort; "*Stage was highly predictive of outcome*" (PMID:30255545).
- **Stage IV and young age** — "*Stage IV disease and young age were significant adverse prognostic factors for event-free survival*" (PMID:23880476). Note the direction: **younger** is worse, which is the opposite of the Wilms tumour pattern and is clinically important.
- **Distant metastasis and year of diagnosis** — independent in SEER; large tumour size (≥15 cm) also adverse (PMID:34095035).
- **Tumour rupture** — independent, HR 5.9, p=0.01; **IVC thrombus** — EFS 41.7%, p=0.028 (PMID:38980838).
- **Chemotherapy and radiotherapy receipt** — independent OS predictors in a pooled nomogram (C-index 0.878), though radiotherapy "*no significant contribution to preventing relapse*" (PMID:36186639). Treat that last finding cautiously: it comes from pooled published cases with severe selection bias, and it is **not** the basis of the COG/SIOP radiotherapy policy.
- **MRI-measured size >4 cm, necrotic signal, and peritumoral oedema** correlated with metastatic-relapse risk in imaging work (not independently validated).

**Prognostic biomarkers (candidate, none validated for clinical use):**
- **TP53 aberration** — "*Patients with both BCOR ITD and TP53 deletion had the poorest prognosis*", with OS and PFS showing "*obvious downward trends, albeit not all reaching statistical significance*" (PMID:36563883). The honest reading is a promising signal in 39 patients, underpowered.
- **FGF3 and the metastatic MAPK/angiogenesis signature (FGF3, VEGFA, SPP1, ADM, JUND)** — "*could offer new prognostic and therapeutic targets in more aggressive cases*" (PMID:36835166), n=9.
- **Driver class (BCOR ITD vs YWHAE vs double-negative)** — prognostic relevance **remains unknown** (PMID:38396300), with suggestive clinical differences between subsets (PMID:27000436) and high aggressiveness in a small YWHAE-rearranged series (PMID:41644425).

---

## 12. Treatment

**The standard of care is trimodal: upfront or post-chemotherapy radical nephrectomy, a doxorubicin-containing multi-agent chemotherapy regimen, and radiotherapy to the tumour bed (omitted for stage I with nodal sampling).** The two cooperative groups differ in surgical timing, not in principle: COG operates first ("upfront surgery principle providing definite pathology"), SIOP gives preoperative chemotherapy first (PMID:38980838 states the contrast explicitly).

### Pharmacotherapy

**COG Regimen I — stages I–III** (PMID:38396300, PMID:30255545):
vincristine + doxorubicin + cyclophosphamide + etoposide over ~6 months (24 weeks); NWTS-5 delivered vincristine/doxorubicin/cyclophosphamide **alternating with** cyclophosphamide/etoposide.

| Agent | CHEBI (verified) | Class / mechanism | NCIT treatment term (verified) |
|---|---|---|---|
| Vincristine | `CHEBI:28445` vincristine | Vinca alkaloid; tubulin polymerisation inhibitor → M-phase arrest | `NCIT:C15632` Chemotherapy |
| Doxorubicin | `CHEBI:28748` doxorubicin | Anthracycline; topoisomerase II poison, DNA intercalation, ROS. **The single most important drug in CCSK** — its addition raised 6-y EFS from 25% to 64% | `NCIT:C15632` Chemotherapy |
| Cyclophosphamide | `CHEBI:4027` cyclophosphamide | Oxazaphosphorine alkylator; DNA crosslinks | `NCIT:C15632` Chemotherapy |
| Etoposide | `CHEBI:4911` etoposide | Epipodophyllotoxin; topoisomerase II inhibitor | `NCIT:C15632` Chemotherapy |

**COG Regimen UH-1 / revised UH-1 — stage IV** (PMID:38396300): Regimen I **plus carboplatin** (`CHEBI:31355` carboplatin). The regimen was **revised in 2008 to reduce doxorubicin, cyclophosphamide and etoposide doses because of toxicity** — a detail worth carrying, because it means "UH-1" in the literature is two different regimens.

**Historical NWTS regimens:** vincristine + dactinomycin (`CHEBI:27666` actinomycin D) ± doxorubicin; NWTS-4 showed 15 months of vincristine/doxorubicin/dactinomycin gave better relapse-free survival than 6 months (88% vs 61% at 8 years), but Seibel et al. showed extended therapy improved relapse-free survival (87.8% vs 65.2–60.6% at 5 and 8 years) **without changing long-term overall survival** (PMID:14752069) — which is why modern CCSK therapy is ~6 months, not 15.

**SIOP/UMBRELLA SIOP-RTSG 2016** (PMID:29485128): preoperative chemotherapy → nephrectomy → stage-adapted postoperative doxorubicin-containing chemotherapy → flank radiotherapy for stages II–III. **I was unable to retrieve the regimen-level drug schedule from the position paper in this session; consult PMID:29485128 directly before curating specific SIOP agents or doses.** Do not reconstruct them from the COG arm.

**Pharmacogenomics:** no CCSK-specific pharmacogenomics. The generically relevant and well-established axes are anthracycline cardiotoxicity risk variants (*RARG*, *SLC28A3*, *UGT1A6* — CPIC/PharmGKB) and *TPMT*/*NUDT15* for thiopurines (not used here). **No CCSK-specific PGx recommendation exists.**

### Advanced therapeutics
- **Gene therapy, cell therapy, RNA-based therapy:** **none** — no trial, no preclinical programme specific to CCSK.
- **Targeted therapy:** **none approved or in trial for CCSK.** The rational candidate hypotheses from the biology, all **preclinical or purely inferential**, are:
  - **EZH2 / PRC2 inhibition** (e.g. tazemetostat) — motivated by PRC1.1 disruption, PRC2-target derepression, and the Dhoondia finding that the BCOR-ITD phenotype is unmasked by PRC2 inhibition (PMID:40646718). **Note the direction of that result carefully: PRC2 inhibition revealed aberrant cell fate in BCOR-ITD cells, which is a rationale for a synthetic-lethal interaction but not a demonstration of antitumour effect.** No CCSK preclinical EZH2-inhibitor data were found.
  - **CDK4/6 inhibition** — motivated by cyclin D1 over-expression (PMID:34673711, PMID:28833375). **No CCSK data.**
  - **FGFR inhibition** — motivated by FGF3 in the metastatic signature and its migration-promoting effect in a BCOR-ITD HEK-293 model (PMID:36835166). **No CCSK in vivo data.**
  - **Anti-angiogenics** — motivated by VEGFA/ADM in the metastatic signature (PMID:36835166).
  - **KIT / EGFR inhibition** — motivated by increased CD117 and EGFR protein, which the authors flagged as "*suggesting therapeutic potential*" (PMID:16299227). This 2005 lead has **not been translated in 20 years**, which is itself informative.
  - **DNMT inhibition (decitabine, `CHEBI:749378`)** — motivated by TCF21 promoter hypermethylation; decitabine raised endogenous TCF21 in a surrogate RCC line (PMID:29080283). **Surrogate cell line, not CCSK.**
  
  Every one of these should be curated, if at all, as a `discussions` entry with `kind: KNOWLEDGE_GAP` plus `proposed_experiments`, **not** as a `treatments:` record. There is no CCSK targeted therapy.
- **Immunotherapy:** none. The low mutational burden (PMID:36835166) argues against checkpoint blockade.

### Surgical and interventional
- **Radical nephrectomy** (`NCIT:C51778` Radical Nephrectomy; also `NCIT:C15284` Nephrectomy, `NCIT:C15329` Surgical Procedure) with **lymph-node sampling** — the latter is not optional bookkeeping: it is what permits radiotherapy omission in stage I (PMID:38396300, PMID:22658515). Upfront in COG (46/54 upfront in the Shanghai NWTS-strategy cohort, PMID:38980838); post-chemotherapy in SIOP.
- **IVC/atrial thrombectomy** where tumour thrombus extends (PMC9428440).
- **Metastasectomy** has a role in selected relapse.

### Radiotherapy
`NCIT:C15313` Radiation Therapy. Flank or whole-abdominal radiotherapy at **10.8 Gy**, with dose-escalated RT to metastatic sites (PMID:38396300); the Shanghai cohort used **10.8–20 Gy** to the tumour bed and omitted lung RT in patients achieving complete radiographic response at 6 weeks (PMID:38980838).
**The key modern de-escalation:** on AREN0321, "*radiation therapy was omitted for stage I disease if lymph nodes were sampled*", and the conclusion was that "*Patients with stage I CCSK had excellent outcomes without local recurrence when treated without RT*" — **no local recurrences among stage I patients treated without RT** (PMID:38396300). The supporting historical analysis: among 53 revised-stage-I CCSK patients on NWTS 1–5, 46 (87%) received flank RT and 7 (13%) did not, median dose 10.8 Gy, and 5-year EFS and OS were **100%** with median follow-up 17 years (PMID:22658515).

### Supportive and rehabilitative
`NCIT:C15747` Supportive Care. Standard paediatric oncology supportive care (antiemetics, growth-factor support, infection prophylaxis, nutrition, pain control), plus **cardiac surveillance for anthracycline exposure** and long-term follow-up for single-kidney status, growth, and fertility. `NCIT:C15315` Rehabilitation as needed after CNS relapse. No CCSK-specific supportive-care guideline exists.

### Experimental treatments / trials
- **There is no CCSK-specific interventional therapeutic trial currently recruiting**, as far as I can determine. AREN0321 (NCT00335556 — high-risk renal tumours, the study whose CCSK results are PMID:38396300) and AREN03B2 (the biology/classification study) are closed to accrual. NCT00025103 (chemotherapy ± stem-cell transplant for relapsed/refractory Wilms tumour **or CCSK**) is historical.
- The nearest active relevant registry is the **International Rare Brain Tumor Registry (NCT05697874)**, which includes BCOR-ITD and BCOR-altered CNS tumours — relevant to the family, not to renal CCSK.
- **The HARMONICA collaboration** is the current international effort addressing relapsed rhabdoid and other non-nephroblastoma childhood kidney tumours (*Nat Rev Urol* 2025, DOI 10.1038/s41585-025-01117-4); I could not retrieve its CCSK-specific content (paywall) and have not curated any claim from it.
- **Before curating any trial, run `just fetch-reference NCT…` and `just clinicaltrials-status-audit`** — the status/phase values above are not verified against the live registry in this session and must not be written into `clinical_trials:` as-is.

### Treatment outcomes
- **Response rates:** not reported as classical response rates (upfront-surgery disease). The relevant outcomes are the EFS/OS figures in §11.
- **Relapse salvage:** chemotherapy, surgery, radiotherapy, and **high-dose chemotherapy with autologous stem-cell rescue in 14/37** in the SIOP/AIEOP relapse study; 59% second CR, but 68% of those relapsed again (PMID:24937667). PDQ notes recurrent CCSK has responded to **ifosfamide (`CHEBI:5864`), carboplatin and etoposide (ICE)**.
- **Side effects / adverse events:** anthracycline cardiomyopathy; alkylator gonadotoxicity and haemorrhagic cystitis; etoposide-associated secondary leukaemia risk; radiation effects on growth, kidney and gonads; the UH-1 dose reduction in 2008 was driven by toxicity (PMID:38396300). No CCSK-specific FAERS signal.

### Treatment strategy
- **Algorithm:** stage-adapted trimodal therapy. Stage I → nephrectomy + nodal sampling + Regimen I, **no RT**. Stages II–III → nephrectomy + Regimen I + flank/whole-abdominal RT 10.8 Gy. Stage IV → carboplatin-containing (revised UH-1) + RT to metastatic sites. Relapse → intensive multimodal salvage ± HDC/ASCT, outcomes poor.
- **Combination therapy** is the norm; monotherapy has no role.
- **Personalised medicine:** **not yet realised.** Driver class does not currently change treatment, and the COG authors state the prognostic relevance of BCOR ITD / YWHAE / BCOR-CCNB3 "*remains unknown*" (PMID:38396300). This is the honest state of the art and should be curated as such.

---

## 13. Prevention

- **Primary prevention: not possible and not applicable.** CCSK arises from a somatic driver mutation in early childhood with no identified environmental cause, no germline predisposition, and no modifiable risk factor. There is nothing to vaccinate against, nothing to avoid, and no risk-factor modification available. **State this explicitly rather than leaving the section empty — the negative is the content.**
- **Secondary prevention (early detection):** no population screening exists or is justified (incidence 0.205 per million). The practically relevant "secondary prevention" is **prompt evaluation of a paediatric abdominal mass** and **complete initial resection with nodal sampling**, which converts stage III into stage II/I and is the single most consequential modifiable step in the pathway.
- **Tertiary prevention (preventing complications in those with disease):** this is where the real content is —
  - **Risk-adapted therapy**: doxorubicin for all; carboplatin for stage IV; radiotherapy omission in stage I to avoid late effects (PMID:38396300, PMID:22658515).
  - **Relapse surveillance in the first 3 years**, when >93% of relapses occur (PMID:38396300), with **brain imaging at diagnosis and in post-treatment surveillance** and a reasoned decision **against** universal interval brain MRI and against routine interval bone scintigraphy (PMID:38396300).
  - **Late-effect surveillance**: echocardiography for anthracycline exposure, renal function monitoring in the single-kidney survivor, growth and endocrine/fertility follow-up after abdominal RT and alkylators.
- **Immunisation:** no CCSK-specific vaccine. Standard immunisation with the usual precautions during and after immunosuppressive therapy.
- **Genetic screening / PGD / prenatal testing: not applicable** — somatic disease, no germline lesion, no familial recurrence risk.
- **Genetic counselling:** the appropriate counselling message is **reassurance about recurrence risk** — the driver is somatic and absent from blood (PMID:26573325), so siblings and offspring are not at increased risk, and no germline testing is indicated. (`NCIT:C15240` Genetic Counseling.) Flag that this is the correct counselling content *because* the lesion is somatic, which is a non-obvious inference for a tumour named and catalogued alongside Mendelian paediatric syndromes.
- **Behavioural interventions, public-health interventions, environmental interventions, prophylaxis:** **none applicable.**

---

## 14. Other Species / Natural Disease

- **Taxonomy:** CCSK is described **only in humans** (`NCBITaxon:9606` *Homo sapiens*). No naturally occurring animal counterpart was found.
- **Breed:** not applicable; no VBO identifier.
- **Orthologous genes:** mouse *Bcor* (MGI; used in the mES models of §15), *Ywhae*, *Tp53*, *Tcf21* are all conserved. Human NCBI Gene IDs: BCOR 54880, YWHAE 7531. **I did not verify mouse NCBI Gene IDs in this session — look them up before curating.** BCOR is broadly conserved across vertebrates; PRC1.1 (BCOR–PCGF1–KDM2B–RNF2) is a deeply conserved chromatin module.
- **Natural disease in other species:** **none reported.** An OMIA search for a BCOR-associated renal sarcoma returns nothing; the naturally occurring canine hereditary renal cancer syndrome (renal cystadenocarcinoma and nodular dermatofibrosis, OMIA:001335-9615) is *FLCN/BHD*-driven and is **not** a CCSK model. **Veterinary relevance: none.**
- **Comparative pathology:** no cross-species comparison possible, because there is no animal disease to compare. The only comparative statement supportable is at the **pathway** level: PRC1.1 composition and function are conserved, and conditional *Bcor* mutation in mouse reproduces **OFCD-syndrome-like and extra-embryonic defects** (*Dev Biol* 2020, DOI 10.1016/j.ydbio.2020.07.004) — i.e. mouse *Bcor* loss models the **germline developmental** phenotype, **not** CCSK.
- **Transmission / zoonotic potential / cross-species susceptibility:** not applicable (non-infectious neoplasm).

---

## 15. Model Organisms

**This is the weakest area of CCSK research and the most consequential gap. There is no established CCSK cell line, no CCSK PDX, no genetically engineered mouse model of CCSK, and consequently no functional genomics (DepMap/CRISPR) data.** Everything below is a surrogate.

### Available models

| Model | Type | What it is | What it shows | Limitation | Reference |
|---|---|---|---|---|---|
| **BCOR-ITD HEK-293 (CRISPR knock-in)** | Cellular, in vitro, human | ITD introduced into the last exon of *BCOR* by CRISPR/Cas9 in HEK-293 | FGF3 treatment "*induced a significant increase in cell migration versus both untreated and scramble cell clone*"; "*FGF3 is able to promote cell migration, with the highest migration induction on cells carrying the BCOR-ITD*" | HEK-293 is an embryonic kidney-derived epithelial-like line of debated identity, **not a renal mesenchymal cell**; migration is a proxy for metastasis; no tumour formation assessed | PMID:36835166 |
| **BCOR-ITD neural stem cells (human + murine, lentiviral)** | Cellular, in vitro, human + mouse | WT or BCOR-ITD introduced into hNSC and mNSC | Murine *BCOR*ᴱ⁷⁻¹⁵-ITD "*significantly enhanced cellular proliferation and invasive capacity*"; derepression of PRC2 targets **PITX1, WNT11, GATA6**; **human NSCs showed transcriptional changes but no sustained growth advantage** | Neural, not renal — built for CNS-BCOR-ITD tumour, not CCSK; species-discordant result; overexpression construct | PMID:33920124 |
| **BCOR-ITD mouse ES cells → neuronal precursors (endogenous + transgenic)** | Cellular, in vitro, mouse | Endogenous and transgenic BCOR-ITD mES cells differentiated to neural precursors | vPRC1.1 composition and H2AK119ub **preserved**; minimal transcriptional change (32 up / 83 down at day 6) vs 344 up for BCOR truncation; aberrant CD24⁺CD26⁺ extra-embryonic-endoderm fate **only under PRC2 inhibition** | Mouse ES/neural, not renal; **directly contradicts the PRC1.1-disassembly model** derived from binding studies | PMID:40646718 |
| **786-O ccRCC line (TCF21 re-expression / decitabine)** | Cellular, in vitro, human | TCF21 restored in a hypermethylated RCC line | ~59% fewer cells migrated; reduced colony size; E-cadherin up, vimentin down; decitabine raised endogenous TCF21 | **A clear cell renal cell carcinoma line, not CCSK**; epithelial, adult, VHL-driven | PMID:29080283 |
| **Conditional *Bcor* mutant mouse** | Mammalian, in vivo, mouse | PRC1.1 gene *Bcor* conditional mutation | OFCD-syndrome and extra-embryonic defects | Models the **germline developmental** disease, **not CCSK**; truncating-type loss, not ITD | *Dev Biol* 2020, DOI 10.1016/j.ydbio.2020.07.004 |
| **Somatic gene delivery sarcoma models** | Mammalian, in vivo, mouse | >10 fusion-positive and fusion-negative sarcoma models by somatic gene delivery | A platform that *could* be applied to BCOR-ITD/YWHAE-NUTM2 | **No CCSK model reported in it**; a prospect, not a result | *Nat Commun* 2025, DOI 10.1038/s41467-025-60519-5 |

### Genetic model types available
Knock-in (CRISPR ITD in HEK-293), lentiviral overexpression (NSC), endogenous knock-in (mES), conditional knockout (mouse *Bcor*, germline phenotype). **No conditional, kidney-restricted, lineage-targeted *Bcor*-ITD mouse exists** — that is the model the field needs and does not have.

### Phenotype recapitulation and limitations
**No model recapitulates CCSK.** Not one of the systems above produces a renal mesenchymal tumour. The specific failures to record in a dismech entry, with the typed divergences that fit:
- **`BOUNDARY_OMISSION`** — the renal medullary mesenchymal compartment, its vascular niche, and the developing kidney are absent from every model.
- **`PROXY_QUANTITY`** — cell migration in HEK-293 stands in for metastasis; transcriptional derepression in NSCs stands in for tumour initiation.
- **`SPECIES_MISMATCH`** — the mNSC and hNSC results diverge (growth advantage in mouse, none in human), and the mES result diverges from the human structural prediction.
- **`SCALE_EXTRAPOLATION`** — all models observe at `MOLECULAR`/`CELLULAR` scale while the claims they are cited for are `TISSUE`/`ORGANISM`.

In dismech terms these all belong in `experimental_models:` (none is an animal model of the disease) with `relationship: PERTURBS` or `MEASURES` — **never `RECAPITULATES`** — `fidelity: LOW`, and `limitations` plus typed `divergences`. A `HUMAN_MODEL_MISMATCH` discussion is warranted and is well evidenced: the BCOR-ITD mechanism question is open **because** the models disagree with each other and none is renal.

### Research applications and resources
Current models support: BCOR-ITD effects on PRC1.1 composition and H2AK119ub; PRC1/PRC2 crosstalk; PRC2-target derepression; FGF3-driven migration; TCF21 tumour-suppressor function (in surrogate). They do **not** support: drug screening against CCSK, metastasis biology, cell-of-origin determination, or in vivo efficacy testing.
Resources to search: MGI, IMPC/KOMP/IMSR (for *Bcor* alleles), Cellosaurus and ATCC (**no CCSK line listed**), DepMap (**no CCSK line**), Alliance of Genome Resources.

---

## Highest-value open questions (for `discussions:` / `mechanistic_hypotheses:`)

1. **Is BCOR-ITD a loss-, gain-, or neomorphic-function allele?** Structural prediction (PMID:32628469) and mES knock-in data (PMID:40646718) disagree, and neither system is renal. `status: EMERGING`.
2. **What is the cell of origin?** Five candidates have been proposed since 2005 (PMID:16299227) and no single-cell study has resolved it.
3. **Why is CCSK male-predominant (IRR 3) when the driver is somatic and X-linked?** No published explanation found.
4. **What drives the YWHAE::NUTM2B/E branch?** Mutual exclusivity and distinct downstream signalling are established (PMID:26493387); the mechanism is not.
5. **Does driver class or TP53 status warrant risk-stratified therapy?** "*their prognostic relevance remains unknown*" (PMID:38396300); the TP53 signal (PMID:36563883) is underpowered at n=39.
6. **Why brain?** The relapse-site shift from bone to brain across treatment eras (PMID:30917048) is unexplained — drug CNS penetration, a tropism, or both.
7. **How can stage IV outcomes be improved beyond ~58–69% EFS?** The COG authors' own closing statement (PMID:38396300).
8. **A renal, lineage-targeted, conditional BCOR-ITD in vivo model** — the enabling resource for every question above.
9. **Quality of life and late effects in CCSK survivors** — no measurement exists.
10. **Molecular characterisation of adult CCSK** — "*the status of BCOR ITDs, YWHAE-NUTM2B/E fusion and hypermethylation of TCF21 in adult CCSKs is not clear*".

---

## Verified ontology term reference

All CURIEs below were resolved in this session against `cache/<prefix>/terms.csv` in this checkout, the EBI OLS4 API, or the HGNC REST API. Labels are as the authority returned them.

**Disease:** `MONDO:0005006` clear cell sarcoma of kidney · `NCIT:C4264` Clear Cell Sarcoma of the Kidney

**HPO:** `HP:0031500` Abdominal mass · `HP:0003270` Abdominal distention · `HP:0002027` Abdominal pain · `HP:0030157` Flank pain · `HP:0000790` Hematuria · `HP:0000822` Hypertension · `HP:0001903` Anemia · `HP:0000980` Pallor · `HP:0012378` Fatigue · `HP:0001945` Fever · `HP:0002013` Vomiting · `HP:0002017` Nausea and vomiting · `HP:0001824` Weight loss · `HP:0000126` Hydronephrosis · `HP:0009726` Renal neoplasm · `HP:0100242` Sarcoma · `HP:0002664` Neoplasm · `HP:0000077` Abnormality of the kidney · `HP:0030692` Brain neoplasm · `HP:0010622` Neoplasm of the skeletal system · `HP:0002653` Bone pain · `HP:0002756` Pathologic fracture · `HP:0002113` Pulmonary infiltrates · `HP:0002315` Headache · `HP:0001250` Seizure · `HP:0001254` Lethargy

*Coarse-binding warning:* `HP:0002664` Neoplasm, `HP:0000077` Abnormality of the kidney and `HP:0010622` Neoplasm of the skeletal system are in dismech's coarse set and will require a `coarse_binding_basis`. For the metastatic-site phenotypes, `SOURCE_UNSPECIFIED` or `NO_HPO_TERM` is the honest value — HPO has no "pulmonary metastasis" or "lymph node metastasis" term suited to these claims.

**GO:** `GO:0140261` BCOR complex (CC) · `GO:0035102` PRC1 complex (CC) · `GO:0140862` histone H2AK119 ubiquitin ligase activity (MF) · `GO:0000122` negative regulation of transcription by RNA polymerase II · `GO:0045814` negative regulation of gene expression, epigenetic · `GO:0006325` chromatin organization · `GO:0006338` chromatin remodeling · `GO:0010468` regulation of gene expression · `GO:0048762` mesenchymal cell differentiation · `GO:0008283` cell population proliferation · `GO:0016477` cell migration · `GO:0030335` positive regulation of cell migration · `GO:0007224` smoothened signaling pathway · `GO:0043491` phosphatidylinositol 3-kinase/protein kinase B signal transduction · `GO:0000165` MAPK cascade · `GO:0008543` fibroblast growth factor receptor signaling pathway · `GO:0048010` vascular endothelial growth factor receptor signaling pathway · `GO:0001525` angiogenesis · `GO:0001822` kidney development · `GO:0001656` metanephros development · `GO:0007219` Notch signaling pathway
**Do not use:** `GO:0006306` — OLS4 returns "obsolete DNA methylation". There is no GO BP term for histone H2AK119 monoubiquitination.

**CL:** `CL:0008019` mesenchymal cell · `CL:0000134` mesenchymal stem cell · `CL:1000692` kidney interstitial fibroblast · `CL:0000669` pericyte · `CL:1000497` kidney cell · `CL:0000057` fibroblast · `CL:0000047` neural stem cell (models only)

**UBERON:** `UBERON:0002113` kidney · `UBERON:0000362` renal medulla · `UBERON:0001225` cortex of kidney · `UBERON:0001224` renal pelvis · `UBERON:0001072` inferior vena cava · `UBERON:0000955` brain · `UBERON:0001474` bone element · `UBERON:0002481` bone tissue · `UBERON:0001434` skeletal system · `UBERON:0002048` lung · `UBERON:0000029` lymph node · `UBERON:0002107` liver · `UBERON:0002358` peritoneum

**CHEBI:** `CHEBI:28445` vincristine · `CHEBI:28748` doxorubicin · `CHEBI:4027` cyclophosphamide · `CHEBI:4911` etoposide · `CHEBI:31355` carboplatin · `CHEBI:27666` actinomycin D · `CHEBI:5864` ifosfamide · `CHEBI:749378` decitabine

**NCIT (treatment actions):** `NCIT:C15632` Chemotherapy · `NCIT:C15313` Radiation Therapy · `NCIT:C15329` Surgical Procedure · `NCIT:C51778` Radical Nephrectomy · `NCIT:C15284` Nephrectomy · `NCIT:C15986` Pharmacotherapy · `NCIT:C15747` Supportive Care · `NCIT:C16039` Autologous Hematopoietic Stem Cell Transplantation · `NCIT:C15431` Hematopoietic Cell Transplantation · `NCIT:C93352` Targeted Therapy · `NCIT:C49236` Therapeutic Procedure · `NCIT:C16722` Immunohistochemistry · `NCIT:C17563` Fluorescence In Situ Hybridization

**HGNC (dismech lowercase form):** `hgnc:20893` BCOR · `hgnc:12851` YWHAE · `hgnc:23445` NUTM2B · `hgnc:23448` NUTM2E · `hgnc:18709` CCNB3 · `hgnc:16272` MAML3 · `hgnc:11998` TP53 · `hgnc:11632` TCF21 · `hgnc:17615` PCGF1 · `hgnc:13610` KDM2B · `hgnc:10061` RNF2 · `hgnc:1001` BCL6 · `hgnc:1582` CCND1 · `hgnc:3527` EZH2 · `hgnc:3681` FGF3 · `hgnc:12680` VEGFA · `hgnc:11255` SPP1 · `hgnc:259` ADM · `hgnc:6206` JUND · `hgnc:8033` NTRK3 · `hgnc:3236` EGFR · `hgnc:6342` KIT · `hgnc:7809` NGFR · `hgnc:21637` SATB2 · `hgnc:11837` TLE1 · `hgnc:990` BCL2 · `hgnc:7656` NCAM1 · `hgnc:9004` PITX1 · `hgnc:12776` WNT11 · `hgnc:4174` GATA6

**NCBITaxon:** `NCBITaxon:9606` Homo sapiens

---

## Reference list with PMIDs

**Molecular drivers and mechanism**
- Ueno-Yokohata H, et al. Consistent in-frame internal tandem duplications of BCOR characterize clear cell sarcoma of the kidney. *Nat Genet.* 2015;47(8):861-3. **PMID:26098867**; doi:10.1038/ng.3338
- Roy A, et al. Recurrent internal tandem duplications of BCOR in clear cell sarcoma of the kidney. *Nat Commun.* 2015;6:8891. **PMID:26573325**; doi:10.1038/ncomms9891
- Astolfi A, et al. Whole transcriptome sequencing identifies BCOR internal tandem duplication as a common feature of clear cell sarcoma of the kidney. *Oncotarget.* 2015;6(38):40934-9. **PMID:26516930**
- O'Meara E, et al. Characterization of the chromosomal translocation t(10;17)(q22;p13) in clear cell sarcoma of kidney. *J Pathol.* 2012;227(1):72-80. **PMID:22294382**
- Karlsson J, Valind A, Gisselsson D. BCOR internal tandem duplication and YWHAE-NUTM2B/E fusion are mutually exclusive events in clear cell sarcoma of the kidney. *Genes Chromosomes Cancer.* 2016;55(2):120-3. **PMID:26493387**
- Kenny C, et al. Mutually exclusive BCOR internal tandem duplications and YWHAE-NUTM2 fusions in clear cell sarcoma of kidney: not the full story. *J Pathol.* 2016;238(5):617-20. **PMID:27000436**
- Wong MK, et al. Clear cell sarcomas of the kidney are characterised by BCOR gene abnormalities, including exon 15 internal tandem duplications and BCOR-CCNB3 gene fusion. *Histopathology.* 2018;72(2):320-9. **PMID:28833375**
- Gooskens SL, et al. The clinical phenotype of YWHAE-NUTM2B/E positive pediatric clear cell sarcoma of the kidney. *Genes Chromosomes Cancer.* 2016;55(2):143-7. **PMID:26542179**
- Zhang M, et al. Clinical relevance of BCOR internal tandem duplication and TP53 aberration in clear cell sarcoma of the kidney. *Hum Pathol.* 2023;134:45-55. **PMID:36563883**
- Fiore M, et al. Molecular Signature of Biological Aggressiveness in Clear Cell Sarcoma of the Kidney (CCSK). *Int J Mol Sci.* 2023;24(4):3743. **PMID:36835166**; doi:10.3390/ijms24043743
- Gooskens SL, et al. TCF21 hypermethylation in genetically quiescent clear cell sarcoma of the kidney. *Oncotarget.* 2015;6(18):15828-41. **PMID:26158413**
- Gooskens SL, et al. TCF21 hypermethylation regulates renal tumor cell clonogenic proliferation and migration. *Mol Oncol.* 2018;12(2):166-79. **PMID:29080283**
- Cutcliffe C, et al. Clear cell sarcoma of the kidney: up-regulation of neural markers with activation of the sonic hedgehog and Akt pathways. *Clin Cancer Res.* 2005;11(22):7986-94. **PMID:16299227**
- Wong KM/Ng D, et al. Structure and Role of BCOR PUFD in Noncanonical PRC1 Assembly and Disease. *Biochemistry.* 2020;59(28):2718-28. **PMID:32628469**
- Dhoondia Z, Kang H, Lee K, Cole PA, Kuroda MI. Analysis of a BCOR internal tandem duplication in mouse embryonic stem cell to neuronal precursor differentiation. *Genetics.* 2025;231(1):iyaf133. **PMID:40646718**; doi:10.1093/genetics/iyaf133
- Nakata S, et al. BCOR Internal Tandem Duplication Expression in Neural Stem Cells Promotes Growth, Invasion, and Expression of PRC2 Targets. *Int J Mol Sci.* 2021;22(8):3913. **PMID:33920124**

**Pathology and diagnosis**
- Argani P, Perlman EJ, Breslow NE, Browning NG, Green DM, D'Angio GJ, Beckwith JB. Clear cell sarcoma of the kidney: a review of 351 cases from the National Wilms Tumor Study Group Pathology Center. *Am J Surg Pathol.* 2000;24(1):4-18. **PMID:10632483**
- Aldera AP, Pillay K. Clear Cell Sarcoma of the Kidney. *Arch Pathol Lab Med.* 2020;144(1):119-23. **PMID:30917048**
- Kao YC, et al. BCOR Overexpression Is a Highly Sensitive Marker in Round Cell Sarcomas With BCOR Genetic Abnormalities. *Am J Surg Pathol.* 2016;40(12):1670-8. **PMID:27428733**
- Singh V, Gupta K, Saraswati A, Peters NJ, Trehan A. Role of Cyclin D1 and BCOR Immunohistochemistry in Differentiating Clear Cell Sarcoma of Kidney From its Mimics. *J Pediatr Hematol Oncol.* 2021;43(8):294-300. **PMID:34673711**
- Argani P, et al. BCOR Overexpression in Renal Malignant Solitary Fibrous Tumors: A Close Mimic of Clear Cell Sarcoma of Kidney. *Am J Surg Pathol.* 2019;43(6):773-82. **PMID:30864973**
- Pediatric BCOR-Altered Tumors From Soft Tissue/Kidney Display Specific DNA Methylation Profiles. *Mod Pathol.* 2023;36(2):100039. **PMID:36853789**; doi:10.1016/j.modpat.2022.100039
- Zhang M, et al. Development, optimization and application of a universal fluorescence multiplex PCR-based assay to detect BCOR genetic alterations in pediatric tumors. *Diagn Pathol.* 2025;20(1):11. **PMID:39871307**
- Goh JY, et al. Paediatric BCOR-associated sarcomas with a novel long spliced internal tandem duplication of BCOR exon 15. *J Pathol Clin Res.* 2022. **PMID:35836306**
- Xing ZW, Wang XL, Chen L. [YWHAE-rearranged clear cell sarcoma of kidney: a clinicopathological analysis of seven cases]. *Zhonghua Bing Li Xue Za Zhi.* 2026;55(2):140-6. **PMID:41644425** (Chinese)
- Dorwal P, et al. Clear Cell Sarcoma of the Kidney (CCSK) With BCOR-CCNB3 Fusion: A Rare Case Report With a Brief Review of the Literature. *Pediatr Dev Pathol.* 2023. **PMID:36533315**

**Clinical cohorts, treatment and outcome**
- Benedetti DJ, Renfro LA, Tfirn I, et al. Treatment and outcomes of clear cell sarcoma of the kidney: A report from the Children's Oncology Group studies AREN0321 and AREN03B2. *Cancer.* 2024;130(13):2361-71. **PMID:38396300**; doi:10.1002/cncr.35266
- Seibel NL, Chi YY, Perlman EJ, et al. Impact of cyclophosphamide and etoposide on outcome of clear cell sarcoma of the kidney treated on the National Wilms Tumor Study-5 (NWTS-5). *Pediatr Blood Cancer.* 2019;66(1):e27450. **PMID:30255545**
- Seibel NL, Li S, Breslow NE, et al. Effect of duration of treatment on treatment outcome for patients with clear-cell sarcoma of the kidney: a report from the National Wilms' Tumor Study Group. *J Clin Oncol.* 2004;22(3):468-73. **PMID:14752069**
- Kalapurakal JA, Perlman EJ, Seibel NL, et al. Outcomes of patients with revised stage I clear cell sarcoma of kidney treated in National Wilms Tumor Studies 1-5. *Int J Radiat Oncol Biol Phys.* 2013;85(2):428-31. **PMID:22658515**
- Furtwängler R, Gooskens SL, van Tinteren H, et al. Clear cell sarcomas of the kidney registered on International Society of Pediatric Oncology (SIOP) 93-01 and SIOP 2001 protocols: a report of the SIOP Renal Tumour Study Group. *Eur J Cancer.* 2013;49(16):3497-506. **PMID:23880476**
- Gooskens SL, Furtwängler R, Spreafico F, et al. Treatment and outcome of patients with relapsed clear cell sarcoma of the kidney: a combined SIOP and AIEOP study. *Br J Cancer.* 2014;111(2):227-33. **PMID:24937667**
- Gooskens SL, Graf N, Furtwängler R, et al. Position paper: Rationale for the treatment of children with CCSK in the UMBRELLA SIOP-RTSG 2016 protocol. *Nat Rev Urol.* 2018;15(5):309-19. **PMID:29485128**
- Gooskens SL, Furtwängler R, Vujanic GM, Dome JS, Graf N, van den Heuvel-Eibrink MM. Clear cell sarcoma of the kidney: a review. *Eur J Cancer.* 2012;48(14):2219-26. **PMID:22579455**
- Gao H, Cheng QY, Zhao Q, Tao LX, Zhang C. Childhood Clear Cell Sarcoma of Kidney: Incidence and Survival. *Front Pediatr.* 2021;9:675373. **PMID:34095035**; doi:10.3389/fped.2021.675373
- Zhang A, Yuan X, Jiang S, et al. Outcomes of children with clear cell sarcoma of kidney following NWTS strategies in Shanghai China (2003-2021). *PLoS One.* 2024;19(7):e0306863. **PMID:38980838**
- Zhang Y, Chu Q, Ma Y, Miao C, Diao JJ. Overall survival nomogram and relapse-related factors of clear cell sarcoma of the kidney: A study based on published patients. *Front Pediatr.* 2022;10:943141. **PMID:36186639**
- McKay KG, Beckhorn C, Kontchou NAT, et al. Renal sarcomas in children and adolescents: a retrospective, multicenter cohort study. *eClinicalMedicine.* 2025. **PMID:41509607**; doi:10.1016/j.eclinm.2025.103713
- Friesenbichler W, et al. Clear cell sarcoma of the kidney in Austrian children: Long-term survival after relapse. *Pediatr Blood Cancer.* 2021. **PMID:33438324**
- Welter N, et al. How to improve initial diagnostic accuracy of kidney tumours in childhood? A non-invasive approach. *Int J Cancer.* 2024;154(11):1955-66. **PMID:38319190**
- Brok J, Treger TD, Gooskens SL, van den Heuvel-Eibrink MM, Pritchard-Jones K. Biology and treatment of renal tumours in childhood. *Eur J Cancer.* 2016. **PMID:27969569**

**Reviews and background**
- Hallmark discoveries in the biology of non-Wilms tumour childhood kidney cancers. *Nat Rev Urol.* 2024. doi:10.1038/s41585-024-00993-6 (**paywalled; PMID not verified in this session**)
- Relapsed rhabdoid tumours and other non-nephroblastoma childhood and adolescent kidney tumours: perspectives from the HARMONICA collaboration. *Nat Rev Urol.* 2025. doi:10.1038/s41585-025-01117-4 (**paywalled; PMID not verified**)
- OMIM. BCL6 COREPRESSOR; BCOR. **`OMIM:300485`**. https://omim.org/entry/300485
- Orphanet. Clear cell sarcoma of kidney. **ORPHA:457246**. https://www.orpha.net/en/disease/detail/457246

---

## Caveats a curator must act on before writing YAML

1. **Re-fetch every reference and re-verify every snippet.** My retrieval returned several abstracts as summaries with embedded quoted fragments rather than full text. Only the following were returned as complete verbatim abstracts and are the safest snippet sources: PMID:26098867, PMID:26573325, PMID:26516930, PMID:26158413, PMID:28833375, PMID:36563883, PMID:36835166, PMID:30255545, PMID:22579455. For everything else, fetch first and quote from the cache.
2. **Do not curate `inheritance:`, penetrance, carrier frequency, allele frequency, or prenatal/carrier screening.** They are category errors for this disease.
3. **`HP:0001442` does not apply.** CCSK is a tumour-restricted somatic driver, not constitutional mosaicism; the `somatic-mosaicism` skill's exclusion cases cover this.
4. **Cancer granularity (design decisions §3a):** CCSK is a **histologic entity** at the WHO/ICD-O level (8964/3) and is correctly a single `Disease` entry. The three driver classes are **not** promoted strata — they fail the §3a test (no stratum-specific first-line therapy, no distinct diagnostic pathway; prognostic relevance explicitly "unknown", PMID:38396300). Record them as `has_subtypes` rows on the parent, or as `genetic:` records, not as separate entries. `Metastatic_CCSK` must not be created.
5. **Cell of origin is derived, not a slot.** Mark the BCOR ITD node with `genetic_context: {variant_origin: SOMATIC, functional_impact_category: PARTIAL_LOSS_OF_FUNCTION}` and bind its `cell_types` to `CL:0008019`; `just check-cancer-origin` will then derive a single origin. Avoid annotating two candidate cells on that node — multi-origin derivation is dismech's lump/split signal and would misfire here.
6. **Module conformance candidates** worth checking with `just list-modules` before creating anything new: the hallmarks-of-cancer family (`sustaining_proliferative_signaling` for the cyclin D1/MAPK axis; `evading_growth_suppressors` for TP53 loss; `inducing_angiogenesis` for the VEGFA/ADM signature; `invasion_and_metastasis` for the brain/bone/lung dissemination). A **Polycomb/chromatin-dysregulation** module would be the natural home for the PRC1.1 mechanism — check whether one already exists under a name you would not guess.
7. **`GO:0006306` is obsolete** and `GO:0001837` (EMT) does not describe CCSK itself. Both would pass `linkml-validate`; one would be wrong and the other would trip `just check-logical-rules`.
8. **The `environmental:` section's content is a documented negative**, and needs the `Left deliberately uncited.` waiver with the searches named, not an empty block.

**Sources:** [Nat Genet 2015 (BCOR ITD)](https://pubmed.ncbi.nlm.nih.gov/26098867/) · [Nat Commun 2015 (BCOR ITD)](https://www.nature.com/articles/ncomms9891) · [Oncotarget 2015 (WTS)](https://pubmed.ncbi.nlm.nih.gov/26516930/) · [J Pathol 2012 (t(10;17))](https://pubmed.ncbi.nlm.nih.gov/22294382/) · [Genes Chromosomes Cancer 2016 (mutual exclusivity)](https://onlinelibrary.wiley.com/doi/10.1002/gcc.22316) · [J Pathol 2016 (not the full story)](https://pathsocjournals.onlinelibrary.wiley.com/doi/10.1002/path.4693) · [Histopathology 2018 (BCOR-CCNB3)](https://pubmed.ncbi.nlm.nih.gov/28833375/) · [Hum Pathol 2023 (TP53)](https://www.sciencedirect.com/science/article/pii/S0046817722002854) · [IJMS 2023 (metastatic signature)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9964999/) · [Oncotarget 2015 (TCF21)](https://pubmed.ncbi.nlm.nih.gov/26158413/) · [Mol Oncol 2017 (TCF21 function)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5792742/) · [Clin Cancer Res 2005 (neural/SHH/AKT)](https://aacrjournals.org/clincancerres/article/11/22/7986/186613/) · [Biochemistry 2020 (PUFD structure)](https://pubs.acs.org/doi/10.1021/acs.biochem.0c00285) · [Genetics 2025 (BCOR-ITD mES)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12875675/) · [IJMS 2021 (BCOR-ITD NSC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8070097/) · [Am J Surg Pathol 2000 (351 cases)](https://pubmed.ncbi.nlm.nih.gov/10632483/) · [Arch Pathol Lab Med 2020 (review)](https://pubmed.ncbi.nlm.nih.gov/30917048/) · [J Pediatr Hematol Oncol 2021 (cyclin D1/BCOR IHC)](https://pubmed.ncbi.nlm.nih.gov/34673711/) · [Am J Surg Pathol 2019 (SFT mimic)](https://pubmed.ncbi.nlm.nih.gov/30864973/) · [Mod Pathol 2023 (methylation classes)](https://www.modernpathology.org/article/S0893-3952(22)00039-4/fulltext) · [Diagn Pathol 2025 (multiplex assay)](https://pubmed.ncbi.nlm.nih.gov/39871307/) · [Cancer 2024 (AREN0321/AREN03B2)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11162327/) · [Pediatr Blood Cancer 2019 (NWTS-5)](https://pubmed.ncbi.nlm.nih.gov/30255545/) · [Eur J Cancer 2013 (SIOP)](https://pubmed.ncbi.nlm.nih.gov/23880476/) · [Br J Cancer 2014 (relapse)](https://pubmed.ncbi.nlm.nih.gov/24937667/) · [Nat Rev Urol 2018 (UMBRELLA)](https://www.nature.com/articles/nrurol.2018.14) · [Eur J Cancer 2012 (review)](https://pubmed.ncbi.nlm.nih.gov/22579455/) · [Front Pediatr 2021 (SEER)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8173214/) · [PLoS One 2024 (Shanghai)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11233012/) · [Front Pediatr 2022 (nomogram)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9523514/) · [eClinicalMedicine 2025 (renal sarcomas)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12775861) · [Orphanet ORPHA:457246](https://www.orpha.net/en/disease/detail/457246) · [OMIM 300485](https://omim.org/entry/300485) · [Pathology Outlines — CCSK](https://www.pathologyoutlines.com/topic/kidneytumorclearcellsarcoma.html) · [Atlas of Genetics — CCSK](https://atlasgeneticsoncology.org/solid-tumor/209016/clear-cell-sarcoma-of-the-kidney) · [NCI PDQ — Wilms Tumor and Other Childhood Kidney Tumors](https://www.cancer.gov/types/kidney/hp/wilms-treatment-pdq)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 76 |
| Resolved | 76 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 33 |
| Quoted claims found in source | 23 |
| Quoted claims **not** found in source | 10 |
| References weighed for topical relevance | 76 |
| On topic | 57 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

5 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:29485128` *(abstract only)*: "*rely on doxorubicin, which is associated with side effects of cardiotoxicity, nephrotoxicity, and fertility risks*"
  - Text part not found as substring: '*rely on doxorubicin, which is associated with side effects of cardiotoxicity, nephrotoxicity, and fertility risks*' (note: only abstract available for PMID:29485128, full text may contain this excerpt)
- `PMID:26158413` *(abstract only)*: "*No recurrent segmental chromosomal copy number changes…were identified*"
  - closest text in source: "No recurrent segmental chromosomal copy number changes or somatic variants (single nucleotide or small insertion/deletion) were identified"
- `PMID:26158413` *(abstract only)*: "*promoter hypermethylation and low expression of the tumor suppressor gene TCF21… in all CCSKs except the case with t(10;17)*"
  - closest text in source: "Integrated analysis of expression and methylation data identified promoter hypermethylation and low expression of the tumor suppressor gene TCF21 (Pod-1/capsulin/epicardin) in all CCSKs except the case with t(10;17)(q22;p13)"
- `PMID:24937667`: "*Fifty-nine percent achieved second complete remission, though 68% of these developed subsequent relapse*"
  - closest text in source: "Twenty-two out of thirty-seven patients (59%) achieved a second complete remission (CR); 15 of whom (68%) developed a second relapse"
- `PMID:38396300`: "*routine interval nuclear medicine imaging for bone recurrences may not be needed*"
  - closest text in source: "This indicates an ongoing shift toward more relapses occurring in the brain rather than the bone or lungs, as seen on NWTS-55 and in SIOP studies.12,14 These findings underscore the importance of obtaining brain imaging at diagnosis and during post-treatment surveillance, and suggest that routine interval nuclear medicine imaging for bone recurrences as required on AREN0321 may not be needed"
- `PMID:30917048` *(abstract only)*: "*frequently mimics other pediatric renal tumors, causing misdiagnosis*"
  - closest text in source: "Histologically, this tumor exhibits a great diversity of morphologic patterns that can mimic most other pediatric renal neoplasms, often leading to confusion and misdiagnosis"
- `PMID:38396300`: "*appeared to benefit from a carboplatin-containing regimen, though their outcomes remain unsatisfactory*"
  - closest text in source: "Patients with stage IV disease appeared to benefit from a carboplatin-containing regimen, although their outcomes remained unsatisfactory"
- `PMID:24937667`: "*5-year event-free survival (EFS) after relapse was 18% (95% CI: 4%-32%), and 5-year overall survival (OS) was 26%*"
  - closest text in source: "Five-year event-free survival (EFS) after relapse was 18% (95% CI: 4%-32%), and 5-year overall survival (OS) was 26% (95% CI: 10%-42%)"
- `PMID:16299227` *(abstract only)*: "*suggesting therapeutic potential*"
  - Text part not found as substring: '*suggesting therapeutic potential*' (note: only abstract available for PMID:16299227, full text may contain this excerpt)
- `PMID:38396300`: "*their prognostic relevance remains unknown*"
  - closest text in source: "Cox proportional hazards models were used to assess the prognostic impact of age at diagnosis in the entire study-pooled cohort, while the prognostic effects of lymph node (LN) involvement, initial procedure type, and nephrectomy margin status were assessed in local stage III patients from both studies combined"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 106 |
| Resolved | 99 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 4 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005006` (4 mentions) - the report calls it "Mondo"; MONDO calls it **clear cell sarcoma of kidney**
- `NCIT:C4264` (4 mentions) - the report calls it "NCIT"; NCIT calls it **Clear Cell Sarcoma of the Kidney**
- `DOID:4880` (1 mention) - the report calls it "DOID"; DOID calls it **kidney clear cell sarcoma**
- `EFO:0000350` (1 mention) - the report calls it "EFO"; EFO calls it **obsolete_clear cell sarcoma of the kidney**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006306` (obsolete DNA methylation) (4 mentions)
- `EFO:0000350` (obsolete_clear cell sarcoma of the kidney) (1 mention) - replaced by `http://purl.obolibrary.org/obo/MONDO:0005006`
- `NCIT:C16722` (Immunohistochemistry) (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `OMIA`.
