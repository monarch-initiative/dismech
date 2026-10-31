---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T07:43:02.025823'
end_time: '2026-10-19T08:01:55.525848'
duration_seconds: 1133.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodevelopmental Disorder With Characteristic Facial And Ectodermal
    Features And Tetraparesis 1
  mondo_id: MONDO:0975745
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
citation_count: 5
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 36
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 13
  labels_variant: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Characteristic_Facial_And_Ectodermal_Features_And_Tetraparesis_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Characteristic_Facial_And_Ectodermal_Features_And_Tetraparesis_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Characteristic Facial And Ectodermal Features And Tetraparesis 1
- **MONDO ID:** MONDO:0975745 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Characteristic Facial And Ectodermal Features And Tetraparesis 1** covering all of the
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

# Neurodevelopmental Disorder With Characteristic Facial And Ectodermal Features And Tetraparesis-1 (NEDFET1)

**Disease identifiers:** OMIM #620888 · MONDO:0975745 · Gene: *GTPBP1* (HGNC:4669) · Chromosome 22q13.1
**Category:** Mendelian, autosomal recessive
**Report type:** Comprehensive disease-characteristics review for knowledge-base population

---

## Summary

Neurodevelopmental Disorder With Characteristic Facial And Ectodermal Features And Tetraparesis-1 (**NEDFET1**; OMIM #620888, MONDO:0975745) is an ultra-rare, congenital-onset, autosomal recessive multisystem syndrome caused by **biallelic loss-of-function (LoF) variants in *GTPBP1***, a translational GTPase gene on chromosome 22q13.1. The disorder was first delineated as a distinct entity by Salpietro et al. in 2024 ([PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)), who showed that biallelic *GTPBP1* variants produce a phenotype **clinically identical** to that caused by biallelic variants in the paralogous gene *GTPBP2* (Jaberi-Elahi syndrome, OMIM #617988). The authors proposed the unifying clinical name **"GTPBP1/2-related ectodermal neurodevelopmental (GREND) syndrome"** for the combined entity.

The clinical core is a severe, early-onset encephalopathy: **profound neurodevelopmental impairment with inability to sit or walk, axial hypotonia, and absent speech in 100% of patients**, upon which are layered progressive spastic tetraparesis (85%), a choreoathetoid/abnormal movement disorder (75%), hearing and/or visual impairment (70%), hand/foot anomalies (65%), epilepsy (50%), feeding difficulties (40%), and postnatal microcephaly (20%). Patients have a **pathognomonic coarse facial gestalt** (high hairline, bitemporal narrowing, thick/protruding lips, macroglossia) combined with **ectodermal defects** (sparse eyebrows/eyelashes, thin brittle hair, abnormal dentition, yellowish skin). Brain MRI uniformly shows progressive cerebellar atrophy/hypoplasia, corpus callosum hypoplasia/agenesis, hypomyelination, and frontotemporal/cortical underdevelopment.

Mechanistically, GTPBP1 is an **eEF1A-like translational GTPase** that functions in ribosome-associated quality control: it resolves stalled/paused ribosomes and directs aberrant mRNAs toward exosomal surveillance/degradation. Its loss leads to **unresolved, codon-specific ribosome pausing in neurons**, triggering the **GCN2–eIF2α–ATF4 integrated stress response (ISR)** and ultimately neurodegeneration. GTPBP1 and GTPBP2 are **non-redundant partners acting in the same pathway**, explaining the identical human phenotypes. Disease is ultra-rare and strongly consanguinity-associated; diagnosis is by exome/genome sequencing; there is no targeted therapy (management is supportive); and prevention rests on genetic counseling and prenatal/preimplantation testing in at-risk families.

---

## Key Findings

### Finding 1 — NEDFET1 is caused by biallelic loss-of-function *GTPBP1* variants (autosomal recessive)

NEDFET1 (OMIM #620888) is an autosomal recessive disorder caused by **biallelic loss-of-function variants in *GTPBP1*** (OMIM 602245; chromosome 22q13). Salpietro et al. (2024) identified bi-allelic *GTPBP1* variants in affected individuals through whole-exome (WES) and whole-genome (WGS) sequencing. OMIM lists **homozygous variants Y509X, Q555X, and T208A in 4 patients from 3 consanguineous families**. Cell-line studies confirmed a loss-of-function impact. Critically, GTPBP1 LoF produces a phenotype identical to GTPBP2-related Jaberi-Elahi syndrome (OMIM 617988).

> *"Here, we describe individuals carrying bi-allelic GTPBP1 variants that display an identical phenotype with GTPBP2"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

> *"Cell line studies identified a loss-of-function (LoF) impact of the disease-associated variants"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

### Finding 2 — Core phenotype: microcephaly, profound neurodevelopmental impairment, craniofacial + ectodermal features, and tetraparesis

The defining clinical picture combines **microcephaly, profound neurodevelopmental impairment, pathognomonic craniofacial features, and ectodermal defects**, with additional core features of abnormal vision and/or hearing, progressive spasticity, choreoathetoid movements, refractory epilepsy, and brain atrophy. OMIM detail for NEDFET1 adds severe-to-profound neurodevelopmental impairment, delayed motor milestones, **tetraparesis**, axial hypotonia; brain MRI cerebellar atrophy and corpus callosum hypoplasia/agenesis, hypomyelination, and cortical gyral simplification; coarse facies with high hairline, bitemporal narrowing, thick/protruding lips, and macroglossia; and ectodermal signs of sparse eyebrows/eyelashes, thin brittle hair, abnormal dentition, and yellowish skin.

> *"Individuals with bi-allelic GTPBP1 or GTPBP2 variants presented with microcephaly, profound neurodevelopmental impairment, pathognomonic craniofacial features, and ectodermal defects"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

> *"Abnormal vision and/or hearing, progressive spasticity, choreoathetoid movements, refractory epilepsy, and brain atrophy were part of the core phenotype of this syndrome"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

### Finding 3 — Quantified phenotype frequencies (combined GTPBP1/GTPBP2 cohort, n = 20)

In the combined cohort of 20 individuals from 16 families, the phenotype frequencies are as follows:

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Profound neurodevelopmental impairment; inability to sit/walk | 20/20 (100%) | HP:0012736 (profound global developmental delay) |
| Axial hypotonia (from first months) | 20/20 (100%) | HP:0008936 (axial hypotonia) |
| Severe-to-profound intellectual disability, absent speech | 20/20 (100%) | HP:0002187; HP:0001344 (absent speech) |
| Progressive spasticity (lower > upper limbs) | 17/20 (85%) | HP:0001257; HP:0002061 (lower limb spasticity) |
| Abnormal movements from infancy (choreoathetoid) | 15/20 (75%) | HP:0001266 (choreoathetosis) |
| Abnormal hearing and/or vision; poor eye contact | 14/20 (70%) | HP:0000365; HP:0000505; HP:0000817 |
| Hand/foot anomalies (contractures, tapered fingers, pes cavus) | 13/20 (65%) | HP:0001371; HP:0001182; HP:0001761 |
| Seizures (first-year onset; tonic/tonic-clonic/myoclonic) | 10/20 (50%) | HP:0001250 (seizure) |
| → of which drug-resistant | 3/10 (33%) | HP:0002197 |
| Feeding difficulties | 8/20 (40%) | HP:0011968 (feeding difficulties) |
| Postnatal microcephaly (OFC ≤ −3 SD) | 4/20 (20%) | HP:0005484 (postnatal microcephaly) |

Mean OFC at birth was −1.4 SD, indicating that microcephaly is largely **postnatal and progressive** rather than congenital. Brain MRI was abnormal in all available cases: global cerebellar atrophy/hypoplasia, callosal hypoplasia, and frontotemporal underdevelopment/atrophy with opercular involvement.

> *"progressive spasticity (higher in the lower limbs than in the upper limbs) was observed in 17 of 20 affected individuals (85%)"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

> *"In total, 10 of 20 individuals developed seizures (50%)"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

> *"Abnormal hearing and/or vision were reported in most individuals (14/20; 70%)"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

> *"Feeding difficulties were reported in 8 of 20 (40%) individuals"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

### Finding 4 — Molecular/genetic detail of *GTPBP1*

*GTPBP1* (HGNC:4669; NCBI Gene 9567; Ensembl ENSG00000100226; UniProt O00178; 669 amino acids) maps to **chr22q13.1** (GRCh38 chr22:38,705,742–38,738,299). The protein contains a **translational (tr-type) G domain** (aa 158–389) with canonical G1–G5 GTP-binding motifs (G1/P-loop 167–174, G2 switch 206–210, G3 252–255, G4 308–311, G5 366–368); the C-terminus (573–669) is disordered. Subcellular localization is cytoplasmic. gnomAD constraint metrics indicate **intolerance to loss-of-function**: pLI = 0.89, LOEUF = 0.53, LOF Z = 4.20, missense Z = 3.90, observed/expected LoF = 0.37.

The disease variants map directly onto functionally critical regions:
- **p.Thr208Ala (T208A)** — a missense variant within/adjacent to the **G2 switch motif (206–210)** of the GTPase domain.
- **p.Tyr509\* (Y509X)** and **p.Gln555\* (Q555X)** — nonsense variants that truncate the C-terminal region.

All act via loss-of-function, confirmed in cell-line studies.

> *"Cell line studies identified a loss-of-function (LoF) impact of the disease-associated variants"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

### Finding 5 — Biochemical function: eEF1A-like translational GTPase and mRNA surveillance factor

Zinoviev et al. (2018) established that GTPBP1 and GTPBP2 are divergent translational GTPases most closely related to **eEF1A, eRF3, and Hbs1**. GTPBP1 possesses **eEF1A-like elongation activity**, delivering cognate aminoacyl-tRNA to the ribosomal A site in a GTP-dependent manner, and it **stimulates exosomal degradation of mRNAs** in elongation complexes. Critically, GTP hydrolysis is **not** followed by rapid peptide-bond formation; GTPBP1 retains the aa-tRNA and delays its A-site accommodation. In physiological settings this causes a controlled ribosome pause, enabling GTPBP1 to elicit quality-control programs (e.g., recruiting the exosome). GTPBP1 can also deliver **deacylated tRNA** to the A site, which is relevant during cellular stress when deacylated tRNA accumulates.

> *"we demonstrate that GTPBP1 possesses eEF1A-like elongation activity, delivering cognate aminoacyl-transfer RNA (aa-tRNA) to the ribosomal A site in a GTP-dependent manner. It also stimulates exosomal degradation of mRNAs in elongation complexes"* — [PMID: 30108131](https://pubmed.ncbi.nlm.nih.gov/30108131/)

> *"In physiological settings, this would cause ribosome stalling, enabling GTPBP1 to elicit quality control programs; e.g., by recruiting the exosome"* — [PMID: 30108131](https://pubmed.ncbi.nlm.nih.gov/30108131/)

### Finding 6 — Pathophysiology: ribosome-rescue failure drives codon-specific pausing, the ISR, and neurodegeneration

Terrey et al. (2020) demonstrated in mouse that **loss of GTPBP1 during tRNA deficiency in the brain leads to codon-specific ribosome pausing and neurodegeneration**, and that GTPBP1 and GTPBP2 are **non-redundant GTPases functioning in the same pathway** to mitigate ribosome pausing. Ishimura et al. (2014) showed that GTPBP2 is a binding partner of the ribosome-recycling protein **Pelota**, and that its loss combined with a CNS-specific tRNA mutation causes ribosome stalling and widespread neurodegeneration — defining GTPBP2 (and by homology GTPBP1) as a **ribosome-rescue factor**. Ishimura et al. (2016) linked stalled elongation complexes to **GCN2-mediated eIF2α (Ser51) phosphorylation and ATF4 activation (the integrated stress response)**, detected prior to neurodegeneration.

> *"loss of the homologous protein GTPBP1 during tRNA deficiency in the mouse brain also leads to codon-specific ribosome pausing and neurodegeneration"* — [PMID: 33186095](https://pubmed.ncbi.nlm.nih.gov/33186095/)

> *"these non-redundant GTPases function in the same pathway to mitigate ribosome pausing"* — [PMID: 33186095](https://pubmed.ncbi.nlm.nih.gov/33186095/)

> *"loss of GTPBP2, a novel binding partner of the ribosome recycling protein Pelota, in mice with a mutation in a tRNA gene that is specifically expressed in the central nervous system causes ribosome stalling and widespread neurodegeneration"* — [PMID: 25061210](https://pubmed.ncbi.nlm.nih.gov/25061210/)

> *"Increased levels of phosphorylation of eIF2α (Ser51) were detected prior to neurodegeneration in these mice and transcriptome analysis demonstrated activation of ATF4, a key transcription factor in the integrated stress response (ISR) pathway"* — [PMID: 27085088](https://pubmed.ncbi.nlm.nih.gov/27085088/)

### Finding 7 — Neuron-specific vulnerability; patient fibroblasts show LoF without a ribosome-profiling abnormality

Salpietro et al. proposed the unifying name **"GREND syndrome"** for the combined GTPBP1 (NEDFET1) and GTPBP2 (Jaberi-Elahi) entity. Functional assays in patient fibroblasts (semi-quantitative PCR, western blot, ribosome profiling) confirmed loss-of-function but showed **"no significant abnormalities on ribosome profiling,"** implying that the pathology is **neuron-specific** — consistent with the mouse data requiring a CNS-specific tRNA deficiency to unmask ribosome stalling. Reduced expression of the Drosophila ortholog *CG2017* caused locomotor impairment, confirming conserved CNS function.

> *"bi-allelic GTPBP1 and GTPBP2 LoF variants cause an identical, distinct neurodevelopmental syndrome"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

### Finding 8 — Model organisms recapitulate ribosome-rescue pathology

Mouse *Gtpbp1* knockout is **phenotypically silent alone** but causes codon-specific ribosome pausing and neurodegeneration on a CNS tRNA-deficient (n-Tr20) background. *Gtpbp2* (nmf205) mutant mice carrying a CNS-specific tRNA-Arg(UCU) deficiency show ribosome stalling, neurodegeneration, and ISR activation. The Drosophila ortholog *CG2017* (FBgn0037391) knockdown/knockout produces motor impairment, demonstrating evolutionary conservation of the CNS role.

> *"Mutant CG2017 knockout flies display motor impairment, highlighting the conserved role for GTP-binding proteins in CNS development across species"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

---

## Full Section-by-Section Report

### 1. Disease Information

**Overview.** NEDFET1 is a severe, congenital-onset, autosomal recessive neurodevelopmental/neurodegenerative syndrome. It combines profound global developmental impairment, spastic tetraparesis, a movement disorder, and sensory deficits with a distinctive coarse facial gestalt and ectodermal abnormalities (hair, teeth, skin). It is a **ribosomopathy of translational quality control** caused by biallelic loss of GTPBP1.

**Key identifiers.**
- **OMIM:** #620888 (phenotype); 602245 (*GTPBP1* gene)
- **MONDO:** MONDO:0975745
- **Gene:** *GTPBP1* — HGNC:4669; NCBI Gene 9567; Ensembl ENSG00000100226; UniProt O00178
- **Orphanet / ICD-10 / ICD-11 / MeSH:** No dedicated codes identified for this newly delineated (2024) entity; it would be coded under general categories for autosomal recessive syndromic intellectual disability / hereditary spastic/neurodegenerative disorders.

**Synonyms / alternative names.** NEDFET1; GTPBP1-related disorder; the GTPBP1 arm of **"GTPBP1/2-related ectodermal neurodevelopmental (GREND) syndrome."** Clinically identical to and often discussed alongside **Jaberi-Elahi syndrome** (GTPBP2-related, OMIM #617988).

**Source of information.** Aggregated disease-level resources (OMIM) combined with individual-patient-level data from a single multicenter cohort study (Salpietro et al. 2024) plus mechanistic data from mouse/Drosophila/in vitro models.

### 2. Etiology

**Causal factor:** Purely **genetic** — biallelic (homozygous or compound-heterozygous) **loss-of-function variants in *GTPBP1***.

**Genetic risk factors:** The causal variants themselves (Y509X, Q555X, T208A, plus novel frameshift variants reported in GTPBP2-related disease). **Consanguinity** is the dominant risk amplifier — all reported GTPBP1 families were consanguineous, producing homozygosity for rare recessive alleles. No modifier genes or susceptibility loci have been defined.

**Environmental risk factors:** None known or implicated. This is a monogenic Mendelian disorder.

**Protective factors:** None identified beyond the trivial — a single wild-type allele is fully protective (heterozygous carriers are unaffected).

**Gene–environment interactions:** Not applicable / none documented. The only "environmental" dependency is experimental: in mouse models, the neurodegenerative phenotype of *Gtpbp1* loss is unmasked by a co-occurring CNS tRNA deficiency, illustrating a genetic-background dependency rather than an environmental one.

### 3. Phenotypes

See the frequency table in **Finding 3** for quantitative detail and HPO suggestions. Summary of phenotype classes:

- **Neurodevelopmental (100%):** Profound global developmental delay, severe-to-profound intellectual disability, absent speech, inability to sit/walk — congenital onset, severe.
- **Motor (85% / 75% / 100%):** Progressive spastic tetraparesis (lower > upper limbs), choreoathetoid movement disorder, and early axial hypotonia.
- **Craniofacial (pathognomonic):** Coarse facies, high hairline, bitemporal narrowing, thick/protruding lips, macroglossia.
- **Ectodermal:** Sparse eyebrows/eyelashes, thin brittle hair, abnormal dentition, yellowish skin.
- **Sensory (70%):** Hearing and/or visual impairment, poor/absent eye contact.
- **Epilepsy (50%):** First-year onset tonic/tonic-clonic/myoclonic seizures; drug-resistant in ~33% of those affected.
- **Growth:** Postnatal, progressive microcephaly (20% reach ≤ −3 SD; mean birth OFC −1.4 SD).
- **Musculoskeletal (65%):** Interphalangeal contractures, tapered fingers, pes cavus.
- **Feeding (40%):** Feeding difficulties.

**Quality of life:** Severe. Patients are non-ambulatory, non-verbal, with profound dependency for all activities of daily living; combined motor, cognitive, sensory, and seizure burden implies maximal disability across all QoL domains. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder.

### 4. Genetic / Molecular Information

**Causal gene:** *GTPBP1* (see Finding 4 for full identifiers and constraint). A 669-aa cytoplasmic translational GTPase with a tr-type G domain (aa 158–389).

**Pathogenic variants (reported, all homozygous, ACMG pathogenic/likely pathogenic):**

| Variant (protein) | Type | Location | Consequence |
|---|---|---|---|
| p.Thr208Ala (T208A) | Missense | G2 switch motif (206–210) | LoF (GTPase activity) |
| p.Tyr509* (Y509X) | Nonsense | C-terminal region | Truncation / LoF |
| p.Gln555* (Q555X) | Nonsense | C-terminal region | Truncation / LoF |

**Allele frequency:** All are ultra-rare/absent in gnomAD. *GTPBP1* itself is LoF-constrained (pLI 0.89, LOEUF 0.53).

**Origin:** **Germline**, biallelic, recessive. No somatic involvement.

**Functional consequence:** **Loss of function** (confirmed in patient cells). No gain-of-function or dominant-negative mechanism.

**Modifier genes / epigenetics / chromosomal abnormalities:** None defined. *GTPBP2* is a functional paralog whose loss causes an identical disease (locus heterogeneity), but it is not a classical "modifier." No epigenetic mechanism or large chromosomal rearrangement is implicated.

### 5. Environmental Information

**Not applicable.** No environmental factors, lifestyle factors, or infectious agents are implicated. NEDFET1 is a purely monogenic Mendelian disorder.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

```
1.  Biallelic LoF variant in GTPBP1 (T208A / Y509X / Q555X)
       | results in
2.  Loss/dysfunction of the eEF1A-like translational GTPase GTPBP1
       | results in
3.  Failure of ribosome-associated quality control: stalled/paused ribosomes
    are not resolved and aberrant mRNAs are not directed to exosomal surveillance
       | leads to (neuron-specific; inferred to require high translational demand /
       |           tRNA-limited codons, by analogy to mouse)
4.  Unresolved, codon-specific ribosome pausing accumulates in neurons
       | leads to
5.  Activation of GCN2 kinase -> phosphorylation of eIF2-alpha (Ser51)
       | results in
6.  Integrated Stress Response (ISR): ATF4 transcriptional program
       | leads to
7.  Progressive neuronal dysfunction and neurodegeneration
       | manifests as
8.  Cerebellar/callosal/cortical atrophy, hypomyelination (MRI) AND
    profound neurodevelopmental impairment, spastic tetraparesis,
    movement disorder, epilepsy, sensory loss, postnatal microcephaly (clinical)

    BRANCH (inferred, mechanism NOT demonstrated): GTPBP1 loss in
    ectoderm-derived lineages -> craniofacial + ectodermal (hair/teeth/skin)
    defects. The molecular basis of the ectodermal arm is unestablished.
```

**Molecular pathways:** Translation elongation / ribosome-associated quality control; the **GCN2–eIF2α–ATF4 integrated stress response** (the explicitly demonstrated downstream cascade). No Wnt/MAPK/mTOR/PI3K-AKT involvement has been shown.

**Cellular processes:** Ribosome stalling/rescue (GO:0072344 rescue of stalled ribosome), translational elongation (GO:0006414), cellular response to nutrient/amino-acid stress, neuronal homeostasis, and neurodegeneration (regulated cell death inferred downstream).

**Protein dysfunction:** Loss of function of a GTPase — abolished/impaired A-site tRNA delivery and loss of the exosome-recruiting surveillance activity (Finding 5). T208A disrupts the G2 switch; nonsense variants truncate the protein.

**Metabolic / biochemical abnormalities:** No classic enzyme-deficiency metabolite signature; the biochemical defect is a GTPase/translational-quality-control deficiency. No immune involvement, autoimmunity, or inflammation is implicated.

**Tissue damage mechanism:** Chronic proteostatic/translational stress culminating in neuronal loss (cerebellum, cortex, white matter).

**Molecular profiling:** Patient fibroblast **ribosome profiling was normal**, underscoring neuron-specific vulnerability; mouse transcriptomics demonstrated ATF4/ISR activation.

**Suggested GO / CL terms:** GO:0006414 (translational elongation); GO:0072344 (rescue of stalled ribosome); GO:0003924 (GTPase activity); CL:0000540 (neuron); CL:0000121 (Purkinje/cerebellar neuron); CL:0000127 (astrocyte, secondary).

### 7. Anatomical Structures Affected

**Organ / system level (primary):** Central nervous system — **brain**, particularly **cerebellum** (UBERON:0002037), **corpus callosum** (UBERON:0002336), **cerebral cortex** (UBERON:0000956, frontotemporal/opercular), and cerebral **white matter** (hypomyelination, UBERON:0002316).

**Secondary involvement / body systems:** Musculoskeletal (contractures, pes cavus — secondary to spasticity); ectodermal structures — **skin** (UBERON:0002097), **hair** (UBERON:0001037), **teeth** (UBERON:0001091); sensory organs — **eye** (UBERON:0000970), **ear/auditory system** (UBERON:0001690); and the feeding/GI apparatus (feeding difficulty). Head/face growth (microcephaly).

**Tissue / cell level:** Nervous tissue (neurons, especially cerebellar/cortical neurons); ectoderm-derived epithelial tissues.

**Subcellular level:** **Cytoplasm** (GO:0005737) — the site of GTPBP1 action at the **cytosolic ribosome** (GO:0022626). No mitochondrial, nuclear, ER, or lysosomal localization.

**Localization / lateralization:** CNS findings are **bilateral and largely symmetric** (global cerebellar atrophy, callosal hypoplasia, bilateral frontotemporal involvement).

### 8. Temporal Development

- **Onset:** Congenital / neonatal — axial hypotonia present in the first months of life in 100%; developmental impairment evident from infancy. Onset is **chronic/insidious** with an early fixed deficit.
- **Progression:** **Progressive** features — spasticity, microcephaly (postnatal), and brain atrophy worsen over time, superimposed on a static profound developmental baseline. Seizures emerge in the first year.
- **Course:** Chronic, lifelong, non-remitting. No remission patterns.
- **Critical period:** Early postnatal development; no interventional window demonstrated (no disease-modifying therapy exists).

### 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic LoF).
- **Penetrance:** Complete in biallelic individuals (all reported homozygotes affected).
- **Expressivity:** Core features highly consistent; variability in seizures, microcephaly severity, and feeding difficulty.
- **Genetic anticipation / mitochondrial / repeat expansion:** None (not a repeat disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** None established; recurrence is driven by **consanguinity** rather than a shared founder haplotype.
- **Carrier frequency:** Not formally estimated; expected very low given rarity.
- **Epidemiology:** **Ultra-rare.** Only 4 GTPBP1 patients from 3 consanguineous families are reported, within a combined GTPBP1/GTPBP2 (GREND) spectrum of 20 individuals from 16 families worldwide. No prevalence/incidence estimate is available.
- **Demographics:** Consanguineous populations over-represented. No sex-ratio bias (recessive); males and females equally affected. Age distribution: pediatric (identified in infancy/childhood).

> *"20 individuals from 16 families with distinct NDDs and syndromic facial features were investigated by whole-exome (WES) or whole-genome (WGS) sequencing"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

> *"Pathogenic variants in GTPBP2 were recently shown to be an ultra-rare cause of neurodegenerative or neurodevelopmental disorders"* — [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/)

### 10. Diagnostics

**Primary diagnostic modality: molecular genetic testing.** Diagnosis is established by **whole-exome (WES) or whole-genome (WGS) sequencing** identifying biallelic LoF *GTPBP1* variants; gene panels for intellectual disability / neurodegeneration / hereditary spastic paraplegia, or single-gene testing, are alternatives. Segregation (parents heterozygous carriers) confirms recessive inheritance.

**Supportive investigations:**
- **Brain MRI:** Cerebellar atrophy/hypoplasia, corpus callosum hypoplasia/agenesis, hypomyelination, frontotemporal/opercular underdevelopment — a supportive imaging signature.
- **Clinical gestalt:** Pathognomonic coarse face + ectodermal defects aid recognition.
- **EEG:** For seizure characterization in the ~50% with epilepsy.
- **Audiology / ophthalmology:** For the ~70% with sensory impairment.

**Omics diagnostics:** Patient-fibroblast ribosome profiling is **not diagnostic** (normal). No biomarker, metabolomic, or liquid-biopsy test exists.

**Differential diagnosis:** GTPBP2-related Jaberi-Elahi syndrome (clinically identical — distinguished only by gene); other syndromic recessive microcephaly/spasticity disorders with cerebellar atrophy (e.g., SNX14/SCAR20, pontocerebellar hypoplasias); coarse-facies/ectodermal conditions. The ectodermal + coarse-facial + tetraparesis combination plus MRI pattern narrows the field, but molecular confirmation is required.

**Screening:** In at-risk consanguineous families, **cascade carrier testing** and prenatal/preimplantation testing apply. No population newborn screening.

### 11. Outcome / Prognosis

- **Survival / mortality:** No formal survival data. Severity (profound impairment, refractory epilepsy, feeding difficulty, progressive neurodegeneration) implies high morbidity and likely reduced life expectancy, but quantitative figures are unavailable.
- **Morbidity / disability:** Maximal — non-ambulatory, non-verbal, fully dependent; combined motor, cognitive, sensory, and seizure disability.
- **Disease course:** Chronic, lifelong, progressive overlay on a static severe baseline. Complications: aspiration/feeding issues, epilepsy, contractures, and consequences of immobility.
- **Recovery:** None expected; no disease-modifying therapy.
- **Prognostic factors:** Refractory epilepsy and feeding difficulty likely worsen outcome; specific prognostic biomarkers are not defined.

### 12. Treatment

**No targeted or disease-modifying therapy exists.** Management is entirely **supportive and symptomatic**, with suggested NCIT intervention categories:
- **Antiseizure medication** for epilepsy (NCIT: Anticonvulsant Agent) — drug-resistant in ~33% of those with seizures.
- **Spasticity management** — physical therapy, baclofen, botulinum toxin (NCIT: Physical Therapy / Muscle Relaxant).
- **Nutritional support / gastrostomy** for feeding difficulties (NCIT: Nutritional Support).
- **Rehabilitation** — physical, occupational, and speech/communication therapy (NCIT: Rehabilitation Therapy).
- **Sensory support** — hearing aids, visual aids, ophthalmologic/audiologic follow-up.
- **Orthopedic management** of contractures/pes cavus.

**Advanced therapeutics / pharmacogenomics / experimental trials:** None approved or in trial for NEDFET1. No gene, cell, RNA, or targeted therapy. Mechanistically, the ISR (GCN2–eIF2α–ATF4) is a conceptual future target, but no intervention has been tested in this disease.

### 13. Prevention

- **Primary prevention:** Not possible (genetic, congenital). Risk reduction is through **genetic counseling** in consanguineous families and informed reproductive choices.
- **Secondary prevention:** **Carrier screening / cascade testing** in at-risk families; **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** for couples known to carry *GTPBP1* variants.
- **Tertiary prevention:** Supportive care to prevent complications (aspiration, seizures, contractures).
- **Counseling:** Autosomal recessive — 25% recurrence risk per pregnancy for carrier couples; genetic counseling is the cornerstone of prevention.
- **Immunization / public-health / behavioral / environmental measures:** Not applicable.

### 14. Other Species / Natural Disease

- **Orthologs:** Mouse *Gtpbp1* (NCBI Gene 14904; Taxon 10090) and *Gtpbp2*; Drosophila *CG2017* (FBgn0037391; Taxon 7227), with closer paralog *Dgp-1*. Function (ribosome rescue / translational GTPase) is **evolutionarily conserved from fly to mouse to human**.
- **Natural disease in other species:** No naturally occurring GTPBP1 disease in companion animals/wildlife is documented (no OMIA entry identified). All animal data derive from engineered models.
- **Comparative biology:** The CNS role of these GTP-binding proteins is conserved across species (fly motor impairment; mouse neurodegeneration; human encephalopathy).
- **Zoonotic potential:** Not applicable (non-infectious genetic disease).

### 15. Model Organisms

| Model | Genotype | Phenotype | Recapitulation | Reference |
|---|---|---|---|---|
| Mouse (*Mus musculus*) | *Gtpbp1* KO alone | Phenotypically silent | Does not model disease alone | [PMID: 33186095](https://pubmed.ncbi.nlm.nih.gov/33186095/) |
| Mouse | *Gtpbp1* loss + CNS tRNA (n-Tr20) deficiency | Codon-specific ribosome pausing, neurodegeneration | Models neurodegenerative mechanism | [PMID: 33186095](https://pubmed.ncbi.nlm.nih.gov/33186095/) |
| Mouse | *Gtpbp2* nmf205 + CNS tRNA-Arg(UCU) deficiency | Ribosome stalling, neurodegeneration, ISR activation | Models paralog disease + ISR | [PMID: 25061210](https://pubmed.ncbi.nlm.nih.gov/25061210/), [PMID: 27085088](https://pubmed.ncbi.nlm.nih.gov/27085088/) |
| Drosophila (*D. melanogaster*) | *CG2017* knockdown/KO | Locomotor/motor impairment | Models conserved CNS role | [PMID: 38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/) |

**Model limitations:** No patient-allele knock-in mouse exists; no iPSC-derived neuron or brain organoid model has been reported. Mouse neurodegeneration requires an engineered CNS tRNA deficiency to unmask the phenotype. Critically, **the ectodermal and craniofacial features are not recapitulated** in any current model, leaving the ectodermal arm of the mechanism unexplained.

---

## Mechanistic Model / Interpretation

NEDFET1 is best understood as a **neuronal ribosome-rescue (translational quality-control) disorder**. The synthesis below integrates all findings:

```
   GTPBP1 (eEF1A-like tr-GTPase)                 Normal role:
   -----------------------------                 - GTP-dependent A-site tRNA delivery
        | biallelic LoF                          - Deliberate A-site accommodation delay
        v                                        - Exosome recruitment -> mRNA surveillance
   Loss of ribosome-rescue / mRNA surveillance   - Partner of GTPBP2/Pelota pathway
        |
        v
   Stalled/paused ribosomes accumulate --> (NEURON-SPECIFIC; fibroblasts unaffected)
        |
        v
   GCN2 kinase activation -> eIF2-alpha-P (Ser51) -> ATF4 / ISR
        |
        v
   Neurodegeneration (cerebellum, cortex, white matter)
        |
        +--> MRI: cerebellar/callosal/cortical atrophy, hypomyelination
        +--> Clinical: profound impairment, spastic tetraparesis, movement
             disorder, epilepsy, sensory loss, postnatal microcephaly

   [Unexplained branch] GTPBP1 loss -> ectodermal/craniofacial defects
                        (coarse face, hair/teeth/skin) -- mechanism unknown
```

Three features make this model robust: (1) GTPBP1 and GTPBP2 are **non-redundant members of the same pathway**, which explains why their loss produces an **identical** human syndrome (locus heterogeneity → "GREND"); (2) the **neuron-specific vulnerability** (normal fibroblast ribosome profiling; mouse phenotype requiring CNS tRNA stress) explains why a housekeeping translational factor produces a predominantly neurological disease; and (3) the **GCN2–eIF2α–ATF4 ISR** provides a demonstrated, potentially druggable downstream node. The principal unresolved gap is the **ectodermal/craniofacial arm**, which no model reproduces and no mechanism yet explains.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [38118446](https://pubmed.ncbi.nlm.nih.gov/38118446/) | *Bi-allelic variants in GTPBP1/GTPBP2 cause a distinct identical NDD* | Human clinical + fly model | **Defining paper**: gene, inheritance, phenotype, frequencies, LoF, GREND unification |
| [33186095](https://pubmed.ncbi.nlm.nih.gov/33186095/) | *GTPBP1 resolves paused ribosomes to maintain neuronal homeostasis* | Mouse model | Direct in vivo proof GTPBP1 loss → ribosome pausing + neurodegeneration; non-redundancy |
| [25061210](https://pubmed.ncbi.nlm.nih.gov/25061210/) | *Ribosome stalling from CNS tRNA mutation causes neurodegeneration* | Mouse model | Defines Pelota-associated ribosome-rescue pathway and CNS tRNA dependency |
| [27085088](https://pubmed.ncbi.nlm.nih.gov/27085088/) | *GCN2 activation by ribosome stalling* | Mouse / mechanistic | Establishes the eIF2α/ATF4 ISR as the downstream cascade |
| [30108131](https://pubmed.ncbi.nlm.nih.gov/30108131/) | *Functions of GTPBP1 and GTPBP2* | In vitro biochemistry | Defines GTPBP1 as eEF1A-like GTPase with mRNA-surveillance/exosomal activity |
| [42553919](https://pubmed.ncbi.nlm.nih.gov/42553919/) | *Novel homozygous frameshift (Jaberi-Elahi)* | Human case report | Supports the GTPBP2 paralog phenotype (microcephaly, delay, seizures, craniofacial, consanguinity) |

All six primary papers converge on a single coherent model; none contradicts the core conclusions. The Salpietro 2024 paper carries the human genotype–phenotype weight, while the mouse/Drosophila/in vitro papers supply the mechanism. Additional papers in the reviewed set (SNX14/SCAR20, DYT-PRKRA, DCC/HGPPS2, Dyggve-Melchior-Clausen, OFDS type 6) serve as **differential-diagnosis comparators** for consanguineous recessive neurodevelopmental disorders rather than direct GTPBP1 evidence.

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** Only 4 GTPBP1 patients from 3 families are reported; several phenotype frequencies derive from the combined n = 20 GREND cohort (GTPBP1 + GTPBP2). GTPBP1-specific frequencies and natural-history data are uncertain.
2. **No prevalence, incidence, survival, or life-expectancy data** exist for this 2024-delineated disorder.
3. **The ectodermal/craniofacial mechanism is unexplained.** The ribosome-rescue/ISR model cleanly explains the neurological phenotype but not the hair/teeth/skin/facial features; no model reproduces them.
4. **Neuron-specific vulnerability is inferred,** supported by normal patient-fibroblast ribosome profiling and the mouse requirement for CNS tRNA deficiency, but the precise human neuronal trigger (which codons/tRNAs are limiting) is undefined.
5. **No patient-allele knock-in mouse, iPSC-neuron, or organoid model** currently exists.
6. **No ICD/Orphanet/MeSH codes** are yet assigned.
7. **No biomarker and no therapeutic target has been validated** in this disease.

---

## Proposed Follow-up Experiments / Actions

1. **Generate patient-allele models:** Knock-in mice carrying T208A/Y509X/Q555X, and patient-derived iPSC neurons / cerebral and cerebellar organoids, to test whether human alleles reproduce ribosome pausing and the ectodermal phenotype.
2. **Map the ectodermal mechanism:** Conditional *Gtpbp1* deletion in ectoderm/neural-crest lineages plus single-cell transcriptomics of skin/tooth/hair primordia to explain the craniofacial/ectodermal arm.
3. **Define the neuronal codon/tRNA signature:** Ribosome profiling in patient iPSC-neurons (not fibroblasts) to identify the codon-specific pausing predicted by mouse data.
4. **Test ISR modulation:** Evaluate ISR inhibitors (e.g., ISRIB) or GCN2 modulators in models as a proof-of-concept disease-modifying strategy, given demonstrated eIF2α/ATF4 activation.
5. **Expand the cohort via GeneMatcher** to refine GTPBP1-specific phenotype frequencies, penetrance, expressivity, and natural history.
6. **Formal nosology:** Assign Orphanet/ICD-11 codes and register NEDFET1 in rare-disease registries for epidemiologic tracking.
7. **Reproductive genetics:** Establish carrier screening and PGT-M protocols for identified consanguineous families.

---

## Conclusion

NEDFET1 (OMIM #620888; MONDO:0975745) is an ultra-rare, autosomal recessive, congenital-onset ribosome-rescue disorder caused by biallelic loss-of-function variants in the translational GTPase gene *GTPBP1*. It is clinically indistinguishable from GTPBP2-related Jaberi-Elahi syndrome, the two together forming "GREND syndrome." Loss of GTPBP1's eEF1A-like ribosome-rescue and mRNA-surveillance activity leads to neuron-specific ribosome stalling, activation of the GCN2–eIF2α–ATF4 integrated stress response, and progressive neurodegeneration — producing profound developmental impairment, spastic tetraparesis, a movement disorder, sensory deficits, epilepsy, postnatal microcephaly, and a characteristic coarse-facial/ectodermal phenotype. Diagnosis is molecular (WES/WGS); there is no targeted therapy (management is supportive); and prevention rests on genetic counseling and prenatal/preimplantation testing in at-risk consanguineous families.


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Characteristic_Facial_And_Ectodermal_Features_And_Tetraparesis_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Characteristic_Facial_And_Ectodermal_Features_And_Tetraparesis_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 8 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0005484` (1 mention) - the report calls it "postnatal microcephaly"; HP calls it **Secondary microcephaly**, and lists "Microcephaly, postnatal" among its other names
- `GO:0072344` (2 mentions) - the report calls it "rescue of stalled ribosome"; GO calls it **rescue of stalled cytosolic ribosome**
- `CL:0000121` (1 mention) - the report calls it "Purkinje/cerebellar neuron"; CL calls it **Purkinje cell**, and lists "Purkinje neuron" among its other names
- `CL:0000127` (1 mention) - the report calls it "astrocyte, secondary"; CL calls it **astrocyte**
- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0001037` (1 mention) - the report calls it "hair"; UBERON calls it **strand of hair**, and lists "hair" among its other names
- `UBERON:0001091` (1 mention) - the report calls it "teeth"; UBERON calls it **calcareous tooth**, and lists "tooth" among its other names
- `UBERON:0001690` (1 mention) - the report calls it "ear/auditory system"; UBERON calls it **ear**, and lists "auditory apparatus" among its other names

35 of 36 terms resolved to a current term; the rest could not be looked up either way.