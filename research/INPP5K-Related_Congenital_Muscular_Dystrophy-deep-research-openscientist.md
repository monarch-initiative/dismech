---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T12:42:49.490616'
end_time: '2026-10-14T13:21:03.225427'
duration_seconds: 2293.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: INPP5K-Related Congenital Muscular Dystrophy
  mondo_id: MONDO:0024607
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
citation_count: 15
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0001251
    reported_labels:
    - Ataxia (subset, MSS-overlap)
    ontology_label: Ataxia
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: INPP5K-Related_Congenital_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: INPP5K-Related_Congenital_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** INPP5K-Related Congenital Muscular Dystrophy
- **MONDO ID:** MONDO:0024607 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **INPP5K-Related Congenital Muscular Dystrophy** covering all of the
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

# INPP5K-Related Congenital Muscular Dystrophy: A Comprehensive Disease Characteristics Report

**Disease:** INPP5K-Related Congenital Muscular Dystrophy
**MONDO ID:** MONDO:0024607 · **OMIM phenotype:** #616827 (MDCCAID/MDCCAIS) · **Gene:** INPP5K (*607875*; HGNC:21940; NCBI Gene 51763; UniProt Q9BT40)
**Category:** Mendelian, autosomal recessive

---

## Summary

INPP5K-Related Congenital Muscular Dystrophy (also termed **Muscular Dystrophy, Congenital, with Cataracts and Intellectual Disability**, OMIM #616827) is an ultra-rare autosomal recessive disorder caused by **biallelic loss-of-function or hypomorphic variants in *INPP5K***, the gene encoding inositol polyphosphate-5-phosphatase K — also known as **SKIP** (Skeletal muscle and Kidney enriched Inositol Phosphatase). The disorder was first defined in 2017 by two independent landmark papers in the *American Journal of Human Genetics* ([PMID: 28190459](https://pubmed.ncbi.nlm.nih.gov/28190459/); [PMID: 28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/)). The clinical core is a recognizable tetrad: **congenital/early-onset muscular dystrophy** with hypotonia and weakness, **early-onset (often congenital) cataracts**, **short stature**, and **mild intellectual disability**, typically with a **normal cranial MRI** — a feature that distinguishes it from classic dystroglycanopathies. The phenotype straddles two overlapping disease spectra: **dystroglycanopathy** (through α-dystroglycan hypoglycosylation) and **Marinesco-Sjögren syndrome** (sharing infantile cataracts, myopathy, and in a subset ataxia).

Mechanistically, INPP5K/SKIP is a **phosphoinositide 5-phosphatase** that hydrolyzes PtdIns(4,5)P₂ and PtdIns(3,4,5)P₃, is enriched at the endoplasmic reticulum (and present at the plasma membrane, cytosol and nucleus), and normally **dampens insulin-driven PI3K-AKT-GSK3β signaling** while promoting myoblast differentiation. Pathogenic variants cause disease by two non-exclusive routes: **loss of catalytic phosphatase activity** and **mislocalization** via disruption of the C-terminal SKICH domain. Downstream consequences demonstrated across patient cells and animal models include α-dystroglycan hypoglycosylation, BiP/HSPA5-associated ER stress, and a striking convergence with Marinesco-Sjögren syndrome on **dysregulation of d-3-phosphoglycerate dehydrogenase (PHGDH) and reduced L-serine biosynthesis**. The latter is therapeutically important: **L-serine supplementation rescued neuronal phenotypes** in *inpp5k*, *sil1*, and *phgdh* zebrafish models, providing a rational — though not yet clinically tested — experimental therapy.

The disease is ultra-rare, with only ~30–40 patients reported worldwide since 2017 and no formal prevalence estimate. Computational population genetics generated in this investigation reinforce the biology: gnomAD constraint metrics (pLI ≈ 0, LOEUF ≈ 0.87) confirm *INPP5K* is **loss-of-function tolerant in the heterozygous state**, consistent with a recessive mechanism; GTEx shows *INPP5K* is **ubiquitously expressed** (≈10–62 TPM across 54 tissues), indicating the tissue specificity of disease reflects **differential cellular vulnerability rather than restricted expression**; and a gnomAD-derived estimate places the predicted biallelic pLoF birth prevalence at a lower bound of **~1 per million** (carrier frequency ~1 in 500). There is no approved disease-modifying therapy; management is supportive (cataract surgery, physiotherapy, developmental and visual support).

---

## Key Findings

### Finding 1 — Biallelic *INPP5K* mutations are causal (autosomal recessive)

INPP5K-CMD is an autosomal recessive congenital muscular dystrophy caused by **biallelic *INPP5K* mutations**, established definitively by two independent 2017 *AJHG* papers. Osborn et al. ([PMID: 28190459](https://pubmed.ncbi.nlm.nih.gov/28190459/)) reported 5 individuals from 4 families with homozygous missense and compound heterozygous mutations identified by whole-exome sequencing. Wiessner et al. ([PMID: 28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/)) independently identified bi-allelic mutations in additional families. *INPP5K* encodes inositol polyphosphate-5-phosphatase K (SKIP), a phosphoinositide 5-phosphatase that hydrolyzes PtdIns(4,5)P₂ and PtdIns(3,4,5)P₃.

> *"Whole-exome sequencing revealed homozygous missense and compound heterozygous mutations in INPP5K in the affected members of each family. INPP5K encodes the inositol polyphosphate-5-phosphatase K, also known as SKIP (skeletal muscle and kidney enriched inositol phosphatase), which is highly expressed in the brain and muscle."* — Osborn et al. [PMID: 28190459](https://pubmed.ncbi.nlm.nih.gov/28190459/)

> *"we identified bi-allelic mutations in INPP5K, encoding inositol polyphosphate-5-phosphatase K. Mutations impaired phosphatase activity toward the phosphoinositide phosphatidylinositol (4,5)-bisphosphate or altered the subcellular localization of INPP5K."* — Wiessner et al. [PMID: 28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/)

**Key identifiers:** OMIM phenotype #616827 (MDCCAID/MDCCAIS); gene *INPP5K* OMIM *607875; MONDO:0024607; Ensembl ENSG00000132376; locus 17p13.3 (GRCh38 chr17:1,494,577–1,516,742). **HGNC:** INPP5K (HGNC:21940). **UniProt:** Q9BT40 (INP5K_HUMAN). Evidence source: **[human clinical]** (WES cohorts) plus functional validation.

### Finding 2 — Clinical tetrad with marked variable expressivity

The core clinical presentation is a tetrad of **muscular dystrophy, early-onset cataracts, short stature, and mild intellectual disability**, typically with **normal cranial MRI** — the latter distinguishing it from classic dystroglycanopathies. Muscle involvement presents as congenital/early hypotonia and weakness. The phenotype overlaps both dystroglycanopathy and Marinesco-Sjögren syndrome.

> *"In individuals exhibiting congenital muscular dystrophy, early-onset cataracts, and mild intellectual disability but normal cranial magnetic resonance imaging, we identified bi-allelic mutations in INPP5K"* — Wiessner et al. [PMID: 28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/)

Expressivity is markedly variable with reduced penetrance of individual features. A consanguineous Pakistani family (LUCC15) presented with congenital cataract and mild–moderate intellectual disability but **no overt muscular dystrophy or cerebellar atrophy** on MRI, with only an irritable myopathy on EMG ([PMID: 28940338](https://pubmed.ncbi.nlm.nih.gov/28940338/)):

> *"Comparison of clinical phenotype of all the known affected individuals, including LUCC15 family, homozygous for INPP5K alleles revealed reduced penetrance of muscular dystrophy and intellectual disability."* — [PMID: 28940338](https://pubmed.ncbi.nlm.nih.gov/28940338/)

At the milder end, a Chinese patient ([PMID: 42467360](https://pubmed.ncbi.nlm.nih.gov/42467360/)) had adolescent-onset limb-girdle weakness and bilateral cataracts from age 5, **lacking intellectual disability**, and showed a **characteristic selective muscle MRI pattern**:

> *"Muscle magnetic resonance imaging (MRI) revealed a characteristic pattern of selective fatty infiltration, with severe involvement of gluteal and thigh muscles and striking sparing of the rectus femoris, sartorius, and gracilis."* — [PMID: 42467360](https://pubmed.ncbi.nlm.nih.gov/42467360/)

**Suggested HPO terms:**

| Phenotype | HPO term | Onset | Frequency (qualitative) |
|---|---|---|---|
| Congenital muscular dystrophy / weakness | HP:0003560 (Muscular dystrophy), HP:0003701 (Proximal muscle weakness) | Congenital–childhood | Frequent (variable) |
| Neonatal hypotonia | HP:0001319 | Neonatal | Frequent |
| Cataract (early-onset/congenital) | HP:0000518 (Cataract), HP:0000519 (Congenital cataract) | Congenital–childhood | Very frequent |
| Short stature | HP:0004322 | Childhood | Frequent |
| Intellectual disability, mild | HP:0001256 | Childhood | Variable (reduced penetrance) |
| Elevated serum creatine kinase | HP:0003236 | — | Frequent |
| Ataxia (subset, MSS-overlap) | HP:0001251 | Variable | Subset |

### Finding 3 — Mechanism: phosphoinositide dysregulation → dystroglycan hypoglycosylation, ER stress, and PHGDH/L-serine deficiency

Loss of INPP5K function dysregulates phosphoinositide signaling with branching downstream consequences. INPP5K hydrolyzes PtdIns(4,5)P₂ and PtdIns(3,4,5)P₃, is enriched at the ER (also plasma membrane, cytosol, nucleus), and its C-terminal SKICH domain mediates protein interactions and localization; it regulates insulin signaling, the ER stress response, myoblast differentiation, cytoskeleton/actin organization, cell adhesion and migration ([PMID: 33060052](https://pubmed.ncbi.nlm.nih.gov/33060052/)).

> *"Its protein structure is comprised of a N-terminal catalytic domain which hydrolyses both PtdIns(4,5)P2 and PtdIns(3,4,5)P3, followed by a SKICH domain at the C-terminus which is responsible for protein-protein interactions and subcellular localization of INPP5K."* — [PMID: 33060052](https://pubmed.ncbi.nlm.nih.gov/33060052/)

The mechanism branches into: **(1)** dystroglycanopathy — muscular dystrophy is characterized by **hypoglycosylation of dystroglycan** ([PMID: 38559586](https://pubmed.ncbi.nlm.nih.gov/38559586/); Osborn et al. reported reduced dystroglycan glycosylation); **(2)** ER stress — INPP5K interacts with the ER chaperone HSPA5/BiP, implicating protein processing/ER proteostasis ([PMID: 28190459](https://pubmed.ncbi.nlm.nih.gov/28190459/)); and **(3)** metabolic convergence — unbiased proteomics showed INPP5K and SIL1 (Marinesco-Sjögren) pathologies converge on **dysregulation of d-3-PHGDH**, reducing L-serine production, with L-serine administration rescuing neuronal phenotypes in zebrafish models ([PMID: 33792664](https://pubmed.ncbi.nlm.nih.gov/33792664/)).

> *"we present six new INPP5K patients and expand the current mutational and phenotypical spectrum of the disease showing the clinical overlap between Marinesco-Sjögren syndrome and the INPP5K phenotype. We applied unbiased proteomic profiling on cells derived from Marinesco-Sjögren syndrome and INPP5K patients and identified alterations in d-3-PHGDH as a common molecular feature."* — Hathazi et al. [PMID: 33792664](https://pubmed.ncbi.nlm.nih.gov/33792664/)

> *"muscular dystrophy is characterized by the hypoglycosylation of dystroglycan"* — [PMID: 38559586](https://pubmed.ncbi.nlm.nih.gov/38559586/)

INPP5K knockdown in N2A neuroblastoma cells impaired neuronal-like differentiation and interfered with protein glycosylation ([PMID: 38559586](https://pubmed.ncbi.nlm.nih.gov/38559586/)). Evidence source: **[human clinical / in vitro / model organism]**.

### Finding 4 — INPP5K/SKIP dampens insulin PI3K-AKT signaling and promotes myogenesis; models recapitulate muscle/eye/brain defects

SKIP is a 5-phosphatase that hydrolyzes PtdIns(3,4,5)P₃ → PtdIns(3,4)P₂ and PtdIns(4,5)P₂ → PtdIns(4)P, **negatively regulating insulin-induced PI3K-Akt-GSK3β-glycogen synthase signaling** in skeletal muscle ([PMID: 22403078](https://pubmed.ncbi.nlm.nih.gov/22403078/); [PMID: 19272022](https://pubmed.ncbi.nlm.nih.gov/19272022/)). In C2C12 myoblasts, SKIP knockdown increased insulin-induced Akt/GSK-3β phosphorylation and glycogen synthesis, while overexpression decreased it ([PMID: 19250614](https://pubmed.ncbi.nlm.nih.gov/19250614/)). SKIP is transcriptionally upregulated during muscle differentiation and regulated by MyoD ([PMID: 20336382](https://pubmed.ncbi.nlm.nih.gov/20336382/)).

> *"Insulin-induced phosphorylation of Akt (protein kinase B) and GSK-3beta (Glycogen synthase kinase), subsequent dephosphorylation of glycogen synthase and glycogen synthesis were increased by inhibiting the expression of SKIP, whereas the insulin-induced glycogen synthesis was decreased by overexpression of WT-SKIP."* — [PMID: 19250614](https://pubmed.ncbi.nlm.nih.gov/19250614/)

> *"Porcine SKIP was expressed abundantly in skeletal muscle tissue and was transcriptionally upregulated during skeletal muscle differentiation. Analysis of the porcine SKIP promoter sequence demonstrated that MyoD was involved in regulating SKIP mRNA expression in myotubes"* — [PMID: 20336382](https://pubmed.ncbi.nlm.nih.gov/20336382/)

**Model organisms** recapitulate the human phenotype. Morpholino *inpp5k* knockdown in zebrafish produces shortened body axis, microphthalmia with disorganized lens, microcephaly, reduced touch-evoked motility, and highly disorganized myofibers:

> *"morpholino-mediated inpp5k loss of function in the zebrafish results in shortened body axis, microphthalmia with disorganized lens, microcephaly, reduced touch-evoked motility, and highly disorganized myofibers"* — Osborn et al. [PMID: 28190459](https://pubmed.ncbi.nlm.nih.gov/28190459/)

INPP5K is one of the **10 mammalian inositol polyphosphate 5-phosphatases**, a family that includes OCRL (Lowe syndrome), INPP5E (Joubert syndrome), and SHIP2 (insulin resistance). Evidence source: **[in vitro / model organism / review]**.

### Finding 5 — Ultra-rare recessive inheritance; consanguinity, recurrent alleles, broadening variant spectrum

Inheritance is autosomal recessive (biallelic): homozygous in consanguineous families or compound heterozygous ([PMID: 28190459](https://pubmed.ncbi.nlm.nih.gov/28190459/); [PMID: 28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/)). Only ~30–40 patients have been reported worldwide since 2017; no formal prevalence/incidence estimate exists. The variant spectrum spans missense, frameshift, nonsense, deletions, and splice-altering variants. A Chinese patient carried a **synonymous c.261G>A p.(Lys87=) that causes exon 3 skipping** → frameshift p.(Leu52SerfsTer49), combined with missense c.274C>T p.(Arg92Cys) ([PMID: 42467360](https://pubmed.ncbi.nlm.nih.gov/42467360/)). A recurrent pathogenic *INPP5K* variant was described in a European cohort ([PMID: 33193651](https://pubmed.ncbi.nlm.nih.gov/33193651/)). Alleles affecting the **catalytic domain** impair PtdIns(4,5)P₂ phosphatase activity, while **SKICH domain** alleles alter localization ([PMID: 28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/)).

> *"Functional studies confirmed the synonymous variant causes aberrant splicing (exon 3 skipping), leading to a frameshift and premature termination p.(Leu52SerfsTer49). According to American College of Medical Genetics and Genomics guidelines, the c.274C>T and c.261G>A variants were classified as likely pathogenic and pathogenic, respectively."* — [PMID: 42467360](https://pubmed.ncbi.nlm.nih.gov/42467360/)

A consanguineous Pakistani family carried homozygous c.149T>C p.(Ile50Thr) presenting predominantly as congenital cataract with reduced penetrance of muscle/cognitive features ([PMID: 28940338](https://pubmed.ncbi.nlm.nih.gov/28940338/)), supporting a role for modifiers:

> *"These phenotypic variabilities may be due to epigenetic factors and/or genetic modifiers."* — [PMID: 28940338](https://pubmed.ncbi.nlm.nih.gov/28940338/)

### Finding 6 — Clinical overlap with Marinesco-Sjögren syndrome

Hathazi et al. ([PMID: 33792664](https://pubmed.ncbi.nlm.nih.gov/33792664/)) describe that **Marinesco-Sjögren syndrome** (biallelic *SIL1* mutations) is characterized by cataracts in infancy, myopathy and ataxia — features also associated with the INPP5K disorder — and that both converge molecularly on d-3-PHGDH/L-serine dysregulation. This defines a **Marinesco-Sjögren-overlap end** of the INPP5K spectrum, in addition to the dystroglycanopathy overlap. However, overt cerebellar atrophy is typically absent on MRI in core INPP5K-CMD patients ([PMID: 28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/); [PMID: 28940338](https://pubmed.ncbi.nlm.nih.gov/28940338/)), so ataxia/cerebellar involvement occurs only in a subset.

> *"Marinesco-Sjögren syndrome is a rare human disorder caused by biallelic mutations in SIL1 characterized by cataracts in infancy, myopathy and ataxia, symptoms which are also associated with a novel disorder caused by mutations in INPP5K."* — [PMID: 33792664](https://pubmed.ncbi.nlm.nih.gov/33792664/)

### Finding 7 — gnomAD constraint confirms LoF tolerance (recessive mechanism)

Computational constraint analysis (this investigation, gnomAD v2.1.1) for *INPP5K* (ENSG00000132376; 17p13.3): **pLI = 4.5×10⁻⁸ (≈0, NOT loss-of-function intolerant)**; observed/expected pLoF (oe_lof) = 0.654 (90% CI 0.50–0.87), **LOEUF ≈ 0.87**; observed pLoF = 35 vs expected 53.5; missense Z = 0.64 (oe_mis = 0.94, not missense-constrained); synonymous Z = −0.79. These metrics indicate heterozygous carriers tolerate loss of function, exactly as expected for a **recessive, biallelic** disease mechanism. Evidence source: **[computational]**.

### Finding 8 — GTEx shows ubiquitous expression → vulnerability, not restriction

GTEx v8 median expression of *INPP5K* (ENSG00000132376.19) across 54 tissues (this investigation): expressed everywhere, range **9.7–62.3 TPM, median ~30.6 TPM**. Highest: thyroid 62.3, testis 54.3, tibial nerve 52.9, subcutaneous adipose 51.7, lung 51.4. Disease-relevant tissues: skeletal muscle 26.6; cerebellum 33.2 / cerebellar hemisphere 31.3 (highest brain regions); cortex 21.3; heart 15.6–16.2; kidney cortex 14.6 / medulla 17.3. Lowest: liver 9.7, pancreas 10.6. Because expression is ubiquitous, the tissue selectivity of INPP5K-CMD (muscle, lens, brain) reflects **differential cellular vulnerability** rather than restricted expression. Evidence source: **[computational]**.

### Finding 9 — gnomAD-derived prevalence estimate: ~1 per million (lower bound)

From gnomAD r2.1.1 variant-level data (926 variants; 27 predicted LoF alleles: frameshift, stop-gained, splice donor/acceptor, start/stop-lost), the summed pLoF allele frequency q ≈ 1.03×10⁻³. Under Hardy-Weinberg: **pLoF carrier frequency ≈ 2q ≈ 2.06×10⁻³ (~1 in 486)**; expected pLoF/pLoF homozygous birth prevalence ≈ q² ≈ **1.06×10⁻⁶ (~1 in ~946,000)**. This is a lower bound (excludes pathogenic missense/hypomorphic alleles, which account for most reported cases), consistent with the ultra-rare clinical observation of only ~30–40 patients worldwide. Evidence source: **[computational]**.

---

## Mechanistic Model / Interpretation

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic pathogenic variants in *INPP5K*** (catalytic-domain alleles or SKICH-domain alleles) → **loss of INPP5K 5-phosphatase activity** toward PtdIns(4,5)P₂/PtdIns(3,4,5)P₃ and/or **mislocalization** of the protein away from the ER membrane. *(Demonstrated — PMID 28190456.)*

2. Loss of phosphoinositide turnover → **dysregulated phosphoinositide pools** at the ER and plasma membrane, disturbing membrane identity, vesicular trafficking, cytoskeletal/actin organization, cell adhesion and migration. *(Demonstrated/inferred — PMID 33060052.)*

3. **Branch A — Insulin/PI3K-AKT signaling:** loss of SKIP removes a brake on insulin-induced PI3K-Akt-GSK3β-glycogen synthase signaling, perturbing myoblast growth/differentiation homeostasis. *(Demonstrated in myoblasts — PMID 19250614, 22403078.)*

4. **Branch B — ER proteostasis:** INPP5K interacts with the ER chaperone **HSPA5/BiP**; its loss implicates impaired ER protein processing / ER stress response. *(Inferred from interaction + MSS convergence — PMID 28190459, 33060052.)*

5. **Branch C — Glycosylation:** ER/trafficking dysfunction → **hypoglycosylation of α-dystroglycan** → weakened dystroglycan–extracellular-matrix link in muscle → sarcolemmal fragility and dystrophic muscle. *(Demonstrated — PMID 38559586, 28190459.)* This places INPP5K-CMD within the **dystroglycanopathy** spectrum.

6. **Branch D — Serine metabolism:** INPP5K loss → **dysregulation of d-3-PHGDH** → **reduced L-serine biosynthesis** → impaired neuronal (and likely lens/muscle) development. Shared with *SIL1*/Marinesco-Sjögren syndrome. *(Demonstrated; rescued by L-serine in zebrafish — PMID 33792664.)*

7. Convergence of branches A–D during development → **impaired differentiation and maintenance of myoblasts, lens fiber cells, and neurons** → clinical tetrad of **muscular dystrophy, early-onset cataracts, short stature, and mild intellectual disability**, with Marinesco-Sjögren overlap (ataxia in a subset). *(Demonstrated phenotypically — PMID 28190456, 28190459, 28940338.)*

```
  Biallelic INPP5K variants (catalytic / SKICH)
                 │
   loss of PtdIns(4,5)P2 / PtdIns(3,4,5)P3 5-phosphatase activity
     + mislocalization from ER
                 │
   dysregulated phosphoinositide pools (ER / PM)
        ┌────────────┬────────────┬─────────────┐
  (A) ↑insulin/   (B) BiP/HSPA5  (C) α-DG       (D) PHGDH ↓
   PI3K-AKT-GSK3β   ER stress     hypoglyco-      → L-serine ↓
   dysregulation                  sylation
        └────────────┴─────┬──────┴─────────────┘
          impaired myoblast / lens / neuron differentiation
                 │
   Muscular dystrophy + cataracts + short stature + mild ID
   (normal brain MRI; MSS/dystroglycanopathy overlap)
```

### Upstream vs downstream

- **Upstream (initiating):** INPP5K enzymatic/localization loss; phosphoinositide dysregulation.
- **Midstream (branching effectors):** PI3K-AKT dysregulation, ER stress/BiP, glycosylation machinery, PHGDH/serine pathway.
- **Downstream (clinical):** dystrophic muscle, cataractous lens, impaired neurodevelopment, growth restriction.

### Cell types and biological processes (ontology suggestions)

| Category | Suggested terms |
|---|---|
| Cell types (CL) | skeletal muscle myoblast (CL:0000515), skeletal muscle fiber (CL:0008002), lens fiber cell (CL:0011004), neuron (CL:0000540) |
| Biological processes (GO) | phosphatidylinositol dephosphorylation (GO:0046856), skeletal muscle cell differentiation (GO:0035914), protein glycosylation (GO:0006486), response to endoplasmic reticulum stress (GO:0034976), L-serine biosynthetic process (GO:0006564), insulin receptor signaling pathway (GO:0008286) |
| Cellular components (GO CC) | endoplasmic reticulum membrane (GO:0005789), plasma membrane (GO:0005886), cytosol (GO:0005829), nucleus (GO:0005634) |
| Anatomy (UBERON) | skeletal muscle tissue (UBERON:0001134), lens of camera-type eye (UBERON:0000965), cerebellum (UBERON:0002037), brain (UBERON:0000955) |
| Chemical entities (CHEBI) | PtdIns(4,5)P₂ (CHEBI:83416), PtdIns(3,4,5)P₃ (CHEBI:16618), L-serine (CHEBI:17115) |

---

## Section-by-Section Content

### 1. Disease Information
A rare autosomal recessive congenital muscular dystrophy defined by muscle, lens, growth and cognitive involvement. **Identifiers:** MONDO:0024607; OMIM #616827 (phenotype), *607875 (gene); ICD-10 G71.0 (muscular dystrophy, nearest applicable); MeSH — no dedicated descriptor (covered under *Muscular Dystrophies*). **Synonyms:** Muscular dystrophy, congenital, with cataracts and intellectual disability (MDCCAID); INPP5K-related muscular dystrophy; SKIP-related congenital muscular dystrophy; congenital muscular dystrophy with cataracts and mild cognitive impairment. Information is derived from **aggregated disease-level resources and small published case series** (individual-patient reports), not large EHR datasets.

### 2. Etiology
**Primary cause:** monogenic — biallelic (homozygous or compound heterozygous) pathogenic variants in *INPP5K*. **Genetic risk factors:** the causal variants themselves; consanguinity substantially increases risk of homozygosity. **Modifiers:** epigenetic factors and/or genetic modifiers proposed to explain reduced penetrance/variable expressivity ([PMID: 28940338](https://pubmed.ncbi.nlm.nih.gov/28940338/)). **Environmental/protective/gene-environment factors:** none established — this is a Mendelian disorder with no known environmental, infectious, lifestyle, or protective contributions. **Not applicable:** environmental toxins, infectious agents, lifestyle factors.

### 3. Phenotypes
See Finding 2 table. Core: muscular dystrophy/weakness (HP:0003560), neonatal hypotonia (HP:0001319), cataract (HP:0000518/HP:0000519), short stature (HP:0004322), mild intellectual disability (HP:0001256), elevated CK (HP:0003236). Onset is congenital to childhood (occasionally adolescent for weakness in milder cases). Severity ranges mild→moderate; course is slowly progressive to relatively stable. **Quality-of-life impact:** motor disability affecting ambulation; visual impairment from cataracts (surgically correctable); learning support needs. No disease-specific QoL instrument has been published.

### 4. Genetic/Molecular Information
**Causal gene:** *INPP5K* (SKIP), 17p13.3, OMIM *607875, HGNC:21940, UniProt Q9BT40. **Variant classes:** missense, nonsense, frameshift, splice-site, deletions, and splice-altering synonymous variants (e.g., c.261G>A causing exon 3 skipping). **Functional consequence:** loss of function / hypomorphic — either loss of catalytic phosphatase activity (catalytic-domain alleles) or altered subcellular localization (SKICH-domain alleles) ([PMID: 28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/)). **Allele frequency:** individual pathogenic alleles are ultra-rare/absent in gnomAD; summed pLoF q ≈ 1×10⁻³. **Origin:** germline. **Classification examples:** c.274C>T p.(Arg92Cys) likely pathogenic; c.261G>A p.(Lys87=) pathogenic (ACMG) ([PMID: 42467360](https://pubmed.ncbi.nlm.nih.gov/42467360/)). **Chromosomal abnormalities / epigenetics:** none established as causal (note: *Inpp5k* appears in a rat 17p tumor-suppressor deletion region — not relevant to CMD — [PMID: 26170120](https://pubmed.ncbi.nlm.nih.gov/26170120/)).

### 5. Environmental Information
Not applicable — no environmental, lifestyle, or infectious contributors are known for this Mendelian disorder.

### 6. Mechanism / Pathophysiology
See **Mechanistic Model** above (ordered causal chain, branches A–D, ontology terms).

### 7. Anatomical Structures Affected
**Primary organs:** skeletal muscle (UBERON:0001134), ocular lens (UBERON:0000965). **Nervous system:** brain/cerebellum (subset; UBERON:0002037) — cognition; MRI usually normal. **Body systems:** musculoskeletal, ocular/visual, nervous. **Tissue/cell:** skeletal muscle fibers, lens fiber cells, neurons. **Subcellular:** endoplasmic reticulum membrane (GO:0005789), plasma membrane, cytosol, nucleus. **Lateralization:** bilateral/symmetric (cataracts and muscle involvement).

### 8. Temporal Development
**Onset:** congenital to childhood (insidious/chronic); cataracts often congenital/early childhood; weakness from birth in classic cases, adolescent in milder cases. **Progression:** slowly progressive to relatively stable; selective muscle fatty infiltration pattern over time. **Course:** chronic, lifelong. **Critical period:** prenatal/early postnatal development (myogenesis, lens formation, neurodevelopment) — the window where L-serine/phosphoinositide pathways are most active and, potentially, most therapeutically relevant.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** reduced/incomplete for individual features (muscular dystrophy, ID); **expressivity:** highly variable. **Epidemiology:** ultra-rare, ~30–40 reported patients; predicted biallelic-pLoF birth prevalence ~1 per million (lower bound); carrier frequency ~1 in 500 (gnomAD-derived, this investigation). **Consanguinity:** major contributor to homozygous cases (Middle Eastern, South Asian families reported). **Founder/recurrent alleles:** a recurrent European variant reported ([PMID: 33193651](https://pubmed.ncbi.nlm.nih.gov/33193651/)). **Sex ratio:** no sex bias expected (autosomal). **No genetic anticipation** (not a repeat-expansion disorder).

### 10. Diagnostics
**Laboratory:** elevated serum creatine kinase (HP:0003236). **Electrophysiology:** EMG may show myopathic/irritable myopathy changes. **Imaging:** cranial MRI typically **normal** (key differentiator); **muscle MRI** shows characteristic selective fatty infiltration (severe gluteal/thigh, sparing rectus femoris, sartorius, gracilis — [PMID: 42467360](https://pubmed.ncbi.nlm.nih.gov/42467360/)); **muscle ultrasound** is a useful bedside tool ([PMID: 39133882](https://pubmed.ncbi.nlm.nih.gov/39133882/)). **Biopsy/IHC:** dystrophic features; reduced α-dystroglycan glycosylation on IHC. **Ophthalmology:** slit-lamp for cataracts. **Genetic testing (definitive):** WES or WGS, or CMD/limb-girdle gene panels including *INPP5K*; single-gene testing confirms candidate variants. RNA studies can confirm splice-altering variants. **Differential diagnosis:** classic dystroglycanopathies (abnormal brain MRI), Marinesco-Sjögren syndrome (*SIL1*; cerebellar atrophy), other congenital muscular dystrophies and congenital cataract syndromes.

### 11. Outcome/Prognosis
**Survival:** no reported reduction in life expectancy from the muscular dystrophy itself; the disorder is **non-lethal and slowly progressive** in reported cases. **Morbidity:** motor disability (ambulation), visual impairment (surgically treatable cataracts), learning/cognitive support needs. **Complications:** potential orthopedic (contractures), respiratory monitoring as in other CMDs (not specifically quantified). **Prognostic factors:** variant severity (null vs hypomorphic) and genotype likely influence phenotype severity, though formal correlations are limited by small numbers. No validated prognostic biomarker.

### 12. Treatment
**No approved disease-modifying therapy.** Management is **supportive/multidisciplinary** (NCIT: Supportive Care; Physical Therapy; Occupational Therapy): cataract extraction surgery (NCIT: Cataract Surgery), physiotherapy to maintain mobility, developmental/educational support, low-vision support, orthopedic management. **Experimental/mechanism-based:** **L-serine supplementation** (CHEBI:17115) is a rationally supported candidate — it rescued neuronal phenotypes in *inpp5k*, *sil1*, and *phgdh* zebrafish models ([PMID: 33792664](https://pubmed.ncbi.nlm.nih.gov/33792664/)) — but has **not been tested in INPP5K-CMD patients** (no NCT identifier). **Pharmacogenomics / gene / cell / RNA / targeted / immunotherapies:** none established. **Treatment algorithm:** symptom-directed, following general congenital muscular dystrophy care standards.

### 13. Prevention
No primary prevention (Mendelian). **Genetic counseling** is central: 25% recurrence risk for carrier couples; **carrier/cascade testing** for at-risk relatives; **prenatal diagnosis** and **preimplantation genetic testing** are available once familial variants are identified. Consanguinity counseling in affected populations. No vaccine, behavioral, public-health, or prophylactic interventions apply. Not part of standard newborn screening.

### 14. Other Species / Natural Disease
**Orthologs:** mouse *Inpp5k* (NCBI Gene 19062), rat *Inpp5k*, zebrafish *inpp5ka/inpp5kb*, pig *SKIP*. **No naturally occurring companion-animal/wildlife disease** attributable to *INPP5K* is catalogued (not in OMIA to the knowledge base). **Comparative biology:** evolutionary conservation is high — the zebrafish model faithfully reproduces muscle, eye, and brain phenotypes (see Finding 4), and porcine/rodent SKIP studies recapitulate the muscle-differentiation and insulin-signaling roles. **No zoonotic potential** (genetic disease).

### 15. Model Organisms
**Zebrafish** (NCBI Taxon 7955): morpholino *inpp5k* knockdown → shortened body axis, microphthalmia/disorganized lens, microcephaly, reduced motility, disorganized myofibers ([PMID: 28190459](https://pubmed.ncbi.nlm.nih.gov/28190459/), [PMID: 28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/)); *inpp5ka* mutants show variable skeletal muscle abnormalities ([PMID: 28940338](https://pubmed.ncbi.nlm.nih.gov/28940338/)); double *inpp5ka+b* model used for **L-serine rescue** ([PMID: 33792664](https://pubmed.ncbi.nlm.nih.gov/33792664/)). **Mouse N2A neuroblastoma** cells: INPP5K knockdown impairs neuronal differentiation and glycosylation ([PMID: 38559586](https://pubmed.ncbi.nlm.nih.gov/38559586/)). **C2C12 myoblasts** (mouse): SKIP knockdown/overexpression define insulin-PI3K-AKT regulation ([PMID: 19250614](https://pubmed.ncbi.nlm.nih.gov/19250614/)). **Porcine SKIP:** muscle-development and MyoD-regulation studies ([PMID: 20336382](https://pubmed.ncbi.nlm.nih.gov/20336382/), [PMID: 22682687](https://pubmed.ncbi.nlm.nih.gov/22682687/)). **Phenotype recapitulation:** zebrafish captures the muscle/eye/brain triad well; **limitation** — no published mammalian (mouse) *Inpp5k*-null disease model recapitulating the full human tetrad, and cataract/short-stature phenotypes are less characterized across models.

---

## Evidence Base

| PMID | Title (abbrev.) | Role / contribution | Evidence type |
|---|---|---|---|
| [28190459](https://pubmed.ncbi.nlm.nih.gov/28190459/) | Mutations in INPP5K cause a CMD overlapping MSS & dystroglycanopathy | Landmark; establishes causality, zebrafish model, dystroglycan/BiP | Human + zebrafish |
| [28190456](https://pubmed.ncbi.nlm.nih.gov/28190456/) | Mutations in INPP5K cause CMD with cataracts & cognitive impairment | Landmark; defines tetrad, normal MRI, two mutational mechanisms | Human + functional |
| [33792664](https://pubmed.ncbi.nlm.nih.gov/33792664/) | INPP5K & SIL1 converge through PHGDH dysregulation | MSS overlap; PHGDH/L-serine mechanism; L-serine rescue | Human + zebrafish proteomics |
| [38559586](https://pubmed.ncbi.nlm.nih.gov/38559586/) | Knockdown of INPP5K compromises N2A differentiation | Links to dystroglycan hypoglycosylation & neuronal differentiation | In vitro |
| [28940338](https://pubmed.ncbi.nlm.nih.gov/28940338/) | INPP5K variant causes recessive congenital cataract | Reduced penetrance/variable expressivity; modifiers | Human |
| [42467360](https://pubmed.ncbi.nlm.nih.gov/42467360/) | INPP5K-MD from synonymous splicing variant (China) | Expands variant spectrum; muscle MRI pattern; ACMG | Human + functional |
| [33060052](https://pubmed.ncbi.nlm.nih.gov/33060052/) | INPP5K: gene structure to in vivo functions | Enzymatic/structural basis; domains; functions | Review |
| [19250614](https://pubmed.ncbi.nlm.nih.gov/19250614/) | SKIP knockdown enhances insulin glycogen signaling (C2C12) | Insulin-PI3K-AKT-GSK3β regulation in muscle | In vitro |
| [20336382](https://pubmed.ncbi.nlm.nih.gov/20336382/) | MyoD control of SKIP during muscle development | SKIP is a MyoD-regulated myogenesis gene | Model (pig) |
| [22403078](https://pubmed.ncbi.nlm.nih.gov/22403078/) | Phosphoinositide phosphatases | Family context; SKIP negatively regulates insulin signaling | Review |
| [19272022](https://pubmed.ncbi.nlm.nih.gov/19272022/) | Role of 5-phosphatases in disease | Family of 10; OCRL/INPP5E/SHIP2 disease links | Review |
| [33193651](https://pubmed.ncbi.nlm.nih.gov/33193651/) | Recurrent pathogenic INPP5K variant | Recurrent/founder allele in a cohort | Human |
| [39133882](https://pubmed.ncbi.nlm.nih.gov/39133882/) | Muscle ultrasound in INPP5K-MD | Diagnostic tool | Human case |
| [22682687](https://pubmed.ncbi.nlm.nih.gov/22682687/) | Porcine SKIP in muscle development | Muscle development/insulin role | Model (pig) |
| [26170120](https://pubmed.ncbi.nlm.nih.gov/26170120/) | Inpp5k/Myo1c as candidate tumor suppressors | Tangential (cancer context, not CMD) | Model (rat) |

Computational evidence generated in this investigation: gnomAD v2.1.1 constraint (Findings 7, 9) and GTEx v8 expression (Finding 8), retrieved via the gnomAD GraphQL and GTEx APIs.

---

## Limitations and Knowledge Gaps

1. **Extremely small patient numbers (~30–40 worldwide)** preclude formal epidemiology, robust genotype–phenotype correlation, and natural-history/prognosis quantification. All clinical content derives from case reports/small series with inherent ascertainment bias.
2. **No formal prevalence/incidence estimate exists.** The ~1 per million figure is a computational lower bound from gnomAD pLoF alleles only and excludes the pathogenic missense/hypomorphic variants that cause most reported cases — true prevalence is uncertain.
3. **Mechanistic branches are partially inferred.** The BiP/HSPA5 ER-stress arm and the precise route from phosphoinositide dysregulation to dystroglycan hypoglycosylation are supported by interaction/association data rather than fully resolved causal demonstration in human muscle.
4. **No mammalian (mouse) disease model** recapitulating the full human tetrad has been published; zebrafish and cell models dominate, limiting translational and cataract/growth-phenotype study.
5. **L-serine therapy is unproven in humans** — efficacy shown only in zebrafish; no clinical trial (no NCT) exists. Optimal dose, timing (critical developmental window), and which phenotypes might respond are unknown.
6. **Modifier genes and epigenetic factors** invoked to explain variable expressivity/reduced penetrance are hypothesized but not identified.
7. **Quality-of-life and functional-outcome data** are absent; no disease-specific instruments.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry/natural-history study** to quantify penetrance, progression rate, muscle-MRI evolution, and genotype–phenotype correlations across the mutational spectrum (null vs hypomorphic; catalytic vs SKICH alleles).
2. **Generate a conditional/knock-in mouse model** (e.g., patient-specific missense knock-in) to test whether the full tetrad is recapitulated in a mammal and to serve as a preclinical therapeutic platform.
3. **Pilot clinical evaluation of L-serine supplementation** in INPP5K-CMD patients, guided by metabolomic PHGDH/serine biomarkers, with careful attention to the developmental critical window suggested by the zebrafish rescue.
4. **Define the glycosylation defect mechanistically** — quantify α-dystroglycan glycosylation and map the phosphoinositide→glycosylation link in patient-derived myotubes/iPSC-myocytes, integrating lipidomics (PtdIns species) with proteomics.
5. **Patient-derived iPSC models** (myocytes, lens epithelial cells, cortical neurons) to dissect tissue-specific vulnerability despite ubiquitous expression (Finding 8) and to screen for small molecules correcting ER stress, PI3K-AKT dysregulation, or serine deficiency.
6. **Systematic variant functional assays** (phosphatase activity, localization, splicing) to resolve VUS and build an ACMG-aligned variant interpretation resource for *INPP5K*.
7. **Search for modifier loci** via whole-genome analysis of discordant family members (e.g., the reduced-penetrance Pakistani family) to explain variable expressivity.

---

*Report compiled from 9 confirmed findings and 15 reviewed papers across a 5-iteration autonomous investigation. Evidence types are distinguished throughout as human clinical, model organism (zebrafish/pig/mouse cell), in vitro, or computational (gnomAD/GTEx).*


## Artifacts

- [OpenScientist final report](INPP5K-Related_Congenital_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](INPP5K-Related_Congenital_Muscular_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001251` (1 mention) - the report calls it "Ataxia (subset, MSS-overlap)"; HP calls it **Ataxia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:17115` (2 mentions) - the report calls it "L-serine supplementation"; CHEBI calls it **L-serine**