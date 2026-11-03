---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T13:11:55.803734'
end_time: '2026-10-16T13:13:41.814436'
duration_seconds: 106.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 20
  mondo_id: MONDO:0054724
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
  web_search_requests: 3
  num_turns: 8
  total_cost_usd: 0.8667659999999998
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 6
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 6
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 1
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0012206
    reported_labels:
    - Asthenozoospermia
    ontology_label: Abnormal sperm motility
  - term_id: HP:0012869
    reported_labels:
    - unverified
    ontology_label: Acephalic spermatozoa
  - term_id: HP:0000007
    reported_labels:
    - verify
    ontology_label: Autosomal recessive inheritance
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 20
- **MONDO ID:** MONDO:0054724 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 20** covering all of the
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

I've finished searching and am now writing the report. I verified the CFAP44 identity, the two core papers, and the ICSI and mouse findings. Everything else is labeled as unverified or general knowledge.

# Spermatogenic Failure 20 (SPGF20; CFAP44-related MMAF): Research Report

**Evidence status.** Verified this session: gene and disease identifiers, the Tang 2017 and Coutton 2018 findings, the ICSI series, and the mouse data. Unverified: items marked **[unverified]** come from general knowledge or from search snippets I did not open. Check them before curation. I did not verify OMIM prose, HPO frequencies, GO/CL/UBERON identifiers, or ClinGen validity. I also quote no exact abstract text, because I read only the Coutton paper's full text, and only partially. The CLAUDE.md rules require the snippets to be exact quotes, so take snippets from `just fetch-reference`, not from this report.

## 1. Disease information

