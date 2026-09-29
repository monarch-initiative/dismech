---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T23:43:47.054105'
end_time: '2026-09-02T00:06:12.121952'
duration_seconds: 1345.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Portal Hypertension Noncirrhotic 2
  mondo_id: ''
  category: Disease
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
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 44
  verified: 43
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 30
  labels_matching: 19
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: CL:1000488
    reported_labels:
    - liver sinusoidal endothelial cell
    ontology_label: cholangiocyte
  - term_id: UBERON:0002106
    reported_labels:
    - spleen
    - Secondary organ involvement:** **spleen
    ontology_label: spleen
  - term_id: GO:0005765
    reported_labels:
    - Subcellular level:** GIMAP5 localizes to the **lysosomal membrane
    ontology_label: lysosomal membrane
  labels_variant: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Portal_Hypertension_Noncirrhotic_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Portal_Hypertension_Noncirrhotic_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Portal Hypertension Noncirrhotic 2
- **MONDO ID:**  (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Portal Hypertension Noncirrhotic 2** covering all of the
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

# Portal Hypertension, Noncirrhotic, 2 (PHNC2 / NCPH2) — Comprehensive Disease Report

**Disease:** Portal Hypertension, Noncirrhotic, 2
**MONDO:** MONDO:0030397 · **OMIM:** #619463 · **Causal gene:** *GIMAP5* (HGNC:18005)
**Evidence base:** Aggregated disease-level resources (OMIM, MONDO, HPO, gnomAD, UniProt) plus individual-patient reports (~21 patients published to date). Fewer than ~25 molecularly confirmed patients worldwide; all conclusions rest on small case series, a landmark human+mouse mechanistic study, and rodent models.

---

## Summary (Answer to the Research Question)

Portal Hypertension, Noncirrhotic, 2 (PHNC2) is a **rare autosomal-recessive disorder caused by biallelic loss-of-function variants in *GIMAP5***, a small organellar GTPase of the immunity-associated protein (IAN) family expressed selectively in **lymphocytes and endothelial cells**. Loss of GIMAP5 produces a **two-arm disease**: (1) a **hepatic vascular arm** in which GIMAP5-deficient liver sinusoidal endothelial cells (LSECs) fail to maintain their identity (via reduced GATA4), undergo **capillarization**, and cause **noncirrhotic (porto-sinusoidal) portal hypertension**; and (2) an **immune arm** with lymphopenia, autoimmune cytopenias, and recurrent infections. A unifying biochemical lesion is **pathological accumulation of long-chain ceramides** (GIMAP5 normally restrains CK2-driven ceramide synthase activity), driving cellular senescence in both endothelium and lymphocytes. Presentation is typically in **childhood** with splenomegaly, thrombocytopenia, esophageal varices, and elevated transaminases, without cirrhosis.

---

## 1. Disease Information

**Overview.** PHNC2 is a Mendelian cause of **idiopathic/noncirrhotic portal hypertension**, now classified within the spectrum of **porto-sinusoidal vascular disorder (PSVD)**. It is distinctive because portal hypertension arises from a primary **endothelial** defect rather than from hepatocellular injury or cirrhosis, and it co-occurs with an **inborn error of immunity**.

**Key identifiers**
- **MONDO:** MONDO:0030397 ("portal hypertension, noncirrhotic, 2"; synonym **NCPH2**)
- **OMIM:** #619463 (phenotype)
- **UMLS:** C5561948 · **MedGen:** 1794158
- **Gene:** *GIMAP5* — HGNC:18005; NCBI Gene 55340; Ensembl ENSG00000196329; UniProt **Q96F15**; gene **MIM 608086**; cytoband **7q36.1**
- **ICD-10:** K76.6 (portal hypertension; no PHNC2-specific code) · **ICD-11:** DB98.5 region (non-cirrhotic portal hypertension/idiopathic; no specific code)
- **MeSH:** most closely "Hypertension, Portal" (D006975); no PHNC2-specific MeSH
- **Orphanet:** no PHNC2-specific ORPHA; overlaps "Idiopathic non-cirrhotic portal hypertension"/PSVD

**Synonyms / alternative names:** NCPH2; GIMAP5 deficiency; GIMAP5-related noncirrhotic portal hypertension; GIMAP5-related porto-sinusoidal vascular disorder; (historically discussed with "idiopathic noncirrhotic portal hypertension," INCPH). Note: **PHNC1 (INCPH1, OMIM 617068)** is a distinct entity caused by *DGUOK* (PMID 26874653).

**Data provenance:** Disease-level ontologies/aggregators + individual patient case reports/series (human clinical), complemented by mouse and rat model data and in-vitro mechanistic studies.

---

## 2. Etiology

**Primary cause — genetic (monogenic).** Biallelic (homozygous or compound-heterozygous) **loss-of-function variants in *GIMAP5***. *"we demonstrate homozygous damaging mutations in GIMAP5, a small organellar GTPase, in four families with unexplained portal hypertension"* (Drzewiecki et al., PMID 33956074).

**Genetic risk factors**
- **Causal variants:** recessive *GIMAP5* alleles (see §4). Disease requires **two damaged alleles**.
- **Consanguinity** is a major contributor: three of four index families were consanguineous (first-cousin unions) (PMID 33956074).
- **Founder/recurrent allele:** **p.Leu204Pro** recurs across independent reports and is relatively common (gnomAD AF ≈2.1×10⁻³), so it is the most likely allele to appear in homozygous or compound-heterozygous state.

**Environmental risk factors.** None established. No toxin, infection, diet, or occupational exposure is required for disease; the phenotype is genetically determined. (Of note, acquired phenocopies of noncirrhotic portal hypertension exist — e.g., didanosine/thioguanine exposure, oxaliplatin — but these are not PHNC2.)

**Protective factors.** No genetic or environmental protective factors are defined. At the population level *GIMAP5* is **LOF-tolerant** (gnomAD pLI = 0.003; observed/expected LOF = 8/9.9), so **monoallelic carriers are generally healthy** — heterozygosity is effectively "protective" relative to the biallelic state.

**Gene–environment interactions.** A 2026 report raised the hypothesis that **partial (monoallelic) GIMAP5 deficiency might subtly predispose to localized vascular anomalies under specific environmental/epigenetic conditions via multi-hit mechanisms** — the dizygotic twin carrying a single p.Leu204Pro allele showed a localized fibro-adipose vascular anomaly but no immune defect (PMID 42358996). This remains speculative.

---

## 3. Phenotypes (with HPO terms, type, and frequency)

Onset is typically in **infancy/childhood**; severity is **variable**; the hepatic disease is **chronic and progressive**.

| Phenotype | HPO | Type | Frequency / notes |
|---|---|---|---|
| Portal hypertension | HP:0001409 | Clinical sign | Defining; universal |
| Splenomegaly | HP:0001744 | Physical sign | All affected subjects (PMID 33956074) |
| Thrombocytopenia | HP:0001873 | Lab abnormality | Near-universal (hypersplenism) |
| Elevated transaminases | HP:0002910 | Lab abnormality | Near-universal |
| Esophageal varices | HP:0002040 | Clinical sign | Near-universal; 7 subjects endoscopically confirmed |
| Nodular regenerative hyperplasia of liver | HP:0011954 | Pathology | Present on biopsy |
| Hepatomegaly | HP:0002240 | Physical sign | Common |
| Elevated GGT | HP:0030948 | Lab abnormality | Reported |
| Ascites | HP:0001541 | Clinical sign | Complication of portal hypertension |
| Ecchymosis / petechiae / epistaxis | HP:0031364 / HP:0000967 / HP:0000421 | Signs | Bleeding from thrombocytopenia/varices |
| Hemoptysis | HP:0002105 | Sign | Reported |
| Recurrent infections | HP:0002719 | Sign | Immune arm |
| Autoimmune cytopenias (hemolytic anemia, immune thrombocytopenia) | HP:0001890 / HP:0001873 | Lab/clinical | Immune dysregulation |
| Lymphopenia | HP:0001888 | Lab abnormality | T (and NK) lymphopenia; T-cell exhaustion |
| Hepatocellular carcinoma | HP:0001402 | Neoplasm | Listed as possible long-term risk |
| Fatigue | HP:0012378 | Symptom | Nonspecific |

**Age of onset:** neonatal–childhood (pediatric); portal hypertension complications and immune features generally manifest in the first two decades.
**Progression:** progressive liver/vascular disease (one patient developed worsening coagulopathy and direct hyperbilirubinemia after shunt surgery) (PMID 33956074).
**Quality-of-life impact:** substantial — recurrent variceal bleeding risk, transfusion-dependent cytopenias, infection susceptibility, growth/activity limitation, and the burden of surveillance endoscopy and possible transplantation. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease.

---

## 4. Genetic / Molecular Information

**Causal gene:** ***GIMAP5*** (GTPase, IMAP family member 5) — HGNC:18005; NCBI Gene 55340; Ensembl ENSG00000196329; UniProt **Q96F15** (307 aa); gene **MIM 608086**; **7q36.1** (GRCh38 chr7:150,722,253–150,750,033, + strand). Part of the IAN GTPase cluster on 7q36.1; read-through transcript with upstream *GIMAP1* exists. Aliases: IAN5, IAN4L1, IROD, **NCPH2**.

**Protein architecture:** GIMAP5 is a small **AIG1-type guanine-nucleotide-binding (G) domain** GTPase (InterPro **IPR006703**; Pfam **PF04548** "AIG1 family"; PROSITE PS51720), belonging to the P-loop NTPase superfamily (IPR027417) and the **GTPase GIMA/IAN/Toc** family (IPR045058), with a C-terminal transmembrane anchor targeting it to lysosomal/endosomal membranes. The reported missense substitutions (I47T, P109L, L204P, L223P) map to/near this G-domain and are predicted to **destabilize the fold and abolish GTPase function**, consistent with the observed absent protein for null combinations.

**Pathogenic variants** (all **germline**, all **loss-of-function / recessive**):

| Variant (protein) | cDNA/type | Zygosity | Population frequency | Source |
|---|---|---|---|---|
| p.Ile47Thr (I47T) | missense | homozygous (kindred 1) | AF = 0 in gnomAD | PMID 33956074 |
| p.Pro109Leu (P109L) | missense | homozygous (kindred 3) | ultra-rare (1/251,400 alleles) | PMID 33956074 |
| p.Leu204Pro (L204P) | missense | homozygous (kindred 4); also compound-het | AF ≈2.1×10⁻³ (recurrent) | PMID 33956074, 29382851, 42358996 |
| p.Leu223Pro (L223P) | missense | homozygous (kindred 2) | rare | PMID 33956074 |
| p.Arg214Ter (R214*) | nonsense | compound-het with L204P | rare | PMID 42358996 |

- **Variant classification (ACMG/AMP):** the recurrent alleles are treated as pathogenic/likely pathogenic given segregation, absent/abolished protein, and functional data; many other *GIMAP5* entries in ClinVar are VUS or large 7q copy-number changes not specific to PHNC2.
- **Variant types:** predominantly **missense**; at least one **nonsense** (R214*). No pathogenic large structural rearrangement specific to PHNC2 is established (7q CNVs in ClinVar are contiguous-gene events, not PHNC2).
- **Functional consequence:** **loss of function** — e.g., compound-het L204P/R214* yields **absent GIMAP5 protein** on immunoblot (PMID 42358996). No gain-of-function or dominant-negative mechanism.
- **Somatic vs germline:** exclusively **germline**.

**Modifier genes.** None formally proven. Mechanistically, GIMAP5 stability requires the lysosomal **MFSD1–GLMP** complex (PMID 38055739), so *MFSD1/GLMP* are candidate biological modifiers; downstream **GATA4** and **GSK3β/CK2/ceramide-synthase** nodes modulate phenotype in models.

**Epigenetic information / chromosomal abnormalities.** No disease-specific DNA-methylation or histone signature reported. Contiguous 7q36 deletions/duplications affect *GIMAP5* among many genes but are not the mechanism of PHNC2.

---

## 5. Environmental Information

- **Environmental factors / toxins:** none required or established for PHNC2. (Toxic/drug-induced noncirrhotic portal hypertension — e.g., didanosine, thioguanine, arsenic, vinyl chloride, oxaliplatin — are separate acquired phenocopies to exclude.)
- **Lifestyle factors:** not applicable to disease causation.
- **Infectious agents:** not causal. However, because of the immune arm, patients suffer **recurrent/severe viral infections** as a *consequence* of the disease (e.g., severe viral infections in the proband, PMID 42358996). CHEBI/pathogen exposure is downstream, not upstream.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. Biallelic **loss-of-function variants in *GIMAP5*** **lead to** loss/instability of the GIMAP5 GTPase (compounded by loss of the stabilizing lysosomal **MFSD1–GLMP–GIMAP5** complex). *(demonstrated)*
2. GIMAP5 loss **results in** failure to restrain **protein kinase CK2**, which **leads to** over-activation of **ceramide synthases** and **pathological accumulation of long-chain ceramides**. *(demonstrated in T cells; inferred in endothelium)*
3. Ceramide overaccumulation **leads to** **cellular senescence / organelle (mitochondrial) dysfunction** in GIMAP5-expressing cells — **endothelial cells and lymphocytes**. *(demonstrated)*

**Branch A — hepatic vascular (portal hypertension):**
4a. In **liver sinusoidal endothelial cells (LSECs)**, GIMAP5 loss **results in** reduced **GATA4** (the transcription factor required for LSEC specification). *(demonstrated by scRNA-seq positioning GIMAP5 upstream of GATA4)*
5a. Reduced GATA4 **leads to** loss of LSEC identity → **capillarization** (loss of fenestrae, acquisition of a basement membrane, **CD34 positivity**) and reduction of macrovascular hepatic endothelial cells. *(demonstrated in humans and mice)*
6a. Sinusoidal capillarization / porto-sinusoidal remodeling (with **nodular regenerative hyperplasia** and obliterative portal venopathy — venules absent in portal areas) **increases intrahepatic vascular resistance**. *(demonstrated histologically)*
7a. Increased resistance **results in** **noncirrhotic portal hypertension** → splenomegaly, esophageal varices, ascites, variceal bleeding; thrombocytopenia via hypersplenism. *(clinical)*

**Branch B — immune (lymphopenia/autoimmunity):**
4b. In lymphocytes, GIMAP5 loss (via ceramide, impaired mitochondrial/ER Ca²⁺ homeostasis, ER-stress/CHOP apoptosis, and constitutive **GSK3β** activity restricting c-Myc/NFATc1) **leads to** **spontaneous T- and NK-cell apoptosis / impaired proliferation**. *(demonstrated in rat/mouse and patient cells)*
5b. Lymphopenia and immune dysregulation **result in** **recurrent infections, autoimmune cytopenias, T-cell exhaustion, and atypical memory B-cell expansion**. *(clinical)*

**Key point (branch independence):** The hepatic vascular disease is **cell-intrinsic to endothelium and lymphocyte-independent** — endothelial-specific *Gimap5* deletion reproduces capillarization, and *Gimap5^sph/sph;Rag1⁻/⁻* mice (lacking T/B cells) still develop the liver phenotype (PMID 33956074). This predicts HSCT will not reverse established portal hypertension.

### Category detail
- **Molecular pathways:** CK2 → ceramide-synthase/sphingolipid pathway (GO:0006672 ceramide metabolic process); **GATA4-dependent endothelial specification**; GSK3β signaling (Wnt/insulin-adjacent) controlling c-Myc and NFATc1; NF-κB/MAPK dysregulation in *Gimap5*-mutant T cells (PMID 16584774).
- **Cellular processes:** anti-apoptotic function (GO:0043066 negative regulation of apoptotic process); **cellular senescence** (GO:0090398); T-cell homeostasis (GO:0043029); endothelial cell differentiation (GO:0045446); autophagy/lysosomal biology.
- **Protein dysfunction:** loss of a small **AIG1-type G-domain GTPase** (Pfam PF04548; InterPro IPR006703; GO:0003924 GTPase activity; GO:0005525 GTP binding); missense variants in/around the G-domain destabilize/abolish the protein (loss of function).
- **Metabolic/lipidomic changes:** accumulation of **long-chain ceramides** (CHEBI:17761 ceramide) — a defining metabolic signature.
- **Immune involvement:** combined features of immunodeficiency (lymphopenia, infection) and autoimmunity (cytopenias) — an inborn error of immunity.
- **Tissue-damage mechanism:** endothelial capillarization/senescence → sinusoidal fibrosis-independent remodeling; progressive liver dysfunction.
- **Molecular profiling:** single-cell RNA-seq of GIMAP5-deficient mouse liver documented replacement of LSECs by capillarized endothelial cells and placed GIMAP5 upstream of GATA4 (PMID 33956074); T-cell proteomics/lipidomics documented the CK2–ceramide axis (PMID 38172257).

**GO / CL / CHEBI suggestions:** GO:0003924, GO:0005525, GO:0043066, GO:0090398, GO:0006672, GO:0045446, GO:0043029; CL:1000488 (liver sinusoidal endothelial cell), CL:0000115 (endothelial cell), CL:0000084 (T cell), CL:0000623 (NK cell), CL:0000182 (hepatocyte); CHEBI:17761 (ceramide).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **liver** (UBERON:0002107) — specifically the **hepatic sinusoid** (UBERON:0001281) and **portal venous system/portal vein** (UBERON:0002017). **Digestive/hepatobiliary and cardiovascular (portal venous) systems** are primarily involved.
- **Secondary organ involvement:** **spleen** (UBERON:0002106) — splenomegaly/hypersplenism; **esophagus** (UBERON:0001043) — varices; **bone marrow** (UBERON:0002371) and lymphoid organs — lymphopenia, extramedullary hematopoiesis (in models); gastrointestinal tract (variceal bleeding).
- **Tissue/cell level:** vascular **endothelium**, chiefly **liver sinusoidal endothelial cells (CL:1000488)**; **T lymphocytes (CL:0000084)** and **NK cells (CL:0000623)**; hepatocytes secondarily; platelets (consumed peripherally).
- **Subcellular level:** GIMAP5 localizes to the **lysosomal membrane (GO:0005765)** and **multivesicular body/endosome membrane (GO:0032585)** (UniProt Q96F15); older studies also implicated **ER (GO:0005783)** and **mitochondria (GO:0005739)** in T-cell survival/Ca²⁺ handling.
- **Localization / lateralization:** intra-abdominal, **bilateral/diffuse** hepatic involvement; not lateralized.

---

## 8. Temporal Development

- **Onset:** **congenital-to-pediatric**; portal hypertension and immune manifestations usually emerge in **infancy through adolescence**. Onset pattern is **insidious/chronic** (portal hypertension often detected via splenomegaly/thrombocytopenia or a variceal bleed).
- **Progression:** **chronic, progressive** hepatic vascular disease; can advance to decompensation (coagulopathy, hyperbilirubinemia) despite shunting (PMID 33956074). Immune disease can be **episodic** (autoimmune cytopenia flares, intercurrent infections).
- **Disease course/duration:** **lifelong**; no spontaneous remission of the vascular disease. Immune cytopenias can be **treatment-induced remission** (e.g., sirolimus) (PMID 42358996).
- **Critical periods / intervention windows:** early molecular diagnosis enables **variceal surveillance/prophylaxis**, infection prophylaxis, and consideration of HSCT before irreversible organ damage; the endothelial disease may have an early window before established capillarization/portal hypertension (inferred).

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (HP:0000007). Recurrence risk 25% for siblings of an affected proband.
- **Penetrance:** appears **high/complete** for biallelic LOF (all reported biallelic individuals affected), though phenotypic **expressivity is variable** (severity, relative weight of hepatic vs immune features).
- **Genetic anticipation / mosaicism:** not applicable / not reported.
- **Consanguinity:** a **major factor** — most index families are consanguineous (PMID 33956074).
- **Founder / recurrent allele:** **p.Leu204Pro** (AF ≈2.1×10⁻³) recurs and drives a disproportionate share of cases; no formal founder haplotype study published.
- **Carrier frequency:** *GIMAP5* is LOF-tolerant (gnomAD pLI=0.003); heterozygous carriers are healthy. Aggregate carrier frequency is low but non-trivial where p.L204P is present.
- **Epidemiology:** **ultra-rare** — on the order of **~20–25 molecularly confirmed patients** reported worldwide (≥4 families in the founding study plus subsequent case reports/series, ~21 patients reviewed by 2026). No reliable prevalence/incidence estimate (well under 1/1,000,000). Reported patients are geographically diverse (Turkey, Europe, China, North America).
- **Sex ratio:** no established skew (autosomal recessive). **Age distribution:** pediatric-predominant at diagnosis.

---

## 10. Diagnostics

**Genetic testing (definitive):**
- **Whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)** identifying **biallelic *GIMAP5*** variants is the diagnostic gold standard (high-depth WES used in the founding study; PMID 33956074). **GeneMatcher/trio exome** aids ultra-rare gene discovery.
- **Single-gene / panel testing:** *GIMAP5* can be included on **PSVD / noncirrhotic portal hypertension** and **inborn errors of immunity** gene panels; targeted testing for the recurrent p.L204P is reasonable in consanguineous pedigrees.
- **CMA/karyotype/FISH:** not primary; only relevant to exclude contiguous 7q36 CNVs. Mitochondrial/repeat-expansion testing not applicable.
- **Confirmatory functional test:** **GIMAP5 protein immunoblot** (absent protein confirms LOF) and **flow-cytometric immunophenotyping** (T/NK lymphopenia, T-cell exhaustion, atypical memory B cells) (PMID 42358996).

