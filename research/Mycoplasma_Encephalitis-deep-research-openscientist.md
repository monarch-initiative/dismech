---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T04:15:53.347325'
end_time: '2026-09-30T04:37:07.997482'
duration_seconds: 1274.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mycoplasma Encephalitis
  mondo_id: MONDO:0019377
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
citation_count: 36
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 36
  on_topic: 20
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 31
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 12
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0011446
    reported_labels:
    - abnormal consciousness
    ontology_label: Abnormality of mental function
  - term_id: HP:0001250
    reported_labels:
    - "~28\u201339%; status epilepticus in severe cases"
    ontology_label: Seizure
  - term_id: HP:0100022
    reported_labels:
    - ~38% in basal-ganglia subset
    ontology_label: Abnormality of movement
  - term_id: HP:0000708
    reported_labels:
    - common (esp. anti-NMDAR overlap)
    ontology_label: Atypical behavior
  - term_id: HP:0001251
    reported_labels:
    - ~10% of neuro cases
    ontology_label: Ataxia
  - term_id: HP:0012229
    reported_labels:
    - ~66.7% (basal-ganglia subset)
    ontology_label: CSF pleocytosis
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mycoplasma_Encephalitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mycoplasma_Encephalitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mycoplasma Encephalitis
- **MONDO ID:** MONDO:0019377 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Mycoplasma Encephalitis** covering all of the
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

# Mycoplasma Encephalitis (MONDO:0019377): A Comprehensive Disease Characteristics Report

## Summary

**Mycoplasma encephalitis (MPE)** is an acute, predominantly pediatric inflammation of the brain triggered by infection with *Mycoplasma pneumoniae* (Mp; NCBI:txid2104), the cell-wall–deficient, atypical respiratory bacterium that is one of the most commonly identified infectious causes of childhood encephalitis. Across large referral and prospective cohorts, *M. pneumoniae* accounts for roughly **5–6% of confirmed childhood encephalitis cases** and is the single most frequently identified bacterial pathogen in several encephalitis surveillance projects. It is not a Mendelian, single-gene disorder; it is an infectious/immune-mediated condition (Infectious Disease category), and no causal human gene or established animal model of the extrapulmonary (neurologic) disease exists. Host susceptibility is polygenic/multifactorial, with candidate immune-gene loci modulating *severity of M. pneumoniae respiratory disease* rather than causing encephalitis specifically.

Mechanistically, MPE injures the central nervous system by at least **three overlapping routes**: (1) an **early-onset, direct/CNS-invasive and toxin-mediated** pattern in which the organism reaches the CSF and the CARDS (Community-Acquired Respiratory Distress Syndrome) toxin plus TLR–MyD88–IL-8 innate neuroinflammation drive damage; (2) a **late-onset, post-infectious autoimmune** pattern driven by molecular mimicry, producing anti-galactocerebroside, antiganglioside (anti-GM1), and anti-NMDA-receptor antibodies that cause demyelination/ADEM and other syndromes; and (3) a **vaso-occlusive/thrombotic** route producing cerebral (often watershed) infarction through focal vasculitis, hypercoagulability, and hypoperfusion. These branches are distinguished clinically by prodrome length and by whether the organism is detectable in CSF.

Clinically, MPE presents with altered consciousness, seizures (frequently progressing to refractory status epilepticus in severe cases), headache, fever, and near-universal preceding/concurrent respiratory illness. Diagnosis relies chiefly on **serology** (CSF *M. pneumoniae* PCR is positive in only ~2% of cases). Treatment combines **CNS-penetrating anti-mycoplasmal antibiotics** (macrolides, tetracyclines, fluoroquinolones — β-lactams are ineffective because Mp lacks a cell wall) with **immunomodulation** (corticosteroids, IVIG, plasma exchange). Prognosis is generally favorable with low mortality (≈2.6% in adult meningoencephalitis), but **neurologic sequelae occur in roughly 25–30%**, and MPE complicated by refractory status epilepticus carries substantial morbidity and mortality.

---

## 1. Disease Information

