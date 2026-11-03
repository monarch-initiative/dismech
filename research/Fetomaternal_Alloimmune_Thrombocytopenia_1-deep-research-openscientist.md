---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T23:25:24.406315'
end_time: '2026-10-15T23:50:28.207510'
duration_seconds: 1503.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Fetomaternal Alloimmune Thrombocytopenia 1
  mondo_id: MONDO:0980723
  category: Complex
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
citation_count: 37
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 37
  on_topic: 32
  validator_version: 0.3.0
term_validation:
  total_terms: 24
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 0
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0002170
    reported_labels:
    - Clinical sign
    ontology_label: Intracranial hemorrhage
  - term_id: HP:0001518
    reported_labels:
    - Clinical sign
    ontology_label: Small for gestational age
  - term_id: HP:0001873
    reported_labels:
    - Lab abnormality
    ontology_label: Thrombocytopenia
  - term_id: HP:0000967
    reported_labels:
    - Physical sign
    ontology_label: Petechiae
  - term_id: HP:0000505
    reported_labels:
    - Sign
    ontology_label: Visual impairment
  - term_id: HP:0012758
    reported_labels:
    - Sign
    ontology_label: Neurodevelopmental delay
  - term_id: UBERON:0000178
    reported_labels:
    - Primary:** blood/platelets
    ontology_label: blood
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Fetomaternal_Alloimmune_Thrombocytopenia_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Fetomaternal_Alloimmune_Thrombocytopenia_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fetomaternal Alloimmune Thrombocytopenia 1
- **MONDO ID:** MONDO:0980723 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Fetomaternal Alloimmune Thrombocytopenia 1** covering all of the
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

# Fetomaternal Alloimmune Thrombocytopenia 1 (FNAIT): A Comprehensive Disease Characterization

**Disease:** Fetomaternal / Fetal-Neonatal Alloimmune Thrombocytopenia 1 (FNAIT, FMAIT, NAIT)
**MONDO ID:** MONDO:0980723
**Category:** Complex (immunogenetic, alloimmune disorder of pregnancy)
**Report date:** 2026-10-15

---

## Summary

Fetomaternal alloimmune thrombocytopenia 1 (FNAIT) is the platelet equivalent of hemolytic disease of the fetus and newborn. It arises when a pregnant woman who lacks a specific human platelet antigen (HPA)—most commonly **HPA-1a**, defined by the **Leu33Pro** polymorphism of **β3 integrin / glycoprotein IIIa (gene *ITGB3*)**—becomes alloimmunized against the paternally inherited antigen expressed on fetal platelets. The resulting maternal IgG alloantibodies cross the placenta and mediate **FcγRIII-dependent destruction of fetal platelets**, with additional suppression of fetal megakaryopoiesis. Clinically apparent immunization occurs almost exclusively in **HPA-1a-negative (HPA-1bb) women carrying HLA-DRB3\*01:01**, establishing the immunogenetic basis of the disorder.

The most feared complication is **intracranial hemorrhage (ICH)**, which occurs in ~10–20% of symptomatic anti-HPA-1a cases, frequently in utero before 28 weeks' gestation. A key mechanistic insight from this investigation is that ICH is **not driven by thrombocytopenia alone** but by anti-β3 antibody impairment of **fetal angiogenesis and endothelial integrity**—a vasculopathic branch demonstrated in murine models and human endothelial assays and reversible by maternal IVIG. A parallel **placental branch** involves chronic histiocytic intervillositis, complement (C4d) deposition, and uterine NK-cell-mediated trophoblast apoptosis, linking FNAIT to intrauterine growth restriction (IUGR) and miscarriage. Disease severity is further modulated by **reduced Fc core fucosylation** of anti-HPA-1a IgG1, which enhances FcγRIIIa/b binding and predicts bleeding severity.

FNAIT-related ICH carries a grave prognosis (~48% perinatal mortality; ~80% death-or-severe-neurodevelopmental impairment), but **antenatal weekly IVIG ± prednisone** is highly effective at preventing ICH and restoring near-normal neurodevelopment. Emerging therapies include the **FcRn blocker nipocalimab** (phase 3 FREESIA trials) and the **anti-HPA-1a prophylactic monoclonal RLYB212** (a "platelet RhoGAM"). FNAIT remains underdiagnosed and is effectively a diagnosis of exclusion, confirmed by parental/neonatal HPA genotyping plus maternal anti-HPA antibody testing. This report synthesizes nine confirmed findings across all 15 template sections, drawn from 43 reviewed papers.

---

## Key Findings

### Finding 1 — Immunogenetic cause: maternal anti-HPA-1a alloantibodies against the Leu33Pro (ITGB3) epitope, restricted by HLA-DRB3\*01:01

FNAIT is most commonly caused by maternal IgG alloantibodies directed against **HPA-1a**, the allelic product of the **Leu33Pro** polymorphism in platelet glycoprotein IIIa (**β3 integrin, *ITGB3***). The immune response is tightly restricted by the maternal HLA class II allele **HLA-DRB3\*01:01**: clinically apparent immunization occurs almost exclusively in HPA-1a-negative (HPA-1bb) women who also carry this allele. In the Polish PREVFNAIT prospective screening of 24,236 pregnant women, 2.4% were HPA-1a-negative, consistent with the ~2.3% frequency seen across Caucasian populations.

