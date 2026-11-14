---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T18:12:07.737730'
end_time: '2026-11-12T18:51:48.671712'
duration_seconds: 2380.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Platyspondylic Dysplasia, Torrance Type
  mondo_id: MONDO:0007895
  category: Mendelian
  causal_genes: COL2A1
  omim_id: OMIM:151210
  synonyms: platyspondylic skeletal dysplasia, Torrance type; PLSD-T; Platyspondylic
    dysplasia, Torrance-Luton type; Platyspondylic lethal skeletal dysplasia, Torrance
    type
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
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 12
  validator_version: 0.5.1
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 10
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: HP:0000926
    reported_labels:
    - Radiographic sign
    ontology_label: Platyspondyly
  - term_id: HP:0001156
    reported_labels:
    - Physical manifestation
    ontology_label: Brachydactyly
  - term_id: HP:0000944
    reported_labels:
    - Radiographic sign
    ontology_label: Abnormal metaphysis morphology
  - term_id: HP:0002089
    reported_labels:
    - Clinical/pathologic
    ontology_label: Pulmonary hypoplasia
  - term_id: HP:0004322
    reported_labels:
    - Physical manifestation
    ontology_label: Short stature
  - term_id: HP:0000256
    reported_labels:
    - Physical manifestation
    ontology_label: Macrocephaly
  - term_id: CL:0000138
    reported_labels:
    - chondrocyte
    - Growth-plate chondrocytes
    - Cell level:** **Growth-plate chondrocytes
    ontology_label: chondrocyte
  - term_id: UBERON:0002515
    reported_labels:
    - growth plate / cartilage growth plate
    ontology_label: periosteum
  - term_id: UBERON:0001091
    reported_labels:
    - cartilage
    ontology_label: calcareous tooth
  - term_id: UBERON:0002228
    reported_labels:
    - rib cage/thorax
    ontology_label: rib
  - term_id: NCIT:C15277
    reported_labels:
    - Supportive Care
    ontology_label: Mastectomy
  - term_id: NCIT:C15431
    reported_labels:
    - Palliative Care
    ontology_label: Hematopoietic Cell Transplantation
  - term_id: NCIT:C15329
    reported_labels:
    - Physical Therapy
    ontology_label: Surgical Procedure
  - term_id: NCIT:C15215
    reported_labels:
    - Respiratory Therapy
    ontology_label: Cryosurgery
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Platyspondylic_Dysplasia_Torrance_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Platyspondylic_Dysplasia_Torrance_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Platyspondylic Dysplasia, Torrance Type
- **MONDO ID:** MONDO:0007895 (if available)
- **Causal gene(s):** COL2A1
- **OMIM:** OMIM:151210
- **Synonyms:** platyspondylic skeletal dysplasia, Torrance type; PLSD-T; Platyspondylic dysplasia, Torrance-Luton type; Platyspondylic lethal skeletal dysplasia, Torrance type
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Platyspondylic Dysplasia, Torrance Type** covering all of the
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

# Platyspondylic Dysplasia, Torrance Type (PLSD-T) — Comprehensive Disease Report

**Disease:** Platyspondylic Dysplasia, Torrance type (PLSD-T)
**MONDO:** MONDO:0007895 · **OMIM:** 151210 · **Causal gene:** **COL2A1** (type II collagen, alpha-1 chain; HGNC:2200; chromosome 12q13.11)
**Category:** Mendelian, autosomal dominant

---

## Summary

Platyspondylic Dysplasia, Torrance type (PLSD-T) is a rare, usually perinatally lethal skeletal dysplasia caused by heterozygous **dominant-negative mutations in the C-propeptide (COOH-/NC2 propeptide) domain of the *COL2A1* gene**, which encodes the alpha-1 chain of type II (cartilage) collagen. It is therefore a **type II collagenopathy**, and specifically defines a distinct **C-propeptide subfamily** within that group of disorders, separate from the more numerous triple-helical-domain type II collagenopathies (achondrogenesis type II, hypochondrogenesis, spondyloepiphyseal dysplasia congenita, Kniest dysplasia, Stickler syndrome). The cardinal features are **platyspondyly** (flat, severely under-ossified vertebral bodies), **micromelia** (extremely short limbs), **brachydactyly**, and characteristic **metaphyseal changes**, with a small thorax causing lethal pulmonary hypoplasia. Most affected infants are stillborn or die in the neonatal period, though rare long-term survivors have been reported.

The mechanistic basis is well established and unusually clear for a rare dysplasia. Unlike loss-of-function/haploinsufficiency mechanisms, the C-propeptide mutations (missense, last-exon nonsense variants that escape nonsense-mediated decay, and frameshift variants) produce an **altered pro-alpha-1(II) chain** that cannot assemble/trimerize and secrete normally. The mutant chains are **retained in the chondrocyte endoplasmic reticulum (ER)**, triggering **ER stress and the unfolded protein response (UPR)** (upregulation of *Grp94*/HSP90B1 and *Chop*/DDIT3), **expanded/distended rough ER**, and **growth-plate chondrocyte apoptosis**. The combination of defective cartilage matrix and chondrocyte death disrupts endochondral ossification, producing the skeletal phenotype. This causal chain has been directly demonstrated in three independent semidominant *Col2a1* C-propeptide mouse models (p.D1469A, p.Y1391S, and the classic disproportionate micromelia *Dmm* allele).

