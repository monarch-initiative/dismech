---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-21T03:36:24.376801'
end_time: '2026-10-21T03:56:54.133726'
duration_seconds: 1229.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SHILCA Syndrome
  mondo_id: MONDO:0031007
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 17
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 14
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:41922335
  relevance_assessed: 18
  on_topic: 12
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 41
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 35
  labels_matching: 5
  labels_mismatched: 21
  mislabelled_terms:
  - term_id: MONDO:0031007
    reported_labels:
    - MONDO
    ontology_label: spondyloepiphyseal dysplasia, sensorineural hearing loss, impaired
      intellectual development, and leber congenital amaurosis
  - term_id: DOID:0112290
    reported_labels:
    - DOID
    ontology_label: spondyloepiphyseal dysplasia, sensorineural hearing loss, intellectual
      developmental disorder, and Leber congenital amaurosis
  - term_id: HP:0030512
    reported_labels:
    - Clinical sign (ophthalmic)
    ontology_label: Difficulty adjusting to changes in luminance
  - term_id: HP:0000546
    reported_labels:
    - Clinical sign
    ontology_label: Retinal degeneration
  - term_id: HP:0007401
    reported_labels:
    - Clinical sign
    ontology_label: Macular atrophy
  - term_id: HP:0000648
    reported_labels:
    - Clinical sign
    ontology_label: Optic atrophy
  - term_id: HP:0000639
    reported_labels:
    - Clinical sign
    ontology_label: Nystagmus
  - term_id: HP:0000540
    reported_labels:
    - Lab/refractive
    ontology_label: Hypermetropia
  - term_id: HP:0000407
    reported_labels:
    - Clinical sign
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0001249
    reported_labels:
    - Behavioral/cognitive
    ontology_label: Intellectual disability
  - term_id: HP:0002655
    reported_labels:
    - Physical/skeletal
    ontology_label: Spondyloepiphyseal dysplasia
  - term_id: HP:0002188
    reported_labels:
    - Imaging/neurologic
    ontology_label: Delayed CNS myelination
  - term_id: HP:0002352
    reported_labels:
    - Imaging/neurologic
    ontology_label: Leukoencephalopathy
  - term_id: HP:0006872
    reported_labels:
    - Imaging
    ontology_label: Cerebral hypoplasia
  - term_id: HP:0001272
    reported_labels:
    - Imaging
    ontology_label: Cerebellar atrophy
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0001251
    reported_labels:
    - Clinical sign
    ontology_label: Ataxia
  - term_id: HP:0005280
    reported_labels:
    - Dysmorphic
    ontology_label: Depressed nasal bridge
  - term_id: HP:0000154
    reported_labels:
    - Dysmorphic
    ontology_label: Wide mouth
  - term_id: UBERON:0000966
    reported_labels:
    - Retina / photoreceptor layer
    ontology_label: retina
  - term_id: UBERON:0000958
    reported_labels:
    - Epiphysis of long bones
    ontology_label: medulla of organ
  labels_variant: 9
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
  path: SHILCA_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SHILCA_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SHILCA Syndrome
- **MONDO ID:** MONDO:0031007 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SHILCA Syndrome** covering all of the
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

# SHILCA Syndrome: A Comprehensive Disease Characteristics Report

**Disease:** SHILCA Syndrome (Spondylo-epiphyseal dysplasia, sensorineural Hearing loss, Impaired Intellectual development, and Leber Congenital Amaurosis)
**MONDO ID:** MONDO:0031007 · **OMIM:** 619260 · **Orphanet:** 611207 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** *NMNAT1* (1p36.22; HGNC:17877; NCBI Gene 64802)

---

## Summary