As stated in a 2025 management update, *"immunization usually occurs in the first pregnancy of an HLA-DRB3\*01:01-positive, HPA-1a-negative woman"* ([PMID: 41089465](https://pubmed.ncbi.nlm.nih.gov/41089465/)). Anti-HPA-1a is *"the most frequent cause of FNAIT in Caucasians"* ([PMID: 26564154](https://pubmed.ncbi.nlm.nih.gov/26564154/)), and the target epitope maps to the extracellular region of the β3 integrin: *"the immunoreactive epitopes in FNAITP are primarily located in the extracellular regions of the platelet glycoprotein IIIa (beta3 integrin)"* ([PMID: 16317099](https://pubmed.ncbi.nlm.nih.gov/16317099/)).

**Ontology anchors:** Gene *ITGB3* (HGNC:6156); protein target integrin β3/GPIIIa; MONDO:0980723.

### Finding 2 — Effector mechanism: FcγRIII-dependent platelet phagocytosis, modulated by IgG Fc glycosylation

Platelet destruction in FNAIT is driven predominantly by **FcγRIII-dependent phagocytosis**. Anti-HPA-1a antibodies from 9 of 10 FNAIT patients induced FcγR-dependent platelet phagocytosis in vitro, whereas complement fixation, platelet activation (CD62P/P-selectin), and desialylation occurred in only a minority of samples—establishing phagocytosis, not complement lysis or activation, as the dominant route of clearance. In a dual-humanized mouse model (APLDQ HPA-1a platelets crossed with human FcγR transgenic mice), an FcγRIII-blocking monovalent antibody significantly reduced platelet clearance.

The primary paper reports: *"Anti-HPA-1a antibodies in pooled plasma and in individual samples of 9 of 10 patients with FNAIT induced Fc gamma receptor (FcγR)-dependent platelet phagocytosis in vitro, indicating this as the major contributor to platelet destruction"* and *"pretreatment with an FcγRIII-blocking monovalent antibody significantly reduced clearance, confirming FcγRIII's central role in mediating platelet destruction"* ([PMID: 42269082](https://pubmed.ncbi.nlm.nih.gov/42269082/)). Effector strength is tuned by Fc glycosylation: *"particularly decreased Fc fucosylation enhancing Fc gamma receptor-mediated effector functions, more accurately determine disease severity"* ([PMID: 41779743](https://pubmed.ncbi.nlm.nih.gov/41779743/)). Maternal sera additionally suppress fetal megakaryopoiesis, reducing platelet production ([PMID: 26209661](https://pubmed.ncbi.nlm.nih.gov/26209661/)).

**Ontology anchors:** GO:0006911 phagocytosis; CL:0000235 macrophage (splenic effector); FCGR3A (FcγRIIIa).

### Finding 3 — Intracranial hemorrhage is driven by anti-β3 impairment of angiogenesis, not thrombocytopenia alone

A pivotal mechanistic finding is that FNAIT-associated ICH results from a **vasculopathic branch** distinct from platelet count. In murine FNAIT models imaged with high-frequency ultrasound, **ICH occurred only with anti-β3 integrin-mediated FNAIT, not anti-GPIbα-mediated FNAIT, despite similar degrees of thrombocytopenia in both groups.** Anti-β3 antibodies reduced brain and retina vessel density, impaired angiogenic (AKT) signaling, and increased endothelial cell apoptosis. Critically, all of these effects were abrogated by maternal IVIG. Human anti-HPA-1a IgG from FNAIT mothers inhibited endothelial proliferation, network formation, and AKT phosphorylation in vitro.

The landmark study states: *"ICH only occurred in fetuses and neonates with anti-β3 integrin-mediated, but not anti-GPIbα-mediated, FNAIT, despite similar thrombocytopenia in both groups. Only anti-β3 integrin-mediated FNAIT reduced brain and retina vessel density, impaired angiogenic signaling, and increased endothelial cell apoptosis, all of which were abrogated by maternal administration of intravenous immunoglobulin (IVIG)"* ([PMID: 25774504](https://pubmed.ncbi.nlm.nih.gov/25774504/)). Clinically, ICH occurs *"in 10% to 20% of fetuses/newborns"* with anti-HPA-1a FNAIT ([PMID: 41779743](https://pubmed.ncbi.nlm.nih.gov/41779743/)), usually in utero before week 28. This reframing—endothelial dysfunction rather than thrombocytopenia as the proximate cause of hemorrhage—is echoed in the fetal-stroke literature ([PMID: 30467085](https://pubmed.ncbi.nlm.nih.gov/30467085/)).

**Ontology anchors:** HP:0002170 intracranial hemorrhage; GO:0001525 angiogenesis; GO:0043066 negative regulation of apoptotic process; CL:0000115 endothelial cell; UBERON:0000955 brain; UBERON:0000966 retina.

### Finding 4 — Epidemiology: ~2.4% HPA-1a-negative, ~9% alloimmunize, minority clinically affected

FNAIT incidence is approximately **1 in 1,000 to 1 in 2,000 live births**. In the PREVFNAIT cohort of 24,236 screened women, 2.4% were HPA-1a-negative; anti-HPA-1a antibodies developed in **48/529 (9.1%)** of HPA-1a-negative women, and FNAIT was diagnosed in roughly a third of neonates born to alloimmunized pregnancies. In the United States, NAIT incidence is cited as ~1/1,000 live births, and it is the most common cause of severe thrombocytopenia (<30×10⁹/L) and ICH in otherwise healthy term newborns. Severe neonatal thrombocytopenia shows a male predominance (241/379, 64% male in a large registry).

Supporting quotes: *"Among 583/24,236 (2.4%) HPA-1a-negative women, samples were obtained from 529, of which 513 were examined during pregnancy. Anti-HPA-1a antibodies were detected in 48/529 (9.1%) women"* ([PMID: 41542834](https://pubmed.ncbi.nlm.nih.gov/41542834/)); *"Fetal/neonatal alloimmune thrombocytopenia (FNAIT) is a relatively rare condition (1/1000-1/2000)"* ([PMID: 26564154](https://pubmed.ncbi.nlm.nih.gov/26564154/)); and *"The incidence of NAIT is 1 in every 1000 live births within the United States; it is the most common cause of severe thrombocytopenia (<30 × 10⁹/L) and intracranial hemorrhage in term newborns"* ([PMID: 32657948](https://pubmed.ncbi.nlm.nih.gov/32657948/)). A Norwegian natural-history cohort estimated major clinically detectable bleeding without intervention at ~11 per 10,000 HPA-1a-negative pregnancies, with 90% of immunized women HLA-DRB3\*01:01-positive ([PMID: 38407610](https://pubmed.ncbi.nlm.nih.gov/38407610/)).

### Finding 5 — Management and prevention: antenatal IVIG ± prednisone standard; FcRn blockade and anti-HPA-1a prophylaxis emerging

Standard antenatal management is **weekly intravenous immunoglobulin (IVIG), commonly 1 g/kg/week, with or without prednisone**, which prevents severe fetal thrombocytopenia and secondary ICH and is highly effective though costly and associated with maternal side effects. Fetal blood sampling and intrauterine platelet transfusion are now generally avoided due to procedural risk. Two emerging therapeutic classes are in advanced development:

- **Nipocalimab**, a neonatal Fc receptor (FcRn) blocker that *"inhibits transplacental transfer of maternal immunoglobulin G (IgG) and lowers circulating maternal IgG levels"* ([PMID: 40720970](https://pubmed.ncbi.nlm.nih.gov/40720970/)), is in phase 3 trials (FREESIA-1 placebo-controlled; FREESIA-3 comparing nipocalimab 45 mg/kg weekly vs IVIG + prednisone, [PMID: 41290206](https://pubmed.ncbi.nlm.nih.gov/41290206/)).
- **RLYB212**, a monoclonal anti-HPA-1a antibody for prophylaxis (the platelet analogue of anti-D RhoGAM), eliminated HPA-1a-positive platelets in a phase 1b antigen-challenge model simulating a 30 mL fetomaternal hemorrhage: *"RLYB212, a monoclonal anti-HPA-1a antibody, to eliminate HPA-1a-positive platelets in an antigen challenge model of a 30 mL fetal-maternal hemorrhage"* ([PMID: 39168139](https://pubmed.ncbi.nlm.nih.gov/39168139/)).

The standard-of-care foundation is documented: *"antenatal administration of intravenous immune globulin and prednisone to the pregnant woman to prevent the development of severe fetal thrombocytopenia and secondary intracranial hemorrhage in utero. That therapy has proven to be highly effective"* ([PMID: 33839095](https://pubmed.ncbi.nlm.nih.gov/33839095/)). Neonatal management relies on HPA-matched (or random-donor) platelet transfusions plus IVIG; HPA-matched transfusions produce larger platelet increments ([PMID: 36108655](https://pubmed.ncbi.nlm.nih.gov/36108655/)).

**Ontology anchors:** NCIT immunoglobulin therapy; NCIT prednisone; FcRn (FCGRT) blockade.

### Finding 6 — Reduced IgG1-Fc core fucosylation of anti-HPA-1a enhances FcγRIIIa/b binding and predicts bleeding severity

A central severity modifier is the **glycosylation state of the anti-HPA-1a IgG1 Fc tail**. Mass spectrometry shows markedly decreased core fucosylation at Asn297 of anti-HPA-1a-specific IgG1 (not observed in total serum IgG1). Low-fucose antibodies bind FcγRIIIa and FcγRIIIb with higher affinity and enhance platelet phagocytosis by FcγRIII-bearing effectors. Fucosylation level correlates positively with neonatal platelet count and negatively with disease severity.

Primary evidence: *"We found markedly decreased levels of core fucosylation of anti-HPA-1a-specific IgG1 from FNAIT patients (n = 48), but not in total serum IgG1. Antibodies with a low amount of fucose displayed higher binding affinity to FcγRIIIa and FcγRIIIb"* and *"the degree of anti-HPA-1a fucosylation correlated positively with the neonatal platelet counts in FNAIT, and negatively to the clinical disease severity"* ([PMID: 24243971](https://pubmed.ncbi.nlm.nih.gov/24243971/)). In a larger series, *"anti-HPA-1a -fucosylation (P = 0·006) combined with galactosylation (P = 0·021) and antibody level (P = 0·038) correlated with bleeding severity"*, and the glycosylation pattern is stable across pregnancies ([PMID: 27017954](https://pubmed.ncbi.nlm.nih.gov/27017954/)). A cellular surface plasmon resonance imaging (cSPRi) assay has been validated against mass spectrometry (n=143) to operationalize this for diagnostics ([PMID: 37868955](https://pubmed.ncbi.nlm.nih.gov/37868955/)).

### Finding 7 — Placental branch: chronic histiocytic intervillositis, complement C4d deposition, and uNK-mediated trophoblast apoptosis drive IUGR and miscarriage

Beyond platelet clearance, HPA-1a is expressed on placental (syncytiotrophoblast) tissue, creating a **placental disease branch**. A systematic placental study found **chronic histiocytic intervillositis in 40.7% of HPA-1a-alloimmunized placentas vs 0% of controls (p = 0.001)**, a lesion not prevented by IVIg. Newly diagnosed FNAIT placentas showed increased complement C4d deposition (10/14 samples) versus IVIg-treated cases (2/21). Untreated NAIT also shows a lymphoplasmacytic chronic villitis that is alleviated by IVIG (p = 0.005). In murine FNAIT, maternal anti-platelet responses recruit uterine NK (uNK) cells (elevated NKp46, CD107, perforin), causing trophoblast apoptosis, impaired spiral-artery remodeling, miscarriage, and IUGR; NK depletion or blockade of NKp46/FcγRIIIa rescues pregnancy loss.

Supporting quotes: *"Chronic histiocytic intervillositis was observed in 40.7% of placentas from HPA-1a alloimmunized pregnancies, compared to none in the control group (p = 0.001)"* ([PMID: 34329972](https://pubmed.ncbi.nlm.nih.gov/34329972/)); *"Uterine natural killer (uNK) cell recruitment and survival beyond mid-gestation lead to elevated NKp46 and CD107 expression, perforin release and trophoblast apoptosis. Depletion of NK cells restores normal spiral artery remodeling and placental function, prevents miscarriage, and rescues hemorrhage in neonates"* ([PMID: 28794456](https://pubmed.ncbi.nlm.nih.gov/28794456/)); and *"A higher degree of C4d deposition was present in the newly diagnosed FNAIT cases (10/14 samples), as compared to the IVIg-treated FNAIT cases (2/21 samples)"* ([PMID: 34201864](https://pubmed.ncbi.nlm.nih.gov/34201864/)). An anti-angiogenic maternal profile (elevated sFlt-1, sFlt-1/PlGF ratio) is associated with adverse neonatal outcome ([PMID: 39486121](https://pubmed.ncbi.nlm.nih.gov/39486121/)), and untreated chronic villitis associates with severe early IUGR ([PMID: 16157119](https://pubmed.ncbi.nlm.nih.gov/16157119/)).

**Ontology anchors:** CL:0000623 natural killer cell; CL:0000351 trophoblast; UBERON:0001987 placenta; GO:0006956 complement activation, classical pathway; HP:0001518 small for gestational age.

### Finding 8 — Prognosis: FNAIT-related ICH carries ~48% perinatal mortality and ~80% death-or-severe-NDI; antenatal IVIG improves outcomes

FNAIT-related ICH is devastating. In a Leiden cohort of 21 ICH-due-to-FNAIT cases (1993–2015), **perinatal mortality was 10/21 (48%)**; among 10 surviving children assessed, severe neurodevelopmental impairment (NDI) was 6/10 (60%) and moderate NDI 1/10 (10%); the overall death-or-severe-NDI outcome was **16/20 (80%)**. Antenatal treatment dramatically changes this trajectory: in a 71-sibling-pair study, antenatally treated younger siblings had higher birth platelet counts, NO perinatal ICH (versus 12 ICH in untreated older siblings), and fewer vision problems. Long-term follow-up of antenatally treated children shows neurodevelopment comparable to the general population.

Supporting quotes: *"The perinatal mortality rate was 10/21 (48%)... Severe and moderate NDI were diagnosed in 6/10 (60%) and 1/10 (10%) of the surviving children. The overall adverse outcome, including perinatal mortality or severe NDI, was 16/20 (80%)"* ([PMID: 29730660](https://pubmed.ncbi.nlm.nih.gov/29730660/)); *"No treated child suffered a perinatal ICH compared with 12 untreated siblings. Treated siblings also had fewer vision problems (three versus 14 in the untreated group)"* ([PMID: 17094038](https://pubmed.ncbi.nlm.nih.gov/17094038/)); *"The general health and neurodevelopmental outcome in the children was comparable to a normal Dutch population"* ([PMID: 15363839](https://pubmed.ncbi.nlm.nih.gov/15363839/)). A 2022 Dutch cohort confirmed reassuring long-term neurodevelopment after antenatal IVIG, with mild-moderate NDI in 14% (6/41) and no severe NDI ([PMID: 35671780](https://pubmed.ncbi.nlm.nih.gov/35671780/)).

### Finding 9 — Diagnosis of exclusion: broad differential, underdiagnosed, confirmed by HPA genotyping plus antibody testing

FNAIT is *"the main cause of primary hemorrhagic morbidity and mortality in fetuses and newborns"* yet remains underdiagnosed, with no national screening program implemented and *"this potentially lethal disease is still underdiagnosed"* ([PMID: 31973628](https://pubmed.ncbi.nlm.nih.gov/31973628/)). Diagnosis is confirmed by molecular **HPA genotyping of parents and newborn plus maternal anti-HPA antibody testing**, which also detects non-HPA-1 incompatibilities such as **HPA-15** and **HPA-5b**. The neonatal thrombocytopenia differential is broad and must be excluded: maternal (autoimmune) immune thrombocytopenia (ITP), sepsis/DIC, congenital infections (TORCH; e.g., Coxsackievirus B3 mimicking NAIT, [PMID: 27250900](https://pubmed.ncbi.nlm.nih.gov/27250900/)), placental insufficiency, and inherited thrombocytopenias (Wiskott-Aldrich syndrome, pyruvate kinase deficiency).

FNAIT is distinguished by **isolated severe thrombocytopenia in an otherwise well term neonate** plus demonstrable maternal–fetal HPA incompatibility and maternal anti-HPA antibody. The HPA-15 case is documented: *"Patients 1 and 2 had severe thrombocytopenia due to incompatibility in HPA-1 and HPA-15, respectively"* ([PMID: 31973628](https://pubmed.ncbi.nlm.nih.gov/31973628/)). Reviews support the key ITP-versus-alloimmune distinction ([PMID: 34033425](https://pubmed.ncbi.nlm.nih.gov/34033425/)), and inherited causes such as Wiskott-Aldrich syndrome ([PMID: 26171707](https://pubmed.ncbi.nlm.nih.gov/26171707/)) and pyruvate kinase deficiency ([PMID: 37473739](https://pubmed.ncbi.nlm.nih.gov/37473739/)) illustrate the need for genetic workup when HPA testing is negative. NAIT-positive neonates have significantly lower platelet nadirs (25 vs 64 ×10⁹/L) and higher treatment requirements than NAIT-negative thrombocytopenia ([PMID: 37027241](https://pubmed.ncbi.nlm.nih.gov/37027241/)). Canadian reference-laboratory data confirm substantial under-identification nationally ([PMID: 41672591](https://pubmed.ncbi.nlm.nih.gov/41672591/)).

---

## Section-by-Section Characterization

### 1. Disease Information
FNAIT is an alloimmune disorder of pregnancy in which maternal IgG antibodies against paternally inherited fetal platelet antigens cross the placenta and destroy fetal/neonatal platelets, causing thrombocytopenia and, in severe cases, hemorrhage. **Key identifiers:** MONDO:0980723; MeSH "Thrombocytopenia, Neonatal Alloimmune"; ICD-10 P61.0 (transient neonatal thrombocytopenia). **Synonyms:** FNAIT, FMAIT, NAIT (neonatal alloimmune thrombocytopenia), fetomaternal alloimmune thrombocytopenia, fetal/neonatal alloimmune thrombocytopenia. Information is derived from **aggregated disease-level resources** (registries, cohorts, screening studies) plus individual clinical case series.

### 2. Etiology
**Primary cause:** maternal–fetal HPA incompatibility, most often HPA-1a (Leu33Pro of *ITGB3*). **Genetic risk factors:** maternal HPA-1bb genotype + **HLA-DRB3\*01:01** (strongest immune-response determinant; ~90% of immunized women). **Other antigens:** HPA-5b, HPA-15, and rarely others. **Environmental/obstetric risk:** fetomaternal hemorrhage exposing fetal platelets; notably, unlike RhD disease, immunization often occurs in the first pregnancy. **Protective factors:** HLA-DRB3\*01:01-negative status markedly reduces immunization risk; carrying an HPA-1a-negative fetus (15% of HPA-1a-negative women) removes risk. **Gene–environment interaction:** antigen exposure (fetomaternal hemorrhage) acts only in the permissive HLA-DRB3\*01:01 genetic context.

### 3. Phenotypes
| Phenotype | Type | HPO term | Onset | Severity/Frequency |
|---|---|---|---|---|
| Thrombocytopenia (isolated, severe) | Lab abnormality | HP:0001873 | Fetal/neonatal | Severe; defining feature |
| Intracranial hemorrhage | Clinical sign | HP:0002170 | Often in utero <28 wk | ~10–20% symptomatic; ~48% mortality |
| Petechiae/purpura | Physical sign | HP:0000967 | Neonatal | Common |
| Intrauterine growth restriction | Clinical sign | HP:0001518 | Fetal | Placental branch |
| Visual impairment (post-ICH) | Sign | HP:0000505 | Neonatal/infant | Sequela of ICH |
| Neurodevelopmental impairment | Sign | HP:0012758 | Infancy/childhood | Sequela of ICH |

Quality-of-life impact is concentrated in ICH survivors (cerebral palsy, cognitive/visual/hearing deficits); uncomplicated FNAIT typically resolves without lasting impact.

### 4. Genetic/Molecular Information
**Causal gene:** *ITGB3* (HGNC:6156; integrin β3/GPIIIa), OMIM *173470. **Key variant:** HPA-1a/1b = **Leu33Pro** (rs5918, c.176T>C). **HLA restriction:** DRB3\*01:01. Other antigens map to *ITGA2B* (HPA-3), *GP1BA* (HPA-2), *CD109* (HPA-15), *ITGA2* (HPA-5). The disease is **immunologically mediated, not a germline mutation of the fetus**; the "variant" is a common population polymorphism, and pathology arises from maternal–fetal antigen mismatch. **Functional consequence:** antibody opsonization → FcγRIII-mediated clearance + anti-angiogenic endothelial effect. **Fc glycosylation (afucosylation)** is a post-translational severity modifier.

### 5. Environmental Information
No classical toxins or infectious agents cause FNAIT. The relevant "environmental" trigger is **fetomaternal hemorrhage** exposing the maternal immune system to fetal HPA-1a platelets. Infectious agents (Coxsackievirus B3, TORCH) are relevant only as **mimics/differentials**, not causes.

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1. Maternal HPA-1a-negative genotype (ITGB3 Pro33/Pro33) + HLA-DRB3*01:01
      │  leads to
2. Fetomaternal hemorrhage exposes paternally-inherited HPA-1a fetal platelets
      │  results in
3. HLA-DRB3*01:01-restricted CD4+ T-cell help → maternal anti-HPA-1a IgG (often afucosylated)
      │  crosses placenta via FcRn
4. Maternal IgG binds fetal platelet / endothelial β3 integrin (GPIIIa)
      │  branches ↓
   ┌──────────────────────────────┬─────────────────────────────┬──────────────────────────────┐
5a. FcγRIII+ splenic macrophages   5b. Anti-β3 binds endothelial 5c. Anti-HPA-1a binds placental
    phagocytose opsonized          αvβ3 → impaired AKT             syncytiotrophoblast → C4d,
    platelets (+ suppressed        angiogenic signaling →          chronic histiocytic
    megakaryopoiesis)              ↑endothelial apoptosis,         intervillositis, uNK
      │ results in                 ↓brain/retina vessel density    recruitment → trophoblast
6a. Fetal/neonatal                   │ results in                  apoptosis
    THROMBOCYTOPENIA               6b. Vascular fragility →           │ results in
                                      INTRACRANIAL HEMORRHAGE      6c. Impaired spiral-artery
                                      (not count-dependent)          remodeling → IUGR / miscarriage
```

**Upstream vs downstream:** steps 1–4 are shared upstream; step 5 branches into platelet clearance (5a), vasculopathy (5b), and placental pathology (5c). Megakaryopoiesis suppression (maternal sera reduce megakaryocyte numbers via early apoptosis, [PMID: 26209661](https://pubmed.ncbi.nlm.nih.gov/26209661/)) compounds thrombocytopenia. The vasculopathic branch (5b→6b) is the key, under-appreciated driver of ICH and is inferred from murine + in vitro human endothelial data. **Pathways:** PI3K-AKT angiogenic signaling; FcγR signaling; classical complement (C4d). **Cell types:** platelet (CL:0000233), megakaryocyte (CL:0000556), macrophage (CL:0000235), endothelial cell (CL:0000115), NK cell (CL:0000623), trophoblast (CL:0000351).

### 7. Anatomical Structures Affected
- **Primary:** blood/platelets (UBERON:0000178), bone marrow megakaryocytes (UBERON:0002371).
- **Secondary:** brain (UBERON:0000955) and retina (UBERON:0000966) — ICH sites; placenta (UBERON:0001987); cerebral ventricles (periventricular/intraventricular hemorrhage).
- **Subcellular:** platelet/endothelial plasma membrane (GO:0005886; β3 integrin); IgG Fc N297 glycan.
- **Lateralization:** ICH may be focal/unilateral or bilateral; porencephaly/multicystic encephalomalacia can follow.

### 8. Temporal Development
**Onset:** congenital/fetal; thrombocytopenia and ICH frequently begin in utero, with ICH often before 28 weeks' gestation. **Course:** self-limited postnatally as maternal antibody clears over days–weeks (platelet count typically recovers within ~1–2 weeks), but ICH sequelae are permanent. **Critical window:** mid-to-late second and third trimester for antenatal IVIG; the therapeutic goal is to initiate treatment before the vulnerable period—earlier (≈12 wk) for high-risk pregnancies with prior ICH.

### 9. Inheritance and Population
Not Mendelian in the fetus; it is an **immunogenetic/multifactorial** condition requiring maternal HPA-1bb + HLA-DRB3\*01:01 and an HPA-1a-positive fetus. **Prevalence:** ~1/1,000–1/2,000 live births; HPA-1a-negative ~2.4% of Caucasian women; ~9% of these alloimmunize. **Population:** predominantly European/Caucasian ancestry (HPA-1a-negative frequency is lower in East Asian populations). **Sex ratio of affected neonates:** male predominance (~64%). Recurrence risk in subsequent HPA-incompatible pregnancies is high and often more severe—justifying antenatal prophylaxis.

### 10. Diagnostics
- **Laboratory:** maternal **anti-HPA antibody** screening (MAIPA/bead assays); **HPA genotyping** of mother, father, and neonate; neonatal CBC showing isolated severe thrombocytopenia (<50×10⁹/L, often <30).
- **Novel:** Fc glycosylation (fucosylation) analysis by MS or **cSPRi** for severity stratification; anti-HPA-1a antibody level (IU/mL) for risk (threshold ~70 IU/mL associated with ICH risk, [PMID: 40833869](https://pubmed.ncbi.nlm.nih.gov/40833869/)).
- **Imaging:** fetal/neonatal cranial **ultrasound** and **MRI** to detect ICH, porencephaly, ventriculomegaly.
- **Clinical criterion:** isolated severe thrombocytopenia in a well term neonate + confirmed maternal–fetal HPA incompatibility + maternal anti-HPA antibody.
- **Differential:** maternal ITP, sepsis/DIC, TORCH infection, inherited thrombocytopenias (Wiskott-Aldrich, pyruvate kinase deficiency).
- **Screening:** no routine antenatal screening program exists anywhere; expert Delphi consensus supports a future anti-HPA-1a-level-based program ([PMID: 40175002](https://pubmed.ncbi.nlm.nih.gov/40175002/)).

### 11. Outcome/Prognosis
Uncomplicated FNAIT resolves without sequelae. **ICH prognosis is grave:** ~48% perinatal mortality, ~80% death-or-severe-NDI. Complications include cerebral palsy, cognitive impairment, blindness, deafness, and epilepsy. **Prognostic factors:** anti-HPA-1a antibody level, Fc afucosylation/galactosylation, prior affected sibling with ICH, and maternal anti-angiogenic profile (sFlt-1/PlGF). Antenatal IVIG reverses most of the adverse prognosis.

### 12. Treatment
| Intervention | Class / NCIT concept | Role |
|---|---|---|
| **IVIG** (1 g/kg/week) | Immunoglobulin therapy | Antenatal standard; prevents ICH |
| **Prednisone** | Corticosteroid | Added in high-risk pregnancies |
| **HPA-matched platelet transfusion** | Cellular transfusion | Neonatal; largest increment |
| **Nipocalimab** | FcRn blocker (mAb) | Phase 3 (FREESIA); blocks IgG transplacental transfer |
| **RLYB212** | Anti-HPA-1a mAb prophylaxis | Phase 1b; "platelet RhoGAM" |

Fetal blood sampling / intrauterine platelet transfusion are now generally avoided. Treatment is personalized by risk tier (prior ICH = highest risk → earlier/more intensive therapy).

### 13. Prevention
**Primary prevention (in development):** prophylactic anti-HPA-1a (RLYB212/NAITgam) to prevent maternal immunization, modeled on anti-D prophylaxis. **Secondary prevention:** antenatal screening for HPA-1a status + antibody level (not yet implemented); antenatal IVIG in identified at-risk pregnancies. **Tertiary prevention:** neonatal platelet transfusion and monitoring to prevent hemorrhagic complications. **Counseling:** genetic/immunohematologic counseling for couples with a prior affected child; fetal HPA-1 typing (15% of at-risk pregnancies carry an HPA-1a-negative fetus and are not at risk).

### 14. Other Species / Natural Disease
A naturally analogous disorder exists in pigs (porcine neonatal alloimmune thrombocytopenia) and is recognized in other livestock; the mechanism (maternal anti-platelet alloantibody via colostrum) differs in transmission route. *ITGB3* is conserved across mammals (NCBI Gene ortholog mouse *Itgb3*). No major zoonotic dimension. Murine models (below) are the principal experimental system.

### 15. Model Organisms
- **Mouse (primary model):** β3-integrin knockout females immunized against β3, then bred to wild-type males, generate anti-β3 (HPA-1a-analogous) FNAIT; recapitulates thrombocytopenia, ICH, impaired angiogenesis, IUGR, and miscarriage, and demonstrates IVIG rescue ([PMID: 25774504](https://pubmed.ncbi.nlm.nih.gov/25774504/), [PMID: 16317099](https://pubmed.ncbi.nlm.nih.gov/16317099/), [PMID: 28794456](https://pubmed.ncbi.nlm.nih.gov/28794456/)).
- **Dual-humanized mouse (APLDQ HPA-1a platelets × human FcγR):** used to prove FcγRIII-dependence of platelet clearance ([PMID: 42269082](https://pubmed.ncbi.nlm.nih.gov/42269082/)).
- **In vitro:** human endothelial cell proliferation/tube-formation assays; in vitro megakaryopoiesis cultures ([PMID: 26209661](https://pubmed.ncbi.nlm.nih.gov/26209661/)).
- **Phenotype recapitulation:** high for thrombocytopenia, ICH, angiogenic defect, placental/NK pathology. **Limitations:** murine HPA system differs antigenically from human; antibody kinetics and placental architecture are not identical.

---

## Mechanistic Model / Interpretation

FNAIT is best understood as a **single upstream trigger (maternal anti-HPA-1a IgG) producing three downstream effector branches**:

| Branch | Effector | Primary lesion | Clinical outcome | Key evidence |
|---|---|---|---|---|
| **Platelet** | FcγRIII+ macrophages (spleen) + MK suppression | Platelet clearance, reduced production | Thrombocytopenia | [PMID: 42269082](https://pubmed.ncbi.nlm.nih.gov/42269082/), [PMID: 26209661](https://pubmed.ncbi.nlm.nih.gov/26209661/) |
| **Vascular** | Anti-β3 on endothelial αvβ3 → ↓AKT | Impaired angiogenesis, endothelial apoptosis | Intracranial hemorrhage | [PMID: 25774504](https://pubmed.ncbi.nlm.nih.gov/25774504/) |
| **Placental** | Complement (C4d) + uNK cells | Histiocytic intervillositis, trophoblast apoptosis | IUGR, miscarriage | [PMID: 34329972](https://pubmed.ncbi.nlm.nih.gov/34329972/), [PMID: 28794456](https://pubmed.ncbi.nlm.nih.gov/28794456/), [PMID: 34201864](https://pubmed.ncbi.nlm.nih.gov/34201864/) |

The clinical corollary is that **platelet count alone poorly predicts the most dangerous outcome (ICH)**, because hemorrhage is a vascular phenomenon. **Fc afucosylation** is the master "volume knob" amplifying the platelet and vascular branches via enhanced FcγRIII engagement. Therapeutically, IVIG acts broadly (competes for FcRn, blocks FcγR, dampens all three branches), whereas **nipocalimab** attacks the upstream delivery step (FcRn-mediated placental IgG transfer) and **RLYB212** aims to prevent the trigger (maternal sensitization) entirely.

---

## Evidence Base

| PMID | Role in report | Key contribution |
|---|---|---|
| [41089465](https://pubmed.ncbi.nlm.nih.gov/41089465/) | Support F1 | HLA-DRB3\*01:01 restriction, first-pregnancy immunization |
| [26564154](https://pubmed.ncbi.nlm.nih.gov/26564154/) | Support F1, F4 | Anti-HPA-1a predominance; 1/1000–1/2000 incidence |
| [16317099](https://pubmed.ncbi.nlm.nih.gov/16317099/) | Support F1; model | GPIIIa/β3 extracellular epitope; murine IVIG model |
| [42269082](https://pubmed.ncbi.nlm.nih.gov/42269082/) | Support F2 | FcγRIII-dependent phagocytosis as dominant clearance |
| [41779743](https://pubmed.ncbi.nlm.nih.gov/41779743/) | Support F2, F3 | Fc fucosylation–severity link; ICH 10–20% |
| [26209661](https://pubmed.ncbi.nlm.nih.gov/26209661/) | Support F2 | Maternal sera suppress in vitro megakaryopoiesis |
| [25774504](https://pubmed.ncbi.nlm.nih.gov/25774504/) | Support F3 | Anti-β3 angiogenesis impairment drives ICH; IVIG rescue |
| [30467085](https://pubmed.ncbi.nlm.nih.gov/30467085/) | Support F3 | Endothelial dysfunction, not thrombocytopenia, in FNAIT ICH |
| [41542834](https://pubmed.ncbi.nlm.nih.gov/41542834/) | Support F4 | PREVFNAIT: 2.4% HPA-1a-neg, 9.1% alloimmunize |
| [32657948](https://pubmed.ncbi.nlm.nih.gov/32657948/) | Support F4 | US incidence; leading cause of severe neonatal thrombocytopenia/ICH |
| [38407610](https://pubmed.ncbi.nlm.nih.gov/38407610/) | Support F4 | Natural history; 90% HLA-DRB3\*01:01+; ~11/10,000 bleeding |
| [33839095](https://pubmed.ncbi.nlm.nih.gov/33839095/) | Support F5 | Antenatal IVIG + prednisone standard of care |
| [40720970](https://pubmed.ncbi.nlm.nih.gov/40720970/), [41290206](https://pubmed.ncbi.nlm.nih.gov/41290206/) | Support F5 | Nipocalimab FcRn blockade phase 3 trials |
| [39168139](https://pubmed.ncbi.nlm.nih.gov/39168139/) | Support F5 | RLYB212 prophylaxis proof-of-concept |
| [36108655](https://pubmed.ncbi.nlm.nih.gov/36108655/) | Support F5 | HPA-matched transfusion increments; postnatal management |
| [24243971](https://pubmed.ncbi.nlm.nih.gov/24243971/) | Support F6 | Afucosylation ↑FcγRIIIa/b binding; correlates with severity |
| [27017954](https://pubmed.ncbi.nlm.nih.gov/27017954/) | Support F6 | Multivariate glyco + titer predicts bleeding; stable across pregnancies |
| [37868955](https://pubmed.ncbi.nlm.nih.gov/37868955/) | Support F6 | cSPRi diagnostic assay validated vs MS |
| [34329972](https://pubmed.ncbi.nlm.nih.gov/34329972/) | Support F7 | Chronic histiocytic intervillositis 40.7% |
| [28794456](https://pubmed.ncbi.nlm.nih.gov/28794456/) | Support F7 | uNK-mediated trophoblast apoptosis; NK depletion rescue |
| [34201864](https://pubmed.ncbi.nlm.nih.gov/34201864/) | Support F7 | Placental C4d complement activation |
| [39486121](https://pubmed.ncbi.nlm.nih.gov/39486121/), [16157119](https://pubmed.ncbi.nlm.nih.gov/16157119/) | Support F7 | Anti-angiogenic sFlt-1 profile; chronic villitis & IUGR |
| [29730660](https://pubmed.ncbi.nlm.nih.gov/29730660/) | Support F8 | ICH 48% mortality, 80% death-or-severe-NDI |
| [17094038](https://pubmed.ncbi.nlm.nih.gov/17094038/) | Support F8 | Sibling-pair IVIG efficacy (no treated ICH) |
| [15363839](https://pubmed.ncbi.nlm.nih.gov/15363839/), [35671780](https://pubmed.ncbi.nlm.nih.gov/35671780/) | Support F8 | Near-normal long-term neurodevelopment after IVIG |
| [31973628](https://pubmed.ncbi.nlm.nih.gov/31973628/) | Support F9 | Underdiagnosis; HPA-15 incompatibility |
| [34033425](https://pubmed.ncbi.nlm.nih.gov/34033425/), [26171707](https://pubmed.ncbi.nlm.nih.gov/26171707/), [37473739](https://pubmed.ncbi.nlm.nih.gov/37473739/), [27250900](https://pubmed.ncbi.nlm.nih.gov/27250900/) | Support F9 | Differential diagnosis (ITP, WAS, PKD, Coxsackievirus) |
| [37027241](https://pubmed.ncbi.nlm.nih.gov/37027241/), [41672591](https://pubmed.ncbi.nlm.nih.gov/41672591/) | Support F9 | NAIT severity vs non-NAIT; under-identification |
| [40833869](https://pubmed.ncbi.nlm.nih.gov/40833869/) | Risk stratification | Antibody threshold (70 IU/mL) for ICH risk |
| [40175002](https://pubmed.ncbi.nlm.nih.gov/40175002/) | Policy | Delphi consensus toward anti-HPA-1a-level screening |

---

## Limitations and Knowledge Gaps

1. **No disease-level omics dataset was analyzed directly.** This report is a literature synthesis; findings rest on published cohorts, case series, and model-organism experiments rather than primary data generated in this investigation.
2. **ICH angiogenesis mechanism is largely murine/in vitro.** The anti-β3 → impaired-AKT → endothelial-apoptosis → ICH pathway is strongly supported in mice and human endothelial assays but has not been directly demonstrated in human fetal brain tissue (an inferred step).
3. **Severity prediction remains imperfect.** Antibody level, Fc glycosylation, and sFlt-1/PlGF each contribute but no single validated biomarker reliably identifies which immunized pregnancies will develop ICH; thresholds (e.g., 70 IU/mL) have high specificity but modest sensitivity.
4. **No implemented screening program.** Cost-effectiveness and the optimal screening algorithm (HPA-1a typing ± antibody level) are unresolved; natural-history incidence estimates have wide confidence intervals.
5. **Non-HPA-1a antigens underexplored.** HPA-5b, HPA-15, and rarer specificities contribute to the under-identified case burden but have thinner mechanistic/epidemiologic data.
6. **Nipocalimab and RLYB212 efficacy pending.** Phase 3 (nipocalimab) and later-phase (RLYB212) outcomes are not yet reported; their comparative benefit over IVIG is unknown.

## Proposed Follow-up Experiments / Actions

1. **Prospective validation of a combined ICH-risk score** integrating anti-HPA-1a IU/mL, Fc afucosylation (cSPRi), and third-trimester sFlt-1/PlGF, with ICH as the endpoint, to enable targeted (rather than universal) antenatal IVIG.
2. **Human placental/endothelial confirmation** of the anti-β3 angiogenesis mechanism using FNAIT patient IgG on fetal brain microvascular endothelial cells and organoid/placenta-on-chip systems.
3. **Cost-effectiveness modeling of antenatal HPA-1a screening** paired with RLYB212 prophylaxis versus current obstetric-history-based management.
4. **Mechanistic readouts in FREESIA trials** — measure platelet counts, antibody transfer, and glycosylation-stratified response to nipocalimab vs IVIG + prednisone.
5. **Registry expansion for non-HPA-1a FNAIT** (HPA-5b, HPA-15) to quantify burden and refine genotyping panels.
6. **uNK/complement-targeted intervention studies** in murine FNAIT (e.g., NKp46 or complement blockade) to test rescue of IUGR/miscarriage distinct from platelet effects.

---

*Report compiled from 9 confirmed findings and 43 reviewed publications across a 5-iteration autonomous investigation. Evidence source types span human clinical cohorts, model-organism experiments, and in vitro studies, as annotated throughout.*


## Artifacts

- [OpenScientist final report](Fetomaternal_Alloimmune_Thrombocytopenia_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Fetomaternal_Alloimmune_Thrombocytopenia_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 37 |
| On topic | 32 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002170` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Intracranial hemorrhage**
- `HP:0001518` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Small for gestational age**
- `HP:0001873` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Thrombocytopenia**
- `HP:0000967` (1 mention) - the report calls it "Physical sign"; HP calls it **Petechiae**
- `HP:0000505` (1 mention) - the report calls it "Sign"; HP calls it **Visual impairment**
- `HP:0012758` (1 mention) - the report calls it "Sign"; HP calls it **Neurodevelopmental delay**
- `UBERON:0000178` (1 mention) - the report calls it "Primary:** blood/platelets"; UBERON calls it **blood**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000955` (2 mentions) - the report calls it "Secondary:** brain"; UBERON calls it **brain**, and lists "the brain" among its other names