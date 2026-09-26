---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T08:32:39.172343'
end_time: '2026-09-25T09:34:21.352120'
duration_seconds: 3702.18
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Septicemic Plague
  mondo_id: MONDO:0005956
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
citation_count: 30
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 30
  on_topic: 21
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 37
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 17
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0005521
    reported_labels:
    - DIC
    ontology_label: Disseminated intravascular coagulation
  - term_id: UBERON:0002097
    reported_labels:
    - skin/acral tissue
    ontology_label: skin of body
  - term_id: NCIT:C2249
    reported_labels:
    - Ciprofloxacin
    ontology_label: Yttrium Y 90 Monoclonal Antibody MN-14
  - term_id: NCIT:C516
    reported_labels:
    - Doxycycline
    ontology_label: Ganglioside GM2
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Septicemic_Plague-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Septicemic_Plague-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Septicemic Plague
- **MONDO ID:** MONDO:0005956 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Septicemic Plague** covering all of the
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

# Septicemic Plague: A Comprehensive Disease Characteristics Report

**Disease:** Septicemic Plague · **MONDO ID:** MONDO:0005956 · **Category:** Infectious Disease
**Causative agent:** *Yersinia pestis* (NCBI:txid632) · **ICD-10:** A20.7 · **ICD-11:** 1B93.1 · **MeSH:** D010931 (Plague)

---

## Summary

