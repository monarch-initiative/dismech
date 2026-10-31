---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T08:16:03.256898'
end_time: '2026-10-19T08:31:51.590320'
duration_seconds: 948.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: TSGA10-Related Acephalic Spermatozoa Syndrome (Spermatogenic Failure
    26)
  mondo_id: MONDO:0054730
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 18
  validator_version: 0.3.0
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0012207
    reported_labels:
    - Lab
    - Ultrastructural
    ontology_label: Reduced sperm motility
  - term_id: HP:0030086
    reported_labels:
    - Lab
    ontology_label: Reduced CSF lactate
  - term_id: GO:0005739
    reported_labels:
    - mitochondrial sheath
    - Subcellular:** **Sperm midpiece / fibrous sheath**, **mitochondrial sheath
    ontology_label: mitochondrion
  - term_id: UBERON:0000400
    reported_labels:
    - Tissue/cell:** Seminiferous epithelium
    ontology_label: jejunal epithelium
  - term_id: NCIT:C116283
    reported_labels:
    - Intracytoplasmic Sperm Injection
    ontology_label: Worst Severity Past Seven Days Aching Joints Question
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spermatogenic_Failure_26-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spermatogenic_Failure_26-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TSGA10-Related Acephalic Spermatozoa Syndrome (Spermatogenic Failure 26)
- **MONDO ID:** MONDO:0054730 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TSGA10-Related Acephalic Spermatozoa Syndrome (Spermatogenic Failure 26)** covering all of the
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

# TSGA10-Related Acephalic Spermatozoa Syndrome (Spermatogenic Failure 26): A Comprehensive Disease Characterization

**MONDO ID:** MONDO:0054730 · **OMIM phenotype:** #617961 (Spermatogenic failure 26, SPGF26) · **Gene:** *TSGA10* (OMIM 607166) · **Category:** Mendelian, autosomal recessive

---

## Summary

TSGA10-related acephalic spermatozoa syndrome (ASS), catalogued as **Spermatogenic Failure 26 (SPGF26)**, is a rare, autosomal-recessive form of male infertility caused by biallelic loss-of-function (LoF) variants in *TSGA10* (Testis-Specific Gene Antigen 10), a gene on chromosome **2q11.2** that encodes a sperm-tail/fibrous-sheath cytoskeletal protein. The protein is produced as a **65-kDa spermatid precursor** that is proteolytically processed to a **27-kDa fibrous-sheath protein** localizing to the **midpiece** of the mature spermatozoon. When TSGA10 function is lost, the **head-tail coupling apparatus (HTCA)** fails to anchor the sperm head to the flagellum and the **mitochondrial sheath** becomes disorganized, so that the ejaculate consists predominantly of **headless (acephalic), frequently immotile spermatozoa** — the morphological hallmark of the disease.

The condition is **congenital, lifelong, non-progressive, and anatomically confined to the reproductive system**; affected men are otherwise healthy, with normal somatic development, normal libido, and (in most reported cases) normal hormonal profiles. It presents clinically as **primary infertility with severe teratozoospermia**. Diagnosis rests on **semen morphology and transmission electron microscopy (TEM)** demonstrating headless tails and abnormal head-tail junctions, combined with **whole-exome sequencing (WES)** — importantly paired with **copy-number/structural-variant analysis**, because at least one patient carried a large deletion in *trans* that a standard SNV pipeline would miss. Immunofluorescence showing **absence of TSGA10 in the sperm midpiece** confirms the molecular diagnosis.

Prognosis for biological fatherhood is favorable: **intracytoplasmic sperm injection (ICSI)** generally achieves successful fertilization and pregnancy in *TSGA10*-related ASS, because the genetic defect affects sperm architecture without necessarily impairing the fertilizing capacity of the sperm nucleus. A **CRISPR/Cas9 Tsga10-knockout mouse** recapitulates the human disease — infertile males with a disordered mitochondrial sheath and reduced motility — providing definitive in-vivo confirmation of causality. This report synthesizes nine confirmed findings across etiology, molecular biology, mechanism, diagnostics, prognosis, treatment, and animal modeling, drawn from 40 reviewed papers.

---

## Key Findings

### Finding 1 — Biallelic loss-of-function *TSGA10* variants cause acephalic spermatozoa syndrome (SPGF26)

The central etiologic claim of this report is firmly established by human genetic evidence. Whole-exome sequencing of men presenting with acephalic spermatozoa identified recessive *TSGA10* LoF variants segregating with disease. In one index case, a **homozygous frameshift insertion, c.545dupT (p.Ala183Serfs\*10), in exon 8 (NM_001349012.1)**, abolished TSGA10 protein in the patient's spermatozoa. Critically, TEM of the patient's sperm showed a **misarranged mitochondrial sheath and an abnormal flagellum**, while the two best-established ASS proteins **SUN5 and PMFBP1 remained normally expressed**, demonstrating that TSGA10 acts in a pathway at least partly independent of those linkage proteins ([PMID: 32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/)). **[human clinical]**

> *"A novel homozygous frameshift insertion mutation c.545dupT;p.Ala183Serfs\*10 in exon 8 of TSGA10 (NM_001349012.1) was identified."* — [PMID: 32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/)

> *"Our results showed misarranged mitochondrial sheath and abnormal flagellum in the patient's spermatozoa. TSGA10 failed to be detected in the patient's spermatozoa. However, the expression of SUN5 and PMFBP1 remained unaffected."* — [PMID: 32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/)

