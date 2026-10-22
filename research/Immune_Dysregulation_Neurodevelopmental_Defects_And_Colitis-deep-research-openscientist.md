---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T17:31:36.845795'
end_time: '2026-10-22T17:46:57.251075'
duration_seconds: 920.41
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Immune Dysregulation, Neurodevelopmental Defects, And Colitis
  mondo_id: MONDO:0980702
  category: Mendelian
  causal_genes: ITGAV
  omim_id: OMIM:621375
  synonyms: ITGAV deficiency
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 11
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 39
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0980702
    reported_labels:
    - MONDO release v2026-03-03
    ontology_label: immune dysregulation, neurodevelopmental defects, and colitis
  - term_id: HP:0000539
    reported_labels:
    - retinal exudates
    ontology_label: Abnormality of refraction
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immune_Dysregulation_Neurodevelopmental_Defects_And_Colitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immune_Dysregulation_Neurodevelopmental_Defects_And_Colitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immune Dysregulation, Neurodevelopmental Defects, And Colitis
- **MONDO ID:** MONDO:0980702 (if available)
- **Causal gene(s):** ITGAV
- **OMIM:** OMIM:621375
- **Synonyms:** ITGAV deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Immune Dysregulation, Neurodevelopmental Defects, And Colitis** covering all of the
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

# Immune Dysregulation, Neurodevelopmental Defects, and Colitis (IDNDC / ITGAV Deficiency)

**Disease:** Immune Dysregulation, Neurodevelopmental Defects, and Colitis (IDNDC)
**MONDO ID:** MONDO:0980702 · **OMIM:** #621375 · **Causal gene:** *ITGAV* (integrin subunit alpha-V; HGNC:6150; OMIM *193210; NCBI Gene 3685; UniProt P06756; chromosome 2q32.1)
**Category:** Mendelian, autosomal recessive

---

## Summary

