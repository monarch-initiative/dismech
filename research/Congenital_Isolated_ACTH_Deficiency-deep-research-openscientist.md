---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T01:39:33.222905'
end_time: '2026-10-15T02:14:42.250726'
duration_seconds: 2109.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Isolated ACTH Deficiency
  mondo_id: MONDO:0008720
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
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 25
  on_topic: 18
  validator_version: 0.3.0
term_validation:
  total_terms: 39
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 11
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0011736
    reported_labels:
    - Decreased circulating ACTH
    ontology_label: Primary hyperaldosteronism
  - term_id: CL:0000152
    reported_labels:
    - corticotroph / corticotropic cell
    - Tissue/cell level:** pituitary **corticotroph** cells
    - corticotroph
    ontology_label: exocrine cell
  - term_id: CL:0002097
    reported_labels:
    - zona fasciculata
    - zona fasciculata cell
    ontology_label: cortical cell of adrenal gland
  - term_id: CHEBI:3650
    reported_labels:
    - ACTH
    ontology_label: chlorpropamide
  - term_id: CHEBI:17754
    reported_labels:
    - glucocorticoid class
    ontology_label: glycerol
  labels_variant: 6
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
  path: Congenital_Isolated_ACTH_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Isolated_ACTH_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Isolated ACTH Deficiency
- **MONDO ID:** MONDO:0008720 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Isolated ACTH Deficiency** covering all of the
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

# Congenital Isolated ACTH Deficiency — Comprehensive Disease Characterization

**Disease:** Congenital Isolated ACTH Deficiency (IAD)
**MONDO:** MONDO:0008720 · **Category:** Mendelian (monogenic endocrine disorder)
**Report type:** Literature-based knowledge-base compilation (no primary datasets provided)
**Evidence base:** 40 primary papers/reviews reviewed across 5 iterations; 8 confirmed findings recorded to the knowledge graph; evidence types indicated per claim (human clinical, model organism, in vitro, computational/structural). Seminal references include the TPIT discovery (Lamolet 2001, *Cell*, PMID 11290323) and the largest clinical series (Couture 2012, PMID 22170728).

---

## 1. Disease Information

**Overview.** Congenital Isolated ACTH Deficiency (IAD) is a rare monogenic form of **secondary (central) adrenal insufficiency** characterized by low or undetectable serum cortisol due to deficient pituitary **adrenocorticotropic hormone (ACTH)** production, with **preservation of all other anterior pituitary hormones** (GH, TSH, LH/FSH, prolactin) and normal pituitary anatomy. The best-defined form is **neonatal-onset, complete IAD** caused by biallelic loss-of-function variants in **TBX19/TPIT** (PMID 22170728, 15613420). It is clinically important because, untreated, it can cause **neonatal death from acute adrenal crisis**, yet it is fully treatable with glucocorticoid replacement.

**Key identifiers.**
- **MONDO:** MONDO:0008720
- **OMIM:** #201400 (Adrenocorticotropic hormone deficiency / isolated ACTH deficiency); gene **TBX19** OMIM *604614
- **Orphanet:** ORPHA 442 (Isolated ACTH deficiency)
- **ICD-10:** E23.0 (Hypopituitarism, includes isolated deficiency of pituitary hormones); **ICD-11:** 5A61.0 (Hypofunction of pituitary gland / ACTH deficiency)
- **MeSH:** "Adrenocorticotropic Hormone" / "Hypopituitarism"; "Adrenal Insufficiency"
- **Gene (HGNC):** TBX19 (HGNC:11596), alias TPIT; also NFKB2 (HGNC:7795), POMC (HGNC:9201)

**Synonyms / alternative names.** Isolated ACTH deficiency; IAD; TPIT deficiency; congenital isolated adrenocorticotropin deficiency; isolated adrenocorticotropic hormone deficiency; isolated corticotropin deficiency.

**Information source.** Derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet) and **individual-patient case reports/series** (e.g., the 91-patient TPIT series, PMID 22170728). No population EHR datasets were used here.

---

## 2. Etiology

**Primary cause: genetic (Mendelian).** IAD is not infectious or environmentally acquired. The principal molecular cause of neonatal-onset **complete** IAD is **biallelic (homozygous or compound heterozygous) loss-of-function (LOF) in TBX19/TPIT**, a pituitary-restricted T-box transcription factor required for corticotroph terminal differentiation and POMC transcription (PMID 15476446, 15613420, 22170728). In the largest series, TPIT mutations were found in **65% of neonatal-onset complete IAD** but **0% of partial or late-onset IAD** (PMID 22170728).

