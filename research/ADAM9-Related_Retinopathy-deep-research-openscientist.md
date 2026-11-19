---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T00:54:28.471866'
end_time: '2026-11-05T01:08:15.020388'
duration_seconds: 826.55
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: ADAM9-Related Retinopathy
  mondo_id: MONDO:0800398
  category: Mendelian
  causal_genes: ADAM9
  omim_id: not recorded
  synonyms: not recorded
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
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 2
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:20806078
  - PMID:20691256
  relevance_assessed: 9
  on_topic: 7
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 1
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0000613
    reported_labels:
    - Frequent
    ontology_label: Photophobia
  - term_id: HP:0000551
    reported_labels:
    - Frequent
    ontology_label: Color vision defect
  - term_id: HP:0000662
    reported_labels:
    - Common as disease advances
    ontology_label: Nyctalopia
  - term_id: HP:0001133
    reported_labels:
    - Common
    ontology_label: Constriction of peripheral visual field
  - term_id: HP:0000639
    reported_labels:
    - Variable
    ontology_label: Nystagmus
  - term_id: HP:0000512
    reported_labels:
    - Defining
    ontology_label: Abnormal electroretinogram
  - term_id: HP:0007843
    reported_labels:
    - Common
    ontology_label: Attenuation of retinal blood vessels
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
  path: ADAM9-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ADAM9-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ADAM9-Related Retinopathy
- **MONDO ID:** MONDO:0800398 (if available)
- **Causal gene(s):** ADAM9
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **ADAM9-Related Retinopathy** covering all of the
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

# ADAM9-Related Retinopathy (Cone-Rod Dystrophy 9, CORD9) — Comprehensive Disease Report

> **Causal gene (stated up front): `ADAM9`** (A Disintegrin And Metalloprotease domain, family member 9; HGNC:216; NCBI Gene 8754; UniProt Q13443; chromosome 8p11.22). The disease referenced by **MONDO:0800398** is the autosomal-recessive, early-onset **cone-rod dystrophy 9 (CORD9)** caused by biallelic loss-of-function variants in **ADAM9**. Despite the serial name, it is unambiguously an *ADAM9* disorder; this report follows the MONDO ID and causal gene given.

Evidence-source legend: **[H]** human clinical, **[M]** mouse model, **[D]** dog/natural animal model, **[V]** in vitro, **[R]** review/computational.

---

## 1. Disease Information

**Overview.** ADAM9-related retinopathy is an inherited, bilateral, progressive retinal dystrophy in which **cone photoreceptors are affected first and most severely, followed by rods** (a "cone-rod" pattern). It is designated **cone-rod dystrophy 9 (CORD9)**. Onset is typically in early childhood with reduced central/color vision, photophobia (day blindness) and later night blindness and peripheral field loss. The initiating lesion is at the **photoreceptor outer-segment–retinal pigment epithelium (POS–RPE) junction** rather than within the photoreceptor itself [H/M, PMID 19409519].

**Key identifiers.**
- **MONDO:** MONDO:0800398
- **OMIM (phenotype):** 612775 — "Cone-rod dystrophy 9" (CORD9)
- **OMIM (gene):** 602713 — ADAM9
- **HGNC:** HGNC:216 (ADAM9); **NCBI Gene:** 8754; **Ensembl:** ENSG00000168615; **UniProt:** Q13443
- **Orphanet:** within "Cone-rod dystrophy" (ORPHA:1872); ADAM9 is a recognized causative gene
- **ICD-10:** H35.5 (Hereditary retinal dystrophy); **ICD-11:** 9B70.0 (Hereditary retinal dystrophy, cone-rod)
- **MeSH:** Cone-Rod Dystrophies (D000076080); Retinal Dystrophies (D058499)

**Synonyms / alternative names.** Cone-rod dystrophy 9; CORD9; CRD9; ADAM9-related cone-rod dystrophy; autosomal recessive cone-rod dystrophy due to ADAM9; (animal homologs: canine cone-rod dystrophy 3 / crd3; canine generalized progressive retinal atrophy, gPRA, in Glen of Imaal Terrier).

