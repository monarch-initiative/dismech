---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-09T01:04:36.389281'
end_time: '2026-11-09T01:21:58.244135'
duration_seconds: 1041.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Occupational Asthma
  disease_slug: Occupational_Asthma
  mondo_id: MONDO:0022742
  category: Complex
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: work-related asthma; occupational allergic asthma; sensitizer-induced
    occupational asthma; irritant-induced asthma
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
citation_count: 41
reference_validation:
  total_references: 41
  verified: 41
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 41
  on_topic: 32
  validator_version: 0.5.1
term_validation:
  total_terms: 41
  verified: 35
  not_found: 0
  obsolete: 1
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 1
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0030828
    reported_labels:
    - Symptom/sign
    ontology_label: Wheezing
  - term_id: HP:0002094
    reported_labels:
    - Symptom
    ontology_label: Dyspnea
  - term_id: HP:0012735
    reported_labels:
    - Symptom
    ontology_label: Cough
  - term_id: HP:0004760
    reported_labels:
    - Symptom
    ontology_label: obsolete Congenital septal defect
  - term_id: HP:0030830
    reported_labels:
    - Functional/lab
    ontology_label: Crackles
  - term_id: HP:0002110
    reported_labels:
    - Lab
    ontology_label: Bronchiectasis
  - term_id: HP:0001880
    reported_labels:
    - Lab abnormality
    ontology_label: Increased total eosinophil count
  - term_id: HP:0003193
    reported_labels:
    - Symptom
    ontology_label: Allergic rhinitis
  - term_id: HP:0000509
    reported_labels:
    - Sign
    ontology_label: Conjunctivitis
  - term_id: UBERON:0001707
    reported_labels:
    - "Secondary involvement:** upper airway \u2014 nasal mucosa/nose"
    ontology_label: nasal cavity
  - term_id: NCIT:C1130
    reported_labels:
    - inhaled corticosteroids
    ontology_label: Hydroxyl Radical
  obsolete_terms:
  - term_id: HP:0004760
    ontology_label: obsolete Congenital septal defect
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Occupational_Asthma-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Occupational_Asthma-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Occupational Asthma
- **MONDO ID:** MONDO:0022742 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** work-related asthma; occupational allergic asthma; sensitizer-induced occupational asthma; irritant-induced asthma
- **Category:** Complex

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Occupational Asthma** covering all of the
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

# Occupational Asthma (MONDO:0022742): A Comprehensive Disease Characteristics Report

**MONDO:0022742** · ICD-11 CA23 (asthma, occupational) · ICD-10 J45 (+ external-cause codes; J68.3 for irritant/RADS) · MeSH "Asthma, Occupational" · no OMIM / no single Mendelian causal gene

> **Causal gene — stated up front, per instructions:** Occupational asthma has **no single Mendelian causal gene.** It is a **complex, polygenic, environmentally-caused disease** in which an occupational inhalational exposure (sensitizer or irritant) is the *necessary* cause and host genetics act as *susceptibility modifiers*. The dominant susceptibility loci are the **HLA class II genes on chromosome 6p21 — principally HLA-DQB1** (with agent-specific haplotypes such as *HLA-DRB1\*15–DPB1\*05* for isocyanates and *HLA-DQ5/DQB1\*0501 + DR1* for acid anhydrides), together with non-HLA modifiers in oxidative-stress and antigen-processing pathways (*GSTM1, GSTP1, CTNNA3, NAT1/2, TNF*). This is a disease defined by its environmental cause plus a polygenic HLA-centred susceptibility background — not by a causal gene.

## Summary

**Occupational asthma (OA)** is a complex, environmentally-caused, adult-onset form of asthma defined by variable airflow limitation and/or airway hyperresponsiveness attributable to causes in the working environment. The *necessary* cause of OA is **workplace exposure** — more than 400 agents are documented — acting upon a **polygenic susceptibility background centred on the HLA class II region** (principally **HLA-DQB1**, with agent-specific haplotypes), supplemented by non-HLA modifier genes in antigen-processing, lymphocyte-activation, cytokine-regulation, and oxidative-stress pathways (e.g., *GSTM1/GSTP1*, *CTNNA3*, *NAT*, *TNF*). OA is therefore categorized as a **complex gene–environment disease**, not a monogenic disorder.

OA is epidemiologically substantial: pooled longitudinal data attribute **~16–17% of adult-onset asthma** to occupational exposures (population attributable fraction). It presents in two mechanistically distinct forms. **Sensitizer-induced (allergic) OA** follows a latency period of exposure and is driven either by **high-molecular-weight (HMW, >10 kDa)** complete protein allergens (flour/grain glycoproteins, enzymes/α-amylase, latex, animal danders, molds) or by **low-molecular-weight (LMW)** chemical **haptens** (isocyanates, acid anhydrides, platinum salts, persulfates, quaternary ammonium compounds) that conjugate to airway proteins to form neoantigens; both converge on an **HLA class II → CD4⁺ Th2 (IL-4/IL-5/IL-13) → IgE / eosinophilic airway inflammation** axis. **Irritant-induced asthma**, including **reactive airways dysfunction syndrome (RADS)**, is a separate non-immunologic entity caused by direct epithelial injury after high-level irritant exposure (classically chlorine, ammonia, acid fumes), characteristically **without a latency period or specific immune sensitization**.

Diagnosis is confirmed by **specific inhalation challenge (SIC)**, the reference standard, supported by spirometry, non-specific bronchial hyperresponsiveness testing, serial peak flow (OASYS), specific IgE, and the complementary inflammatory biomarkers **FeNO** and **sputum eosinophils**. Prognosis is frequently poor: only **~32% symptomatic recovery** after exposure cessation, with **persistent non-specific bronchial hyperresponsiveness in ~73%**. **Complete removal from exposure gives the best clinical outcome but the worst socioeconomic outcome** (income/job loss), the central management trade-off. **Primary prevention by exposure elimination/reduction** is the single most effective intervention, with powder-free low-protein latex gloves providing landmark proof-of-principle. This report synthesizes 12 confirmed findings and 53 reviewed papers across all 15 requested disease-characteristic domains.

---

## Key Findings

### Finding 1 — OA is a complex, environmentally-caused disease with three main phenotypes and no single causal gene

Occupational asthma is asthma caused by workplace conditions. It is subdivided into **sensitizer-induced (allergic) OA** and **irritant-induced (non-allergic) OA**; together with **work-exacerbated asthma (WEA)** — pre-existing asthma made worse but not initially caused by work — these constitute the umbrella category **work-related asthma (WRA)**. More than **400 workplace agents** are implicated. The recognized disease phenotypes are: OA caused by HMW agents, OA caused by LMW agents, irritant-induced asthma, and an OA–COPD overlap phenotype.

