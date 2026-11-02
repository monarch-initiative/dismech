---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T17:21:13.853253'
end_time: '2026-10-25T17:33:58.700660'
duration_seconds: 764.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Dysmorphic Facies And Variable Seizures
  mondo_id: MONDO:0031011
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: NEDDFAS; EMC10-related neurodevelopmental disorder
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
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 12
  relevance_assessed: 12
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 17
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0031011
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with dysmorphic facies and variable
      seizures
  - term_id: NCIT:C157866
    reported_labels:
    - Orthopedic Procedure
    ontology_label: Gluten Free Diet
  labels_variant: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Dysmorphic_Facies_And_Variable_Seizures-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Dysmorphic_Facies_And_Variable_Seizures-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Dysmorphic Facies And Variable Seizures
- **MONDO ID:** MONDO:0031011 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** NEDDFAS; EMC10-related neurodevelopmental disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Dysmorphic Facies And Variable Seizures** covering all of the
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

# Neurodevelopmental Disorder With Dysmorphic Facies And Variable Seizures (NEDDFAS): A Comprehensive Disease Report

**MONDO:** MONDO:0031011 · **OMIM:** #619264 · **Causal gene:** *EMC10* (HGNC:28974; chromosome 19q13.33) · **Inheritance:** Autosomal recessive · **Category:** Mendelian

---

## Summary

**Neurodevelopmental Disorder With Dysmorphic Facies And Variable Seizures (NEDDFAS)** is an ultra-rare autosomal recessive syndromic intellectual-disability disorder caused by **biallelic loss-of-function (LoF) variants in *EMC10***, the gene encoding subunit 10 of the **endoplasmic reticulum (ER) membrane protein complex (EMC)**. The EMC is a highly conserved, membrane-embedded insertase that mediates the insertion and folding of **tail-anchored and multipass transmembrane proteins** into the ER membrane. NEDDFAS was first delineated in 2021 in 13 individuals from 7 consanguineous families who shared a recurrent homozygous frameshift variant, *EMC10* c.287delG (p.Gly96Alafs*9) ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/)), and the molecular and clinical spectrum was expanded in 2022 and by subsequent case reports.

The disorder presents in **infancy or early childhood** with **global developmental delay/intellectual disability (GDD/ID) of variable severity**, **variable seizures**, **microcephaly**, **minor facial dysmorphism** (elongated/long face, curly hair), and **variable renal and skeletal features** (cubitus valgus, arachnodactyly, scoliosis), with additional reports of gingival hyperplasia. The intellectual disability is static (non-progressive) and lifelong. A single recurrent allele — **c.287delG (p.Gly96Alafs*9)** — accounts for the majority of reported patients; remarkably, it arose independently on two distinct founder haplotypes at a likely hypermutable site, explaining its recurrence across unrelated international, consanguineous families.

The proposed mechanism is that **biallelic EMC10 LoF reduces functional EMC insertase capacity**, impairing the biogenesis of membrane-protein clients (receptors, ion channels, transporters) in developing neurons and other tissues, leading to abnormal neurodevelopment and the multisystem phenotype. There is **no disease-specific or disease-modifying therapy**; management is supportive and symptomatic (antiseizure medication, early developmental intervention, rehabilitation, orthopedic and dental care) with **genetic counseling** for at-risk consanguineous/carrier families. Diagnosis is achieved almost exclusively through **whole-exome or whole-genome sequencing** with Sanger confirmation and segregation analysis.

---

## 1. Disease Information

**Overview.** NEDDFAS is a Mendelian, autosomal recessive neurodevelopmental syndrome. It is defined molecularly by biallelic LoF variants in *EMC10* and clinically by the combination of developmental delay/intellectual disability, variable seizures, and variable dysmorphic facial features — as captured in its name. The first cohort described it as "a phenotypic spectrum of intellectual disability (ID) and global developmental delay (GDD), variable seizures and variable dysmorphic features" ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0031011 |
| OMIM | #619264 |
| Causal gene | *EMC10* (HGNC:28974; NCBI Gene; located 19q13.33) |
| Reference transcript | NM_206538.3 |
| Orphanet | Not separately catalogued at time of research (subsumed under rare syndromic intellectual disability) |
| ICD-11 | Closest: syndromic intellectual developmental disorder (no NEDDFAS-specific code) |
| MeSH | No disease-specific descriptor; indexed under Neurodevelopmental Disorders / Intellectual Disability |

**Synonyms / alternative names.** NEDDFAS; EMC10-related neurodevelopmental disorder; EMC10 deficiency; Neurodevelopmental disorder with dysmorphic facies and variable seizures.

