---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-14T20:46:30.655129'
end_time: '2026-09-14T21:00:51.264746'
duration_seconds: 860.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SLC35A1-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0011342
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 26
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 11
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0011342
    reported_labels:
    - MONDO
    ontology_label: SLC35A1-congenital disorder of glycosylation
  - term_id: HP:0001875
    reported_labels:
    - Laboratory
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0002719
    reported_labels:
    - Clinical
    ontology_label: Recurrent infections
  - term_id: HP:0001263
    reported_labels:
    - Clinical
    ontology_label: Global developmental delay
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0001298
    reported_labels:
    - Clinical
    ontology_label: Encephalopathy
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SLC35A1-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SLC35A1-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SLC35A1-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0011342 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SLC35A1-Congenital Disorder of Glycosylation** covering all of the
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

# SLC35A1-Congenital Disorder of Glycosylation (SLC35A1-CDG / CDG-IIf): Comprehensive Disease Characterization

**Disease:** SLC35A1-Congenital Disorder of Glycosylation
**MONDO ID:** MONDO:0011342 · **Category:** Mendelian (autosomal recessive)
**Gene:** *SLC35A1* (Golgi CMP-sialic acid transporter; HGNC:10940, chromosome 6q15) · **OMIM phenotype:** CDG-IIf
**Report date:** 2026-09-14 · Evidence base: human clinical case reports, cellular/biochemical studies, and one conditional mouse model.

---

## Summary

SLC35A1-CDG, historically designated **CDG type IIf**, is an ultra-rare autosomal recessive congenital disorder of glycosylation caused by biallelic loss-of-function of ***SLC35A1***, the gene encoding the **sole Golgi CMP–sialic acid transporter**. This transporter imports the activated sialic acid donor (CMP-Neu5Ac) from the cytosol into the Golgi lumen, where it is the substrate for the sialyltransferases that cap N-glycans, O-glycans, and glycolipids with terminal sialic acid. When the transporter fails, the Golgi is deprived of its sialic acid donor and the cell produces **globally hyposialylated glycoproteins and glycolipids**, despite normal cytosolic sialic acid synthesis. This single upstream lesion propagates into two clinically distinct but overlapping presentations.

The disease spectrum runs from a **hematologic phenotype** — macrothrombocytopenia, bleeding tendency, neutropenia, recurrent infections, and complete absence of the sialyl-Lewis-x leukocyte ligand — to a **severe neurological phenotype** — developmental delay, hypotonia, seizures, and encephalopathy. The index patient (2005) presented with the hematologic picture; the third reported patient (2017) presented with a neurological-dominant picture and *no* hematological abnormalities, establishing genotype-dependent phenotypic heterogeneity. Mechanistically, the thrombocytopenia is explained by hepatic Ashwell-Morell receptor clearance of desialylated platelets plus impaired megakaryocytopoiesis (demonstrated in a conditional mouse model), while the neurological phenotype is linked to deficient synthesis of the two major brain sialoglycan families — **gangliosides** and **polysialic acid on NCAM**.

Diagnosis rests on a **Type II serum transferrin glycoprofile** (isoelectric focusing, capillary zone electrophoresis, or high-resolution intact-transferrin mass spectrometry) followed by molecular confirmation of biallelic *SLC35A1* variants. **No targeted or curative therapy exists.** Unlike some other CDG subtypes treatable by monosaccharide supplementation (mannose for MPI-CDG, galactose for SLC35A2-CDG/PGM1-CDG, fucose for SLC35C1-CDG), sialic acid supplementation cannot bypass an SLC35A1 defect because the lesion is in Golgi *delivery* of the activated donor, not in sialic acid availability. Management is supportive. Sialidase (neuraminidase) inhibition is a mechanistically plausible but unproven candidate strategy for the desialylation-driven thrombocytopenia.

---

## 1. Disease Information

**Overview.** SLC35A1-CDG is a Type II congenital disorder of glycosylation in which defective transport of CMP-sialic acid into the Golgi apparatus produces global hyposialylation of glycoconjugates. It is a defect of glycan *processing/elaboration* (hence "Type II"), distinct from the Type I CDGs that impair assembly of the lipid-linked oligosaccharide precursor.

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0011342 |
| OMIM (phenotype) | CDG-IIf |
| Gene | *SLC35A1*, HGNC:10940; chromosome 6q15 |
| Legacy name | CDG-IIf; CMP-sialic acid transporter deficiency |
| Classification | Congenital disorder of glycosylation, Type II |

**Synonyms / alternative names:** CDG-IIf; CDG type IIf; CMP-sialic acid transporter deficiency; congenital disorder of glycosylation type 2F; SLC35A1-CDG.

**Information source.** The disease-level characterization here is derived from **aggregated disease-level resources** (OMIM, published case reports, functional studies, mouse models) rather than from individual EHR data. The clinical picture is assembled from a very small number of individually reported patients (fewer than ten worldwide since 2005), so most claims rest on single-case or small-case-series evidence supplemented by mechanistic model-organism and in-vitro work.

---

## 2. Etiology

