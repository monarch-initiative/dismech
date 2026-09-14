---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-13T20:52:47.711338'
end_time: '2026-09-13T21:23:19.939282'
duration_seconds: 1832.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome 2
  mondo_id: MONDO:0025708
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
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 22
  on_topic: 17
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 0
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0025708
    reported_labels:
    - MONDO
    ontology_label: megacystis-microcolon-intestinal hypoperistalsis syndrome 2
  - term_id: HP:0004388
    reported_labels:
    - Physical/imaging sign
    ontology_label: Microcolon
  - term_id: HP:0004389
    reported_labels:
    - Clinical sign
    ontology_label: Intestinal pseudo-obstruction
  - term_id: HP:0002579
    reported_labels:
    - Clinical sign
    ontology_label: Gastrointestinal dysmotility
  - term_id: HP:0000126
    reported_labels:
    - Imaging sign
    ontology_label: Hydronephrosis
  - term_id: HP:0000072
    reported_labels:
    - Imaging sign
    ontology_label: Hydroureter
  - term_id: HP:0002566
    reported_labels:
    - Structural
    ontology_label: Intestinal malrotation
  - term_id: HP:0001561
    reported_labels:
    - Prenatal sign
    ontology_label: Polyhydramnios
  - term_id: HP:0011968
    reported_labels:
    - Symptom
    ontology_label: Feeding difficulties
  labels_variant: 7
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Megacystis-Microcolon-Intestinal_Hypoperistalsis_Syndrome_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Megacystis-Microcolon-Intestinal_Hypoperistalsis_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome 2
- **MONDO ID:** MONDO:0025708 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome 2** covering all of the
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

# Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome 2 (MMIHS2): A Comprehensive Disease Characteristics Report

**Disease:** Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome 2
**MONDO ID:** MONDO:0025708 | **OMIM:** 619431 | **Causal gene:** *MYH11* (HGNC:7569)
**Category:** Mendelian (autosomal recessive)

> **Evidence source note:** This report is compiled from **aggregated disease-level resources** (OMIM, Orphanet, HGNC/Ensembl/UniProt/gnomAD) and **primary literature** (human clinical case series/cohorts, mouse models, in vitro/immunohistochemical studies, and computational constraint data). Because MMIHS2 is ultra-rare, most human evidence derives from case reports and small cohorts; MMIHS-wide cohort statistics (which are dominated by *ACTG2* cases) are used where *MYH11*-specific numbers are unavailable and are flagged as such.

---

## Summary

Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome 2 (MMIHS2) is a rare, severe congenital **visceral myopathy** caused by **autosomal-recessive biallelic loss-of-function (LOF) variants in *MYH11***, the gene encoding smooth-muscle myosin heavy chain (SM myosin II) — the dominant motor protein that drives smooth-muscle-cell contraction. Loss of functional SM myosin abolishes contractility in the smooth muscle of the urinary bladder and gastrointestinal tract, producing the defining triad from birth: a massively distended, non-obstructed urinary bladder (**megacystis**), an unused, small-caliber **microcolon**, and intestinal hypo- or aperistalsis causing a **functional (non-mechanical) intestinal obstruction**. MMIHS2 is the *MYH11*-linked subtype within the broader MMIHS family, which also includes the more common *ACTG2*-related form (MMIHS type 1, OMIM 155310) and rarer recessive forms caused by *LMOD1*, *MYLK*, *MYL9*, and the candidate gene *PDCL3*.

Mechanistically, MMIHS2 is a "contractile apparatus" disease: all confirmed MMIHS genes encode components of the smooth-muscle thin/thick filament and the myosin-light-chain-kinase (MLCK) phosphorylation axis. Biallelic *MYH11* null alleles remove or drastically reduce the myosin motor itself, so the smooth muscle cannot generate force despite the presence of normal enteric ganglion cells and interstitial cells of Cajal. This distinguishes MMIHS from Hirschsprung disease (a neuropathic aganglionosis) and classifies it among the "variants of Hirschsprung's disease" — congenital smooth-muscle-cell disorders. Notably, routine histopathology and electron microscopy of *MYH11* visceral myopathy are often near-normal, underscoring that the defect is **functional rather than grossly structural**.

Clinically, MMIHS shows a striking **female preponderance** (~70–73%), is frequently detected on prenatal ultrasound (megacystis ± polyhydramnios), and historically carried a very poor prognosis (survival <20% in older series). Modern management — total parenteral nutrition (TPN), intestinal rehabilitation, bladder catheterization/vesicostomy, enteric stomas, and isolated-intestinal or multivisceral (± liver) transplantation — has raised survival to roughly **55–65%**, with patients now living into the second and third decades of life. There is **no effective disease-specific pharmacotherapy**; treatment is entirely supportive/surgical, with transplantation the only definitive option once TPN-associated liver failure develops. This report synthesizes 9 confirmed findings across 26 reviewed papers into a complete disease-characteristics knowledge-base entry.

---

## Section 1. Disease Information

