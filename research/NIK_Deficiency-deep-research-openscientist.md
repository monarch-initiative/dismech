---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T05:31:48.788497'
end_time: '2026-10-25T05:49:46.901337'
duration_seconds: 1078.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: NIK Deficiency
  mondo_id: MONDO:0018642
  category: Mendelian
  causal_genes: MAP3K14
  omim_id: not recorded
  synonyms: MAP3K14 non-severe combined immunodeficiency; non-severe combined immunodeficiency
    caused by mutation in MAP3K14; primary immunodeficiency with multifaceted aberrant
    lymphoid immunity
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 16
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 30
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 5
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0018642
    reported_labels:
    - MONDO
    ontology_label: NIK deficiency
  - term_id: HP:0002718
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent bacterial infections
  - term_id: HP:0004429
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent viral infections
  - term_id: HP:0100792
    reported_labels:
    - Clinical/laboratory
    ontology_label: Acantholysis
  - term_id: HP:0010976
    reported_labels:
    - Laboratory abnormality
    ontology_label: Decreased total B cell count
  - term_id: HP:0002720
    reported_labels:
    - Laboratory abnormality
    ontology_label: Decreased circulating IgA concentration
  - term_id: HP:0005404
    reported_labels:
    - Laboratory abnormality
    ontology_label: Increased total B cell count
  - term_id: HP:0040218
    reported_labels:
    - Laboratory abnormality
    ontology_label: Reduced total natural killer cell count
  - term_id: HP:0005415
    reported_labels:
    - abnormal T-cell count
    ontology_label: Decreased total CD8+ T cell proportion
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0004704
    ontology_label: obsolete NF-kappaB-inducing kinase activity
  - term_id: GO:0051092
    ontology_label: obsolete positive regulation of NF-kappaB transcription factor
      activity
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: NIK_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: NIK_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NIK Deficiency
- **MONDO ID:** MONDO:0018642 (if available)
- **Causal gene(s):** MAP3K14
- **OMIM:** not recorded
- **Synonyms:** MAP3K14 non-severe combined immunodeficiency; non-severe combined immunodeficiency caused by mutation in MAP3K14; primary immunodeficiency with multifaceted aberrant lymphoid immunity
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **NIK Deficiency** covering all of the
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

# NIK Deficiency (MONDO:0018642): A Comprehensive Disease Characteristics Report

## Summary

**NIK Deficiency is an ultra-rare, autosomal-recessive combined primary immunodeficiency caused by biallelic loss-of-function mutations in *MAP3K14*** (HGNC:6853; NCBI Gene 9020; OMIM \*604655; Ensembl ENSG00000006062; UniProt Q99558; chr17q21.31), the gene encoding **NIK (NF-κB–inducing kinase)**. NIK is the apical, rate-limiting kinase of the **non-canonical (alternative) NF-κB pathway**. Disease arises when both alleles carry a kinase-inactivating mutation, abolishing NIK's ability to drive IKKα-mediated processing of the NF-κB2 precursor p100 into active p52, and consequently crippling RelB/p52-dependent transcription. Because NIK also feeds forward into prolonged canonical NF-κB signaling, patients have defects in *both* arms of the pathway.

The clinical consequence is a multifaceted combined immunodeficiency. The index report (Willmann et al. 2014, [PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/)) described patients with recurrent bacterial, viral, and *Cryptosporidium* infections, who exhibited B-cell lymphopenia, decreased class-switched memory B cells, hypogammaglobulinemia, impaired ICOSL expression, perturbed follicular-helper (Tfh) and memory T cells, and decreased/defective NK cells with impaired immunological-synapse formation. The disease belongs to a tightly related family of **non-canonical NF-κB inborn errors of immunity** (alongside *NFKB2*, *RELB*, and *CHUK*/IKKα defects) that share a striking predisposition to **neutralizing autoantibodies against type I interferon**.

