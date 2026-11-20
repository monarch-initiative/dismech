---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T18:12:07.725813'
end_time: '2026-11-12T18:39:07.000923'
duration_seconds: 1619.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Severe Combined Immunodeficiency Due To DNA-PKcs Deficiency
  mondo_id: MONDO:0014423
  category: Mendelian
  causal_genes: PRKDC
  omim_id: OMIM:615966
  synonyms: SCID due to DNA-PKcs deficiency
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
citation_count: 30
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 32
  on_topic: 27
  validator_version: 0.5.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.029
  labels_checked: 6
  labels_matching: 1
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014423
    reported_labels:
    - MONDO
    ontology_label: severe combined immunodeficiency due to DNA-PKcs deficiency
  - term_id: HP:0004430
    reported_labels:
    - Lab abnormality
    ontology_label: Severe combined immunodeficiency
  - term_id: HP:0000252
    reported_labels:
    - Physical manifestation
    ontology_label: Microcephaly
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: UBERON:0002371
    reported_labels:
    - "Primary:** hematolymphoid system \u2014 bone marrow"
    ontology_label: bone marrow
  unresolved_terms:
  - HP:0002543
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Severe_Combined_Immunodeficiency_Due_To_DNA-PKcs_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Severe_Combined_Immunodeficiency_Due_To_DNA-PKcs_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe Combined Immunodeficiency Due To DNA-PKcs Deficiency
- **MONDO ID:** MONDO:0014423 (if available)
- **Causal gene(s):** PRKDC
- **OMIM:** OMIM:615966
- **Synonyms:** SCID due to DNA-PKcs deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Severe Combined Immunodeficiency Due To DNA-PKcs Deficiency** covering all of the
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

# Severe Combined Immunodeficiency Due to DNA-PKcs Deficiency — Comprehensive Disease Report

**Disease:** Severe Combined Immunodeficiency Due To DNA-PKcs Deficiency
**Causal gene:** *PRKDC* (Protein Kinase, DNA-Activated, Catalytic Polypeptide), encoding the **DNA-dependent protein kinase catalytic subunit (DNA-PKcs)**
**MONDO:** MONDO:0014423 · **OMIM:** 615966 (Immunodeficiency 26, IMD26) · **Inheritance:** Autosomal recessive

---

## Summary

Severe combined immunodeficiency (SCID) due to DNA-PKcs deficiency is an **ultra-rare, autosomal-recessive inborn error of immunity caused by biallelic loss-of-function or hypomorphic mutations in *PRKDC***, the gene encoding the DNA-dependent protein kinase catalytic subunit (DNA-PKcs). DNA-PKcs is a core factor of the non-homologous end-joining (NHEJ) DNA double-strand-break repair pathway; it recruits and activates the nuclease **Artemis** to open DNA hairpins during V(D)J recombination, the process that builds the antigen-receptor repertoire of T and B lymphocytes. When DNA-PKcs function is lost, V(D)J recombination fails, T- and B-cell development arrests, and patients develop a **radiosensitive T-B-NK+ SCID**. As of 2024, only about **seven patients** have been described worldwide, making this one of the rarest defined SCID genotypes.

The human disease spectrum is broader than classic neonatal SCID. The predominant reported presentation is an **"atypical" / "leaky" form dominated by granulomas, autoimmunity, and inflammation** (5 of 7 patients), featuring cutaneous and visceral granulomas, autoimmune cytopenias and thyroiditis, a strong blood interferon signature, and—in at least one case—persistent **rubella vaccine-strain virus** within granuloma tissue. Mechanistically, this is linked both to failed V(D)J recombination and to a distinct role of DNA-PK in promoting **AIRE-dependent central T-cell tolerance**. Uniquely among NHEJ disorders, DNA-PKcs deficiency can also cause **severe human-specific neurodevelopmental disease** (microcephaly, seizures, progressive cerebral and hippocampal atrophy) that is not recapitulated in Prkdc-deficient mice, dogs, or horses, revealing a stringent requirement for DNA-PKcs in human neuronal development.

Untreated SCID is usually fatal in the first year of life. **Allogeneic hematopoietic stem cell transplantation (HSCT) is the only established curative therapy**, but patients' intrinsic radio- and chemosensitivity demands minimizing alkylator-based conditioning and ionizing radiation. Survival is best when the diagnosis is made presymptomatically through newborn screening (low/absent T-cell receptor excision circles, TRECs). Diagnosis cannot rely on DNA-PK kinase activity—the recurrent p.L3062R variant retains kinase activity—so **molecular sequencing of *PRKDC* is required**, supported by the characteristic long palindromic (P)-nucleotide signature in antigen-receptor coding joints and by cellular radiosensitivity assays.

---

## Key Findings

### F001 — A recurrent hypomorphic missense mutation, p.L3062R, dominates the human cohort

Of the seven reported patients with human DNA-PKcs deficiency, **six carry the autosomal-recessive *PRKDC* missense variant p.L3062R**. The first human case was reported in 2009. The variant is **hypomorphic rather than null**: DNA-PKcs protein is still expressed and retains autophosphorylation and DNA end-binding capacity, but the mutant protein **fails to properly activate the Artemis nuclease**, impairing hairpin opening during V(D)J recombination. Structural studies place residue L3062 in the FAT/kinase region of DNA-PKcs and explain how the substitution produces insufficient Artemis activation while preserving the kinase's own catalytic output.