> "we found a TPIT mutation in 65% of patients with neonatal-onset complete IAD. These patients are homozygous or compound heterozygous for TPIT mutations, and their parents are healthy heterozygous carriers." (PMID 22170728, human clinical)

**Genetic risk factors / genetic heterogeneity.** Other monogenic causes of congenital/childhood central ACTH deficiency:
- **NFKB2** (DAVID syndrome) — heterozygous, usually de novo C-terminal mutations; ACTH deficiency + common variable immunodeficiency (PMID 37322808, 25524009).
- **POMC** — biallelic LOF; adrenal insufficiency with early-onset obesity and red hair (not truly "isolated") (PMID 35775692).
- Rare/other hypopituitarism genes may present with ACTH deficiency within broader combined pituitary hormone deficiency.

**Environmental risk factors.** None established as causal for the congenital genetic disease. **Consanguinity** increases the chance of homozygous TPIT/POMC LOF (autosomal recessive). Family history of an affected sibling/neonatal death is a major risk indicator.

**Protective factors.** No genetic or environmental protective modifiers are established. The main "protective" intervention is **presymptomatic diagnosis** (prenatal/cascade testing in at-risk families) enabling immediate glucocorticoid replacement.

**Gene–environment interactions.** Not applicable as a cause. Clinically, **physiological stressors** (infection, fasting, surgery) unmask/precipitate adrenal crisis on the genetic background of cortisol deficiency — a genotype × stressor interaction at the level of clinical decompensation rather than disease causation.

---

## 3. Phenotypes

Neonatal TPIT-related IAD has a **highly homogeneous** presentation (PMID 15613420). Onset is typically within **hours to days** of birth.

| Phenotype | Type | HPO term | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Hypoglycemia (recurrent, severe; seizures, limpness, apnea/respiratory arrest) | Lab + clinical sign | HP:0001943 (Hypoglycemia); HP:0001998 (Neonatal hypoglycemia) | Neonatal | Severe | Very frequent (hallmark) |
| Low/undetectable serum cortisol | Lab abnormality | HP:0008163 (Decreased circulating cortisol) | Neonatal | Severe | Near-universal |
| Inappropriately low/normal plasma ACTH | Lab abnormality | HP:0011736 (Decreased circulating ACTH) | Neonatal | — | Defining feature |
| Prolonged conjugated (cholestatic) jaundice | Clinical sign / lab | HP:0002908 (Conjugated hyperbilirubinemia); HP:0001396 (Cholestasis) | Neonatal | Moderate–severe | Frequent |
| Seizures | Clinical sign | HP:0001250 (Seizure) | Neonatal | Severe | Frequent (secondary to hypoglycemia) |
| Adrenal insufficiency / adrenal crisis | Clinical | HP:0000846 (Adrenal insufficiency) | Neonatal–lifelong | Life-threatening | Core |
| Hypokalemia / electrolyte disturbance | Lab | HP:0002900 (Hypokalemia) | Neonatal | Variable | Reported |
| Hyponatremia (dilutional, cortisol-dependent) | Lab | HP:0002902 (Hyponatremia) | Variable | Variable | Reported (esp. later/adult cases) |
| Facial dysmorphism (long philtrum, depressed nasal root, epicanthus, low-set ears, mild hypertelorism) | Physical | HP:0000271 (Abnormal facial shape) | Congenital | Mild | Occasional (reported in some cases) |
| Prolonged/severe infections, lethargy, poor feeding, failure to thrive | Clinical | HP:0004322/HP:0001508 | Neonatal–infancy | Variable | Variable |

- **Severity/progression:** Episodic life-threatening decompensations (hypoglycemia, adrenal crisis) on a chronic lifelong deficiency; metabolic/hepatic features are **fully reversible** on hydrocortisone.
- **Important distinction:** Because ACTH is **low**, there is **no hyperpigmentation** (unlike primary adrenal insufficiency/FGD). No salt-wasting/mineralocorticoid deficiency (aldosterone preserved).
- **Quality-of-life impact:** With treatment, generally normal growth, development and QoL; residual burden stems from chronic medication dependence, risk of adrenal crisis, and the vigilance required for sick-day management (QoL instruments: AddiQoL, SF-36, EQ-5D — disease-specific data limited).

