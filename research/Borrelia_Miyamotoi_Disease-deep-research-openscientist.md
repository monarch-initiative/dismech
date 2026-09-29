---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-28T21:08:07.281337'
end_time: '2026-09-28T21:24:22.515250'
duration_seconds: 975.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Borrelia Miyamotoi Disease
  mondo_id: MONDO:0958150
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
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 22
  relevance_assessed: 27
  on_topic: 26
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 31
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 1
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - Near-universal
    ontology_label: Fever
  - term_id: HP:0025143
    reported_labels:
    - Common
    ontology_label: Chills
  - term_id: HP:0002315
    reported_labels:
    - Common
    ontology_label: Headache
  - term_id: HP:0003326
    reported_labels:
    - Common
    ontology_label: Myalgia
  - term_id: HP:0002829
    reported_labels:
    - Common
    ontology_label: Arthralgia
  - term_id: HP:0001873
    reported_labels:
    - Common
    ontology_label: Thrombocytopenia
  - term_id: HP:0001875
    reported_labels:
    - Common
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0002910
    reported_labels:
    - Common
    ontology_label: Elevated circulating hepatic transaminase concentration
  - term_id: HP:0012378
    reported_labels:
    - Common
    ontology_label: Fatigue
  - term_id: HP:0025142
    reported_labels:
    - recurrent fever
    ontology_label: Constitutional symptom
  - term_id: UBERON:0000178
    reported_labels:
    - Blood/circulatory system
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
  path: Borrelia_Miyamotoi_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Borrelia_Miyamotoi_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Borrelia Miyamotoi Disease
- **MONDO ID:** MONDO:0958150 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Borrelia Miyamotoi Disease** covering all of the
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

# Borrelia Miyamotoi Disease (BMD): Comprehensive Disease Characterization Report

**Target disease:** Borrelia Miyamotoi Disease (Hard-tick relapsing fever)
**MONDO ID:** MONDO:0958150 | **Category:** Infectious Disease (tick-borne, zoonotic bacterial)
**Report basis:** 5 investigative iterations, 9 confirmed findings, 35 papers reviewed. Evidence types: human clinical, model organism, in-vitro/genomic. Date: 2026-09-29.

---

## Summary

**Borrelia miyamotoi disease (BMD)** is an emerging, hard-tick–transmitted **relapsing fever** caused by the spirochete *Borrelia miyamotoi*. Unlike the classical soft-tick relapsing fever borreliae, *B. miyamotoi* is transmitted by hard-bodied *Ixodes* ticks — the same ticks that transmit Lyme disease (*B. burgdorferi*), human granulocytic anaplasmosis (*Anaplasma phagocytophilum*), and babesiosis (*Babesia microti*). The organism was discovered in *Ixodes persulcatus* in 1994, and the first human disease was described in Russia in 2011. It now has a documented northern-hemisphere distribution spanning Asia, Europe, and North America.

Clinically, BMD is an **acute, non-specific febrile illness**: high fever, chills, marked headache, and myalgia/arthralgia, frequently accompanied by the laboratory triad of **thrombocytopenia, neutropenia, and elevated transaminases**. A minority of untreated patients (~10%) manifest the relapsing (recurrent) fever course that gives the relapsing-fever group its name. Severe disease — chiefly **meningoencephalitis/meningitis** — occurs almost exclusively in **immunocompromised patients**, particularly those on B-cell–depleting therapy (e.g., rituximab). The pathophysiology rests on a **two-tier immune-evasion strategy**: (1) innate **complement resistance** mediated by the Factor H–binding outer-surface protein **CbiA**, which sustains high-grade spirochetemia, and (2) **Vmp antigenic variation** by long-segment plasmid gene conversion, which evades adaptive antibody responses and drives relapses. Bacterial clearance ultimately depends on specific antibodies, explaining why antibody-deficient hosts develop severe, persistent, or CNS disease.

Diagnosis relies on **acute-phase whole-blood PCR** (targets: 16S rRNA, *fla*/flagellin, *glpQ*) during spirochetemia, complemented by **GlpQ serology** — GlpQ (glycerophosphodiester phosphodiesterase) being an antigen absent from Lyme-group *Borrelia*, which allows serological discrimination. Because acute seropositivity is low (~16%) while convalescent seroconversion is high (~78%), PCR is the key acute test. Treatment with **doxycycline** (oral, first-line) is highly effective with excellent prognosis and no chronic sequelae; **ceftriaxone** is used for CNS disease. There is **no genetic etiology, no heritability, and no vaccine**; prevention is entirely tick-bite avoidance and prompt tick removal.

---

## Key Findings

### F001 — BMD is caused by a hard-tick–transmitted relapsing fever spirochete

*Borrelia miyamotoi* is phylogenetically a member of the **relapsing fever group** of spirochetes, distinct from the Lyme borreliosis group (*B. burgdorferi* sensu lato). It was discovered in *Ixodes persulcatus* in 1994, and human *B. miyamotoi* disease was first described in Russia in 2011. Its defining epidemiological anomaly is transmission by **hard-bodied *Ixodes* ticks** (*I. persulcatus*, *I. scapularis*, *I. pacificus*, *I. ricinus*) rather than the soft (argasid) ticks that classically transmit relapsing fever. Small rodents — for example *Peromyscus leucopus* (the white-footed mouse) — serve as reservoir hosts. Transmission occurs both **transovarially (vertically, dam to egg)** and **horizontally (via blood feeding)**, and the pathogen is passed **transtadially** across larval, nymphal, and adult life stages.

