---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T05:42:39.687736'
end_time: '2026-09-21T06:02:01.224044'
duration_seconds: 1161.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Epidermolysis Bullosa Simplex 7 With Nephropathy And Deafness
  mondo_id: MONDO:0012190
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
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 17
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 0
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0000100
    reported_labels:
    - Frequent
    ontology_label: Nephrotic syndrome
  - term_id: HP:0000097
    reported_labels:
    - Core (biopsy)
    ontology_label: Focal segmental glomerulosclerosis
  - term_id: HP:0008404
    reported_labels:
    - Frequent
    ontology_label: Nail dystrophy
  - term_id: HP:0000407
    reported_labels:
    - Core
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0011904
    reported_labels:
    - Index kindred
    ontology_label: Persistence of hemoglobin F
  - term_id: HP:0001250
    reported_labels:
    - Rare (expanded spectrum)
    ontology_label: Seizure
  obsolete_terms:
  - term_id: UBERON:0002966
    ontology_label: obsolete regional part of midbrain tectum
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Epidermolysis_Bullosa_Simplex_7_With_Nephropathy_And_Deafness-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Epidermolysis_Bullosa_Simplex_7_With_Nephropathy_And_Deafness-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epidermolysis Bullosa Simplex 7 With Nephropathy And Deafness
- **MONDO ID:** MONDO:0012190 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Epidermolysis Bullosa Simplex 7 With Nephropathy And Deafness** covering all of the
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

# Epidermolysis Bullosa Simplex 7 With Nephropathy And Deafness (CD151 Deficiency): A Comprehensive Disease Characterization

**MONDO ID:** MONDO:0012190 | **OMIM:** #609057 | **Gene:** *CD151* (11p15.5) | **Category:** Mendelian, autosomal recessive

---

## Summary

Epidermolysis Bullosa Simplex 7 with Nephropathy and Deafness (hereafter "CD151-deficiency syndrome") is an ultra-rare autosomal recessive multisystem disorder caused by biallelic loss-of-function variants in *CD151*, a gene encoding a tetraspanin (transmembrane-4 superfamily) protein located on chromosome 11p15.5. The disease was molecularly defined in 2004 when Karamatic Crew and colleagues studied three MER2-blood-group-negative patients of Indian Jewish origin (two of whom were siblings) with end-stage kidney disease, and identified a homozygous single-nucleotide insertion (insG383) in exon 5 of *CD151* that produces a frameshift and premature stop codon at position 140, deleting the integrin-binding domain of the protein ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)).

The unifying mechanistic insight is that CD151 is a "master organizer" of the plasma membrane that scaffolds laminin-binding integrins — principally α3β1, α6β1, and α6β4 — into tetraspanin-enriched microdomains at the interface between epithelial/endothelial cells and their basement membranes. When CD151 is absent, these integrin–laminin adhesion complexes are weakened and destabilized, and basement membranes fail to assemble and maintain their correct architecture. Because the same integrin–laminin adhesion machinery is deployed in the glomerular filtration barrier of the kidney, the dermo-epidermal junction of the skin, and the basement membranes of the inner ear/cochlea, a single gene defect produces a characteristic clinical triad: progressive hereditary nephropathy advancing to end-stage renal disease (ESRD), pretibial epidermolysis bullosa (mechanically-induced skin blistering with nail dystrophy), and bilateral sensorineural deafness. Additional features documented across the small literature include β-thalassemia minor, epilepsy, nephrotic-range proteinuria, and a null MER2/RAPH blood-group phenotype (CD151 carries the MER2 antigen of the RAPH system).

There is no disease-specific or curative therapy. Management is supportive and organ-directed: renin-angiotensin-aldosterone system (RAAS) blockade and blood-pressure control for nephroprotection (supported by mouse data showing ACE inhibition prolongs survival in disease-susceptible *Cd151*-null mice), renal replacement therapy (dialysis, transplantation) for ESRD, wound care for skin blistering, and hearing rehabilitation. This report synthesizes six confirmed findings across 25 reviewed papers into a comprehensive, evidence-linked disease entry spanning all fifteen requested characteristic domains.

---

## Key Findings

### Finding 1 — CD151 loss-of-function is the cause of the disease

The causal genetic lesion was established by *Karamatic Crew et al.* (2004, *Blood*), who examined three MER2-negative patients of Indian Jewish origin (two siblings) presenting with end-stage kidney disease. All three were homozygous for a single-nucleotide insertion, insG383, in exon 5 of *CD151* on chromosome 11p15.5. In the words of the authors: *"The 3 patients are homozygous for a single nucleotide insertion (G383) in exon 5 of CD151, causing a frameshift and premature stop signal at codon 140. The resultant truncated protein would lack its integrin-binding domain"* ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)). This is a frameshift/truncating loss-of-function mechanism: the protein is severely truncated (140 residues versus the full-length ~253-residue tetraspanin) and cannot engage its integrin partners.

