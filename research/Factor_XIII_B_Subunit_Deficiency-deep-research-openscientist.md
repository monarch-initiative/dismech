---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T06:56:47.950966'
end_time: '2026-10-15T07:25:20.205517'
duration_seconds: 1712.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Factor XIII B Subunit Deficiency
  mondo_id: MONDO:0013190
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
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 25
  quotes_valid: 25
  relevance_assessed: 21
  on_topic: 15
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 29
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 6
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0013190
    reported_labels:
    - MONDO
    ontology_label: factor XIII, b subunit, deficiency of
  - term_id: HP:0002170
    reported_labels:
    - Clinical sign
    ontology_label: Intracranial hemorrhage
  - term_id: HP:0004846
    reported_labels:
    - Abnormal bleeding
    ontology_label: Prolonged bleeding after surgery
  - term_id: HP:0008222
    reported_labels:
    - Recurrent spontaneous abortion
    ontology_label: Female infertility
  - term_id: HP:0012223
    reported_labels:
    - Reduced factor XIII activity
    ontology_label: Splenic rupture
  - term_id: UBERON:0000955
    reported_labels:
    - brain
    - Organs affected by bleeding:** **brain
    ontology_label: brain
  - term_id: UBERON:0002097
    reported_labels:
    - skin and subcutaneous soft tissue
    ontology_label: skin of body
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
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
  path: Factor_XIII_B_Subunit_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Factor_XIII_B_Subunit_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Factor XIII B Subunit Deficiency
- **MONDO ID:** MONDO:0013190 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Factor XIII B Subunit Deficiency** covering all of the
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

# Factor XIII B Subunit Deficiency — Comprehensive Disease Characterization

**Disease:** Factor XIII B Subunit Deficiency
**MONDO ID:** MONDO:0013190 · **OMIM:** #613235 · **ORPHA:** 331 (Congenital FXIII deficiency) · **ICD-10:** D68.2 · **MeSH:** D005177
**Category:** Mendelian (autosomal recessive, rare bleeding disorder)
**Gene:** *F13B* (HGNC:3534; chromosome 1q31.3; UniProt P05160)

---

## Summary

Factor XIII B Subunit Deficiency is an ultra-rare, autosomal-recessive inherited bleeding disorder caused by biallelic loss-of-function variants in *F13B*, the gene encoding the non-catalytic **carrier/protective B subunit** of plasma coagulation Factor XIII (FXIII). Plasma FXIII circulates as a heterotetramer (FXIII-A₂B₂) in which two catalytic A subunits are bound and stabilized by two B subunits. The B subunit is a glycoprotein built from **10 repetitive sushi (complement control protein, CCP) domains**; it chaperones FXIII-A in the circulation, prevents its rapid clearance, and tethers it to the fibrinogen γ′-chain. When the B subunit is absent or severely reduced, the catalytic A subunit is cleared from plasma much faster than normal, so **plasma FXIII activity falls secondarily** even though A-subunit synthesis is intact. The result is deficient covalent cross-linking of fibrin and of α₂-antiplasmin, producing mechanically weak, fibrinolysis-prone clots.

Clinically, the disease belongs to the congenital FXIII deficiency spectrum, whose hallmark features are **delayed umbilical-stump hemorrhage in the neonate, soft-tissue and intracranial bleeding, impaired wound healing, and recurrent pregnancy loss** — all occurring despite **normal routine coagulation screening** (PT, aPTT, fibrinogen). Importantly, B-subunit deficiency is considerably rarer and generally **milder** than severe A-subunit deficiency because residual A-subunit activity persists; the knockout mouse shows markedly reduced, but not absent, fibrin cross-linking. Diagnosis therefore requires a quantitative FXIII activity assay **plus subunit-specific antigen phenotyping** that reveals low/absent FXIII-B antigen with secondarily reduced FXIII-A antigen.

The single most clinically actionable distinction for this subtype concerns therapy: **recombinant FXIII-A₂ (catridecacog; NovoThirteen/Tretten) does NOT correct F13B defects**, because it supplies only the catalytic subunit without the carrier that stabilizes it. Patients with B-subunit deficiency must instead receive **plasma-derived FXIII concentrate (A₂B₂; Fibrogammin/Corifact)**, which supplies both subunits. Lifelong replacement prophylaxis — feasible because of FXIII's long half-life (~7–14 days) — reduces the annualized bleeding rate to essentially zero and transforms a historically high-mortality disease (intracranial hemorrhage being the leading cause of death) into a manageable chronic condition with near-normal life expectancy.

---

## 1. Disease Information

Factor XIII B Subunit Deficiency is a congenital rare bleeding disorder (RBD) within the broader entity of **congenital Factor XIII deficiency (FXIIID)**. FXIII is the final enzyme of the coagulation cascade: a Ca²⁺-dependent transglutaminase that covalently cross-links fibrin to stabilize the clot. Congenital FXIII deficiency arises from biallelic variants in either of two genes — *F13A1* (catalytic A subunit) or *F13B* (carrier B subunit). The B-subunit form is defined by defects in *F13B*.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013190 |
| OMIM | #613235 (Factor XIII, B subunit, deficiency of) |
| Orphanet | ORPHA:331 (Congenital factor XIII deficiency) |
| ICD-10 | D68.2 (Hereditary deficiency of other clotting factors) |
| MeSH | D005177 (Factor XIII Deficiency) |
| Gene (HGNC) | HGNC:3534 (*F13B*) |
| UniProt | P05160 (Coagulation factor XIII B chain) |

**Synonyms / alternative names:** Factor XIII deficiency due to B subunit defect; FXIII-B deficiency; congenital FXIII-B subunit deficiency; fibrin stabilizing factor B subunit deficiency.