**Clinical-spectrum note.** Although classified as a "cone-rod dystrophy," ADAM9 disease in humans is frequently **early-onset and severe**, with some patients presenting in the first years of life with marked visual impairment/nystagmus, so that the phenotype overlaps the **early-onset severe retinal dystrophy (EOSRD) / Leber congenital amaurosis (LCA) spectrum** and ADAM9 is included on EOSRD/LCA and generic inherited-retinal-disease gene panels [H, PMIDs 25091951, 25546566, 38892339]. This is a more severe, earlier-onset presentation than the classic adult-onset cone-rod dystrophies.

**Information source.** Disease-level, aggregated from small consanguineous-family case series and from mouse/dog models — **not** from large EHR cohorts. The condition is rare and most publications describe individual families or single patients [H, PMIDs 19409519, 25091951, 25546566, 38028590]. Panel-sequencing cohorts of childhood retinal dystrophy (e.g., a Chilean EOSRD/LCA cohort of 67 patients/60 families) illustrate that ADAM9 is among the recurrently tested genes in this diagnostic category [H, PMID 38892339].

---

## 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound-heterozygous) **null/loss-of-function mutations in ADAM9**. Discovery: "By autozygosity mapping, we identified null mutations in the ADAM metallopeptidase domain 9 (ADAM9) gene in four consanguineous families with recessively inherited early-onset CRD" [H, PMID 19409519].

**Genetic risk factors.**
- *Causal variants:* nonsense, frameshift, splice-site and whole-exon/large deletions in ADAM9 (see §4).
- *Consanguinity / founder homozygosity* is the dominant risk context; most reported families are consanguineous (Middle East, North Africa, South Asia) [H, PMIDs 19409519, 25091951].
- *Carrier status:* heterozygotes are unaffected (recessive).
- No established common-variant susceptibility loci or modifier genes are reported.

**Environmental / lifestyle risk factors.** None established as causal. The disease is monogenic. (Light exposure is a generic theoretical accelerant of photoreceptor stress in retinal dystrophies but is **not** demonstrated specifically for ADAM9.)

**Protective factors.** None genetically defined. General retinal-health measures (UV/blue-light protection, avoidance of smoking) are prudent but unproven for this disease.

**Gene–environment interactions.** Not characterized for CORD9. Of note, in RPE cells *hyperglycemia upregulates ADAM9*, increasing MerTK shedding and impairing outer-segment phagocytosis [V, PMID 35163068] — a metabolic modulator of ADAM9 biology, though not shown to modify CORD9 severity.

---

## 3. Phenotypes

Phenotypes are **clinical signs, symptoms, and electrophysiological/laboratory (ERG, OCT) abnormalities**. Onset is usually **childhood/early-onset**; course is **progressive**. Frequencies are qualitative (small cohorts).

| Phenotype | Type | Typical onset / course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Cone-rod dystrophy (cone > rod loss) | Clinical sign / core | Childhood; progressive | Defining (~100%) | HP:0000548 (Cone/cone-rod dystrophy) |
| Reduced visual acuity / visual impairment | Symptom | Childhood; progressive | Very frequent | HP:0000505 / HP:0032037 |
| Photophobia ("day blindness") | Symptom | Early | Frequent | HP:0000613 |
| Color vision defect (dyschromatopsia) | Symptom | Early | Frequent | HP:0000551 |
| Nyctalopia (night blindness) | Symptom | Later (rod involvement) | Common as disease advances | HP:0000662 |
| Constricted / peripheral visual field loss | Sign | Progressive | Common | HP:0001133 |
| Nystagmus | Sign | Early if infantile onset | Variable | HP:0000639 |
| Abnormal / reduced ERG (photopic > scotopic) | Lab/electrophysiology | At diagnosis | Defining | HP:0000512 |
| RPE changes / pigmentary retinopathy, mid-peripheral greyish-white discoloration | Sign (fundus) | Progressive | Frequent | HP:0000580 / HP:0007894 |
| Attenuated retinal vasculature | Sign | Advanced | Common | HP:0007843 |
| Optic disc pallor | Sign | Advanced | Reported | HP:0000543 |
| Macular atrophy / "coloboma-like" macular lesion | Sign | Variable | Reported in some | HP:0007754 |
| Cataract (anterior polar / posterior subcapsular) | Sign | Variable | Reported in some families | HP:0000518 |

Representative description: childhood-onset visual impairment, "reorganisation of the retinal pigment epithelium with mid-periphery greyish-white discolouration, attenuated retinal vasculatur and optic disc pallor," with a coloboma-like macular lesion in one case, plus anterior polar/posterior subcapsular cataract [H, PMID 25091951].

