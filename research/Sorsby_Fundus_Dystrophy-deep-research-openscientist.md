---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T13:53:07.357835'
end_time: '2026-10-31T14:07:54.892902'
duration_seconds: 887.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Sorsby Fundus Dystrophy
  mondo_id: MONDO:0007640
  category: Mendelian
  causal_genes: TIMP3
  omim_id: OMIM:136900
  synonyms: SFD
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
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 27
  on_topic: 19
  validator_version: 0.4.0
term_validation:
  total_terms: 35
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 9
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: UBERON:0001782
    reported_labels:
    - Bruch's membrane
    - Bruch's membrane (sub-RPE deposits)
    - "macula/retina \u2192 RPE \u2192 Bruch's membrane"
    ontology_label: pigmented layer of retina
  - term_id: HP:0000662
    reported_labels:
    - nyctalopia
    - Progressive
    ontology_label: Nyctalopia
  - term_id: HP:0000512
    reported_labels:
    - abnormal dark adaptation
    - Progressive
    ontology_label: Abnormal electroretinogram
  - term_id: HP:0011506
    reported_labels:
    - choroidal neovascularization
    - Episodic/progressive
    ontology_label: Choroidal neovascularization
  - term_id: HP:0001103
    reported_labels:
    - macular atrophy
    - Progressive
    ontology_label: Abnormal macular morphology
  - term_id: GO:0006919
    reported_labels:
    - TNF-mediated signaling
    ontology_label: obsolete activation of cysteine-type endopeptidase activity involved
      in apoptotic process
  - term_id: UBERON:0005388
    reported_labels:
    - Macula
    ontology_label: photoreceptor array
  - term_id: HP:0030532
    reported_labels:
    - Progressive
    ontology_label: Visual acuity test abnormality
  - term_id: HP:0011505
    reported_labels:
    - Progressive
    ontology_label: Cystoid macular edema
  - term_id: HP:0000603
    reported_labels:
    - Progressive
    ontology_label: Central scotoma
  - term_id: HP:0000532
    reported_labels:
    - Progressive
    ontology_label: Abnormal chorioretinal morphology
  - term_id: NCIT:C1490
    reported_labels:
    - Adalimumab
    ontology_label: Taxane Compound
  - term_id: NCIT:C181947
    reported_labels:
    - CRISPR
    ontology_label: Assay Device Identifier
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0006919
    ontology_label: obsolete activation of cysteine-type endopeptidase activity involved
      in apoptotic process
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Sorsby_Fundus_Dystrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Sorsby_Fundus_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sorsby Fundus Dystrophy
- **MONDO ID:** MONDO:0007640 (if available)
- **Causal gene(s):** TIMP3
- **OMIM:** OMIM:136900
- **Synonyms:** SFD
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Sorsby Fundus Dystrophy** covering all of the
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

# Sorsby Fundus Dystrophy (SFD): Comprehensive Disease Characteristics Report

**Disease:** Sorsby Fundus Dystrophy (SFD) · **Causal gene:** **TIMP3** (Tissue Inhibitor of Metalloproteinases 3)
**MONDO:** MONDO:0007640 · **OMIM:** 136900 (and allelic 188826, TIMP3) · **Gene locus:** 22q12.3 · **Inheritance:** Autosomal dominant, complete penetrance

---

## Summary

