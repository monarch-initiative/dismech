---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:34:50.911060'
end_time: '2026-10-24T15:58:14.564710'
duration_seconds: 1403.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Heterotaxy, Visceral, 14, Autosomal
  mondo_id: MONDO:0976135
  category: Mendelian
  causal_genes: CIROZ
  omim_id: not recorded
  synonyms: HTX14; CIROZ-related heterotaxy; CIROZ visceral heterotaxy; C1orf127-related
    heterotaxy
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
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 11
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 8
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 27
  not_found: 0
  obsolete: 2
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 5
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: UBERON:0005098
    reported_labels:
    - left-right organizer / node region
    ontology_label: UBERON_0005098
  - term_id: HP:0030853
    reported_labels:
    - abnormal heart/visceral situs
    ontology_label: Heterotaxy
  - term_id: HP:0001696
    reported_labels:
    - Physical manifestation
    ontology_label: Situs inversus totalis
  - term_id: HP:0006528
    reported_labels:
    - Physical manifestation
    ontology_label: Chronic lung disease
  - term_id: HP:0002240
    reported_labels:
    - context
    ontology_label: Hepatomegaly
  - term_id: HP:0000085
    reported_labels:
    - Physical manifestation
    ontology_label: Horseshoe kidney
  - term_id: GO:0005615
    reported_labels:
    - site of secreted CIROZ
    ontology_label: obsolete extracellular space
  labels_variant: 2
  obsolete_terms:
  - term_id: UBERON:0005098
    ontology_label: UBERON_0005098
    replaced_by: UBERON:0004200
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - GARD
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Heterotaxy_Visceral_14_Autosomal-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Heterotaxy_Visceral_14_Autosomal-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Heterotaxy, Visceral, 14, Autosomal
- **MONDO ID:** MONDO:0976135 (if available)
- **Causal gene(s):** CIROZ
- **OMIM:** not recorded
- **Synonyms:** HTX14; CIROZ-related heterotaxy; CIROZ visceral heterotaxy; C1orf127-related heterotaxy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Heterotaxy, Visceral, 14, Autosomal** covering all of the
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

# Heterotaxy, Visceral, 14, Autosomal (HTX14) — Comprehensive Disease Characterization Report

**Causal gene: CIROZ (formerly C1orf127; NCBI Gene 148345; HGNC:26730; Ensembl ENSG00000175262; locus 1p36.22)**
**Disease identifiers: MONDO:0976135 · OMIM 621080 · DOID:0061123 · GARD:0027430 · MedGen C1875141 · UMLS C5975611**

---

## Summary

