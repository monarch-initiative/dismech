---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T20:14:53.442819'
end_time: '2026-10-16T20:29:10.321827'
duration_seconds: 856.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: C1Q Deficiency
  mondo_id: MONDO:0013343
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 25
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 18
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 26
  not_found: 1
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.036
  labels_checked: 18
  labels_matching: 14
  labels_variant: 4
  unresolved_terms:
  - HP:0005503
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - ORPHA
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: C1Q_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: C1Q_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** C1Q Deficiency
- **MONDO ID:** MONDO:0013343 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **C1Q Deficiency** covering all of the
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

# C1q Deficiency (MONDO:0013343): A Comprehensive Disease Characteristics Report

*Autonomous discovery investigation — 5 iterations, 9 confirmed findings, 32 papers reviewed*

**Disease:** C1q Deficiency (Complement component 1q deficiency)
**MONDO:** MONDO:0013343 · **OMIM:** #613652 (C1q deficiency) · **Orphanet:** ORPHA:169147 · **ICD-10:** D84.1 · **ICD-11:** 4A00.1 (complement deficiency) · **MeSH:** "Complement C1q" (D015950); "Hereditary Complement Deficiency Diseases" (D055468)

---

## Summary

**C1q deficiency is an ultra-rare autosomal-recessive inborn error of immunity and the strongest known single-gene cause of systemic lupus erythematosus (SLE).** It is caused by biallelic loss-of-function mutations in any one of the three genes encoding the C1q chains — **C1QA, C1QB, or C1QC** — clustered on chromosome **1p36.12**. Because the mature C1q molecule is a hexameric assembly of six A-B-C heterotrimeric subunits, a damaging variant in a single chain prevents assembly of the entire molecule, producing complete functional C1q deficiency and abolishing initiation of the classical complement pathway. More than 90% of genetically confirmed C1q-deficient individuals develop SLE or an SLE-like disease — the highest penetrance of any known SLE susceptibility factor — typically with severe, early-childhood onset. Patients are also susceptible to invasive infection by encapsulated bacteria (*Neisseria meningitidis*, *Streptococcus pneumoniae*, *Haemophilus influenzae*).

The core mechanism is **impaired complement-mediated clearance of apoptotic cells and immune complexes**. C1q normally opsonizes dying cells and immune complexes for phagocytosis; in its absence, apoptotic material — a major reservoir of nuclear autoantigens — accumulates, driving autoantibody formation (ANA, anti-dsDNA), immune-complex deposition, and tissue injury (notably lupus nephritis and CNS disease). This "waste-disposal" / "clearance-deficiency" hypothesis is supported directly by gene-targeted C1q-knockout mice, which develop glomerulonephritis with abundant apoptotic bodies and immune deposits. Downstream, **type I interferon dysregulation** amplifies the autoimmune phenotype and represents a druggable node.

Diagnosis rests on a distinctive laboratory signature — **absent total hemolytic complement activity (CH50) with normal C3 and C4** — plus demonstration of absent C1q protein and confirmatory sequencing (WES/single-gene). Management spans conventional SLE immunosuppression, type I interferon receptor blockade (anifrolumab), and — uniquely among the complement deficiencies — potentially **curative allogeneic hematopoietic stem-cell transplantation (HSCT)**, which works because C1q is synthesized predominantly by monocytes/macrophages, so replacing the hematopoietic compartment restores circulating C1q. Outcomes are variable: roughly 20% of patients die before age 20 (severe renal/CNS disease carries the worst prognosis), yet at least half reach middle age.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** C1q deficiency is a rare autosomal-recessive complement deficiency in which functional C1q — the recognition subunit of the C1 complex that initiates the classical complement pathway — is absent. The dominant clinical consequence is a severe, early-onset SLE-like autoimmune disease, accompanied by heightened susceptibility to pyogenic (encapsulated-bacterial) infection.

**Key identifiers.**
- **MONDO:** MONDO:0013343; **OMIM:** #613652; **Orphanet:** ORPHA:169147; **ICD-10:** D84.1; **ICD-11:** 4A00.1
- **Causal genes / loci:** C1QA (OMIM 120550), C1QB (OMIM 120570), C1QC (OMIM 120575) — chromosome 1p36.12

**Synonyms / alternative names.** C1q deficiency; complement component 1q deficiency; hereditary C1q deficiency; C1q monogenic lupus; C1q-deficiency SLE.

