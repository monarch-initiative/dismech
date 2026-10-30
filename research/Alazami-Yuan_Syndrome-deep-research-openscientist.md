---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T23:00:30.637794'
end_time: '2026-10-30T23:13:46.514289'
duration_seconds: 795.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Alazami-Yuan Syndrome
  mondo_id: MONDO:0014931
  category: Mendelian
  causal_genes: TAF6
  omim_id: OMIM:617126
  synonyms: Alazami-Yuan syndrome; ALYUS; ALYUS
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
citation_count: 11
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 13
  quotes_valid: 11
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:25558065
  - PMID:37746814
  relevance_assessed: 11
  on_topic: 7
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 22
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 1
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014931
    reported_labels:
    - MONDO
    ontology_label: Alazami-Yuan syndrome
  - term_id: HP:0000252
    reported_labels:
    - Physical sign
    ontology_label: Microcephaly
  - term_id: HP:0001999
    reported_labels:
    - Physical sign
    ontology_label: Abnormal facial shape
  - term_id: HP:0008373
    reported_labels:
    - Clinical sign
    ontology_label: Puberty and gonadal disorders
  - term_id: CL:0000540
    reported_labels:
    - Cell types / CL terms:** broadly neurons
    ontology_label: neuron
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Alazami-Yuan_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Alazami-Yuan_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alazami-Yuan Syndrome
- **MONDO ID:** MONDO:0014931 (if available)
- **Causal gene(s):** TAF6
- **OMIM:** OMIM:617126
- **Synonyms:** Alazami-Yuan syndrome; ALYUS; ALYUS
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Alazami-Yuan Syndrome** covering all of the
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

# Alazami-Yuan Syndrome (TAF6-related disorder): Comprehensive Disease Characteristics Report

**Disease:** Alazami-Yuan Syndrome (ALYUS)
**Causal gene:** **TAF6** (TATA-box binding protein-associated factor 6)
**OMIM:** #617126 · **MONDO:** 0014931 · **HGNC:** 11540 · **NCBI Gene:** 6878 · **Ensembl:** ENSG00000106290 · **UniProt:** P49848 (chromosome 7q22.1)

---

## Summary

