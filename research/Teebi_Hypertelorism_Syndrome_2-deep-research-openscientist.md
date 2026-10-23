---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T17:31:37.444145'
end_time: '2026-10-22T18:06:48.283325'
duration_seconds: 2110.84
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Teebi Hypertelorism Syndrome 2
  mondo_id: MONDO:0030674
  category: Mendelian
  causal_genes: CDH11
  omim_id: OMIM:619736
  synonyms: TBHS2
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
citation_count: 12
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 0
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0000316
    reported_labels:
    - Physical / clinical sign
    ontology_label: Hypertelorism
  - term_id: HP:0003196
    reported_labels:
    - Physical
    ontology_label: Short nose
  - term_id: HP:0000047
    reported_labels:
    - Physical / genital
    ontology_label: Hypospadias
  - term_id: HP:0000049
    reported_labels:
    - Physical / genital
    ontology_label: Shawl scrotum
  - term_id: HP:0001627
    reported_labels:
    - Clinical
    ontology_label: Abnormal heart morphology
  - term_id: HP:0001537
    reported_labels:
    - Physical
    ontology_label: Umbilical hernia
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Teebi_Hypertelorism_Syndrome_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Teebi_Hypertelorism_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Teebi Hypertelorism Syndrome 2
- **MONDO ID:** MONDO:0030674 (if available)
- **Causal gene(s):** CDH11
- **OMIM:** OMIM:619736
- **Synonyms:** TBHS2
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Teebi Hypertelorism Syndrome 2** covering all of the
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

# Teebi Hypertelorism Syndrome 2 (THS2 / TBHS2): A Comprehensive Disease Characteristics Report

**Disease:** Teebi Hypertelorism Syndrome 2 · **MONDO:** MONDO:0030674 · **OMIM:** 619736 · **Causal gene:** *CDH11* (cadherin-11 / OB-cadherin; HGNC:1750; 16q21) · **Category:** Mendelian, autosomal dominant

---

## Summary