> "*Borrelia miyamotoi is an emerging tick-borne pathogen phylogenetically belonging to spirochaetes causing relapsing fever. It is primarily transmitted by ticks from the Ixodes ricinus complex, similarly to borreliae causing Lyme borreliosis. Small rodents can serve as reservoir hosts.*" — [PMID: 34412488](https://pubmed.ncbi.nlm.nih.gov/34412488/)

> "*B. miyamotoi has a wide distribution since its discovery in Ixodes persulcatus in 1994. The human B. miyamotoi disease was first described in Russia in 2011.*" — [PMID: 33582142](https://pubmed.ncbi.nlm.nih.gov/33582142/)

> "*The pathogen is acquired either transovarially (vertically) or horizontally through blood-feeding and passed transtadially across life stages.*" — [PMID: 35858517](https://pubmed.ncbi.nlm.nih.gov/35858517/)

**Ontology anchors:** NCBI Taxon *Borrelia miyamotoi* (txid47466); vector *Ixodes scapularis* (txid6945); reservoir *Peromyscus leucopus* (txid10041); disease MONDO:0958150.

### F002 — BMD presents as an acute febrile illness with relapsing fever and characteristic lab abnormalities

The largest US case series (Molloy et al. 2015; 97 PCR-confirmed cases) established the core clinical picture. Reviewed patients presented with **high fever, chills, marked headache, and myalgia or arthralgia**; **24% were hospitalized**; and **elevated liver enzymes, neutropenia, and thrombocytopenia** were common laboratory findings. Symptoms resolved with doxycycline and no chronic sequelae were observed. In a Russian inpatient cohort of 79 patients, a **recurrent (relapsing) fever course occurred in ~10% (8/79)**, with affected patients experiencing 2–3 discrete febrile episodes prior to antibiotic treatment.

> "*Most of the 51 case patients on whom clinical histories were reviewed presented with high fever, chills, marked headache, and myalgia or arthralgia. Twenty-four percent were hospitalized. Elevated liver enzyme levels, neutropenia, and thrombocytopenia were common.*" — [PMID: 26053877](https://pubmed.ncbi.nlm.nih.gov/26053877/)

> "*The recurrent course of the disease was observed in 8 (10%) of the 79 patients. The relapsing fever curve was noted in 6 of the 8 patients; 4 patients had 2 episodes of fever and 2 patients had 3 episodes.*" — [PMID: 26821411](https://pubmed.ncbi.nlm.nih.gov/26821411/)

**Suggested HPO terms:** Fever HP:0001945; Chills HP:0025143; Headache HP:0002315; Myalgia HP:0003326; Arthralgia HP:0002829; Thrombocytopenia HP:0001873; Neutropenia HP:0001875; Elevated hepatic transaminase HP:0002910.

### F003 — Antigenic variation via Vmp long-segment plasmid conversion drives relapsing fever

*B. miyamotoi* carries clusters of gene cassettes encoding **variable major proteins (Vmps)** on multiple linear plasmids and undergoes antigenic variation in mammalian hosts by switching the expressed *vmp* cassette. Takeuchi et al. (2025) demonstrated that the switch occurs by replacing the expression cassette and downstream silent cassettes with a **long segment (up to 16 kb+)** copied from an archival plasmid — a mechanism termed **long-segment conversion**. Critically, **segment conversion was detected by day 5 post-infection, earlier than antibody production, and occurred even in SCID (severe combined immunodeficient) mice**, whereas **bacterial elimination depended on specific antibodies**. This decoupling explains both the relapsing dynamics (new antigenic variants escape existing antibodies) and the vulnerability of antibody-deficient hosts to severe disease.

> "*Like relapsing fever Borrelia, B. miyamotoi carries clusters of gene cassettes encoding variable major proteins (Vmps) on multiple linear plasmids and shows antigenic variation in mammalian hosts by switching the expression vmp gene cassette.*" — [PMID: 41026790](https://pubmed.ncbi.nlm.nih.gov/41026790/)

> "*while bacterial elimination depended on the presence of specific antibodies, the segment conversion was detected at five days post-infection, earlier than antibody production in mice, and even in severe combined immunodeficient mice.*" — [PMID: 41026790](https://pubmed.ncbi.nlm.nih.gov/41026790/)

**Suggested GO terms:** antigenic variation GO:0020033; evasion of host immune response GO:0042783 / GO:0052572.

### F004 — Epidemiology: low tick infection prevalence but measurable human seroprevalence across the northern hemisphere

A systematic review and meta-analysis (Hoornstra et al. 2022) synthesizing 157 studies (165,637 ticks; 45,608 individuals; 504 well-described human cases) found *B. miyamotoi* prevalence in **questing ticks highest in *Ixodes persulcatus* (2.8%, 95% CI 2.4–3.1)** and **lowest in *I. pacificus* (0.7%, 95% CI 0.6–0.8)**. **Overall human seroprevalence was 4.4% (95% CI 2.8–6.3)**, and slightly higher (~4.6%) in high-risk groups. US surveillance shows *B. miyamotoi* co-occurs with *B. burgdorferi* across the Northeast, Upper Midwest, Ohio Valley, and southern Appalachia. Genotypic analyses reveal **three distinct geographic populations** (North America, Asia, Europe).

> "*In ticks, the highest prevalence of B miyamotoi was observed in Ixodes persulcatus (2·8%, 95% CI 2·4-3·1) and the lowest in Ixodes pacificus (0·7%, 0·6-0·8). The overall seroprevalence in humans was 4·4% (2·8-6·3).*" — [PMID: 36113496](https://pubmed.ncbi.nlm.nih.gov/36113496/)

> "*Borrelia miyamotoi belongs to the relapsing fever group of spirochetes and forms distinct populations in North America, Asia, and Europe.*" — [PMID: 31906865](https://pubmed.ncbi.nlm.nih.gov/31906865/)

| Tick species | *B. miyamotoi* prevalence (questing ticks) | Region |
|---|---|---|
| *Ixodes persulcatus* | 2.8% (2.4–3.1) | Asia / eastern Europe |
| *Ixodes ricinus* | intermediate | Europe |
| *Ixodes scapularis* | intermediate | Eastern/Midwest US |
| *Ixodes pacificus* | 0.7% (0.6–0.8) | Western US |

### F005 — Diagnosis relies on blood PCR and GlpQ serology; CNS disease occurs in immunocompromised patients

Diagnosis uses **whole-blood real-time PCR** (targets: 16S rRNA, *fla*/flagellin, *glpQ*) during acute spirochetemia, and **serology against recombinant glycerophosphodiester phosphodiesterase (GlpQ)** — an antigen absent from Lyme-group *Borrelia*, enabling serological discrimination from Lyme disease. In the Molloy 2015 series, only **16% of patients were seropositive at presentation, but 78% seroconverted in convalescence**, underscoring that **acute-phase PCR is the key diagnostic**. A multiplexed **protein array** (Hoornstra 2022) incorporating GlpQ, multiple Vmps, and flagellin improved serodiagnostic accuracy. **Meningoencephalitis/meningitis** is reported almost exclusively in immunocompromised patients (e.g., those on B-cell–depleting rituximab therapy) and is diagnosed via CSF PCR, sequencing, or Gram stain.

> "*At presentation, 16% of patients with BMD were seropositive for IgG and/or IgM antibody to B. miyamotoi rGlpQ. Most (78%) had seropositive convalescent specimens.*" — [PMID: 26053877](https://pubmed.ncbi.nlm.nih.gov/26053877/)

> "*Borrelia miyamotoi is an emerging tickborne pathogen that has been associated with central nervous system infections in immunocompromised patients, albeit infrequently.*" — [PMID: 38916722](https://pubmed.ncbi.nlm.nih.gov/38916722/)

> "*The array included six B. miyamotoi antigens: glycerophosphodiester phosphodiesterase (GlpQ), multiple variable major proteins (Vmps), and flagellin.*" — [PMID: 36314925](https://pubmed.ncbi.nlm.nih.gov/36314925/)

**Suggested diagnostic anchors:** *B. miyamotoi* DNA by PCR (blood/CSF); anti-GlpQ IgM/IgG serology.

### F006 — BMD is effectively treated with doxycycline; CNS disease requires ceftriaxone

In the Molloy 2015 US case series, symptoms **resolved after doxycycline treatment with no chronic sequelae**. **Oral doxycycline is first-line** for uncomplicated disease, while **parenteral ceftriaxone** is used for meningoencephalitis/CNS disease. Early antibiotic treatment appears to prevent relapse and seroconversion: in the Boyer 2020 Alsace study, three patients with isolated IgM were treated with doxycycline, which could have prevented seroconversion. Relapses occurred **only in untreated patients** — in the Russian cohort, all 8 relapsing patients relapsed *before* antibiotic treatment.

> "*Symptoms resolved after treatment with doxycycline, and no chronic sequelae or symptoms were observed.*" — [PMID: 26053877](https://pubmed.ncbi.nlm.nih.gov/26053877/)

> "*Relapses occurred in all the 8 patients before antibiotic treatment.*" — [PMID: 26821411](https://pubmed.ncbi.nlm.nih.gov/26821411/)

**Suggested NCIT terms:** Doxycycline C560; Ceftriaxone C596; Antibiotic Therapy C15844. **CHEBI:** doxycycline CHEBI:50845; ceftriaxone CHEBI:29007.

### F007 — BMD affects all ages including children and co-occurs geographically with other Ixodes-borne pathogens

BMD occurs across the full age spectrum, including young children. Krause et al. (2016) reported hard-tick relapsing fever in a **5-year-old Massachusetts child**, PCR-confirmed from an *I. scapularis* tick removed from the scalp, with seroconversion, fatigue, and recurrent fever. Doxycycline is now acceptable for tick-borne illness in children of any age. Although *B. miyamotoi* co-occurs geographically with *B. burgdorferi* across the eastern US, an analysis of 13,437 CDC-tested nymphs (2013–2024) found that **B. burgdorferi–B. miyamotoi coinfection did NOT form more often than expected by chance** — unlike other *Ixodes* coinfection pairs — and was the least prevalent of the four studied coinfections. This suggests the two spirochetes' co-occurrence in humans is largely coincidental (shared vector) rather than biologically facilitated.

> "*A 5-year-old Massachusetts resident developed hard tick-borne relapsing fever caused by Borrelia miyamotoi. A partially engorged Ixodes scapularis tick was removed from her scalp and identified as infected with B. miyamotoi using polymerase chain reaction.*" — [PMID: 27626914](https://pubmed.ncbi.nlm.nih.gov/27626914/)

> "*Except for Bbss-Bmiya, resampling simulations for all coinfections revealed coinfections form more often than expected by chance.*" — [PMID: 41637958](https://pubmed.ncbi.nlm.nih.gov/41637958/)

### F008 — Innate immune evasion via complement resistance mediated by the Factor H–binding protein CbiA

*B. miyamotoi* is **strongly resistant to complement-mediated bacteriolysis** by human serum. It shows **reduced surface deposition of C3, C5, C7, C8, C9 and the membrane attack complex (MAC)**, acting principally at the central component **C3** to block C3-convertase formation (Teegler/Wagemakers 2014). Röttgerding et al. (2017) identified **CbiA (complement binding and inhibitory protein A)**, a novel outer-surface Factor H–binding protein that interacts with **FH, C3, C3b, C4b, C5, and C9**. Factor H bound to CbiA retains cofactor activity for Factor I–mediated C3b inactivation, and CbiA directly inhibits both the classical pathway and terminal complement complex assembly. Ectopic expression of CbiA rendered serum-sensitive *B. garinii* serum-resistant, and loss of *cbiA* during in vitro passage increased serum susceptibility — establishing CbiA as a functional determinant. By contrast, the avian relapsing-fever spirochete *B. anserina* is serum-sensitive, consistent with its lack of human pathogenicity.

> "*we found that B. miyamotoi showed reduced deposition of components C3, C5, C7, C8, C9 as well as the membrane attack complex (MAC) on the borrelial surface.*" — [PMID: 25104575](https://pubmed.ncbi.nlm.nih.gov/25104575/)

> "*we identified a gene encoding for a putative Factor H-binding protein, termed CbiA (complement binding and inhibitory protein A). Functional analyses revealed that CbiA interacted with complement regulator Factor H (FH), C3, C3b, C4b, C5, and C9.*" — [PMID: 28331202](https://pubmed.ncbi.nlm.nih.gov/28331202/)

> "*we describe that B. miyamotoi is resistant to human complement, which might play an important role in pathogenesis.*" — [PMID: 25189195](https://pubmed.ncbi.nlm.nih.gov/25189195/)

**Suggested GO terms:** complement activation GO:0006956; negative regulation of complement activation GO:0045916; regulation of complement-dependent cytotoxicity GO:1903659.

### F009 — Seroprevalence is low in blood donors but markedly elevated in tick-exposed and occupational risk groups

Serosurveys quantify a clear **exposure gradient by risk group**. In Denmark (n=1180, 2002–2021), seroprevalence was **8.3% in tick-exposed individuals vs 1.5% in blood donors and 3.3% in immunocompromised individuals** (p<0.0001; overall 3.1%). In the Netherlands, seroprevalence was **2.0% in blood donors, 10% in forestry workers, and 14.6% in patients with suspected human granulocytic anaplasmosis**. In California blood donors (n=1700, western US, *I. pacificus* zone), only **0.12% were *B. miyamotoi*-seropositive vs 0.47% for *B. burgdorferi***, reflecting lower western-US vector infection rates. These figures align with the global meta-analytic seroprevalence of 4.4% (higher, ~4.6%, in high-risk groups).

> "*Borrelia miyamotoi seroprevalence (being either IgM or IgG positive) among tick-exposed individuals (8.3 %, 95%CI 5.1-13.3) was significantly higher compared to healthy blood donors (1.5 %, 95 % CI 0.8-2.8) and immunocompromised individuals (3.3 %, 95 %CI 1.9-5.5), p < 0.0001.*" — [PMID: 41086691](https://pubmed.ncbi.nlm.nih.gov/41086691/)

> "*The prevalence of anti-B. miyamotoi antibodies among forestry workers was 10% (5.3-16.8%) and in patients with serologically unconfirmed but suspected human granulocytic anaplasmosis was 14.6% (9.0-21.8%); these were significantly higher compared with the seroprevalence in blood donors.*" — [PMID: 25356364](https://pubmed.ncbi.nlm.nih.gov/25356364/)

> "*eight tested positive for antibodies to B. burgdorferi (0.47%, Exact 95% CI: 0.20, 0.93) and two tested positive for antibodies to B. miyamotoi (0.12%.*" — [PMID: 33370341](https://pubmed.ncbi.nlm.nih.gov/33370341/)

| Population | Seroprevalence | Country | PMID |
|---|---|---|---|
| Blood donors | 1.5% | Denmark | 41086691 |
| Immunocompromised | 3.3% | Denmark | 41086691 |
| Tick-exposed | 8.3% | Denmark | 41086691 |
| Blood donors | 2.0% | Netherlands | 25356364 |
| Forestry workers | 10% | Netherlands | 25356364 |
| Suspected HGA patients | 14.6% | Netherlands | 25356364 |
| Blood donors (western US) | 0.12% | California, USA | 33370341 |

---

## Section-by-Section Disease Characterization

### 1. Disease Information
**Overview:** BMD ("hard-tick relapsing fever") is an emerging zoonotic bacterial infection caused by *Borrelia miyamotoi*, a relapsing-fever–group spirochete transmitted by *Ixodes* (hard) ticks. It presents as an acute febrile illness that can relapse and, rarely, cause meningoencephalitis in immunocompromised hosts.
**Identifiers:** MONDO:0958150; MeSH "Borrelia miyamotoi" and "Relapsing Fever"; ICD-11 category 1C1G (relapsing fevers) / ICD-10 A68.- (relapsing fevers). No OMIM entry (non-genetic). Not in Orphanet as a rare Mendelian disease.
**Synonyms:** *B. miyamotoi* disease; hard-tick relapsing fever (HTRF); *Borrelia miyamotoi* infection; ixodid tick-borne borreliosis caused by *B. miyamotoi* (BM-ITBB, Russian literature).
**Data source type:** Aggregated disease-level resources (case series, serosurveys, meta-analyses) plus individual case reports — **not** EHR-derived at population scale.

### 2. Etiology
**Causal factor:** Infectious — the bacterium *Borrelia miyamotoi* (F001). This is the sole and sufficient cause; the disease is not genetic and has no heritable component.
**Environmental/behavioral risk factors:** Tick exposure is the dominant risk factor — occupational (forestry work), recreational (hiking in endemic areas), and residential proximity to *Ixodes* habitat (F009). Seasonality follows tick questing activity (late spring–summer). Geographic residence in endemic zones (northeastern/upper-midwestern US, Europe, Russia, Japan, China) increases risk.
**Host susceptibility factor:** Immunocompromise — especially **B-cell depletion (rituximab)** — is the key modifier of *severity*, converting a self-limited febrile illness into meningoencephalitis (F003, F005).
**Genetic risk/protective factors:** None identified — there is no human genetic susceptibility locus, GWAS signal, or protective allele known for BMD. **Not applicable.**
**Gene–environment interactions:** Not applicable in the human host (no host genetic contribution). At the pathogen level, the mammalian-host "environment" drives *bacterial* genetic switching (Vmp conversion, F003).

### 3. Phenotypes
| Phenotype | Type | Frequency | HPO term |
|---|---|---|---|
| Fever (often high) | Symptom | Near-universal | HP:0001945 |
| Chills | Symptom | Common | HP:0025143 |
| Headache (marked) | Symptom | Common | HP:0002315 |
| Myalgia | Symptom | Common | HP:0003326 |
| Arthralgia | Symptom | Common | HP:0002829 |
| Fatigue | Symptom | Common | HP:0012378 |
| Relapsing/recurrent fever | Clinical course | ~10% (untreated) | HP:0025142 (recurrent fever) |
| Thrombocytopenia | Lab abnormality | Common | HP:0001873 |
| Neutropenia | Lab abnormality | Common | HP:0001875 |
| Elevated transaminases | Lab abnormality | Common | HP:0002910 |
| Meningoencephalitis / meningitis | Clinical sign | Rare (immunocompromised) | HP:0001287 / HP:0002383 |

**Onset:** Adult-predominant but all ages including children (age 5 documented, F007). **Severity:** Mild-to-moderate in immunocompetent hosts; severe/CNS in immunocompromised. **Progression:** Self-limited or episodic/relapsing; resolves fully with treatment. **QoL impact:** Acute illness causes transient functional impairment; no chronic sequelae reported in immunocompetent patients (F006).

### 4. Genetic/Molecular Information
**Not applicable to the human host.** BMD has no causal human genes, pathogenic germline/somatic variants, modifier genes, epigenetic changes, or chromosomal abnormalities — it is an infectious disease with no Mendelian or complex-trait genetic architecture. The relevant molecular biology is **microbial**: *B. miyamotoi* has a segmented genome with a main linear chromosome and multiple linear/circular plasmids carrying *vmp* cassettes (F003); the reference isolate Izh-4 genome is characterized ([PMID: 31906865](https://pubmed.ncbi.nlm.nih.gov/31906865/)). Key pathogen genes/proteins: **vmp** (variable major proteins, antigenic variation), **cbiA** (Factor H–binding complement inhibitor), **glpQ** (glycerophosphodiester phosphodiesterase — metabolic enzyme and diagnostic antigen), **flaB** (flagellin), **p66** (porin).

### 5. Environmental Information
**Infectious agent:** *Borrelia miyamotoi* (NCBI Taxon 47466), Spirochaetales: Spirochaetaceae, relapsing-fever group (F001). **Vectors:** *Ixodes persulcatus, I. scapularis, I. pacificus, I. ricinus* (F001, F004). **Reservoirs:** small rodents including *Peromyscus leucopus* (F001). **Environmental drivers:** tick habitat (deciduous/mixed woodland, leaf litter), climate influencing tick density and questing, and human land use. **Lifestyle/occupational factors:** outdoor occupation (forestry) and recreation drive exposure (F009). No toxin, radiation, or pollution etiology.

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1. Infected Ixodes tick bites human and inoculates B. miyamotoi during blood feeding
      │  (transtadially/transovarially maintained in tick — F001)
      ▼
2. Spirochetes enter dermis and bloodstream → establish spirochetemia
      ▼
3. CbiA (Factor H-binding protein) recruits host Factor H to the spirochete surface
      │  → blocks C3-convertase formation, reduces C3/C5/MAC deposition (F008)
      ▼
4. Complement resistance → spirochetes survive innate serum killing → HIGH-GRADE SPIROCHETEMIA
      ▼
5. High bacterial load → PAMP-driven innate inflammation (fever, chills, myalgia;
      cytopenias: thrombocytopenia, neutropenia; hepatic transaminase elevation) (F002)
      ▼
6. Host mounts specific antibody response against expressed Vmp
      │
      ├─► 7a. Vmp long-segment plasmid conversion (from day 5, antibody-independent,
      │        occurs even in SCID mice) switches surface antigen (F003)
      │            ▼
      │        8a. New antigenic variant escapes existing antibodies → RELAPSE
      │            (recurrent febrile episodes, ~10% untreated — F002/F003)
      │
      └─► 7b. In immunocompetent host: successive antibody waves eventually
               clear all variants → RESOLUTION, no chronic sequelae (F003, F006)

   BRANCH (immunocompromised / B-cell depleted, e.g., rituximab):
      antibody clearance fails → persistent spirochetemia → CNS invasion →
      MENINGOENCEPHALITIS / MENINGITIS (F003, F005)
```

**Upstream vs downstream:** The *initiating* lesions are tick inoculation and **CbiA-mediated complement evasion** (upstream, innate). **Vmp antigenic variation** is the mid-stream driver of relapse. Antibody-dependent clearance is the terminal determinant of outcome — its failure (downstream, in immunocompromised hosts) produces severe/CNS disease. **Cell types/processes involved:** endothelial and blood compartment (spirochetemia); hepatocytes (transaminase elevation); bone marrow/blood cells (cytopenias); complement system components (C3, C5b–C9/MAC); B lymphocytes (CL:0000236) as the critical clearance effector. **Metabolic note:** GlpQ (glycerophosphodiester phosphodiesterase) supports phospholipid/glycerol metabolism and doubles as the key serodiagnostic antigen (F005).

### 7. Anatomical Structures Affected
- **Blood/circulatory system** (UBERON:0000178) — primary compartment of spirochetemia.
- **Liver** (UBERON:0002107) — transaminase elevation indicates hepatocyte involvement.
- **Bone marrow / hematopoietic system** (UBERON:0002371) — cytopenias (thrombocytopenia, neutropenia).
- **Central nervous system / meninges** (UBERON:0001016 / UBERON:0002360) — meningoencephalitis in immunocompromised hosts.
- **Musculoskeletal system** — myalgia/arthralgia (symptomatic).
- **Cell types:** B lymphocytes (CL:0000236, protective clearance); neutrophils (CL:0000775); platelets (CL:0000233).
- **Subcellular/molecular:** bacterial outer membrane/surface (CbiA, Vmp); host complement (extracellular).
- **Lateralization:** systemic/bilateral — not a focal or lateralized disease.

### 8. Temporal Development
**Onset:** Acute, days after an infected tick bite; all ages (pediatric to geriatric). **Incubation:** on the order of days to ~2 weeks. **Course:** self-limited in most; **relapsing/episodic** in ~10% of untreated patients (2–3 febrile episodes; F002). **Duration:** short (days–weeks) with treatment; no chronic phase in immunocompetent hosts (F006). **Critical intervention window:** early doxycycline aborts relapse and may prevent seroconversion (F006). **Severe branch:** in immunocompromised patients, disease may progress to CNS involvement if untreated (F005).

### 9. Inheritance and Population
**Inheritance:** None — non-genetic infectious disease (no AD/AR/X-linked/mitochondrial pattern; no penetrance/expressivity/anticipation/founder effects). **Epidemiology:** Questing-tick prevalence 0.7–2.8% by species; human seroprevalence ~4.4% overall (meta-analysis), with strong risk-group gradients (blood donors ~1.5–2%; forestry ~10%; tick-exposed ~8.3%; western US ~0.12%) (F004, F009). **Geographic distribution:** northern hemisphere — three distinct populations in North America, Europe, and Asia (F004). **Age/sex:** all ages affected; no strong sex predilection established. Case-level data derive from aggregated series and serosurveys.

### 10. Diagnostics
- **Acute-phase whole-blood real-time PCR** (16S rRNA, *fla*/flagellin, *glpQ*) — key test during spirochetemia (F005).
- **GlpQ serology** (IgM/IgG) — GlpQ absent from Lyme *Borrelia*, enabling discrimination; low acute (16%) but high convalescent (78%) positivity → paired sera valuable (F005).
- **Multiplex protein array** (GlpQ + Vmps + flagellin) — improved serodiagnostic accuracy (F005).
- **CSF PCR/sequencing/Gram stain** — for suspected CNS disease in immunocompromised patients (F005).
- **Supporting labs:** CBC (thrombocytopenia, neutropenia), liver panel (elevated transaminases) (F002).
- **Blood smear:** spirochetes may be visualized during high spirochetemia (relapsing-fever feature).
- **Differential diagnosis:** Lyme disease (usually with erythema migrans; GlpQ-negative), anaplasmosis, babesiosis, tick-borne encephalitis, and other febrile zoonoses. A Russian decision-tree algorithm distinguished BM-ITBB from Lyme, TBE, and HFRS with ~95% accuracy using routine clinical/lab variables ([PMID: 24432595](https://pubmed.ncbi.nlm.nih.gov/24432595/)).
- **Genetic/omics testing:** Not applicable for host diagnosis.

### 11. Outcome / Prognosis
**Excellent prognosis** with prompt antibiotic therapy: symptoms resolve and **no chronic sequelae** are observed in immunocompetent patients (F006). Mortality is very low; deaths are exceptional and generally linked to severe CNS disease in profoundly immunocompromised hosts. **Complications:** relapse (untreated), meningoencephalitis (immunocompromised). **Prognostic factors:** immune status (B-cell competence) is the dominant determinant of severity; timeliness of antibiotic treatment governs relapse prevention (F003, F005, F006). No validated prognostic biomarkers beyond spirochetemia and immune status.

### 12. Treatment
- **Doxycycline** (oral, first-line; NCIT:C560; CHEBI:50845) for uncomplicated disease — highly effective, no chronic sequelae (F006). Acceptable in children of any age (F007).
- **Ceftriaxone** (parenteral; NCIT:C596; CHEBI:29007) for meningoencephalitis/CNS disease (F005/F006).
- **Beta-lactams** (e.g., penicillin) and other tetracyclines are alternatives per relapsing-fever practice.
- **Jarisch–Herxheimer reaction** is a recognized consideration when initiating antibiotics against spirochetes (monitor early after first dose).
- **No advanced therapeutics** (gene/cell/RNA/immunotherapy), no pharmacogenomic guidance, and **no vaccine**. Early treatment prevents relapse and may prevent seroconversion (F006).

### 13. Prevention
- **Primary prevention:** tick-bite avoidance — protective clothing, EPA-registered repellents (DEET, picaridin), permethrin-treated clothing, avoiding tick habitat, and prompt tick removal (transmission risk rises with attachment duration). Occupational protections for forestry/outdoor workers (F009).
- **Secondary prevention:** early recognition and PCR/serology testing of febrile patients after tick exposure; prompt doxycycline (F005/F006).
- **Tertiary prevention:** early antibiotics to prevent relapse and CNS progression; heightened vigilance in immunocompromised patients (F003/F005).
- **Immunization:** none available (no vaccine).
- **Public health:** tick surveillance (e.g., CDC ArboNET Tick Module), clinician awareness, vector/habitat management.
- **Genetic counseling / screening:** Not applicable (non-heritable).

### 14. Other Species / Natural Disease
- **Reservoir hosts:** small rodents, notably *Peromyscus leucopus* (NCBI Taxon 10041) and other *Peromyscus*/*Myodes* species (F001).
- **Vectors (obligate for maintenance):** *Ixodes* spp. (*I. persulcatus*, *I. scapularis* txid6945, *I. pacificus*, *I. ricinus* txid34613).
- **Zoonotic potential:** BMD is a zoonosis — humans are incidental hosts; the enzootic cycle is tick–rodent (F001).
- **Comparative note:** The avian relapsing-fever spirochete *B. anserina* is **serum-sensitive** and non-pathogenic to humans, contrasting with *B. miyamotoi*'s complement resistance and providing a comparative anchor for the role of CbiA (F008).
- **Orthologous host genes:** Not applicable (no host disease gene).

### 15. Model Organisms
- **Mouse models:** *B. miyamotoi* infects laboratory mice; **SCID (severe combined immunodeficient) mice** were pivotal in demonstrating that Vmp segment conversion is antibody-independent while clearance is antibody-dependent (F003). A dedicated laboratory mouse model to study BMD has been reported ([PMID: 42367759](https://pubmed.ncbi.nlm.nih.gov/42367759/)).
- **Model utility:** immunocompetent vs immunodeficient mice dissect innate (complement/CbiA) vs adaptive (antibody/Vmp) contributions — recapitulating the human immunocompetent-vs-immunocompromised severity dichotomy.
- **In vitro:** *B. miyamotoi* is cultivable in modified Kelly-Pettenkofer medium, enabling complement-resistance and CbiA functional assays ([PMID: 25189195](https://pubmed.ncbi.nlm.nih.gov/25189195/), [PMID: 28331202](https://pubmed.ncbi.nlm.nih.gov/28331202/)).
- **Heterologous expression:** ectopic *cbiA* in serum-sensitive *B. garinii* confers serum resistance — a gain-of-function validation (F008).
- **Limitations:** murine models may not fully capture human CNS disease; tick-transmission dynamics require the *Ixodes* vector.

---

## Mechanistic Model / Interpretation

The unifying model of BMD is a **two-tier immune-evasion cascade** in which the outcome is set by the balance between bacterial evasion and host humoral immunity:

| Tier | Effector | Immune arm evaded | Consequence | Evidence |
|---|---|---|---|---|
| **Tier 1 (innate)** | **CbiA** binds Factor H; blocks C3-convertase, reduces MAC | Complement (innate) | Survives serum killing → high spirochetemia | F008 (PMID 25104575, 28331202, 25189195) |
| **Tier 2 (adaptive)** | **Vmp** long-segment plasmid conversion | Antibody (adaptive) | Antigenic escape → relapse | F003 (PMID 41026790) |
| **Resolution / severity switch** | Specific antibodies clear all variants | — | Cure (immunocompetent) *or* CNS disease (immunocompromised) | F003, F005, F006 |

This model explains the full clinical spectrum from a single axis — **humoral competence**. Immunocompetent hosts eventually generate antibody waves that outpace Vmp switching and clear infection (self-limited, curable, no sequelae). Immunocompromised/B-cell–depleted hosts cannot clear the antigenically shifting population, permitting persistence and CNS invasion. CbiA-mediated complement resistance is the permissive upstream event that allows spirochetemia to reach the levels needed for both symptomatic disease and antigenic-variation–driven relapse.

---

## Evidence Base

| PMID | Contribution | Finding |
|---|---|---|
| [34412488](https://pubmed.ncbi.nlm.nih.gov/34412488/) | Relapsing-fever phylogeny, *I. ricinus* complex transmission, rodent reservoirs | F001 |
| [33582142](https://pubmed.ncbi.nlm.nih.gov/33582142/) | 1994 discovery, 2011 first human disease | F001 |
| [35858517](https://pubmed.ncbi.nlm.nih.gov/35858517/) | Transovarial + horizontal + transtadial transmission | F001 |
| [26053877](https://pubmed.ncbi.nlm.nih.gov/26053877/) | US case series: symptoms, 24% hospitalized, lab triad, doxycycline cure, serology kinetics | F002, F005, F006 |
| [26821411](https://pubmed.ncbi.nlm.nih.gov/26821411/) | Russian cohort: ~10% relapse, pre-treatment relapses | F002, F006 |
| [41026790](https://pubmed.ncbi.nlm.nih.gov/41026790/) | Vmp long-segment conversion; antibody-independent switching, antibody-dependent clearance (SCID) | F003 |
| [36113496](https://pubmed.ncbi.nlm.nih.gov/36113496/) | Meta-analysis: tick prevalence by species, 4.4% human seroprevalence | F004 |
| [31906865](https://pubmed.ncbi.nlm.nih.gov/31906865/) | Reference genome; 3 geographic populations | F004 |
| [38916722](https://pubmed.ncbi.nlm.nih.gov/38916722/) | CNS infection in immunocompromised | F005 |
| [36314925](https://pubmed.ncbi.nlm.nih.gov/36314925/) | Protein array (GlpQ, Vmps, flagellin) | F005 |
| [27626914](https://pubmed.ncbi.nlm.nih.gov/27626914/) | Pediatric case (age 5) | F007 |
| [41637958](https://pubmed.ncbi.nlm.nih.gov/41637958/) | Bbss–Bmiya coinfection at chance frequency only | F007 |
| [25104575](https://pubmed.ncbi.nlm.nih.gov/25104575/) | Reduced C3/C5/MAC deposition (complement resistance) | F008 |
| [28331202](https://pubmed.ncbi.nlm.nih.gov/28331202/) | CbiA identification and function | F008 |
| [25189195](https://pubmed.ncbi.nlm.nih.gov/25189195/) | Human complement resistance; cultivability | F008 |
| [41086691](https://pubmed.ncbi.nlm.nih.gov/41086691/) | Denmark seroprevalence gradient | F009 |
| [25356364](https://pubmed.ncbi.nlm.nih.gov/25356364/) | Netherlands occupational seroprevalence | F009 |
| [33370341](https://pubmed.ncbi.nlm.nih.gov/33370341/) | Low western-US seroprevalence | F009 |
| [24432595](https://pubmed.ncbi.nlm.nih.gov/24432595/) | Differential-diagnosis decision tree (~95% accuracy) | Diagnostics |

**Supporting surveillance literature:** Pennsylvania statewide *I. scapularis* survey ([PMID: 38686844](https://pubmed.ncbi.nlm.nih.gov/38686844/)), ArboNET DIN trends ([PMID: 40907973](https://pubmed.ncbi.nlm.nih.gov/40907973/)), German tick-removal study (7.4% of Borrelia-positive ticks were *B. miyamotoi*; [PMID: 31987819](https://pubmed.ncbi.nlm.nih.gov/31987819/)), Slovakia ([PMID: 35094490](https://pubmed.ncbi.nlm.nih.gov/35094490/)), Kazakhstan ([PMID: 39332111](https://pubmed.ncbi.nlm.nih.gov/39332111/)), Belgium ([PMID: 39238018](https://pubmed.ncbi.nlm.nih.gov/39238018/)), and NY/Long Island clinical series ([PMID: 32473652](https://pubmed.ncbi.nlm.nih.gov/32473652/)).

---

## Limitations and Knowledge Gaps

1. **Non-genetic disease:** Sections 4 (Genetic/Molecular), 9 (Inheritance), and the genetic-testing portions of Section 10 are **not applicable** — BMD has no host genetic architecture. This is a definitive negative finding, not a data gap.
2. **True incidence unknown:** Seroprevalence quantifies exposure, not clinical incidence. Underdiagnosis is likely because BMD is non-specific and overlaps clinically/geographically with Lyme disease.
3. **Sex ratio and age distribution** of *clinical* cases are not well quantified across populations.
4. **Diagnostic sensitivity limits:** Acute serology is insensitive (16%); PCR requires active spirochetemia; standardized commercial assays remain limited.
5. **CNS disease is under-characterized** — reported almost exclusively in small case reports of immunocompromised patients; natural history and optimal CNS treatment duration are not established from trials.
6. **No randomized treatment trials:** Doxycycline efficacy rests on case series and relapsing-fever precedent, not RCTs; optimal regimen/duration is empirically derived.
7. **QoL and long-term outcomes** are inferred from "no chronic sequelae" observations rather than prospective cohorts.
8. **Vaccine and prophylaxis** research is essentially absent.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective incidence study** in high-endemicity regions using paired acute/convalescent PCR + GlpQ serology to convert seroprevalence into true clinical incidence and define age/sex distributions.
2. **Structural and functional dissection of CbiA** (AlphaFold model + Factor H co-crystal) to map the FH-binding interface and evaluate CbiA as a vaccine/therapeutic target; test *cbiA* knockout attenuation in the SCID vs immunocompetent mouse model.
3. **Longitudinal Vmp repertoire sequencing** during human/murine infection to quantify switching rate, cassette usage hierarchy, and correlation with relapse timing.
4. **Randomized/pragmatic treatment comparison** (doxycycline duration; ceftriaxone for CNS disease) to establish evidence-based regimens, including Jarisch–Herxheimer incidence.
5. **Improved point-of-care diagnostics:** multiplex PCR panels and next-generation serologic arrays (GlpQ + Vmp + flagellin) validated against paired sera; evaluate metagenomic sequencing for CNS disease.
6. **Immunocompromised-host registry** (especially rituximab-treated patients) to characterize CNS disease natural history, treatment response, and outcomes.
7. **Vector/reservoir surveillance integration** (ArboNET Tick Module expansion) to map acarological risk and guide clinician awareness where *B. miyamotoi* and *B. burgdorferi* co-occur.
8. **Vaccine feasibility assessment** targeting conserved surface antigens (CbiA, GlpQ), leveraging the observation that antibodies mediate clearance.

---

*Report compiled from 9 confirmed findings and 35 reviewed papers across 5 investigative iterations. Evidence types: human clinical case series/cohorts, serosurveys, meta-analysis, in vitro microbiology, and mouse (including SCID) model studies.*


## Artifacts

- [OpenScientist final report](Borrelia_Miyamotoi_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Borrelia_Miyamotoi_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 22 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 27 |
| On topic | 26 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 13 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (2 mentions) - the report calls it "Near-universal"; HP calls it **Fever**
- `HP:0025143` (2 mentions) - the report calls it "Common"; HP calls it **Chills**
- `HP:0002315` (2 mentions) - the report calls it "Common"; HP calls it **Headache**
- `HP:0003326` (2 mentions) - the report calls it "Common"; HP calls it **Myalgia**
- `HP:0002829` (2 mentions) - the report calls it "Common"; HP calls it **Arthralgia**
- `HP:0001873` (2 mentions) - the report calls it "Common"; HP calls it **Thrombocytopenia**
- `HP:0001875` (2 mentions) - the report calls it "Common"; HP calls it **Decreased total neutrophil count**
- `HP:0002910` (2 mentions) - the report calls it "Common"; HP calls it **Elevated circulating hepatic transaminase concentration**
- `HP:0012378` (1 mention) - the report calls it "Common"; HP calls it **Fatigue**
- `HP:0025142` (1 mention) - the report calls it "recurrent fever"; HP calls it **Constitutional symptom**
- `UBERON:0000178` (1 mention) - the report calls it "Blood/circulatory system"; UBERON calls it **blood**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002371` (1 mention) - the report calls it "Bone marrow / hematopoietic system"; UBERON calls it **bone marrow**