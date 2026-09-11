---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T19:11:11.300511'
end_time: '2026-09-06T19:42:46.187673'
duration_seconds: 1894.89
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Retinitis Pigmentosa With or Without Situs Inversus
  mondo_id: MONDO:0014186
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
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - PMID:33438581
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 2
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0014186
    reported_labels:
    - MONDO
    ontology_label: retinitis pigmentosa with or without situs inversus
  - term_id: HP:0000662
    reported_labels:
    - Symptom
    ontology_label: Nyctalopia
  - term_id: HP:0000613
    reported_labels:
    - Symptom
    ontology_label: Photophobia
  - term_id: HP:0001133
    reported_labels:
    - Clinical sign
    ontology_label: Constriction of peripheral visual field
  - term_id: HP:0007737
    reported_labels:
    - Physical manifestation
    ontology_label: Spicular pigmentation of the retina
  - term_id: HP:0001696
    reported_labels:
    - Physical manifestation
    ontology_label: Situs inversus totalis
  - term_id: HP:0000122
    reported_labels:
    - Physical manifestation
    ontology_label: Unilateral renal agenesis
  - term_id: HP:0000028
    reported_labels:
    - Physical manifestation
    ontology_label: Cryptorchidism
  - term_id: HP:0000458
    reported_labels:
    - Symptom
    ontology_label: Anosmia
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Retinitis_Pigmentosa_With_or_Without_Situs_Inversus-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Retinitis_Pigmentosa_With_or_Without_Situs_Inversus-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Retinitis Pigmentosa With or Without Situs Inversus
- **MONDO ID:** MONDO:0014186 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Retinitis Pigmentosa With or Without Situs Inversus** covering all of the
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

# Retinitis Pigmentosa With or Without Situs Inversus (ARL2BP-Related Ciliopathy)

**Disease:** Retinitis Pigmentosa With or Without Situs Inversus
**MONDO ID:** MONDO:0014186 · **OMIM Phenotype:** #615434 (RP66) · **Gene:** ARL2BP (16q13)
**Category:** Mendelian (autosomal recessive)

---

## Summary

