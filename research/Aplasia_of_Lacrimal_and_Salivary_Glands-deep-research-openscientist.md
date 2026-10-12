---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-08T13:33:01.097221'
end_time: '2026-10-08T14:09:51.137237'
duration_seconds: 2210.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Aplasia of Lacrimal and Salivary Glands
  mondo_id: MONDO:0008397
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
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 8
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 27
  not_found: 1
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.034
  labels_checked: 20
  labels_matching: 6
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0008397
    reported_labels:
    - MONDO
    ontology_label: aplasia of lacrimal and salivary glands
  - term_id: HP:0000217
    reported_labels:
    - Symptom
    ontology_label: Xerostomia
  - term_id: HP:0000670
    reported_labels:
    - Clinical sign
    ontology_label: Carious teeth
  - term_id: HP:0009746
    reported_labels:
    - abnormal salivary gland morphology
    ontology_label: Thick nasal septum
  - term_id: HP:0009926
    reported_labels:
    - Symptom
    ontology_label: Epiphora
  - term_id: HP:0000495
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent corneal erosions
  - term_id: HP:0100580
    reported_labels:
    - Clinical sign
    ontology_label: Barrett esophagus
  - term_id: UBERON:0001833
    reported_labels:
    - Sublingual gland
    ontology_label: lip
  labels_variant: 6
  unresolved_terms:
  - HP:0000562
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Aplasia_of_Lacrimal_and_Salivary_Glands-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Aplasia_of_Lacrimal_and_Salivary_Glands-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aplasia of Lacrimal and Salivary Glands
- **MONDO ID:** MONDO:0008397 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Aplasia of Lacrimal and Salivary Glands** covering all of the
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

# Aplasia of Lacrimal and Salivary Glands (ALSG): A Comprehensive Disease Characterization

**Disease:** Aplasia of Lacrimal and Salivary Glands
**MONDO ID:** MONDO:0008397 · **OMIM:** #180920 · **Category:** Mendelian (autosomal dominant)
**Causal gene:** *FGF10* (HGNC:3853; 5p12)
**Evidence basis:** Literature synthesis (human clinical case reports/kindreds, ex vivo organ culture, mouse developmental genetics). Aggregated disease-level synthesis; no patient-level/EHR data.

---

## Summary

Aplasia of Lacrimal and Salivary Glands (ALSG) is a rare, congenital, autosomal dominant Mendelian disorder caused by heterozygous loss-of-function variants in the fibroblast growth factor 10 gene (*FGF10*), producing **haploinsufficiency**. The disorder is characterized by aplasia, atresia, or hypoplasia of the lacrimal and salivary gland systems, leading to lifelong dry eyes (xerophthalmia), excessive tearing from blocked drainage (epiphora), and dry mouth (xerostomia). ALSG sits at the mild end of a phenotypic spectrum that is allelic with the more severe **Lacrimo-Auriculo-Dento-Digital (LADD) syndrome**, which is caused by mutations in *FGF10* and in its receptors *FGFR2* and *FGFR3*. Whereas ALSG is restricted to lacrimal and salivary involvement, LADD adds ear, dental, and digital anomalies.

Mechanistically, ALSG is a **dosage-sensitive developmental signaling disorder**. During embryogenesis, FGF10 secreted from gland mesenchyme activates epithelial FGFR2b (FGFR2-IIIb) and downstream ERK1/2 signaling to drive the branching morphogenesis and duct elongation that build the lacrimal and salivary glands. Reduced FGF10 gene dosage fails to adequately drive this epithelial program, so the glands never form properly. This mechanism is firmly supported by mouse genetics: *Fgf10*-null mice fail to develop lacrimal and salivary glands, and blocking FGFR2-IIIb suppresses endogenous lacrimal bud development. The clinical consequences are secondary and largely preventable: chronic xerostomia produces rampant dental caries (approaching 100% of reported agenesis cases), oral candidiasis, and ascending sialadenitis, while alacrimia produces recurrent corneal erosions, ulceration, scarring, and sight-threatening keratopathy.

ALSG is ultra-rare, reported only in scattered multigenerational kindreds and sporadic cases, with no validated population prevalence. It shows **incomplete penetrance and marked intrafamilial variable expressivity**, and each child of an affected parent has a 50% risk of inheriting the variant. Lifespan is normal, and there is **no disease-modifying therapy**. Management is entirely supportive: aggressive caries prevention with fluoride and saliva substitutes, artificial tears, lacrimal drainage reconstruction, and, for severe congenital alacrimia with corneal damage, autologous minor salivary gland transplantation (shown to improve corneal transparency and neovascularization at 5-year follow-up). This report synthesizes 11 confirmed findings across 21 reviewed papers into a complete disease knowledge base entry spanning all 15 template sections.

---

## 1. Disease Information

