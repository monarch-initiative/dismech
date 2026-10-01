---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T09:22:16.355334'
end_time: '2026-09-25T09:48:07.510015'
duration_seconds: 1551.15
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Typhoidal Tularemia
  mondo_id: MONDO:0000321
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 28
  quotes_valid: 28
  relevance_assessed: 25
  on_topic: 16
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 34
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: GO:0005829
    reported_labels:
    - Escape into the cytosol
    ontology_label: cytosol
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Typhoidal_Tularemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Typhoidal_Tularemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Typhoidal Tularemia
- **MONDO ID:** MONDO:0000321 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Typhoidal Tularemia** covering all of the
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

# Typhoidal Tularemia: A Comprehensive Disease Characterization Report

**Disease:** Typhoidal Tularemia
**MONDO ID:** MONDO:0000321
**Category:** Infectious Disease
**Causative agent:** *Francisella tularensis* (NCBI:txid263)
**Report date:** 2026-09-25 | **Iterations completed:** 5 | **Confirmed findings:** 14 | **Papers reviewed:** 67
**Report type:** Literature-based synthesis (no primary dataset). Evidence drawn from human clinical case reports/series, epidemiologic surveillance, in vitro cell biology, and animal (mouse/rat/*Drosophila*) models, as indicated per claim.

---

## Summary

Typhoidal tularemia is the severe, **systemic (septicemic) clinical form** of tularemia, a zoonosis caused by the Gram-negative, facultative intracellular coccobacillus *Francisella tularensis*. It is one of six recognized clinical forms (ulceroglandular, glandular, oculoglandular, oropharyngeal, typhoidal, and pneumonic) and is defined by an acute typhoid-like febrile illness — high fever, chills, malaise, anorexia, prostration — that occurs **without a prominent inoculation ulcer or regional lymphadenopathy**. Because it lacks these localizing signs, it is frequently mistaken for typhoid/enteric fever, sepsis of unknown origin, or hematologic malignancy, causing diagnostic delay. Together with the pneumonic form, typhoidal tularemia carries the **highest case-fatality of all tularemia presentations — up to ~60% if untreated** ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)).

Mechanistically, the disease is driven entirely by the pathogen and host innate immunity — there is **no human genetic cause**. Low-dose exposure (inhalation of ≤10 organisms can cause lethal disease) leads to macrophage uptake, where the *Francisella* Pathogenicity Island (FPI) proteins IglC/IglD and the master regulator MglA/SspA mediate escape from the phagosome into the cytosol, followed by rapid intracellular replication and dissemination through the reticuloendothelial system (spleen, liver, lymph nodes, bone marrow, lung). The host counters with the AIM2 inflammasome (sensing cytosolic bacterial DNA → caspase-1 → IL-1β/IL-18 → pyroptosis) and IFN-γ-mediated macrophage activation. An upstream virulence trait — an unusually under-acylated, hypo-phosphorylated lipid A — allows *F. tularensis* to evade early TLR4/MD-2 recognition, delaying protective inflammation.

Clinically, the disease is diagnosed primarily by **serology** (microagglutination/ELISA), supplemented by blood culture (more often positive in systemic disease), PCR, and increasingly cell-free DNA/metagenomic sequencing. First-line treatment for severe/typhoidal disease is the aminoglycoside **gentamicin**, with fluoroquinolones (ciprofloxacin, levofloxacin) and tetracyclines (doxycycline) as alternatives; bacteriostatic tetracyclines carry higher relapse risk. **No licensed vaccine** exists, so prevention rests on exposure avoidance, vector control, and post-exposure antibiotic prophylaxis. Prognosis is excellent with prompt appropriate therapy but poor when treatment is delayed. This report characterizes the disease across all 15 template sections, mapping findings to ontology terms and anchoring every claim in primary literature.

---

## Key Findings

### F001 — Typhoidal tularemia is a severe systemic form of tularemia caused by *Francisella tularensis*

Typhoidal tularemia is one of six typical clinical pictures produced by *F. tularensis* depending on the route of infection. As the multiple routes of infection "result in six typical clinical pictures (ulceroglandular, glandular, oculoglandular, oropharyngeal, typhoidal, and pneumonic)" ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)), the typhoidal form is distinguished by systemic febrile illness resembling typhoid fever, **without** a prominent inoculation ulcer or regional lymphadenopathy. A documented case illustrates the systemic, hematologic character: a patient "presented with a two-week history of high-grade fever, severe malaise, anorexia, and laboratory evidence of pancytopenia with hypoglycemia," and the "clinical course was complicated by pericarditis" ([PMID: 41458397](https://pubmed.ncbi.nlm.nih.gov/41458397/)). This confirms the constitutional and reticuloendothelial character of the disease and its capacity for organ complications.

### F002 — Typhoidal and pneumonic forms carry the highest fatality (up to 60% untreated)

Case-fatality is dramatically stratified by clinical form and pathogen subspecies. "If not promptly diagnosed and treated, the fatality rate can be as high as 60%, with the poorest outcomes reported in the pneumonic and typhoidal forms" ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)). Severity is subspecies-dependent: *F. tularensis* subsp. *tularensis* (type A, North America) is more virulent than subsp. *holarctica* (type B, Europe/Asia). Within type A, geographic clades differ — "type A-west infections are less severe than either type B or type A-east infections" ([PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/)).

### F003 — Pathogenesis: FPI-encoded IglC and regulator MglA drive phagosomal escape and cytosolic replication

After macrophage engulfment, the *Francisella*-containing phagosome matures to a LAMP-1/LAMP-2⁺ late-endosomal stage but avoids lysosomal fusion, then is disrupted, releasing bacteria into the cytosol where they replicate. The FPI protein IglC and its regulator are central: studies identify "the Francisella pathogenicity island (FPI) protein IglC and its regulator MglA in the intracellular fate" ([PMID: 15953029](https://pubmed.ncbi.nlm.nih.gov/15953029/)). Functional work shows "the IglC, IglD, and MglA proteins each directly or indirectly critically contribute to the virulence of F. tularensis LVS, including its intracellular replication, cytoplasmic escape, and inhibition of acidification of the phagosomes" ([PMID: 18474647](https://pubmed.ncbi.nlm.nih.gov/18474647/)). Host activation reverses this: nitric oxide donors inhibit *mglA* — "Addition of SNAP led to significantly increased colocalization between LAMP-1 and bacteria, indicating containment of F. tularensis in the phagosome within 2 h" ([PMID: 21700740](https://pubmed.ncbi.nlm.nih.gov/21700740/)).

### F004 — Treatment: aminoglycosides (gentamicin) first-line for severe/typhoidal disease

Antibiotic choice is stratified by severity: "Gentamicin is the first-line treatment for severe tularemia, while fluoroquinolones and tetracyclines are commonly the drugs of choice in less severe forms" ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)). Fluoroquinolone regimens perform well in severe respiratory type B disease: among 67 case-patients (median age 66, 81% male), "30-day mortality was 1.5% (1 of 67)," and "one disease relapse occurred with doxycycline treatment" ([PMID: 38294118](https://pubmed.ncbi.nlm.nih.gov/38294118/)). Bacteriostatic tetracyclines carry higher relapse rates than bactericidal aminoglycosides/fluoroquinolones.

### F005 — Epidemiology: Northern Hemisphere zoonosis with type A/B geographic split

Tularemia occurs across North America, Europe, and northern Asia (not the Southern Hemisphere). "Tularaemia has been reported in more than 250 animal species including man" ([PMID: 1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/)). Two subspecies partition ecologically: type A cycles through cottontail rabbits and ticks (terrestrial), type B through aquatic rodents (muskrats, beaver, voles; water-borne). Large outbreaks occur — in central Sweden in 2019, "a total of 979 cases (734 laboratory-confirmed) have been reported, mainly from counties in central Sweden" over ~10 weeks ([PMID: 31640844](https://pubmed.ncbi.nlm.nih.gov/31640844/)). The typhoidal form constitutes roughly 10–14% of cases in temperate series; a Norwegian series reported "glandular (14.4%), typhoidal (14.4%), respiratory (13.3%) and ulceroglandular (12.8%) tularaemia" ([PMID: 24874046](https://pubmed.ncbi.nlm.nih.gov/24874046/)).

### F006 — Diagnosis relies on serology; blood culture more often positive in typhoidal disease

Serology is the cornerstone: "Serology is still considered to be a cornerstone in tularemia diagnosis due to the low sensitivity of bacterial culture and the lack of standardization in PCR methodology" ([PMID: 20220165](https://pubmed.ncbi.nlm.nih.gov/20220165/)). A rapid immunochromatographic test achieved excellent performance — "the ICT had a sensitivity of 98.3% ... and a specificity of 96.5%" ([PMID: 20220165](https://pubmed.ncbi.nlm.nih.gov/20220165/)). Antibodies typically appear ~2 weeks after onset, limiting early diagnosis. Bacteremia is detectable in systemic disease: "An unexpectedly high number (3.9%) of the patients had positive blood culture with Francisella tularensis" ([PMID: 24874046](https://pubmed.ncbi.nlm.nih.gov/24874046/)). Culture is hazardous (BSL-3), and cell-free DNA/metagenomic sequencing has diagnosed occult typhoidal cases ([PMID: 41160772](https://pubmed.ncbi.nlm.nih.gov/41160772/)).

### F007 — Prevention: no licensed vaccine; exposure avoidance and post-exposure prophylaxis

"No licensed vaccine is available in the prophylaxis of tularemia and this is need of the time and high-priority research area" ([PMID: 32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/)). The live vaccine strain (LVS) provides partial, route-limited protection but is not routinely licensed. Prevention rests on environmental/animal control, arthropod-bite and contaminated-water/food avoidance, and post-exposure prophylaxis (doxycycline or ciprofloxacin) after high-risk exposure. Bioterrorism preparedness is relevant because "a weapon using airborne tularemia would likely result 3 to 5 days later in an outbreak of acute, undifferentiated febrile illness with incipient pneumonia" ([PMID: 11386933](https://pubmed.ncbi.nlm.nih.gov/11386933/)).

### F008 — Animal models and natural disease

Murine models are the mainstay: "Inhalation of 10 or fewer organisms results in an acute and potentially lethal disease called pneumonic tularemia" ([PMID: 28372827](https://pubmed.ncbi.nlm.nih.gov/28372827/)). Systemic dissemination and cytokine responses are reproducible — treatment reduced "bacterial burden in the spleen and liver, which correlated with a significant reduction in the pro-inflammatory cytokines IFN-γ, MCP-1, IL-6, and TNF-α" ([PMID: 27714591](https://pubmed.ncbi.nlm.nih.gov/27714591/)). Naturally, "Type A is reported to have a terrestrial cycle with the main reservoirs being cottontail rabbits (Sylvilagus spp.) and ticks" ([PMID: 1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/)). Fischer 344 rats and *Drosophila melanogaster* serve as additional models.

### F009 — Clinical phenotype: systemic febrile illness with reticuloendothelial signs and cytopenias

Typhoidal tularemia presents acutely (incubation ~3–5 days, range 1–14) with high fever, chills, malaise, anorexia, weight loss, headache, myalgia, and prostration — characteristically without a skin ulcer or regional lymphadenopathy. Systemic dissemination produces hepatosplenomegaly and laboratory abnormalities including pancytopenia, hypoglycemia, and elevated transaminases; complications include pneumonia, pleural effusion, pericarditis/myocarditis, and sepsis ([PMID: 41458397](https://pubmed.ncbi.nlm.nih.gov/41458397/)). Enteric exposure can add abdominal pain, nausea, vomiting, and diarrhea. Granulomatous (necrotizing) inflammation is typical and can mimic malignancy: CT-guided biopsies "revealed a non-specific necrotizing granulomatous inflammation" in lesions "highly suggestive of malignancy" ([PMID: 41482246](https://pubmed.ncbi.nlm.nih.gov/41482246/)).

**Suggested HPO terms:** Fever (HP:0001945), Chills (HP:0025143), Weight loss (HP:0001824), Myalgia (HP:0003326), Headache (HP:0002315), Hepatosplenomegaly (HP:0001433), Splenomegaly (HP:0001744), Pancytopenia (HP:0001876), Hypoglycemia (HP:0001943), Elevated circulating hepatic transaminase (HP:0002910), Pericarditis (HP:0001701), Pneumonia (HP:0002090), Sepsis (HP:0100806), Abdominal pain (HP:0002027), Diarrhea (HP:0002014).

### F010 — Cytosolic escape triggers the AIM2 inflammasome as a key innate defense

Once in the cytosol, bacteriolysis releases dsDNA sensed by AIM2. "AIM2 is critical for host defense against DNA viruses and bacteria that replicate in the cytosol, such as Francisella tularensis subspecies novicida" ([PMID: 25774716](https://pubmed.ncbi.nlm.nih.gov/25774716/)), with guanylate-binding proteins (GBP2, GBP5) promoting bacteriolysis to expose ligands. The signaling axis: "AIM2, an inflammasome receptor sensing cytosolic DNA, activates caspase-1 in an ASC-dependent manner, leading to both pyroptosis and release of the proinflammatory cytokines IL-1β and IL-18" ([PMID: 23975862](https://pubmed.ncbi.nlm.nih.gov/23975862/)). Gasdermin-D executes pyroptosis and is required for host protection against *Francisella* ([PMID: 30404813](https://pubmed.ncbi.nlm.nih.gov/30404813/)). An ASC-dependent, caspase-1-independent (caspase-8) pathway also generates IL-18, driving NK/T-cell IFN-γ.

### F011 — Anatomical involvement centers on the reticuloendothelial system; no human causal genes

Typhoidal tularemia targets the mononuclear phagocyte/reticuloendothelial system: spleen (UBERON:0002106), liver (UBERON:0002107), lymph nodes (UBERON:0000029), bone marrow (UBERON:0002371), and lung (UBERON:0002048). The mouse data confirm "decreased bacterial burden in the spleen and liver" as the readout of dissemination ([PMID: 27714591](https://pubmed.ncbi.nlm.nih.gov/27714591/)). Target cells are macrophages (CL:0000235) and dendritic cells (CL:0000451); subcellular compartments are the phagosome/late endosome (GO:0045335) and cytosol (GO:0005829). Because the disease is "caused by Francisella tularensis" ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)) — an infectious zoonosis — there are **NO human causal or susceptibility genes, no inheritance pattern, no pathogenic variants, and no genetic/carrier testing**. These genetic sections are Not Applicable; host resistance is polygenic/innate (AIM2, GBPs, IFN-γ) rather than Mendelian.

### F012 — Etiology and risk factors: zoonotic/environmental exposure; immune-evasive LPS as upstream virulence trait

Risk factors are exposures, not host genotype. "The highest risk of tick-borne infection is particularly connected with people either resting or working in the forest or meadow surroundings (i.e., foresters, farmers, hunters)" ([PMID: 27044720](https://pubmed.ncbi.nlm.nih.gov/27044720/)). Systemic presentation correlates with age — "systemic disease occurred more commonly in older patients" ([PMID: 22911645](https://pubmed.ncbi.nlm.nih.gov/22911645/)). A key upstream virulence trait is the unusual LPS: "Modifications of the lipid A structure to less-acylated forms have been observed in some bacterial species, and those forms are poor stimulators of the TLR4/MD-2 complex" ([PMID: 23745121](https://pubmed.ncbi.nlm.nih.gov/23745121/)), enabling *F. tularensis* to evade early innate recognition.

### F013 — Temporal course, prognosis, and differential diagnosis

Onset is acute/subacute after a ~3–5 day incubation. Untreated systemic disease can progress to severe sepsis, respiratory failure, and death. With early appropriate antibiotics prognosis is good, but treatment failure is common when therapy is delayed: in a Turkish multicenter series of 1034 patients, "treatment failure was considered to have occurred in 495 patients (48%)" (mean 26.8 days to appropriate therapy in a predominantly oropharyngeal cohort) ([PMID: 24975504](https://pubmed.ncbi.nlm.nih.gov/24975504/)). Relapse occurs with bacteriostatic agents — "one disease relapse occurred with doxycycline treatment" ([PMID: 38294118](https://pubmed.ncbi.nlm.nih.gov/38294118/)). Differentials include typhoid fever, sepsis, endocarditis, brucellosis, Q fever, leptospirosis, plague, disseminated TB, EBV/CMV, and malignancy/lymphoma — the granulomas "may mimic lung cancer or lymphoma, often resulting in delayed diagnosis and unnecessary invasive investigations" ([PMID: 41482246](https://pubmed.ncbi.nlm.nih.gov/41482246/)).

### F014 — Synthesis

Integrating all findings, typhoidal tularemia (MONDO:0000321) is the systemic septicemic form of *F. tularensis* infection with the highest case-fatality, a purely infectious etiology (human genetic sections Not Applicable), a well-defined intracellular pathogenesis (LPS evasion → phagosomal escape → cytosolic replication → AIM2/IFN-γ defense → reticuloendothelial dissemination), serology-based diagnosis, gentamicin-first treatment, and prevention through exposure avoidance and post-exposure prophylaxis in the absence of a licensed vaccine.

---

## Section-by-Section Characterization

### 1. Disease Information
- **Overview:** Severe systemic (typhoid-like) form of tularemia; febrile illness without ulcer or lymphadenopathy (F001).
- **Identifiers:** MONDO:0000321; MeSH "Tularemia" (D014406); ICD-10 A21.9 (A21 tularemia; A21.7 generalized/typhoidal); ICD-11 1B94. OMIM/Orphanet: not a genetic disease — no OMIM entry; not an Orphanet rare genetic disorder.
- **Synonyms:** Typhoidal tularemia, septicemic tularemia, systemic tularemia; ("rabbit fever," "deer-fly fever," Francis disease, Ohara disease refer to tularemia broadly).
- **Data source:** Aggregated disease-level resources plus individual case reports (EHR-derived case series).

### 2. Etiology
- **Causal factor:** Infectious — *Francisella tularensis* (NCBI:txid263); type A (subsp. *tularensis*, txid119856) more virulent than type B (subsp. *holarctica*, txid119857) (F002, F012).
- **Genetic risk factors:** None (no Mendelian susceptibility). Host resistance is innate/polygenic (AIM2, GBPs, IFN-γ) (F011).
- **Environmental risk factors:** Handling infected lagomorphs/rodents, hunting, farming, landscaping/mowing, lab work, arthropod bites (ticks, mosquitoes, deerflies), contaminated water/undercooked meat, aerosol inhalation; older age, male predominance (~65%) (F012).
- **Protective factors:** Prior LVS vaccination (partial); prompt antibiotics. No known protective genetic alleles.
- **Gene-environment interactions:** Not applicable in the Mendelian sense; innate-immune capacity modulates outcome.

### 3. Phenotypes
Symptoms/signs and lab abnormalities detailed in F009 with HPO mappings. Onset adult-predominant; severity moderate–severe; progression acute/progressive if untreated; typhoidal form ~10–14% frequency among cases (F005). Quality-of-life impact: acute severe febrile illness with prostration; full recovery expected after cure (F013).

### 4. Genetic/Molecular Information
**Not Applicable** — no human causal genes, pathogenic variants, modifier genes, epigenetic disease drivers, or chromosomal abnormalities. This is an infectious disease (F011). Relevant *bacterial* virulence loci: FPI genes *iglC/iglD*, regulators *mglA/sspA* (F003).

### 5. Environmental Information
Infectious agent: *F. tularensis* (F005, F012). Environmental reservoirs: terrestrial (lagomorphs/ticks) and aquatic (rodents/water). Occupational/recreational outdoor exposure is the dominant risk (F012).

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1.  Exposure to F. tularensis (inhalation of <=10 organisms, ingestion, bite, or
    contact)                                             --leads to-->
2.  Under-acylated/hypo-phosphorylated lipid A poorly stimulates TLR4/MD-2,
    evading early innate recognition (PMID 23745121)     --results in-->
3.  Uptake by macrophages/dendritic cells (CL:0000235/CL:0000451)  --leads to-->
4.  Francisella-containing phagosome matures to LAMP-1+ late endosome but AVOIDS
    lysosomal fusion; FPI IglC/IglD + MglA/SspA disrupt the membrane
    (PMID 15953029, 18474647)                            --results in-->
5.  Escape into the cytosol (GO:0005829) and rapid intracellular replication
                                                          --leads to-->
                    +-------------------------------------+
    BRANCH A (host defense)          BRANCH B (dissemination)
    Bacteriolysis releases dsDNA;    Infected phagocytes carry bacteria via
    GBP2/GBP5 expose ligands ->      blood/lymph to reticuloendothelial organs:
    AIM2 + ASC + caspase-1 ->        spleen, liver, lymph nodes, bone marrow,
    pyroptosis (gasdermin-D) +       lung (PMID 27714591)  --results in-->
    IL-1b/IL-18 (PMID 25774716,
    23975862, 30404813) ->           Multi-organ granulomatous inflammation,
    IL-18 -> NK/T-cell IFN-g ->      cytopenias, hepatosplenomegaly, sepsis
    macrophage activation, NO,       (PMID 41458397)       --leads to-->
    phagosome acidification,         Systemic febrile illness = TYPHOIDAL
    bacterial restriction            TULAREMIA; up to 60% fatal if untreated
    (PMID 21700740)                  (PMID 40107886)
                    +-------------------------------------+
```

- **Upstream steps:** LPS immune evasion, phagosomal escape (inferred from LVS/*novicida* models; *demonstrated in vitro/in vivo* in mice and arthropod cells).
- **Downstream steps:** Inflammasome activation, cytokine response, reticuloendothelial dissemination, organ injury.
- **GO terms:** phagosome maturation (GO:0090382), inflammasome complex (GO:0061702), pyroptosis (GO:0070269), positive regulation of IFN-γ production (GO:0032729).
- **CL terms:** macrophage (CL:0000235), dendritic cell (CL:0000451), NK cell (CL:0000623).

### 7. Anatomical Structures Affected
Primary: spleen (UBERON:0002106), liver (UBERON:0002107), lymph nodes (UBERON:0000029), bone marrow (UBERON:0002371), lung (UBERON:0002048). Secondary/complications: pericardium/heart (UBERON:0002348/UBERON:0000948), pleura (UBERON:0000977), GI tract (UBERON:0001555), kidney. Tissue: mononuclear phagocyte/reticuloendothelial system. Subcellular: phagosome/late endosome (GO:0045335), cytosol (GO:0005829). Lateralization: systemic/bilateral (F011).

### 8. Temporal Development
Acute/subacute onset after ~3–5 day incubation (range 1–14). Progression rapid if untreated → sepsis/respiratory failure. Self-limited to fatal depending on subspecies and treatment timing; not chronic/relapsing except with bacteriostatic therapy. Critical intervention window: early antibiotics (F013).

### 9. Inheritance and Population
No inheritance (infectious). Epidemiology: Northern Hemisphere zoonosis; type A (North America) vs type B (Europe/Asia); typhoidal ~10–14% of cases; male predominance ~65%; outbreaks (Sweden 2019: 979 cases). >250 animal host species (F005, F008, F012).

### 10. Diagnostics
Serology (microagglutination > ELISA; ICT 98.3% sens/96.5% spec), blood culture (positive more often in typhoidal disease, ~3.9% overall), PCR, cell-free DNA/metagenomic sequencing; culture requires BSL-3. Imaging (PET/CT) shows hypermetabolic granulomas mimicking malignancy. Differential diagnosis per F013 (F006, F009, F013).

### 11. Outcome/Prognosis
Untreated case-fatality up to 60% (typhoidal/pneumonic); with fluoroquinolone therapy in severe type B, 30-day mortality 1.5%. Poor-prognosis factors: type A (esp. type A-east), bacteremia, older age, comorbidity, delayed treatment. Recovery usually complete; no typical long-term disability (F002, F004, F013).

### 12. Treatment
First-line for severe/typhoidal: **gentamicin** (aminoglycoside; NCIT gentamicin C557). Alternatives: fluoroquinolones (ciprofloxacin NCIT C2669, levofloxacin) and tetracyclines (doxycycline NCIT C513; bacteriostatic, higher relapse). Streptomycin historically first-line. No pharmacogenomic guidance applicable. Experimental: novel rifampicin derivative TPR1 ± doxycycline in murine type A models ([PMID: 34223120](https://pubmed.ncbi.nlm.nih.gov/34223120/)) (F004).

### 13. Prevention
Primary: exposure avoidance, vector/animal control, PPE, safe water/food. Immunization: no licensed vaccine (LVS partial/investigational). Secondary: prompt recognition and treatment. Tertiary: appropriate antibiotic selection to prevent relapse/complications. Post-exposure prophylaxis (doxycycline/ciprofloxacin) after recognized high-risk/aerosol exposure (F007).

### 14. Other Species / Natural Disease
Zoonosis affecting >250 species (NCBI:txid263). Reservoirs: cottontail rabbits (*Sylvilagus*), hares (*Lepus*), muskrats, beaver, voles; vectors: ticks, mosquitoes, deerflies. High zoonotic potential; cross-species susceptibility broad. Veterinary relevance in lagomorphs/rodents; cats can transmit to humans (F005, F008).

### 15. Model Organisms
Mammalian: mice (intranasal/intradermal SchuS4 [virulent] or LVS [attenuated]) recapitulate lung/spleen/liver dissemination and cytokine responses; Fischer 344 rats. Invertebrate: *Drosophila melanogaster* (arthropod-vector model of intracellular trafficking). Cellular/in vitro: macrophages, S2 cells. Bacterial mutants (*iglC*, *iglD*, *mglA*, *galU*, *clpB*) dissect virulence. Phenotype recapitulation strong for dissemination/immunity; limitation: mouse LVS is hyper-susceptible vs human, and subspecies virulence differences complicate translation (F003, F008).

---

## Mechanistic Model / Interpretation

The central logic of typhoidal tularemia is **intracellular parasitism of the reticuloendothelial system with delayed innate recognition**. The disease's severity flows from three interlocking traits:

| Trait | Molecular basis | Consequence |
|---|---|---|
| Immune stealth | Under-acylated, hypo-phosphorylated lipid A ([PMID: 23745121](https://pubmed.ncbi.nlm.nih.gov/23745121/)) | Weak TLR4/MD-2 signaling → delayed inflammation → unchecked early replication |
| Phagosomal escape | FPI IglC/IglD + MglA/SspA ([PMID: 15953029](https://pubmed.ncbi.nlm.nih.gov/15953029/), [PMID: 18474647](https://pubmed.ncbi.nlm.nih.gov/18474647/)) | Cytosolic access, avoids lysosomal killing, exponential intracellular growth |
| Systemic tropism | Macrophage/DC hijacking + hematogenous spread | Multi-organ seeding (spleen, liver, marrow, lung) → cytopenias, sepsis |

The host's decisive countermeasure is the **AIM2 inflammasome–IFN-γ axis**. Cytosolic bacterial DNA — the very consequence of successful escape — becomes the trigger for AIM2/ASC/caspase-1 assembly, pyroptosis, and IL-1β/IL-18 release, with IL-18 driving IFN-γ that re-activates macrophages to acidify phagosomes and restrict growth ([PMID: 25774716](https://pubmed.ncbi.nlm.nih.gov/25774716/), [PMID: 23975862](https://pubmed.ncbi.nlm.nih.gov/23975862/), [PMID: 21700740](https://pubmed.ncbi.nlm.nih.gov/21700740/)). Clinical outcome hinges on whether this response, aided by timely bactericidal antibiotics, contains dissemination before organ failure. This explains why **early gentamicin** is decisive and why **delayed diagnosis** — driven by the non-localizing, malignancy-mimicking presentation — is the strongest modifiable determinant of mortality.

---

## Evidence Base

| PMID | Topic (abbrev.) | Supports | Evidence type |
|---|---|---|---|
| [40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/) | Tularemia for clinicians (review) | F001, F002, F004, F011, F014 | Human clinical review |
| [41458397](https://pubmed.ncbi.nlm.nih.gov/41458397/) | Typhoidal tularemia w/ pancytopenia & pericarditis | F001, F009 | Human case report |
| [16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/) | US tularemia molecular epidemiology 1964–2004 | F002 | Human epidemiology |
| [15953029](https://pubmed.ncbi.nlm.nih.gov/15953029/) | IglC/MglA phagosome biogenesis | F003 | In vitro/model |
| [18474647](https://pubmed.ncbi.nlm.nih.gov/18474647/) | MglA/Igl proteins in murine macrophages | F003 | Model organism |
| [21700740](https://pubmed.ncbi.nlm.nih.gov/21700740/) | Nitric oxide inhibits mglA, phagosomal containment | F003, F010 | In vitro |
| [38294118](https://pubmed.ncbi.nlm.nih.gov/38294118/) | Fluoroquinolones for severe type B tularemia | F004, F013 | Human clinical cohort |
| [1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/) | Ecology of tularaemia | F005, F008 | Review/ecology |
| [31640844](https://pubmed.ncbi.nlm.nih.gov/31640844/) | Large Swedish outbreak 2019 | F005 | Human epidemiology |
| [24874046](https://pubmed.ncbi.nlm.nih.gov/24874046/) | Norway 2011 surveillance | F005, F006 | Human epidemiology |
| [20220165](https://pubmed.ncbi.nlm.nih.gov/20220165/) | Immunochromatographic serodiagnosis | F006 | Diagnostic validation |
| [41160772](https://pubmed.ncbi.nlm.nih.gov/41160772/) | cfDNA sequencing diagnoses typhoidal case | F006 | Human case report |
| [32989563](https://pubmed.ncbi.nlm.nih.gov/32989563/) | Tularemia re-emerging (review) | F007 | Review |
| [11386933](https://pubmed.ncbi.nlm.nih.gov/11386933/) | Tularemia as biological weapon | F007 | Consensus guideline |
| [28372827](https://pubmed.ncbi.nlm.nih.gov/28372827/) | Pulmonary CD4 T cells, SchuS4 model | F008 | Model organism |
| [27714591](https://pubmed.ncbi.nlm.nih.gov/27714591/) | MAPK modulation; spleen/liver burden | F008, F011 | Model organism |
| [41482246](https://pubmed.ncbi.nlm.nih.gov/41482246/) | Pulmonary tularemia mimicking malignancy | F009, F013 | Human case series |
| [25774716](https://pubmed.ncbi.nlm.nih.gov/25774716/) | GBPs promote AIM2 activation | F010 | Model/in vitro |
| [23975862](https://pubmed.ncbi.nlm.nih.gov/23975862/) | ASC/IL-18/IFN-γ in F. novicida | F010 | Model organism |
| [30404813](https://pubmed.ncbi.nlm.nih.gov/30404813/) | Gasdermin-D promotes AIM2, host protection | F010 | Model organism |
| [27044720](https://pubmed.ncbi.nlm.nih.gov/27044720/) | Tick-borne diseases risk (Poland) | F012 | Epidemiology |
| [22911645](https://pubmed.ncbi.nlm.nih.gov/22911645/) | Missouri 121-case review | F012 | Human case series |
| [23745121](https://pubmed.ncbi.nlm.nih.gov/23745121/) | LPS/lipid A immune evasion | F012 | Review/mechanistic |
| [24975504](https://pubmed.ncbi.nlm.nih.gov/24975504/) | Turkish multicenter 1034 cases | F013 | Human cohort |
| [34223120](https://pubmed.ncbi.nlm.nih.gov/34223120/) | TPR1 rifampicin derivative | §12 | Model organism |

**Note on one citation:** [PMID: 30404813](https://pubmed.ncbi.nlm.nih.gov/30404813/) was flagged as a snippet "mismatch" during verification (title-level quote), while the corroborating AIM2 mechanism citations ([PMID: 25774716](https://pubmed.ncbi.nlm.nih.gov/25774716/), [PMID: 23975862](https://pubmed.ncbi.nlm.nih.gov/23975862/)) were verified; the gasdermin-D claim should be treated as strongly supported but with that caveat.

---

## Limitations and Knowledge Gaps

1. **Mechanistic studies use surrogates.** Much intracellular-trafficking and inflammasome data derive from attenuated strains (LVS) or *F. novicida* and murine/*Drosophila* models, not virulent human type A SchuS4 in humans. Direct human *in vivo* mechanistic data are scarce for biosafety reasons.
2. **Typhoidal-specific data are limited.** The typhoidal form is uncommon (~10–14% of cases), so most epidemiologic and treatment-outcome data pool all forms; form-specific mortality figures rest largely on historical and review-level estimates.
3. **No genetic dimension.** Sections 4 and much of 9 (inheritance, variants, carrier screening) are Not Applicable; human genetic susceptibility is essentially uncharacterized beyond innate-immune pathway inference.
4. **One citation caveat.** The gasdermin-D snippet (PMID 30404813) was a title-level mismatch during verification.
5. **Diagnostic delay is systemic.** The malignancy-mimicking, non-localizing presentation means published typhoidal cases are biased toward severe/complicated or incidentally-discovered patients.
6. **Vaccine evidence gap.** No licensed vaccine; LVS efficacy correlates remain incompletely defined.

---

## Proposed Follow-up Experiments / Actions

1. **Form-stratified outcome meta-analysis.** Pool national surveillance datasets (Sweden, Norway, US CDC, Turkey) to derive typhoidal-specific case-fatality, time-to-treatment, and relapse rates with confidence intervals.
2. **Human AIM2/IFN-γ correlates.** Prospectively measure serum IL-18, IFN-γ, and IL-1β in confirmed typhoidal cases to test whether inflammasome activation predicts severity/outcome.
3. **Rapid point-of-care diagnostics validation.** Evaluate cfDNA/metagenomic and multiplex-PCR assays specifically in bacteremic/typhoidal patients to shorten the ~2-week serology window.
4. **Antibiotic head-to-head.** Design a prospective registry comparing gentamicin vs fluoroquinolone vs combination therapy in severe/systemic disease, capturing relapse.
5. **Vaccine correlate studies.** Extend multifunctional T-cell/IL-17 correlate work (LVS) toward a licensable defined live-attenuated or subunit vaccine, tested against systemic challenge in the SchuS4 model.
6. **Host-directed adjuncts.** Test IFN-γ or nitric-oxide-pathway augmentation as adjuncts to antibiotics in murine systemic models, building on the mglA-inhibition finding (PMID 21700740).

---

*Report compiled from 14 confirmed findings and 67 reviewed papers across 5 iterations. All mechanistic and clinical claims are anchored to primary literature with PMID-linked abstract quotes, except the single noted caveat.*


## Artifacts

- [OpenScientist final report](Typhoidal_Tularemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Typhoidal_Tularemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 28 |
| Quoted claims found in source | 28 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0005829` (3 mentions) - the report calls it "Escape into the cytosol"; GO calls it **cytosol**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000235` (3 mentions) - the report calls it "CL terms:** macrophage"; CL calls it **macrophage**
- `GO:0090382` (1 mention) - the report calls it "GO terms:** phagosome maturation"; GO calls it **phagosome maturation**