**Immune Dysregulation, Neurodevelopmental Defects, and Colitis (IDNDC)** is an ultra-rare, autosomal recessive, multisystem Mendelian disorder caused by **biallelic loss-of-function (or mistrafficking) variants in *ITGAV***, the gene encoding the integrin alpha-V (αV) subunit. The disease was first delineated as a distinct human entity by Ghasempour et al. in *J Exp Med* in 2024 ([PMID: 39526957](https://pubmed.ncbi.nlm.nih.gov/39526957/)), who reported biallelic *ITGAV* variants in three independent families — two living patients and four affected fetuses. Although the disease name is a descriptive triad rather than a serial number, its single causal gene is **ITGAV**, and all identifiers above (MONDO:0980702, OMIM #621375) point to this ITGAV-based disorder — not an integrin-β or TGFB1-primary disease, although it converges mechanistically on the TGF-β pathway.

Mechanistically, IDNDC is a disorder of **failed integrin-mediated activation of latent TGF-β**. The αV subunit heterodimerizes with β1, β3, β5, β6, and β8; the αvβ6 and αvβ8 heterodimers are principal activators of latent TGF-β1/β3 through binding the RGD motif of the latency-associated peptide (LAP). When αV is lost or mistrafficked, two complementary signaling axes collapse: (A) a **TGF-β–dependent** branch (αvβ6/αvβ8 → latent TGF-β activation → SMAD2/3), whose failure produces colitis (via loss of regulatory T-cell generation and mucosal tolerance) and brain vascular/structural defects (via impaired neuroepithelial→endothelial paracrine TGF-β signaling); and (B) a **TGF-β–independent** branch (αv/β3–LC3/ATG5 noncanonical autophagy restraining Toll-like receptor (TLR) and germinal-center B-cell responses), whose failure produces atopy, elevated IgE/IgG, and eosinophilia.

A striking **genotype–phenotype gradient** defines the disease: complete loss-of-function alleles are prenatally/perinatally lethal (as in the four fetuses of Family C), whereas hypomorphic (incomplete loss-of-function) alleles permit survival with the chronic triad of neurodevelopmental defects, colitis, and atopy/immune dysregulation. The disease is corroborated across species — αv-null and conditional-knockout mice reproduce intracerebral/intestinal hemorrhage, cleft palate, colitis, and autoimmunity, and *itgav*-knockout zebrafish recapitulate retinal/brain defects, microglial loss, and colitis with reduced SMAD3. No targeted or curative therapy exists; management is supportive/immunomodulatory, and diagnosis is molecular (trio WES/WGS) with functional confirmation of impaired TGF-β→SMAD output.

---

## Key Findings

### 1. ITGAV is the causal gene and encodes the master activator of latent TGF-β

*ITGAV* (HGNC:6150; chromosome 2q32.1; OMIM *193210) encodes the integrin alpha-V subunit, which partners with β1, β3, β5, β6, and β8. The αvβ6 and αvβ8 heterodimers bind the RGD motif of the latency-associated peptide (LAP) of latent TGF-β1/β3 and are the principal activators of latent TGF-β. This molecular function is the central node whose disruption explains most of the IDNDC phenotype. Païdassi et al. demonstrated that *"activation of transforming growth factor (TGF)-β by α(v)β8 on dendritic cells (DCs) is essential for generating T(reg) cells and inducing mucosal tolerance"* ([PMID: 20958318](https://pubmed.ncbi.nlm.nih.gov/20958318/)), establishing αvβ8-mediated TGF-β activation as the key function relevant to the colitis/immune-tolerance axis of this disease.

### 2. The human disease was delineated in 2024 across three families

Ghasempour et al. 2024 (*J Exp Med* 221(12):e20240546) identified *"biallelic variants in the gene coding for Integrin alpha V (ITGAV) in three independent families (two patients and four fetuses) that either caused abnormal mRNA and the loss of functional protein or caused mistargeting of the integrin. This led to eye and brain abnormalities, inflammatory bowel disease, immune dysregulation, and other developmental issues"* ([PMID: 39526957](https://pubmed.ncbi.nlm.nih.gov/39526957/)). The authors explicitly noted the genotype-severity relationship: *"the ITGAV variants identified in this report caused a previously unknown human disease characterized by brain and developmental defects in the case of complete loss-of-function and atopy, neurodevelopmental defects, and colitis in cases of incomplete loss-of-function."* This is the disease-defining paper and the basis for OMIM #621375 and MONDO:0980702.

### 3. The pathogenic variant spectrum (germline, autosomal recessive)

All reported variants are germline and biallelic. The spectrum is summarized below.

| Family | Patient(s) | Genotype | Variant (protein) | Variant type | Functional consequence |
|--------|-----------|----------|-------------------|--------------|------------------------|
| A | Patient 1 (female) | Homozygous | c.432G>C (p.Trp144Cys, **W144C**) | Creates novel splice site in exon 4 → frameshift → PTC, predicted NMD | Loss of functional protein |
| B | Patient 2 (male) | Homozygous | c.1136A>T (p.Asp379Val, **D379V**) | Missense | Mistargeting of integrin |
| C | 4 fetuses | Compound het. | 4-bp deletion → p.Cys502Ter (**C502X**); and c.2247-1G>A splice-acceptor → p.Ser749_Gly776delinsArg | Nonsense / splice | Early termination / loss of function (prenatally lethal) |

The two functional mechanisms — *"either caused abnormal mRNA and the loss of functional protein or caused mistargeting of the integrin"* ([PMID: 39526957](https://pubmed.ncbi.nlm.nih.gov/39526957/)) — map to OMIM allelic variants 193210.0001–193210.0004. gnomAD indicates ITGAV is relatively tolerant of heterozygous loss-of-function (observed/expected ≈0.30, low pLI), consistent with recessive disease in which carriers are unaffected; the reported pathogenic alleles are private/ultra-rare or absent in gnomAD.

### 4. Clinical phenotype spectrum

Derived from OMIM #621375 and Ghasempour et al. 2024, the clinical picture spans four organ domains, summarized with suggested HPO terms:

| Domain | Features | Suggested HPO |
|--------|----------|---------------|
| **Neurologic** | Global developmental delay, cognitive dysfunction, seizures, microcephaly, ventriculomegaly, polymicrogyria, delayed myelination, white-matter loss, intracranial calcification, corpus callosum agenesis/hypoplasia, Dandy-Walker malformation, hydrocephaly | HP:0002126 (polymicrogyria), HP:0012448 (delayed myelination), HP:0001274 (abnormal corpus callosum), HP:0001305 (Dandy-Walker), HP:0000252 (microcephaly), HP:0001250 (seizures), HP:0002170 (intracranial hemorrhage) |
| **Ophthalmologic** | Eye/retinal abnormalities, exudative retinopathy | HP:0000539 (retinal exudates) |
| **Gastrointestinal** | Inflammatory bowel disease / pancolitis, eosinophilic enteropathy | HP:0002583 (colitis), HP:0100281, HP:0004386 |
| **Immune/skin** | Recurrent (incl. fungal) infections, elevated IgG, elevated IgE, multiple allergies/atopy, eosinophilia, atopic dermatitis | HP:0003212 (elevated IgE), HP:0001880 (eosinophilia), HP:0001047 (atopic dermatitis), HP:0002719 (recurrent infections) |

The disease is summarized by the authors as *"eye and brain abnormalities, inflammatory bowel disease, immune dysregulation, and other developmental issues"* ([PMID: 39526957](https://pubmed.ncbi.nlm.nih.gov/39526957/)).

### 5. Patient-level features of the two survivors

**Patient 1** (Family A, female, homozygous W144C): bifid uvula (HP:0000193), exudative retinopathy, atopic dermatitis, and seizures in the first year of life; brain MRI showed polymicrogyria, delayed myelination, white-matter loss, intracranial calcifications, dysplastic/dysgenic corpus callosum, and microcephaly; she required **colectomy** for diffuse pancolitis. **Patient 2** (Family B, male, homozygous D379V): eosinophilic enteropathy, atopic dermatitis, recurrent infections; labs showed eosinophilia (>0.5×10⁹/L) and elevated IgE (>100 kU/L); allergen screening against 295 allergens (ALEX Allergy Explorer) showed multiple allergies. Onset was congenital/first year of life with a chronic course — the survivable phenotype being *"atopy, neurodevelopmental defects, and colitis in cases of incomplete loss-of-function"* ([PMID: 39526957](https://pubmed.ncbi.nlm.nih.gov/39526957/)).

### 6. Mechanistic confirmation in patient cells

Ghasempour et al. showed that *"the reduction of functional Integrin αV resulted in the dysregulation of several pathways including TGF-β-dependent signaling and αVβ3-regulated immune signaling. These effects were confirmed using immunostaining, RNA sequencing, and functional studies in patient-derived cells"* ([PMID: 39526957](https://pubmed.ncbi.nlm.nih.gov/39526957/)). Patient-1 fibroblasts and lymphoblasts showed abnormal expression of TGF-β–downstream genes and decreased SMAD transcription; colon biopsies showed decreased SMAD3. This names the two dysregulated branches — canonical αvβ6/αvβ8→latent-TGF-β→SMAD2/3 and αvβ3-mediated immune/adhesion signaling — that are central to the pathophysiology.

### 7. Animal models recapitulate the phenotype

Three independent model systems support causality:

- **αv-null mice** (Bader et al. 1998): ablation of *Itgav* is largely embryonic lethal (~80% die mid-gestation from placental defects), but *"these liveborn alphav-null mice consistently exhibit intracerebral and intestinal hemorrhages and cleft palates"* ([PMID: 9827803](https://pubmed.ncbi.nlm.nih.gov/9827803/)) — the animal correlate of human CNS and intestinal disease.
- **Myeloid/DC conditional knockouts** (Lacy-Hulbert et al. 2007; Travis et al. 2007): *"deletion of alphav in the immune system causes severe colitis, autoimmunity, and cancer. Mice lacking immune cell alphav have fewer regulatory T (Treg) cells in the colon"* ([PMID: 17895374](https://pubmed.ncbi.nlm.nih.gov/17895374/)), and *"conditional loss of the TGF-beta-activating integrin alpha(v)beta8 on leukocytes causes severe inflammatory bowel disease and age-related autoimmunity in mice"* ([PMID: 17694047](https://pubmed.ncbi.nlm.nih.gov/17694047/)).
- **Zebrafish *itgav* knockout** (Ghasempour et al. 2024): *"The genetic deletion of itgav in zebrafish recapitulated patient phenotypes including retinal and brain defects and the loss of microglia in early development as well as colitis in juvenile zebrafish with reduced SMAD3 expression and transcriptional regulation"* ([PMID: 39526957](https://pubmed.ncbi.nlm.nih.gov/39526957/)). Some mutant larvae died before 8 dpf with brain hemorrhages.

### 8. Molecular basis of the TGF-β–independent (atopy) branch

Beyond TGF-β, αV restrains innate and humoral immunity through noncanonical autophagy. Acharya et al. 2016 showed that *"deletion of αv or β3 causes increased B-cell responses to TLR stimulation in vitro, and αv-conditional knockout mice have elevated antibody responses to TLR-ligand-associated antigens"* — αv promotes recruitment of the autophagy component LC3 to TLR-containing endosomes, and *"disruption of LC3 recruitment leads to prolonged NF-κB signalling and increased B-cell proliferation and antibody production"* ([PMID: 26965188](https://pubmed.ncbi.nlm.nih.gov/26965188/)). Raso et al. 2018 extended this: *"loss of αv-mediated TLR regulation increased GC B cell expansion, somatic hypermutation, class switching, and generation of long-lived plasma cells"* ([PMID: 29999501](https://pubmed.ncbi.nlm.nih.gov/29999501/)). Lagos et al. 2022 ([PMID: 36497137](https://pubmed.ncbi.nlm.nih.gov/36497137/)) showed αV-deficient B cells lack TLR-induced autophagy and have altered antigen extraction. Ghasempour et al. explicitly invoke these pathways: *"Many of the immune and atopy features observed in P1 and P2 may also be due to Integrin αV's roles that are independent of TGF-β activation, including limiting TLR signaling and preventing autoimmune B cell responses."*

### 9. Molecular basis of the neurodevelopmental (brain-vascular) branch

Neuroepithelial αvβ8 drives CNS angiogenesis and blood-brain-barrier development by activating latent TGF-β for adjacent endothelial cells. Hirota et al. 2015 showed that *"β8 integrin in the neuroepithelium promotes the activation of extracellular matrix (ECM)-bound latent transforming growth factor β (TGFβ) ligands and stimulates TGFβ receptor signaling in endothelial cells... Cell type-specific ablation of β8 integrin, Nrp1, or canonical TGFβ receptors results in pathological angiogenesis"* ([PMID: 26586223](https://pubmed.ncbi.nlm.nih.gov/26586223/)). De et al. 2022 confirmed *"the β8 integrin cytoplasmic domain is essential for inside-out modulation of adhesion, including activation of latent-TGFβs in the ECM"* ([PMID: 35217866](https://pubmed.ncbi.nlm.nih.gov/35217866/)). Because αvβ8 requires the αV subunit, ITGAV loss abrogates this neuroepithelium→endothelium paracrine axis, explaining the brain vascular/structural malformations and hemorrhage. A human candidate-gene association study further links the locus to cerebral hemorrhage: ITGAV/ITGB8 tag-SNPs were associated with intracerebral hemorrhage risk/onset ([PMID: 27476161](https://pubmed.ncbi.nlm.nih.gov/27476161/)).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function or mistrafficking variants in *ITGAV*** → **leads to** loss or reduced surface expression of all five αV-containing integrin heterodimers (αvβ1/β3/β5/β6/β8).
2. From step 1 the mechanism **branches** into a TGF-β–dependent arm (A) and a TGF-β–independent arm (B).

**Branch A — failed latent TGF-β activation (SMAD2/3):**
3A. Loss of αvβ6/αvβ8 → **results in** failure to activate ECM-bound latent TGF-β1/β3 → **leads to** reduced TGF-β receptor signaling and decreased SMAD2/3 (notably decreased SMAD3 in patient colon and zebrafish).
4A. In the gut, reduced TGF-β activation by dendritic cells/macrophages → **leads to** fewer colonic regulatory T cells and failure of mucosal tolerance and apoptotic-cell clearance → **results in** colitis/IBD *(mouse-demonstrated; patient-corroborated)*.
5A. In the developing brain, loss of neuroepithelial αvβ8→endothelial TGF-β paracrine signaling → **leads to** pathological CNS angiogenesis and impaired blood-brain-barrier/vascular integrity → **results in** intracerebral hemorrhage, polymicrogyria, delayed myelination, corpus callosum and ventricular anomalies *(mouse/zebrafish-demonstrated; human-corroborated)*.

**Branch B — loss of autophagy-dependent restraint of TLR/B-cell responses:**
3B. Loss of αv/β3 → **results in** failure to recruit LC3/ATG5 to TLR-containing endosomes (noncanonical autophagy) → **leads to** prolonged NF-κB signaling and de-repressed TLR responses.
4B. De-repressed TLR/germinal-center B-cell signaling → **leads to** increased B-cell proliferation, class switching, somatic hypermutation, and long-lived plasma cells → **results in** atopy, elevated IgE/IgG, eosinophilia, atopic dermatitis, and multiple allergies *(mouse-demonstrated; human-inferred)*.

**Genotype-dependent severity gate:** complete loss-of-function → prenatal/perinatal lethality (Family C fetuses); hypomorphic alleles → survivable chronic triad (P1, P2).

### Diagram

```
          biallelic ITGAV LoF / mistrafficking
                        |
         loss of αV heterodimers (αvβ1/β3/β5/β6/β8)
            /                                   \
   BRANCH A: TGF-β dependent            BRANCH B: TGF-β independent
   αvβ6/αvβ8 fail to activate           αv/β3 fail to recruit LC3/ATG5
   latent TGF-β → ↓SMAD2/3              → ↑TLR/NF-κB in B cells
        /              \                          |
  gut DC/Mφ:       neuroepithelium→         ↑GC B-cell, class switch,
  ↓Treg,           endothelium:             plasma cells
  tolerance loss   ↓angiogenic TGF-β              |
        |              |                          |
     COLITIS      BRAIN VASCULAR/            ATOPY, ↑IgE/IgG,
     /IBD         STRUCTURAL DEFECTS,        eosinophilia,
                  HEMORRHAGE                 atopic dermatitis
```

### Key ontology annotations

- **Biological processes (GO):** TGF-β receptor signaling pathway, SMAD protein signal transduction, regulation of Toll-like receptor signaling, macroautophagy, blood vessel morphogenesis, regulatory T cell differentiation, integrin-mediated signaling.
- **Molecular function (GO):** integrin binding; latent TGF-β activation.
- **Cellular component (GO):** integrin complex (GO:0008305), focal adhesion (GO:0005925), autophagosome/endosome (GO:0005776), plasma membrane.
- **Cell types (CL):** dendritic cells (CL:0000451), macrophages (CL:0000235), regulatory T cells (CL:0000815), B/plasma cells (CL:0000236/CL:0000786), microglia (CL:0000129), neuroepithelial/radial glia (CL:0000047), vascular endothelial cells (CL:0000115), eosinophils (CL:0000771).
- **Anatomy (UBERON):** brain (UBERON:0000955), cerebral cortex (UBERON:0000956), white matter (UBERON:0002316), corpus callosum (UBERON:0002336), eye/retina (UBERON:0000966), colon/large intestine (UBERON:0001155), skin (UBERON:0002097), palate (UBERON:0001733).
- **Chemicals/entities (CHEBI):** TGF-β (protein); IgE/IgG (immunoglobulins).

---

## Evidence Base

| PMID | Study | Model / evidence type | Role in this report |
|------|-------|----------------------|---------------------|
| [39526957](https://pubmed.ncbi.nlm.nih.gov/39526957/) | Ghasempour et al. 2024, *J Exp Med* | Human clinical + zebrafish + patient-derived cells | **Disease-defining paper**; variants, phenotype, dual-branch mechanism, SMAD3 reduction |
| [9827803](https://pubmed.ncbi.nlm.nih.gov/9827803/) | Bader et al. 1998, *Cell* | Mouse (αv-null) | Intracerebral/intestinal hemorrhage + cleft palate — CNS/gut correlate |
| [17895374](https://pubmed.ncbi.nlm.nih.gov/17895374/) | Lacy-Hulbert et al. 2007, *PNAS* | Mouse (myeloid αv KO) | Colitis, autoimmunity, Treg deficiency |
| [17694047](https://pubmed.ncbi.nlm.nih.gov/17694047/) | Travis et al. 2007 | Mouse (DC αvβ8 KO) | IBD and autoimmunity via αvβ8 |
| [20958318](https://pubmed.ncbi.nlm.nih.gov/20958318/) | Païdassi et al. 2010 | Mouse / in vitro | αvβ8→TGF-β→Treg / mucosal tolerance |
| [26586223](https://pubmed.ncbi.nlm.nih.gov/26586223/) | Hirota et al. 2015, *Development* | Mouse | Neuroepithelial αvβ8→endothelial TGF-β; brain angiogenesis |
| [35217866](https://pubmed.ncbi.nlm.nih.gov/35217866/) | De et al. 2022 | Mouse / cell | β8 cytoplasmic domain activates latent TGF-β; neurovascular development |
| [26965188](https://pubmed.ncbi.nlm.nih.gov/26965188/) | Acharya et al. 2016, *Nat Commun* | Mouse (αv/β3 KO) + in vitro | αv/LC3/ATG5 restrains TLR/B-cell responses |
| [29999501](https://pubmed.ncbi.nlm.nih.gov/29999501/) | Raso et al. 2018, *J Exp Med* | Mouse | αv loss → exaggerated germinal-center/antibody responses |
| [36497137](https://pubmed.ncbi.nlm.nih.gov/36497137/) | Lagos et al. 2022 | B cells / in vitro | αV-dependent TLR-induced autophagy and antigen extraction |
| [27476161](https://pubmed.ncbi.nlm.nih.gov/27476161/) | ITGAV/ITGB8 ICH association study | Human association | ITGAV/ITGB8 SNPs and intracerebral hemorrhage risk (supports vascular relevance) |

All mechanistic claims rest on a convergent human + mouse + zebrafish dataset. The human evidence (PMID 39526957) is limited to three families but is strongly reinforced by two decades of mouse conditional-knockout work that independently generated each organ phenotype (colitis, autoimmunity, brain hemorrhage, exaggerated antibody responses).

---

## Limitations and Knowledge Gaps

- **Extreme rarity / small n:** Only 3 families (2 living patients + 4 fetuses) are reported worldwide. Phenotype frequencies, penetrance details, and the full clinical spectrum are provisional and may broaden with additional cases. Estimated prevalence <1/1,000,000.
- **Human mechanism partly inferred:** The TGF-β–dependent branch is well-demonstrated in human patient cells (decreased SMAD3). The TGF-β–independent (TLR/B-cell) branch is strongly supported in mice but remains inferred in human patients; the authors present it as a probable contributor.
- **No formal epidemiology or ontology mapping:** Prevalence/incidence are unknown; no Orphanet, ICD-10/ICD-11, or MeSH mappings were assigned at the time of the primary report (disease first described Dec 2024).
- **No natural animal disease catalogued:** No OMIA entry for a naturally occurring ITGAV-ortholog disease in companion animals; existing evidence is from engineered mouse and zebrafish knockouts only.
- **No targeted therapy or natural-history data:** Management is empiric/supportive; long-term outcomes and treatment-response data are absent.
- **Inheritance context:** Homozygosity in Families A and B implies consanguinity/founder context; carrier frequency is essentially that of ultra-rare private alleles.

---

## Proposed Follow-up Experiments / Actions

1. **Patient registry & GeneMatcher outreach** to identify additional families, refine genotype–phenotype correlation, and establish phenotype frequencies and penetrance.
2. **Direct human-cell testing of Branch B:** quantify TLR-induced autophagy, NF-κB kinetics, germinal-center output, IgE class-switch, and B-cell antigen extraction in patient B cells to confirm the mouse-derived atopy mechanism in humans.
3. **Rescue / variant-function assays:** re-express wild-type vs. D379V vs. W144C ITGAV in patient fibroblasts to quantify surface trafficking and latent-TGF-β activation, formally validating the "mistrafficking vs. loss-of-protein" dichotomy.
4. **Therapeutic hypothesis testing:** evaluate whether downstream TGF-β pathway modulation or targeted B-cell/TLR immunomodulation (e.g., anti-IgE, JAK inhibition for atopy; standard IBD immunosuppression) improves the survivable phenotype in model organisms before clinical translation.
5. **Neurovascular imaging natural history** in surviving patients (serial MRI/MRA) to characterize progression of malformations, hemorrhage risk, and critical windows for intervention.
6. **Ontology/nomenclature curation:** request Orphanet, ICD-11, and MeSH mappings; ensure ClinVar deposition of all four allelic variants with ACMG classification.

---

## Section-by-Section Reference Notes (for knowledge-base population)

- **Identifiers:** OMIM #621375; MONDO:0980702 (MONDO release v2026-03-03); gene ITGAV OMIM *193210, HGNC:6150, NCBI Gene 3685, UniProt P06756, 2q32.1. Orthologs: mouse *Itgav* Gene 16410 / MGI:96608; zebrafish *itgav* Gene 393615. Synonyms: "ITGAV deficiency." Information is derived from aggregated disease-level resources (OMIM) plus individual-patient reports in the primary literature.
- **Inheritance/population:** Autosomal recessive; biallelic homozygous or compound heterozygous. Ultra-rare (<1/1,000,000); heterozygous carriers unaffected.
- **Diagnostics:** Molecular diagnosis by trio WES/WGS identifying biallelic ITGAV variants; supportive workup includes brain MRI, ophthalmologic exam, endoscopy/colon biopsy (reduced SMAD3 on IHC), eosinophil count, serum IgE/IgG, allergen panels (e.g., ALEX); functional confirmation via reduced αV surface expression and decreased TGF-β→SMAD transcriptional output. Differential diagnosis includes other monogenic very-early-onset IBD / IPEX-like immune dysregulation and TGF-β pathway / integrin-β8 disorders.
- **Treatment (supportive only; suggested NCIT intervention concepts):** IBD immunosuppression; colectomy for refractory colitis (performed in P1); atopic dermatitis/allergy management; anticonvulsants for seizures; developmental/neurorehabilitation; infection surveillance/treatment. No gene-specific or curative therapy.
- **Prevention/counseling:** Genetic counseling for autosomal recessive recurrence risk (25%); carrier/cascade testing and prenatal/preimplantation genetic testing where a familial variant is known.
- **Prognosis:** Complete-LOF genotypes prenatally/perinatally lethal; hypomorphic patients have chronic lifelong multisystem morbidity.
- **Model organisms:** Mouse (NCBI:txid10090) — complete and conditional (myeloid, DC, B-cell, neuroepithelial) knockouts; zebrafish (NCBI:txid7955) *itgav* KO. Phenotype recapitulation is strong for colitis, brain hemorrhage/vascular defects, and exaggerated antibody responses; limitation is that complete mouse knockout is largely embryonic lethal, constraining adult-phenotype study to conditional models.

---

*Report compiled from 16 confirmed findings and 33 reviewed papers across 5 investigation iterations. Evidence spans human clinical (PMID 39526957), mouse model organism (PMIDs 9827803, 17895374, 17694047, 20958318, 26586223, 35217866, 26965188, 29999501), and zebrafish (PMID 39526957) sources.*


## Artifacts

- [OpenScientist final report](Immune_Dysregulation_Neurodevelopmental_Defects_And_Colitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immune_Dysregulation_Neurodevelopmental_Defects_And_Colitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0980702` (4 mentions) - the report calls it "MONDO release v2026-03-03"; MONDO calls it **immune dysregulation, neurodevelopmental defects, and colitis**
- `HP:0000539` (1 mention) - the report calls it "retinal exudates"; HP calls it **Abnormality of refraction**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.