- **Overview.** SPGF20 is an autosomal recessive form of male infertility. The underlying defect is "multiple morphological abnormalities of the sperm flagella" (MMAF), also called asthenoteratozoospermia with flagellar defects. Sperm tails are absent, short, coiled, bent or of irregular caliber. Men are otherwise typically healthy. Sperm count can be normal, but sperm are almost immotile.
- **Identifiers.**
  - MONDO:0054724 (the repository stub names CFAP44 as MONDO's causal gene).
  - OMIM phenotype 617593; OMIM gene 617559 (CFAP44, 3q13.2). A search-derived [DrugMap record](https://drugmap.idrblab.net/data/disease/details/DISPF5HX) and a [PMC 2023 table](https://pmc.ncbi.nlm.nih.gov/articles/PMC10042652/table/T1) agree on the pairing.
  - Orphanet, ICD and MeSH identifiers: not checked.
- **Synonyms.** Spermatogenic failure 20; SPGF20; MMAF type 20 [unverified]. CFAP44 was formerly WDR52 [unverified].
- **Data source.** Disease-level, aggregated from family and cohort sequencing, not EHR.
- **Repository state.** `stubs/Spermatogenic_Failure_20.yaml` exists, with `entry_type: UNDECIDED`. No `kb/disorders` entry exists yet.
- **Lump/split note.** Many SPGF entries share the same MMAF phenotype (CFAP43, DNAH1, CFAP69, ARMC2 and others). A curator should keep SPGF20 as a gene-defined disease entry and consider a covering MMAF grouping.

## 2. Etiology

- **Cause.** Biallelic loss-of-function variants in *CFAP44* (cilia- and flagella-associated protein 44).
- **Genetic risk factors.** No modifier genes are established. Digenic CFAP43/CFAP44 involvement has not been shown. CFAP43 and CFAP44 variants are found in separate patients.
- **Environmental factors.** None established for this form. The known MMAF causes are genetic.
- **Protective factors and gene-environment interactions.** None known.

## 3. Phenotypes

All items below are for male patients. Female carriers are not reported to be affected.

| Phenotype | Suggested HPO | Evidence |
|---|---|---|
| Male infertility | HP:0003251 | Core feature (PMID:28552195; PMID:29449551) |
| Asthenozoospermia | HP:0012206 | Near-universal [unverified ID] |
| Teratozoospermia / flagellar abnormalities | HP:0012864 | Absent, short, coiled and irregular-caliber flagella |
| Abnormal sperm tail morphology | HP:0012869 [unverified] | MMAF |

- **Frequencies.** In CFAP44 patients from Coutton 2018 (PMID:29449551), mean absent flagella were 36.8%, short flagella 52.2% and irregular-caliber flagella 28.4%.
- **Onset, progression and quality of life.** Onset is at reproductive age and the phenotype is stable. Infertility is the presenting complaint. No quality-of-life data were found.
- **Verify every HPO CURIE with a lookup before binding.** Per CLAUDE.md, I wrote none of these from a source in this session.

## 4. Genetic/molecular information

- **Gene.** *CFAP44*, HGNC symbol (lowercase `hgnc:` form in the KB, number to be looked up), 3q13.2.
- **Variants (Coutton 2018, PMID:29449551, Table 2).** All six patients were homozygous.
  - c.1890+1G>A (p.Pro631Ile*22), splice site, Tunisia.
  - c.3175C>T (p.Arg1059Ter), nonsense, Tunisia.
  - c.2818dupG (p.Glu940GlyfsTer19), frameshift, Morocco.
  - c.1387G>T (p.Glu463Ter), nonsense, two patients, Algeria.
  - c.4767delT (p.Ile1589MetfsTer6), frameshift, Algeria.
  - The paper's text gives the first variant as c.1890+1C>T, which conflicts with the table. Resolve this against the source before curating.
- **Tang 2017 (PMID:28552195).** A homozygous frameshift in CFAP44 was found in 1 of 30 Han Chinese MMAF men. Compound-heterozygous CFAP43 variants were found in 3 other men. These variants were absent in 984 controls.
- **Functional consequence.** Loss of function (nonsense, frameshift, splice). Origin is germline.
- **Gene share.** CFAP44 explained 6 of 78 men (7.7%) in Coutton 2018. CFAP43 and CFAP44 together explained about 20.5%. The cohort was mainly North African, so the share is cohort-dependent.
- **Epigenetics and chromosomal abnormalities.** None reported.
- **Population frequency (gnomAD) and ClinVar classifications.** Not retrieved.

## 5. Environmental information

None established. Infectious agents are not applicable.

## 6. Mechanism / pathophysiology

**Causal chain**

1. Biallelic loss-of-function variants in *CFAP44* produce absent or truncated CFAP44 protein. This is demonstrated by genetics and inferred at the protein level.
2. CFAP44 is lost from the sperm axoneme. In the *T. brucei* ortholog, it localizes next to the paraflagellar rod, apposed to doublets 5–6 (PMID:29449551).
3. Axonemal organization fails. In patient sperm, TEM showed about 95% abnormal cross-sections in one patient, most often lacking the central pair (9+0, 66.7%). Reduced SPAG6 and RSPH1 staining implicates central-pair and radial-spoke components.
4. Flagellar assembly and beating fail, so tails are absent, short or coiled and motility is reduced. This step is established in humans and mice.
5. Sperm are immotile and structurally abnormal, which causes male infertility.

Evidence by model system:
- **Human:** MMAF patients with biallelic variants (above).
- **Mouse:** Cfap44 knockout males are infertile with MMAF, and females are fertile (PMID:28552195).
- **Trypanosome:** RNAi knockdown of TbCFAP44 gave abnormal beating, growth arrest and multiflagellated cells. Axonemal defects were found in 27.3% of axonemes versus 0.6% of controls.

Cell and tissue targets:
- **Cell type:** spermatid or sperm (CL term to look up).
- **Tissue:** testis.
- **Components:** axoneme, sperm flagellum (GO terms to look up).
- **Biological processes:** sperm flagellum assembly, spermatid differentiation.
- **Omics and other mechanisms.** No metabolic, immune, proteomic or single-cell findings were retrieved. A 2025 Mol Hum Reprod study (Muroňová et al.) compared mouse knockouts. Cfap44-/- sperm had the mildest nuclear defects and the lowest embryo-developmental failure among the knockouts compared (Cfap43, Armc2, Ccdc146) (per a search summary; paper not opened).

## 7. Anatomical structures affected

- **Organ:** testis and sperm. Other organs are not involved, and there is no ciliary syndrome in these patients. That statement is from the literature picture, not from a source I checked. Primary ciliary dyskinesia-like features are reported for some other MMAF genes, not for CFAP44 [unverified].
- **Cell level:** spermatids and spermatozoa. Subcellular: axoneme and flagellum.
- Lateralization: not applicable (systemic germline).

## 8. Temporal development

Onset is at reproductive age (detected on infertility workup). Stable, lifelong, with no remission.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007 – verify).
- **Penetrance and sex:** limited to males. Females are unaffected in mice.
- **Consanguinity:** the Coutton 2018 CFAP44 patients were all homozygous. Consanguinity is likely in the North African cohort. Verify this against the full text.
- **Founder effects:** none established.
- **Prevalence:** unknown. MMAF is rare, and CFAP44 accounts for about 7.7% of the MMAF cohort studied.

## 10. Diagnostics

- **Semen analysis:** asthenozoospermia with flagellar abnormalities on morphology.
- **Electron microscopy and immunostaining:** central-pair and axoneme defects (TEM); SPAG6 and RSPH1 staining.
- **Genetic testing:** whole-exome sequencing or an MMAF gene panel. WES in 78 MMAF men gave a diagnosis in 22 (28%) across DNAH1, CFAP43 and CFAP44.
- **Differential diagnosis:** other MMAF genes (DNAH1, CFAP43, CFAP69, ARMC2 and others) and primary ciliary dyskinesia.
- **Screening:** none.

## 11. Outcome/prognosis

Life expectancy is normal, and the burden is infertility. Assisted reproduction outcomes in a small retrospective series (6 MMAF patients with biallelic CFAP44 or CFAP43 variants; [Frontiers in Endocrinology 2024](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1377780/full)):
- For CFAP44, ICSI gave 76.47% fertilization, 88.46% transferable embryos, 50% pregnancy and 50% delivery.
- Fertilization was significantly higher than in the DNAH1 group.
- Samples were very small. Coutton 2018 does not report ICSI outcomes for CFAP44.
- Also check Coutton 2018's own discussion, which says ICSI prognosis is hard to predict for non-DNAH1 genotypes.

## 12. Treatment

- No curative or drug therapy exists.
- **Intracytoplasmic sperm injection (ICSI)** is the main option, with the outcomes above (NCIT term to look up; the repository table suggests a procedure term, but look up the CURIE rather than trusting memory).
- Gene therapy and other advanced approaches: none found. Clinical trials: none found, and I did not search ClinicalTrials.gov.

## 13. Prevention

- Genetic counseling for couples. A male partner's biallelic status confers 100% transmission of one pathogenic allele to children, who would be carriers. This is inferred from recessive inheritance.
- Preimplantation genetic testing is possible if the variants are known. This is general knowledge and was not verified.

## 14. Other species

I did not search OMIA or ortholog databases. The mouse ortholog is *Cfap44*, and the Trypanosoma ortholog is TbCFAP44 (NCBITaxon IDs and NCBI Gene IDs to look up).

## 15. Model organisms

- **Mouse:** CRISPR/Cas9 Cfap44 knockout. Males are infertile with MMAF and peri-axonemal and axonemal defects. Females are fertile (PMID:28552195). This is `MODEL_ORGANISM` evidence, and the model recapitulates the human phenotype well. Since 2025, comparative data show milder nuclear and embryo-development defects than other MMAF knockouts.
- **Trypanosoma brucei:** RNAi knockdown with flagellar defects (PMID:29449551). The relevance to human spermatogenesis is by homology only.
- **Resources:** MGI and IMPC (not queried here).

## Evidence summary for curation

| Claim | PMID | Evidence source |
|---|---|---|
| CFAP44 homozygous frameshift in an MMAF man; CFAP43 compound-heterozygous variants; absent in 984 controls | 28552195 | HUMAN_CLINICAL |
| 22 of 78 MMAF men with biallelic DNAH1, CFAP43 or CFAP44 variants (CFAP44 n=6); Cfap43/44 knockout mice infertile; Trypanosoma RNAi | 29449551 | HUMAN_CLINICAL, MODEL_ORGANISM |
| ICSI outcomes for CFAP44 patients | See Frontiers 2024 link above (PMID not retrieved) | HUMAN_CLINICAL |
| Cfap44 knockout nuclear and embryo-development comparison | Muroňová 2025 (PMID not retrieved) | MODEL_ORGANISM |

**Next steps before curation.** Run `just fetch-reference` for PMIDs 28552195 and 29449551. Look up every HPO, GO, CL and UBERON CURIE. Resolve the c.1890+1G>A versus C>T discrepancy. Retrieve the PMIDs for the ICSI series and the 2025 knockout comparison. Also check ClinGen validity for CFAP44-MMAF and the GeneReviews baseline (`just check-genereviews`).

Sources:
- [DrugMap SPGF20 record](https://drugmap.idrblab.net/data/disease/details/DISPF5HX)
- [PMC 2023 gene table](https://pmc.ncbi.nlm.nih.gov/articles/PMC10042652/table/T1)
- [Coutton et al. 2018, Nat Commun (PMC5814398)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5814398/)
- [Tang et al. 2017 AJHG (PMID 28552195)](https://scicrunch.org/ASWG/literature/pmid:28552195?rpKey=on)
- [Frontiers in Endocrinology 2024 review/ICSI series](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1377780/full)
- [Muroňová et al. 2025, Mol Hum Reprod (HAL record)](https://archivesic.ccsd.cnrs.fr/IAB_GETI/hal-05354598v1)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 5 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012206` (1 mention) - the report calls it "Asthenozoospermia"; HP calls it **Abnormal sperm motility**
- `HP:0012869` (1 mention) - the report calls it "unverified"; HP calls it **Acephalic spermatozoa**
- `HP:0000007` (1 mention) - the report calls it "verify"; HP calls it **Autosomal recessive inheritance**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012864` (1 mention) - the report calls it "Teratozoospermia / flagellar abnormalities"; HP calls it **Abnormal sperm morphology**, and lists "Teratozoospermia" among its other names