PLSD-T lies on an **allelic phenotypic continuum** with the milder, viable **spondyloperipheral dysplasia (SPD)**: identical C-propeptide mutations (e.g., Y1391C) have been reported in both lethal PLSD-T and surviving SPD patients. Familial recurrence from phenotypically normal parents is explained by **germline (germinal) mosaicism**, and a documented mother–fetus pair sharing the same mutation illustrates **somatic mosaicism** producing mild SPD in the mosaic parent and lethal PLSD-T in the fully-affected offspring. There is no disease-modifying therapy; management is supportive/palliative, and the mainstays of care are accurate diagnosis, genetic counseling, and reproductive risk management.

---

## Key Findings

### Finding 1 — PLSD-T is caused by dominant-negative C-propeptide mutations in *COL2A1*

The defining molecular study (Zankl et al., 2005) examined eight additional PLSD-T cases (plus two previously reported) and found that **all** had mutations localized to the **C-propeptide domain** of *COL2A1*. The mutational spectrum includes **missense, nonsense (stop-codon), and frameshift** mutations. Critically, all nonsense mutations fell within the **last exon**, where they escape nonsense-mediated mRNA decay (NMD) — meaning a stable, altered protein is produced rather than a null allele. This establishes PLSD-T as a **dominant-negative** disorder of collagen chain assembly, not haploinsufficiency, and defines it as a "**novel subfamily within the type 2 collagenopathies**."