As the review by Lemière and colleagues states: *"OA is asthma caused by workplace conditions, and is subdivided into sensitizer-induced (allergic) OA and irritant-induced (nonallergic) OA. WEA is asthma that is made worse, but was not initially caused, by workplace conditions"* ([PMID: 26024347](https://pubmed.ncbi.nlm.nih.gov/26024347/)). The phenotypic subdivision is confirmed by Vandenplas et al.: *"The main phenotypes of occupational asthma are: occupational asthma caused by high-molecular-weight (HMW) or low-molecular-weight (LMW) agents, irritant-induced asthma and occupational asthma-chronic obstructive pulmonary disease overlap"* ([PMID: 33141780](https://pubmed.ncbi.nlm.nih.gov/33141780/)). **Evidence source: human clinical / aggregated disease-level reviews.**

### Finding 2 — Occupational exposures account for ~16–17% of adult-onset asthma

Pooled data from nine longitudinal studies yielded a **population attributable fraction (PAF) of 16%** for the occupational contribution to incident asthma: *"Data from nine longitudinal studies showed a population attributable fraction for the occupational contribution to incident asthma of 16%"* ([PMID: 33141780](https://pubmed.ncbi.nlm.nih.gov/33141780/)). This is independently corroborated by the population-based Telemark 5-year cohort (n=7120), in which new-onset asthma incidence was 7.5 per 1000 person-years, ever exposure to vapour/gas/dust/fumes (VGDF) carried an odds ratio of 1.49 (95% CI 1.15–1.94) with a clear exposure–response (daily exposure OR 2.46, 95% CI 1.39–4.35): *"The corresponding PAF for ever exposed to VGDF was 17% (95% CI 5.4% to 27.8%) and the risk of asthma onset increased with frequent VGDF exposure"* ([PMID: 39277201](https://pubmed.ncbi.nlm.nih.gov/39277201/)). GBD-2021 analysis separately attributed 13.9% of young-adult asthma DALYs to environmental/occupational risks ([PMID: 42323982](https://pubmed.ncbi.nlm.nih.gov/42323982/)). **Evidence source: human epidemiological cohorts.**

### Finding 3 — Causative agents divide into HMW complete allergens and LMW haptens; genetic susceptibility modifies risk

**HMW proteins (>10 kDa)** — flour/grain glycoproteins, fungal α-amylase and other enzymes, natural rubber latex, animal danders, avian and insect proteins, molds — act as **complete allergens** driving IgE sensitization. **LMW agents** — isocyanates, acid anhydrides, metals/platinum salts, quaternary ammonium compounds, persulfates — act as **haptens** that bind airway proteins. Only a subset of exposed workers develop disease, implicating genetic susceptibility. As Cannon et al. summarize: *"OA can be triggered by high-molecular-weight (HMW) proteins that act as complete allergens or by low-molecular-weight (LMW) sensitizers that act as haptens"* ([PMID: 31690384](https://pubmed.ncbi.nlm.nih.gov/31690384/)). A systematic review/meta-analysis of diisocyanate asthma found: *"only a subset of workers exposed to diisocyanates develop diisocyanate-induced occupational asthma (diisocyanate asthma, DA), indicating that genetic susceptibility may play a role"*, with associated gene functions spanning *"antigen processing, lymphocyte activation, cytokine production regulation, and response to oxidative stress"* ([PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/)). **Evidence source: human clinical + genetic meta-analysis.**

### Finding 4 — Specific inhalation challenge is the diagnostic gold standard; prognosis is often poor

Diagnosis combines clinical history, spirometry/bronchodilator responsiveness, non-specific bronchial hyperresponsiveness testing, specific IgE, serial peak-flow analysis (OASYS), and **SIC as the reference standard**: *"specific inhalation challenge (SIC) is considered as the reference standard and represents the best way to confirm the specific cause of WRA"* ([PMID: 33652998](https://pubmed.ncbi.nlm.nih.gov/33652998/)). Specific IgE performance differs by agent class — for HMW agents sensitivity ~0.74/specificity ~0.71, for LMW agents sensitivity 0.28/specificity 0.89. A systematic review of 39 studies (1681 patients) quantified the poor prognosis: *"Reported rates of symptomatic recovery varied from 0% to 100%, with a pooled estimate of 32% (95% CI 26% to 38%)"* and *"The pooled prevalence of persistent NSBHR at follow-up was 73% (95% CI 66% to 79%)"* ([PMID: 17040933](https://pubmed.ncbi.nlm.nih.gov/17040933/)). Severity at diagnosis and airway inflammation predict persistence; early diagnosis and removal improve outcome. **Evidence source: human clinical / systematic review.**

### Finding 5 — HLA class II alleles are the principal susceptibility loci; specific haplotypes confer agent-specific risk

**HLA-DQB1 is the haplotype most associated with occupational asthma**, in contrast to HLA-DRB1 in general allergic asthma and HLA-DPB1 in aspirin-sensitive asthma: *"The most common HLA haplotypes in the different asthma phenotypes are HLA-DRB1 in allergic asthma, HLA-DQB1 in occupational asthma and HLA-DPB1 in aspirin-sensitive asthma"* ([PMID: 24994462](https://pubmed.ncbi.nlm.nih.gov/24994462/)). Agent-specific associations have been mapped:

| Sensitizer | HLA / genetic association | Effect size | PMID |
|---|---|---|---|
| Toluene diisocyanate (TDI) | DRB1\*15–DPB1\*05 haplotype | 10.6% cases vs 0% exposed-asymptomatic, P=0.001 | [16792590](https://pubmed.ncbi.nlm.nih.gov/16792590/) |
| Diisocyanates (MHC SNPs) | HLA-E rs1573294 | OR 6.27 (2.37–16.6) | [24709764](https://pubmed.ncbi.nlm.nih.gov/24709764/) |
| Diisocyanates | HLA-DOA rs3128935 | OR 19.69 | [24709764](https://pubmed.ncbi.nlm.nih.gov/24709764/) |
| Acid anhydrides (HHPA/MHHPA) | HLA-DQ5 / DQB1\*0501 | OR 4.3 (1.7–11) | [15144476](https://pubmed.ncbi.nlm.nih.gov/15144476/) |
| Acid anhydrides | HLA-DR1 | OR 3.0 (1.2–11) | [15144476](https://pubmed.ncbi.nlm.nih.gov/15144476/) |
| Detergent enzyme (subtilisin) | HLA-DQ8 (predisposing) | transgenic mouse | [16185928](https://pubmed.ncbi.nlm.nih.gov/16185928/) |

Notably, **DQB1\*0501 is protective for isocyanate/plicatic-acid asthma while predisposing for anhydride sensitization**, illustrating agent-specific allele effects. Non-HLA modifiers include glutathione-S-transferase genes (*GSTM1/GSTP1*), *CTNNA3*, *NAT*, and *TNF*, acting in oxidative-stress and antigen-processing pathways. Direct quotes: *"the allelic frequency of HLA DRB1\*15-DPB1\*05 in group I (10.6%) was significantly higher than that of group II (0%, P = 0.001)"* ([PMID: 16792590](https://pubmed.ncbi.nlm.nih.gov/16792590/)); *"The linked alleles DQ5 (odds ratio [OR]=4.3; 95% confidence interval [95% CI]=1.7, 11) and DR1 (OR 3.0; 95% CI 1.2, 11) were more prevalent in cases than in referents"* ([PMID: 15144476](https://pubmed.ncbi.nlm.nih.gov/15144476/)); *"The HLA-E rs1573294 and HLA-DPB1 rs928976 SNPs were associated with an increased risk of DA"* ([PMID: 24709764](https://pubmed.ncbi.nlm.nih.gov/24709764/)). **Evidence source: human genetic association studies.**

### Finding 6 — Immunopathogenesis: hapten–protein conjugates drive CD4⁺ Th2 responses with eosinophilic airway inflammation

LMW agents such as diisocyanates react with biological nucleophiles to form **diisocyanate-adducted (hapten–carrier) biomolecules that act as neoantigens**: *"The importance of diisocyanate-adducted biomolecules will be emphasized and their potential contributions to pathogenesis discussed"* ([PMID: 11811926](https://pubmed.ncbi.nlm.nih.gov/11811926/)). Sensitization is associated with recruitment of CD4⁺ T lymphocytes and Th2 cytokine production: *"The diisocyanate-induced sensitization, is associated with the recruitment of CD4 T lymphocytes to the lungs and the production of Th2-type cytokines, including IL-4, IL-5 and IL-13"* ([PMID: 22774468](https://pubmed.ncbi.nlm.nih.gov/22774468/)). A Wistar rat TDI-vapor model confirmed eosinophilic Th2 inflammation: *"marked infiltration of eosinophils in the TDI-exposed rats. The cytokine assay showed that IL-4 and IL-5 were predominantly produced in the BAL fluid in vivo"* ([PMID: 24570807](https://pubmed.ncbi.nlm.nih.gov/24570807/)). Prevalence of diisocyanate asthma among exposed workers is ~5–15%. **Evidence source: human clinical mechanism + rodent model.**

### Finding 7 — Primary prevention by exposure control is the most effective intervention

A systematic review of 29 studies concluded: *"Exposure elimination is the strongest and preferred primary preventive approach to reduce the burden of occupational asthma"* and *"There is strong evidence to recommend not using powdered allergen-rich natural rubber latex gloves"* ([PMID: 22654083](https://pubmed.ncbi.nlm.nih.gov/22654083/)). Interventional proof-of-principle comes from a health-care-worker cohort: *"After the intervention, new latex sensitization rates declined 16-fold, and 25% of previously sensitized employees reverted to negative skin tests"* ([PMID: 21775898](https://pubmed.ncbi.nlm.nih.gov/21775898/)); pre-intervention sensitization was dose-dependent on airborne latex antigen (low 2%, intermediate 8%, high 16%, P<0.0001). Germany's nationwide switch to low-protein powder-free gloves produced a steady decline in reported occupational latex allergy cases after 1998 ([PMID: 12170275](https://pubmed.ncbi.nlm.nih.gov/12170275/)). Management of established disease centres on complete cessation of exposure plus standard asthma pharmacotherapy (inhaled corticosteroids ± bronchodilators; type-2 biologics — omalizumab, mepolizumab, dupilumab, tezepelumab — by extrapolation from severe type-2 asthma). **Evidence source: human clinical / interventional + ecological.**

### Finding 8 — Animal and transgenic models recapitulate sensitizer-induced OA

Validated models include the Wistar rat exposed to TDI vapor (airway hyperresponsiveness, eosinophilic inflammation, IL-4/IL-5 in BAL); **murine models of diisocyanate asthma**, preferred for defined genome and reagent availability (*"Murine models of diisocyanate-induced asthma have proved to be the most useful"*, [PMID: 22774468](https://pubmed.ncbi.nlm.nih.gov/22774468/)); guinea pig and swine models of trimellitic anhydride (*"Animal models revealed sIgG, sIgE, sIgA, and sIgM along with pulmonary lesions, cellular infiltrates, alveolar hemorrhage, and pneumonitis associated with TMA exposure"*, [PMID: 32594360](https://pubmed.ncbi.nlm.nih.gov/32594360/)); and **HLA-DQ8 / HLA class II transgenic mice** reproducing detergent-enzyme hypersensitivity: *"The DQ8 mice also developed allergic eosinophilic inflammatory reactions in the airways following intranasal instillations of this enzyme"* ([PMID: 16185928](https://pubmed.ncbi.nlm.nih.gov/16185928/)). **Evidence source: model organism studies.**

### Finding 9 — Dominant risk factors are exposure intensity/duration, atopy, and concomitant rhinitis/conjunctivitis

Risk of sensitizer-induced OA rises with exposure intensity and duration and with host atopy. A florist study (n=128) found work-related asthma-like symptoms in 14.1%, with *"The most prominent risk factors in florists were work intensity, work duration, and specific atopy"* ([PMID: 15189959](https://pubmed.ncbi.nlm.nih.gov/15189959/)); specific odds ratios were high work intensity OR 7.3 (1.1–51.8), long duration OR 5.1 (1.2–21.6), specific flower atopy OR 5.9 (1.4–24.3), and notably *"excess risk for work-related asthma-like symptoms among those with allergic rhinitis (OR, 13.2; 95% CI, 3.1 to 56.4)"* and conjunctivitis OR 8.4 (2.4–29.2). A pooled laboratory-animal-worker study (n=650) demonstrated the exposure–response for sensitization: *"the likelihood of IgE-mediated sensitization increases with increasing exposure"* ([PMID: 10200019](https://pubmed.ncbi.nlm.nih.gov/10200019/)). Rhinitis frequently precedes/accompanies OA. Smoking is a risk factor for IgE sensitization to some HMW agents (platinum salts, anhydrides). **Evidence source: human epidemiological studies.**

### Finding 10 — FeNO and sputum eosinophils are complementary biomarkers during SIC

A multicenter study (n=321 undergoing SIC, 156 positive) found post-challenge rises in **FeNO** and **sputum eosinophils** had similar diagnostic accuracy (AUC 0.78 and 0.81). Optimal thresholds were defined: *"Increases in FeNO level ≥ 13 ppb and sputum eosinophils ≥ 1.25% were identified as the optimal threshold values for differentiating positive from negative SICs"* — each ≥95% specific but of low sensitivity (55% and 62%) — and *"Combining either a rise in FeNO ≥ 13 ppb or an increase in sputum eosinophils ≥ 1.25% increased the sensitivity to 77%"* ([PMID: 39726396](https://pubmed.ncbi.nlm.nih.gov/39726396/)). Increases were discordant in 38% of positives, indicating complementary information. **Evidence source: human clinical / diagnostic accuracy study.**

### Finding 11 — Irritant-induced asthma / RADS is a distinct non-immunologic phenotype with rapid onset

Irritant-induced OA is a separate non-immunologic entity. **RADS** is an asthma-like syndrome persisting >3 months, beginning within minutes to hours after a single high-concentration irritant exposure: *"RADS is defined as an asthma-like syndrome that persists for >3 months and occurs within minutes to hours after a single exposure to a high concentration of a respiratory irritant"* ([PMID: 31690384](https://pubmed.ncbi.nlm.nih.gov/31690384/)). Chlorine is the most common cause: *"A variety of agents were implicated, with chlorine or chlorine-releasing molecules most frequently reported"* ([PMID: 33063819](https://pubmed.ncbi.nlm.nih.gov/33063819/)); other documented causes include ammonia, acid fumes, lithium hydroxide dust, and β-mercaptoethanol. Unlike sensitizer-induced OA, there is **no latency period and no IgE/specific immune sensitization**. Chronic moderate irritant exposure can also cause **irritant-induced asthma "with latency"**: *"there is epidemiological evidence for irritant-induced asthma with latency from chronic moderate exposure"* ([PMID: 30661311](https://pubmed.ncbi.nlm.nih.gov/30661311/)). Diagnosis uses Brooks (1985)/ACCP 2008 criteria with methacholine challenge (e.g., PC20 1.36–6.74 mg/mL). **Evidence source: human clinical / case series + reviews.**

### Finding 12 — Complete removal gives best clinical but worst socioeconomic outcome; OA imposes major burden

A Cochrane review of workplace interventions found: *"complete removal from exposure resulted in the best outcome in terms of symptoms, lung function, and airway hyper-responsiveness. Reduction of exposure appeared to be less effective in terms of improving asthma but was also less likely to result in loss of income or unemployment"* ([PMID: 23407122](https://pubmed.ncbi.nlm.nih.gov/23407122/)). A follow-up of 125 sensitizer-induced OA patients (median 18 months symptom duration before referral; 79% no longer exposed at 1 year) found unexposed patients had better symptoms (82% vs 53% improved, P=0.023) but *"poorer outcomes in terms of career, income and how they felt treated by their employer"* ([PMID: 32307530](https://pubmed.ncbi.nlm.nih.gov/32307530/)). Diagnostic delay worsens prognosis: *"In adult asthmatics, work-relatedness can account for 15%-33% of cases, but delays in diagnosis remain common and lead to worse outcomes"* ([PMID: 30661311](https://pubmed.ncbi.nlm.nih.gov/30661311/)). **Evidence source: human clinical / systematic review + cohort.**

---

## Full Section-by-Section Report

### 1. Disease Information

**Overview.** Occupational asthma is adult-onset asthma — variable airflow obstruction, airway hyperresponsiveness, and airway inflammation — caused by agents or conditions in the workplace. It is the most common occupational lung disease in industrialized countries and belongs to the broader category of **work-related asthma (WRA)**, which comprises OA (caused by work) and work-exacerbated asthma (worsened by, but not caused by, work) ([PMID: 26024347](https://pubmed.ncbi.nlm.nih.gov/26024347/)).

**Key identifiers.**
- **Mondo:** MONDO:0022742 (occupational asthma)
- **MeSH:** "Asthma, Occupational"
- **ICD-10:** J45 (asthma) with occupational specification; J68.3 (airway disease due to chemical fumes/vapors, for irritant/RADS)
- **ICD-11:** CA23 (asthma) with external-cause coding for occupational origin
- **OMIM:** Not applicable — no single Mendelian causal gene (complex trait)
- **Orphanet:** Not a classic rare-disease entry; captured under occupational respiratory disorders

**Synonyms:** work-related asthma; occupational allergic asthma; sensitizer-induced occupational asthma; irritant-induced asthma; reactive airways dysfunction syndrome (RADS, for acute irritant form).

**Data source type.** Information is derived predominantly from **aggregated disease-level resources** — systematic reviews, occupational cohorts, registries (e.g., SHIELD, SWORD), and challenge-test case series — rather than from individual EHR records.

### 2. Etiology

**Causal factors.** The primary cause is **environmental (occupational inhalational exposure)**, acting on a genetic susceptibility background. There is no infectious etiology. More than 400 agents are implicated, divided into HMW complete allergens and LMW chemical haptens, plus irritant agents ([PMID: 34031758](https://pubmed.ncbi.nlm.nih.gov/34031758/), [PMID: 31690384](https://pubmed.ncbi.nlm.nih.gov/31690384/)).

**Genetic risk factors.** HLA class II alleles, principally **HLA-DQB1**, are the dominant susceptibility loci, with agent-specific haplotypes (Finding 5). Non-HLA modifiers: *GSTM1/GSTP1* (oxidative stress), *CTNNA3*, *NAT*, *TNF* ([PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/), [PMID: 24994462](https://pubmed.ncbi.nlm.nih.gov/24994462/)).

**Environmental/occupational risk factors.** Exposure intensity and duration (exposure–response relationship), high-risk occupations (bakers, farmers, spray painters, isocyanate/plastics workers, health-care workers, cleaners, woodworkers, laboratory-animal workers), atopy, and smoking (for some HMW agents) ([PMID: 15189959](https://pubmed.ncbi.nlm.nih.gov/15189959/), [PMID: 10200019](https://pubmed.ncbi.nlm.nih.gov/10200019/), [PMID: 22794690](https://pubmed.ncbi.nlm.nih.gov/22794690/)). Exposure–response thresholds exist for specific allergens (wheat flour 1–2.4 mg/m³, fungal α-amylase 0.25 ng/m³, latex 0.6 ng/m³, rat allergen 0.7 µg/m³) ([PMID: 9645589](https://pubmed.ncbi.nlm.nih.gov/9645589/)).

**Protective factors.** Reduction/elimination of exposure; engineering controls; respiratory protection (limited evidence); powder-free low-protein latex gloves ([PMID: 22654083](https://pubmed.ncbi.nlm.nih.gov/22654083/)). HLA-DQB1\*0501 is protective for isocyanate/plicatic-acid asthma. No well-established dietary protective factor is specific to OA.

**Gene–environment interactions.** The defining feature of OA: identical exposures produce disease only in genetically susceptible (e.g., HLA-DQB1-defined) individuals, and only a subset of exposed workers (~5–15% for diisocyanates) develop disease ([PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/)).

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Course | Frequency |
|---|---|---|---|---|---|
| Wheezing | Symptom/sign | HP:0030828 | Adult | Episodic, worse at work | Very common |
| Dyspnea | Symptom | HP:0002094 | Adult | Episodic→persistent | Very common |
| Cough | Symptom | HP:0012735 | Adult | Episodic | Common |
| Chest tightness | Symptom | HP:0004760 | Adult | Episodic | Common |
| Airway hyperresponsiveness | Functional/lab | HP:0030830 | Adult | Often persistent (~73%) | Majority |
| Airflow obstruction (↓FEV1) | Lab | HP:0002110 | Adult | Variable/progressive | Majority |
| Sputum/blood eosinophilia | Lab abnormality | HP:0001880 | Adult | Fluctuating | HMW/Th2 disease |
| Allergic rhinitis (often precedes OA) | Symptom | HP:0003193 | Adult | Episodic | Frequent comorbid |
| Conjunctivitis | Sign | HP:0000509 | Adult | Episodic | Frequent comorbid |

Characteristic feature: **symptom improvement away from work (weekends/holidays) and worsening on return** — the clinical hallmark of sensitizer-induced OA. **Quality-of-life impact** is substantial, with career disruption, income loss, and unemployment documented ([PMID: 32307530](https://pubmed.ncbi.nlm.nih.gov/32307530/)).

### 4. Genetic / Molecular Information

**Causal genes:** None (complex disease). **Susceptibility genes:** HLA-DQB1 (HGNC:4944), HLA-DRB1 (HGNC:4948), HLA-DPB1 (HGNC:4940), HLA-E, HLA-DOA, HLA-DQA2; modifiers *GSTM1* (HGNC:4632), *GSTP1* (HGNC:4638), *CTNNA3*, *NAT1/NAT2*, *TNF*. Variants are germline common polymorphisms/SNPs and HLA haplotypes (not classic pathogenic Mendelian variants), classified as **susceptibility alleles**, not ACMG pathogenic variants. Allele frequencies are population-level HLA frequencies. Functional consequences relate to altered antigen presentation (HLA) and reduced detoxification capacity (GST null genotypes → oxidative stress). **Epigenetic/chromosomal abnormalities:** No recurrent chromosomal abnormality; epigenetic contributions are plausible but not yet firmly established ([PMID: 36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/), [PMID: 24709764](https://pubmed.ncbi.nlm.nih.gov/24709764/)).

### 5. Environmental Information

**Environmental/occupational factors.** HMW: wheat/grain flour and glycoproteins, fungal/bacterial enzymes (α-amylase, subtilisin), natural rubber latex, animal danders/urinary proteins, avian proteins, molds. LMW haptens: diisocyanates (TDI, MDI, HDI; CHEBI toluene diisocyanate), acid anhydrides (trimellitic, phthalic, HHPA/MHHPA), platinum salts, persulfates (hairdressing), quaternary ammonium compounds, cleaning/disinfectant chemicals (chloramine, benzalkonium chloride). Irritants: chlorine (CHEBI:17997), ammonia (CHEBI:16134), acid fumes, lithium hydroxide dust, β-mercaptoethanol ([PMID: 34031758](https://pubmed.ncbi.nlm.nih.gov/34031758/), [PMID: 34247391](https://pubmed.ncbi.nlm.nih.gov/34247391/), [PMID: 42427009](https://pubmed.ncbi.nlm.nih.gov/42427009/)).

**Lifestyle factors.** Smoking increases IgE sensitization to some HMW agents (platinum salts, anhydrides). **Infectious agents:** Not applicable — OA is non-infectious (molds and bacterial-derived enzymes act as allergens, not as infections).

### 6. Mechanism / Pathophysiology

**Ordered causal chain — sensitizer-induced (allergic) OA:**

1. **Workplace inhalation exposure** to an HMW allergen or LMW chemical → deposition on the airway epithelium.
2. **(LMW branch)** The hapten reacts with biological nucleophiles (airway/serum proteins, e.g., albumin) → **forms a hapten–carrier conjugate (neoantigen)** [demonstrated for diisocyanates; [PMID: 11811926](https://pubmed.ncbi.nlm.nih.gov/11811926/)]. **(HMW branch)** The intact protein is a complete allergen requiring no conjugation.
3. Antigen uptake by dendritic/antigen-presenting cells and **presentation on HLA class II molecules** (principally HLA-DQ) → **activates CD4⁺ T lymphocytes** in genetically susceptible (HLA-DQB1-defined) hosts [inferred from HLA association + demonstrated CD4⁺ recruitment; [PMID: 24994462](https://pubmed.ncbi.nlm.nih.gov/24994462/), [PMID: 22774468](https://pubmed.ncbi.nlm.nih.gov/22774468/)].
4. CD4⁺ T cells **polarize to Th2** → **secrete IL-4, IL-5, IL-13** → drive **B-cell IgE class-switching** and **eosinophil recruitment/activation** [demonstrated; [PMID: 22774468](https://pubmed.ncbi.nlm.nih.gov/22774468/), [PMID: 24570807](https://pubmed.ncbi.nlm.nih.gov/24570807/)].
5. Re-exposure → IgE-mediated mast-cell degranulation + eosinophilic inflammation → **airway smooth-muscle contraction, mucosal edema, mucus hypersecretion** → **variable airflow obstruction and bronchial hyperresponsiveness** (clinical asthma).
6. Chronic inflammation → **airway remodeling** → **persistent, often irreversible hyperresponsiveness** even after exposure cessation [demonstrated; [PMID: 17040933](https://pubmed.ncbi.nlm.nih.gov/17040933/), [PMID: 18394133](https://pubmed.ncbi.nlm.nih.gov/18394133/)].

**Ordered causal chain — irritant-induced asthma / RADS:**

1. **Single high-concentration irritant exposure** (e.g., chlorine, ammonia, LiOH dust) → **direct toxic epithelial injury** (no immune sensitization, no latency).
2. Epithelial denudation → **neurogenic inflammation, oxidative stress, innate immune activation** → bronchial hyperresponsiveness.
3. Airway injury/repair → **persistent asthma-like syndrome (>3 months)** with bronchial hyperresponsiveness [demonstrated clinically; [PMID: 31690384](https://pubmed.ncbi.nlm.nih.gov/31690384/), [PMID: 42427009](https://pubmed.ncbi.nlm.nih.gov/42427009/)].

**Molecular pathways / GO terms:** antigen processing and presentation via MHC class II (GO:0019886), T-helper 2 cell differentiation (GO:0045064), IL-4/IL-5/IL-13 cytokine signaling, immune response (GO:0006955), eosinophil chemotaxis (GO:0048245), response to oxidative stress (GO:0006979), inflammatory response (GO:0006954). **Cell types / CL terms:** CD4⁺ Th2 lymphocyte (CL:0000899), eosinophil (CL:0000771), mast cell (CL:0000097), dendritic cell (CL:0000451), bronchial epithelial cell (CL:0002328), airway smooth muscle cell (CL:0000192), B cell/plasma cell (CL:0000786). **Upstream:** exposure, hapten conjugation, HLA presentation. **Downstream:** Th2 cytokines, IgE, eosinophilia, remodeling.

### 7. Anatomical Structures Affected

- **Primary organ:** lung / bronchi (UBERON:0002048 lung; UBERON:0002185 bronchus); **body system:** respiratory system (UBERON:0001004).
- **Secondary involvement:** upper airway — nasal mucosa/nose (UBERON:0001707) with occupational rhinitis; conjunctiva (UBERON:0001811) with conjunctivitis.
- **Tissue level:** bronchial/airway epithelium, airway smooth muscle, lamina propria/submucosa.
- **Cell populations (CL):** bronchial epithelial cell (CL:0002328), airway smooth muscle cell (CL:0000192), eosinophil (CL:0000771), CD4⁺ Th2 cell (CL:0000899), mast cell (CL:0000097).
- **Subcellular (GO CC):** MHC class II protein complex (GO:0042613); secretory granules of eosinophils/mast cells.
- **Localization/lateralization:** bilateral, diffuse airway involvement ([PMID: 22794690](https://pubmed.ncbi.nlm.nih.gov/22794690/), [PMID: 31690384](https://pubmed.ncbi.nlm.nih.gov/31690384/)).

### 8. Temporal Development

- **Onset:** adult-onset, work-age. **Sensitizer-induced OA** requires a **latency period** (weeks to years) of exposure for sensitization (insidious/subacute). **RADS** is **acute**, within minutes–hours of a single exposure.
- **Progression:** episodic initially (worse at work, better away), may become persistent/progressive with ongoing exposure and remodeling.
- **Course/duration:** often chronic and lifelong; persistent bronchial hyperresponsiveness in ~73% after cessation ([PMID: 17040933](https://pubmed.ncbi.nlm.nih.gov/17040933/)).
- **Patterns:** partial remission possible after cessation (~32% symptomatic recovery); **critical period** — early diagnosis and prompt removal markedly improve prognosis ([PMID: 9383254](https://pubmed.ncbi.nlm.nih.gov/9383254/), [PMID: 30661311](https://pubmed.ncbi.nlm.nih.gov/30661311/)).

### 9. Inheritance and Population

- **Epidemiology:** OA accounts for ~16–17% of adult-onset asthma (PAF) ([PMID: 33141780](https://pubmed.ncbi.nlm.nih.gov/33141780/), [PMID: 39277201](https://pubmed.ncbi.nlm.nih.gov/39277201/)); work-relatedness 15–33% of adult asthma ([PMID: 30661311](https://pubmed.ncbi.nlm.nih.gov/30661311/)). New-onset asthma incidence ~7.5/1000 person-years in an exposed population cohort.
- **Inheritance pattern:** **multifactorial/polygenic** (not Mendelian). No single-gene inheritance, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier-frequency metrics apply classically; "penetrance" of HLA risk alleles is low and exposure-dependent.
- **Demographics:** occupation-determined rather than ethnicity-determined. Sex ratio reflects workforce composition of exposed industries; age distribution: working adults; geographic distribution follows industrial/agricultural activity ([PMID: 42323982](https://pubmed.ncbi.nlm.nih.gov/42323982/), [PMID: 39212906](https://pubmed.ncbi.nlm.nih.gov/39212906/)).

### 10. Diagnostics

- **Functional tests:** spirometry with bronchodilator responsiveness; **non-specific bronchial hyperresponsiveness** (methacholine/histamine, PC20); **serial peak expiratory flow** at/away from work (OASYS).
- **Immunologic tests:** specific IgE / skin-prick tests (HMW sensitivity ~0.74, specificity ~0.71; LMW sensitivity 0.28, specificity 0.89).
- **Inflammatory biomarkers:** FeNO rise ≥13 ppb and sputum eosinophils ≥1.25% during SIC (each ≥95% specific; combined sensitivity 77%) ([PMID: 39726396](https://pubmed.ncbi.nlm.nih.gov/39726396/)).
- **Reference standard:** **specific inhalation challenge (SIC)** ([PMID: 33652998](https://pubmed.ncbi.nlm.nih.gov/33652998/), [PMID: 22191204](https://pubmed.ncbi.nlm.nih.gov/22191204/)).
- **Genetic/omics testing:** Not used diagnostically — HLA typing is a research tool.
- **Clinical criteria:** work-relatedness by history + objective evidence; RADS by Brooks (1985)/ACCP 2008 criteria.
- **Differential diagnosis:** work-exacerbated (pre-existing) asthma, hypersensitivity pneumonitis (CD4/CD8 <1 on BAL), COPD, eosinophilic bronchitis, vocal cord dysfunction ([PMID: 22794690](https://pubmed.ncbi.nlm.nih.gov/22794690/)).

### 11. Outcome / Prognosis

- **Mortality:** low; OA is rarely directly fatal (though fatal asthma attacks and fatal anaphylaxis to occupational allergens occur).
- **Morbidity/function:** substantial — persistent airflow obstruction, chronic bronchial hyperresponsiveness (~73%), long-term FEV1 decline (median ~79 mL/year in one diisocyanate cohort) ([PMID: 18394133](https://pubmed.ncbi.nlm.nih.gov/18394133/)).
- **Recovery:** only ~32% symptomatic recovery after exposure cessation ([PMID: 17040933](https://pubmed.ncbi.nlm.nih.gov/17040933/)).
- **Prognostic factors:** severity at diagnosis, degree of airway inflammation, duration of symptoms before diagnosis, and promptness of removal. Favourable prognosis is associated with short symptom duration, immediate cessation, and milder hyperresponsiveness at diagnosis ([PMID: 9383254](https://pubmed.ncbi.nlm.nih.gov/9383254/), [PMID: 15764901](https://pubmed.ncbi.nlm.nih.gov/15764901/)).
- **Socioeconomic burden:** career disruption, income/job loss, especially after complete removal ([PMID: 32307530](https://pubmed.ncbi.nlm.nih.gov/32307530/)).

### 12. Treatment

- **Cornerstone:** **removal from / avoidance of the causative exposure** (NCIT: avoidance). Complete removal gives best clinical outcome; reduction is a clinical–socioeconomic compromise ([PMID: 23407122](https://pubmed.ncbi.nlm.nih.gov/23407122/)).
- **Pharmacotherapy** (NCIT): **inhaled corticosteroids** (NCIT:C1130), **short-/long-acting β2-agonists / bronchodilators**, **leukotriene receptor antagonists**, antihistamines — standard asthma therapy extrapolated to OA.
- **Advanced/biologic therapy:** type-2 biologics — **omalizumab** (anti-IgE), **mepolizumab** (anti-IL-5), **dupilumab** (anti-IL-4Rα), **tezepelumab** (anti-TSLP) — effective in severe type-2 asthma and applied by extrapolation to severe type-2 OA ([PMID: 32007172](https://pubmed.ncbi.nlm.nih.gov/32007172/), [PMID: 38878250](https://pubmed.ncbi.nlm.nih.gov/38878250/)).
- **No gene/cell/RNA therapy** applies (no monogenic target).
- **Treatment strategy:** accurate diagnosis → exposure management → pharmacotherapy → monitoring; personalized by phenotype (type-2 vs non-type-2) ([PMID: 33141780](https://pubmed.ncbi.nlm.nih.gov/33141780/), [PMID: 34031758](https://pubmed.ncbi.nlm.nih.gov/34031758/)).

### 13. Prevention

- **Primary prevention (most effective):** exposure **elimination** > reduction; substitution of safer materials; engineering controls; **powder-free low-protein latex gloves** ([PMID: 22654083](https://pubmed.ncbi.nlm.nih.gov/22654083/), [PMID: 21775898](https://pubmed.ncbi.nlm.nih.gov/21775898/), [PMID: 12170275](https://pubmed.ncbi.nlm.nih.gov/12170275/)); enforceable exposure thresholds (TLVs) for allergens ([PMID: 9645589](https://pubmed.ncbi.nlm.nih.gov/9645589/)).
- **Secondary prevention:** medical surveillance of exposed workers; early symptom/sensitization detection; prompt removal ([PMID: 40306950](https://pubmed.ncbi.nlm.nih.gov/40306950/)).
- **Tertiary prevention:** optimizing asthma control, preventing irreversible remodeling.
- **Respiratory protection (PPE):** limited supporting evidence; HEPA-filtered helmets reduce latex symptoms ([PMID: 9847441](https://pubmed.ncbi.nlm.nih.gov/9847441/)).
- **Immunization / genetic counseling:** not applicable.

### 14. Other Species / Natural Disease

- **Species used as models/affected:** rat (*Rattus norvegicus*, NCBITaxon:10116), mouse (*Mus musculus*, NCBITaxon:10090), guinea pig (*Cavia porcellus*, NCBITaxon:10141), swine (*Sus scrofa*, NCBITaxon:9823) — all as experimental models ([PMID: 24570807](https://pubmed.ncbi.nlm.nih.gov/24570807/), [PMID: 32594360](https://pubmed.ncbi.nlm.nih.gov/32594360/)).
- **Natural disease:** OA is fundamentally a human occupational disease; no established naturally-occurring companion-animal equivalent. **Orthologous susceptibility genes** (HLA orthologs — murine H2/I-A/I-E; GST orthologs) exist. **Zoonotic potential:** none (non-infectious).

### 15. Model Organisms

- **Mammalian models:** Wistar rat (TDI vapor) — airway hyperresponsiveness, eosinophilic inflammation, IL-4/IL-5 BAL ([PMID: 24570807](https://pubmed.ncbi.nlm.nih.gov/24570807/)); **murine diisocyanate models** (preferred for defined genome/reagents) ([PMID: 22774468](https://pubmed.ncbi.nlm.nih.gov/22774468/)); guinea pig/swine trimellitic-anhydride models ([PMID: 32594360](https://pubmed.ncbi.nlm.nih.gov/32594360/)).
- **Genetic/humanized models:** **HLA-DQ8 and HLA class II transgenic mice** reproducing detergent-enzyme (subtilisin BPN') hypersensitivity with antigen-specific T-cell responses, airway eosinophilia, and IgG1/IgE ([PMID: 16185928](https://pubmed.ncbi.nlm.nih.gov/16185928/)).
- **Phenotype recapitulation:** models reproduce Th2/eosinophilic airway inflammation, hyperresponsiveness, and HLA-dependent sensitization central to human OA.
- **Limitations:** rodent airway anatomy/immunology differs from human; models capture sensitization/acute inflammation better than chronic remodeling and socioeconomic/persistence aspects.

---

## Mechanistic Model / Interpretation

```
                 WORKPLACE INHALATION EXPOSURE (>400 agents)
                               │
        ┌──────────────────────┼───────────────────────┐
        │                      │                        │
   HMW ALLERGEN          LMW HAPTEN                HIGH-LEVEL IRRITANT
   (flour, latex,        (isocyanate,             (chlorine, ammonia,
    enzymes, dander)      anhydride, Pt)           LiOH, acid fumes)
        │                      │                        │
        │              conjugates to airway            │  direct toxic
   complete            protein → HAPTEN–CARRIER         │  EPITHELIAL INJURY
   allergen            NEOANTIGEN                       │  (no latency,
        │                      │                        │   no sensitization)
        └──────────┬───────────┘                        │
                   ▼                                     │
      HLA CLASS II (DQB1) PRESENTATION ──► CD4⁺ T cell   │
                   │   [requires genetic susceptibility] │
                   ▼                                     │
            Th2 POLARIZATION                             │
         IL-4 / IL-5 / IL-13                             │
                   │                                     │
         ┌─────────┴─────────┐                           │
         ▼                   ▼                           │
    IgE class-switch   EOSINOPHIL recruitment            │
    (mast-cell arming)  + activation                     │
         └─────────┬─────────┘                           │
                   ▼                                     ▼
        AIRWAY INFLAMMATION, SMOOTH-MUSCLE CONTRACTION,
        MUCUS, EDEMA ► VARIABLE AIRFLOW OBSTRUCTION + BHR
                   │
                   ▼
        CHRONIC INFLAMMATION ► AIRWAY REMODELING
                   │
                   ▼
   PERSISTENT / OFTEN IRREVERSIBLE ASTHMA (~73% persistent BHR,
             only ~32% recover after exposure cessation)
```

The unifying interpretation is that **OA is the paradigmatic gene–environment respiratory disease**: an environmental exposure is *necessary* but not *sufficient*, with HLA-class-II-centred genetic susceptibility determining which exposed workers progress to sensitization and disease. The two sensitizer branches (HMW complete allergen; LMW hapten–carrier neoantigen) converge on a shared HLA-II → Th2 → IgE/eosinophil effector axis, while the irritant branch bypasses immunity entirely via direct epithelial toxicity. The therapeutic and preventive corollary follows directly from the causal chain: because the initiating lesion is the exposure, **removing the exposure is both the most effective treatment and the only true primary prevention**, yet it generates a clinical–socioeconomic trade-off that dominates real-world management.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports finding(s) |
|---|---|---|
| [26024347](https://pubmed.ncbi.nlm.nih.gov/26024347/) | Occupational asthma and work-exacerbated asthma | F1 (definition, WRA) |
| [33141780](https://pubmed.ncbi.nlm.nih.gov/33141780/) | Novel approaches in OA diagnosis/management | F1, F2 (phenotypes, 16% PAF) |
| [39277201](https://pubmed.ncbi.nlm.nih.gov/39277201/) | Telemark 5-year follow-up | F2 (17% PAF, exposure-response) |
| [31690384](https://pubmed.ncbi.nlm.nih.gov/31690384/) | Occupational immunologic lung disease | F3, F11 (HMW/LMW, RADS) |
| [36276967](https://pubmed.ncbi.nlm.nih.gov/36276967/) | Genetics of diisocyanate OA (meta-analysis) | F3, F5 (genetic susceptibility) |
| [33652998](https://pubmed.ncbi.nlm.nih.gov/33652998/) | PFT in work-related asthma / SIC | F4 (SIC gold standard) |
| [17040933](https://pubmed.ncbi.nlm.nih.gov/17040933/) | Outcome after cessation (systematic review) | F4, F12 (32% recovery, 73% BHR) |
| [24994462](https://pubmed.ncbi.nlm.nih.gov/24994462/) | HLA and asthma phenotypes | F5 (HLA-DQB1 in OA) |
| [16792590](https://pubmed.ncbi.nlm.nih.gov/16792590/) | DRB1\*15-DPB1\*05 in isocyanate OA | F5 (TDI haplotype) |
| [15144476](https://pubmed.ncbi.nlm.nih.gov/15144476/) | HLA-DQ5/DR1 and acid anhydrides | F5 (anhydride HLA) |
| [24709764](https://pubmed.ncbi.nlm.nih.gov/24709764/) | MHC class I/II SNPs in diisocyanate asthma | F5 (MHC SNPs) |
| [11811926](https://pubmed.ncbi.nlm.nih.gov/11811926/) | Diisocyanate asthma immunopathogenesis | F6 (hapten–carrier adducts) |
| [22774468](https://pubmed.ncbi.nlm.nih.gov/22774468/) | Pathogenetic aspects of diisocyanate asthma | F6, F8 (CD4⁺ Th2, mouse model) |
| [24570807](https://pubmed.ncbi.nlm.nih.gov/24570807/) | IL-4/IL-5 in TDI-exposed Wistar rats | F6, F8 (eosinophilic Th2) |
| [22654083](https://pubmed.ncbi.nlm.nih.gov/22654083/) | Primary prevention: exposure reduction | F7 (prevention hierarchy) |
| [21775898](https://pubmed.ncbi.nlm.nih.gov/21775898/) | Prevention of latex IgE sensitization | F7 (16-fold reduction) |
| [12170275](https://pubmed.ncbi.nlm.nih.gov/12170275/) | German latex prevention program | F7 (national decline) |
| [16185928](https://pubmed.ncbi.nlm.nih.gov/16185928/) | HLA-DQ8 subtilisin hypersensitivity | F5, F8 (transgenic model) |
| [32594360](https://pubmed.ncbi.nlm.nih.gov/32594360/) | Trimellitic anhydride animal models | F8 (TMA models) |
| [15189959](https://pubmed.ncbi.nlm.nih.gov/15189959/) | Work-related symptoms among florists | F9 (risk factors) |
| [10200019](https://pubmed.ncbi.nlm.nih.gov/10200019/) | Rat urinary allergen exposure-response | F9 (exposure-response) |
| [39726396](https://pubmed.ncbi.nlm.nih.gov/39726396/) | FeNO + sputum eosinophils for OA | F10 (biomarkers) |
| [33063819](https://pubmed.ncbi.nlm.nih.gov/33063819/) | Updated review of RADS cases | F11 (chlorine common) |
| [30661311](https://pubmed.ncbi.nlm.nih.gov/30661311/) | Management of OA/WEA update | F11, F12 (latency, delay) |
| [23407122](https://pubmed.ncbi.nlm.nih.gov/23407122/) | Avoidance vs reduction (Cochrane) | F12 (trade-off) |
| [32307530](https://pubmed.ncbi.nlm.nih.gov/32307530/) | Follow-up survey of OA patients | F12 (socioeconomic burden) |
| [9383254](https://pubmed.ncbi.nlm.nih.gov/9383254/) | Prognostic factors TDI-OA | Prognosis (early removal) |
| [18394133](https://pubmed.ncbi.nlm.nih.gov/18394133/) | Inflammation/outcome after cessation | Prognosis (FEV1 decline) |
| [42427009](https://pubmed.ncbi.nlm.nih.gov/42427009/) | RADS from lithium hydroxide dust | F11 (LiOH RADS) |
| [9645589](https://pubmed.ncbi.nlm.nih.gov/9645589/) | Exposure-response thresholds | Prevention (TLVs) |
| [32007172](https://pubmed.ncbi.nlm.nih.gov/32007172/) | Type-2 targeted therapeutics | Treatment (biologics) |

**Concordance and tension.** The evidence base is strongly concordant across human cohorts, systematic reviews, and animal/transgenic models. The principal internal tension is the **clinical–socioeconomic trade-off** (Finding 12): the intervention with the best biological outcome (complete removal) produces the worst livelihood outcome, which the literature resolves pragmatically rather than definitively. A second nuance is the **agent-specific directionality of HLA alleles** (DQB1\*0501 protective for isocyanates yet predisposing for anhydrides), cautioning against treating "HLA susceptibility" as a single uniform risk factor.

---

## Limitations and Knowledge Gaps

1. **No single causal gene / no Mendelian model.** OA is polygenic; HLA and modifier-gene effects are modest, population-dependent, and not clinically actionable for prediction. Genetic testing has no current diagnostic role.
2. **Mechanistic detail is richest for diisocyanates.** The hapten–carrier → HLA-II → Th2 pathway is best demonstrated for isocyanates; mechanisms for many of the 400+ agents are inferred by analogy rather than directly demonstrated.
3. **Irritant-induced asthma / RADS mechanisms** (oxidative/neurogenic epithelial injury) are less molecularly resolved than the allergic pathway, and the boundary between acute RADS and "irritant-induced asthma with latency" is not sharply defined.
4. **Biologic therapy evidence in OA specifically is extrapolated** from severe type-2 asthma trials; no large OA-specific randomized trials of type-2 biologics exist.
5. **Epigenetics, single-cell, and spatial transcriptomics** of occupational airway tissue are largely unexplored — a genuine data gap.
6. **Prognostic prediction** remains imprecise; no validated molecular biomarker predicts who will recover versus develop persistent disease after cessation.
7. **Health-equity dimension:** occupational exposures and OA burden fall disproportionately on low-income and minority workers, and surveillance under-counts these risks ([PMID: 39212906](https://pubmed.ncbi.nlm.nih.gov/39212906/)).

---

## Proposed Follow-up Experiments / Actions

1. **Agent-stratified GWAS / HLA fine-mapping** across multiple sensitizers (isocyanates, anhydrides, flour, enzymes, latex) in harmonized cohorts to resolve shared vs agent-specific susceptibility loci and formalize the HLA-DQB1 signal.
2. **Single-cell and spatial transcriptomics of bronchial biopsies** pre/post specific inhalation challenge to map the dendritic → CD4⁺ Th2 → eosinophil axis in situ and identify remodeling drivers that predict persistence.
3. **Prospective biomarker validation** combining FeNO, sputum eosinophils, periostin, and serum specific-IgE as a multivariate predictor of (a) SIC positivity and (b) post-cessation recovery, enabling risk-stratified removal decisions.
4. **Randomized or pragmatic trials of type-2 biologics specifically in severe sensitizer-induced OA**, including workers unable to fully avoid exposure, to replace current extrapolation with direct evidence.
5. **Mechanistic dissection of RADS** using LiOH/chlorine inhalation models to characterize the oxidative/neurogenic injury pathway and test epithelial-protective interventions.
6. **Implementation research on exposure-elimination programs** (following the latex-glove template) for high-burden agents (flour, cleaning chemicals, isocyanates), coupled with socioeconomic-support interventions that mitigate the income/job-loss penalty of removal.
7. **Enforceable allergen exposure limits (TLVs)** development and surveillance for agents lacking thresholds, extending the demonstrated exposure–response evidence base.

---

*Report compiled from 12 confirmed findings and 53 reviewed papers across all 15 disease-characteristic domains. Evidence types span human epidemiological cohorts, human clinical/diagnostic studies, systematic reviews/meta-analyses, genetic association studies, and rodent/transgenic model-organism studies.*


## Artifacts

- [OpenScientist final report](Occupational_Asthma-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Occupational_Asthma-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 41 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 41 |
| On topic | 32 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 12 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0030828` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Wheezing**
- `HP:0002094` (1 mention) - the report calls it "Symptom"; HP calls it **Dyspnea**
- `HP:0012735` (1 mention) - the report calls it "Symptom"; HP calls it **Cough**
- `HP:0004760` (1 mention) - the report calls it "Symptom"; HP calls it **obsolete Congenital septal defect**
- `HP:0030830` (1 mention) - the report calls it "Functional/lab"; HP calls it **Crackles**
- `HP:0002110` (1 mention) - the report calls it "Lab"; HP calls it **Bronchiectasis**
- `HP:0001880` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Increased total eosinophil count**
- `HP:0003193` (1 mention) - the report calls it "Symptom"; HP calls it **Allergic rhinitis**
- `HP:0000509` (1 mention) - the report calls it "Sign"; HP calls it **Conjunctivitis**
- `UBERON:0001707` (1 mention) - the report calls it "Secondary involvement:** upper airway — nasal mucosa/nose"; UBERON calls it **nasal cavity**
- `NCIT:C1130` (1 mention) - the report calls it "inhaled corticosteroids"; NCIT calls it **Hydroxyl Radical**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0004760` (obsolete Congenital septal defect) (1 mention)