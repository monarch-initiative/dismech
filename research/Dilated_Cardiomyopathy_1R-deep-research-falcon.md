---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T13:08:35.740381'
end_time: '2026-09-03T13:17:49.753203'
duration_seconds: 554.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dilated Cardiomyopathy 1R (CMD1R, ACTC1-related dilated cardiomyopathy)
  mondo_id: MONDO:0013261
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0013261
    reported_labels:
    - if available
    ontology_label: dilated cardiomyopathy 1R
  - term_id: HP:0001631
    reported_labels:
    - About **88%** of p.Gly247Asp carriers in the reported families
    ontology_label: Atrial septal defect
  - term_id: HP:0001644
    reported_labels:
    - Core CMD1R phenotype
    ontology_label: Dilated cardiomyopathy
  - term_id: HP:0012664
    reported_labels:
    - Borderline LVEF 52% in one 2023 p.Arg185Trp carrier; severe dysfunction in the
      infant case
    ontology_label: Reduced left ventricular ejection fraction
  - term_id: HP:0001711
    reported_labels:
    - Severe in the 1-year-old 2024 case
    ontology_label: Abnormal left ventricle morphology
  - term_id: HP:0001635
    reported_labels:
    - Late onset in p.Gly247Asp carriers; advanced cases required transplant
    ontology_label: Congestive heart failure
  - term_id: HP:0030680
    reported_labels:
    - Part of broader ACTC1 allelic spectrum, not obligatory CMD1R
    ontology_label: Abnormal cardiovascular system morphology
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dilated_Cardiomyopathy_1R-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1R (CMD1R, ACTC1-related dilated cardiomyopathy)
- **MONDO ID:** MONDO:0013261 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1R (CMD1R, ACTC1-related dilated cardiomyopathy)** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1R (CMD1R, ACTC1-related dilated cardiomyopathy)
- **MONDO ID:** MONDO:0013261 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1R (CMD1R, ACTC1-related dilated cardiomyopathy)** covering all of the
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


# Dilated Cardiomyopathy 1R (CMD1R): ACTC1-related dilated cardiomyopathy

## Executive summary and evidence boundaries

CMD1R is an exceptionally rare, usually autosomal-dominant sarcomeric cardiomyopathy caused by pathogenic germline variants in **ACTC1**, encoding α-cardiac actin. The core phenotype is left-ventricular or biventricular dilation with systolic dysfunction not sufficiently explained by coronary disease, loading conditions, valvular disease, or congenital heart disease. ACTC1 alleles are markedly pleiotropic: different variants can cause isolated DCM, hypertrophic cardiomyopathy (HCM), left-ventricular noncompaction (LVNC), atrial septal defect (ASD), or a congenital-contracture syndrome with cardiac abnormalities. Consequently, pathogenicity and prognosis must be assessed at the **variant–phenotype** level rather than inferred merely from the gene name. Open Targets independently links ACTC1 (ENSG00000159251) to DCM, familial DCM, and familial isolated DCM, drawing partly on landmark human genetic studies (PMIDs 9563954 and 20301486). (OpenTargets Search: dilated cardiomyopathy-ACTC1)

The evidence base consists mainly of a few pedigrees, individual cases, myocardial pathology, cultured cardiomyocytes, purified-protein assays, and computational modeling. Disease-specific prevalence, prospective natural history, treatment-response rates, quality-of-life data, and ACTC1-directed trials are unavailable. General DCM statistics and recommendations are therefore labeled explicitly as extrapolations.

The following table summarizes the most actionable evidence.