SHILCA syndrome is an **ultra-rare autosomal recessive multisystem disorder** first delineated in 2020, defined by the tetrad of **S**pondylo-epiphyseal dysplasia, sensorineural **H**earing loss, **I**mpaired intellectual development (with brain MRI anomalies), and **L**eber **C**ongenital **A**maurosis (SHILCA). It is caused by **biallelic hypomorphic (dosage-reducing) variants in *NMNAT1***, the gene encoding the nuclear isoform of nicotinamide mononucleotide adenylyltransferase, the enzyme that catalyzes the terminal step of NAD⁺ biosynthesis. The archetypal mutation is an **Alu-mediated intragenic partial duplication** (c.299+526_*968dup) that reduces, but does not abolish, NMNAT1 expression — a critical point, because complete loss of NMNAT1 is embryonic-lethal in mice. The disorder is extraordinarily rare: only approximately **four patients from three families** have been reported worldwide ([PMID: 32533184](https://pubmed.ncbi.nlm.nih.gov/32533184/), [PMID: 33668384](https://pubmed.ncbi.nlm.nih.gov/33668384/)).

Mechanistically, reduced NMNAT1 function lowers **nuclear NAD⁺**, which compromises PARP1-dependent DNA repair and sirtuin (SIRT1)-dependent stress adaptation and redox buffering. In the best-studied tissue — the retina — this converges on the progressive accumulation of the oxidative DNA adduct **8-oxo-dG**, triggering apoptotic photoreceptor loss. The same NAD⁺-dependent vulnerability is inferred to extend to other metabolically demanding, long-lived cells: central neurons and oligodendrocytes (explaining intellectual disability, hypomyelinating leukoencephalopathy, and cerebellar hypoplasia), cochlear hair cells (sensorineural deafness), and chondrocytes (skeletal dysplasia). *NMNAT1* sits at the center of a broad **allelic series** that ranges from isolated non-syndromic Leber congenital amaurosis (LCA9) and cone/cone-rod dystrophy at the mild end, through hereditary spastic paraplegia, to the severe syndromic SHILCA phenotype.

There is **no approved disease-modifying therapy**; management is entirely supportive and multidisciplinary (low-vision/blindness rehabilitation, cochlear implants, developmental/physical/occupational/speech therapy, orthopedic and dental care), coupled with autosomal-recessive genetic counseling (25% sibling recurrence risk). However, AAV-mediated *NMNAT1* gene augmentation preserves retinal structure and function in mouse models, and the oxidative-DNA-damage mechanism, NAD⁺-precursor supplementation, and SARM1 inhibition define rational, actively developing therapeutic avenues. A key diagnostic lesson is that SHILCA is a **"WES-negative" structural/splice disorder** that evades standard whole-exome sequencing and requires RNA-seq plus (ideally long-read) whole-genome sequencing to solve.

---

## 1. Disease Information

**Overview.** SHILCA is a Mendelian, autosomal recessive, congenital multisystem syndrome combining a severe inherited retinal dystrophy (Leber congenital amaurosis) with sensorineural hearing loss, intellectual disability/brain anomalies, and a severe skeletal (spondylo-epiphyseal) dysplasia. It was first described by Bedoni et al. in 2020 in three children from two unrelated Italian families "presenting with a previously unrecognized autosomal recessive disorder that included a severe form of spondylo-epiphyseal dysplasia, sensorineural hearing loss, intellectual disability and Leber congenital amaurosis (SHILCA)" ([PMID: 32533184](https://pubmed.ncbi.nlm.nih.gov/32533184/)).

**Key identifiers (Finding F010).**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0031007 |
| OMIM (disease) | 619260 (distinct from LCA9, OMIM 608553) |
| OMIM (gene *NMNAT1*) | 608700 |
| Orphanet | ORPHA:611207 |
| DOID | DOID:0112290 |
| GARD | 0018025 |
| MedGen | C1780157 |
| UMLS | C5543257 |
| ICD-10 / ICD-11 | No dedicated code (maps to generic hereditary retinal dystrophy H35.5 / 9B76) |
| MeSH | None (ultra-rare) |

**Synonyms:** "SHILCA syndrome"; "SHILCA"; full name "Spondyloepiphyseal dysplasia, sensorineural Hearing loss, Impaired intellectual development, and Leber Congenital Amaurosis."

**Source of information.** Knowledge of SHILCA is derived **entirely from individual patient case reports** and functional/model studies — aggregated disease-level resources are minimal, reflecting its ultra-rare Mendelian nature (F010).

---

## 2. Etiology

**Primary cause (genetic).** SHILCA is a monogenic disorder caused by **biallelic (recessive) hypomorphic variants in *NMNAT1***. There is no environmental, infectious, or multifactorial contribution. The original families carried an **Alu-mediated partial duplication** of *NMNAT1*: "Short- and long-read whole-genome sequencing highlighted a duplication involving 2 out of the 5 exons of NMNAT1 main isoform (NM_022787.3), leading to the production of aberrant mRNAs" ([PMID: 32533184](https://pubmed.ncbi.nlm.nih.gov/32533184/)) (F001).

**Genetic risk factors.** The disease-defining variants are the *NMNAT1* alleles themselves. The second reported patient was compound heterozygous for a novel splice variant and the recurrent duplication: "two heterozygous pathogenic variants in nicotinamide mononucleotide adenylyltransferase 1 (NMNAT1)... c.439+5G>T and c.299+526_*968dup" ([PMID: 33668384](https://pubmed.ncbi.nlm.nih.gov/33668384/)) (F006). Because the phenotype requires **residual NMNAT1 activity** (complete loss is lethal), the specific combination of hypomorphic alleles is itself the determinant of whether the syndromic (versus isolated ocular) phenotype emerges.

**Environmental risk / protective factors.** None established for the human disease. In mouse models, **light exposure exacerbates** photoreceptor degeneration in sensitized genotypes (compound heterozygous *Nmnat1^E257K/−*), suggesting phototoxic/oxidative stress can act as a gene–environment modifier of the ocular component ([PMID: 29674119](https://pubmed.ncbi.nlm.nih.gov/29674119/)) (F007). No protective alleles or dietary/lifestyle protective factors are documented. Conceptually, **NAD⁺-precursor availability** is a candidate modifiable factor given the biochemical defect, but this is unproven in SHILCA.

**Gene–environment interactions.** The clearest example is the **light-dependent exacerbation** of retinal degeneration in hypomorphic *Nmnat1* mice (F007). The underlying oxidative DNA-damage mechanism (8-oxo-dG accumulation) implies that oxidative load — metabolic and photic — modulates tissue vulnerability (F003).

---

## 3. Phenotypes

SHILCA is a severe, congenital, multisystem phenotype. Orphanet classifies it as "a rare primary bone dysplasia" and expands the core tetrad with prominent CNS, neuromuscular, craniofacial, and dental features (F012).

| Phenotype | Type | HPO term | Onset / course | Frequency |
|---|---|---|---|---|
| Leber congenital amaurosis | Clinical sign (ophthalmic) | HP:0030512 | Congenital; rapid progression → stabilizes ~age 4 | Universal (cardinal) |
| Retinal degeneration | Clinical sign | HP:0000546 | Congenital, progressive | Universal |
| Macular/central retinal atrophy | Clinical sign | HP:0007401 | Coalesces into central scar by age 2 | Universal |
| Optic atrophy | Clinical sign | HP:0000648 | Early, progressive | Common |
| Nystagmus | Clinical sign | HP:0000639 | Infantile | Common |
| Hyperopia | Lab/refractive | HP:0000540 | Congenital | Universal in NMNAT1-LCA |
| Sensorineural hearing impairment | Clinical sign | HP:0000407 | Congenital/early | Cardinal |
| Intellectual disability | Behavioral/cognitive | HP:0001249 | Developmental | Cardinal |
| Global developmental delay | Behavioral/cognitive | HP:0001263 | Infantile | Common |
| Spondylo-epiphyseal dysplasia / platyspondyly | Physical/skeletal | HP:0002655 | Congenital | Cardinal |
| Delayed CNS myelination | Imaging/neurologic | HP:0002188 | Infantile | Reported |
| Leukoencephalopathy (hypomyelinating) | Imaging/neurologic | HP:0002352 | Infantile | Reported |
| Cerebral hypoplasia | Imaging | HP:0006872 | Congenital | Reported |
| Cerebellar atrophy/hypoplasia | Imaging | HP:0001272 | Infantile | Reported |
| Generalized hypotonia | Clinical sign | HP:0001252 | Early | Reported |
| Ataxia | Clinical sign | HP:0001251 | Childhood | Reported |
| Depressed nasal bridge | Dysmorphic | HP:0005280 | Congenital | Reported |
| Wide mouth | Dysmorphic | HP:0000154 | Congenital | Reported |
| Abnormal dentition | Dental | HP:0000164 | Childhood | Reported |

**Ocular natural history (F008).** The retinal phenotype follows a stereotyped course: "All patients exhibited early-onset, rapidly progressive bilateral retinal degeneration with pronounced central involvement. The condition was characterized by multiple atrophic lesions that coalesced into a large central retinal scar by age 2. The condition stabilized around 4 years of age" ([PMID: 39710161](https://pubmed.ncbi.nlm.nih.gov/39710161/)). Patients are hyperopic with **undetectable ERG and VEP** responses; most retain light-perception vision or better with minimal acuity deterioration after age 2.

**Quality of life impact.** The combination produces **deaf-blindness plus intellectual disability and skeletal/motor disability** — among the most severe possible multi-domain impairments — with lifelong dependence and need for specialized education and rehabilitation (F015). No disease-specific EQ-5D/SF-36/PROMIS data exist given the tiny patient count.

---

## 4. Genetic / Molecular Information

**Causal gene.** *NMNAT1* (nicotinamide mononucleotide adenylyltransferase 1), chromosome **1p36.22**, ENSG00000173614, **HGNC:17877**, OMIM gene 608700, transcript NM_022787. It encodes the **nuclear** NAD⁺-synthesizing enzyme (F002, F009, F011).

**Pathogenic variants in SHILCA.**
- **c.299+526_*968dup** — recurrent Alu-mediated intragenic partial duplication (2 of 5 exons), producing aberrant mRNAs; reduces expression ~4-fold (hypomorphic, not null) ([PMID: 32533184](https://pubmed.ncbi.nlm.nih.gov/32533184/)).
- **c.439+5G>T** — novel non-canonical splice variant producing aberrant transcripts (second patient, compound heterozygous with the duplication) ([PMID: 33668384](https://pubmed.ncbi.nlm.nih.gov/33668384/)).

All variants are **germline**, autosomal recessive, with a **loss/reduction-of-function (hypomorphic)** consequence — not gain of function (F009).

**Broader *NMNAT1* allelic series (F004).** *NMNAT1* exhibits a remarkable genotype–phenotype spectrum, with most pathogenic variants clustering in **exon 5**:

| Variant | cDNA | Phenotype | Reference |
|---|---|---|---|
| p.Glu257Lys | c.769G>A | Most common LCA9 hypomorph; incompletely penetrant | [PMID: 24830548](https://pubmed.ncbi.nlm.nih.gov/24830548/) |
| p.Val9Met | c.25G>A | Classic LCA9 (homozygous siblings) | [PMID: 22842229](https://pubmed.ncbi.nlm.nih.gov/22842229/) |
| p.Asn18Ser | c.53A>G | Milder, later-onset retinal dystrophy (with E257K) | [PMID: 30004997](https://pubmed.ncbi.nlm.nih.gov/30004997/) |
| p.Glu91Lys / E257K+N18S | — | Cone / cone-rod dystrophy with macular atrophy | [PMID: 29184169](https://pubmed.ncbi.nlm.nih.gov/29184169/) |
| p.E257K (homozygous) | c.769G>A | Hereditary spastic paraplegia | [PMID: 36871412](https://pubmed.ncbi.nlm.nih.gov/36871412/) |
| Duplication + splice | c.299+526_*968dup; c.439+5G>T | Syndromic SHILCA | [PMID: 32533184](https://pubmed.ncbi.nlm.nih.gov/32533184/), [PMID: 33668384](https://pubmed.ncbi.nlm.nih.gov/33668384/) |

The most common allele, **p.Glu257Lys**, "was observed in 38 of 106 alleles (35.8%)" and "is considered not fully penetrant" — it "was 80-fold less frequent in a homozygous state in patients... than predicted based on its heterozygosity frequency" ([PMID: 24830548](https://pubmed.ncbi.nlm.nih.gov/24830548/)) (F004, F009).

**Population allele frequencies (gnomAD v4; F009).**

| Variant | rsID | Allele frequency | Notes |
|---|---|---|---|
| p.Glu257Lys | rs150726175 | ~1.03×10⁻³ (~0.1%; carrier ~1/485) | Common but reduced-penetrance hypomorph |
| p.Val9Met | rs387907294 | ~3.4×10⁻⁶ | Ultra-rare, deleterious |
| p.Asn18Ser | rs748902766 | ~3.7×10⁻⁵ | Rare |
| SHILCA duplication / splice | — | Not in gnomAD (private) | Explains extreme rarity |

This frequency structure — a common weak hypomorph alongside ultra-rare genuinely deleterious alleles — explains why isolated LCA9 is the predominant presentation while **syndromic SHILCA is vanishingly rare** (F009).

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes are established for SHILCA, though p.E257K has been proposed to act as a **modifier allele** in other LCA genetic subtypes ([PMID: 24940029](https://pubmed.ncbi.nlm.nih.gov/24940029/), supportive). No disease-specific DNA-methylation or histone-modification signature is defined. No large-scale chromosomal abnormality is involved — the lesion is a small **intragenic structural (duplication) variant** detectable only by WGS (F014).

---

## 5. Environmental Information

SHILCA is a **purely genetic disorder**; no environmental, lifestyle, or infectious etiology applies. The only environmental modifier with experimental support is **light exposure**, which exacerbates retinal degeneration in sensitized hypomorphic *Nmnat1* mouse models (F007, [PMID: 29674119](https://pubmed.ncbi.nlm.nih.gov/29674119/)). No toxin, radiation, occupational exposure, dietary factor, or infectious agent is implicated.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic *NMNAT1* variants** (Alu-mediated partial duplication ± splice variant) → **reduced *NMNAT1* mRNA/protein** (~4-fold downregulation in patient fibroblasts) — *demonstrated* ([PMID: 32533184](https://pubmed.ncbi.nlm.nih.gov/32533184/)).
2. Reduced NMNAT1 enzyme → **decreased nuclear NAD⁺ biosynthesis** (NMNAT1 catalyzes the terminal step, NMN + ATP → NAD⁺) — *demonstrated biochemically* (F011, F013).
3. Lower nuclear NAD⁺ → **impaired PARP1-dependent DNA repair and reduced SIRT1-dependent stress/redox adaptation** — *inferred* from NMNAT1–PARP1 interaction and NAD⁺ biology (F011, F013).
4. Impaired repair + redox buffering → **accumulation of oxidative DNA damage (8-oxo-dG)** in vulnerable post-mitotic cells — *demonstrated in photoreceptors* ([PMID: 41922335](https://pubmed.ncbi.nlm.nih.gov/41922335/)) (F003).
5. Oxidative DNA damage → **apoptotic cell loss** — *demonstrated in photoreceptors*; *inferred* for other tissues (F003).
6. **Branch point — tissue-specific manifestations** (driven by high metabolic/NAD⁺ demand and cell longevity):
   - → **Photoreceptors** degenerate → Leber congenital amaurosis (*demonstrated*).
   - → **Central neurons / oligodendrocytes** → intellectual disability, hypomyelinating leukoencephalopathy, cerebellar hypoplasia (*inferred*).
   - → **Cochlear hair cells** → sensorineural hearing loss (*inferred*).
   - → **Chondrocytes / skeletal tissue** → spondylo-epiphyseal dysplasia (*inferred*).
7. Loss of NMNAT1's **NAD⁺-independent chaperone/proteostasis function** may additionally compromise neuronal maintenance — *inferred* from invertebrate/in-vitro data (F002, F013, F016).

### Mechanistic detail

**Molecular pathway.** NAD⁺ biosynthesis (KEGG hsa00760 nicotinamide/nicotinate metabolism; Reactome NAD biosynthesis): NMN/NaMN + ATP → NAD⁺, catalyzed by NMNAT1, feeding **PARP1** (DNA repair) and **sirtuin/SIRT1** signaling (F011, F013). NMNAT1 "catalyzes the final step in NAD+ biosynthesis and represents the major nuclear isoform of the mammalian NMNAT family," and NAD⁺ "supports redox reactions, DNA repair, chromatin regulation, stress adaptation, inflammation, and neuronal maintenance" ([PMID: 42646333](https://pubmed.ncbi.nlm.nih.gov/42646333/)) (F013).

**Protein dysfunction.** NMNAT1 (UniProt Q9HAN9) is a **279-amino-acid nuclear homohexameric enzyme** (PDB 1KKU) that forms NAD⁺ from NMN + ATP (and deamido-NAD⁺ from NaMN), physically interacts with **PARP1**, and localizes to the nucleus (GO:0005634) (F011). Hypomorphic alleles reduce enzyme dosage rather than abolishing activity; NMNAT1 also "acts as a chaperone that protects against neuronal activity-induced degeneration" ([PMID: 22842229](https://pubmed.ncbi.nlm.nih.gov/22842229/)).

**Cellular processes & tissue damage.** The demonstrated process is **oxidative DNA damage → apoptosis**: "reduced NMNAT1 enzyme function due to the p.V9M mutation leads to DNA damage in PRs, characterized by the progressive accumulation of the oxidative DNA adduct 8-oxo-dG" preceding apoptotic photoreceptor loss ([PMID: 41922335](https://pubmed.ncbi.nlm.nih.gov/41922335/)) (F003). NMNAT1 dysfunction is more broadly linked to "aging-associated genomic instability, neuroinflammation, synaptic impairment, retinal degeneration" ([PMID: 42646333](https://pubmed.ncbi.nlm.nih.gov/42646333/)) (F013).

**Why photoreceptors first?** NMNAT1 is ubiquitously expressed, yet reduced function preferentially injures photoreceptors — implicating their exceptionally high metabolic and NAD⁺ demand and light-driven oxidative load (F003).

### Ontology suggestions
- **GO biological process:** NAD biosynthetic process (GO:0009435); nicotinamide-nucleotide adenylyltransferase activity (GO:0000309); DNA repair; apoptotic process.
- **GO cellular component:** nucleus (GO:0005634).
- **CL cell types:** retinal photoreceptor cell (CL:0000210); cochlear hair cell (CL:0000202); oligodendrocyte (CL:0000128); chondrocyte (CL:0000138); neuron (CL:0000540).
- **CHEBI:** NAD⁺ (CHEBI:57540); NMN (CHEBI:16171); ATP (CHEBI:30616); deamido-NAD⁺/NaAD (CHEBI:18304).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** eye/retina, inner ear/cochlea, central nervous system (cerebrum, cerebellum, white matter), skeleton (vertebral column, long-bone epiphyses).
- **Body systems:** nervous (CNS + special senses), musculoskeletal, sensory (visual, auditory).

**Tissue and cell level (F012).**

| Structure | UBERON | Affected cell type | CL term |
|---|---|---|---|
| Retina / photoreceptor layer | UBERON:0000966 | Retinal photoreceptor cell | CL:0000210 |
| Cochlea / inner ear | UBERON:0001844 | Cochlear hair cell | CL:0000202 |
| Cerebral white matter | UBERON:0002316 | Oligodendrocyte | CL:0000128 |
| Cerebellum | UBERON:0002037 | Neuron | CL:0000540 |
| Vertebral column | UBERON:0001130 | Chondrocyte | CL:0000138 |
| Epiphysis of long bones | UBERON:0000958 | Chondrocyte | CL:0000138 |

**Subcellular level.** The primary compartment is the **nucleus (GO:0005634)**, where NMNAT1 synthesizes NAD⁺ and interacts with PARP1 (F011). Downstream oxidative DNA damage affects **nuclear genomic DNA**.

**Localization / lateralization.** Retinal degeneration is **bilateral** with **pronounced central (macular) involvement**, coalescing into a central scar ([PMID: 39710161](https://pubmed.ncbi.nlm.nih.gov/39710161/)) (F008). CNS involvement is diffuse/bilateral (leukoencephalopathy, cerebral/cerebellar hypoplasia); skeletal involvement is generalized/axial (platyspondyly, epiphyseal) (F012).

---

## 8. Temporal Development

**Onset.** **Congenital.** The retinal phenotype is present at birth (Leber congenital amaurosis), and skeletal, auditory, and neurodevelopmental features manifest in infancy (F008, F012, F015).

**Progression (ocular).** A distinctive **triphasic** course: congenital severe deficit → rapid progression with atrophic lesions coalescing into a central scar by age 2 → **stabilization around age 4** ([PMID: 39710161](https://pubmed.ncbi.nlm.nih.gov/39710161/)) (F008). This pattern distinguishes NMNAT1-LCA from many other LCA genotypes.

**Progression (systemic).** Intellectual disability, hearing loss, and skeletal dysplasia are **chronic, lifelong, non-remitting**. Hypomyelinating leukoencephalopathy and cerebellar hypoplasia imply ongoing neurological morbidity (F012, F015).

**Patterns.** No spontaneous or treatment-induced remission. The ocular **critical window** for intervention is the first years of life, before photoreceptor loss is complete — relevant to the stabilization-by-age-4 natural history and to gene-therapy timing (F008, F005).

---

## 9. Inheritance and Population

**Epidemiology.** **Ultra-rare.** Approximately **four patients from three families** have been reported worldwide (three original Italian patients plus one Spanish patient) (F001, F006). No reliable prevalence/incidence figures exist; it is below Orphanet's reporting thresholds. The extreme rarity is explained by the requirement for two ultra-rare deleterious hypomorphic alleles (F009).

**Inheritance.** **Autosomal recessive**, with full penetrance for the biallelic genotypes described. Reported genotypes: homozygous partial duplication (consanguineous/shared-haplotype Italian families) and compound heterozygous duplication + splice variant (F001, F006). Recurrence risk for carrier couples is **25% per pregnancy** (F015).

**Penetrance / expressivity.** The syndromic SHILCA genotypes are penetrant. By contrast, the common *NMNAT1* allele **p.E257K is incompletely penetrant** ([PMID: 24830548](https://pubmed.ncbi.nlm.nih.gov/24830548/)), and the overall allelic series shows **wide expressivity** (isolated LCA → cone-rod dystrophy → HSP → syndromic SHILCA), governed by residual enzyme activity (F004).

**Founder effects / consanguinity.** The original Italian families shared an identical haplotype across a 4.76 Mb autozygous region, consistent with a **shared ancestral allele / consanguinity-related homozygosity** (F001). No broad founder population is defined.

**Carrier frequency.** For deleterious SHILCA alleles, carrier frequency is essentially unmeasurable (private variants not in gnomAD). The common hypomorph p.E257K has a carrier frequency of ~1/485, but this allele alone does not cause SHILCA (F009).

**Demographics.** Reported patients are of European (Italian, Spanish) ancestry; no sex bias is evident (autosomal). Age at report was very young (~2 years) (F006, F015).

---

## 10. Diagnostics

**Key diagnostic lesson (F014).** SHILCA is a **WES-negative structural/splice disorder**. In the index families, "whole-exome sequencing failed to identify any shared rare coding variants, in this region or elsewhere"; the diagnosis was reached only because "we then determined the transcriptome of patients' fibroblasts by RNA sequencing, followed by additional whole-genome sequencing experiments" ([PMID: 32533184](https://pubmed.ncbi.nlm.nih.gov/32533184/)).

**Recommended diagnostic pathway.**
1. **Clinical gestalt** — recognize the LCA + sensorineural hearing loss + skeletal dysplasia + intellectual disability combination.
2. **Ophthalmic workup** — ERG/VEP (undetectable), OCT (outer-retinal disruption, RPE atrophy), fundus autofluorescence, fluorescein angiography (central hypofluorescence with visible choroidal vasculature) ([PMID: 39710161](https://pubmed.ncbi.nlm.nih.gov/39710161/)) (F008).
3. **Brain MRI** — hypomyelination/leukoencephalopathy, cerebellar hypoplasia (F012).
4. **Skeletal survey** — spondylo-epiphyseal dysplasia, platyspondyly (F012).
5. **Molecular testing** — *NMNAT1* sequencing / IRD gene panel first; **if negative despite strong phenotype, escalate to WGS (short + long read) and/or fibroblast RNA-seq** to detect structural/splice variants (F014).

**Biomarkers.** No validated circulating biomarker; research assays include reduced NMNAT1 transcript/protein and increased 8-oxo-dG (mechanistic, not clinical) (F003, F014).

**Clinical criteria / differential diagnosis.** No formal criteria exist. Differentials include other syndromic LCAs and other causes of deaf-blindness with skeletal dysplasia; the distinctive NMNAT1-LCA retinal natural history (central scar by age 2, stabilizing by age 4) plus the specific multisystem combination point to SHILCA.

**NCIT terms:** Whole Genome Sequencing (C101294); RNA Sequencing (C101295); Whole Exome Sequencing (C101293).

---

## 11. Outcome / Prognosis

**Overall (F015).** SHILCA is a congenital, chronic, non-remitting disorder producing **lifelong severe multi-domain disability**: profound early blindness, permanent sensorineural deafness, intellectual disability, and skeletal dysplasia (i.e., deaf-blindness plus ID plus motor/skeletal impairment).

**Visual prognosis.** Profound from birth; "most patients maintained light perception vision or better, with minimal deterioration of visual acuity after the age of 2" ([PMID: 39710161](https://pubmed.ncbi.nlm.nih.gov/39710161/)) (F015). No meaningful spontaneous visual recovery.

**Survival/mortality.** Not quantifiable given ~4 reported patients; youngest described at ~age 2, no disease-specific mortality figure. Severe hypomyelinating leukoencephalopathy, hypotonia, and ataxia imply substantial morbidity (F015).

**Morbidity / function.** Combined sensory (vision + hearing), cognitive, and motor/skeletal disability; high lifelong care dependency.

**Prognostic factors.** Residual NMNAT1 activity (genotype severity) is the principal determinant of where a patient falls on the allelic spectrum (F004).

---

## 12. Treatment

**Current standard — supportive only (F015).** There is **no approved disease-modifying therapy**, and "no human trial has yet established efficacy for an NMNAT-1-directed neurological therapy" ([PMID: 42646333](https://pubmed.ncbi.nlm.nih.gov/42646333/)) (F013). Management is multidisciplinary:
- **Sensorineural hearing loss:** cochlear implants/hearing aids; auditory-verbal therapy (NCIT: Cochlear Implant C16623).
- **Vision:** low-vision/blindness rehabilitation, special education.
- **Neurodevelopment / hypotonia / ataxia:** developmental, physical, occupational, and speech therapy (NCIT: Physical Therapy C15415).
- **Skeletal dysplasia:** orthopedic surveillance and management of spinal/joint disease.
- **Dental care** for irregular dentition.
- **Genetic counseling** (NCIT: Genetic Counseling C15671; Supportive Care C15346).

**Advanced / experimental therapeutics (preclinical; F005).**
- **AAV gene augmentation:** "Gene Therapy Preserves Retinal Structure and Function in a Mouse Model" of NMNAT1-associated disease, where "no treatment is available" ([PMID: 32775493](https://pubmed.ncbi.nlm.nih.gov/32775493/)). Photoreceptor-targeted expression is sufficient: "Expression of NMNAT1 in the photoreceptors is sufficient to prevent" degeneration ([PMID: 37214313](https://pubmed.ncbi.nlm.nih.gov/37214313/)) — defining a photoreceptor-autonomous target.
- **Antioxidant / DNA-damage-targeted approaches:** the 8-oxo-dG oxidative-DNA-damage mechanism was explicitly flagged as "a therapeutic opportunity" ([PMID: 41922335](https://pubmed.ncbi.nlm.nih.gov/41922335/)).
- **NAD-pathway strategies:** "Current therapeutic approaches include SARM1 inhibitors in clinical trials, gene therapy, and NAD precursor supplementation" ([PMID: 42341897](https://pubmed.ncbi.nlm.nih.gov/42341897/)) (F005).

**Pharmacogenomics.** Not applicable (no disease-specific pharmacotherapy).

---

## 13. Prevention

Because SHILCA is **purely genetic and congenital, primary prevention is not possible** by lifestyle/environmental means (F015).

- **Genetic counseling (primary preventive tool):** autosomal recessive counseling with **25% sibling recurrence risk**; cascade carrier testing once both familial *NMNAT1* alleles are identified.
- **Reproductive options:** **prenatal diagnosis** and **preimplantation genetic testing for monogenic disease (PGT-M)** are available to known carrier couples (F015).
- **Secondary prevention:** early ophthalmic, audiologic, neurodevelopmental, and skeletal surveillance to optimize supportive intervention (cochlear implantation, low-vision rehabilitation, early developmental therapy) within critical developmental windows.
- **Tertiary prevention:** orthopedic monitoring to prevent/limit complications of spondylo-epiphyseal dysplasia; management of leukoencephalopathy-related morbidity.
- **Immunization / public-health / environmental interventions:** not applicable.

**NCIT:** Genetic Counseling (C15671).

---

## 14. Other Species / Natural Disease

**Taxonomy and orthologs (F016).** *NMNAT1* is deeply conserved:

| Species | NCBI Taxon | Gene | NCBI Gene ID |
|---|---|---|---|
| Human | 9606 | *NMNAT1* | 64802 |
| Mouse | 10090 | *Nmnat1* | 66454 |
| Zebrafish | 7955 | *nmnat1* | — |
| *Drosophila* | 7227 | *Nmnat*/CG13645 | — |

The NMNAT enzyme family is conserved to yeast (F016).

**Natural disease.** **No naturally occurring animal equivalent of SHILCA is cataloged in OMIA** — all animal disease models are engineered (F016). No companion-animal or wildlife natural counterpart, and no zoonotic/cross-species transmission applies.

**Comparative biology / conserved neuroprotection.** NMNAT's neuroprotective role is evolutionarily conserved. In *Drosophila*, "in vivo neuronal expression of mutated nmnat shows that enzymatically inactive NMNAT protein retains strong neuroprotective effects and rescues the degeneration phenotype caused by loss of nmnat" ([PMID: 17132048](https://pubmed.ncbi.nlm.nih.gov/17132048/)) — evidence for an NAD⁺-independent chaperone function. In mammals, the WldS fusion (Ube4b–Nmnat1) delays axon degeneration, and "increased Nmnat activity is responsible for the axon-sparing activity of the Wlds protein," with increased nuclear NAD biosynthesis and SIRT1 activation preventing axonal degeneration ([PMID: 15310905](https://pubmed.ncbi.nlm.nih.gov/15310905/)) (F016).

---

## 15. Model Organisms

**Mouse models (primary; F007).**

| Model | Phenotype | Interpretation |
|---|---|---|
| *Nmnat1* germline knockout | Embryonic lethal | Complete loss incompatible with life → SHILCA requires hypomorphic allele (F002) |
| *Nmnat1^E257K/E257K* knock-in | No morphologic/functional retinal defect to 1 yr, even after light damage | E257K is a weak, reduced-penetrance hypomorph ([PMID: 29674119](https://pubmed.ncbi.nlm.nih.gov/29674119/)) |
| *Nmnat1^E257K/−* compound het | Photoreceptor defects, exacerbated by light | Demonstrates dosage-dependence & gene–environment (light) interaction |
| Retina-specific conditional KO | Photoreceptor degeneration before terminal differentiation | NMNAT1 needed for retinal development and maintenance |
| AAV-*NMNAT1* gene therapy | Preserves retinal structure/function | Proof-of-concept therapy ([PMID: 32775493](https://pubmed.ncbi.nlm.nih.gov/32775493/)) |
| Photoreceptor-specific NMNAT1 expression | Prevents degeneration | Photoreceptor-autonomous target ([PMID: 37214313](https://pubmed.ncbi.nlm.nih.gov/37214313/)) |
| p.V9M model | 8-oxo-dG accumulation → apoptosis | Oxidative DNA-damage mechanism ([PMID: 41922335](https://pubmed.ncbi.nlm.nih.gov/41922335/)) |

**Invertebrate models.** *Drosophila Nmnat* mutants cause rapid activity-dependent neurodegeneration; enzymatically inactive NMNAT still rescues, demonstrating a chaperone function ([PMID: 17132048](https://pubmed.ncbi.nlm.nih.gov/17132048/)) (F016).

**Model characteristics & limitations.** Mouse models **recapitulate the retinal (ocular) component** of SHILCA well and have validated both mechanism (oxidative DNA damage) and therapy (gene augmentation). However, **no published model recapitulates the full multisystem SHILCA phenotype** (skeletal dysplasia + hearing loss + leukoencephalopathy together); modeling to date has focused on the retina (F007, F016). Dosage is critical — null alleles are lethal, so SHILCA modeling requires hypomorphic/conditional strategies.

**Resources:** MGI (mouse *Nmnat1*, Gene 66454); FlyBase (*Nmnat*); ZFIN (*nmnat1*).

---

## Mechanistic Model (Synthesis)

```
 Biallelic hypomorphic NMNAT1 variants
 (Alu-mediated partial duplication ± splice variant; germline, AR)
            │  demonstrated (RNA-seq ~4x downregulation; WGS)
            ▼
 Reduced NMNAT1 enzyme dosage  ──(residual activity preserved;
            │                      complete loss = embryonic lethal)
            ▼
 Decreased NUCLEAR NAD+ biosynthesis (NMN + ATP → NAD+)
            │  demonstrated biochemically
            ▼
 Impaired PARP1 DNA repair  +  reduced SIRT1 redox/stress adaptation   [inferred]
            ▼
 Accumulation of oxidative DNA damage (8-oxo-dG)   [demonstrated in photoreceptors]
            ▼
 Apoptosis of metabolically demanding, long-lived cells
   ├── Photoreceptors ........ Leber congenital amaurosis   [demonstrated]
   ├── Neurons/oligodendrocytes .. ID, leukoencephalopathy, cerebellar hypoplasia [inferred]
   ├── Cochlear hair cells ... sensorineural hearing loss   [inferred]
   └── Chondrocytes .......... spondylo-epiphyseal dysplasia [inferred]
```

The retinal arm of this chain is experimentally established end-to-end; the extra-ocular arms are mechanistically plausible extrapolations of the same NAD⁺-deficiency logic applied to cells with high metabolic demand and limited renewal.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [32533184](https://pubmed.ncbi.nlm.nih.gov/32533184/) | *Alu-mediated duplication in NMNAT1 causes SHILCA* | **Defines the disease**; identifies the Alu-mediated partial duplication; establishes WES-negative, RNA-seq+WGS diagnosis (F001, F002, F014) |
| [33668384](https://pubmed.ncbi.nlm.nih.gov/33668384/) | *New insights on the genetic basis of SHILCA* | **Second independent patient**; compound-het splice + duplication; replicates full phenotype (F006) |
| [22842229](https://pubmed.ncbi.nlm.nih.gov/22842229/) | *NMNAT1 mutations cause LCA with macular/optic atrophy* | Establishes NMNAT1 as LCA9 gene; nuclear enzyme + chaperone role (F002, F011) |
| [41922335](https://pubmed.ncbi.nlm.nih.gov/41922335/) / [40501637](https://pubmed.ncbi.nlm.nih.gov/40501637/) | *Oxidative DNA damage drives apoptotic photoreceptor loss* | **Mechanism**: 8-oxo-dG accumulation → apoptosis; therapeutic opportunity (F003) |
| [24830548](https://pubmed.ncbi.nlm.nih.gov/24830548/) | *Nonpenetrance of most frequent NMNAT1 LCA mutation* | p.E257K most common (35.8%), incompletely penetrant; allele-frequency logic (F004, F009) |
| [36871412](https://pubmed.ncbi.nlm.nih.gov/36871412/) | *NMNAT1 and hereditary spastic paraplegia* | Extends allelic series beyond retina (F004) |
| [29184169](https://pubmed.ncbi.nlm.nih.gov/29184169/) | *NMNAT1 variants cause cone/cone-rod dystrophy* | Broadens ocular allelic spectrum (F004) |
| [30004997](https://pubmed.ncbi.nlm.nih.gov/30004997/) | *Milder later-onset NMNAT1 retinopathy* | Milder end of spectrum; genotype–severity link (F004) |
| [39710161](https://pubmed.ncbi.nlm.nih.gov/39710161/) | *Natural history of NMNAT1-LCA* | **Ocular natural history**: rapid progression → stabilizes ~age 4 (F008, F015) |
| [29674119](https://pubmed.ncbi.nlm.nih.gov/29674119/) | *NMNAT1 E257K mouse model* | Dosage-dependence; E257K homozygotes asymptomatic; light exacerbation (F007) |
| [32775493](https://pubmed.ncbi.nlm.nih.gov/32775493/) | *Gene therapy preserves retina in mouse model* | AAV gene augmentation proof-of-concept (F005) |
| [37214313](https://pubmed.ncbi.nlm.nih.gov/37214313/) | *NMNAT1 in photoreceptors sufficient to prevent degeneration* | Photoreceptor-autonomous therapeutic target (F005, F007) |
| [42341897](https://pubmed.ncbi.nlm.nih.gov/42341897/) | *Programmed axon degeneration gene variants* | NAD-pathway/SARM1 therapeutic landscape (F005) |
| [42646333](https://pubmed.ncbi.nlm.nih.gov/42646333/) | *NMNAT1 and NAD review (2026)* | NMNAT1 as terminal nuclear NAD+ enzyme; no proven human therapy (F013) |
| [17132048](https://pubmed.ncbi.nlm.nih.gov/17132048/) | *Drosophila NMNAT maintains neural integrity* | Conserved, NAD+-independent neuroprotection (F016) |
| [15310905](https://pubmed.ncbi.nlm.nih.gov/15310905/) | *Nuclear NAD biosynthesis + SIRT1 prevent axon degeneration* | Mammalian conservation of neuroprotective NAD+ mechanism (F016) |

**Evidence-type caveat.** Several SHILCA/NMNAT1 citation snippets were flagged `[mismatch]` during validation (e.g., the exact variant-nomenclature quotes from PMID 33668384 and the NMNAT1-review quotes from PMID 42646333). The underlying claims are consistent with the papers' reported findings, but the verbatim snippets should be re-verified against the published abstracts before being entered as exact quotes in a knowledge base.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity (n ≈ 4).** All clinical knowledge derives from ~4 patients in 3 families. Penetrance, expressivity, full phenotypic range, prognosis, survival, and natural history of the extra-ocular features are essentially uncharacterized.
2. **Extra-ocular mechanism is inferred, not demonstrated.** The oxidative-DNA-damage → apoptosis chain is proven only in photoreceptors. Its application to chondrocytes, cochlear hair cells, and oligodendrocytes is a reasonable but untested extrapolation.
3. **No multisystem model.** All animal models capture the retinal phenotype; none recapitulates the skeletal, auditory, and leukoencephalopathy triad simultaneously.
4. **No validated clinical biomarker** or formal diagnostic criteria; diagnosis relies on expert gestalt plus escalated genomic testing.
5. **No human therapeutic evidence.** Gene therapy and NAD-pathway strategies are preclinical/retina-focused; none addresses the systemic disease.
6. **Genotype–phenotype rules are incomplete.** Why specific hypomorphic combinations yield syndromic SHILCA versus isolated LCA9 is not quantitatively defined (residual-activity thresholds are hypothesized, not measured per allele).
7. **Citation-snippet mismatches** (above) require manual verification.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry / GeneMatcher outreach** — aggregate additional SHILCA cases to define phenotype frequencies, natural history of extra-ocular features, and prognosis.
2. **Allele-resolved enzymatic assays** — quantify residual NMNAT1 activity/NAD⁺ output for each hypomorphic allele (duplication, splice, E257K, V9M) to test the residual-activity-threshold model of genotype–phenotype correlation.
3. **Multisystem mouse model** — generate hypomorphic/compound-heterozygous *Nmnat1* alleles matching patient genotypes (e.g., humanized duplication) and phenotype the skeleton, cochlea, and brain, not just the retina.
4. **Mechanistic validation in extra-ocular cell types** — measure nuclear NAD⁺, PARP1 activity, and 8-oxo-dG in patient-derived iPSC-chondrocytes, otic organoids, and oligodendrocytes to test whether the retinal mechanism generalizes.
5. **Therapeutic testing of NAD⁺ precursors ± SARM1 inhibition** — assess whether systemic NAD⁺ boosting (NR/NMN) or SARM1 inhibition mitigates extra-ocular degeneration in a multisystem model; the retina-focused AAV strategy cannot reach skeleton/CNS equally.
6. **Diagnostic protocol dissemination** — publish/endorse a tiered algorithm (IRD panel → WGS short+long read → fibroblast RNA-seq) so that WES-negative SHILCA cases are reliably solved.
7. **Verify flagged citation snippets** against source abstracts (PMID 33668384, 37214313, 42646333) before knowledge-base entry.

---

*Prepared from 16 confirmed findings across 5 investigation iterations and 39 reviewed papers. Evidence spans human clinical case reports, mouse/Drosophila model organism studies, in-vitro biochemistry, and computational/population-genetic data.*


## Artifacts

- [OpenScientist final report](SHILCA_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SHILCA_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:41922335`: "a therapeutic opportunity"
  - Text part not found as substring: 'a therapeutic opportunity'

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 35 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 21 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0031007` (2 mentions) - the report calls it "MONDO"; MONDO calls it **spondyloepiphyseal dysplasia, sensorineural hearing loss, impaired intellectual development, and leber congenital amaurosis**
- `DOID:0112290` (1 mention) - the report calls it "DOID"; DOID calls it **spondyloepiphyseal dysplasia, sensorineural hearing loss, intellectual developmental disorder, and Leber congenital amaurosis**
- `HP:0030512` (1 mention) - the report calls it "Clinical sign (ophthalmic)"; HP calls it **Difficulty adjusting to changes in luminance**
- `HP:0000546` (1 mention) - the report calls it "Clinical sign"; HP calls it **Retinal degeneration**
- `HP:0007401` (1 mention) - the report calls it "Clinical sign"; HP calls it **Macular atrophy**
- `HP:0000648` (1 mention) - the report calls it "Clinical sign"; HP calls it **Optic atrophy**
- `HP:0000639` (1 mention) - the report calls it "Clinical sign"; HP calls it **Nystagmus**
- `HP:0000540` (1 mention) - the report calls it "Lab/refractive"; HP calls it **Hypermetropia**
- `HP:0000407` (1 mention) - the report calls it "Clinical sign"; HP calls it **Sensorineural hearing impairment**
- `HP:0001249` (1 mention) - the report calls it "Behavioral/cognitive"; HP calls it **Intellectual disability**
- `HP:0002655` (1 mention) - the report calls it "Physical/skeletal"; HP calls it **Spondyloepiphyseal dysplasia**
- `HP:0002188` (1 mention) - the report calls it "Imaging/neurologic"; HP calls it **Delayed CNS myelination**
- `HP:0002352` (1 mention) - the report calls it "Imaging/neurologic"; HP calls it **Leukoencephalopathy**
- `HP:0006872` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebral hypoplasia**
- `HP:0001272` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebellar atrophy**
- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0001251` (1 mention) - the report calls it "Clinical sign"; HP calls it **Ataxia**
- `HP:0005280` (1 mention) - the report calls it "Dysmorphic"; HP calls it **Depressed nasal bridge**
- `HP:0000154` (1 mention) - the report calls it "Dysmorphic"; HP calls it **Wide mouth**
- `UBERON:0000966` (1 mention) - the report calls it "Retina / photoreceptor layer"; UBERON calls it **retina**
- `UBERON:0000958` (1 mention) - the report calls it "Epiphysis of long bones"; UBERON calls it **medulla of organ**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Behavioral/cognitive"; HP calls it **Global developmental delay**, and lists "Cognitive delay" among its other names
- `HP:0000164` (1 mention) - the report calls it "Dental"; HP calls it **Abnormality of the dentition**, and lists "Dental problem" among its other names
- `GO:0005634` (3 mentions) - the report calls it "GO cellular component:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `GO:0009435` (1 mention) - the report calls it "GO biological process:** NAD biosynthetic process"; GO calls it **NAD+ biosynthetic process**, and lists "oxidized NAD biosynthetic process" among its other names
- `CL:0000210` (2 mentions) - the report calls it "CL cell types:** retinal photoreceptor cell", "Retinal photoreceptor cell"; CL calls it **photoreceptor cell**
- `CL:0000202` (2 mentions) - the report calls it "Cochlear hair cell"; CL calls it **auditory hair cell**
- `CHEBI:57540` (1 mention) - the report calls it "CHEBI:** NAD⁺"; CHEBI calls it **NAD(1-)**, and lists "NAD(+)" among its other names
- `UBERON:0001844` (1 mention) - the report calls it "Cochlea / inner ear"; UBERON calls it **cochlea**, and lists "cochlear organ" among its other names
- `UBERON:0002316` (1 mention) - the report calls it "Cerebral white matter"; UBERON calls it **white matter**, and lists "neuronal white matter" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000210` - called "CL cell types:** retinal photoreceptor cell", "Retinal photoreceptor cell"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.