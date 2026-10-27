---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T18:37:13.475534'
end_time: '2026-09-04T19:12:56.706886'
duration_seconds: 2143.23
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Neuralgic Amyotrophy
  mondo_id: ''
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
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 40
reference_validation:
  total_references: 40
  verified: 40
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 40
  on_topic: 16
  off_topic: 1
  off_topic_references:
  - PMID:40213747
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 32
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.03
  labels_checked: 23
  labels_matching: 14
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0100053
    reported_labels:
    - neuralgic amyotrophy
    ontology_label: anaphylaxis
  - term_id: UBERON:0001824
    reported_labels:
    - brachial plexus
    ontology_label: mucosa of larynx
  - term_id: UBERON:0001379
    reported_labels:
    - deltoid
    ontology_label: vastus lateralis
  - term_id: NCIT:C198
    reported_labels:
    - Prednisone
    ontology_label: Acetaminophen
  - term_id: NCIT:C1409
    reported_labels:
    - Corticosteroid
    ontology_label: Carbenicillin Indanyl Sodium
  - term_id: NCIT:C579
    reported_labels:
    - Immunoglobulin therapy
    ontology_label: Inorganic Chemical
  - term_id: NCIT:C157810
    reported_labels:
    - Neurolysis
    ontology_label: Cervical Cancer Surgery
  - term_id: NCIT:C15296
    reported_labels:
    - Physical Therapy
    ontology_label: Isolated Chemotherapeutic Perfusion
  labels_variant: 1
  unresolved_terms:
  - UBERON:0003732
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
  path: Neuralgic_Amyotrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neuralgic_Amyotrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neuralgic Amyotrophy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Neuralgic Amyotrophy** covering all of the
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

# Neuralgic Amyotrophy (Parsonage–Turner Syndrome): A Comprehensive Disease Characterization

## Summary

**Neuralgic Amyotrophy (NA)**, also known as **Parsonage–Turner syndrome (PTS)** or **brachial plexus neuritis**, is a distinct, painful, multifocal peripheral neuropathy that predominantly targets the brachial plexus and its terminal branches. Its clinical hallmark is an abrupt onset of severe, continuous neuropathic pain in the shoulder and upper arm, which after roughly four weeks gives way to patchy flaccid paresis, muscle atrophy, and sensory disturbance. NA exists in two forms: a common **idiopathic form (INA)** and a rarer **autosomal-dominant hereditary form (HNA)**, the latter caused in about 55% of families by mutations in the **SEPT9 (SEPTIN9)** gene on chromosome 17q25. Once regarded as a rare and benign self-limited condition, NA is now recognized as **common (incidence ~1 per 1,000 per year), profoundly underdiagnosed, and prognostically guarded**, with a majority of patients left with residual functional limitations.

The pathophysiology reflects a **three-factor model**: an underlying genetic predisposition, a mechanical susceptibility of the brachial plexus (likely involving the epineurial blood–nerve barrier), and an **immune/autoimmune trigger** for individual attacks. Triggers include infection (notably **hepatitis E virus**, HEV), vaccination (including COVID-19 mRNA and viral-vector vaccines), surgery, trauma, childbirth, and strenuous exercise. The convergence of these factors produces a focal inflammatory neuritis whose imaging signature is the **pathognomonic hourglass-like nerve constriction (HGC)**, detectable by high-resolution ultrasound and MR neurography in roughly three-quarters of acutely imaged patients. Direct histopathologic evidence of multifocal mononuclear inflammatory infiltrates on nerve biopsy supports the immune basis, and a naturally occurring inflammatory brachial plexus neuritis in cats provides a comparative-species analogue.

Management centers on **early high-dose corticosteroids** for pain control in the acute phase, **motor-relearning multidisciplinary rehabilitation** (rather than strength training) for the chronic phase, and **microsurgical neurolysis** of hourglass constrictions in selected patients who fail to recover. Diagnosis remains fundamentally clinical and one of exclusion, supported by electrodiagnostics, modern nerve imaging, HEV serology (particularly when the phrenic nerve/diaphragm is involved), and SEPT9 genetic testing in hereditary or pediatric cases. This report synthesizes eight confirmed findings drawn from 47 reviewed papers across all 15 requested disease-characteristic domains.

---

## 1. Disease Information

**Overview.** Neuralgic Amyotrophy is an uncommon-to-underrecognized peripheral nervous-system disorder characterized by episodes ("attacks") of extreme neuropathic pain followed by rapid, multifocal, patchy weakness and atrophy predominantly in the upper limbs. In its classic presentation it is a brachial plexopathy or multifocal motor-predominant neuropathy with a monophasic course, though sensory involvement is common and extra-plexus nerves are frequently affected.

**Key identifiers (as commonly catalogued):**
- **MONDO:** MONDO:0100053 (neuralgic amyotrophy) — suggested; confirm in current release
- **OMIM:** 162100 (Neuralgic amyotrophy / hereditary brachial plexus neuropathy, HNA)
- **Orphanet:** ORPHA:2901 (Neuralgic amyotrophy)
- **ICD-10:** G54.5 (Neuralgic amyotrophy)
- **ICD-11:** 8B93 / brachial plexus disorder region (neuralgic amyotrophy)
- **MeSH:** D020968 (Brachial Plexus Neuritis)
- **Gene (HNA):** SEPT9 / SEPTIN9, HGNC:7323, chromosome 17q25

