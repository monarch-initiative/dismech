---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T09:02:32.712183'
end_time: '2026-09-03T09:23:13.953610'
duration_seconds: 1241.24
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Cardiomyopathy Dilated 2H
  mondo_id: MONDO:0859358
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
citation_count: 13
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 8
  relevance_assessed: 14
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 2
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0859358
    reported_labels:
    - if available
    - cardiomyopathy, dilated, 2H
    ontology_label: cardiomyopathy, dilated, 2H
  - term_id: HP:0001644
    reported_labels:
    - Severe, rapidly progressive
    ontology_label: Dilated cardiomyopathy
  - term_id: HP:0001635
    reported_labels:
    - congestive heart failure
    - Severe, fatal
    ontology_label: Congestive heart failure
  - term_id: HP:0001522
    reported_labels:
    - Fatal
    ontology_label: Death in infancy
  - term_id: GO:0005829
    reported_labels:
    - 'GO cellular component: cytosol'
    ontology_label: cytosol
  labels_variant: 3
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cardiomyopathy_Dilated_2H-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cardiomyopathy_Dilated_2H-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiomyopathy Dilated 2H
- **MONDO ID:** MONDO:0859358 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cardiomyopathy Dilated 2H** covering all of the
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

# Cardiomyopathy Dilated 2H (CMD2H) — Comprehensive Disease Report

**Disease:** Cardiomyopathy, Dilated, 2H (CMD2H)
**MONDO ID:** MONDO:0859358
**OMIM (phenotype):** 620203
**Causal gene:** GET3 / ASNA1 (TRC40), 19p13.13
**Category:** Mendelian (autosomal recessive)

---

## Summary

**Cardiomyopathy Dilated 2H (CMD2H; MONDO:0859358, OMIM 620203) is an ultra-rare, autosomal recessive, infantile-onset, rapidly progressive dilated cardiomyopathy caused by biallelic loss-of-function variants in GET3/ASNA1 (TRC40; NCBI Gene 439; 19p13.13).** GET3/ASNA1 encodes the cytosolic ATPase that recognizes the transmembrane domain of tail-anchored (TA) membrane proteins and delivers them to the endoplasmic reticulum (ER) for post-translational insertion via the GET/TRC pathway. Reduced GET3 function impairs TA-protein insertion and cardiomyocyte proteostasis, producing ventricular dilation, heart failure, and death in early infancy.

**A critical disambiguation underpins this report.** The disease name "Cardiomyopathy Dilated 2H" and MONDO:0859358 map to OMIM 620203 and are caused by **GET3/ASNA1**, not by GATAD1. GATAD1 causes a *different* recessive dilated cardiomyopathy, **CMD2B** (OMIM 614672). Early iterations of this investigation initially followed the GATAD1 literature; identifier cross-referencing through Monarch/OLS4 established that MONDO:0859358 → OMIM:620203 → GET3/ASNA1, and the report was corrected accordingly. GATAD1/CMD2B findings are retained below only as an explicitly labeled contrast, to prevent future confusion, and should **not** be attributed to CMD2H.

The molecular and clinical picture of CMD2H is supported by a coherent evidence chain: the index human family (compound heterozygous ASNA1 variants p.Gln305* and p.Val163Ala in two siblings with fatal infantile DCM; Verhagen et al. 2019), an in vitro TA-protein insertion assay demonstrating reduced function of the missense allele, zebrafish rescue experiments confirming both variants are deleterious, and cardiomyocyte-specific *Asna1*-knockout mice (Feng et al. 2025) that recapitulate ventricular dilation, myocardial thinning, and disrupted TA-protein proteostasis. There is currently no disease-specific or targeted therapy; management follows standard guideline-directed heart-failure care, with transplantation as the definitive option.

---

## Section 1 — Disease Information

**Overview.** CMD2H is a Mendelian, autosomal recessive form of dilated cardiomyopathy (DCM) — a cardiac muscle disorder defined by left-ventricular (or biventricular) dilation and systolic dysfunction in the absence of abnormal loading conditions or coronary disease sufficient to explain it. CMD2H is distinguished from common idiopathic DCM by its monogenic recessive etiology (biallelic GET3/ASNA1 variants), its very early (infantile) onset, and its rapid, frequently fatal course.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0859358 ("cardiomyopathy, dilated, 2H") |
| OMIM (phenotype) | 620203 |
| OMIM (gene, GET3/ASNA1) | 601913 |
| MedGen | C5774296 |
| UMLS | C5774296 |
| GARD | 0026714 |
| NCBI Gene | 439 (GET3; aliases ASNA1, TRC40, ASNA-I, ARSA1, CMD2H) |
| Ensembl (gene) | ENSG00000198356 |
| HGNC symbol | GET3 (previously ASNA1) |