**Severity:** generally moderate-to-severe with legal blindness common by adulthood; **variable expressivity** even within families. **Quality-of-life impact:** substantial — early loss of central acuity, color vision and glare disability impair reading, schooling, driving (precluded), and independent navigation; night blindness and field constriction add mobility impairment. No disease-specific EQ-5D/SF-36 datasets are published.

---

## 4. Genetic / Molecular Information

**Causal gene.** **ADAM9** (OMIM 602713; HGNC:216; 8p11.22). A single-gene, autosomal-recessive disorder.

**Pathogenic variants.**
- **Variant types:** nonsense, frameshift (small indels), canonical splice-site, and multi-exon genomic **deletions** — all converging on **loss of function/null alleles**. Examples:
  - Homozygous splice-acceptor **c.1396-2A>G** (exon 14 region) — consanguineous Egyptian family [H, PMID 25091951].
  - Compound-heterozygous ADAM9 variants detected by exome sequencing in a child with CRD [H, PMID 25546566].
  - (Animal homolog, mechanistically informative) canine **deletion of exons 15–16** → frameshift + premature stop, removing catalytic/downstream domains [D, PMIDs 20806078, 20691256].
- **ACMG classification:** reported disease alleles are predominantly **pathogenic / likely pathogenic** (null variants meeting PVS1 + recessive segregation + rarity).
- **ClinVar spectrum (NCBI E-utilities, 2026):** 718 ADAM9 records — **101 Pathogenic, 17 Likely pathogenic, 623 VUS**. Among sequence-level P/LP variants the molecular consequences are overwhelmingly **truncating/LoF: nonsense (16), frameshift (7), splice-acceptor (6), splice-donor (6), with only 1 missense**; types include SNVs (28) and small deletions (11). Many "pathogenic" entries are large regional copy-number gains/losses spanning ADAM9 among multiple genes and are **not** CORD9-specific. The large VUS fraction and low pathogenic-missense count mean splice/functional assessment and intragenic deletion/CNV detection materially aid molecular diagnosis. *(Retrieved programmatically via ClinVar E-utilities.)*
- **Allele frequency:** individual pathogenic alleles are rare/absent in gnomAD (consistent with a rare recessive disorder); specific population allele frequencies are not systematically catalogued.
- **Population genetic constraint (gnomAD, GRCh38; ENSG00000168615, chr8:38,996,754–39,105,445):** ADAM9 is **not haploinsufficient** — **pLI = 2.4×10⁻⁶ (≈0)**, **oe_lof = 0.499 (90% CI 0.40–0.63; LOEUF ≈ 0.63)**, 54 observed vs 108.1 expected LoF variants (LoF z = 4.42; missense z = 2.26, oe_mis = 0.83). Heterozygous LoF is tolerated (healthy carriers), concordant with autosomal-recessive, biallelic-null disease biology and excluding a dominant/haploinsufficiency mechanism. *(Retrieved programmatically via gnomAD GraphQL API.)*
- **Origin:** **germline**, biallelic. (Somatic ADAM9 changes occur in cancer but are unrelated to the retinopathy.)
- **Functional consequence:** **loss of function** of the ADAM9 metalloprotease/adhesion protein (not gain-of-function or dominant-negative), confirmed by concordant human null mutations and knockout mouse/dog phenotypes [H/M/D, PMID 19409519].

**Modifier genes.** None established; intra-familial variable expressivity suggests unidentified genetic/environmental modifiers.

**Epigenetic information.** No disease-specific methylation/chromatin findings reported.

**Chromosomal abnormalities.** Large intragenic deletions (exon-level) occur; no recurrent whole-chromosome aneuploidy or translocation is associated.

Suggested ontology: gene **HGNC:216**; GO molecular function **GO:0004222** (metalloendopeptidase activity), **GO:0008237** (metallopeptidase activity).

---

## 5. Environmental Information

- **Environmental factors:** none established as causal or necessary; the disease is fully penetrant genetically.
- **Lifestyle factors:** no proven role; general counseling on UV/blue-light protection and smoking avoidance is extrapolated, not evidence-based for ADAM9.
- **Infectious agents:** not applicable — non-infectious Mendelian disease.

