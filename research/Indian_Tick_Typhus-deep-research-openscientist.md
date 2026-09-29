---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-27T22:50:43.129888'
end_time: '2026-09-27T23:05:55.971601'
duration_seconds: 912.84
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Indian Tick Typhus
  mondo_id: MONDO:0000229
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
citation_count: 37
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 37
  on_topic: 22
  off_topic: 1
  off_topic_references:
  - PMID:12832625
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 31
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 1
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0000229
    reported_labels:
    - MONDO
    ontology_label: Indian tick typhus
  - term_id: HP:0200041
    reported_labels:
    - cutaneous ulcer/eschar
    ontology_label: Skin erosion
  - term_id: UBERON:0002097
    reported_labels:
    - Rash, eschar/*tache noire
    ontology_label: skin of body
  - term_id: UBERON:0000955
    reported_labels:
    - Meningoencephalitis, cerebral infarction
    ontology_label: brain
  - term_id: UBERON:0002048
    reported_labels:
    - Interstitial pneumonia/infiltrates
    ontology_label: lung
  - term_id: UBERON:0002107
    reported_labels:
    - Transaminitis, hepatic granulomas (Kupffer cell/hepatocyte infection)
    ontology_label: liver
  - term_id: UBERON:0002113
    reported_labels:
    - Proteinuria, acute tubular necrosis/renal failure
    ontology_label: kidney
  - term_id: UBERON:0000178
    reported_labels:
    - Thrombocytopenia, HLH
    ontology_label: blood
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Indian_Tick_Typhus-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Indian_Tick_Typhus-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Indian Tick Typhus
- **MONDO ID:** MONDO:0000229 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Indian Tick Typhus** covering all of the
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

# Indian Tick Typhus (MONDO:0000229): A Comprehensive Disease Characterization

## Summary

**Indian tick typhus (ITT)** is an acute, tick-borne bacterial zoonosis and a member of the spotted fever group (SFG) rickettsioses. It is caused by *Rickettsia conorii* subsp. *indica* (reference strain ITTR, ATCC VR-597), an obligate intracellular Gram-negative coccobacillus, and is transmitted to humans through the bite of the brown dog tick, *Rhipicephalus sanguineus* [PMID: 22628514](https://pubmed.ncbi.nlm.nih.gov/22628514/); [PMID: 32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/). It is one of four genotypic subspecies within *R. conorii* — alongside the Malish/Mediterranean spotted fever (MSF) strain, Astrakhan fever, and Israeli spotted fever — which are >98% identical at the nucleotide level yet serotypically distinct [PMID: 15766388](https://pubmed.ncbi.nlm.nih.gov/15766388/). Because ITT is clinically, mechanistically, and therapeutically part of the *R. conorii*/MSF continuum, much of the mechanistic and clinical evidence base is shared across these subspecies.