Cross-references were verified via Monarch and OLS4. Note that "CMD2H" is itself listed among the official gene aliases for GET3 in NCBI Gene.

**Synonyms / alternative names.** Dilated cardiomyopathy 2H; DCM 2H; CMD2H; (gene-based) ASNA1-related / GET3-related dilated cardiomyopathy; ASNA1-related infantile dilated cardiomyopathy.

**Information source.** Disease-level, aggregated Mendelian resources (OMIM, MONDO, MedGen) combined with a small number of primary case reports and functional studies. The clinical description derives from a single index family (two siblings) plus supporting model-organism and in vitro data — it is *not* derived from large EHR cohorts, reflecting the ultra-rare nature of the disorder.

---

## Section 2 — Etiology

**Primary cause: genetic.** CMD2H is caused by **biallelic (compound heterozygous or homozygous) loss-of-function variants in GET3/ASNA1**. It is a monogenic, autosomal recessive disorder with no established environmental or infectious primary cause.

> "We identified compound heterozygous variants in the highly conserved ASNA1 gene (arsA arsenite transporter, ATP-binding, homolog), which encodes an ATPase required for post-translational membrane insertion of tail-anchored proteins." — Verhagen et al. 2019, [PMID: 31461301](https://pubmed.ncbi.nlm.nih.gov/31461301/)

> "Biallelic variants in ASNA1 cause severe pediatric cardiomyopathy and early death." — Verhagen et al. 2019, [PMID: 31461301](https://pubmed.ncbi.nlm.nih.gov/31461301/)

**Genetic risk factors.** The causal risk factor is inheritance of two damaging GET3/ASNA1 alleles. Consistent with a recessive mechanism, gnomAD shows GET3/ASNA1 is constrained but tolerant of *heterozygous* loss of function (pLI = 0.05; LoF observed/expected = 15/32.4; oe_lof = 0.46, 90% CI 0.31–0.71; lof_z = 2.59; mis_z = 2.51). This constraint profile — tolerant of one null allele but depleted overall — is exactly what is expected for a gene in which heterozygous carriers are healthy and disease requires biallelic hits.

**Environmental risk / protective factors / gene–environment interactions.** No environmental risk factors, protective factors, or gene–environment interactions specific to CMD2H have been reported. Given the severe, near-fully-penetrant recessive genotype, environmental modifiers are unlikely to be dominant contributors, though data are too sparse to exclude modifiers of severity. (For DCM broadly, "second-hit" models — inflammation, clonal hematopoiesis, environmental triggers layered on genetic susceptibility — are increasingly recognized [PMID: 41898170], but these apply to common/idiopathic DCM, not specifically CMD2H.)

---

## Section 3 — Phenotypes

The CMD2H phenotype, as documented in the index sibling pair, is a **severe, rapidly progressive, infantile-onset dilated cardiomyopathy**:

| Phenotype | Type | Onset | Severity / course | HPO suggestion |
|---|---|---|---|---|
| Dilated cardiomyopathy | Clinical sign (imaging) | Infantile / early | Severe, rapidly progressive | HP:0001644 |
| Ventricular systolic dysfunction | Clinical sign | Infantile | Severe | HP:0001635 (congestive heart failure) |
| Ventricular dilation | Structural | Infantile | Severe | HP:0001711 (abnormal LV morphology) |
| Heart failure | Clinical syndrome | Infantile | Severe, fatal | HP:0001635 |
| Death in infancy | Outcome | Early infancy | Fatal | HP:0001522 |

**Phenotype characteristics.** Age of onset: neonatal/infantile. Severity: severe. Progression: rapidly progressive. Frequency among affected individuals: in the reported family, both biallelic siblings were affected and died in early infancy (high penetrance for the severe biallelic genotype), though the total number of reported patients is very small (n ≈ 2 index cases), limiting frequency estimates.

**Quality-of-life impact.** Not formally measured with instruments (EQ-5D, SF-36, PROMIS) given infantile lethality. The practical impact is maximal — the disease is life-limiting in infancy in reported cases.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** GET3 / ASNA1 (TRC40). NCBI Gene 439; 19p13.13; Ensembl ENSG00000198356; OMIM gene 601913.

**Pathogenic variants (index family).** Verhagen et al. 2019 identified **compound heterozygous** ASNA1/GET3 variants in two affected siblings:

| Variant (cDNA) | Protein | Parental origin | Class | Functional consequence |
|---|---|---|---|---|
| c.913C>T | p.(Gln305*) | Paternal | Nonsense / premature termination codon | Decreased protein in myocardium and skin fibroblasts (null / LoF) |
| c.488T>C | p.(Val163Ala) | Maternal | Missense | Protein misfolding; less effective tail-anchored protein insertion (hypomorphic LoF) |

> "Exome sequencing was used to screen for the causative genetic defect in a pair of siblings with rapidly progressive dilated cardiomyopathy and death in early infancy." — [PMID: 31461301](https://pubmed.ncbi.nlm.nih.gov/31461301/)

**Variant classification.** Both variants segregate with disease in a recessive pattern and are supported by functional evidence (reduced protein/insertion activity; failure to rescue zebrafish). They are consistent with pathogenic/likely-pathogenic classification under ACMG/AMP criteria (functional evidence PS3; recessive segregation; predicted null variant PVS1 for p.Gln305*).

**Variant type/class.** One nonsense/PTC allele (loss of protein) and one missense/misfolding allele. **Origin:** germline, biallelic (autosomal recessive). **Population frequency:** rare, consistent with an ultra-rare Mendelian disorder. **Functional consequence:** loss of function for both alleles (one null, one hypomorphic).

**Modifier genes / epigenetics / chromosomal abnormalities.** No CMD2H-specific modifier genes, epigenetic marks, or chromosomal abnormalities have been reported. This is a single-gene, small-variant disorder; no aneuploidy/translocation involvement is described.

---

## Section 5 — Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in CMD2H. It is a purely genetic (Mendelian recessive) disorder. This contrasts with acquired/inflammatory DCM (e.g., viral myocarditis progressing to DCM [PMID: 42415986]; inflammatory cardiomyopathy [PMID: 41747776]), which is mechanistically distinct and not part of the CMD2H entity.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in GET3/ASNA1** (e.g., p.Gln305* null + p.Val163Ala misfolding) **result in** reduced GET3/ASNA1 protein level and/or ATPase/chaperone activity in cardiomyocytes.
2. Reduced GET3 activity **leads to** destabilization of the cytosolic pre-targeting complex and impaired recognition/delivery of tail-anchored (TA) membrane proteins to the ER membrane (GET/TRC pathway failure). *(Demonstrated in vitro via a TA-insertion assay for p.Val163Ala.)*
3. Failed TA-protein insertion **results in** reduced expression/mistargeting of multiple TA-protein substrates (SNAREs, ER/Golgi trafficking components, apoptosis regulators), **impairing** membrane trafficking and organelle proteostasis. *(Demonstrated in Asna1-KO mouse cardiomyocytes.)*
4. Disrupted cardiomyocyte proteostasis and membrane-protein homeostasis **lead to** a maladaptive compensatory transcriptional response (upregulation of protein-trafficking and Golgi-to-ER transport genes) and **impaired cardiomyocyte function/contractility**. *(Transcriptomics + zebrafish contractility data.)*
5. Cardiomyocyte dysfunction **results in** ventricular myocardial thinning (developmental) and/or ventricular dilation with reduced systolic function (postnatal/adult).
6. Progressive ventricular dilation and pump failure **lead to** heart failure and, in reported human cases, **death in early infancy**.

Steps 1–3 are directly demonstrated (human protein data, in vitro insertion assay, mouse molecular data). Steps 4–6 are supported by convergent zebrafish (contractility, lethality) and mouse (dilation, thinning, mortality) evidence; the precise identity of the critical cardiac TA-protein substrate(s) whose loss is rate-limiting for the heart phenotype remains **inferred rather than fully demonstrated**.

### Detail by category

**Molecular pathway — the GET/TRC (guided-entry of tail-anchored proteins) pathway.** GET3/ASNA1 (yeast Get3; mammalian TRC40) is the central cytosolic ATPase that binds the C-terminal transmembrane domain of TA proteins and delivers them to an ER membrane receptor formed by **WRB (=GET1)** and **CAML/CAMLG (=GET2)** ([PMID: 21444755](https://pubmed.ncbi.nlm.nih.gov/21444755/), [PMID: 27226539](https://pubmed.ncbi.nlm.nih.gov/27226539/)). This is a post-translational, ATP-dependent targeting cycle.

**Cellular processes.** Membrane-protein biogenesis, ER-targeted protein trafficking, proteostasis, and (indirectly) apoptosis regulation (many apoptotic/BCL-2-family and SNARE proteins are TA proteins). ASNA1's ATPase activity is required for cell survival and ER homeostasis in other tissues (pancreatic progenitors [PMID: 29180572]; β-cell ER homeostasis [PMID: 26438609]), underscoring the pathway's general importance to proteostasis.

**Protein dysfunction.** p.Gln305* → truncation/loss of protein (reduced abundance in patient myocardium and fibroblasts). p.Val163Ala → misfolding and reduced TA-insertion efficiency (hypomorph). Net effect: loss of function.

> "Protein expression was assessed in patient samples, followed by an in vitro tail-anchored protein insertion assay and functional analyses in zebrafish." — [PMID: 31461301](https://pubmed.ncbi.nlm.nih.gov/31461301/)

**Downstream molecular profiling (mouse).** In cardiomyocyte-specific *Asna1*-KO mice, ASNA1 deficiency destabilized the pre-targeting complex and reduced expression of multiple TA-protein substrates, impairing membrane trafficking. Transcriptomics revealed compensatory (maladaptive) upregulation of protein-trafficking and Golgi-to-ER transport genes.

> "ASNA1 deficiency destabilized the pre-targeting complex and reduced the expression of multiple TA protein substrates, impairing membrane trafficking and protein transport." — Feng et al. 2025, [PMID: 41370295](https://pubmed.ncbi.nlm.nih.gov/41370295/)

**Tissue-damage mechanisms.** Impaired proteostasis → cardiomyocyte dysfunction → myocardial thinning (embryonic) or dilation and pathological remodeling (postnatal). Fibrosis/oxidative stress are downstream remodeling features common to DCM but not specifically characterized in CMD2H.

**Upstream vs downstream.** Upstream: GET3/ASNA1 LoF → GET/TRC pathway failure. Downstream: TA-substrate depletion → cardiomyocyte proteostatic stress → contractile dysfunction → ventricular dilation → heart failure.

**Suggested ontology terms.**
- GO biological process: tail-anchored membrane protein insertion into ER membrane (GO:0071816); post-translational protein targeting to endoplasmic reticulum membrane (GO:0006620); protein insertion into ER membrane (GO:0045048).
- GO cellular component: cytosol (GO:0005829); endoplasmic reticulum membrane (GO:0005789); TRC/GET complex.
- CL cell type: cardiac muscle cell / cardiomyocyte (CL:0000746); regular ventricular cardiac myocyte (CL:2000046).

---

## Section 7 — Anatomical Structures Affected

**Organ level.** Primary organ: **heart** (UBERON:0000948), specifically the **ventricular myocardium** — left ventricle (UBERON:0002084) and, in mouse, biventricular. Body system: **cardiovascular system** (UBERON:0004535). Secondary involvement: systemic congestion / heart-failure sequelae (pulmonary, hepatic, renal hypoperfusion) as in any severe infantile DCM.

**Tissue and cell level.** Tissue: **cardiac muscle tissue / myocardium** (UBERON:0002349). Target cell: **cardiomyocyte** (CL:0000746; ventricular cardiac myocyte CL:2000046). GET3/ASNA1 is broadly expressed, but the disease phenotype is myocardium-predominant.

**Subcellular level.** Compartments: **cytosol** (GO:0005829, site of GET3 targeting complex) and **ER membrane** (GO:0005789, destination of TA-protein insertion). Membrane trafficking machinery (Golgi-to-ER transport) is transcriptionally perturbed.

**Localization / lateralization.** Cardiac, bilateral/biventricular (mouse); left-ventricular predominant description in human DCM. No focal or asymmetric lateralization is characteristic.

---

## Section 8 — Temporal Development

**Onset.** Congenital/infantile. In the index human family, disease was evident and rapidly progressive in early infancy. In constitutive *Asna1*-KO mice, myocardial thinning appears by embryonic day 16.5 with perinatal lethality, indicating a developmental component.

**Progression.** Rapid. Human course: rapidly progressive DCM with death in early infancy. Inducible adult-cardiomyocyte *Asna1* deletion in mice caused rapid ventricular dilation, impaired function, remodeling, and early mortality — indicating that GET3/ASNA1 is required for both cardiac development and ongoing adult cardiomyocyte maintenance.

> "Constitutive Asna1 deletion during embryogenesis caused perinatal lethality with marked ventricular myocardial thinning by embryonic day 16.5, whereas inducible deletion in adult cardiomyocytes led to rapid ventricular dilation, impaired cardiac function, pathological remodeling, and early mortality." — Feng et al. 2025, [PMID: 41370295](https://pubmed.ncbi.nlm.nih.gov/41370295/)

**Course pattern.** Progressive, non-remitting, fatal in reported cases. No spontaneous remission described. **Critical period:** perinatal/infancy is the window of vulnerability; there is no established intervention window beyond supportive heart-failure care and transplantation.

---

## Section 9 — Inheritance and Population

**Inheritance.** Autosomal recessive (biallelic GET3/ASNA1 LoF). Heterozygous carriers are unaffected — consistent with gnomAD constraint showing tolerance of a single LoF allele.

**Penetrance / expressivity.** In the single reported family both biallelic siblings were severely affected (apparently high penetrance for the severe biallelic genotype), but the extremely small case count precludes robust penetrance/expressivity estimates.

**Epidemiology.** Ultra-rare. Only a single index family (two siblings) is definitively reported for CMD2H, plus supporting functional data; prevalence/incidence are not established. For context, idiopathic DCM overall has an approximate historical prevalence near 1:2500 and is "the most common cardiomyopathy worldwide" ([PMID: 42511685](https://pubmed.ncbi.nlm.nih.gov/42511685/)), but CMD2H represents a vanishingly small monogenic subset.

**Carrier frequency / founder effects / consanguinity.** Not established; no founder effect reported. **Sex ratio:** no sex bias expected for an autosomal recessive gene; not established given tiny sample. **Geographic distribution:** not established.

**gnomAD constraint (ENSG00000198356; chr19:12,737,139–12,748,323, GRCh38):** pLI = 0.05; LoF o/e = 15/32.4 (oe_lof = 0.46, 90% CI 0.31–0.71); lof_z = 2.59; mis_z = 2.51 — supports a recessive, loss-of-function model with healthy heterozygous carriers.

---

## Section 10 — Diagnostics

**Genetic testing is the definitive diagnostic modality.** Because CMD2H is clinically indistinguishable from other infantile DCM on imaging alone, molecular diagnosis rests on identifying biallelic GET3/ASNA1 variants.

- **Recommended approach:** trio exome sequencing (WES) or genome sequencing (WGS), or a comprehensive cardiomyopathy gene panel that includes ASNA1/GET3, with segregation testing of parents to confirm compound heterozygosity/biallelic status. Exome sequencing was the method that discovered the disease gene.
- **Single-gene testing:** targeted ASNA1/GET3 sequencing (with deletion/duplication analysis) is appropriate once the diagnosis is suspected or in cascade testing.
- **Variant interpretation:** classify per ACMG/AMP using ClinVar/ClinGen, incorporating functional evidence (reduced protein, impaired TA-insertion) and recessive segregation.

**Clinical/imaging tests (phenotype confirmation, non-specific).** Echocardiography and cardiac MRI to document ventricular dilation and reduced ejection fraction; ECG; natriuretic peptides (BNP/NT-proBNP) and troponin as heart-failure biomarkers. Endomyocardial biopsy could show reduced GET3 protein (as in the index case) but is not routinely required.

**Differential diagnosis.** Other genetic infantile/pediatric DCMs (e.g., TTN, LMNA, sarcomeric and metabolic cardiomyopathies), CTNNA3-related recessive DCM [PMID: 42471840], GATAD1-related CMD2B (see disambiguation), mitochondrial/metabolic cardiomyopathies, and acquired causes (viral myocarditis, inflammatory cardiomyopathy). Genetic testing distinguishes CMD2H.

**Screening.** Cascade genetic testing of at-risk relatives and carrier testing of parents for reproductive counseling. No population newborn screening exists for this ultra-rare disorder.

---

## Section 11 — Outcome / Prognosis

**Prognosis is poor in reported cases** — rapidly progressive DCM with death in early infancy in the two index siblings. Mouse models mirror this severity (perinatal lethality with constitutive KO; early mortality with adult inducible KO).

**Survival / mortality.** Reported human outcome: fatal in infancy. Definitive survival statistics are not available due to the tiny case count.

**Morbidity / complications.** Severe heart failure, arrhythmia risk, and the sequelae of low cardiac output. For DCM broadly, non-ischaemic DCM confers ~12-fold higher out-of-hospital cardiac arrest incidence versus the general population (532 vs 45 per 100,000 person-years) with higher shockable-rhythm rates [PMID: 42536775] — underscoring arrhythmic risk that informs management of any DCM, though CMD2H's infantile lethality dominates its natural history.

> "The incident rate of OHCA was approximately 12 times higher in NIDCM patients compared with the general population (incidence rate 532 vs 45 per 100 000 person years)." — [PMID: 42536775](https://pubmed.ncbi.nlm.nih.gov/42536775/)

**Prognostic factors.** Biallelic null genotype and infantile onset predict severe outcome. No CMD2H-specific prognostic biomarkers are established.

---

## Section 12 — Treatment

**There is no disease-specific or targeted therapy for CMD2H.** Management follows **standard guideline-directed heart-failure therapy** for pediatric/infantile DCM, with **heart transplantation** as the definitive option for end-stage disease.

**Pharmacotherapy (supportive, standard HF care; NCIT terms in brackets).**
- Diuretics for congestion (e.g., furosemide) [Loop Diuretic].
- ACE inhibitors / ARBs / ARNI for afterload reduction and remodeling [Angiotensin-Converting Enzyme Inhibitor, NCIT:C776].
- Beta-blockers where tolerated [Beta-Adrenergic Blocker, NCIT:C2568].
- Mineralocorticoid receptor antagonists.
- SGLT2 inhibitors are now standard in adult HFrEF; pediatric applicability is individualized.
- Inotropic support for acute decompensation.

**Device / advanced therapies.** ICD for arrhythmic protection in appropriate patients; mechanical circulatory support (VAD) as a bridge; **cardiac transplantation** [Heart Transplantation, NCIT:C15326] for refractory disease.

**Advanced / experimental therapeutics.** No approved gene therapy, RNA therapy, or targeted small molecule exists for GET3/ASNA1-related DCM. Because the mechanism is recessive loss of function, **gene-replacement / gene-addition strategies (e.g., AAV-delivered ASNA1)** are conceptually rational future directions but are entirely preclinical/hypothetical at present.

**Pharmacogenomics.** None specific to CMD2H.

---

## Section 13 — Prevention

**Primary prevention** of the disease itself is genetic: **carrier identification and reproductive counseling**. Options for at-risk couples (both carriers) include prenatal diagnosis and **preimplantation genetic testing (PGT-M)**.

- **Genetic counseling** for families with an affected child: 25% recurrence risk per pregnancy for two carrier parents (autosomal recessive).
- **Cascade carrier testing** of relatives.
- **Secondary/tertiary prevention** for an affected infant is limited to early heart-failure management, arrhythmia surveillance/ICD where appropriate, and timely transplant evaluation.

No immunization, behavioral, or public-health prevention applies to this monogenic disorder.

---

## Section 14 — Other Species / Natural Disease

**Evolutionary conservation.** GET3/ASNA1 is a highly conserved ATPase. Functional orthologs span yeast (**GET3**), *C. elegans* (**asna-1**), zebrafish (**asna1**), and mouse (**Asna1**), all participating in TA-protein insertion. This deep conservation supports the mechanistic model and enables cross-species modeling.

> "Our findings point toward a critical role of the tail-anchored membrane protein insertion pathway in vertebrate cardiac function and disease." — Verhagen et al. 2019, [PMID: 31461301](https://pubmed.ncbi.nlm.nih.gov/31461301/)

**Orthologous genes (suggested identifiers to populate):** mouse *Asna1*, zebrafish *asna1*, *C. elegans* asna-1, *S. cerevisiae* GET3. **Natural disease in companion animals/wildlife:** no OMIA entry for spontaneous ASNA1/GET3 cardiomyopathy is established; the animal data are experimental models rather than naturally occurring disease. **Zoonotic potential:** not applicable (genetic disorder).

---

## Section 15 — Model Organisms

**Zebrafish (*Danio rerio*, asna1).** Loss of asna1 produced reduced cardiac contractility and early lethality; wild-type asna1 mRNA rescued the phenotype, whereas mRNA carrying either patient variant (p.Gln305* or p.Val163Ala) failed to rescue — establishing both human alleles as functionally deleterious and validating the gene–disease relationship in vivo.

**Mouse (*Mus musculus*, Asna1) — cardiomyocyte-specific conditional knockouts (Feng et al. 2025, [PMID: 41370295](https://pubmed.ncbi.nlm.nih.gov/41370295/)).**
- *Constitutive* cardiomyocyte deletion → perinatal lethality with ventricular myocardial thinning by E16.5.
- *Inducible* adult deletion → rapid ventricular dilation, impaired cardiac function, pathological remodeling, and early mortality.
- Molecular: destabilized pre-targeting complex, reduced TA-substrate expression, impaired membrane trafficking; compensatory transcriptional upregulation of trafficking genes.

**Phenotype recapitulation.** Excellent — mouse models reproduce the core human features (ventricular dilation, impaired function, early death) and provide the mechanistic link to TA-protein proteostasis. Zebrafish provide orthogonal in vivo validation and a variant-specific rescue assay.

**Model limitations.** Species differences in cardiac physiology; conditional models are engineered LoF rather than the exact human compound-heterozygous genotype; human natural-history and therapeutic-response data remain minimal.

**Suggested resources:** MGI (Asna1), ZFIN (asna1), IMPC/IMSR for mouse alleles.

---

## Key Findings (with evidence)

### Finding 1 — CMD2H is caused by biallelic GET3/ASNA1, not GATAD1 (critical disambiguation)
MONDO:0859358 "cardiomyopathy, dilated, 2H" cross-references OMIM:620203, MedGen/UMLS C5774296, and GARD 0026714 (verified via Monarch/OLS4). The causal gene is **GET3/ASNA1** (NCBI Gene 439, 19p13.13), whose official aliases include ASNA1, TRC40, ARSA1, and **CMD2H**. Verhagen et al. 2019 identified compound heterozygous ASNA1 variants in two siblings with fatal infantile DCM. **GATAD1 causes a distinct disease, CMD2B (OMIM 614672)** — the initial GATAD1 leads in this investigation belong to CMD2B and do not apply to CMD2H.

> "Biallelic variants in ASNA1 cause severe pediatric cardiomyopathy and early death." — [PMID: 31461301](https://pubmed.ncbi.nlm.nih.gov/31461301/)

### Finding 2 — Pathogenic variant spectrum: a truncating null plus a misfolding missense, both LoF
Paternal c.913C>T, p.(Gln305*) (null; reduced protein in myocardium/fibroblasts) + maternal c.488T>C, p.(Val163Ala) (misfolding; impaired TA insertion). Both are loss-of-function; zebrafish rescue failed for both. Germline, biallelic, autosomal recessive.

> "Exome sequencing was used to screen for the causative genetic defect in a pair of siblings with rapidly progressive dilated cardiomyopathy and death in early infancy." — [PMID: 31461301](https://pubmed.ncbi.nlm.nih.gov/31461301/)

### Finding 3 — Mechanism: defective GET/TRC tail-anchored-protein insertion impairs cardiomyocyte function
GET3/ASNA1 (TRC40) is the cytosolic ATPase delivering TA proteins to the ER via the WRB(GET1)/CAML(GET2) receptor. Biallelic LoF reduces TA-insertion capacity (in vitro assay), reducing cardiac contractility (zebrafish) and causing dilation/failure.

> "Protein expression was assessed in patient samples, followed by an in vitro tail-anchored protein insertion assay and functional analyses in zebrafish." — [PMID: 31461301](https://pubmed.ncbi.nlm.nih.gov/31461301/)

### Finding 4 — Mouse cardiomyocyte-specific Asna1 KO recapitulates CMD2H
Constitutive KO → perinatal lethality + myocardial thinning by E16.5; inducible adult KO → ventricular dilation, impaired function, remodeling, early death; molecular destabilization of the pre-targeting complex with reduced TA-substrate expression.

> "ASNA1 deficiency destabilized the pre-targeting complex and reduced the expression of multiple TA protein substrates, impairing membrane trafficking and protein transport." — [PMID: 41370295](https://pubmed.ncbi.nlm.nih.gov/41370295/)

### Finding 5 — gnomAD constraint supports a recessive LoF model
pLI = 0.05; oe_lof = 0.46 (90% CI 0.31–0.71); lof_z = 2.59; mis_z = 2.51 — constrained but heterozygous-LoF-tolerant, consistent with unaffected carriers and biallelic disease.

---

## Mechanistic Model / Interpretation

```
 Biallelic GET3/ASNA1 LoF          [p.Gln305* (null) + p.Val163Ala (misfolding)]
            |
            v
 Reduced GET3/ASNA1 protein & ATPase activity in cardiomyocytes
            |
            v
 Destabilized cytosolic pre-targeting (TRC/GET) complex
            |
            v
 Impaired delivery of tail-anchored (TA) proteins to ER
 (via WRB=GET1 / CAML=GET2 receptor)  -- in vitro TA-insertion assay down
            |
            v
 Reduced expression / mistargeting of multiple TA-protein substrates
 (SNAREs, trafficking & apoptosis regulators) -> impaired membrane trafficking
            |
            v
 Cardiomyocyte proteostatic stress + maladaptive compensatory transcription
            |
      +-----+---------------------------+
      v                                 v
 (embryonic) myocardial          (postnatal/adult) ventricular
 thinning by E16.5               dilation + systolic dysfunction
      |                                 |
      +----------------+----------------+
                       v
        Heart failure -> death in early infancy
```

Upstream driver: GET/TRC pathway failure. Downstream effectors: TA-substrate depletion → cardiomyocyte dysfunction → dilation → pump failure. The identity of the single most rate-limiting cardiac TA substrate remains inferred.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Support / Challenge |
|---|---|---|---|
| [31461301](https://pubmed.ncbi.nlm.nih.gov/31461301/) | *Biallelic Variants in ASNA1...* (Verhagen 2019) | Index human family; gene discovery; in vitro + zebrafish | **Core support** — establishes GET3/ASNA1 causation, variants, mechanism |
| [41370295](https://pubmed.ncbi.nlm.nih.gov/41370295/) | Cardiomyocyte-specific Asna1 KO mice (Feng 2025) | Mouse model | **Core support** — recapitulates dilation/thinning; molecular mechanism |
| Monarch / OLS4 | MONDO:0859358 ↔ OMIM:620203 ↔ GET3/ASNA1 | Identifier verification | **Core support** — disease/gene mapping; disambiguation from CMD2B |
| gnomAD (ENSG00000198356) | Constraint metrics | Population genetics | **Support** — recessive LoF model |
| [21444755](https://pubmed.ncbi.nlm.nih.gov/21444755/), [27226539](https://pubmed.ncbi.nlm.nih.gov/27226539/) | WRB/CAML TA-insertion receptor | Pathway biology | **Support** — GET/TRC receptor machinery |
| [29180572](https://pubmed.ncbi.nlm.nih.gov/29180572/), [26438609](https://pubmed.ncbi.nlm.nih.gov/26438609/) | ASNA1 in pancreas / β-cell ER homeostasis | Pathway importance | **Support** — ASNA1 ATPase essential for survival/proteostasis |
| [42536775](https://pubmed.ncbi.nlm.nih.gov/42536775/) | OHCA risk in non-ischaemic DCM | Clinical context | Context — DCM arrhythmic risk (broad) |
| [42511685](https://pubmed.ncbi.nlm.nih.gov/42511685/) | Geographical/ethnic heterogeneity in genetic DCM | Epidemiology context | Context — DCM epidemiology framing |
| [41898170](https://pubmed.ncbi.nlm.nih.gov/41898170/) | Emerging mechanisms/therapies in DCM | Therapy context | Context — general DCM management |
| [21965549](https://pubmed.ncbi.nlm.nih.gov/21965549/) | GATAD1 in AR DCM (Theis 2011) | **Disambiguation** | **Belongs to CMD2B**, not CMD2H |

---

## Limitations and Knowledge Gaps

1. **Extremely small human evidence base.** The core clinical description rests on a single family (two siblings). Prevalence, penetrance, expressivity, carrier frequency, sex ratio, and geographic/ethnic distribution are essentially unknown.
2. **Substrate specificity unresolved.** It is not established which cardiac TA-protein substrate(s) are most critically depleted; the link from "reduced TA insertion" to "cardiomyocyte failure" is mechanistically plausible and model-supported but the rate-limiting node is inferred.
3. **No natural-history or therapeutic-response data** specific to CMD2H; treatment recommendations are extrapolated from general DCM/heart-failure care.
4. **Historical disambiguation risk.** Much online and literature content conflates "Dilated Cardiomyopathy 2H" with GATAD1; this report explicitly corrects that — CMD2H = GET3/ASNA1; GATAD1 = CMD2B.
5. **No CMD2H-specific biomarkers, modifiers, or epigenetic data** are available.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the case series.** Query GeneMatcher, DECIPHER, and large cardiomyopathy registries (e.g., the Dutch Cardiomyopathy Registry [PMID: 42573902]) for additional biallelic ASNA1/GET3 patients to define phenotypic range and penetrance.
2. **Define the critical cardiac TA-substrate(s).** Proteomics/TA-substrate profiling in Asna1-KO cardiomyocytes and patient-derived iPSC-cardiomyocytes to pinpoint the rate-limiting insertion defect.
3. **iPSC-CM disease modeling.** Generate patient-derived iPSC-cardiomyocytes (and isogenic corrected controls) to characterize contractility, ER stress, and trafficking, and to serve as a therapeutic-screening platform.
4. **Genotype–phenotype and rescue studies.** Systematic in vitro insertion assays across additional ASNA1 variants to build an ACMG-grade functional evidence base (PS3) for clinical variant interpretation.
5. **Preclinical gene-replacement proof of concept.** Test AAV-mediated ASNA1 restoration in the inducible Asna1-KO mouse as a rational strategy for a recessive LoF disorder.
6. **Curate identifiers.** Ensure knowledge-base entries link MONDO:0859358 → OMIM 620203 → GET3/ASNA1 (gene OMIM 601913) and flag the GATAD1/CMD2B distinction to prevent propagation of the historical error.

---

*Evidence source legend:* human clinical (Verhagen 2019, index family), in vitro (TA-insertion assay), model organism (zebrafish asna1; mouse Asna1 conditional KO), computational/population genetics (gnomAD constraint), and database/ontology cross-referencing (Monarch/OLS4, OMIM, MONDO, NCBI Gene).


## Artifacts

- [OpenScientist final report](Cardiomyopathy_Dilated_2H-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cardiomyopathy_Dilated_2H-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859358` (9 mentions) - the report calls it "if available", "cardiomyopathy, dilated, 2H"; MONDO calls it **cardiomyopathy, dilated, 2H**
- `HP:0001644` (1 mention) - the report calls it "Severe, rapidly progressive"; HP calls it **Dilated cardiomyopathy**
- `HP:0001635` (2 mentions) - the report calls it "congestive heart failure", "Severe, fatal"; HP calls it **Congestive heart failure**
- `HP:0001522` (1 mention) - the report calls it "Fatal"; HP calls it **Death in infancy**
- `GO:0005829` (2 mentions) - the report calls it "GO cellular component: cytosol"; GO calls it **cytosol**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001711` (1 mention) - the report calls it "abnormal LV morphology"; HP calls it **Abnormal left ventricle morphology**
- `CL:0000746` (2 mentions) - the report calls it "CL cell type: cardiac muscle cell / cardiomyocyte"; CL calls it **cardiac muscle cell**
- `UBERON:0002349` (1 mention) - the report calls it "cardiac muscle tissue / myocardium"; UBERON calls it **myocardium**, and lists "cardiac muscle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0859358` - called "if available", "cardiomyopathy, dilated, 2H"
- `HP:0001635` - called "congestive heart failure", "Severe, fatal"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.
