---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T03:30:07.980968'
end_time: '2026-09-25T03:46:51.222432'
duration_seconds: 1003.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Human Monocytic Ehrlichiosis
  mondo_id: MONDO:0000225
  category: Infectious Disease
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
citation_count: 28
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 23
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 31
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Human_Monocytic_Ehrlichiosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Human_Monocytic_Ehrlichiosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Human Monocytic Ehrlichiosis
- **MONDO ID:** MONDO:0000225 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Human Monocytic Ehrlichiosis** covering all of the
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

# Human Monocytic Ehrlichiosis (HME): Comprehensive Disease Characterization Report

**Target disease:** Human Monocytic Ehrlichiosis
**MONDO ID:** MONDO:0000225
**Category:** Infectious Disease (tick-borne bacterial zoonosis)
**Causative organism:** *Ehrlichia chaffeensis* (NCBI:txid159)

---

## Summary

Human Monocytic Ehrlichiosis (HME) is an acute, potentially life-threatening tick-borne bacterial infection caused by the obligate intracellular bacterium *Ehrlichia chaffeensis* (family Anaplasmataceae, order Rickettsiales). It is transmitted primarily by the lone star tick, *Amblyomma americanum*, and is maintained in nature in an enzootic cycle in which the white-tailed deer (*Odocoileus virginianus*) serves as the keystone host and major reservoir. First recognized as a human pathogen in 1986, *E. chaffeensis* infects and replicates within cells of the mononuclear phagocyte lineage (monocytes and macrophages), residing in membrane-bound vacuoles that resemble early endosomes. The disease is endemic to the southeastern and south-central United States and its incidence has risen steeply and expanded geographically over the past three decades, tracking the northward spread of its vector.

Clinically, HME presents as an undifferentiated febrile illness. Fever occurs in ~95% of patients, and the disease is characterized by a distinctive laboratory triad of **thrombocytopenia, leukopenia, and elevated hepatic transaminases**. Additional common features include headache, myalgia, and gastrointestinal symptoms; rash is common in children (~67%) but occurs in only about 30% of adults. Severe disease is largely **immunopathological** — a toxic-shock-like syndrome driven by dysregulated tumor necrosis factor-alpha (TNF-α) production by CD8⁺ T cells, suppressed protective CD4⁺ Th1/IFN-γ responses, and neutrophil-mediated tissue injury. Multi-organ involvement (central nervous system, lungs, kidneys, liver, and bone marrow) and complications such as acute respiratory distress syndrome (ARDS), acute renal failure, multi-organ failure, and secondary hemophagocytic lymphohistiocytosis (HLH) are more frequent in immunocompromised and elderly patients, who bear a disproportionate share of severe and fatal cases.

HME is a **non-genetic infectious disease**: there are no causal human genes, pathogenic variants, or inheritance considerations — host risk is defined by exposure and immune status rather than germline genetics. Diagnosis in the acute phase relies on nucleic-acid amplification (PCR, e.g., targeting the *E. chaffeensis* TRP120 gene), supported by peripheral-blood smear examination for intracytoplasmic morulae (specific but insensitive) and retrospective serology (indirect immunofluorescence antibody, IFA, requiring convalescent seroconversion). Treatment is **empiric doxycycline**, which is first-line for adults and children and should not be delayed pending laboratory confirmation; early therapy prevents severe morbidity and death. No vaccine exists, so prevention rests on tick-bite avoidance (DEET/picaridin repellents, permethrin-treated clothing, tick checks, and prompt tick removal). Surveillance case-fatality is ~1–3%, but rises to ~10–16% in hospitalized/immunocompromised cohorts.

---

## Key Findings

### 1. Etiology and transmission: an obligate intracellular tick-borne bacterium (F001, F011, F012)

