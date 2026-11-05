---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T18:12:32.378009'
end_time: '2026-11-05T18:27:21.112858'
duration_seconds: 888.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Mitochondrial DNA Depletion Syndrome 12B
  mondo_id: MONDO:0014175
  category: Mendelian
  causal_genes: SLC25A4
  omim_id: OMIM:615418
  synonyms: mitochondrial DNA depletion syndrome 12B (cardiomyopathic type) AR; mitochondrial
    DNA depletion syndrome 12B (cardiomyopathic type), AR; MTDPS12B; mitochondrial
    DNA depletion syndrome 12
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
citation_count: 9
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 11
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:22187496
  - PMID:18439414
  - PMID:16303948
  relevance_assessed: 9
  on_topic: 6
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 6
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014175
    reported_labels:
    - MONDO
    ontology_label: mitochondrial DNA depletion syndrome 12B (cardiomyopathic type),
      autosomal recessive
  - term_id: HP:0001639
    reported_labels:
    - Clinical sign / cardiac
    ontology_label: Hypertrophic cardiomyopathy
  - term_id: HP:0003546
    reported_labels:
    - Symptom
    ontology_label: Exercise intolerance
  - term_id: HP:0003200
    reported_labels:
    - Laboratory/histopathology
    ontology_label: Ragged-red muscle fibers
  - term_id: HP:0000519
    reported_labels:
    - Clinical sign / ocular
    ontology_label: Developmental cataract
  labels_variant: 6
  obsolete_terms:
  - term_id: GO:0000002
    ontology_label: obsolete mitochondrial genome maintenance
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mitochondrial_DNA_Depletion_Syndrome_12B-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mitochondrial_DNA_Depletion_Syndrome_12B-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial DNA Depletion Syndrome 12B
- **MONDO ID:** MONDO:0014175 (if available)
- **Causal gene(s):** SLC25A4
- **OMIM:** OMIM:615418
- **Synonyms:** mitochondrial DNA depletion syndrome 12B (cardiomyopathic type) AR; mitochondrial DNA depletion syndrome 12B (cardiomyopathic type), AR; MTDPS12B; mitochondrial DNA depletion syndrome 12
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial DNA Depletion Syndrome 12B** covering all of the
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

# Mitochondrial DNA Depletion Syndrome 12B (MTDPS12B): A Comprehensive Disease Characterization

**Disease:** Mitochondrial DNA Depletion Syndrome 12B (cardiomyopathic type), autosomal recessive
**Causal gene:** **SLC25A4** (encoding ANT1/AAC1, the heart- and skeletal-muscle-specific mitochondrial ADP/ATP translocase)
**MONDO:** MONDO:0014175 · **OMIM:** 615418 · **Synonyms:** MTDPS12B; mitochondrial DNA depletion syndrome 12 (cardiomyopathic type), AR
**Inheritance:** Autosomal recessive · **Category:** Mendelian

---

## Summary

Mitochondrial DNA Depletion Syndrome 12B (MTDPS12B; MONDO:0014175; OMIM 615418) is an **ultra-rare autosomal-recessive mitochondrial disorder caused by biallelic loss-of-function variants in SLC25A4**, the gene encoding **adenine nucleotide translocator 1 (ANT1, also called AAC1)** — the heart- and skeletal-muscle-predominant carrier that exchanges mitochondrial matrix ATP for cytosolic ADP across the inner mitochondrial membrane. It is critical to note that *SLC25A4* is the correct causal gene (not a similarly numbered mitochondrial depletion syndrome from a different locus): the disease name is a serial number, and the identifiers above (SLC25A4; OMIM 615418) govern. Recessive null alleles abolish ADP/ATP exchange, producing a bioenergetic ("energy crisis") defect accompanied by secondary mitochondrial DNA instability (multiple mtDNA deletions and reduced mtDNA copy number) that is largely restricted to oxidative, high-energy-demand tissues — the heart and skeletal muscle.

Clinically, MTDPS12B presents in infancy or childhood with **hypertrophic cardiomyopathy**, **mitochondrial myopathy** with exercise intolerance, and **lactic acidosis**; one complete-null patient additionally had **congenital cataracts**. Muscle biopsy shows the hallmarks of mitochondrial myopathy — ragged-red fibers, proliferation of structurally abnormal mitochondria, increased mitochondrial mass, and multiple mtDNA deletions. Notably, patients lack the chronic progressive external ophthalmoplegia (CPEO) that characterizes the *dominant* SLC25A4 disorders, defining a clear recessive-versus-dominant genotype–phenotype dichotomy.

The recessive cardiomyopathic form (MTDPS12B) is mechanistically and clinically distinct from the dominant SLC25A4 diseases: heterozygous dominant-negative missense alleles cause adult-onset autosomal-dominant PEO with multiple mtDNA deletions, while recurrent *de novo* dominant alleles (p.Arg80His, p.Arg235Gly) cause a severe neonatal depletion disorder (MTDPS12A, OMIM 617184). The *Ant1*-knockout mouse faithfully recapitulates the human cardiomyopathic/myopathic phenotype — including lactic acidosis, mitochondrial hyperproliferation, OXPHOS induction, elevated ROS, and excessive mtDNA damage — providing a validated model system. There is currently **no disease-specific or curative therapy**; management is supportive.