**Primary cause — genetic.** SLC35A1-CDG is caused exclusively by **biallelic (compound heterozygous or homozygous) loss-of-function variants in *SLC35A1***. There is no environmental or infectious etiology; the disease is a monogenic inborn error of metabolism. The original 2005 report identified a patient lacking sialyl-Lewis-x on polymorphonuclear cells who carried compound heterozygous *SLC35A1* defects: one allele with a double microdeletion producing a premature stop at codon 327, the other with a splice mutation causing a 130-bp deletion and a premature stop at codon 684. Complementation studies in Lec2 cells (which lack the CMP-sialic acid transporter) showed that neither patient allele restored sialylation, whereas wild-type transcript fully restored it — establishing loss of function as causal. *"The inactivation of one patient allele by a double microdeletion inducing a premature stop codon at position 327 and a splice mutation of the other allele inducing a 130-base pair (bp) deletion and a premature stop codon at position 684 are proposed to be the causal defects of this disease."* ([PMID: 15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/)).

**Genetic risk factors.** The only risk factor is inheritance of two pathogenic *SLC35A1* alleles. Heterozygous carriers are unaffected. As an autosomal recessive Mendelian disorder, **consanguinity** and **founder effects** increase risk in specific families/populations, although the disorder is too rare for population-specific founder alleles to have been formally established.

**Environmental risk factors / protective factors / gene-environment interactions.** **Not applicable.** No environmental risk factors, protective factors, lifestyle factors, or gene-environment interactions are known or expected for this fully penetrant monogenic disorder. No protective modifier alleles have been reported.

---

## 3. Phenotypes