The core pathophysiology is a **systemic small-vessel vasculitis**: the bacterium adheres to and invades vascular endothelial cells using surface cell antigen (Sca) autotransporter proteins and hijacks the host Arp2/3 actin-nucleation machinery for entry and intracellular actin-based motility [PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/); [PMID: 22188208](https://pubmed.ncbi.nlm.nih.gov/22188208/). Endothelial infection triggers inflammation, platelet and coagulation activation, and increased vascular permeability, producing the classic clinical triad of fever, an inoculation eschar (*tache noire*), and a maculopapular rash [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/); [PMID: 8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/). Disease is usually mild-to-moderate and self-limited, but severe "malignant" forms — strongly age-dependent — cause meningoencephalitis, hemophagocytic lymphohistiocytosis (HLH), purpura fulminans, and multi-organ failure [PMID: 32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/); [PMID: 30972588](https://pubmed.ncbi.nlm.nih.gov/30972588/).

Diagnosis rests on serology (indirect immunofluorescence assay [IFA] is the gold standard, Weil–Felix is nonspecific) and, increasingly, species-specific PCR of the *gltA* and *ompA* genes. **Doxycycline** is the unequivocal treatment of choice, producing rapid defervescence and excellent outcomes; there is **no human genetic etiology and no licensed vaccine**, so prevention depends on personal protection against tick bites and control of brown dog ticks on dogs and in the environment [PMID: 42390463](https://pubmed.ncbi.nlm.nih.gov/42390463/); [PMID: 30150470](https://pubmed.ncbi.nlm.nih.gov/30150470/); [PMID: 15109588](https://pubmed.ncbi.nlm.nih.gov/15109588/). This report is compiled from **aggregated disease-level resources and primary literature**, not from individual EHR records. Because ITT is caused by an intracellular bacterium, several template sections designed for genetic/Mendelian disorders (causal human genes, pathogenic variants, inheritance patterns) are **not applicable** and are explicitly marked as such.

---

## Section 1 — Disease Information

**Overview.** Indian tick typhus is an acute febrile illness caused by *Rickettsia conorii* subsp. *indica*, an obligate intracellular member of the spotted fever group of the genus *Rickettsia*. It is the principal SFG rickettsiosis of the Indian subcontinent and presents as fever with an inoculation eschar and maculopapular rash following a tick bite [PMID: 30451192](https://pubmed.ncbi.nlm.nih.gov/30451192/); [PMID: 41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0000229 |
| ICD-10 | A77.1 (Spotted fever due to *Rickettsia conorii*) |
| ICD-11 | 1C30.0 (Spotted fever group rickettsiosis) |
| MeSH | Boutonneuse Fever (D001907) — MSF/*R. conorii* group |
| NCBI Taxonomy (pathogen) | *Rickettsia conorii* subsp. *indica* |
| Reference strain | ITTR, ATCC VR-597 |

**Synonyms / alternative names:** Indian tick typhus; *Rickettsia conorii* subsp. *indica* infection; Indian tick typhus rickettsiosis (ITTR). It sits within the broader **Mediterranean spotted fever / boutonneuse fever** complex and the SFG rickettsioses.

**Source of information:** Aggregated disease-level literature and reference microbiology resources — not individual EHR data.

---

## Section 2 — Etiology

**Primary cause (infectious).** ITT is caused by *R. conorii* subsp. *indica* strain ITTR (ATCC VR-597), the etiologic agent identified by genome sequencing [PMID: 22628514](https://pubmed.ncbi.nlm.nih.gov/22628514/). It is one of four multi-locus sequence typing (MLST) genotypes within *R. conorii*, sharing 98.2–100% pairwise nucleotide similarity across *16S rRNA*, *gltA*, *ompA*, *ompB*, and *sca4* with the Malish (MSF), Astrakhan fever, and Israeli spotted fever genotypes, yet remaining serotypically distinct [PMID: 15766388](https://pubmed.ncbi.nlm.nih.gov/15766388/). The vector is the brown dog tick *Rhipicephalus sanguineus*; ITTR has also been detected in *Rhipicephalus turanicus* removed from a patient [PMID: 41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/).

**Risk factors — environmental/behavioral.** The dominant risk factor is **tick exposure**. In a military cohort, the primary risk factor for confirmed/probable SFG disease was finding **>10 ticks on the body** [PMID: 12653142](https://pubmed.ncbi.nlm.nih.gov/12653142/). Occupational and recreational contact with dogs and tick habitats, warm-season (summer) exposure, and residence in or travel to endemic areas increase risk [PMID: 40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/); [PMID: 41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/). **Advanced age** is the strongest risk factor for *severe* disease (see Section 11).

**Risk factors — genetic.** No human host genetic susceptibility variants have been established for ITT; this is an environmentally/behaviorally driven infectious disease. *(Not applicable — no human causal or susceptibility loci identified.)*

**Protective factors.** Behavioral: doxycycline use and rolling up long sleeves were protective against seropositivity in an exposed cohort [PMID: 12653142](https://pubmed.ncbi.nlm.nih.gov/12653142/); tick repellents, permethrin-treated clothing, and frequent tick checks reduce exposure [PMID: 33549976](https://pubmed.ncbi.nlm.nih.gov/33549976/). No genetic protective variants are described. *(Genetic protective factors not applicable.)*

**Gene–environment interactions.** Not applicable — no human genotype × exposure interactions have been characterized for this infectious disease.

---

## Section 3 — Phenotypes

The clinical phenotype is a systemic febrile vasculitic illness. Key manifestations, with suggested HPO terms:

| Phenotype | Type | Frequency / notes | HPO suggestion |
|---|---|---|---|
| Fever | Symptom | ~100% (universal) | HP:0001945 Fever |
| Maculopapular rash (incl. palms/soles) | Clinical sign | ~100% in pediatric cohorts; may involve palms and soles | HP:0000988 Skin rash |
| Inoculation eschar (*tache noire*) | Clinical sign | ~74–77% in adult MSF; **rare (6%)** in some pediatric cohorts | HP:0200041 (cutaneous ulcer/eschar) |
| Headache | Symptom | Common | HP:0002315 Headache |
| Thrombocytopenia | Lab abnormality | ~56% | HP:0001873 Thrombocytopenia |
| Elevated transaminases | Lab abnormality | ~83% | HP:0002910 Elevated hepatic transaminase |
| Proteinuria | Lab abnormality | Reported | HP:0000093 Proteinuria |
| Hyponatremia | Lab abnormality | ~78% (pediatric) | HP:0002902 Hyponatremia |
| Meningoencephalitis | Clinical sign (severe) | ~28% neurological involvement (pediatric); rare severe | HP:0002383 Encephalitis |
| Hemophagocytic lymphohistiocytosis | Lab/clinical (severe) | Rare; fatal case, H-score 224 | HLH-associated |
| Retinitis (bilateral multifocal) | Clinical sign (severe) | Rare; ~4 weeks post-fever | Retinitis (HP:0000602-adjacent) |
| Peripheral gangrene / purpura fulminans | Clinical sign (severe) | Rare | HP:0100758 Gangrene |

The **classic triad** is fever + eschar/rash + multisystem involvement [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/). A representative adult presentation: "*A 55-year-old female farmer presented with fever, headache, eschar, and a maculopapular rash following a tick bite. Laboratory findings indicated thrombocytopenia, liver enzyme elevation, and proteinuria*" [PMID: 41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/).

**Onset, severity, progression, frequency.** Onset is **acute**, typically after an incubation of several days following a tick bite. Rash usually appears on days 3–6 but may be delayed to day 8 in atypical cases [PMID: 29331008](https://pubmed.ncbi.nlm.nih.gov/29331008/). Severity is **variable** — most cases are mild and self-limited; a minority progress to severe multi-organ disease. Progression is **acute/monophasic** with recovery on treatment.

**Quality-of-life impact.** In uncomplicated, promptly treated disease, QoL impact is short-lived (hospital stay ~5 days, full recovery) [PMID: 41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/). Severe forms cause lasting disability: e.g., a 14-month-old with meningoencephalitis had persistent neurological sequelae including decreased vision and epileptic seizures [PMID: 20797742](https://pubmed.ncbi.nlm.nih.gov/20797742/), and amputation was required in one case of symmetric peripheral gangrene [PMID: 29169658](https://pubmed.ncbi.nlm.nih.gov/29169658/). No formal EQ-5D/SF-36 data are available for ITT specifically.

---

## Section 4 — Genetic/Molecular Information

**This section is largely NOT APPLICABLE** in the Mendelian sense: ITT is an infectious disease with **no causal human genes, no pathogenic human germline/somatic variants, no modifier genes, and no chromosomal abnormalities**. There is no human inheritance.

The relevant "genetics" are those of the **pathogen genome**:

- *R. conorii* has a small, **reductive genome** (~1.27 Mb, ~1,374 genes) with the fewest pseudogenes among rickettsiae and 560 unique genes [PMID: 16481486](https://pubmed.ncbi.nlm.nih.gov/16481486/).
- All *Rickettsia* **lack enzymes for sugar metabolism, lipid biosynthesis, nucleotide synthesis, and amino acid metabolism**, depending on the host for nutrition and building blocks; they retain a complete TCA cycle, multiple ATP/ADP translocase genes (to import host ATP), and a type IV secretion system [PMID: 16481486](https://pubmed.ncbi.nlm.nih.gov/16481486/).
- Key pathogen loci: *sca2* (adhesin/invasin/actin motility), *ompA* and *ompB* (Sca5/Sca0 outer membrane proteins; also diagnostic targets), *sca4*, *gltA* (citrate synthase; diagnostic target), and *rickA* (actin polymerization, unique to SFG) [PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/); [PMID: 16481486](https://pubmed.ncbi.nlm.nih.gov/16481486/).
- **Virulence in *Rickettsia* is largely associated with genome reduction / loss of regulatory genes** [PMID: 19379498](https://pubmed.ncbi.nlm.nih.gov/19379498/), and ~80% of *R. conorii* "orphan" ORFs are short gene fragments reflecting ongoing genome decay [PMID: 12832625](https://pubmed.ncbi.nlm.nih.gov/12832625/).

**Epigenetics / host molecular profiling:** No host DNA-methylation, histone-modification, or large-scale transcriptomic/proteomic/metabolomic disease signatures specific to ITT have been established beyond selective modulation of host antioxidant enzymes (Section 6).

---

## Section 5 — Environmental Information

**Infectious agent:** *Rickettsia conorii* subsp. *indica* (SFG rickettsia; obligate intracellular Gram-negative coccobacillus) [PMID: 22628514](https://pubmed.ncbi.nlm.nih.gov/22628514/).

**Environmental / ecological factors:** The disease is defined by an arthropod-borne transmission ecology. The vector-and-reservoir is the brown dog tick *R. sanguineus* (with transovarial and transstadial maintenance characteristic of SFG rickettsiae), and dogs/companion animals amplify circulation [PMID: 32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/); [PMID: 40871278](https://pubmed.ncbi.nlm.nih.gov/40871278/). Warm seasons and tick-dense habitats increase exposure.

**Lifestyle factors:** Outdoor/occupational activity (farming, military, recreation) in endemic areas and dog contact are the principal behavioral determinants [PMID: 12653142](https://pubmed.ncbi.nlm.nih.gov/12653142/); [PMID: 41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/). Classic toxic/pollution/radiation exposures are not relevant.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. An infected *R. sanguineus* tick bites the human host and inoculates *R. conorii* subsp. *indica* into the dermis — **leads to** local infection at the bite site (forming the eschar/*tache noire*).
2. Rickettsial **Sca2** autotransporter (with OmpA/OmpB adhesins) mediates **adherence to and invasion of vascular endothelial cells** — **results in** intracellular infection [PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/).
3. Invasion **converges on the host Arp2/3 complex** (with Rac GTPases and the WAVE nucleation-promoting complex), which nucleates actin to drive bacterial entry — **leads to** cytosolic access [PMID: 22188208](https://pubmed.ncbi.nlm.nih.gov/22188208/).
4. Once cytosolic, **Sca2** and **RickA** nucleate actin for **intracellular actin-based motility**, enabling cell-to-cell spread — **results in** dissemination through the endothelium [PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/); [PMID: 16481486](https://pubmed.ncbi.nlm.nih.gov/16481486/).
5. Endothelial infection triggers **endothelial inflammation and injury (vasculitis)** — **leads to** microvascular dysfunction [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/).
   - **Branch A (coagulation):** Endothelial injury drives **TXA2-dependent platelet activation and thrombin generation** — **results in** focal microthrombus formation [PMID: 8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/).
   - **Branch B (permeability):** Endothelial dysfunction (raised endothelin-1) **increases vascular permeability** — **results in** edema, rash, and, when severe, multi-organ failure [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/); [PMID: 8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/).
   - **Branch C (autoimmunity, inferred):** Endothelial membrane damage elicits **antiphospholipid antibodies**, which may contribute to microthrombi (mechanistic role inferred, not proven) [PMID: 8679900](https://pubmed.ncbi.nlm.nih.gov/8679900/).
6. Systemic small-vessel vasculitis in skin, brain, lung, liver, kidney, and eye — **leads to** the multi-organ clinical phenotype (fever, rash, eschar, and, in severe cases, meningoencephalitis, HLH, gangrene, renal failure) [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/); [PMID: 7511715](https://pubmed.ncbi.nlm.nih.gov/7511715/).
7. **Protective immunity** requires **CD8 T lymphocytes** to clear rickettsiae from endothelial cells; failure of this response — **leads to** persistent/lethal infection [PMID: 9164951](https://pubmed.ncbi.nlm.nih.gov/9164951/).

### Detail by category

**Molecular pathways / cellular processes.** Host actin-cytoskeleton remodeling via the **Arp2/3 complex, WAVE2, and Rho-family GTPases (Rac1/Rac2)** drives invasion; an RNAi screen identified 21 core host proteins required [PMID: 22188208](https://pubmed.ncbi.nlm.nih.gov/22188208/). Downstream cellular processes are **endothelial inflammation/activation, platelet activation, coagulation, and increased permeability** (GO suggestions: GO:0002544 chronic inflammatory response; GO:0007596 blood coagulation; GO:0030041 actin filament polymerization; GO:0050900 leukocyte migration).

**Protein dysfunction.** Pathogen surface autotransporters **Sca2, OmpA (Sca5), OmpB (Sca0)** mediate host-cell association; Sca2 has separable **mammalian-association** and **actin-nucleation** domains — pre-incubation with the mammalian-association region competitively inhibits invasion [PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/).

**Metabolic changes.** The pathogen imports host ATP via ATP/ADP translocases and lacks biosynthetic pathways [PMID: 16481486](https://pubmed.ncbi.nlm.nih.gov/16481486/). In the host, **antioxidant/oxidative-stress enzymes (glutathione peroxidase/reductase, SOD, G6PD) are selectively modulated in infected tissues, most in the lungs** [PMID: 15120155](https://pubmed.ncbi.nlm.nih.gov/15120155/) — evidence for **oxidative stress** as a tissue-damage mechanism.

**Immune involvement.** Protective clearance is **CD8 T-cell dependent**: CD8-depleted (but not CD4-depleted) mice die or remain persistently infected, and adoptive transfer of immune CD4 or CD8 cells protects [PMID: 9164951](https://pubmed.ncbi.nlm.nih.gov/9164951/). Cell types (CL suggestions): endothelial cell (CL:0000115); CD8-positive T cell (CL:0000625); platelet (CL:0000233); Kupffer cell / macrophage (CL:0000091).

**Tissue damage mechanisms.** Vasculitis-driven microvascular injury, microthrombosis/ischemia, oxidative stress, and increased permeability [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/); [PMID: 8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/); [PMID: 15120155](https://pubmed.ncbi.nlm.nih.gov/15120155/).

---

## Section 7 — Anatomical Structures Affected

Because the primary target is **vascular endothelium** (UBERON:0002139 endothelium; UBERON:0001981 blood vessel), disease is **systemic and multi-organ**.

| Organ / system | Involvement | UBERON | Evidence |
|---|---|---|---|
| Skin | Rash, eschar/*tache noire* | UBERON:0002097 | [PMID: 40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/) |
| Brain / CNS | Meningoencephalitis, cerebral infarction | UBERON:0000955 | [PMID: 20797742](https://pubmed.ncbi.nlm.nih.gov/20797742/); [PMID: 28491211](https://pubmed.ncbi.nlm.nih.gov/28491211/); [PMID: 35263931](https://pubmed.ncbi.nlm.nih.gov/35263931/) |
| Lung | Interstitial pneumonia/infiltrates | UBERON:0002048 | [PMID: 7511715](https://pubmed.ncbi.nlm.nih.gov/7511715/); [PMID: 30972588](https://pubmed.ncbi.nlm.nih.gov/30972588/) |
| Liver | Transaminitis, hepatic granulomas (Kupffer cell/hepatocyte infection) | UBERON:0002107 | [PMID: 7511715](https://pubmed.ncbi.nlm.nih.gov/7511715/); [PMID: 41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/) |
| Kidney | Proteinuria, acute tubular necrosis/renal failure | UBERON:0002113 | [PMID: 41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/); [PMID: 28292166](https://pubmed.ncbi.nlm.nih.gov/28292166/) |
| Eye | Bilateral multifocal retinitis | retina UBERON:0000966 | [PMID: 30451192](https://pubmed.ncbi.nlm.nih.gov/30451192/) |
| Blood / marrow | Thrombocytopenia, HLH | UBERON:0000178 | [PMID: 40693676](https://pubmed.ncbi.nlm.nih.gov/40693676/); [PMID: 41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/) |

**Body systems:** cardiovascular (small vessels), nervous, respiratory, hepatobiliary/digestive, urinary, hematologic, and ophthalmic. **Tissue/cell level:** vascular endothelial cells (CL:0000115) are the primary target; Kupffer cells/macrophages and hepatocytes are infected in the liver [PMID: 7511715](https://pubmed.ncbi.nlm.nih.gov/7511715/). **Subcellular:** the bacterium resides free in the **host cytosol** (GO:0005829 cytosol) and manipulates the **actin cytoskeleton** (GO:0015629). **Lateralization:** manifestations are generally **bilateral/systemic** (e.g., bilateral multifocal retinitis; bilateral asymmetric brain lesions on MRI) [PMID: 30451192](https://pubmed.ncbi.nlm.nih.gov/30451192/); [PMID: 35263931](https://pubmed.ncbi.nlm.nih.gov/35263931/).

---

## Section 8 — Temporal Development

**Onset:** Acute, affecting all age groups (children through elderly) [PMID: 32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/). Symptoms begin days after a tick bite; rash typically emerges on days 3–6 (occasionally delayed to day 8) [PMID: 29331008](https://pubmed.ncbi.nlm.nih.gov/29331008/).

**Progression / course:** Predominantly **acute, monophasic, and self-limited**. With prompt doxycycline, fever resolves within ~2–2.5 days and patients recover fully in days [PMID: 30150470](https://pubmed.ncbi.nlm.nih.gov/30150470/); [PMID: 41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/). A minority progress rapidly to **severe "malignant" multi-organ disease** [PMID: 32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/).

**Duration / remission:** Self-limited/treatment-resolved; not chronic or relapsing. There is no established latent or recurrent phase.

**Critical period for intervention:** The **acute phase**, when doxycycline is most effective — early empirical therapy (before serologic confirmation) is the key intervention window [PMID: 42390463](https://pubmed.ncbi.nlm.nih.gov/42390463/); [PMID: 28361787](https://pubmed.ncbi.nlm.nih.gov/28361787/).

---

## Section 9 — Inheritance and Population

**Inheritance:** Not applicable — infectious, non-heritable. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency applies.

**Epidemiology.** In a 10-year Bulgarian cohort of 549 MSF patients, incidence reached **9.44/100,000**; *tache noire* was present in ~74–77% [PMID: 32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/). Rickettsial diseases contribute **25–50% of acute undifferentiated febrile illnesses** in endemic regions [PMID: 42390463](https://pubmed.ncbi.nlm.nih.gov/42390463/); [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/). In India, only limited serologically proven outbreaks of ITT specifically have been reported, and it is likely underdiagnosed [PMID: 30451192](https://pubmed.ncbi.nlm.nih.gov/30451192/).

**Geographic distribution:** Endemic to the Indian subcontinent for the *indica* subspecies; the broader *R. conorii*/MSF complex is endemic across the Mediterranean basin, Africa, the Middle East, and parts of Asia [PMID: 15766388](https://pubmed.ncbi.nlm.nih.gov/15766388/); [PMID: 40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/). Cases cluster in **summer/warm seasons** [PMID: 41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/).

**Demographics / sex / age:** All ages are affected; pediatric cohorts show slight male predominance (e.g., 56% male) [PMID: 41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/). **Age is the dominant demographic determinant of severity**, with severe disease more frequent in those >65 years (26.4% vs 10.5%; p=0.002) [PMID: 30972588](https://pubmed.ncbi.nlm.nih.gov/30972588/).

---

## Section 10 — Diagnostics

**Serology (mainstay):** **IFA** is the gold standard but is largely retrospective due to delayed seroconversion; the **Weil–Felix test** lacks specificity; false negatives occur early [PMID: 42390463](https://pubmed.ncbi.nlm.nih.gov/42390463/); [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/). Seroconversion is often documented only in convalescent samples [PMID: 30522428](https://pubmed.ncbi.nlm.nih.gov/30522428/).

**Molecular (PCR):** **Multiplex/real-time PCR** enables early, species-specific identification during the acute phase; species confirmation is by PCR and DNA sequencing of the ***gltA*** and ***ompA*** genes, often from eschar/skin biopsy [PMID: 42390463](https://pubmed.ncbi.nlm.nih.gov/42390463/); [PMID: 40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/); [PMID: 30522428](https://pubmed.ncbi.nlm.nih.gov/30522428/).

**Laboratory findings (supportive):** thrombocytopenia, elevated transaminases, proteinuria, hyponatremia, raised CRP [PMID: 41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/); [PMID: 41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/). **Imaging:** MRI shows multifocal bilateral T2/FLAIR hyperintensities with diffusion restriction in meningoencephalitis [PMID: 35263931](https://pubmed.ncbi.nlm.nih.gov/35263931/).

**Genetic/omics testing (host):** Not applicable — no human genetic testing is used to diagnose this infectious disease. The relevant "genetic testing" is **pathogen genotyping** (gltA/ompA sequencing).

**Clinical criteria & differential diagnosis:** Diagnosis is clinical-epidemiological (fever + rash involving palms/soles + eschar after tick exposure) supported by serology/PCR [PMID: 40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/). **Differentials:** dengue, malaria, leptospirosis, scrub typhus, measles, and other causes of acute undifferentiated febrile illness [PMID: 42390463](https://pubmed.ncbi.nlm.nih.gov/42390463/); [PMID: 42658412](https://pubmed.ncbi.nlm.nih.gov/42658412/).

---

## Section 11 — Outcome/Prognosis

**Overall prognosis is excellent with prompt treatment.** In a prospective cohort, single-day doxycycline produced uneventful recovery in **all** patients, with fever clearing **2.55 ± 1.14 days** after treatment; 11.4% had severe disease [PMID: 30150470](https://pubmed.ncbi.nlm.nih.gov/30150470/). A pediatric cohort reported rapid defervescence and full recovery with **no deaths or severe complications** [PMID: 41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/).

**Severity and mortality.** MSF/*R. conorii* is historically benign but includes **severe "malignant" forms with fatal outcomes strongly influenced by patient age** [PMID: 32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/). Severe disease is more frequent in the elderly (**26.4% vs 10.5%; p=0.002**) [PMID: 30972588](https://pubmed.ncbi.nlm.nih.gov/30972588/). A purpura fulminans case series (including SFG rickettsioses) reported **18.2% overall mortality** [PMID: 32998655](https://pubmed.ncbi.nlm.nih.gov/32998655/).

**Complications:** meningoencephalitis with neurological sequelae (decreased vision, epilepsy) [PMID: 20797742](https://pubmed.ncbi.nlm.nih.gov/20797742/); cerebral infarction/stroke [PMID: 28491211](https://pubmed.ncbi.nlm.nih.gov/28491211/); HLH (fatal case, H-score 224) [PMID: 40693676](https://pubmed.ncbi.nlm.nih.gov/40693676/); symmetric peripheral gangrene requiring amputation [PMID: 29169658](https://pubmed.ncbi.nlm.nih.gov/29169658/); acute tubular necrosis and fatal multivisceral failure with late diagnosis [PMID: 28292166](https://pubmed.ncbi.nlm.nih.gov/28292166/); and rickettsial retinitis [PMID: 30451192](https://pubmed.ncbi.nlm.nih.gov/30451192/).

**Prognostic factors:** advanced age, diagnostic/treatment delay, and severe multi-organ involvement predict poor outcome; timely doxycycline is the strongest modifiable predictor of good outcome [PMID: 32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/); [PMID: 28292166](https://pubmed.ncbi.nlm.nih.gov/28292166/).

---

## Section 12 — Treatment

**First-line pharmacotherapy: Doxycycline** (tetracycline-class; NCIT: C305 Doxycycline). It is the drug of choice, halting bacterial replication and producing rapid clinical response [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/); [PMID: 28361787](https://pubmed.ncbi.nlm.nih.gov/28361787/). Regimens include short-course oral therapy (even single-day, two 200 mg doses) with uneventful recovery [PMID: 30150470](https://pubmed.ncbi.nlm.nih.gov/30150470/), and **IV doxycycline with a loading dose** in critically ill patients [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/). Indian pediatric guidelines emphasize prompt empirical treatment without waiting for confirmatory tests [PMID: 28361787](https://pubmed.ncbi.nlm.nih.gov/28361787/).

**Alternative:** **Azithromycin** (macrolide; NCIT: C1005) is a suitable alternative [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/); fluoroquinolones have been used adjunctively in some reports [PMID: 28491211](https://pubmed.ncbi.nlm.nih.gov/28491211/).

**Supportive/interventional care:** organ support in severe disease; vasodilators (iloprost) and anticoagulation for peripheral gangrene; renal replacement therapy for acute tubular necrosis [PMID: 29169658](https://pubmed.ncbi.nlm.nih.gov/29169658/); [PMID: 28292166](https://pubmed.ncbi.nlm.nih.gov/28292166/). "Early appropriate treatment and organ support can decrease the duration of illness and be life-saving" [PMID: 34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/).

**Not applicable:** gene therapy, cell therapy, RNA-based therapy, targeted/immuno-oncology therapy, and pharmacogenomics are not part of standard management (surgery limited to debridement/amputation of necrotic tissue). No ITT-specific clinical-trial experimental agents (NCT IDs) were identified.

**Treatment outcomes / adverse events:** Response is rapid and near-universal with timely doxycycline [PMID: 30150470](https://pubmed.ncbi.nlm.nih.gov/30150470/). Doxycycline is generally well tolerated; historic concerns about pediatric dental staining are outweighed by benefit and short courses are considered safe per Indian pediatric guidance [PMID: 28361787](https://pubmed.ncbi.nlm.nih.gov/28361787/).

---

## Section 13 — Prevention

**No licensed human vaccine exists.** Prevention is based on **personal protective measures against tick bites** and **tick control on dogs and in the environment** [PMID: 15109588](https://pubmed.ncbi.nlm.nih.gov/15109588/).

- **Primary prevention (behavioral/public health):** tick repellents, permethrin-treated clothing, protective clothing (e.g., rolling up long sleeves), and frequent tick checks [PMID: 33549976](https://pubmed.ncbi.nlm.nih.gov/33549976/); [PMID: 12653142](https://pubmed.ncbi.nlm.nih.gov/12653142/). Reducing tick burden — "finding >10 ticks on the body" was the primary risk factor — is central [PMID: 12653142](https://pubmed.ncbi.nlm.nih.gov/12653142/).
- **One Health / veterinary control:** controlling *R. sanguineus* on dogs and in the peridomestic environment reduces the reservoir/vector burden [PMID: 40871278](https://pubmed.ncbi.nlm.nih.gov/40871278/).
- **Chemoprophylaxis:** doxycycline use was protective against seropositivity in an exposed cohort [PMID: 12653142](https://pubmed.ncbi.nlm.nih.gov/12653142/), though routine prophylaxis is not standard.
- **Secondary prevention:** clinician awareness and early empirical doxycycline prevent progression to severe disease [PMID: 42390463](https://pubmed.ncbi.nlm.nih.gov/42390463/); [PMID: 28361787](https://pubmed.ncbi.nlm.nih.gov/28361787/).
- **Not applicable:** immunization, genetic/carrier screening, and genetic counseling.

Notably, "most infected travellers cannot recall a preceding tick bite," underscoring the limits of avoidance alone and the importance of clinical vigilance [PMID: 15109588](https://pubmed.ncbi.nlm.nih.gov/15109588/).

---

## Section 14 — Other Species / Natural Disease

**Taxonomy of affected/involved species:** Humans (*Homo sapiens*) are incidental hosts. The vector/reservoir is the brown dog tick ***Rhipicephalus sanguineus***; ITTR has also been detected in ***Rhipicephalus turanicus*** [PMID: 41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/). **Dogs** (*Canis lupus familiaris*) are key reservoir/amplifying hosts within a One Health transmission ecology [PMID: 40871278](https://pubmed.ncbi.nlm.nih.gov/40871278/).

**Zoonosis / cross-species susceptibility:** ITT/MSF is a **tick-borne zoonosis** [PMID: 32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/). SFG rickettsiae infect multiple mammals: in a Colombian focus, incident SFG seroconversion reached **32.3% in equines vs 6.23% in humans**, indicating shared cross-species exposure [PMID: 30379820](https://pubmed.ncbi.nlm.nih.gov/30379820/). Ticks serve as both vector and reservoir via transovarial/transstadial maintenance [PMID: 40871278](https://pubmed.ncbi.nlm.nih.gov/40871278/).

**Comparative biology:** Because the disease depends on conserved rickettsial invasion machinery (Sca2, RickA) and host actin/Arp2/3 pathways present across mammals, mechanisms are broadly conserved across host species [PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/); [PMID: 22188208](https://pubmed.ncbi.nlm.nih.gov/22188208/). *(No VBO breed-specific susceptibility or OMIA natural-disease entry is established for ITT specifically.)*

---

## Section 15 — Model Organisms

**Primary in vivo model — C3H/HeN mouse.** IV inoculation of *R. conorii* (Malish 7) establishes disseminated endothelial infection by day 1; a high dose causes death on days 5–6 with **vascular-injury-based meningoencephalitis and interstitial pneumonia**, while a low dose recovers by day 10 with lymphohistiocytic perivasculitis, and Kupffer cell/hepatocyte infection forms transient hepatic granulomas. It is described as "the best available model for rickettsial disease with endothelial infection and injury" [PMID: 7511715](https://pubmed.ncbi.nlm.nih.gov/7511715/).

**Phenotype recapitulation:** The model reproduces the **key human features** — endothelial-target vasculitis, meningoencephalitis, interstitial pneumonia, hepatic involvement, and dose-dependent severity — making it well-suited to studying pathogenesis and immunity [PMID: 7511715](https://pubmed.ncbi.nlm.nih.gov/7511715/).

**Immunological/mechanistic applications:** The murine model established that **CD8 T lymphocytes are required to clear rickettsiae from endothelium**; CD8 depletion causes lethal/persistent infection, and adoptive transfer of immune CD4 or CD8 cells is protective [PMID: 9164951](https://pubmed.ncbi.nlm.nih.gov/9164951/).

**In vitro models:** Human endothelial cell invasion assays (defining Sca2 mammalian-association and actin-nucleation domains) [PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/) and RNAi screens in mammalian cells (SFG *R. parkeri*) mapping the Arp2/3–WAVE–Rho invasion pathway [PMID: 22188208](https://pubmed.ncbi.nlm.nih.gov/22188208/).

**Limitations:** Most experimental data use the Malish (MSF) strain rather than the *indica* subspecies specifically; murine dosing/route (IV) differs from natural tick inoculation; and models may not fully capture human age-dependent "malignant" severity.

---

## Mechanistic Model / Interpretation

```
 Infected Rhipicephalus tick bite
              │ inoculates R. conorii subsp. indica into dermis
              ▼
     Local infection (eschar / tache noire)
              │ Sca2 + OmpA/OmpB adhesion
              ▼
   Adhesion & invasion of VASCULAR ENDOTHELIUM
              │ host Arp2/3 + WAVE2 + Rac GTPases nucleate actin
              ▼
   Cytosolic replication + actin-based motility (Sca2, RickA)
              │ cell-to-cell spread → dissemination
              ▼
   ENDOTHELIAL INFLAMMATION & INJURY (VASCULITIS)
        ├── TXA2-dependent platelet activation + thrombin → microthrombi
        ├── ↑ endothelin-1, ↑ permeability → edema / rash / MOF
        └── endothelial membrane damage → antiphospholipid Abs (inferred)
              ▼
  Systemic small-vessel disease: skin, brain, lung, liver, kidney, eye, marrow
              │
   Host defense: CD8 T cells clear endothelial rickettsiae ──► recovery
   (failure / delay / age >65 ──► severe "malignant" form ──► death)
              ▲
   Doxycycline (halts replication) short-circuits the chain → rapid recovery
```

The model is internally consistent: a single upstream lesion — **endothelial infection** — explains the entire downstream phenotype (rash, coagulopathy, multi-organ vasculitis), the therapeutic target (intracellular bacterium → intracellular-active doxycycline), the immune requirement (CD8 clearance of infected endothelium), and prevention (block the tick bite that initiates the chain).

---

## Evidence Base

| PMID | Study type | Contribution |
|---|---|---|
| [22628514](https://pubmed.ncbi.nlm.nih.gov/22628514/) | Genome sequence | Identifies *R. conorii* subsp. *indica* strain ITTR as the ITT agent |
| [15766388](https://pubmed.ncbi.nlm.nih.gov/15766388/) | MLST taxonomy | Defines four *R. conorii* subspecies; ITTR genotype |
| [41650674](https://pubmed.ncbi.nlm.nih.gov/41650674/) | Case report | ITTR in human + tick; core clinical/lab phenotype |
| [34345128](https://pubmed.ncbi.nlm.nih.gov/34345128/) | Review | Endothelial vasculitis mechanism; doxycycline therapy |
| [8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/) | Human study | TXA2-dependent platelet/coagulation activation in vivo |
| [8679900](https://pubmed.ncbi.nlm.nih.gov/8679900/) | Case study | Antiphospholipid antibodies from endothelial damage (inferred role) |
| [15120155](https://pubmed.ncbi.nlm.nih.gov/15120155/) | Animal/tissue | Oxidative-stress enzyme modulation; endothelial localization |
| [22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/) | In vitro | Sca2 mediates adhesion, invasion, actin motility |
| [22188208](https://pubmed.ncbi.nlm.nih.gov/22188208/) | RNAi screen | Arp2/3–WAVE–Rho invasion pathway |
| [7511715](https://pubmed.ncbi.nlm.nih.gov/7511715/) | Mouse model | C3H/HeN endothelial-target rickettsiosis model |
| [9164951](https://pubmed.ncbi.nlm.nih.gov/9164951/) | Mouse model | CD8 T cells required for endothelial clearance |
| [16481486](https://pubmed.ncbi.nlm.nih.gov/16481486/) | Genomics | Reductive genome; host-ATP dependence; RickA |
| [19379498](https://pubmed.ncbi.nlm.nih.gov/19379498/) | Genomics | Virulence linked to genome reduction |
| [12832625](https://pubmed.ncbi.nlm.nih.gov/12832625/) | Genomics | Orphan genes reflect ongoing genome decay |
| [32997473](https://pubmed.ncbi.nlm.nih.gov/32997473/) | Cohort (n=549) | Incidence 9.44/100,000; age-dependent malignant forms |
| [30972588](https://pubmed.ncbi.nlm.nih.gov/30972588/) | Cohort | Severe MSF 26.4% vs 10.5% in elderly (p=0.002) |
| [30150470](https://pubmed.ncbi.nlm.nih.gov/30150470/) | Prospective cohort | Single-day doxycycline; defervescence 2.55±1.14 d |
| [41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/) | Pediatric cohort | Fever/rash 100%, eschar 6%, thrombocytopenia 56% |
| [42390463](https://pubmed.ncbi.nlm.nih.gov/42390463/) | Review | Diagnostic modalities; PCR advantage; doxycycline |
| [40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/) | Case series | Palm/sole rash, eschar; gltA/ompA confirmation |
| [12653142](https://pubmed.ncbi.nlm.nih.gov/12653142/) | Epidemiology | >10 ticks = risk; doxycycline/sleeves protective |
| [15109588](https://pubmed.ncbi.nlm.nih.gov/15109588/) | Review | Prevention via personal protection |
| [40871278](https://pubmed.ncbi.nlm.nih.gov/40871278/) | One Health surveillance | Dogs/companion animals in transmission ecology |
| [30379820](https://pubmed.ncbi.nlm.nih.gov/30379820/) | Epidemiology | Cross-species (equine 32.3%) SFG exposure |
| [30451192](https://pubmed.ncbi.nlm.nih.gov/30451192/) | Case report | Ocular retinitis; ITT within India's SFG |
| [28361787](https://pubmed.ncbi.nlm.nih.gov/28361787/) | Guidelines | IAP pediatric rickettsial guidance; doxycycline |
| [40693676](https://pubmed.ncbi.nlm.nih.gov/40693676/) | Case report | HLH complication (H-score 224) |
| [20797742](https://pubmed.ncbi.nlm.nih.gov/20797742/) | Case report | Infant meningoencephalitis with sequelae |
| [35263931](https://pubmed.ncbi.nlm.nih.gov/35263931/) | Case report | Meningoencephalitis MRI findings |
| [29169658](https://pubmed.ncbi.nlm.nih.gov/29169658/) | Case series | Symmetric peripheral gangrene / amputation |
| [28491211](https://pubmed.ncbi.nlm.nih.gov/28491211/) | Case report | Cerebral infarction |
| [28292166](https://pubmed.ncbi.nlm.nih.gov/28292166/) | Case report | Fatal late-diagnosed multivisceral failure |
| [32998655](https://pubmed.ncbi.nlm.nih.gov/32998655/) | Case series | Purpura fulminans; 18.2% mortality |
| [29331008](https://pubmed.ncbi.nlm.nih.gov/29331008/) | Case report | Atypical late (day 8) rash |
| [33549976](https://pubmed.ncbi.nlm.nih.gov/33549976/) | Review | Tick-bite personal protection measures |
| [30522428](https://pubmed.ncbi.nlm.nih.gov/30522428/) | Case report | PCR-positive, serology-negative acute phase; seroconversion |
| [42658412](https://pubmed.ncbi.nlm.nih.gov/42658412/) | Case report | Diagnostic challenges; differentials (measles, dengue) |

**Consistency:** No contradictory findings emerged. Case reports, cohorts, guidelines, genomics, and experimental models all converge on a single coherent picture: an endothelium-tropic intracellular bacterium causing doxycycline-responsive systemic vasculitis.

---

## Limitations and Knowledge Gaps

1. **Subspecies-specific data are sparse.** Most mechanistic (Sca2, Arp2/3, CD8) and clinical-cohort evidence derives from the **Malish/MSF strain** or the broader *R. conorii*/SFG group, not the *indica* subspecies specifically. Subspecies are >98% identical and clinically indistinguishable, so extrapolation is reasonable but not formally validated for *indica*.
2. **No ITT-specific epidemiology.** Incidence/prevalence figures (e.g., 9.44/100,000) come from Mediterranean/MSF cohorts; India-specific ITT burden is under-characterized and likely underreported [PMID: 30451192](https://pubmed.ncbi.nlm.nih.gov/30451192/).
3. **No host genomic/omics disease signatures** (transcriptomics, proteomics, metabolomics, epigenomics) specific to ITT beyond antioxidant-enzyme modulation.
4. **Mechanism of severity is incomplete.** Why some patients (especially elderly) develop "malignant" disease is not molecularly defined; the role of antiphospholipid antibodies in microthrombosis remains inferred, not proven [PMID: 8679900](https://pubmed.ncbi.nlm.nih.gov/8679900/).
5. **No human vaccine or genetic/pharmacogenomic component**, so several template sections are intrinsically not applicable.
6. **Diagnostic timing gap:** IFA is retrospective and PCR access is limited in endemic settings, leading to diagnostic delay and preventable severe outcomes [PMID: 42390463](https://pubmed.ncbi.nlm.nih.gov/42390463/); [PMID: 28292166](https://pubmed.ncbi.nlm.nih.gov/28292166/).

---

## Proposed Follow-up Experiments / Actions

1. **Subspecies-specific characterization:** Confirm Sca2/OmpA-mediated invasion kinetics and virulence of *R. conorii* subsp. *indica* (ITTR) in human endothelial cells and the C3H/HeN mouse, benchmarked against Malish, to validate mechanistic extrapolations.
2. **India-focused surveillance:** Establish PCR-based (gltA/ompA) surveillance in Indian febrile-illness cohorts to quantify true ITT incidence, seasonal/geographic distribution, and severe-disease frequency.
3. **Host response omics:** Perform transcriptomic/proteomic profiling of endothelial and PBMC responses in acute ITT to identify prognostic biomarkers distinguishing benign from malignant courses.
4. **Severity determinants:** Test whether antiphospholipid-antibody titers, endothelin-1, and coagulation markers (prothrombin F1+2) predict progression to multi-organ failure — moving Branch A/C from inferred to demonstrated.
5. **Point-of-care diagnostics:** Develop and validate a rapid acute-phase molecular or antigen test to close the IFA seroconversion gap and enable earlier doxycycline in endemic, resource-limited settings.
6. **One Health vector control trials:** Evaluate whether canine *R. sanguineus* control (acaricides, environmental management) measurably reduces human ITT incidence in endemic foci.

---

*Report compiled from 12 confirmed findings and 47 reviewed papers across 5 investigation iterations. Evidence types span human clinical (case reports, case series, cohorts, guidelines), model organism (C3H/HeN mouse), in vitro (endothelial invasion, RNAi screens), and computational/comparative genomics.*


## Artifacts

- [OpenScientist final report](Indian_Tick_Typhus-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Indian_Tick_Typhus-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 37 |
| On topic | 22 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:12832625` (4 mentions) - Birth and death of orphan genes in Rickettsia.
  - shared terms: conorii

Weighed against this report's own most characteristic terms: `disease`, `tick`, `conorii`, `human`, `severe`, `acute`, `host`, `sfg`, `fever`, `indica`, `msf`, `doxycycline`, `itt`, `rash`, `endothelial`, `cell`, `cohort`, `clinical`, `meningoencephalitis`, `sca2`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 9 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0000229` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Indian tick typhus**
- `HP:0200041` (1 mention) - the report calls it "cutaneous ulcer/eschar"; HP calls it **Skin erosion**
- `UBERON:0002097` (1 mention) - the report calls it "Rash, eschar/*tache noire"; UBERON calls it **skin of body**
- `UBERON:0000955` (1 mention) - the report calls it "Meningoencephalitis, cerebral infarction"; UBERON calls it **brain**
- `UBERON:0002048` (1 mention) - the report calls it "Interstitial pneumonia/infiltrates"; UBERON calls it **lung**
- `UBERON:0002107` (1 mention) - the report calls it "Transaminitis, hepatic granulomas (Kupffer cell/hepatocyte infection)"; UBERON calls it **liver**
- `UBERON:0002113` (1 mention) - the report calls it "Proteinuria, acute tubular necrosis/renal failure"; UBERON calls it **kidney**
- `UBERON:0000178` (1 mention) - the report calls it "Thrombocytopenia, HLH"; UBERON calls it **blood**