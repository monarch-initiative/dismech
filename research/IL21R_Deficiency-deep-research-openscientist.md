---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T15:44:16.979448'
end_time: '2026-09-06T16:15:17.330849'
duration_seconds: 1860.35
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: IL21R Deficiency
  mondo_id: ''
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 46
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 1
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0014219
    reported_labels:
    - immunodeficiency 56
    ontology_label: alacrima, achalasia, and intellectual disability syndrome
  - term_id: HP:0001394
    reported_labels:
    - frequent, progressive
    ontology_label: Cirrhosis
  - term_id: HP:0001508
    reported_labels:
    - common
    ontology_label: Failure to thrive
  - term_id: HP:0004313
    reported_labels:
    - most
    ontology_label: Decreased circulating immunoglobulin concentration
  - term_id: HP:0002850
    reported_labels:
    - most
    ontology_label: Decreased circulating IgM concentration
  - term_id: HP:0040218
    reported_labels:
    - most
    ontology_label: Reduced total natural killer cell count
  - term_id: NCIT:C603
    reported_labels:
    - for hypogammaglobulinemia
    ontology_label: Isotretinoin
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: IL21R_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: IL21R_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IL21R Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IL21R Deficiency** covering all of the
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

# IL21R Deficiency (Immunodeficiency 56) — Comprehensive Disease Characterization

*Autonomous literature-based discovery report. Evidence types are labeled: **[human clinical]**, **[model organism]**, **[in vitro]**, **[computational/database]**. Primary citations are given as PMIDs.*

---

## Summary (Answer to the Research Question)