(Mechanistic aside: ADAM9 expression is metabolically regulated — e.g., upregulated under high glucose in RPE [V, PMID 35163068] — but no environmental trigger is implicated in CORD9 onset.)

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic null ADAM9 variants** → **loss of functional ADAM9 metalloprotease/adhesion protein** at the apical surface of the RPE (and photoreceptor interface). *[demonstrated — human null mutations + KO models]*
2. Loss of ADAM9 → **disorganization of RPE apical processes/microvilli** and loss of normal integrin/ectodomain-shedding–mediated adhesion between RPE and photoreceptor outer segments. *[demonstrated in mouse and dog]* "the apical processes of the retinal pigment epithelium (RPE) cells are disorganized and contact between photoreceptor outer segments (POSs) and the RPE apical surface is compromised" [M, PMID 19409519]; "the primary lesion … appears to be a failure of the apical microvilli of the retinal pigm[ent epithelium]" [D, PMID 20806078].
3. Disrupted POS–RPE apposition → **expansion of the subretinal space**. A compensatory response occurs: RPE forms **elongated pseudopods** that bridge the gap to continue ingesting outer-segment tips, temporarily preserving outer-segment renewal and photoreceptor function. *[demonstrated in mouse]* [M, PMID 41642651].
4. When compensation fails over time → **progressive photoreceptor outer-segment shortening/disorganization and outer nuclear layer thinning**, with RPE basal deposits and macrophage infiltration. *[demonstrated in aged KO mice]* [M, PMID 19409519].
5. Photoreceptor loss (cones preferentially, then rods) → **reduced photopic then scotopic ERG, loss of central/color vision, photophobia, then night blindness and field constriction** — the clinical cone-rod dystrophy. *[inferred from model + human concordance]*

   **Branch (modulatory, inferred):** Because ADAM9 sheds the phagocytic receptor **MerTK** and regulates **ADAM10 α-secretase**, ADAM9 loss may also perturb outer-segment phagocytosis and local growth-factor/receptor signaling at the RPE, contributing to the renewal defect [V, PMIDs 35163068, 21956108]. This branch is mechanistically plausible but not yet demonstrated to drive CORD9.

**Molecular pathways / processes.** Ectodomain shedding (sheddase activity), integrin-β1–mediated cell adhesion/migration, and signaling modulation (ADAM9 influences EGFR/AKT, mTOR, NF-κB, STAT3 pathways) [R, PMID 42171934]; physiologically relevant RPE process is **photoreceptor outer-segment phagocytosis/renewal** and POS–RPE adhesion. Suggested GO terms: **GO:0006911/GO:0043277** (phagocytosis / apoptotic cell clearance), **GO:0007155** (cell adhesion), **GO:0006508** (proteolysis), **GO:0001895** (retina homeostasis).

**Protein dysfunction.** ADAM9 is a type-I transmembrane multidomain metalloprotease (prodomain, catalytic Zn-metalloprotease, disintegrin, cysteine-rich, EGF-like, transmembrane, cytoplasmic). Disease alleles truncate/abolish the protein → **complete loss of catalytic and adhesion function** [R, PMID 42171934; H, PMID 19409519].

**Cell types / compartments.** Primary: **retinal pigment epithelial cell (CL:0002586)** apical microvilli; secondary: **retinal cone (CL:0000573)** then **rod (CL:0000604)** photoreceptors. Subcellular: plasma membrane / apical microvilli, extracellular/subretinal space; (ADAM9 also at endosomes/Golgi during trafficking).

**Immune/inflammation, tissue-damage.** Secondary **macrophage** recruitment and **RPE basal (drusen-like) deposits** in late disease [M, PMID 19409519]; chronic photoreceptor loss is degenerative, not autoimmune. Oxidative stress is a generic downstream contributor (inferred).

---

## 7. Anatomical Structures Affected

- **Organ level — primary:** **eye / retina** (UBERON:0000970 eye; UBERON:0000966 retina). **Body system:** visual/nervous system.
- **Secondary:** **lens** (cataract in some families; UBERON:0000965), optic nerve head (pallor; UBERON:0000941), retinal vasculature (attenuation; UBERON:0003516).
- **Tissue/cell level:** **retinal pigment epithelium** (UBERON:0001782; cell CL:0002586) — the initiating site; **neural retina photoreceptor layer** — cones (CL:0000573) then rods (CL:0000604); outer nuclear layer thinning.
- **Subcellular:** RPE **apical microvilli / processes** and **plasma membrane**; **subretinal space** (POS–RPE interface). Suggested GO cellular component: **GO:0005886** (plasma membrane), **GO:0005902** (microvillus).
- **Localization / laterality:** **bilateral**, generally symmetric; disease is **posterior-segment** centered with early macular/central and later mid-peripheral involvement.

