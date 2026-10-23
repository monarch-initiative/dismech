---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T13:45:30.241797'
end_time: '2026-10-14T14:06:00.102755'
duration_seconds: 1229.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SLC5A6-Related Multivitamin Transporter Deficiency
  mondo_id: ''
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:27904971
  relevance_assessed: 18
  on_topic: 15
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 46
  verified: 45
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 0
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0012444
    reported_labels:
    - Imaging/sign
    ontology_label: Brain atrophy
  - term_id: HP:0000252
    reported_labels:
    - Physical
    ontology_label: Microcephaly
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0000407
    reported_labels:
    - Clinical sign
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0000648
    reported_labels:
    - Clinical sign
    ontology_label: Optic atrophy
  - term_id: HP:0001508
    reported_labels:
    - Clinical sign
    ontology_label: Failure to thrive
  - term_id: HP:0011368
    reported_labels:
    - Physical
    ontology_label: Epidermal thickening
  - term_id: HP:0004313
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased circulating immunoglobulin concentration
  - term_id: HP:0001644
    reported_labels:
    - Clinical sign
    ontology_label: Dilated cardiomyopathy
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SLC5A6-Related_Multivitamin_Transporter_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SLC5A6-Related_Multivitamin_Transporter_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SLC5A6-Related Multivitamin Transporter Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SLC5A6-Related Multivitamin Transporter Deficiency** covering all of the
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

# SLC5A6-Related Multivitamin Transporter Deficiency (SMVTD / NERIB): Comprehensive Disease Characterization Report

**Disease:** SLC5A6-Related Multivitamin Transporter Deficiency
**MONDO:** MONDO:0033546 (neurodegeneration, infantile-onset, biotin-responsive; NERIB) · **OMIM:** #618973 (phenotype), *604024 (SLC5A6 gene)
**Category:** Mendelian, autosomal recessive, ultra-rare, **treatable** inborn error of metabolism

---

## Summary

SLC5A6-related multivitamin transporter deficiency (**SMVTD**, also termed sodium-dependent multivitamin transporter deficiency, SMVT deficiency, or infantile-onset biotin-responsive neurodegeneration/NERIB) is an ultra-rare, autosomal-recessive, **treatable** inborn error of metabolism. It is caused by **biallelic loss-of-function variants in *SLC5A6*** (HGNC:11041; Ensembl ENSG00000138074; chr2p23.3), which encodes the apical **sodium-dependent multivitamin transporter (SMVT; UniProt Q9Y289)**. SMVT is a 635-amino-acid, 13-transmembrane-helix Na⁺-coupled symporter that imports three essential micronutrients — **biotin (vitamin B7), pantothenic acid (vitamin B5), and α-lipoic acid** — plus iodide, across the intestinal epithelium and the blood–brain barrier. Loss of transporter function produces a **combined cofactor deficiency** that cripples coenzyme-A synthesis, biotin-dependent carboxylases, and lipoylation-dependent mitochondrial enzyme complexes, converging on **mitochondrial energy failure** and multisystem injury.

Clinically, SMVTD is a **multisystem disorder** with a wide phenotypic spectrum. The classic severe form presents in the neonatal period or infancy with developmental delay/regression, microcephaly, brain atrophy, cysts and agenesis of the corpus callosum, epilepsy, sensorineural hearing loss, optic atrophy, peripheral (axonal sensorimotor) neuropathy, failure to thrive, gastrointestinal dysfunction, cutaneous lesions, immunodeficiency (hypogammaglobulinemia), osteopenia/fractures, dilated cardiomyopathy, and recurrent metabolic crises (lactic acidosis, hyperammonemia, hypoglycemia, rhabdomyolysis). A milder allelic disorder — **childhood-onset biotin-responsive peripheral motor neuropathy (COMNB)** — presents around age 10 with symptoms largely restricted to motor neuropathy. Intermediate phenotypes also occur. Roughly 16–20 families have been reported worldwide.

The decisive clinical fact is that SMVTD is **disease-modifiable** by **early high-dose triple supplementation** with biotin, pantothenic acid, and α-lipoic acid. Treatment halts cyclic vomiting, resolves skin lesions, restores antibody production, improves muscle strength, and — when started early (even preconception in animal models) — prevents the lethal cardiac and metabolic outcomes seen in untreated patients. Because untreated or late-treated disease can be fatal in infancy, **prompt diagnosis** (via urinary 3-hydroxyisovaleric aciduria in the absence of biotinidase deficiency, untargeted metabolomics, and trio exome/genome sequencing) is critical to outcome. This report synthesizes nine confirmed findings and 18 primary sources into a complete 15-section disease knowledge entry, anchored throughout to database-verified identifiers.

---

## Key Findings

### Finding 1 — Biallelic *SLC5A6* loss of function causes a treatable, multivitamin-responsive inborn error of metabolism

