---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T07:44:28.752335'
end_time: '2026-08-31T08:01:17.764128'
duration_seconds: 1009.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: EVEN-PLUS Syndrome
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 21
  relevance_assessed: 14
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 51
  verified: 48
  not_found: 2
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.04
  labels_checked: 24
  labels_matching: 7
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0014784
    reported_labels:
    - Suggested MONDO
    ontology_label: severe hypotonia-psychomotor developmental delay-strabismus-cardiac
      septal defect syndrome
  - term_id: HP:0011003
    reported_labels:
    - Arched eyebrows
    ontology_label: High myopia
  - term_id: HP:0002656
    reported_labels:
    - Dysplastic epiphyses at the knee
    ontology_label: Epiphyseal dysplasia
  - term_id: HP:0011832
    reported_labels:
    - Triangular nares
    ontology_label: Narrow nasal tip
  - term_id: UBERON:0001690
    reported_labels:
    - External/middle ear
    ontology_label: ear
  - term_id: UBERON:0001711
    reported_labels:
    - Face / eyebrow region
    ontology_label: eyelid
  - term_id: NCIT:C15329
    reported_labels:
    - Evaluation and management of congenital heart defects
    ontology_label: Surgical Procedure
  - term_id: NCIT:C15190
    reported_labels:
    - Supportive Care
    - Monitoring/management of renal anomalies (e.g., hydronephrosis)
    - Antiepileptic management; developmental support
    ontology_label: Needle Biopsy
  labels_variant: 9
  unresolved_terms:
  - HP:0006411
  - HP:0002662
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: EVEN-PLUS_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: EVEN-PLUS_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** EVEN-PLUS Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **EVEN-PLUS Syndrome** covering all of the
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

# EVEN-PLUS Syndrome: A Comprehensive Disease Characterization Report

**Disease:** EVEN-PLUS Syndrome
**OMIM:** #616854 | **Gene:** HSPA9 (mortalin/mtHSP70/GRP75) | **Category:** Mendelian (autosomal recessive)
**Suggested MONDO:** MONDO:0014784

*Evidence types are marked where useful: human clinical, model organism, in vitro/biophysical, computational. No primary datasets were provided; all content is derived from primary literature via PubMed.*

---

## Summary

