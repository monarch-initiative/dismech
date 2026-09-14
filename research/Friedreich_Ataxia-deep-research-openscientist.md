---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T10:32:13.762575'
end_time: '2026-09-07T10:51:40.007427'
duration_seconds: 1166.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Friedreich Ataxia
  mondo_id: MONDO:0100339
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
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 20
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 11
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0003390
    reported_labels:
    - Impaired vibration sense
    ontology_label: Sensory axonal neuropathy
  labels_variant: 3
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
  path: Friedreich_Ataxia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Friedreich_Ataxia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Friedreich Ataxia
- **MONDO ID:** MONDO:0100339 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Friedreich Ataxia** covering all of the
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

# Friedreich Ataxia: Comprehensive Disease Characteristics Report

**Disease:** Friedreich Ataxia (FRDA) · **MONDO:** MONDO:0100339 · **Category:** Mendelian (autosomal recessive)
**OMIM:** #229300 · **Orphanet:** ORPHA:95 · **ICD-10:** G11.1 · **ICD-11:** 8A03.10 · **MeSH:** D005621 · **Gene:** *FXN* (HGNC:3951), 9q21.11

---

## Summary

Friedreich Ataxia (FRDA) is the most common inherited ataxia in populations of European descent and the prototypical mitochondrial iron–sulfur (Fe-S) disorder of nuclear-genetic origin. It is an autosomal recessive, progressive, multisystem neurodegenerative disease caused in ~96–98% of patients by a **biallelic GAA·TTC trinucleotide-repeat expansion in intron 1 of the *FXN* gene** on chromosome 9q21.11; the remainder are compound heterozygotes carrying one expansion and one point mutation or deletion. The expanded repeat adopts non-B DNA structures and induces repressive heterochromatin that impairs transcriptional elongation, silencing *FXN* and producing a deficiency of the mitochondrial protein **frataxin**. Because frataxin is essential for Fe-S cluster biosynthesis, its loss cripples the electron transport chain and Fe-S–dependent enzymes (e.g., aconitase), causing bioenergetic failure, secondary mitochondrial iron accumulation, and oxidative stress.

This molecular lesion selectively injures a characteristic set of tissues: the **dorsal root ganglia (DRG)** — the primary lesion — together with dorsal columns, spinocerebellar and corticospinal tracts, the **cerebellar dentate nucleus**, the **myocardium**, and **pancreatic islet β-cells**. The clinical result is a stereotyped phenotype of progressive afferent and cerebellar ataxia, dysarthria, lower-limb areflexia, extensor plantar responses, loss of proprioception/vibration sense, and frequently nystagmus, dysphagia, optic atrophy, and hearing loss, accompanied by **hypertrophic cardiomyopathy** (the leading cause of death), **scoliosis**, **pes cavus**, and **diabetes mellitus**. Disease severity is governed largely by residual frataxin level: the length of the smaller GAA allele (GAA1) inversely predicts age of onset (accounting for ~50% of the variance) and correlates with cardiomyopathy and diabetes risk.

FRDA is relentlessly progressive, with early-onset patients losing ambulation a median of ~11.5 years after symptom onset and dying most often of cardiac causes in their 30s. Management remains predominantly multidisciplinary and symptomatic; **omaveloxolone (SKYCLARYS)**, an Nrf2 activator approved by the FDA (2023) and EMA, is the first and only disease-modifying therapy, producing modest slowing of neurological decline. AAV-based *FXN* gene replacement, CRISPR/epigenetic reactivation, and frataxin-stabilizing approaches are advancing through preclinical and early clinical development.

---

## Key Findings

### 1. Genetic cause: biallelic intronic GAA expansion in *FXN* (F001)

Most FRDA patients are **homozygous for a GAA trinucleotide repeat expansion in intron 1 of *FXN*** (9q21.11). The expansion silences the gene epigenetically and reduces frataxin. Approximately 96–98% of patients are homozygous for the expansion; the remainder are compound heterozygous (expansion on one allele + point mutation or deletion on the other). Inheritance is autosomal recessive.

