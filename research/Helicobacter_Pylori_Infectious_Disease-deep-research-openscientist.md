---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T01:10:19.761621'
end_time: '2026-09-30T01:27:13.333285'
duration_seconds: 1013.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Helicobacter Pylori Infectious Disease
  mondo_id: MONDO:0006781
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 43
reference_validation:
  total_references: 43
  verified: 43
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 43
  on_topic: 37
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 1
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0031273
    reported_labels:
    - chronic gastritis
    ontology_label: Shock
  - term_id: HP:0011834
    reported_labels:
    - Symptom
    ontology_label: Moyamoya phenomenon
  - term_id: HP:0025439
    reported_labels:
    - dyspepsia
    ontology_label: Pharyngitis
  - term_id: HP:0001891
    reported_labels:
    - Lab abnormality
    ontology_label: Iron deficiency anemia
  - term_id: HP:0100502
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased circulating vitamin B12 concentration
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Helicobacter_Pylori_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Helicobacter_Pylori_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Helicobacter Pylori Infectious Disease
- **MONDO ID:** MONDO:0006781 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Helicobacter Pylori Infectious Disease** covering all of the
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

# Helicobacter pylori Infectious Disease — Comprehensive Disease Characterization

**Disease:** Helicobacter pylori Infectious Disease
**MONDO ID:** MONDO:0006781
**Category:** Infectious Disease
**Causative organism:** *Helicobacter pylori* (NCBI Taxon 210)
**Report type:** Literature-based disease-level synthesis (no primary patient data). Evidence sources labeled *human clinical*, *model organism*, or *in vitro*.

---

## Summary