---

## Section 1 — Disease Information

**Overview.** MTDPS12B is a Mendelian mitochondrial disease in which inherited biallelic loss of the heart/skeletal-muscle ADP/ATP translocase cripples the export of mitochondrially produced ATP to the cytosol. Energy-demanding striated muscle (cardiac and skeletal) is preferentially affected, yielding an infantile/childhood-onset syndrome of cardiomyopathy and myopathy with lactic acidosis. The disorder sits within the broader family of mitochondrial DNA maintenance disorders because affected tissue accumulates **multiple mtDNA deletions** and shows **reduced mtDNA copy number** as a secondary consequence of the primary transport defect.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014175 |
| OMIM | 615418 |
| Gene (HGNC) | SLC25A4 (HGNC:10990) |
| Protein (UniProt) | P12235 (ADT1_HUMAN / ANT1) |
| Synonyms | MTDPS12B; mitochondrial DNA depletion syndrome 12 (cardiomyopathic type), AR; ANT1 deficiency, recessive |

**Data source type.** The evidence base is derived from **individual patient case reports** (aggregated into disease-level resources such as OMIM) combined with **model-organism and in-vitro functional studies**, rather than from large EHR cohorts. Because the disorder is ultra-rare, the human literature comprises a small number of index families.

---

## Section 2 — Etiology

**Primary cause (genetic).** MTDPS12B is caused exclusively by **biallelic (autosomal recessive) loss-of-function of SLC25A4/ANT1** (Finding F001). Two mechanisms of complete functional loss are documented: (1) a homozygous missense allele that abolishes transport activity (c.368C>A, p.Ala123Asp), and (2) a homozygous splice-donor abolition (c.111+1G>A) that eliminates ANT1 expression entirely. In the first recessive report, "*No ATP uptake was measured in proteoliposomes reconstituted with protein extracts from the patient's muscle*" [PMID: 16155110], and the equivalent mutation in the yeast ortholog AAC2 abolished transport — establishing true loss of function. In the complete-null case, "*Complete loss of expression of the ANT1 gene causes a clinical syndrome mainly characterised by cardiomyopathy and myopathy*" [PMID: 22187496].

**Genetic risk factors.** The only established risk factor is **inheritance of two pathogenic SLC25A4 alleles** (homozygous or compound heterozygous). Consanguinity increases risk of homozygosity for recessive alleles, consistent with the reported homozygous cases. No susceptibility loci or common modifier variants have been established for this ultra-rare disorder.

**Environmental risk factors.** None established. The disease is monogenic; onset and expression are driven by the genotype rather than environmental exposure. Age and the high intrinsic metabolic demand of striated muscle act as biological context rather than modifiable exposures.

**Protective factors.** No genetic or environmental protective factors are established in humans. At the mechanistic level, expression of the paralogous translocases **ANT2 (SLC25A5)** and **ANT3 (SLC25A6)** could in principle buffer ANT1 loss; in the mouse, higher *Ant2* expression in extraocular muscle may spare ocular motility (see Sections 6 and 15). However, in the human complete-null patient, "*No compensating increase in the transcript level of the ANT3 gene … was observed*" [PMID: 22187496], so paralog compensation is tissue-dependent and incomplete.

**Gene–environment interactions.** None documented. This is a highly penetrant monogenic disorder with no reported GxE modulation.

---

## Section 3 — Phenotypes

The phenotypic spectrum (Finding F004) is dominated by striated-muscle and metabolic manifestations. Across the two index recessive cases:

| Phenotype | Type | Suggested HPO | Onset | Severity / course | Frequency |
|---|---|---|---|---|---|
| Hypertrophic cardiomyopathy | Clinical sign / cardiac | HP:0001639 | Infantile–childhood | Severe, progressive | Core feature (both cases) |
| Mitochondrial myopathy / muscle weakness | Clinical sign | HP:0003198 / HP:0003737 | Infantile–childhood | Mild→moderate, progressive | Core feature (both cases) |
| Exercise intolerance | Symptom | HP:0003546 | Childhood | Variable | Reported |
| Lactic acidosis | Laboratory abnormality | HP:0003128 (elevated lactate) | Infantile–childhood | Moderate–severe | Core feature (both cases) |
| Ragged-red fibers | Laboratory/histopathology | HP:0003200 | — | — | Present on biopsy |
| Multiple mtDNA deletions | Laboratory/molecular | HP:0003689 (mtDNA deletion) | — | — | Present in muscle |
| Congenital cataracts | Clinical sign / ocular | HP:0000519 | Congenital | — | Complete-null case |
| **Absence** of ophthalmoplegia | Distinguishing feature | (cf. HP:0000602) | — | — | Notably absent (vs dominant PEO) |

Supporting quotes: a "*sporadic patient who presented with hypertrophic cardiomyopathy, mild myopathy with exercise intolerance and lactic acidosis but no ophthalmoplegia*" [PMID: 16155110]; and "*an autosomal recessive mitochondrial disorder characterised by congenital cataracts, hypertrophic cardiomyopathy, myopathy and lactic acidosis*" [PMID: 22187496].

