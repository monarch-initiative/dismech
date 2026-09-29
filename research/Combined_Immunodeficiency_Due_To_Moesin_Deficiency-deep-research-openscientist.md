---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T12:53:14.114073'
end_time: '2026-09-12T13:27:18.681804'
duration_seconds: 2044.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Immunodeficiency Due To Moesin Deficiency
  mondo_id: MONDO:0010514
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
citation_count: 9
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 0
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0002720
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased circulating IgA concentration
  - term_id: HP:0001875
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0012311
    reported_labels:
    - Lab abnormality
    ontology_label: Increased total monocyte count
  - term_id: HP:0002718
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent bacterial infections
  - term_id: HP:0004429
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent viral infections
  - term_id: HP:0100845
    reported_labels:
    - Clinical sign
    ontology_label: Anaphylactic shock
  - term_id: HP:0005406
    reported_labels:
    - Lab/functional
    ontology_label: Recurrent bacterial skin infections
  - term_id: HP:0002960
    reported_labels:
    - Clinical sign
    ontology_label: Autoimmunity
  - term_id: HP:0000099
    reported_labels:
    - Clinical sign
    ontology_label: Glomerulonephritis
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Immunodeficiency_Due_To_Moesin_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Immunodeficiency_Due_To_Moesin_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Immunodeficiency Due To Moesin Deficiency
- **MONDO ID:** MONDO:0010514 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Immunodeficiency Due To Moesin Deficiency** covering all of the
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

# Combined Immunodeficiency Due to Moesin Deficiency (X-MAID): A Comprehensive Disease Characteristics Report

**Disease:** Combined Immunodeficiency Due to Moesin Deficiency
**Synonyms:** X-linked Moesin-Associated Immunodeficiency (X-MAID); Immunodeficiency 50 (IMD50); Moesin deficiency
**Key identifiers:** MONDO:0010514 · OMIM 300988 (disease) / 309845 (MSN gene) · Orphanet 504530 · HGNC:7373 · UniProt P26038 · NCBI Gene 4478
**Category:** Mendelian, X-linked recessive, inborn error of immunity

---

## Summary

Combined Immunodeficiency Due to Moesin Deficiency—known in the clinical literature as **X-linked Moesin-Associated Immunodeficiency (X-MAID)** or **Immunodeficiency 50 (IMD50)**—is an ultra-rare, X-linked recessive inborn error of immunity first described by Lagresle-Peyrou and colleagues in 2016. It is caused by hemizygous loss-of-function mutations in **MSN**, the gene on chromosome Xq12 encoding the cytoskeletal adaptor protein **moesin**. Moesin is a member of the ezrin–radixin–moesin (ERM) family that reversibly tethers cortical F-actin to the plasma membrane, and it is essential for lymphocyte shape, adhesion, migration, and signaling. The overwhelmingly recurrent disease allele is the FERM-domain missense variant **p.Arg171Trp (c.511C>T)**, found in 6 of the 7 patients in the founding cohort and in multiple independent families worldwide.

Affected males present in infancy or childhood with **profound lymphopenia** affecting T, B, and NK compartments (with characteristically low naïve T cells and reduced CD8 T cells), **hypogammaglobulinemia**, **fluctuating neutropenia and monocytopenia**, poor responses to vaccine antigens, and heightened susceptibility to bacterial, varicella-zoster (VZV), and Epstein–Barr virus (EBV) infections. In its most severe form the disease produces a **T–B–NK+ SCID-like picture detectable by TREC-based newborn screening**. Beyond classic immunodeficiency, an expanding phenotypic spectrum includes autoimmunity and immune dysregulation: lupus-like nephritis, inflammatory bowel disease–like disease, Kawasaki disease, EBV-driven NK/T-cell lymphoma, and dermatomyositis-like features.

Diagnosis rests on immune laboratory findings, whole-exome (or panel) sequencing of MSN, and confirmation of reduced/absent moesin protein by Western blot and flow cytometry, supported by functional Transwell migration and proliferation assays. Management is lifelong immunoglobulin replacement and anti-infective prophylaxis, while **allogeneic hematopoietic stem cell transplantation (HSCT) offers definitive cure**. Two complementary mouse systems—a moesin knockout and an R171W knock-in—faithfully recapitulate both the lymphopenia/migration defects and an age-dependent lupus-like autoimmunity, anchoring the mechanistic model. Population genetic data from gnomAD (pLI ≈ 1.0, LOEUF ≈ 0.13, missense Z = 3.99) confirm that MSN is highly intolerant to loss-of-function variation, corroborating the pathogenic mechanism.

---

## Key Findings