---

## 8. Temporal Development

- **Onset:** **early childhood** ("early-onset CRD") in humans [H, PMID 19409519]; childhood-onset visual impairment typical [H, PMID 25091951]. Pattern is **insidious/chronic**, not acute.
- **Progression:** slowly **progressive** over years to decades; **cone-first** functional loss (acuity, color, photophobia) preceding **rod** involvement (night blindness, field loss). Variable rate and expressivity.
- **Stages:** early (photophobia, reduced acuity, abnormal photopic ERG, subtle RPE changes) → intermediate (color/field loss, pigmentary RPE changes, vascular attenuation) → advanced (macular/widespread atrophy, severe visual loss / legal blindness, optic disc pallor).
- **Course / duration:** **chronic, lifelong**; no spontaneous remission. (Animal models are informative on tempo: mouse is comparatively mild/late — photoreceptors near-normal at 12 months, degeneration by 20 months [M, PMID 19409519]; dog disease is adult/late-onset with variable, at times very late onset [D, PMID 20691256].)
- **Critical window for intervention:** the period of preserved photoreceptors with compensatory RPE pseudopods [M, PMID 41642651] defines a **therapeutic window** before irreversible photoreceptor loss (inferred).

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (AR) [H, PMID 19409519].
- **Penetrance:** essentially **complete** in biallelic carriers (age-dependent emergence of signs).
- **Expressivity:** **variable**, including intra-familial variability (e.g., associated cataract in some members) [H, PMID 25091951].
- **Carrier frequency:** heterozygous carriers unaffected; pathogenic alleles individually rare in gnomAD. Specific carrier-frequency estimates are not established, but gnomAD constraint confirms heterozygous LoF is tolerated (**pLI ≈ 0, LOEUF ≈ 0.63**; 54 obs vs 108 exp LoF variants), consistent with a healthy-carrier recessive model.
- **Consanguinity / founder effects:** strongly associated with **consanguineous pedigrees** (autozygosity); reported families from Egypt, Middle East, South Asia and the UK [H, PMIDs 19409519, 25091951, 25546566]. No single global founder allele; private family mutations predominate.
- **Anticipation / mosaicism:** not applicable (no repeat expansion); germline mosaicism not reported.
- **Epidemiology:** **rare.** No disease-specific prevalence/incidence is published. For context, all cone-rod dystrophies together have an estimated prevalence of ~1 in 30,000–40,000, and ADAM9 is a **minor** contributor overall but enriched in consanguineous populations. Both sexes affected equally (**M:F ≈ 1:1**), consistent with autosomal inheritance.

---

## 10. Diagnostics

**Clinical / functional tests.**
- **Full-field electroretinography (ERG):** reduced responses with **photopic (cone) dysfunction ≥ scotopic (rod)** — hallmark of cone-rod pattern (HPO HP:0000512) [H/M, PMID 19409519].
- **Optical coherence tomography (OCT):** outer-retinal/ellipsoid-zone disruption, ONL thinning, RPE changes, subretinal-space abnormalities.
- **Fundus examination / autofluorescence:** RPE reorganization, mid-peripheral greyish-white discoloration, vascular attenuation, optic disc pallor, macular atrophy [H, PMID 25091951].
- **Color vision and visual-field testing:** early dyschromatopsia; progressive field constriction.
- Biopsy/histopathology is not used clinically (findings known from models: disorganized RPE apical microvilli, POS–RPE separation, basal deposits, macrophages).

**Genetic testing (definitive).**
- Approach: **molecular genetic testing of ADAM9** via **inherited-retinal-disease gene panels** or **whole-exome/whole-genome sequencing**; single-gene/Sanger confirmation of candidate variants; **CMA/deletion analysis** to detect multi-exon deletions (important given large-deletion alleles). Exome sequencing has directly diagnosed ADAM9 CRD in children [H, PMID 25546566]. Targeted enrichment panels (e.g., IROme) plus Sanger confirmation were used historically [H, PMID 25091951]. Because the ClinVar P/LP spectrum is truncating/splice-dominated with a large VUS fraction (623 VUS) and few pathogenic missense, **including copy-number/intragenic-deletion analysis and RNA/splice assays improves diagnostic yield**.
- Karyotype/FISH/mtDNA/repeat-expansion testing: not indicated.