> *"6 patients displayed the autosomal recessive p.L3062R mutation in PRKDC-encoding DNA-PKcs"* — [PMID: 38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/)
>
> *"The mutation concerned a hypomorphic missense mutation (L3062R) that did not result in absence of protein expression nor in deficient in vivo or in vitro (auto)phosphorylation"* — [PMID: 19823081](https://pubmed.ncbi.nlm.nih.gov/19823081/)
>
> *"All of the findings are useful in explaining how a hypomorphic L3062R missense mutation of DNA-PKcs could lead to insufficient Artemis activation, hence RS-SCID"* — [PMID: 35801871](https://pubmed.ncbi.nlm.nih.gov/35801871/)

This has a direct **diagnostic corollary**: because the recurrent allele leaves kinase activity intact, a normal DNA-PK kinase assay does not exclude a *PRKDC* defect.

### F002 — The predominant human presentation is atypical SCID with granuloma, autoimmunity, and inflammation

In the cohort of seven patients, **atypical (leaky) SCID with inflammatory lesions, granulomas, and autoimmunity was the predominant manifestation (5 of 7)**. Reported features include cutaneous and visceral granulomas, autoimmune cytopenias and thyroiditis, a strong whole-blood interferon signature, progressively declining T- and B-cell counts over time, and severe infections. In two patients tested for rubella, **rubella vaccine-strain virus was detected within granuloma tissue in one**, linking persistent live-attenuated vaccine virus to the granulomatous pathology—a phenomenon well documented across combined immunodeficiencies.

> *"Atypical severe combined immunodeficiency with inflammatory lesions, granulomas, and autoimmunity was the predominant clinical manifestation (n = 5 of 7)"* — [PMID: 38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/)
>
> *"Rubella viral strain was detected in the granuloma of 1 patient over the 2 tested"* — [PMID: 38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/)
>
> *"Whole-blood mRNA analysis revealed a strong interferon signature"* — [PMID: 25842288](https://pubmed.ncbi.nlm.nih.gov/25842288/)

Two siblings with a *PRKDC* defect presenting with cutaneous granulomas and recurrent lung infections ([PMID: 30121298](https://pubmed.ncbi.nlm.nih.gov/30121298/)) further illustrate that primary immune deficiency in this disorder may first present with skin findings, and that modifier genes and environmental factors likely shape the variable phenotype.

### F003 — DNA-PKcs deficiency uniquely causes severe human neurodevelopmental disease

A patient with **compound-heterozygous *PRKDC* mutations** (low DNA-PKcs expression, barely detectable kinase activity) had SCID plus dysmorphism, severe growth failure, **microcephaly, seizures, and profound, globally impaired neurological function**. MRI demonstrated cortical and hippocampal dysplasia with **progressive atrophy over two years**. These neurological features were markedly more severe than in deficiencies of other NHEJ proteins (e.g., Artemis, LIG4, Cernunnos), and—critically—are **not seen in Prkdc-deficient mice, dogs, or horses**, pointing to a stringent, human-specific requirement for DNA-PKcs during neuronal development.

> *"the patient was also dysmorphic; showed severe growth failure, microcephaly, and seizures; and had profound, globally impaired neurological function"* — [PMID: 23722905](https://pubmed.ncbi.nlm.nih.gov/23722905/)
>
> *"These neurological features were markedly more severe than those observed in patients with deficiencies in other NHEJ proteins"* — [PMID: 23722905](https://pubmed.ncbi.nlm.nih.gov/23722905/)
>
> *"our findings demonstrate a stringent requirement for DNA-PKcs during human neuronal development"* — [PMID: 23722905](https://pubmed.ncbi.nlm.nih.gov/23722905/)

The neurological severity is thought to reflect the role of NHEJ in repairing endogenous double-strand breaks in post-mitotic and developing neurons; it distinguishes DNA-PKcs deficiency from the otherwise overlapping NHEJ-SCID disorders.

### F004 — Causal chain: *PRKDC* loss impairs NHEJ/V(D)J recombination and AIRE-dependent tolerance

DNA-PKcs is a core NHEJ factor that **recruits and activates Artemis to open DNA hairpins during V(D)J recombination**. Autophosphorylation of the **ABCDE/Thr2609 cluster** switches DNA-PK from an end-protection to an end-processing mode, structurally widening the DNA-binding groove to admit Artemis for hairpin cleavage. Loss of function **blocks formation of coding and signal joints**, arresting T- and B-cell development (producing T-B-NK+ SCID) and conferring cellular radiosensitivity to double-strand-break damage.

A **second, parallel mechanistic branch** explains the autoimmunity: DNA-PK interacts with the transcription factor **AIRE (autoimmune regulator)** to promote central T-cell tolerance. Mutant DNA-PKcs failed to drive AIRE-dependent transcription of peripheral-tissue antigens in vitro, and this correlated in vivo with anti-calcium-sensing-receptor autoantibodies typical of AIRE deficiency.

> *"In mice DNA-PK also interacts with the transcription factor autoimmune regulator (AIRE) to promote central T-cell tolerance"* — [PMID: 25842288](https://pubmed.ncbi.nlm.nih.gov/25842288/)
>
> *"mutated DNA-PKcs did not promote AIRE-dependent transcription of peripheral tissue antigens in vitro"* — [PMID: 25842288](https://pubmed.ncbi.nlm.nih.gov/25842288/)
>
> *"Phosphorylation of four Thr residues in ABCDE leads to gross structural rearrangement of DNA-PK, widening the DNA binding groove for Artemis recruitment and hairpin cleavage"* — [PMID: 34936881](https://pubmed.ncbi.nlm.nih.gov/34936881/)

### F005 — DNA-PKcs deficiency occurs naturally across species with graded V(D)J severity; HSCT is curative

Spontaneous DNA-PKcs deficiency defines the classic **C.B-17 *scid* mouse** and occurs naturally in **Arabian horse foals** and **Jack Russell terrier dogs**. The severity of the V(D)J recombination block **inversely correlates with the residual DNA-PK activity** measured in normal fibroblasts from each species (horse most severe, mouse leakiest, dog intermediate). None of these animals develops the human neurological phenotype. **Allogeneic HSCT is the only established curative therapy** for radiosensitive SCID, but patients' intrinsic radio- and chemosensitivity mandates minimizing alkylating conditioning agents and ionizing radiation. Proof-of-concept gene therapy exists: **iPSC-based nuclease gene correction restored DNA-PK signaling and T-cell maturation** in a *prkdc*-deficient disease model.

> *"the severity of the V(D)J recombination deficits in these three examples of genetic DNA-PKcs deficiency inversely correlates with the relative DNA-PK enzymatic activity expressed in normal fibroblasts derived from these three species"* — [PMID: 11489998](https://pubmed.ncbi.nlm.nih.gov/11489998/)
>
> *"Patients with the radiosensitive form of SCID may also have increased short- and long-term sensitivity to the alkylator-based chemotherapy regimens that are traditionally used for conditioning before allogeneic hematopoietic cell transplantation (HCT)"* — [PMID: 20113890](https://pubmed.ncbi.nlm.nih.gov/20113890/)
>
> *"Genetic correction of the RS-SCID iPSC restored T-lymphocyte maturation, polyclonal V(D)J recombination of the T-cell receptor followed by successful beta-selection"* — [PMID: 26000857](https://pubmed.ncbi.nlm.nih.gov/26000857/)

### F006 — Diagnosis rests on T-B-NK+ immunophenotype, radiosensitivity, a P-nucleotide signature, and *PRKDC* sequencing

The recurrent L3062R mutation does not abolish DNA-PKcs kinase activity or DNA end-binding; diagnosis therefore relies on the **functional consequence**—insufficient Artemis activation, revealed by **long palindromic (P)-nucleotide stretches in immunoglobulin/TCR coding joints**—plus impaired overall end-joining and cellular radiosensitivity (colony-survival and γ-H2AX assays). The immunophenotype is **T-B-NK+ SCID**. Because kinase activity is retained, authors explicitly warn that a normal DNA-PK activity assay does **not** exclude a *PRKDC* defect, so **molecular sequencing of *PRKDC* is required for definitive diagnosis**. Newborn screening detects **low/absent T-cell receptor excision circles (TRECs)** on dried blood spots.

> *"The causative mutation did not affect the kinase activity or DNA end-binding capacity of DNA-PKcs itself; rather, the presence of long P-nucleotide stretches in the immunoglobulin coding joints indicated that it caused insufficient Artemis activation"* — [PMID: 19075392](https://pubmed.ncbi.nlm.nih.gov/19075392/)
>
> *"the presence of DNA-PKcs kinase activity is not sufficient to rule out a defect in this gene during diagnosis and treatment of RS-SCID patients"* — [PMID: 19075392](https://pubmed.ncbi.nlm.nih.gov/19075392/)
>
> *"Without treatment, severe combined immunodeficiency is usually fatal in the first year of life"* — [PMID: 42299943](https://pubmed.ncbi.nlm.nih.gov/42299943/)

The P-nucleotide / microhomology signature is shared with Artemis deficiency ([PMID: 18034425](https://pubmed.ncbi.nlm.nih.gov/18034425/)), consistent with DNA-PKcs and Artemis acting in the same hairpin-opening step.

### F007 — Ultra-rarity, detected within broader SCID newborn screening

Human *PRKDC* deficiency is **extremely rare—only ~7 patients reported worldwide as of 2024**—making individual prevalence incalculable (far below 1 per million). It is one subtype within all-cause SCID, which arises from mutations in **at least 19 known genes**. A seven-year **Catalonia (Spain) TREC newborn-screening program of 420,263 newborns** diagnosed SCID in 8 infants plus 1 congenital athymia, giving an all-cause SCID incidence of **1:46,753 live births**. Inheritance is autosomal recessive; the recurrent p.L3062R allele raises the possibility of founder effects and/or consanguinity in reported families.

> *"Among 420,263 screened newborns, 105 screened positive (0.02%). SCID was diagnosed in eight infants and congenital athymia in one, corresponding to an overall incidence of 1:46,753 live births"* — [PMID: 42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/)
>
> *"Severe combined immunodeficiency is an inherited condition arising from mutations in at least 19 known genes"* — [PMID: 42299943](https://pubmed.ncbi.nlm.nih.gov/42299943/)
>
> *"human mutations in PRKDC are extremely rare and the disease spectrum has not been described so far"* — [PMID: 38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/)

### F008 — Prognosis is fatal untreated; allogeneic HSCT is curative, best after newborn-screening diagnosis

Untreated SCID is usually fatal within the first year of life, and **allogeneic HSCT is the only established cure**. In a 100-patient SCID HSCT cohort, overall survival was **68% (84% excluding first-month mortality)**; survival was significantly higher for cases identified by **newborn screening (93%)** versus clinical presentation, and better with bone-marrow graft source, matched related donor, and use of conditioning. For DNA-PKcs/radiosensitive SCID specifically, intrinsic radio- and chemosensitivity mandates minimizing alkylator conditioning and ionizing radiation. Supportive management includes immunoglobulin replacement, antimicrobial prophylaxis, protective isolation, irradiated/CMV-safe blood products, and avoidance of live vaccines—particularly relevant given the persistence of live rubella vaccine strain in granulomas. Experimental directions include gene therapy / gene correction (iPSC proof-of-concept).

> *"SCID cases identified by NBS demonstrated superior OS (93%) compared to cases identified by clinical presentation"* — [PMID: 39900265](https://pubmed.ncbi.nlm.nih.gov/39900265/)
>
> *"The OS rate was 68%, increasing to 84% when excluding mortality in the first month after transplantation"* — [PMID: 39900265](https://pubmed.ncbi.nlm.nih.gov/39900265/)
>
> *"minimizing exposure to alkylating agents and ionizing radiation is important for optimizing survival and minimizing late effects"* — [PMID: 26055221](https://pubmed.ncbi.nlm.nih.gov/26055221/)

---

## Report by Section

### 1. Disease Information

DNA-PKcs–deficient SCID is a monogenic, autosomal-recessive inborn error of immunity in the **NHEJ / V(D)J-recombination-defect ("radiosensitive SCID", RS-SCID)** family. The causal gene is **PRKDC**, encoding **DNA-PKcs**, the ~469 kDa catalytic subunit of the DNA-dependent protein kinase holoenzyme (DNA-PK = Ku70/Ku80 + DNA-PKcs).

| Identifier | Value |
|---|---|
| MONDO | MONDO:0014423 |
| OMIM | 615966 (Immunodeficiency 26, IMD26) |
| Gene | *PRKDC* (HGNC:9413), chromosome 8q11.21 |
| Protein | DNA-PKcs (UniProt P78527) |
| Inheritance | Autosomal recessive |
| MeSH | Severe Combined Immunodeficiency (D016511) |
| ICD-10 / ICD-11 | D81.x (combined immunodeficiencies) / 4A01.1 family |
| Orphanet | Within "Radiosensitive SCID" grouping |

**Synonyms:** SCID due to DNA-PKcs deficiency; PRKDC deficiency; DNA-PKcs deficiency; radiosensitive T-B-NK+ SCID due to *PRKDC* mutation; Immunodeficiency 26.

Most of the disease-level knowledge is derived from **aggregated case reports and small series** (the comprehensive review covering 7 patients, [PMID: 38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/)) rather than from EHR-scale cohorts, reflecting extreme rarity.

### 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound-heterozygous) pathogenic variants in *PRKDC*. The recurrent **p.L3062R** hypomorphic missense allele accounts for 6 of 7 reported patients ([PMID: 38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/)); a distinct compound-heterozygous genotype with very low expression and near-absent kinase activity underlies the severe neurological case ([PMID: 23722905](https://pubmed.ncbi.nlm.nih.gov/23722905/)).

**Genetic risk factors.** The disease is fully penetrant Mendelian; "risk" is conferred by inheriting two pathogenic alleles. Consanguinity and possible founder effects likely contribute to recurrence of L3062R. **Modifier genes, epigenetic, and environmental factors** are proposed to explain the broad phenotypic variability ([PMID: 30121298](https://pubmed.ncbi.nlm.nih.gov/30121298/)).

**Environmental risk / protective factors.** No classical environmental risk factors cause the disease. However, environmental exposures strongly modulate outcome: **ionizing radiation and alkylating chemotherapy are hazardous** owing to intrinsic radiosensitivity, and **live-attenuated vaccines (e.g., rubella, BCG, rotavirus) are dangerous** and can cause disseminated vaccine-strain disease and granulomas ([PMID: 38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/)). Protective measures are behavioral/clinical (isolation, prophylaxis, avoidance of live vaccines and radiation) rather than genetic.

**Gene–environment interactions.** The defective DNA-repair genotype converts otherwise routine exposures—radiologic imaging, conditioning chemotherapy, live vaccines—into serious hazards, the defining gene–environment interaction of radiosensitive SCID.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset / severity / frequency |
|---|---|---|---|
| Severe/recurrent infections | Clinical sign | HP:0002719, HP:0002721 | Neonatal–infancy; severe; near-universal |
| T-B-NK+ severe combined immunodeficiency | Lab abnormality | HP:0004430 | Congenital; severe; defining |
| Granulomas (cutaneous/visceral) | Physical manifestation | HP:0032252, HP:0001061 | Infancy–childhood; variable; 5/7 (atypical form) |
| Autoimmunity (cytopenias, thyroiditis) | Clinical sign | HP:0002960, HP:0002633 | Childhood; variable; frequent in leaky form |
| Interferon signature (blood) | Lab abnormality | — | Correlates with inflammation |
| Microcephaly | Physical manifestation | HP:0000252 | Congenital; severe; subset (neurological case) |
| Seizures | Clinical sign | HP:0001250 | Infancy; severe; subset |
| Progressive cerebral/hippocampal atrophy | Imaging | HP:0002059, HP:0002543 | Progressive over ~2 y; subset |
| Growth failure / dysmorphism | Physical | HP:0001508, HP:0001999 | Congenital; severe; subset |
| Declining T- and B-cell counts | Lab abnormality | HP:0005403, HP:0010976 | Progressive in leaky form |

**Quality-of-life impact:** profound. Untreated disease is lethal in infancy; survivors require lifelong immune support until/after HSCT. Neurological involvement, where present, causes severe lifelong disability.

### 4. Genetic / Molecular Information

- **Causal gene:** *PRKDC* (HGNC:9413; OMIM 600899), 8q11.21; protein DNA-PKcs (UniProt P78527), a PIKK-family serine/threonine kinase with FAT, kinase, and FATC domains and a large HEAT-repeat N-terminal solenoid.
- **Pathogenic variants:**
  - **p.L3062R** — recurrent hypomorphic missense in the FAT/kinase region; LOF for Artemis activation but retains autophosphorylation/kinase activity; classified pathogenic (functional + segregation evidence). 6/7 patients.
  - **Compound-heterozygous** genotype with reduced expression + minimal kinase activity → severe SCID + neurodevelopmental disease ([PMID: 23722905](https://pubmed.ncbi.nlm.nih.gov/23722905/)).
- **Variant types:** missense (predominant); other LOF classes expected but under-reported given rarity.
- **Allele frequency:** pathogenic alleles are vanishingly rare in gnomAD; the biallelic disease is <1 per million.
- **Origin:** germline, autosomal recessive.
- **Functional consequence:** loss of function with respect to Artemis activation / NHEJ end-processing (hypomorphic, not complete null, for L3062R).
- **Modifier genes / epigenetics:** proposed to shape variable expressivity ([PMID: 30121298](https://pubmed.ncbi.nlm.nih.gov/30121298/)); no specific modifier locus established.
- **Chromosomal abnormalities:** none characteristic; DNA-PKcs loss predisposes to genomic instability and telomere-fusion phenotypes in model cells ([PMID: 15162023](https://pubmed.ncbi.nlm.nih.gov/15162023/), [PMID: 38407308](https://pubmed.ncbi.nlm.nih.gov/38407308/)).

### 5. Environmental Information

- **Environmental factors:** ionizing radiation and radiomimetic/alkylating agents cause excess cellular damage owing to the DSB-repair defect ([PMID: 20113890](https://pubmed.ncbi.nlm.nih.gov/20113890/)).
- **Lifestyle factors:** not applicable (congenital genetic disease).
- **Infectious agents:** opportunistic and common pathogens cause severe infection due to immunodeficiency; **live-attenuated vaccine strains** (notably **rubella virus**) can persist and drive granulomas ([PMID: 38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic *PRKDC* mutation (e.g., p.L3062R)** → expression of a DNA-PKcs protein that retains kinase activity but is defective in activating Artemis (*leads to*, demonstrated biochemically; [PMID: 19075392](https://pubmed.ncbi.nlm.nih.gov/19075392/)).
2. During V(D)J recombination, RAG1/2 generate hairpin-sealed coding ends → DNA-PKcs normally autophosphorylates its **ABCDE/Thr2609 cluster**, rearranging to admit Artemis (*results in* hairpin opening; [PMID: 34936881](https://pubmed.ncbi.nlm.nih.gov/34936881/)).
3. Mutant DNA-PKcs **fails to activate Artemis** → hairpins are not opened, coding joints form with **long P-nucleotide stretches**, and overall NHEJ end-joining is impaired (*leads to*; [PMID: 19075392](https://pubmed.ncbi.nlm.nih.gov/19075392/)).
4. Failed V(D)J recombination **arrests T- and B-lymphocyte development** → **T-B-NK+ SCID** (*results in*, demonstrated by immunophenotype).
5. In parallel, impaired NHEJ leaves cells unable to repair radiation/chemotherapy-induced DSBs → **cellular radiosensitivity** (*results in*; [PMID: 19858715](https://pubmed.ncbi.nlm.nih.gov/19858715/)).
6. **Branch — tolerance:** mutant DNA-PKcs fails to support **AIRE-dependent transcription of peripheral-tissue antigens**, impairing central T-cell tolerance → **autoimmunity, autoantibodies, granuloma** (*leads to*; [PMID: 25842288](https://pubmed.ncbi.nlm.nih.gov/25842288/)); amplified by a **type I interferon signature** and, in some, **persistent rubella vaccine strain** in tissue (*contributes to* granuloma; [PMID: 38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/)).
7. **Branch — neurodevelopment (human-specific):** loss of DNA-PKcs-dependent repair of endogenous DSBs in developing/post-mitotic neurons → **microcephaly, seizures, progressive cerebral/hippocampal atrophy** (*results in*; demonstrated clinically but mechanistically inferred; [PMID: 23722905](https://pubmed.ncbi.nlm.nih.gov/23722905/)).

```
PRKDC mutation (L3062R)
        │  (hypomorphic: kinase OK, Artemis activation lost)
        ▼
NHEJ end-processing defect ──► cellular radiosensitivity (DSB repair failure)
        │
        ├──► V(D)J recombination block ──► T-B-NK+ SCID ──► severe infections
        │
        ├──► impaired AIRE-dependent tolerance ──► autoimmunity + granuloma
        │          (+ IFN signature, + persistent rubella vaccine strain)
        │
        └──► [human-specific] neuronal DSB repair failure ──► microcephaly,
                   seizures, progressive cerebral atrophy
```

- **Molecular pathways:** NHEJ DSB repair; V(D)J recombination; DNA-PK/PIKK signaling (GO:0006303 DSB repair via NHEJ; GO:0033151 V(D)J recombination).
- **Protein dysfunction:** loss of function for Artemis activation; structurally localized to FAT/kinase region ([PMID: 35801871](https://pubmed.ncbi.nlm.nih.gov/35801871/), [PMID: 36270581](https://pubmed.ncbi.nlm.nih.gov/36270581/)).
- **Cellular processes:** arrested lymphocyte development; genomic instability; defective repair response to DSBs.
- **Immune involvement:** profound combined immunodeficiency (GO:0002250 adaptive immune response) plus dysregulated inflammation/autoimmunity.
- **Cell types (CL):** T cells (CL:0000084), B cells (CL:0000236), developing thymocytes (CL:0000893), neurons (CL:0000540).

### 7. Anatomical Structures Affected

- **Primary:** hematolymphoid system — bone marrow (UBERON:0002371), thymus (UBERON:0002370), lymph nodes (UBERON:0000029), spleen (UBERON:0002106).
- **Secondary / inflammatory:** skin (UBERON:0002097, granulomas), lung (UBERON:0002048, infections/granulomas), thyroid (UBERON:0002046, autoimmune thyroiditis), and other viscera with granulomas.
- **Nervous system (subset):** cerebral cortex (UBERON:0000956), hippocampus (UBERON:0002421) — dysplasia and progressive atrophy.
- **Subcellular (GO CC):** **nucleus** (GO:0005634) — site of DNA-PK action; DNA-dependent protein kinase complex (GO:0005958).
- **Lateralization:** systemic/bilateral; CNS atrophy global.

### 8. Temporal Development

- **Onset:** congenital immune defect; classic SCID presents in the **neonatal period / first months** with infections and failure to thrive. The leaky/granulomatous form may present later in **childhood**. Neurological features (subset) are congenital and **progressive**.
- **Progression:** without HSCT, relentless and fatal in infancy. In leaky disease, **T- and B-cell counts decline over time**, and inflammatory/autoimmune disease accrues. CNS atrophy progressed over ~2 years in the reported neurological case.
- **Critical period:** the window for pre-symptomatic newborn-screening detection and early HSCT is decisive for survival.

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive; complete penetrance for biallelic pathogenic genotypes.
- **Expressivity:** highly variable (classic SCID ↔ granulomatous/autoimmune ↔ severe neurodevelopmental), attributed to allele type and proposed modifiers.
- **Epidemiology:** ultra-rare — ~7 patients worldwide; individual prevalence <1/1,000,000. All-cause SCID incidence context: **1:46,753 live births** (Catalonia TREC screening; [PMID: 42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/)); SCID arises from ≥19 genes ([PMID: 42299943](https://pubmed.ncbi.nlm.nih.gov/42299943/)).
- **Founder/consanguinity:** recurrence of p.L3062R suggests possible founder/consanguinity contributions.
- **Sex ratio / geography:** no established predilection given tiny numbers.

### 10. Diagnostics

- **Immunophenotype:** **T-B-NK+ SCID** by flow cytometry; low/absent T and B cells, preserved NK cells.
- **Newborn screening:** **low/absent TRECs** on dried blood spots (multiplex TREC/KREC qPCR) — the frontline population screen ([PMID: 42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/), [PMID: 42496450](https://pubmed.ncbi.nlm.nih.gov/42496450/)).
- **Radiosensitivity testing:** colony-survival assay (gold standard), γ-H2AX foci — confirms the DSB-repair defect ([PMID: 19858715](https://pubmed.ncbi.nlm.nih.gov/19858715/)).
- **V(D)J coding-joint analysis:** **long palindromic (P)-nucleotide stretches** (shared signature with Artemis deficiency) indicate impaired hairpin opening ([PMID: 19075392](https://pubmed.ncbi.nlm.nih.gov/19075392/), [PMID: 18034425](https://pubmed.ncbi.nlm.nih.gov/18034425/)).
- **Caveat:** DNA-PK kinase activity may be **normal** (L3062R) — a normal assay does not exclude *PRKDC* defect ([PMID: 19075392](https://pubmed.ncbi.nlm.nih.gov/19075392/)).
- **Genetic testing (definitive):** *PRKDC* sequencing via SCID/IEI NGS panels or WES/WGS ([PMID: 35303369](https://pubmed.ncbi.nlm.nih.gov/35303369/)).
- **Differential diagnosis:** other radiosensitive SCIDs — Artemis/*DCLRE1C* ([PMID: 19953608](https://pubmed.ncbi.nlm.nih.gov/19953608/)), *LIG4* syndrome ([PMID: 16585603](https://pubmed.ncbi.nlm.nih.gov/16585603/)), Cernunnos/*NHEJ1* ([PMID: 37842439](https://pubmed.ncbi.nlm.nih.gov/37842439/)); also non-radiosensitive SCID (RAG1/2, IL2RG, ADA, etc.).

### 11. Outcome / Prognosis

- **Untreated:** usually fatal in the first year of life ([PMID: 42299943](https://pubmed.ncbi.nlm.nih.gov/42299943/)).
- **With HSCT:** overall survival ~68% (84% excluding first-month mortality) in a 100-patient SCID cohort; **93% when diagnosed by newborn screening** ([PMID: 39900265](https://pubmed.ncbi.nlm.nih.gov/39900265/)). Better outcomes with matched related donor, bone-marrow source, and conditioning—balanced against radiosensitivity.
- **Complications:** disseminated infection, granuloma/autoimmunity, and—where present—neurological disability that HSCT does not reverse.
- **Prognostic factors:** age at diagnosis (newborn screening vs symptomatic), donor match, conditioning intensity/toxicity, and presence of neurological disease.

### 12. Treatment

- **Curative — allogeneic HSCT** (NCIT: Allogeneic Hematopoietic Stem Cell Transplantation) is the standard of care, with **radiosensitivity-adapted, reduced-genotoxic conditioning** and avoidance of ionizing radiation ([PMID: 26055221](https://pubmed.ncbi.nlm.nih.gov/26055221/), [PMID: 31392129](https://pubmed.ncbi.nlm.nih.gov/31392129/), [PMID: 20113890](https://pubmed.ncbi.nlm.nih.gov/20113890/)). Haploidentical approaches with modified conditioning/GVHD prophylaxis have been used in radiosensitive SCID ([PMID: 37842439](https://pubmed.ncbi.nlm.nih.gov/37842439/)).
- **Supportive care:** immunoglobulin replacement, antimicrobial prophylaxis (PJP, antifungal, antiviral), protective isolation, **irradiated/CMV-safe blood products**, and **avoidance of live vaccines** (NCIT: Supportive Care; Immunoglobulin Therapy; Antimicrobial Prophylaxis).
- **Experimental:** **gene therapy / gene correction** — nuclease-based correction of *prkdc* in iPSCs restored DNA-PK signaling and T-cell maturation, a proof of concept ([PMID: 26000857](https://pubmed.ncbi.nlm.nih.gov/26000857/)).
- **Pharmacogenomics:** the radiosensitive genotype itself dictates avoidance of alkylators/radiation—genotype-guided conditioning.

### 13. Prevention

- **Primary prevention:** not applicable (congenital genetic disease); **genetic counseling** and reproductive options (carrier testing, PGD/prenatal testing) for at-risk families.
- **Secondary prevention:** **newborn screening (TREC)** for presymptomatic detection, enabling early HSCT and markedly improved survival ([PMID: 39900265](https://pubmed.ncbi.nlm.nih.gov/39900265/), [PMID: 42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/)).
- **Tertiary prevention:** infection prophylaxis, avoidance of live vaccines and radiation, and management of autoimmunity/granuloma.
- **Immunization caveat:** **live-attenuated vaccines are contraindicated**; inactivated vaccines are generally ineffective pre-immune reconstitution.

### 14. Other Species / Natural Disease

Naturally occurring DNA-PKcs deficiency is well documented:

| Species | NCBI Taxon | Model/natural | Severity of V(D)J block |
|---|---|---|---|
| Mouse (*Mus musculus*, C.B-17 *scid*) | 10090 | Spontaneous | Leakiest |
| Dog (*Canis familiaris*, Jack Russell terrier) | 9615 | Natural | Intermediate |
| Horse (*Equus caballus*, Arabian foal) | 9796 | Natural | Most severe |

Severity inversely correlates with residual fibroblast DNA-PK activity ([PMID: 11489998](https://pubmed.ncbi.nlm.nih.gov/11489998/)). **None of these animals develops the human neurological phenotype**, underscoring the human-specific neuronal requirement ([PMID: 23722905](https://pubmed.ncbi.nlm.nih.gov/23722905/)). Orthologous gene: *Prkdc* in mouse/dog/horse. These are of veterinary importance (fatal SCID in affected foals and pups) and serve as comparative-biology and preclinical models. No zoonotic transmission (genetic disease).

### 15. Model Organisms

- **Mouse:** C.B-17 *scid* (spontaneous *Prkdc* mutation); recapitulates T-B-NK+ SCID, radiosensitivity, V(D)J block, and genomic-instability/telomere phenotypes ([PMID: 15162026](https://pubmed.ncbi.nlm.nih.gov/15162026/), [PMID: 27136939](https://pubmed.ncbi.nlm.nih.gov/27136939/)). Comparator NHEJ models: Artemis-deficient mice (leaky SCID, [PMID: 12504013](https://pubmed.ncbi.nlm.nih.gov/12504013/)); *Lig4* R278H knock-in (LIG4-syndrome model, [PMID: 20133615](https://pubmed.ncbi.nlm.nih.gov/20133615/)).
- **Large-animal natural models:** Jack Russell terrier dog; Arabian horse foal ([PMID: 11489998](https://pubmed.ncbi.nlm.nih.gov/11489998/)).
- **Cellular / iPSC:** patient-derived and *prkdc*-deficient iPSCs corrected by targeted genome editing restored DNA-PK signaling and T-cell differentiation ([PMID: 26000857](https://pubmed.ncbi.nlm.nih.gov/26000857/)).
- **Model limitation:** no model reproduces the **human neurodevelopmental disease**, the key gap between animal and human phenotypes.
- **Resources:** MGI, IMSR (mouse); OMIA (natural animal disease); Cellosaurus (iPSC/cell lines).

---

## Mechanistic Model / Interpretation

DNA-PKcs sits at the intersection of two biological programs that together explain the full disease spectrum. First, as the **regulatory hub that licenses Artemis** to open DNA hairpins, DNA-PKcs is indispensable for V(D)J recombination; its loss produces the core T-B-NK+ SCID with radiosensitivity shared across NHEJ defects (Artemis, LIG4, Cernunnos). The recurrent **L3062R allele is informative precisely because it is "surgical"**: it preserves the kinase's catalytic and DNA-binding functions but severs the Artemis-activation step, producing a diagnostic P-nucleotide fingerprint and the warning that kinase assays cannot exclude the disease.

Second, DNA-PK's **partnership with AIRE** adds a tolerance-breaking layer absent from a simple "empty immune compartment" model, explaining why the human cohort is dominated by **granulomas, autoimmunity, and an interferon signature** rather than pure infection susceptibility. Persistent live rubella vaccine strain acts as an antigenic driver of granuloma within this tolerance-defective, immune-dysregulated milieu.

Third, and uniquely, DNA-PKcs is required for **human neuronal genome maintenance**, a requirement not met by compensatory repair in mouse, dog, or horse. This species difference is the single most striking feature of the human disease and the principal unmet gap in animal modeling.

Therapeutically, the logic is coherent: **HSCT corrects the hematopoietic defect**, newborn screening maximizes survival by enabling pre-infection transplant, and the intrinsic DSB-repair defect converts conditioning genotoxins into hazards—mandating reduced-intensity, radiation-sparing regimens. Gene correction offers a future route that could, in principle, also address non-hematopoietic (e.g., neuronal) requirements, though this remains preclinical.

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [38977084](https://pubmed.ncbi.nlm.nih.gov/38977084/) | Comprehensive review/update: 7-patient spectrum, L3062R recurrence, granuloma/autoimmunity, rubella in granuloma, rarity |
| [19823081](https://pubmed.ncbi.nlm.nih.gov/19823081/) | First human DNA-PKcs deficiency; hypomorphic L3062R retains expression/phosphorylation |
| [35801871](https://pubmed.ncbi.nlm.nih.gov/35801871/) | Structure of Artemis:DNA-PKcs basal state; links L3062R to insufficient Artemis activation |
| [23722905](https://pubmed.ncbi.nlm.nih.gov/23722905/) | Compound-het patient with severe neurodevelopmental disease; human-specific DNA-PKcs requirement |
| [25842288](https://pubmed.ncbi.nlm.nih.gov/25842288/) | AIRE-dependent tolerance branch; interferon signature; autoimmunity mechanism |
| [34936881](https://pubmed.ncbi.nlm.nih.gov/34936881/) | ABCDE/Thr2609 autophosphorylation switch for Artemis recruitment/hairpin cleavage |
| [19075392](https://pubmed.ncbi.nlm.nih.gov/19075392/) | P-nucleotide diagnostic signature; retained-kinase caveat |
| [11489998](https://pubmed.ncbi.nlm.nih.gov/11489998/) | Cross-species natural models; graded V(D)J severity vs residual activity |
| [20113890](https://pubmed.ncbi.nlm.nih.gov/20113890/) | Radiosensitive SCID: chemo/radiation sensitivity and conditioning |
| [26000857](https://pubmed.ncbi.nlm.nih.gov/26000857/) | iPSC genome-editing restores DNA-PK signaling and T-cell maturation |
| [39900265](https://pubmed.ncbi.nlm.nih.gov/39900265/) | HSCT survival 68/84%; 93% with newborn screening |
| [26055221](https://pubmed.ncbi.nlm.nih.gov/26055221/) | Rationale for minimizing alkylators/radiation in RS-SCID |
| [42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/) | All-cause SCID incidence 1:46,753 (TREC screening) |
| [42299943](https://pubmed.ncbi.nlm.nih.gov/42299943/) | SCID fatal untreated in first year; ≥19 SCID genes |
| [18034425](https://pubmed.ncbi.nlm.nih.gov/18034425/) | P-nucleotide/microhomology signature (Artemis defect, shared step) |
| [30121298](https://pubmed.ncbi.nlm.nih.gov/30121298/) | Two PRKDC siblings with cutaneous granulomas; modifier hypothesis |
| [19858715](https://pubmed.ncbi.nlm.nih.gov/19858715/) | DSB-repair defects and radiosensitivity; colony-survival assay |

Supporting/contextual: [35303369](https://pubmed.ncbi.nlm.nih.gov/35303369/) (SCID gene panel incl. PRKDC), [25987660](https://pubmed.ncbi.nlm.nih.gov/25987660/) (V(D)J congenital defects), [36270581](https://pubmed.ncbi.nlm.nih.gov/36270581/) (Artemis:DNA-PKcs dynamics), [38407308](https://pubmed.ncbi.nlm.nih.gov/38407308/) (DNA-PK telomere control), [12504013](https://pubmed.ncbi.nlm.nih.gov/12504013/) (Artemis mouse), [20133615](https://pubmed.ncbi.nlm.nih.gov/20133615/) (LIG4 mouse), [16585603](https://pubmed.ncbi.nlm.nih.gov/16585603/) (LIG4 human), [37842439](https://pubmed.ncbi.nlm.nih.gov/37842439/) (haploidentical HSCT in RS-SCID), [31392129](https://pubmed.ncbi.nlm.nih.gov/31392129/) / [28918671](https://pubmed.ncbi.nlm.nih.gov/28918671/) (HSCT in PID and late effects).

---

## Limitations and Knowledge Gaps

- **Extreme rarity (~7 patients)** precludes robust estimates of prevalence, penetrance of specific features, survival, and genotype–phenotype correlations; most evidence is from case reports/small series.
- **Genotype–phenotype relationships are uncertain:** why the same L3062R allele yields classic vs granulomatous disease (modifier genes, environment, epigenetics) is unresolved.
- **No animal model of the human neurological phenotype**, limiting mechanistic dissection of the CNS requirement.
- **Disease-specific HSCT outcomes** for *PRKDC* are not separately quantified; survival figures are extrapolated from all-cause/radiosensitive SCID cohorts.
- **Gene/cell therapy** remains preclinical (iPSC proof-of-concept); no clinical trials specific to *PRKDC*.
- **Allele-frequency and carrier data** for pathogenic *PRKDC* variants are sparse in population databases.

## Proposed Follow-up Experiments / Actions

1. **International *PRKDC* registry** to pool cases, standardize phenotyping, and quantify genotype–phenotype correlations and HSCT outcomes.
2. **Modifier screens** (WGS + transcriptomics) in patients sharing L3062R but divergent phenotypes to identify genetic/epigenetic modifiers of granuloma/autoimmunity.
3. **Humanized or neuron-focused models** (patient iPSC-derived cortical organoids) to interrogate the human-specific neuronal DSB-repair requirement.
4. **Mechanistic validation** of the DNA-PK–AIRE tolerance axis in patient thymic/mTEC systems, with therapeutic implications for autoimmunity.
5. **Radiosensitivity-adapted conditioning trials** (reduced-intensity/radiation-sparing) specifically in NHEJ/RS-SCID to optimize HSCT safety.
6. **Advancement of gene correction** from iPSC proof-of-concept toward in vivo/ex vivo gene-editing strategies, addressing whether hematopoietic correction suffices given non-hematopoietic requirements.
7. **Systematic rubella/live-vaccine surveillance** in granulomatous combined immunodeficiency to guide vaccine-avoidance policy.


## Artifacts

- [OpenScientist final report](Severe_Combined_Immunodeficiency_Due_To_DNA-PKcs_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Severe_Combined_Immunodeficiency_Due_To_DNA-PKcs_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 32 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014423` (2 mentions) - the report calls it "MONDO"; MONDO calls it **severe combined immunodeficiency due to DNA-PKcs deficiency**
- `HP:0004430` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Severe combined immunodeficiency**
- `HP:0000252` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Microcephaly**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `UBERON:0002371` (1 mention) - the report calls it "Primary:** hematolymphoid system — bone marrow"; UBERON calls it **bone marrow**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002543` (1 mention) - HP does not contain this term