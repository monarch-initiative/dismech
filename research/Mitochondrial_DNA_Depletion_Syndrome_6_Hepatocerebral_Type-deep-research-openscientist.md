---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T03:23:10.690978'
end_time: '2026-10-30T03:37:29.689283'
duration_seconds: 859.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Mitochondrial DNA Depletion Syndrome 6 (Hepatocerebral Type)
  mondo_id: MONDO:0009747
  category: Mendelian
  causal_genes: MPV17
  omim_id: not recorded
  synonyms: MTDPS6; MPV17-related mitochondrial DNA maintenance defect; MPV17-related
    hepatocerebral mitochondrial DNA depletion syndrome; MPV17 deficiency; Navajo
    neurohepatopathy; Navajo neuropathy
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
citation_count: 20
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 13
  quotes_valid: 11
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:22137549
  - PMID:32703289
  relevance_assessed: 20
  on_topic: 19
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 31
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0009747
    reported_labels:
    - MONDO
    ontology_label: mitochondrial DNA depletion syndrome 6 (hepatocerebral type)
  - term_id: UBERON:0002107
    reported_labels:
    - Primary organ:** **liver
    ontology_label: liver
  - term_id: NCIT:C1505
    reported_labels:
    - 'Supportive mitochondrial care; used in survivors (PMID: 36753038)'
    ontology_label: Dietary Supplement
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mitochondrial_DNA_Depletion_Syndrome_6_Hepatocerebral_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mitochondrial_DNA_Depletion_Syndrome_6_Hepatocerebral_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial DNA Depletion Syndrome 6 (Hepatocerebral Type)
- **MONDO ID:** MONDO:0009747 (if available)
- **Causal gene(s):** MPV17
- **OMIM:** not recorded
- **Synonyms:** MTDPS6; MPV17-related mitochondrial DNA maintenance defect; MPV17-related hepatocerebral mitochondrial DNA depletion syndrome; MPV17 deficiency; Navajo neurohepatopathy; Navajo neuropathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial DNA Depletion Syndrome 6 (Hepatocerebral Type)** covering all of the
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

# Mitochondrial DNA Depletion Syndrome 6 (Hepatocerebral Type) — Comprehensive Disease Dossier

**Disease:** Mitochondrial DNA Depletion Syndrome 6, Hepatocerebral Type (MTDPS6)
**MONDO:** MONDO:0009747 · **OMIM phenotype:** 256810 · **Causal gene:** **MPV17** (HGNC:7224, chromosome 2p23.3)
**Category:** Mendelian, autosomal recessive

---

## Summary