**Clinical criteria / differential diagnosis.** Diagnosis = compatible cone-rod ERG/OCT phenotype + biallelic pathogenic ADAM9 variants. **Differentials:** other cone-rod dystrophies (ABCA4, CRX, GUCY2D, RPGR, RIMS1, PROM1, etc.), achromatopsia (CNGB3/CNGA3), Leber congenital amaurosis, and Stargardt disease — distinguished by gene testing and phenotype nuances.

**Screening.** Cascade/carrier testing within affected families; preconception/prenatal testing possible given known familial variants. No population newborn screening.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **normal life expectancy**; ADAM9 retinopathy is **not life-limiting** — it is an isolated (non-syndromic) ocular disorder.
- **Morbidity / disability:** **progressive visual disability** is the principal burden — early loss of central acuity, color vision and glare tolerance, later night blindness and peripheral field loss, frequently culminating in **legal blindness** in adulthood. Major impact on education, employment, mobility and independence (ICF visual-function domains).
- **Disease course / complications:** chronic progressive vision loss; cataract in some patients (surgically treatable); no systemic complications.
- **Recovery potential:** none spontaneously; vision loss is irreversible once photoreceptors degenerate.
- **Prognostic factors:** earlier onset and more complete null genotypes tend to associate with more severe course (inferred); residual photoreceptor/ellipsoid-zone integrity on OCT is a practical prognostic/therapeutic-window biomarker.

---

## 12. Treatment

**No approved disease-specific or curative therapy currently exists.** Management is **supportive and rehabilitative**:
- **Low-vision rehabilitation** (NCIT: low-vision aids), magnification, high-contrast tools, orientation/mobility training.
- **Photophobia management:** tinted/edge-filter lenses, sunglasses, environmental lighting adaptation.
- **Cataract surgery** when visually significant cataract is present [H, PMID 25091951].
- **Genetic counseling** (see §13).
- **General retinal support:** correction of refractive error; UV protection (prudential).

**Experimental / future directions.**
- **Gene-replacement (AAV-mediated ADAM9 augmentation)** is a biologically rational strategy — ADAM9 is a small, recessive loss-of-function gene expressed in RPE/photoreceptors, matching the paradigm of RPE-directed retinal gene therapy; the preserved-photoreceptor/pseudopod window [M, PMID 41642651] supports a treatable interval. (Status: **preclinical/investigational**; no approved product. No specific completed human trial identified in this review.)
- Other modalities under general IRD research (optogenetics, cell replacement) are not ADAM9-specific.

**Pharmacogenomics:** not applicable. **Treatment outcomes / adverse events:** none established for disease-specific therapy.

Suggested NCIT concepts: Gene Therapy, Adeno-Associated Viral Vector, Supportive Care, Cataract Surgery, Low Vision Aid.

---

## 13. Prevention

- **Primary prevention:** not possible for a monogenic recessive disease except via **reproductive genetic counseling**. In consanguineous communities, awareness and **carrier screening** can reduce incidence.
- **Secondary prevention:** early diagnosis (gene testing in children with photophobia/reduced acuity/abnormal cone ERG) to enable timely low-vision support and candidacy for future therapies.
- **Tertiary prevention:** manage complications (cataract surgery), maximize residual vision via rehabilitation.
- **Genetic counseling:** recurrence risk 25% for offspring of two carriers; **cascade carrier testing**, **preimplantation genetic testing (PGT)** and **prenatal diagnosis** available where familial variants are known. Counseling on consanguinity-related risk is central.
- **Public-health / behavioral / immunization measures:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / natural disease:** Naturally occurring ADAM9 retinopathy is well documented in the **dog (*Canis lupus familiaris*, NCBI Taxon 9615)** — **canine cone-rod dystrophy 3 (crd3)** and **generalized progressive retinal atrophy (gPRA)** in the **Glen of Imaal Terrier** breed (VBO/breed-specific), caused by an **ADAM9 exon 15–16 deletion** [D, PMIDs 20806078, 20691256] (OMIA entry for ADAM9/cone-rod dystrophy in dog).
- **Orthologous genes:** mouse *Adam9* (NCBI Gene 11491), dog *ADAM9* — functionally conserved.
- **Comparative biology:** across human, mouse and dog the **primary lesion is the RPE apical microvilli / POS–RPE junction**, confirming deep evolutionary conservation of ADAM9's role in retinal homeostasis; canine disease is a validated large-animal model "with superior potential to elucidate functional consequences of the … human ADAM9 null mutations" [D, PMID 20691256].
- **Zoonotic potential:** none (genetic disease).

