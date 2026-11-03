---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-05T12:47:09.366361'
end_time: '2026-10-05T13:04:48.338820'
duration_seconds: 1058.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Factor XII Deficiency
  mondo_id: MONDO:0009315
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
citation_count: 36
reference_validation:
  total_references: 40
  verified: 40
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 20
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:41499201
  relevance_assessed: 40
  on_topic: 24
  off_topic: 3
  off_topic_references:
  - PMID:42433832
  - PMID:41499201
  - PMID:42268494
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 17
  verified: 15
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 7
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0003005
    reported_labels:
    - Abnormal coagulation factor activity
    ontology_label: Ganglioneuroma
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Factor_XII_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Factor_XII_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Factor XII Deficiency
- **MONDO ID:** MONDO:0009315 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Factor XII Deficiency** covering all of the
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

# Congenital Factor XII (Hageman Factor) Deficiency — Comprehensive Disease Characteristics Report

**Disease:** Congenital Factor XII Deficiency (Hageman trait)
**MONDO ID:** MONDO:0009315 · **OMIM:** 234000 · **Orphanet:** ORPHA:330 · **ICD-10:** D68.2 · **ICD-11:** 3B10.1 · **MeSH:** D005173 (Factor XII Deficiency)
**Category:** Mendelian (autosomal recessive)
**Causal gene:** *F12* (HGNC:3530; locus 5q35.3; UniProt P00748)

---

## Summary

Congenital Factor XII deficiency is the clearest example in human medicine of a dramatic laboratory abnormality that carries essentially no clinical consequence. It is an autosomal-recessive disorder caused by biallelic loss-of-function variants in the *F12* gene on chromosome 5q35.3. The hallmark is a **markedly prolonged activated partial thromboplastin time (aPTT)**—often exceeding 150–180 seconds against a reference range of roughly 22–32 s—accompanied by severely reduced FXII coagulant activity (FXII:C frequently <1–4%), yet **no bleeding tendency whatsoever**. This paradox is the central story of the disease: FXII initiates the contact (intrinsic) coagulation pathway *in vitro* but is dispensable for *in vivo* hemostasis. Most patients are identified incidentally during preoperative screening, during workup of an unexplained prolonged aPTT, or through family cascade testing, and require no treatment.

The mechanistic basis is now well understood. FXII is the initiator of the plasma **contact system**: it autoactivates on anionic surfaces (polyphosphate, extracellular DNA/NETs, collagen, and artificial surfaces such as kaolin or glass) to FXIIa, which drives two downstream arms—(1) the **intrinsic coagulation pathway** via activation of FXI, and (2) the **kallikrein-kinin system**, generating the vasoactive peptide bradykinin. Because the contact system contributes to thrombosis and inflammation (immunothrombosis) but not to the hemostatic plug that stops bleeding, its congenital absence is thrombo-neutral-to-protective and hemostatically silent. This decoupling has been confirmed across human cohorts, naturally FXII-deficient cats, knockout and humanized-knock-in mouse models, and—most decisively—by the 2025 FDA approval of the anti-FXIIa antibody **garadacimab**, which pharmacologically recapitulates the deficiency safely in humans.

Two important counterpoints frame the entry. First, well-powered studies **refute** the older suspicions that FXII deficiency causes venous/arterial thrombosis or recurrent pregnancy loss; both associations fail to survive rigorous, adjusted analysis. Second, *F12* is a two-faced gene: while loss-of-function causes benign deficiency, **gain-of-function** variants (e.g., p.Thr328Lys) cause **hereditary angioedema with normal C1-inhibitor (HAE-FXII)**—a mechanistically opposite, estrogen-dependent, bradykinin-driven swelling disorder. The same enzyme that is harmless to lose is dangerous to over-activate.

---

## Section 1 — Disease Information

