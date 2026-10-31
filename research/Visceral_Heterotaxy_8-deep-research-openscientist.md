---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T23:35:12.559218'
end_time: '2026-10-20T23:47:57.179013'
duration_seconds: 764.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Visceral Heterotaxy 8
  mondo_id: MONDO:0014967
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
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 7
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:27616478
  - PMID:27272319
  - PMID:20080492
  relevance_assessed: 17
  on_topic: 10
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 35
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 26
  labels_matching: 12
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0004935
    reported_labels:
    - Visceral heterotaxy
    - Physical malformation
    ontology_label: Pulmonary artery atresia
  - term_id: HP:0001696
    reported_labels:
    - Physical malformation
    ontology_label: Situs inversus totalis
  - term_id: HP:0001651
    reported_labels:
    - Physical
    ontology_label: Dextrocardia
  - term_id: HP:0001746
    reported_labels:
    - Physical/laboratory
    ontology_label: Asplenia
  - term_id: HP:0002566
    reported_labels:
    - Physical
    ontology_label: Intestinal malrotation
  - term_id: HP:0005301
    reported_labels:
    - Structural
    ontology_label: Persistent left superior vena cava
  - term_id: GO:0060287
    reported_labels:
    - epithelial cilium / "nodal cilium
    ontology_label: epithelial cilium movement involved in determination of left/right
      asymmetry
  - term_id: GO:0072372
    reported_labels:
    - primary cilium assembly
    ontology_label: GO_0072372
  - term_id: UBERON:0005725
    reported_labels:
    - ciliated embryonic node
    ontology_label: olfactory system
  - term_id: UBERON:0004341
    reported_labels:
    - node
    ontology_label: primitive streak
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0072372
    ontology_label: GO_0072372
    replaced_by: GO:0005929
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
  path: Visceral_Heterotaxy_8-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Visceral_Heterotaxy_8-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Visceral Heterotaxy 8
- **MONDO ID:** MONDO:0014967 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Visceral Heterotaxy 8** covering all of the
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

# Visceral Heterotaxy 8 (HTX8) — Comprehensive Disease Characteristics Report

**Disease:** Visceral Heterotaxy 8 (HTX8) · **MONDO:** MONDO:0014967 · **Gene:** *PKD1L1* · **Category:** Mendelian (autosomal recessive)
**Report date:** 2026-10-20 · Evidence base: human clinical case reports, model-organism genetics, in-vitro/biochemical, and computational/database sources.