**Synonyms and alternative names:** Parsonage–Turner syndrome; brachial plexus neuritis; brachial neuritis; brachial neuralgic amyotrophy; idiopathic brachial plexopathy; acute brachial neuropathy; hereditary brachial plexus neuropathy (HBPN, hereditary form); shoulder-girdle syndrome. Parsonage and Turner unified previously separate descriptions under the term "neuralgic amyotrophy" in 1948, highlighting the combination of neuropathic pain and muscular atrophy ([PMID: 39070412](https://pubmed.ncbi.nlm.nih.gov/39070412/)).

**Source of information.** The knowledge in this report is derived from **aggregated disease-level resources** — cohort studies, case-control studies, clinical reviews, and case reports/series — rather than individual EHR extraction. The largest supporting cohort comprised 246 patients ([PMID: 16371410](https://pubmed.ncbi.nlm.nih.gov/16371410/)).

---

## 2. Etiology

**Disease causal factors.** NA is a **complex disease** arising from the interaction of genetic predisposition, mechanical vulnerability, and immune-mediated triggering. There is no single cause; rather, the current, well-supported model is a **triad** ([PMID: 21556032](https://pubmed.ncbi.nlm.nih.gov/21556032/)):

> "The disease is thought to result from an underlying genetic predisposition, a susceptibility to mechanical injury of the brachial plexus (possibly representing disturbance of the epineurial blood-nerve barrier), and an immune or autoimmune trigger for the attacks."

**Genetic risk factors.** In the hereditary form (HNA), **SEPT9** point mutations and duplications on 17q25 are causal in ~55% of families (see Section 4). SEPT9 variants have also been linked to a broader phenotypic spectrum, including a Charcot–Marie–Tooth-like presentation ([PMID: 32122354](https://pubmed.ncbi.nlm.nih.gov/32122354/)). In idiopathic NA, a genetic susceptibility is inferred but not molecularly defined; recurrence and family history predict a discoverable genetic cause ([PMID: 30560241](https://pubmed.ncbi.nlm.nih.gov/30560241/)).

**Environmental / triggering risk factors.** Attacks are frequently preceded by immunologically active events:
- **Infection** — the single most-cited category; HEV genotype 3 is a recurrent, characteristic trigger (Section 5).
- **Vaccination** — COVID-19 mRNA and viral-vector vaccines; also post-exposure prophylaxis and influenza vaccine ([PMID: 38543940](https://pubmed.ncbi.nlm.nih.gov/38543940/); [PMID: 25098693](https://pubmed.ncbi.nlm.nih.gov/25098693/)).
- **Surgery, trauma, childbirth/peripartum period, strenuous exercise, cold, and psychological stress** ([PMID: 21556032](https://pubmed.ncbi.nlm.nih.gov/21556032/); [PMID: 31619932](https://pubmed.ncbi.nlm.nih.gov/31619932/)).
- **Age and sex** — idiopathic NA typically presents in adulthood (mean ~41 years) with a male predominance; hereditary NA presents earlier (mean ~28 years).

**Protective factors.** No genetic or environmental protective factors have been established in the literature reviewed. This is a genuine knowledge gap. Prophylactic corticosteroids or IVIG may reduce surgical- or childbirth-induced attacks in HNA, functioning as a preventive (not naturally protective) intervention ([PMID: 38176820](https://pubmed.ncbi.nlm.nih.gov/38176820/)).

**Gene–environment interactions.** The triad model is itself a gene–environment interaction: an immune trigger acting upon a genetically/mechanically predisposed plexus precipitates the focal neuritis. In HNA, external stimuli (infections, vaccinations, cold, stress, surgery, exercise) provoke recurrent attacks on the SEPT9-predisposed background ([PMID: 31619932](https://pubmed.ncbi.nlm.nih.gov/31619932/)).

---

## 3. Phenotypes

NA's phenotype evolves through **three consecutive pain phases**, beginning with an initial severe, continuous pain lasting approximately 4 weeks on average ([PMID: 16371410](https://pubmed.ncbi.nlm.nih.gov/16371410/)):

> "the course of the pain manifests itself in three consecutive phases with an initial severe, continuous pain lasting for approximately 4 weeks on average. Sensory involvement was quite common and found in 78.4% of patients"

| Phenotype | Type | HPO suggestion | Frequency / characteristics |
|---|---|---|---|
| Severe shoulder/arm neuropathic pain | Symptom | HP:0012532 (Chronic pain) / HP:0003326 (Myalgia); neuropathic pain | Near-universal at onset; acute, continuous ~4 weeks |
| Multifocal muscle weakness/paresis | Clinical sign | HP:0003484 (Upper limb muscle weakness) | Follows pain; patchy, motor-predominant |
| Muscle atrophy | Physical manifestation | HP:0003202 (Skeletal muscle atrophy) | Common; early |
| Sensory loss/paresthesia | Symptom/sign | HP:0003390 (Sensory neuropathy) / HP:0003401 (Paresthesia) | 78.4% |
| Scapular winging / dyskinesia | Clinical sign | HP:0003691 (Scapular winging) | >60% residual (Sections 6/11) |
| Phrenic nerve palsy / diaphragmatic paralysis | Clinical sign | HP:0002094 (Dyspnea); diaphragmatic paralysis | Subset, esp. HEV-associated; orthopnea |
| Fatigue | Symptom | HP:0012378 (Fatigue) | ~1/3 long-term |

**Distribution.** The upper/middle trunk pattern — long thoracic and/or suprascapular nerve — is most frequent (71.1%) ([PMID: 16371410](https://pubmed.ncbi.nlm.nih.gov/16371410/)). Involvement is typically **unilateral and asymmetric**, though bilateral involvement occurs, particularly after acute viral infection.

**Age of onset, severity, progression.** Onset is predominantly adult in INA (mean 41.3 yrs) and earlier in HNA (mean 28.4 yrs), spanning infancy to adulthood ([PMID: 16371410](https://pubmed.ncbi.nlm.nih.gov/16371410/); [PMID: 31619932](https://pubmed.ncbi.nlm.nih.gov/31619932/)). Severity is variable; the course is classically **monophasic/episodic**, with recurrence in 26.1% of INA over ~6-year follow-up and a mean of 3.5 attacks in HNA versus 1.5 in INA.

**Quality-of-life impact.** About a quarter to a third of patients report significant long-term pain and fatigue, and half to two-thirds experience persistent impairments in daily life; symptoms correlate with residual shoulder/arm dysfunction rather than psychological distress ([PMID: 19254608](https://pubmed.ncbi.nlm.nih.gov/19254608/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** Hereditary NA is autosomal dominant and associated with a point mutation or duplication in **SEPT9 (SEPTIN9)** on chromosome **17q25** in **55% of affected families** ([PMID: 21556032](https://pubmed.ncbi.nlm.nih.gov/21556032/)):

> "in 55% of affected families, neuralgic amyotrophy is associated with a point mutation or duplication in the SEPT9 gene on chromosome 17q25"

- **Gene:** SEPT9 / SEPTIN9, HGNC:7323, OMIM *604061; HNA phenotype OMIM #162100.
- **Variant types:** missense point mutations (e.g., **p.Arg106Trp / R106W**), intragenic **duplications** (including duplication of exon 2), and CNVs. Classification: pathogenic/likely pathogenic per ACMG in segregating families.
- **Population frequency:** rare; HNA is a rare Mendelian disorder. Specific gnomAD allele frequencies were not established in the reviewed literature.
- **Origin:** germline, autosomal dominant.

**Functional consequences.** SEPT9 mediates septin binding to microtubules. HNA mutations impair this function ([PMID: 34854883](https://pubmed.ncbi.nlm.nih.gov/34854883/)):

> "HNA mutations abrogate this association, identifying a putative regulatory domain"

A MAP-like motif unique to septin-9 isoform 1 drives septin octamer–microtubule interaction, and HNA mutations abrogate this. Molecular-dynamics simulation shows the mutation significantly alters septin-9 conformation, impairing microtubule binding and bundling ([PMID: 39428775](https://pubmed.ncbi.nlm.nih.gov/39428775/)):

> "Molecular simulation study has revealed that the mutation has significantly altered the conformation of septin-9 protein, thereby impairing the microtubule binding and bundling ability"

This constitutes a **loss/alteration of function** in cytoskeletal regulation (cytokinesis, membrane trafficking, stress-fiber tuning).

**Phenotype extensions.** SEPT9 variants can produce dysmorphic features (hypotelorism, cleft palate, long nasal bridge, hypertelorism, epicanthal folds), and a childhood-onset family showed **platelet dysfunction** (reduced ADP/epinephrine-induced aggregation, impaired δ-secretion) and kidney cysts alongside an exon-2 duplication ([PMID: 30019529](https://pubmed.ncbi.nlm.nih.gov/30019529/); [PMID: 40852410](https://pubmed.ncbi.nlm.nih.gov/40852410/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** No modifier genes, disease-specific epigenetic marks, or large-scale chromosomal abnormalities have been established for NA in the reviewed literature — genuine knowledge gaps.

**Suggested ontology terms:** Gene HGNC:7323 (SEPTIN9); GO:0005819 (spindle), GO:0000910 (cytokinesis), GO:0008017 (microtubule binding).

---

## 5. Environmental Information

**Environmental / infectious triggers.** Immune events preceding NA are well documented. In a prospective matched case-control study (n=57), a symptomatic infectious trigger confirmed microbiologically preceded NA in 26.3% of patients, and COVID-19 vaccination was a potential trigger in 12.3% ([PMID: 39364568](https://pubmed.ncbi.nlm.nih.gov/39364568/)):

> "NA onset was preceded by a symptomatic infectious trigger confirmed by microbiological tests in 15/57 (26.3%) patients. Coronavirus disease 2019 vaccination was considered a potential trigger in 7/57 (12.3%) subjects. An acute viral infection was associated with a bilateral involvement of the brachial plexus (p = 0.003, Cramèr's V = 0.43)"

**Hepatitis E virus (HEV, genotype 3)** is a recurrently reported and clinically distinctive trigger, characteristically causing NA with **phrenic nerve involvement and diaphragmatic paralysis** ([PMID: 40534221](https://pubmed.ncbi.nlm.nih.gov/40534221/); [PMID: 38657646](https://pubmed.ncbi.nlm.nih.gov/38657646/)):

> "Electromyography showed severe bilateral phrenic nerve involvement. The diagnosis of neuralgic amyotrophy with diaphragmatic paralysis secondary to HEV was made"

> "NA that shows involvement of the phrenic nerve resulting in diaphragmatic dysfunction and dyspnoea, may be associated with HEV infection"

Agents tested/reported in NA workups include HEV, HIV, SARS-CoV-2, EBV, CMV, parvovirus B19, VZV, *Borrelia*, *Mycoplasma*, and *Bartonella*. Livestock-associated HEV exposure has been implicated ([PMID: 35379662](https://pubmed.ncbi.nlm.nih.gov/35379662/)).

**Occupational/toxic factors.** A rare report links epidemic dropsy (argemone-oil-adulterated mustard oil) with brachial neuritis, but toxic causes are not a recognized major etiology ([PMID: 22231775](https://pubmed.ncbi.nlm.nih.gov/22231775/)).

**Lifestyle factors.** Strenuous physical exercise and unaccustomed exertion of the shoulder girdle are reported precipitants; smoking/diet/alcohol are not established risk factors.

**Suggested ontology term:** NCBI Taxonomy Orthohepevirus A (HEV).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Genetic predisposition** (SEPT9 mutation in HNA; undefined susceptibility in INA) → **leads to** an intrinsically vulnerable brachial plexus, plausibly via altered septin–microtubule cytoskeletal regulation in nerve/supporting cells *(tissue-level mechanism inferred, not fully demonstrated)*.
2. Predisposition **plus** a **mechanical susceptibility** of the plexus — possibly a disturbed epineurial blood–nerve barrier — **results in** a nerve segment prone to immune access and injury ([PMID: 21556032](https://pubmed.ncbi.nlm.nih.gov/21556032/)).
3. An **immune/autoimmune trigger** (infection—especially HEV—vaccination, surgery, trauma, childbirth, exercise) **activates** a focal immune response directed at the brachial plexus ([PMID: 39364568](https://pubmed.ncbi.nlm.nih.gov/39364568/)).
4. The immune response **produces** multifocal **mononuclear inflammatory-cell infiltration** of nerve fascicles (demonstrated on biopsy) ([PMID: 8614534](https://pubmed.ncbi.nlm.nih.gov/8614534/)).
5. Inflammation and focal swelling **lead to** the pathognomonic **hourglass-like constriction / nerve torsion** at vulnerable segments, with proximal/distal thickening ([PMID: 36214185](https://pubmed.ncbi.nlm.nih.gov/36214185/); [PMID: 38248282](https://pubmed.ncbi.nlm.nih.gov/38248282/)).
6. Focal constriction and axonal injury **cause** the acute severe neuropathic **pain** (phase 1).
7. Axonal degeneration **results in** **multifocal flaccid paresis, muscle atrophy, and sensory loss** (phase 2), branching by nerve territory:
   - Long thoracic/suprascapular → **scapular winging and dyskinesia**.
   - Phrenic nerve → **diaphragmatic paralysis, orthopnea, respiratory failure** (branch strongly associated with HEV).
8. Incomplete axonal regeneration and compensatory abnormal motor control **lead to** **chronic scapular dyskinesia, residual weakness, pain, and fatigue** (phase 3) ([PMID: 36697215](https://pubmed.ncbi.nlm.nih.gov/36697215/)).

```
SEPT9 mutation / susceptibility  ─┐
Mechanical vulnerability          ─┼──► predisposed plexus segment
(blood–nerve barrier disturbance) ─┘             │
                                                 ▼
        Immune trigger (HEV, vaccine, surgery, exercise…)
                                                 │
                                                 ▼
        Multifocal mononuclear inflammatory infiltrate
                                                 │
                                                 ▼
        Hourglass constriction / nerve torsion + axonal injury
                          │                          │
                          ▼                          ▼
          Acute neuropathic pain (~4 wk)   Patchy paresis / atrophy / sensory loss
                                                 │
                    ┌────────────────────────────┼───────────────────────┐
                    ▼                            ▼                        ▼
        Long thoracic/suprascapular     Phrenic nerve            Other plexus/extra-plexus
        → scapular winging/dyskinesia   → diaphragm paralysis    → multifocal deficits
                                          (HEV-linked)
                                                 │
                                                 ▼
        Incomplete regeneration + abnormal motor control → chronic disability
```

**Molecular pathways / protein dysfunction.** Upstream: SEPT9 loss of microtubule-binding/bundling disrupts cytoskeletal regulation (cytokinesis, membrane trafficking, stress fibers) ([PMID: 34854883](https://pubmed.ncbi.nlm.nih.gov/34854883/); [PMID: 39428775](https://pubmed.ncbi.nlm.nih.gov/39428775/)). Downstream: an inflammatory-immune cascade drives the attack.

**Cellular processes / immune involvement.** The core downstream mechanism is **inflammation** with mononuclear (lymphocytic/macrophage) infiltration and axonal degeneration ([PMID: 8614534](https://pubmed.ncbi.nlm.nih.gov/8614534/)):

> "There were florid multifocal mononuclear inflammatory cell infiltrates. Present evidence suggests that these brachial neuropathies have an immune basis"

**Tissue damage mechanisms.** Focal constriction/torsion with ischemic and mechanical axonal injury; denervation muscle edema is seen on MRN in 91% of acute cases ([PMID: 36214185](https://pubmed.ncbi.nlm.nih.gov/36214185/)).

**Cell types and biological processes (ontology suggestions):**
- **GO:0006954** (inflammatory response); **GO:0002250** (adaptive immune response) — biological processes.
- **GO:0008017** (microtubule binding), **GO:0000910** (cytokinesis) — SEPT9 molecular function/process.
- **CL:0000101** (sensory neuron); **CL:0011001** (spinal cord motor neuron); **CL:0002573** (Schwann cell); **CL:0000235** (macrophage); **CL:0000542** (lymphocyte) — cell types.

Molecular profiling specific to NA nerve tissue (transcriptomics, proteomics, metabolomics, single-cell, spatial, CRISPR/RNAi screens) was **not available** in the reviewed literature — a substantial knowledge gap.

---

## 7. Anatomical Structures Affected

**Organ / system level.** Primary target: the **peripheral nervous system**, specifically the **brachial plexus** and its branches (long thoracic, suprascapular, axillary, musculocutaneous, radial, median nerves). Secondary involvement: the **respiratory system** via phrenic nerve → diaphragm; the **musculoskeletal system** (shoulder girdle) via denervation atrophy and dyskinesia.

**Nerve territories.** Upper/middle trunk pattern (long thoracic and/or suprascapular) is most frequent (71.1%) ([PMID: 16371410](https://pubmed.ncbi.nlm.nih.gov/16371410/)). Extra-plexus nerves are commonly involved, more so in HNA (55.8% vs 17.3% in INA). Lesions distal to the brachial plexus (e.g., median nerve, mimicking carpal tunnel) can occur in HNA ([PMID: 37587058](https://pubmed.ncbi.nlm.nih.gov/37587058/)).

**Tissue / cell level.** Peripheral nerve tissue (axons, Schwann cells, epineurium/perineurium) and skeletal muscle (secondary denervation atrophy and edema). Inflammatory infiltrate composed of mononuclear cells.

**Subcellular level.** SEPT9 dysfunction implicates the **microtubule cytoskeleton** (GO:0005874) and associated stress fibers; axonal transport machinery is plausibly affected (inferred).

**Localization and lateralization.** Predominantly **unilateral and asymmetric**; **bilateral** involvement occurs, associated with acute viral infection (p=0.003) and characteristically with HEV-linked phrenic disease ([PMID: 39364568](https://pubmed.ncbi.nlm.nih.gov/39364568/); [PMID: 40534221](https://pubmed.ncbi.nlm.nih.gov/40534221/)).

**Suggested UBERON/CL terms:** UBERON:0001824 (brachial plexus); UBERON:0003732 (phrenic nerve); UBERON:0001134 (skeletal muscle tissue); UBERON:0001379 (deltoid); CL:0000101 (sensory neuron); CL:0002573 (Schwann cell).

---

## 8. Temporal Development

**Onset.** Typically **adult-onset** (INA mean 41.3 yrs) but ranges from infancy to old age; HNA onsets earlier (mean 28.4 yrs) and may present in early childhood (e.g., age 2–9 yrs) ([PMID: 16371410](https://pubmed.ncbi.nlm.nih.gov/16371410/); [PMID: 30019529](https://pubmed.ncbi.nlm.nih.gov/30019529/); [PMID: 40852410](https://pubmed.ncbi.nlm.nih.gov/40852410/)). Onset pattern is **acute/subacute** — sudden severe pain within hours to two weeks.

**Progression (three-phase course):**
1. **Acute pain phase** — severe continuous pain, ~4 weeks average.
2. **Paresis phase** — as pain subsides, patchy weakness, atrophy, sensory loss emerge.
3. **Recovery/chronic phase** — slow recovery over months to years; frequently incomplete.

**Course pattern.** Classically **monophasic/episodic**; recurrence in INA is 26.1% over ~6 years, higher in HNA (mean 3.5 attacks). Serratus anterior winging from NA resolves spontaneously within 3 years in a substantial fraction, but no full recovery was seen if winging persisted beyond 3 years ([PMID: 33675974](https://pubmed.ncbi.nlm.nih.gov/33675974/)).

**Critical windows.** Early corticosteroid administration (first month) shortens pain and improves recovery ([PMID: 19321467](https://pubmed.ncbi.nlm.nih.gov/19321467/)). Surgical neurolysis is considered after 6–12 months of non-recovery ([PMID: 32868098](https://pubmed.ncbi.nlm.nih.gov/32868098/)). Imaging abnormalities appear early — as early as 12 h on ultrasound and ~3 days on MRN.

---

## 9. Inheritance and Population

**Epidemiology.** Historically considered rare, NA's true incidence is **~1 per 1,000 per year** ([PMID: 33823638](https://pubmed.ncbi.nlm.nih.gov/33823638/)):

> "its actual incidence rate is about 1 per 1000 per year"

Combined INA + HBPN incidence has been cited as 3–100 per 100,000 persons per year ([PMID: 38176820](https://pubmed.ncbi.nlm.nih.gov/38176820/)). Most cases are diagnosed late or not at all.

**Inheritance (HNA).** **Autosomal dominant**, caused by SEPT9 mutations/duplications in ~55% of families. Features consistent with:
- **Incomplete/variable penetrance and variable expressivity** — inferred from wide intrafamilial clinical variability (e.g., R106W pedigrees) ([PMID: 39428775](https://pubmed.ncbi.nlm.nih.gov/39428775/); [PMID: 42644177](https://pubmed.ncbi.nlm.nih.gov/42644177/)).
- **Anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency** — not established in the reviewed literature (knowledge gaps).

**Demographics.** INA shows a male predominance; HNA affects both sexes. Post-COVID-vaccination PTS occurred more frequently in males (61.1% mRNA; 83.3% viral vector) ([PMID: 38543940](https://pubmed.ncbi.nlm.nih.gov/38543940/)). No strong ethnic or geographic clustering is established, though HNA families are reported across diverse populations (Lebanese, Chinese, Italian, German, Turkish).

**INA vs HNA comparison:**

| Feature | Idiopathic (INA) | Hereditary (HNA) |
|---|---|---|
| n (reference cohort) | 199 | 47 |
| Mean age at onset | 41.3 yrs | 28.4 yrs |
| Mean number of attacks | 1.5 | 3.5 |
| Extra-plexus involvement | 17.3% | 55.8% |
| Genetic cause | undefined | SEPT9 (~55% of families) |
| Outcome | better | poorer |

Source: [PMID: 16371410](https://pubmed.ncbi.nlm.nih.gov/16371410/).

---

## 10. Diagnostics

**Diagnosis is clinical and one of exclusion** ([PMID: 32140911](https://pubmed.ncbi.nlm.nih.gov/32140911/)):

> "The diagnosis is clinical, through a comprehensive history and neurological examination"

Conditions to exclude: cervical radiculopathy, rotator cuff tear, CIDP, compressive plexopathy, and **neurolymphomatosis** (recurrent "attacks" can herald B-cell lymphoma) ([PMID: 30560241](https://pubmed.ncbi.nlm.nih.gov/30560241/)).

**Electrodiagnostics (EMG/NCS).** Show multifocal axonal denervation (fibrillations in ~73%), confirming the pattern and distribution.

**Imaging — the modern confirmatory pillar.** High-resolution ultrasound and MR neurography detect nerve abnormalities in ~90% of patients within one month, including **hourglass constrictions in 74%** and denervation muscle edema on MRN in 91% ([PMID: 36214185](https://pubmed.ncbi.nlm.nih.gov/36214185/)):

> "US and MRN showed nerve abnormalities within 1 mo from NA onset in 90% of patients. HGCs were found in 74% (29/39) of the patients"

Gadolinium-enhanced MRI/MRN help confirm the diagnosis and guide treatment ([PMID: 33823638](https://pubmed.ncbi.nlm.nih.gov/33823638/)):

> "Gadolinium-enhanced magnetic resonance imaging and high-resolution magnetic resonance neurography are useful for confirming the diagnosis and choosing the appropriate treatment"

Diaphragm ultrasound improves detection of phrenic involvement ([PMID: 38176820](https://pubmed.ncbi.nlm.nih.gov/38176820/)).

**Laboratory / biomarkers.** No specific serum biomarker exists. **HEV serology (IgM/IgG plus serum HEV RNA) and transaminases** should be checked, especially with phrenic/diaphragmatic involvement, to identify a treatable trigger. CSF may show albuminocytological dissociation in vaccine-associated cases.

**Genetic testing.** **SEPT9 single-gene testing** (sequencing plus copy-number/duplication analysis) confirms HNA; WES/WGS is useful in atypical or pediatric cases ([PMID: 42644177](https://pubmed.ncbi.nlm.nih.gov/42644177/); [PMID: 40852410](https://pubmed.ncbi.nlm.nih.gov/40852410/)). Indicated with recurrent attacks, family history, early onset, or dysmorphic features.

**Differential diagnosis (distinguishing features):** cervical radiculopathy (dermatomal, neck-movement-related), rotator cuff pathology (mechanical, no denervation), CIDP (symmetric, demyelinating, chronic), compressive plexopathy/neoplasm (progressive, mass), hereditary neuropathy with liability to pressure palsies.

---

## 11. Outcome / Prognosis

**Prognosis is guarded**, contrary to older "benign self-limited" characterizations ([PMID: 38835178](https://pubmed.ncbi.nlm.nih.gov/38835178/)):

> "The prognosis of untreated NA is poor, with 25% of patients remaining unable to work at three years. The main form of treatment is with corticosteroids that are administered as early as possible"

**Morbidity and function.** Over **60% of patients have residual complaints and functional limitations**, correlated with scapular dyskinesia ([PMID: 36697215](https://pubmed.ncbi.nlm.nih.gov/36697215/)):

> "leading to severe pain and multifocal paresis resulting in >60% of patients having residual complaints and functional limitations correlated with scapular dyskinesia"

About a quarter to a third report significant long-term pain and fatigue; half to two-thirds retain impairments; symptoms are not correlated with residual MRC-scale paresis or psychological distress but with mechanical shoulder/arm dysfunction ([PMID: 19254608](https://pubmed.ncbi.nlm.nih.gov/19254608/)).

**Mortality.** NA is not directly fatal, but bilateral diaphragmatic paralysis (e.g., HEV-associated or severe PTS) can cause hypercapnic respiratory failure requiring ventilatory support ([PMID: 41428787](https://pubmed.ncbi.nlm.nih.gov/41428787/)).

**Recovery potential.** Slow recovery over months to years; many never achieve full recovery. Serratus anterior winging resolves spontaneously within 3 years in some but not if it persists beyond 3 years ([PMID: 33675974](https://pubmed.ncbi.nlm.nih.gov/33675974/)). Surgical neurolysis rescues motor function in chronic HGC cases (Section 12).

**Prognostic factors.** Hereditary form, extra-plexus involvement, greater winging severity, comorbidity, and delayed treatment predict worse outcomes. No validated molecular prognostic biomarker exists.

---

## 12. Treatment

**Pharmacotherapy (acute phase).** **Corticosteroids** (oral prednisolone/prednisone; high-dose pulsed steroids) given as early as possible shorten the initial pain and may accelerate recovery in some patients ([PMID: 19321467](https://pubmed.ncbi.nlm.nih.gov/19321467/)):

> "The median time until initial pain relief was lower in the study group (12.5 days vs 20.5 days), and a significantly higher percentage already recovered strength in the first month of treatment (18% vs 6.3%; p = 0.011)"

The Cochrane review found no randomized trials but concluded open-label evidence supports early oral prednisone shortening initial pain ([PMID: 19588414](https://pubmed.ncbi.nlm.nih.gov/19588414/)). Adjunct **non-narcotic analgesics** for neuropathic pain; opioids are generally avoided. NCIT suggestions: NCIT:C769 (Prednisolone), NCIT:C198 (Prednisone), NCIT:C1409 (Corticosteroid).

**Immunotherapy.** In pediatric NA, immunotherapy (IVIG/steroids) appears effective, with improvement continuing over one year ([PMID: 32228355](https://pubmed.ncbi.nlm.nih.gov/32228355/)). Prophylactic steroids or **IVIG** may reduce surgery- or childbirth-induced attacks in HNA ([PMID: 38176820](https://pubmed.ncbi.nlm.nih.gov/38176820/)). NCIT:C579 (Immunoglobulin therapy).

**Etiologic treatment.** When HEV is the trigger, recognition allows targeted management/monitoring and respiratory support.

**Surgical / interventional.** **Microsurgical epineurolysis and perineurolysis of hourglass constrictions** improves recovery in chronic NA that fails conservative management: 9/11 operative vs 3/13 nonsurgical patients recovered clinically, with EMG-confirmed axonal regeneration ([PMID: 32868098](https://pubmed.ncbi.nlm.nih.gov/32868098/)). Surgery is generally considered after ~6–12 months without recovery. Nerve resection/direct suture or grafting is used for unsalvageable segments ([PMID: 41163648](https://pubmed.ncbi.nlm.nih.gov/41163648/)). **Phrenic nerve reconstruction** is an option for symptomatic diaphragmatic paralysis ([PMID: 36031309](https://pubmed.ncbi.nlm.nih.gov/36031309/)). Tendon transfers when recovery does not occur after ~18 months. Early neurolysis/nerve grafts remain controversial ([PMID: 38176820](https://pubmed.ncbi.nlm.nih.gov/38176820/)). NCIT:C15329 (Surgical Procedure), NCIT:C157810 (Neurolysis).

**Rehabilitation.** Modern multidisciplinary rehabilitation targeting **motor relearning, energy conservation, and self-management of pain/fatigue** — not strength training — improves functional outcomes. An RCT (n=47) showed an adjusted mean SRQ-DLV group difference of **8.60 (95% CI 0.26–16.94, p=0.044)**, with clinically relevant improvement in 59% (rehab) vs 33% (usual care), NNT = 4 ([PMID: 36697215](https://pubmed.ncbi.nlm.nih.gov/36697215/)):

> "The mean group difference adjusted for sex, age and SRQ-DLV baseline score was 8.60 (95%CI: 0.26 to 16.94, p=0.044)"

The recommended strategy explicitly avoids strength training ([PMID: 39402917](https://pubmed.ncbi.nlm.nih.gov/39402917/)):

> "target compensatory abnormal motor control and fatigue by focusing on motor coordination, energy conservation strategies, and behavioral change, rather than strength training which may worsen the symptoms"

Multimodal programs (physiotherapy, scapular stabilization) show benefit in case reports ([PMID: 40213747](https://pubmed.ncbi.nlm.nih.gov/40213747/)). NCIT:C15296 (Physical Therapy), NCIT:C15315 (Rehabilitation Therapy).

**Not established for NA (not applicable at present):** pharmacogenomics, gene therapy, RNA-based therapy, cell therapy, targeted molecular immunotherapy.

---

## 13. Prevention

**Primary prevention.** No population-level primary prevention exists for sporadic NA. Trigger awareness/avoidance and, in HNA, avoidance of provocations before elective surgery may help.

**Secondary prevention / early detection.** Early clinical recognition plus imaging (US/MRN) enables timely corticosteroids within the critical first-month window, which improves outcomes ([PMID: 19321467](https://pubmed.ncbi.nlm.nih.gov/19321467/)). Increased awareness in orthopedic and primary-care settings is emphasized to prevent misdiagnosis ([PMID: 34435146](https://pubmed.ncbi.nlm.nih.gov/34435146/)).

**Tertiary prevention.** Rehabilitation to prevent chronic scapular dyskinesia, contractures, and disability; energy-conservation strategies to manage fatigue; prophylactic steroids/IVIG to reduce peri-procedural or peripartum attacks in HNA ([PMID: 38176820](https://pubmed.ncbi.nlm.nih.gov/38176820/)).

**Genetic counseling.** Appropriate for HNA families — autosomal dominant inheritance, ~50% offspring risk, variable expressivity; SEPT9 testing informs family planning and pre-procedure prophylaxis.

**Immunization / public-health / environmental interventions.** No vaccine prevents NA; conversely, certain vaccinations are recognized (rare) triggers. HEV exposure reduction (food safety, livestock-contact awareness) is a plausible environmental measure given HEV's trigger role.

---

## 14. Other Species / Natural Disease

A **naturally occurring inflammatory brachial plexus neuritis exists in cats (*Felis catus*, NCBI:txid9685)**, providing a comparative-species analogue ([PMID: 29925717](https://pubmed.ncbi.nlm.nih.gov/29925717/)):

> "A postmortem examination revealed swollen radial nerves and cervical nerve roots in which infiltration of inflammatory cells was histologically confirmed"

This hypertrophic neuritis caused tetraparesis with histologically confirmed inflammatory infiltration, paralleling the human immune/inflammatory mechanism. **Orthologous gene:** Sept9/SEPTIN9 is conserved across mammals (human HGNC:7323; mouse Sept9). **Comparative biology:** conservation of septin cytoskeletal function and of immune-mediated peripheral neuritis supports cross-species mechanistic relevance. **Zoonotic angle:** HEV is zoonotic (swine reservoir), relevant to the trigger rather than to NA transmission; NA is not itself transmissible. Formal OMIA/veterinary registry entries were not established in the reviewed literature — a knowledge gap.

---

## 15. Model Organisms

No dedicated animal model that recapitulates the full NA phenotype was identified in the reviewed literature. Relevant systems include:

- **In vitro / molecular models:** Molecular-dynamics simulation of mutant septin-9 demonstrates impaired microtubule binding/bundling ([PMID: 39428775](https://pubmed.ncbi.nlm.nih.gov/39428775/)); cell-based assays of septin–microtubule association define the isoform-1 MAP-like motif and show HNA mutations abrogate it ([PMID: 34854883](https://pubmed.ncbi.nlm.nih.gov/34854883/)). Evidence type: computational and in vitro.
- **Naturally occurring animal analogue:** feline hypertrophic brachial plexus neuritis (spontaneous, not engineered) ([PMID: 29925717](https://pubmed.ncbi.nlm.nih.gov/29925717/)).
- **Genetic models (knockout/knock-in/transgenic Sept9):** not established for the NA phenotype in the reviewed literature.

**Limitations of available models:** they capture the molecular (septin/microtubule) dimension or the inflammatory-pathology dimension separately, but no single model reproduces the triad (genetic predisposition + mechanical vulnerability + immune trigger) with hourglass-constriction formation. **Recommended resources for future work:** MGI (mouse Sept9), IMPC/KOMP, Cellosaurus/ATCC and patient-derived iPSC-neuron models.

---

## Mechanistic Model / Interpretation

NA is best understood as a **"three-hit" focal inflammatory neuropathy**. The first hit is a **predisposing background** — a SEPT9 mutation compromising microtubule-based cytoskeletal regulation in HNA, or an undefined susceptibility in INA. The second hit is a **mechanical/anatomical vulnerability** of specific plexus segments, possibly through a leaky epineurial blood–nerve barrier that grants immune cells access. The third hit is an **immune trigger** — most compellingly an infection such as HEV, but also vaccination, surgery, childbirth, or exertion — that ignites a **multifocal mononuclear inflammatory attack**. The convergence produces the disease's structural signature, the **hourglass constriction/nerve torsion**, and drives the stereotyped clinical sequence of severe pain → patchy paresis/atrophy/sensory loss → slow, often incomplete recovery.

This model unifies otherwise disparate observations: why NA recurs and starts earlier in SEPT9 carriers (stronger first hit); why bilateral and phrenic disease cluster with viral infection/HEV (a systemic third hit reaching multiple vulnerable segments); why nerve biopsies show inflammation (the effector mechanism); and why steroids help acutely (dampening the immune hit) but weakness responds mainly to time, rehabilitation, and — for fixed constrictions — surgery (repairing the structural end-lesion). The **directionality is clear**: genetic/mechanical predisposition is upstream and permissive; the immune trigger is the proximate initiator; hourglass constriction and axonal loss are the downstream lesions producing symptoms; chronic scapular dyskinesia is the tertiary consequence of incomplete regeneration and maladaptive motor control.

---

## Evidence Base

| PMID | Contribution | Supports finding |
|---|---|---|
| [16371410](https://pubmed.ncbi.nlm.nih.gov/16371410/) | 246-case clinical spectrum; three-phase pain; INA vs HNA | F001 |
| [21556032](https://pubmed.ncbi.nlm.nih.gov/21556032/) | SEPT9 in 55% of HNA families; triad pathophysiology | F002, F003 |
| [34854883](https://pubmed.ncbi.nlm.nih.gov/34854883/) | Septin-9 isoform-1 MAP motif; HNA mutations abrogate MT binding | F002 |
| [39428775](https://pubmed.ncbi.nlm.nih.gov/39428775/) | MD simulation: mutation impairs MT binding/bundling | F002 |
| [30019529](https://pubmed.ncbi.nlm.nih.gov/30019529/) | Childhood HNA, exon-2 duplication, platelet dysfunction | F002 |
| [36214185](https://pubmed.ncbi.nlm.nih.gov/36214185/) | Acute-phase US/MRN; HGCs 74%, muscle edema 91% | F003, F008 |
| [33823638](https://pubmed.ncbi.nlm.nih.gov/33823638/) | Incidence ~1/1000/yr; Gd-MRI/MRN confirmatory | F004, F008 |
| [38835178](https://pubmed.ncbi.nlm.nih.gov/38835178/) | Poor prognosis (25% unable to work at 3 yr); steroids first | F004 |
| [19321467](https://pubmed.ncbi.nlm.nih.gov/19321467/) | Prednisolone shortens pain (12.5 vs 20.5 d) | F004 |
| [39364568](https://pubmed.ncbi.nlm.nih.gov/39364568/) | Infectious trigger 26.3%; viral infection → bilateral (p=0.003) | F005 |
| [40534221](https://pubmed.ncbi.nlm.nih.gov/40534221/) | HEV NA with bilateral phrenic/diaphragm paralysis | F005 |
| [38657646](https://pubmed.ncbi.nlm.nih.gov/38657646/) | HEV → phrenic/diaphragmatic dysfunction | F005 |
| [36697215](https://pubmed.ncbi.nlm.nih.gov/36697215/) | >60% residual; rehab RCT (Δ8.60, p=0.044) | F006, F011 |
| [39402917](https://pubmed.ncbi.nlm.nih.gov/39402917/) | Motor-relearning strategy, not strength training | F006 |
| [8614534](https://pubmed.ncbi.nlm.nih.gov/8614534/) | Nerve biopsy: multifocal mononuclear infiltrates | F007 |
| [29925717](https://pubmed.ncbi.nlm.nih.gov/29925717/) | Feline inflammatory brachial plexus neuritis analogue | F007 |
| [32140911](https://pubmed.ncbi.nlm.nih.gov/32140911/) | Diagnosis is clinical | F008 |
| [32868098](https://pubmed.ncbi.nlm.nih.gov/32868098/) | Microneurolysis of HGCs (9/11 vs 3/13 recover) | Treatment |
| [38543940](https://pubmed.ncbi.nlm.nih.gov/38543940/) | Systematic review: PTS after COVID-19 vaccines | Etiology |
| [19588414](https://pubmed.ncbi.nlm.nih.gov/19588414/) | Cochrane: no RCTs; steroid open-label evidence | Treatment |

**Challenges / caveats in the evidence base.** The prednisolone and rehabilitation data come from observational studies and a single small RCT (n=47), respectively; the Cochrane review found no RCTs of drug therapy. HGC prevalence figures derive from modest imaging series. These limit the strength of causal treatment claims.

---

## Limitations and Knowledge Gaps

1. **No high-level RCT evidence for pharmacotherapy** — corticosteroid benefit rests on observational data ([PMID: 19588414](https://pubmed.ncbi.nlm.nih.gov/19588414/); [PMID: 19321467](https://pubmed.ncbi.nlm.nih.gov/19321467/)).
2. **Molecular profiling absent** — no NA-specific transcriptomic, proteomic, metabolomic, single-cell, or CRISPR/RNAi data were identified; the immune effector cells and antigens remain undefined.
3. **INA genetics undefined** — the "genetic predisposition" in idiopathic NA is inferred, not mapped; no GWAS/susceptibility loci established.
4. **Modifier genes, epigenetics, penetrance/expressivity metrics, carrier frequency** for SEPT9-HNA are not quantified.
5. **Mechanism of hourglass constriction** — the link from inflammation to focal constriction/torsion is described but not mechanistically demonstrated.
6. **No engineered animal model** recapitulating the full triad; the feline analogue is naturally occurring and incompletely characterized.
7. **Identifier confirmation** — MONDO/OMIM/Orphanet/ICD codes should be verified against current ontology releases before database ingestion.

---

## Proposed Follow-up Experiments / Actions

1. **Randomized controlled trial of early corticosteroids ± IVIG** in acute NA, powered for functional recovery and pain outcomes, to convert observational signals into Level-I evidence.
2. **Multi-omic characterization of NA nerve/biopsy and blood** (bulk + single-cell RNA-seq, proteomics) during acute attacks to identify immune effector populations, candidate autoantigens, and biomarkers — populating the currently empty molecular-profiling domain.
3. **SEPT9 genotype–phenotype and penetrance study** across HNA registries, including CNV analysis, to quantify penetrance, expressivity, and modifier loci; establish carrier frequency in gnomAD-linked cohorts.
4. **Prospective HEV-screening protocol** in all new NA cases (IgM/IgG + RNA + transaminases), especially with phrenic/bilateral involvement, to define the treatable-trigger fraction and guide etiologic management.
5. **Engineered Sept9 knock-in mouse (e.g., R106W)** with an inducible immune/inflammatory challenge to test the three-hit model and reproduce hourglass-constriction formation.
6. **Standardized imaging staging** (US/MRN) with defined timing to predict which HGCs spontaneously resolve versus require early neurolysis, refining the 6–12-month surgical decision window.
7. **Ontology reconciliation** — verify and finalize MONDO, OMIM, Orphanet, ICD-10/11, MeSH, HPO, GO, CL, and UBERON term assignments for knowledge-base ingestion.

---

*Report compiled from 8 confirmed findings and 47 reviewed papers across a 5-iteration autonomous investigation. Evidence types span human clinical cohorts, case-control and observational studies, one small RCT, nerve-biopsy histopathology, in vitro/computational molecular studies, and a naturally occurring veterinary analogue.*


## Artifacts

- [OpenScientist final report](Neuralgic_Amyotrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neuralgic_Amyotrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 40 |
| On topic | 16 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:40213747` (3 mentions) - Functional Restoring in Parsonage-Turner Syndrome With a Multimodal Rehabilitation Program: A Case Report.
  - shared terms: pain

Weighed against this report's own most characteristic terms: `hna`, `sept9`, `nerve`, `attack`, `trigger`, `pain`, `plexus`, `hev`, `genetic`, `phrenic`, `brachial`, `immune`, `involvement`, `ina`, `clinical`, `acute`, `mutation`, `chronic`, `multifocal`, `infection`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 23 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100053` (1 mention) - the report calls it "neuralgic amyotrophy"; MONDO calls it **anaphylaxis**
- `UBERON:0001824` (1 mention) - the report calls it "brachial plexus"; UBERON calls it **mucosa of larynx**
- `UBERON:0001379` (1 mention) - the report calls it "deltoid"; UBERON calls it **vastus lateralis**
- `NCIT:C198` (1 mention) - the report calls it "Prednisone"; NCIT calls it **Acetaminophen**
- `NCIT:C1409` (1 mention) - the report calls it "Corticosteroid"; NCIT calls it **Carbenicillin Indanyl Sodium**
- `NCIT:C579` (1 mention) - the report calls it "Immunoglobulin therapy"; NCIT calls it **Inorganic Chemical**
- `NCIT:C157810` (1 mention) - the report calls it "Neurolysis"; NCIT calls it **Cervical Cancer Surgery**
- `NCIT:C15296` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Isolated Chemotherapeutic Perfusion**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0003732` (1 mention), reported as "phrenic nerve" - UBERON does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005874` (1 mention) - the report calls it "microtubule cytoskeleton"; GO calls it **microtubule**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
