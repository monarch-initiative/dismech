---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T16:49:20.833126'
end_time: '2026-08-28T17:09:13.315981'
duration_seconds: 1192.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spondyloepimetaphyseal Dysplasia Guo-Campeau Type
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
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 6
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 14
  relevance_assessed: 6
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 0
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0958006
    reported_labels:
    - MONDO
    ontology_label: spondyloepimetaphyseal dysplasia, Guo-Campeau type
  - term_id: HP:0003510
    reported_labels:
    - Physical/growth
    ontology_label: Severe short stature
  - term_id: HP:0000926
    reported_labels:
    - Skeletal/radiographic
    ontology_label: Platyspondyly
  - term_id: HP:0003417
    reported_labels:
    - Radiographic
    ontology_label: Coronal cleft vertebrae
  - term_id: HP:0002650
    reported_labels:
    - Skeletal
    ontology_label: Scoliosis
  - term_id: HP:0030084
    reported_labels:
    - Digital
    ontology_label: Clinodactyly
  - term_id: HP:0012385
    reported_labels:
    - Digital
    ontology_label: Camptodactyly
  - term_id: HP:0001159
    reported_labels:
    - Digital
    ontology_label: Syndactyly
  - term_id: HP:0000268
    reported_labels:
    - Craniofacial
    ontology_label: Dolichocephaly
  - term_id: HP:0000243
    reported_labels:
    - Craniofacial
    ontology_label: Trigonocephaly
  - term_id: HP:0001256
    reported_labels:
    - Neurodevelopmental
    ontology_label: Mild intellectual disability
  - term_id: CL:0000138
    reported_labels:
    - growth-plate chondrocytes
    - Cell populations:** Chondrocytes, particularly **growth-plate chondrocytes
    ontology_label: chondrocyte
  labels_variant: 2
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
  path: Spondyloepimetaphyseal_Dysplasia_Guo-Campeau_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spondyloepimetaphyseal_Dysplasia_Guo-Campeau_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondyloepimetaphyseal Dysplasia Guo-Campeau Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondyloepimetaphyseal Dysplasia Guo-Campeau Type** covering all of the
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

# Spondyloepimetaphyseal Dysplasia, Guo-Campeau Type (SEMDGC): Comprehensive Disease Characteristics Report

## Summary