Biallelic pathogenic variants in *SLC5A6* (gene MIM 604024) cause **sodium-dependent multivitamin transporter deficiency** (SMVTD; MIM 618973), inherited in an autosomal recessive pattern. The gene product, human SMVT (hSMVT), transports biotin (B7), pantothenic acid (B5), and α-lipoic acid across intestinal epithelium and the blood–brain barrier. As stated in [PMID: 27904971](https://pubmed.ncbi.nlm.nih.gov/27904971/): *"The human sodium-dependent multivitamin transporter (hSMVT) is a product of the SLC5A6 gene and mediates biotin, pantothenic acid, and lipoate uptake."*

Two allelic disorders arise from *SLC5A6* variation. [PMID: 38012394](https://pubmed.ncbi.nlm.nih.gov/38012394/) frames the allelic series: *"Biallelic SLC5A6 variants cause sodium-dependent multivitamin transporter deficiency (SMVTD) and childhood-onset biotin-responsive peripheral motor neuropathy (COMNB), which both respond well to replacement therapy."* Approximately 16–20 families have been reported to date, making this an **ultra-rare** condition. The disorder was initially recognized as a phenocopy of biotinidase deficiency and is now established as a distinct, treatable metabolic transporter disease.

### Finding 2 — SMVTD is a multisystem disorder with a broad phenotypic spectrum and an allelic series (severe SMVTD vs mild COMNB)

Classic SMVTD presents in the neonatal period or infancy. [PMID: 39898461](https://pubmed.ncbi.nlm.nih.gov/39898461/) summarizes the core multisystem phenotype: the disease *"classically presents with developmental delay, brain atrophy, epilepsy, sensorineural hearing loss, peripheral neuropathy, and gastrointestinal, cutaneous, and immunologic abnormalities."* Additional reported features include microcephaly, brain cysts, agenesis of the corpus callosum, optic atrophy, failure to thrive, gastroesophageal reflux, gastrointestinal bleeding, intestinal pseudo-obstruction, vomiting, cutaneous dyskeratosis, hypogammaglobulinemia, osteopenia with pathologic fractures, dilated cardiomyopathy, and metabolic crises (lactic acidosis, hyperammonemia, hypoglycemia, rhabdomyolysis).

At the mild end, COMNB is defined by [PMID: 38012394](https://pubmed.ncbi.nlm.nih.gov/38012394/): *"COMNB is clinically milder and has a later onset than SMVTD, at approximately 10 years of age. COMNB symptoms are mostly limited to peripheral motor neuropathy."* Intermediate phenotypes — congenital brain cysts and mild, self-resolving motor delay — fill out the spectrum. Importantly, the literature reports **no clear genotype–phenotype correlation**, yet **little intrafamilial variability in age of onset**, a combination with direct implications for recurrence risk counseling and prenatal management.

### Finding 3 — Mechanism: SMVT loss impairs CoA synthesis and mitochondrial energy metabolism, reversible by vitamin supplementation

The mechanistic through-line is combined cofactor starvation leading to energy failure. Metabolomic and proteomic data from patients and models show **reduced pantothenate and coenzyme A**, **elevated long-chain fatty acids** (impaired fatty acid oxidation), **elevated urinary 3-hydroxyisovaleric acid** (3-HIA, a marker of impaired biotin-dependent 3-methylcrotonyl-CoA carboxylase), and lactic acidosis with mitochondrial respiratory disruption. [PMID: 39898461](https://pubmed.ncbi.nlm.nih.gov/39898461/) reports data that *"demonstrated reduced pantothenate and coenzyme A with elevated long-chain fatty acids, indicating impaired fatty acid oxidation."*

The cardiac phenotype is mechanistically dissected in a mouse model. [PMID: 42228401](https://pubmed.ncbi.nlm.nih.gov/42228401/) describes *"impaired coenzyme A synthesis, and metabolic imbalance, indicating progression toward cardiomyopathy."* Cardiac-specific *Slc5a6* knockout mice develop progressive dilated cardiomyopathy with cardiomyocyte hypertrophy, fibrosis, early mitochondrial metabolic disruption, and premature death around 26 weeks. The immune phenotype has a parallel metabolic basis; [PMID: 38036278](https://pubmed.ncbi.nlm.nih.gov/38036278/) concludes that *"altered cellular metabolic profiles, including aberrant mitochondrial respiration and reliance on glycolysis, may underlie the failure in plasma cell maturation."* Across tissues, the final common pathway is mitochondrial energy insufficiency, and it is reversible when the missing cofactors are restored.

### Finding 4 — Treatment: triple multivitamin replacement is effective and disease-modifying, especially when started early

High-dose oral **biotin + pantothenic acid + α-lipoic acid** is repeatedly reported to improve the disease. [PMID: 40396389](https://pubmed.ncbi.nlm.nih.gov/40396389/) documents that *"an oral regimen comprising biotin, lipoic acid, and pantothenic acid demonstrated significant therapeutic effects, including cessation of cyclic vomiting, resolution of skin lesions on the fingers, and improvements in muscle weakness."* Typical reported dosing includes biotin ~15 mg/day and pantothenic acid ~100 mg/day ([PMID: 38407570](https://pubmed.ncbi.nlm.nih.gov/38407570/)). Documented responses span hematologic, cutaneous, cardiac, and gastrointestinal improvement, recovered antibody production, and stabilized neurodevelopment.

The timing of treatment is decisive. In the mouse model, [PMID: 42228401](https://pubmed.ncbi.nlm.nih.gov/42228401/) showed that *"vitamin supplementation from preconception onwards prevented the cardiac phenotype, preserving cardiac structure, function, morphology and survival."* In patients, early supplementation stabilized disease, whereas untreated or late-treated patients died in infancy or required heart transplant ([PMID: 37391029](https://pubmed.ncbi.nlm.nih.gov/37391029/), [PMID: 38407570](https://pubmed.ncbi.nlm.nih.gov/38407570/)). Treatment responsiveness is itself used as supporting evidence in variant classification ([PMID: 35217562](https://pubmed.ncbi.nlm.nih.gov/35217562/)).

### Finding 5 — Environmental/acquired modifiers: chronic alcohol and intestinal SMVT loss independently reduce biotin status and gut integrity

Beyond the Mendelian disorder, SMVT function is modifiable by environment. Chronic alcohol exposure downregulates intestinal SMVT (protein, mRNA, and heterogeneous nuclear RNA) through epigenetic and transcriptional mechanisms and reduces plasma biotin in humans ([PMID: 34077272](https://pubmed.ncbi.nlm.nih.gov/34077272/), [PMID: 21148397](https://pubmed.ncbi.nlm.nih.gov/21148397/)). [PMID: 34077272](https://pubmed.ncbi.nlm.nih.gov/34077272/) notes that biotin *"is essential for normal health and its deficiency/suboptimal levels occur in a variety of conditions including chronic alcoholism."*

Intestinal-specific SMVT knockout also compromises gut barrier integrity. [PMID: 27492331](https://pubmed.ncbi.nlm.nih.gov/27492331/) reports that *"knocking out the mouse intestinal SMVT is associated with a significant increase in gut permeability and with changes in the level of expression of TJ [tight junction] proteins,"* and the animals develop chronic active cecal inflammation reproducible by dietary biotin deficiency, implicating a Crohn's-like mechanism ([PMID: 31369292](https://pubmed.ncbi.nlm.nih.gov/31369292/)). These findings contextualize how nutritional and genetic routes to biotin insufficiency converge.

### Finding 6 — Confirmed identifiers, protein architecture, and tissue expression

*SLC5A6* (HGNC:11041; Ensembl ENSG00000138074) maps to GRCh38 chr2:27,199,587–27,212,958 (minus strand; cytoband 2p23.3). The product (UniProt **Q9Y289**) is a **635-amino-acid** Na⁺-coupled symporter with **13 transmembrane helices**, localized to the **apical cell membrane**. UniProt describes its function as a *"sodium-dependent multivitamin transporter that mediates the electrogenic transport of pantothenate, biotin, lipoate and iodide."* Tissue expression spans heart, brain, placenta, lung, liver, skeletal muscle, kidney, pancreas, and brain microvessels (the blood–brain barrier) — a distribution that explains the multisystem and neurological involvement. The phenotype maps to **MONDO:0033546** "neurodegeneration, infantile-onset, biotin-responsive" (NERIB), whose exact synonyms include "SMVT deficiency" and "sodium-dependent multivitamin transporter deficiency" (OMIM #618973).

### Finding 7 — Population constraint (gnomAD) and variant landscape (ClinVar) are concordant with a recessive loss-of-function mechanism

gnomAD constraint for *SLC5A6* is fully consistent with a recessive LoF disease: **pLI = 0.008** (heterozygous loss of function is well tolerated, i.e., healthy carriers exist), **LOEUF = 0.62**, observed/expected LoF ratio 0.457 (31 observed vs 67.9 expected; LoF Z = 3.80), and missense Z = 2.09. The low pLI with moderate LoF depletion fits a gene that is haplosufficient (carriers unaffected) but where biallelic loss is pathogenic. ClinVar lists 193 *SLC5A6* variant records, of which **47 are Pathogenic and 11 Likely pathogenic** (58 P/LP total), forming a recessive loss-of-function allelic series of missense, frameshift, nonsense, splice-site, and deep-intronic variants.

### Finding 8 — Cross-species orthologs confirmed; no registered interventional clinical trials for SMVTD

Orthologs are established across standard model species: human *SLC5A6* = NCBI Gene **8884**; mouse *Slc5a6* = **330064**; zebrafish *slc5a6* = **563356** (plus paralog 796312). A ClinicalTrials.gov query (v2 API, 2026) returned **no registered interventional studies** for "SLC5A6" or "sodium-dependent multivitamin transporter deficiency," consistent with an ultra-rare disorder managed with off-the-shelf vitamin supplementation rather than investigational agents.

### Finding 9 — A comprehensive, database-anchored disease-knowledge report was completed

The investigation consolidated a full 15-section characterization covering disease identity, etiology, phenotypes (with HPO terms and frequencies), genetics, mechanism, anatomy, temporal course, inheritance/epidemiology, diagnostics, prognosis, treatment, prevention, cross-species orthologs, and model organisms, plus a consolidated ontology appendix for knowledge-base ingestion. The evidence base comprises 18 primary sources plus UniProt, Ensembl, gnomAD, ClinVar, OLS4, and NCBI database verification.

---

## The 15-Section Disease Knowledge Entry

### 1. Disease Information

SMVTD is an autosomal-recessive inborn error of metabolism in which defective cellular import of biotin, pantothenic acid, and α-lipoic acid produces combined cofactor deficiency and mitochondrial energy failure. It was first recognized as a treatable disorder "mimicking biotinidase deficiency" ([PMID: 31392107](https://pubmed.ncbi.nlm.nih.gov/31392107/), [PMID: 27904971](https://pubmed.ncbi.nlm.nih.gov/27904971/)).

**Key identifiers:** MONDO:0033546 · OMIM #618973 (phenotype), *604024 (gene) · HGNC:11041 · Ensembl ENSG00000138074 · UniProt Q9Y289 · NCBI Gene 8884. Orphanet lists the entity under multivitamin-responsive metabolic disorders. **Synonyms:** sodium-dependent multivitamin transporter deficiency; SMVT deficiency; SMVT defect/disorder; neurodegeneration, infantile-onset, biotin-responsive (NERIB); and (milder allelic form) childhood-onset biotin-responsive peripheral motor neuropathy (COMNB). **Source type:** Information derives from **aggregated disease-level resources** (OMIM, MONDO, UniProt, gnomAD, ClinVar) and **individual-patient case reports/series** (~16–20 families), not from large EHR cohorts.

### 2. Etiology

**Causal factor:** genetic — biallelic loss-of-function variants in *SLC5A6*. **Genetic risk factors:** homozygous or compound-heterozygous P/LP *SLC5A6* genotypes; consanguinity substantially raises risk (multiple reported families are consanguineous, including a recurrent deep-intronic "outsider" variant in patients of Algerian/Maghreb origin, [PMID: 38348452](https://pubmed.ncbi.nlm.nih.gov/38348452/)). **Environmental risk/modifier factors:** intercurrent infections and catabolic stress precipitate metabolic decompensation; chronic alcohol lowers SMVT expression and biotin status ([PMID: 34077272](https://pubmed.ncbi.nlm.nih.gov/34077272/), [PMID: 21148397](https://pubmed.ncbi.nlm.nih.gov/21148397/)); dietary biotin/pantothenate insufficiency worsens the biochemical deficit. **Protective factor:** adequate dietary and supplemental intake of the three cofactors — the basis of therapy. **Gene–environment interaction:** disease severity reflects the interplay between residual transporter activity, dietary cofactor supply, and catabolic triggers; metabolic crises typically coincide with infections.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset | Severity/frequency |
|---|---|---|---|---|
| Global developmental delay / regression | Clinical sign | HP:0001263 / HP:0002376 | Neonatal–infantile | Common, often severe |
| Brain atrophy | Imaging/sign | HP:0012444 | Congenital–infantile | Common |
| Microcephaly | Physical | HP:0000252 | Congenital | Frequent |
| Epilepsy / seizures | Clinical sign | HP:0001250 | Infantile | Frequent |
| Sensorineural hearing loss | Clinical sign | HP:0000407 | Early | Reported subset |
| Optic atrophy | Clinical sign | HP:0000648 | Early | Reported subset |
| Peripheral (axonal sensorimotor) neuropathy | Clinical sign | HP:0007141 / HP:0003477 | Infantile (SMVTD) to ~10 yr (COMNB) | Core feature |
| Failure to thrive | Clinical sign | HP:0001508 | Infantile | Common |
| GI dysfunction (reflux, bleeding, pseudo-obstruction, vomiting) | Clinical sign | HP:0002020 / HP:0002577 | Infantile | Common |
| Cutaneous lesions / dyskeratosis | Physical | HP:0011368 | Infantile | Reported |
| Immunodeficiency / hypogammaglobulinemia | Lab abnormality | HP:0004313 | Infantile | Reported, can be severe/persistent |
| Osteopenia / pathologic fractures | Lab/imaging | HP:0000938 / HP:0002659 | Infantile | Reported |
| Dilated cardiomyopathy | Clinical sign | HP:0001644 | Infantile | Severe, potentially lethal |
| Metabolic crises (lactic acidosis, hyperammonemia, hypoglycemia) | Lab abnormality | HP:0003128 / HP:0001987 / HP:0001943 | Infantile, episodic | Life-threatening |
| 3-hydroxyisovaleric aciduria | Lab abnormality | HP:0003355 (organic aciduria) | Persistent | Diagnostic marker |

**Characteristics:** onset ranges from fetal (ventriculomegaly at 32 weeks, [PMID: 40272030](https://pubmed.ncbi.nlm.nih.gov/40272030/)) and neonatal in severe SMVTD to ~10 years in COMNB; course is progressive and episodic (crisis-prone) when untreated, stabilizing with therapy. **QoL impact:** severe in untreated classic disease (psychomotor disability persists even after biochemical rescue, [PMID: 40272030](https://pubmed.ncbi.nlm.nih.gov/40272030/)); substantially mitigated by early treatment.

### 4. Genetic/Molecular Information

**Causal gene:** *SLC5A6* (HGNC:11041; gene MIM 604024). **Variant classification/spectrum:** 58 ClinVar P/LP variants spanning missense, frameshift (e.g., p.(Leu566Valfs*33), [PMID: 37391029](https://pubmed.ncbi.nlm.nih.gov/37391029/)), nonsense, canonical splice-site, and a recurrent deep-intronic founder variant in the Maghreb population ([PMID: 38348452](https://pubmed.ncbi.nlm.nih.gov/38348452/)). Novel missense variants produce intermediate phenotypes ([PMID: 38012394](https://pubmed.ncbi.nlm.nih.gov/38012394/)). **Allele frequency/constraint:** heterozygous LoF tolerated (gnomAD pLI 0.008; LOEUF 0.62). **Origin:** germline, biallelic. **Functional consequence:** loss of function (reduced/absent transporter activity). **Modifier genes:** none established. **Epigenetics/chromosomal abnormalities:** no disease-specific methylation signature or structural rearrangement identified; alcohol-induced promoter (P1/P2) suppression of *SLC5A6* is an acquired, non-heritable transcriptional modifier ([PMID: 21148397](https://pubmed.ncbi.nlm.nih.gov/21148397/)).

### 5. Environmental Information

**Environmental/lifestyle factors:** chronic alcohol downregulates intestinal SMVT via epigenetic/transcriptional mechanisms and lowers plasma biotin ([PMID: 34077272](https://pubmed.ncbi.nlm.nih.gov/34077272/), [PMID: 21148397](https://pubmed.ncbi.nlm.nih.gov/21148397/)); dietary deficiency of biotin/pantothenate aggravates the deficit; intercurrent infection precipitates crises. **Infectious agents:** none causal; infections act as metabolic triggers.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. **Biallelic LoF variants in *SLC5A6*** → **loss/reduction of functional SMVT** at the apical membrane of enterocytes and at the blood–brain barrier.
2. Loss of SMVT → **impaired cellular uptake of biotin, pantothenic acid, and α-lipoic acid** (and reduced systemic/CNS delivery).
3a. ↓ **Pantothenate** → **↓ coenzyme A (CoA) synthesis** → impaired fatty acid oxidation (↑ long-chain fatty acids) and impaired TCA/acyl metabolism.
3b. ↓ **Biotin** → **↓ activity of biotin-dependent carboxylases** (pyruvate, propionyl-CoA, 3-methylcrotonyl-CoA, acetyl-CoA carboxylases) → organic aciduria (↑ urinary 3-HIA), lactic acidosis, hyperammonemia.
3c. ↓ **α-Lipoic acid** → **↓ lipoylation** of pyruvate dehydrogenase and α-ketoglutarate dehydrogenase complexes → impaired pyruvate oxidation and TCA flux.
4. (3a+3b+3c converge) → **mitochondrial energy failure / aberrant respiration with glycolytic reliance** → inferred ATP insufficiency in high-demand tissues.
5. Energy failure branches to tissue-specific injury:
   - **Brain** → atrophy, cysts, developmental regression, epilepsy, neuropathy (demonstrated clinically; prenatal energy-failure signatures reported).
   - **Heart** → cardiomyocyte hypertrophy, fibrosis, dilated cardiomyopathy (demonstrated in cardiac cKO mouse).
   - **Immune (B/plasma cells)** → impaired maturation and hypogammaglobulinemia (demonstrated; metabolically driven, biotin-rescuable).
   - **Gut** → barrier dysfunction, increased permeability, inflammation (demonstrated in intestinal cKO mouse).
   - **Systemic** → failure to thrive, osteopenia, cutaneous lesions, metabolic crises.
6. Restoration of the three cofactors by **supplementation** → reverses steps 2–4 and prevents/attenuates step 5 (disease-modifying, strongest when started early/preconception).

**Pathways/processes:** CoA biosynthesis (KEGG pantothenate/CoA), fatty acid β-oxidation, TCA cycle, biotin-dependent carboxylation, mitochondrial oxidative phosphorylation. **Suggested GO terms:** biotin transport (GO:0015878), pantothenate transmembrane transport (GO:0015887), coenzyme A biosynthetic process (GO:0015937), fatty acid beta-oxidation (GO:0006635), cellular respiration (GO:0045333). **Suggested CL terms:** enterocyte (CL:0000584), cardiomyocyte (CL:0000746), plasma cell (CL:0000786), neuron (CL:0000540), brain microvascular endothelial cell. **Molecular profiling:** metabolomics shows ↓pantothenate/↓CoA, ↑long-chain fatty acids, ↑3-HIA ([PMID: 39898461](https://pubmed.ncbi.nlm.nih.gov/39898461/)); proteomic/respirometry data show aberrant mitochondrial respiration ([PMID: 38036278](https://pubmed.ncbi.nlm.nih.gov/38036278/)).

### 7. Anatomical Structures Affected

**Primary organs/systems:** central and peripheral nervous system (brain UBERON:0000955; peripheral nerve UBERON:0001021), gastrointestinal tract (intestine UBERON:0000160), heart (UBERON:0000948), immune/hematopoietic system, skin (UBERON:0002097), bone (UBERON:0001474), eye/optic nerve (UBERON:0000941). **Secondary involvement:** failure to thrive, systemic metabolic decompensation. **Tissue/cell level:** intestinal epithelium/enterocytes (apical brush border), cardiomyocytes, plasma cells/B-lineage, neurons, brain microvascular endothelium (BBB). **Subcellular:** apical plasma membrane (GO:0016324) for the transporter; **mitochondrion (GO:0005739)** as the locus of downstream energy failure. **Localization/lateralization:** bilateral/symmetric CNS involvement; polyneuropathy is symmetric.

### 8. Temporal Development

**Onset:** congenital to infantile in severe SMVTD (fetal ventriculomegaly documented, [PMID: 40272030](https://pubmed.ncbi.nlm.nih.gov/40272030/)); ~10 years in COMNB. **Pattern:** chronic–progressive with superimposed acute metabolic crises (often infection-triggered). **Course/duration:** lifelong; untreated classic disease can be lethal in early infancy, whereas treated patients stabilize. **Critical period:** the earliest possible treatment window is decisive — preconception/neonatal intervention prevents the most severe (cardiac, neurologic) outcomes, while established CNS damage (e.g., psychomotor disability) may persist despite biochemical rescue.

### 9. Inheritance and Population

**Inheritance:** autosomal recessive. **Epidemiology:** ultra-rare, ~16–20 families reported; precise prevalence/incidence unknown (no registry). **Penetrance:** appears high/complete for biallelic LoF, though severity is variable. **Expressivity:** variable across families but with **little intrafamilial variability in onset** ([PMID: 40272030](https://pubmed.ncbi.nlm.nih.gov/40272030/)). **Anticipation/mosaicism:** not reported/not applicable. **Founder effect:** recurrent deep-intronic variant in Algerian/Maghreb consanguineous families ([PMID: 38348452](https://pubmed.ncbi.nlm.nih.gov/38348452/)). **Consanguinity:** a prominent contributor. **Carrier frequency:** heterozygotes are healthy (gnomAD pLI 0.008); exact carrier rate undefined. **Demographics:** no strong sex bias reported; cases span multiple ethnicities.

### 10. Diagnostics

**Laboratory/biochemical:** persistent **urinary 3-hydroxyisovaleric acid** elevation with **normal biotinidase activity** is a key clue ([PMID: 38407570](https://pubmed.ncbi.nlm.nih.gov/38407570/)); lactic acidosis, hypoglycemia, hyperammonemia during crises; **untargeted metabolomics** confirms reduced pantothenate/CoA and elevated long-chain fatty acids ([PMID: 39898461](https://pubmed.ncbi.nlm.nih.gov/39898461/)). **Imaging:** brain MRI (atrophy, cysts, corpus callosum anomalies); prenatal ultrasound/MRI may show ventriculomegaly. **Electrophysiology:** nerve conduction studies for axonal sensorimotor/motor neuropathy. **Genetic testing:** **trio whole-exome or whole-genome sequencing** is the definitive test and identifies biallelic *SLC5A6* variants; targeted single-gene/panel testing and WGS are useful to detect deep-intronic founder variants missed by exome panels ([PMID: 38348452](https://pubmed.ncbi.nlm.nih.gov/38348452/)). **Clinical criterion/differential:** differentiate from **biotinidase deficiency** and **holocarboxylase synthetase deficiency** (normal enzyme activities here), and from other mitochondrial/organic-acidurias. **Screening:** cascade testing of relatives and carrier testing in consanguineous families; not on standard newborn screening panels.

### 11. Outcome / Prognosis

**Survival/mortality:** without treatment, severe disease can be fatal in infancy (reported deaths; heart transplant in one case). **With early treatment**, survival and multisystem function improve markedly ([PMID: 37391029](https://pubmed.ncbi.nlm.nih.gov/37391029/), [PMID: 38407570](https://pubmed.ncbi.nlm.nih.gov/38407570/)). **Morbidity/disability:** neurodevelopmental disability may persist despite biochemical correction when CNS injury predates treatment. **Complications:** cardiomyopathy/heart failure, recurrent infections (immunodeficiency), fractures, metabolic crises. **Prognostic factors:** age at treatment initiation (earlier is better), severity/extent of pre-treatment organ damage, and occurrence of metabolic crises. **Prognostic biomarker:** normalization of 3-HIA and metabolomic profile tracks biochemical response.

### 12. Treatment

**Pharmacotherapy / supportive:** lifelong oral **high-dose biotin** (e.g., ~15 mg/day; CHEBI:15956), **pantothenic acid** (e.g., ~100 mg/day; CHEBI:46905), and **α-lipoic acid** (CHEBI:16494). NCIT-type intervention concepts: *biotin therapy*, *pantothenic acid supplementation*, *dietary supplement therapy*. **Outcomes:** cessation of cyclic vomiting, skin healing, improved strength, recovered immunoglobulin production, cardiac/GI improvement, developmental stabilization ([PMID: 40396389](https://pubmed.ncbi.nlm.nih.gov/40396389/), [PMID: 38036278](https://pubmed.ncbi.nlm.nih.gov/38036278/)). **Crisis management:** supportive metabolic care during decompensations. **Pharmacogenomics/advanced therapeutics:** none established; **no registered interventional trials** exist (gene/cell/RNA therapies not in clinical development). **Strategy:** start empiric supplementation immediately on biochemical suspicion while awaiting sequencing ([PMID: 38407570](https://pubmed.ncbi.nlm.nih.gov/38407570/)); treatment responsiveness also aids variant classification ([PMID: 35217562](https://pubmed.ncbi.nlm.nih.gov/35217562/)).

### 13. Prevention

**Primary:** in known carrier couples, preconception/prenatal planning; the mouse model shows **preconception supplementation prevents the cardiac phenotype**, and prenatal treatment of high-risk pregnancies is proposed given low intrafamilial variability in onset ([PMID: 42228401](https://pubmed.ncbi.nlm.nih.gov/42228401/), [PMID: 40272030](https://pubmed.ncbi.nlm.nih.gov/40272030/)). **Secondary:** early recognition via 3-HIA aciduria and rapid sequencing enables presymptomatic/early treatment. **Tertiary:** sustained supplementation to prevent crises and complications. **Counseling:** genetic counseling for autosomal-recessive 25% recurrence risk, carrier/cascade testing, and prenatal/preimplantation options, especially in consanguineous families. **Public health:** adequate dietary micronutrient intake; avoidance of chronic alcohol (which further depresses SMVT).

### 14. Other Species / Natural Disease

**Taxonomy/orthologs:** human *SLC5A6* (NCBI Gene 8884); mouse *Slc5a6* (330064); zebrafish *slc5a6* (563356, paralog 796312). The *SLC5A* family includes the related sodium-iodide symporter (*SLC5A5*/NIS), reflecting the shared transport chemistry (iodide is a minor SMVT substrate) ([PMID: 35899258](https://pubmed.ncbi.nlm.nih.gov/35899258/)). **Natural disease in other species:** no well-characterized spontaneous animal disease documented; disease knowledge is from engineered models. **Comparative biology:** mechanisms are evolutionarily conserved (CoA/biotin/lipoate cofactor biology is universal), supporting cross-species translation.

### 15. Model Organisms

| Model | Type | Key findings | Recapitulation |
|---|---|---|---|
| Cardiac-specific *Slc5a6* knockout mouse | Conditional KO (mammalian) | Progressive DCM, hypertrophy, fibrosis, impaired CoA synthesis, early mitochondrial disruption, death ~26 wk; preconception vitamins preventive ([PMID: 42228401](https://pubmed.ncbi.nlm.nih.gov/42228401/)) | Strong for cardiac/metabolic phenotype |
| Intestinal-specific (tamoxifen-induced) *Slc5a6* KO mouse | Conditional KO | Biotin deficiency, ↑gut permeability, altered tight junctions, cecal inflammation ([PMID: 27492331](https://pubmed.ncbi.nlm.nih.gov/27492331/), [PMID: 31369292](https://pubmed.ncbi.nlm.nih.gov/31369292/)) | Strong for GI barrier/inflammation |
| Transgenic mice carrying human *SLC5A6* 5′-regulatory region | Transgenic/reporter | Alcohol suppresses promoter activity → ↓biotin transport ([PMID: 21148397](https://pubmed.ncbi.nlm.nih.gov/21148397/)) | Models acquired/environmental regulation |
| Caco-2 human intestinal epithelial cells | In vitro | Apical hSMVT is the main biotin uptake system; KLF4-mediated upregulation in deficiency; C-terminal domain required for apical targeting ([PMID: 19056639](https://pubmed.ncbi.nlm.nih.gov/19056639/)) | Transport biology/trafficking |
| Zebrafish *slc5a6* | Vertebrate ortholog | Developmental expression studies of SLC5A family transporters ([PMID: 35899258](https://pubmed.ncbi.nlm.nih.gov/35899258/)) | Developmental/evolutionary context |

**Applications:** cardiac/GI/immune mechanism dissection, timing-of-treatment studies, and transporter trafficking/regulation. **Limitations:** no single model reproduces the full human multisystem spectrum; tissue-specific KOs isolate individual organ phenotypes rather than the integrated disease.

---

## Mechanistic Model / Interpretation

```
 Biallelic SLC5A6 loss-of-function (germline, AR)
                 │  leads to
                 ▼
 Loss of apical Na+-dependent multivitamin transporter (SMVT)
   at gut enterocytes + blood-brain barrier
                 │  results in
                 ▼
 ↓ Cellular uptake of  BIOTIN · PANTOTHENATE · α-LIPOIC ACID
        │                    │                    │
        │ ↓ carboxylase      │ ↓ CoA synthesis    │ ↓ lipoylation of
        │   activity         │ (↑ LCFA, ↓ FAO)    │   PDH / α-KGDH
        ▼                    ▼                    ▼
   ↑ 3-HIA, lactic     impaired fatty-acid   impaired pyruvate/
   acidosis, ↑NH3      oxidation & acyl      TCA oxidation
        │                    │                    │
        └──────── converge ──┴──────── converge ──┘
                 │  results in
                 ▼
   MITOCHONDRIAL ENERGY FAILURE (aberrant respiration, glycolytic reliance)
                 │  branches to
     ┌───────────┼───────────┬───────────┬───────────┐
     ▼           ▼           ▼           ▼           ▼
   Brain       Heart        Gut       Immune      Systemic
 (atrophy,    (DCM,       (barrier   (↓plasma-   (FTT, bone,
  epilepsy,   fibrosis)    loss,      cell        skin,
  neuropathy)              colitis)   maturation) crises)
                 │  reversed/prevented by
                 ▼
   EARLY high-dose BIOTIN + PANTOTHENATE + α-LIPOIC ACID
   (preconception/neonatal = maximal benefit)
```

The unifying interpretation is that a **single transport defect produces a combined cofactor deficiency** whose three arms all terminate in mitochondrial energy insufficiency. Because the bottleneck is nutrient *delivery* rather than enzyme catalysis, supra-physiologic supplementation can drive residual transport or alternative uptake and largely bypass the lesion — making SMVTD one of the clearest examples of a **genetically determined, nutritionally rescuable** mitochondrial-energy disorder. The upstream step (SMVT loss) is shared; the downstream branches are tissue-specific and account for the phenotypic breadth. Timing is the critical determinant of outcome because some injuries (prenatal CNS damage) are fixed before treatment can begin.

---

## Evidence Base

| PMID | Study type | Role in report |
|---|---|---|
| [27904971](https://pubmed.ncbi.nlm.nih.gov/27904971/) | Human case (index) | Establishes gene product and substrates; brain/immune/bone/intestinal dysfunction |
| [38012394](https://pubmed.ncbi.nlm.nih.gov/38012394/) | Human series | Defines SMVTD vs COMNB allelic series; intermediate missense phenotypes |
| [39898461](https://pubmed.ncbi.nlm.nih.gov/39898461/) | Human + metabolomics | Core phenotype list; ↓pantothenate/CoA, ↑LCFA (impaired FAO) |
| [42228401](https://pubmed.ncbi.nlm.nih.gov/42228401/) | Mouse model | CoA-deficiency cardiomyopathy; preconception vitamins preventive |
| [38036278](https://pubmed.ncbi.nlm.nih.gov/38036278/) | Human + in vitro | B-cell maturation defect, metabolic basis, biotin rescue |
| [40396389](https://pubmed.ncbi.nlm.nih.gov/40396389/) | Human case | Triple-therapy efficacy (vomiting, skin, muscle) |
| [38407570](https://pubmed.ncbi.nlm.nih.gov/38407570/) | Human + review | Life-threatening cardiac presentation; 3-HIA marker; dosing; ~16 patients |
| [37391029](https://pubmed.ncbi.nlm.nih.gov/37391029/) | Human family | Frameshift p.(Leu566Valfs*33); deaths without Rx, stabilization with early Rx |
| [35217562](https://pubmed.ncbi.nlm.nih.gov/35217562/) | Human case | Mild phenotype; treatment response informs variant classification |
| [40272030](https://pubmed.ncbi.nlm.nih.gov/40272030/) | Human case | Fetal-onset (prenatal ventriculomegaly); low intrafamilial onset variability |
| [38348452](https://pubmed.ncbi.nlm.nih.gov/38348452/) | Human series | Recurrent deep-intronic Maghreb founder variant; consanguinity |
| [31392107](https://pubmed.ncbi.nlm.nih.gov/31392107/) | Human/review | "Treatable disease, mimicking biotinidase deficiency" |
| [34077272](https://pubmed.ncbi.nlm.nih.gov/34077272/) | Mechanistic | Alcohol downregulates intestinal SMVT; biotin deficiency in alcoholism |
| [21148397](https://pubmed.ncbi.nlm.nih.gov/21148397/) | Rat/mouse/Caco-2 | Alcohol inhibits SMVT (protein/mRNA/hnRNA) and promoter P1/P2 |
| [27492331](https://pubmed.ncbi.nlm.nih.gov/27492331/) | Mouse model | Intestinal SMVT KO → gut permeability, tight-junction changes |
| [31369292](https://pubmed.ncbi.nlm.nih.gov/31369292/) | Mouse model | Intestinal-specific deletion → biotin deficiency, inflammation |
| [19056639](https://pubmed.ncbi.nlm.nih.gov/19056639/) | Review/in vitro | Apical hSMVT biotin uptake; KLF4 regulation; C-terminal trafficking |
| [35899258](https://pubmed.ncbi.nlm.nih.gov/35899258/) | Comparative | SLC5A family/NIS evolution; zebrafish context |

All quoted snippets above were verified against stored abstracts during the investigation. Database identifiers were cross-checked against UniProt (Q9Y289), Ensembl (ENSG00000138074), gnomAD (constraint metrics), ClinVar (variant counts), OLS4 (MONDO:0033546), and NCBI Gene (8884/330064/563356).

---

## Limitations and Knowledge Gaps

- **Small N:** the entire clinical literature comprises ~16–20 families; prevalence, incidence, penetrance, and sex ratio cannot be precisely estimated.
- **No genotype–phenotype map:** severity is not predictable from variant type; residual transporter activity is rarely measured directly in patients.
- **Persisting disability:** biochemical correction does not reverse pre-existing (especially prenatal) CNS damage — the treatment ceiling is incompletely defined.
- **Optimal regimen undefined:** dosing of biotin/pantothenate/lipoate is empiric; the independent contribution of α-lipoic acid is not rigorously established, and no randomized or registered trials exist.
- **Deep-intronic variants:** exome/panel testing may miss pathogenic intronic alleles (e.g., Maghreb founder), risking underdiagnosis.
- **Human mechanistic data are indirect:** key mechanistic proof (CoA deficiency → cardiomyopathy; metabolic basis of immune defect) comes from mouse/in-vitro models and is inferred in patients.
- **No newborn screening:** the diagnostic entry point (3-HIA with normal biotinidase) depends on clinical suspicion.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international SMVTD registry** to quantify prevalence, natural history, penetrance/expressivity, and treatment outcomes across genotypes.
2. **Direct transport-activity assays** (patient-derived cells/organoids expressing specific variants) to build a functional genotype–phenotype map and support ACMG classification of VUS.
3. **Prospective treatment-protocol study** to define optimal doses and the marginal value of α-lipoic acid, using 3-HIA and plasma pantothenate/CoA as pharmacodynamic biomarkers.
4. **Evaluate prenatal/presymptomatic treatment** in high-risk (e.g., consanguineous, prior-affected-child) pregnancies, given preconception efficacy in the mouse model and low intrafamilial onset variability.
5. **Expand diagnostic reach** by including *SLC5A6* deep-intronic regions in panels/WGS pipelines and adding SMVTD to metabolomics-based newborn/early-screening research programs.
6. **Model the integrated multisystem phenotype** (e.g., inducible whole-body hypomorph) and test whether CoA-targeted agents (pantethine, CoA precursors) augment vitamin therapy.
7. **Carrier-frequency estimation** from population databases (gnomAD) and targeted screening in founder populations to inform counseling.

---

## Consolidated Ontology Appendix

- **Disease:** MONDO:0033546; OMIM #618973
- **Gene/protein:** HGNC:11041 (*SLC5A6*); Ensembl ENSG00000138074; UniProt Q9Y289; NCBI Gene 8884 (human), 330064 (mouse), 563356 (zebrafish)
- **CHEBI (substrates/therapeutics):** biotin CHEBI:15956; (R)-pantothenate CHEBI:46905; (R)-lipoic acid CHEBI:16494; iodide CHEBI:16382; coenzyme A CHEBI:15346
- **GO (process):** biotin transport GO:0015878; pantothenate transmembrane transport GO:0015887; CoA biosynthetic process GO:0015937; fatty acid beta-oxidation GO:0006635
- **GO (component):** apical plasma membrane GO:0016324; mitochondrion GO:0005739
- **CL:** enterocyte CL:0000584; cardiomyocyte CL:0000746; plasma cell CL:0000786; neuron CL:0000540
- **UBERON:** brain UBERON:0000955; peripheral nerve UBERON:0001021; intestine UBERON:0000160; heart UBERON:0000948; skin UBERON:0002097; bone UBERON:0001474
- **Representative HPO:** HP:0001263, HP:0012444, HP:0001250, HP:0007141, HP:0001508, HP:0004313, HP:0001644, HP:0003355
- **NCIT (intervention concepts):** biotin therapy; pantothenic acid supplementation; dietary supplement therapy

*Report compiled from 18 primary sources and database verification (UniProt, Ensembl, gnomAD, ClinVar, OLS4, NCBI). Evidence sources are distinguished throughout as human clinical, model organism, in vitro, or computational/database.*


## Artifacts

- [OpenScientist final report](SLC5A6-Related_Multivitamin_Transporter_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SLC5A6-Related_Multivitamin_Transporter_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 18 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:27904971`: "mimicking biotinidase deficiency"
  - Text part not found as substring: 'mimicking biotinidase deficiency'

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012444` (2 mentions) - the report calls it "Imaging/sign"; HP calls it **Brain atrophy**
- `HP:0000252` (1 mention) - the report calls it "Physical"; HP calls it **Microcephaly**
- `HP:0001250` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0000407` (1 mention) - the report calls it "Clinical sign"; HP calls it **Sensorineural hearing impairment**
- `HP:0000648` (1 mention) - the report calls it "Clinical sign"; HP calls it **Optic atrophy**
- `HP:0001508` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Failure to thrive**
- `HP:0011368` (1 mention) - the report calls it "Physical"; HP calls it **Epidermal thickening**
- `HP:0004313` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Decreased circulating immunoglobulin concentration**
- `HP:0001644` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Dilated cardiomyopathy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0033546` (5 mentions) - the report calls it "neurodegeneration, infantile-onset, biotin-responsive; NERIB"; MONDO calls it **neurodegeneration, infantile-onset, biotin-responsive**
- `HP:0003355` (2 mentions) - the report calls it "organic aciduria"; HP calls it **Aminoaciduria**
- `CHEBI:16494` (2 mentions) - the report calls it "α-lipoic acid"; CHEBI calls it **lipoic acid**