Evidence: PMID 15613420 (homogeneous presentation), 15301051 (hypoglycemia + conjugated hyperbilirubinemia resolving on hydrocortisone), 34564059 (neonatal onset at 15 h, undetectable cortisol with normal-range ACTH), 40990269 (hypoglycemic seizures, hypokalemia, cholestasis, dysmorphism).

---

## 4. Genetic / Molecular Information

**Causal gene (principal): TBX19 / TPIT** — HGNC:11596; OMIM *604614; locus **1q24.2**; T-box transcription factor family. Encodes a corticotroph/melanotroph-restricted DNA-binding transcription factor. TPIT was discovered by **Lamolet et al. (2001, *Cell*; PMID 11290323)** as a T-box factor present **only** in pituitary POMC lineages (corticotrophs, melanotrophs) and "apparently in no other tissue, including hypothalamic POMC neurons," that activates POMC transcription cooperatively with PITX1 and can **initiate** POMC-lineage differentiation; the same study reported TPIT mutations in patients with isolated POMC-derived ACTH deficiency.

**Other causal genes:** **NFKB2** (HGNC:7795; 10q24.32; DAVID syndrome), **POMC** (HGNC:9201; 2p23.3; adrenal insufficiency–obesity–red hair).

**Pathogenic variant spectrum (TBX19).** All variant classes reported, all **loss-of-function**:
- **Missense** (e.g., p.Met86Arg within the T-box, disrupting protein–protein interaction/DNA binding; PMID 17652218, 15476446)
- **Nonsense** (e.g., p.Arg286Ter; PMID 40990269)
- **Frameshift / small indels** (e.g., c.782delA; PMID 15476446)
- **Splice-site and synonymous/exonic splice-disrupting** (e.g., p.Thr96= c.288G>A causing exon-2 missplicing; PMID 34564059)
- **Large deletions** (PMID 22170728)

**Functional consequences / mechanisms of LOF** (PMID 22170728): nonsense-mediated mRNA decay, aberrant splicing, loss of DNA binding, and loss of protein–protein interactions (e.g., with PITX1 and coactivator SRC2). The M86R mutation impairs cooperative DNA binding (homodimers, PITX1 heterodimers) and SRC2 recruitment despite retaining monomeric DNA binding (PMID 17652218, in vitro).

**Variant classification (ACMG/AMP).** Reported variants are predominantly **pathogenic/likely pathogenic** (functional assays + recessive segregation + absent/rare in population databases). Allele frequencies are very low in **gnomAD** (e.g., rs376493164 ~1×10⁻⁵, no homozygotes; PMID 34564059).

**Origin:** **germline**, biallelic (AR) for TBX19/POMC; heterozygous (often **de novo**) for NFKB2. No somatic involvement.

**Modifier genes.** None established. Partners/functionally related factors (PITX1, NEUROD1, PAX7, ETV1, CREB3L2, NR4A/Nur family) shape the corticotroph program but are not reported disease modifiers in IAD (PMID 26792828, 21622576, 31481663, 23070814).

**Epigenetics.** No disease-specific methylation signature established in patients. Mechanistically, the POMC locus is controlled by pioneer-factor chromatin remodeling (PAX7) and lineage enhancers on which TPIT acts (PMID 23070814, 26792828) — relevant to normal regulation rather than a documented epigenetic lesion in IAD.

**Chromosomal abnormalities.** Not characteristic; large TBX19 deletions occur but gross cytogenetic abnormalities are not a feature.

---

## 5. Environmental Information

- **Environmental/toxic factors:** None causal for congenital IAD.
- **Infectious agents:** None causal. Intercurrent **infection** is the most common **precipitant of adrenal crisis** (not a cause of the disease).
- **Lifestyle factors:** Not applicable to disease causation. Relevant to management: adherence, stress-dosing behavior, carrying emergency hydrocortisone.

