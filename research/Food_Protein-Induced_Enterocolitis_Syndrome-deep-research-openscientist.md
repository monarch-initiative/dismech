---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T19:13:04.318628'
end_time: '2026-10-23T19:33:58.654080'
duration_seconds: 1254.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Food Protein-Induced Enterocolitis Syndrome
  mondo_id: MONDO:0100008
  category: Complex
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: FPIES
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
citation_count: 23
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 30
  quotes_valid: 30
  relevance_assessed: 23
  on_topic: 23
  validator_version: 0.3.0
term_validation:
  total_terms: 34
  verified: 31
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 19
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: NCIT:C1157
    reported_labels:
    - NCIT suggestions:** Ondansetron
    ontology_label: Recombinant GRO1 Protein
  - term_id: CL:0000084
    reported_labels:
    - "T cell \u2014 not antigen-specific"
    ontology_label: T cell
  - term_id: CL:0000548
    reported_labels:
    - enteroendocrine/enterochromaffin cell
    - enterochromaffin/enteroendocrine cells
    ontology_label: obsolete animal cell
  labels_variant: 5
  obsolete_terms:
  - term_id: CL:0000548
    ontology_label: obsolete animal cell
    replaced_by: CL:0000000
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
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
  path: Food_Protein-Induced_Enterocolitis_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Food_Protein-Induced_Enterocolitis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Food Protein-Induced Enterocolitis Syndrome
- **MONDO ID:** MONDO:0100008 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** FPIES
- **Category:** Complex

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Food Protein-Induced Enterocolitis Syndrome** covering all of the
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

# Food Protein-Induced Enterocolitis Syndrome (FPIES): Comprehensive Disease Characteristics Report

**Disease:** Food Protein-Induced Enterocolitis Syndrome (FPIES)
**MONDO ID:** MONDO:0100008 | **ICD-10:** K52.21 | **MeSH:** Food Protein-Induced Enterocolitis Syndrome | **Synonyms:** FPIES
**Causal gene:** **None — FPIES has no identified causal gene.** It is a *complex*, acquired, non-IgE-mediated gastrointestinal food allergy with multifactorial/polygenic (shared atopic) liability.

---

## Summary

Food Protein-Induced Enterocolitis Syndrome (FPIES) is a **non-IgE-mediated gastrointestinal food allergy** that, despite its placement in this genetic-disease research template, **has no causal gene, no OMIM Mendelian entry, and no ClinVar monogenic variant**. The "Causal gene(s): not recorded" field in the template is correct and not an omission: FPIES is classified as **Complex**, and its liability is best understood as **multifactorial/polygenic** — a shared atopic predisposition interacting with dietary allergen exposure and early-life gut microbial dysbiosis. The first paragraph of this report therefore names *no gene*, by design and by evidence. The reader researching MONDO:0100008 should expect an immunologic/environmental disease, not a single-gene disorder.