HME is caused by ***Ehrlichia chaffeensis***, an obligately intracellular, tick-transmitted bacterium in the family Anaplasmataceae, order Rickettsiales. Its principal vector is the **lone star tick, *Amblyomma americanum*** (NCBI:txid6943), and its keystone vertebrate reservoir is the **white-tailed deer, *Odocoileus virginianus*** (NCBI:txid9874). The pathogen was first identified in 1986, and more than 1,000 patients had been reported by 2000. As stated in the foundational review, *"Ehrlichia chaffeensis is an obligately intracellular, tick-transmitted bacterium that is maintained in nature in a cycle involving at least one and perhaps several vertebrate reservoir hosts"* and the deer *"serves as a keystone host for all life stages of the principal tick vector (Amblyomma americanum) and is perhaps the most important vertebrate reservoir host for E. chaffeensis"* [PMID: 12525424](https://pubmed.ncbi.nlm.nih.gov/12525424/). The disease designation itself — *"human monocytic ehrlichiosis [HME], caused by Ehrlichia chaffeensis"* — is confirmed in [PMID: 17582569](https://pubmed.ncbi.nlm.nih.gov/17582569/).

**Alternative transmission routes** exist beyond tick bite. A review of U.S. cases from 1997–2020 identified 132 ehrlichiosis/anaplasmosis cases among blood transfusion and solid-organ transplant recipients — *"12 transfusion-associated cases and 120 cases in transplant recipients; 8 cases were donor-derived"* [PMID: 34670661](https://pubmed.ncbi.nlm.nih.gov/34670661/). Because *Ehrlichia* survives in stored blood and transplant recipients are immunosuppressed, blood transfusion and organ transplantation are recognized non-vector transmission routes.

**Zoonotic maintenance:** *E. chaffeensis* is maintained *"in a complex cycle involving white-tailed deer (WTD; Odocoileus virginianus) as a primary reservoir and the lone star tick (LST; Amblyomma americanum) as a primary vector"*, and natural *"disease has been documented in some domestic animals and wildlife including domestic dogs and ring-tailed lemurs"* [PMID: 19819631](https://pubmed.ncbi.nlm.nih.gov/19819631/). The closely related *E. canis* is *"primarily responsible for the canine monocytic ehrlichiosis and is endemic throughout the world"* [PMID: 18770538](https://pubmed.ncbi.nlm.nih.gov/18770538/), and *E. ewingii* causes granulocytotropic ehrlichiosis in humans and dogs (white-tailed deer are reservoirs for both *E. chaffeensis* and *E. ewingii*).

### 2. Clinical presentation and the laboratory triad (F002, F008, F013)

HME presents as a nonspecific febrile illness. A systematic review reported that *"HME primarily presents as an unspecific febrile illness (95% of the cases), often accompanied by thrombocytopenia (79.1% of the cases), leukopenia (57.8% of the cases), and abnormal liver function tests (68.1% of the cases)"* [PMID: 39093857](https://pubmed.ncbi.nlm.nih.gov/39093857/). The core laboratory triad is confirmed independently: *"The diseases generally present as undifferentiated fever, but thrombocytopenia, leukopenia, and increased serum transaminase activities are important laboratory features"* [PMID: 17582569](https://pubmed.ncbi.nlm.nih.gov/17582569/).

**Symptom spectrum differs by age.** In a pediatric case series (n=12, median age 7.4 y), *"Symptoms demonstrated by the patients during their illness included fever (100%), rash (67%), myalgias (58%), and vomiting, diarrhea, and headache (25%)"* and laboratory abnormalities included *"thrombocytopenia (92%), elevated liver function tests (91%), lymphopenia (75%), hyponatremia (67%), leukopenia (58%), and anemia (42%)"* [PMID: 9200384](https://pubmed.ncbi.nlm.nih.gov/9200384/); 4 of 12 presented in shock. In adults, *"Patients infected with Human Monocytic Ehrlichiosis often present with symptoms including fever, headache, myalgia, and occasionally a macular rash"* [PMID: 35986240](https://pubmed.ncbi.nlm.nih.gov/35986240/) — rash being far less common (~30%) than in children and less common than in Rocky Mountain spotted fever (RMSF).

**Gastrointestinal-hepatic involvement is prominent.** *"Signs and symptoms include abdominal pain, nausea, vomiting, diarrhea, jaundice, and hepatosplenomegaly"* and *"If not diagnosed and treated in a timely fashion, ehrlichiosis can progress to multiorgan failure"* [PMID: 10436355](https://pubmed.ncbi.nlm.nih.gov/10436355/).

| Feature | Frequency (pooled adults) | Frequency (pediatric series) |
|---|---|---|
| Fever | 95% | 100% |
| Thrombocytopenia | 79.1% | 92% |
| Elevated LFTs / transaminases | 68.1% | 91% |
| Leukopenia | 57.8% | 58% |
| Rash | ~30% | 67% |
| Lymphopenia | — | 75% |
| Hyponatremia | — | 67% |
| Anemia | — | 42% |

*Suggested HPO terms:* Fever (HP:0001945), Thrombocytopenia (HP:0001873), Leukopenia (HP:0001882), Elevated hepatic transaminase (HP:0002910), Headache (HP:0002315), Myalgia (HP:0003326), Skin rash (HP:0000988), Hepatosplenomegaly (HP:0001433), Hyponatremia (HP:0002902), Anemia (HP:0001903), Nausea and vomiting (HP:0002017), Diarrhea (HP:0002014).

### 3. Multi-system disease and complications (F009, F005)

HME is a multi-system disease. Neurologic involvement spans a wide spectrum: *"Ehrlichiosis can present with a spectrum of neurologic manifestations, ranging in severity from headache to meningoencephalitis"* [PMID: 16569376](https://pubmed.ncbi.nlm.nih.gov/16569376/). Pulmonary, renal, and hepatic complications are documented; one case report noted that the patient *"manifested known sequelae for this emerging disease, including dyspnea, pedal edema, increased transminases, and nephrotic syndrome"* [PMID: 11272720](https://pubmed.ncbi.nlm.nih.gov/11272720/).

Complications are strongly stratified by immune status. In the systematic review, complications were more frequent in immunocompromised versus immunocompetent patients: ARDS 34% vs 19.8%, acute renal failure 34% vs 15.8%, multi-organ failure 26% vs 14.9%, and secondary HLH 26% vs 14.9% [PMID: 39093857](https://pubmed.ncbi.nlm.nih.gov/39093857/).

*Affected organs / body systems (UBERON):* blood (UBERON:0000178), liver (UBERON:0002107), spleen (UBERON:0002106), bone marrow (UBERON:0002371), central nervous system (UBERON:0001017), lung (UBERON:0002048), kidney (UBERON:0002113). *Target cell types (CL):* monocyte (CL:0000576), macrophage (CL:0000235).

### 4. Pathophysiology: cellular subversion and immunopathology (F004, F003)

**Cellular subversion — upstream mechanism.** *E. chaffeensis* replicates in membrane-bound vacuoles resembling early endosomes within monocytes/macrophages, and it deploys **type IV secretion system (T4SS) effectors** to remodel host-cell biology. The effector Etf-2 arrests phagosome/endosome maturation: *"The type IV secretion system effector Ehrlichia translocated factor-2 (Etf-2) directly binds to RAB5-GTP on E. chaffeensis-containing vacuoles. Consequently, Etf-2 hinders the engagement of RAB5 GTPase-activating protein with RAB5-GTP, delays maturation of Ehrlichia vacuoles to late endosomes, thus facilitates infection"* [PMID: 40797321](https://pubmed.ncbi.nlm.nih.gov/40797321/). A second effector steals iron: *"Ehrlichia translocated factor-3 (Etf-3) is a type IV secretion system effector that binds host-cell ferritin light chain and induces ferritinophagy, thus increasing cellular labile iron pool for Ehrlichia proliferation"* [PMID: 39705831](https://pubmed.ncbi.nlm.nih.gov/39705831/); the same iron-robbery mechanism is described in [PMID: 34074773](https://pubmed.ncbi.nlm.nih.gov/34074773/).

**Immunopathology — downstream mechanism of severe disease.** In the Ixodes ovatus Ehrlichia (IOE / *Ehrlichia* sp. HF) murine model of fatal ehrlichiosis, lethal infection is driven not by bacterial burden alone but by a dysregulated host response: *"Lethal infections caused by high or low doses of IOE were accompanied by extensive liver damage, extremely elevated levels of TNF-alpha in the serum, high frequency of Ehrlichia-specific, TNF-alpha-producing CD8(+) T cells in the spleen, decreased Ehrlicha-specific CD4(+) T cell proliferation, low IL-12 levels in the spleen, and a 40-fold decrease in the number of IFN-gamma-producing CD4(+) Th1 cells"* [PMID: 14734762](https://pubmed.ncbi.nlm.nih.gov/14734762/). Neutrophils amplify the damage: *"depletion of neutrophils from lethally infected mice enhanced bacterial elimination, decreased immune-mediated pathology, and prolonged survival"* [PMID: 23478316](https://pubmed.ncbi.nlm.nih.gov/23478316/).

*Suggested GO / molecular terms:* protein secretion by the type IV secretion system (GO:0030255), phagosome maturation (GO:0090382), autophagy/ferritinophagy (GO:0006914), tumor necrosis factor production (GO:0032640), positive regulation of inflammatory response (GO:0050729), early endosome (GO:0005769). *Chemical entities (CHEBI):* iron (CHEBI:18248), doxycycline (CHEBI:50845).

### 5. Ordered mechanistic causal chain

```
1.  Infected Amblyomma americanum tick bites human
        -> inoculates Ehrlichia chaffeensis into dermis/blood
2.  E. chaffeensis is taken up by monocytes/macrophages
        -> resides in an early-endosome-like vacuole (morula)
3.  T4SS effector Etf-2 binds RAB5-GTP on the vacuole
        -> BLOCKS phagosome maturation to late endosome/lysosome
        -> bacterium evades lysosomal killing (immune evasion)
4.  T4SS effector Etf-3 binds ferritin light chain -> ferritinophagy
        -> RAISES labile iron pool -> fuels bacterial replication
5.  Intracellular proliferation + dissemination via mononuclear phagocytes
        -> seeds liver, spleen, bone marrow, lung, kidney, CNS
        -> cytopenias (thrombocytopenia, leukopenia) + transaminitis
   +---------------------------- BRANCH ----------------------------+
   | (a) Controlled response:                                       |
   |     CD4+ Th1 / IFN-gamma + macrophage activation               |
   |        -> bacterial clearance -> self-limited illness           |
   |        -> prompt doxycycline accelerates resolution             |
   |                                                                |
   | (b) Dysregulated response (severe/fatal; inferred from         |
   |     IOE murine model + immunocompromised human cohorts):       |
   |     Excess TNF-alpha from CD8+ T cells + suppressed CD4+ Th1    |
   |     (40-fold down IFN-gamma) + neutrophil-mediated injury       |
   |        -> toxic-shock-like syndrome, HLH, ARDS,                 |
   |           renal failure, multi-organ failure, death            |
   +----------------------------------------------------------------+
```

Steps 3–4 are demonstrated mechanistically in cellular/molecular models; the branch to severe immunopathology (step b) is strongly supported by the IOE murine model and by the clinical over-representation of immunocompromised patients among severe/fatal human cases, but the precise human effector-cell dynamics remain **inferred** rather than directly demonstrated in patients.

### 6. Epidemiology and demographics (F010, F005)

HME is endemic to the **southeastern and south-central United States**. Historical surveillance (1986–1997) reported 742 HME cases, and *"HME was most commonly reported from southeastern and southcentral states, while HGE was most often reported from northeastern and upper midwestern states"*; reported cases rose sharply — *"The annual number of reported cases increased sharply, from 69 in 1994 to 364 in 1997"* [PMID: 10511519](https://pubmed.ncbi.nlm.nih.gov/10511519/). Genus-level surveillance shows continued increases and northward geographic expansion tracking the vector; among the related *E. ewingii*, *"ehrlichiosis was reported more commonly among older, White, non-Hispanic, and male patients"* [PMID: 39983701](https://pubmed.ncbi.nlm.nih.gov/39983701/).

**Case fatality.** The Tick-Borne Disease Working Group reported that *"Human monocytic ehrlichiosis and anaplasmosis are life threatening diseases with estimated case fatality rates of 2.7 and 0.3%, respectively"* [PMID: 34517150](https://pubmed.ncbi.nlm.nih.gov/34517150/). In pooled reported (often hospitalized) cases, *"The overall case fatality is 11.6%, with a significant difference between immunocompetent (9.9%) and immunocompromized (16.3%) cases"*, and *"Immunocompromized patients are overrepresented among reviewed HME cases (26.7%), which indicates the role of HME as an opportunistic infection"* [PMID: 39093857](https://pubmed.ncbi.nlm.nih.gov/39093857/).

| Metric | Value | Source |
|---|---|---|
| Surveillance case-fatality | ~2.7% | [PMID: 34517150](https://pubmed.ncbi.nlm.nih.gov/34517150/) |
| Pooled reported-case fatality (overall) | 11.6% | [PMID: 39093857](https://pubmed.ncbi.nlm.nih.gov/39093857/) |
| Case-fatality, immunocompetent | 9.9% | [PMID: 39093857](https://pubmed.ncbi.nlm.nih.gov/39093857/) |
| Case-fatality, immunocompromised | 16.3% | [PMID: 39093857](https://pubmed.ncbi.nlm.nih.gov/39093857/) |
| Immunocompromised share of cases | 26.7% | [PMID: 39093857](https://pubmed.ncbi.nlm.nih.gov/39093857/) |

### 7. Diagnostics and differential diagnosis (F015, F016)

Acute-phase diagnosis relies on **nucleic-acid amplification**: real-time/duplex PCR targeting the *E. chaffeensis* TRP120 gene and multiplex qPCR panels. *"Early diagnosis is essential for rapid clinical treatment to avoid misdiagnosis and severe patient outcomes"* and *"the duplex real-time PCR assay was more sensitive than the nested PCR assay"* [PMID: 24023963](https://pubmed.ncbi.nlm.nih.gov/24023963/). Supporting laboratory findings include the CBC triad (thrombocytopenia, leukopenia) and elevated transaminases. **Serology** (IFA) is the reference standard but requires a ≥4-fold rise between acute and convalescent sera (collected 2–4 weeks apart) and is therefore retrospective. **Peripheral blood smear** for intracytoplasmic morulae in monocytes is rapid and specific but low-sensitivity.

The **differential diagnosis** encompasses other tick-borne illnesses. *"Tickborne diseases that affect patients in the United States include Lyme disease, Rocky Mountain spotted fever (RMSF), ehrlichiosis, anaplasmosis, babesiosis, tularemia, Colorado tick fever, and tickborne relapsing fever"* [PMID: 32352736](https://pubmed.ncbi.nlm.nih.gov/32352736/), and *"many of the signs and symptoms can mimic other common presentations"* [PMID: 37465658](https://pubmed.ncbi.nlm.nih.gov/37465658/). Distinguishing features of HME: less frequent rash than RMSF, prominent leukopenia/thrombocytopenia/transaminitis, and exposure geography/vector. Importantly, empiric doxycycline covers HME, anaplasmosis, ehrlichiosis, and RMSF simultaneously.

### 8. Treatment (F006, F013)

**Doxycycline is first-line** for HME in both adults and children. CDC guidelines direct clinicians to *"recognize that doxycycline is the treatment of choice for suspected tickborne rickettsial diseases in adults and children"* [PMID: 27172113](https://pubmed.ncbi.nlm.nih.gov/27172113/) and to *"understand that early empiric antibiotic therapy can prevent severe morbidity and death"* [PMID: 16572105](https://pubmed.ncbi.nlm.nih.gov/16572105/). Therapy should not be delayed pending laboratory confirmation; clinicians are advised *"to promptly start therapy with doxycycline, even in young children, when rickettsial infections are suspected"* [PMID: 26188606](https://pubmed.ncbi.nlm.nih.gov/26188606/) — concerns about dental staining from short courses in children are considered unfounded. Treatment is typically continued at least 3 days after defervescence (usually a 7–14 day course); defervescence usually occurs within 24–48 h of therapy. In the case series of GI/hepatic ehrlichiosis, all 8 patients responded to doxycycline [PMID: 10436355](https://pubmed.ncbi.nlm.nih.gov/10436355/). In severe HME-associated HLH, adjunctive corticosteroids/IVIG or anakinra have been used alongside doxycycline in case reports.

*Suggested NCIT term:* Doxycycline (NCIT:C299).

### 9. Prevention (F007)

No vaccine exists for HME; prevention rests on **tick-bite avoidance**. The Wilderness Medical Society guidelines give strong recommendations for *"the use of DEET, picaridin, and permethrin; tick checks; washing and drying clothing at high temperatures; mechanical tick removal within 36 h of attachment"* [PMID: 34642107](https://pubmed.ncbi.nlm.nih.gov/34642107/). Antibiotic prophylaxis after a tick bite is not routine for ehrlichiosis: *"Prophylactic treatment after tick exposure in patients without symptoms is generally not recommended"* [PMID: 32352736](https://pubmed.ncbi.nlm.nih.gov/32352736/).

### 10. Animal models and comparative biology (F014, F012)

Because *E. chaffeensis* does not cause lethal disease in immunocompetent mice, the ***Ehrlichia* sp. HF (IOE) fatal murine model** fills a critical gap: it *"causes acute fatal infection in laboratory mice that resembles acute fatal human monocytic ehrlichiosis caused by Ehrlichia chaffeensis"* and, *"As there is no small laboratory animal model to study fatal human ehrlichiosis, Ehrlichia sp. HF provides a needed disease model"* [PMID: 33407096](https://pubmed.ncbi.nlm.nih.gov/33407096/). *E. muris* provides a non-lethal, persistent-infection model. **White-tailed deer and dogs** serve as models of the natural transmission cycle; ticks infected with cultured organisms transmit infection — *"the transmission of both wild-type and transposon mutants of E. chaffeensis to its primary reservoir host, white tailed deer and to another known host, dog"* [PMID: 27729288](https://pubmed.ncbi.nlm.nih.gov/27729288/). The canine counterpart disease, canine monocytic ehrlichiosis (caused by *E. canis*), is an important veterinary analogue [PMID: 18770538](https://pubmed.ncbi.nlm.nih.gov/18770538/).

*Model organism / taxonomy identifiers:* *Ehrlichia chaffeensis* NCBI:txid159; *Amblyomma americanum* NCBI:txid6943; *Odocoileus virginianus* NCBI:txid9874; *Canis lupus familiaris* NCBI:txid9615; *Mus musculus* NCBI:txid10090.

---

## Section-by-Section Reference to the Research Template

### 1. Disease Information
Concise overview and identifiers as above. **Key identifiers:** MONDO:0000225; MeSH "Ehrlichiosis" (D016873); ICD-10 A77.40–A77.49 (Ehrlichiosis); ICD-11 1C30.2. There is no OMIM entry (non-genetic infectious disease). **Synonyms:** human monocytic ehrlichiosis, human monocytotropic ehrlichiosis, *Ehrlichia chaffeensis* infection, HME. Information is derived from **aggregated disease-level resources** (systematic reviews, CDC/surveillance data, case series) rather than a single EHR cohort.

### 2. Etiology
Primary cause is **infectious** (*E. chaffeensis*). **Risk factors** are environmental/behavioral: residence or activity in endemic southeastern/south-central U.S., outdoor/wooded exposure, tick bite, older age, male sex, and — for severe disease — **immunocompromise** (transplant, immunosuppression). No genetic (germline) susceptibility loci are established for humans. **Protective factors** are behavioral: repellent use, protective clothing, tick checks. **Gene–environment interactions:** not applicable in the human-germline sense; host–pathogen interaction is dominated by immune status.

### 3. Phenotypes
See Finding 2 table with HPO suggestions. Onset is acute; severity ranges mild → severe (variable), and untreated disease can be progressive to multi-organ failure. Quality-of-life impact is acute (days–weeks) in uncomplicated disease; survivors of severe disease may have prolonged recovery, but HME is not typically a chronic condition.

### 4. Genetic/Molecular Information
**Not applicable** to the human host: HME has no causal human genes, pathogenic variants, modifier genes, epigenetic disease drivers, or chromosomal abnormalities. The relevant molecular biology is that of the **pathogen genome** (~1.15 Mb), encoding the T4SS apparatus and effectors (Etf-1/Etf-2/Etf-3), ~23 P28/OMP-1 outer-membrane protein paralogs, and ankyrin-repeat/tandem-repeat proteins (TRP120 is a PCR diagnostic target).

### 5. Environmental Information
**Infectious agent:** *Ehrlichia chaffeensis* (NCBI:txid159). Environmental/lifestyle contributors are exposure-related (endemic geography, outdoor activity, occupational exposure such as forestry or military field exercises). No chemical toxins or pollutants are implicated.

### 6. Mechanism/Pathophysiology
See the ordered causal chain and Finding 4.

### 7. Anatomical Structures Affected
Primary target cells: **monocytes/macrophages** (CL:0000576, CL:0000235). Organs: blood, liver, spleen, bone marrow, lung, kidney, CNS (UBERON terms above). Subcellular: the pathogen resides in an **early-endosome-like vacuole** (GO:0005769). Involvement is systemic/bilateral where paired organs are affected.

### 8. Temporal Development
**Onset:** acute, typically days after tick exposure; any age (pediatric through geriatric). **Course:** self-limited or rapidly resolving with timely doxycycline (defervescence within 24–48 h); progressive to multi-organ failure if untreated. Not relapsing-remitting or chronic in typical disease.

### 9. Inheritance and Population
No inheritance pattern (infectious). Epidemiology per Finding 6: endemic southeastern/south-central U.S., rising and geographically expanding incidence; older, male predominance; immunocompromised over-representation among severe cases.

### 10. Diagnostics
Per Finding 7: acute-phase PCR (TRP120) is the test of choice; IFA serology retrospective; blood-smear morulae specific but insensitive; supporting CBC and LFT abnormalities. No genetic/omics diagnostics are used clinically.

### 11. Outcome/Prognosis
Case-fatality ~2.7% (surveillance) to ~10–16% (hospitalized/immunocompromised). Prognostic factors: **immune status, age, delay to doxycycline, and severity of cytopenias/organ dysfunction.** Complications: ARDS, acute renal failure, multi-organ failure, secondary HLH. Recovery is generally complete with timely treatment.

### 12. Treatment
Per Finding 8: empiric doxycycline first-line; adjunctive immunomodulation (steroids/IVIG/anakinra) for HLH in severe cases (case-report level evidence).

### 13. Prevention
Per Finding 9: tick-bite avoidance; no vaccine; prophylaxis not routine.

### 14. Other Species/Natural Disease
Zoonotic maintenance in white-tailed deer; natural infection of dogs and other mammals; veterinary counterpart canine monocytic ehrlichiosis (*E. canis*). See Finding 10.

### 15. Model Organisms
IOE/*Ehrlichia* sp. HF fatal murine model; *E. muris* persistent model; deer and dog transmission-cycle models. See Finding 10.

---

## Mechanistic Model / Interpretation

The unifying theme of HME pathogenesis is **a two-stage host–pathogen conflict inside the mononuclear phagocyte**. Upstream, *E. chaffeensis* wins the intracellular battle by secreting T4SS effectors that (i) freeze phagosome maturation (Etf-2/RAB5) to escape lysosomal destruction and (ii) divert host iron (Etf-3/ferritinophagy) to fuel replication. This explains the organism's tropism for monocytes/macrophages and its dissemination through the reticuloendothelial system, producing the hallmark cytopenias and transaminitis.

Downstream, disease **severity is determined by the host, not the microbe.** The IOE murine model demonstrates that fatal outcomes correlate with a maladaptive immune response — excess CD8⁺-derived TNF-α, collapse of protective CD4⁺ Th1/IFN-γ immunity, and neutrophil-driven tissue injury — rather than with overwhelming bacterial load. This immunopathological framework reconciles the clinical epidemiology: immunocompromised and elderly patients, whose immune regulation is impaired, suffer disproportionately severe disease, HLH, and death. It also rationalizes the therapeutic success of early doxycycline (halting bacterial replication before the immune response becomes self-destructive) and the emerging, case-report-level role of immunomodulation (steroids, IVIG, anakinra) in the sickest patients.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [12525424](https://pubmed.ncbi.nlm.nih.gov/12525424/) | Defines *E. chaffeensis* as obligate intracellular tick-borne pathogen; deer as keystone reservoir | Review |
| [17582569](https://pubmed.ncbi.nlm.nih.gov/17582569/) | HME etiology; undifferentiated fever + laboratory triad | Review |
| [39093857](https://pubmed.ncbi.nlm.nih.gov/39093857/) | Systematic review: phenotype frequencies, case-fatality by immune status | Systematic review |
| [14734762](https://pubmed.ncbi.nlm.nih.gov/14734762/) | TNF-α/CD8⁺ toxic-shock-like immunopathology (IOE model) | Model organism |
| [23478316](https://pubmed.ncbi.nlm.nih.gov/23478316/) | Neutrophils mediate immunopathology in fatal ehrlichiosis | Model organism |
| [40797321](https://pubmed.ncbi.nlm.nih.gov/40797321/) | Etf-2 blocks phagosome maturation via RAB5 | In vitro/molecular |
| [39705831](https://pubmed.ncbi.nlm.nih.gov/39705831/) | Etf-3 induces ferritinophagy / iron acquisition | In vitro/molecular |
| [34074773](https://pubmed.ncbi.nlm.nih.gov/34074773/) | Bacterial effector-induced ferritinophagy ("iron robbery") | In vitro/molecular |
| [34517150](https://pubmed.ncbi.nlm.nih.gov/34517150/) | Population-level case-fatality (2.7%) | Working group report |
| [27172113](https://pubmed.ncbi.nlm.nih.gov/27172113/) | CDC: doxycycline first-line, adults & children | Guideline |
| [16572105](https://pubmed.ncbi.nlm.nih.gov/16572105/) | Early empiric therapy prevents severe outcomes | Guideline |
| [26188606](https://pubmed.ncbi.nlm.nih.gov/26188606/) | Prompt doxycycline even in young children | Guideline/review |
| [34642107](https://pubmed.ncbi.nlm.nih.gov/34642107/) | Prevention: repellents, tick checks, removal | Guideline |
| [32352736](https://pubmed.ncbi.nlm.nih.gov/32352736/) | Differential diagnosis; prophylaxis not routine | Review |
| [9200384](https://pubmed.ncbi.nlm.nih.gov/9200384/) | Pediatric symptom/lab frequencies (rash 67%) | Case series |
| [35986240](https://pubmed.ncbi.nlm.nih.gov/35986240/) | Adult symptom spectrum | Case report |
| [16569376](https://pubmed.ncbi.nlm.nih.gov/16569376/) | CNS involvement | Review |
| [11272720](https://pubmed.ncbi.nlm.nih.gov/11272720/) | Pulmonary/renal/hepatic sequelae | Case report |
| [10511519](https://pubmed.ncbi.nlm.nih.gov/10511519/) | Geographic distribution; rising incidence | Surveillance |
| [39983701](https://pubmed.ncbi.nlm.nih.gov/39983701/) | Demographic pattern (older, male) | Surveillance |
| [34670661](https://pubmed.ncbi.nlm.nih.gov/34670661/) | Transfusion/transplant (donor-derived) transmission | Review |
| [19819631](https://pubmed.ncbi.nlm.nih.gov/19819631/) | Reservoir–vector zoonotic cycle | Review |
| [18770538](https://pubmed.ncbi.nlm.nih.gov/18770538/) | *E. canis* / canine monocytic ehrlichiosis | Review |
| [10436355](https://pubmed.ncbi.nlm.nih.gov/10436355/) | GI/hepatic manifestations; multi-organ failure | Case series/review |
| [33407096](https://pubmed.ncbi.nlm.nih.gov/33407096/) | IOE fatal murine model | Model organism |
| [27729288](https://pubmed.ncbi.nlm.nih.gov/27729288/) | Deer/dog transmission-cycle models | Model organism |
| [24023963](https://pubmed.ncbi.nlm.nih.gov/24023963/) | Duplex real-time PCR diagnosis | Diagnostic |
| [37465658](https://pubmed.ncbi.nlm.nih.gov/37465658/) | Signs/symptoms mimic other illnesses | Review |

---

## Limitations and Knowledge Gaps

1. **Immunopathology evidence is largely from murine models.** The TNF-α/CD8⁺/neutrophil toxic-shock-like mechanism is demonstrated primarily in the IOE (*Ehrlichia* sp. HF) mouse model, not *E. chaffeensis* in humans. Human immune-cell dynamics during severe HME remain inferred.
2. **Case-fatality estimates are heterogeneous.** Surveillance (~2.7%) versus pooled reported cases (~11.6%) differ because reported cohorts are enriched for hospitalized and immunocompromised patients; true population incidence and infection-fatality ratio are likely underestimated due to under-recognition of mild disease.
3. **No human genetic susceptibility data.** Whether host genetic variation modulates HME severity has not been studied at scale; the disease is treated as purely exposure/immune-status driven.
4. **Effector biology is incompletely mapped.** Beyond Etf-2 and Etf-3, the full T4SS effector repertoire and the roles of P28/OMP-1 paralogs and TRP/ankyrin proteins in pathogenesis are only partially characterized.
5. **HLH management is anecdotal.** Adjunctive immunomodulation (steroids, IVIG, anakinra) rests on case reports/small series, not trials.
6. **Diagnostic sensitivity gaps.** Acute serology is insensitive (retrospective), and blood-smear morulae are insensitive; PCR sensitivity depends on timing and bacterial load. There is no rapid point-of-care test.

## Proposed Follow-up Experiments / Actions

1. **Human immunophenotyping cohort:** longitudinal single-cell/cytokine profiling (TNF-α, IFN-γ, CD8⁺/CD4⁺ dynamics, neutrophil activation) in patients stratified by severity to validate the murine immunopathology model in humans.
2. **Effector-targeted therapeutics:** advance anti-Etf nanobody / mRNA-LNP approaches (already in cellular/murine proof-of-concept) toward preclinical efficacy against *E. chaffeensis*.
3. **Host-directed therapy trials:** structured evaluation of adjunctive immunomodulation (corticosteroids, anakinra/IL-1 blockade, IVIG) for HME-associated HLH and toxic-shock-like syndrome.
4. **Point-of-care molecular diagnostics:** develop and validate rapid isothermal amplification (e.g., RPA) assays for *E. chaffeensis* to enable earlier empiric-to-confirmed transitions.
5. **Prospective severity biomarkers:** test serum ferritin, TNF-α, and cytopenia trajectories as early predictors of progression to HLH/multi-organ failure.
6. **Expanded surveillance modeling:** integrate vector-range expansion (northward *A. americanum* spread) with climate data to forecast emerging endemic zones and guide prevention messaging.
7. **Blood/organ safety:** evaluate donor screening strategies given documented transfusion- and transplant-associated (donor-derived) transmission.

---

*Report compiled from 16 confirmed findings and 52 reviewed papers across 5 investigation iterations. Evidence types are distinguished as human clinical (case series, surveillance, guidelines), model organism (murine IOE, deer/dog), and in vitro/molecular (effector biology).*


## Artifacts

- [OpenScientist final report](Human_Monocytic_Ehrlichiosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Human_Monocytic_Ehrlichiosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005769` (2 mentions) - the report calls it "early-endosome-like vacuole"; GO calls it **early endosome**

Every term resolved, and every label the report gave matched.