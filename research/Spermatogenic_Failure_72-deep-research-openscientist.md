---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T12:21:54.381812'
end_time: '2026-10-22T12:36:44.616357'
duration_seconds: 890.23
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Spermatogenic Failure 72
  mondo_id: MONDO:0030809
  category: Mendelian
  causal_genes: WDR19
  omim_id: not recorded
  synonyms: SPGF72; WDR19-related nonsyndromic asthenoteratozoospermia
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
citation_count: 17
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 15
  verified: 14
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 7
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0040031
    reported_labels:
    - Asthenozoospermia
    ontology_label: Chorioretinal hyperpigmentation
  - term_id: UBERON:0010314
    reported_labels:
    - Sperm flagellum
    ontology_label: structure with developmental contribution from neural crest
  - term_id: CL:0000018
    reported_labels:
    - Spermatid
    - "Tissue/cell:** seminiferous epithelium germ cells \u2014 spermatids"
    ontology_label: spermatid
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spermatogenic_Failure_72-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spermatogenic_Failure_72-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 72
- **MONDO ID:** MONDO:0030809 (if available)
- **Causal gene(s):** WDR19
- **OMIM:** not recorded
- **Synonyms:** SPGF72; WDR19-related nonsyndromic asthenoteratozoospermia
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 72** covering all of the
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

# Spermatogenic Failure 72 (SPGF72): A Comprehensive Disease Characterization

**Disease:** Spermatogenic Failure 72 (SPGF72)
**MONDO ID:** MONDO:0030809
**Causal gene:** **WDR19** (WD repeat domain 19 / IFT144; HGNC:18340; NCBI Gene 57728; OMIM *608151; UniProt Q8NEZ3)
**Category:** Mendelian, autosomal recessive

---

## Summary

**Spermatogenic Failure 72 (SPGF72) is an autosomal-recessive, nonsyndromic form of male infertility caused by biallelic loss-of-function variants in the gene *WDR19*** (also called *IFT144*), which encodes a core subunit of the intraflagellar transport-A (IFT-A) complex. It is important to anchor this report on the gene rather than the serial-numbered disease name: *WDR19* is pleiotropic, and biallelic variants more commonly cause severe syndromic ciliopathies (Sensenbrenner/cranioectodermal dysplasia, nephronophthisis, Jeune asphyxiating thoracic dystrophy, Senior-Løken syndrome, retinitis pigmentosa). SPGF72 is the *nonsyndromic* end of this allelic spectrum, presenting purely as asthenoteratozoospermia with multiple morphological abnormalities of the sperm flagella (MMAF), without the renal, skeletal, retinal, or ectodermal features of the syndromic phenotypes.

The disease was defined by a single landmark report ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)) describing a proband from a consanguineous family who carried a homozygous *WDR19* missense variant (c.A3811G, p.K1271E). The proband had progressive sperm motility reduced to zero and flagella showing the MMAF spectrum (absent, short, bent, coiled, irregular-calibre tails). Scanning and transmission electron microscopy showed completely destroyed flagellar axonemal ultrastructure; immunofluorescence showed WDR19 absent from the sperm neck and flagellum, with mislocalization of its IFT partners IFT140 and IFT88. CT imaging and retinal examination explicitly excluded a syndromic ciliopathy, establishing the nonsyndromic nature of the condition.

Mechanistically, loss of WDR19 cripples retrograde intraflagellar transport within the six-subunit IFT-A complex during spermiogenesis, preventing proper assembly and maintenance of the sperm flagellar axoneme and abolishing motility. The inheritance is recessive, consistent with population genetics data (gnomAD) showing that heterozygous WDR19 loss-of-function is well tolerated. There is no disease-modifying pharmacotherapy; however, intracytoplasmic sperm injection (ICSI) bypasses the motility defect and achieved clinical pregnancy in the index couple, consistent with favorable ICSI outcomes for MMAF generally. The principal limitation of current knowledge is that the human nonsyndromic phenotype rests on a single reported proband, and no dedicated *Wdr19* testis-specific knockout model has been published.

---

## Key Findings

### Finding 1 — Biallelic *WDR19* mutation causes nonsyndromic asthenoteratozoospermia (SPGF72)

