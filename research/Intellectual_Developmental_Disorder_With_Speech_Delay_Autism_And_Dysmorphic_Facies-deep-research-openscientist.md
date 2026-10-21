---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T20:30:12.347768'
end_time: '2026-10-19T20:52:44.924322'
duration_seconds: 1352.58
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Developmental Disorder with Speech Delay, Autism, and
    Dysmorphic Facies
  mondo_id: MONDO:0032864
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
citation_count: 8
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 9
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:31474762
  relevance_assessed: 9
  on_topic: 4
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 42
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 26
  labels_matching: 13
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0032864
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder with speech delay, autism,
      and dysmorphic facies
  - term_id: NCIT:C15381
    reported_labels:
    - Speech Therapy
    ontology_label: Quality Assurance
  - term_id: NCIT:C15349
    reported_labels:
    - Occupational Therapy
    ontology_label: Nutrition Research, Water
  - term_id: NCIT:C53555
    reported_labels:
    - Behavioral Therapy
    ontology_label: Luminal B Breast Carcinoma
  labels_variant: 9
  unresolvable_prefixes:
  - NCBIGene
  - OMIM
  - GARD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Developmental_Disorder_With_Speech_Delay_Autism_And_Dysmorphic_Facies-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Developmental_Disorder_With_Speech_Delay_Autism_And_Dysmorphic_Facies-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder with Speech Delay, Autism, and Dysmorphic Facies
- **MONDO ID:** MONDO:0032864 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder with Speech Delay, Autism, and Dysmorphic Facies** covering all of the
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

# Intellectual Developmental Disorder with Speech Delay, Autism, and Dysmorphic Facies (IDDSADF) — Comprehensive Disease Characteristics Report

**Disease:** Intellectual Developmental Disorder with Speech Delay, Autism, and Dysmorphic Facies (IDDSADF)
**MONDO ID:** MONDO:0032864 · **OMIM phenotype:** #618672 · **Causal gene:** *CNOT3* (19q13.42)
**Category:** Mendelian, autosomal dominant

---

## Summary

