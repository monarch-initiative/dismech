---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-17T16:19:06.099612'
end_time: '2026-09-17T17:04:26.586737'
duration_seconds: 2720.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy 2E
  mondo_id: MONDO:0030366
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
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0030366
    reported_labels:
    - MONDO
    ontology_label: cardiomyopathy, dilated, 2E
  - term_id: HP:0001644
    reported_labels:
    - Clinical sign (imaging)
    ontology_label: Dilated cardiomyopathy
  - term_id: HP:0001635
    reported_labels:
    - Clinical sign
    ontology_label: Congestive heart failure
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
  path: Cardiomyopathy_Dilated_2E-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cardiomyopathy_Dilated_2E-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 2E
- **MONDO ID:** MONDO:0030366 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 2E** covering all of the
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

# Dilated Cardiomyopathy 2E (CMD2E): A Comprehensive Disease Characterization

**Disease:** Dilated Cardiomyopathy 2E (CMD2E)
**MONDO ID:** MONDO:0030366 · **OMIM Phenotype:** #619492 · **Gene:** JPH2 (junctophilin-2)
**Category:** Mendelian (autosomal recessive)

---

## Summary

Dilated Cardiomyopathy 2E (**CMD2E**; OMIM #619492, MONDO:0030366) is a rare, autosomal **recessive**, non-syndromic form of dilated cardiomyopathy caused by **biallelic loss-of-function (LOF) mutations in *JPH2***, the gene encoding **junctophilin-2** (chromosome 20q13.12; OMIM *605267; HGNC:14179; UniProt Q9BR39). The disease was established by two independent recessive kindreds: a Finnish family with a homozygous nonsense variant **p.Q428X (c.1282C>T)** in which the proband was diagnosed at age 3 and transplanted at age 4 ([PMID: 30384889](https://pubmed.ncbi.nlm.nih.gov/30384889/)), and consanguineous Iranian families sharing a founder haplotype carrying a homozygous 1-bp insertion **p.E641\* (c.1920dupT)** with neonatal DCM and childhood death ([PMID: 31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/)).

The mechanistic core of the disease is the **cardiac dyad**. Junctophilin-2 physically tethers the T-tubule sarcolemma to the junctional sarcoplasmic reticulum (jSR), maintaining the ~12–15 nm dyadic cleft that positions L-type Ca²⁺ channels (CACNA1C/LTCC) opposite ryanodine receptors (RyR2) so that calcium-induced calcium release (CICR) can drive contraction. When both *JPH2* alleles are lost, the dyad cannot assemble, excitation–contraction (EC) coupling fails, and the ventricle dilates with progressively impaired systolic function. This is corroborated by mouse genetics: germline *Jph2*-null embryos die immediately after the heart begins to beat, with deficient junctional membrane complexes and asynchronous Ca²⁺ transients ([PMID: 10949023](https://pubmed.ncbi.nlm.nih.gov/10949023/)), while cardiac-specific knockdown produces contractile failure and heart failure ([PMID: 21339484](https://pubmed.ncbi.nlm.nih.gov/21339484/)).

Clinically, CMD2E presents in the **neonatal period or early childhood** with rapidly progressive systolic heart failure, frequently requiring mechanical circulatory support or **heart transplantation**. There is **no CMD2E-specific approved therapy**; management follows standard guideline-directed pediatric heart-failure care, with **AAV9-mediated JPH2 gene replacement** as a strong preclinical rationale ([PMID: 27760414](https://pubmed.ncbi.nlm.nih.gov/27760414/)). CMD2E is mechanistically and genetically distinct from the *dominant* JPH2 **missense** hypertrophic cardiomyopathy (CMH17), which acts through altered RyR2 regulation rather than protein loss.

---

## 1. Disease Information

**Overview.** CMD2E is a Mendelian, gene-defined subtype of dilated cardiomyopathy (DCM). DCM is characterized by left ventricular (or biventricular) dilation and systolic dysfunction not explained by abnormal loading conditions or coronary disease. CMD2E is the specific entity attributable to biallelic *JPH2* loss-of-function.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #619492 (CARDIOMYOPATHY, DILATED, 2E; CMD2E) |
| OMIM (gene) | *605267 (JPH2) |
| MONDO | MONDO:0030366 |
| HGNC | HGNC:14179 (JPH2) |
| NCBI Gene | 57158 |
| Ensembl | ENSG00000149596 |
| UniProt | Q9BR39 |
| Cytoband | 20q13.12 (GRCh38 chr20:44,106,590–44,187,188) |
| ICD-10 (parent DCM) | I42.0 |
| ICD-11 (parent DCM) | BC43.0 |
| MeSH (parent DCM) | D002311 |
| Orphanet | Under familial isolated DCM (ORPHA:154) |

**Synonyms / alternative names.** "Dilated cardiomyopathy 2E"; "CMD2E"; "JPH2-related dilated cardiomyopathy"; "junctophilin-2-related recessive dilated cardiomyopathy." Note that "CMD2E" (with numeric-letter suffix) denotes the OMIM molecular-genetic subtype and should not be confused with dominant JPH2 disease.

**Information source type.** Evidence is derived from **aggregated disease-level resources** (OMIM, MONDO, gnomAD) combined with **individual-patient case reports and small kindreds** (two founding families plus subsequent case reports), and from **model-organism and in vitro** mechanistic studies. There is no large EHR-derived cohort specific to CMD2E owing to its rarity.

---

## 2. Etiology

**Primary cause — genetic.** CMD2E is caused by **homozygous or compound heterozygous loss-of-function variants in *JPH2***. Two independent recessive kindreds established causality (Finding F001):

- **p.Q428X (c.1282C>T)**, homozygous nonsense, Finnish family — proband diagnosed at age 3, transplanted at age 4 ([PMID: 30384889](https://pubmed.ncbi.nlm.nih.gov/30384889/)). The paper identifies JPH2 among calcium-signaling genes in a severe childhood cardiomyopathy cohort: *"calcium signaling (JPH2, CALM1, CACNA1C)."*
- **p.E641\* (c.1920dupT)**, homozygous 1-bp insertion creating a premature stop, consanguineous Iranian families on a shared founder haplotype ([PMID: 31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/)): *"identified an Iranian patient with dilated cardiomyopathy (DCM) as a carrier of a novel, homozygous single nucleotide insertion in JPH2 resulting in a stop codon (JPH2-p.E641\*)."*

**Genetic risk factors.** The obligate risk factor is inheritance of **two** LOF *JPH2* alleles. **Consanguinity** and **founder effects** substantially elevate risk (the Iranian p.E641\* variant on a shared haplotype). Heterozygous carriers are asymptomatic (see §9), consistent with a recessive mechanism.

**Environmental risk factors.** No specific environmental trigger is established as causal for CMD2E; the disease is monogenic. General DCM environmental modifiers (viral myocarditis, toxins, alcohol) are not implicated in the biallelic-JPH2 entity, though they could theoretically aggravate any myocardial reserve deficit.

**Protective factors.** No genetic or environmental protective factors are specifically documented for CMD2E. By inference, retention of even one functional *JPH2* allele is "protective" (carriers are unaffected), reflecting haplosufficiency.

**Gene–environment interactions.** None specifically documented. The dominant driver is genotype (biallelic LOF); environmental contribution appears minimal relative to the primary lesion.

---

## 3. Phenotypes

CMD2E presents with the core phenotype of **dilated cardiomyopathy**: left ventricular dilation and impaired systolic function (reduced ejection fraction) producing **congestive heart failure**, with **arrhythmia risk** and risk of **premature death** (Finding F006). Progression is **rapid**, frequently to transplant-dependent end-stage failure.

| Phenotype | Type | HPO term (suggested) | Onset | Severity / progression | Frequency |
|---|---|---|---|---|---|
| Dilated cardiomyopathy | Clinical sign (imaging) | HP:0001644 | Neonatal–early childhood | Severe, progressive | Defining (all patients) |
| Left ventricular systolic dysfunction / reduced EF | Laboratory/imaging abnormality | HP:0005162 / HP:0012664 | Neonatal–early childhood | Severe, progressive | Very frequent |
| Congestive heart failure | Clinical sign | HP:0001635 | Neonatal–early childhood | Severe | Very frequent |
| Ventricular arrhythmia / arrhythmia | Clinical sign | HP:0004308 / HP:0011675 | Childhood | Variable | Reported risk |
| Sudden cardiac death / premature death | Outcome | HP:0001645 / HP:0001663 | Childhood | — | Reported |

**Phenotype characteristics.** *Age of onset:* neonatal to early childhood (congenital/pediatric). *Severity:* severe. *Progression:* rapid and progressive. *Frequency:* the DCM/systolic-failure phenotype is fully penetrant in reported biallelic patients. Supporting quote ([PMID: 31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/)): *"A second Iranian family with consanguineous parents hosting an identical heterozygous variant had 2 children die in childhood from cardiac failure."*

**Quality-of-life impact.** Not formally measured with standardized instruments (EQ-5D/SF-36/PROMIS) in this rare disease, but the burden is profound: infants/children experience heart-failure symptoms (feeding difficulty, failure to thrive, dyspnea, exercise intolerance), hospitalization, need for mechanical support, and transplantation with lifelong immunosuppression.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***JPH2*** — junctophilin-2 (OMIM *605267; HGNC:14179; NCBI Gene 57158; Ensembl ENSG00000149596; UniProt Q9BR39; 20q13.12). Finding F007 verified these identifiers via mygene.info.

**Pathogenic variants (CMD2E, recessive).**

| Variant (protein) | cDNA | Type | Zygosity | Population | Reference |
|---|---|---|---|---|---|
| p.Q428X | c.1282C>T | Nonsense (LOF) | Homozygous | Finnish | [PMID: 30384889](https://pubmed.ncbi.nlm.nih.gov/30384889/) |
| p.E641\* | c.1920dupT | Frameshift/stop-gain (LOF) | Homozygous (founder) | Iranian / Greater Middle East | [PMID: 31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/) |

**Variant classification.** Both founding variants are truncating **loss-of-function** alleles (nonsense / frameshift-stopgain) and are consistent with **Pathogenic** classification under ACMG/AMP (null variant in a gene where LOF is a known disease mechanism, segregation, rarity/absence in controls). Additional recessive frameshift cases have subsequently been reported in pediatric DCM (e.g., [PMID: 41919412](https://pubmed.ncbi.nlm.nih.gov/41919412/)).

**Variant type/class.** Truncating (nonsense, frameshift → premature termination codon); predicted to trigger nonsense-mediated decay or produce truncated non-functional protein → **loss of function**.

**Allele frequency (population databases).** gnomAD constraint for *JPH2* (Finding F004): **pLI ≈ 3.9×10⁻⁹**, **LOEUF (oe_lof upper) = 0.89**, observed/expected LOF = **38/55.9 (oe_lof 0.68)** — i.e., heterozygous LOF is **tolerated**, consistent with unaffected carriers and a recessive disease requiring biallelic loss. LOF variants are rare overall (0.04%) but enriched in Greater Middle Eastern (GME) individuals (0.21%) ([PMID: 31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/)): *"Worldwide, 1.45% of healthy individuals hosted a rare JPH2 variant with a significantly higher proportion among GME individuals (4.45%); LOF variants were rare overall (0.04%) yet were most prevalent in GME (0.21%)."*

**Somatic vs germline.** **Germline** (inherited). No somatic mechanism is relevant.

**Functional consequences.** **Loss of function** (haploinsufficiency is tolerated; biallelic loss is pathogenic). This contrasts sharply with the *dominant missense* JPH2 variants causing hypertrophic cardiomyopathy/arrhythmia (e.g., A405S — [PMID: 28393127](https://pubmed.ncbi.nlm.nih.gov/28393127/); E169K causing atrial fibrillation via impaired RyR2 stabilization — [PMID: 23973696](https://pubmed.ncbi.nlm.nih.gov/23973696/)), which act by altered/reduced RyR2 regulation rather than complete protein loss.

**Modifier genes.** None specifically established for CMD2E. Other calcium-handling/dyadic genes (RYR2, CACNA1C, CALM1, BIN1, CMYA5) are biologically plausible modifiers but unproven in this disorder.

**Epigenetic information / chromosomal abnormalities.** No disease-specific DNA-methylation, histone-modification, or large-scale chromosomal abnormality (aneuploidy/translocation) is documented for CMD2E. The disease is a small-scale sequence (point/indel) disorder.

---

## 5. Environmental Information

CMD2E is a **monogenic recessive** disorder; **no environmental, lifestyle, or infectious agents are established as causal**. Unlike acquired DCM (viral myocarditis, alcohol, chemotherapy toxins), the biallelic-JPH2 entity arises from the genetic lesion. Consanguinity is the principal non-molecular contributor to disease occurrence at the population level, by increasing the probability of biallelic inheritance of rare founder LOF alleles (§9). Environmental cardiac stressors are, at most, plausible aggravators of already-compromised myocardial reserve, not initiators.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *JPH2* loss-of-function mutation** (e.g., p.Q428X, p.E641\*) **leads to** absence/severe reduction of functional junctophilin-2 protein in cardiomyocytes (loss of function; both alleles null).
2. Loss of junctophilin-2 **results in** failure to tether the T-tubule sarcolemma to the junctional sarcoplasmic reticulum, so the **cardiac dyad / junctional membrane complex cannot assemble or be maintained** (the ~12–15 nm dyadic cleft is lost or disordered). *Demonstrated* in mouse *Jph2*-null myocytes ([PMID: 10949023](https://pubmed.ncbi.nlm.nih.gov/10949023/)).
3. Without an intact dyad, **L-type Ca²⁺ channels (CACNA1C/LTCC) are no longer recruited to and juxtaposed with RyR2** — the JPH2 "joining region" that directly binds the LTCC α1C subunit is lost ([PMID: 33092464](https://pubmed.ncbi.nlm.nih.gov/33092464/)), which **leads to** loss of the tight spatial coupling required for CICR.
4. Disrupted LTCC–RyR2 coupling **results in** impaired/asynchronous **calcium-induced calcium release** and reduced EC-coupling gain — abnormal, spatially and temporally desynchronized Ca²⁺ transients (*demonstrated* in null and knockdown myocytes; [PMID: 10949023](https://pubmed.ncbi.nlm.nih.gov/10949023/), [PMID: 21339484](https://pubmed.ncbi.nlm.nih.gov/21339484/)).
5. Deficient Ca²⁺ transients **lead to** reduced cardiomyocyte contractility (weak systole).
6. Chronic contractile insufficiency **results in** **ventricular dilation and systolic heart failure** (the DCM phenotype) — *inferred* progression from cellular to organ level, supported by cardiac-knockdown mice developing heart failure ([PMID: 21339484](https://pubmed.ncbi.nlm.nih.gov/21339484/)).
7. Ventricular remodeling and abnormal Ca²⁺ handling **lead to** **arrhythmia risk and premature death** (*inferred* from clinical course and RyR2 dysregulation literature).

**Branch (stress-adaptive signaling).** In parallel with structural loss, proteolytic cleavage of JPH2 (by calpain, [PMID: 30409805](https://pubmed.ncbi.nlm.nih.gov/30409805/); by MMP-2, [PMID: 31506724](https://pubmed.ncbi.nlm.nih.gov/31506724/)) generates an N-terminal fragment (JP2NT) that translocates to the nucleus as a **stress-adaptive transcriptional regulator**. This branch is most relevant to acquired heart failure, but it underscores that JPH2 has both a **structural** (dyad-tethering) and a **signaling** role; in CMD2E, complete germline loss abolishes both. Supporting quote ([PMID: 30409805](https://pubmed.ncbi.nlm.nih.gov/30409805/)): *"After cardiac stress, JP2 is cleaved by the calcium ion-dependent protease calpain, which disrupts the E-C coupling ultrastructural machinery and drives heart failure progression."*

### Category detail

- **Molecular pathways.** Cardiac **excitation–contraction coupling** and **calcium-induced calcium release** (CICR) at the dyad; LTCC (CACNA1C) → RyR2 signaling axis. GO biological processes: **GO:0006942** (regulation of striated muscle contraction), **GO:0055117** (regulation of cardiac muscle contraction), **GO:0010881** (regulation of cardiac muscle contraction by regulation of the release of sequestered calcium ion), **GO:0051209** (release of sequestered calcium ion into cytosol). Supporting quote ([PMID: 33092464](https://pubmed.ncbi.nlm.nih.gov/33092464/)): *"The interaction between LTCC and the joining region in JPH2 facilitates dyad assembly and maintains normal CICR in cardiomyocytes."*
- **Cellular processes.** Impaired myocyte contraction; disrupted junctional membrane complex biogenesis; abnormal intracellular Ca²⁺ homeostasis. In the acquired/proteolysis branch: stress-adaptive transcriptional reprogramming.
- **Protein dysfunction.** Loss of function — truncated/absent junctophilin-2; loss of the membrane-tethering MORN motifs and the LTCC-binding "joining region."
- **Metabolic changes.** No primary metabolic defect; secondary bioenergetic strain accompanies heart failure (not specific to CMD2E).
- **Immune involvement.** Not a primary feature; CMD2E is not autoimmune/inflammatory in origin.
- **Tissue-damage mechanisms.** Progressive myocardial dysfunction and dilation; interstitial/collagen remodeling accompanies advanced failure (t-tubule/dyad disorganization associated with collagen deposition in failing human myocardium — [PMID: 34690801](https://pubmed.ncbi.nlm.nih.gov/34690801/)).
- **Biochemical abnormality.** Defective calcium-channel coupling (LTCC–RyR2 microdomain failure) — an ion-handling/microdomain defect rather than an enzyme deficiency.
- **Cell types & GO cellular components.** Cell type: **ventricular cardiac muscle cell (CL:0002131)** / cardiac muscle cell (CL:0000746). Cellular components: **cardiac dyad**, **T-tubule (GO:0033268 / GO:0014801)**, **junctional sarcoplasmic reticulum membrane (GO:0014701)** / sarcoplasmic reticulum (GO:0016529), **Z-disc (GO:0030018)**.

### Mechanistic schematic

```
Biallelic JPH2 LOF (p.Q428X / p.E641*)
        │  (loss of function)
        ▼
No functional junctophilin-2
        │  (cannot tether T-tubule ↔ jSR)
        ▼
Dyad / junctional membrane complex fails to form
        │  (LTCC not recruited opposite RyR2)
        ▼
LTCC (CACNA1C) — RyR2 coupling lost
        │
        ▼
Impaired calcium-induced calcium release
(asynchronous, low-gain Ca2+ transients)
        │
        ▼
Reduced cardiomyocyte contractility
        │
        ▼
LV dilation + systolic heart failure (DCM)  ──► arrhythmia / premature death
```

---

## 7. Anatomical Structures Affected

- **Organ level (primary).** **Heart (UBERON:0000948)**, specifically the **ventricular myocardium / cardiac ventricle (UBERON:0002349 / UBERON:0002082)**; left ventricle predominant with possible biventricular involvement. **Body system:** cardiovascular.
- **Secondary organ involvement.** Downstream congestive effects of heart failure (pulmonary congestion, hepatic congestion, systemic hypoperfusion) — complications rather than primary sites.
- **Tissue/cell level.** **Cardiac (striated) muscle tissue**; **ventricular cardiac muscle cells / cardiomyocytes (CL:0002131 / CL:0000746)**.
- **Subcellular level.** The **cardiac dyad** — the junction of **T-tubule (GO:0033268)** and **junctional sarcoplasmic reticulum (GO:0014701 / GO:0016529)**; the **Z-disc (GO:0030018)**; sarcolemma–SR contact microdomain.
- **Localization / lateralization.** Bilateral/global ventricular process (not lateralized); a diffuse cardiomyocyte-autonomous defect rather than a focal lesion.

---

## 8. Temporal Development

- **Onset.** **Neonatal to early-childhood** (congenital/pediatric). Onset pattern is early and can be insidious to subacute, progressing to overt decompensated heart failure. In the founding kindreds, the Finnish proband was diagnosed at age 3 ([PMID: 30384889](https://pubmed.ncbi.nlm.nih.gov/30384889/)) and Iranian children died in childhood from cardiac failure ([PMID: 31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/)).
- **Progression.** **Rapid and progressive**, advancing to **end-stage** systolic failure. Disease course is progressive (not relapsing-remitting), typically culminating in transplant dependence within a few years of diagnosis (Finnish proband transplanted at age 4).
- **Duration.** Chronic and lifelong from a genetic standpoint; without transplantation the natural course is early fatal.
- **Patterns / remission.** No spontaneous remission is expected; "remission" is achieved only via transplantation (replacement of the affected organ). Critical intervention window is early — before irreversible ventricular remodeling and end-organ compromise.

---

## 9. Inheritance and Population

**Inheritance pattern.** **Autosomal recessive** (biallelic LOF required). Established by homozygous variants segregating with disease in two independent consanguineous/founder kindreds (Finding F001).

**Penetrance / expressivity.** In reported **biallelic** individuals, penetrance of the DCM/heart-failure phenotype appears **complete/high**; **heterozygous carriers are unaffected**. Expressivity within biallelic patients is severe with early onset; the small number of families limits precise estimates.

**Carrier frequency & founder effects.** gnomAD shows *JPH2* tolerates heterozygous LOF (LOEUF 0.89; oe_lof 0.68), consistent with silent carriers (Finding F004). Worldwide ~**1.45%** of healthy individuals carry a rare *JPH2* variant, rising to **4.45%** in GME populations; LOF alleles are rare (0.04%) but most prevalent in GME (0.21%) ([PMID: 31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/)). The Iranian **p.E641\*** allele arose on a shared **founder haplotype**.

**Consanguinity.** A major contributor — recessive disease manifests when consanguineous unions bring together two copies of a rare founder LOF allele.

**Anticipation / mosaicism.** No evidence of genetic anticipation (not a repeat-expansion disorder). Germline mosaicism not specifically reported.

**Epidemiology.** CMD2E is **very rare** (an ultra-rare Mendelian subtype of DCM); precise prevalence/incidence figures are not established given the small number of reported families. It falls under the Orphanet umbrella of familial isolated DCM (ORPHA:154). Enrichment is expected in **consanguineous populations, particularly the Greater Middle East**.

**Demographics.** No strong sex bias is established (recessive, autosomal). Affected individuals are infants/children. Geographic clustering follows founder/consanguinity patterns (e.g., Iranian founder for p.E641\*).

---

## 10. Diagnostics

**Clinical/imaging.** Diagnosis of the DCM phenotype rests on **echocardiography** (LV dilation, reduced ejection fraction) and **cardiac MRI** (chamber dimensions, systolic function, fibrosis on late gadolinium enhancement). **ECG** and Holter monitoring assess arrhythmia/conduction. **Biomarkers**: elevated **BNP/NT-proBNP** (heart-failure severity); **troponin** may be monitored. Endomyocardial biopsy is not required for diagnosis but would show non-specific myocyte changes/remodeling.

**Genetic testing (definitive for CMD2E).** Because CMD2E is defined molecularly, **genetic testing is the confirmatory diagnostic**:
- **Cardiomyopathy/DCM multigene NGS panels** including *JPH2* are first-line.
- **Whole-exome (WES)** or **whole-genome sequencing (WGS)** is highly useful, especially for early-onset/consanguineous pediatric DCM where recessive genes are implicated; the founding CMD2E variants were identified via broad sequencing in severe childhood cardiomyopathy cohorts ([PMID: 30384889](https://pubmed.ncbi.nlm.nih.gov/30384889/)).
- **Confirming biallelic status** (homozygous vs compound heterozygous, with parental segregation) is essential to distinguish recessive CMD2E from incidental heterozygous carriage.
- Chromosomal microarray/karyotype/FISH/mtDNA/repeat-expansion testing are **not** indicated for this small-scale sequence disorder.

**Clinical criteria & differential diagnosis.** Standard DCM diagnostic criteria (dilation + systolic dysfunction not explained by loading/coronary disease). **Differential:** other genetic pediatric DCM (e.g., TTN, LMNA, FLNC, DES, DSP, TNNT2), syndromic/oligogenic DCM ([PMID: 42559185](https://pubmed.ncbi.nlm.nih.gov/42559185/)), metabolic/mitochondrial cardiomyopathies, myocarditis, and — importantly — **dominant JPH2 hypertrophic cardiomyopathy (CMH17)**, which is phenotypically hypertrophic (not dilated) and mechanistically distinct.

**Screening.** For affected families: **cascade genetic testing** of relatives to identify carriers and at-risk future offspring; **carrier screening** in consanguineous couples with a founder allele; prenatal/preimplantation testing where a familial biallelic risk exists.

---

## 11. Outcome / Prognosis

**Survival/mortality.** Prognosis is **poor without transplantation**: both founding kindreds illustrate early end-stage disease — transplantation at age 4 in the Finnish proband ([PMID: 30384889](https://pubmed.ncbi.nlm.nih.gov/30384889/)) and childhood death from cardiac failure in Iranian children ([PMID: 31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/)). With modern pediatric heart-failure care, outcomes for end-stage DCM are favorable: registry data show adolescents with DCM have excellent 3-year survival with either a HeartMate 3 VAD (**94.4%**) or transplant (**95.6%**) ([PMID: 42334151](https://pubmed.ncbi.nlm.nih.gov/42334151/)): *"Adolescents with DCM treated with either HM3 or transplant had excellent 3-year outcomes."*

**Morbidity/function.** High morbidity from heart failure (hospitalizations, activity limitation, feeding/growth impairment in infants), device-related complications in those on mechanical support, and lifelong immunosuppression after transplant.

**Complications.** Progressive systolic failure, ventricular arrhythmia, thromboembolism, end-organ hypoperfusion, and sequelae of mechanical support/transplant.

**Prognostic factors.** Age/severity at presentation, degree of ventricular dysfunction, arrhythmia burden, and response to guideline-directed therapy. Recovery of native ventricular function is not expected given the fixed genetic dyadic defect; definitive treatment is organ replacement (or, prospectively, gene replacement).

---

## 12. Treatment

**No CMD2E-specific approved therapy exists** (Finding F005). Management is **standard pediatric dilated-cardiomyopathy / heart-failure care**:

- **Pharmacotherapy (guideline-directed medical therapy).** ACE inhibitors / ARBs, **beta-blockers**, **mineralocorticoid-receptor antagonists**, **diuretics**; contemporary HFrEF agents as age-appropriate. (Suggested NCIT concept classes: *Angiotensin-Converting Enzyme Inhibitor*, *Beta-Adrenergic Blocker*, *Diuretic*, *Aldosterone Antagonist*.)
- **Mechanical circulatory support.** **Ventricular assist devices** (e.g., HeartMate 3) as bridge-to-transplant or longer-term support; pediatric VAD outcomes are well documented ([PMID: 42622114](https://pubmed.ncbi.nlm.nih.gov/42622114/), [PMID: 42334151](https://pubmed.ncbi.nlm.nih.gov/42334151/)). (NCIT: *Ventricular Assist Device*.)
- **Orthotopic heart transplantation.** The definitive treatment for end-stage disease; the Finnish proband was transplanted at age 4. (NCIT: *Heart Transplantation*.)
- **Device therapy / arrhythmia management** as indicated (ICD for high arrhythmic risk).

**Targeted / advanced therapeutics (investigational rationale).** Because CMD2E is a **loss-of-function** disorder, **gene replacement** is the mechanistically ideal strategy. **AAV9-mediated JPH2 overexpression rescued cardiac contractility, preserved T-tubule structure, and normalized RyR2-mediated Ca²⁺ release** in a mouse (transverse aortic constriction) heart-failure model ([PMID: 27760414](https://pubmed.ncbi.nlm.nih.gov/27760414/)): *"AAV9-mediated expression of JPH2 rescued cardiac contractility in mice subjected to TAC. AAV9-JPH2 also preserved T-tubule structure."* This provides a strong preclinical rationale for **AAV9-JPH2 gene therapy** in CMD2E, though no human trial yet exists.

**Pharmacogenomics.** No gene-specific pharmacogenomic guidance is established for CMD2E.

**Treatment outcomes.** Supportive/GDMT slows progression but does not correct the primary defect; end-stage disease is managed with VAD/transplant, with excellent short-to-medium-term survival in modern pediatric practice ([PMID: 42334151](https://pubmed.ncbi.nlm.nih.gov/42334151/)).

---

## 13. Prevention

- **Primary prevention.** No population-level primary prevention (monogenic disease). The principal lever is **reproductive genetic counseling** in families/populations carrying founder LOF alleles — particularly reducing recessive risk in consanguineous unions.
- **Secondary prevention.** **Cascade genetic screening** of relatives of probands to identify carriers and at-risk offspring; early echocardiographic surveillance in genetically at-risk children enables timely heart-failure therapy.
- **Tertiary prevention.** Optimizing GDMT, arrhythmia risk management, and timely VAD/transplant to prevent complications and death in affected individuals.
- **Genetic counseling & reproductive options.** For couples both carrying a *JPH2* LOF allele, recurrence risk is 25% per pregnancy; **preimplantation genetic testing** and **prenatal diagnosis** are options. Carrier screening is especially relevant in Greater Middle Eastern / consanguineous populations given founder enrichment ([PMID: 31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/)).
- **Immunization / public health / prophylaxis.** Not applicable (non-infectious, monogenic).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs (Finding F007).** *JPH2* is conserved across vertebrates: **mouse *Jph2*** (NCBI Gene 59091; Ensembl ENSMUSG00000017817; UniProt Q9ET78), **zebrafish *jph2*** (NCBI Gene 553333; Ensembl ENSDARG00000028625). The essential role in cardiac dyad/EC-coupling formation is conserved.
- **Natural disease in other species.** No well-characterized naturally occurring biallelic-JPH2 dilated cardiomyopathy is documented in companion animals or wildlife in the reviewed literature; disease knowledge derives from engineered models (§15).
- **Comparative biology / evolutionary conservation.** The dyad is an evolutionarily conserved cardiomyocyte structure, and junctophilin's tethering function is conserved, making cross-species models highly informative. (For background on dyad evolution, see [PMID: 36189805](https://pubmed.ncbi.nlm.nih.gov/36189805/).)
- **Zoonotic potential.** Not applicable.

---

## 15. Model Organisms

CMD2E biology is strongly supported by mouse genetics (Finding F003):

| Model | Manipulation | Key phenotype | Reference |
|---|---|---|---|
| Germline *Jph2*-null mouse | Global knockout | **Embryonic lethal** immediately after heartbeat onset; deficient junctional membrane complexes; abnormal, asynchronous Ca²⁺ transients | [PMID: 10949023](https://pubmed.ncbi.nlm.nih.gov/10949023/); [PMID: 12086916](https://pubmed.ncbi.nlm.nih.gov/12086916/) |
| Cardiac-specific shRNA JPH2 knockdown | Partial (postnatal) loss | Impaired contractility, fewer junctional membrane complexes, increased plasmalemma–SR distance variability, reduced EC-coupling gain, **heart failure and increased mortality** | [PMID: 21339484](https://pubmed.ncbi.nlm.nih.gov/21339484/) |
| AAV9-JPH2 gene delivery (TAC HF model) | Overexpression/rescue | Rescued contractility, preserved T-tubules, normalized RyR2-mediated Ca²⁺ release | [PMID: 27760414](https://pubmed.ncbi.nlm.nih.gov/27760414/) |

**Model types available.** Mammalian (mouse) knockout, cardiac-specific knockdown, and AAV-based rescue; zebrafish orthologs enable developmental modeling. iPSC-derived cardiomyocytes from patients are a logical (in vitro) system to model biallelic human variants.

**Phenotype recapitulation.** Mouse models faithfully recapitulate the **core mechanism** — dyad loss, EC-coupling failure, abnormal Ca²⁺ handling, and contractile/heart failure — validating the human causal chain. Supporting quotes: *"JP-2 is abundantly expressed in the heart, and mutant mice lacking JP-2 exhibited embryonic lethality. Cardiac myocytes from the mutant mice showed deficiency of the junctional membrane complexes and abnormal Ca2+ transients"* ([PMID: 10949023](https://pubmed.ncbi.nlm.nih.gov/10949023/)); *"Cardiac-specific JPH2 knockdown resulted in impaired cardiac contractility, which caused heart failure and increased mortality"* ([PMID: 21339484](https://pubmed.ncbi.nlm.nih.gov/21339484/)).

**Model limitations.** Germline null is embryonic-lethal, so it cannot model the postnatal human course; knockdown produces partial rather than complete loss; TAC models pressure-overload HF rather than the primary congenital dyadic deficit. A conditional/humanized biallelic-LOF model or patient iPSC-cardiomyocytes would better capture the human CMD2E trajectory.

---

## Mechanistic Model / Interpretation

CMD2E is best understood as a **structural dyadopathy of the cardiomyocyte**. Junctophilin-2 is the molecular "staple" that holds the T-tubule sarcolemma against the junctional SR; its "joining region" additionally recruits L-type Ca²⁺ channels into the dyad opposite RyR2. Removing both alleles removes the staple, the dyad cannot form, and the exquisitely spatially-organized CICR that powers every heartbeat becomes weak and asynchronous. Because contractility depends on this microdomain, the ventricle cannot generate adequate force, dilates, and fails.

The genetics reinforce the mechanism: heterozygous LOF is tolerated (gnomAD LOEUF 0.89; unaffected carriers), so **one functional allele suffices** — the disease is unmasked only by biallelic loss, explaining its recessive inheritance and enrichment in consanguineous/founder settings. This is the mirror image of dominant JPH2 **missense** disease (HCM/AF; [PMID: 28393127](https://pubmed.ncbi.nlm.nih.gov/28393127/), [PMID: 23973696](https://pubmed.ncbi.nlm.nih.gov/23973696/)), where a mutant protein perturbs RyR2 regulation in a dose-dependent, dominant manner. The dichotomy — *dominant missense → hypertrophic/arrhythmic* vs *recessive null → dilated/failing* — is a clean genotype–mechanism–phenotype correspondence.

The therapeutic corollary follows directly: a loss-of-function disease is the archetypal target for **gene replacement**, and AAV9-JPH2 rescue in mice ([PMID: 27760414](https://pubmed.ncbi.nlm.nih.gov/27760414/)) shows that restoring the protein restores dyad structure and Ca²⁺ handling. Until such therapy is available for humans, the clinical pathway is heart-failure GDMT → mechanical support → transplant, for which contemporary pediatric outcomes are strong ([PMID: 42334151](https://pubmed.ncbi.nlm.nih.gov/42334151/)).

---

## Evidence Base

| PMID | Role | How it supports the findings |
|---|---|---|
| [30384889](https://pubmed.ncbi.nlm.nih.gov/30384889/) | Gene discovery | Identifies JPH2 (homozygous Q428X) in severe childhood cardiomyopathy; establishes CMD2E gene (F001) |
| [31227780](https://pubmed.ncbi.nlm.nih.gov/31227780/) | Gene confirmation + population genetics | Homozygous p.E641\* recessive DCM; GME carrier/LOF frequencies; founder effect (F001, F004, F006) |
| [33092464](https://pubmed.ncbi.nlm.nih.gov/33092464/) | Mechanism | JPH2 joining region binds LTCC to assemble dyad and maintain CICR (F002) |
| [30409805](https://pubmed.ncbi.nlm.nih.gov/30409805/) | Mechanism (proteolysis/signaling) | Calpain cleavage disrupts EC-coupling; JP2NT transcription regulator branch (F002) |
| [31506724](https://pubmed.ncbi.nlm.nih.gov/31506724/) | Mechanism (proteolysis) | MMP-2 cleaves JPH2, damages dyads in ischemia-reperfusion (F002) |
| [10949023](https://pubmed.ncbi.nlm.nih.gov/10949023/) | Model organism | Germline Jph2-null: embryonic lethal, deficient junctional complexes, abnormal Ca²⁺ (F003) |
| [12086916](https://pubmed.ncbi.nlm.nih.gov/12086916/) | Model organism | JP-2 and RyR2 knockouts lethal at heartbeat onset; dyad essential for Ca²⁺ homeostasis (F003) |
| [21339484](https://pubmed.ncbi.nlm.nih.gov/21339484/) | Model organism | Cardiac JPH2 knockdown → contractile failure, heart failure, mortality (F003) |
| [27760414](https://pubmed.ncbi.nlm.nih.gov/27760414/) | Therapeutic rationale | AAV9-JPH2 rescues contractility, T-tubules, RyR2 Ca²⁺ release (F005) |
| [42334151](https://pubmed.ncbi.nlm.nih.gov/42334151/) | Clinical management | Excellent 3-yr survival with VAD/transplant in adolescent DCM (F005) |
| [28393127](https://pubmed.ncbi.nlm.nih.gov/28393127/) | Contrast (dominant) | JPH2 A405S dominant HCM — distinguishes from recessive CMD2E |
| [23973696](https://pubmed.ncbi.nlm.nih.gov/23973696/) | Contrast (dominant) | JPH2 E169K AF via impaired RyR2 stabilization — dominant mechanism |
| [34690801](https://pubmed.ncbi.nlm.nih.gov/34690801/) | Human failing heart | RyR2/JPH2 nanoscale disorganization and collagen in failing myocardium |

---

## Limitations and Knowledge Gaps

1. **Very small human evidence base.** CMD2E rests on a handful of families (Finnish Q428X; Iranian founder E641\*; subsequent case reports). Prevalence, incidence, precise penetrance, sex ratio, and natural-history statistics are therefore not robustly quantified.
2. **No standardized QoL or registry data** specific to CMD2E; morbidity/QoL is inferred from general pediatric DCM.
3. **Mechanism largely extrapolated from models and dominant-disease studies.** Direct functional validation of the specific recessive human LOF variants (e.g., patient iPSC-cardiomyocytes) is limited; the causal chain steps 6–7 (cell → organ; arrhythmia/death) are inferred.
4. **No human gene-therapy data.** AAV9-JPH2 rescue is preclinical (mouse pressure-overload HF), not tested in congenital biallelic-LOF disease or in humans.
5. **Modifier genes, epigenetics, and environmental interactions** are essentially uncharacterized for CMD2E.
6. **Ontology mappings** for the specific CMD2E entity (e.g., exact Orphanet subtype, ICD-11 extension code) are approximate; identifiers here reflect the parent DCM class where a subtype-specific code is unavailable.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived iPSC-cardiomyocyte modeling** of p.Q428X and p.E641\* (and isogenic corrected controls) to directly quantify dyad density, LTCC–RyR2 colocalization (dSTORM), Ca²⁺-transient synchrony, and contractility — closing the inference gap between genotype and cellular phenotype.
2. **Conditional / humanized biallelic-LOF mouse** (bypassing embryonic lethality) to establish a postnatal CMD2E model recapitulating the human dilated, progressive course.
3. **Preclinical AAV9-JPH2 gene-replacement trial** in a biallelic-LOF model, with dose-finding and durability endpoints, to advance the rational targeted therapy toward first-in-human studies.
4. **International registry / GeneMatcher-style aggregation** of biallelic *JPH2* DCM cases to define prevalence, penetrance, natural history, and genotype–phenotype correlations.
5. **Targeted carrier screening** for *JPH2* LOF founder alleles in Greater Middle Eastern / consanguineous populations, with genetic counseling and reproductive-option education.
6. **Cascade testing protocols** and early echocardiographic surveillance guidelines for genotype-positive relatives.
7. **Deep clinical phenotyping** (arrhythmia burden via Holter/ICD data, cardiac MRI fibrosis) in future cases to refine risk stratification and timing of VAD/transplant.

---

*Evidence source types represented: human clinical (case reports/kindreds, pediatric HF registries), model organism (mouse knockout/knockdown/AAV rescue), in vitro/biochemical (JPH2–LTCC interaction, proteolysis), and computational/population genetics (gnomAD constraint, founder-haplotype analysis).*


## Artifacts

- [OpenScientist final report](Cardiomyopathy_Dilated_2E-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cardiomyopathy_Dilated_2E-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030366` (3 mentions) - the report calls it "MONDO"; MONDO calls it **cardiomyopathy, dilated, 2E**
- `HP:0001644` (1 mention) - the report calls it "Clinical sign (imaging)"; HP calls it **Dilated cardiomyopathy**
- `HP:0001635` (1 mention) - the report calls it "Clinical sign"; HP calls it **Congestive heart failure**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.