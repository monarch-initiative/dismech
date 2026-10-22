---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T20:30:12.343475'
end_time: '2026-10-19T20:44:31.853345'
duration_seconds: 859.51
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cataract 40
  mondo_id: MONDO:0010544
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
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 15
  relevance_assessed: 12
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 26
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 5
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0010544
    reported_labels:
    - MONDO
    ontology_label: cataract 40
  - term_id: HP:0000482
    reported_labels:
    - Common
    ontology_label: Microcornea
  - term_id: HP:0000568
    reported_labels:
    - Common
    ontology_label: Microphthalmia
  - term_id: HP:0000486
    reported_labels:
    - Common
    ontology_label: Strabismus
  - term_id: HP:0000639
    reported_labels:
    - Common sequela of deprivation
    ontology_label: Nystagmus
  - term_id: HP:0001999
    reported_labels:
    - Classic NHS
    ontology_label: Abnormal facial shape
  - term_id: HP:0001249
    reported_labels:
    - Up to ~30% of affected males
    ontology_label: Intellectual disability
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cataract_40-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cataract_40-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 40
- **MONDO ID:** MONDO:0010544 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cataract 40** covering all of the
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

# Cataract 40 (CTRCT40): A Comprehensive Disease Characteristics Report

**Disease:** Cataract 40 (CTRCT40)
**MONDO ID:** MONDO:0010544 · **OMIM:** #302200 · **Locus:** Xp22.13 · **Gene:** *NHS*
**Category:** Mendelian, X-linked
**Report compiled:** 2026-10-19 (5-iteration autonomous investigation; 9 confirmed findings; 25 papers reviewed)

---

## Summary