**Source of information.** Evidence is derived from **individual patient reports and small aggregated case series** (~25–30 reported patients across fewer than 15 families), not from large disease-level registries or EHR-derived cohorts. All data come from the primary genetics literature.

---

## 2. Etiology

**Primary cause (genetic).** NEDDFAS is a **monogenic Mendelian disorder** caused exclusively by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *EMC10***. There are no known environmental, infectious, toxic, or multifactorial causes. The disease is fully genetic in origin.

**Genetic risk factors.**
- **Causal variants:** biallelic *EMC10* LoF alleles. The recurrent frameshift **c.287delG (p.Gly96Alafs*9)** is the predominant pathogenic allele. Additional reported variants include the nonsense **c.343C>T (p.Arg115Ter)** ([PMID: 40150819](https://pubmed.ncbi.nlm.nih.gov/40150819/)) and the frameshift **c.431del (p.Asp144AlafsTer3)** ([PMID: 40741735](https://pubmed.ncbi.nlm.nih.gov/40741735/)), plus five additional novel biallelic LoF variants reported in the expanded cohort ([PMID: 35684946](https://pubmed.ncbi.nlm.nih.gov/35684946/)).
- **Consanguinity** is a major risk factor: most families are consanguineous, which raises the probability of homozygosity for rare recessive LoF alleles.
- **Modifier genes:** none established. Variable expressivity exists but no specific genetic modifiers have been identified.

**Environmental risk factors.** None known or implicated. There are no toxins, exposures, lifestyle factors, or occupational hazards associated with disease occurrence or severity.

**Protective factors.** None known (genetic or environmental). As a fully penetrant recessive disorder, the only "protective" factor is the absence of a second pathogenic allele (i.e., heterozygous carriers are unaffected).

**Gene–environment interactions.** None described. The disorder is monogenic with no documented gene–environment modulation.

---

## 3. Phenotypes

The NEDDFAS phenotype is **syndromic and multisystem**, with a neurodevelopmental core plus variable dysmorphic, renal, and skeletal features. The first cohort described "a phenotypic spectrum of intellectual disability (ID) and global developmental delay (GDD), variable seizures and variable dysmorphic features (elongated face, curly hair, cubitus valgus, and arachnodactyly)" ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/)). The expanded cohort found ID "ranging from mild to severe" and "an overlap between the clinical features of EMC10- and EMC1-related disease" ([PMID: 35684946](https://pubmed.ncbi.nlm.nih.gov/35684946/)). Forest-St-Onge et al. summarized it as "an autosomal recessive syndrome characterized by global developmental delay, intellectual disability, microcephaly, seizures, renal abnormalities, and minor facial dysmorphic features" ([PMID: 40150819](https://pubmed.ncbi.nlm.nih.gov/40150819/)).

| Phenotype | HPO term | Type | Frequency | Onset | Severity / course |
|---|---|---|---|---|---|
| Global developmental delay | HP:0001263 | Clinical sign | Core (near-universal) | Infancy/early childhood | Variable; static |
| Intellectual disability | HP:0001249 | Clinical sign | Core (near-universal) | Early childhood | Mild→severe; non-progressive |
| Seizures | HP:0001250 | Clinical sign | Variable | Childhood | Variable |
| Microcephaly | HP:0000252 | Physical manifestation | Common | Congenital/early | Variable |
| Facial dysmorphism (elongated/long face) | HP:0000276 | Physical manifestation | Variable | Congenital | Minor |
| Curly hair | HP:0002212 | Physical manifestation | Variable | Congenital | Minor |
| Cubitus valgus | HP:0002967 | Physical manifestation | Variable | Childhood | Minor |
| Arachnodactyly | HP:0001166 | Physical manifestation | Variable | Congenital | Minor |
| Renal abnormalities | HP:0000077 | Clinical sign | Variable | Variable | Variable |
| Scoliosis | HP:0002650 | Physical manifestation | Reported (case) | Childhood | Variable |
| Gingival hyperplasia | HP:0000212 | Physical manifestation | Reported (case) | Childhood | Variable |

**Age of onset.** Infancy to early childhood (developmental delay typically evident in the first years of life; some features such as microcephaly and dysmorphism are congenital).

**Severity and progression.** Highly **variable** in severity (ID mild to severe). The neurodevelopmental deficit is **static/non-progressive**; seizures are variable and may be episodic.

**Quality of life impact.** Lifelong intellectual disability and developmental delay substantially affect adaptive functioning, independence, communication, and education; seizures and skeletal/renal complications add further burden. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***EMC10*** (ER membrane protein complex subunit 10), HGNC:28974, located on **chromosome 19q13.33**; reference transcript **NM_206538.3**. OMIM gene/phenotype entry **#619264**.

**Pathogenic variants.**

| Variant (cDNA / protein) | Type | Classification | Notes |
|---|---|---|---|
| c.287delG (p.Gly96Alafs*9) | Frameshift | Pathogenic | Recurrent founder/hotspot allele; ~majority of patients; two distinct founder haplotypes ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/)) |
| c.343C>T (p.Arg115Ter) | Nonsense | Pathogenic | [PMID: 40150819](https://pubmed.ncbi.nlm.nih.gov/40150819/) |
| c.431del (p.Asp144AlafsTer3) | Frameshift | Pathogenic | [PMID: 40741735](https://pubmed.ncbi.nlm.nih.gov/40741735/) |
| 5 additional novel biallelic LoF variants | Frameshift/nonsense/splice | Pathogenic/Likely pathogenic | Expanded cohort ([PMID: 35684946](https://pubmed.ncbi.nlm.nih.gov/35684946/)) |

**Variant class and functional consequence.** All disease alleles are **loss-of-function** (frameshift, nonsense, splice). The recurrent c.287delG "results in significantly reduced EMC10 RNA expression and an unstable truncated EMC10 protein" ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/)) — i.e., LoF via nonsense-mediated decay of the transcript plus instability of any residual protein. Mechanistically this is a **loss-of-function**, not gain-of-function or dominant-negative, mechanism in the recessive context. Note that one report raised the possibility of "dual molecular effects" on the neuropsychiatric phenotype ([PMID: 40741735](https://pubmed.ncbi.nlm.nih.gov/40741735/)); nonetheless the established disease mechanism is biallelic LoF.

**Allele frequency / population databases.** Pathogenic *EMC10* LoF alleles are ultra-rare in gnomAD; the recurrent c.287delG is notable for arising at a **hypermutable site** rather than as a single ancient founder event.

**Somatic vs germline.** All variants are **germline**. No somatic association.

**Modifier genes.** None identified. Phenotypic variability is unexplained at the genetic-modifier level.

**Epigenetic information.** None specifically described for NEDDFAS.

**Chromosomal abnormalities.** None; disease is caused by small sequence variants, not large structural/chromosomal rearrangements. Chromosomal microarray and karyotype are typically normal (and used to exclude differentials).

---

## 5. Environmental Information

**Environmental factors:** None. NEDDFAS is a purely genetic Mendelian disorder.
**Lifestyle factors:** Not applicable.
**Infectious agents:** Not applicable.

This section is **not applicable** beyond noting that consanguinity (a demographic/social factor) increases the probability of a child being homozygous for a rare recessive allele, but it is not an "environmental cause" of the mutation itself.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **biallelic loss-of-function variant in *EMC10*** (e.g., c.287delG, p.Gly96Alafs*9) is present. **(Demonstrated.)**
2. The frameshift transcript undergoes **nonsense-mediated decay**, *leading to* "significantly reduced EMC10 RNA expression," and any residual protein is "an unstable truncated EMC10 protein" ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/)). **(Demonstrated.)**
3. Loss of the EMC10 subunit *results in* **reduced functional ER membrane protein complex (EMC) insertase activity**. **(Inferred** from EMC subunit biology.)
4. Reduced EMC capacity *impairs* the **co-/post-translational insertion and folding of EMC client proteins** — tail-anchored and multipass transmembrane proteins, including neuronal receptors, ion channels, and transporters — because EMC is "responsible for the post-translational insertion of tail-anchored membrane proteins into the endoplasmic reticulum in a defined topology" ([PMID: 35684946](https://pubmed.ncbi.nlm.nih.gov/35684946/)). **(Inferred** from EMC function; supported by model-organism data, e.g., [PMID: 34918864](https://pubmed.ncbi.nlm.nih.gov/34918864/).)
5. Defective biogenesis of these membrane clients *leads to* **dysregulated neuronal excitability and impaired neurodevelopment**, manifesting as GDD/ID and seizures; parallel effects in other tissues *produce* dysmorphism and renal/skeletal anomalies. **(Inferred.)**

**Branch — secreted EMC10 isoform.** EMC10 also has a secreted isoform (EMC10/INM02/HSS-1/SCA1) that acts as a bone-marrow-derived angiogenic growth factor: "Emc10 signaled through small GTPases, p21-activated kinase, and the p38 mitogen-activated protein kinase (MAPK)-MAPK-activated protein kinase 2 (MK2) pathway to promote actin polymerization and endothelial cell migration" ([PMID: 28931551](https://pubmed.ncbi.nlm.nih.gov/28931551/)). Loss of this secreted signaling function *could* contribute to developmental/vascular phenotypes. **(Speculative.)**

```
EMC10 biallelic LoF (c.287delG)      [DEMONSTRATED]
        │  NMD + unstable truncated protein
        ▼
Reduced EMC10 protein                 [DEMONSTRATED]
        │
        ▼
Reduced EMC insertase capacity        [INFERRED]
        │
        ▼
Impaired insertion/folding of         [INFERRED, model-organism support]
tail-anchored & multipass membrane
clients (receptors, channels, transporters)
        │
        ├──► Neurons: dysregulated excitability,  ──► GDD / ID / seizures
        │    impaired neurodevelopment
        │
        └──► Other tissues (craniofacial, renal,  ──► Dysmorphism, microcephaly,
             skeletal)                                 renal & skeletal anomalies

Branch: Loss of secreted EMC10 (HSS-1/INM02)
        → ↓ small GTPase→PAK→p38-MAPK-MK2 signaling  [SPECULATIVE contribution]
```

### Detail by category

- **Molecular pathways:** Core defect is in the **EMC-mediated membrane-protein insertion pathway** (parallel to the GET pathway) in the ER. The catalytic core belongs to the **Oxa1 insertase family** ([PMID: 37417332](https://pubmed.ncbi.nlm.nih.gov/37417332/); [PMID: 33629497](https://pubmed.ncbi.nlm.nih.gov/33629497/); [PMID: 36041783](https://pubmed.ncbi.nlm.nih.gov/36041783/)). The secreted-isoform branch involves **small GTPase → PAK → p38-MAPK-MK2** signaling ([PMID: 28931551](https://pubmed.ncbi.nlm.nih.gov/28931551/)).
- **Cellular processes:** Membrane-protein biogenesis, ER protein quality control/folding. In fungi, EMC loss also impaired **autophagy** via reduced Atg9 steady-state levels ([PMID: 36772852](https://pubmed.ncbi.nlm.nih.gov/36772852/)) — a potential but unproven contributor in humans.
- **Protein dysfunction:** Loss of function of the EMC10 subunit; truncated protein is unstable and degraded.
- **Immune / metabolic / tissue-damage mechanisms:** No specific autoimmune, metabolic, or oxidative-stress mechanism established for NEDDFAS.
- **Cell types & biological processes (ontology suggestions):** GO:0045050 (protein insertion into ER membrane), GO:0071816 (tail-anchored membrane protein insertion into ER membrane), GO:0006612 (protein targeting to membrane), GO:0007399 (nervous system development), GO:0021954 (central nervous system neuron development). Cell types: CL:0000540 (neuron), CL:0000679 (glutamatergic neuron), CL:0000099 (interneuron).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** Central nervous system / brain (UBERON:0000955) — the dominant target (ID, GDD, seizures, microcephaly).
- **Secondary:** Kidney (UBERON:0002113) — renal abnormalities; skeleton (UBERON:0001434) — scoliosis, cubitus valgus, arachnodactyly; craniofacial structures (UBERON:0000033, head) — dysmorphism; gingiva/oral cavity (UBERON:0001828) — gingival hyperplasia.
- **Body systems:** Nervous system (primary); musculoskeletal, renal/urinary, and craniofacial systems (secondary).

**Tissue and cell level.** Nervous tissue (neurons, CL:0000540). Because EMC is ubiquitously required for membrane-protein biogenesis, multiple tissue types are affected, but neurons appear most clinically vulnerable. EMC10 is expressed in normal human brain by immunohistochemistry ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/)).

**Subcellular level.** The **endoplasmic reticulum membrane** (GO:0005789) is the site of EMC function; the EMC is an integral ER-membrane complex. GO cellular component: GO:0072546 (EMC/ER membrane protein complex).

**Localization / lateralization.** Brain involvement is **bilateral/diffuse**; dysmorphic and skeletal features are generally symmetric. No consistent lateralization.

---

## 8. Temporal Development

**Onset.** Congenital to early childhood. Developmental delay is apparent in infancy; microcephaly and dysmorphism may be present at birth. Onset is **insidious/chronic** rather than acute.

**Progression.** The intellectual disability is **static (non-progressive)** — a stable neurodevelopmental deficit rather than a neurodegenerative course. This contrasts with EMC1-related disease, which can feature cerebellar atrophy/degeneration ([PMID: 26942288](https://pubmed.ncbi.nlm.nih.gov/26942288/)). Seizures may be episodic. Disease duration is **lifelong/chronic**.

**Patterns / critical periods.** No spontaneous remission of the core neurodevelopmental phenotype. The key window for intervention is **early childhood** (early developmental intervention, seizure control), consistent with general neurodevelopmental-disorder principles.

---

## 9. Inheritance and Population

**Epidemiology.** **Ultra-rare.** No formal prevalence or incidence estimates exist. Approximately **25–30 reported patients across fewer than 15 families** at the time of research. The disorder is enriched in **consanguineous populations** and international in distribution (reported in Middle Eastern, South Asian, and other consanguineous cohorts).

**Inheritance.** **Autosomal recessive.** Affected individuals are homozygous (or compound heterozygous) for biallelic LoF *EMC10* variants in consanguineous families ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/); [PMID: 35684946](https://pubmed.ncbi.nlm.nih.gov/35684946/)). **No monoallelic (dominant) EMC10 disease has been established** — a notable contrast with *EMC1*, where both monoallelic and biallelic variants cause disease ([PMID: 26942288](https://pubmed.ncbi.nlm.nih.gov/26942288/)).

**Penetrance / expressivity.** Appears **fully penetrant** in biallelic LoF individuals, with **variable expressivity** (ID severity mild to severe; variable seizures and dysmorphism).

**Founder effect / hypermutable site.** The recurrent c.287delG "arose on two founder haplotypes" and, remarkably, "is likely the result of a hypermutable site and arose on distinct founder haplotypes" ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/)) — i.e., recurrence is driven by a mutational hotspot rather than a single shared ancestor.

**Anticipation / germline mosaicism.** No genetic anticipation (not a repeat-expansion disorder). Germline mosaicism not specifically reported.

**Consanguinity.** A major contributing factor, as expected for a rare recessive disorder.

**Carrier frequency.** Not established; ultra-rare alleles make population carrier frequency very low outside affected families.

**Demographics.** No strong sex bias established (autosomal recessive; males and females affected). Age distribution reflects pediatric diagnosis.

---

## 10. Diagnostics

**Genetic testing (the diagnostic cornerstone).** All reported cases were identified by **whole-exome sequencing (WES) or whole-genome sequencing (WGS)** with **Sanger confirmation and familial segregation analysis**. A representative diagnostic pathway: "Initial genetic testing included karyotype analysis, FMR1 CGG repeat analysis, and chromosomal microarray analysis. Subsequently, whole-exome sequencing (WES) was performed, and Sanger sequencing was used to confirm the identified variant and conduct familial segregation analysis" ([PMID: 40741735](https://pubmed.ncbi.nlm.nih.gov/40741735/)). The value of reanalysis is emphasized: Forest-St-Onge et al. "underscore the importance of exome reanalysis in clinical practice" ([PMID: 40150819](https://pubmed.ncbi.nlm.nih.gov/40150819/)).

- **WES / WGS:** High diagnostic utility; the primary method by which the disorder is identified.
- **Gene panels / single-gene testing:** ID/epilepsy gene panels or *EMC10* single-gene testing can detect the recurrent c.287delG, especially in consanguineous families or those of shared ancestry.
- **Chromosomal microarray, karyotype, FMR1 (Fragile X) testing:** Typically **normal**; used to exclude common differentials before/alongside sequencing.
- **Mitochondrial DNA / repeat-expansion testing:** Not indicated (not the disease mechanism).

**Clinical and imaging workup.** Brain **MRI** and **EEG** (for seizure characterization) support the clinical assessment. Renal imaging/ultrasound where renal abnormalities are suspected.

**Biomarkers / laboratory tests.** No specific biochemical biomarker exists; diagnosis is genetic.

**Clinical criteria / differential diagnosis.** No formal consensus diagnostic criteria. Key **differential diagnoses** include **EMC1-related neurodevelopmental disorder** (overlapping features; "an overlap between the clinical features of EMC10- and EMC1-related disease," [PMID: 35684946](https://pubmed.ncbi.nlm.nih.gov/35684946/)) and other syndromic autosomal recessive intellectual-disability disorders.

**Screening.** In families with a known *EMC10* variant, **cascade carrier testing** is appropriate. No population-based newborn screening exists for this ultra-rare disorder.

---

## 11. Outcome / Prognosis

**Survival / mortality.** No disease-specific mortality data and **no evidence of reduced survival** reported. Life expectancy appears not markedly shortened based on available (limited) reports.

**Morbidity and function.** The dominant burden is **lifelong intellectual disability and developmental delay** of variable severity, with associated impacts on education, communication, independence, and adaptive functioning. Seizures, scoliosis, renal anomalies, and dental issues add morbidity. No formal disability/QoL instrument data exist.

**Disease course.** **Static (non-progressive)** neurodevelopmental deficit; chronic and lifelong. Complications are managed symptomatically.

**Prognostic factors.** Severity of baseline intellectual disability and seizure control are the main determinants of functional outcome. No validated molecular prognostic biomarkers; given the small cohort, genotype–phenotype correlation (beyond "all LoF") is not well established.

---

## 12. Treatment

**There is no disease-specific or disease-modifying therapy.** Management is **supportive and symptomatic**, following standard practice for syndromic neurodevelopmental disorders.

| Domain | Intervention | NCIT suggestion |
|---|---|---|
| Epilepsy/seizures | Antiseizure medications (chosen by seizure type) | NCIT:C264 (Anticonvulsant Agent) |
| Developmental delay | Early intervention, special education | NCIT:C15215 (Rehabilitation Therapy) |
| Motor/functional | Physical and occupational therapy | NCIT:C15351 (Physical Therapy); NCIT:C15402 (Occupational Therapy) |
| Communication | Speech/language therapy | NCIT (Speech Therapy) |
| Skeletal (scoliosis) | Orthopedic management/monitoring | NCIT:C157866 (Orthopedic Procedure) |
| Dental (gingival hyperplasia) | Dental care | — |
| Renal abnormalities | Nephrology monitoring/management | — |

- **Pharmacogenomics:** No disease-specific pharmacogenomic guidance; standard antiseizure medication selection applies.
- **Advanced therapeutics (gene/cell/RNA therapy, targeted/immunotherapy):** None available or in trials for NEDDFAS.
- **Experimental treatments / clinical trials:** None identified (no NCT-registered NEDDFAS-specific trials).
- **Treatment outcomes / adverse events:** Not formally studied for this disorder; outcomes relate to symptomatic control.

---

## 13. Prevention

NEDDFAS cannot be prevented at the individual (mutation) level; prevention focuses on **reproductive genetic risk management**.

- **Primary prevention:** Not applicable (genetic disorder).
- **Genetic counseling:** The cornerstone of prevention for at-risk families, particularly **consanguineous couples** and known carriers. Counseling covers the 25% recurrence risk per pregnancy for carrier couples.
- **Carrier / cascade testing:** Available once the familial variant is known.
- **Prenatal diagnosis and preimplantation genetic testing (PGT):** Available for families with a known *EMC10* variant.
- **Immunization / behavioral / public-health / environmental interventions:** Not applicable.
- **Tertiary prevention:** Prevent complications via seizure control, orthopedic surveillance for scoliosis, renal monitoring, and dental care.

---

## 14. Other Species / Natural Disease

- **Taxonomy / naturally occurring disease:** No naturally occurring *EMC10*-related disease is catalogued in companion animals or wildlife (no OMIA entry identified). **Not applicable** beyond experimental models.
- **Orthologous genes:** *EMC10* is conserved; mouse *Emc10* (used in the angiogenesis/myocardial-infarction work, [PMID: 28931551](https://pubmed.ncbi.nlm.nih.gov/28931551/)). The **EMC complex itself is deeply conserved** from yeast and fungi (e.g., *Magnaporthe oryzae* MoEmc2/MoEmc5, [PMID: 36772852](https://pubmed.ncbi.nlm.nih.gov/36772852/)) through *Drosophila* ([PMID: 34918864](https://pubmed.ncbi.nlm.nih.gov/34918864/)) to humans, underscoring strong **evolutionary conservation of the disease-relevant mechanism** (membrane-protein insertion).
- **Zoonotic potential / transmission:** Not applicable (non-communicable genetic disorder).

---

## 15. Model Organisms

No dedicated published NEDDFAS (*EMC10*-specific) disease model recapitulating the full human syndrome was identified at the time of research. However, the **EMC complex** has been extensively studied across model systems, providing strong mechanistic support:

| System | Finding | Relevance | Reference |
|---|---|---|---|
| Mouse (*Emc10*) | Secreted Emc10 is a bone-marrow-derived angiogenic growth factor promoting tissue repair after myocardial infarction | Documents the secreted-isoform signaling branch | [PMID: 28931551](https://pubmed.ncbi.nlm.nih.gov/28931551/) |
| *Drosophila* | EMC required for biogenesis of Xport-A, Rhodopsin-1, and TRP channel; EMC needed for TMD membrane insertion | Demonstrates EMC's essential role in membrane-protein (incl. ion channel) biogenesis | [PMID: 34918864](https://pubmed.ncbi.nlm.nih.gov/34918864/) |
| Fungus (*M. oryzae*) | EMC loss reduces membrane-protein steady-state levels, impairs autophagy, cell-wall integrity, pathogenicity | Shows conserved EMC function and client-protein dependence | [PMID: 36772852](https://pubmed.ncbi.nlm.nih.gov/36772852/) |
| Yeast→human (structural) | Cryo-EM structures reveal conserved EMC architecture and substrate TMD-binding pocket | Structural basis of insertase mechanism | [PMID: 33629497](https://pubmed.ncbi.nlm.nih.gov/33629497/); [PMID: 35850079](https://pubmed.ncbi.nlm.nih.gov/35850079/) |

**Applications and gaps.** These models establish *what EMC does* but do not yet model the *EMC10-deficient neurodevelopmental phenotype*. A faithful mammalian neuronal or whole-animal *Emc10*-LoF model (knockout/knock-in of the patient allele) that reproduces developmental delay/seizures is a key unmet need (see Follow-up).

---

## Mechanistic Model / Interpretation

NEDDFAS is best understood as a **membrane-protein biogenesis disorder of the endoplasmic reticulum**. The unifying model: biallelic *EMC10* LoF → reduced/degraded EMC10 protein → diminished EMC insertase capacity → impaired insertion and folding of tail-anchored and multipass membrane clients → cell-biological dysfunction most clinically evident in neurons (ID, GDD, seizures) with additional craniofacial, renal, and skeletal manifestations. Steps 1–2 are **demonstrated** in patient material ([PMID: 33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/)); steps 3–5 are **inferred** from robust, cross-species EMC biology ([PMID: 35684946](https://pubmed.ncbi.nlm.nih.gov/35684946/), [PMID: 34918864](https://pubmed.ncbi.nlm.nih.gov/34918864/), [PMID: 33629497](https://pubmed.ncbi.nlm.nih.gov/33629497/), [PMID: 36041783](https://pubmed.ncbi.nlm.nih.gov/36041783/)). A secondary, speculative branch involves loss of the **secreted EMC10 isoform** and its small-GTPase→PAK→p38-MAPK-MK2 angiogenic signaling ([PMID: 28931551](https://pubmed.ncbi.nlm.nih.gov/28931551/)).

The **close parallel to EMC1-related disease** ([PMID: 26942288](https://pubmed.ncbi.nlm.nih.gov/26942288/)) is informative: both are EMC-subunit disorders causing syndromic ID, but EMC1 disease prominently features cerebellar atrophy/degeneration and can be dominant or recessive, whereas EMC10 disease is recessive and static. This suggests that **different EMC subunits, when disrupted, produce overlapping but distinguishable neurodevelopmental syndromes**, reflecting partially distinct client repertoires or dosage sensitivities.

---

## Evidence Base

| PMID | Paper (abbrev.) | Role in this report |
|---|---|---|
| [33531666](https://pubmed.ncbi.nlm.nih.gov/33531666/) | Recurrent homozygous *EMC10* frameshift → syndrome (Shao 2021) | **Foundational.** Defines disease, core phenotype, recurrent c.287delG, two founder haplotypes/hypermutable site, LoF molecular consequence |
| [35684946](https://pubmed.ncbi.nlm.nih.gov/35684946/) | Biallelic *EMC10* LoF → mild-to-severe ID (Kaiyrzhanov/Maroofian 2022) | **Confirmatory/expansion.** 10 more patients, 5 new LoF variants; EMC10 function definition; EMC1 overlap |
| [40150819](https://pubmed.ncbi.nlm.nih.gov/40150819/) | Gingival hyperplasia & scoliosis as added features (Forest-St-Onge 2025) | Multisystem phenotype (microcephaly, renal); c.343C>T; exome reanalysis |
| [40741735](https://pubmed.ncbi.nlm.nih.gov/40741735/) | *EMC10* dual molecular effects (Bolat 2025) | Diagnostic pathway; c.431del; possible dual molecular effect |
| [28931551](https://pubmed.ncbi.nlm.nih.gov/28931551/) | Secreted EMC10 angiogenic factor (Reboll 2017) | Secreted-isoform signaling branch (GTPase/PAK/p38-MAPK-MK2) |
| [26942288](https://pubmed.ncbi.nlm.nih.gov/26942288/) | *EMC1* variants in NDD (Harel 2016) | Differential diagnosis; EMC-subunit disease comparison |
| [37417332](https://pubmed.ncbi.nlm.nih.gov/37417332/) | Membrane insertases at a glance | EMC as Oxa1-family insertase |
| [33629497](https://pubmed.ncbi.nlm.nih.gov/33629497/) | Cryo-EM of EMC | Structural basis of insertase; substrate TMD pocket |
| [36041783](https://pubmed.ncbi.nlm.nih.gov/36041783/) | GET vs EMC TA-insertion pathways | Pathway context |
| [35850079](https://pubmed.ncbi.nlm.nih.gov/35850079/) | Cryo-EM of TA biogenesis | Conserved insertase core |
| [34918864](https://pubmed.ncbi.nlm.nih.gov/34918864/) | EMC & Xport-A/Rh1/TRP (Drosophila) | Model-organism evidence for client biogenesis incl. channels |
| [36772852](https://pubmed.ncbi.nlm.nih.gov/36772852/) | Fungal EMC & membrane proteins/autophagy | Conserved function; autophagy link |

**Consistency.** All disease-focused reports agree on autosomal recessive biallelic LoF of *EMC10* as the cause and converge on the GDD/ID + variable seizures + dysmorphism core, with progressive broadening of the phenotype (microcephaly, renal, skeletal, dental) as more cases accrue. The mechanistic literature (structural, model-organism) consistently supports the EMC insertase role, though direct demonstration in human NEDDFAS neurons is still lacking.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** ~25–30 patients across <15 families; frequencies are qualitative ("variable"), and robust genotype–phenotype correlations and prevalence/incidence are unavailable.
2. **Inferred downstream mechanism.** Steps beyond reduced EMC10 protein (insertase-capacity loss, specific affected clients, neuronal consequences) are **inferred from EMC biology**, not directly demonstrated in NEDDFAS patient neurons. The specific client proteins whose mislocalization drives the neurodevelopmental phenotype are unknown.
3. **No animal model of the syndrome.** Existing *Emc10*/EMC models address function or angiogenesis, not the human neurodevelopmental disorder.
4. **Unexplained variability.** No modifier genes or epigenetic factors identified to explain the mild-to-severe range of ID.
5. **Secreted-isoform branch speculative.** The contribution (if any) of lost secreted EMC10 signaling to the human phenotype is untested.
6. **"Dual molecular effects"** ([PMID: 40741735](https://pubmed.ncbi.nlm.nih.gov/40741735/)) is intriguing but not mechanistically resolved.
7. **No therapeutics.** No disease-modifying treatment or trials.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a patient-allele mouse model** (knock-in *Emc10* p.Gly96Alafs*9 or conditional neuronal knockout) and assess developmental, behavioral, EEG/seizure, and craniofacial/renal phenotypes to test the inferred causal chain.
2. **Patient-derived iPSC neurons/organoids:** quantify EMC assembly/stability and perform surfaceome/membrane-proteomics (e.g., quantitative MS) to identify which EMC client proteins (receptors, ion channels, transporters) are depleted — directly testing step 4.
3. **Electrophysiology** in patient neurons/organoids to connect client-protein deficits to the inferred excitability changes underlying seizures.
4. **Natural-history registry** for *EMC10* patients to establish prevalence, age-dependent features, seizure semiology, QoL, and genotype–phenotype correlation.
5. **Test the secreted-isoform branch** by measuring circulating EMC10 and vascular/angiogenic readouts in patients vs controls.
6. **Systematic EMC10 vs EMC1 comparison** (and other EMC subunits) to map subunit-specific client dependencies that explain the distinct clinical syndromes.
7. **Variant curation:** submit all reported alleles to ClinVar with ACMG classifications and establish an *EMC10* gene–disease ClinGen curation to standardize diagnosis.

---

*Report compiled from 6 confirmed findings and 12 reviewed papers over a 5-iteration investigation. Evidence source types: human clinical (case series/reports), model organism (mouse, Drosophila, fungus), and structural/computational (cryo-EM). All mechanistic steps are flagged as demonstrated, inferred, or speculative.*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Dysmorphic_Facies_And_Variable_Seizures-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Dysmorphic_Facies_And_Variable_Seizures-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 27 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0031011` (2 mentions) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with dysmorphic facies and variable seizures**
- `NCIT:C157866` (1 mention) - the report calls it "Orthopedic Procedure"; NCIT calls it **Gluten Free Diet**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000276` (1 mention) - the report calls it "Facial dysmorphism (elongated/long face)"; HP calls it **Long face**, and lists "Vertical elongation of face" among its other names
- `HP:0000077` (1 mention) - the report calls it "Renal abnormalities"; HP calls it **Abnormality of the kidney**, and lists "Renal anomalies" among its other names
- `HP:0000212` (1 mention) - the report calls it "Gingival hyperplasia"; HP calls it **Gingival overgrowth**, and lists "Gingival hyperplasia" among its other names
- `GO:0045050` (1 mention) - the report calls it "protein insertion into ER membrane"; GO calls it **protein insertion into ER membrane by stop-transfer membrane-anchor sequence**, and lists "protein-ER insertion by stop-transfer membrane-anchor sequence" among its other names
- `UBERON:0000955` (1 mention) - the report calls it "Primary:** Central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Secondary:** Kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `GO:0072546` (1 mention) - the report calls it "EMC/ER membrane protein complex"; GO calls it **EMC complex**, and lists "ER membrane protein complex" among its other names
- `NCIT:C15215` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Cryosurgery**, and lists "Ablation, Cryo" among its other names