**Clinical/laboratory workup (supportive, to characterize the phenotype):**
- **Labs:** CBC (thrombocytopenia, cytopenias), transaminases (elevated), GGT (elevated), bilirubin/coagulation (with progression), lymphocyte subsets. LOINC-codable.
- **Liver histology (PSVD pattern):** **nodular regenerative hyperplasia**, **CD34-positive capillarized LSECs**, **obliterative portal venopathy** (absent portal venules), **no cirrhosis/significant fibrosis** (PMID 33956074). SNOMED CT: nodular regenerative hyperplasia of liver.
- **Endoscopy:** upper GI endoscopy for **esophageal/gastric varices**.
- **Imaging:** ultrasound/Doppler, CT/MRI showing **splenomegaly, portosystemic collaterals, patent portal vein** (excluding portal/splanchnic vein thrombosis); transient elastography typically discordant with severe portal hypertension (low fibrosis vs high pressure).

**Diagnostic criteria / differential.** No PHNC2-specific criteria; diagnosis = PSVD/noncirrhotic portal hypertension features + biallelic *GIMAP5*. **Differential diagnosis:** cirrhosis of any cause; portal/splenic vein thrombosis (extrahepatic); congenital hepatic fibrosis; schistosomiasis; drug/toxin-induced NRH (didanosine, thioguanine, oxaliplatin); other genetic PSVD/INCPH genes — **DGUOK (PHNC1/INCPH1)**, **KCNN3, FCHSD1, FOPV, TRMT5, HRG**, and syndromic causes (Adams–Oliver, telomere biology disorders, cystic fibrosis, Turner, Williams–Beuren) (review PMID 38900412). GIMAP5's **accompanying immunodeficiency/autoimmunity** is a key distinguishing clue.