> **Summary answer.** Visceral Heterotaxy 8 (HTX8; OMIM #617205) is a rare autosomal-recessive laterality (left–right patterning) disorder caused by biallelic loss-of-function or damaging variants in *PKD1L1* (polycystin-1-like 1, chr 7p12.3). PKD1L1 partners with PKD2 (polycystin-2/TRPP2) on motile cilia of the embryonic node/Kupffer's vesicle to sense leftward "nodal flow"; its loss disrupts the earliest left-biased Ca²⁺/Nodal signal, randomizing or bilateralizing organ situs and producing a spectrum from situs inversus totalis to situs ambiguus (heterotaxy) with frequent complex congenital heart disease and splenic anomalies (including asplenia). There is no gene-specific therapy; management is anatomy-driven (cardiac surgery, infection prophylaxis for asplenia), and prognosis is governed mainly by the severity of congenital heart disease.

---

## 1. Disease Information

**Overview.** HTX8 is a Mendelian subtype of visceral heterotaxy — a congenital disorder of left–right (L-R) body-axis determination in which thoracic and abdominal organs are abnormally arranged across the midline. Clinically it ranges from **situs inversus totalis (SIT)** (complete mirror-image reversal) to **situs ambiguus / heterotaxy** (discordant, randomized organ positioning), typically with congenital heart disease (CHD). "Disruption of the establishment of left-right (L-R) asymmetry leads to situs anomalies ranging from situs inversus totalis (SIT) to situs ambiguus (heterotaxy)" (PMID 27616478).

**Key identifiers.**
- **MONDO:** MONDO:0014967 (Visceral heterotaxy 8)
- **OMIM:** #617205 (phenotype, HTX8, autosomal recessive); gene *PKD1L1* \*609721
- **Gene/HGNC:** *PKD1L1*, HGNC:18053; Ensembl ENSG00000158683; NCBI Gene 168507; UniProt Q8TDX9
- **Orphanet:** broad entry ORPHA:450 (Heterotaxia); no PKD1L1-specific ORPHA code
- **MeSH:** D059446 (Heterotaxy Syndrome)
- **ICD-10:** Q89.3 (Situs inversus); **ICD-11:** LB01.1 (Situs ambiguous / heterotaxy)
- **HPO anchor:** HP:0004935 (Visceral heterotaxy)

**Synonyms / alternative names.** Heterotaxy, visceral, 8, autosomal recessive; HTX8; PKD1L1-related heterotaxy/laterality defect; situs ambiguus/situs inversus due to *PKD1L1*.

**Information source type.** Derived from **aggregated disease-level resources** (OMIM, Orphanet, ClinVar, UniProt, gnomAD) combined with **individual patient case reports** (small families); not from large EHR cohorts.

---

## 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous or compound-heterozygous) pathogenic variants in *PKD1L1*. Whole-exome sequencing "identified homozygous mutations in PKD1L1 from three affected individuals in two unrelated families" (PMID 27616478). This is a **monogenic, recessive developmental disorder**; it is not infectious and has no established acquired cause.

**Genetic risk factors.**
- **Causal variants:** loss-of-function (splice, nonsense) and damaging missense alleles in *PKD1L1* (see §4).
- **Consanguinity** is a key risk context — reported probands are homozygous, consistent with autosomal-recessive inheritance and increased in consanguineous or founder settings.
- **Carrier status:** heterozygotes are unaffected (gene is not haploinsufficient; gnomAD pLI≈0).

**Environmental risk factors.** None established specifically for HTX8. For heterotaxy broadly, **maternal pregestational diabetes mellitus** is associated with laterality/abdominal-situs phenotypes (PMID 41974186) and is a recognized teratogenic risk factor for L-R defects; this is a disease-level association, not demonstrated for PKD1L1 cases.

**Protective factors.** None identified (genetic or environmental). A single wild-type *PKD1L1* allele is "protective" in the Mendelian sense (carriers are healthy).

**Gene–environment interactions.** Not specifically characterized for *PKD1L1*. Laterality determination is a threshold/stochastic developmental process; modifier/background effects are plausible (variable expressivity between SIT and heterotaxy even within families) but unproven.

---

## 3. Phenotypes

All manifestations are **congenital (prenatal/neonatal onset)**, structural/physical, lifelong, and non-progressive as malformations (clinical course is driven by complications). Frequencies below are qualitative given the very small reported cohort.

| Phenotype | Type | HPO term | Notes / frequency |
|---|---|---|---|
| Visceral heterotaxy / situs ambiguus | Physical malformation | HP:0004935 | Core feature |
| Situs inversus totalis | Physical malformation | HP:0001696 | Reported (p.Cys1691Ser family) |
| Complex congenital heart disease | Clinical sign/structural | HP:0001627 (Abnormal heart morphology) | Very frequent; often lethal |
| Dextrocardia / abnormal cardiac position | Physical | HP:0001651 | Common in situs defects |
| Atrioventricular septal defect, DORV, TAPVC, transposition | Structural | HP:0006695 / HP:0011565 etc. | Seen across heterotaxy spectrum |
| Asplenia | Physical/laboratory | HP:0001746 | Reported (p.Gln463*); confers infection risk |
| Polysplenia / abnormal spleen | Physical | HP:0001748 / HP:0025059 | Part of spectrum |
| Intestinal malrotation | Physical | HP:0002566 | Common heterotaxy complication |
| Abnormal inferior vena cava / vascular laterality | Structural | HP:0005301 | Interrupted IVC in left isomerism |

**Onset:** neonatal/congenital (often detected prenatally). **Severity:** variable — from isolated SIT (potentially mild) to lethal complex CHD. **Progression:** stable malformation; secondary deterioration from cardiac failure, arrhythmia, or infection. **Quality of life:** dominated by cardiac disease burden (surgeries, heart failure, arrhythmia) and, in asplenia, lifelong infection vigilance; no disease-specific QoL instruments exist — generic pediatric CHD tools (PedsQL, PROMIS) apply.

---

## 4. Genetic / Molecular Information

**Causal gene.** *PKD1L1* (polycystin-1-like 1), HGNC:18053, Ensembl ENSG00000158683, gene OMIM \*609721, GRCh38 chr7:47,740,202–47,948,466 (7p12.3), canonical transcript ENST00000289672; protein UniProt Q8TDX9, 2849 aa.

**Protein architecture (UniProt Q8TDX9).** 11-transmembrane polycystin-1-family receptor with a large extracellular N-terminus (res. 1–1748): two **PKD domains** (508–590; 592–673), a large **REJ** (receptor-for-egg-jelly) domain (674–1571), a **GAIN-B** domain (1587–1735) containing the **GPS** autoproteolysis motif (1691–1735), and a cytoplasmic **PLAT/LH2** domain (1796–1913); ~20 N-glycosylation sites and disulfide bonding.

**Reported pathogenic variants (germline).**
| Variant (cDNA) | Protein | Class | Consequence | Phenotype | PMID |
|---|---|---|---|---|---|
| c.6473+2_6473+3delTG | splice-donor, intron 42 | Splice-site, LoF | Loss of function | Heterotaxy + complex CHD | 27616478 |
| c.5072G>C | p.Cys1691Ser | Missense (GPS motif) | Disrupts GPS disulfide, folding/autoproteolysis | SIT + CHD | 27616478 |
| c.1387C>T | p.Gln463* | Nonsense, LoF | Truncation (loss of REJ/TM/channel region) | Heterotaxy + congenital asplenia | 35691949 |

"the p.Cys1691Ser substitution affects a highly conserved cysteine residue and is predicted by molecular modeling to disrupt a disulfide bridge essential for the proper folding of the … (GPS) motif" (PMID 27616478).

**Variant classification & frequency.** ClinVar lists ~1,417 *PKD1L1* variants, the large majority **variants of uncertain significance (VUS)** (~1,157 VUS vs ~170 pathogenic / ~72 likely pathogenic), reflecting limited functional/segregation data. Pathogenic HTX8 alleles are individually rare/absent in population databases (gnomAD). **Origin:** germline. **Functional consequence:** **loss of function** (recessive); no gain-of-function or dominant-negative mechanism established.

**Population constraint (gnomAD).** pLI ≈ 0, oe_lof = 0.73 (90% CI 0.66–0.81), missense oe = 0.95, mis_z = 1.35. The gene is **not haploinsufficient**, consistent with asymptomatic heterozygous carriers and recessive disease.

**Modifier genes.** None proven. Variable expressivity (SIT vs heterotaxy) suggests modifiers/stochastic effects. In mouse genetics, *Pkd1l1* acts as an **upstream repressor of *Pkd2*** (PMID 27272319), so dosage of polycystin-pathway genes is biologically relevant.

**Epigenetics / chromosomal abnormalities.** No HTX8-specific epigenetic signature reported. HTX8 is caused by point/small variants, not large chromosomal rearrangements; however, CNVs in body-patterning pathways (NODAL/BMP/WNT, e.g., *NIPBL, TBX6, FGF12, RBFOX1*) contribute to the broader heterotaxy population (PMID 27637763).

---

## 5. Environmental Information

- **Environmental factors / toxins / infectious agents:** none causal for HTX8 (purely genetic).
- **Lifestyle factors:** not applicable to disease causation.
- **Disease-level association:** maternal **pregestational diabetes** correlates with laterality-spectrum phenotypes (PMID 41974186) — relevant to heterotaxy broadly, not to monogenic PKD1L1 cases.
- **Infectious agents:** not causal, but **secondary infection risk is central** in patients with asplenia (see §11/§13).

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic *PKD1L1* loss-of-function/damaging variant** → results in absent or misfolded PKD1L1 protein (truncation; GPS-motif disulfide disruption for p.Cys1691Ser). *[demonstrated: human genetics + molecular modeling]*
2. **Loss of functional PKD1L1** → prevents assembly of the PKD1L1–PKD2 (polycystin-1-like-1 / polycystin-2) receptor–channel complex on cilia of the embryonic node / Kupffer's vesicle. *[demonstrated: co-localization + physical interaction, mouse & medaka]*
3. **Motile node cilia still generate normal leftward "nodal flow"** (cilia motility is intact) → but the flow **cannot be interpreted** without the PKD1L1–PKD2 sensor. *[demonstrated: normal flow/cilia in mutants]*
4. **Flow normally transfers PKD1L1-containing fibrous strands leftward**, facilitating a **left-dominant intracellular Ca²⁺ elevation** at the left node margin (FGFR/Shh-dependent) → in mutants this earliest left-biased signal fails. *[demonstrated in mouse; Tanaka 2023]*
5. **Failed/symmetric Ca²⁺ signaling** → loss of left-restricted repression such that the **Nodal–Lefty–Pitx2 cascade is not confined to the left** (becomes absent, bilateral, or randomized) in the lateral plate mesoderm. *[demonstrated: PKD1L1 restricts Nodal to the left; Pkd1l1 mutant activates Nodal bilaterally]*
6. **Loss of asymmetric Pitx2 patterning** → randomized/discordant morphogenesis and looping of heart, gut, spleen, lungs and great vessels. *[inferred from conserved L-R pathway]*
7. **Abnormal situs** → **situs inversus totalis OR situs ambiguus/heterotaxy with complex CHD, splenic anomalies, intestinal malrotation, vascular laterality defects** → clinical disease. *[demonstrated: human phenotypes]*

**Branch point** at step 5: depending on whether Nodal is lost, bilateral, or randomized, the organism develops SIT (coordinated reversal), left isomerism (polysplenia), or right isomerism (asplenia) — explaining the phenotypic spectrum, including the asplenia case (PMID 35691949).

**Supporting detail by category.**
- **Molecular pathways:** Nodal/TGF-β signaling (Nodal–Lefty2–Pitx2), upstream FGFR and Sonic hedgehog (Shh) signaling, calcium signaling. Reactome "Nodal signaling"; KEGG TGF-β pathway.
- **Protein dysfunction:** loss of function via truncation or GPS-domain misfolding; PKD1L1 normally undergoes GPS autoproteolysis and forms a Ca²⁺-permeable channel complex with PKD2/TRPP2. "PKD1L1 is sufficient to mediate a Ca2+ signaling response after flow stimulation … an extracellular PKD domain within PKD1L1 is crucial for PKD1L1 function" (PMID 27272319).
- **Cellular processes:** ciliary mechanosensation/chemosensation and ciliary Ca²⁺ signaling; embryonic L-R symmetry breaking.
- **Biochemical abnormality:** defective ciliary cation (Ca²⁺) channel/receptor complex.
- **Immune involvement:** not primary; functional/anatomic **asplenia** causes secondary immunodeficiency to encapsulated bacteria.
- **Metabolic/epigenetic changes:** none characteristic.

**GO term suggestions:** GO:0007368 (determination of left/right symmetry); GO:0003351 (epithelial cilium movement involved in determination of L/R asymmetry); GO:0060287 (epithelial cilium / "nodal cilium"); GO:0060170 (ciliary membrane); GO:0005929 (cilium); GO:0072372 (primary cilium assembly); GO:0005262 (calcium channel activity); GO:0019228/GO:0070588 (Ca²⁺ ion transmembrane transport).
**Cell Ontology (CL):** node/pit cells & crown cells of the embryonic organizer → CL:0000222 (mesodermal cell), ciliated embryonic node cells; CL:0000057 (fibroblast, LPM context). **CHEBI:** CHEBI:29108 (calcium(2+)).

---

## 7. Anatomical Structures Affected

**Organ level (primary):** heart and great vessels (cardiovascular), spleen (asplenia/polysplenia), stomach/intestine (malrotation), liver (midline/abnormal lobation), lungs (isomerism), inferior vena cava/systemic veins.
**Body systems:** cardiovascular (primary), digestive, respiratory, lymphatic/immune (spleen), hepatobiliary.
**Secondary involvement:** immune deficiency from asplenia; biliary atresia in some left-isomerism heterotaxy; pulmonary consequences of CHD.

**Developmental origin (where the defect acts):** the **embryonic node / Kupffer's vesicle** (midline left–right organizer) and **lateral plate mesoderm** — UBERON:0005725 (ciliated embryonic node) / UBERON:0004341 (node), UBERON:0003081 (lateral plate mesoderm). Resulting organ UBERON terms: UBERON:0000948 (heart), UBERON:0002106 (spleen), UBERON:0000160 (intestine), UBERON:0002048 (lung), UBERON:0001072 (inferior vena cava).

**Tissue/cell level:** ciliated epithelial cells of the node/KV; lateral-plate mesoderm; cardiac progenitor mesoderm. **Subcellular (GO Cellular Component):** primary/motile cilium (GO:0005929), ciliary membrane (GO:0060170), plasma membrane.

**Localization & lateralization:** defect is of **body-axis laterality itself** — manifestations are intrinsically bilateral/asymmetric/randomized (loss of normal left-right asymmetry; isomerism = loss of sidedness). HPO HP:0001631 etc. for specific cardiac lesions.

---

## 8. Temporal Development

- **Onset:** congenital; organ situs is specified in early embryogenesis (gastrulation/node stage, ~weeks 3–4 in humans). Frequently **diagnosed prenatally** by ultrasound/fetal echocardiography (heterotaxy has among the highest prenatal detection rates, ~91% in one series, PMID 42324491).
- **Onset pattern:** structural malformation present at birth (not acute/subacute).
- **Progression:** the malformation is **stable**; clinical course is **non-progressive as a lesion** but complicated by heart failure, arrhythmia (complete heart block), pulmonary venous obstruction, and infection.
- **Critical period:** the **node/LPM signaling window** in early embryogenesis is the only period during which L-R situs can be set — there is **no postnatal window to correct the primary patterning defect**, only to palliate its consequences.
- **Duration:** lifelong (chronic).

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (biallelic *PKD1L1*). Heterozygous carriers unaffected.
- **Penetrance/expressivity:** biallelic genotypes appear highly penetrant for a laterality phenotype, but **expressivity is variable** (SIT vs heterotaxy; differing CHD severity, including within the same family).
- **Consanguinity:** relevant — reported probands are homozygous; recessive disease risk rises with consanguinity/founder effects.
- **Carrier frequency / founder effects:** not precisely established; individual pathogenic alleles are rare; a Chinese nonsense allele (p.Gln463*) was the first reported in that population (PMID 35691949).
- **Anticipation / mitochondrial / germline mosaicism:** not applicable / not reported.

**Epidemiology.**
- **HTX8 specifically:** ultra-rare; only a handful of families reported worldwide — population prevalence **unknown**.
- **Heterotaxy / atrial isomerism (parent category):** prevalence **~1 in 10,000–20,000 live births**, accounting for up to **~4% of all cardiac malformations** (PMID 34491249); heterotaxy represents a minority of laterality disorders (e.g., 249 HS among 566 fetal laterality cases over 721,562 deliveries, PMID 42110452).
- **Sex ratio / geography:** no established PKD1L1-specific skew; general heterotaxy shows modest male predominance in some registries. Reported PKD1L1 cases span diverse ancestries (consistent with private recessive alleles).

---

## 10. Diagnostics

**Imaging (anatomic diagnosis, primary).**
- **Fetal ultrasound + fetal echocardiography** — mainstay prenatal detection (very high detection for heterotaxy, PMID 42324491).
- **Postnatal echocardiography**, cardiac **CT/MRI/angiography** for segmental cardiac/vascular anatomy; **abdominal ultrasound/CT** for spleen, liver, gut malrotation; **upper GI series** for malrotation.
**Laboratory / functional.**
- **Peripheral blood smear for Howell-Jolly bodies** → screen for functional asplenia; pitted-RBC counts / spleen scintigraphy to assess splenic function.
- ECG/Holter for **complete heart block** and arrhythmia.

**Genetic testing (definitive molecular diagnosis).**
- **Approach:** because heterotaxy is highly heterogeneous ("pathogenic genetic lesions are found in less than 20% of HS patients," PMID 35691949), **broad testing is preferred**: multigene **heterotaxy/CHD panels** (including *PKD1L1, ZIC3, NODAL, CFC1, ACVR2B, LEFTY2, GDF1, MMP21, CCDC11/CFAP53, DNAH5*…), **whole-exome (WES)** or **whole-genome sequencing (WGS)**. WES identified the original PKD1L1 families (PMID 27616478).
- **Single-gene testing** of *PKD1L1* is appropriate when a consistent phenotype or family variant is known; confirm **biallelic** status and parental phase (segregation).
- **Chromosomal microarray (CMA)/karyotype** to exclude CNVs/aneuploidy contributing to heterotaxy (PMID 27637763).
- **Interpretation caveat:** high **VUS burden** in *PKD1L1* — classification benefits from recessive segregation, consanguinity, GPS/LoF functional rationale, and ACMG/AMP criteria.

**Clinical criteria / differential diagnosis.** No disease-specific criteria; diagnosis = demonstrated situs anomaly + biallelic *PKD1L1* variants. **Differential:** other genetic heterotaxy (X-linked *ZIC3* = HTX1; *NODAL, CFC1, ACVR2B, GDF1, MMP21*, etc.), **primary ciliary dyskinesia (PCD)** with laterality defects (distinguished by chronic sinopulmonary disease, abnormal ciliary motility/ultrastructure, nasal nitric oxide — features *absent* in PKD1L1, whose cilia are motile), and syndromic/CNV causes.

**Screening.** No newborn screening for HTX8; **cascade carrier testing** of relatives and **prenatal/preimplantation genetic testing** are options once the familial variants are known.

---

## 11. Outcome / Prognosis

- **Prognosis is driven by the cardiac phenotype.** In a heterotaxy+CHD cohort (n=197), **5- and 10-year survival ≈71% and ≈68%**; **left atrial isomerism had better survival than right atrial isomerism**; **complete heart block (CHB)** and ventricular dysfunction predicted fetal demise, and **pulmonary venous obstruction + CHB** predicted postnatal mortality (PMID 42185088). "CHB and pulmonary venous obstruction remain significant predictors of postnatal mortality…" (PMID 42185088).
- **Infection/asplenia mortality:** asplenia confers high risk of overwhelming bacteremia — in a systematic review, "There were 42 documented cases of bacteremia in 32 patients. Approximately, 79% of these had absence of a spleen" (PMID 27425254), mean age ~17 months, with high mortality.
- **Perinatal outcomes (laterality spectrum):** major CHD drives termination, surgery and early mortality; live birth ~80%, with infant mortality concentrated in infancy (PMID 41974186).
- **Morbidity:** multiple cardiac surgeries, arrhythmia/pacemaker dependence, heart failure, GI morbidity (malrotation/volvulus), feeding/growth problems; lifelong infection risk with asplenia.
- **Prognostic factors:** type/severity of CHD, atrial isomerism subtype (RAI worse), CHB, pulmonary venous obstruction, splenic status. No molecular prognostic biomarker specific to PKD1L1.

---

## 12. Treatment

**No disease-specific or gene-directed therapy exists.** Management is **symptomatic, anatomy-driven, and multidisciplinary** (NCIT terms suggested).
- **Cardiac surgical/interventional:** staged palliation (single-ventricle pathway: Norwood/Glenn/Fontan) or biventricular repair depending on anatomy; repair of AVSD, TAPVC, DORV; **pacemaker** for complete heart block (NCIT: C157809 Cardiac Surgery; C50106 Pacemaker; C98298 Fontan Procedure).
- **Gastrointestinal:** **Ladd procedure** for intestinal malrotation/volvulus (NCIT: C157751 surgical procedure).
- **Asplenia management (critical):** **vaccination** against encapsulated organisms — pneumococcal (PCV + PPSV23), *Haemophilus influenzae* type b, meningococcal (ACWY + B) — plus **antibiotic prophylaxis** (e.g., penicillin/amoxicillin) and immediate empiric antibiotics for febrile illness (NCIT: C15346 Vaccination; C154547 Antibiotic Therapy; C15431 Prophylaxis). Patient education and medical-alert measures improve adherence (PMID 32759171; PMID 31937251).
- **Supportive:** heart-failure pharmacotherapy (diuretics e.g. furosemide, afterload reduction, beta-blockade), nutritional support/gastrostomy, arrhythmia management (PMID 41049903 case series).
- **Advanced/experimental therapeutics:** **none** — no gene therapy, RNA therapy, cell therapy, or targeted/immunotherapy for PKD1L1-heterotaxy (the primary defect is prenatal/developmental and not correctable postnatally). No pharmacogenomic considerations specific to the gene.
- **Pharmacogenomics / personalized medicine:** genotype confirms diagnosis and informs recurrence risk/reproductive counseling rather than drug selection.

---

## 13. Prevention

- **Primary prevention:** not possible for the genetic lesion. **Preconception/prenatal genetic counseling** for recessive 25% recurrence risk; **carrier screening** of partners in known families; **PGT/prenatal diagnosis** where familial variants are defined. Optimizing **maternal glycemic control** addresses a disease-level (not PKD1L1-specific) laterality risk factor (PMID 41974186).
- **Secondary prevention:** **prenatal detection** (fetal echo/ultrasound) enabling planned delivery at a cardiac center and early intervention (PMID 42324491); early postnatal spleen-function assessment (Howell-Jolly bodies).
- **Tertiary prevention (prevent complications):** the **cornerstone** — asplenia **vaccination + antibiotic prophylaxis** to prevent overwhelming post-splenectomy/asplenia sepsis (PMID 27425254; PMID 31937251; PMID 32759171); arrhythmia surveillance/pacing; surgical correction of malrotation before volvulus; endocarditis prophylaxis per cardiac guidelines.
- **Genetic counseling:** autosomal-recessive counseling; cascade testing; reproductive options.

---

## 14. Other Species / Natural Disease

- **Conservation:** *PKD1L1*'s L-R role is **highly conserved across vertebrates**. Orthologs: **mouse** *Pkd1l1* (NCBI Gene 207225; MGI), **medaka** *pkd1l1* (ZFIN/medaka; the classic L-R mutant **abecobe/abc**), **zebrafish** *pkd1l1* (ZFIN). Taxa: *Mus musculus* (NCBI:txid10090), *Oryzias latipes* (medaka, NCBI:txid8090), *Danio rerio* (NCBI:txid7955).
- **Natural animal disease / veterinary:** no well-characterized naturally occurring *PKD1L1* heterotaxy disease in companion animals is documented in OMIA for this gene; situs/laterality anomalies occur sporadically across species but are not established as a *PKD1L1* natural disease.
- **Comparative biology:** mouse and fish models reproduce the human mechanism (node/KV flow-sensing), making them the key translational systems (see §15). **Evolutionary note:** the two-cilia/polycystin flow-sensing paradigm is conserved from fish to mammals.
- **Zoonotic potential:** not applicable (non-infectious developmental disorder).

---

## 15. Model Organisms

**Mouse (*Mus musculus*) — primary mammalian model.**
- **Types:** *Pkd1l1* knockout (e.g., gene-trap/null line, Vogel 2010, PMID 20080492) and ENU/point mutants (e.g., *rks*); knock-in reporter **KikGR-PKD1L1** for live protein imaging (Tanaka 2023, PMID 37413993).
- **Phenotype recapitulation (strong):** situs inversus/laterality defects; "both mutants fail to activate asymmetric gene expression at the node or in the lateral plate and exhibit right isomerism of the lungs" (PMID 21307093). Node morphology and cilia motility normal → defect is in **flow interpretation**, matching human mechanism.
- **Key insight:** "the absence of respiratory tract lesions, hydrocephalus, and male infertility in Pkd1l1(-/-) mice … suggested that dysfunction of motile cilia was not involved" (PMID 20080492) — **distinguishes HTX8 from PCD**.
- **Limitation:** high perinatal lethality of nulls; models the developmental patterning defect but not the postnatal human CHD surgical course.

**Medaka (*Oryzias latipes*).** The L-R mutant **abecobe (abc) = *pkd1l1***: "abecobe (abc) is defective for left-right asymmetric expression of southpaw, lefty and charon, but not for nodal flow" (PMID 21307098); PKD1L1 required in **Kupffer's vesicle** and colocalizes/interacts with Pkd2 on motile KV cilia.

**Zebrafish (*Danio rerio*).** *pkd1l1* expressed in KV; morpholino/mutant studies implicate polycystin signaling in L-R patterning (Kupffer's vesicle = node equivalent).

**In-vitro / cellular.** Cultured cells supplied **artificial flow** show PKD1L1 is "sufficient to mediate a Ca2+ signaling response after flow stimulation" (PMID 27272319); heterologous PKD1L1–PKD2 complexes used for biochemistry/channel studies.

**Applications:** dissecting node/KV flow sensing, polycystin complex assembly, Nodal cascade restriction, Ca²⁺ signaling, and variant functional testing. **Resources:** MGI, IMPC, ZFIN, Alliance of Genome Resources.

---

## Supported vs. Refuted Hypotheses

**Supported.**
1. HTX8 is autosomal-recessive, caused by biallelic *PKD1L1* LoF/damaging variants (PMID 27616478, 35691949).
2. PKD1L1–PKD2 ciliary complex is the nodal-flow sensor restricting Nodal to the left (PMID 21307093, 21307098, 27272319, 37413993).
3. The pathology is a **flow-interpretation (sensory) defect, not a ciliary-motility defect** → mechanistically distinct from PCD (PMID 20080492).
4. Prognosis is governed by CHD severity and asplenia-related infection risk (PMID 42185088, 27425254).

**Refuted / not supported.**
- *PKD1L1* is **not** a dominant/haploinsufficient disease gene (gnomAD pLI≈0; carriers healthy).
- HTX8 is **not** driven by motile-cilia dysfunction (no PCD airway/hydrocephalus phenotype in nulls).
- No evidence for gain-of-function, somatic, infectious, or acquired/environmental primary causation.

## Limitations and Future Directions

- **Very small human evidence base** (few families); PKD1L1-specific prevalence, penetrance, sex ratio, and natural history are not quantified — most clinical figures derive from the broader heterotaxy category.
- **High VUS burden** limits molecular diagnosis; **functional assays** (flow-induced Ca²⁺, GPS autoproteolysis, PKD1L1–PKD2 trafficking) are needed to reclassify variants.
- **No structural model of the human PKD1L1–PKD2 complex** at the variant level; cryo-EM would clarify GPS/PKD-domain variant effects.
- **No targeted therapy;** research should define modifier genes, improve prenatal risk stratification, and standardize asplenia prophylaxis in this population.

---

### Key references (PMIDs)
27616478 (Vetrini 2016, human biallelic PKD1L1); 35691949 (Gu 2022, nonsense + asplenia); 21307093 (Field 2011, mouse); 21307098 (Kamura 2011, medaka); 27272319 (Grimes 2016, epistasis/Ca²⁺); 37413993 (Tanaka 2023, flow transfers polycystin); 20080492 (Vogel 2010, Pkd1l1−/− mouse); 24756726 (TRPP/polycystin review); 42185088 (heterotaxy+CHD outcomes); 27425254 (bacteremia in heterotaxy); 34491249 (isomerism epidemiology); 42324491 (prenatal detection); 41974186 (laterality spectrum outcomes/PDM); 27637763 (heterotaxy CNVs); 38884744 (human genetics of situs); 32759171 / 31937251 (asplenia prophylaxis).


## Artifacts

- [OpenScientist final report](Visceral_Heterotaxy_8-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Visceral_Heterotaxy_8-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 17 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:27616478`: "the p.Cys1691Ser substitution affects a highly conserved cysteine residue and is predicted by molecular modeling to disrupt a disulfide bridge essential for the proper folding of the … (GPS) motif"
  - closest text in source: "The p.Cys1691Ser substitution affects a highly conserved cysteine residue and is predicted by molecular modeling to disrupt a disulfide bridge essential for the proper folding of the G protein-coupled receptor proteolytic site (GPS) motif"
- `PMID:27272319`: "PKD1L1 is sufficient to mediate a Ca2+ signaling response after flow stimulation … an extracellular PKD domain within PKD1L1 is crucial for PKD1L1 function"
  - closest text in source: "Finally, we show that an extracellular PKD domain within PKD1L1 is crucial for PKD1L1 function; as such, destabilizing the domain causes L-R defects in the mouse"
- `PMID:20080492` *(abstract only)*: "the absence of respiratory tract lesions, hydrocephalus, and male infertility in Pkd1l1(-/-) mice … suggested that dysfunction of motile cilia was not involved"
  - closest text in source: "In contrast, the absence of respiratory tract lesions, hydrocephalus, and male infertility in Pkd1l1(-/-) mice (for: polycystic kidney disease 1 like 1) suggested that dysfunction of motile cilia was not involved in the development of SI in this line"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 26 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0004935` (2 mentions) - the report calls it "Visceral heterotaxy", "Physical malformation"; HP calls it **Pulmonary artery atresia**
- `HP:0001696` (1 mention) - the report calls it "Physical malformation"; HP calls it **Situs inversus totalis**
- `HP:0001651` (1 mention) - the report calls it "Physical"; HP calls it **Dextrocardia**
- `HP:0001746` (1 mention) - the report calls it "Physical/laboratory"; HP calls it **Asplenia**
- `HP:0002566` (1 mention) - the report calls it "Physical"; HP calls it **Intestinal malrotation**
- `HP:0005301` (1 mention) - the report calls it "Structural"; HP calls it **Persistent left superior vena cava**
- `GO:0060287` (1 mention) - the report calls it "epithelial cilium / "nodal cilium"; GO calls it **epithelial cilium movement involved in determination of left/right asymmetry**
- `GO:0072372` (1 mention) - the report calls it "primary cilium assembly"; GO calls it **GO_0072372**
- `UBERON:0005725` (1 mention) - the report calls it "ciliated embryonic node"; UBERON calls it **olfactory system**
- `UBERON:0004341` (1 mention) - the report calls it "node"; UBERON calls it **primitive streak**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0072372` (GO_0072372) (1 mention) - replaced by `GO:0005929`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0014967` (2 mentions) - the report calls it "Visceral heterotaxy 8"; MONDO calls it **heterotaxy, visceral, 8, autosomal**, and lists "PKD1L1 visceral heterotaxy" among its other names
- `GO:0003351` (1 mention) - the report calls it "epithelial cilium movement involved in determination of L/R asymmetry"; GO calls it **epithelial cilium movement involved in extracellular fluid movement**
- `GO:0070588` (1 mention) - the report calls it "Ca²⁺ ion transmembrane transport"; GO calls it **calcium ion transmembrane transport**
- `CL:0000057` (1 mention) - the report calls it "fibroblast, LPM context"; CL calls it **fibroblast**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0004935` - called "Visceral heterotaxy", "Physical malformation"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.