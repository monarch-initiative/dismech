---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T08:22:53.435688'
end_time: '2026-09-25T08:43:10.150901'
duration_seconds: 1216.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pneumonic Plague
  mondo_id: MONDO:0001024
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 38
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 24
  quotes_valid: 24
  relevance_assessed: 38
  on_topic: 25
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 35
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 12
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0011446
    reported_labels:
    - Abnormal consciousness
    ontology_label: Abnormality of mental function
  - term_id: HP:0005521
    reported_labels:
    - DIC
    ontology_label: Disseminated intravascular coagulation
  - term_id: UBERON:0002106
    reported_labels:
    - spleen
    - Secondary organ involvement:** **spleen
    ontology_label: spleen
  - term_id: NCIT:C2159
    reported_labels:
    - Fluoroquinolones:** ciprofloxacin
    ontology_label: Protein Phosphatase Inhibitor
  - term_id: NCIT:C692
    reported_labels:
    - Tetracyclines:** doxycycline
    ontology_label: Nimodipine
  - term_id: NCIT:C375
    reported_labels:
    - Chloramphenicol
    ontology_label: Ciprofloxacin
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pneumonic_Plague-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pneumonic_Plague-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pneumonic Plague
- **MONDO ID:** MONDO:0001024 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pneumonic Plague** covering all of the
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

# Pneumonic Plague (MONDO:0001024): A Comprehensive Disease Characterization

*Autonomous discovery report — 5 iterations, 14 confirmed findings, 53 papers reviewed*

---

## Summary

**Pneumonic plague is a rapidly progressive, near-uniformly fatal infection of the lung caused by the Gram-negative bacterium *Yersinia pestis* (NCBITaxon:632).** It is the most dangerous of the three clinical forms of plague (bubonic, septicemic, pneumonic) because it is the only form that is directly transmissible from person to person by respiratory droplets, and because — untreated — its case-fatality approaches 100% within 3–7 days. Two routes produce it: **primary pneumonic plague**, from inhaling infectious aerosols, and **secondary pneumonic plague**, when bubonic or septicemic infection seeds the lungs hematogenously. The disease is fundamentally an infectious, not a genetic, disorder; there are no causal human genes, and the "genetic" story of the disease lies almost entirely in the pathogen's plasmid- and chromosome-encoded virulence arsenal.

The mechanistic core of pneumonic plague is a **stealth-then-storm immunopathology**. In the first 24–36 hours, *Y. pestis* deploys a coordinated set of virulence factors — the **Pla** plasminogen-activating protease, the **F1 capsular antigen**, and the **type III secretion system (T3SS)** with its Yop effectors and the **LcrV (V) antigen** — to actively suppress innate immunity. LcrV signals through **TLR2/CD14 to induce IL-10**, dampening TNFα and IFNγ; the T3SS blocks leukocyte synthesis of the chemoattractant **leukotriene B4 (LTB4)**; and F1 plus the T3SS render the organism resistant to phagocytosis. This anti-inflammatory window lets bacteria replicate freely in the airways. By ~48 hours the disease flips to an **overwhelming pro-inflammatory state**, producing a purulent, multifocal, necrotizing exudative bronchopneumonia and death by day 3 in the mouse model that faithfully mirrors human disease.

**Clinically, the outlook is entirely dictated by the speed of antibiotic therapy.** US surveillance across 1942–2018 showed mortality of 9% with high-efficacy antimicrobials (aminoglycosides, tetracyclines, fluoroquinolones) versus 51% with only limited-efficacy therapy; a 2020–2024 Madagascar randomized trial established that **oral ciprofloxacin monotherapy is noninferior** to aminoglycoside-ciprofloxacin combination. The disease is a **flea-borne rodent zoonosis** maintained in sylvatic foci, with Madagascar accounting for ~75% of global cases; the 2017 urban Madagascar epidemic (78% pneumonic) demonstrated the epidemic potential of person-to-person spread. There is **no licensed vaccine**, though F1/LcrV-based candidates (subunit, adenoviral-vectored, mRNA-LNP, nanolipoprotein) confer 90–100% protection in animal models. Early antibiotics and post-exposure prophylaxis (doxycycline or ciprofloxacin for 7 days) remain the mainstays of control.

---

## Disease Information

**Overview.** Pneumonic plague is a fulminant bacterial pneumonia caused by *Yersinia pestis*, a non-motile, Gram-negative coccobacillus of the family *Yersiniaceae*. It is one of three overlapping clinical presentations of plague. Pneumonic plague is distinguished by (i) its respiratory localization, (ii) its capacity for direct human-to-human aerosol transmission, and (iii) the highest case-fatality of the three forms.

**Key identifiers.**
- **MONDO:** MONDO:0001024 (pneumonic plague)
- **Causative organism:** *Yersinia pestis* — **NCBITaxon:632**
- **ICD-10:** A20.2 (pneumonic plague); parent A20 (plague)
- **ICD-11:** 1B93.1 (pneumonic plague)
- **MeSH:** D010930 ("Plague"); pneumonic form indexed under plague
- **SNOMED CT:** Pneumonic plague (disorder)

**Synonyms / alternative names.** Pulmonary plague; plague pneumonia; lung plague; "the Black Death" (historical, non-specific); pest (older usage). Primary vs. secondary pneumonic plague denote route of lung involvement.

**Data source type.** This report is derived from **aggregated disease-level resources** — peer-reviewed primary literature, outbreak epidemiology (WHO/Madagascar/CDC), and controlled animal-model studies — rather than individual EHR patient data.

---

## Etiology

**Primary cause — infectious.** The sole cause of pneumonic plague is infection with *Yersinia pestis*. This is not a genetic or multifactorial disease; there is no human causal gene. Primary pneumonic plague follows inhalation of infectious respiratory aerosols (from an infected human or, rarely, an animal such as a domestic cat); secondary pneumonic plague arises when bubonic or septicemic *Y. pestis* seeds the lungs.