**Screening (asymptomatic):** cascade/carrier testing of relatives; prenatal/preimplantation testing in known families (see §13).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **guarded** in severe cases. In the founding cohort, three affected individuals in one kindred were deceased, **two dying from complications of portal hypertension**; one patient died at 17 with recurrent infections (PMID 33956074). No formal 5-/10-year survival statistics exist (too few patients).
- **Morbidity:** recurrent variceal bleeding, refractory/transfusion-dependent cytopenias, infection susceptibility, progressive liver dysfunction (coagulopathy, hyperbilirubinemia), and risk of extramedullary hematopoiesis (models). **Hepatocellular carcinoma (HP:0001402)** is listed as a potential long-term risk.
- **Recovery potential:** the vascular disease does not spontaneously remit; **portosystemic shunting improves varices** but does not halt underlying liver disease (PMID 33956074). Immune cytopenias can respond well to immunomodulation.
- **Prognostic factors:** degree of portal hypertension/hepatic decompensation; severity of immunodeficiency and infection burden; genotype (null/absent protein alleles such as R214* may predict more complete deficiency). **Prognostic biomarker candidate:** long-chain ceramide accumulation (mechanistic; not clinically validated).

---

## 12. Treatment

*No disease-specific approved therapy exists; management is organ-directed and, increasingly, mechanism-informed.*