Mitochondrial DNA Depletion Syndrome 6, hepatocerebral type (MTDPS6; MONDO:0009747; OMIM 256810) is a rare autosomal-recessive mitochondrial disorder caused by **biallelic loss-of-function variants in MPV17**, a gene that encodes a small hydrophobic protein of the **inner mitochondrial membrane**. The disease was originally thought to involve a peroxisomal protein, but was definitively re-localized to mitochondria and linked to hepatocerebral mtDNA depletion in 2006 ([PMID: 16582910](https://pubmed.ncbi.nlm.nih.gov/16582910/), [PMID: 16582907](https://pubmed.ncbi.nlm.nih.gov/16582907/)). **Navajo neurohepatopathy (NNH)**, long described as a distinct entity among Diné (Navajo) children of the southwestern United States, is the same disease, caused by a homozygous **p.R50Q founder mutation** in MPV17 ([PMID: 16909392](https://pubmed.ncbi.nlm.nih.gov/16909392/)).

Mechanistically, MPV17 is required for **mitochondrial deoxynucleotide (dNTP) homeostasis**. Loss of MPV17 lowers the mitochondrial pools of dGTP and dTTP, slowing mtDNA replication and producing **tissue-specific, liver-predominant mtDNA depletion** and consequent **oxidative phosphorylation (OXPHOS) failure** ([PMID: 26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/)). The protein is thought to form a non-selective channel/pore in the inner membrane that imports nucleotides ([PMID: 25205723](https://pubmed.ncbi.nlm.nih.gov/25205723/)), functioning as part of a high-molecular-weight complex ([PMID: 30273399](https://pubmed.ncbi.nlm.nih.gov/30273399/)). Critically, the mtDNA depletion and its downstream consequences can be **prevented or rescued by deoxynucleoside supplementation** in cellular models, nominating a rational therapy.

Clinically, most patients present in infancy with an **encephalohepatopathic** phenotype: hepatic failure/cholestasis, failure to thrive, lactic acidemia, hypoketotic hypoglycemia, and central/peripheral neurological disease, with mtDNA depletion detectable mainly in liver ([PMID: 29282788](https://pubmed.ncbi.nlm.nih.gov/29282788/)). A rarer **late-onset neuromyopathic** form presents as axonal sensorimotor polyneuropathy (overlapping Charcot-Marie-Tooth) with little or no liver involvement ([PMID: 30298599](https://pubmed.ncbi.nlm.nih.gov/30298599/)). Prognosis in the infantile form is poor, but **hypomorphic missense genotypes** (homozygous p.R50Q, p.P98L, p.R41Q) carry a relatively better course, and **liver transplantation** is viable in selected patients with limited neurological burden ([PMID: 29282788](https://pubmed.ncbi.nlm.nih.gov/29282788/), [PMID: 32703289](https://pubmed.ncbi.nlm.nih.gov/32703289/), [PMID: 35466509](https://pubmed.ncbi.nlm.nih.gov/35466509/)). Preclinical **AAV-MPV17 gene therapy** restores liver mtDNA and OXPHOS in mouse models ([PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/)).

This report is derived from **aggregated disease-level resources** (OMIM, Orphanet, MONDO) and the **primary literature** — case series, cohort studies, and mechanistic/model-organism work — rather than individual-patient EHR data.

---

## 1. Disease Information

**Overview.** MTDPS6 is a Mendelian mitochondrial DNA maintenance disorder in the **mtDNA depletion syndrome (MDDS/MDS)** family. In MDDS, nuclear-gene mutations cause a severe reduction in the *quantity* of mtDNA (copy number) in affected tissues — distinct from mtDNA *point mutations* or large rearrangements. Reduced mtDNA leads to deficiency of mtDNA-encoded OXPHOS subunits and impaired energy production in the organs involved. MTDPS6 is the **hepatocerebral** form, predominantly affecting liver and the nervous system.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009747 |
| OMIM (phenotype) | 256810 |
| Gene | MPV17 (HGNC:7224; chr2p23.3) |
| ICD-10 | E88.49 (other disorders of mitochondrial metabolism) / mitochondrial cytopathies |
| MeSH | Mitochondrial Diseases; DNA, Mitochondrial |

**Synonyms / alternative names.** MTDPS6; MPV17-related mitochondrial DNA maintenance defect; MPV17-related hepatocerebral mitochondrial DNA depletion syndrome; MPV17 deficiency; **Navajo neurohepatopathy (NNH); Navajo neuropathy**.

**Source type.** Disease-level aggregated resources plus primary case series and mechanistic studies. One large review consolidates **100 affected individuals** carrying 48 MPV17 pathogenic variants ([PMID: 29282788](https://pubmed.ncbi.nlm.nih.gov/29282788/)).

---

## 2. Etiology

**Primary cause — genetic.** MTDPS6 is caused by **biallelic (homozygous or compound-heterozygous) pathogenic variants in MPV17**. There is no infectious or primary environmental cause. Spinazzola et al. mapped hepatocerebral MDDS to chromosome 2p21-23 and identified disease-segregating MPV17 mutations in three families; Calvo et al. independently nominated MPV17 via integrative genomics ([PMID: 16582910](https://pubmed.ncbi.nlm.nih.gov/16582910/), [PMID: 16582907](https://pubmed.ncbi.nlm.nih.gov/16582907/)).

**Genetic risk factors.** The causal determinant is the MPV17 genotype itself. **Founder effects** elevate risk in specific populations — most notably the **p.R50Q (c.149G>A)** allele among the Navajo (Diné), and a recurrent **c.451dupC** allele reported in Japanese patients. **Consanguinity** increases risk of homozygosity, as in other autosomal-recessive disorders.

**Environmental modifiers (disease triggers, not causes).** Metabolic stressors that increase energetic demand or alter fuel utilization can precipitate decompensation: **fasting, intercurrent infection, and ketogenic/high-fat states**. In the Mpv17−/− mouse, a **ketogenic diet precipitates liver cirrhosis and failure** in otherwise near-asymptomatic animals ([PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/)); one infant's liver function fluctuated, worsening with infection and improving with aggressive treatment ([PMID: 36753038](https://pubmed.ncbi.nlm.nih.gov/36753038/)).

**Protective factors.** No validated protective alleles in humans. Mechanistically, **deoxynucleoside availability** is protective at the cellular level (rescues mtDNA depletion; [PMID: 26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/)), and avoidance of fasting/ketosis is protective at the organismal level ([PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/)).

**Gene-environment interaction.** The clearest GxE signal is **genotype × dietary/metabolic state**: hypomorphic genotypes combined with avoidance of catabolic stress yield milder courses, whereas ketosis/fasting unmasks severe liver disease even on a permissive genetic background (mouse model, [PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/)).

---

## 3. Phenotypes

The dominant presentation is **early-onset encephalohepatopathy**: "The vast majority of affected individuals presented with an early-onset encephalohepatopathic disease characterized by hepatic and neurological manifestations, failure to thrive, lactic acidemia, and mtDNA depletion detected mainly in liver tissue" ([PMID: 29282788](https://pubmed.ncbi.nlm.nih.gov/29282788/)).

| Phenotype | Type | Onset | Frequency / notes | Suggested HPO |
|---|---|---|---|---|
| Hepatic failure / liver dysfunction | Clinical sign | Neonatal–infantile | Core feature; ALF or progressive cholestasis | HP:0001399 Hepatic failure |
| Cholestasis / jaundice | Lab + sign | Neonatal–infantile | 91.3% (21/23) in Japanese cohort | HP:0001396 Cholestasis |
| Failure to thrive | Sign | Infantile | 56.5% (13/23); most common initial manifestation | HP:0001508 Failure to thrive |
| Lactic acidemia / lactic acidosis | Lab abnormality | Neonatal–infantile | Core biochemical feature | HP:0003128 Lactic acidosis |
| Hypoketotic hypoglycemia | Lab abnormality | Infantile | Common; triggered by fasting/infection | HP:0012418 Hypoglycemia |
| Peripheral neuropathy (sensorimotor axonal) | Sign | Childhood–adult (late form) | Hallmark of neuromyopathic form / NNH | HP:0003477 Peripheral axonal neuropathy |
| Leukoencephalopathy / CNS involvement | Imaging/sign | Variable | Cerebral white-matter disease in NNH | HP:0002352 Leukoencephalopathy |
| Corneal anesthesia / scarring | Sign | NNH forms | Characteristic of NNH | HP:0000532 Corneal opacity |
| Acral mutilation / self-injury | Sign | NNH (sensory loss) | NNH feature from sensory neuropathy | HP:0009775 Acral ulceration |
| Hepatocellular carcinoma | Complication | Childhood | Reported complication | HP:0001402 Hepatocellular carcinoma |
| Myopathy | Sign | Late-onset form | Neuromyopathic form | HP:0003198 Myopathy |
| Developmental delay / hypotonia | Sign | Infantile | In hepatocerebral form | HP:0001263 / HP:0001252 |

**Severity, progression, QoL.** The infantile form is **severe and progressive**, frequently fatal before age 1–2 years; recurrent metabolic acidosis with intercurrent infection is characteristic of NNH ([PMID: 16909392](https://pubmed.ncbi.nlm.nih.gov/16909392/)). Quality of life is profoundly impaired by liver failure, feeding difficulties, developmental delay, and (in NNH/late form) disabling neuropathy and acral mutilation. The late-onset neuromyopathic form is milder with slower progression and preserved liver function ([PMID: 30298599](https://pubmed.ncbi.nlm.nih.gov/30298599/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** **MPV17** (HGNC:7224; chr2p23.3), encoding a hydrophobic **inner mitochondrial membrane** protein. "MPV17 is a mitochondrial inner membrane protein, and its absence or malfunction causes oxidative phosphorylation (OXPHOS) failure and mtDNA depletion" ([PMID: 16582910](https://pubmed.ncbi.nlm.nih.gov/16582910/)).

**Pathogenic variants.** The El-Hattab review catalogues **48 MPV17 pathogenic variants across 100 individuals, ~half missense** ([PMID: 29282788](https://pubmed.ncbi.nlm.nih.gov/29282788/)). Representative variants:

| Variant (cDNA / protein) | Type | Significance | Population / note |
|---|---|---|---|
| c.149G>A / p.R50Q | Missense | Pathogenic | Navajo founder; milder prognosis |
| c.293C>T / p.P98L | Missense | Pathogenic | Associated with better prognosis |
| c.122G>A / p.R41Q | Missense | Pathogenic | Axonal neuropathy / late-onset form |
| c.451dupC | Frameshift | Pathogenic | Recurrent in Japanese patients |
| c.55delC / p.Gln19ArgfsTer3 | Frameshift | Pathogenic (novel) | Infantile liver failure |
| c.277C>T / p.Gln93* | Nonsense | Pathogenic | Infantile hepatic failure |
| c.461+1G>C | Splice-site | Pathogenic (novel) | Hepatic failure |
| c.376-9T>G | Near-splice | Pathogenic | In-frame 11-aa deletion; neuropathy |
| c.388G>C / p.Ala130Pro | Missense | Likely pathogenic | Infantile series |

**Variant classification.** Classified per ACMG/AMP; most are pathogenic/likely pathogenic. **Allele frequency** in gnomAD is very low (rare), consistent with a recessive, severe disorder (specific frequencies not independently extracted here).

**Functional consequence.** **Loss of function** (reduced/absent dNTP transport), whether by truncation, splice disruption, or destabilizing/complex-disrupting missense changes. Missense alleles still localize correctly to mitochondria but fail to join a high-MW complex ([PMID: 30273399](https://pubmed.ncbi.nlm.nih.gov/30273399/)).

**Origin.** Germline, biallelic. No somatic/oncogenic role (the HCC complication is secondary to chronic liver injury, not a somatic driver).

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes, disease-specific epigenetic signatures, or large chromosomal abnormalities. Severity is driven primarily by the **specific MPV17 genotype** (hypomorphic missense vs. null).

---

## 5. Environmental Information

- **Environmental/toxic factors:** none causative. Metabolic stressors (fasting, catabolism) act as **decompensation triggers**.
- **Lifestyle/dietary factors:** **ketogenic/high-fat dietary states** are deleterious in the mouse model ([PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/)); fasting and infection worsen infantile disease ([PMID: 36753038](https://pubmed.ncbi.nlm.nih.gov/36753038/)).
- **Infectious agents:** none cause the disease, but **intercurrent infections** precipitate metabolic crises and liver decompensation ([PMID: 16909392](https://pubmed.ncbi.nlm.nih.gov/16909392/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic MPV17 loss-of-function variants** → **absent or non-functional MPV17 protein** in the inner mitochondrial membrane (missense alleles localize but fail to assemble into the high-MW complex). *(demonstrated — [PMID: 16582910](https://pubmed.ncbi.nlm.nih.gov/16582910/), [PMID: 30273399](https://pubmed.ncbi.nlm.nih.gov/30273399/))*
2. **Loss of the MPV17 channel/pore** → **impaired import/homeostasis of deoxynucleotides** across the inner membrane. *(inferred channel function — [PMID: 25205723](https://pubmed.ncbi.nlm.nih.gov/25205723/))*
3. → **Mitochondrial dNTP insufficiency** (decreased dGTP and dTTP in liver mitochondria). *(demonstrated — [PMID: 26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/))*
4. → **Slowed mtDNA replication** by the mtDNA replisome (POLG) due to inadequate substrate supply. *(demonstrated — [PMID: 26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/))*
5. → **Tissue-specific mtDNA depletion**, most severe in **liver** (where salvage-pathway dNTP supply cannot compensate), relatively spared in tissues with adequate dNTP pools (kidney, brain in mouse). *(demonstrated — [PMID: 26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/))*
6. → **Deficiency of mtDNA-encoded OXPHOS subunits** → **respiratory-chain/OXPHOS failure** and reduced ATP. *(demonstrated — [PMID: 16582910](https://pubmed.ncbi.nlm.nih.gov/16582910/))*

   **Branch A (hepatic):** OXPHOS failure in hepatocytes → impaired energy metabolism, cholestasis, steatosis, necrosis, fibrosis/cirrhosis → **liver failure**; chronic injury → **hepatocellular carcinoma** risk. *(demonstrated — [PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/), [PMID: 22137549](https://pubmed.ncbi.nlm.nih.gov/22137549/))*

   **Branch B (systemic metabolic):** OXPHOS failure → **lactic acidemia**, **hypoketotic hypoglycemia**, **failure to thrive**; impaired mitochondrial AdoMet utilization → **hypermethioninemia and elevated S-adenosylmethionine**. *(demonstrated — [PMID: 29282788](https://pubmed.ncbi.nlm.nih.gov/29282788/), [PMID: 22137549](https://pubmed.ncbi.nlm.nih.gov/22137549/))*

   **Branch C (neurological):** energy failure in CNS and peripheral nerve → **leukoencephalopathy, developmental delay, axonal sensorimotor polyneuropathy, corneal anesthesia, acral mutilation**. *(demonstrated clinically; neuronal model — [PMID: 36587049](https://pubmed.ncbi.nlm.nih.gov/36587049/))*

7. **Metabolic trigger (ketosis/fasting/infection)** modulates branch severity → precipitates acute decompensation and liver crisis. *(demonstrated in mouse — [PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/))*

### Detail by category

- **Biochemical core defect:** mitochondrial **dNTP insufficiency** → "our study establishes dNTP insufficiency in the mitochondria as the cause of mitochondrial DNA depletion in MPV17 deficiency, and identifies deoxynucleoside supplementation as a potential therapeutic strategy" ([PMID: 26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/)).
- **Protein dysfunction:** MPV17 forms a **channel/pore** ("the Mpv17 protein forms a channel in the inner mitochondrial membrane, allowing small molecules - in vertebrates probably nucleotides"; [PMID: 25205723](https://pubmed.ncbi.nlm.nih.gov/25205723/)) and participates in a **high-molecular-weight complex**; pathological missense alleles compromise complex formation ([PMID: 30273399](https://pubmed.ncbi.nlm.nih.gov/30273399/)).
- **Metabolic changes:** OXPHOS failure, lactic acidosis, hypoglycemia, elevated methionine/AdoMet.
- **Cellular processes:** impaired mtDNA replication, bioenergetic failure, oxidative stress and elevated ROS (shown in Drosophila dMpv17 knockdown; [PMID: 36587049](https://pubmed.ncbi.nlm.nih.gov/36587049/)), hepatocyte injury/necrosis and fibrosis.
- **Tissue damage mechanisms:** energy-deprivation-driven hepatocyte death, cholestasis, fibrosis/cirrhosis; axonal degeneration in peripheral nerve.
- **Immune involvement:** none primary.

**Suggested GO / CL / anatomy terms.** GO:0006264 mitochondrial DNA replication; GO:0006119 oxidative phosphorylation; GO:1990542 mitochondrial transmembrane transport; GO:0005743 mitochondrial inner membrane (CC); GO:0005739 mitochondrion (CC). Cell types: **hepatocyte (CL:0000182)**, neuron/peripheral sensory & motor neuron (CL:0000540).

---

## 7. Anatomical Structures Affected

- **Primary organ:** **liver (UBERON:0002107)** — hepatocytes bear the greatest mtDNA depletion and OXPHOS failure.
- **Nervous system:** **brain/CNS white matter (UBERON:0002316)** and **peripheral nerves (UBERON:0001021)**; cornea (UBERON:0000964) in NNH.
- **Secondary / systemic:** growth failure (failure to thrive), systemic lactic acidosis; kidney involvement reported in the mouse model (glomerulosclerosis) and occasionally clinically.
- **Body systems:** digestive/hepatobiliary, central and peripheral nervous, metabolic/endocrine (glucose homeostasis).
- **Tissue types:** hepatic epithelial parenchyma; nervous tissue (CNS myelin, peripheral axons); muscle (neuromyopathic form).
- **Subcellular compartment:** **mitochondrion / mitochondrial inner membrane** (GO:0005743) — the primary site of the lesion.
- **Lateralization:** systemic/bilateral; neuropathy is typically length-dependent and symmetric.

---

## 8. Temporal Development

- **Onset:** Most commonly **neonatal to early-infantile** (encephalohepatopathic form). In the single-centre series, MPV17 liver involvement developed at a **median ~2.5 months** ([PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/)). The **late-onset neuromyopathic** form presents in **juvenile-to-adult** years ([PMID: 30298599](https://pubmed.ncbi.nlm.nih.gov/30298599/)).
- **Pattern:** Acute liver failure or subacute/progressive cholestasis in infants; chronic insidious progression in the late form.
- **Course:** Infantile form is **rapidly progressive**; many die within months of presentation (median death ~8 months; 5/10 MPV17 patients died at median 8 months in one series, [PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/)). NNH classically has **infantile, childhood, and classic** sub-forms ([PMID: 16909392](https://pubmed.ncbi.nlm.nih.gov/16909392/)).
- **Critical period / intervention window:** Early infancy — before irreversible neurological injury — is the key window; pre-transplant neurological burden strongly predicts outcome.
- **Remission:** No spontaneous remission; stabilization is treatment-dependent (dietary management, transplant).

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive.** Biallelic MPV17 variants; carriers are asymptomatic.
- **Penetrance / expressivity:** High penetrance in biallelic carriers; **variable expressivity** strongly influenced by genotype (null vs. hypomorphic missense).
- **Founder effects:** **p.R50Q among the Navajo (Diné)** — "Identification of a single missense mutation in patients with NNH confirms that the disease is probably due to a founder effect" ([PMID: 16909392](https://pubmed.ncbi.nlm.nih.gov/16909392/)); recurrent **c.451dupC** in Japanese patients ([PMID: 32703289](https://pubmed.ncbi.nlm.nih.gov/32703289/)).
- **Consanguinity:** Increases homozygosity risk, relevant in several reported families.
- **Epidemiology:** Ultra-rare globally (Orphanet rare-disease classification; exact prevalence/incidence not established). NNH is comparatively more prevalent among Navajo children of the southwestern USA.
- **Sex ratio:** No strong sex predilection (autosomal recessive).
- **Geographic/variant distribution:** p.R50Q — southwestern USA (Navajo); c.451dupC — Japan; others distributed worldwide.

---

## 10. Diagnostics

**Laboratory / biochemistry.** Elevated lactate (lactic acidemia), hypoketotic hypoglycemia, abnormal liver function tests, cholestasis, and characteristically **marked hypermethioninemia with elevated S-adenosylmethionine** — "plasma methionine concentrations as high as 15-21-fold above the upper limit… S-adenosylmethionine (AdoMet) 4.4-8.6-fold above the upper limit" ([PMID: 22137549](https://pubmed.ncbi.nlm.nih.gov/22137549/)). Hypermethioninemia/cholestasis frequently causes **initial misdiagnosis as tyrosinemia** ([PMID: 31664948](https://pubmed.ncbi.nlm.nih.gov/31664948/)).

**Tissue mtDNA quantification.** **Reduced mtDNA copy number in liver** is the diagnostic hallmark; quantitative mtDNA analysis on liver tissue is central ([PMID: 28209105](https://pubmed.ncbi.nlm.nih.gov/28209105/)). Respiratory-chain enzymology may be abnormal but is variably sensitive.

**Histopathology (liver biopsy).** Variable **necrosis, steatosis, cholestasis, and fibrosis/cirrhosis** ([PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/)).

**Genetic testing (definitive).** **Whole-exome/whole-genome or targeted MDDS gene-panel sequencing** (including MPV17, DGUOK, POLG, TK2, FBXL4) confirms diagnosis; NGS "should be considered the first-tier diagnostic test obviating the need for more invasive testing like muscle biopsies" ([PMID: 35750291](https://pubmed.ncbi.nlm.nih.gov/35750291/)). Single-gene MPV17 testing is appropriate where a founder allele is suspected (e.g., Navajo ancestry → p.R50Q). **Rapid genetic testing is advised** in infantile ALF to guide transplant decisions ([PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/)).

**Differential diagnosis.** Tyrosinemia type I, other hepatocerebral MDDS (**DGUOK, POLG**), galactosemia, neonatal hemochromatosis, bile-acid synthesis defects, and other causes of infantile acute liver failure. Distinguishing feature: liver mtDNA depletion + MPV17 variants.

**Screening.** No population newborn screening exists. **Carrier and cascade screening** is valuable in founder populations (Navajo p.R50Q); prenatal/preimplantation testing is available once the familial variant is known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Poor in the infantile hepatocerebral form. Representative mortality: **17/24 MDDS patients died (median age 8 months)**, including **5/10 MPV17 at median 8 months** ([PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/)).
- **Genotype-dependent prognosis:** "A genotype with biallelic missense variants, in particular homozygous p.R50Q, p.P98L, and p.R41Q, can carry a relatively better prognosis" ([PMID: 29282788](https://pubmed.ncbi.nlm.nih.gov/29282788/)).
- **Transplant outcomes:** Of 12 transplanted Japanese patients, "five… survived; while seven who had remarkable neurological symptoms before LT died" ([PMID: 32703289](https://pubmed.ncbi.nlm.nih.gov/32703289/)); survivors were enriched for p.R50Q/p.P98L. Three MPV17 patients in a UK series were alive 3–19 years post-LT ([PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/)). "MPV17 deficiency should not be considered a contraindication to liver transplantation" ([PMID: 35466509](https://pubmed.ncbi.nlm.nih.gov/35466509/)).
- **Complications:** Progressive liver failure, **hepatocellular carcinoma** ("At age 7 years he was found to have hepatocellular carcinoma, underwent a liver transplant and died of progressive liver and renal failure at age almost 9 years"; [PMID: 22137549](https://pubmed.ncbi.nlm.nih.gov/22137549/)), progressive neurological disease (which may continue after LT), renal involvement.
- **Prognostic factors:** Genotype (missense/hypomorphic → better), **pre-transplant neurological burden** (worse → post-LT mortality), degree of liver failure.

---

## 12. Treatment

**No curative pharmacotherapy is approved; management is largely supportive.**

| Intervention | Rationale / evidence | NCIT suggestion |
|---|---|---|
| Avoid fasting/ketosis; frequent feeds, slow-release carbohydrate, **MCT-based diet** | Prevents catabolic decompensation; survivors managed with MCT diet + supplements ([PMID: 36753038](https://pubmed.ncbi.nlm.nih.gov/36753038/)) | NCIT:C15227 Dietary Intervention |
| **Deoxynucleoside / deoxynucleotide supplementation** (investigational) | Rescues mtDNA depletion in patient fibroblasts ([PMID: 26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/)) | NCIT:C1505 Dietary Supplement |
| CoQ10, carnitine, vitamin cofactors | Supportive mitochondrial care; used in survivors ([PMID: 36753038](https://pubmed.ncbi.nlm.nih.gov/36753038/)) | NCIT:C1505 |
| **Liver transplantation** | Viable in selected patients with limited neurology ([PMID: 35466509](https://pubmed.ncbi.nlm.nih.gov/35466509/), [PMID: 32703289](https://pubmed.ncbi.nlm.nih.gov/32703289/), [PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/)) | NCIT:C15393 Liver Transplantation |
| Management of hypoglycemia, acidosis, infection | Acute metabolic crisis control ([PMID: 16909392](https://pubmed.ncbi.nlm.nih.gov/16909392/)) | NCIT:C15329 Supportive Care |
| **AAV-MPV17 gene therapy** (preclinical) | "restore liver mtDNA copy number and oxidative phosphorylation (OXPHOS) proficiency, and prevent liver failure induced by the KD" ([PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/)) | NCIT:C15431 Gene Therapy |
| Drug repurposing (yeast-identified dNTP-pool modulators) | "we identify ten drugs active against MPV17 disorder, modelled in yeast" ([PMID: 34830106](https://pubmed.ncbi.nlm.nih.gov/34830106/)) | — |

**Pharmacogenomics / personalized medicine:** Genotype guides prognosis and transplant candidacy (hypomorphic missense favorable). **Avoid sodium valproate** and other mitochondrial toxins — valproate precipitated liver injury in POLG patients in the same series and is a general caution in MDDS ([PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/)). No approved RNA/cell therapies.

---

## 13. Prevention

- **Primary prevention:** None for occurrence (genetic); **genetic counseling** and **carrier/cascade screening** in founder populations (Navajo p.R50Q) reduce incidence; prenatal and preimplantation genetic testing available for known familial variants.
- **Secondary prevention:** Early genetic diagnosis in infantile ALF to enable timely dietary management and transplant evaluation; rapid testing advised ([PMID: 37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/)).
- **Tertiary prevention:** Avoid fasting/ketosis and hepatotoxins (valproate); aggressively treat intercurrent infections; monitor for HCC in survivors; neurological surveillance.
- **Behavioral/dietary interventions:** Structured feeding regimens, MCT diet, avoidance of prolonged fasting.
- **Immunization / public health / environmental interventions:** Standard childhood immunization to reduce infection-triggered crises; otherwise not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human **MPV17**; mouse **Mpv17** (NCBI Gene 17527); dog **MPV17**; *Drosophila* **CG11077 (dMpv17)**; yeast ortholog **SYM1** (*Saccharomyces cerevisiae*).
- **Natural disease in animals:** A **canine MPV17 truncation** (1-bp insertion in exon 4, enriched in Boxers) exists but is **clinically silent** — "despite the truncation of MPV17, we could not find any common phenotypes in the genetically affected dogs," suggesting species-specific compensation ([PMID: 26353863](https://pubmed.ncbi.nlm.nih.gov/26353863/)).
- **Comparative biology:** Mouse Mpv17−/− shows renal (glomerulosclerosis) and hearing defects not prominent in humans, and is diet-dependent for liver disease ([PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/), [PMID: 25205723](https://pubmed.ncbi.nlm.nih.gov/25205723/)). The dNTP-import function is **evolutionarily conserved** from yeast (SYM1) to vertebrates.
- **Zoonotic potential:** None (genetic disease).

---

## 15. Model Organisms

| Model | Type | Key features | Limitation | Reference |
|---|---|---|---|---|
| **Mpv17−/− mouse** | Mammalian KO | Near-asymptomatic on standard diet; **ketogenic diet → cirrhosis/liver failure**; renal + hearing defects | No spontaneous severe liver phenotype; extra renal/auditory features | [PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/), [PMID: 25205723](https://pubmed.ncbi.nlm.nih.gov/25205723/) |
| **AAV-MPV17 mouse (gene therapy)** | Rescue model | Liver-specific human MPV17 restores mtDNA/OXPHOS, prevents KD-induced failure | Liver-directed only | [PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/) |
| **Patient fibroblasts (quiescent)** | In vitro | Absent protein, decreased dNTPs, mtDNA depletion; **rescued by deoxynucleosides** | Cell-autonomous, non-hepatic | [PMID: 26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/) |
| ***Drosophila* dMpv17 knockdown** | Invertebrate | Recapitulates **neurological defects**: impaired locomotion/learning, ↓mtDNA/ATP, ↑lactate/ROS, abnormal NMJ | Not hepatic | [PMID: 36587049](https://pubmed.ncbi.nlm.nih.gov/36587049/) |
| **Yeast SYM1 (sym1 mutants)** | In vitro / genetic | OXPHOS + mtDNA instability; models missense alleles; **drug-repurposing platform** (10 active molecules) | Unicellular; no tissue phenotype | [PMID: 30273399](https://pubmed.ncbi.nlm.nih.gov/30273399/), [PMID: 34830106](https://pubmed.ncbi.nlm.nih.gov/34830106/) |
| **Canine MPV17 truncation** | Natural large-animal | Clinically silent; model of species-specific compensation | No disease phenotype | [PMID: 26353863](https://pubmed.ncbi.nlm.nih.gov/26353863/) |

**Applications:** The mouse enables gene-therapy and diet-modulation studies; fibroblasts validate deoxynucleoside rescue; *Drosophila* uniquely captures the neurological phenotype absent in mouse/zebrafish/human-cell models; yeast enables mechanistic dissection and drug screening.

---

## Mechanistic Model (synthesis)

```
 Biallelic MPV17 LoF variants (p.R50Q, truncations, splice, complex-disrupting missense)
            │
            ▼
 Absent / non-functional MPV17 inner-membrane channel  ──(missense: localizes but fails to
            │                                              join high-MW complex)
            ▼
 Impaired mitochondrial deoxynucleotide import  →  ↓ mitochondrial dGTP, dTTP
            │
            ▼
 Slowed mtDNA replication (substrate-limited POLG)
            │
            ▼
 Tissue-specific mtDNA DEPLETION  (LIVER >> kidney/brain; salvage pathway cannot rescue liver)
            │
            ▼
 Deficient mtDNA-encoded OXPHOS subunits → RESPIRATORY-CHAIN / OXPHOS FAILURE, ↓ATP
            │
   ┌────────┼─────────────────────────────┬──────────────────────────────┐
   ▼        ▼                             ▼                              ▼
 LIVER    SYSTEMIC METABOLIC          NEUROLOGICAL                 BIOCHEMICAL MARKER
 injury   lactic acidemia,           leukoencephalopathy,         hypermethioninemia +
 cholestasis hypoketotic             axonal polyneuropathy,       ↑S-adenosylmethionine
 fibrosis/   hypoglycemia,           corneal anesthesia,
 cirrhosis   failure to thrive       acral mutilation
   │
   ▼
 LIVER FAILURE → (chronic) HEPATOCELLULAR CARCINOMA

 MODIFIER: fasting / ketosis / infection  ⇒ precipitates acute hepatic decompensation
 RESCUE:   deoxynucleoside supplementation / AAV-MPV17 ⇒ restores mtDNA + OXPHOS
```

---

## Evidence Base

| PMID | Role in this dossier |
|---|---|
| [16582910](https://pubmed.ncbi.nlm.nih.gov/16582910/) | Identifies MPV17 as causal gene; inner-membrane localization; OXPHOS/mtDNA depletion |
| [16582907](https://pubmed.ncbi.nlm.nih.gov/16582907/) | Independent integrative-genomics discovery of MPV17 |
| [26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/) | Core mechanism: dNTP insufficiency; deoxynucleoside rescue |
| [25205723](https://pubmed.ncbi.nlm.nih.gov/25205723/) | MPV17 channel function; cross-species model comparison |
| [30273399](https://pubmed.ncbi.nlm.nih.gov/30273399/) | Missense alleles disrupt high-MW complex (yeast SYM1) |
| [29282788](https://pubmed.ncbi.nlm.nih.gov/29282788/) | 100-patient review; phenotype spectrum; genotype-prognosis |
| [16909392](https://pubmed.ncbi.nlm.nih.gov/16909392/) | Navajo neurohepatopathy = MPV17 R50Q founder disease |
| [32703289](https://pubmed.ncbi.nlm.nih.gov/32703289/) | Japanese cohort; transplant outcomes; phenotype frequencies |
| [35466509](https://pubmed.ncbi.nlm.nih.gov/35466509/) | LT not a contraindication in MPV17/NNH |
| [37204315](https://pubmed.ncbi.nlm.nih.gov/37204315/) | UK MDDS series; mortality; MPV17 LT survivors |
| [24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/) | Mouse KD-dependence; AAV gene-therapy proof of concept |
| [34830106](https://pubmed.ncbi.nlm.nih.gov/34830106/) | Yeast drug-repurposing; dNTP-pool modulators |
| [36587049](https://pubmed.ncbi.nlm.nih.gov/36587049/) | Drosophila model of neurological phenotype |
| [30298599](https://pubmed.ncbi.nlm.nih.gov/30298599/) | Late-onset axonal polyneuropathy form (p.R41Q) |
| [22137549](https://pubmed.ncbi.nlm.nih.gov/22137549/) | HCC complication; hypermethioninemia/↑AdoMet |
| [31664948](https://pubmed.ncbi.nlm.nih.gov/31664948/) | Tyrosinemia misdiagnosis; novel splice/nonsense variants |
| [36753038](https://pubmed.ncbi.nlm.nih.gov/36753038/) | Infantile series; MCT-diet management; infection triggers |
| [35750291](https://pubmed.ncbi.nlm.nih.gov/35750291/) | WES as first-tier diagnostic; novel variants |
| [28209105](https://pubmed.ncbi.nlm.nih.gov/28209105/) | NNH clinicopathologic diagnosis; liver mtDNA analysis |
| [26353863](https://pubmed.ncbi.nlm.nih.gov/26353863/) | Clinically silent canine MPV17 truncation |

---

## Limitations and Knowledge Gaps

1. **Precise epidemiology unknown.** No reliable prevalence/incidence figures; counts derive from case series and a 100-patient review, subject to ascertainment bias.
2. **Exact molecular function incompletely resolved.** MPV17 is proposed as a dNTP-importing channel within a high-MW complex, but the complex composition, selectivity, and regulation remain uncharacterized.
3. **Tissue-specificity of liver predominance** is attributed to salvage-pathway differences but is not fully mechanistically explained.
4. **Human therapeutic evidence is thin.** Deoxynucleoside supplementation and AAV gene therapy are supported only by in vitro/mouse data; no human trials with NCT identifiers were identified.
5. **Genotype-phenotype correlations are coarse** — missense/hypomorphic alleles trend milder, but individual variability (expressivity) is incompletely predicted.
6. **Allele frequencies** in gnomAD were not independently extracted here for each variant.
7. **Neurological progression after liver transplant** is recognized but poorly quantified longitudinally.

## Proposed Follow-up Experiments / Actions

1. **Human deoxynucleoside/deoxynucleotide trial** in MPV17 patients (building on fibroblast rescue, [PMID: 26760297](https://pubmed.ncbi.nlm.nih.gov/26760297/)) with mtDNA copy number and liver-function endpoints.
2. **AAV-MPV17 translational development** toward IND, including biodistribution, durability, and whether liver-directed therapy mitigates neurological disease ([PMID: 24247928](https://pubmed.ncbi.nlm.nih.gov/24247928/)).
3. **Structural characterization** of the MPV17 high-MW complex (cryo-EM/AlphaFold-Multimer) to define the channel and the effect of missense alleles ([PMID: 30273399](https://pubmed.ncbi.nlm.nih.gov/30273399/)).
4. **Prospective natural-history registry** capturing genotype, onset, transplant timing, and neurological trajectory to refine prognostic modeling and the critical intervention window.
5. **Validate yeast-nominated drugs** ([PMID: 34830106](https://pubmed.ncbi.nlm.nih.gov/34830106/)) in patient fibroblasts and the Drosophila neurological model ([PMID: 36587049](https://pubmed.ncbi.nlm.nih.gov/36587049/)).
6. **Carrier-screening program evaluation** in the Navajo population for the p.R50Q founder allele, with genetic-counseling outcomes.
7. **Biomarker study** of plasma methionine/AdoMet ([PMID: 22137549](https://pubmed.ncbi.nlm.nih.gov/22137549/)) as a non-invasive diagnostic/monitoring tool and to reduce tyrosinemia misdiagnosis ([PMID: 31664948](https://pubmed.ncbi.nlm.nih.gov/31664948/)).

---

*Evidence source types: human clinical (case series, cohorts, reviews), model organism (mouse, Drosophila, yeast, dog), in vitro (patient fibroblasts), and computational/comparative genomics. All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Mitochondrial_DNA_Depletion_Syndrome_6_Hepatocerebral_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mitochondrial_DNA_Depletion_Syndrome_6_Hepatocerebral_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 20 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:22137549` *(abstract only)*: "plasma methionine concentrations as high as 15-21-fold above the upper limit… S-adenosylmethionine (AdoMet) 4.4-8.6-fold above the upper limit"
  - closest text in source: "Each was initially investigated metabolically because of plasma methionine concentrations as high as 15-21-fold above the upper limit of the reference range, then found also to have plasma levels of S-adenosylmethionine (AdoMet) 4.4-8.6-fold above the upper limit of the reference range"
- `PMID:32703289`: "five… survived; while seven who had remarkable neurological symptoms before LT died"
  - closest text in source: "Among the 12 transplanted patients, five, including one with mild intellectual disability, survived; while seven who had remarkable neurological symptoms before LT died"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009747` (3 mentions) - the report calls it "MONDO"; MONDO calls it **mitochondrial DNA depletion syndrome 6 (hepatocerebral type)**
- `UBERON:0002107` (1 mention) - the report calls it "Primary organ:** **liver"; UBERON calls it **liver**
- `NCIT:C1505` (2 mentions) - the report calls it "Supportive mitochondrial care; used in survivors (PMID: 36753038)"; NCIT calls it **Dietary Supplement**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005743` (2 mentions) - the report calls it "mitochondrion / mitochondrial inner membrane", "Subcellular compartment:** **mitochondrion / mitochondrial inner membrane"; GO calls it **mitochondrial inner membrane**
- `UBERON:0002316` (1 mention) - the report calls it "Nervous system:** **brain/CNS white matter"; UBERON calls it **white matter**, and lists "neuronal white matter" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005743` - called "mitochondrion / mitochondrial inner membrane", "Subcellular compartment:** **mitochondrion / mitochondrial inner membrane"