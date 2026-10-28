---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T13:34:07.397674'
end_time: '2026-10-19T13:49:30.206922'
duration_seconds: 922.81
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Spastic Tetraplegia and Axial Hypotonia, Progressive
  mondo_id: MONDO:0032828
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
citation_count: 20
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 12
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 13
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032828
    reported_labels:
    - MONDO
    ontology_label: spastic tetraplegia and axial hypotonia, progressive
  labels_variant: 3
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spastic_Tetraplegia_And_Axial_Hypotonia_Progressive-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spastic_Tetraplegia_And_Axial_Hypotonia_Progressive-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spastic Tetraplegia and Axial Hypotonia, Progressive
- **MONDO ID:** MONDO:0032828 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spastic Tetraplegia and Axial Hypotonia, Progressive** covering all of the
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

# Spastic Tetraplegia and Axial Hypotonia, Progressive (STAHP): A Comprehensive Disease Characteristics Report

**Disease:** Spastic Tetraplegia and Axial Hypotonia, Progressive
**MONDO ID:** MONDO:0032828 · **OMIM:** #618598 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** *SOD1* (Cu/Zn superoxide dismutase 1; HGNC:11179; chromosome 21q22.11)

---

## Summary

Spastic Tetraplegia and Axial Hypotonia, Progressive (STAHP) is an ultra-rare, autosomal-recessive, childhood-onset neurodegenerative disorder caused by **complete biallelic loss of function of the antioxidant enzyme Cu/Zn superoxide dismutase (SOD1)**. It was first delineated as a distinct nosological entity in 2019 by Park and colleagues, who identified a homozygous truncating variant, c.335dupG (p.Cys112Trpfs\*11), that abolishes all SOD1 enzyme activity in multiple consanguineous families ([PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/)). The clinical picture comprises progressive loss of acquired motor milestones, spastic tetraplegia with lower-extremity predominance, axial (truncal) hypotonia, mild cerebellar atrophy, and a hyperekplexia-like exaggerated startle. Heterozygous carriers, despite having markedly reduced enzyme activity, are neurologically normal — establishing a recessive mechanism in which roughly 50% of SOD1 activity is sufficient for health.

STAHP is best understood as the **mechanistic mirror-image of SOD1-associated amyotrophic lateral sclerosis (ALS)**. Dominant *SOD1* missense variants cause ~2% of ALS through a toxic gain-of-function (protein misfolding and aggregation), whereas STAHP arises from the *total absence* of the enzyme. This distinction has direct therapeutic-safety implications: the FDA-approved antisense oligonucleotide tofersen lowers SOD1 protein to treat SOD1-ALS, and the existence of a human SOD1-deficiency syndrome cautions that deep, chronic SOD1 suppression is not biologically inert. The pathophysiology converges on chronic oxidative stress — most critically in **mitochondria and motor neurons** — that produces a distal motor axonopathy and neuromuscular-junction (NMJ) failure. This causal chain is strongly supported by *Sod1*-null (knockout) mouse models, in which the phenotype is rescued by restoring SOD1 selectively to neurons or to the mitochondrial intermembrane space.

Because fewer than ~20 patients have been reported worldwide, almost all from consanguineous pedigrees carrying a recurrent founder frameshift, the evidence base is a hybrid of a small number of human clinical reports and an extensive body of *Sod1*-knockout mouse biology. There is no approved disease-modifying therapy; care is supportive. Mechanism-rational but clinically unproven strategies include antioxidants/SOD mimetics and SOD1 gene augmentation — the latter supported by the mouse rescue data. This report synthesizes eight confirmed findings across all 15 template sections, flagging clearly where human data are absent and where conclusions are extrapolated from model systems.

---

## Section 1 — Disease Information