**A. Portal-hypertension / hepatic care (standard of care):**
- **Endoscopic variceal band ligation** and **nonselective beta-blockers** (e.g., propranolol/carvedilol) for variceal prophylaxis (NCIT: Propranolol C692; Endoscopic Variceal Ligation).
- **Portosystemic shunt surgery / TIPS** — improved varices/collaterals in a reported patient (PMID 33956074) (NCIT: Transjugular Intrahepatic Portosystemic Shunt).
- **Ascites management** (diuretics/sodium restriction); **liver transplantation** for end-stage disease (NCIT: Liver Transplantation C15356) — rational because the defect is intrahepatic-endothelial.

**B. Immune-directed therapy:**
- **Sirolimus (rapamycin; mTOR inhibitor)** achieved **sustained remission of autoimmune cytopenias** (PMID 42358996) (NCIT: Sirolimus C1212).
- Supportive: **IVIG**, targeted **antimicrobial/antiviral prophylaxis**, vaccination as tolerated (NCIT: Intravenous Immunoglobulin Therapy).
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** is considered **definitive for the immune/hematologic disease** (NCIT: Hematopoietic Stem Cell Transplantation C15431), but — because the liver disease is endothelial-intrinsic and lymphocyte-independent — **HSCT is not expected to reverse established portal hypertension**; the risk/benefit must be weighed carefully (PMID 42358996).

