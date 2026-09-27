---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-11T11:46:52.961398'
end_time: '2026-09-11T12:29:44.180829'
duration_seconds: 2571.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Deoxyhypusine Synthase Deficiency
  mondo_id: MONDO:0032775
  category: Genetic
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
citation_count: 9
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 15
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: GO:0008612
    reported_labels:
    - peptidyl-lysine modification to peptidyl-hypusine
    ontology_label: peptidyl-hypusine biosynthetic process
  labels_variant: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Deoxyhypusine_Synthase_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Deoxyhypusine_Synthase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Deoxyhypusine Synthase Deficiency
- **MONDO ID:** MONDO:0032775 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Deoxyhypusine Synthase Deficiency** covering all of the
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

# Deoxyhypusine Synthase (DHPS) Deficiency — Comprehensive Disease Characterization Report

**MONDO ID:** MONDO:0032775  |  **OMIM phenotype:** #618480  |  **Category:** Genetic (autosomal recessive neurodevelopmental disorder)

---

## Summary

Deoxyhypusine synthase (DHPS) deficiency is an **ultra-rare autosomal recessive neurodevelopmental disorder** caused by biallelic hypomorphic (partial loss-of-function) variants in the *DHPS* gene on chromosome 19p13.13. It is one of five recognized **"polyaminopathies"** — inborn disorders of polyamine biosynthesis/utilization — and belongs to the subgroup of **hypusination (eIF5A) disorders**. DHPS catalyzes the first and committed step in the post-translational synthesis of the unique amino acid **hypusine**, which is present in only one cellular protein, **eukaryotic translation initiation factor 5A (eIF5A)** and its homolog eIF5A2. Hypusinated eIF5A is required for the efficient translation-elongation of mRNAs containing polyproline stretches and for general control of ribosomal elongation and termination. Because complete loss of DHPS is embryonic-lethal in mice, all surviving human patients carry **partial-function allele combinations**.

The disorder was first delineated by Ganapathi et al. in 2019 (*American Journal of Human Genetics*), who described five affected individuals from four unrelated families. Remarkably, all five shared a **recurrent hypomorphic missense allele, c.518A>G (p.Asn173Ser)**, in *trans* with a near-null allele (a splice-site, in-frame deletion, or start-loss variant). The clinical picture is a **static (non-progressive) encephalopathy** dominated by global developmental delay/intellectual disability and seizures, with variable hypotonia, microcephaly, short stature, and mild facial dysmorphism. Model organisms — conditional/neuron-specific *Dhps* knockout mice and *dhps* mutant zebrafish — recapitulate the growth, cognitive, and epilepsy phenotypes, and the zebrafish model provides a circuit-level mechanism via **reduced arborization of inhibitory (GABAergic) interneurons**.

Diagnosis is molecular — via whole-exome or whole-genome sequencing — and no validated metabolite biomarker or newborn-screening assay exists. Management is currently **supportive/symptomatic** (anti-seizure medication, developmental therapies). A preclinical **AAV-based gene therapy** for DHPS syndrome was reported in 2026, representing the first disease-modifying strategy in development. Because only ~5 patients have been fully characterized, formal epidemiology, penetrance, expressivity, and natural-history data remain undefined, and much mechanistic understanding is extrapolated from model systems and the closely related aging/spermidine literature.

---

## Key Findings

### Finding 1 — DHPS deficiency is an autosomal recessive neurodevelopmental disorder caused by biallelic hypomorphic *DHPS* variants

Ganapathi et al. (2019) identified rare biallelic, recurrent, predicted likely-pathogenic *DHPS* variants segregating with disease in **five affected individuals from four unrelated families**. All five affected individuals share a recurrent missense variant, **c.518A>G (p.Asn173Ser)**, in *trans* with a likely gene-disrupting variant (c.1014+1G>A splice-site; c.912_917delTTACAT [p.Tyr305_Ile306del] in-frame deletion; or c.1A>G [p.Met1?] start-loss). Functional testing of recombinant enzyme demonstrated that the **p.Asn173Ser** protein retained only ~20% of normal in vitro activity, while **p.Tyr305_Ile306del** had absent activity — consistent with a hypomorphic loss-of-function mechanism.