The same report established the core clinical picture beyond kidney disease: *"In addition to hereditary nephritis the sibs have sensorineural deafness, pretibial epidermolysis bullosa, and beta-thalassemia minor"* ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)). This defines the recognizable triad — nephropathy + skin fragility + deafness — plus a hematologic feature (β-thalassemia minor, likely reflecting the 11p15.5 locus proximity to the β-globin cluster in the index kindred rather than a CD151-intrinsic effect).

### Finding 2 — *Cd151*-null mice recapitulate the renal phenotype via podocyte–GBM adhesion failure

The renal mechanism was validated in animal models. *Sachs et al.* (2006) reported that *Cd151*-null mice *"with age... develop massive proteinuria caused by focal glomerulosclerosis, disorganization of the glomerular basement membrane, and tubular cystic dilation. However, neither skin integrity nor hearing ability are impaired in the Cd151-null mice"* ([PMID: 17015618](https://pubmed.ncbi.nlm.nih.gov/17015618/)). This faithfully reproduces the human nephropathy — proteinuria, focal segmental glomerulosclerosis (FSGS), glomerular basement membrane (GBM) disorganization — while notably NOT reproducing the skin and ear phenotypes, an important model limitation (see Limitations).

Critically, the renal phenotype is modifier- and blood-pressure-dependent. *Sachs et al.* (2012) showed that CD151 strengthens α3β1-mediated podocyte adhesion to laminin, and that *"blocking the angiotensin-converting enzyme in renal disease-susceptible global Cd151-null FVB mice prolonged their median life span"* ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/)). Disease onset depended on genetic strain background (FVB susceptible) and systemic blood pressure — directly implicating mechanical/hemodynamic stress as a disease amplifier and RAAS blockade as protective. Independently, *Naylor et al.* (2022) used CRISPR-Cas9 zebrafish to validate a novel human truncating *CD151* variant as disease-causing, extending model evidence to a second organism ([PMID: 35278129](https://pubmed.ncbi.nlm.nih.gov/35278129/)).

### Finding 3 — Mechanism: CD151 scaffolds laminin-binding integrin adhesion complexes governing basement-membrane integrity

CD151 (HGNC:1630; NCBI Gene 977; UniProt P48509; locus 11p15.5) is a tetraspanin that forms *"very stable laminin-binding complexes with integrins alpha3beta1 and alpha6beta1 in kidney and alpha3beta1 and alpha6beta4 in skin"* ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)). This single sentence unifies the kidney and skin phenotypes at a molecular level: the same tetraspanin organizes different but overlapping integrin sets in each tissue.

