---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-27T14:17:53.717757'
end_time: '2026-09-27T14:34:07.577931'
duration_seconds: 973.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Yersinia Enterocolitica Infectious Disease
  mondo_id: MONDO:0042370
  category: Infectious Disease
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
citation_count: 54
reference_validation:
  total_references: 54
  verified: 54
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:19058737
  relevance_assessed: 54
  on_topic: 19
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 35
  verified: 34
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 3
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0002014
    reported_labels:
    - Very common in enterocolitis
    ontology_label: Diarrhea
  - term_id: HP:0001945
    reported_labels:
    - Common
    ontology_label: Fever
  - term_id: HP:0002605
    reported_labels:
    - approximate
    ontology_label: Hepatic necrosis
  - term_id: HP:0100806
    reported_labels:
    - Rare; iron-overloaded/immunocompromised
    ontology_label: Sepsis
  - term_id: HP:0001369
    reported_labels:
    - "~1/1000 (ReA overall); young adults 18\u201340"
    ontology_label: Arthritis
  - term_id: HP:0012219
    reported_labels:
    - Occasional
    ontology_label: Erythema nodosum
  - term_id: HP:0000554
    reported_labels:
    - Occasional
    ontology_label: Uveitis
  - term_id: HP:0100647
    reported_labels:
    - "Association (see \xA75)"
    ontology_label: Graves disease
  - term_id: GO:0030260
    reported_labels:
    - entry into host cell
    ontology_label: GO_0030260
  - term_id: CHEBI:18248
    reported_labels:
    - CHEBI entities:** iron
    ontology_label: iron atom
  - term_id: UBERON:0002107
    reported_labels:
    - liver
    - Secondary organ involvement:** **liver
    ontology_label: liver
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0030260
    ontology_label: GO_0030260
    replaced_by: GO:0044409
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Yersinia_Enterocolitica_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Yersinia_Enterocolitica_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Yersinia Enterocolitica Infectious Disease
- **MONDO ID:** MONDO:0042370 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Yersinia Enterocolitica Infectious Disease** covering all of the
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

# Yersinia enterocolitica Infectious Disease (Yersiniosis): A Comprehensive Disease Characterization

**Disease:** Yersinia enterocolitica infectious disease (yersiniosis)
**MONDO ID:** MONDO:0042370 · **ICD-10:** A04.6 · **ICD-11:** 1A03 · **MeSH:** D015008 (Yersinia enterocolitica infection) / D015009 (Yersiniosis) · **Pathogen NCBI Taxon:** NCBI:txid630 · **Category:** Infectious Disease

---

## Summary