**Risk factors (environmental / behavioral).**
- **Exposure to sylvatic reservoirs and vectors** — living or working in endemic rural foci with rodent–flea cycles. *Y. pestis* is "primarily a rodent-associated, flea-borne zoonosis maintained in sylvatic foci throughout western North America" ([PMID: 23590319](https://pubmed.ncbi.nlm.nih.gov/23590319/)).
- **Close contact with a pneumonic plague case** — "Human-to-human transmission of the pathogen occurs primarily through aerosol droplets" ([PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)), so household members and healthcare workers are at elevated risk.
- **Handling infected animals**, including hunting/skinning rodents and lagomorphs, and exposure to sick domestic cats.
- **Crowding and urbanization**, which amplified the 2017 Madagascar epidemic (burial practices, movement of people, overcrowding) ([PMID: 30632956](https://pubmed.ncbi.nlm.nih.gov/30632956/)).
- **Pregnancy** as a state of increased infection severity requiring special management ([PMID: 32435804](https://pubmed.ncbi.nlm.nih.gov/32435804/)).
- **Deliberate release (bioterrorism)** — aerosolized *Y. pestis* is a Tier-1 select agent.

**Genetic risk / protective factors (human host).** No validated human susceptibility or protective loci are established for pneumonic plague. One speculative, unproven hypothesis in the recent literature considers whether immune-tuning variants such as **TYK2 P1104A** could influence responses to pneumonic plague, but this is explicitly framed as speculation ([PMID: 42382739](https://pubmed.ncbi.nlm.nih.gov/42382739/)). **This should be treated as a knowledge gap, not an established fact.**

**Gene–environment interactions.** Not applicable in the classical host-genetics sense. The operative "gene–environment" axis is the **pathogen's genome × host environment**: temperature-regulated virulence gene expression (F1 and T3SS are induced at 37°C, the mammalian host temperature) is the key switch that converts a flea-adapted organism into a mammalian pathogen.

---

## Phenotypes

Pneumonic plague presents as an acute, fulminant febrile respiratory illness. Onset is **adult and all-age** (no age restriction), **acute**, and **severe/progressive** in essentially all untreated patients. Frequencies below are qualitative/clinical-series–based.

| Phenotype | Type | HPO suggestion | Characteristics |
|---|---|---|---|
| High fever, chills | Symptom/sign | HP:0001945 (Fever) | Near-universal; abrupt onset |
| Cough | Symptom | HP:0012735 (Cough) | Common; progresses rapidly |
| Hemoptysis / bloody sputum | Sign | HP:0002105 (Hemoptysis) | Classic; blood-tinged/watery sputum |
| Dyspnea | Symptom | HP:0002094 (Dyspnea) | Rapidly worsening respiratory distress |
| Chest pain | Symptom | HP:0100749 (Chest pain) | Frequent |
| Pneumonia / bronchopneumonia | Clinical sign | HP:0002090 (Pneumonia) | Purulent, multifocal, exudative |
| Headache, malaise | Symptom | HP:0002315 (Headache) | Early prodrome |
| Sepsis / shock | Sign | HP:0100806 (Sepsis) | Terminal, with multi-organ failure |
| Altered consciousness | Sign | HP:0011446 (Abnormal consciousness) | Late/terminal |
| Leukocytosis | Lab abnormality | HP:0001974 (Leukocytosis) | With neutrophilia |
| Disseminated intravascular coagulation | Lab/clinical | HP:0005521 (DIC) | Terminal complication |

**Severity and progression.** Uniformly **severe and progressive**. The classic course runs from a nonspecific febrile prodrome to fulminant pneumonia with respiratory failure and death within 3–7 days if untreated. The mouse intranasal model produces "a purulent multifocal severe exudative bronchopneumonia that closely resembles the disease observed in humans" ([PMID: 16306265](https://pubmed.ncbi.nlm.nih.gov/16306265/)).

**Atypical presentations.** During the 2017 Madagascar urban outbreak, atypical features (prolonged illness, prominent upper-respiratory symptoms) were reported, complicating recognition ([PMID: 32274983](https://pubmed.ncbi.nlm.nih.gov/32274983/)).

**Quality-of-life impact.** As an acute, life-threatening illness measured in days, pneumonic plague's "QoL" burden is dominated by acute mortality and, in survivors treated early, generally full recovery. Chronic disability is not a characteristic feature; there are no established EQ-5D/SF-36 datasets specific to plague survivors (knowledge gap).

---

## Genetic / Molecular Information

**Human genetics: not applicable.** Pneumonic plague has **no causal human genes, no pathogenic germline/somatic variants, no modifier genes, no chromosomal abnormalities, and no disease-defining epigenetic signature** in the host. It is an acquired infectious disease. Sections that would apply to a Mendelian disorder (ACMG variant classification, gnomAD allele frequencies, COSMIC somatic mutations, karyotyping) are **not applicable**.

**Pathogen genetics (the operative "molecular information").** Virulence is encoded across the *Y. pestis* chromosome and three plasmids:

| Locus / gene | Location | Product & role |
|---|---|---|
| **pla** | pPCP1 / pPst (~9.5 kb) | Plasminogen-activator protease; **essential for primary pneumonic plague** |
| **caf1** (+ *caf1M/caf1A*) | pFra / pMT1 (~100 kb) | F1 capsular antigen (Caf1, 15.5 kDa) via chaperone–usher assembly; antiphagocytic |
| ***ymt*** | pFra / pMT1 | Murine toxin / phospholipase D; flea-gut survival |
| **lcrV, yop genes, ysc** | pCD1 / pYV (~70 kb) | T3SS injectisome, LcrV (V antigen), Yop effectors |
| **hms** locus (*hmsHFRS*, *hmsT/P*) | Chromosome (pgm/pigmentation) | Biofilm; flea proventricular blockage |
| **pgm** locus / *yop-ysc* | Chromosome / pCD1 | Upregulated in vivo during lung infection |

- Pla is encoded on the pPCP1 plasmid and is "essential for Y. pestis to cause primary pneumonic plague" ([PMID: 17255510](https://pubmed.ncbi.nlm.nih.gov/17255510/)).
- "F1 is encoded by the caf1 gene located on the large 100-kb pFra plasmid, which is unique to Y. pestis" ([PMID: 11854232](https://pubmed.ncbi.nlm.nih.gov/11854232/)).
- In vivo microarray during lung infection showed upregulation of the *yop-ysc* T3SS and the chromosomal *pgm* locus ([PMID: 16306265](https://pubmed.ncbi.nlm.nih.gov/16306265/)).

---

## Environmental Information

- **Environmental factors:** *Y. pestis* persists in sylvatic rodent–flea cycles; interannual variation in US human cases is linked to **precipitation and temperature** ([PMID: 39808829](https://pubmed.ncbi.nlm.nih.gov/39808829/)). Temperature governs the vector-to-host switch (37°C induces F1/T3SS).
- **Lifestyle factors:** hunting/skinning wild rodents/lagomorphs, rural residence in endemic foci, and contact with sick cats. Smoking/diet/alcohol are not established plague risk factors.
- **Infectious agent:** *Yersinia pestis* — **NCBITaxon:632**. Vectors include *Oropsylla montana* (southwestern US) and *Xenopsylla cheopis* (Oriental rat flea, elsewhere) ([PMID: 23590319](https://pubmed.ncbi.nlm.nih.gov/23590319/)).

---

## Mechanism / Pathophysiology

### Ordered causal chain (initiating event → clinical manifestation)

1. **Inhalation of *Y. pestis* aerosol** (primary) — *or* hematogenous seeding of the lung from bubonic/septicemic infection (secondary) — **delivers bacteria to the alveolar space.** *[established]*
2. **Shift to 37°C host temperature induces expression** of F1 capsule and the T3SS/LcrV system. *[established]*
3. **The T3SS injects Yop effectors into host leukocytes**, which normally recognize the T3SS and respond by synthesizing **leukotriene B4 (LTB4)**; Yop effectors **actively block LTB4 synthesis**, **leading to** failure of neutrophil chemoattraction. *[established — PMID 38271464]*
4. **Secreted LcrV signals via TLR2/CD14 to induce IL-10**, which **results in** suppression of pro-inflammatory TNFα and IFNγ. *[established — PMID 12391013, 11801671]*
5. **F1 capsule + T3SS together confer resistance to phagocytosis**, **allowing** extracellular bacterial survival and replication. *[established — PMID 11854232]*
6. **Pla protease remodels the host fibrinolytic/hemostatic environment in the airway**, **enabling** rapid bacterial replication and fulminant pneumonia; without Pla, inflammation aborts and lung repair activates. *[established — PMID 17255510]*
7. Steps 3–6 jointly produce an **early anti-inflammatory "stealth" window (0–36 h)** with unchecked bacterial proliferation. *[established — PMID 16306265]*
8. Rising bacterial burden **crosses a threshold that flips the response to a highly pro-inflammatory state (~48 h)**, **causing** massive neutrophil influx, purulent multifocal exudative bronchopneumonia, and alveolar destruction. *[established — PMID 16306265]*
9. **Bacteremic dissemination → septicemia, endotoxin/cytokine-driven shock, DIC, and multi-organ failure**, **resulting in** death by ~day 3 (model) / 3–7 days (human) if untreated. *[established]*

```
 Aerosol inhalation
        │  (37°C induces F1, T3SS/LcrV)
        ▼
 ┌─────────── EARLY "STEALTH" PHASE (0–36 h) ───────────┐
 │  T3SS/Yop ──┤ blocks LTB4  ──► no neutrophil recruit  │
 │  LcrV ─TLR2/CD14─► IL-10 ──► ↓TNFα ↓IFNγ              │
 │  F1 + T3SS ──► antiphagocytic ──► extracellular growth│
 │  Pla ──► fibrinolysis, rapid airway replication       │
 └───────────────────────────┬──────────────────────────┘
                              │  bacterial burden threshold
                              ▼
 ┌────────── LATE "STORM" PHASE (~48 h → death) ─────────┐
 │  Overwhelming pro-inflammatory response               │
 │  Purulent multifocal exudative bronchopneumonia       │
 │  Dissemination ► septicemia ► shock ► DIC ► MOF ► death│
 └───────────────────────────────────────────────────────┘
```

### Detail by category

- **Molecular pathways / immune signaling:** TLR2/CD14 → IL-10 immunosuppressive axis (LcrV); LTB4 biosynthesis (5-lipoxygenase pathway) suppression; TNFα and IFNγ (Th1) axes suppressed early and required for vaccine-mediated protection. GO suggestions: **GO:0032496** (response to LPS), **GO:0032613** (IL-10 production), **GO:0019370** (leukotriene biosynthesis), **GO:0050830** (defense response to Gram-negative bacterium), **GO:0030593** (neutrophil chemotaxis).
- **Cellular processes:** inhibition of phagocytosis, suppression of neutrophil recruitment/chemotaxis, macrophage cytokine reprogramming, and — late — necrotizing inflammation. Early intracellular survival in macrophages seeds infection.
- **Protein dysfunction (pathogen effectors, not host):** Pla (omptin protease) cleaves plasminogen→plasmin and host substrates; Yop effectors (YopE, YopH, YopJ/P, YopM, YopT) disrupt host cytoskeleton, signaling, and cytokines; LcrV caps the T3SS translocon and immunomodulates. UniProt: Pla (P17811), LcrV (LcrV family).
- **Immune involvement:** the disease is defined by **immune evasion followed by immunopathology** — not autoimmunity or primary immunodeficiency. IL-10 is the central immunosuppressive node; TNFα/IFNγ are protective when present.
- **Tissue damage mechanisms:** purulent exudative inflammation, alveolar necrosis, vascular involvement, and coagulopathy (DIC). A recent model reports vascular-associated bacterial burden and neuroinflammatory transcriptional responses in the CNS after aerosol exposure ([PMID: 42422735](https://pubmed.ncbi.nlm.nih.gov/42422735/)).
- **Cell types (CL suggestions):** alveolar macrophage (**CL:0000583**), neutrophil (**CL:0000775**), monocyte/macrophage (**CL:0000235**), type II pneumocyte (**CL:0002063**), dendritic cell (**CL:0000451**).

---

## Anatomical Structures Affected

- **Primary organ:** **lung** — UBERON:0002048. Specifically alveoli (UBERON:0002299), bronchi/bronchioles, and lung parenchyma; disease is typically **bilateral/multifocal**.
- **Secondary organ involvement:** **spleen** (UBERON:0002106) and **liver** (UBERON:0002107) via dissemination (bacterial load tracked there in models), **blood/vasculature** (septicemia), lymph nodes, and — reported experimentally — **CNS** ([PMID: 42422735](https://pubmed.ncbi.nlm.nih.gov/42422735/)).
- **Body systems:** **respiratory** (primary), **cardiovascular/hematologic** (sepsis, DIC), **immune/lymphatic**.
- **Tissue level:** respiratory epithelium and alveolar–capillary membrane; inflammatory exudate rich in neutrophils and fibrin.
- **Cell populations:** alveolar macrophages (CL:0000583), neutrophils (CL:0000775), pneumocytes (CL:0002063).
- **Subcellular:** host plasma membrane (T3SS translocation pore), cytosol (Yop effector targets). GO cellular component: **GO:0005886** (plasma membrane), pathogen **GO:0030257** (type III protein secretion system complex).
- **Lateralization:** typically **bilateral**, multifocal.

---

## Temporal Development

- **Onset:** **acute**; all ages. Incubation typically **1–6 days** after aerosol exposure (often 2–4 days). Rapid febrile prodrome.
- **Progression:** **rapid and progressive.** Model kinetics: anti-inflammatory state 0–36 h → pro-inflammatory state by 48 h → death by ~72 h ([PMID: 16306265](https://pubmed.ncbi.nlm.nih.gov/16306265/)). Human untreated course: death within **3–7 days** ([PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)).
- **Stages:** (1) incubation, (2) febrile prodrome, (3) fulminant pneumonia with hemoptysis/dyspnea, (4) respiratory failure + septic shock/DIC.
- **Disease course pattern:** monophasic, fulminant, self-limited only by death or by recovery with early antibiotics; not relapsing-remitting or chronic.
- **Critical period for intervention:** the **first ~24 hours of symptoms** is the decisive window — antibiotics started later have markedly reduced efficacy given the rapid trajectory.

---

## Inheritance and Population (Epidemiology)

- **Inheritance:** **not applicable** — infectious disease, not heritable. No penetrance/expressivity/anticipation/founder effects/carrier frequency apply to the host.
- **Global burden & geography:** Plague is endemic on three continents. **Madagascar accounts for ~75% of global cases reported to WHO, with an annual incidence of 200–700 suspected cases (mainly bubonic)** ([PMID: 30930106](https://pubmed.ncbi.nlm.nih.gov/30930106/)). In the US it is "a rare, potentially fatal flea-borne zoonosis endemic in the western United States" ([PMID: 39808829](https://pubmed.ncbi.nlm.nih.gov/39808829/)).
- **2017 Madagascar urban epidemic (Aug–Nov 2017):** 2414 suspected cases, of which **1878 (78%) pneumonic**, 395 (16%) bubonic, 1 septicemic, 140 unspecified ([PMID: 30930106](https://pubmed.ncbi.nlm.nih.gov/30930106/)). Genomic analysis showed **>20 independent emergences** from rural reservoirs into urban areas ([PMID: 38270131](https://pubmed.ncbi.nlm.nih.gov/38270131/)).
- **Sex / age:** no strong intrinsic sex predilection; exposure-driven. Pregnant women may have increased severity ([PMID: 32435804](https://pubmed.ncbi.nlm.nih.gov/32435804/)).
- **Seasonality:** linked to weather and vector/rodent dynamics ([PMID: 39808829](https://pubmed.ncbi.nlm.nih.gov/39808829/)); the 2017 epidemic notably began before the usual season ([PMID: 30632956](https://pubmed.ncbi.nlm.nih.gov/30632956/)).

---

## Diagnostics

**Clinical/microbiological.** Definitive diagnosis rests on isolating *Y. pestis* or detecting its antigens/DNA from sputum, blood, or bronchoalveolar specimens.

- **Rapid diagnostic test (F1 antigen lateral-flow):** detects F1 antigen "as low as 0.5 ng/mL in up to 15 min... shelf life of 21 days at 60 degrees C. Its sensitivity and specificity were both 100%" ([PMID: 12547544](https://pubmed.ncbi.nlm.nih.gov/12547544/)); positive/negative predictive values 90.6%/86.7%, detecting substantially more positives than bacteriology or ELISA. This is the key **bedside** tool in endemic settings.
- **Culture:** blood, sputum — remains a gold-standard confirmation.
- **PCR / NAAT:** *pla* and *caf1* targets; the field has advanced from conventional PCR to real-time PCR, isothermal LAMP/RPA, ddPCR, and CRISPR-based platforms ([PMID: 42413880](https://pubmed.ncbi.nlm.nih.gov/42413880/)).
- **Serology:** anti-F1 antibody (retrospective/confirmatory).
- **Imaging:** chest radiograph/CT showing multifocal/bilateral infiltrates, consolidation, and effusions (nonspecific; supportive).
- **Laboratory abnormalities:** leukocytosis with neutrophilia; coagulopathy/DIC markers in severe disease.

**Differential diagnosis:** community-acquired bacterial pneumonia, inhalational anthrax, tularemia pneumonia, influenza/severe viral pneumonia, hantavirus pulmonary syndrome, melioidosis, and Q fever. Distinguishing features: rapid progression, hemoptysis, epidemiologic exposure, and F1 antigen positivity. Co-infection can occur — a case of pneumonic plague with nosocomial MDR *Stenotrophomonas maltophilia* has been reported ([PMID: 29843675](https://pubmed.ncbi.nlm.nih.gov/29843675/)).

**Omics/genetic testing of the host:** not applicable diagnostically.

---

## Outcome / Prognosis

**Mortality is the defining outcome and is dominated by treatment timing.**

- **Untreated:** "Without antibacterial therapy, the disease is associated with a high case fatality rate, ranging from 40% (bubonic plague) to nearly 100% (septicemic and pneumonic plague)" ([PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)).
- **US surveillance (1942–2018, 533 cases):** mortality **9% with high-efficacy therapy vs 51% with limited-efficacy therapy** ([PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/)).
- **2017 Madagascar:** observed mortality among treated cases (~25%) was lower than the classic ~50% "in treated patients," attributed partly to widespread community antibiotic use and overdiagnosis ([PMID: 32274983](https://pubmed.ncbi.nlm.nih.gov/32274983/)); confirmed-case CFR (25%) exceeded probable (8%) ([PMID: 30930106](https://pubmed.ncbi.nlm.nih.gov/30930106/)).

| Population / setting | Case-fatality | Source |
|---|---|---|
| Untreated pneumonic/septicemic | ~100% | [PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/) |
| US, high-efficacy antimicrobials | 9% | [PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/) |
| US, limited-efficacy therapy only | 51% | [PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/) |
| 2017 Madagascar, treated (observed) | ~25% | [PMID: 32274983](https://pubmed.ncbi.nlm.nih.gov/32274983/) |
| 2017 Madagascar, confirmed cases | 25% (8/32) | [PMID: 30930106](https://pubmed.ncbi.nlm.nih.gov/30930106/) |

**Prognostic factors:** time from symptom onset to effective antibiotic (single most important), antimicrobial class (aminoglycosides/tetracyclines/fluoroquinolones favorable), pregnancy, co-infection, and access to care. **Recovery potential:** with early appropriate antibiotics and supportive care, full recovery is expected; chronic sequelae are not characteristic. **Complications:** ARDS, septic shock, DIC, multi-organ failure, secondary/opportunistic infection.

---

## Treatment

**Antibiotics are the definitive therapy; speed is decisive.** NCIT term suggestions in brackets.

- **Aminoglycosides:** streptomycin (historical gold standard) and gentamicin [NCIT:C820 Streptomycin; NCIT:C563 Gentamicin]. In US data, "Aminoglycosides and tetracyclines were used more commonly than other classes, and their use was associated with increased odds of survival of plague" ([PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/)).
- **Fluoroquinolones:** ciprofloxacin [NCIT:C2159], levofloxacin, moxifloxacin. **Oral ciprofloxacin monotherapy was noninferior to aminoglycoside-ciprofloxacin** in a Madagascar RCT (treatment failure 9.0% [10/111]) ([PMID: 40768716](https://pubmed.ncbi.nlm.nih.gov/40768716/)). In vitro pharmacodynamic modeling found comparator agents (including ciprofloxacin, moxifloxacin, gentamicin, meropenem) superior to streptomycin without selecting resistance ([PMID: 21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/)).
- **Tetracyclines:** doxycycline [NCIT:C692] — treatment and prophylaxis.
- **Chloramphenicol** [NCIT:C375] — historically used, including for plague meningitis.
- **Intracellular considerations:** streptomycin and ciprofloxacin retain efficacy against intracellular *Y. pestis*, whereas gentamicin and doxycycline are less potent intracellularly ([PMID: 21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/)) — relevant to early-stage/prophylactic selection.
- **Supportive care:** oxygen/mechanical ventilation for respiratory failure, fluid resuscitation, vasopressors for shock, management of DIC. Strict respiratory isolation for pneumonic cases.
- **Combination therapy** may be used in severe/septic disease or co-infection ([PMID: 29843675](https://pubmed.ncbi.nlm.nih.gov/29843675/)).

**Pharmacogenomics:** no plague-specific host pharmacogenomic guidance. Standard aminoglycoside ototoxicity considerations (e.g., MT-RNR1 variants) are general, not plague-specific.

**Antimicrobial resistance.** Resistance is rare but a documented threat: the 1995 Madagascar isolate IP275 carried a self-transmissible IncA/C plasmid (pIP1202) "that conferred resistance to many of the antimicrobials recommended for plague treatment and prophylaxis" ([PMID: 17375195](https://pubmed.ncbi.nlm.nih.gov/17375195/)); independent streptomycin- and doxycycline-resistance plasmids have also been found ([PMID: 29030266](https://pubmed.ncbi.nlm.nih.gov/29030266/)). However, a survey found "no resistance in 392 Y. pestis isolates from 17 countries to eight antimicrobials used for treatment or prophylaxis of plague" ([PMID: 22024826](https://pubmed.ncbi.nlm.nih.gov/22024826/)).

---

## Prevention

- **Primary prevention:** vector/rodent control (flea control, reservoir management), avoidance of sick animals, public health education in endemic foci, and infection control (respiratory isolation, PPE) around pneumonic cases.
- **Post-exposure prophylaxis (PEP):** "Persons who come in contact with patients with pneumonic plague should receive antibiotic prophylaxis with doxycycline or ciprofloxacin for 7 days" ([PMID: 15677847](https://pubmed.ncbi.nlm.nih.gov/15677847/)).
- **Immunization:** **no licensed vaccine currently available.** Leading candidates target **F1 and LcrV/V antigens**:
  - Subunit **F1-V (rF1-LcrV) fusion** — protection requires TNFα and IFNγ: "neutralizing TNFα and IFNγ interferes with protection conferred by immunization with recombinant F1-LcrV fusion protein vaccine (p<0.0005)" ([PMID: 20840834](https://pubmed.ncbi.nlm.nih.gov/20840834/)).
  - **T-cell antigen:** "immunizing mice with a single peptide, YopE(69-77), suffices to confer significant protection from lethal pulmonary challenge" ([PMID: 21653834](https://pubmed.ncbi.nlm.nih.gov/21653834/)).
  - **Adenoviral-vectored F1-V:** "only the human adenovirus 5 construct expressing a full length F1-V fusion provided 100% protection from both morbidity and mortality after a single dose" ([PMID: 41736398](https://pubmed.ncbi.nlm.nih.gov/41736398/)).
  - **Bivalent mRNA-LNP (F1 + LcrV)** ([PMID: 40279638](https://pubmed.ncbi.nlm.nih.gov/40279638/)) and **nanolipoprotein F1:V** ([PMID: 40642079](https://pubmed.ncbi.nlm.nih.gov/40642079/)) confer strong protection against aerosol challenge.
  - **rV10** — an LcrV variant lacking residues 271–300 with reduced IL-10-inducing/immunomodulatory activity while remaining protective, a rational safer-antigen design ([PMID: 16041032](https://pubmed.ncbi.nlm.nih.gov/16041032/)).
- **Secondary/tertiary prevention:** rapid case detection (F1 RDT), early treatment, and contact tracing with PEP.
- **Genetic screening/counseling:** not applicable.

---

## Other Species / Natural Disease

- **Causative organism taxonomy:** *Yersinia pestis* — **NCBITaxon:632**.
- **Reservoirs & vectors:** rodents (e.g., ground squirrels, rats, marmots, prairie dogs) and their fleas — *Oropsylla montana*, *Xenopsylla cheopis* ([PMID: 23590319](https://pubmed.ncbi.nlm.nih.gov/23590319/)).
- **Naturally occurring disease in other species:** highly susceptible carnivores and companion animals — **domestic cats** develop pneumonic/systemic plague and can transmit to humans; dogs are more resistant. Prairie dogs suffer devastating epizootics.
- **Zoonotic potential:** high — plague is a paradigmatic zoonosis with direct animal-to-human and human-to-human (pneumonic) transmission.
- **Comparative pathology / evolution:** the mouse pneumonic model recapitulates human purulent exudative bronchopneumonia closely ([PMID: 16306265](https://pubmed.ncbi.nlm.nih.gov/16306265/)); virulence mechanisms (T3SS, LcrV/IL-10 axis) are conserved across *Yersinia* — V-antigen-induced IL-10 evasion is shared with *Y. enterocolitica* ([PMID: 11801671](https://pubmed.ncbi.nlm.nih.gov/11801671/)).

---

## Model Organisms

- **Mouse (intranasal / aerosol) — primary model.** *Mus musculus* (NCBITaxon:10090); BALB/c and C57BL/6 strains. The intranasal model produces disease that "closely resembles the disease observed in humans," with defined biphasic kinetics ([PMID: 16306265](https://pubmed.ncbi.nlm.nih.gov/16306265/)); the aerosol-challenge model is standard for vaccine efficacy ([PMID: 20840834](https://pubmed.ncbi.nlm.nih.gov/20840834/), [PMID: 41736398](https://pubmed.ncbi.nlm.nih.gov/41736398/)). BALB/c is used for CNS/vascular studies ([PMID: 42422735](https://pubmed.ncbi.nlm.nih.gov/42422735/)).
- **Non-human primates** — used to confirm F1/LcrV vaccine protection and to model human aerosol disease.
- **In vitro / cellular models:** J774 and RAW 264.7 macrophages (phagocytosis/T3SS assays; [PMID: 11854232](https://pubmed.ncbi.nlm.nih.gov/11854232/), [PMID: 21118021](https://pubmed.ncbi.nlm.nih.gov/21118021/)); THP-1 human macrophages (intracellular antibiotic efficacy; [PMID: 21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/)); primary human/murine leukocytes (LTB4 studies; [PMID: 38271464](https://pubmed.ncbi.nlm.nih.gov/38271464/)); in vitro pharmacodynamic models for antibiotic testing ([PMID: 21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/)).
- **Flea vector models:** *X. cheopis* and *O. montana* transmission models delineate blockage-dependent and early-phase transmission ([PMID: 17074909](https://pubmed.ncbi.nlm.nih.gov/17074909/), [PMID: 20395271](https://pubmed.ncbi.nlm.nih.gov/20395271/), [PMID: 23590319](https://pubmed.ncbi.nlm.nih.gov/23590319/)).
- **Model caveat:** analgesia can confound immunologic readouts — extended-release buprenorphine altered immune responses and bacterial dissemination in aerosolized-challenge mice ([PMID: 42212153](https://pubmed.ncbi.nlm.nih.gov/42212153/)).

---

## Key Findings (with statistical evidence)

### 1. Pla protease is essential for primary pneumonic plague
The *Y. pestis* outer-membrane omptin protease **Pla** (plasminogen activator, encoded on pPCP1/pPst) is indispensable specifically for the pneumonic form. In mouse intranasal infection, "the plasminogen activator Pla is essential for Y. pestis to cause primary pneumonic plague but is less important for dissemination during pneumonic plague than during bubonic plague" and "Pla allows Y. pestis to replicate rapidly in the airways, causing a lethal fulminant pneumonia; if unexpressed, inflammation is aborted, and lung repair is activated" ([PMID: 17255510](https://pubmed.ncbi.nlm.nih.gov/17255510/)). This makes Pla the pivotal airway-replication switch and a rational target. Notably, its interaction with the host substrate α2-antiplasmin appears not to be the operative in-vivo mechanism ([PMID: 26438794](https://pubmed.ncbi.nlm.nih.gov/26438794/)).

### 2. Disease follows a biphasic anti-inflammatory → pro-inflammatory course
The mouse model reveals "a strikingly biphasic syndrome, in which the infection begins with an antiinflammatory state in the first 24-36 h that rapidly progresses to a highly proinflammatory state by 48 h and death by 3 days," with mice succumbing to "a purulent multifocal severe exudative bronchopneumonia that closely resembles the disease observed in humans" ([PMID: 16306265](https://pubmed.ncbi.nlm.nih.gov/16306265/)). In vivo the *yop-ysc* T3SS and the chromosomal *pgm* locus are upregulated. This kinetic — stealth then storm — is the organizing principle of the pathophysiology.

### 3. The T3SS suppresses leukotriene B4 to evade early immunity
Leukocytes normally sense the T3SS to trigger LTB4-driven neutrophil recruitment, but *Y. pestis* actively blocks it: "we demonstrate that leukocytes recognize the T3SS to initiate the rapid synthesis of LTB4," and "exogenous administration of LTB4 prior to infection limited bacterial proliferation, suggesting that the absence of LTB4 synthesis during plague contributes to Y. pestis immune evasion" ([PMID: 38271464](https://pubmed.ncbi.nlm.nih.gov/38271464/)). This identifies a druggable early-immune-evasion node.

### 4. LcrV drives TLR2/CD14–IL-10 immunosuppression
Secreted **LcrV** induces the anti-inflammatory cytokine IL-10 and suppresses TNFα/IFNγ: "recombinant LcrV signals in a CD14- and toll-like receptor 2 (TLR2)-dependent fashion leading to immunosuppression by interleukin 10 induction" ([PMID: 12391013](https://pubmed.ncbi.nlm.nih.gov/12391013/)). The suppression is IL-10-dependent — "TNF-alpha suppression was absent in LcrV-treated macrophages of IL-10-deficient (IL-10-/-) mice" ([PMID: 11801671](https://pubmed.ncbi.nlm.nih.gov/11801671/)) — and IL-10−/− mice are highly resistant to *Yersinia*. A de-immunomodulated LcrV variant (rV10) retains protection with reduced IL-10 induction ([PMID: 16041032](https://pubmed.ncbi.nlm.nih.gov/16041032/)).

### 5. F1 capsule + T3SS jointly make *Y. pestis* antiphagocytic
"F1 is encoded by the caf1 gene located on the large 100-kb pFra plasmid, which is unique to Y. pestis," and "F1 and the virulence plasmid-encoded type III system act in concert to make Y. pestis highly resistant to uptake by phagocytes"; a strain lacking both was phagocytosed ~95% ([PMID: 11854232](https://pubmed.ncbi.nlm.nih.gov/11854232/)). F1 is both a virulence factor and the key diagnostic/vaccine antigen.

### 6. F1 antigen rapid diagnostic test enables bedside diagnosis
The lateral-flow RDT "detected concentrations of F1 antigen as low as 0.5 ng/mL in up to 15 min, and had a shelf life of 21 days at 60 degrees C. Its sensitivity and specificity were both 100%," outperforming bacteriology and ELISA on clinical specimens ([PMID: 12547544](https://pubmed.ncbi.nlm.nih.gov/12547544/)) — transformative for endemic, resource-limited settings.

### 7. Antibiotics transform prognosis; ciprofloxacin monotherapy is sufficient
US surveillance: "Mortality differed significantly among those receiving high-efficacy therapy (9%) and only limited-efficacy therapy (51%)," with aminoglycosides and tetracyclines associated with survival ([PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/)). The Madagascar RCT: "Ciprofloxacin monotherapy was noninferior to aminoglycoside-ciprofloxacin therapy" ([PMID: 40768716](https://pubmed.ncbi.nlm.nih.gov/40768716/)). PEP is doxycycline or ciprofloxacin for 7 days ([PMID: 15677847](https://pubmed.ncbi.nlm.nih.gov/15677847/)).

### 8. F1/LcrV immunity protects via antibodies + Th1 cytokines
Protection by the F1-V vaccine requires TNFα and IFNγ ([PMID: 20840834](https://pubmed.ncbi.nlm.nih.gov/20840834/)); YopE(69-77) is a protective CD8 epitope ([PMID: 21653834](https://pubmed.ncbi.nlm.nih.gov/21653834/)); next-gen adenoviral, mRNA-LNP, and nanolipoprotein platforms give 90–100% protection against aerosol challenge ([PMID: 41736398](https://pubmed.ncbi.nlm.nih.gov/41736398/), [PMID: 40279638](https://pubmed.ncbi.nlm.nih.gov/40279638/), [PMID: 40642079](https://pubmed.ncbi.nlm.nih.gov/40642079/)).

### 9. Transmission ecology: flea-borne zoonosis + biofilm + early-phase transmission
*Y. pestis* is "primarily a rodent-associated, flea-borne zoonosis maintained in sylvatic foci" ([PMID: 23590319](https://pubmed.ncbi.nlm.nih.gov/23590319/)); pneumonic spread is airborne ([PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)). Flea transmission occurs by *hms*-biofilm proventricular blockage — "Yersinia pestis biofilm formation causes massive adsorption of haemin or Congo red in vitro as well as colonization and eventual blockage of the flea proventriculus in vivo" ([PMID: 17074909](https://pubmed.ncbi.nlm.nih.gov/17074909/)) — and by a complementary biofilm-independent early-phase mechanism, where "Biofilm-defective mutants transmitted... as efficiently as the parent strain, whereas the EPT efficiency of fleas fed the biofilm-overproducing strain was significantly less" ([PMID: 20395271](https://pubmed.ncbi.nlm.nih.gov/20395271/)).

### 10. Epidemic potential: 2017 Madagascar
78% of the 2414 suspected cases were pneumonic ([PMID: 30930106](https://pubmed.ncbi.nlm.nih.gov/30930106/)), with >20 independent introductions from rural foci ([PMID: 38270131](https://pubmed.ncbi.nlm.nih.gov/38270131/)) and atypical presentations complicating diagnosis ([PMID: 32274983](https://pubmed.ncbi.nlm.nih.gov/32274983/)).

### 11. MDR is rare but a documented, transmissible threat
The first MDR isolate (IP275, 1995) carried a self-transmissible plasmid conferring resistance to many recommended antimicrobials ([PMID: 17375195](https://pubmed.ncbi.nlm.nih.gov/17375195/)), yet a 392-isolate, 17-country survey found no resistance to eight anti-plague antimicrobials ([PMID: 22024826](https://pubmed.ncbi.nlm.nih.gov/22024826/)).

---

## Mechanistic Model / Interpretation

Pneumonic plague is best understood as a **race between bacterial immune subversion and the host's ability to mount protective inflammation — a race the pathogen almost always wins unless antibiotics intervene early.** The virulence factors are not redundant; they attack complementary arms of innate defense:

| Virulence factor | Genetic locus | Immune arm neutralized | Net effect |
|---|---|---|---|
| Pla protease | pPCP1 | Fibrinolytic control of airway | Rapid airway replication |
| T3SS/Yop | pCD1 | LTB4 → neutrophil recruitment | No early neutrophil influx |
| LcrV | pCD1 | TLR2/CD14 → IL-10 → TNFα/IFNγ | Global cytokine suppression |
| F1 capsule | pFra (caf1) | Phagocytosis | Extracellular survival |
| hms biofilm | chromosome | (vector stage) | Flea transmission |

The **early anti-inflammatory phase** is the therapeutic window and the reason mortality is so exquisitely time-dependent: once bacterial burden crosses the threshold that triggers the **late cytokine storm**, tissue destruction, sepsis, and DIC become self-sustaining and antibiotics can no longer reverse the trajectory. This model explains three clinical observations at once: (1) near-100% untreated lethality (unopposed early evasion), (2) the dramatic mortality drop with *early* high-efficacy antibiotics, and (3) why vaccines that restore/require TNFα and IFNγ (or that provide neutralizing anti-F1/anti-LcrV antibody before challenge) are protective — they pre-empt the very axes the pathogen suppresses.

---

## Evidence Base

| PMID | Contribution |
|---|---|
| [17255510](https://pubmed.ncbi.nlm.nih.gov/17255510/) | Pla essential for primary pneumonic plague (mouse) |
| [16306265](https://pubmed.ncbi.nlm.nih.gov/16306265/) | Biphasic immunopathology; validated mouse model |
| [38271464](https://pubmed.ncbi.nlm.nih.gov/38271464/) | T3SS suppression of LTB4 immune evasion |
| [12391013](https://pubmed.ncbi.nlm.nih.gov/12391013/) | LcrV → TLR2/CD14 → IL-10 axis |
| [11801671](https://pubmed.ncbi.nlm.nih.gov/11801671/) | IL-10-dependence of V-antigen TNFα suppression |
| [16041032](https://pubmed.ncbi.nlm.nih.gov/16041032/) | rV10 de-immunomodulated vaccine antigen |
| [11854232](https://pubmed.ncbi.nlm.nih.gov/11854232/) | F1 + T3SS antiphagocytic synergy |
| [12547544](https://pubmed.ncbi.nlm.nih.gov/12547544/) | F1 rapid diagnostic test performance |
| [32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/) | US mortality 9% vs 51% by antimicrobial efficacy |
| [40768716](https://pubmed.ncbi.nlm.nih.gov/40768716/) | Ciprofloxacin monotherapy noninferiority RCT |
| [15677847](https://pubmed.ncbi.nlm.nih.gov/15677847/) | PEP with doxycycline/ciprofloxacin 7 days |
| [25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/) | Untreated CFR ~100%; airborne transmission |
| [30930106](https://pubmed.ncbi.nlm.nih.gov/30930106/) | 2017 Madagascar epidemiology; global distribution |
| [38270131](https://pubmed.ncbi.nlm.nih.gov/38270131/) | Multiple introductions in 2017 epidemic |
| [32274983](https://pubmed.ncbi.nlm.nih.gov/32274983/) | Atypical presentations; observed vs expected mortality |
| [20840834](https://pubmed.ncbi.nlm.nih.gov/20840834/) | TNFα/IFNγ required for F1-V protection |
| [21653834](https://pubmed.ncbi.nlm.nih.gov/21653834/) | YopE(69-77) protective CD8 epitope |
| [41736398](https://pubmed.ncbi.nlm.nih.gov/41736398/) / [40279638](https://pubmed.ncbi.nlm.nih.gov/40279638/) / [40642079](https://pubmed.ncbi.nlm.nih.gov/40642079/) | Next-gen vaccine platforms |
| [17375195](https://pubmed.ncbi.nlm.nih.gov/17375195/) / [22024826](https://pubmed.ncbi.nlm.nih.gov/22024826/) / [29030266](https://pubmed.ncbi.nlm.nih.gov/29030266/) | MDR plasmids vs. low resistance prevalence |
| [23590319](https://pubmed.ncbi.nlm.nih.gov/23590319/) / [17074909](https://pubmed.ncbi.nlm.nih.gov/17074909/) / [20395271](https://pubmed.ncbi.nlm.nih.gov/20395271/) | Flea vector ecology & transmission mechanisms |
| [21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/) / [21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/) | Intracellular & pharmacodynamic antibiotic efficacy |
| [39808829](https://pubmed.ncbi.nlm.nih.gov/39808829/) | US endemicity & weather-linked variation |

---

## Limitations and Knowledge Gaps

1. **Host genetics essentially unknown.** No validated human susceptibility/protective loci exist; the TYK2 P1104A link to pneumonic plague is explicitly speculative ([PMID: 42382739](https://pubmed.ncbi.nlm.nih.gov/42382739/)). Host GWAS in endemic populations are lacking.
2. **Model-organism reliance.** Much mechanistic detail (biphasic kinetics, Pla essentiality, LTB4 suppression) derives from mouse and in-vitro systems; direct human tissue confirmation is limited by the disease's rarity and lethality. Analgesia confounds animal readouts ([PMID: 42212153](https://pubmed.ncbi.nlm.nih.gov/42212153/)).
3. **Epidemiologic uncertainty.** Outbreak counts include clinically suspected cases with overdiagnosis; observed mortality figures (e.g., 2017 Madagascar) are confounded by widespread community antibiotic use ([PMID: 32274983](https://pubmed.ncbi.nlm.nih.gov/32274983/)).
4. **No licensed vaccine.** Despite strong animal efficacy, no F1/LcrV vaccine is licensed; correlates of protection in humans are undefined.
5. **Resistance surveillance.** MDR is rare but plasmid-mediated resistance is proven and transmissible; ongoing genomic surveillance is essential ([PMID: 17375195](https://pubmed.ncbi.nlm.nih.gov/17375195/)).
6. **Long-term outcomes/QoL in survivors** are essentially uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Human genetic susceptibility study** — GWAS/immunogenetic study in Madagascar endemic populations to test host-modifier hypotheses (including TYK2, IL-10 pathway variants).
2. **Host-directed adjunctive therapy trials** — test whether IL-10 blockade, or early exogenous LTB4/TNFα/IFNγ restoration, augments antibiotics in animal models, exploiting the identified evasion nodes ([PMID: 38271464](https://pubmed.ncbi.nlm.nih.gov/38271464/), [PMID: 12391013](https://pubmed.ncbi.nlm.nih.gov/12391013/)).
3. **Advance a de-immunomodulated LcrV (rV10)-based mRNA/adenoviral vaccine** toward human Phase I, defining human correlates of protection ([PMID: 16041032](https://pubmed.ncbi.nlm.nih.gov/16041032/), [PMID: 40279638](https://pubmed.ncbi.nlm.nih.gov/40279638/)).
4. **Deploy and evaluate point-of-care CRISPR/isothermal NAATs** alongside F1 RDTs for earlier confirmation in endemic settings ([PMID: 42413880](https://pubmed.ncbi.nlm.nih.gov/42413880/)).
5. **Strengthen genomic AMR surveillance** in Madagascar and other foci to detect emerging transmissible resistance plasmids ([PMID: 22024826](https://pubmed.ncbi.nlm.nih.gov/22024826/), [PMID: 29030266](https://pubmed.ncbi.nlm.nih.gov/29030266/)).
6. **Operational research on time-to-antibiotic** — given the 9% vs 51% mortality gradient, quantify and shorten the symptom-onset-to-treatment interval in endemic health systems ([PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/)).

---

*Report compiled from 14 confirmed findings and 53 reviewed papers. Evidence types span human clinical/epidemiologic studies, mouse and non-human primate models, in-vitro cellular assays, and computational/genomic analyses, as annotated per claim.*


## Artifacts

- [OpenScientist final report](Pneumonic_Plague-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pneumonic_Plague-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 24 |
| Quoted claims found in source | 24 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 38 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 20 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0011446` (1 mention) - the report calls it "Abnormal consciousness"; HP calls it **Abnormality of mental function**
- `HP:0005521` (1 mention) - the report calls it "DIC"; HP calls it **Disseminated intravascular coagulation**
- `UBERON:0002106` (1 mention) - the report calls it "spleen", "Secondary organ involvement:** **spleen"; UBERON calls it **spleen**
- `NCIT:C2159` (1 mention) - the report calls it "Fluoroquinolones:** ciprofloxacin"; NCIT calls it **Protein Phosphatase Inhibitor**
- `NCIT:C692` (1 mention) - the report calls it "Tetracyclines:** doxycycline"; NCIT calls it **Nimodipine**
- `NCIT:C375` (1 mention) - the report calls it "Chloramphenicol"; NCIT calls it **Ciprofloxacin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `CL:0000583` (2 mentions) - the report calls it "Cell populations:** alveolar macrophages"; CL calls it **alveolar macrophage**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002106` - called "spleen", "Secondary organ involvement:** **spleen"