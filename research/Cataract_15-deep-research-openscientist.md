---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-28T22:35:05.791084'
end_time: '2026-10-28T22:48:53.410454'
duration_seconds: 827.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cataract 15
  mondo_id: MONDO:0014110
  category: Mendelian
  causal_genes: MIP
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
citation_count: 15
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 17
  validator_version: 0.4.0
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 3
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0014110
    reported_labels:
    - MONDO
    ontology_label: cataract 15 multiple types
  - term_id: HP:0000518
    reported_labels:
    - Clinical sign
    ontology_label: Cataract
  - term_id: HP:0000519
    reported_labels:
    - Clinical sign
    ontology_label: Developmental cataract
  - term_id: HP:0100018
    reported_labels:
    - Clinical sign
    ontology_label: Nuclear cataract
  - term_id: HP:0010920
    reported_labels:
    - Clinical sign
    ontology_label: Zonular cataract
  - term_id: HP:0100019
    reported_labels:
    - Clinical sign
    ontology_label: Cortical cataract
  - term_id: HP:0000505
    reported_labels:
    - Symptom
    ontology_label: Visual impairment
  - term_id: CL:0000204
    reported_labels:
    - Tissue/cell level:** Lens fiber cells
    ontology_label: acceleration receptive cell
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0016021
    ontology_label: GO_0016021
    replaced_by: GO:0016020
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cataract_15-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cataract_15-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 15
- **MONDO ID:** MONDO:0014110 (if available)
- **Causal gene(s):** MIP
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

Please provide a comprehensive research report on **Cataract 15** covering all of the
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

# Cataract 15 (MONDO:0014110): A Comprehensive Disease Characterization

## Summary