| Domain | Best-supported finding | Evidence type | Key ontology/identifier | Important limitation |
|---|---|---|---|---|
| Disease identity | CMD1R denotes ACTC1-related familial dilated cardiomyopathy, a rare sarcomeric cardiomyopathy characterized by ventricular dilation and systolic dysfunction. | Aggregated disease-level resources plus human pedigrees | ACTC1: **MIM 102540**; DCM: MONDO:0005021 | The requested **MONDO:0013261** should be independently verified before database ingestion; some resources map ACTC1 to broad familial DCM rather than a uniquely resolved CMD1R concept. (OpenTargets Search: dilated cardiomyopathy-ACTC1, chong2023variantsinactc1 pages 7-10) |
| Genetic architecture | Best-established disease mechanism is heterozygous germline **missense** variation with autosomal-dominant segregation; de novo cases also occur. | Human familial segregation and case reports | ACTC1; chr15q14; AD inheritance | Penetrance and phenotype are variant-specific; an ACTC1 variant associated with another phenotype cannot automatically be classified as pathogenic for DCM. (frank2019cardiacαactin(actc1) pages 1-2, chong2023variantsinactc1 pages 7-10, acunaochoa2024adenovo pages 1-2) |
| Foundational evidence | Olson et al. identified ACTC1 missense variants cosegregating with hereditary idiopathic DCM in two unrelated families and proposed defective force transmission through Z-band/intercalated-disc interfaces. | Primary human genetic study | Science, May 1998; DOI: [10.1126/science.280.5364.750](https://doi.org/10.1126/science.280.5364.750) | Small pedigree-based discovery study predating modern population databases and ACMG/AMP classification. (chong2023variantsinactc1 pages 22-24) |
| Quantitative familial evidence | **p.Gly247Asp** was present in 15 affected relatives and absent from 63 unaffected relatives; ASD-II occurred in about 88% of carriers, while DCM generally emerged in the fourth–fifth decades. Outcomes included transplantation at ages 51 and 55 and sudden death at 63. | Human linkage, segregation, imaging, and myocardial pathology | ACTC1 p.Gly247Asp; ASD: HP:0001631; DCM: HP:0001644 | “Fully penetrant” referred to the combined familial phenotype; DCM itself affected only a subset and was age-dependent. (frank2019cardiacαactin(actc1) pages 1-2, frank2019cardiacαactin(actc1) pages 4-6) |
| 2023 phenotypic expansion | Five families with heterozygous ACTC1 missense variants established a syndromic spectrum of distal arthrogryposis with congenital heart defects; one p.Arg185Trp carrier had borderline LV systolic function (LVEF 52%) and reduced strain. | Human case series plus molecular-dynamics modeling | DOI: [10.1016/j.xhgg.2023.100213](https://doi.org/10.1016/j.xhgg.2023.100213); ACTC1 MIM 102540 | This is not a classical isolated-CMD1R cohort; it demonstrates allelic and tissue pleiotropy rather than DCM prevalence. (chong2023variantsinactc1 pages 13-16, chong2023variantsinactc1 pages 7-10) |
| 2024 infant case | A 1-year-old with severe LV dilation/dysfunction and sudden death carried apparently de novo **ACTC1 c.664G>A (p.Ala222Thr)** plus paternally inherited **TTN p.Glu11084Lys**. | Single human case; NGS, Sanger validation, and computational modeling | DOI: [10.1155/crig/9517735](https://doi.org/10.1155/crig/9517735); HP:0001644; HP:0001699 | Causality cannot be assigned to ACTC1 alone because of the co-occurring TTN variant and absence of direct functional validation. (acunaochoa2024adenovo pages 1-2) |
| Mechanism | Mutant α-cardiac actin can impair actin polymerization/turnover, thin-filament organization, actomyosin regulation, and force transmission, leading to hypocontractility, sarcomeric disarray, myofibrillar degeneration, apoptosis, extracellular-matrix expansion, remodeling, and heart failure. | Human myocardial pathology, cultured rat cardiomyocytes, purified-protein assays, and computational modeling | Suggested GO: actin filament organization (GO:0007015), muscle contraction (GO:0006936), cardiac muscle contraction (GO:0060048), apoptotic process (GO:0006915) | Mechanisms differ among substitutions; calcium-desensitization and dominant-negative models are plausible but not universal across ACTC1 variants. (frank2019cardiacαactin(actc1) pages 1-2, frank2019cardiacαactin(actc1) pages 4-6, jones2023divergenceofdisease pages 68-73) |
| Diagnosis | Diagnosis requires DCM phenotyping with history/pedigree, ECG, echocardiography, ambulatory rhythm monitoring, and usually CMR, followed by a curated cardiomyopathy panel including ACTC1 and ACMG/AMP variant interpretation; a pathogenic familial variant enables cascade testing. | Contemporary cardiomyopathy guidance extrapolated to ACTC1 | DCM: HP:0001644; reduced LVEF: HP:0012664; genetic testing intervention | No ACTC1-specific diagnostic threshold exists; a VUS must not establish diagnosis or direct predictive testing. (jurcut2025keyprioritiesfor pages 6-7, sorella2025diagnosisandmanagement pages 12-13, mcnally2017dilatedcardiomyopathygenetic pages 3-4) |
| Treatment | Management is phenotype-based guideline-directed therapy for HFrEF and complications: neurohormonal therapy, diuretics for congestion, rhythm/thromboembolism management, ICD/CRT when standard criteria are met, and mechanical support or transplantation for refractory advanced disease. | General DCM/heart-failure guidelines and limited ACTC1 case experience | Suggested NCIT: pharmacologic therapy, implantable cardioverter-defibrillator, cardiac resynchronization therapy, heart transplantation | No drug, device criterion, or pharmacogenomic recommendation is validated specifically for ACTC1-CMD1R. (frustaci2018novelα‐actingene pages 6-7, sorella2025diagnosisandmanagement pages 12-13) |
| Epidemiology | ACTC1-CMD1R is exceptionally rare; no reliable disease-specific prevalence, incidence, carrier frequency, sex ratio, founder effect, or geographic enrichment has been established. | Evidence-gap assessment from sparse pedigrees/cases | Orphan/Mendelian disease; broad DCM only: MONDO:0005021 | General DCM estimates must not be reported as ACTC1-specific epidemiology. (OpenTargets Search: dilated cardiomyopathy-ACTC1, acunaochoa2024adenovo pages 1-2) |
| Clinical trials | No interventional trial specifically targeting ACTC1-CMD1R was identified; available genetic/familial DCM studies enroll mixed genotypes and test early neurohormonal or precision-care strategies. | Clinical-trial registry search | Example mixed-genotype study: NCT05321875 | Results from unselected or mixed-genotype DCM trials cannot be assumed to show ACTC1-specific efficacy. (frank2019cardiacαactin(actc1) pages 1-2, chong2023variantsinactc1 pages 1-5) |


*Table: Compact evidence table distinguishing well-supported ACTC1-specific findings from general DCM guidance and unresolved evidence gaps. It highlights foundational pedigrees, recent phenotypic expansion, mechanisms, and the absence of disease-specific epidemiology or therapy.*

## 1. Disease information

### Definition and nomenclature

**Preferred name:** Dilated cardiomyopathy 1R; **CMD1R**; **ACTC1-related dilated cardiomyopathy**. Common alternatives include *familial dilated cardiomyopathy due to ACTC1*, *cardiac α-actin–related DCM*, and historically *ACTC/ACTC1-associated idiopathic dilated cardiomyopathy*.

**Key identifiers and mappings**

- **Gene:** ACTC1, *actin alpha cardiac muscle 1*; OMIM/MIM **102540**; Ensembl **ENSG00000159251**; chromosome **15q14**. (OpenTargets Search: dilated cardiomyopathy-ACTC1, chong2023variantsinactc1 pages 7-10)
- **Broad DCM:** MONDO **MONDO:0005021**; familial DCM **MONDO:0016333**; familial isolated DCM **MONDO:0700335** in Open Targets. (OpenTargets Search: dilated cardiomyopathy-ACTC1)
- **Requested disease identifier:** **MONDO:0013261** should be verified directly against the current MONDO release before ingestion; the retrieved authoritative mappings did not independently resolve that identifier to CMD1R.
- **OMIM disease number:** commonly reported for CMD1R as **613424**, but the retrieved text also associated MIM 613424 with ACTC1-related LVNC. Because historical ACTC1 phenotype labels overlap, this number likewise requires direct OMIM verification before database loading. (chong2023variantsinactc1 pages 7-10)
- **MeSH:** *Cardiomyopathy, Dilated*; no ACTC1-specific MeSH descriptor identified.
- **ICD-10-CM:** **I42.0**, dilated cardiomyopathy. **ICD-11:** use the current dilated-cardiomyopathy category with genetic etiology extension where locally supported; there is no ACTC1-specific billing code.
- **SNOMED CT:** inherited/familial dilated cardiomyopathy and genetic disorder concepts may be combined; verify release-specific identifiers.

This report is an **aggregated disease-level synthesis** from published patients, pedigrees, experimental systems, guidelines, and databases—not an individual EHR-derived record.

### Foundational evidence

Olson et al. reported ACTC1 missense mutations cosegregating with hereditary idiopathic DCM in two unrelated families. Their abstract states: **“Both mutations affect universally conserved amino acids in domains of actin that attach to Z bands and intercalated discs”** and proposes defective force transmission as a mechanism of heart failure. Science, 1 May 1998; DOI [10.1126/science.280.5364.750](https://doi.org/10.1126/science.280.5364.750); PMID **9563954**. (chong2023variantsinactc1 pages 22-24, OpenTargets Search: dilated cardiomyopathy-ACTC1)

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The initiating lesion is usually a **heterozygous germline ACTC1 missense variant**. Familial segregation supports autosomal-dominant inheritance; de novo alleles also occur. The principal molecular etiologies are variant-dependent disruption of α-cardiac-actin polymerization, thin-filament assembly/regulation, actomyosin mechanics, or force transmission to Z-discs and intercalated discs. (frank2019cardiacαactin(actc1) pages 1-2, acunaochoa2024adenovo pages 1-2, jones2023divergenceofdisease pages 68-73)

### Genetic risk factors

- A pathogenic/likely pathogenic ACTC1 variant is the major causal risk factor.
- Family history of DCM, unexplained heart failure, transplant, sudden death, ASD, HCM, LVNC, arrhythmia, or congenital contractures increases prior probability.
- Additional variants may modify severity. In the 2024 infant report, ACTC1 p.Ala222Thr occurred with a paternally inherited TTN p.Glu11084Lys variant; the contribution of each allele cannot be disentangled. (acunaochoa2024adenovo pages 1-2)
- ACTC1 had only **moderate** monogenic DCM evidence in the 2021 ClinGen-style assessment, emphasizing that even in a valid disease gene, individual variants require rigorous ACMG/AMP evaluation.

No reproducible CMD1R modifier gene, polygenic score, founder allele, or protective ACTC1 allele has been established.

### Environmental and lifestyle factors

There is no ACTC1-specific quantified environmental risk. By analogy with genetic DCM, myocardial stressors—heavy alcohol exposure, cardiotoxic chemotherapy, myocarditis, pregnancy/peripartum stress, uncontrolled hypertension, tachyarrhythmia, and extreme sustained exercise—may unmask or worsen a susceptible myocardium, but this interaction has **not been demonstrated specifically for ACTC1**. Infectious agents do not cause the Mendelian lesion, although viral myocarditis can be a competing or superimposed myocardial insult.

### Protective factors

No genetic or nutritional protective factor is validated. Practical risk reduction consists of avoiding cardiotoxic exposure, treating hypertension and arrhythmias, limiting alcohol, maintaining vaccination and infection prevention appropriate for heart-failure patients, and detecting ventricular dysfunction early. These are tertiary/secondary prevention measures, not prevention of inheriting the variant.

## 3. Phenotypes

| Phenotype | Type and course | Disease-specific evidence | Suggested HPO |
|---|---|---|---|
| Dilated cardiomyopathy | Structural/functional sign; onset ranges from infancy to middle age; often progressive | Core CMD1R phenotype | **HP:0001644** |
| LV dilation | Imaging sign; severity variable | Severe in the 1-year-old 2024 case | **HP:0001711** |
| Reduced systolic function/LVEF | Imaging/functional abnormality | Borderline LVEF 52% in one 2023 p.Arg185Trp carrier; severe dysfunction in the infant case | **HP:0012664** |
| Heart failure | Symptom complex/sign; progressive or episodically decompensated | Late onset in p.Gly247Asp carriers; advanced cases required transplant | **HP:0001635** |
| Dyspnea/exercise intolerance/fatigue | Symptoms | Expected with overt DCM; variant-specific frequencies unavailable | **HP:0002094**, **HP:0003546**, **HP:0012378** |
| Ventricular/atrial arrhythmia | Electrophysiologic sign | Atrial flutter/fibrillation reported after ASD closure; sudden death occurred in severe cases | **HP:0001663**, **HP:0005110**, **HP:0001699** |
| Secundum ASD | Congenital structural sign | About **88%** of p.Gly247Asp carriers in the reported families | **HP:0001631** |
| LVNC/trabeculation | Imaging/pathology sign | Part of broader ACTC1 allelic spectrum, not obligatory CMD1R | **HP:0030680** |
| Sarcomeric/myofibrillar disarray | Histopathology | Demonstrated in p.Gly247Asp myocardium | **HP:0003198** or local pathology term |
| Distal arthrogryposis/contractures | Musculoskeletal manifestation | 2023 allelic syndrome; not typical isolated CMD1R | **HP:0002804**, **HP:0001371** |

In the p.Gly247Asp family, DCM generally emerged in the **fourth or fifth decade**. Documented severe outcomes were transplant at ages **51 and 55** and sudden death at **63**. This demonstrates age-dependent expression of DCM even though the combined ASD/cardiomyopathy familial phenotype was described as fully penetrant. (frank2019cardiacαactin(actc1) pages 4-6)

At the opposite temporal extreme, a 1-year-old Mexican child had severe LV dilation and dysfunction followed by sudden cardiac death. Because the child carried ACTC1 p.Ala222Thr plus a TTN variant, this is evidence for possible oligogenic severe infantile disease, not proof that p.Ala222Thr alone causes CMD1R. Case Reports in Genetics, 2024; DOI [10.1155/crig/9517735](https://doi.org/10.1155/crig/9517735). (acunaochoa2024adenovo pages 1-2)

**Quality of life:** no ACTC1-specific EQ-5D, SF-36, PROMIS, or disease-specific patient-reported outcome study was found. Overt heart failure predictably impairs exertion, employment/school participation, sleep, and psychosocial well-being; arrhythmia and sudden-death risk add anxiety and device burden. These are general DCM effects rather than quantified CMD1R estimates.

## 4. Genetic and molecular information

### Gene and protein

ACTC1 encodes α-cardiac actin, the dominant actin isoform in adult myocardium—reported as approximately **80% of adult cardiac actin**—and an important fetal cardiac and skeletal-muscle protein. Actin monomers polymerize into F-actin, the sarcomeric thin-filament backbone that binds tropomyosin, troponin, myosin, and cytoskeletal anchoring complexes. (chong2023variantsinactc1 pages 13-16)

Suggested annotations include **HGNC:143**, UniProt **P68032** (verify current releases); GO cellular components **sarcomere (GO:0030017)**, **myofibril (GO:0030016)**, **actin filament (GO:0005884)**, **Z disc (GO:0030018)**, and **intercalated disc (GO:0014704)**.

### Variant evidence

- **Foundational DCM variants:** Olson et al. identified two cosegregating missense substitutions in conserved force-transmission domains. The retrieved material did not provide reliable HGVS strings; these should be obtained from the original sequence table rather than reconstructed. (chong2023variantsinactc1 pages 22-24)
- **p.Gly247Asp:** heterozygous exon-5 missense variant, absent from gnomAD/control databases and predicted deleterious by 20/22 algorithms. It occurred in 15 affected relatives and no 63 unaffected relatives in the principal genotyped cohort; a second family also supported segregation. (frank2019cardiacαactin(actc1) pages 1-2, frank2019cardiacαactin(actc1) pages 4-6)
- **c.664G>A, p.Ala222Thr:** apparently de novo in the 2024 infant case; called likely pathogenic by the authors using computational evidence, but direct functional validation and independent cases are absent. Co-occurring TTN variation weakens single-gene attribution. (acunaochoa2024adenovo pages 1-2)
- **p.Arg312His and p.Glu361Gly:** reported DCM-associated substitutions used in mechanistic studies; biochemical effects are assay- and variant-dependent. Purified R312H showed altered regulation and increased residual motility under relaxing conditions in one study. (jones2023divergenceofdisease pages 68-73)
- **2023 syndromic variants:** p.Gly199Ser, p.Arg374Ser, p.Thr68Asn, p.Arg185Trp, and p.Arg374His were de novo or dominantly segregating and absent or exceedingly rare in gnomAD, with CADD >20. They principally caused distal arthrogryposis/congenital defects; they should not automatically be labeled CMD1R variants. (chong2023variantsinactc1 pages 7-10)

The established alleles are overwhelmingly **missense** and germline. A dominant-negative or altered-function mechanism is more plausible than simple haploinsufficiency for many variants, but it has not been demonstrated uniformly. Population allele frequencies are usually absent or extremely low; exact current gnomAD counts must be reported per transcript/build and ancestry. No recurrent pathogenic copy-number change, translocation, repeat expansion, mitochondrial mutation, or somatic ACTC1 mechanism defines CMD1R.

### Modifier and epigenetic data

No CMD1R-specific modifier or epigenetic signature is validated. Increased extracellular-matrix proteins in p.Gly247Asp myocardium indicate downstream remodeling, not a primary inherited epigenetic lesion. No disease-specific methylome, chromatin, single-cell, spatial-transcriptomic, metabolomic, or lipidomic dataset was identified. (frank2019cardiacαactin(actc1) pages 1-2)

## 5. Environmental information

CMD1R is not infectious, toxic, occupational, or radiation-induced. Environmental insults can nevertheless contribute to penetrance or progression of genetic DCM. A clinical work-up should assess alcohol and stimulant use, anthracyclines and other cardiotoxins, pregnancy timing, endurance exercise, endocrine/nutritional disorders, viral illness, and occupational exposures. Evidence that any one exposure interacts specifically with ACTC1 is unavailable. Smoking is a cardiovascular risk factor but is not known to cause CMD1R.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous ACTC1 missense variant **leads to** incorporation of structurally or dynamically altered α-cardiac actin into sarcomeric thin filaments.
2. Altered actin **leads to** variant-specific defects in polymerization/turnover, inter-subunit contacts, tropomyosin–troponin regulation, myosin interaction, or attachment-mediated force transmission; the precise defect is experimentally demonstrated for selected variants but inferred for others. (frank2019cardiacαactin(actc1) pages 1-2, chong2023variantsinactc1 pages 13-16, jones2023divergenceofdisease pages 68-73)
3. Thin-filament dysfunction **results in** impaired or dysregulated actomyosin force generation and relaxation, with reduced effective contractile reserve.
4. Chronic mechanical inefficiency **leads to** myofibrillar/Z-disc disarray and degeneration; a branch **leads to** abnormal calcium-regulated activity, while another branch **leads to** cytoskeletal/intercalated-disc stress.
5. Cellular stress **results in** cardiomyocyte shape abnormalities, apoptosis and probably altered autophagy/mitochondrial handling; apoptosis, autophagic vacuoles, and mitochondrial accumulation were observed in p.Gly247Asp-associated tissue, but causal ordering is partly inferred. (frank2019cardiacαactin(actc1) pages 4-6)
6. Cardiomyocyte loss and mechanical stress **lead to** extracellular-matrix expansion/fibrosis and adverse ventricular remodeling.
7. Remodeling **results in** chamber dilation and reduced ejection fraction, which **lead to** heart failure, functional mitral regurgitation, thromboembolic risk, and atrial or ventricular arrhythmias.
8. Severe pump failure or malignant arrhythmia **leads to** transplantation or premature/sudden death in a subset. (frank2019cardiacαactin(actc1) pages 4-6, acunaochoa2024adenovo pages 1-2)
9. **Developmental branch:** fetal ACTC1 dysfunction **leads to** disturbed actin-dependent morphogenesis and force signaling—an inferred bridge to ASD, LVNC, and contractures—while the same allele may later **lead to** DCM. (frank2019cardiacαactin(actc1) pages 1-2, chong2023variantsinactc1 pages 13-16)

### Mechanistic evidence by system

**Human myocardium:** p.Gly247Asp tissue showed sarcomeric/Z-band disarray, myofibrillar degeneration, wavy/streaming Z-discs, autophagic vacuoles, mitochondrial accumulation, apoptosis, and increased extracellular-matrix proteins. This is direct disease-tissue evidence, although based on very limited sampling. (frank2019cardiacαactin(actc1) pages 1-2, frank2019cardiacαactin(actc1) pages 4-6)

**Cultured cardiomyocytes:** neonatal rat ventricular cardiomyocytes overexpressing p.Gly247Asp developed abnormal morphology, sarcomeric defects, and increased apoptosis compared with wild-type ACTC1. Overexpression and immature rat cells limit quantitative translation to heterozygous adult human myocardium. (frank2019cardiacαactin(actc1) pages 1-2)

**Computational structure:** molecular dynamics implicated impaired G247D polymerization/turnover. Modeling of 2023 contracture-associated variants predicted D-loop/subdomain-2 contact disruption, increased filament disorder, weaker force or slower force development. These are mechanistic predictions, not direct measurements in affected human hearts. (chong2023variantsinactc1 pages 13-16)

**Purified proteins:** R312H/R312C experiments found altered calcium response, incomplete inhibition under relaxing conditions, and possible changed tropomyosin/blocked-state energetics. The authors explicitly treated the link between resting activity and divergent HCM/DCM phenotypes as a hypothesis. (jones2023divergenceofdisease pages 68-73)

Suggested GO biological processes: **actin filament organization (GO:0007015)**, **actin filament polymerization (GO:0030041)**, **muscle contraction (GO:0006936)**, **cardiac muscle contraction (GO:0060048)**, **sarcomere organization (GO:0045214)**, **regulation of heart contraction (GO:0008016)**, **apoptotic process (GO:0006915)**, **extracellular-matrix organization (GO:0030198)**, and **cardiac chamber morphogenesis (GO:0003206)**.

Principal cell types are **cardiac muscle cell/cardiomyocyte (CL:0000746)**, atrial cardiomyocyte, ventricular cardiomyocyte, and downstream cardiac fibroblast. Immune activation, canonical Wnt/MAPK/mTOR pathways, or a disease-specific metabolic pathway has not been established for CMD1R.

## 7. Anatomical structures affected

The primary organ is the **heart (UBERON:0000948)**, especially **myocardium (UBERON:0002349)** and **left ventricle (UBERON:0002084)**; biventricular involvement can occur. The atrial septum is affected in developmental ACTC1 phenotypes. At tissue level, the lesion is cardiac striated muscle; at cellular level, ventricular cardiomyocytes predominate. Subcellular sites are thin filaments, sarcomeres, myofibrils, Z-discs, intercalated discs, and secondarily mitochondria/autophagic compartments. Disease is diffuse rather than unilateral; lateralization is not applicable.

Secondary structures may include atria through dilation/arrhythmia, valves through functional regurgitation, lungs through venous congestion, liver and kidneys through advanced low-output/congestive failure, and systemic arteries/brain through thromboembolism. Skeletal-muscle/joint abnormalities belong principally to the recently delineated syndromic ACTC1 spectrum. (chong2023variantsinactc1 pages 13-16, chong2023variantsinactc1 pages 7-10)

## 8. Temporal development

Onset is highly variable—from severe infantile disease to asymptomatic childhood carrier status and late-onset DCM in the fourth or fifth decade. The usual pattern is chronic and initially insidious: genotype-positive/phenotype-negative state → subtle ECG, strain, or chamber changes → overt LV systolic dysfunction/dilation → symptomatic heart failure/arrhythmia → advanced heart failure or sudden death in severe cases.

The p.Gly247Asp pedigree demonstrates a critical need for **lifelong surveillance**, because congenital ASD preceded late DCM by decades. (frank2019cardiacαactin(actc1) pages 4-6) Reverse remodeling can occur with general heart-failure therapy, but genetic substrate persists; apparent remission does not eliminate relapse risk. No ACTC1-specific progression rate or remission proportion is available.

## 9. Inheritance and population

### Inheritance

Inheritance is predominantly **autosomal dominant**, with vertical transmission and male-to-male transmission possible. De novo missense alleles occur. Penetrance is **variant- and age-dependent**, and expressivity is broad: DCM, ASD, HCM, LVNC, or syndromic contractures may occur. The G247D combined familial phenotype showed strong/nominally complete segregation, but only a subset developed DCM and generally later in life. (frank2019cardiacαactin(actc1) pages 1-2, frank2019cardiacαactin(actc1) pages 4-6)

Genetic anticipation is not established. Germline mosaicism is theoretically possible after an apparently de novo result but has not been documented. Consanguinity is not a typical driver of this dominant disease. No validated founder effect, ethnic enrichment, carrier frequency, geographic cluster, or sex ratio exists.

### Epidemiology

**ACTC1-specific prevalence and incidence are unknown.** Published evidence consists of rare families and cases; broad DCM rates must not be assigned to CMD1R. One 2024 report cited general DCM prevalence of approximately **1:250–400** and incidence of **5–7 per 100,000 person-years**, but those are not ACTC1-specific estimates. (acunaochoa2024adenovo pages 1-2)

## 10. Diagnostics

### Clinical diagnosis

The 2023 ESC phenotype-first framework defines cardiomyopathy by myocardial structural/functional abnormality not sufficiently explained by coronary disease, hypertension, valvular disease, or congenital disease. In ACTC1 carriers, congenital ASD does not exclude superimposed primary myocardial disease if its severity does not account for the cardiomyopathy.

Recommended evaluation, extrapolated from genetic DCM guidance, comprises:

1. Three- to four-generation pedigree and history of heart failure, transplant, sudden death, arrhythmia, stroke, ASD/LVNC/HCM, pregnancy-related disease, and contractures.
2. Examination, 12-lead ECG, transthoracic echocardiography including LV/RV size, LVEF and preferably global longitudinal strain.
3. Ambulatory ECG for ectopy, atrial arrhythmia, conduction disease, or nonsustained ventricular tachycardia.
4. CMR for ventricular phenotype, LVNC assessment, edema, scar/fibrosis and alternative diagnoses.
5. Laboratory testing guided by phenotype: BNP/NT-proBNP, high-sensitivity troponin, blood count, renal/liver/thyroid studies, iron studies, electrolytes, and creatine kinase if skeletal involvement is suspected.
6. Exclusion of ischemic disease, significant valve/loading disease, toxins, endocrine/metabolic causes, tachycardia-mediated cardiomyopathy, and myocarditis.
7. Endomyocardial biopsy only when inflammatory, infiltrative, storage, or other biopsy-addressable disease is suspected; ACTC1 cannot be diagnosed histologically alone.

General inherited-DCM evaluation supports family history, ECG, echo, Holter, CMR and CK, with CMR late gadolinium enhancement helping detect early disease and refine arrhythmic risk. (mcnally2017dilatedcardiomyopathygenetic pages 3-4)

### Genetic testing

Use a **curated cardiomyopathy multigene panel** that includes ACTC1 and well-validated DCM genes, with deletion/duplication analysis where technically appropriate. Panels usually outperform ACTC1-only testing because phenotype overlap and multilocus findings are possible. Analyze an affected proband first and classify variants under ACMG/AMP/ClinGen specifications.

- **Pathogenic/likely pathogenic:** supports molecular diagnosis and enables targeted cascade testing.
- **VUS:** does not establish CMD1R and should not be used for predictive testing or irreversible management; segregation and functional evidence may aid reclassification.
- **Negative panel:** does not exclude genetic DCM. Exome/genome sequencing may detect less typical genes or structural/noncoding variants, ideally with periodic reanalysis.
- **CMA/karyotype/FISH:** low yield for isolated CMD1R; consider for syndromic congenital anomalies.
- **mtDNA and repeat-expansion testing:** not routine unless phenotype suggests another diagnosis.
- **RNA sequencing:** potentially useful for unresolved splice variants, but no validated CMD1R transcriptomic diagnostic exists.

### Family screening

After identifying a familial P/LP variant, offer counseling and targeted testing to first-degree relatives regardless of current symptoms. Genotype-positive relatives require serial ECG and imaging; genotype-negative, phenotype-negative relatives can generally be discharged from disease-specific surveillance unless the family has unresolved complexity. Contemporary implementation guidance suggests ECG plus echocardiography every **1–3 years before age 60** and every **3–5 years thereafter**, individualized for variant, family history, symptoms and phenotype. (jurcut2025keyprioritiesfor pages 6-7, sorella2025diagnosisandmanagement pages 12-13)

Differential diagnoses include TTN-, LMNA-, FLNC-, DSP-, RBM20-, BAG3-, MYH7-, TNNT2-, TPM1-, TNNI3-, and TNNC1-related cardiomyopathies; myocarditis; ischemic, alcohol-, chemotherapy-, tachycardia-, endocrine- or peripartum cardiomyopathy; muscular dystrophy; mitochondrial disease; HCM transitioning to dilation; and LVNC-associated cardiomyopathy.

## 11. Outcome and prognosis

There are no valid ACTC1-specific 5- or 10-year survival curves, mortality rates, or life-expectancy estimates. Prognosis ranges from late asymptomatic carrier status to infantile sudden death. Within the G247D families, advanced outcomes included transplant in the sixth decade and sudden death at 63. (frank2019cardiacαactin(actc1) pages 4-6)

General adverse markers include lower LVEF, RV dysfunction, progressive dilation, myocardial fibrosis/LGE, ventricular arrhythmia, syncope, conduction disease, elevated natriuretic peptide/troponin, recurrent hospitalization, and failure to reverse remodel. Family history of early sudden death or transplant increases concern. ACTC1 has not been validated as one of the genotypes with independent ICD thresholds; standard phenotype-based risk assessment remains appropriate.

Complications include chronic/acute heart failure, atrial and ventricular arrhythmias, sudden cardiac death, functional mitral regurgitation, intracardiac thrombus/systemic embolism, stroke, pulmonary hypertension, and multiorgan dysfunction in advanced failure. Recovery of LVEF is possible with therapy, but inherited susceptibility remains lifelong.

## 12. Treatment and current applications

### Current care

There is **no approved ACTC1-directed treatment**. Management follows DCM/HFrEF and arrhythmia guidelines:

- ARNI or ACE inhibitor/ARB, evidence-based β-blocker, mineralocorticoid-receptor antagonist, and SGLT2 inhibitor for eligible HFrEF patients.
- Loop diuretics for congestion; hydralazine/isosorbide dinitrate, ivabradine, digoxin, or intravenous iron in selected patients.
- Anticoagulation for atrial fibrillation, intracardiac thrombus, previous embolism, or another standard indication—not for genotype alone.
- ICD for secondary prevention and for eligible primary-prevention patients after optimized therapy; CRT for standard electrical/mechanical criteria.
- Catheter ablation or antiarrhythmic therapy for selected clinically important arrhythmias.
- Mechanical circulatory support and heart transplantation for refractory advanced heart failure. Guideline synthesis supports transplant for refractory NYHA III–IV disease without prohibitive contraindications. (sorella2025diagnosisandmanagement pages 12-13)

Suggested NCIT intervention terms: **Pharmacologic Therapy**, **Angiotensin Receptor-Neprilysin Inhibitor**, **Beta Blocker**, **Mineralocorticoid Receptor Antagonist**, **Sodium-Glucose Cotransporter 2 Inhibitor**, **Diuretic**, **Anticoagulant Therapy**, **Implantable Cardioverter-Defibrillator**, **Cardiac Resynchronization Therapy**, **Ventricular Assist Device**, and **Heart Transplantation**; verify current NCIT codes.

A related ACTC1 p.Ala21Val family with HCM/LVNC—not classical CMD1R—was treated with carvedilol, amiodarone, diuretics, ACE inhibition, anticoagulation, and consideration of ICD/transplant, illustrating phenotype-based rather than genotype-specific care. (frustaci2018novelα‐actingene pages 6-7)

### Experimental therapy and trials

No ACTC1-specific gene replacement, CRISPR, ASO/siRNA, cell therapy, or molecular thin-filament drug has reached clinical implementation. Challenges include the structural stoichiometry of sarcomeric actin and the likelihood that many missense alleles act through altered/dominant-negative protein function rather than simple deficiency.

Relevant mixed-genotype trials include **EARLY-GENE, NCT05321875**, a recruiting phase III study of candesartan versus placebo in genetic DCM carriers (planned n=320), and broader familial/genetic DCM precision-medicine studies. These do not establish ACTC1-specific efficacy. No ACTC1-selective interventional trial was identified.

## 13. Prevention

**Primary prevention:** inheritance cannot be prevented by lifestyle. Reproductive options after identifying a familial P/LP variant include preconception counseling, natural conception with prenatal diagnosis, IVF with PGT-M, donor gametes, or adoption. Counseling should address variable expressivity and inability to predict severity reliably.

**Secondary prevention:** targeted cascade testing and longitudinal ECG/echo—plus CMR or ambulatory monitoring when indicated—can detect preclinical disease. The p.Gly247Asp data particularly support long-term surveillance of ACTC1-positive patients initially presenting with ASD. (frank2019cardiacαactin(actc1) pages 1-2, frank2019cardiacαactin(actc1) pages 4-6)

**Tertiary prevention:** early guideline-directed therapy, rhythm surveillance, blood-pressure control, avoidance of cardiotoxins and heavy alcohol, individualized exercise advice, prompt evaluation of pregnancy-related symptoms, vaccination according to heart-failure guidance, and device/transplant referral when indicated. There is no newborn population screening program, vaccine, or prophylactic drug validated specifically for CMD1R.

## 14. Other species and natural disease

ACTC1 orthologues are highly conserved across vertebrates. Relevant taxa include **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, **Rattus norvegicus (10116)**, and **Danio rerio (7955)**. No well-established naturally occurring veterinary syndrome confidently equivalent to human ACTC1-CMD1R was identified, and no breed/VBO association can be recommended. The disorder has no zoonotic potential and is not transmissible between species.

## 15. Model organisms and experimental systems

- **Neonatal rat ventricular cardiomyocytes:** adenoviral p.Gly247Asp overexpression reproduced sarcomeric disruption, abnormal morphology and apoptosis. Strength: direct cardiomyocyte phenotype. Limitation: overexpression, nonhuman and neonatal context. (frank2019cardiacαactin(actc1) pages 1-2, frank2019cardiacαactin(actc1) pages 4-6)
- **Purified regulated thin filaments/actomyosin assays:** R312 substitutions were tested by in-vitro motility, ATPase, tropomyosin-binding and cMyBP-C-fragment assays. Strength: residue-level mechanistic resolution. Limitation: incomplete cellular architecture and discrepant calcium-sensitivity findings across assays. (jones2023divergenceofdisease pages 68-73)
- **Molecular dynamics:** G247D and 2023 syndromic variants predicted defective polymerization, D-loop interactions and filament mechanics. Strength: structural hypotheses; limitation: computational inference. (frank2019cardiacαactin(actc1) pages 1-2, chong2023variantsinactc1 pages 13-16)
- **Human myocardial biopsy:** highest disease relevance and direct visualization of myofibrillar degeneration/remodeling, but exceptionally scarce and cross-sectional. (frank2019cardiacαactin(actc1) pages 4-6)

No validated ACTC1-CMD1R knock-in mouse, zebrafish natural-history platform, patient-specific iPSC-cardiomyocyte series, cardiac organoid, CRISPR rescue screen, or single-cell/spatial atlas was identified in the retrieved evidence. These are major research opportunities.

## Recent developments and expert interpretation

1. **2023 phenotypic expansion:** Chong et al. identified five families with heterozygous ACTC1 variants causing distal arthrogryposis with congenital cardiac defects. The abstract states: **“Our discovery delineates a new DA condition due to mutations in ACTC1 and suggests that some functions of actin, alpha, cardiac muscle 1 are shared in cardiac and skeletal muscle.”** Human Genetics and Genomics Advances, July 2023; DOI [10.1016/j.xhgg.2023.100213](https://doi.org/10.1016/j.xhgg.2023.100213). This establishes allelic pleiotropy but should not inflate CMD1R case counts. (chong2023variantsinactc1 pages 1-5, chong2023variantsinactc1 pages 7-10)

2. **2024 severe infant case:** Acuña-Ochoa et al. reported ACTC1 p.Ala222Thr plus TTN p.Glu11084Lys in a child dying at age one. Their abstract conclusion states that the findings **“suggest a likely pathogenic de novo mutation in ACTC1 in coexpression of a TTN variant as possible causes of an early onset of a severe DCM and premature death.”** The cautious words “suggest” and “possible” are important because this is one computationally supported, potentially oligogenic case. (acunaochoa2024adenovo pages 1-2)

3. **Current expert approach:** contemporary cardiomyopathy guidance favors deep phenotyping, CMR, genetic counseling, curated testing, and cascade screening, while acknowledging major gaps in genotype-specific trajectory and therapy. For ACTC1, experts should resist deterministic counseling: the same gene spans developmental defects, HCM, LVNC, DCM and skeletal contractures. (jurcut2025keyprioritiesfor pages 6-7, sorella2025diagnosisandmanagement pages 12-13, chong2023variantsinactc1 pages 1-5)

## Knowledge gaps and database-ingestion cautions

- Verify **MONDO:0013261** and the phenotype-specific OMIM disease number directly in current source releases.
- Do not treat every rare ACTC1 missense variant as pathogenic or every ACTC1 pathogenic variant as DCM-causing.
- Do not assign broad DCM prevalence, prognosis, or treatment-response statistics to CMD1R.
- “Fully penetrant” G247D segregation applies to the reported combined familial phenotype, not necessarily age-independent DCM.
- p.Ala222Thr remains confounded by a co-occurring TTN variant and lacks direct functional validation.
- No CMD1R-specific environmental exposure, protective factor, biomarker, transcriptomic signature, pharmacogenomic rule, treatment, trial, or validated risk calculator is currently established.

References

1. (OpenTargets Search: dilated cardiomyopathy-ACTC1): Open Targets Query (dilated cardiomyopathy-ACTC1, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (chong2023variantsinactc1 pages 7-10): Jessica X. Chong, Matthew Carter Childers, Colby T. Marvin, Anthony J. Marcello, Hernan Gonorazky, Lili-Naz Hazrati, James J. Dowling, Fatema Al Amrani, Yasemin Alanay, Yolanda Nieto, Miguel Á Marín Gabriel, Arthur S. Aylsworth, Kati J. Buckingham, Kathryn M. Shively, Olivia Sommers, Kailyn Anderson, Michael Regnier, and Michael J. Bamshad. Variants in actc1 underlie distal arthrogryposis accompanied by congenital heart defects. Jul 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100213, doi:10.1016/j.xhgg.2023.100213. This article has 20 citations and is from a peer-reviewed journal.

3. (frank2019cardiacαactin(actc1) pages 1-2): Derk Frank, Ashraf Yusuf Rangrez, Corinna Friedrich, Sven Dittmann, Birgit Stallmeyer, Pankaj Yadav, Alexander Bernt, Ellen Schulze-Bahr, Ankush Borlepawar, Wolfram-Hubertus Zimmermann, Stefan Peischard, Guiscard Seebohm, Wolfgang A. Linke, Hideo A. Baba, Marcus Krüger, Andreas Unger, Philip Usinger, Norbert Frey, and Eric Schulze-Bahr. Cardiac α-actin (actc1) gene mutation causes atrial-septal defects associated with late-onset dilated cardiomyopathy. Circulation. Genomic and precision medicine, 12 8:e002491, Aug 2019. URL: https://doi.org/10.1161/circgen.119.002491, doi:10.1161/circgen.119.002491. This article has 78 citations and is from a peer-reviewed journal.

4. (acunaochoa2024adenovo pages 1-2): Jose G. Acuña-Ochoa, Norma A. Balderrábano-Saucedo, Ana C. Cepeda-Nieto, Maria Y. Alvarado-Cervantes, Vianca L. Ibarra-Garcia, Daniel Barr, Matthew J. Gage, Ryan Pfeiffer, Dan Hu, and Hector Barajas-Martinez. A de novo mutation in actc1 and a ttn variant linked to a severe sporadic infant dilated cardiomyopathy case. Case Reports in Genetics, Jan 2024. URL: https://doi.org/10.1155/crig/9517735, doi:10.1155/crig/9517735. This article has 2 citations.

5. (chong2023variantsinactc1 pages 22-24): Jessica X. Chong, Matthew Carter Childers, Colby T. Marvin, Anthony J. Marcello, Hernan Gonorazky, Lili-Naz Hazrati, James J. Dowling, Fatema Al Amrani, Yasemin Alanay, Yolanda Nieto, Miguel Á Marín Gabriel, Arthur S. Aylsworth, Kati J. Buckingham, Kathryn M. Shively, Olivia Sommers, Kailyn Anderson, Michael Regnier, and Michael J. Bamshad. Variants in actc1 underlie distal arthrogryposis accompanied by congenital heart defects. Jul 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100213, doi:10.1016/j.xhgg.2023.100213. This article has 20 citations and is from a peer-reviewed journal.

6. (frank2019cardiacαactin(actc1) pages 4-6): Derk Frank, Ashraf Yusuf Rangrez, Corinna Friedrich, Sven Dittmann, Birgit Stallmeyer, Pankaj Yadav, Alexander Bernt, Ellen Schulze-Bahr, Ankush Borlepawar, Wolfram-Hubertus Zimmermann, Stefan Peischard, Guiscard Seebohm, Wolfgang A. Linke, Hideo A. Baba, Marcus Krüger, Andreas Unger, Philip Usinger, Norbert Frey, and Eric Schulze-Bahr. Cardiac α-actin (actc1) gene mutation causes atrial-septal defects associated with late-onset dilated cardiomyopathy. Circulation. Genomic and precision medicine, 12 8:e002491, Aug 2019. URL: https://doi.org/10.1161/circgen.119.002491, doi:10.1161/circgen.119.002491. This article has 78 citations and is from a peer-reviewed journal.

7. (chong2023variantsinactc1 pages 13-16): Jessica X. Chong, Matthew Carter Childers, Colby T. Marvin, Anthony J. Marcello, Hernan Gonorazky, Lili-Naz Hazrati, James J. Dowling, Fatema Al Amrani, Yasemin Alanay, Yolanda Nieto, Miguel Á Marín Gabriel, Arthur S. Aylsworth, Kati J. Buckingham, Kathryn M. Shively, Olivia Sommers, Kailyn Anderson, Michael Regnier, and Michael J. Bamshad. Variants in actc1 underlie distal arthrogryposis accompanied by congenital heart defects. Jul 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100213, doi:10.1016/j.xhgg.2023.100213. This article has 20 citations and is from a peer-reviewed journal.

8. (jones2023divergenceofdisease pages 68-73): M Jones. Divergence of disease: a characterization of actin residue r312 and its relation to hypertrophic and dilated cardiomyopathy onset. Unknown journal, 2023.

9. (jurcut2025keyprioritiesfor pages 6-7): Ruxandra Jurcut, Roberto Barriales-Villa, Elena Biagini, Pablo Garcia-Pavia, Iacopo Olivotto, Alexandros Protonotarios, Eloisa Arbustini, Jens Mogensen, Perry Elliott, Elena Arbelo, Juan Pablo Kaski, Cristina Basso, Connie Bezzina, Nico Blom, Rudolf de Boer, Tim de Winter, Marcus Flather, Pablo García-Pavía, Juan R Gimeno, Sabine Klaassen, Giuseppe Limongelli, Bart Loeys, Antonis Pantazis, Sanjay Sharma, Peter Van Tintelen, and James Ware. Key priorities for the implementation of the 2023 esc guidelines for the management of cardiomyopathies in low-resource settings. Mar 2025. URL: https://doi.org/10.1093/ehjqcco/qcae103, doi:10.1093/ehjqcco/qcae103. This article has 7 citations.

10. (sorella2025diagnosisandmanagement pages 12-13): Anna Sorella, Kristian Galanti, Lorena Iezzi, Sabina Gallina, Selma F Mohammed, Neha Sekhri, Mohammed Majid Akhtar, Sanjay K Prasad, Choudhary Anwar Ahmed Chahal, Fabrizio Ricci, and Mohammed Yunus Khanji. Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations. European Heart Journal. Quality of Care & Clinical Outcomes, 11:206-222, Dec 2025. URL: https://doi.org/10.1093/ehjqcco/qcae109, doi:10.1093/ehjqcco/qcae109. This article has 45 citations.

11. (mcnally2017dilatedcardiomyopathygenetic pages 3-4): Elizabeth M. McNally and Luisa Mestroni. Dilated cardiomyopathy: genetic determinants and mechanisms. Circulation Research, 121:731–748, Sep 2017. URL: https://doi.org/10.1161/circresaha.116.309396, doi:10.1161/circresaha.116.309396. This article has 996 citations and is from a highest quality peer-reviewed journal.

12. (frustaci2018novelα‐actingene pages 6-7): Andrea Frustaci, Alessandro De Luca, Valentina Guida, Tommaso Biagini, Tommaso Mazza, Carlo Gaudio, Claudio Letizia, Matteo Antonio Russo, Nicola Galea, and Cristina Chimenti. Novel α‐actin gene mutation p.(ala21val) causing familial hypertrophic cardiomyopathy, myocardial noncompaction, and transmural crypts. clinical‐pathologic correlation. Feb 2018. URL: https://doi.org/10.1161/jaha.117.008068, doi:10.1161/jaha.117.008068. This article has 31 citations.

13. (chong2023variantsinactc1 pages 1-5): Jessica X. Chong, Matthew Carter Childers, Colby T. Marvin, Anthony J. Marcello, Hernan Gonorazky, Lili-Naz Hazrati, James J. Dowling, Fatema Al Amrani, Yasemin Alanay, Yolanda Nieto, Miguel Á Marín Gabriel, Arthur S. Aylsworth, Kati J. Buckingham, Kathryn M. Shively, Olivia Sommers, Kailyn Anderson, Michael Regnier, and Michael J. Bamshad. Variants in actc1 underlie distal arthrogryposis accompanied by congenital heart defects. Jul 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100213, doi:10.1016/j.xhgg.2023.100213. This article has 20 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Dilated_Cardiomyopathy_1R-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013261` (4 mentions) - the report calls it "if available"; MONDO calls it **dilated cardiomyopathy 1R**
- `HP:0001631` (2 mentions) - the report calls it "About **88%** of p.Gly247Asp carriers in the reported families"; HP calls it **Atrial septal defect**
- `HP:0001644` (4 mentions) - the report calls it "Core CMD1R phenotype"; HP calls it **Dilated cardiomyopathy**
- `HP:0012664` (2 mentions) - the report calls it "Borderline LVEF 52% in one 2023 p.Arg185Trp carrier; severe dysfunction in the infant case"; HP calls it **Reduced left ventricular ejection fraction**
- `HP:0001711` (1 mention) - the report calls it "Severe in the 1-year-old 2024 case"; HP calls it **Abnormal left ventricle morphology**
- `HP:0001635` (1 mention) - the report calls it "Late onset in p.Gly247Asp carriers; advanced cases required transplant"; HP calls it **Congestive heart failure**
- `HP:0030680` (1 mention) - the report calls it "Part of broader ACTC1 allelic spectrum, not obligatory CMD1R"; HP calls it **Abnormal cardiovascular system morphology**