**Teebi Hypertelorism Syndrome 2 (THS2) is a rare autosomal-dominant congenital craniofacial disorder caused by heterozygous missense variants in *CDH11*, the gene encoding cadherin-11 (OB-cadherin).** This is the central, identifier-anchored fact of this report: although the disease name is a serial-numbered "hypertelorism syndrome," THS2 is specifically a *CDH11* disorder (OMIM 619736; MONDO:0030674), distinct from THS1, which is caused by *SPECC1L* (OMIM 145420). The causal gene was established by Li et al. in 2021, who reported 19 affected subjects from 9 families carrying heterozygous *CDH11* missense variants ([PMID: 33811546](https://pubmed.ncbi.nlm.nih.gov/33811546/)).

Mechanistically, the pathogenic variants cluster in the extracellular (EC) domains of cadherin-11 — particularly the EC2–EC3 and EC3–EC4 calcium-binding linker regions and the EC1 trans-dimerization pocket. These residues are highly conserved across vertebrates and across classical cadherins, and they are predicted to impair Ca²⁺ binding and calcium-dependent homophilic cell–cell adhesion. Functional assays indicate a **dominant-negative mechanism**: the variants decrease cell–cell/cell–substrate adhesion and increase cell migratory behavior. Because cadherin-11 is strongly expressed in human facial mesenchyme and drives cranial neural crest cell (CNCC) contact-inhibition-of-locomotion and collective migration during frontonasal morphogenesis, its dysfunction produces the characteristic craniofacial phenotype: hypertelorism (widely spaced eyes), prominent forehead, short nose with a broad/depressed nasal root, and associated male genital anomalies (hypospadias, shawl scrotum), typically with preserved cognition.

*CDH11* is an allelic locus with a striking genotype–phenotype dichotomy: **monoallelic missense** variants cause the dominant THS2, whereas **biallelic loss-of-function** variants cause the more severe recessive Elsahy-Waters syndrome (EWS/branchio-skeleto-genital syndrome; OMIM 211380). The two conditions are now regarded as a *CDH11*-related spectrum. There is no disease-specific therapy; management is supportive and surgical (hypertelorism correction, hypospadias repair). This report synthesizes 8 confirmed findings and 35 reviewed papers across all 15 requested disease-characteristic domains, flagging where primary evidence is strong (molecular genetics, developmental mechanism) and where it is sparse or absent (epidemiology, prognosis, treatment trials, animal models of THS2 specifically).

---

## Key Findings

### Finding 1 — THS2 is caused by heterozygous *CDH11* missense variants

Teebi Hypertelorism Syndrome 2 is caused by heterozygous (monoallelic) missense variants in *CDH11*. The defining cohort study by Li et al. (2021) reported THS in 19 subjects from 9 families, all carrying *CDH11* heterozygous missense variants. Critically, every affected residue lies in the **extracellular region** of cadherin-11, and all are highly conserved across vertebrate species and across classical cadherins. Six of the reported variants cluster around the EC2–EC3 and EC3–EC4 linker regions and are predicted to affect Ca²⁺ binding, thereby impairing cell adhesion.

> *"We report THS due to CDH11 heterozygous missense variants on 19 subjects from 9 families. All affected residues in the extracellular region of Cadherin-11 (CHD11) are highly conserved across vertebrate species and classical cadherins."* — [PMID: 33811546](https://pubmed.ncbi.nlm.nih.gov/33811546/)

This is **human clinical + genetic evidence** from a multi-family cohort, and it is the primary citation anchoring THS2 = OMIM 619736 = MONDO:0030674 to the *CDH11* gene.

### Finding 2 — *CDH11* is an allelic locus: a dominant (missense) and a recessive (LOF) disorder

*CDH11* produces two distinct Mendelian disorders depending on zygosity and variant class:

| Feature | Teebi Hypertelorism Syndrome 2 (THS2) | Elsahy-Waters Syndrome (EWS/BSGS) |
|---|---|---|
| OMIM | 619736 | 211380 |
| Inheritance | Autosomal dominant | Autosomal recessive |
| Variant class | Heterozygous **missense** (EC domains) | Biallelic **truncating / loss-of-function** |
| Proposed mechanism | Dominant-negative adhesion defect | Loss of function |
| Core phenotype | Hypertelorism, prominent forehead, short nose, genital anomalies; usually normal cognition | Characteristic face, premature tooth loss, vertebral & genital anomalies, intellectual disability |

Harms et al. (2018, [PMID: 29271567](https://pubmed.ncbi.nlm.nih.gov/29271567/)) and Castori et al. (2018, [PMID: 30194892](https://pubmed.ncbi.nlm.nih.gov/30194892/)) established that **biallelic truncating/LOF** *CDH11* variants cause EWS. Harms et al. explicitly *"confirms that EWS is caused by biallelic CDH11 loss of function mutations."* Kuroda et al. (2024, [PMID: 37646430](https://pubmed.ncbi.nlm.nih.gov/37646430/)) describe a Japanese THS patient with a novel EC1-domain variant and conclude that *"THS and EWS may represent a spectrum of CDH11-related disorders,"* noting overlapping features (polysyndactyly, broad thumb, cutaneous syndactyly). Castori et al. identified a *"novel homozygous nonsense variant in the first exon"* of *CDH11* producing a truncated protein in EWS, supporting cadherin-11 as *"a key player in axial and craniofacial malformations."*

### Finding 3 — Cadherin-11 drives cranial neural crest cell adhesion and migration (the developmental basis of the craniofacial phenotype)

The mechanistic link between a *CDH11* adhesion defect and craniofacial malformation runs through the cranial neural crest. In *Xenopus*, cadherin-11 is predominantly expressed in cranial neural crest cells (CNCCs) and is required for their directional, collective migration via **contact inhibition of locomotion (CIL)**:

> *"we demonstrate that Xenopus cadherin-11 (Xcad-11) mediated cell-cell adhesion is necessary in CIL for directional and collective migration of CNC cells. Reduction of Xcad-11 adhesive function resulted in higher invasiveness of CNC due to loss of CIL."* — Becker et al. 2013, [PMID: 24392028](https://pubmed.ncbi.nlm.nih.gov/24392028/)

Beyond adhesion, cadherin-11 tunes CNCC **specification and proliferation** by regulating the nuclear pool of β-catenin and the Wnt targets *cyclin D1* and *c-myc* through its cytoplasmic β-catenin-binding domain (Koehler et al. 2013, [PMID: 23958437](https://pubmed.ncbi.nlm.nih.gov/23958437/)). Its shed EC1–3 ectodomain binds ErbB2 and stimulates PI3K/Akt phosphorylation to promote CNC migration (Mathavan et al. 2017, [PMID: 29190819](https://pubmed.ncbi.nlm.nih.gov/29190819/)):

> *"EC1-3 stimulates phosphorylation of Akt, a target of PI3K, in X.laevis CNC"* — [PMID: 29190819](https://pubmed.ncbi.nlm.nih.gov/29190819/)

This is **model-organism (Xenopus) evidence** that establishes cadherin-11 as a master regulator of the exact developmental process whose disruption produces facial clefting/dysmorphism.

### Finding 4 — Teebi hypertelorism syndrome is genetically heterogeneous; THS1 (*SPECC1L*) and THS2 (*CDH11*) converge on CNCC adhesion

THS1 (OMIM 145420) is associated with *SPECC1L* variants. SPECC1L is an adherens-junction protein that, like cadherin-11, acts in the cranial neural crest:

> *"It modulates PI3K-AKT signaling and controls cranial neural crest cell delamination during facial morphogenesis."* — Bhoj et al. 2019, [PMID: 30472488](https://pubmed.ncbi.nlm.nih.gov/30472488/)

Thus both Teebi hypertelorism genes act in **cell adhesion / adherens junctions within migrating cranial neural crest**, and both converge on PI3K-AKT signaling. This convergence provides a unifying mechanistic framework: THS is fundamentally a **"neurocristopathy of adhesion,"** reachable by lesions in more than one adhesion-junction gene. This is important for differential diagnosis and for interpreting the overlapping facial gestalt.

### Finding 5 — *CDH11* is a highly constrained gene, consistent with dominant missense pathogenicity

Population constraint metrics from gnomAD v2.1.1 for *CDH11* (ENSG00000140937, HGNC:1750, GRCh38 chr16:64,943,753–65,126,112; cytoband 16q21):

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 1.00 | Extremely LoF-intolerant |
| LOEUF (o/e LoF) | 0.162 (90% CI 0.102–0.268) | Strong depletion of LoF variants |
| LoF Z | 5.85 | Highly significant LoF constraint |
| Missense Z | 2.45 | Significant missense constraint |
| Missense o/e | 0.82 | Mild depletion of missense variation |

The gene is extremely intolerant to loss-of-function and significantly constrained for missense variation. This constraint profile is consistent with the observation that THS2 arises specifically from missense (not null) alleles acting dominantly — null alleles are strongly selected against, and the dominant disorder is produced by a qualitatively altered (dominant-negative) protein rather than simple haploinsufficiency. (Note: the recessive EWS requires *two* LoF hits, consistent with heterozygous LoF being tolerated/non-pathogenic for THS2.)

### Finding 6 — ClinVar documents recurrent heterozygous *CDH11* missense variants classified Pathogenic/Likely pathogenic for THS2

A ClinVar query (2026) against "Teebi hypertelorism syndrome 2" returns exclusively **missense** alleles (all on transcript NM_001797.4):

| Variant (cDNA) | Protein | Domain / note | Classification |
|---|---|---|---|
| c.164G>C | p.Trp55Ser | EC1 (trans-dimer) | Pathogenic |
| c.229C>T | p.Leu77Phe | EC1 | Likely pathogenic |
| c.778G>A | p.Asp260Asn | EC2–EC3 linker | Pathogenic/Likely pathogenic |
| c.780T>A | p.Asp260Glu | EC2–EC3 linker (recurrent codon) | Pathogenic |
| c.835G>C | p.Glu279Gln | EC3 | Pathogenic |
| c.979G>T | p.Gly327Trp | — ("CDH11-related disorder") | Likely pathogenic |
| c.1121T>A | p.Val374Glu | EC3–EC4 linker | Pathogenic |
| c.1145T>C | p.Met382Thr | — | VUS |
| c.1600G>C | p.Glu534Gln | — | VUS |
| c.1969C>T | p.Arg657Cys | — | VUS |
| c.2152G>A | p.Asp718Asn | — | VUS |

Key observations: (1) **all reported THS2 pathogenic/likely-pathogenic alleles are missense**; (2) **codon Asp260 is a recurrent mutational hotspot** (both p.Asp260Asn and p.Asp260Glu reported), consistent with a critical Ca²⁺-coordinating residue in the EC2–EC3 linker; (3) no pathogenic *CDH11* variant carries a population-frequency flag, consistent with absence from population controls (de novo or private familial variants).

### Finding 7 — Functional assays demonstrate a dominant-negative mechanism: decreased adhesion, increased migration

Li et al. (2021) performed functional characterization of THS2 variants:

> *"five variants from the EC1, EC2-EC3 linker, and EC3 regions significantly reduced the cell-substrate trans adhesion activity and one variant from EC3-EC4 linker results in changes in cell morphology, focal adhesion, and migration, suggesting dominant negative effect."* — [PMID: 33811546](https://pubmed.ncbi.nlm.nih.gov/33811546/)

Two variants (c.164G>C, p.Trp55Ser; c.418G>A, p.Glu140Lys) are predicted to directly disrupt **trans-homodimer formation**. Immunohistochemistry localized the protein to the relevant tissue:

> *"Immunohistochemical study demonstrates that CDH11 is strongly expressed in human facial mesenchyme."* — [PMID: 33811546](https://pubmed.ncbi.nlm.nih.gov/33811546/)

The authors conclude that *"heterozygous variants in CDH11, which decrease cell-cell adhesion and increase cell migratory behavior, cause a form of THS."* Cohort-distinguishing clinical features — depressed nasal root, cardiac and umbilical defects — helped separate *CDH11*-THS from *SPECC1L*-related hypertelorism and from *CDH11*-related EWS. This is **in vitro functional + human-tissue evidence**, and it is the strongest direct support for the dominant-negative model.

### Finding 8 — *CDH11* shows a mesenchymal/fibroblast-dominant tissue expression pattern (GTEx v8)

GTEx v8 median expression for *CDH11* (ENSG00000140937.13) is highest in mesenchyme-rich tissues:

| Tissue | Median TPM |
|---|---|
| Ovary | 74.7 |
| Cultured fibroblasts | 43.8 |
| Endocervix | 30.2 |
| Lung | 27.2 |
| Coronary artery | 26.5 |
| Aorta | 24.9 |
| Spleen | 22.7 |
| Tibial nerve | 20.1 |
| Uterus | 18.1 |
| Bladder | 14.0 |

This bulk-tissue, mesenchymal/fibroblast-dominant expression pattern complements the facial-mesenchyme immunohistochemistry of Li et al. and the gene's classical identity as "OB-cadherin" in osteoblasts. It is consistent with cadherin-11's role in mesenchymal populations including craniofacial mesenchyme, and it rationalizes the skeletal/connective-tissue involvement seen across the *CDH11*-related spectrum.

---

## Report by Section

### 1. Disease Information

**Overview.** Teebi Hypertelorism Syndrome 2 (THS2; synonym **TBHS2**) is a rare congenital craniofacial dysmorphology syndrome. Its cardinal feature is **hypertelorism** (increased interpupillary/inner-canthal distance; widely spaced eyes), accompanied by a prominent/broad forehead, a short nose with broad or depressed nasal root, and — particularly in males — genital anomalies such as hypospadias and shawl scrotum. Cognition is generally normal. The disorder is one of (at least) two genetically distinct forms of Teebi hypertelorism syndrome.

**Key identifiers.**
- **OMIM:** 619736
- **MONDO:** MONDO:0030674
- **Causal gene:** *CDH11* (cadherin-11 / OB-cadherin), HGNC:1750; NCBI Gene; Ensembl ENSG00000140937; locus 16q21
- **Orphanet / ICD-10 / ICD-11 / MeSH:** No THS2-specific code was retrievable in this investigation; the condition falls under broad categories for congenital facial dysmorphism / hypertelorism. (Gap — see Limitations.)
- **Synonyms:** TBHS2; Teebi hypertelorism syndrome 2; *CDH11*-related Teebi hypertelorism.

**Data provenance.** The knowledge here is derived from **aggregated disease-level resources** (OMIM, ClinVar, gnomAD, GTEx) and from **primary case-cohort literature** (Li et al. 2021; Kuroda et al. 2024), i.e., individual-patient reports aggregated into cohorts — not from EHR-scale datasets.

### 2. Etiology

**Primary cause — genetic.** THS2 is a monogenic Mendelian disorder caused by **heterozygous missense variants in *CDH11***. No environmental, infectious, or multifactorial cause is implicated. Variants affect conserved extracellular residues, predominantly in the EC2–EC3 and EC3–EC4 Ca²⁺-binding linkers and the EC1 trans-dimerization pocket (Findings 1, 6, 7).

**Genetic risk factors.** The causal variants *are* the risk factor; there are no known susceptibility loci or common-variant modifiers for this Mendelian trait. *CDH11* is highly constrained (pLI 1.0; missense Z 2.45), and pathogenic alleles are absent from population controls (Findings 5, 6).

**Environmental risk factors / protective factors / gene–environment interactions.** None identified or expected for a dominant monogenic malformation syndrome. No protective alleles or dietary/lifestyle modifiers are known. This is a *data-absent* category for THS2, which should be stated explicitly in any knowledge-base entry.

### 3. Phenotypes

Phenotypes are drawn from the Li et al. (2021) cohort (n=19) and the Kuroda et al. (2024) case, cross-referenced to the *CDH11*-spectrum literature. Frequencies below are qualitative/cohort-level; precise percentages per feature were not uniformly reported.

| Phenotype | Type | Suggested HPO | Onset / course | Notes |
|---|---|---|---|---|
| Hypertelorism (widely spaced eyes) | Physical / clinical sign | HP:0000316 | Congenital, stable | Cardinal feature |
| Prominent / broad forehead | Physical | HP:0011220 / HP:0000337 | Congenital | |
| Short nose | Physical | HP:0003196 | Congenital | |
| Broad / depressed nasal root | Physical | HP:0000431 / HP:0000458 | Congenital | Cohort-distinguishing (Li 2021) |
| Hypospadias (males) | Physical / genital | HP:0000047 | Congenital | Male-predominant |
| Shawl scrotum | Physical / genital | HP:0000049 | Congenital | |
| Congenital heart defect | Clinical | HP:0001627 | Congenital | Cohort-distinguishing feature |
| Umbilical anomaly (e.g., hernia) | Physical | HP:0001537 | Congenital | Cohort-distinguishing feature |
| Polysyndactyly / broad thumb / cutaneous syndactyly | Physical | HP:0000238 / HP:0011304 / HP:0010554 | Congenital | Overlap with EWS (Kuroda 2024) |
| Normal cognition (typical) | — | — | — | Distinguishes THS2 from EWS |

**Characteristics (overall):** onset is **congenital**; severity is **variable** (variable expressivity); course is **stable/non-progressive** (structural malformation, not a degenerative process). **Quality-of-life impact** derives from craniofacial appearance (psychosocial), potential genital-surgery needs, and any associated cardiac defect; no THS2-specific QoL instrument data (EQ-5D/SF-36) exist (Gap).

### 4. Genetic / Molecular Information

- **Causal gene:** *CDH11* (cadherin-11 / OB-cadherin), HGNC:1750; OMIM gene 600023; NCBI Gene; Ensembl ENSG00000140937; locus 16q21. Transcript NM_001797.4.
- **Pathogenic variants:** exclusively **missense** for THS2 (Findings 1, 6). Classifications per ACMG/AMP in ClinVar range from Pathogenic (e.g., p.Trp55Ser, p.Asp260Glu, p.Glu279Gln, p.Val374Glu) through Pathogenic/Likely pathogenic (p.Asp260Asn) and Likely pathogenic (p.Leu77Phe, p.Gly327Trp) to VUS (p.Met382Thr, p.Glu534Gln, p.Arg657Cys, p.Asp718Asn).
- **Variant type/class:** missense substitutions in extracellular cadherin (EC) domains; mutational hotspot at **codon Asp260** (EC2–EC3 linker).
- **Allele frequency:** pathogenic alleles absent from gnomAD/population databases (de novo or private familial). *CDH11* missense o/e = 0.82; pLI = 1.0.
- **Origin:** germline (constitutional); variants may arise de novo or be transmitted (autosomal dominant). No somatic/oncologic role in THS2 (though *CDH11* is implicated in cancer biology separately).
- **Functional consequence:** **dominant-negative** — reduced trans-adhesion and increased migration (Finding 7); contrast with **loss-of-function** causing recessive EWS (Finding 2).
- **Modifier genes / epigenetics / chromosomal abnormalities:** none established for THS2. *SPECC1L* is not a modifier but an independent cause of the allied THS1.

### 5. Environmental Information

Not applicable. THS2 is a monogenic congenital disorder with no known environmental, lifestyle, or infectious contributors. (Separately, *CDH11* as a protein participates in inflammatory/fibrotic and even host–pathogen contexts — e.g., it serves as a receptor for *Fusobacterium nucleatum* adhesin FadA in lung epithelium, [PMID: 42008577](https://pubmed.ncbi.nlm.nih.gov/42008577/) — but these are unrelated to the developmental THS2 phenotype.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous missense variant** arises in *CDH11*, substituting a conserved extracellular residue — most often in the EC2–EC3 / EC3–EC4 Ca²⁺-binding linkers (hotspot Asp260) or the EC1 trans-dimer pocket (p.Trp55Ser, p.Glu140Lys). *(demonstrated — Li 2021, ClinVar)*
2. The altered residue **impairs Ca²⁺ coordination and/or trans-homodimer formation**, which **results in** defective calcium-dependent homophilic adhesion by the mutant cadherin-11. *(demonstrated in vitro — reduced trans-adhesion activity, Li 2021)*
3. Because cadherin-11 functions as a homodimer at adherens junctions, the mutant subunit **acts in a dominant-negative fashion**, poisoning adhesive complexes that also contain wild-type protein; this **leads to** decreased cell–cell/cell–substrate adhesion and increased cell migratory behavior even in the heterozygous state. *(inferred mechanism supported by functional data — "suggesting dominant negative effect," Li 2021)*
4. In the **cranial neural crest**, where cadherin-11 is predominantly expressed, loss of adhesive function **disrupts contact inhibition of locomotion (CIL)**, **resulting in** non-directional, overly invasive, and poorly coordinated collective migration. *(demonstrated in Xenopus — Becker 2013)*
   - **Branch A (adhesion/migration):** impaired CIL → aberrant CNCC migration.
   - **Branch B (signaling):** altered cadherin-11 function perturbs **Wnt/β-catenin** (nuclear β-catenin → cyclin D1, c-myc; affecting CNCC specification/proliferation — Koehler 2013) and **PI3K-AKT/ErbB2** (ectodomain–ErbB2 signaling that normally promotes migration — Mathavan 2017). *(demonstrated in model organism)*
5. Mis-migration/mis-specification of CNCCs populating the **frontonasal and facial mesenchyme** (where CDH11 is strongly expressed in humans) **leads to** disordered craniofacial morphogenesis. *(demonstrated tissue expression — Li 2021 IHC; inferred link to human phenotype)*
6. The disordered frontonasal development **manifests as** hypertelorism, prominent forehead, short nose with broad/depressed nasal root, and, via parallel mesenchymal roles, genital (hypospadias, shawl scrotum), cardiac, and umbilical anomalies. *(clinical — Li 2021 cohort)*

**Upstream vs downstream.** Upstream = the missense lesion and the adhesion/Ca²⁺-binding defect; midstream = dominant-negative disruption of CNCC adhesion and CIL plus Wnt and PI3K-AKT signaling branches; downstream = craniofacial and genital malformation.

**Molecular pathways:** Wnt/β-catenin (CTNNB1, CCND1, MYC); PI3K-AKT (via ErbB2/ERBB2); cadherin-mediated cell–cell adhesion. **Cellular processes:** collective cell migration, contact inhibition of locomotion, cell specification/proliferation, cell adhesion. **Protein dysfunction:** loss/alteration of homophilic trans-adhesion with dominant-negative quality (not aggregation or simple haploinsufficiency). **Subcellular:** adherens junction (plasma membrane); β-catenin shuttling to nucleus. Mechanobiology: cadherin-11 reduces intracellular tension to permit CNCC spreading/delamination (AFM evidence, [PMID: 28919310](https://pubmed.ncbi.nlm.nih.gov/28919310/)); ADAM13 ectodomain shedding generates a pro-migratory EC1–3 fragment ([PMID: 26206614](https://pubmed.ncbi.nlm.nih.gov/26206614/)).

**Suggested GO / CL / UBERON / CHEBI terms:**
- GO:BP — cell-cell adhesion (GO:0098609); homophilic cell adhesion via plasma-membrane adhesion molecules (GO:0007156); neural crest cell migration (GO:0001755); canonical Wnt signaling pathway (GO:0060070); regulation of cell migration (GO:0030334).
- GO:CC — adherens junction (GO:0005912); catenin complex / cell-cell junction (GO:0005911); plasma membrane (GO:0005886).
- CL — neural crest cell (CL:0000333); fibroblast (CL:0000057); osteoblast (CL:0000062); mesenchymal cell (CL:0008019).
- UBERON — neural crest (UBERON:0002342); frontonasal process / facial mesenchyme; cranium/calvaria (UBERON:0001682).
- CHEBI — calcium(2+) (CHEBI:29108), the ion whose coordination is impaired.

### 7. Anatomical Structures Affected

- **Organ/system level — primary:** craniofacial skeleton and soft tissue (orbits, forehead, nose), male external genitalia. **Secondary/variable:** cardiovascular system (congenital heart defect), anterior abdominal wall (umbilical anomaly), skeleton/limbs (digit anomalies in spectrum cases).
- **Tissue/cell level:** mesenchyme, especially **cranial neural crest-derived craniofacial mesenchyme**; connective tissue/fibroblasts; osteoblasts (OB-cadherin). Cell Ontology: neural crest cell (CL:0000333), fibroblast (CL:0000057), osteoblast (CL:0000062).
- **Subcellular level:** adherens junctions at the plasma membrane (GO:0005912); cytoplasmic β-catenin pool and its nuclear translocation.
- **Localization:** bilateral/symmetric craniofacial involvement (hypertelorism is a midline-spacing anomaly). UBERON suggestions: orbit, frontal bone, nasal bone/nasal root, external male genitalia.

### 8. Temporal Development

- **Onset:** **congenital** — the phenotype originates during embryonic craniofacial morphogenesis (neural crest migration occurs in the first trimester) and is present at birth.
- **Progression:** **stable / non-progressive**; this is a structural malformation syndrome, not a degenerative or episodic disease. No disease "stages."
- **Course / duration:** lifelong structural features; appearance may be modified by growth and by surgical correction.
- **Critical period:** the therapeutic/developmental window for the primary lesion is prenatal (CNCC migration); postnatally, intervention is reconstructive/supportive rather than mechanism-reversing.
- **Remission:** not applicable (no spontaneous resolution of malformation; surgical correction is possible).

### 9. Inheritance and Population

- **Inheritance pattern:** **autosomal dominant** (heterozygous *CDH11* missense). Contrast: EWS is autosomal recessive (biallelic LOF).
- **Penetrance / expressivity:** data limited; the multi-family cohort (9 families) implies familial transmission consistent with high penetrance, with **variable expressivity** (range of features across individuals). Precise penetrance figures are not established (Gap).
- **De novo vs inherited:** both occur; pathogenic alleles are absent from population databases (de novo or private).
- **Anticipation / mosaicism / founder effects / consanguinity:** no evidence for anticipation (not a repeat-expansion disorder). Germline mosaicism not specifically documented for THS2 but is plausible for a dominant malformation gene. Consanguinity is relevant to the **recessive** EWS, not THS2. No founder effect reported.
- **Carrier frequency:** not applicable in the classic sense for a dominant disorder; population frequency of pathogenic alleles is effectively zero.
- **Epidemiology:** THS2 is **ultra-rare**; precise prevalence/incidence are unknown. The defining cohort comprised 19 individuals from 9 families (Li 2021) plus scattered case reports (e.g., Kuroda 2024). **No population-based prevalence or incidence estimate is available** (Gap).
- **Demographics:** reported across multiple families/ethnicities (including a Japanese patient, Kuroda 2024); genital-anomaly features are male-predominant by nature, but the underlying autosomal variant affects both sexes. No specific geographic clustering or variant-specific geographic distribution established.

### 10. Diagnostics

- **Recommended approach:** **molecular genetic testing** is the definitive diagnostic. Clinical recognition of the dysmorphic gestalt (hypertelorism + prominent forehead + short nose with broad/depressed nasal root ± genital anomalies, with normal cognition) prompts testing.
- **Genetic testing modalities:**
  - **Whole-exome sequencing (WES)** — the discovery method (Li 2021; Kuroda 2024) and the most practical clinical test for an atypical/syndromic dysmorphism; identifies *CDH11* missense variants.
  - **Whole-genome sequencing (WGS)** — equally applicable; not specifically required.
  - **Gene panels** — craniofacial/hypertelorism or dysmorphology panels that include *CDH11* and *SPECC1L*.
  - **Single-gene testing** — targeted *CDH11* (NM_001797.4) sequencing if THS2 is specifically suspected.
  - **Chromosomal microarray / karyotype / FISH** — useful to exclude copy-number/chromosomal mimics of hypertelorism (e.g., 22q11.2, 1p36, 8p23.1 syndromes), but will not detect the *CDH11* point mutations.
- **Variant interpretation:** apply ACMG/AMP criteria; use ClinVar and the EC-domain/Ca²⁺-linker clustering (hotspot Asp260) and functional-domain context as supporting evidence. VUS are common (Finding 6) and may warrant functional follow-up.
- **Supportive clinical tests:** craniofacial imaging (to characterize orbital spacing/skeletal features), echocardiography (to screen for associated CHD), and genital examination. No specific biomarker, laboratory abnormality, or histopathology defines THS2.
- **Differential diagnosis:** THS1 (*SPECC1L*); Elsahy-Waters syndrome (*CDH11*, recessive — distinguished by intellectual disability, premature tooth loss, vertebral anomalies); other hypertelorism/frontonasal dysplasia syndromes; chromosomal microdeletion/duplication syndromes with hypertelorism (22q11.2, 1p36, 8p23.1, 2q31). Key discriminators: normal cognition and the specific nasal-root/genital pattern favor THS2; intellectual disability and dental/vertebral signs favor EWS.
- **Omics-based / liquid-biopsy diagnostics:** not applicable.
- **Screening:** no newborn or population screening exists or is indicated for this ultra-rare dominant malformation; **cascade testing** of at-risk relatives for a known familial variant is appropriate.

### 11. Outcome / Prognosis

- **Survival / life expectancy:** No disease-specific mortality is attributed to THS2 itself; life expectancy is expected to be normal in the absence of severe associated anomalies. Prognosis may be influenced by any associated **congenital heart defect**. No formal survival data exist (Gap).
- **Morbidity / function:** morbidity is primarily **structural/cosmetic and reconstructive** (craniofacial appearance; hypospadias requiring surgery). Cognition is typically normal, preserving functional independence. No validated QoL/disability datasets (EQ-5D/SF-36/PROMIS) for THS2 (Gap).
- **Disease course:** stable, non-progressive; outcomes depend on the presence/severity of associated malformations and on surgical correction.
- **Prognostic factors:** presence and severity of cardiac/umbilical/genital anomalies; recovery (cosmetic/functional) is good with surgical management. No molecular prognostic biomarkers established.

### 12. Treatment

**No disease-specific or disease-modifying therapy exists.** Management is **supportive, surgical, and multidisciplinary**, directed at individual manifestations:

| Manifestation | Intervention | Suggested NCIT concept |
|---|---|---|
| Hypertelorism | Craniofacial surgical correction (orbital/interorbital procedures) as indicated | NCIT "Craniofacial Surgery" / "Reconstructive Surgical Procedure" |
| Hypospadias | Surgical urethroplasty / hypospadias repair | NCIT "Surgical Procedure" (urogenital) |
| Congenital heart defect | Cardiology evaluation ± cardiac surgery per lesion | NCIT "Cardiac Surgical Procedure" |
| Umbilical anomaly | Surgical repair as indicated | NCIT "Surgical Procedure" |
| Developmental/psychosocial support | As needed (cognition usually normal) | NCIT "Supportive Care" |

- **Pharmacotherapy / pharmacogenomics:** none specific.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** none; no clinical trials (NCT) identified for THS2.
- **Experimental treatments:** none registered specifically for THS2.
- **Treatment strategy:** individualized, guided by the specific anomalies present; genetic counseling is a core component (see Prevention). Personalized/genotype-guided pharmacotherapy is not applicable.

### 13. Prevention

- **Primary prevention:** not possible for a de novo germline malformation; no risk-factor modification applies.
- **Secondary prevention / screening:** prenatal ultrasound may detect hypertelorism/structural features; **prenatal molecular testing** or **preimplantation genetic testing (PGT)** is available for families with a known pathogenic *CDH11* variant. **Cascade genetic testing** identifies at-risk relatives.
- **Genetic counseling (central):** counsel on **autosomal dominant** inheritance — a 50% transmission risk for an affected heterozygous parent — and on variable expressivity. De novo cases carry a low recurrence risk (with a caveat for possible germline mosaicism). Distinguish clearly from the recessive EWS when counseling, because recurrence risks differ fundamentally.
- **Immunization / public health / environmental / prophylaxis:** not applicable.
- **Tertiary prevention:** monitoring and timely surgical management of associated anomalies (e.g., cardiac) to prevent complications.

### 14. Other Species / Natural Disease

- **Orthologs / taxonomy:** *CDH11* is conserved across vertebrates; affected residues in THS2 are "highly conserved across vertebrate species and across classical cadherins" (Li 2021), underscoring strong evolutionary conservation of the adhesive function. Orthologs include mouse *Cdh11* (NCBI Gene) and the extensively studied *Xenopus* cadherin-11. NCBI Taxon: *Homo sapiens* (9606); *Mus musculus* (10090); *Xenopus laevis* (8355).
- **Natural disease in other species:** no naturally occurring THS2-equivalent Mendelian disease is documented in companion animals or wildlife (no OMIA entry retrieved for a *CDH11* craniofacial syndrome). (Gap/Not applicable.)
- **Comparative biology:** the developmental role of cadherin-11 in cranial neural crest migration is conserved and was principally elucidated in *Xenopus* (Finding 3); mouse *Cdh11* knockouts show skeletal (bone-density) phenotypes ([PMID: 11450702](https://pubmed.ncbi.nlm.nih.gov/11450702/)).
- **Zoonotic / transmission:** not applicable (non-infectious, non-transmissible).

### 15. Model Organisms

No model engineered to carry a THS2 patient-specific *CDH11* missense allele has been reported; however, cadherin-11 biology is well modeled:

| Model | Type | Key phenotype / use | Relevance to THS2 |
|---|---|---|---|
| *Xenopus laevis* (morpholino knockdown, mutant rescue) | Vertebrate, in vivo | Cadherin-11 required for CNCC CIL and directional migration; loss increases invasiveness; β-catenin/Wnt and PI3K-AKT branches mapped | **High** — models the exact developmental process disrupted in THS2 (Becker 2013 [PMID: 24392028](https://pubmed.ncbi.nlm.nih.gov/24392028/); Koehler 2013 [PMID: 23958437](https://pubmed.ncbi.nlm.nih.gov/23958437/); Mathavan 2017 [PMID: 29190819](https://pubmed.ncbi.nlm.nih.gov/29190819/)) |
| *Cdh11*-null mouse | Mammalian, knockout | Reduced bone density in calvaria and long-bone metaphyses; round-shaped calvaria | Partial — models LOF (relevant to EWS); shows cranial skeletal role ([PMID: 11450702](https://pubmed.ncbi.nlm.nih.gov/11450702/)) |
| Cultured cells (adhesion/migration assays) | In vitro | THS2 missense variants reduce trans-adhesion, alter morphology/focal adhesion/migration | **High** — direct dominant-negative evidence (Li 2021 [PMID: 33811546](https://pubmed.ncbi.nlm.nih.gov/33811546/)) |

**Limitations of current models:** the *Xenopus* and mouse systems principally model **knockdown/knockout (loss-of-function)**, which best mirrors the recessive EWS; a **knock-in of a THS2 dominant-negative missense allele** (e.g., murine *Cdh11* p.Asp260 equivalent) is the missing model that would directly recapitulate THS2 pathophysiology. **Resources:** MGI (*Cdh11*), Xenbase, IMPC/IMSR for existing *Cdh11* alleles.

---

## Mechanistic Model / Interpretation

```
 Heterozygous CDH11 missense variant (EC domains; hotspot Asp260; EC1 trans-dimer pocket)
                               │  (demonstrated: Li 2021, ClinVar)
                               ▼
     Impaired Ca²⁺ coordination / impaired trans-homodimer formation
                               │  (demonstrated in vitro: reduced trans-adhesion)
                               ▼
        DOMINANT-NEGATIVE poisoning of adherens-junction complexes
         (↓ cell–cell & cell–substrate adhesion, ↑ cell migration)
                               │  (inferred mechanism, functional support: Li 2021)
                               ▼
     Cranial neural crest cells: loss of contact inhibition of locomotion
         ┌─────────────────────┴─────────────────────┐
         ▼ (Branch A: adhesion/migration)             ▼ (Branch B: signaling)
  Non-directional / over-invasive            Dysregulated Wnt/β-catenin (↑cyclinD1,
  collective CNCC migration                  c-myc → specification/proliferation)
  (Becker 2013)                              + PI3K-AKT/ErbB2 (Koehler 2013; Mathavan 2017)
         └─────────────────────┬─────────────────────┘
                               ▼
     Disordered frontonasal / facial mesenchyme morphogenesis
         (CDH11 strongly expressed in human facial mesenchyme — Li 2021 IHC)
                               ▼
  Hypertelorism · prominent forehead · short nose / broad-depressed nasal root
         · male genital anomalies (hypospadias, shawl scrotum)
         · ± congenital heart defect, umbilical anomaly  (normal cognition)
```

**Genotype–mechanism dichotomy at the *CDH11* locus:**

```
 Heterozygous MISSENSE (EC domains) ──► dominant-negative ──► THS2 (AD, OMIM 619736)
 Biallelic LOF / truncating          ──► loss of function  ──► Elsahy-Waters (AR, OMIM 211380)
                                   └──────── one CDH11-related spectrum ────────┘
```

The coherent story: THS2 is a **neurocristopathy of cell adhesion**. A single mis-sense'd cadherin-11 subunit is sufficient to degrade the homodimeric adhesion machinery of cranial neural crest cells, derailing the finely tuned migration and specification that sculpt the midface — hence hypertelorism as the signature. The convergence of *CDH11* (THS2) and *SPECC1L* (THS1) on adherens-junction/PI3K-AKT control of neural-crest delamination explains why lesions in two different adhesion genes produce the same Teebi hypertelorism gestalt.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [33811546](https://pubmed.ncbi.nlm.nih.gov/33811546/) | *Pathogenic variants in CDH11 impair cell adhesion and cause Teebi hypertelorism syndrome* | Human cohort + in vitro | Findings 1, 7 (causal gene, dominant-negative mechanism, facial-mesenchyme expression) |
| [37646430](https://pubmed.ncbi.nlm.nih.gov/37646430/) | *Japanese patient with THS and a novel CDH11 EC1 variant* | Human case | Findings 2, 6 (EC1 variant; THS–EWS spectrum) |
| [29271567](https://pubmed.ncbi.nlm.nih.gov/29271567/) | *Elsahy-Waters syndrome is caused by biallelic mutations in CDH11* | Human genetics | Finding 2 (biallelic LOF → recessive EWS) |
| [30194892](https://pubmed.ncbi.nlm.nih.gov/30194892/) | *Novel CDH11 mutation causes Branchioskeletogenital (Elsahy-Waters) syndrome* | Human genetics | Finding 2 (homozygous nonsense; craniofacial role) |
| [24392028](https://pubmed.ncbi.nlm.nih.gov/24392028/) | *Cadherin-11 mediates CIL during Xenopus neural crest migration* | Model organism | Finding 3 (CNCC adhesion/CIL/migration) |
| [23958437](https://pubmed.ncbi.nlm.nih.gov/23958437/) | *Loss of Xenopus cadherin-11 → ↑Wnt/β-catenin, c-myc, cyclin D1 in neural crest* | Model organism | Finding 3 (Wnt branch, specification/proliferation) |
| [29190819](https://pubmed.ncbi.nlm.nih.gov/29190819/) | *Cadherin-11 ectodomain binds erbB2, stimulates Akt to promote CNC migration* | Model organism | Finding 3 (PI3K-AKT/ErbB2 branch) |
| [30472488](https://pubmed.ncbi.nlm.nih.gov/30472488/) | *SPECC1L phenotypic spectrum; Teebi/Opitz GBBB/Baraitser-Winter nosology* | Human genetics / review | Finding 4 (THS1 = SPECC1L; convergence on CNCC) |
| [11450702](https://pubmed.ncbi.nlm.nih.gov/11450702/) | *Cadherin-11 disruption reduces bone density in calvaria/long bones* | Mouse knockout | Finding 8 / §15 (skeletal LOF model) |
| [28919310](https://pubmed.ncbi.nlm.nih.gov/28919310/) | *Cadherin-11 promotes neural crest spreading by reducing intracellular tension* | Model organism (AFM) | §6 (mechanobiology of CNCC delamination) |
| [26206614](https://pubmed.ncbi.nlm.nih.gov/26206614/) | *ADAM13 cleavage of cadherin-11 promotes CNC migration* | Model organism | §6 (ectodomain shedding / migration) |
| [35662129](https://pubmed.ncbi.nlm.nih.gov/35662129/) | *Cadherin-11 and tissue fibrosis* (review) | Review | Context (CDH11 mesenchymal/fibrotic biology) |

Supporting constraint and expression evidence: **gnomAD v2.1.1** (Finding 5 — pLI 1.0, LOEUF 0.162, missense Z 2.45); **GTEx v8** (Finding 8 — mesenchymal/fibroblast-dominant expression); **ClinVar** (Finding 6 — missense-only pathogenic spectrum, Asp260 hotspot).

**No paper in the reviewed set challenges the core conclusions.** The chief tension in the literature is interpretive, not contradictory: the strongest *in vivo* developmental data (Xenopus, mouse) model **loss of function**, whereas THS2 is driven by **dominant-negative missense** alleles — so the human phenotype is extrapolated from LOF models plus direct in vitro functional assays of the actual THS2 variants (Li 2021). This is noted as an inference in the causal chain.

---

## Limitations and Knowledge Gaps

1. **Ultra-rare, small evidence base.** The disease rests largely on a single defining cohort (19 subjects/9 families; Li 2021) plus isolated case reports. **Prevalence, incidence, penetrance, and expressivity figures are not quantitatively established.**
2. **No THS2-specific animal model.** Existing *Cdh11* mouse/Xenopus models are loss-of-function; a knock-in of a THS2 dominant-negative missense allele has not been reported, leaving the dominant-negative model directly untested *in vivo*.
3. **Dominant-negative mechanism is inferred, not proven in vivo.** It is supported by in vitro trans-adhesion/migration assays and structural prediction (Li 2021) but not by an allelic-series animal study.
4. **Incomplete ontology/coding cross-references.** THS2-specific Orphanet, ICD-10/11, and MeSH codes were not retrievable in this investigation; HPO frequencies per phenotype are qualitative rather than quantitative.
5. **No prognosis, QoL, or treatment-outcome data.** Management recommendations are extrapolated from general craniofacial/urogenital surgical practice; there are no THS2 clinical trials or outcome cohorts.
6. **VUS burden.** Several *CDH11* missense variants remain VUS (p.Met382Thr, p.Glu534Gln, p.Arg657Cys, p.Asp718Asn), limiting diagnostic certainty for some patients.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a *Cdh11* knock-in mouse** carrying a THS2 hotspot allele (e.g., the murine equivalent of p.Asp260Asn/Glu) and assess craniofacial (hypertelorism/midface) and genital phenotypes — the decisive test of the in vivo dominant-negative model and phenotype recapitulation.
2. **Structural/biophysical validation.** Model (AlphaFold) or solve the EC2–EC3/EC3–EC4 linker with Asp260 substitutions to quantify loss of Ca²⁺ coordination and trans-dimer affinity; use SPR to measure adhesion kinetics of mutant vs WT ectodomains.
3. **Reclassify VUS** via standardized trans-adhesion and migration assays (replicating Li 2021's platform) to resolve p.Met382Thr, p.Glu534Gln, p.Arg657Cys, p.Asp718Asn.
4. **Establish a THS2 patient registry / natural-history study** to quantify prevalence, penetrance, expressivity, cardiac/umbilical anomaly frequencies, and surgical outcomes.
5. **iPSC → cranial neural crest model** from patient fibroblasts to test CIL, Wnt/β-catenin, and PI3K-AKT branch activity in a human cellular system, and to screen whether modulating these pathways rescues the adhesion/migration defect.
6. **Formal ontology curation:** assign and publish HPO frequency annotations, UBERON/CL/GO term mappings, and ICD-11/Orphanet cross-references for the knowledge-base entry.

---

*Report compiled from 8 confirmed findings and 35 reviewed papers across a 5-iteration autonomous investigation. Evidence types are labeled throughout as human clinical/genetic, model organism, in vitro, or computational. All mechanistic claims are tied to the cited PMIDs or to the named aggregate resources (gnomAD, GTEx, ClinVar).*


## Artifacts

- [OpenScientist final report](Teebi_Hypertelorism_Syndrome_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Teebi_Hypertelorism_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000316` (1 mention) - the report calls it "Physical / clinical sign"; HP calls it **Hypertelorism**
- `HP:0003196` (1 mention) - the report calls it "Physical"; HP calls it **Short nose**
- `HP:0000047` (1 mention) - the report calls it "Physical / genital"; HP calls it **Hypospadias**
- `HP:0000049` (1 mention) - the report calls it "Physical / genital"; HP calls it **Shawl scrotum**
- `HP:0001627` (1 mention) - the report calls it "Clinical"; HP calls it **Abnormal heart morphology**
- `HP:0001537` (1 mention) - the report calls it "Physical"; HP calls it **Umbilical hernia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0098609` (1 mention) - the report calls it "GO:BP — cell-cell adhesion"; GO calls it **cell-cell adhesion**
- `GO:0005912` (2 mentions) - the report calls it "GO:CC — adherens junction", "Subcellular level:** adherens junctions at the plasma membrane"; GO calls it **adherens junction**, and lists "cell-cell adherens junction" among its other names
- `CL:0000333` (2 mentions) - the report calls it "CL — neural crest cell"; CL calls it **migratory neural crest cell**
- `UBERON:0002342` (1 mention) - the report calls it "UBERON — neural crest"; UBERON calls it **neural crest**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005912` - called "GO:CC — adherens junction", "Subcellular level:** adherens junctions at the plasma membrane"