---

## 15. Model Organisms

- **Mouse (*Mus musculus*):** **Adam9-knockout** mouse — reduced photoreceptor ERG responses; at 12 months RPE apical-process disorganization with normal photoreceptors; by 20 months progressive degeneration (ONL thinning, POS disorganization, RPE basal deposits, macrophages) [M, PMID 19409519]. Recent work shows **compensatory RPE pseudopods** maintaining outer-segment renewal before degeneration [M, PMID 41642651]. **Strengths:** genetically defined null matching human LOF; dissects RPE-interface mechanism. **Limitation:** milder/later phenotype than human (species difference in tempo). Resource: MGI (Adam9).
- **Dog (Glen of Imaal Terrier):** naturally occurring ADAM9-null crd3/gPRA — adult/late-onset, variable; valuable **large-eye preclinical/therapeutic model** [D, PMIDs 20806078, 20691256]. Resource: OMIA.
- **Model types available:** germline knockout (mouse); spontaneous null (dog). In-vitro **RPE cell models (e.g., ARPE-19)** are used to study ADAM9 sheddase biology (MerTK shedding) [V, PMID 35163068].
- **Phenotype recapitulation:** both mouse and dog reproduce the **core RPE apical-microvilli / POS–RPE junction lesion** and progressive photoreceptor loss; they under-represent the **early, severe cone-dominated childhood onset** seen in humans.

---

## Evidence Summary (key PMIDs)

| PMID | Type | Contribution |
|---|---|---|
| 19409519 | H/M | Landmark: ADAM9 null mutations cause human early-onset CRD; KO mouse; POS–RPE junction lesion |
| 25091951 | H | Novel homozygous splice variant c.1396-2A>G; fundus phenotype; cataract association |
| 25546566 | H | Exome sequencing diagnoses ADAM9 CRD in a child |
| 38028590 | H | ADAM9 among genes in a multi-family cone-rod dystrophy cohort |
| 20806078 | D | Canine crd3 (Glen of Imaal Terrier); establishes homology with human CORD9; RPE microvilli failure |
| 20691256 | D | Canine gPRA ADAM9 exon 15–16 deletion; model for human disease |
| 41642651 | M | RPE pseudopods maintain outer-segment renewal despite subretinal space expansion |
| 42171934 | R | ADAM9 biology: domains, isoforms, substrates, signaling pathways |
| 35163068 | V | ADAM9 sheds MerTK in RPE; metabolic regulation (high glucose) |
| 21956108 | V | ADAM9 regulates ADAM10 α-secretase activity |
| 17704059 | V | ADAM9 disintegrin-cysteine-rich domain binds β1 integrin (adhesion/motility) |

### Database-derived quantitative evidence (this investigation)

| Source | Metric | Value | Implication |
|---|---|---|---|
| gnomAD (GRCh38) | pLI | 2.4×10⁻⁶ (≈0) | Not haploinsufficient → recessive |
| gnomAD | oe_lof / LOEUF | 0.50 / ≈0.63 (obs 54 vs exp 108 LoF) | Under purifying selection but LoF tolerated in heterozygotes |
| gnomAD | missense z / oe_mis | 2.26 / 0.83 | Mild missense constraint |
| ClinVar | Total records | 718 | — |
| ClinVar | Pathogenic / Likely-path / VUS | 101 / 17 / 623 | Large VUS burden; interpretation challenge |
| ClinVar | P/LP sequence consequences | nonsense 16, frameshift 7, splice 12, missense 1 | Truncating/LoF-dominated disease spectrum |

**Convergent conclusion:** gnomAD constraint (healthy heterozygous carriers) and the ClinVar truncating-allele spectrum independently confirm that CORD9 is an **autosomal-recessive, biallelic loss-of-function** disorder — not dominant/haploinsufficient and not gain-of-function.

---

## Key Findings & Hypothesis Status