Sorsby Fundus Dystrophy is a rare, fully penetrant **autosomal dominant macular degeneration** caused by heterozygous missense mutations in **TIMP3** (Tissue Inhibitor of Metalloproteinases 3; HGNC:11822), located on chromosome 22q12.3. The gene was identified as causal by Weber and colleagues in 1994 ([PMID: 7894485](https://pubmed.ncbi.nlm.nih.gov/7894485/)). The large majority of pathogenic variants are missense changes that introduce or disrupt a **cysteine residue in the C-terminal domain** of TIMP-3 (e.g., Ser179Cys, Tyr168Cys, Tyr191Cys, Ser204Cys), producing an unpaired cysteine that promotes aberrant intermolecular disulfide bonding, protein dimerization/aggregation, and resistance to normal turnover. The misfolded protein is secreted but accumulates abnormally in **Bruch's membrane** beneath the retinal pigment epithelium (RPE), the histologic hallmark of the disease.

The accumulated mutant TIMP-3 drives disease through **three convergent mechanistic arms**: (1) a **degenerative arm**, in which thickened sub-RPE deposits impair nutrient/vitamin-A transport (producing night blindness and delayed dark adaptation) while oxidative and metabolic stress drive RPE death and geographic atrophy; (2) a **neovascular arm**, in which dysregulated TIMP-3/VEGFR2 competition permits choroidal and polypoidal neovascularization; and (3) an inferred **inflammatory arm**, in which loss of TIMP-3's unique inhibition of ADAM17/TACE increases TNF-α signaling. Clinically, patients present in the **third to sixth decade** with nyctalopia and delayed dark adaptation, progressing to macular neovascularization, geographic atrophy, and ultimately widespread chorioretinal atrophy with central then peripheral vision loss.

There is currently **no cure and no approved gene therapy**, but management is meaningful: early **intravitreal anti-VEGF** therapy preserves vision in neovascular disease when initiated promptly, **high-dose vitamin A** can improve rod-mediated dark adaptation, **anti-TNF-α (adalimumab)** controlled refractory neovascular disease in a case report, and **CRISPR base-editing** correction strategies are in preclinical development. Patient-derived iPSC-RPE models now faithfully recapitulate the sub-RPE deposits and have established that **excess accumulation of functional mutant TIMP3** — rather than loss of TIMP-3 function — is the primary driver of pathology.

---

## Key Findings

### Finding 1 — TIMP3 is the causal gene; dominant missense mutations cluster in the C-terminal domain and introduce cysteines

Sorsby Fundus Dystrophy is caused by heterozygous, germline mutations in **TIMP3** on chromosome 22q12.3. Approximately **21 pathogenic variants** are currently reported, predominantly missense substitutions that affect or introduce cysteine residues in the C-terminal domain of the mature protein — including the well-studied **Ser179Cys, Tyr191Cys, and Ser204Cys** variants, as well as Tyr168Cys, Tyr174Cys, Tyr177Cys, Tyr182Cys, Tyr137Cys, and the novel Arg107Cys. The introduction of an odd/unpaired cysteine promotes aberrant intermolecular disulfide bonding and protein dimerization. All reported variants are germline, heterozygous, and classified pathogenic or likely pathogenic under ACMG/AMP criteria.

A 2024 mechanistic review states: *"There are 21 mutations currently associated with SFD, with some variants (e.g., Ser179Cys, Tyr191Cys, and Ser204Cys) having been studied much more than others"* ([PMID: 38601018](https://pubmed.ncbi.nlm.nih.gov/38601018/)). Newly reported variants continue to expand the spectrum, such as the **c.319C>T, p.(Arg107Cys)** variant proposed as likely pathogenic in a 51-year-old woman with presenile cataract and nyctalopia ([PMID: 40714900](https://pubmed.ncbi.nlm.nih.gov/40714900/)), and the **p.Tyr137Cys** variant found in patients initially diagnosed with retinitis pigmentosa ([PMID: 32715858](https://pubmed.ncbi.nlm.nih.gov/32715858/)).

*Ontology suggestions:* Gene — HGNC:11822 (TIMP3); MONDO:0007640 (Sorsby fundus dystrophy); SO:0001583 (missense_variant).

### Finding 2 — Mutant TIMP3 accumulates in Bruch's membrane and drives RPE dysfunction via metabolic, oxidative, and angiogenic derangement

Patient-derived iPSC-RPE carrying TIMP3 **S204C** form thick sub-RPE deposits that recapitulate the SFD donor-eye phenotype. These cells show **reduced transepithelial electrical resistance**, elevated accumulation of TIMP3 monomer and dimer **despite unchanged TIMP3 mRNA**, and increased oxidative stress; CRISPR correction of S204C reverses the phenotype. A key study found SFD iPSC-RPE *"formed significantly more sub-RPE deposits (∼6–90 μm in height) compared to control RPE at 8 weeks"* ([PMID: 34929159](https://pubmed.ncbi.nlm.nih.gov/34929159/)).

Crucially, a proof-of-concept stem-cell study demonstrated that **excess accumulation of mutant TIMP3** — not loss of function — drives SFD. SFD-hiPSC-RPE exhibited *"basolateral accumulation of TIMP3 monomers, despite no change in TIMP3 gene expression"* and *"mutant TIMP3 retained matrix metalloproteinase activity,"* with *"increased expression of ECM proteins, endothelial cell interactions and angiogenesis-related pathways"* ([PMID: 32666594](https://pubmed.ncbi.nlm.nih.gov/32666594/)). This supports a **gain-of-function / toxic-accumulation** model rather than simple haploinsufficiency.

Oxidative stress is a central downstream consequence. S179C mutant mouse RPE shows baseline up-regulation of antioxidant genes and heightened sensitivity to oxidative insult (sodium iodate), indicating *"the presence of a pro-oxidant environment in the RPE in the presence of Timp3 mutations"* ([PMID: 32828705](https://pubmed.ncbi.nlm.nih.gov/32828705/)). Metabolically, *"Mutations in Tissue Inhibitor of Metalloproteinases 3 (TIMP3) cause Sorsby's Fundus Dystrophy (SFD)"* and increase RPE **glycolytic activity** while dysregulating **glutamine metabolism** ([PMID: 39047907](https://pubmed.ncbi.nlm.nih.gov/39047907/)). Post-translational modification matters too: **deglycosylation increases the aggregation and angiogenic properties** of mutant TIMP3 ([PMID: 36430707](https://pubmed.ncbi.nlm.nih.gov/36430707/)).

*Ontology suggestions:* GO:0006979 (response to oxidative stress); GO:0006096 (glycolytic process); GO:0001525 (angiogenesis); CL:0002586 (retinal pigment epithelial cell); UBERON:0001782 (Bruch's membrane).

### Finding 3 — Clinical course: adult-onset night blindness progressing to CNV and geographic atrophy; anti-VEGF preserves vision if treated early

Early symptoms of SFD include **nyctalopia (night blindness), delayed dark adaptation**, and reduced low-luminance/contrast acuity, often with normal photopic best-corrected visual acuity (BCVA) initially. Scotopic testing demonstrates *"a delayed rod-intercept time"* ([PMID: 34352251](https://pubmed.ncbi.nlm.nih.gov/34352251/)), consistent with early rod/dark-adaptation dysfunction. Onset is typically in the **third to sixth decade of life**. The disease course includes drusen-like deposits, rapidly progressive geographic atrophy, and choroidal/polypoidal neovascularization leading to central vision loss ([PMID: 25766588](https://pubmed.ncbi.nlm.nih.gov/25766588/)). A characteristically **reduced late-phase ICG-A fluorescence** is an early sign detectable in asymptomatic carriers and may be useful for early identification of at-risk individuals ([PMID: 25766588](https://pubmed.ncbi.nlm.nih.gov/25766588/)).

Therapeutically, a systematic review of 31 cases (mean follow-up 54 months) *"reported satisfied to excellent responses to anti-VEGF therapy if patients were diagnosed and treated immediately after onset of symptoms,"* with 55% maintaining driving vision ([PMID: 34070857](https://pubmed.ncbi.nlm.nih.gov/34070857/)). High-dose **vitamin A** can improve rod-mediated dark adaptation ([PMID: 34352251](https://pubmed.ncbi.nlm.nih.gov/34352251/); mechanism consistent with the classic rod-plateau findings in [PMID: 9286267](https://pubmed.ncbi.nlm.nih.gov/9286267/)). **Anti-TNF-α (adalimumab)** controlled recurrent neovascularization over 18 months in one patient with the Ser204Cys variant ([PMID: 34376817](https://pubmed.ncbi.nlm.nih.gov/34376817/)).

*Ontology suggestions:* HP:0000662 (nyctalopia); HP:0000512 (abnormal dark adaptation); HP:0007754 (macular dystrophy); HP:0011506 (choroidal neovascularization); HP:0001103 (macular atrophy).

### Finding 4 — Historical gene discovery and human histopathology of the Bruch's membrane deposit

Weber et al. (1994) mapped the SFD locus to 22q13-qter and *"identified point mutations in the TIMP3 gene in affected members of two SFD pedigrees… predicted to disrupt the tertiary structure and thus the functional properties of the mature protein"* ([PMID: 7894485](https://pubmed.ncbi.nlm.nih.gov/7894485/)) — the landmark discovery establishing TIMP3 causality. Six years later, Chong et al. (2000) analyzed a genetically confirmed SFD donor eye and showed that the sub-RPE deposit contained **collagens, elastin, glycosaminoglycans, lipids, and calcium**, with TIMP-3 immunoreactivity *"more extensive in the SFD eye"* and co-localizing with elastin, on a morphologically altered elastic layer of Bruch's membrane ([PMID: 10711711](https://pubmed.ncbi.nlm.nih.gov/10711711/)). This provides the direct human-tissue anchor for the molecular model.

### Finding 5 — Wild-type TIMP-3 is anti-angiogenic via VEGFR2 competition; SFD mutations dysregulate this axis

Wild-type TIMP-3 **competes with VEGF-A for binding to VEGFR2 (KDR)**, inhibiting downstream ERK and AKT phosphorylation and thereby suppressing endothelial proliferation, migration, and capillary formation. One study described *"tissue inhibitor of metalloproteinase (TIMP-3), which competed with vascular endothelial growth factor (VEGF-A) to bind to vascular endothelial growth factor receptor 2 (VEGFR2, KDR). This effect was related to inhibiting the phosphorylation of ERK and AKT"* ([PMID: 32762747](https://pubmed.ncbi.nlm.nih.gov/32762747/)). A TIMP-3-derived peptide (p700) *"binds to and inhibits a number of tyrosine kinase growth factor receptors (VEGFRs1-3, FGFRs 1-4 and PDGFRα)"* ([PMID: 33504102](https://pubmed.ncbi.nlm.nih.gov/33504102/)), confirming the receptor-binding anti-angiogenic activity resides in TIMP-3. In SFD, mutant TIMP-3 dimerization impairs VEGFR2 inhibition ([PMID: 37013036](https://pubmed.ncbi.nlm.nih.gov/37013036/)), and deglycosylation increases its angiogenic properties ([PMID: 36430707](https://pubmed.ncbi.nlm.nih.gov/36430707/)) — providing the mechanistic basis for the choroidal neovascularization seen clinically and the clinical response to anti-VEGF therapy.

*Ontology suggestions:* GO:0001525 (angiogenesis); GO:0048010 (VEGF receptor signaling pathway); GO:0043066 (negative regulation of apoptotic process).

### Finding 6 — TIMP-3 is the physiological inhibitor of ADAM17/TACE (TNF-α sheddase); the inferred inflammatory arm

Among the four TIMPs, **only TIMP-3 inhibits ADAM17/TACE**, the enzyme that sheds TNF-α and TNF receptors. Under basal conditions *"TACE was predominantly present as dimers at the cell surface… enabl[ing] efficient association with tissue inhibitor of metalloproteinase-3 (TIMP3) and silencing of TACE activity,"* while MAPK (ERK/p38) signaling shifts TACE to monomers and relieves inhibition ([PMID: 22550340](https://pubmed.ncbi.nlm.nih.gov/22550340/)). Recombinant TIMP-3 blocks TACE-mediated shedding of TNF-α and TNFR1 in multiple tissues, including corneal epithelium ([PMID: 19407014](https://pubmed.ncbi.nlm.nih.gov/19407014/)) and hepatic ischemia/reperfusion models ([PMID: 17164725](https://pubmed.ncbi.nlm.nih.gov/17164725/)). This provides the biological rationale for anti-TNF (adalimumab) controlling SFD neovascular activity ([PMID: 34376817](https://pubmed.ncbi.nlm.nih.gov/34376817/)). A review frames SFD within a broader context: *"Pathological changes in the ECM of Bruch's membrane have been described in both monogenic IRDs, such as Sorsby fundus dystrophy (SFD) and Doyne honeycomb retinal dystrophy (DHRD), as well as in the genetically complex age-related macular degeneration (AMD)"* ([PMID: 36936905](https://pubmed.ncbi.nlm.nih.gov/36936905/)) — relevant to shared pathomechanism and differential diagnosis. Note: the inflammatory arm is **inferred** from TIMP-3 biology and a single case report, not yet demonstrated in SFD tissue at scale.

*Ontology suggestions:* GO:0006919 (TNF-mediated signaling); GO:0051044 (positive regulation of membrane protein ectodomain proteolysis); CHEBI — TNF-alpha; protein target ADAM17 (HGNC:195).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous missense mutation in TIMP3** (e.g., Ser204Cys) introduces an unpaired cysteine in the C-terminal domain → **leads to** an odd number of cysteine residues in the mature protein.
2. The unpaired cysteine **results in** aberrant intermolecular disulfide bonding → **leads to** mutant TIMP-3 **dimerization and aggregation** (demonstrated: [PMID: 37013036](https://pubmed.ncbi.nlm.nih.gov/37013036/)).
3. The misfolded protein is still secreted and retains MMP-inhibitory activity but **resists normal turnover** → **results in** progressive **accumulation of TIMP-3 in Bruch's membrane** despite normal TIMP3 mRNA levels (demonstrated in iPSC-RPE: [PMID: 32666594](https://pubmed.ncbi.nlm.nih.gov/32666594/), [PMID: 34929159](https://pubmed.ncbi.nlm.nih.gov/34929159/); human tissue: [PMID: 10711711](https://pubmed.ncbi.nlm.nih.gov/10711711/)).
4. Accumulated protein nucleates **thick sub-RPE deposits** containing elastin, collagen, GAGs, lipid, and calcium, thickening and altering Bruch's membrane → **the chain then branches into three arms:**

```
                 ┌─> ARM A (DEGENERATIVE): Thickened Bruch's membrane impairs
                 │     nutrient/vitamin-A transport across RPE  ──> rod dysfunction,
                 │     delayed dark adaptation, NIGHT BLINDNESS (early symptom)
                 │     + pro-oxidant RPE environment & altered glycolysis/glutamine
   Mutant TIMP-3 │     metabolism  ──> RPE death ──> GEOGRAPHIC ATROPHY
   accumulation ─┤
   in Bruch's    ├─> ARM B (NEOVASCULAR): Dysregulated mutant TIMP-3 loses control
   membrane      │     of VEGF-A / VEGFR2 (KDR) competition  ──> endothelial
                 │     ERK/AKT activation ──> CHOROIDAL / POLYPOIDAL NEOVASCULARIZATION
                 │     ──> exudation, hemorrhage, disciform scar ──> CENTRAL VISION LOSS
                 │
                 └─> ARM C (INFLAMMATORY, inferred): Loss of TIMP-3 inhibition of
                       ADAM17/TACE ──> increased TNF-α / TNFR1 shedding ──> local
                       inflammation amplifying neovascular/degenerative injury
```

5. Convergence of the three arms **results in** the full clinical picture: adult-onset nyctalopia → macular neovascularization and/or geographic atrophy → widespread chorioretinal atrophy, fibrosis, and choroidal thinning → **progressive central then peripheral vision loss**.

### Upstream vs downstream

- **Upstream (initiating):** TIMP3 mutation → misfolding/dimerization → Bruch's membrane accumulation. These are shared across all patients and variants and are the logical targets for curative (gene-correction) therapy.
- **Downstream (effector):** oxidative stress, metabolic reprogramming, VEGFR2 dysregulation, TNF-α signaling. These are variant-independent convergence points and the targets of current symptomatic therapy (anti-VEGF, vitamin A, anti-TNF).

### Cell types and tissues

| Level | Structure | Ontology term |
|---|---|---|
| Organ | Eye / retina | UBERON:0000970 / UBERON:0000966 |
| Primary site | Macula | UBERON:0005388 |
| Key membrane | Bruch's membrane (sub-RPE deposits) | UBERON:0001782 |
| Primary cell | Retinal pigment epithelial cell | CL:0002586 |
| Affected cells | Rod photoreceptor (early), cone photoreceptor | CL:0000604 / CL:0000573 |
| Vascular | Choroidal endothelial cells (neovascularization) | CL:0000115 |
| Subcellular | ER (misfolding), extracellular matrix | GO:0005788 / GO:0031012 |

---

## Section-by-Section Disease Characteristics

### 1. Disease Information
SFD is a rare autosomal dominant macular dystrophy with complete penetrance affecting the macula ([PMID: 36197222](https://pubmed.ncbi.nlm.nih.gov/36197222/)). **Identifiers:** OMIM 136900 (phenotype) and 188826 (TIMP3 gene); MONDO:0007640; gene locus 22q12.3. **Synonyms:** SFD, Sorsby's fundus dystrophy, Sorsby pseudoinflammatory macular dystrophy, hereditary hemorrhagic macular dystrophy, fundus dystrophy pseudoinflammatory of Sorsby. Information is derived primarily from **aggregated disease-level resources** (OMIM, Orphanet) and from case series/pedigrees — the disease is rare and no large EHR cohorts exist.

### 2. Etiology
**Primary cause:** monogenic — heterozygous dominant TIMP3 missense mutations (Finding 1). **Genetic risk:** the causal variant is sufficient for disease (complete penetrance); no established modifier genes. **Environmental risk/protective:** none established as causal; oxidative stress is a downstream amplifier, and antioxidant/vitamin-A status may modulate symptom severity (Findings 2, 3). **Gene–environment interaction:** mutant RPE shows heightened sensitivity to oxidative insult ([PMID: 32828705](https://pubmed.ncbi.nlm.nih.gov/32828705/)), suggesting environmental oxidative load could modulate progression, though this is not clinically proven.

### 3. Phenotypes
| Phenotype | Type | Onset | Progression | HPO |
|---|---|---|---|---|
| Night blindness / nyctalopia | Symptom | Early (3rd–6th decade) | Progressive | HP:0000662 |
| Delayed dark adaptation | Functional sign | Early | Progressive | HP:0000512 |
| Reduced contrast/low-luminance acuity | Sign | Early | Progressive | HP:0030532 |
| Drusen-like sub-RPE deposits | Clinical sign | Early–mid | Progressive | HP:0011505 |
| Choroidal/polypoidal neovascularization | Clinical sign | Mid | Episodic/progressive | HP:0011506 |
| Geographic/macular atrophy | Clinical sign | Mid–late | Progressive | HP:0001103 |
| Central scotoma / central vision loss | Symptom | Mid–late | Progressive | HP:0000603 |
| Widespread chorioretinal atrophy | Sign | Late | Progressive | HP:0000532 |

Severity is **moderate-to-severe** and progressive; quality-of-life impact is substantial due to loss of central (reading, driving) and eventually peripheral vision ([PMID: 25766588](https://pubmed.ncbi.nlm.nih.gov/25766588/), [PMID: 34352251](https://pubmed.ncbi.nlm.nih.gov/34352251/)).

### 4. Genetic / Molecular Information
**Causal gene:** TIMP3 (HGNC:11822), 22q12.3. **Variants:** ~21 reported, predominantly **missense** introducing/affecting C-terminal cysteines; classified pathogenic/likely pathogenic (ACMG). Examples: Ser179Cys, Tyr168Cys, Tyr174Cys, Tyr177Cys, Tyr182Cys, Tyr191Cys, Ser204Cys (c.610A>T), Tyr137Cys (c.410A>G), Arg107Cys (c.319C>T), and the c.484G>A variant used in iPSC modeling ([PMID: 38640637](https://pubmed.ncbi.nlm.nih.gov/38640637/)). **Origin:** germline, heterozygous. **Allele frequency:** extremely rare in gnomAD (private/near-private pathogenic variants). **Functional consequence:** toxic gain-of-function via accumulation — mutant protein retains MMP-inhibitory activity ([PMID: 32666594](https://pubmed.ncbi.nlm.nih.gov/32666594/)); dimerization impairs VEGFR2 inhibition ([PMID: 37013036](https://pubmed.ncbi.nlm.nih.gov/37013036/)). **Modifier genes/epigenetics/chromosomal abnormalities:** none established for SFD.

### 5. Environmental Information
No established environmental, lifestyle, or infectious causes. Oxidative stress acts as a **downstream modifier** rather than an environmental cause (Finding 2). SFD is not infectious or zoonotic.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full ordered causal chain and three-arm branching. Molecular pathways: VEGF/VEGFR2–ERK/AKT (angiogenesis), ADAM17/TACE–TNF-α (inflammation), ECM/metalloproteinase homeostasis, glycolysis/glutamine metabolism, oxidative-stress response. Protein dysfunction: misfolding, aberrant disulfide dimerization, aggregation, impaired turnover. Biochemical hallmark: accumulation of a catalytically active but mislocalized/aggregated inhibitor.

### 7. Anatomical Structures Affected
Primary: **macula/retina → RPE → Bruch's membrane** (UBERON:0001782) → choroid. Secondary: photoreceptors (rods early, then cones), choroidal vasculature. Bilateral involvement is the rule, though inter-eye and intra-familial variability occurs ([PMID: 10396378](https://pubmed.ncbi.nlm.nih.gov/10396378/)). Subcellular: ECM, ER. Body system: visual/nervous (special sense).

### 8. Temporal Development
**Onset:** adult, typically 3rd–6th decade; insidious/chronic. Some variants (e.g., Tyr174Cys) present earlier (3rd decade) with dark-adaptation problems, others (Tyr177Cys, Tyr182Cys) in the 6th decade with metamorphopsia/acuity loss ([PMID: 25766588](https://pubmed.ncbi.nlm.nih.gov/25766588/)). **Progression:** chronic, lifelong, progressive — drusen-like deposits → neovascularization and/or geographic atrophy → widespread chorioretinal atrophy. Rate variable even within families ([PMID: 10396378](https://pubmed.ncbi.nlm.nih.gov/10396378/)). **Critical window:** prompt detection and treatment of neovascularization is the key intervention opportunity ([PMID: 34070857](https://pubmed.ncbi.nlm.nih.gov/34070857/)).

### 9. Inheritance and Population
**Inheritance:** autosomal dominant, **complete penetrance**, variable expressivity (including intra-familial). **Epidemiology:** rare (orphan disease; exact prevalence not well established). No anticipation, no documented germline mosaicism specific to SFD. Founder/geographic clustering has been described for specific variants; novel variants reported in Czech families ([PMID: 38612555](https://pubmed.ncbi.nlm.nih.gov/38612555/)). Sex ratio ~equal (autosomal). Carrier frequency not applicable in the recessive sense (dominant disease).

### 10. Diagnostics
**Clinical imaging:** fundus exam (drusen-like deposits, atrophy), **OCT** and **OCT-angiography** (deposits, neovascular membranes), **fundus autofluorescence** (hyper-AF), **ICG-A** (characteristic reduced late-phase fluorescence — early sign, [PMID: 25766588](https://pubmed.ncbi.nlm.nih.gov/25766588/)), **fluorescein angiography**. **Functional:** dark adaptation (delayed rod-intercept time), scotopic/ERG abnormalities ([PMID: 34352251](https://pubmed.ncbi.nlm.nih.gov/34352251/), [PMID: 40714900](https://pubmed.ncbi.nlm.nih.gov/40714900/)). **Genetic testing:** single-gene TIMP3 testing or inherited-retinal-disease gene panels is **definitive and recommended**. **Differential diagnosis:** neovascular AMD (SFD often misdiagnosed as "wet AMD" in young patients, [PMID: 36421778](https://pubmed.ncbi.nlm.nih.gov/36421778/)), retinitis pigmentosa ([PMID: 32715858](https://pubmed.ncbi.nlm.nih.gov/32715858/)), Doyne honeycomb/malattia leventinese (EFEMP1), and other macular dystrophies. A strong family history of early-onset "wet AMD" should prompt TIMP3 testing.

### 11. Outcome / Prognosis
**Not life-limiting** — SFD affects vision, not survival. Prognosis for vision is **guarded but improved by early treatment**: 55% of anti-VEGF-treated patients maintained driving vision ([PMID: 34070857](https://pubmed.ncbi.nlm.nih.gov/34070857/)). Without treatment, bilateral central vision loss and eventual widespread chorioretinal atrophy are expected. **Prognostic factors:** promptness of neovascular detection/treatment is the dominant modifiable factor. Complications: disciform scarring, geographic atrophy, legal blindness.

### 12. Treatment
| Modality | Agent/approach | Evidence | NCIT suggestion |
|---|---|---|---|
| Anti-VEGF (first-line for CNV) | Bevacizumab, ranibizumab, aflibercept | Favorable if early ([PMID: 34070857](https://pubmed.ncbi.nlm.nih.gov/34070857/), [PMID: 25766588](https://pubmed.ncbi.nlm.nih.gov/25766588/)) | NCIT:C2039 (anti-VEGF therapy) |
| Vitamin A supplementation | High-dose vitamin A | Improves dark adaptation ([PMID: 34352251](https://pubmed.ncbi.nlm.nih.gov/34352251/), [PMID: 9286267](https://pubmed.ncbi.nlm.nih.gov/9286267/)) | NCIT:C944 (Vitamin A) |
| Anti-TNF-α | Adalimumab | Controlled refractory CNV (case, [PMID: 34376817](https://pubmed.ncbi.nlm.nih.gov/34376817/)) | NCIT:C1490 (Adalimumab) |
| Corticosteroid | Intravitreal triamcinolone | Inactivated CNV (case, [PMID: 34376817](https://pubmed.ncbi.nlm.nih.gov/34376817/)) | NCIT:C874 (Triamcinolone) |
| Gene correction (experimental) | CRISPR base editing (ABE/GBE) | Preclinical bioinformatic feasibility ([PMID: 36421778](https://pubmed.ncbi.nlm.nih.gov/36421778/)) | NCIT:C181947 (CRISPR) |

No approved gene therapy exists ([PMID: 36197222](https://pubmed.ncbi.nlm.nih.gov/36197222/)). Personalized medicine: base-editing strategies are inherently variant-specific ([PMID: 36421778](https://pubmed.ncbi.nlm.nih.gov/36421778/)).

### 13. Prevention
No primary prevention (monogenic). **Secondary prevention:** cascade genetic testing of at-risk relatives, early ICG-A/OCT surveillance of carriers, and prompt treatment of incipient neovascularization. **Genetic counseling:** autosomal dominant 50% transmission risk; prenatal/preimplantation testing possible for known familial variants. Tertiary prevention: ongoing anti-VEGF for recurrent neovascular disease.

### 14. Other Species / Natural Disease
No naturally occurring SFD analog is established in companion animals or wildlife. The gene is conserved: **Timp3** orthologs exist in mouse (NCBI Gene 21859) and other vertebrates. No zoonotic or cross-species transmission (genetic disease).

### 15. Model Organisms
- **Patient-derived iPSC-RPE** (in vitro): the leading model — recapitulates sub-RPE deposits, reduced TEER, TIMP3 accumulation, oxidative/metabolic stress; CRISPR-correctable ([PMID: 34929159](https://pubmed.ncbi.nlm.nih.gov/34929159/), [PMID: 32666594](https://pubmed.ncbi.nlm.nih.gov/32666594/)). iPSC lines established for S204C and c.484G>A variants ([PMID: 38640637](https://pubmed.ncbi.nlm.nih.gov/38640637/)).
- **Mouse knock-in (Timp3 S179C):** recapitulates pro-oxidant RPE environment and heightened oxidative-stress sensitivity ([PMID: 32828705](https://pubmed.ncbi.nlm.nih.gov/32828705/)).
- **Limitations:** mouse models do not fully reproduce the human macular neovascular phenotype (mice lack a macula); iPSC-RPE lack choroidal vasculature and long-term in-vivo aging. Databases: MGI (mouse), Cellosaurus (iPSC lines).

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [7894485](https://pubmed.ncbi.nlm.nih.gov/7894485/) | *TIMP3 mutations in Sorsby's fundus dystrophy* (Weber 1994) | Landmark gene identification (Finding 4) |
| [10711711](https://pubmed.ncbi.nlm.nih.gov/10711711/) | *TIMP-3, collagen, elastin histopathology of SFD* (Chong 2000) | Human donor-eye deposit composition (Finding 4) |
| [38601018](https://pubmed.ncbi.nlm.nih.gov/38601018/) | *Mechanisms of TIMP-3 accumulation in SFD* (review) | Variant spectrum; 21 mutations (Finding 1) |
| [34929159](https://pubmed.ncbi.nlm.nih.gov/34929159/) | *ECM dysfunction in SFD patient-derived RPE* | iPSC-RPE sub-RPE deposits (Finding 2) |
| [32666594](https://pubmed.ncbi.nlm.nih.gov/32666594/) | *Excess mutant TIMP3 as cause of SFD* | Gain-of-function / accumulation model (Finding 2) |
| [32828705](https://pubmed.ncbi.nlm.nih.gov/32828705/) | *RPE oxidative-stress sensitivity in SFD* | Pro-oxidant RPE; mouse S179C (Finding 2) |
| [39047907](https://pubmed.ncbi.nlm.nih.gov/39047907/) | *TIMP3 mutations alter glycolysis/glutamine* | Metabolic reprogramming (Finding 2) |
| [36430707](https://pubmed.ncbi.nlm.nih.gov/36430707/) | *Deglycosylation increases aggregation/angiogenesis* | PTM modulates pathogenicity (Findings 2, 5) |
| [37013036](https://pubmed.ncbi.nlm.nih.gov/37013036/) | *All SFD mutations cause TIMP3 dimerization impairing VEGFR2* | Unifying dimerization mechanism (Finding 5) |
| [32762747](https://pubmed.ncbi.nlm.nih.gov/32762747/) | *TIMP-3 competes with VEGF-A for VEGFR2* | Anti-angiogenic mechanism (Finding 5) |
| [33504102](https://pubmed.ncbi.nlm.nih.gov/33504102/) | *TIMP3 peptide p700 inhibits VEGFR/FGFR/PDGFR* | Receptor-binding activity (Finding 5) |
| [22550340](https://pubmed.ncbi.nlm.nih.gov/22550340/) | *TACE dimerization and TIMP3 association* | TIMP-3 inhibits ADAM17/TACE (Finding 6) |
| [19407014](https://pubmed.ncbi.nlm.nih.gov/19407014/) | *TIMP-3 blocks TNFR1 shedding in corneal epithelium* | TNF-α axis control (Finding 6) |
| [17164725](https://pubmed.ncbi.nlm.nih.gov/17164725/) | *TIMP-3 inhibits TACE in hepatic injury* | TNF-α axis control (Finding 6) |
| [34376817](https://pubmed.ncbi.nlm.nih.gov/34376817/) | *Anti-TNF-α (adalimumab) for SFD* | Clinical inflammatory-arm support (Findings 3, 6) |
| [34070857](https://pubmed.ncbi.nlm.nih.gov/34070857/) | *Anti-VEGF for SFD MNV: systematic review* | Treatment efficacy (Finding 3) |
| [34352251](https://pubmed.ncbi.nlm.nih.gov/34352251/) | *Visual dysfunction/structure in SFD* | Early rod dysfunction; vitamin A (Finding 3) |
| [25766588](https://pubmed.ncbi.nlm.nih.gov/25766588/) | *Novel mutations, phenotype, treatment* | Phenotype, ICG-A early sign (Finding 3) |
| [36421778](https://pubmed.ncbi.nlm.nih.gov/36421778/) | *CRISPR base editing options in SFD* | Experimental gene correction (Finding 1, Treatment) |
| [36936905](https://pubmed.ncbi.nlm.nih.gov/36936905/) | *ECM microenvironment in retinal disorders* | Shared pathomechanism/DDx (Finding 6) |

**Evidence-type mix:** human clinical/genetic (Findings 1, 3, 4), in vitro iPSC and biochemistry (Findings 2, 5, 6), model organism (mouse S179C, Finding 2), and computational/bioinformatic (base editing, Finding 1).

---

## Limitations and Knowledge Gaps

1. **Inflammatory arm is inferred, not proven in SFD.** The ADAM17/TACE–TNF-α mechanism rests on TIMP-3 biology from non-ocular tissues plus a single SFD case treated with adalimumab ([PMID: 34376817](https://pubmed.ncbi.nlm.nih.gov/34376817/)). TNF-α levels in SFD retina/vitreous have not been systematically quantified.
2. **Conflicting dimerization data.** One iPSC study found TIMP3 dimers in both SFD and control cells and concluded dimerization does *not* drive pathology ([PMID: 32666594](https://pubmed.ncbi.nlm.nih.gov/32666594/)), whereas others argue all SFD mutations converge on dimerization impairing VEGFR2 ([PMID: 37013036](https://pubmed.ncbi.nlm.nih.gov/37013036/)). The precise toxic species (monomer accumulation vs dimer/aggregate) remains unresolved.
3. **No large epidemiological data** — prevalence, incidence, and natural-history cohorts are limited to case series; QoL has not been measured with standardized instruments (EQ-5D/SF-36).
4. **No model fully recapitulates human neovascularization** — mice lack a macula; iPSC-RPE lack choroid.
5. **Genotype–phenotype correlation** (e.g., why Tyr174Cys presents a decade earlier) is incompletely mapped.
6. **No approved disease-modifying therapy** exists; all curative approaches remain preclinical.

---

## Proposed Follow-up Experiments / Actions

1. **Quantify TNF-α/ADAM17 activity directly in SFD models** (iPSC-RPE ± co-cultured immune/endothelial cells and S179C mouse RPE) to test whether the inflammatory arm is active in SFD tissue, and whether adalimumab normalizes it — converting an inferred mechanism to a demonstrated one.
2. **Resolve the toxic-species question** with quantitative, variant-matched assays comparing monomer accumulation, dimer formation, aggregation, and VEGFR2-binding across multiple variants in isogenic iPSC-RPE, reconciling [PMID: 32666594](https://pubmed.ncbi.nlm.nih.gov/32666594/) and [PMID: 37013036](https://pubmed.ncbi.nlm.nih.gov/37013036/).
3. **Advance CRISPR base-editing correction** ([PMID: 36421778](https://pubmed.ncbi.nlm.nih.gov/36421778/)) from bioinformatic feasibility to functional rescue in patient iPSC-RPE, measuring deposit resolution, TEER recovery, and off-target/bystander edits (e.g., the predicted p.Ile205Thr bystander).
4. **Build a prospective natural-history registry** with standardized imaging (OCT, FAF, ICG-A), dark-adaptation testing, and QoL instruments to define progression rates, genotype–phenotype correlations, and treatment windows.
5. **Test antioxidant/vitamin-A combination prophylaxis** in carriers, given the pro-oxidant RPE environment ([PMID: 32828705](https://pubmed.ncbi.nlm.nih.gov/32828705/)) and dark-adaptation benefit of vitamin A ([PMID: 34352251](https://pubmed.ncbi.nlm.nih.gov/34352251/)).
6. **Evaluate deposit-clearance / ECM-remodeling strategies** targeting Bruch's-membrane accumulation upstream of all three disease arms.

---

*Report compiled from a 5-iteration autonomous investigation: 6 confirmed findings, 42 papers reviewed. Evidence spans human clinical/genetic, in vitro iPSC-RPE, mouse model, biochemical, and computational sources.*


## Artifacts

- [OpenScientist final report](Sorsby_Fundus_Dystrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Sorsby_Fundus_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 27 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001782` (3 mentions) - the report calls it "Bruch's membrane", "Bruch's membrane (sub-RPE deposits)", "macula/retina → RPE → Bruch's membrane"; UBERON calls it **pigmented layer of retina**
- `HP:0000662` (2 mentions) - the report calls it "nyctalopia", "Progressive"; HP calls it **Nyctalopia**
- `HP:0000512` (2 mentions) - the report calls it "abnormal dark adaptation", "Progressive"; HP calls it **Abnormal electroretinogram**
- `HP:0011506` (2 mentions) - the report calls it "choroidal neovascularization", "Episodic/progressive"; HP calls it **Choroidal neovascularization**
- `HP:0001103` (2 mentions) - the report calls it "macular atrophy", "Progressive"; HP calls it **Abnormal macular morphology**
- `GO:0006919` (1 mention) - the report calls it "TNF-mediated signaling"; GO calls it **obsolete activation of cysteine-type endopeptidase activity involved in apoptotic process**
- `UBERON:0005388` (1 mention) - the report calls it "Macula"; UBERON calls it **photoreceptor array**
- `HP:0030532` (1 mention) - the report calls it "Progressive"; HP calls it **Visual acuity test abnormality**
- `HP:0011505` (1 mention) - the report calls it "Progressive"; HP calls it **Cystoid macular edema**
- `HP:0000603` (1 mention) - the report calls it "Progressive"; HP calls it **Central scotoma**
- `HP:0000532` (1 mention) - the report calls it "Progressive"; HP calls it **Abnormal chorioretinal morphology**
- `NCIT:C1490` (1 mention) - the report calls it "Adalimumab"; NCIT calls it **Taxane Compound**
- `NCIT:C181947` (1 mention) - the report calls it "CRISPR"; NCIT calls it **Assay Device Identifier**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006919` (obsolete activation of cysteine-type endopeptidase activity involved in apoptotic process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0048010` (1 mention) - the report calls it "VEGF receptor signaling pathway"; GO calls it **vascular endothelial growth factor receptor signaling pathway**, and lists "VEGF receptor signaling pathway" among its other names
- `CL:0000115` (1 mention) - the report calls it "Choroidal endothelial cells (neovascularization)"; CL calls it **endothelial cell**
- `NCIT:C2039` (1 mention) - the report calls it "anti-VEGF therapy"; NCIT calls it **Bevacizumab**, and lists "Anti-VEGF rhuMAb" among its other names
- `NCIT:C944` (1 mention) - the report calls it "Vitamin A"; NCIT calls it **Vitamin**
- `NCIT:C874` (1 mention) - the report calls it "Triamcinolone"; NCIT calls it **Thiamine**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0002586` - called "retinal pigment epithelial cell", "Retinal pigment epithelial cell"
- `UBERON:0001782` - called "Bruch's membrane", "Bruch's membrane (sub-RPE deposits)", "macula/retina → RPE → Bruch's membrane"
- `HP:0000662` - called "nyctalopia", "Progressive"
- `HP:0000512` - called "abnormal dark adaptation", "Progressive"
- `HP:0011506` - called "choroidal neovascularization", "Episodic/progressive"
- `HP:0001103` - called "macular atrophy", "Progressive"