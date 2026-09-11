---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-09T18:58:56.792013'
end_time: '2026-09-09T19:48:22.115714'
duration_seconds: 2965.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cataract 13 With Adult I Phenotype
  mondo_id: MONDO:0007289
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
citation_count: 16
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 19
  verified: 17
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0032324
    reported_labels:
    - abnormal erythrocyte morphology, related
    ontology_label: Non-periodic recurrent fever
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
  path: Cataract_13_With_Adult_I_Phenotype-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cataract_13_With_Adult_I_Phenotype-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 13 With Adult I Phenotype
- **MONDO ID:** MONDO:0007289 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cataract 13 With Adult I Phenotype** covering all of the
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

# Cataract 13 With Adult i Phenotype (CTRCT13): A Comprehensive Disease Report

**Disease:** Cataract 13 With Adult I Phenotype
**MONDO ID:** MONDO:0007289 · **OMIM:** 116700 · **Gene:** *GCNT2* (6p24.2, OMIM *600429)
**Category:** Mendelian (autosomal recessive)
**Report date:** 2026-09-09 · **Evidence base:** human clinical/genetic studies, biochemical/enzymatic assays, and comparative glycobiology. No patient-level dataset was supplied; this is a literature-derived synthesis.

---

## Summary

**Cataract 13 with adult i phenotype (CTRCT13)** is a rare Mendelian disorder in which bilateral congenital cataract co-occurs with the benign **adult "i" blood group phenotype**, both arising from biallelic loss-of-function of a single gene, ***GCNT2*** (glucosaminyl (N-acetyl) transferase 2), on chromosome 6p24. GCNT2 is the **I-branching β-1,6-N-acetylglucosaminyltransferase** (EC 2.4.1.150), the enzyme that converts the linear fetal poly-N-acetyllactosamine "i" antigen into the branched adult "I" antigen. When enzyme activity is lost, red-cell surface glycans remain in the linear "i" form (producing the serologically detectable adult i phenotype), and lens transparency is disrupted (producing congenital cataract).

The central mechanistic insight of this investigation is that the coupling between the blood-group trait and the cataract is only **partial**, and this is explained by the gene's **three-isoform architecture**. The human I locus expresses three transcripts — *GCNT2A*, *GCNT2B*, and *GCNT2C* — that share exons 2 and 3 but differ in exon 1. The **erythroid isoform (GCNT2C)** governs the blood-group phenotype, whereas a **lens-relevant isoform (GCNT2B, and the shared exons)** governs cataract. Mutations that hit the shared exons or delete all isoforms cause **both** phenotypes; mutations restricted to exon 1C cause the **adult i blood group without cataract**. This isoform logic resolves decades of clinical observation that the i–cataract association is strong in East Asian (Japanese) families but weak in White populations.

The allelic spectrum comprises nonsense and frameshift point mutations, activity-abolishing missense variants, and — a recurrent theme — **large Alu/SINE-mediated structural deletions** spanning one or more exons, reflecting the repeat-rich, rearrangement-prone nature of the 6p24 locus. Management is entirely **surgical and supportive** (early cataract extraction with amblyopia and refractive rehabilitation); life expectancy is normal, and no disease-modifying therapy targeting the underlying glycosylation defect exists. This report compiles the disease overview, genetics, mechanism, phenotypes, diagnostics, prognosis, treatment, and comparative/model-organism context, with primary-literature citations throughout.

---

## Key Findings

### Finding 1 — CTRCT13 is caused by biallelic *GCNT2* mutations