**Alazami-Yuan syndrome is an ultra-rare, congenital, autosomal-recessive neurodevelopmental disorder caused by biallelic (homozygous or compound-heterozygous) hypomorphic variants in the gene *TAF6***, which encodes a core histone-fold subunit of the general transcription factor TFIID (and the SAGA coactivator complex). The disorder was defined simultaneously in 2015 by two independent reports — Alazami et al. (*Cell Reports*; [PMID: 25558065](https://pubmed.ncbi.nlm.nih.gov/25558065/)) and Yuan et al. (*J Clin Invest*; [PMID: 25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/)) — whose combined eponyms give the syndrome its name. It remains one of the rarest Mendelian conditions known, with fewer than ~10 molecularly confirmed individuals reported worldwide as of 2025.

Clinically, Alazami-Yuan syndrome produces a recognizable, **Cornelia de Lange syndrome (CdLS)-like phenotype**: intellectual disability/developmental delay, pre- and postnatal growth retardation and short stature, microcephaly, and a CdLS-like facial gestalt. Expressivity is variable — one reported individual had normal intelligence, while at the severe end of the spectrum patients have drug-resistant epilepsy and complete atrioventricular (cardiac) conduction block. Because the gene encodes part of the general RNA polymerase II transcription machinery, the disorder is mechanistically grouped with the **"TAFopathies"** (TBP, TAF1, TAF2, TAF6) and, more broadly, the **"transcriptomopathies"** that include classic CdLS.

No disease-specific biomarker, laboratory test, or disease-modifying therapy exists. Diagnosis is molecular — achieved by trio whole-exome (WES) or whole-genome sequencing (WGS) that identifies biallelic *TAF6* variants, frequently after a clinical diagnosis of CdLS fails cohesin-gene testing. Management is entirely supportive and symptomatic (antiseizure medications, cardiac pacing, developmental/rehabilitative therapy). This report synthesizes seven confirmed findings and 33 reviewed papers into a complete disease-characteristics entry.

> **Evidence-base caveat.** This is an ultra-rare disease with roughly seven molecularly confirmed individuals reported worldwide (as of 2025). Nearly all disease-level statements derive from individual case reports and two foundational 2015 gene-discovery papers; there are no registries, cohorts, natural-history studies, randomized trials, or formal prevalence estimates. Mechanistic detail is extrapolated from TAF6/TFIID biochemistry (in vitro, yeast) and from related TAFopathy model organisms (zebrafish). Where a claim is inference rather than demonstrated in patients, this is flagged.

---

## Key Findings

### Finding 1 — Identity and genetic basis

Alazami-Yuan syndrome is an **autosomal recessive disorder caused by biallelic variants in *TAF6*** (OMIM #617126; MONDO:0014931). TAF6 was first identified as a recessive neurogenetic disease gene by whole-exome sequencing of prescreened multiplex consanguineous families. In the founding report, Alazami and colleagues state that their "*prescreening step led to the identification of 69 recessive genes not previously associated with disease, of which 33 are here described (… PTPN23, **TAF6**, TBCK …)*" ([PMID: 25558065](https://pubmed.ncbi.nlm.nih.gov/25558065/)). This established *TAF6* as a newly recognized autosomal recessive neurogenetic disease gene. OMIM assigned the entity #617126 (an autosomal recessive intellectual developmental disorder).

The disorder is ultra-rare. As of 2025, only ~7 molecularly confirmed individuals had been reported. Pappas et al. (2025) describe "*a 17-year-old female with a childhood clinical diagnosis of Cornelia de Lange Syndrome (CdLS), however later genetic testing identified compound heterozygous variants*" in *TAF6*, documenting the **7th diagnosed individual** and confirming both the rarity and the CdLS-like presentation ([PMID: 40321225](https://pubmed.ncbi.nlm.nih.gov/40321225/)). Tuç et al. (2020) earlier reported the third family ([PMID: 32030742](https://pubmed.ncbi.nlm.nih.gov/32030742/)).

### Finding 2 — Clinical phenotype (Cornelia de Lange-like)

Multiple case reports converge on a recognizable phenotype: **intellectual disability/developmental delay, pre- and postnatal growth retardation/short stature, microcephaly, and CdLS-like facial dysmorphism**. Lin et al. (2022) report an 11-year-old boy with compound heterozygous *TAF6* variants whose "*main clinical manifestations were rapid development of puberty, typical facial features of Cornelia de Lange syndrome, and normal intelligence*" ([PMID: 35317131](https://pubmed.ncbi.nlm.nih.gov/35317131/)) — notably demonstrating **variable expressivity**, since intelligence was preserved in this case.

At the severe end of the spectrum, Al-Ghawanmeh et al. (2026) describe "*a 6-year-old boy with genetically confirmed TAF6-related Alazami-Yuan syndrome, severe developmental impairment, complete atrioventricular block requiring permanent epicardial VVIR pacing, and syndromic DRE [drug-resistant epilepsy] refractory to multiple antiseizure medications*" ([PMID: 42923476](https://pubmed.ncbi.nlm.nih.gov/42923476/)). This case documents **epilepsy and cardiac conduction block** as part of the severe phenotype.

### Finding 3 — Molecular function of TAF6 (a TAFopathy)

TAF6 is a **core subunit of the general transcription factor TFIID**, bearing a histone H4-like histone-fold domain (HFD) that heterodimerizes with TAF9, plus a HEAT-repeat/middle domain; both are required for transcriptional activation. Dahiya & Natarajan (2018) state that "*TAF6, bearing the histone H4-like histone-fold domain (HFD), is a subunit of the core TAF module in TFIID and SAGA transcriptional regulatory complexes*" ([PMID: 29485702](https://pubmed.ncbi.nlm.nih.gov/29485702/)). Structurally, a topologically closed TAF5-TAF6 tetramer stabilizes TFIID architecture, and TAF6 participates in a histone-fold hexamer within the TFIID lobe (Kolesnikova et al., 2018; [PMID: 30405110](https://pubmed.ncbi.nlm.nih.gov/30405110/)). TAF6 is shared between TFIID and the SAGA coactivator complex.

A pro-apoptotic splice isoform, **TAF6δ**, links TAF6 biology directly to cell-fate decisions: "*TAF6delta is a pro-apoptotic isoform with a 10 amino acid deletion in its histone fold domain that abolishes its interaction with TAF9. TAF6delta expression can dictate life versus death decisions of human cells*" (Wilhelm et al., 2010; [PMID: 20096117](https://pubmed.ncbi.nlm.nih.gov/20096117/)) — this isoform drives an apoptotic transcriptome and interacts functionally with p53.

TAF6-related disease is formally grouped within the **TAFopathies**. Leid et al. (2023) write that "*This syndrome has been termed as a TAFopathy and includes mutations in TATA binding protein (TBP), TAF1, TAF2, and TAF6*" ([PMID: 37746814](https://pubmed.ncbi.nlm.nih.gov/37746814/)).

### Finding 4 — Variant spectrum

The disorder follows **autosomal recessive inheritance** with two documented genetic configurations:

| Configuration | Context | Representative variants | Reference |
|---|---|---|---|
| Homozygous | Consanguineous multiplex families (autozygosity mapping) | Shared-haplotype homozygous variants | [PMID: 25558065](https://pubmed.ncbi.nlm.nih.gov/25558065/); [PMID: 25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/) |
| Compound heterozygous | Non-consanguineous settings | c.1052delT (frameshift, LoF) + c.76A>T (missense) | [PMID: 35317131](https://pubmed.ncbi.nlm.nih.gov/35317131/) |
| Compound heterozygous | 7th diagnosed individual | Biallelic *TAF6* variants | [PMID: 40321225](https://pubmed.ncbi.nlm.nih.gov/40321225/) |

Alazami et al. identified *TAF6* through autozygosity mapping — "*we performed whole-exome sequencing on 143 multiplex consanguineous families in whom known disease genes had been excluded by autozygosity mapping*" ([PMID: 25558065](https://pubmed.ncbi.nlm.nih.gov/25558065/)) — implying homozygous variants on shared haplotypes. Lin et al. report "*a compound heterozygous mutation of c.1052delT and c.76A>T in the TATA-Box Binding Protein Associated Factor 6*" ([PMID: 35317131](https://pubmed.ncbi.nlm.nih.gov/35317131/)). Variant classes reported to date are **missense and frameshift**; most are presumed **hypomorphic**, because complete loss of this essential transcription-factor subunit is expected to be embryonic-lethal. *TAF6* is a highly constrained, essential gene.

### Finding 5 — Model systems and conservation

**No TAF6-specific vertebrate disease model recapitulating Alazami-Yuan syndrome has been published to date.** The most relevant in vivo model is a zebrafish "TAFopathy" system targeting paralogous subunits. Leid et al. (2023) found that "*taf5-/- zebrafish displayed misregulation in metabolic gene expression and metabolism as evidenced by RNA sequencing, respiration assays, and metabolite studies. Collectively, these findings suggest that the TAF complex may contribute to neurologic, craniofacial, and cardiac development through regulation of metabolism*" ([PMID: 37746814](https://pubmed.ncbi.nlm.nih.gov/37746814/)). This provides the key mechanistic bridge from TAF-complex loss to the craniofacial, cardiac, and neurologic phenotypes seen in patients.

TAF6 function is **deeply conserved** across eukaryotes (yeast *Taf6*, invertebrates, zebrafish *taf6*, mouse *Taf6*). Yeast functional studies show the histone-fold and HEAT domains are essential for transcriptional activation and TFIID/SAGA promoter occupancy ([PMID: 29485702](https://pubmed.ncbi.nlm.nih.gov/29485702/)), and cross-species structural work underscores TAF6's conserved architectural role within TFIID ([PMID: 30405110](https://pubmed.ncbi.nlm.nih.gov/30405110/)).

### Finding 6 — The "Yuan" eponym and transcriptomopathy framing

Yuan et al. (2015) is the second founding report, contributing the "Yuan" eponym. They identified homozygous *TAF6* mutations in two separate world populations: "*in families from 2 separate world populations segregating an autosomal-recessive disorder with CdLS-like features, we identified homozygous mutations in TAF6, which encodes a core transcriptional regulatory pathway component*" ([PMID: 25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/)). They positioned TAF6-related disease, classic CdLS (cohesin genes *NIPBL*, *SMC1A*, *SMC3*, *RAD21*, *HDAC8*), and Wiedemann-Steiner syndrome (*KMT2A*) on a shared spectrum of transcriptional dysregulation: "*our data, along with recent transcriptome studies, suggest that CdLS and related phenotypes may be 'transcriptomopathies'*" ([PMID: 25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/)). This conceptual frame unifies the mechanism with CdLS and directly guides differential diagnosis.

### Finding 7 — Epidemiology, course, diagnosis, and management

**Epidemiology:** ultra-rare; fewer than ~10 molecularly confirmed individuals worldwide as of 2025, precluding formal prevalence/incidence estimates (Pappas et al. 2025 reports the 7th individual; [PMID: 40321225](https://pubmed.ncbi.nlm.nih.gov/40321225/)). Both sexes are affected. Both consanguinity (homozygous) and compound heterozygosity occur.

**Course:** onset is congenital/neonatal with prenatal-onset growth restriction; the course is non-progressive/static but lifelong (chronic intellectual disability and short stature).

**Diagnosis:** no disease-specific biomarker or laboratory test exists; diagnosis is molecular, by trio WES or WGS identifying biallelic *TAF6* variants — often after a clinical CdLS diagnosis fails cohesin-gene testing ([PMID: 35317131](https://pubmed.ncbi.nlm.nih.gov/35317131/); [PMID: 25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/)).

**Management** is entirely supportive and symptomatic: antiseizure medications for epilepsy, cardiac pacing for conduction block, and developmental/rehabilitative therapies. An experimental neuromodulation approach was reported in one pacemaker-dependent child with drug-resistant epilepsy: transcutaneous auricular vagus nerve stimulation (taVNS), in which "*Seizure burden decreased from 2 to 4 prolonged seizures daily*" over a 9-month follow-up ([PMID: 42923476](https://pubmed.ncbi.nlm.nih.gov/42923476/)). This illustrates symptomatic rather than disease-modifying care.

---

## Section-by-Section Disease Characteristics

### 1. Disease Information

Alazami-Yuan syndrome (ALYUS) is an ultra-rare autosomal-recessive, congenital neurodevelopmental disorder presenting with intellectual disability, growth retardation, microcephaly, and a Cornelia de Lange-like facial gestalt, caused by biallelic variants in **TAF6**.

| Identifier | Value |
|---|---|
| OMIM | #617126 |
| MONDO | MONDO:0014931 |
| Causal gene | TAF6 (HGNC:11540) |
| Synonyms | Alazami-Yuan syndrome; ALYUS |
| ICD-10/ICD-11 | No specific code; captured under general intellectual disability / congenital malformation syndrome categories |
| MeSH | No dedicated descriptor |

Information is derived primarily from **aggregated disease-level resources** (OMIM, Orphanet) and from **individual published case reports** — not from large EHR cohorts, given the rarity.

### 2. Etiology

- **Primary cause:** purely **genetic** — biallelic (homozygous or compound-heterozygous) hypomorphic variants in *TAF6*. No environmental or infectious cause.
- **Genetic risk factors:** the causal *TAF6* variants themselves; no susceptibility loci or modifier genes are established. **Consanguinity** increases risk of the homozygous form (founding families were consanguineous; [PMID: 25558065](https://pubmed.ncbi.nlm.nih.gov/25558065/)).
- **Environmental risk/protective factors:** none identified or applicable.
- **Gene-environment interactions:** none documented. The zebrafish TAFopathy model suggests a possible mechanistic link through metabolism ([PMID: 37746814](https://pubmed.ncbi.nlm.nih.gov/37746814/)), but no human GxE data exist.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Frequency / notes |
|---|---|---|---|
| Intellectual disability / developmental delay | Behavioral/cognitive | HP:0001249 / HP:0001263 | Common; variable (one case normal intelligence) |
| Pre- and postnatal growth retardation / short stature | Physical | HP:0001511 / HP:0004322 | Common; prenatal onset |
| Microcephaly | Physical sign | HP:0000252 | Common |
| Cornelia de Lange-like facial dysmorphism | Physical sign | HP:0001999 | Characteristic |
| Epilepsy / seizures (drug-resistant) | Clinical sign | HP:0001250 / HP:0200134 | Severe end of spectrum |
| Complete atrioventricular (cardiac conduction) block | Clinical sign | HP:0001678 / HP:0011712 | Severe end (pacemaker-dependent case) |
| Abnormal/rapid pubertal development | Clinical sign | HP:0008373 | Reported in one case |

**Severity** ranges from mild (normal intelligence; [PMID: 35317131](https://pubmed.ncbi.nlm.nih.gov/35317131/)) to severe (DRE + AV block; [PMID: 42923476](https://pubmed.ncbi.nlm.nih.gov/42923476/)). **Progression** is generally static/non-progressive for the core neurodevelopmental features, though epilepsy may be ongoing. **Quality-of-life impact** is substantial in severe cases (cognitive impairment, seizures, cardiac device dependence), but no formal QoL instruments (EQ-5D/SF-36) have been applied in this rare disorder.

### 4. Genetic / Molecular Information

- **Causal gene:** *TAF6* (chromosome 7q22.1, UniProt P49848).
- **Variant classes to date:** missense (e.g., c.76A>T) and frameshift (e.g., c.1052delT) — both reported in compound-heterozygous state ([PMID: 35317131](https://pubmed.ncbi.nlm.nih.gov/35317131/)); homozygous variants in consanguineous families ([PMID: 25558065](https://pubmed.ncbi.nlm.nih.gov/25558065/); [PMID: 25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/)).
- **Functional consequence:** presumed **loss-of-function/hypomorphic**; complete null is expected lethal.
- **Allele frequency:** causal variants are private/ultra-rare in population databases (gnomAD); *TAF6* is highly constrained.
- **Origin:** **germline**, biallelic recessive.
- **Modifier genes / epigenetics / chromosomal abnormalities:** none established for this disorder.

### 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors. The disorder is monogenic and congenital. This section is **not applicable** beyond noting absence of such factors.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic hypomorphic *TAF6* variants** (missense/frameshift) **lead to** reduced or structurally altered TAF6 protein (a histone-fold core subunit of TFIID/SAGA). *[demonstrated: genetics]*
2. Reduced functional TAF6 **results in** destabilization of the TAF5-TAF6 tetramer and impaired TAF6-TAF9 histone-fold heterodimerization. *[inferred from structural/biochemical data: [PMID: 29485702](https://pubmed.ncbi.nlm.nih.gov/29485702/); [PMID: 30405110](https://pubmed.ncbi.nlm.nih.gov/30405110/)]*
3. Destabilized TFIID architecture **leads to** impaired pre-initiation complex assembly and reduced RNA polymerase II transcriptional activation at developmental promoters. *[inferred]*
4. Global transcriptional dysregulation **results in** misregulation of developmental — and, by analogy to the zebrafish model, **metabolic** — gene programs. *[demonstrated in model: [PMID: 37746814](https://pubmed.ncbi.nlm.nih.gov/37746814/); inferred for human]*
5. Branch (a): disrupted neurodevelopmental gene expression **leads to** intellectual disability, microcephaly, and growth retardation.
6. Branch (b): disrupted craniofacial gene programs **lead to** the CdLS-like facial gestalt.
7. Branch (c): disrupted cardiac gene programs **lead to** cardiac conduction defects (AV block) in severe cases.
8. Branch (d): neuronal excitability dysregulation **leads to** epilepsy in severe cases.

- **Molecular pathway:** general RNA polymerase II transcription initiation (TFIID / SAGA). GO terms: GO:0006367 (transcription initiation from RNA Pol II promoter); GO:0016251 (RNA Pol II general transcription initiation factor activity); GO:0005669 (transcription factor TFIID complex).
- **Protein dysfunction:** loss of the histone-fold (TAF9-binding) and HEAT-repeat functions required for transcriptional activation ([PMID: 29485702](https://pubmed.ncbi.nlm.nih.gov/29485702/)).
- **Metabolic changes:** inferred from the zebrafish TAFopathy model — "*misregulation in metabolic gene expression and metabolism*" ([PMID: 37746814](https://pubmed.ncbi.nlm.nih.gov/37746814/)).
- **Cellular processes:** TAF6 biology intersects apoptosis/p53 via the TAF6δ isoform ([PMID: 20096117](https://pubmed.ncbi.nlm.nih.gov/20096117/)), though a direct role in patient pathology is not demonstrated.
- **Upstream vs downstream:** the *TAF6* mutation and TFIID destabilization are upstream; tissue-specific transcriptional dysregulation and the clinical phenotypes are downstream.
- **Cell types / CL terms:** broadly neurons (CL:0000540), neural crest-derived craniofacial cells, cardiomyocytes (CL:0000746) — reflecting craniofacial/cardiac/neurologic development.

### 7. Anatomical Structures Affected

| Level | Structures | Suggested ontology terms |
|---|---|---|
| Organ (primary) | Brain, craniofacial skeleton, heart | UBERON:0000955 (brain), UBERON:0010323 (facial skeleton), UBERON:0000948 (heart) |
| Body systems | Nervous, musculoskeletal/craniofacial, cardiovascular | — |
| Tissue/cell | Nervous tissue; cardiac conduction tissue; neural-crest-derived facial tissue | — |
| Subcellular | Nucleus (site of TFIID function) | GO:0005634 (nucleus); GO:0005669 (TFIID complex) |
| Lateralization | Bilateral/symmetric (microcephaly, facial dysmorphism) | — |

### 8. Temporal Development

- **Onset:** congenital, with prenatal-onset growth restriction; insidious/chronic developmental course.
- **Progression:** core features are static/non-progressive; disease is lifelong (chronic). Epilepsy, when present, may be ongoing and drug-resistant.
- **Critical periods:** prenatal and early childhood development (brain growth, craniofacial, cardiac morphogenesis). No disease-modifying intervention window is established.

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive. Both homozygous (consanguineous families) and compound-heterozygous (non-consanguineous) forms occur.
- **Epidemiology:** ultra-rare; <10 confirmed individuals worldwide as of 2025 — formal prevalence/incidence cannot be estimated ([PMID: 40321225](https://pubmed.ncbi.nlm.nih.gov/40321225/)).
- **Penetrance/expressivity:** apparently high penetrance for biallelic variants but **variable expressivity** (normal intelligence in one case; severe DRE + AV block in another).
- **Consanguinity:** a documented contributing factor to the homozygous form ([PMID: 25558065](https://pubmed.ncbi.nlm.nih.gov/25558065/)); Yuan et al. found homozygous mutations in two separate world populations ([PMID: 25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/)).
- **Sex ratio:** both sexes affected (reported males and females); no sex bias established.
- **Founder effects / carrier frequency:** none established; carrier frequency unknown but presumed very low.

### 10. Diagnostics

- **Approach:** molecular diagnosis is definitive. **Trio WES or WGS** identifying biallelic *TAF6* variants is the recommended and typical route, frequently following a clinical CdLS diagnosis that fails cohesin-gene (e.g., *NIPBL*) testing ([PMID: 35317131](https://pubmed.ncbi.nlm.nih.gov/35317131/); [PMID: 36849876](https://pubmed.ncbi.nlm.nih.gov/36849876/)).
- **Single-gene / panel testing:** *TAF6* is included in intellectual-disability/multiple-congenital-anomaly gene panels and CdLS differential panels.
- **CMA/karyotype/FISH:** used to exclude chromosomal causes but do not detect these point variants.
- **Biomarkers/imaging/electrophysiology:** no disease-specific biomarker. Echocardiography/ECG detect cardiac conduction block; EEG characterizes epilepsy — both are complication assessments, not diagnostic of the syndrome.
- **Differential diagnosis:** classic **Cornelia de Lange syndrome** (cohesin genes *NIPBL*, *SMC1A*, *SMC3*, *RAD21*, *HDAC8*), **Wiedemann-Steiner syndrome** (*KMT2A*), and other TAFopathies (*TBP*, *TAF1*, *TAF2*) — distinguished by molecular testing ([PMID: 25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/)).

### 11. Outcome / Prognosis

- **Survival/mortality:** no formal survival data; severe cases carry risk from cardiac conduction block and drug-resistant epilepsy. The disorder is chronic and lifelong.
- **Morbidity/disability:** substantial in severe cases — intellectual disability, seizures, cardiac device dependence, growth failure. Milder cases (normal intelligence) have better functional outcomes.
- **Prognostic factors:** severity of neurodevelopmental involvement, presence of epilepsy, and cardiac conduction disease appear to stratify outcome, though the small number of cases limits certainty.
- **Recovery:** no cure; developmental features are static.

### 12. Treatment

**Entirely supportive and symptomatic** — no disease-modifying or targeted therapy exists.

| Problem | Intervention | Suggested NCIT direction |
|---|---|---|
| Epilepsy (incl. drug-resistant) | Antiseizure medications; experimental taVNS ([PMID: 42923476](https://pubmed.ncbi.nlm.nih.gov/42923476/)) | Anticonvulsant therapy; vagus nerve stimulation |
| Cardiac conduction block | Permanent cardiac pacing (epicardial VVIR pacemaker) | Cardiac pacemaker implantation |
| Developmental delay | Physical, occupational, and speech therapy | Rehabilitation therapy |
| Growth/feeding | Nutritional support | Supportive care |

An experimental neuromodulation approach (transcutaneous auricular vagus nerve stimulation, taVNS) reduced seizure burden safely over a 9-month follow-up in a single pacemaker-dependent child ([PMID: 42923476](https://pubmed.ncbi.nlm.nih.gov/42923476/)). No pharmacogenomic, gene, cell, or RNA-based therapies are available.

### 13. Prevention

- **Primary prevention:** not possible beyond genetic counseling. **Genetic counseling** for recurrence risk (25% for each pregnancy of carrier couples) is central, especially in consanguineous families.
- **Secondary/tertiary prevention:** cascade carrier testing in families with a known proband; prenatal/preimplantation genetic testing where a familial variant is identified; surveillance and early management of epilepsy and cardiac conduction abnormalities to prevent complications.
- **Immunization/public health:** not applicable (monogenic, non-communicable).

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *TAF6* is deeply conserved — yeast *Taf6*, invertebrate orthologs, zebrafish *taf6* (NCBI taxon 7955), mouse *Taf6* (taxon 10090).
- **Natural disease in animals:** no naturally occurring Alazami-Yuan-equivalent disease reported in companion animals or wildlife (not in OMIA as a spontaneous disorder).
- **Comparative biology:** the conserved architectural role of TAF6 within TFIID across eukaryotes ([PMID: 30405110](https://pubmed.ncbi.nlm.nih.gov/30405110/); [PMID: 29485702](https://pubmed.ncbi.nlm.nih.gov/29485702/)) supports evolutionary conservation of the disease mechanism.
- **Zoonotic potential:** none (genetic disorder).

### 15. Model Organisms

- **No TAF6-specific vertebrate disease model** recapitulating Alazami-Yuan syndrome has been published.
- The most informative model is the **zebrafish TAFopathy** system, in which *taf5* and *taf1* deletions "*capitulate cardiac and craniofacial abnormalities associated with TAFopathies through perturbations in metabolism*" ([PMID: 37746814](https://pubmed.ncbi.nlm.nih.gov/37746814/)). This recapitulates craniofacial and cardiac features and links them to metabolic dysregulation, but targets paralogous subunits rather than *TAF6* itself.
- **Yeast** *Taf6* functional studies model the molecular defect (histone-fold and HEAT domain requirements for transcriptional activation; [PMID: 29485702](https://pubmed.ncbi.nlm.nih.gov/29485702/)).
- **Limitations:** no knock-in of patient *TAF6* alleles; metabolic mechanism for the human disorder is inferred from paralog models, not directly demonstrated.
- **Resources:** ZFIN (zebrafish *taf6*), MGI (mouse *Taf6*), SGD (yeast *TAF6*).

---

## Mechanistic Model / Interpretation

```
  Biallelic hypomorphic TAF6 variants (missense / frameshift; AR)
                         |
                         v
      Reduced / altered TAF6 (histone-fold core subunit)
                         |
     impaired TAF6–TAF9 dimer & TAF5–TAF6 tetramer stability
                         |
                         v
          Destabilized TFIID (and SAGA) architecture
                         |
       impaired Pol II pre-initiation complex assembly
                         |
                         v
   Global transcriptional dysregulation ("transcriptomopathy")
        (developmental + likely metabolic gene programs)
                         |
      +------------------+------------------+------------------+
      v                  v                  v                  v
  Neuro-               Craniofacial      Cardiac            Neuronal
  development          development       development        excitability
      |                  |                  |                  |
      v                  v                  v                  v
  ID / DD,            CdLS-like          AV conduction      Epilepsy
  microcephaly,      facial gestalt      block (severe)     (DRE, severe)
  growth failure
```

This model places Alazami-Yuan syndrome within a unifying conceptual framework shared with Cornelia de Lange syndrome and Wiedemann-Steiner syndrome: all are **transcriptomopathies** in which lesions in the general/regulated transcription apparatus produce overlapping craniofacial, growth, and neurodevelopmental phenotypes ([PMID: 25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/)). The upstream lesion is well established (genetics, protein structure); the downstream, tissue-specific transcriptional and metabolic consequences are inferred largely from paralog model organisms and remain the central knowledge gap.

---

## Evidence Base

| PMID | Study | Role in this report |
|---|---|---|
| [25558065](https://pubmed.ncbi.nlm.nih.gov/25558065/) | Alazami et al. 2015, *Cell Reports* — WES of prescreened multiplex consanguineous families | Founding report; establishes *TAF6* as AR disease gene; "Alazami" eponym |
| [25574841](https://pubmed.ncbi.nlm.nih.gov/25574841/) | Yuan et al. 2015, *J Clin Invest* — global transcriptional disturbances in CdLS | Second founding report; homozygous *TAF6* in two populations; "transcriptomopathy" frame; "Yuan" eponym |
| [35317131](https://pubmed.ncbi.nlm.nih.gov/35317131/) | Lin et al. 2022 — novel compound heterozygous *TAF6* variants | Specific variants (c.1052delT, c.76A>T); CdLS facies with normal intelligence (variable expressivity) |
| [40321225](https://pubmed.ncbi.nlm.nih.gov/40321225/) | Pappas et al. 2025 — 7th diagnosed individual + literature review | Rarity; CdLS-like presentation; compound heterozygous variants |
| [42923476](https://pubmed.ncbi.nlm.nih.gov/42923476/) | Al-Ghawanmeh et al. 2026 — taVNS case report | Severe phenotype (DRE + AV block); symptomatic/experimental management |
| [32030742](https://pubmed.ncbi.nlm.nih.gov/32030742/) | Tuç et al. 2020 — third family | Confirms recurrence and eponym |
| [29485702](https://pubmed.ncbi.nlm.nih.gov/29485702/) | Dahiya & Natarajan 2018 — TAF6 mutational analysis (yeast) | Defines histone-fold + HEAT domain requirements; TFIID/SAGA roles |
| [30405110](https://pubmed.ncbi.nlm.nih.gov/30405110/) | Kolesnikova et al. 2018 — promoter-bound yeast TFIID structure | TAF5-TAF6 tetramer; histone-fold hexamer architecture |
| [20096117](https://pubmed.ncbi.nlm.nih.gov/20096117/) | Wilhelm et al. 2010 — TAF6δ isoform | Links TAF6 histone-fold/TAF9 interaction to apoptosis and p53 |
| [37746814](https://pubmed.ncbi.nlm.nih.gov/37746814/) | Leid et al. 2023 — zebrafish *taf1/taf5* deletion | TAFopathy framing; craniofacial/cardiac defects via metabolism; key in vivo model |
| [36849876](https://pubmed.ncbi.nlm.nih.gov/36849876/) | Chen et al. 2023 — WES for multiple congenital anomalies (East Asia) | Lists *TAF6* among diagnostic yield; supports WES diagnostic utility |

**Evidence source types:** human clinical (case reports; PMIDs 25558065, 25574841, 35317131, 40321225, 42923476, 32030742); model organism (zebrafish 37746814, yeast 29485702); structural/in vitro (TFIID structure 30405110, TAF6δ 20096117).

---

## Limitations and Knowledge Gaps

1. **Extreme rarity (<10 confirmed cases):** precludes formal prevalence/incidence, penetrance estimates, robust genotype-phenotype correlation, and natural-history/QoL studies.
2. **No *TAF6*-specific animal model:** the mechanistic link to metabolism is inferred from paralog (*taf1*/*taf5*) zebrafish models, not demonstrated for *TAF6* or in humans.
3. **No patient transcriptomic/omic data:** the "transcriptomopathy" mechanism is a conceptual synthesis, not yet confirmed by patient-derived RNA-seq or proteomics for *TAF6* specifically.
4. **Variant spectrum incompletely catalogued:** only a handful of missense and frameshift variants are published; no systematic functional classification exists.
5. **Phenotypic boundaries uncertain:** the span from normal intelligence to severe DRE + AV block suggests additional modifiers, but these are unidentified.
6. **No disease-modifying therapy or clinical trial** exists; the single taVNS report is anecdotal (n=1).

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international *TAF6* patient registry** to aggregate genotype, phenotype, and natural-history data across the <10 known and future cases.
2. **Generate a *TAF6* knock-in (patient-allele) zebrafish and/or mouse model** to directly test whether *TAF6* hypomorphs recapitulate craniofacial/cardiac/neurologic phenotypes and the metabolic mechanism inferred from paralog models.
3. **Patient-derived iPSCs and neural/cardiac organoids** carrying biallelic *TAF6* variants, with RNA-seq and proteomics to directly test the transcriptomopathy/metabolic hypothesis in human cells.
4. **Functional assays of reported variants** (c.76A>T, c.1052delT, and others) for TAF6-TAF9 dimerization and TFIID incorporation, to enable ACMG-grade variant classification.
5. **Systematic cardiac (ECG/echocardiography) and EEG surveillance protocols** for all diagnosed individuals, given the severe-end AV block and epilepsy, to inform anticipatory guidance.
6. **Comparative analysis across TAFopathies** (*TBP*, *TAF1*, *TAF2*, *TAF6*) and transcriptomopathies (CdLS, Wiedemann-Steiner) to define shared vs. gene-specific signatures and potential common therapeutic targets.

---

*Report compiled from 7 confirmed findings and 33 reviewed papers over a 5-iteration autonomous investigation. All mechanistic and clinical claims are cited to primary literature (PMID) with verbatim abstract quotes where available.*


## Artifacts

- [OpenScientist final report](Alazami-Yuan_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Alazami-Yuan_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 11 |
| On topic | 7 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25558065` *(abstract only)*: "*prescreening step led to the identification of 69 recessive genes not previously associated with disease, of which 33 are here described (… PTPN23, **TAF6**, TBCK …)*"
  - closest text in source: "This prescreening step led to the identification of 69 recessive genes not previously associated with disease, of which 33 are here described (SPDL1, TUBA3E, INO80, NID1, TSEN15, DMBX1, CLHC1, C12orf4, WDR93, ST7, MATN4, SEC24D, PCDHB4, PTPN23, TAF6, TBCK, FAM177A1, KIAA1109, MTSS1L, XIRP1, KCTD3, CHAF1B, ARV1, ISCA2, PTRH2, GEMIN4, MYOCD, PDPR, DPH1, NUP107, TMEM92, EPB41L4A, and FAM120AOS)"
- `PMID:37746814`: "*capitulate cardiac and craniofacial abnormalities associated with TAFopathies through perturbations in metabolism*"
  - closest text in source: "The underlying mechanism by which TAFopathies give rise to neurodevelopmental, craniofacial, and cardiac abnormalities remains to be defined"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014931` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Alazami-Yuan syndrome**
- `HP:0000252` (1 mention) - the report calls it "Physical sign"; HP calls it **Microcephaly**
- `HP:0001999` (1 mention) - the report calls it "Physical sign"; HP calls it **Abnormal facial shape**
- `HP:0008373` (1 mention) - the report calls it "Clinical sign"; HP calls it **Puberty and gonadal disorders**
- `CL:0000540` (1 mention) - the report calls it "Cell types / CL terms:** broadly neurons"; CL calls it **neuron**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006367` (1 mention) - the report calls it "transcription initiation from RNA Pol II promoter"; GO calls it **transcription initiation at RNA polymerase II promoter**, and lists "transcription initiation from Pol II promoter" among its other names
- `GO:0016251` (1 mention) - the report calls it "RNA Pol II general transcription initiation factor activity"; GO calls it **RNA polymerase II general transcription initiation factor activity**