---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T15:20:21.016955'
end_time: '2026-09-25T15:35:33.724675'
duration_seconds: 912.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Klebsiella Pneumonia
  mondo_id: MONDO:0030602
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
citation_count: 37
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 37
  on_topic: 18
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 30
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 14
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: UBERON:0002048
    reported_labels:
    - lung
    - Primary organs:** **lung
    ontology_label: lung
  - term_id: UBERON:0002107
    reported_labels:
    - liver
    - hvKp target organs:** **liver
    ontology_label: liver
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Klebsiella_Pneumonia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Klebsiella_Pneumonia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Klebsiella Pneumonia
- **MONDO ID:** MONDO:0030602 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Klebsiella Pneumonia** covering all of the
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

# Klebsiella Pneumonia — Comprehensive Disease Characteristics Report

**Disease:** Klebsiella pneumonia (infection caused by *Klebsiella pneumoniae*)
**MONDO ID:** MONDO:0030602 · **Pathogen taxonomy:** NCBI:txid573 · **Category:** Infectious Disease
**Report type:** Multi-iteration autonomous literature synthesis (10 confirmed findings; 46 papers reviewed)

---

## Summary

Klebsiella pneumonia is an acute bacterial infection caused by the encapsulated, non-motile, Gram-negative
rod *Klebsiella pneumoniae*, a member of the *Enterobacteriaceae*. Clinically the disease is not a single
entity but a spectrum: lobar/nosocomial pneumonia, ventilator-associated pneumonia, bloodstream infection
(bacteremia/sepsis), urinary tract infection, and — for a distinct **hypervirulent** pathotype — community-acquired
pyogenic liver abscess with metastatic spread. *K. pneumoniae* is one of the **ESKAPE** organisms and a **WHO
critical-priority** antimicrobial-resistance (AMR) pathogen, making it a central actor in the global AMR crisis
[PMID: 42178970](https://pubmed.ncbi.nlm.nih.gov/42178970/). Unlike the Mendelian disorders this template was
designed around, Klebsiella pneumonia is an **infectious, non-heritable disease**: its "causal genes" are bacterial
virulence and resistance genes, not human germline variants, and host genetic susceptibility loci are minor
relative to healthcare exposures.

The investigation converged on a **two-pathotype model**. **Classical *K. pneumoniae* (cKp)** is an opportunistic
nosocomial pathogen that infects debilitated, catheterized, ventilated, or antibiotic-exposed patients and is the
leading cause of neonatal sepsis in low- and middle-income countries (LMICs); much of its burden is driven by
in-hospital transmission [PMID: 42127138](https://pubmed.ncbi.nlm.nih.gov/42127138/). Its danger lies in
**carbapenem resistance** mediated by KPC, NDM, and OXA-48 carbapenemases, which pushes in-hospital mortality of
bloodstream infection to 30–50% [PMID: 42734011](https://pubmed.ncbi.nlm.nih.gov/42734011/),
[PMID: 42518856](https://pubmed.ncbi.nlm.nih.gov/42518856/). **Hypervirulent *K. pneumoniae* (hvKp)** infects
younger, immunocompetent hosts in the community, causing invasive liver abscess through K1/K2 capsule serotypes,
*rmpADC*-driven hypermucoviscosity, and multiple siderophore systems
[PMID: 42021129](https://pubmed.ncbi.nlm.nih.gov/42021129/). The two pathotypes are converging on mobile plasmids
(e.g., ST11 KPC-2 hvKp), an emerging worst-case threat that fuses resistance with virulence
[PMID: 32576652](https://pubmed.ncbi.nlm.nih.gov/32576652/).

Mechanistically, pathogenesis runs from **gut/mucosal colonization → barrier breach → capsule- and
siderophore-mediated immune evasion → TLR4- and NLRC4-inflammasome-driven neutrophil/macrophage recruitment →
either clearance or, when immunity fails or the organism is resistant, invasive infection, sepsis, and death**
[PMID: 22547706](https://pubmed.ncbi.nlm.nih.gov/22547706/),
[PMID: 36018281](https://pubmed.ncbi.nlm.nih.gov/36018281/). Diagnosis rests on culture with MALDI-TOF species
identification plus molecular/phenotypic resistance detection; treatment is susceptibility-guided, favoring newer
β-lactam/β-lactamase-inhibitor combinations (ceftazidime-avibactam, meropenem-vaborbactam, imipenem-relebactam)
and cefiderocol for metallo-β-lactamase producers; and prevention hinges on antibiotic stewardship and infection
control, because no vaccine is yet licensed.

---

## 1. Disease Information

**Overview.** Klebsiella pneumonia is infection by *Klebsiella pneumoniae*, historically described by Carl
Friedländer (hence "Friedländer's bacillus" / "Friedländer's pneumonia") as a cause of severe lobar pneumonia
classically producing thick, blood-tinged "currant-jelly" sputum. Modern disease is dominated by
**healthcare-associated** presentations — hospital-acquired and ventilator-associated pneumonia, catheter-associated
UTI, and central-line bloodstream infection — plus **community-acquired invasive syndromes** driven by the
hypervirulent pathotype.

**Key identifiers.**
- **MONDO:** MONDO:0030602 (Klebsiella pneumonia)
- **Pathogen (NCBI Taxonomy):** *Klebsiella pneumoniae* txid573
- **MeSH:** *Klebsiella Infections* (D007710); *Pneumonia, Bacterial*
- **ICD-10:** J15.0 (Pneumonia due to *Klebsiella pneumoniae*); A49.8/B96.1 (*Klebsiella* as cause of disease classified elsewhere)
- **ICD-11:** CA40 (bacterial pneumonia) with pathogen extension; infection codes under 1B/1C
- **OMIM / Orphanet:** Not applicable — this is an acquired infectious disease, not a Mendelian disorder. There is no OMIM phenotype entry; Orphanet does not list it as a rare genetic disease.

**Synonyms / alternative names.** Friedländer's pneumonia; Friedländer's bacillus infection; *Klebsiella pneumoniae*
infection; Klebsiella infection (when generalized); (for the invasive pathotype) hypervirulent *Klebsiella pneumoniae*
infection / invasive Klebsiella syndrome.

**Data source type.** The evidence base is overwhelmingly **aggregated disease-level** — surveillance cohorts,
genomic epidemiology, meta-analyses, and clinical guidelines — supplemented by individual case reports/series for
the hypervirulent syndrome. It is not derived from a single-patient EHR data file.

---

## 2. Etiology

**Primary cause — infectious.** The disease is caused by infection with *K. pneumoniae*. There is **no human
germline genetic cause**. Two ecological/virulence pathotypes drive distinct etiologies:

| Feature | Classical (cKp) | Hypervirulent (hvKp) |
|---|---|---|
| Typical host | Debilitated, hospitalized, immunocompromised | Younger, often immunocompetent |
| Setting | Nosocomial | Community-acquired |
| Hallmark syndrome | HAP/VAP, BSI, UTI, neonatal sepsis | Pyogenic liver abscess, metastatic (endophthalmitis, meningitis) |
| Key genetics | Carbapenemases (KPC/NDM/OXA-48) | K1/K2 capsule, *rmpADC*, aerobactin/salmochelin/yersiniabactin |
| Mortality driver | Antibiotic resistance | Dissemination/metastasis |

**Risk factors (host/environmental — quantified).** A meta-analysis of 30 studies (5,075 cases) established that
carbapenem-resistant *K. pneumoniae* (CRKP) infection is driven by **healthcare exposures and prior antibiotics,
not host demographics** [PMID: 31525540](https://pubmed.ncbi.nlm.nih.gov/31525540/):

| Risk factor | Odds ratio (95% CI) |
|---|---|
| Carbapenem exposure | 3.99 (2.86–5.56) |
| ICU admission | 3.25 (2.36–4.47) |
| Glycopeptide exposure | 3.08 (1.93–4.91) |
| Central venous catheterization | 2.93 (2.00–4.28) |
| Mechanical ventilation | 2.91 (1.96–4.31) |
| Indwelling (urinary) catheter | 2.62 (1.65–4.17) |
| Any prior antibiotic exposure | 2.53 (1.56–4.11) |
| Nasogastric intubation | 2.38 (1.22–4.62) |
| β-lactam/β-lactamase-inhibitor exposure | 2.28 (1.37–3.80) |
| Quinolone exposure | 1.75 (1.38–2.22) |
| Surgery | 1.59 (1.08–2.34) |
| Immunosuppression | 1.47 (1.14–1.90) |

Notably, **age, sex, and diabetes mellitus were NOT associated** with CRKP infection in this meta-analysis (a
useful negative finding) — although diabetes is a well-recognized risk factor specifically for **hvKp liver abscess**
in the Asian literature. Additional exposure-based risks include prolonged mechanical ventilation and prolonged
ECMO support, where prior antibiotic use before ECMO (RR 1.25) and longer ventilation (RR 1.31) independently
predicted healthcare-associated infection [PMID: 42685911](https://pubmed.ncbi.nlm.nih.gov/42685911/).

**Genetic risk factors (human).** No robust, replicated human susceptibility loci for *K. pneumoniae* disease were
identified in this investigation. Innate-immune pathway integrity (TLR4, NLRC4/inflammasome, IL-1β signaling) is
mechanistically protective in models, implying that host defects in these pathways would increase susceptibility,
but this remains inferred rather than demonstrated in human genetic association studies.

**Protective factors.** Intact mucosal barriers, a diverse gut microbiome that resists colonization by
multidrug-resistant Enterobacterales, and competent innate immunity are protective. Gut microbiome composition
modulates intestinal colonization by MDR Enterobacterales
[PMID: 41009869](https://pubmed.ncbi.nlm.nih.gov/41009869/),
[PMID: 38659243](https://pubmed.ncbi.nlm.nih.gov/38659243/) — implying microbiome preservation (avoiding
unnecessary broad-spectrum antibiotics) is protective. No validated protective human genetic variant was found.

**Gene–environment interaction.** The dominant interaction is **antibiotic exposure × bacterial resistance
genotype**: antibiotic pressure selects for carbapenemase-carrying clones in the gut reservoir, which then cause
endogenous infection or spread nosocomially. This is an environment-(bacterial)genotype interaction rather than a
human GxE effect.

---

## 3. Phenotypes

Phenotypes are clinical manifestations of infection, varying by syndrome. Onset is typically **acute**;
severity ranges **moderate to severe**; frequency figures are syndrome-dependent.

| Phenotype | Type | Syndrome | Suggested HPO term |
|---|---|---|---|
| Pneumonia / productive cough | Clinical sign | HAP/VAP, CAP | HP:0002090 (Pneumonia); HP:0031246 (Productive cough) |
| Fever | Symptom | All | HP:0001945 (Fever) |
| Dyspnea | Symptom | Pneumonia, sepsis | HP:0002094 (Dyspnea) |
| "Currant-jelly" / bloody sputum | Clinical sign | Friedländer pneumonia | HP:0002105 (Hemoptysis) |
| Sepsis / septic shock | Clinical sign | BSI | HP:0100806 (Sepsis) |
| Bacteremia | Laboratory | BSI | HP:0031864 (Bacteremia)* |
| Liver abscess | Physical/imaging | hvKp | HP:0100523 (Hepatic abscess)* |
| Leukocytosis | Laboratory | All | HP:0001974 (Leukocytosis) |
| Elevated D-dimer / coagulopathy | Laboratory | Severe BSI | HP:0003581-adjacent (coagulation abnormality) |
| Urinary tract infection | Clinical sign | Catheter-associated | HP:0000010 (Recurrent UTI) |
| Neonatal sepsis | Clinical sign | LMIC neonates | HP:0001945 + neonatal onset |
| Metastatic endophthalmitis / meningitis | Clinical sign | hvKp dissemination | HP:0000623 / HP:0001287 |

\*Term suggestions; verify exact HPO ID before ingestion.

**Age of onset.** Bimodal — **neonatal** (LMIC sepsis) and **older adults** (nosocomial; mean age ≈66 years,
male predominance ≈70% in BSI cohorts). hvKp liver abscess tends to occur in middle-aged adults.

**Quality-of-life impact.** Severe infection causes ICU-level morbidity, prolonged hospitalization, and
long-term functional impairment in survivors of sepsis; disease-specific QoL instruments were not identified in
the literature reviewed.

---

## 4. Genetic / Molecular Information (bacterial)

Because this is an infectious disease, the relevant genetics are the **pathogen's virulence and resistance
determinants**, not human variants.

**Resistance genes (carbapenemases).** Carbapenem resistance is mediated chiefly by three carbapenemase families
[PMID: 42734011](https://pubmed.ncbi.nlm.nih.gov/42734011/),
[PMID: 42439974](https://pubmed.ncbi.nlm.nih.gov/42439974/):
- **KPC** (*bla*KPC; class A) — dominant in many regions; 88.9% (48/54) of CRKP BSI isolates in a Chinese cohort.
- **NDM** (*bla*NDM; class B metallo-β-lactamase) — 7.4% in the same cohort; alters therapy because MBLs hydrolyze most β-lactams and are not inhibited by avibactam/vaborbactam.
- **OXA-48** (*bla*OXA-48; class D) — predominant (50.4%) in a southern Saudi Arabia CRE cohort, illustrating strong geographic variation.
Additional/associated genes: *bla*VIM (MBL), *bla*SHV and *bla*CTX-M (ESBLs).

**Virulence genes.** In CRKP BSI, virulence genes *ycfM*, *wabG*, and *entB* were present in **all** strains;
*fimH* 98.15%, *mrkD* 96.30%, *uge* 92.60%, *kpn* 92.60% [PMID: 42734011](https://pubmed.ncbi.nlm.nih.gov/42734011/).
For **hvKp**, the defining loci are the **capsular polysaccharide serotypes K1/K2**, the **regulator of
mucoid phenotype** operon ***rmpADC*** (drives hypermucoviscosity), and multiple **siderophore** systems —
**aerobactin**, **salmochelin** (*iroBCDN*), and **yersiniabactin** (*ybt*) — frequently carried on large
virulence plasmids. A characterized ST111 hvKp isolate harbored a **181 kb IncHI1B/IncFIB virulence plasmid**
encoding *rmpADC* and salmochelin (*iroBCDN*) plus yersiniabactin; CRISPR/Cas9 plasmid curing followed by murine
infection **confirmed the plasmid's causal contribution** to hypervirulence
[PMID: 42021129](https://pubmed.ncbi.nlm.nih.gov/42021129/).

**Lineages (multilocus sequence types).** hvKp liver abscess is canonically linked to **ST23, ST65, ST86**;
convergent resistance-plus-virulence clones include **ST11** (KPC-2-producing hvKp).

**Epigenetics / chromosomal abnormalities / human modifier genes.** Not applicable to this infectious disease.
(Bacterial DNA methylation/restriction-modification systems exist but are not disease-defining here.)

---

## 5. Environmental Information

**Infectious agent.** *Klebsiella pneumoniae* (NCBI:txid573), Gram-negative, encapsulated, non-motile,
lactose-fermenting, oxidase-negative rod of the *Enterobacteriaceae*.

**Environmental reservoirs & transmission.** The **gastrointestinal tract is the principal reservoir**;
the organism also colonizes the oropharynx and skin, and persists on hospital surfaces and medical devices,
enabling patient-to-patient nosocomial transmission via healthcare-worker hands and equipment. Genomic clustering
of neonatal isolates across 27 units in 13 countries confirmed extensive nosocomial spread
[PMID: 42127138](https://pubmed.ncbi.nlm.nih.gov/42127138/).

**Lifestyle / host-environment factors.** Alcohol use and diabetes are associated with invasive hvKp disease in
Asian populations; broad-spectrum antibiotic exposure is the dominant modifiable environmental driver of resistant
infection (see Section 2). Timor-Leste and Ethiopian surveillance underscore that third-generation cephalosporin
and emerging carbapenem resistance are widespread, particularly in LMIC settings
[PMID: 42662930](https://pubmed.ncbi.nlm.nih.gov/42662930/),
[PMID: 42594141](https://pubmed.ncbi.nlm.nih.gov/42594141/).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating event → clinical manifestation)

1. **Gut/mucosal colonization** by *K. pneumoniae* (often a resistant or hypervirulent clone selected by prior antibiotics) **establishes a reservoir** in the GI tract [PMID: 32576652](https://pubmed.ncbi.nlm.nih.gov/32576652/), [PMID: 42127138](https://pubmed.ncbi.nlm.nih.gov/42127138/).
2. **Barrier breach** — via micro-aspiration into the lung, a urinary/vascular catheter, surgery, or translocation across a compromised gut epithelium — **allows the organism to reach a normally sterile site** (*inferred from reservoir + device risk-factor data*).
3. At the tissue site, the **polysaccharide capsule and hypermucoviscosity (hvKp: K1/K2, *rmpADC*) resist phagocytosis and complement**, while **siderophores (aerobactin, salmochelin, yersiniabactin) scavenge host iron**, **enabling bacterial survival and replication** [PMID: 42021129](https://pubmed.ncbi.nlm.nih.gov/42021129/).
4. Bacterial ligands (LPS) **engage TLR4 on epithelium/macrophages**, which **triggers NF-κB signaling and cytokine/chemokine release (KC, MIP-2, LIX)**, **recruiting neutrophils and monocytes/macrophages** to the lung [PMID: 36018281](https://pubmed.ncbi.nlm.nih.gov/36018281/).
5. In parallel, the **NLRC4 inflammasome senses the organism and drives IL-1β (and IL-17A) production**, which **is essential for neutrophil-mediated clearance and host survival** [PMID: 22547706](https://pubmed.ncbi.nlm.nih.gov/22547706/).
6. **Branch A — effective immunity:** neutrophil/macrophage phagocytosis and inflammasome/IL-1β signaling **clear the infection → recovery.**
7. **Branch B — failed immunity or antibiotic-resistant organism:** the bacterium **evades clearance and disseminates into blood → bacteremia/sepsis**, activating coagulation (elevated D-dimer) and causing **organ dysfunction and death (30–50% in resistant BSI)** [PMID: 42518856](https://pubmed.ncbi.nlm.nih.gov/42518856/), [PMID: 42734011](https://pubmed.ncbi.nlm.nih.gov/42734011/).
8. **Branch C — hypervirulent dissemination:** hvKp seeds the **liver (pyogenic abscess)** and metastasizes to **eye (endophthalmitis), meninges, lung**, producing invasive syndrome even in immunocompetent hosts [PMID: 41356976](https://pubmed.ncbi.nlm.nih.gov/41356976/).

### Detail by category

- **Molecular pathways:** TLR4 → MyD88 → NF-κB (pro-inflammatory transcription); NLRC4 inflammasome → caspase-1 → IL-1β/IL-18 maturation.
- **Cellular processes:** acute inflammation, neutrophil chemotaxis and phagocytosis, macrophage activation, pyroptosis (inflammasome-linked cell death).
- **Immune involvement:** innate immunity is decisive; NLRC4-derived **IL-1β specifically** (not IL-18 or IL-17A) partially rescued survival and neutrophil accumulation in NLRC4−/− mice [PMID: 22547706](https://pubmed.ncbi.nlm.nih.gov/22547706/). TLR4-agonist (3D-PHAD) pretreatment increased phagocytic innate cells, reduced lung CFU, and improved survival [PMID: 36018281](https://pubmed.ncbi.nlm.nih.gov/36018281/).
- **Bacterial "protein dysfunction":** capsule and siderophore systems are gain-of-virulence; carbapenemases are enzymatic drug-inactivation.
- **Tissue damage:** neutrophilic inflammation, abscess/necrosis (liver in hvKp), and sepsis-associated microvascular injury/coagulopathy.

**Suggested ontology terms.** GO:0006954 (inflammatory response); GO:0002224/GO:0038123 (toll-like receptor signaling); GO:0072559 (NLRP/NLRC4-type inflammasome complex — verify exact ID); GO:0006935 (chemotaxis); GO:0006909 (phagocytosis). **Cell types (CL):** CL:0000775 (neutrophil), CL:0000235 (macrophage), CL:0000583 (alveolar macrophage), CL:0000066 (epithelial cell). **Anatomy (UBERON):** UBERON:0002048 (lung), UBERON:0002107 (liver), UBERON:0000178 (blood).

---

## 7. Anatomical Structures Affected

- **Primary organs:** **lung** (UBERON:0002048) — pneumonia; **blood** (UBERON:0000178) — bacteremia; **urinary tract/bladder** (UBERON:0001255) — UTI.
- **hvKp target organs:** **liver** (UBERON:0002107) — pyogenic abscess; with metastasis to **eye** (UBERON:0000970, endophthalmitis) and **meninges/CNS** (UBERON:0002360, meningitis).
- **Body systems:** respiratory, cardiovascular (sepsis), hepatobiliary, urinary, and (neonatal) systemic.
- **Tissues/cells:** respiratory and urinary **epithelium** (adhesion via type 1/type 3 fimbriae *fimH*/*mrkD*); recruited **neutrophils** (CL:0000775) and **macrophages/alveolar macrophages** (CL:0000235/CL:0000583).
- **Subcellular compartments (host innate response):** cytosolic inflammasome complex, plasma-membrane TLR4 receptor; (bacterial) outer-membrane capsule and LPS.
- **Lateralization:** pneumonia may be lobar (classically upper-lobe in Friedländer pneumonia) or bilateral; liver abscess is often solitary right-lobe.

---

## 8. Temporal Development

- **Onset:** typically **acute** (hours–days). Neonatal sepsis presents early/late neonatal period; nosocomial pneumonia after device exposure/ICU stay.
- **Progression:** can be **rapid**, progressing to sepsis and septic shock, particularly with resistant organisms or delayed effective therapy. hvKp abscess may be subacute but disseminate.
- **Course:** acute and, with treatment, often self-limited to the treatment course; complicated/resistant infections have prolonged courses. Not relapsing-remitting or chronic in the Mendelian sense.
- **Critical intervention window:** early appropriate (susceptibility-matched) antimicrobial therapy is the key modifiable determinant of survival; delays worsen outcome. Faster microbiological clearance with ceftazidime-avibactam (HR 2.475; 95% CI 1.493–4.102) underscores the value of rapid, correct therapy [PMID: 42708480](https://pubmed.ncbi.nlm.nih.gov/42708480/).

---

## 9. Inheritance and Population

**Inheritance.** Not applicable — infectious, non-heritable. No AD/AR/X-linked pattern; no penetrance/expressivity/
anticipation/founder-effect/consanguinity considerations for the human host.

**Epidemiology.**
- *K. pneumoniae* is the **leading cause of neonatal sepsis in LMICs** in Africa and Asia; in a genomic study of
1,523 isolates from 27 neonatal units across 13 countries, an estimated **68.0% (1,035/1,523) of neonatal
infections were part of nosocomial transmission clusters**, with ≥57.7% (879) acquired via nosocomial
transmission [PMID: 42127138](https://pubmed.ncbi.nlm.nih.gov/42127138/).
- In ICU/ECMO cohorts, *K. pneumoniae* is repeatedly among the top VAP/HAP pathogens; VAP reached 31.1 cases/1,000
ECMO-days [PMID: 42685911](https://pubmed.ncbi.nlm.nih.gov/42685911/).
- CRKP bloodstream infection incidence was ~2.2/100,000 patient-days in one Chinese study
[PMID: 42734011](https://pubmed.ncbi.nlm.nih.gov/42734011/).

**Demographics.** BSI cohorts show **male predominance (~67–70%)** and **older age (mean ≈64–66 years)**
[PMID: 42518856](https://pubmed.ncbi.nlm.nih.gov/42518856/),
[PMID: 42563676](https://pubmed.ncbi.nlm.nih.gov/42563676/). Geographic variation in carbapenemase type is
pronounced: KPC-dominant in East Asia/parts of the Americas, OXA-48-dominant in the Middle East/Mediterranean,
NDM widespread in South Asia. hvKp invasive liver-abscess syndrome is most reported in East/Southeast Asia.

---

## 10. Diagnostics

**Culture + identification.** The reference approach is **culture with MALDI-TOF MS identification** plus
**molecular/phenotypic resistance detection**. MALDI-TOF correctly identified **174/174** *K. pneumoniae* isolates
with log score >2.0, 100% concordant with reference systems
[PMID: 27239799](https://pubmed.ncbi.nlm.nih.gov/27239799/).

**Rapid molecular panels.** BioFire FilmArray Blood Culture Identification from positive blood cultures showed
**94% concordance** with MALDI Biotyper and detects *bla*KPC
[PMID: 32305272](https://pubmed.ncbi.nlm.nih.gov/32305272/).

**Resistance detection.** PCR/WGS identify carbapenemase genes (*bla*KPC, *bla*NDM, *bla*OXA-48, *bla*VIM);
phenotypic tests include the modified Carbapenem Inactivation Method (mCIM). The **MALDIxin test** detects lipid A
modifications (L-Ara4N/pEtN) underlying **colistin resistance in <30 min** and distinguishes chromosomal vs
MCR-mediated resistance [PMID: 31580426](https://pubmed.ncbi.nlm.nih.gov/31580426/). Strain typing (rep-PCR,
WGS/MLST) supports outbreak investigation [PMID: 21568752](https://pubmed.ncbi.nlm.nih.gov/21568752/).

**Biomarkers / labs.** Leukocytosis, elevated CRP/procalcitonin; **elevated D-dimer** is an independent prognostic
marker in BSI (see Section 11). Imaging: chest radiograph/CT for pneumonia (classic bulging-fissure lobar
consolidation); abdominal CT/ultrasound for hvKp liver abscess.

**Differential diagnosis.** Other Gram-negative pneumonias/BSI (*E. coli*, *Pseudomonas aeruginosa*,
*Acinetobacter baumannii*, *Serratia*), *S. aureus* pneumonia, and other causes of liver abscess (*E. coli*,
anaerobes, amebic abscess).

---

## 11. Outcome / Prognosis

**Mortality is high**, especially for resistant bloodstream infection.

| Outcome metric | Value | Source |
|---|---|---|
| In-hospital mortality, KP BSI (n=222) | **47.7% (106/222)** | [PMID: 42518856](https://pubmed.ncbi.nlm.nih.gov/42518856/) |
| 28-day mortality, BSI in acute-on-chronic liver failure | 49.1% | [PMID: 42717128](https://pubmed.ncbi.nlm.nih.gov/42717128/) |
| Donor-derived / hospital-acquired pneumonia in lung transplant | 50% | [PMID: 42781399](https://pubmed.ncbi.nlm.nih.gov/42781399/) |

**Prognostic factors.** Independent predictors and correlates of death include **elevated D-dimer** (adjusted
HR 1.04 per unit, 95% CI 1.03–1.07; high vs low group HR 2.14, 95% CI 1.27–3.59)
[PMID: 42518856](https://pubmed.ncbi.nlm.nih.gov/42518856/); **capsular type K47/K64 and KPC-plasmid features**
in CRKP bacteraemia [PMID: 42216056](https://pubmed.ncbi.nlm.nih.gov/42216056/); disease severity scores
(MELD, Pitt bacteremia score, APACHE II); and **choice of therapy** — non-polymyxin regimens achieved higher
clinical cure than polymyxin-based therapy in CRKP bacteraemia (**58.4% vs 15.4%; p=0.02**)
[PMID: 42455851](https://pubmed.ncbi.nlm.nih.gov/42455851/).

**Complications.** Septic shock, multi-organ failure, DIC/coagulopathy; for hvKp, metastatic endophthalmitis,
meningitis, and septic emboli. Recovery is achievable with early appropriate therapy but is compromised by
resistance and host frailty.

---

## 12. Treatment

**Susceptibility-guided antibiotic therapy is the cornerstone.** For **non-metallo-β-lactamase CRE**, IDSA 2022
guidance and the German MDRO guideline recommend **ceftazidime-avibactam, meropenem-vaborbactam, and
imipenem-relebactam** as first-choice agents; **metallo-β-lactamase (e.g., NDM) production must be detected or
excluded** because it changes therapy to **cefiderocol** or **ceftazidime-avibactam plus aztreonam**
[PMID: 35439291](https://pubmed.ncbi.nlm.nih.gov/35439291/),
[PMID: 42661422](https://pubmed.ncbi.nlm.nih.gov/42661422/).

| Scenario | Preferred therapy | NCIT-type intervention |
|---|---|---|
| Susceptible *K. pneumoniae* | β-lactam per susceptibility (e.g., ceftriaxone) | Cephalosporin therapy |
| ESBL producer | Carbapenem | Carbapenem therapy |
| CRE (non-MBL: KPC/OXA-48) | Ceftazidime-avibactam, meropenem-vaborbactam, imipenem-relebactam | β-lactam/β-lactamase-inhibitor therapy |
| MBL (NDM/VIM) | Cefiderocol, or ceftazidime-avibactam + aztreonam | Siderophore-cephalosporin therapy |
| Adjunct / renal-sparing | IV fosfomycin-containing regimens | Fosfomycin therapy |

**Ceftazidime-avibactam** produced faster microbiological clearance than alternatives
[PMID: 42708480](https://pubmed.ncbi.nlm.nih.gov/42708480/). **IV fosfomycin** combination regimens achieved
79.4% clinical success and were associated with **reduced acute kidney injury** versus colistin-heavy regimens
[PMID: 42599357](https://pubmed.ncbi.nlm.nih.gov/42599357/),
[PMID: 42482780](https://pubmed.ncbi.nlm.nih.gov/42482780/). **Colistin/polymyxins** are now later-line owing to
nephrotoxicity and inferior cure rates [PMID: 42455851](https://pubmed.ncbi.nlm.nih.gov/42455851/).

**Source control** (drainage of liver abscess/empyema, removal of infected catheters/lines) is essential,
particularly for hvKp.

**Adjunctive/experimental.** In a murine model, **atorvastatin added to imipenem** provided additional benefit
in Gram-negative pneumonia [PMID: 29463546](https://pubmed.ncbi.nlm.nih.gov/29463546/); immunomodulation of the
ICOS pathway influenced airway-pathogen pathogenesis [PMID: 29378030](https://pubmed.ncbi.nlm.nih.gov/29378030/).
TLR4-agonist innate stimulation was protective in mice [PMID: 36018281](https://pubmed.ncbi.nlm.nih.gov/36018281/).
These are pre-clinical.

---

## 13. Prevention

**Primary prevention.** Antibiotic **stewardship** (limiting carbapenem/glycopeptide/quinolone pressure — the
strongest modifiable risk factors, Section 2) and **infection prevention and control**: hand hygiene, contact
precautions, device-care bundles (ventilator, central-line, urinary-catheter), and environmental cleaning to
interrupt nosocomial transmission [PMID: 42127138](https://pubmed.ncbi.nlm.nih.gov/42127138/),
[PMID: 42685911](https://pubmed.ncbi.nlm.nih.gov/42685911/).

**Secondary prevention.** Active surveillance cultures / rectal screening for CRKP carriage in high-risk units;
early detection of carbapenemase producers enables cohorting and rapid appropriate therapy.

**Vaccines (investigational).** **No licensed *Klebsiella* vaccine exists.** Candidates target capsular
polysaccharides, O-antigen (LPS), and the **MrkA** type-3 fimbrial subunit. A **pVAX1-MrkA DNA vaccine protected
80% of mice against sepsis (p=0.0373)**, identifying MrkA as a lead antigen
[PMID: 42634491](https://pubmed.ncbi.nlm.nih.gov/42634491/); reverse-vaccinology antigen discovery is ongoing
[PMID: 42511741](https://pubmed.ncbi.nlm.nih.gov/42511741/),
[PMID: 42453653](https://pubmed.ncbi.nlm.nih.gov/42453653/).

**Microbiome-based prevention (emerging).** Because the gut is the reservoir, strategies preserving/restoring a
colonization-resistant microbiome are under investigation
[PMID: 41009869](https://pubmed.ncbi.nlm.nih.gov/41009869/).

---

## 14. Other Species / Natural Disease

- **Taxonomy of pathogen:** *Klebsiella pneumoniae* (NCBI:txid573); related species *K. oxytoca*, *K. variicola*,
*K. aerogenes*.
- **Host range:** broad — *K. pneumoniae* naturally infects humans and many animals (cattle mastitis, equine and
companion-animal infections, primates, wildlife) and colonizes environmental niches (water, soil, plants). It is
an important **One Health** organism, with resistance genes shared across human, animal, agricultural, and
environmental compartments [PMID: 42568440](https://pubmed.ncbi.nlm.nih.gov/42568440/).
- **Zoonotic/cross-species transmission:** plausible via the environment and food chain; direct zoonosis is less
defined than the environmental resistance-gene flow. No single human ortholog gene is relevant (infectious disease).

---

## 15. Model Organisms

- **Mouse (murine) models** are the primary system for pathogenesis and immunity: pulmonary infection models
demonstrated the essential role of **NLRC4/IL-1β** [PMID: 22547706](https://pubmed.ncbi.nlm.nih.gov/22547706/)
and **TLR4-agonist protection** [PMID: 36018281](https://pubmed.ncbi.nlm.nih.gov/36018281/); sepsis models
validated the **MrkA DNA vaccine** [PMID: 42634491](https://pubmed.ncbi.nlm.nih.gov/42634491/) and
**atorvastatin+imipenem** adjunctive therapy [PMID: 29463546](https://pubmed.ncbi.nlm.nih.gov/29463546/).
- **Genetic host models:** knockout mice (e.g., *Nlrc4−/−*, *Icos−/−*) dissect host-defense pathways
[PMID: 29378030](https://pubmed.ncbi.nlm.nih.gov/29378030/).
- **Bacterial genetic tools:** CRISPR/Cas9 plasmid curing established causality of the hvKp virulence plasmid
[PMID: 42021129](https://pubmed.ncbi.nlm.nih.gov/42021129/).
- **Phenotype recapitulation:** murine pneumonia/sepsis models reproduce neutrophilic lung inflammation,
bacteremia, and (for hvKp) dissemination, and predict vaccine/therapy efficacy. **Limitations:** mouse innate
immunity and microbiome differ from humans; models may not capture chronic colonization dynamics, human
device-associated disease, or the full breadth of resistance-plasmid ecology. General animal-model reviews are
available [PMID: 38559342](https://pubmed.ncbi.nlm.nih.gov/38559342/).

---

## Mechanistic Model / Interpretation

```
                    ┌─────────────────────────────────────────────────────────┐
                    │  ANTIBIOTIC PRESSURE (carbapenem OR≈4.0, ICU, catheters) │
                    └───────────────────────────┬─────────────────────────────┘
                                                 ▼
   GUT / MUCOSAL RESERVOIR  ──(prior antibiotics select resistant/hvKp clones)──►  colonization
                                                 │
                             barrier breach (aspiration, catheter, surgery, translocation)
                                                 ▼
                           BACTERIUM AT STERILE SITE (lung / blood / liver / urine)
                                                 │
            ┌───────────────── capsule (K1/K2) + rmpADC + siderophores ──────────────────┐
            │                  resist phagocytosis/complement; scavenge iron              │
            ▼                                                                             ▼
   HOST INNATE SENSING:  TLR4→NF-κB  +  NLRC4 inflammasome→caspase-1→IL-1β
            │
            ▼
   NEUTROPHIL + MACROPHAGE recruitment & phagocytosis
            │
   ┌────────┴─────────┬──────────────────────────────┐
   ▼                  ▼                              ▼
 CLEARANCE       FAILED IMMUNITY / RESISTANCE     HYPERVIRULENT DISSEMINATION
 (recovery)      → bacteremia → SEPSIS            → liver abscess → metastasis
                 → coagulopathy (↑D-dimer)          (eye, meninges, lung)
                 → 30–50% MORTALITY
```

The unifying insight is that **two epidemiologically distinct pathotypes share a common virulence toolkit**
(capsule + siderophores) and a **common gut reservoir**, but differ in their principal threat: cKp weaponizes
**antibiotic resistance** against debilitated hosts, whereas hvKp weaponizes **capsule-based hypervirulence**
against healthy hosts. Their **convergence on mobile plasmids** (resistant *and* hypervirulent, e.g., ST11 KPC-2
hvKp) is the field's chief emerging concern.

---

## Evidence Base

| PMID | Contribution | Role |
|---|---|---|
| [42127138](https://pubmed.ncbi.nlm.nih.gov/42127138/) | Neonatal sepsis, 68% nosocomial clusters across 13 countries | Establishes burden & nosocomial transmission |
| [42734011](https://pubmed.ncbi.nlm.nih.gov/42734011/) | KPC 88.9%, NDM 7.4% in CRKP BSI; virulence gene profile | Resistance & virulence genetics |
| [42439974](https://pubmed.ncbi.nlm.nih.gov/42439974/) | OXA-48 predominant (50.4%) in Saudi CRE | Geographic resistance variation |
| [42021129](https://pubmed.ncbi.nlm.nih.gov/42021129/) | ST111 hvKp; 181 kb virulence plasmid; CRISPR curing | hvKp causal genetics |
| [41356976](https://pubmed.ncbi.nlm.nih.gov/41356976/) | 53-case systematic review of hvKp liver abscess | hvKp clinical phenotype |
| [22547706](https://pubmed.ncbi.nlm.nih.gov/22547706/) | NLRC4/IL-1β essential for pulmonary defense | Host mechanism |
| [36018281](https://pubmed.ncbi.nlm.nih.gov/36018281/) | TLR4 agonist protective in mice | Host mechanism / therapy lead |
| [42518856](https://pubmed.ncbi.nlm.nih.gov/42518856/) | 47.7% BSI mortality; D-dimer HR 1.04 | Prognosis/biomarker |
| [42455851](https://pubmed.ncbi.nlm.nih.gov/42455851/) | Non-polymyxin cure 58.4% vs 15.4% | Treatment outcome |
| [42216056](https://pubmed.ncbi.nlm.nih.gov/42216056/) | K47/K64 + KPC-plasmid features & mortality | Prognostic genetics |
| [35439291](https://pubmed.ncbi.nlm.nih.gov/35439291/) | IDSA 2022 CRE treatment guidance | Treatment standard |
| [42661422](https://pubmed.ncbi.nlm.nih.gov/42661422/) | German MDRO guideline first-line agents | Treatment standard |
| [42708480](https://pubmed.ncbi.nlm.nih.gov/42708480/) | CAZ-AVI faster clearance HR 2.475 | Treatment efficacy |
| [31525540](https://pubmed.ncbi.nlm.nih.gov/31525540/) | Meta-analysis of CRKP risk factors | Etiology/risk |
| [27239799](https://pubmed.ncbi.nlm.nih.gov/27239799/) | MALDI-TOF 174/174 identification | Diagnostics |
| [32305272](https://pubmed.ncbi.nlm.nih.gov/32305272/) | FilmArray BCID 94% concordance, blaKPC | Diagnostics |
| [31580426](https://pubmed.ncbi.nlm.nih.gov/31580426/) | MALDIxin colistin-resistance test | Diagnostics |
| [32576652](https://pubmed.ncbi.nlm.nih.gov/32576652/) | Stool reservoir of ST11 KPC-2 hvKp | Reservoir/convergence |
| [42634491](https://pubmed.ncbi.nlm.nih.gov/42634491/) | MrkA DNA vaccine 80% protection | Prevention |
| [42178970](https://pubmed.ncbi.nlm.nih.gov/42178970/) | ESKAPE priority designation | Public-health framing |

---

## Limitations and Knowledge Gaps

- **Template mismatch.** This template is designed for Mendelian/genetic diseases; sections on human causal genes,
inheritance, penetrance, chromosomal abnormalities, and germline variants are **not applicable** to an infectious
disease and were reframed to bacterial genetics.
- **Human host-susceptibility genetics** are underexplored — no replicated GWAS loci were identified; the
protective role of TLR4/NLRC4 is inferred from mouse models, not human association data.
- **Geographic bias.** Resistance and hvKp data skew toward East Asia, the Middle East, and select LMIC surveillance
sites; global prevalence/incidence per 100,000 is not uniformly quantified.
- **Prognostic evidence** derives largely from single-center retrospective cohorts (risk of confounding by
indication for therapy choices).
- **Vaccine and adjunctive-therapy data** are pre-clinical (murine); none is licensed or validated in humans.
- **Convergent resistant-hypervirulent clones** (e.g., ST11 KPC-2 hvKp) are documented but their population-level
frequency and outcome impact remain incompletely quantified.

---

## Proposed Follow-up Experiments / Actions

1. **Human host-genetics study:** targeted or genome-wide association analysis of *TLR4*, *NLRC4/NLRP*, *IL1B*,
and complement variants against severe *K. pneumoniae* sepsis to test the inferred protective pathways in humans.
2. **Prospective, multicenter trial** comparing ceftazidime-avibactam-based vs fosfomycin-combination vs
polymyxin-based regimens for CRKP BSI, powered for mortality and nephrotoxicity, stratified by carbapenemase class.
3. **Reservoir-interruption trial:** evaluate microbiome-preserving stewardship or decolonization strategies to
reduce endogenous CRKP/hvKp infection in ICU cohorts.
4. **Convergent-clone surveillance:** systematic WGS monitoring for resistant-plus-hypervirulent plasmids
(rmpADC + carbapenemase) to quantify emergence and outcomes.
5. **Advance MrkA/capsule/O-antigen vaccine candidates** toward first-in-human immunogenicity trials, prioritizing
high-risk populations (neonates in LMICs, ICU/transplant patients).
6. **Validate D-dimer and capsular-type (K47/K64) prognostic markers** in prospective cohorts and integrate into a
clinical risk-stratification tool.

---

*Report generated from a 5-iteration autonomous literature synthesis (10 confirmed findings, 46 papers). Evidence
types span human clinical cohorts/meta-analyses, genomic epidemiology, murine model studies, and in-vitro
diagnostics. All quantitative claims are attributed to the cited PMIDs.*


## Artifacts

- [OpenScientist final report](Klebsiella_Pneumonia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Klebsiella_Pneumonia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 37 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 22 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002048` (2 mentions) - the report calls it "lung", "Primary organs:** **lung"; UBERON calls it **lung**
- `UBERON:0002107` (2 mentions) - the report calls it "liver", "hvKp target organs:** **liver"; UBERON calls it **liver**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0100523` (1 mention) - the report calls it "Hepatic abscess"; HP calls it **Liver abscess**, and lists "Hepatic abscess" among its other names
- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `HP:0000010` (1 mention) - the report calls it "Recurrent UTI"; HP calls it **Recurrent urinary tract infections**, and lists "Recurrent UTIs" among its other names
- `GO:0038123` (1 mention) - the report calls it "toll-like receptor signaling"; GO calls it **toll-like receptor TLR1:TLR2 signaling pathway**
- `GO:0072559` (1 mention) - the report calls it "NLRP/NLRC4-type inflammasome complex — verify exact ID"; GO calls it **NLRP3 inflammasome complex**
- `UBERON:0001255` (1 mention) - the report calls it "urinary tract/bladder"; UBERON calls it **urinary bladder**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000775` - called "neutrophil", "neutrophils"
- `UBERON:0002048` - called "lung", "Primary organs:** **lung"
- `UBERON:0002107` - called "liver", "hvKp target organs:** **liver"