Whole-exome sequencing of 65 individuals with asthenoteratospermia identified a proband carrying a homozygous *WDR19* variant c.A3811G (p.K1271E), inherited within a consanguineous family ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)). The authors state directly: *"We identified WDR19 as a novel pathogenic gene for male infertility caused by asthenoteratospermia in the absence of other ciliopathic phenotypes."* The clinical and laboratory picture was characteristic of MMAF: progressive motility decreased to zero, and the sperm flagella displayed multiple morphological abnormalities. SEM and TEM demonstrated completely destroyed flagellar ultrastructure, while immunofluorescence showed WDR19 absent from the sperm neck/flagella and its IFT-A partner IFT140 and IFT-B component IFT88 mislocalized. Critically, CT imaging and retinal examination excluded syndromic ciliopathy features, establishing the disorder as **nonsyndromic**. The couple achieved clinical pregnancy via ICSI: *"the MMAF subject harboring WDR19 variant and his partner successfully achieved clinical pregnancy through intracytoplasmic sperm injection (ICSI)."*

This single report is the defining evidence for SPGF72 as a discrete clinical entity and anchors the gene–disease relationship (WDR19 → nonsyndromic MMAF).

### Finding 2 — *WDR19* is a pleiotropic IFT-A gene; the allelic spectrum ranges from severe syndromic ciliopathy to isolated SPGF72