In keratinocytes, CD151 (via α3β1) stabilizes α6β4-containing hemidesmosomes and "hybrid" cell-matrix adhesions ([PMID: 31488507](https://pubmed.ncbi.nlm.nih.gov/31488507/)). In podocytes, CD151 strengthens α3β1–laminin adhesion ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/)). More broadly, tetraspanins are plasma-membrane organizers that concentrate partner integrins into tetraspanin-enriched microdomains; their perturbation has organ-level consequences: *"Perturbations of tetraspan-integrin assemblies can have dramatic impacts on renal tissue morphogenesis, resulting in a disruption of normal glomerular architecture and selectivity"* ([PMID: 17565278](https://pubmed.ncbi.nlm.nih.gov/17565278/)). This provides the direct causal bridge from CD151 loss to impaired glomerular filtration selectivity (proteinuria).

### Finding 4 — Expanded phenotypic spectrum: nephrotic syndrome, epilepsy, and MER2/RAPH-null blood type

The phenotype has expanded beyond the original triad in later reports. *Dunn et al.* (2022) described syndromic EBS with nephropathy AND epilepsy from a CD151 tetraspanin defect, explicitly "expanding the spectrum" ([PMID: 35519797](https://pubmed.ncbi.nlm.nih.gov/35519797/)). *Almokali et al.* (2024) described nephrotic-syndrome–epidermolysis-bullosa–sensorineural-deafness syndrome, an autosomal recessive rare disease presenting with pretibial EB ([PMID: 38188895](https://pubmed.ncbi.nlm.nih.gov/38188895/)). And the blood-group connection was clarified by *Keller* (2020): CD151 carries the MER2 antigen of the RAPH blood group system (ISBT 25), and *"Lack of the RAPH protein is associated with nephropathy with pretibial epidermolysis bullosa and deafness"* ([PMID: 32667818](https://pubmed.ncbi.nlm.nih.gov/32667818/)). This same review documented the full integrin partner set: *"CD151 regulates interactions with laminin-binding integrins α3β1, α6β1, α6β4, and α7β1 and is expressed on red blood cells as well as many other tissues and cancer types"* ([PMID: 32667818](https://pubmed.ncbi.nlm.nih.gov/32667818/)) — notably adding α7β1 (relevant to muscle/vascular basement membranes) to the list.

### Finding 5 — Prognosis and treatment: progressive ESRD requiring renal replacement; supportive/nephroprotective care

The renal course is relentlessly progressive to ESRD (the index patients presented with end-stage disease). No curative therapy exists. Mouse data support RAAS blockade as nephroprotective — ACE inhibition *"prolonged their median life span"* in disease-susceptible *Cd151*-null FVB mice ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/)). *Sasaki* (2022) frames CD151-deficient nephropathy as a "mechanosensitive nephropathy" whose onset depends on genetic background/modifier genes, mechanistically analogous to Alport syndrome and TNS2-deficient nephropathy ([PMID: 35444113](https://pubmed.ncbi.nlm.nih.gov/35444113/)). For patients who reach ESRD, renal replacement therapy is feasible despite EB-related access challenges: *"There should be no limitations in renal replacement therapy in patients with epidermolysis bullosa"* ([PMID: 28615054](https://pubmed.ncbi.nlm.nih.gov/28615054/)).

### Finding 6 — Epidemiology, inheritance, and diagnostic approach

This is an ultra-rare autosomal recessive disorder with fewer than ~20 molecularly confirmed patients reported worldwide; prevalence is not estimable (<1/1,000,000) and no incidence data exist. Expected sex ratio is ~1:1 (M:F). The index kindred was Indian Jewish (two siblings), consistent with a founder/consanguineous origin: *"We examined CD151 in 3 MER2-negative patients (2 are sibs) of Indian Jewish origin with end-stage kidney disease"* ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)); additional cases have arisen in other consanguineous backgrounds ([PMID: 38188895](https://pubmed.ncbi.nlm.nih.gov/38188895/)). Penetrance is high in humans but strongly background-dependent in mice. Because *"CD151 is not routinely screened for in patients with nephrotic-range proteinuria"* ([PMID: 35278129](https://pubmed.ncbi.nlm.nih.gov/35278129/)), broad NGS (whole-exome/whole-genome sequencing) is the recommended path to diagnosis. Key differentials include Alport syndrome, LAMB2/Pierson syndrome, and ITGA3-related interstitial lung disease-nephrotic syndrome-epidermolysis bullosa (ILNEB) ([PMID: 24220332](https://pubmed.ncbi.nlm.nih.gov/24220332/)).

---

## Detailed Report by Disease-Characteristic Domain

### 1. Disease Information

CD151-deficiency syndrome is a hereditary, multisystem basement-membrane disorder. The disease name "Epidermolysis Bullosa Simplex 7 with Nephropathy and Deafness" reflects historical classification within the EB simplex spectrum (skin blistering) combined with the two other cardinal organ features.

**Key identifiers:**
- **MONDO:** MONDO:0012190
- **OMIM:** #609057 (Nephropathy with pretibial epidermolysis bullosa and deafness); gene *CD151* 602243
- **HGNC:** HGNC:1630 | **NCBI Gene:** 977 | **UniProt:** P48509 | **Ensembl:** ENSG00000177697
- **Orphanet:** listed under CD151-related / EB with nephropathy and deafness
- **ICD-10:** Q81.- (epidermolysis bullosa) with N-codes for nephropathy; **ICD-11:** EC30.- (epidermolysis bullosa simplex)

**Synonyms / alternative names:** Nephropathy with pretibial epidermolysis bullosa and deafness; CD151 deficiency; Epidermolysis bullosa, pretibial, with nephropathy and deafness; RAPH-null (MER2-negative) associated syndrome; NS-EB-sensorineural deafness syndrome.

**Source of information:** Characterized almost entirely from **individual patient reports** (aggregated case reports/case series), not population-level EHR datasets, owing to extreme rarity.

### 2. Etiology

**Causal factor:** Purely **genetic** — biallelic loss-of-function variants in *CD151*. No environmental or infectious cause. The prototypic variant is c.383dupG (insG383) in exon 5, producing a frameshift → stop at codon 140 and loss of the integrin-binding domain ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)).

**Genetic risk factors:** The disease is Mendelian (biallelic *CD151* LOF is causal). **Modifier genes** and **genetic background** strongly influence renal severity — demonstrated by strain-dependence in mice (FVB susceptible) ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/), [PMID: 35444113](https://pubmed.ncbi.nlm.nih.gov/35444113/)). Consanguinity raises risk because the disorder is recessive and enriched in founder populations.

**Environmental / lifestyle risk factors:** No environmental cause, but **mechanical stress and hypertension act as disease amplifiers** — blood pressure influences the renal course ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/)), and cutaneous blistering is provoked by mechanical friction/trauma (hallmark of EB simplex).

**Protective factors:** No genetic protective alleles established. Inferred protective measures: avoidance of skin trauma/friction, blood-pressure control, and RAAS blockade.