**Quality-of-life impact.** Although no formal EQ-5D/SF-36 data exist for this ultra-rare disease, the combination of hypertrophic cardiomyopathy (risk of heart failure/arrhythmia), progressive myopathy with exercise intolerance, and metabolic (lactic) acidosis implies substantial functional limitation from early life, with cardiac disease being the principal determinant of morbidity and prognosis.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** **SLC25A4** (solute carrier family 25 member 4), chromosome 4q35.1, encoding ANT1/AAC1 (UniProt P12235), a ~298-residue inner-mitochondrial-membrane carrier of the SLC25 mitochondrial carrier family with the characteristic three tandem ~100-residue repeats and six transmembrane helices.

**Pathogenic variants (recessive, MTDPS12B).**

| Variant (cDNA) | Protein | Type | Functional consequence | Classification | Source |
|---|---|---|---|---|---|
| c.368C>A | p.Ala123Asp | Missense | Abolished ADP/ATP transport (no ATP uptake in proteoliposomes); yeast AAC2 equivalent abolished transport; absent in 500 controls | Pathogenic | [PMID: 16155110] |
| c.111+1G>A | — (splice donor loss) | Splice-site | Complete loss of ANT1 expression; transcript undetectable in muscle and fibroblasts | Pathogenic | [PMID: 22187496] |

Both recessive alleles produce **complete loss of function**. Origin is **germline**; no somatic contribution is relevant. Allele frequencies in gnomAD are vanishingly rare/absent, consistent with the ultra-rare recessive disease.

**Contrast — dominant SLC25A4 alleles (NOT MTDPS12B).** Heterozygous missense alleles cause adult-onset autosomal-dominant PEO (adPEO / PEOA2) with multiple mtDNA deletions, acting through a dominant-negative mechanism; recurrent *de novo* dominant alleles **c.239G>A (p.Arg80His)** and **c.703C>G (p.Arg235Gly)** cause severe neonatal MTDPS12A (OMIM 617184) with marked loss of mtDNA copy number (Finding F002) [PMID: 27693233]. Recent structural work maps the "lethal" mutations near the primary substrate (S1) site and "milder" PEO mutations near a secondary (S2) site, correlating mutation location with severity [PMID: 42308345].

**Functional consequence.** **Loss of function** (recessive MTDPS12B). The dominant disorders by contrast behave as dominant-negative/gain-of-toxicity.

**Modifier genes.** The paralogs **ANT2 (SLC25A5)** and **ANT3 (SLC25A6)** are candidate functional modifiers via dosage compensation, though compensation is tissue-restricted and was absent for ANT3 in affected human muscle [PMID: 22187496].

**Epigenetic / chromosomal abnormalities.** None reported; MTDPS12B is a point-mutation/splice disorder, not a structural/cytogenetic one.

---

## Section 5 — Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in MTDPS12B. It is a purely genetic, monogenic recessive disorder. (Environmental mitochondrial toxins are relevant to acquired mitochondrial dysfunction generally but are not causes of this inherited syndrome.)

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function mutation in SLC25A4** (missense p.Ala123Asp or splice-null c.111+1G>A) → **leads to** absent or non-functional ANT1/AAC1 protein in heart and skeletal muscle.
2. Loss of functional ANT1 → **results in** abolished ADP/ATP exchange across the inner mitochondrial membrane (demonstrated: no ATP uptake in patient-muscle proteoliposomes) → matrix ATP cannot be exported and cytosolic ADP cannot be imported.
3. Failure of adenine-nucleotide exchange → **leads to** a cellular **bioenergetic/energy crisis** in high-demand oxidative tissue (cytosolic ATP shortfall; impaired re-supply of ADP substrate to ATP synthase).
4. (Branch A — bioenergetic) Energy crisis → **results in** lactic acidosis and impaired contractile function of cardiac and skeletal muscle.
5. (Branch B — mtDNA instability, partly inferred) Impaired adenine-nucleotide/matrix nucleotide homeostasis → **probably affects mitochondrial DNA maintenance** → **leads to** multiple mtDNA deletions and reduced mtDNA copy number → loss of respiratory-chain complexes containing mtDNA-encoded subunits → further aggravates the energy crisis (feed-forward loop).
6. Chronic bioenergetic stress → **results in** compensatory mitochondrial hyperproliferation (ragged-red fibers, increased mitochondrial mass), OXPHOS enzyme induction, and increased reactive oxygen species (ROS) → **leads to** additional oxidative mtDNA damage (demonstrated in the mouse).
7. Cumulative cardiac and skeletal-muscle energetic failure → **results in** the clinical manifestation: **hypertrophic cardiomyopathy, mitochondrial myopathy with exercise intolerance, lactic acidosis** (± congenital cataracts).

> *Branch B (step 5) is the mechanism stated as "probably" in the literature* — the mtDNA-maintenance link is inferred/associative rather than fully demonstrated: "*This highly reduced capacity for transport probably affects mitochondrial DNA maintenance and in turn respiration, causing a severe energy crisis*" [PMID: 27693233].

### Detail by category

