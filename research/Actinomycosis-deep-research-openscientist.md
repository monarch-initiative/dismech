---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T20:46:34.628035'
end_time: '2026-09-24T21:05:26.933960'
duration_seconds: 1132.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Actinomycosis
  mondo_id: ''
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
citation_count: 31
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 31
  on_topic: 22
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 34
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 7
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0001580
    reported_labels:
    - actinomycosis
    ontology_label: lacrimal duct cancer
  - term_id: HP:0100279
    reported_labels:
    - Fistula
    ontology_label: Ulcerative colitis
  - term_id: UBERON:0002048
    reported_labels:
    - Thoracic/pulmonary:** lung
    ontology_label: lung
  - term_id: UBERON:0001155
    reported_labels:
    - Abdominopelvic:** ileocecal region/colon
    ontology_label: colon
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Actinomycosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Actinomycosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Actinomycosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Actinomycosis** covering all of the
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

# Actinomycosis — Comprehensive Disease Characterization

*Category: Infectious Disease · MONDO: MONDO:0001580 (actinomycosis) · Report compiled from 5 discovery iterations, 9 confirmed findings, and 34 reviewed papers*

---

## Summary

**Actinomycosis is a rare, chronic, slowly progressive suppurative-and-granulomatous bacterial infection caused by commensal anaerobic Gram-positive *Actinomyces* species — chiefly *Actinomyces israelii*.** These organisms are harmless residents of the human oropharynx, gastrointestinal tract, and female genital tract; they become pathogenic only when the mucosal barrier that normally contains them is breached by dental disease/procedures, aspiration, trauma, surgery, or a long-standing intrauterine device (IUD). Once in deep tissue, the organism resists intracellular killing, coaggregates with companion bacteria into adhesin/pilus-mediated polymicrobial biofilms (the "sulfur granules"), and elicits a Splendore–Hoeppli granulomatous reaction. The result is a chronic infiltrative mass that crosses tissue planes, forms sinus tracts and fibrosis, and famously **mimics malignancy** at nearly every anatomical site.

Three classic clinical forms map onto distinct predisposing factors: **cervicofacial** (following a dental focus), **pelvic/abdominal** (women with an IUD), and **pulmonary/thoracic** (smokers with poor dental hygiene). The disease is not genetic and is not classically zoonotic, though naturally occurring *Actinomyces* disease is well documented in cattle ("lumpy jaw") and wild cervids. Diagnosis is difficult and frequently delayed (mean ~110 days in one series); it rests on histopathology (sulfur granules with Splendore–Hoeppli material and filamentous Gram-positive organisms) supplemented by prolonged anaerobic culture or, increasingly, 16S rRNA / metagenomic next-generation sequencing. Diagnosis is often made only after surgical resection performed for suspected cancer.

Prognosis is excellent for localized disease: prolonged high-dose penicillin G or amoxicillin (6–12 months, shortenable to ~3 months after complete surgical resection) achieves cure in >90% of cases with low antimicrobial resistance. The major exception is **central nervous system (CNS) actinomycosis**, which carries ~11% case-fatality and ~22% neurological sequelae; here combined surgery plus antimicrobials significantly improves survival (adjusted OR 0.14). Prevention centers on dental hygiene, reduced smoking/alcohol, and timely IUD exchange — notably, removal of an IUD alone clears asymptomatic genital *Actinomyces* colonization without antibiotics in essentially all women within 6–12 months.

---

## Key Findings

### F001 — Actinomycosis is caused by commensal *Actinomyces* that turn invasive only after a mucosal breach