**Overview.** Congenital FXII (Hageman factor) deficiency is a rare inherited coagulation-factor disorder characterized by reduced or absent plasma FXII activity. It is almost always **asymptomatic** and is typically discovered incidentally when a prolonged aPTT is found during routine or preoperative coagulation screening. Despite the striking *in vitro* clotting abnormality, affected individuals do not bleed abnormally, even during major surgery ([PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/); [PMID: 41977511](https://pubmed.ncbi.nlm.nih.gov/41977511/)).

**Key identifiers.** MONDO:0009315 · OMIM 234000 · Orphanet ORPHA:330 · ICD-10 D68.2 ("Other specified coagulation defects") · ICD-11 3B10.1 · MeSH D005173.

**Synonyms / alternative names.** Hageman factor deficiency; Hageman trait; FXII deficiency; F12 deficiency; coagulation factor XII deficiency. (The disorder is named for John Hageman, the first patient described, whose prolonged clotting time was discovered incidentally without any bleeding history.)

**Source of information.** Characterization derives from **aggregated disease-level resources** (OMIM, Orphanet, systematic reviews) supplemented by **individual-patient and pedigree reports** (case reports, single-center cohorts with molecular genotyping). Both evidence streams converge on the same benign phenotype.

---

## Section 2 — Etiology

**Primary cause — genetic.** The disease is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *F12***. Finding **F003** established this recessive basis: "Factor XII deficiency can be related to either homozygous or compound heterozygous pathogenic variants in the F12 gene" ([PMID: 38057855](https://pubmed.ncbi.nlm.nih.gov/38057855/)). Heterozygous carriers exhibit intermediate FXII:C (~50%) and are generally considered to have partial deficiency rather than overt disease.

**Genetic risk factors / modifier.** The common **F12 46C>T promoter polymorphism (c.-4C>T, rs1801020)** is a quantitative modifier of plasma FXII levels. T-allele carriers have dose-dependently lower FXII: ~132 U/dL in 46CC, 87 U/dL in 46CT, and 53 U/dL in 46TT individuals ([PMID: 18021303](https://pubmed.ncbi.nlm.nih.gov/18021303/)). This polymorphism explains much of the population variance in FXII activity and contributes to "partial" deficiency phenotypes.

**Environmental / acquired factors.** Congenital deficiency is genetically determined and not caused by environmental exposure. However, **acquired low FXII** can occur with liver disease (FXII is liver-synthesized), nephrotic syndrome, DIC, and in the presence of **anti-FXII autoantibodies or lupus anticoagulant / antiphospholipid antibodies**, which must be distinguished from inherited deficiency. Mild reductions in FXII:C have been noted in asymptomatic pediatric patients with transient antiphospholipid antibodies, so a differential diagnosis with mild congenital FXII deficiency should be considered ([PMID: 11333473](https://pubmed.ncbi.nlm.nih.gov/11333473/)).

**Protective factors / gene–environment interactions.** Not applicable in the conventional sense. Paradoxically, the loss-of-function state is itself *protective* against thrombosis in model systems (see Sections 6 and 12), but there are no established dietary, lifestyle, or protective-allele factors that modify the benign congenital phenotype.

---

## Section 3 — Phenotypes

The defining feature of FXII deficiency is the **dissociation between a laboratory abnormality and clinical silence**.

| Phenotype | Type | Onset | Severity | Frequency | HPO suggestion |
|---|---|---|---|---|---|
| Prolonged aPTT | Laboratory abnormality | Congenital (detectable lifelong) | Marked (often >150 s) | ~100% of severe cases | HP:0003645 (Prolonged partial thromboplastin time) |
| Reduced FXII:C / FXII:Ag | Laboratory abnormality | Congenital | Severe (<1–4% in homozygotes; ~50% in heterozygotes) | ~100% | HP:0003005 (Abnormal coagulation factor activity) |
| Normal PT, bleeding time, platelets | Laboratory finding | Congenital | — | ~100% | — |
| Absence of bleeding | Clinical (negative) | — | None | ~100% | — |

**Characteristics.** The abnormality is **congenital, stable, non-progressive, and lifelong**. In the Chinese Han cohort (n=14), all patients exhibited prolonged aPTT (mean 155.9 ± 89.7 s) and severely reduced FXII activity (mean 3.8 ± 4.0%) ([PMID: 42636605](https://pubmed.ncbi.nlm.nih.gov/42636605/), Finding **F001**). Crucially, this did not translate into bleeding: "Congenital FXII deficiency does not increase bleeding risk" ([PMID: 41977511](https://pubmed.ncbi.nlm.nih.gov/41977511/)), and patients "do not experience a higher risk of surgical bleeding despite a markedly prolonged activated partial thromboplastin time" ([PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/)).

**Quality-of-life impact.** For the great majority, essentially **none**. The disease does not impair daily functioning. The only meaningful QoL impacts are iatrogenic/psychological: unnecessary delay or cancellation of surgery, unnecessary transfusion of fresh frozen plasma, anticoagulation-management confusion (the prolonged aPTT cannot be used to monitor heparin), and anxiety from an abnormal lab value. No disease-specific EQ-5D/SF-36 data exist because there is no symptomatic disease to measure.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *F12* (HGNC:3530), on **chromosome 5q35.3**, encoding coagulation factor XII (Hageman factor), UniProt **P00748**. OMIM gene 610619; OMIM phenotype 234000.

**Pathogenic variant spectrum.** Severe deficiency arises from biallelic loss-of-function variants spanning missense, frameshift, and nonsense classes (Finding **F003**). Documented examples include:

| Variant (protein) | Variant (cDNA) | Type | Zygosity / context | PMID |
|---|---|---|---|---|
| p.Gly506Asp | — | Missense | Homozygous | [38057855](https://pubmed.ncbi.nlm.nih.gov/38057855/) |
| p.Lys365Glnfs*69 | c.1092dup / c.1092_1093insC | Frameshift | Homozygous in 28.6% of a Chinese cohort; recurrent | [42636605](https://pubmed.ncbi.nlm.nih.gov/42636605/), [37730224](https://pubmed.ncbi.nlm.nih.gov/37730224/) |
| p.Cys238Leufs*73 + p.Glu521Lys | c.712_713insT + c.1561G>A | Frameshift + missense | Compound heterozygous | [40372218](https://pubmed.ncbi.nlm.nih.gov/40372218/) |
| p.Phe51Serfs*44 | c.150delC | Frameshift | Homozygous, consanguineous | [37391120](https://pubmed.ncbi.nlm.nih.gov/37391120/) |
| p.Val579Hisfs*32 | c.1792_1796delGTCTA | Frameshift | Compound heterozygous (pathogenic, PVS1) | [37730224](https://pubmed.ncbi.nlm.nih.gov/37730224/) |
| p.Cys467Tyr | c.1457G>A | Missense (secretion defect) | Heterozygous modifier | [41811038](https://pubmed.ncbi.nlm.nih.gov/41811038/) |

Fifteen distinct *F12* variants (including eight novel) were catalogued in a single Chinese Han cohort, with impaired cellular secretion demonstrated for p.Q254P, p.S528Y, p.G376W, and p.V211Wfs*40: "Fifteen distinct F12 variants were identified, including eight novel ones. The frameshift variant c.1092dup was homozygous in 28.6% of this single-center cohort" ([PMID: 42636605](https://pubmed.ncbi.nlm.nih.gov/42636605/)). In-vitro expression work shows that some missense variants (e.g., p.Cys467Tyr) reduce FXII plasma levels through a **secretion defect**—protein accumulates in the cell lysate but fails to reach the supernatant—rather than through a transcription defect ([PMID: 41811038](https://pubmed.ncbi.nlm.nih.gov/41811038/)).

**Functional consequence.** **Loss of function** (quantitative reduction in secreted, functional FXII). Origin is **germline**. There is no somatic/oncologic dimension to this disorder, so COSMIC/TCGA are not applicable.

**Variant classification.** Truncating variants are classified pathogenic under ACMG/AMP (PVS1-based); recurrent missense/secretion-defect variants are pathogenic/likely-pathogenic with functional support. The 46C>T promoter variant is a benign common polymorphism acting as a quantitative modifier.

**Contrast — gain-of-function (HAE-FXII).** The missense **p.Thr328Lys (c.1032C>A)** and related exon-9 variants are **gain-of-function** changes that increase FXII amidolytic activity without lowering plasma FXII levels, causing hereditary angioedema rather than deficiency (Finding **F004**; see Section 6).

**Modifier genes / epigenetics / chromosomal abnormalities.** The dominant modifier is the *F12* 46C>T promoter polymorphism itself. No disease-specific epigenetic signatures (methylation/histone) or chromosomal abnormalities (aneuploidy, translocation) are associated with congenital FXII deficiency; it is a single-gene, point-/small-indel disorder.

---

## Section 5 — Environmental Information

Congenital FXII deficiency is a **purely genetic (Mendelian) disorder** with no environmental, lifestyle, or infectious etiology. There are no toxins, occupational exposures, dietary factors, or pathogens that cause the inherited condition. (Acquired FXII reduction—from liver disease, nephrotic syndrome, consumptive coagulopathy, or anti-FXII antibodies—is a separate, non-congenital phenomenon and a key differential diagnosis.) Infectious agents are not applicable.

---

## Section 6 — Mechanism / Pathophysiology

### Causal chain (ordered)

1. **Biallelic loss-of-function variant in *F12*** → **leads to** reduced synthesis/secretion of functional plasma FXII zymogen (demonstrated: truncating variants, secretion-defect missense variants; [PMID: 42636605](https://pubmed.ncbi.nlm.nih.gov/42636605/), [PMID: 41811038](https://pubmed.ncbi.nlm.nih.gov/41811038/)).
2. Low/absent plasma FXII → **results in** failure of contact activation when blood contacts an anionic surface (kaolin, glass, ellagic acid) in the aPTT reagent → **leads to** a **markedly prolonged aPTT** with normal PT (demonstrated; [PMID: 30630206](https://pubmed.ncbi.nlm.nih.gov/30630206/)).
3. Branch A (in vitro / artificial surfaces): Loss of FXIIa → **results in** no downstream FXI activation in the test tube → prolonged clotting time. **BUT** — the branch does **not** propagate to the body: in vivo hemostasis proceeds normally via tissue factor/FVIIa (extrinsic) and FXI activation by thrombin, so **no bleeding results** (demonstrated across cohorts and surgery; [PMID: 41977511](https://pubmed.ncbi.nlm.nih.gov/41977511/), [PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/)).
4. Branch B (pathological surfaces in vivo—polyphosphate, NETs/DNA): In normal individuals FXII autoactivates here to drive **immunothrombosis** and **bradykinin** generation; in deficiency this branch is **blunted**, which is thrombo-protective and anti-inflammatory rather than harmful (demonstrated in models; [PMID: 29483100](https://pubmed.ncbi.nlm.nih.gov/29483100/), [PMID: 34363738](https://pubmed.ncbi.nlm.nih.gov/34363738/), [PMID: 41683756](https://pubmed.ncbi.nlm.nih.gov/41683756/)).
5. Net clinical manifestation → a **benign, asymptomatic prolonged aPTT**, usually discovered incidentally.

### Normal FXII biology and the decoupling principle

FXII is a **modular multidomain zymogen** (Finding **F007**). Its heavy chain comprises fibronectin type II and type I domains, two EGF-like domains, a kringle domain, and a proline-rich region; the light chain is the serine-protease catalytic domain. On contacting a negatively charged surface, FXII binds and **autoactivates** to FXIIa. Surface binding maps to the **fibronectin type II domain** (residues ~30–47; [PMID: 11154114](https://pubmed.ncbi.nlm.nih.gov/11154114/)) and, critically, to **two positively charged lysine/histidine patches in the EGF-1 domain**: "Two unique, positively charged patches in the EGF-1 domain were identified (upstream, 73K74K76K78H81K82H; downstream, 87K113K). Neutralizing the charge of both patches led to a 99% reduction in FXII kaolin binding, subsequent decrease in autoactivation of 94%" ([PMID: 38897387](https://pubmed.ncbi.nlm.nih.gov/38897387/))—with aPTT prolonged from 36 to 223 s, a structural proof that surface binding is the trigger step.

FXIIa then drives **two pathways** (Finding **F005**): "This system activates 2 distinct pathways, the intrinsic pathway of coagulation via cleavage of FIX, and inflammation via HK cleavage resulting in bradykinin (BK) generation" ([PMID: 40638675](https://pubmed.ncbi.nlm.nih.gov/40638675/)). Beyond proteolysis, zymogen FXII "signals via urokinase-type plasminogen activator receptor (uPAR) to induce neutrophil extracellular trap formation (NETosis), thereby amplifying immunothrombosis" ([PMID: 41301820](https://pubmed.ncbi.nlm.nih.gov/41301820/)).

The pivotal mechanistic insight—explaining the entire benign phenotype—is that **thrombosis and hemostasis are decoupled at FXII**: "targeting factor XII or its activator polyphosphate, provides protection from thromboembolic diseases without interfering with hemostasis" ([PMID: 29483100](https://pubmed.ncbi.nlm.nih.gov/29483100/)), and in animal models "either its knock-out or inhibition in animal models efficiently reduced thrombosis without affecting normal hemostasis" ([PMID: 34363738](https://pubmed.ncbi.nlm.nih.gov/34363738/)).

### Gain-of-function branch (the mechanistic opposite)

The same gene produces an opposite disease when activity is *increased*. The HAE-causing **p.Thr328Lys** is "a gain-of-function mutation that markedly increases FXII amidolytic activity but that does not alter FXII plasma levels" ([PMID: 17186468](https://pubmed.ncbi.nlm.nih.gov/17186468/)). Excess FXIIa over-drives the kallikrein-kinin arm → excess **bradykinin** → recurrent angioedema—especially under high-estrogen states (oral contraceptives, pregnancy), almost exclusively in women; in some such families "mutations in the coagulation factor XII (Hageman factor) gene were detected" ([PMID: 24176211](https://pubmed.ncbi.nlm.nih.gov/24176211/)) (Finding **F004**).

```
                         ┌─ LOSS OF FUNCTION (deficiency) ─ benign, no bleeding, thrombo-neutral
   F12 variant ──────────┤
                         └─ GAIN OF FUNCTION (p.Thr328Lys) ─ HAE-FXII, excess bradykinin, angioedema

   Normal FXII pathway:
   anionic surface → FXII → FXIIa ──► (A) FXI → intrinsic coagulation  [in vitro aPTT; dispensable in vivo]
                                   ├─► (B) prekallikrein → kallikrein → HK → BRADYKININ  [inflammation/HAE]
                                   └─► uPAR signaling → NETosis → immunothrombosis
```

**Ontology suggestions.** GO:0007596 (blood coagulation); GO:0002542 (Factor XII activation); GO:0007597 (blood coagulation, intrinsic pathway); GO:0030193 (regulation of blood coagulation); CHEBI:bradykinin; CHEBI:polyphosphate. Cell types: hepatocyte (CL:0000182, source of FXII); neutrophil (CL:0000775, NETosis/immunothrombosis); platelet (CL:0000233, polyphosphate source).

---

## Section 7 — Anatomical Structures Affected

Congenital FXII deficiency is a **systemic plasma-protein deficiency without a target organ**; there is no structural tissue pathology.

- **Organ / system level.** The affected "compartment" is the **blood / circulatory system** (UBERON:0000178, blood; UBERON:0001969, blood plasma). The **liver** (UBERON:0002107) is the site of FXII synthesis and thus the biological origin of the deficient protein, but the liver is structurally normal. No organ is damaged by the deficiency.
- **Tissue / cell level.** **Hepatocytes** (CL:0000182) synthesize FXII. Cells functionally relevant to normal FXII biology (and therefore to its absence) include **neutrophils** (CL:0000775, NETosis/immunothrombosis) and **platelets** (CL:0000233, polyphosphate release). None is pathologically altered in deficiency.
- **Subcellular level.** FXII is a **secreted plasma protein**; relevant compartments are the **endoplasmic reticulum / secretory pathway** (GO:0005783; GO:0005576, extracellular region) where secretion-defect missense variants cause intracellular retention ([PMID: 41811038](https://pubmed.ncbi.nlm.nih.gov/41811038/)).
- **Localization / lateralization.** Not applicable—this is a diffuse plasma deficiency with no anatomical site or lateralization.

---

## Section 8 — Temporal Development

- **Onset.** **Congenital**; the deficiency is present from birth and is lifelong. Because it is asymptomatic, the *age of detection* varies widely—from neonatal incidental findings to late-adult preoperative workups.
- **Onset pattern.** Chronic/constitutive (a stable trait, not an acute event).
- **Progression.** **None.** The disorder is **stable and non-progressive**; FXII levels remain constant throughout life (barring superimposed acquired causes). There are no disease "stages."
- **Disease course.** Chronic and lifelong, but clinically silent. There is no relapsing-remitting or progressive course.
- **Remission / critical periods.** Not applicable. The only clinically relevant "time windows" are iatrogenic decision points—e.g., **perioperative assessment**, where the prolonged aPTT must be correctly interpreted as benign to avoid unnecessary intervention, and **pregnancy/delivery**, where management guidance is debated but the deficiency itself does not warrant routine prophylaxis.

---

## Section 9 — Inheritance and Population

**Inheritance.** **Autosomal recessive.** Severe (complete) deficiency requires biallelic variants; heterozygotes have partial (~50%) deficiency that is itself benign (Finding **F003**). Consanguinity increases the likelihood of homozygous severe deficiency—documented in a consanguineous family where "Sequencing revealed a homozygous frameshift mutation c.150delC (p.Phe51Serfs*44) site in the F12 gene exon 3" ([PMID: 37391120](https://pubmed.ncbi.nlm.nih.gov/37391120/)).

**Penetrance / expressivity.** The laboratory phenotype (prolonged aPTT, low FXII:C) is **fully penetrant** for the biochemical trait; the *clinical* phenotype is essentially null (no symptoms). Expressivity of FXII level varies with genotype and the 46C>T modifier.

**Epidemiology.**

| Measure | Estimate | Source |
|---|---|---|
| Severe (homozygous/complete) deficiency incidence | **≈ 1 in 1,000,000** | [PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/) |
| Partial (heterozygous) deficiency | Relatively common | [PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/) |
| Low FXII in a general population (Korea) | High incidence of plasma FXII deficiency reported in normal Korean subjects | [PMID: 16165195](https://pubmed.ncbi.nlm.nih.gov/16165195/) |

"A total absence of FXII as seen in homozygous patients, is rare, with an incidence of approximately 1/1,000,000 individuals" ([PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/), Finding **F006**).

**Population demographics.** Partial FXII deficiency / low FXII activity appears **more frequent in some East Asian populations** (notably a high incidence reported in normal Korean subjects, [PMID: 16165195](https://pubmed.ncbi.nlm.nih.gov/16165195/)), consistent with the recurrent frameshift variants seen in Chinese Han cohorts ([PMID: 42636605](https://pubmed.ncbi.nlm.nih.gov/42636605/)). The 46C>T promoter T-allele—lowering FXII—has substantial population frequency (~38% heterozygous, ~5% homozygous in one European cardiology cohort; [PMID: 18021303](https://pubmed.ncbi.nlm.nih.gov/18021303/)). **Sex ratio** for the deficiency is approximately equal (autosomal). (By contrast, the gain-of-function HAE-FXII disorder occurs almost exclusively in women.)

---

## Section 10 — Diagnostics

**Core laboratory pattern (Finding F006):**

1. **Isolated prolonged aPTT with normal PT** (intrinsic-pathway screen abnormal; extrinsic normal). "The APTT is also sensitive to contact factor deficiencies, including factor XII, prekallikrein, and high-molecular-weight kininogen" ([PMID: 30630206](https://pubmed.ncbi.nlm.nih.gov/30630206/)).
2. **Mixing study corrects the aPTT**—indicating factor deficiency rather than an inhibitor: "an isolated prolonged aPTT, which was corrected with mixing studies, and a severe FXII deficiency with activity levels < 1%" ([PMID: 41977339](https://pubmed.ncbi.nlm.nih.gov/41977339/)).
3. **Confirmation by one-stage FXII:C clotting assay** plus **FXII:Ag ELISA** to distinguish cross-reactive-material (CRM) status.
4. **Viscoelastic testing** shows a hypocoagulable INTEM with a normal EXTEM ([PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/)).

**Key differential diagnoses.** Other contact-factor deficiencies (prekallikrein, high-molecular-weight kininogen), which also prolong the aPTT without bleeding ([PMID: 30630206](https://pubmed.ncbi.nlm.nih.gov/30630206/)); **lupus anticoagulant / antiphospholipid antibodies** (which do *not* fully correct on mixing and may coexist with mildly reduced FXII:C, [PMID: 11333473](https://pubmed.ncbi.nlm.nih.gov/11333473/)); heparin contamination; and bleeding-associated intrinsic-factor deficiencies (FVIII, FIX, FXI—which *do* cause bleeding and must be excluded).

**Genetic / molecular confirmation.** Sanger sequencing or whole-exome sequencing of *F12* confirms the diagnosis and identifies the causal variant(s) ([PMID: 37391120](https://pubmed.ncbi.nlm.nih.gov/37391120/); [PMID: 42636605](https://pubmed.ncbi.nlm.nih.gov/42636605/)). Single-gene *F12* testing is sufficient; WGS/CMA/karyotyping/FISH/mtDNA/repeat-expansion testing are **not applicable**. A key clinical caveat: the prolonged aPTT **cannot be used to monitor heparin** in these patients and can confound activated-clotting-time (ACT) assessment during cardiac surgery ([PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/)).

**Omics.** Plasma **metabolomic profiling** has been applied to FXII-deficient cohorts ([PMID: 42636605](https://pubmed.ncbi.nlm.nih.gov/42636605/)), but no omics test is required for diagnosis.

**Screening.** There is **no newborn or population screening** for FXII deficiency (no clinical benefit). **Cascade family testing** is reasonable for genetic counseling once a proband is identified, chiefly to reassure relatives and prevent unnecessary perioperative intervention.

---

## Section 11 — Outcome / Prognosis

**Prognosis is excellent—essentially a normal life expectancy.** FXII deficiency does not cause bleeding, does not shorten survival, and does not independently cause thrombosis.

**Thrombosis—refuted as a causal risk (Finding F002).** Despite longstanding speculation (fueled by the original patient John Hageman, who later died of a pulmonary embolism), rigorous studies find **no independent association**:

| Study | Design | Result |
|---|---|---|
| Leiden Thrombophilia Study ([PMID: 7947293](https://pubmed.ncbi.nlm.nih.gov/7947293/)) | Population-based case-control (DVT) | FXII deficiency 6% (21/350) cases vs 5% (18/350) controls; **matched OR 1.2 (95% CI 0.6–2.4)**. "We do not consider factor XII to be a determinant of deep-vein thrombosis." |
| 2026 systematic review/meta-analysis ([PMID: 42035525](https://pubmed.ncbi.nlm.nih.gov/42035525/)) | 6 studies, 5,003 individuals | Pooled **RR 1.34 (95% CI 0.99–1.81)**; DVT subgroup RR 1.44 (0.88–2.36); **adjusted OR 1.03 (0.65–1.64)** — not significant. |

Lower FXII activity is best regarded as a **risk marker rather than a risk factor** for cardiovascular disease ([PMID: 18331454](https://pubmed.ncbi.nlm.nih.gov/18331454/)); emerging consensus even views FXII (and FXI) deficiency as **protective** against thrombosis ([PMID: 42610269](https://pubmed.ncbi.nlm.nih.gov/42610269/); [PMID: 41977511](https://pubmed.ncbi.nlm.nih.gov/41977511/)).

**Recurrent pregnancy loss—controversial, not clearly causal (Finding F009).** Some cohorts report reduced FXII in women with recurrent spontaneous abortion ([PMID: 24597288](https://pubmed.ncbi.nlm.nih.gov/24597288/)) or recurrent IVF-ET failure (median FXII 79.5 vs 109, p<0.001; [PMID: 18294355](https://pubmed.ncbi.nlm.nih.gov/18294355/)). However, a careful study found "Low FXII activity was not associated with RPL"—only the 46C/T genotype showed a weak association (OR 2.8), and FXII level did not predict subsequent miscarriage ([PMID: 25489738](https://pubmed.ncbi.nlm.nih.gov/25489738/)). Where a reproductive association exists, it may reflect **acquired anti-FXII autoantibodies** (which augment platelet aggregation), not congenital deficiency ([PMID: 26011374](https://pubmed.ncbi.nlm.nih.gov/26011374/)).

**Complications / morbidity.** The chief "complications" are **iatrogenic**: unnecessary surgical delay, inappropriate FFP transfusion, and misinterpretation of heparin monitoring. True disease-related morbidity is negligible.

---

## Section 12 — Treatment

**No treatment is required for congenital FXII deficiency itself.** Because there is no bleeding tendency, factor replacement and prophylaxis are generally unnecessary even for major surgery ([PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/)). Management is largely **educational**: correctly interpreting the prolonged aPTT, avoiding unneeded blood products, and counseling.

**Perioperative / obstetric management** is individualized and not standardized. A pregnancy case series (19 pregnancies across 9 publications) used prophylactic fresh frozen plasma with selective low-molecular-weight heparin, emphasizing multidisciplinary, dynamic risk stratification balancing a theoretical bleeding/thrombosis concern—though the evidence base is thin and guidelines are lacking ([PMID: 41429486](https://pubmed.ncbi.nlm.nih.gov/41429486/)).

**FXII as a therapeutic target (the inverse application).** The deficiency's safety makes **FXIIa inhibition** an attractive antithrombotic/anti-inflammatory strategy (Findings **F005**, **F011**). Classes in development include antisense oligonucleotides, siRNAs, monoclonal antibodies, peptides (e.g., Ir-CPI), and recombinant inhibitors (rHA-Infestin-4) ([PMID: 41640375](https://pubmed.ncbi.nlm.nih.gov/41640375/); [PMID: 41977511](https://pubmed.ncbi.nlm.nih.gov/41977511/)).

**Clinical proof-of-concept — garadacimab (Finding F011).** **Garadacimab (Andembry, garadacimab-gxii)** — "a first-in-class monoclonal antibody that inhibits activated Factor XII (FXIIa)" — was FDA-approved for "prophylaxis of HAE attacks in patients aged ≥12 years" ([PMID: 42433832](https://pubmed.ncbi.nlm.nih.gov/42433832/); [PMID: 41499201](https://pubmed.ncbi.nlm.nih.gov/41499201/)).

| Parameter | Value | Source |
|---|---|---|
| Pivotal trial | Phase 3 VANGUARD (NCT04656418) | [PMID: 42433832](https://pubmed.ncbi.nlm.nih.gov/42433832/) |
| Attack reduction | **91.5%**; ~77% attack-free | [PMID: 42433832](https://pubmed.ncbi.nlm.nih.gov/42433832/) |
| Integrated efficacy | 94.9% monthly-attack reduction (n=164) | [PMID: 42268494](https://pubmed.ncbi.nlm.nih.gov/42268494/) |
| Dosing | 200 mg SC monthly (half-life ~18–20 d) | [PMID: 42057602](https://pubmed.ncbi.nlm.nih.gov/42057602/) |
| Safety | No drug-related SAEs; mild injection-site reactions, headache, nasopharyngitis; no deaths | [PMID: 42268494](https://pubmed.ncbi.nlm.nih.gov/42268494/) |

Critically, the **long-term safety profile of pharmacologic FXIIa blockade mirrors the benign congenital deficiency**: preclinically, "FXII inhibition prevented thrombus formation and reduced fibrin deposition, achieving effects comparable to heparin but with markedly lower bleeding risk" ([PMID: 41977511](https://pubmed.ncbi.nlm.nih.gov/41977511/)). Garadacimab thus provides a human "experiment" confirming that removing FXII(a) activity is safe. **NCIT suggestion:** Garadacimab (monoclonal antibody); drug class — anti-FXIIa monoclonal antibody / contact-pathway inhibitor.

---

## Section 13 — Prevention

Because congenital FXII deficiency is a benign Mendelian trait, **classical prevention is neither needed nor possible**. There is no primary prevention (no modifiable risk factor), no immunization, and no indicated population screening.

- **Genetic counseling** is the only relevant preventive measure: explaining autosomal-recessive inheritance, offering **cascade testing** of relatives primarily to prevent *iatrogenic harm* (unnecessary surgical delay/transfusion), and providing reassurance regarding the absence of bleeding risk.
- **Tertiary "prevention"** amounts to avoiding inappropriate medical intervention based on the isolated prolonged aPTT.
- For affected women contemplating pregnancy, individualized counseling is reasonable given the (unresolved) literature on reproductive outcomes, but no standardized prophylaxis is established ([PMID: 41429486](https://pubmed.ncbi.nlm.nih.gov/41429486/)).

---

## Section 14 — Other Species / Natural Disease

FXII deficiency occurs **naturally and commonly in the domestic cat** (*Felis catus*; NCBI Taxon 9685), providing a striking comparative-biology confirmation of the benign phenotype (Finding **F010**).

- A clinically normal cat showed "an intrinsic coagulation defect characterized by prolonged activated partial thromboplastin time, with normal bleeding time, platelet count, and prothrombin time," confirmed as FXII deficiency ([PMID: 879587](https://pubmed.ncbi.nlm.nih.gov/879587/)).
- Breeding studies established an inheritance pattern that "revealed an autosomal recessive pattern similar to that reported in humans (Hageman trait)" (heterozygotes ~50% FXII:C; homozygotes <2%) ([PMID: 7427778](https://pubmed.ncbi.nlm.nih.gov/7427778/)).
- A modern cohort found that "FXII deficiency is common in domestic cats, and also present in many different breeds," with a Midwestern-US geographic bias; **none of 26 deficient cats bled**, and two high-frequency *F12* variants were identified: "an exon 13 missense mutation (c.1631G > C) and an exon 11 deletion mutation (c.1321delC)" ([PMID: 31022435](https://pubmed.ncbi.nlm.nih.gov/31022435/)).

**Evolutionary perspective (Finding F008).** An evolutionary review frames the FXII contact system as a **foreign-surface-sensing / immunothrombosis module** that arose in terrestrial animals, consistent with the minimal bleeding phenotype of deficiency and with the **secondary loss of *F12* in marine mammals**: these facts help "explain the minimal bleeding phenotype of FXII deficiency and the secondary loss of F12 in marine mammals" ([PMID: 41301820](https://pubmed.ncbi.nlm.nih.gov/41301820/)). The gene is evolutionarily dispensable for hemostasis—whole lineages have lost it. **Orthologous gene:** cat *F12*; mouse *F12*. No zoonotic/transmission dimension applies.

---

## Section 15 — Model Organisms

- **Mouse (*Mus musculus*, NCBI Taxon 10090).** *F12* **knockout mice** are the foundational model: they show reduced experimental thrombosis **without impaired hemostasis**, directly demonstrating the thrombosis/hemostasis decoupling ([PMID: 34363738](https://pubmed.ncbi.nlm.nih.gov/34363738/); [PMID: 29483100](https://pubmed.ncbi.nlm.nih.gov/29483100/)). A **humanized FXII knock-in mouse** was generated as "a powerful model system to test novel anti-thrombotic agents," enabling testing of human-FXII-targeting therapeutics in vivo ([PMID: 34363738](https://pubmed.ncbi.nlm.nih.gov/34363738/)).
- **Disease-relevant model phenotypes (Finding F012).** FXII deficiency/inhibition in rodent models reduces arterial/venous thrombosis and extracorporeal-circuit clotting; reduces **stroke infarct volume**; attenuates **neutrophil-driven inflammation**—"FXII deficiency has been associated with reduced neutrophil adhesion and migration in sterile skin wounds and immune complex-induced vasculitis"; and in neurological conditions "FXII deficiency significantly reduced the number and severity of multiple sclerosis relapses and decreased the volume of post-traumatic brain oedema" ([PMID: 41683756](https://pubmed.ncbi.nlm.nih.gov/41683756/)).
- **Cat (natural model).** The naturally FXII-deficient domestic cat is an informative *spontaneous* model recapitulating the human recessive, non-bleeding trait ([PMID: 31022435](https://pubmed.ncbi.nlm.nih.gov/31022435/)).
- **In vitro.** HEK293T expression systems have characterized the molecular consequences of *F12* missense variants (secretion defects), a tractable system for variant interpretation ([PMID: 41811038](https://pubmed.ncbi.nlm.nih.gov/41811038/)).

**Phenotype recapitulation.** Mouse knockouts faithfully reproduce the human **non-bleeding** phenotype and the **anti-thrombotic/anti-inflammatory** consequences—arguably better than they model any "disease," since FXII deficiency has no overt human pathology to reproduce. **Limitation:** because the human condition is essentially asymptomatic, models are used to study FXII's *normal* roles and to validate it as a *drug target*, rather than to model a damaging disease.

---

## Mechanistic Model / Interpretation (Synthesis)

The unifying thesis is the **thrombosis–hemostasis decoupling at FXII**, which explains every observation in this report:

```
 F12 LOF variant (biallelic)
        │
        ▼
 ↓ secreted functional FXII  ──────────────┐
        │                                   │ (contrast)
        ▼                           F12 GOF (p.Thr328Lys)
 No contact activation on                   │
 artificial anionic surface                 ▼
        │                           ↑ FXIIa amidolytic activity
        ▼                                   │
 PROLONGED aPTT (normal PT)                 ▼
        │                           excess bradykinin
        │                                   │
   ┌────┴─────────────┐                     ▼
   ▼                  ▼                 HAE-FXII (angioedema)
 In vitro:        In vivo:
 clotting slow    hemostasis intact (TF/FVIIa + thrombin→FXI)
                       │
                       ├─► thrombosis risk NOT increased (OR~1.0–1.2)
                       ├─► immunothrombosis/NETosis BLUNTED (protective)
                       └─► NO BLEEDING  →  benign incidental lab finding
```

Four independent evidence streams converge on the same conclusion:
1. **Human cohorts** — severe deficiency, markedly prolonged aPTT, no bleeding ([PMID: 42636605](https://pubmed.ncbi.nlm.nih.gov/42636605/), [PMID: 35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/)).
2. **Epidemiology** — no causal thrombosis link ([PMID: 7947293](https://pubmed.ncbi.nlm.nih.gov/7947293/), [PMID: 42035525](https://pubmed.ncbi.nlm.nih.gov/42035525/)).
3. **Comparative biology** — cats deficient and non-bleeding; marine mammals have *lost* the gene ([PMID: 31022435](https://pubmed.ncbi.nlm.nih.gov/31022435/), [PMID: 41301820](https://pubmed.ncbi.nlm.nih.gov/41301820/)).
4. **Pharmacology** — FXIIa blockade (garadacimab) is safe and effective in humans ([PMID: 42433832](https://pubmed.ncbi.nlm.nih.gov/42433832/)).

The deeper insight is that FXII is better understood as an **immunothrombosis / foreign-surface-sensing node** than as a hemostatic factor. Its congenital absence removes a pathological-amplification pathway (thrombosis, NETosis, bradykinin-driven inflammation) while leaving physiological clotting intact—making "the disease" a near-perfect natural knockout and the gene an ideal drug target.

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [42636605](https://pubmed.ncbi.nlm.nih.gov/42636605/) | Chinese Han cohort: aPTT 155.9±89.7 s, FXII:C 3.8±4.0%; 15 variants incl. recurrent c.1092dup; metabolomics (F001, F003, F006) |
| [30630206](https://pubmed.ncbi.nlm.nih.gov/30630206/) | aPTT sensitivity to contact-factor deficiencies incl. FXII (F001) |
| [41977511](https://pubmed.ncbi.nlm.nih.gov/41977511/) | FXII deficiency does not increase bleeding; FXII inhibition antithrombotic with low bleeding (F001, F002, F005, F011) |
| [7947293](https://pubmed.ncbi.nlm.nih.gov/7947293/) | Leiden Thrombophilia Study — no DVT association (F002) |
| [42035525](https://pubmed.ncbi.nlm.nih.gov/42035525/) | Meta-analysis — no significant thrombosis association (F002) |
| [38057855](https://pubmed.ncbi.nlm.nih.gov/38057855/) | Recessive genetic basis; homozygous p.Gly506Asp (F003) |
| [37391120](https://pubmed.ncbi.nlm.nih.gov/37391120/) | Consanguineous family, homozygous frameshift; WES (F003, F006) |
| [40372218](https://pubmed.ncbi.nlm.nih.gov/40372218/), [37730224](https://pubmed.ncbi.nlm.nih.gov/37730224/) | Compound-heterozygous pedigrees, variant spectrum (F003) |
| [41811038](https://pubmed.ncbi.nlm.nih.gov/41811038/) | p.Cys467Tyr secretion-defect mechanism (Sections 4, 7) |
| [17186468](https://pubmed.ncbi.nlm.nih.gov/17186468/) | p.Thr328Lys gain-of-function → HAE (F004) |
| [24176211](https://pubmed.ncbi.nlm.nih.gov/24176211/) | F12 mutations in HAE with normal C1-INH (F004) |
| [27905115](https://pubmed.ncbi.nlm.nih.gov/27905115/) | HAE-FXII treatment cohort (n=72) (F004) |
| [40638675](https://pubmed.ncbi.nlm.nih.gov/40638675/) | Contact system structure; dual intrinsic + bradykinin pathways (F005) |
| [29483100](https://pubmed.ncbi.nlm.nih.gov/29483100/) | Thrombosis/hemostasis decoupling (F005) |
| [34363738](https://pubmed.ncbi.nlm.nih.gov/34363738/) | Humanized FXII knock-in mouse; KO reduces thrombosis, spares hemostasis (F005, Sec 15) |
| [38897387](https://pubmed.ncbi.nlm.nih.gov/38897387/) | EGF-1 domain patches mediate surface binding/autoactivation (F007) |
| [11154114](https://pubmed.ncbi.nlm.nih.gov/11154114/) | Fibronectin type II surface-binding site (F007) |
| [35417978](https://pubmed.ncbi.nlm.nih.gov/35417978/) | Incidence ~1/1,000,000; no surgical bleeding; ACT/viscoelastic findings (F006, Sec 11) |
| [41977339](https://pubmed.ncbi.nlm.nih.gov/41977339/) | Diagnostic pattern: isolated prolonged aPTT correcting on mixing, FXII <1% (F006) |
| [41301820](https://pubmed.ncbi.nlm.nih.gov/41301820/) | Evolutionary immunothrombosis module; marine-mammal F12 loss; uPAR/NETosis (F008, F012) |
| [25489738](https://pubmed.ncbi.nlm.nih.gov/25489738/) | RPL not associated with low FXII (F009) |
| [24597288](https://pubmed.ncbi.nlm.nih.gov/24597288/), [18294355](https://pubmed.ncbi.nlm.nih.gov/18294355/), [26011374](https://pubmed.ncbi.nlm.nih.gov/26011374/) | Opposing RPL/IVF evidence; anti-FXII autoantibodies (F009) |
| [31022435](https://pubmed.ncbi.nlm.nih.gov/31022435/), [7427778](https://pubmed.ncbi.nlm.nih.gov/7427778/), [879587](https://pubmed.ncbi.nlm.nih.gov/879587/) | Feline natural disease: common, AR, non-bleeding; F12 variants (F010) |
| [42433832](https://pubmed.ncbi.nlm.nih.gov/42433832/), [42268494](https://pubmed.ncbi.nlm.nih.gov/42268494/), [41499201](https://pubmed.ncbi.nlm.nih.gov/41499201/), [42057602](https://pubmed.ncbi.nlm.nih.gov/42057602/) | Garadacimab FDA approval, efficacy, safety, dosing (F011) |
| [41683756](https://pubmed.ncbi.nlm.nih.gov/41683756/) | FXII deficiency anti-inflammatory/neuroprotective in models (F012) |
| [18021303](https://pubmed.ncbi.nlm.nih.gov/18021303/), [18331454](https://pubmed.ncbi.nlm.nih.gov/18331454/) | 46C>T polymorphism dose-effect; FXII as risk marker not factor (Sec 4, 11) |
| [16165195](https://pubmed.ncbi.nlm.nih.gov/16165195/) | High incidence of low FXII in Korean subjects (Sec 9) |
| [42610269](https://pubmed.ncbi.nlm.nih.gov/42610269/) | FXII/FXI deficiency viewed as thrombo-protective (Sec 11) |
| [41429486](https://pubmed.ncbi.nlm.nih.gov/41429486/) | Pregnancy management case series (Sec 12, 13) |
| [11333473](https://pubmed.ncbi.nlm.nih.gov/11333473/) | Mild FXII reduction vs antiphospholipid antibodies — differential dx (Sec 2, 10) |

**Evidence-source mix:** human clinical cohorts/case reports and epidemiology (most sections); model-organism (mouse KO/knock-in, natural feline disease); in vitro (HEK293T variant expression, domain mutagenesis); and computational/evolutionary (comparative genomics of F12 loss).

---

## Limitations and Knowledge Gaps

1. **Rarity limits power.** Complete (homozygous) deficiency is ~1/1,000,000, so cohorts are small (often single-center, n≤30) and geographically skewed (many from East Asian centers), limiting generalizability of variant-frequency and metabolomic data.
2. **Reproductive outcomes unresolved.** The link to recurrent pregnancy loss remains genuinely controversial. The best-designed study is negative, but publication bias and the confound of acquired anti-FXII autoantibodies vs congenital deficiency are not fully disentangled.
3. **No standardized perioperative/obstetric guidelines.** Management in pregnancy and surgery is based on small case series and expert opinion, not trials.
4. **Thrombosis meta-analysis borderline.** Although the adjusted OR is ~1.0, the unadjusted pooled RR (1.34, CI 0.99–1.81) sits at the edge of significance, reflecting residual confounding and heterogeneity across studies.
5. **Genotype–phenotype quantitation.** Precise mapping of specific *F12* variants to FXII:C/FXII:Ag levels (CRM+ vs CRM−) and the modifying effect of 46C>T is incompletely catalogued.

---

## Proposed Follow-up Experiments / Actions

1. **Harmonized international *F12* variant registry** linking genotype (including 46C>T status) to FXII:C, FXII:Ag, and CRM classification, to resolve genotype–phenotype relationships.
2. **Prospective, adequately powered cohort** assessing thrombosis and pregnancy outcomes in genetically confirmed severe deficiency, with mandatory anti-FXII antibody and antiphospholipid testing to separate congenital from acquired low FXII.
3. **Functional reclassification pipeline** (HEK293T/CHO secretion assays + autoactivation kinetics, as in [PMID: 41811038](https://pubmed.ncbi.nlm.nih.gov/41811038/)) to resolve VUS and distinguish loss- vs gain-of-function *F12* variants.
4. **Clinical-education intervention study** quantifying (and reducing) iatrogenic harm—unnecessary FFP, surgical delay, heparin-monitoring errors—triggered by isolated prolonged aPTT.
5. **Translational extension of garadacimab**: given the deficiency's safety, evaluate FXIIa inhibition in thrombosis, stroke, and extracorporeal circulation (dialysis, ECMO, cardiopulmonary bypass), where the congenital-deficiency phenotype predicts antithrombotic benefit without bleeding.

---

*Report compiled from a 5-iteration autonomous investigation: 12 confirmed findings, 47 papers reviewed. Evidence spans human clinical, model-organism (mouse, cat), in vitro, and computational/evolutionary sources.*


## Artifacts

- [OpenScientist final report](Congenital_Factor_XII_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Factor_XII_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 40 |
| On topic | 24 |
| Off topic | 3 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41499201` *(abstract only)*: "prophylaxis of HAE attacks in patients aged ≥12 years"
  - closest text in source: "OBJECTIVE: To describe garadacimab-gxii, an antibody that inhibits factor XII, indicated for hereditary angioedema (HAE) prophylaxis, approved by the Food and Drug Administration in June 2025 for patients 12 years and older"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42433832` (10 mentions) - Garadacimab and the future of hereditary angioedema prophylaxis: a step upstream in the bradykinin pathway.
  - shared terms: xii
- `PMID:41499201` (4 mentions) - Garadacimab-gxii-A Novel Prophylactic Treatment for Hereditary Angioedema: A Drug Review.
  - shared terms: xii, reduced
- `PMID:42268494` (6 mentions) - Long-Term Integrated Safety and Efficacy of Garadacimab for Hereditary Angioedema Prophylaxis.
  - shared terms: xii

Weighed against this report's own most characteristic terms: `fxii`, `deficiency`, `congenital`, `prolonged`, `disease`, `f12`, `aptt`, `variant`, `cohort`, `bleeding`, `normal`, `plasma`, `thrombosis`, `phenotype`, `benign`, `activity`, `xii`, `reduced`, `pregnancy`, `gene`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 17 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 8 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003005` (1 mention) - the report calls it "Abnormal coagulation factor activity"; HP calls it **Ganglioneuroma**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.