**Overview.** STAHP is a progressive, early-onset neurodegenerative disease of the central and peripheral motor system caused by inherited deficiency of SOD1. The cardinal triad is (i) progressive spastic tetraplegia (upper-motor-neuron signs in all four limbs, lower extremity > upper), (ii) axial hypotonia (truncal low tone), and (iii) progressive loss of previously acquired motor abilities. Additional features include mild cerebellar atrophy and hyperekplexia-like startle responses ([PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032828 |
| OMIM | #618598 (Spastic tetraplegia and axial hypotonia, progressive) |
| Gene (OMIM) | *SOD1* \*147450 |
| HGNC | HGNC:11179 (*SOD1*) |
| Orphanet | SOD1-deficiency syndrome (ultra-rare; dedicated ORPHAcode may not be assigned) |
| ICD-11 | Closest: hereditary spastic paraplegia–adjacent category (no STAHP-specific code) |
| MeSH | No STAHP-specific descriptor; indexed under *Superoxide Dismutase* / *Muscle Spasticity* |

**Synonyms / alternative names:** STAHP; SOD1 deficiency; SOD1-deficiency syndrome; progressive spastic tetraplegia and axial hypotonia.

**Information source:** Disease-level, aggregated from a small number of primary case reports and families (OMIM, PubMed). This is **not** an EHR-derived or population-cohort entity; the characterization rests on individual clinical descriptions supplemented by mechanistic work in *Sod1*-knockout mice.

---

## Section 2 — Etiology

**Primary cause (genetic).** STAHP is a monogenic Mendelian disorder caused by **homozygous (biallelic) loss-of-function variants in *SOD1***. The prototype is the frameshift c.335dupG (p.Cys112Trpfs\*11), which truncates the protein and **abolishes all enzyme activity**. Park et al. state: *"In this study we describe the homozygous truncating variant c.335dupG (p.C112Wfs\*11) in SOD1 that leads to total absence of enzyme activity"* ([PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/)). A second independent homozygous loss-of-function *SOD1* variant has since been reported, confirming the gene–disease relationship ([PMID: 36935613](https://pubmed.ncbi.nlm.nih.gov/36935613/)).

**Genetic risk factors.** The only established genetic cause is biallelic *SOD1* LoF. **Consanguinity is the dominant risk factor** — all reported families are consanguineous, and the recurrent c.335dupG allele behaves as a founder mutation. There are no established common-variant susceptibility loci (STAHP is Mendelian, not polygenic).

**Protective / modifier factors.** Being a heterozygous carrier is effectively "protective" against disease: carriers have reduced enzyme activity but **no overt neurologic phenotype**. Park et al.: *"Heterozygous carriers have a markedly reduced enzyme activity when compared to wild-type controls but show no overt neurologic phenotype"* ([PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/)), indicating ~50% SOD1 activity suffices. In model systems, the mitochondrial-intermembrane-space pool of SOD1 and neuronal (vs. muscle) SOD1 expression are the critical protective compartments (see Sections 6 and 15). No validated human environmental protective factor is known.

**Environmental risk factors / gene–environment interactions.** No environmental trigger is required to manifest STAHP — the disorder is fully penetrant from the genetic lesion. However, because SOD1 is the frontline defense against superoxide, oxidative-stress–increasing exposures are biologically plausible modifiers. In *Sod1*-null mice, superimposed oxidative or metabolic stressors (e.g., diabetes, aging, a second cochlear mutation) accelerate organ-specific injury (renal: [PMID: 17697870](https://pubmed.ncbi.nlm.nih.gov/17697870/); hearing: [PMID: 20470874](https://pubmed.ncbi.nlm.nih.gov/20470874/)). These gene–environment interactions are demonstrated in mice and only *inferred* for human STAHP.

---

## Section 3 — Phenotypes

All phenotypes are **progressive** and of **childhood onset**, with prenatal/neonatal antecedents in a substantial fraction.

| Phenotype | Type | HPO term | Onset | Severity / Course | Frequency |
|---|---|---|---|---|---|
| Progressive loss of motor abilities (regression) | Clinical sign | HP:0002376 (Developmental regression) | Childhood | Severe, progressive | All reported patients |
| Spastic tetraplegia (LL > UL) | Clinical sign | HP:0002510 (Spastic tetraplegia) | Childhood | Severe, progressive | All |
| Axial hypotonia | Clinical sign | HP:0008936 (Axial hypotonia) | Early childhood | Moderate–severe | All |
| Mild cerebellar atrophy | Imaging/physical | HP:0001272 (Cerebellar atrophy) | Childhood | Mild | Index families |
| Hyperekplexia-like exaggerated startle | Clinical sign | HP:0002267 (Exaggerated startle response) | Childhood | Variable | Index families |
| Polyhydramnios (gestational) | Prenatal sign | HP:0001561 (Polyhydramnios) | Prenatal | — | 4/5 (de Souza cohort) |
| Intrauterine growth restriction | Prenatal sign | HP:0001511 (IUGR) | Prenatal | — | 3/5 (de Souza cohort) |

**Characteristics.** De Souza et al. described a Brazilian series of 5 patients: **childhood-onset spastic tetraplegia with axial hypotonia in all 5**, with *"gestational history showing polyhydramnios in 4/5 and intrauterine growth restriction in 3/5 patients"* ([PMID: 34380534](https://pubmed.ncbi.nlm.nih.gov/34380534/)), and progressive loss of acquired motor milestones. The prenatal features indicate that the disease process begins in utero, while overt neurodegeneration becomes clinically apparent in childhood. Park et al. summarize the core phenotype as *"severe and marked by progressive loss of motor abilities, tetraspasticity with predominance in the lower extremities, mild cerebellar atrophy, and hyperekplexia-like symptoms"* ([PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/)).

**Quality of life.** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease. Qualitatively, the combination of progressive tetraspasticity, motor regression, and axial hypotonia implies profound loss of independent ambulation and self-care, high caregiver dependence, and likely feeding/respiratory vulnerability — a severe QoL burden inferred from the phenotype rather than directly measured.

---

## Section 4 — Genetic / Molecular Information

**Causal gene:** *SOD1* (Cu/Zn superoxide dismutase 1), OMIM \*147450, HGNC:11179, chromosome 21q22.11. SOD1 catalyzes dismutation of the superoxide radical (O₂·⁻) to O₂ and H₂O₂.

**Pathogenic variants.**

| Variant (cDNA) | Protein | Type | Zygosity | Consequence | Reference |
|---|---|---|---|---|---|
| c.335dupG | p.Cys112Trpfs\*11 | Frameshift (truncating) | Homozygous | Total loss of enzyme activity | [PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/) |
| Novel homozygous LoF | (loss of function) | LoF | Homozygous | Loss of function | [PMID: 36935613](https://pubmed.ncbi.nlm.nih.gov/36935613/) |

**Classification:** The truncating variants are **pathogenic** by ACMG/AMP criteria (null variant in a gene where LoF is an established mechanism; PVS1 + segregation + functional enzyme-activity evidence).

**Functional consequence:** **Loss of function** — complete abolition of superoxide dismutase activity in the homozygous state. This is the defining molecular feature distinguishing STAHP from the **gain-of-function** missense variants of SOD1-ALS.

**Allele frequency:** The c.335dupG founder allele is essentially private to the reported consanguineous pedigrees and is vanishingly rare/absent at homozygosity in population databases (gnomAD), consistent with a recessive ultra-rare disorder.

**Somatic vs germline:** Germline.

**Modifier genes:** None established in humans. Mouse data implicate redox-pathway genes (e.g., *Gpx4* overexpression modulates the muscle phenotype, [PMID: 37878529](https://pubmed.ncbi.nlm.nih.gov/37878529/); the *Nrf2*/*NFE2L2* pathway is broadly protective, [PMID: 32061629](https://pubmed.ncbi.nlm.nih.gov/32061629/)).

**Epigenetic information / chromosomal abnormalities:** No disease-specific epigenetic signature or large-scale chromosomal rearrangement is described for STAHP.

---

## Section 5 — Environmental Information

STAHP is a **genetically determined, fully penetrant** disorder; no environmental exposure, lifestyle factor, or infectious agent is required for or known to cause it. Because SOD1 is the primary cytosolic/mitochondrial-IMS superoxide scavenger, exposures that raise oxidative load (certain drugs, metabolic stress, aging) are *plausible* disease modifiers, but this is extrapolated from *Sod1*-knockout mouse organ-injury studies (diabetic nephropathy acceleration, [PMID: 17697870](https://pubmed.ncbi.nlm.nih.gov/17697870/); age-related hearing loss, [PMID: 10466888](https://pubmed.ncbi.nlm.nih.gov/10466888/)) and is not established in patients. **Infectious agents: not applicable.**

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *SOD1* loss-of-function mutation** (e.g., c.335dupG) → **leads to** total absence of Cu/Zn superoxide dismutase enzyme activity. *(Demonstrated — enzyme assay, [PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/).)*
2. Absence of dismutation → **results in** accumulation of superoxide radical (O₂·⁻) and chronic oxidative stress, most critically at the **mitochondrial intermembrane space** and in **peripheral nerve**. *(Demonstrated in mouse: oxidized glutathione redox potential in tibial nerve, [PMID: 21963651](https://pubmed.ncbi.nlm.nih.gov/21963651/); mitochondrial-IMS SOD1 sufficiency, [PMID: 21078595](https://pubmed.ncbi.nlm.nih.gov/21078595/).)*
3. Chronic oxidative stress in motor axons → **leads to** a **progressive distal motor axonopathy**, with preferential denervation of fast-twitch muscle, while motor-neuron cell bodies and sensory fibers are relatively preserved. *(Demonstrated in mouse, [PMID: 21963651](https://pubmed.ncbi.nlm.nih.gov/21963651/).)*
4. Distal axon injury → **results in** **neuromuscular-junction (NMJ) destabilization and functional failure** — reduced endplate occupancy, terminal sprouting, axon swelling, and impaired evoked neurotransmitter (synaptic-vesicle) release despite preserved acetylcholine-receptor density. *(Demonstrated in mouse, [PMID: 24971750](https://pubmed.ncbi.nlm.nih.gov/24971750/).)*
5. NMJ failure + central motor-tract involvement → **produces** muscle weakness/atrophy and the clinical upper-motor-neuron picture (spastic tetraplegia) together with axial hypotonia, motor regression, mild cerebellar atrophy, and hyperekplexia-like startle. *(Human phenotype, [PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/), [PMID: 34380534](https://pubmed.ncbi.nlm.nih.gov/34380534/); the step from NMJ/axon biology to the specific human CNS signs is partly inferred.)*

**Branch / protective node:** Restoring SOD1 selectively to **neurons** (synapsin promoter) or to the **mitochondrial intermembrane space** prevents the axonopathy and muscle loss — defining the neuronal, mitochondrial-IMS redox pool as the critical protective compartment. Fischer et al.: *"mitochondrial SOD1 is sufficient to prevent biochemical and morphological defects in the Sod1(-/-) model, and to rescue the motor phenotype of these mice when followed to 12 months of age"* ([PMID: 21078595](https://pubmed.ncbi.nlm.nih.gov/21078595/)); and neuron-specific CuZnSOD *"is sufficient to prevent the loss of muscle mass and function"* ([PMID: 24378874](https://pubmed.ncbi.nlm.nih.gov/24378874/)).

### Detail by category

- **Molecular pathway:** Superoxide → (normally) dismutation by SOD1 → H₂O₂ (GO:0019430 removal of superoxide radicals; GO:0006801 superoxide metabolic process). Loss shifts redox balance; downstream, the Nrf2/antioxidant response (NFE2L2) is a compensatory axis ([PMID: 32061629](https://pubmed.ncbi.nlm.nih.gov/32061629/)).
- **Cellular processes:** Chronic oxidative stress (GO:0006979), mitochondrial dysfunction, impaired synaptic transmission at the NMJ (GO:0007274 neuromuscular synaptic transmission), axon degeneration.
- **Protein dysfunction:** Pure **loss of function** (no enzyme) — in contrast to misfolding/aggregation in SOD1-ALS. CHEBI entities: superoxide (CHEBI:18421), hydrogen peroxide (CHEBI:16240), copper(II) (CHEBI:29036), zinc(II) (CHEBI:29105).
- **Metabolic changes:** Oxidation of the glutathione pool in peripheral nerve ([PMID: 21963651](https://pubmed.ncbi.nlm.nih.gov/21963651/)); lipid-hydroperoxide accumulation in muscle (modifiable by GPx4, [PMID: 37878529](https://pubmed.ncbi.nlm.nih.gov/37878529/)); mitochondrial respiratory deficits in muscle.
- **Tissue damage mechanism:** Oxidative stress → distal axon degeneration and NMJ dismantling.
- **Cell types involved (CL):** Motor neuron / lower motor neuron (CL:0011001, CL:0000100), skeletal muscle fiber (CL:0000188), with fast-twitch (type II) fibers preferentially affected.
- **Immune involvement:** Not a primary driver in STAHP (contrast canine degenerative myelopathy, where glial UPR/neuroinflammation occurs, [PMID: 30273700](https://pubmed.ncbi.nlm.nih.gov/30273700/)).

**GO biological-process suggestions:** GO:0019430 (removal of superoxide radicals), GO:0006801 (superoxide metabolic process), GO:0006979 (response to oxidative stress), GO:0007274 (neuromuscular synaptic transmission), GO:0098754 (detoxification).

---

## Section 7 — Anatomical Structures Affected

- **Primary organ/system:** Nervous system — central (corticospinal tracts → spasticity; cerebellum → mild atrophy) and peripheral motor axons. **Body system:** nervous (UBERON:0001016) and musculoskeletal.
- **Secondary involvement:** Skeletal muscle (atrophy/weakness, secondary to denervation); respiratory and feeding musculature at risk with progression.
- **Tissue/cell level:** Nervous tissue — **motor neurons and their distal axons** (CL:0000100 / CL:0011001); **skeletal muscle fibers** (CL:0000188), with fast-twitch (type II) fibers preferentially denervated.
- **Subcellular level (GO cellular component):** **Mitochondrion** (GO:0005739) and specifically the **mitochondrial intermembrane space** (GO:0005758) — the critical protective SOD1 pool; **cytosol** (GO:0005829, principal SOD1 localization); **neuromuscular junction** (GO:0031594).
- **Localization (UBERON):** spinal cord (UBERON:0002240), corticospinal tract (UBERON:0002716), cerebellum (UBERON:0002037), peripheral/tibial nerve (UBERON:0001323), neuromuscular junction (UBERON:0002515).
- **Lateralization:** Bilateral and symmetric (tetraplegia; axial).

---

## Section 8 — Temporal Development

- **Onset:** Prenatal antecedents (polyhydramnios 4/5, IUGR 3/5) with **childhood clinical onset** of neurologic disease ([PMID: 34380534](https://pubmed.ncbi.nlm.nih.gov/34380534/)). Onset pattern: insidious/chronic.
- **Progression:** **Progressive** course — loss of previously acquired motor milestones (regression), worsening spasticity. No relapsing-remitting or episodic pattern described. Duration: chronic, lifelong.
- **Stages:** Not formally staged; practically, early (axial hypotonia, developmental concerns) → intermediate (emerging spasticity, regression) → advanced (fixed tetraspasticity, severe disability).
- **Remission:** None reported; no spontaneous remission.
- **Critical period:** The in-utero-to-childhood window is when the degenerative process establishes; mouse rescue data suggest that restoring SOD1 *before* axonopathy is established is key (preventive rather than reparative), implying an early therapeutic window ([PMID: 21078595](https://pubmed.ncbi.nlm.nih.gov/21078595/)).

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Autosomal recessive.** Biallelic LoF required; **heterozygous carriers are asymptomatic** despite reduced enzyme activity ([PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/)).
- **Penetrance:** Complete in biallelic-null individuals (all reported homozygotes affected); zero in heterozygotes.
- **Expressivity:** Core triad consistent; prenatal features (polyhydramnios, IUGR) variable (present in a majority but not all patients).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effect / consanguinity:** Prominent — recurrent c.335dupG founder allele; all families consanguineous.
- **Carrier frequency:** Not established; expected very low outside specific consanguineous populations.
- **Epidemiology:** Ultra-rare — **fewer than ~20 patients published worldwide** (principally [PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/), [PMID: 34380534](https://pubmed.ncbi.nlm.nih.gov/34380534/), [PMID: 36935613](https://pubmed.ncbi.nlm.nih.gov/36935613/)). No reliable prevalence/incidence figures (effectively <1/1,000,000).
- **Demographics / geography:** Reported in consanguineous families; a cohort from Brazil ([PMID: 34380534](https://pubmed.ncbi.nlm.nih.gov/34380534/)). No strong sex bias reported; sex ratio ~1:1 expected for an autosomal-recessive trait.

---

## Section 10 — Diagnostics

- **Genetic testing (definitive):** Diagnosis rests on identifying **biallelic loss-of-function *SOD1* variants**. Recommended approach: **whole-exome or whole-genome sequencing**, or a hereditary-spastic-paraplegia / neurodegeneration gene panel that includes *SOD1*; targeted single-gene/founder-variant testing (c.335dupG) is appropriate in consanguineous families or known pedigrees.
- **Biochemical biomarker (disease-specific):** **Red-cell / tissue SOD1 enzyme-activity assay** — **absent activity in affected homozygotes**, intermediate (~50%) in carriers ([PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/)). This is a powerful, mechanism-specific confirmatory test that distinguishes STAHP from SOD1-ALS (where enzyme activity is retained).
- **Imaging:** Brain MRI may show **mild cerebellar atrophy** (HP:0001272).
- **Electrophysiology:** EMG / nerve-conduction studies may reflect the distal motor axonopathy / NMJ involvement inferred from mouse models (by extrapolation).
- **Clinical criteria:** No formal consensus criteria; diagnosis is the characteristic clinical triad + biallelic *SOD1* LoF + absent enzyme activity.
- **Differential diagnosis:** Hereditary spastic paraplegias; cerebral palsy (non-progressive — the key distinguishing feature is STAHP's regression); other childhood neurodegenerative / leukodystrophy syndromes. Importantly, **SOD1-ALS is NOT a childhood differential** and is mechanistically opposite.
- **Screening:** Cascade carrier testing within affected families; no newborn or population screening exists (ultra-rare).

---

## Section 11 — Outcome / Prognosis

- **Course:** Progressive, chronic, disabling; motor regression and fixed tetraspasticity lead to loss of ambulation and high dependency.
- **Survival/mortality:** No formal survival statistics are published given the tiny cohort; prognosis is guarded, driven by progressive neurodegeneration and attendant complications (respiratory, feeding).
- **Morbidity/disability:** Severe long-term functional impairment is expected (ICF: profound mobility and self-care limitation).
- **Complications:** Inferred from severe spastic tetraplegia — contractures, respiratory insufficiency, aspiration / feeding difficulty, secondary musculoskeletal deformity.
- **Prognostic factors:** Complete enzyme absence predicts the full phenotype; no validated molecular prognostic biomarkers exist. Any residual SOD1 activity would be expected to attenuate severity (hypothesis based on carrier data and mouse dosage effects).
- **Recovery:** No spontaneous recovery; no disease-modifying therapy currently alters the trajectory.

---

## Section 12 — Treatment

**There is no approved disease-specific therapy. Management is supportive** ([PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/), [PMID: 34380534](https://pubmed.ncbi.nlm.nih.gov/34380534/)).

**Supportive / rehabilitative (standard of care):**
- Physical, occupational, and speech therapy (NCIT: Physical Therapy; Occupational Therapy).
- Spasticity management — oral antispastics (baclofen, tizanidine), botulinum toxin, intrathecal baclofen (NCIT: Baclofen; Botulinum Toxin).
- Nutritional and respiratory support; orthopedic management of contractures.

**Mechanism-rational but unproven (experimental) strategies:**
- **Antioxidants / SOD mimetics** (e.g., EUK-8, tempol) — protective in *Sod1*-null mouse organ-injury models ([PMID: 14988070](https://pubmed.ncbi.nlm.nih.gov/14988070/), [PMID: 17697870](https://pubmed.ncbi.nlm.nih.gov/17697870/)); not tested in STAHP patients.
- **Nrf2 activators** (e.g., sulforaphane) — upregulate endogenous antioxidant defenses and are neuroprotective in oxidative-stress models ([PMID: 32061629](https://pubmed.ncbi.nlm.nih.gov/32061629/)); conceptual only for STAHP.
- **SOD1 gene augmentation / enzyme replacement** — the most mechanistically direct approach for a loss-of-function disorder. Proof-of-concept from mouse rescue: restoring SOD1 to **neurons** ([PMID: 24378874](https://pubmed.ncbi.nlm.nih.gov/24378874/)) or to the **mitochondrial intermembrane space** ([PMID: 21078595](https://pubmed.ncbi.nlm.nih.gov/21078595/)) prevents the motor phenotype. Neurotrophic gene therapy (AAV1.NT-3) improved muscle/function in *Sod1*-KO mice ([PMID: 37553101](https://pubmed.ncbi.nlm.nih.gov/37553101/)) — supportive, not curative.

**Critical caveat — do NOT use SOD1-lowering therapy:** Tofersen (an intrathecal antisense oligonucleotide that *reduces* SOD1 synthesis) is the approved therapy for **SOD1-ALS**. Miller et al. note tofersen *"is the first and only approved therapy for the treatment of ALS in adults who have a variant in the SOD1 gene"* ([PMID: 41661214](https://pubmed.ncbi.nlm.nih.gov/41661214/)); robust human SOD1 reduction is confirmed in autopsy tissue ([PMID: 42406382](https://pubmed.ncbi.nlm.nih.gov/42406382/)). STAHP, being a SOD1-*deficiency* disease, requires the **opposite** intervention (enzyme restoration). Park et al. explicitly caution that the deficiency phenotype *"should be considered before application of previously proposed SOD1 silencing as a treatment option for amyotrophic lateral sclerosis"* ([PMID: 31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/)).

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable (not acquired). For at-risk couples: **genetic counseling, carrier testing, and reproductive options** (prenatal diagnosis, preimplantation genetic testing) — especially relevant in consanguineous families carrying the founder allele (NCIT: Genetic Counseling).
- **Secondary prevention:** Cascade testing of relatives; early identification could, in principle, open an early therapeutic window should enzyme-restoration therapy become available (mouse data favor early/preventive intervention, [PMID: 21078595](https://pubmed.ncbi.nlm.nih.gov/21078595/)).
- **Tertiary prevention:** Proactive management to prevent complications of spasticity (contracture prevention, respiratory and nutritional surveillance).
- **Immunization / public health / environmental:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** Human disease (NCBI Taxon:9606). The closest *natural* SOD1-related disease in another species is **canine degenerative myelopathy (DM)** in dogs (NCBI Taxon:9615).
- **Orthologous gene:** Canine *SOD1* (NCBI Gene ID 403559).
- **Key comparative insight — DM is NOT a STAHP model:** Canine DM is caused by **homozygous *SOD1* missense variants (E40K; also T18S)** across ≥5 breeds (Pembroke Welsh corgi, Boxer, Rhodesian ridgeback, German Shepherd, Chesapeake Bay retriever) and features SOD1-immunoreactive cytoplasmic inclusions resembling human SOD1-ALS. Awano et al. report *"The resequencing of SOD1 in normal and affected dogs revealed a G to A transition, resulting in an E40K missense mutation"* ([PMID: 19188595](https://pubmed.ncbi.nlm.nih.gov/19188595/)). Biochemically, the canine mutants *"form enzymatically active dimers, arguing against a loss of function in affected homozygous animals"* ([PMID: 23707216](https://pubmed.ncbi.nlm.nih.gov/23707216/)), with unfolded-protein-response / ER-stress activation in spinal glia ([PMID: 30273700](https://pubmed.ncbi.nlm.nih.gov/30273700/)). Thus DM is a **gain-of-function** (ALS-like) disease, mechanistically the opposite of STAHP.
- **Zoonotic potential:** None (genetic disorder).

---

## Section 15 — Model Organisms

The *Sod1*-null (knockout) **mouse** is the principal and highly informative model of the STAHP loss-of-function mechanism.

| Model | Type | Key finding | Phenotype recapitulation | Reference |
|---|---|---|---|---|
| *Sod1⁻/⁻* whole-body KO | Mouse (knockout) | Peripheral-nerve oxidative stress; progressive distal motor axonopathy; fast-twitch denervation; cell bodies/sensory preserved | Recapitulates motor-axon / oxidative-stress core | [PMID: 21963651](https://pubmed.ncbi.nlm.nih.gov/21963651/) |
| Mitochondrial-IMS-targeted SOD1 | Mouse (transgenic rescue) | mito-IMS SOD1 prevents defects; rescues motor phenotype to 12 months | Defines protective subcellular pool | [PMID: 21078595](https://pubmed.ncbi.nlm.nih.gov/21078595/) |
| Neuron-specific CuZnSOD (synapsin) | Mouse (transgenic rescue) | Neuronal SOD1 prevents loss of muscle mass/function | Identifies critical protective cell type | [PMID: 24378874](https://pubmed.ncbi.nlm.nih.gov/24378874/) |
| *Sod1⁻/⁻* NMJ studies | Mouse | Impaired evoked neurotransmitter release, NMJ destabilization, reduced strength | Models NMJ failure | [PMID: 24971750](https://pubmed.ncbi.nlm.nih.gov/24971750/) |
| Neuronal-CuZnSOD deletion | Mouse (conditional) | Muscle mitochondrial / Ca²⁺-handling dysfunction precedes sarcopenia, independent of denervation | Dissects upstream mechanisms | [PMID: 34639076](https://pubmed.ncbi.nlm.nih.gov/34639076/) |
| AAV1.NT-3 in *Sod1*KO | Mouse (gene-therapy test) | Improved muscle fiber size, function, remyelination via mTOR | Therapeutic proof-of-concept | [PMID: 37553101](https://pubmed.ncbi.nlm.nih.gov/37553101/) |
| GPx4 overexpression in *Sod1*KO | Mouse | Lipid-hydroperoxide reduction modulates muscle pathology | Modifier-pathway dissection | [PMID: 37878529](https://pubmed.ncbi.nlm.nih.gov/37878529/) |

**Mouse model — findings in words.** The knockout develops *"oxidation of the glutathione pool"* in tibial nerve but not muscle, *"suggesting that axonal degeneration is a consequence"* of nerve oxidative stress ([PMID: 21963651](https://pubmed.ncbi.nlm.nih.gov/21963651/)). At the synapse, *"motor axons innervating the extensor digitorum longus (EDL) and gastrocnemius muscles release fewer synaptic vesicles upon nerve stimulation"* ([PMID: 24971750](https://pubmed.ncbi.nlm.nih.gov/24971750/)). Compartment-specific rescue localizes the protection to neurons and mitochondria ([PMID: 24378874](https://pubmed.ncbi.nlm.nih.gov/24378874/), [PMID: 21078595](https://pubmed.ncbi.nlm.nih.gov/21078595/)).

**Limitations of the mouse model:** The *Sod1*-KO mouse was developed chiefly as an **accelerated-sarcopenia / peripheral-axonopathy** model and reproduces the oxidative-stress-driven distal motor axonopathy and NMJ failure. It does **not** fully capture the human CNS features — spastic tetraplegia (an upper-motor-neuron sign), axial hypotonia, cerebellar atrophy, and hyperekplexia-like startle. The human-to-mouse mapping of the *central* motor phenotype therefore remains partly inferred. No STAHP-specific iPSC, organoid, or non-murine genetic model has yet been reported.

---

## Mechanistic Model / Interpretation

```
  Biallelic SOD1 loss-of-function (c.335dupG, p.Cys112Trpfs*11)
                        │  [demonstrated: zero enzyme activity]
                        ▼
      No superoxide dismutation  →  superoxide (O2·−) accumulation
                        │  [chronic oxidative stress]
         ┌──────────────┴───────────────┐
         ▼                              ▼
  Mitochondrial-IMS              Peripheral nerve
  redox imbalance                glutathione oxidation
         │                              │
         └──────────────┬───────────────┘
                        ▼
        Progressive DISTAL MOTOR AXONOPATHY
        (fast-twitch denervation; cell bodies spared)
                        ▼
        NEUROMUSCULAR-JUNCTION destabilization & failure
        (↓ evoked neurotransmitter release; AChR density preserved)
                        ▼
   CLINICAL: spastic tetraplegia (LL>UL) + axial hypotonia +
   motor regression + mild cerebellar atrophy + hyperekplexia-like startle

  PROTECTIVE NODES (rescue in mouse):  neuronal SOD1  &  mitochondrial-IMS SOD1
```

**SOD1 as a two-sided coin.** STAHP sits at one pole of SOD1 biology; SOD1-ALS at the other:

| Feature | STAHP (this disease) | SOD1-ALS |
|---|---|---|
| Variant type | Biallelic truncating/LoF | Heterozygous missense |
| Inheritance | Autosomal recessive | Autosomal dominant |
| Enzyme activity | **Absent** | Retained (often normal) |
| Mechanism | **Loss of function** (no antioxidant defense) | **Toxic gain of function** (misfolding/aggregation) |
| Onset | Childhood (prenatal antecedents) | Adult |
| Carrier state | Asymptomatic | — |
| Rational therapy | **Increase/restore SOD1** | **Lower SOD1** (tofersen) |

This symmetry is the central scientific message of the investigation: it reframes SOD1 not merely as an "ALS gene" but as a dosage-sensitive antioxidant whose complete absence is itself a distinct, severe neurodevelopmental/neurodegenerative disease — and it draws a biological safety boundary around aggressive SOD1-lowering.

---

## Evidence Base

| PMID | Role in this report | Source type |
|---|---|---|
| [31332433](https://pubmed.ncbi.nlm.nih.gov/31332433/) | **Defining paper** — identifies c.335dupG, total enzyme loss, clinical triad, recessive inheritance, ALS-therapy caution | Human clinical |
| [34380534](https://pubmed.ncbi.nlm.nih.gov/34380534/) | 5-patient cohort — prenatal (polyhydramnios 4/5, IUGR 3/5) & childhood onset | Human clinical |
| [36935613](https://pubmed.ncbi.nlm.nih.gov/36935613/) | Second independent homozygous LoF *SOD1* family — confirms gene–disease relationship | Human clinical |
| [21963651](https://pubmed.ncbi.nlm.nih.gov/21963651/) | *Sod1*-KO: nerve oxidative stress → distal motor axonopathy | Mouse model |
| [21078595](https://pubmed.ncbi.nlm.nih.gov/21078595/) | Mitochondrial-IMS SOD1 rescues phenotype → pinpoints initiating compartment | Mouse model |
| [24971750](https://pubmed.ncbi.nlm.nih.gov/24971750/) | NMJ functional failure (↓ neurotransmitter release) | Mouse model |
| [24378874](https://pubmed.ncbi.nlm.nih.gov/24378874/) | Neuronal SOD1 sufficient to protect muscle/NMJ | Mouse model |
| [41661214](https://pubmed.ncbi.nlm.nih.gov/41661214/) | Tofersen (SOD1-lowering) approved for SOD1-ALS — grounds safety boundary | Human clinical trial |
| [42406382](https://pubmed.ncbi.nlm.nih.gov/42406382/) | Tofersen CNS distribution & robust SOD1 reduction in humans | Human autopsy |
| [19188595](https://pubmed.ncbi.nlm.nih.gov/19188595/) | Canine DM caused by *SOD1* E40K missense (gain-of-function) | Veterinary/comparative |
| [23707216](https://pubmed.ncbi.nlm.nih.gov/23707216/) | Canine mutants are active dimers — "arguing against a loss of function" | In vitro/comparative |
| [30273700](https://pubmed.ncbi.nlm.nih.gov/30273700/) | UPR/ER-stress in canine DM glia (gain-of-function pathology) | Veterinary |

The evidence is strongest for (a) the human genetic/biochemical definition of the disease and (b) the mouse-derived oxidative-stress → axonopathy → NMJ-failure mechanism. The weakest link is the direct demonstration that the *human central* phenotype (spasticity, cerebellar atrophy, startle) arises through the same chain validated in mice.

---

## Limitations and Knowledge Gaps

1. **Tiny human sample size (<~20 patients):** No robust epidemiology, natural-history, survival, or quantitative penetrance/expressivity data; frequencies of individual phenotypes rest on small series.
2. **Model–human phenotype gap:** The *Sod1*-KO mouse reproduces peripheral motor-axon/NMJ pathology but not the human **upper-motor-neuron spasticity, cerebellar atrophy, or hyperekplexia-like startle**; the central-nervous-system mechanism of STAHP is therefore inferred.
3. **No STAHP-specific omics:** No patient transcriptomics, proteomics, metabolomics, single-cell, or spatial data are available; molecular-profiling claims are extrapolated.
4. **No disease-specific biomarker validation beyond enzyme activity:** Prognostic biomarkers are unknown.
5. **No therapeutic trials:** Antioxidant, Nrf2-activator, and SOD1-augmentation strategies are rationally motivated but entirely untested in STAHP patients.
6. **Ontology/identifier gaps:** No dedicated ICD-11/MeSH code; Orphanet characterization is minimal.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international STAHP patient registry** to aggregate genotype, enzyme activity, natural history, imaging, and survival across the few known families (addresses Gap 1).
2. **Generate patient-derived iPSC motor neurons / NMJ organoids** carrying c.335dupG to test whether the human central and peripheral phenotypes recapitulate the mouse oxidative-stress → axonopathy chain, and to screen antioxidants / SOD mimetics / Nrf2 activators (addresses Gaps 2–3).
3. **Pursue SOD1 gene-augmentation / enzyme-replacement proof-of-concept** building on the mouse rescue data (neuronal and mitochondrial-IMS targeting), including biodistribution and an early-intervention window study (addresses Gaps 2, 5; leverages [PMID: 24378874](https://pubmed.ncbi.nlm.nih.gov/24378874/), [PMID: 21078595](https://pubmed.ncbi.nlm.nih.gov/21078595/)).
4. **Deep-phenotype patients with CNS-focused MRI and electrophysiology** to test whether a demonstrable distal motor axonopathy / NMJ signature exists in humans, directly bridging the model–human gap.
5. **Perform patient CSF/plasma redox and neurofilament profiling** to search for a tractable pharmacodynamic/prognostic biomarker (mirroring neurofilament utility in SOD1-ALS).
6. **Formal nosology/ontology update:** advocate for dedicated ICD-11 and Orphanet entries and ensure carrier/cascade-testing guidance for consanguineous populations harboring the founder allele.

---

### Evidence-source legend
**Human clinical** = patient reports/cohorts; **Mouse model** = *Sod1*-knockout/transgenic studies; **Veterinary/comparative** = canine degenerative myelopathy; **In vitro** = biochemical/cell studies. Wherever a mechanistic step is supported only by model data, this report labels it *inferred* for human STAHP.


## Artifacts

- [OpenScientist final report](Spastic_Tetraplegia_And_Axial_Hypotonia_Progressive-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spastic_Tetraplegia_And_Axial_Hypotonia_Progressive-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 17 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032828` (2 mentions) - the report calls it "MONDO"; MONDO calls it **spastic tetraplegia and axial hypotonia, progressive**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001272` (2 mentions) - the report calls it "Cerebellar atrophy", "mild cerebellar atrophy", "Imaging:** Brain MRI may show **mild cerebellar atrophy"; HP calls it **Cerebellar atrophy**
- `GO:0006979` (2 mentions) - the report calls it "Cellular processes:** Chronic oxidative stress", "response to oxidative stress"; GO calls it **response to oxidative stress**
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle fibers"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001272` - called "Cerebellar atrophy", "mild cerebellar atrophy", "Imaging:** Brain MRI may show **mild cerebellar atrophy"
- `GO:0006979` - called "Cellular processes:** Chronic oxidative stress", "response to oxidative stress"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.