**C. Experimental / mechanism-based (preclinical):**
- **GSK3 inhibitors** rescued patient T-cell proliferation in vitro (PMID 29382851).
- **CK2 inhibitors + ceramide-synthase inhibitors** rescued GIMAP5-deficient T cells by preventing ceramide overaccumulation (PMID 38172257) — a candidate for future targeted therapy.
- **Gene/RNA therapy:** none developed; conceptually attractive given recessive LOF and endothelial/lymphoid expression (not yet in trials). No NCT registrations identified.

**Pharmacogenomics:** none disease-specific. **Personalized approach:** genotype/phenotype-guided balancing of liver-directed vs immune-directed (sirolimus) vs HSCT strategies.

---

## 13. Prevention

- **Primary prevention:** not possible for the genetic disease itself; **preconception genetic counseling** in consanguineous/known-carrier families, with **carrier testing**, **prenatal diagnosis**, and **preimplantation genetic testing (PGT-M)** to prevent affected births (autosomal recessive, 25% recurrence).
- **Secondary prevention (early detection):** molecular diagnosis enables **variceal surveillance endoscopy**, monitoring of platelet counts/liver tests, and early immune monitoring; **cascade genetic screening** of at-risk relatives.
- **Tertiary prevention (complication avoidance):** beta-blockers/band ligation to prevent variceal hemorrhage; infection prophylaxis and vaccination; timely immunomodulation for cytopenias; transplant planning.
- **Immunization/public-health/environmental measures:** standard immunizations (with attention to live-vaccine caution in immunodeficiency); no vector/sanitation measures apply (non-infectious etiology).
- **Counseling:** genetic counseling is central given recessive inheritance and consanguinity.

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected/model species:** human *Homo sapiens* (NCBI:txid9606); *Mus musculus* (NCBI:txid10090); *Rattus norvegicus* (NCBI:txid10116). *GIMAP5* orthologs are also studied in **chicken** (*Gallus gallus*, NCBI:txid9031; PMIDs 31579581, 32147998).
- **Orthologous genes:** mouse *Gimap5* (NCBI Gene 14468; MGI), rat *Gimap5* (RGD). Mechanisms (anti-apoptotic GTPase, lymphocyte survival) are **evolutionarily conserved** across rodents and birds.
- **Natural (spontaneous) animal disease:** the **BioBreeding diabetes-prone (BB-DP) rat** carries a spontaneous *Gimap5* frameshift (*lyp*) allele causing **T-cell lymphopenia and autoimmune type 1 diabetes** (PMIDs 17655828, 19007993) — a naturally occurring model of GIMAP5 deficiency, though its hallmark is autoimmune diabetes rather than portal hypertension. No specific companion-animal PHNC2 (no OMIA entry for GIMAP5 portal hypertension identified).
- **Comparative pathology:** rodents recapitulate lymphopenia and liver pathology; the **portal-hypertension/LSEC-capillarization** phenotype is specifically demonstrated in **mouse** (endothelial-intrinsic).
- **Zoonotic potential:** none (genetic, non-transmissible).