**Overview.** Mycoplasma encephalitis is acute encephalitis (inflammation of the brain parenchyma, often with meningeal involvement → meningoencephalitis) occurring during or shortly after *M. pneumoniae* infection. Neurologic disease is the **most common extrapulmonary complication** of *M. pneumoniae*, with a total incidence of about **0.1% of infections**, and encephalitis is the most common neurologic syndrome within that spectrum ([PMID: 41697567](https://pubmed.ncbi.nlm.nih.gov/41697567/); [PMID: 26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/)).

**Key identifiers.**
- **MONDO:** MONDO:0019377 (Mycoplasma encephalitis)
- **MeSH:** *Encephalitis* (D004660) with *Pneumonia, Mycoplasma* (D011019) / *Mycoplasma pneumoniae* (D009976); no dedicated MeSH descriptor for the encephalitis subtype
- **ICD-10:** Best mapped via *G05.3* (Encephalitis in other diseases classified elsewhere) plus *J15.7 / A49.3* (*M. pneumoniae* infection); ICD-11: *1D01* (encephalitis) with an infectious-agent extension code
- **OMIM/Orphanet:** Not applicable as a Mendelian entry; not a rare genetic disease with an OMIM phenotype number
- **NCBI Taxonomy (causal agent):** *Mycoplasma pneumoniae* NCBI:txid2104

**Synonyms / alternative names:** *M. pneumoniae* encephalitis, *Mycoplasma pneumoniae*-associated encephalitis, mycoplasmal meningoencephalitis, *M. pneumoniae* meningoencephalitis, *M. pneumoniae*-associated CNS disease.

**Information source type.** This report is derived from **aggregated disease-level resources** — published case series, prospective cohorts (California Encephalitis Project, Australian Childhood Encephalitis study, Toronto SickKids series), systematic reviews, and mechanistic/microbiology studies — rather than individual EHR data.

---

## 2. Etiology

**Primary cause — infectious.** MPE is caused by infection with *M. pneumoniae*, a small, self-replicating, cell-wall–deficient bacterium that colonizes the respiratory epithelium via specialized attachment organelles ("gliding" colonization) ([PMID: 42211665](https://pubmed.ncbi.nlm.nih.gov/42211665/)). It is **not genetic** in origin.

**Genetic risk factors (host susceptibility to Mp disease, not MPE-specific).** No germline variant causes MPE. Candidate-gene studies of *M. pneumoniae* pneumonia (MPP) susceptibility in Chinese children have identified associated loci: **ACE rs4340, IL-6 rs1800795, and NOS3 rs1799983** (n=415 cases/300 controls; [PMID: 28403117](https://pubmed.ncbi.nlm.nih.gov/28403117/)); functional eQTL-SNPs including **rs8032531** ([PMID: 35836993](https://pubmed.ncbi.nlm.nih.gov/35836993/)); and **IL2 rs6534349 / IL4 rs2227284** linked to Mp infection and asthma risk ([PMID: 25747600](https://pubmed.ncbi.nlm.nih.gov/25747600/)). These modulate respiratory-disease susceptibility/severity and are best regarded as polygenic modifiers, not causes of encephalitis.

**Environmental risk factors.**
- **Age:** pediatric predominance (median ~7 years for MPE) ([PMID: 41935250](https://pubmed.ncbi.nlm.nih.gov/41935250/))
- **Season:** winter/epidemic peaks; Mp epidemics recur every **3–7 years**, with a post-COVID-pandemic resurgence in 2023–2024 ([PMID: 42560049](https://pubmed.ncbi.nlm.nih.gov/42560049/); [PMID: 42283501](https://pubmed.ncbi.nlm.nih.gov/42283501/))
- **Sex:** modest male predominance in pediatric MPE (43M:28F in one cohort)
- **Exposure:** crowded settings (schools, households) favor transmission

**Protective factors.** No validated genetic protective variants for MPE are established. At the level of *respiratory* disease progression, early β-lactam therapy and EBV coinfection were paradoxically inversely associated with fulminant Mp pneumonia in one case–control study ([PMID: 41772495](https://pubmed.ncbi.nlm.nih.gov/41772495/)) — a respiratory, not neurologic, endpoint. Prompt appropriate anti-mycoplasmal therapy is the principal modifiable protective factor.

**Gene–environment interactions.** Intrafamilial cases infected by **identical A2063G macrolide-resistant strains** showed markedly different disease severity, indicating that **host immune maturity, rather than organism virulence, is the dominant determinant of severity** ([PMID: 19898978](https://pubmed.ncbi.nlm.nih.gov/19898978/)). This is the clearest documented gene/host–environment interaction: identical pathogen exposure, divergent host outcome.

---

## 3. Phenotypes

MPE produces a broad neurologic phenotype superimposed on a systemic inflammatory/respiratory illness.

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| Impaired/altered consciousness | Clinical sign | 90% (pediatric) / 67% (mixed) | HP:0011446 (abnormal consciousness) |
| Headache | Symptom | 87.4% | HP:0002315 |
| Fever | Symptom | 96.5% | HP:0001945 |
| Respiratory involvement | Sign | 94.3% | HP:0002086 |
| Seizures | Clinical sign | ~28–39%; status epilepticus in severe cases | HP:0001250 |
| Movement disorders | Clinical sign | ~38% in basal-ganglia subset | HP:0100022 |
| Behavioral/psychiatric change | Behavioral | common (esp. anti-NMDAR overlap) | HP:0000708 |
| Ataxia / cerebellar signs | Clinical sign | ~10% of neuro cases | HP:0001251 |
| Elevated CRP | Laboratory | 90.8% | HP:0011227 |
| CSF pleocytosis | Laboratory | ~66.7% (basal-ganglia subset) | HP:0012229 |

**Onset:** acute to subacute, typically within days to <2 weeks of the respiratory prodrome. **Severity:** variable — from mild, reversible (MERS-type splenial lesion) to severe with refractory status epilepticus. **Progression:** usually monophasic/acute; episodic seizures may occur acutely; most cases are self-limited with treatment.

**Quality-of-life impact.** In survivors with sequelae, impacts include epilepsy, motor deficits, cognitive/behavioral impairment, and (in a documented hypothalamic case) secondary hypersomnia/narcolepsy-like symptoms with decreased CSF hypocretin-1 ([PMID: 22419016](https://pubmed.ncbi.nlm.nih.gov/22419016/)). No disease-specific EQ-5D/SF-36 data exist for MPE.

Quantitative phenotype data: pediatric MPE (n=87) — consciousness disturbance 90%, headache 87.4%, fever 96.5%, respiratory involvement 94.3%, multisystem involvement 98.2%, elevated CRP 90.8% ([PMID: 37417436](https://pubmed.ncbi.nlm.nih.gov/37417436/)). Adult meningoencephalitis (n=39) — MRI abnormalities 78.9%, leptomeningeal enhancement 55.3%, EEG abnormalities 35.9% ([PMID: 42624009](https://pubmed.ncbi.nlm.nih.gov/42624009/)).

---

## 4. Genetic / Molecular Information

**Causal genes:** **None.** MPE has no Mendelian cause, no causal human gene, and no pathogenic germline variant. It is not listed in ClinVar/OMIM as a monogenic disorder.

**Modifier / susceptibility genes (host, respiratory-disease level):** ACE (rs4340), IL6 (rs1800795), NOS3 (rs1799983), IL2 (rs6534349), IL4 (rs2227284), and eQTL-SNP rs8032531 — all associated with Mp pneumonia susceptibility/severity, not MPE per se ([PMID: 28403117](https://pubmed.ncbi.nlm.nih.gov/28403117/); [PMID: 35836993](https://pubmed.ncbi.nlm.nih.gov/35836993/); [PMID: 25747600](https://pubmed.ncbi.nlm.nih.gov/25747600/)).

**Pathogen genetics (clinically actionable):** Macrolide resistance in *M. pneumoniae* is driven predominantly by the **23S rRNA A2063G point mutation**, with high prevalence in China ([PMID: 42568601](https://pubmed.ncbi.nlm.nih.gov/42568601/); [PMID: 42757852](https://pubmed.ncbi.nlm.nih.gov/42757852/)). The 2023–2024 resurgence coincided with clonal replacement by a **P1-1/ST3 lineage** carrying fixed A2063G macrolide resistance ([PMID: 41586312](https://pubmed.ncbi.nlm.nih.gov/41586312/)).

**Epigenetic / chromosomal information:** Not applicable — no human epigenetic or chromosomal abnormality is associated with MPE.

---

## 5. Environmental Information

**Infectious agent:** *Mycoplasma pneumoniae* (NCBI:txid2104) — the sole and necessary cause. It is a cell-wall–deficient bacterium (class Mollicutes) transmitted person-to-person via respiratory droplets.

**Environmental/lifestyle factors:** Seasonality (winter peaks), epidemic cycling every 3–7 years, and crowded living/schooling conditions increase exposure. No chemical toxin, radiation, or occupational exposure is implicated. CTD-type toxicant associations are not relevant to this infectious disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

```
1. M. pneumoniae colonizes respiratory epithelium via attachment organelle ("gliding" adhesion)
        → leads to local infection and systemic immune activation
                                   │
        ┌──────────────────────────┼───────────────────────────────┐
        ▼ (early, <7d prodrome)     ▼ (late, ≥7d prodrome)          ▼ (vascular)
2a. Organism reaches CNS/CSF   2b. Host mounts antibody response  2c. Infection induces
    (direct invasion)              cross-reactive with neural         hypercoagulable,
        → CARDS toxin (ADP-          antigens (molecular mimicry)      pro-inflammatory
          ribosylating/vacuolating)  → anti-galactocerebroside,        vascular state
          binds sphingomyelin/       anti-GM1 ganglioside,            → focal vasculitis +
          phosphatidylcholine/       anti-NMDAR antibodies             hypercoagulability +
          annexin-A2                   → leads to demyelination        hypoperfusion
        → H2O2 + oxidative damage      (ADEM), receptor              → leads to cerebral
        → TLR–MyD88–IL-8 / NLRP3       dysfunction, basal-ganglia      (watershed) infarction
          inflammasome activation      injury                          → arterial thrombi;
        → results in neuro-          → results in post-              → some CSF MP-PCR+,
          inflammation & neuronal      infectious immune-mediated      elevated D-dimer
          injury                       encephalitis / ADEM
        │                              │                              │
        └──────────────┬───────────────┴──────────────┬─────────────┘
                       ▼                               ▼
3. Blood–brain barrier disruption, cytokine-mediated neuronal dysfunction, edema
        → results in clinical manifestations:
           encephalopathy, seizures (± refractory status epilepticus),
           movement disorders, focal deficits, coma
```

### Detail by category

**Molecular pathways / innate immunity.** The **TLR → MyD88 → IL-8** axis and the **NLRP3 inflammasome** are central innate drivers. CARDS toxin, MyD88, and IL-8 expression are positively correlated with severe Mp pneumonia and disease severity ([PMID: 42572866](https://pubmed.ncbi.nlm.nih.gov/42572866/)); Mp activates the NLRP3 inflammasome in airway injury ([PMID: 42211665](https://pubmed.ncbi.nlm.nih.gov/42211665/)).

**Protein dysfunction / toxin (direct branch).** The **CARDS toxin** is the key virulence factor — an **ADP-ribosylating and vacuolating** exotoxin that binds host membrane phospholipids (sphingomyelin, phosphatidylcholine) and annexin-A2 as receptors, recapitulating the inflammatory and histopathological damage seen in infected tissue ([PMID: 41482890](https://pubmed.ncbi.nlm.nih.gov/41482890/)). Mp also generates **hydrogen peroxide**, causing direct oxidative cytotoxicity ([PMID: 42211665](https://pubmed.ncbi.nlm.nih.gov/42211665/)).

**Immune / autoimmune branch (molecular mimicry).** Anti-galactocerebroside (anti-GalC) antibodies — GalC is a **major CNS myelin component** — were found in the CSF of **8/21 (31%)** Mp patients, implicating antibody-mediated demyelination ([PMID: 17651816](https://pubmed.ncbi.nlm.nih.gov/17651816/); [PMID: 22419016](https://pubmed.ncbi.nlm.nih.gov/22419016/)). Anti-GM1/antiganglioside IgM antibodies accompany reversible basal-ganglia/thalamic involvement ([PMID: 20305125](https://pubmed.ncbi.nlm.nih.gov/20305125/)). Short latency (**62% within two weeks**) supports a para-infectious immune mechanism ([PMID: 41661491](https://pubmed.ncbi.nlm.nih.gov/41661491/)). ADEM occurs in ~12–18% of Mp neurologic cases ([PMID: 26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/); [PMID: 31549170](https://pubmed.ncbi.nlm.nih.gov/31549170/)).

**Vaso-occlusive branch.** Focal vasculitis, hypercoagulability, and hypoperfusion produce **cerebral watershed infarction**, sometimes with arterial thrombi and CSF MP-PCR positivity; elevated D-dimer marks the thrombotic/severe late-onset phenotype ([PMID: 41398820](https://pubmed.ncbi.nlm.nih.gov/41398820/); [PMID: 41935250](https://pubmed.ncbi.nlm.nih.gov/41935250/)).

**Upstream vs downstream.** Upstream = respiratory colonization/infection. The three branches are parallel intermediate mechanisms. Downstream convergence = BBB disruption, neuroinflammation, edema, and neuronal dysfunction producing the clinical syndrome.

**Suggested ontology terms:** GO:0006954 (inflammatory response), GO:0002376 (immune system process), GO:0050900 (leukocyte migration), GO:0097190 (apoptotic signaling), GO:0006979 (response to oxidative stress); CL:0000129 (microglial cell), CL:0000127 (astrocyte), CL:0000540 (neuron); CHEBI:16240 (hydrogen peroxide), CHEBI:18390 (galactocerebroside class).

---

## 7. Anatomical Structures Affected

**Organ / system:** Central nervous system (nervous system, UBERON:0001016); brain (UBERON:0000955). Primary respiratory-tract involvement (lung, UBERON:0002048) precedes/accompanies neurologic disease.

**Regional CNS localization (by syndrome):**
- **Basal ganglia** (UBERON:0002420) and **thalamus** (UBERON:0001897) — symmetric T2/FLAIR hyperintensities in basal-ganglia encephalitis ([PMID: 42475768](https://pubmed.ncbi.nlm.nih.gov/42475768/); [PMID: 20305125](https://pubmed.ncbi.nlm.nih.gov/20305125/))
- **Corpus callosum / splenium** (UBERON:0002336) — reversible splenial lesion (MERS) ([PMID: 32307392](https://pubmed.ncbi.nlm.nih.gov/32307392/))
- **Cerebellum** (UBERON:0002037) — cerebellitis/ataxia ([PMID: 26961264](https://pubmed.ncbi.nlm.nih.gov/26961264/))
- **Brainstem** (UBERON:0002298) — Bickerstaff brainstem encephalitis ([PMID: 26115201](https://pubmed.ncbi.nlm.nih.gov/26115201/))
- **Hypothalamus** (UBERON:0001898) — secondary hypersomnia, diabetes insipidus ([PMID: 22419016](https://pubmed.ncbi.nlm.nih.gov/22419016/))
- **White matter / myelin** — demyelination (ADEM)
- **Cerebral watershed territories** — infarction ([PMID: 41398820](https://pubmed.ncbi.nlm.nih.gov/41398820/))
- **Leptomeninges** — leptomeningeal enhancement in 55.3% of adults ([PMID: 42624009](https://pubmed.ncbi.nlm.nih.gov/42624009/))

**Tissue/cell level:** Neurons (CL:0000540), oligodendrocytes/myelin (CL:0000128), microglia (CL:0000129), astrocytes (CL:0000127), and cerebral vascular endothelium.

**Lateralization:** Frequently **bilateral and symmetric** (basal ganglia, thalamus, splenium, cerebellum); infarcts may be focal/asymmetric.

---

## 8. Temporal Development

**Onset:** Acute to subacute. Two temporal patterns partition the disease (see Key Findings): **early-onset (≤7 days from fever)** with direct/CSF-detectable invasion vs **late-onset (>7 days)** immune-mediated disease ([PMID: 26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/); [PMID: 41935250](https://pubmed.ncbi.nlm.nih.gov/41935250/)). Post-infectious autoimmune presentations show short latency, with 62% presenting within two weeks ([PMID: 41661491](https://pubmed.ncbi.nlm.nih.gov/41661491/)).

**Progression:** Usually **monophasic**. Course ranges from mild, self-limited (MERS, transient basal-ganglia lesions that fully reverse) to fulminant with refractory status epilepticus. Reversible lesions may resolve within 1–4 weeks on imaging ([PMID: 32307392](https://pubmed.ncbi.nlm.nih.gov/32307392/); [PMID: 20305125](https://pubmed.ncbi.nlm.nih.gov/20305125/)).

**Remission / recovery:** Most patients recover, many completely (e.g., 85.7% complete neurological recovery in the basal-ganglia subset at median 3.5 years; [PMID: 42475768](https://pubmed.ncbi.nlm.nih.gov/42475768/)). **Critical intervention window:** early anti-mycoplasmal therapy plus timely immunomodulation during the acute phase.

---

## 9. Inheritance and Population

**Inheritance:** Not applicable — infectious/multifactorial, no Mendelian inheritance, penetrance, anticipation, mosaicism, founder effect, or carrier frequency.

**Epidemiology:**
- Neurologic disease is the most common extrapulmonary complication of Mp, incidence **~0.1% of infections** ([PMID: 41697567](https://pubmed.ncbi.nlm.nih.gov/41697567/)).
- *M. pneumoniae* accounts for **~5–6% of confirmed childhood encephalitis** and is the most frequently identified pathogen in several cohorts (see F001).
- **Age:** pediatric predominance; MPE median ~7 years; adult meningoencephalitis median ~40 years.
- **Sex:** modest male predominance (43M:28F pediatric).
- **Season/geography:** winter onset in ~half of cases; epidemics every 3–7 years; notable post-pandemic surge (2023–2024), with high macrolide resistance in China.

| Cohort | N | Mp finding | PMID |
|---|---|---|---|
| California Encephalitis Project | 1988 referred | 111 acute Mp; 84 pediatric (76%); most frequent pathogen | [17671056](https://pubmed.ncbi.nlm.nih.gov/17671056/) |
| Australian childhood encephalitis | 287 confirmed | 6% Mp | [31549170](https://pubmed.ncbi.nlm.nih.gov/31549170/) |
| SickKids (16-yr) | 42/365 PCR+ | 11.5% attributable neuro disease; encephalitis 52% | [26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/) |

---

## 10. Diagnostics

**Core principle:** Diagnosis is **serology-driven** because direct CSF detection is insensitive. In the California Encephalitis Project, **80%** of Mp-associated cases were diagnosed by serology alone and **CSF PCR was positive in only 2%** ([PMID: 17671056](https://pubmed.ncbi.nlm.nih.gov/17671056/)).

**Laboratory / microbiology:**
- **Serology:** seroconversion, IgM positivity, or a single high titer (≥1:320); paired acute/convalescent titers preferred ([PMID: 42624009](https://pubmed.ncbi.nlm.nih.gov/42624009/)).
- **PCR:** respiratory-tract PCR often positive; **CSF PCR rarely positive** (marks the direct-invasive subset).
- **Intrathecal antibody synthesis** can prove CNS infection ([PMID: 26115201](https://pubmed.ncbi.nlm.nih.gov/26115201/)).
- **Multiplex syndromic panels** (BioFire FA-ME, QIAstat-Dx) include Mp but detect it rarely in CSF, consistent with low CSF burden ([PMID: 41716049](https://pubmed.ncbi.nlm.nih.gov/41716049/)).
- **Inflammatory markers:** elevated CRP (90.8%); D-dimer and LDH mark severe/late-onset disease ([PMID: 37417436](https://pubmed.ncbi.nlm.nih.gov/37417436/); [PMID: 42568601](https://pubmed.ncbi.nlm.nih.gov/42568601/)).
- **CSF:** mild pleocytosis (~66.7% in basal-ganglia subset), oligoclonal bands (42.1%) ([PMID: 42475768](https://pubmed.ncbi.nlm.nih.gov/42475768/)).
- **Autoantibodies (subset):** anti-GalC, anti-GM1/ganglioside, anti-NMDAR.

**Imaging:** MRI abnormalities in ~79% of adults; patterns include symmetric basal-ganglia/thalamic T2/FLAIR hyperintensity, reversible splenial lesion (MERS), cerebellar involvement, white-matter (ADEM) lesions, and watershed infarcts. **EEG:** abnormal in ~36%; focal slow/delta waves predict adverse outcome.

**Diagnostic categories:** definite/probable/possible, graded by strength of microbiologic evidence ([PMID: 26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/)).

**Differential diagnosis:** viral encephalitis (HSV, enterovirus, HHV-6), **anti-NMDAR autoimmune encephalitis** (important overlap — see Section on Key Findings F008), ADEM of other cause, metabolic/toxic encephalopathy.

**Genetic/omics testing:** Not applicable for diagnosis (no causal gene). WGS/WES/panels/karyotyping/CMA have no role.

---

## 11. Outcome / Prognosis

**Overall:** Generally favorable — most cases are acute/monophasic and recoverable — but severe forms carry high morbidity/mortality.

- **Adult meningoencephalitis:** 90-day mortality **2.6%** (unrelated to meningoencephalitis); neurologic sequelae **28.2%** ([PMID: 42624009](https://pubmed.ncbi.nlm.nih.gov/42624009/)).
- **Pediatric MPE:** 9/71 poor outcome (GOS 3); late-onset associated with elevated D-dimer and severe pneumonia ([PMID: 41935250](https://pubmed.ncbi.nlm.nih.gov/41935250/)).
- **Status epilepticus subset:** 67% developed refractory status epilepticus; at 18–86 months, 2 died, 7 developed epilepsy/deficits, **none returned to baseline** ([PMID: 20682202](https://pubmed.ncbi.nlm.nih.gov/20682202/)).
- **Mycoplasma-associated acute encephalitis:** sequelae in 5/12 (42%) in one cohort ([PMID: 17240177](https://pubmed.ncbi.nlm.nih.gov/17240177/)).
- **Reversible syndromes** (MERS, antibody-mediated basal-ganglia lesions) often fully reverse ([PMID: 32307392](https://pubmed.ncbi.nlm.nih.gov/32307392/); [PMID: 20305125](https://pubmed.ncbi.nlm.nih.gov/20305125/)).

**Prognostic factors for adverse outcome:** focal neurological signs, multiple seizures or status epilepticus on admission, leukopenia, focal slow/continuous generalized delta waves on EEG, and focal cortical parenchymal hyperintensity on MRI ([PMID: 17240177](https://pubmed.ncbi.nlm.nih.gov/17240177/)). Early-invasive disease generally carries worse outcomes than reversible immune-mediated forms.

---

## 12. Treatment

**Dual strategy: antibiotics + immunomodulation.**

**Anti-mycoplasmal antibiotics** (must penetrate CNS and target a cell-wall–independent bacterium — **β-lactams are ineffective**):
- **Macrolides** — azithromycin (NCIT: Azithromycin); limited by widespread A2063G resistance ([PMID: 42568601](https://pubmed.ncbi.nlm.nih.gov/42568601/))
- **Tetracyclines** — doxycycline, **minocycline** (used successfully with clinical/CSF hypocretin recovery in an anti-GalC case; [PMID: 22419016](https://pubmed.ncbi.nlm.nih.gov/22419016/))
- **Fluoroquinolones** — for macrolide-resistant strains

**Immunomodulation** (targets the autoimmune/inflammatory branches):
- **Corticosteroids** (NCIT: Corticosteroid) — used in essentially all immune-mediated cases ([PMID: 26961264](https://pubmed.ncbi.nlm.nih.gov/26961264/); [PMID: 20305125](https://pubmed.ncbi.nlm.nih.gov/20305125/))
- **IVIG** (intravenous immunoglobulin)
- **Plasma exchange / plasmapheresis** — for severe/refractory or antibody-mediated disease
- **Rituximab** — reported for anti-NMDAR overlap after steroids/IVIG/plasma exchange ([PMID: 25222311](https://pubmed.ncbi.nlm.nih.gov/25222311/))

**Adjunctive:** anticoagulation/thrombolysis (heparin, aspirin, urokinase) for the vaso-occlusive/infarction branch ([PMID: 41398820](https://pubmed.ncbi.nlm.nih.gov/41398820/)); anticonvulsants for seizures/status epilepticus; supportive/rehabilitative care for sequelae.

**Pharmacogenomics:** Not established for MPE. **Personalized medicine** here means resistance-guided antibiotic selection (23S rRNA A2063G testing → non-macrolide agents) rather than host-genotype-guided therapy.

---

## 13. Prevention

**Primary prevention:** No licensed *M. pneumoniae* vaccine exists. A **three-component subunit vaccine candidate** — P1 protein, P40/90 complex, and a detoxified CARDS toxin mutant — induced protective immunity in preclinical models ([PMID: 42042806](https://pubmed.ncbi.nlm.nih.gov/42042806/)). General measures: respiratory hygiene, reducing transmission in crowded settings.

**Secondary prevention:** Early recognition of neurologic symptoms during/after Mp respiratory illness and prompt initiation of effective (resistance-appropriate) antibiotics plus immunotherapy to limit CNS injury.

**Tertiary prevention:** Aggressive seizure control to avert refractory status epilepticus; anticoagulation where thrombotic mechanisms operate; rehabilitation for sequelae.

**Genetic counseling / screening:** Not applicable (non-genetic disease). **Public-health surveillance** of epidemic cycles and macrolide-resistance genotypes supports population-level control ([PMID: 42757852](https://pubmed.ncbi.nlm.nih.gov/42757852/)).

---

## 14. Other Species / Natural Disease

Mycoplasma species cause **natural CNS disease across multiple animal species** ([PMID: 28889017](https://pubmed.ncbi.nlm.nih.gov/28889017/)):
- ***Mycoplasma agalactiae*** (sheep/goats, NCBI:txid2110) — found in large quantities in brain, causing **non-purulent encephalitis and ataxia** in young animals; CNS histopathology reproduced by experimental intra-mammary infection.
- ***Mycoplasma bovis*** (cattle, NCBI:txid28903) — brain abscesses and fibrinous meningitis in calves/adult cattle.
- **Avian *M. gallisepticum* / *M. synoviae*** — meningeal vasculitis and encephalitis in poultry.
- **Marine mammals** — mycoplasmas isolated from brains of sea mammals.
- **Spiroplasma** — implicated in transmissible spongiform encephalopathies.

**Zoonotic potential:** *M. pneumoniae* is a human-restricted pathogen; the animal mycoplasma encephalitides are largely species-specific and not zoonotic. **Comparative value:** these natural veterinary diseases demonstrate conserved mycoplasmal neuroinvasive and immune-mediated CNS injury mechanisms.

---

## 15. Model Organisms

**No animal model of *M. pneumoniae* extrapulmonary (neurologic) disease has been established** ([PMID: 41697567](https://pubmed.ncbi.nlm.nih.gov/41697567/)): *"the animal model of extrapulmonary manifestations caused by MP has not been established."* This is a major research gap. Existing Mp models focus on **respiratory** infection (mouse/hamster pneumonia models) and are used for vaccine and pathogenesis studies (e.g., CARDS toxin biology, subunit vaccine testing; [PMID: 42042806](https://pubmed.ncbi.nlm.nih.gov/42042806/)). Naturally occurring animal mycoplasma encephalitides (Section 14) serve as **comparative** systems but do not model human MPE directly.

---

## Key Findings (Expanded)

### F001 — *M. pneumoniae* is a leading identifiable infectious cause of childhood encephalitis
Multiple independent cohorts converge on this conclusion. In the **California Encephalitis Project**, of 1988 referred patients, evidence of acute Mp infection was found in 111, of which 84 (76%) were pediatric, making Mp the most frequently identified pathogen ([PMID: 17671056](https://pubmed.ncbi.nlm.nih.gov/17671056/)). A prospective Australian cohort of 287 confirmed childhood encephalitis cases placed Mp at **6%**, on par with HSV ([PMID: 31549170](https://pubmed.ncbi.nlm.nih.gov/31549170/)). A 16-year Toronto SickKids series found 42/365 PCR-positive children (11.5%) with attributable neurologic disease, of which **encephalitis was 52%** ([PMID: 26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/)).

### F002 — Two pathogenetic patterns: early-onset direct/invasive vs late-onset immune-mediated
The SickKids series identified two distinct patterns: (1) **prolonged prodrome (≥7 days)**, respiratory symptoms, a blood IgM response, and Mp detected in the respiratory tract **but not CSF** (immune-mediated); and (2) **brief (<7 days) or no prodrome** with Mp detected in CSF (direct invasion) ([PMID: 26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/)). This early/late split was reproduced in a pediatric MPE cohort ([PMID: 41935250](https://pubmed.ncbi.nlm.nih.gov/41935250/)). Anti-GalC autoantibodies in CSF of 8/21 (31%) supports the autoimmune branch ([PMID: 17651816](https://pubmed.ncbi.nlm.nih.gov/17651816/)).

### F003 — Clinical phenotype: altered consciousness, seizures, movement disorders; frequent sequelae, low mortality
Pediatric MPE (n=87): consciousness disturbance 90%, headache 87.4%, fever 96.5%, respiratory involvement 94.3%, elevated CRP 90.8% ([PMID: 37417436](https://pubmed.ncbi.nlm.nih.gov/37417436/)). Adult meningoencephalitis (n=39): 90-day mortality 2.6% (unrelated), sequelae 28.2% ([PMID: 42624009](https://pubmed.ncbi.nlm.nih.gov/42624009/)).

### F004 — Diagnosis relies on serology/PCR because CSF Mp PCR is rarely positive
80% of Mp-associated cases were diagnosed by serology alone; CSF PCR positive in only 2% ([PMID: 17671056](https://pubmed.ncbi.nlm.nih.gov/17671056/)). Intrathecal antibody synthesis can prove CNS infection ([PMID: 26115201](https://pubmed.ncbi.nlm.nih.gov/26115201/)).

### F005 — Three mechanistic branches of CNS injury
Direct/toxin-mediated (CARDS toxin, MyD88/IL-8; [PMID: 41482890](https://pubmed.ncbi.nlm.nih.gov/41482890/), [PMID: 42572866](https://pubmed.ncbi.nlm.nih.gov/42572866/)); autoimmune/molecular mimicry (anti-GalC, anti-GM1, short latency; [PMID: 17651816](https://pubmed.ncbi.nlm.nih.gov/17651816/), [PMID: 41661491](https://pubmed.ncbi.nlm.nih.gov/41661491/)); vaso-occlusive/thrombotic (watershed infarction, elevated D-dimer; [PMID: 41398820](https://pubmed.ncbi.nlm.nih.gov/41398820/)).

### F006 — Broad CNS syndrome spectrum; encephalitis most common
Neurologic disease is the most common extrapulmonary complication (~0.1%; [PMID: 41697567](https://pubmed.ncbi.nlm.nih.gov/41697567/)). Syndromes: encephalitis (52%), ADEM (12%), transverse myelitis (12%), cerebellar ataxia (10%) ([PMID: 26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/)), plus basal-ganglia encephalitis, MERS, Bickerstaff brainstem encephalitis, opsoclonus-myoclonus-ataxia, and stroke.

### F007 — Epidemiology and treatment
Pediatric predominance (median 7 y, 43M:28F, winter onset in half; [PMID: 41935250](https://pubmed.ncbi.nlm.nih.gov/41935250/)); macrolide resistance via A2063G ([PMID: 42568601](https://pubmed.ncbi.nlm.nih.gov/42568601/)); dual antibiotic + immunomodulatory therapy; preclinical subunit vaccine candidate ([PMID: 42042806](https://pubmed.ncbi.nlm.nih.gov/42042806/)).

### F008 — Overlap with anti-NMDAR autoimmune encephalitis
In the California Encephalitis Project, 4 of 8 non-teratoma anti-NMDAR encephalitis patients had serologic evidence of acute Mycoplasma infection ([PMID: 19718525](https://pubmed.ncbi.nlm.nih.gov/19718525/)). A pediatric anti-NMDAR case with Mp IgM was treated with steroids/IVIG/plasma exchange/rituximab ([PMID: 25222311](https://pubmed.ncbi.nlm.nih.gov/25222311/)). Immune-mediated encephalitis affects older children than infectious encephalitis (median 7.6 vs 1.7 y; [PMID: 31549170](https://pubmed.ncbi.nlm.nih.gov/31549170/)).

### F009 — Comparative/veterinary disease and absence of an MPE animal model
Mycoplasmas cause natural CNS disease across species ([PMID: 28889017](https://pubmed.ncbi.nlm.nih.gov/28889017/)); no animal model of human Mp extrapulmonary disease exists ([PMID: 41697567](https://pubmed.ncbi.nlm.nih.gov/41697567/)).

### F010 — Host genetic/immune-maturity factors modulate severity
Candidate susceptibility loci (ACE, IL-6, NOS3, IL2, IL4) for Mp pneumonia ([PMID: 28403117](https://pubmed.ncbi.nlm.nih.gov/28403117/)); identical resistant strains produced divergent intrafamilial severity, implicating host immune maturity over virulence ([PMID: 19898978](https://pubmed.ncbi.nlm.nih.gov/19898978/)).

### F011 — Prognosis: mostly recoverable, but refractory status epilepticus carries high morbidity/mortality
MPE with status epilepticus: 67% refractory, 2 died / 7 with epilepsy or deficits, none returned to baseline ([PMID: 20682202](https://pubmed.ncbi.nlm.nih.gov/20682202/)). Validated adverse-outcome predictors ([PMID: 17240177](https://pubmed.ncbi.nlm.nih.gov/17240177/)).

---

## Mechanistic Model / Interpretation

MPE is best understood as a **single trigger (M. pneumoniae infection) producing three convergent injury pathways**, partitioned in time by the length of the respiratory prodrome:

| Feature | Early-onset (direct/invasive) | Late-onset (immune-mediated) | Vaso-occlusive |
|---|---|---|---|
| Prodrome | Brief (<7 d) or none | Prolonged (≥7 d) | Variable |
| Organism in CSF | Yes (PCR+) | No (respiratory only) | Sometimes |
| Dominant mechanism | CARDS toxin, H₂O₂, TLR–MyD88–IL-8, NLRP3 | Molecular mimicry (anti-GalC, anti-GM1, anti-NMDAR) → ADEM | Vasculitis, hypercoagulability, hypoperfusion |
| Peripheral marker | Direct detection | Blood IgM response | Elevated D-dimer |
| Representative syndrome | Fulminant encephalitis, status epilepticus | ADEM, basal-ganglia encephalitis, cerebellitis | Watershed infarction |
| Reversibility | Often worse | Frequently reversible | Variable |
| Key evidence | [26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/), [41482890](https://pubmed.ncbi.nlm.nih.gov/41482890/), [42572866](https://pubmed.ncbi.nlm.nih.gov/42572866/) | [17651816](https://pubmed.ncbi.nlm.nih.gov/17651816/), [20305125](https://pubmed.ncbi.nlm.nih.gov/20305125/), [41661491](https://pubmed.ncbi.nlm.nih.gov/41661491/) | [41398820](https://pubmed.ncbi.nlm.nih.gov/41398820/), [41935250](https://pubmed.ncbi.nlm.nih.gov/41935250/) |

This tripartite model explains why MPE demands **both** anti-mycoplasmal antibiotics (for the invasive branch) **and** immunomodulation (for the autoimmune branch), sometimes with anticoagulation (for the thrombotic branch) — and why host immune maturity, not organism virulence, dominates severity.

---

## Evidence Base

| PMID | Contribution |
|---|---|
| [17671056](https://pubmed.ncbi.nlm.nih.gov/17671056/) | Mp = most frequent identified pathogen in California Encephalitis Project; serology-driven diagnosis, CSF PCR+ only 2% |
| [31549170](https://pubmed.ncbi.nlm.nih.gov/31549170/) | Mp = 6% of confirmed childhood encephalitis; infectious younger than immune-mediated |
| [26084846](https://pubmed.ncbi.nlm.nih.gov/26084846/) | Two pathogenetic patterns by prodrome; syndrome spectrum (encephalitis 52%) |
| [37417436](https://pubmed.ncbi.nlm.nih.gov/37417436/) | Quantitative pediatric MPE phenotype |
| [42624009](https://pubmed.ncbi.nlm.nih.gov/42624009/) | Adult meningoencephalitis: imaging, 2.6% mortality, 28.2% sequelae |
| [41482890](https://pubmed.ncbi.nlm.nih.gov/41482890/) | CARDS toxin — ADP-ribosylating/vacuolating virulence factor, phospholipid receptor |
| [42572866](https://pubmed.ncbi.nlm.nih.gov/42572866/) | CARDS TX/MyD88/IL-8 correlate with severity |
| [17651816](https://pubmed.ncbi.nlm.nih.gov/17651816/) | Anti-GalC in CSF of 31% of Mp patients (autoimmune branch) |
| [41661491](https://pubmed.ncbi.nlm.nih.gov/41661491/) | Short latency (62% <2 weeks) supports para-infectious immunity |
| [19718525](https://pubmed.ncbi.nlm.nih.gov/19718525/) | Mp–anti-NMDAR link and differential diagnosis |
| [28889017](https://pubmed.ncbi.nlm.nih.gov/28889017/) | Comparative/veterinary mycoplasma encephalitis |
| [41697567](https://pubmed.ncbi.nlm.nih.gov/41697567/) | Neuro = most common extrapulmonary complication (~0.1%); no animal model |
| [19898978](https://pubmed.ncbi.nlm.nih.gov/19898978/) | Host immune maturity > virulence for severity |
| [20682202](https://pubmed.ncbi.nlm.nih.gov/20682202/) | High morbidity of MPE with status epilepticus |
| [17240177](https://pubmed.ncbi.nlm.nih.gov/17240177/) | Validated prognostic predictors |
| [42568601](https://pubmed.ncbi.nlm.nih.gov/42568601/) | A2063G macrolide resistance; D-dimer/LDH severity predictors |
| [42042806](https://pubmed.ncbi.nlm.nih.gov/42042806/) | Preclinical three-component subunit vaccine (P1, P40/90, detoxified CARDS) |

---

## Limitations and Knowledge Gaps

1. **Definition and coding:** MPE lacks a dedicated OMIM/Orphanet entry and specific ICD code; it is captured via combinations of encephalitis + Mp infection codes, limiting registry-based epidemiology.
2. **Diagnostic uncertainty:** Because CSF PCR is positive in only ~2%, most diagnoses rest on serology, which cannot always distinguish causation from coincident infection — the watershed-infarction case series explicitly asked whether the association was coincidental ([PMID: 41398820](https://pubmed.ncbi.nlm.nih.gov/41398820/)).
3. **No animal model** of extrapulmonary/neurologic disease impedes mechanistic dissection and therapeutic testing ([PMID: 41697567](https://pubmed.ncbi.nlm.nih.gov/41697567/)).
4. **Autoimmune mechanism** evidence is largely from case series and small cohorts; anti-GalC and antiganglioside antibodies are found in only a subset, and the causal weight of each branch per patient is often uncertain.
5. **Host genetics** data pertain to respiratory disease susceptibility (mostly Chinese pediatric cohorts) and may not generalize or apply to encephalitis specifically.
6. **Treatment evidence** is observational; no randomized trials define optimal antibiotic/immunotherapy combinations or timing for MPE.

---

## Proposed Follow-up Experiments / Actions

1. **Develop a murine neuroinvasion model** using intranasal Mp challenge with CARDS-toxin-competent vs detoxified strains to test the direct-injury branch and evaluate CNS-penetrating therapeutics.
2. **Prospective biomarker stratification:** Combine CSF PCR, paired serology, anti-GalC/anti-GM1/anti-NMDAR panels, D-dimer, and cytokines (IL-8, MyD88-axis) to prospectively classify patients into the three mechanistic branches and match therapy accordingly.
3. **Randomized/adaptive trial** of antibiotic-plus-immunotherapy timing (early corticosteroids/IVIG vs standard) stratified by early- vs late-onset phenotype.
4. **Resistance-guided treatment study:** Evaluate whether rapid 23S rRNA A2063G genotyping and non-macrolide selection improves neurologic outcomes during high-resistance epidemics.
5. **Standardize MPE case definitions and ontology mapping** (MONDO, HPO, UBERON) to enable pooled multicenter registries and improve epidemiologic precision.
6. **Advance CARDS-toxin subunit vaccine** ([PMID: 42042806](https://pubmed.ncbi.nlm.nih.gov/42042806/)) and assess whether toxin neutralization reduces neurologic complications.

---

*Evidence source types: predominantly human clinical (cohorts, case series, systematic reviews); mechanistic/in vitro (CARDS toxin biology); comparative/veterinary (natural animal mycoplasma encephalitis); no established model-organism data for the neurologic disease.*


## Artifacts

- [OpenScientist final report](Mycoplasma_Encephalitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mycoplasma_Encephalitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 36 |
| On topic | 20 |
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
| Terms whose name was checked | 23 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0011446` (1 mention) - the report calls it "abnormal consciousness"; HP calls it **Abnormality of mental function**
- `HP:0001250` (1 mention) - the report calls it "~28–39%; status epilepticus in severe cases"; HP calls it **Seizure**
- `HP:0100022` (1 mention) - the report calls it "~38% in basal-ganglia subset"; HP calls it **Abnormality of movement**
- `HP:0000708` (1 mention) - the report calls it "common (esp. anti-NMDAR overlap)"; HP calls it **Atypical behavior**
- `HP:0001251` (1 mention) - the report calls it "~10% of neuro cases"; HP calls it **Ataxia**
- `HP:0012229` (1 mention) - the report calls it "~66.7% (basal-ganglia subset)"; HP calls it **CSF pleocytosis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0097190` (1 mention) - the report calls it "apoptotic signaling"; GO calls it **apoptotic signaling pathway**
- `CHEBI:18390` (1 mention) - the report calls it "galactocerebroside class"; CHEBI calls it **N-acyl-beta-D-galactosylsphingosine**, and lists "galactocerebrosides" among its other names
- `UBERON:0002420` (1 mention) - the report calls it "Basal ganglia"; UBERON calls it **basal ganglion**, and lists "basal ganglia" among its other names
- `UBERON:0001897` (1 mention) - the report calls it "thalamus"; UBERON calls it **dorsal plus ventral thalamus**, and lists "thalamus" among its other names
- `UBERON:0002336` (1 mention) - the report calls it "Corpus callosum / splenium"; UBERON calls it **corpus callosum**