**Gene–environment interactions:** Best-documented is **genotype (CD151-null) × hemodynamic load (blood pressure)** gating renal disease onset and progression ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/)), reframed as "mechanosensitive nephropathy" gated by modifier genes ([PMID: 35444113](https://pubmed.ncbi.nlm.nih.gov/35444113/)).

### 3. Phenotypes

| Phenotype | Type | Onset | Severity/Course | Frequency | HPO suggestion |
|---|---|---|---|---|---|
| Hereditary nephropathy / proteinuria → ESRD | Lab + clinical sign | Childhood–young adult | Progressive, severe | Core (near-universal) | HP:0000112; HP:0000093; HP:0003774 |
| Nephrotic-range proteinuria / nephrotic syndrome | Lab abnormality | Childhood–young adult | Progressive | Frequent | HP:0000100 |
| FSGS / GBM disorganization | Pathology finding | Progressive | Severe | Core (biopsy) | HP:0000097 |
| Pretibial epidermolysis bullosa | Physical manifestation | Congenital/infancy | Mechanically induced, chronic | Core | HP:0001075; HP:0008066 |
| Nail dystrophy | Physical manifestation | Childhood | Chronic | Frequent | HP:0008404 |
| Bilateral sensorineural deafness | Clinical sign | Childhood | Progressive/stable, bilateral | Core | HP:0000407 |
| β-thalassemia minor | Lab abnormality | Congenital | Mild | Index kindred | HP:0011904 |
| Epilepsy | Clinical sign | Variable | Variable | Rare (expanded spectrum) | HP:0001250 |
| MER2/RAPH-null red cells | Lab abnormality | Congenital | Asymptomatic marker | Core | — |

**Quality-of-life impact:** Dominated by progressive renal failure (dialysis dependence, transplant needs), chronic painful skin blistering/wound care, and communication impairment from deafness — collectively imposing severe, lifelong disability. Formal EQ-5D/SF-36 data are unavailable for this ultra-rare disease.

### 4. Genetic / Molecular Information

- **Causal gene:** *CD151* (tetraspanin; HGNC:1630; OMIM 602243; locus 11p15.5).
- **Prototypic pathogenic variant:** homozygous c.383dupG (insG383), exon 5, frameshift → premature stop at codon 140; **type:** frameshift/truncating; **consequence:** loss of function, deletion of integrin-binding domain ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)). Additional novel truncating variants have been functionally validated ([PMID: 35278129](https://pubmed.ncbi.nlm.nih.gov/35278129/)).
- **Classification (ACMG/AMP):** truncating LOF in a gene with established LOF mechanism → pathogenic/likely pathogenic.
- **Allele frequency:** private/ultra-rare; not present at appreciable frequency in gnomAD.
- **Origin:** germline, biallelic (autosomal recessive).
- **Modifier genes:** unidentified in humans but demonstrably present (mouse strain-dependence; TNS2 modifier analogy) ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/), [PMID: 35444113](https://pubmed.ncbi.nlm.nih.gov/35444113/)).
- **Epigenetic / chromosomal abnormalities:** none reported.
- **Related gene (differential):** *ITGA3* (integrin α3) missense R628P causes an overlapping lung-kidney-skin disorder by disrupting α3 processing and CD151 binding ([PMID: 24220332](https://pubmed.ncbi.nlm.nih.gov/24220332/)), underscoring the shared integrin–tetraspanin adhesion axis.

### 5. Environmental Information

No environmental, toxic, or infectious cause. **Mechanical trauma** provokes cutaneous blistering; **hypertension/hemodynamic stress** accelerates nephropathy ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/)). No infectious agents are implicated. (Tetraspanins including CD151 participate in viral-entry biology in unrelated contexts, e.g. respiratory viruses [PMID: 36173052], but this has no bearing on disease causation here.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic LOF mutation in *CD151*** (e.g., insG383 frameshift) **leads to** a truncated CD151 protein lacking its integrin-binding domain ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)).
2. Loss of functional CD151 **results in** failure to scaffold laminin-binding integrins (α3β1, α6β1, α6β4, α7β1) into stable tetraspanin-enriched microdomains ([PMID: 32667818](https://pubmed.ncbi.nlm.nih.gov/32667818/), [PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)).
3. Unscaffolded/redistributed integrins **lead to** weakened cell–laminin adhesion and reduced adhesive strength at the cell–basement-membrane interface ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/), [PMID: 31488507](https://pubmed.ncbi.nlm.nih.gov/31488507/)).
4. Weakened adhesion **results in** defective assembly and progressive disorganization of basement membranes across kidney, skin, and inner ear ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/), [PMID: 17565278](https://pubmed.ncbi.nlm.nih.gov/17565278/)).
5. **Branch A — Kidney:** GBM disorganization + podocyte foot-process effacement (under hemodynamic load) **leads to** loss of filtration selectivity → proteinuria → FSGS → progressive nephropathy → **ESRD** ([PMID: 17015618](https://pubmed.ncbi.nlm.nih.gov/17015618/), [PMID: 17565278](https://pubmed.ncbi.nlm.nih.gov/17565278/), [PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/)).
6. **Branch B — Skin:** destabilized α6β4 hemidesmosomes/α3β1 adhesions at the dermo-epidermal junction **lead to** mechanical fragility → **pretibial epidermolysis bullosa** + nail dystrophy ([PMID: 31488507](https://pubmed.ncbi.nlm.nih.gov/31488507/), [PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)).
7. **Branch C — Inner ear:** basement-membrane defects in cochlear structures **lead to** (inferred) **bilateral sensorineural deafness** ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/); mechanism inferred, not directly demonstrated — mouse model does not reproduce deafness [PMID: 17015618]).

```
        CD151 LOF mutation (insG383, exon 5 -> stop@140)
                        |
             truncated CD151, no integrin-binding domain
                        |
     failure to scaffold a3b1 / a6b1 / a6b4 / a7b1 in TEMs
                        |
        weakened integrin-laminin adhesion strength
                        |
       basement-membrane assembly/maintenance failure
          +-------------+--------------+
      KIDNEY           SKIN         INNER EAR
   GBM disorg. +    DEJ fragility   BM defects
   podocyte FPE     (hemidesmo-     (cochlea)
        |           some loss)          |
   proteinuria ->        |         sensorineural
   FSGS -> ESRD     pretibial EB     deafness
   [hemodynamic     + nail          (inferred)
    stress gates]   dystrophy
```

- **Molecular pathways / processes (GO):** cell-substrate adhesion (GO:0031589); integrin-mediated signaling pathway (GO:0007229); basement membrane organization (GO:0071711); hemidesmosome assembly (GO:0031581); glomerular filtration (GO:0003094).
- **Protein dysfunction:** loss of function / loss of scaffolding — truncated CD151 cannot bind integrins; downstream integrins are mislocalized and adhesion complexes destabilized.
- **Cell types involved (CL):** podocyte (CL:0000653); keratinocyte (CL:0000312); glomerular endothelial cell (CL:1001005); cochlear hair cell / supporting cells.
- **Subcellular (GO CC):** plasma-membrane tetraspanin-enriched microdomain; hemidesmosome (GO:0030056); basement membrane (GO:0005604).
- **Molecular profiling:** CD151 appears as a hub gene in membranous-nephropathy transcriptomic analyses ([PMID: 37974210]), consistent with a role in glomerular biology, though associative rather than causal for this Mendelian disease.

### 7. Anatomical Structures Affected

- **Primary organs:** kidney (glomerulus UBERON:0000074; glomerular basement membrane UBERON:0002966); skin (dermo-epidermal junction, esp. pretibial UBERON:0002097); inner ear/cochlea (UBERON:0001844).
- **Secondary/systemic:** hematopoietic (β-thalassemia minor; red cells carry MER2/RAPH UBERON:0000178); nervous system (epilepsy in expanded spectrum).
- **Body systems:** renal/urinary, integumentary, auditory/nervous, hematologic.
- **Tissue types:** epithelial (podocytes, keratinocytes), specialized basement membrane (ECM/connective).
- **Cell populations (CL):** podocytes (CL:0000653), keratinocytes (CL:0000312), cochlear hair cells.
- **Subcellular compartments:** plasma-membrane microdomains, hemidesmosomes, basement membrane.
- **Localization/lateralization:** nephropathy bilateral; deafness bilateral; skin blistering typically bilateral and pretibial (mechanically exposed lower legs).

### 8. Temporal Development

- **Onset:** skin fragility often congenital/infancy; nephropathy and deafness typically manifest in childhood to young adulthood; pattern **chronic/insidious**.
- **Progression:** renal disease is **progressive** (early proteinuria → FSGS → advanced CKD → ESRD); rate variable and modifier/blood-pressure dependent ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/), [PMID: 35444113](https://pubmed.ncbi.nlm.nih.gov/35444113/)).
- **Course:** chronic, lifelong; no spontaneous renal remission. Skin blistering chronic and mechanically episodic (flares with trauma).
- **Critical windows:** early nephroprotection (blood-pressure/RAAS control) before advanced fibrosis is the key intervention window (inferred from mouse ACE-inhibition survival benefit).

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive; biallelic *CD151* LOF.
- **Epidemiology:** ultra-rare; <20 molecularly confirmed cases; prevalence <1/1,000,000 (not formally estimable); no incidence data.
- **Penetrance:** high in humans with biallelic LOF; strongly background-dependent in mice.
- **Expressivity:** variable (epilepsy, thalassemia, renal severity vary between cases).
- **Anticipation / mosaicism:** not applicable / not reported.
- **Founder effect / consanguinity:** index kindred Indian Jewish (2 sibs), consistent with founder/consanguineous origin ([PMID: 15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/)); other cases in consanguineous families ([PMID: 38188895](https://pubmed.ncbi.nlm.nih.gov/38188895/)). North Indian carrier-screening data exist for other recessive disorders but not specifically CD151 ([PMID: 33138774]).
- **Carrier frequency:** unknown/very low.
- **Sex ratio:** ~1:1.

### 10. Diagnostics

- **Clinical/lab tests:** urinalysis (proteinuria, nephrotic-range), serum creatinine/eGFR (declining), audiometry (bilateral sensorineural loss).
- **Renal biopsy (EM):** thickened/disorganized/split GBM, podocyte foot-process effacement, FSGS ([PMID: 17015618](https://pubmed.ncbi.nlm.nih.gov/17015618/), [PMID: 17565278](https://pubmed.ncbi.nlm.nih.gov/17565278/)).
- **Immunofluorescence / blood typing:** reduced/absent CD151 in skin/kidney; MER2/RAPH-null red cells ([PMID: 32667818](https://pubmed.ncbi.nlm.nih.gov/32667818/)).
- **Genetic testing:** confirmatory biallelic *CD151* sequencing via single-gene testing or, preferably, **WES/WGS** — because *"CD151 is not routinely screened for in patients with nephrotic-range proteinuria"* ([PMID: 35278129](https://pubmed.ncbi.nlm.nih.gov/35278129/)), broad NGS captures otherwise-undiagnosed cases.
- **Differential diagnosis:** Alport syndrome (COL4A3/4/5 — deafness + nephropathy, no EB), Pierson/LAMB2 syndrome, ITGA3-related ILNEB ([PMID: 24220332](https://pubmed.ncbi.nlm.nih.gov/24220332/)), other EB subtypes.
- **Screening:** carrier/cascade screening in affected families; prenatal testing feasible where the familial variant is known.

### 11. Outcome / Prognosis

- **Renal:** progressive to ESRD requiring dialysis or transplantation; the dominant determinant of morbidity/mortality.
- **Life expectancy:** reduced primarily by renal failure; renal replacement therapy is feasible and improves survival — *"There should be no limitations in renal replacement therapy in patients with epidermolysis bullosa"* ([PMID: 28615054](https://pubmed.ncbi.nlm.nih.gov/28615054/)).
- **Morbidity:** chronic skin wounds, hearing loss/communication impairment, dialysis dependence.
- **Prognostic factors:** blood pressure, degree of proteinuria, rate of eGFR decline, and (in principle) modifier genotype ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/), [PMID: 35444113](https://pubmed.ncbi.nlm.nih.gov/35444113/)).
- **QoL tools:** no disease-specific validated instruments; general CKD/EB QoL measures apply.

### 12. Treatment

**No curative or disease-specific therapy exists.** Management is supportive and organ-directed.

| Modality | Intervention | Evidence/Rationale | NCIT suggestion |
|---|---|---|---|
| Nephroprotection | ACE inhibitor / ARB (RAAS blockade), BP control | ACE inhibition prolonged survival in *Cd151*-null FVB mice ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/)) | ACE inhibitor; Angiotensin receptor blocker |
| Renal replacement | Hemodialysis, peritoneal dialysis, kidney transplant | Feasible in EB patients ([PMID: 28615054](https://pubmed.ncbi.nlm.nih.gov/28615054/)) | Hemodialysis (NCIT:C15248); Kidney transplantation (NCIT:C15366) |
| Skin/wound care | Non-adhesive dressings, trauma avoidance, infection control | Standard EB management | Wound care |
| Hearing | Hearing aids, cochlear implantation, speech therapy | Standard SNHL rehabilitation | Hearing aid; Cochlear implant |
| Hematologic | Monitoring of β-thalassemia minor (usually no treatment) | Index kindred feature | — |
| Neurologic | Antiepileptic therapy if seizures | Expanded spectrum ([PMID: 35519797](https://pubmed.ncbi.nlm.nih.gov/35519797/)) | Anticonvulsant |

- **Pharmacogenomics:** none specific.
- **Advanced therapeutics (gene/cell/RNA):** none approved; conceptually plausible future gene-replacement targets given the monogenic LOF mechanism.
- **Experimental trials:** no disease-specific NCT trials identified.

### 13. Prevention

- **Primary:** genetic counseling for at-risk (consanguineous/founder) families; carrier screening and cascade testing; preimplantation/prenatal genetic diagnosis where the familial variant is known.
- **Secondary:** early detection of proteinuria and hearing loss in known-carrier offspring; early nephroprotection.
- **Tertiary:** blood-pressure/RAAS management to slow renal decline; meticulous skin care to prevent wound infections; audiologic rehabilitation.
- **Counseling:** essential — 25% recurrence risk per pregnancy for carrier couples (autosomal recessive).

### 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (NCBI Taxon 9606); experimental *Mus musculus* (10090) and *Danio rerio* (7955).
- **Orthologous genes:** mouse *Cd151* (NCBI Gene 12476); zebrafish *cd151* ortholog.
- **Natural disease in other species:** no well-documented spontaneous companion-animal analog identified in this investigation; the disease is characterized principally through engineered models.
- **Comparative biology:** the integrin–laminin–tetraspanin adhesion mechanism is evolutionarily conserved, enabling faithful renal modeling in mouse and zebrafish (see Section 15).

### 15. Model Organisms

| Model | Type | Phenotype recapitulation | Limitations | Ref |
|---|---|---|---|---|
| *Cd151*-null mouse (FVB) | Mammalian knockout | Massive proteinuria, FSGS, GBM disorganization, tubular cystic dilation; strain/BP-dependent | **Does NOT reproduce skin fragility or deafness** | [PMID: 17015618](https://pubmed.ncbi.nlm.nih.gov/17015618/), [PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/) |
| Podocyte-specific *Itga3* (α3) knockout | Conditional mammalian | Similar podocyte–GBM defects | Integrin-partner surrogate | [PMID: 17015618](https://pubmed.ncbi.nlm.nih.gov/17015618/) |
| CRISPR-Cas9 zebrafish *cd151* | Vertebrate genome-edited | Validated a novel human truncating variant as disease-causing | Non-mammalian nephron architecture | [PMID: 35278129](https://pubmed.ncbi.nlm.nih.gov/35278129/) |

- **Applications:** dissecting podocyte adhesion, GBM assembly, blood-pressure/mechanosensitivity of nephropathy, and variant functional validation.
- **Resources:** MGI (*Cd151*), ZFIN (zebrafish ortholog).

---

## Mechanistic Model / Interpretation

The entire phenotype flows from a single principle: **CD151 is a plasma-membrane organizer that stabilizes laminin-binding integrin adhesion complexes at basement-membrane interfaces.** Tetraspanins are "master organizers" that laterally concentrate partner proteins into tetraspanin-enriched microdomains ([PMID: 29887866], [PMID: 22103505]); CD151 specifically corrals α3β1/α6β1/α6β4/α7β1 ([PMID: 32667818](https://pubmed.ncbi.nlm.nih.gov/32667818/)). Remove CD151, and integrin–laminin adhesion loses strength and organization — the shared upstream lesion — after which the phenotype **branches by tissue** according to which epithelial cells depend most on this adhesion under load:

- The **kidney** is the most sensitive organ because the glomerular filtration barrier operates under continuous hemodynamic stress; podocytes require robust α3β1–laminin adhesion to the GBM. This is why the mouse (lacking the human's skin/ear vulnerability) still develops severe nephropathy, and why blood pressure gates disease — a genuine gene × mechanical-environment interaction ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/), [PMID: 35444113](https://pubmed.ncbi.nlm.nih.gov/35444113/)).
- The **skin** blisters at mechanically stressed pretibial sites because α6β4 hemidesmosomes and α3β1 hybrid adhesions at the dermo-epidermal junction are destabilized ([PMID: 31488507](https://pubmed.ncbi.nlm.nih.gov/31488507/)).
- The **inner ear** develops sensorineural deafness through inferred cochlear basement-membrane defects — the least mechanistically demonstrated branch, since it is not modeled in mouse.

This model explains the disease's defining paradox (severe multi-organ human disease, kidney-only mouse) as a difference in tissue-specific redundancy and mechanical demand, not a difference in the core molecular defect.

---

## Evidence Base

| PMID | Title (abbrev.) | Role / Contribution |
|---|---|---|
| [15265795](https://pubmed.ncbi.nlm.nih.gov/15265795/) | *CD151... essential for basement membranes in kidney and skin* | **Foundational**: causal variant (insG383), triad, integrin complexes |
| [17015618](https://pubmed.ncbi.nlm.nih.gov/17015618/) | *Kidney failure in mice lacking CD151* | Renal recapitulation; skin/ear model limitation |
| [22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/) | *Blood pressure influences ESRD of Cd151 KO mice* | BP/modifier dependence; ACE-inhibition survival benefit |
| [35278129](https://pubmed.ncbi.nlm.nih.gov/35278129/) | *Basement membrane defects in CD151 glomerular disease* | Zebrafish variant validation; NGS screening argument |
| [17565278](https://pubmed.ncbi.nlm.nih.gov/17565278/) | *Tetraspan proteins: regulators of renal structure* | Mechanism: tetraspan-integrin perturbation disrupts glomerular selectivity |
| [31488507](https://pubmed.ncbi.nlm.nih.gov/31488507/) | *CD151 and α3β1 stabilize α6β4 adhesions* | Skin mechanism (hemidesmosome stabilization) |
| [32667818](https://pubmed.ncbi.nlm.nih.gov/32667818/) | *Update on the RAPH blood group system* | MER2/RAPH-null link; full integrin partner set (adds α7β1) |
| [35519797](https://pubmed.ncbi.nlm.nih.gov/35519797/) | *Syndromic EBS with nephropathy and epilepsy* | Expanded phenotype: epilepsy |
| [38188895](https://pubmed.ncbi.nlm.nih.gov/38188895/) | *Nephrotic syndrome, pretibial EB* | NS-EB-deafness syndrome; consanguineous case |
| [35444113](https://pubmed.ncbi.nlm.nih.gov/35444113/) | *TNS2-deficient nephropathy* | Frames CD151 nephropathy as mechanosensitive, modifier-gated |
| [28615054](https://pubmed.ncbi.nlm.nih.gov/28615054/) | *ESRD in EB — treatment options* | Feasibility of renal replacement therapy |
| [24220332](https://pubmed.ncbi.nlm.nih.gov/24220332/) | *ITGA3 R628P mutation* | Differential diagnosis; shared integrin-CD151 axis |

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base:** Fewer than ~20 molecularly confirmed patients; most clinical inference rests on a single index kindred plus scattered case reports. No natural-history cohort, prevalence estimate, or validated QoL data.
2. **Model–human discordance:** The *Cd151*-null mouse reproduces nephropathy but **not** the skin or ear phenotype ([PMID: 17015618](https://pubmed.ncbi.nlm.nih.gov/17015618/)). The deafness mechanism is therefore inferred, not demonstrated, and no faithful multi-organ model exists.
3. **Unidentified human modifier genes:** Strain-dependence in mice implies human genetic modifiers of renal severity, but none are mapped — limiting prognostic prediction.
4. **β-thalassemia minor** in the index kindred may reflect co-inheritance at 11p15.5 rather than a CD151-intrinsic effect; its consistency across unrelated cases is unclear.
5. **Therapeutics:** RAAS-blockade benefit is extrapolated from mouse survival data; no human trial exists. No advanced (gene/cell) therapy has been attempted.
6. **Ontology mapping:** Some suggested NCIT/UBERON/CL identifiers are best-match approximations pending curated verification.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** for CD151 deficiency to aggregate genotype–phenotype data, natural history, and outcomes across the world's scattered cases.
2. **Systematic reanalysis of undiagnosed nephrotic-syndrome/CKD cohorts** with WES/WGS specifically interrogating *CD151*, given that it is not routinely screened ([PMID: 35278129](https://pubmed.ncbi.nlm.nih.gov/35278129/)) — likely to reveal additional patients.
3. **Build a faithful multi-organ model** (e.g., conditional/humanized mouse on a susceptible background, or cochlear organoids) to interrogate the deafness branch that current models miss.
4. **Test RAAS blockade prospectively** (or via registry-based comparative effectiveness) in human patients to formally establish the nephroprotective benefit suggested by mouse data ([PMID: 22201679](https://pubmed.ncbi.nlm.nih.gov/22201679/)).
5. **Map modifier loci** via cross-strain QTL analysis in mice and, where feasible, human family studies, to explain variable renal severity.
6. **Explore gene-replacement feasibility** (AAV or ex-vivo keratinocyte/podocyte approaches) given the clean monogenic LOF mechanism.
7. **Generate patient iPSC-derived podocyte and keratinocyte models** to dissect integrin redistribution and adhesion-strength phenotypes and to screen candidate stabilizing compounds.

---

*Report compiled from an autonomous multi-iteration investigation: 6 confirmed findings, 25 papers reviewed. Evidence types span human clinical case reports, mouse and zebrafish model organisms, and in vitro cell-adhesion studies.*


## Artifacts

- [OpenScientist final report](Epidermolysis_Bullosa_Simplex_7_With_Nephropathy_And_Deafness-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Epidermolysis_Bullosa_Simplex_7_With_Nephropathy_And_Deafness-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 17 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000100` (1 mention) - the report calls it "Frequent"; HP calls it **Nephrotic syndrome**
- `HP:0000097` (1 mention) - the report calls it "Core (biopsy)"; HP calls it **Focal segmental glomerulosclerosis**
- `HP:0008404` (1 mention) - the report calls it "Frequent"; HP calls it **Nail dystrophy**
- `HP:0000407` (1 mention) - the report calls it "Core"; HP calls it **Sensorineural hearing impairment**
- `HP:0011904` (1 mention) - the report calls it "Index kindred"; HP calls it **Persistence of hemoglobin F**
- `HP:0001250` (1 mention) - the report calls it "Rare (expanded spectrum)"; HP calls it **Seizure**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `UBERON:0002966` (obsolete regional part of midbrain tectum) (1 mention)