---

## 15. Model Organisms

**Mouse (*Mus musculus*; MGI) — primary PHNC2 model:**
- **Germline *Gimap5* knockout / *sph* (sphinx) ENU allele:** impaired peripheral T-cell survival, disrupted NK/NKT development, chronic hepatic hematopoiesis, **hepatocyte apoptosis and liver failure**, median survival ~15 weeks (PMID 18796632).
- **Endothelial-cell-conditional *Gimap5* deletion:** reproduces **LSEC capillarization** — the most faithful model of the human portal-hypertension mechanism (PMID 33956074).
- **Epistasis models:** *Gimap5^sph/sph;Rag1⁻/⁻* mice (no T/B cells) still develop liver disease → **portal hypertension is lymphocyte-independent** (PMID 33956074).
- **Complex/humanized biology:** *Mfsd1*, *Glmp*, and *Gimap5* germline knockouts each cause lymphopenia, liver pathology, and extramedullary hematopoiesis, defining the stabilizing **MFSD1–GLMP–GIMAP5** complex (PMID 38055739).
- **Mechanistic mouse models:** GSK3β-axis studies (PMID 29382851); ceramide/CK2 senescence pathway (PMID 38172257).

**Rat (*Rattus norvegicus*; RGD):** **BB-DP (*lyp/lyp*)** and congenic lines — spontaneous *Gimap5* frameshift; robust model of **T-cell lymphopenia, ER-stress/CHOP apoptosis, mitochondrial Ca²⁺ dysregulation, and autoimmune diabetes** (PMIDs 17655828, 19424493, 19007993, 21502331).