**Intellectual Developmental Disorder with Speech Delay, Autism, and Dysmorphic Facies (IDDSADF)** is a rare autosomal-dominant Mendelian neurodevelopmental disorder caused by heterozygous, predominantly *de novo* variants in **CNOT3** (CCR4-NOT transcription complex subunit 3; HGNC:7879; NCBIGene:4849; ENSG00000088038; UniProt O75175; 19q13.42). The disorder was first delineated as a discrete entity by Martin et al. (2019) in 16 probands ascertained through the Deciphering Developmental Disorders (DDD) study, each carrying *de novo* *CNOT3* variants [PMID: 31201375](https://pubmed.ncbi.nlm.nih.gov/31201375/). The phenotype combines global developmental delay/intellectual disability with speech delay, hypotonia, motor delay, autistic/behavioral features, relatively small stature, and a mild, non-recognizable facial dysmorphism; seizures are uncommon.

**CNOT3 is a scaffold subunit of the CCR4-NOT complex**, the principal cytoplasmic mRNA deadenylase that shortens poly(A) tails to trigger mRNA decay and that also contributes to transcription and protein ubiquitination. The gene is among the most mutation-intolerant in the human genome (gnomAD pLI = 1.0; LOEUF = 0.07; missense z = 4.65), and the balance of truncating and missense alleles, together with the authors' own conclusion, indicates that **haploinsufficiency** is the most likely mechanism. Reduced CNOT3 dosage is inferred to impair poly(A)-tail shortening and mRNA decay, dysregulating the post-transcriptional gene-expression programs that govern cell differentiation and identity — a role demonstrated across embryonic stem cells, pancreatic β-cells, hepatocytes, cardiomyocytes, and innate lymphoid cells in model systems. How this general post-transcriptional defect is translated into the specific neurodevelopmental phenotype in humans has not yet been directly demonstrated and remains the central knowledge gap.

**Clinically**, there is no targeted therapy. Diagnosis is molecular, achieved primarily through trio exome or genome sequencing; there is no biochemical biomarker and brain MRI findings are non-specific. Management is entirely supportive — early intervention, speech/occupational/physical therapy, special education, and behavioral support. An important pleiotropic observation is that *de novo* *CNOT3* variants have also been associated with moyamoya angiopathy, extending the clinical spectrum into later-onset cerebrovascular disease and warranting awareness in long-term follow-up.

> **Note on provenance / a corrected mis-identification.** Early in this investigation the MONDO ID was provisionally matched to KDM6B-related disorder (OMIM #618906). This was **retracted** upon ontology cross-referencing: MONDO:0032864 maps unambiguously to OMIM:618672 / MedGen C5231456 / GARD:0027947, and the causal gene is **CNOT3**, not KDM6B. All conclusions in this report refer to the CNOT3 disorder.

---

## 1. Disease Information

**Overview.** IDDSADF is a monogenic neurodevelopmental disorder characterized by global developmental delay and intellectual disability, prominent speech delay, autistic/behavioral features, hypotonia, relatively small stature, and mild facial dysmorphism without a readily recognizable gestalt. It is a "developmental disorder" in the DDD-study sense — a congenital-onset, non-progressive condition of brain development.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032864 |
| OMIM (phenotype) | #618672 |
| OMIM (gene *CNOT3*) | 604910 |
| MedGen | C5231456 (also 1684848) |
| GARD | 0027947 |
| Gene (NCBI) | 4849 |
| HGNC | 7879 |
| Ensembl | ENSG00000088038 |
| UniProt | O75175 |
| Cytoband | 19q13.42 |

**Synonyms / alternative names.** IDDSADF; CNOT3-related neurodevelopmental disorder; CNOT3-associated developmental disorder; intellectual developmental disorder with speech delay, autism, and dysmorphic facies.

**Source of information.** The entry is derived from **aggregated disease-level resources** (OMIM, Orphanet, HPO, MONDO) that themselves summarize **individual-patient data** from published cohorts — primarily the 16-proband DDD cohort of Martin et al. 2019 [PMID: 31201375](https://pubmed.ncbi.nlm.nih.gov/31201375/) plus subsequent case reports (Meyer et al. 2020 [PMID: 32720325](https://pubmed.ncbi.nlm.nih.gov/32720325/)).

---

## 2. Etiology

**Disease causal factor — genetic.** IDDSADF is caused by heterozygous, predominantly *de novo* pathogenic variants in *CNOT3*. There is no known environmental, infectious, or mechanistic (non-genetic) cause.

> *Martin et al. 2019:* "de novo variants in CNOT3 have emerged as a newly recognised cause of a developmental disorder." [PMID: 31201375](https://pubmed.ncbi.nlm.nih.gov/31201375/)

**Genetic risk factors.** The causal variants are the risk factor. *CNOT3* is extremely intolerant to loss-of-function and missense variation (gnomAD pLI = 1.0; LoF o/e = 0.022, LOEUF = 0.07; missense z = 4.65), so a single damaging allele is sufficient to cause disease (see §4, §6). No independent susceptibility loci or modifier genes have been established.

**Environmental risk factors.** None identified. Because most variants arise *de novo*, advanced parental age is a plausible but unproven generic contributor to *de novo* mutation rate (not specifically demonstrated for *CNOT3*).

**Protective factors.** None identified — no protective alleles or environmental protective exposures are known for this rare Mendelian disorder.

**Gene–environment interactions.** None documented. The disorder is essentially fully genetically determined given a pathogenic allele; variable expressivity (see §9) is more likely attributable to genetic background/stochastic developmental factors than to defined environmental modifiers.

---

## 3. Phenotypes

Curated HPO annotations for OMIM:618672, with cohort frequencies drawn from Martin et al. 2019 (n = 16) [PMID: 31201375](https://pubmed.ncbi.nlm.nih.gov/31201375/):

| Phenotype | HPO term | Type | Frequency (cohort) |
|---|---|---|---|
| Intellectual disability | HP:0001249 | Cognitive/behavioral | Core / consistent |
| Global developmental delay | HP:0001263 | Developmental | Core / consistent |
| Delayed ability to walk | HP:0031936 | Motor | 12/15 |
| Hypotonia | HP:0001252 | Neuromuscular sign | 10/16 |
| Autistic behavior | HP:0000729 | Behavioral | 7/16 |
| Prominent forehead | HP:0011220 | Dysmorphism | 5/16 |
| Malar flattening | HP:0000272 | Dysmorphism | 4/16 |
| Short philtrum | HP:0000322 | Dysmorphism | 4/16 |
| Strabismus | HP:0000486 | Ophthalmologic | 4/16 |
| Deeply set eye | HP:0000490 | Dysmorphism | 4/16 |
| Tapered finger | HP:0001182 | Skeletal/dysmorphism | 3/16 |
| Hypoplasia of corpus callosum | HP:0002079 | Neuroimaging | 2/12 |
| Speech delay | HP:0000750 | Developmental | Core (named in disease title) |
| Short stature / small stature | HP:0004322 | Growth | Frequent ("relatively small stature") |

**Phenotype characteristics.**
- **Age of onset:** infantile/congenital (HP:0003593) — developmental delay is evident in the first years of life.
- **Severity:** variable; intellectual disability ranges from mild to moderate–severe across the cohort.
- **Progression:** stable/non-progressive (a static encephalopathy of developmental origin), not neurodegenerative.
- **Facial dysmorphism:** mild and inconsistent — notably **no easily recognizable facial gestalt**; recurring features include anteverted nares, thin upper lip, and low-set eyebrows.

> *Martin et al. 2019:* "The most consistent phenotypic features seen in subjects with de novo variants in CNOT3 were hypotonia, relatively small stature, developmental delay, behavioural problems and intellectual disability. There is no easily recognisable facial phenotype, but some common dysmorphic features such as anteverted nares, thin upper lip and low set eyebrows were shared among some of the probands." [PMID: 31201375](https://pubmed.ncbi.nlm.nih.gov/31201375/)

**Quality-of-life impact.** Intellectual disability, speech delay, and autistic/behavioral features are the dominant drivers of long-term functional limitation, affecting communication, education, independent living, and social participation. Hypotonia and motor delay add early functional burden. No disease-specific QoL instruments (EQ-5D, SF-36, PROMIS) have been applied to this rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** *CNOT3* — CCR4-NOT transcription complex subunit 3 (aliases NOT3, NOT3H, LENG2). Gene OMIM 604910; HGNC:7879; NCBIGene:4849; ENSG00000088038; UniProt O75175; cytoband **19q13.42** (GRCh38 chr19:54,137,749–54,155,681).

**Pathogenic variants.**
- **Variant classes:** both protein-truncating variants (nonsense, frameshift, splice-site) and missense. In the defining cohort, **8/16 probands had protein-truncating variants and 8/16 had missense variants**; three of the missense cases shared an amino-acid substitution at the **same residue**, suggesting a functionally critical position.
- **Classification (ACMG/AMP):** ClinVar (queried 2026-10) lists **530 CNOT3 variant records — 183 pathogenic, 44 likely pathogenic, and 422 of uncertain significance (VUS)** (counts overlap across submissions/categories). Disease-causing alleles are heterozygous.
- **Allele frequency:** pathogenic alleles are absent/ultra-rare in gnomAD, consistent with strong negative selection and a largely *de novo* origin.
- **Somatic vs germline:** **germline** (constitutional), overwhelmingly *de novo*; rare parent-to-child transmission is documented (see §9).
- **Functional consequence:** **loss of function / haploinsufficiency.** Missense alleles at critical residues are inferred to be damaging/hypomorphic rather than gain-of-function.

> *Martin et al. 2019:* "Haploinsufficiency appears to be the most likely mechanism of action, with eight cases found to have protein-truncating variants. Of the other eight cases (all missense variants), three share an amino acid substitution at the same position which may therefore represent an important functional domain." [PMID: 31201375](https://pubmed.ncbi.nlm.nih.gov/31201375/)

**Constraint metrics (gnomAD).**

| Metric | *CNOT3* value | Interpretation |
|---|---|---|
| pLI | 1.0 | Fully LoF-intolerant |
| LoF o/e (LOEUF) | 0.022 (0.07) | 2 observed vs 89.4 expected LoF |
| LoF z | 7.84 | Extreme LoF constraint |
| Missense o/e | 0.657 | Depleted for missense |
| Missense z | 4.65 | Strong missense constraint |

These place *CNOT3* among the most constrained genes in the genome and directly support a dosage-sensitive, haploinsufficiency mechanism.

**Modifier genes.** None established. Variable expressivity within families (§9) implies genetic/stochastic modifiers whose identity is unknown.

**Epigenetic information.** No disease-specific DNA-methylation episignature has been reported for CNOT3-IDDSADF (unlike several chromatin-gene NDDs). Not applicable/unknown.

**Chromosomal abnormalities.** Most cases are SNV/indel; chromosomal microarray can detect 19q13.42 copy-number changes, but large structural rearrangements are not the typical mechanism.

---

## 5. Environmental Information

Not applicable. IDDSADF is a monogenic disorder with no established environmental, lifestyle, toxic, or infectious contributors. No gene–environment interaction has been demonstrated.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. A heterozygous *de novo* (rarely inherited) **loss-of-function or damaging missense variant arises in *CNOT3*** (19q13.42). *[demonstrated — variant data, Martin 2019]*
2. This **reduces functional CNOT3 protein to ~50%** (haploinsufficiency), because *CNOT3* is dosage-sensitive and LoF-intolerant (pLI = 1, LOEUF = 0.07). *[inferred from constraint + truncating/missense split]*
3. Reduced CNOT3 **impairs assembly/scaffolding of the CCR4-NOT deadenylase complex**, of which CNOT3 is a NOT-module scaffold subunit. *[demonstrated — CNOT3 is a defined scaffold subunit]*
4. Impaired CCR4-NOT function **reduces mRNA poly(A)-tail shortening (deadenylation)**, the rate-limiting step of bulk cytoplasmic mRNA decay. *[demonstrated — complex biochemistry]*
5. Defective deadenylation **stabilizes and dysregulates target mRNAs**, perturbing the post-transcriptional gene-expression programs that control **cell differentiation, maturation, and identity**. *[demonstrated in multiple cell types — ESC, β-cell, hepatocyte, ILC2]*
6. During neurodevelopment, this dysregulation **disrupts the timing and fidelity of neuronal differentiation and brain patterning**. *[inferred — not yet directly shown in human/mouse neurons]*
7. The result is **static, congenital brain dysfunction** manifesting as intellectual disability, speech delay, hypotonia, autistic/behavioral features, and mild dysmorphism. *[demonstrated — clinical cohort]*

**Branch (pleiotropy):** independently, *de novo* *CNOT3* variants **predispose to moyamoya angiopathy**, a later-onset large-artery occlusive cerebrovascular disease, implicating CNOT3-dependent post-transcriptional control in vascular as well as neural development. *[demonstrated — Pinard 2020]*

### Detail by category

**Molecular pathway.** The core lesion is in the **CCR4-NOT mRNA-deadenylation pathway** (cytoplasmic mRNA turnover / post-transcriptional regulation), not a classical signaling cascade (Wnt/MAPK/mTOR). CNOT3 also contributes to transcription and protein ubiquitination.

> *Kuba 2018:* "deadenylation is mostly executed by the CCR4-NOT complex. CCR4-NOT complex is a multi-subunit protein complex, which controls gene expression in the levels from transcription through mRNA deadenylation and protein ubiquitination. We had previously identified CNOT3, a scaffold subunit of the CCR4-NOT complex." [PMID: 29526923](https://pubmed.ncbi.nlm.nih.gov/29526923/)

**Cellular processes.** Loss of cell-identity maintenance and failure of proper maturation/differentiation; in some contexts, de-repression of senescence programs. CNOT3 knockdown stabilizes *CDKN1A*(p21)/*TP53* transcripts and induces cellular senescence hallmarks [PMID: 39823890](https://pubmed.ncbi.nlm.nih.gov/39823890/).

**Protein dysfunction.** Truncating variants delete functional domains / trigger nonsense-mediated decay (loss of function); recurrent same-residue missense variants likely disrupt a critical functional domain (hypomorphic loss of function). Net effect: reduced deadenylase scaffold function.

**Metabolic / biochemical abnormalities.** No specific enzyme deficiency or metabolite is measurable clinically; the "biochemical" defect is global, at the level of mRNA poly(A) metabolism rather than intermediary metabolism — so there is no diagnostic biomarker.

**Immune involvement.** Not a feature of the human disorder, though model work shows CNOT3 shapes innate lymphoid cell (ILC2) differentiation by destabilizing *Tbx21*/*Rorc* [PMID: 42118148](https://pubmed.ncbi.nlm.nih.gov/42118148/) — illustrating the breadth of CNOT3's identity-controlling function rather than a disease immunophenotype.

**Molecular profiling.** Functional studies (model organisms, see §15) show that *Cnot3* deletion increases mRNA stability of differentiation regulators and derails lineage programs; no human patient-tissue transcriptomic/proteomic signature has been published.

**Evidence that CNOT3-dependent deadenylation controls cell identity:**
> *Mostafa et al. 2020:* "CNOT3, a CCR4-NOT deadenylase complex subunit, is dysregulated in islets in diabetic db/db mice, and that it is essential for murine β cell maturation and identity." [PMID: 32859966](https://pubmed.ncbi.nlm.nih.gov/32859966/)

**GO / CL / UBERON suggestions.**
- GO biological process: mRNA deadenylation (GO:0000289); nuclear-transcribed mRNA poly(A) tail shortening (GO:0000290); regulation of mRNA stability (GO:0043488); nervous system development (GO:0007399); cell differentiation (GO:0030154).
- GO cellular component: CCR4-NOT complex (GO:0030014); cytoplasm (GO:0005737); nucleus (GO:0005634).
- CL cell types (inferred): neuron (CL:0000540); glutamatergic/GABAergic neurons; neural progenitor/stem cell (CL:0000047).
- UBERON: brain (UBERON:0000955); cerebral cortex (UBERON:0000956); corpus callosum (UBERON:0002336).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary organ is the **brain** (central nervous system; body system = nervous system). Secondary/associated involvement: ophthalmologic (strabismus), musculoskeletal (hypotonia, tapered fingers, small stature), craniofacial skeleton (mild dysmorphism). The pleiotropic branch involves the **cerebral arteries** (moyamoya angiopathy).

**Tissue / cell level.** Affected tissue is **neural (nervous) tissue**. Inferred target populations: neurons and neural progenitor cells during corticogenesis; in the moyamoya branch, arterial **vascular smooth muscle / endothelium**. No specific neuronal subtype has been proven as the locus of disease.

**Subcellular level.** The molecular machinery localizes to the **cytoplasm** (site of CCR4-NOT–mediated deadenylation; GO:0005737) with additional **nuclear** functions (GO:0005634). The relevant subcellular process is cytoplasmic mRNA turnover rather than organelle pathology.

**Localization & lateralization.** Brain involvement is **bilateral/global**. Structural neuroimaging is non-specific — occasional thin/hypoplastic corpus callosum (UBERON:0002336), enlarged cisterna magna, and delayed myelination.
UBERON terms: brain (UBERON:0000955), cerebral cortex (UBERON:0000956), corpus callosum (UBERON:0002336), cerebral artery (UBERON:0001629).

---

## 8. Temporal Development

**Onset.** Congenital/infantile; developmental delay and hypotonia are typically apparent in the first year of life. Onset pattern is **insidious/chronic** (developmental), not acute.

**Progression.** **Static (non-progressive)** encephalopathy — intellectual disability and core features are stable over time rather than degenerative. Disease duration is **chronic/lifelong**.

**Patterns.** No remission or relapsing course for the neurodevelopmental features. The **critical period** for intervention is early childhood (early-intervention and therapy windows for language, motor, and behavioral development). The **moyamoya branch** introduces a distinct later-onset, potentially progressive cerebrovascular time-course requiring separate surveillance.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare. Precise prevalence/incidence are **not established**; the literature comprises on the order of dozens of reported individuals (16 in the defining DDD cohort plus subsequent cases). No registry-based prevalence figures are available.

**Inheritance pattern.** **Autosomal dominant** (HP:0000006). The overwhelming majority of cases are **de novo**; Meyer et al. 2020 reported the **first two unrelated families with parent-to-child transmission**, establishing that the allele can be inherited and showing **substantial intra-familial phenotypic variability (variable expressivity)**.

> *Meyer et al. 2020:* "We report for the first time autosomal dominant transmissions of the CNOT3-associated developmental disorder in two unrelated families. The clinical characteristics in our patients match the IDDSADF features reported so far and suggest substantial variability of the phenotype within the same family." [PMID: 32720325](https://pubmed.ncbi.nlm.nih.gov/32720325/)

**Penetrance / expressivity.** Penetrance appears high for a neurodevelopmental phenotype but **expressivity is variable**, even within families. Genetic anticipation: not applicable (not a repeat-expansion disorder). Germline mosaicism: plausible for *de novo* disorders but not specifically documented for *CNOT3*. Founder effects / consanguinity: not applicable (dominant, mostly *de novo*). Carrier frequency: not applicable (no asymptomatic-carrier recessive state; the disease is dominant).

**Population demographics.** No ethnic predilection, geographic clustering, or variant-specific geographic distribution is known. Sex ratio is not established (no strong sex bias reported). Age distribution: diagnosed in childhood.

**Pleiotropy.** *De novo* *CNOT3* variants also predispose to **moyamoya angiopathy**, grouping *CNOT3* with chromatin/developmental NDD genes (*CHD4*, *SETD5*) whose pleiotropy extends into cerebrovascular disease.

> *Pinard et al. 2020:* "We identified four de novo variants in three genes not previously associated with MMA: CHD4, CNOT3, and SETD5… these data expand the spectrum of phenotypic pleiotropy due to alterations of CHD4, CNOT3, and SETD5 beyond DD to later onset disease in the cerebrovascular arteries." [PMID: 31474762](https://pubmed.ncbi.nlm.nih.gov/31474762/)

---

## 10. Diagnostics

**Diagnostic approach — molecular.** Diagnosis rests on identifying a heterozygous pathogenic/likely-pathogenic *CNOT3* variant. The disorder was itself discovered through exome sequencing in the DDD study.

> *Martin et al. 2019:* "As a result of exome-based sequencing work performed by the DDD study, de novo variants in CNOT3 have emerged as a newly recognised cause of a developmental disorder." [PMID: 31201375](https://pubmed.ncbi.nlm.nih.gov/31201375/)

| Modality | Utility for IDDSADF |
|---|---|
| **Trio exome sequencing (WES)** | **Primary/highest-yield** — detects *de novo* SNV/indel; trio design confirms *de novo* status |
| Genome sequencing (WGS) | Alternative; adds non-coding/structural detection |
| ID/ASD/epilepsy multigene panels (incl. *CNOT3*) | Targeted alternative |
| Single-gene *CNOT3* testing | For confirmation or familial cascade testing |
| Chromosomal microarray (CMA) | Detects 19q13.42 CNV; most cases are SNV/indel (lower yield) |
| Karyotype / FISH | Low yield (not a translocation disorder) |
| mtDNA / repeat-expansion testing | Not applicable |

**Clinical / laboratory tests.** No specific blood, urine, or enzyme biomarker exists. Routine metabolic workup is non-diagnostic.

**Imaging.** Brain MRI is **non-specific**: occasional thin/hypoplastic corpus callosum, enlarged cisterna magna, delayed myelination. In patients with cerebrovascular symptoms, MRA/angiography should be considered to evaluate for moyamoya.

**Omics-based diagnostics.** No validated RNA/proteomic/metabolomic/methylation diagnostic signature is currently available for CNOT3-IDDSADF.

**Clinical criteria / differential diagnosis.** There are no formal consensus diagnostic criteria; diagnosis is gene-based. The non-specific phenotype overlaps broadly with other monogenic intellectual-disability/autism syndromes (e.g., chromatin-regulator and transcription/mRNA-regulation NDDs), so molecular testing is required to distinguish them.

**Screening.** No population newborn or carrier screening exists or is indicated (dominant, mostly *de novo*, ultra-rare).

---

## 11. Outcome / Prognosis

**Survival / mortality.** The core neurodevelopmental disorder is **not life-limiting** per se; no disease-specific mortality or reduced-life-expectancy data are established. Life expectancy is presumed near-normal in the absence of serious complications.

**Morbidity / function.** The principal long-term burden is **cognitive and communicative disability** — intellectual disability and speech delay affecting education, independence, and social participation — plus behavioral/autistic features. Hypotonia and motor delay contribute early functional impairment. No standardized QoL measures have been applied.

**Disease course / complications.** Core features are static. The most clinically significant potential complication is the pleiotropic **moyamoya cerebrovascular disease** (risk of TIA/stroke), which, where present, carries its own morbidity and warrants neurovascular surveillance and management.

**Recovery potential.** The developmental disability is permanent; however, **functional gains are achievable with early intervention and therapies**. Prognosis is otherwise variable, mirroring the variable expressivity of the phenotype.

**Prognostic factors / biomarkers.** No validated molecular prognostic biomarker. Genotype (truncating vs specific missense) has not been shown to reliably predict severity; variable expressivity is observed even within a family at a shared variant.

---

## 12. Treatment

**There is no targeted or disease-modifying therapy.** Management is entirely **supportive and multidisciplinary**, directed at the symptoms.

| Intervention | Purpose | NCIT suggestion |
|---|---|---|
| Early-intervention developmental programs | Maximize developmental trajectory | NCIT:C15317 (Rehabilitation) |
| Speech-language therapy | Address speech delay / communication | NCIT:C15381 (Speech Therapy) |
| Occupational therapy | Fine motor, daily-living skills | NCIT:C15349 (Occupational Therapy) |
| Physical therapy | Hypotonia, motor delay | NCIT:C15344 (Physical Therapy) |
| Special education / IEP support | Learning and cognition | — |
| Behavioral / ASD-directed support | Autistic/behavioral features | NCIT:C53555 (Behavioral Therapy) |
| Ophthalmology (strabismus) | Correct strabismus | — |
| Neurovascular management (if moyamoya) | Stroke prevention/treatment | NCIT:C15329 (Surgical procedure, e.g., revascularization) |

**Pharmacotherapy.** No gene-specific drug. Symptomatic psychotropic/behavioral medications may be used per standard ASD/ADHD/behavioral practice; no pharmacogenomic guidance is specific to *CNOT3*.

**Advanced therapeutics (gene/cell/RNA/targeted/immuno).** None approved or in trials for this disorder.

**Experimental treatments.** No disease-specific clinical trials (no NCT identifiers) are known for CNOT3-IDDSADF.

**Treatment outcomes / strategy.** No response-rate data; care follows general neurodevelopmental-disability pathways with individualized, combination (multidisciplinary) support. Personalized medicine is currently limited to accurate molecular diagnosis, genetic counseling, and surveillance for pleiotropic complications.

---

## 13. Prevention

- **Primary prevention:** Not possible for *de novo* disease. Where a variant is inherited (rare), **genetic counseling** informs recurrence risk (up to 50% transmission for an affected/carrier parent).
- **Secondary prevention:** Early developmental surveillance and **early-intervention therapy** to optimize outcomes once diagnosed.
- **Tertiary prevention:** Monitoring for and managing complications — notably **neurovascular surveillance for moyamoya** in symptomatic individuals, plus management of strabismus and behavioral issues.
- **Genetic screening / reproductive options:** For families with an identified variant, options include prenatal diagnosis and preimplantation genetic testing (PGT); cascade testing of at-risk relatives where transmission has occurred.
- **Immunization / public-health / environmental measures:** Not applicable.
- **Counseling:** Genetic counseling is central — explaining *de novo* origin, low but non-zero recurrence (germline mosaicism cannot be excluded), and variable expressivity.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *CNOT3* is deeply conserved. Mouse ortholog *Cnot3* (NCBIGene:232791, chromosome 7); *Drosophila* ortholog *Not3*. NCBI Taxon: *Homo sapiens* (9606), *Mus musculus* (10090), *Drosophila melanogaster* (7227).
- **Natural disease in other species:** No naturally occurring companion-animal or wildlife analog of IDDSADF is catalogued (e.g., in OMIA). CNOT3 biology in animals is known almost entirely from engineered/conditional models (see §15), not spontaneous disease.
- **Comparative biology / conservation:** CNOT3's role as a conserved regulator of development and tissue identity is demonstrated across *Drosophila* and mouse (e.g., conserved regulator of heart function). This evolutionary conservation supports the human disease mechanism.

> *Kuba 2018:* "We had previously identified CNOT3, a scaffold subunit of the CCR4-NOT complex, as a conserved regulator of heart function in Drosophila and mouse." [PMID: 29526923](https://pubmed.ncbi.nlm.nih.gov/29526923/)

- **Transmission / zoonosis:** Not applicable (genetic disorder).

---

## 15. Model Organisms

*Cnot3* is **essential and evolutionarily conserved**; constitutive knockout is embryonic lethal, so disease modeling uses **conditional/tissue-specific** approaches. There is currently **no published neuron-specific or brain-conditional mouse model** directly recapitulating IDDSADF — a key gap.

| Model system | Manipulation | Phenotype / finding | PMID |
|---|---|---|---|
| Mouse embryonic stem cells | *Cnot3* conditional deletion (CRISPR) | Disrupted pluripotency and differentiation; platform for dissecting CCR4-NOT in cell fate | [37824068](https://pubmed.ncbi.nlm.nih.gov/37824068/) |
| Mouse β-cell–specific KO | *Cnot3* deletion in β-cells | Loss of β-cell identity/maturation, increased mRNA stability, diabetes | [32859966](https://pubmed.ncbi.nlm.nih.gov/32859966/) |
| Mouse liver-specific KO (Cnot3-LKO) | *Cnot3* deletion in liver | Impaired hepatic maturation, hepatitis/necrosis, anemia, transient alopecia | [31630801](https://pubmed.ncbi.nlm.nih.gov/31630801/) |
| *Drosophila* + mouse (heart) | *Cnot3/Not3* loss | Conserved regulator of heart function; links poly(A) shortening to *Atg7*/p53 transcriptional control | [29526923](https://pubmed.ncbi.nlm.nih.gov/29526923/) |
| Mouse ILC2 conditional KO | *Cnot3* deletion in ILC2 | Aberrant T-bet/RORγt; destabilization of *Tbx21*/*Rorc* — identity control | [42118148](https://pubmed.ncbi.nlm.nih.gov/42118148/) |

> *Suzuki et al. 2020:* "in mice lacking a Cnot3 gene, which encodes an essential component of the CCR4-NOT deadenylase complex in liver (Cnot3-LKO mice), the liver does not mature properly, resulting in various pathologies such as hepatitis, hepatic necrosis, and anemia." [PMID: 31630801](https://pubmed.ncbi.nlm.nih.gov/31630801/)

**Phenotype recapitulation.** Across tissues the unifying theme is **failure of cell maturation/identity** upon *Cnot3* loss — strongly supporting the human haploinsufficiency mechanism — but **none of these models is neural**, so they recapitulate the *molecular* mechanism rather than the *neurodevelopmental phenotype*. **Model resources:** MGI (mouse *Cnot3*), FlyBase (*Not3*), IMPC/IMSR.

---

## Mechanistic Model / Interpretation

```
 de novo CNOT3 LoF / damaging missense variant (19q13.42)
            │  [demonstrated: variant data, Martin 2019]
            ▼
 ~50% functional CNOT3  (haploinsufficiency; pLI=1, LOEUF=0.07, mis_z=4.65)
            │  [inferred from constraint + 8 truncating / 8 missense split]
            ▼
 Impaired CCR4-NOT deadenylase assembly (CNOT3 = NOT-module scaffold)
            │  [demonstrated: complex biochemistry, Kuba 2018]
            ▼
 Reduced mRNA poly(A)-tail shortening → impaired mRNA decay
            │  [demonstrated]
            ▼
 Dysregulated post-transcriptional programs → loss of cell maturation/identity
            │  [demonstrated in ESC, β-cell, hepatocyte, ILC2 models]
            ▼
 ┌──────────────────────────────┐      ┌───────────────────────────────┐
 │ Disrupted neurodevelopment   │      │ Branch: cerebral artery        │
 │ (inferred — not shown in     │      │ dysregulation → MOYAMOYA        │
 │ neurons)                     │      │ angiopathy [demonstrated,       │
 │                              │      │ Pinard 2020]                   │
 └──────────────┬───────────────┘      └───────────────────────────────┘
                ▼
 IDDSADF: ID, speech delay, hypotonia, motor delay,
 autistic/behavioral features, mild dysmorphism, small stature
 [demonstrated — clinical cohort]
```

The coherent story: a dosage-sensitive, ubiquitously required post-transcriptional regulator is reduced by ~half; this does not abolish any single pathway but subtly degrades the **fidelity and timing of cell-fate programs**. In the developing brain this manifests as a static encephalopathy; in cerebral vasculature it can later manifest as moyamoya. The strongest, directly demonstrated links are at the molecular/cellular level (steps 1–5); the neuron-specific translation of the defect (step 6) is currently **inferred by analogy** from non-neural models and from the clinical phenotype.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | How it supports / challenges |
|---|---|---|---|
| [31201375](https://pubmed.ncbi.nlm.nih.gov/31201375/) | *De novo variants in CNOT3 cause a variable neurodevelopmental disorder* | **Defining cohort** | Establishes gene–disease link (16 probands), phenotype spectrum, 8 truncating/8 missense, haploinsufficiency conclusion |
| [32720325](https://pubmed.ncbi.nlm.nih.gov/32720325/) | *Inherited cases of CNOT3-associated IDDSADF* | Inheritance | First AD transmission; names IDDSADF/OMIM #618672; variable expressivity |
| [31474762](https://pubmed.ncbi.nlm.nih.gov/31474762/) | *Pleiotropy… extends to moyamoya angiopathy* | Pleiotropy/prognosis | CNOT3 *de novo* variants predispose to moyamoya — expands spectrum |
| [29526923](https://pubmed.ncbi.nlm.nih.gov/29526923/) | *poly(A) shortening in heart function* | Mechanism | CNOT3 = CCR4-NOT scaffold; conserved *Drosophila*/mouse regulator |
| [32859966](https://pubmed.ncbi.nlm.nih.gov/32859966/) | *Loss of β-cell identity… CNOT3 deadenylation* | Mechanism/model | CNOT3-dependent deadenylation essential for maturation/identity |
| [31630801](https://pubmed.ncbi.nlm.nih.gov/31630801/) | *Insufficient liver maturation (Cnot3-LKO)* | Model | Conditional mouse KO; Cnot3 essential, maturation failure |
| [37824068](https://pubmed.ncbi.nlm.nih.gov/37824068/) | *Ccr4-Not in pluripotency and differentiation* | Model/methods | ESC conditional deletion disrupts pluripotency/differentiation |
| [39823890](https://pubmed.ncbi.nlm.nih.gov/39823890/) | *CNOT3 knockdown and senescence* | Mechanism | Links CNOT3 loss to p21/p53 mRNA stabilization and senescence |
| [42118148](https://pubmed.ncbi.nlm.nih.gov/42118148/) | *CNOT3 supports ILC2 differentiation* | Mechanism | CNOT3 destabilizes *Tbx21*/*Rorc* — identity control |

Constraint metrics (gnomAD) and ClinVar variant counts were queried directly during the investigation and corroborate the haploinsufficiency mechanism and the pathogenic-variant landscape.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** The clinical phenotype rests largely on one 16-proband cohort plus scattered cases; frequencies are imprecise and prevalence is unknown.
2. **No neural model.** All functional *Cnot3* models are non-neural (ESC, β-cell, liver, heart, ILC2). The critical step linking CNOT3 haploinsufficiency to disrupted human neurodevelopment (step 6) is **inferred, not demonstrated**.
3. **No patient-tissue omics.** No transcriptomic/proteomic/methylation signature from patient neural tissue exists; there is no episignature and no biomarker.
4. **Genotype–phenotype correlation unresolved.** Variable expressivity (even intra-familial) is unexplained; modifier genes are unknown. It is unclear whether specific missense alleles are partial loss-of-function, dominant-negative, or truly equivalent to truncating alleles.
5. **Pleiotropy scope.** The penetrance and predictors of moyamoya in CNOT3 variant carriers are not quantified; surveillance guidelines are not evidence-based.
6. **No therapeutics.** No disease-specific trials, drugs, or outcome data.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a brain-conditional / heterozygous *Cnot3* mouse** (e.g., *Nestin-Cre* or neuron-specific heterozygous model) and phenotype for learning/memory, sociability, and cortical development — to directly test step 6 of the causal chain.
2. **Patient iPSC-derived neurons/organoids** with CNOT3 LoF and recurrent missense alleles; perform RNA-seq + poly(A)-tail profiling (nanopore direct RNA) to identify stabilized neural target mRNAs and build a candidate molecular signature.
3. **Allelic-series functional assays** (truncating vs recurrent missense) to classify missense alleles as LoF/hypomorph/dominant-negative and establish genotype–phenotype rules.
4. **Expand and deep-phenotype the cohort** via GeneMatcher/registry to refine HPO frequencies, define prevalence, and quantify moyamoya penetrance → inform surveillance guidelines.
5. **Search for a DNA-methylation episignature** in patient blood to enable VUS reclassification (as achieved for many chromatin-gene NDDs).
6. **Draft consensus management/surveillance recommendations**, including neurovascular imaging criteria for the moyamoya branch.

---

## Consensus Answer

Intellectual Developmental Disorder with Speech Delay, Autism, and Dysmorphic Facies (IDDSADF; MONDO:0032864, OMIM #618672) is a rare autosomal-dominant Mendelian neurodevelopmental disorder caused by heterozygous, mostly *de novo* loss-of-function or damaging missense variants in **CNOT3** (19q13.42), a haploinsufficiency-sensitive scaffold subunit of the CCR4-NOT mRNA deadenylase complex. Reduced CNOT3 dosage impairs poly(A)-tail shortening and mRNA decay, dysregulating post-transcriptional programs that control cell differentiation and identity, producing variable intellectual disability/developmental delay with speech delay, hypotonia, motor delay, autistic/behavioral features, mild non-specific dysmorphism and small stature (seizures uncommon), with a subset developing moyamoya cerebrovascular disease. Management is entirely supportive with no targeted therapy, and diagnosis rests on trio exome/genome sequencing.


## Artifacts

- [OpenScientist final report](Intellectual_Developmental_Disorder_With_Speech_Delay_Autism_And_Dysmorphic_Facies-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Developmental_Disorder_With_Speech_Delay_Autism_And_Dysmorphic_Facies-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:31474762`: "We identified four de novo variants in three genes not previously associated with MMA: CHD4, CNOT3, and SETD5… these data expand the spectrum of phenotypic pleiotropy due to alterations of CHD4, CNOT3, and SETD5 beyond DD to later onset disease in the cerebrovascular arteries."
  - closest text in source: "RESULTS: We identified four de novo variants in three genes not previously associated with MMA: CHD4, CNOT3, and SETD5"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 26 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032864` (4 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder with speech delay, autism, and dysmorphic facies**
- `NCIT:C15381` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Quality Assurance**
- `NCIT:C15349` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Nutrition Research, Water**
- `NCIT:C53555` (1 mention) - the report calls it "Behavioral Therapy"; NCIT calls it **Luminal B Breast Carcinoma**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002079` (1 mention) - the report calls it "Hypoplasia of corpus callosum"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplasia of corpus callosum" among its other names
- `HP:0004322` (1 mention) - the report calls it "Short stature / small stature"; HP calls it **Short stature**
- `HP:0003593` (1 mention) - the report calls it "Age of onset:** infantile/congenital"; HP calls it **Infantile onset**
- `GO:0000289` (1 mention) - the report calls it "GO biological process: mRNA deadenylation"; GO calls it **nuclear-transcribed mRNA poly(A) tail shortening**, and lists "3' to 5' mRNA deadenylation" among its other names
- `GO:0030014` (1 mention) - the report calls it "GO cellular component: CCR4-NOT complex"; GO calls it **CCR4-NOT complex**
- `UBERON:0000955` (2 mentions) - the report calls it "UBERON: brain"; UBERON calls it **brain**, and lists "the brain" among its other names
- `HP:0000006` (1 mention) - the report calls it "Autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names
- `NCIT:C15317` (1 mention) - the report calls it "Rehabilitation"; NCIT calls it **Second-Look Surgery**, and lists "Reoperation" among its other names
- `NCIT:C15344` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **UV Light Therapy**, and lists "UV Phototherapy" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `NCBIGene`, `OMIM`, `GARD`.