> *"We studied eight additional cases of PLSD-T and found that all had mutations in the C-propeptide domain of COL2A1. The mutational spectrum includes missense, stop codon and frameshift mutations. All non-sense mutations were located in the last exon, where they would escape non-sense-mediated RNA-decay."* — [PMID: 15643621](https://pubmed.ncbi.nlm.nih.gov/15643621/)

**Mechanistic significance:** The C-propeptide is essential for correct selection and nucleation of the three pro-alpha chains into the procollagen trimer. A mutation here produces a chain that incorporates into (or blocks) trimer assembly, poisoning the product of the normal allele — the hallmark of a dominant-negative effect.

### Finding 2 — ER stress-mediated chondrocyte apoptosis is the mechanistic driver

Two independent *Col2a1* ENU-induced mutant mouse lines carrying C-propeptide mutations (**p.D1469A** and **p.Y1391S**) at residues corresponding to human PLSD-T mutations recapitulated the lethal skeletal dysplasia when homozygous (extremely short limbs, severe spondylar and pelvic dysplasia, brachydactyly). In these mice, secretion of the mutant collagen into the extracellular space was disrupted, the rough ER was abnormally expanded, ER-stress/UPR genes (*Grp94*, *Chop*) were upregulated, and **chondrocyte apoptosis was severely induced** in the growth plate.

> *"The secretion of the mutant proteins into the extracellular space was disrupted, accompanied by an abnormally expanded endoplasmic reticulum (ER) and the up-regulation of ER stress-related genes in chondrocytes. Chondrocyte apoptosis was severely induced in the growth plate of the homozygotes."* — [PMID: 26545783](https://pubmed.ncbi.nlm.nih.gov/26545783/)

> *"The secretion of the mutant proteins into the extracellular space was disrupted, accompanied by abnormally expanded rough endoplasmic reticulum (ER) and upregulation of ER stress-related genes, such as Grp94 and Chop, in chondrocytes."* — [PMID: 21538020](https://pubmed.ncbi.nlm.nih.gov/21538020/)

**Mechanistic significance:** This provides direct in-vivo evidence that **ER retention → UPR activation → chondrocyte apoptosis** is the pathway linking the mutation to growth-plate failure, in two independently-derived models.

### Finding 3 — PLSD-T and spondyloperipheral dysplasia form an allelic spectrum with germline/somatic mosaicism

The same C-propeptide mutations cause lethal PLSD-T and the milder, viable **spondyloperipheral dysplasia (SPD)**; for example, the **Y1391C** substitution has been reported in both conditions, directly demonstrating a phenotypic continuum. Recurrence in two siblings born to phenotypically normal parents (c.3545G>A, p.Gly1182Asp) proved **germinal (germline) mosaicism** in a parent. A separate mother–fetus pair sharing c.4458_4460delCTT (p.Phe1486del) demonstrated **somatic mosaicism**: the mosaic mother had mild SPD while her non-mosaic fetus had lethal PLSD-T.

> *"the presence of the same mutation in the two sibs is proof of germinal mosaicism in one of the parents"* — [PMID: 22711552](https://pubmed.ncbi.nlm.nih.gov/22711552/)

> *"The phenotype in the mother was compatible with mild spondyloperipheral dysplasia (SPD). Molecular studies documented somatic mosaicism for the same mutation in the mother."* — [PMID: 22495950](https://pubmed.ncbi.nlm.nih.gov/22495950/)

**Clinical significance:** This explains apparent "autosomal recessive"-looking recurrence in sporadic dominant disease, and has direct recurrence-risk and genetic-counseling implications. The dosage/mosaicism dependence of severity is a recurring theme across the human and mouse data.

### Finding 4 — Multiple *Col2a1* C-propeptide mouse models recapitulate the disease via impaired procollagen assembly/secretion

Three semidominant mouse lines carry *Col2a1* C-propeptide mutations: the ENU alleles **p.D1469A** (PMID 21538020) and **p.Y1391S** (PMID 26545783), and the classic **disproportionate micromelia (*Dmm*)** allele (PMID 18678883). Homozygotes show lethal dwarfism with short limbs and spondylar dysplasia; heterozygotes show mild dwarfism — a clean **gene-dosage-dependent severity gradient**. Ultrastructurally, chondrocytes show distended rough ER, impaired assembly/secretion of type II procollagen trimers, thinner and sparser cartilage fibrils, and reduced aggrecan mRNA.

> *"These findings support the prevailing hypothesis that a C-propeptide mutation could interrupt the normal assembly and secretion of Type II procollagen trimers"* — [PMID: 18678883](https://pubmed.ncbi.nlm.nih.gov/18678883/)

> *"The phenotype was inherited as a semidominant trait. The heterozygotes were mildly but significantly smaller than wild-type mice. The homozygotes exhibited lethal skeletal dysplasias"* — [PMID: 21538020](https://pubmed.ncbi.nlm.nih.gov/21538020/)

**Significance:** These faithful models confirm the human mechanism and provide a platform for testing interventions targeting ER stress/UPR.

### Finding 5 — PLSD-T clinical/radiographic phenotype: platyspondyly, micromelia, brachydactyly, metaphyseal changes, perinatal lethality

PLSD-T is defined clinically and radiographically by **platyspondyly, brachydactyly, and metaphyseal changes**, and is generally **perinatally lethal**, though a few long-term survivors are on record. Fetal descriptions emphasize **platyspondyly, extremely short limbs, and mild brachydactyly**. The distinctive radiology — metaphyseal changes plus brachydactyly — is what separates this C-propeptide subfamily from the helical-domain type II collagenopathies.

> *"Platyspondylic lethal skeletal dysplasia (PLSD) Torrance type (PLSD-T) is a rare skeletal dysplasia characterized by platyspondyly, brachydactyly, and metaphyseal changes. Generally a perinatally lethal disease, a few long-term survivors have been reported."* — [PMID: 15643621](https://pubmed.ncbi.nlm.nih.gov/15643621/)

> *"a rare skeletal dysplasia characterized by platyspondyly, extremely short limbs, and mild brachydactyly"* — [PMID: 22495950](https://pubmed.ncbi.nlm.nih.gov/22495950/)

---

## Report by Section

### 1. Disease Information

PLSD-T is a rare, usually lethal **chondrodysplasia / skeletal dysplasia** of the type II collagenopathy group. It is characterized by severe platyspondyly, extremely short limbs (micromelia), brachydactyly, and characteristic metaphyseal changes, with a narrow thorax leading to pulmonary hypoplasia and perinatal death.

**Key identifiers:**
- **OMIM:** 151210
- **MONDO:** MONDO:0007895
- **Gene:** *COL2A1* (OMIM 120140; HGNC:2200; NCBI Gene 1280; UniProt P02458)
- **Orphanet:** Platyspondylic dysplasia, Torrance type (within the type II collagenopathy / lethal platyspondylic dysplasia group)
- **ICD-10:** Q77.x (chondrodysplasia with defects of growth of tubular bones and spine); **ICD-11:** LD24 (chondrodysplasias)
- **MeSH:** closest terms — Osteochondrodysplasias; Dwarfism

**Synonyms:** platyspondylic skeletal dysplasia, Torrance type; PLSD-T; Platyspondylic dysplasia, Torrance-Luton type; Platyspondylic lethal skeletal dysplasia, Torrance type.

**Information source:** Aggregated disease-level resources (OMIM, Orphanet) combined with primary case reports and small case series (individual patients/fetuses). There is no large EHR-based cohort given the rarity and lethality.

### 2. Etiology

- **Primary cause:** Genetic — heterozygous **dominant-negative mutations in the C-propeptide domain of *COL2A1*** (Finding 1). The condition is monogenic and Mendelian; no environmental or infectious etiology.
- **Genetic risk factors:** The causal variants themselves are the risk factor. Most cases arise from **de novo** mutations; **germline and somatic mosaicism** in a parent can cause recurrence or mild parental phenotypes (Finding 3).
- **Environmental risk factors:** None identified. As with most de novo dominant disorders, advanced parental age is a theoretical contributor to de novo mutation rate but is not specifically established for PLSD-T.
- **Protective factors:** None known (genetic or environmental). Not applicable for a fully-penetrant dominant-negative lethal disorder.
- **Gene–environment interactions:** None established; the phenotype is essentially determined by the specific mutation and its dosage/mosaic status.

### 3. Phenotypes

All phenotypes are **congenital/neonatal**, **severe**, and generally **non-progressive** (the disorder is lethal in the perinatal period, so progression is largely moot). Frequencies are "typical/near-universal" in affected individuals given the small reported case numbers.

| Phenotype | Type | HPO term (suggested) | Onset / severity / frequency |
|---|---|---|---|
| Platyspondyly (flat vertebral bodies) | Radiographic sign | HP:0000926 | Congenital; severe; near-universal |
| Micromelia / extremely short limbs | Physical manifestation | HP:0002983 (micromelia) / HP:0003097 (short femur) | Congenital; severe; near-universal |
| Brachydactyly | Physical manifestation | HP:0001156 | Congenital; mild–moderate; frequent |
| Metaphyseal changes/dysplasia | Radiographic sign | HP:0000944 | Congenital; characteristic; frequent |
| Narrow/small thorax | Clinical sign | HP:0000774 (narrow chest) | Congenital; severe |
| Pulmonary hypoplasia | Clinical/pathologic | HP:0002089 | Congenital; cause of lethality |
| Perinatal/neonatal lethality | Outcome | HP:0003811 (neonatal death) | Usual outcome |
| Short stature / dwarfism (survivors) | Physical manifestation | HP:0004322 | In rare survivors; severe disproportionate |
| Macrocephaly (reported in SPD end) | Physical manifestation | HP:0000256 | Variable |

**Quality-of-life impact:** For the lethal presentation, QoL metrics are not applicable (perinatal death). For rare survivors and for the milder SPD end of the spectrum, expect profound disproportionate short stature, orthopedic/spinal complications, and respiratory compromise with substantial impact on mobility and daily function. No disease-specific EQ-5D/SF-36 data exist.

### 4. Genetic/Molecular Information

- **Causal gene:** *COL2A1* (12q13.11), encoding pro-alpha-1(II) collagen chain.
- **Pathogenic variants:** Located in the **C-propeptide (COOH-/NC2) domain**, encoded largely by the final exons. Variant classes: **missense**, **nonsense** (last-exon, NMD-escaping), and **frameshift**. Representative reported variants: **Y1391C/Y1391S**, **D1469A** (mouse-equivalent residue), **p.Gly1182Asp (c.3545G>A)**, **p.Phe1486del (c.4458_4460delCTT)** (Findings 1, 3). Per ACMG/AMP, such variants are classified **pathogenic/likely pathogenic** given gene–phenotype match, functional data, and de novo occurrence.
- **Allele frequency:** Absent from population databases (gnomAD); these are private, disease-causing variants, consistent with a lethal dominant disorder.
- **Somatic vs germline:** **Germline** (constitutional) in affected offspring; parental **germline or somatic mosaicism** documented (Finding 3).
- **Functional consequence:** **Dominant-negative** (misassembly + ER retention), NOT loss of function/haploinsufficiency.
- **Modifier genes:** None established. Severity appears driven chiefly by the specific mutation and mosaic dosage rather than trans-acting modifiers.
- **Epigenetics:** No disease-specific methylation/histone data reported.
- **Chromosomal abnormalities:** None; this is a single-nucleotide/small-indel disorder, not a structural/aneuploidy syndrome.

### 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors are known or expected. PLSD-T is a purely genetic, de-novo-dominant disorder (or inherited via parental mosaicism). Not applicable for toxins, radiation, diet, or infectious agents.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous C-propeptide mutation in *COL2A1*** (missense, last-exon nonsense, or frameshift) **produces an altered, stable pro-alpha-1(II) chain** (not a null allele; nonsense variants escape NMD). *[demonstrated — PMID 15643621]*
2. The altered C-propeptide **impairs correct chain selection, trimerization and assembly of the type II procollagen trimer** (dominant-negative poisoning of normal chains). *[demonstrated in Dmm mouse — PMID 18678883]*
3. Misassembled procollagen **cannot be secreted and is retained in the chondrocyte rough endoplasmic reticulum**, which becomes **abnormally distended/expanded**. *[demonstrated — PMID 21538020, 26545783]*
4. ER accumulation of misfolded protein **triggers the unfolded protein response / ER stress**, with **upregulation of Grp94 (HSP90B1) and Chop (DDIT3)**. *[demonstrated — PMID 21538020, 26545783]*
5. Sustained ER stress **leads to growth-plate chondrocyte apoptosis**. *[demonstrated — PMID 26545783]*
6. Chondrocyte death **plus a deficient/abnormal cartilage extracellular matrix** (thinner, sparser type II collagen fibrils; reduced aggrecan) **disrupts the cartilage growth plate and endochondral ossification**. *[demonstrated — PMID 18678883]*
7. Disrupted endochondral ossification **results in platyspondyly, micromelia, brachydactyly and metaphyseal dysplasia**, and a **small thorax**. *[demonstrated — PMID 15643621]*
8. The small thorax **causes pulmonary hypoplasia and respiratory failure → perinatal lethality**. *[inferred from phenotype; standard for lethal platyspondylic dysplasias]*

**Branch:** The severity of the chain depends on **mutant dosage** — full constitutional heterozygosity → lethal PLSD-T; **mosaicism** (lower effective mutant load) → milder, viable SPD. In mice, heterozygotes are mildly affected while homozygotes are lethal (semidominant), reinforcing dosage dependence.

**Supporting detail by category:**
- **Molecular pathways:** ER-stress / **unfolded protein response (UPR)** — PERK/ATF4–CHOP and GRP94 chaperone axis. Collagen biosynthesis/secretion pathway (Reactome: Collagen biosynthesis and modifying enzymes, R-HSA-1650814; Collagen trimerization).
- **Cellular processes:** Protein misfolding, ER retention, UPR activation, **apoptosis** of growth-plate chondrocytes; impaired chondrocyte secretory function.
- **Protein dysfunction:** Dominant-negative misassembly of type II procollagen trimers; intracellular aggregation/retention.
- **Metabolic/biochemical:** Reduced secreted type II collagen and aggrecan; defective cartilage matrix composition.
- **Immune involvement:** None (non-immune disorder).
- **Tissue damage:** ER-stress-driven apoptotic loss of chondrocytes in growth plate.
- **GO terms:** GO:0030199 (collagen fibril organization); GO:0006986 (response to unfolded protein); GO:0034976 (response to ER stress); GO:0036503 (ERAD pathway); GO:0006915 (apoptotic process); GO:0001958 (endochondral ossification).
- **CL terms:** CL:0000138 (chondrocyte); CL:0000057 (fibroblast, for cDNA studies).

### 7. Anatomical Structures Affected

- **Organ/system level:** **Skeletal system** is primarily affected — the **axial skeleton (vertebrae/spine)** and **appendicular skeleton (long bones, hands/feet)**. Secondary: **respiratory system** (hypoplastic lungs due to small thorax).
- **Tissue level:** **Cartilage / connective tissue** — specifically the **cartilage growth plate** and developing **vertebral bodies**; nucleus pulposus and, in milder/viable type II collagenopathies, the vitreous body are type II collagen–containing tissues.
- **Cell level:** **Growth-plate chondrocytes** (CL:0000138) are the primary affected cell population.
- **Subcellular level:** **Rough endoplasmic reticulum** (GO:0005791; GO:0005788 ER lumen) is the key compartment (distended, retains misfolded procollagen); the secretory pathway broadly.
- **UBERON terms:** UBERON:0002481 (bone tissue); UBERON:0001474 (bone element); UBERON:0001075 (vertebral column/axial skeleton); UBERON:0002515 (growth plate / cartilage growth plate); UBERON:0001091 (cartilage); UBERON:0002228 (rib cage/thorax); UBERON:0002048 (lung).
- **Lateralization:** **Bilateral and symmetric** (generalized skeletal dysplasia).

### 8. Temporal Development

- **Onset:** **Congenital / prenatal**; typically detected on second-trimester prenatal ultrasound (short, bowed long bones; narrow thorax; platyspondyly) or at birth.
- **Onset pattern:** Congenital, non-acute (developmental).
- **Progression:** The lethal form is **non-progressive in the usual sense** because death occurs perinatally. In rare survivors and the milder SPD end, disproportionate short stature and skeletal/spinal complications persist lifelong; early-onset spondyloarthropathy/osteoarthritis is seen in milder allelic conditions.
- **Disease course:** Self-limited by perinatal lethality in classic PLSD-T; chronic lifelong in survivors/SPD.
- **Critical period:** The vulnerable window is fetal/early neonatal (endochondral ossification and lung development). No intervention window currently alters the course.

### 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant**; the vast majority are **de novo** heterozygous mutations. Apparent recessive-like sibling recurrence is explained by **parental germline/somatic mosaicism** (Finding 3).
- **Penetrance:** **Complete** for the constitutional heterozygous (non-mosaic) state.
- **Expressivity:** Variable along the **PLSD-T ↔ SPD spectrum**, driven largely by mutation identity and mosaic dosage.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Mosaicism:** Documented germline and somatic mosaicism (PMID 22711552, 22495950).
- **Founder effects / consanguinity:** None established; consanguinity is not relevant to a dominant-negative de novo disorder (note: rare *recessive* COL2A1 disorders exist but are distinct from PLSD-T).
- **Carrier frequency:** Not applicable (dominant, de novo).
- **Epidemiology:** **Very rare** — exact prevalence/incidence not established; reported as isolated cases and small series worldwide (Zankl et al. assembled ~10 cases). No ethnic predilection; essentially sporadic global distribution.
- **Sex ratio:** No strong sex bias reported (autosomal).

### 10. Diagnostics

- **Imaging (primary diagnostic modality):** **Radiographs** show severe **platyspondyly**, **micromelia**, **brachydactyly**, and characteristic **metaphyseal changes**; **prenatal ultrasound** detects short/bowed long bones and narrow thorax. The radiographic pattern (metaphyseal changes + brachydactyly) distinguishes PLSD-T from other platyspondylic lethal dysplasias (e.g., thanatophoric dysplasia) and from helical-domain type II collagenopathies.
- **Genetic testing (confirmatory):** **Single-gene *COL2A1* sequencing** (targeting the C-propeptide-encoding exons) or **skeletal dysplasia gene panels**; **WES/WGS** are effective and increasingly first-line for undiagnosed lethal dysplasias. **Chromosomal microarray/karyotype/FISH are not informative** (no copy-number/structural lesion). Test for **parental mosaicism** when recurrence-risk counseling is needed.
- **Histopathology:** Growth-plate examination shows disorganized chondrocytes with **distended rough ER** and abnormal matrix (as modeled in mice).
- **Biomarkers / labs:** No specific blood/urine biomarker; diagnosis is radiographic + molecular.
- **Clinical criteria / differential diagnosis:** Differentials include **thanatophoric dysplasia** (FGFR3), **achondrogenesis type II / hypochondrogenesis** (helical-domain COL2A1), **fibrochondrogenesis**, and **spondyloperipheral dysplasia** (allelic, milder). C-propeptide localization of the mutation is the molecular distinguisher.
- **Screening:** No population newborn screening. **Prenatal ultrasound** and, in families with a known mutation or documented parental mosaicism, **targeted prenatal molecular testing / preimplantation genetic testing** apply.

### 11. Outcome/Prognosis

- **Survival/mortality:** Generally **perinatally lethal** (stillbirth or neonatal death from pulmonary hypoplasia/respiratory failure); **a few long-term survivors reported** (PMID 15643621).
- **Life expectancy:** Days or less for classic cases; indefinite but with severe disability for rare survivors / SPD.
- **Morbidity (survivors/SPD):** Profound disproportionate short stature, spinal deformity, restrictive respiratory disease, and orthopedic complications; early spondyloarthropathy at the mild allelic end.
- **Complications:** Respiratory failure (primary), spinal cord/foramen magnum compression risk, feeding difficulties.
- **Prognostic factors:** **Degree of thoracic hypoplasia** and **mutation dosage/mosaic status** are the main determinants; mosaicism predicts the milder (viable) SPD outcome.

### 12. Treatment

- **No disease-modifying therapy exists.** Management is **supportive/palliative**.
- **Perinatal/neonatal care:** Palliative or intensive respiratory support depending on severity and family wishes; most cases are not survivable.
- **Survivors/SPD:** Multidisciplinary skeletal-dysplasia care — respiratory support, orthopedic/spine management, hearing/vision surveillance (type II collagen tissues), physical/occupational therapy, pain management.
- **Advanced/experimental therapeutics:** None approved. Conceptually, the ER-stress mechanism (Findings 2, 4) suggests **UPR-modulating or allele-specific/ASO knockdown strategies** as theoretical future targets, but none are in clinical use.
- **Pharmacogenomics / targeted / cell / gene therapy / immunotherapy:** Not applicable at present.
- **NCIT suggestions:** NCIT:C15277 (Supportive Care); NCIT:C15431 (Palliative Care); NCIT:C15329 (Physical Therapy); NCIT:C15215 (Respiratory Therapy).

### 13. Prevention

- **Primary prevention:** Not possible for de novo mutations. Where parental mosaicism is known, **reproductive options** (PGT, prenatal diagnosis, gamete donation) reduce recurrence.
- **Secondary prevention / early detection:** **Prenatal ultrasound** screening; targeted prenatal molecular testing in at-risk pregnancies.
- **Genetic counseling (central):** Counsel that most cases are de novo with low recurrence, but **germline/somatic mosaicism confers a non-negligible recurrence risk** and can manifest as mild parental SPD (PMID 22711552, 22495950, 21356074). Counseling also addresses pregnancy-associated and newborn risks when a mosaic parent is affected.
- **Immunization / public health / environmental measures:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *COL2A1* is highly conserved. Mouse *Col2a1* (NCBI Gene 12824; *Mus musculus*, NCBI:txid10090) is the key ortholog used for modeling.
- **Natural animal disease:** The mouse **disproportionate micromelia (*Dmm*)** allele is a naturally arising *Col2a1* C-propeptide mutation causing a dysplasia analogous to human C-propeptide collagenopathy (PMID 18678883). No well-characterized naturally occurring companion-animal homolog of PLSD-T specifically is established in OMIA.
- **Comparative biology / conservation:** The ER-stress/misassembly mechanism is evolutionarily conserved — mouse C-propeptide mutants reproduce the human disease and its UPR/apoptosis mechanism, confirming conserved pathophysiology.

### 15. Model Organisms

| Model | Allele / type | Zygosity → phenotype | Key features | PMID |
|---|---|---|---|---|
| Mouse (ENU) | *Col2a1* **p.D1469A** (missense, C-propeptide) | Semidominant; het = mild, hom = lethal | Disrupted secretion, distended rough ER, ↑*Grp94*/*Chop* | [21538020](https://pubmed.ncbi.nlm.nih.gov/21538020/) |
| Mouse (ENU) | *Col2a1* **p.Y1391S** (missense, C-propeptide) | Semidominant; hom = lethal dysplasia | ER expansion, ER-stress genes up, **severe growth-plate apoptosis** | [26545783](https://pubmed.ncbi.nlm.nih.gov/26545783/) |
| Mouse (classic) | **disproportionate micromelia (*Dmm*)** C-propeptide allele | Semidominant; het = dwarfism, hom = lethal | Impaired procollagen trimer assembly/secretion; thin, sparse fibrils; ↓aggrecan | [18678883](https://pubmed.ncbi.nlm.nih.gov/18678883/) |

- **Model type:** Mammalian (mouse); genetic (ENU-induced and spontaneous point mutations); humanized-residue correspondence (D1469A, Y1391S match human PLSD-T residues).
- **Phenotype recapitulation:** Excellent — homozygotes reproduce lethal micromelia, spondylar/pelvic dysplasia, brachydactyly, and the ER-stress/apoptosis mechanism; heterozygotes model milder/dosage-reduced disease (parallel to human mosaic SPD).
- **Limitations:** Mouse homozygosity is required for the full lethal phenotype (humans are heterozygous, dominant-negative), reflecting species differences in dosage sensitivity; models capture mechanism well but are not perfect genotype matches.
- **Resources:** MGI (*Col2a1*, *Dmm* allele); IMPC; published ENU lines.

---

## Mechanistic Model / Interpretation

```
 Heterozygous C-propeptide COL2A1 mutation (missense / last-exon nonsense / frameshift)
                 │   (stable altered pro-α1(II) chain; escapes NMD)
                 ▼
 Impaired chain selection & trimerization of type II procollagen  ◄── dominant-negative
                 │
                 ▼
 Misassembled procollagen NOT secreted → retained in rough ER (distended/expanded)
                 │
                 ▼
 ER stress / Unfolded Protein Response  (↑GRP94/HSP90B1, ↑CHOP/DDIT3)
                 │
                 ▼
 Growth-plate CHONDROCYTE APOPTOSIS  +  deficient cartilage matrix (↓type II fibrils, ↓aggrecan)
                 │
                 ▼
 Disrupted cartilage growth plate & endochondral ossification
                 │
     ┌───────────┴───────────────────────────┐
     ▼                                         ▼
 Platyspondyly, micromelia,              Small thorax → pulmonary hypoplasia
 brachydactyly, metaphyseal dysplasia           │
                                                 ▼
                                    Respiratory failure → perinatal lethality

 DOSAGE BRANCH:  full heterozygous load → lethal PLSD-T
                 mosaic (reduced load)  → viable, milder Spondyloperipheral Dysplasia (SPD)
```

The model is notable for being **mechanistically closed** from genotype to phenotype and corroborated in three independent animal models. The central, actionable insight is that PLSD-T is an **ER-storage/UPR-driven apoptotic chondrodysplasia**, placing it mechanistically alongside other collagenopathies and metaphyseal dysplasias where misfolded matrix protein triggers chondrocyte ER stress — and distinguishing it from haploinsufficiency-based skeletal disorders.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [15643621](https://pubmed.ncbi.nlm.nih.gov/15643621/) | *Dominant negative C-propeptide COL2A1 mutations cause PLSD-T; novel type 2 collagenopathy subfamily* | Human genetic (case series) | Findings 1, 5 (genotype, phenotype definition) |
| [26545783](https://pubmed.ncbi.nlm.nih.gov/26545783/) | *ER stress-mediated apoptosis in a Col2a1 mutant mouse resembling PLSD-T* | Mouse model | Findings 2, 4 (ER stress, apoptosis) |
| [21538020](https://pubmed.ncbi.nlm.nih.gov/21538020/) | *ENU missense in Col2a1 C-propeptide creates a mouse model of PLSD-T* | Mouse model | Findings 2, 4 (ER retention, UPR, semidominance) |
| [18678883](https://pubmed.ncbi.nlm.nih.gov/18678883/) | *Heterozygous disproportionate micromelia (dmm) mouse* | Mouse model | Finding 4 (procollagen assembly/secretion defect, dosage) |
| [22711552](https://pubmed.ncbi.nlm.nih.gov/22711552/) | *PLSD-T in two sibs from normal parents (germline mosaicism)* | Human genetic | Finding 3 (germline mosaicism) |
| [22495950](https://pubmed.ncbi.nlm.nih.gov/22495950/) | *SPD as mosaic form of PLSD-T in mother and fetus* | Human genetic | Finding 3 (somatic mosaicism; PLSD-T↔SPD spectrum) |
| [17726487](https://pubmed.ncbi.nlm.nih.gov/17726487/) | *Czech dysplasia; Y1391C in SPD* | Human genetic | Supports PLSD-T↔SPD continuum (Y1391C in both) |
| [21356074](https://pubmed.ncbi.nlm.nih.gov/21356074/) | *Prenatal management of SPD with C-propeptide mutation* | Human clinical | Genotype–phenotype (SPD–Torrance spectrum); counseling |
| [8723097](https://pubmed.ncbi.nlm.nih.gov/8723097/) | *COL2A1 mutation presenting as spondyloperipheral dysplasia* | Human genetic | C-terminal (C-propeptide) frameshift → SPD spectrum |
| [8157027](https://pubmed.ncbi.nlm.nih.gov/8157027/) | *The type II collagenopathies: a spectrum* | Review | Places PLSD-T in the type II collagenopathy family |
| [31755234](https://pubmed.ncbi.nlm.nih.gov/31755234/), [32896647](https://pubmed.ncbi.nlm.nih.gov/32896647/) | *Biallelic/recessive COL2A1 disorders* | Human genetic | Contrast: distinct recessive type II collagenopathies (NOT PLSD-T) |

All findings are convergent; no paper in the reviewed set contradicts the core mechanism. The recessive-COL2A1 papers are included to **delimit** PLSD-T (dominant, C-propeptide, dominant-negative) from mechanistically distinct recessive type II collagenopathies.

---

## Limitations and Knowledge Gaps

1. **Epidemiology is unquantified.** No reliable prevalence/incidence figures exist; the literature is limited to isolated cases and a ~10-case series. Sex ratio and any population differences are undetermined.
2. **Small human N.** Genotype–phenotype correlations (including the PLSD-T↔SPD boundary) rest on a handful of patients; the precise determinants of lethal vs. viable outcome beyond mosaic dosage are not fully resolved.
3. **Mechanism confirmed mainly in mouse.** The ER-stress/apoptosis causal chain is directly shown in mouse models; human chondrocyte in-vivo confirmation is limited to histopathology, and the final step (thorax → pulmonary hypoplasia → death) is inferred rather than experimentally dissected.
4. **No molecular profiling (omics) data** specific to human PLSD-T chondrocytes (transcriptomics/proteomics/single-cell) were identified.
5. **No therapeutics.** UPR-modulating or allele-specific strategies are only conceptual; no preclinical efficacy data exist for PLSD-T.
6. **Modifier genes and epigenetics** are essentially unexplored.

## Proposed Follow-up Experiments / Actions

1. **Single-cell/spatial transcriptomics of growth plates** from the D1469A/Y1391S mouse models to map the UPR→apoptosis trajectory at cell-type resolution (GEO deposition).
2. **Preclinical UPR-modulation trials** (e.g., chemical chaperones such as 4-PBA/TUDCA, or genetic CHOP/DDIT3 knockdown) in the established mouse models to test whether dampening ER stress rescues growth-plate apoptosis and skeletal phenotype.
3. **Allele-selective silencing (ASO/siRNA)** proof-of-concept targeting the mutant *COL2A1* transcript in patient-derived or knock-in chondrocytes/iPSC-chondroid organoids.
4. **International PLSD-T/SPD registry** to quantify prevalence, natural history of survivors, mosaicism-associated recurrence risk, and genotype–phenotype boundaries.
5. **Deep phenotyping of parental mosaicism** (sensitive sequencing of multiple parental tissues/gametes) to refine recurrence-risk counseling.
6. **Structural/biophysical study** (UniProt P02458 C-propeptide; AlphaFold + experimental PDB) of how specific residue substitutions impair trimer nucleation, to build a predictive severity model.

---

*Report compiled from 5 iterations of autonomous investigation; 5 confirmed findings; 13 papers reviewed. Causal gene named in first paragraph: **COL2A1**.*


## Artifacts

- [OpenScientist final report](Platyspondylic_Dysplasia_Torrance_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Platyspondylic_Dysplasia_Torrance_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 12 |
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
| Terms named correctly | 10 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000926` (1 mention) - the report calls it "Radiographic sign"; HP calls it **Platyspondyly**
- `HP:0001156` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Brachydactyly**
- `HP:0000944` (1 mention) - the report calls it "Radiographic sign"; HP calls it **Abnormal metaphysis morphology**
- `HP:0002089` (1 mention) - the report calls it "Clinical/pathologic"; HP calls it **Pulmonary hypoplasia**
- `HP:0004322` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Short stature**
- `HP:0000256` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Macrocephaly**
- `CL:0000138` (2 mentions) - the report calls it "chondrocyte", "Growth-plate chondrocytes", "Cell level:** **Growth-plate chondrocytes"; CL calls it **chondrocyte**
- `UBERON:0002515` (1 mention) - the report calls it "growth plate / cartilage growth plate"; UBERON calls it **periosteum**
- `UBERON:0001091` (1 mention) - the report calls it "cartilage"; UBERON calls it **calcareous tooth**
- `UBERON:0002228` (1 mention) - the report calls it "rib cage/thorax"; UBERON calls it **rib**
- `NCIT:C15277` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Mastectomy**
- `NCIT:C15431` (1 mention) - the report calls it "Palliative Care"; NCIT calls it **Hematopoietic Cell Transplantation**
- `NCIT:C15329` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Surgical Procedure**
- `NCIT:C15215` (1 mention) - the report calls it "Respiratory Therapy"; NCIT calls it **Cryosurgery**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0034976` (1 mention) - the report calls it "response to ER stress"; GO calls it **response to endoplasmic reticulum stress**, and lists "response to ER stress" among its other names
- `CL:0000057` (1 mention) - the report calls it "fibroblast, for cDNA studies"; CL calls it **fibroblast**
- `UBERON:0001075` (1 mention) - the report calls it "vertebral column/axial skeleton"; UBERON calls it **bony vertebral centrum**, and lists "vertebral centra" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000138` - called "chondrocyte", "Growth-plate chondrocytes", "Cell level:** **Growth-plate chondrocytes"