IL21R Deficiency is an **ultra-rare, autosomal-recessive combined immunodeficiency (Immunodeficiency 56; OMIM #615207)** caused by **biallelic loss-of-function mutations in *IL21R*** (chromosome 16p12.1). Loss of a functional IL-21 receptor abolishes IL-21 → common-gamma-chain/JAK1–JAK3 → STAT3 (and STAT1/STAT5) signaling, crippling B-cell class switching/plasma-cell differentiation, T-follicular-helper help, CD8 memory, and NK/MAIT/NKT cytotoxicity. Clinically this produces recurrent bacterial/fungal/viral infections, hypogammaglobulinemia with paradoxically elevated IgE/atopy, and—most characteristically—**chronic *Cryptosporidium* infection driving sclerosing cholangitis and progressive liver disease**. Hematopoietic stem cell transplantation (HSCT) is the only curative therapy but must be performed before irreversible biliary/liver damage; overall prognosis without early transplant is poor.

**First described:** Kotlarz et al., *J Exp Med* 2013 (PMID 23440042). **Largest cohort:** Cagdas et al. 2021, n=13 (PMID 33929673).

---

## 1. Disease Information

**Overview.** A monogenic inborn error of immunity in the "combined immunodeficiency (CID)" category, defined by absent/non-functional IL-21 receptor signaling. It affects both adaptive (B and T cell) and innate (NK) immunity and characteristically predisposes to opportunistic *Cryptosporidium* infection of the biliary tree. **[human clinical]** (PMID 23440042, 33929673)

**Key identifiers (computational/database):**
- **OMIM:** #615207 — "Immunodeficiency 56" (IMD56)
- **Gene:** *IL21R*, OMIM *605383; **HGNC:6006**; NCBI Gene 50615; Ensembl ENSG00000159374; UniProt Q9HBE5 (IL21R_HUMAN); cytoband 16p12.1
- **Orphanet:** Listed under combined immunodeficiencies / IL-21R-related; no widely used dedicated ORPHAcode—commonly grouped with "Combined immunodeficiency."
- **MONDO:** Suggested MONDO:0014219 ("immunodeficiency 56") — *to be verified against current MONDO release.*
- **ICD-10:** D81.8 / D81.9 (other/unspecified combined immunodeficiencies). **ICD-11:** 4A01.3Y (combined immunodeficiencies, other).
- **MeSH:** No dedicated descriptor; indexed under "Severe Combined Immunodeficiency"/"Primary Immunodeficiency Diseases" + "Receptors, Interleukin-21."

**Synonyms / alternative names:** IL-21R deficiency; Interleukin-21 receptor deficiency; Immunodeficiency 56 (IMD56); IL21R-related combined immunodeficiency.

**Information source.** Aggregated disease-level knowledge derived from **individual patient case series** (≈20+ patients worldwide) synthesized in cohort papers and reviews—not from large registries/EHR. **[human clinical]**

---

## 2. Etiology

**Disease causal factors.** *Monogenic/genetic.* Biallelic (homozygous or compound-heterozygous) loss-of-function variants in *IL21R* are necessary and sufficient. An **infectious trigger** (chronic *Cryptosporidium parvum/hominis* biliary infection) is the principal driver of the signature organ pathology (cholangitis/liver disease) in the setting of the genetic immune defect—an obligate gene × pathogen interaction. **[human clinical]** (PMID 23440042: *"cryptosporidial infections associated with chronic cholangitis and liver disease"*)

**Genetic risk factors.**
- *Causal variants:* e.g., c.G602T (p.Arg201Leu, missense causing receptor mistrafficking/loss of ligand binding); c.240_245delCTGCCA (p.C81_H82del, in-frame deletion). 8 unique mutations reported across 8 families by 2021 (missense, in-frame indels, and other LOF classes). **[human clinical/in vitro]** (PMID 23440042, 33929673)
- *Modifier genes:* None established (cohort too small).

**Environmental risk factors.** **Consanguinity** (parental relatedness) is the dominant epidemiologic risk factor, increasing homozygosity for rare recessive alleles. Exposure to *Cryptosporidium* (contaminated water/food) converts the immune defect into life-threatening cholangiopathy. No sex, occupational, or toxin risk factors. **[human clinical]** (PMID 23440042)

**Protective factors.** No genetic protective/modifier alleles identified. Environmentally, **avoidance of *Cryptosporidium* exposure** (water precautions/filtration) and early curative HSCT are protective against the worst outcomes. **[human clinical]** (inferred)

**Gene–environment interactions.** The core GxE interaction: *IL21R*-null immune state + *Cryptosporidium* exposure → sclerosing cholangitis. Restoration of immune competence (HSCT) enables clearance of the parasite, halting the environmental driver. **[human clinical]** (PMID 30850087: cholangiopathy improvement *"following establishment of immune competence"*)

---

## 3. Phenotypes (with HPO suggestions & frequencies)

Frequencies from the 13-patient cohort (PMID 33929673) unless noted. **[human clinical]**

| Phenotype (type) | Frequency | HPO |
|---|---|---|
| Recurrent bacterial infections (clinical sign) | 84.6% | HP:0002718 |
| Recurrent fungal infections | 46.2% | HP:0009098 |
| Recurrent viral infections (incl. CMV) | 38.5% | HP:0004429 |
| Cryptosporidiosis (protozoan infection) | ~46% | HP:0002726 (recurrent protozoan infection) |
| Sclerosing cholangitis / cholangitis (sign) | 46.2% | HP:0100574 |
| Chronic diarrhea (symptom) | frequent | HP:0002028 / HP:0002014 |
| Chronic liver disease / cirrhosis (sign) | frequent, progressive | HP:0001394 |
| Failure to thrive (sign) | common | HP:0001508 |
| Asthma (sign) | 23.1% | HP:0002099 |
| Inflammatory/eczematous skin disease | 15.3% | HP:0000964 / HP:0011123 |
| Recurrent anaphylaxis | 7.9% | HP:0100845 |
| Lymphadenopathy | reported | HP:0002716 |
| Marginal zone B-cell lymphoma (malignancy) | reported (PMID 33966600) | HP:0012190 |
| Hypogammaglobulinemia (lab) | most | HP:0004313 |
| Elevated serum IgE (lab) | ~50% | HP:0003212 |
| Decreased memory B cells (lab) | most | HP:0002850 |
| Reduced circulating Tfh (lab) | most | (Abnormal Tfh; HP:0410276-family) |
| Reduced MAIT cells (lab) | most | — |
| Abnormal/reduced terminally differentiated NK cells (lab) | most | HP:0040218 |

**Characteristics.** Onset pediatric — **median 2.5 years (range 0.5–7)**. Severity variable but the hepatobiliary component is typically **progressive** and life-limiting. Infections are **recurrent/chronic**; atopy (IgE, asthma, anaphylaxis) is **episodic**.

**Quality-of-life impact.** No formal EQ-5D/SF-36/PROMIS data. Qualitatively severe: chronic diarrhea/malabsorption → growth failure; progressive cholangiopathy → cholestasis, portal hypertension, end-stage liver disease; recurrent infections and hospitalizations; transplant-related morbidity. **[human clinical]**

Key quote (PMID 33929673): *"The main clinical manifestations were recurrent bacterial (84.6%), fungal (46.2%), and viral (38.5%) infections; cryptosporidiosis-associated cholangitis (46.2%); and asthma (23.1%). Inflammatory skin diseases (15.3%) and recurrent anaphylaxis (7.9%) constitute novel phenotypes."*

---

## 4. Genetic / Molecular Information

- **Causal gene:** ***IL21R*** (HGNC:6006; 16p12.1; NCBI 50615; UniProt Q9HBE5). Type I cytokine receptor; heterodimerizes with the common gamma chain (γc / IL2RG / CD132). **[computational/database]**
- **Pathogenic variants (ACMG):** classified pathogenic/likely pathogenic. Reported types: **missense** (p.Arg201Leu), **in-frame deletion** (p.C81_H82del), and additional LOF alleles (8 unique across 8 families). Loss-of-function is the uniform functional consequence—no gain-of-function or dominant-negative disease described; heterozygous carriers are healthy (recessive). **[human clinical/in vitro]** (PMID 23440042, 33929673)
- **Allele frequency:** Biallelic *IL21R* LOF is essentially absent in gnomAD; individual pathogenic alleles are ultra-rare/private. **[computational/database]**
- **Somatic vs germline:** **Germline.** No somatic/oncogenic *IL21R* role in this disease.
- **Functional consequences:** p.Arg201Leu → **aberrant receptor trafficking to the plasma membrane, loss of IL-21 ligand binding, and abrogated STAT1/STAT3/STAT5 phosphorylation** (PMID 23440042: *"aberrant trafficking of the IL-21R to the plasma membrane, abrogates IL-21 ligand binding, and leads to defective phosphorylation of ... STAT1, STAT3, and STAT5"*). **[in vitro]**
- **Modifier genes / epigenetics / chromosomal abnormalities:** None reported; disease is a point-mutation/small-indel monogenic disorder, not a structural/aneuploidy syndrome.

---

## 5. Environmental Information

- **Environmental factors:** No toxin/radiation/pollution etiology. The critical environmental element is **exposure to the waterborne protozoan *Cryptosporidium***.
- **Lifestyle factors:** Not applicable as risk drivers; hygiene/water safety are relevant for preventing opportunistic infection.
- **Infectious agents (NCBI Taxonomy):** ***Cryptosporidium parvum*** (NCBI:txid5807) / ***C. hominis*** (NCBI:txid237895) — biliary/intestinal; **Cytomegalovirus** (HHV-5, NCBI:txid10359); plus recurrent pyogenic bacteria and fungi (incl. *Pneumocystis*). These are **opportunistic consequences** of the immunodeficiency, not primary causes. **[human clinical]** (PMID 23440042, 33966600)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain
1. **Biallelic *IL21R* loss-of-function mutation** (e.g., p.Arg201Leu) → **leads to** absent or mistrafficked IL-21R protein that fails to reach/function at the plasma membrane and cannot bind IL-21. **[in vitro, demonstrated]** (PMID 23440042)
2. Loss of surface IL-21R → **prevents** assembly of the IL-21R/γc receptor complex and **abrogates** JAK1/JAK3 activation → **results in** failed phosphorylation of STAT3 (and STAT1/STAT5). **[in vitro, demonstrated]** (PMID 23440042; pathway review PMID 24126614)
3. Absent STAT3 signaling → **fails to up-regulate the plasma-cell master regulator BLIMP1/PRDM1 (and to down-regulate BCL6)** → **impairs** IL-21-driven B-cell activation, immunoglobulin class-switch recombination, and differentiation into plasmablasts/plasma cells → **causes** hypogammaglobulinemia, poor specific-antibody responses, and reduced memory B cells. **[in vitro + human clinical]** (PMID 23440042, 24126614, 18354204 — the latter: *"stimulation with IL-21 ... induced robust and prolonged STAT3 activation in primary human B cells"* and STAT3 *"triggered BLIMP1 mRNA and protein up-regulation, plasma cell phenotypic features, and Ig secretion"*)
4. **Branch A (humoral/atopy):** Loss of IL-21's normal restraint on IgE, unopposed IL-4/Th2 activity → **leads to** elevated IgE, asthma, eczema, anaphylaxis. **[model organism + human clinical]** (PMID 12446913: high IgE/low IgG1 in Il21r-/- mice; PMID 33929673: IgE elevated in 50%)
5. **Branch B (cellular cytotoxicity):** Absent STAT3 downstream of IL-21R → **reduces** CD8+ T-cell memory and lytic-machinery induction, NK-cell cytotoxicity, and MAIT/NKT-cell numbers → **impairs** control of intracellular/opportunistic pathogens. **[human clinical/in vitro]** (PMID 23830147, 25941256, 23440042)
6. Combined humoral + cytotoxic failure + reduced Tfh help → **permits** chronic **Cryptosporidium** infection of intestinal and **biliary epithelium**. **[human clinical]** (PMID 23440042)
7. Persistent biliary *Cryptosporidium* → **drives** chronic inflammation of bile ducts → **causes** sclerosing cholangitis, fibrosis, cirrhosis, portal hypertension, end-stage liver disease (and rare cholangiocarcinoma risk by analogy to other cryptosporidial-cholangitis PIDs). **[human clinical]** (PMID 23440042, 30850087)
8. Chronic immune dysregulation/impaired tumor surveillance → **contributes to** lymphoproliferation/lymphoma (e.g., marginal zone lymphoma). **[human clinical, inferred]** (PMID 33966600)

### Detail by category
- **Molecular pathways:** IL-21 → IL-21R/γc → **JAK1/JAK3 → STAT3** (canonical), with STAT1/STAT5 and PI3K–AKT and MAPK as secondary arms (Reactome "Interleukin-21 signaling"; KEGG "Jak-STAT signaling pathway hsa04630"). **GO:0038114** IL-21-mediated signaling pathway; **GO:0007259** JAK-STAT signaling.
- **Cellular processes:** B-cell differentiation (**GO:0030183**), isotype/class switching (**GO:0045190**), plasma-cell differentiation (**GO:0002317**), germinal-center/Tfh help, NK-mediated cytotoxicity (**GO:0042267**), CD8 memory formation.
- **Protein dysfunction:** Receptor **misfolding/mistrafficking and loss of ligand binding** (not aggregation); pure loss of function.
- **Immune system involvement:** Combined immunodeficiency + immune dysregulation (atopy, lymphoproliferation).
- **Tissue damage:** Immune-mediated + infection-driven **biliary fibrosis/sclerosis** and hepatocellular injury.
- **Cell types (CL):** B cells CL:0000236 (memory B, plasmablast CL:0000980), Tfh CL:0002038, CD8 memory T CL:0000909, NK CL:0000623, MAIT CL:0000940, NKT cells; biliary epithelial (cholangiocyte) as the injured target.
- **Omics:** No dedicated transcriptomic/proteomic/metabolomic disease signatures published (ultra-rare). Mechanistic data are from targeted immunophenotyping and STAT-phosphorylation flow assays. **[human clinical/in vitro]**

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **Bile ducts** (UBERON:0002394; intra- and extrahepatic — sclerosing cholangitis, bilateral/diffuse), **liver** (UBERON:0002107), **intestine/GI tract** (UBERON:0000160), **immune/lymphoid organs** (bone marrow UBERON:0002371, lymph node UBERON:0000029, spleen UBERON:0002106, thymus). **[human clinical]**
- **Secondary/complications:** lung/respiratory tract (UBERON:0002048; recurrent pneumonia incl. CMV/*Pneumocystis*), skin (UBERON:0002097; eczema), portal hypertension complications.
- **Body systems:** immune/hematolymphoid, hepatobiliary/digestive, respiratory, integumentary.
- **Tissue/cell level:** biliary/intestinal **epithelium** (infection target); lymphoid cell populations (B/T/NK as above).
- **Subcellular (GO CC):** plasma membrane (**GO:0005886**) — site of the receptor-localization defect; secretory pathway/ER involved in receptor mistrafficking.
- **Localization/lateralization:** Cholangitis is typically **diffuse/bilateral intrahepatic ± extrahepatic**; systemic immune involvement.

---

## 8. Temporal Development

- **Onset:** Pediatric/early childhood; **median 2.5 y (0.5–7 y)**; onset often **insidious** (chronic diarrhea, recurrent infections) (PMID 33929673). **[human clinical]**
- **Progression:** Hepatobiliary disease is **chronic and progressive** (cholangitis → fibrosis → cirrhosis → end-stage liver disease). Infections are recurrent; atopy episodic. Rate variable between patients.
- **Course/duration:** Chronic, lifelong without curative HSCT; frequently fatal in childhood if untreated or if transplant occurs after advanced organ damage.
- **Critical period:** A key **therapeutic window** exists — HSCT before advanced cholangiopathy/liver damage markedly improves outcome (PMID 30850087). **[human clinical]**

---

## 9. Inheritance and Population

- **Epidemiology:** **Ultra-rare;** ~20+ patients reported worldwide by 2021; no reliable prevalence/incidence figures. **[human clinical]** (PMID 33929673)
- **Inheritance:** **Autosomal recessive**; biallelic *IL21R* mutations. **[human clinical]** (PMID 23440042)
- **Penetrance/expressivity:** Immunodeficiency penetrance appears **complete** in biallelic-null individuals; **expressivity variable** (onset age, presence of cholangitis/atopy/lymphoma).
- **Anticipation / germline mosaicism:** Not applicable/none reported.
- **Founder effects:** None established (8 distinct mutations/8 families).
- **Consanguinity:** Strong association — most families consanguineous.
- **Carrier frequency:** Not defined; alleles are private/ultra-rare in gnomAD → cascade (family-specific) rather than population carrier screening.
- **Demographics:** Reported across multiple ethnic groups (Middle Eastern, Turkish, European and others via 7 centers); **no sex predilection** (autosomal); age distribution skewed pediatric.

---

## 10. Diagnostics

- **Genetic testing (definitive):** **Whole-exome sequencing or NGS inborn-errors-of-immunity gene panels** identify biallelic *IL21R* variants; targeted single-gene/Sanger for cascade testing. WGS useful for non-coding/structural variants. CMA/karyotype/FISH not indicated. **[human clinical]** (PMID 33929673: 5 novel patients found by *"exome or NGS panel sequencing"*)
- **Functional confirmation (in vitro):** absent surface IL-21R expression; **abrogated IL-21-induced STAT3 phosphorylation** by flow cytometry; impaired IL-21-driven B-cell class switch/Ig secretion (PMID 23440042). **[in vitro]**
- **Laboratory (LOINC-type):** serum immunoglobulins (hypogammaglobulinemia; **high IgE**), specific antibody titers, lymphocyte subsets (low memory B, low Tfh/MAIT, altered NK), liver function/cholestatic panel.
- **Microbiology:** **Cryptosporidium stool/bile PCR (more sensitive than microscopy)** — critical and often missed (PMID 12690272: *"Cryptosporidium could be detected by PCR but not by microscopy"*).
- **Imaging:** **MRI/MRCP** or cholangiography for sclerosing cholangitis (ductal strictures/beading, dilatation); ultrasound.
- **Biopsy/pathology:** liver biopsy showing sclerosing cholangiopathy/fibrosis.
- **Clinical criteria / differential:** No disease-specific criteria; diagnosed under IUIS CID framework. **Differential:** IL-21 (ligand) deficiency (phenocopy; PMID 24746753), CD40L/CD40 (hyper-IgM), MHC class II deficiency, DOCK8 deficiency, STAT3-LOF hyper-IgE syndrome, CVID — distinguished by genetics + the IL-21-signaling assay.
- **Screening:** Not on newborn-screening TREC panels (patients usually have T cells). Carrier/cascade testing and prenatal/PGD available for known familial variants. **[human clinical]**

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Poor without early curative therapy. In the largest cohort, **post-HSCT overall survival was only 33.3% (2/6)**, and mortality among non-transplanted patients was high (PMID 33929673). In a broader PID sclerosing-cholangitis cohort, **7/13 (53.8%) died a median 4 months post-HSCT**, while 6/13 with milder cholangiopathy survived and improved (PMID 30850087). **[human clinical]**
- **Prognostic factors:** **Pre-existing organ (liver/biliary) damage is the key negative prognostic factor** (PMID 33929673: *"pre-existing organ damage constituting a negative prognostic factor"*); earlier diagnosis/transplant improves outcome.
- **Morbidity/QoL:** growth failure, chronic liver disease/portal hypertension, transplant-related complications; substantial disability.
- **Complications:** end-stage liver disease, portal hypertension, disseminated/opportunistic infection, lymphoma/lymphoproliferation, post-transplant *Cryptosporidium* recrudescence.
- **Recovery potential:** Immune reconstitution and cholangiopathy reversal possible if HSCT precedes advanced fibrosis.
- **Prognostic biomarkers:** severity/stage of cholangiopathy on imaging/histology; persistent *Cryptosporidium* positivity.

---

## 12. Treatment

- **Definitive (curative):** **Allogeneic hematopoietic stem cell transplantation (HSCT)** — NCIT:C15431; ideally with **reduced-intensity conditioning**, performed **before** advanced liver disease (PMID 23440042 recommends *"early diagnosis and allogeneic hematopoietic stem cell transplantation"*; PMID 30850087). **[human clinical]**
- **Sequential liver + HSCT (NCIT:C15393 liver transplantation):** for end-stage liver disease with combined immunodeficiency; curative in analogous PID cryptosporidial cirrhosis (PMID 29377874). **[human clinical]**
- **Supportive pharmacotherapy:**
  - **Immunoglobulin replacement therapy** (IVIG/SCIG) — NCIT:C603 — for hypogammaglobulinemia.
  - **Anti-*Cryptosporidium* agents:** **nitazoxanide** (CHEBI:189102/NCIT), **paromomycin**; often only partially effective without immune reconstitution.
  - **Antimicrobial prophylaxis:** e.g., trimethoprim-sulfamethoxazole for *Pneumocystis*; antivirals/antifungals as indicated.
  - **Atopy management:** asthma controllers, anaphylaxis precautions.
- **Advanced/experimental:** No approved gene therapy or targeted molecular therapy; *IL21R* is a plausible future **gene-addition/gene-editing** target by analogy to other γc-family SCID gene therapies (PMID 20660403). No IL21R-specific clinical trials (NCT) identified. **[human clinical/inferred]**
- **Pharmacogenomics:** none specific.
- **Strategy:** Diagnose early → prevent/treat *Cryptosporidium* + IgG replacement + prophylaxis → **proceed to HSCT before liver damage**; combined liver+HSCT if cirrhotic.

---

## 13. Prevention

- **Primary prevention:** Not preventable at the genetic level; **genetic counseling** for consanguineous/at-risk families; **preimplantation/prenatal genetic diagnosis** for known familial variants.
- **Secondary prevention:** Early molecular diagnosis (NGS) in infants with recurrent infection/chronic diarrhea; **surveillance for *Cryptosporidium*** (PCR) and hepatobiliary monitoring (MRCP/LFTs).
- **Tertiary prevention:** IgG replacement, antimicrobial prophylaxis, timely HSCT to prevent progression; post-transplant vigilance against *Cryptosporidium* recrudescence.
- **Environmental/public-health:** **Water safety/filtration and hygiene** to avoid *Cryptosporidium* exposure (boil/filter water, avoid recreational water risk).
- **Immunization:** standard non-live vaccines as able; **avoid live vaccines** in combined immunodeficiency.
- **Counseling:** autosomal-recessive 25% recurrence risk per pregnancy; cascade carrier testing. **[human clinical/guideline-inferred]**

---

## 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** *IL21R* is conserved in mammals. **Mouse** *Il21r* (NCBI Gene 60504; chr 7; NCBI:txid10090); rat, zebrafish orthologs exist.
- **Natural disease:** No well-characterized naturally occurring IL21R-deficiency disease in companion animals/wildlife (OMIA — none prominent). Veterinary relevance is chiefly as engineered research models.
- **Comparative biology:** IL-21/IL-21R humoral-regulatory function is evolutionarily conserved; the γc-cytokine receptor family (IL-2/4/7/9/15/21) shares CD132 across species (structural conservation, PMID 37535730). **[computational/model organism]**
- **Transmission/zoonosis:** Not applicable to the genetic disease (though *Cryptosporidium* itself is zoonotic).

---

## 15. Model Organisms

- **Mouse (mammalian) — *Il21r*-knockout** (Ozaki et al. 2002, *Science*, PMID 12446913): normal lymphoid development but, after immunization, **higher IgE and lower IgG1**; **Il4/Il21r double-KO → dysgammaglobulinemia with severely impaired IgG**. **[model organism]**
  - *Phenotype recapitulation:* reproduces human antibody dysregulation (IgE-high/IgG-low, impaired specific antibody) and demonstrates IL-21/IL-4 cooperation.
  - *Limitations:* mice have grossly normal lymphoid development and **do not spontaneously develop cryptosporidial sclerosing cholangitis** (redundancy + differing pathogen exposure), so the hepatobiliary phenotype is not captured.
  - *Applications:* dissecting IL-21 control of B-cell class switching, Tfh/germinal-center biology, CD8/NK function.
- **Other models:** γc-family biology also modeled in zebrafish/other systems (e.g., IL-2Rγc SCID models, PMID 35216498), informing the shared-receptor mechanism though not IL21R-specific.
- **Genetic model types available:** knockout (constitutive); conditional/humanized IL21R models feasible but not disease-defining. Resources: MGI (mouse), Alliance of Genome Resources.

---

## Supported vs. Refuted Hypotheses

**Supported (evidence-backed):**
- Biallelic *IL21R* LOF causes an autosomal-recessive combined immunodeficiency (PMID 23440042, 33929673).
- Mechanism is failed IL-21R→JAK/STAT3 signaling affecting B, Tfh, CD8-memory, NK, MAIT/NKT compartments (PMID 23440042, 24126614, 23830147, 25941256).
- *Cryptosporidium*-driven sclerosing cholangitis/liver disease is the prognosis-defining complication (PMID 23440042, 30850087).
- HSCT is curative but timing-dependent; organ damage worsens outcome (PMID 33929673, 30850087).
- Il21r-/- mice model the antibody dysregulation (PMID 12446913).

**Refuted / not applicable:**
- Not X-linked (distinct from γc/IL2RG SCID); heterozygotes unaffected → not dominant/dominant-negative.
- No environmental/toxin primary etiology; no founder mutation; no somatic/oncogenic driver role.

## Limitations & Future Directions

- Evidence rests on **<25 patients**; frequencies/prognosis have wide uncertainty. No prevalence, QoL (EQ-5D/SF-36), or omics datasets exist.
- MONDO/Orphanet identifiers should be verified against current releases.
- Future needs: international registry/natural-history study; standardized *Cryptosporidium* surveillance; evaluation of gene-editing/gene-addition therapy; optimized reduced-intensity conditioning and combined liver+HSCT protocols.

---

### Key References (PMIDs)
23440042 (Kotlarz 2013, original description) · 33929673 (Cagdas 2021, cohort n=13) · 33966600 (Edeer Karaca 2021, marginal zone lymphoma) · 24746753 (Salzer 2014, IL-21 ligand deficiency) · 12446913 (Ozaki 2002, Il21r-/- mouse) · 24126614 (Desjardins 2013, IL-21/B-cell memory review) · 23830147 (Ives 2013, CD8 memory) · 25941256 (Wilson 2015, MAIT/NKT via STAT3) · 30850087 (Hadžić 2019, HSCT for PID cholangitis) · 29377874 (sequential liver+HSCT) · 12690272 (Cryptosporidium PCR diagnosis) · 18354204 (Diehl 2008, IL-21/STAT3→BLIMP1 plasma-cell differentiation) · 37535730 (γc receptor structure) · 20660403 (γc-family gene therapy).


## Artifacts

- [OpenScientist final report](IL21R_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](IL21R_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014219` (1 mention) - the report calls it "immunodeficiency 56"; MONDO calls it **alacrima, achalasia, and intellectual disability syndrome**
- `HP:0001394` (1 mention) - the report calls it "frequent, progressive"; HP calls it **Cirrhosis**
- `HP:0001508` (1 mention) - the report calls it "common"; HP calls it **Failure to thrive**
- `HP:0004313` (1 mention) - the report calls it "most"; HP calls it **Decreased circulating immunoglobulin concentration**
- `HP:0002850` (1 mention) - the report calls it "most"; HP calls it **Decreased circulating IgM concentration**
- `HP:0040218` (1 mention) - the report calls it "most"; HP calls it **Reduced total natural killer cell count**
- `NCIT:C603` (1 mention) - the report calls it "for hypogammaglobulinemia"; NCIT calls it **Isotretinoin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002726` (1 mention) - the report calls it "recurrent protozoan infection"; HP calls it **Recurrent Staphylococcus aureus infection**
- `UBERON:0000160` (1 mention) - the report calls it "intestine/GI tract"; UBERON calls it **intestine**, and lists "intestinal tract" among its other names