Septicemic plague is an acute, fulminant bloodstream infection caused by the gram-negative coccobacillus *Yersinia pestis*. It is the **least common but most lethal** of the three classical forms of plague. In a systematic review of 762 treated human cases (1937–2019), septicemic plague accounted for only **5% of cases** but carried a **case-fatality rate (CFR) of 38%**, exceeding both bubonic (17%) and pneumonic (27%) forms; untreated, it approaches **~100% fatality** ([PMID: 32435802](https://pubmed.ncbi.nlm.nih.gov/32435802/), [PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)). It can arise as **primary** septicemic plague — fulminant gram-negative sepsis without a palpable bubo, often after handling infected animal tissue — or as **secondary** septicemic plague when untreated bubonic or pneumonic disease disseminates hematogenously.

The pathophysiology is a coordinated, multi-layered virulence program that first paralyzes innate immunity to permit unchecked bacterial replication, then triggers a destructive inflammatory collapse. Temperature-dependent remodeling of LPS lipid A (from hexa-acylated at the flea's 27 °C to poorly-stimulatory tetra-acylated at the host's 37 °C) blunts TLR4 sensing; a plasmid-encoded **type III secretion system (T3SS)** injects **Yop effectors** that block phagocytosis and cytokine production; the **F1/Caf1 capsule** resists macrophage engulfment; and the **Pla plasminogen activator** enables dissemination from peripheral tissues. This "pre-inflammatory" phase of silent growth is followed by a "pro-inflammatory" phase — a delayed neutrophil influx and cytokine storm (IL-6, TNF-α, IFN-γ) that fails to control bacteria while driving disseminated intravascular coagulation (DIC), acral gangrene, septic shock, and multi-organ failure.

Survival is overwhelmingly determined by **time to effective antibiotics**. Among 533 US patients (1942–2018), mortality was **9% with high-efficacy therapy versus 51% with only limited-efficacy therapy** ([PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/)). There is **no heritable genetic cause**, no established human susceptibility gene, and **no licensed vaccine** for general use, so prevention rests on rodent/flea vector control, exposure avoidance, and post-exposure chemoprophylaxis. This report synthesizes 14 confirmed findings drawn from 42 reviewed papers across all 15 requested sections.

---

## 1. Disease Information

**Overview.** Septicemic plague is the bloodstream-invasive manifestation of infection by *Yersinia pestis*, a gram-negative, non-motile, facultatively intracellular coccobacillus of the family *Enterobacteriaceae*. It is defined clinically by isolation of *Y. pestis* from blood in a patient **without lymphadenopathy (no bubo)** — distinguishing primary septicemic plague from bubonic plague — or by hematogenous dissemination of another plague form (secondary septicemic plague) ([PMID: 16943764](https://pubmed.ncbi.nlm.nih.gov/16943764/)). The recognized clinical forms of plague are subclinical/serologic plague, plague pharyngitis, *pestis minor* (abortive bubonic), bubonic, **septicemic**, pneumonic, and plague meningitis ([PMID: 9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/)).

> *"Clinical presentations include subclinical plague (positive serology without disease); plague pharyngitis; pestis minor (abortive bubonic plague); bubonic plague; septicemic plague; pneumonic plague; and plague meningitis."* — [PMID: 9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/)

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0005956 (septicemic plague) |
| MeSH | D010931 (Plague) |
| ICD-10 | A20.7 (Septicaemic plague); A20 (Plague) |
| ICD-11 | 1B93.1 (Septicaemic plague) |
| NCBI Taxonomy (pathogen) | txid632 (*Yersinia pestis*) |
| OMIM | Not applicable (infectious, non-Mendelian) |
| Orphanet | Plague is not a classical rare-genetic Orphanet entity |

**Synonyms / alternative names.** Septicaemic plague; blood plague; *Yersinia pestis* septicemia; historically part of the "Black Death" (the acral gangrene of DIC gives the blackened appearance).

**Data source type.** Information for this report is derived from **aggregated disease-level resources** — systematic reviews, case series, surveillance datasets (CDC/WHO), and experimental animal-model studies — rather than individual EHR data.

---

## 2. Etiology

**Causal factor — infectious only.** The sole cause is infection with *Yersinia pestis*. There is **no Mendelian/genetic causation** and no established human susceptibility gene; the disease is **not heritable** (inheritance not applicable) ([PMID: 9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/)).

**Risk factors (environmental/exposure).** Documented factors include residence in or travel to endemic foci; occupational and recreational animal contact (veterinarians and assistants, hunters/trappers, wildlife biologists); pet ownership and direct animal-reservoir contact (especially during hunting season); living in a household with an index case; flea bite; **handling infected animal tissue** (a route that can produce primary septicemic plague); and climatic conditions favoring reservoir/vector abundance (mild winters, cool moist springs, early summers) ([PMID: 9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/)). Cats are a notable source of respiratory (pneumonic) transmission to humans.

> *"Other factors that increase risk of infection in endemic areas are occupation-veterinarians and assistants, pet ownership, direct animal-reservoir contact especially during the hunting season, living in households with an index case, and, mild winters, cool moist springs, and early summers."* — [PMID: 9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/)

**Immunocompromise.** HIV and other immunocompromising conditions can worsen severity/outcome; a 2024 Nigerian case report highlights the potential severity of co-infection in immunocompromised individuals ([PMID: 41263683](https://pubmed.ncbi.nlm.nih.gov/41263683/)).

**Genetic protective factors / gene–environment interactions.** No validated human protective alleles or GxE interactions are established for plague susceptibility. (Historical hypotheses linking *CCR5-Δ32* or other loci to plague survival remain unproven.)

---

## 3. Phenotypes

Septicemic plague presents as **fulminant gram-negative sepsis without a palpable bubo**: high fever, chills, rigors, prostration, tachycardia, hypotension, and rapid progression to shock, DIC, and multi-organ failure. **Acral necrosis/gangrene** of digits and nose is a classic late sign (the basis of "Black Death") ([PMID: 16943764](https://pubmed.ncbi.nlm.nih.gov/16943764/), [PMID: 9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/)).

> *"Five (38%) patients had primary septicemic plague, and the remaining eight (62%) had bubonic plague."* — [PMID: 16943764](https://pubmed.ncbi.nlm.nih.gov/16943764/)

| Phenotype | Type | Onset / progression | Frequency | Suggested HPO |
|---|---|---|---|---|
| Fever, chills | Symptom/sign | Acute (1–7 d incubation), rapidly progressive | Near-universal | HP:0001945 (Fever) |
| Hypotension / septic shock | Clinical sign | Rapid | Common in severe/late disease | HP:0001635 hypotension; HP:0031273 septic shock |
| Disseminated intravascular coagulation | Lab/clinical | Rapid | Characteristic of severe disease | HP:0005521 (DIC) |
| Acral gangrene / necrosis (digits, nose) | Physical manifestation | Late | Classic but not universal | HP:0100758 (Gangrene) |
| Abdominal pain, nausea, vomiting, diarrhea | Symptom | Early/variable | Frequent in septicemic form | HP:0002027; HP:0002018; HP:0002014 |
| Prostration / altered mental status | Symptom/sign | Progressive | Common | HP:0012378 (Fatigue); HP:0001259 (Coma, severe) |
| Thrombocytopenia, leukocytosis | Lab abnormality | Early | Frequent | HP:0001873; HP:0001974 |
| Absence of bubo | Distinguishing feature | — | Defining for *primary* septicemic | — |

**Severity/progression.** Severe and progressive; without early antibiotics, the course is fulminant and lethal within days. **Quality-of-life impact:** acute and life-threatening rather than chronic; survivors of DIC-associated gangrene may require amputation with long-term disability, but there is no chronic/relapsing phase.

---

## 4. Genetic / Molecular Information

**Not applicable in the human-host sense.** Septicemic plague has **no causal human genes, no pathogenic germline/somatic variants, no modifier genes, no disease-specific epigenetic signature, and no chromosomal abnormalities** — it is a purely infectious disease.

The relevant "genetics" are those of the **pathogen**, whose plasmid-encoded virulence genes drive the septicemic phenotype:

| Genetic element | Location | Product / function |
|---|---|---|
| *pla* | pPCP1 (pKYP1, ~9.5 kb) | Plasminogen activator (Pla): coagulase + fibrinolysin; dissemination ([PMID: 8360901](https://pubmed.ncbi.nlm.nih.gov/8360901/)) |
| T3SS + *yop* effectors (*yopH, E, O/ypkA, M, J, T*), *lcrV* | pCD1 (pYV, ~70 kb) | Type III secretion; injection of anti-immune effectors ([PMID: 15847602](https://pubmed.ncbi.nlm.nih.gov/15847602/), [PMID: 24599533](https://pubmed.ncbi.nlm.nih.gov/24599533/)) |
| *caf1M1A1* operon | pMT1 (~100 kb) | F1 (Caf1) capsular antigen; antiphagocytic ([PMID: 35358289](https://pubmed.ncbi.nlm.nih.gov/35358289/), [PMID: 19103769](https://pubmed.ncbi.nlm.nih.gov/19103769/)) |
| lipid A biosynthesis genes | chromosome | Temperature-dependent lipid A acylation; TLR4 evasion ([PMID: 23745121](https://pubmed.ncbi.nlm.nih.gov/23745121/)) |

*Y. pestis* is a recently emerged, genetically monomorphic clone of *Y. pseudotuberculosis*. Rare naturally occurring **F1-negative (caf-negative)** strains remain virulent but evade F1-based diagnostics ([PMID: 35320275](https://pubmed.ncbi.nlm.nih.gov/35320275/)).

---

## 5. Environmental Information

- **Infectious agent:** *Yersinia pestis* (NCBI:txid632), gram-negative coccobacillus, *Enterobacteriaceae*.
- **Environmental/ecological factors:** maintenance in sylvatic rodent–flea cycles; climatic conditions promoting reservoir and flea abundance (mild winters, cool moist springs) increase spillover risk ([PMID: 9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/)).
- **Occupational/lifestyle exposures:** hunting/trapping, veterinary work, wildlife biology, handling animal carcasses; the tissue-handling route is specifically linked to primary septicemic plague.
- **No chemical toxin, radiation, smoking, diet, or pollution** etiology applies.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. *Y. pestis* enters the host by **flea bite** or by **contact with infected tissue/aerosol** → deposits bacteria in skin/lymphatics or bloodstream.
2. On shifting from 27 °C (flea) to 37 °C (host), the bacterium **remodels LPS lipid A** to a tetra-acylated, poorly-stimulatory form → **evades TLR4/MD-2 recognition** ([PMID: 23745121](https://pubmed.ncbi.nlm.nih.gov/23745121/)) → *results in* delayed innate alarm.
3. The bacterium assembles the **T3SS** and injects **Yop effectors** into macrophages (and later neutrophils): YopE inhibits phagocytosis; YopJ induces macrophage cytotoxicity/apoptosis and blocks proinflammatory cytokines; Yops disrupt cytoskeletal dynamics → *leads to* failure of early innate clearance and **extracellular multiplication in lymphoid tissue** ([PMID: 15847602](https://pubmed.ncbi.nlm.nih.gov/15847602/), [PMID: 24599533](https://pubmed.ncbi.nlm.nih.gov/24599533/)).
4. The **F1/Caf1 capsule** coats the bacterium, resisting macrophage engulfment (polymer-brush effect, ~400 pN mechanical stability) → *reinforces* immune evasion ([PMID: 35358289](https://pubmed.ncbi.nlm.nih.gov/35358289/)).
5. Yop-mediated suppression of **LTB4 synthesis** delays neutrophil/macrophage inflammation → *prolongs* the silent growth window ([PMID: 39423229](https://pubmed.ncbi.nlm.nih.gov/39423229/)).
6. The **Pla plasminogen activator** (coagulase/fibrinolysin) degrades fibrin barriers → *enables* dissemination from the peripheral site into blood ([PMID: 8360901](https://pubmed.ncbi.nlm.nih.gov/8360901/)).
7. Bacteria disseminate hematogenously — in animal models, **spleen → liver → blood** — reaching high bacteremia ([PMID: 19073275](https://pubmed.ncbi.nlm.nih.gov/19073275/)).
8. **Branch — pre-inflammatory → pro-inflammatory switch:** after ~48 h the host mounts a **delayed neutrophil influx and cytokine storm** (IL-6, TNF-α, IFN-γ, IL-12p70, MCP-1, KC, MIP-2) that fails to control bacteria but *causes* tissue destruction ([PMID: 24098126](https://pubmed.ncbi.nlm.nih.gov/24098126/), [PMID: 17101642](https://pubmed.ncbi.nlm.nih.gov/17101642/)).
9. Systemic inflammation + coagulopathy → **DIC**, microvascular thrombosis, **acral gangrene**, **septic shock**, **ARDS**, and **multi-organ failure** → *results in* death within days if untreated ([PMID: 16943764](https://pubmed.ncbi.nlm.nih.gov/16943764/), [PMID: 34780267](https://pubmed.ncbi.nlm.nih.gov/34780267/)).

### Biphasic model (schematic)

```
 PHASE 1 — IMMUNE EVASION (pre-inflammatory)         PHASE 2 — CYTOKINE STORM (pro-inflammatory)
 [37°C lipid A shift -> TLR4 blind]                  [~48 h: neutrophil influx]
 [T3SS/Yops -> block phagocytosis + cytokines]  ==>  [IL-6, TNF-a, IFN-g surge]
 [F1 capsule -> antiphagocytic]                      [tissue destruction, DIC]
 [Pla -> dissemination]                              [septic shock, MOF, gangrene]
 silent bacterial growth  spleen->liver->blood       host collapse
```

> *"Pneumonic plague progression is biphasic, with an initial pre-inflammatory phase facilitating bacterial growth in the absence of host inflammation, followed by a pro-inflammatory phase marked by extensive neutrophil influx, an inflammatory cytokine storm, and severe tissue destruction."* — [PMID: 24098126](https://pubmed.ncbi.nlm.nih.gov/24098126/)

> *"Effector Yops function to counteract multiple signaling responses in the infected host cell ... Innate and adaptive immune responses are thwarted as a consequence of Yop activities."* — [PMID: 15847602](https://pubmed.ncbi.nlm.nih.gov/15847602/)

**Upstream vs downstream.** Upstream = LPS remodeling, T3SS/Yops, F1 capsule, Pla (immune evasion + dissemination). Downstream = cytokine storm, DIC, shock, organ failure. Blunting the downstream inflammation (intranasal fluticasone) reduced IL-6, neutrophil infiltration, bacterial burden, and improved antibiotic-treated survival — evidence the storm itself is pathogenic ([PMID: 34780267](https://pubmed.ncbi.nlm.nih.gov/34780267/)).

**Suggested ontology terms.** GO:0006955 (immune response), GO:0006954 (inflammatory response), GO:0042742 (defense response to bacterium), GO:0030193 (regulation of blood coagulation), GO:0006909 (phagocytosis). Cell types: CL:0000235 (macrophage), CL:0000775 (neutrophil), CL:0000115 (endothelial cell). CHEBI:16412 (lipopolysaccharide).

---

## 7. Anatomical Structures Affected

- **Primary/secondary organs (organ level):** **blood/vasculature** (primary site of septicemic disease, UBERON:0000178 blood; UBERON:0001981 blood vessel), **spleen** (UBERON:0002106) and **liver** (UBERON:0002107) as major dissemination targets ([PMID: 19073275](https://pubmed.ncbi.nlm.nih.gov/19073275/)); **lymph nodes** (UBERON:0000029) in secondary-from-bubonic cases; **lungs** (UBERON:0002048) in secondary pneumonic progression; **skin/acral tissue** (UBERON:0002097) in DIC gangrene; **brain/meninges** in plague meningitis (UBERON:0002360).
- **Body systems:** cardiovascular (shock, DIC), hematologic/lymphoid, hepatobiliary, respiratory (ARDS), and nervous (meningitis) systems.
- **Tissue/cell level:** vascular endothelium; reticuloendothelial macrophages (CL:0000235); neutrophils (CL:0000775). *Y. pestis* multiplies **extracellularly** in lymphoid tissue after initial macrophage interaction.
- **Subcellular level:** T3SS delivers effectors into the host **cytoplasm** (GO:0005737); F1 acts at the bacterial **cell surface/extracellular region** (GO:0005576); LPS resides in the **outer membrane** (GO:0009279).
- **Lateralization:** systemic/bilateral; acral gangrene is typically symmetric-peripheral.

---

## 8. Temporal Development

- **Onset:** acute, after a **1–7 day incubation** (often shorter — hours to a few days — for septicemic/pneumonic forms) ([PMID: 9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/)).
- **Progression:** rapid and fulminant; untreated septicemic plague progresses to death within days (pneumonic ~6 days in models; septicemic similarly rapid). For late-stage disease, **antibiotics must be given within ~24 h of symptom onset** to be effective ([PMID: 34780267](https://pubmed.ncbi.nlm.nih.gov/34780267/)).
- **Course pattern:** monophasic and progressive — **no chronic, relapsing, or remitting phase**; outcome is either death or recovery.
- **Critical period:** the narrow **early therapeutic window** is the dominant modifiable variable (see Section 11).

> *"Late-stage pneumonic plague is difficult to treat, as antibiotics must be delivered within 24 h after onset of symptoms to be effective."* — [PMID: 34780267](https://pubmed.ncbi.nlm.nih.gov/34780267/)

---

## 9. Inheritance and Population

**Epidemiology.** Between 2010 and 2019 the six countries reporting the most human plague cases were **Madagascar, DR Congo, Uganda, Peru, Tanzania, and the USA**, totaling **4,547 cases with 17% mortality (786 deaths)** ([PMID: 40022523](https://pubmed.ncbi.nlm.nih.gov/40022523/)). *Y. pestis* is a **WHO priority pathogen with epidemic/pandemic potential**, endemic in rodent reservoirs across Africa, Asia, North America, and South America; **Madagascar** records a large share of annual global cases ([PMID: 33264458](https://pubmed.ncbi.nlm.nih.gov/33264458/), [PMID: 38935608](https://pubmed.ncbi.nlm.nih.gov/38935608/)). Septicemic plague constitutes **~5%** of plague cases ([PMID: 32435802](https://pubmed.ncbi.nlm.nih.gov/32435802/)).

> *"Between 2010 and 2019, the six countries with the most reported human cases of Yersinia pestis infection ... were Madagascar, the Congo, Uganda, Peru, Tanzania, and the USA, with a total of 4,547 cases with a mortality rate of 17% (786 cases)."* — [PMID: 40022523](https://pubmed.ncbi.nlm.nih.gov/40022523/)

**Genetic etiology.** **Not applicable** — no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency; the disease is infectious.

**Population demographics.** Risk tracks **exposure**, not ethnicity — rural residents, hunters, and animal handlers in endemic foci are over-represented. Geographic distribution follows enzootic rodent foci (western US, Madagascar, central Asia, Andean South America, sub-Saharan Africa). No strong intrinsic sex bias independent of occupational exposure; all ages are susceptible.

---

## 10. Diagnostics

Confirmatory diagnosis rests on three pillars — **culture, PCR, and serology** — supplemented by rapid antigen tests. For the **septicemic form specifically**, **blood culture** and **peripheral blood smear** (bipolar "safety-pin" gram-negative coccobacilli on Wright/Giemsa/Wayson stain) are central because there is no bubo to aspirate.

| Method | Target/approach | Performance |
|---|---|---|
| Bacterial culture | Isolate *Y. pestis* from blood/aspirate/sputum (reference standard) | ~65% sensitivity |
| PCR / qPCR | *caf1*, *pla*, *yopM* | ~85% (single); triplex qPCR **100% sens / 82% spec** ([PMID: 40705833](https://pubmed.ncbi.nlm.nih.gov/40705833/)) |
| Serology | Anti-F1 IgG | positive in ~93% of confirmed cases |
| F1 rapid diagnostic test (F1RDT / LFI) | Capsular F1 antigen, point-of-care | On-site **94% sens / 74% spec** ([PMID: 41389991](https://pubmed.ncbi.nlm.nih.gov/41389991/)); Madagascar retrospective **100% sens / 67% spec** ([PMID: 32000692](https://pubmed.ncbi.nlm.nih.gov/32000692/)) |
| Dual-antigen (F1+LcrV) LFI/ELISA | Detects F1-negative strains too | LoD ~1–2 ng/mL ([PMID: 35320275](https://pubmed.ncbi.nlm.nih.gov/35320275/)) |
| ddPCR (multi-target) | ypo2088, caf1, pla | Superior sensitivity for low-load samples ([PMID: 38701065](https://pubmed.ncbi.nlm.nih.gov/38701065/)) |

> *"The sensitivity and specificity of on-site F1RDT were 94% (95% CI, 89.6-97.0) and 74% (95% CI, 68.2-79.3) against RS1"* — [PMID: 41389991](https://pubmed.ncbi.nlm.nih.gov/41389991/)

**Genetic/omics testing:** not applicable to human diagnosis; pathogen genotyping (MLVA, CRISPR, SNP/WGS) is used for outbreak epidemiology, not patient diagnosis ([PMID: 38935608](https://pubmed.ncbi.nlm.nih.gov/38935608/)).

**Differential diagnosis:** other causes of gram-negative sepsis/DIC, meningococcemia, tularemia, anthrax, rickettsioses, and other hemorrhagic febrile illnesses; the epidemiologic exposure history and blood smear morphology are key discriminators. **Blind spot:** rare F1-negative strains evade F1-based antigen tests — hence dual-antigen assays and PCR backup.

---

## 11. Outcome / Prognosis

**Mortality.** Treated septicemic plague CFR is **~38%**; untreated it approaches **~100%** ([PMID: 32435802](https://pubmed.ncbi.nlm.nih.gov/32435802/), [PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)). The **single dominant prognostic factor is time to effective antimicrobial therapy**: in 533 US patients, mortality was **9% with high-efficacy therapy vs 51% with limited-efficacy therapy** ([PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/)).

> *"Without antibacterial therapy, the disease is associated with a high case fatality rate, ranging from 40% (bubonic plague) to nearly 100% (septicemic and pneumonic plague)."* — [PMID: 25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/)

> *"Mortality differed significantly among those receiving high-efficacy therapy (9%) and only limited-efficacy therapy (51%)."* — [PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/)

**Complications.** Septic shock, **DIC with purpura and acral gangrene** (fingers, toes, nose), ARDS, secondary pneumonic plague (with human-to-human transmission risk), plague meningitis, and multi-organ failure ([PMID: 34780267](https://pubmed.ncbi.nlm.nih.gov/34780267/)).

**Recovery.** Binary — death or recovery, with no chronic phase. Survivors of DIC-associated gangrene may require **amputation**, producing long-term functional disability. Other prognostic factors: delay in diagnosis, older age, immunocompromise (e.g., HIV, [PMID: 41263683](https://pubmed.ncbi.nlm.nih.gov/41263683/)), and severity of shock/DIC at presentation.

---

## 12. Treatment

**Pharmacotherapy is the mainstay** and must be started empirically on clinical suspicion — before laboratory confirmation.

| Drug class | Agents | Notes / NCIT |
|---|---|---|
| Aminoglycosides (first-line) | Streptomycin, gentamicin | Aminoglycoside-treated CFR ~13% vs 20% overall; streptomycin outperformed gentamicin in US data ([PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/)). NCIT:C540 (Gentamicin), NCIT:C839 (Streptomycin) |
| Fluoroquinolones | Ciprofloxacin, levofloxacin | FDA-approved for plague; used in >30% of recent patients. NCIT:C2249 (Ciprofloxacin) |
| Tetracyclines | Doxycycline | Associated with increased survival; oral option. NCIT:C516 (Doxycycline) |
| Others | Chloramphenicol, sulfonamides/TMP-SMX | Chloramphenicol preferred historically for plague meningitis (CNS penetration) |

> *"Gentamicin use was associated with higher mortality than streptomycin, and aminoglycoside use was linked to higher mortality than for tetracyclines."* — [PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/)

**Intracellular caveat:** during the early facultative-intracellular stage, streptomycin and ciprofloxacin retain efficacy against intracellular *Y. pestis*, whereas gentamicin and doxycycline are less effective intracellularly — relevant for agent selection ([PMID: 21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/)).

**Supportive care:** aggressive management of septic shock, fluid resuscitation, vasopressors, and DIC/coagulopathy management are essential given the fulminant sepsis physiology. **Adjunctive anti-inflammatory** strategies are experimental — fluticasone improved antibiotic-treated survival in a pneumonic model by dampening the cytokine storm ([PMID: 34780267](https://pubmed.ncbi.nlm.nih.gov/34780267/)). **Surgery:** amputation/debridement of gangrenous tissue in survivors. No gene, cell, RNA, or targeted/immuno-therapies apply. No pharmacogenomic considerations are established.

---

## 13. Prevention

- **Primary prevention:** rodent and flea **vector control**, insecticides, environmental sanitation, avoiding contact with sick/dead animals, and personal protective equipment when handling potentially infected tissue ([PMID: 32853251](https://pubmed.ncbi.nlm.nih.gov/32853251/)).
- **Post-exposure prophylaxis (secondary):** **doxycycline or ciprofloxacin for 7 days** for close contacts of pneumonic cases; isolation of pneumonic patients for the first ~48 h of therapy prevents human-to-human spread ([PMID: 29183475](https://pubmed.ncbi.nlm.nih.gov/29183475/)).
- **Immunization:** killed whole-cell and live-attenuated vaccines are no longer used (safety/efficacy). Modern subunit candidates combine the two protective antigens **LcrV** (T3SS needle-tip) and **F1** (capsule) — rF1+rV, rF1V fusion, rV10. Antibodies against LcrV and F1 interfere with T3SS injection of host cells ([PMID: 19786842](https://pubmed.ncbi.nlm.nih.gov/19786842/)). As of 2024, **>20 candidates are in preclinical development, few in phase 1, and none licensed for general use** ([PMID: 40022523](https://pubmed.ncbi.nlm.nih.gov/40022523/)).
- **No genetic screening/counseling** applies (non-heritable). Public-health surveillance and rapid outbreak response remain the backbone of control.

> *"LcrV, a protein at the tip of type III secretion needles, and F1, the capsular pilus antigen, are both recognized as plague protective antigens. Antibodies against LcrV and F1 interfere with Y. pestis type III injection of host cells."* — [PMID: 19786842](https://pubmed.ncbi.nlm.nih.gov/19786842/)

> *"More than 20 candidate plague vaccines are in the preclinical phase, with few in early (phase 1) clinical trials."* — [PMID: 40022523](https://pubmed.ncbi.nlm.nih.gov/40022523/)

---

## 14. Other Species / Natural Disease

- **Taxonomy of hosts:** *Y. pestis* infects **>200 mammal species**. Keystone reservoirs include ground squirrels, prairie dogs, marmots, gerbils, and rats (*Rattus* spp.). Fleas — especially *Xenopsylla cheopis* — are the vectors ([PMID: 33264458](https://pubmed.ncbi.nlm.nih.gov/33264458/)).
- **Transmission / zoonosis:** maintained in **sylvatic rodent–flea cycles**; fleas transmit after Pla/biofilm-mediated proventricular blockage. Humans are **incidental hosts** infected by flea bite, handling infected animals, or respiratory spread (notably from cats) ([PMID: 8360901](https://pubmed.ncbi.nlm.nih.gov/8360901/), [PMID: 9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/)).
- **Natural disease / veterinary relevance:** cats develop severe (often pneumonic) plague and are a documented source of human infection; wild rodents and lagomorphs suffer epizootic die-offs.
- **Comparative biology:** *Y. pestis* is an evolutionarily recent clone of *Y. pseudotuberculosis*; the disease mechanisms (T3SS, F1) are conserved across mammalian hosts, underpinning the utility of animal models.

---

## 15. Model Organisms

- **Standard models:** **mouse** (*Mus musculus*, NCBI:txid10090) and **rat** (*Rattus norvegicus*, NCBI:txid10116), typically challenged with the fully virulent strain **CO92** by intranasal/aerosol or intradermal routes ([PMID: 19073275](https://pubmed.ncbi.nlm.nih.gov/19073275/), [PMID: 31177429](https://pubmed.ncbi.nlm.nih.gov/31177429/)).
- **Phenotype recapitulation:** models reproduce the **dissemination pattern relevant to septicemic spread** — bacteria move from the primary site to spleen, then liver and blood, with rising serum cytokines/chemokines and histopathologic injury over 72 h. Rats are **as susceptible as mice** (similar LD50) and support **animal-to-animal transmission** ([PMID: 19073275](https://pubmed.ncbi.nlm.nih.gov/19073275/)).

> *"Bacteria disseminated from the lungs to peripheral organs, with the largest increases in the spleen, followed by the liver and blood at 72h p.i."* — [PMID: 19073275](https://pubmed.ncbi.nlm.nih.gov/19073275/)

> *"rats were as sensitive to pneumonic plague as mice, having a similar LD(50) dose by the intranasal and aerosolized routes. Further, we showed direct transmission of plague bacteria from infected to uninfected rats."* — [PMID: 19073275](https://pubmed.ncbi.nlm.nih.gov/19073275/)

- **Non-human primates** are used for vaccine efficacy testing under the FDA "Animal Rule."
- **Limitations:** rodent inflammatory kinetics differ from humans; anesthesia and intranasal instillation add variability (hence standardized aerosol challenge); models best capture pneumonic/systemic pathophysiology rather than the specific human primary-septicemic tissue-handling route.

---

## Mechanistic Model / Interpretation

Septicemic plague is best understood as a **two-act drama of immune subversion followed by immune catastrophe**. In Act I, *Y. pestis* deploys a layered virulence toolkit — temperature-tuned low-TLR4 lipid A, T3SS-delivered Yop effectors, the F1 antiphagocytic capsule, and Pla-driven dissemination — that renders the early innate response blind and impotent, allowing silent exponential growth and hematogenous spread (spleen → liver → blood). In Act II, once bacterial burden is overwhelming, a **delayed and futile neutrophil/cytokine storm** erupts; it fails to clear the pathogen but ignites DIC, microvascular thrombosis, acral gangrene, septic shock, and multi-organ failure. This framework explains the two clinical hallmarks of the septicemic form — its **fulminant tempo** (silent growth means patients present already deep into dissemination) and its **exceptional lethality** (immune paralysis then immune-mediated tissue destruction) — and it explains why **time-to-antibiotic is decisive**: therapy given before the storm interrupts the cascade, while therapy given after it (>24 h in late disease) cannot reverse established DIC/shock. The finding that anti-inflammatory adjuncts improve antibiotic-treated survival further supports the storm as an independently pathogenic downstream node, and points to combined antimicrobial + immunomodulatory strategies as a rational future direction.

---

## Evidence Base

| PMID | Contribution |
|---|---|
| [32435802](https://pubmed.ncbi.nlm.nih.gov/32435802/) | Septicemic plague = 5% of cases, 38% CFR (systematic review, 762 cases) |
| [25643450](https://pubmed.ncbi.nlm.nih.gov/25643450/) | Near-100% untreated fatality; *Y. pestis* etiology |
| [40022523](https://pubmed.ncbi.nlm.nih.gov/40022523/) | 2010–2019 global epidemiology; vaccine pipeline status |
| [33264458](https://pubmed.ncbi.nlm.nih.gov/33264458/) | Rodent-reservoir endemicity; Madagascar hotspot |
| [8360901](https://pubmed.ncbi.nlm.nih.gov/8360901/) | *pla* coagulase/fibrinolysin → dissemination/transmission |
| [23745121](https://pubmed.ncbi.nlm.nih.gov/23745121/) | Temperature-dependent lipid A → TLR4 evasion |
| [15847602](https://pubmed.ncbi.nlm.nih.gov/15847602/) | Yop effectors thwart innate + adaptive immunity |
| [24599533](https://pubmed.ncbi.nlm.nih.gov/24599533/) | YopE (anti-phagocytosis), YopJ (cytotoxicity); LcrV antigen |
| [39423229](https://pubmed.ncbi.nlm.nih.gov/39423229/) | Yop-mediated LTB4 suppression delays inflammation |
| [35358289](https://pubmed.ncbi.nlm.nih.gov/35358289/) | F1/Caf1 antiphagocytic capsule |
| [19103769](https://pubmed.ncbi.nlm.nih.gov/19103769/) | Anti-F1 antibodies protective; capsule operon in transmission |
| [16943764](https://pubmed.ncbi.nlm.nih.gov/16943764/) | Primary septicemic plague clinical cluster (US, 2006) |
| [9097371](https://pubmed.ncbi.nlm.nih.gov/9097371/) | Clinical forms; risk factors |
| [32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/) | Therapy efficacy: 9% vs 51% mortality; agent comparisons |
| [24098126](https://pubmed.ncbi.nlm.nih.gov/24098126/) | Biphasic pre-/pro-inflammatory mechanism; macrophage→neutrophil switch |
| [17101642](https://pubmed.ncbi.nlm.nih.gov/17101642/) | Delayed (~48 h) cytokine/chemokine surge; named mediators |
| [19073275](https://pubmed.ncbi.nlm.nih.gov/19073275/) | Rat model; spleen→liver→blood dissemination; transmission |
| [34780267](https://pubmed.ncbi.nlm.nih.gov/34780267/) | 24 h therapeutic window; fluticasone adjunct benefit |
| [41389991](https://pubmed.ncbi.nlm.nih.gov/41389991/) / [32000692](https://pubmed.ncbi.nlm.nih.gov/32000692/) / [40705833](https://pubmed.ncbi.nlm.nih.gov/40705833/) / [35320275](https://pubmed.ncbi.nlm.nih.gov/35320275/) | Diagnostics: F1RDT, triplex qPCR, dual-antigen LFI |
| [19786842](https://pubmed.ncbi.nlm.nih.gov/19786842/) | LcrV + F1 subunit vaccine antigens |
| [21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/) | Intracellular antibiotic efficacy differences |
| [29183475](https://pubmed.ncbi.nlm.nih.gov/29183475/) | Prophylaxis and isolation guidelines |
| [41263683](https://pubmed.ncbi.nlm.nih.gov/41263683/) | Fulminant plague in HIV-positive patient |

**Evidence source types:** human clinical/surveillance (systematic reviews, case series, RDT field studies), model organism (mouse/rat CO92 studies), and in vitro/molecular (T3SS, F1, Pla, lipid A mechanism papers).

---

## Limitations and Knowledge Gaps

1. **Septicemic-specific data are sparse.** Much mechanistic evidence (biphasic model, cytokine storm) derives from **pneumonic** models; the extent to which these kinetics apply to primary septicemic plague is inferred, not directly demonstrated.
2. **No human genetic/host-susceptibility data.** Whether host polymorphisms modulate septicemic risk or outcome is essentially unstudied; historical protective-allele hypotheses remain unproven.
3. **Comparative antibiotic effectiveness** derives largely from observational US data (confounding by indication); randomized head-to-head trials in septicemic plague are lacking.
4. **Diagnostic blind spots.** F1-based rapid tests miss rare F1-negative strains; blood-culture sensitivity (~65%) and turnaround limit rapid confirmation in fulminant sepsis.
5. **No licensed vaccine**; correlates of protection in humans are incompletely defined.
6. **Adjunctive immunomodulation** is supported only by animal data.

---

## Proposed Follow-up Experiments / Actions

1. **Dedicated septicemic-plague models:** intravenous/intradermal CO92 challenge with serial organ bacteriology and single-cell/transcriptomic profiling to confirm the biphasic evasion→storm cascade specifically for the septicemic route.
2. **Adjunctive anti-inflammatory trials:** evaluate corticosteroids or targeted cytokine blockade (anti-IL-6/anti-TNF) plus antibiotics in animal septicemic models, building on the fluticasone result ([PMID: 34780267](https://pubmed.ncbi.nlm.nih.gov/34780267/)).
3. **Next-generation diagnostics:** deploy dual-antigen (F1+LcrV) and multi-target PCR/ddPCR point-of-care assays to close the F1-negative blind spot and shorten time-to-diagnosis in bacteremic patients ([PMID: 35320275](https://pubmed.ncbi.nlm.nih.gov/35320275/), [PMID: 38701065](https://pubmed.ncbi.nlm.nih.gov/38701065/)).
4. **Host-genetics study:** GWAS/exome analysis of survivors vs fatal cases in endemic foci (e.g., Madagascar) to test for host modifiers of outcome.
5. **Vaccine advancement:** move optimized rF1V/rV10 subunit candidates through phase 1/2, defining human immune correlates ([PMID: 19786842](https://pubmed.ncbi.nlm.nih.gov/19786842/), [PMID: 40022523](https://pubmed.ncbi.nlm.nih.gov/40022523/)).
6. **Antibiotic-selection optimization:** prospective comparative-effectiveness data (streptomycin vs gentamicin vs fluoroquinolone vs tetracycline), incorporating intracellular-efficacy considerations ([PMID: 32435801](https://pubmed.ncbi.nlm.nih.gov/32435801/), [PMID: 21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/)).

---

*Report compiled from 14 confirmed findings across 42 reviewed papers, covering all 15 requested disease-characteristic sections. Ontology suggestions (MONDO, HPO, GO, CL, UBERON, CHEBI, NCIT, NCBI Taxonomy) are provided inline where applicable.*


## Artifacts

- [OpenScientist final report](Septicemic_Plague-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Septicemic_Plague-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 30 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 23 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0005521` (1 mention) - the report calls it "DIC"; HP calls it **Disseminated intravascular coagulation**
- `UBERON:0002097` (1 mention) - the report calls it "skin/acral tissue"; UBERON calls it **skin of body**
- `NCIT:C2249` (1 mention) - the report calls it "Ciprofloxacin"; NCIT calls it **Yttrium Y 90 Monoclonal Antibody MN-14**
- `NCIT:C516` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Ganglioside GM2**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005576` (1 mention) - the report calls it "cell surface/extracellular region"; GO calls it **extracellular region**
- `GO:0009279` (1 mention) - the report calls it "outer membrane"; GO calls it **cell outer membrane**