- **Molecular pathways / biochemistry.** The core defect is in the adenine-nucleotide translocation step of **oxidative phosphorylation (OXPHOS)**. ANT1 "*exports mitochondrial ATP to the cytosol*" in exchange for ADP [PMID: 18439414]; loss blocks the ATP/ADP shuttle that couples matrix ATP synthesis to cytosolic energy demand. Downstream compensation engages the mitochondrial biogenesis program — in the *Ant1−/−* mouse there is "*coordinate upregulation of Pgc-1α, Nrf-1, Tfam, myogenin and antioxidant genes*" [PMID: 18439414].
- **Cellular processes.** Mitochondrial hyperproliferation/biogenesis; oxidative stress; secondary apoptosis signaling (ANT1 is a component of the mitochondrial permeability transition pore). GO terms: GO:0140021 (mitochondrial ADP transmembrane transport), GO:0006839 (mitochondrial transport), GO:0006119 (oxidative phosphorylation), GO:0007005 (mitochondrion organization), GO:0000002 (mitochondrial genome maintenance), GO:0006979 (response to oxidative stress).
- **Protein dysfunction.** Loss of transport function — either by abolished catalytic activity (p.Ala123Asp) or absent protein (splice-null). Structural mapping indicates substrate-binding/architecture disruption underlies severity gradients across the allelic series [PMID: 42308345].
- **Metabolic changes.** Impaired ATP export → lactic acidosis (anaerobic compensation), respiratory-chain deficiency for mtDNA-encoded subunits.
- **Tissue damage mechanisms.** Oxidative stress (increased ROS), excessive mtDNA damage, energy-deprivation-driven cardiomyocyte hypertrophy and myofiber degeneration.
- **Immune involvement.** None; this is a non-inflammatory metabolic myopathy/cardiomyopathy.

**Upstream vs downstream.** Upstream = the SLC25A4 mutation and loss of ADP/ATP exchange. Downstream = energy crisis, mtDNA instability, ROS, mitochondrial proliferation, and ultimately cardiomyopathy/myopathy.

**Cell types involved (CL):** cardiomyocyte (CL:0000746), skeletal muscle fiber (CL:0008002 / CL:0000188), lens fiber cell (CL:0011004, for cataract).

---

## Section 7 — Anatomical Structures Affected

- **Primary organs:** heart (UBERON:0000948) and skeletal muscle (UBERON:0001134). Cardiovascular and musculoskeletal systems are primarily affected.
- **Secondary involvement:** ocular lens (UBERON:0000965) — congenital cataracts in the complete-null case; systemic metabolic effect via lactic acidosis.
- **Tissue/cell level:** striated (cardiac and skeletal) muscle tissue; cardiomyocytes (CL:0000746) and skeletal myofibers (CL:0000188); lens fiber cells.
- **Subcellular level:** **mitochondrion** (GO:0005739), specifically the **inner mitochondrial membrane** (GO:0005743) where ANT1 resides; the mitochondrial matrix (nucleotide pools) and the mitochondrial genome (mtDNA maintenance) are secondarily affected.
- **Localization / lateralization:** bilateral/systemic involvement of striated muscle; cardiomyopathy affects the whole myocardium; cataracts are bilateral. The disease is not lateralized.

The tissue restriction is explained by **isoform-specific expression**: "*The ANT1 isoform predominates in heart and muscle while ANT2 is systemic*" [PMID: 35714845] (Finding F006).

---

## Section 8 — Temporal Development

- **Onset:** congenital to early childhood (infantile/childhood-onset). Congenital cataracts in one case indicate prenatal/neonatal onset of at least one feature; recessive cardiomyopathic SLC25A4 disease is described as **childhood-onset** [PMID: 27693233].
- **Onset pattern:** chronic/insidious with progressive deterioration; metabolic crises (lactic acidosis) can be episodic.
- **Progression:** progressive myopathy and cardiomyopathy; muscle shows accumulating mtDNA deletions and mitochondrial proliferation over time. Progression rate is variable but the cardiomyopathy is the life-limiting component.
- **Disease course:** chronic, lifelong, progressive.
- **Critical periods:** infancy/early childhood, when cardiac decompensation is most threatening.
- **Remission:** no spontaneous remission; no disease-modifying treatment exists to induce remission.

---

## Section 9 — Inheritance and Population

- **Inheritance:** **autosomal recessive** (Finding F001). The heterozygous carrier mother in the complete-null family had "*normal clinical, biochemical and pathological features*," confirming no carrier phenotype [PMID: 22187496].
- **Penetrance / expressivity:** biallelic LOF appears fully penetrant for the striated-muscle/metabolic phenotype; expressivity varies (e.g., cataracts present in one case, not emphasized in the other).
- **Epidemiology:** **ultra-rare.** Only a small number of recessive index cases are reported worldwide; precise prevalence/incidence figures are not established (too few cases). No reliable per-100,000 estimate exists.
- **Carrier frequency / founder effects:** not established; pathogenic recessive alleles are essentially absent from population databases (gnomAD).
- **Consanguinity:** relevant — homozygous recessive cases are consistent with consanguineous or founder backgrounds, though not detailed for every case.
- **Sex ratio:** no sex predilection expected (autosomal); too few cases to quantify.
- **Genetic anticipation / germline mosaicism:** not applicable/not reported (no repeat expansion).

---

## Section 10 — Diagnostics

