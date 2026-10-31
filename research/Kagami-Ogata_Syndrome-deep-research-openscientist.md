---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:43:16.697932'
end_time: '2026-10-24T16:00:05.056681'
duration_seconds: 1008.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Kagami-Ogata Syndrome
  mondo_id: MONDO:0016779
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 16
  validator_version: 0.4.0
term_validation:
  total_terms: 35
  verified: 30
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 3
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: CL:0000115
    reported_labels:
    - Tissue/cell:** placental **villous vascular endothelial cells
    ontology_label: endothelial cell
  - term_id: HP:0000889
    reported_labels:
    - Coat-hanger rib configuration
    ontology_label: Abnormal clavicle morphology
  - term_id: HP:0001520
    reported_labels:
    - Birth overgrowth / high birth weight
    ontology_label: Large for gestational age
  - term_id: HP:0000271
    reported_labels:
    - Distinctive face (full cheeks, protruding philtrum, depressed nasal bridge)
    ontology_label: Abnormality of the face
  - term_id: HP:0001537
    reported_labels:
    - Abdominal wall defect (omphalocele, diastasis recti)
    ontology_label: Umbilical hernia
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0006349
    ontology_label: obsolete regulation of gene expression by genomic imprinting
    replaced_by: GO:0071514
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
  path: Kagami-Ogata_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Kagami-Ogata_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kagami-Ogata Syndrome
- **MONDO ID:** MONDO:0016779 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Kagami-Ogata Syndrome** covering all of the
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

# Kagami-Ogata Syndrome (KOS14): A Comprehensive Disease Characterization Report

**MONDO ID:** MONDO:0016779 · **OMIM:** #608149 · **Orphanet:** ORPHA:97570 (UPD(14)pat) · **Category:** Mendelian / genomic-imprinting disorder

---

## Summary

**Kagami-Ogata syndrome (KOS) is not caused by a classical single-gene mutation but by an imbalance of genomic imprinting at the chromosome 14q32.2 DLK1-MEG3 (DLK1-DIO3) imprinted cluster.** The disease results from a **net excess of paternally expressed genes — chiefly the retrotransposon-derived gene RTL1/PEG11 and DLK1 — with concomitant loss of maternally expressed non-coding RNAs** (MEG3/GTL2, the RTL1 antisense transcript RTL1as, MEG8, and clustered miRNAs/snoRNAs). There is therefore no single "causal gene" in the Mendelian sense; rather, the disease is defined by the dosage of an imprinted gene cluster. Among the imprinted genes, **RTL1 overdosage is the principal driver** of the characteristic phenotype, with DLK1 contributing to the growth and metabolic features.

Three distinct molecular mechanisms converge on the same lesion — a "double dose paternal / zero dose maternal" state at 14q32.2: **paternal uniparental disomy of chromosome 14 (upd(14)pat, ~65%), maternally-derived microdeletions (~19%), and epimutations (hypermethylation of the IG-DMR/MEG3-DMR, ~15%)**. The clinical result is a pathognomonic gestalt: a small, bell-shaped thorax with "coat-hanger" angled ribs, a distinctive face (full cheeks, protruding philtrum, depressed nasal bridge), abdominal wall defects, polyhydramnios, placentomegaly, and birth overgrowth. Postnatally, severe respiratory insufficiency from the constricted thorax dominates the course and drives a poor prognosis; survivors have universal developmental delay (median IQ/DQ ~55) and an elevated (~8.8%) risk of hepatoblastoma.

KOS is the **molecular mirror image of Temple syndrome (TS14)**, which arises from the reciprocal dosage state (maternal UPD / paternal deletion or hypomethylation). The dosage mechanism is validated across species by mouse models (Rtl1 and miR-127 knockouts) and by the naturally occurring ovine **callipyge** muscular-hypertrophy phenotype, both of which demonstrate that gene dosage at this cluster — not coding mutation — is the pathogenic variable. No disease-modifying therapy exists; diagnosis relies on recognizing the radiographic gestalt confirmed by methylation/UPD/CNV testing, and management is supportive.

---

## Key Findings

### Finding 1 — KOS is caused by excess paternal / absent maternal gene dosage at the 14q32.2 DLK1-MEG3 imprinted locus

The foundational finding of this investigation is that **KOS is a genomic-imprinting disorder rather than a conventional coding-variant disease**. Three molecular mechanisms all produce the same functional endpoint — overexpression of paternally-expressed genes and silence of maternally-expressed non-coding RNAs at 14q32.2:

1. **Paternal uniparental disomy 14 (upd(14)pat)** — two paternal copies, no maternal copy.
2. **Maternal-origin microdeletions** — loss of the maternal allele/DMR.
3. **Epimutations** — aberrant hypermethylation of the maternally-inherited IG-DMR (MEG3/DLK1:IG-DMR) and MEG3:TSS-DMR, silencing the maternal program.