**Spondyloepimetaphyseal Dysplasia, Guo-Campeau type (SEMDGC; OMIM #620663; MONDO:0958006)** is an ultra-rare autosomal-recessive Mendelian skeletal dysplasia caused by **biallelic missense variants in the *ERI1* gene** (chromosome 8p23.1; OMIM *608739; HGNC:23994). *ERI1* encodes a highly conserved DEDDh-family 3′→5′ exoribonuclease that carries out two essential RNA-metabolic functions: 3′-end maturation of the 5.8S ribosomal RNA (ribosome biogenesis) and degradation of replication-dependent histone mRNAs (cell-cycle-coupled histone homeostasis). The disease was defined by Guo et al. in 2023 (*American Journal of Human Genetics*) in a landmark cohort of 8 affected individuals from 7 unrelated families and has since been reviewed comprehensively (2025).

The defining scientific feature of this disorder is a striking **genotype–phenotype dichotomy**: individuals carrying **at least one missense variant** develop the severe skeletal dysplasia (SEMDGC), whereas individuals with **biallelic null (nonsense) variants** present only with mild intellectual disability and digital anomalies — a distinct, milder allelic condition now designated **Hoxha-Aliu syndrome (HXAL; OMIM #620662)**. This inverse relationship — where the "milder" molecular lesion (missense) produces the more severe clinical phenotype — strongly implies a **dominant-negative or neomorphic (gain-of-toxic-function) mechanism** of the catalytically dead protein, rather than simple loss-of-function haploinsufficiency. Functionally, the pathogenic missense variants cluster in the C-terminal exonuclease (EXOIII/DEDDh) domain, abolish 3′→5′ exoribonuclease activity, and fail to rescue 5.8S rRNA processing defects in *ERI1*-knockout cells.

The clinical phenotype spans a broad severity spectrum, from survival into adulthood to infantile/early-childhood lethality (deaths at 4 months, 5 months, and 2 years documented in the founding cohort). Core features include severe short stature, platyspondyly with irregular vertebral endplates, scoliosis, epiphyseal/metaphyseal dysplasia, facial dysmorphism, and dysplastic-to-absent digits. Patient-derived iPSCs show impaired in vitro chondrogenesis with downregulation of skeletal-patterning genes, providing the cellular link between RNA-metabolic dysfunction and the skeletal phenotype. No curative therapy exists; management is supportive and orthopedic. *Eri1*-knockout mice only partially recapitulate the disease (growth restriction and brachydactyly, but not SEMD), and notably resemble the human null-allele (Hoxha-Aliu) phenotype rather than the missense-driven SEMDGC.

---

## Section 1: Disease Information

### Overview
SEMDGC is a congenital, autosomal-recessive skeletal dysplasia belonging to the spondyloepimetaphyseal dysplasia (SEMD) group — disorders affecting the **spine (spondylo-)**, the **epiphyses (epi-)**, and the **metaphyses (-metaphyseal)** of the long bones. It is caused by biallelic pathogenic variants in *ERI1*, a gene central to RNA metabolism. The disorder is characterized by severe growth failure, vertebral and long-bone abnormalities, and hand/foot malformations, often accompanied by facial dysmorphism and, in a subset, extraskeletal (renal, cardiac) anomalies and developmental delay.

### Key Identifiers
| Resource | Identifier |
|----------|-----------|
| **OMIM (disease)** | #620663 (SEMDGC) |
| **OMIM (gene)** | *608739 (*ERI1*) |
| **MONDO** | MONDO:0958006 |
| **UniProt disease** | DI-06817 |
| **Gene locus** | 8p23.1 |
| **HGNC** | HGNC:23994 |
| **NCBI Gene** | 90459 |
| **Ensembl** | ENSG00000104626 |
| **UniProt (protein)** | Q8IV48 |

### Synonyms / Alternative Names
- Spondyloepimetaphyseal dysplasia, Guo-Campeau type
- SEMDGC
- SEMD Guo-Campeau type
- ERI1-related spondyloepimetaphyseal dysplasia

### Information Source
Information is derived from **aggregated disease-level resources** (OMIM, MONDO, UniProt) and **individual-patient case reports** aggregated into the founding cohort study of 8 individuals from 7 families ([PMID: 37352860](https://pubmed.ncbi.nlm.nih.gov/37352860/)) plus a 2025 review ([PMID: 39945916](https://pubmed.ncbi.nlm.nih.gov/39945916/)). It is not derived from large-scale EHR datasets — appropriately, given the ultra-rare nature of the condition.

---

## Section 2: Etiology

### Disease Causal Factors
The disease is **entirely genetic (Mendelian, monogenic, autosomal recessive)**. There are no known environmental, infectious, or mechanical causes. The cause is **biallelic missense variants in *ERI1***, with a requirement that at least one allele be a missense variant to produce the severe SEMD phenotype.

### Genetic Risk Factors
- **Causal variants:** Biallelic *ERI1* variants; specifically, at least one **missense** variant in the C-terminal exonuclease domain is required for the severe SEMDGC phenotype.
- **Genotype–phenotype relationship (the central etiologic insight):** "*A severe spondyloepimetaphyseal dysplasia (SEMD) was identified in five affected individuals with missense variants but not in those with bi-allelic null variants, who showed mild intellectual disability and digital anomalies*" ([PMID: 37352860](https://pubmed.ncbi.nlm.nih.gov/37352860/)).
- **Susceptibility loci / modifier genes:** None established. Given the monogenic, highly penetrant nature, classical susceptibility loci are not applicable.

### Environmental / Lifestyle Risk Factors
None known or applicable. As a Mendelian congenital disorder, environmental exposures, lifestyle, occupational factors, age, and sex are not established contributors to disease occurrence. Consanguinity is relevant as it increases the likelihood of biallelic (homozygous) recessive variants (see Section 9).

### Protective Factors
No genetic or environmental protective factors are established. Theoretically, the null-allele end of the allelic series is "protective" against the severe skeletal phenotype in the sense that biallelic nulls do NOT produce SEMD — but this reflects the neomorphic biology of the missense protein rather than a conventional protective factor.

### Gene–Environment Interactions
None documented. The disorder is deterministic and genetic.

---

## Section 3: Phenotypes

The phenotype is congenital in onset and, in the severe (missense) form, ranges from moderate to lethal. The following table catalogs the reported phenotypes with suggested HPO terms.

| Phenotype | Type | HPO Term | Notes / Frequency |
|-----------|------|----------|-------------------|
| Severe short stature | Physical/growth | HP:0003510 | Core feature; congenital growth failure |
| Platyspondyly (flattened vertebrae) | Skeletal/radiographic | HP:0000926 | Core spondylo- feature |
| Irregular vertebral endplates | Radiographic | HP:0003417 | Characteristic |
| Scoliosis | Skeletal | HP:0002650 | Progressive |
| Epiphyseal dysplasia | Radiographic | — | Defines "epi-" component |
| Metaphyseal dysplasia | Radiographic | — | Defines "metaphyseal" component |
| Clinodactyly | Digital | HP:0030084 | Dysplastic digits |
| Camptodactyly | Digital | HP:0012385 | Dysplastic digits |
| Syndactyly | Digital | HP:0001159 | Including toe syndactyly |
| Short/rudimentary/absent digits | Digital | — | Severe end of spectrum |
| Dolichocephaly | Craniofacial | HP:0000268 | Facial dysmorphism |
| Trigonocephaly | Craniofacial | HP:0000243 | Facial dysmorphism |
| Facial dysmorphism | Craniofacial | — | Variable |
| Intellectual disability (mild) | Neurodevelopmental | HP:0001256 | More characteristic of null-allele (HXAL) form |
| Renal anomalies | Extraskeletal | — | Reported in ≥1 severe SEMDGC patient (family 4) |
| Cardiac anomalies | Extraskeletal | — | Reported in ≥1 severe SEMDGC patient (family 4) |
| Developmental delay | Neurodevelopmental | HP:0001263 | Reported in ≥1 severe SEMDGC patient (family 4) |

### Phenotype Characteristics
- **Age of onset:** Congenital / neonatal (skeletal dysplasia present from birth).
- **Severity:** Variable — from survival into adulthood to infantile lethality. Severity tracks with genotype (missense → severe; null → mild).
- **Progression:** Skeletal features (e.g., scoliosis) are progressive with age; overall the disorder is chronic and lifelong in survivors.
- **Frequency among affected:** In the founding cohort, severe SEMD occurred in 5 of 8 affected individuals (all carrying ≥1 missense variant); the remaining individuals (biallelic null) had only mild ID and digital anomalies.

### Quality of Life Impact
Severe short stature, skeletal deformity (scoliosis, joint/limb abnormalities), and digital malformations substantially impair mobility, dexterity, and daily functioning. In the lethal subset, infants die in early childhood. Disease-specific QoL instruments (EQ-5D, SF-36) have not been applied to this ultra-rare condition; QoL impact is inferred from phenotype severity.

---

## Section 4: Genetic / Molecular Information

### Causal Gene
- **Gene:** *ERI1* (Exoribonuclease 1); OMIM *608739; HGNC:23994; NCBI Gene 90459; Ensembl ENSG00000104626.
- **Aliases:** 3′HEXO, THEX1, HEXO.
- **Locus:** 8p23.1.
- **Protein:** UniProt Q8IV48 — a DEDDh-superfamily 3′→5′ exonuclease with an N-terminal SAP (RNA-binding) domain and a C-terminal EXOIII/DEDDh catalytic exonuclease domain.

### Pathogenic Variants
The SEMDGC-causing missense variants cluster in the **C-terminal 3′ exonuclease (EXOIII/DEDDh) domain**, sparing the N-terminal SAP RNA-binding domain.

| Family | Variant(s) | Nomenclature | Zygosity | Population frequency |
|--------|-----------|--------------|----------|---------------------|
| Family 1 | p.Glu150Asp (E150D) | rs2486219940 | — | Rare |
| Family 2 | p.Asp298Ala (D298A) + p.Pro155Leu (P155L) | c.893A>C + c.464C>T (NM_153332.4) | Compound heterozygous | D298A absent from population DBs; P155L <0.0001 in gnomAD/ExAC |
| Hoxha-Aliu (HXAL) | p.Lys118* (K118X) | 608739.0001 | Homozygous | Nonsense (null) |

- **Variant classification:** Pathogenic (functionally validated).
- **Variant types:** Missense (SEMDGC); nonsense/null (Hoxha-Aliu syndrome).
- **Somatic vs germline:** Germline.
- **Functional consequences:** The missense variants cause **loss of exoribonuclease catalytic activity**. Critically, in *ERI1*-knockout HeLa cells, the defective 5.8S rRNA processing was rescued by wild-type *ERI1* but **NOT** by the D298A or P155L mutants — confirming loss-of-catalytic-function at the enzymatic level. However, because biallelic null variants produce a milder phenotype, the missense proteins are inferred to act via a **dominant-negative/neomorphic mechanism** (the catalytically dead but still-expressed protein interferes beyond simple loss of function).

Direct evidence: "*The ERI1 missense variants cause a loss of the exoribonuclease activity, leading to defective trimming of the 5.8S rRNA 3′ end and a decreased degradation of replication-dependent histone mRNAs.*" ([PMID: 37352860](https://pubmed.ncbi.nlm.nih.gov/37352860/)).

### Modifier Genes
None established.

### Epigenetic Information
No disease-specific DNA methylation or histone-modification changes have been reported for SEMDGC itself. Of note, ERI1 participates in heterochromatin formation and RNA interference in model organisms, but a direct epigenetic disease mechanism in humans has not been demonstrated.

### Chromosomal Abnormalities
None. SEMDGC is caused by point mutations, not large-scale structural/chromosomal changes.

---

## Section 5: Environmental Information

- **Environmental factors:** None. Not applicable to this monogenic disorder.
- **Lifestyle factors:** None applicable.
- **Infectious agents:** None. This is not an infectious or trigger-mediated disease.

This section is **not applicable** to SEMDGC beyond noting the deterministic genetic etiology.

---

## Section 6: Mechanism / Pathophysiology

### Causal Chain Overview

```
Biallelic ERI1 missense variant (≥1 allele)
        │  (C-terminal DEDDh exonuclease domain)
        ▼
Loss of 3′→5′ exoribonuclease catalytic activity
   (dominant-negative / neomorphic — worse than null)
        │
        ├──► Defective 3′-end trimming of 5.8S rRNA
        │        → impaired ribosome biogenesis (ribosomopathy-like)
        │
        └──► Decreased degradation of replication-dependent histone mRNAs
                 → accumulation of oligouridylated histone mRNAs;
                   dysregulated cell-cycle-coupled histone supply
        │
        ▼
Impaired chondrocyte differentiation (defective chondrogenesis)
   + downregulation of skeletal-patterning genes
        │
        ▼
Abnormal growth-plate function
        │
        ▼
Spondyloepimetaphyseal dysplasia: short stature, platyspondyly,
epi-/metaphyseal dysplasia, digital anomalies
```

### Molecular Pathways
ERI1 is not part of a classical signaling cascade (Wnt, MAPK, etc.) but operates in two core RNA-metabolic pathways:
1. **Ribosome biogenesis** — 5.8S rRNA 3′-end maturation. "*Eri1 is an evolutionarily conserved 3′-5′ exoribonuclease that participates in 5.8S rRNA 3′ end processing and turnover of replication-dependent histone mRNAs*" ([PMID: 24929628](https://pubmed.ncbi.nlm.nih.gov/24929628/)).
2. **Replication-dependent histone mRNA turnover** — ERI1 degrades the 3′ stem-loop of oligouridylated histone mRNAs to trigger replication-dependent decay. "*Both processes are impaired in Eri1-deficient mouse cells, which instead accumulate oligouridylated histone mRNAs*" ([PMID: 23202588](https://pubmed.ncbi.nlm.nih.gov/23202588/)).

The 2025 review summarizes ERI1's multifunctional role: "*including modulating RNA interference, heterochromatin formation, rRNA maturation, and histone mRNA degradation*" ([PMID: 39945916](https://pubmed.ncbi.nlm.nih.gov/39945916/)).

### Cellular Processes
The convergent cellular phenotype is **impaired chondrogenesis**. Patient iPSC-derived chondrocytes: "*Affected-individual-derived induced pluripotent stem cells (iPSCs) showed impaired in vitro chondrogenesis with downregulation of genes regulating skeletal patterning*" ([PMID: 37352860](https://pubmed.ncbi.nlm.nih.gov/37352860/)). Because ribosome biogenesis and histone-mRNA supply are both essential for the rapid, tightly cell-cycle-coupled proliferation of growth-plate chondrocytes, this cell type is particularly vulnerable — consistent with the ribosomopathy paradigm in which defects in housekeeping RNA machinery produce tissue-selective (often skeletal) phenotypes.

### Protein Dysfunction
The pathogenic missense substitutions in the C-terminal DEDDh catalytic domain abolish exonuclease activity while (presumably) preserving expression and RNA-binding via the intact N-terminal SAP domain. This is the structural basis for a dominant-negative effect: a stable but catalytically dead enzyme that can still engage substrates/complexes and thereby interfere with residual function — explaining why missense is worse than null.

### Metabolic / Immune / Tissue-Damage Mechanisms
- **Metabolic changes:** Not a classical metabolic disorder; the "metabolism" affected is RNA metabolism.
- **Immune involvement:** Not established as a primary driver, though ERI1 has roles in RNA interference/innate nucleic-acid handling in model systems.
- **Tissue damage mechanism:** Developmental — failure of proper chondrocyte differentiation and growth-plate function rather than degenerative injury.

### Suggested Ontology Terms
- **GO (biological process):** rRNA processing (GO:0006364); ribosomal large subunit biogenesis (GO:0042273); histone mRNA catabolic process (GO:0071044); chondrocyte differentiation (GO:0002062); skeletal system development (GO:0001501).
- **GO (molecular function):** 3′-5′ exoribonuclease activity (GO:0000175); rRNA binding.
- **GO (cellular component):** cytoplasm (GO:0005737); nucleolus (GO:0005730).
- **CL (cell types):** chondrocyte (CL:0000138); growth plate chondrocyte.

---

## Section 7: Anatomical Structures Affected

### Organ Level
- **Primary:** Skeletal system — vertebral column (spine), epiphyses and metaphyses of long bones, hands and feet (digits), skull/craniofacial bones.
- **Secondary / extraskeletal (subset of severe patients):** Kidneys (renal anomalies), heart (cardiac anomalies), central nervous system (developmental delay/intellectual disability).
- **Body systems:** Musculoskeletal (primary); renal, cardiovascular, and nervous systems (secondary, variable).

### Tissue and Cell Level
- **Tissue:** Cartilage / growth-plate cartilage (connective tissue); bone.
- **Cell populations:** Chondrocytes, particularly **growth-plate chondrocytes** (CL:0000138). Chondrocyte differentiation from mesenchymal/iPSC-derived precursors is the demonstrated point of failure.

### Subcellular Level
- **Compartments:** Nucleolus (GO:0005730) — site of rRNA processing; cytoplasm (GO:0005737) — histone mRNA turnover. ERI1's activity spans nucleolar (ribosome biogenesis) and cytoplasmic (histone mRNA decay) compartments.

### Localization
- **Anatomical sites (UBERON):** vertebral column (UBERON:0001130); epiphysis (UBERON:0002515); metaphysis (UBERON:0004417); manus/digits (UBERON:0002398); growth plate (UBERON:0006611); skull (UBERON:0003129).
- **Lateralization:** Bilateral and generally symmetric (as typical for generalized skeletal dysplasias).

---

## Section 8: Temporal Development

### Onset
- **Age of onset:** Congenital / prenatal-neonatal. The skeletal dysplasia is present at birth; some features detectable prenatally.
- **Onset pattern:** Chronic/congenital (present from development).

### Progression
- **Stages:** No formal staging system exists. Skeletal features such as scoliosis progress with growth.
- **Progression rate:** Variable — correlates with genotype and residual function.
- **Course pattern:** Progressive (skeletal deformities) but non-episodic.
- **Duration:** Lifelong in survivors; lethal in a subset during infancy/early childhood.

### Patterns
- **Severity spectrum (documented):** In the founding cohort, family 1 comprised a 28-year-old woman and her 26-year-old brother (survival into adulthood), whereas families 2, 3, and 4 had children who died at **4 months, 5 months, and 2 years** of age, respectively — demonstrating infantile/early-childhood lethality in a subset.
- **Critical periods:** Fetal and early-postnatal growth-plate development is the window of vulnerability; there is no known intervention window given the developmental, genetic nature.
- **Remission:** None; this is a structural, developmental disorder without remission.

---

## Section 9: Inheritance and Population

### Epidemiology
- **Prevalence / incidence:** Ultra-rare; no formal prevalence or incidence estimates. Fewer than 10 individuals reported worldwide (8 affected individuals from 7 families in the founding cohort). Too rare for population registry quantification.

### Genetic Etiology
- **Inheritance pattern:** **Autosomal recessive** (biallelic *ERI1* variants required).
- **Penetrance:** Complete for the biochemical/skeletal phenotype given the appropriate genotype; **genotype-dependent expressivity** determines whether severe SEMD (≥1 missense) or mild Hoxha-Aliu (biallelic null) results.
- **Expressivity:** Highly variable within the severe form — from adult survival to infantile lethality.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** None established.
- **Consanguinity:** Relevant — recessive inheritance means consanguineous unions increase risk of homozygous biallelic variants (e.g., the homozygous K118X in the Nepali Hoxha-Aliu patient).
- **Carrier frequency:** Not established; expected to be very low given rarity. P155L allele frequency <0.0001 in gnomAD/ExAC; D298A absent from population databases.

### Population Demographics
- **Affected populations:** No specific ethnic predisposition; families reported are geographically/ethnically diverse.
- **Geographic distribution:** Global, sporadic; no endemic clustering.
- **Sex ratio:** No sex bias expected (autosomal); cohort included both sexes.
- **Age distribution:** Congenital-onset; affected individuals range from infants to adults (in survivors).

---

## Section 10: Diagnostics

### Clinical Tests
- **Imaging (central to diagnosis):** Skeletal survey / radiography (X-ray) revealing platyspondyly (HP:0000926), irregular vertebral endplates (HP:0003417), epiphyseal and metaphyseal dysplasia, scoliosis, and digital anomalies. Radiographic pattern recognition is the first-line diagnostic modality for skeletal dysplasias.
- **Laboratory tests:** No specific biochemical marker; biochemical tests (e.g., for mucopolysaccharidoses) are used to *exclude* differential diagnoses.
- **Biomarkers:** None validated (no circulating protein/metabolite biomarker).
- **Biopsy/pathology:** Not routinely used; cartilage histology may show abnormal chondrocyte organization but is not standard.

### Genetic Testing (definitive)
- **Recommended approach:** Molecular confirmation of **biallelic *ERI1* variants** via sequencing.
- **WES / WGS:** High utility — exome or genome sequencing is the primary route to diagnosis, especially given the rarity and the need to detect two variants in *ERI1*. GeneMatcher-type data sharing was instrumental in defining the cohort.
- **Gene panels:** Skeletal dysplasia / SEMD gene panels including *ERI1*.
- **Single-gene testing:** Targeted *ERI1* sequencing when the phenotype is recognized.
- **CMA / karyotype / FISH / mtDNA / repeat expansion:** Not indicated (point-mutation disorder).

### Omics-Based Diagnostics
- Functional/research assays: iPSC-derived chondrogenesis and 5.8S rRNA processing/histone mRNA turnover assays can confirm variant pathogenicity but are research tools, not clinical diagnostics.

### Clinical Criteria & Differential Diagnosis
- **Diagnostic criteria:** Combination of characteristic radiographic SEMD pattern + biallelic *ERI1* variants (≥1 missense for the severe form).
- **Differential diagnosis:** Other spondyloepimetaphyseal dysplasias and skeletal dysplasias, including:
  - **Dyggve-Melchior-Clausen (DMC) syndrome** — AR SEMD with platyspondyly, rhizomelic shortening, metaphyseal dysplasia; overlaps with MPS IV; caused by *DYM* variants ([PMID: 41549465](https://pubmed.ncbi.nlm.nih.gov/41549465/)).
  - **SEMD with joint laxity, leptodactylic (Hall) type** — short stature, midface hypoplasia, joint dislocations/laxity, metaphyseal vertical striations ([PMID: 19277648](https://pubmed.ncbi.nlm.nih.gov/19277648/)).
  - **Mucopolysaccharidosis type IV (Morquio)** — excluded by urine GAG / enzyme testing.
- Genetic testing distinguishes SEMDGC from these phenocopies.

### Screening
- **Cascade / carrier screening:** Offered to relatives once a familial variant is identified.
- **Prenatal testing:** Available for at-risk pregnancies via targeted variant testing.
- **Newborn screening:** Not part of any newborn screening program.

---

## Section 11: Outcome / Prognosis

### Survival and Mortality
- **Life expectancy:** Highly variable and genotype/severity-dependent. Documented outcomes range from **survival into adulthood** (28- and 26-year-old sibs, family 1) to **early death** (4 months, 5 months, 2 years in families 2–4).
- **Mortality:** A significant subset of severe (missense) SEMDGC is **infantile/early-childhood lethal**. The milder null-allele (Hoxha-Aliu) form is not lethal.

### Morbidity and Function
- Survivors face substantial morbidity: severe short stature, skeletal deformity/scoliosis, digital malformations, and (in some) intellectual disability and extraskeletal (renal/cardiac) complications, all impairing mobility, dexterity, and independence.
- Formal disability/QoL metrics have not been reported for this ultra-rare disease.

### Disease Course & Complications
- Complications include progressive scoliosis, joint/limb deformity, and — in severely affected infants — the systemic consequences that lead to early death (potentially compounded by renal/cardiac anomalies).
- Recovery potential: none; the disorder is structural and developmental, without curative options.

### Prognostic Factors
- **Genotype is the key prognostic factor:** missense (≥1 allele) → severe SEMD, potentially lethal; biallelic null → mild phenotype (Hoxha-Aliu).
- No validated prognostic biomarkers beyond genotype.

---

## Section 12: Treatment

There is **no curative or disease-modifying therapy** for SEMDGC. Management is **supportive and multidisciplinary**.

### Pharmacotherapy
- No approved pharmacotherapy targets the underlying RNA-metabolic defect. Symptomatic management (e.g., analgesia for musculoskeletal pain) as needed.
- **Pharmacogenomics:** Not applicable.

### Advanced Therapeutics
- **Gene therapy / gene editing, RNA-based, cell, immuno-, targeted therapies:** None available or in trials for SEMDGC. The dominant-negative/neomorphic mechanism suggests that allele-specific silencing (e.g., ASO/siRNA against the mutant allele) is a *theoretically* rational future strategy, but this is purely conceptual at present.

### Surgical and Interventional
- Orthopedic surgery for scoliosis and limb/joint deformities as clinically indicated (NCIT: Orthopedic Surgical Procedure).

### Supportive and Rehabilitative
- Physical therapy, occupational therapy, orthotics, and mobility aids to optimize function (NCIT: Physical Therapy, Occupational Therapy).
- Management of extraskeletal complications (renal, cardiac) per subspecialty guidelines when present.

### Experimental
- No registered clinical trials specific to SEMDGC (ultra-rare condition).

### Treatment Strategy
- Supportive, symptom-directed, multidisciplinary care coordinated by clinical genetics, orthopedics, and relevant subspecialties.
- **Suggested NCIT concepts:** Supportive Care; Physical Therapy; Orthopedic Surgery; Genetic Counseling.

---

## Section 13: Prevention

### Prevention Levels
- **Primary prevention:** Not possible for occurrence in a conceived affected individual (genetic, congenital). Prevention is achieved at the reproductive level via genetic counseling and reproductive options.
- **Secondary prevention:** Early diagnosis (radiographic + genetic) to enable timely supportive/orthopedic management and surveillance for extraskeletal complications.
- **Tertiary prevention:** Management to prevent/limit complications (scoliosis progression, joint deformity).

### Genetic Screening & Counseling
- **Genetic counseling** is central: for autosomal-recessive inheritance, unaffected carrier parents have a 25% recurrence risk per pregnancy.
- **Carrier / cascade screening** for at-risk relatives once the familial variants are known.
- **Prenatal diagnosis** and **preimplantation genetic testing (PGT)** are options for families with known biallelic variants.
- Consanguinity counseling is relevant in affected/at-risk families.

### Immunization / Public Health / Environmental / Behavioral
- Not applicable — no infectious, environmental, or behavioral component.

---

## Section 14: Other Species / Natural Disease

### Taxonomy & Orthologs
*ERI1* is highly evolutionarily conserved. Orthologs (with NCBI Gene where noted):

| Species | Gene | Identifier |
|---------|------|-----------|
| Human (*Homo sapiens*) | *ERI1* | Gene 90459 |
| Mouse (*Mus musculus*) | *Eri1* | MGI:1914526 / Gene 67276 |
| Zebrafish (*Danio rerio*) | *eri1* | Gene 553641 |
| *C. elegans* | *eri-1* | — |
| Rat, chicken, cow, dog, cat, horse, sheep | *Eri1/ERI1* | conserved orthologs |

### Natural Disease in Other Species
- No naturally occurring SEMDGC-equivalent disease has been reported in companion animals or wildlife (OMIA lists no established natural *ERI1* skeletal-dysplasia phenotype).

### Comparative Biology
- The 3′→5′ exoribonuclease function and its roles in 5.8S rRNA processing and histone mRNA turnover are **evolutionarily conserved** from *C. elegans* to humans, underscoring that these functions are ancient and essential. Functional conservation of ERI1's roles across human cells and the mouse ortholog was demonstrated by Guo et al. 2023.

### Transmission
- Not applicable (non-infectious genetic disorder; no zoonotic potential).

---

## Section 15: Model Organisms

### Available Models
| Model | Type | Key phenotype | Recapitulation |
|-------|------|---------------|----------------|
| *Eri1*-knockout mouse | Mammalian, null | Postnatal lethality, decreased body size from ~E15.5, reduced MEF proliferation, brachydactyly, mild platyspondyly | **Partial** — models the *null* (Hoxha-Aliu) end, NOT severe SEMDGC |
| Patient-derived iPSCs | In vitro human, missense | Impaired chondrogenesis, downregulated skeletal-patterning genes | **Good** — reproduces the cellular chondrogenic defect |
| *ERI1*-knockout HeLa cells | In vitro human | 5.8S rRNA processing defect (rescued by WT but not D298A/P155L) | Functional validation platform |

### Model Characteristics & Limitations
- **Mouse KO:** "*Although Eri1 knockout (KO) mice showed mild skeletal phenotypes, neither SEMD nor digital anomaly were found*" ([PMID: 39945916](https://pubmed.ncbi.nlm.nih.gov/39945916/)). X-ray/histology showed reduced body size and brachydactyly but no clear epimetaphyseal changes; the mild platyspondyly was attributed to small body size. The authors concluded the **KO phenotype resembles human null-variant (Hoxha-Aliu) patients rather than the missense (SEMDGC) patients** — an important caveat: a knockout does not model a dominant-negative missense disorder. A knock-in of the missense allele would be the appropriate model.
- **iPSC model:** Reproduces impaired chondrocyte differentiation — the most disease-relevant human cellular readout.

### Applications & Resources
- Models enable study of RNA-metabolic function (rRNA/histone mRNA), chondrogenesis, and variant pathogenicity.
- **Resources:** MGI (mouse *Eri1*, MGI:1914526), ZFIN (zebrafish *eri1*), Cellosaurus/patient iPSC lines.

---

## Mechanistic Model / Interpretation

SEMDGC is best understood as a **ribosomopathy-like RNA-metabolic disorder with a neomorphic twist**. The central, non-obvious insight is the **inverse genotype–phenotype relationship**:

```
Molecular severity:   NULL (nonsense)   <   MISSENSE (catalytically dead but stable)
Clinical severity:    MILD (Hoxha-Aliu) <   SEVERE (SEMDGC, sometimes lethal)
```

A simple loss-of-function model would predict that null alleles (which remove the protein entirely) should be at least as severe as missense alleles. The **opposite is observed**, which is the signature of a **dominant-negative or neomorphic (gain-of-toxic-function) mechanism**: the missense proteins retain expression and likely RNA-binding (intact N-terminal SAP domain) but lack catalysis (mutated C-terminal DEDDh domain), allowing them to occupy substrates or complexes non-productively and interfere with residual RNA-processing capacity beyond mere absence of the enzyme.

Downstream, the loss of ERI1 catalytic function corrupts two housekeeping RNA pathways — **5.8S rRNA 3′-end maturation** (ribosome biogenesis) and **replication-dependent histone mRNA decay** (cell-cycle-coupled histone homeostasis). Both are indispensable for the intense proliferative and biosynthetic demands of **growth-plate chondrocytes**, explaining the tissue-selective skeletal phenotype despite the ubiquitous expression of *ERI1*. The patient iPSC data — impaired chondrogenesis with downregulated skeletal-patterning genes — provide the empirical bridge from RNA machinery to bone.

This model is corroborated by the mouse: because the KO removes the protein (mimicking the human null/Hoxha-Aliu allele), it produces only the mild phenotype and *fails* to reproduce SEMD — exactly as the neomorphic model predicts.

### Allelic Series Summary
| Disorder | OMIM | ERI1 allele type | Phenotype |
|----------|------|------------------|-----------|
| **SEMDGC (Guo-Campeau)** | #620663 | ≥1 missense (biallelic) | Severe SEMD; can be infantile-lethal |
| **Hoxha-Aliu syndrome (HXAL)** | #620662 | Biallelic nonsense (null), e.g., K118X | Mild ID, ptosis, brachydactyly, digital/nail anomalies |

*(Note: A "renal hypodysplasia/aplasia 3, #617805" association listed by some aggregators (GeneCards) is a curation artifact and is NOT an established ERI1 disorder. Renal and cardiac anomalies with developmental delay were, however, observed as features in one severe SEMDGC patient — family 4.)*

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [37352860](https://pubmed.ncbi.nlm.nih.gov/37352860/) | *Null and missense mutations of ERI1 cause a recessive phenotypic dichotomy in humans* | **Landmark/defining study.** Establishes *ERI1* as the causal gene; documents the missense-vs-null dichotomy; provides variant, enzymatic, iPSC-chondrogenesis, and mouse data. Cohort of 8 individuals/7 families. |
| [39945916](https://pubmed.ncbi.nlm.nih.gov/39945916/) | *Congenital Bone Disorders Associated with ERI1-Mediated RNA Metabolism Dysfunction: SEMDGC and Beyond* (2025) | **Comprehensive review.** Independently confirms the genotype–phenotype dichotomy; summarizes ERI1's multifunctional RNA roles; documents model limitations (KO mouse resembles null patients). |
| [24929628](https://pubmed.ncbi.nlm.nih.gov/24929628/) | *Eri1: a conserved enzyme at the crossroads of multiple RNA-processing pathways* | Defines the normal molecular functions of ERI1 (5.8S rRNA processing, histone mRNA turnover) disrupted in disease. |
| [23202588](https://pubmed.ncbi.nlm.nih.gov/23202588/) | *Eri1 degrades the stem-loop of oligouridylated histone mRNAs to induce replication-dependent decay* | Mechanistic basis of the histone-mRNA arm; shows Eri1-deficient cells accumulate oligouridylated histone mRNAs. |
| [41549465](https://pubmed.ncbi.nlm.nih.gov/41549465/) | *Dyggve-Melchior-Clausen syndrome in three siblings...* | Differential diagnosis (DMC syndrome; another AR SEMD with platyspondyly/metaphyseal dysplasia). |
| [19277648](https://pubmed.ncbi.nlm.nih.gov/19277648/) | *A distinct form of SEMD with joint laxity (SEMDJL)-leptodactylic type* | Differential diagnosis (another SEMD subtype). |

**Key supporting quotes:**
- Genotype–phenotype dichotomy: "*A severe spondyloepimetaphyseal dysplasia (SEMD) was identified in five affected individuals with missense variants but not in those with bi-allelic null variants, who showed mild intellectual disability and digital anomalies*" ([PMID: 37352860](https://pubmed.ncbi.nlm.nih.gov/37352860/)).
- Enzymatic/RNA consequence: "*The ERI1 missense variants cause a loss of the exoribonuclease activity, leading to defective trimming of the 5.8S rRNA 3′ end and a decreased degradation of replication-dependent histone mRNAs*" ([PMID: 37352860](https://pubmed.ncbi.nlm.nih.gov/37352860/)).
- Cellular mechanism: "*Affected-individual-derived induced pluripotent stem cells (iPSCs) showed impaired in vitro chondrogenesis with downregulation of genes regulating skeletal patterning*" ([PMID: 37352860](https://pubmed.ncbi.nlm.nih.gov/37352860/)).
- Normal ERI1 function: "*Eri1 is an evolutionarily conserved 3′-5′ exoribonuclease that participates in 5.8S rRNA 3′ end processing and turnover of replication-dependent histone mRNAs*" ([PMID: 24929628](https://pubmed.ncbi.nlm.nih.gov/24929628/)).
- Histone mRNA arm: "*Both processes are impaired in Eri1-deficient mouse cells, which instead accumulate oligouridylated histone mRNAs*" ([PMID: 23202588](https://pubmed.ncbi.nlm.nih.gov/23202588/)).
- ERI1 multifunctionality: "*including modulating RNA interference, heterochromatin formation, rRNA maturation, and histone mRNA degradation*" ([PMID: 39945916](https://pubmed.ncbi.nlm.nih.gov/39945916/)).
- Model limitation: "*Although Eri1 knockout (KO) mice showed mild skeletal phenotypes, neither SEMD nor digital anomaly were found*" ([PMID: 39945916](https://pubmed.ncbi.nlm.nih.gov/39945916/)).

**Evidence source types:** human clinical/genetic (cohort and case reports), in vitro (iPSC-derived chondrocytes, HeLa rescue assays, enzymatic activity), and model organism (mouse, zebrafish, *C. elegans*).

---

## Limitations and Knowledge Gaps

1. **Ultra-small evidence base.** The disease is defined by a single cohort (8 individuals/7 families) plus one review. Epidemiological parameters (prevalence, incidence, carrier frequency, sex ratio) are unknown.
2. **Mechanism not fully resolved.** The dominant-negative/neomorphic model is strongly inferred from the inverse genotype–phenotype relationship and rescue assays, but the precise molecular mechanism by which the catalytically dead protein produces a *worse* phenotype than its absence has not been directly demonstrated (e.g., no structural or interactome study of the mutant protein interfering with a complex).
3. **No missense knock-in animal model.** The existing *Eri1*-KO mouse models the null (Hoxha-Aliu) end, not SEMDGC. A knock-in of a patient missense allele is needed to faithfully model the severe disease.
4. **Extraskeletal phenotype incompletely characterized.** Renal, cardiac, and neurodevelopmental features were noted in only a subset (family 4) and their penetrance/mechanism are unclear.
5. **Genotype–phenotype granularity.** Which specific missense residues correlate with lethal vs adult-survival outcomes is not established; the sample is too small.
6. **Epigenetic and multi-omic data absent.** No methylation, proteomic, or metabolomic profiling of patient tissues exists.
7. **Database curation artifact.** The "renal hypodysplasia/aplasia 3" (RHDA3, #617805) association listed by some aggregators (GeneCards) is NOT a validated ERI1 disorder — only SEMDGC (#620663) and Hoxha-Aliu syndrome (#620662) are established ERI1 phenotypes.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a missense knock-in mouse** (e.g., *Eri1* D298A or P155L) to test whether the missense allele — unlike the KO — recapitulates severe SEMD, directly validating the neomorphic model.
2. **Biochemically dissect the dominant-negative mechanism:** compare mutant vs WT ERI1 in substrate binding, complex incorporation, and competition assays; determine whether mutant protein sequesters substrates/partners.
3. **Deep-phenotype and expand the cohort** via international data sharing (GeneMatcher, Matchmaker Exchange) to define penetrance of extraskeletal features and refine residue-level genotype–phenotype correlations.
4. **Multi-omic profiling of patient iPSC-chondrocytes:** RNA-seq (skeletal-patterning gene networks), ribosome profiling (translational impact of 5.8S rRNA defect), and histone mRNA/protein quantification to map the causal chain quantitatively.
5. **Test allele-selective therapeutic concepts in vitro:** ASO/siRNA knockdown of the mutant allele in patient iPSC-chondrocytes to determine whether removing the dominant-negative protein rescues chondrogenesis — a proof-of-concept for future therapy.
6. **Correct database curation:** flag the erroneous RHDA3/#617805–ERI1 association and ensure knowledge bases list only SEMDGC (#620663) and Hoxha-Aliu syndrome (#620662).
7. **Establish natural-history surveillance guidance:** given the lethal subset, define recommended monitoring (renal, cardiac, spinal/scoliosis) for diagnosed infants.

---

*Report compiled from a 5-iteration autonomous investigation. Evidence types: human clinical (cohort/case reports), in vitro (iPSC-chondrocytes, HeLa rescue assays), and model organism (mouse, zebrafish, C. elegans). All mechanistic and clinical claims are attributed to the cited primary literature and review as indicated.*


## Artifacts

- [OpenScientist final report](Spondyloepimetaphyseal_Dysplasia_Guo-Campeau_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spondyloepimetaphyseal_Dysplasia_Guo-Campeau_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 6 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0958006` (2 mentions) - the report calls it "MONDO"; MONDO calls it **spondyloepimetaphyseal dysplasia, Guo-Campeau type**
- `HP:0003510` (1 mention) - the report calls it "Physical/growth"; HP calls it **Severe short stature**
- `HP:0000926` (2 mentions) - the report calls it "Skeletal/radiographic"; HP calls it **Platyspondyly**
- `HP:0003417` (2 mentions) - the report calls it "Radiographic"; HP calls it **Coronal cleft vertebrae**
- `HP:0002650` (1 mention) - the report calls it "Skeletal"; HP calls it **Scoliosis**
- `HP:0030084` (1 mention) - the report calls it "Digital"; HP calls it **Clinodactyly**
- `HP:0012385` (1 mention) - the report calls it "Digital"; HP calls it **Camptodactyly**
- `HP:0001159` (1 mention) - the report calls it "Digital"; HP calls it **Syndactyly**
- `HP:0000268` (1 mention) - the report calls it "Craniofacial"; HP calls it **Dolichocephaly**
- `HP:0000243` (1 mention) - the report calls it "Craniofacial"; HP calls it **Trigonocephaly**
- `HP:0001256` (1 mention) - the report calls it "Neurodevelopmental"; HP calls it **Mild intellectual disability**
- `CL:0000138` (2 mentions) - the report calls it "growth-plate chondrocytes", "Cell populations:** Chondrocytes, particularly **growth-plate chondrocytes"; CL calls it **chondrocyte**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Neurodevelopmental"; HP calls it **Global developmental delay**, and lists "Developmental delay" among its other names
- `GO:0005730` (2 mentions) - the report calls it "Compartments:** Nucleolus"; GO calls it **nucleolus**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000138` - called "growth-plate chondrocytes", "Cell populations:** Chondrocytes, particularly **growth-plate chondrocytes"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.