**Cataract 15** (MONDO:0014110; OMIM #615274) is a rare, non-syndromic, autosomal dominant inherited cataract caused by heterozygous mutations in **MIP** (Major Intrinsic Protein of lens fiber; HGNC: MIP; gene OMIM 154050; chromosome 12q13.3). MIP encodes **Aquaporin-0 (AQP0, also MP26/MP28)**, the single most abundant membrane protein of the lens fiber cell, constituting approximately 45% of fiber-cell membrane protein. The disease is defined by the *gene*, not merely by the serial disease name: the causal gene for Cataract 15 is **MIP/AQP0**, and this report follows the MONDO ID and gene identifier rather than the serial numeral.

AQP0 is a bifunctional protein. In its open conformation it acts as a water channel transporting water across the fiber-cell membrane; in its closed/junctional conformation it acts as a cell-to-cell adhesion molecule that holds adjacent fiber cells in tight register, maintaining the narrow intercellular space, Y-suture architecture, compact fiber packing, and the smooth refractive-index gradient (RING) required for lens transparency. Most pathogenic MIP variants are missense changes that cause the mutant protein to misfold and become retained in the cytoplasm rather than trafficking to the plasma membrane. Because AQP0 is a tetramer, the mislocalized mutant subunit co-retains wild-type subunits, producing a **dominant-negative** effect that explains the autosomal dominant inheritance in heterozygotes.

Clinically, Cataract 15 presents as bilateral, congenital or early-childhood, progressive lens opacity with highly variable morphology (polymorphic, lamellar/zonular, nuclear, cortical punctate, with or without Y-suture involvement), even within a single family. It affects only the ocular lens, is not life-limiting, and has no disease-modifying pharmacotherapy. Management is surgical — lensectomy with or without intraocular lens implantation, performed early in infancy to prevent deprivation amblyopia — supported by optical correction, amblyopia therapy, newborn red-reflex screening, and genetic counseling with ~50% transmission risk in affected families.

---

## Key Findings

### Finding 1 — MIP/AQP0 is the causal gene; inheritance is autosomal dominant

Cataract 15 (MONDO:0014110; OMIM 615274) is caused by mutations in **MIP** (Major Intrinsic Protein of lens fiber; gene OMIM 154050; HGNC MIP; chromosome 12q13.3), which encodes **Aquaporin-0 (AQP0/MP26)**, the most abundant membrane protein of lens fiber cells (~45% of fiber membrane protein). A 2021 systematic review catalogued **29 distinct MIP mutations** causing congenital cataract. Inheritance is **autosomal dominant** with reported variable expressivity. Reported pathogenic variants span missense (e.g., p.E134G, p.T138R, p.P191R [c.572C>G], p.G212R [c.634G>C]), frameshift (e.g., p.K228fs), and other classes, clustering in transmembrane helices H4/H5/H6, the C-terminal intracellular domain (C-TID), and extracellular loop C.

> *"Mutations in the AQP0 gene in human and mice result in genetic cataracts"* — [PMID: 19096783](https://pubmed.ncbi.nlm.nih.gov/19096783/)

> *"A total of 29 MIP gene mutations causing congenital cataract were obtained"* and *"most of them caused amino acid codon changes in the H4, H5, H6, C-TIDs, and loop C in the structure of the MIP protein"* — [PMID: 32920712](https://pubmed.ncbi.nlm.nih.gov/32920712/)

**Evidence source:** human clinical genetics + systematic review.

### Finding 2 — Dual water-channel/adhesion function and a dominant-negative mistrafficking mechanism

AQP0 functions both as a **water channel** (open configuration) and a **cell-to-cell adhesion (CTCA) molecule** (closed/junctional configuration), maintaining the narrow intercellular space, Y-suture formation, and refractive-index gradient required for lens transparency. Functional studies of human mutations (p.P191R, p.G212R, p.K228fs) consistently show that the mutant protein **fails to reach the plasma membrane and is retained in the cytoplasm**, with reduced water-transport activity (Xenopus oocyte / cell swelling assays) — consistent with a **dominant-negative / loss-of-function** mechanism in heterozygotes.

Mouse *Aqp0* knockout (AQP0−/−) lenses are cataractous, lack Y sutures and ordered fiber packing, and show wide extracellular spaces. Heterozygous AQP0+/− lenses show ~50% reduced water permeability, light scattering, spherical aberration, and cataract. Critically, restoring water permeability with transgenic AQP1 does **not** fully restore transparency, demonstrating that the **adhesion/structural role is independent and essential**.

> *"Crystallography studies support the notion of the double function of aquaporin 0 as a water channel (open configuration) or adhesion molecule (closed configuration) in the ocular lens fibers"* — [PMID: 19096783](https://pubmed.ncbi.nlm.nih.gov/19096783/)

> *"WT MIP protein predominantly localized on the plasma membrane, the mutant protein was rich in the cytoplasm"* — [PMID: 29947569](https://pubmed.ncbi.nlm.nih.gov/29947569/)

> *"AQP0(-/-) lenses were cataractous, lacked 'Y' sutures, ordered packing and well-defined lateral interdigitations"* — [PMID: 21511033](https://pubmed.ncbi.nlm.nih.gov/21511033/)

> *"the more efficient water channel AQP1 transgenically expressed in the fiber cells compensate and restore lens transparency in the AQP0 knockout"* (tested; did not fully restore transparency) — [PMID: 20599966](https://pubmed.ncbi.nlm.nih.gov/20599966/)

**Evidence source:** in vitro functional studies + mouse models + structural biology.

### Finding 3 — Clinical phenotype: bilateral congenital/childhood AD cataract with variable morphology

The first MIP mutations (Berry et al., *Nat Genet* 2000) linked to chromosome 12q were missense changes (p.E134G and p.T138R) causing autosomal dominant **'polymorphic'** and **lamellar** cataracts. Francis et al. (2000) described the polymorphic phenotype: bilateral discrete **progressive punctate** opacities limited to mid/peripheral lamellae with asymmetric polar opacification; intrafamilial variation included cortical and serpiginous nuclear opacities — i.e., **variable expressivity even within one family**. Subsequent families show nuclear, cortical punctate ± Y-suture, and lamellar forms. Cataracts are typically **bilateral, congenital or early-childhood onset, and progressive**.

Suggested **HPO terms**: Cataract (HP:0000518), Congenital cataract (HP:0000519), Nuclear cataract (HP:0100018), Lamellar/zonular cataract (HP:0010920), Cortical cataract (HP:0100019), Punctate cataract, Visual impairment (HP:0000505), Autosomal dominant inheritance (HP:0000006).

> *"we report the identification of the first mutations affecting the major intrinsic protein of the lens, MIP"* — [PMID: 10802646](https://pubmed.ncbi.nlm.nih.gov/10802646/)

> *"Affected individuals had bilateral discrete progressive punctate lens opacities limited to mid and peripheral lamellae with additional asymmetric polar opacification"* and *"The pattern of opacification appears to reflect the distribution of MIP in the lens"* — [PMID: 11090476](https://pubmed.ncbi.nlm.nih.gov/11090476/)

**Evidence source:** human clinical.

### Finding 4 — Animal models recapitulate MIP cataract; allele behavior distinguishes dominant-negative from true-null

Multiple orthologous models exist:

- **Mouse:** *Aqp0/Mip* knockout (AQP0−/− cataractous; AQP0+/− heterozygous cataract — **dominant**); historic *Cat-Fr* (insertion) and *Lop* alleles; and the **Nodai cataract (Nat)** mouse carrying a c.631G>A missense *Mip* mutation causing early-onset **semi-dominant** nuclear cataracts.
- **Rat:** KFRS4/Kyo carries a 5-bp *Mip* insertion producing a frameshift/truncation that inactivates MIP (no immunoreactivity); homozygotes develop nuclear cataract with disorganized/vacuolated fibers by 1 month, but **heterozygotes remain clear up to 1 year** — i.e., a **true null allele behaves recessively**. This contrasts with human disease, where most pathogenic missense alleles act dominant-negatively by mistrafficking and co-retaining the wild-type subunit.
- **Zebrafish:** two paralogues (*aqp0a*/*aqp0b*) with divergent adhesion vs water-permeability roles, where a single extracellular residue (position 110) underlies adhesive differences.

Orthologues: mouse *Mip* (NCBI Gene 17339), rat *Mip*, zebrafish *aqp0a*/*aqp0b*; human *MIP* (NCBI Gene 4284).

> *"the kfrs4/+ heterozygotes showed reduced expression of Mip mRNA"* and *"the lenses of kfrs4/kfrs4 homozygotes showed severely disorganised fibres and vacuolation"* — [PMID: 23226368](https://pubmed.ncbi.nlm.nih.gov/23226368/)

> *"The Nodai cataract (Nat) mice harbor a spontaneous mutation in Mip and develop early-onset nuclear cataracts"* — [PMID: 28442635](https://pubmed.ncbi.nlm.nih.gov/28442635/)

**Evidence source:** model organism.

### Finding 5 — Diagnosis and epidemiology

Diagnosis is **clinical** (slit-lamp biomicroscopy, red reflex, retroillumination documenting bilateral lens opacities) plus **molecular confirmation**. In a 20-year US pediatric congenital cataract cohort, diagnostic yield was **46.2% for whole-exome sequencing** and **37.5% for targeted congenital-cataract gene panels**, while chromosomal microarray yielded only **11%**. A Dutch vision gene-panel/exome study achieved **33% yield** in cataract patients. All-pediatric cataract incidence is ~**2.2/10,000 births** (Australian cohort), with a literature range of ~1–6/10,000; ~¼ of bilateral cases are inherited, most commonly autosomal dominant. MIP accounts for a minority of inherited cataract (crystallin genes are most common, then connexins GJA3/GJA8).

AQP0 adopts the conserved MIP **'hourglass' fold** of six transmembrane helices plus two half-helices with NPA motifs and an aromatic/arginine (ar/R) selectivity filter — the structural context in which pathogenic residues (H4–H6, loop C) sit.

> *"Whole exome sequencing and targeted congenital cataract panels showed diagnostic yields of 46.2% and 37.5%, respectively. Microarray had the lowest yield at 11%"* — [PMID: 36980880](https://pubmed.ncbi.nlm.nih.gov/36980880/)

> *"421 patients with paediatric cataract were identified, which gives an estimated incidence of 2.2 per 10,000 births"* — [PMID: 12084750](https://pubmed.ncbi.nlm.nih.gov/12084750/)

> *"MIPs adopt a unique conserved hourglass helical fold consisting of six transmembrane helices (TM1-TM6) and two half-helices (LB and LE)"* — [PMID: 25950979](https://pubmed.ncbi.nlm.nih.gov/25950979/)

**Evidence source:** human clinical + structural/computational.

### Finding 6 — Non-syndromic, surgically treatable disease with normal life expectancy

Cataract 15 affects only the ocular lens (UBERON:0000965), is **not life-limiting** (normal life expectancy, zero disease-specific mortality), and has **no pharmacological or gene/cell/RNA therapy**. Definitive management is surgical **lensectomy ± intraocular lens** (NCIT:C15277 Cataract Surgery), with the critical intervention window being early infancy to prevent **deprivation amblyopia**: recommended timing is within ~**8 weeks** (unilateral) and by ~**4 months** (bilateral). Infant options include IOL implantation vs primary aphakia with contact-lens/spectacle correction, complicated by ongoing axial-length growth and risks of glaucoma, posterior-capsule/visual-axis opacification, strabismus, and nystagmus. Prevention is **secondary** (universal newborn red-reflex screening) and **reproductive** (genetic counseling, prenatal/preimplantation testing in known-variant AD families, ~50% transmission risk). There is no environmental/infectious etiology, no established modifier gene, no somatic origin, and no disease-specific biomarker.

> *"The recommended surgical timing is within 8 weeks for unilateral cases and by 4 months for bilateral cases to minimize long-term visual impairment"* — [PMID: 40193670](https://pubmed.ncbi.nlm.nih.gov/40193670/)

> *"Two options currently considered for children under 2 years of age with bilateral congenital cataracts are: (i) intraocular lens (IOL) implantation; or (ii) leaving a child with primary aphakia"* — [PMID: 36107778](https://pubmed.ncbi.nlm.nih.gov/36107778/)

**Evidence source:** human clinical + guidelines.

---

## Full Section-by-Section Report

### 1. Disease Information

Cataract 15 is a rare, non-syndromic, **autosomal dominant congenital/early-childhood cataract** — a clouding of the ocular lens caused by mutations in a single gene, **MIP/AQP0**. The lens opacity disrupts the passage and focusing of light on the retina, producing visual impairment that, if untreated during the critical period of visual development, leads to deprivation amblyopia and permanent vision loss.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014110 |
| OMIM (phenotype) | #615274 |
| Causal gene | MIP (HGNC: MIP) |
| Gene OMIM | 154050 |
| NCBI Gene (human MIP) | 4284 |
| UniProt (AQP0 human) | P30301 |
| Chromosomal locus | 12q13.3 |
| ICD-10 | Q12.0 (congenital cataract) |
| ICD-11 | LD2E.0 / 9B10 (congenital lens opacity) |
| MeSH | Cataract (D002386) |
| Affected organ | Lens (UBERON:0000965) |

**Synonyms / alternative names:** "Cataract 15, multiple types"; MIP-related congenital cataract; AQP0-related cataract; autosomal dominant "polymorphic" cataract; lamellar cataract linked to 12q. MIP protein synonyms: Aquaporin-0, AQP0, MP26, MP28, Major Intrinsic Protein of lens fiber.

**Information source:** Aggregated disease-level resources (OMIM, Orphanet, MONDO) plus individual family case reports in the primary literature — not EHR-derived.

### 2. Etiology

**Primary cause:** A heterozygous germline mutation in **MIP** (Finding 1). The disease is **purely genetic (Mendelian, monogenic)**; there is **no environmental, infectious, toxic, or mechanistic co-cause**.

**Genetic risk factors:** The causal variants themselves — predominantly missense substitutions clustering in transmembrane helices H4–H6, extracellular loop C, and the C-terminal intracellular domain, plus frameshift/truncating variants (Finding 1). No independent susceptibility loci or modifier genes have been established for Cataract 15.

**Environmental risk factors / protective factors / gene-environment interactions:** **Not applicable.** This is a deterministic Mendelian disorder; no environmental risk or protective factors, dietary modifiers, or GxE interactions have been described. (This contrasts sharply with common age-related cataract, where UV exposure, smoking, diabetes, and corticosteroids are relevant — none of which pertain to the Mendelian MIP form.)

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Severity/Progression | Frequency |
|---|---|---|---|---|---|
| Lens opacity (cataract) | Clinical sign | HP:0000518 | Congenital–childhood | Progressive | Obligate (100%) |
| Congenital cataract | Clinical sign | HP:0000519 | Birth | Progressive | Common |
| Bilateral involvement | Clinical sign | — | Congenital | Usually symmetric–asymmetric | Typical |
| Nuclear cataract | Clinical sign | HP:0100018 | Congenital | Progressive | Subset of families |
| Lamellar/zonular cataract | Clinical sign | HP:0010920 | Congenital–childhood | Progressive | Subset |
| Cortical punctate cataract (± Y-suture) | Clinical sign | HP:0100019 | Childhood | Progressive | Subset |
| Polymorphic cataract | Clinical sign | — | Congenital–childhood | Progressive | Subset |
| Visual impairment | Symptom | HP:0000505 | Follows opacity | Variable | Depends on density/location |

Morphology is **highly variable (variable expressivity)** even within a single family (Finding 3). **Quality-of-life impact:** when dense and bilateral, visually significant cataract in infancy threatens normal visual-cortical development, carrying risk of lifelong amblyopia; timely surgery generally yields good functional outcomes, though with ongoing refractive and amblyopia management.

### 4. Genetic / Molecular Information

- **Causal gene:** MIP (AQP0), 12q13.3; gene OMIM 154050; NCBI Gene 4284; UniProt P30301.
- **Variant spectrum:** ~29 distinct reported mutations (Finding 1). Representative variants:

| Variant (protein) | cDNA | Type | Phenotype | Functional consequence |
|---|---|---|---|---|
| p.E134G | — | Missense | Polymorphic/AD | Lens opacity; 12q linkage (landmark) |
| p.T138R | — | Missense | Lamellar/AD | Lens opacity; 12q linkage (landmark) |
| p.P191R | c.572C>G | Missense | Congenital | Cytoplasmic retention, reduced membrane targeting |
| p.G212R | c.634G>C | Missense | Cortical punctate ± Y-suture | Cytoplasmic retention, reduced protein level |
| p.K228fs (K228fs230X) | c.682_683delAA | Frameshift/truncation | Nuclear/cortical | Instability, cytoplasmic trapping |

- **Variant classification (ACMG/AMP):** Reported pathogenic/likely pathogenic based on co-segregation, absence from population databases, in-silico damaging predictions, and functional mistrafficking evidence.
- **Allele frequency:** Pathogenic alleles are **absent or ultra-rare** in gnomAD/1000 Genomes (private family variants).
- **Origin:** **Germline**, heterozygous. No somatic/COSMIC role.
- **Functional consequence:** Predominantly **dominant-negative** via misfolding and cytoplasmic retention that co-retains the wild-type subunit in the AQP0 tetramer; net loss of both water-channel and adhesion function (Finding 2).
- **Modifier genes:** None established for the human disease. (In mouse, genetic background — e.g., presence/absence of beaded-filament proteins CP49/filensin in FVB vs C57 strains — modulates severity, an experimental modifier observation.)
- **Epigenetic information:** No disease-specific methylation/histone changes reported. Lens-specific *Mip* regulation involves Pax6 and open/closed chromatin dynamics during fiber differentiation (ATAC-seq studies), but no epigenetic lesion causes Cataract 15.
- **Chromosomal abnormalities:** None; this is a single-nucleotide/small-indel disorder, not a structural/CNV disorder (chromosomal microarray yield is low, ~11%).

### 5. Environmental Information

**Not applicable.** No environmental factors, toxins, radiation, occupational exposures, lifestyle factors, or infectious agents contribute to MIP-related Cataract 15. The disease is fully determined by the inherited MIP variant.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous **MIP missense (or truncating) mutation** alters an AQP0 residue, typically in TM helix H4/H5/H6, extracellular loop C, or the C-terminal intracellular domain → **leads to** a misfolded AQP0 subunit (demonstrated in vitro).
2. The misfolded subunit **fails ER/Golgi quality control and does not traffic to the plasma membrane**, accumulating in the cytoplasm → **results in** reduced membrane AQP0 (demonstrated for p.P191R, p.G212R, p.K228fs).
3. Because AQP0 assembles as a **tetramer**, the mislocalized mutant subunit **co-retains wild-type subunits** → **leads to** a dominant-negative reduction in functional membrane AQP0 below the ~50% haploinsufficiency threshold (inferred from heterozygote severity exceeding simple half-dose, and from mouse/rat allele comparisons).
4. Loss of functional AQP0 **simultaneously removes two activities** → the mechanism **branches**:
   - **Branch A (water channel):** reduced transmembrane water permeability → **impairs** the lens microcirculation/homeostasis → osmotic imbalance and light scattering (mouse AQP0+/− shows ~50% reduced Pf, spherical aberration).
   - **Branch B (cell-to-cell adhesion):** loss of AQP0-mediated fiber-cell adhesion → **leads to** widened extracellular spaces, failure of ordered fiber packing, loss of Y sutures, and disruption of the refractive-index gradient (RING) (mouse AQP0−/− lacks Y sutures; AQP1 rescue of water permeability fails to restore transparency, isolating the adhesion deficit as independently essential).
5. Branches A and B **converge** → disrupted fiber-cell architecture and refractive homogeneity → **results in** light scattering and lens opacity (cataract).
6. Lens opacity **results in** obstruction of the visual axis → **leads to** visual impairment and, in infancy, deprivation amblyopia (clinical manifestation).

**Molecular pathways / cellular processes:** The defect is a **membrane-protein trafficking/quality-control** problem (ER retention of misfolded polytopic membrane protein) combined with **loss of structural/adhesive integrity** of the lens fiber syncytium. Relevant GO biological processes: water transport (GO:0006833), cell-cell adhesion (GO:0098609), lens fiber cell differentiation (GO:0070306), visual perception (GO:0007601), maintenance of lens transparency. GO molecular function: water channel/aquaporin activity (GO:0015250). GO cellular component: plasma membrane (GO:0005886), integral component of membrane (GO:0016021); mutant protein mislocalizes to cytoplasm/ER (GO:0005783).

**Protein dysfunction:** AQP0 adopts the conserved MIP hourglass fold (6 TM helices + 2 half-helices bearing NPA motifs, with an aromatic/arginine selectivity filter). Pathogenic residues destabilize this fold or disrupt the extracellular adhesive surface (loop C, where P110/residue-110 governs adhesion). Dysfunction is **misfolding + mistrafficking + dominant-negative loss of function**.

**Metabolic / immune / biochemical:** No primary metabolic enzyme deficiency, immune involvement, or systemic biochemical abnormality — the lesion is a lens-restricted structural/transport membrane-protein defect. Downstream, osmotic/water-content changes and altered gap-junction coupling (AQP0 modulates lens gap junctions in the presence of beaded-filament proteins) contribute to opacity.

**Cell types involved:** lens fiber cell (CL:0000204) and lens epithelial precursor cells (CL:0002224) that differentiate into fibers. **Biological process GO terms:** GO:0070306 (lens fiber cell differentiation), GO:0006833 (water transport), GO:0098609 (cell-cell adhesion).

### 7. Anatomical Structures Affected

- **Organ:** Ocular lens (UBERON:0000965) — the *only* directly affected organ. Secondary functional consequence is on the visual system/retina-cortex pathway via image degradation; no other organ is involved (non-syndromic).
- **Body system:** Visual/ocular system exclusively.
- **Tissue/cell level:** Lens fiber cells (CL:0000204) — the differentiated, elongated, organelle-free cells that make up the lens bulk; lens epithelium (CL:0002224) as precursor. AQP0 is fiber-cell specific.
- **Subcellular level:** Normally **plasma membrane** (GO:0005886) / integral membrane (GO:0016021); in disease, mutant AQP0 is retained in the **cytoplasm/endoplasmic reticulum** (GO:0005783).
- **Localization:** Lens, **bilateral** (though opacity density/morphology can be asymmetric). Specific lens zones vary by variant (nuclear, lamellar/zonular, cortical, polar, mid-/peripheral lamellae), reflecting the distribution of AQP0.

### 8. Temporal Development

- **Onset:** **Congenital to early childhood.** Many families show opacities at birth or in infancy; some variants (e.g., K228fs) show sex-influenced onset (earlier in males, by ~1 year; later in females).
- **Onset pattern:** Insidious/chronic (not acute).
- **Progression:** Typically **slowly progressive**; discrete punctate opacities can accumulate and coalesce over time (described as "progressive punctate").
- **Course:** Chronic, lifelong (until surgical removal of the lens). Non-episodic, non-relapsing.
- **Critical period:** The **window for intervention is early infancy** — surgery within ~8 weeks (unilateral) / ~4 months (bilateral) is critical to prevent irreversible deprivation amblyopia (Finding 6). No spontaneous remission.

### 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal dominant** (AD). (The human missense alleles are dominant via dominant-negative mistrafficking; by contrast a true-null rat allele is recessive — Finding 4 — underscoring that human dominance derives from the co-retention mechanism.)
- **Penetrance:** High, generally considered complete, though with **variable expressivity** (morphology and severity differ within and between families).
- **Expressivity:** **Variable**, even intrafamilially (Finding 3).
- **Anticipation / germline mosaicism / founder effects / consanguinity:** No evidence of anticipation (not a repeat-expansion disorder); no established founder mutations; consanguinity is not relevant to a dominant disorder.
- **Carrier frequency:** Not applicable (dominant; affected individuals are heterozygous and express disease).
- **Epidemiology:** All-pediatric cataract incidence ~**2.2/10,000 births** (range ~1–6/10,000); ~¼ of bilateral cases are inherited, most commonly AD. **MIP is a minority cause** of inherited cataract (crystallins most common, then connexins GJA3/GJA8) (Finding 5). Precise prevalence of the MIP subtype specifically is not well quantified.
- **Population demographics:** Reported families are geographically broad (notably several Chinese families and the original UK/Australian linkage families). No strong ethnic predilection or sex bias established for the AD trait overall (individual variants may show sex-influenced onset).

### 10. Diagnostics

- **Clinical examination:** Slit-lamp biomicroscopy, red-reflex testing, and retroillumination document bilateral lens opacities and their morphology/zonal distribution (Finding 5).
- **Genetic testing (recommended, confirmatory):** Molecular diagnosis via **whole-exome sequencing (yield ~46%)** or **targeted congenital-cataract gene panels (~37.5%)**; chromosomal microarray is low-yield (~11%) and karyotyping/FISH are not indicated for this single-gene disorder. Single-gene MIP testing is appropriate when phenotype/linkage points to 12q. Dutch vision-panel/exome study yield in cataract ~33% (Finding 5).
- **Panels:** Congenital/pediatric cataract NGS panels (e.g., 51-gene panels) that include MIP alongside crystallins (CRYAA, CRYBB2, etc.), connexins (GJA3/GJA8), and others.
- **Biomarkers / omics / imaging:** No disease-specific biomarker, metabolomic, proteomic, or imaging signature; diagnosis rests on slit-lamp morphology + genetics.
- **Differential diagnosis:** Other inherited congenital cataracts (crystallin-, connexin-, transcription-factor-related), syndromic cataracts, metabolic cataracts (e.g., galactosemia), and infectious (congenital rubella) cataract — distinguished by systemic features, metabolic screening, and gene panel results.
- **Screening:** Universal **newborn red-reflex screening** detects congenital lens opacity; **cascade genetic testing** of at-risk relatives once a familial variant is known.

### 11. Outcome / Prognosis

- **Survival/mortality:** Normal life expectancy; **zero disease-specific mortality** (lens-restricted, non-syndromic) (Finding 6).
- **Morbidity/function:** The principal morbidity is **visual** — risk of deprivation amblyopia if untreated in the critical period. With timely surgery and amblyopia therapy, visual outcomes are generally favorable but depend on cataract density, laterality, timing of surgery, and postoperative refractive/amblyopia management.
- **Complications (chiefly surgical/postoperative):** glaucoma, posterior-capsule/visual-axis opacification, strabismus, nystagmus, and refractive changes from ongoing axial growth (Finding 6).
- **Prognostic factors:** Age at surgery (earlier within the safe window is better for visual development), laterality (bilateral vs unilateral), opacity density/location, and adherence to amblyopia therapy.

### 12. Treatment

- **Pharmacotherapy:** **None disease-modifying.** No drug reverses or prevents MIP cataract.
- **Definitive treatment — surgical:** **Lensectomy** (cataract extraction) ± **intraocular lens (IOL)** implantation (NCIT:C15277 Cataract Surgery / cataract extraction). Timing is critical: within ~**8 weeks** (unilateral) and by ~**4 months** (bilateral) to prevent amblyopia (Finding 6).
- **Optical/rehabilitative:** In infants, either primary IOL or primary aphakia with **contact-lens/spectacle** correction; subsequent **amblyopia therapy** (patching). IOL power calculation in growing eyes is challenging (axial elongation causes myopic shift).
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** **None** — not applicable/not developed.
- **Experimental:** No disease-specific clinical trials for MIP cataract; management follows general pediatric-cataract surgical and optical trial evidence.
- **Pharmacogenomics / personalized medicine:** Not applicable; "personalization" is limited to genetic counseling and reproductive options.

### 13. Prevention

- **Primary prevention:** Not possible for the Mendelian lesion itself; reproductive options (below) prevent transmission.
- **Secondary prevention:** **Universal newborn red-reflex screening** for early detection and timely surgery, preventing amblyopia.
- **Tertiary prevention:** Early surgery + amblyopia therapy + close postoperative monitoring to limit visual disability and manage complications (glaucoma, opacification).
- **Genetic counseling / reproductive:** AD inheritance with **~50% transmission risk**; options include prenatal diagnosis and **preimplantation genetic testing** in families with a known MIP variant, plus **cascade testing** of relatives.
- **Immunization / public-health / environmental / prophylaxis:** Not applicable (no infectious or environmental component).

### 14. Other Species / Natural Disease

- **Taxonomy / orthologues:** Human *MIP* (NCBI Gene 4284); mouse *Mip* (NCBI Gene 17339); rat *Mip*; zebrafish paralogues *aqp0a* and *aqp0b*. The gene and its lens function are **highly evolutionarily conserved** across vertebrates.
- **Natural disease in animals:** Spontaneous *Mip* mutations cause cataract in mice (Nat, Cat-Fr, Lop alleles) and rats (KFRS4/Kyo), establishing naturally occurring and engineered animal cataract that parallels the human disease (Finding 4).
- **Comparative pathology:** Shared histopathology of disorganized/vacuolated lens fibers, loss of ordered packing, and loss of sutures. **Key comparative insight:** dominant-negative *missense* alleles are dominant (mouse Nat, human), whereas *true-null/truncating* alleles can be recessive (rat KFRS4), clarifying the mechanism of human dominance.
- **Zoonosis / cross-species transmission:** Not applicable (genetic, non-transmissible).

### 15. Model Organisms

| Model | Allele | Inheritance | Phenotype recapitulation | Key reference |
|---|---|---|---|---|
| Mouse | *Aqp0*/*Mip* knockout (−/− and +/−) | Dominant (+/− cataract) | Cataract, no Y sutures, wide extracellular spaces, ~50% reduced Pf, spherical aberration | [PMID: 21511033](https://pubmed.ncbi.nlm.nih.gov/21511033/), [PMID: 20599966](https://pubmed.ncbi.nlm.nih.gov/20599966/) |
| Mouse | Nat (c.631G>A missense) | Semi-dominant | Early-onset nuclear cataract | [PMID: 28442635](https://pubmed.ncbi.nlm.nih.gov/28442635/) |
| Mouse | Cat-Fr (insertion), Lop | Dominant | Historic cataract alleles | — |
| Rat | KFRS4/Kyo (5-bp insertion, truncating null) | Recessive | Homozygote nuclear cataract, disorganized/vacuolated fibers by 1 month; heterozygotes clear to 1 yr | [PMID: 23226368](https://pubmed.ncbi.nlm.nih.gov/23226368/) |
| Zebrafish | *aqp0a*/*aqp0b* paralogues | — | Divergence of adhesion (residue 110) vs water-permeability functions | [PMID: 34440774](https://pubmed.ncbi.nlm.nih.gov/34440774/) |

- **Model types:** Mammalian (mouse, rat), teleost (zebrafish), plus in vitro cell models (HeLa/HEK transfection, Xenopus oocyte swelling assays) used to demonstrate mistrafficking and reduced water transport.
- **Phenotype recapitulation:** Strong — animal models reproduce cataract, fiber disorganization, suture loss, and the water/adhesion dual-function deficit.
- **Model limitations:** Allele behavior differs (null→recessive in rat vs dominant-negative missense in human), and genetic background (beaded-filament status) modifies severity; care is needed in extrapolating dosage effects.
- **Resources:** MGI (mouse *Mip*), RGD (rat *Mip*), ZFIN (zebrafish *aqp0a*/*aqp0b*), Cellosaurus/ATCC for cell lines.

---

## Mechanistic Model / Interpretation

```
 MIP (AQP0) heterozygous mutation (missense in H4-H6 / loop C / C-TID, or truncating)
                    |
                    v
          Misfolded AQP0 subunit  --(ER quality-control retention)--> cytoplasmic accumulation
                    |
                    v
   Tetramer co-assembly: mutant co-retains WT subunit  ==>  DOMINANT-NEGATIVE loss
                    |
        +-----------+-----------------------------+
        |                                         |
        v  BRANCH A (water channel)               v  BRANCH B (cell adhesion)
  reduced membrane water permeability       loss of fiber-fiber adhesion
  (~50% in mouse +/-)                        widened extracellular space,
        |                                     no Y sutures, disordered packing,
        v                                     disrupted refractive-index gradient
  osmotic/homeostatic imbalance                       |
        |                                             |
        +--------------------+------------------------+
                             v
                 Light scattering / lens opacity (cataract)
                             v
             Visual axis obstruction -> visual impairment
                             v
             (infancy) deprivation amblyopia if untreated
```

The decisive experiment distinguishing the two branches is the **AQP1 rescue**: transgenic AQP1 restores water permeability in AQP0-knockout mouse lenses but **fails to restore transparency** ([PMID: 20599966](https://pubmed.ncbi.nlm.nih.gov/20599966/); [PMID: 21511033](https://pubmed.ncbi.nlm.nih.gov/21511033/)), proving the **adhesion/structural function (Branch B) is independently essential**. The dominant-negative nature of human disease is corroborated by the contrast between dominant missense mouse/human alleles and the **recessive true-null rat allele** ([PMID: 23226368](https://pubmed.ncbi.nlm.nih.gov/23226368/)): a complete absence of protein behaves recessively, whereas a mistrafficking mutant that poisons the tetramer behaves dominantly.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [19096783](https://pubmed.ncbi.nlm.nih.gov/19096783/) | Structural function of MIP/AQP0; genetic defects → cataract | Causal gene; dual water-channel/adhesion function |
| [32920712](https://pubmed.ncbi.nlm.nih.gov/32920712/) | MIP genes and cataract (systematic review) | 29 mutations; structural clustering H4–H6/loop C/C-TID |
| [10802646](https://pubmed.ncbi.nlm.nih.gov/10802646/) | First MIP cataract mutations (E134G, T138R) | Landmark identification; AD polymorphic/lamellar |
| [11090476](https://pubmed.ncbi.nlm.nih.gov/11090476/) | Congenital progressive polymorphic cataract (MIP) | Progressive punctate morphology; variable expressivity |
| [29947569](https://pubmed.ncbi.nlm.nih.gov/29947569/) | Novel MIP mutation, Chinese family | Mistrafficking (cytoplasmic vs membrane) |
| [28059152](https://pubmed.ncbi.nlm.nih.gov/28059152/) | p.G212R MIP | Mistrafficking; cortical punctate ± Y-suture |
| [29695758](https://pubmed.ncbi.nlm.nih.gov/29695758/) | p.K228fs frameshift MIP | Truncation, instability, cytoplasmic trapping; sex-influenced onset |
| [21511033](https://pubmed.ncbi.nlm.nih.gov/21511033/) | AQP0 fiber architecture/transparency (mouse KO) | No Y sutures; structural/adhesion role |
| [20599966](https://pubmed.ncbi.nlm.nih.gov/20599966/) | AQP1 transgene in AQP0-KO | Water permeability alone insufficient for transparency |
| [25229686](https://pubmed.ncbi.nlm.nih.gov/25229686/) | AQP0 and refractive-index gradient | RING/spherical-aberration role |
| [28442635](https://pubmed.ncbi.nlm.nih.gov/28442635/) | Nat mouse (missense) | Dominant missense cataract model |
| [23226368](https://pubmed.ncbi.nlm.nih.gov/23226368/) | KFRS4 rat (truncating null) | Null allele recessive → dominant-negative logic |
| [34440774](https://pubmed.ncbi.nlm.nih.gov/34440774/) | Zebrafish aqp0a/aqp0b adhesion | Residue-110 adhesion; functional divergence |
| [25950979](https://pubmed.ncbi.nlm.nih.gov/25950979/) | MIP superfamily structure | Hourglass fold; selectivity filter context |
| [36980880](https://pubmed.ncbi.nlm.nih.gov/36980880/) | Genetic testing in congenital cataract (US) | WES 46.2% / panel 37.5% / CMA 11% |
| [12084750](https://pubmed.ncbi.nlm.nih.gov/12084750/) | Paediatric cataract aetiology (Australia) | Incidence ~2.2/10,000 |
| [28224992](https://pubmed.ncbi.nlm.nih.gov/28224992/) | Exome in visual impairment (Dutch) | ~33% cataract yield |
| [40193670](https://pubmed.ncbi.nlm.nih.gov/40193670/) | IOL power / pediatric cataract surgery | Surgical timing windows |
| [36107778](https://pubmed.ncbi.nlm.nih.gov/36107778/) | Surgery for bilateral congenital cataract (Cochrane) | IOL vs aphakia options/trade-offs |

---

## Limitations and Knowledge Gaps

1. **Subtype-specific epidemiology is unquantified.** Incidence/prevalence data are for pediatric cataract as a whole; the specific contribution and frequency of MIP (Cataract 15) are described only qualitatively as a "minority" cause.
2. **Genotype–phenotype correlation is incomplete.** Variable expressivity (even intrafamilial) is documented, but the determinants of which lens zone/morphology a given variant produces are not fully mapped.
3. **Dominant-negative mechanism is inferred from in vitro and cross-species data**, not directly proven for every human allele; co-retention of wild-type subunit by mutant in human lens fiber cells is a model consistent with (but not exhaustively demonstrated across) all variants.
4. **No disease-specific biomarker, omics signature, or imaging feature** exists beyond morphologic slit-lamp findings and genetics.
5. **Human modifier genes are unidentified**; strain-dependent severity (beaded-filament proteins) is a mouse observation whose human relevance is untested.
6. **No pharmacologic or molecular therapy** has been developed or trialed specifically for MIP cataract.

---

## Proposed Follow-up Experiments / Actions

1. **Variant-level functional pipeline:** Systematically express each reported MIP variant (and co-express with wild-type) in lens-relevant cells to quantify trafficking, water permeability, adhesion, and dominant-negative co-retention — directly validating the dominant-negative model per allele.
2. **Structure-guided classification:** Map all ~29 variants onto the AQP0 cryo-EM/crystal structure to build a predictive genotype→conformational-defect→morphology model, improving ACMG classification of future VUS.
3. **Registry and natural-history study** of MIP-positive families to estimate the true MIP-attributable fraction of inherited cataract, penetrance, and expressivity quantitatively.
4. **Modifier search in humans:** Test whether beaded-filament genes (BFSP1/BFSP2), connexins (GJA3/GJA8), or crystallins modify MIP cataract severity, mirroring mouse strain effects.
5. **iPSC-derived lens organoid / "lentoid" models** carrying patient MIP variants to study human-cell fiber differentiation, trafficking, and candidate correction strategies (e.g., chemical chaperones to rescue mistrafficking).
6. **Optimize surgical/optical outcomes:** Continue comparative-effectiveness work on primary IOL vs aphakia and amblyopia protocols in genetically defined MIP cataract cohorts.

---

*Report prepared from a 5-iteration autonomous investigation (6 confirmed findings; 32 papers reviewed). Evidence sources are annotated as human clinical, model organism, in vitro, or computational/structural throughout.*


## Artifacts

- [OpenScientist final report](Cataract_15-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cataract_15-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 14 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014110` (4 mentions) - the report calls it "MONDO"; MONDO calls it **cataract 15 multiple types**
- `HP:0000518` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Cataract**
- `HP:0000519` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Developmental cataract**
- `HP:0100018` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Nuclear cataract**
- `HP:0010920` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Zonular cataract**
- `HP:0100019` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Cortical cataract**
- `HP:0000505` (2 mentions) - the report calls it "Symptom"; HP calls it **Visual impairment**
- `CL:0000204` (2 mentions) - the report calls it "Tissue/cell level:** Lens fiber cells"; CL calls it **acceleration receptive cell**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016021` (GO_0016021) (2 mentions) - replaced by `GO:0016020`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000965` (3 mentions) - the report calls it "Lens", "Organ:** Ocular lens"; UBERON calls it **lens of camera-type eye**, and lists "ocular lens" among its other names
- `GO:0005886` (2 mentions) - the report calls it "plasma membrane", "Subcellular level:** Normally **plasma membrane"; GO calls it **plasma membrane**, and lists "integral to plasma membrane" among its other names
- `GO:0005783` (2 mentions) - the report calls it "cytoplasm/endoplasmic reticulum"; GO calls it **endoplasmic reticulum**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000965` - called "Lens", "Organ:** Ocular lens"
- `GO:0005886` - called "plasma membrane", "Subcellular level:** Normally **plasma membrane"