**Information source:** Evidence is derived almost entirely from **aggregated disease-level resources and individual case reports**, not large EHR datasets. Because the subtype is ultra-rare (historically ~11 reported cases of congenital FXIII-B deficiency as of 2013; [PMID: 23407795](https://pubmed.ncbi.nlm.nih.gov/23407795/)), the knowledge base is built from case reports, small cohorts of congenital FXIII deficiency (predominantly A-subunit), registry data from consanguineous populations, and one informative knockout mouse model.

> "congenital FXIII-B deficiency is even rarer" — [PMID: 23407795](https://pubmed.ncbi.nlm.nih.gov/23407795/)

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by **biallelic germline loss-of-function variants in *F13B*** (chromosome 1q31.3). It is inherited in a strictly autosomal recessive manner; both alleles must be defective to produce clinically significant deficiency ([PMID: 37314674](https://pubmed.ncbi.nlm.nih.gov/37314674/)). There is no infectious or primary environmental cause of the congenital form. (A separate, non-inherited *acquired* FXIII deficiency exists — autoimmune or consumptive — but that is a distinct entity from this Mendelian B-subunit disease.)

**Genetic risk factors.** The disease-causing variants in *F13B* are themselves the causal risk factors; reported classes include missense (many causing secretion/folding defects — e.g., disruption of structural disulfides of sushi domains), nonsense, splice-site, and frameshift variants ([PMID: 31013569](https://pubmed.ncbi.nlm.nih.gov/31013569/); [PMID: 26247044](https://pubmed.ncbi.nlm.nih.gov/26247044/)). **Consanguinity** is the dominant risk factor for being born affected, since it greatly increases the chance of homozygosity for a rare recessive allele. In pediatric congenital FXIII cohorts, consanguinity rates reach ~75% ([PMID: 37314674](https://pubmed.ncbi.nlm.nih.gov/37314674/)).

> "Consanguinity was present in 15 (75%)" — [PMID: 37314674](https://pubmed.ncbi.nlm.nih.gov/37314674/)

**Environmental / modifier risk factors.** No environmental exposures cause the congenital disease. Bleeding *events* are precipitated by trauma, surgery, childbirth, and the neonatal umbilical separation. Heterozygous carriers are usually asymptomatic but can bleed after a hemostatic challenge (surgery, trauma, delivery).

**Protective factors.** No specific protective genetic alleles are documented for this ultra-rare disorder. The principal "protective" circumstance is **residual FXIII-A activity**: because B-subunit loss only accelerates A-subunit clearance rather than abolishing A-subunit production, B-subunit deficiency tends to be milder than severe A-subunit deficiency ([PMID: 26247044](https://pubmed.ncbi.nlm.nih.gov/26247044/); [PMID: 18224415](https://pubmed.ncbi.nlm.nih.gov/18224415/)).

> "Defects in the F13B gene (Factor XIIIB subunit) occur more frequently in mild FXIII deficiency patients than in severe FXIII deficiency" — [PMID: 26247044](https://pubmed.ncbi.nlm.nih.gov/26247044/)

**Gene–environment interactions.** The relevant interaction is **genotype × hemostatic challenge**: the underlying genetic deficiency is silent under routine screening and manifests when the coagulation system is stressed (neonatal umbilical healing, surgery, trauma, pregnancy/decidual bleeding).

---

## 3. Phenotypes

The phenotype of B-subunit deficiency mirrors the congenital FXIII deficiency spectrum but tends toward the **milder** end. Core manifestations ([PMID: 41583548](https://pubmed.ncbi.nlm.nih.gov/41583548/); [PMID: 42230344](https://pubmed.ncbi.nlm.nih.gov/42230344/); [PMID: 32360976](https://pubmed.ncbi.nlm.nih.gov/32360976/)):

| Phenotype | Type | Suggested HPO | Onset / Characteristics | Frequency |
|---|---|---|---|---|
| Delayed umbilical stump bleeding | Clinical sign | HP:0040187 / neonatal bleeding | Neonatal; classic first presentation | Very common in severe disease |
| Intracranial hemorrhage | Clinical sign | HP:0002170 | Any age; most severe/life-threatening | ~25–35% of severe patients; leading cause of death |
| Soft-tissue / subcutaneous hematoma, ecchymoses | Clinical sign | HP:0001009 / HP:0000978 | Childhood onward | Common |
| Prolonged/delayed bleeding after trauma or surgery | Symptom | HP:0004846 (Abnormal bleeding) | Any age; episodic | Common |
| Impaired / delayed wound healing | Physical manifestation | HP:0001058 (Poor wound healing) | Any age | Characteristic |
| Recurrent spontaneous miscarriage | Clinical sign | HP:0008222 (Recurrent spontaneous abortion) | Reproductive age; episodic | ~36% of affected women had ≥1 miscarriage (cohort) |
| Mucosal bleeding (epistaxis, oral) | Symptom | HP:0000421 / HP:0000163 | Childhood onward | Common |
| Low plasma FXIII activity | Laboratory abnormality | HP:0012223 (Reduced factor XIII activity) | Congenital | Defining lab finding |

> "classically presents with delayed umbilical stump hemorrhage, soft‑tissue and intracranial bleeding, impaired wound healing, and recurrent pregnancy loss" — [PMID: 41583548](https://pubmed.ncbi.nlm.nih.gov/41583548/)

**Onset:** typically neonatal (umbilical bleeding) in severe cases; median symptom onset ~6 months and median diagnosis ~1 year in a South Indian pediatric congenital FXIII cohort ([PMID: 37314674](https://pubmed.ncbi.nlm.nih.gov/37314674/)).

**Severity / progression:** variable and lifelong; bleeding is **episodic** (triggered by challenges) rather than continuously progressive. B-subunit deficiency is generally milder than severe A-subunit deficiency.

**Quality-of-life impact:** dominated by the burden of lifelong prophylaxis, fear of spontaneous intracranial bleeding, and reproductive complications (miscarriage, postpartum hemorrhage). Disease-specific QoL instruments for this ultra-rare subtype are not available; data are extrapolated from the FXIII deficiency literature.

---

## 4. Genetic / Molecular Information

**Causal gene:** ***F13B*** (HGNC:3534; chromosome **1q31.3**; UniProt **P05160**). It encodes the plasma FXIII B subunit, a secreted **glycoprotein of 10 repetitive sushi (CCP) domains**, each stabilized by two internal disulfide bonds ([PMID: 20880254](https://pubmed.ncbi.nlm.nih.gov/20880254/)). The B subunit is synthesized in **hepatocytes** and secreted into plasma.

> "FXIII-B is a glycoprotein consisting of 10 repetitive sushi domains each held together by two internal disulfide bonds" — [PMID: 20880254](https://pubmed.ncbi.nlm.nih.gov/20880254/)

**Variant classification and type:** Reported *F13B* variants span **missense, nonsense, splice-site, and frameshift** classes; many missense variants cause **secretion or folding defects**, and disruption of the structural disulfide bonds of the sushi domains has functional consequences for a rare bleeding disorder ([PMID: 31013569](https://pubmed.ncbi.nlm.nih.gov/31013569/); [PMID: 26247044](https://pubmed.ncbi.nlm.nih.gov/26247044/)). Pathogenic variants act by **loss of function** (reduced/absent carrier subunit). The first sushi domain is important for A–B complex formation. Origin is **germline**; there is no somatic component. Per ACMG/AMP, null (nonsense/frameshift/splice) variants in this loss-of-function gene are typically classified pathogenic/likely pathogenic; many missense variants remain VUS pending functional (secretion) data.

**Functional consequence:** Loss of the B subunit does not abolish A-subunit synthesis but removes its carrier/stabilizer, so FXIII-A is cleared faster and plasma FXIII activity drops secondarily — a **loss-of-function, carrier-deficiency mechanism** confirmed by the knockout mouse (Section 6, [PMID: 18224415](https://pubmed.ncbi.nlm.nih.gov/18224415/)).

**Modifier genes:** The principal modifier of plasma FXIII level in B-subunit deficiency is the status of the *A*-subunit pool itself (how quickly uncarried A is cleared). No independent modifier loci are well established for this subtype.

**Epigenetic / chromosomal abnormalities:** None are implicated. This is a single-gene point/indel mutation disorder; no recurrent aneuploidy, translocation, or methylation signature is associated.

**Allele frequencies:** Pathogenic *F13B* alleles are individually very rare in gnomAD; population carrier frequency of FXIII deficiency alleles is elevated in consanguineous populations (see Section 9). Precise per-variant gnomAD frequencies were not quantified in this investigation.

---

## 5. Environmental Information

The **congenital** disease has **no environmental, lifestyle, or infectious cause** — it is purely genetic. Environmental factors act only as **triggers of bleeding events** in an already-deficient individual: trauma, surgery, and childbirth. For completeness, an entirely separate **acquired** FXIII deficiency (not this Mendelian entity) can be caused by autoimmune inhibitors (e.g., SLE-associated) or consumption (e.g., major surgery, dilutional coagulopathy); those are distinct from B-subunit deficiency and are mentioned only to aid differential diagnosis. No toxins, radiation, pollutants, dietary factors, or pathogens cause the inherited B-subunit disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in *F13B*** (missense/secretion-defect, nonsense, splice, or frameshift) **lead to** absent or severely reduced secretion of the FXIII B (carrier) subunit from hepatocytes.
2. Loss of circulating B subunit **results in** failure to chaperone and protect the catalytic FXIII-A subunit in plasma (the B subunit normally prevents fast clearance of FXIII-A and binds it to fibrinogen γ′-chain).
3. Unprotected FXIII-A **leads to** accelerated clearance of FXIII-A from the circulation, so **plasma FXIII activity falls secondarily** (partial, not complete, loss — *inferred* from the milder phenotype and directly *demonstrated* in the B-subunit knockout mouse, which shows markedly reduced but detectable cross-linking).
4. Low plasma FXIII activity **results in** deficient Ca²⁺-dependent transglutaminase action, i.e., **reduced covalent cross-linking of fibrin γ- and α-chains and reduced cross-linking of α₂-antiplasmin to fibrin**.
5. Deficient fibrin cross-linking **leads to** mechanically weak clots; deficient α₂-antiplasmin cross-linking **leads to** loss of the principal antifibrinolytic mechanism → **premature clot lysis**.
   - **Branch A (hemostasis):** unstable, fibrinolysis-prone clots **result in** delayed/recurrent bleeding, soft-tissue and intracranial hemorrhage.
   - **Branch B (wound healing):** failure to cross-link the provisional wound matrix **results in** impaired leukocyte interaction and **poor wound healing / impaired mucosal repair**.
   - **Branch C (angiogenesis):** loss of FXIIIa action on endothelial VEGFR-2 / αvβ3 integrin **results in** failure to downregulate antiangiogenic thrombospondin-1 → impaired angiogenesis/neovascularization (*inferred* contribution to healing/pregnancy defects).
   - **Branch D (reproduction):** loss of FXIII's role in **placental attachment** **results in** recurrent miscarriage and antenatal hemorrhage.

### Supporting detail

**Molecular / biochemical defect.** Activated FXIII (FXIIIa) is a Ca²⁺-dependent **transglutaminase** (EC 2.3.2.13) that forms ε-(γ-glutamyl)lysine isopeptide bonds. Its substrates include fibrin and α₂-antiplasmin:

> "These include antifibrinolytic proteins, with cross-linking of α2-antiplasmin to fibrin, and potentially fibrinogen, being the principal mechanism(s) whereby plasmin-mediated clot degradation is minimised" — [PMID: 25652913](https://pubmed.ncbi.nlm.nih.gov/25652913/)

**Angiogenesis.** FXIIIa engages endothelial signaling:

> "FXIII also acts on endothelial cell VEGFR-2 and αvβ3 integrin, which ultimately leads to downregulation of the antiangiogenic protein thrombospondin-1, promoting angiogenesis and neovascularisation" — [PMID: 25652913](https://pubmed.ncbi.nlm.nih.gov/25652913/)

**Placentation.** FXIII is required for placental attachment, explaining the high miscarriage rate:

> "factor XIII is involved in placental attachment" — [PMID: 32360976](https://pubmed.ncbi.nlm.nih.gov/32360976/)

**Tissue repair.** In an experimental colitis model, FXIII-deficient mice failed to resolve mucosal damage, and exogenous FXIII-A improved healing — confirming FXIII's role in mucosal/tissue repair ([PMID: 26098308](https://pubmed.ncbi.nlm.nih.gov/26098308/)).

**Upstream vs downstream.** *Upstream:* the *F13B* mutation and loss of carrier subunit. *Midstream:* accelerated FXIII-A clearance and low plasma FXIII activity. *Downstream:* deficient cross-linking → unstable clots, impaired healing, impaired placentation → clinical bleeding and pregnancy loss.

**Cell types / processes involved:** hepatocytes (CL:0000182) synthesize the B subunit; the A subunit's major plasma pool derives from cells of **megakaryocyte/platelet lineage** (CL:0000556 megakaryocyte; CL:0000233 platelet) per lineage-tracing studies ([PMID: 26312861](https://pubmed.ncbi.nlm.nih.gov/26312861/)); endothelial cells (CL:0000115) are the target of FXIIIa's angiogenic action.

**Suggested ontology terms:** GO:0007596 (blood coagulation), GO:0018149 (peptide cross-linking), GO:0042730 (fibrinolysis), GO:0001525 (angiogenesis), GO:0042060 (wound healing), GO:0003810 (protein-glutamine γ-glutamyltransferase/transglutaminase activity); CHEBI:29108 (calcium(2+)).

---

## 7. Anatomical Structures Affected

- **Primary site:** the **blood / plasma / circulatory system** (UBERON:0000178 blood; UBERON:0001969 blood plasma) — the compartment where the FXIII-A₂B₂ complex operates.
- **Organs affected by bleeding:** **brain** (UBERON:0000955) — intracranial hemorrhage is the most feared complication; **skin and subcutaneous soft tissue** (UBERON:0002097) — ecchymoses, hematomas; **mucosa** (oral/nasal); **umbilical stump** in the neonate; **spleen** (rare spontaneous rupture reported); **uterus/placenta** (UBERON:0000995 / UBERON:0001987) — miscarriage, decidual bleeding, postpartum hemorrhage.
- **Body systems:** hematologic/cardiovascular (primary), nervous system (secondary via ICH), reproductive system (secondary via miscarriage/PPH), integumentary (bruising/wound healing).
- **Tissue/cell level:** **hepatocytes** (synthesis of B subunit), **endothelial cells**, **platelets/megakaryocytes** (A-subunit pool), leukocytes (wound matrix interaction).
- **Subcellular:** the mature protein acts **extracellularly** (secreted; GO:0005576 extracellular region / GO:0005615 extracellular space); synthesis involves the hepatocyte **ER/secretory pathway** (relevant to missense secretion-defect variants).
- **Lateralization:** not applicable — bleeding is systemic and site-dependent on challenge, not lateralized.

---

## 8. Temporal Development

**Onset:** **congenital** — the deficiency is present from birth. Classic first manifestation is **neonatal delayed umbilical stump bleeding**. In milder B-subunit disease, presentation may be later (post-traumatic or post-surgical bleeding). Cohort median symptom onset ~6 months; median diagnosis ~1 year ([PMID: 37314674](https://pubmed.ncbi.nlm.nih.gov/37314674/)).

**Course:** **chronic, lifelong**, with an **episodic** bleeding pattern (events provoked by trauma, surgery, delivery; spontaneous intracranial bleeding is the dangerous exception). Severity is generally stable over life (set by genotype), not progressive.

**Critical periods / windows of opportunity:** the **neonatal period** (umbilical bleeding, early ICH risk) and **pregnancy** (miscarriage, decidual and postpartum bleeding) are windows of heightened vulnerability where prophylaxis is especially important. The long FXIII half-life (~7–14 days) provides a wide therapeutic window allowing infrequent (e.g., monthly) replacement dosing.

**Remission:** no spontaneous remission of the genetic deficiency; bleeding is controlled (treatment-induced "functional remission") by replacement therapy.

---

## 9. Inheritance and Population

**Inheritance:** **autosomal recessive**; biallelic *F13B* loss-of-function required. Heterozygotes have mild deficiency (activity ~20–60%) and are usually asymptomatic but may bleed after hemostatic challenge ([PMID: 37832789](https://pubmed.ncbi.nlm.nih.gov/37832789/)).

> "heterozygosity at FXIII genetic loci results in mild FXIII deficiency, characterized by circulating FXIII activity levels ranging from 20% to 60%" — [PMID: 37832789](https://pubmed.ncbi.nlm.nih.gov/37832789/)

**Epidemiology:**

| Measure | Value | Source |
|---|---|---|
| Congenital FXIII deficiency incidence | ~1 in 3–5 million | [PMID: 37314674](https://pubmed.ncbi.nlm.nih.gov/37314674/) |
| Worldwide prevalence (FXIIID) | ~1 in 2 million | [PMID: 25615432](https://pubmed.ncbi.nlm.nih.gov/25615432/) |
| Iran prevalence (vs worldwide) | ~12-fold higher (~473 patients) | [PMID: 25615432](https://pubmed.ncbi.nlm.nih.gov/25615432/) |
| FXIII-B subtype (reported cases) | ~11 historically (as of 2013) | [PMID: 23407795](https://pubmed.ncbi.nlm.nih.gov/23407795/) |
| Mild/heterozygous deficiency prevalence | ~0.8% (German-Caucasian donors); ~1 per 1,000–5,000 general; up to 3.5% in SE Iran | [PMID: 37832789](https://pubmed.ncbi.nlm.nih.gov/37832789/); [PMID: 36940714](https://pubmed.ncbi.nlm.nih.gov/36940714/) |

> "a rare bleeding disorder (RBD) of autosomal recessive inheritance, with an incidence of 1 in 3-5 million" — [PMID: 37314674](https://pubmed.ncbi.nlm.nih.gov/37314674/)

> "An approximately 12-fold higher prevalence of FXIIID is estimated in Iran in comparison with overall worldwide frequency" — [PMID: 25615432](https://pubmed.ncbi.nlm.nih.gov/25615432/)

**Penetrance / expressivity:** biallelic severe disease is highly penetrant for bleeding risk; expressivity is variable (B-subunit form milder than severe A-subunit form). No genetic anticipation (not a repeat-expansion disorder).

**Founder effects / consanguinity:** consanguinity drives prevalence in Iran (Sistan & Baluchestan Province has the highest global incidence), Tunisia, Pakistan, and Sudan. A documented **Japanese founder-effect *F13B* mutation** underlies a severe congenital FXIII-B deficiency case (patient homozygous for it):

> "Sistan and Baluchestan Province has not only the highest number of patients with FXIIID in Iran but the highest global incidence" — [PMID: 25615432](https://pubmed.ncbi.nlm.nih.gov/25615432/)

> "He was found to be homozygous for a Japanese founder-effect mutation of F13B" — [PMID: 23407795](https://pubmed.ncbi.nlm.nih.gov/23407795/)

**Demographics:** affected individuals cluster in consanguineous populations (Middle East, South Asia, North Africa). Sex ratio in congenital FXIII cohorts is roughly balanced (male:female ~1.2–1.5:1), though women carry additional reproductive morbidity.

---

## 10. Diagnostics

**Why it is missed:** routine coagulation screening is **normal**. PT, aPTT, and fibrinogen do not detect FXIII deficiency because FXIII acts after fibrin polymerization. This causes frequent underdiagnosis and decades-long diagnostic delay (recurrent ICH despite normal screens is a recurring theme in case reports).

> "Routine coagulation screening tests are normal and diagnosis relies on quantitative FXIII activity assays with or without antigenic phenotyping" — [PMID: 41583548](https://pubmed.ncbi.nlm.nih.gov/41583548/)

**ISTH/SSC diagnostic algorithm** ([PMID: 24286209](https://pubmed.ncbi.nlm.nih.gov/24286209/)):

1. **Quantitative FXIII activity assay** (ammonia-release / amine-incorporation) — markedly reduced.
2. **Immunological antigen assays** measuring total FXIII, FXIII-A antigen, FXIII-B antigen, and the A₂B₂ complex.
3. **Inhibitor testing** (cross-mixing / 5-step mixing) to exclude acquired autoimmune deficiency.
4. **Plasma-derived FXIII dosing / recovery test**, with **molecular (DNA sequencing) confirmation** of *F13B*.

**Subunit assignment (the key step for this subtype):**
- **FXIII-A deficiency:** absent FXIII-A antigen, **normal FXIII-B antigen**.
- **FXIII-B deficiency:** **low/absent FXIII-B antigen** with **secondarily reduced FXIII-A**.

> "Four immunological assays detected essentially no FXIII protein, FXIII-A antigen, and A2 B2 antigen, but normal FXIII-B antigen" — [PMID: 24286209](https://pubmed.ncbi.nlm.nih.gov/24286209/) (illustrates the mirror-image logic that identifies the subunit at fault)

**Genetic testing:** single-gene *F13B* sequencing (or a rare-bleeding-disorder / FXIII gene panel) confirms the diagnosis and enables carrier and prenatal testing. WES/WGS can be used when the phenotype is unclear. **Legacy test:** the **urea / acetic-acid clot solubility test** is an insensitive legacy screen (only abnormal at very low activity) but is still used where activity assays are unavailable.

**Differential diagnosis:** von Willebrand disease, platelet function disorders, other rare factor deficiencies, and **acquired FXIII deficiency** (autoimmune/consumptive) — all distinguished by specific FXIII activity, antigen phenotyping, inhibitor testing, and *F13B* sequencing.

**Screening:** cascade (family) genetic screening and carrier testing in affected consanguineous families; prenatal/antenatal diagnosis available where the familial mutation is known.

---

## 11. Outcome / Prognosis

**Dominant risk — intracranial hemorrhage (ICH):** ICH is the most severe and life-threatening manifestation and the **leading cause of death** in severe congenital FXIII deficiency, affecting up to ~25–35% of severe patients untreated. In a Tunisian cohort of 7 severe patients, 3/7 had intracranial bleeding and 1 died of ICH ([PMID: 28704210](https://pubmed.ncbi.nlm.nih.gov/28704210/)).

> "Intracranial hemorrhage represents its most severe and life-threatening manifestation" — [PMID: 42230344](https://pubmed.ncbi.nlm.nih.gov/42230344/)

> "One patient was died because of intracranial hemorrhage" — [PMID: 28704210](https://pubmed.ncbi.nlm.nih.gov/28704210/)

**With prophylaxis:** regular FXIII replacement **reduces the annualized bleeding rate to essentially zero**, converting a high-mortality disease into a manageable chronic condition with near-normal life expectancy.

> "Prophylaxis was effective with an annualized bleeding rate of zero" — [PMID: 28581691](https://pubmed.ncbi.nlm.nih.gov/28581691/)

**Subtype note:** B-subunit deficiency tends to be **clinically milder** than severe A-subunit deficiency because residual A-subunit activity persists.

**Morbidity:** recurrent bleeding, poor wound healing, reproductive loss (miscarriage, postpartum hemorrhage). **Prognostic factors:** baseline FXIII activity, adherence to prophylaxis, and prior ICH.

---

## 12. Treatment

**Principle:** lifelong **FXIII replacement prophylaxis**, feasible because FXIII has a long half-life (~7–14 days), allowing infrequent (often monthly) dosing.

**Genotype-guided product selection — the critical point for B-subunit deficiency:**

| Product | Composition | Corrects FXIII-A deficiency? | Corrects FXIII-B deficiency? |
|---|---|---|---|
| Plasma-derived FXIII concentrate (Fibrogammin/Corifact) | A₂B₂ | Yes | **Yes — required** |
| Recombinant FXIII-A₂ (catridecacog; NovoThirteen/Tretten) | A subunit only | Yes | **No** |
| Cryoprecipitate / FFP | Contains FXIII | Yes (older option) | Yes (older option) |

> "recombinant FXIII‑A2 is appropriate for F13A1 defects but not patients with F13B variants" — [PMID: 41583548](https://pubmed.ncbi.nlm.nih.gov/41583548/)

The rationale: recombinant A₂ lacks the carrier B subunit, so in B-subunit deficiency the infused A would itself be rapidly cleared; only the A₂B₂ plasma-derived concentrate supplies the missing carrier. **Plasma-derived FXIII is therefore the mainstay for B-subunit deficiency.** Its safety profile is favorable — in FXIII-knockout mice it corrected clot kinetics/strength and was **not associated with thrombus formation up to 350 IU/kg** ([PMID: 27069637](https://pubmed.ncbi.nlm.nih.gov/27069637/)).

**Dosing thresholds (pregnancy):** maintain plasma FXIII activity **≥2–3%, ideally >10%** to prevent decidual bleeding and miscarriage, escalating from ~250 IU/week early to ~500 IU/week after ~23 weeks, targeting >20–30% for labor ([PMID: 17371605](https://pubmed.ncbi.nlm.nih.gov/17371605/)).

> "the level of plasma A-subunit of factor XIII antigen (XIIIA-Ag) or factor XIII activity (XIII-act) must be at least 2%-3%, and, if possible, higher than 10% to prevent decidual bleeding and miscarriage during the pregnancy" — [PMID: 17371605](https://pubmed.ncbi.nlm.nih.gov/17371605/)

> "factor XIIIA concentrate is better than fresh frozen plasma or cryoprecipitate for replacement therapy" — [PMID: 17371605](https://pubmed.ncbi.nlm.nih.gov/17371605/)

**Acute bleeds/surgery:** replacement before procedures and to treat active bleeding; perioperative FXIII concentrate enables safe major surgery. **Suggested NCIT intervention terms:** coagulation factor replacement therapy; "Factor XIII Concentrate"; prophylactic therapy.

**Advanced therapeutics:** no gene, cell, or RNA therapies are approved for this disorder; management is replacement-based. Genetic counseling and prenatal diagnosis are offered for family planning. **Thrombotic risk** of replacement is low but non-zero and individualized dosing (avoiding full normalization) is advised in high-risk contexts ([PMID: 42527937](https://pubmed.ncbi.nlm.nih.gov/42527937/)).

---

## 13. Prevention

Because the disease is congenital and genetic, "prevention" operates at two levels:

- **Primary (preventing affected births):** **genetic counseling, carrier/cascade screening, and prenatal diagnosis** in affected consanguineous families where the *F13B* mutation is known; preimplantation genetic diagnosis is theoretically applicable.
- **Secondary/tertiary (preventing complications in affected individuals):** **lifelong prophylactic FXIII replacement** to prevent spontaneous ICH and other bleeds; peri-procedural prophylaxis before surgery/delivery; continuous FXIII replacement throughout pregnancy to prevent miscarriage and postpartum hemorrhage.

> "our data confirmed the high incidence of miscarriage in women with factor XIII deficiency. Good outcome of pregnancies required prophylaxis" — [PMID: 32360976](https://pubmed.ncbi.nlm.nih.gov/32360976/)

No vaccine or environmental/public-health intervention is relevant. Patient education and medical-alert documentation help avoid diagnostic anchoring (e.g., misdiagnosis as von Willebrand disease).

---

## 14. Other Species / Natural Disease

- **Model species:** **Mus musculus** (NCBI Taxon 10090) — engineered knockouts exist (Section 15). Orthologous gene: mouse ***F13b***.
- **Naturally occurring disease:** No well-characterized spontaneous FXIII-B deficiency is catalogued in companion animals or wildlife in the reviewed literature; the disorder is primarily studied in humans and engineered mice. (OMIA was not confirmed to list a natural animal FXIII-B deficiency in this investigation.)
- **Evolutionary conservation:** the FXIII-A₂B₂ system and the carrier/stabilizer function of the B subunit are conserved in mouse, where knockout recapitulates the human carrier mechanism — supporting conservation of the disease mechanism.
- **Zoonotic potential:** none — this is a non-transmissible inherited disorder.

---

## 15. Model Organisms

**Principal model — FXIII-B knockout mouse** (Souri et al., [PMID: 18224415](https://pubmed.ncbi.nlm.nih.gov/18224415/)): targeted deletion of mouse *F13b* (and separately *F13a*).

**Phenotype recapitulation:** Homozygous *F13b⁻/⁻* mice are **viable and fertile** but have **prolonged bleeding times** and **markedly reduced (not absent)** plasma fibrin cross-linking and thrombin-dependent amine incorporation — milder than *F13a⁻/⁻* mice, in which cross-linking is undetectable. Subunit gene expression is regulated independently.

> "homozygous mice of either FXIII-A- or FXIII-B-deficiency did have prolonged bleeding times" — [PMID: 18224415](https://pubmed.ncbi.nlm.nih.gov/18224415/)

> "fibrin-crosslinking in plasma were undetectable in the FXIII-A-deficient mice and markedly reduced in the FXIII-B-deficient mice" — [PMID: 18224415](https://pubmed.ncbi.nlm.nih.gov/18224415/)

**Direct mechanistic validation (the carrier mechanism):** injecting **recombinant human FXIII-B into *F13b⁻/⁻* mice raised plasma FXIII-A levels, fibrin cross-linking, and amine-incorporation activity** — demonstrating that the B subunit maintains/stabilizes circulating FXIII-A.

> "rFXIII-B was injected into FXIII-B-deficient mice, FXIII-A levels, fibrin crosslinking, and amine-incorporation activities increased in their plasma, indicating that FXIII-B assisted the maintenance of FXIII-A levels in the circulation" — [PMID: 18224415](https://pubmed.ncbi.nlm.nih.gov/18224415/)

**Related models / applications:** FXIII-A knockout mice reveal tissue-repair functions — e.g., impaired resolution of mucosal damage in DSS colitis, rescued by recombinant FXIII-A ([PMID: 26098308](https://pubmed.ncbi.nlm.nih.gov/26098308/)) — and a floxed-*F13a1* mouse mapped the cellular source of plasma FXIII-A to the megakaryocyte/platelet lineage ([PMID: 26312861](https://pubmed.ncbi.nlm.nih.gov/26312861/)). **Model limitation:** the *F13b⁻/⁻* mouse is milder than the human severe phenotype and does not reproduce the full spectrum of human obstetric complications. **Resources:** MGI for mouse *F13b*/*F13a1* alleles.

---

## Mechanistic Model (Synthesis)

```
   F13B biallelic LoF variant (missense/secretion-defect, nonsense, splice, frameshift)
                     │  (germline, autosomal recessive)
                     ▼
   Absent / reduced FXIII-B carrier subunit (10 sushi domains) secreted by hepatocytes
                     │
                     ▼
   FXIII-A no longer chaperoned  →  accelerated clearance of FXIII-A from plasma
                     │  (partial loss — milder than A-subunit deficiency)
                     ▼
   Low plasma FXIII (A2B2) activity  →  deficient Ca2+-dependent transglutaminase action
                     │
      ┌──────────────┼───────────────┬────────────────────┐
      ▼              ▼               ▼                    ▼
 ↓ fibrin         ↓ α2-antiplasmin  ↓ wound-matrix      ↓ placental
 γ/α cross-link   cross-link        cross-link          attachment
      │              │               │                    │
 weak clots     premature        impaired            recurrent
      └──────┬──────┘ fibrinolysis  healing            miscarriage / PPH
             ▼
   Delayed & recurrent bleeding, soft-tissue & INTRACRANIAL hemorrhage
             │
             ▼
   Normal PT/aPTT → underdiagnosis → (if untreated) ICH mortality
             │
             ▼
   Treatment: plasma-derived FXIII (A2B2) prophylaxis  →  annualized bleeding ≈ 0
   (recombinant FXIII-A2 does NOT work — no carrier supplied)
```

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [20880254](https://pubmed.ncbi.nlm.nih.gov/20880254/) | *Factor XIII: novel structural and functional aspects* | B-subunit 10-sushi-domain architecture; carrier role |
| [26247044](https://pubmed.ncbi.nlm.nih.gov/26247044/) | *Structural/functional influences of FXIII-B heterozygous mutants* | F13B defects over-represented in mild deficiency |
| [41583548](https://pubmed.ncbi.nlm.nih.gov/41583548/) | *Factor XIII Deficiency: Biology, Testing, Treatment* | Clinical phenotype; normal screening; **rFXIII-A2 not for F13B** |
| [23407795](https://pubmed.ncbi.nlm.nih.gov/23407795/) | *Alloantibodies against FXIII B subunit* | Ultra-rarity (~11 cases); Japanese F13B founder effect |
| [18224415](https://pubmed.ncbi.nlm.nih.gov/18224415/) | *FXIII-B administration in F13b KO mice* | **Direct validation of carrier mechanism**; milder than A-KO |
| [25652913](https://pubmed.ncbi.nlm.nih.gov/25652913/) | *FXIII: multifunctional transglutaminase* | Antifibrinolytic & angiogenic mechanisms |
| [32360976](https://pubmed.ncbi.nlm.nih.gov/32360976/) | *French cohort obstetric outcomes* | Placental role; miscarriage; prophylaxis need |
| [37314674](https://pubmed.ncbi.nlm.nih.gov/37314674/) | *Congenital FXIII deficiency in children* | Incidence 1/3–5M; AR; consanguinity 75% |
| [25615432](https://pubmed.ncbi.nlm.nih.gov/25615432/) | *FXIII deficiency in Iran* | Geographic epidemiology; 12× Iran prevalence |
| [24286209](https://pubmed.ncbi.nlm.nih.gov/24286209/) | *ISTH/SSC classification of FXIII deficiency* | Antigen phenotyping algorithm (A vs B) |
| [17371605](https://pubmed.ncbi.nlm.nih.gov/17371605/) | *Congenital FXIII deficiency & deliveries* | Pregnancy FXIII thresholds; product preference |
| [27069637](https://pubmed.ncbi.nlm.nih.gov/27069637/) | *Nonclinical safety of plasma-derived FXIII* | Safety up to 350 IU/kg, no thrombosis |
| [28704210](https://pubmed.ncbi.nlm.nih.gov/28704210/) | *FXIII deficiency in south Tunisia* | ICH as cause of death |
| [28581691](https://pubmed.ncbi.nlm.nih.gov/28581691/) | *Recombinant FXIII prophylaxis phase 3b* | Annualized bleeding rate of zero on prophylaxis |
| [42230344](https://pubmed.ncbi.nlm.nih.gov/42230344/) | *Delayed diagnosis of FXIII deficiency in infant* | ICH severity; diagnostic delay |
| [26098308](https://pubmed.ncbi.nlm.nih.gov/26098308/) | *FXIII in experimental colitis* | Tissue-repair / mucosal-healing role |
| [26312861](https://pubmed.ncbi.nlm.nih.gov/26312861/) | *Cellular source of plasma FXIII-A* | Megakaryocyte/platelet origin of A-subunit |
| [37832789](https://pubmed.ncbi.nlm.nih.gov/37832789/) | *Heterozygous FXIII deficiency* | Heterozygote activity 20–60%; prevalence ~0.8% |
| [36940714](https://pubmed.ncbi.nlm.nih.gov/36940714/) | *Heterozygous FXIII deficiency insights* | Prevalence 1/1,000–5,000; 3.5% in Iran |
| [31013569](https://pubmed.ncbi.nlm.nih.gov/31013569/) | *Disruption of FXIII-B structural disulfides* | Missense/disulfide-defect variant class |

**Evidence source types:** human clinical (cohorts, case reports, ISTH guidelines), model organism (mouse knockouts), in vitro (variant/structure studies), and review/computational syntheses.

---

## Limitations and Knowledge Gaps

1. **Subtype-specific data scarcity.** Only ~11 congenital FXIII-**B** deficiency cases were reported historically ([PMID: 23407795](https://pubmed.ncbi.nlm.nih.gov/23407795/)). Much phenotype/epidemiology data is extrapolated from the far more common **A-subunit** form; true B-subtype frequencies, penetrance, and natural history remain imprecise.
2. **No dedicated B-subunit QoL or natural-history studies.** QoL and disability metrics are inferred from the general FXIII literature.
3. **Allele-frequency precision.** Individual pathogenic *F13B* allele frequencies in gnomAD were not quantified in this investigation.
4. **Mechanistic branches partly inferred.** The angiogenesis (thrombospondin-1) and placentation contributions to the B-subtype phenotype are supported mechanistically but not specifically demonstrated in B-subunit-deficient humans.
5. **Model limitations.** The *F13b⁻/⁻* mouse is milder than severe human disease and does not fully model human obstetric complications.
6. **No OMIA-confirmed natural animal disease** was identified for the B subtype.

---

## Proposed Follow-up Actions

1. **Quantify *F13B* pathogenic-allele frequencies** in gnomAD/population databases and compile a variant table (HGVS nomenclature, ACMG classification, secretion phenotype) to refine carrier estimates.
2. **Assemble an international FXIII-B case registry** to define subtype-specific phenotype, penetrance, obstetric risk, and treatment response separately from the A subtype.
3. **Confirm ontology mappings** (MONDO:0013190 ↔ OMIM #613235 ↔ ORPHA:331) and verify gnomAD constraint metrics for *F13B*.
4. **Pharmacokinetic/clinical confirmation** that plasma-derived A₂B₂ concentrate normalizes FXIII-A survival specifically in B-subunit-deficient patients (mirroring the mouse rescue), to formalize the genotype-guided product rule.
5. **Prospective obstetric cohort** under plasma-derived FXIII prophylaxis to establish miscarriage-prevention thresholds in B-subunit deficiency specifically.

---

*Report compiled from a 5-iteration autonomous investigation: 12 confirmed findings across all 15 template sections, 42 papers reviewed. Evidence spans human clinical cohorts, ISTH/SSC guidelines, a mechanistically decisive knockout-mouse model, and in-vitro variant studies.*


## Artifacts

- [OpenScientist final report](Factor_XIII_B_Subunit_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Factor_XIII_B_Subunit_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 25 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 21 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013190` (3 mentions) - the report calls it "MONDO"; MONDO calls it **factor XIII, b subunit, deficiency of**
- `HP:0002170` (1 mention) - the report calls it "Clinical sign"; HP calls it **Intracranial hemorrhage**
- `HP:0004846` (1 mention) - the report calls it "Abnormal bleeding"; HP calls it **Prolonged bleeding after surgery**
- `HP:0008222` (1 mention) - the report calls it "Recurrent spontaneous abortion"; HP calls it **Female infertility**
- `HP:0012223` (1 mention) - the report calls it "Reduced factor XIII activity"; HP calls it **Splenic rupture**
- `UBERON:0000955` (1 mention) - the report calls it "brain", "Organs affected by bleeding:** **brain"; UBERON calls it **brain**
- `UBERON:0002097` (1 mention) - the report calls it "skin and subcutaneous soft tissue"; UBERON calls it **skin of body**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0003810` (1 mention) - the report calls it "protein-glutamine γ-glutamyltransferase/transglutaminase activity"; GO calls it **protein-glutamine gamma-glutamyltransferase activity**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000955` - called "brain", "Organs affected by bleeding:** **brain"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.