**In vitro / cellular:** patient T cells (proliferation defect rescued by GSK3 inhibitors), Jurkat/HEK overexpression studies, and primary LSEC analyses.

**Phenotype recapitulation & limitations:** rodents faithfully model the **immune arm** (lymphopenia, autoimmunity) and, in mouse endothelial-specific/whole-body models, the **hepatic vascular arm** (capillarization, portal hypertension). **Limitations:** the BB-DP rat's dominant phenotype is autoimmune diabetes (not seen as a core human PHNC2 feature); mouse whole-body nulls have very short lifespans complicating chronic-disease study; hepatocellular carcinoma risk and human-specific variant effects are not fully captured.
**Resources:** MGI (mouse *Gimap5*), RGD (rat *Gimap5*, BB rat), IMPC/IMSR for alleles.

---

## Supported vs. Refuted Hypotheses

**Supported:**
- PHNC2 is caused by **biallelic LOF *GIMAP5*** variants, **autosomal recessive** (PMID 33956074).
- Portal hypertension arises from **GATA4-dependent LSEC capillarization**, an **endothelial-intrinsic, lymphocyte-independent** mechanism (PMID 33956074).
- A unifying **CK2–ceramide senescence** pathway links hepatic and immune disease (PMID 38172257).
- Disease is **multisystem** (portal hypertension + immunodeficiency/autoimmunity) with childhood onset (PMIDs 33956074, 42358996).