**Clinical/laboratory tests.**
- **Blood lactate:** elevated (lactic acidosis) — HP:0003128; a key biochemical clue.
- **Cardiac evaluation:** echocardiography/MRI demonstrating hypertrophic cardiomyopathy; ECG.
- **Muscle biopsy histopathology:** ragged-red fibers; COX/SDH histochemistry; proliferation of structurally abnormal mitochondria; increased mitochondrial mass [PMID: 16155110; PMID: 22187496].
- **Respiratory-chain enzymology:** deficiency of complexes containing mtDNA-encoded subunits [PMID: 27693233].
- **Functional transport assay (research):** proteoliposome ATP-uptake assay from patient muscle demonstrated absent transport [PMID: 16155110].

**Molecular/mtDNA testing.**
- **mtDNA analysis** (long-range PCR / Southern blot / sequencing): reveals **multiple mtDNA deletions** and **reduced mtDNA copy number** — the molecular signature of an mtDNA-maintenance disorder.
- **Nuclear gene testing:** single-gene **SLC25A4** sequencing, or (preferably) a **mitochondrial/nuclear mtDNA-maintenance gene panel**, **whole-exome (WES)**, or **whole-genome sequencing (WGS)** to identify biallelic SLC25A4 variants. Because the phenotype overlaps many mitochondrial disorders, broad panel/exome testing is the practical first-line genetic approach.

**Clinical criteria / differential diagnosis.** No disease-specific criteria. Differential diagnosis includes other causes of **infantile hypertrophic cardiomyopathy + lactic acidosis**: other mtDNA-maintenance/depletion syndromes (e.g., other SLC25A4 disorders, POLG, MPV17, TK2, AGK/Sengers syndrome — note Sengers also features congenital cataracts + HCM), respiratory-chain complex deficiencies, and fatty-acid-oxidation defects (e.g., VLCADD). The recessive SLC25A4 form is distinguished from dominant SLC25A4 disease by the **absence of ophthalmoplegia** and the childhood cardiomyopathic presentation.

**Screening.** Carrier/cascade testing within affected families once the pathogenic alleles are known; prenatal/preimplantation genetic testing is feasible. No population newborn screening targets this ultra-rare disorder.

---

## Section 11 — Outcome / Prognosis

No formal survival statistics exist for this ultra-rare disease. Prognosis is driven primarily by the **hypertrophic cardiomyopathy**, which carries risk of heart failure and arrhythmia from early life; the myopathy contributes chronic disability and exercise intolerance, and recurrent lactic acidosis adds metabolic morbidity. The disease is chronic, progressive, and lifelong. There is no established disease-specific mortality figure; cardiac involvement is the principal determinant of outcome. **Prognostic factors** likely include severity and progression of cardiomyopathy and the completeness of ANT1 loss. No validated prognostic biomarkers beyond serial cardiac imaging and lactate monitoring are established.

---

## Section 12 — Treatment

**No disease-specific or curative therapy exists.** Management is **supportive and symptomatic**:

- **Cardiac care:** standard heart-failure management for hypertrophic/dilated cardiomyopathy; monitoring for arrhythmia; consideration of advanced cardiac support/transplantation in end-stage cardiac failure (as applied generically in mitochondrial cardiomyopathies).
- **Metabolic support:** management of lactic acidosis; "mitochondrial cocktail" supplements (e.g., coenzyme Q10, L-carnitine, riboflavin) are used empirically across mitochondrial myopathies/cardiomyopathies, though no controlled evidence establishes efficacy specifically in MTDPS12B. (NCIT candidate terms: Coenzyme Q10 therapy, Levocarnitine, Riboflavin.)
- **Supportive/rehabilitative:** physiotherapy for myopathy; activity modification for exercise intolerance; cataract surgery if visually significant.
- **Avoidance** of mitochondrial toxins where possible.

**Advanced therapeutics.** No approved gene, cell, RNA, or targeted therapy. Because the recessive form is a **loss-of-function** disorder, **gene replacement/augmentation** of SLC25A4 is a conceptually attractive but currently experimental strategy. No disease-specific clinical trials (NCT identifiers) are established.

**Pharmacogenomics / personalized medicine.** Not applicable beyond confirming biallelic LOF genotype to guide family counseling.

---

## Section 13 — Prevention

- **Primary prevention:** not possible (inherited monogenic disorder). Prevention centers on **reproductive genetic counseling**.
- **Genetic counseling / reproductive options:** autosomal-recessive recurrence risk of 25% for couples who are both carriers; **carrier screening, prenatal diagnosis, and preimplantation genetic testing (PGT)** are available once the familial SLC25A4 variants are identified.
- **Secondary/tertiary prevention:** early cardiac surveillance and heart-failure management to prevent decompensation; metabolic management to limit acidotic crises; cataract monitoring.
- **Immunization / public-health / environmental interventions:** not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Orthologous genes:** mouse *Slc25a4* (*Ant1*); yeast *AAC2* (the functional ortholog used to validate the human p.Ala123Asp mutation) [PMID: 16155110].
- **Model/natural disease:** the *Ant1−/−* **mouse** (NCBI Taxon 10090) is an engineered model (see Section 15) rather than a naturally occurring disease. No well-characterized naturally occurring companion-animal or wildlife form of recessive ANT1 deficiency is established in the reviewed literature.
- **Evolutionary conservation:** ANT/AAC function (ADP/ATP exchange across the inner mitochondrial membrane) is deeply conserved from yeast to human, underpinning the utility of the yeast AAC2 and mouse *Ant1* systems for modeling human disease.
- **Zoonotic potential:** not applicable (non-infectious genetic disease).

