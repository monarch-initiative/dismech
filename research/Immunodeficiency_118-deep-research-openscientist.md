---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-22T16:58:06.047627'
end_time: '2026-09-22T17:25:41.581159'
duration_seconds: 1655.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 118
  mondo_id: MONDO:0958030
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
citation_count: 13
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 21
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0958030
    reported_labels:
    - IMD118
    ontology_label: immunodeficiency 118
  - term_id: UBERON:0002107
    reported_labels:
    - UBERON anatomy:** liver
    - liver
    ontology_label: liver
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_118-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_118-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 118
- **MONDO ID:** MONDO:0958030 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 118** covering all of the
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

# Immunodeficiency 118 (IMD118): A Comprehensive Disease Characteristics Report

**Disease:** Immunodeficiency 118 (IMD118)
**MONDO ID:** MONDO:0958030 · **OMIM:** #301115 · **Gene:** *MCTS1* (Xq24)
**Category:** Mendelian — X-linked recessive inborn error of immunity (a subtype of Mendelian Susceptibility to Mycobacterial Disease, MSMD)
**Primary reference:** Bohlen J, Zhou Q, Philippot Q, et al. "Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria." 2023 ([PMID: 37875108](https://pubmed.ncbi.nlm.nih.gov/37875108/)).

---

## Summary

**Immunodeficiency-118 (IMD118) is an ultra-rare, X-linked recessive inborn error of immunity caused by hemizygous loss-of-function mutations in *MCTS1* on chromosome Xq24.** The disease was defined by a single landmark study — Bohlen, Zhou, Béziat, Casanova and colleagues (2023, [PMID: 37875108](https://pubmed.ncbi.nlm.nih.gov/37875108/)) — which identified complete MCTS1 deficiency in **5 unrelated males** from kindreds of different ancestries (China, Finland, Iran, and Saudi Arabia). Clinically, IMD118 belongs to the MSMD spectrum: affected males present in infancy with disseminated infection by weakly virulent mycobacteria, most commonly after Bacillus Calmette-Guérin (BCG) vaccination, while otherwise displaying essentially normal immunity, growth, and development.

**The mechanism is a specific and elegant translational defect.** MCTS1 (Malignant T-cell-amplified sequence 1) is a translation re-initiation and 40S ribosome-recycling factor that forms a heterodimer with DENR. Complete MCTS1 deficiency impairs the translation of a small subset of proteins — most importantly the tyrosine kinase **JAK2** — in all cell types tested. JAK2 loss cripples signaling downstream of **IL-23** (and partially IL-12), which in turn reduces **IFN-γ** production by innate-like adaptive **MAIT (mucosal-associated invariant T)** and **γδ T lymphocytes** upon mycobacterial challenge. Because IFN-γ is the central macrophage-activating cytokine controlling intracellular mycobacteria, its failure produces the characteristic mycobacterial susceptibility. The selectivity of the JAK2 defect is explained by two ultra-short "start-stop" upstream open reading frames (**stuORFs**) in the *JAK2* 5′UTR that render JAK2 translation uniquely dependent on MCTS1-mediated ribosome recycling.

**Prognosis is generally favorable but not benign.** Among the 5 reported patients, one died of disseminated mycobacterial disease while the other four responded to antimycobacterial therapy and remained asymptomatic after early childhood, with normal growth and development. Critically, patient leukocytes retained **normal responses to exogenous IFN-γ and IFN-α**, meaning the block is upstream of the IFN-γ receptor and is potentially bypassable — providing a clear rationale for recombinant IFN-γ as adjunctive therapy, as used successfully in other MSMD genotypes. A notable paradox is that *MCTS1* is an established oncogene, yet its complete germline loss produces only a narrow immunological phenotype rather than developmental defects or cancer, indicating that its translational function is largely physiologically redundant except along the IL-23→JAK2→IFN-γ axis.

---

## Key Findings

### Finding 1 — IMD118 is X-linked recessive MCTS1 deficiency causing isolated mycobacterial disease

IMD118 (OMIM #301115) is caused by **hemizygous loss-of-function variants in *MCTS1*** (Xq24) and was described in 5 unrelated males from four countries. As the primary report states: *"We report X-linked recessive MCTS1 deficiency in men with mycobacterial disease from kindreds of different ancestries (from China, Finland, Iran, and Saudi Arabia)"* ([PMID: 37875108](https://pubmed.ncbi.nlm.nih.gov/37875108/)).

The five patients carried a spectrum of loss-of-function variant types: **2 frameshift variants, 1 splice-site variant, and 2 in-frame 3′ deletions**, the latter two both yielding a truncated protein lacking residues Ala133–Lys181 (p.Ala133_Lys181del). All variants result in complete MCTS1 deficiency. The molecular consequence is defined by the authors: *"Complete deficiency of this translation re-initiation factor impairs the translation of a subset of proteins, including the kinase JAK2 in all cell types tested, including T lymphocytes and phagocytes."* The downstream immunological consequence connects the translation defect to disease: *"Defective responses to IL-23 preferentially impair the production of IFN-γ by innate-like adaptive mucosal-associated invariant T cells (MAIT) and γδ T lymphocytes upon mycobacterial challenge."*

This establishes IMD118 as a single-gene, X-linked recessive disorder in which a general translation factor defect is funneled into a strikingly narrow clinical outcome via a single critical substrate (JAK2) and a single critical pathway (IL-23→IFN-γ).

### Finding 2 — MCTS1 forms a heterodimer with DENR to mediate 40S ribosome recycling and translation reinitiation

MCTS1 (also called MCT-1; NCBI Gene 28985; Xq24) is a translation factor that partners with **DENR** (density-regulated reinitiation factor). Together MCTS1/DENR are the mammalian counterparts of the yeast Tma20/Tma22 heterodimer, with **eIF2D** (yeast Tma64) providing a parallel activity. These factors recycle post-termination 40S ribosomal subunits at stop codons and modulate reinitiation on mRNAs containing short upstream open reading frames (uORFs).

The functional role was demonstrated in yeast and in vitro systems: *"Tma64 (eIF2D), Tma20 (MCT-1), and Tma22 (DENR) function as 40S recycling factors in vitro"* ([PMID: 30146315](https://pubmed.ncbi.nlm.nih.gov/30146315/)). The reinitiation-promoting property that is mechanistically central to IMD118 was shown by Jendruchová et al.: *"MCTS1/DENR enhance reinitiation at short upstream open reading frames (uORFs) harboring penultimate codons that confer dependence on these factors in bulk 40S recycling"* ([PMID: 38903097](https://pubmed.ncbi.nlm.nih.gov/38903097/)). When MCTS1 is absent, 80S ribosomes queue behind stop codons and aberrant reinitiation occurs in 3′UTRs — the general failure that, at the *JAK2* locus, specifically prevents translation of the main JAK2 open reading frame.

### Finding 3 — MCTS1 is a known oncoprotein, yet germline complete loss causes only isolated mycobacterial disease

A striking feature of IMD118 is the mismatch between MCTS1's known oncogenic biology and the narrow phenotype of its germline loss. MCTS1/DENR are **established oncogenes**: *"DENR and MCTS1 have been identified as oncogenes in several different tumor entities. The heterodimeric DENR·MCTS1 protein complex promotes translation of mRNAs containing upstream Open Reading Frames (uORFs)"* ([PMID: 35115540](https://pubmed.ncbi.nlm.nih.gov/35115540/)). The complex is cell-cycle regulated (DENR Ser73 phosphorylated by Cyclin B/CDK1 and Cyclin A/CDK2), and MCTS1 overexpression drives proliferation in laryngeal squamous cell carcinoma via the OTUD6B-LIN28B axis and LARP7 stabilization ([PMID: 37634410](https://pubmed.ncbi.nlm.nih.gov/37634410/), [PMID: 35274760](https://pubmed.ncbi.nlm.nih.gov/35274760/)), and appears in breast-cancer prognostic gene signatures ([PMID: 35441810](https://pubmed.ncbi.nlm.nih.gov/35441810/), [PMID: 35120331](https://pubmed.ncbi.nlm.nih.gov/35120331/)).

Despite this oncogenic role, the 5 hemizygous MCTS1-null males exhibited **only isolated mycobacterial disease** with otherwise normal immunity, growth, development, and no reported malignancy. The authors note: *"the lack of MCTS1-dependent translation re-initiation and ribosome recycling seems to be otherwise physiologically redundant in these patients"* ([PMID: 37875108](https://pubmed.ncbi.nlm.nih.gov/37875108/)). This tells us that, in humans, MCTS1's translational function is largely dispensable for viability and development, and that its physiological non-redundancy is confined to the anti-mycobacterial IFN-γ axis.

### Finding 4 — IMD118 lies on the IL-23-to-IFN-γ axis, independently validated by IL23R and IL-23 deficiencies

IMD118 is mechanistically embedded within the well-characterized IL-12/IL-23/IFN-γ circuit whose disruption defines MSMD. The essential role of IL-23 was established by Philippot et al.: *"Human IL-23 is essential for IFN-γ-dependent immunity to mycobacteria"* ([PMID: 36763636](https://pubmed.ncbi.nlm.nih.gov/36763636/)). Independent genetic validation comes from IL23R deficiency: a homozygous R381X mutation in *IL23R* causes MSMD, where *"impaired IL-23 immunity caused by a homozygous R381X mutation in IL23R underlies MSMD"* ([PMID: 35829840](https://pubmed.ncbi.nlm.nih.gov/35829840/)), producing impaired IL-23-mediated STAT3 phosphorylation, reduced IFN-γ secretion, and isolated disseminated BCG/NTM disease.

The effector cells are innate-like T cells. MAIT cells recognize mycobacterial vitamin-B metabolites presented on MR1 and produce IFN-γ, TNF, and granzyme B, and are reduced/exhausted in active tuberculosis ([PMID: 37147816](https://pubmed.ncbi.nlm.nih.gov/37147816/), [PMID: 41707313](https://pubmed.ncbi.nlm.nih.gov/41707313/)). MCTS1 deficiency impairs JAK2 → IL-23 signaling → IFN-γ from MAIT/γδ cells, placing IMD118 firmly in the same functional pathway as IL12B, IL12RB1, IL23R, IFNGR1/2, STAT1, and the other MSMD genes.

### Finding 5 — Clinical spectrum: infantile-onset disseminated mycobacteriosis with recovery after early childhood

The OMIM #301115 Clinical Synopsis, derived from Bohlen et al. 2023, describes the clinical picture of the 5 unrelated males (aged 3–18 years at report). **Disseminated mycobacterial disease developed between 3 and 12 months of age, usually after BCG vaccination.** Reported organ-system features and suggested HPO terms include:

| Feature | HPO term |
|---|---|
| Hepatomegaly | HP:0002240 |
| Splenomegaly | HP:0001744 |
| Osteomyelitis | HP:0002754 |
| Fever | HP:0001945 |
| Lymphadenopathy / enlarged lymph nodes | HP:0002716 |
| Abscess | HP:0025615 |
| Disseminated mycobacteriosis | (BCG/NTM) |

Immunologically, patients had **normal numbers of circulating leukocyte subsets** — routine immune workup is typically unrevealing, a hallmark of MSMD that necessitates molecular diagnosis. Most patients recover with treatment and remain asymptomatic after early childhood. The source data underlie the OMIM synopsis: *"We report X-linked recessive MCTS1 deficiency in men with mycobacterial disease from kindreds of different ancestries"* ([PMID: 37875108](https://pubmed.ncbi.nlm.nih.gov/37875108/)).

### Finding 6 — JAK2's selective MCTS1-dependence is caused by two ultra-short start-stop uORFs (stuORFs); exogenous IFN-γ responses remain intact

The molecular reason JAK2 is uniquely vulnerable among the many proteins translated in the cell was resolved by 5′UTR reporter assays. Among **17 MSMD/IFN-γ-immunity genes** tested in MCTS1-KO HeLa cells, **only JAK2 showed a >65% decrease in translation**, which was rescued by wild-type MCTS1 but not by patient variants or a synthetic loss-of-function control (A109D). The *JAK2* 5′UTR contains three uORFs, two of which are **ultra-short start-stop "stuORFs"** (uORF1, uORF2). In the absence of MCTS1, 40S ribosomes stall (a "roadblock") at these stuORF stop codons, blocking re-initiation at the JAK2 main ORF — confirmed directly by accumulation of 40S ribosomal footprints. CRISPR MCTS1-knockout in THP-1 monocytes reproducibly lowered endogenous JAK2 across 5 independent clones.

Functionally, patient leukocytes had **impaired IFN-γ production after BCG stimulation** and impaired IL-23 responses (but normal IL-12 responses), yet retained **NORMAL responses to exogenous IFN-γ and IFN-α**. This localizes the defect upstream of the IFN-γ receptor and predicts that exogenous IFN-γ can bypass the block.

The protein architecture underpinning MCTS1's role was characterized earlier: *"MCT-1 contains the PUA domain, a recently described RNA-binding domain that is found in several tRNA and rRNA modification enzymes... MCT-1 protein interacts with the cap complex through its PUA domain and recruits the density-regulated protein (DENR/DRP), containing the SUI1 translation initiation domain"* ([PMID: 16982740](https://pubmed.ncbi.nlm.nih.gov/16982740/)).

### Finding 7 — Prognosis is generally favorable but the disease can be fatal (1 of 5 patients died)

Of the 5 hemizygous MCTS1-deficient males, **one died of disseminated mycobacterial disease**; the remaining four responded to antimycobacterial treatment, had no other infections, and showed normal growth and development. The redundancy of MCTS1 outside the mycobacterial axis is emphasized by the authors: *"Surprisingly, the lack of MCTS1-dependent translation re-initiation and ribosome recycling seems to be otherwise physiologically redundant in these patients"* ([PMID: 37875108](https://pubmed.ncbi.nlm.nih.gov/37875108/)). The preserved response to exogenous IFN-γ and IFN-α provides both a favorable prognostic indicator and a therapeutic target.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **hemizygous loss-of-function mutation in *MCTS1*** (Xq24; frameshift, splice-site, or in-frame 3′ deletion) **leads to** complete absence of functional MCTS1 protein in a male (X-linked recessive; single X chromosome). *[demonstrated]*
2. Loss of MCTS1 **results in** failure of MCTS1/DENR-mediated 40S ribosome recycling and translation re-initiation. *[demonstrated in vitro and in cells]*
3. At the *JAK2* mRNA, the two ultra-short start-stop uORFs (stuORFs) in the 5′UTR **cause** 40S ribosomes to stall at the stuORF stop codons (a translational roadblock), which **blocks** re-initiation at the JAK2 main ORF. *[demonstrated by 40S footprint accumulation and 5′UTR reporter assays]*
4. Blocked re-initiation **leads to** selectively reduced JAK2 protein in all cell types, including T lymphocytes and phagocytes, while most other proteins are unaffected. *[demonstrated]*
5. Reduced JAK2 **results in** impaired signal transduction downstream of the IL-23 receptor (and partial impairment of IL-12 signaling). *[demonstrated — impaired IL-23 response, normal IL-12 response in patient cells]*
6. Impaired IL-23 signaling **preferentially impairs** IFN-γ production by innate-like adaptive **MAIT and γδ T lymphocytes** upon mycobacterial challenge. *[demonstrated]*
7. Deficient IFN-γ **fails to** activate macrophages to control intracellular mycobacteria. *[inferred from the established MSMD paradigm — IFN-γ is the central macrophage-activating cytokine]*
8. Failure of macrophage activation **leads to** uncontrolled proliferation of weakly virulent mycobacteria (BCG, NTM), **resulting in** disseminated mycobacterial disease with fever, lymphadenopathy, hepatosplenomegaly, abscesses, and osteomyelitis in infancy. *[demonstrated clinically]*

**Branch point (bypass):** Because the lesion is upstream of the IFN-γ receptor, exogenous IFN-γ can activate macrophages directly (patient cells respond normally to IFN-γ and IFN-α) → therapeutic bypass and generally favorable prognosis.

```
 MCTS1 LoF (Xq24, hemizygous male)
        │ loss of 40S recycling / reinitiation factor
        ▼
 JAK2 stuORF roadblock in 5'UTR ──► 40S ribosome stall
        │ selective translational block (>65% ↓ JAK2)
        ▼
 ↓ JAK2 protein (all cell types)
        │
        ▼
 impaired IL-23 signaling (± partial IL-12)      [IL-12 response NORMAL]
        │
        ▼
 ↓ IFN-γ from MAIT & γδ T cells (mycobacterial challenge)
        │
        ▼
 macrophages not activated ──► uncontrolled mycobacteria
        │                                   ▲
        ▼                                   │ BYPASS
 disseminated mycobacterial disease   exogenous IFN-γ (response intact)
 (fever, HSM, lymphadenopathy,
  abscess, osteomyelitis; infancy)
```

### Upstream vs downstream

- **Upstream / initiating:** MCTS1 loss → global translation-recycling defect (a general molecular lesion).
- **Bottleneck / specificity-determining:** JAK2 stuORFs — the single feature that channels a general translation defect into a narrow clinical phenotype.
- **Downstream / effector:** IL-23 signaling → MAIT/γδ IFN-γ → macrophage activation → mycobacterial control.

### Ontology term suggestions

- **Gene/protein:** *MCTS1* (HGNC:7838), *JAK2* (HGNC:6192), *DENR*, *IL23R*, *IL12B*
- **GO biological process:** regulation of translational initiation (GO:0006446), positive regulation of interferon-gamma production (GO:0032729), response to molecule of bacterial origin, ribosomal subunit recycling
- **GO cellular component:** cytosolic ribosome (GO:0022626), cytosol (GO:0005829), messenger ribonucleoprotein / cap complex
- **CL cell types:** mucosal invariant T cell / MAIT (CL:0000940), gamma-delta T cell (CL:0000798), macrophage (CL:0000235), monocyte (CL:0000576)
- **UBERON anatomy:** liver (UBERON:0002107), spleen (UBERON:0002106), lymph node (UBERON:0000029), bone (UBERON:0001474)
- **NCIT treatment:** recombinant interferon gamma; antimycobacterial therapy; hematopoietic stem cell transplantation
- **Disease:** MONDO:0958030 (IMD118)

---

## Section-by-Section Report Content

### 1. Disease Information
IMD118 is an X-linked recessive inborn error of immunity within the MSMD spectrum, characterized by selective susceptibility to weakly virulent mycobacteria (BCG vaccine strain and non-tuberculous mycobacteria). **Identifiers:** OMIM #301115; MONDO:0958030; gene *MCTS1* (Xq24). ICD-11 maps to inborn errors of immunity / MSMD categories; no dedicated ICD-10 code. Synonyms: **MCTS1 deficiency**, **X-linked MCTS1 deficiency**, MSMD due to MCTS1 deficiency. The information is derived from an **aggregated disease-level primary report** (Bohlen et al. 2023, 5 individual patients) and OMIM, not from EHR-scale data.

### 2. Etiology
**Causal factor:** monogenic — hemizygous loss-of-function variants in *MCTS1*. **Genetic risk factor:** male sex (X-linked recessive; a single mutant X allele is sufficient in males). **Environmental trigger:** BCG vaccination and exposure to environmental (non-tuberculous) mycobacteria precipitate disease; the mutation is necessary, mycobacterial exposure is the environmental precipitant. No protective genetic variants are described; **exogenous IFN-γ acts as an acquired protective/therapeutic factor** because responses to it are intact. **Gene–environment interaction:** the classic MSMD interaction — an inherited IL-23→IFN-γ axis defect that becomes clinically manifest only upon mycobacterial exposure (especially live BCG vaccine).

### 3. Phenotypes
Predominantly **infectious/physical manifestations** rather than behavioral. Onset is **infantile (3–12 months)**, typically post-BCG. Features (with qualitative frequencies given the 5-patient series): disseminated mycobacteriosis (defining), fever (HP:0001945), lymphadenopathy (HP:0002716), hepatomegaly (HP:0002240), splenomegaly (HP:0001744), abscess (HP:0025615), osteomyelitis (HP:0002754). Severity is variable — from recoverable disseminated disease to fatal dissemination. Progression is **episodic/acute during active infection**, with recovery and asymptomatic status after early childhood in survivors. Quality-of-life impact is concentrated in infancy/early childhood during active infection; survivors have generally normal function thereafter.

### 4. Genetic / Molecular Information
**Causal gene:** *MCTS1* (Xq24; NCBI Gene 28985; HGNC:7838). **Variant types among 5 patients:** 2 frameshift, 1 splice-site, 2 in-frame 3′ deletions (both → p.Ala133_Lys181del). **Classification:** pathogenic loss-of-function (ACMG). **Zygosity/origin:** germline, hemizygous in males. **Functional consequence:** complete loss of function → loss of 40S recycling/reinitiation → selectively reduced JAK2 translation. **Allele frequency:** extremely rare/private; not established as recurrent in gnomAD. **Modifier genes:** none formally identified. **Epigenetics/chromosomal abnormalities:** none reported; the mechanism is translational, not epigenetic.

### 5. Environmental Information
The key environmental factors are **mycobacterial exposures** — live attenuated **BCG vaccine** (Mycobacterium bovis BCG) and environmental **non-tuberculous mycobacteria (NTM)**. No toxin, radiation, pollution, occupational, or lifestyle factors are implicated. Infectious agents are causative triggers acting on the genetic substrate rather than independent causes.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full ordered causal chain. In brief: MCTS1 LoF → failure of 40S ribosome recycling/reinitiation → JAK2 stuORF roadblock → selective JAK2 depletion → impaired IL-23 (and partial IL-12) signaling → reduced IFN-γ from MAIT/γδ T cells → failed macrophage activation → disseminated mycobacterial disease. Molecular pathway: **JAK-STAT (JAK2) / IL-23→IFN-γ axis**. Cellular process: cytokine signaling and antimicrobial macrophage activation. Protein dysfunction: loss of function of a ribosome-recycling factor (MCTS1) causing loss of a downstream kinase (JAK2). Immune involvement: immunodeficiency (not autoimmunity).

### 7. Anatomical Structures Affected
**Primary organs:** reticuloendothelial/lymphoid system — **liver** (UBERON:0002107), **spleen** (UBERON:0002106), **lymph nodes** (UBERON:0000029), **bone/bone marrow** (osteomyelitis; UBERON:0001474). **Body systems:** immune/hematopoietic and, via sites of mycobacterial dissemination, potentially multi-organ. **Cell populations:** MAIT cells (CL:0000940), γδ T cells (CL:0000798), macrophages/monocytes (CL:0000235/CL:0000576) — because the JAK2 defect is present in all cell types tested, including phagocytes. **Subcellular:** cytosolic ribosome/translation machinery (GO:0022626). **Lateralization:** not applicable (systemic/bilateral dissemination).

### 8. Temporal Development
**Onset:** infantile, 3–12 months, typically after BCG vaccination; onset pattern acute/subacute. **Course:** episodic active disease during infection with recovery in survivors; survivors are typically asymptomatic after early childhood. **Critical period:** early infancy around BCG exposure is the window of vulnerability and of opportunity for early recognition/intervention. **Remission:** treatment-induced with antimycobacterial therapy (± IFN-γ).

### 9. Inheritance and Population
**Inheritance:** X-linked recessive; affects males, mothers are obligate carriers. **Penetrance:** appears high in exposed hemizygous males but based on only 5 patients. **Expressivity:** variable (recovery to death). **Epidemiology:** ultra-rare — 5 reported patients worldwide; prevalence/incidence not estimable. **Populations:** four ancestries reported (Chinese, Finnish, Iranian, Saudi Arabian) — no single founder population. **Sex ratio:** essentially all affected are male (X-linked recessive). **Consanguinity:** relevant for autosomal recessive MSMD genes but less so here given X-linkage; the geographic spread suggests independent (private) mutations rather than a founder effect. **Carrier frequency:** unknown/very low.

### 10. Diagnostics
Routine immune workup is typically **normal** (normal circulating leukocyte subsets), so diagnosis rests on **molecular genetics**. Recommended approach: **whole-exome or whole-genome sequencing / targeted MSMD gene panels** including *MCTS1*, prompted by disseminated BCG/NTM disease in an otherwise healthy infant. Functional confirmation: reduced JAK2 protein, impaired IFN-γ after BCG stimulation, impaired IL-23 (but normal IL-12) responses, and **preserved responses to exogenous IFN-γ/IFN-α** — the last both diagnostic and therapeutically informative. Microbiology: blood/tissue mycobacterial culture and, increasingly, metagenomic next-generation sequencing (mNGS) to identify unculturable NTM. **Differential diagnosis:** other MSMD genotypes — IL12RB1, IL12B, IFNGR1/2, STAT1, ISG15, IRF8, IL23R, RORC, NEMO, CYBB — distinguished by their specific gene defects and, in some, broader infectious susceptibility.

### 11. Outcome / Prognosis
**Generally favorable but potentially fatal:** 1 of 5 patients died of disseminated mycobacterial disease; 4 recovered with antimycobacterial therapy, had no other infections, and showed normal growth and development. **Prognostic factors:** early diagnosis and prompt antimycobacterial (± IFN-γ) therapy; intact response to exogenous IFN-γ is a favorable feature. Long-term survivors are typically asymptomatic after early childhood. Given the tiny cohort, survival statistics are indicative rather than definitive.

### 12. Treatment
**Antimycobacterial therapy** is the cornerstone (multidrug regimens directed at BCG/NTM). **Recombinant IFN-γ** is a rational adjunct because patient cells respond normally to it, bypassing the upstream block — a strategy with established benefit in other MSMD genotypes (e.g., partial IFNGR1 and IL12RB1 defects). **Hematopoietic stem cell transplantation** is a consideration in severe/refractory MSMD generally, though not specifically reported for IMD118. No pharmacogenomic, gene, RNA, or targeted small-molecule therapies exist yet for MCTS1 deficiency. Suggested **NCIT** terms: recombinant interferon gamma; antimycobacterial agent; hematopoietic stem cell transplantation.

### 13. Prevention
**Primary prevention:** in families with a known *MCTS1* variant, **avoid live BCG vaccination** in at-risk male infants until immune status is clarified — BCG is the principal precipitant. **Secondary prevention:** early recognition of disseminated mycobacterial disease and prompt therapy. **Genetic counseling:** X-linked recessive inheritance — carrier mothers have a 50% chance of transmitting the variant; sons of carriers have a 50% risk of being affected, daughters a 50% chance of being carriers. **Carrier/prenatal testing** and cascade testing are available once the familial variant is known. **Tertiary prevention:** antimycobacterial prophylaxis and monitoring in affected individuals.

### 14. Other Species / Natural Disease
Species affected: **human (*Homo sapiens*, NCBI Taxon 9606)** — the disease is described only in humans. Mechanistic conservation is strong: the MCTS1/DENR–eIF2D recycling system has direct yeast counterparts (Tma20/Tma22/Tma64), demonstrating deep evolutionary conservation of the underlying translation machinery ([PMID: 30146315](https://pubmed.ncbi.nlm.nih.gov/30146315/), [PMID: 38903097](https://pubmed.ncbi.nlm.nih.gov/38903097/)). Orthologous *Mcts1* exists in mouse and other vertebrates. No naturally occurring animal disease (OMIA) is reported. No zoonotic component.

### 15. Model Organisms
No dedicated *Mcts1*-deficient mammalian disease model of IMD118 has been reported. **In vitro/cellular models** were central to the discovery: MCTS1-knockout HeLa cells (5′UTR reporter screens), CRISPR MCTS1-knockout THP-1 monocytes (endogenous JAK2 reduction across 5 clones), and patient-derived leukocytes. **Yeast** (*Saccharomyces cerevisiae*, Tma20/Tma22/Tma64) is a powerful model for the ribosome-recycling/reinitiation mechanism itself. These systems recapitulate the molecular defect (JAK2 translational block, ribosome stalling) but not the whole-organism immunophenotype; a conditional or humanized mouse expressing the *JAK2* stuORF-containing 5′UTR would be needed to model the immunological disease in vivo.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [37875108](https://pubmed.ncbi.nlm.nih.gov/37875108/) | *Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria* | **Primary/defining source.** Identifies IMD118, the 5 patients, variant spectrum, JAK2 stuORF mechanism, IL-23→IFN-γ/MAIT-γδ axis, outcomes (1 death), preserved exogenous IFN-γ response. |
| [30146315](https://pubmed.ncbi.nlm.nih.gov/30146315/) | *Tma64/eIF2D, Tma20/MCT-1, Tma22/DENR recycle post-termination 40S subunits in vivo* | Establishes MCTS1/DENR/eIF2D as 40S recycling factors; evolutionary conservation. |
| [38903097](https://pubmed.ncbi.nlm.nih.gov/38903097/) | *Impacts of yeast Tma20/MCTS1, Tma22/DENR and Tma64/eIF2D on translation reinitiation* | Shows MCTS1/DENR enhance reinitiation at uORFs — mechanism underlying JAK2 dependence. |
| [16982740](https://pubmed.ncbi.nlm.nih.gov/16982740/) | *MCT-1 protein interacts with the cap complex...* | Defines MCTS1 PUA domain, cap-complex interaction, DENR recruitment. |
| [35115540](https://pubmed.ncbi.nlm.nih.gov/35115540/) | *Cyclin B/CDK1 and Cyclin A/CDK2 phosphorylate DENR...* | Establishes MCTS1/DENR as oncogenes and cell-cycle-regulated uORF translation factors. |
| [37634410](https://pubmed.ncbi.nlm.nih.gov/37634410/) / [35274760](https://pubmed.ncbi.nlm.nih.gov/35274760/) | MCTS1 in laryngeal squamous cell carcinoma | Oncogenic role of MCTS1 (contrast with benign germline-loss phenotype). |
| [36763636](https://pubmed.ncbi.nlm.nih.gov/36763636/) | *Human IL-23 is essential for IFN-γ-dependent immunity to mycobacteria* | Validates the IL-23→IFN-γ axis that MCTS1/JAK2 loss disrupts. |
| [35829840](https://pubmed.ncbi.nlm.nih.gov/35829840/) | *Homozygous stop mutation in IL23R causes MSMD* | Independent genetic validation that disrupting IL-23 signaling causes MSMD. |
| [37147816](https://pubmed.ncbi.nlm.nih.gov/37147816/) / [41707313](https://pubmed.ncbi.nlm.nih.gov/41707313/) | MAIT cells in mycobacterial immunity | Effector-cell biology: MAIT cells produce IFN-γ via MR1, reduced in active TB. |
| [40656276](https://pubmed.ncbi.nlm.nih.gov/40656276/) / [41786143](https://pubmed.ncbi.nlm.nih.gov/41786143/) / [41048447](https://pubmed.ncbi.nlm.nih.gov/41048447/) | MSMD overviews & management | Context for MSMD classification, diagnostics, and IFN-γ/antimycobacterial/HSCT management. |

**Evidence source types:** IMD118-defining data are **human clinical + in vitro/cellular** (Bohlen 2023); mechanistic recycling/reinitiation data are **in vitro + model organism (yeast)**; pathway validation is **human genetic** (IL23R, IL-23); oncogenic role is **in vitro / tumor genomics**.

---

## Limitations and Knowledge Gaps

1. **Single defining cohort (n = 5).** Nearly all disease-specific knowledge derives from one report ([PMID: 37875108](https://pubmed.ncbi.nlm.nih.gov/37875108/)). Prevalence, penetrance, expressivity, sex-specific carrier phenotypes, and long-term outcomes are therefore uncertain.
2. **No formal epidemiology.** Prevalence and incidence cannot be estimated; the disease is ultra-rare and likely underdiagnosed.
3. **No animal model of the disease.** Mechanistic work used cell lines and yeast; whole-organism recapitulation (e.g., stuORF-humanized mouse) is absent, so in vivo immunodynamics remain inferred.
4. **Therapeutic evidence is indirect.** IFN-γ benefit is inferred from preserved in vitro responses and from other MSMD genotypes, not from a trial in MCTS1-deficient patients.
5. **Spectrum of mycobacterial species and non-mycobacterial risk** is incompletely defined given the small cohort; whether MCTS1-deficient patients have subtle susceptibility to other intracellular pathogens (as some MSMD genotypes do) is unknown.
6. **Female carriers / X-inactivation effects** have not been characterized.
7. **Cancer risk over the lifespan** is unassessed — germline MCTS1 loss is oncologically "silent" in childhood, but the long-term consequences of losing an oncogene's function are unstudied.

## Proposed Follow-up Experiments / Actions

1. **International case-finding and registry.** Add *MCTS1* to MSMD/IEI sequencing panels worldwide and pool cases (e.g., via GeneMatcher) to define penetrance, expressivity, microbial spectrum, and outcomes.
2. **Therapeutic evaluation of recombinant IFN-γ** as adjunct to antimycobacterial therapy in confirmed patients, leveraging their intact IFN-γ responses; document response rates and adverse events.
3. **Generate an in vivo model** — a knock-in mouse humanizing the *JAK2* 5′UTR stuORFs on an *Mcts1*-deficient background, or a conditional myeloid/T-cell *Mcts1* knockout — to test whether the JAK2→IL-23→IFN-γ chain and mycobacterial susceptibility are recapitulated.
4. **Ribosome profiling** in patient-derived macrophages and MAIT/γδ cells to catalog the full set of MCTS1-dependent (stuORF/uORF) transcripts beyond JAK2 and confirm JAK2's privileged dependence.
5. **Vaccination guidance:** formalize the recommendation to withhold live BCG in at-risk male infants of carrier mothers pending genetic clarification.
6. **Long-term surveillance** of survivors for late infections and — given MCTS1's oncogene status — for any oncologic outcomes, to establish lifetime prognosis.
7. **Structural/biophysical work** on how patient variants (esp. p.Ala133_Lys181del) disrupt MCTS1–DENR–ribosome interactions, to inform potential small-molecule or read-through therapeutic strategies.

---

*Report compiled from 7 confirmed findings and 35 reviewed papers over 5 investigation iterations. All disease-specific clinical and mechanistic claims trace primarily to Bohlen et al. 2023 ([PMID: 37875108](https://pubmed.ncbi.nlm.nih.gov/37875108/)); mechanistic and pathway claims are corroborated by the cited translation-machinery and MSMD literature.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_118-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_118-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 12 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0958030` (3 mentions) - the report calls it "IMD118"; MONDO calls it **immunodeficiency 118**
- `UBERON:0002107` (2 mentions) - the report calls it "UBERON anatomy:** liver", "liver"; UBERON calls it **liver**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002716` (2 mentions) - the report calls it "Lymphadenopathy / enlarged lymph nodes"; HP calls it **Lymphadenopathy**
- `GO:0006446` (1 mention) - the report calls it "GO biological process:** regulation of translational initiation"; GO calls it **regulation of translational initiation**
- `GO:0022626` (2 mentions) - the report calls it "GO cellular component:** cytosolic ribosome"; GO calls it **cytosolic ribosome**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:7838` - called "MCTS1", "Gene/protein:** *MCTS1"
- `UBERON:0002107` - called "UBERON anatomy:** liver", "liver"