Retinitis Pigmentosa With or Without Situs Inversus is a rare, autosomal-recessive **ciliopathy** caused by biallelic loss-of-function mutations in **ARL2BP** (ADP-ribosylation-factor-like 2 binding protein; also called *BART*), located at chromosome 16q13. ARL2BP was the first identified ARL2-GTP–specific effector protein, and it functions as an anchor/co-GEF for the ARL2 and ARL3 small GTPase cycle that governs the ciliary trafficking of lipid-modified phototransduction proteins and the assembly of the photoreceptor connecting-cilium axoneme. The disease was first defined in 2013 through homozygosity mapping and exome sequencing in two consanguineous families ([PMID: 23849777](https://pubmed.ncbi.nlm.nih.gov/23849777/)), where one family combined retinitis pigmentosa (RP) with **situs inversus**, establishing the phenotypic hallmark that names the disorder.

The core disease process is degeneration of rod and cone photoreceptors producing classic retinitis pigmentosa (night blindness, progressive peripheral-then-central visual field loss, bone-spicule pigmentation, reduced/extinguished electroretinogram). Because ARL2BP is required for both **primary/sensory cilia** (photoreceptor outer segment) and **motile cilia** (embryonic node, sperm flagellum, airway), affected individuals may additionally show situs inversus totalis (in roughly half of patients — hence "with or without"), male infertility from oligo-/asthenozoospermia, and, in some cases, unilateral renal agenesis with renal microcysts and anosmia. This multisystem presentation places the disorder within the broader ciliopathy spectrum overlapping primary ciliary dyskinesia.

The condition is **ultra-rare**, reported in only a handful of largely consanguineous families worldwide, and is one molecular subtype of retinitis pigmentosa (overall prevalence ~1:4,000). There is currently **no approved disease-modifying therapy**; management is supportive (visual aids, low-vision rehabilitation, nutritional counseling, assisted reproduction for infertility, and airway management if primary ciliary dyskinesia features are present). The one FDA/EMA-approved retinal gene therapy (voretigene neparvovec, Luxturna) is specific to *RPE65* and does not apply to ARL2BP. Diagnosis rests on ophthalmic phenotyping (ERG, OCT, fundus autofluorescence) plus next-generation sequencing, and an *Arl2bp*-knockout mouse faithfully recapitulates the retinal and ciliary phenotype, providing a validated preclinical model.

---

## 1. Disease Information

Retinitis Pigmentosa With or Without Situs Inversus is a Mendelian inherited retinal dystrophy in which progressive rod–cone degeneration (retinitis pigmentosa) occurs either in isolation or accompanied by laterality defects (situs inversus) and other ciliopathy features. It is a **primary retinal ciliopathy** — the underlying lesion affects the photoreceptor connecting cilium, a specialized primary cilium.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014186 |
| OMIM (phenotype) | #615434 (Retinitis pigmentosa 66; RP66/RP with or without situs inversus) |
| OMIM (gene) | 615407 (ARL2BP) |
| Gene / HGNC | ARL2BP / HGNC:702 |
| NCBI Gene | GeneID 23568 |
| UniProt | Q9Y2Y0 |
| Ensembl | ENSG00000102931 |
| Cytogenetic location | 16q13 (GRCh38 chr16:57,245,259–57,253,635) |

**Synonyms / alternative names:** Retinitis pigmentosa 66 (RP66); RP with situs inversus; ARL2BP-related retinitis pigmentosa; ARL2BP-related syndromic rod–cone dystrophy. Gene aliases: *BART, BART1, RP66, RP82*.

**Information source type:** The knowledge base entry is derived primarily from **aggregated disease-level resources** (OMIM, ClinVar, gnomAD, UniProt, NCBI Gene) supplemented by **individual patient case reports** describing single families or probands. It is not derived from large EHR cohorts, reflecting the disease's rarity.

---

## 2. Etiology

**Primary cause — genetic.** The disease is monogenic and Mendelian: biallelic (homozygous or compound-heterozygous) **loss-of-function variants in ARL2BP** cause the phenotype. There is no environmental, infectious, or acquired etiology. The original identification used a combination of homozygosity mapping and exome sequencing in two consanguineous families to establish ARL2BP as causative ([PMID: 23849777](https://pubmed.ncbi.nlm.nih.gov/23849777/)): *"we used a combination of homozygosity mapping and exome sequencing to identify mutations in ARL2BP, which encodes an effector protein of the small GTPases ARL2 and ARL3, as causative for autosomal-recessive RP (RP66)."*

**Genetic risk factors.** The causal alleles are the pathogenic ARL2BP variants themselves (see Section 4). Because the disorder is recessive, **consanguinity** is the dominant risk-elevating factor — all originally reported families were consanguineous with homozygous variants. No modifier loci or susceptibility SNPs have been established for this ultra-rare disorder.

**Environmental risk factors.** None identified or expected for a monogenic recessive disorder. General retinitis-pigmentosa risk modifiers such as light exposure are not established for the ARL2BP subtype.

**Protective factors.** No genetic or environmental protective factors have been identified. Population constraint data (gnomAD: pLI ≈ 5.8×10⁻⁶, observed/expected LoF ≈ 0.79) indicate ARL2BP is tolerant of heterozygous loss of function — consistent with carriers being unaffected and disease requiring biallelic loss.

**Gene–environment interactions.** None documented. Disease expression is determined by genotype; the "with or without situs inversus" variability reflects the stochastic nature of left–right axis determination by motile nodal cilia rather than any environmental interaction.

---

## 3. Phenotypes

The phenotype is a **syndromic rod–cone dystrophy** with variable extra-ocular ciliopathy features. Core and associated phenotypes, with suggested HPO terms:

| Phenotype | Type | HPO term (suggested) | Onset | Severity / progression | Frequency |
|---|---|---|---|---|---|
| Retinitis pigmentosa / rod–cone dystrophy | Clinical sign | HP:0000510 (Rod-cone dystrophy) | Photophobia ~20 y; nyctalopia & central vision loss ~30 y | Progressive; can be slow | Constant (100%) |
| Night blindness (nyctalopia) | Symptom | HP:0000662 | Early | Progressive | Very frequent |
| Photophobia | Symptom | HP:0000613 | Often first symptom (~20 y) | Progressive | Frequent |
| Constricted / peripheral visual field loss | Clinical sign | HP:0001133 | Early–mid adult | Progressive | Very frequent |
| Bone-spicule retinal pigmentation | Physical manifestation | HP:0007737 | Adult | Progressive | Typical |
| Reduced/absent ERG responses | Laboratory/functional | HP:0000512 (Abnormal ERG) | Early | Progressive | Constant |
| Situs inversus totalis | Physical manifestation | HP:0001696 | Congenital | Stable | ~50% ("with or without") |
| Male infertility (oligo-/asthenozoospermia) | Laboratory / clinical | HP:0000798 / HP:0012041 | Post-pubertal | Stable | Reported subset of males |
| Unilateral renal agenesis | Physical manifestation | HP:0000122 | Congenital | Stable | Rare |
| Renal microcysts | Physical manifestation | HP:0000107 (Renal cyst) | Variable | Variable | Rare |
| Cryptorchidism | Physical manifestation | HP:0000028 | Congenital | Stable | Rare |
| Anosmia / olfactory dysfunction | Symptom | HP:0000458 | Variable | Stable | Rare |

The multisystem triad of RP, situs inversus, and male infertility was explicitly described as novel in a Chinese patient ([PMID: 36507858](https://pubmed.ncbi.nlm.nih.gov/36507858/)): *"presenting with retinitis pigmentosa (RP), situs inversus totalis, and oligozoospermia … this a novel ARL2BP-associated phenotypic triad of RP, situs inversus, and male infertility."* Renal and sperm involvement was further documented ([PMID: 38649918](https://pubmed.ncbi.nlm.nih.gov/38649918/)): *"a splice site variant in the ARL2BP gene causing situs inversus, asthenozoospermia, unilateral renal agenesis and microcysts."*

**Quality-of-life impact.** The dominant burden is progressive vision loss, which impairs mobility, reading, driving, and independence and is a leading cause of visual disability; situs inversus totalis is generally asymptomatic; male infertility affects family planning. No disease-specific QoL instrument data exist for this ultra-rare subtype, but generic RP QoL measures (VFQ-25, low-vision instruments) apply.

**Progression note.** Course can be relatively slow — one patient retained useful residual vision at age 63 with slow progression over 5 years of follow-up ([PMID: 38649918](https://pubmed.ncbi.nlm.nih.gov/38649918/)).

---

## 4. Genetic / Molecular Information

**Causal gene:** *ARL2BP* (GeneID 23568; OMIM 615407; HGNC:702; UniProt Q9Y2Y0), 16q13. NCBI summary: *"This protein is considered to be the first ARL2-specific effector identified, due to its interaction with ARL2.GTP but lack of ARL2 GTPase-activating protein activity."*

**Pathogenic variants** (all germline; no somatic involvement):

| Variant (cDNA) | Protein / effect | Type | Classification | Source |
|---|---|---|---|---|
| c.101-1G>C | Alters pre-mRNA splicing (splice acceptor) | Splice-site | Pathogenic | [PMID: 23849777](https://pubmed.ncbi.nlm.nih.gov/23849777/) |
| c.134T>G | p.Met45Arg — reduces ARL2 binding, abolishes basal-body localization | Missense | Pathogenic | [PMID: 23849777](https://pubmed.ncbi.nlm.nih.gov/23849777/) |
| c.22_23delAG | p.Ser8Leufs*10 | Frameshift (null) | Pathogenic | [PMID: 36507858](https://pubmed.ncbi.nlm.nih.gov/36507858/) |
| c.294-1G>C | Splice acceptor | Splice-site | Pathogenic | [PMID: 38649918](https://pubmed.ncbi.nlm.nih.gov/38649918/) |

**Variant classification (ACMG/AMP):** ClinVar (accessed 2026) holds 146 ARL2BP variant records: ~11 Pathogenic and ~2 Likely pathogenic (predominantly splice-site and frameshift null alleles), ~10 VUS, ~8 likely-benign, and 1 with conflicting classifications. The predominance of null/loss-of-function pathogenic alleles supports a **loss-of-function disease mechanism**.

**Allele frequency:** Pathogenic alleles are extremely rare/absent in gnomAD, consistent with a recessive disorder confined to consanguineous or founder contexts. ARL2BP is LoF-tolerant in heterozygotes (pLI ≈ 5.8×10⁻⁶; o/e LoF ≈ 0.79).

**Functional consequence:** Loss of function. The p.Met45Arg missense allele mechanistically reduces ARL2 binding and abolishes ARL2BP localization to the photoreceptor basal body — a demonstrated pathomechanism rather than merely predicted ([PMID: 23849777](https://pubmed.ncbi.nlm.nih.gov/23849777/)).

**Modifier genes:** None established. **Epigenetic changes:** Not implicated. **Chromosomal abnormalities:** None; the disease is caused by point/small variants, not large structural rearrangements (situs inversus here is a ciliary-motility consequence, not a chromosomal inversion despite the name).

---

## 5. Environmental Information

There are **no environmental, lifestyle, or infectious contributors** to this monogenic recessive disorder. No toxins, radiation, occupational exposures, dietary factors, or pathogens are implicated in causing or triggering ARL2BP-related disease. The only relevant "environmental" factor in a population-genetics sense is **consanguineous mating**, which increases the probability of homozygosity for rare recessive alleles.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function mutation in ARL2BP** (splice, frameshift, or function-abolishing missense) → **loss or dysfunction of ARL2BP protein**.
2. Loss of ARL2BP → **failure to anchor/localize at the ciliary basal body and cilium-associated centriole** of photoreceptors (demonstrated: p.Met45Arg abolishes basal-body localization; ARL2 depletion displaces ARL2BP) ([PMID: 23849777](https://pubmed.ncbi.nlm.nih.gov/23849777/)).
3. Mislocalized/absent ARL2BP → **disrupted ARL2/ARL3 small-GTPase cycle** (ARL2BP is the first ARL2-GTP-specific effector and acts as a co-GEF stabilizing active ARL3-GTP) ([PMID: 33438581](https://pubmed.ncbi.nlm.nih.gov/33438581/)).
4. Impaired ARL3 activity → **defective ciliary trafficking of lipid-modified (prenylated/myristoylated) phototransduction proteins** via the RP2–ARL3–PDE6D axis, which chaperones prenylated cargo such as PDE6 and GRK1 into the outer segment ([PMID: 25422369](https://pubmed.ncbi.nlm.nih.gov/25422369/)).
   - **Branch A (sensory cilium / retina):** cargo mistrafficking + axonemal defect → **disorganized photoreceptor outer segments** with vertically aligned disks, shortened axonemes, open B-tubule doublets, and loss of singlet microtubules (demonstrated in KO mouse) ([PMID: 29718757](https://pubmed.ncbi.nlm.nih.gov/29718757/)) → **progressive rod and cone death** → **retinitis pigmentosa** (nyctalopia → field loss → central vision loss).
   - **Branch B (motile cilia):** the same ciliary/axonemal assembly defect in **embryonic nodal cilia** → randomized left–right axis determination → **situs inversus** (present in ~half of patients); in **sperm flagella** → oligo-/asthenozoospermia → **male infertility**; in **airway cilia** → potential primary-ciliary-dyskinesia-type respiratory features; in **renal cilia** → renal agenesis/microcysts; in **olfactory cilia** → anosmia.

### Detail by category

- **Molecular pathways:** ARL2/ARL3 GTPase signaling; RP2–ARL3–PDE6D lipidated-cargo ciliary trafficking. ARL2BP moonlights in ARL2-dependent STAT3 nuclear translocation/transcriptional activity (UniProt Q9Y2Y0: *"Together with ARL2, plays a role in the nuclear translocation, retention and transcriptional activity of STAT3."*).
- **Cellular processes:** Ciliogenesis and ciliary maintenance; intraflagellar/ciliary protein transport; photoreceptor outer-segment disk morphogenesis; progressive photoreceptor apoptosis.
- **Protein dysfunction:** Loss of function via truncation (frameshift/splice) or loss of ARL2 binding + mislocalization (p.Met45Arg). GO molecular functions: GTPase regulator activity (GO:0030695), transcription coactivator activity (GO:0003713).
- **Metabolic changes:** Disrupted delivery of PDE6 (cGMP phototransduction cascade) impairs the visual cycle at the outer segment; broader metabolic changes not characterized.
- **Immune involvement:** None; not an autoimmune/inflammatory disease.
- **Tissue damage mechanism:** Structural failure of the connecting cilium/axoneme leading to outer-segment malformation and photoreceptor degeneration.
- **Biochemical abnormalities:** Failure of the ARL2BP→ARL3-GTP→PDE6D trafficking module; mislocalization of prenylated phototransduction enzymes.

**Suggested GO / CL terms:** BP — cilium assembly (GO:0060271), intraciliary transport (GO:0042073), photoreceptor cell maintenance (GO:0045494), determination of left/right symmetry (GO:0007368), regulation of GTPase activity (GO:0043087). CC — ciliary basal body (GO:0036064), photoreceptor connecting cilium (GO:0032391), centrosome (GO:0005813). CL — retinal rod cell (CL:0000604), retinal cone cell (CL:0000573), ciliated cell (CL:0000064), sperm (CL:0000019).

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Eye — retina, specifically the photoreceptor layer (UBERON:0000970 eye; UBERON:0000966 retina; UBERON:0001789 photoreceptor layer). **Secondary/associated organs:** thoraco-abdominal viscera (laterality reversal in situs inversus — heart, lungs, liver, spleen, stomach mirror-imaged), testis/sperm (male reproductive system), kidney, olfactory epithelium.

**Body systems involved:** visual/nervous (sensory), reproductive (male infertility), renal/urinary, respiratory (if PCD features), and the visceral situs of cardiovascular/digestive systems.

**Tissue and cell level:** Neural retina — **rod photoreceptors (CL:0000604)** and **cone photoreceptors (CL:0000573)** are the primary targets; motile ciliated cells of node, airway, and reproductive tract; renal tubular epithelium. Patient fibroblasts (in vitro) show shortened cilia and reduced proliferation ([PMID: 36507858](https://pubmed.ncbi.nlm.nih.gov/36507858/)).

**Subcellular level:** The **connecting cilium / basal body** (GO:0036064) is the central compartment. UniProt/GO also annotate ARL2BP to centrosome (GO:0005813), spindle (GO:0005819), midbody (GO:0030496), cytosol (GO:0005829), nucleoplasm (GO:0005654), and mitochondrial intermembrane space (GO:0005758)/matrix (GO:0005759) — reflecting moonlighting roles.

**Localization / lateralization:** Retinal involvement is **bilateral and roughly symmetric**; situs inversus is a whole-body **laterality reversal** (mirror-image organ arrangement); renal agenesis reported as **unilateral**.

---

## 8. Temporal Development

**Onset:** Situs inversus and renal/laterality anomalies are **congenital**. Retinal disease is typically **young-adult onset**: photophobia often first at ~20 years, nyctalopia and central vision loss by ~30 years ([PMID: 38649918](https://pubmed.ncbi.nlm.nih.gov/38649918/)). Onset pattern is **insidious and chronic**.

**Progression:** Chronic, lifelong, and **progressive** but can be **slow** — one patient retained useful residual vision at 63 with slow progression over a 5-year window ([PMID: 38649918](https://pubmed.ncbi.nlm.nih.gov/38649918/)). Typical RP staging applies: early (night blindness, mid-peripheral field loss) → intermediate (ring scotoma, constricted fields) → advanced (tunnel vision) → end-stage (central/legal blindness). Situs inversus is stable and non-progressive.

**Patterns:** No remissions; no relapsing–remitting course. The **therapeutic window** for any future retinal gene therapy is early disease while viable photoreceptors remain — an important critical-period consideration.

---

## 9. Inheritance and Population

**Inheritance:** Autosomal recessive. Biallelic ARL2BP variants; reported families are consanguineous with homozygous alleles.

**Penetrance / expressivity:** Retinal disease appears fully penetrant in biallelic carriers; **situs inversus shows incomplete penetrance / variable expressivity** ("with or without"), reflecting the stochastic left–right axis determination by nodal cilia. Extra-ocular features (renal, olfactory, fertility) are variably expressed.

**Founder effects / consanguinity:** Strong consanguinity contribution; homozygous variants in geographically distinct families (Middle East, China, Italy, Pakistan). No genetic anticipation, germline mosaicism, or repeat-expansion mechanism.

**Epidemiology:** Retinitis pigmentosa overall has a worldwide prevalence of ~1:4,000 (~100,000 affected in the USA), with 20–30% of cases syndromic ([PMID: 29597005](https://pubmed.ncbi.nlm.nih.gov/29597005/)): *"RP is a leading cause of visual disability, with a worldwide prevalence of 1:4000. Although the majority of RP cases are non-syndromic, 20-30% of patients with RP also have an associated non-ocular condition."* ARL2BP-related RP (RP66) is an **ultra-rare** subtype — only a handful of families reported worldwide. In a consanguineous Pakistani IRD cohort it accounted for 1 of 72 families (1.4%) ([PMID: 40384762](https://pubmed.ncbi.nlm.nih.gov/40384762/)): *"…1/72(1.38%) … in … retinitis pigmentosa with situs inversus … segregated families."*

**Sex ratio:** Retinal disease affects both sexes; the infertility phenotype is specific to males. **Carrier frequency:** Not precisely established; expected very low outside consanguineous populations.

---

## 10. Diagnostics

**Ophthalmic evaluation (core):** Full-field **electroretinogram (ERG)** shows markedly reduced or absent rod and cone responses; **fundus** shows bone-spicule pigmentation and optic-disc pallor; **OCT** and **fundus autofluorescence (FAF)** show progressive loss of outer retinal layers ([PMID: 29597005](https://pubmed.ncbi.nlm.nih.gov/29597005/)): *"Photoreceptor function measured with an electroretinogram is markedly reduced or even absent. Optical coherence tomography (OCT) and fundus autofluorescence (FAF) imaging show a progressive loss of outer retinal layers."* ARL2BP cases were additionally assessed with full-field stimulus threshold testing and multimodal imaging ([PMID: 38649918](https://pubmed.ncbi.nlm.nih.gov/38649918/)).

**Molecular genetic testing (definitive):** Next-generation sequencing — targeted IRD capture panels (e.g., a 344-gene panel, [PMID: 40384762](https://pubmed.ncbi.nlm.nih.gov/40384762/)), whole-exome, or whole-genome sequencing — with ACMG/AMP variant interpretation and Sanger segregation confirmation. Homozygosity mapping is valuable in consanguineous families ([PMID: 23849777](https://pubmed.ncbi.nlm.nih.gov/23849777/)).

**Extra-ocular workup:** Chest X-ray/abdominal imaging/echocardiography to detect **situs inversus**; **semen analysis** for oligo-/asthenozoospermia; renal ultrasound for agenesis/microcysts; olfactory testing where indicated.

**Differential diagnosis:** Other syndromic retinal ciliopathies — Usher syndrome, Bardet–Biedl syndrome, Senior–Løken syndrome, and other RP-with-situs-inversus/PCD overlaps; distinguished by gene panel and by the specific extra-ocular pattern. **Screening:** Cascade genetic testing of at-risk relatives and carrier testing in consanguineous families once the familial variant is known.

---

## 11. Outcome / Prognosis

**Survival / mortality:** The disorder is **not life-limiting** in itself. Situs inversus totalis is typically asymptomatic and compatible with normal lifespan. Life expectancy is generally normal unless significant primary-ciliary-dyskinesia respiratory disease is present.

**Morbidity / function:** The principal morbidity is **progressive, irreversible vision loss** leading to legal blindness in advanced disease — a major disability outcome with substantial QoL impact. Male infertility is a reproductive-health morbidity. **Recovery potential:** None with current therapy; photoreceptor loss is irreversible.

**Disease course / complications:** Chronic, progressive vision loss; cystoid macular edema and cataract can complicate RP generally; PCD-associated respiratory infections if motile-cilia airway disease is present.

**Prognostic factors:** Age at onset, rate of ERG/field decline, and residual outer-retinal structure on OCT predict visual outcome. Some ARL2BP patients show relatively slow progression with preserved vision into the seventh decade ([PMID: 38649918](https://pubmed.ncbi.nlm.nih.gov/38649918/)).

---

## 12. Treatment

**There is no proven disease-modifying therapy.** A 2020 Cochrane review of vitamin A and DHA/fish oils concluded evidence for slowing RP progression is limited/uncertain ([PMID: 32573764](https://pubmed.ncbi.nlm.nih.gov/32573764/)): *"At this time, there is no proven therapy for RP."*

**Supportive / rehabilitative care (mainstay):** Visual aids, orientation and mobility training, and nutritional supplementation provide only symptomatic relief and do not halt progression ([PMID: 40731809](https://pubmed.ncbi.nlm.nih.gov/40731809/)): *"While current management is largely supportive-relying on visual aids, orientation training, and nutritional supplementation-these interventions offer only symptomatic relief and do not halt disease progression."* (NCIT: Supportive Care; Low Vision Aid.)

**Not applicable:** The only approved retinal gene therapy, **voretigene neparvovec (Luxturna)**, is specific to biallelic *RPE65* mutations and does **not** apply to ARL2BP ([PMID: 37762059](https://pubmed.ncbi.nlm.nih.gov/37762059/)).

**Investigational:** AAV gene-replacement, RNA-based, and CRISPR/Cas9 strategies are advancing for RP broadly but remain **investigational for ARL2BP** ([PMID: 40869487](https://pubmed.ncbi.nlm.nih.gov/40869487/), [PMID: 40731809](https://pubmed.ncbi.nlm.nih.gov/40731809/)). ARL2BP's small coding sequence makes it a favorable candidate for AAV gene replacement in principle.

**Management of extra-ocular features:** Situs inversus totalis usually needs no treatment; PCD-type respiratory disease (if present) needs airway clearance/antibiotics; male infertility may be addressed with assisted reproduction (**ICSI**). (NCIT: Assisted Reproductive Technology; Intracytoplasmic Sperm Injection.)

**Pharmacogenomics / personalized medicine:** No genotype-guided pharmacotherapy exists; future precision approaches would be gene-replacement or variant-specific (e.g., splice-modulating ASOs for splice-site alleles).

---

## 13. Prevention

Being monogenic and recessive, prevention is **genetic/reproductive**, not lifestyle-based.

- **Primary prevention:** Not achievable by risk-factor modification. **Genetic counseling** for consanguineous families and known carriers; recurrence risk is 25% per pregnancy for two carrier parents.
- **Carrier / cascade screening:** Test at-risk relatives once the familial ARL2BP variant is identified.
- **Reproductive options:** Prenatal diagnosis and **preimplantation genetic testing (PGT-M)** for couples known to carry pathogenic ARL2BP variants.
- **Secondary/tertiary prevention:** Early ophthalmic monitoring to manage complications (cataract, macular edema), low-vision rehabilitation, and airway surveillance where PCD features exist. No immunization or public-health intervention is relevant.

---

## 14. Other Species / Natural Disease

**Orthologs (NCBI Gene):** mouse *Arl2bp* (GeneID 107566), rat *Arl2bp* (GeneID 498910), zebrafish *arl2bp* (GeneID 393976). A functional ARL2BP homolog is present and essential in **ciliate protozoa**, where RNAi is lethal and disrupts cortical microtubules ([PMID: 40432967](https://pubmed.ncbi.nlm.nih.gov/40432967/)): *"RNAi of ARL2BP and DYNLRB2 increased mortality, reduced motility, and disrupted cortical microtubule organization"* — demonstrating **deep evolutionary conservation** of ARL2BP's ciliary/microtubule role.

**Natural disease in other species:** No well-characterized naturally occurring ARL2BP disease is documented in companion animals or wildlife (OMIA entries not established for this specific gene–disease pair). **Comparative biology:** The conserved ciliary function across mammals, fish, and protozoa underpins the utility of cross-species models. **Zoonotic potential:** None (non-transmissible genetic disease).

---

## 15. Model Organisms

**Primary model — *Arl2bp*-knockout mouse:** A knockout mouse recapitulates key human features ([PMID: 29718757](https://pubmed.ncbi.nlm.nih.gov/29718757/)): *"we generated a knockout (KO) mouse model for ARL2BP, a ciliary protein linked to retinitis pigmentosa. The KO mice display an early and progressive reduction in visual response."* Structurally: *"we observed disorganization of the photoreceptor OS, with vertically aligned disks and shortened axonemes … ciliary doublet microtubule (MT) structure was also impaired, displaying open B-tubule doublets, paired with loss of singlet MTs."*

- **Phenotype recapitulation:** High for the retinal phenotype — early, progressive ERG decline; disorganized outer segments; connecting-cilium/axoneme and doublet-microtubule defects.
- **Applications:** Studying outer-segment morphogenesis, ciliary microtubule assembly, ARL2/ARL3 trafficking, and as a preclinical platform for gene-replacement testing.
- **Limitations:** Mouse retinal architecture (rod-dominant, no macula) limits translation of central-vision outcomes; extent to which the model reproduces situs inversus/laterality and fertility phenotypes is less fully characterized.

**In vitro models:** Patient-derived fibroblasts show reduced proliferation and shortened cilia ([PMID: 36507858](https://pubmed.ncbi.nlm.nih.gov/36507858/)), providing a cellular ciliogenesis assay. Zebrafish and ciliate systems offer additional conserved platforms for ciliary-function studies.

---

## Mechanistic Model / Interpretation

```
 ARL2BP biallelic LoF mutation (splice / frameshift / p.Met45Arg)
              │
              ▼
 Loss/dysfunction of ARL2BP protein
              │
              ▼
 Failure to localize at basal body / cilium-associated centriole
   (p.Met45Arg abolishes basal-body localization; loses ARL2 binding)
              │
              ▼
 Disrupted ARL2 / ARL3 GTPase cycle  (ARL2BP = ARL2-GTP effector + ARL3 co-GEF)
              │
              ▼
 Defective ARL3–PDE6D ciliary trafficking of prenylated proteins (PDE6, GRK1)
   + defective axoneme / doublet-microtubule assembly
              │
        ┌─────┴───────────────────────────────┐
        ▼ (sensory cilium)                     ▼ (motile cilia)
 Disorganized photoreceptor outer segment   Nodal cilia → SITUS INVERSUS (~50%)
 (vertical disks, short axoneme,            Sperm flagella → male infertility
  open B-tubules, lost singlet MTs)         Airway cilia → PCD-type disease
        │                                    Renal cilia → agenesis/microcysts
        ▼                                    Olfactory cilia → anosmia
 Progressive rod & cone death
        │
        ▼
 RETINITIS PIGMENTOSA (nyctalopia → field loss → central vision loss)
```

**Upstream vs downstream:** The mutation and ARL2BP loss are upstream; the ARL2/ARL3 cycle and PDE6D trafficking are the central molecular node; outer-segment malformation and photoreceptor death are downstream retinal outcomes; laterality/fertility/renal/olfactory features are parallel downstream consequences in motile-cilia tissues. The **"with or without situs inversus"** naming captures the branch point: the same molecular lesion produces retinal disease in all patients but laterality defects only when nodal-cilia motility is sufficiently disrupted during embryogenesis.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [23849777](https://pubmed.ncbi.nlm.nih.gov/23849777/) | *Mutations in ARL2BP cause AR retinitis pigmentosa* | Gene discovery; causal variants; situs inversus; ARL2-binding mechanism |
| [29718757](https://pubmed.ncbi.nlm.nih.gov/29718757/) | *ARL2BP needed for photoreceptor cilia doublets and OS structure* | KO mouse model; ciliary/axonemal defect |
| [25422369](https://pubmed.ncbi.nlm.nih.gov/25422369/) | *Mistrafficking of prenylated proteins causes RP2* | ARL3–PDE6D lipidated-cargo trafficking pathway |
| [33438581](https://pubmed.ncbi.nlm.nih.gov/33438581/) | *ARL3 activation requires co-GEF BART* | ARL2BP/BART as ARL3 co-GEF stabilizing ARL3-GTP |
| [36507858](https://pubmed.ncbi.nlm.nih.gov/36507858/) | *Novel ARL2BP variant: RP, situs inversus, infertility* | Phenotypic triad; frameshift allele; fibroblast cilia defect |
| [38649918](https://pubmed.ncbi.nlm.nih.gov/38649918/) | *Splice variant: situs inversus, asthenozoospermia, renal* | Renal/sperm phenotype expansion; slow progression |
| [29597005](https://pubmed.ncbi.nlm.nih.gov/29597005/) | *Non-syndromic retinitis pigmentosa* | RP prevalence 1:4000; diagnostic modalities |
| [40384762](https://pubmed.ncbi.nlm.nih.gov/40384762/) | *Consanguineous Pakistani IRD panel study* | Rarity (1/72 families); panel-based diagnosis |
| [32573764](https://pubmed.ncbi.nlm.nih.gov/32573764/) | *Vitamin A/fish oils for RP (Cochrane)* | No proven therapy for RP |
| [40731809](https://pubmed.ncbi.nlm.nih.gov/40731809/) | *RP: genetic insights to therapeutics* | Supportive-only management; investigational gene therapy |
| [37762059](https://pubmed.ncbi.nlm.nih.gov/37762059/) | *Gene therapy in hereditary retinal dystrophies* | Luxturna is RPE65-specific, not ARL2BP |
| [40869487](https://pubmed.ncbi.nlm.nih.gov/40869487/) | *Genetic therapies for RP* | Investigational AAV/RNA/CRISPR landscape |
| [40432967](https://pubmed.ncbi.nlm.nih.gov/40432967/) | *Cilia-associated gene families (ciliate)* | Deep conservation; essential ciliary role |

**Evidence source types:** Human clinical/genetic (23849777, 36507858, 38649918, 40384762, 29597005); model organism (29718757 mouse; 40432967 ciliate); in vitro (36507858 fibroblasts; 33438581 biochemistry; 25422369); systematic review/therapeutic (32573764, 40731809, 37762059, 40869487).

---

## Limitations and Knowledge Gaps

- **Ultra-rare with small n.** The entire literature rests on a handful of families/probands. Penetrance estimates (especially the ~50% figure for situs inversus) are approximate, and genotype–phenotype correlations are underpowered.
- **No formal epidemiology.** No registry-based prevalence/incidence for the ARL2BP subtype; figures derive from overall RP prevalence and single-cohort proportions.
- **QoL and natural-history data are absent** for this specific subtype; progression rate estimates come from isolated case follow-up.
- **Motile-cilia phenotype incompletely characterized.** The mechanistic link between ARL2BP loss and nodal/sperm/airway ciliary dysfunction is inferred from ciliopathy biology and case observations more than direct experiment; airway/PCD burden is not systematically documented.
- **Modifier and epigenetic factors unexplored**; explanation for variable situs inversus penetrance is mechanistic/stochastic rather than empirically mapped.
- **No therapy validated** — gene replacement is promising in principle but untested in ARL2BP models.

## Proposed Follow-up Experiments / Actions

1. **International case registry / GeneMatcher recruitment** to aggregate ARL2BP patients, refine penetrance of situs inversus, fertility, renal and olfactory involvement, and establish natural-history/progression rates.
2. **AAV-*ARL2BP* gene-replacement proof-of-concept** in the *Arl2bp*-KO mouse — the small coding sequence fits AAV capacity; measure ERG rescue and outer-segment/axoneme restoration.
3. **Splice-modulating ASO testing** for recurrent splice-acceptor alleles (c.101-1G>C, c.294-1G>C) in patient fibroblasts/iPSC-derived retinal organoids.
4. **iPSC-derived retinal organoids and multiciliated-airway cultures** from patients to model both sensory- and motile-cilia branches and to quantify trafficking of prenylated cargo (PDE6, GRK1).
5. **Systematic PCD/airway and fertility phenotyping** across the cohort to define the motile-cilia disease burden and inform surveillance guidelines.
6. **Structural/biochemical dissection** of the ARL2BP–ARL2/ARL3 co-GEF interface to enable variant-specific functional classification of VUS in ClinVar.

---

*Report compiled from 9 confirmed findings and 21 reviewed papers across a 5-iteration autonomous investigation. Evidence types and PMIDs are indicated throughout; ontology term suggestions (HPO, GO, CL, UBERON, NCIT) are embedded per section.*


## Artifacts

- [OpenScientist final report](Retinitis_Pigmentosa_With_or_Without_Situs_Inversus-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Retinitis_Pigmentosa_With_or_Without_Situs_Inversus-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:33438581` (4 mentions) - ARL3 activation requires the co-GEF BART and effector-mediated turnover.
  - shared terms: arl3

Weighed against this report's own most characteristic terms: `arl2bp`, `situs`, `inversus`, `disease`, `retinal`, `loss`, `gene`, `photoreceptor`, `renal`, `patient`, `progressive`, `feature`, `phenotype`, `pigmentosa`, `retinitis`, `familie`, `arl2`, `arl3`, `consanguineous`, `infertility`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014186` (2 mentions) - the report calls it "MONDO"; MONDO calls it **retinitis pigmentosa with or without situs inversus**
- `HP:0000662` (1 mention) - the report calls it "Symptom"; HP calls it **Nyctalopia**
- `HP:0000613` (1 mention) - the report calls it "Symptom"; HP calls it **Photophobia**
- `HP:0001133` (1 mention) - the report calls it "Clinical sign"; HP calls it **Constriction of peripheral visual field**
- `HP:0007737` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Spicular pigmentation of the retina**
- `HP:0001696` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Situs inversus totalis**
- `HP:0000122` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Unilateral renal agenesis**
- `HP:0000028` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Cryptorchidism**
- `HP:0000458` (1 mention) - the report calls it "Symptom"; HP calls it **Anosmia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000512` (1 mention) - the report calls it "Abnormal ERG"; HP calls it **Abnormal electroretinogram**, and lists "Abnormal ERG" among its other names
- `GO:0036064` (2 mentions) - the report calls it "connecting cilium / basal body"; GO calls it **ciliary basal body**, and lists "cilium basal body" among its other names