**Cataract 40 (CTRCT40; OMIM #302200, MONDO:0010544) is a rare, X-linked congenital cataract caused by loss-of-function or rearrangement-associated lesions of the *NHS* (Nance-Horan Syndrome) gene at Xp22.13.** It represents the *isolated-cataract end* of an allelic spectrum whose severe, syndromic counterpart is Nance-Horan syndrome (NHS; OMIM #302350), which adds dental anomalies (screwdriver/peg-shaped incisors), facial dysmorphism, and intellectual disability (in up to ~30% of affected males). The distinction is primarily molecular and quantitative: classic NHS results from nonsense mutations and small deletions producing frank protein loss of function, whereas isolated X-linked congenital cataract (CTRCT40) can arise from non-recurrent structural rearrangements that cause aberrant *NHS* transcription ([PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/)).

Mechanistically, *NHS* encodes an actin-cytoskeleton scaffolding protein. Recent cell-biological work demonstrates that the NHS protein organizes the WAVE Regulatory Complex (assembling a "WAVE Shell Complex") and remodels WAVE/N-WASP nucleation-promoting-factor complexes to control Arp2/3-dependent actin nucleation and cell-migration persistence ([PMID: 42595116](https://pubmed.ncbi.nlm.nih.gov/42595116/)). Haploinsufficiency of *NHS* — accentuated in heterozygous females by skewed X-chromosome inactivation — is concluded to drive the clinical phenotype ([PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/)). The inferred downstream consequence is disordered lens epithelial/fiber-cell polarity and cytoskeletal organization, producing loss of lens transparency, i.e., bilateral congenital cataract. Hemizygous males are consistently and severely affected; heterozygous females show variable, often milder, lens opacities.

Clinically, there is **no pharmacologic or gene-based therapy**. Management is **early surgical lensectomy** with optical rehabilitation, performed within a developmental "critical period" (ideally before ~6 weeks for unilateral and ~10 weeks for bilateral cataract; a bilinear model identifies a critical age of ~14 weeks for dense bilateral cataract), followed by rigorous amblyopia therapy. The principal determinant of lifelong visual prognosis is **deprivation amblyopia**, and common post-surgical complications include nystagmus, strabismus, glaucoma, and posterior capsule/visual-axis opacification ([PMID: 22383071](https://pubmed.ncbi.nlm.nih.gov/22383071/), [PMID: 19084444](https://pubmed.ncbi.nlm.nih.gov/19084444/)). Prevention is genetic — molecular diagnosis of the *NHS* variant, cascade carrier testing in females, newborn red-reflex screening, and reproductive counseling.

---

## 1. Disease Information

**Overview.** Cataract 40 is a Mendelian, X-linked congenital cataract. It is the **isolated-cataract phenotype within the Nance-Horan spectrum**, caused by lesions in the *NHS* gene. In affected individuals the principal (often sole) manifestation is bilateral congenital lens opacity; when extra-ocular features (dental, facial, neurodevelopmental) are present and prominent, the diagnosis shifts toward classic Nance-Horan syndrome, reflecting an allelic continuum rather than two unrelated disorders ([PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #302200 (Cataract 40, X-linked; CTRCT40) |
| OMIM (allelic syndromic form) | #302350 (Nance-Horan syndrome) |
| MONDO | MONDO:0010544 |
| Gene | *NHS* (Nance-Horan Syndrome gene) |
| Cytogenetic locus | Xp22.13 |
| Orphanet (NHS) | ORPHA:627 |
| Inheritance | X-linked dominant |

**Synonyms / alternative names.** X-linked congenital cataract; isolated X-linked cataract; CTRCT40; *NHS*-related cataract; (within the allelic spectrum) Nance-Horan syndrome / cataract-dental syndrome / mesiodens-cataract syndrome.

**Information source.** The evidence base is derived primarily from **aggregated disease-level resources** (OMIM, Orphanet) and **individual case reports / small family pedigrees** in the primary literature, supplemented by functional cell-biology studies. There is no large EHR-derived cohort specific to CTRCT40; it is a rare, frequently under-diagnosed condition ([PMID: 39858638](https://pubmed.ncbi.nlm.nih.gov/39858638/)).

---

## 2. Etiology

**Primary cause — genetic.** CTRCT40 is a **monogenic germline disorder** caused by pathogenic variants or structural rearrangements affecting the *NHS* gene at Xp22.13. There is no environmental or infectious etiology. The two mechanistic routes within the spectrum are:

1. **Loss-of-function point/small variants** (nonsense, frameshift, small deletions) → classic Nance-Horan syndrome end of the spectrum.
2. **Non-recurrent structural rearrangements** causing aberrant *NHS* transcription → isolated X-linked congenital cataract (CTRCT40 end) ([PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/)).

> "Isolated X-linked congenital cataract is caused by non-recurrent rearrangement-associated aberrant NHS transcription." ([PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/))

**Genetic risk factors.** The causal locus is *NHS* itself. In **females**, phenotypic expression and severity are governed by **X-chromosome inactivation (XCI)** patterns; skewed (non-random) XCI >85% was documented in an affected female carrier of a 0.52 Mb Xp22.13 microdeletion, correlating with reduced *NHS* expression and symptomatic disease versus her unaffected mother ([PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/)). Balanced X;autosome translocations [t(X;19), t(X;1)] that disrupt *NHS*, combined with skewed XCI, can render females affected ([PMID: 28922055](https://pubmed.ncbi.nlm.nih.gov/28922055/)).

**Environmental / lifestyle / infectious risk factors.** **Not applicable.** CTRCT40 is a Mendelian germline disorder; its occurrence is not modulated by toxins, radiation, smoking, diet, or infectious agents. (These factors are relevant to acquired/age-related cataract, not to this monogenic entity.)

**Protective factors.** No genetic or environmental protective factors are established for the lens-opacity phenotype itself. In female carriers, **favorably skewed XCI** (preferential inactivation of the mutant X) would be expected to reduce expression, functioning as an endogenous modifier rather than a classical protective allele.

**Gene–environment interactions.** None demonstrated. The only well-supported "interaction" is the **gene–epigenetic interaction** between the *NHS* lesion and X-inactivation choice in females, which determines expressivity.

---

## 3. Phenotypes

**Core phenotype:** bilateral congenital cataract (dense, often total) causing profound early visual deprivation.

| Phenotype | Type | Onset | Severity | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Bilateral congenital cataract | Clinical sign / physical | Congenital | Severe (males); mild–moderate (females) | Obligate in affected males | HP:0000519 (Congenital cataract) / HP:0000518 (Cataract) |
| Microcornea | Physical | Congenital | Variable | Common | HP:0000482 |
| Microphthalmia | Physical | Congenital | Variable | Common | HP:0000568 |
| Congenital ptosis | Physical | Congenital | Variable | Reported in families | HP:0000508 |
| Strabismus | Clinical sign | Infancy | Variable | Common | HP:0000486 |
| High myopia | Lab/refractive | Childhood | Variable | Reported | HP:0011003 |
| Nystagmus (secondary) | Clinical sign | Infancy | — | Common sequela of deprivation | HP:0000639 |
| Screwdriver/peg-shaped incisors, dental anomalies | Physical | Childhood (dentition) | Syndromic end | ~Classic NHS | HP:0006077 / HP:0000705 |
| Facial dysmorphism | Physical | Congenital | Syndromic end | Classic NHS | HP:0001999 |
| Intellectual disability | Behavioral/cognitive | Childhood | Variable | Up to ~30% of affected males | HP:0001249 |

**Supporting evidence.**

> "The Nance-Horan syndrome is an X-linked disorder characterized by congenital cataract, facial features, microcornea, microphthalmia, and dental anomalies" ([PMID: 28922055](https://pubmed.ncbi.nlm.nih.gov/28922055/))

> "up to 30% of the affected males have intellectual disability" ([PMID: 28922055](https://pubmed.ncbi.nlm.nih.gov/28922055/))

> "All affected members exhibited congenital cataracts, congenital ptosis, strabismus, high myopia as well as dental and facial anomalies" ([PMID: 39994540](https://pubmed.ncbi.nlm.nih.gov/39994540/))

**Characteristics.** Onset is **congenital**; severity is **severe in hemizygous males** (bilateral dense opacity → profound vision loss) and **mild-to-variable in heterozygous females** (sometimes isolated, subtle lens opacities). The lens opacity itself is **stable/non-progressive** structurally, but the *visual* consequence is **progressive and irreversible** if untreated, because form deprivation during the critical period produces amblyopia.

**Quality-of-life impact.** Untreated bilateral congenital cataract is among the leading causes of lifelong childhood blindness, with severe effects on education, employment, and independent living. Even after successful surgery, residual amblyopia, nystagmus, strabismus, and glaucoma degrade visual acuity and quality of life ([PMID: 22383071](https://pubmed.ncbi.nlm.nih.gov/22383071/), [PMID: 40780670](https://pubmed.ncbi.nlm.nih.gov/40780670/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** ***NHS*** (Nance-Horan Syndrome gene), Xp22.13; OMIM gene *300457*. HGNC symbol *NHS*. The protein is an actin-remodeling scaffold (see Section 6).

**Variant spectrum.** The predominant mutation class is **loss-of-function**:

| Variant (example) | Type | Phenotype end | Source |
|---|---|---|---|
| Nonsense mutations (various) | LoF, truncating | Classic NHS | [PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/) |
| Small deletions | LoF | Classic NHS | [PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/) |
| c.1735delA (p.Arg579Glyfs*91) | Frameshift | NHS/cataract | [PMID: 39994540](https://pubmed.ncbi.nlm.nih.gov/39994540/) |
| c.3333del (p.Phe1111Leufs*9) | Frameshift | NHS/cataract | [PMID: 39858638](https://pubmed.ncbi.nlm.nih.gov/39858638/) |
| 0.52 Mb Xp22.13 microdeletion (*REPS2* + *NHS*) | Structural/CNV | Female carrier, haploinsufficiency | [PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/) |
| Balanced t(X;19), t(X;1) disrupting *NHS* | Structural rearrangement | Affected females | [PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/), [PMID: 28922055](https://pubmed.ncbi.nlm.nih.gov/28922055/) |
| Non-recurrent rearrangements → aberrant transcription | Structural | **Isolated cataract (CTRCT40)** | [PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/) |

> "The majority of reported cases of NHS are the result of nonsense mutations and small deletions." ([PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/))

**Variant classification.** Reported truncating/frameshift variants are classified **pathogenic/likely pathogenic** per ACMG/AMP criteria (null variant in a LoF-intolerant gene, PVS1; segregation; absence from population controls).

**Allele frequency / origin.** Variants are **germline** and **rare/private** (family-specific); not present at appreciable frequency in gnomAD. No somatic contribution (not a cancer context).

**Functional consequence.** **Loss of function / haploinsufficiency.** Dosage and allelic effects explain the spectrum: frank truncation → syndromic NHS; rearrangement-driven transcriptional dysregulation → isolated cataract ([PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/)).

**Modifier genes / epigenetics.** The dominant modifier of female expressivity is **X-chromosome inactivation** (an epigenetic mechanism), not a separate autosomal modifier gene ([PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/)). *REPS2*, adjacent to *NHS*, is co-deleted in some microdeletions but *NHS* haploinsufficiency is concluded to drive symptoms.

**Chromosomal abnormalities.** Xp22.13 microdeletions and balanced X-autosome translocations are documented structural causes.

---

## 5. Environmental Information

**Not applicable.** CTRCT40 is a purely genetic (germline, monogenic) X-linked disorder. There are no established environmental factors, lifestyle factors, or infectious agents contributing to this specific entity. (Environmental cataractogenesis — UV, corticosteroids, trauma, radiation, galactosemia — pertains to other, acquired cataracts and is explicitly distinct from the *NHS*-driven mechanism here.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

```
1. Germline NHS loss-of-function variant / rearrangement (Xp22.13)
      │  leads to
2. Reduced/aberrant NHS protein (haploinsufficiency; in females amplified by skewed XCI)
      │  results in
3. Failure to assemble the WAVE Regulatory Complex / "WAVE Shell Complex"
   and to remodel WAVE and N-WASP nucleation-promoting-factor (NPF) complexes
      │  leads to
4. Dysregulated Arp2/3-dependent actin nucleation → loss of cell-migration
   persistence and cytoskeletal organization  [DEMONSTRATED in vitro, CRISPR NHS-KO]
      │  leads to (INFERRED for lens)
5. Disturbed lens epithelial/fiber-cell polarity, adhesion and cytoskeletal order
   (paralleled by lens-polarity gene SIPA1L3)
      │  results in
6. Structural disorganization → loss of lens transparency
   = BILATERAL CONGENITAL CATARACT
      │  leads to
7. Form deprivation during the ~14-week visual critical period
      │  results in
8. Irreversible DEPRIVATION AMBLYOPIA (+ nystagmus, strabismus) → lifelong vision loss

   ┌── SYNDROMIC BRANCH (global/truncating NHS loss): adds dental (screwdriver
   │   incisors), facial dysmorphism, and neurodevelopmental/intellectual disability
```

Steps 1–4 are **experimentally demonstrated**; step 5 (lens-specific) is **inferred** by analogy to the cytoskeletal/polarity role of NHS and to the related lens-polarity gene *SIPA1L3*; steps 6–8 are **clinically established**.

### Detail by category

**Molecular pathways / cellular processes.** NHS acts in the **actin cytoskeleton regulatory network**. Tandem affinity purification identified **all subunits of the WAVE Regulatory Complex (WRC) except the WAVE subunits** as NHS partners, indicating the N-terminal WAVE Homology Domain (WHD) of NHS assembles a "WAVE Shell Complex." CRISPR knockout of *NHS* in MCF10A cells reduced migration persistence; this was **fully rescued by the long isoform i1** (containing the WHD) but only **partially by isoform i2** lacking it ([PMID: 42595116](https://pubmed.ncbi.nlm.nih.gov/42595116/)).

> "we identified as major NHS partners all subunits of the WAVE Regulatory Complex (WRC) except WAVE subunits themselves, indicating that the WHD of NHS assembles a WAVE Shell Complex (WSC)" ([PMID: 42595116](https://pubmed.ncbi.nlm.nih.gov/42595116/))

> "These results suggest that NHS controls cell migration by remodeling NPF complexes and their higher order assembly." ([PMID: 42595116](https://pubmed.ncbi.nlm.nih.gov/42595116/))

**Protein dysfunction.** Truncating variants abolish functional domains (including, depending on position, the WHD), producing loss of function; haploinsufficiency lowers NHS dosage below the threshold required for normal lens cytoarchitecture ([PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/)).

> "the haploinsufficiency of the NHS gene may account for the majority of clinical symptoms in the affected subjects. The variability among female carriers presumably results from nonrandom X chromosome inactivation" ([PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/))

**Tissue damage mechanism.** The lens depends on exquisitely ordered fiber-cell elongation, packing, and cytoskeletal architecture for transparency. Loss of NHS-dependent actin regulation is inferred to disorganize fiber cells, scattering light = cataract. The supporting precedent: *SIPA1L3* mutations cause lens/eye defects via disruption of **cell polarity and cytoskeleton organization**, with abnormal epithelial-to-mesenchymal transition in the lens ([PMID: 26231217](https://pubmed.ncbi.nlm.nih.gov/26231217/)).

**Epigenetic changes.** X-chromosome inactivation is the key epigenetic determinant of female expressivity ([PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/)).

**Immune / metabolic involvement.** Not implicated — this is a developmental/structural cytoskeletal disorder, not an inflammatory, autoimmune, or primary metabolic disease.

**Suggested ontology terms.** GO:0030036 (actin cytoskeleton organization); GO:0034314 (Arp2/3 complex-mediated actin nucleation); GO:0016477 (cell migration); GO:0007163 (establishment or maintenance of cell polarity); GO:0002088 (lens development in camera-type eye). Cell types: lens fiber cell (CL:0002224) and lens epithelial cell. Anatomy: UBERON:0000965 (lens of camera-type eye).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary: the **crystalline lens** (UBERON:0000965) of the eye, **bilaterally**. Secondary ocular structures: cornea (microcornea, UBERON:0000964), whole globe (microphthalmia), eyelid (ptosis), extraocular alignment (strabismus), and retina/visual cortex functionally via amblyopia. Body system: **visual/sensory nervous system**. In the syndromic branch, additional systems: **dentition/craniofacial** and **central nervous system** (cognition).

**Tissue and cell level.** Lens **epithelial cells** and **lens fiber cells** (CL:0002224) are the targeted populations; the defect is in epithelial/fiber-cell polarity, adhesion, and cytoskeletal organization (inferred from NHS function and the *SIPA1L3* paradigm, [PMID: 26231217](https://pubmed.ncbi.nlm.nih.gov/26231217/)).

**Subcellular level.** The **actin cytoskeleton** and associated **cell cortex / membrane-cytoskeleton interface** (GO:0015629 actin cytoskeleton; GO:0005938 cell cortex). NHS localizes to actin-regulatory machinery (WRC/NPF complexes).

**Localization / lateralization.** **Bilateral** lens involvement in affected males; female carriers may show asymmetric or milder, sometimes unilateral-appearing, opacities.

---

## 8. Temporal Development

**Onset.** **Congenital** (present at birth). Onset pattern is **chronic/structural** — the opacity is established in prenatal/early lens development rather than acquired acutely.

**Progression.** The anatomical lens opacity is largely **stable/non-progressive**. The clinically decisive temporal dimension is the **visual critical period**: without timely surgery, **deprivation amblyopia develops progressively and becomes irreversible**. A bilinear model of dense bilateral congenital cataract identifies a **critical age of ~14 weeks**, with roughly **one line of acuity lost per 3 weeks of delay** during weeks 0–14 ([PMID: 19084444](https://pubmed.ncbi.nlm.nih.gov/19084444/)).

> "A bilinear model with a critical age of 14 weeks fit the data better than a linear model" ([PMID: 19084444](https://pubmed.ncbi.nlm.nih.gov/19084444/))

**Critical periods / windows of intervention.** Best outcomes: surgery **before 6 weeks** (unilateral) and **before 10 weeks** (bilateral) ([PMID: 22383071](https://pubmed.ncbi.nlm.nih.gov/22383071/)). This defines the actionable therapeutic window.

> "Good outcomes have been reported in children undergoing surgery before 6 weeks of age in children with unilateral cataract and before 10 weeks of age in bilateral cases." ([PMID: 22383071](https://pubmed.ncbi.nlm.nih.gov/22383071/))

**Disease duration.** Lifelong (the genetic lesion and any residual amblyopia persist for life), though the lens opacity itself is removed surgically.

---

## 9. Inheritance and Population

**Inheritance pattern.** **X-linked dominant.** The *NHS* gene maps to Xp22.13 ([PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/)).

> "Nance-Horan syndrome (NHS) is a rare X-linked dominant disorder caused by mutation in the NHS gene on chromosome Xp22.13." ([PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/))

**Penetrance / expressivity.** Hemizygous **males**: high penetrance, consistently and severely affected (bilateral dense cataract ± syndromic features). Heterozygous **females**: **variable expressivity** driven by X-inactivation; often milder (subtle lens opacities) and sometimes clinically silent, leading to under-diagnosis ([PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/), [PMID: 28922055](https://pubmed.ncbi.nlm.nih.gov/28922055/), [PMID: 41236159](https://pubmed.ncbi.nlm.nih.gov/41236159/)).

**Sex ratio / sex-specific severity.** Male-predominant severity; females affected more mildly and variably.

**Germline mosaicism / anticipation / founder effects.** No genetic anticipation (not a repeat-expansion disorder). No established founder effect; reported variants are largely private/family-specific. Germline mosaicism is not a prominent reported feature.

**Epidemiology.** CTRCT40/NHS is **rare and frequently under-diagnosed** ([PMID: 39858638](https://pubmed.ncbi.nlm.nih.gov/39858638/)). Precise prevalence is not established; Orphanet lists NHS (ORPHA:627) in the ultra-rare range (order of <1/1,000,000). For context, congenital cataract overall is the commonest worldwide cause of lifelong childhood visual loss, of which *NHS*-related cataract is a rare monogenic subset ([PMID: 22383071](https://pubmed.ncbi.nlm.nih.gov/22383071/)).

> "Nance-Horan syndrome (NHS) is a rare, frequently underdiagnosed, X-linked disease caused by mutations in the NHS gene." ([PMID: 39858638](https://pubmed.ncbi.nlm.nih.gov/39858638/))

**Population demographics.** Reported in multiple populations (e.g., Chinese Han families, European, and others); no strong ethnic predilection beyond ascertainment. Isolated-cataract presentations may be misclassified as simple hereditary cataract until genetic testing reveals the *NHS* etiology ([PMID: 40702650](https://pubmed.ncbi.nlm.nih.gov/40702650/)).

---

## 10. Diagnostics

**Clinical / ophthalmic examination.** Diagnosis begins with detection of congenital lens opacity — **newborn red-reflex testing**, **slit-lamp biomicroscopy**, and assessment for associated microcornea, microphthalmia, ptosis, strabismus, and high myopia. Optical coherence tomography and full physical exam (including dental/craniofacial survey) help distinguish isolated CTRCT40 from the syndromic NHS end ([PMID: 40702650](https://pubmed.ncbi.nlm.nih.gov/40702650/)).

**Genetic testing (definitive).** The recommended approach:

| Test | Utility for CTRCT40 |
|---|---|
| Next-generation sequencing / WES gene panels | First-line to identify *NHS* point/frameshift/nonsense variants; uncovers *NHS* etiology even when initially diagnosed as "isolated" cataract ([PMID: 39858638](https://pubmed.ncbi.nlm.nih.gov/39858638/), [PMID: 40702650](https://pubmed.ncbi.nlm.nih.gov/40702650/)) |
| Sanger sequencing | Variant confirmation and familial segregation |
| Chromosomal microarray (CMA) / karyotype / FISH | Detect Xp22.13 microdeletions and X-autosome translocations ([PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/), [PMID: 28922055](https://pubmed.ncbi.nlm.nih.gov/28922055/)) |
| X-inactivation (skewing) analysis | Explain/predict female-carrier expressivity ([PMID: 36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/)) |

**Clinical criteria / differential diagnosis.** Differentials include other hereditary congenital cataracts (crystallin *CRYAA/CRYBB*, connexin *GJA3/GJA8*, *HSF4*, *SIPA1L3*-related, *BCOR*-related oculofaciocardiodental syndrome, etc.). The presence of screwdriver-shaped incisors, facial dysmorphism, and an X-linked pattern points to the *NHS* spectrum; genetic testing resolves ambiguity.

**Screening.** Population: **universal newborn red-reflex screening**. Family: **cascade carrier testing** of at-risk females once the proband variant is known.

---

## 11. Outcome / Prognosis

**Survival / mortality.** CTRCT40/NHS is **not life-limiting**; mortality is not increased by the ocular disease. (Prognosis concerns vision and, in the syndromic branch, neurodevelopment.)

**Visual prognosis.** Determined chiefly by **timing of surgery** relative to the critical period and the adequacy of amblyopia therapy. Good visual outcomes are achievable with early surgery (before ~6 weeks unilateral / ~10 weeks bilateral) and diligent optical/amblyopia management ([PMID: 22383071](https://pubmed.ncbi.nlm.nih.gov/22383071/), [PMID: 19084444](https://pubmed.ncbi.nlm.nih.gov/19084444/)). Late presentation → deprivation amblyopia → lifelong visual impairment.

**Complications.** Even after timely surgery, children may develop:

> "children may still develop deprivation amblyopia, nystagmus, strabismus, and glaucoma" ([PMID: 22383071](https://pubmed.ncbi.nlm.nih.gov/22383071/))

Glaucoma following cataract surgery (GFCS) and posterior capsule/visual-axis opacification (PCO) are well-documented post-surgical risks requiring lifelong monitoring ([PMID: 40780670](https://pubmed.ncbi.nlm.nih.gov/40780670/)).

**Morbidity / quality of life.** Visual disability (variable, from mild to blindness) is the dominant morbidity. In the syndromic branch, intellectual disability (up to ~30% of affected males) and dental/facial anomalies add to morbidity ([PMID: 28922055](https://pubmed.ncbi.nlm.nih.gov/28922055/)).

**Prognostic factors.** Age at surgery, laterality, density of cataract, presence of microphthalmia/microcornea (risk factor for aphakic glaucoma), and quality of post-operative amblyopia therapy.

---

## 12. Treatment

**There is no pharmacologic, gene, cell, or RNA-based therapy** for CTRCT40/NHS cataract. Management is **surgical and rehabilitative**.

**Surgical (definitive).** Early **lensectomy** (lens extraction) with optical rehabilitation, timed within the critical period (NCIT concept: Cataract Surgery / Lensectomy). Techniques include primary posterior capsulotomy and anterior vitrectomy to reduce PCO; intraocular lens (IOL) implantation is typically reserved for older children (commonly >2 years) given axial growth and myopic shift, with contact lenses or spectacles used for aphakic correction in infants ([PMID: 40780670](https://pubmed.ncbi.nlm.nih.gov/40780670/)).

**Supportive / rehabilitative.** **Amblyopia therapy** (occlusion/patching, optical correction) is central to preserving vision. Management of strabismus, nystagmus, and glaucoma as they arise; refractive correction via contact lens, spectacle, or IOL ([PMID: 40780670](https://pubmed.ncbi.nlm.nih.gov/40780670/)).

**Pharmacogenomics / targeted / immunotherapy / experimental.** Not applicable; no disease-modifying systemic therapy exists. No NCT-registered trials target the *NHS* genetic lesion.

**Treatment strategy (algorithm).**
1. Detect congenital cataract early (red reflex) →
2. Urgent referral; assess density/laterality/associated anomalies →
3. Early lensectomy within critical window →
4. Immediate optical correction (contact lens/spectacles; IOL when age-appropriate) →
5. Aggressive amblyopia therapy →
6. Lifelong surveillance for glaucoma and PCO →
7. Genetic testing + counseling for the family.

**Suggested NCIT terms:** Cataract Surgery; Lens Extraction; Intraocular Lens Implantation; Amblyopia Therapy; Genetic Counseling.

---

## 13. Prevention

**No primary prevention exists** — CTRCT40 is a germline monogenic disorder not modifiable by lifestyle or environment.

**Genetic prevention (the core intervention).** Molecular confirmation of the *NHS* variant enables **accurate family counseling, carrier detection in females, and reproductive options** (prenatal testing, preimplantation genetic diagnosis). NGS/WES of probands with bilateral familial pediatric cataract uncovers the *NHS* etiology — and associated systemic risk — even when initially labeled isolated cataract ([PMID: 39858638](https://pubmed.ncbi.nlm.nih.gov/39858638/), [PMID: 40702650](https://pubmed.ncbi.nlm.nih.gov/40702650/)).

> "it also made possible accurate family counseling essential in all pediatric cataract cases" ([PMID: 39858638](https://pubmed.ncbi.nlm.nih.gov/39858638/))

> "with important implications for clinical presentation and genetic counseling" ([PMID: 28922055](https://pubmed.ncbi.nlm.nih.gov/28922055/))

**Secondary prevention.** **Universal newborn red-reflex screening** to detect congenital cataract early and enable surgery within the critical period ([PMID: 22383071](https://pubmed.ncbi.nlm.nih.gov/22383071/)).

**Tertiary prevention.** **Amblyopia therapy** and structured post-operative surveillance for **glaucoma and PCO/visual-axis opacification** ([PMID: 40780670](https://pubmed.ncbi.nlm.nih.gov/40780670/)).

**Counseling.** Genetic counseling should address X-linked dominant inheritance, male-predominant severity, variable female expressivity due to X-inactivation, and recurrence risk. **Immunization / public-health / prophylaxis:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy.** Reported as a human (NCBI Taxon:9606) disease.
- **Orthologous gene.** An *Nhs* ortholog exists in **mouse** (*Mus musculus*, NCBI Taxon:10090) and other vertebrates; the gene/protein (WAVE-complex scaffolding role) is evolutionarily conserved, consistent with cytoskeletal function demonstrated in human cell lines ([PMID: 42595116](https://pubmed.ncbi.nlm.nih.gov/42595116/)). The related lens-polarity gene *SIPA1L3* shows conserved lens phenotypes across zebrafish and mouse ([PMID: 26231217](https://pubmed.ncbi.nlm.nih.gov/26231217/)).
- **Natural disease in animals.** No well-characterized spontaneous *NHS*-ortholog cataract described in companion animals/wildlife was identified in the reviewed literature (data gap; OMIA not surveyed within this investigation).
- **Zoonotic potential.** Not applicable (genetic disorder).

---

## 15. Model Organisms

- **Cellular/in vitro models (demonstrated).** **CRISPR *NHS*-knockout MCF10A** human epithelial cells were used to establish NHS function in migration persistence and WRC/NPF organization, with isoform rescue experiments (i1 full rescue; i2 partial) ([PMID: 42595116](https://pubmed.ncbi.nlm.nih.gov/42595116/)). This is the principal functional model for the molecular mechanism. **Limitation:** it is a non-lens epithelial system, so the lens phenotype is modeled only indirectly.
- **Comparative / parallel models.** *Sipa1l3*-deficient **zebrafish and mouse** recapitulate lens/eye abnormalities with disrupted epithelial organization and polarity, providing a validated paradigm for how cytoskeleton/polarity disruption causes cataract — a mechanistic parallel informing the inferred lens pathology of NHS ([PMID: 26231217](https://pubmed.ncbi.nlm.nih.gov/26231217/)).
- **Gap.** A dedicated, published *Nhs*-knockout mouse specifically phenotyped for lens cataract was not identified within this investigation; this is a key resource gap (see Follow-up).

---

## Mechanistic Model / Interpretation

The investigation converges on a single, coherent causal narrative integrating all nine confirmed findings (F001–F009):

```
         GENETIC LESION                        MOLECULAR DEFECT                 TISSUE/CLINICAL OUTCOME
  ┌───────────────────────────┐        ┌──────────────────────────────┐    ┌───────────────────────────┐
  │ NHS LoF variant /          │  ───►  │ ↓NHS protein (haploinsuff.)  │──► │ Disorganized lens fiber   │
  │ rearrangement @ Xp22.13    │        │ → no WAVE Shell Complex      │    │ cells → loss of           │
  │ (♀: skewed XCI amplifies)  │        │ → dysregulated Arp2/3 actin  │    │ transparency = bilateral  │
  └───────────────────────────┘        │   nucleation (DEMONSTRATED)  │    │ congenital cataract       │
                                        └──────────────────────────────┘    └─────────────┬─────────────┘
                                                                                           │ form deprivation
                                                                           ┌───────────────▼─────────────┐
   SYNDROMIC BRANCH (truncating/global loss):                             │ within ~14-wk critical       │
   + dental (screwdriver incisors), facial dysmorphism,                   │ period → DEPRIVATION         │
   + intellectual disability (~30% of males)                              │ AMBLYOPIA (irreversible)     │
                                                                           └──────────────────────────────┘
```

**Upstream vs downstream.** The *NHS* genetic lesion and resulting actin-cytoskeleton dysregulation (F002, F005) are **upstream**; lens opacity (F004) is the **midpoint structural outcome**; deprivation amblyopia (F006) is the **downstream, prognosis-determining** endpoint. Female X-inactivation (F003) modulates the entire chain's penetrance in heterozygotes. The allelic/dosage logic (F001, F005) explains why the same gene yields either isolated cataract (CTRCT40) or full Nance-Horan syndrome. F009 is the explicit synthesis of this chain.

**Key interpretive caveat:** Step 5 (lens-specific cytoskeletal disorganization) is **inferred**, bridging demonstrated NHS cell-migration biology (in non-lens epithelial cells) and the demonstrated lens phenotype. The *SIPA1L3* precedent strongly supports, but does not prove, that the same actin/polarity logic operates in the lens for NHS.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/) | *Allelic and dosage effects of NHS in X-linked cataract and Nance-Horan syndrome* | **Anchor** for gene/locus, X-linked dominant inheritance, LoF variant predominance, and the rearrangement→isolated-cataract distinction (F001, F005, F007) |
| [42595116](https://pubmed.ncbi.nlm.nih.gov/42595116/) | *NHS regulates cell migration by organizing WAVE and N-WASP NPF complexes* | **Mechanism** — demonstrates NHS organizes WRC/WSC and controls Arp2/3 actin nucleation (F002, F009) |
| [36370055](https://pubmed.ncbi.nlm.nih.gov/36370055/) | *NHS pedigree: novel microdeletion and skewed XCI* | Establishes haploinsufficiency as causal and XCI as the female-expressivity modifier (F003) |
| [28922055](https://pubmed.ncbi.nlm.nih.gov/28922055/) | *NHS in females due to balanced X;1 translocation* | Core phenotype list; female translocation mechanism; counseling implications (F004, F005, F008) |
| [39994540](https://pubmed.ncbi.nlm.nih.gov/39994540/) | *Novel single-nucleotide deletion in NHS* | Documents associated ocular features and a frameshift variant (F004, F005) |
| [39858638](https://pubmed.ncbi.nlm.nih.gov/39858638/) | *Genotype-phenotype correlations in male/female carriers* | Rarity, under-diagnosis, frameshift variant, family counseling (F005, F007, F008) |
| [41236159](https://pubmed.ncbi.nlm.nih.gov/41236159/) | *Further delineation of male and female carrier phenotypes* | Phenotype spectrum and female variability (F003, F004, F007) |
| [40702650](https://pubmed.ncbi.nlm.nih.gov/40702650/) | *Leveraging genetic testing for cataract diagnosis* | Value of NGS for uncovering NHS etiology (F007, F008) |
| [19084444](https://pubmed.ncbi.nlm.nih.gov/19084444/) | *Critical period for surgery of dense congenital bilateral cataracts* | Defines ~14-week critical period (F006, F009) |
| [22383071](https://pubmed.ncbi.nlm.nih.gov/22383071/) | *Congenital and infantile cataract: aetiology and management* | Surgical timing targets, complications, epidemiology context (F006, F007) |
| [40780670](https://pubmed.ncbi.nlm.nih.gov/40780670/) | *Update on pediatric cataract surgery* | Modern surgical/IOL/amblyopia/complication management (F006, F008) |
| [26231217](https://pubmed.ncbi.nlm.nih.gov/26231217/) | *SIPA1L3 mutations cause eye defects through disruption of cell polarity/cytoskeleton* | Mechanistic parallel for inferred lens-cytoskeleton step (F009) |

**Evidence-type mix:** human clinical case reports/pedigrees (phenotype, inheritance, variants), human in vitro CRISPR functional genomics (NHS molecular mechanism), cross-species model data (*SIPA1L3* parallel), and clinical-outcome cohorts (surgical timing, complications). No large natural-history registry specific to CTRCT40 exists.

---

## Limitations and Knowledge Gaps

1. **Inferred lens mechanism.** The direct molecular evidence for NHS function (F002) derives from a non-lens epithelial cell line (MCF10A). The lens-specific step connecting actin dysregulation to fiber-cell disorganization is **inferred**, not directly demonstrated for NHS.
2. **No dedicated *Nhs* cataract animal model identified** in the reviewed literature — a significant gap for validating the causal chain in vivo.
3. **Imprecise epidemiology.** Prevalence/incidence of CTRCT40 specifically is not established; it is subsumed within rare congenital cataract and often under-diagnosed/misclassified.
4. **Genotype–phenotype boundary is quantitative, not absolute.** The line between "isolated CTRCT40" and "syndromic NHS" depends on variant class/dosage and ascertainment; some patients may be reclassified as more systemic features emerge.
5. **Female expressivity prediction is imperfect.** While skewed XCI explains variability qualitatively, it does not yet permit precise prediction of individual female carrier severity.
6. **No disease-modifying therapy.** Management addresses the downstream opacity, not the upstream genetic/molecular defect.

---

## Proposed Follow-up Experiments / Actions

1. **Lens-specific functional validation.** Generate a conditional lens-targeted *Nhs* knockout (or *NHS* perturbation in human iPSC-derived lens organoids/micro-lenses) and assay fiber-cell polarity, actin architecture, and transparency — to directly test inferred step 5 of the causal chain.
2. **Isoform-resolved lens biology.** Determine which *NHS* isoforms (i1 with WHD vs i2) are expressed in lens epithelium/fibers and whether WHD-dependent WAVE Shell Complex assembly is required for lens transparency (extending [PMID: 42595116](https://pubmed.ncbi.nlm.nih.gov/42595116/)).
3. **XCI-based carrier risk model.** Correlate quantitative X-inactivation skewing with measured lens-opacity severity across a larger female-carrier cohort to build a predictive expressivity model.
4. **Genotype–phenotype registry.** Establish a curated *NHS*-variant registry linking variant class (truncating vs rearrangement vs microdeletion) to isolated-cataract vs syndromic outcome, refining the dosage/allelic model ([PMID: 34620209](https://pubmed.ncbi.nlm.nih.gov/34620209/)).
5. **Prospective surgical-outcome study in NHS-confirmed cases.** Stratify visual outcomes by age at lensectomy within molecularly confirmed CTRCT40 to confirm the critical-period model applies to this genetic subset.
6. **Systematic genetic testing in bilateral pediatric cataract.** Promote routine NGS panels (including *NHS*, plus CMA for Xp22.13 structural events) to reduce under-diagnosis and enable timely counseling ([PMID: 40702650](https://pubmed.ncbi.nlm.nih.gov/40702650/)).

---

*Report generated from a 5-iteration autonomous investigation of Cataract 40 (CTRCT40). Evidence attributions are based on verified abstract-level citation snippets recorded during the investigation.*


## Artifacts

- [OpenScientist final report](Cataract_40-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cataract_40-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010544` (3 mentions) - the report calls it "MONDO"; MONDO calls it **cataract 40**
- `HP:0000482` (1 mention) - the report calls it "Common"; HP calls it **Microcornea**
- `HP:0000568` (1 mention) - the report calls it "Common"; HP calls it **Microphthalmia**
- `HP:0000486` (1 mention) - the report calls it "Common"; HP calls it **Strabismus**
- `HP:0000639` (1 mention) - the report calls it "Common sequela of deprivation"; HP calls it **Nystagmus**
- `HP:0001999` (1 mention) - the report calls it "Classic NHS"; HP calls it **Abnormal facial shape**
- `HP:0001249` (1 mention) - the report calls it "Up to ~30% of affected males"; HP calls it **Intellectual disability**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0002224` (2 mentions) - the report calls it "lens fiber cells"; CL calls it **lens epithelial cell**
- `UBERON:0000965` (2 mentions) - the report calls it "lens of camera-type eye", "crystalline lens"; UBERON calls it **lens of camera-type eye**, and lists "crystalline lens" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000965` - called "lens of camera-type eye", "crystalline lens"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Taxon`.