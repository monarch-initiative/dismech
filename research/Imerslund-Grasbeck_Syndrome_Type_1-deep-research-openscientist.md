---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-09T14:53:11.628747'
end_time: '2026-09-09T15:07:33.762552'
duration_seconds: 862.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Imerslund-Grasbeck Syndrome Type 1
  mondo_id: MONDO:0100156
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 15
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 19
  relevance_assessed: 19
  on_topic: 15
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 25
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 9
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: CL:0002254
    reported_labels:
    - enterocyte of epithelium of small intestine
    - Ileal enterocyte / absorptive brush-border cell
    ontology_label: epithelial cell of small intestine
  - term_id: HP:0012325
    reported_labels:
    - Methylmalonic aciduria
    ontology_label: Chronic myelomonocytic leukemia
  - term_id: NCIT:C542
    reported_labels:
    - Hydroxocobalamin
    ontology_label: Heterocyclic Compound
  - term_id: NCIT:C29273
    reported_labels:
    - Cyanocobalamin/Vitamin B12
    ontology_label: Aluminum Hydroxide/Magnesium Hydroxide
  - term_id: GO:0006810
    reported_labels:
    - Protein reabsorption / transcytosis
    ontology_label: transport
  labels_variant: 6
  obsolete_terms:
  - term_id: NCIT:C29273
    ontology_label: Aluminum Hydroxide/Magnesium Hydroxide
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Imerslund-Grasbeck_Syndrome_Type_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Imerslund-Grasbeck_Syndrome_Type_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Imerslund-Grasbeck Syndrome Type 1
- **MONDO ID:** MONDO:0100156 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Imerslund-Grasbeck Syndrome Type 1** covering all of the
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

# Imerslund-Gräsbeck Syndrome Type 1 (IGS-1): Comprehensive Disease Characteristics Report

**Disease:** Imerslund-Gräsbeck Syndrome Type 1 (Megaloblastic Anemia 1, MGA1)
**MONDO ID:** MONDO:0100156 · **OMIM:** #261100 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** *CUBN* (cubilin), chromosome 10p12.1

---

## Summary

Imerslund-Gräsbeck Syndrome type 1 (IGS-1; also called megaloblastic anemia 1, MGA1) is a rare autosomal recessive disorder of **selective intestinal vitamin B12 (cobalamin) malabsorption** caused by biallelic pathogenic variants in *CUBN*, the gene encoding **cubilin**. Cubilin is a 460-kDa multiligand peripheral membrane endocytic receptor that, together with its obligate partner **amnionless (AMN)**, forms the **cubam** receptor complex. Cubam mediates two physiologically distinct functions: (1) uptake of the **intrinsic factor–vitamin B12 (IF–Cbl)** complex across the ileal brush border, and (2) reabsorption of filtered low-molecular-weight plasma proteins (albumin, transferrin, vitamin D-binding protein, apolipoprotein A-I) in the **renal proximal tubule**. Loss of cubilin function therefore produces the syndrome's two hallmark features: **selective B12 malabsorption not correctable by exogenous intrinsic factor**, and **benign low-molecular-weight proteinuria**.

Clinically, IGS-1 presents in infancy or early childhood (typically from ~4 months up to several years of age) with **megaloblastic anemia**, **failure to thrive**, **recurrent infections**, and—if untreated—**neurological/neurocognitive damage** that can be the sole presenting manifestation. Mild proteinuria without renal insufficiency is present in roughly half of patients. The metabolic signature of intracellular B12 deficiency (methylmalonic aciduria and hyperhomocysteinemia) accompanies the hematologic picture. Prevalence is approximately **1:200,000**, with the highest rates in Finland (0.8/100,000) and Norway due to founder effects, and additional clusters in Middle Eastern countries driven by consanguinity. IGS type 2 is the allelic disorder caused by *AMN* mutations (chromosome 14).

The disorder is exquisitely treatable: **lifelong parenteral (intramuscular) hydroxocobalamin/cyanocobalamin** fully corrects the anemia and metabolic derangement, and early treatment allows complete recovery. Maintenance dosing as infrequent as 1 mg twice yearly can suffice. Prognosis is excellent with timely diagnosis, but **delayed diagnosis can leave permanent neurodevelopmental deficits**, and the proteinuria persists lifelong (though benign). The molecular defect is well characterized at atomic resolution: the Finnish founder mutation **p.Pro1297Leu (FM1)** lies in the IF–Cbl-binding region (CUB domains 5–8) and impairs IF–Cbl recognition, and the crystal structure of IF–Cbl bound to cubilin CUB5–8 reveals a Ca²⁺-dependent "dual-point" binding mode. Naturally occurring canine IGS models (Beagles, Border Collies) faithfully recapitulate the human disease.