---

## Section 15 — Model Organisms

**Mouse (*Ant1−/−* knockout).** This is the principal model and faithfully recapitulates the human cardiomyopathic/myopathic phenotype (Finding F003). The knockout "*results in lactic acidosis and mitochondrial cardiomyopathy and myopathy, the latter involving hyper-proliferation of mitochondria, induction of oxidative phosphorylation (OXPHOS) enzymes, increased reactive oxygen species (ROS), and excessive mtDNA damage*" [PMID: 18439414], with coordinate upregulation of the mitochondrial-biogenesis and antioxidant programs. *Ant1−/−* skeletal muscle shows ragged-red-fiber-like mitochondrial myopathy [PMID: 16303948].

**Phenotype recapitulation and limitations.** The mouse reproduces the cardiomyopathy, myopathy, ragged-red fibers, mitochondrial proliferation, ROS, and mtDNA damage of the human recessive disease. A key **species difference** is ocular: human *dominant* ANT1 disease (CPEO) preferentially affects extraocular muscle, yet *Ant1−/−* mice have "*no measurable ocular motor abnormalities*," apparently because "*EOMs of wild-type mice exhibited higher levels of Ant2 mRNA … which may compensate for the Ant1 loss*" [PMID: 16303948] — directly illustrating the **ANT2 paralog-compensation** principle (Finding F006). Retinal function is also largely preserved in *Ant1−/−* mice, with supernormal ERG b-waves but normal morphology, suggesting ANT1 is not essential for retinal ATP transport [PMID: 20671283].

**Other models.** The **yeast *AAC2*** system provided orthogonal validation that the human p.Ala123Asp mutation abolishes transport [PMID: 16155110]. *Ant1* heterozygous conditional-knockout mice have additionally been used to probe neuropsychiatric links (bipolar-disorder-associated serotonergic changes) tied to ANT1 haploinsufficiency [PMID: 29892051], although this is tangential to the recessive cardiomyopathic disease.

**Research applications.** These models allow dissection of the bioenergetic defect, mtDNA-maintenance failure, ROS biology, compensatory biogenesis, and tissue-specific paralog compensation — and provide a platform for testing gene-replacement and metabolic therapies.

---

## Key Findings (expanded)

### F001 — Biallelic loss-of-function of SLC25A4/ANT1 is the cause
MTDPS12B is caused by **autosomal-recessive, complete loss of function** of ANT1. The first recessive report described a homozygous c.368C>A (p.Ala123Asp) variant absent from 500 controls, with proteoliposome assays showing no ATP uptake and the yeast AAC2 equivalent abolishing transport [PMID: 16155110]. A later complete-null case documented homozygous c.111+1G>A splice-donor abolition with ANT1 transcript undetectable in muscle and fibroblasts [PMID: 22187496]. Together these establish LOF as the disease mechanism.

### F002 — Recessive and dominant SLC25A4 alleles cause distinct diseases
A clear allelic dichotomy exists: "*Several heterozygous SLC25A4 mutations cause adult-onset autosomal-dominant progressive external ophthalmoplegia associated with multiple mitochondrial DNA deletions, whereas recessive SLC25A4 mutations cause childhood-onset mitochondrial myopathy and cardiomyopathy*" [PMID: 27693233]. Recurrent *de novo* dominant alleles (p.Arg80His, p.Arg235Gly) cause severe neonatal MTDPS12A (OMIM 617184) with marked mtDNA-copy-number loss. This is central to correct diagnosis and classification.

### F003 — The Ant1−/− mouse recapitulates the human phenotype
The knockout mouse develops lactic acidosis, mitochondrial cardiomyopathy and myopathy, mitochondrial hyperproliferation, OXPHOS induction, increased ROS, excessive mtDNA damage, and coordinate upregulation of Pgc-1α/Nrf-1/Tfam/myogenin/antioxidant genes [PMID: 18439414], with ragged-red-fiber-like myopathy [PMID: 16303948] — validating it as a disease model.

### F004 — Clinical phenotype: HCM, myopathy, lactic acidosis, ± cataracts
Core features are hypertrophic cardiomyopathy, mitochondrial myopathy with exercise intolerance, and lactic acidosis, **without ophthalmoplegia** [PMID: 16155110]; the complete-null case added **congenital cataracts** [PMID: 22187496]. Biopsies show ragged-red fibers, abnormal mitochondrial proliferation, increased mitochondrial mass, and multiple mtDNA deletions. The heterozygous carrier mother was unaffected, confirming recessivity.

### F005 — Mechanism: transport loss → energy crisis + secondary mtDNA instability
ANT1 normally "*exports mitochondrial ATP to the cytosol*" [PMID: 18439414]; recessive LOF abolishes ADP/ATP exchange. The reduced transport "*probably affects mitochondrial DNA maintenance and in turn respiration, causing a severe energy crisis*" [PMID: 27693233], with loss of mtDNA-encoded respiratory-chain complexes and reduced mtDNA copy number. Structural work maps disease mutations onto the carrier's substrate-binding architecture, correlating location with severity [PMID: 42308345].