(Note: acquired/late-onset isolated ACTH deficiency in adults can be autoimmune/hypophysitis-related or drug-related, e.g., immune-checkpoint-inhibitor hypophysitis — but that is a separate, non-congenital entity.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic LOF variant in TBX19/TPIT** (germline) **results in** absent or non-functional TPIT transcription-factor protein (nucleus). *[demonstrated: functional assays, PMID 22170728, 17652218]*
2. Loss of TPIT **leads to** failure of **terminal differentiation of pituitary corticotrophs** (and melanotrophs) and failure to activate the **POMC** gene via the TPIT/PITX1 regulatory element. *[demonstrated in human + mouse, PMID 11290323, 26792828, 15525497]*
3. Failed POMC program **results in** absent/deficient **POMC** precursor and its product **ACTH** in anterior-pituitary corticotrophs. *[demonstrated]*
4. Low circulating ACTH **leads to** loss of **MC2R (ACTH receptor) + MRAP1** activation on adrenocortical (zona fasciculata) cells. *[downstream; receptor biology demonstrated, PMID 36588120]*
5. Loss of MC2R/cAMP–PKA signaling **results in** failure of **adrenal steroidogenesis → cortisol (glucocorticoid) deficiency**. *[inferred from HPA physiology + clinical cortisol absence]*
6. Cortisol deficiency **leads to** the clinical phenotype — via branches:
   - **6a.** Impaired hepatic gluconeogenesis/glycogenolysis **→ neonatal hypoglycemia → seizures/apnea**. *[inferred/clinical]*
   - **6b.** Impaired bile flow/hepatic adaptation **→ neonatal cholestasis/conjugated hyperbilirubinemia**. *[clinical association, reversible on replacement]*
   - **6c.** Loss of permissive glucocorticoid effects on vascular tone/stress response **→ hypotension, vulnerability to adrenal crisis → potential neonatal death**. *[clinical, PMID 15613420]*
7. Because TPIT is **lineage-restricted**, **other pituitary hormones are spared** → the deficiency is **isolated** (selective ACTH loss). *[demonstrated]*

**Branch (NFKB2/DAVID):** heterozygous C-terminal **NFKB2** mutation → defective non-canonical NF-κB p100→p52 processing → corticotroph dysfunction **and** B-cell/immune defect → ACTH deficiency **+** hypogammaglobulinemia (PMID 25524009, 37322808, organoid support PMID 39607428).

### Supporting detail
- **Molecular pathways:** POMC transcriptional regulation (TPIT–PITX1–NEUROD1; NR4A/Nur-mediated CRH response; glucocorticoid-receptor negative feedback) (PMID 26792828); downstream **cAMP–PKA** steroidogenic signaling at MC2R (PMID 36588120); non-canonical **NF-κB** (NFKB2 branch).
- **Cellular processes:** arrest of corticotroph terminal differentiation; TPIT also drives a cell-cycle-control switch and secretory/translational scale-up via **CREB3L2** (PMID 31481663, 35524583). BDNF autocrine loop couples precursor engagement to glucocorticoid feedback (PMID 42392084).
- **Protein dysfunction:** TPIT missense (e.g., M86R) → impaired cooperative DNA binding and coactivator (SRC2) recruitment (PMID 17652218). *Structural note:* M86 lies at the T-box dimer interface.
- **Immune involvement:** only in the **NFKB2/DAVID** branch (hypogammaglobulinemia/CVID). TPIT-IAD is **not** immune-mediated.
- **Metabolic changes:** cortisol-dependent failure of gluconeogenesis → hypoglycemia; no primary enzyme defect.

**GO terms:** GO:0045944 (positive regulation of transcription by RNA Pol II), GO:0003700 (DNA-binding transcription factor activity), GO:0030855/GO:0030154 (epithelial/cell differentiation), GO:0042446 (hormone biosynthetic process), GO:0006704 (glucocorticoid biosynthetic process), GO:0051458 (corticotropin secretion), GO:0007267 (cell–cell signaling).
**CL terms:** CL:0000152 (corticotroph / corticotropic cell), CL:1000298? melanotroph (CL:0002487), CL:0000164 (endocrine cell), adrenal cortical cell (CL:0002097 zona fasciculata cell).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **Anterior pituitary / adenohypophysis** (UBERON:0002196 / anterior pituitary UBERON:0002196; adenohypophysis UBERON:0002196) — specifically the corticotroph population. **Secondary (functional):** **Adrenal cortex** (UBERON:0001235), which is hypofunctional/atrophic due to lack of ACTH trophic drive (adrenal hypoplasia in Tpit-null mice, PMID 15525497).
- **Body systems:** **Endocrine system** (hypothalamic–pituitary–adrenal axis); secondary impacts on **hepatobiliary** (cholestasis), **metabolic/CNS** (hypoglycemic seizures), **cardiovascular** (hypotension in crisis). In the NFKB2 branch, the **immune system** is involved.
- **Tissue/cell level:** pituitary **corticotroph** cells (CL:0000152) and melanotrophs (intermediate lobe, vestigial in humans); adrenocortical cells of the **zona fasciculata** (CL:0002097).
- **Subcellular (GO Cellular Component):** **nucleus** (GO:0005634, site of TPIT action/DNA binding); secretory pathway / dense-core secretory granules for ACTH (GO:0030141); plasma membrane MC2R receptor complex on adrenal cells (GO:0005886).
- **Localization/lateralization:** midline pituitary; bilateral adrenal glands. No lateralization.

---

## 8. Temporal Development

- **Onset:** **Congenital**, typically presenting in the **neonatal period** (first hours to days of life) for TPIT-complete IAD; NFKB2/DAVID typically presents in **childhood** (mean ACTH-deficiency diagnosis ~8.6 y, often after infections/alopecia) (PMID 37322808). Onset pattern: **acute** decompensation (hypoglycemia/crisis) superimposed on a congenital deficiency.
- **Progression:** The hormonal deficiency is **stable and lifelong** (not progressive in the TPIT form), but the clinical course is **episodic**, punctuated by stress-precipitated adrenal crises. Metabolic/hepatic features **remit rapidly** with glucocorticoid replacement (treatment-induced remission of manifestations; the underlying deficiency does not remit).
- **Critical periods:** The **neonatal window** is the period of highest vulnerability (risk of death) and of greatest benefit from early diagnosis/replacement. Lifelong vigilance during intercurrent illness/surgery.
- **Duration:** Chronic, lifelong; requires lifelong replacement.

---

## 9. Inheritance and Population

- **Epidemiology:** **Very rare.** Congenital IAD has no robust prevalence/incidence estimates (Orphanet: prevalence unknown/<1/1,000,000 order of magnitude; reported as an "underestimated cause of neonatal death," PMID 15613420). The literature consists of case reports and a few multinational series (largest = 91 IAD patients; TPIT mutations in 17/27 then expanded, PMID 15613420, 22170728).
- **Inheritance patterns:**
  - **TBX19/TPIT:** **Autosomal recessive** (homozygous/compound heterozygous; unaffected heterozygous carrier parents) (PMID 15613420, 22170728).
  - **POMC:** autosomal recessive.
  - **NFKB2 (DAVID):** **autosomal dominant**, frequently **de novo** (PMID 25524009).
- **Penetrance:** For biallelic TPIT LOF, **complete/high penetrance** with early lethal potential if untreated; NFKB2 shows **variable expressivity** (endocrine vs immune features vary within families; some carriers show only immune phenotype) (PMID 25524009).
- **Expressivity:** TPIT-IAD is **phenotypically homogeneous**; NFKB2 is **variable**.
- **Genetic anticipation:** Not applicable (no repeat expansion).
- **Germline mosaicism:** Not specifically documented; de novo events occur for NFKB2.
- **Founder effects / consanguinity:** **Consanguinity** contributes to homozygous TPIT cases; a recurrent TPIT mutation was seen in multiple unrelated families (PMID 15613420). A **POMC 5′-UTR founder mutation** was described in the Perm Tatar population (PMID 35775692) — relevant to the POMC-deficiency differential.
- **Carrier frequency:** Very low; TPIT pathogenic alleles are rare in gnomAD.
- **Demographics / sex ratio:** No strong sex predilection for TPIT-IAD (autosomal). Reported across diverse ethnicities/geographies; no defined endemic region.

---

## 10. Diagnostics

**Biochemical (first-line).**
- **Low/undetectable serum cortisol** (e.g., <1 µg/dL; LOINC 2143-6) with **inappropriately low or normal plasma ACTH** (LOINC 2141-0) — the defining combination of **secondary** adrenal insufficiency (PMID 34564059).
- **Hypoglycemia** (LOINC 2345-7), sometimes hyponatremia/hypokalemia.
- **Normal mineralocorticoid axis:** normal/near-normal aldosterone and plasma renin activity (distinguishes from primary AI).
- **Dynamic testing:** low-dose/standard **ACTH (Synacthen) stimulation** may show adrenal response if atrophy is not advanced; **insulin tolerance test / CRH test / metyrapone** assess central axis (used cautiously in neonates). ACTH-stimulation can transiently increase cortisol early (PMID 15301051).
- **Normal other pituitary hormones** (GH, TSH/free T4, gonadotropins, prolactin) confirms "isolated."

**Imaging.** Pituitary **MRI** is typically **normal** (no structural lesion) in TPIT-IAD — an important feature separating it from structural hypopituitarism.

**Genetic testing (confirmatory).**
- **Approach:** targeted **single-gene (TBX19)** testing in neonatal complete IAD; **gene panels** for adrenal insufficiency/hypopituitarism (TBX19, POMC, NFKB2, and FGD genes MC2R, MRAP, STAR, NNT, TXNRD2) via **NGS/WES**; **WES/WGS** for undiagnosed cases (HaloPlex/NGS arrays used in practice, PMID 34564059).
- CMA/karyotype/FISH, mtDNA, repeat-expansion testing are **not** indicated (not a CNV/mitochondrial/repeat disorder).

**Clinical criteria / differential diagnosis.**
- **Primary (ACTH-high) adrenal insufficiency:** **Familial Glucocorticoid Deficiency** (MC2R/MRAP/STAR/NNT/TXNRD2) — **high ACTH**, hyperpigmentation, preserved mineralocorticoid (PMID 37352919); Addison disease; congenital adrenal hyperplasia (elevated 17-OHP/androgens).
- **Central causes:** combined pituitary hormone deficiency/panhypopituitarism (multiple deficits, abnormal MRI); **POMC deficiency** (obesity/red hair, PMID 35775692); **NFKB2/DAVID** (hypogammaglobulinemia, infections, alopecia, PMID 37322808).
- **Key discriminator:** the **ACTH level** (low/normal = central IAD; high = primary).

**Screening.** No population newborn screening exists for IAD; **cascade genetic testing** and, in families with a known variant, **prenatal/preimplantation testing** enable presymptomatic management (PMID 15613420).

---

## 11. Outcome / Prognosis

- **With early diagnosis + glucocorticoid replacement:** **excellent prognosis** — hypoglycemia and cholestasis resolve, and normal growth/development is achieved (PMID 15301051). Long-term follow-up of TPIT cases supports good outcomes on replacement (PMID 40727905).
- **Without treatment:** potentially **fatal in the neonatal period** from acute adrenal insufficiency; IAD is described as an **underestimated cause of neonatal death** (PMID 15613420).
- **Principal ongoing risk / mortality driver:** **adrenal crisis** during intercurrent illness/stress — in adrenal-insufficiency populations, adrenal crisis mortality is ~**0.5/100 patient-years** and a leading cause of death (PMID 40416465). Rare severe complications include reversible cardiomyopathy during crisis (PMID 39935712).
- **Morbidity/QoL:** chronic medication dependence, need for emergency preparedness; neurodevelopmental sequelae possible if recurrent severe neonatal hypoglycemia is not prevented.
- **Prognostic factors:** time to diagnosis, prevention of hypoglycemic brain injury, adherence, quality of sick-day/stress-dosing education.

---

## 12. Treatment

**Pharmacotherapy (mainstay — lifelong hormone replacement).**
- **Hydrocortisone**, oral, physiological dosing (~**8–15 mg/m²/day** divided 2–3×; neonates/infants often need individualized dosing) — rapidly reverses hypoglycemia and cholestasis and restores growth (PMID 15301051). *NCIT: Hydrocortisone C379; Glucocorticoid C821; Hormone Replacement Therapy C62604.*
- **Mineralocorticoid (fludrocortisone) is generally NOT required** — aldosterone is preserved in central/secondary AI (contrast with primary AI). *NCIT: Fludrocortisone C29089.*
- **Stress/sick-day dosing:** double–triple oral hydrocortisone during febrile illness; **parenteral (IM/IV) hydrocortisone** for vomiting, severe illness, surgery, or adrenal crisis (emergency kit + medical alert). Structured stress-dosing protocols reduce crises (PMID 40416465, 40696758, 40214077).
- **Emergency adrenal crisis management:** immediate parenteral hydrocortisone, IV dextrose for hypoglycemia, fluids/electrolyte correction.

**Advanced/experimental therapeutics.** No gene therapy, cell therapy, RNA therapy, or targeted/immunotherapy exists for IAD; treatment is replacement only. Modified-release hydrocortisone formulations (e.g., Plenadren, Chronocort) aim for more physiological cortisol rhythms (PMID 26683495) — relevant to adrenal insufficiency broadly. In the **NFKB2/DAVID** branch, **immunoglobulin replacement** addresses the immune deficiency (PMID 37322808).

**Surgical/rehabilitative:** not applicable (no surgical target). Supportive care = nutrition, infection management, caregiver education.

**Pharmacogenomics:** none specific to IAD.

**Treatment strategy / personalized medicine:** genotype-informed (TPIT vs POMC vs NFKB2) management — e.g., add Ig replacement for NFKB2; weight/obesity and pigmentation surveillance for POMC; otherwise identical glucocorticoid-replacement backbone.

---

## 13. Prevention

- **Primary prevention:** Not possible for the germline genetic disease. **Genetic counseling** for at-risk (carrier) couples; options include **prenatal diagnosis** and **preimplantation genetic testing** where a familial variant is known (AR recurrence risk 25%) (PMID 15613420).
- **Secondary prevention (early detection):** **Cascade/presymptomatic genetic testing** of newborn siblings in affected families permits immediate glucocorticoid prophylaxis and prevents neonatal death/hypoglycemic injury (PMID 15613420). No population newborn-screening program currently targets IAD.
- **Tertiary prevention (preventing complications):** structured **adrenal-crisis prevention** — patient/caregiver education, written stress-dosing plans, emergency hydrocortisone injection kits, medical-alert identification; address knowledge gaps that drive preventable crises/deaths (PMID 40696758, 40214077, 40416465).
- **Immunization / public health / environmental:** standard childhood immunization (reduces infections that precipitate crisis); in NFKB2/DAVID, vaccine responses may be impaired and Ig replacement considered.
- **Counseling:** genetic counseling re: AR inheritance (TPIT/POMC) vs AD/de novo (NFKB2) and recurrence risks.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** **Mouse** *Tbx19/Tpit* (NCBI Taxon 10090; MGI ortholog) is the principal comparative model; TPIT and the POMC regulatory program are **evolutionarily conserved** across mammals (PMID 26792828). PAX7 expression in melanotropes is conserved in human and **dog** (PMID 23070814).
- **Natural disease in animals:** No well-established spontaneous TPIT-mutation disease analog is documented in companion animals/livestock (OMIA: not a classically catalogued natural animal disease). Canine pituitary biology is referenced comparatively (Cushing's/adenoma context), not as a natural IAD model.
- **Comparative biology:** Mouse Tpit-null endocrine phenotype closely mirrors human IAD (reduced ACTH, undetectable corticosterone, adrenal hypoplasia) — strong mechanistic conservation (PMID 15525497).
- **Zoonotic potential:** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

- **Mouse (Mus musculus, NCBI Taxon 10090):**
  - **Tpit-null (knockout)** — recapitulates IAD: *"plasma ACTH is greatly reduced … plasma corticosterone is undetectable and the adrenals are hypoplastic"* (PMID 15525497, model organism). Demonstrates Tpit as positive regulator of POMC-cell differentiation and negative regulator of alternate (gonadotroph) fate.
  - **Pax7 knockout** — defines chromatin/enhancer context of Tpit action (melanotrope identity) (PMID 23070814).
  - **POMC-knockout and adrenalectomized mice** — reveal compensatory corticotrope-precursor accumulation and BDNF/Tpit precursor biology (PMID 42392084).
  - Resources: **MGI/IMPC/IMSR**.
- **In vitro / cellular:** **AtT-20** corticotroph tumor cell line (POMC/Tpit functional assays, PMID 21622576); heterologous expression systems for TPIT mutation functional testing and splicing assays (PMID 17652218, 34564059).
- **Human iPSC-derived pituitary organoids:** model corticotroph deficiency and support the functional role of **NFKB2** in DAVID syndrome (PMID 39607428, in vitro human).
- **Phenotype recapitulation:** strong for the **endocrine core** (ACTH/corticosterone deficiency, adrenal hypoplasia). **Limitations:** neonatal **cholestasis**, dysmorphism, and human-specific developmental/clinical features are not fully modeled; mouse intermediate-lobe (melanotrope) biology differs from humans.
- **Applications:** dissecting corticotroph differentiation, POMC transcriptional control, testing differentiation signals (BDNF, CREB3L2), and modeling genotype-specific mechanisms.

---

## Supported vs. Refuted Hypotheses

**Supported:**
- Biallelic TBX19/TPIT LOF is the principal cause of neonatal-onset **complete** IAD (65% of such cases) — PMID 22170728.
- Highly homogeneous neonatal phenotype (hypoglycemia, cholestasis, undetectable cortisol with low/normal ACTH), fatal if untreated, reversible with hydrocortisone — PMID 15613420, 15301051.
- Mechanistic chain TPIT→POMC/ACTH→MC2R→cortisol, with isolated (lineage-restricted) deficiency — PMID 26792828, 36588120.
- Tpit-null mouse recapitulates the endocrine phenotype — PMID 15525497.

**Refuted / bounded:**
- TPIT mutations do **NOT** explain **partial** or **late-onset** IAD (0% in those groups) — PMID 22170728; implies additional, partly unknown genetic/acquired causes.
- IAD is **not** a mineralocorticoid-deficient, hyperpigmented, or ACTH-high disorder — these features indicate **primary** AI/FGD instead — PMID 37352919.

## Limitations & Future Directions
- No large-scale prevalence/incidence or registry data; epidemiology is case-series-based.
- Genetic cause of partial/late-onset IAD remains largely unexplained (gene-discovery opportunity via WES/WGS).
- Limited QoL and long-term neurodevelopmental outcome data specific to IAD.
- Mechanistic links from cortisol deficiency to neonatal **cholestasis** remain incompletely defined (largely inferred/clinical).
- No disease-modifying/curative therapy; replacement is lifelong — future directions include physiological cortisol delivery and, speculatively, corticotroph cell/gene-based restoration.

---

### Ontology quick-reference
- **Disease:** MONDO:0008720; OMIM #201400; ORPHA:442; ICD-10 E23.0
- **Genes:** TBX19 (HGNC:11596, OMIM *604614), NFKB2 (HGNC:7795), POMC (HGNC:9201)
- **HPO:** HP:0001943, HP:0001998, HP:0008163, HP:0011736, HP:0001396, HP:0002908, HP:0000846, HP:0001250, HP:0002900
- **GO:** GO:0045944, GO:0003700, GO:0030154, GO:0006704, GO:0051458
- **CL:** CL:0000152 (corticotroph), CL:0002097 (zona fasciculata cell)
- **UBERON:** UBERON:0002196 (adenohypophysis/anterior pituitary), UBERON:0001235 (adrenal cortex)
- **CHEBI:** CHEBI:17650 (cortisol), CHEBI:3650 (ACTH), CHEBI:17754 (glucocorticoid class)
- **NCIT:** C379 (Hydrocortisone), C821 (Glucocorticoid), C62604 (Hormone Replacement Therapy)


## Artifacts

- [OpenScientist final report](Congenital_Isolated_ACTH_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Isolated_ACTH_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 22 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0011736` (2 mentions) - the report calls it "Decreased circulating ACTH"; HP calls it **Primary hyperaldosteronism**
- `CL:0000152` (3 mentions) - the report calls it "corticotroph / corticotropic cell", "Tissue/cell level:** pituitary **corticotroph** cells", "corticotroph"; CL calls it **exocrine cell**
- `CL:0002097` (3 mentions) - the report calls it "zona fasciculata", "zona fasciculata cell"; CL calls it **cortical cell of adrenal gland**
- `CHEBI:3650` (1 mention) - the report calls it "ACTH"; CHEBI calls it **chlorpropamide**
- `CHEBI:17754` (1 mention) - the report calls it "glucocorticoid class"; CHEBI calls it **glycerol**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008163` (2 mentions) - the report calls it "Decreased circulating cortisol"; HP calls it **Decreased circulating cortisol level**
- `HP:0000271` (1 mention) - the report calls it "Abnormal facial shape"; HP calls it **Abnormality of the face**, and lists "Abnormal face" among its other names
- `GO:0045944` (2 mentions) - the report calls it "positive regulation of transcription by RNA Pol II"; GO calls it **positive regulation of transcription by RNA polymerase II**
- `GO:0030154` (2 mentions) - the report calls it "epithelial/cell differentiation"; GO calls it **cell differentiation**
- `CL:0000164` (1 mention) - the report calls it "endocrine cell"; CL calls it **enteroendocrine cell**
- `UBERON:0002196` (4 mentions) - the report calls it "adenohypophysis/anterior pituitary"; UBERON calls it **adenohypophysis**, and lists "anterior pituitary" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000152` - called "corticotroph / corticotropic cell", "Tissue/cell level:** pituitary **corticotroph** cells", "corticotroph"
- `CL:0002097` - called "zona fasciculata", "zona fasciculata cell"
- `UBERON:0001235` - called "Adrenal cortex", "adrenal cortex"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.