**Overview.** MMIHS (Berdon syndrome) is a congenital disorder of impaired smooth-muscle contractility producing functional obstruction of the bladder and bowel. MMIHS2 designates the subtype caused by biallelic *MYH11* variants. It is the most severe form of functional intestinal obstruction in the newborn ([PMID: 18280270](https://pubmed.ncbi.nlm.nih.gov/18280270/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (MMIHS2) | 619431 |
| OMIM (MMIHS1, *ACTG2*) | 155310 |
| MONDO | MONDO:0025708 |
| Orphanet (MMIHS) | ORPHA:2241 |
| Gene-OMIM (*MYH11*) | 160745 |
| HGNC | HGNC:7569 |
| NCBI Gene | 4629 |
| Ensembl | ENSG00000133392 |
| UniProt | P35749 |
| Cytoband | 16p13.11 (GRCh38 chr16:15,703,135–15,858,438, minus strand) |

**Synonyms / alternative names.** Berdon syndrome; Berdon's syndrome; MMIHS; congenital visceral myopathy (MMIHS subtype); megacystis–microcolon–intestinal hypoperistalsis syndrome type 2.

**Information source.** Content here is derived from **aggregated disease-level resources** (OMIM, Orphanet, HGNC/Ensembl/UniProt) plus **individual-patient and small-cohort clinical reports** and systematic reviews. It is not derived from a large EHR/population registry, reflecting the disease's rarity.

---

## Section 2. Etiology

**Primary cause — genetic.** MMIHS2 is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *MYH11*** (Finding F001). This is a monogenic Mendelian cause; there is no established environmental, infectious, or acquired etiology.

Evidence:
- A **homozygous nonsense variant c.3598A>T (p.Lys1200Ter)** was identified by exome sequencing in a newborn with MMIHS and prune-belly phenotype from consanguineous parents ([PMID: 25407000](https://pubmed.ncbi.nlm.nih.gov/25407000/)): *"We performed exome sequencing in a newborn with MMIHS and prune belly phenotype whose parents are consanguineous and identified a homozygous variant (c.3598A>T: p.Lys1200Ter) in MYH11, which codes for the smooth muscle myosin heavy chain."*
- **Compound heterozygous variants** c.2051G>A (p.R684H) and c.3540_3541delinsTT (p.(E1180D,Q1181Ter)) were found in a Chinese family, with a marked decrease in MYH11 protein on Western blot ([PMID: 31427716](https://pubmed.ncbi.nlm.nih.gov/31427716/)): *"Trio-targeted exome sequencing identified compound heterozygous variants, c.2051 G > A (p.R684H) and c.3540_3541delinsTT (p.(E1180D, Q1181Ter)), in MYH11."*
- A **16p13.11 microdeletion** encompassing *MYH11* unmasked a missense p.Pro127Ser variant on the other allele, confirming a biallelic null mechanism ([PMID: 31044419](https://pubmed.ncbi.nlm.nih.gov/31044419/)): *"Megacystis-microcolon-intestinal hypoperistalsis syndrome (MMIHS), a rare condition that affects smooth muscle cells, is caused by biallelic null alleles in MYH11."*

**Genetic risk factors.** The causal variants are the risk factor. **Consanguinity** is a major contributor (multiple index cases arose from consanguineous unions), consistent with an autosomal-recessive rare-allele architecture. *MYH11* is highly intolerant to LOF in the general population (Finding F008): gnomAD constraint pLI ≈ 1.0; observed/expected LoF = 80/246.6 (o/e = 0.32, 90% CI 0.27–0.39; LOEUF ≈ 0.39); LoF Z = 9.0; missense Z = 3.29 — i.e., strong depletion of both LoF and missense variants. This intolerance explains the **dual disease architecture** of *MYH11*: heterozygous dominant-negative or protein-elongating variants cause thoracic aortic aneurysm/dissection and a dominant dysmotility syndrome, while biallelic null alleles cause recessive MMIHS2.

**Environmental risk factors / protective factors / gene–environment interactions.** **Not applicable / none identified.** As a fully penetrant Mendelian disorder driven by biallelic null alleles, no environmental risk factors, protective factors, lifestyle exposures, or gene–environment interactions have been described. Sex is a phenotype-modifying factor (female predominance and worse outcomes in girls) rather than a causal risk factor.

---

## Section 3. Phenotypes

All phenotypes are **congenital/neonatal in onset**, **severe**, and **stable-to-progressive** (organ damage accrues secondary to chronic obstruction and TPN). HPO terms below were verified against EBI OLS4/HPO (Finding F009).

| Phenotype | Type | HPO term | Onset | Frequency / notes |
|---|---|---|---|---|
| Megacystis (massively distended non-obstructed bladder) | Physical/imaging sign | HP:0000021 (Fetal megacystis HP:0010956) | Congenital/prenatal | Defining; detectable prenatally |
| Microcolon | Physical/imaging sign | HP:0004388 | Congenital | Defining; girls > boys (*ACTG2* data) |
| Intestinal pseudo-obstruction / hypoperistalsis | Clinical sign | HP:0004389 | Neonatal | Defining |
| Gastrointestinal dysmotility | Clinical sign | HP:0002579 | Neonatal | Universal |
| Abdominal distention | Clinical sign | HP:0003270 | Neonatal | Very frequent |
| Hydronephrosis | Imaging sign | HP:0000126 | Congenital | Common (upper-tract effects of megacystis) |
| Hydroureter | Imaging sign | HP:0000072 | Congenital | Common |
| Intestinal malrotation | Structural | HP:0002566 | Congenital | Frequent |
| Polyhydramnios | Prenatal sign | HP:0001561 | Prenatal | Common |
| Feeding difficulties | Symptom | HP:0011968 | Neonatal | Universal (leads to TPN dependence) |

**Important negative:** Aganglionic megacolon / Hirschsprung disease (HP:0002251) is **NOT** a feature — enteric ganglia are present in MMIHS2 (Finding F009). This is a key differential-diagnostic point.

**Quality-of-life impact.** Profound. Affected individuals are typically **dependent on parenteral nutrition** and require **bladder drainage** (intermittent catheterization or vesicostomy) and **enteric stomas** from birth. Chronic complications include TPN-associated cholestatic liver disease, recurrent sepsis, and chronic kidney disease ([PMID: 41591435](https://pubmed.ncbi.nlm.nih.gov/41591435/)). Disease-specific formal QoL instrument data (EQ-5D/SF-36/PROMIS) are not available for this ultra-rare condition.

---

## Section 4. Genetic / Molecular Information

**Causal gene.** *MYH11* — "myosin heavy chain 11" (smooth muscle) — HGNC:7569, NCBI Gene 4629, Ensembl ENSG00000133392, UniProt P35749, gene-OMIM 160745, located at **16p13.11** (Finding F007).

**Pathogenic variants (MMIHS2 = recessive, biallelic).**

| Variant (cDNA / protein) | Type | Zygosity | Evidence |
|---|---|---|---|
| c.3598A>T (p.Lys1200Ter) | Nonsense | Homozygous | [PMID: 25407000](https://pubmed.ncbi.nlm.nih.gov/25407000/) |
| c.2051G>A (p.R684H) + c.3540_3541delinsTT (p.(E1180D,Q1181Ter)) | Missense + delins/nonsense | Compound het | [PMID: 31427716](https://pubmed.ncbi.nlm.nih.gov/31427716/) |
| p.Pro127Ser + 16p13.11 microdeletion (whole-gene) | Missense unmasked by deletion | Compound (point + CNV) | [PMID: 31044419](https://pubmed.ncbi.nlm.nih.gov/31044419/) |

- **Classification:** Pathogenic/likely pathogenic per ACMG (nonsense/frameshift LOF; missense-unmasked-by-deletion). All are exceedingly rare in population databases.
- **Variant types:** Nonsense, frameshift/delins, missense, and whole-gene deletion (CNV) — all converging on a **loss-of-function / biallelic-null** mechanism.
- **Allele frequency:** All variants are ultra-rare; *MYH11* is strongly LoF-constrained in gnomAD (Finding F008), so these alleles are essentially private/family-specific.
- **Origin:** **Germline**, inherited from carrier (often consanguineous) parents.
- **Functional consequence:** **Loss of function** — absent or markedly reduced SM myosin heavy chain (confirmed by Western blot in [PMID: 31427716](https://pubmed.ncbi.nlm.nih.gov/31427716/)).

**Contrast — dominant *MYH11* variants (NOT MMIHS2).** Heterozygous **dominant-negative** *MYH11* variants cause familial thoracic aortic aneurysm/dissection, and **protein-elongating** heterozygous variants (e.g., c.5819_5820insCA p.Gln1941Asnfs*91; c.5819del p.Pro1940Hisfs*91) cause a **dominant** severe smooth-muscle dysmotility syndrome via a distinct "dominant hypercontractile loss-of-function" mechanism ([PMID: 31944481](https://pubmed.ncbi.nlm.nih.gov/31944481/)). MMIHS2 specifically requires **biallelic null** alleles.

**Genetic heterogeneity of MMIHS (related genes).** *ACTG2* (dominant, most common), and recessive *LMOD1*, *MYLK*, *MYL9*, plus candidate *PDCL3* ([PMID: 28602422](https://pubmed.ncbi.nlm.nih.gov/28602422/), [PMID: 29453416](https://pubmed.ncbi.nlm.nih.gov/29453416/), [PMID: 32621347](https://pubmed.ncbi.nlm.nih.gov/32621347/), [PMID: 38461165](https://pubmed.ncbi.nlm.nih.gov/38461165/)). Approximately 10% of cases lack a variant in known genes, implying further loci.

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes are established for MMIHS2. Sex acts as a phenotype modifier (see Sections 3, 9, 11). No disease-specific epigenetic mechanism is described. A **16p13.11 microdeletion** encompassing *MYH11* is a relevant structural abnormality that can contribute one null allele ([PMID: 31044419](https://pubmed.ncbi.nlm.nih.gov/31044419/)).

---

## Section 5. Environmental Information

**Not applicable.** MMIHS2 is a monogenic recessive disorder. No environmental factors, toxins, radiation, occupational exposures, lifestyle factors, or infectious agents are known to cause or trigger it. (Recurrent bacterial **sepsis** occurs as a *complication* of chronic TPN/central lines and bacterial translocation, not as an etiologic agent — see Sections 11–12.)

---

## Section 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in *MYH11*** (nonsense, frameshift, missense-over-deletion; germline, recessive) **lead to** absent or markedly reduced smooth-muscle myosin heavy chain (SM myosin II) protein. *(Demonstrated — homozygous/compound-het LOF; Western blot shows reduced protein.)*
2. Loss of SM myosin II **results in** failure to assemble functional thick filaments in the smooth-muscle contractile apparatus, so myosin cannot engage actin thin filaments to generate force. *(Inferred from protein function; SMII is "the dominant motor protein driving SMC contraction.")*
3. Absent myosin motor activity **leads to** loss of smooth-muscle contraction in the **detrusor (bladder)** and **intestinal muscularis propria**. *(Demonstrated functionally; mechanistically inferred.)*
4a. **Bladder branch:** Detrusor failure **results in** a non-contractile, massively distended bladder (**megacystis**) → **leads to** upstream **hydroureter** and **hydronephrosis**, and (chronically) **chronic kidney disease**. *(Demonstrated clinically/radiologically.)*
4b. **Intestinal branch:** Muscularis failure **results in** intestinal hypo-/aperistalsis (**intestinal pseudo-obstruction**) → the unused distal bowel remains small-caliber (**microcolon**) and the proximal bowel distends (**abdominal distention**). *(Demonstrated.)*
5. Functional intestinal obstruction **leads to** inability to feed enterally → **TPN dependence** → **TPN-associated cholestatic liver disease, sepsis, and multi-organ failure**, the principal causes of death. *(Demonstrated clinically.)*

Key qualifier: enteric **ganglion cells are present and normal**, and routine histology/EM of *MYH11* visceral myopathy is often near-normal with preserved MYH11 immunostaining — the lesion is **functional (motor deficit)** rather than a gross structural loss of smooth muscle ([PMID: 36571289](https://pubmed.ncbi.nlm.nih.gov/36571289/)): *"Apart from non-specific changes (e.g., muscle hypertrophy and distension-related muscularis propria necrosis), no alterations were identified by routine histopathological evaluation or electron microscopy."*

### Mechanistic detail

**Molecular pathway / contractile apparatus (Finding F004).** *MYH11* encodes SM myosin II, described as *"the dominant motor protein driving SMC contraction"* ([PMID: 42094517](https://pubmed.ncbi.nlm.nih.gov/42094517/)). The MMIHS gene set — *ACTG2, MYH11, LMOD1, MYLK, MYL9* — collectively encodes proteins of the thin/thick-filament and MLCK-phosphorylation axis; *"MYLK, LMOD1, MYL9, and MYH11 encode for various proteins within smooth muscle cells; abnormalities within these proteins lead to abnormal intestinal smooth muscle contractions"* ([PMID: 31848803](https://pubmed.ncbi.nlm.nih.gov/31848803/)). The physiologic contraction cascade is: Ca²⁺/calmodulin → **MLCK (MYLK)** phosphorylates **regulatory myosin light chain (MYL9)** → activated **SM myosin (MYH11)** cross-bridges with **γ-smooth-muscle actin (ACTG2)**, stabilized by **leiomodin (LMOD1)**. MMIHS2 removes the motor itself.

**Cellular process.** Failure of **smooth-muscle-cell contraction** (the core defect). Downstream, chronic distension produces non-specific muscle **hypertrophy** and distension-related **muscularis propria necrosis** ([PMID: 36571289](https://pubmed.ncbi.nlm.nih.gov/36571289/)).

**Protein dysfunction.** **Loss of function** of SM myosin heavy chain — reduced/absent protein rather than a toxic aggregate. (Contrast: dominant *MYH11* disease uses dominant-negative or hypercontractile mechanisms — [PMID: 31944481](https://pubmed.ncbi.nlm.nih.gov/31944481/).)

**Immune involvement.** None primary. Recurrent sepsis is secondary to catheters/TPN and bacterial translocation.

**Tissue-damage mechanisms.** Mechanical over-distension → ischemia/necrosis of muscularis; secondary uropathy (hydronephrosis → CKD) and TPN-associated cholestatic hepatopathy.

**Suggested ontology terms.**
- GO biological process: smooth muscle contraction (GO:0006939); regulation of smooth muscle contraction (GO:0006940); myosin filament assembly (GO:0031034); muscle filament sliding (GO:0030049).
- GO molecular function: microfilament motor activity (GO:0000146); actin binding (GO:0003779).
- GO cellular component: myosin filament (GO:0032982); contractile fiber (GO:0043292); myosin II complex (GO:0016460).
- CL cell types: smooth muscle cell (CL:0000192); smooth muscle cell of the bladder / visceral smooth muscle cell (CL:0000514).
- CHEBI: calcium(2+) (CHEBI:29108); ATP (CHEBI:15422).

---

## Section 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** Urinary bladder (UBERON:0001255) → megacystis; large intestine/colon (UBERON:0001155) → microcolon; small intestine (UBERON:0002108) → hypoperistalsis.
- **Secondary:** Ureter (UBERON:0000056) → hydroureter; kidney (UBERON:0002113) → hydronephrosis, chronic kidney disease; liver (UBERON:0002107) → TPN-associated cholestasis.
- **Body systems:** Digestive/gastrointestinal and urinary (renal) systems are primary.

**Tissue and cell level.**
- Tissue: **visceral (smooth) muscle** — muscularis propria of gut and detrusor of bladder (UBERON:0001135 smooth muscle tissue).
- Cell population: **visceral smooth muscle cells** (CL:0000192 smooth muscle cell; CL:0000514 smooth muscle cell of the bladder/visceral). Enteric neurons/ganglia and interstitial cells of Cajal are **spared** (normal).

**Subcellular level.**
- **Contractile apparatus / myosin filament** (GO:0032982), contractile fiber (GO:0043292), actomyosin cytoskeleton (GO:0042641). The primary compartment is the contractile cytoskeleton, not mitochondria/nucleus/ER/lysosome.

**Localization / laterality.** **Bilateral and diffuse** — both the entire lower urinary tract and the intestinal tract are affected symmetrically (a systemic visceral myopathy, not a focal lesion).

---

## Section 8. Temporal Development

**Onset.** **Congenital.** Megacystis and polyhydramnios are detectable **prenatally** (megacystis on antenatal ultrasound; bowel findings may appear late in gestation — [PMID: 15543490](https://pubmed.ncbi.nlm.nih.gov/15543490/)). ~63–65% of cases are identified by prenatal imaging ([PMID: 27421821](https://pubmed.ncbi.nlm.nih.gov/27421821/)). Symptoms manifest as **neonatal functional bowel obstruction** with distended bladder and microcolon in essentially all patients ([PMID: 26413901](https://pubmed.ncbi.nlm.nih.gov/26413901/)).

**Onset pattern.** Chronic/congenital from birth (not acute or relapsing).

**Progression.** The primary smooth-muscle defect is **stable** (fixed genetic lesion), but the disease **course is progressive** because of accumulating secondary organ injury — TPN-associated liver disease, chronic kidney disease from chronic uropathy, and recurrent sepsis. Disease **duration is lifelong**; there is no self-limited course and no spontaneous remission.

**Critical periods / intervention windows.** The **neonatal period** is critical for diagnosis and establishment of bladder drainage, enteral/parenteral nutrition, and enteric diversion. Preventing TPN-associated liver failure defines the window for considering **isolated intestinal transplant before multivisceral/liver transplant becomes necessary** ([PMID: 41591435](https://pubmed.ncbi.nlm.nih.gov/41591435/)).

---

## Section 9. Inheritance and Population

**Epidemiology.** MMIHS is **ultra-rare** (no precise prevalence/incidence per 100,000 is established; Orphanet ORPHA:2241). Systematic reviews aggregate ~227 total cases across the literature since 1976 ([PMID: 21792650](https://pubmed.ncbi.nlm.nih.gov/21792650/)); MMIHS2 (*MYH11*) is a small minority of these, most published as individual families.

**Inheritance (MMIHS2).** **Autosomal recessive**, biallelic null (Finding F001). Consanguinity is a recurring feature. Penetrance appears **complete** for biallelic null genotypes; **expressivity** varies (sex-associated severity differences). No genetic anticipation (not a repeat-expansion disorder). No established germline mosaicism or founder effect specific to *MYH11* MMIHS2. **Carrier frequency** is very low, consistent with strong gnomAD LoF constraint (Finding F008); heterozygous carriers of *MYH11* null alleles are generally unaffected for MMIHS (though other heterozygous *MYH11* variant classes cause dominant aortic/dysmotility disease).

**Population demographics.**
- **Sex ratio:** Strong **female preponderance** (Findings F003, F005). Across 227 cases, *"A clear preponderance for female infants was found (female 70.6 vs. male 29.4%)"* ([PMID: 21792650](https://pubmed.ncbi.nlm.nih.gov/21792650/)); a 121–135-patient review found *"73% (88/121) of the patients were female"* ([PMID: 27421821](https://pubmed.ncbi.nlm.nih.gov/27421821/)). In an *ACTG2* cohort (n=103), girls had higher rates of microcolon (p=0.009), PN dependency (p=0.003), and death/transplant (p=0.029) ([PMID: 35149643](https://pubmed.ncbi.nlm.nih.gov/35149643/)).
- **Geographic/ethnic distribution:** No specific endemic distribution; cases reported worldwide (e.g., consanguineous kindreds, a Chinese family, a Japanese nationwide cohort). Consanguineous populations are over-represented for recessive forms.
- **Age distribution:** Present at birth; historically few survived beyond infancy, though survivors now reach the second–third decade (oldest historical survivor 24 years).

---

## Section 10. Diagnostics

**Clinical/imaging.** Diagnosis rests on the **clinico-radiological triad**: distended non-obstructed bladder (megacystis) + microcolon + intestinal hypoperistalsis, often with hydronephrosis/hydroureter and malrotation. Imaging (prenatal ultrasound, then neonatal radiographs, contrast studies, ultrasound, MRI) is central; the radiologist frequently first suggests the diagnosis and later monitors for mechanical obstruction vs dysmotility, CKD, and TPN-cholestasis ([PMID: 41591435](https://pubmed.ncbi.nlm.nih.gov/41591435/)).

**Biopsy / histopathology.** Full-thickness intestinal biopsy shows **present, normal ganglion cells** (excluding Hirschsprung) and often near-normal muscle on routine histology/EM, with only non-specific changes (hypertrophy, distension necrosis) and preserved MYH11 immunostaining ([PMID: 36571289](https://pubmed.ncbi.nlm.nih.gov/36571289/), [PMID: 26413901](https://pubmed.ncbi.nlm.nih.gov/26413901/)). Histology alone is therefore insufficient — genetic testing is required for subtype assignment.

**Genetic testing (definitive for MMIHS2).**
- Recommended approach: **NGS gene panel or exome sequencing** covering *ACTG2, MYH11, LMOD1, MYLK, MYL9* (± *PDCL3*), plus **chromosomal microarray (CMA)** to detect CNVs such as 16p13.11 deletions unmasking a *MYH11* allele ([PMID: 38461165](https://pubmed.ncbi.nlm.nih.gov/38461165/), [PMID: 31044419](https://pubmed.ncbi.nlm.nih.gov/31044419/)).
- WES/WGS successfully identified the founding *MYH11* variants ([PMID: 25407000](https://pubmed.ncbi.nlm.nih.gov/25407000/)); trio/targeted exome identified compound-het variants ([PMID: 31427716](https://pubmed.ncbi.nlm.nih.gov/31427716/)).
- Karyotyping/FISH have limited utility except for detecting large structural changes; mitochondrial DNA and repeat-expansion testing are **not applicable**.

**Biomarkers / omics.** No specific circulating biomarker exists. Western blot for MYH11 protein and cDNA analysis are research/confirmatory tools. No validated metabolomic/proteomic diagnostic signature.

**Clinical criteria / differential diagnosis.** Differential includes **Hirschsprung disease** (distinguished by aganglionosis — HP:0002251, absent in MMIHS2), other visceral myopathies/CIPO, *ACTG2*/*LMOD1*/*MYLK*/*MYL9* MMIHS subtypes, prune-belly syndrome, and mechanical obstruction. MMIHS is formally classified among "variants of Hirschsprung's disease" (congenital smooth-muscle-cell disorders with present ganglia) ([PMID: 23943250](https://pubmed.ncbi.nlm.nih.gov/23943250/)).

**Screening.** Prenatal ultrasound (megacystis/polyhydramnios) is the de facto screen. **Carrier and cascade screening** for at-risk families and **prenatal/preimplantation genetic testing** are available once the family's biallelic *MYH11* variants are known.

---

## Section 11. Outcome / Prognosis

**Survival/mortality.**

| Cohort | N | Female % | Survival | Notes | PMID |
|---|---|---|---|---|---|
| Systematic review 1976–2011 | 227 | 70.6% | 19.7% (43/218); oldest survivor 24 y | Deaths: sepsis, malnutrition, MOF | [21792650](https://pubmed.ncbi.nlm.nih.gov/21792650/) |
| Urologic-focus review | ~121–135 | 73% | 57% (68/121) | 15% transplant; 63% prenatal detection | [27421821](https://pubmed.ncbi.nlm.nih.gov/27421821/) |
| Japan nationwide survey | 19 | 84% (16/19) | 5-y 63%, 10-y 57% | 16/19 needed PN; 9 died (sepsis/liver failure) | [26413901](https://pubmed.ncbi.nlm.nih.gov/26413901/) |
| *ACTG2* cohort (related) | 103 | 52% | 25.7% died, 5.8% transplant | Girls worse outcomes | [35149643](https://pubmed.ncbi.nlm.nih.gov/35149643/) |

Modern management (TPN, intestinal rehabilitation, multivisceral transplant) now allows survival **into the second decade of life** ([PMID: 41591435](https://pubmed.ncbi.nlm.nih.gov/41591435/)). Overall modern survival is roughly **55–65%**. Main causes of death are *"sepsis, malnutrition and multiple organ failure"* ([PMID: 21792650](https://pubmed.ncbi.nlm.nih.gov/21792650/)).

**Morbidity/function.** Very high: lifelong PN dependence, bladder drainage, enteric stomas; chronic complications include TPN-cholestatic liver disease, CKD, and recurrent sepsis. Disability is substantial.

**Complications.** Sepsis, malnutrition/multiple-organ failure (leading causes of death); TPN-associated liver failure; chronic kidney disease.

**Prognostic factors.** **Female sex** predicts worse outcomes (higher microcolon, PN dependence, death/transplant — [PMID: 35149643](https://pubmed.ncbi.nlm.nih.gov/35149643/)); early onset (<2 y) associates with full MMIHS features. Development of TPN-liver failure is a key adverse prognostic event driving transplant need. Successful transplantation can restore enteral autonomy ([PMID: 23167913](https://pubmed.ncbi.nlm.nih.gov/23167913/)).

---

## Section 12. Treatment

**No disease-specific pharmacotherapy exists** (Finding F006). In the Japanese cohort, *"although various medications were given, the patients did not show significant improvement"* ([PMID: 26413901](https://pubmed.ncbi.nlm.nih.gov/26413901/)). Prokinetics and related drugs are ineffective because the defect is the absence of the myosin motor itself. Management is **supportive and surgical**:

**Nutritional / supportive.**
- **Total parenteral nutrition (TPN)** and **intestinal rehabilitation** — mainstay for enteral failure (NCIT: Total Parenteral Nutrition). 16/19 patients required PN in the Japanese cohort ([PMID: 26413901](https://pubmed.ncbi.nlm.nih.gov/26413901/)).
- Prophylactic antibiotics for urinary/enteric infection.

**Urologic.**
- **Clean intermittent catheterization** or **vesicostomy** for bladder drainage (30% [22/73] had vesicostomy) ([PMID: 27421821](https://pubmed.ncbi.nlm.nih.gov/27421821/)) (NCIT: Vesicostomy; Intermittent Catheterization).

**Enteric/surgical diversion.**
- Gastrostomy, ileostomy, jejunostomy for decompression/venting ([PMID: 27421821](https://pubmed.ncbi.nlm.nih.gov/27421821/)) (NCIT: Gastrostomy; Ileostomy).

**Transplantation (definitive).**
- **Isolated intestinal transplantation** restored enteral autonomy: *"We report an eight-yr-old patient with MMIHS who was treated with isolated intestinal transplantation. She had completely oral intake during the four yr of follow-up"* ([PMID: 23167913](https://pubmed.ncbi.nlm.nih.gov/23167913/)) (NCIT: Intestinal Transplantation).
- **Combined living-related liver + bowel transplantation** restored enteral autonomy when TPN-liver failure developed ([PMID: 18280270](https://pubmed.ncbi.nlm.nih.gov/18280270/)) (NCIT: Liver Transplantation; Multivisceral Transplantation).
- **Multivisceral transplantation** used when TPN-associated liver failure supervenes; ~15% (18/116) of patients received intestinal/multivisceral transplant ([PMID: 27421821](https://pubmed.ncbi.nlm.nih.gov/27421821/)).

**Advanced / experimental therapeutics.** No approved gene therapy, cell therapy, RNA-based, targeted, or immunotherapy exists for MMIHS2. Given the biallelic-null LOF mechanism, **gene-replacement strategies** are conceptually attractive but remain **experimental/preclinical**. No pharmacogenomic guidance applies.

**Treatment strategy.** Neonatal stabilization → bladder drainage + enteric diversion + PN → intestinal rehabilitation → **transplantation** if PN fails or TPN-liver disease develops. Personalized care depends on genetic confirmation for counseling and family planning.

---

## Section 13. Prevention

Because MMIHS2 is a fully penetrant recessive Mendelian disorder, prevention is **genetic/reproductive**, not lifestyle-based.

- **Primary prevention:** Not achievable by risk-factor modification. **Genetic counseling** for consanguineous/at-risk couples; **carrier testing** once family variants are known; **prenatal diagnosis** and **preimplantation genetic testing (PGT)** to prevent recurrence.
- **Secondary prevention:** **Prenatal ultrasound** detection of megacystis/polyhydramnios enables early diagnosis and planning ([PMID: 15543490](https://pubmed.ncbi.nlm.nih.gov/15543490/), [PMID: 27421821](https://pubmed.ncbi.nlm.nih.gov/27421821/)).
- **Tertiary prevention (complication avoidance):** Meticulous line/TPN management to prevent sepsis and cholestatic liver disease; timely transplant referral; upper-urinary-tract protection to limit CKD ([PMID: 41591435](https://pubmed.ncbi.nlm.nih.gov/41591435/)).
- **Immunization / public-health / environmental interventions / prophylactic drugs:** Not applicable to disease causation; standard infection prophylaxis applies to catheter/TPN care.
- **Counseling:** **Genetic counseling** is central — recurrence risk is 25% for future pregnancies of carrier couples; cascade testing offered to relatives.

---

## Section 14. Other Species / Natural Disease

**Orthologous genes (Finding F007; HomoloGene 128512):**

| Species | Gene | NCBI Gene ID | Database |
|---|---|---|---|
| Mouse (*Mus musculus*, NCBI Taxon 10090) | *Myh11* | 17880 | MGI |
| Rat (*Rattus norvegicus*, 10116) | *Myh11* | 24582 | RGD |
| Zebrafish (*Danio rerio*, 7955) | *myh11a* | 554168 | ZFIN |
| Chicken (*Gallus gallus*, 9031) | *MYH11* | 396211 | — |
| Dog (*Canis lupus familiaris*, 9615) | *MYH11* | 479836 | — |
| Cow (*Bos taurus*, 9913) | *MYH11* | 530050 | — |

**Natural disease in animals.** No well-characterized naturally occurring *MYH11*-MMIHS analog is documented in companion animals or wildlife (no established OMIA entry identified in this investigation). **Comparative biology** shows the smooth-muscle contractile pathway is deeply conserved across vertebrates, supporting mechanistic translation from model organisms. **No zoonotic potential** (genetic disease).

---

## Section 15. Model Organisms

**Mouse (*Mus musculus*) — the principal model (Finding F002).**
- A **Myh11 knockout / haploinsufficiency mouse** recapitulates core MMIHS features: *"Myh11 deficiency leads to significant bladder enlargement, smooth muscle thickening, collagen accumulation, and voiding dysfunction, establishing a good disease model for MMIHS"* ([PMID: 41797110](https://pubmed.ncbi.nlm.nih.gov/41797110/)).
- Earlier work cited by the founding human study noted that loss of *Myh11* function in mice produces a bladder and intestinal phenotype "highly reminiscent of MMIHS" ([PMID: 25407000](https://pubmed.ncbi.nlm.nih.gov/25407000/)).

**Model types available.** Constitutive knockout, haploinsufficient (heterozygous), and conditional/lineage models exist; *Myh11-CreER* driver lines are widely used for smooth-muscle-specific gene manipulation (e.g., *Myh11CreER;Yy1fl/fl*, *Myh11CreER;Mettl3fl/fl* — [PMID: 40795179](https://pubmed.ncbi.nlm.nih.gov/40795179/)), and a **CRISPR knock-in EGFP-SMII** mouse enables live imaging of myosin filament dynamics ([PMID: 42094517](https://pubmed.ncbi.nlm.nih.gov/42094517/)).

**Phenotype recapitulation.** Good for the **bladder** phenotype (megacystis, voiding dysfunction, muscle thickening, collagen accumulation). Recapitulation of the full **microcolon / intestinal-aperistalsis** triad and neonatal lethality is less completely characterized in the reviewed literature.

**Limitations.** Constitutive *Myh11* null mice may have confounding vascular/aortic phenotypes (heterozygous *MYH11* causes aortic disease), and mouse gut anatomy/physiology differs from human; the human microcolon feature and TPN-dependence course are not fully modeled.

**Applications.** Study of smooth-muscle contractile mechanics, bladder/voiding physiology, myosin-filament assembly dynamics, and preclinical testing of interventions.

**In vitro / other systems.** Rat aortic SMC lines (A7R5) and patient-derived approaches inform SMII biology; iPSC-derived smooth muscle and organoid models are plausible but not established for MMIHS2 in the reviewed literature. **Resources:** MGI, RGD, ZFIN, IMPC/IMSR.

---

## Mechanistic Model / Interpretation

```
   Biallelic LOF variants in MYH11 (16p13.11)
   (nonsense / frameshift / missense-over-deletion; germline, recessive)
                     │  [Western blot: reduced MYH11 protein]
                     ▼
   Absent / reduced SM myosin II (the dominant SMC motor protein)
                     │  (no functional thick filaments to engage actin)
                     ▼
   Failure of smooth-muscle-cell CONTRACTION (functional, not structural)
        │                                            │
        ▼ (bladder branch)                           ▼ (gut branch)
   Detrusor fails --> MEGACYSTIS               Muscularis fails --> hypo/aperistalsis
        │                                            │
        ▼                                            ▼
   Hydroureter --> Hydronephrosis          MICROCOLON (unused bowel) +
        │                                   abdominal distention
        ▼                                            │
   Chronic kidney disease                            ▼
                                          Enteral failure --> TPN dependence
                                                       │
                                                       ▼
                                    TPN-cholestatic liver disease, SEPSIS,
                                    multi-organ failure --> leading cause of death
                                                       │
                                                       ▼
                                    Rescue: isolated intestinal / multivisceral
                                    (+/- liver) transplantation --> enteral autonomy

   NB: Enteric ganglia + interstitial cells of Cajal are NORMAL
       (distinguishes MMIHS from Hirschsprung disease).
```

**Upstream vs downstream.** The **mutation → protein loss → contractile failure** steps are upstream and demonstrated at the molecular level. The **organ-level distension, microcolon, uropathy, and TPN-related complications** are downstream, demonstrated clinically/radiologically. The gut and bladder branches are parallel consequences of the same single lesion.

**Genotype–phenotype logic.** *MYH11* is a "double-hit-dependent" locus: heterozygous null carriers are unaffected for MMIHS (strong gnomAD LoF constraint reflects selection against *other* heterozygous variant classes that cause dominant aortic/dysmotility disease), while **only biallelic null** genotypes cause the recessive MMIHS2 visceral myopathy. This clean loss-of-function logic makes gene replacement a rational (though unproven) therapeutic direction.

---

## Evidence Base

| PMID | Contribution | Supports finding |
|---|---|---|
| [25407000](https://pubmed.ncbi.nlm.nih.gov/25407000/) | First homozygous LOF *MYH11* (p.Lys1200Ter) in MMIHS; mouse phenotype note | F001, F002 |
| [31427716](https://pubmed.ncbi.nlm.nih.gov/31427716/) | Compound-het *MYH11*; Western blot reduced protein | F001 |
| [31044419](https://pubmed.ncbi.nlm.nih.gov/31044419/) | 16p13.11 deletion unmasks missense; states biallelic-null mechanism | F001, F004 |
| [41797110](https://pubmed.ncbi.nlm.nih.gov/41797110/) | *Myh11* KO/haploinsufficient mouse recapitulates megacystis | F002 |
| [31848803](https://pubmed.ncbi.nlm.nih.gov/31848803/) | Contractile-apparatus genes → abnormal smooth-muscle contraction | F004 |
| [36571289](https://pubmed.ncbi.nlm.nih.gov/36571289/) | Near-normal histology/EM → functional (not structural) defect | F004 |
| [42094517](https://pubmed.ncbi.nlm.nih.gov/42094517/) | SMII = dominant motor of SMC contraction; EGFP-SMII model | F004 |
| [27421821](https://pubmed.ncbi.nlm.nih.gov/27421821/) | 73% female; 63% prenatal detection; 15% transplant; 57% survival | F003 |
| [35149643](https://pubmed.ncbi.nlm.nih.gov/35149643/) | Girls worse outcomes (p=0.009/0.003/0.029); *ACTG2* cohort | F003 |
| [21792650](https://pubmed.ncbi.nlm.nih.gov/21792650/) | 227 cases: 70.6% female; 19.7% survival; sepsis/MOF deaths | F005 |
| [23943250](https://pubmed.ncbi.nlm.nih.gov/23943250/) | Classifies MMIHS as a "variant of Hirschsprung's" (ganglia present) | F005 |
| [26413901](https://pubmed.ncbi.nlm.nih.gov/26413901/) | Japan survey: no drug benefit; 5/10-y survival 63/57% | F006 |
| [23167913](https://pubmed.ncbi.nlm.nih.gov/23167913/) | Isolated intestinal transplant → 4 y oral intake | F006 |
| [18280270](https://pubmed.ncbi.nlm.nih.gov/18280270/) | Combined living-related liver+bowel transplant | F006 |
| [41591435](https://pubmed.ncbi.nlm.nih.gov/41591435/) | Modern survival into 2nd decade; imaging/complication surveillance | F003 |
| [31944481](https://pubmed.ncbi.nlm.nih.gov/31944481/) | Dominant *MYH11* mechanism distinct from recessive MMIHS | F001/F008 context |
| [28602422](https://pubmed.ncbi.nlm.nih.gov/28602422/), [29453416](https://pubmed.ncbi.nlm.nih.gov/29453416/), [32621347](https://pubmed.ncbi.nlm.nih.gov/32621347/), [38461165](https://pubmed.ncbi.nlm.nih.gov/38461165/) | Genetic heterogeneity (*MYLK*, *MYL9*, *PDCL3*; landscape review) | Section 4 context |

---

## Limitations and Knowledge Gaps

1. **Small case numbers.** MMIHS2 (*MYH11*-specific) is described in a handful of families; most epidemiologic/survival statistics are drawn from **mixed-genotype MMIHS cohorts** (including the far more common *ACTG2* form), so *MYH11*-specific prognosis and frequencies are extrapolated, not directly measured.
2. **No precise prevalence/incidence** for MMIHS2 exists; the disease is ultra-rare.
3. **Female predominance is unexplained.** The strong female skew (~70%) is well documented but mechanistically unresolved for a nominally autosomal-recessive condition; it may reflect ascertainment, X-linked/hormonal modifiers, or sex-specific smooth-muscle biology — none proven.
4. **Mechanism step 2 (filament-assembly failure) is inferred**, not directly demonstrated in patient tissue; histology is near-normal, so the functional deficit is deduced from protein loss and physiology.
5. **Intestinal-branch modeling is incomplete.** Mouse models robustly show the bladder phenotype; full microcolon/aperistalsis recapitulation is less characterized.
6. **No biomarkers, no disease-specific drug, no gene/cell therapy** — the therapeutic pipeline is empty beyond supportive care and transplantation.
7. **Modifier genes and epigenetics** for MMIHS2 severity are essentially unstudied.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-stratified natural-history study.** Assemble a *MYH11*-specific MMIHS2 registry to derive subtype-specific survival, transplant rates, and complication timelines (vs *ACTG2* and other genes).
2. **Investigate the female-predominance mechanism.** Test for X-linked or sex-hormone modifiers of visceral smooth-muscle contractility in *Myh11*-deficient mice of both sexes; re-examine ascertainment bias.
3. **Complete the intestinal phenotype in models.** Generate/characterize smooth-muscle-conditional *Myh11* knockouts assessing colonic caliber, peristalsis (spatiotemporal mapping), and neonatal survival to fully model the triad.
4. **Preclinical gene-replacement proof-of-concept.** Given the clean biallelic-LOF mechanism, test AAV- or nanoparticle-delivered *MYH11* restoration (or read-through agents for nonsense alleles such as p.Lys1200Ter) in patient-derived iPSC smooth-muscle/organoid systems and mouse models.
5. **Biomarker discovery.** Explore whether circulating SM-myosin fragments, urodynamic parameters, or bowel-motility signatures can serve as diagnostic/prognostic markers and transplant-timing tools.
6. **Refine transplant timing.** Compare outcomes of pre-emptive isolated intestinal transplant versus multivisceral (± liver) transplant after TPN-liver failure develops, to optimize the intervention window.
7. **Prenatal-diagnosis optimization.** Correlate prenatal megacystis/polyhydramnios findings with genetically confirmed MMIHS2 to improve early counseling and PGT uptake in at-risk families.

---

*Report compiled from 9 confirmed findings and 26 reviewed papers. Evidence types span human clinical case reports and systematic reviews (majority), mouse model-organism studies (Myh11 KO/haploinsufficiency), in vitro smooth-muscle biology, and computational/population-genetics constraint data (gnomAD).*


## Artifacts

- [OpenScientist final report](Megacystis-Microcolon-Intestinal_Hypoperistalsis_Syndrome_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Megacystis-Microcolon-Intestinal_Hypoperistalsis_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 16 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0025708` (2 mentions) - the report calls it "MONDO"; MONDO calls it **megacystis-microcolon-intestinal hypoperistalsis syndrome 2**
- `HP:0004388` (1 mention) - the report calls it "Physical/imaging sign"; HP calls it **Microcolon**
- `HP:0004389` (1 mention) - the report calls it "Clinical sign"; HP calls it **Intestinal pseudo-obstruction**
- `HP:0002579` (1 mention) - the report calls it "Clinical sign"; HP calls it **Gastrointestinal dysmotility**
- `HP:0000126` (1 mention) - the report calls it "Imaging sign"; HP calls it **Hydronephrosis**
- `HP:0000072` (1 mention) - the report calls it "Imaging sign"; HP calls it **Hydroureter**
- `HP:0002566` (1 mention) - the report calls it "Structural"; HP calls it **Intestinal malrotation**
- `HP:0001561` (1 mention) - the report calls it "Prenatal sign"; HP calls it **Polyhydramnios**
- `HP:0011968` (1 mention) - the report calls it "Symptom"; HP calls it **Feeding difficulties**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003270` (1 mention) - the report calls it "Clinical sign"; HP calls it **Abdominal distention**, and lists "Abdominal swelling" among its other names
- `GO:0006939` (1 mention) - the report calls it "GO biological process: smooth muscle contraction"; GO calls it **smooth muscle contraction**
- `GO:0000146` (1 mention) - the report calls it "GO molecular function: microfilament motor activity"; GO calls it **microfilament motor activity**, and lists "actin filament motor activity" among its other names
- `GO:0032982` (2 mentions) - the report calls it "GO cellular component: myosin filament", "Contractile apparatus / myosin filament"; GO calls it **myosin filament**
- `CL:0000192` (2 mentions) - the report calls it "CL cell types: smooth muscle cell"; CL calls it **smooth muscle cell**
- `UBERON:0001255` (1 mention) - the report calls it "Primary:** Urinary bladder"; UBERON calls it **urinary bladder**
- `UBERON:0000056` (1 mention) - the report calls it "Secondary:** Ureter"; UBERON calls it **ureter**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:7569` - called "MYH11", "HGNC"
- `GO:0032982` - called "GO cellular component: myosin filament", "Contractile apparatus / myosin filament"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.