**Refuted / not supported:**
- PHNC2 is **not** due to cirrhosis, fibrosis, or portal/splanchnic vein thrombosis (explicitly excluded; PMID 33956074).
- Not caused by *DGUOK* (that is the distinct **PHNC1/INCPH1**, PMID 26874653).
- No environmental/infectious cause is required; heterozygous carriers are unaffected.

## Limitations and Future Directions
- **Very small N** (~20–25 patients) limits penetrance, expressivity, natural-history, prognosis, and QoL precision.
- **Genotype–phenotype** relationships (e.g., missense vs null alleles; the recurrent p.L204P; possible monoallelic vascular predisposition) need larger cohorts.
- **Therapeutic priorities:** validate CK2/ceramide-synthase and GSK3 inhibition clinically; define whether early HSCT alters liver outcomes; assess liver transplantation outcomes; explore endothelial-directed or gene-based therapy.
- **Registry/omics:** a dedicated PSVD-genetics registry and hepatic single-cell/lipidomic profiling in patients would refine mechanism and biomarkers.

---

### Key References (PMID)
- **33956074** Drzewiecki et al., *J Exp Med* 2021 — GIMAP5 maintains liver endothelial cell homeostasis and prevents portal hypertension (**disease-defining**).
- **38172257** Park et al., *Nat Immunol* 2024 — GIMAP5 deficiency reveals a ceramide-driven longevity/senescence pathway.
- **38055739** Zhong et al., *PNAS* 2023 — MFSD1–GLMP–GIMAP5 complex in lymphocyte survival and liver homeostasis.
- **42358996** Moratti et al., *Front Immunol* 2026 — clinical spectrum, sirolimus, HSCT dilemmas (compound-het L204P/R214*).
- **29382851** Patterson et al., *Nat Commun* 2018 — Gimap5–GSK3β; first human LOF patient.
- **18796632** Schulteis et al., *Blood* 2008 — Gimap5-KO mouse liver failure/lymphopenia.
- **38900412** Ciriaci et al., *Hepatology* 2026 — genetic predisposition to PSVD (differential/gene list).
- **26874653** Vilarinho et al., 2016 — *DGUOK* in INCPH1 (distinct PHNC1).


## Artifacts

- [OpenScientist final report](Portal_Hypertension_Noncirrhotic_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Portal_Hypertension_Noncirrhotic_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 30 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:1000488` (2 mentions) - the report calls it "liver sinusoidal endothelial cell"; CL calls it **cholangiocyte**
- `UBERON:0002106` (1 mention) - the report calls it "spleen", "Secondary organ involvement:** **spleen"; UBERON calls it **spleen**
- `GO:0005765` (1 mention) - the report calls it "Subcellular level:** GIMAP5 localizes to the **lysosomal membrane"; GO calls it **lysosomal membrane**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0030397` (2 mentions) - the report calls it "portal hypertension, noncirrhotic, 2"; synonym **NCPH2"; MONDO calls it **portal hypertension, noncirrhotic, 2**
- `HP:0002910` (1 mention) - the report calls it "Elevated transaminases"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated transaminases" among its other names
- `HP:0002040` (1 mention) - the report calls it "Esophageal varices"; HP calls it **Esophageal varix**, and lists "Esophageal varices" among its other names
- `HP:0030948` (1 mention) - the report calls it "Elevated GGT"; HP calls it **Elevated gamma-glutamyltransferase level**, and lists "Elevated serum GGT" among its other names
- `HP:0001888` (1 mention) - the report calls it "Lymphopenia"; HP calls it **Decreased total lymphocyte count**, and lists "Lymphopenia" among its other names
- `CL:0000623` (2 mentions) - the report calls it "NK cell"; CL calls it **natural killer cell**, and lists "NK cell" among its other names
- `UBERON:0002017` (1 mention) - the report calls it "portal venous system/portal vein"; UBERON calls it **portal vein**, and lists "portal venous tree organ part" among its other names
- `HP:0000007` (1 mention) - the report calls it "Autosomal recessive", "Inheritance:** **Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002106` - called "spleen", "Secondary organ involvement:** **spleen"
- `HP:0000007` - called "Autosomal recessive", "Inheritance:** **Autosomal recessive"