**Supported (evidence-backed):**
1. ADAM9 biallelic null mutations cause autosomal-recessive early-onset cone-rod dystrophy 9 (CORD9) [H, PMID 19409519].
2. The initiating lesion is at the RPE apical microvilli / POS–RPE junction, upstream of photoreceptor death [M/D, PMIDs 19409519, 20806078; compensatory RPE pseudopods, PMID 41642651].
3. ADAM9 is a sheddase/adhesion metalloprotease (MerTK, ADAM10, β1-integrin) whose loss disrupts the RPE–photoreceptor interface [R/V, PMIDs 42171934, 35163068, 21956108, 17704059].
4. Disease is typically early-onset/severe, overlapping the EOSRD/LCA spectrum [H, PMIDs 25091951, 25546566, 38892339].
5. gnomAD constraint shows ADAM9 is NOT haploinsufficient (pLI≈0, LOEUF≈0.63) → recessive, healthy-carrier model.
6. ClinVar P/LP spectrum is truncating/LoF-dominated (nonsense/frameshift/splice ≫ missense), with a large VUS burden.
7. Cross-species mouse and dog (Glen of Imaal Terrier) models recapitulate the RPE-interface lesion [M/D, PMIDs 19409519, 20691256].

**Refuted / excluded:** dominant or gain-of-function mechanism (excluded by pLI≈0 + recessive segregation + null-allele spectrum); syndromic/systemic involvement (disease is isolated/non-syndromic, normal lifespan); infectious/environmental causation (none).

## Limitations and Future Directions

- The literature base is **small** (few consanguineous families, individual patients), so **phenotype frequencies, prevalence, penetrance and genotype–phenotype correlations are approximate**. No large natural-history or QoL dataset exists.
- Mechanistic depth comes largely from **mouse/dog models**, which are milder/later-onset than human disease; direct human RPE/photoreceptor molecular data are limited.
- **Gene therapy** is biologically well-justified but remains **preclinical/investigational**; no specific completed human trial was identified here — a priority for future work.
- Several ontology term suggestions (HPO/GO/CL/UBERON) should be verified against current ontology releases before database ingestion.

---

### One-paragraph answer
ADAM9-Related Retinopathy (MONDO:0800398) is **cone-rod dystrophy 9 (CORD9)**, an autosomal-recessive, early-childhood-onset, progressive retinal dystrophy caused by **biallelic null (loss-of-function) mutations in the metalloprotease gene ADAM9**. Loss of ADAM9 disrupts the apical microvilli of the retinal pigment epithelium and the photoreceptor-outer-segment–RPE junction — the initiating lesion — leading to subretinal-space expansion and, over time, cone-predominant then rod photoreceptor degeneration with reduced ERG, photophobia, color-vision and acuity loss, and later night blindness and field constriction, culminating in severe low vision/legal blindness but normal lifespan.


## Artifacts

- [OpenScientist final report](ADAM9-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ADAM9-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:20806078` *(abstract only)*: "the primary lesion … appears to be a failure of the apical microvilli of the retinal pigm[ent epithelium]"
  - closest text in source: "Light and electron microscopy established that, as in ADAM9 knockout mice, the primary lesion in crd3 appears to be a failure of the apical microvilli of the retinal pigment epithelium to appropriately invest photoreceptor outer segments"
- `PMID:20691256` *(abstract only)*: "with superior potential to elucidate functional consequences of the … human ADAM9 null mutations"
  - closest text in source: "Hence, the identification of the genetic defect underlying gPRA in the GIT represents a suitable model for cone-rod dystrophy of humans, with superior potential to elucidate functional consequences of the recently described null mutations in the human ADAM9 gene."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 8 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000613` (1 mention) - the report calls it "Frequent"; HP calls it **Photophobia**
- `HP:0000551` (1 mention) - the report calls it "Frequent"; HP calls it **Color vision defect**
- `HP:0000662` (1 mention) - the report calls it "Common as disease advances"; HP calls it **Nyctalopia**
- `HP:0001133` (1 mention) - the report calls it "Common"; HP calls it **Constriction of peripheral visual field**
- `HP:0000639` (1 mention) - the report calls it "Variable"; HP calls it **Nystagmus**
- `HP:0000512` (2 mentions) - the report calls it "Defining"; HP calls it **Abnormal electroretinogram**
- `HP:0007843` (1 mention) - the report calls it "Common"; HP calls it **Attenuation of retinal blood vessels**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `ORPHA:1872` - called "Cone-rod dystrophy", "Orphanet:** within "Cone-rod dystrophy"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.