Yersinia enterocolitica infectious disease (yersiniosis) is a **foodborne zoonotic enteric infection** caused by the Gram-negative coccobacillus *Yersinia enterocolitica*. It is most commonly acquired through consumption of undercooked or contaminated **pork**, with swine serving as the principal reservoir of the human-pathogenic bioserotype 4/O:3 ([PMID: 26403101](https://pubmed.ncbi.nlm.nih.gov/26403101/), [PMID: 29307129](https://pubmed.ncbi.nlm.nih.gov/29307129/)). The organism is **psychrotolerant** (grows at 4 °C) and forms biofilms throughout the cold food chain, making it a persistent hazard in refrigerated foods, dairy, and blood products ([PMID: 41539755](https://pubmed.ncbi.nlm.nih.gov/41539755/)). Non-pestis yersiniosis has shown the largest increase in reported incidence of any bacterial enteric infection in the United States during 2016–2023 ([PMID: 42720049](https://pubmed.ncbi.nlm.nih.gov/42720049/)).

Mechanistically, after ingestion the bacterium colonizes the terminal ileum, uses the outer-membrane adhesin **invasin** to bind host **β1 integrins** on **M cells** overlying Peyer's patches, and invades follicle-associated lymphoid tissue ([PMID: 27107739](https://pubmed.ncbi.nlm.nih.gov/27107739/)). At 37 °C the ~70-kb **pYV virulence plasmid** activates (via the VirF/LcrF regulator) a **type III secretion system (T3SS)** that injects **Yop effector proteins** into phagocytes, subverting phagocytosis, actin dynamics, and NF-κB/MAPK survival and inflammasome signaling — YopP/YopJ in particular drives macrophage/dendritic-cell death ([PMID: 22563435](https://pubmed.ncbi.nlm.nih.gov/22563435/)). Host **iron status** is a decisive branch point: because *Y. enterocolitica* lacks its own high-affinity siderophore, iron overload and **deferoxamine** therapy dramatically increase virulence and the risk of septicemia, lowering the murine LD₅₀ by more than 5 log units ([PMID: 12019084](https://pubmed.ncbi.nlm.nih.gov/12019084/)).

The clinical spectrum is **age- and host-dependent**: self-limiting enterocolitis in young children; pseudoappendicitis (terminal ileitis / mesenteric adenitis) in older children and young adults; and invasive septicemia with hepatic/splenic abscesses in iron-overloaded or immunocompromised hosts ([PMID: 15254824](https://pubmed.ncbi.nlm.nih.gov/15254824/), [PMID: 9376035](https://pubmed.ncbi.nlm.nih.gov/9376035/)). Important **post-infectious sequelae** include HLA-B27-associated **reactive arthritis**, erythema nodosum, uveitis ([PMID: 40473988](https://pubmed.ncbi.nlm.nih.gov/40473988/), [PMID: 7221767](https://pubmed.ncbi.nlm.nih.gov/7221767/)), and **autoimmune thyroid disease / Graves' disease** via molecular mimicry between the bacterial outer-membrane porin OmpF and the TSH receptor ([PMID: 32564766](https://pubmed.ncbi.nlm.nih.gov/32564766/), [PMID: 20484489](https://pubmed.ncbi.nlm.nih.gov/20484489/)). Most cases resolve without antibiotics; invasive disease is treated with third-generation cephalosporins, fluoroquinolones, and/or aminoglycosides — the organism is intrinsically resistant to ampicillin and first-generation cephalosporins ([PMID: 10803262](https://pubmed.ncbi.nlm.nih.gov/10803262/)). No human vaccine exists; prevention relies on farm-to-fork food-chain hygiene ([PMID: 19058737](https://pubmed.ncbi.nlm.nih.gov/19058737/)).

---

## 1. Disease Information

**Overview.** Yersiniosis is an enteric infection caused by *Yersinia enterocolitica*, a Gram-negative, facultatively anaerobic, non-lactose-fermenting member of the Enterobacteriaceae. It is one of the more common causes of bacterial gastroenteritis in temperate regions and is notable for its psychrotolerance and its zoonotic, pork-associated transmission. Clinically it manifests along a spectrum from acute enteritis/enterocolitis to pseudoappendicitis and, in vulnerable hosts, septicemia ([PMID: 15254824](https://pubmed.ncbi.nlm.nih.gov/15254824/)).

**Key identifiers.** MONDO:0042370; ICD-10 A04.6 (Enteritis due to *Yersinia enterocolitica*); ICD-11 1A03 (Enteritis due to *Yersinia enterocolitica*); MeSH D015008/D015009; causative organism NCBI:txid630.

**Synonyms / alternative names.** Yersiniosis; intestinal yersiniosis; *Yersinia enterocolitica* enteritis/enterocolitis; enteric yersiniosis; non-pestis yersiniosis.

**Data provenance.** This report aggregates disease-level evidence from primary literature, microbiological surveillance, case reports, meta-analysis, and experimental (rodent/in-vitro) studies rather than individual EHR records.

---

## 2. Etiology

**Causal factor (infectious).** The disease is caused by pathogenic bioserotypes of *Y. enterocolitica*. Globally, the principal human-pathogenic serotypes are **O:3, O:9, O:8, and O:5,27**, with bioserotype **4/O:3** dominant in most regions ([PMID: 29307129](https://pubmed.ncbi.nlm.nih.gov/29307129/), [PMID: 40445798](https://pubmed.ncbi.nlm.nih.gov/40445798/)). Pigs are the primary reservoir; insufficiently cooked pork is the main vehicle ([PMID: 26403101](https://pubmed.ncbi.nlm.nih.gov/26403101/)).

**Environmental / exposure risk factors.** Consumption of raw or undercooked pork (including chitterlings), unpasteurized dairy, and contaminated water; cold-chain storage that permits psychrotolerant growth; transfusion via contaminated blood products; occupational contact in the pork production chain. Young age is a risk factor for enterocolitis.

**Host risk factors (the key modifier — iron).** **Iron overload** and iron-chelation therapy with **deferoxamine** are the most important host risk factors for severe/invasive disease. In a mouse model, deferoxamine pretreatment decreased the LD₅₀ of *Y. enterocolitica* by **>5 log units**, whereas deferiprone did not ([PMID: 12019084](https://pubmed.ncbi.nlm.nih.gov/12019084/)). Transfusion-dependent conditions (β-thalassemia, sickle cell disease) and dialysis iron supplementation predispose to fulminant infection ([PMID: 31219970](https://pubmed.ncbi.nlm.nih.gov/31219970/), [PMID: 21266629](https://pubmed.ncbi.nlm.nih.gov/21266629/), [PMID: 11698009](https://pubmed.ncbi.nlm.nih.gov/11698009/), [PMID: 21151549](https://pubmed.ncbi.nlm.nih.gov/21151549/)). Diabetes, malignancy, and other immunocompromising conditions also predispose to bacteremia ([PMID: 9376035](https://pubmed.ncbi.nlm.nih.gov/9376035/)).

**Genetic host factor.** **HLA-B27** is a genetic susceptibility factor for the post-infectious complication of reactive arthritis ([PMID: 7221767](https://pubmed.ncbi.nlm.nih.gov/7221767/)).

**Protective factors.** Thorough cooking of pork, pasteurization, cold-chain hygiene, and biosecurity reduce exposure. Mucosal innate defenses (e.g., Paneth-cell α-defensin HD6, which entraps enteric pathogens in self-assembled nanonets) limit invasion ([PMID: 22722251](https://pubmed.ncbi.nlm.nih.gov/22722251/)). Use of the oral iron chelators **deferiprone/deferasirox** instead of deferoxamine avoids promoting bacterial growth ([PMID: 12019084](https://pubmed.ncbi.nlm.nih.gov/12019084/), [PMID: 19413741](https://pubmed.ncbi.nlm.nih.gov/19413741/)).

**Gene–environment interaction.** The clearest interaction is **iron availability × siderophore biology**: exogenous ferrioxamine (from deferoxamine) supplies iron the bacterium cannot otherwise scavenge, converting a contained mucosal infection into systemic disease. A second interaction is **HLA-B27 × enteric infection**, where a genetically predisposed host mounts an aberrant post-infectious arthritic response.

---

## 3. Phenotypes

| Phenotype | Type | Onset / course | Frequency | HPO suggestion |
|---|---|---|---|---|
| Diarrhea (often watery, sometimes bloody) | Symptom | Acute, self-limiting | Very common in enterocolitis | HP:0002014 |
| Abdominal pain (right-lower-quadrant) | Symptom | Acute | Common; prominent in pseudoappendicitis | HP:0002027 / HP:0002574 |
| Fever | Sign | Acute | Common | HP:0001945 |
| Terminal ileitis / mesenteric lymphadenitis | Clinical sign | Subacute | Older children/adults | HP:0002583 (enterocolitis) |
| Pseudoappendicitis | Clinical syndrome | Acute | Older children/young adults | HP:0002605 (approximate) |
| Septicemia / bacteremia | Lab/clinical | Acute, severe | Rare; iron-overloaded/immunocompromised | HP:0100806 |
| Hepatic/splenic abscesses | Manifestation | Invasive disease | Rare | HP:0012199 / HP:0020104 |
| Reactive arthritis (asymmetric, lower-limb) | Post-infectious | Days–weeks after infection | ~1/1000 (ReA overall); young adults 18–40 | HP:0001369 |
| Erythema nodosum | Post-infectious skin sign | Weeks after | Occasional | HP:0012219 |
| Uveitis | Post-infectious | Weeks after | Occasional | HP:0000554 |
| Graves' disease / autoimmune thyroiditis | Post-infectious autoimmune | Delayed | Association (see §5) | HP:0100647 |

**Characteristics.** Onset is typically **acute**; enterocolitis is generally **self-limiting** (1–3 weeks). Severity ranges from mild (children) to life-threatening (septicemia in iron overload). Post-infectious immunological syndromes are episodic/delayed ([PMID: 8363822](https://pubmed.ncbi.nlm.nih.gov/8363822/), [PMID: 3545747](https://pubmed.ncbi.nlm.nih.gov/3545747/)).

**Quality-of-life impact.** Acute enterocolitis causes short-term disability from diarrhea/pain; pseudoappendicitis may lead to unnecessary appendectomy. Reactive arthritis and other post-infectious syndromes can cause prolonged joint pain and functional impairment persisting weeks to months ([PMID: 32648451](https://pubmed.ncbi.nlm.nih.gov/32648451/)).

---

## 4. Genetic / Molecular Information

*Yersiniosis is an infectious, not a Mendelian, disease; there are no causal human genes.* The relevant genetics are (a) **host susceptibility loci** and (b) **bacterial virulence genes**.

**Host genetics.** HLA-B27 predisposes to post-infectious reactive arthritis ([PMID: 7221767](https://pubmed.ncbi.nlm.nih.gov/7221767/)). No causal germline variants, chromosomal abnormalities, or pathogenic ACMG-classified variants apply to the disease itself. gnomAD/ClinVar entries are **not applicable**.

**Bacterial virulence genetics.** Pathogenicity of biotypes 1B and 2–5 depends on **both chromosomal and pYV plasmid-borne genes**; biotype 1A lacks pYV ([PMID: 28400007](https://pubmed.ncbi.nlm.nih.gov/28400007/)).

- **Chromosomal:** *ail* (attachment-invasion locus; principal chromosomal virulence marker — [PMID: 28283072](https://pubmed.ncbi.nlm.nih.gov/28283072/)); *inv* (invasin); *ystA* (heat-stable enterotoxin YstA; best marker of pathogenic biotypes — [PMID: 28400007](https://pubmed.ncbi.nlm.nih.gov/28400007/)); *myfA* (fimbriae); *hreP* (protease). Biotype 1A carries *ystB* and *hreP* but lacks *ail/ystA* ([PMID: 39805396](https://pubmed.ncbi.nlm.nih.gov/39805396/)).
- **Plasmid (pYV, ~70 kb):** *virF/lcrF* (master transcriptional activator of the T3SS regulon), *yadA* (adhesin), and the *ysc* operon encoding the T3SS (e.g., *yscE, F, G, I, J, K, H*) plus *yop* effector genes ([PMID: 8709853](https://pubmed.ncbi.nlm.nih.gov/8709853/)). YstA enterotoxin production is **pYV-independent** ([PMID: 30961808](https://pubmed.ncbi.nlm.nih.gov/30961808/)).

---

## 5. Environmental Information

**Infectious agent.** *Yersinia enterocolitica* (NCBI:txid630); a species divided into ~6 biotypes and ~60 O-serotypes, with O:3, O:9, O:8, O:5,27 principally associated with human disease ([PMID: 40445798](https://pubmed.ncbi.nlm.nih.gov/40445798/)).

**Environmental factors.** The organism's **psychrotolerance** (growth at 4 °C) and **biofilm formation** enable persistence across refrigerated foods and food-processing environments; slaughterhouses (40.2%) and farmers' markets (34.8%) are high-risk contamination zones ([PMID: 41539755](https://pubmed.ncbi.nlm.nih.gov/41539755/)). Contaminated red-blood-cell units support proliferation during cold storage, a recognized transfusion hazard ([PMID: 33341965](https://pubmed.ncbi.nlm.nih.gov/33341965/)).

**Lifestyle / dietary factors.** Consumption of raw/undercooked pork (notably chitterlings), unpasteurized milk/dairy (18% of US outbreak vehicles), and untreated water ([PMID: 42720049](https://pubmed.ncbi.nlm.nih.gov/42720049/)). Pork accounted for 46% of identified US outbreak vehicles.

**Reservoirs.** Swine are the primary reservoir (bioserotype 4/O:3); wildlife (badgers, roe deer, mustelids), poultry, and other livestock also carry the organism ([PMID: 40582279](https://pubmed.ncbi.nlm.nih.gov/40582279/), [PMID: 41527869](https://pubmed.ncbi.nlm.nih.gov/41527869/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating exposure → clinical manifestation)

1. **Ingestion** of *Y. enterocolitica* in contaminated pork/dairy/water **leads to** delivery of viable bacteria to the small intestine (survival aided by psychrotolerance and acid tolerance).
2. Bacteria **colonize the terminal ileum**; expression of chromosomal adhesins/invasins is favored at intestinal temperature/pH.
3. **Invasin binds host β1 integrins** on the apical surface of **M cells** overlying Peyer's patches, **resulting in** receptor-mediated internalization and translocation across the follicle-associated epithelium ([PMID: 27107739](https://pubmed.ncbi.nlm.nih.gov/27107739/), [PMID: 26731748](https://pubmed.ncbi.nlm.nih.gov/26731748/)). *(Invasin is rapidly degraded by gut proteases, which limits the efficiency of this step — [PMID: 21501502](https://pubmed.ncbi.nlm.nih.gov/21501502/).)*
4. Uptake by **lamina propria CD103⁺ dendritic cells and monocyte-derived phagocytes** (invasin-dependent; YadA dispensable) **leads to** dissemination to mesenteric lymph nodes, and in some hosts the spleen and liver ([PMID: 27107739](https://pubmed.ncbi.nlm.nih.gov/27107739/)).
5. At **37 °C**, the **VirF/LcrF regulator induces the pYV-encoded T3SS**, which upon host-cell contact **injects Yop effectors** (YopH, YopE, YopT, YopO, YopP/J, YopM) into phagocytes ([PMID: 8709853](https://pubmed.ncbi.nlm.nih.gov/8709853/)).
6. Yop effectors **subvert innate immunity**: YopH/E/T/O disrupt phagocytosis and actin dynamics; **YopP/YopJ inhibits NF-κB/MAPK survival pathways, causing macrophage/DC apoptosis** and modulating caspase-1/IL-1β ([PMID: 22563435](https://pubmed.ncbi.nlm.nih.gov/22563435/), [PMID: 18559430](https://pubmed.ncbi.nlm.nih.gov/18559430/)). This **results in** immune evasion and local tissue inflammation → **enterocolitis / terminal ileitis / mesenteric adenitis / pseudoappendicitis**.
7. **YstA heat-stable enterotoxin** activates guanylate cyclase in enterocytes, **contributing to** secretory diarrhea ([PMID: 28400007](https://pubmed.ncbi.nlm.nih.gov/28400007/), [PMID: 30961808](https://pubmed.ncbi.nlm.nih.gov/30961808/)).

**Branch A — host iron status → septicemia.** Because *Y. enterocolitica* lacks a high-affinity siderophore, **iron overload or deferoxamine therapy supplies chelated iron (ferrioxamine)**, which **leads to** unrestrained bacterial replication and **systemic septicemia with hepatic/splenic abscesses** ([PMID: 12019084](https://pubmed.ncbi.nlm.nih.gov/12019084/), [PMID: 31219970](https://pubmed.ncbi.nlm.nih.gov/31219970/)).

**Branch B — post-infectious autoimmunity.** In HLA-B27⁺ hosts, enteric infection **triggers reactive arthritis** ([PMID: 7221767](https://pubmed.ncbi.nlm.nih.gov/7221767/)). Independently, **molecular mimicry** between the bacterial outer-membrane porin **OmpF (aa190–197)** and a leucine-rich domain of the **TSH receptor** generates cross-reactive, thyroid-stimulating antibodies, **contributing to Graves' disease / autoimmune thyroid disease** ([PMID: 20484489](https://pubmed.ncbi.nlm.nih.gov/20484489/), [PMID: 32564766](https://pubmed.ncbi.nlm.nih.gov/32564766/)).

### Mechanistic categories

- **Molecular pathways:** T3SS/Yop-mediated inhibition of **NF-κB and MAPK** signaling; modulation of the **pyrin and caspase-1 inflammasomes** ([PMID: 31456795](https://pubmed.ncbi.nlm.nih.gov/31456795/), [PMID: 22563435](https://pubmed.ncbi.nlm.nih.gov/22563435/)); integrin/FAK signaling on invasion ([PMID: 26731748](https://pubmed.ncbi.nlm.nih.gov/26731748/)). GO suggestions: GO:0030260 (entry into host cell), GO:0052031 (modulation by symbiont of host defense response), GO:0043123 (positive regulation of NF-κB signaling — inhibited).
- **Cellular processes:** macrophage/DC **apoptosis**, inhibited phagocytosis, inflammation, MDSC-mediated immunosuppression ([PMID: 39529636](https://pubmed.ncbi.nlm.nih.gov/39529636/)).
- **Protein dysfunction (host):** Yop-driven dephosphorylation (YopH phosphatase) and cytoskeletal GTPase inactivation.
- **Immune involvement:** ILC3-mediated mucosal protection ([PMID: 32147792](https://pubmed.ncbi.nlm.nih.gov/32147792/)); neutrophils resist YopJ/P-induced apoptosis ([PMID: 20174624](https://pubmed.ncbi.nlm.nih.gov/20174624/)); autoimmunity via mimicry (§5).
- **Cell types (CL):** M cell (CL:0000682), dendritic cell (CL:0000451), macrophage (CL:0000235), neutrophil (CL:0000775), enterocyte (CL:0000584).
- **CHEBI entities:** iron (CHEBI:18248), deferoxamine (CHEBI:4356), ferrioxamine B (CHEBI:87109).

---

## 7. Anatomical Structures Affected

- **Primary organs/systems (digestive):** terminal **ileum** (UBERON:0002116), **Peyer's patches** (UBERON:0001211), **mesenteric lymph nodes** (UBERON:0002509), **appendix/cecum** region (pseudoappendicitis) ([PMID: 15254824](https://pubmed.ncbi.nlm.nih.gov/15254824/)).
- **Secondary organ involvement:** **liver** (UBERON:0002107) and **spleen** (UBERON:0002106) abscesses in septicemia; joints (reactive arthritis); skin (erythema nodosum); eye (uveitis); thyroid gland (Graves'); rarely heart (myopericarditis — [PMID: 35728146](https://pubmed.ncbi.nlm.nih.gov/35728146/)) and inner ear/vestibular system ([PMID: 9376035](https://pubmed.ncbi.nlm.nih.gov/9376035/)).
- **Tissue/cell level:** intestinal **follicle-associated epithelium** and M cells; lymphoid tissue; mononuclear phagocytes.
- **Subcellular (GO cellular component):** host plasma membrane / β1-integrin complex (GO:0008305); host cytoskeleton (targeted by Yops); bacterial T3SS injectisome.
- **Lateralization:** reactive arthritis is characteristically **asymmetric**, lower-extremity oligoarthritis.

---

## 8. Temporal Development

- **Onset:** acute, typically 4–7 days after ingestion; enterocolitis predominates in infants/young children, pseudoappendicitis in older children/young adults ([PMID: 15254824](https://pubmed.ncbi.nlm.nih.gov/15254824/)).
- **Progression / duration:** enterocolitis is usually **self-limiting** over 1–3 weeks; diarrhea can occasionally persist. Septicemia is acute and can be fulminant, especially with rapid decompensation after transfusion in iron-overloaded patients ([PMID: 31219970](https://pubmed.ncbi.nlm.nih.gov/31219970/)).
- **Post-infectious window:** reactive arthritis and erythema nodosum appear **days to weeks** after the enteric phase; autoimmune thyroid sequelae are more delayed.
- **Course pattern:** acute self-limited enteric phase; post-infectious syndromes may be episodic/relapsing. **Critical intervention windows:** early antibiotics in high-risk (iron-overloaded/immunocompromised) hosts; avoidance of deferoxamine during suspected infection.

---

## 9. Inheritance and Population (Epidemiology)

- **Not heritable** — infectious etiology; no Mendelian inheritance, penetrance, founder effects, or carrier frequency apply. Host susceptibility to sequelae is modulated by HLA-B27.
- **Incidence trend:** non-pestis yersiniosis had **the largest increase in reported incidence of any bacterial enteric infection in the US during 2016–2023** ([PMID: 42720049](https://pubmed.ncbi.nlm.nih.gov/42720049/)).
- **Reservoir prevalence:** *Y. enterocolitica* isolated from **9.31%** of pig tonsils (bioserotype 4/O:3 = 95.74%) ([PMID: 29307129](https://pubmed.ncbi.nlm.nih.gov/29307129/)); ~9.3% porcine tonsils and 3.3% pig faeces in other surveys ([PMID: 19058737](https://pubmed.ncbi.nlm.nih.gov/19058737/)); ~9.3–9.7% prevalence in retail meats ([PMID: 41527869](https://pubmed.ncbi.nlm.nih.gov/41527869/), [PMID: 40382034](https://pubmed.ncbi.nlm.nih.gov/40382034/)).
- **Geographic distribution:** worldwide in temperate/cold climates; bioserotype 4/O:3 predominant in Europe/Asia; highly pathogenic 1B/O:8 historically North American but now reported in Iran ([PMID: 40669762](https://pubmed.ncbi.nlm.nih.gov/40669762/)).
- **Age distribution:** enterocolitis skews to young children (<5 years — [PMID: 40669762](https://pubmed.ncbi.nlm.nih.gov/40669762/)); pseudoappendicitis to older children/young adults.
- **Seasonality:** cold-season predominance consistent with psychrotolerance ([PMID: 40669762](https://pubmed.ncbi.nlm.nih.gov/40669762/)).

---

## 10. Diagnostics

**Culture (gold standard).** Stool culture on **CIN (cefsulodin–irgasan–novobiocin) agar** with **cold enrichment** (4 °C) enhances recovery — cold enrichment recovered ~25% of 4/O:3 and 2/O:9 strains not otherwise detected ([PMID: 19219471](https://pubmed.ncbi.nlm.nih.gov/19219471/)). Blood culture in suspected septicemia.

**Bio/serotyping.** Congo-red magnesium-oxalate (**CR-MOX**) agar detects the pYV virulence plasmid; biochemical panels assign biotype; agglutination/PCR serotyping identifies O:3, O:9, O:8, O:5,27 ([PMID: 19219471](https://pubmed.ncbi.nlm.nih.gov/19219471/), [PMID: 40445798](https://pubmed.ncbi.nlm.nih.gov/40445798/)).

**Molecular confirmation.** PCR for virulence genes (**ail, ystA/ystB, virF, yadA, inv, myfA**) distinguishes pathogenic from non-pathogenic (biotype 1A) strains; 16S rRNA and *gyrB* sequencing resolves *Y. enterocolitica*-like species; multiplex/quadruplex RT-qPCR patho-serotyping is available ([PMID: 19219471](https://pubmed.ncbi.nlm.nih.gov/19219471/), [PMID: 40445798](https://pubmed.ncbi.nlm.nih.gov/40445798/)).

**Serology.** Anti-*Yersinia* antibody titers (e.g., against O:3, O:9) support diagnosis of post-infectious syndromes such as reactive arthritis ([PMID: 9376035](https://pubmed.ncbi.nlm.nih.gov/9376035/)). Caveat: O:9 cross-reacts serologically with *Brucella*.

**Imaging.** CT/ultrasound in pseudoappendicitis shows terminal ileitis and mesenteric lymphadenopathy (helping avoid unnecessary appendectomy).

**Differential diagnosis.** Acute appendicitis, Crohn's disease/terminal ileitis, *Campylobacter*/*Salmonella*/*Shigella* enterocolitis, mesenteric adenitis of other cause.

---

## 11. Outcome / Prognosis

- **Enterocolitis:** excellent prognosis; usually **self-limiting** without antibiotics.
- **Pseudoappendicitis:** favorable; risk of unnecessary surgery.
- **Septicemia:** serious, with mortality concentrated in iron-overloaded/immunocompromised patients; requires prompt IV antibiotics ([PMID: 21266629](https://pubmed.ncbi.nlm.nih.gov/21266629/), [PMID: 31219970](https://pubmed.ncbi.nlm.nih.gov/31219970/)). Case reports document successful treatment (e.g., 14-day ceftriaxone) with resolution and no recurrence.
- **Post-infectious morbidity:** reactive arthritis (ReA overall prevalence ~1/1000) can cause weeks-to-months of joint disability ([PMID: 40473988](https://pubmed.ncbi.nlm.nih.gov/40473988/)); persistent extraintestinal manifestations (uveitis, erythema nodosum, rare vestibular loss/myopericarditis) ([PMID: 9376035](https://pubmed.ncbi.nlm.nih.gov/9376035/), [PMID: 35728146](https://pubmed.ncbi.nlm.nih.gov/35728146/)).
- **Prognostic factors:** host iron status, immunocompetence, age, timeliness of antibiotic therapy, and infecting bioserotype (1B/O:8 highly pathogenic).

---

## 12. Treatment

**General principle.** Uncomplicated enterocolitis is **self-limiting** and generally does **not** require antibiotics; supportive care (rehydration) suffices. Antibiotics are indicated for **invasive/septicemic disease** and in high-risk hosts.

**Antimicrobial susceptibility profile.**

| Antimicrobial class | Susceptibility | Evidence |
|---|---|---|
| Ampicillin, 1st-gen cephalosporins (cefazolin) | **Intrinsically RESISTANT** (chromosomal β-lactamases blaA/blaB) | [PMID: 10803262](https://pubmed.ncbi.nlm.nih.gov/10803262/), [PMID: 10755244](https://pubmed.ncbi.nlm.nih.gov/10755244/) |
| 3rd-gen cephalosporins (cefotaxime, ceftriaxone) | **Susceptible — drug of choice** | [PMID: 10803262](https://pubmed.ncbi.nlm.nih.gov/10803262/), [PMID: 21266629](https://pubmed.ncbi.nlm.nih.gov/21266629/) |
| Fluoroquinolones (ciprofloxacin, ofloxacin) | **Susceptible; highly effective in models** | [PMID: 10803262](https://pubmed.ncbi.nlm.nih.gov/10803262/), [PMID: 1952849](https://pubmed.ncbi.nlm.nih.gov/1952849/) |
| Aminoglycosides (gentamicin) | Susceptible | [PMID: 10755244](https://pubmed.ncbi.nlm.nih.gov/10755244/), [PMID: 20828475](https://pubmed.ncbi.nlm.nih.gov/20828475/) |
| TMP-SMX, tetracyclines, chloramphenicol, imipenem, aztreonam | Susceptible | [PMID: 10755244](https://pubmed.ncbi.nlm.nih.gov/10755244/) |

Susceptibility is independent of the pYV plasmid ([PMID: 10755244](https://pubmed.ncbi.nlm.nih.gov/10755244/)). In murine systemic infection, newer β-lactams may fail while fluoroquinolones (ofloxacin, 5 mg/kg) are very effective ([PMID: 1952849](https://pubmed.ncbi.nlm.nih.gov/1952849/)).

**Regimens.** Septicemia is typically treated with a **third-generation cephalosporin** (e.g., ceftriaxone) ± an **aminoglycoside** or a **fluoroquinolone**; combination therapy is used for severe disease. NCIT term suggestions: Ceftriaxone (NCIT:C749), Ciprofloxacin (NCIT:C405), Gentamicin (NCIT:C557), Trimethoprim-Sulfamethoxazole (NCIT:C273).

**Critical host management.** In iron-overloaded patients, **discontinue deferoxamine** during infection and consider deferiprone/deferasirox, which do not promote bacterial growth ([PMID: 12019084](https://pubmed.ncbi.nlm.nih.gov/12019084/), [PMID: 19413741](https://pubmed.ncbi.nlm.nih.gov/19413741/)).

**AMR surveillance.** Prudent antimicrobial use in pig farming is emphasized to limit resistance-gene spread via horizontal transfer ([PMID: 41413462](https://pubmed.ncbi.nlm.nih.gov/41413462/), [PMID: 35369517](https://pubmed.ncbi.nlm.nih.gov/35369517/)).

**Advanced/experimental therapeutics.** Not applicable — no gene/cell/RNA/targeted therapies; treatment is antimicrobial and supportive.

---

## 13. Prevention

- **Primary prevention (food-chain hygiene — the mainstay):** "Good hygienic slaughter practices are essential to prevent contamination of pork" ([PMID: 19058737](https://pubmed.ncbi.nlm.nih.gov/19058737/)). Thorough cooking of pork, pasteurization of dairy, avoidance of cross-contamination, on-farm biosecurity, and cold-chain management from farm to fork ([PMID: 40023561](https://pubmed.ncbi.nlm.nih.gov/40023561/)). Key on-farm risk factors to mitigate: batch mixing in fattening herds and poor pen cleaning/biosecurity ([PMID: 19175574](https://pubmed.ncbi.nlm.nih.gov/19175574/)).
- **Immunization:** **No licensed human vaccine exists.** Oral mucosal-vaccine constructs using *Y. enterocolitica* OmpH as a carrier are experimental ([PMID: 32569608](https://pubmed.ncbi.nlm.nih.gov/32569608/)).
- **Secondary prevention:** microbiological surveillance of the pork chain; molecular subtyping (SNP/MLST) to track transmission hotspots (slaughterhouses, markets) ([PMID: 41539755](https://pubmed.ncbi.nlm.nih.gov/41539755/)).
- **Tertiary prevention:** in iron-overloaded/dialysis patients, monitor ferritin, avoid deferoxamine when infection is suspected, and screen blood products (transfusion transmission hazard) ([PMID: 21266629](https://pubmed.ncbi.nlm.nih.gov/21266629/), [PMID: 33341965](https://pubmed.ncbi.nlm.nih.gov/33341965/)).
- **Public health:** food-safety education, blood-bank visual inspection/interdiction of contaminated RBC units.

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected/reservoir species:** *Sus scrofa domesticus* (pig; NCBI:txid9825) — primary reservoir; also cattle, sheep, poultry (chicken, duck), dogs, cats, and wildlife (badgers, roe deer, mustelids) ([PMID: 40582279](https://pubmed.ncbi.nlm.nih.gov/40582279/), [PMID: 41527869](https://pubmed.ncbi.nlm.nih.gov/41527869/)).
- **Zoonotic transmission:** fecal–oral via contaminated food, water, and animal contact; strong swine–human genomic link established by pangenome analysis ([PMID: 41413462](https://pubmed.ncbi.nlm.nih.gov/41413462/)). Environmental persistence broadens the ecology.
- **Comparative pathology:** pigs are typically **asymptomatic carriers** (tonsils, gut, mesenteric nodes), unlike humans who develop enteric disease — an important distinction for control.
- **Evolutionary conservation:** T3SS/Yop virulence mechanisms are conserved across pathogenic *Yersinia* (*Y. enterocolitica*, *Y. pseudotuberculosis*, *Y. pestis*), enabling cross-species mechanistic inference ([PMID: 18559430](https://pubmed.ncbi.nlm.nih.gov/18559430/), [PMID: 38271464](https://pubmed.ncbi.nlm.nih.gov/38271464/)).

---

## 15. Model Organisms

- **Rodent oral-infection models faithfully recapitulate human yersiniosis:** "experimental *Y. enterocolitica* infection in rodents resembles yersiniosis in humans and thus offers extraordinary opportunities to study the sequential steps of the infectious process" ([PMID: 8363822](https://pubmed.ncbi.nlm.nih.gov/8363822/)).
- **Mouse (C57BL/6):** oral infection with serotype O:8 strains (WA-314, WAP-314) models Peyer's-patch/M-cell entry, ILC3-mediated protection ([PMID: 32147792](https://pubmed.ncbi.nlm.nih.gov/32147792/)), NO-producing Mo-MDSC immunosuppression ([PMID: 39529636](https://pubmed.ncbi.nlm.nih.gov/39529636/)), and bacterial population dynamics ([PMID: 35205164](https://pubmed.ncbi.nlm.nih.gov/35205164/)). The deferoxamine-potentiation LD₅₀ experiment was performed in mice ([PMID: 12019084](https://pubmed.ncbi.nlm.nih.gov/12019084/)).
- **Rabbit:** models enterotoxin-mediated enteritis and humoral response ([PMID: 8363822](https://pubmed.ncbi.nlm.nih.gov/8363822/)).
- **In vitro / cellular:** Caco-2 intestinal epithelial cells for invasin–β1-integrin internalization ([PMID: 26731748](https://pubmed.ncbi.nlm.nih.gov/26731748/)); primary macrophages/neutrophils for Yop-mediated apoptosis studies ([PMID: 22563435](https://pubmed.ncbi.nlm.nih.gov/22563435/), [PMID: 20174624](https://pubmed.ncbi.nlm.nih.gov/20174624/)); suckling-mouse bioassay for YstA enterotoxin activity ([PMID: 39805396](https://pubmed.ncbi.nlm.nih.gov/39805396/)).
- **Computational:** ODE-based models of gastrointestinal bacterial population dynamics ([PMID: 35205164](https://pubmed.ncbi.nlm.nih.gov/35205164/)).
- **Limitations:** mouse strains used experimentally are often serotype O:8 (highly pathogenic 1B), which may not reflect the globally dominant 4/O:3; post-infectious autoimmune sequelae (Graves', HLA-B27 ReA) are not well captured in rodents.

---

## Mechanistic Model / Integrated Interpretation

```
   Contaminated pork/dairy/water (psychrotolerant, biofilm)
                     │  ingestion
                     ▼
        Terminal ileum colonization
                     │  invasin → β1 integrin (M cells)
                     ▼
        Peyer's patch invasion ── (gut proteases degrade invasin: limiting)
                     │  CD103+ DC / monocyte uptake
                     ▼
        Mesenteric lymph nodes ──► spleen/liver (dissemination)
                     │  37°C → VirF/LcrF → T3SS
                     ▼
        Yop injection (YopH/E/T/O/P-J/M)
          inhibits phagocytosis, NF-κB/MAPK, inflammasome
                     │
        ┌────────────┼───────────────────────────┐
        ▼            ▼                            ▼
  Enterocolitis /   Branch A: IRON OVERLOAD    Branch B: POST-INFECTION
  pseudoappendicitis  + deferoxamine            HLA-B27 → reactive arthritis
  (+ YstA enterotoxin) → SEPTICEMIA,            OmpF≈TSHR mimicry → Graves'
   → diarrhea        hepatic/splenic abscess    erythema nodosum, uveitis
```

**Upstream vs downstream.** Invasin-mediated M-cell entry is the upstream initiating event; T3SS/Yop immune subversion is the central amplifying node; enterocolitis, septicemia, and autoimmune sequelae are downstream outcomes gated by host iron status and HLA background.

---

## Evidence Base (key literature)

| PMID | Contribution | Type |
|---|---|---|
| [26403101](https://pubmed.ncbi.nlm.nih.gov/26403101/) | Swine/pork as reservoir & main infection source | Review |
| [29307129](https://pubmed.ncbi.nlm.nih.gov/29307129/) | 9.31% pig-tonsil prevalence; 4/O:3 = 95.74% | Surveillance |
| [12019084](https://pubmed.ncbi.nlm.nih.gov/12019084/) | Deferoxamine lowers LD₅₀ >5 log; deferiprone does not | Model organism |
| [31219970](https://pubmed.ncbi.nlm.nih.gov/31219970/) | Transfusional iron overload → fulminant yersiniosis | Case report |
| [27107739](https://pubmed.ncbi.nlm.nih.gov/27107739/) | Invasin-dependent DC/M-cell uptake & dissemination | Mechanistic |
| [22563435](https://pubmed.ncbi.nlm.nih.gov/22563435/) | YopJ inhibits survival pathways → macrophage death | Mechanistic |
| [40473988](https://pubmed.ncbi.nlm.nih.gov/40473988/) | Y. enterocolitica as post-enteric ReA trigger | Review |
| [7221767](https://pubmed.ncbi.nlm.nih.gov/7221767/) | ReA linked to HLA-B27 | Case report |
| [32564766](https://pubmed.ncbi.nlm.nih.gov/32564766/) | Graves' association OR 6.12 (3.71–10.10) | Meta-analysis |
| [20484489](https://pubmed.ncbi.nlm.nih.gov/20484489/) | OmpF–TSHR molecular mimicry | In vitro |
| [42720049](https://pubmed.ncbi.nlm.nih.gov/42720049/) | Rising US incidence; pork 46%, dairy 18% | Surveillance |
| [19219471](https://pubmed.ncbi.nlm.nih.gov/19219471/) | Culture/cold-enrichment diagnostics; bioserotype prevalence | Surveillance |
| [10803262](https://pubmed.ncbi.nlm.nih.gov/10803262/) | 3rd-gen cephalosporins & ciprofloxacin most active | In vitro |
| [1952849](https://pubmed.ncbi.nlm.nih.gov/1952849/) | Fluoroquinolone efficacy vs β-lactam failure | Model organism |
| [15254824](https://pubmed.ncbi.nlm.nih.gov/15254824/) | Three clinical syndromes defined | Review |
| [19058737](https://pubmed.ncbi.nlm.nih.gov/19058737/) | Slaughter hygiene as key prevention | Surveillance |
| [8363822](https://pubmed.ncbi.nlm.nih.gov/8363822/) | Rodent model fidelity to human disease | Review |
| [28400007](https://pubmed.ncbi.nlm.nih.gov/28400007/) | ystA best pathogenicity marker; ystB for 1A | Molecular |
| [28283072](https://pubmed.ncbi.nlm.nih.gov/28283072/) | ail as main chromosomal virulence marker | Molecular |
| [41539755](https://pubmed.ncbi.nlm.nih.gov/41539755/) | Psychrotolerance/biofilm across cold chain | Surveillance |

---

## Limitations and Knowledge Gaps

- **No human genetic causal architecture** — as an infectious disease, sections on causal genes, pathogenic ACMG variants, inheritance, penetrance, and carrier frequency are **not applicable**; only host modifiers (HLA-B27, iron-handling) are relevant.
- **Quantitative human epidemiology is incomplete** here — precise population incidence/prevalence per 100,000 and absolute mortality rates were not extracted; the strongest quantitative signal is the documented US incidence *increase* rather than an absolute rate.
- **Causal certainty of autoimmune sequelae** — the Graves'/AITD association is epidemiological (OR-based meta-analysis) plus a plausible mimicry mechanism; direct causation in humans remains inferential.
- **Model–strain mismatch** — much mechanistic work uses highly pathogenic 1B/O:8 mouse strains, whereas most human disease is 4/O:3; findings may not fully transfer.
- **Effect sizes for some clinical claims** (e.g., proportion progressing to septicemia, ReA incidence specifically after *Yersinia*) rely on case series and reviews rather than large cohorts.

## Proposed Follow-up Actions

1. **Extract absolute incidence/prevalence** from GBD, CDC FoodNet, and Orphanet to complete Section 9 quantitatively.
2. **Systematic review of HLA-B27 penetrance** for *Yersinia*-triggered reactive arthritis (attributable risk, time-to-onset).
3. **Prospective study** of oral iron-chelator choice (deferiprone/deferasirox vs deferoxamine) on yersiniosis incidence in transfusion-dependent patients.
4. **Genomic surveillance (One Health)** linking swine and human isolates via SNP/MLST to quantify attributable transmission and AMR gene flow ([PMID: 41413462](https://pubmed.ncbi.nlm.nih.gov/41413462/)).
5. **4/O:3-based infection models** to align mechanistic studies with the globally dominant human bioserotype.
6. **Mechanistic test of OmpF–TSHR mimicry in vivo** to establish causality for the Graves' association.

---

*Report compiled from 13 confirmed findings across 73 reviewed papers over 5 investigation iterations. Evidence types are labeled (human clinical, model organism, in vitro, computational, surveillance/review) throughout.*


## Artifacts

- [OpenScientist final report](Yersinia_Enterocolitica_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Yersinia_Enterocolitica_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 54 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 54 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:19058737` *(abstract only)*: "Good hygienic slaughter practices are essential to prevent contamination of pork"
  - closest text in source: "Good hygienic slaughter practices are essential to prevent the contamination of pork with pathogenic Y"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 18 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002014` (1 mention) - the report calls it "Very common in enterocolitis"; HP calls it **Diarrhea**
- `HP:0001945` (1 mention) - the report calls it "Common"; HP calls it **Fever**
- `HP:0002605` (1 mention) - the report calls it "approximate"; HP calls it **Hepatic necrosis**
- `HP:0100806` (1 mention) - the report calls it "Rare; iron-overloaded/immunocompromised"; HP calls it **Sepsis**
- `HP:0001369` (1 mention) - the report calls it "~1/1000 (ReA overall); young adults 18–40"; HP calls it **Arthritis**
- `HP:0012219` (1 mention) - the report calls it "Occasional"; HP calls it **Erythema nodosum**
- `HP:0000554` (1 mention) - the report calls it "Occasional"; HP calls it **Uveitis**
- `HP:0100647` (1 mention) - the report calls it "Association (see §5)"; HP calls it **Graves disease**
- `GO:0030260` (1 mention) - the report calls it "entry into host cell"; GO calls it **GO_0030260**
- `CHEBI:18248` (1 mention) - the report calls it "CHEBI entities:** iron"; CHEBI calls it **iron atom**
- `UBERON:0002107` (1 mention) - the report calls it "liver", "Secondary organ involvement:** **liver"; UBERON calls it **liver**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0030260` (GO_0030260) (1 mention) - replaced by `GO:0044409`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002583` (1 mention) - the report calls it "enterocolitis"; HP calls it **Colitis**
- `GO:0052031` (1 mention) - the report calls it "modulation by symbiont of host defense response"; GO calls it **symbiont-mediated perturbation of host defense response**, and lists "modulation by symbiont of host defense response" among its other names
- `GO:0043123` (1 mention) - the report calls it "positive regulation of NF-κB signaling — inhibited"; GO calls it **positive regulation of canonical NF-kappaB signal transduction**, and lists "positive regulation of I-kappaB kinase/NF-kappaB signaling" among its other names
- `UBERON:0001211` (1 mention) - the report calls it "Peyer's patches"; UBERON calls it **Peyer's patch**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002107` - called "liver", "Secondary organ involvement:** **liver"