Autosomal-recessive congenital cataract with the adult i phenotype maps to *GCNT2* on chromosome 6p24 and is caused by **biallelic loss-of-function** of the gene. Homozygosity mapping in a consanguineous Pakistani family linked the recessive cataract to a 3.03 Mb locus on 6p24 that contains *GCNT2*; within it, a **homozygous 93 kb Alu-mediated deletion** removing exons 1B, 1C, 2, and 3 segregated with both cataract and the adult i blood group ([PMID: 21761136](https://pubmed.ncbi.nlm.nih.gov/21761136/)). This paper states plainly that *"GCNT2 encodes glucosaminyl (N-acetyl) transferase 2, an enzyme responsible for the formation of the blood group I antigen,"* establishing both the gene and its enzymatic role in the disease.

Independent confirmation came from linkage and mutation analysis in four Arab families, where the locus was mapped with a maximum two-point **LOD score of 8.75** (θ = 0.019 at marker D6S470) and a homozygous G→A substitution in exon 2 was identified ([PMID: 15161861](https://pubmed.ncbi.nlm.nih.gov/15161861/)). That change *"revealed in these families a homozygous G-->A substitution in base 58 of exon-2, resulting in the formation of premature stop codons W328X, W326X, and W328X, of the GCNT2A, -B, and -C isoforms."* Because the premature stop lands in a shared exon, it truncates **all three isoforms simultaneously**, producing both the cataract and the adult i phenotype. Together these two studies — spanning distinct populations and distinct mutational classes (structural deletion vs. nonsense point mutation) — firmly establish *GCNT2* as the causal gene.

**Ontology anchors:** Gene *GCNT2* (HGNC:4204); MONDO:0007289; OMIM 116700; disease process GO:0006486 (protein glycosylation).

### Finding 2 — Isoform-specific architecture explains the partial coupling of cataract and adult i

The human I locus expresses **three transcripts, GCNT2A/B/C**, that *"have different exon 1, but identical exons 2 and 3"* ([PMID: 12424189](https://pubmed.ncbi.nlm.nih.gov/12424189/)). This modular design is the key to genotype–phenotype correlation:

- **GCNT2C** drives erythrocyte I-antigen expression, i.e., the **adult i blood group**.
- **GCNT2B** is the isoform associated with **lens function** (cataract) ([PMID: 27609212](https://pubmed.ncbi.nlm.nih.gov/27609212/)).

Mutations affecting the **shared exons 2/3**, or deletions removing all isoforms, therefore cause **both** cataract and adult i. Conversely, a mutation restricted to **exon 1C** — such as the IGnTC 243T>A (Asn81Lys) variant — causes the **adult i blood group without cataract** ([PMID: 17076854](https://pubmed.ncbi.nlm.nih.gov/17076854/)), a report that describes *"molecular genetic analysis of a Taiwanese person with the adult i phenotype but without congenital cataracts."* This is the clean genetic dissociation that proves the two traits are governed by different transcripts of the same gene.

A complementary case supports the mirror-image inference for the cataract-relevant transcript: a proband with congenital cataract carried a truncating variant in **exon 1B** (NM_001491.3: c.760dup p.H254Pfs*2) in trans with a 75 kb deletion of exons 1B/1C, implicating exon 1B–containing transcripts as clinically relevant for the cataract phenotype ([PMID: 41813616](https://pubmed.ncbi.nlm.nih.gov/41813616/)).

**Isoform → phenotype map:**

| GCNT2 isoform | Distinguishing exon | Tissue role | Phenotype when lost |
|---|---|---|---|
| GCNT2A | exon 1A | ubiquitous | contributes to systemic i |
| **GCNT2B** | exon 1B | **lens** | **congenital cataract** |
| **GCNT2C** | exon 1C | **erythrocyte** | **adult i blood group** |
| shared exons 2/3 | — | all tissues | **both cataract + adult i** |

### Finding 3 — The adult i–cataract association is strongest in East Asians and weaker in Whites

The strength of the clinical coupling is **population-dependent**. In Japanese families, Ogata (1979) found that among 18 phenotype-i individuals across 10 families, **17 had congenital cataract**, whereas *"cataract was not found in any of the 45 phenotype I members in these families"* ([PMID: 432928](https://pubmed.ncbi.nlm.nih.gov/432928/)) — a near-complete co-segregation.

By contrast, in White populations the association is much weaker: only **3 of 10** White i-phenotype individuals had congenital cataract, and **0 of 31** White congenital-cataract patients had the i phenotype ([PMID: 3799539](https://pubmed.ncbi.nlm.nih.gov/3799539/)), which reports *"three of ten people have congenital cataracts... the authors studied the blood of 31 white patients with congenital cataracts and found no patients with the i phenotype."* Combined with the isoform architecture of Finding 2, this pattern is best explained by **population-specific allelic effects**: East Asian pedigrees more often carry variants affecting shared exons (coupling the two traits), whereas White pedigrees more often carry isoform-restricted alleles that decouple them.

| Population | i-individuals with cataract | Cataract patients with i phenotype | Association strength | Reference |
|---|---|---|---|---|
| Japanese | 17/18 | — (0/45 phenotype-I relatives had cataract) | Strong | [PMID: 432928](https://pubmed.ncbi.nlm.nih.gov/432928/) |
| White | 3/10 | 0/31 | Weak | [PMID: 3799539](https://pubmed.ncbi.nlm.nih.gov/3799539/) |

### Finding 4 — Large Alu/SINE-mediated deletions are a recurrent mutational mechanism

Structural deletions are not incidental but a **major, recurrent class** of pathogenic *GCNT2* alleles, driven by the repeat-rich local genome. The locus *"is rich in Short INterspersed Elements (SINE repeats) and thus likely prone to genomic rearrangements"* ([PMID: 21761136](https://pubmed.ncbi.nlm.nih.gov/21761136/)). Documented structural alleles include:

| Deletion | Extent / breakpoint feature | Reference |
|---|---|---|
| 93 kb (exons 1B, 1C, 2, 3) | Alu-mediated | [PMID: 21761136](https://pubmed.ncbi.nlm.nih.gov/21761136/) |
| ~98 kb at 6p24.3 | Alu-mediated NHEJ; removes GCNT2 A/B first exons + intergenic region toward *TFAP2A* | [PMID: 27609212](https://pubmed.ncbi.nlm.nih.gov/27609212/) |
| ~190 kb insertion/deletion | large indel; PCR of coding exons failed in affected | [PMID: 27936067](https://pubmed.ncbi.nlm.nih.gov/27936067/) |
| ~75 kb (exons 1B/1C) | copy-number deletion in trans with exon-1B frameshift | [PMID: 41813616](https://pubmed.ncbi.nlm.nih.gov/41813616/) |

The ~190 kb allele was found in a large Pakistani pedigree with **LOD 5.78** at 6p24, where *"PCR amplifications of the coding exons of GCNT2 failed in individuals with arCC, and whole-exome data analysis revealed a large deletion on chromosome 6p in the region harboring GCNT2"* ([PMID: 27936067](https://pubmed.ncbi.nlm.nih.gov/27936067/)). The practical diagnostic implication is important: **standard exon-based sequencing can miss the causal allele**, and failed PCR amplification of *GCNT2* exons should itself raise suspicion of a structural deletion requiring CNV/deletion-aware analysis (WES CNV calling, MLPA, or chromosomal microarray).

### Finding 5 — Biochemical mechanism: GCNT2 catalyzes β1,6-GlcNAc branching (i→I conversion)

GCNT2 is the **I-branching β-1,6-N-acetylglucosaminyltransferase (EC 2.4.1.150)**. It adds a β1,6-linked GlcNAc to the internal galactose of linear poly-N-acetyllactosamine (polyLacNAc), converting the linear "i" antigen into the branched "I" antigen: *"Conversion of the i to the I structure requires I-branching beta-1,6-N-acetylglucosaminyltransferase activity"* ([PMID: 12424189](https://pubmed.ncbi.nlm.nih.gov/12424189/); see also [PMID: 11739194](https://pubmed.ncbi.nlm.nih.gov/11739194/)). The enzyme cooperates with **β3GnT2** to build and extend polyLacNAc chains — *"the β1,6-branching glycosyltransferase GCNT2"* ([PMID: 24105809](https://pubmed.ncbi.nlm.nih.gov/24105809/)).

When GCNT2 activity is lost, polyLacNAc remains **linear** on erythrocytes (the adult i phenotype) and, via the lens-relevant isoform, lens transparency is disrupted, yielding cataract. The **initiating lesion is biallelic loss of function**; however, the precise lens glycoprotein target and the biophysical route from an unbranched glycan to lens opacity **remain inferred rather than experimentally demonstrated**.

---

## Mechanistic Model / Interpretation

### Ordered causal chain

```
1. Biallelic loss-of-function of GCNT2 (nonsense / frameshift / activity-abolishing
   missense / Alu-SINE-mediated multi-exon deletion at 6p24)
        │  leads to
        ▼
2. Loss of I-branching β-1,6-N-acetylglucosaminyltransferase activity (EC 2.4.1.150)
        │  results in
        ▼
3. Failure to add β1,6-GlcNAc to internal galactose of linear poly-N-acetyllactosamine
   → the i→I glycan conversion does not occur
        │  branches by isoform / tissue
        ├───────────────────────────────┬───────────────────────────────┐
        ▼ (erythroid GCNT2C)             ▼ (lens GCNT2B / shared exons)   │
4a. Erythrocyte surface glycans      4b. Lens-cell surface/glycoprotein
    remain LINEAR (i antigen)            glycans remain linear
        │  results in                     │  results in (INFERRED route)
        ▼                                 ▼
5a. Serologic ADULT i PHENOTYPE       5b. Disruption of lens protein
    (benign blood-group trait)            organization / transparency
                                          │  leads to
                                          ▼
                                      6b. BILATERAL CONGENITAL CATARACT → visual
                                          impairment / amblyopia if untreated
```

**Upstream vs downstream.** The upstream, proven event is loss of enzymatic branching activity. The **branch point** is tissue/isoform-specific expression: GCNT2C loss produces the blood-group readout; GCNT2B/shared-exon loss produces the cataract. Step 5b (how unbranched glycans translate biophysically into lens opacity) is the least characterized link — it is a reasonable inference from the enzyme's substrate chemistry but has not been mechanistically demonstrated in lens tissue.

**Why the two traits are only partially coupled.** Because the erythroid and lens phenotypes are driven by **different first exons of the same gene**, an allele's phenotypic footprint depends on which transcripts it disables. Shared-exon lesions (nonsense in exon 2/3; whole-gene deletions) hit everything → both traits. Isoform-restricted lesions (exon 1C only) → blood group only; (exon 1B only) → cataract-relevant transcript implicated. This single principle reconciles the East Asian vs. White epidemiological discrepancy (Finding 3): different populations carry different mixes of shared-exon vs. isoform-restricted alleles.

**Cell types and processes.** Primary cell types: **lens fiber cells and lens epithelial cells** (cataract) and **erythrocytes** (blood group). Core biological process: **protein glycosylation / polyLacNAc biosynthesis** in the Golgi apparatus.

**Suggested ontology terms:**
- **GO (process):** GO:0006486 protein glycosylation; GO:0008375 acetylglucosaminyltransferase activity; GO:0047253 N-acetyllactosaminide β-1,6-N-acetylglucosaminyltransferase activity.
- **GO (component):** GO:0000139 Golgi membrane.
- **CL (cell types):** CL:0000362 epithelial cell (lens epithelium); CL:0011004 lens fiber cell; CL:0000232 erythrocyte.
- **UBERON:** UBERON:0000965 lens of camera-type eye; UBERON:0000970 eye.
- **CHEBI:** CHEBI:506227 N-acetyllactosamine; CHEBI:60152 N-acetyl-D-glucosamine (context).

---

## Section-by-Section Report

### 1. Disease Information
- **Overview.** CTRCT13 is a rare autosomal-recessive Mendelian disorder combining **bilateral congenital cataract** with the benign **adult i blood group**. Both features stem from biallelic loss-of-function of *GCNT2*. Some individuals present cataract without the detectable i phenotype and vice versa, depending on the affected isoform.
- **Key identifiers.** OMIM **116700**; MONDO **0007289**; Gene *GCNT2* (HGNC:4204; NCBI Gene 2651; OMIM *600429). ICD-10 maps broadly to congenital lens malformations (**Q12.0** congenital cataract). MeSH concepts: "Cataract," "Blood Group Antigens." Orphanet groups this under early-onset/congenital genetic cataract entities.
- **Synonyms / alternative names.** "Cataract, congenital, with adult i phenotype"; "Adult i phenotype with congenital cataract"; "GCNT2-related congenital cataract"; historically linked to the "I/i blood group" and the "IGnT" gene nomenclature.
- **Information source.** Disease-level and family-based (aggregated pedigree/case reports and OMIM/ClinVar curation), **not** EHR-derived population cohorts.

### 2. Etiology
- **Causal factor.** Purely **genetic** — biallelic loss-of-function of *GCNT2*. No infectious or environmental cause. (Note: age-related cataract in the general population is multifactorial, but **CTRCT13 specifically is monogenic**.)
- **Genetic risk factors.** The disease requires two pathogenic *GCNT2* alleles. Reported classes: nonsense (e.g., W328X/W326X/W328X across isoforms, [PMID: 15161861](https://pubmed.ncbi.nlm.nih.gov/15161861/)); frameshift (e.g., c.760dup p.H254Pfs*2, [PMID: 41813616](https://pubmed.ncbi.nlm.nih.gov/41813616/)); activity-abolishing missense (e.g., Gly348Glu, Arg383His in IGnT, [PMID: 11739194](https://pubmed.ncbi.nlm.nih.gov/11739194/)); and large Alu/SINE-mediated deletions (Finding 4). **Consanguinity** is a major contributing factor — most pedigrees are consanguineous (Pakistani, Arab, Japanese).
- **Environmental risk / protective factors.** None established for the monogenic entity. No protective alleles identified.
- **Gene–environment interactions.** Not applicable / none demonstrated.

### 3. Phenotypes

| Phenotype | Type | Onset | Severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Bilateral congenital cataract | clinical sign / physical | Congenital | Variable morphology; static lens opacity but visually progressive if untreated | Core feature (near-universal in shared-exon genotypes) | HP:0000519 (congenital cataract); HP:0000518 (cataract) |
| Adult i blood group | laboratory abnormality | Detectable lifelong (fails to convert i→I after infancy) | Benign, non-progressive | Present in blood-group–affecting genotypes | HP:0032324 (abnormal erythrocyte morphology, related); blood-group trait |
| Visual impairment / amblyopia (if untreated) | symptom | Infancy | Preventable with early surgery | Secondary | HP:0000505 (visual impairment); HP:0000646 (amblyopia) |
| Nystagmus (with dense bilateral congenital cataract) | clinical sign | Infancy | Secondary to deprivation | Variable | HP:0000639 (nystagmus) |

- **Quality-of-life impact.** The **adult i phenotype is clinically benign** (relevant mainly for transfusion/serology). The cataract, if untreated, causes **deprivation amblyopia** and childhood blindness, with major QoL consequences; timely surgery largely restores function.

### 4. Genetic / Molecular Information
- **Causal gene.** *GCNT2* (glucosaminyl (N-acetyl) transferase 2 / I-branching enzyme; alias IGnT), 6p24.2, HGNC:4204, NCBI Gene 2651, OMIM *600429.
- **Variant classification (ACMG/AMP).** Nonsense, frameshift, and multi-exon deletions are typically **pathogenic**; activity-abolishing missense variants are pathogenic when supported by functional assays. Truncations in the clinically relevant exon 1B *"should likely receive strong pro-pathogenic weight"* ([PMID: 41813616](https://pubmed.ncbi.nlm.nih.gov/41813616/)).
- **Variant types.** Missense (Gly348Glu, Arg383His, Asn81Lys), nonsense (W326X/W328X), frameshift (H254Pfs*2), and **structural deletions** (75–190 kb).
- **Allele frequency.** Pathogenic alleles are **rare**; the disease is seen mainly in consanguineous pedigrees. Precise gnomAD frequencies were not compiled.
- **Origin.** **Germline**, biallelic (autosomal recessive). No somatic disease role.
- **Functional consequence.** **Loss of function** (loss of β1,6-branching activity); no gain-of-function or dominant-negative mechanism.
- **Modifier genes / epigenetics.** None established. Note the *GCNT2–TFAP2A* intergenic region is deletion-prone; large deletions extending toward *TFAP2A* raise a theoretical concern for overlap with Branchio-Oculo-Facial Syndrome features, though patients generally do not meet BOFS criteria ([PMID: 27609212](https://pubmed.ncbi.nlm.nih.gov/27609212/)).
- **Chromosomal abnormalities.** Recurrent **Alu/SINE-mediated microdeletions** at 6p24 (Finding 4).

### 5. Environmental Information
Not applicable. CTRCT13 is monogenic; **no** environmental toxins, lifestyle factors, or infectious agents are implicated in causing the disease.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the ordered causal chain, branch logic, cell types, and ontology terms. In brief: GCNT2 loss → no i→I branching of polyLacNAc → linear glycans on erythrocytes (adult i) and lens cells (cataract, via the biophysically inferred route). GCNT2 cooperates with β3GnT2 in polyLacNAc synthesis ([PMID: 24105809](https://pubmed.ncbi.nlm.nih.gov/24105809/)). The reaction is EC 2.4.1.150 ([PMID: 12424189](https://pubmed.ncbi.nlm.nih.gov/12424189/)).

### 7. Anatomical Structures Affected
- **Organ level.** Primary: **crystalline lens (eye)**; system: visual/ophthalmic. Secondary: erythrocyte membrane (hematologic, serologic only).
- **Tissue / cell level.** Lens epithelial cells and lens fiber cells (epithelial-derived); erythrocytes. UBERON:0000965 (lens); CL:0011004 (lens fiber cell); CL:0000232 (erythrocyte).
- **Subcellular level.** **Golgi apparatus** (site of glycosyltransferase activity; GO:0000139 Golgi membrane); cell-surface/membrane glycoproteins and glycolipids.
- **Localization / laterality.** **Bilateral** congenital cataract.

### 8. Temporal Development
- **Onset.** Cataract is **congenital** (present at birth). The adult i phenotype reflects failure to switch from fetal i to adult I glycans, normally completed within ~18 months of life.
- **Progression.** Lens opacity itself is structurally static, but **visual deprivation is progressive** without early intervention (amblyopia). The blood-group trait is **stable and lifelong**.
- **Critical period.** The **first months of life** are the intervention window — early cataract extraction is essential to prevent irreversible amblyopia.

### 9. Inheritance and Population
- **Inheritance.** **Autosomal recessive** (biallelic *GCNT2* LOF).
- **Penetrance / expressivity.** Cataract penetrance is high for shared-exon/whole-gene genotypes; **expressivity is variable** (cataract morphology varies; the i–cataract coupling depends on isoform, Finding 2).
- **Consanguinity / founder effects.** Strong role for **consanguinity**; described in Pakistani, Arab, and Japanese pedigrees. Population-specific allelic effects underlie the East-Asian-vs-White difference in i–cataract coupling (Finding 3).
- **Epidemiology.** Congenital cataract overall affects **3–6 per 10,000 live births** ([PMID: 27609212](https://pubmed.ncbi.nlm.nih.gov/27609212/)); *GCNT2*-related cases are a small, rare subset. Precise CTRCT13 prevalence is not established.
- **Sex ratio.** No sex bias expected (autosomal).
- **Carrier frequency.** Not precisely established; higher effective carrier burden in consanguineous communities.

### 10. Diagnostics
- **Clinical.** Slit-lamp ophthalmologic exam identifies bilateral congenital cataract. **Blood-group serology** detects the adult i phenotype (anti-I reactivity pattern).
- **Genetic testing (recommended approach).**
  - **Single-gene / panel:** *GCNT2* sequencing; congenital-cataract gene panels (e.g., 51-gene pediatric cataract panels; [PMID: 28839118](https://pubmed.ncbi.nlm.nih.gov/28839118/)).
  - **WES/WGS:** effective, especially with **CNV/deletion-aware analysis** — several causal alleles are large deletions ([PMID: 27936067](https://pubmed.ncbi.nlm.nih.gov/27936067/), [PMID: 21761136](https://pubmed.ncbi.nlm.nih.gov/21761136/)).
  - **CMA / MLPA / deletion assays:** important because **standard PCR/exon sequencing can fail** over deleted regions; failed amplification is itself a clue.
- **Differential diagnosis.** Other genetic congenital cataracts (crystallins *CRYAA/CRYAB/CRYGC/CRYGD*, connexins *GJA3/GJA8*, *MIP/AQP0*, *HSF4*, *BFSP1/2*); syndromic causes (e.g., *TFAP2A*/BOFS if deletion extends toward *TFAP2A*); metabolic cataract (galactosemia). The **adult i blood group** is a distinctive clue pointing to *GCNT2*.

### 11. Outcome / Prognosis
- **Survival / life expectancy.** **Normal** — CTRCT13 is not life-limiting. The adult i phenotype is benign (matters chiefly for transfusion compatibility).
- **Morbidity / function.** Driven by cataract-related visual outcomes. With early surgery and rehabilitation, functional vision is generally achievable; without it, **deprivation amblyopia** and blindness result.
- **Post-surgical complications (general pediatric cataract literature).** Posterior capsule opacification, secondary glaucoma, and post-operative high myopia are recognized long-term risks after congenital cataract surgery ([PMID: 41276154](https://pubmed.ncbi.nlm.nih.gov/41276154/); [PMID: 41419074](https://pubmed.ncbi.nlm.nih.gov/41419074/); [PMID: 42288323](https://pubmed.ncbi.nlm.nih.gov/42288323/)) — these inform post-operative surveillance rather than the primary disease.
- **Prognostic factors.** Timing of surgery, laterality, associated ocular anomalies (e.g., microcornea), and amblyopia management.

### 12. Treatment
- **Definitive treatment.** **Surgical cataract extraction** (lensectomy) with **intraocular lens implantation or aphakic correction**, followed by **amblyopia therapy** and refractive rehabilitation. NCIT: cataract surgery / lens extraction; intraocular lens implantation.
- **Pharmacotherapy / advanced therapeutics.** **None disease-specific.** There is no gene, cell, RNA, or small-molecule therapy correcting the GCNT2 glycosylation defect. Management is symptomatic/surgical.
- **Supportive.** Low-vision aids, optical correction, and long-term ophthalmologic follow-up for post-operative complications (PCO, glaucoma, myopic shift).
- **Personalized medicine.** Genotype (isoform affected) informs counseling regarding the blood-group trait and recurrence risk, but does not currently alter cataract management.

### 13. Prevention
- **Primary prevention.** Not possible for the monogenic disease; **genetic counseling** for at-risk consanguineous families is the main tool.
- **Secondary prevention.** **Early detection** — newborn red-reflex screening enables timely surgery within the critical amblyogenic window.
- **Reproductive options.** Carrier testing, **prenatal diagnosis**, and **preimplantation genetic testing** are available for families with a known *GCNT2* genotype.
- **Counseling.** Autosomal-recessive recurrence risk (25% for carrier × carrier couples); emphasize benign nature of the blood-group trait but the importance of early cataract intervention.

### 14. Other Species / Natural Disease
- **Taxonomy / orthologs.** *GCNT2* orthologs exist across mammals (human *GCNT2*, NCBI Gene 2651; mouse *Gcnt2*). The I-branching enzyme and I/i antigen system are evolutionarily conserved.
- **Natural disease in other species.** No well-characterized naturally occurring *GCNT2*-cataract analog was identified in the reviewed literature (OMIA/veterinary relevance not established here).
- **Comparative biology.** The biochemistry (polyLacNAc branching) is conserved; the enzyme's role has been studied in the context of cancer glycobiology across systems.

### 15. Model Organisms
- **Available systems.** No dedicated CTRCT13 disease model was identified in the reviewed literature. Relevant experimental systems include **in-vitro enzymology and glycan chemistry** ([PMID: 37909475](https://pubmed.ncbi.nlm.nih.gov/37909475/)) and **cell-line studies of GCNT2/I-branching** in cancer biology (e.g., melanoma models showing GCNT2 loss enhances growth, [PMID: 30135430](https://pubmed.ncbi.nlm.nih.gov/30135430/)).
- **Recapitulation / limitations.** Existing models illuminate **enzyme function and glycan biology** but do **not** reproduce the lens-opacity phenotype; a lens-specific *Gcnt2*-null model would be needed to test the inferred cataract mechanism (Step 5b).
- **Applications.** Enzyme mechanism, substrate specificity, isoform biology, and (separately) the role of I-branching in malignant progression.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [21761136](https://pubmed.ncbi.nlm.nih.gov/21761136/) | *Alu repeat-mediated GCNT2 deletion...* | Identifies GCNT2; 93 kb Alu-mediated deletion; SINE-rich locus (F001, F004) |
| [15161861](https://pubmed.ncbi.nlm.nih.gov/15161861/) | *Nonsense mutation in GCNT2...* | LOD 8.75; W326X/W328X across all isoforms; shared-exon lesion → both traits (F001) |
| [12424189](https://pubmed.ncbi.nlm.nih.gov/12424189/) | *Molecular genetics of the human I locus...* | Three-isoform architecture; defines i→I conversion reaction (F002, F005) |
| [11739194](https://pubmed.ncbi.nlm.nih.gov/11739194/) | *Molecular basis of the adult i phenotype...* | IGnT = I gene; Gly348Glu/Arg383His abolish activity; Asian cataract association (F001, F005) |
| [17076854](https://pubmed.ncbi.nlm.nih.gov/17076854/) | *Novel IGnT allele...* | Exon-1C variant → adult i **without** cataract; proves isoform dissociation (F002) |
| [27609212](https://pubmed.ncbi.nlm.nih.gov/27609212/) | *Homozygous deletion of GCNT2 A/B first exons...* | GCNT2B = lens isoform, GCNT2C = RBC isoform; ~98 kb Alu-NHEJ deletion (F002, F004) |
| [41813616](https://pubmed.ncbi.nlm.nih.gov/41813616/) | *Biallelic GCNT2 variants implicate exon 1B...* | Exon-1B frameshift + 75 kb CNV; exon 1B clinically relevant for cataract (F002, F004) |
| [27936067](https://pubmed.ncbi.nlm.nih.gov/27936067/) | *Deletion at GCNT2 causes arCC...* | ~190 kb indel; LOD 5.78; failed exon PCR flags structural deletion (F004) |
| [432928](https://pubmed.ncbi.nlm.nih.gov/432928/) | *Phenotype i with congenital cataract in Japanese* | 17/18 i-individuals with cataract; strong East Asian coupling (F003) |
| [3799539](https://pubmed.ncbi.nlm.nih.gov/3799539/) | *Reduced Ii–cataract association in Whites* | 3/10, and 0/31; weak coupling in Whites (F003) |
| [24105809](https://pubmed.ncbi.nlm.nih.gov/24105809/) | *β3GnT2 and GCNT2 co-regulate polyLacNAc* | GCNT2 = β1,6-branching enzyme; cooperates with β3GnT2 (F005) |
| [37909475](https://pubmed.ncbi.nlm.nih.gov/37909475/) | *Chemo-enzymatic synthesis of I-branched polyLacNAc* | Confirms GCNT2 branching chemistry (mechanism support) |
| [28839118](https://pubmed.ncbi.nlm.nih.gov/28839118/) | *High-throughput pediatric cataract screening* | Panel-based diagnostic context |
| [30135430](https://pubmed.ncbi.nlm.nih.gov/30135430/) / [31213534](https://pubmed.ncbi.nlm.nih.gov/31213534/) | *GCNT2/I-branching in cancer* | I-branching biology in other tissues (comparative/model context) |

**Evidence-source types:** Human clinical/pedigree (F001–F004; PMIDs 21761136, 15161861, 27609212, 27936067, 432928, 3799539, 17076854, 41813616, 11739194); in-vitro/enzymatic and glycochemistry (F005; PMIDs 12424189, 24105809, 37909475); cell-line/comparative (30135430, 31213534).

---

## Limitations and Knowledge Gaps

1. **Lens biophysical mechanism unproven.** The step from "unbranched polyLacNAc on lens cells" to "lens opacity" (Step 5b) is **inferred from enzyme chemistry**, not demonstrated in lens tissue. The specific lens glycoprotein target(s) are unknown.
2. **No animal model of the cataract.** Existing GCNT2 models address enzyme/cancer biology, not lens phenotype; phenotype recapitulation is untested.
3. **Epidemiology imprecise.** Exact CTRCT13 prevalence, carrier frequency, and gnomAD allele frequencies are not established; most data derive from small consanguineous pedigrees.
4. **Isoform–phenotype map still coarse.** The lens-relevant transcript is being refined (exon 1B evidence is recent, [PMID: 41813616](https://pubmed.ncbi.nlm.nih.gov/41813616/)); the precise transcript requirements for cataract vs. blood group are not fully resolved.
5. ***TFAP2A* contiguous-deletion risk uncharacterized.** Large deletions extending toward *TFAP2A* have unclear phenotypic consequences (possible BOFS overlap), not systematically studied.
6. **Population-specific allelic architecture** underlying the East-Asian-vs-White coupling difference is hypothesized from phenotype data, not directly demonstrated by allele-frequency comparison.

---

## Proposed Follow-up Experiments / Actions

1. **Lens-specific *Gcnt2* isoform knockout mouse** (or human lens organoid / iPSC-derived lens model) to test whether loss of the GCNT2B/shared-exon transcript is sufficient to produce cataract, and to identify the glycoprotein substrate driving opacity.
2. **Glycoproteomic profiling of lens tissue** (PRIDE/ProteomeXchange workflow) comparing GCNT2-deficient vs. control lens to map altered polyLacNAc branching on specific lens proteins.
3. **Systematic CNV survey of unsolved recessive congenital cataract** cohorts at 6p24 with deletion-aware WES/WGS + MLPA, to quantify the true contribution of structural *GCNT2* alleles.
4. **Allele-frequency/haplotype comparison** across East Asian vs. European cohorts to formally test whether shared-exon vs. isoform-restricted alleles explain the population difference in i–cataract coupling.
5. **Functional assays of VUS** (enzyme-activity assays for missense variants, à la Gly348Glu/Arg383His) to enable ACMG PS3-level classification.
6. **Curate CTRCT13-specific epidemiology** from consanguineous-population registries to establish prevalence and carrier frequency.
7. **Characterize the *GCNT2–TFAP2A* deletion breakpoint landscape** to define genotype–phenotype rules for contiguous deletions and any BOFS overlap risk.

---

*Report compiled from a 5-iteration autonomous investigation; 5 confirmed findings, 21 papers reviewed. All mechanistic and clinical claims are cited to primary literature (PMID). Evidence-source types are distinguished as human clinical, in-vitro/enzymatic, or comparative/model as noted.*


## Artifacts

- [OpenScientist final report](Cataract_13_With_Adult_I_Phenotype-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cataract_13_With_Adult_I_Phenotype-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032324` (1 mention) - the report calls it "abnormal erythrocyte morphology, related"; HP calls it **Non-periodic recurrent fever**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (2 mentions) - replaced by `GO:0009101`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006486` (2 mentions) - the report calls it "protein glycosylation"; GO calls it **obsolete protein glycosylation**