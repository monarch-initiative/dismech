---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-02T05:32:17.438169'
end_time: '2026-09-02T06:02:19.204886'
duration_seconds: 1801.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hennekam lymphangiectasia-lymphedema syndrome 1
  mondo_id: ''
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 37
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 14
  relevance_assessed: 37
  on_topic: 17
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 11
  labels_variant: 2
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
  path: Hennekam_Lymphangiectasia-Lymphedema_Syndrome_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hennekam_Lymphangiectasia-Lymphedema_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hennekam lymphangiectasia-lymphedema syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hennekam lymphangiectasia-lymphedema syndrome 1** covering all of the
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

# Hennekam Lymphangiectasia–Lymphedema Syndrome Type 1 (HKLLS1): Comprehensive Disease Characteristics Report

## Summary

**Hennekam lymphangiectasia–lymphedema syndrome type 1 (HKLLS1; OMIM 235510)** is an ultra-rare, autosomal recessive form of **generalized lymphatic dysplasia (GLD)** caused by biallelic loss-of-function variants in **CCBE1** (Collagen- and Calcium-Binding EGF domain-containing protein 1; chromosome 18q21.32). CCBE1 is a secreted extracellular matrix protein that, in concert with the metalloprotease **ADAMTS3**, proteolytically activates the pro-form of **VEGFC** into mature VEGFC. Mature VEGFC is the principal ligand that drives **VEGFR3 (FLT4)**-dependent lymphangiogenesis through downstream PI3K and Ras/ERK signaling. When CCBE1 function is lost, mature VEGFC production falls, VEGFR3 signaling in lymphatic endothelial cells is impaired, and lymphatic vessels develop abnormally throughout the body — producing the widespread lymphatic dysplasia that defines the disease.

Clinically, HKLLS1 presents with **congenital peripheral lymphedema, intestinal (and often serosal/pulmonary) lymphangiectasia causing protein-losing enteropathy (PLE), chylous effusions, characteristic facial dysmorphism (hypertelorism, flat nasal bridge, flat midface), and variable intellectual disability**. Secondary consequences of intestinal lymph leakage — hypoproteinemia, hypoalbuminemia, lymphopenia, and hypogammaglobulinemia — produce a secondary (combined) immunodeficiency that in some patients has presented as pediatric-onset common variable immune deficiency (CVID). Expressivity is highly variable, ranging from mild isolated lymphatic dysplasia without intellectual disability or dysmorphism, to severe recurrent non-immune hydrops fetalis detected prenatally. CCBE1 accounts for roughly **25%** of all Hennekam syndrome patients; the syndrome is genetically heterogeneous, with **FAT4** (HKLLS2) and **ADAMTS3** (HKLLS3) causing clinically overlapping disease, and **FBXL7** proposed as a candidate fourth gene.

There is **no curative or disease-specific therapy**. Management is supportive and multidisciplinary: a **low-long-chain-triglyceride, high-protein diet supplemented with medium-chain triglycerides (MCT)** is the cornerstone for the protein-losing enteropathy, supplemented as needed by albumin and immunoglobulin replacement, octreotide, diuretics, drainage of effusions, surgical resection of localized lesions, and complex decongestive therapy/compression for lymphedema. Diagnosis is confirmed by **whole-exome or whole-genome sequencing**, which is applicable prenatally in cases of recurrent hydrops fetalis. The disease is lifelong, and prognosis depends primarily on the severity of protein-losing enteropathy, effusions, and hydrops.

---

## Key Findings

### Finding 1 — HKLLS1 is caused by biallelic loss-of-function CCBE1 variants that impair VEGFC processing

Multiple independent families with HKLLS1 carry biallelic (homozygous or compound heterozygous) variants in **CCBE1**. Reported pathogenic variants include the homozygous missense c.472C>T (p.Arg158Cys), the compound heterozygous combination c.310G>A (p.Asp104Asn) + c.80T>C (p.Leu27Pro), and additional missense substitutions such as C174Y, C98W, and L27P. Functional assays in the zebrafish lymphatic-disease model demonstrated that these patient variants are **loss-of-function**. Mechanistically, CCBE1 is capable of upregulating the levels of fully processed, mature VEGFC in vitro, and overexpression of mature VEGFC rescues *ccbe1* loss-of-function phenotypes in zebrafish; genetically, *ccbe1* interacts with *vegfc* and *vegfr3*, and Vegfc/Vegfr3-dependent ERK signaling is impaired in the absence of Ccbe1.

