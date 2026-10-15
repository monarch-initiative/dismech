---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T17:05:10.323066'
end_time: '2026-09-07T17:28:35.805162'
duration_seconds: 1405.48
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Erb Palsy
  mondo_id: MONDO:0700303
  category: Acquired
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
citation_count: 39
reference_validation:
  total_references: 40
  verified: 40
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 9
  relevance_assessed: 40
  on_topic: 31
  validator_version: 0.2.1
term_validation:
  total_terms: 22
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 8
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0001319
    reported_labels:
    - approximate
    ontology_label: Neonatal hypotonia
  - term_id: HP:0031843
    reported_labels:
    - Shoulder contracture, approximate
    ontology_label: Abnormally slow thought process
  - term_id: CL:0000138
    reported_labels:
    - chondrocyte, for glenoid remodeling
    ontology_label: chondrocyte
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Erb_Palsy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Erb_Palsy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Erb Palsy
- **MONDO ID:** MONDO:0700303 (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Erb Palsy** covering all of the
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

# Erb Palsy — Comprehensive Disease Characterization Report

**Disease:** Erb Palsy (Erb–Duchenne Palsy)
**MONDO ID:** MONDO:0700303 · **ICD-10:** P14.0 · **Category:** Acquired (non-genetic birth injury)

---

## Summary

**Erb palsy is an acquired, non-genetic mechanical traction/stretch injury of the upper brachial plexus (nerve roots C5–C6, sometimes extending to C7) sustained during birth.** It is the single most common subtype of obstetric brachial plexus injury (OBPI), accounting for roughly two-thirds of all cases (66.6% in a German national cohort). Reported incidence ranges from ~0.15–1.5 per 1000 live births using administrative data, rising to ~14.5 per 1000 under active prospective surveillance, reflecting that many mild neuropraxic injuries at birth go under-recorded. The strongest single risk factor is **shoulder dystocia** (adjusted odds ratio ~57), with fetal macrosomia, maternal diabetes, and maternal obesity as major contributors; **cesarean delivery is protective**, most strongly in macrosomic infants.

Clinically the newborn presents with a flaccid, adducted, internally rotated arm with an extended, pronated forearm — the classic "waiter's-tip" posture. Diagnosis is clinical (Narakas classification), supported by MRI (modest sensitivity ~68% for root avulsion) and electrophysiology. The natural history is favorable: **80–95% of infants recover spontaneously**, with recovery of biceps (elbow flexion) function by ~3 months being the pivotal prognostic milestone. In the ~5–20% with persistent injury, denervation of the shoulder muscles (particularly the subscapularis) plus muscle imbalance drives a **shoulder internal-rotation contracture** and secondary **glenohumeral dysplasia** (seen in ~49% of permanent cases), the chief long-term morbidity.

Management follows a **staged, time-sensitive ladder**: physiotherapy/occupational therapy first-line to maintain range of motion; botulinum toxin A to counter early contracture; microsurgical nerve reconstruction (nerve grafting after neuroma excision) or distal nerve transfers when biceps recovery is absent by ~3–6 months; and secondary orthopedic procedures (soft-tissue releases, tendon transfers, humeral derotation osteotomy, radioulnar synostosis) for residual deformity. Prevention is fundamentally obstetric: multi-professional shoulder-dystocia simulation training and maternal glycemic control measurably reduce brachial plexus injury at birth, though 50–70% of shoulder dystocia occurs without identifiable risk factors, limiting predictive prevention. Because Erb palsy is a mechanical acquired injury, there is **no causal gene, no OMIM Mendelian entry, no ClinVar variant, and no heritable transmission** — sections of this template addressing genetics, epigenetics, and inheritance are largely **not applicable**, and this is documented explicitly below.

---

## Key Findings

### Finding 1 — Erb palsy is the most common OBPI subtype; incidence ~0.9–1.5 per 1000 live births

Erb palsy is the dominant clinical presentation among obstetric brachial plexus injuries. In a German national cohort (2005–2018; n = 2,069 infants hospitalized with OBPI in the first year of life), Erb palsy (ICD-10 **P14.0**) was the most frequent subtype at **66.60%**, and overall OBPI incidence declined by 47.57%, from 0.28 per 1000 births in 2005 to 0.15 in 2018 (p < 0.001) — a trend attributed to improved obstetric practice and rising cesarean rates ([PMID: 40315612](https://pubmed.ncbi.nlm.nih.gov/40315612/)). The US Kids' Inpatient Database found brachial plexus birth injury (BPBI) rates steady at ~0.9–1.1 per 1000 live births between 2006 and 2019 ([PMID: 39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/)). A 2021–2024 prospective surveillance study using real-time reporting found a substantially higher incidence of **14.5 per 1000 live births** at birth, dropping to **3.6 per 1000** for injuries persisting beyond 2 months — demonstrating that administrative datasets undercount mild, transient neuropraxias ([PMID: 41616322](https://pubmed.ncbi.nlm.nih.gov/41616322/)).

> "Erb palsy was the most frequent OBPI subtype (66.60%)." — [PMID: 40315612](https://pubmed.ncbi.nlm.nih.gov/40315612/)

### Finding 2 — Shoulder dystocia is the strongest risk factor; cesarean delivery is protective

The mechanical origin of Erb palsy is reflected in its risk-factor profile. In a US Kids' Inpatient Database logistic-regression analysis, **shoulder dystocia was the strongest predictor** of BPBI (adjusted OR **56.9**, p < 0.001), and cesarean delivery was protective across all newborn weight classes, with the greatest protection in macrosomic infants (macrosomic + C-section AOR 0.581, 95% CI 0.365–0.925) ([PMID: 39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/)). A prospective shoulder-dystocia cohort found that neonatal BPI at 48 hours was associated with maternal BMI > 30 kg/m² (OR 7.91, 95% CI 1.3–47.7), shoulder dystocia lasting > 120 s (OR 14.4, 95% CI 1.7–121.8), and operative delivery (OR 6.8, 95% CI 1.2–37.6) ([PMID: 39411814](https://pubmed.ncbi.nlm.nih.gov/39411814/)). Earlier US data (KID 1997–2012) similarly identified shoulder dystocia, fetal macrosomia, and gestational diabetes as the highest-risk factors, with a protective effect of multiple birth mates ([PMID: 31856038](https://pubmed.ncbi.nlm.nih.gov/31856038/)). Additionally, resolution of shoulder dystocia requiring ≥3 maneuvers doubled the neonatal composite adverse outcome risk and specifically raised brachial plexus palsy risk (aIRR 2.58, 95% CI 1.45–4.60) ([PMID: 40239714](https://pubmed.ncbi.nlm.nih.gov/40239714/)).

> "Shoulder dystocia was the strongest risk factor for BPBI in the logistic regression model [adjusted odds ratio (AOR): 56.9, P <0.001]." — [PMID: 39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/)

| Risk / protective factor | Effect size | Source |
|---|---|---|
| Shoulder dystocia | AOR 56.9 (p<0.001) | PMID 39187951 |
| Shoulder dystocia > 120 s | OR 14.4 (95% CI 1.7–121.8) | PMID 39411814 |
| Maternal BMI > 30 kg/m² | OR 7.91 (95% CI 1.3–47.7) | PMID 39411814 |
| Operative (assisted vaginal) delivery | OR 6.8 (95% CI 1.2–37.6) | PMID 39411814 |
| ≥3 maneuvers to resolve dystocia | aIRR 2.58 (95% CI 1.45–4.60) | PMID 40239714 |
| Cesarean delivery (macrosomic) | AOR 0.581 (95% CI 0.365–0.925) — **protective** | PMID 39187951 |

### Finding 3 — Most cases recover spontaneously; surgery is indicated when biceps recovery is absent by 3–6 months

The natural history of Erb palsy is favorable. Multiple series report **80–95% spontaneous recovery** ([PMID: 12874720](https://pubmed.ncbi.nlm.nih.gov/12874720/)). A natural-history cohort documented spontaneous recovery in 59 of 81 patients (**73%**), with a functional biceps typically achieved by 10 months ([PMID: 25509702](https://pubmed.ncbi.nlm.nih.gov/25509702/)). A prospective OBPI cohort reported recovery in 24 of 28 infants (**85.7%**) and permanent injury in 4 of 28 (14.3%); notably, all permanent cases had shoulder dystocia (p = 0.007) ([PMID: 40843939](https://pubmed.ncbi.nlm.nih.gov/40843939/)). The classic surgical criterion, associated with Tassin and Gilbert, holds that infants with **no recovery of biceps function by 3 months** should undergo microsurgical exploration/repair without delay ([PMID: 8838992](https://pubmed.ncbi.nlm.nih.gov/8838992/)). This is nuanced by decision-analytic modeling favoring delayed repair at 12 months for quality-of-life optimization, since early surgery may be overly aggressive for infants who would recover spontaneously ([PMID: 24483255](https://pubmed.ncbi.nlm.nih.gov/24483255/)).

> "80 to 95% of these lesions recover spontaneously." — [PMID: 12874720](https://pubmed.ncbi.nlm.nih.gov/12874720/)
> "babies who have no recovery of the biceps function by three months of age should be operated without delay." — [PMID: 8838992](https://pubmed.ncbi.nlm.nih.gov/8838992/)

### Finding 4 — Diagnosis is clinical (Narakas classification); MRI has modest sensitivity for avulsion; glenohumeral dysplasia is a major sequela

Diagnosis rests on clinical examination and the Narakas classification (grade I: C5–C6; grade II: C5–C7; grade III: C5–T1; grade IV: C5–T1 with Horner syndrome). A meta-analysis of 8 studies (116 children) found MRI had a mean sensitivity of **68%** (95% CI 55–79%) and specificity of **89%** (95% CI 78–95%) for detecting root avulsion versus surgical exploration, with pseudomeningocele an unreliable marker ([PMID: 39432686](https://pubmed.ncbi.nlm.nih.gov/39432686/)); a 3T single-center series reported concordant accuracy (68% overall, 67% sensitivity, 92% specificity) ([PMID: 41451467](https://pubmed.ncbi.nlm.nih.gov/41451467/)). Clinical classification does not map perfectly onto anatomical injury: among Narakas 1 patients, only **23% had isolated C5–C6 injury**, while 55% had additional C7/C8/T1 involvement on MRI, and C6 was the most commonly injured/avulsed root ([PMID: 40828115](https://pubmed.ncbi.nlm.nih.gov/40828115/)). Shoulder dysplasia was diagnosed in **49% of 270 patients** with permanent BPBI, underscoring glenohumeral dysplasia as the principal long-term structural sequela ([PMID: 37503533](https://pubmed.ncbi.nlm.nih.gov/37503533/)).

> "The mean sensitivity and mean specificity of MRI for detecting root avulsion was 68% (95% CI: 55%, 79%) and 89% (95% CI: 78%, 95%), respectively." — [PMID: 39432686](https://pubmed.ncbi.nlm.nih.gov/39432686/)

### Finding 5 — Shoulder internal-rotation contracture arises from denervation-induced impaired subscapularis growth and muscle imbalance (rat models)

The mechanism of the contracture that defines chronic Erb palsy has been dissected in neonatal rat models of brachial plexus injury (NBPI). After C5–C6 neurotomy/crush at postnatal day 5, **all animals developed internal-rotation contracture within 4 weeks**, with external-rotation loss progressing from 52° to 82° over 1–4 months, and glenoid version shifting from 2° retroversion to 8° anteversion with pseudoglenoid formation, subluxation, and glenoid/humeral head deformity — recapitulating human glenohumeral dysplasia ([PMID: 18343282](https://pubmed.ncbi.nlm.nih.gov/18343282/)). Two complementary mechanisms were isolated: **(a) denervation** — selective subscapularis denervation alone caused 58° external-rotation loss and 69% muscle mass loss with reduced fiber size ([PMID: 25124991](https://pubmed.ncbi.nlm.nih.gov/25124991/)); and **(b) muscle imbalance** — suprascapular neurectomy sparing the subscapularis also produced contracture (66° ER loss) by unbalancing internal vs. external rotators ([PMID: 24388715](https://pubmed.ncbi.nlm.nih.gov/24388715/)). Cocontractions (simultaneous firing of antagonist muscles) are attributed to aberrant reinnervation through a neuroma-in-continuity, where regenerating axons reach the wrong target muscles ([PMID: 38263956](https://pubmed.ncbi.nlm.nih.gov/38263956/)). Glenoid deformity severity correlates with measurable gait/limb-function impairment in these models ([PMID: 29244216](https://pubmed.ncbi.nlm.nih.gov/29244216/)).

> "subscapularis denervation, per se, could explain shoulder contracture after neonatal brachial plexus injury" — [PMID: 25124991](https://pubmed.ncbi.nlm.nih.gov/25124991/)

### Finding 6 — Prevention is primarily obstetric: shoulder-dystocia simulation training and glycemic control reduce injury

Because Erb palsy is mechanically caused at delivery, prevention targets obstetric practice. An interrupted time-series study over 12 years in Bristol found that after introducing multi-professional shoulder-dystocia simulation training, the use of at least one resolution maneuver rose from 46.3% to 99.8%, and **brachial plexus injury at birth fell from 7.4% (24/324) pre-training to 1.3% (7/562) in late training** (p < 0.01) ([PMID: 25688719](https://pubmed.ncbi.nlm.nih.gov/25688719/)). French CNGOF guidelines establish that gestational-diabetes care reduces macrosomia and shoulder-dystocia risk (LE1, Grade A), that physical activity plus dietary measures in obese women reduce macrosomia (Grade A), and set estimated-fetal-weight thresholds for cesarean delivery ([PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/)). Importantly, **50–70% of shoulder-dystocia cases occur without identifiable risk factors**, capping the achievable benefit of risk-based prevention ([PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/)).

> "50-70% of SD cases occur in their absence, and most deliveries when they are present do not result in SD" — [PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/)

### Finding 7 — Treatment follows a staged ladder: physiotherapy → botulinum toxin → nerve reconstruction/transfers → secondary orthopedic procedures

Conservative therapy (physiotherapy/occupational therapy) is first-line to maintain passive range of motion and prevent contractures. **Botulinum toxin A** injected into the internal rotators improves passive external rotation (~46° gain at 4 months) and can defer or avoid tendon transfer in some children ([PMID: 32753228](https://pubmed.ncbi.nlm.nih.gov/32753228/)). **Primary microsurgery** — nerve grafting after neuroma excision, plus neurotization — is indicated when biceps recovery is absent by ~3–6 months. **Distal nerve transfers** as primary treatment in Narakas I injuries (spinal accessory → suprascapular nerve, plus Oberlin ulnar-fascicle → biceps) achieved ≥grade 4 elbow flexion in all 17 evaluable patients (mean Mallet 15) ([PMID: 27543083](https://pubmed.ncbi.nlm.nih.gov/27543083/)); a structured pediatric rehabilitation protocol (DAFRA) after SAN–SSN transfer achieved full external rotation against gravity in 71.4% ([PMID: 41500917](https://pubmed.ncbi.nlm.nih.gov/41500917/)). **Secondary orthopedic procedures** address residual deformity: subscapularis/anterior shoulder release improved glenoid version from −32° to −12° ([PMID: 30981548](https://pubmed.ncbi.nlm.nih.gov/30981548/)); open subscapularis lengthening with joint relocation gave durable glenohumeral remodeling at 10-year follow-up ([PMID: 31085034](https://pubmed.ncbi.nlm.nih.gov/31085034/)); latissimus dorsi/teres major tendon transfers, humeral derotation osteotomy, and radioulnar synostosis for supination deformity round out the toolkit ([PMID: 42568170](https://pubmed.ncbi.nlm.nih.gov/42568170/)). A systematic review of 965 patients confirmed that nerve grafts and transfers produce significant long-term gains in shoulder, elbow, and wrist function, though no single approach is universally superior ([PMID: 40958300](https://pubmed.ncbi.nlm.nih.gov/40958300/)).

> "Botulinum toxin A injections result in improvement in IRC due to BPBI, which is sustained beyond the expected half-life of 3 months." — [PMID: 32753228](https://pubmed.ncbi.nlm.nih.gov/32753228/)

### Finding 8 — Integrated synthesis: Erb palsy as an acquired, non-genetic C5–C6 birth traction injury

Synthesizing across all disease-characterization domains: Erb palsy is (1) the most common OBPI subtype (66.6%; [PMID: 40315612](https://pubmed.ncbi.nlm.nih.gov/40315612/)), incidence ~0.9–1.5/1000 ([PMID: 39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/)); (2) caused by mechanical stretch/overstretching of C5–C6/upper trunk during delivery, with shoulder dystocia the strongest risk factor (AOR 56.9) and cesarean protective ([PMID: 39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/)); (3) **without any genetic or infectious cause** (no OMIM/ClinVar gene); (4) 80–95% spontaneously recovering, with biceps recovery by 3 months pivotal ([PMID: 12874720](https://pubmed.ncbi.nlm.nih.gov/12874720/), [PMID: 8838992](https://pubmed.ncbi.nlm.nih.gov/8838992/)); (5) producing secondary internal-rotation contracture and glenohumeral dysplasia (49% of permanent cases) via denervation and muscle imbalance ([PMID: 25124991](https://pubmed.ncbi.nlm.nih.gov/25124991/), [PMID: 24388715](https://pubmed.ncbi.nlm.nih.gov/24388715/), [PMID: 37503533](https://pubmed.ncbi.nlm.nih.gov/37503533/)); (6) treated by a staged ladder ([PMID: 32753228](https://pubmed.ncbi.nlm.nih.gov/32753228/), [PMID: 27543083](https://pubmed.ncbi.nlm.nih.gov/27543083/), [PMID: 40958300](https://pubmed.ncbi.nlm.nih.gov/40958300/)); and (7) prevented obstetrically ([PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/), [PMID: 25688719](https://pubmed.ncbi.nlm.nih.gov/25688719/)). ICD-10 P14.0; MONDO:0700303.

> "overstretching of one or more cervical and thoracic nerve roots (C5-T1)" — [PMID: 41588374](https://pubmed.ncbi.nlm.nih.gov/41588374/)

---

## Full Report by Section

### 1. Disease Information

**Overview.** Erb palsy (Erb–Duchenne palsy) is a paralysis of the upper arm and shoulder caused by injury to the **upper trunk of the brachial plexus (C5–C6, sometimes C7)**, most commonly sustained during birth through lateral traction on the neck/head as the shoulder is delivered. It is the most common form of obstetric brachial plexus injury.

**Key identifiers.**
- **MONDO:** MONDO:0700303
- **ICD-10:** P14.0 (Erb paralysis due to birth injury)
- **ICD-11:** structural birth injury of brachial plexus (injury of brachial plexus codes)
- **MeSH:** "Brachial Plexus Neuropathies" / "Neonatal Brachial Plexus Palsy"; historically indexed under "Paralysis, Obstetric"
- **OMIM:** *Not applicable* — Erb palsy is an acquired mechanical injury, not a Mendelian disorder; there is no OMIM entry with a causal gene.
- **Orphanet:** Not a rare-disease genetic entry; obstetric brachial plexus palsy is captured as an acquired peripartum condition.

**Synonyms / alternative names:** Erb–Duchenne palsy; Erb's palsy; Duchenne–Erb paralysis; obstetric/obstetrical brachial plexus palsy or injury (OBPP/OBPI); brachial plexus birth injury (BPBI); neonatal brachial plexus palsy (NBPP); upper brachial plexus palsy; "waiter's-tip" deformity (describing posture, not a formal synonym).

**Information source type.** Evidence derives from **aggregated disease-level resources** (national inpatient/administrative databases, prospective surveillance cohorts, natural-history and surgical case series, and animal models), supplemented by individual-patient clinical follow-up cohorts. It is not a variant/EHR-genomic entity.

### 2. Etiology

**Primary cause — mechanical.** Erb palsy is caused by **traction/stretch (and, in severe cases, rupture or avulsion) of the C5–C6 nerve roots and upper trunk** during delivery, typically when the fetal head and neck are laterally displaced away from the shoulder. It is not genetic, infectious, toxic, or metabolic in origin.

**Risk factors (all environmental/obstetric — no genetic risk loci apply):**
- **Shoulder dystocia** — strongest factor, AOR 56.9 ([PMID: 39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/)); prolonged (>120 s) dystocia OR 14.4 ([PMID: 39411814](https://pubmed.ncbi.nlm.nih.gov/39411814/)); ≥3 resolution maneuvers aIRR 2.58 ([PMID: 40239714](https://pubmed.ncbi.nlm.nih.gov/40239714/)).
- **Fetal macrosomia** and **large-for-gestational-age** infants ([PMID: 31856038](https://pubmed.ncbi.nlm.nih.gov/31856038/)).
- **Maternal diabetes / gestational diabetes** ([PMID: 31856038](https://pubmed.ncbi.nlm.nih.gov/31856038/), [PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/)).
- **Maternal obesity** (BMI > 30, OR 7.91) ([PMID: 39411814](https://pubmed.ncbi.nlm.nih.gov/39411814/)).
- **Operative (assisted) vaginal delivery** (forceps/vacuum), OR 6.8 ([PMID: 39411814](https://pubmed.ncbi.nlm.nih.gov/39411814/)).
- **Anatomical predisposition** — a prefixed brachial plexus and the neonate's high head:body ratio and weak neck musculature increase susceptibility to traction ([PMID: 33904192](https://pubmed.ncbi.nlm.nih.gov/33904192/)).
- **Socioeconomic deprivation** has been associated with OBPP incidence ([PMID: 37694876](https://pubmed.ncbi.nlm.nih.gov/37694876/)).

**Protective factors.**
- **Cesarean delivery** — protective across weight classes, strongest in macrosomia (AOR 0.581) ([PMID: 39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/)).
- **Maternal glycemic control** and **weight management** reduce macrosomia and thereby dystocia risk ([PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/)).
- No genetic protective variants apply.

**Gene–environment interactions:** *Not applicable* — there is no established genetic contribution to Erb palsy risk.

### 3. Phenotypes

The core phenotype is a **flaccid, adducted, internally rotated arm with an extended, pronated forearm and flexed wrist** — the "waiter's-tip" posture — present at birth (neonatal onset). Grip is typically preserved (C8–T1 spared) in classic upper-trunk Erb palsy, distinguishing it from total plexus palsy.

| Phenotype | Type | HPO suggestion | Onset | Severity/progression | Frequency |
|---|---|---|---|---|---|
| Upper limb paralysis/weakness (shoulder abduction, external rotation, elbow flexion) | Clinical sign | HP:0003484 (Upper limb muscle weakness) | Neonatal/congenital | Variable; mostly improving | ~100% at presentation |
| "Waiter's-tip" posture (arm adducted, internally rotated, forearm pronated) | Physical manifestation | HP:0011461 (neonatal-onset, approximate) | Neonatal | Variable | Characteristic |
| Absent/reduced Moro reflex on affected side | Clinical sign | HP:0001319 (approximate) | Neonatal | — | Common |
| Shoulder internal-rotation contracture | Physical manifestation | HP:0031843 (Shoulder contracture, approximate) | Develops over months in persistent cases | Progressive if untreated | Major in persistent cases |
| Glenohumeral dysplasia/joint deformity | Clinical sign (imaging) | HP:0006633 (Glenoid dysplasia, approximate) | Infancy–childhood | Progressive | ~49% of permanent cases (PMID 37503533) |
| Limb-length/muscle atrophy of affected arm | Physical manifestation | HP:0009824 (Upper limb undergrowth) | Childhood | Slowly progressive | Persistent cases |
| Elbow flexion contracture / forearm supination deformity | Physical manifestation | HP:0001377 (Limited elbow extension) | Childhood | Progressive | Subset |

**Quality-of-life impact.** Persistent Erb palsy impairs bimanual activities of daily living, dressing, and self-care; residual weakness, contracture, cosmetic asymmetry, and limb-length discrepancy affect function and psychosocial well-being. Formal QoL instrument data (EQ-5D/SF-36/PROMIS) specific to Erb palsy are sparse; functional outcomes are typically measured with the **Mallet score** and the **Active Movement Scale (AMS)** rather than generic QoL tools ([PMID: 41500917](https://pubmed.ncbi.nlm.nih.gov/41500917/), [PMID: 40958300](https://pubmed.ncbi.nlm.nih.gov/40958300/)).

### 4. Genetic / Molecular Information

**Not applicable.** Erb palsy is an acquired mechanical birth injury. There is:
- **No causal gene** (no OMIM Mendelian entry).
- **No pathogenic variants** (no ClinVar/HGMD entries; no ACMG classification applies).
- **No allele frequencies**, no somatic/germline distinction.
- **No modifier genes** established. (The only "genetic-adjacent" susceptibility is anatomical variation such as a prefixed brachial plexus, which is not a molecular genetic trait; [PMID: 33904192](https://pubmed.ncbi.nlm.nih.gov/33904192/).)
- **No disease-specific epigenetic changes** or **chromosomal abnormalities**.

This absence is itself an informative characterization: knowledge-base fields for causal genes, variants, inheritance, and epigenetics should be marked **"not applicable — acquired non-genetic injury."**

### 5. Environmental Information

The relevant "environmental" factors are **peripartum mechanical and maternal-metabolic** rather than toxic/infectious:
- **Mechanical:** lateral neck traction during delivery, shoulder dystocia, instrumented delivery.
- **Maternal-metabolic:** diabetes/gestational diabetes and obesity (via macrosomia).
- **Lifestyle:** maternal physical activity and dietary control reduce risk indirectly by reducing macrosomia ([PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/)).
- **Infectious agents:** *Not applicable* — no pathogen causes or triggers Erb palsy.
- **Toxins/radiation/pollution/occupational exposure:** *Not applicable.*

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. During delivery (frequently complicated by shoulder dystocia/macrosomia), **excessive lateral traction increasing the head-to-shoulder angle** stretches the upper brachial plexus → **results in** overstretching of the C5–C6 (± C7) roots and upper trunk ([PMID: 41588374](https://pubmed.ncbi.nlm.nih.gov/41588374/), [PMID: 39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/)).
2. Stretch **leads to** a graded nerve injury — neuropraxia (conduction block), axonotmesis (axon disruption with intact sheath), neurotmesis (rupture), or, most severe, **root avulsion** from the spinal cord.
3. The nerve lesion **results in** partial or complete **denervation** of upper-limb muscles supplied by C5–C6: deltoid, supraspinatus, infraspinatus, biceps, brachialis, and subscapularis. *(GO: muscle denervation; cell types: CL:0000100 motor neuron, CL:0008002 skeletal muscle fiber.)*
4. **Branch A — spontaneous recovery (80–95%):** neuropraxic/mild axonotmetic fibers **remyelinate/regenerate**, restoring biceps and shoulder function, typically with biceps recovery by ~3 months ([PMID: 12874720](https://pubmed.ncbi.nlm.nih.gov/12874720/), [PMID: 8838992](https://pubmed.ncbi.nlm.nih.gov/8838992/)).
5. **Branch B — persistent injury (~5–20%):** severe axonotmesis, rupture, or avulsion **leads to** incomplete/aberrant reinnervation.
   - 5a. **Denervation atrophy of the subscapularis** and impaired muscle *growth* during a period of rapid skeletal growth **results in** a relatively short, stiff internal rotator → **shoulder internal-rotation contracture** ([PMID: 25124991](https://pubmed.ncbi.nlm.nih.gov/25124991/)).
   - 5b. **Muscle imbalance** between (relatively preserved) internal rotators and (weak, denervated) external rotators **contributes to** the same contracture even when the subscapularis is spared ([PMID: 24388715](https://pubmed.ncbi.nlm.nih.gov/24388715/)).
   - 5c. **Aberrant reinnervation through a neuroma-in-continuity** misroutes regenerating axons to antagonist muscles → **cocontractions** (e.g., simultaneous biceps/triceps firing), limiting usable motion ([PMID: 38263956](https://pubmed.ncbi.nlm.nih.gov/38263956/)).
6. Sustained contracture and abnormal muscle forces across the growing glenohumeral joint **result in** posterior humeral-head subluxation, **glenoid retroversion/pseudoglenoid formation, and glenohumeral dysplasia** — demonstrated in rat NBPI models (glenoid version shifting from retroversion toward anteversion) and observed in ~49% of human permanent cases ([PMID: 18343282](https://pubmed.ncbi.nlm.nih.gov/18343282/), [PMID: 37503533](https://pubmed.ncbi.nlm.nih.gov/37503533/)).
7. The combination **manifests clinically** as a weak, internally rotated, functionally impaired upper limb with limited abduction/external rotation, and secondary elbow-flexion and forearm-supination deformities in some ([PMID: 42568170](https://pubmed.ncbi.nlm.nih.gov/42568170/)).

**Upstream vs. downstream.** *Upstream:* the mechanical nerve lesion and denervation. *Downstream:* muscle atrophy/growth impairment, muscle imbalance, aberrant reinnervation → contracture → bony glenohumeral dysplasia. Steps 5a–5c are demonstrated primarily in **rat models** (inference to humans is strong but model-based); the human structural endpoint (dysplasia) is well documented clinically.

**Molecular/cellular processes involved:** peripheral nerve axonal injury and Wallerian degeneration/regeneration; muscle denervation atrophy (reduced fiber cross-sectional area, ~69% mass loss in denervated subscapularis; [PMID: 25124991](https://pubmed.ncbi.nlm.nih.gov/25124991/)); impaired skeletal-muscle longitudinal growth; endochondral/joint remodeling of the glenoid. **GO term suggestions:** GO:0031102 (neuron projection regeneration); GO:0043403 (skeletal muscle tissue regeneration); GO:0014732 (skeletal muscle atrophy). **CL suggestions:** CL:0000100 (motor neuron), CL:0008002 (skeletal muscle fiber), CL:0000138 (chondrocyte, for glenoid remodeling). No canonical intracellular signaling cascade (Wnt/MAPK/mTOR/PI3K–AKT) is disease-defining; this is a structural/mechanical injury rather than a signaling disorder.

### 7. Anatomical Structures Affected

- **Organ/system level (primary):** peripheral nervous system — the **brachial plexus, upper trunk (C5–C6 roots)**. UBERON: **UBERON:0001812** (brachial plexus); **UBERON:0000010** (peripheral nervous system).
- **Secondary/complication level:** shoulder girdle musculature and the **glenohumeral joint** (UBERON:0001470), with secondary bony deformity of the **glenoid/scapula** (UBERON:0006849 glenoid; UBERON:0006849/UBERON:0000976 humeral head). The **musculoskeletal system** is secondarily involved.
- **Tissue level:** **nervous tissue** (peripheral nerve) primarily; **skeletal muscle tissue** (subscapularis, deltoid, biceps, infraspinatus/supraspinatus) and **cartilage/bone** secondarily.
- **Cell level:** motor neurons/axons (CL:0000100), Schwann cells (CL:0002573), skeletal muscle fibers (CL:0008002), chondrocytes (CL:0000138).
- **Subcellular level:** axonal cytoskeleton and myelin sheath; no organelle-specific defect. GO cellular component: axon (GO:0030424), myelin sheath (GO:0043209).
- **Localization / lateralization:** **unilateral** in the overwhelming majority; affects the shoulder that was impacted during delivery. Bilateral involvement is rare (associated with breech delivery).

### 8. Temporal Development

- **Onset:** **congenital/neonatal** — present at or immediately after birth; onset is **acute** (a single mechanical event).
- **Course branches:**
  - *Recovery branch:* rapid improvement over weeks to months; biceps recovery by ~3 months is the key favorable prognostic sign; most recover by 10–12 months ([PMID: 25509702](https://pubmed.ncbi.nlm.nih.gov/25509702/)).
  - *Persistent branch:* if recovery is incomplete, deformities (contracture, dysplasia) **progress slowly** through childhood as the limb grows.
- **Disease "stages"** (functional/persistent cases): early denervation → developing contracture → established glenohumeral dysplasia → fixed bony deformity.
- **Duration:** self-limited in the majority; chronic/lifelong impairment in persistent cases.
- **Remission:** predominantly **spontaneous**; treatment-induced improvement via surgery/therapy in persistent cases.
- **Critical periods / windows of opportunity:** biceps recovery assessment at **3 months** (surgical-decision window); primary nerve reconstruction generally within **3–9 months**; glenohumeral remodeling after soft-tissue release is most reliable **before ~5 years of age** ([PMID: 31085034](https://pubmed.ncbi.nlm.nih.gov/31085034/), [PMID: 8838992](https://pubmed.ncbi.nlm.nih.gov/8838992/)).

### 9. Inheritance and Population

- **Epidemiology:** incidence ~**0.9–1.5 per 1000 live births** in administrative datasets, ~0.15/1000 in some declining national cohorts, up to **14.5/1000** by active surveillance (with 3.6/1000 persisting beyond 2 months) ([PMID: 40315612](https://pubmed.ncbi.nlm.nih.gov/40315612/), [PMID: 39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/), [PMID: 41616322](https://pubmed.ncbi.nlm.nih.gov/41616322/)). Incidence has declined over time in several countries (–47.6% in Germany 2005–2018) alongside rising cesarean rates and obstetric training.
- **Inheritance / penetrance / expressivity / anticipation / mosaicism / founder effects / carrier frequency:** **Not applicable** — acquired, non-heritable condition.
- **Population demographics:** no ethnic genetic predisposition; distribution tracks obstetric risk factors (macrosomia, maternal diabetes/obesity, birth-attendant practice, and access to cesarean delivery). Socioeconomic deprivation is associated with higher OBPP incidence ([PMID: 37694876](https://pubmed.ncbi.nlm.nih.gov/37694876/)). No consistent sex predilection is established. Age distribution: by definition affected at birth; the prevalent chronic population comprises children/adults with residual deficits.

### 10. Diagnostics

- **Clinical examination (primary):** characteristic waiter's-tip posture; assessment with **Active Movement Scale** and **Mallet score**; classification by **Narakas grade (I–IV)**.
- **Imaging:**
  - **MRI (3T)** — for root avulsion vs. rupture: mean sensitivity ~68%, specificity ~89% ([PMID: 39432686](https://pubmed.ncbi.nlm.nih.gov/39432686/), [PMID: 41451467](https://pubmed.ncbi.nlm.nih.gov/41451467/)); useful but cannot solely guide surgical decisions. Pseudomeningocele is an unreliable avulsion marker.
  - **CT myelography** — alternative for avulsion assessment.
  - **Ultrasound / MRI / CT** — for glenohumeral dysplasia (glenoid version, % humeral head anterior to scapular line).
  - **X-ray** — to exclude clavicular/humeral fracture (differential and co-injury).
- **Electrophysiology:** **EMG and nerve conduction studies** help characterize denervation, reinnervation, and prognosis; useful but must be interpreted cautiously in neonates.
- **Genetic testing (WGS/WES/panels/karyotype/CMA/FISH/mtDNA/repeat testing):** **Not applicable** — no genetic basis; genetic testing has no diagnostic role.
- **Laboratory tests / biomarkers / omics diagnostics:** **Not applicable** — no blood, metabolomic, proteomic, or molecular biomarker is used diagnostically.
- **Differential diagnosis:** clavicular or humeral fracture (pseudoparalysis), septic shoulder/osteomyelitis, cerebral injury with hemiparesis, total (pan-plexus) palsy, Klumpke (lower-plexus) palsy, and — in older presentations — non-plexus conditions (a specialty clinic found ~7% of presumed BPI patients had a non-plexus condition; [PMID: 40379206](https://pubmed.ncbi.nlm.nih.gov/40379206/)).
- **Screening:** newborn physical examination is the effective "screen"; no carrier/genetic screening applies.

### 11. Outcome / Prognosis

- **Survival/mortality:** Erb palsy is **not life-threatening**; survival is that of the general newborn population. Mortality is not disease-attributable.
- **Recovery:** **80–95% recover spontaneously**; the strongest positive prognostic factor is **biceps (elbow-flexion) recovery by 3 months** ([PMID: 12874720](https://pubmed.ncbi.nlm.nih.gov/12874720/), [PMID: 8838992](https://pubmed.ncbi.nlm.nih.gov/8838992/)). Presence of **shoulder dystocia** and severe/avulsion injuries predict persistence ([PMID: 40843939](https://pubmed.ncbi.nlm.nih.gov/40843939/)).
- **Morbidity/disability (persistent cases):** shoulder internal-rotation contracture, glenohumeral dysplasia (~49%), limb-length discrepancy, muscle atrophy, cocontractions, elbow-flexion and forearm-supination deformities; functional limitation in bimanual tasks.
- **Prognostic factors:** injury severity/extent (Narakas grade, root avulsion), timing of biceps recovery, presence of Horner syndrome (worse), and access to timely microsurgery.
- **Prognostic biomarkers:** none molecular; **serial clinical scoring (AMS/Mallet)** and **imaging of glenohumeral remodeling** serve as functional prognostic measures.

### 12. Treatment

**Staged, time-sensitive ladder** (NCIT-style intervention terms in brackets):

1. **Physiotherapy / occupational therapy** — first-line to maintain passive ROM and prevent contractures. *(NCIT: Physical Therapy; Occupational Therapy.)*
2. **Botulinum toxin A** into internal rotators/co-contracting muscles — improves passive external rotation (~46° at 4 months), may defer tendon transfer; also used before tendon transfer without permanent muscle atrophy ([PMID: 32753228](https://pubmed.ncbi.nlm.nih.gov/32753228/), [PMID: 36995203](https://pubmed.ncbi.nlm.nih.gov/36995203/)). *(NCIT: Botulinum Toxin Therapy.)*
3. **Primary microsurgical nerve reconstruction** — neuroma excision + **nerve grafting** ± neurotization when biceps recovery is absent by ~3–6 months; decision-analysis supports individualized timing (some model up to 12 months) ([PMID: 8838992](https://pubmed.ncbi.nlm.nih.gov/8838992/), [PMID: 24483255](https://pubmed.ncbi.nlm.nih.gov/24483255/), [PMID: 32588706](https://pubmed.ncbi.nlm.nih.gov/32588706/)). *(NCIT: Nerve Graft; Nerve Repair.)*
4. **Distal nerve transfers** — spinal accessory → suprascapular; Oberlin (ulnar fascicle → biceps); medial pectoral → axillary; effective as primary treatment in Narakas I with structured pediatric rehab ([PMID: 27543083](https://pubmed.ncbi.nlm.nih.gov/27543083/), [PMID: 41500917](https://pubmed.ncbi.nlm.nih.gov/41500917/)). *(NCIT: Nerve Transfer.)*
5. **Secondary orthopedic procedures** for residual deformity — subscapularis/anterior shoulder release (glenoid version −32°→−12°; [PMID: 30981548](https://pubmed.ncbi.nlm.nih.gov/30981548/)); open subscapularis lengthening + joint relocation (durable remodeling at 10 yr; [PMID: 31085034](https://pubmed.ncbi.nlm.nih.gov/31085034/)); arthroscopic release + conjoint tendon transfer ([PMID: 40772960](https://pubmed.ncbi.nlm.nih.gov/40772960/)); latissimus dorsi/teres major tendon transfers; humeral derotation osteotomy; radioulnar synostosis for supination deformity ([PMID: 42568170](https://pubmed.ncbi.nlm.nih.gov/42568170/)). *(NCIT: Tendon Transfer; Osteotomy; Arthrodesis.)*

**Outcomes.** A systematic review of 965 patients found nerve grafts/transfers produced significant long-term gains in shoulder, elbow, and wrist function, but no approach was universally superior and outcome heterogeneity limits comparison ([PMID: 40958300](https://pubmed.ncbi.nlm.nih.gov/40958300/)). **Pharmacotherapy** is limited to botulinum toxin; there are **no systemic drugs, gene therapies, cell therapies, RNA therapies, targeted therapies, or immunotherapies** for this mechanical injury — those categories are **not applicable**. **Pharmacogenomics:** not applicable.

### 13. Prevention

- **Primary (obstetric):** multi-professional **shoulder-dystocia simulation training** reduced brachial plexus injury at birth from 7.4% to 1.3% ([PMID: 25688719](https://pubmed.ncbi.nlm.nih.gov/25688719/)); **maternal glycemic control** and weight management reduce macrosomia/dystocia (Grade A) ([PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/), [PMID: 41365423](https://pubmed.ncbi.nlm.nih.gov/41365423/)); **cesarean delivery** for estimated fetal weight thresholds (e.g., >4500 g with diabetes, >5000 g without); judicious **induction of labor** for impending macrosomia ([PMID: 38477187](https://pubmed.ncbi.nlm.nih.gov/38477187/), [PMID: 33972073](https://pubmed.ncbi.nlm.nih.gov/33972073/)).
- **Secondary:** newborn examination for early detection and prompt referral to a multidisciplinary brachial plexus team.
- **Tertiary:** physiotherapy, botulinum toxin, and timely surgery to prevent contracture/dysplasia.
- **Limits:** 50–70% of shoulder dystocia occurs without identifiable risk factors, so prediction-based prevention is inherently capped ([PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/)).
- **Immunization / genetic counseling / vector control:** **Not applicable.**

### 14. Other Species / Natural Disease

- **Taxonomy affected (experimental):** *Rattus norvegicus* (NCBI:txid10116) is the principal experimental species; humans (NCBI:txid9606) are the natural host.
- **Natural veterinary disease:** Brachial plexus **traction/avulsion injuries** occur in companion animals (dogs, cats) — typically **traumatic (road-traffic)** rather than obstetric — and share the pathophysiology of nerve root avulsion and denervation. A specific *obstetric* Erb palsy analog is not a recognized distinct veterinary entity; the comparative value lies in shared nerve-injury/denervation mechanisms.
- **Comparative biology / evolutionary conservation:** the neonatal rat model faithfully reproduces the human sequence of denervation → contracture → glenohumeral dysplasia, indicating conserved musculoskeletal-growth responses to denervation ([PMID: 18343282](https://pubmed.ncbi.nlm.nih.gov/18343282/), [PMID: 29244216](https://pubmed.ncbi.nlm.nih.gov/29244216/)).
- **Transmission / zoonosis:** **Not applicable** (non-infectious, mechanical).

### 15. Model Organisms

- **Model type:** mammalian in vivo — **neonatal rat (Sprague-Dawley/Wistar) brachial plexus injury (NBPI) model**, created by C5–C6 neurotomy, crush, or selective neurectomy at postnatal day ~5 (an **induced/surgical** model, not genetic).
- **Genetic models:** none (no gene to target); models are surgical/chemodenervation-based.
- **Phenotype recapitulation:** high — 100% develop internal-rotation contracture within 4 weeks; progressive external-rotation loss; glenoid version changes; pseudoglenoid, subluxation, and humeral-head deformity mirror human glenohumeral dysplasia; gait/limb-function deficits correlate with deformity severity ([PMID: 18343282](https://pubmed.ncbi.nlm.nih.gov/18343282/), [PMID: 25124991](https://pubmed.ncbi.nlm.nih.gov/25124991/), [PMID: 24388715](https://pubmed.ncbi.nlm.nih.gov/24388715/), [PMID: 29244216](https://pubmed.ncbi.nlm.nih.gov/29244216/), [PMID: 38263956](https://pubmed.ncbi.nlm.nih.gov/38263956/)).
- **Limitations:** rodent shoulder biomechanics and quadrupedal loading differ from the human; the model does not reproduce the obstetric mechanism itself (it isolates the downstream denervation/contracture sequence); functional/QoL endpoints are not directly translatable.
- **Applications:** dissecting denervation vs. muscle-imbalance contributions to contracture, testing chemodenervation timing, studying aberrant reinnervation/cocontractions, and evaluating surgical/rehabilitative interventions.

---

## Mechanistic Model / Interpretation

```
  Shoulder dystocia / macrosomia / operative delivery
                    │  (lateral neck traction ↑ head–shoulder angle)
                    ▼
   Stretch injury of C5–C6 (± C7) roots / upper trunk
                    │
        ┌───────────┴───────────────┐
   neuropraxia/mild            severe axonotmesis /
   axonotmesis                 rupture / AVULSION
        │                            │
        ▼                            ▼
  spontaneous regeneration     incomplete + aberrant reinnervation
  (biceps by ~3 mo)                  │
        │                   ┌────────┼─────────────┐
        ▼                   ▼        ▼             ▼
   RECOVERY (80–95%)   subscapularis  muscle     neuroma-in-
                       denervation   imbalance   continuity →
                       + impaired    (IR>ER)     misrouting →
                       growth         │          COCONTRACTIONS
                            └────┬─────┘
                                 ▼
              SHOULDER INTERNAL-ROTATION CONTRACTURE
                                 │
                                 ▼
        posterior humeral-head subluxation + glenoid
        retroversion → GLENOHUMERAL DYSPLASIA (~49% of
        permanent cases) → fixed deformity, limb undergrowth
```

The unifying interpretation is that Erb palsy is a **single mechanical trigger with a bifurcating natural history**. The favorable branch dominates numerically. The unfavorable branch is not primarily about the nerve failing to regenerate but about the *downstream musculoskeletal consequences of denervation during active growth* — a subscapularis that is denervated, atrophic, and growth-restricted, compounded by imbalance and misrouted reinnervation, deforms the growing glenohumeral joint. This is why treatment is a *time-sensitive ladder*: nerve-level interventions must occur before irreversible muscle/joint changes, and once dysplasia is established, orthopedic reconstruction targets the downstream deformity. Prevention, correspondingly, sits entirely upstream at the obstetric event.

---

## Evidence Base

| PMID | Contribution | Type |
|---|---|---|
| [40315612](https://pubmed.ncbi.nlm.nih.gov/40315612/) | Erb palsy = 66.6% of OBPI; incidence trend –47.6% | Human, national cohort |
| [39187951](https://pubmed.ncbi.nlm.nih.gov/39187951/) | Shoulder dystocia AOR 56.9; cesarean protective; ~0.9–1.1/1000 | Human, KID database |
| [41616322](https://pubmed.ncbi.nlm.nih.gov/41616322/) | Active surveillance incidence 14.5/1000 (3.6/1000 persistent) | Human, prospective |
| [39411814](https://pubmed.ncbi.nlm.nih.gov/39411814/) | BMI, dystocia duration, operative delivery risk factors | Human, cohort |
| [40239714](https://pubmed.ncbi.nlm.nih.gov/40239714/) | ≥3 maneuvers double adverse outcomes; BPI aIRR 2.58 | Human, cohort |
| [31856038](https://pubmed.ncbi.nlm.nih.gov/31856038/) | Dystocia, macrosomia, gestational diabetes as top risks | Human, KID database |
| [12874720](https://pubmed.ncbi.nlm.nih.gov/12874720/) | 80–95% spontaneous recovery | Human, series |
| [25509702](https://pubmed.ncbi.nlm.nih.gov/25509702/) | 73% spontaneous recovery; natural history | Human, cohort |
| [40843939](https://pubmed.ncbi.nlm.nih.gov/40843939/) | 85.7% recovery; permanent cases all had dystocia | Human, prospective |
| [8838992](https://pubmed.ncbi.nlm.nih.gov/8838992/) | 3-month biceps criterion for surgery | Human, clinical |
| [24483255](https://pubmed.ncbi.nlm.nih.gov/24483255/) | Decision analysis favoring delayed (12 mo) repair for QoL | Computational |
| [32588706](https://pubmed.ncbi.nlm.nih.gov/32588706/) | Evidence review supporting nerve surgery when recovery delayed | Human, review |
| [39432686](https://pubmed.ncbi.nlm.nih.gov/39432686/) | MRI sensitivity 68%/specificity 89% for avulsion (meta-analysis) | Human, meta-analysis |
| [41451467](https://pubmed.ncbi.nlm.nih.gov/41451467/) | 3T MRI accuracy 68% vs. surgery | Human, cohort |
| [40828115](https://pubmed.ncbi.nlm.nih.gov/40828115/) | Narakas class ≠ MRI injury pattern; C6 most injured | Human, cohort |
| [37503533](https://pubmed.ncbi.nlm.nih.gov/37503533/) | Shoulder dysplasia in 49% of permanent BPBI | Human, cohort |
| [18343282](https://pubmed.ncbi.nlm.nih.gov/18343282/) | Rat model recapitulates contracture + dysplasia | Model organism |
| [25124991](https://pubmed.ncbi.nlm.nih.gov/25124991/) | Subscapularis denervation causes contracture | Model organism |
| [24388715](https://pubmed.ncbi.nlm.nih.gov/24388715/) | Muscle imbalance causes contracture | Model organism |
| [38263956](https://pubmed.ncbi.nlm.nih.gov/38263956/) | Neuroma-in-continuity → aberrant reinnervation/cocontractions | Model organism |
| [29244216](https://pubmed.ncbi.nlm.nih.gov/29244216/) | Glenoid deformity correlates with gait | Model organism |
| [25688719](https://pubmed.ncbi.nlm.nih.gov/25688719/) | Dystocia training reduces BPI 7.4%→1.3% | Human, time-series |
| [27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/) | CNGOF guidelines; glycemic control; prevention limits | Guideline |
| [32753228](https://pubmed.ncbi.nlm.nih.gov/32753228/) | Botulinum toxin improves IR contracture | Human, cohort |
| [27543083](https://pubmed.ncbi.nlm.nih.gov/27543083/) | Distal nerve transfers as primary treatment | Human, series |
| [41500917](https://pubmed.ncbi.nlm.nih.gov/41500917/) | DAFRA rehab; SAN–SSN 71.4% full ER | Human, series |
| [30981548](https://pubmed.ncbi.nlm.nih.gov/30981548/) | Anterior shoulder release improves glenoid version | Human, cohort |
| [31085034](https://pubmed.ncbi.nlm.nih.gov/31085034/) | Subscapularis lengthening; durable 10-yr remodeling | Human, cohort |
| [42568170](https://pubmed.ncbi.nlm.nih.gov/42568170/) | Radioulnar synostosis for supination deformity | Human, series |
| [40958300](https://pubmed.ncbi.nlm.nih.gov/40958300/) | Systematic review of 965 patients: nerve surgery gains | Human, systematic review |
| [41913992](https://pubmed.ncbi.nlm.nih.gov/41913992/) | Current concepts: staged surgical ladder | Human, review |
| [41588374](https://pubmed.ncbi.nlm.nih.gov/41588374/) | Defines overstretching of C5–T1 roots | Human, review |
| [33904192](https://pubmed.ncbi.nlm.nih.gov/33904192/) | Neonatal anatomy/evolution as predisposing factors | Human, review |
| [37694876](https://pubmed.ncbi.nlm.nih.gov/37694876/) | Deprivation associated with OBPP | Human, cohort |
| [40379206](https://pubmed.ncbi.nlm.nih.gov/40379206/) | ~7% of presumed BPI are non-plexus conditions | Human, cohort |

---

## Limitations and Knowledge Gaps

1. **Incidence uncertainty.** Estimates span an order of magnitude (0.15 to 14.5/1000) depending on ascertainment; administrative data undercount transient neuropraxia while active surveillance captures it. A standardized case definition and reporting mechanism is needed.
2. **Surgical timing controversy.** The 3-month biceps criterion ([PMID: 8838992](https://pubmed.ncbi.nlm.nih.gov/8838992/)) conflicts with decision-analytic support for delay to 12 months ([PMID: 24483255](https://pubmed.ncbi.nlm.nih.gov/24483255/)); no randomized trial exists, and evidence for nerve surgery vs. conservative management is Level IV at best ([PMID: 32588706](https://pubmed.ncbi.nlm.nih.gov/32588706/)).
3. **Outcome heterogeneity.** The systematic review of 965 patients highlights inconsistent outcome measures (AMS vs. Mallet vs. others), precluding definitive comparison of nerve-graft vs. nerve-transfer superiority ([PMID: 40958300](https://pubmed.ncbi.nlm.nih.gov/40958300/)).
4. **Classification–anatomy mismatch.** Narakas clinical grades do not reliably predict the true MRI/surgical injury pattern ([PMID: 40828115](https://pubmed.ncbi.nlm.nih.gov/40828115/)), and MRI sensitivity for avulsion is only ~68% ([PMID: 39432686](https://pubmed.ncbi.nlm.nih.gov/39432686/)).
5. **Mechanism evidence is model-based.** The denervation/muscle-imbalance/aberrant-reinnervation mechanisms are strongest in rat models; direct human molecular confirmation is limited.
6. **QoL data gap.** Erb-palsy-specific quality-of-life instrument data (EQ-5D/SF-36/PROMIS) are scarce; functional scores dominate.
7. **Prevention ceiling.** 50–70% of shoulder dystocia is unpredictable, limiting primary prevention ([PMID: 27318182](https://pubmed.ncbi.nlm.nih.gov/27318182/)).

## Proposed Follow-up Experiments / Actions

1. **Multicenter prospective registry** with a uniform case definition and standardized outcome set (AMS + Mallet + a validated pediatric QoL tool) to resolve incidence and outcome heterogeneity.
2. **Randomized/pragmatic trial** of surgical timing (early ~3 mo vs. delayed ~9–12 mo) stratified by injury severity and biceps recovery trajectory.
3. **Prospective head-to-head comparison** of primary distal nerve transfers vs. nerve grafting in Narakas I injuries.
4. **Improved imaging** — validate high-resolution/diffusion MRI or intraoperative electrophysiology to raise avulsion-detection sensitivity above the current ~68%.
5. **Mechanistic translation** — molecular/transcriptomic study of denervated human subscapularis at surgery to confirm rat-model growth-impairment pathways and identify anti-contracture drug targets.
6. **Prevention effectiveness** — evaluate scaled, mandatory shoulder-dystocia simulation training and its impact on population-level BPI rates, building on the Bristol interrupted time-series.

---

*Report compiled from an autonomous, literature-grounded investigation (5 iterations, 8 confirmed findings, 42 papers reviewed). Erb palsy is characterized here as an acquired, non-genetic C5–C6 brachial plexus birth traction injury; template sections concerning heritable genetics, epigenetics, inheritance, infectious agents, and systemic/gene/cell/RNA/immuno-therapeutics are explicitly marked not applicable.*


## Artifacts

- [OpenScientist final report](Erb_Palsy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Erb_Palsy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 40 |
| On topic | 31 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 14 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001319` (1 mention) - the report calls it "approximate"; HP calls it **Neonatal hypotonia**
- `HP:0031843` (1 mention) - the report calls it "Shoulder contracture, approximate"; HP calls it **Abnormally slow thought process**
- `CL:0000138` (2 mentions) - the report calls it "chondrocyte, for glenoid remodeling"; CL calls it **chondrocyte**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011461` (1 mention) - the report calls it "neonatal-onset, approximate"; HP calls it **Fetal onset**
- `HP:0006633` (1 mention) - the report calls it "Glenoid dysplasia, approximate"; HP calls it **Glenoid fossa hypoplasia**, and lists "Glenoid hypoplasia" among its other names
- `CL:0000100` (3 mentions) - the report calls it "motor neuron", "Cell level:** motor neurons/axons"; CL calls it **motor neuron**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000100` - called "motor neuron", "Cell level:** motor neurons/axons"