**Overview.** ALSG is a congenital Mendelian disorder defined by aplasia, atresia, or hypoplasia of the lacrimal and salivary glands and ducts. Affected individuals present with a combination of dry eyes, excessive tearing (epiphora due to nasolacrimal drainage obstruction or punctal atresia), and dry mouth. As one primary source states: *"Aplasia of lacrimal and salivary glands (ALSG) is a rare autosomal dominant inherited disease, characterized by aplasia, atresia, or hypoplasia of the lacrimal and salivary systems with variable expressivity"* ([PMID: 26955834](https://pubmed.ncbi.nlm.nih.gov/26955834/)).

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0008397 |
| OMIM | #180920 (Aplasia of lacrimal and salivary glands; ALSG) |
| Gene | *FGF10* (HGNC:3853), chromosome 5p12 |
| Allelic disorder | LADD syndrome (OMIM #149730) |
| Inheritance | Autosomal dominant |

**Synonyms / alternative names:** ALSG; Aplasia of lacrimal and salivary glands; Aplasia/hypoplasia of lacrimal and salivary glands; Lacrimal and salivary gland aplasia. Related/overlapping entity: Lacrimo-auriculo-dento-digital syndrome (LADD; Levy-Hollister syndrome).

**Information source type.** This report is derived from **aggregated disease-level resources** (OMIM, published case reports, kindred studies, and systematic reviews) rather than individual EHR data. The evidence base consists predominantly of multigenerational family studies and single-case reports, consistent with an ultra-rare Mendelian disorder.

---

## 2. Etiology

**Primary cause — genetic.** ALSG is a monogenic disorder caused by **heterozygous loss-of-function variants in *FGF10*** that reduce the amount of functional FGF10 ligand by half (haploinsufficiency). *"This report further confirms that ALSG is caused by the haploinsufficiency of functional FGF10"* ([PMID: 26955834](https://pubmed.ncbi.nlm.nih.gov/26955834/)).

**Genetic risk factors.** The disease is causally determined by the *FGF10* variant itself; there are no established susceptibility loci or GWAS signals (consistent with Mendelian etiology). A candidate second-locus/modifier gene, *IGSF3*, has been reported in the context of bony congenital nasolacrimal duct obstruction (see Section 4), but its role as a modifier remains to be established ([PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/)).

**Environmental risk factors.** None are established. ALSG is a congenital developmental disorder with no known environmental, toxic, infectious, or lifestyle contribution to causation.

**Protective factors.** No genetic or environmental protective factors have been identified. Because the glands fail to form during embryogenesis, there is no modifiable exposure window after birth that alters disease occurrence (only secondary complications are modifiable).

**Gene–environment interactions.** None demonstrated. The phenotype is determined by *FGF10* dosage; however, the observed **incomplete penetrance and variable expressivity** (Section 4, Finding F004) imply the existence of unidentified genetic modifiers and/or stochastic developmental factors influencing how a given variant manifests.

---

## 3. Phenotypes

ALSG phenotypes fall into two anatomical domains — ocular/lacrimal and oral/salivary — plus rare extended features. All are **congenital** in onset (present from birth), though clinical recognition often occurs in early childhood (mean age ~6.4 years in a salivary agenesis review; [PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/)). Severity is **variable**; progression of the primary gland defect is **stable** (non-progressive aplasia), but secondary complications (caries, keratopathy) are **progressive** if untreated.

| Phenotype | Type | Suggested HPO term | Frequency / notes |
|-----------|------|--------------------|-------------------|
| Xerostomia (dry mouth) | Symptom | HP:0000217 | 80% of major salivary agenesis cases ([PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/)) |
| Dental caries (rampant) | Clinical sign | HP:0000670 | 100% of reviewed agenesis cases ([PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/)) |
| Aplasia/hypoplasia of salivary glands | Physical manifestation | HP:0009746 (abnormal salivary gland morphology) | Parotid, submandibular, sublingual |
| Decreased lacrimation / alacrimia | Symptom | HP:0000633 (xerophthalmia); HP:0000522 (alacrima) | ~50% lacrimal involvement ([PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/)) |
| Epiphora (excessive tearing) | Symptom | HP:0009926 | Unilateral or bilateral; from drainage obstruction ([PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/)) |
| Aplasia/atresia of lacrimal gland | Physical manifestation | HP:0000562 (abnormal lacrimal duct morphology) | Variable |
| Lacrimal punctal atresia/anomaly | Clinical sign | HP:0000562 | Reported with gland agenesis ([PMID: 22339588](https://pubmed.ncbi.nlm.nih.gov/22339588/)) |
| Recurrent corneal erosion / keratopathy | Clinical sign | HP:0000495 | Sight-threatening in severe alacrimia ([PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)) |
| Oral candidiasis | Clinical sign | HP:0100580 | Secondary to xerostomia ([PMID: 22339588](https://pubmed.ncbi.nlm.nih.gov/22339588/)) |
| Bony congenital nasolacrimal duct obstruction | Physical manifestation | HP:0000579 (abnormal nasolacrimal system) | Novel extended phenotype ([PMID: 38081329](https://pubmed.ncbi.nlm.nih.gov/38081329/)) |

**Quality-of-life impact.** Chronic xerostomia impairs eating, swallowing, speech, and taste, and promotes relentless dental disease requiring continuous intervention. Alacrimia causes photophobia, ocular pain from corneal erosions, and risk of vision loss. Minor salivary gland transplantation for severe alacrimia produced *"considerable improvement in the photophobia, corneal transparency, and neovascularization"* ([PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)), underscoring both the baseline burden and the modifiability of ocular morbidity.

---

## 4. Genetic / Molecular Information

**Causal gene.** *FGF10* (fibroblast growth factor 10), HGNC:3853, chromosome 5p12; encodes a paracrine FGF ligand that signals through FGFR2b.

**Pathogenic variant spectrum.** ALSG-causing variants are heterozygous and loss-of-function, acting through haploinsufficiency. Documented variant classes:

| Variant | Type | Mechanism | Reference |
|---------|------|-----------|-----------|
| c.237G>A (p.Trp79*) in exon 1 | Nonsense | NMD-mediated haploinsufficiency | [PMID: 26955834](https://pubmed.ncbi.nlm.nih.gov/26955834/) |
| c.429+1G>T (donor splice site) | Splice-site | Exon 2 skipping | [PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/) |
| c.429+2T>A (donor splice site) | Splice-site | Aberrant splicing | [PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/) |
| 6 missense variants | Missense | Reduced ligand function | [PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/) |
| 5p12 deletion encompassing *FGF10* | Structural (CNV) | Whole-gene loss | [PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/) |
| Novel LoF variant (EA/ALSG/PH case) | Loss-of-function | Haploinsufficiency | [PMID: 41409311](https://pubmed.ncbi.nlm.nih.gov/41409311/) |

**Variant classification (ACMG/AMP).** Nonsense, canonical splice-site, and whole-gene deletion variants meet pathogenic criteria (PVS1 null-variant in a LoF-mechanism gene plus segregation). Missense variants require case-by-case classification.

**Allele frequency.** Pathogenic variants are private/ultra-rare and essentially absent from population databases (gnomAD), consistent with a highly penetrant Mendelian disorder.

**Somatic vs germline.** All reported ALSG variants are **germline**.

**Functional consequence.** **Loss of function → haploinsufficiency.** A 50% reduction in functional FGF10 ligand is insufficient to drive normal gland morphogenesis, indicating the developing lacrimal/salivary epithelium is exquisitely dosage-sensitive to FGF10.

**Allelism with LADD.** ALSG and LADD form a single FGF-signaling disease spectrum. *"We identified heterozygous mutations in the tyrosine kinase domains of the genes encoding fibroblast growth factor receptors 2 and 3 (FGFR2, FGFR3) in LADD families, and in one further LADD family, we detected a mutation in the gene encoding fibroblast growth factor 10 (FGF10), a known FGFR ligand"* ([PMID: 16501574](https://pubmed.ncbi.nlm.nih.gov/16501574/)). *"Lacrimo-auriculo-dento-digital (LADD) syndrome is a rare autosomal dominant disorder caused by mutations in one of the three genes: fibroblast growth factor receptor 2 (FGFR2), FGFR3, or FGF10"* ([PMID: 32715658](https://pubmed.ncbi.nlm.nih.gov/32715658/)).

**Modifier genes / second locus.** *IGSF3* variants (three reported) co-occurring with *FGF10* variants in bony congenital nasolacrimal duct obstruction are candidate modifiers or an independent contributing locus ([PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/)).

**Epigenetic / chromosomal.** No disease-specific epigenetic signature is established. The principal structural abnormality is the 5p12 microdeletion encompassing *FGF10*, detectable by chromosomal microarray ([PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/)).

---

## 5. Environmental Information

No environmental, lifestyle, or infectious etiological factors are relevant to ALSG causation — it is a purely genetic developmental disorder. Environmental factors are relevant only to **secondary complication management**: dietary sugar intake and oral hygiene modulate the rate of caries progression, and ambient dryness/wind exacerbate ocular surface disease. Infectious agents (e.g., *Candida albicans* causing oral candidiasis; ascending bacterial sialadenitis) are **downstream consequences** of glandular hypofunction, not causes of the disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous loss-of-function *FGF10* variant (nonsense, splice-site, missense, or whole-gene deletion) **leads to** nonsense-mediated decay or non-functional product, **resulting in** ~50% reduction of functional FGF10 ligand (haploinsufficiency). [[PMID: 26955834](https://pubmed.ncbi.nlm.nih.gov/26955834/)]
2. Reduced FGF10 secreted by gland **mesenchyme leads to** insufficient activation of epithelial **FGFR2b (FGFR2-IIIb)** receptors on the developing lacrimal and salivary epithelium. [[PMID: 10821755](https://pubmed.ncbi.nlm.nih.gov/10821755/)]
3. Diminished FGFR2b signaling **results in** reduced downstream **ERK1/2 (MAPK) phosphorylation** and loss of localized epithelial proliferation at duct/bud tips. [[PMID: 15716343](https://pubmed.ncbi.nlm.nih.gov/15716343/)]
4. Failed proliferation/duct elongation **leads to** defective **branching morphogenesis** of the lacrimal and salivary gland anlagen during embryogenesis. [[PMID: 15716343](https://pubmed.ncbi.nlm.nih.gov/15716343/), [PMID: 26565022](https://pubmed.ncbi.nlm.nih.gov/26565022/)]
5. Defective morphogenesis **results in** congenital **aplasia/atresia/hypoplasia** of lacrimal glands, salivary glands (parotid, submandibular, sublingual), and associated ducts/puncta. [[PMID: 10821755](https://pubmed.ncbi.nlm.nih.gov/10821755/)]
6. Absent/deficient glands **lead to** reduced tear and saliva production → **xerophthalmia/alacrimia and xerostomia** (and epiphora where drainage structures are atretic). [[PMID: 38081329](https://pubmed.ncbi.nlm.nih.gov/38081329/)]
7. **Branch A (oral):** Chronic xerostomia **leads to** rampant dental caries (~100%), oral candidiasis, and ascending sialadenitis. [[PMID: 22339588](https://pubmed.ncbi.nlm.nih.gov/22339588/), [PMID: 11340723](https://pubmed.ncbi.nlm.nih.gov/11340723/)]
8. **Branch B (ocular):** Alacrimia **leads to** recurrent corneal erosions, ulceration, scarring, and neovascularization → sight-threatening keratopathy. [[PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)]

*(Steps 1 and 2 are directly demonstrated in human and mouse genetics; steps 3–4 are demonstrated ex vivo in mouse submandibular gland cultures; steps 5–8 are human clinical observations.)*

### ASCII mechanistic diagram

```
 FGF10 LoF variant (heterozygous)
          │ haploinsufficiency (~50% ligand)
          ▼
 Mesenchymal FGF10  ──(paracrine)──►  Epithelial FGFR2b (FGFR2-IIIb)
                                              │  [Cx43 gap junctions,
                                              │   perlecan-HS/heparanase
                                              │   modulate availability]
                                              ▼
                                       ERK1/2 (MAPK) ↓
                                              ▼
                              Localized tip proliferation ↓
                                              ▼
                          Branching morphogenesis / duct elongation ↓
                                              ▼
                 Congenital aplasia of lacrimal & salivary glands
                         │                                    │
             ┌───────────┘                                    └───────────┐
             ▼ (ocular branch)                                            ▼ (oral branch)
   Alacrimia → corneal erosion,                          Xerostomia → rampant caries,
   ulceration, keratopathy                               candidiasis, sialadenitis
```

### Supporting detail

- **Molecular pathway (KEGG hsa04010 MAPK; FGF signaling).** FGF10→FGFR2b→RAS/MAPK(ERK1/2) is the core cascade. *"FGF7 induces epithelial budding, whereas FGF10 induces duct elongation, and both are inhibited by FGFR or ERK1/2 signaling inhibitors"* and *"FGF10 stimulates localized proliferation at the tip of the duct"* ([PMID: 15716343](https://pubmed.ncbi.nlm.nih.gov/15716343/)).
- **Cellular process.** Epithelial cell proliferation and branching morphogenesis (GO:0048754, branching morphogenesis of an epithelial tube; GO:0060442, branching involved in salivary gland morphogenesis).
- **Co-regulators of ligand availability.** Connexin 43 (Cx43) gap junctions are required for FGF10-induced ERK1/2 phosphorylation and SMG branching ([PMID: 26565022](https://pubmed.ncbi.nlm.nih.gov/26565022/)); perlecan heparan sulfate and heparanase regulate release and activity of the FGF10–FGFR2b complex in the basement membrane ([PMID: 17959718](https://pubmed.ncbi.nlm.nih.gov/17959718/)).
- **Extended developmental roles.** FGF10 also governs limb and lung morphogenesis; *Fgf10*-null mice show limb and lung agenesis, rescuable by ubiquitous *Fgf10* ([PMID: 23924632](https://pubmed.ncbi.nlm.nih.gov/23924632/)), explaining the rare extended ALSG phenotypes (esophageal atresia, pulmonary hypoplasia; [PMID: 41409311](https://pubmed.ncbi.nlm.nih.gov/41409311/)).

**Suggested ontology terms:** GO:0060442 (branching involved in salivary gland morphogenesis), GO:0060664 (epithelial cell proliferation involved in salivary gland morphogenesis), GO:0008543 (FGF receptor signaling pathway), GO:0070374 (positive regulation of ERK1/ERK2 cascade). Cell types: CL:0000066 (epithelial cell), CL:0000134 (mesenchymal cell).

---

## 7. Anatomical Structures Affected

**Organ level (primary).**
- Lacrimal gland (UBERON:0001817) and lacrimal apparatus/nasolacrimal duct (UBERON:0000395 / UBERON:0004515)
- Parotid gland (UBERON:0001831)
- Submandibular gland (UBERON:0001736)
- Sublingual gland (UBERON:0001833)

**Secondary / complication sites.**
- Cornea (UBERON:0000964) and ocular surface — keratopathy from alacrimia
- Teeth (UBERON:0001091) — rampant caries from xerostomia
- Oral mucosa — candidiasis

**Rare extended involvement (FGF10 pleiotropy).** Lung (UBERON:0002048; pulmonary hypoplasia), esophagus (UBERON:0001043; esophageal atresia), and digits/limb (thumb phalangeal hypoplasia), reflecting FGF10's broader developmental roles ([PMID: 41409311](https://pubmed.ncbi.nlm.nih.gov/41409311/)).

**Body systems:** exocrine/glandular (primary), visual/ocular, and digestive (oral) systems.

**Tissue and cell level.** The affected tissue is **glandular epithelium** (and its inducing **mesenchyme**). The disease is a failure of epithelial branching morphogenesis; FGF10 is expressed in mesenchyme and acts on epithelial FGFR2b.

**Subcellular level.** FGF10 is a secreted ligand (extracellular/basement membrane, GO:0005615); signaling is transduced at the plasma membrane receptor (FGFR2b) to the cytoplasmic MAPK cascade. No specific organelle pathology (mitochondria, lysosome) is implicated.

**Localization / lateralization.** Involvement is typically **bilateral** but can be **unilateral or asymmetric**, consistent with variable expressivity — e.g., *"unilateral or bilateral epiphora"* and absence of unilateral lacrimal puncta reported across kindreds ([PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/), [PMID: 22339588](https://pubmed.ncbi.nlm.nih.gov/22339588/)).

---

## 8. Temporal Development

**Onset.** Congenital — the glands fail to form during embryonic development. Symptoms are present from birth (e.g., *"absence of tear secretion since birth"*; [PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)), though clinical diagnosis often occurs in early childhood (mean ~6.4 years in a salivary agenesis review; [PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/)).

**Onset pattern.** Chronic/static with respect to the primary structural defect (aplasia does not progress — the glands are simply absent or hypoplastic from the outset).

**Progression.** The **primary defect is stable** (non-progressive). **Secondary complications are progressive** if untreated: dental caries advance relentlessly under chronic xerostomia, and recurrent corneal erosions lead to cumulative scarring and neovascularization.

**Disease course.** Chronic, lifelong. Not episodic or relapsing-remitting for the gland defect itself, though complications (caries episodes, corneal erosion episodes, sialadenitis flares) may recur.

**Critical periods / windows for intervention.** The critical **developmental** window (gland morphogenesis in utero) has passed by birth, so no primary prevention is possible postnatally. The critical **clinical** windows are early childhood for initiating intensive caries prevention and ocular surface protection to prevent irreversible dental and corneal damage.

---

## 9. Inheritance and Population

**Epidemiology.** ALSG is **ultra-rare**. No validated prevalence or incidence figures exist; the disorder is known only from scattered multigenerational kindreds and sporadic case reports. *"Congenital agenesis of the major salivary glands is a rare developmental anomaly"* — a systematic review found only ~20 pediatric cases of complete major salivary gland agenesis ([PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/)). *"Aplasia of lacrimal and salivary glands (ALSG) is a rare autosomal dominant inherited disease"* ([PMID: 26955834](https://pubmed.ncbi.nlm.nih.gov/26955834/)).

**Inheritance pattern.** Autosomal dominant.

**Penetrance.** **Incomplete.** In a six-generation kindred with a single *FGF10* splice variant (c.429+1G>T), *"one of the variant carriers had no ALSG-related clinical findings, demonstrating incomplete penetrance"* ([PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/)).

**Expressivity.** **Variable**, including intrafamilial variability — unilateral vs bilateral involvement, variable dry mouth/caries, and variable lacrimal involvement within the same family carrying one variant ([PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/)).

**Recurrence risk.** As an autosomal dominant condition, each child of an affected parent has a **50% risk** of inheriting the variant; penetrance and expressivity modify the clinical outcome.

**Genetic anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency.** No genetic anticipation (not a repeat-expansion disorder). No founder effect, sex predilection, or population enrichment established. "Carrier frequency" is not a standard concept for this dominant, ultra-rare disorder.

**Population demographics.** No ethnic, geographic, or sex-specific predilection is established; reported kindreds span multiple populations (e.g., Korean LADD family; [PMID: 32715658](https://pubmed.ncbi.nlm.nih.gov/32715658/)).

---

## 10. Diagnostics

**Imaging (cornerstone).**
- **Salivary scintigraphy** with technetium-99m sodium pertechnetate is the principal modality demonstrating bilateral aplasia of parotid, submandibular, and sublingual glands: *"Tc-99m scintigraphy was the most common diagnostic modality"* ([PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/), [PMID: 22339588](https://pubmed.ncbi.nlm.nih.gov/22339588/)).
- **Orbital CT / cervicofacial MRI** show absent lacrimal, parotid, and submandibular glands, and bony congenital nasolacrimal duct obstruction ([PMID: 38081329](https://pubmed.ncbi.nlm.nih.gov/38081329/), [PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/)).
- **Ultrasonography** (including UHFUS) can evaluate major and labial salivary/lacrimal glands ([PMID: 37685309](https://pubmed.ncbi.nlm.nih.gov/37685309/)).

**Ocular functional tests.** Reduced **Schirmer I test** and shortened **tear breakup time** document tear deficiency: *"Affected patients showed decreased tear production on the Schimer I test and reduced tear breakup time"* ([PMID: 38081329](https://pubmed.ncbi.nlm.nih.gov/38081329/)).

**Genetic testing.** **Whole-exome sequencing (WES)** identifies causal *FGF10* variants and is the molecular confirmation of choice; single-gene *FGF10* testing and targeted panels (*FGF10/FGFR2/FGFR3* for the ALSG–LADD spectrum) are appropriate. **Chromosomal microarray** detects the 5p12 deletion ([PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/)).

**Differential diagnosis.** The key differential is **juvenile/primary Sjögren disease** (also causing xerostomia + xerophthalmia), excluded by the congenital onset, absence of autoimmune serology (ANA, anti-SS-A/SS-B), and non-inflammatory imaging/pathology ([PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/), [PMID: 32715658](https://pubmed.ncbi.nlm.nih.gov/32715658/)). Other differentials: LADD syndrome (add ear/dental/digital features), and radiation/iatrogenic gland loss.

**Screening.** No population newborn screening exists. Cascade genetic testing of at-risk relatives in known kindreds is appropriate given autosomal dominant inheritance.

---

## 11. Outcome / Prognosis

**Survival / life expectancy.** Normal. ALSG is **not life-limiting**; mortality is not increased by the disorder itself.

**Morbidity.** Substantial but largely preventable. The dominant morbidities are **dental** (rampant caries, potential tooth loss) and **ocular** (keratopathy with risk of vision impairment), plus the quality-of-life burden of chronic dry mouth and dry/irritated eyes.

**Complications.** Rampant dental caries (~100% of agenesis cases), oral candidiasis, ascending sialadenitis, and recurrent corneal erosions/ulceration with scarring and neovascularization. *"which may cause severe xerostomia, progressive dental caries, and oropharyngeal candidiasis in children"* ([PMID: 22339588](https://pubmed.ncbi.nlm.nih.gov/22339588/)); *"repeated episodes of corneal erosions and ulceration and absence of tear secretion since birth"* ([PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)).

**Recovery potential.** The structural gland aplasia is irreversible, but complications are modifiable and partly reversible: minor salivary gland transplantation improved corneal transparency and neovascularization at 5-year follow-up ([PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)).

**Prognostic factors.** Severity of gland involvement (uni- vs bilateral, complete vs partial), timeliness of caries prevention, and ocular surface protection determine long-term outcomes. No molecular prognostic biomarker is established; given variable expressivity, genotype is an imperfect predictor of severity.

---

## 12. Treatment

**No disease-modifying therapy exists.** Management is entirely **symptomatic and supportive**, and because secondary complications are preventable, prevention is the mainstay: *"attention focused on the prevention and treatment of resultant oral disease"* ([PMID: 11340723](https://pubmed.ncbi.nlm.nih.gov/11340723/)).

**Oral / dental management.**
- Intensive caries prevention: topical/systemic **fluoride**, meticulous oral hygiene, dietary counseling, remineralizing agents.
- **Saliva substitutes** and sialogogues for symptomatic relief; restorative dental care for established caries ([PMID: 26955834](https://pubmed.ncbi.nlm.nih.gov/26955834/), [PMID: 11340723](https://pubmed.ncbi.nlm.nih.gov/11340723/)).
- Antifungal therapy for oral candidiasis; antibiotics for sialadenitis as needed.

**Ocular management.**
- **Artificial tears / tear substitutes**, lubricating ointments, and ocular surface protection.
- **Lacrimal drainage reconstruction** for punctal/duct atresia and epiphora ([PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/)).
- **Autologous minor salivary gland transplantation** for severe congenital alacrimia with corneal damage: *"we observed considerable improvement in the photophobia, corneal transparency, and neovascularization"* at long-term (5-year) follow-up ([PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)).

**Advanced / experimental therapeutics.** No gene therapy, cell therapy, RNA-based therapy, or targeted pharmacotherapy is in clinical use for ALSG. Given the haploinsufficiency mechanism, ligand-restoration (recombinant FGF10 or dosage-correction) is a conceptual but untested avenue.

**Suggested NCIT intervention terms:** Fluoride therapy, saliva substitute, artificial tears/ocular lubricant, salivary gland transplantation, lacrimal duct reconstruction, antifungal therapy.

---

## 13. Prevention

**Primary prevention (of the disease).** Not possible postnatally — the glandular defect is established in utero. For families with a known *FGF10* variant, **genetic counseling**, prenatal testing, and preimplantation genetic diagnosis can prevent transmission.

**Secondary prevention (early detection).** Early clinical recognition and molecular confirmation enable prompt institution of protective measures. Cascade genetic testing identifies at-risk relatives.

**Tertiary prevention (of complications) — the practical mainstay.** Aggressive, lifelong caries prevention (fluoride, hygiene, diet, regular dental review) and ocular surface protection (lubrication, drainage correction) prevent the major morbidities of ALSG.

**Counseling.** Autosomal dominant inheritance with 50% recurrence risk, incomplete penetrance, and variable expressivity should be communicated; an unaffected-appearing carrier can still transmit a fully penetrant phenotype to offspring ([PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/)).

**Immunization / public health / environmental prophylaxis.** Not applicable (non-infectious, non-environmental disorder).

---

## 14. Other Species / Natural Disease

**Taxonomy.** The disease has been modeled in **mouse** (*Mus musculus*, NCBI:txid10090). No naturally occurring ALSG-equivalent disorder in companion animals or wildlife is documented in the reviewed literature (OMIA entry not identified here).

**Orthologous gene.** *Fgf10* is highly conserved; mouse *Fgf10* is the functional ortholog used to define the mechanism.

**Comparative biology / evolutionary conservation.** The FGF10→FGFR2b→ERK1/2 branching-morphogenesis mechanism is deeply conserved across vertebrates, and mouse knockouts faithfully reproduce the human gland-aplasia phenotype (Section 15), indicating strong evolutionary conservation of the disease mechanism.

**Transmission / zoonotic potential.** Not applicable (genetic developmental disorder).

---

## 15. Model Organisms

**Primary model — mouse (*Mus musculus*).**

- **Knockout:** *Fgf10*-null mice fail to develop lacrimal and salivary glands, directly recapitulating human aplasia. *"Expression of FGF10 in the mesenchyme adjacent to the presumptive lacrimal bud and absence of lacrimal gland development in FGF10-null mice strongly suggest that it is an endogenous inducer"* ([PMID: 10821755](https://pubmed.ncbi.nlm.nih.gov/10821755/)). FGF10 is also *sufficient* to induce ectopic lacrimal bud formation, and *"inhibition of signaling by a receptor for FGF10 (receptor 2 IIIb) suppressed development of the endogenous lacrimal bud"* ([PMID: 10821755](https://pubmed.ncbi.nlm.nih.gov/10821755/)), confirming FGFR2-IIIb as the mediating receptor.
- **Phenotype recapitulation:** Excellent for the core defect. Homozygous *Fgf10* null is perinatal-lethal (limb and lung agenesis; [PMID: 23924632](https://pubmed.ncbi.nlm.nih.gov/23924632/)); the **heterozygous dosage-reduction state** models human haploinsufficiency.
- **Ex vivo organ culture** (embryonic submandibular gland) is a powerful model dissecting FGF10's role in duct elongation/branching via FGFR2b and ERK1/2 ([PMID: 15716343](https://pubmed.ncbi.nlm.nih.gov/15716343/)), the Cx43 requirement ([PMID: 26565022](https://pubmed.ncbi.nlm.nih.gov/26565022/)), and heparan-sulfate/heparanase regulation of ligand availability ([PMID: 17959718](https://pubmed.ncbi.nlm.nih.gov/17959718/)).

**Model limitations.** Homozygous lethality limits adult phenotyping of complete loss; the mouse does not perfectly replicate the human secondary complications (rampant caries depends on human oral ecology/diet). Variable expressivity and modifier effects seen in human kindreds are not fully captured by inbred knockout lines.

**Resources:** MGI (*Fgf10*), IMPC/KOMP for allele availability.

---

## Key Findings (Expanded)

**F001 — ALSG is an autosomal dominant disorder caused by FGF10 haploinsufficiency.** Multiple independent kindreds show heterozygous loss-of-function *FGF10* variants segregating with disease, including a novel nonsense c.237G>A (p.Trp79*) causing NMD-mediated haploinsufficiency ([PMID: 26955834](https://pubmed.ncbi.nlm.nih.gov/26955834/)) and a donor splice-site c.429+1G>T causing exon 2 skipping ([PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/)). This establishes a clean gene–dosage etiology.

**F002 — ALSG and LADD are allelic FGF-signaling disorders.** LADD results from heterozygous mutations in *FGFR2*, *FGFR3*, or *FGF10* ([PMID: 16501574](https://pubmed.ncbi.nlm.nih.gov/16501574/), [PMID: 32715658](https://pubmed.ncbi.nlm.nih.gov/32715658/)); ALSG is the restricted, milder phenotype within the same pathway.

**F003 / F009 — Mesenchymal FGF10 → epithelial FGFR2b/ERK1/2 drives gland morphogenesis, and mouse knockouts recapitulate the aplasia.** FGF10 induces duct elongation via FGFR2b and ERK1/2 and stimulates localized tip proliferation ([PMID: 15716343](https://pubmed.ncbi.nlm.nih.gov/15716343/)); *Fgf10*-null mice lack lacrimal gland development and blocking FGFR2-IIIb suppresses the endogenous bud ([PMID: 10821755](https://pubmed.ncbi.nlm.nih.gov/10821755/)). Cx43 and perlecan-HS/heparanase tune ligand availability ([PMID: 26565022](https://pubmed.ncbi.nlm.nih.gov/26565022/), [PMID: 17959718](https://pubmed.ncbi.nlm.nih.gov/17959718/)).

**F004 — Incomplete penetrance and variable expressivity.** A single splice variant in a six-generation kindred produced unilateral-to-bilateral disease with one non-penetrant obligate carrier ([PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/)); xerostomia 80% and caries 100% in a salivary-agenesis review ([PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/)).

**F005–F007 — Diagnosis, complications, and management.** Diagnosis uses Tc-99m scintigraphy, orbital/facial imaging, Schirmer test, and genetic testing to exclude Sjögren disease ([PMID: 41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/), [PMID: 38081329](https://pubmed.ncbi.nlm.nih.gov/38081329/)). Complications include rampant caries, candidiasis, sialadenitis, and keratopathy ([PMID: 22339588](https://pubmed.ncbi.nlm.nih.gov/22339588/), [PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)). Management is supportive, with minor salivary gland transplantation benefiting severe alacrimia ([PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)).

**F008 — Extended phenotypic spectrum.** WES of bony CNLDO found 8 novel *FGF10* variants plus candidate *IGSF3* variants ([PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/)); a novel LoF variant linked ALSG to esophageal atresia and pulmonary hypoplasia ([PMID: 41409311](https://pubmed.ncbi.nlm.nih.gov/41409311/)).

---

## Mechanistic Model / Integrated Interpretation

ALSG is best understood as a **dosage-sensitive FGF10 developmental signaling disorder** (Finding F011). The unifying model runs: autosomal dominant *FGF10* haploinsufficiency ([PMID: 26955834](https://pubmed.ncbi.nlm.nih.gov/26955834/), [PMID: 37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/)) → deficient mesenchymal FGF10 → inadequate epithelial FGFR2b/ERK1/2 activation ([PMID: 10821755](https://pubmed.ncbi.nlm.nih.gov/10821755/), [PMID: 15716343](https://pubmed.ncbi.nlm.nih.gov/15716343/)) → failed branching morphogenesis → congenital, variably bilateral aplasia of lacrimal and salivary glands → xerophthalmia/alacrimia and xerostomia → preventable secondary morbidity (rampant caries ~100%, candidiasis, sialadenitis, sight-threatening keratopathy; [PMID: 22339588](https://pubmed.ncbi.nlm.nih.gov/22339588/), [PMID: 11340723](https://pubmed.ncbi.nlm.nih.gov/11340723/), [PMID: 38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/)). The disorder is allelic with LADD ([PMID: 16501574](https://pubmed.ncbi.nlm.nih.gov/16501574/)); the *Fgf10* mouse knockout anchors causality ([PMID: 10821755](https://pubmed.ncbi.nlm.nih.gov/10821755/), [PMID: 23924632](https://pubmed.ncbi.nlm.nih.gov/23924632/)).

### ALSG vs LADD comparison

| Feature | ALSG | LADD syndrome |
|---------|------|---------------|
| Causal genes | *FGF10* (ligand) | *FGF10*, *FGFR2*, *FGFR3* |
| Lacrimal involvement | Yes | Yes |
| Salivary involvement | Yes | Yes |
| Ear anomalies | No | Yes |
| Dental anomalies (beyond caries) | No | Yes |
| Digital anomalies | No | Yes |
| Inheritance | AD | AD |
| Relationship | Milder, restricted form | Broader allelic form |

---

## Evidence Base

| PMID | Role in this report | Source type |
|------|---------------------|-------------|
| [26955834](https://pubmed.ncbi.nlm.nih.gov/26955834/) | ALSG = AD *FGF10* haploinsufficiency; nonsense p.Trp79* | Human clinical/genetic |
| [37615310](https://pubmed.ncbi.nlm.nih.gov/37615310/) | Incomplete penetrance, variable expressivity; splice variant c.429+1G>T | Human kindred |
| [16501574](https://pubmed.ncbi.nlm.nih.gov/16501574/) | LADD caused by FGFR2/FGFR3/FGF10 — allelism | Human genetic |
| [32715658](https://pubmed.ncbi.nlm.nih.gov/32715658/) | LADD three-gene model; differential from Sjögren | Human clinical/review |
| [10821755](https://pubmed.ncbi.nlm.nih.gov/10821755/) | Mouse *Fgf10*-null → absent lacrimal gland; FGFR2-IIIb receptor | Model organism |
| [15716343](https://pubmed.ncbi.nlm.nih.gov/15716343/) | FGF10→FGFR2b→ERK1/2 drives duct elongation | Ex vivo model |
| [26565022](https://pubmed.ncbi.nlm.nih.gov/26565022/) | Cx43 required for FGF10-induced ERK1/2 and branching | Ex vivo model |
| [17959718](https://pubmed.ncbi.nlm.nih.gov/17959718/) | Perlecan-HS/heparanase regulate FGF10 availability | Ex vivo model |
| [23924632](https://pubmed.ncbi.nlm.nih.gov/23924632/) | *Fgf10*-null limb/lung agenesis; rescue by ubiquitous Fgf10 | Model organism |
| [41791508](https://pubmed.ncbi.nlm.nih.gov/41791508/) | Phenotype frequencies; Tc-99m scintigraphy; rarity | Systematic review |
| [22339588](https://pubmed.ncbi.nlm.nih.gov/22339588/) | Oral complications; punctal absence | Human case/review |
| [38537898](https://pubmed.ncbi.nlm.nih.gov/38537898/) | Minor salivary gland transplant for alacrimia (5-yr) | Human clinical |
| [11340723](https://pubmed.ncbi.nlm.nih.gov/11340723/) | Prevention-centered oral management | Human case |
| [38081329](https://pubmed.ncbi.nlm.nih.gov/38081329/) | Bony CNLDO phenotype; Schirmer/TBUT | Human clinical |
| [41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/) | Variant spectrum; IGSF3 candidate modifier; 5p12 deletion | Human genotype-phenotype |
| [41409311](https://pubmed.ncbi.nlm.nih.gov/41409311/) | FGF10 LoF with EA, pulmonary hypoplasia (VACTERL overlap) | Human case |
| [37685309](https://pubmed.ncbi.nlm.nih.gov/37685309/) | Ultrasound of exocrine glands (diagnostic context) | Methods |

---

## Limitations and Knowledge Gaps

1. **No population epidemiology.** Prevalence/incidence are unknown; the evidence base is limited to ~20 complete-agenesis pediatric cases and scattered kindreds, precluding robust frequency, sex-ratio, or geographic estimates.
2. **Modifiers unexplained.** Incomplete penetrance and variable expressivity imply genetic/stochastic modifiers that remain uncharacterized; the role of candidate *IGSF3* variants is unresolved ([PMID: 41533940](https://pubmed.ncbi.nlm.nih.gov/41533940/)).
3. **Genotype–phenotype correlation is weak.** The same variant produces unilateral to bilateral disease within one family, so genotype poorly predicts severity.
4. **No disease-modifying therapy or trials.** No ClinicalTrials.gov interventions target the FGF10 axis in ALSG; ligand-restoration is untested.
5. **Human molecular profiling absent.** No transcriptomic/proteomic/metabolomic patient datasets exist; mechanism is inferred from mouse and ex vivo systems.
6. **No natural animal disease / OMIA entry** identified, limiting comparative pathology.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international ALSG/LADD registry** to aggregate genotype, phenotype laterality, penetrance, and natural-history data, enabling the first prevalence and genotype–phenotype estimates.
2. **Test *FGF10* modifier hypotheses** — sequence *IGSF3* and perform exome-wide modifier screens in penetrant vs non-penetrant carriers within multigenerational kindreds.
3. **Generate heterozygous *Fgf10* dosage mouse models** (and conditional epithelium/mesenchyme alleles) to quantify the gland-formation dosage threshold and phenotype laterality, directly modeling human haploinsufficiency.
4. **Patient-derived organoid/iPSC salivary and lacrimal gland models** to functionally classify missense VUS and screen FGF10-pathway agonists (recombinant FGF10, FGFR2b activators, heparanase modulators).
5. **Prospective evaluation of minor salivary gland transplantation** for alacrimia across more patients with standardized corneal and quality-of-life endpoints, building on the encouraging 5-year single-series result.
6. **Standardize a diagnostic algorithm** (scintigraphy + orbital/cervicofacial imaging + Schirmer/TBUT + *FGF10/FGFR2/FGFR3* sequencing) with explicit criteria to distinguish congenital ALSG from juvenile Sjögren disease.

---

*Report compiled from 11 confirmed findings and 21 reviewed papers over a 5-iteration autonomous investigation. Evidence source types are indicated throughout as human clinical/genetic, model organism, or ex vivo.*


## Artifacts

- [OpenScientist final report](Aplasia_of_Lacrimal_and_Salivary_Glands-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Aplasia_of_Lacrimal_and_Salivary_Glands-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008397` (2 mentions) - the report calls it "MONDO"; MONDO calls it **aplasia of lacrimal and salivary glands**
- `HP:0000217` (1 mention) - the report calls it "Symptom"; HP calls it **Xerostomia**
- `HP:0000670` (1 mention) - the report calls it "Clinical sign"; HP calls it **Carious teeth**
- `HP:0009746` (1 mention) - the report calls it "abnormal salivary gland morphology"; HP calls it **Thick nasal septum**
- `HP:0009926` (1 mention) - the report calls it "Symptom"; HP calls it **Epiphora**
- `HP:0000495` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent corneal erosions**
- `HP:0100580` (1 mention) - the report calls it "Clinical sign"; HP calls it **Barrett esophagus**
- `UBERON:0001833` (1 mention) - the report calls it "Sublingual gland"; UBERON calls it **lip**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000562` (2 mentions), reported as "abnormal lacrimal duct morphology", "Clinical sign" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000579` (1 mention) - the report calls it "abnormal nasolacrimal system"; HP calls it **Nasolacrimal duct obstruction**
- `GO:0060442` (2 mentions) - the report calls it "branching involved in salivary gland morphogenesis"; GO calls it **branching involved in prostate gland morphogenesis**
- `GO:0008543` (1 mention) - the report calls it "FGF receptor signaling pathway"; GO calls it **fibroblast growth factor receptor signaling pathway**, and lists "FGF receptor signaling pathway" among its other names
- `GO:0070374` (1 mention) - the report calls it "positive regulation of ERK1/ERK2 cascade"; GO calls it **positive regulation of ERK1 and ERK2 cascade**, and lists "positive regulation of ERK1/2 cascade" among its other names
- `CL:0000134` (1 mention) - the report calls it "mesenchymal cell"; CL calls it **mesenchymal stem cell**
- `UBERON:0001091` (1 mention) - the report calls it "Teeth"; UBERON calls it **calcareous tooth**, and lists "tooth" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000562` - called "abnormal lacrimal duct morphology", "Clinical sign"