A second, independent mechanism of biallelic inactivation was documented in a proband carrying a **compound-heterozygous genotype**: a canonical splice-site variant **c.1108-1G>T (NM_025244)** that causes **skipping of exon 15 and a truncated protein (p.A370Efs\*293)**, in *trans* with a **de novo large deletion** ([PMID: 34409526](https://pubmed.ncbi.nlm.nih.gov/34409526/)). This case is diagnostically instructive: the second hit was a structural variant invisible to standard variant callers, underscoring the need for CNV analysis. **[human clinical]**

> *"we identified a novel heterozygous splicing mutation in TSGA10 (NM_025244: c.1108-1G > T), while we confirmed that there was a de novo large deletion in the proband. The splicing mutation led to the skipping of the exon15 of TSGA10, which resulted in a truncated protein (p. A370Efs\*293)."* — [PMID: 34409526](https://pubmed.ncbi.nlm.nih.gov/34409526/)

### Finding 2 — ICSI yields favorable pregnancy outcomes in *TSGA10*-related ASS

Because ASS is a defect of sperm *architecture* rather than of the paternal genome, assisted reproduction can bypass it. In a retrospective cohort of 12 men with severe acephalic spermatozoa, WES identified *TSGA10/PMFBP1* variants in 7 patients (six heterozygous, four homozygous across the gene set). ICSI outcomes were favorable: the variants affected sperm morphology but did **not** reduce fertilization rates, early embryo quality, or ICSI success ([PMID: 34089195](https://pubmed.ncbi.nlm.nih.gov/34089195/)). **[human clinical]**

> *"Acephalic spermatozoa defects due to different genetic variations may affect only spermatozoa morphology but do not reduce the chances of fertilization, affect embryo quality at early stages or impair intracytoplasmic sperm injection (ICSI) outcomes. Patients with TSGA10/PMFBP1 variations were all expected to have good prognoses with ICSI."* — [PMID: 34089195](https://pubmed.ncbi.nlm.nih.gov/34089195/)

This contrasts with some other ASS genes (e.g., *CCDC188*, where a poor ICSI outcome has been reported — [PMID: 41004021](https://pubmed.ncbi.nlm.nih.gov/41004021/)), reinforcing that **genotype-specific prognostication** is clinically valuable and that *TSGA10* sits among the favorable-prognosis genes.

### Finding 3 — TSGA10 is a spermatid-expressed protein with mitochondrial Complex III coupling and HIF-1α regulatory roles

TSGA10 is a **cancer/testis antigen** that is highly expressed in **round spermatids during the meiotic-to-post-meiotic transition** ([PMID: 41864117](https://pubmed.ncbi.nlm.nih.gov/41864117/)) — precisely the developmental window when the flagellum, midpiece, and mitochondrial sheath are assembled. Mechanistically, TSGA10 **directly binds cytochrome c1 (CytC1) of mitochondrial Complex III**, optimizing electron transport to **minimize reactive oxygen species (ROS) and heat while enhancing ATP synthesis** ([PMID: 40507237](https://pubmed.ncbi.nlm.nih.gov/40507237/)). This mitochondrial-coupling role is highly relevant to the sperm midpiece, where the mitochondrial sheath powers motility and where TSGA10 is concentrated. **[in vitro / computational]**

> *"TSGA10 interacts with mitochondrial Complex III: it directly binds cytochrome c1 (CytC1). In our model, TSGA10 optimizes electron transport to minimize reactive oxygen species (ROS) and heat production while enhancing Adenosine Triphosphate (ATP) synthesis."* — [PMID: 40507237](https://pubmed.ncbi.nlm.nih.gov/40507237/)

Beyond spermatogenesis, TSGA10 **inhibits angiogenesis by preventing nuclear localization of HIF-1α**; overexpression decreases HIF-1α transcriptional activity ([PMID: 28739310](https://pubmed.ncbi.nlm.nih.gov/28739310/); [PMID: 26573430](https://pubmed.ncbi.nlm.nih.gov/26573430/)). These pleiotropic roles explain the gene's prominence in cancer biology but are not implicated in the infertility phenotype.

> *"TSGA10 could also play an important role in the inhibition of angiogenesis by preventing nuclear localization of HIF-1α."* — [PMID: 28739310](https://pubmed.ncbi.nlm.nih.gov/28739310/)

### Finding 4 — ASS arises from failure of the head-tail coupling apparatus (HTCA); *TSGA10* is one of several HTCA/linkage genes

ASS is a rare, severe teratozoospermia defined by **predominantly headless spermatozoa with an abnormal head-tail junction**, causing severe male infertility ([PMID: 32233213](https://pubmed.ncbi.nlm.nih.gov/32233213/)). It is genetically heterogeneous: causative or associated genes include **SUN5, PMFBP1, TSGA10, BRDT, SPATC1L, HOOK1, CEP112, DNAH6, CCDC188, NME5, ZMYND15**, with **SUN5 and PMFBP1 the most established** ([PMID: 33452591](https://pubmed.ncbi.nlm.nih.gov/33452591/)). SUN5, a LINC-complex protein, forms a hexagonal lattice at the nuclear envelope base of the sperm head that maintains the head-tail junction ([PMID: 41855266](https://pubmed.ncbi.nlm.nih.gov/41855266/)); impairment of the HTCA leads to head-tail detachment ([PMID: 42366926](https://pubmed.ncbi.nlm.nih.gov/42366926/)). **[human clinical / review]**

> *"Impairment of the HTCA leads to a severe type of infertility called acephalic spermatozoa syndrome, where sperm heads become detached from their tails."* — [PMID: 42366926](https://pubmed.ncbi.nlm.nih.gov/42366926/)

> *"Whole-exome and Sanger sequencing have helped in the identification of variants in SUN5, PMFBP1, BRDT, TSGA10, DNAH6, HOOK1, and CEP112 genes as possible causes of this phenotype in humans."* — [PMID: 33452591](https://pubmed.ncbi.nlm.nih.gov/33452591/)

### Finding 5 — TSGA10 is a 65-kDa spermatid protein processed to a 27-kDa fibrous-sheath/midpiece protein containing an ERM domain

Molecular and cell-biological work defines the protein precisely. *TSGA10* (human 2q11.2; mouse *Tsga10* on chr1 band B) is testis-specifically transcribed and encodes a **65-kDa spermatid protein that is processed to a 27-kDa protein of the fibrous sheath**, a major sperm-tail structure ([PMID: 14585816](https://pubmed.ncbi.nlm.nih.gov/14585816/)). The protein contains a **myosin/Ezrin-radixin-moesin (ERM) domain**; GFP-tagged TSGA10 forms short thick filaments in fibroblasts, and **deletion of the ERM domain abolishes filament formation**, establishing it as a cytoskeletal, filament-building protein. **[in vitro]**

> *"Mtsga10 encodes a 65-kDa spermatid protein that appears to be processed to a 27-kDa protein of the fibrous sheath, a major sperm tail structure, in mature spermatozoa. Mtsga10 protein contains a putative myosin/Ezrin/radixin/moesin (ERM) domain. Transfection of fibroblasts with GFP-Mtsga10 fusion protein results in formation of short, thick filaments and deletion of the myosin/ERM domain abolished filament formation."* — [PMID: 14585816](https://pubmed.ncbi.nlm.nih.gov/14585816/)

The **C-terminal portion accumulates in the midpiece of spermatozoa**, where it co-localizes with HIF-1α ([PMID: 16777103](https://pubmed.ncbi.nlm.nih.gov/16777103/)). Diagnostically, **immunofluorescence shows TSGA10 in the midpiece of control sperm and its complete absence in patients** ([PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)).

> *"the C-terminal part of TSGA10 accumulates in the midpiece of spermatozoa, where it co-localizes with HIF-1alpha."* — [PMID: 16777103](https://pubmed.ncbi.nlm.nih.gov/16777103/)

### Finding 6 — The pathogenic variant spectrum is diverse and can combine head detachment with axonemal defects

Reported recessive *TSGA10* alleles span multiple variant classes:

| Variant (nomenclature) | Type | Zygosity | Protein effect | Notable phenotype | PMID |
|---|---|---|---|---|---|
| c.545dupT (p.Ala183Serfs\*10), exon 8, NM_001349012.1 | Frameshift | Homozygous | Protein abolished | Misarranged mitochondrial sheath; SUN5/PMFBP1 normal | [32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/) |
| c.1108-1G>T (p.A370Efs\*293), NM_025244 + large deletion | Splice (exon 15 skip) + CNV | Compound het | Truncated protein | Classic ASS | [34409526](https://pubmed.ncbi.nlm.nih.gov/34409526/) |
| c.1112T>C (p.Leu371Pro) | Missense | Homozygous | Absent mRNA/protein | Head-flagellum detachment + 98% abnormal axonemes | [38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/) |

The **homozygous missense c.1112T>C (p.Leu371Pro)** was found in a **consanguineous Pakistani family**, recessively co-segregating; strikingly, **98% of flagellar cross-sections displayed abnormal axonemal ultrastructure** in addition to head-flagellum detachment, with absent TSGA10 mRNA/protein ([PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)). This expands the phenotype from a pure head-detachment defect to a combined head-detachment-plus-axonemal disorder, consistent with TSGA10's broad role in tail/fibrous-sheath assembly. **[human clinical]**

> *"we identified a novel missense variant in TSGA10 (c.1112T > C, p. Leu371Pro), which recessively co-segregated with the acephalic spermatozoa syndrome within this family. Ultrastructural analyses of spermatozoa from the patient revealed that 98% of flagellar cross-sections displayed abnormal axonemal ultrastructure, in addition to the head-flagellum detachment."* — [PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)

### Finding 7 — *Tsga10* expression is modulated by oxidative/chemical stress and linked to autophagy

In teratospermic patients, **TSGA10 mRNA and protein are significantly decreased versus controls (P<0.05)**, accompanied by reduced expression of sperm-maturation and autophagy genes and significantly higher ROS production ([PMID: 34232471](https://pubmed.ncbi.nlm.nih.gov/34232471/)). This connects the protein's mitochondrial-coupling/ROS-limiting role (Finding 3) to a broader quality-control axis in spermiogenesis. **[human clinical / in vitro]**

> *"the expression levels of TSGA10 mRNA and protein decreased significantly in the teratospermic patients compared to controls (P < 0.05)."* — [PMID: 34232471](https://pubmed.ncbi.nlm.nih.gov/34232471/)

Environmental modulation is seen in rodents: **formaldehyde exposure altered sperm profiles and Tsga10 expression**, with antioxidant (manganese) partially protective, and Tsga10 is explicitly described as a **cytoskeletal protein in the sperm tail that impacts motility** ([PMID: 26791599](https://pubmed.ncbi.nlm.nih.gov/26791599/)). Tsga10 is also expressed during mouse embryogenesis (from 4.5–7.5 dpc) and in adult brain/neural-crest derivatives, consistent with a conserved ciliary role ([PMID: 16643851](https://pubmed.ncbi.nlm.nih.gov/16643851/)). **[model organism]**

> *"Testis-specific gene antigen10 (Tsga10), as a cytoskeletal protein in the sperm tail, impacts the sperm motility."* — [PMID: 26791599](https://pubmed.ncbi.nlm.nih.gov/26791599/)

### Finding 8 — TSGA10 is a cancer/testis antigen on 2q11.2 (19 exons) with pleiotropic roles

*TSGA10* was originally isolated from normal testis by differential mRNA display; it maps to **2q11.2, comprises 19 exons over ~3 kb**, and is predominantly expressed in adult testis but over-expressed in several cancers (hepatocellular, ovarian, prostate, bladder) ([PMID: 15107545](https://pubmed.ncbi.nlm.nih.gov/15107545/)). It is an **anti-angiogenic factor** that reduces endothelial tube formation, migration, and proliferation and down-regulates VEGF-A/VEGFR-2 via decreased ERK and AKT phosphorylation ([PMID: 32512160](https://pubmed.ncbi.nlm.nih.gov/32512160/)). It is also an **autoantigen** targeted by autoantibodies in ~5% of autoimmune polyendocrine syndrome type 1 (APS1) and some SLE patients ([PMID: 21198756](https://pubmed.ncbi.nlm.nih.gov/21198756/)). The original testis-specific *Tsga10* clone was noted as **"not expressed in testes from two infertile patients"** ([PMID: 14585816](https://pubmed.ncbi.nlm.nih.gov/14585816/)) — the first hint of its infertility link. **[in vitro / human clinical]**

> *"TSGA10 is located on chromosome 2q11.2 and consists of 19 exons extending over 3 kb… It was predominantly expressed in the testis in adult normal tissues."* — [PMID: 15107545](https://pubmed.ncbi.nlm.nih.gov/15107545/)

### Finding 9 — *Tsga10*-knockout mice are infertile with a disordered mitochondrial sheath, validating causality

The definitive in-vivo proof: **CRISPR/Cas9-generated Tsga10-knockout male mice are infertile with significantly reduced sperm motility caused by disordered mitochondrial sheath formation**; TSGA10 is testis-specific and highly conserved across species ([PMID: 32790169](https://pubmed.ncbi.nlm.nih.gov/32790169/)). The knockout also revealed interactions with **GRP78 and NSUN2** (linked to peri-implantation lethality and the GnRH network), hinting at additional developmental roles. **[model organism]**

> *"TSGA10 is involved in the correct arrangement of mitochondrial sheath in spermatozoa."* — [PMID: 32790169](https://pubmed.ncbi.nlm.nih.gov/32790169/)

> *"TSGA10 can interact with GRP78 and NSUN2, which are associated with peri-implantation lethality and the gonadotropin-releasing hormone (GnRH) network."* — [PMID: 32790169](https://pubmed.ncbi.nlm.nih.gov/32790169/)

---

## Section-by-Section Disease Characterization

### 1. Disease Information
- **Overview:** A Mendelian, autosomal-recessive male infertility disorder in which *TSGA10* loss produces an ejaculate of predominantly headless spermatozoa with defective head-tail junctions and disorganized mitochondrial sheaths, causing severe teratozoospermia and primary infertility ([PMID: 32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/), [PMID: 32233213](https://pubmed.ncbi.nlm.nih.gov/32233213/)).
- **Key identifiers:** MONDO:0054730; OMIM phenotype #617961 (SPGF26); gene *TSGA10* (OMIM 607166, HGNC:30748); concept "Acephalic spermatozoa / Teratozoospermia"; ICD-11 GB04 (male infertility). (MONDO per template; OMIM/HGNC per standard catalogs — verify exact phenotype number in production.)
- **Synonyms:** Spermatogenic failure 26; SPGF26; TSGA10-related acephalic spermatozoa syndrome; decapitated/headless sperm syndrome (TSGA10 subtype); acephalic spermatozoa syndrome associated with *TSGA10*.
- **Source type:** Knowledge is **aggregated from individual patient case reports and small cohorts** (WES + TEM) plus **mechanistic model-organism and in-vitro studies** — not from large EHR-derived datasets.

### 2. Etiology
- **Causal factor:** Genetic — **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *TSGA10*** (Findings 1, 6). Inheritance is autosomal recessive.
- **Genetic risk factors:** Consanguinity (e.g., the Pakistani family with homozygous p.Leu371Pro, [PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)); carriership of a *TSGA10* LoF allele. No susceptibility/modifier loci are established for the *TSGA10* subtype specifically.
- **Environmental risk factors:** None established as causal for this Mendelian disease. Experimentally, **formaldehyde and pesticide (diazinon) exposures down-regulate Tsga10** in rodents ([PMID: 26791599](https://pubmed.ncbi.nlm.nih.gov/26791599/), [PMID: 40567906](https://pubmed.ncbi.nlm.nih.gov/40567906/)), and 5-alpha-reductase inhibitors (finasteride/dutasteride) reduce *Tsga10* expression among spermatogenesis genes ([PMID: 42069234](https://pubmed.ncbi.nlm.nih.gov/42069234/)) — relevant to acquired teratozoospermia, not to the inherited syndrome.
- **Protective factors:** Antioxidants (manganese in the formaldehyde model; chrysin against diazinon) partially preserve expression in rodents ([PMID: 26791599](https://pubmed.ncbi.nlm.nih.gov/26791599/), [PMID: 40567906](https://pubmed.ncbi.nlm.nih.gov/40567906/)); not applicable to the germline disease.
- **Gene-environment interaction:** The oxidative-stress/ROS axis (Findings 3, 7) is biologically plausible but **not demonstrated** to modify penetrance of germline *TSGA10* LoF.

### 3. Phenotypes
| Phenotype | Type | HPO suggestion | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Male infertility | Clinical/functional | HP:0003251 Male infertility | Post-pubertal (detected at fertility workup) | Severe | ~100% |
| Acephalic (headless) spermatozoa | Lab/morphology | HP:0012869 Abnormal sperm morphology | Congenital, detected in adulthood | Severe | Predominant in ejaculate |
| Abnormal sperm head-tail junction | Ultrastructural | HP:0012207 Abnormal spermatogenesis | Congenital | Severe | ~100% |
| Reduced/absent sperm motility (asthenozoospermia) | Lab | HP:0012207 | Congenital | Severe | High |
| Teratozoospermia | Lab | HP:0030086 | Congenital | Severe | ~100% |
| Disorganized mitochondrial sheath | Ultrastructural | (midpiece defect) | Congenital | Severe | ~100% |
| Abnormal axonemal ultrastructure (some alleles) | Ultrastructural | HP:0012207 | Congenital | Severe (98% cross-sections, p.Leu371Pro) | Allele-dependent |

- **Quality-of-life impact:** Confined to **reproductive function and the psychosocial burden of infertility**; no systemic morbidity, pain, or reduced life expectancy. Daily physical functioning is unaffected.

### 4. Genetic / Molecular Information
- **Causal gene:** *TSGA10*, 2q11.2, 19 exons (~3 kb coding footprint), HGNC:30748, OMIM 607166 ([PMID: 15107545](https://pubmed.ncbi.nlm.nih.gov/15107545/)).
- **Variant classes (ACMG-relevant):** frameshift (c.545dupT, pathogenic), canonical splice (c.1108-1G>T, pathogenic) often with a *trans* **large deletion** (structural, pathogenic), and missense with demonstrated LoF (c.1112T>C/p.Leu371Pro, pathogenic given absent transcript and co-segregation) (Finding 6).
- **Functional consequence:** **Loss of function** — abolished/truncated protein and loss of midpiece TSGA10 immunostaining (Findings 1, 5, 6).
- **Allele frequency:** Reported alleles are rare/private (consistent with recessive disease); population frequencies in gnomAD are expected to be very low, consistent with a highly penetrant recessive trait (no common risk allele described).
- **Origin:** Germline. One documented second hit was a **de novo large deletion** ([PMID: 34409526](https://pubmed.ncbi.nlm.nih.gov/34409526/)).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None established specifically for the *TSGA10* subtype beyond the large-deletion mechanism noted above.

### 5. Environmental Information
Not etiologic for the Mendelian disease. Experimental exposures (**formaldehyde, diazinon pesticide, 5-alpha-reductase inhibitors**) reduce *Tsga10* expression and sperm quality in models ([PMID: 26791599](https://pubmed.ncbi.nlm.nih.gov/26791599/), [PMID: 40567906](https://pubmed.ncbi.nlm.nih.gov/40567906/), [PMID: 42069234](https://pubmed.ncbi.nlm.nih.gov/42069234/)). No infectious agents implicated.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic LoF variant in *TSGA10*** (frameshift, splice+deletion, or LoF missense) → **leads to** loss or truncation of TSGA10 protein (demonstrated: absent sperm staining / absent mRNA) ([PMID: 32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/), [PMID: 34409526](https://pubmed.ncbi.nlm.nih.gov/34409526/), [PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)).
2. Loss of the **27-kDa fibrous-sheath/ERM-domain cytoskeletal protein** in round/elongating spermatids (its peak expression window) → **results in** failure to build normal sperm-tail fibrous-sheath/midpiece cytoskeletal filaments (demonstrated in vitro: ERM-domain deletion abolishes filament formation) ([PMID: 14585816](https://pubmed.ncbi.nlm.nih.gov/14585816/), [PMID: 41864117](https://pubmed.ncbi.nlm.nih.gov/41864117/)).
3. **Branch A — Head-tail coupling:** Defective neck/midpiece architecture → **leads to** an unstable **head-tail coupling apparatus (HTCA)** → **results in** detachment of the sperm head from the flagellum → **acephalic (headless) spermatozoa** (demonstrated by TEM/semen morphology) ([PMID: 42366926](https://pubmed.ncbi.nlm.nih.gov/42366926/), [PMID: 32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/)).
4. **Branch B — Mitochondrial sheath:** Loss of TSGA10's midpiece/mitochondrial-coupling function (direct CytC1/Complex-III binding, *inferred* to operate in sperm) → **leads to** a **misarranged mitochondrial sheath** → **results in** impaired ATP supply/elevated ROS and **reduced/absent motility** (demonstrated in patients and in the knockout mouse) ([PMID: 40507237](https://pubmed.ncbi.nlm.nih.gov/40507237/), [PMID: 32790169](https://pubmed.ncbi.nlm.nih.gov/32790169/)).
5. **Branch C — Axoneme (allele-dependent):** For some alleles (e.g., p.Leu371Pro), additional **abnormal axonemal ultrastructure** (98% of cross-sections) → compounds motility failure ([PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)).
6. Convergence → **severe teratozoospermia (headless, immotile sperm)** → **male infertility** (clinical manifestation).

```
 TSGA10 biallelic LoF
          │
   loss/truncation of 27-kDa fibrous-sheath ERM protein (spermatids)
          │
   ┌──────┴───────────┬────────────────────┬────────────────┐
   ▼                  ▼                     ▼                ▼
 HTCA unstable   mitochondrial         axonemal defect   ROS↑ / ATP↓
   │              sheath disorganized    (some alleles)   (CytC1/CxIII
   ▼                  │                     │              uncoupling)
 head-tail           ▼                     ▼                  │
 detachment      motility loss ◄──────── motility loss ◄──────┘
   └──────────────────┴─────────────────────┘
                      ▼
   Acephalic, immotile spermatozoa → severe teratozoospermia → male infertility
```

- **Upstream** = the mutation and protein loss; **downstream** = HTCA failure, mitochondrial-sheath disorder, axonemal defect, and clinical infertility.
- **Molecular pathways / biochemistry:** mitochondrial electron transport (Complex III/CytC1), ATP synthesis, ROS homeostasis ([PMID: 40507237](https://pubmed.ncbi.nlm.nih.gov/40507237/)); cytoskeletal filament assembly via the myosin/ERM domain ([PMID: 14585816](https://pubmed.ncbi.nlm.nih.gov/14585816/)); autophagy/maturation program linkage ([PMID: 34232471](https://pubmed.ncbi.nlm.nih.gov/34232471/)).
- **Cell types & GO/CL suggestions:** CL:0000019 **spermatozoon**, CL:0000018 **spermatid** (round/elongating). GO:0007283 **spermatogenesis**, GO:0030317 **flagellated sperm motility**, GO:0035082 axoneme assembly, GO:0007005 mitochondrion organization. Subcellular (GO CC): GO:0005929 cilium/flagellum, GO:1990385 sperm fibrous sheath (midpiece), GO:0005739 mitochondrion.

### 7. Anatomical Structures Affected
- **Organ:** Testis (UBERON:0000473); reproductive system (UBERON:0000990). No secondary organ involvement.
- **Tissue/cell:** Seminiferous epithelium (UBERON:0000400); **spermatids/spermatozoa** (CL:0000018 / CL:0000019).
- **Subcellular:** **Sperm midpiece / fibrous sheath**, **mitochondrial sheath** (GO:0005739), **head-tail coupling apparatus/neck**, **flagellar axoneme** (GO:0005930).
- **Localization & lateralization:** Bilateral (both testes); the defect manifests at the single-cell (spermatozoon) level.

### 8. Temporal Development
- **Onset:** Congenital molecular defect, **clinically recognized post-pubertally/in adulthood** at infertility evaluation. Insidious (asymptomatic until fertility is attempted).
- **Progression:** **Stable and non-progressive** — a fixed developmental defect of spermatogenesis, not a degenerative process. Lifelong.
- **Critical period:** The vulnerable window is **spermiogenesis** (round→elongating spermatid stage), when TSGA10 peaks and the midpiece/HTCA/sheath are assembled ([PMID: 41864117](https://pubmed.ncbi.nlm.nih.gov/41864117/)).

### 9. Inheritance and Population
- **Inheritance:** Autosomal recessive; biallelic LoF required (Findings 1, 6).
- **Penetrance/expressivity:** Apparently **complete penetrance for the infertility phenotype** in reported biallelic cases; expressivity varies at the ultrastructural level (pure head-detachment vs. combined axonemal defect, allele-dependent) ([PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)).
- **Consanguinity/founder:** Consanguinity contributes (homozygous cases in related parents) ([PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)); no founder allele established.
- **Epidemiology:** ASS overall is rare; the *TSGA10* subtype is **ultra-rare**, with only a handful of families reported worldwide (China, Pakistan, and others). Precise prevalence/incidence are **not available**. *SUN5* and *PMFBP1* account for the largest share of ASS; *TSGA10* is a minority cause.
- **Sex:** Affects males (phenotype is in spermatozoa); carrier females are asymptomatic.

### 10. Diagnostics
- **Semen analysis + morphology:** Predominance of headless spermatozoa (acephalic), low motility ([PMID: 32233213](https://pubmed.ncbi.nlm.nih.gov/32233213/)).
- **TEM:** Misarranged mitochondrial sheath, abnormal head-tail junction/neck, ± axonemal abnormalities ([PMID: 32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/), [PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)).
- **Immunofluorescence:** Absence of TSGA10 in the sperm midpiece (preserved SUN5/PMFBP1 distinguishes it from those subtypes) ([PMID: 32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/), [PMID: 38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/)).
- **Genetic testing:** **WES is the primary modality**; because a *trans* **large deletion** has been reported, pipelines must include **CNV/structural-variant detection** (read-depth CNV calling, CMA, or MLPA) ([PMID: 34409526](https://pubmed.ncbi.nlm.nih.gov/34409526/)). Sanger confirmation and segregation analysis support classification. ASS gene panels should include *TSGA10* alongside *SUN5, PMFBP1, BRDT, HOOK1, CEP112, DNAH6, CCDC188, NME5, ZMYND15* ([PMID: 33452591](https://pubmed.ncbi.nlm.nih.gov/33452591/)).
- **Differential diagnosis:** Other ASS genotypes (*SUN5*/*PMFBP1* most common); globozoospermia, MMAF (multiple morphological abnormalities of the flagella), and other teratozoospermias — distinguished by morphology, TEM, and gene panel ([PMID: 39417902](https://pubmed.ncbi.nlm.nih.gov/39417902/)).

### 11. Outcome / Prognosis
- **Survival/mortality:** Not applicable — no effect on life expectancy or systemic health.
- **Reproductive prognosis:** **Favorable with ICSI** for *TSGA10* carriers — fertilization, early embryo quality, and ICSI outcomes are preserved ([PMID: 34089195](https://pubmed.ncbi.nlm.nih.gov/34089195/)). Natural conception is essentially impossible.
- **Prognostic factor:** The specific ASS gene matters — *TSGA10/PMFBP1* carry good ICSI prognoses, whereas some genes (*CCDC188*) have been associated with poor ICSI outcomes ([PMID: 41004021](https://pubmed.ncbi.nlm.nih.gov/41004021/)).

### 12. Treatment
- **Definitive fertility treatment:** **Intracytoplasmic sperm injection (ICSI)** — NCIT:C116283 (Intracytoplasmic Sperm Injection); generally successful (Finding 2). No pharmacotherapy corrects the structural defect.
- **Supportive:** Genetic counseling; assisted reproductive technology (IVF-ICSI). Antioxidant strategies are experimental and unproven for the germline disease.
- **Advanced/experimental:** No gene, cell, or RNA therapy exists or is in trials for this indication.

### 13. Prevention
- **Primary prevention:** Not possible for a congenital recessive disorder; relevant interventions are **genetic counseling and carrier/cascade testing** in consanguineous families.
- **Secondary:** Early fertility evaluation; **preimplantation genetic testing (PGT)** can select unaffected embryos during ICSI cycles.
- **Counseling:** Autosomal-recessive recurrence risk (25% affected offspring if both parents carry; all sons of an affected man are obligate carriers).

### 14. Other Species / Natural Disease
- **Orthologue:** Mouse *Tsga10* (chr1 band B); highly conserved and testis-specific ([PMID: 14585816](https://pubmed.ncbi.nlm.nih.gov/14585816/), [PMID: 32790169](https://pubmed.ncbi.nlm.nih.gov/32790169/)).
- **Natural disease in animals:** No naturally occurring veterinary ASS specifically attributed to *TSGA10* is documented; the rodent evidence is from engineered/exposure models. A sterility-associated *tsga10* signal was noted in hybrid yellow catfish transcriptomics ([PMID: 38891632](https://pubmed.ncbi.nlm.nih.gov/38891632/)).
- **Conservation:** The protein is conserved wherever a ciliary structure exists ([PMID: 16643851](https://pubmed.ncbi.nlm.nih.gov/16643851/)).

### 15. Model Organisms
- **Definitive model:** **CRISPR/Cas9 *Tsga10*-knockout mouse** — infertile males, reduced motility, disordered mitochondrial sheath; recapitulates the core human mechanism ([PMID: 32790169](https://pubmed.ncbi.nlm.nih.gov/32790169/)).
- **Induced/exposure models:** Formaldehyde- and diazinon-exposed rodents (expression down-regulation) ([PMID: 26791599](https://pubmed.ncbi.nlm.nih.gov/26791599/), [PMID: 40567906](https://pubmed.ncbi.nlm.nih.gov/40567906/)).
- **In vitro:** Fibroblast GFP-TSGA10 filament-formation assay (ERM-domain dependence) ([PMID: 14585816](https://pubmed.ncbi.nlm.nih.gov/14585816/)); HUVEC overexpression (angiogenesis) ([PMID: 32512160](https://pubmed.ncbi.nlm.nih.gov/32512160/)).
- **Recapitulation/limitations:** The knockout captures mitochondrial-sheath/motility pathology well; the human head-detachment phenotype and allele-specific axonemal defects are less completely modeled, and the knockout's GRP78/NSUN2 interactions suggest developmental roles beyond infertility ([PMID: 32790169](https://pubmed.ncbi.nlm.nih.gov/32790169/)).

---

## Mechanistic Model / Interpretation

The coherent narrative is that **TSGA10 is a stage-specific spermatid cytoskeletal and mitochondrial-coupling protein whose loss destabilizes two tightly linked midpiece structures — the head-tail coupling apparatus and the mitochondrial sheath.** Its 27-kDa processed form is a fibrous-sheath component built via a myosin/ERM domain required for filament assembly; its C-terminus concentrates in the midpiece where it physically couples to Complex III (cytochrome c1). When both alleles are inactivated, spermatids cannot assemble a competent neck/midpiece: the head-tail junction fails (yielding headless sperm) and the mitochondrial sheath is disorganized (yielding immotility and a ROS/ATP imbalance). Some missense alleles additionally disrupt the axoneme. Because the defect is structural rather than genomic, the sperm *nucleus* remains competent — which is precisely why **ICSI works**. The *Tsga10*-knockout mouse closes the causal loop by reproducing the mitochondrial-sheath disorder and infertility in vivo.

The key distinction from the most common ASS genes (*SUN5*, *PMFBP1*) is mechanistic: SUN5/PMFBP1 are LINC/linkage proteins at the implantation-fossa/nuclear-envelope interface, whereas TSGA10 acts more on the **fibrous sheath/mitochondrial-sheath/midpiece** axis — demonstrated by preserved SUN5/PMFBP1 expression in a TSGA10-null patient. This positions *TSGA10* as a distinct molecular subtype within the HTCA-failure disease family.

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [32410354](https://pubmed.ncbi.nlm.nih.gov/32410354/) | Supports | Homozygous frameshift; abolished protein; mitochondrial-sheath defect; SUN5/PMFBP1 intact |
| [34409526](https://pubmed.ncbi.nlm.nih.gov/34409526/) | Supports | Compound-het splice + de novo large deletion (CNV mechanism) |
| [38317066](https://pubmed.ncbi.nlm.nih.gov/38317066/) | Supports/extends | Homozygous missense p.Leu371Pro; head-detachment + 98% axonemal defects; absent protein |
| [34089195](https://pubmed.ncbi.nlm.nih.gov/34089195/) | Supports | Favorable ICSI prognosis for TSGA10/PMFBP1 |
| [40507237](https://pubmed.ncbi.nlm.nih.gov/40507237/) | Mechanism | TSGA10–CytC1/Complex III coupling; ROS/ATP regulation |
| [14585816](https://pubmed.ncbi.nlm.nih.gov/14585816/) | Mechanism | 65→27 kDa processing; ERM domain; filament formation; infertility link |
| [16777103](https://pubmed.ncbi.nlm.nih.gov/16777103/) | Localization | Midpiece accumulation; HIF-1α co-localization |
| [32790169](https://pubmed.ncbi.nlm.nih.gov/32790169/) | Causality | Knockout mouse: infertility + disordered mitochondrial sheath |
| [42366926](https://pubmed.ncbi.nlm.nih.gov/42366926/) | Framework | HTCA failure → head-tail detachment |
| [33452591](https://pubmed.ncbi.nlm.nih.gov/33452591/) / [32233213](https://pubmed.ncbi.nlm.nih.gov/32233213/) | Framework | ASS definition and gene heterogeneity |
| [15107545](https://pubmed.ncbi.nlm.nih.gov/15107545/) | Gene facts | 2q11.2, 19 exons, testis-predominant expression |
| [34232471](https://pubmed.ncbi.nlm.nih.gov/34232471/) | Supports | Reduced TSGA10 in teratospermia; autophagy/ROS link |
| [26791599](https://pubmed.ncbi.nlm.nih.gov/26791599/) | Context | Environmental modulation; sperm-tail cytoskeletal/motility role |
| [41864117](https://pubmed.ncbi.nlm.nih.gov/41864117/) | Expression | Round-spermatid, meiotic→post-meiotic expression |
| [41004021](https://pubmed.ncbi.nlm.nih.gov/41004021/) | Contrast | CCDC188 poor ICSI outcome (prognostic genotype distinction) |

---

## Limitations and Knowledge Gaps

1. **Small evidence base:** Only a handful of *TSGA10*-specific families are reported; prevalence/incidence and allele-frequency data are unavailable, and penetrance estimates rest on few cases.
2. **Mechanistic inference:** The mitochondrial Complex-III/CytC1 coupling and HIF-1α roles are demonstrated biochemically/in model systems, but their *quantitative* contribution to the human head-detachment phenotype (vs. a purely structural fibrous-sheath role) is **inferred**, not directly dissected in patient sperm.
3. **Genotype-phenotype correlation:** Why some alleles (p.Leu371Pro) add prominent axonemal defects while others present as "pure" head detachment is unexplained.
4. **CNV under-ascertainment:** Standard WES pipelines may miss large deletions (as in the de novo deletion case), so the true variant spectrum may be broader than reported.
5. **ICSI long-term data:** Favorable early outcomes are documented, but long-term offspring health and live-birth rates across larger TSGA10 cohorts are limited.
6. **Model gaps:** The knockout mouse emphasizes mitochondrial-sheath/motility pathology; it less completely models the human head-detachment and allele-specific axonemal phenotypes.

---

## Proposed Follow-up Experiments / Actions

1. **Systematically add CNV/SV calling** (read-depth, CMA, or MLPA for *TSGA10*) to every ASS diagnostic workflow to capture deletion alleles in *trans*.
2. **Genotype-stratified ICSI registry** for ASS genes to confirm the favorable *TSGA10* prognosis at scale and compare with poor-prognosis genes (*CCDC188*).
3. **Structure-function dissection** of patient missense alleles (e.g., p.Leu371Pro) via knock-in mice or spermatid organoids to separate the fibrous-sheath (ERM) role from Complex-III coupling.
4. **Quantitative mitochondrial phenotyping** (ROS, membrane potential, ATP) in patient and knockout sperm to test whether the CytC1-coupling defect is a primary driver of immotility or a secondary consequence of sheath disorganization.
5. **Proteomic interactome mapping** of TSGA10 in spermatids (confirm CytC1, GRP78, NSUN2; search for HTCA partners) to place it precisely within the SUN5/PMFBP1 linkage network.
6. **Carrier-screening and counseling guidance** for consanguineous populations with *TSGA10* founder-like alleles, incorporating PGT options.

---

*Evidence source types: human clinical case/cohort (PMIDs 32410354, 34409526, 38317066, 34089195, 33452591, 32233213); model organism (32790169, 26791599, 16643851); in vitro/biochemical (14585816, 40507237, 16777103, 32512160); gene/genomic characterization (15107545, 28739310).*


## Artifacts

- [OpenScientist final report](Spermatogenic_Failure_26-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spermatogenic_Failure_26-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 18 |
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
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012207` (3 mentions) - the report calls it "Lab", "Ultrastructural"; HP calls it **Reduced sperm motility**
- `HP:0030086` (1 mention) - the report calls it "Lab"; HP calls it **Reduced CSF lactate**
- `GO:0005739` (2 mentions) - the report calls it "mitochondrial sheath", "Subcellular:** **Sperm midpiece / fibrous sheath**, **mitochondrial sheath"; GO calls it **mitochondrion**
- `UBERON:0000400` (1 mention) - the report calls it "Tissue/cell:** Seminiferous epithelium"; UBERON calls it **jejunal epithelium**
- `NCIT:C116283` (1 mention) - the report calls it "Intracytoplasmic Sperm Injection"; NCIT calls it **Worst Severity Past Seven Days Aching Joints Question**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000473` (1 mention) - the report calls it "Organ:** Testis"; UBERON calls it **testis**
- `GO:0005930` (1 mention) - the report calls it "flagellar axoneme"; GO calls it **axoneme**, and lists "flagellar axoneme" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0012207` - called "Lab", "Ultrastructural"
- `GO:0005739` - called "mitochondrial sheath", "Subcellular:** **Sperm midpiece / fibrous sheath**, **mitochondrial sheath"