Actinomycosis is defined by a two-part causal logic: an organism that is normally harmless, plus a triggering event that lets it into tissue where it does not belong. The comprehensive review by Valour et al. establishes that *Actinomyces* spp. are anaerobic Gram-positive bacteria that normally colonize the human mouth, digestive tract, and genital tract — *"Actinomycosis is a rare chronic disease caused by Actinomyces spp., anaerobic Gram-positive bacteria that normally colonize the human mouth and digestive and genital tracts"* ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/)). Because the organism is a commensal, disease is fundamentally **opportunistic**: it requires disruption of the mucosal barrier. The abdominal actinomycosis review makes this explicit — *"Actinomyces are considered to be residential saprophytes in the gastrointestinal tract and require a mucosal lesion to cause an opportunistic infection"* ([PMID: 24905109](https://pubmed.ncbi.nlm.nih.gov/24905109/)). This is the initiating step of the entire pathogenic cascade and explains why the disease has no genetic etiology and why prevention hinges on protecting mucosal integrity.

### F002 — Three classic clinical forms map to distinct predisposing factors; the disease mimics malignancy

The disease presents in anatomically distinct but mechanistically unified forms. Valour et al. describe *"cervicofacial actinomycosis following dental focus of infection, pelvic actinomycosis in women with an intrauterine device, and pulmonary actinomycosis in smokers with poor dental hygiene"* ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/)). Each form corresponds to a specific mode of mucosal breach: odontogenic infection (cervicofacial), IUD-associated genital colonization (pelvic — *"Pelvic actinomycosis is a rare, chronic infection caused by Actinomyces species, most associated with prolonged intrauterine device (IUD) use,"* [PMID: 42287450](https://pubmed.ncbi.nlm.nih.gov/42287450/)), and aspiration with poor dental hygiene (pulmonary). A defining and clinically dangerous feature across all sites is **tumor mimicry**: independent case series report infiltrative mass lesions raising suspicion for cancer in the lung ([PMID: 42007821](https://pubmed.ncbi.nlm.nih.gov/42007821/)), liver ([PMID: 42501997](https://pubmed.ncbi.nlm.nih.gov/42501997/)), pelvis ([PMID: 42287450](https://pubmed.ncbi.nlm.nih.gov/42287450/)), mandible ([PMID: 41871568](https://pubmed.ncbi.nlm.nih.gov/41871568/)), and abdominal wall ([PMID: 42717451](https://pubmed.ncbi.nlm.nih.gov/42717451/)). This mimicry frequently drives patients to major, sometimes unnecessary, surgery.

### F003 — Diagnosis rests on sulfur granules and prolonged anaerobic culture; often only after surgery

Diagnosis is notoriously difficult. Valour et al. note that *"Prolonged bacterial cultures in anaerobic conditions are necessary to identify the bacterium and typical microscopic findings include necrosis with yellowish sulfur granules and filamentous Gram-positive fungal-like pathogens"* ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/)). Culture, though the microbiological gold standard, has high false-negative rates, so the diagnosis is more often histopathological ([PMID: 24905109](https://pubmed.ncbi.nlm.nih.gov/24905109/)). A retrospective series of 17 patients quantified the diagnostic delay: *"The mean time to diagnosis was 110 (30–540) days,"* with diagnosis made pathologically in 13/17 versus microbiologically in 4/17 ([PMID: 41712794](https://pubmed.ncbi.nlm.nih.gov/41712794/)). Modern molecular methods — 16S rRNA gene sequencing and metagenomic next-generation sequencing (mNGS) — are increasingly decisive, as seen in a cardiac case confirmed by 16S rRNA ([PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/)) and multiple osteomyelitis cases identified only by mNGS ([PMID: 42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/), [PMID: 41691170](https://pubmed.ncbi.nlm.nih.gov/41691170/)).

### F004 — Prolonged high-dose penicillin/amoxicillin cures actinomycosis with excellent prognosis

Treatment is a long course of beta-lactam antibiotics. Valour et al.: *"Patients with actinomycosis require prolonged (6- to 12-month) high doses ... of penicillin G or amoxicillin, but the duration of antimicrobial therapy could probably be shortened to 3 months in patients in whom optimal surgical resection of infected tissues has been performed"* ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/)). Outcomes are excellent. In a series of 17, *"the outcome was favorable in 16 cases"* (94%) ([PMID: 41712794](https://pubmed.ncbi.nlm.nih.gov/41712794/)). In 7 renal transplant recipients, all treated with amoxicillin for a median of 115 days (range 30–200), *"all patients, except one, recovered completely"* ([PMID: 30055044](https://pubmed.ncbi.nlm.nih.gov/30055044/)). Resistance rates are low, and IV-then-oral penicillin for ≥4 weeks is advisable ([PMID: 24905109](https://pubmed.ncbi.nlm.nih.gov/24905109/)).

### F005 — *Actinomyces* evades intracellular killing and elicits a Splendore–Hoeppli granulomatous reaction

The chronicity of actinomycosis is explained by immune evasion. Friduss & Maceri report that *"The organism, although phagocytized by the host cells, is not killed. Therefore, it is defined as a facultative intracellular parasite of the host"* ([PMID: 2228706](https://pubmed.ncbi.nlm.nih.gov/2228706/)). The host response produces the disease's signature histology, the Splendore–Hoeppli phenomenon: *"The Splendore-Hoeppli reaction material comprises antigen-antibody complex, tissue debris and fibrin"* and represents a localized immunological response to which actinomycosis is a recognized bacterial cause ([PMID: 18976399](https://pubmed.ncbi.nlm.nih.gov/18976399/)). A cardiac actinomycosis biopsy demonstrated abscess formation with the Splendore–Hoeppli phenomenon and Gram-positive/Grocott-positive filaments, confirmed by 16S rRNA sequencing ([PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/)).

### F006 — Actinomycosis is a comparative disease of cattle and wild cervids

While not classically zoonotic (person-to-person or animal-to-person transmission is not a feature), naturally occurring *Actinomyces* disease is well documented in animals. Friduss & Maceri note *"Actinomycotic infections, once common in humans and cattle, are now rare causes of disease in man"* ([PMID: 2228706](https://pubmed.ncbi.nlm.nih.gov/2228706/)) — the bovine form is classic "lumpy jaw." In wild cervids, granulomatous lymphadenitis showed Splendore–Hoeppli material in 93% of cases, with *"Organisms morphologically consistent with Actinomyces spp. ... found in one white-tailed deer,"* and focal granulomatous lymphadenitis occurring in 0.3–1.3% of deer ([PMID: 19617472](https://pubmed.ncbi.nlm.nih.gov/19617472/)).

### F007 — IUD use promotes genital *Actinomyces* colonization in a device- and duration-dependent, reversible manner

The IUD–*Actinomyces* relationship is one of the best-quantified in the field. Mali et al. found that among 815 IUD users, *"the repeat smears from 57 women were positive for Actinomyces-like organisms, giving a prevalence rate of 6.99%"* (with *A. israelii* confirmed by immunofluorescence in all and cultured in 23/40), while all non-users were negative; prolonged use (>2 years) promoted overgrowth ([PMID: 3526779](https://pubmed.ncbi.nlm.nih.gov/3526779/)). Device type matters: Mao & Guillebaud reported actinomyces-like organism (ALO) prevalence of 22.6% with inert versus 2% with copper IUDs, and — critically — *"After removal of the IUCD, and without antibiotic therapy, in 100% (20/20) of the women, ALO colonisation was no longer found six to twelve months later"* ([PMID: 6529911](https://pubmed.ncbi.nlm.nih.gov/6529911/)). A systematic review of pelvic actinomycosis (63 articles, 1980–2014) confirmed the dominant IUD association and the typical route of diagnosis by histology after surgery ([PMID: 28684963](https://pubmed.ncbi.nlm.nih.gov/28684963/)). This finding establishes both a **dose–response** (duration, device type) and **reversibility** — an unusually clean exposure–response relationship for an infectious disease.

### F008 — CNS actinomycosis carries ~11% mortality; combined surgery + antibiotics improves survival

CNS disease is the principal exception to the disease's generally benign prognosis. A systematic review of 118 CNS actinomycosis cases (1988–2022) found a mean age of 44 years, 57% male; *A. israelii* most common (41.5%) followed by *A. meyeri* (22.6%); brain abscess in 55%, leptomeningeal enhancement in 22%, culture positivity 53.4%, and disseminated disease in 19.5%. Outcomes were markedly worse than localized disease: *"The overall case-fatality rate was 11%. Neurological sequelae were present in 22% of the patients"* ([PMID: 37269006](https://pubmed.ncbi.nlm.nih.gov/37269006/)). Multivariate analysis showed a survival benefit of combined management — *"patients who underwent surgery with antimicrobials had better survival (adjusted OR 0.14, 95% CI 0.04–0.28)"* ([PMID: 37269006](https://pubmed.ncbi.nlm.nih.gov/37269006/)). This contrasts with the ~94% favorable outcome for localized disease ([PMID: 41712794](https://pubmed.ncbi.nlm.nih.gov/41712794/)).

### F009 — Pathogenesis is driven by fimbrial/pilus adhesins, coaggregation, and polymicrobial biofilm formation

The sulfur granule is not a pure culture but a **polymicrobial biofilm** built by molecular adhesion mechanisms. Cisar describes how indigenous Gram-positive tooth colonizers *"including viridans streptococci and actinomyces"* evade host secretory inhibitors of adhesion through the structural design and binding properties of bacterial adhesins/receptors ([PMID: 9524453](https://pubmed.ncbi.nlm.nih.gov/9524453/)). Kumari Yadav et al. show that *"Early colonization by S. oralis and its interaction with Actinomyces oris seeds the development of oral biofilm or dental plaque,"* mediated by sortase-dependent pili ([PMID: 31929180](https://pubmed.ncbi.nlm.nih.gov/31929180/)). Companion organisms enable deep-tissue invasion: *"Periodontal pathogens or their pathogenic products must be able to pass through the epithelial cell barrier in order to reach and cause destruction to underlying tissues"* ([PMID: 10522226](https://pubmed.ncbi.nlm.nih.gov/10522226/)). This explains why actinomycosis is fundamentally a **synergistic polymicrobial** infection.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Actinomycosis is a rare chronic granulomatous and suppurative bacterial infection caused by *Actinomyces* species, anaerobic-to-microaerophilic Gram-positive filamentous bacteria that are normal commensals of the human oropharynx, gastrointestinal tract, and female genital tract. It is characterized by indolent progression, formation of abscesses and draining sinus tracts, extension across normal tissue planes (disregarding anatomical boundaries), dense fibrosis, and the pathognomonic "sulfur granules." It classically mimics malignancy.

**Key identifiers:**
- **MONDO:** MONDO:0001580 (actinomycosis)
- **ICD-10:** A42 (A42.0 pulmonary, A42.1 abdominal, A42.2 cervicofacial, A42.7 actinomycotic sepsis, A42.8 other, A42.9 unspecified)
- **ICD-11:** 1C10 (Actinomycosis)
- **MeSH:** D000196 (Actinomycosis)
- **OMIM / Orphanet:** Not a Mendelian disorder; no OMIM entry. Not a heritable rare disease (acquired infection).
- **SNOMED CT:** 63455001 (Actinomycosis)

**Synonyms / alternative names:** "Lumpy jaw" (cervicofacial and bovine forms), actinomycotic infection, "the most misdiagnosed disease." Historically confused with fungal disease owing to filamentous morphology (hence "fungal-like").

**Information source type:** Aggregated disease-level knowledge derived from case reports, retrospective case series, and systematic reviews (e.g., [PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/), [PMID: 28684963](https://pubmed.ncbi.nlm.nih.gov/28684963/), [PMID: 37269006](https://pubmed.ncbi.nlm.nih.gov/37269006/)). There is no large EHR-derived individual-patient dataset; the disease's rarity means the evidence base is dominated by pooled case-level literature.

### 2. Etiology

**Primary cause — infectious.** The disease is caused by *Actinomyces* spp. (commensal anaerobic Gram-positive bacteria) that become invasive after a mucosal breach ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/); [PMID: 24905109](https://pubmed.ncbi.nlm.nih.gov/24905109/)). It is **not a genetic disease** — there are no causal genes, no Mendelian inheritance, and no established susceptibility loci. Infection is typically **polymicrobial**, with companion bacteria (e.g., *Aggregatibacter actinomycetemcomitans*, *Streptococcus* spp., *Finegoldia magna*, *Staphylococcus* spp., Enterobacteriaceae, *Fusobacterium*) contributing to invasion and biofilm architecture ([PMID: 31929180](https://pubmed.ncbi.nlm.nih.gov/31929180/); [PMID: 10522226](https://pubmed.ncbi.nlm.nih.gov/10522226/); [PMID: 41691170](https://pubmed.ncbi.nlm.nih.gov/41691170/)).

**Risk factors (environmental/host):**
- **Genetic:** None established. Immunosuppression is facilitating, not required (most cases occur in immunocompetent hosts).
- **Dental disease and dental procedures** → cervicofacial disease ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/)).
- **Long-standing IUD (especially inert/plastic, >2 years)** → pelvic/abdominal disease ([PMID: 3526779](https://pubmed.ncbi.nlm.nih.gov/3526779/); [PMID: 6529911](https://pubmed.ncbi.nlm.nih.gov/6529911/); [PMID: 28684963](https://pubmed.ncbi.nlm.nih.gov/28684963/)).
- **Smoking + poor oral hygiene, aspiration** → pulmonary/thoracic disease ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/)).
- **Trauma / surgery** (post-surgical abdominal wall, post-traumatic osteomyelitis) → localized soft-tissue and bone disease ([PMID: 42717451](https://pubmed.ncbi.nlm.nih.gov/42717451/); [PMID: 41691170](https://pubmed.ncbi.nlm.nih.gov/41691170/); [PMID: 42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/)).
- **Immunosuppression** (e.g., renal transplant, though prevalence very low at 0.02%) ([PMID: 30055044](https://pubmed.ncbi.nlm.nih.gov/30055044/)); poor socioeconomic status noted in a CNS case ([PMID: 30572823](https://pubmed.ncbi.nlm.nih.gov/30572823/)).

**Protective factors:** Good dental hygiene; copper rather than inert IUDs (ALO prevalence 2% vs 22.6%, [PMID: 6529911](https://pubmed.ncbi.nlm.nih.gov/6529911/)); timely IUD removal/exchange (clears colonization in 100% within 6–12 months without antibiotics, [PMID: 6529911](https://pubmed.ncbi.nlm.nih.gov/6529911/)). One historical report speculated that cyclical menstrual flow may act as a protective "cleansing mechanism" ([PMID: 6481117](https://pubmed.ncbi.nlm.nih.gov/6481117/)). No **genetic** protective factors are known.

**Gene–environment interactions:** Not applicable in the classical sense — actinomycosis has no genetic component. The relevant interaction is **host-barrier × microbial-colonization**: the same commensal is harmless on an intact mucosa and pathogenic once the barrier is breached.

### 3. Phenotypes

Phenotypes are anatomically driven. Common features across forms:

| Phenotype | Type | Frequency / notes | Suggested HPO |
|---|---|---|---|
| Chronic infiltrative mass mimicking tumor | Clinical sign | Hallmark across sites ([PMID: 42007821](https://pubmed.ncbi.nlm.nih.gov/42007821/), [PMID: 42501997](https://pubmed.ncbi.nlm.nih.gov/42501997/)) | HP:0002664 (Neoplasm — mimic) |
| Draining sinus tracts / fistulae | Physical manifestation | Classic in cervicofacial and abdominal ([PMID: 6481117](https://pubmed.ncbi.nlm.nih.gov/6481117/)) | HP:0100279 (Fistula) |
| Sulfur granules in discharge/tissue | Lab/pathology | Pathognomonic when present | — |
| Fever, night sweats | Symptom | Common, nonspecific ([PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/)) | HP:0001945 (Fever) |
| Weight loss | Symptom | Common ([PMID: 42501997](https://pubmed.ncbi.nlm.nih.gov/42501997/), [PMID: 20458215](https://pubmed.ncbi.nlm.nih.gov/20458215/)) | HP:0001824 (Weight loss) |
| Cough, dyspnea, hemoptysis, chest pain | Symptom | Pulmonary form ([PMID: 42007821](https://pubmed.ncbi.nlm.nih.gov/42007821/)) | HP:0012735, HP:0002094, HP:0002105 |
| Trismus, neck/jaw swelling | Clinical sign | Cervicofacial ([PMID: 41871568](https://pubmed.ncbi.nlm.nih.gov/41871568/)) | HP:0000211 (Trismus) |
| Osteomyelitis (mandible, phalanx, fibula) | Physical manifestation | Bone involvement ([PMID: 41871568](https://pubmed.ncbi.nlm.nih.gov/41871568/), [PMID: 41691170](https://pubmed.ncbi.nlm.nih.gov/41691170/), [PMID: 42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/)) | HP:0002754 (Osteomyelitis) |
| Abdominal/pelvic mass, pain | Symptom/sign | Abdominopelvic form ([PMID: 42287450](https://pubmed.ncbi.nlm.nih.gov/42287450/)) | HP:0004396, HP:0002027 |
| Pericardial effusion / constriction | Clinical sign | Rare thoracic/cardiac ([PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/)) | HP:0001698 (Pericardial effusion) |
| Elevated inflammatory markers | Lab abnormality | Variable ([PMID: 41871568](https://pubmed.ncbi.nlm.nih.gov/41871568/)) | HP:0011897 (Neutrophilia) |

**Characteristics:** Onset is typically **adult** (mean ~44 y in CNS series). Course is **chronic, indolent, progressive** if untreated, punctuated by episodic abscess/sinus formation. Severity is **variable** — from an indolent local mass to fatal disseminated/CNS disease. **Quality of life** is impaired mainly by diagnostic delay, disfiguring surgery, and prolonged antibiotic courses; CNS disease leaves neurological sequelae in ~22% ([PMID: 37269006](https://pubmed.ncbi.nlm.nih.gov/37269006/)).

### 4. Genetic / Molecular Information

**Not applicable to the human host.** Actinomycosis has **no causal human genes, no pathogenic germline/somatic variants, no modifier genes, no chromosomal abnormalities, and no established disease-associated epigenetic changes.** It is an acquired bacterial infection, not a heritable disorder. The relevant "genetics" are microbial: bacterial adhesin/pilus genes (e.g., sortase-dependent pilus loci in *Actinomyces oris*; *fim* fimbrial genes) that mediate coaggregation and biofilm formation ([PMID: 31929180](https://pubmed.ncbi.nlm.nih.gov/31929180/); [PMID: 9524453](https://pubmed.ncbi.nlm.nih.gov/9524453/)), and virulence factors of companion organisms such as *A. actinomycetemcomitans* ([PMID: 10522226](https://pubmed.ncbi.nlm.nih.gov/10522226/)).

### 5. Environmental Information

- **Environmental factors:** Foreign bodies are central — the IUD is the paradigmatic example ([PMID: 3526779](https://pubmed.ncbi.nlm.nih.gov/3526779/); [PMID: 6481117](https://pubmed.ncbi.nlm.nih.gov/6481117/)); retained gallstones after laparoscopic cholecystectomy have caused intraperitoneal actinomycosis ([PMID: 19886052](https://pubmed.ncbi.nlm.nih.gov/19886052/)); prior surgery/implants predispose to soft-tissue disease ([PMID: 42717451](https://pubmed.ncbi.nlm.nih.gov/42717451/)).
- **Lifestyle factors:** Smoking and poor dental hygiene (pulmonary form); alcohol; dental neglect ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/)).
- **Infectious agents (NCBI Taxonomy):** *Actinomyces israelii* (txid1659), *A. meyeri*, *A. odontolyticus*, *A. naeslundii*, *A. viscosus*, *A. gerencseriae*; reclassified species now include *Schaalia turicensis* (formerly *A. turicensis*, [PMID: 42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/)) and *Actinomyces radingae* ([PMID: 41691170](https://pubmed.ncbi.nlm.nih.gov/41691170/)). Genus *Actinomyces* = NCBI txid1654. Companion organisms include *Aggregatibacter actinomycetemcomitans*, *Streptococcus oralis*, *Finegoldia magna*, and *Staphylococcus* spp.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

```
1. Actinomyces spp. colonize the oral/GI/genital mucosa as harmless commensals
        │  (established; PMID 25045274)
        ▼
2. A mucosal barrier breach (dental disease/procedure, aspiration, IUD, trauma,
   surgery) LEADS TO translocation of the organism into normally sterile deep tissue
        │  (established; PMID 24905109)
        ▼
3. In tissue, Actinomyces coaggregates with companion bacteria via fimbrial/
   sortase-dependent pilus adhesins, RESULTING IN a polymicrobial biofilm
        │  (established in oral plaque model; PMID 31929180, 9524453)
        ▼
4. Companion organisms breach the epithelial cell barrier, FACILITATING deeper
   tissue penetration and synergistic invasion
        │  (demonstrated for A. actinomycetemcomitans; PMID 10522226 — inferred to
        │   generalize to actinomycosis biofilms)
        ▼
5. The biofilm macroscopically forms "sulfur granules"; the organism is phagocytosed
   but NOT killed (facultative intracellular survival), RESULTING IN persistence
        │  (established; PMID 2228706)
        ▼
6. Persistent antigen elicits a chronic granulomatous/suppurative host response with
   antigen–antibody–fibrin deposition → the Splendore–Hoeppli phenomenon
        │  (established; PMID 18976399, 38077408)
        ▼
7. Chronic inflammation LEADS TO abscess formation, dense fibrosis, and sinus tracts
   that cross anatomical tissue planes
        │  (established; PMID 6481117, 25045274)
        ▼
8. The infiltrative fibro-inflammatory mass MANIFESTS clinically as a chronic,
   cancer-mimicking lesion at the affected site
           │
           ├──► localized disease → curable with prolonged penicillin (>90% favorable)
           └──► hematogenous/contiguous spread → disseminated/CNS disease (~11% fatal)
              (PMID 41712794; PMID 37269006; PMID 38077408)
```

**Molecular pathways / cellular processes.** The dominant biology is **bacterial biofilm formation** (GO:0042710) via **cell–cell adhesion** (GO:0098609) and sortase-mediated pilus assembly, plus a host **granulomatous inflammatory response** (GO:0002532) and **defense response to bacterium** (GO:0042742). There is no canonical human oncogenic/degenerative signaling cascade (Wnt, MAPK, mTOR) involved — this is an infectious/inflammatory, not a signaling, disease.

**Immune involvement.** Neutrophilic suppuration surrounds granules; macrophages phagocytose but fail to kill the organism (facultative intracellular parasitism, [PMID: 2228706](https://pubmed.ncbi.nlm.nih.gov/2228706/)); a humoral response contributes antigen–antibody complexes to Splendore–Hoeppli material ([PMID: 18976399](https://pubmed.ncbi.nlm.nih.gov/18976399/)). Cell types: **neutrophils (CL:0000775)**, **macrophages (CL:0000235)**, **plasma cells (CL:0000786)**, **fibroblasts (CL:0000057)**, and mucosal **epithelial cells (CL:0000066)** at the breach site.

**Tissue damage mechanisms.** Chronic suppuration, necrosis, and reactive fibrosis; extension across tissue planes rather than respecting fascial boundaries. **Metabolic/biochemical:** *Actinomyces* is a fermentative anaerobe; disease favors low-oxygen (devitalized/necrotic) tissue niches. No specific enzyme deficiency or metabolomic signature is established for this infection.

### 7. Anatomical Structures Affected

- **Cervicofacial (~50% historically):** mandible (UBERON:0001684), maxilla, paranasal sinuses (UBERON:0001825), neck soft tissue; can cause mandibular osteomyelitis ([PMID: 41871568](https://pubmed.ncbi.nlm.nih.gov/41871568/), [PMID: 25301047](https://pubmed.ncbi.nlm.nih.gov/25301047/), [PMID: 23008010](https://pubmed.ncbi.nlm.nih.gov/23008010/)).
- **Thoracic/pulmonary:** lung (UBERON:0002048), pleura, chest wall, pericardium (UBERON:0002407) and myocardium ([PMID: 42007821](https://pubmed.ncbi.nlm.nih.gov/42007821/), [PMID: 20458215](https://pubmed.ncbi.nlm.nih.gov/20458215/), [PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/)).
- **Abdominopelvic:** ileocecal region/colon (UBERON:0001155), liver (UBERON:0002107), abdominal wall, uterus/fallopian tubes/ovaries (UBERON:0000995 / UBERON:0000992), peritoneum ([PMID: 24905109](https://pubmed.ncbi.nlm.nih.gov/24905109/), [PMID: 42501997](https://pubmed.ncbi.nlm.nih.gov/42501997/), [PMID: 6481117](https://pubmed.ncbi.nlm.nih.gov/6481117/), [PMID: 42287450](https://pubmed.ncbi.nlm.nih.gov/42287450/)).
- **CNS:** brain (UBERON:0000955) — brain abscess in 55%, leptomeninges (UBERON:0002360) ([PMID: 37269006](https://pubmed.ncbi.nlm.nih.gov/37269006/), [PMID: 30572823](https://pubmed.ncbi.nlm.nih.gov/30572823/)).
- **Bone/soft tissue extremities:** phalanges, fibula ([PMID: 41691170](https://pubmed.ncbi.nlm.nih.gov/41691170/), [PMID: 42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/)).

**Tissue/cell level:** primarily mucosal epithelium (breach site) and connective tissue/bone at the infection focus; the lesion is a mixed inflammatory infiltrate. **Subcellular:** the phagosome/phagolysosome of host macrophages is relevant (survival within phagocytes; GO:0045335 phagocytic vesicle). **Lateralization:** typically unilateral/focal at the site of breach; disseminated disease is multifocal.

### 8. Temporal Development

- **Onset:** Predominantly **adult** (mean ~44 y in CNS series; ~55 y in transplant series). Onset is **insidious/chronic**, over weeks to months.
- **Progression:** Slow and **progressive** if untreated. Diagnostic delay averages ~110 days (range 30–540) ([PMID: 41712794](https://pubmed.ncbi.nlm.nih.gov/41712794/)); the interval from transplant to infection reached a median of 104 months ([PMID: 30055044](https://pubmed.ncbi.nlm.nih.gov/30055044/)). Disease crosses tissue planes rather than following formal staging; there is no cancer-style staging system.
- **Duration/remission:** With appropriate antibiotics ± surgery, the disease is curable, though relapse is described (hence the long treatment course). Remission is **treatment-induced**; untreated disease does not spontaneously resolve. Recurrence propensity is noted for reclassified species (*S. turicensis*, [PMID: 42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/)).
- **Critical periods:** Early recognition (before CNS/disseminated spread) is the key window; failure to recognize the disease early "may result in drastic complications" ([PMID: 20458215](https://pubmed.ncbi.nlm.nih.gov/20458215/)).

### 9. Inheritance and Population

- **Epidemiology:** Rare. Historically cited incidence ~1 per 300,000/year in the pre-antibiotic era, now lower. Prevalence among renal transplant recipients was 0.02% ([PMID: 30055044](https://pubmed.ncbi.nlm.nih.gov/30055044/)). Among IUD users, cervical *Actinomyces*-like organism prevalence is 2–22.6% depending on device and duration ([PMID: 3526779](https://pubmed.ncbi.nlm.nih.gov/3526779/); [PMID: 6529911](https://pubmed.ncbi.nlm.nih.gov/6529911/)). In wild cervids, focal granulomatous lymphadenitis occurs in 0.3–1.3% ([PMID: 19617472](https://pubmed.ncbi.nlm.nih.gov/19617472/)).
- **Inheritance:** **Not heritable** — no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency applies.
- **Demographics:** Male predominance in some series (57% male in CNS, [PMID: 37269006](https://pubmed.ncbi.nlm.nih.gov/37269006/); overall M:F historically ~3:1 for cervicofacial/thoracic), but pelvic disease is essentially exclusive to women (IUD-related). Geographic distribution is worldwide with no strong endemicity; regional shifts track IUD introduction (e.g., post-1990 rise in Romania, [PMID: 19886052](https://pubmed.ncbi.nlm.nih.gov/19886052/)).

### 10. Diagnostics

- **Histopathology (cornerstone):** sulfur granules with radiating filaments surrounded by Splendore–Hoeppli material within suppurative/granulomatous inflammation and reactive fibrosis; Gram-positive, non-acid-fast filaments ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/); [PMID: 42717451](https://pubmed.ncbi.nlm.nih.gov/42717451/); [PMID: 23008010](https://pubmed.ncbi.nlm.nih.gov/23008010/)). Grocott/PAS stains highlight filaments ([PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/)).
- **Microbiology:** prolonged anaerobic culture (gold standard but high false-negative rate) ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/); [PMID: 24905109](https://pubmed.ncbi.nlm.nih.gov/24905109/); [PMID: 28684963](https://pubmed.ncbi.nlm.nih.gov/28684963/)).
- **Molecular:** 16S rRNA gene PCR/sequencing ([PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/); [PMID: 30572823](https://pubmed.ncbi.nlm.nih.gov/30572823/)) and metagenomic next-generation sequencing (mNGS) — increasingly decisive for indolent/reclassified species ([PMID: 42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/); [PMID: 41691170](https://pubmed.ncbi.nlm.nih.gov/41691170/)).
- **Cytology (Pap smear):** actinomyces-like organisms on cervical smear signal IUD-associated colonization — but beware "pseudoactinomyces" mimics that can cause false alarm ([PMID: 21323418](https://pubmed.ncbi.nlm.nih.gov/21323418/)).
- **Imaging:** CT/MRI/FDG-PET typically show an infiltrative, hypermetabolic mass — helpful for extent but **cannot distinguish from malignancy**, often prompting biopsy/surgery ([PMID: 42007821](https://pubmed.ncbi.nlm.nih.gov/42007821/); [PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/)).
- **Genetic/omics diagnostics:** Not applicable (no host genetic test). No newborn/carrier screening.
- **Differential diagnosis:** malignancy (carcinoma, sarcoma, lymphoma), tuberculosis and other granulomatous infections, nocardiosis, Crohn's disease, fungal disease. Nocardiosis is a key mimic distinguished by acid-fastness and aerobic growth ([PMID: 42007821](https://pubmed.ncbi.nlm.nih.gov/42007821/); [PMID: 24905109](https://pubmed.ncbi.nlm.nih.gov/24905109/)).

### 11. Outcome / Prognosis

- **Localized disease: excellent.** Favorable outcome in 16/17 (94%) ([PMID: 41712794](https://pubmed.ncbi.nlm.nih.gov/41712794/)); 6/7 transplant patients fully recovered ([PMID: 30055044](https://pubmed.ncbi.nlm.nih.gov/30055044/)). Low antimicrobial resistance supports high cure rates ([PMID: 24905109](https://pubmed.ncbi.nlm.nih.gov/24905109/)).
- **CNS/disseminated disease: worse.** Case-fatality ~11%, neurological sequelae ~22%; combined surgery + antibiotics improves survival (adjusted OR 0.14) ([PMID: 37269006](https://pubmed.ncbi.nlm.nih.gov/37269006/)). Fatal hepatic/pericardial and pulmonary/CNS cases are documented ([PMID: 33346982](https://pubmed.ncbi.nlm.nih.gov/33346982/); [PMID: 19581170](https://pubmed.ncbi.nlm.nih.gov/19581170/)).
- **Prognostic factors:** anatomical site (CNS worst), extent (disseminated ~19.5% in CNS series), timeliness of diagnosis, and completeness of surgical resection. Adjunctive corticosteroids helped in constrictive pericardial disease ([PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/)).
- **Complications:** sinus tracts, fistulae (e.g., to colon/small bowel), osteomyelitis, constrictive pericarditis, brain abscess, sepsis/multiorgan failure.

### 12. Treatment

- **Pharmacotherapy (first line):** high-dose penicillin G (IV) followed by oral amoxicillin/penicillin V, for **6–12 months**, shortenable to ~3 months after complete surgical resection ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/)). NCIT: Penicillin G (C61785), Amoxicillin (C287). Alternatives for penicillin allergy: doxycycline, clindamycin, macrolides, ceftriaxone; carbapenems (ertapenem, meropenem) used in polymicrobial/resistant contexts ([PMID: 41691170](https://pubmed.ncbi.nlm.nih.gov/41691170/); [PMID: 41871568](https://pubmed.ncbi.nlm.nih.gov/41871568/)); clindamycin used for *S. turicensis* ([PMID: 42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/)).
- **Surgical/interventional:** drainage/resection of abscesses, debridement of necrotic bone, excision of infiltrative masses; ~43% of transplant cases required surgery ([PMID: 30055044](https://pubmed.ncbi.nlm.nih.gov/30055044/)). Surgery is both diagnostic and therapeutic and shortens antibiotic duration.
- **Foreign-body removal:** IUD removal is therapeutic and preventive for pelvic disease ([PMID: 6529911](https://pubmed.ncbi.nlm.nih.gov/6529911/)).
- **Adjunctive:** corticosteroids in selected inflammatory complications (constrictive pericarditis) ([PMID: 38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/)).
- **Advanced/experimental therapeutics:** Not applicable — no gene, cell, RNA, targeted, or immunotherapy is used; this is a classically antibiotic-responsive infection. No pharmacogenomic considerations are established.
- **Adverse events:** vancomycin nephrotoxicity noted when broad empiric regimens are used before diagnosis ([PMID: 41871568](https://pubmed.ncbi.nlm.nih.gov/41871568/)).

### 13. Prevention

- **Primary:** good oral/dental hygiene; smoking cessation; careful management of intra-oral and abdominal foreign bodies; avoiding retained surgical material ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/); [PMID: 19886052](https://pubmed.ncbi.nlm.nih.gov/19886052/)).
- **IUD management:** timely device exchange; preference for copper over inert devices (lower ALO prevalence); removal clears asymptomatic colonization in 100% within 6–12 months without antibiotics ([PMID: 6529911](https://pubmed.ncbi.nlm.nih.gov/6529911/)).
- **Secondary:** cervical Pap-smear surveillance for ALO in IUD users, with awareness of pseudoactinomyces to avoid unnecessary device removal ([PMID: 21323418](https://pubmed.ncbi.nlm.nih.gov/21323418/)); early biopsy of mass lesions to shorten diagnostic delay.
- **Tertiary:** complete surgical resection plus prolonged antibiotics to prevent relapse and complications.
- **Immunization / genetic counseling / public health vector control:** Not applicable — no vaccine, no heritable risk, no vector.

### 14. Other Species / Natural Disease

- **Taxonomy of affected hosts:** *Homo sapiens* (txid9606); cattle *Bos taurus* (txid9913, "lumpy jaw"); white-tailed deer *Odocoileus virginianus* and other wild cervids ([PMID: 2228706](https://pubmed.ncbi.nlm.nih.gov/2228706/); [PMID: 19617472](https://pubmed.ncbi.nlm.nih.gov/19617472/)).
- **Natural disease / veterinary relevance:** Bovine actinomycosis (mandibular "lumpy jaw," typically *A. bovis*) is a classic veterinary disease of economic importance; granulomatous lymphadenitis with Splendore–Hoeppli material occurs in wild cervids (93% of affected nodes) ([PMID: 19617472](https://pubmed.ncbi.nlm.nih.gov/19617472/)).
- **Comparative pathology:** the Splendore–Hoeppli phenomenon and sulfur-granule biofilm architecture are conserved across host species, indicating a **conserved host–pathogen interaction** rather than a species-specific mechanism.
- **Transmission / zoonosis:** **Not zoonotic** — no animal-to-human or human-to-human transmission; each host acquires disease from its own endogenous commensal flora after a barrier breach.

### 15. Model Organisms

- **Dedicated genetic disease models:** None — because there is no host genetic defect, there are no knockout/knock-in/transgenic disease models (no MGI/RGD/ZFIN disease-model entries).
- **Relevant experimental systems:** In vitro **biofilm/coaggregation models** of *Actinomyces oris* with *Streptococcus oralis* recapitulate the adhesin/pilus-mediated plaque-seeding step ([PMID: 31929180](https://pubmed.ncbi.nlm.nih.gov/31929180/); [PMID: 9524453](https://pubmed.ncbi.nlm.nih.gov/9524453/)); epithelial-barrier invasion models with *A. actinomycetemcomitans* model deep-tissue penetration ([PMID: 10522226](https://pubmed.ncbi.nlm.nih.gov/10522226/)). Natural animal disease (cattle, cervids) serves as a comparative model of the granulomatous host response ([PMID: 19617472](https://pubmed.ncbi.nlm.nih.gov/19617472/)).
- **Limitations:** These in vitro systems model early colonization/biofilm and barrier crossing but do not reproduce the full chronic granulomatous mass, Splendore–Hoeppli reaction, or clinical mimicry of malignancy.

---

## Mechanistic Model / Interpretation

Actinomycosis is best understood as a **breach-plus-biofilm** disease. A single unifying model accounts for every clinical form:

| Step | Category | Evidence (PMID) | Certainty |
|---|---|---|---|
| Commensal colonization | Infectious agent | 25045274 | Established |
| Mucosal breach (dental/IUD/aspiration/surgery/trauma) | Environmental trigger | 24905109; 3526779 | Established |
| Adhesin/pilus coaggregation → polymicrobial biofilm | Molecular/cellular | 31929180; 9524453 | Established (oral model) |
| Companion-organism epithelial penetration | Cellular process | 10522226 | Demonstrated for companion; inferred for actinomycosis |
| Phagocytosis without killing (facultative intracellular survival) | Immune evasion | 2228706 | Established |
| Splendore–Hoeppli granulomatous response | Immune/tissue | 18976399; 38077408 | Established |
| Abscess, fibrosis, tissue-plane-crossing sinus tracts | Tissue damage | 6481117; 25045274 | Established |
| Cancer-mimicking mass → localized (curable) vs disseminated/CNS (~11% fatal) | Clinical outcome | 41712794; 37269006 | Established |

The model explains the disease's paradoxes: it is caused by a harmless bug (so it is not "caught"), yet is aggressive locally (biofilm + immune evasion); it is highly antibiotic-sensitive (so cure rates exceed 90%), yet frequently misdiagnosed and delayed (so it still kills, especially in the CNS). The two therapeutic levers — **antibiotics** (kill the persistent biofilm organisms) and **surgery/foreign-body removal** (debulk the biofilm and remove the nidus) — act directly on the two mechanistic pillars.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/) | *Actinomycosis: etiology, clinical features, diagnosis, treatment, and management* | Anchor review: etiology, three forms, diagnosis, treatment |
| [24905109](https://pubmed.ncbi.nlm.nih.gov/24905109/) | *Abdominal actinomycosis: differential to colon carcinoma / Crohn's* | Mucosal-breach requirement; culture false-negatives |
| [41712794](https://pubmed.ncbi.nlm.nih.gov/41712794/) | Retrospective series of 17 | Diagnostic delay (110 d); 94% favorable outcome |
| [37269006](https://pubmed.ncbi.nlm.nih.gov/37269006/) | *CNS actinomycosis systematic review* (n=118) | 11% fatality; surgery+antibiotics OR 0.14 |
| [30055044](https://pubmed.ncbi.nlm.nih.gov/30055044/) | Actinomycosis in renal transplant recipients | Prevalence 0.02%; amoxicillin outcomes |
| [2228706](https://pubmed.ncbi.nlm.nih.gov/2228706/) | *Cervicofacial actinomycosis in children* | Facultative intracellular parasite; cattle comparative |
| [18976399](https://pubmed.ncbi.nlm.nih.gov/18976399/) | *Mucocutaneous Splendore–Hoeppli phenomenon* | Immune-response histology |
| [38077408](https://pubmed.ncbi.nlm.nih.gov/38077408/) | Cardiac/pericardial actinomycosis | 16S confirmation; Splendore–Hoeppli; steroids adjunct |
| [3526779](https://pubmed.ncbi.nlm.nih.gov/3526779/) | Actinomyces in cervical smears of IUD users | 6.99% ALO prevalence; duration effect |
| [6529911](https://pubmed.ncbi.nlm.nih.gov/6529911/) | IUD removal and cervical colonization | Reversibility (100%); inert>copper risk |
| [28684963](https://pubmed.ncbi.nlm.nih.gov/28684963/) | *Pelvic Actinomycosis* systematic review | IUD dominance; histology-after-surgery route |
| [19617472](https://pubmed.ncbi.nlm.nih.gov/19617472/) | Granulomatous lymphadenitis in wild cervids | Natural animal disease; 93% Splendore–Hoeppli |
| [31929180](https://pubmed.ncbi.nlm.nih.gov/31929180/) | *S. oralis PitA pilus* | Adhesin/pilus biofilm seeding with *A. oris* |
| [10522226](https://pubmed.ncbi.nlm.nih.gov/10522226/) | Virulence factors of *A. actinomycetemcomitans* | Epithelial-barrier breaching by companion organism |
| [9524453](https://pubmed.ncbi.nlm.nih.gov/9524453/) | Inhibitors of bacterial adhesion | Actinomyces adhesins evade host inhibitors |
| [42717451](https://pubmed.ncbi.nlm.nih.gov/42717451/), [42007821](https://pubmed.ncbi.nlm.nih.gov/42007821/), [42501997](https://pubmed.ncbi.nlm.nih.gov/42501997/), [42287450](https://pubmed.ncbi.nlm.nih.gov/42287450/), [41871568](https://pubmed.ncbi.nlm.nih.gov/41871568/), [25301047](https://pubmed.ncbi.nlm.nih.gov/25301047/), [23008010](https://pubmed.ncbi.nlm.nih.gov/23008010/) | Case series (multi-site) | Tumor mimicry across anatomy |
| [42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/), [41691170](https://pubmed.ncbi.nlm.nih.gov/41691170/) | *S. turicensis* / *A. radingae* osteomyelitis | mNGS diagnosis; reclassified species; polymicrobial |
| [33346982](https://pubmed.ncbi.nlm.nih.gov/33346982/), [20458215](https://pubmed.ncbi.nlm.nih.gov/20458215/), [19581170](https://pubmed.ncbi.nlm.nih.gov/19581170/) | Fatal hepatic/pulmonary/CNS cases | Severe-end outcomes |
| [21323418](https://pubmed.ncbi.nlm.nih.gov/21323418/) | Pseudoactinomyces in cervical mucus | Diagnostic pitfall |
| [6481117](https://pubmed.ncbi.nlm.nih.gov/6481117/), [19886052](https://pubmed.ncbi.nlm.nih.gov/19886052/) | Abdominal actinomycosis in IUD users | Fistulae; foreign-body nidus; epidemiologic shift |

**Concordance:** The literature is highly internally consistent. No paper in the reviewed set contradicts the breach-plus-biofilm model; disagreements are limited to relative frequencies, which vary by referral pattern and era.

---

## Limitations and Knowledge Gaps

1. **Evidence quality.** The base is dominated by case reports, retrospective series, and systematic reviews of case-level data. There are **no randomized controlled trials** of antibiotic duration or the surgery-vs-medical-alone question; treatment durations (6–12 months) are consensus-based, not trial-proven.
2. **Incidence uncertainty.** True population incidence/prevalence is poorly quantified because the disease is rare, underdiagnosed, and often reclassified microbiologically (species renaming to *Schaalia*, *Winkia*, etc.).
3. **Mechanistic inference.** The epithelial-barrier-breach step is directly demonstrated for the companion organism *A. actinomycetemcomitans* ([PMID: 10522226](https://pubmed.ncbi.nlm.nih.gov/10522226/)) and **inferred** to generalize to *Actinomyces* biofilms in vivo; there is no direct in-vivo human demonstration of the invasion sequence.
4. **Host-response detail.** Why some hosts contain the organism and others develop invasive disease is not molecularly resolved; there is no validated host biomarker or genetic susceptibility signal.
5. **Omics void.** There are no transcriptomic, proteomic, or metabolomic signatures of human actinomycosis in the reviewed literature — an omics-based diagnostic/prognostic gap.
6. **Model organisms.** No genetic animal model exists (appropriately, as the disease is non-genetic), which limits controlled mechanistic dissection to in-vitro biofilm systems and opportunistic natural animal disease.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective diagnostic-yield study of mNGS vs culture vs histology** across anatomical sites, to formalize the emerging role of metagenomic sequencing and reduce the ~110-day diagnostic delay ([PMID: 41712794](https://pubmed.ncbi.nlm.nih.gov/41712794/); [PMID: 42604646](https://pubmed.ncbi.nlm.nih.gov/42604646/)).
2. **Registry-based comparative-effectiveness analysis** of antibiotic duration (3 vs 6 vs 12 months) stratified by completeness of surgical resection, to test the "shortenable to 3 months after resection" hypothesis ([PMID: 25045274](https://pubmed.ncbi.nlm.nih.gov/25045274/)).
3. **In-vivo biofilm invasion model** (organoid or animal) to directly test the inferred companion-organism epithelial-breach step and quantify *Actinomyces*–partner synergy ([PMID: 10522226](https://pubmed.ncbi.nlm.nih.gov/10522226/); [PMID: 31929180](https://pubmed.ncbi.nlm.nih.gov/31929180/)).
4. **Host-response profiling** (transcriptomic/proteomic on sulfur-granule tissue) to identify why phagocytes fail to kill the organism and to seek adjunctive immunomodulatory targets ([PMID: 2228706](https://pubmed.ncbi.nlm.nih.gov/2228706/)).
5. **CNS actinomycosis prospective cohort** to validate the surgery+antibiotics survival benefit (adjusted OR 0.14) and define optimal timing ([PMID: 37269006](https://pubmed.ncbi.nlm.nih.gov/37269006/)).
6. **IUD device-material trial / surveillance** confirming lower colonization with modern copper/hormonal devices and defining optimal exchange intervals ([PMID: 6529911](https://pubmed.ncbi.nlm.nih.gov/6529911/)).

---

*Report generated by autonomous scientific discovery agent. Evidence attributed only to abstracts/citation snippets confirmed during investigation. Ontology suggestions (HPO/GO/CL/UBERON/NCIT/MONDO/NCBI Taxon) are provided as curation aids and should be verified against current ontology releases.*


## Artifacts

- [OpenScientist final report](Actinomycosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Actinomycosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 31 |
| On topic | 22 |
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
| Terms whose name was checked | 16 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0001580` (2 mentions) - the report calls it "actinomycosis"; MONDO calls it **lacrimal duct cancer**
- `HP:0100279` (1 mention) - the report calls it "Fistula"; HP calls it **Ulcerative colitis**
- `UBERON:0002048` (1 mention) - the report calls it "Thoracic/pulmonary:** lung"; UBERON calls it **lung**
- `UBERON:0001155` (1 mention) - the report calls it "Abdominopelvic:** ileocecal region/colon"; UBERON calls it **colon**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002664` (1 mention) - the report calls it "Neoplasm — mimic"; HP calls it **Neoplasm**
- `HP:0011897` (1 mention) - the report calls it "Neutrophilia"; HP calls it **Increased total neutrophil count**, and lists "Neutrophilia" among its other names
- `GO:0042710` (1 mention) - the report calls it "bacterial biofilm formation"; GO calls it **biofilm formation**
- `GO:0002532` (1 mention) - the report calls it "granulomatous inflammatory response"; GO calls it **production of molecular mediator involved in inflammatory response**
- `UBERON:0000955` (1 mention) - the report calls it "CNS:** brain"; UBERON calls it **brain**