### F006 — Tissue specificity from isoform expression; partial paralog compensation
"*The ANT1 isoform predominates in heart and muscle while ANT2 is systemic*" [PMID: 35714845], explaining the striated-muscle-restricted disease. Compensation is incomplete and tissue-dependent: no ANT3 upregulation occurred in affected human muscle [PMID: 22187496], whereas higher *Ant2* in mouse extraocular muscle may spare ocular motility [PMID: 16303948].

---

## Mechanistic Model

```
  SLC25A4 biallelic LOF (p.Ala123Asp / c.111+1G>A)
                 │
                 ▼
  Absent / nonfunctional ANT1 (AAC1) in heart & skeletal muscle
                 │   (ANT2/ANT3 compensate only partially,
                 │    tissue-dependent → striated-muscle restriction)
                 ▼
  Abolished inner-membrane ADP/ATP exchange
      ├───────────────┐
      ▼               ▼
 Energy crisis    Impaired mtDNA maintenance (inferred)
 (ATP export         → multiple mtDNA deletions
  failure)           → reduced mtDNA copy number
      │               → loss of mtDNA-encoded OXPHOS subunits
      │                      │
      ▼                      ▼
 Lactic acidosis    Respiratory-chain deficiency ──► feeds back to energy crisis
      │
      ▼
 Compensatory mitochondrial biogenesis / hyperproliferation
 (ragged-red fibers, ↑ROS → more mtDNA damage)
      │
      ▼
 CLINICAL: Hypertrophic cardiomyopathy + mitochondrial myopathy
           + exercise intolerance + lactic acidosis (± congenital cataracts)
```