### Finding 1 — X-MAID is an X-linked combined immunodeficiency caused by hemizygous MSN mutations, most commonly R171W

The founding study by Lagresle-Peyrou et al. (2016) identified hemizygous **MSN** mutations in **7 male patients from 5 different families**. Six of the seven shared the identical missense mutation **c.511C>T, p.Arg171Trp (R171W)**, located in the moesin FERM (four-point-one, ezrin, radixin, moesin) domain; the seventh patient carried a nonsense mutation **R533X** producing a premature stop codon. MSN maps to the X chromosome (Xq12), establishing the X-linked inheritance.

> *"We observed hemizygous mutations in the moesin (MSN) gene (located on the X chromosome and coding for MSN) in all 7 patients. Six of the latter had the same missense mutation, which led to an amino acid substitution (R171W) in the MSN four-point-one, ezrin, radixin, moesin domain. The seventh patient had a nonsense mutation leading to a premature stop codon mutation (R533X)."* — [PMID: 27405666](https://pubmed.ncbi.nlm.nih.gov/27405666/)

The clinical presentation defined in this cohort—profound lymphopenia, hypogammaglobulinemia, fluctuating monocytopenia and neutropenia, poor vaccine responses, and susceptibility to bacterial and VZV infections—remains the diagnostic core of the disease. Subsequent independent reports have confirmed R171W as a recurrent allele (PMID 31139601, 40788322) and added novel pathogenic variants including **N23S** (PMID 38922539) and **I115T** (PMID 42174291), all within the FERM domain.

### Finding 2 — Moesin links the plasma membrane to cortical actin; R171W disrupts lymphocyte homeostasis, proliferation, and migration

Moesin is an ERM-family protein that **reversibly links F-actin to the plasma membrane**, governing cell shape, adhesion, migration, and signal transduction.

> *"The Ezrin-Radixin-Moesin (ERM) family member moesin (MSN) plays a crucial role in reversibly linking F-actin to the cell membrane."* — [PMID: 40788322](https://pubmed.ncbi.nlm.nih.gov/40788322/)

The functional consequences of moesin loss in lymphocytes have been demonstrated in both patients and models. A murine R171W knock-in model revealed **defects in T-cell homeostasis and migration** ([PMID: 35069520](https://pubmed.ncbi.nlm.nih.gov/35069520/)). In patients, impaired T-cell proliferation and impaired cell migration have been documented by Transwell assay (PMID 38922539), and altered B-cell receptor clustering and F-actin dynamics have been shown by TIRF microscopy (PMID 40788322). Patients characteristically display **very low naïve T-cell counts and reduced CD8 T cells** (PMID 27405666), consistent with a defect in the cytoskeletal machinery required for lymphocyte egress, trafficking, and immune synapse formation.

### Finding 3 — The phenotype extends beyond immunodeficiency to autoimmunity/immune dysregulation, and is treatable by HSCT

While recurrent infection defines the disease, an expanding spectrum of immune-dysregulatory and autoimmune manifestations has emerged:

- **Lupus-like autoimmunity and glomerulonephritis** (moesin-KO mice, PMID 28978692; lupus-like nephritis with CXCL13-producing patrolling monocytes, PMID 38640733)
- **EBV infection with nasal-type NK/T-cell lymphoma and dermatomyositis-like symptoms** (N23S, PMID 38922539)
- **Kawasaki disease** with broad-spectrum autoantibodies, Tfr-cell reduction, and a Th1–Th17 imbalance (I115T, PMID 42174291)
- **Inflammatory bowel disease–like disease** (PMID 35754805)
- **Chronic neutropenia** (PMID 39781543)

At its most severe, the disease presents as a **T–B–NK+ SCID phenotype detectable by TREC-based newborn screening** and is effectively treated by hematopoietic stem cell transplantation.

> *"These cases represent a novel manifestation of non-radiosensitive X-linked form of T-B-NK+ SCID that is able to be detected by TREC based newborn screening and effectively treated with HCT."* — [PMID: 31139601](https://pubmed.ncbi.nlm.nih.gov/31139601/)

> *"Mutations in the human moesin gene cause a primary immunodeficiency called X-linked moesin-associated immunodeficiency (X-MAID), which may be complicated by an autoimmune phenotype with kidney involvement."* — [PMID: 38640733](https://pubmed.ncbi.nlm.nih.gov/38640733/)

### Finding 4 — Mouse models recapitulate X-MAID

Two complementary murine systems model the disease:

1. **Moesin-deficient (knockout) mice** exhibit profound lymphopenia mirroring X-MAID. With age, they develop an **SLE-like phenotype** with elevated serum autoantibodies and glomerulonephritis, spontaneous germinal-center B-cell and Tfh accumulation, and enhanced antibody affinity maturation (PMID 28978692). The kidney disease features accumulation of CD4+ cells and CXCL13-producing patrolling monocytes (PMID 38640733).
2. A **moesin R171W knock-in mouse** (Avery et al., 2021) reproduces the exact human point mutation and reveals defects in T-cell homeostasis and migration (PMID 35069520).

> *"we show that aging moesin-deficient mice develop a systemic lupus erythematosus-like autoimmune phenotype, which is characterized by elevated serum autoantibody levels and glomerulonephritis"* — [PMID: 28978692](https://pubmed.ncbi.nlm.nih.gov/28978692/)

> *"We previously reported that moesin-deficient mice exhibit lymphopenia similar to that of X-MAID and develop a lupus-like autoimmune phenotype with age."* — [PMID: 38640733](https://pubmed.ncbi.nlm.nih.gov/38640733/)

### Finding 5 — Diagnosis by TREC newborn screening and exome sequencing, confirmed by absent/reduced moesin protein

The diagnostic pathway integrates four elements: (1) immune laboratory studies showing profound lymphopenia, low naïve T cells, hypogammaglobulinemia, fluctuating neutropenia/monocytopenia, and poor vaccine/proliferative responses (PMID 27405666); (2) **TREC-based newborn screening**, which detected two brothers with a T–B–NK+ SCID phenotype (PMID 31139601); (3) **genetics**, in which whole-exome sequencing (including trio and CNV analysis of exome data) identifies MSN variants—diagnosing cases undiagnosed for as long as 24 years (PMID 29556235); and (4) **protein confirmation** by reduced/absent moesin on Western blot and flow cytometry, complemented by functional Transwell migration and proliferation assays (PMID 29556235, 38922539).

> *"two brothers with positive TREC newborn screening for SCID who were found to have a T-B-NK+ SCID phenotype attributable to X-linked moesin associated immunodeficiency (X-MAID)"* — [PMID: 31139601](https://pubmed.ncbi.nlm.nih.gov/31139601/)

> *"These findings confirm X-linked moesin-associated immunodeficiency in a proband previously undiagnosed up to 24 years of age. This study also highlights the utility of WES for the diagnosis of rare or novel forms of primary immunodeficiency disease."* — [PMID: 29556235](https://pubmed.ncbi.nlm.nih.gov/29556235/)

### Finding 6 — Moesin (577 aa, UniProt P26038): pathogenic missense variants cluster in the N-terminal FERM domain; a Thr558 phospho-switch governs activation

Moesin comprises **577 residues** (UniProt P26038; NCBI Gene 4478; HGNC:7373; Ensembl ENST00000360270). Its domain architecture is an **N-terminal FERM domain (residues ~2–295)**, a central α-helical region, and a **C-terminal ERM association domain (C-ERMAD)** bearing the F-actin binding site. Every reported X-MAID missense mutation—**N23S, I115T, and R171W (c.511C>T)**—maps inside the FERM domain, while the nonsense **R533X** truncates the C-ERMAD.

Moesin activation is regulated by **phosphorylation of Thr558** (by ROCK2 and STK10), which relieves the autoinhibitory head-to-tail interaction between the FERM domain and the C-ERMAD. This conformational switch model, established biochemically for the ERM/merlin family, explains how ligand binding and phosphorylation convert the dormant, autoinhibited protein into its active, actin-linking form.

> *"these interdomain contacts provide a functional explanation for how PIP(2) binding and tyrosine phosphorylation of ezrin lead to activation"* — [PMID: 17134719](https://pubmed.ncbi.nlm.nih.gov/17134719/)

> *"The MSN p.I115T mutant showed reduced protein stability and decreased expression in multiple immune cell types."* — [PMID: 42174291](https://pubmed.ncbi.nlm.nih.gov/42174291/)

FERM-domain missense variants therefore act as **loss-of-function alleles**, at least in part through **reduced protein stability and expression**, rather than gain-of-function or dominant-negative effects.

### Finding 7 — Ultra-rare X-linked recessive disorder of males; fewer than ~20 cases reported; lifelong disease with HSCT curative

X-MAID follows **X-linked recessive** inheritance: affected individuals are hemizygous males and carrier mothers are typically unaffected obligate carriers (PMID 27405666, 31139601). The recurrent **c.511C>T (R171W)** arises independently across unrelated families (French, US, and Chinese cohorts), indicating a **recurrent mutational event at a CpG dinucleotide in an arginine codon** rather than a single ancestral founder. Prevalence is **unknown and ultra-rare**, with only a handful of families reported worldwide since 2016. Cases span pre-symptomatic neonatal detection through diagnosis at age 24 years.

> *"We investigated 7 male patients (from 5 different families)"* — [PMID: 27405666](https://pubmed.ncbi.nlm.nih.gov/27405666/)

Management is **lifelong**: immunoglobulin replacement and anti-infective prophylaxis address the humoral/combined defect, while **allogeneic HSCT provides definitive cure** (three transplanted patients engrafted and were corrected, PMID 31139601).

> *"effectively treated with HCT"* — [PMID: 31139601](https://pubmed.ncbi.nlm.nih.gov/31139601/)

### Finding 8 — MSN is highly loss-of-function intolerant in gnomAD

gnomAD v4 constraint metrics for MSN (queried via the gnomAD GraphQL API) show strong intolerance to variation:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 0.99999 (~1.0) | Extreme LoF intolerance |
| Observed/Expected LoF (oe_lof) | 0.042 | Very few observed LoF variants |
| LOEUF (90% CI upper bound) | 0.131 | Top constraint decile |
| LoF Z | 5.63 | Strongly constrained |
| Missense oe | 0.568 | Depleted missense |
| Missense Z | 3.99 | Significant missense constraint |

These values indicate that pathogenic MSN alleles are essentially **absent from population controls**, providing population-genetic corroboration that MSN loss-of-function is deleterious and consistent with a Mendelian disease gene.

---

## Section-by-Section Disease Characteristics

### 1. Disease Information
X-MAID is a recently described (2016) monogenic combined immunodeficiency with immune dysregulation. **Identifiers:** MONDO:0010514; OMIM 300988 (disease, "Immunodeficiency 50"); OMIM 309845 (MSN gene); Orphanet 504530; MeSH indexing under primary/severe combined immunodeficiency. **Synonyms:** X-linked moesin-associated immunodeficiency; Moesin deficiency; Immunodeficiency 50 (IMD50). Information is derived primarily from **aggregated disease-level resources and individual case reports/small cohorts** (fewer than ~20 patients), supplemented by mouse models.

### 2. Etiology
- **Causal factor:** germline hemizygous loss-of-function mutations in **MSN** (Xq12). Recurrent **p.Arg171Trp (R171W, c.511C>T)** dominates; additional pathogenic FERM-domain missense variants (**N23S, I115T**), a nonsense variant (**R533X**), and a hemizygous gene deletion (PMID 39781543) are reported.
- **Genetic risk factor:** being a hemizygous male carrier of a pathogenic MSN allele; the CpG context of the R171 codon predisposes to recurrent C>T transition.
- **Environmental/protective/gene-environment factors:** none established. Infections (VZV, EBV) act as clinical triggers/complications rather than causes. No protective alleles or lifestyle modifiers are documented.

### 3. Phenotypes
| Phenotype | Type | HPO suggestion | Frequency/notes |
|---|---|---|---|
| Lymphopenia (T, B, NK) | Lab abnormality | HP:0001888 (Lymphopenia) | Profound; near-universal; low naïve T & CD8 T cells |
| Hypogammaglobulinemia | Lab abnormality | HP:0002720 | Common (variable; IgG may be normal in some) |
| Neutropenia | Lab abnormality | HP:0001875 | Fluctuating |
| Monocytopenia | Lab abnormality | HP:0012311 | Fluctuating |
| Recurrent bacterial infections | Clinical sign | HP:0002718 | Common |
| VZV susceptibility | Clinical sign | HP:0004429 | Reported |
| EBV infection / lymphoproliferation | Clinical sign | HP:0100845 | N23S case → NK/T-cell lymphoma |
| Poor vaccine response | Lab/functional | HP:0005406 | Common |
| Autoimmunity (lupus-like, IBD-like, Kawasaki) | Clinical sign | HP:0002960 | Subset |
| Glomerulonephritis / nephritis | Clinical sign | HP:0000099 | Lupus-like nephritis |

**Onset:** neonatal to childhood (SCID-like cases detectable at birth); diagnosis can be delayed to adulthood (up to 24 years). **Severity:** variable, from SCID-like to milder combined immunodeficiency. **Progression:** chronic/lifelong; infections episodic; autoimmunity may be progressive/age-dependent (as in KO mice). **QoL:** substantial burden from recurrent infections, lifelong therapy, and (in transplanted patients) transplant-related morbidity; no formal QoL instruments reported.

### 4. Genetic/Molecular Information
- **Causal gene:** **MSN** (HGNC:7373; OMIM 309845; NCBI Gene 4478; Ensembl ENST00000360270), Xq12.
- **Variants:** missense **p.Asn23Ser (N23S)**, **p.Ile115Thr (I115T)**, **p.Arg171Trp (R171W, c.511C>T)**; nonsense **p.Arg533Ter (R533X)**; whole-gene hemizygous deletion. All missense variants localize to the FERM domain.
- **Classification:** pathogenic/likely pathogenic (ACMG); supported by segregation, functional loss (reduced protein, impaired migration/proliferation), and population absence.
- **Allele frequency:** effectively absent from gnomAD (see Finding 8).
- **Origin:** germline; hemizygous in males.
- **Functional consequence:** **loss of function** (reduced protein stability/expression for missense; truncation for nonsense/deletion). No dominant-negative or gain-of-function mechanism established.
- **Modifier/epigenetic/chromosomal:** none defined.

### 5. Environmental Information
No environmental, occupational, toxic, or lifestyle causal factors. **Infectious agents** (VZV, EBV, bacteria) are opportunistic complications enabled by the immune defect; EBV in particular drives lymphoproliferation/lymphoma in at least one case (N23S, PMID 38922539).

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. A hemizygous MSN FERM-domain mutation (most often R171W) **results in** a destabilized/reduced-abundance moesin protein (loss of function; demonstrated for I115T, inferred for R171W).
2. Reduced functional moesin **leads to** impaired reversible linkage between cortical F-actin and the plasma membrane in leukocytes.
3. Defective actin–membrane coupling **leads to** impaired lymphocyte cytoskeletal dynamics—defective cell shape change, adhesion, immune-synapse F-actin organization, and BCR clustering.
4. These cytoskeletal defects **result in** impaired T-cell migration/trafficking and defective proliferation (shown by Transwell and proliferation assays; recapitulated in the R171W knock-in mouse).
5. Impaired trafficking and proliferation **lead to** profound peripheral lymphopenia (low naïve T, reduced CD8 T, plus B and NK deficits) and fluctuating myeloid cytopenias.
6. Lymphopenia and poor antigen responses **result in** hypogammaglobulinemia, poor vaccine responses, and susceptibility to bacterial, VZV, and EBV infection — the combined immunodeficiency phenotype.
7. **Branch (immune dysregulation):** disrupted lymphocyte homeostasis **leads to** spontaneous germinal-center/Tfh accumulation, autoantibody production, and (age-dependent, shown in KO mice) lupus-like nephritis with CXCL13+ patrolling monocytes; and, in some patients, IBD-like disease, Kawasaki disease (Th1/Th17 imbalance, Tfr reduction), and EBV-driven lymphoma.

**Molecular/cellular detail:** Moesin activation depends on relief of FERM–C-ERMAD autoinhibition via Thr558 phosphorylation (ROCK2, STK10) and PIP2 binding (PMID 17134719). **GO terms:** actin filament binding (GO:0051015), cortical actin cytoskeleton organization (GO:0030866), leukocyte/lymphocyte migration (GO:0050900/GO:0072676), plasma membrane (GO:0005886), cell cortex (GO:0005938). **Cell types (CL):** T cell (CL:0000084), CD8-positive αβ T cell (CL:0000625), naïve T cell (CL:0000898), B cell (CL:0000236), NK cell (CL:0000623), monocyte (CL:0000576), neutrophil (CL:0000775).

### 7. Anatomical Structures Affected
- **Organ/system level:** **immune (hematopoietic/lymphoid) system** primarily — bone marrow, thymus, lymph nodes, spleen (UBERON:0002405 immune system; UBERON:0002371 bone marrow; UBERON:0002370 thymus). Secondary involvement of **kidney** (glomeruli; UBERON:0002113) in lupus-like nephritis, **gastrointestinal tract** in IBD-like disease, **skin/muscle** in dermatomyositis-like cases.
- **Cell level:** lymphocytes (T/B/NK), monocytes, neutrophils.
- **Subcellular:** cell cortex / cortical actin cytoskeleton and plasma membrane (GO:0005938, GO:0005886).
- **Lateralization:** systemic/bilateral (not applicable as a focal lesion).

### 8. Temporal Development
- **Onset:** congenital defect; clinical onset neonatal to childhood; SCID-like cases identifiable at birth by TREC screening. Diagnostic delay up to 24 years reported.
- **Progression:** chronic, lifelong. Infections episodic/recurrent; autoimmunity may emerge and progress with age (age-dependent lupus-like disease in models).
- **Remission:** infections managed but not spontaneously remitting; **HSCT can be curative** (treatment-induced correction).
- **Critical period:** early identification (e.g., via newborn screening) enables timely prophylaxis and transplant before severe infections.

### 9. Inheritance and Population
- **Inheritance:** X-linked recessive; affected males hemizygous; mothers obligate/unaffected carriers.
- **Penetrance/expressivity:** appears high penetrance in hemizygous males but **variable expressivity** (SCID-like to milder; variable autoimmunity).
- **Founder effect:** none; R171W recurs independently (CpG hotspot).
- **Prevalence/incidence:** unknown, ultra-rare (<~20 reported patients worldwide since 2016).
- **Demographics:** males affected; reported across French, US, and Chinese populations — no ethnic clustering. Male-restricted sex ratio.

### 10. Diagnostics
- **Laboratory:** CBC/differential (lymphopenia, fluctuating neutropenia/monocytopenia), lymphocyte subsets (low naïve T, low CD8 T; low B and NK), immunoglobulins (hypogammaglobulinemia), vaccine/antigen response, lymphocyte proliferation assays.
- **Newborn screening:** **TREC assay** detects T–B–NK+ SCID-like cases (PMID 31139601).
- **Genetics:** **whole-exome sequencing** (with trio and exome-CNV analysis) is the primary route; targeted MSN testing and PID gene panels apply; CMA/deletion analysis for the reported gene deletion.
- **Protein/functional confirmation:** reduced/absent moesin by **Western blot and flow cytometry**; **Transwell migration** and proliferation assays.
- **Differential diagnosis:** other SCID/CID (e.g., IL2RG/X-SCID, other actin-regulator defects such as WAS, DOCK8, DOCK2, ARPC1B, coronin-1A), other causes of combined lymphopenia with autoimmunity.

### 11. Outcome/Prognosis
- **Without definitive therapy:** lifelong susceptibility to serious/recurrent infections and, in a subset, autoimmune organ disease (nephritis) and EBV-driven malignancy — significant morbidity and mortality risk.
- **With treatment:** immunoglobulin replacement and prophylaxis reduce infection burden; **allogeneic HSCT is curative** (3 patients corrected, PMID 31139601). No formal survival statistics exist given rarity.
- **Prognostic factors:** severity of lymphopenia (SCID-like vs milder), presence of EBV lymphoproliferation/autoimmunity, and timeliness of diagnosis/transplant.

### 12. Treatment
- **Supportive/pharmacotherapy:** **immunoglobulin replacement** (IVIG/SCIG) for hypogammaglobulinemia (NCIT: Immunoglobulin Therapy); **antimicrobial prophylaxis** (antibacterial, antiviral including VZV/EBV consideration).
- **Definitive:** **allogeneic hematopoietic stem cell transplantation** (NCIT: Allogeneic Hematopoietic Stem Cell Transplantation) — curative; non-radiosensitive disease.
- **Disease-specific management:** treat autoimmune complications (e.g., nephritis, IBD-like disease) and EBV lymphoproliferation per standard protocols.
- **Advanced/experimental:** no approved gene therapy; MSN's strong LoF intolerance and X-linkage make it a conceptual gene-therapy/gene-correction candidate, but none is reported. **Pharmacogenomics:** not established.

### 13. Prevention
- **Primary:** not preventable (germline). **Genetic counseling** for carrier females and at-risk families; prenatal/preimplantation testing feasible where the familial variant is known.
- **Secondary:** **newborn screening (TREC)** enables presymptomatic identification and early intervention; cascade testing of relatives.
- **Tertiary:** infection prophylaxis, immunoglobulin replacement, immunization strategy (avoid live vaccines in SCID-like disease), and timely HSCT to prevent complications.

### 14. Other Species / Natural Disease
- **Orthologs/taxonomy:** mouse *Msn* (NCBI Gene 17698; *Mus musculus*, NCBI Taxon 10090) is the principal comparator. Moesin is highly evolutionarily conserved across vertebrates.
- **Natural disease:** no naturally occurring companion-animal or wildlife X-MAID equivalent is documented in the reviewed literature.
- **Comparative biology:** mouse models replicate lymphopenia, migration defects, and age-dependent lupus-like autoimmunity (see Finding 4), indicating conserved mechanisms.

### 15. Model Organisms
| Model | Type | Key phenotypes | Reference |
|---|---|---|---|
| Moesin knockout mouse | Mammalian, KO | Profound lymphopenia; age-dependent SLE-like autoimmunity, autoantibodies, glomerulonephritis; spontaneous GC B-cell/Tfh accumulation; CXCL13+ patrolling monocytes in kidney | PMID 28978692; 38640733 |
| Moesin R171W knock-in mouse | Mammalian, knock-in | Reproduces human point mutation; defects in T-cell homeostasis and migration | PMID 35069520 |
| Patient-derived cells (in vitro) | Cellular | Reduced moesin protein; impaired T-cell proliferation/migration; altered BCR clustering/F-actin (TIRF) | PMID 38922539; 40788322 |

**Recapitulation:** high for the immunodeficiency (lymphopenia, migration) and for autoimmunity (age-dependent lupus-like disease). **Limitations:** mouse autoimmunity is age-dependent and may not capture full human clinical heterogeneity (IBD-like, Kawasaki, EBV lymphoma); no reported invertebrate model of the disease.

---

## Mechanistic Model / Interpretation

```
MSN FERM-domain mutation (R171W / N23S / I115T / R533X / deletion)  [germline, X-linked, hemizygous male]
        │  (loss of function; reduced protein stability/abundance)
        ▼
Reduced functional moesin
        │  (impaired reversible F-actin ↔ plasma-membrane linkage)
        ▼
Defective cortical actin cytoskeleton dynamics in leukocytes
        │  (cell shape, adhesion, immune synapse, BCR clustering)
        ▼
Impaired lymphocyte migration/trafficking + defective proliferation
        │
        ▼
Profound T/B/NK lymphopenia  ─────────────────┐
(low naïve T, low CD8 T) + myeloid cytopenias  │
        │                                      │ (branch: disrupted homeostasis)
        ▼                                      ▼
Hypogammaglobulinemia, poor vaccine      Immune dysregulation:
responses, infection susceptibility      - lupus-like nephritis (CXCL13+ monocytes)
(bacteria, VZV, EBV)                     - IBD-like disease
        │                                - Kawasaki disease (Th1/Th17, ↓Tfr)
        ▼                                - EBV-driven NK/T-cell lymphoma
Combined immunodeficiency (X-MAID / IMD50)
        │
        ▼
Treatment: Ig replacement + prophylaxis  →  HSCT (curative)
```

The unifying interpretation is that moesin is a **rheostat for leukocyte cortical mechanics**: because it is the dominant ERM protein in lymphocytes, its loss cannot be fully compensated by ezrin/radixin, so cells fail to execute the shape changes required for egress, trafficking, and synapse formation. The **upstream lesion** is a single FERM-domain amino-acid change; the **downstream immunologic consequences** bifurcate into an immunodeficiency arm (numerical/functional lymphocyte failure) and an immune-dysregulation arm (loss of tolerance, spontaneous germinal-center activity). The population-genetic constraint data (Finding 8) and the convergence of independent recurrent R171W events reinforce that MSN dosage/function is under strong purifying selection.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [27405666](https://pubmed.ncbi.nlm.nih.gov/27405666/) | *X-linked PID with hemizygous MSN mutations* | Founding cohort; establishes MSN causality, R171W hotspot, X-linkage, core phenotype |
| [31139601](https://pubmed.ncbi.nlm.nih.gov/31139601/) | *HSCT for X-MAID* | SCID-like presentation, TREC newborn-screening detection, HSCT cure |
| [29556235](https://pubmed.ncbi.nlm.nih.gov/29556235/) | *Exome sequencing diagnoses X-MAID* | WES as diagnostic route; diagnostic delay to age 24 |
| [28978692](https://pubmed.ncbi.nlm.nih.gov/28978692/) | *ERM protein moesin regulates CD8 / KO mouse* | KO mouse: lymphopenia + age-dependent SLE-like autoimmunity |
| [38640733](https://pubmed.ncbi.nlm.nih.gov/38640733/) | *Moesin deficiency → lupus-like nephritis* | Autoimmune kidney mechanism; CXCL13+ patrolling monocytes |
| [35069520](https://pubmed.ncbi.nlm.nih.gov/35069520/) | *Murine R171W model of X-MAID* | Knock-in mouse: T-cell homeostasis & migration defects |
| [38922539](https://pubmed.ncbi.nlm.nih.gov/38922539/) | *Novel MSN N23S mutation* | New variant; EBV/NK-T lymphoma, dermatomyositis-like features; impaired proliferation/migration |
| [42174291](https://pubmed.ncbi.nlm.nih.gov/42174291/) | *Novel MSN I115T variant* | New variant; reduced protein stability (LoF mechanism); Kawasaki disease |
| [40788322](https://pubmed.ncbi.nlm.nih.gov/40788322/) | *Immunodeficiency profile with MSN mutation* | Moesin F-actin–membrane linker function; BCR/F-actin dynamics |
| [39781543](https://pubmed.ncbi.nlm.nih.gov/39781543/) | *Hemizygous MSN deletion, adult neutropenia* | Structural (deletion) allele; chronic neutropenia presentation |
| [35754805](https://pubmed.ncbi.nlm.nih.gov/35754805/) | *Novel MSN variant, IBD-like disease* | Expands phenotype to IBD-like disease |
| [17134719](https://pubmed.ncbi.nlm.nih.gov/17134719/) | *Self-masking in ERM-merlin* | Autoinhibition/activation switch model (Thr558 phospho-regulation) |
| [15751968](https://pubmed.ncbi.nlm.nih.gov/15751968/) | *Ezrin dimerization/activation mutants* | Supports conformational activation model of ERM proteins |
| [19084535](https://pubmed.ncbi.nlm.nih.gov/19084535/) | *Ezrin mutant defective in F-actin binding* | Maps C-terminal F-actin binding & FERM/tail hotspot |

**Evidence source types:** human clinical (case reports/small cohorts), model organism (KO and knock-in mice), in vitro (patient cells, TIRF/Transwell), and computational/population-genetic (gnomAD constraint).

---

## Limitations and Knowledge Gaps

- **Extreme rarity:** fewer than ~20 patients worldwide preclude reliable prevalence, penetrance, survival, and genotype–phenotype correlation estimates.
- **Direct R171W functional proof:** reduced protein stability is demonstrated for I115T; the R171W loss-of-function mechanism is strongly inferred (via modeling and phenotype) but less directly quantified in patient cells.
- **Phenotype–genotype map:** why some patients develop SCID-like disease versus milder CID, or specific autoimmune manifestations (Kawasaki, IBD-like, lupus-like, EBV lymphoma), is unexplained—no established modifier genes or environmental modifiers.
- **HSCT evidence base:** curative HSCT is documented in only a few patients; long-term outcomes, optimal conditioning, and autoimmunity resolution post-transplant are not systematically characterized.
- **No approved targeted/gene therapy;** pharmacogenomics undefined.
- **QoL and natural-history data** are absent; no standardized instruments applied.
- **Citation caveat:** one supporting snippet (PMID 35069520) was recorded as a title-level match rather than a verified abstract quote; the corresponding claim (mouse T-cell homeostasis/migration defects) is consistent with the model's stated purpose but should be confirmed against the primary text.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry** for X-MAID to aggregate genotype, phenotype, treatment, and outcome data across the scattered case reports and enable prevalence/penetrance estimates.
2. **Systematic functional characterization of each variant** (N23S, I115T, R171W, R533X, deletion) in primary patient lymphocytes and isogenic cell lines: quantify moesin abundance, Thr558 phosphorylation, F-actin binding, migration (Transwell/chemotaxis), and immune-synapse formation to build a variant-function map.
3. **Structural analysis** (cryo-EM/crystallography or AlphaFold-guided modeling) of R171W and other FERM-domain mutants to define how each perturbs FERM folding, C-ERMAD autoinhibition, and ligand binding.
4. **Post-HSCT longitudinal follow-up** across all transplanted patients to determine whether transplantation resolves both immunodeficiency and autoimmunity, and to define conditioning best practices.
5. **Mechanistic dissection of the autoimmunity branch** using the KO and R171W knock-in mice—track germinal-center/Tfh dynamics, CXCL13+ monocyte recruitment, and test whether B-cell– or Tfh-targeted therapies prevent lupus-like nephritis.
6. **EBV surveillance protocol** given the reported NK/T-cell lymphoma, to establish whether pre-emptive EBV monitoring/therapy reduces malignancy risk.
7. **Explore gene-correction/gene-therapy feasibility** (e.g., HSC lentiviral or base/prime editing of MSN) leveraging the strong LoF intolerance and single recurrent hotspot as an attractive editing target.
8. **Expand newborn-screening interpretation** so that TREC-positive, non-radiosensitive T–B–NK+ cases prompt early MSN sequencing.

---

*Report compiled from 8 confirmed findings and 17 reviewed papers over 5 investigation iterations. Evidence is predominantly human case-level and model-organism data, corroborated by population-genetic constraint metrics.*


## Artifacts

- [OpenScientist final report](Combined_Immunodeficiency_Due_To_Moesin_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Immunodeficiency_Due_To_Moesin_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002720` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased circulating IgA concentration**
- `HP:0001875` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased total neutrophil count**
- `HP:0012311` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Increased total monocyte count**
- `HP:0002718` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent bacterial infections**
- `HP:0004429` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent viral infections**
- `HP:0100845` (1 mention) - the report calls it "Clinical sign"; HP calls it **Anaphylactic shock**
- `HP:0005406` (1 mention) - the report calls it "Lab/functional"; HP calls it **Recurrent bacterial skin infections**
- `HP:0002960` (1 mention) - the report calls it "Clinical sign"; HP calls it **Autoimmunity**
- `HP:0000099` (1 mention) - the report calls it "Clinical sign"; HP calls it **Glomerulonephritis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001888` (1 mention) - the report calls it "Lymphopenia"; HP calls it **Decreased total lymphocyte count**, and lists "Lymphopenia" among its other names