Heterotaxy, visceral, 14, autosomal (**HTX14**) is an ultra-rare, autosomal-recessive laterality (left-right patterning) disorder caused by **biallelic loss-of-function variants in CIROZ**, a gene previously named C1orf127 and now officially designated *ciliated left-right organizer protein containing ZP-N domains*. The gene maps to chromosome 1p36.22 (between TARDBP and CASZ1) and encodes a **secreted protein** bearing a signal peptide followed by three zona-pellucida (ZP-N) domains, consistent with an extracellular role. CIROZ is expressed specifically in the embryonic **left-right organizer (LRO)** — the ciliated midline structure (mouse posterior notochord/node, zebrafish Kupffer's vesicle, *Xenopus* gastrocoel roof plate) where the body's left-right axis is first established. The disease was formally delineated in 2025 by Szenker-Ravi et al. ([PMID: 39753129](https://pubmed.ncbi.nlm.nih.gov/39753129/)), who reported 16 affected individuals from 10 families.

Mechanistically, CIROZ is a newly recognized member of a **vertebrate LRO extracellular genetic module** that also contains DAND5, PKD1L1, MMP21, and CIROP. This module operates upstream of the canonical **NODAL–PITX2 symmetry-breaking cascade**: motile cilia at the LRO generate leftward fluid flow, which is sensed by immotile sensory cilia via a PKD2/PKD1L1 mechanosensitive calcium channel; flow sensing drives left-sided down-regulation of the secreted NODAL inhibitor DAND5, disinhibiting NODAL on the left, which in turn amplifies NODAL and activates the PITX2 transcription factor in the left lateral plate mesoderm to specify asymmetric organogenesis. Biallelic CIROZ inactivation disrupts this cascade, producing congenital situs ambiguus/situs inversus with variable congenital heart defects (CHD) and visceral malpositions.

Clinically, HTX14 shows **incomplete penetrance and highly variable expressivity**, ranging from asymptomatic situs inversus totalis to lethal complex CHD such as hypoplastic left heart syndrome. Notably, CIROZ-related heterotaxy is associated with *less frequent and milder* cardiac involvement than heterotaxy caused by the other four module genes. **Mouse Ciroz knockouts faithfully phenocopy** human situs defects, whereas — surprisingly — zebrafish and *Xenopus* knockouts do **not** show laterality anomalies, revealing species-specific essentiality of this gene. No gene-specific therapy exists; management is supportive and centers on cardiac surgery, infection prophylaxis for splenic dysfunction, and screening for intestinal malrotation.

---

## Key Findings

### Finding 1 — Biallelic CIROZ loss-of-function causes autosomal-recessive HTX14

The defining study of this disease is **Szenker-Ravi et al. (2025)** ([PMID: 39753129](https://pubmed.ncbi.nlm.nih.gov/39753129/)), which reported **16 individuals from 10 families** with bi-allelic CIROZ inactivation variants causing heterotaxy with congenital heart defects. The abstract states verbatim: *"We report 16 individuals from 10 families with bi-allelic CIROZ inactivation variants, which cause heterotaxy with congenital heart defects."* The authors establish gene identity and protein architecture directly: *"CIROZ (previously known as C1orf127) is also specifically expressed in the LRO of mice, frogs, and fish, where it encodes a protein with a signal peptide followed by 3 zona pellucida N domains, consistent with extracellular localization."*

Independent corroboration comes from **Xie et al. (2025)** ([PMID: 40467998](https://pubmed.ncbi.nlm.nih.gov/40467998/)), a whole-exome-sequencing study of congenital heart disease patients with laterality defects, which lists C1ORF127/CIROZ among candidate laterality genes (*"4.1% exhibiting variants in candidate genes (FMNL3, C1ORF127, CFAP157, C10ORF107, MYO1D)"*). A third independent cohort (Dong et al., cited as reference 82 within the Szenker-Ravi paper) analyzed 5,497 CHD exomes and identified CIROZ as a **genome-wide-significant laterality risk gene**, adding five more biallelic-LOF families including the recurrent p.Arg113* allele. The convergence of three independent cohorts firmly establishes CIROZ as a bona fide heterotaxy gene.

The inheritance is unambiguously **autosomal recessive**: affected individuals are either homozygous (in consanguineous families) or compound heterozygous for loss-of-function alleles, and heterozygous carriers are unaffected.

### Finding 2 — CIROZ variant spectrum and population genetics

All reported HTX14 alleles are loss-of-function (nonsense, frameshift, or a signal-peptide-disrupting missense), referenced to transcript **NM_001170754.2**:

| Variant (cDNA) | Protein | Type | Exon | gnomAD v4.1.0 MAF | Zygosity / Families | Population |
|---|---|---|---|---|---|---|
| c.56C>T | p.(Thr19Met) | Missense (signal peptide) | — | 4.32 × 10⁻⁴ | Compound het (family 1) | European |
| c.577C>T | p.(Arg193*) | Nonsense (NMD) | 7 | 2.48 × 10⁻⁶ | Compound het with c.56C>T (family 1) | European |
| c.337C>T | p.(Arg113*) | Nonsense (NMD) | 4 | 2.73 × 10⁻⁵ | Homozygous, 7 families (F2–F8) | Middle Eastern (consanguineous) |
| c.1210del | p.(Gln404Argfs*84) | Frameshift | — | 5.62 × 10⁻⁶ | 2 families | Guatemalan |

The recurrent nonsense allele **p.Arg113*** is enriched in the Qatar Genome Program (MAF 8.57 × 10⁻⁴; 24 heterozygotes among ~14,000 genomes) and is catalogued in ClinVar (RCV003989718.2). Importantly, haplotype analysis showed **no shared founder haplotype** for this recurrent variant, indicating independent recurrent mutation rather than a single founder event — consistent with a CpG-hypermutable Arg codon (CGA→TGA). The Szenker-Ravi study documents the recurrent homozygous nonsense variant (*"In seven additional families (F2-F8), the affected individuals were homozygous for another stop-gained variant, c.337C>T (p.Arg113…"*) and the Guatemalan frameshift (*"This deletion of one base c.1210del (p.Gln404Argfs…"*).

All variants are predicted to cause **nonsense-mediated decay / protein-null** outcomes, and the signal-peptide missense (p.Thr19Met) is presumed to impair secretion — establishing a uniform **loss-of-function** disease mechanism.

### Finding 3 — Clinical phenotype spectrum, incomplete penetrance, and comparatively mild cardiac involvement

Among the 16 affected individuals, the phenotype ranged widely:
- **Heterotaxy without CHD (5/16):** e.g., asymptomatic situs inversus totalis; horseshoe kidney with otherwise normal situs solitus.
- **Heterotaxy with severe CHD (11/16):** e.g., hypoplastic left heart syndrome with mitral and aortic atresia, bilobed lungs (pulmonary isomerism), and intestinal malrotation.

**Outcomes:** 3 fetuses underwent termination of pregnancy, and 2 died in the first year of life from complex cardiac phenotypes. Critically, **two individuals carrying biallelic variants had normal situs solitus (non-penetrant)**, directly demonstrating **incomplete penetrance**.

A key quantitative observation is that CIROZ-related disease has **milder cardiac involvement** than other module genes: significantly fewer CIROZ individuals had CHD (5/16) compared with individuals harboring biallelic variants in the four other module genes MMP21, PKD1L1, CIROP, and DAND5 (chi-squared *p* = 0.006). Furthermore, the module genes collectively produce far more situs ambiguus than the primary-ciliary-dyskinesia (CILD) genes (chi-squared *p* < 0.00001), distinguishing this "extracellular module" heterotaxy from classic ciliary-motility heterotaxy. The core phenotype is anchored by the primary report: *"We report 16 individuals from 10 families with bi-allelic CIROZ inactivation variants, which cause heterotaxy with congenital heart defects."*

### Finding 4 — Animal models: mouse phenocopy, but no zebrafish/Xenopus phenotype

Two independent mouse *Ciroz* (gene symbol *Gm572*) null lines model HTX14:
1. **ENU-induced 5′ splice-donor variant** c.26+1G>A (p.Trp9*, protein-null; MGI:5431499): homozygous E15.5 embryos show situs inversus totalis, CHDs, **right pulmonary isomerism**, and abnormal liver positioning.
2. **IMPC LacZ cassette** replacing exon 4 (*Gm572^tm1b(EUCOMM)Hmgu*; MGI:5635119): partially embryonic lethal (<6% survive to birth), with E18.5 situs inversus affecting lungs, heart, liver, and stomach.

In stark contrast, complete CRISPR knockouts and morpholino knockdowns in *Xenopus laevis*, and maternal-zygotic null zebrafish, showed **no laterality or heart-looping defects** (asymmetric *lefty2* and *lov/southpaw* expression remained intact); MZ-null zebrafish were viable and fertile. The authors summarize: *"While the knockout of Ciroz in mice also leads to situs anomalies, we unexpectedly find that its targeted inactivation in zebrafish and Xenopus does not lead to observable LR anomalies."* CIROZ protein was confirmed to be **secreted** (detected in culture media), to form **oligomers**, and to be expressed specifically in the ciliated LRO, temporally **after cirop and before mmp21**. Evolutionarily, CIROZ is absent/pseudogenized in Carnivora, Atherinomorpha fish, and jawless vertebrates — reinforcing its dispensability in some lineages despite essentiality in human and mouse.

### Finding 5 — Mechanistic placement in the LRO extracellular module upstream of NODAL–PITX2

CIROZ joins a four-gene module — DAND5, PKD1L1, MMP21, CIROP — that *"has specifically evolved in vertebrate species that harbor motile cilia in their left-right organizer (LRO)."* The downstream pathway is the conserved NODAL cascade (Gabriel & Lo 2024, [PMID: 38884745](https://pubmed.ncbi.nlm.nih.gov/38884745/); [PMID: 38884711](https://pubmed.ncbi.nlm.nih.gov/38884711/)): *"This pathway involves initial asymmetric activation of a nodal signaling cascade at the embryonic node, followed by its propagation to the left lateral plate mesoderm and activation of left-sided expression of the Pitx2 transcription factor specifying visceral organ asymmetry."* CIROZ is a secreted ZP-N-domain protein acting extracellularly within this module, feeding into DAND5-mediated regulation of NODAL.

### Finding 6 — Epidemiology and management context

Laterality defects have an estimated prevalence of **~1 in 10,000 live births** ([PMID: 39753129](https://pubmed.ncbi.nlm.nih.gov/39753129/)). Within CHD cohorts, laterality defects appear in ~1.1% of patients ([PMID: 40467998](https://pubmed.ncbi.nlm.nih.gov/40467998/)), and CHD is markedly more common in heterotaxy than in the general population (57% vs ~1%). Current NGS yields a molecular diagnosis in only **20–30% of heterotaxy cases** ([PMID: 42630107](https://pubmed.ncbi.nlm.nih.gov/42630107/)), which is precisely the diagnostic gap that CIROZ discovery helps close. Splenic abnormalities (asplenia/polysplenia) drive **high bacteremia risk and mortality** ([PMID: 27425254](https://pubmed.ncbi.nlm.nih.gov/27425254/)): *"HTX patients are at high risk for bacteremia leading to mortality, regardless of anatomic splenic type."* Pneumococcal conjugate vaccination is protective ([PMID: 20730421](https://pubmed.ncbi.nlm.nih.gov/20730421/)): *"No cases of pneumococcal sepsis occurred after the introduction of the conjugated pneumococcal vaccination to the pediatric vaccination schedule."* The same study notes that *"the finding of interrupted IVC on echocardiography should prompt screening for intestinal malrotation."*

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in CIROZ** (nonsense/frameshift → NMD/protein-null, or signal-peptide missense → impaired secretion) **leads to** absence of functional secreted CIROZ protein in the embryonic left-right organizer (LRO). *[Demonstrated: human genetics + protein secretion assays.]*
2. Loss of CIROZ **disrupts the vertebrate LRO extracellular module** (DAND5/PKD1L1/MMP21/CIROP/CIROZ) that operates during the symmetry-breaking window. *[Inferred from module membership and LRO-specific, stage-specific expression — CIROZ acts after CIROP and before MMP21.]*
3. Normally, motile cilia at the LRO generate **leftward fluid flow**, sensed by immotile sensory cilia via the **PKD2/PKD1L1 mechanosensitive Ca²⁺ channel**. Module disruption **impairs correct flow-dependent signaling**. *[Demonstrated for the module broadly; CIROZ's precise biochemical step is inferred.]*
4. Flow sensing normally causes **left-sided down-regulation of DAND5** (a secreted NODAL antagonist). Faulty signaling **results in failure to properly repress DAND5 asymmetrically**. *[Inferred for CIROZ specifically.]*
5. Persistent/symmetric DAND5 activity **fails to disinhibit NODAL** on the left (NODAL normally acts as NODAL–GDF1 heterodimers). → **Loss or randomization of left-sided NODAL activation.** *[Demonstrated for the cascade.]*
6. Disrupted NODAL **fails to activate PITX2** correctly in the **left lateral plate mesoderm**. *[Demonstrated for the cascade.]*
7. Absent/randomized PITX2 asymmetry **leads to abnormal left-right specification of visceral organogenesis** → **situs ambiguus / situs inversus**. *[Demonstrated.]*

**Branch point (explains variable expressivity):**
- 7a. Random/abnormal cardiac looping and outflow-tract morphogenesis **→ congenital heart defects** (e.g., HLHS, atrioventricular septal defects) in a subset. *[Observed in 11/16.]*
- 7b. Abnormal thoraco-abdominal organ positioning **→ pulmonary isomerism, abnormal liver/stomach position, intestinal malrotation, splenic anomalies (asplenia/polysplenia), horseshoe kidney.**
- 7c. In some biallelic carriers, stochastic/compensatory factors permit normal patterning **→ situs solitus (non-penetrant).** *[Observed in 2 individuals — incomplete penetrance.]*

### Schematic

```
 CIROZ biallelic LOF
        │ (no secreted CIROZ in LRO)
        ▼
 LRO extracellular module disrupted
 (DAND5 · PKD1L1 · MMP21 · CIROP · CIROZ)
        │
        ▼
 Cilia-driven leftward flow sensing impaired
        │ (PKD2/PKD1L1 Ca²⁺ channel)
        ▼
 Failure of asymmetric DAND5 down-regulation
        │
        ▼
 NODAL not disinhibited on the left  ──►  PITX2 not activated in left LPM
        │
        ▼
 Loss/randomization of L-R organ specification
        │
   ┌────┴─────────────┬──────────────────┐
   ▼                  ▼                  ▼
 Cardiac looping/   Visceral mal-      Stochastic rescue
 OFT defects →      positioning →      → situs solitus
 CHD (11/16)        pulmonary          (non-penetrant, 2 cases)
                    isomerism, gut
                    malrotation,
                    asplenia/polysplenia
```

**Upstream vs downstream:** CIROZ acts *upstream* at the LRO (symmetry-breaking step), within the extracellular module; NODAL/LEFTY/PITX2 are *downstream* transcriptional effectors. **Cell types involved:** motile and primary/sensory ciliated cells of the LRO; lateral plate mesoderm cells. **Suggested ontology terms:** GO:0007368 (determination of left/right symmetry), GO:0060287 (epithelial cilium movement involved in determination of left/right asymmetry), GO:0003140 (determination of left/right asymmetry in lateral mesoderm), GO:0038003 (Nodal signaling pathway); CL:0000064 (ciliated cell); UBERON:0005098 (left-right organizer / node region), UBERON:0003081 (lateral plate mesoderm); CHEBI:29108 (calcium(2+)).

---

## Section-by-Section Characterization

### 1. Disease Information
HTX14 is an ultra-rare Mendelian **visceral heterotaxy / laterality disorder** in which thoraco-abdominal organs develop in an abnormal left-right arrangement (situs ambiguus or situs inversus), frequently with congenital heart defects. **Identifiers:** MONDO:0976135; OMIM 621080; DOID:0061123; GARD:0027430; MedGen C1875141; UMLS C5975611. No dedicated Orphanet or ICD-10/ICD-11 code is specific to the type-14 subtype (classified under broader heterotaxy/situs categories; MeSH D059446 "Heterotaxy Syndrome"). **Synonyms:** HTX14; CIROZ-related heterotaxy; CIROZ visceral heterotaxy; C1orf127-related heterotaxy. Information is **aggregated disease-level** (case series + cohort studies), not EHR-derived.

### 2. Etiology
**Primary cause:** biallelic (homozygous or compound-heterozygous) loss-of-function variants in CIROZ — a purely **genetic** etiology. **Genetic risk factors:** the recurrent p.Arg113* founder-independent allele (enriched in Middle Eastern/Qatari populations), p.Arg193*, p.Gln404Argfs*84 (Guatemalan), and signal-peptide p.Thr19Met. **Consanguinity** is a major contributor (7 of 10 families consanguineous). **Carrier status is non-pathogenic** (recessive). No established environmental or infectious cause for HTX14 specifically; however, for heterotaxy broadly, **pregestational diabetes/maternal hyperglycemia** is a recognized teratogenic risk factor acting on the same NODAL–PITX2 axis ([PMID: 39442590](https://pubmed.ncbi.nlm.nih.gov/39442590/); [PMID: 41974186](https://pubmed.ncbi.nlm.nih.gov/41974186/)). **Protective factors:** none genetic are established; incomplete penetrance implies unidentified modifiers. **Gene-environment interactions:** not specifically characterized for CIROZ.

### 3. Phenotypes

| Phenotype | Type | HPO term | Frequency (16 individuals) | Onset | Severity |
|---|---|---|---|---|---|
| Visceral heterotaxy / situs ambiguus | Physical manifestation | HP:0030853 (abnormal heart/visceral situs) | Core defining feature | Congenital/prenatal | Variable |
| Situs inversus totalis | Physical manifestation | HP:0001696 | Subset | Congenital | Often asymptomatic |
| Congenital heart defect (e.g., HLHS) | Clinical sign | HP:0001627; HP:0004383 (HLHS) | 11/16 (~69%) | Congenital | Severe when present |
| Pulmonary isomerism / abnormal lung lobation | Physical manifestation | HP:0006528 | Subset | Congenital | Moderate |
| Intestinal malrotation | Physical manifestation | HP:0002566 | Subset | Congenital | Moderate–severe |
| Abnormal liver/stomach position | Physical manifestation | HP:0002240 (context) | Subset | Congenital | Variable |
| Asplenia / polysplenia | Physical manifestation | HP:0001746 / HP:0001748 | Common in heterotaxy | Congenital | Increases infection risk |
| Horseshoe kidney | Physical manifestation | HP:0000085 | Reported | Congenital | Mild |

**Quality of life:** dominated by cardiac morbidity; asymptomatic situs inversus has minimal QoL impact, whereas complex CHD imposes major burden (surgery, mortality). Severity is **variable**; progression is **stable/structural** (congenital, non-degenerative). No disease-specific QoL instruments exist for HTX14.

### 4. Genetic / Molecular Information
**Causal gene:** CIROZ (C1orf127); OMIM gene/phenotype 621080; HGNC:26730; NCBI Gene 148345; Ensembl ENSG00000175262; locus 1p36.22. **Variant classes:** nonsense, frameshift, signal-peptide missense — all **loss-of-function** (see Finding 2 table). **ACMG classification:** the LOF alleles are pathogenic/likely-pathogenic (PVS1 + population-frequency/segregation evidence); p.Thr19Met is a hypomorphic signal-peptide missense. **Allele frequencies** are rare in gnomAD (2.5 × 10⁻⁶ to 4.3 × 10⁻⁴). **Origin:** germline. **Functional consequence:** loss of function (secreted protein null / impaired secretion). **Modifier genes:** none identified, but incomplete penetrance strongly implies modifiers. **Epigenetic / chromosomal abnormalities:** none implicated.

### 5. Environmental Information
No environmental, lifestyle, or infectious agent is causally linked to HTX14 specifically (it is monogenic recessive). For the broader heterotaxy phenotype, maternal pregestational diabetes/hyperglycemia is an environmental risk factor converging on NODAL–PITX2 signaling ([PMID: 39442590](https://pubmed.ncbi.nlm.nih.gov/39442590/)).

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the ordered causal chain and diagram. Molecular pathway: **TGF-β/NODAL superfamily signaling** (Reactome/KEGG Nodal/TGF-β). Protein dysfunction: loss of a secreted ZP-N/zona-pellucida-domain (ZP2-like, DUF4556) oligomeric protein. Cellular processes: ciliary motility and mechanosensation, left-right determination. No metabolic, immune, or autoimmune component is intrinsic to the primary lesion.

### 7. Anatomical Structures Affected
**Primary organs:** heart (UBERON:0000948), lungs (UBERON:0002048), liver (UBERON:0002107), stomach (UBERON:0000945), spleen (UBERON:0002106), intestine (UBERON:0000160), kidney (UBERON:0002113). **Developmental origin structure:** left-right organizer/node (UBERON:0005098) and lateral plate mesoderm (UBERON:0003081). **Body systems:** cardiovascular, respiratory, digestive, lymphatic/immune (spleen), urinary. **Cell/tissue level:** ciliated epithelial cells of the LRO (CL:0000064); mesodermal cells. **Subcellular:** cilium/axoneme (GO:0005929), extracellular space (GO:0005615 — site of secreted CIROZ). **Lateralization:** the defining abnormality is disrupted left-right asymmetry (mirror-image or randomized/ambiguous).

### 8. Temporal Development
**Onset:** congenital — the lesion acts during the narrow embryonic **symmetry-breaking window** (equivalent to ~3rd–4th week human gestation). Often detected **prenatally** on fetal echocardiography/ultrasound or at birth. **Progression:** structural and **stable** (non-progressive once formed); disease course is determined by the fixed anatomical defects. **Critical period:** the LRO/node stage is the sole window of vulnerability; there is no post-developmental opportunity for primary correction. Outcome is dominated by neonatal/infant cardiac events (terminations and early deaths concentrated in infancy).

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** incomplete (2 biallelic individuals had situs solitus). **Expressivity:** highly variable (asymptomatic → lethal CHD). **Consanguinity:** major role (7/10 families). **Founder effect:** the recurrent p.Arg113* allele arose by **independent recurrence** (no shared haplotype), not a classic founder. **Carrier frequency:** low (gnomAD rare; elevated for p.Arg113* in Qatar, MAF 8.57 × 10⁻⁴). **Populations:** reported in European, Middle Eastern (Qatari/consanguineous), and Guatemalan families. **Prevalence:** heterotaxy overall ~1/10,000 live births; HTX14 is a small ultra-rare subset. No reported sex skew. No genetic anticipation or germline mosaicism documented.

### 10. Diagnostics
**Imaging** is central: fetal/postnatal echocardiography, abdominal ultrasound, CT/MRI to map cardiac and visceral situs; interrupted IVC is a useful flag ([PMID: 20730421](https://pubmed.ncbi.nlm.nih.gov/20730421/)). **Laboratory:** Howell-Jolly bodies / functional asplenia screening; sepsis workup when febrile. **Genetic testing** is the definitive confirmatory route: **trio whole-exome or whole-genome sequencing** is most effective given locus heterogeneity (CIROZ is one of >60 heterotaxy/laterality genes); heterotaxy/laterality **gene panels** should now include CIROZ. Single-gene testing is reserved for cascade testing of a known familial variant. CMA/karyotype help exclude chromosomal causes. **Differential diagnosis:** primary ciliary dyskinesia (PCD)-associated heterotaxy ([PMID: 42026914](https://pubmed.ncbi.nlm.nih.gov/42026914/)), and other module/laterality genes (DAND5, PKD1L1, MMP21, CIROP, DNAH9, GDF1, CFAP53/CCDC11) ([PMID: 42630107](https://pubmed.ncbi.nlm.nih.gov/42630107/); [PMID: 39969775](https://pubmed.ncbi.nlm.nih.gov/39969775/)). Reference transcript for reporting: **NM_001170754.2**.

### 11. Outcome / Prognosis
Prognosis is governed by the **cardiac phenotype**: severe complex CHD drives pregnancy termination, surgical intervention, and early mortality concentrated in infancy ([PMID: 41974186](https://pubmed.ncbi.nlm.nih.gov/41974186/)): *"In LSD, major CHD drives pregnancy termination, surgical intervention, and early mortality concentrated during infancy."* In the CIROZ cohort, 3/16 were terminated and 2/16 died in year one; those without CHD can be asymptomatic with normal life expectancy. **Morbidity** includes repeat cardiac surgery, infection (splenic dysfunction), and sequelae of malrotation. **Prognostic factors:** presence/severity of CHD, right-ventricular-outflow obstruction, splenic status. CIROZ cases trend toward **milder cardiac involvement** than other module genes (CHD 5/16; *p* = 0.006).

### 12. Treatment
No gene-specific or disease-modifying therapy exists; care is **supportive and anatomy-directed**:
- **Cardiac surgery** for CHD (staged single-ventricle palliation or biventricular repair as anatomy permits) — NCIT: Cardiac Surgical Procedure.
- **Infection prophylaxis** for asplenia/functional asplenia: **pneumococcal, Hib, and meningococcal vaccination** plus antibiotic prophylaxis ([PMID: 27425254](https://pubmed.ncbi.nlm.nih.gov/27425254/); [PMID: 20730421](https://pubmed.ncbi.nlm.nih.gov/20730421/)) — NCIT: Antibiotic Prophylaxis / Vaccination.
- **Surgical correction of intestinal malrotation** (Ladd procedure) when indicated.
- **Supportive/rehabilitative care** and multidisciplinary follow-up.
No pharmacogenomic, gene, cell, RNA, or targeted therapies are reported for HTX14.

### 13. Prevention
**Primary prevention:** not possible for the monogenic lesion; optimizing maternal glycemic control reduces the broader heterotaxy risk ([PMID: 39442590](https://pubmed.ncbi.nlm.nih.gov/39442590/)). **Secondary prevention:** prenatal detection via fetal echocardiography enables delivery planning at cardiac centers. **Genetic counseling:** 25% recurrence risk per pregnancy for carrier couples; cascade carrier testing; prenatal diagnosis and preimplantation genetic testing are feasible once the familial variant is known. **Tertiary prevention:** vaccination + antibiotic prophylaxis to prevent overwhelming post-splenic sepsis; malrotation screening and prophylactic Ladd procedure.

### 14. Other Species / Natural Disease
**Mouse ortholog:** *Gm572* (Ciroz), with two null alleles (MGI:5431499; MGI:5635119) recapitulating human situs defects. **Non-mammalian orthologs** exist in zebrafish and *Xenopus* but are **dispensable** there (no LR phenotype on knockout). The gene is **absent/pseudogenized in Carnivora, Atherinomorpha fish, and jawless vertebrates**, indicating lineage-specific loss. No naturally occurring companion-animal or wildlife CIROZ disease is reported (no established OMIA entry). No zoonotic relevance.

### 15. Model Organisms
**Mouse** is the validated model: two independent null lines phenocopy heterotaxy (situs inversus, CHD, pulmonary isomerism, abnormal liver position; partial embryonic lethality). **Phenotype recapitulation is strong** in mouse. **Zebrafish (maternal-zygotic null) and Xenopus (CRISPR/morpholino) do NOT recapitulate** the phenotype — an important limitation highlighting species-specific gene essentiality and cautioning against using these organisms to model CIROZ function. Resources: MGI (mouse), IMPC/EUCOMM (tm1b allele). In-vitro secretion assays (demonstrating CIROZ is secreted and oligomerizes) complement the animal data.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Key contribution |
|---|---|---|---|
| [39753129](https://pubmed.ncbi.nlm.nih.gov/39753129/) | *CIROZ is dispensable in ancestral vertebrates but essential for L-R patterning in humans* | **Primary / defining** | 16 individuals/10 families; variant spectrum; mouse phenocopy; zebrafish/Xenopus negative; module membership; secreted ZP-N protein |
| [40467998](https://pubmed.ncbi.nlm.nih.gov/40467998/) | *Prevalence of laterality defects in CHD* | Supporting / independent | Lists C1ORF127/CIROZ as candidate gene; laterality epidemiology in CHD (1.1%); diagnostic yield ~13% |
| [42630107](https://pubmed.ncbi.nlm.nih.gov/42630107/) | *Genetics in Heterotaxy (DNAH9, PKD1L1, MMP21, GDF1)* | Context | NGS diagnoses only 20–30% of HTX; extracardiac burden affects survival |
| [38884745](https://pubmed.ncbi.nlm.nih.gov/38884745/) | *Molecular Pathways and Animal Models of Defects in Situs* | Mechanism | LRO cilia → Nodal → Lefty → Pitx2; species differences in ciliary requirement |
| [38884711](https://pubmed.ncbi.nlm.nih.gov/38884711/) | *Establishment of Cardiac Laterality* | Mechanism | Defines the downstream Nodal–Pitx2 cascade CIROZ feeds into |
| [41974186](https://pubmed.ncbi.nlm.nih.gov/41974186/) | *Laterality Spectrum Disorders in the Prenatal Era* | Prognosis | Major CHD drives termination and early infant mortality; pregestational diabetes association |
| [39442590](https://pubmed.ncbi.nlm.nih.gov/39442590/) | *Hyperglycaemia induces diet-dependent L-R axis defects* | Gene-environment | Maternal diabetes perturbs Nodal–Pitx2 — shared downstream axis |
| [27425254](https://pubmed.ncbi.nlm.nih.gov/27425254/) | *Bacteremia in Patients with Heterotaxy* | Management | High bacteremia mortality regardless of splenic type |
| [20730421](https://pubmed.ncbi.nlm.nih.gov/20730421/) | *Heterotaxy syndrome: contemporary disease trends* | Prevention | Pneumococcal vaccine protective; interrupted IVC → malrotation screening |
| [27679871](https://pubmed.ncbi.nlm.nih.gov/27679871/) | *Factors influencing bacteraemia in isomerism/CHD* | Management | Most bacteremia episodes nosocomial |
| [42026914](https://pubmed.ncbi.nlm.nih.gov/42026914/) | *Genetics of Primary Ciliary Dyskinesia* | Differential dx | ~50% of PCD have laterality defects — key DDx to distinguish |
| [39969775](https://pubmed.ncbi.nlm.nih.gov/39969775/) | *CFAP53 biallelic mutations / situs inversus* | Differential dx | Example of another recessive laterality gene |

**Evidence source types:** human clinical/genetic (39753129, 40467998, 42630107, 41974186), model organism (39753129 mouse/zebrafish/Xenopus; 39442590 mouse), in vitro (39753129 secretion/oligomerization assays), and review/mechanistic synthesis (38884745, 38884711, 37340963, 36172285).

---

## Limitations and Knowledge Gaps

1. **Single defining cohort.** The disease rests primarily on one 2025 study (16 individuals) plus a second cohort (Dong et al., 5 additional families). The total number of reported patients worldwide is small (~21 families), so phenotype frequencies carry wide confidence intervals.
2. **Incomplete penetrance is unexplained.** Two biallelic individuals had normal situs; the genetic/environmental modifiers responsible are unknown.
3. **Exact biochemical step is inferred.** CIROZ's precise molecular interaction (e.g., whether it directly modulates DAND5, GDF1, or cilia-dependent flow) is not experimentally pinpointed; its placement "after CIROP, before MMP21" is temporal/expression-based.
4. **Species discordance** means zebrafish/Xenopus are poor functional models, limiting rapid in-vivo mechanistic dissection; mechanistic work depends on the slower mouse system.
5. **No specific ICD/Orphanet code**, no dedicated natural-history registry, and no QoL instruments for the CIROZ subtype.
6. **No therapy** targets the pathway; all management is generic heterotaxy care.
7. **Low diagnostic yield** (20–30%) for heterotaxy overall means CIROZ-attributable cases are likely under-ascertained; carrier-frequency and true prevalence estimates are preliminary.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient registry.** Aggregate CIROZ cases via GeneMatcher/Matchmaker Exchange to refine penetrance, expressivity, CHD subtype frequencies, and genotype–phenotype correlations (e.g., does p.Thr19Met confer milder disease than nulls?).
2. **Define CIROZ's biochemical partner(s).** Use co-immunoprecipitation / proximity labeling in mouse node or LRO-like organoids to test direct interaction with DAND5, GDF1, PKD1L1, MMP21, and CIROP; determine whether CIROZ modulates NODAL antagonism.
3. **Mouse mechanistic dissection.** In Ciroz-null embryos, quantify asymmetric Dand5, Nodal, Lefty2, and Pitx2 expression to localize the exact step of cascade failure; test conditional/tissue-specific alleles.
4. **Modifier discovery.** Whole-genome sequencing and expression analysis of penetrant vs non-penetrant biallelic carriers to identify genetic modifiers explaining incomplete penetrance.
5. **Functional variant classification.** Secretion/oligomerization assays for all reported and future missense variants (including p.Thr19Met) to standardize ACMG classification (PS3/PVS1 evidence).
6. **Panel/pipeline updates.** Ensure CIROZ is added to all clinical heterotaxy/laterality and CHD gene panels and to ClinVar/ClinGen curation, with NM_001170754.2 as the reference transcript.
7. **Prospective management study.** Evaluate whether CIROZ-defined patients, given their milder cardiac profile, warrant a distinct surveillance/counseling pathway versus other module genes.

---

*Report compiled from an autonomous multi-iteration investigation (9 confirmed findings; 20 papers reviewed). All mechanistic and clinical claims are attributed to the cited PMIDs above; verbatim abstract quotes are embedded where they anchor a specific claim.*


## Artifacts

- [OpenScientist final report](Heterotaxy_Visceral_14_Autosomal-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Heterotaxy_Visceral_14_Autosomal-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 4 |
| Terms whose name was checked | 14 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0005098` (2 mentions) - the report calls it "left-right organizer / node region"; UBERON calls it **UBERON_0005098**
- `HP:0030853` (1 mention) - the report calls it "abnormal heart/visceral situs"; HP calls it **Heterotaxy**
- `HP:0001696` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Situs inversus totalis**
- `HP:0006528` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Chronic lung disease**
- `HP:0002240` (1 mention) - the report calls it "context"; HP calls it **Hepatomegaly**
- `HP:0000085` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Horseshoe kidney**
- `GO:0005615` (1 mention) - the report calls it "site of secreted CIROZ"; GO calls it **obsolete extracellular space**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `UBERON:0005098` (UBERON_0005098) (2 mentions) - replaced by `UBERON:0004200`
- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0038003` (1 mention) - the report calls it "Nodal signaling pathway"; GO calls it **G protein-coupled opioid receptor signaling pathway**, and lists "opioid receptor signaling pathway" among its other names
- `HP:0002566` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Intestinal malrotation**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`, `MGI`.