*WDR19* (IFT144) encodes a core component of the IFT-A complex required for retrograde intraflagellar transport. Biallelic *WDR19* variants cause a broad **syndromic ciliopathy spectrum**: Sensenbrenner syndrome / cranioectodermal dysplasia (CED4), nephronophthisis (NPHP13), Jeune asphyxiating thoracic dystrophy / short-rib thoracic dysplasia, Caroli disease, and retinal dystrophy / Senior-Løken syndrome ([PMID: 28621010](https://pubmed.ncbi.nlm.nih.gov/28621010/); [PMID: 29134781](https://pubmed.ncbi.nlm.nih.gov/29134781/); [PMID: 28332779](https://pubmed.ncbi.nlm.nih.gov/28332779/)). A review of renal phenotypes states: *"WDR19 has been reported as a causative gene of nephronophthisis-related ciliopathies. Patients with WDR19 mutations can show various extrarenal manifestations such as skeletal disorders, Caroli disease, and retinal dystrophy"* ([PMID: 28621010](https://pubmed.ncbi.nlm.nih.gov/28621010/)).

Variable expressivity is marked: the same residue (homozygous p.Leu710Ser) can cause **either** isolated retinitis pigmentosa **or** Jeune syndrome ([PMID: 25044745](https://pubmed.ncbi.nlm.nih.gov/25044745/): *"analogous to homozygous p.Leu710Ser in WDR19 causing either isolated retinitis pigmentosa or Jeune syndrome"*). Against this backdrop, SPGF72 ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)) sits at the nonsyndromic extreme — a proband with asthenoteratospermia and **no** detectable ciliopathy features on CT or retinal imaging. This is a central interpretive point: the disease serial number ("Spermatogenic Failure 72") obscures that the causal gene is a well-known ciliopathy gene, and a researcher could easily confuse it with the more common syndromic WDR19 disorders.

### Finding 3 — IFT-A dysfunction mechanistically links WDR19 loss to MMAF and sperm immotility

Intraflagellar transport is indispensable for sperm flagellum formation and male fertility (review [PMID: 34815207](https://pubmed.ncbi.nlm.nih.gov/34815207/)). The mechanistic chain is supported by convergent model-organism and interaction evidence:

- **IFT140, WDR19's direct IFT-A partner:** germ-cell-specific *Ift140* knockout mice are infertile with reduced sperm number and motility, amorphous heads, short/bent flagella, and cytoplasmic vesicles ([PMID: 29236364](https://pubmed.ncbi.nlm.nih.gov/29236364/): *"IFT140 is a key regulator for male fertility and normal spermiogenesis in mice"*).
- **Testis IFT-A network:** DNAI4 interacts with IFT144 (WDR19) within the testis, and *Dnai4*-null mice show MMAF with downregulation of IFT-A members IFT140/IFT122/IFT121 ([PMID: 42083518](https://pubmed.ncbi.nlm.nih.gov/42083518/): *"Immunoprecipitation demonstrated an interaction between DNAI4 and the intraflagellar transport protein IFT144 within the testes"*).
- **Human corroboration:** in the WDR19 proband, IFT140 and IFT88 were mislocalized in sperm ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)).

Together these establish that WDR19 loss disrupts an IFT-A–dependent transport network required for building the sperm flagellar axoneme, recapitulating the MMAF phenotype.

### Finding 4 — IFT-A is a six-subunit β-propeller/TPR complex (including WDR19) essential for flagellum assembly

Recent cryo-EM / cryo-electron tomography of IFT-A from *Tetrahymena* and *Chlamydomonas* resolved a **six-component complex** — WDR19/IFT144, IFT140, IFT122, WDR35/IFT121, IFT43, and TTC21B/IFT139 — that polymerizes laterally along anterograde IFT trains and sits between the IFT-B complex and the ciliary membrane ([PMID: 36932088](https://pubmed.ncbi.nlm.nih.gov/36932088/); [PMID: 36593313](https://pubmed.ncbi.nlm.nih.gov/36593313/); [PMID: 36563665](https://pubmed.ncbi.nlm.nih.gov/36563665/)). A sperm-formation review states: *"Twenty-two IFT components form the IFT-A complex (six components) and IFT-B complex (sixteen components)"* and *"IFT is required to assemble these structures to form functional sperm"* ([PMID: 40301266](https://pubmed.ncbi.nlm.nih.gov/40301266/)). Structurally, *"IFT-A is sandwiched between IFT-B and the ciliary membrane, consistent with its putative role in transporting transmembrane and membrane-associated cargoes"* ([PMID: 36563665](https://pubmed.ncbi.nlm.nih.gov/36563665/)). WDR19 contributes β-propeller and α-solenoid (clathrin heavy-chain repeat) domains to this scaffold, consistent with a structural/cargo-adaptor role whose loss collapses retrograde transport.

### Finding 5 — ICSI is effective for MMAF/asthenoteratozoospermia, with a caveat of possibly reduced embryo potential

Because the defect is in sperm motility and flagellar structure (not in the sperm genome or fertilizing capacity per se), **ICSI bypasses the defect**. Evidence:

| Study | Cohort | Key outcome | PMID |
|---|---|---|---|
| Paris cohort | 20 MMAF couples | *"ICSI outcomes for couples with MMAF do not differ from those of other couples requiring ICSI, irrespective of the genetic defect"* | [34529793](https://pubmed.ncbi.nlm.nih.gov/34529793/) |
| DNAH2/6/10 MMAF | 6 couples | Live birth in 5/6 via ICSI | [40592014](https://pubmed.ncbi.nlm.nih.gov/40592014/) |
| Propensity-matched | n=38 | *"decreased embryo developmental potential and compromised clinical outcomes in the MMAF cohort"*; lower cumulative live birth rate | [38745955](https://pubmed.ncbi.nlm.nih.gov/38745955/) |
| WDR19 index case | 1 couple | Clinical pregnancy achieved via ICSI | [32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/) |

Overall, ICSI is the standard effective intervention, though some MMAF cohorts show modestly reduced embryo developmental potential.

### Finding 6 — gnomAD constraint supports a recessive mechanism (WDR19 is heterozygous-LoF-tolerant)

Population constraint metrics for *WDR19* (ENSG00000157796; chr4:39,182,504–39,285,810, GRCh38) are consistent with recessive inheritance: **pLI ≈ 0** (1.76e-26); observed/expected LoF = 0.67 (121 observed vs ~180 expected); **LOEUF ≈ 0.78**; missense Z = 2.01; LoF Z = 3.73. These values indicate WDR19 is **not** haploinsufficient or LoF-intolerant at the heterozygous level, even though there is moderate overall depletion of LoF alleles. This fits the clinical picture that heterozygous carriers are unaffected and disease requires biallelic variants.

### Finding 7 — WDR19 is a rare contributor within a heterogeneous MMAF gene landscape

MMAF is genetically heterogeneous. Recurrent causal genes include **DNAH1, CFAP43, CFAP44, CFAP69, FSIP2, WDR66, ARMC2**, among many others ([PMID: 30686508](https://pubmed.ncbi.nlm.nih.gov/30686508/); [PMID: 30415212](https://pubmed.ncbi.nlm.nih.gov/30415212/)). *"Six genes (DNAH1, CFAP43, CFAP44, CFAP69, FSIP2, and WDR66) have been found to be recurrently associated with MMAF"* ([PMID: 30686508](https://pubmed.ncbi.nlm.nih.gov/30686508/)). Exome sequencing of severe sperm motility disorders found disease-causing variants in 10/21 (48%) patients, and *"up to 50% of causality in patients with severe sperm motility disorders can be explained by pathogenic variants in at least 22 genes"* ([PMID: 34089056](https://pubmed.ncbi.nlm.nih.gov/34089056/)). WDR19 is a **rare, recently added** MMAF gene (a single reported proband) that sits among the minority of unexplained/rare contributors.

### Finding 8 — WDR19 orthologs, aliases, and domain architecture

NCBI/MyGene records: human *WDR19* = Gene **57728** (ENSG00000157796, cytoband 4p14); mouse *Wdr19* = Gene **213081** (chr5 C3.1); rat *Wdr19* = Gene **305349**; zebrafish *wdr19* = Gene **556414**; *C. elegans* ortholog **dyf-2**. Official aliases include ATD5, CED4, CFAP66, DYF-2, FAP66, **IFT144**, NPHP13, ORF26, Oseg6, PWDMP, **SPGF72**, SRTD5. The NCBI gene summary notes the protein *"contains six WD repeats … and a clathrin heavy-chain repeat"* (i.e., β-propeller plus α-solenoid architecture), and that mutations cause ciliopathies including Jeune, Sensenbrenner, Senior-Løken, nephronophthisis, and retinitis pigmentosa.

### Finding 9 — Consolidated SPGF72 (WDR19) disease profile

SPGF72 (MONDO:0030809; gene *WDR19*/IFT144, HGNC:18340, NCBI 57728, OMIM *608151) is an autosomal-recessive nonsyndromic asthenoteratozoospermia with MMAF. The single reported proband carried homozygous *WDR19* c.A3811G/p.K1271E from a consanguineous family, with progressive motility of 0%, destroyed flagellar ultrastructure, WDR19 absent, and IFT140/IFT88 mislocalized ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)). The mechanism is IFT-A retrograde transport failure within a six-subunit complex. Treatment is ICSI; there is no disease-modifying drug and no environmental or infectious etiology.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function/missense variant in *WDR19*** (e.g., homozygous c.A3811G, p.K1271E) **leads to** loss or destabilization of the WDR19/IFT144 protein in the male germ line ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)).
2. Absence of WDR19 **results in** destabilization of the six-subunit IFT-A complex and **mislocalization of partner proteins** IFT140 (IFT-A) and IFT88 (IFT-B) in differentiating spermatids ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/); mechanism inferred from IFT-A architecture, [PMID: 36563665](https://pubmed.ncbi.nlm.nih.gov/36563665/)).
3. IFT-A destabilization **impairs retrograde intraflagellar transport** along the developing flagellar axoneme (inferred from IFT-A's established retrograde-transport and membrane-cargo role; [PMID: 36932088](https://pubmed.ncbi.nlm.nih.gov/36932088/)).
4. Defective IFT **leads to** failure of proper assembly and maintenance of the flagellar "9+2" axoneme and accessory structures during spermiogenesis (supported by *Ift140* KO mouse spermiogenesis defects, [PMID: 29236364](https://pubmed.ncbi.nlm.nih.gov/29236364/); review [PMID: 34815207](https://pubmed.ncbi.nlm.nih.gov/34815207/)).
5. Axonemal disassembly **results in** the **MMAF phenotype** — absent, short, bent, coiled, and irregular-calibre flagella with completely destroyed ultrastructure on SEM/TEM ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)).
6. Structurally defective flagella **cause** loss of progressive motility (reduced to 0%) → **asthenoteratozoospermia** → **male infertility / SPGF72** ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)).

**Branch point:** Because WDR19 is required in *all* cilia, the same gene's biallelic variants can instead (or additionally) impair primary and motile cilia in kidney, retina, skeleton, and liver → syndromic ciliopathies (CED4, NPHP13, SRTD5, Senior-Løken). The nonsyndromic SPGF72 outcome implies that the specific SPGF72 allele (p.K1271E) has a germ-cell/flagellum-predominant functional impact, sparing somatic ciliary function — an inference consistent with the marked variable expressivity documented for WDR19 alleles ([PMID: 25044745](https://pubmed.ncbi.nlm.nih.gov/25044745/)).

```
 WDR19 biallelic variant (p.K1271E)
            │
            ▼
 Loss of WDR19 protein in germ line
            │
            ▼
 IFT-A complex destabilized ──► IFT140/IFT88 mislocalized
            │
            ▼
 Retrograde intraflagellar transport fails
            │
            ▼
 Flagellar axoneme (9+2) fails to assemble/maintain
            │
            ▼
 MMAF: absent/short/bent/coiled flagella (SEM/TEM destroyed)
            │
            ▼
 Progressive motility = 0%  ──►  Asthenoteratozoospermia
            │
            ▼
 Male infertility (SPGF72)  ──► [treatable by ICSI]

 BRANCH (somatic cilia): WDR19 loss in kidney/retina/skeleton/liver
   ──► syndromic ciliopathies (CED4, NPHP13, SRTD5, Senior-Løken)
```

### Ontology annotations

| Category | Term | ID |
|---|---|---|
| Disease | Spermatogenic failure 72 | MONDO:0030809 |
| Gene | WDR19 | HGNC:18340 / NCBI 57728 / OMIM *608151 |
| Phenotype | Male infertility | HP:0003251 |
| Phenotype | Reduced sperm motility | HP:0012207 |
| Phenotype | Asthenozoospermia | HP:0040031 |
| Phenotype | Abnormal sperm morphology | HP:0012865 |
| Anatomy | Testis | UBERON:0000473 |
| Anatomy | Sperm flagellum | UBERON:0010314 |
| Cell type | Spermatid | CL:0000018 |
| Cell type | Spermatozoon | CL:0000019 |
| GO-CC | Sperm flagellum | GO:0036126 |
| GO-CC | Axoneme | GO:0005930 |
| GO-CC | IFT particle A (IFT-A complex) | GO:0030991 |
| GO-BP | Intraciliary retrograde transport | GO:0035721 |
| GO-BP | Cilium assembly | GO:0060271 |
| Treatment | Intracytoplasmic sperm injection (ICSI) | NCIT C18113 |

---

## Section-by-Section Report

### 1. Disease Information
SPGF72 is a nonsyndromic autosomal-recessive male-infertility disorder characterized by asthenoteratozoospermia with MMAF, caused by biallelic *WDR19* variants. Identifiers: **MONDO:0030809**; gene *WDR19* (OMIM *608151; the phenotype-series OMIM number was not recorded in the provided brief). Synonyms: SPGF72; WDR19-related nonsyndromic asthenoteratozoospermia. Information is derived from an **aggregated disease-level / single-case report** source ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)), not large EHR cohorts.

### 2. Etiology
**Causal factor is purely genetic:** biallelic (homozygous in the index case) *WDR19* variants. The reported genetic risk context is **consanguinity** (index family was consanguineous). No environmental, infectious, lifestyle, or protective factors have been established for this specific disorder, and no gene–environment interactions are documented. gnomAD constraint (pLI≈0, LOEUF≈0.78) confirms heterozygous carriers are unaffected (recessive).

### 3. Phenotypes
Core phenotypes (all **laboratory/clinical-sign** abnormalities of semen):
- **Male infertility** (HP:0003251) — the presenting complaint; adult onset at reproductive age; severe; stable (non-progressive); essentially 100% in affected (biallelic) individuals.
- **Reduced/absent sperm motility — asthenozoospermia** (HP:0012207 / HP:0040031) — progressive motility reduced to 0%.
- **Abnormal sperm morphology — MMAF** (HP:0012865) — absent, short, bent, coiled, irregular-calibre flagella; destroyed axonemal ultrastructure.

Quality-of-life impact is confined to reproductive function and the psychosocial burden of infertility; there is no systemic morbidity because the disorder is nonsyndromic. Onset is effectively congenital at the molecular level but clinically recognized in adulthood during infertility workup.

### 4. Genetic / Molecular Information
**Causal gene:** *WDR19* (IFT144), HGNC:18340, NCBI 57728, OMIM *608151, 4p14. **Index variant:** homozygous c.A3811G (p.K1271E), a missense variant ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)); **germline** origin. Functional consequence is **loss of function** (protein absent from sperm by immunofluorescence). Across the WDR19 allelic series, variant types include missense, nonsense, splice, and frameshift. No modifier genes, epigenetic mechanisms, or chromosomal abnormalities are established for SPGF72. Population allele frequency of the specific variant is very low (consistent with a private/rare recessive allele).

### 5. Environmental Information
**Not applicable.** No environmental toxins, lifestyle factors, or infectious agents are implicated. The disorder is monogenic/recessive.

### 6. Mechanism / Pathophysiology
See the ordered causal chain above. In brief: WDR19 loss → IFT-A destabilization → failed retrograde intraflagellar transport → defective axoneme assembly → MMAF → immotility → infertility. Molecular pathway = intraflagellar transport (not a classical signaling cascade). Cellular process = cilium/flagellum assembly (spermiogenesis). Protein dysfunction = loss of a β-propeller/α-solenoid IFT-A scaffold subunit. No metabolic, immune, or inflammatory involvement is implicated.

### 7. Anatomical Structures Affected
- **Organ:** testis (UBERON:0000473); body system = male reproductive system.
- **Tissue/cell:** seminiferous epithelium germ cells — spermatids (CL:0000018) and spermatozoa (CL:0000019).
- **Subcellular:** sperm flagellum (GO:0036126 / UBERON:0010314), axoneme (GO:0005930), IFT particle A (GO:0030991).
- **Localization:** bilateral (both testes); no lateralization asymmetry.
No secondary organ involvement (nonsyndromic).

### 8. Temporal Development
Onset is **congenital/developmental** at the cellular level (spermiogenesis is defective from puberty onward) but **clinically recognized in adulthood** at infertility evaluation. Course is **stable/non-progressive**: the defect is constitutive, not degenerative. No remission occurs spontaneously. The relevant "critical period" is the window of assisted-reproduction intervention (ICSI).

### 9. Inheritance and Population
**Autosomal recessive**, with complete penetrance for the reproductive phenotype in biallelic individuals (based on a single family). **Consanguinity** is a documented contributing factor. gnomAD shows WDR19 is heterozygous-LoF-tolerant. **Epidemiology:** extremely rare — SPGF72 is defined by a single reported proband; precise prevalence/incidence are unknown. Within MMAF (itself a rare cause of male infertility), WDR19 is a minor contributor relative to DNAH1/CFAP43/CFAP44/etc. Affected sex is **male only** (the phenotype is male infertility). No founder effect is reported for WDR19 in SPGF72.

### 10. Diagnostics
- **Semen analysis** (LOINC-codable) showing severe asthenozoospermia / absent progressive motility with abnormal morphology.
- **Sperm ultrastructure:** SEM/TEM showing MMAF and destroyed axoneme.
- **Immunofluorescence:** WDR19 absent; IFT140/IFT88 mislocalized (research-grade confirmation).
- **Genetic testing:** whole-exome sequencing (how the gene was discovered) or targeted MMAF gene panels including *WDR19*; confirmatory Sanger of the biallelic variant. Chromosomal microarray, karyotyping, FISH, and mtDNA testing are **not** indicated for this monogenic nuclear-gene disorder.
- **Differential diagnosis:** other MMAF genes (DNAH1, CFAP43, CFAP44, CFAP69, FSIP2, WDR66, ARMC2, DNAH2/6/10) and — importantly — syndromic WDR19 ciliopathies, which must be excluded by renal/skeletal/retinal evaluation (CT, retinal imaging), as was done in the index case.

### 11. Outcome / Prognosis
**No effect on survival or lifespan** — the disorder is confined to fertility. Morbidity is reproductive/psychosocial only. **Prognosis for biological fatherhood is good with ICSI**: the index couple achieved clinical pregnancy, and MMAF cohorts broadly achieve good ICSI outcomes, with a caveat that some cohorts show modestly reduced embryo developmental potential and cumulative live-birth rates ([PMID: 38745955](https://pubmed.ncbi.nlm.nih.gov/38745955/)).

### 12. Treatment
- **ICSI (NCIT C18113)** is the mainstay and is effective ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/); [PMID: 34529793](https://pubmed.ncbi.nlm.nih.gov/34529793/)).
- **No pharmacotherapy, gene therapy, or disease-modifying treatment** exists or is in trials for this disorder.
- **Personalized medicine:** genotype (biallelic WDR19 LoF) guides counseling that natural conception is very unlikely but ICSI is appropriate; no pharmacogenomic considerations.

### 13. Prevention
- **Genetic counseling** for consanguineous couples and families with affected males.
- **Carrier/cascade screening** of relatives for the familial WDR19 variant.
- **Preimplantation genetic testing (PGT)** could prevent transmission of biallelic disease, though offspring of an affected father + non-carrier mother would be obligate heterozygous carriers (unaffected).
- No primary/secondary population prevention, immunization, or environmental intervention is applicable.

### 14. Other Species / Natural Disease
Orthologs: mouse *Wdr19* (NCBI 213081), rat *Wdr19* (305349), zebrafish *wdr19* (556414), *C. elegans* **dyf-2**. IFT/WDR19 function is deeply evolutionarily conserved across ciliated eukaryotes. No naturally occurring WDR19 male-infertility disease is catalogued in companion animals in the reviewed evidence; the conservation of IFT-A implies broad cross-species relevance for flagellar biology.

### 15. Model Organisms
No dedicated **testis-specific *Wdr19* knockout** has been published for SPGF72. The most informative proxy is the **germ-cell-specific *Ift140* knockout mouse** (WDR19's direct IFT-A partner), which is infertile with reduced sperm number/motility and MMAF-like flagellar defects ([PMID: 29236364](https://pubmed.ncbi.nlm.nih.gov/29236364/)), and the ***Dnai4*-null mouse**, which shows MMAF with downregulation of IFT-A members and a demonstrated DNAI4–IFT144 interaction in testis ([PMID: 42083518](https://pubmed.ncbi.nlm.nih.gov/42083518/)). These models recapitulate the flagellar/infertility mechanism but not WDR19 specifically. Resource databases: MGI, IMPC, ZFIN, WormBase.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/) | *Novel homozygous WDR19 mutation … nonsyndromic asthenoteratospermia* | **Primary/defining evidence** for SPGF72: gene, variant, phenotype, ultrastructure, ICSI outcome |
| [28621010](https://pubmed.ncbi.nlm.nih.gov/28621010/) | *Diversity of renal phenotypes in WDR19 mutations* | Documents syndromic WDR19 ciliopathy spectrum (contrast with nonsyndromic SPGF72) |
| [25044745](https://pubmed.ncbi.nlm.nih.gov/25044745/) | *POC1B severe syndromic retinal ciliopathy* | WDR19 p.Leu710Ser variable expressivity (RP vs Jeune) |
| [29134781](https://pubmed.ncbi.nlm.nih.gov/29134781/) / [28332779](https://pubmed.ncbi.nlm.nih.gov/28332779/) | *Sensenbrenner/CED, WDR35* | IFT/CED gene-family context including WDR19 |
| [34815207](https://pubmed.ncbi.nlm.nih.gov/34815207/) | *Role of IFT in mammalian spermiogenesis* | IFT indispensable for sperm flagellum/male fertility |
| [29236364](https://pubmed.ncbi.nlm.nih.gov/29236364/) | *IFT140 essential for male fertility/spermiogenesis* | Mouse model of WDR19's IFT-A partner recapitulates MMAF |
| [42083518](https://pubmed.ncbi.nlm.nih.gov/42083518/) | *DNAI4 required for flagellum assembly/male fertility* | DNAI4–IFT144 testis interaction; IFT-A downregulation causes MMAF |
| [36932088](https://pubmed.ncbi.nlm.nih.gov/36932088/) / [36593313](https://pubmed.ncbi.nlm.nih.gov/36593313/) / [36563665](https://pubmed.ncbi.nlm.nih.gov/36563665/) | *IFT-A structure / train assembly* | Six-subunit IFT-A architecture and retrograde role |
| [40301266](https://pubmed.ncbi.nlm.nih.gov/40301266/) | *Intraflagellar Transport and Sperm Formation* | Defines WDR19 as 1 of 6 IFT-A subunits; IFT builds sperm |
| [34529793](https://pubmed.ncbi.nlm.nih.gov/34529793/) | *ICSI in MMAF* | ICSI efficacy independent of genetic defect |
| [40592014](https://pubmed.ncbi.nlm.nih.gov/40592014/) | *DNAH2/6/10 MMAF ICSI outcomes* | Live birth 5/6 via ICSI |
| [38745955](https://pubmed.ncbi.nlm.nih.gov/38745955/) | *Decreased embryo potential in MMAF* | Caveat: reduced embryo/cumulative outcomes |
| [34089056](https://pubmed.ncbi.nlm.nih.gov/34089056/) | *Exome sequencing in sperm motility disorders* | MMAF heterogeneity (~22 genes, ~50% yield) |
| [30686508](https://pubmed.ncbi.nlm.nih.gov/30686508/) / [30415212](https://pubmed.ncbi.nlm.nih.gov/30415212/) | *ARMC2 / CFAP69 MMAF* | Recurrent MMAF genes; differential diagnosis |

**Evidence source types:** human clinical (single-case report) for the WDR19–SPGF72 link; model-organism (mouse) for the IFT-A mechanism; structural/computational (cryo-EM, AlphaFold) for IFT-A architecture; population-genetics (gnomAD) for inheritance mode.

---

## Limitations and Knowledge Gaps

1. **Single human proband.** The entire human nonsyndromic WDR19 phenotype rests on one case ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)). Penetrance, expressivity, allelic range, and population frequency for SPGF72 are therefore essentially unknown. The gene–disease relationship would be classified as **limited** by ClinGen-style criteria until additional cases are reported.
2. **No dedicated WDR19 testis knockout.** The mechanism is inferred from IFT140 and DNAI4 models, not from direct WDR19 germ-cell perturbation. A conditional/germ-cell *Wdr19* knockout is the critical missing experiment.
3. **Variant-specific functional data absent.** Whether p.K1271E is a pure LoF or has flagellum-selective effects (explaining nonsyndromic sparing of somatic cilia) has not been functionally dissected.
4. **No epidemiology.** Prevalence, incidence, founder effects, and ethnic distribution are not quantifiable from one case.
5. **ICSI outcome generalization.** WDR19-specific ICSI data = 1 pregnancy; broader MMAF data apply by analogy and show a possible embryo-potential caveat.
6. **OMIM phenotype number.** The phenotype-series OMIM MIM number for SPGF72 was not recorded in the provided brief (gene OMIM = *608151).

---

## Proposed Follow-up Experiments / Actions

1. **Case accrual / GeneMatcher.** Identify additional unrelated SPGF72 probands through MMAF cohorts and GeneMatcher to upgrade gene–disease evidence and define the allelic spectrum.
2. **Conditional germ-cell *Wdr19* knockout mouse.** Generate a Stra8-Cre or Ddx4-Cre conditional *Wdr19* deletion to test whether WDR19 loss directly causes MMAF and to determine why somatic cilia can be spared (flagellum-selective hypothesis).
3. **Variant functional assays.** Express p.K1271E in cell/ciliary models and in sperm-like systems to measure IFT-A stability, retrograde transport velocity, and IFT140/IFT88 localization versus wild type.
4. **Structural modeling.** Map p.K1271E onto the cryo-EM IFT-A structure to predict whether it disrupts a β-propeller interface, inter-subunit contact, or cargo-binding surface.
5. **ICSI outcome registry.** Pool WDR19/MMAF ICSI cases to quantify fertilization, embryo quality, and live-birth rates and to test whether WDR19 patients share the reduced embryo-potential signal seen in some MMAF cohorts ([PMID: 38745955](https://pubmed.ncbi.nlm.nih.gov/38745955/)).
6. **Panel inclusion.** Ensure *WDR19* is included in clinical MMAF/male-infertility gene panels, with pre-test counseling to screen for latent syndromic ciliopathy features (renal, retinal, skeletal) given the gene's pleiotropy.

---

*Report compiled from 5 discovery iterations, 9 confirmed findings, and 22 reviewed papers. Evidence base is dominated by a single human report ([PMID: 32323121](https://pubmed.ncbi.nlm.nih.gov/32323121/)) supplemented by IFT-A structural biology and model-organism studies of partner genes.*


## Artifacts

- [OpenScientist final report](Spermatogenic_Failure_72-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spermatogenic_Failure_72-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 15 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 14 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0040031` (2 mentions) - the report calls it "Asthenozoospermia"; HP calls it **Chorioretinal hyperpigmentation**
- `UBERON:0010314` (2 mentions) - the report calls it "Sperm flagellum"; UBERON calls it **structure with developmental contribution from neural crest**
- `CL:0000018` (2 mentions) - the report calls it "Spermatid", "Tissue/cell:** seminiferous epithelium germ cells — spermatids"; CL calls it **spermatid**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012865` (2 mentions) - the report calls it "Abnormal sperm morphology", "Abnormal sperm morphology — MMAF"; HP calls it **Abnormal sperm head morphology**
- `UBERON:0000473` (2 mentions) - the report calls it "Testis", "Organ:** testis"; UBERON calls it **testis**
- `CL:0000019` (2 mentions) - the report calls it "Spermatozoon"; CL calls it **sperm**, and lists "spermatozoon" among its other names
- `GO:0030991` (2 mentions) - the report calls it "IFT particle A (IFT-A complex)"; GO calls it **intraciliary transport particle A**, and lists "IFT A complex" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0012865` - called "Abnormal sperm morphology", "Abnormal sperm morphology — MMAF"
- `UBERON:0000473` - called "Testis", "Organ:** testis"
- `CL:0000018` - called "Spermatid", "Tissue/cell:** seminiferous epithelium germ cells — spermatids"