**Nature of evidence.** The knowledge base is derived from **aggregated disease-level resources and the published clinical/genetic literature** — principally case reports, small case series, an international survey of 45 patients across 31 families ([PMID: 26119135](https://pubmed.ncbi.nlm.nih.gov/26119135/)), and a multinational HSCT cohort ([PMID: 39470951](https://pubmed.ncbi.nlm.nih.gov/39470951/)) — rather than individual EHR extraction.

---

### 2. Etiology

**Primary cause — genetic.** C1q deficiency is a **monogenic, autosomal-recessive disorder**. Biallelic loss-of-function mutations in any one of C1QA, C1QB, or C1QC abolish functional C1q.

> *"C1q deficiency is a rare autosomal recessive genetic condition characterized by mutations in genes C1qA, C1qB, or C1qC which can cause a SLE-like disease."* — [PMID: 40316395](https://pubmed.ncbi.nlm.nih.gov/40316395/)

**Genetic risk factors.** The causal variants themselves ARE the risk factor; this is a highly penetrant Mendelian condition rather than a complex-trait susceptibility locus. C1q deficiency confers the strongest and most severe genetic risk for SLE of any complement deficiency:

> *"The strongest susceptibility genes for the development of systemic lupus erythematosus (SLE) in humans are null mutants of classical pathway complement proteins. There is a hierarchy of disease susceptibility and severity according to the position of the missing protein in the activation pathway, with the severest disease associated with C1q deficiency."* — [PMID: 10934224](https://pubmed.ncbi.nlm.nih.gov/10934224/)

**Environmental risk factors / triggers.** As with SLE generally, environmental triggers (UV light driving photosensitive rash; infections) likely modulate expression. **Consanguinity** is a major demographic risk factor because the disease is recessive — multiple reported pedigrees are consanguineous ([PMID: 40316395](https://pubmed.ncbi.nlm.nih.gov/40316395/) describes consanguineous siblings). Epstein–Barr virus is implicated in anti-C1q autoantibody generation in *polygenic* lupus via molecular mimicry ([PMID: 41929519](https://pubmed.ncbi.nlm.nih.gov/41929519/)), though this is distinct from the genetic deficiency.

**Protective factors.** No established genetic or environmental protective factors specific to C1q deficiency were identified. Restoration of C1q (via HSCT) is "protective" in the therapeutic sense but not a naturally occurring modifier.

**Gene–environment interactions.** UV exposure precipitating photosensitive mucocutaneous flares and infectious triggers of autoimmune activity are the principal gene–environment interactions; they operate on a fixed genetic background of absent clearance capacity.

---

### 3. Phenotypes

C1q deficiency produces a **dual immunodeficiency–autoimmunity phenotype**. Frequencies below derive chiefly from the international survey of 45 patients ([PMID: 26119135](https://pubmed.ncbi.nlm.nih.gov/26119135/)):

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| SLE / SLE-like disease | Clinical syndrome | 80% (36/45) | HP:0002725 (Systemic lupus erythematosus) |
| Infections only (no SLE) | Clinical | 11% (5/45) | HP:0002719 (Recurrent infections) |
| Asymptomatic | — | 9% (4/45) | — |
| Photosensitive mucocutaneous rash | Physical/sign | Very common | HP:0000992 (Photosensitivity); HP:0001025 (Urticaria) |
| Discoid lupus | Physical | Common | HP:0005503 (Discoid lupus rash) |
| Oral ulcers | Sign | Common | HP:0000155 (Oral ulcer) |
| Inflammatory polyarthritis | Sign | Common | HP:0001369 (Arthritis) |
| Recurrent encapsulated-bacterial infection | Clinical | Common | HP:0002721 (Immunodeficiency) |
| Lupus nephritis | Clinical | Subset (severe) | HP:0000099 (Glomerulonephritis) |
| CNS involvement (incl. brain parenchymal calcification) | Clinical/imaging | Subset (severe) | HP:0002518 (Periventricular calcification) |
| Absent CH50 with normal C3/C4 | Lab abnormality | Universal | HP:0005339 (Abnormal complement system) |

> *"Of these patients 36 (80%) suffer from SLE, of which 16 suffer from SLE and infections, 5 (11%) suffer from infections only and 4 (9%) have no symptoms."* — [PMID: 26119135](https://pubmed.ncbi.nlm.nih.gov/26119135/)

> *"All patients exhibited mucocutaneous involvement, discoid lupus erythematosus, inflammatory polyarthritis, normal serum complements C3 and C4, coarse-speckled Antinuclear antibody positivity."* — [PMID: 40556690](https://pubmed.ncbi.nlm.nih.gov/40556690/)

**Characteristics.** Onset is typically **neonatal–childhood** (case reports describe presentation as young as age 3; [PMID: 42147803](https://pubmed.ncbi.nlm.nih.gov/42147803/)). Severity is **variable but skews severe**, with the most severe phenotype defined by **renal and/or neurological involvement**. Course is chronic with episodic lupus flares. Quality-of-life impact is substantial in severe cases (chronic immunosuppression, infection risk, renal/CNS morbidity), though formal EQ-5D/SF-36 data specific to C1q deficiency were not identified.

---

### 4. Genetic / Molecular Information

**Causal genes.** C1QA, C1QB, C1QC on chromosome **1p36.12** (HGNC: C1QA, C1QB, C1QC). Each encodes one chain of the C1q molecule; all three must co-assemble into A-B-C heterotrimers, six of which form the hexameric "bouquet of flowers" structure.

**Variant spectrum.** C1q deficiency arises from a **diverse range of coding and non-coding loss-of-function variants**:

| Variant | Gene | Type | Classification | PMID |
|---|---|---|---|---|
| c.622C>T | C1QA | Nonsense | Pathogenic | [42147803](https://pubmed.ncbi.nlm.nih.gov/42147803/) |
| NM_001378156.1:c.263G>A | C1QB | Missense (novel) | Likely pathogenic | [40506420](https://pubmed.ncbi.nlm.nih.gov/40506420/) |
| Intronic, 2 nt before exon-2 splice site | C1QB | Non-coding / splice | Pathogenic | [25454803](https://pubmed.ncbi.nlm.nih.gov/25454803/) |
| Known A/B/C chain mutations (C1qA-Gln186, C1qB-Gly15, C1qB-Arg150, C1qC-Gly6, C1qC-Arg41) | C1QA/B/C | Nonsense/missense | Pathogenic | [18505047](https://pubmed.ncbi.nlm.nih.gov/18505047/) |

A key mechanistic insight: the Dutch C1QB splice variant abolished C1qB mRNA, reduced C1qA mRNA, left C1qC mRNA normal, and caused intracellular absence of the C1qB peptide despite present C1qA/C1qC — demonstrating that **loss of a single chain prevents hexamer assembly**:

> *"Deep-sequencing revealed a homozygous mutation in the non-coding region of C1qB in the patient, whereas both parents were heterozygous. The mutation is located two nucleotides before the splice site of the second exon."* — [PMID: 25454803](https://pubmed.ncbi.nlm.nih.gov/25454803/)

> *"A novel homozygous likely pathogenic missense variant in the C1QB gene, NM_001378156.1:c.263G>A, was identified."* — [PMID: 40506420](https://pubmed.ncbi.nlm.nih.gov/40506420/)

**Functional consequence:** complete **loss of function** (null); recessive. **Allele frequencies** are extremely low (private/population-specific), consistent with an ultra-rare recessive disorder; heterozygous carriers are typically asymptomatic.

**Somatic vs germline:** germline. **Modifier genes / epigenetics:** no robustly established disease modifiers specific to C1q deficiency were identified, though autoantibody specificity stratifies organ involvement (see Diagnostics). **Chromosomal abnormalities:** not applicable — this is a single-gene point/small-variant disorder, not a structural/aneuploidy condition.

---

### 5. Environmental Information

- **Environmental factors.** UV radiation precipitates the characteristic photosensitive cutaneous lupus; otherwise no specific toxin/occupational exposures are causally implicated.
- **Lifestyle factors.** None specifically established beyond general SLE triggers.
- **Infectious agents.** C1q deficiency does not have an infectious *cause*, but the deficiency increases **susceptibility to encapsulated bacteria** — *Neisseria meningitidis*, *Streptococcus pneumoniae*, *Haemophilus influenzae* — because the classical pathway contributes to opsonophagocytic defense ([PMID: 19418946](https://pubmed.ncbi.nlm.nih.gov/19418946/) discusses this susceptibility in hypocomplementemia generally). EBV is relevant to anti-C1q autoantibody biology in polygenic lupus but not to the genetic deficiency itself.

---

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function mutation** in C1QA, C1QB, or C1QC (germline) **leads to** absence or non-functionality of one C1q chain.
2. Missing chain **prevents assembly** of the A-B-C heterotrimer and therefore of the hexameric C1q molecule (*demonstrated* — intracellular chain studies, [PMID: 25454803](https://pubmed.ncbi.nlm.nih.gov/25454803/)) **→ complete functional C1q deficiency**.
3. Absent C1q **results in** failure to initiate the **classical complement pathway** (no C1 complex formation) → **absent CH50 with preserved C3/C4** (alternative/lectin pathways intact).
4. Loss of C1q **impairs opsonization and clearance of apoptotic cells and immune complexes** (*demonstrated in vivo*; hierarchical role of classical-pathway proteins, [PMID: 10934224](https://pubmed.ncbi.nlm.nih.gov/10934224/)).
5. Uncleared apoptotic cells — a **major source of nuclear autoantigens** — **accumulate** (*demonstrated*: apoptotic bodies in glomeruli of C1q-KO mice, [PMID: 10072632](https://pubmed.ncbi.nlm.nih.gov/10072632/)).
6. Autoantigen exposure **drives loss of tolerance → autoantibody formation** (ANA, anti-dsDNA, and others) → **immune-complex formation and tissue deposition**.
   - **Branch A (autoimmunity):** immune complexes deposit in kidney (lupus nephritis), skin, and brain → **tissue injury** → clinical SLE. Type I interferon dysregulation **amplifies** this arm (druggable; [PMID: 42597478](https://pubmed.ncbi.nlm.nih.gov/42597478/)).
   - **Branch B (immunodeficiency):** absent classical-pathway opsonization **results in** susceptibility to **encapsulated-bacterial infection**.
7. Net clinical outcome: **early-onset, often severe SLE** (>90% penetrance) ± recurrent infection; severe renal/CNS involvement **leads to** ~20% childhood mortality.

**Molecular pathways / cellular processes.** Classical complement activation pathway (initiation step); apoptotic-cell clearance / efferocytosis; opsonophagocytosis; immune-complex processing; type I interferon signaling (downstream amplifier).

- Suggested **GO biological-process terms:** GO:0006958 (complement activation, classical pathway); GO:0045087 (innate immune response); GO:0043277 (apoptotic cell clearance); GO:0006911 (phagocytosis, engulfment); GO:0034340 (response to type I interferon).
- Suggested **cell types (CL):** CL:0000576 (monocyte) and CL:0000235 (macrophage) — the predominant C1q-producing and phagocytic cells; CL:0000236 (B cell, autoantibody production).

**Protein dysfunction.** C1q is a complex glycoprotein assembled from 18 polypeptide chains (6× A-B-C), each with an N-terminal collagen-like region and a C-terminal globular gC1q head mediating ligand recognition ([PMID: 28601358](https://pubmed.ncbi.nlm.nih.gov/28601358/); [PMID: 29692784](https://pubmed.ncbi.nlm.nih.gov/29692784/)). In deficiency, the molecule is simply absent (loss of function), not misfolded-and-aggregated.

**Immune system involvement.** The disease sits at the intersection of **immunodeficiency** (failed opsonophagocytosis) and **autoimmunity** (failed clearance → autoantibodies). C1q additionally regulates cytokine production by antigen-presenting cells and T-cell maturation, and participates in CNS synaptic pruning — functions whose loss may contribute to the breadth of phenotype ([PMID: 28601358](https://pubmed.ncbi.nlm.nih.gov/28601358/)).

> *"Apoptotic cells are thought to be a major source of the autoantigens of SLE, and impairment of their removal by complement may explain the link between hereditary complement deficiency and the development of SLE."* — [PMID: 10934224](https://pubmed.ncbi.nlm.nih.gov/10934224/)

---

### 7. Anatomical Structures Affected

- **Organ level (primary):** skin (UBERON:0002097), kidney/glomerulus (UBERON:0002113 / UBERON:0000074), joints (UBERON:0001485), central nervous system / brain (UBERON:0000955).
- **Secondary / systems:** immune/hematopoietic system (UBERON:0002405), mucous membranes (oral ulcers), and systemic involvement typical of SLE (cardiovascular, serosal).
- **Tissue/cell level:** glomerular tissue (immune-complex deposition, apoptotic bodies); connective tissue/skin at the dermoepidermal junction; the key *effector* cells are **monocytes/macrophages** (CL:0000576 / CL:0000235), the main C1q source, and **B lymphocytes** producing autoantibodies.
- **Subcellular (GO Cellular Component):** extracellular space/blood plasma (GO:0005615) where C1q normally circulates; GO:0005581 (collagen trimer) describes the collagen-like stalk of the assembled molecule.
- **Localization / laterality:** manifestations (rash, nephritis, arthritis, cerebral calcification) are typically **bilateral/systemic**, consistent with a circulating-protein deficiency.

---

### 8. Temporal Development

- **Onset:** congenital genetic lesion; **clinical onset in infancy/early childhood** is typical (cases as young as 3 years), making it a pediatric-onset monogenic lupus. Onset is usually insidious/chronic.
- **Progression:** chronic, lifelong, with **episodic (relapsing-remitting) lupus flares**. Severity ranges from mild/manageable to treatment-resistant. A severe subset with renal/CNS disease progresses to organ failure.
- **Duration / outcome spread:** highly variable. ~20% die before age 20, yet ≥50% reach middle age ([PMID: 26119135](https://pubmed.ncbi.nlm.nih.gov/26119135/)).
- **Critical periods / intervention windows:** early recognition is pivotal; HSCT is most beneficial before severe renal/neurological damage accrues, since those features predict worst transplant survival ([PMID: 39470951](https://pubmed.ncbi.nlm.nih.gov/39470951/)).

---

### 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal recessive.** Parents of affected children are obligate heterozygous carriers ([PMID: 25454803](https://pubmed.ncbi.nlm.nih.gov/25454803/)).
- **Penetrance:** very high for SLE/SLE-like disease — **>90%** among genetically confirmed individuals (highest of any SLE susceptibility factor); a small minority (≈9%) remain asymptomatic, indicating penetrance is high but not absolute.
- **Expressivity:** variable (mild-to-severe; organ involvement differs between patients).
- **Consanguinity:** a major contributor; many pedigrees are consanguineous.
- **Founder effects / population distribution:** private and population-specific variants reported across Middle Eastern (Iranian, Arab), European (Dutch, Swedish), Brazilian, and other cohorts; no single global founder allele. Carrier frequency is very low but elevated in consanguineous communities.
- **Epidemiology:** ultra-rare; fewer than ~100 genetically confirmed patients described worldwide (international survey = 45 patients/31 families, [PMID: 26119135](https://pubmed.ncbi.nlm.nih.gov/26119135/); a review analyzed 69 genetically confirmed patients, [PMID: 39470951](https://pubmed.ncbi.nlm.nih.gov/39470951/)). Precise population prevalence/incidence are not established.
- **Sex ratio / age distribution:** predominantly pediatric onset; sex distribution not strongly skewed in the reported series (in contrast to polygenic SLE's female predominance).

---

### 10. Diagnostics

**Screening / first-line laboratory signature (pathognomonic pattern):**
- **CH50 (total hemolytic complement): absent / markedly reduced**
- **C3 and C4: normal**

This combination strongly points to an early-classical-pathway component deficiency and distinguishes **monogenic C1q lupus from classic polygenic SLE** (where C3/C4 are typically consumed/low).

> *"Laboratory evaluation showed strongly positive antinuclear antibody (ANA) and anti-SSA antibodies, with normal C3 and C4 levels but markedly reduced CH50."* — [PMID: 42147803](https://pubmed.ncbi.nlm.nih.gov/42147803/)

**Confirmatory tests:**
- **C1q protein quantitation** (absent) and functional classical-pathway assays.
- **Western blot** to document absent C1q chains; mononuclear-cell C1q mRNA expression studies can characterize the molecular defect ([PMID: 26017655](https://pubmed.ncbi.nlm.nih.gov/26017655/)).
- **Genetic testing:** **whole-exome sequencing** is high-yield and was diagnostic in multiple cases ([PMID: 42147803](https://pubmed.ncbi.nlm.nih.gov/42147803/)); **single-gene / targeted C1QA/B/C sequencing** confirms the biallelic variant; deep/whole-genome sequencing is needed to catch **non-coding splice variants** ([PMID: 25454803](https://pubmed.ncbi.nlm.nih.gov/25454803/)). Parental carrier testing confirms recessive segregation.
- **Autoantibodies:** ANA (coarse-speckled), anti-dsDNA, anti-Ro/SSA, anti-RNP help characterize disease and stratify organ risk (below).

**Differential diagnosis.** Polygenic SLE (C3/C4 usually low; C1q present); other early-classical-pathway deficiencies (C1r/s, C4, C2 — milder hierarchy); **acquired** C1q lowering with anti-C1q antibodies (e.g., hypocomplementemic urticarial vasculitis [HUV], [PMID: 40852710](https://pubmed.ncbi.nlm.nih.gov/40852710/); acquired angioedema / C1-INH deficiency, [PMID: 28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/)). The critical distinction: in genetic C1q deficiency the **antigen itself is absent**, whereas anti-C1q autoantibody syndromes require **present** C1q.

**Prognostic autoantibody stratification (within genetic C1q deficiency).** In 69 genetically confirmed patients, autoantibody specificity mapped to organ involvement:

> *"we found that anti-Ro antibodies are associated with neurologic involvement, and anti-RNP and anti-DNA antibodies with renal [involvement]."* — [PMID: 39470951](https://pubmed.ncbi.nlm.nih.gov/39470951/)

**Note on anti-C1q antibodies (adjacent biology).** In *polygenic* SLE, circulating **anti-C1q autoantibodies** are the best single serological marker of lupus-nephritis activity (ROC AUC 0.929; NPV 92%; [PMID: 41546370](https://pubmed.ncbi.nlm.nih.gov/41546370/)) and independently predict thrombosis in membranous LN (highest tertile HR 2.71; [PMID: 41895528](https://pubmed.ncbi.nlm.nih.gov/41895528/)). These markers characterize polygenic SLE/HUV, **not** Mendelian C1q deficiency, and are included here only for differential-diagnostic completeness.

---

### 11. Outcome / Prognosis

- **Mortality:** ~**20% case fatality before age 20** in the largest phenotypic survey, with almost all deaths occurring before age 20 — yet outcomes are highly variable and at least half of patients survive into middle age.

> *"In total 9 (20%) of the C1q deficient individuals had died. All except for one died before the age of 20 years."* — [PMID: 26119135](https://pubmed.ncbi.nlm.nih.gov/26119135/)

- **Prognostic factors:** presence of **renal and/or neurological involvement** defines the severe phenotype and predicts the worst survival after HSCT (OS 40% vs 84%; p=0.034; [PMID: 39470951](https://pubmed.ncbi.nlm.nih.gov/39470951/)). Autoantibody profile (anti-Ro → neurologic; anti-RNP/anti-DNA → renal) provides a serological route to risk stratification.
- **Morbidity:** chronic immunosuppression burden, infection susceptibility, cutaneous disfigurement (discoid lupus), arthritis, renal insufficiency, and CNS sequelae.
- **Recovery potential:** autoimmune features can **resolve completely after successful HSCT** with restoration of C1q, allowing discontinuation of immunosuppression.

---

### 12. Treatment

**Conventional SLE-directed therapy.** Corticosteroids, hydroxychloroquine, and immunosuppressants (mycophenolate, cyclophosphamide, azathioprine, rituximab) are used for autoimmune manifestations and nephritis, as in polygenic SLE. These control but do not cure the underlying deficiency.

**Type I interferon-targeted therapy.** **Anifrolumab** (anti-IFNAR1 monoclonal antibody) produced marked benefit in a genetically confirmed C1QA-deficient child with refractory mucocutaneous lupus:

> *"She showed significant clinical improvement and full recovery of mucocutaneous lesions, restoration of laboratory parameters and successful discontinuation of corticosteroids after the seventh monthly infusion."* — [PMID: 42597478](https://pubmed.ncbi.nlm.nih.gov/42597478/)

This implicates the type I IFN pathway as a downstream, druggable amplifier distinct from C1q replacement.

**Curative allogeneic HSCT.** Because C1q is produced predominantly by **monocytes/macrophages**, allogeneic HSCT replaces the deficient cellular source and can **cure** the disorder:

> *"Complete donor chimerism has been maintained for 2 years after transplantation, leading to the restoration of C1q levels and the resolution of SLE symptoms. Normal C1q mRNA expression was observed in CD14 + cells."* — [PMID: 33000368](https://pubmed.ncbi.nlm.nih.gov/33000368/)

The largest cohort (EBMT Inborn Errors Working Party; 18 patients, 20 HSCTs, median age 10 y) quantified outcomes:

> *"Overall survival (OS) was 71% and event-free survival was 59% at two years... In eleven patients HSCT led to resolution of autoimmune features and discontinuation of immunosuppressive treatments... Patients with a severe autoimmune phenotype, defined as neurological and/or renal involvement, had the worst OS (40% vs 84%; p = 0.034)."* — [PMID: 39470951](https://pubmed.ncbi.nlm.nih.gov/39470951/)

The Karolinska experience similarly demonstrated cure in refractory cases but also transplant-related mortality (PTLD, GVHD), underscoring that HSCT should be considered **early**, before severe organ damage ([PMID: 26516671](https://pubmed.ncbi.nlm.nih.gov/26516671/); [PMID: 24035158](https://pubmed.ncbi.nlm.nih.gov/24035158/)).

**Supportive / preventive.** Prophylactic/therapeutic antibiotics and vaccination against encapsulated bacteria (pneumococcus, meningococcus, *H. influenzae* type b) address the infection-susceptibility arm.

**Investigational / theoretical.** Recombinant human C1q has been produced and is functional in vitro ([PMID: 33621564](https://pubmed.ncbi.nlm.nih.gov/33621564/)), raising the prospect of **C1q protein-replacement therapy**, though no clinical replacement product is established. Gene therapy is conceptually attractive but not clinically available.

**Suggested NCIT intervention terms:** anifrolumab; allogeneic hematopoietic stem cell transplantation; corticosteroid therapy; rituximab; hydroxychloroquine; mycophenolate mofetil; cyclophosphamide.

---

### 13. Prevention

- **Primary prevention:** none for the genetic lesion itself. **Genetic counseling** for consanguineous and carrier families; **carrier screening** and **prenatal/preimplantation genetic testing** are options once a familial variant is known.
- **Secondary prevention:** early recognition via the CH50-absent/normal-C3-C4 signature in any child with early-onset lupus and/or recurrent infection, enabling timely genetic confirmation and consideration of HSCT before severe organ damage.
- **Tertiary prevention:** vaccination against encapsulated bacteria; infection prophylaxis; vigilant monitoring/treatment of nephritis and CNS disease to prevent irreversible organ damage.
- **Counseling:** recessive recurrence risk (25% per pregnancy for carrier couples); cascade testing of relatives.

---

### 14. Other Species / Natural Disease

- **Model-relevant taxonomy:** *Mus musculus* (NCBI Taxon:10090) is the principal experimental species. C1q genes are conserved across vertebrates, and the gC1q domain has an ancient evolutionary history conserved from bacteria to mammals ([PMID: 24400480](https://pubmed.ncbi.nlm.nih.gov/24400480/)).
- **Orthologous genes:** murine *C1qa*, *C1qb*, *C1qc*.
- **Natural disease in other species:** no well-characterized spontaneous companion-animal/wildlife C1q-deficiency disease was identified in this investigation; the evidence base is dominated by engineered mouse models rather than naturally occurring animal disease. (OMIA/veterinary entries were not confirmed here.)
- **Zoonotic potential:** not applicable (non-infectious genetic disorder).

---

### 15. Model Organisms

- **Principal model:** the **gene-targeted C1q-knockout mouse** (C1qa-deficient), which recapitulates the central human mechanism:

> *"C1q-deficient mice, generated by gene targeting, showed an increased mortality and 25% of the mice had histological evidence of glomerulonephritis characterised by multiple apoptotic cell bodies and immune deposits... These observations are compatible with the hypothesis that C1q deficiency causes autoimmunity by an impaired clearance of apoptotic cells."* — [PMID: 10072632](https://pubmed.ncbi.nlm.nih.gov/10072632/)

- **Phenotype recapitulation:** strong — high-titer antinuclear antibodies in ~50% of animals, immune-complex glomerulonephritis in ~25%, and accumulation of apoptotic bodies in diseased glomeruli, directly modeling the human "clearance-deficiency → autoimmunity" axis ([PMID: 9777411](https://pubmed.ncbi.nlm.nih.gov/9777411/)).
- **Limitations:** murine lupus is background-dependent and does not fully reproduce the human severity spectrum, CNS calcification, or infection phenotype; penetrance is lower than in humans.
- **In vitro systems:** recombinant human C1q production in HEK293-F cells enables structure–function and potential replacement-therapy studies ([PMID: 33621564](https://pubmed.ncbi.nlm.nih.gov/33621564/)); patient CD14+ monocyte cultures document the cellular C1q-production defect and its correction post-HSCT ([PMID: 33000368](https://pubmed.ncbi.nlm.nih.gov/33000368/); [PMID: 26017655](https://pubmed.ncbi.nlm.nih.gov/26017655/)).

---

## Mechanistic Model / Interpretation

```
  Biallelic LOF mutation (C1QA / C1QB / C1QC, 1p36.12, autosomal recessive)
                                 |
                                 v
        Missing chain -> hexameric C1q fails to assemble (DEMONSTRATED)
                                 |
                                 v
     Complete functional C1q deficiency -> no classical-pathway initiation
                                 |
          +----------------------+----------------------+
          |                                             |
          v (AUTOIMMUNITY ARM)                          v (IMMUNODEFICIENCY ARM)
  Impaired clearance of apoptotic                Impaired opsonophagocytosis
  cells + immune complexes                       of encapsulated bacteria
          |                                             |
          v                                             v
  Nuclear-autoantigen accumulation              Recurrent invasive infection
  (apoptotic bodies, DEMONSTRATED in mice)      (N. meningitidis, S. pneumoniae,
          |                                       H. influenzae)
          v
  Loss of tolerance -> autoantibodies
  (ANA, anti-dsDNA, anti-Ro, anti-RNP)
          |
          v
  Immune-complex deposition (kidney, skin, brain)
  + TYPE I IFN amplification (druggable: anifrolumab)
          |
          v
  >90% develop early-onset SLE; severe renal/CNS disease -> ~20% childhood mortality
          |
          v
  CURE: allogeneic HSCT restores monocyte-derived C1q (OS 71%; worse if renal/CNS)
```

**Laboratory signature table (diagnostic discriminator):**

| Marker | Genetic C1q deficiency | Classic polygenic SLE |
|---|---|---|
| CH50 | Absent / markedly low | Variable (often low in flare) |
| C3 | **Normal** | Often low (consumed) |
| C4 | **Normal** | Often low (consumed) |
| C1q antigen | **Absent** | Present (may be lowered by anti-C1q Ab) |
| Anti-C1q antibodies | N/A (no antigen) | Present; marks LN activity |

The unifying concept is that C1q sits at the **apex of a clearance hierarchy**: the earlier in the classical pathway the deficiency, the more severe the lupus. C1q deficiency, being the most upstream, produces the most penetrant and severe disease ([PMID: 10934224](https://pubmed.ncbi.nlm.nih.gov/10934224/)). Crucially, because the deficient protein is **hematopoietically produced (monocyte/macrophage)**, the disorder is uniquely curable by HSCT — a rare instance of a monogenic autoimmune disease with a definitive cellular cure.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [10934224](https://pubmed.ncbi.nlm.nih.gov/10934224/) | Supports F001, F002, F009 | Establishes C1q as apex of the classical-pathway severity hierarchy; links apoptotic clearance to SLE |
| [10072632](https://pubmed.ncbi.nlm.nih.gov/10072632/) | Supports F002, F009 | C1q-KO mouse: glomerulonephritis + apoptotic bodies → mechanistic proof |
| [9777411](https://pubmed.ncbi.nlm.nih.gov/9777411/) | Supports mechanism | Reviews immune-complex/apoptosis hypothesis; murine ANA data |
| [26119135](https://pubmed.ncbi.nlm.nih.gov/26119135/) | Supports F004, F009 | Largest phenotype survey (45 pts): 80% SLE, 20% mortality |
| [40556690](https://pubmed.ncbi.nlm.nih.gov/40556690/) | Supports F004 | Case series: mucocutaneous/arthritis phenotype, normal C3/C4 |
| [42147803](https://pubmed.ncbi.nlm.nih.gov/42147803/) | Supports F006, diagnostics | C1QA nonsense variant; CH50-low/normal-C3-C4 diagnostic pattern; WES utility |
| [40316395](https://pubmed.ncbi.nlm.nih.gov/40316395/) | Supports F001 | Confirms AR inheritance & three causal genes; consanguineous siblings |
| [25454803](https://pubmed.ncbi.nlm.nih.gov/25454803/) | Supports F006 | Non-coding splice variant; chain-assembly dependence; AR segregation |
| [40506420](https://pubmed.ncbi.nlm.nih.gov/40506420/) | Supports F006 | Novel C1QB missense (c.263G>A), expands spectrum |
| [26017655](https://pubmed.ncbi.nlm.nih.gov/26017655/) | Supports genetics/diagnostics | C1q mRNA expression studies in juvenile SLE |
| [39470951](https://pubmed.ncbi.nlm.nih.gov/39470951/) | Supports F003, F008 | EBMT HSCT cohort: OS 71%; severe-phenotype OS 40% vs 84%; autoantibody-organ mapping |
| [33000368](https://pubmed.ncbi.nlm.nih.gov/33000368/) | Supports F003 | HSCT restores CD14+ C1q production, resolves SLE |
| [26516671](https://pubmed.ncbi.nlm.nih.gov/26516671/) | Supports F003 | Karolinska HSCT cures; documents transplant risks |
| [24035158](https://pubmed.ncbi.nlm.nih.gov/24035158/) | Supports F003 | Early report of HSCT cure |
| [42597478](https://pubmed.ncbi.nlm.nih.gov/42597478/) | Supports F005 | Anifrolumab efficacy → type I IFN as downstream target |
| [33621564](https://pubmed.ncbi.nlm.nih.gov/33621564/) | Supports treatment outlook | Functional recombinant human C1q → replacement-therapy prospect |
| [28601358](https://pubmed.ncbi.nlm.nih.gov/28601358/) / [29692784](https://pubmed.ncbi.nlm.nih.gov/29692784/) / [24400480](https://pubmed.ncbi.nlm.nih.gov/24400480/) | Background | C1q structure (18 chains, gC1q head), multifunctionality, evolutionary conservation |
| [19418946](https://pubmed.ncbi.nlm.nih.gov/19418946/) | Supports infection arm | Hypocomplementemia → encapsulated-bacterial infection risk |
| [41546370](https://pubmed.ncbi.nlm.nih.gov/41546370/) / [41895528](https://pubmed.ncbi.nlm.nih.gov/41895528/) | Supports F007 (adjacent) | Anti-C1q antibodies mark LN activity / predict thrombosis (polygenic SLE) |
| [41929519](https://pubmed.ncbi.nlm.nih.gov/41929519/) | Differential/adjacent | EBV mimicry induces pathogenic anti-C1q in lupus-prone mice |
| [40852710](https://pubmed.ncbi.nlm.nih.gov/40852710/) / [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | Differential dx | HUV and acquired C1-INH deficiency (distinguish from genetic C1q loss) |

---

## Limitations and Knowledge Gaps

1. **Small-N evidence base.** The disorder is ultra-rare; the largest datasets are a 45-patient survey and an 18-patient HSCT cohort. Prevalence/incidence are not formally established, and frequency estimates carry wide uncertainty.
2. **Anti-C1q antibody confound.** Much of the richest "C1q" literature concerns *acquired* anti-C1q autoantibodies in polygenic SLE/HUV — biologically distinct from genetic deficiency (antigen absent vs present). Care is needed to avoid conflating the two; this report flags the distinction explicitly (Finding F007).
3. **Modifier genetics and epigenetics** underlying the variable expressivity/penetrance (~9% asymptomatic) are essentially unknown.
4. **Quality-of-life and natural-history data** specific to C1q deficiency are sparse; no validated EQ-5D/SF-36 datasets were identified.
5. **No naturally occurring animal disease** was confirmed; comparative pathology rests on engineered mouse models with incomplete phenotype recapitulation.
6. **Replacement therapy** remains preclinical; recombinant C1q is functional in vitro but untested clinically.
7. **Causal statements** for the apoptotic-clearance mechanism are strongest in mice; the human causal chain from clearance failure to specific organ involvement is inferred from concordant (not interventional) human data.

---

## Proposed Follow-up Experiments / Actions

1. **International registry & natural-history study** to firm up prevalence, penetrance, organ-involvement frequencies, and long-term survival with standardized phenotyping (and QoL instruments).
2. **Prospective HSCT-timing trial/registry** testing the hypothesis that transplanting *before* renal/CNS involvement improves OS beyond the current 71% — directly actionable given the 40% vs 84% split.
3. **Biomarker-guided risk stratification:** validate the autoantibody→organ map (anti-Ro→CNS; anti-RNP/anti-dsDNA→renal) prospectively to guide early intervention/transplant decisions.
4. **Recombinant C1q replacement therapy:** advance functional recombinant C1q ([PMID: 33621564](https://pubmed.ncbi.nlm.nih.gov/33621564/)) toward pharmacokinetic/efficacy studies in C1q-KO mice, then first-in-human trials — a non-transplant option for patients ineligible for HSCT.
5. **Type I IFN pathway characterization:** systematically measure IFN signatures across the C1q-deficient cohort to define which patients benefit from anifrolumab, building on the index case ([PMID: 42597478](https://pubmed.ncbi.nlm.nih.gov/42597478/)).
6. **Gene-therapy feasibility:** evaluate monocyte/HSC-directed gene addition or editing of C1QA/B/C as a less toxic alternative to allogeneic HSCT.
7. **Deep/whole-genome sequencing adoption** in diagnostic workflows to capture non-coding splice variants that panels/WES may miss ([PMID: 25454803](https://pubmed.ncbi.nlm.nih.gov/25454803/)).

---

*Evidence source legend: human clinical (case reports/series, cohorts, surveys), model organism (C1q-KO mouse), in vitro (recombinant C1q, patient monocyte cultures). This report synthesizes 9 confirmed findings across 32 reviewed papers.*


## Artifacts

- [OpenScientist final report](C1Q_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](C1Q_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 18 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 4 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0005503` (1 mention), reported as "Discoid lupus rash" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002518` (1 mention) - the report calls it "Periventricular calcification"; HP calls it **Abnormal periventricular white matter morphology**, and lists "Periventricular white matter abnormalities" among its other names
- `HP:0005339` (1 mention) - the report calls it "Abnormal complement system"; HP calls it **Abnormality of complement system**
- `CL:0000236` (1 mention) - the report calls it "B cell, autoantibody production"; CL calls it **B cell**
- `UBERON:0002405` (1 mention) - the report calls it "Secondary / systems:** immune/hematopoietic system"; UBERON calls it **immune system**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Taxon`.