In a cohort of 26 patients with the UPD(14)pat-like phenotype, the relative frequencies were **upd(14)pat 65.4% (17/26), microdeletions 19.2% (5/26), and epimutations 15.4% (4/26)** ([PMID: 22353941](https://pubmed.ncbi.nlm.nih.gov/22353941/)): *"we identified UPD(14)pat in 17 patients (65.4%), microdeletions of different patterns in 5 patients (19.2%), and epimutations in 4 patients (15.4%)."*

The mechanistic through-line is **RTL1 overexpression**. When the maternally expressed RTL1as (antisense) transcript — which encodes microRNAs that repress RTL1 — is lost, RTL1 is de-repressed. RTL1 placental expression was **~5× control** in patient placentas ([PMID: 22917972](https://pubmed.ncbi.nlm.nih.gov/22917972/)): *"RTL1 expression level was about five times higher in the placental samples of the two patients than in control placental samples"*, and ~2.5× in body tissues. A review concluded that *"excessive RTL1 expression and absent MEG expression constitute the primary underlying fact"* ([PMID: 26377239](https://pubmed.ncbi.nlm.nih.gov/26377239/)).

| Molecular mechanism | Frequency | Net effect at 14q32.2 |
|---|---|---|
| Paternal UPD14 (upd(14)pat) | ~65% | 2× paternal, 0× maternal |
| Maternal microdeletion | ~19% | Loss of maternal DMR/genes |
| Epimutation (IG-DMR/MEG3-DMR hypermethylation) | ~15% | Maternal allele epigenetically silenced |

### Finding 2 — KOS has a pathognomonic clinical gestalt with developmental delay and ~8.8% hepatoblastoma risk

In the landmark cohort of **34 molecularly-defined patients** (UPD(14)pat n=23, epimutations n=5, microdeletions n=6), the defining clinical features were a **distinctive face** (full cheeks, protruding philtrum) and an **increased coat-hanger rib angle** on chest X-ray with a small bell-shaped thorax ([PMID: 25689926](https://pubmed.ncbi.nlm.nih.gov/25689926/)). These two features together are considered pathognomonic and sufficient to prompt molecular confirmation.

Quantitatively:
- **Birth overgrowth:** median birth weight **+2.3 SD** (range +0.1 to +8.8 SD) — *"a median birth weight of +2.3 SD (range, +0.1 to +8.8 SD)"*.
- **Developmental delay:** *"developmental delay and/or intellectual disability was invariably present, with a median developmental/intellectual quotient of 55 (range, 29–70)"* — i.e., 100% penetrant with moderate severity.
- **Hepatoblastoma:** *"hepatoblastoma was identified in three infantile patients (8.8%)"* (3/34), paralleling the tumor predisposition of another imprinting disorder, Beckwith-Wiedemann syndrome.

Prenatally the syndrome presents with **polyhydramnios and placentomegaly** ([PMID: 25689926](https://pubmed.ncbi.nlm.nih.gov/25689926/), [PMID: 33179779](https://pubmed.ncbi.nlm.nih.gov/33179779/)). The postnatal course is dominated by **severe respiratory distress** from the restrictive small thorax ([PMID: 33179779](https://pubmed.ncbi.nlm.nih.gov/33179779/), [PMID: 34746047](https://pubmed.ncbi.nlm.nih.gov/34746047/)), which is the principal determinant of early mortality.

### Finding 3 — Mouse models confirm Rtl1 dosage as the driver; both overexpression and loss are lethal

The dosage model is directly supported by mouse genetics. **Rtl1 (Peg11)**, a retrotransposon-derived paternally expressed gene on mouse chromosome 12 (syntenic to human 14q32), is essential for maintenance of fetal capillaries at the feto-maternal interface. Critically, **both its loss and its overproduction cause late-fetal/neonatal lethality** ([PMID: 18176565](https://pubmed.ncbi.nlm.nih.gov/18176565/)): *"both its loss and its overproduction cause late-fetal and/or neonatal lethality in mice"* — the clearest demonstration that this gene is exquisitely dosage-sensitive, recapitulating KOS lethality.

The repressor arm is equally informative: **miR-127**, processed from the maternally expressed Rtl1as antisense transcript, is an essential trans-acting repressor of Rtl1. **miR-127 knockout mice exhibit placentomegaly** with labyrinthine-zone defects and increased Rtl1 transcript/protein ([PMID: 26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/)): *"The miR-127 knockout mice exhibit placentomegaly with specific defects within the labyrinthine zone involved in maternal-fetal nutrient transfer"* — directly linking loss of the maternal microRNA repressor to the placentomegaly hallmark of KOS. Mouse chromosome 12qF1 is strongly syntenic to human 14q32 ([PMID: 32592473](https://pubmed.ncbi.nlm.nih.gov/32592473/)).

### Finding 4 — Diagnosis rests on the radiographic gestalt confirmed by methylation/UPD/CNV testing; management is supportive

Prenatal clues that should trigger investigation are **severe polyhydramnios + small bell-shaped thorax + protuberant abdomen + dysmorphic face** ([PMID: 33179779](https://pubmed.ncbi.nlm.nih.gov/33179779/)). Confirmatory molecular testing uses a tiered approach:
- **Methylation-specific MLPA (MS-MLPA)** of the IG-DMR/MEG3-DMR and methylation-specific PCR;
- **SNP microarray** and microsatellite/UPD analysis (to detect upd(14)pat);
- **Karyotype/FISH** to detect Robertsonian translocations predisposing to UPD;
- **CNV-seq** for microdeletions.

*"Prenatal diagnosis using methylation-specific multiplex ligation-dependent probe amplification (MLPA) or a single-nucleotide polymorphism-based microarray analysis is recommended"* ([PMID: 34746047](https://pubmed.ncbi.nlm.nih.gov/34746047/); see also [PMID: 36035167](https://pubmed.ncbi.nlm.nih.gov/36035167/), [PMID: 32211354](https://pubmed.ncbi.nlm.nih.gov/32211354/)).

There is **no disease-modifying therapy**. Management is supportive: mechanical ventilation/tracheostomy for respiratory insufficiency, surgical repair of abdominal wall defects (omphalocele/diastasis recti), feeding support, developmental/physical therapy, and **periodic hepatoblastoma surveillance (serum AFP + abdominal ultrasound)** ([PMID: 25689926](https://pubmed.ncbi.nlm.nih.gov/25689926/), [PMID: 31853915](https://pubmed.ncbi.nlm.nih.gov/31853915/)): *"These findings suggest the necessity of an adequate support for developmental delay and periodical screening for hepatoblastoma in the affected patients."*

### Finding 5 — KOS is the molecular mirror image of Temple syndrome; DLK1 dosage links the locus to growth, puberty, and metabolism

KOS and **Temple syndrome (TS14)** are reciprocal imprinting disorders of the identical cluster ([PMID: 32592473](https://pubmed.ncbi.nlm.nih.gov/32592473/)): *"Temple syndrome (TS) and Kagami-Ogata syndrome (KOS) are imprinting disorders caused by absence or overexpression of genes within a single imprinted cluster on human chromosome 14q32."* TS14 arises from maternal UPD14 / paternal deletion or hypomethylation (the *opposite* dosage state), and presents with growth restriction, hypotonia, small hands/feet, and precocious puberty.

The locus encodes **paternally expressed DLK1, RTL1, DIO3** and **maternally expressed lncRNAs MEG3/GTL2, RTL1as, MEG8** plus clustered miRNAs/snoRNAs. **DLK1 is dosage-sensitive**: loss-of-function causes central precocious puberty with obesity and metabolic derangement ([PMID: 36577869](https://pubmed.ncbi.nlm.nih.gov/36577869/), [PMID: 31460623](https://pubmed.ncbi.nlm.nih.gov/31460623/)): *"DLK1 is an imprinted gene, whose mutations have been described as a rare cause of CPP in girls and adult women with precocious menarche, obesity and metabolic derangement."* By inference, the DLK1 *over*expression in KOS contributes to its growth/metabolic phenotype — the dosage-opposite of the DLK1-loss phenotype.

### Finding 6 — The IG-DMR is the master imprinting control element; KOS placental pathology localizes to villous endothelial cells and pericytes

The **IG-DMR is the master maternal-allele imprinting control center**. In mouse, deletion of the IG-DMR from the maternally inherited chromosome causes **bidirectional loss of imprinting of all genes in the cluster**, whereas paternal transmission of the same deletion leaves imprinting unchanged ([PMID: 12937418](https://pubmed.ncbi.nlm.nih.gov/12937418/)): *"deletion of the IG-DMR from the maternally inherited chromosome causes bidirectional loss of imprinting of all genes in the cluster."* This explains why epimutations of the maternal IG-DMR in KOS recapitulate the full molecular phenotype.

KOS placental pathology has a specific **cellular localization**: terminal villi show swollen vascular endothelial cells and hypertrophic pericytes with narrowed capillary lumens, and DLK1, RTL1, and DIO3 proteins localize specifically to vascular endothelial cells and pericytes, with staining intensity tracking gene dosage ([PMID: 22917972](https://pubmed.ncbi.nlm.nih.gov/22917972/)): *"Terminal villi were associated with swollen vascular endothelial cells and hypertrophic pericytes, together with narrowed capillary lumens."* Mouse uniparental-disomy studies link Dlk1/Gtl2 dosage to skeletal muscle maturation, bone formation, and placental defects ([PMID: 17449025](https://pubmed.ncbi.nlm.nih.gov/17449025/)). Notably, **epimutation cases can be milder**, sometimes with near-normal development, reflecting mosaic methylation ([PMID: 35953028](https://pubmed.ncbi.nlm.nih.gov/35953028/)).

### Finding 7 — The ovine callipyge phenotype is a naturally occurring DLK1-DIO3 imprinting disorder that validates the dosage mechanism

In sheep (*Ovis aries*), the **callipyge (CLPG)** phenotype — postnatal muscular hypertrophy — is caused by a single **A→G SNP in a muscle-specific long-range control element** within the DLK1-GTL2 intergenic (IG) region. The mutation up-regulates paternally expressed DLK1/RTL1 and maternal ncRNAs **in cis without altering imprinting status** ([PMID: 24990181](https://pubmed.ncbi.nlm.nih.gov/24990181/), [PMID: 16690740](https://pubmed.ncbi.nlm.nih.gov/16690740/)): *"A single nucleotide polymorphism in the DLK1-DIO3 imprinted gene cluster alters gene expression of the paternal allele-specific protein-coding genes and several maternal allele-specific long noncoding RNA and microRNA when the mutation is inherited in cis."*

Callipyge displays **non-Mendelian polar overdominance** (hypertrophy only in +mat/CLPGpat heterozygotes), explained by trans-inhibition of DLK1 by maternally expressed miRNAs (miR-379/miR-544 cluster, including miR-329) ([PMID: 26487685](https://pubmed.ncbi.nlm.nih.gov/26487685/), [PMID: 20944086](https://pubmed.ncbi.nlm.nih.gov/20944086/)). Crucially, **DLK1 and RTL1 — not MEG3/MEG8 — drive the muscle gene-expression changes** ([PMID: 19816583](https://pubmed.ncbi.nlm.nih.gov/19816583/)): *"The muscle-specific expression patterns of most genes were similar to DLK1 and included genes that are transcriptional repressors or affect feedback mechanisms in beta-adrenergic and growth factor signaling pathways."* This natural model independently confirms that DLK1/RTL1 overdosage drives musculoskeletal reprogramming, the same mechanistic axis implicated in KOS.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. INITIATING LESION at 14q32.2 (one of three):
   (a) upd(14)pat (~65%)  |  (b) maternal microdeletion (~19%)  |  (c) IG-DMR/MEG3-DMR hypermethylation / epimutation (~15%)
        |
        v
2. LEADS TO loss of the maternally expressed non-coding program
   (MEG3/GTL2, RTL1as, MEG8, miRNA/snoRNA clusters incl. miR-127)
        |
        v
3. RESULTS IN de-repression / overdosage of paternally expressed genes
   — principally RTL1 (~5x placenta, ~2.5x soma) and DLK1; also DIO3
        |
        +-----------------------------+-----------------------------+
        v                             v                             v
4a. RTL1 overdose in villous      4b. DLK1 overdose in            4c. RTL1/DLK1 overdose in
    endothelium & pericytes           mesoderm-derived tissues         developing muscle/bone
        |                             |  (Notch/Delta signaling)        |
        v                             v                             v
5a. Swollen endothelium,          5b. Altered growth signaling    5c. Thoracic / rib
    hypertrophic pericytes,           -> birth overgrowth              dysplasia -> small
    narrowed capillaries ->           (+2.3 SD), metabolic             bell-shaped thorax,
    PLACENTOMEGALY + feto-            derangement (inferred            "coat-hanger" ribs
    maternal transfer defect          from DLK1 dosage biology)        |
        |                                                              v
        v                                                      6. LEADS TO restrictive
   POLYHYDRAMNIOS (prenatal)                                      lung physiology ->
                                                                  SEVERE NEONATAL
                                                                  RESPIRATORY DISTRESS
                                                                      |
                                                                      v
                                                              7. PRINCIPAL DRIVER OF
                                                                 EARLY MORTALITY
   Parallel downstream branches:
   - CNS effects -> universal developmental delay / ID (median IQ ~55)
   - Liver -> hepatoblastoma predisposition (~8.8%) [mechanism inferred, shared with BWS]
   - Abdominal wall -> omphalocele / diastasis recti
   - Facial mesenchyme -> distinctive face (full cheeks, protruding philtrum)
```

**Upstream vs downstream.** The upstream, proximal event is always a change in *dosage/imprinting state* at 14q32.2 (not a coding mutation). The master control point is the **IG-DMR**, whose maternal methylation state governs the entire cluster ([PMID: 12937418](https://pubmed.ncbi.nlm.nih.gov/12937418/)). Immediately downstream is the loss of maternal ncRNAs (especially the RTL1as-derived miR-127) and consequent **RTL1/DLK1 protein overdosage**. The most distal manifestations — respiratory failure, developmental delay, hepatoblastoma — are tissue-specific consequences of this overdosage.

**Cell types and processes.** Documented cellular targets are **villous vascular endothelial cells (CL:0000115)** and **pericytes (CL:0000669)** in the placenta ([PMID: 22917972](https://pubmed.ncbi.nlm.nih.gov/22917972/)), with **skeletal muscle (CL:0000188)** and bone-forming cells implicated by cross-species and UPD-mouse data. Relevant biological processes include **genomic imprinting (GO:0071514)**, **regulation of gene expression by genomic imprinting (GO:0006349)**, **Notch signaling pathway (GO:0007219)** (DLK1 is a Notch/Delta-family modulator), **placenta development (GO:0001890)**, and **negative regulation of gene expression by miRNA (GO:0035195)**.

**Key chemical/molecular entities.** 5-methylcytosine (CHEBI:27551) at the DMRs is the central epigenetic mark; serum **alpha-fetoprotein** is the hepatoblastoma surveillance marker.

### Cross-species validation table

| System | Lesion | Phenotype | Mechanistic lesson | PMID |
|---|---|---|---|---|
| Human KOS | upd(14)pat / del / epimutation | Coat-hanger ribs, respiratory failure, DD, hepatoblastoma | Paternal-excess dosage is pathogenic | [25689926](https://pubmed.ncbi.nlm.nih.gov/25689926/) |
| Human TS14 | mat UPD / pat del / hypomethylation | Growth restriction, precocious puberty | Reciprocal/mirror dosage | [32592473](https://pubmed.ncbi.nlm.nih.gov/32592473/) |
| Mouse Rtl1 | Loss **or** overexpression | Fetal/neonatal lethality | Rtl1 is dosage-sensitive | [18176565](https://pubmed.ncbi.nlm.nih.gov/18176565/) |
| Mouse miR-127 KO | Loss of maternal repressor | Placentomegaly, ↑Rtl1 | Maternal miRNA restrains Rtl1 | [26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/) |
| Sheep callipyge | cis IG SNP | Muscle hypertrophy (polar overdominance) | DLK1/RTL1 overdosage reprograms muscle | [24990181](https://pubmed.ncbi.nlm.nih.gov/24990181/), [19816583](https://pubmed.ncbi.nlm.nih.gov/19816583/) |

---

## Section-by-Section Report

### 1. Disease Information
KOS14 is a rare congenital genomic-imprinting disorder of chromosome 14q32.2, first described clinically by Wang et al. in 1991. **Identifiers:** OMIM #608149; MONDO:0016779; Orphanet ORPHA:97570 ("Paternal uniparental disomy of chromosome 14"). **Synonyms:** Kagami-Ogata syndrome; UPD(14)pat syndrome; paternal uniparental disomy 14 syndrome; "coat-hanger rib" syndrome. The knowledge base here is **aggregated disease-level** evidence drawn from published molecularly-defined cohorts (the 34-patient Kagami-Ogata cohort, [PMID: 25689926](https://pubmed.ncbi.nlm.nih.gov/25689926/)) and case series/reports ([PMID: 34055463](https://pubmed.ncbi.nlm.nih.gov/34055463/)), not individual EHR data.

### 2. Etiology
**Primary cause:** genetic/epigenetic imbalance (not environmental or infectious). Three mechanisms — upd(14)pat (~65%), maternal microdeletion (~19%), epimutation (~15%) ([PMID: 22353941](https://pubmed.ncbi.nlm.nih.gov/22353941/)). **Genetic risk factor:** Robertsonian translocations (e.g., ROB 13;14) predispose to upd(14)pat through trisomy/monosomy rescue ([PMID: 32211354](https://pubmed.ncbi.nlm.nih.gov/32211354/)). **Environmental/lifestyle/infectious factors:** none established. **Protective factors:** none known; however, **mosaic/partial epimutation** attenuates severity ([PMID: 35953028](https://pubmed.ncbi.nlm.nih.gov/35953028/)). **Gene-environment interactions:** none documented; this is a predominantly genetic/epigenetic disorder.

### 3. Phenotypes
| Phenotype | HPO suggestion | Type | Onset | Frequency / severity |
|---|---|---|---|---|
| Bell-shaped/small thorax | HP:0001591 / HP:0005257 | Physical/skeletal | Prenatal–neonatal | Near-universal; pathognomonic |
| Coat-hanger rib configuration | HP:0000889 | Radiographic sign | Neonatal | Pathognomonic |
| Neonatal respiratory distress | HP:0002643 | Clinical sign | Neonatal | Very frequent; severe |
| Polyhydramnios | HP:0001561 | Prenatal sign | Prenatal | Frequent |
| Placentomegaly | HP:0100767 | Physical | Prenatal | Frequent |
| Birth overgrowth / high birth weight | HP:0001520 | Physical | Congenital | Median +2.3 SD |
| Developmental delay / intellectual disability | HP:0001263 / HP:0001249 | Behavioral/cognitive | Childhood | **100%**, median IQ ~55 |
| Distinctive face (full cheeks, protruding philtrum, depressed nasal bridge) | HP:0000271 | Physical | Congenital | Frequent |
| Abdominal wall defect (omphalocele, diastasis recti) | HP:0001537 | Physical | Congenital | Frequent |
| Muscular hypotonia | HP:0001252 | Clinical sign | Neonatal | Frequent |
| Hepatoblastoma | HP:0002884 | Neoplasm | Infancy | ~8.8% |

Evidence: [PMID: 25689926](https://pubmed.ncbi.nlm.nih.gov/25689926/), [PMID: 33179779](https://pubmed.ncbi.nlm.nih.gov/33179779/), [PMID: 31853915](https://pubmed.ncbi.nlm.nih.gov/31853915/). **Quality of life:** severely impacted by respiratory dependence (ventilation/tracheostomy), feeding difficulties, and intellectual disability requiring lifelong special-needs support.

### 4. Genetic / Molecular Information
**Locus:** 14q32.2 DLK1-DIO3 (DLK1-MEG3) imprinted cluster. **Paternally expressed:** DLK1 (HGNC:2907), RTL1/PEG11, DIO3 (HGNC:2885). **Maternally expressed (lost in KOS):** MEG3/GTL2 (HGNC:14575), RTL1as, MEG8, and clustered miRNAs (incl. miR-127 / miR-379–miR-544) and snoRNAs. **Variant classes:** structural (UPD, microdeletions) and epigenetic (DMR hypermethylation) — classic coding SNVs are *not* the usual mechanism. **Functional consequence:** gene dosage gain (overexpression) of paternal genes + loss of maternal ncRNA repression. **Epigenetics:** aberrant hypermethylation of the maternal IG-DMR (MEG3/DLK1:IG-DMR) and MEG3:TSS-DMR, the master and secondary control regions ([PMID: 12937418](https://pubmed.ncbi.nlm.nih.gov/12937418/), [PMID: 35953028](https://pubmed.ncbi.nlm.nih.gov/35953028/)). **Chromosomal abnormalities:** Robertsonian translocations predisposing to upd(14)pat ([PMID: 32211354](https://pubmed.ncbi.nlm.nih.gov/32211354/)).

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are established. KOS is a constitutional (epi)genetic disorder.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full ordered causal chain. In brief: imprinting imbalance at 14q32.2 → loss of maternal ncRNAs (esp. RTL1as/miR-127) → RTL1 and DLK1 overdosage → endothelial/pericyte pathology (placentomegaly, polyhydramnios) + musculoskeletal dysplasia (coat-hanger ribs, small thorax) → restrictive respiratory failure, plus CNS (developmental delay) and hepatic (hepatoblastoma) branches. DLK1 acts in the Notch/Delta developmental-signaling axis; RTL1 is a retrotransposon-derived gene essential for fetal capillary maintenance.

### 7. Anatomical Structures Affected
- **Organ/system (primary):** thoracic skeleton/ribs (UBERON:0002228 rib; UBERON:0000915 thoracic segment), lungs (UBERON:0002048) — restrictive physiology; placenta (UBERON:0001987). **Secondary:** liver (UBERON:0002107, hepatoblastoma); CNS/brain (UBERON:0000955, developmental delay); abdominal wall (UBERON:0003697).
- **Tissue/cell:** placental **villous vascular endothelial cells (CL:0000115)** and **pericytes (CL:0000669)** ([PMID: 22917972](https://pubmed.ncbi.nlm.nih.gov/22917972/)); skeletal muscle (CL:0000188); bone-forming cells.
- **Subcellular:** nucleus (GO:0005634) — site of imprinting control/methylation; plasma membrane (DLK1 is a transmembrane protein).
- **Lateralization:** bilateral/symmetric skeletal involvement.

### 8. Temporal Development
**Onset:** congenital; often detectable prenatally (polyhydramnios, small thorax, placentomegaly on ultrasound, [PMID: 33179779](https://pubmed.ncbi.nlm.nih.gov/33179779/)). **Pattern:** chronic, non-episodic. **Course:** the critical period is the **neonatal interval**, when respiratory insufficiency determines survival; survivors have a static-to-slowly-evolving course with persistent developmental delay. Hepatoblastoma risk is concentrated in **infancy**. No spontaneous remission; lifelong condition.

### 9. Inheritance and Population
**Prevalence/incidence:** unknown/unrecorded — >80 cases reported in the literature; likely underdiagnosed ([PMID: 34055463](https://pubmed.ncbi.nlm.nih.gov/34055463/), [PMID: 31853915](https://pubmed.ncbi.nlm.nih.gov/31853915/)). **Inheritance:** usually sporadic (de novo UPD or epimutation); microdeletion and translocation-associated cases can recur in families, warranting genetic counseling. **Penetrance:** developmental delay effectively 100% in classic molecular cases; **expressivity variable** (epimutation/mosaic cases milder, [PMID: 35953028](https://pubmed.ncbi.nlm.nih.gov/35953028/)). **Founder effects / carrier frequency / ethnic predilection:** none established. **Sex ratio:** no strong skew documented (both male and female cases reported).

### 10. Diagnostics
**Imaging:** chest X-ray showing coat-hanger ribs + small bell-shaped thorax is the key diagnostic sign; prenatal ultrasound shows polyhydramnios, narrow thorax, protuberant abdomen, placentomegaly. **Confirmatory molecular testing (tiered):** MS-MLPA and methylation-specific PCR of IG-DMR/MEG3-DMR; SNP microarray; microsatellite/UPD analysis; karyotype/FISH (Robertsonian translocations); CNV-seq for microdeletions ([PMID: 34746047](https://pubmed.ncbi.nlm.nih.gov/34746047/), [PMID: 36035167](https://pubmed.ncbi.nlm.nih.gov/36035167/), [PMID: 32211354](https://pubmed.ncbi.nlm.nih.gov/32211354/)). **Biomarker surveillance:** serum AFP for hepatoblastoma. **Differential diagnosis:** Beckwith-Wiedemann syndrome (overgrowth + hepatoblastoma), other skeletal dysplasias with small thorax, Pena-Shokeir phenotype; the coat-hanger rib sign distinguishes KOS.

### 11. Outcome / Prognosis
**Overall prognosis is poor**, driven by neonatal respiratory insufficiency ([PMID: 34055463](https://pubmed.ncbi.nlm.nih.gov/34055463/)). Survivors have **universal developmental delay (median IQ/DQ ~55)** and require long-term ventilatory, feeding, and developmental support. **Hepatoblastoma (~8.8%)** is a key complication requiring surveillance. Milder epimutation/mosaic cases can have near-normal development and better outcomes ([PMID: 35953028](https://pubmed.ncbi.nlm.nih.gov/35953028/)). No validated prognostic biomarkers beyond molecular subtype (epimutation/mosaic → generally milder).

### 12. Treatment
**No disease-modifying therapy exists.** Management is entirely **supportive** (NCIT: Supportive Care):
- **Respiratory:** mechanical ventilation, tracheostomy for chronic respiratory insufficiency.
- **Surgical:** repair of abdominal wall defects (omphalocele/diastasis recti); hepatectomy if hepatoblastoma arises ([PMID: 23181499](https://pubmed.ncbi.nlm.nih.gov/23181499/)).
- **Nutrition/feeding support;** developmental/physical/occupational/speech therapy.
- **Oncologic surveillance:** AFP + abdominal ultrasound.

No pharmacotherapy, gene therapy, or RNA-based therapy is approved. (Note: growth hormone benefits the *reciprocal* disorder, Temple syndrome, [PMID: 30836360](https://pubmed.ncbi.nlm.nih.gov/30836360/) — not applicable to KOS, where overgrowth is the phenotype.)

### 13. Prevention
No primary prevention exists (sporadic de novo origin in most cases). **Secondary prevention:** prenatal recognition of the ultrasound gestalt enabling molecular confirmation and informed pregnancy/postnatal planning ([PMID: 33179779](https://pubmed.ncbi.nlm.nih.gov/33179779/)). **Tertiary prevention:** hepatoblastoma surveillance; respiratory support to prevent complications. **Genetic counseling** is indicated, especially for translocation- or deletion-associated familial recurrence risk.

### 14. Other Species / Natural Disease
The orthologous cluster is conserved in mouse (chr12qF1) and sheep. The **ovine callipyge** phenotype (*Ovis aries*, NCBI Taxon 9940) is a naturally occurring DLK1-DIO3 imprinting disorder of veterinary/agricultural relevance, producing muscular hypertrophy via cis up-regulation of DLK1/RTL1 ([PMID: 24990181](https://pubmed.ncbi.nlm.nih.gov/24990181/), [PMID: 19816583](https://pubmed.ncbi.nlm.nih.gov/19816583/)). Orthologous genes: mouse *Rtl1/Peg11*, *Dlk1*, *Dio3*. The conservation of imprinting and dosage sensitivity across sheep, mouse, and human demonstrates deep evolutionary conservation of the mechanism.

### 15. Model Organisms
- **Mouse (NCBI Taxon 10090):** *Rtl1* knockout and overexpression (both lethal, [PMID: 18176565](https://pubmed.ncbi.nlm.nih.gov/18176565/)); **miR-127 knockout** (placentomegaly, [PMID: 26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/)); **IG-DMR deletion** (imprinting control, [PMID: 12937418](https://pubmed.ncbi.nlm.nih.gov/12937418/)); **uniparental disomy chr12** (muscle/bone/placenta defects, [PMID: 17449025](https://pubmed.ncbi.nlm.nih.gov/17449025/)); miR-379/miR-544 cluster knockout (muscle hypertrophy, [PMID: 26487685](https://pubmed.ncbi.nlm.nih.gov/26487685/)). **Phenotype recapitulation:** strong for placentomegaly, dosage-lethality, and musculoskeletal effects. **Limitation:** no single mouse fully reproduces the complete human KOS gestalt (e.g., coat-hanger ribs).
- **Sheep:** callipyge as a natural dosage model (muscle-specific).

---

## Evidence Base

| PMID | Role in this report | Key supporting quote |
|---|---|---|
| [22353941](https://pubmed.ncbi.nlm.nih.gov/22353941/) | Mechanism frequencies | "UPD(14)pat in 17 patients (65.4%), microdeletions ... 5 patients (19.2%), and epimutations in 4 patients (15.4%)" |
| [26377239](https://pubmed.ncbi.nlm.nih.gov/26377239/) | Primary molecular cause | "excessive RTL1 expression and absent MEG expression constitute the primary underlying fact" |
| [22917972](https://pubmed.ncbi.nlm.nih.gov/22917972/) | RTL1 dosage + placental cell pathology | "RTL1 expression level was about five times higher..."; "swollen vascular endothelial cells and hypertrophic pericytes" |
| [25689926](https://pubmed.ncbi.nlm.nih.gov/25689926/) | Clinical gestalt, DD, hepatoblastoma | "developmental delay ... invariably present ... median ... quotient of 55"; "hepatoblastoma ... three infantile patients (8.8%)"; "+2.3 SD" |
| [18176565](https://pubmed.ncbi.nlm.nih.gov/18176565/) | Rtl1 dosage-lethality | "both its loss and its overproduction cause late-fetal and/or neonatal lethality in mice" |
| [26138477](https://pubmed.ncbi.nlm.nih.gov/26138477/) | miR-127 repressor | "miR-127 knockout mice exhibit placentomegaly with specific defects within the labyrinthine zone" |
| [12937418](https://pubmed.ncbi.nlm.nih.gov/12937418/) | IG-DMR as master control | "deletion of the IG-DMR from the maternally inherited chromosome causes bidirectional loss of imprinting" |
| [32592473](https://pubmed.ncbi.nlm.nih.gov/32592473/) | TS14/KOS mirror model | "imprinting disorders caused by absence or overexpression of genes within a single imprinted cluster on ... 14q32" |
| [36577869](https://pubmed.ncbi.nlm.nih.gov/36577869/) | DLK1 dosage biology | "DLK1 is an imprinted gene, whose mutations have been described as a rare cause of CPP ... obesity and metabolic derangement" |
| [34746047](https://pubmed.ncbi.nlm.nih.gov/34746047/) | Diagnostic approach | "Prenatal diagnosis using methylation-specific ... MLPA or a single-nucleotide polymorphism-based microarray ... is recommended" |
| [24990181](https://pubmed.ncbi.nlm.nih.gov/24990181/) | Callipyge cis dosage | "A single nucleotide polymorphism in the DLK1-DIO3 imprinted gene cluster alters gene expression..." |
| [19816583](https://pubmed.ncbi.nlm.nih.gov/19816583/) | DLK1/RTL1 drive muscle reprogramming | "muscle-specific expression patterns of most genes were similar to DLK1 ..." |

Supporting case/series literature: [PMID: 33179779](https://pubmed.ncbi.nlm.nih.gov/33179779/), [PMID: 34055463](https://pubmed.ncbi.nlm.nih.gov/34055463/), [PMID: 31853915](https://pubmed.ncbi.nlm.nih.gov/31853915/), [PMID: 32211354](https://pubmed.ncbi.nlm.nih.gov/32211354/), [PMID: 36035167](https://pubmed.ncbi.nlm.nih.gov/36035167/), [PMID: 23181499](https://pubmed.ncbi.nlm.nih.gov/23181499/), [PMID: 35953028](https://pubmed.ncbi.nlm.nih.gov/35953028/), [PMID: 25656753](https://pubmed.ncbi.nlm.nih.gov/25656753/).

---

## Limitations and Knowledge Gaps

1. **Epidemiology is unquantified.** True prevalence/incidence of KOS is unknown; the disorder is rare (>80 reported cases) and probably underdiagnosed. Sex ratio, geographic distribution, and carrier frequencies are not established.
2. **Relative contribution of RTL1 vs DLK1.** While RTL1 overdosage is identified as the primary driver, the precise, tissue-specific contribution of DLK1, DIO3, and lost maternal ncRNAs to each phenotype (ribs vs CNS vs liver) is not fully dissected in humans.
3. **Hepatoblastoma mechanism is inferred.** The ~8.8% risk is well documented, but the molecular link between 14q32.2 dosage and hepatoblastomagenesis is extrapolated from the shared imprinting-disorder biology with Beckwith-Wiedemann syndrome rather than directly demonstrated.
4. **Genotype–phenotype correlation is incomplete.** Epimutation/mosaic cases are milder, but predictors of severity (methylation level, tissue mosaicism distribution) are not standardized.
5. **No mouse model fully recapitulates the human gestalt**, limiting mechanistic study of specific features such as coat-hanger ribs.
6. **No therapeutics pipeline.** There are no disease-modifying treatments, and no clinical trials were identified; the imprinting nature of the disorder makes classical gene-replacement approaches conceptually difficult.
7. **This report is literature-derived.** No primary patient-level dataset was analyzed; findings rest on published cohorts and case reports (aggregated disease-level evidence).

---

## Proposed Follow-up Experiments / Actions

1. **Establish a KOS registry** to quantify prevalence, incidence, survival, and genotype-stratified outcomes — directly addressing the epidemiology gap.
2. **Standardize methylation-based severity prediction:** correlate quantitative IG-DMR/MEG3-DMR methylation (and tissue mosaic ratio) with respiratory severity and DQ/IQ to build a prognostic model for epimutation cases ([PMID: 35953028](https://pubmed.ncbi.nlm.nih.gov/35953028/)).
3. **Dissect RTL1 vs DLK1 contributions** using tissue-specific conditional mouse overexpression (rib/thorax, CNS, hepatocyte) to attribute individual phenotypes to specific gene overdosage.
4. **Interrogate the hepatoblastoma mechanism** via molecular profiling (transcriptomics/methylomics) of KOS-associated tumors vs sporadic hepatoblastoma to test the shared-imprinting hypothesis.
5. **Explore allele-specific epigenetic editing** (e.g., CRISPR-dCas9 demethylation targeting the hypermethylated maternal IG-DMR in epimutation cases) as a proof-of-concept corrective strategy in patient-derived iPSC/organoid models.
6. **Single-cell/spatial transcriptomics of KOS placenta and thoracic mesenchyme** to resolve the cell-type-specific dosage effects already localized to villous endothelium and pericytes ([PMID: 22917972](https://pubmed.ncbi.nlm.nih.gov/22917972/)).
7. **Prospective hepatoblastoma surveillance protocol evaluation** (AFP + ultrasound interval optimization) to validate the recommended surveillance against outcomes.

---

*Report compiled from 7 confirmed findings and 33 reviewed papers over 5 investigation iterations. Evidence type: predominantly human clinical cohort/case data, supported by mouse and ovine model-organism genetics and in vitro expression studies.*


## Artifacts

- [OpenScientist final report](Kagami-Ogata_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Kagami-Ogata_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 11 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000115` (2 mentions) - the report calls it "Tissue/cell:** placental **villous vascular endothelial cells"; CL calls it **endothelial cell**
- `HP:0000889` (1 mention) - the report calls it "Coat-hanger rib configuration"; HP calls it **Abnormal clavicle morphology**
- `HP:0001520` (1 mention) - the report calls it "Birth overgrowth / high birth weight"; HP calls it **Large for gestational age**
- `HP:0000271` (1 mention) - the report calls it "Distinctive face (full cheeks, protruding philtrum, depressed nasal bridge)"; HP calls it **Abnormality of the face**
- `HP:0001537` (1 mention) - the report calls it "Abdominal wall defect (omphalocele, diastasis recti)"; HP calls it **Umbilical hernia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006349` (obsolete regulation of gene expression by genomic imprinting) (1 mention) - replaced by `GO:0071514`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0100767` (1 mention) - the report calls it "Placentomegaly"; HP calls it **Abnormal placenta morphology**, and lists "Placental issue" among its other names
- `HP:0001252` (1 mention) - the report calls it "Muscular hypotonia"; HP calls it **Hypotonia**, and lists "Muscular hypotonia" among its other names
- `GO:0005634` (1 mention) - the report calls it "Subcellular:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.