---

## Key Findings

### F001 — IGS-1 is an autosomal recessive selective B12 malabsorption disorder caused by biallelic *CUBN* mutations

IGS type 1 (megaloblastic anemia 1, MGA1; OMIM #261100; MONDO:0100156) is caused by biallelic loss-of-function and missense mutations in **CUBN** on chromosome **10p12.1**, encoding cubilin, the intrinsic factor–vitamin B12 receptor. The landmark linkage and positional cloning study by Aminoff et al. (1999) refined the MGA1 locus by linkage-disequilibrium mapping, fine-mapped *CUBN*, and identified two independent disease-specific *CUBN* mutations across 17 Finnish MGA1 families, establishing *CUBN* as causal:

> "We have now refined the MGA1 region by linkage disequilibrium (LD) mapping, fine-mapped CUBN and identified two independent disease-specific CUBN mutations in 17 Finnish MGA1 families. Our genetic and molecular data indicate that mutations in CUBN cause MGA1." — [PMID: 10080186](https://pubmed.ncbi.nlm.nih.gov/10080186/)

Genetic heterogeneity underlies the syndrome: IGS type 1 results from *CUBN* variants (chr 10), whereas the clinically indistinguishable IGS type 2 results from *AMN* variants (chr 14):

> "the molecular basis of the selective malabsorption and proteinuria involves a mutation in one of two genes, cubilin (CUBN) on chromosome 10 or amnionless (AMN) on chromosome 14" — [PMID: 16722557](https://pubmed.ncbi.nlm.nih.gov/16722557/)

**Ontology/annotation suggestions:** MONDO:0100156; HGNC gene *CUBN*; inheritance HP:0000007 (autosomal recessive).

### F002 — Cubam (cubilin + amnionless) is a dual-tissue endocytic receptor: ileal B12 uptake and renal protein reabsorption

Cubilin is a large peripheral membrane endocytic receptor containing **27 CUB domains** for ligand binding. It has no transmembrane anchor of its own and depends on the membrane protein **amnionless (AMN)** for correct apical membrane translocation—together they constitute the **cubam** complex. In the renal proximal tubule, cubilin additionally cooperates with **megalin (LRP2)**. Its ligand repertoire includes IF–B12, albumin, transferrin, and vitamin D-binding protein:

> "Cubilin is a large endocytic receptor serving such diverse functions as the intestinal absorption of the intrinsic factor-B(12) complex and the renal proximal tubule reabsorption of filtered proteins including albumin, transferrin, vitamin D-binding protein and other important plasma carriers. Cubilin is a structurally unique, peripheral membrane protein, which depends on the membrane protein amnionless (AMN) for correct apical translocation." — [PMID: 23291372](https://pubmed.ncbi.nlm.nih.gov/23291372/)

> "CUBN encodes for cubilin, an intestinal and proximal tubular uptake receptor containing 27 CUB domains for ligand binding." — [PMID: 31613795](https://pubmed.ncbi.nlm.nih.gov/31613795/)

This dual function explains why loss of cubilin causes **both** B12 malabsorption **and** low-molecular-weight proteinuria—the two are mechanistically linked through a single receptor operating in two epithelia.

**Ontology suggestions:** GO:0006898 (receptor-mediated endocytosis); UBERON:0002116 (ileum); UBERON:0001232 (renal proximal tubule); CL:0002306 (epithelial cell of proximal tubule); CL:0002254 (enterocyte of epithelium of small intestine).

### F003 — Epidemiology: ~1:200,000 prevalence, founder effects in Scandinavia, consanguinity clusters in the Middle East

Overall prevalence is approximately **1:200,000**, highest in Finland (**0.8/100,000**). Tanner et al. (2004) studied 42 sibships and found a striking geographic gene distribution: **all Finnish cases were due to *CUBN* (three mutations)** and **all Norwegian cases due to *AMN* (two mutations)**, whereas Turkey, Israel, and Saudi Arabia showed a mix of *AMN* and *CUBN* mutations. The Scandinavian aggregation reflects **founder effects**; the Middle Eastern clusters reflect **consanguinity**. Estimated prevalence based on Scandinavian data is **<6:1,000,000**.

> "We studied 42 sibships and found all cases in Finland to be due to CUBN (three different mutations) and all cases in Norway to be due to AMN (two different mutations), while in Turkey, Israel, and Saudi Arabia, there were two different AMN mutations and three different CUBN mutations." — [PMID: 15024727](https://pubmed.ncbi.nlm.nih.gov/15024727/)

> "The syndrome was first described in Finland and Norway where the prevalence is about 1:200,000." — [PMID: 16722557](https://pubmed.ncbi.nlm.nih.gov/16722557/)

> "MGA1 occurs worldwide, but its prevalence is higher in several Middle Eastern countries and Norway, and highest in Finland (0.8/100,000)." — [PMID: 10080186](https://pubmed.ncbi.nlm.nih.gov/10080186/)

### F004 — Clinical phenotype: childhood-onset megaloblastic anemia, failure to thrive, neurological damage, and mild proteinuria (~50%)

The core clinical features are: **juvenile megaloblastic anemia** responsive to parenteral B12; **failure to thrive and grow**; **recurrent infections**; and **neurological damage**, which may be the only manifestation. **Mild proteinuria without kidney disease** is present in about half of patients. Symptoms characteristically appear from **~4 months** up to several years after birth—not immediately at birth, distinguishing IGS from transcobalamin deficiency. B12 absorption tests show low absorption **not corrected by adding intrinsic factor**. Associated biochemical abnormalities include **methylmalonic aciduria**, **hyperhomocysteinemia**, and **pancytopenia**; subacute combined degeneration (funicular myelosis) has been reported.

> "Other manifestations include failure to thrive and grow, infections and neurological damage. Mild proteinuria (with no signs of kidney disease) is present in about half of the patients." — [PMID: 16722557](https://pubmed.ncbi.nlm.nih.gov/16722557/)

> "The symptoms appear from 4 months (not immediately after birth as in transcobalamin deficiency) up to several years after birth." — [PMID: 16722557](https://pubmed.ncbi.nlm.nih.gov/16722557/)

> "Patients may if untreated, develop severe neurocognitive manifestations. If recognized and treated with sufficient doses of vitamin B12, patients recover completely." — [PMID: 37710296](https://pubmed.ncbi.nlm.nih.gov/37710296/)

**Suggested HPO terms:**

| Phenotype | HPO term | Frequency | Onset |
|---|---|---|---|
| Megaloblastic anemia | HP:0001889 | Very frequent (hallmark) | Infancy/childhood |
| Failure to thrive | HP:0001508 | Frequent | Infancy/childhood |
| Recurrent infections | HP:0002719 | Frequent | Childhood |
| Cognitive/neurological impairment | HP:0002376 / HP:0100543 | Variable | Childhood (if untreated) |
| Proteinuria (LMW) | HP:0000093 | ~50% | Childhood, persistent |
| Methylmalonic aciduria | HP:0012325 | Frequent | Childhood |
| Hyperhomocysteinemia | HP:0002160 | Frequent | Childhood |
| Pancytopenia | HP:0001876 | Occasional | Childhood |

### F005 — Treatment is lifelong parenteral B12; naturally occurring canine models recapitulate the disease

Management is **lifelong parenteral (intramuscular) hydroxocobalamin or cyanocobalamin**. Early diagnosis and treatment are life-saving and prevent deterioration. Boina Abdallah et al. (2012) demonstrated that a maintenance dose of **1 mg cobalamin twice yearly** kept clinical, hematological, and metabolic parameters normal in 7 patients:

> "we showed that a maintenance dosage of 1 mg cobalamin twice a year was enough to ensure a normal clinical status and keep the hematological and metabolic parameters in the normal range" — [PMID: 22854512](https://pubmed.ncbi.nlm.nih.gov/22854512/)

**Naturally occurring IGS** occurs in dogs and provides validated disease models: Beagles (*CUBN* c.786delC frameshift, p.Asp262Glufs*47), Border Collies (*CUBN* c.8392delC, p.Gln2798Rfs*3; and an exon 53 frameshift), and AMN mutations in Giant Schnauzers/Australian Shepherds. Affected Beagles reproduce the full human phenotype:

> "Juvenile-affected Beagles exhibited failure to thrive, dyshematopoiesis with neutropenia, serum cobalamin deficiency, methylmalonic aciduria, hyperammonemia, and proteinuria. Affected dogs' kidneys lacked detectable cubilin protein. All affected dogs were homozygous for a single-base deletion in CUBN exon 8 (CUBN c.786delC)" — [PMID: 24433284](https://pubmed.ncbi.nlm.nih.gov/24433284/)

**Suggested NCIT terms:** NCIT:C542 (Hydroxocobalamin); NCIT:C29273 (Cyanocobalamin/Vitamin B12); intramuscular route NCIT:C28161.

### F006 — Prognosis is excellent with early treatment; late diagnosis leaves residual deficits; proteinuria persists

With adequate lifelong B12 replacement, anemia and neurological signs resolve and patients recover completely. However, long-term follow-up of late- or severely-affected children documents **persistent failure to thrive and physical/mental retardation with microcephaly**, indicating that **delayed diagnosis can cause irreversible neurodevelopmental sequelae**:

> "Long-term follow up showed failure to thrive in the girl and physical and mental retardation, microcephaly in her brother." — [PMID: 26958680](https://pubmed.ncbi.nlm.nih.gov/26958680/)

The proteinuria persists lifelong but is benign (normal renal function). Notably, C-terminal *CUBN* variants can cause **isolated chronic proteinuria/albuminuria without B12 malabsorption**, expanding the *CUBN* phenotypic spectrum and demonstrating a genotype–phenotype relationship in which the location of the variant within cubilin determines which of the two receptor functions is impaired:

> "biallelic pathogenic variants in the CUBN gene were associated with chronic isolated proteinuria and early childhood onset... renal function was normal in all cases" — [PMID: 31613795](https://pubmed.ncbi.nlm.nih.gov/31613795/)

### F007 — Finnish founder mutation FM1 (p.Pro1297Leu) impairs IF–B12 binding within cubilin CUB domains 5–8

Most Finnish MGA1/IGS-1 patients carry the disease-specific missense mutation **p.Pro1297Leu (P1297L, "FM1")**. Kristiansen et al. (2000) used surface plasmon resonance to show that P1297L—located in the IF–Cbl-binding cubilin region (CUB domains 5–8, residues 928–1386)—**specifically increases the K_d for IF–Cbl binding several-fold, largely by decreasing the association rate constant**, and that the mutant fails to inhibit uptake of ¹²⁵I-IF–Cbl in cubilin-expressing cells:

> "Most Finnish patients with MGA1 carry the disease-specific P1297L mutation (FM1) in the IF-B(12) receptor, cubilin." — [PMID: 10887099](https://pubmed.ncbi.nlm.nih.gov/10887099/)

> "the P1297L substitution specifically increases the K(d) for IF-Cbl binding several-fold, largely by decreasing the association rate constant" — [PMID: 10887099](https://pubmed.ncbi.nlm.nih.gov/10887099/)

The structural basis was resolved by Andersen et al. (2010), who determined the crystal structure of the IF–Cbl / cubilin CUB5–8 complex at 3.3 Å, revealing that two distant CUB domains embrace cobalamin via Ca²⁺-dependent binding of the two IF domains—a "dual-point" recognition model:

> "the crystal structure of the complex between IF-Cbl and the cubilin IF-Cbl-binding-region (CUB(5-8)) determined at 3.3 A resolution" — [PMID: 20237569](https://pubmed.ncbi.nlm.nih.gov/20237569/)

### F008 — Cubilin is a 460-kDa multiligand receptor (8 EGF + 27 CUB domains) with two ligand-binding regions and megalin-dependent internalization

Cubilin (gp280; *CUBN*) is a **460-kDa** peripheral membrane protein composed of **8 EGF-like repeats and 27 CUB domains**. It interacts with two molecular partners: **AMN** (for plasma-membrane transport) and **Lrp2/megalin** (essential for efficient internalization):

> "Cubilin is a peripheral membrane protein consisting of 8 Epidermal Growth Factor (EGF)-like repeats and 27 CUB (defined as Complement C1r/C1s, Uegf, BMP1) domains. This structurally unique protein interacts with at least two molecular partners, Amnionless (AMN) and Lrp2/Megalin. AMN is involved in appropriate plasma membrane transport of Cubilin whereas Lrp2 is essential for efficient internalization of Cubilin and its ligands." — [PMID: 30295181](https://pubmed.ncbi.nlm.nih.gov/30295181/)

Cubilin has **two distinct ligand-binding regions**—an N-terminal region (113-residue N-terminus + EGF repeats + CUB1-2) and the CUB6-8 region—both of which bind IF–Cbl and albumin:

> "cubilin contains two distinct regions that bind both IF-Cbl and albumin" — [PMID: 11581259](https://pubmed.ncbi.nlm.nih.gov/11581259/)

Cubilin also modulates Fgf8 signaling in embryonic development, and megalin's role in vitamin B12/folate carrier handling extends the biology into renal vitamin homeostasis (PMID: 16760376, PMID: 11375443).

**Suggested ontology terms:** UniProt O60494 (CUBN human); GO:0005905 (clathrin-coated pit); GO:0031232 (extrinsic component of external side of plasma membrane); CHEBI:17439 (cyanocobalamin); CHEBI:18408 / cobalamin.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (from initiating lesion to clinical manifestation)

```
1. Biallelic pathogenic variant in CUBN (e.g., p.Pro1297Leu, frameshift/nonsense)
        │  leads to
2. Absent or functionally defective cubilin protein
        │  (missense in CUB5–8 → impaired IF–Cbl affinity;
        │   truncating variants → loss of surface expression / NMD)
        ├─────────────── BRANCH A (intestine) ───────────────┐
        │                                                    │
3A. Cubam receptor cannot bind/endocytose IF–Cbl at        3B. Cubam cannot reabsorb
    the ileal brush border                                     filtered LMW proteins in
        │  results in                                          the renal proximal tubule
4A. Selective malabsorption of dietary vitamin B12              │  results in
    (NOT corrected by exogenous intrinsic factor)          4B. Urinary loss of albumin,
        │  leads to                                             transferrin, apoA-I, DBP
5A. Systemic cobalamin deficiency                              │  manifests as
        │  results in                                       5B. Benign low-molecular-weight
6A. Impaired methionine synthase + methylmalonyl-CoA            proteinuria (~50% of patients,
    mutase activity → ↑ homocysteine, ↑ methylmalonic acid      normal renal function)
        │  leads to
7A. Impaired DNA synthesis in rapidly dividing cells
    → megaloblastic (ineffective) hematopoiesis
        │  manifests as
8A. Megaloblastic anemia, pancytopenia, failure to thrive,
    recurrent infections
        │  and (via impaired myelin/CNS methylation) leads to
9A. Neurological/neurocognitive damage
    (may be irreversible if diagnosis delayed)
```

Steps 6A–9A are the standard, well-established biochemistry of intracellular B12 deficiency (inferred from cobalamin metabolism rather than demonstrated specifically in IGS tissue). Steps 3A/3B are directly demonstrated by binding assays, canine kidney cubilin loss, and human urinary proteomics.

### Upstream vs downstream

- **Upstream (primary lesion):** *CUBN* mutation → cubilin loss of function. The single molecular defect bifurcates into two anatomically separate consequences because cubam operates in two epithelia.
- **Downstream (intestinal arm):** B12 deficiency → methylmalonic acidemia + hyperhomocysteinemia → megaloblastic hematopoiesis and neurological injury. This arm is **treatable and reversible** by bypassing the absorption defect with parenteral B12.
- **Downstream (renal arm):** LMW proteinuria. This arm is **not corrected** by B12 and persists lifelong, but is clinically benign.

### Genotype–phenotype logic

The location of the *CUBN* variant predicts the phenotype:
- Variants in the **IF–Cbl-binding region (CUB5–8)** or that abolish surface expression → classic IGS-1 (B12 malabsorption ± proteinuria).
- **C-terminal** variants can cause **isolated proteinuria with intact B12 absorption** (PMID: 31613795), because they perturb renal reabsorption while sparing the intestinal IF–Cbl function.

### Cell types and processes involved

| Level | Entity | Ontology |
|---|---|---|
| Cell (intestine) | Ileal enterocyte / absorptive brush-border cell | CL:0002254 |
| Cell (kidney) | Proximal tubule epithelial cell | CL:0002306 |
| Tissue | Ileal mucosa; renal proximal convoluted tubule | UBERON:0002116; UBERON:0001232 |
| Process | Receptor-mediated endocytosis | GO:0006898 |
| Process | Cobalamin metabolic process | GO:0009235 |
| Process | Protein reabsorption / transcytosis | GO:0006810 |
| Subcellular | Apical plasma membrane, clathrin-coated pit, endosome | GO:0016324; GO:0005905 |

---

## Evidence Base

| PMID | Type | Contribution |
|---|---|---|
| [10080186](https://pubmed.ncbi.nlm.nih.gov/10080186/) | Human genetics (landmark) | Established *CUBN* mutations cause MGA1/IGS-1; Finnish prevalence 0.8/100,000 |
| [16722557](https://pubmed.ncbi.nlm.nih.gov/16722557/) | Clinical review | Defines two-gene basis (CUBN/AMN), clinical features, ~50% proteinuria, onset window, prevalence 1:200,000 |
| [15024727](https://pubmed.ncbi.nlm.nih.gov/15024727/) | Population genetics | Founder effects (Finland=CUBN, Norway=AMN) vs consanguinity (Middle East) |
| [10887099](https://pubmed.ncbi.nlm.nih.gov/10887099/) | In vitro / biophysics | FM1 p.P1297L increases K_d for IF–Cbl; functional mechanism |
| [20237569](https://pubmed.ncbi.nlm.nih.gov/20237569/) | Structural biology | 3.3 Å crystal structure of IF–Cbl/cubilin CUB5–8; dual-point Ca²⁺ binding |
| [11581259](https://pubmed.ncbi.nlm.nih.gov/11581259/) | Biochemistry | Two distinct ligand-binding regions of cubilin |
| [30295181](https://pubmed.ncbi.nlm.nih.gov/30295181/) | Review | 460-kDa architecture (8 EGF + 27 CUB); AMN and megalin partners |
| [23291372](https://pubmed.ncbi.nlm.nih.gov/23291372/) | Review | Dual intestinal/renal function; AMN dependence |
| [31613795](https://pubmed.ncbi.nlm.nih.gov/31613795/) | Human genetics | C-terminal CUBN variants → isolated benign proteinuria (genotype–phenotype) |
| [22854512](https://pubmed.ncbi.nlm.nih.gov/22854512/) | Clinical | Maintenance B12 dosing (1 mg twice yearly effective) |
| [24433284](https://pubmed.ncbi.nlm.nih.gov/24433284/) | Animal model | Beagle CUBN c.786delC recapitulates human phenotype |
| [23613799](https://pubmed.ncbi.nlm.nih.gov/23613799/) | Animal model | Border Collie CUBN c.8392delC frameshift |
| [23746554](https://pubmed.ncbi.nlm.nih.gov/23746554/) | Animal model | Border Collie exon 53 frameshift; C-terminal mutation abrogates receptor |
| [26958680](https://pubmed.ncbi.nlm.nih.gov/26958680/) | Clinical follow-up | Residual neurodevelopmental deficits after delayed diagnosis |
| [37710296](https://pubmed.ncbi.nlm.nih.gov/37710296/) | Review of cases | Complete recovery with treatment; neurocognitive risk if untreated |
| [24156255](https://pubmed.ncbi.nlm.nih.gov/24156255/) | Human / functional | Urinary proteomics; genotype correlates with LMW proteinuria |
| [17668238](https://pubmed.ncbi.nlm.nih.gov/17668238/) | Case report | Compound heterozygous CUBN; funicular myelosis in German patient |
| [16760376](https://pubmed.ncbi.nlm.nih.gov/16760376/) | Review | Renal receptors (megalin/cubam) for B12 and carrier proteins |
| [11375443](https://pubmed.ncbi.nlm.nih.gov/11375443/) | Review | Megalin/cubilin endocytosis of protein-bound vitamins |

**Sources of evidence by type:** Human clinical/genetic (majority), in vitro biophysics (PMID 10887099, 11581259), structural/computational (PMID 20237569), and model organism/veterinary (PMIDs 24433284, 24164695, 23613799, 23746554).

---

## Section-by-Section Synthesis

**1. Disease Information.** IGS-1 = megaloblastic anemia 1 (MGA1). Identifiers: OMIM #261100; MONDO:0100156; ICD-10 D51.1 (vitamin B12 deficiency anemia due to selective B12 malabsorption with proteinuria); MeSH "Anemia, Megaloblastic" / "Malabsorption Syndromes." Synonyms: Imerslund syndrome, Imerslund-Najman-Gräsbeck syndrome, selective vitamin B12 malabsorption with proteinuria, congenital cobalamin malabsorption, MGA1. Information derives from aggregated disease-level resources (OMIM, Orphanet) and published patient case series/cohorts (~300 cases reported worldwide).

**2. Etiology.** Primary cause is genetic: biallelic *CUBN* variants (type 1). No environmental cause; the disorder is monogenic and fully penetrant for the biochemical phenotype. Consanguinity is a major risk factor for homozygous inheritance in Middle Eastern populations. There are no established environmental protective factors; the only "protective"/corrective factor is exogenous parenteral B12, which bypasses the absorptive defect. No gene–environment interaction is required for disease.

**3. Phenotypes.** See F004 table above. Laboratory abnormalities (megaloblastic anemia, macrocytosis, low serum B12, elevated methylmalonic acid and homocysteine, LMW proteinuria) are as central as the clinical signs. Quality-of-life impact is dominated by fatigue/anemia and, if untreated, neurodevelopmental impairment; with treatment, QoL is near-normal.

**4. Genetic/Molecular.** Causal gene *CUBN* (HGNC:2548; NCBI Gene 8029; 10p12.1; 62 exons). Variant classes: missense (e.g., p.Pro1297Leu), frameshift, nonsense, splice-site, and gene deletions—all germline, biallelic, recessive. Functional consequence is **loss of function** (reduced surface expression, impaired IF–Cbl binding, or NMD of truncating alleles). ~37 different *CUBN* mutations reported (as of the cited case reports). Modifier genes: *AMN* and *LRP2/megalin* are functional partners; the possibility of ≥1 additional unidentified locus was raised by haplotype data. No established epigenetic contribution or chromosomal abnormality.

**5. Environmental.** Not applicable as a cause. Dietary B12 intake is irrelevant to pathogenesis because the defect is in receptor-mediated uptake, not intake—oral B12 cannot be absorbed via the normal ileal route.

**6. Mechanism.** See the causal-chain diagram above (F001, F002, F007, F008).

**7. Anatomical structures.** Primary organs: **ileum** (UBERON:0002116) and **kidney/renal proximal tubule** (UBERON:0001232). Body systems: digestive (absorption), urinary (proteinuria), hematopoietic (anemia), and nervous (neurological damage, secondary). Cells: ileal enterocytes (CL:0002254), renal proximal tubule epithelial cells (CL:0002306). Subcellular: apical brush-border plasma membrane, clathrin-coated pits, endosomes. Lateralization: bilateral (kidneys); systemic.

**8. Temporal development.** Onset: infancy/early childhood, typically ~4 months to a few years (not congenital in presentation). Course: chronic, lifelong; progressive if untreated (worsening anemia, neurological deterioration), but stable/remitting with treatment. Critical period: early recognition and treatment prevents irreversible neurodevelopmental injury—the key therapeutic window.

**9. Inheritance and population.** Autosomal recessive (HP:0000007). Prevalence ~1:200,000 (Finland 0.8/100,000). Complete penetrance for biochemical/hematologic phenotype; variable expressivity (proteinuria in ~50%, neurological involvement variable). Founder effects in Finland (CUBN, including FM1 p.P1297L) and Norway (AMN). Consanguinity drives Middle Eastern cases. No anticipation. Sex ratio approximately equal (autosomal). No repeat expansion.

**10. Diagnostics.** Labs: CBC (macrocytic/megaloblastic anemia), low serum B12, elevated methylmalonic acid and homocysteine, bone marrow megaloblastosis, urinalysis showing LMW proteinuria. Absorption test (Schilling-type): low B12 absorption **not corrected by intrinsic factor** (distinguishes from pernicious anemia/IF deficiency). Confirmatory test: molecular genetic testing of *CUBN* (and *AMN* to distinguish type 1 vs 2), by single-gene, panel, or exome sequencing. Differential diagnosis: transcobalamin deficiency (presents at birth, no proteinuria), hereditary intrinsic factor deficiency, pernicious anemia (autoimmune, older patients), other inborn errors of cobalamin metabolism (cblC, etc.), dietary B12 deficiency.

**11. Outcome/Prognosis.** Excellent with lifelong parenteral B12: complete hematologic and metabolic normalization. Delayed diagnosis risks permanent neurodevelopmental deficits (retardation, microcephaly). Proteinuria persists but renal function remains normal—benign. Not associated with reduced life expectancy when treated.

**12. Treatment.** **Parenteral hydroxocobalamin/cyanocobalamin**, lifelong. Loading followed by maintenance (as infrequent as 1 mg IM twice yearly can suffice). No gene, cell, or RNA therapy exists or is needed given the simplicity and efficacy of B12 replacement. NCIT: Hydroxocobalamin (NCIT:C542), Cyanocobalamin (NCIT:C29273).

**13. Prevention.** No primary prevention (genetic). Genetic counseling for affected families; carrier and cascade testing in founder/consanguineous populations. Prenatal/preimplantation diagnosis possible where the familial variant is known. Tertiary prevention (of complications) = adherence to lifelong B12 to prevent anemia and neurological sequelae.

**14. Other species / natural disease.** Naturally occurring IGS is well documented in **dogs** (NCBI Taxon 9615): Beagles (*CUBN* c.786delC), Border Collies (*CUBN* c.8392delC and exon 53 frameshift), and *AMN* mutations in Giant Schnauzers/Australian Shepherds/Border Collies. Canine *CUBN* is orthologous to human *CUBN*. These are of veterinary importance and serve as faithful comparative-pathology models (failure to thrive, dyshematopoiesis, methylmalonic aciduria, hyperammonemia, proteinuria, absent renal cubilin). No zoonotic potential (genetic disease).

**15. Model organisms.** The primary and most faithful models are the **naturally occurring canine models** above (recapitulate hematologic, metabolic, and renal phenotypes with near-complete fidelity). *Amn* knockout mice are embryonic lethal (amnionless is essential for embryonic development), which limits murine modeling of the intestinal/renal phenotype—a notable limitation. Cellular/in vitro models: cubilin-expressing cell lines used for IF–Cbl uptake and binding assays (basis of the FM1 functional characterization). Resources: OMIA (canine IGS entries), MGI (mouse *Cubn*/*Amn*).

---

## Limitations and Knowledge Gaps

1. **Incomplete genetic accounting.** Not all IGS cases map to *CUBN* or *AMN*; haplotype data historically suggested a possible additional locus. The full mutational spectrum and genotype–phenotype correlations (especially for proteinuria presence/absence) remain incompletely defined.
2. **Mechanism of neurological injury is inferred.** The link from systemic B12 deficiency to CNS damage in IGS is extrapolated from general cobalamin biochemistry rather than demonstrated in IGS-specific tissue; the determinants of reversibility vs permanence are not precisely mapped.
3. **No mouse model of the classic disease.** *Amn* knockout embryonic lethality precludes a standard murine IGS model, leaving canines and cell lines as the main experimental systems.
4. **Renal arm long-term outcomes.** Whether lifelong LMW proteinuria has any subtle long-term renal or systemic consequences (e.g., vitamin D/lipid carrier loss) is not fully characterized.
5. **Rarity limits epidemiology.** Prevalence estimates rely largely on Scandinavian data; global under-diagnosis is likely, and exact incidence/prevalence in non-founder populations is uncertain.
6. **This report was literature-only.** No primary dataset was analyzed; conclusions rest on published cohorts, case reports, and structural/functional studies.

---

## Proposed Follow-up Experiments / Actions

1. **Systematic *CUBN* variant–phenotype map.** Aggregate ClinVar/HGMD/published variants and correlate variant location (IF–Cbl-binding CUB5–8 vs C-terminal vs N-terminal) with presence of B12 malabsorption vs isolated proteinuria to formalize the genotype–phenotype rule suggested by PMID 31613795 and PMID 24156255.
2. **Structure-guided functional assays** for variants of uncertain significance: express candidate CUBN missense variants in cubilin/AMN cell systems and measure surface expression and IF–Cbl binding kinetics (SPR), extending the FM1 approach (PMID 10887099) to classify VUS per ACMG.
3. **Conditional (tissue-specific) *Cubn/Amn* mouse models** (intestine- and kidney-specific knockouts) to bypass embryonic lethality and dissect the intestinal vs renal arms independently.
4. **Longitudinal renal-function cohort study** in treated IGS patients to determine whether persistent LMW proteinuria carries any long-term risk and whether it warrants monitoring.
5. **Newborn/carrier screening pilot** in high-prevalence founder populations (Finland, Norway) and consanguineous communities, using targeted *CUBN*/*AMN* panels, to reduce diagnostic delay and prevent neurodevelopmental sequelae.
6. **Optimize maintenance dosing** with prospective trials confirming the minimum effective parenteral B12 schedule (building on PMID 22854512) and evaluating whether high-dose oral B12 has any role given residual passive absorption.

---

*Report compiled from an autonomous multi-iteration literature investigation (8 confirmed findings, 31 papers reviewed). All mechanistic and clinical claims are cited to primary literature by PMID; direct abstract quotes are provided for key statements.*


## Artifacts

- [OpenScientist final report](Imerslund-Grasbeck_Syndrome_Type_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Imerslund-Grasbeck_Syndrome_Type_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 19 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0002254` (3 mentions) - the report calls it "enterocyte of epithelium of small intestine", "Ileal enterocyte / absorptive brush-border cell"; CL calls it **epithelial cell of small intestine**
- `HP:0012325` (1 mention) - the report calls it "Methylmalonic aciduria"; HP calls it **Chronic myelomonocytic leukemia**
- `NCIT:C542` (2 mentions) - the report calls it "Hydroxocobalamin"; NCIT calls it **Heterocyclic Compound**
- `NCIT:C29273` (2 mentions) - the report calls it "Cyanocobalamin/Vitamin B12"; NCIT calls it **Aluminum Hydroxide/Magnesium Hydroxide**
- `GO:0006810` (1 mention) - the report calls it "Protein reabsorption / transcytosis"; GO calls it **transport**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C29273` (Aluminum Hydroxide/Magnesium Hydroxide) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000007` (2 mentions) - the report calls it "autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names
- `UBERON:0001232` (3 mentions) - the report calls it "renal proximal tubule", "kidney/renal proximal tubule"; UBERON calls it **collecting duct of renal tubule**, and lists "kidney collecting tubule" among its other names
- `CL:0002306` (3 mentions) - the report calls it "epithelial cell of proximal tubule", "Proximal tubule epithelial cell"; CL calls it **epithelial cell of proximal tubule**, and lists "kidney proximal tubule epithelial cell" among its other names
- `HP:0000093` (1 mention) - the report calls it "Proteinuria (LMW)"; HP calls it **Proteinuria**
- `HP:0002160` (1 mention) - the report calls it "Hyperhomocysteinemia"; HP calls it **Hyperhomocystinemia**
- `CHEBI:17439` (1 mention) - the report calls it "cyanocobalamin"; CHEBI calls it **cyanocob(III)alamin**, and lists "cyanocobalamin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0006898` - called "receptor-mediated endocytosis", "Receptor-mediated endocytosis"
- `UBERON:0001232` - called "renal proximal tubule", "kidney/renal proximal tubule"
- `CL:0002306` - called "epithelial cell of proximal tubule", "Proximal tubule epithelial cell"
- `CL:0002254` - called "enterocyte of epithelium of small intestine", "Ileal enterocyte / absorptive brush-border cell"