> *"large intronic guanine-adenine-adenine (GAA) tracts at the frataxin (FXN) gene locus induce heterochromatin formation, impaired transcriptional elongation, and reduced FXN expression, driving progressive neurodegeneration and cardiomyopathy"* — [PMID: 42295329](https://pubmed.ncbi.nlm.nih.gov/42295329/)

> *"FRDA is caused by an expansion of GAA repeats in the first intron of the frataxin (FXN) gene. The expansion disrupts transcription of FXN, resulting in significantly decreased FXN expression in FRDA patients' tissues."* — [PMID: 41514384](https://pubmed.ncbi.nlm.nih.gov/41514384/)

> *"Most patients have a homozygous GAA repeat expansion in the FXN gene, resulting in a deficiency of the mitochondrial protein frataxin."* — [PMID: 40541211](https://pubmed.ncbi.nlm.nih.gov/40541211/)

### 2. Core biochemical defect: impaired Fe-S cluster biosynthesis (F002)

Frataxin is an evolutionarily conserved mitochondrial matrix protein required for **iron–sulfur (Fe-S) cluster biosynthesis**, which is essential for the electron transport chain complexes I–III and many metabolic enzymes (e.g., aconitase). Frataxin deficiency reduces ATP production, causes **mitochondrial iron accumulation** that exacerbates **oxidative stress**, and disrupts glucose and fatty-acid oxidation.

> *"Frataxin is involved in biosynthesis of iron-sulfur (Fe-S) clusters, which are critical for the function of the electron transport chain and many metabolic enzymes. Frataxin deficiency leads to reduced energy production and accumulation of iron in mitochondria that exacerbates oxidative stress."* — [PMID: 41514384](https://pubmed.ncbi.nlm.nih.gov/41514384/)

> *"Frataxin deficiency impairs key mitochondrial metabolic enzymes, leading to widespread mitochondrial dysfunction with disrupted glucose and fatty acid oxidation."* — [PMID: 41447358](https://pubmed.ncbi.nlm.nih.gov/41447358/)

### 3. Epigenetic silencing mechanism (F016)

The large intronic GAA·TTC tract adopts non-B DNA structures (triplex/"sticky DNA" and R-loops) and nucleates **repressive heterochromatin** (increased H3K9me2/3, DNA methylation, HDAC-associated histone hypoacetylation) at the *FXN* locus, impairing RNA polymerase II elongation and reducing *FXN* mRNA. This mechanism is the rationale for epigenetic reactivation therapies (class I-selective benzamide HDAC inhibitors, high-dose nicotinamide, anti-gene oligonucleotides, gene-targeted chimeras) and splice-modulation to boost the extramitochondrial FXN-E isoform.

> *"class I-selective benzamide histone deacetylase inhibitors and high-dose nicotinamide, to emerging locus-targeted platforms such as anti-gene oligonucleotides and gene-targeted chimera small molecules"* — [PMID: 42295329](https://pubmed.ncbi.nlm.nih.gov/42295329/)

### 4. Multisystem disorder; cardiomyopathy is the leading cause of death (F003, F007)

FRDA affects the nervous system, heart, musculoskeletal system, and metabolism. **Neurological deficits are the only feature uniformly present in all patients**, while extraneural manifestations vary. Onset is typically in adolescence but ranges from early childhood to late adulthood.

> *"Common extraneural manifestations include cardiomyopathy, which is the most common cause of mortality, and also scoliosis and diabetes."* — [PMID: 40541211](https://pubmed.ncbi.nlm.nih.gov/40541211/)

> *"neurological deficits are the only feature uniformly observed in all FRDA patients"* — [PMID: 41447358](https://pubmed.ncbi.nlm.nih.gov/41447358/)

**Core phenotype and suggested HPO terms:**

| Phenotype | HPO term | Frequency |
|---|---|---|
| Gait ataxia | HP:0002066 | ~universal |
| Limb ataxia | HP:0001251 | ~universal |
| Dysarthria | HP:0001260 | very frequent |
| Lower-limb areflexia | HP:0001284 | ~universal |
| Extensor plantar response (Babinski) | HP:0003487 | very frequent |
| Impaired proprioception | HP:0010831 | ~universal |
| Impaired vibration sense | HP:0003390 | ~universal |
| Nystagmus | HP:0000639 | frequent |
| Dysphagia | HP:0002015 | frequent |
| Optic atrophy | HP:0000648 | subset |
| Sensorineural hearing loss | HP:0000407 | subset |
| Hypertrophic cardiomyopathy | HP:0001639 | frequent (major mortality driver) |
| Scoliosis | HP:0002650 | frequent |
| Pes cavus | HP:0001761 | frequent |
| Diabetes mellitus | HP:0000819 | subset (~10–30%) |

### 5. Genotype–phenotype correlation (F005)

In 67 FRDA patients (48 Italian families), *FXN* intron-1 GAA alleles ranged **201–1,186 repeats** with no overlap with the normal range and a peak at 800–1,000. Both allele lengths inversely correlated with age at onset; the **smaller allele (GAA1) best predicted onset, accounting for ~50% of variance**. Mean allele length was significantly higher in patients with diabetes and cardiomyopathy. An independent cohort confirmed inverse correlation of GAA length with onset age, disease duration, and cardiomyopathy. The repeat is meiotically unstable (median variation ~150 repeats), providing a basis for genetic anticipation.

> *"The lengths of both larger and smaller alleles in each patient inversely correlated with age at onset of the disorder. Smaller alleles showed the best correlation, accounting for approximately 50% of the variation of age at onset. Mean allele length was significantly higher in patients with diabetes and in those with cardiomyopathy."* — [PMID: 8751856](https://pubmed.ncbi.nlm.nih.gov/8751856/)

> *"Genotype-phenotype correlation analyses in FA patients have evidenced an inverse relationship between GAA repeat expansion length and age of onset, disease duration, and presence of cardiomyopathy."* — [PMID: 11719273](https://pubmed.ncbi.nlm.nih.gov/11719273/)

### 6. Residual frataxin level (not mutation type) determines phenotype (F009)

Matched neuropathology of compound heterozygous versus homozygous FRDA showed **similar cardiac and neuropathological lesions**. Frataxin in heart and dentate nucleus of all cases was ≤10 ng/g wet weight (ELISA detection limit) versus normal dentate 126 ± 43 ng/g and normal heart 266 ± 92 ng/g. The pathologic phenotype is set by residual frataxin, not the specific mutation — explaining why complete loss (embryonic lethal) is never seen in patients.

> *"The pathologic phenotype in homozygous and compound heterozygous FA is determined by residual frataxin levels rather than unique mutations."* — [PMID: 28789479](https://pubmed.ncbi.nlm.nih.gov/28789479/)

### 7. Neuropathology: dorsal root ganglia and dentate nucleus (F008)

The **primary lesion is the DRG**: initial hypoplasia followed by progressive atrophy, producing thinning of dorsal roots, degeneration of dorsal columns, transsynaptic atrophy of Clarke column and dorsal spinocerebellar fibers, atrophy of gracile/cuneate nuclei, and sensory neuropathy. The **dentate nucleus** shows selective atrophy of large glutamatergic neurons and grumose degeneration of GABAergic corticonuclear terminals. Systemic involvement of myocardium and pancreatic islets confirms it as a systemic disease.

> *"Progressive destruction of dorsal root ganglia accounts for thinning of dorsal roots, degeneration of dorsal columns, transsynaptic atrophy of nerve cells in Clarke column and dorsal spinocerebellar fibers, atrophy of gracile and cuneate nuclei, and neuropathy of sensory nerves."* — [PMID: 23334592](https://pubmed.ncbi.nlm.nih.gov/23334592/)

> *"The lesion of the dentate nucleus consists of progressive and selective atrophy of large glutamatergic neurons and grumose degeneration of corticonuclear synaptic terminals that contain γ-aminobutyric acid (GABA)."* — [PMID: 23334592](https://pubmed.ncbi.nlm.nih.gov/23334592/)

> *"Involvement of the myocardium and pancreatic islets of Langerhans indicates that it is also a systemic disease."* — [PMID: 23859341](https://pubmed.ncbi.nlm.nih.gov/23859341/)

**Anatomical/cellular ontology terms:** dorsal root ganglion (UBERON:0000044); dorsal column (UBERON:0002211); spinocerebellar tract (UBERON:0004704); corticospinal tract (UBERON:0002460); dentate nucleus (UBERON:0002439); myocardium (UBERON:0002349); pancreatic islet (UBERON:0000006). Cell types: sensory neuron (CL:0000101), cardiac muscle cell (CL:0000746), pancreatic β-cell (CL:0000169), cerebellar dentate glutamatergic neurons. Subcellular: mitochondrion (GO:0005739); mitochondrial matrix (GO:0005759); Fe-S cluster assembly (GO:0016226).

### 8. Progression and prognosis (F006, F010)

In the FA-COMS natural history cohort (1,021 patients, 4,606 visits), FRDA causes progressive loss of coordination and balance leading to **loss of ambulation (LoA) in nearly all patients**. Early-onset (<15 y) patients become fully wheelchair-dependent at a median of **11.5 years** (IQR 8.6–16.2) after first symptoms. A characteristic sequence of loss of FARS stance/balance functions predicts future LoA risk.

> *"Early onset FRDA patients (<15y of age) typically become fully wheelchair dependent at a median of 11.5y (25th, 75th percentiles 8.6y, 16.2y) after the onset of first symptoms."* — [PMID: 31938785](https://pubmed.ncbi.nlm.nih.gov/31938785/)

A Brazilian cohort (n=151; 24 deaths, 15.9%) found **mean age at death 33 ± 10.7 years**; among 12 known causes, cardiac in 7, pulmonary in 3, diabetic ketoacidosis in 1, sepsis in 1. Shorter life expectancy was associated with male sex (54.0 vs 56.8 y, p=0.03), classical vs late onset (52.2 vs 71.0 y, p<0.01), and cardiomyopathy (50.8 vs 65.0 y, p<0.01).

> *"Male sex, early onset and presence of cardiomyopathy are negative survival prognostic markers."* — [PMID: 41273607](https://pubmed.ncbi.nlm.nih.gov/41273607/)

### 9. Epidemiology (F011)

FRDA is worldwide the **most common form of hereditary ataxia**. Prevalence in populations of European descent is ~1 in 30,000–50,000 (~2–4 per 100,000), carrier frequency ~1 in 60–100. Strong regional/founder variation exists: in Finland carrier frequency was only 1/500 (birth incidence ~1/10⁶), because pre-mutation "reservoir" alleles (28–36 GAA) at the upper end of normal variation were absent. A single major universal risk haplotype underlies most patients; the disease is essentially restricted to European, North African, Middle Eastern, and Indian (Indo-European) populations and rare in sub-Saharan African, East Asian, and Amerindian populations.

> *"Worldwide it is considered to be the most common form of hereditary ataxia, but it is infrequently encountered in Finland."* — [PMID: 11810294](https://pubmed.ncbi.nlm.nih.gov/11810294/)

> *"Alleles in the uppermost end of the normal variation (28-36 GAA) were totally missing in the Finnish population."* — [PMID: 11810294](https://pubmed.ncbi.nlm.nih.gov/11810294/)

### 10. Diagnosis (F014)

Hallmark clinical features prompting diagnosis: progressive afferent and cerebellar ataxia, dysarthria, impaired vibration/proprioception, absent lower-limb reflexes, pyramidal weakness, scoliosis, foot deformity, and cardiomyopathy. Confirmation is molecular — detection of biallelic GAA expansion in *FXN* intron 1 by triplet-repeat-primed PCR / fluorescent amplicon-length PCR (long-read sequencing for accurate sizing); compound heterozygotes require *FXN* sequencing. Supportive tests: nerve conduction studies show absent/reduced sensory nerve action potentials with preserved motor conduction (axonal sensory neuronopathy); ECG/echocardiography detect concentric hypertrophic (later dilated) cardiomyopathy; spinal MRI shows cervical cord atrophy with early sparing of the cerebellum.

> *"The hallmark clinical features of FRDA include progressive afferent and cerebellar ataxia, dysarthria, impaired vibration sense and proprioception, absent tendon reflexes in lower limbs, pyramidal weakness, scoliosis, foot deformity and cardiomyopathy."* — [PMID: 25928624](https://pubmed.ncbi.nlm.nih.gov/25928624/)

**Differential diagnosis:** ataxia with vitamin E deficiency (AVED), ataxia-telangiectasia, ARSACS, ataxia with oculomotor apraxia (AOA1/2), POLG-related ataxia, and FGF14 (SCA27B) GAA-repeat ataxia.

> *"In the case of recessive disease, a stepwise diagnostic work-up is recommended, including both biochemical markers and targeted genetic testing, particularly aimed at Friedreich's ataxia, ataxia telangiectasia, ataxia due to vitamin E deficiency"* — [PMID: 24418350](https://pubmed.ncbi.nlm.nih.gov/24418350/)

### 11. First disease-modifying therapy: omaveloxolone (F004)

In the pivotal **MOXIe phase 2 trial (NCT02255435)**, 150 mg/day omaveloxolone vs placebo (ages 16–40, mFARS 20–80) produced a placebo-corrected mFARS difference of **−2.40 ± 0.96 at 48 weeks (p = 0.014)** — omaveloxolone −1.55 ± 0.69 vs placebo +0.85 ± 0.64. Main adverse effects: transient reversible aminotransferase elevations, headache, nausea, fatigue. FDA (2023) and EMA approval followed (SKYCLARYS; NCIT: omaveloxolone).

> *"Changes from baseline in mFARS scores in omaveloxolone (-1.55 ± 0.69) and placebo (0.85 ± 0.64) patients showed a difference between treatment groups of -2.40 ± 0.96 (p = 0.014)."* — [PMID: 33068037](https://pubmed.ncbi.nlm.nih.gov/33068037/)

> *"Omaveloxolone, an Nrf2 activator, improves mitochondrial function, restores redox balance, and reduces inflammation in models of FA."* — [PMID: 33068037](https://pubmed.ncbi.nlm.nih.gov/33068037/)

### 12. Management and experimental therapeutics (F015, F013)

Prior to omaveloxolone, **no proven treatment could slow progression**; care is multidisciplinary and symptomatic (Corben 2014; 146 recommendations, 62% expert opinion). Components: physiotherapy, occupational and speech therapy; mobility aids/wheelchair; surveillance and pharmacologic/device management of cardiomyopathy and arrhythmia (ACE inhibitors/beta-blockers; HRS arrhythmia consensus); diabetes screening/treatment; orthopedic management of scoliosis (bracing, spinal fusion) and pes cavus; treatment of spasticity, bladder dysfunction, pain, and sensory complications. Idebenone, high-dose CoQ10/vitamin E, and deferiprone (iron chelation) have been trialed but are not established as disease-modifying.

> *"At present there is no proven treatment that can slow the progression or eventual outcome of this life-shortening condition."* — [PMID: 25928624](https://pubmed.ncbi.nlm.nih.gov/25928624/)

**Gene therapy proof-of-concept:** A single dose of AAV9-hFXN (6×10¹¹ v.p.) **more than doubled lifespan** of conditional *Fxn*-KO mice and preserved cardiac systolic function, with frataxin detected in heart, brain, muscle, kidney, and liver. AAV2-based intravitreal *FXN* supplementation partially preserved retinal structure/function in ocular-phenotype models.

> *"A single administration of the AAV9-hFXN at 6 × 10(11) v.p. more than doubled the life of these mice."* — [PMID: 26015982](https://pubmed.ncbi.nlm.nih.gov/26015982/)

> *"Gene supplementation via intravitreal injection of a novel AAV2-based capsid carrying FXN partially preserved retinal structure and/or function in both models, establishing proof of concept for this therapeutic strategy."* — [PMID: 41137390](https://pubmed.ncbi.nlm.nih.gov/41137390/)

### 13. Animal and cellular models (F012)

Complete *Fxn* knockout is **embryonic lethal** (frataxin essential for development), which is why patients always retain residual frataxin. Conditional KOs (MCK-Cre striated muscle; NSE-Cre neuron/cardiac) reproduce cardiac hypertrophy without skeletal-muscle involvement, large-sensory-neuron dysfunction sparing small sensory/motor neurons, and deficient complexes I–III and aconitase; critically, **intramitochondrial iron accumulation occurs AFTER Fe-S enzyme inactivation and pathology onset**, establishing enzyme dysfunction as upstream of iron deposition. Humanized GAA-repeat YAC transgenic models (YG8R/YG22R) show reduced frataxin, decreased aconitase, oxidative stress, DRG vacuolation, and rotarod deficits. iPSC-derived neurons, cardiomyocytes, microglia, and organoids provide human isogenic in-vitro systems.

> *"cardiac hypertrophy without skeletal muscle involvement, large sensory neuron dysfunction without alteration of the small sensory and motor neurons, and deficient activities of complexes I-III of the respiratory chain and of the aconitases ... time-dependent intramitochondrial iron accumulation ... which occurs after onset of the pathology and after inactivation of the Fe-S-dependent enzymes."* — [PMID: 11175786](https://pubmed.ncbi.nlm.nih.gov/11175786/)

> *"The resultant FRDA mice that express only human-derived frataxin show comparatively reduced levels of frataxin mRNA and protein expression, decreased aconitase activity, and oxidative stress, leading to progressive neurodegenerative and cardiac pathological phenotypes."* — [PMID: 16919418](https://pubmed.ncbi.nlm.nih.gov/16919418/)

---

## Section-by-Section Details

### 1. Disease Information
FRDA is an autosomal recessive, progressive, multisystem neurodegenerative disorder combining a neurological ataxic syndrome with cardiac, skeletal, and metabolic features. **Identifiers:** MONDO:0100339, OMIM #229300, Orphanet ORPHA:95, ICD-10 G11.1, ICD-11 8A03.10, MeSH D005621. **Synonyms:** Friedreich's ataxia, FRDA, FA, spinocerebellar degeneration (historical), hereditary spinal ataxia. Information here derives from aggregated disease-level resources (OMIM, Orphanet, HPO), natural history registries (FA-COMS), and primary literature — not individual EHR.

### 2. Etiology
**Causal factor:** biallelic loss-of-function of *FXN* via intronic GAA expansion (or expansion + point mutation/deletion). **Genetic risk:** homozygosity for the expanded GAA allele; larger GAA1 length increases severity/earlier onset. **Modifiers:** proposed roles for oxidative-stress and iron-handling genes; residual frataxin level is the dominant determinant of phenotype (F009). **Environmental risk/protective factors:** none established as causal — FRDA is essentially fully genetically determined; no dietary, occupational, or infectious triggers are recognized. **Gene–environment interaction:** limited; oxidative-stress exposure could theoretically aggravate an already compromised redox system, but this is not clinically validated. **Protective genetics:** absence of upper-normal "reservoir" alleles (28–36 GAA) in a population reduces disease incidence (Finland; F011).

### 3. Phenotypes
See the HPO table above (Finding 4). Onset is typically adolescent (childhood to late-adult range); severity is variable and largely GAA1-dependent; progression is chronic and relentless. Quality-of-life impact is severe and cumulative: progressive loss of independent mobility, communication (dysarthria), swallowing, and — with cardiac/diabetic complications — survival. Afferent/sensory ataxia and cerebellar dysfunction jointly drive disability.

### 4. Genetic/Molecular Information
**Causal gene:** *FXN* (frataxin), HGNC:3951, 9q21.11. **Variant class:** intronic GAA·TTC repeat expansion (structural/repeat-expansion; pathogenic per ACMG when biallelic), plus rare pathogenic point mutations (missense, nonsense, splice-site) and deletions in compound heterozygotes. **Functional consequence:** loss of function via transcriptional silencing (not a toxic protein gain-of-function, distinguishing it from coding CAG disorders like Huntington's). **Allele ranges:** normal <~33; pre-mutation ~34–65; pathogenic ~66 to >1,000 (patient peak 800–1,000; F005). **Epigenetics:** heterochromatin marks (H3K9me2/3), DNA methylation, histone hypoacetylation at *FXN* (F016). No recurrent aneuploidy/translocation.

### 5. Environmental Information
No environmental, lifestyle, or infectious agents are established causes or triggers of FRDA. It is a monogenic disease. Iron intake/chelation modulate downstream biochemistry but do not cause disease.

### 6. Mechanism / Pathophysiology — ordered causal chain

```
1. Biallelic GAA·TTC expansion in FXN intron 1 (or expansion + point mutation)
        │  leads to
2. Non-B DNA structures (triplex/"sticky DNA", R-loops) + repressive heterochromatin
   (H3K9me2/3, DNA methylation, histone hypoacetylation)
        │  results in
3. Impaired RNA Pol II transcriptional elongation → reduced FXN mRNA → frataxin deficiency
        │  leads to
4. Impaired mitochondrial Fe-S cluster biosynthesis
        │  results in (branch)
   ├─► 5a. Deficient ETC complexes I–III + aconitase → bioenergetic failure
   ├─► 5b. Mitochondrial iron accumulation (occurs AFTER Fe-S enzyme loss — model-demonstrated)
   └─► 5c. Increased ROS / oxidative stress + lipid peroxidation
        │  converge to cause
6. Selective cellular vulnerability: DRG proprioceptive neurons, dentate glutamatergic
   neurons, cardiomyocytes, pancreatic β-cells (+ microglial dysfunction, iPSC-inferred)
        │  leads to
7. Tissue lesions: DRG atrophy → dorsal column/spinocerebellar/corticospinal degeneration;
   dentate nucleus atrophy; myocardial hypertrophy/fibrosis; islet β-cell loss
        │  results in
8. Clinical manifestations: afferent + cerebellar ataxia, areflexia, pyramidal signs,
   dysarthria, sensory loss; hypertrophic cardiomyopathy; diabetes; scoliosis; pes cavus
        │  progresses to
9. Loss of ambulation (~11.5 y post-onset, early onset) and death (mean ~33–38 y),
   most often from cardiac causes
```

**Upstream vs downstream:** steps 1–3 (genetic/epigenetic silencing) are upstream; frataxin deficiency (4) is the pivotal node; Fe-S enzyme failure (5a) precedes iron accumulation (5b) per mouse-model ordering (F012). **Molecular pathways/GO terms:** iron-sulfur cluster assembly (GO:0016226), mitochondrial electron transport chain (GO:0022900), cellular response to oxidative stress (GO:0034599), tricarboxylic acid cycle (aconitase; GO:0006099), Nrf2/KEAP1 antioxidant response (drug target). **Immune involvement:** iPSC studies suggest intrinsic microglial mitochondrial/iron/lysosomal defects driving a pro-inflammatory, neurotoxic state (PMID: 41318543) — a candidate primary mediator rather than purely secondary. **CL terms:** sensory neuron (CL:0000101), microglial cell (CL:0000129), cardiac muscle cell (CL:0000746), pancreatic β-cell (CL:0000169).

### 7. Anatomical Structures Affected
**Primary:** nervous system (DRG, dorsal columns, spinocerebellar/corticospinal tracts, dentate nucleus) and heart. **Secondary/systemic:** pancreas (islets → diabetes), skeleton (spine → scoliosis; feet → pes cavus), optic and auditory pathways. **Body systems:** nervous, cardiovascular, musculoskeletal, endocrine. **Subcellular:** mitochondrion (GO:0005739), mitochondrial matrix (GO:0005759). Involvement is bilateral and largely symmetric.

### 8. Temporal Development
**Onset:** typically adolescent/childhood (classical), with late-onset (LOFA, >25 y) and very-late-onset (VLOFA, >40 y) variants generally milder and slower (smaller GAA1). **Pattern:** insidious, chronic, progressive (not relapsing-remitting or episodic). **Stages:** ambulatory → assisted → wheelchair-dependent → advanced with bulbar/cardiac complications. **Progression rate:** variable, inversely related to GAA1 length. **Critical window:** early intervention before irreversible neuronal loss is the therapeutic goal, given DRG hypoplasia may have a developmental component.

### 9. Inheritance and Population
Autosomal recessive; complete penetrance of biallelic expansions; **variable expressivity** governed by GAA1 length; **genetic anticipation** possible via meiotic repeat instability (median ~150-repeat variation). **Prevalence** ~1/30,000–50,000 (European descent); **carrier frequency** ~1/60–100. Founder haplotype; near-absence in East Asian, sub-Saharan African, Amerindian populations. Consanguinity increases risk as in any recessive disorder. Sex ratio ~1:1 (males show worse survival, F010).

### 10. Diagnostics
See Finding 10. Genetic testing is confirmatory (repeat-expansion sizing ± *FXN* sequencing). Adjuncts: nerve conduction (sensory neuronopathy), ECG/echocardiography (hypertrophic → dilated cardiomyopathy), HbA1c/glucose (diabetes), spinal MRI (cervical cord atrophy). No newborn screening currently standard; cascade and carrier testing available.

### 11. Outcome/Prognosis
Life-shortening; mean age at death ~33–38 y, predominantly cardiac. Near-universal loss of ambulation. Negative prognostic markers: male sex, early onset, cardiomyopathy, longer GAA1 (F005, F010). Morbidity is dominated by mobility, communication, swallowing, cardiac, and metabolic impairment. mFARS/FARS and SARA are the standard progression measures.

### 12. Treatment
Omaveloxolone (Nrf2 activator; NCIT concept) is the only approved disease-modifying drug. Symptomatic/supportive: cardiac (ACE-I, beta-blockers, device therapy), antidiabetic agents, orthopedic surgery (spinal fusion), physiotherapy/OT/speech therapy, spasticity and pain management. Experimental: AAV-*FXN* gene therapy, CRISPR repeat excision/epigenetic reactivation, HDAC inhibitors, high-dose nicotinamide, frataxin-stabilizing and splice-modulating molecules, iron chelation (deferiprone).

### 13. Prevention
No primary prevention (monogenic). **Genetic counseling, carrier/cascade screening, prenatal and preimplantation genetic testing** are the mainstays for at-risk families. Tertiary prevention: surveillance and management of cardiomyopathy, diabetes, and scoliosis to avert complications. No immunization or public-health/environmental interventions apply.

### 14. Other Species / Natural Disease
Human disease (NCBI Taxon 9606). *FXN* is evolutionarily conserved with orthologs across mammals, *Drosophila*, *C. elegans*, and yeast (*YFH1*), enabling cross-species mechanistic study. No prominent naturally occurring FRDA-equivalent in companion animals is established; models are engineered. Conservation of the Fe-S/frataxin pathway underlies model validity.

### 15. Model Organisms
**Mouse:** complete KO embryonic lethal; conditional KO (MCK-Cre, NSE-Cre) and humanized GAA-repeat YAC transgenics (YG8R/YG22R) recapitulate cardiac, sensory-neuron, and biochemical phenotypes (F012). **In vitro/human:** iPSC-derived neurons, cardiomyocytes, microglia, and organoids; isogenic CRISPR-corrected lines. **Applications:** mechanism dissection (Fe-S/iron ordering), biomarker discovery, and therapeutic testing (AAV gene therapy, epigenetic reactivation). **Limitations:** models incompletely capture the slow, decades-long human course and full DRG/dentate selective vulnerability. Databases: MGI, IMSR, Cellosaurus.

---

## Mechanistic Model / Interpretation

The unifying model is **dose-dependent frataxin insufficiency**. A single upstream lesion — the intronic GAA expansion — produces graded frataxin deficiency whose magnitude (set principally by GAA1 length and hence residual expression) determines the entire downstream cascade and clinical severity (F005, F009). The pivotal biochemical consequence is failure of Fe-S cluster biosynthesis (F002), which starves the respiratory chain and Fe-S enzymes of function, with mitochondrial iron accumulation and oxidative stress as **downstream, not initiating**, events (established by the temporal ordering in conditional-KO mice, F012). Selective vulnerability of proprioceptive DRG neurons, dentate glutamatergic neurons, cardiomyocytes, and β-cells — cells with high oxidative metabolic demand and/or long axons — explains the stereotyped phenotype (F007, F008). Emerging iPSC data implicate intrinsic microglial dysfunction as a possible primary amplifier of neuronal death (PMID: 41318543).

Therapeutically, three tiers map onto this chain: (1) **antioxidant/bioenergetic buffering downstream** (omaveloxolone via Nrf2; the only approved agent, F004); (2) **transcriptional/epigenetic reactivation at the silenced locus** (HDAC inhibitors, nicotinamide, anti-gene oligonucleotides; F016); and (3) **frataxin restoration at the source** (AAV-*FXN* gene replacement and CRISPR repeat correction; F013, F012). The further upstream the intervention, the greater the theoretical disease modification — but the harder the delivery to CNS and heart.

---

## Evidence Base

| PMID | Contribution |
|---|---|
| [42295329](https://pubmed.ncbi.nlm.nih.gov/42295329/) | Epigenetic silencing mechanism; reactivation therapies |
| [41514384](https://pubmed.ncbi.nlm.nih.gov/41514384/) | GAA expansion → reduced FXN; Fe-S cluster role; iPSC models |
| [41447358](https://pubmed.ncbi.nlm.nih.gov/41447358/) | Metabolic consequences; universal neurological involvement |
| [40541211](https://pubmed.ncbi.nlm.nih.gov/40541211/) | Multisystem overview; cardiomyopathy mortality; omaveloxolone approval |
| [8751856](https://pubmed.ncbi.nlm.nih.gov/8751856/) | Genotype–phenotype: GAA length vs onset/cardiomyopathy/diabetes |
| [11719273](https://pubmed.ncbi.nlm.nih.gov/11719273/) | Independent confirmation of GAA–onset correlation |
| [31938785](https://pubmed.ncbi.nlm.nih.gov/31938785/) | FA-COMS: loss of ambulation ~11.5 y |
| [41273607](https://pubmed.ncbi.nlm.nih.gov/41273607/) | Survival: mean death age 33 y; prognostic markers |
| [23334592](https://pubmed.ncbi.nlm.nih.gov/23334592/) | Neuropathology: DRG primary lesion, dentate nucleus |
| [23859341](https://pubmed.ncbi.nlm.nih.gov/23859341/) | Systemic (myocardial/islet) involvement |
| [28789479](https://pubmed.ncbi.nlm.nih.gov/28789479/) | Residual frataxin determines phenotype |
| [11810294](https://pubmed.ncbi.nlm.nih.gov/11810294/) | Epidemiology and founder/reservoir-allele effect |
| [33068037](https://pubmed.ncbi.nlm.nih.gov/33068037/) | MOXIe trial: omaveloxolone efficacy |
| [25928624](https://pubmed.ncbi.nlm.nih.gov/25928624/) | Consensus management guidelines; diagnostic hallmarks |
| [24418350](https://pubmed.ncbi.nlm.nih.gov/24418350/) | EFNS/ENS diagnostic algorithm; differentials |
| [11175786](https://pubmed.ncbi.nlm.nih.gov/11175786/) | Conditional-KO mouse: Fe-S loss precedes iron accumulation |
| [16919418](https://pubmed.ncbi.nlm.nih.gov/16919418/) | Humanized GAA-repeat YAC mouse model |
| [26015982](https://pubmed.ncbi.nlm.nih.gov/26015982/) | AAV9-hFXN doubles lifespan; cardiac rescue |
| [41137390](https://pubmed.ncbi.nlm.nih.gov/41137390/) | AAV2-FXN ocular gene-therapy proof-of-concept |
| [41318543](https://pubmed.ncbi.nlm.nih.gov/41318543/) | Microglial dysfunction as candidate primary mediator |

**Evidence source types:** human clinical/pathology (40541211, 23334592, 28789479, 31938785, 41273607, 33068037, 8751856, 11719273, 11810294, 25928624, 24418350); model organism (11175786, 16919418, 26015982, 41137390); in vitro/iPSC (41514384, 41318543); reviews/mechanistic synthesis (42295329, 41447358, 23859341).

---

## Limitations and Knowledge Gaps

- **Iron's causal role remains debated.** Mouse data place iron accumulation downstream of Fe-S enzyme failure, and iron chelation has not been established as disease-modifying — so iron may be a marker/amplifier rather than a primary driver.
- **Microgliopathy** as a primary vs secondary mediator is supported by iPSC/xenograft data but not yet confirmed in patients.
- **Modifier genes** beyond GAA1 length are incompletely defined; GAA1 explains ~50% of onset-age variance, leaving substantial unexplained variability.
- **Omaveloxolone's effect is modest** (mFARS −2.40 over 48 weeks) and long-term/hard-outcome (mortality, ambulation) benefit is not yet proven.
- **Gene-therapy translation** faces CNS + cardiac delivery, dosing, durability, and safety hurdles; human efficacy is unproven.
- **Epidemiology** relies on European-ancestry data; prevalence in admixed and under-studied populations is uncertain.
- **Natural animal disease** and standardized model-to-human progression mapping are limited.

---

## Proposed Follow-up Experiments / Actions

1. **Frataxin as a surrogate biomarker:** validate blood/skin/platelet frataxin (and lipid-peroxidation/Fe-S metabolite panels) against mFARS progression and cardiac endpoints to enable shorter trials.
2. **Long-term omaveloxolone outcomes:** analyze open-label extension and real-world registry data for effects on ambulation loss and cardiac mortality.
3. **Iron-handling intervention trials** stratified by residual frataxin and cardiac iron (MRI T2*) to resolve iron's causal contribution.
4. **Head-to-head model benchmarking** of AAV-*FXN* serotypes/capsids for combined CNS+cardiac transduction and durability in humanized YG8R mice.
5. **Microglia-targeted studies:** test whether CRISPR-corrected or pharmacologically rescued microglia halt neuronal death in xenograft models, and seek patient CSF/imaging correlates of neuroinflammation.
6. **Modifier-gene GWAS/QTL** in large FA-COMS-scale cohorts to explain residual onset-age variance beyond GAA1.
7. **Cross-omics integration** (transcriptomic + proteomic + metabolomic) in DRG/cardiac iPSC models to prioritize druggable downstream nodes and cell-type-specific biomarkers.

---

*Report compiled from 16 confirmed findings and 32 reviewed papers across 5 investigation iterations. Ontology suggestions: MONDO:0100339; HGNC:3951 (FXN); GO:0016226, GO:0005739, GO:0022900, GO:0034599; UBERON:0000044, UBERON:0002439, UBERON:0002349, UBERON:0000006; CL:0000101, CL:0000129, CL:0000746, CL:0000169.*


## Artifacts

- [OpenScientist final report](Friedreich_Ataxia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Friedreich_Ataxia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003390` (1 mention) - the report calls it "Impaired vibration sense"; HP calls it **Sensory axonal neuropathy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001251` (1 mention) - the report calls it "Limb ataxia"; HP calls it **Ataxia**
- `HP:0001284` (1 mention) - the report calls it "Lower-limb areflexia"; HP calls it **Areflexia**
- `HP:0003487` (1 mention) - the report calls it "Extensor plantar response (Babinski)"; HP calls it **Babinski sign**, and lists "Extensor plantar responses" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.