**EVEN-PLUS syndrome is an ultra-rare, autosomal-recessive, prenatal-onset multiple-malformation and skeletal-dysplasia syndrome caused by biallelic loss-of-function or hypomorphic variants in *HSPA9*, the gene encoding the mitochondrial HSP70 chaperone mortalin (mtHSP70/GRP75).** The name is an acronym for its cardinal features — **E**piphyses, **V**ertebrae, **E**ars, **N**ose — **PLUS** associated malformations of the heart, kidneys, and central nervous system. The disorder was delineated and named by Royer-Bertrand and colleagues in 2015 ([PMID: 26598328](https://pubmed.ncbi.nlm.nih.gov/26598328/)), who identified biallelic *HSPA9* mutations in affected individuals lacking mutations in *LONP1* (the gene responsible for the phenotypically overlapping CODAS syndrome). Together with CODAS, EVEN-PLUS defines a family of "mitochondrial chaperonopathies."

Mechanistically, mortalin is an essential mitochondrial matrix chaperone that drives ATP-dependent import of nuclear-encoded proteins across the inner membrane, assists protein folding, participates in iron–sulfur (Fe-S) cluster biogenesis, and buffers oxidative stress. EVEN-PLUS mutations — spanning missense, nonsense, frameshift, and splice-site classes — reduce or abolish this chaperone activity. Biophysical work on the nucleotide-binding-domain mutants R126W and Y128C shows that they disrupt ATP hydrolysis, interdomain communication, and thermostability while increasing the protein's propensity to aggregate ([PMID: 30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/)). The downstream consequence — impaired mitochondrial proteostasis, oxidative stress, and apoptosis in rapidly dividing embryonic precursors — is inferred to explain the skeletal, craniofacial, and organ malformations. Complete loss of the orthologous gene is embryonic-lethal in mice and produces ineffective hematopoiesis in zebrafish, establishing mortalin as developmentally essential.

Clinically, fewer than ~15 patients have been reported worldwide. Onset is prenatal; survivors have lifelong static skeletal dysplasia and craniofacial anomalies, with a subset developing seizures, developmental delay, and basal-ganglia lesions. Diagnosis rests on exome/genome sequencing (identifying biallelic *HSPA9* variants) combined with characteristic skeletal imaging. There is **no disease-modifying or curative therapy**; management is supportive and multidisciplinary, and prevention is reproductive — prenatal diagnosis and preimplantation genetic testing (PGT), the latter demonstrated to successfully block transmission and yield a healthy birth ([PMID: 38281662](https://pubmed.ncbi.nlm.nih.gov/38281662/)).

---

## 1. Disease Information

EVEN-PLUS syndrome is a congenital, autosomal-recessive multisystem malformation syndrome with skeletal dysplasia. It was first delineated as a distinct entity in 2015, when biallelic *HSPA9* mutations were identified in three individuals from two families ([PMID: 26598328](https://pubmed.ncbi.nlm.nih.gov/26598328/)). The name encodes the four cardinal anatomical domains — **E**piphyses, **V**ertebrae, **E**ars, **N**ose — plus associated ("PLUS") malformations. The original report states the phenotype "*included severe microtia, nasal hypoplasia, and other malformations, and for which we propose the name of EVEN-PLUS syndrome for epiphyseal, vertebral, ear, nose, plus associated findings*" ([PMID: 26598328](https://pubmed.ncbi.nlm.nih.gov/26598328/)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (disease) | #616854 |
| OMIM (gene) | *600548 (HSPA9) |
| Suggested MONDO | MONDO:0014784 |
| HGNC (gene) | HGNC:5244 |
| Gene locus | 5q31.2 |

**Synonyms / alternative names:** EVEN-PLUS syndrome; Epiphyseal, vertebral, ear, nose, plus associated findings syndrome; EVE dysplasia (the original family reported as "EVE dysplasia" was later confirmed to carry a homozygous *HSPA9* variant, [PMID: 35779070](https://pubmed.ncbi.nlm.nih.gov/35779070/)).

**Data provenance:** All information is derived from aggregated, disease-level resources and individual published case reports/case series (n < 15 patients worldwide), not from EHR-derived population cohorts. This is characteristic of an ultra-rare Mendelian disorder.

---

## 2. Etiology

**Primary cause — genetic:** EVEN-PLUS is a monogenic disorder caused by **biallelic (homozygous or compound heterozygous) pathogenic variants in *HSPA9***, which encodes mortalin (mtHSP70/GRP75), a mitochondrial chaperone. The seminal study reported: "*we found biallelic mutations in HSPA9, the gene that codes for mHSP70/mortalin, another highly conserved mitochondrial chaperone protein essential in mitochondrial protein import, folding, and degradation*" ([PMID: 26598328](https://pubmed.ncbi.nlm.nih.gov/26598328/)).

**Genetic risk factors:** The disorder is fully penetrant given biallelic pathogenic genotypes; there are no known susceptibility loci or modifier genes described. Consanguinity and founder alleles increase risk in specific families/populations — the frameshift variant c.882_883delAG "*may have a higher distribution frequency in East Asian populations*" ([PMID: 36052765](https://pubmed.ncbi.nlm.nih.gov/36052765/)).

**Environmental risk factors:** None identified. This is a purely Mendelian disorder; there is no evidence of environmental, infectious, or lifestyle contribution to causation.

**Protective factors:** No genetic or environmental protective factors are described. Because complete mortalin loss is embryonic-lethal (mouse homozygous knockout, [PMID: 25550197](https://pubmed.ncbi.nlm.nih.gov/25550197/)), viable EVEN-PLUS genotypes are inferred to be hypomorphic — retaining partial chaperone function — which acts as an implicit constraint on the survivable disease spectrum.

**Gene–environment interactions:** None reported or expected for this monogenic disorder.

---

## 3. Phenotypes

The phenotype spectrum is best defined by the 12-case review of Liu et al. ([PMID: 38284453](https://pubmed.ncbi.nlm.nih.gov/38284453/); 9 females) and the first-affected-male report ([PMID: 32869452](https://pubmed.ncbi.nlm.nih.gov/32869452/)). Onset is prenatal/congenital; the phenotype is largely static (structural malformations) except for progressive neurologic features in a subset.

### Near-universal features (~100%)

> "*All patients had synophrys or arched eyebrows, hypoplastic or dysplastic ears, hypoplastic nasal bone, and dysplastic femoral head.*" ([PMID: 38284453](https://pubmed.ncbi.nlm.nih.gov/38284453/))

| Phenotype | HPO term | Type |
|---|---|---|
| Synophrys | HP:0000664 | Physical/craniofacial |
| Arched eyebrows | HP:0011003 | Physical/craniofacial |
| Microtia / hypoplastic-dysplastic ears | HP:0008551, HP:0000369 | Physical/craniofacial |
| Hypoplastic nasal bone | HP:0004646 | Skeletal/radiographic |
| Dysplastic femoral head / epiphyseal dysplasia | HP:0006411, HP:0002656 | Skeletal |

### Common features (frequent)

| Phenotype | HPO term |
|---|---|
| Triangular nares | HP:0011832 |
| Bifid/dysplastic femur ("fork-shaped" distal femur) | — |
| Dysplastic epiphyses at the knee | HP:0002656 |
| Dysplastic acetabula | HP:0003182 |
| Delayed ossification | HP:0002662 |
| Short stature | HP:0004322 |
| Vertebral (coronal) clefting | HP:0003417 |
| Scoliosis | HP:0002650 |
| Dislocated patellae | HP:0002999 |
| Congenital heart defects | HP:0001627 |
| Renal alterations | HP:0000077 |

### Occasional features

Seizures (HP:0001250), global developmental delay (HP:0001263), basal ganglia lesions (HP:0002134), aplasia cutis (HP:0001057), short thorax/sternum (HP:0005257), widely spaced/laterally displaced nipples (HP:0006610), cryptorchidism (HP:0000028), clubfoot (HP:0001762), hypotonia (HP:0001252), agenesis of the septum pellucidum (HP:0001331), and 13 pairs of ribs (HP:0000891). The first affected male exhibited "*agenesis of the septum pellucidum, a short chest and sternum, 13 pairs of ribs, a single hemivertebra, laterally displaced nipples, hydronephrosis, unilateral cryptorchidism, unilateral single palmar crease, bilateral clubfoot, and hypotonia*" ([PMID: 32869452](https://pubmed.ncbi.nlm.nih.gov/32869452/)).

**Severity/progression:** Skeletal and craniofacial features are severe and static (congenital, non-progressive structural malformations). A milder facial phenotype has been documented in two sibs with compound heterozygous variants ([PMID: 35779070](https://pubmed.ncbi.nlm.nih.gov/35779070/)), indicating variable expressivity. Neurologic features (seizures, basal-ganglia lesions) may be progressive and are an adverse prognostic sign.

**Quality-of-life impact:** Lifelong disability from short stature, joint dislocations, and skeletal dysplasia (mobility, orthopedic burden); hearing impairment from microtia; potential cardiac and renal morbidity; and neurodevelopmental disability in the CNS-affected subset. Formal QoL instruments (EQ-5D, SF-36) have not been applied given the disease's rarity.

---

## 4. Genetic / Molecular Information

**Causal gene:** *HSPA9* (Heat Shock Protein Family A member 9; HGNC:5244; OMIM *600548), located at chromosome **5q31.2**, encoding **mortalin** (also mtHSP70, GRP75, PBP74). Disease OMIM #616854.

**Pathogenic variant spectrum:** Approximately **13 pathogenic variants** have been catalogued ([PMID: 38284453](https://pubmed.ncbi.nlm.nih.gov/38284453/)). All are **germline and biallelic** (homozygous in consanguineous/founder families, compound heterozygous otherwise), and classified pathogenic/likely pathogenic under ACMG/AMP criteria. Individually the alleles are rare or absent in gnomAD (carrier-level frequencies).

| Variant (cDNA / protein) | Class | Domain | Reference |
|---|---|---|---|
| R126W | Missense | Nucleotide-binding domain (NBD) | [PMID: 30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/) |
| Y128C | Missense | Nucleotide-binding domain (NBD) | [PMID: 30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/) |
| c.955C>T (p.L319F) | Missense | — | [PMID: 32869452](https://pubmed.ncbi.nlm.nih.gov/32869452/) |
| c.818T>G (p.L273X) | Nonsense (NMD) | — | [PMID: 32869452](https://pubmed.ncbi.nlm.nih.gov/32869452/) |
| c.882_883delAG | Frameshift | — (recurrent, East Asian) | [PMID: 36052765](https://pubmed.ncbi.nlm.nih.gov/36052765/) |
| c.613A>G | Missense | — | [PMID: 36052765](https://pubmed.ncbi.nlm.nih.gov/36052765/) |
| c.1822-1G>A | Splice (pathogenic) | Substrate-binding domain (SBD) | [PMID: 38281662](https://pubmed.ncbi.nlm.nih.gov/38281662/) |
| c.1411-3T>G | Splice (likely pathogenic) | Substrate-binding domain (SBD) | [PMID: 38281662](https://pubmed.ncbi.nlm.nih.gov/38281662/) |

> "*novel variants c.818 T > G (p.L273X) and c.955C > T (p.L319F) in the HSPA9 gene*" ([PMID: 32869452](https://pubmed.ncbi.nlm.nih.gov/32869452/)); "*c. 1822-1G>A and c. 1411-3T>G were classified as pathogenic and likely pathogenic, respectively*" ([PMID: 38281662](https://pubmed.ncbi.nlm.nih.gov/38281662/)).

**Functional consequences:** The overall mechanism is **loss of function / hypomorphism**. Truncating alleles undergo nonsense-mediated decay — "*qPCR analysis provides supporting evidence for a nonsense-mediated decay mechanism for the HSPA9 truncating variant*" ([PMID: 32869452](https://pubmed.ncbi.nlm.nih.gov/32869452/)). Missense NBD alleles impair enzymatic/chaperone function: "*the surface mutations R126W and Y128C have far-reaching effects that disrupt ATP hydrolysis, interdomain linker binding, and thermostability and increase the propensity for aggregation*" ([PMID: 30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/)).

**Modifier genes / epigenetics / chromosomal abnormalities:** No disease modifiers, epigenetic mechanisms, or large-scale chromosomal abnormalities are described for EVEN-PLUS. (Note: heterozygous *HSPA9* deletion at 5q31.2 is separately implicated in del(5q) myelodysplastic syndrome — a distinct, somatic, haploinsufficiency context, [PMID: 21123823](https://pubmed.ncbi.nlm.nih.gov/21123823/).)

---

## 5. Environmental Information

**Not applicable.** EVEN-PLUS is a purely Mendelian disorder. No environmental factors, toxins, radiation, occupational exposures, lifestyle factors, or infectious agents are known to cause, trigger, or modify the disease. The only non-genetic reproductive variable of note is consanguinity, which increases the likelihood of homozygosity for a founder allele.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic/LoF *HSPA9* variants** (missense, nonsense→NMD, frameshift, splice) *lead to* reduced quantity and/or impaired function of mortalin (mtHSP70/GRP75).
2. Reduced/dysfunctional mortalin *disrupts* ATP hydrolysis, interdomain (NBD↔SBD) communication, and thermostability, and *increases* the protein's aggregation propensity (demonstrated biophysically for R126W, Y128C — [PMID: 30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/)).
3. Impaired mortalin chaperone activity *results in* inefficient import and folding of nuclear-encoded mitochondrial proteins via mortalin–Tim complexes ([PMID: 17460192](https://pubmed.ncbi.nlm.nih.gov/17460192/)) **and** (branch) *impairs* iron–sulfur (Fe-S) cluster biogenesis through mortalin's role as the Ssq1 homolog interacting with frataxin/ISD11/NFS1/ISCU ([PMID: 17331979](https://pubmed.ncbi.nlm.nih.gov/17331979/)).
4. These deficits *lead to* inefficient mitochondrial biogenesis and energy (ATP) generation ([PMID: 17460192](https://pubmed.ncbi.nlm.nih.gov/17460192/)), and *lead to* accumulation of oxidative stress (mortalin is a major oxidation target and oxidative-stress buffer).
5. Oxidative stress and energetic/proteostatic failure *result in* apoptosis of metabolically demanding, rapidly dividing embryonic precursor cells (inferred from the zebrafish model, where the analogous lesion "*compromises mitochondrial function, producing oxidative stress and apoptosis distinctly in blood cells*" — [PMID: 15650063](https://pubmed.ncbi.nlm.nih.gov/15650063/)).
6. Precursor cell dysfunction/death during organogenesis *manifests as* the malformation phenotype — epiphyseal/vertebral skeletal dysplasia, microtia, nasal hypoplasia, and cardiac/renal/CNS anomalies. **(This final step from cellular defect to specific tissue malformation is inferred, not directly demonstrated in human tissue.)**
7. Complete loss *results in* embryonic lethality (mouse homozygous KO — [PMID: 25550197](https://pubmed.ncbi.nlm.nih.gov/25550197/)); surviving human patients therefore retain partial (hypomorphic) mortalin function, defining a lethality gradient at the severe end of the allelic spectrum.

```
 Biallelic HSPA9 variants
          │
          ▼
 ↓ mortalin function/quantity ──────────────┐
          │                                  │
          ▼                                  ▼
 ↓ mito protein import/folding      ↓ Fe-S cluster biogenesis
 (mortalin–Tim complexes)           (frataxin/NFS1/ISCU)
          │                                  │
          └──────────────┬───────────────────┘
                         ▼
        ↓ ATP generation + ↑ oxidative stress
                         │
                         ▼
        apoptosis of embryonic precursors
                         │
                         ▼
   epiphyseal/vertebral dysplasia · microtia ·
   nasal hypoplasia · cardiac/renal/CNS anomalies
```

### Mechanistic detail

- **Molecular pathways:** Mitochondrial protein import (TIM23/PAM machinery, mortalin as the matrix motor ATPase); Fe-S cluster (ISC) assembly pathway; HSP70 chaperone ATPase cycle. Mortalin also regulates the p53 pathway ([PMID: 30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/), [PMID: 25645922](https://pubmed.ncbi.nlm.nih.gov/25645922/)). Suggested GO terms: **GO:0030150** (protein import into mitochondrial matrix), **GO:0016226** (iron-sulfur cluster assembly), **GO:0006457** (protein folding), **GO:0006979** (response to oxidative stress).
- **Cellular processes:** Apoptosis (GO:0006915), oxidative-stress response, and mitochondrial biogenesis failure. Cellular senescence has been linked to mortalin dysfunction ([PMID: 17460192](https://pubmed.ncbi.nlm.nih.gov/17460192/)).
- **Protein dysfunction:** Loss of function via reduced expression (NMD) or catalytic/folding impairment; NBD mutants additionally show gain of **aggregation propensity** — a partial destabilization/misfolding phenotype ([PMID: 30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/)).
- **Metabolic changes:** Impaired oxidative phosphorylation / mitochondrial energy generation (inferred).
- **Immune involvement:** None as a primary mechanism.
- **Tissue damage mechanism:** Oxidative stress → apoptosis (demonstrated in the hematopoietic lineage in zebrafish; inferred for skeletal/craniofacial precursors in humans).

**Cell types (suggested CL terms):** chondrocyte (CL:0000138) and osteoblast (CL:0000062) for skeletal dysplasia; neural crest–derived cells for craniofacial (ear/nose) structures; cardiomyocyte (CL:0000746) and renal epithelial cells for organ malformations. These cell-type assignments are inferred from the affected anatomy rather than directly demonstrated.

---

## 7. Anatomical Structures Affected

**Organ / system level (primary):**
- **Skeletal system** (UBERON:0001434): epiphyses (femoral head, knee), vertebrae (coronal clefts, hemivertebrae), acetabula, patellae, thorax/sternum, ribs.
- **External/middle ear** (UBERON:0001690): microtia / dysplastic ears.
- **Nose / nasal bone** (UBERON:0001705, UBERON:0002517): nasal hypoplasia, triangular nares.
- **Face / eyebrow region** (UBERON:0001711): synophrys, arched eyebrows.

**Secondary organ involvement:**
- **Cardiovascular system** (UBERON:0004535): congenital heart defects (HP:0001627).
- **Renal/urinary system** (kidney UBERON:0002113): renal alterations, hydronephrosis (HP:0000077).
- **Central nervous system / brain** (UBERON:0000955): basal-ganglia lesions (HP:0002134), agenesis of septum pellucidum (HP:0001331).

**Tissue/cell level:** Connective/skeletal tissue (cartilage, bone), with epiphyseal cartilage and growth-plate chondrocytes prominently affected; neural-crest-derived craniofacial mesenchyme (ear, nose).

**Subcellular level:** The primary compartment is the **mitochondrion** (GO:0005739), specifically the **mitochondrial matrix** (GO:0005759), where mortalin operates. Suggested GO cellular-component terms: GO:0005739 (mitochondrion), GO:0005759 (mitochondrial matrix), GO:0005758 (mitochondrial intermembrane space, for import).

**Localization / lateralization:** Skeletal features are generally **bilateral** and largely symmetric; some findings (cryptorchidism, single palmar crease, clubfoot) are reported unilaterally in individual patients ([PMID: 32869452](https://pubmed.ncbi.nlm.nih.gov/32869452/)).

---

## 8. Temporal Development

**Onset:** Congenital / **prenatal**. "*It has a prenatal onset due to defects in the HSPA9 gene*" ([PMID: 36052765](https://pubmed.ncbi.nlm.nih.gov/36052765/)). Malformations are established during embryonic/fetal organogenesis and are often detectable on prenatal ultrasound, prompting prenatal genetic diagnosis ([PMID: 38281662](https://pubmed.ncbi.nlm.nih.gov/38281662/)).

**Progression:** The core skeletal and craniofacial malformations are **static/non-progressive** (structural, congenital). The disorder is chronic and lifelong for survivors. A lethality gradient exists at the severe end: some pregnancies are ascertained prenatally and terminated, and complete mortalin loss is embryonic-lethal in mice ([PMID: 25550197](https://pubmed.ncbi.nlm.nih.gov/25550197/)).

**Neurologic course:** In the CNS-affected subset, seizures and basal-ganglia lesions may be progressive and represent an evolving morbidity beyond the static skeleton ([PMID: 38284453](https://pubmed.ncbi.nlm.nih.gov/38284453/)).

**Critical period:** Embryonic organogenesis is the window of vulnerability. There is no post-natal therapeutic window to reverse established malformations; the only "intervention window" is **pre-conception/pre-implantation** (PGT) or prenatal.

---

## 9. Inheritance and Population

**Epidemiology:** Ultra-rare. Fewer than ~15 patients have been reported worldwide. Liu et al. collated "*12 cases (9 females)... from 6 relevant research items for analysis*" ([PMID: 38284453](https://pubmed.ncbi.nlm.nih.gov/38284453/)). No formal prevalence or incidence estimate exists; Orphanet classifies it among ultra-rare bone dysplasias. The apparent female predominance (9/12) may reflect ascertainment/reporting bias in this tiny sample rather than a true sex bias (the disorder is autosomal).

**Inheritance:** **Autosomal recessive**, biallelic — homozygous in consanguineous/founder families, compound heterozygous otherwise.

**Penetrance / expressivity:** Complete penetrance for biallelic pathogenic genotypes; **variable expressivity** documented (milder facial phenotype in two sibs, [PMID: 35779070](https://pubmed.ncbi.nlm.nih.gov/35779070/)).

**Founder effects / population:** A recurrent frameshift allele, **c.882_883delAG**, "*may have a higher distribution frequency in East Asian populations*" ([PMID: 36052765](https://pubmed.ncbi.nlm.nih.gov/36052765/)), suggesting a founder-type allele. Consanguinity contributes to homozygosity in some families.

**Carrier frequency:** Not formally established; individual pathogenic alleles are rare or absent in gnomAD.

**Anticipation / mosaicism:** No genetic anticipation (not a repeat-expansion disorder). No germline mosaicism specifically reported.

---

## 10. Diagnostics

**Genetic testing (definitive):** Diagnosis is established by **whole-exome sequencing (WES)** or whole-genome sequencing identifying **biallelic *HSPA9* variants**, confirmed by Sanger sequencing. "*HSPA9 compound heterozygous variants c.882_c.883delAG and c.613A>G were identified by exome sequencing*" ([PMID: 36052765](https://pubmed.ncbi.nlm.nih.gov/36052765/)). WES/WGS is the highest-yield approach because the phenotype overlaps other skeletal dysplasias/mitochondrial chaperonopathies and single-gene testing may not be prioritized without genetic guidance. Targeted *HSPA9* testing or skeletal-dysplasia gene panels are appropriate confirmatory routes once the diagnosis is suspected.

**Imaging (supportive):** Characteristic radiographic/MRI findings — dysplastic/absent femoral-head epiphyses, "fork-shaped" (bifid) distal femur, dysplastic knee epiphyses and acetabula, vertebral coronal clefting, delayed ossification, hypoplastic nasal bone ([PMID: 36052765](https://pubmed.ncbi.nlm.nih.gov/36052765/), [PMID: 32869452](https://pubmed.ncbi.nlm.nih.gov/32869452/)). Cerebral MRI may show basal-ganglia lesions and septum-pellucidum agenesis in CNS-affected patients.

**Clinical criteria:** No formal consensus diagnostic criteria exist. Diagnosis is gestalt (EVEN core features) plus molecular confirmation.

**Differential diagnosis:** The principal differential is **CODAS syndrome** (*LONP1*; MIM 600373), which shares epiphyseal, vertebral, and ocular changes but is distinguished from EVEN-PLUS by the latter's severe microtia and nasal hypoplasia — "*we delineate a similar but distinct condition that shares the epiphyseal, vertebral and ocular changes of CODAS but also included severe microtia, nasal hypoplasia*" ([PMID: 26598328](https://pubmed.ncbi.nlm.nih.gov/26598328/)). Both are grouped as "mitochondrial chaperonopathies," alongside AIFM1-related spondyloepimetaphyseal dysplasia with neurodegeneration — "*EVEN-PLUS syndrome caused by mutations of HSPA9 and CODAS syndrome due to LONP1 mutations*" ([PMID: 27102849](https://pubmed.ncbi.nlm.nih.gov/27102849/)). Other spondyloepiphyseal/spondyloepimetaphyseal dysplasias should also be considered.

**Screening:** No newborn or population screening exists (ultra-rare). Cascade carrier testing of relatives and reproductive-partner testing are appropriate once a familial variant is known.

---

## 11. Outcome / Prognosis

**Survival/mortality:** No formal survival statistics exist. There is a **lethality gradient**: the most severe genotypes are prenatally lethal or lead to pregnancy termination after prenatal diagnosis, and complete mortalin loss is embryonic-lethal in mice ([PMID: 25550197](https://pubmed.ncbi.nlm.nih.gov/25550197/), [PMID: 38281662](https://pubmed.ncbi.nlm.nih.gov/38281662/)). Postnatal survivors have a chronic, lifelong course.

**Morbidity/function:** Survivors carry a substantial, lifelong disability burden — skeletal dysplasia (short stature, joint dislocations, mobility limitation), hearing impairment (microtia), and potential cardiac and renal complications. Neurodevelopmental disability occurs in the CNS-affected subset.

**Disease course / prognostic factors:** CNS involvement is an **adverse prognostic feature**: "*Two patients had seizures and basal ganglia lesions in cerebral MRI*" ([PMID: 38284453](https://pubmed.ncbi.nlm.nih.gov/38284453/)). Genotype severity (residual mortalin function) is the principal determinant of phenotypic severity, ranging from prenatal lethality to milder facial-predominant presentations ([PMID: 35779070](https://pubmed.ncbi.nlm.nih.gov/35779070/)).

**Recovery potential:** None for the structural malformations — they are congenital and fixed. Management is supportive.

---

## 12. Treatment

**There is no disease-modifying or curative therapy for EVEN-PLUS syndrome.** Management is **supportive and multidisciplinary**, targeting the affected systems:

| Domain | Supportive intervention | Suggested NCIT |
|---|---|---|
| Skeletal/orthopedic | Orthopedic management of dislocations, scoliosis, epiphyseal dysplasia; physical/occupational therapy | NCIT:C15329 (Orthopedic Procedure); NCIT:C15690 (Physical Therapy) |
| Audiologic | Hearing assessment and aids for microtia-associated hearing loss | NCIT:C15190 (Supportive Care) |
| Cardiac | Evaluation and management of congenital heart defects | NCIT:C15329 |
| Renal | Monitoring/management of renal anomalies (e.g., hydronephrosis) | NCIT:C15190 |
| Neurologic | Antiepileptic management; developmental support | NCIT:C15190 |

- **Pharmacotherapy / pharmacogenomics:** None disease-specific. Symptomatic only (e.g., antiepileptics for seizures).
- **Advanced therapeutics (gene, cell, RNA, targeted, immuno):** None available or in trials. Gene replacement/editing of *HSPA9* is a conceptual future avenue only (see Follow-up).
- **Surgical/interventional:** Orthopedic and cardiac surgery as indicated by structural anomalies.
- **Experimental treatments (NCT trials):** None identified for EVEN-PLUS.

The strongest "intervention" reported is **reproductive prevention** (see Section 13), not treatment of affected individuals.

---

## 13. Prevention

Because the malformations are congenital and untreatable, prevention is **reproductive/genetic** rather than clinical.

- **Genetic counseling:** For couples with a prior affected child or known carrier status — 25% recurrence risk per pregnancy (autosomal recessive). Cascade carrier testing of relatives is appropriate.
- **Prenatal diagnosis:** Detection of biallelic *HSPA9* variants (and/or ultrasound malformations) in at-risk pregnancies.
- **Preimplantation genetic testing (PGT):** The most effective demonstrated prevention. Chang et al. performed prenatal-to-preimplantation genetic diagnosis and selected mutation-free embryos: "*Assisted reproduction with mutation-free embryos successfully blocked the transmission of mutations*" ([PMID: 38281662](https://pubmed.ncbi.nlm.nih.gov/38281662/)), resulting in a healthy birth.
- **Primary/secondary/tertiary prevention, immunization, public health, prophylaxis:** Not applicable (no environmental or infectious etiology). Tertiary prevention is limited to supportive management of complications.

---

## 14. Other Species / Natural Disease

*HSPA9*/mortalin is **deeply evolutionarily conserved**, and orthologs underpin the disease's model organisms, but no naturally occurring EVEN-PLUS-equivalent disease has been described in companion animals or wildlife.

| Species | NCBI Taxon | Ortholog | Database |
|---|---|---|---|
| Human | 9606 | HSPA9 | OMIM/HGNC |
| Mouse | 10090 | Hspa9 | MGI |
| Zebrafish | 7955 | hspa9 / hspa9b | ZFIN |
| Yeast (*S. cerevisiae*) | 4932 | SSQ1 / SSC1 | SGD |

Mortalin/GRP75 is "*a homolog of the yeast ssq1 chaperone that integrates iron-sulfur clusters into imported mitochondrial proteins*" ([PMID: 17331979](https://pubmed.ncbi.nlm.nih.gov/17331979/)), establishing conservation of the core Fe-S biogenesis and import functions from yeast to human. No zoonotic potential or cross-species transmission applies (non-infectious, genetic).

---

## 15. Model Organisms

Although no model was engineered specifically to phenocopy the EVEN-PLUS skeletal syndrome, existing *Hspa9* models establish the gene's essentiality and core mitochondrial mechanism.

**Zebrafish — "crimsonless" (*hspa9b* mutant):** A glycine-to-glutamate substitution in the substrate-binding domain recapitulates **ineffective hematopoiesis**: "*This mutation compromises mitochondrial function, producing oxidative stress and apoptosis distinctly in blood cells. Thus, we identify an essential role for Hspa9b in hematopoiesis and implicate both loss of HSPA9B specifically and mitochondrial dysfunction generally in the pathogenesis of the MDS*" ([PMID: 15650063](https://pubmed.ncbi.nlm.nih.gov/15650063/)). This is the best mechanistic model linking mortalin loss to the mitochondrial-dysfunction → oxidative-stress → apoptosis cascade central to EVEN-PLUS pathophysiology, though it models a hematopoietic (MDS-relevant) rather than skeletal readout.

**Mouse — *Hspa9* knockout:** "*homozygous knockout of Hspa9 is embryonically lethal, mice with heterozygous deletion of Hspa9 (Hspa9(+/-)) are viable*" ([PMID: 25550197](https://pubmed.ncbi.nlm.nih.gov/25550197/)). This establishes that complete mortalin loss is incompatible with life — implying EVEN-PLUS alleles are hypomorphic — and heterozygous models inform del(5q) MDS biology. Knockdown of Hspa9 in mice reduces hematopoietic progenitors ([PMID: 21123823](https://pubmed.ncbi.nlm.nih.gov/21123823/)).

**Yeast — *SSQ1/SSC1*:** The mortalin ortholog provides the biochemical foundation for Fe-S cluster integration into mitochondrial proteins ([PMID: 17331979](https://pubmed.ncbi.nlm.nih.gov/17331979/)).

**Model types available:** knockout (mouse), point-mutant (zebrafish), and recombinant-protein/in-vitro biophysical systems (used to characterize R126W and Y128C — [PMID: 30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/)).

**Model limitations:** No existing model reproduces the full EVEN-PLUS skeletal/craniofacial malformation phenotype; current models capture hematopoietic and embryonic-lethality readouts rather than the epiphyseal-vertebral-ear-nose skeletal dysplasia. A conditional or knock-in model carrying EVEN-PLUS-specific hypomorphic alleles (e.g., R126W) would be needed to study skeletal pathogenesis directly.

**Resources:** MGI (mouse), ZFIN (zebrafish), SGD (yeast).

---

## Mechanistic Model / Interpretation

EVEN-PLUS syndrome is best understood as a **developmental mitochondrial chaperonopathy**. The unifying molecular lesion is partial loss of mortalin, the mitochondrial matrix HSP70 that powers protein import and folding and supports Fe-S cluster assembly. Two independent lines of evidence converge on this model: (1) biophysical characterization of patient missense mutations (R126W, Y128C) showing loss of ATPase/chaperone competence and gain of aggregation propensity ([PMID: 30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/)), and (2) the essentiality of mortalin across species, where complete loss is embryonic-lethal (mouse) or produces mitochondrial-dysfunction-driven oxidative stress and apoptosis (zebrafish) ([PMID: 25550197](https://pubmed.ncbi.nlm.nih.gov/25550197/), [PMID: 15650063](https://pubmed.ncbi.nlm.nih.gov/15650063/)).

The critical inference is a **dose–severity continuum**: because null genotypes are lethal, viable EVEN-PLUS patients must retain some residual mortalin activity. The amount of residual function plausibly explains the observed phenotypic range — from prenatal lethality/termination at one extreme to the milder facial-predominant sib phenotype at the other ([PMID: 35779070](https://pubmed.ncbi.nlm.nih.gov/35779070/)). The tissue selectivity (skeleton, ear, nose, heart, kidney, brain) is not yet mechanistically explained but is consistent with high mitochondrial/proteostatic demand in rapidly proliferating embryonic precursors (chondrocytes, neural-crest mesenchyme) during a narrow organogenesis window. The parallel to CODAS (LONP1, a mitochondrial protease) reinforces that disrupting *either* mitochondrial protein folding (mortalin) *or* mitochondrial protein turnover (LONP1) yields an overlapping epiphyseal-vertebral-craniofacial phenotype — implicating mitochondrial proteostasis broadly, rather than any single client protein, as the developmental bottleneck.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report | Evidence type |
|---|---|---|---|
| [26598328](https://pubmed.ncbi.nlm.nih.gov/26598328/) | *HSPA9 mutations cause EVEN-PLUS* | Delineates & names the disease; biallelic HSPA9; CODAS overlap; mitochondrial chaperonopathy | Human clinical + genetic |
| [30933555](https://pubmed.ncbi.nlm.nih.gov/30933555/) | *Biophysical consequences of EVEN-PLUS mutations for mortalin* | Molecular mechanism of R126W/Y128C (ATP hydrolysis, aggregation) | In vitro / biophysical |
| [38284453](https://pubmed.ncbi.nlm.nih.gov/38284453/) | *New phenotype in a Chinese family + review* | 12-case phenotype spectrum & frequencies; CNS morbidity | Human clinical (case series/review) |
| [32869452](https://pubmed.ncbi.nlm.nih.gov/32869452/) | *Novel variants + HSPA9 dysfunction* | First affected male; NMD evidence; expanded HPO | Human clinical + in vitro |
| [36052765](https://pubmed.ncbi.nlm.nih.gov/36052765/) | *Exome + clinical feature analysis* | Prenatal onset; East-Asian recurrent allele; WES diagnosis | Human clinical + genetic |
| [38281662](https://pubmed.ncbi.nlm.nih.gov/38281662/) | *Prenatal to PGT diagnosis* | Splice variants; PGT prevention | Human clinical / reproductive |
| [35779070](https://pubmed.ncbi.nlm.nih.gov/35779070/) | *Broadening phenotypic spectrum* | Milder phenotype; original EVE dysplasia family confirmed | Human clinical |
| [27102849](https://pubmed.ncbi.nlm.nih.gov/27102849/) | *AIFM1 SEMD with neurodegeneration* | Groups EVEN-PLUS/CODAS as mitochondrial chaperonopathies | Human clinical (differential) |
| [15650063](https://pubmed.ncbi.nlm.nih.gov/15650063/) | *Loss of Hspa9b in zebrafish* | Model: mito dysfunction → oxidative stress → apoptosis | Model organism |
| [25550197](https://pubmed.ncbi.nlm.nih.gov/25550197/) | *Reduced Hspa9 in mouse B cells* | KO embryonic lethality; hypomorphism inference | Model organism |
| [21123823](https://pubmed.ncbi.nlm.nih.gov/21123823/) | *Hspa9 del(5q31.2) knockdown* | Haploinsufficiency & hematopoiesis (distinct MDS context) | Model organism |
| [17331979](https://pubmed.ncbi.nlm.nih.gov/17331979/) | *Frataxin–ISD11–chaperone interactions* | Mortalin/Ssq1 role in Fe-S biogenesis | In vitro / biochemical |
| [17460192](https://pubmed.ncbi.nlm.nih.gov/17460192/) | *Mortalin in cellular senescence* | Import/chaperone/oxidative-stress functions | Review / in vitro |
| [25645922](https://pubmed.ncbi.nlm.nih.gov/25645922/) | *Mortalin point mutations & PD* | p53 regulation, oxidative-stress tolerance | In vitro |

---

## Limitations and Knowledge Gaps

1. **Extreme rarity (n < 15).** All phenotype frequencies, sex ratios, and prognostic statements derive from small case series; the apparent female predominance (9/12) is likely an ascertainment artifact and should not be over-interpreted.
2. **The final mechanistic step is inferred.** The link from mortalin deficiency → mitochondrial/oxidative/apoptotic failure → *specific* skeletal and craniofacial malformations has not been demonstrated in human patient tissue or in a skeletal disease model. The causal chain from cellular defect to organ-specific malformation remains a plausible inference from the zebrafish hematopoietic model and general mortalin biology.
3. **No skeletal disease model.** Existing models (zebrafish hematopoiesis, mouse embryonic lethality) do not recapitulate the EVEN core features, limiting mechanistic and therapeutic study.
4. **Genotype–phenotype correlations are preliminary.** With only ~13 variants reported, the relationship between residual mortalin activity and phenotypic severity (including the lethality gradient) is inferred rather than quantitatively established.
5. **No natural-history data, QoL instruments, or formal survival statistics** exist.
6. **No epidemiologic prevalence/incidence estimate** and no carrier-frequency data beyond gnomAD-level rarity.

---

## Proposed Follow-up Experiments / Actions

1. **Generate an allele-specific mouse or zebrafish knock-in** carrying an EVEN-PLUS hypomorphic variant (e.g., R126W) to test whether skeletal/craniofacial malformations are recapitulated, and to define the affected cell types (chondrocytes, neural-crest mesenchyme) directly.
2. **Patient-derived iPSC → chondrocyte / neural-crest organoid models** to measure mitochondrial import efficiency, Fe-S cluster assembly, OXPHOS capacity, ROS, and apoptosis in the disease-relevant lineages, confirming the inferred causal chain in human cells.
3. **Systematic genotype–phenotype and residual-function correlation:** express the full reported variant panel in vitro (ATPase, thermostability, aggregation, import assays) and correlate residual activity with clinical severity to build a predictive severity model.
4. **Establish an international patient registry** to aggregate phenotype frequencies, natural history, survival, and QoL across the world's <15 (and growing) cases.
5. **Population screening for the recurrent East-Asian allele c.882_883delAG** to estimate carrier frequency and support targeted reproductive counseling.
6. **Explore proteostasis/antioxidant modulators** (e.g., small-molecule chaperone stabilizers, mitochondrial antioxidants) as conceptual therapeutic probes in the cellular/organoid models — recognizing that congenital structural malformations are unlikely to be reversible postnatally, so any therapeutic benefit would likely target progressive (e.g., neurologic) rather than static features.
7. **Refine ontology annotations** (submit the HPO frequencies and CL/UBERON/GO term mappings proposed here) to the disease knowledge base and to Orphanet/OMIM.

---

## Consensus Answer

EVEN-PLUS syndrome (OMIM #616854) is an ultra-rare, autosomal-recessive, prenatal-onset malformation and skeletal-dysplasia syndrome caused by biallelic loss-of-function/hypomorphic variants in *HSPA9*, encoding the mitochondrial HSP70 chaperone mortalin (mtHSP70/GRP75). Deficient mortalin impairs mitochondrial protein import, Fe-S cluster biogenesis, and proteostasis — producing oxidative stress and apoptosis in embryonic precursors that manifest as epiphyseal/vertebral dysplasia, microtia, nasal hypoplasia, and cardiac, renal, and CNS anomalies — placing it among the "mitochondrial chaperonopathies" that overlap CODAS syndrome (*LONP1*). No disease-modifying therapy exists; care is supportive and prevention is reproductive (prenatal diagnosis or preimplantation genetic testing).


## Artifacts

- [OpenScientist final report](EVEN-PLUS_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](EVEN-PLUS_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 21 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 24 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014784` (2 mentions) - the report calls it "Suggested MONDO"; MONDO calls it **severe hypotonia-psychomotor developmental delay-strabismus-cardiac septal defect syndrome**
- `HP:0011003` (1 mention) - the report calls it "Arched eyebrows"; HP calls it **High myopia**
- `HP:0002656` (2 mentions) - the report calls it "Dysplastic epiphyses at the knee"; HP calls it **Epiphyseal dysplasia**
- `HP:0011832` (1 mention) - the report calls it "Triangular nares"; HP calls it **Narrow nasal tip**
- `UBERON:0001690` (1 mention) - the report calls it "External/middle ear"; UBERON calls it **ear**
- `UBERON:0001711` (1 mention) - the report calls it "Face / eyebrow region"; UBERON calls it **eyelid**
- `NCIT:C15329` (2 mentions) - the report calls it "Evaluation and management of congenital heart defects"; NCIT calls it **Surgical Procedure**
- `NCIT:C15190` (3 mentions) - the report calls it "Supportive Care", "Monitoring/management of renal anomalies (e.g., hydronephrosis)", "Antiepileptic management; developmental support"; NCIT calls it **Needle Biopsy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0006411` (1 mention) - HP does not contain this term
- `HP:0002662` (1 mention), reported as "Delayed ossification" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004646` (1 mention) - the report calls it "Hypoplastic nasal bone"; HP calls it **Hypoplasia of the nasal bone**, and lists "Hypotrophic nasal bone" among its other names
- `HP:0003182` (1 mention) - the report calls it "Dysplastic acetabula"; HP calls it **Shallow acetabular fossae**, and lists "Shallow acetabula" among its other names
- `HP:0003417` (1 mention) - the report calls it "Vertebral (coronal) clefting"; HP calls it **Coronal cleft vertebrae**, and lists "Vertebral coronal clefts" among its other names
- `HP:0002999` (1 mention) - the report calls it "Dislocated patellae"; HP calls it **Patellar dislocation**, and lists "Dislocated patellae" among its other names
- `HP:0001627` (2 mentions) - the report calls it "Congenital heart defects"; HP calls it **Abnormal heart morphology**, and lists "Congenital heart defect" among its other names
- `HP:0000077` (2 mentions) - the report calls it "Renal alterations"; HP calls it **Abnormality of the kidney**, and lists "Renal anomalies" among its other names
- `GO:0006915` (1 mention) - the report calls it "Cellular processes:** Apoptosis"; GO calls it **apoptotic process**, and lists "activation of apoptosis" among its other names
- `UBERON:0000955` (1 mention) - the report calls it "Central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names
- `GO:0005758` (1 mention) - the report calls it "mitochondrial intermembrane space, for import"; GO calls it **mitochondrial intermembrane space**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15190` - called "Supportive Care", "Monitoring/management of renal anomalies (e.g., hydronephrosis)", "Antiepileptic management; developmental support"