SLC35A1-CDG presents along a spectrum with two overlapping symptom clusters. The index CDG-IIf patient presented with **macrothrombocytopenia, neutropenia, and complete lack of sialyl-Lewis-x** ([PMID: 27387429](https://pubmed.ncbi.nlm.nih.gov/27387429/)). A subsequently reported (third) patient carried compound heterozygous missense variants p.Thr156Arg and p.Glu196Lys and presented with a **profound neurological phenotype (encephalopathy) without hematological abnormalities** ([PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)).

| Phenotype | Type | HPO term (suggested) | Onset | Severity / course |
|-----------|------|----------------------|-------|-------------------|
| Macrothrombocytopenia | Laboratory / hematologic | HP:0011897 (thrombocytopenia); HP:0040326 (giant platelets) | Congenital/neonatal | Variable; may be presenting feature |
| Bleeding tendency | Clinical sign | HP:0001892 (abnormal bleeding) | Congenital | Variable |
| Neutropenia | Laboratory | HP:0001875 | Congenital/neonatal | Variable |
| Recurrent infections | Clinical | HP:0002719 | Infancy | Related to neutropenia / absent sLeˣ |
| Absent sialyl-Lewis-x | Laboratory/biochemical | — | Congenital | Constant (biochemical hallmark) |
| Developmental delay | Clinical | HP:0001263 | Infancy | Severe in neurological form |
| Hypotonia | Clinical sign | HP:0001252 | Neonatal/infancy | Common |
| Seizures | Clinical sign | HP:0001250 | Infancy | Present in encephalopathic form |
| Encephalopathy | Clinical | HP:0001298 | Infancy | Severe, progressive |

**Phenotype characteristics.** Onset is **congenital/neonatal to early infancy**. Severity is **variable and genotype-influenced**: null/truncating biallelic genotypes are associated with the hematologic-dominant picture, whereas hypomorphic missense genotypes (e.g., T156R/E196K) have been associated with the severe neurological-dominant picture. Frequency data across affected individuals cannot be quantified reliably given the very small number of reported patients; features are described qualitatively.

**Quality of life impact.** In the neurological form, encephalopathy, seizures, and severe developmental delay produce profound impairment of daily functioning and lifelong dependency. In the hematologic form, bleeding risk and infection susceptibility dominate. Formal QoL instruments (EQ-5D, SF-36, PROMIS) have not been applied to this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***SLC35A1*** (solute carrier family 35 member A1; HGNC:10940), encoding the Golgi CMP–sialic acid transporter, a multipass transmembrane nucleotide-sugar transporter of the SLC35 family.

**Pathogenic variants reported:**

| Variant | Type | Consequence | Clinical association |
|---------|------|-------------|----------------------|
| Double microdeletion → stop at codon 327 | Frameshift/truncating | Loss of function | Index case, hematologic ([PMID: 15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/)) |
| Splice mutation → 130-bp deletion, stop at codon 684 | Splice/truncating | Loss of function | Index case, hematologic ([PMID: 15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/)) |
| p.Thr156Arg (T156R) | Missense | Reduced transport | Third case, neurological ([PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)) |
| p.Glu196Lys (E196K) | Missense | Reduced transport; disrupts ST3Gal4 coupling | Third case, neurological ([PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/); [PMID: 36257191](https://pubmed.ncbi.nlm.nih.gov/36257191/)) |

**Variant classification.** Reported variants are pathogenic/likely pathogenic per ACMG criteria, supported by functional complementation assays. Population allele frequencies (gnomAD) for pathogenic *SLC35A1* alleles are extremely low, consistent with an ultra-rare recessive disorder.

**Functional consequences.** All disease variants are **loss-of-function** (either complete via truncation or partial/hypomorphic via missense reduction of transport activity). Structure-guided mutagenesis has defined three substrate pockets in SLC35A1 — **nucleobase (E52, K55, Y214), middle (Q101, N102, T260), and sugar (K124, T128, S188, K272)** — with Y214 discriminating cytosine from uracil. *"The pockets comprise (1) nucleobase (residues E52, K55, and Y214 of SLC35A1…"* ([PMID: 34384782](https://pubmed.ncbi.nlm.nih.gov/34384782/)). Beyond transport, SLC35A1 physically associates with the α2,3-sialyltransferase **ST3Gal4**; the CDG-causing **E196K mutation (but not T156R) disrupts this interaction** and E196K is less efficient at restoring N-glycan sialylation in SLC35A1-knockout cells: *"This phenomenon is compromised by the E196K (but not T156R) mutation in the SLC35A1 gene. We also demonstrated that the E196K mutant is less efficient in restoring N-glycan sialylation upon expression in the SLC35A1 knockout cells."* ([PMID: 36257191](https://pubmed.ncbi.nlm.nih.gov/36257191/)). This shows that some missense variants impair sialylation both by reducing transport and by decoupling the transporter from the sialyltransferase machinery.

**Modifier genes, epigenetics, chromosomal abnormalities.** No modifier genes, epigenetic mechanisms, or chromosomal-scale abnormalities have been established for SLC35A1-CDG. Origin is germline; somatic contribution is not applicable.

---

## 5. Environmental Information

**Not applicable.** SLC35A1-CDG is a purely monogenic disorder. No environmental factors, toxins, lifestyle factors, or infectious agents cause or trigger the disease. Recurrent infections in affected individuals are a *consequence* of neutropenia and absent leukocyte sialyl-Lewis-x adhesion ligands, not an etiologic agent.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in *SLC35A1*** → **loss/reduction of functional Golgi CMP–sialic acid transporter** protein (demonstrated by complementation failure in Lec2 cells; [PMID: 15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/)).
2. Loss of transporter → **failure to import CMP-Neu5Ac (the activated sialic acid donor) from cytosol into the Golgi lumen** (direct: reduced Golgi CMP-sialic acid transport rate measured in patient fibroblasts; [PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)).
3. Golgi donor depletion → **sialyltransferases (e.g., ST3Gal4) cannot cap glycans**, leading to **global hyposialylation of N-glycans, O-glycans, and glycolipids** (direct: decreased sialylated N-/O-glycans in patient serum and fibroblasts; [PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)). Some missense variants (E196K) additionally **decouple SLC35A1 from ST3Gal4**, worsening the sialylation defect ([PMID: 36257191](https://pubmed.ncbi.nlm.nih.gov/36257191/)).
4. Hyposialylation then **branches** into tissue-specific consequences:

   **Branch A — Hematologic:**
   - 4A-i. Loss of terminal sialic acid on platelet surface glycoproteins **exposes subterminal galactose** → recognition by **hepatocyte Ashwell-Morell receptors** → **Fc-independent hepatic platelet clearance** (inferred for SLC35A1-CDG from the general desialylation-clearance mechanism; demonstrated directly in ITP models; [PMID: 26185093](https://pubmed.ncbi.nlm.nih.gov/26185093/)).
   - 4A-ii. In parallel, hyposialylation **impairs megakaryocytopoiesis** — reduced bone marrow megakaryocyte numbers and impaired maturation — with excess desialylated platelets cleared by **hepatic Kupffer cells** (direct, mouse model; [PMID: 32303557](https://pubmed.ncbi.nlm.nih.gov/32303557/)).
   - 4A-iii. → **Macrothrombocytopenia, bleeding, neutropenia, absent leukocyte sialyl-Lewis-x → recurrent infections.**

   **Branch B — Neurological:**
   - 4B-i. Loss of Golgi sialic acid delivery **impairs synthesis of the two major brain sialoglycan families — gangliosides and polysialic acid on NCAM** (inferred from the essential requirement of these glycans for sialic acid; [PMID: 24692354](https://pubmed.ncbi.nlm.nih.gov/24692354/)).
   - 4B-ii. Ganglioside deficiency **disrupts axon-myelin interactions, axon stability/regeneration, and neuronal excitability**; polySia-NCAM deficiency **disrupts neurite outgrowth, synaptic connectivity, and memory formation** ([PMID: 24692354](https://pubmed.ncbi.nlm.nih.gov/24692354/); [PMID: 22585926](https://pubmed.ncbi.nlm.nih.gov/22585926/)).
   - 4B-iii. → **Developmental delay, hypotonia, seizures, encephalopathy.**

```
 SLC35A1 biallelic LoF
          │
   ↓ functional Golgi CMP-sialic acid transporter
          │
   ✗ CMP-Neu5Ac import into Golgi lumen
          │
   Global HYPOSIALYLATION (N-/O-glycans, glycolipids)
          │
   ┌──────┴───────────────────────────┐
   │ BRANCH A (hematologic)            │ BRANCH B (neurological)
   │                                   │
 Desialylated platelets             Deficient gangliosides +
   │                                 polySia-NCAM
 Ashwell-Morell (hepatocyte) +        │
 Kupffer cell clearance;            Impaired axon-myelin,
 impaired megakaryocytopoiesis      synaptic connectivity,
   │                                 excitability
 Macrothrombocytopenia,              │
 neutropenia, absent sLeˣ          Developmental delay,
   │                                 hypotonia, seizures,
 Bleeding, infections               encephalopathy
```

### Detail by category

- **Molecular pathways / biochemical abnormality.** The core defect is in the **sialylation branch of the glycosylation pathway** (KEGG/Reactome: "Sialic acid metabolism"; Reactome "Transport of nucleotide sugars"). The specific biochemical lesion is **failure of CMP-sialic acid (CMP-Neu5Ac) antiport into the Golgi**, upstream of all sialyltransferase reactions.
- **Protein dysfunction.** Loss of function of a multipass Golgi membrane transporter, via truncation or hypomorphic missense changes mapping to defined substrate pockets; some missense variants also disrupt a protein-protein interaction with ST3Gal4.
- **Cellular processes.** Impaired megakaryocyte maturation (hematopoiesis); increased platelet clearance (phagocytosis/endocytic clearance); impaired neuronal differentiation/connectivity.
- **Metabolic changes.** Altered glycoconjugate metabolism — deficiency of sialylated glycolipids (gangliosides) and glycoproteins; cytosolic sialic acid synthesis remains intact.
- **Immune involvement.** Secondary immunodeficiency: neutropenia plus loss of sialyl-Lewis-x (the selectin ligand mediating leukocyte rolling/adhesion) impairs leukocyte trafficking → recurrent infections.
- **Molecular profiling.** Patient serum and fibroblast glycomics show markedly decreased N- and O-glycans terminating in sialic acid ([PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)); intact-transferrin high-resolution mass spectrometry detects a Type II pattern ([PMID: 26307094](https://pubmed.ncbi.nlm.nih.gov/26307094/)).

**Suggested GO / CL terms.** GO:0015739 (sialic acid transport), GO:0008373 (sialyltransferase activity), GO:0006486 (protein glycosylation), GO:0005794 (Golgi apparatus), GO:0000139 (Golgi membrane). Cell types (CL): CL:0000556 (megakaryocyte), CL:0000233 (platelet), CL:0000775 (neutrophil), CL:0000540 (neuron).

---

## 7. Anatomical Structures Affected

**Organ / system level.**
- **Hematopoietic / blood system** (UBERON:0002390 hematopoietic system; UBERON:0000178 blood): platelets, megakaryocytes, neutrophils.
- **Liver** (UBERON:0002107): site of desialylated-platelet clearance via Ashwell-Morell receptors (hepatocytes) and Kupffer cells.
- **Central nervous system / brain** (UBERON:0000955): primary target in the neurological form.
- **Bone marrow** (UBERON:0002371): impaired megakaryocytopoiesis.

**Tissue and cell level.** Megakaryocytes (CL:0000556) and platelets (CL:0000233); neutrophils/polymorphonuclear cells (CL:0000775); neurons and glia in the CNS; hepatocytes (CL:0000182) and Kupffer cells (CL:0000091) as clearance sites.

**Subcellular level.** The primary lesion is at the **Golgi apparatus membrane** (GO:0000139 Golgi membrane; GO:0005794 Golgi apparatus). Downstream, glycolipid/ganglioside deficits affect **plasma membrane** composition (GO:0005886).

**Localization / lateralization.** Systemic and bilateral; no lateralization. The disorder is multisystem, reflecting the ubiquitous requirement for sialylation.

---

## 8. Temporal Development

- **Onset:** Congenital; clinical manifestations appear in the **neonatal period to early infancy**. Onset pattern is chronic/insidious for developmental features and can be acute for bleeding or infection episodes.
- **Progression:** In the neurological form, encephalopathy and developmental impairment are severe and effectively lifelong; disease course is progressive to stable-severe. In the hematologic form, thrombocytopenia and infection susceptibility persist chronically.
- **Duration:** Chronic, lifelong.
- **Critical periods:** Early infancy is the window in which neurodevelopmental sialoglycan requirements (ganglioside and polySia-NCAM–dependent synaptogenesis) are greatest, making this the theoretical window of vulnerability and, hypothetically, of intervention.

---

## 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (biallelic *SLC35A1* loss-of-function; [PMID: 15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/)).
- **Penetrance / expressivity:** Effectively complete penetrance in biallelic carriers; **variable expressivity** across the hematologic–neurological spectrum, influenced by genotype (null vs hypomorphic missense).
- **Epidemiology:** **Ultra-rare.** Only a handful of patients reported worldwide since 2005; the 2017 encephalopathy report described its subject as *"the third patient with CMP-sialic acid transporter deficiency"* ([PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)). Precise prevalence/incidence cannot be estimated. For context, aggregate CDG screening in Tunisia over 15 years estimated total CDGS incidence at ~1:23,720 live births (4.21/100,000), of which SLC35A1-CDG would be a minute fraction ([PMID: 38262859](https://pubmed.ncbi.nlm.nih.gov/38262859/)).
- **Carrier frequency / founder effects:** Not established; extremely low based on gnomAD rarity of pathogenic alleles. Consanguinity would increase homozygous risk.
- **Demographics:** No sex predilection (autosomal); no established ethnic or geographic clustering given the small number of cases.

---

## 10. Diagnostics

**First-line biochemical screen.** Plasma **transferrin glycoform analysis** — isoelectric focusing (IEF), capillary zone electrophoresis (CZE), or high-resolution mass spectrometry. SLC35A1-CDG produces a **Type II (CDG-II) transferrin pattern**, reflecting defective glycan sialylation/processing rather than whole-glycan loss. **High-resolution intact-transferrin mass spectrometry** can directly detect and subtype the SLC35A1-CDG defect among CDG-II disorders; SLC35A1-CDG is explicitly listed among *"Known CDG-II defects (phosphoglucomutase 1 [PGM1-CDG], … [MGAT2-CDG], … [B4GALT1-CDG], CMP-sialic acid transporter [SLC35A1-CDG]…"* ([PMID: 26307094](https://pubmed.ncbi.nlm.nih.gov/26307094/)).

**Confirmatory glycomics.** Serum/fibroblast N- and O-glycan profiling shows markedly decreased sialylated species; assay of Golgi CMP-sialic acid transport rate in patient fibroblasts is reduced ([PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)).

**Specialized markers.** Absent/decreased **sialyl-Lewis-x** on polymorphonuclear cells is a distinctive biochemical hallmark in the hematologic form ([PMID: 27387429](https://pubmed.ncbi.nlm.nih.gov/27387429/)).

**Hematology.** CBC with platelet indices (macrothrombocytopenia, giant platelets), neutrophil count (neutropenia), and peripheral smear.

**Genetic testing.** Molecular confirmation of **biallelic *SLC35A1* variants** is definitive. Recommended approach: exome or genome sequencing, or a targeted CDG/glycosylation gene panel that includes *SLC35A1*; complementation assays (as in Lec2 cells) can functionally confirm novel variants ([PMID: 15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/)). Chromosomal microarray, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not applicable**.

**Clinical criteria / differential diagnosis.** No disease-specific consensus criteria exist; diagnosis follows the general CDG workup (abnormal transferrin glycoform → glycan analysis → molecular confirmation). Differential diagnosis includes other CDG-II subtypes (PGM1-CDG, MGAT2-CDG, B4GALT1-CDG, SLC35A2-CDG), inherited thrombocytopenias/macrothrombocytopenias, and other genetic encephalopathies.

**Screening.** Not part of routine newborn screening. Carrier and cascade testing are appropriate in families with a known pathogenic genotype.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Formal survival statistics are unavailable given ultra-rarity. The severe neurological form carries a guarded prognosis with substantial morbidity; the hematologic form's prognosis is dominated by bleeding and infection risk.
- **Morbidity/disability:** In the neurological form, profound and lifelong developmental disability, seizures, and encephalopathy. In the hematologic form, bleeding tendency and infection susceptibility.
- **Complications:** Hemorrhage (thrombocytopenia), recurrent/severe infections (neutropenia + adhesion defect), seizures, and developmental sequelae.
- **Recovery potential:** Limited; the underlying transport defect is not correctable, so outcomes reflect symptomatic burden.
- **Prognostic factors:** Genotype (null vs hypomorphic), predominant organ system, seizure control, and infection/bleeding management. No validated prognostic biomarkers exist.

---

## 12. Treatment

**No targeted or curative therapy exists.** Management is **supportive and symptomatic**:
- **Hematologic support:** transfusion and bleeding precautions for thrombocytopenia; infection prophylaxis/treatment and management of neutropenia.
- **Neurological support:** anti-seizure medication; developmental, physical, occupational, and speech therapy; supportive/palliative care.
- **Nutrition:** general CDG nutritional support.

**Why monosaccharide supplementation does not work here.** Reviews of CDG therapeutics emphasize that among 160+ CDG subtypes few have specific therapy, and available treatments are largely **dietary monosaccharide/precursor supplementation** — e.g., mannose (MPI-CDG/PMM2-CDG trials), galactose (SLC35A2-CDG, PGM1-CDG), fucose (SLC35C1-CDG). *"Patients present with a wide range of symptoms and therapies are only available for very few subtypes. Specific nutritional treatment options for certain CDG types include oral supplementation of monosaccharide sugars, manganese, uridine, or pyridoxine."* ([PMID: 35562242](https://pubmed.ncbi.nlm.nih.gov/35562242/)); *"Although the number of identified CDG is growing rapidly, there are few therapeutic options. Most treatments involve dietary supplementation with monosaccharides or other precursors."* ([PMID: 34788024](https://pubmed.ncbi.nlm.nih.gov/34788024/)). For SLC35A1-CDG, **sialic acid (Neu5Ac) supplementation cannot readily bypass the defect** because the lesion is in Golgi *delivery* of the activated CMP-sialic acid donor, not in cytosolic sialic acid availability. No supplementation therapy is established for this subtype.

**Candidate/experimental strategy.** Because the thrombocytopenia is driven by clearance of desialylated platelets, **sialidase (neuraminidase) inhibition** is a mechanistically rational candidate: *"sialidase inhibitors ameliorate anti-GPα-mediated thrombocytopenia in mice."* ([PMID: 26185093](https://pubmed.ncbi.nlm.nih.gov/26185093/)). This has **not** been tested in SLC35A1-CDG and is hypothetical. Gene therapy and other advanced therapeutics have not been developed. **Suggested NCIT terms:** platelet transfusion, supportive care, anticonvulsant therapy.

---

## 13. Prevention

- **Primary prevention:** Not applicable (monogenic). Prevention is limited to **genetic counseling and reproductive options** — carrier testing, prenatal diagnosis, and preimplantation genetic testing in families with a known genotype.
- **Secondary/tertiary prevention:** Early diagnosis via transferrin glycoprofiling and molecular testing enables anticipatory management of bleeding, infection, and developmental support (tertiary prevention of complications).
- **Counseling:** Autosomal recessive recurrence risk is 25% for future pregnancies of carrier couples; cascade testing of relatives is appropriate.
- **Immunization / public health / environmental interventions:** Not applicable to the disease etiology, though standard immunizations and infection precautions are advisable given the immune compromise.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologues:** *SLC35A1* is conserved across mammals. The functional mouse orthologue is ***Slc35a1*** (*Mus musculus*, NCBI Taxon:10090). The classic in-vitro model is the CHO **Lec2** mutant, which lacks the CMP-sialic acid transporter and is used for complementation assays ([PMID: 15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/)).
- **Natural disease in animals:** No spontaneously occurring SLC35A1 disease has been characterized in companion animals or wildlife (no OMIA entry noted here).
- **Comparative biology:** The transport-and-sialylation mechanism is evolutionarily conserved; the mouse conditional knockout reproduces the hematologic mechanism (see Section 15), supporting cross-species conservation of the disease mechanism.
- **Zoonotic potential:** Not applicable.

---

## 15. Model Organisms

| Model | Type | Key features | Relevance |
|-------|------|--------------|-----------|
| **Platelet/megakaryocyte-specific *Slc35a1* conditional knockout mouse (Plt Slc35a1⁻/⁻)** | Mammalian, conditional KO | Thrombocytopenia; reduced/immature bone marrow megakaryocytes; increased hepatic Kupffer-cell clearance of desialylated platelets | Recapitulates the hematologic mechanism ([PMID: 32303557](https://pubmed.ncbi.nlm.nih.gov/32303557/)) |
| **CHO Lec2 mutant cells** | In vitro cell line | Deficient CMP-sialic acid transporter | Complementation/functional assay platform ([PMID: 15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/)) |
| **SLC35A1-knockout cell lines** | In vitro | Loss of N-glycan sialylation; used to test rescue by variant constructs | Variant functional characterization ([PMID: 36257191](https://pubmed.ncbi.nlm.nih.gov/36257191/)) |
| **Patient-derived fibroblasts** | In vitro (human) | Decreased sialylated N-/O-glycans; reduced Golgi CMP-sialic acid transport rate | Biochemical confirmation ([PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)) |

**Phenotype recapitulation & limitations.** The conditional mouse faithfully models the **hematologic** arm (thrombocytopenia via a dual defect: impaired megakaryocytopoiesis plus hepatic clearance) but, being platelet/megakaryocyte-restricted, does **not** model the neurological arm. *"The number of bone marrow megakaryocytes in Plt Slc35a1–/– mice was reduced, and megakaryocyte maturation was also impaired. In addition, an increased number of desialylated platelets was cleared by Küpffer cells in the liver of Plt Slc35a1–/– mice."* ([PMID: 32303557](https://pubmed.ncbi.nlm.nih.gov/32303557/)). Cell-based systems capture the biochemical sialylation defect and enable variant functional testing but cannot reproduce the multisystem clinical phenotype. A neural or whole-body model that recapitulates the encephalopathy has not been reported — a notable gap.

---

## Key Findings (Evidence Detail)

### Finding 1 — SLC35A1-CDG is caused by biallelic loss of the Golgi CMP-sialic acid transporter
The 2005 index report identified a patient lacking sialyl-Lewis-x on PMN cells with compound heterozygous *SLC35A1* defects (double microdeletion → stop at codon 327; splice mutation → 130-bp deletion, stop at codon 684). Complementation in Lec2 cells showed neither patient allele restored sialylation while wild-type did. *"We conclude that this defect is a new type of congenital disorder of glycosylation (CDG) of type IIf affecting the transport of CMP-sialic acid into the Golgi apparatus."* ([PMID: 15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/))

### Finding 2 — Two overlapping presentations: hematologic vs neurological
Hematologic-dominant (macrothrombocytopenia, neutropenia, absent sLeˣ) in the index case ([PMID: 27387429](https://pubmed.ncbi.nlm.nih.gov/27387429/)); neurological-dominant encephalopathy with missense genotype (T156R/E196K) and *no* hematologic abnormality in the third patient: *"Here we report the identification of the third patient with CMP-sialic acid transporter deficiency, who presented with severe neurological phenotype, but without hematological abnormalities."* Patient fibroblasts/serum showed *"a considerable decrease in the amount of N- and O-glycans terminating in sialic acid"* ([PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)).

### Finding 3 — Mouse Slc35a1 deficiency: thrombocytopenia via impaired megakaryocytopoiesis + hepatic clearance
A conditional platelet/megakaryocyte-specific knockout produced thrombocytopenia via reduced megakaryocyte numbers, impaired maturation, and increased Kupffer-cell clearance of desialylated platelets ([PMID: 32303557](https://pubmed.ncbi.nlm.nih.gov/32303557/)).

### Finding 4 — Substrate pockets and a sialyltransferase interaction disrupted by CDG mutations
Three substrate pockets defined (nucleobase E52/K55/Y214; middle Q101/N102/T260; sugar K124/T128/S188/K272) ([PMID: 34384782](https://pubmed.ncbi.nlm.nih.gov/34384782/)). E196K (not T156R) disrupts SLC35A1–ST3Gal4 coupling and reduces sialylation rescue in knockout cells ([PMID: 36257191](https://pubmed.ncbi.nlm.nih.gov/36257191/)).

### Finding 5 — Ultra-rare; diagnosis via Type II transferrin glycoprofile + molecular confirmation
Only the third patient by 2017 ([PMID: 28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/)); classified among CDG-II defects detectable by intact-transferrin mass spectrometry alongside PGM1-, MGAT2-, and B4GALT1-CDG ([PMID: 26307094](https://pubmed.ncbi.nlm.nih.gov/26307094/)).

### Finding 6 — No targeted therapy; supportive management within the CDG landscape
Therapy is available for very few CDG subtypes and is largely dietary monosaccharide/precursor supplementation ([PMID: 35562242](https://pubmed.ncbi.nlm.nih.gov/35562242/); [PMID: 34788024](https://pubmed.ncbi.nlm.nih.gov/34788024/)). Sialic acid supplementation cannot bypass the Golgi-delivery lesion.

### Finding 7 — Neurological phenotype linked to deficient brain sialoglycans
*"In the brain, two families of sialoglycans are of particular interest: gangliosides and polysialic acid."* and *"Mouse genetic studies and human disorders of ganglioside metabolism implicate gangliosides in axon-myelin interactions, axon stability, axon regeneration, and the modulation of nerve cell excitability."* ([PMID: 24692354](https://pubmed.ncbi.nlm.nih.gov/24692354/)); *"Polysialylated NCAM and neural gangliosides both play critical roles in mediating cell-to-cell interactions important for neuronal outgrowth, synaptic connectivity, and memory formation."* ([PMID: 22585926](https://pubmed.ncbi.nlm.nih.gov/22585926/)).

### Finding 8 — Ashwell-Morell receptor clearance underlies thrombocytopenia; sialidase inhibition is a candidate therapy
*"This leads to platelet clearance in the liver via hepatocyte Ashwell-Morell receptors, which is fundamentally different from the classical Fc-FcγR-dependent macrophage phagocytosis."* and *"sialidase inhibitors ameliorate anti-GPα-mediated thrombocytopenia in mice."* ([PMID: 26185093](https://pubmed.ncbi.nlm.nih.gov/26185093/)).

---

## Mechanistic Model / Interpretation

SLC35A1-CDG is a paradigm of **"one lesion, two phenotypes."** A single upstream defect — failure to deliver CMP-sialic acid into the Golgi — produces global hyposialylation, which then manifests differently depending on which sialylated glycoconjugates a given tissue most depends on. In the **blood**, the critical cargo is sialic acid on platelet and leukocyte surface glycoproteins: its loss triggers hepatic clearance of platelets (Ashwell-Morell + Kupffer) and abolishes the selectin ligand sialyl-Lewis-x, producing thrombocytopenia, bleeding, and infection susceptibility. In the **brain**, the critical cargo is sialic acid on gangliosides and polysialic acid–NCAM: its loss impairs axon-myelin interaction, synaptic connectivity, and excitability, producing encephalopathy, seizures, and developmental delay.

The **genotype-phenotype correlation** appears to hinge on residual transporter activity: truncating null alleles (index case) associate with the hematologic picture, whereas hypomorphic missense alleles (T156R/E196K) associate with the neurological picture — possibly because partial activity, tissue-specific demand, or selective decoupling from particular sialyltransferases (E196K–ST3Gal4) shapes which organ crosses its functional threshold. This remains an inference from very few patients and should be treated cautiously.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|------|-------------|---------------|
| [15576474](https://pubmed.ncbi.nlm.nih.gov/15576474/) | Defines CDG-IIf; biallelic LoF; Lec2 complementation | Human + in vitro |
| [28856833](https://pubmed.ncbi.nlm.nih.gov/28856833/) | Third patient; neurological phenotype; missense genotype; reduced transport | Human + in vitro |
| [27387429](https://pubmed.ncbi.nlm.nih.gov/27387429/) | Hematologic presentation; absent sLeˣ | Human/review |
| [32303557](https://pubmed.ncbi.nlm.nih.gov/32303557/) | Mouse KO: megakaryocytopoiesis + hepatic clearance | Model organism |
| [34384782](https://pubmed.ncbi.nlm.nih.gov/34384782/) | Substrate-pocket mapping | In vitro/structural |
| [36257191](https://pubmed.ncbi.nlm.nih.gov/36257191/) | SLC35A1–ST3Gal4 interaction; E196K decoupling | In vitro |
| [26307094](https://pubmed.ncbi.nlm.nih.gov/26307094/) | Diagnostic transferrin MS; CDG-II classification | Human/methods |
| [24692354](https://pubmed.ncbi.nlm.nih.gov/24692354/) | Brain sialoglycans (gangliosides, polySia) | Review |
| [22585926](https://pubmed.ncbi.nlm.nih.gov/22585926/) | Sialic acid in neurodevelopment/cognition | Review |
| [26185093](https://pubmed.ncbi.nlm.nih.gov/26185093/) | Ashwell-Morell clearance; sialidase inhibitors | Model organism/mechanism |
| [35562242](https://pubmed.ncbi.nlm.nih.gov/35562242/), [34788024](https://pubmed.ncbi.nlm.nih.gov/34788024/) | CDG therapeutics landscape | Review |
| [38262859](https://pubmed.ncbi.nlm.nih.gov/38262859/) | CDG epidemiology context (Tunisia) | Human/epidemiology |

---

## Limitations and Knowledge Gaps

1. **Extreme rarity.** Fewer than ~10 reported patients; phenotype frequencies, penetrance details, natural history, and survival cannot be quantified.
2. **Genotype-phenotype correlation is provisional**, based on individual cases; the mechanistic explanation for why some genotypes are hematologic and others neurological is inferred, not proven.
3. **No neural model.** The mouse model is platelet/megakaryocyte-restricted and does not capture the encephalopathy; the CNS mechanism (ganglioside/polySia deficiency) is inferred from sialoglycan biology rather than demonstrated in an SLC35A1 model.
4. **The Ashwell-Morell mechanism** in SLC35A1-CDG is extrapolated from ITP/desialylation models; direct demonstration in patient platelets is lacking.
5. **No therapy.** No trials, no established supplementation strategy; sialidase inhibition is untested in this disorder.
6. **Ontology term suggestions** here (HPO/GO/CL/UBERON/NCIT) are proposed based on clinical/mechanistic mapping and should be curator-verified.

---

## Proposed Follow-up Experiments / Actions

1. **Build a neural SLC35A1 model** (neuron-specific conditional KO mouse or patient iPSC-derived neurons/organoids) to directly test whether ganglioside and polySia-NCAM deficiency drives the encephalopathy, and to define the critical developmental window.
2. **Systematic genotype-phenotype curation** across all reported patients, correlating residual transport activity of each variant (quantitative Lec2/KO-cell rescue assays) with predominant organ involvement.
3. **Test sialidase inhibition** (e.g., oseltamivir-class neuraminidase inhibitors) in the Plt Slc35a1⁻/⁻ mouse to determine whether blocking desialylation-driven clearance corrects thrombocytopenia — a translatable candidate for the hematologic phenotype.
4. **Evaluate whether any sialic acid–precursor or metabolic-bypass strategy** (e.g., agents raising cytosolic CMP-Neu5Ac or leveraging alternative transporters) can partially restore Golgi sialylation in patient fibroblasts.
5. **Characterize the SLC35A1–sialyltransferase interactome** beyond ST3Gal4 to understand variant-specific decoupling and its contribution to tissue-selective phenotypes.
6. **Establish a clinical registry / minimal biomarker panel** (transferrin glycoprofile, serum sialoglycan/ganglioside markers such as GM3, platelet desialylation markers) to enable natural-history study and future trial readiness.

---

*Report compiled from 5 iterations of autonomous investigation; 8 confirmed findings; 26 papers reviewed. Evidence types are distinguished throughout as human clinical, model organism, in vitro, or review.*


## Artifacts

- [OpenScientist final report](SLC35A1-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SLC35A1-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011342` (2 mentions) - the report calls it "MONDO"; MONDO calls it **SLC35A1-congenital disorder of glycosylation**
- `HP:0001875` (1 mention) - the report calls it "Laboratory"; HP calls it **Decreased total neutrophil count**
- `HP:0002719` (1 mention) - the report calls it "Clinical"; HP calls it **Recurrent infections**
- `HP:0001263` (1 mention) - the report calls it "Clinical"; HP calls it **Global developmental delay**
- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0001298` (1 mention) - the report calls it "Clinical"; HP calls it **Encephalopathy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006486` (1 mention) - the report calls it "protein glycosylation"; GO calls it **obsolete protein glycosylation**
- `UBERON:0000955` (1 mention) - the report calls it "Central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.