Clinically, FPIES presents in **infancy** (median age at diagnosis ~6–7 months) with **delayed (1–4 h), profuse, repetitive projectile vomiting**, frequently accompanied by **lethargy and pallor**, and in ~15–20% of severe acute cases progressing to **hypovolemic/distributive shock**. Common triggers vary geographically (cow's milk globally; grains/rice/oat in the US and Australia; fish in Europe; hen's egg in Japan; seafood in adults). The disease is a **clinical diagnosis** anchored on the **2017 First International Consensus Guidelines**, with **oral food challenge (OFC)** as the diagnostic reference standard. There is **no validated biomarker** and genetic testing is not indicated. Prognosis is favorable for most children (~90% resolve by age 3 for cow's milk FPIES), but is poor for fish/seafood, adult-onset (female-predominant), and IgE-sensitized "atypical" phenotypes.

Mechanistically, acute FPIES reactions are driven by **systemic innate immune activation** rather than antigen-specific IgE or classical T-cell immunity. During reactions, patients show **pan-leukocyte activation and cytokine release**, an **IL-17 inflammatory signature**, elevation of the mucosal-damage marker **REG1A**, and activation of a **purinergic → enterochromaffin-cell serotonin axis** that mechanistically explains the emesis and the efficacy of the 5-HT3 antagonist **ondansetron**. The pivotal unresolved question is how the food antigen is recognized to trigger this innate cascade. Management is **strict trigger avoidance** plus **acute supportive care** (IV fluid resuscitation, ondansetron, ± corticosteroids); epinephrine is *not* indicated unless concurrent IgE-mediated symptoms are present. No gene, cell, RNA, biologic, or targeted disease-modifying therapy exists.

---

## Key Findings

### Finding 1 — FPIES is a non-IgE-mediated GI food allergy with no known causal gene (F001)

FPIES (MONDO:0100008; ICD-10 K52.21) is characterized by **delayed, repetitive projectile vomiting 1–4 hours after ingesting a culprit food**, often with pallor and lethargy. In approximately **15–20% of severe acute reactions**, patients progress to hypovolemic or distributive shock. It is a **clinical diagnosis with NO validated biomarker and NO identified causal gene**. Notably, the first dedicated ICD-10 code appeared only recently, and the first international consensus guidelines were published in 2017. Acute, chronic, adult-onset, and atypical (IgE-sensitized) subtypes are recognized.

> "Food protein-induced enterocolitis syndrome (FPIES) is a non-IgE-mediated gastrointestinal food allergy characterized by delayed, protracted vomiting and accompanied by lethargy and pallor, usually 1 to 4 hours after ingesting the food allergen. The pathophysiology of FPIES remains unknown, and currently there are no diagnostic biomarkers available" — [PMID: 39521282](https://pubmed.ncbi.nlm.nih.gov/39521282/)

> "In ∼15-20% of severe cases, patients go into hypovolemic or distributive shock" — [PMID: 39022754](https://pubmed.ncbi.nlm.nih.gov/39022754/)

**Evidence source:** Human clinical / consensus review.

### Finding 2 — Pathophysiology: systemic innate immune activation and neuroimmune pathways, not antigen-specific IgE/humoral immunity (F002)

Peripheral-blood studies **fail to show antigen-specific humoral or cellular (T-cell) immunity** underlying reactivity. Instead, reactions feature **robust systemic innate immune activation** (pan-leukocyte activation, cytokine release), **increased gastrointestinal permeability**, and activation of **neuroendocrine/autonomic** pathways. Acute reactions typically show neutrophilia and thrombocytosis **without fever or significant CRP rise** — a key feature distinguishing FPIES from sepsis. The mechanism of food-specific antigen recognition remains unknown.

> "Studies of peripheral blood fail to exhibit evidence of antigen-specific humoral or cellular immunity underlying clinical reactivity to foods in FPIES. However, growing evidence suggests a robust systemic innate immune activation occurring during FPIES reactions and the activation of neuroendocrine pathways." — [PMID: 33548465](https://pubmed.ncbi.nlm.nih.gov/33548465/)

> "studies show pan-leukocyte activation, cytokine release, and increased gastrointestinal permeability" — [PMID: 35522370](https://pubmed.ncbi.nlm.nih.gov/35522370/)

> "a lack of a significant rise in C-reactive protein at presentation" — [PMID: 30656696](https://pubmed.ncbi.nlm.nih.gov/30656696/)

**Evidence source:** Human clinical / mechanistic review.

### Finding 3 — Epidemiology, triggers, and natural history: infant-onset, resolves by school age, geographically variable triggers (F003)

Prevalence is estimated at **0.015–0.7%** in children; US estimates are **0.51–0.9% of children and 0.22% of adults**. Most patients present in infancy (median age at diagnosis ~7 months). Trigger foods vary by geography:

| Region | Predominant trigger(s) |
|--------|------------------------|
| Global | Cow's milk |
| US / Australia | Grains (rice, oat) |
| Europe | Fish |
| Japan | Hen's egg |
| Adults (any region) | Seafood / shellfish (female-predominant, prolonged course) |

Most children acquire tolerance before school age. In a Swiss prospective cohort, median resolution ages were **cow's milk 1.6 y, hen's egg 4 y, meat 4.8 y, fish 10 y**, with acute FPIES overall resolving at a median of 4.8 years and chronic FPIES at ~11 months. Fish/seafood FPIES resolves poorly. Rising egg and peanut FPIES incidence correlating with early-allergen-introduction guidelines suggests an infancy "window of susceptibility."

> "FPIES is a relatively rare disease, with a prevalence of 0.015%-0.7%" — [PMID: 36653144](https://pubmed.ncbi.nlm.nih.gov/36653144/)

> "FPIES is estimated to affect 0.51-0.9% of children and 0.22% of adults in the United States" — [PMID: 39022754](https://pubmed.ncbi.nlm.nih.gov/39022754/)

> "Cow's milk is a major trigger globally, and other notable triggers including grains in the United States and Australia, fish in Europe, and hen's egg in Japan" — [PMID: 40976417](https://pubmed.ncbi.nlm.nih.gov/40976417/)

> "a median age of resolution of 11 months in children with chronic FPIES, and 4.8 years in children with acute FPIES with great variety across different foods (1.6 years for cow's milk, 4 years for hen's egg, 4.8 years for meat, and 10 years for fish)" — [PMID: 41524093](https://pubmed.ncbi.nlm.nih.gov/41524093/)

**Evidence source:** Human clinical / population cohorts.

### Finding 4 — Management: allergen avoidance plus acute rehydration and ondansetron; diagnosis via clinical criteria and supervised OFC (F004)

Diagnosis rests on the **2017 international consensus clinical criteria**; **OFC is the diagnostic reference standard**, with emerging **low-dose protocols (25–33% of an age-appropriate serving)** sufficient to provoke symptoms while reducing severity. Acute reactions are treated with **IV fluid resuscitation (10 mL/kg boluses)** and the 5-HT3 antagonist **ondansetron** (oral/sublingual for mild–moderate; IV for severe); corticosteroids are added in severe cases. **Adrenaline/epinephrine is NOT indicated** unless concurrent IgE symptoms are present. **Granisetron** (another 5-HT3 antagonist) shows efficacy in case series. Long-term management is strict trigger elimination with periodic OFC to confirm tolerance, with dietitian support to prevent nutritional deficiency.

> "Emerging literature supports the safety and effectiveness of low-dose OFC protocols, with evidence indicating that administering 25% to 33% of an age-appropriate serving size can provoke symptoms in most individuals with persistent FPIES while reducing reaction severity. Furthermore, evidence suggests that the antiemetic ondansetron can ameliorate FPIES symptoms" — [PMID: 41076074](https://pubmed.ncbi.nlm.nih.gov/41076074/)

> "According to severity, acute reactions require prompt rehydration and ondansetron. Oral or sublingual ondansetron, effective for mild to moderate reactions, can limit dehydration and hospital transfers" — [PMID: 42473072](https://pubmed.ncbi.nlm.nih.gov/42473072/)

> "Vomiting ceased within an hour after granisetron administration in all cases, allowing successful oral rehydration" — [PMID: 41220525](https://pubmed.ncbi.nlm.nih.gov/41220525/)

**NCIT term suggestions:** Ondansetron (NCIT:C1157), Corticosteroid therapy, Intravenous fluid replacement, Dietary/elimination therapy.

**Evidence source:** Human clinical / guidelines.

### Finding 5 — Clinical phenotype, trigger distribution, and elevated atopic comorbidity (shared atopic predisposition) (F005)

The CHOP referral population (n=462) found **milk (67%), soy (41%), rice (19%), oat (16%), egg (11%)** as top triggers; 70% of patients reacted to only 1–2 foods; onset was ~7 months for milk/soy vs ~12 months for solids; skin-prick and atopy patch testing were unhelpful. A birth cohort (n=158,510; 214 FPIES) found incidence 0.17–0.42%, 78% acute presentation, mean diagnosis age 6.8 months, and **significantly elevated atopic comorbidity** vs controls:

| Comorbidity | FPIES | Controls | p |
|-------------|-------|----------|---|
| Atopic dermatitis | 20.6% | 11.7% | <.001 |
| IgE-mediated food allergy | 23.8% | 4.0% | <.001 |
| Asthma | 26.6% | 18.4% | <.001 |
| Allergic rhinitis | 28.0% | 16.7% | <.001 |

Importantly, longitudinal analysis did **not** support causation — the atopy–FPIES link reflects a **shared predisposition**, not a causal cascade. An Asian American cohort showed 55.5% with atopic dermatitis, median diagnosis 7 months, 23.9% multi-food, and 14.4% atypical FPIES.

> "The most common foods identified were milk (67%), soy (41%), rice (19%), oat (16%), and egg (11%)" — [PMID: 24565539](https://pubmed.ncbi.nlm.nih.gov/24565539/)

> "Atopic comorbidity was higher in patients with FPIES compared with healthy children (AD, 20.6% vs 11.7%; IgE-FA, 23.8% vs 4.0%; asthma, 26.6% vs 18.4%; AR, 28.0% vs 16.7%; P < .001" — [PMID: 31759160](https://pubmed.ncbi.nlm.nih.gov/31759160/)

> "longitudinal analysis does not support direct causation as the etiology of these associations. Rather it suggests a shared predisposition to both types of allergy" — [PMID: 31759160](https://pubmed.ncbi.nlm.nih.gov/31759160/)

**Evidence source:** Human clinical / large cohorts.

### Finding 6 — Differential diagnosis: mimics sepsis/gastroenteritis and neonatal necrotizing enterocolitis (NEC) (F006)

FPIES is frequently misdiagnosed as **sepsis or gastroenteritis**; it is favored by **rapid symptom resolution within hours**, **absence of fever**, and **lack of significant CRP rise**. In neonates, FPIES mimics **NEC**: in a NICU series, **6.7% of preterm and 44.7% of term infants** with presumed NEC were actually FPIES. Distinguishing features in term infants (P<.05): hematochezia, shock, leukocytosis, peripheral eosinophilia, and response to extensively hydrolyzed/elemental formula. Pneumatosis intestinalis can rarely occur in FPIES (more common in preterm FPIES 44.4% vs NEC 21.6%), overlapping with NEC radiology. Early-onset neonatal FPIES may represent a distinct entity.

> "FPIES is often misdiagnosed as sepsis or gastroenteritis. However, a diagnosis of FPIES is favoured if there is rapid resolution of symptoms within hours of presentation, an absence of fever, and a lack of a significant rise in C-reactive protein at presentation" — [PMID: 30656696](https://pubmed.ncbi.nlm.nih.gov/30656696/)

> "A total of 10 of 150 (6.7%) preterm and 17 of 38 (44.7%) term infants with presumed NEC were confirmed to have FPIES" — [PMID: 34626783](https://pubmed.ncbi.nlm.nih.gov/34626783/)

> "Symptoms such as hematochezia, shock, leukocytosis, peripheral eosinophilia, and feeding of extensively hydrolyzed milk formula or elemental formula after discharge were significantly different between the 2 groups in term infants" — [PMID: 34626783](https://pubmed.ncbi.nlm.nih.gov/34626783/)

**Evidence source:** Human clinical / NICU case series.

### Finding 7 — FPIES is associated with gut microbial dysbiosis (F007)

Multiple independent 16S/shotgun studies show **gut dysbiosis** in FPIES infants vs controls. At diagnosis (n=56 FPIES vs 43 controls), age was the strongest determinant followed by FPIES status; β-diversity differed (P<.01); FPIES had **lower Bifidobacterium** and **higher Bacteroides, Haemophilus, Veillonella**, with reduced Verrucomicrobiota. Cow's-milk FPIES (n=12) showed **enterobacteria enrichment** and increased fecal fatty-acid excretion. A longitudinal cohort (n=38) found lower gut/salivary alpha-diversity, less Ruminococcus, higher acetate; tolerance acquisition partially normalized diversity and SCFAs (more Blautia, Ruminococcus, Faecalibacterium, Prevotella-9; less Escherichia-Shigella). Another cohort found lower Bifidobacterium and higher hexanoic acid, with EHF vs AAF formulas differentially shaping microbiota/SCFAs.

> "Children with FPIES had lower Bifidobacterium and higher abundances of Bacteroides, Haemophilus, and Veillonella. FPIES food triggers were associated with reduced Verrucomicrobiota abundance" — [PMID: 41825597](https://pubmed.ncbi.nlm.nih.gov/41825597/)

> "A specific pattern of microbiota in the gut of CM FPIES patients was found, characterized by a high abundance of enterobacteria. Also, an intense excretion of FAs in the feces of these infants was observed" — [PMID: 39175183](https://pubmed.ncbi.nlm.nih.gov/39175183/)

> "Allergic patients exhibited lower gut and salivary alpha-diversities, and several different genera (12 in stools, including less Ruminococcus, and 2 in saliva), and higher relative abundance of acetate than the controls. With tolerance acquisition, faecal alpha-diversities partially increased, whereas SCFAs normalised" — [PMID: 42050666](https://pubmed.ncbi.nlm.nih.gov/42050666/)

**Evidence source:** Human clinical / microbiome cohorts.

### Finding 8 — Mechanism: IL-17/innate cytokine signature, REG1A mucosal-damage marker, and purinergic→serotonin axis driving emesis (F008)

During supervised OFCs, **symptomatic** FPIES reactions (not asymptomatic/outgrown challenges) show three linked molecular features:

1. **Systemic innate immune activation** with TNF-α–producing cells, without detectable antigen-specific antibody/T-cell response (CyTOF/RNAseq; [PMID: 28192147](https://pubmed.ncbi.nlm.nih.gov/28192147/)).
2. An **IL-17 inflammatory signature**: significant elevation of IL-17A, IL-22, IL-17C, CCL20, plus IL-2, and innate markers IL-8, oncostatin M, leukemia inhibitory factor, TNF-α, IL-10, IL-6; the mucosal-damage marker **REG1A** (regenerating family member 1 alpha) is significantly increased ([PMID: 33891982](https://pubmed.ncbi.nlm.nih.gov/33891982/)).
3. A **purinergic → serotonin axis**: untargeted serum metabolomics (10 FPIES vs 10 asymptomatic) found 34 metabolites elevated during reactions including **inosine and urate** (purine pathway); purine receptors P2RX7, P2RY10 and ectonucleotidase CD73 were reduced in blood after reaction; the serotonin metabolite **5-hydroxyindoleacetate (5-HIAA)** was significantly elevated; and *in vitro*, **adenosine stimulation of human gastric/duodenal biopsies induced serotonin release** ([PMID: 36306938](https://pubmed.ncbi.nlm.nih.gov/36306938/)).

> "Our data demonstrate a compelling role of systemic innate immune activation in adverse reactions elicited by foods in FPIES. Further investigation is needed to identify the mechanism of antigen specificity" — [PMID: 28192147](https://pubmed.ncbi.nlm.nih.gov/28192147/)

> "associated with significant elevation of levels of cytokines and chemokines, including IL-17 family markers (IL-17A, IL-22, IL-17C, and CCL20) and T-cell activation (IL-2), and innate inflammatory markers (IL-8, oncostatin M, leukemia inhibitory factor, TNF-α, IL-10, and IL-6). The level of the mucosal damage marker regenerating family member 1 alpha (REG1A) was also significantly increased" — [PMID: 33891982](https://pubmed.ncbi.nlm.nih.gov/33891982/)

> "The level of the serotonin metabolite 5-hydroxyindoleacetate was significantly elevated after reaction. Adenosine stimulation of gastric and duodenal biopsy specimens from FPIES-free donors induced a significant release of serotonin, suggesting a link between purinergic pathway" — [PMID: 36306938](https://pubmed.ncbi.nlm.nih.gov/36306938/)

**Evidence source:** Human clinical (OFC-timed) + ex vivo human biopsy.

### Finding 9 — Symptom frequencies, natural history/prognosis, and distinct adult (seafood, female-predominant) phenotype (F009)

The landmark population-based prospective study (Katz 2011, n=13,019 infants) found a **cow's-milk FPIES cumulative incidence of 0.34% by age 1** (vs 0.5% for IgE-CMA). Symptom frequencies: **recurrent vomiting 100%, lethargy 77%, diarrhea 25%, pallor 14%, bloody diarrhea 4.5%**; ALL onset was within the first 6 months; **90% recovered by age 3**. Resolution ages (Caubet 2014, n=160): rice 4.7 y, oat 4 y, soy 6.7 y, milk 5.1 y (sIgE-negative). Detectable food-specific IgE ("atypical" FPIES) predicts delayed/absent resolution — 41% of milk-sIgE+ patients switched to an IgE-mediated phenotype, and **none** became milk-tolerant during the study. Adult FPIES (González-Delgado 2022, n=107, **93.5% female**, median follow-up 6.2 y): abdominal pain 96.3%, diarrhea 72%, vomiting 60.7%; triggers seafood 59.8%, egg 14%, milk 10.3%; only 16.8% achieved tolerance (median 3.5 y), with elevated comorbid IBS, eosinophilic esophagitis, IBD, and celiac disease.

> "The cumulative incidence for FPIES was 0.34% (44/13,019 patients). The most common symptoms were recurrent vomiting (100%), lethargy (77%) diarrhea (25%), pallor (14%), and bloody diarrhea (4.5%). All patients had FPIES within the first 6 months of life. By the age of 3 years, 90% of the patients had recovered" — [PMID: 21377033](https://pubmed.ncbi.nlm.nih.gov/21377033/)

> "The median age when tolerance was established was 4.7 years for rice, 4 years for oat, and 6.7 years for soy. Median age when milk tolerance was established for subjects with undetectable milk-specific IgE levels was 5.1 years, whereas none of the subjects with detectable milk-specific IgE became tolerant to milk" — [PMID: 24880634](https://pubmed.ncbi.nlm.nih.gov/24880634/)

> "One hundred and seven adults with FPIES (93.5% female) were followed for a median of 6.2 years. Abdominal pain was the most common manifestation (96.3%), followed by diarrhea (72%) and vomiting (60.7%). Seafood (59.8%), egg (14%), and milk (10.3%) were the most common triggers" — [PMID: 35598865](https://pubmed.ncbi.nlm.nih.gov/35598865/)

**Evidence source:** Human clinical / prospective + retrospective cohorts.

### Finding 10 — FPIES is clinically diagnosed, has no causal gene/biomarker/animal model, and no disease-modifying therapy (F010)

Diagnosis is clinical per the **2017 First International Consensus Guidelines**; OFC is the reference standard; there are **no diagnostic biomarkers** and genetic testing is not indicated. The first dedicated ICD-10 code (K52.21) appeared ~40 years after the initial description. No OMIM/ClinVar monogenic entry exists — FPIES is a complex, non-Mendelian, non-IgE food allergy with multifactorial/polygenic (shared atopic) liability. Targeted literature searches found **no validated animal/organoid model**; mechanism is studied in human subjects during OFC and in ex vivo human gut biopsies. Management is strict trigger avoidance plus acute supportive care; **no gene, cell, RNA, biologic, or targeted therapy is approved.**

> "Forty years after the initial FPIES description, the first FPIES code appeared in the International Classification of Diseases, Tenth Revision (ICD-10), and the first international consensus guidelines for the diagnosis and management of FPIES were published" — [PMID: 39521282](https://pubmed.ncbi.nlm.nih.gov/39521282/)

> "The pathophysiology of FPIES remains unknown, and currently there are no diagnostic biomarkers available to assess disease activity or its resolution" — [PMID: 39521282](https://pubmed.ncbi.nlm.nih.gov/39521282/)

> "Currently, no validated biomarker is available for diagnosis, and the mechanisms related to gastrointestinal manifestations and immune system involved in the development of FPIES have not yet been elucidated" — [PMID: 36653144](https://pubmed.ncbi.nlm.nih.gov/36653144/)

**Evidence source:** Human clinical / consensus review.

---

## Report by Template Section

### 1. Disease Information

FPIES is a **non-IgE-mediated gastrointestinal food allergy** characterized by delayed, protracted vomiting with lethargy and pallor, usually 1–4 hours after ingesting a culprit food. **Identifiers:** MONDO:0100008; ICD-10 **K52.21**; MeSH "Food Protein-Induced Enterocolitis Syndrome." **No OMIM entry** (not a Mendelian disorder). Orphanet lists FPIES among non-IgE-mediated food allergies. **Synonyms:** FPIES; food protein-induced enterocolitis syndrome. **Subtypes:** acute FPIES (children), chronic FPIES, acute FPIES (adults), and early-onset neonatal FPIES. Information is derived from **aggregated disease-level resources** (consensus guidelines, cohort studies) as well as individual-patient EHR cohorts (e.g., ICD-10 K52.21-coded retrospective studies).

### 2. Etiology

**Causal factors:** FPIES is **not genetic in a Mendelian sense** and has **no identified causal gene**. The primary driver is **immunologic (innate) reactivity to dietary food proteins** (cow's milk, soy, grains, egg, fish/seafood). Contributing factors include **early-life gut microbial dysbiosis** (Finding 7) and a **shared atopic predisposition** (Finding 5).

- **Genetic risk factors:** None confirmed; no GWAS Catalog susceptibility loci, no ClinVar pathogenic variants. Liability is inferred to be **polygenic/multifactorial**, overlapping with general atopy.
- **Environmental risk factors:** Dietary allergen exposure is necessary; **age (infancy)** and **timing of allergen introduction** modulate risk — early introduction of egg/peanut correlates with rising FPIES of those foods, suggesting an infancy "window of susceptibility." Female sex predominates in **adult** FPIES.
- **Protective factors:** No validated genetic protective alleles. Breastfeeding appears protective in that FPIES to proteins in maternal breast milk is rare. Tolerance acquisition is associated with **normalization of gut microbiota/SCFAs** (Finding 7).
- **Gene–environment interactions:** Best framed as **host (atopic/innate-immune) predisposition × dietary antigen × gut microbiome**; no specific GxE locus identified.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Frequency / characteristics |
|-----------|------|----------------|------------------------------|
| Delayed repetitive vomiting (1–4 h post-ingestion) | Symptom | HP:0002013 (Vomiting) | ~100% (acute); defining feature |
| Lethargy | Clinical sign | HP:0001254 (Lethargy) | ~77% |
| Pallor | Clinical sign | HP:0000980 (Pallor) | ~14% |
| Diarrhea | Symptom | HP:0002014 (Diarrhea) | ~25% (children); ~72% (adults) |
| Bloody stools / hematochezia | Clinical sign | HP:0002573 (Hematochezia) | ~4.5% |
| Hypovolemic/distributive shock | Clinical sign | HP:0031273 (Shock) | ~15–20% of severe acute |
| Dehydration | Clinical sign | HP:0001944 (Dehydration) | Common in severe reactions |
| Failure to thrive (chronic FPIES) | Physical manifestation | HP:0001508 (Failure to thrive) | Chronic subtype |
| Leukocytosis / neutrophilia | Lab abnormality | HP:0001974 (Leukocytosis) | Acute reactions |
| Thrombocytosis | Lab abnormality | HP:0001894 (Thrombocytosis) | Acute reactions |
| Peripheral eosinophilia | Lab abnormality | HP:0001880 (Eosinophilia) | Subset |
| Abdominal pain (adults) | Symptom | HP:0002027 (Abdominal pain) | ~96% of adults |
| Metabolic acidosis | Lab abnormality | HP:0001942 (Metabolic acidosis) | Severe reactions |

**Onset:** Neonatal–infantile (median diagnosis ~6–7 months for children); adult-onset variant exists. **Severity:** variable (mild–severe/shock). **Progression:** episodic (reaction-triggered), self-limiting in most children. **QoL impact:** significant caregiver anxiety, dietary restriction, risk of nutritional deficiency; adult FPIES has prolonged course with comorbid functional GI disorders.

### 4. Genetic / Molecular Information

- **Causal genes:** **None.** No monogenic cause; no OMIM/ClinVar entry.
- **Pathogenic variants:** Not applicable — no established pathogenic/likely-pathogenic/VUS variants per ACMG/AMP. No allele-frequency data (gnomAD) relevant. No somatic/germline distinction applies.
- **Modifier genes:** None validated. **Food-specific IgE sensitization status** (not a gene) is the key molecular modifier of prognosis ("atypical" FPIES, Finding 9).
- **Epigenetic information:** No FPIES-specific DNA methylation/histone studies identified.
- **Chromosomal abnormalities:** None associated.

*Molecular markers of disease activity* (not germline genetics): **REG1A** (mucosal damage), **IL-17A/IL-22/IL-17C/CCL20** (inflammatory signature), **5-HIAA** (serotonin metabolite), purine metabolites (inosine, urate), and purinergic receptors **P2RX7, P2RY10, NT5E/CD73** — all altered during acute reactions (Finding 8).

### 5. Environmental Information

- **Environmental factors:** Dietary food proteins are the essential trigger — cow's milk, soy, rice, oat, egg, fish/shellfish. No toxin/radiation/pollution role.
- **Lifestyle factors:** Infant feeding practices and **timing of solid/allergen introduction** modulate incidence.
- **Infectious agents:** No pathogen causes FPIES. However, **gut microbial dysbiosis** (reduced Bifidobacterium, enterobacteria enrichment) is mechanistically implicated as a contributing/permissive factor (Finding 7). FPIES is frequently *misdiagnosed* as infectious gastroenteritis or sepsis.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating exposure → clinical manifestation):**

1. **Dietary food protein ingestion** in a predisposed infant (atopic/innate-immune susceptibility, often with gut dysbiosis) → *leads to* antigen presentation at the intestinal mucosa. *(Antigen-recognition step is INFERRED/UNKNOWN — the key mechanistic gap.)*
2. Food antigen recognition → *triggers* **systemic innate immune activation** (pan-leukocyte activation, TNF-α–producing cells) rather than antigen-specific IgE or classical adaptive T-cell responses. *(Demonstrated: CyTOF/RNAseq, PMID 28192147.)*
3. Innate activation → *results in* an **IL-17 family cytokine surge** (IL-17A, IL-22, IL-17C, CCL20) plus IL-8, oncostatin M, LIF, TNF-α, IL-6, IL-10. *(Demonstrated: PMID 33891982.)*
4. Mucosal inflammation → *causes* **intestinal epithelial injury**, marked by elevated **REG1A** and **increased gut permeability**. *(Demonstrated.)*
5. Tissue injury releases **purine metabolites** (ATP/adenosine → inosine, urate); purinergic signaling → *stimulates* **enterochromaffin cells** to release **serotonin (5-HT)**. *(Demonstrated ex vivo: adenosine induces serotonin release from human gut biopsies; 5-HIAA elevated in serum, PMID 36306938.)*
6. Serotonin acting on **5-HT3 receptors** (vagal/enteric afferents and area postrema) → *drives* **delayed, repetitive vomiting**; branch: autonomic/neuroendocrine activation → *produces* **lethargy, pallor, hypotension/shock**. *(Mechanistically consistent with ondansetron efficacy — a 5-HT3 antagonist.)*
7. Fluid loss + distributive component → *leads to* **hypovolemic/distributive shock** in ~15–20% of severe cases.

```
Food protein  ──(unknown antigen recognition)──►  Systemic INNATE immune activation
                                                        │
                                                        ▼
                               IL-17/IL-22/IL-8/TNF-α cytokine surge
                                                        │
                                                        ▼
                     Epithelial injury (REG1A↑, ↑permeability)
                                                        │
                                   ┌────────────────────┴───────────────────┐
                                   ▼                                        ▼
                 Purine release (ATP→adenosine)              Autonomic/neuroendocrine
                                   │                              activation
                                   ▼                                        │
              Enterochromaffin serotonin (5-HT) release                     │
                                   │                                        │
                                   ▼                                        ▼
                      5-HT3 → DELAYED VOMITING          Lethargy, pallor, hypotension → SHOCK
                      (blocked by ondansetron)
```

- **Molecular pathways:** IL-17/Th17-associated cytokine signaling; **purinergic signaling (P2X7/P2Y receptors, adenosine/CD73)**; serotonergic (5-HT3) neuroimmune signaling.
- **Cellular processes:** Innate inflammation; pan-leukocyte activation; epithelial damage/regeneration (REG1A); enterochromaffin cell secretion.
- **Immune involvement:** Innate immune activation **without** antigen-specific IgE or demonstrable adaptive T-cell specificity — the antigen-recognition mechanism is the central unsolved question.
- **Tissue damage mechanisms:** Mucosal inflammation and increased GI permeability.
- **GO term suggestions:** GO:0045087 (innate immune response), GO:0032620 (IL-17 production), GO:0006954 (inflammatory response), GO:0023052 (signaling), GO:0001820 (serotonin secretion).
- **CL term suggestions:** CL:0000775 (neutrophil), CL:0000235 (macrophage), CL:0000084 (T cell — not antigen-specific), CL:0000548 (enteroendocrine/enterochromaffin cell), CL:0002254 (intestinal epithelial cell).

### 7. Anatomical Structures Affected

- **Primary organs:** **Small and large intestine** (UBERON:0000160 intestine; UBERON:0002108 small intestine; UBERON:0001155 colon); **stomach** (UBERON:0000945) for vomiting reflex. Body system: **digestive system** (UBERON:0001007).
- **Secondary involvement:** **Cardiovascular/circulatory** (shock, hypotension), **hematopoietic** (neutrophilia, thrombocytosis, methemoglobinemia), **autonomic nervous system** (neuroimmune component).
- **Tissue/cell level:** Intestinal **epithelium** (UBERON:0001277 intestinal mucosa); **enterochromaffin/enteroendocrine cells** (CL:0000548); infiltrating **leukocytes** (neutrophils, eosinophils).
- **Subcellular level:** No specific organelle defect; secretory granules of enterochromaffin cells (serotonin release) and cytokine-secretory machinery are functionally relevant. GO:0005615 (extracellular space — cytokine/serotonin).
- **Localization:** GI tract, bilateral/diffuse (not lateralized).

### 8. Temporal Development

- **Onset:** Pediatric/infantile; **all onset within first 6 months** for cow's-milk FPIES (Katz 2011); solids-triggered FPIES onset ~later in first year; adult-onset variant exists. Onset pattern: **acute** (reaction-bound) or **chronic** (continuous exposure → failure to thrive).
- **Progression:** **Episodic**, reaction-triggered; not progressive. Self-limited in most children.
- **Duration/resolution:** ~90% of cow's-milk FPIES resolve by age 3; trigger-specific resolution ages (rice 4.7 y, oat 4 y, soy 6.7 y, milk 5.1 y if sIgE-negative; fish ~10 y). **Atypical (sIgE+)** and **adult/seafood** FPIES resolve poorly (adults: only ~16.8% tolerant, median 3.5 y).
- **Patterns:** Spontaneous remission (tolerance) is the norm in children; treatment-induced remission not applicable. **Critical period:** infancy "window of susceptibility" tied to allergen introduction timing.

### 9. Inheritance and Population

- **Epidemiology:** Prevalence 0.015–0.7% (children); US 0.51–0.9% children, 0.22% adults. Cow's-milk FPIES cumulative incidence 0.34% by age 1 (Israel).
- **Inheritance:** **Not Mendelian.** Multifactorial/polygenic liability (shared atopic predisposition). No penetrance/expressivity/anticipation/mosaicism/founder-effect/carrier-frequency parameters apply (no causal gene).
- **Demographics:** Infants of both sexes in childhood (slight male predominance in some cohorts, e.g., 52% male Asian American cohort). **Adults: strongly female (93.5%).** Geographic variation in triggers (Finding 3). Atopic comorbidity elevated.

### 10. Diagnostics

- **Clinical tests:** No specific lab test; supportive findings during acute reaction include **neutrophilia, thrombocytosis, metabolic acidosis, methemoglobinemia, peripheral eosinophilia**, and notably **no CRP rise / no fever** (distinguishes from sepsis). Skin-prick and atopy patch testing are **unhelpful** for diagnosis. Allergen-specific lymphocyte stimulation test (ALST) shows only modest accuracy for egg-yolk FPIES (AUC 0.68).
- **Biomarkers:** **None validated.** Research markers (REG1A, IL-17 panel, 5-HIAA) are not clinical tests.
- **Imaging:** Non-specific; may show pneumatosis intestinalis (overlapping with NEC).
- **Biopsy:** Not required for diagnosis; shows non-specific inflammation.
- **Genetic testing:** **Not indicated** (no causal gene). WGS/WES/panels/CMA/karyotype/FISH/mtDNA/repeat-expansion testing all **not applicable**.
- **Clinical criteria:** **2017 First International Consensus Guidelines**; **OFC is the diagnostic reference standard** (low-dose protocols emerging).
- **Differential diagnosis:** Sepsis, acute gastroenteritis, **necrotizing enterocolitis** (neonates), IgE-mediated food allergy/anaphylaxis, metabolic disorders, surgical abdomen. Distinguished by rapid resolution, afebrility, normal CRP, and reproducibility on re-exposure.
- **Screening:** No population or newborn screening; cascade/carrier screening not applicable.

### 11. Outcome / Prognosis

- **Survival/mortality:** Generally **excellent survival**; FPIES is not typically fatal with appropriate supportive care, though severe reactions can cause life-threatening shock. No disease-specific mortality rate established.
- **Morbidity/function:** Acute dehydration/shock morbidity; chronic FPIES → failure to thrive; nutritional/dietary burden; caregiver QoL impact.
- **Disease course:** Most children acquire tolerance (90% cow's-milk by age 3). **Poor-prognosis groups:** fish/seafood, adult-onset (female), and **IgE-sensitized "atypical" FPIES** (may convert to IgE-mediated allergy; milk-sIgE+ rarely tolerize).
- **Prognostic factors:** Trigger food (fish/seafood worst), **food-specific IgE positivity** (adverse), multiple-food FPIES, family history of allergy, male sex + diagnostic delay (→ multiple food allergies). Adult onset predicts prolonged course.

### 12. Treatment

- **Pharmacotherapy:** **Ondansetron** (5-HT3 antagonist; oral/sublingual for mild–moderate, IV for severe) — first-line adjunct; **granisetron** as alternative; **IV corticosteroids** in severe reactions; **IV fluid resuscitation** (10 mL/kg boluses) is the cornerstone of acute management. **Epinephrine NOT indicated** unless concurrent IgE symptoms.
- **Pharmacogenomics:** Not applicable.
- **Advanced therapeutics (gene/cell/RNA/targeted/immunotherapy):** **None approved or in trials** for FPIES.
- **Surgical/interventional:** None (surgery only to exclude differentials).
- **Supportive/rehabilitative:** Strict **trigger-food elimination**; dietitian-guided nutrition; formula choice (extensively hydrolyzed vs amino-acid-based) in infants.
- **Experimental:** No targeted disease-modifying agents; research focuses on low-dose OFC protocols and biomarker discovery.
- **Treatment strategy:** Avoidance + emergency action plan (oral rehydration solution + ondansetron) + periodic supervised OFC to confirm tolerance.
- **NCIT suggestions:** Ondansetron (NCIT:C1157), Corticosteroid, Intravenous Fluid, Dietary Intervention, Granisetron (NCIT:C1096).

### 13. Prevention

- **Primary prevention:** No vaccine/drug. Avoidance of known triggers in diagnosed patients; awareness of FPIES risk during early allergen introduction (but early introduction should **not** be abandoned — peanut FPIES is rare at 0.3% and mostly resolves).
- **Secondary prevention:** Early recognition to prevent misdiagnosis (sepsis/NEC) and unnecessary workup; emergency action plans.
- **Tertiary prevention:** Nutritional monitoring; supervised reintroduction to prevent prolonged unnecessary elimination.
- **Immunization/public health/environmental:** Not applicable.
- **Counseling:** Caregiver education and dietary counseling (not genetic counseling — no heritable gene).

### 14. Other Species / Natural Disease

- **Taxonomy:** Human disease (NCBI Taxon:9606). **No naturally occurring animal homolog** documented in OMIA. Cow's-milk protein intolerance/allergy phenomena exist in other species but a direct FPIES analog is **not established**.
- **Orthologous genes:** Not applicable (no causal gene).
- **Comparative/veterinary relevance:** Not established.
- **Zoonotic/transmission:** Not applicable (non-infectious).

### 15. Model Organisms

- **No validated animal, organoid, or iPSC model of FPIES exists.** Mechanistic research is conducted **in human subjects during supervised OFCs** and in **ex vivo human gastric/duodenal biopsies** (e.g., adenosine-induced serotonin release). This absence of a tractable model is a major barrier to mechanistic dissection and therapeutic development.

---

## Mechanistic Model / Interpretation

FPIES is best understood as a **food-antigen–triggered innate immune and neuroimmune reflex disorder of the gut**, superimposed on a predisposing host background (atopic/innate susceptibility + early-life dysbiosis). The defining and still-unsolved puzzle is **step 1 — antigen recognition**: unlike IgE-mediated allergy, no antigen-specific antibody or T cell has been demonstrated, yet reactions are exquisitely food-specific and reproducible. Downstream, the chain is comparatively well supported: innate activation → IL-17/cytokine surge → epithelial injury (REG1A) + barrier breakdown → purine release → enterochromaffin serotonin → 5-HT3-mediated emesis, with a parallel autonomic/neuroendocrine branch producing lethargy, pallor, and shock. This model is internally consistent with the two most reliable clinical observations: **ondansetron (5-HT3 antagonist) stops the vomiting**, and **CRP does not rise / no fever** (innate cytokine activation without a classic infectious acute-phase response). Gut dysbiosis (reduced Bifidobacterium, enterobacteria enrichment, altered SCFAs) likely acts upstream as a **permissive/modulatory** factor, given that tolerance acquisition partially normalizes the microbiome.

---

## Evidence Base

| PMID | Supports |
|------|----------|
| [39521282](https://pubmed.ncbi.nlm.nih.gov/39521282/) | Definition, ICD-10, 2017 guidelines, no biomarker (F001, F010) |
| [39022754](https://pubmed.ncbi.nlm.nih.gov/39022754/) | Shock rate, US prevalence (F001, F003) |
| [33548465](https://pubmed.ncbi.nlm.nih.gov/33548465/) | Innate + neuroendocrine mechanism (F002) |
| [35522370](https://pubmed.ncbi.nlm.nih.gov/35522370/) | Pan-leukocyte/cytokine, permeability (F002) |
| [30656696](https://pubmed.ncbi.nlm.nih.gov/30656696/) | No CRP rise, sepsis differential (F002, F006) |
| [36653144](https://pubmed.ncbi.nlm.nih.gov/36653144/) | Prevalence, no biomarker (F003, F010) |
| [40976417](https://pubmed.ncbi.nlm.nih.gov/40976417/) | Geographic trigger variation (F003) |
| [41524093](https://pubmed.ncbi.nlm.nih.gov/41524093/) | Trigger-specific resolution ages (F003) |
| [41076074](https://pubmed.ncbi.nlm.nih.gov/41076074/) | Low-dose OFC, ondansetron (F004) |
| [42473072](https://pubmed.ncbi.nlm.nih.gov/42473072/) | Rehydration + ondansetron (F004) |
| [41220525](https://pubmed.ncbi.nlm.nih.gov/41220525/) | Granisetron efficacy (F004) |
| [24565539](https://pubmed.ncbi.nlm.nih.gov/24565539/) | Trigger distribution (F005) |
| [31759160](https://pubmed.ncbi.nlm.nih.gov/31759160/) | Comorbidity, shared predisposition (F005) |
| [34626783](https://pubmed.ncbi.nlm.nih.gov/34626783/) | NEC differential (F006) |
| [41825597](https://pubmed.ncbi.nlm.nih.gov/41825597/) | Dysbiosis at diagnosis (F007) |
| [39175183](https://pubmed.ncbi.nlm.nih.gov/39175183/) | Enterobacteria enrichment (F007) |
| [42050666](https://pubmed.ncbi.nlm.nih.gov/42050666/) | Diversity/SCFA normalization (F007) |
| [28192147](https://pubmed.ncbi.nlm.nih.gov/28192147/) | Core innate mechanism (F008) |
| [33891982](https://pubmed.ncbi.nlm.nih.gov/33891982/) | IL-17/REG1A signature (F008) |
| [36306938](https://pubmed.ncbi.nlm.nih.gov/36306938/) | Purine→serotonin axis (F008) |
| [21377033](https://pubmed.ncbi.nlm.nih.gov/21377033/) | Incidence, symptom frequencies, recovery (F009) |
| [24880634](https://pubmed.ncbi.nlm.nih.gov/24880634/) | Resolution ages, sIgE prognosis (F009) |
| [35598865](https://pubmed.ncbi.nlm.nih.gov/35598865/) | Female-predominant adult seafood phenotype (F009) |

---

## Limitations and Knowledge Gaps

1. **Antigen-recognition mechanism is unknown** — the single largest gap. No antigen-specific antibody or T cell has been demonstrated; how food specificity is encoded by an innate response is unexplained.
2. **No validated biomarker** — diagnosis remains clinical/OFC-dependent, which is invasive and risky. REG1A, IL-17 panel, and 5-HIAA are promising but unvalidated for clinical use.
3. **No animal/organoid model** — mechanism relies on human OFC studies and ex vivo biopsies, limiting experimental manipulation.
4. **Mechanistic studies are small** (e.g., metabolomics n=10 vs 10; IL-17 study 11 vs 12), warranting replication.
5. **Heterogeneity across subtypes** (acute child, chronic, adult, early-onset neonatal) may reflect distinct pathophysiologies that current data blur together.
6. **Microbiome causality unresolved** — dysbiosis associations are correlational; whether dysbiosis is cause, consequence, or bystander is untested.
7. **No disease-modifying therapy** — all treatment is symptomatic/avoidance-based.

## Proposed Follow-up Experiments / Actions

1. **Define the antigen-recognition step:** combine single-cell multi-omics (CITE-seq/scRNA) of gut mucosa with antigen-specific innate-cell profiling (e.g., mucosal mast cells, ILC3s, γδ T cells) during OFC to test non-classical antigen sensing.
2. **Biomarker validation:** prospectively validate **REG1A, IL-17A, and 5-HIAA** (serum/stool) as diagnostic/disease-activity biomarkers across subtypes to reduce OFC reliance.
3. **Develop a model system:** establish patient-derived intestinal **organoids** co-cultured with immune cells and microbiota to recapitulate the purinergic→serotonin axis ex vivo.
4. **Test the mechanistic hypothesis therapeutically:** evaluate **P2X7/purinergic antagonists** and confirm the 5-HT3-antagonist mechanism in controlled trials.
5. **Microbiome intervention trials:** test whether **Bifidobacterium-restoring** probiotics/synbiotics accelerate tolerance.
6. **Subtype-specific natural-history registries:** characterize adult/seafood and atypical (sIgE+) FPIES to improve prognostication.
7. **Genetic/polygenic exploration:** given the shared atopic predisposition, a **GWAS or polygenic-risk-score** analysis in a large FPIES cohort could test whether any common-variant liability exists, since no Mendelian gene is expected.

---

*Report compiled from 10 confirmed findings and 40 reviewed papers across 5 investigation iterations. FPIES (MONDO:0100008) has no causal gene; this is a confirmed feature of the disease, not a gap in the research.*


## Artifacts

- [OpenScientist final report](Food_Protein-Induced_Enterocolitis_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Food_Protein-Induced_Enterocolitis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 30 |
| Quoted claims found in source | 30 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 23 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 27 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C1157` (2 mentions) - the report calls it "NCIT suggestions:** Ondansetron"; NCIT calls it **Recombinant GRO1 Protein**
- `CL:0000084` (1 mention) - the report calls it "T cell — not antigen-specific"; CL calls it **T cell**
- `CL:0000548` (2 mentions) - the report calls it "enteroendocrine/enterochromaffin cell", "enterochromaffin/enteroendocrine cells"; CL calls it **obsolete animal cell**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0000548` (obsolete animal cell) (2 mentions) - replaced by `CL:0000000`
- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `HP:0001880` (1 mention) - the report calls it "Eosinophilia"; HP calls it **Increased total eosinophil count**, and lists "Eosinophilia" among its other names
- `GO:0032620` (1 mention) - the report calls it "IL-17 production"; GO calls it **interleukin-17 production**, and lists "IL-17 production" among its other names
- `CL:0002254` (1 mention) - the report calls it "intestinal epithelial cell"; CL calls it **epithelial cell of small intestine**
- `GO:0005615` (1 mention) - the report calls it "extracellular space — cytokine/serotonin"; GO calls it **obsolete extracellular space**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000548` - called "enteroendocrine/enterochromaffin cell", "enterochromaffin/enteroendocrine cells"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.