*Helicobacter pylori* infectious disease is a lifelong chronic bacterial infection of the human gastric mucosa caused by the urease-producing, microaerophilic, spiral Gram-negative bacterium *H. pylori*. It is one of the most common chronic infections of humankind: a Bayesian meta-analysis of 181 studies estimated global population prevalence at 36.3% in 2023, down modestly from 43.1% in 1990 ([PMID: 42757050](https://pubmed.ncbi.nlm.nih.gov/42757050/)). Infection is almost always acquired in childhood via oral–oral, gastric–oral, and fecal–oral routes, and if untreated persists for the life of the host. Virtually every colonized individual develops chronic active gastritis, yet only ~10–20% ever develop overt clinical disease.

The clinical outcome of infection is not uniform; it branches according to the **anatomical topography of gastritis** and the interaction of **bacterial virulence factors** (chiefly CagA and VacA) with **host genetic susceptibility** (chiefly pro-inflammatory *IL1B*/*IL1RN* polymorphisms). Antral-predominant gastritis drives acid hypersecretion and duodenal ulceration, whereas corpus-predominant or pangastritis drives atrophy, hypochlorhydria, intestinal metaplasia, dysplasia, and ultimately gastric adenocarcinoma (the Correa cascade). *H. pylori* is classified by the IARC as a Group 1 (definite) human carcinogen and is the dominant cause of gastric cancer, with a population attributable fraction averaging ~70% across 27 countries. It also causes gastric MALT (mucosa-associated lymphoid tissue) lymphoma, which regresses completely in most patients after eradication of the bacterium alone.

The disease is diagnosed non-invasively by the urea breath test and monoclonal stool antigen test (serology cannot distinguish active from past infection) and is curable with combination acid-suppression plus antibiotic therapy. Landmark long-term randomized controlled trial evidence establishes that eradication is effective **primary prevention** of gastric cancer. No licensed vaccine yet exists, although multivalent candidates (VacA/CagA/NAP) have reached human trials. This report synthesizes 15 confirmed findings drawn from 72 papers across all requested domains.

---

## 1. Disease Information

**Overview.** *H. pylori* infectious disease is chronic colonization of the gastric mucosa by *H. pylori*, a neutralophilic, microaerophilic, spiral (helical) Gram-negative bacterium that produces urease, catalase, and oxidase. The organism was discovered by Marshall and Warren in 1982, linking it to ulcer disease ([PMID: 15345211](https://pubmed.ncbi.nlm.nih.gov/15345211/)). Colonization causes chronic active type B gastritis in essentially all infected individuals; a minority progress to peptic ulcer disease, gastric adenocarcinoma, or gastric MALT lymphoma ([PMID: 9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/)).

**Key identifiers.**
- **MONDO:** MONDO:0006781
- **MeSH:** *Helicobacter Infections* (D016481); organism *Helicobacter pylori*
- **ICD-10:** B96.81 (*H. pylori* as cause of diseases classified elsewhere); associated gastritis K29.-, peptic ulcer K25–K27
- **ICD-11:** coding under gastritis/duodenitis and infectious agents
- **NCBI Taxon:** 210 (*Helicobacter pylori*)
- OMIM/Orphanet: not applicable as a primary Mendelian entry — this is an infectious, not a monogenic, disease. Host susceptibility loci such as *IL1B* have OMIM gene entries (see Section 4).

**Synonyms / alternative names.** *Helicobacter pylori* infection; *H. pylori* infection; *Campylobacter pylori* infection (historical, pre-1989); *Campylobacter pyloridis* infection (original 1983–84 designation); Helicobacter-associated gastritis; type B gastritis (when antral).

**Information source.** This report derives predominantly from **aggregated disease-level resources** — meta-analyses, systematic reviews, RCTs, consensus guidelines (Maastricht V/VI, ACG), and mechanistic laboratory studies — rather than individual EHR-level patient records.

---

## 2. Etiology

**Primary cause — infectious.** The disease is caused by infection with *H. pylori*, a necessary cause of the chronic active gastritis underlying all downstream *H. pylori* disease. Core virulence factors are the vacuolating cytotoxin **VacA**, the **cag pathogenicity island / CagA** oncoprotein delivered by a type IV secretion system, **urease**, and **flagellar motility** ([PMID: 9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/)).

**Environmental / lifestyle risk factors.** Acquisition is strongly socioeconomic: *"In the vast majority of individuals, infection is acquired during childhood with those of low socioeconomic means and having infected family members being at highest risk for early childhood acquisition"* ([PMID: 15758899](https://pubmed.ncbi.nlm.nih.gov/15758899/)). Household crowding, an infected family member (especially the mother), and poor sanitation are dominant environmental risk factors. Progression to cancer is further modulated by high dietary salt, smoking, and low ascorbate intake.

**Host genetic risk factors.** Host pro-inflammatory polymorphisms strongly modify cancer risk. In *H. pylori*-infected Pakistani individuals, combined carriage of *IL-1B*-511\*T and *IL-1RN*\*2 conferred dramatically increased gastric cancer risk (**OR 19.064; 95% CI 2.319–156.7; p = 0.001**): *"A combination of IL-1B-511\*T and IL-1RN\*2 alleles ... in H. pylori infected individuals had markedly increased risk of GC development"* ([PMID: 28110439](https://pubmed.ncbi.nlm.nih.gov/28110439/)). In an Algerian cohort, *IL-1β*-31C associated with gastric carcinoma (OR 4.614, 95% CI 1.43–14.81, p = 0.01) and *IL-1β*-511T with chronic atrophic gastritis (OR 4.286, 95% CI 1.54–11.89, p = 0.005) ([PMID: 27340011](https://pubmed.ncbi.nlm.nih.gov/27340011/)). Interactions among *PGC*, *PTPN11*, *TLR4*, and *IL1B* SNPs further modify carcinogenesis under infection ([PMID: 26158864](https://pubmed.ncbi.nlm.nih.gov/26158864/)).

**Protective factors.** Eradication is the principal protective intervention (Sections 11–13). Diets rich in ascorbate and low in salt are associated with reduced progression. No robust protective germline allele has been established with the confidence of the *IL1* risk alleles.

**Gene–environment interaction.** The paradigm is explicitly gene × environment: the same *IL1* polymorphisms are innocuous without infection but high-risk in its presence. A cumulative *PGC/PTPN11* interaction *"switched from being beneficial to being risky by the status of H. pylori infection"* ([PMID: 26158864](https://pubmed.ncbi.nlm.nih.gov/26158864/)) — a clean demonstration that host genotype manifests risk only in the infected context.

---

## 3. Phenotypes

Most infection is clinically silent. Nearly all colonized individuals develop chronic active gastritis, but the majority remain asymptomatic, and only ~10–20% develop clinical disease over a lifetime ([PMID: 15758899](https://pubmed.ncbi.nlm.nih.gov/15758899/)). In symptomatic dyspeptic cohorts undergoing endoscopy, **epigastric pain is predominant (67.4–79.2%)**, followed by heartburn (26.1%); gastritis is the most common endoscopic finding (65.5%), with gastric ulcers ~4.6% and carcinoma <1% ([PMID: 33251073](https://pubmed.ncbi.nlm.nih.gov/33251073/): *"Epigastric pain was the predominant symptom (79.2%) followed by heartburn (26.1%) ... Gastritis (65.5%) and oesophagitis (33.1%) were the most common findings"*; [PMID: 34579657](https://pubmed.ncbi.nlm.nih.gov/34579657/)).

| Phenotype | Type | HPO suggestion | Frequency / notes |
|---|---|---|---|
| Chronic active gastritis | Histopathologic sign | HP:0031273 (chronic gastritis) | ~100% of infected (mostly subclinical) |
| Epigastric pain | Symptom | HP:0011834 | 67–79% of symptomatic dyspeptics |
| Heartburn / dyspepsia | Symptom | HP:0025439 (dyspepsia) | ~26% |
| Peptic (gastric/duodenal) ulcer | Clinical sign / lesion | HP:0004398 (peptic ulcer) | Minority; PAF for PUD ~57% |
| Gastric MALT lymphoma | Neoplasm | HP:0012190 (MALT lymphoma) | Rare; PAF ~33% of gastric lymphoma |
| Gastric adenocarcinoma | Neoplasm | HP:0012126 (gastric cancer) | PAF ~70% (non-cardia) |
| Iron-deficiency anemia | Lab abnormality | HP:0001891 | Extragastric association |
| Vitamin B12 deficiency | Lab abnormality | HP:0100502 | Extragastric association |
| Immune thrombocytopenia | Lab/clinical sign | HP:0001973 (thrombocytopenia) | Extragastric association |

**Characteristics.** Colonization onset is in childhood, but clinical disease typically manifests decades later. Children may nonetheless develop chronic active gastritis, ulcers, and MALT lymphoma ([PMID: 15758899](https://pubmed.ncbi.nlm.nih.gov/15758899/)). Severity ranges from mild asymptomatic gastritis to lethal carcinoma; progression is chronic and, for the neoplastic branch, stepwise over decades.

**Quality-of-life impact.** Symptomatic dyspepsia and peptic ulcer disease impair daily functioning; gastric cancer and lymphoma carry the greatest burden. Disease burden extends beyond cancer: attributable fractions were 57% for peptic ulcer disease, 7% for dyspepsia, and 33% for gastric lymphoma ([PMID: 41236450](https://pubmed.ncbi.nlm.nih.gov/41236450/)).

---

## 4. Genetic / Molecular Information

This is an infectious disease, so there are **no human causal germline genes**. The relevant genetics are (a) host susceptibility modifier loci and (b) bacterial virulence and resistance genes.

**Host modifier genes.**
- ***IL1B*** (interleukin-1β; HGNC:5992) — promoter polymorphisms -511 C/T (rs16944), -31 (rs1143627) and rs1143627 raise gastric cancer / atrophic gastritis risk under infection ([PMID: 28110439](https://pubmed.ncbi.nlm.nih.gov/28110439/), [PMID: 27340011](https://pubmed.ncbi.nlm.nih.gov/27340011/)).
- ***IL1RN*** (IL-1 receptor antagonist; HGNC:6000) — the \*2 VNTR allele synergizes with *IL1B* ([PMID: 28110439](https://pubmed.ncbi.nlm.nih.gov/28110439/)).
- ***PGC*, *PTPN11*, *TLR4*** — interacting susceptibility loci ([PMID: 26158864](https://pubmed.ncbi.nlm.nih.gov/26158864/)).
- ***CYP2C19*** — pharmacogenetic modifier of treatment: rapid/ultrarapid metabolizers have 2.52-fold higher eradication failure with PPI-based regimens ([PMID: 34358488](https://pubmed.ncbi.nlm.nih.gov/34358488/)).

**Bacterial virulence and resistance genes (the true "pathogenic variants" of this disease).**
- ***cagA*** and the *cag* pathogenicity island / type IV secretion system — principal oncogenic determinant ([PMID: 17237808](https://pubmed.ncbi.nlm.nih.gov/17237808/), [PMID: 28338646](https://pubmed.ncbi.nlm.nih.gov/28338646/)).
- ***vacA*** — vacuolating cytotoxin, allelic mosaicism (s1/m1 more virulent).
- ***ureA/ureB/ureI*** — urease and its pH-gated urea channel (colonization).
- **Resistance mutations:** 23S rRNA A2142G/A2143G (clarithromycin), *rdxA* (metronidazole), *pbp1A* (amoxicillin), *gyrA/gyrB* (levofloxacin) ([PMID: 41966313](https://pubmed.ncbi.nlm.nih.gov/41966313/)).

**Functional consequence.** CagA acts as a **bacterial oncoprotein** with gain-of-function signaling in host cells (Section 6). Host *IL1B* risk alleles are gain-of-function for IL-1β expression, amplifying gastric inflammation and acid suppression.

**Epigenetics.** *H. pylori*-driven chronic inflammation induces aberrant promoter DNA methylation in gastric epithelium, contributing to the field of cancerization. CagA also transactivates *CDX1* and induces *MUC2*, marking intestinal transdifferentiation ([PMID: 17237808](https://pubmed.ncbi.nlm.nih.gov/17237808/)).

**Chromosomal abnormalities.** Not applicable at the germline level; somatic copy-number and mutational changes accumulate in gastric epithelium during the cancer cascade.

---

## 5. Environmental Information

**Environmental / lifestyle factors.** Low socioeconomic status, crowding, poor sanitation, and contaminated water in childhood are the principal drivers of acquisition ([PMID: 15758899](https://pubmed.ncbi.nlm.nih.gov/15758899/), [PMID: 11488660](https://pubmed.ncbi.nlm.nih.gov/11488660/)). High dietary salt, smoking, and low vitamin C promote progression along the cancer cascade.

**Infectious agent.** The causative pathogen is *H. pylori* (NCBI:txid210), a Gram-negative, microaerophilic, spiral bacterium. Related non-pylori gastric *Helicobacter* species (*H. suis*, *H. heilmannii*, *H. felis*, *H. salomonis*, *H. bizzozeronii*) cause a smaller fraction of human gastric disease and are zoonotic (Section 14) ([PMID: 26155631](https://pubmed.ncbi.nlm.nih.gov/26155631/)).

**CHEBI-relevant chemical entities:** urea (CHEBI:16199), ammonia (CHEBI:16134), nitrite (CHEBI:16301), ascorbic acid (CHEBI:29073), nickel ion (CHEBI:49786, urease cofactor).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Ingestion** of *H. pylori* (oral–oral / fecal–oral, in childhood) **leads to** arrival in the gastric lumen.
2. **Urease-mediated acid resistance** — constitutive Ni²⁺-dependent urease hydrolyzes urea to ammonia; the pH-gated urea channel UreI opens when periplasmic pH falls below ~6.2 — **allows** transient survival in gastric acid. *"Acute acid resistance depends on the constitutive synthesis of a neutral pH optimum urease ... Gastric juice urea is able to rapidly access intrabacterial urease when the periplasmic pH falls below approximately 6.2 owing to pH-gating of a urea channel, UreI"* ([PMID: 12471160](https://pubmed.ncbi.nlm.nih.gov/12471160/)).
3. **Flagellar motility + adhesins** **enable** penetration of the mucus layer and colonization of the epithelial-surface niche, avoiding mucus clearance ([PMID: 24914320](https://pubmed.ncbi.nlm.nih.gov/24914320/)).
4. **Persistent colonization** **induces** chronic active gastritis (neutrophil + lymphocyte infiltration) ([PMID: 9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/)).
5. **CagA injection via T4SS** → tyrosine phosphorylation by Src-family kinases → **binds and activates SHP-2 phosphatase**, causing "hummingbird" cell-morphological transformation: *"Tyrosine-phosphorylated CagA specifically binds to and activates SHP-2 phosphatase, thereby inducing cell-morphological transformation"* ([PMID: 17237808](https://pubmed.ncbi.nlm.nih.gov/17237808/), [PMID: 28338646](https://pubmed.ncbi.nlm.nih.gov/28338646/)).
6. **Phosphorylation-independent CagA** → **binds E-cadherin**, disrupting the E-cadherin/β-catenin complex → **cytoplasmic/nuclear β-catenin accumulation** → transactivates *CDX1* → induces goblet-cell marker *MUC2* → **intestinal metaplasia**: *"The CagA/E-cadherin interaction impairs the complex formation between E-cadherin and beta-catenin, causing cytoplasmic and nuclear accumulation of beta-catenin. CagA-deregulated beta-catenin then transactivates beta-catenin-dependent genes such as cdx1"* ([PMID: 17237808](https://pubmed.ncbi.nlm.nih.gov/17237808/)).
7. **Chronic inflammation** → dicarbonyl/isolevuglandin electrophiles form DNA adducts → **DNA damage and increased somatic mutation frequency** ([PMID: 33189701](https://pubmed.ncbi.nlm.nih.gov/33189701/)).

**Branch point — topography of gastritis determines outcome** ([PMID: 9494857](https://pubmed.ncbi.nlm.nih.gov/9494857/): *"Subjects in whom the infection produces acid hypersecretion develop duodenal ulcer disease ... In subjects in whom the infection induces marked hypochlorhydria, there is an increased risk of gastric cancer"*; [PMID: 9376611](https://pubmed.ncbi.nlm.nih.gov/9376611/)):

```
        Chronic active gastritis (universal)
                     |
        ┌────────────┴─────────────────────┐
   ANTRAL-PREDOMINANT              CORPUS-PREDOMINANT / PANGASTRITIS
        |                                   |
  ↑ antral gastrin                    corpus gland damage
        |                                   |
  ↑ acid output (oxyntic mucosa)      ↓ acid → HYPOCHLORHYDRIA
        |                                   |
  ↑ duodenal acid load                ↑ intragastric pH, ↑ nitrite,
        |                             ↓ ascorbate, nitrosating bacteria
  gastric metaplasia of duodenum            |
        |                             ATROPHY → INTESTINAL METAPLASIA
  DUODENAL ULCER                            → DYSPLASIA
                                            → GASTRIC ADENOCARCINOMA
                                      (+ MALT LYMPHOMA branch)
```

**Molecular pathways / cellular processes.** CagA-driven signaling co-opts SHP-2/ERK-MAPK, NF-κB, and Wnt/β-catenin pathways. Chronic inflammation, apoptosis dysregulation, and oxidative/lipid-peroxidation DNA damage are the core cellular processes. Relevant GO biological-process terms: **GO:0006954** (inflammatory response), **GO:0016477** (cell migration, "hummingbird"), **GO:0006281** (DNA repair). CL cell types: **CL:0000584** (enterocyte, metaplastic), **CL:0002180** (mucous cell of stomach), **CL:0000236** (B cell, MALT lymphoma).

**Immune involvement.** Chronic Th1/Th17-skewed gastric inflammation is central both to pathology and to the immunity candidate vaccines aim to elicit ([PMID: 37971157](https://pubmed.ncbi.nlm.nih.gov/37971157/), [PMID: 40776465](https://pubmed.ncbi.nlm.nih.gov/40776465/)).

---

## 7. Anatomical Structures Affected

- **Primary organ:** stomach (**UBERON:0000945**), specifically the gastric mucosa. Antrum (**UBERON:0001165**) in the duodenal-ulcer branch; corpus/body (**UBERON:0001161**) in the cancer branch.
- **Secondary sites:** duodenum (**UBERON:0002114**) — gastric metaplasia and duodenal ulcer; systemic/hematologic involvement in extragastric disease.
- **Body system:** digestive system (**UBERON:0001007**).
- **Tissue level:** gastric surface mucous epithelium; gastric glands (parietal, chief, G-cells, D-cells, ECL cells); mucosa-associated lymphoid tissue for MALT lymphoma.
- **Cell populations (CL):** gastric surface mucous cell (CL:0002180), parietal cell (CL:0000162), chief cell (CL:0000155), G-cell/gastrin cell, ECL cell, gastric stem/progenitor cells, mucosal B lymphocytes (CL:0000236).
- **Subcellular (GO cellular component):** bacterial urease is cytoplasmic/periplasmic; CagA localizes to the host inner plasma membrane (**GO:0005886**) and translocates to the nucleus (**GO:0005634**), where β-catenin accumulates.
- **Localization / lateralization:** not applicable — a midline, non-lateralized luminal organ; disease is defined by mucosal topography (antrum vs corpus) rather than laterality.

---

## 8. Temporal Development

- **Onset:** colonization in early childhood; insidious and chronic. If untreated, *"H pylori infection is lifelong"* ([PMID: 15758899](https://pubmed.ncbi.nlm.nih.gov/15758899/)).
- **Progression:** clinical disease typically manifests decades after acquisition. The neoplastic branch follows the multi-decade **Correa cascade**: chronic gastritis → atrophy → intestinal metaplasia → dysplasia → adenocarcinoma. Clarithromycin resistance rises with disease severity along the cascade: CNAG 33.3% → CAG 31.7% → gastric ulcer 59.3% → MALT-L 54.1% → gastric cancer 69.6% ([PMID: 42365653](https://pubmed.ncbi.nlm.nih.gov/42365653/)).
- **Course:** chronic and progressive if untreated; ulcer disease can be episodic/relapsing-remitting.
- **Remission / critical windows:** eradication is treatment-induced remission. Earlier eradication (before premalignant lesions develop) yields the greatest cancer-prevention benefit — a critical intervention window (Section 11).

---

## 9. Inheritance and Population

**Epidemiology.** Global population prevalence declined modestly *"from 43.1% (95% credible interval 39.1-47.4) in 1990 to 36.3% (33.2-39.6) in 2023"* ([PMID: 42757050](https://pubmed.ncbi.nlm.nih.gov/42757050/)). Prevalence approaches 100% in some developing regions and is falling in high-income countries. The organism is the dominant cause of gastric cancer: the population attributable fraction averaged **69.7%** across 27 countries (*"ranging from 40.7% in Malaysia to 82.3% in South Africa"*; risk ratio 5.9) ([PMID: 41115989](https://pubmed.ncbi.nlm.nih.gov/41115989/)).

**Inheritance.** Not applicable — this is an acquired infection, not a heritable Mendelian disorder. Host **susceptibility is polygenic/multifactorial** (e.g., *IL1B*, *IL1RN*, *TLR4*). Familial clustering reflects **shared household transmission** (chiefly mother-to-child), not genetic inheritance.

**Population demographics.** Higher prevalence in low-socioeconomic and developing-country populations; East Asian, Latin American, and some African populations bear the highest gastric-cancer burden, partly attributable to more virulent East-Asian *cagA* genotypes. Acquisition is concentrated in childhood; prevalence rises with age in cross-section (cohort effect). Infection sex ratio is roughly equal; gastric cancer shows a male predominance (~2:1).

---

## 10. Diagnostics

**Non-invasive tests.** Pooled sensitivity/specificity from meta-analysis ([PMID: 38143438](https://pubmed.ncbi.nlm.nih.gov/38143438/): *"The pooled sensitivity and specificity for HpSA were 72.5 and 94.7%, for Serology 83.7 and 73.3%, and for UBT 96.4 and 88.3%"*):

| Test | Sensitivity | Specificity | Diagnostic OR | Note |
|---|---|---|---|---|
| Urea breath test (UBT) | 96.4% | 88.3% | 94.5 | Best overall; detects active infection |
| Monoclonal stool antigen (HpSA/SAT) | 72.5% | 94.7% | 47.9 | High specificity; reliable, non-invasive |
| Serology (IgG) | 83.7% | 73.3% | 14.2 | Cannot confirm active infection |

Serology *"is useful only in selected settings because it cannot reliably distinguish current from previous infection"* ([PMID: 42724990](https://pubmed.ncbi.nlm.nih.gov/42724990/)). UBT sensitivity falls in advanced atrophic/metaplastic mucosa; qPCR and monoclonal SAT show superior performance across disease stages, and multimodal strategies (e.g., SAT + histology) achieve the highest sensitivity ([PMID: 41985696](https://pubmed.ncbi.nlm.nih.gov/41985696/)).

**Invasive / reference-standard tests.** Endoscopic biopsy with histology (H&E, IHC), rapid urease test (CLO test), and culture remain reference standards and permit resistance testing and staging of premalignant lesions ([PMID: 42724990](https://pubmed.ncbi.nlm.nih.gov/42724990/)). Molecular detection of 23S rRNA resistance mutations guides tailored therapy.

**Genetic/omics diagnostics.** Human germline genetic testing is not diagnostically indicated. Bacterial molecular testing (qPCR, sequencing for resistance mutations) is increasingly used; *CYP2C19* genotyping can inform PPI dosing.

**Differential diagnosis.** Functional dyspepsia, NSAID-induced ulcer, autoimmune (type A) gastritis, Zollinger-Ellison syndrome, gastroparesis, biliary disease, and gastric neoplasia of other etiology.

**Screening.** Population "test-and-treat" / "screen-and-treat" programs are recommended in high-incidence regions and are being trialed in adolescents (e.g., Chile, NCT05926804) ([PMID: 39890135](https://pubmed.ncbi.nlm.nih.gov/39890135/)).

---

## 11. Outcome / Prognosis

**Untreated course.** Lifelong infection; ~10–20% develop clinical disease. Most morbidity/mortality flows from gastric adenocarcinoma (poor prognosis when diagnosed late) and peptic ulcer complications (bleeding, perforation).

**With eradication.** Excellent — eradication cures gastritis, heals ulcers, prevents recurrence, and reduces cancer risk. **MALT lymphoma prognosis is outstanding:** in a 398-patient multicenter cohort, overall complete remission (CR) was **97.0%** (*"98.3% in HPP and 93.3% in HPN (P = 0.018)"*), 91.2% presented at localized stage IE, and relapse was only 8.3% over a median 179 weeks ([PMID: 41776408](https://pubmed.ncbi.nlm.nih.gov/41776408/)). Pediatric cases also regress completely after eradication alone ([PMID: 42034998](https://pubmed.ncbi.nlm.nih.gov/42034998/)).

**Cancer prevention (landmark RCT).** In 1,630 asymptomatic infected individuals in high-risk southern China with **26.5 years of follow-up**, eradication reduced gastric cancer incidence (2.57% vs 4.31%; **HR 0.57, 95% CI 0.33–0.98**), with greater benefit in those without premalignant lesions (**HR 0.37, 95% CI 0.15–0.95**) ([PMID: 35364066](https://pubmed.ncbi.nlm.nih.gov/35364066/)). A Cochrane meta-analysis confirmed eradication reduces both gastric cancer incidence (RR 0.54, 95% CI 0.40–0.72) and gastric-cancer mortality (RR 0.61, 95% CI 0.40–0.92) ([PMID: 32628791](https://pubmed.ncbi.nlm.nih.gov/32628791/)).

**Prognostic factors.** Presence of premalignant lesions at treatment predicts residual cancer risk; *cagA*-positive/East-Asian strains and virulent *vacA* alleles and high-risk host genotypes worsen prognosis; successful eradication vs persistent infection is itself prognostic (HR 0.46) ([PMID: 35364066](https://pubmed.ncbi.nlm.nih.gov/35364066/)).

---

## 12. Treatment

**First-line pharmacotherapy** (Maastricht V/VI and ACG guidelines):
- **Clarithromycin-based triple therapy** (PPI + clarithromycin + amoxicillin) in regions with clarithromycin resistance <15% ([PMID: 29600697](https://pubmed.ncbi.nlm.nih.gov/29600697/)).
- **Bismuth quadruple therapy** (PPI + bismuth + tetracycline + metronidazole) in high-resistance regions — *"Greater than 90% eradication success can be obtained by bismuth-containing quadruple therapy"* ([PMID: 26808355](https://pubmed.ncbi.nlm.nih.gov/26808355/)).
- **Potassium-competitive acid blockers (vonoprazan)** increasingly replace PPIs, giving more potent acid suppression and higher eradication rates ([PMID: 29600697](https://pubmed.ncbi.nlm.nih.gov/29600697/), [PMID: 42410737](https://pubmed.ncbi.nlm.nih.gov/42410737/)).

**Rescue / second-line:** levofloxacin-based triple therapy, rifabutin- or furazolidone-based regimens, or susceptibility-guided tailored therapy ([PMID: 29600697](https://pubmed.ncbi.nlm.nih.gov/29600697/)).

**Antibiotic resistance** is the key driver of failure: *"Clarithromycin resistance in H. pylori is mainly driven by A2142G/A2143G mutations (19-34%), while metronidazole resistance exceeds 84% in East Asia via rdxA mutations. Amoxicillin resistance (6-34%) links to pbp1A variants, and levofloxacin resistance (31-66%) to gyrA/B mutations"* ([PMID: 41966313](https://pubmed.ncbi.nlm.nih.gov/41966313/)).

**Pharmacogenomics.** Host **CYP2C19** rapid/ultrarapid-metabolizer phenotype raises PPI-based eradication failure — *"enhanced vs poor metabolizer phenotypes were associated with a 2.52-fold significantly higher likelihood of eradication failure"* ([PMID: 34358488](https://pubmed.ncbi.nlm.nih.gov/34358488/)) — the rationale for genotype-guided PPI dosing or P-CABs, which are less CYP2C19-dependent.

**NCIT term suggestions:** Proton Pump Inhibitor (NCIT:C1454), Clarithromycin (NCIT:C349), Amoxicillin (NCIT:C284), Metronidazole (NCIT:C619), Tetracycline (NCIT:C859), Bismuth Subsalicylate, Levofloxacin (NCIT:C1615), Vonoprazan.

---

## 13. Prevention

- **Primary prevention:** *H. pylori* eradication is proven primary prevention of gastric cancer ([PMID: 35364066](https://pubmed.ncbi.nlm.nih.gov/35364066/); Cochrane [PMID: 32628791](https://pubmed.ncbi.nlm.nih.gov/32628791/)). Improved sanitation, clean water, and reduced crowding lower transmission.
- **Secondary prevention:** test-and-treat / screen-and-treat programs; endoscopic surveillance of premalignant lesions ([PMID: 39890135](https://pubmed.ncbi.nlm.nih.gov/39890135/)).
- **Tertiary prevention:** eradication in patients with ulcers, MALT lymphoma, or post-resection gastric cancer to prevent recurrence.
- **Vaccination (not yet available):** *"notwithstanding a proof-of-concept that vaccination can protect children from acquisition of H. pylori infection, there are currently no advanced vaccine candidates with only a single vaccine in Phase I clinical trial"* ([PMID: 29627231](https://pubmed.ncbi.nlm.nih.gov/29627231/)). A parenteral three-antigen vaccine (**VacA + CagA + NAP**) *"was well tolerated and highly immunogenic in healthy adults"* in a randomized phase 1/2 human challenge study ([PMID: 30042064](https://pubmed.ncbi.nlm.nih.gov/30042064/)). Leading antigens: UreB, VacA, CagA, HspA; effective immunity likely requires Th1/Th17 responses ([PMID: 37971157](https://pubmed.ncbi.nlm.nih.gov/37971157/), [PMID: 40776465](https://pubmed.ncbi.nlm.nih.gov/40776465/)).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *H. pylori* (NCBI:txid210). Non-pylori gastric *Helicobacter* species that infect humans zoonotically include *H. suis*, *H. felis*, *H. salomonis*, *H. bizzozeronii*, and *"H. heilmannii"*.
- **Natural / zoonotic disease:** *"Animal Helicobacter species other than Helicobacter pylori are also able to cause human gastritis, gastric ulcers, and MALT lymphomas"* ([PMID: 26155631](https://pubmed.ncbi.nlm.nih.gov/26155631/)). *H. suis* *"infects the stomach of humans and animals such as dogs, cats, pigs, and rodents, the latter giving rise to zoonotic infection"* ([PMID: 28534071](https://pubmed.ncbi.nlm.nih.gov/28534071/)).
- **Reservoirs / host range:** dogs, cats, pigs, primates, cattle, rodents, and even rabbits harbor gastric *Helicobacter* species ([PMID: 15751578](https://pubmed.ncbi.nlm.nih.gov/15751578/)). In humans with non-*H. pylori* spiral bacteria, PCR identified *Candidatus* H. suis (30.9%), *H. salomonis* (11.4%), and *H. felis* (8.9%), with dogs and cats as reservoirs ([PMID: 15872252](https://pubmed.ncbi.nlm.nih.gov/15872252/)).
- **Comparative biology:** these species share cholesteryl-α-glucoside cell-wall biology with *H. pylori* (56% αCgT amino-acid identity) ([PMID: 28534071](https://pubmed.ncbi.nlm.nih.gov/28534071/)), indicating conserved gastric-colonization mechanisms.

---

## 15. Model Organisms

Wild-type rodents do not spontaneously develop gastric adenocarcinoma, but it can be induced by *Helicobacter* infection ([PMID: 15080846](https://pubmed.ncbi.nlm.nih.gov/15080846/)):

| Model | Type | Phenotype recapitulation | Application |
|---|---|---|---|
| **Mongolian gerbil** (*Meriones unguiculatus*) | Induced infection | Develops adenocarcinoma after *H. pylori* infection; recapitulates atrophy→metaplasia→dysplasia→carcinoma | Virulence-gene, dietary-salt, carcinogenesis studies |
| **C57BL/6 mouse + *H. felis*** | Induced infection | Gastric cancer after long-term infection | Host-immune / inflammation studies |
| **INS-GAS transgenic mouse** (FVB/N insulin-gastrin) | Genetic (hypergastrinemic) | Spontaneous carcinoma in old age, greatly accelerated by *Helicobacter* | Gastrin/acid–cancer axis, chemoprevention |

Key quotes: *"gastric adenocarcinoma can be induced in Mongolian gerbils by H. pylori infection and in C57BL/6 mice by long-term H. felis infection"* and *"the hypergastrinaemic INS-GAS mouse, in which gastric carcinoma develops spontaneously in old animals, but the process is greatly accelerated by Helicobacter infection"* ([PMID: 15080846](https://pubmed.ncbi.nlm.nih.gov/15080846/)). These models linked carcinogenesis to a specific molecular mechanism: *"EtHOBA inhibited gastric carcinoma in infected INS-GAS mice and gerbils and attenuated isoLG adducts, DNA damage, and somatic mutation frequency"* ([PMID: 33189701](https://pubmed.ncbi.nlm.nih.gov/33189701/)).

**Limitations:** rodent gastric anatomy/physiology differs from human; models often require East-Asian or highly virulent strains and long timelines; the MALT-lymphoma phenotype is imperfectly modeled.

---

## Mechanistic Model / Interpretation

The unifying model is that a single infectious agent produces a **spectrum of divergent diseases** governed by three axes: (1) **anatomical topography** of the induced gastritis, (2) **bacterial virulence genotype** (*cagA*, *vacA*), and (3) **host inflammatory genotype** (*IL1B*/*IL1RN*). Colonization is universally possible because urease/UreI acid resistance plus motility and adhesion let the organism occupy the gastric mucus niche. Once resident, the outcome bifurcates:

```
INFECTION (childhood) ──> urease/motility/adhesion ──> chronic active gastritis
      │
      ├─ antral-predominant + acid hypersecretion ──> DUODENAL ULCER
      │
      └─ corpus/pangastritis (amplified by IL1B risk alleles + CagA)
             │  hypochlorhydria, ↑nitrite, ↓ascorbate
             │  CagA→SHP-2 (proliferation) + CagA→E-cadherin/β-catenin→CDX1/MUC2 (metaplasia)
             │  inflammation→isoLG DNA adducts→somatic mutation
             └─> ATROPHY→METAPLASIA→DYSPLASIA→ADENOCARCINOMA  (+ MALT LYMPHOMA)
```

The therapeutic corollary is powerful: because the bacterium is a *necessary* upstream cause, **removing it reverses or prevents downstream disease** — ulcers heal, MALT lymphoma regresses in ~97%, and cancer incidence falls by ~40–60% — with the largest benefit when eradication precedes irreversible premalignant change.

---

## Evidence Base

| PMID | Contribution | Role |
|---|---|---|
| [42757050](https://pubmed.ncbi.nlm.nih.gov/42757050/) | Global prevalence 36.3% (2023) | Epidemiology |
| [41115989](https://pubmed.ncbi.nlm.nih.gov/41115989/) | Gastric-cancer PAF ~70% | Causality/burden |
| [41236450](https://pubmed.ncbi.nlm.nih.gov/41236450/) | PAF for PUD/dyspepsia/lymphoma | Burden beyond cancer |
| [28110439](https://pubmed.ncbi.nlm.nih.gov/28110439/) / [27340011](https://pubmed.ncbi.nlm.nih.gov/27340011/) | *IL1B*/*IL1RN* gene×infection risk | Host genetics |
| [26158864](https://pubmed.ncbi.nlm.nih.gov/26158864/) | SNP interaction effect-modification | Host genetics |
| [17237808](https://pubmed.ncbi.nlm.nih.gov/17237808/) / [28338646](https://pubmed.ncbi.nlm.nih.gov/28338646/) | CagA→SHP-2 and β-catenin/CDX1 | Mechanism (in vitro) |
| [12471160](https://pubmed.ncbi.nlm.nih.gov/12471160/) / [24914320](https://pubmed.ncbi.nlm.nih.gov/24914320/) | Urease/UreI, mucus-niche colonization | Colonization biology |
| [9494857](https://pubmed.ncbi.nlm.nih.gov/9494857/) / [9376611](https://pubmed.ncbi.nlm.nih.gov/9376611/) | Topography branch point | Pathophysiology |
| [33189701](https://pubmed.ncbi.nlm.nih.gov/33189701/) | isoLG DNA adducts, EtHOBA | DNA-damage mechanism (model) |
| [38143438](https://pubmed.ncbi.nlm.nih.gov/38143438/) / [42724990](https://pubmed.ncbi.nlm.nih.gov/42724990/) / [41985696](https://pubmed.ncbi.nlm.nih.gov/41985696/) | UBT/SAT/serology accuracy | Diagnostics |
| [29600697](https://pubmed.ncbi.nlm.nih.gov/29600697/) / [26808355](https://pubmed.ncbi.nlm.nih.gov/26808355/) / [41966313](https://pubmed.ncbi.nlm.nih.gov/41966313/) / [34358488](https://pubmed.ncbi.nlm.nih.gov/34358488/) | Regimens, resistance, CYP2C19 | Treatment |
| [35364066](https://pubmed.ncbi.nlm.nih.gov/35364066/) / [32628791](https://pubmed.ncbi.nlm.nih.gov/32628791/) | RCT/Cochrane cancer prevention | Prevention/prognosis |
| [41776408](https://pubmed.ncbi.nlm.nih.gov/41776408/) / [42034998](https://pubmed.ncbi.nlm.nih.gov/42034998/) | MALT lymphoma regression | Prognosis |
| [29627231](https://pubmed.ncbi.nlm.nih.gov/29627231/) / [30042064](https://pubmed.ncbi.nlm.nih.gov/30042064/) / [37971157](https://pubmed.ncbi.nlm.nih.gov/37971157/) | Vaccine status/candidates | Prevention |
| [15080846](https://pubmed.ncbi.nlm.nih.gov/15080846/) | Gerbil/INS-GAS models | Model organisms |
| [26155631](https://pubmed.ncbi.nlm.nih.gov/26155631/) / [28534071](https://pubmed.ncbi.nlm.nih.gov/28534071/) / [15872252](https://pubmed.ncbi.nlm.nih.gov/15872252/) / [15751578](https://pubmed.ncbi.nlm.nih.gov/15751578/) | Zoonotic non-pylori species | Comparative biology |
| [15758899](https://pubmed.ncbi.nlm.nih.gov/15758899/) / [11488660](https://pubmed.ncbi.nlm.nih.gov/11488660/) / [15345211](https://pubmed.ncbi.nlm.nih.gov/15345211/) | Transmission, childhood acquisition | Etiology/epidemiology |

Evidence source types span **human clinical** (RCTs, cohorts, meta-analyses, guidelines), **model organism** (gerbil, mouse), and **in vitro** (CagA signaling, urease biochemistry).

---

## Limitations and Knowledge Gaps

1. **Extragastric associations** (iron-deficiency anemia, B12 deficiency, ITP) rest partly on association and guideline consensus rather than mechanistic proof; molecular-mimicry mechanisms for ITP remain hypothesized ([PMID: 42410737](https://pubmed.ncbi.nlm.nih.gov/42410737/), [PMID: 28727656](https://pubmed.ncbi.nlm.nih.gov/28727656/)).
2. **Prevalence heterogeneity** is large; global averages mask 5-fold regional variation, and declining-prevalence trends may not generalize.
3. **Host genetic risk estimates** (e.g., *IL1B* OR up to 19) come from modest single-population studies with wide confidence intervals and require multi-ethnic replication.
4. **No licensed vaccine** exists; correlates of protective immunity are incompletely defined.
5. **Antibiotic resistance** is rising and geographically variable, undermining empiric regimens; real-world eradication rates increasingly fall below the >90% target.
6. **Non-pylori Helicobacter disease** is under-recognized because standard tests target *H. pylori*.
7. **Model organisms** imperfectly recapitulate human MALT lymphoma and the full Correa cascade timeline.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-guided therapy trials:** prospectively test *CYP2C19*- and 23S rRNA-resistance-guided regimens (P-CAB-based) versus empiric therapy for eradication success.
2. **Multi-ethnic host-genetics replication:** validate *IL1B*/*IL1RN*/*TLR4* risk in large, diverse cohorts with standardized cancer endpoints.
3. **Vaccine development:** advance multivalent VacA/CagA/NAP/UreB candidates through controlled human infection models with defined Th17 correlates.
4. **Screen-and-treat outcome studies:** complete adolescent screen-and-treat RCTs (e.g., NCT05926804) to quantify population-level cancer prevention and cost-effectiveness.
5. **Chemoprevention:** translate dicarbonyl-scavenger (EtHOBA-class) findings from gerbil/INS-GAS models toward human premalignant-lesion trials.
6. **Diagnostics in advanced mucosa:** deploy qPCR/monoclonal-SAT multimodal panels for reliable detection in atrophic/metaplastic stomachs where UBT underperforms.
7. **Non-pylori Helicobacter surveillance:** implement broad-range Helicobacter PCR in culture-negative gastritis with animal contact to capture zoonotic cases.

---

*Report compiled from 15 confirmed findings across 72 reviewed papers over 5 investigation iterations. Ontology suggestions: MONDO:0006781; NCBI:txid210; UBERON:0000945/0001165/0001161/0002114; CL:0002180/0000162/0000155/0000236; GO:0006954/0016477/0006281/0005886/0005634; CHEBI:16199/16134/16301/29073/49786; HPO terms per Section 3; NCIT drug terms per Section 12.*


## Artifacts

- [OpenScientist final report](Helicobacter_Pylori_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Helicobacter_Pylori_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 43 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 43 |
| On topic | 37 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031273` (1 mention) - the report calls it "chronic gastritis"; HP calls it **Shock**
- `HP:0011834` (1 mention) - the report calls it "Symptom"; HP calls it **Moyamoya phenomenon**
- `HP:0025439` (1 mention) - the report calls it "dyspepsia"; HP calls it **Pharyngitis**
- `HP:0001891` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Iron deficiency anemia**
- `HP:0100502` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased circulating vitamin B12 concentration**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012190` (1 mention) - the report calls it "MALT lymphoma"; HP calls it **T-cell lymphoma**
- `HP:0012126` (1 mention) - the report calls it "gastric cancer"; HP calls it **Stomach cancer**, and lists "Gastric cancer" among its other names
- `HP:0001973` (1 mention) - the report calls it "thrombocytopenia"; HP calls it **Autoimmune thrombocytopenia**, and lists "Immune thrombocytopenia" among its other names