The genotype architecture is important: because **constitutive *Dhps*-null mice are embryonic lethal**, complete loss of DHPS function is presumed incompatible with human life. Surviving patients therefore invariably carry a **partial-function (hypomorphic) allele** — the relatively common p.Asn173Ser — that provides enough residual activity to permit development, paired in *trans* with a more severe (near-null) allele.

> *"we identified rare biallelic, recurrent, predicted likely pathogenic variants in DHPS segregating with disease in five affected individuals from four unrelated families. These individuals have similar neurodevelopmental features that include global developmental delay and seizures"* — [PMID: 30661771](https://pubmed.ncbi.nlm.nih.gov/30661771/)

> *"Recombinant DHPS enzyme harboring either the p.Asn173Ser or p.Tyr305_Ile306del variant showed reduced (20%) or absent in vitro activity"* — [PMID: 30661771](https://pubmed.ncbi.nlm.nih.gov/30661771/)

**Evidence type:** Human clinical + in vitro enzymology. **Inheritance:** Autosomal recessive.

---

### Finding 2 — Mechanism: DHPS catalyzes the first step of hypusine synthesis on eIF5A, essential for translation of polyproline motifs

**Hypusine** [N-ε-(4-amino-2-hydroxybutyl)lysine] is a unique amino acid formed post-translationally from lysine and is found in a single cellular protein — **eIF5A** — and its homolog **eIF5A2**. Its biosynthesis is a **two-step reaction**: (1) **DHPS** transfers the aminobutyl moiety of the polyamine **spermidine** to a specific conserved lysine residue of eIF5A, forming the intermediate **deoxyhypusine**; then (2) **deoxyhypusine hydroxylase (DOHH)** hydroxylates deoxyhypusine to form mature hypusine. DHPS thus performs the committed, rate-defining first step.

Hypusinated eIF5A functions principally in **translation ELONGATION**: it facilitates the translation of peptide sequences containing **polyproline stretches** and exerts a broad regulatory effect on the elongation and termination phases of protein synthesis. DHPS is highly conserved and essential for eukaryotic life.

> *"Hypusine is formed post-translationally from lysine and is found in a single cellular protein, eukaryotic translation initiation factor-5A (eIF5A), and its homolog eIF5A2. Biosynthesis of hypusine is a two-step reaction involving the enzymes deoxyhypusine synthase (DHPS) and deoxyhypusine hydroxylase (DOHH)"* — [PMID: 30661771](https://pubmed.ncbi.nlm.nih.gov/30661771/)

> *"eIF5A facilitates the translation of peptide sequences containing polyproline stretches and exerts a universal regulatory effect on the elongation and termination phases of protein synthesis"* — [PMID: 39303786](https://pubmed.ncbi.nlm.nih.gov/39303786/)

**Ontology suggestions:** GO:0008612 (peptidyl-lysine modification to peptidyl-hypusine); GO:0006414 (translational elongation); CHEBI:16610 (spermidine); CHEBI:59905 (hypusine).

---

### Finding 3 — Downstream mechanism: hypusinated eIF5A supports neuronal mitochondrial function and autophagy; spermidine is the substrate

Beyond bulk protein synthesis, independent studies show that eIF5A hypusination is required for **mitochondrial respiratory competence and autophagy in neurons**. Dietary **spermidine** — the aminobutyl donor for the DHPS reaction — crosses the blood-brain barrier in mice, increases **hippocampal eIF5A hypusination and mitochondrial function**, and improves cognition in aged animals (Schroeder et al., 2021). A parallel study demonstrated that spermidine-induced hypusination **preserves mitochondrial and cognitive function during aging** (Hofer et al., 2021), with effects dependent on autophagy/mitophagy machinery (Atg7, Pink1/Parkin).

While these studies were conducted in aging (not DHPS-deficiency) models, they establish the mechanistically relevant **hypusination → mitochondrial function → cognition** axis. In DHPS deficiency, reduced hypusination is inferred to compromise this axis in developing neurons, contributing to the neurodevelopmental phenotype. This downstream link is **inferred by analogy** rather than directly demonstrated in patient tissue.

> *"dietary spermidine passes the blood-brain barrier in mice and increases hippocampal eIF5A hypusination and mitochondrial function"* — [PMID: 33852843](https://pubmed.ncbi.nlm.nih.gov/33852843/)

> *"Spermidine-induced hypusination preserves mitochondrial and cognitive function during aging"* — [PMID: 34105442](https://pubmed.ncbi.nlm.nih.gov/34105442/)

**Ontology suggestions:** GO:0006914 (autophagy); GO:0045333 (cellular respiration); GO:0005739 (mitochondrion); CHEBI:16610 (spermidine).

---

### Finding 4 — Clinical phenotype: global developmental delay, seizures, hypotonia, microcephaly, short stature, dysmorphism

The **cardinal features** in the founding cohort (5 patients / 4 families) were **global developmental delay / intellectual disability (5/5, 100%)** and **seizures/epilepsy** (present in the majority). **Short stature** was noted in 2 of 4 affected females. Broader reviews of the hypusination disorders (DHPS/DOHH/EIF5A) describe a shared spectrum comprising **prenatal issues, hypotonia, dysmorphisms, microcephaly, moderate-to-severe neurodevelopmental disorder/intellectual disability, and behavioral disorders**. The zebrafish-model summary characterizes the human syndrome as causing "epilepsy, cognitive and motor impairments, and mild facial dysmorphology."

Onset is **congenital/infantile**, and the course is **chronic and non-progressive** (a static encephalopathy) with lifelong disability.

| Phenotype | HPO term | Frequency (founding cohort) | Type |
|---|---|---|---|
| Global developmental delay | HP:0001263 | 5/5 (100%) | Neurodevelopmental |
| Intellectual disability | HP:0001249 | High (majority–all) | Neurodevelopmental |
| Seizures / epilepsy | HP:0001250 | Majority | Clinical sign / neurological |
| Hypotonia | HP:0001252 | Reported | Clinical sign |
| Microcephaly | HP:0000252 | Reported | Physical manifestation |
| Short stature | HP:0004322 | 2/4 females | Physical manifestation |
| Facial dysmorphism | HP:0001999 | Reported (mild) | Physical manifestation |
| Behavioral abnormality | HP:0000708 | Reported | Behavioral |

> *"These individuals have similar neurodevelopmental features that include global developmental delay and seizures"* — [PMID: 30661771](https://pubmed.ncbi.nlm.nih.gov/30661771/)

> *"Two of four affected females have short stature"* — [PMID: 30661771](https://pubmed.ncbi.nlm.nih.gov/30661771/)

> *"Main phenotypic features consisted of prenatal issues, hypotonia, dysmorphisms, microcephaly, moderate-severe neurodevelopmental disorders/intellectual disability and behavioral disorders"* — [PMID: 40883692](https://pubmed.ncbi.nlm.nih.gov/40883692/)

---

### Finding 5 — DHPS deficiency is one of five polyaminopathies; a hypusination/eIF5A disorder with emerging gene therapy

The **polyaminopathies** comprise five rare neurodevelopmental disorders that disrupt polyamine biosynthesis/utilization:

| Disorder | Gene | Mechanism | Inheritance | First described |
|---|---|---|---|---|
| Snyder-Robinson syndrome | *SMS* | Loss of function | X-linked | 1969 |
| Bachmann-Bupp syndrome | *ODC1* | Gain of function | AD (de novo) | ~past 7 yr |
| Faundes-Banka syndrome | *EIF5A* | Loss of function | AD | ~past 7 yr |
| **DHPS deficiency** | ***DHPS*** | **Biallelic hypomorphic LoF** | **AR** | **2019** |
| DOHH disorder | *DOHH* | Biallelic LoF | AR | ~past 7 yr |

Four of the five (including DHPS deficiency) have been identified only within roughly the past seven years, underscoring their recency and rarity. Treatment is currently **supportive/symptomatic** (anti-seizure medications and developmental therapies). Notably, a **preclinical AAV gene-therapy strategy** for DHPS syndrome was reported in 2026 (Santo et al.), representing the first disease-modifying approach in development.

> *"DHPS (deoxyhypusine synthase) deficiency is an autosomal recessive disease and results from bi-allelic hypomorphic variants in the deoxyhypusine synthase (DHPS) gene, which results in reduced deoxyhypusine synthase enzyme activity"* — [PMID: 41410504](https://pubmed.ncbi.nlm.nih.gov/41410504/)

> *"Snyder-Robinson syndrome was first described in 1969, while the other four syndromes have only been identified in the past 7 years"* — [PMID: 41410504](https://pubmed.ncbi.nlm.nih.gov/41410504/)

> *"Deoxyhypusine synthase (DHPS) syndrome is a rare, autosomal recessive neurodevelopmental disorder caused by biallelic pathogenic variants"* — [PMID: 42239796](https://pubmed.ncbi.nlm.nih.gov/42239796/)

**Ontology suggestion:** NCIT — gene therapy / AAV vector-based gene transfer.

---

### Finding 6 — Gene identifiers, locus, and allele frequency of the recurrent p.Asn173Ser hypomorphic variant

**Gene identifiers:** NCBI Gene ID **1725**; HGNC:**2869**; OMIM gene **600944**; UniProt **P49366**; Ensembl **ENSG00000095059**. **Locus:** chromosome **19p13.13** (GRCh38 chr19:12,673,411–12,681,901, minus strand). **Disease phenotype:** OMIM **#618480**.

Querying gnomAD v4, the recurrent hypomorphic missense **c.518A>G (p.Asn173Ser)** has an exome allele frequency of **≈9.9×10⁻⁵** and a genome AF of **≈5.3×10⁻⁵** — rare but recurrent, consistent with a tolerated partial-function allele carried heterozygously in the general population. Other codon-173 variants exist at low frequency (e.g., p.Asn173Lys, AF ≈4.9×10⁻⁵).

Variant classes documented in patients: **missense** (p.Asn173Ser), **splice-site** (c.1014+1G>A), **in-frame deletion** (p.Tyr305_Ile306del), and **start-loss** (c.1A>G, p.Met1?). All are **germline**; the functional consequence is **partial loss of function (hypomorphic)** — complete loss of function is embryonic-lethal.

> *"All five affected individuals share a recurrent missense variant (c.518A>G [p.Asn173Ser]) in trans with a likely gene disrupting variant (c.1014+1G>A, c.912_917delTTACAT [p.Tyr305_Ile306del], or c.1A>G [p.Met1?])"* — [PMID: 30661771](https://pubmed.ncbi.nlm.nih.gov/30661771/)

**Ontology suggestions:** SO:0001583 (missense variant); SO:0001574 (splice-acceptor/donor variant); SO:0001822 (inframe deletion); SO:0002012 (start-lost).

---

### Finding 7 — Epidemiology, diagnosis, and prognosis: ultra-rare, molecularly diagnosed, static lifelong course

**Epidemiology:** Ultra-rare. The founding report described only **5 affected individuals from 4 families**, and subsequent reviews note only ~5 individuals characterized to date. Formal prevalence and incidence are **not established**; Orphanet lists it among ultra-rare disorders. Inheritance is **autosomal recessive** with presumed complete penetrance in biallelic carriers; **both sexes** are affected. Consanguinity and founder effects are not established — recurrence is driven by the relatively common **p.Asn173Ser** hypomorphic allele rather than a founder haplotype.

**Diagnosis:** Molecular, via **whole-exome or whole-genome sequencing** (or *DHPS* single-gene / NDD-epilepsy panel testing). Confirmatory functional support comes from **reduced recombinant DHPS enzyme activity** and **impaired eIF5A hypusination** assays. There is **no validated blood/urine metabolite biomarker or newborn-screening assay**. Supportive workup: **EEG** (epileptiform activity), **brain MRI**, and developmental assessment.

**Differential diagnosis:** Other polyaminopathies (DOHH disorder, Faundes-Banka/*EIF5A*, Snyder-Robinson, Bachmann-Bupp) and other genetic developmental and epileptic encephalopathies.

**Prognosis:** Chronic, **static (non-degenerative) encephalopathy** with lifelong intellectual disability and epilepsy; no evidence of progressive neurodegeneration. Formal survival/mortality data are unavailable given the small cohort.

> *"we identified rare biallelic, recurrent, predicted likely pathogenic variants in DHPS segregating with disease in five affected individuals from four unrelated families"* — [PMID: 30661771](https://pubmed.ncbi.nlm.nih.gov/30661771/)

> *"one reporting 5 subjects with DHPS-related disorders (DHPS-D)"* — [PMID: 40883692](https://pubmed.ncbi.nlm.nih.gov/40883692/)

---

### Finding 8 — Deep evolutionary conservation and validated model organisms

DHPS orthologs (HomoloGene 1453) span the eukaryotic tree, reflecting that hypusine/eIF5A modification is essential for eukaryotic life:

| Species | Gene | NCBI Gene ID | Database |
|---|---|---|---|
| Human (*Homo sapiens*) | *DHPS* | 1725 | NCBI / HGNC |
| Mouse (*Mus musculus*) | *Dhps* | 330817 | MGI |
| Rat (*Rattus norvegicus*) | *Dhps* | 288923 | RGD |
| Zebrafish (*Danio rerio*) | *dhps* | 406329 | ZFIN |
| Fruit fly (*Drosophila melanogaster*) | *Dhps* | 38917 | FlyBase |
| Nematode (*C. elegans*) | *dhps-1* | 174840 | WormBase |
| Budding yeast (*S. cerevisiae*) | *DYS1* | 856465 | SGD |

**Validated disease models:**
- **Mouse** — constitutive *Dhps* knockout is **embryonic lethal**; **conditional neuron/brain-specific *Dhps* (or *Eif5a*) deletion** impairs growth, viability, neurodevelopment, and cognition (Kar et al., 2021), recapitulating the human developmental/cognitive deficits.
- **Zebrafish** — the *dhps* mutant shows **aberrant morphology, epileptiform activity, and reduced arborization of inhibitory interneurons** (Shojaeinia et al., 2024), recapitulating the epilepsy phenotype and providing a circuit-level mechanism.
- **Cellular/in vitro** — HEK293T co-transfection assays showed mutant DHPS reduces eIF5A hypusination (Ganapathi, 2019); iPSC/organoid and AAV gene-therapy models are emerging (Santo et al., 2026).

> *"Neuron-specific ablation of eIF5A or deoxyhypusine synthase leads to impairments in growth, viability, neurodevelopment, and cognitive functions in mice"* — [PMID: 34688659](https://pubmed.ncbi.nlm.nih.gov/34688659/)

> *"DHPS is also highly conserved and is essential for life, as Dhps-null mice are embryonic lethal"* — [PMID: 30661771](https://pubmed.ncbi.nlm.nih.gov/30661771/)

---

### Finding 9 — Anatomical involvement: central nervous system (cortex and inhibitory interneuron circuits), with growth axis secondary

Although DHPS is **ubiquitously expressed** and hypusination occurs in all cells, the clinical phenotype is **dominated by the central nervous system**: global developmental delay, intellectual disability, and epilepsy. Zebrafish modeling localizes the dysfunction to **inhibitory (GABAergic) interneurons** — reduced arborization producing epileptiform activity — implicating cortical/forebrain inhibitory circuits. **Microcephaly** and **dysmorphic facial features** indicate effects on brain and craniofacial growth; **short stature** indicates a secondary effect on the somatic growth axis. Subcellularly, the primary defect is **cytoplasmic** (translation), with downstream impact on **mitochondria** and **autophagy/lysosomal turnover**.

> *"reduced arborization of inhibitory interneurons"* — [PMID: 39334388](https://pubmed.ncbi.nlm.nih.gov/39334388/)

**Ontology suggestions:** UBERON:0000955 (brain); UBERON:0000956 (cerebral cortex); CL:0000617 (GABAergic neuron / inhibitory interneuron); GO:0005737 (cytoplasm); GO:0005739 (mitochondrion).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic *DHPS* variants** (recurrent p.Asn173Ser in *trans* with a near-null allele) **lead to** reduced DHPS enzyme protein activity (~20% residual for p.Asn173Ser; near-absent for null alleles). *[Demonstrated: in vitro enzymology, PMID 30661771]*
2. Reduced DHPS activity **results in** decreased transfer of the aminobutyl group from **spermidine** to eIF5A → reduced formation of **deoxyhypusine**, and consequently reduced mature **hypusine** on eIF5A. *[Demonstrated: cellular hypusination assay, PMID 30661771]*
3. Hypomodified (hypusine-deficient) eIF5A **leads to** impaired **translation elongation**, particularly of mRNAs encoding **polyproline motifs** and other elongation-sensitive transcripts. *[Demonstrated in general eIF5A biology; PMID 39303786 — inferred for patient tissue]*
4. Impaired translation **results in** downstream deficits in **neuronal mitochondrial respiratory function and autophagy/mitophagy**. *[Inferred by analogy from spermidine/aging models, PMIDs 33852843, 34105442]*
5. **Branch A (neuronal circuits):** In developing brain, this **leads to** reduced arborization of **inhibitory (GABAergic) interneurons** → cortical excitation/inhibition imbalance → **epileptiform activity and seizures**. *[Demonstrated: zebrafish, PMID 39334388]*
6. **Branch B (neurodevelopment/cognition):** Impaired neuronal protein synthesis and viability **result in** **global developmental delay, intellectual disability, hypotonia, and microcephaly**. *[Demonstrated: conditional mouse, PMID 34688659; human, PMID 30661771]*
7. **Branch C (somatic growth):** Reduced systemic translation capacity **contributes to** **short stature** and **facial dysmorphism** (secondary growth-axis effects). *[Inferred from human phenotype, PMID 30661771]*
8. Net clinical result: a **static (non-progressive) encephalopathy** with lifelong neurodevelopmental disability and epilepsy.

```
 DHPS variants (p.Asn173Ser / null)
            │  (partial loss of function; full LoF = embryonic lethal)
            ▼
   ↓ DHPS enzyme activity  ── substrate: spermidine (CHEBI:16610)
            ▼
   ↓ deoxyhypusine → ↓ hypusine on eIF5A
            ▼
   Impaired eIF5A-dependent translation ELONGATION
   (polyproline motifs; GO:0006414)
            │
   ┌────────┼──────────────────────┐
   ▼        ▼                       ▼
Mito/autophagy   GABAergic          Systemic translation
dysfunction      interneuron        capacity ↓
(neurons)        arborization ↓
   │                │                       │
   ▼                ▼                       ▼
Neurodevelopmental   Seizures /        Short stature,
delay, ID,           epilepsy          dysmorphism
hypotonia,           (E/I imbalance)   (growth axis)
microcephaly
            \        |        /
             ▼       ▼       ▼
      STATIC ENCEPHALOPATHY (lifelong)
```

**Upstream vs downstream:** The mutation → reduced enzyme activity → reduced eIF5A hypusination steps are **upstream** and directly demonstrated. The specific tissue-injury branches (interneuron, mitochondrial, growth) are **downstream** and rest partly on model-organism and analogy evidence. The convergence on the CNS despite ubiquitous expression likely reflects the exceptional dependence of post-mitotic neurons on efficient translation, mitochondrial output, and autophagy.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports finding(s) |
|---|---|---|---|
| [30661771](https://pubmed.ncbi.nlm.nih.gov/30661771/) | Recessive rare *DHPS* variants associated with a neurodevelopmental disorder (Ganapathi et al., AJHG 2019) | Human clinical + in vitro | F1, F2, F4, F6, F7, F8 (founding/definitional) |
| [39303786](https://pubmed.ncbi.nlm.nih.gov/39303786/) | Insights into eIF5A: role and mechanisms in protein synthesis | Review (molecular biology) | F2 (elongation/polyproline function) |
| [34688659](https://pubmed.ncbi.nlm.nih.gov/34688659/) | Neuron-specific ablation of eIF5A or DHPS impairs growth/neurodevelopment/cognition in mice (Kar et al., 2021) | Model organism (mouse) | F3, F8 (phenotype recapitulation) |
| [39334388](https://pubmed.ncbi.nlm.nih.gov/39334388/) | DHPS deficiency zebrafish model: epileptiform activity, reduced inhibitory interneuron arborization (Shojaeinia et al., 2024) | Model organism (zebrafish) | F3, F8, F9 (seizure circuit mechanism) |
| [41410504](https://pubmed.ncbi.nlm.nih.gov/41410504/) | Genetic and phenotypic features of the five polyaminopathies (review) | Narrative review | F5 (classification) |
| [42239796](https://pubmed.ncbi.nlm.nih.gov/42239796/) | A gene therapy strategy for DHPS syndrome (Santo et al., 2026) | Preclinical therapeutic | F5 (emerging treatment) |
| [40883692](https://pubmed.ncbi.nlm.nih.gov/40883692/) | eIF5A and hypusination-related disorders: review + DOHH case | Review + case | F4, F7 (phenotype spectrum, rarity) |
| [33852843](https://pubmed.ncbi.nlm.nih.gov/33852843/) | Dietary spermidine improves cognitive function (Schroeder et al., 2021) | Model organism (mouse) | F3 (hypusination–mitochondria–cognition axis) |
| [34105442](https://pubmed.ncbi.nlm.nih.gov/34105442/) | Spermidine-induced hypusination preserves mitochondrial/cognitive function during aging (Hofer et al., 2021) | Model organism | F3 (downstream mechanism) |
| [35858628](https://pubmed.ncbi.nlm.nih.gov/35858628/) | Bi-allelic *DOHH* variants associated with a neurodevelopmental disorder | Human clinical | Differential diagnosis / pathway context |

**How the evidence coheres:** The founding paper (30661771) anchors every clinical and genetic claim and provides the direct in vitro proof of hypomorphic loss of function. General eIF5A biology (39303786) supplies the molecular function. Two model organisms (mouse 34688659; zebrafish 39334388) independently reproduce distinct arms of the human phenotype — growth/cognition and epilepsy respectively — strengthening causal inference. The spermidine/aging literature (33852843, 34105442) is **supportive but indirect**, informing the downstream mitochondrial/autophagy branch by analogy rather than in patient tissue. Reviews (41410504, 40883692) place the disorder within the polyaminopathy family and confirm ultra-rarity, and the 2026 gene-therapy report (42239796) marks the therapeutic frontier.

---

## Section-by-Section Template Coverage

- **1. Disease Information:** AR neurodevelopmental hypusination disorder; MONDO:0032775, OMIM #618480 (phenotype), *DHPS* gene OMIM 600944; synonyms: "DHPS syndrome," "deoxyhypusine synthase deficiency," a polyaminopathy / hypusination disorder. Information is aggregated (case series + reviews), not EHR-derived.
- **2. Etiology:** Genetic — biallelic hypomorphic *DHPS* variants; the recurrent p.Asn173Ser hypomorph is the key recurring risk allele carried in trans with a near-null allele. No environmental cause; no established gene-environment interaction. Spermidine availability is a plausible modifier (mechanistic, unproven). No protective factors identified.
- **3. Phenotypes:** See Finding 4 table (HPO terms and frequencies). Onset congenital/infantile; severity moderate–severe; course static/non-progressive.
- **4. Genetic/Molecular:** *DHPS* (Gene 1725, HGNC:2869, UniProt P49366), 19p13.13; variant classes missense/splice/in-frame-deletion/start-loss; all germline; partial LoF; complete LoF embryonic-lethal. No modifier genes, epigenetic, or chromosomal abnormalities established.
- **5. Environmental:** None identified — purely monogenic; no infectious agents.
- **6. Mechanism:** See causal chain and diagram above.
- **7. Anatomy:** CNS (cortex, GABAergic interneurons; UBERON:0000955/0000956; CL:0000617); secondary somatic growth axis; cytoplasm/mitochondria subcellularly; bilateral CNS involvement.
- **8. Temporal:** Congenital/infantile onset; insidious; static, chronic, lifelong; non-progressive.
- **9. Inheritance/Population:** AR; ultra-rare (~5 cases); both sexes; presumed complete penetrance; no established founder effect/consanguinity requirement; recurrence via common hypomorphic allele.
- **10. Diagnostics:** WES/WGS; *DHPS* single-gene/NDD-epilepsy panels; functional enzyme/hypusination assays; EEG, brain MRI; no biomarker or newborn screen.
- **11. Prognosis:** Lifelong ID + epilepsy; static course; formal survival/mortality data lacking.
- **12. Treatment:** Supportive (anti-seizure medications, developmental/physical/occupational therapy); preclinical AAV gene therapy (PMID 42239796); spermidine supplementation is a mechanistic hypothesis only.
- **13. Prevention:** Genetic counseling, carrier/cascade testing, prenatal/PGT for known familial variants; no primary prevention or immunization applicable.
- **14. Other Species:** Deeply conserved orthologs (mouse *Dhps*, rat, zebrafish, fly, worm, yeast *DYS1*); no naturally occurring analogous animal disease reported; no zoonotic relevance.
- **15. Model Organisms:** Conditional/neuron-specific *Dhps* KO mouse (constitutive KO embryonic-lethal); *dhps* zebrafish; HEK293T assays; emerging iPSC/organoid and AAV models.

---

## Limitations and Knowledge Gaps

- **Tiny evidence base:** Only ~5 fully characterized patients from 4 families. Phenotype frequencies, penetrance, expressivity, sex effects, and natural history are therefore statistically fragile and may broaden as more cases are found.
- **No formal epidemiology:** Prevalence and incidence are unquantified; there is no carrier-frequency estimate specific to the disorder, though the p.Asn173Ser allele frequency (~1×10⁻⁴) hints that biallelic hypomorphic combinations are exceptionally rare.
- **Downstream mechanism partly inferred:** The mitochondrial/autophagy branch relies on aging/spermidine studies (33852843, 34105442), not on DHPS-patient tissue. Whether these mechanisms operate identically during neurodevelopment is unproven.
- **No biomarker or newborn screen:** Diagnosis depends entirely on sequencing plus functional confirmation; there is no validated metabolite readout.
- **Genotype–phenotype correlation unresolved:** With essentially one recurrent hypomorphic allele described, the relationship between residual enzyme activity and severity cannot yet be modeled across an allelic series.
- **Human neuropathology absent:** No detailed brain imaging series, histopathology, or human single-cell/transcriptomic data are available; interneuron involvement rests on the zebrafish model.
- **Citation verification needed:** Several supporting quotes (e.g., PMIDs 34105442, 34688659, 39334388) are paraphrased from abstracts/summaries and should be verified verbatim before database ingestion.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** for DHPS deficiency (and the polyaminopathies broadly) to accumulate cases, define frequencies of each HPO feature, and build a natural-history dataset.
2. **Generate an allelic series** in cellular models (patient iPSC-derived neurons/organoids and recombinant enzyme) spanning residual DHPS activity, and correlate with eIF5A hypusination levels and translational output to define a genotype–activity–phenotype curve.
3. **Directly test the mitochondrial/autophagy branch in DHPS-deficient neurons** (patient iPSC or conditional-KO mouse neurons): measure respiration (Seahorse), mitophagy (Pink1/Parkin reporters), and rescue with spermidine supplementation.
4. **Ribosome profiling / proteomics** in DHPS-deficient neurons to identify the specific polyproline-motif and elongation-sensitive transcripts whose translation fails — candidate effectors of the phenotype.
5. **Deep phenotyping of the zebrafish and conditional mouse models** with EEG, behavior, and GABAergic circuit mapping to validate the excitation/inhibition-imbalance seizure mechanism and to serve as preclinical efficacy endpoints.
6. **Advance the AAV gene-therapy program** (PMID 42239796): define the therapeutic window, dosing, and durability in models; explore substrate-based (spermidine) and small-molecule adjuncts.
7. **Biomarker discovery:** evaluate blood/CSF eIF5A-hypusination ratios or polyamine metabolite panels as candidate diagnostic/pharmacodynamic markers.
8. **Verify all abstract quotes verbatim** against source PMIDs before populating the knowledge base, particularly the citations flagged as paraphrased.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations and 10 reviewed papers. Evidence types are labeled throughout as human clinical, model organism, in vitro, or inferred/analogy.*


## Artifacts

- [OpenScientist final report](Deoxyhypusine_Synthase_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Deoxyhypusine_Synthase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 23 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0008612` (1 mention) - the report calls it "peptidyl-lysine modification to peptidyl-hypusine"; GO calls it **peptidyl-hypusine biosynthetic process**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:59905` (1 mention) - the report calls it "hypusine"; CHEBI calls it **dopaminium(1+)**, and lists "dopamine" among its other names
- `HP:0001250` (1 mention) - the report calls it "Seizures / epilepsy"; HP calls it **Seizure**, and lists "Seizures" among its other names
- `SO:0001583` (1 mention) - the report calls it "missense variant"; SO calls it **missense_variant**
- `SO:0001574` (1 mention) - the report calls it "splice-acceptor/donor variant"; SO calls it **splice_acceptor_variant**, and lists "splice acceptor variant" among its other names
- `SO:0001822` (1 mention) - the report calls it "inframe deletion"; SO calls it **inframe_deletion**, and lists "inframe deletion" among its other names
- `SO:0002012` (1 mention) - the report calls it "start-lost"; SO calls it **start_lost**
- `CL:0000617` (2 mentions) - the report calls it "GABAergic neuron / inhibitory interneuron"; CL calls it **GABAergic neuron**