NIK deficiency sits at the **loss-of-function pole of a bidirectional, dose-dependent NIK disease axis**: too little NIK produces immunodeficiency, while excess NIK activity drives autoimmunity, cancer, sterile inflammation, fibrosis, and metabolic disease (Valiño-Rivas et al. 2019, [PMID: 30926358](https://pubmed.ncbi.nlm.nih.gov/30926358/)). Diagnosis currently rests on **functional validation of kinase activity** because no pathogenic *MAP3K14* variants are deposited in ClinVar, and the gene is strongly loss-of-function–intolerant in the general population (gnomAD pLI ≈ 1.0) yet the disease is recessive. Allogeneic hematopoietic stem cell transplantation (HSCT) can reconstitute the hematopoietic immune compartment but does not repair the radioresistant stromal/thymic architectural defects, so lifelong immunologic and anti-cytokine autoantibody surveillance is required (Köstel Bal et al. 2025, [PMID: 41280889](https://pubmed.ncbi.nlm.nih.gov/41280889/)).

This report synthesizes 8 confirmed findings across 34 reviewed papers into a comprehensive disease-knowledge-base entry covering all 15 requested domains. Where primary human data are sparse (reflecting the extreme rarity of the disorder), mechanism is supported by an extensive murine and in vitro literature, and these evidence levels are flagged throughout.

---

## Key Findings

### F001 — NIK deficiency is a biallelic *MAP3K14* loss-of-function primary immunodeficiency

Willmann et al. (2014) identified a **biallelic mutation in *MAP3K14* (NIK)** in patients presenting with recurrent bacterial, viral, and *Cryptosporidium* infections. The mutation abolishes NIK kinase activity, which was *"predicted by in silico analysis and confirmed by functional assays"* and *"leads to defective activation of both canonical and non-canonical NF-κB signalling"* ([PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/)). The immunological phenotype is broad and spans all three major lymphocyte lineages: B-cell lymphopenia, decreased class-switched memory B cells, hypogammaglobulinemia (reflecting impaired B-cell survival), impaired ICOSL expression, perturbed Tfh and memory T-cell compartments, and decreased/defective NK cells with impaired immunological-synapse formation. This single landmark paper establishes the causal gene, the recessive (biallelic) inheritance, and the core molecular lesion — loss of NIK kinase activity — that defines the disease.

**Evidence level:** Human clinical + in vitro functional assay.

### F002 — NIK is the rate-limiting kinase of the non-canonical NF-κB pathway, controlling p100→p52/RelB processing

NIK (MAP3K14) is normally held at vanishingly low levels by constitutive degradation through the **TRAF2–TRAF3–cIAP1/2 ubiquitin-ligase complex**. Engagement of TNF-receptor-superfamily receptors — **BAFFR, CD40, LTβR, RANK, and Fn14** — triggers TRAF3 degradation, which stabilizes and allows NIK to accumulate. Accumulated NIK phosphorylates **IKKα**, which in turn phosphorylates **NF-κB2/p100**, driving its proteasomal processing to **p52** and the nuclear translocation of **RelB/p52** heterodimers. Senftleben et al. (2001) established the kinase hierarchy: *"IKKalpha is required for B cell maturation, formation of secondary lymphoid organs, increased expression of certain NF-kappaB target genes, and processing of the NF-kappaB2 (p100) precursor. IKKalpha preferentially phosphorylates NF-kappaB2, and this activity requires its phosphorylation by upstream kinases, one of which may be NF-kappaB-inducing kinase (NIK)"* ([PMID: 11520989](https://pubmed.ncbi.nlm.nih.gov/11520989/)). Dash et al. (2020) showed in multiple myeloma that lower TRAF3 expression and higher NIK expression mark pathway activation ([PMID: 32350909](https://pubmed.ncbi.nlm.nih.gov/32350909/)). In NIK-deficient patients, kinase-dead NIK abolishes p100→p52 processing, collapsing the entire downstream axis.

**Evidence level:** In vitro / model organism (mechanistic hierarchy); human (disease relevance).

### F003 — Mouse models (aly/aly, NIK KO, conditional) recapitulate the lymphoid defects

The spontaneous **alymphoplasia (*aly/aly*) mouse** carries a loss-of-function point mutation in *Nik/Map3k14* and displays absence of lymph nodes and Peyer's patches, disrupted lymphoid architecture, and impaired B-cell formation and immunoglobulin production. Ozcan et al. (2026) summarize: *"NIK deficiency causes loss of lymph nodes, disruption of lymphoid organ structure and deficits in B-cell formation and immunoglobulin production"* ([PMID: 42175627](https://pubmed.ncbi.nlm.nih.gov/42175627/)). Conditional deletion of NIK in adult mice reduces B-cell populations and germinal-center B cells and abrogates BAFF responses: *"Germline deletion or inactivation of NIK in mice results in the defective development of B cells and secondary lymphoid organs"* (Brightbill et al. 2015, [PMID: 26116508](https://pubmed.ncbi.nlm.nih.gov/26116508/)). NIK additionally supports medullary and cortical thymic-epithelial-cell development (Eshima et al. 2020, [PMID: 32145062](https://pubmed.ncbi.nlm.nih.gov/32145062/)) and has a cell-intrinsic role in effector/memory T-cell generation (Li et al. 2016, [PMID: 26912039](https://pubmed.ncbi.nlm.nih.gov/26912039/)). The murine models thus faithfully reproduce the B-cell, secondary-lymphoid-organ, and thymic-architectural defects seen in patients.

**Evidence level:** Model organism (mouse).

### F004 — The NIK kinase domain is structurally characterized, active-like without phosphorylation, with a narrow flexible active site

Crystal structures of the apo NIK catalytic domain (both human and murine) reveal an **active-like conformation in the absence of phosphorylation**. de Leon-Boenig et al. (2012) report: *"Structures of the apo NIK kinase domain from both species reveal an active-like conformation in the absence of phosphorylation. ATP consumption and peptide phosphorylation assays confirm that phosphorylation of NIK does not increase enzymatic activity"* ([PMID: 22921830](https://pubmed.ncbi.nlm.nih.gov/22921830/)). The active site is narrow with a flexible gatekeeper residue. This structural biology explains two important facts about the disease: (1) NIK is regulated primarily by **protein abundance** (stabilization), not by activation-loop phosphorylation, so loss-of-function in disease is achieved by missense mutations that destroy catalytic competence or protein stability rather than by blocking an activating phosphorylation; and (2) the well-defined ATP pocket has enabled structure-based inhibitor design (Li et al. 2013, [PMID: 23374866](https://pubmed.ncbi.nlm.nih.gov/23374866/)), relevant to the *gain-of-function* end of the disease axis.

**Evidence level:** Computational/structural + in vitro biochemistry.

### F005 — NIK deficiency belongs to the non-canonical NF-κB IEI family that shares anti–type I IFN autoantibody predisposition

Human inborn errors of the non-canonical NF-κB axis — *NFKB2* (p100), *RELB*, *CHUK*/IKKα, and *MAP3K14*/NIK — produce overlapping combined immunodeficiency with hypogammaglobulinemia. A clinically important shared feature is **neutralizing autoantibodies against type I interferon**. Riller et al. (2025) reported that IKKα (CHUK) kinase-domain–deficient patients have diminished non-canonical (and partially impaired canonical) NF-κB with *"neutralizing autoantibodies against type I IFN, akin to non-canonical NF-κB pathway deficiencies"* ([PMID: 39812688](https://pubmed.ncbi.nlm.nih.gov/39812688/)). RelB deficiency likewise *"disrupts the non-canonical NF-κB pathway, underlying a T- and B cell immunodeficiency, which, together with neutralizing autoantibodies against type I IFNs"* (Moriya 2026, [PMID: 42261849](https://pubmed.ncbi.nlm.nih.gov/42261849/)). Consistent with membership in this family, the NIK-deficiency HSCT follow-up study emphasized monitoring for anti-cytokine autoantibodies ([PMID: 41280889](https://pubmed.ncbi.nlm.nih.gov/41280889/)). This predisposition likely reflects failure of central/peripheral tolerance mechanisms that depend on non-canonical NF-κB (AIRE-dependent medullary thymic epithelial cell function).

**Evidence level:** Human clinical (family of disorders).

### F006 — NIK dosage determines disease direction: loss → immunodeficiency; overactivity → autoimmunity/cancer/fibrosis

NIK sits at the center of a **bidirectional, dose-dependent disease axis**. Valiño-Rivas et al. (2019) frame NIK as the apical non-canonical NF-κB kinase whose disease spectrum *"now ranges from immunodeficiency (when NIK is defective) to autoimmunity, cancer, sterile inflammation, fibrosis, and metabolic disease when NIK is overactive"* ([PMID: 30926358](https://pubmed.ncbi.nlm.nih.gov/30926358/)). NIK deficiency occupies the **loss-of-function pole**. The physiological processes placed at risk by NIK loss are enumerated by Liu et al. (2019): *"The non-canonical NF-κB signalling cascade is essential for lymphoid organogenesis, B cell maturation, osteoclast differentiation, and inflammation in mammals"* ([PMID: 30894749](https://pubmed.ncbi.nlm.nih.gov/30894749/)). NIK also drives prolonged *canonical* NF-κB via IKKα/β in endothelium (Kucharzewska et al. 2019, [PMID: 30837284](https://pubmed.ncbi.nlm.nih.gov/30837284/)), explaining the combined-pathway defect. TRAF2, the upstream NIK regulator, stimulates NK-cell cytotoxicity (Albini et al. 2025, [PMID: 40229245](https://pubmed.ncbi.nlm.nih.gov/40229245/)), consistent with the NK defect observed in patients.

**Evidence level:** Review synthesis + model organism + human.

### F007 — Gene identifiers confirmed; ClinVar holds no pathogenic *MAP3K14* variants

Programmatic verification established: **MAP3K14 = HGNC:6853, NCBI Gene 9020, OMIM \*604655, Ensembl ENSG00000006062, UniProt Q99558, cytoband 17q21.31, GRCh38 chr17:45,263,119–45,317,112 (minus strand), RefSeq NM_003954.5.** A ClinVar query (`MAP3K14[gene]`) returned 30 variant records, all classified **VUS or Likely benign** (e.g., p.Ser97Ter VUS; p.Val828fs VUS); **zero Pathogenic/Likely-pathogenic entries**. The disease-causing biallelic kinase-domain variants described in patients are *not* deposited in ClinVar as pathogenic. This is a critical practical point: a clinical diagnosis cannot currently rely on a ClinVar pathogenicity lookup and must instead be anchored by **functional kinase-activity assays**, exactly as in the index report where pathogenicity was *"predicted by in silico analysis and confirmed by functional assays"* ([PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/)).

**Evidence level:** Database verification (computational) + human.

### F008 — *MAP3K14* is strongly LoF-intolerant in gnomAD (pLI ≈ 1.0), yet the disease is recessive

gnomAD constraint metrics for *MAP3K14* (GRCh38) are: **pLI = 1.00, observed/expected LoF = 0.16 (LOEUF 90% CI 0.11–0.24), LoF Z = 7.09, missense Z = 5.21** — indicating strong depletion of both predicted-LoF and missense variation in the general population. The apparent paradox — a haploinsufficiency-intolerant gene causing a *recessive* disease — is resolved by the biology: heterozygous carrier parents are clinically unaffected (Willmann et al. 2014, [PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/)), so the immunodeficiency requires biallelic loss, while the high population constraint likely reflects strong selection against *loss* in combination with the fact that NIK overactivity (the other pole of the axis) is also deleterious — tight dosage control is evolutionarily favored in both directions.

**Evidence level:** Population genetics (computational) + human.

---

## Detailed Section-by-Section Report

### 1. Disease Information

**Overview.** NIK deficiency is a Mendelian, autosomal-recessive **combined primary immunodeficiency / inborn error of immunity** caused by biallelic loss-of-function mutations in ***MAP3K14***, which encodes **NF-κB–inducing kinase (NIK)**. The disorder produces a multifaceted defect of lymphoid immunity affecting B cells, T cells, and NK cells, together with structural defects of secondary lymphoid organs and thymic epithelium, clinically manifesting as recurrent bacterial, viral, and *Cryptosporidium* infections.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0018642 |
| Causal gene | *MAP3K14* (NIK) |
| HGNC | HGNC:6853 |
| NCBI Gene | 9020 |
| Gene OMIM | \*604655 |
| Disease OMIM | Not recorded |
| Ensembl | ENSG00000006062 |
| UniProt | Q99558 |
| Cytoband | 17q21.31 |
| RefSeq transcript | NM_003954.5 |
| ICD-10 / ICD-11 | No specific code; best coded under combined immunodeficiency (ICD-10 D81.-; ICD-11 4A00.-) |

**Synonyms / alternative names.** MAP3K14 non-severe combined immunodeficiency; non-severe combined immunodeficiency caused by mutation in MAP3K14; primary immunodeficiency with multifaceted aberrant lymphoid immunity; NIK deficiency.

**Source of information.** The disease-level knowledge is derived from a small number of **individual patient reports** (index family, Willmann et al. 2014; HSCT long-term follow-up, Köstel Bal et al. 2025) supplemented by **aggregated gene/variant resources** (OMIM, ClinVar, gnomAD) and an extensive **model-organism and in vitro mechanistic literature**. There is no large aggregated clinical registry given the disorder's rarity.

### 2. Etiology

**Primary cause — genetic.** Biallelic loss-of-function mutations in *MAP3K14* abolishing NIK kinase activity (F001). The index variant was a kinase-domain mutation confirmed functionally ([PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/)).

**Genetic risk factors.** The disease is monogenic and fully penetrant with biallelic LoF; there is no evidence for susceptibility loci or modifier genes in humans (too few patients). Carrier status (heterozygous) confers no known clinical risk. **Consanguinity** is a strong contextual risk factor as for most ultra-rare recessive disorders.

**Environmental / infectious contributors.** Environmental factors do not *cause* the disease but act as the **trigger for clinical presentation**: encapsulated bacteria, herpesviruses (e.g., CMV), and the opportunistic protozoan ***Cryptosporidium*** are the organisms that exploit the immune defect. *Cryptosporidium* infection with potential hepatobiliary involvement is a hallmark that overlaps with other T-cell/combined immunodeficiencies.

**Protective factors.** None specific are documented. In principle, a functional second *MAP3K14* allele (heterozygosity) is fully protective, consistent with recessive inheritance (F008).

**Gene–environment interactions.** The core interaction is permissive: the genetic lesion removes host defense, and environmental pathogen exposure determines the timing, severity, and organ pattern of disease. No classical GxE modifier data exist.

### 3. Phenotypes

Phenotypes are drawn primarily from the index clinical report (F001) and HSCT follow-up (F005). Frequencies are qualitative given the tiny cohort.

| Phenotype | Type | HPO suggestion | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Recurrent bacterial infections | Clinical sign | HP:0002718 | Childhood | Severe | Characteristic |
| Recurrent viral infections (incl. CMV) | Clinical sign | HP:0004429 | Childhood | Severe | Characteristic |
| Chronic *Cryptosporidium* diarrhea | Clinical sign | HP:0002028 (chronic diarrhea) | Childhood | Severe | Characteristic |
| Sclerosing cholangitis / hepatobiliary involvement | Clinical/laboratory | HP:0100792 | Childhood | Severe | Reported |
| B-cell lymphopenia | Laboratory abnormality | HP:0010976 | Congenital/early | Severe | Consistent |
| Hypogammaglobulinemia | Laboratory abnormality | HP:0002720 | Early | Moderate–severe | Consistent |
| Decreased class-switched memory B cells | Laboratory abnormality | HP:0005404 | Early | Severe | Consistent |
| Decreased/defective NK cells | Laboratory abnormality | HP:0040218 | Early | Moderate–severe | Consistent |
| Perturbed Tfh / memory T cells | Laboratory abnormality | HP:0005415 (abnormal T-cell count) | Early | Moderate | Consistent |
| Impaired NK immunological synapse | Cellular phenotype | — | — | — | In vitro |
| Predisposition to anti–type I IFN autoantibodies | Laboratory abnormality | HP:0002960 (autoimmunity) | Variable | Variable | Shared-family feature |

**Quality-of-life impact.** Chronic/recurrent infections and chronic diarrhea with hepatobiliary disease substantially impair growth, nutrition, and daily functioning. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder.

### 4. Genetic / Molecular Information

**Causal gene.** *MAP3K14* / NIK (identifiers in Section 1; F007).

**Pathogenic variants.** The index disease allele is a **kinase-domain mutation** causing loss of NIK catalytic activity, validated functionally (F001). **No pathogenic or likely-pathogenic *MAP3K14* variants are currently in ClinVar** (30 records, all VUS/likely-benign; F007). Variant classes expected to cause disease: **missense within the kinase domain** (as in the index case), and in principle **nonsense, frameshift, and splice-site** biallelic LoF alleles. All are **germline**. **Functional consequence: loss of function** (kinase-dead), impairing both non-canonical and canonical NF-κB (F001, F006).

**Allele frequency / constraint.** *MAP3K14* is strongly LoF-intolerant: **pLI = 1.00, o/e LoF = 0.16 (LOEUF 0.11–0.24), LoF Z = 7.09, missense Z = 5.21** (gnomAD; F008). Disease-causing alleles are private/ultra-rare.

**Modifier genes / epigenetics / chromosomal abnormalities.** No human modifier genes, disease-specific epigenetic marks, or chromosomal abnormalities are documented for NIK deficiency. (Note: in *cancers*, non-canonical NF-κB activation can occur via *MAP3K14* dysregulation — e.g., S100A14/UPF1-mediated stabilization of *MAP3K14/NFKB2/RELB* transcripts, [PMID: 42350366](https://pubmed.ncbi.nlm.nih.gov/42350366/) — but this is the opposite, gain-of-activity pole and not the inherited deficiency.)

### 5. Environmental Information

- **Environmental/occupational toxins, radiation, pollution:** Not implicated in disease causation.
- **Lifestyle factors:** Not applicable (monogenic disorder).
- **Infectious agents:** Central to clinical expression. Key organisms include encapsulated **bacteria**, **viruses** (notably CMV and other herpesviruses), and the protozoan ***Cryptosporidium*** (NCBI Taxonomy: *Cryptosporidium* genus), which causes chronic diarrhea and can involve the hepatobiliary tract in immunodeficient hosts. These are *opportunistic consequences* of the immune defect, not causes of the mutation.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic LoF mutation in *MAP3K14*** → produces a **kinase-dead NIK protein** (demonstrated: in silico + functional assays, [PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/)).
2. Kinase-dead NIK **fails to phosphorylate IKKα** upon TNF-receptor-superfamily engagement (BAFFR, CD40, LTβR, RANK, Fn14) → **results in** failure of IKKα to phosphorylate p100 (demonstrated mechanistically, [PMID: 11520989](https://pubmed.ncbi.nlm.nih.gov/11520989/)).
3. Unphosphorylated **p100 is not processed to p52** → **leads to** loss of nuclear RelB/p52 heterodimer transcription (non-canonical NF-κB collapse).
4. NIK loss **also impairs sustained canonical NF-κB** (NIK–IKKα/β interaction) → **results in** a combined two-pathway defect ([PMID: 30837284](https://pubmed.ncbi.nlm.nih.gov/30837284/); [PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/)).
5. **Branch A — Stromal/structural:** Loss of LTβR→NIK→RelB/p52 signaling in stromal and epithelial cells → **leads to** absent/hypoplastic **lymph nodes, Peyer's patches**, disrupted splenic architecture, and defective **thymic epithelial cell** development (demonstrated in mouse; [PMID: 42175627](https://pubmed.ncbi.nlm.nih.gov/42175627/), [PMID: 32145062](https://pubmed.ncbi.nlm.nih.gov/32145062/)).
6. **Branch B — B cells:** Loss of BAFFR/CD40→NIK signaling → **leads to** impaired B-cell survival and maturation → **results in** B-cell lymphopenia, decreased class-switched memory B cells, and hypogammaglobulinemia ([PMID: 26116508](https://pubmed.ncbi.nlm.nih.gov/26116508/); [PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/)).
7. **Branch C — T cells:** Cell-intrinsic NIK loss → **impairs** effector/memory T-cell generation and Tfh function → **contributes to** impaired antibody help and ICOSL dysregulation ([PMID: 26912039](https://pubmed.ncbi.nlm.nih.gov/26912039/)).
8. **Branch D — NK cells:** NIK/TRAF2-axis loss → **leads to** decreased/defective NK cells with impaired immunological-synapse formation ([PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/); [PMID: 40229245](https://pubmed.ncbi.nlm.nih.gov/40229245/)).
9. **Branch E — Tolerance (inferred):** Impaired AIRE-dependent medullary thymic epithelial function → **predisposes to** neutralizing anti–type I IFN autoantibodies (inferred from shared non-canonical NF-κB IEI family; [PMID: 39812688](https://pubmed.ncbi.nlm.nih.gov/39812688/), [PMID: 42261849](https://pubmed.ncbi.nlm.nih.gov/42261849/)).
10. Combined cellular and structural defects → **result in** the clinical phenotype: **recurrent bacterial/viral/*Cryptosporidium* infections**, with chronic diarrhea and hepatobiliary disease.

**Molecular pathways (Reactome/KEGG):** Non-canonical NF-κB signaling (Reactome R-HSA-5676590); canonical NF-κB; TNF-receptor-superfamily signaling.

**Cellular processes & GO terms:** NIK/NF-κB-inducing kinase activity (GO:0004704 MAP kinase kinase kinase activity); positive regulation of NF-κB transcription factor activity (GO:0051092); B-cell homeostasis (GO:0001782); lymph node development (GO:0048535); I-κB kinase/NF-κB signaling (GO:0007249).

**Protein dysfunction:** Loss of kinase function in an otherwise **constitutively active-like** kinase domain regulated by abundance (F004, [PMID: 22921830](https://pubmed.ncbi.nlm.nih.gov/22921830/)).

**Immune system involvement:** Combined immunodeficiency (B, T, NK) plus autoimmune/tolerance predisposition (F005).

**Molecular profiling:** In myeloma, low TRAF3 + high NIK expression mark pathway activation ([PMID: 32350909](https://pubmed.ncbi.nlm.nih.gov/32350909/)) — a useful readout of the axis, though from the opposite (gain) pole.

**Upstream vs downstream:** Mutation (upstream) → NIK kinase failure → IKKα → p100/p52 (midstream) → RelB/p52 transcriptional programs in B cells, stroma, TECs, T cells, NK cells (downstream) → clinical infection susceptibility.

### 7. Anatomical Structures Affected

- **Organ level (primary):** Secondary lymphoid organs — **lymph nodes** (UBERON:0000029), **spleen** (UBERON:0002106), **Peyer's patches / gut-associated lymphoid tissue** (UBERON:0001211); **thymus** (UBERON:0002370, thymic epithelium); **bone marrow** (UBERON:0002371).
- **Secondary involvement:** **Gastrointestinal tract** (chronic *Cryptosporidium* diarrhea; UBERON:0000160) and **hepatobiliary system / bile ducts** (sclerosing cholangitis; UBERON:0002394).
- **Body systems:** Immune/hematolymphoid system (primary); digestive and hepatobiliary systems (secondary).
- **Tissue/cell level (Cell Ontology):** B cells (CL:0000236), including class-switched memory B cells; T cells (CL:0000084), follicular-helper and memory subsets; NK cells (CL:0000623); thymic epithelial cells (CL:0002293); lymphoid stromal cells.
- **Subcellular (GO cellular component):** Cytoplasm (GO:0005737, where NIK acts upstream of IKK), nucleus (GO:0005634, RelB/p52 translocation target).
- **Lateralization:** Systemic/bilateral; not a lateralized disorder.

### 8. Temporal Development

- **Onset:** Early — **congenital immune architecture defects** present from development; **clinical infections in infancy/childhood**. Onset pattern is chronic/insidious with recurrent acute infectious episodes.
- **Progression:** Without immune reconstitution, the course is a chronic, lifelong combined immunodeficiency with recurrent and opportunistic infections; organ damage (e.g., sclerosing cholangitis) can be progressive and severe.
- **Course pattern:** Chronic with episodic infectious exacerbations.
- **Remission:** No spontaneous remission; **treatment-induced** immune reconstitution is achievable with HSCT for the hematopoietic compartment, but the **radioresistant stromal/thymic architectural defects persist** after transplant ([PMID: 41280889](https://pubmed.ncbi.nlm.nih.gov/41280889/)).
- **Critical period:** Early diagnosis and transplant before cumulative infectious/organ damage is the key window of intervention.

### 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; only a handful of genetically confirmed cases worldwide. No reliable prevalence/incidence estimates exist.
- **Inheritance:** **Autosomal recessive**; requires biallelic LoF. Heterozygous carriers are unaffected (F001, F008).
- **Penetrance / expressivity:** Presumed complete penetrance with biallelic LoF; expressivity across the few cases includes the core lymphoid/infectious phenotype.
- **Anticipation / mosaicism:** Not applicable / not reported.
- **Founder effects / consanguinity:** No founder allele established; consanguinity is the expected context for recessive presentation. Carrier frequency is extremely low, consistent with strong gnomAD constraint (F008).
- **Demographics:** No ethnic predilection established; too few cases for sex-ratio or geographic analysis.

### 10. Diagnostics

**Diagnostic approach.** Because **no pathogenic *MAP3K14* variants are catalogued in ClinVar** (F007), diagnosis rests on a combination of **genetic sequencing + functional validation**:

- **Genetic testing:** **Whole-exome (WES)** or **whole-genome sequencing (WGS)** is the practical route to identify biallelic *MAP3K14* variants, often via GeneMatcher-style collaboration given rarity. Targeted single-gene or **inborn-errors-of-immunity (IEI) gene panels** that include *MAP3K14* are appropriate. CMA/karyotyping/FISH are not primary tools (no chromosomal mechanism).
- **Functional confirmation (essential):** Assays of **NIK kinase activity** and **p100→p52 processing** in patient cells/transfected constructs — the strategy used in the index report ([PMID: 25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/)).
- **Immunophenotyping (laboratory):** Flow cytometry showing B-cell lymphopenia, reduced class-switched memory B cells, reduced/defective NK cells, and perturbed memory/Tfh T cells; **serum immunoglobulins** showing hypogammaglobulinemia.
- **Autoantibody screen:** Test for **neutralizing anti–type I IFN autoantibodies** (shared family feature; F005).
- **Infectious work-up:** Stool microscopy/antigen for *Cryptosporidium*; CMV viral load; imaging (MRCP) if cholangitis suspected.

**Differential diagnosis:** Other combined immunodeficiencies and CVID-spectrum disorders, especially the related non-canonical NF-κB IEIs (*NFKB2*, *RELB*, *CHUK*/IKKα) and other causes of chronic *Cryptosporidium* infection (e.g., CD40L deficiency, IL-21R deficiency [PMID: 33966600](https://pubmed.ncbi.nlm.nih.gov/33966600/), DOCK8 deficiency [PMID: 41695074](https://pubmed.ncbi.nlm.nih.gov/41695074/)). Distinguishing feature: combined B/T/NK defect with absent secondary lymphoid organs and NIK functional defect.

**Screening:** Not part of standard newborn screening (which detects T-cell lymphopenia via TRECs; NIK deficiency may be TREC-variable). **Cascade/carrier testing** in affected families is appropriate once the variant is known.

### 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics (ultra-rare). Prognosis without immune reconstitution is guarded due to recurrent/opportunistic infections and organ complications (e.g., sclerosing cholangitis).
- **Morbidity:** Substantial — chronic infections, chronic diarrhea/malnutrition, hepatobiliary disease.
- **Disease course / complications:** Progressive organ damage possible; CMV disease and *Cryptosporidium*-associated cholangitis are major threats.
- **Recovery potential:** **HSCT** can restore hematopoietic immunity (full donor chimerism and T-cell reconstitution reported) but **does not repair the stromal/thymic architectural defects** ([PMID: 41280889](https://pubmed.ncbi.nlm.nih.gov/41280889/)).
- **Prognostic factors:** Early diagnosis, pre-transplant infection/organ-damage burden, and post-transplant immune dysregulation (including anti-cytokine autoantibodies) shape outcome.

### 12. Treatment

- **Definitive therapy — allogeneic HSCT:** The principal curative-intent treatment for the hematopoietic immune defect. Both reported patients achieved full donor chimerism and early T-cell reconstitution, but the authors stress the **non-redundant, radioresistant role of non-canonical NF-κB in thymic reconstitution and secondary lymphoid organ development**, which HSCT does not restore ([PMID: 41280889](https://pubmed.ncbi.nlm.nih.gov/41280889/)). NCIT suggestion: **Hematopoietic Stem Cell Transplantation (NCIT:C15431)**; Allogeneic Bone Marrow Transplantation (NCIT:C15335).
- **Supportive pharmacotherapy:** **Immunoglobulin replacement therapy** (IVIG/SCIG) for hypogammaglobulinemia (NCIT:C584 Immunoglobulin Therapy); **antimicrobial prophylaxis** against bacterial/viral/opportunistic pathogens; targeted treatment of *Cryptosporidium* (e.g., nitazoxanide) and CMV (e.g., ganciclovir/valganciclovir).
- **Monitoring/adjunct:** Long-term immunologic monitoring, including surveillance for immune dysregulation and **anti-cytokine autoantibodies**; the follow-up study suggests future consideration of **thymic regeneration or targeted immune modulation** to address architectural defects ([PMID: 41280889](https://pubmed.ncbi.nlm.nih.gov/41280889/)).
- **Gene/cell/RNA therapy:** No approved gene therapy; *MAP3K14* is a conceptual candidate for gene correction given the recessive LoF mechanism, but none exists clinically.
- **Pharmacogenomics / NIK inhibitors:** NIK *inhibitors* (e.g., Cpd33; [PMID: 32169603](https://pubmed.ncbi.nlm.nih.gov/32169603/)) are relevant to the **opposite (gain-of-function) pole** of the axis (cancer, bone loss, inflammation) and are **contraindicated** in NIK deficiency.

### 13. Prevention

- **Primary prevention:** Not preventable at the level of the mutation; **genetic counseling** for consanguineous/affected families and **reproductive options** (preimplantation/prenatal testing once the variant is known).
- **Secondary prevention:** Early molecular diagnosis enabling pre-emptive antimicrobial prophylaxis, IgG replacement, and timely HSCT.
- **Tertiary prevention:** Infection prophylaxis, nutritional support, and surveillance/management of hepatobiliary disease and anti-cytokine autoantibodies to prevent complications.
- **Immunization:** **Live vaccines are contraindicated**; inactivated vaccines may give blunted responses due to antibody-production defects.
- **Counseling:** Genetic counseling with cascade carrier testing is central.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *MAP3K14* (NCBI Gene 9020); mouse ortholog *Map3k14* / *Nik* (NCBI Gene 53859; *Mus musculus*, NCBI Taxon 10090).
- **Natural animal disease:** The **alymphoplasia (*aly/aly*) mouse** is a spontaneous natural *Nik* loss-of-function point mutant — the prototypical animal model (F003). No companion-animal (OMIA) natural disease is established.
- **Comparative biology / conservation:** The NIK→IKKα→p100/p52 non-canonical NF-κB axis and its role in lymphoid organogenesis, B-cell maturation, and osteoclast differentiation are conserved across mammals ([PMID: 30894749](https://pubmed.ncbi.nlm.nih.gov/30894749/)), underpinning the strong translational value of mouse models.
- **Zoonosis:** Not applicable.

### 15. Model Organisms

| Model | Type | Genetic basis | Phenotype recapitulation | Reference |
|---|---|---|---|---|
| *aly/aly* mouse | Mammalian, spontaneous | *Nik/Map3k14* LoF point mutation | Absent LN/Peyer's patches, disrupted lymphoid architecture, impaired B-cell/Ig production | [PMID: 42175627](https://pubmed.ncbi.nlm.nih.gov/42175627/) |
| Germline NIK KO | Mammalian, knockout | Full *Nik* deletion/inactivation | Defective B-cell development and secondary lymphoid organs | [PMID: 26116508](https://pubmed.ncbi.nlm.nih.gov/26116508/) |
| Conditional/adult NIK deletion | Mammalian, conditional | Inducible/tissue-specific | Reduced mature B cells and germinal-center B cells; abrogated BAFF responses | [PMID: 26116508](https://pubmed.ncbi.nlm.nih.gov/26116508/) |
| T-cell–conditional NIK KO | Mammalian, conditional | T-cell-specific *Nik* deletion | Reduced effector/memory T cells; impaired infection response; EAE-resistant | [PMID: 26912039](https://pubmed.ncbi.nlm.nih.gov/26912039/) |
| aly/aly thymic epithelium | Mammalian | *Nik* LoF | Abnormal cortical/medullary TEC development | [PMID: 32145062](https://pubmed.ncbi.nlm.nih.gov/32145062/) |

**Recapitulation & limitations.** Mouse models faithfully reproduce the **B-cell, secondary-lymphoid-organ, and thymic-architectural** features of human disease and were instrumental in defining the pathway. Limitations: murine models may not capture the human **anti–type I IFN autoantibody** predisposition or the full **NK-cell/*Cryptosporidium*** susceptibility, and species differences in immune architecture mean phenotype severity does not map 1:1. Resources: MGI (mouse), with aly/aly as the canonical strain.

---

## Mechanistic Model / Interpretation

```
  Biallelic MAP3K14 LoF mutation
            │  (kinase-dead NIK; functionally confirmed)
            ▼
  TNFRSF ligation (BAFFR/CD40/LTβR/RANK/Fn14)
  normally stabilizes NIK via TRAF3 degradation
            │  ── but kinase-dead NIK cannot act ──
            ▼
  NIK fails to phosphorylate IKKα
            ▼
  IKKα fails to phosphorylate p100 (NFKB2)
            ▼
  p100 NOT processed to p52  ──►  no nuclear RelB/p52
            │                         │
            │                         └── (also: impaired sustained canonical NF-κB)
            ▼
  ┌─────────┬─────────┬─────────┬─────────┬─────────────┐
  ▼         ▼         ▼         ▼         ▼             ▼
Stroma/   B cells   T cells   NK cells  Tolerance    Combined
TEC                                     (inferred)   two-pathway
  │         │         │         │         │           defect
absent LN/ B-lympho- impaired  defective anti-IFN-α
Peyer's,   penia,    effector/ NK +      autoAb
disrupted  low memory memory,  impaired  predisposition
thymus     B, hypo-  Tfh dys-  synapse
           gammaglob function
  └─────────┴─────────┴─────────┴─────────┴─────────────┘
                        ▼
   Recurrent bacterial, viral (CMV), and Cryptosporidium
   infections; chronic diarrhea; sclerosing cholangitis
```

**The bidirectional dosage axis** (F006) frames NIK deficiency as one pole of a continuum:

| NIK activity | Consequence | Example conditions |
|---|---|---|
| **Loss (this disease)** | Immunodeficiency | NIK deficiency; aly/aly mouse |
| **Normal** | Balanced lymphoid development & immunity | — |
| **Overactive** | Autoimmunity, cancer, fibrosis, bone loss, metabolic disease | Myeloma, RA synovium, osteoporosis, neointimal hyperplasia |

This dosage logic explains the paradox of a recessive disease in a highly LoF-constrained gene (F008): evolution selects against *both* loss and excess, favoring tight control.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [25406581](https://pubmed.ncbi.nlm.nih.gov/25406581/) | *Biallelic LoF mutation in NIK causes PID* | Human clinical + in vitro | **Defining paper** — causal gene, inheritance, core defect (F001) |
| [11520989](https://pubmed.ncbi.nlm.nih.gov/11520989/) | *Activation by IKKα of second NF-κB pathway* | In vitro / mouse | NIK→IKKα→p100/p52 hierarchy (F002) |
| [26116508](https://pubmed.ncbi.nlm.nih.gov/26116508/) | *Conditional NIK deletion disrupts B cells* | Mouse | B-cell/lymphoid organ recapitulation (F003) |
| [42175627](https://pubmed.ncbi.nlm.nih.gov/42175627/) | *Adipocyte NIK depletion...* (states aly/aly phenotype) | Mouse | Lymphoid architecture summary (F003) |
| [32145062](https://pubmed.ncbi.nlm.nih.gov/32145062/) | *NIK in cortical thymic epithelial cells* | Mouse | Thymic epithelial defect (F003) |
| [26912039](https://pubmed.ncbi.nlm.nih.gov/26912039/) | *Cell-intrinsic NIK in T cells* | Mouse | T-cell effector/memory defect (F003) |
| [22921830](https://pubmed.ncbi.nlm.nih.gov/22921830/) | *Crystal structure of NIK catalytic domain* | Structural/in vitro | Active-like, abundance-regulated kinase (F004) |
| [23374866](https://pubmed.ncbi.nlm.nih.gov/23374866/) | *NIK inhibitor design, co-crystals* | Structural/in vitro | Druggable pocket (F004) |
| [39812688](https://pubmed.ncbi.nlm.nih.gov/39812688/) | *IKKα kinase-domain mutations* | Human clinical | Anti-IFN-α autoAb in family (F005) |
| [42261849](https://pubmed.ncbi.nlm.nih.gov/42261849/) | *Inborn errors in NF-κB pathway (RELB)* | Human clinical | Family-shared T/B defect + anti-IFN (F005) |
| [41280889](https://pubmed.ncbi.nlm.nih.gov/41280889/) | *Long-term HSCT outcome in NIK deficiency* | Human clinical | Treatment; architectural limits; autoAb monitoring |
| [30926358](https://pubmed.ncbi.nlm.nih.gov/30926358/) | *NIK as druggable mediator of tissue injury* | Review | Bidirectional dosage axis (F006) |
| [30894749](https://pubmed.ncbi.nlm.nih.gov/30894749/) | *NIK-SIX axis / non-canonical NF-κB* | Review/mechanism | Core physiological functions lost (F006) |
| [30837284](https://pubmed.ncbi.nlm.nih.gov/30837284/) | *NIK-IKK in endothelium* | In vitro | NIK's canonical-pathway role (F006) |
| [32350909](https://pubmed.ncbi.nlm.nih.gov/32350909/) | *Non-canonical NF-κB in myeloma* | Human (cancer) | TRAF3-low/NIK-high readout (F002) |
| [40229245](https://pubmed.ncbi.nlm.nih.gov/40229245/) | *TRAF2 in inflammation/cancer* | Review | TRAF2–NIK regulation; NK cytotoxicity (F006) |

Supporting/context papers (gain-of-function pole, differentials): [PMID: 32169603](https://pubmed.ncbi.nlm.nih.gov/32169603/) (NIK inhibitor, bone), [PMID: 42350366](https://pubmed.ncbi.nlm.nih.gov/42350366/) (CRC S100A14/MAP3K14), [PMID: 33966600](https://pubmed.ncbi.nlm.nih.gov/33966600/) (IL-21R differential), [PMID: 41695074](https://pubmed.ncbi.nlm.nih.gov/41695074/) (DOCK8 differential), [PMID: 31709944](https://pubmed.ncbi.nlm.nih.gov/31709944/) (Cryptosporidium context).

---

## Limitations and Knowledge Gaps

1. **Extremely few human cases.** Essentially all human clinical knowledge derives from a single index family (Willmann 2014) plus a long-term HSCT follow-up of two patients (2025). Frequencies, penetrance, expressivity, survival, and QoL statistics cannot be reliably quantified.
2. **No pathogenic variants in ClinVar.** Diagnosis cannot rely on variant-database pathogenicity and requires functional kinase assays (F007), limiting routine clinical recognition.
3. **Anti–type I IFN autoantibody link is inferred for NIK specifically.** The predisposition is well-documented for *CHUK*/IKKα and *RELB* and is monitored in NIK patients, but direct, quantified human NIK-deficiency autoantibody data remain limited (F005).
4. **Mouse–human divergence.** Murine models capture lymphoid-architecture and B/T defects but may not fully model NK/*Cryptosporidium* susceptibility or autoantibody tolerance breakdown (F003).
5. **No disease-specific OMIM number, ICD code, prevalence, or registry.**
6. **No modifier genes, epigenetic marks, or population-specific founder alleles identified.**

---

## Proposed Follow-up Experiments / Actions

1. **Deposit functionally validated pathogenic *MAP3K14* variants in ClinVar/ClinGen** with ACMG/AMP evidence codes (PS3 functional) to enable future molecular diagnosis.
2. **International case aggregation** via GeneMatcher/IEI consortia to assemble a cohort large enough to estimate penetrance, phenotype spectrum, and survival.
3. **Systematic anti–type I IFN autoantibody screening** in all genetically confirmed NIK-deficiency patients to quantify the predisposition and its clinical impact (infection severity).
4. **Standardized functional diagnostic assay** (NIK kinase activity / p100→p52 processing in patient PBMCs or transfected constructs) validated for clinical laboratory use.
5. **Pre-clinical gene-correction / thymic-regeneration studies** in aly/aly mice to address the HSCT-refractory stromal/thymic architectural defect highlighted by the long-term follow-up ([PMID: 41280889](https://pubmed.ncbi.nlm.nih.gov/41280889/)).
6. **Single-cell transcriptomic profiling** of patient lymphoid tissue/HSCT grafts to map the stromal vs hematopoietic contributions to residual immune dysfunction.
7. **Natural-history / registry study** (Orphanet-linked) to generate epidemiology, prognosis, and QoL data currently absent.

---

*Report compiled from 8 confirmed findings and 34 reviewed papers over 5 completed investigation iterations. Evidence levels (human clinical / model organism / in vitro / computational) are flagged per finding. NIK deficiency is caused by biallelic loss-of-function mutations in **MAP3K14** encoding **NF-κB–inducing kinase (NIK)**.*


## Artifacts

- [OpenScientist final report](NIK_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](NIK_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 15 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018642` (2 mentions) - the report calls it "MONDO"; MONDO calls it **NIK deficiency**
- `HP:0002718` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent bacterial infections**
- `HP:0004429` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent viral infections**
- `HP:0100792` (1 mention) - the report calls it "Clinical/laboratory"; HP calls it **Acantholysis**
- `HP:0010976` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Decreased total B cell count**
- `HP:0002720` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Decreased circulating IgA concentration**
- `HP:0005404` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Increased total B cell count**
- `HP:0040218` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Reduced total natural killer cell count**
- `HP:0005415` (1 mention) - the report calls it "abnormal T-cell count"; HP calls it **Decreased total CD8+ T cell proportion**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0004704` (obsolete NF-kappaB-inducing kinase activity) (1 mention)
- `GO:0051092` (obsolete positive regulation of NF-kappaB transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001211` (1 mention) - the report calls it "Peyer's patches / gut-associated lymphoid tissue"; UBERON calls it **Peyer's patch**, and lists "aggregated lymphoid nodule" among its other names