The landmark study establishing this mechanism states that "*CCBE1 is capable of upregulating the levels of fully processed, mature VEGFC in vitro and the overexpression of mature VEGFC rescues ccbe1 loss-of-function phenotypes in zebrafish*" and directly links "*mutations in CCBE1 causing generalized lymphatic dysplasia and lymphedema (Hennekam syndrome)*" ([PMID: 24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/)). A separate cohort confirmed that patient CCBE1 variants act by loss of function: "*Functional analysis in a zebrafish model of lymphatic disease showed that both mutations lead to CCBE1 loss of function*" ([PMID: 27345729](https://pubmed.ncbi.nlm.nih.gov/27345729/)).

### Finding 2 — Hennekam syndrome is genetically heterogeneous: CCBE1 (type 1), FAT4 (type 2), ADAMTS3 (type 3)

HKLLS is an autosomal recessive disorder caused by biallelic variants in at least three genes: **CCBE1** (HKLLS1; OMIM 235510), **FAT4** (HKLLS2; OMIM 616006), and **ADAMTS3** (HKLLS3). CCBE1 mutations account for approximately **25%** of Hennekam patients. Critically, CCBE1 and ADAMTS3 act in the same molecular pathway: CCBE1 acts via ADAMTS3 to enhance VEGFC signaling, and ADAMTS3 mutations abolish proteolytic activation of pro-VEGFC. **FBXL7** has been proposed as a candidate fourth gene, acting through the FAT4 pathway.

A comprehensive review states: "*It is an autosomal recessive condition caused by biallelic mutations in CCBE1 ... (HKLLS1; OMIM 235510) or FAT4 (HKLLS2; OMIM 616006). CCBE1 acts via ADAMTS3 ... to enhance vascular endothelial growth factor C signaling*" ([PMID: 30450763](https://pubmed.ncbi.nlm.nih.gov/30450763/)). The 25% CCBE1 contribution is documented in [PMID: 27345729](https://pubmed.ncbi.nlm.nih.gov/27345729/): "*Hennekam lymphangiectasia-lymphedema syndrome is an autosomal recessive disorder, with 25% of patients having mutations in CCBE1.*" ADAMTS3 as the HKLLS3 gene was established through the discovery of "*bi-allelic missense mutations in ADAMTS3*" ([PMID: 28985353](https://pubmed.ncbi.nlm.nih.gov/28985353/)). A recent report of a novel biallelic FAT4 splice variant confirms HKLLS2 and the three-gene model: "*Hennekam lymphangiectasia-lymphedema syndrome (HKLLS) is an autosomal recessive disorder, caused by biallelic variants in CCBE1, FAT4, and ADAMTS3 genes*" ([PMID: 41992670](https://pubmed.ncbi.nlm.nih.gov/41992670/)).

### Finding 3 — Core clinical phenotype: congenital lymphedema, intestinal lymphangiectasia/PLE, facial dysmorphism, variable ID, and secondary immunodeficiency

The HKLLS1 phenotype comprises congenital peripheral lymphedema, generalized lymphatic dysplasia, intestinal lymphangiectasia causing protein-losing enteropathy with severe hypoproteinemia/hypoalbuminemia and hypogammaglobulinemia, ascites and chylous effusions, recurrent pericardial effusion, characteristic facial dysmorphism (hypertelorism, flat nasal bridge, flat midface), and variable intellectual disability. Some CCBE1 cases present as pediatric-onset common variable immune deficiency (CVID). The phenotype is notably variable: mild cases may lack intellectual disability and dysmorphism entirely.

A CCBE1-confirmed pediatric case documented the lymphedema and facial features: "*she presented an abdominal circumference of 60 cm, edema of the lower extremities and vulva, and facial dysmorphisms (hypertelorism, flat nasal bridge, flat mid-face)*" and "*blood laboratory investigations revealed severe hypoproteinemia, hypoalbuminemia and hypogammaglobulinemia*" ([PMID: 32629717](https://pubmed.ncbi.nlm.nih.gov/32629717/)). The core clinical tetrad is summarized as "*characterized by congenital lymphedema, intestinal lymphangiectasia, facial dysmorphism, and variable intellectual disability*" ([PMID: 31633297](https://pubmed.ncbi.nlm.nih.gov/31633297/)). The phenotypic variability at the mild end of the spectrum is illustrated by a CCBE1 (p.C98W) patient with "*lymphatic dysplasia without intellectual disability or dysmorphism*" ([PMID: 25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/)).

### Finding 4 — Mechanistic axis: CCBE1/ADAMTS3 → mature VEGFC → VEGFR3 (FLT4) → PI3K/Ras-ERK in lymphatic endothelium

VEGFR3 is the principal receptor tyrosine kinase in lymphatic endothelial cells (LECs). Binding of mature VEGFC (or VEGFD) stimulates VEGFR3 autophosphorylation and downstream **PI3K** and **Ras/ERK** cascades that drive LEC proliferation, migration, and survival. CCBE1, together with ADAMTS3, is required to proteolytically generate mature, active VEGFC. In HKLLS1, loss of CCBE1 function reduces the supply of mature VEGFC and thereby lowers VEGFR3 signaling output — an upstream lesion producing downstream failure of lymphatic vessel formation.

A recent review of VEGFR3 biology states that "*VEGFR3 primarily promotes downstream signaling through the phosphoinositide 3-kinase (PI3K) and Ras signaling cascades that promote functions including cell proliferation and migration*," and that "*The importance of VEGFR3 cascades in lymphatic physiology is underscored by identification of dysfunctional VEGFR3 signaling across several lymphatic-related diseases*" ([PMID: 40046235](https://pubmed.ncbi.nlm.nih.gov/40046235/)). The specific coupling of CCBE1 loss to reduced VEGFR3-ERK signaling is demonstrated by "*Vegfc- and Vegfr3-dependent Erk signaling is impaired in the absence of Ccbe1*" ([PMID: 24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/)).

### Finding 5 — CCBE1 function and disease mechanism are conserved and validated in zebrafish and mouse models

CCBE1 orthologs are highly conserved across zebrafish, mice, and humans, and CCBE1 mutations cause generalized lymphatic dysplasia/Hennekam syndrome across species. In zebrafish, *ccbe1* genetically interacts with *vegfc* and *vegfr3* (*flt4*), and patient variants (e.g., L27P, D104N, C98W) recapitulate loss of function. In mice, the biochemical mechanism has been dissected: an **ADAMTS3-CCBE1 complex forms independently of VEGFR3** and is required to convert VEGFC (but not VEGFD) into an active ligand. Inducible deletion of Ccbe1 in mice impairs postnatal meningeal lymphatic development and reduces macromolecule drainage, establishing a role for CCBE1 in both development and maintenance of lymphatics.

Conservation and disease relevance are stated directly: "*The role of CCBE1 orthologs is highly conserved in zebrafish, mice and humans with mutations in CCBE1 causing generalized lymphatic dysplasia and lymphedema (Hennekam syndrome)*" ([PMID: 24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/)). The biochemical complex is established in "*an ADAMTS3-CCBE1 complex can form independently of VEGFR3 and is required to convert VEGFC, but not VEGFD, into an active ligand*" ([PMID: 27159393](https://pubmed.ncbi.nlm.nih.gov/27159393/)). Meningeal lymphatic requirement is documented in [PMID: 38141283](https://pubmed.ncbi.nlm.nih.gov/38141283/): "*inducible deletion of CCBE1 leads to impaired postnatal development of the meningeal lymphatics and decreased macromolecule drainage to deep cervical lymph nodes.*"

### Finding 6 — Immunodeficiency in HKLLS1 is secondary to protein-losing enteropathy, not a primary immune defect

Intestinal lymphangiectasia causes leakage of protein- and lymphocyte-rich lymph into the gut lumen, producing hypoalbuminemia, lymphopenia, and hypogammaglobulinemia — a **secondary (combined) immunodeficiency** rather than an intrinsic defect in immune-cell development. HKLLS1/CCBE1 cases have presented as pediatric-onset CVID. Immunoglobulin replacement (including subcutaneous) can be used, but the MCT diet, which reduces lymph loss, is the cornerstone that addresses the root cause.

The causal chain is stated as "*it is responsible for protein losing enteropathy leading to lymphopenia, hypoalbuminemia and hypogammaglobulinemia*" ([PMID: 26934740](https://pubmed.ncbi.nlm.nih.gov/26934740/)), and the corresponding laboratory abnormalities in a CCBE1 patient are documented in [PMID: 32629717](https://pubmed.ncbi.nlm.nih.gov/32629717/): "*blood laboratory investigations revealed severe hypoproteinemia, hypoalbuminemia and hypogammaglobulinemia.*"

### Finding 7 — Diagnosis relies on exome/genome sequencing; prenatal presentation is recurrent non-immune hydrops fetalis

Because HKLLS1 has nonspecific, overlapping features, **whole-exome sequencing (WES)** is the recommended diagnostic approach and can be applied prenatally. WES diagnosed HKLLS1 as the cause of recurrent hydrops fetalis. Generalized lymphatic dysplasia — lymphedema, lymphangiectasia, chylothorax, and pleural/pericardial effusions — can present prenatally as **non-immune hydrops fetalis**. The differential diagnosis includes other autosomal recessive GLD genes (**PIEZO1, GDF2**) and syndromic lymphedema genes. Supportive diagnostics include hypoproteinemia/hypoalbuminemia, low immunoglobulins, elevated stool alpha-1-antitrypsin, lymphoscintigraphy showing abnormal tracer leakage, and endoscopic/biopsy evidence of dilated intestinal lymphatics.

WES utility and prenatal presentation are documented: "*Whole exome sequencing (WES) was used to determine the etiology of recurrent hydrops fetalis in this case of Hennekam lymphangiectasia-lymphedema syndrome-1. WES is a useful approach for diagnosing rare single-gene conditions with nonspecific phenotypes*" ([PMID: 30564329](https://pubmed.ncbi.nlm.nih.gov/30564329/)). Supportive laboratory findings appear in [PMID: 40394495](https://pubmed.ncbi.nlm.nih.gov/40394495/): "*laboratory tests showed decreased blood albumin and increased stool α1-antitrypsin.*" The GLD spectrum and prenatal hydrops context are defined in [PMID: 26333996](https://pubmed.ncbi.nlm.nih.gov/26333996/): "*Generalized lymphatic dysplasia (GLD) is a rare form of primary lymphoedema characterized by a uniform, widespread lymphoedema affecting all segments of the body, with systemic involvement such as intestinal and/or pulmonary lymphangiectasia, pleural effusions, chylothoraces and/or pericardial effusions. This may present prenatally as non-immune hydrops.*"

### Finding 8 — Epidemiology: ultra-rare autosomal recessive disorder; consanguinity is a major risk context

Hennekam syndrome is autosomal recessive; CCBE1 mutations account for ~25% of patients. It is ultra-rare, with only ~50–60 total reported patients across all subtypes (one patient described as the 51st case worldwide). Many CCBE1 families are consanguineous with homozygous variants. Recurrence risk is **25% per pregnancy**, and expressivity is highly variable (from mild lymphatic dysplasia to severe recurrent non-immune hydrops fetalis).

The rarity scale is noted in [PMID: 38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/): "*this is the 51st case of HS worldwide.*" Consanguinity as a recurring context is documented in [PMID: 26686525](https://pubmed.ncbi.nlm.nih.gov/26686525/): "*born to consanguineous parents of Turkish ancestry*," and in the mild-form report of a consanguineous family of Pakistani descent ([PMID: 25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/)).

### Finding 9 — Management is supportive: MCT/low-LCT high-protein diet, albumin/immunoglobulin, drainage, and multidisciplinary care

No disease-specific or curative therapy exists. Intestinal lymphangiectasia/PLE is managed with a low-long-chain-triglyceride, high-protein diet supplemented with **medium-chain triglycerides (MCT)**, sometimes with (total) parenteral nutrition and fat-soluble vitamin supplementation. In a pooled review of primary intestinal lymphangiectasia (PIL), **63% (17/27)** of MCT-treated patients had complete symptom resolution versus **35.7% (10/28)** untreated, with lower mortality (**3.7% vs 17.85%**). Octreotide is used when MCT fails; diuretics, albumin transfusions, and surgical resection of localized lesions or effusion drainage are adjuncts. Lymphedema is managed with complex decongestive therapy/compression.

The quantitative benefit of MCT is documented in [PMID: 19449286](https://pubmed.ncbi.nlm.nih.gov/19449286/): "*17 of 27 cases (63%) treated with MCT had complete resolution of symptoms while only 10 of 28 (35.7%) patients in group B showed complete resolution. Mortality for Group A was 1 out of 27 (3.7%), while mortality in group B was 5 of 28 (17.85%).*" MCT diet as standard management is reinforced by [PMID: 20571826](https://pubmed.ncbi.nlm.nih.gov/20571826/): "*In patients with lymphangiectasia, a low fat with medium chain triglycerides (MCT) diet should be prescribed.*"

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** HKLLS1 is a Mendelian, autosomal recessive **generalized lymphatic dysplasia** — a systemic disorder of lymphatic vessel development. It combines lymphedema with lymphangiectasia (dilated, dysfunctional lymphatic vessels) affecting the intestine and other tissues, characteristic facial dysmorphism, and variable intellectual disability. It is the CCBE1-defined subtype of Hennekam syndrome.

**Key identifiers.**
- **OMIM:** 235510 (Hennekam lymphangiectasia-lymphedema syndrome 1)
- **Gene:** CCBE1 (HGNC:29426), chromosome 18q21.32
- **Related subtypes:** HKLLS2 (FAT4; OMIM 616006), HKLLS3 (ADAMTS3)
- **Orphanet:** Hennekam syndrome (ORPHA:2136 for the clinical entity)
- **Suggested MONDO:** the MONDO class mapping to OMIM 235510 (Hennekam lymphangiectasia-lymphedema syndrome 1)
- **ICD-10:** Q82.0 (hereditary lymphedema) as closest mapping; **ICD-11:** hereditary lymphedema / lymphatic malformation category (LD-block)
- **MeSH:** Lymphangiectasis; Lymphedema (no dedicated Hennekam MeSH descriptor)

**Synonyms / alternative names:** Hennekam syndrome; Hennekam lymphangiectasia-lymphedema syndrome; generalized lymphatic dysplasia of Hennekam; intestinal lymphangiectasia–lymphedema–intellectual disability syndrome; lymphedema–lymphangiectasia–intellectual disability syndrome.

**Information source.** The knowledge base for HKLLS1 is derived from **aggregated disease-level resources** (OMIM, Orphanet) and from **individual patient case reports and small case series** in the primary literature, given the disease's rarity (~50–60 reported patients).

### 2. Etiology

**Causal factors.** HKLLS1 is a purely **genetic** disorder caused by biallelic (homozygous or compound heterozygous) loss-of-function variants in **CCBE1**. There is no infectious or environmental cause. The primary lesion disrupts proteolytic maturation of pro-VEGFC (Findings 1, 4).

**Genetic risk factors.** The causal factor is biallelic pathogenic CCBE1 variation. **Consanguinity** substantially increases risk of homozygous disease and is a recurring context in reported families (Finding 8; [PMID: 26686525](https://pubmed.ncbi.nlm.nih.gov/26686525/), [PMID: 25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/)). Heterozygous carriers are unaffected. Genes in the same pathway (FAT4, ADAMTS3, and candidate FBXL7) cause clinically overlapping but distinct HKLLS subtypes.

**Environmental risk factors / protective factors.** None are established. The disorder is fully penetrant given a biallelic loss-of-function genotype; no protective alleles or environmental modifiers have been described. Diet (MCT) modifies the *complication* (protein-losing enteropathy) but does not alter the underlying genetic cause.

**Gene–environment interactions.** No specific GxE interactions are documented for HKLLS1.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset | Frequency/severity | Notes |
|---|---|---|---|---|---|
| Congenital lymphedema (limbs, genitalia) | Physical manifestation | HP:0001004 (Lymphedema) | Congenital/neonatal | Common; variable | Peripheral, often bilateral; may persist after generalized edema resolves ([PMID: 25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/)) |
| Intestinal lymphangiectasia | Clinical sign / pathology | HP:0002593 (Intestinal lymphangiectasia) | Infancy/childhood | Common | Cause of PLE ([PMID: 32629717](https://pubmed.ncbi.nlm.nih.gov/32629717/)) |
| Protein-losing enteropathy | Lab/clinical | HP:0002243 (Protein-losing enteropathy) | Infancy/childhood | Common | Hypoproteinemia, edema |
| Hypoproteinemia / hypoalbuminemia | Lab abnormality | HP:0003075 (Hypoproteinemia); HP:0003073 (Hypoalbuminemia) | Infancy | Common | Secondary to PLE |
| Hypogammaglobulinemia | Lab abnormality | HP:0004313 (Decreased circulating antibody level) | Childhood | Common | Secondary immunodeficiency ([PMID: 26934740](https://pubmed.ncbi.nlm.nih.gov/26934740/)) |
| Lymphopenia | Lab abnormality | HP:0001888 (Lymphopenia) | Childhood | Common | Lymph loss into gut |
| Chylous ascites / pleural / pericardial effusion | Clinical sign | HP:0001541 (Ascites); HP:0002202 (Pleural effusion); HP:0001698 (Pericardial effusion) | Congenital–childhood | Variable | Recurrent pericardial effusion reported ([PMID: 40394495](https://pubmed.ncbi.nlm.nih.gov/40394495/)) |
| Facial dysmorphism (hypertelorism, flat nasal bridge, flat midface) | Physical manifestation | HP:0000316 (Hypertelorism); HP:0005280 (Depressed nasal bridge); HP:0011800 (Midface retrusion) | Congenital | Common in classic form | ([PMID: 32629717](https://pubmed.ncbi.nlm.nih.gov/32629717/)) |
| Intellectual disability | Neurodevelopmental | HP:0001249 (Intellectual disability) | Childhood | Variable; absent in mild forms | ([PMID: 31633297](https://pubmed.ncbi.nlm.nih.gov/31633297/), [PMID: 25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/)) |
| Non-immune hydrops fetalis | Prenatal clinical sign | HP:0001790 (Nonimmune hydrops fetalis) | Prenatal | Severe end of spectrum | Recurrent presentation ([PMID: 30564329](https://pubmed.ncbi.nlm.nih.gov/30564329/)) |

**Quality-of-life impact.** Lymphedema and recurrent effusions impair mobility and require lifelong compression/decongestive therapy. Protein-losing enteropathy necessitates lifelong dietary management and predisposes to recurrent infections (secondary immunodeficiency), edema, and growth impairment. Severe/prenatal presentations carry high perinatal morbidity and mortality (hydrops). Formal EQ-5D/SF-36 data are not available for this ultra-rare disease.

### 4. Genetic/Molecular Information

**Causal gene:** **CCBE1** (Collagen- and Calcium-Binding EGF domain-containing protein 1), 18q21.32; OMIM gene 612753; HGNC:29426; NCBI Gene 147372. The protein is a secreted extracellular-matrix factor with an N-terminal EGF-like (calcium-binding) domain and C-terminal collagen-repeat domains.

**Pathogenic variants (reported in HKLLS1):**

| Variant (cDNA) | Protein | Zygosity | Class | Evidence |
|---|---|---|---|---|
| c.472C>T | p.Arg158Cys | Homozygous / compound het | Missense, LoF | [PMID: 32472549](https://pubmed.ncbi.nlm.nih.gov/32472549/) |
| c.521G>A | (compound het partner) | Compound het | Missense | [PMID: 32472549](https://pubmed.ncbi.nlm.nih.gov/32472549/) |
| c.310G>A | p.Asp104Asn | Compound het | Missense, LoF | [PMID: 24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/) |
| c.80T>C | p.Leu27Pro | Compound het | Missense, LoF | [PMID: 24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/) |
| — | p.Cys98Trp (C98W) | Homozygous | Missense, LoF (mild form) | [PMID: 25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/) |
| — | p.Cys174Tyr (C174Y) | — | Missense | (cohort) [PMID: 27345729](https://pubmed.ncbi.nlm.nih.gov/27345729/) |

**Variant classification.** Reported variants are classified pathogenic/likely pathogenic under ACMG/AMP criteria, supported by functional zebrafish loss-of-function assays (PS3-level functional evidence), segregation, and rarity in population databases. In silico analyses predict additional deleterious CCBE1 nsSNPs (e.g., G330E, C102S, C174R, G107D) as candidate pathogenic variants, several affecting conserved cysteines/EGF domains and ligand-binding residues ([PMID: 34234628](https://pubmed.ncbi.nlm.nih.gov/34234628/)).

**Variant type/class:** Predominantly **missense** variants (many affecting conserved cysteine residues critical for domain folding), plus splice and nonsense variants; large deletions are not the dominant mechanism for CCBE1.

**Allele frequency:** Pathogenic CCBE1 variants are individually rare/absent in gnomAD, consistent with a recessive ultra-rare disorder. One kindred carried a homozygous CCBE1 variant that does not prevent protein expression, indicating that some pathogenic variants act by disrupting function rather than abolishing protein ([PMID: 26686525](https://pubmed.ncbi.nlm.nih.gov/26686525/)).

**Somatic vs germline:** **Germline** (biallelic, inherited) in HKLLS1. (Note: CCBE1 is also somatically dysregulated/overexpressed in colorectal cancer where it promotes tumor lymphangiogenesis, but this is unrelated to the germline disease — [PMID: 32089745](https://pubmed.ncbi.nlm.nih.gov/32089745/), [PMID: 36781122](https://pubmed.ncbi.nlm.nih.gov/36781122/).)

**Functional consequence:** **Loss of function** — reduced proteolytic maturation of pro-VEGFC and impaired VEGFR3 signaling (Findings 1, 4, 5).

**Modifier genes:** Not formally established. Genes in the same pathway (ADAMTS3, VEGFC, FLT4/VEGFR3, VEGFD) are biologically plausible modifiers; VEGFD can partially compensate for VEGFC loss in zebrafish facial lymphatics ([PMID: 24903752](https://pubmed.ncbi.nlm.nih.gov/24903752/)).

**Epigenetic information / chromosomal abnormalities:** No disease-specific epigenetic signature or recurrent chromosomal abnormality is defined for HKLLS1. (Zebrafish work shows copper stress can epigenetically regulate *ccbe1* expression, a mechanistic curiosity rather than a human disease mechanism — [PMID: 35034208](https://pubmed.ncbi.nlm.nih.gov/35034208/).)

### 5. Environmental Information

No environmental, lifestyle, or infectious factors cause or trigger HKLLS1 — it is a monogenic, congenital disorder. Environmental factors are relevant only insofar as diet (long-chain triglyceride intake) exacerbates protein-losing enteropathy, which is why MCT substitution is therapeutic (Finding 9). No infectious agents are implicated; recurrent infections in patients are a *consequence* of secondary immunodeficiency, not a cause.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function CCBE1 variants** (germline) **lead to** a dysfunctional or reduced-activity CCBE1 protein in the extracellular matrix. *(demonstrated — patient variants shown LoF in zebrafish)*
2. Loss of CCBE1 function **impairs formation of the ADAMTS3–CCBE1 complex** and reduces colocalization of pro-VEGFC with its activating protease at the lymphatic endothelial cell surface. *(demonstrated — mouse/in vitro; [PMID: 27159393](https://pubmed.ncbi.nlm.nih.gov/27159393/), [PMID: 28687807](https://pubmed.ncbi.nlm.nih.gov/28687807/))*
3. Reduced proteolytic activation **results in decreased levels of mature (fully processed) VEGFC**. *(demonstrated — [PMID: 24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/))*
4. Decreased mature VEGFC **leads to reduced VEGFR3 (FLT4) autophosphorylation** on lymphatic endothelial cells. *(inferred from ligand loss + established VEGFR3 biology)*
5. Reduced VEGFR3 signaling **results in impaired downstream PI3K and Ras/ERK cascades**. *(demonstrated — impaired Vegfc/Vegfr3-dependent ERK signaling without Ccbe1; [PMID: 24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/))*
6. Impaired PI3K/ERK signaling **leads to defective LEC proliferation, migration, sprouting, and survival**. *(demonstrated in zebrafish/mouse lymphangiogenesis models)*
7. Defective lymphangiogenesis **results in generalized lymphatic dysplasia** — hypoplastic/dysfunctional, dilated lymphatic vessels (lymphangiectasia) throughout the body. *(demonstrated clinically/histologically)*
8. Branch A: dysplastic peripheral lymphatics **cause congenital lymphedema**.
9. Branch B: dilated/leaky intestinal lymphatics **cause intestinal lymphangiectasia → protein-losing enteropathy**, leaking protein- and lymphocyte-rich lymph into the gut lumen.
10. PLE **leads to hypoproteinemia, hypoalbuminemia, lymphopenia, and hypogammaglobulinemia → secondary (combined) immunodeficiency** and edema. *(demonstrated — [PMID: 26934740](https://pubmed.ncbi.nlm.nih.gov/26934740/))*
11. Branch C: dysplastic serosal/pulmonary lymphatics **cause chylous ascites, pleural and pericardial effusions**, and — at the severe end — **prenatal non-immune hydrops fetalis**. *(demonstrated — [PMID: 26333996](https://pubmed.ncbi.nlm.nih.gov/26333996/), [PMID: 30564329](https://pubmed.ncbi.nlm.nih.gov/30564329/))*
12. Facial dysmorphism and variable intellectual disability arise via incompletely understood developmental effects (possibly abnormal facial/cranial lymphatic development and fluid dynamics). *(inferred)*

```
CCBE1 (LoF, biallelic)
        │  (with ADAMTS3)
        ▼
  pro-VEGFC  ──X──►  mature VEGFC   [reduced]
                          │
                          ▼
                    VEGFR3 / FLT4   [reduced signaling]
                     ┌────┴────┐
                   PI3K      Ras/ERK
                     └────┬────┘
                          ▼
         LEC proliferation/migration/survival  [impaired]
                          ▼
             Generalized lymphatic dysplasia
             ┌───────────┼───────────────┐
             ▼           ▼               ▼
   peripheral        intestinal      serosal/pulmonary
   lymphedema      lymphangiectasia   lymphatics
                        │                  │
                        ▼                  ▼
                  protein-losing      ascites/pleural/
                  enteropathy         pericardial effusion;
                        │             prenatal hydrops fetalis
                        ▼
        hypoproteinemia, lymphopenia,
        hypogammaglobulinemia
        → secondary immunodeficiency
```

**Molecular pathways:** VEGFC–VEGFR3 (FLT4) lymphangiogenic signaling; downstream PI3K-AKT and Ras/MAPK-ERK. **Suggested GO terms:** GO:0001945 (lymph vessel development), GO:0001946 (lymphangiogenesis), GO:0048010 (vascular endothelial growth factor receptor signaling pathway), GO:0004175 (endopeptidase activity, for ADAMTS3), GO:0043542 (endothelial cell migration), GO:0001936 (regulation of endothelial cell proliferation). **Cellular processes:** LEC proliferation, migration, survival; extracellular matrix–mediated growth-factor processing. **Protein dysfunction:** loss of CCBE1 co-factor/protease-enhancing function (reduced ADAMTS3 cleavage activity and reduced VEGFC/ADAMTS3 colocalization). **Cell types:** lymphatic endothelial cells (**CL:0002138**, endothelial cell of lymphatic vessel); supporting sources of Vegfc/Ccbe1 include fibroblasts and neuronal/mural cells in model systems ([PMID: 32483144](https://pubmed.ncbi.nlm.nih.gov/32483144/), [PMID: 35316177](https://pubmed.ncbi.nlm.nih.gov/35316177/)). **CHEBI:** medium-chain triglyceride / triacylglycerol (CHEBI:17855) relevant to therapy.

### 7. Anatomical Structures Affected

**Organ / system level:**
- **Primary:** lymphatic vasculature (systemic) — **UBERON:0001473** (lymphatic vessel); lymphatic system (UBERON:0006558).
- **Intestine** — intestinal lymphatics/lacteals (**UBERON:0000160** intestine); site of lymphangiectasia and PLE.
- **Skin/subcutis** of limbs and genitalia (lymphedema) — **UBERON:0002097** (skin).
- **Serous cavities:** peritoneal (ascites — UBERON:0002358), pleural (effusion — UBERON:0002402), pericardial (effusion — UBERON:0002407).
- **Lungs** (pulmonary lymphangiectasia) — UBERON:0002048.
- **Face/craniofacial** (dysmorphism).
- **Secondary/complication:** immune system (secondary immunodeficiency), cardiovascular (pericardial effusion), and — prenatally — generalized fetal edema (hydrops).

**Tissue and cell level:** endothelial tissue of lymphatic vessels; the targeted cell population is the **lymphatic endothelial cell (CL:0002138)**. Connective-tissue/fibroblast and mural/neuronal sources of pathway ligands are involved in normal development.

**Subcellular level:** CCBE1 is a **secreted / extracellular matrix** protein (GO:0005576 extracellular region; GO:0031012 extracellular matrix). VEGFR3 signaling occurs at the plasma membrane (GO:0005886) with downstream cytoplasmic kinase cascades.

**Localization / lateralization:** Systemic and generally **bilateral**; lymphedema of limbs and genitalia is typically bilateral, though asymmetric involvement occurs across the broader lymphangiectasia spectrum.

### 8. Temporal Development

- **Onset:** Congenital — lymphedema is present at birth or in the neonatal period; the most severe presentations occur **prenatally** as recurrent non-immune hydrops fetalis ([PMID: 30564329](https://pubmed.ncbi.nlm.nih.gov/30564329/)). Intestinal lymphangiectasia/PLE typically manifests in infancy/early childhood ([PMID: 32629717](https://pubmed.ncbi.nlm.nih.gov/32629717/)).
- **Onset pattern:** Chronic/congenital (structural developmental defect present from birth).
- **Progression:** Lifelong (chronic). Effusions and PLE may follow a **fluctuating/episodic** course (e.g., recurrent pericardial effusion — [PMID: 40394495](https://pubmed.ncbi.nlm.nih.gov/40394495/)). Some patients stabilize with dietary management; the underlying lymphatic dysplasia is non-remitting.
- **Disease duration:** Chronic, lifelong.
- **Critical periods:** The prenatal/perinatal period is the key window of vulnerability (hydrops-related mortality); early diagnosis and initiation of the MCT diet in infancy is the main window of therapeutic opportunity for PLE.

### 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic CCBE1). Recurrence risk 25% per pregnancy; carrier parents unaffected.
- **Penetrance:** Effectively complete for the biallelic loss-of-function genotype, but **expressivity is highly variable** — from mild isolated lymphatic dysplasia to lethal recurrent hydrops (Findings 3, 8).
- **Epidemiology:** Ultra-rare; ~50–60 total reported patients of Hennekam syndrome across all subtypes, with CCBE1 accounting for ~25% ([PMID: 27345729](https://pubmed.ncbi.nlm.nih.gov/27345729/), [PMID: 38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/)). Precise prevalence/incidence figures are not established; Orphanet lists Hennekam syndrome as <1/1,000,000.
- **Consanguinity / founder effects:** Consanguinity is a major risk context; multiple homozygous CCBE1 families of Turkish, Pakistani, and other ancestries reported ([PMID: 26686525](https://pubmed.ncbi.nlm.nih.gov/26686525/), [PMID: 25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/)). No specific founder mutation is established.
- **Sex ratio:** No strong sex bias reported (autosomal recessive; both sexes affected). Carrier frequency is not precisely defined but is expected to be low.
- **Geographic distribution:** Worldwide; case clusters reflect consanguineous populations rather than a true endemic distribution.

### 10. Diagnostics

**Genetic testing (definitive):** **Whole-exome sequencing (WES)** or whole-genome sequencing is the recommended diagnostic approach because the phenotype is nonspecific and overlaps other GLD syndromes; WES is applicable prenatally ([PMID: 30564329](https://pubmed.ncbi.nlm.nih.gov/30564329/)). Targeted CCBE1 sequencing or a **primary-lymphedema/GLD gene panel** (CCBE1, FAT4, ADAMTS3, PIEZO1, GDF2, FLT4, VEGFC, FOXC2, SOX18, etc.) is appropriate. Sanger confirmation of candidate variants and parental segregation should follow ([PMID: 32472549](https://pubmed.ncbi.nlm.nih.gov/32472549/)). Chromosomal microarray/karyotype are used to exclude aneuploidy in hydrops workups but do not diagnose HKLLS1.

**Supportive laboratory tests:** hypoproteinemia, hypoalbuminemia, low immunoglobulins (hypogammaglobulinemia), lymphopenia, and **elevated stool alpha-1-antitrypsin** (marker of enteric protein loss) ([PMID: 40394495](https://pubmed.ncbi.nlm.nih.gov/40394495/), [PMID: 32629717](https://pubmed.ncbi.nlm.nih.gov/32629717/)).

**Imaging / functional:** **lymphoscintigraphy** demonstrates abnormal lymphatic drainage/tracer leakage; ultrasound/MRI/CT characterize effusions, ascites, and lymphatic malformations; prenatal ultrasound detects hydrops, subcutaneous edema, and effusions.

**Endoscopy / biopsy:** upper GI endoscopy shows dilated intestinal lymphatics; **duodenal/jejunal biopsy** confirms dilated mucosal/submucosal lymphatic vessels (lymphangiectasia).

**Clinical criteria / differential diagnosis:** Diagnosis is clinical (generalized lymphedema + lymphangiectasia + dysmorphism ± ID) plus molecular confirmation. **Differential diagnosis** includes other autosomal recessive GLD genes — **PIEZO1** (recessive GLD/hydrops, may have skeletal features; [PMID: 34371190](https://pubmed.ncbi.nlm.nih.gov/34371190/), [PMID: 26333996](https://pubmed.ncbi.nlm.nih.gov/26333996/), [PMID: 33227434](https://pubmed.ncbi.nlm.nih.gov/33227434/)) and **GDF2** (lymphatic dysplasia with hydrothorax and NIHF; [PMID: 32618121](https://pubmed.ncbi.nlm.nih.gov/32618121/)) — as well as FAT4 (HKLLS2 / Van Maldergem syndrome overlap; [PMID: 37551355](https://pubmed.ncbi.nlm.nih.gov/37551355/)) and ADAMTS3 (HKLLS3). Note that "Menke-Hennekam syndrome" (CREBBP/EP300, exon 30/31) is an **unrelated** dominant disorder despite the similar name.

**Screening:** No newborn screening exists. Cascade/carrier testing of at-risk relatives and prenatal/preimplantation genetic testing are appropriate once the familial variants are known.

### 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics exist for HKLLS1 specifically. Prognosis is driven by severity of PLE, effusions, and prenatal hydrops; the most severe (hydrops) cases can be lethal in utero or perinatally ([PMID: 30564329](https://pubmed.ncbi.nlm.nih.gov/30564329/)). For the related complication of primary intestinal lymphangiectasia, MCT treatment is associated with markedly lower mortality (3.7% vs 17.85% untreated) ([PMID: 19449286](https://pubmed.ncbi.nlm.nih.gov/19449286/)).
- **Morbidity:** Chronic lymphedema, recurrent effusions, malnutrition/growth impairment, recurrent infections from secondary immunodeficiency, and (in classic form) intellectual disability contribute substantial lifelong disability.
- **Complications:** protein-losing enteropathy, chylous effusions, recurrent pericardial effusion (potential tamponade risk), infections, edema.
- **Recovery potential:** The lymphatic dysplasia is structural and non-reversible; however, complications (PLE, effusions) are frequently controllable with supportive care, and some patients achieve complete symptom resolution of PLE on MCT diet ([PMID: 19449286](https://pubmed.ncbi.nlm.nih.gov/19449286/)).
- **Prognostic factors:** severity/onset of lymphatic dysplasia (prenatal hydrops = worst prognosis), degree of protein loss, presence of intellectual disability, and responsiveness to dietary therapy.

### 12. Treatment

**No curative or disease-specific therapy exists.** Management is **supportive and multidisciplinary** (Finding 9). Suggested NCIT concepts noted in brackets.

- **Dietary (cornerstone):** low-long-chain-triglyceride, high-protein diet with **medium-chain triglyceride (MCT)** supplementation [NCIT: dietary intervention / medium-chain triglyceride]. Improves PLE; 63% complete resolution vs 35.7% untreated ([PMID: 19449286](https://pubmed.ncbi.nlm.nih.gov/19449286/), [PMID: 20571826](https://pubmed.ncbi.nlm.nih.gov/20571826/), [PMID: 34587695](https://pubmed.ncbi.nlm.nih.gov/34587695/)). **Total parenteral nutrition** and **fat-soluble vitamin** supplementation when needed.
- **Pharmacologic:** **octreotide** [NCIT:C1611 Octreotide] when MCT fails ([PMID: 14723832](https://pubmed.ncbi.nlm.nih.gov/14723832/)); **diuretics** for effusions/edema; **albumin transfusions** for severe hypoproteinemia; **immunoglobulin replacement** (including subcutaneous) for symptomatic hypogammaglobulinemia ([PMID: 26934740](https://pubmed.ncbi.nlm.nih.gov/26934740/)).
- **Lymphedema care:** **complex decongestive therapy**, manual lymphatic drainage, and compression garments [NCIT: compression therapy / lymphedema therapy].
- **Surgical/interventional:** drainage of pleural/pericardial effusions and ascites; **pleurodesis**; surgical resection of localized/segmental lymphatic lesions ([PMID: 14723832](https://pubmed.ncbi.nlm.nih.gov/14723832/)).
- **Experimental / future directions:** Because the mechanism converges on the VEGFC–VEGFR3 axis, **VEGF-C–pathway–directed therapy** is a conceptual future target. Preclinical work shows small molecules (e.g., notoginsenoside R1 via cAMP/PKA/CREB) can upregulate VEGF-C and promote lymphangiogenesis ([PMID: 40020630](https://pubmed.ncbi.nlm.nih.gov/40020630/)); mTOR inhibitors (sirolimus) and VEGFR-3 inhibitors are used in other lymphatic malformations ([PMID: 40414533](https://pubmed.ncbi.nlm.nih.gov/40414533/)). None are established HKLLS1 therapies. No genotype-guided pharmacogenomic approach exists.

### 13. Prevention

- **Primary prevention:** Not possible for an established genetic disease. **Genetic counseling** for consanguineous couples and families with an affected child (25% recurrence risk) is central.
- **Secondary prevention:** **Prenatal testing** (WES/targeted variant testing) and **preimplantation genetic diagnosis** once familial CCBE1 variants are known; prenatal ultrasound surveillance for hydrops in at-risk pregnancies. **Cascade/carrier screening** of relatives; expanded carrier screening can retrospectively identify pathway-gene disease in families ([PMID: 37551355](https://pubmed.ncbi.nlm.nih.gov/37551355/)).
- **Tertiary prevention (complication prevention):** early MCT dietary therapy to prevent malnutrition and immunodeficiency; immunoglobulin replacement and infection prophylaxis; monitoring/drainage of effusions to prevent tamponade; nutritional and fat-soluble vitamin support.
- **Immunization / public health:** routine vaccination is advisable given secondary immunodeficiency risk, but no disease-specific immunization exists. No environmental public-health intervention applies.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** CCBE1 orthologs are highly conserved across humans (*Homo sapiens*, NCBI:txid9606), mouse (*Mus musculus*, txid10090), and zebrafish (*Danio rerio*, txid7955) ([PMID: 24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/)). Human **CCBE1** (NCBI Gene 147372); mouse *Ccbe1*; zebrafish *ccbe1*.
- **Natural disease in other species:** No well-documented naturally occurring HKLLS1-equivalent Mendelian disease in companion animals or wildlife is established; disease models are experimentally induced (see Section 15).
- **Comparative biology:** The VEGFC–CCBE1/ADAMTS3–VEGFR3 lymphangiogenesis mechanism is evolutionarily conserved across vertebrates, making cross-species models highly informative ([PMID: 27159393](https://pubmed.ncbi.nlm.nih.gov/27159393/), [PMID: 28129845](https://pubmed.ncbi.nlm.nih.gov/28129845/)).
- **Transmission / zoonosis:** Not applicable (genetic, non-transmissible).

### 15. Model Organisms

- **Zebrafish (*Danio rerio*):** The principal functional-validation model. *ccbe1* loss-of-function reproduces lymphatic sprouting defects; *ccbe1* genetically interacts with *vegfc* and *vegfr3 (flt4)*; patient CCBE1 variants (L27P, D104N, C98W) tested for loss of function; mature VEGFC overexpression rescues the phenotype ([PMID: 24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/), [PMID: 27345729](https://pubmed.ncbi.nlm.nih.gov/27345729/)). Zebrafish's superior live imaging has clarified the cellular sources (fibroblasts, neuronal/mural cells) of Vegfc-processing components ([PMID: 32483144](https://pubmed.ncbi.nlm.nih.gov/32483144/), [PMID: 35316177](https://pubmed.ncbi.nlm.nih.gov/35316177/)). **Resource:** ZFIN.
- **Mouse (*Mus musculus*):** *Ccbe1* is required for lymphatic development identically to *Vegfc* and *Adamts3*; biochemistry established that the ADAMTS3–CCBE1 complex forms independently of VEGFR3 and activates VEGFC (not VEGFD) ([PMID: 27159393](https://pubmed.ncbi.nlm.nih.gov/27159393/)); the N-terminal EGF domain of CCBE1 colocalizes pro-VEGFC with ADAMTS3 ([PMID: 28687807](https://pubmed.ncbi.nlm.nih.gov/28687807/)). **Inducible/conditional Ccbe1 deletion** impairs postnatal meningeal lymphatic development and macromolecule drainage and causes age-related regression ([PMID: 38141283](https://pubmed.ncbi.nlm.nih.gov/38141283/)). **Resources:** MGI, IMPC.
- **In vitro:** lymphatic endothelial cell cultures and transgenic reporter assays for VEGFC processing and VEGFR3 signaling.
- **Phenotype recapitulation:** Models faithfully reproduce the **lymphatic developmental defect** and the molecular mechanism (VEGFC maturation/VEGFR3 signaling). **Limitations:** they less directly model the full human syndrome (facial dysmorphism, intellectual disability, in-situ protein-losing enteropathy), and species differences in lymphatic anatomy exist.

---

## Mechanistic Model / Interpretation

The findings converge on a single, coherent, well-supported mechanistic narrative: **HKLLS1 is a lymphangiogenesis-signaling deficiency disease.** CCBE1 is not itself a growth factor or receptor; it is an accessory extracellular protein whose job is to make the ADAMTS3 protease efficiently convert inactive pro-VEGFC into the mature VEGFC ligand and to concentrate that reaction at the lymphatic endothelial cell surface. Remove CCBE1 function and the entire VEGFC → VEGFR3 → PI3K/ERK signaling axis is throttled at its source. Because this axis is *the* master pathway for lymphatic vessel growth, its partial failure produces a **generalized** — not localized — lymphatic dysplasia, which then manifests organ-by-organ: skin (lymphedema), gut (lymphangiectasia → protein-losing enteropathy → secondary immunodeficiency), and serosal/pulmonary lymphatics (effusions, and, at the extreme, prenatal hydrops).

This model explains the disease's key features. The **genetic heterogeneity** (CCBE1, ADAMTS3, FAT4) is unified by the pathway: CCBE1 and ADAMTS3 are literally partners in the same enzymatic reaction, so mutating either produces the same phenotype. The **variable expressivity** — from a mild lymphatic dysplasia to lethal recurrent hydrops — is consistent with a dosage-sensitive signaling pathway in which residual VEGFC-activation capacity (variant-specific) sets the severity. The **secondary immunodeficiency** is fully accounted for as a downstream leak phenomenon, not a primary immune-cell defect, which correctly predicts that reducing enteric lymph loss (MCT diet) is the causal therapy rather than immunosuppression. And the **therapeutic logic** follows directly: absent a way to restore CCBE1/VEGFC signaling in patients, the only available levers are downstream and symptomatic — dietary reduction of lymphatic load, protein/immunoglobulin replacement, and mechanical management of edema and effusions.

The most important conceptual gap between the molecular model and the clinical picture is the **non-lymphatic features** — facial dysmorphism and intellectual disability — which are not obviously explained by lymphatic signaling and remain mechanistically inferred rather than demonstrated.

| Layer | Upstream ← → Downstream |
|---|---|
| Genetic lesion | Biallelic LoF **CCBE1** variants (upstream initiator) |
| Biochemical | ↓ ADAMTS3–CCBE1 complex → ↓ pro-VEGFC cleavage → ↓ mature VEGFC |
| Signaling | ↓ VEGFR3 (FLT4) activation → ↓ PI3K & Ras/ERK |
| Cellular | ↓ LEC proliferation/migration/survival |
| Tissue | Generalized lymphatic dysplasia / lymphangiectasia |
| Clinical (downstream) | Lymphedema; PLE → secondary immunodeficiency; effusions; hydrops; dysmorphism; ID |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [24523457](https://pubmed.ncbi.nlm.nih.gov/24523457/) | *Ccbe1 regulates Vegfc-mediated induction of Vegfr3 signaling* | Core mechanism: CCBE1 upregulates mature VEGFC; rescue in zebrafish; ERK impaired without Ccbe1; conservation. Supports F1, F4, F5. |
| [27345729](https://pubmed.ncbi.nlm.nih.gov/27345729/) | *Expanding the genotypic spectrum of CCBE1 mutations* | AR inheritance; ~25% CCBE1; patient variants are LoF in zebrafish. Supports F1, F2, F8, F9. |
| [30450763](https://pubmed.ncbi.nlm.nih.gov/30450763/) | *ADAMTS3 loss-of-function in HKLLS* | Three-gene heterogeneity; CCBE1→ADAMTS3→VEGFC axis. Supports F2, F5. |
| [28985353](https://pubmed.ncbi.nlm.nih.gov/28985353/) | *Loss of ADAMTS3 activity causes HKLLS3* | Establishes ADAMTS3 as HKLLS3. Supports F2. |
| [41992670](https://pubmed.ncbi.nlm.nih.gov/41992670/) | *Biallelic FAT4 splice variant causes HKLLS2* | Confirms FAT4 (HKLLS2) and the CCBE1/FAT4/ADAMTS3 model. Supports F2. |
| [27159393](https://pubmed.ncbi.nlm.nih.gov/27159393/) | *Proteolytic activation ... VEGFC and VEGFD* | ADAMTS3–CCBE1 complex activates VEGFC. Supports F5. |
| [28687807](https://pubmed.ncbi.nlm.nih.gov/28687807/) | *CCBE1 N-terminal domain and VEGF-C activation* | CCBE1 colocalizes pro-VEGFC with ADAMTS3; enhances cleavage. Supports F4, F5. |
| [40046235](https://pubmed.ncbi.nlm.nih.gov/40046235/) | *Regulation of VEGFR3 signaling in LECs* | Defines PI3K/Ras cascades; links VEGFR3 dysfunction to lymphatic disease. Supports F4. |
| [38141283](https://pubmed.ncbi.nlm.nih.gov/38141283/) | *CCBE1 regulates meningeal lymphatics* | Inducible Ccbe1 deletion impairs lymphatic development/maintenance. Supports F5. |
| [32629717](https://pubmed.ncbi.nlm.nih.gov/32629717/) | *Intestinal lymphangiectasia — CCBE1* | Clinical phenotype: lymphedema, dysmorphism, PLE labs. Supports F3, F6, F7. |
| [31633297](https://pubmed.ncbi.nlm.nih.gov/31633297/) | *FBXL7 — novel form of Hennekam* | Core clinical tetrad; candidate 4th gene. Supports F3, F2. |
| [25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/) | *Mild form of Hennekam — CCBE1 (C98W)* | Phenotypic variability; consanguinity. Supports F3, F8. |
| [26686525](https://pubmed.ncbi.nlm.nih.gov/26686525/) | *Multiplex kindred — CCBE1* | Consanguinity; variant with retained protein expression. Supports F8. |
| [26934740](https://pubmed.ncbi.nlm.nih.gov/26934740/) | *Secondary hypogammaglobulinemia (Waldmann's)* | PLE → lymphopenia, hypoalbuminemia, hypogammaglobulinemia. Supports F6. |
| [30564329](https://pubmed.ncbi.nlm.nih.gov/30564329/) | *Novel mutation — WES for recurrent hydrops* | WES diagnoses HKLLS1; prenatal hydrops. Supports F7. |
| [26333996](https://pubmed.ncbi.nlm.nih.gov/26333996/) | *PIEZO1 recessive GLD with NIHF* | Defines GLD spectrum & prenatal hydrops; differential dx. Supports F7. |
| [40394495](https://pubmed.ncbi.nlm.nih.gov/40394495/) | *Recurrent pericardial effusion — HKLLS* | Supportive diagnostics (albumin, stool α1-antitrypsin); pericardial effusion. Supports F3, F7. |
| [19449286](https://pubmed.ncbi.nlm.nih.gov/19449286/) | *MCT for primary intestinal lymphangiectasia* | Quantifies MCT benefit and mortality reduction. Supports F9. |
| [20571826](https://pubmed.ncbi.nlm.nih.gov/20571826/) | *Protein-losing enteropathy in children* | MCT diet as standard PLE management. Supports F9. |
| [38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/) | *Newfound features — Hennekam ("51st case")* | Ultra-rare scale. Supports F8. |
| [34234628](https://pubmed.ncbi.nlm.nih.gov/34234628/) | *In silico deleterious CCBE1 nsSNPs* | Predicts additional pathogenic variants/residues. Supports F1 (genetics). |

Evidence spans **human clinical** case reports/series (e.g., PMIDs 32629717, 25925991, 26686525, 40394495, 30564329, 36748365), **model-organism** functional studies (zebrafish/mouse; PMIDs 24523457, 27345729, 27159393, 38141283), and **in vitro/biochemical** work (PMIDs 28687807, 27159393), with **computational** prediction (PMID 34234628).

---

## Limitations and Knowledge Gaps

1. **Ultra-rare, case-report-based evidence.** With only ~50–60 total Hennekam patients reported (a minority genotyped as CCBE1), quantitative frequencies, penetrance/expressivity estimates, survival statistics, and prevalence figures are imprecise or unavailable. Phenotype frequencies in Section 3 are qualitative, not derived from a systematic cohort.
2. **Unexplained non-lymphatic features.** The mechanistic link from CCBE1/VEGFC signaling to **facial dysmorphism** and **intellectual disability** is inferred, not demonstrated. Whether these reflect craniofacial lymphatic effects, a moonlighting CCBE1 function, or secondary metabolic/nutritional effects is unknown.
3. **Genotype–phenotype correlation is weak.** It is not established which CCBE1 variants predict severe (hydrops) vs mild disease; the concept that residual VEGFC-activation capacity sets severity is plausible but not quantitatively demonstrated.
4. **No approved targeted therapy.** VEGFC-pathway-directed treatment is conceptually attractive but entirely preclinical; efficacy/safety in HKLLS1 patients is unknown.
5. **Model limitations.** Zebrafish/mouse models reproduce the lymphatic developmental defect and molecular mechanism but do not fully capture the syndromic human phenotype (dysmorphism, ID, in-situ PLE).
6. **Ontology term verification needed.** The suggested HPO/GO/CL/UBERON/NCIT/CHEBI identifiers above are indicative and should be reconciled against the current ontology releases before knowledge-base ingestion.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype–phenotype database.** Aggregate all reported CCBE1 (and FAT4/ADAMTS3) HKLLS variants with paired phenotype severity into a curated table; correlate variant type/domain (e.g., conserved cysteines, EGF vs collagen domains) with severity and prenatal-hydrops risk.
2. **Functional severity assay.** Systematically test additional CCBE1 patient/candidate variants (including in-silico-predicted G330E, C102S, C174R, G107D) in the zebrafish rescue assay and quantitative VEGFC-processing biochemistry to build a variant-to-residual-activity map that could inform prognosis.
3. **VEGFC-pathway therapeutic proof-of-concept.** Evaluate VEGF-C/VEGFR3 agonism (e.g., recombinant mature VEGFC or small molecules that upregulate VEGF-C) in Ccbe1-deficient mouse/zebrafish models for rescue of lymphatic function and PLE-equivalent phenotypes.
4. **Natural-history / registry study.** Establish an international HKLLS registry to capture survival, complication rates, effusion recurrence, growth, immune outcomes, and MCT-diet response prospectively — currently the single greatest evidence gap.
5. **Mechanism of non-lymphatic features.** Investigate CCBE1/VEGFC-pathway effects on craniofacial and neurodevelopment (e.g., conditional models, patient iPSC-derived neural cells) to explain dysmorphism and intellectual disability.
6. **Diagnostic pathway standardization.** Define a formal diagnostic algorithm (GLD gene panel → WES/WGS → functional confirmation) and prenatal work-up (recurrent hydrops → exome) as a clinical guideline, with elevated stool α1-antitrypsin and lymphoscintigraphy as supportive first-line tests.
7. **Ontology verification.** Reconcile all suggested HPO/GO/CL/UBERON/NCIT/CHEBI terms against current ontology releases prior to knowledge-base ingestion.

---

*Report compiled from a 5-iteration autonomous investigation: 9 confirmed findings, 62 papers reviewed. Evidence sources span human clinical case reports/series, model-organism (zebrafish, mouse) functional studies, and in vitro biochemistry, as noted per claim.*


## Artifacts

- [OpenScientist final report](Hennekam_Lymphangiectasia-Lymphedema_Syndrome_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hennekam_Lymphangiectasia-Lymphedema_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 37 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001888` (1 mention) - the report calls it "Lymphopenia"; HP calls it **Decreased total lymphocyte count**, and lists "Lymphopenia" among its other names
- `GO:0004175` (1 mention) - the report calls it "endopeptidase activity, for ADAMTS3"; GO calls it **endopeptidase activity**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

35 of 37 terms resolved to a current term; the rest could not be looked up either way.