**Upstream:** SLC25A4 mutation → transport loss. **Downstream:** energy crisis, mtDNA instability, ROS, mitochondrial proliferation → cardiomyopathy/myopathy.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [PMID: 16155110](https://pubmed.ncbi.nlm.nih.gov/16155110/) | Complete LOF of heart/muscle ANT associated with myopathy & cardiomyopathy | Establishes recessive LOF (p.Ala123Asp), transport-null proteoliposomes, yeast validation; core phenotype without ophthalmoplegia |
| [PMID: 22187496](https://pubmed.ncbi.nlm.nih.gov/22187496/) | Complete loss of ANT1 expression causing cardiomyopathy & myopathy | Splice-null complete-null case; adds congenital cataracts; no ANT3 compensation; recessive (unaffected carrier mother) |
| [PMID: 27693233](https://pubmed.ncbi.nlm.nih.gov/27693233/) | Recurrent de novo dominant SLC25A4 mutations (MTDPS12A) | Distinguishes recessive vs dominant disease; energy-crisis/mtDNA-maintenance mechanism |
| [PMID: 18439414](https://pubmed.ncbi.nlm.nih.gov/18439414/) | MITOCHIP in Ant1-KO muscle | Mouse phenotype + biogenesis/antioxidant program; defines ANT1 ATP-export function |
| [PMID: 16303948](https://pubmed.ncbi.nlm.nih.gov/16303948/) | Ant1-KO: CPEO pathology, normal ocular motility | Ragged-red-fiber myopathy; ANT2 paralog compensation in EOM |
| [PMID: 35714845](https://pubmed.ncbi.nlm.nih.gov/35714845/) | ANT transporters in myogenesis | Isoform expression (ANT1 heart/muscle; ANT2 systemic) explaining tissue specificity |
| [PMID: 42308345](https://pubmed.ncbi.nlm.nih.gov/42308345/) | Structural basis of AAC substrate transport & disease heterogeneity | Maps severity to substrate-binding sites (S1 lethal, S2 milder) |
| [PMID: 20671283](https://pubmed.ncbi.nlm.nih.gov/20671283/) | Retinal function in Ant1-deficient mice | Retina largely spared; ANT1 not essential for retinal ATP transport |
| [PMID: 29892051](https://pubmed.ncbi.nlm.nih.gov/29892051/) | Ant1 mutant mice & serotonergic/BD link | Heterozygous haploinsufficiency neuropsychiatric model (tangential) |

---

## Limitations and Knowledge Gaps

- **Very small human sample.** The recessive cardiomyopathic form rests on a handful of index cases; prevalence, incidence, sex ratio, penetrance estimates, survival statistics, and the full phenotypic range are therefore poorly quantified.
- **mtDNA-maintenance link is associative.** The connection between ANT1 transport loss and secondary mtDNA deletions/depletion is stated as "probable" [PMID: 27693233]; the precise biochemical pathway (e.g., matrix dNTP/adenine-nucleotide pool imbalance) has not been fully demonstrated for the recessive disease.
- **Compensation biology incomplete.** Why ANT2/ANT3 fail to rescue human heart/muscle, and the quantitative thresholds for compensation, remain to be defined.
- **No therapeutic evidence.** No controlled trials; "mitochondrial cocktail" use is empirical and unproven for MTDPS12B.
- **Cataract mechanism unexplained.** Whether congenital cataracts are a consistent feature or case-specific (and their mechanistic basis) is unresolved; overlap with Sengers-like phenotypes warrants attention in differential diagnosis.

---

## Proposed Follow-up Experiments / Actions

1. **Aggregate a patient registry / genotype–phenotype series** (via GeneMatcher, mitochondrial-disease networks) to quantify prevalence, penetrance, phenotype frequencies, cataract incidence, and natural history.
2. **Directly test the mtDNA-maintenance hypothesis** — measure mitochondrial dNTP/adenine-nucleotide pools and mtDNA deletion burden in ANT1-null human cardiomyocytes/myotubes (iPSC-derived) versus isogenic controls.
3. **iPSC-derived cardiomyocyte and skeletal-myotube models** from recessive patients to characterize bioenergetics (Seahorse), OXPHOS assembly, ROS, and mtDNA copy number, and to screen candidate therapies.
4. **Paralog-rescue experiments:** test whether forced ANT2/ANT3 expression rescues the energy crisis in ANT1-null human striated-muscle models, defining compensation thresholds.
5. **Gene-replacement proof-of-concept** (AAV-SLC25A4) in the *Ant1−/−* mouse heart/muscle, given the recessive LOF mechanism.
6. **Structure-guided variant interpretation:** apply the S1/S2 substrate-site framework [PMID: 42308345] to classify newly found SLC25A4 variants and predict recessive-versus-dominant behavior and severity.
7. **Cardiac natural-history imaging study** to identify prognostic biomarkers (echo/MRI parameters, serial lactate) for the life-limiting cardiomyopathy.

---

*Evidence source types: human clinical case reports (PMID 16155110, 22187496, 27693233), model-organism studies (mouse: 18439414, 16303948, 20671283, 29892051; yeast: within 16155110), and in-vitro/computational structural work (42308345). Ontology suggestions (MONDO:0014175; HPO HP:0001639, HP:0003198, HP:0003546, HP:0003128, HP:0003200, HP:0000519; GO:0140021, GO:0005743, GO:0000002, GO:0006979; CL:0000746, CL:0000188; UBERON:0000948, UBERON:0001134, UBERON:0000965) are provided to support knowledge-base curation.*


## Artifacts

- [OpenScientist final report](Mitochondrial_DNA_Depletion_Syndrome_12B-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mitochondrial_DNA_Depletion_Syndrome_12B-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 9 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:22187496` *(abstract only)*: "*No compensating increase in the transcript level of the ANT3 gene … was observed*"
  - closest text in source: "No compensating increase in the transcript level of the ANT3 gene, which encodes the human ubiquitous isoform of the ADP/ATP translocase, was observed"
- `PMID:18439414` *(abstract only)*: "*coordinate upregulation of Pgc-1α, Nrf-1, Tfam, myogenin and antioxidant genes*"
  - closest text in source: "The mitochondrial regulatory proteins Pgc-1alpha, Nrf-1, Tfam, and myogenin were up-regulated and could account for the induction of the OXPHOS and antioxidant enzymes"
- `PMID:16303948` *(abstract only)*: "*EOMs of wild-type mice exhibited higher levels of Ant2 mRNA … which may compensate for the Ant1 loss*"
  - closest text in source: "EOMs of wild-type mice exhibited higher levels of Ant2 mRNA compared with hindlimb muscle, which may compensate for the Ant1 loss in mutant mouse EOMs and account for the normal EOM function"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014175` (4 mentions) - the report calls it "MONDO"; MONDO calls it **mitochondrial DNA depletion syndrome 12B (cardiomyopathic type), autosomal recessive**
- `HP:0001639` (2 mentions) - the report calls it "Clinical sign / cardiac"; HP calls it **Hypertrophic cardiomyopathy**
- `HP:0003546` (2 mentions) - the report calls it "Symptom"; HP calls it **Exercise intolerance**
- `HP:0003200` (2 mentions) - the report calls it "Laboratory/histopathology"; HP calls it **Ragged-red muscle fibers**
- `HP:0000519` (2 mentions) - the report calls it "Clinical sign / ocular"; HP calls it **Developmental cataract**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0000002` (obsolete mitochondrial genome maintenance) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003128` (3 mentions) - the report calls it "elevated lactate"; HP calls it **Lactic acidosis**, and lists "Increased lactate in body" among its other names
- `HP:0003689` (1 mention) - the report calls it "mtDNA deletion"; HP calls it **Multiple mitochondrial DNA deletions**, and lists "Multiple mtDNA deletions" among its other names
- `GO:0000002` (2 mentions) - the report calls it "mitochondrial genome maintenance"; GO calls it **obsolete mitochondrial genome maintenance**
- `UBERON:0000948` (2 mentions) - the report calls it "Primary organs:** heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names
- `UBERON:0000965` (2 mentions) - the report calls it "Secondary involvement:** ocular lens"; UBERON calls it **lens of camera-type eye**, and lists "ocular lens" among its other names
- `GO:0005739` (1 mention) - the report calls it "mitochondrion", "Subcellular level:** **mitochondrion"; GO calls it **mitochondrion**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005739` - called "mitochondrion", "Subcellular level:** **mitochondrion"