---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T16:05:22.684171'
end_time: '2026-10-14T16:19:42.287641'
duration_seconds: 859.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Camptodactyly-Arthropathy-Coxa Vara-Pericarditis Syndrome
  mondo_id: MONDO:0008828
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 24
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 20
  validator_version: 0.3.0
term_validation:
  total_terms: 20
  verified: 17
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 6
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0005750
    reported_labels:
    - coxa vara
    ontology_label: Lower-limb joint contracture
  - term_id: HP:0001644
    reported_labels:
    - pericardial effusion
    ontology_label: Dilated cardiomyopathy
  - term_id: HP:0100658
    reported_labels:
    - joint effusion
    ontology_label: Cellulitis
  - term_id: HP:0100763
    reported_labels:
    - synovial hypertrophy
    ontology_label: Abnormality of the lymphatic system
  - term_id: NCIT:C15431
    reported_labels:
    - Physical Therapy
    ontology_label: Hematopoietic Cell Transplantation
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
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
  path: Camptodactyly-Arthropathy-Coxa_Vara-Pericarditis_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Camptodactyly-Arthropathy-Coxa_Vara-Pericarditis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Camptodactyly-Arthropathy-Coxa Vara-Pericarditis Syndrome
- **MONDO ID:** MONDO:0008828 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Camptodactyly-Arthropathy-Coxa Vara-Pericarditis Syndrome** covering all of the
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

# Camptodactyly–Arthropathy–Coxa Vara–Pericarditis (CACP) Syndrome: A Comprehensive Disease Characteristics Report

**Disease:** Camptodactyly–Arthropathy–Coxa Vara–Pericarditis Syndrome
**MONDO ID:** MONDO:0008828 · **OMIM:** 208250 · **Causal gene:** *PRG4* (lubricin / proteoglycan 4)
**Category:** Mendelian (autosomal recessive)

---

## Summary

Camptodactyly–Arthropathy–Coxa Vara–Pericarditis (CACP) syndrome is an ultra-rare, autosomal recessive Mendelian disorder caused by **biallelic loss-of-function mutations in *PRG4***, the gene encoding **lubricin** (also known as proteoglycan 4, superficial zone protein, or megakaryocyte-stimulating factor precursor). Lubricin is a large secreted, mucin-like glycoprotein that provides **boundary lubrication** to articular cartilage and serosal (pericardial, pleural, tendon-sheath) surfaces and simultaneously **suppresses the overgrowth of synovial intimal cells**. When lubricin is absent, two coupled pathological processes occur: friction-driven death of superficial-zone chondrocytes and uncontrolled synovial intimal hyperplasia. Together these drive the disease's characteristic non-inflammatory tetrad: congenital **camptodactyly** (flexion contractures of the fingers), early-childhood **non-inflammatory large-joint arthropathy** with synovial hyperplasia, progressive **coxa vara** with a short femoral neck, and non-inflammatory serosal (**pericardial/pleural**) effusions.

A central clinical theme — recurring across essentially every modern case series — is that CACP is **repeatedly misdiagnosed as juvenile idiopathic arthritis (JIA)** and treated, ineffectively, with NSAIDs, methotrexate, corticosteroids, and biologic TNF inhibitors. The key distinguishing features are **persistently normal inflammatory markers (ESR/CRP), non-inflammatory synovial fluid (low white-cell count), absence of erosions on imaging, and the presence of coxa vara/short femoral neck**. Definitive diagnosis is made by *PRG4* sequencing (whole-exome/whole-genome or single-gene), which typically reveals homozygous (or compound heterozygous) **truncating** variants in consanguineous families, supported by an antibody-based assay showing **lubricin absence in blood and synovial fluid**.

There is **no approved disease-modifying treatment**; management is supportive (physiotherapy, orthopedic correction of coxa vara, joint replacement for end-stage disease, pericardiectomy for constrictive pericarditis). The most mechanistically rational investigational therapy is **recombinant human PRG4 (rhPRG4) replacement**, supported by preclinical large-animal and in vitro data. Prognosis is dominated by progressive joint deformity/disability, with **cardiac serositis (constrictive pericarditis) representing the principal life-threatening complication**; cognition and lifespan are otherwise generally preserved.

---

## Key Findings

### Finding 1 — CACP is caused by biallelic loss-of-function mutations in *PRG4* (lubricin)

CACP was mapped and cloned by positional-candidate methods to chromosome **1q25–q31**, where mutations in a gene designated *CACP* (now *PRG4*) encoding a secreted proteoglycan were identified as the cause of the autosomal recessive syndrome ([PMID: 10545950](https://pubmed.ncbi.nlm.nih.gov/10545950/)): *"we identified mutations in a gene (CACP) encoding a secreted proteoglycan as the cause of CACP."* *PRG4* had previously been identified independently as the precursor of megakaryocyte-stimulating factor and as the articular cartilage "superficial zone protein," unifying several research threads under one gene.

Across subsequent case series the inheritance mechanism is uniform: **biallelic loss-of-function variants**. A large cohort of 13 Indian patients explicitly states the syndrome *"is caused by biallelic loss-of-function variants in PRG4"* ([PMID: 38856641](https://pubmed.ncbi.nlm.nih.gov/38856641/)), and multiple independent reports describe homozygous truncating variants such as c.1290del (p.T431Lfs*481) in consanguineous families ([PMID: 40874560](https://pubmed.ncbi.nlm.nih.gov/40874560/)).

**Gene annotation:** HGNC *PRG4*; OMIM gene *605602*; OMIM phenotype *208250*. Suggested MONDO: **MONDO:0008828**.

### Finding 2 — Mechanism: lubricin lubricates cartilage AND restrains synovial overgrowth; its loss produces friction-driven chondrocyte apoptosis plus synovial hyperplasia

Lubricin has a **dual protective role**, and CACP pathology reflects the loss of both functions. In lubricin-mutant mice, abnormal protein deposits accumulate on the cartilage surface, superficial-zone chondrocytes are lost, and — critically — *"intimal cells in the synovium surrounding the joint space became hyperplastic, which further contributed to joint failure. Purified or recombinant lubricin inhibited the growth of these synoviocytes in vitro"* ([PMID: 15719068](https://pubmed.ncbi.nlm.nih.gov/15719068/)). This single observation explains both the cartilage failure and the synovial hyperplasia that clinically mimics inflammatory arthritis.

The friction–apoptosis link is mechanistically demonstrated: lubricin-knockout joints show elevated whole-joint friction and increased chondrocyte apoptosis, and in a bovine cartilage-on-cartilage explant system *"we observed a direct correlation between coefficient of friction and chondrocyte apoptosis in the superficial layers of cartilage,"* an effect reversed by adding lubricin ([PMID: 23530215](https://pubmed.ncbi.nlm.nih.gov/23530215/)). Downstream, friction induces chondrocyte **mitochondrial dysregulation and caspase-3 activation** ([PMID: 28604608](https://pubmed.ncbi.nlm.nih.gov/28604608/)), identifying apoptosis as the terminal tissue-damage step.

**Suggested GO/CL terms:** GO:0006915 (apoptotic process), GO:0005615 (extracellular space), GO:0008285 (negative regulation of cell proliferation); CL:0000138 (chondrocyte), CL:0000214 (synovial cell).

### Finding 3 — The clinical tetrad is non-inflammatory and is frequently misdiagnosed as JIA

CACP presents as a tetrad: congenital/early-onset **camptodactyly**, childhood-onset **non-inflammatory arthropathy with synovial hyperplasia**, progressive **coxa vara**, and non-inflammatory **pericardial (± pleural) effusion** ([PMID: 40830943](https://pubmed.ncbi.nlm.nih.gov/40830943/)). Phenotype frequencies from the 13-patient Indian cohort are: *"Camptodactyly (13/13), coxa vara (11/13), short femoral neck (11/13) and arthritis in large joints (12/13)"* ([PMID: 38856641](https://pubmed.ncbi.nlm.nih.gov/38856641/)), with wrists (11/13), ankles (11/13), elbows (10/13) and knees (10/13) most affected.

Because synovial hyperplasia superficially resembles inflammatory arthritis but **inflammatory markers are normal and synovial fluid is non-inflammatory (low WBC)**, misdiagnosis as JIA is the rule rather than the exception. In one series *"all patients were exposed to biologic therapy due to recalcitrant JIA"* ([PMID: 40475173](https://pubmed.ncbi.nlm.nih.gov/40475173/)), and multiple independent reports describe prolonged, ineffective immunosuppression before genetic confirmation ([PMID: 41626297](https://pubmed.ncbi.nlm.nih.gov/41626297/); [PMID: 42074176](https://pubmed.ncbi.nlm.nih.gov/42074176/); [PMID: 42482035](https://pubmed.ncbi.nlm.nih.gov/42482035/)).

**Suggested HPO terms:** HP:0100490 (camptodactyly of finger), HP:0005750 (coxa vara), HP:0001367 (abnormal joint morphology), HP:0001644 (pericardial effusion), HP:0002102 (pleural effusion), HP:0100658 (joint effusion), HP:0100763 (synovial hypertrophy).

### Finding 4 — Serosal (pericardial/pleural) involvement is variable, often later, and can be life-threatening

Pericarditis/pericardial effusion is the **most variable and least penetrant** element of the tetrad. It is described as occurring *"rarely"* in some cohorts ([PMID: 40475173](https://pubmed.ncbi.nlm.nih.gov/40475173/): *"early-onset camptodactyly, noninflammatory arthropathy, coxa vara deformity, and, rarely, pericardial effusion"*), reflecting lubricin's role on visceral serosal surfaces. When present and severe, it progresses to **constrictive pericarditis requiring pericardiectomy**, and has been misattributed to tuberculosis: *"the elder sister had pericardial effusion with constrictive pericarditis, underwent pericardiectomy and received empirical treatment for suspected tuberculosis"* ([PMID: 38955384](https://pubmed.ncbi.nlm.nih.gov/38955384/)). Neonatal pleural effusion with respiratory distress followed by later pericardiectomy has also been reported ([PMID: 40830943](https://pubmed.ncbi.nlm.nih.gov/40830943/)), and a unique association with **mitral stenosis** requiring commissurotomy was documented, hypothesized to relate to the proteoglycan content of the mitral valve ([PMID: 38523390](https://pubmed.ncbi.nlm.nih.gov/38523390/)).

### Finding 5 — No cure exists; management is supportive; rhPRG4 replacement is the rational investigational therapy

No approved disease-modifying treatment exists. Because the arthropathy is non-inflammatory, anti-inflammatory/immunosuppressive regimens fail: a patient *"despite receiving treatment modalities such as non-steroidal anti-inflammatory drugs (NSAIDs), methotrexate, and corticosteroids... experienced minimal improvement"* ([PMID: 40830943](https://pubmed.ncbi.nlm.nih.gov/40830943/)). The mechanistically rational strategy is **lubricin (rhPRG4) replacement**: intra-articular full-length recombinant human PRG4 reduced cartilage damage in a Yucatan minipig model of medial-meniscus destabilization — *"the rhPRG4 group had significantly less macroscopic cartilage damage in the medial tibial [plateau]"* ([PMID: 28129516](https://pubmed.ncbi.nlm.nih.gov/28129516/)) — and purified/recombinant lubricin inhibits synoviocyte overgrowth and reduces chondrocyte apoptosis in vitro ([PMID: 15719068](https://pubmed.ncbi.nlm.nih.gov/15719068/); [PMID: 23530215](https://pubmed.ncbi.nlm.nih.gov/23530215/)). Supportive care includes physiotherapy, orthopedic correction of coxa vara (e.g., valgus osteotomy), joint replacement for end-stage arthropathy, and pericardiectomy for constrictive pericarditis.

**Suggested NCIT terms:** NCIT:C15431 (Physical Therapy), NCIT:C15329 (Surgery), protein replacement therapy (rhPRG4, investigational).

### Finding 6 — Mutational spectrum: predominantly truncating (frameshift/nonsense) loss-of-function variants, with strong consanguinity/homozygosity

As of 2023 only *"36 pathogenic mutations have been reported in this gene"* ([PMID: 36694203](https://pubmed.ncbi.nlm.nih.gov/36694203/)), underscoring the disease's rarity. The spectrum is overwhelmingly **truncating**:

| Variant | Type | Reference |
|---|---|---|
| c.1290del (p.T431Lfs*481) | Frameshift | [PMID: 40874560](https://pubmed.ncbi.nlm.nih.gov/40874560/) |
| c.3756dup | Frameshift (duplication) | [PMID: 41626297](https://pubmed.ncbi.nlm.nih.gov/41626297/) |
| c.2208del (p.Thr737ProfsTer175) | Frameshift | [PMID: 42482035](https://pubmed.ncbi.nlm.nih.gov/42482035/) |
| c.4104T>A (p.Tyr1368Ter) | Nonsense | [PMID: 42482035](https://pubmed.ncbi.nlm.nih.gov/42482035/) |
| c.3636G>T, c.1935del, c.1134dup, c.1699del, c.962T>A | 5 novel | [PMID: 38856641](https://pubmed.ncbi.nlm.nih.gov/38856641/) |
| c.2645_2646delGA; c.2883_2886delAAGA | Frameshift deletions | [PMID: 25297354](https://pubmed.ncbi.nlm.nih.gov/25297354/) |

The 13-patient Indian cohort reported *"five novel disease-causing variants (c.3636G>T, c.1935del, c.1134dup, c.1699del and c.962T>A)"* ([PMID: 38856641](https://pubmed.ncbi.nlm.nih.gov/38856641/)). Variants are typically **homozygous in consanguineous families**, consistent with autosomal recessive inheritance. Most truncating variants are predicted to trigger **nonsense-mediated decay** or yield non-functional truncated protein ([PMID: 40874560](https://pubmed.ncbi.nlm.nih.gov/40874560/)). Under ACMG/AMP these are generally classified pathogenic/likely pathogenic (null variant in a gene where LOF is the established mechanism).

### Finding 7 — The *Prg4*-null mouse recapitulates key CACP features

The lubricin-deficient (*Prg4⁻/⁻*) mouse is the primary disease model. Mice are viable and fertile with normal joints at birth, then develop age-dependent cartilage-surface protein deposits, superficial-zone chondrocyte loss, synovial intimal hyperplasia, and periarticular pathology: *"tendon and tendon sheath involvement was present in the ankle joints, where morphologic changes and abnormal calcification of these structures were observed"* ([PMID: 15719068](https://pubmed.ncbi.nlm.nih.gov/15719068/)) — relevant to the camptodactyly/contracture phenotype. Stereological analysis confirms deficient superficial/upper-intermediate-zone chondrocyte cellularity with caspase-3/TUNEL-positive apoptosis ([PMID: 26975998](https://pubmed.ncbi.nlm.nih.gov/26975998/)). In the temporomandibular joint, *"as early as 2 weeks of age, mutant mice exhibited hyperplasia in the glenoid fossa articular cartilage, articular disc, and synovial membrane"* progressing to osteoarthritic degradation, ectopic cartilage, and mineralization ([PMID: 24834922](https://pubmed.ncbi.nlm.nih.gov/24834922/); [PMID: 26945615](https://pubmed.ncbi.nlm.nih.gov/26945615/); [PMID: 26534931](https://pubmed.ncbi.nlm.nih.gov/26534931/)). Ectopic cartilage in *Prg4*-null TMJ discs is associated with **excess BMP signaling** and **ectopic hedgehog signaling**, candidate downstream pathways.

### Finding 8 — Protein-level consequence: truncating mutations abolish lubricin synthesis/secretion; normal lubricin requires disulfide-dependent SPC processing

In patients carrying frameshift or nonsense *PRG4* mutations, *"the antiserum did not detect lubricin in synovial fluid or cultured synoviocytes from several patients with frameshift or nonsense mutations in PRG4"* ([PMID: 16000300](https://pubmed.ncbi.nlm.nih.gov/16000300/)) — direct evidence that the disease mechanism is **loss of protein (absent synthesis/secretion)**. The same work showed that wild-type lubricin undergoes post-translational cleavage within its C-terminal hemopexin-like domain by a **subtilisin-like proprotein convertase (SPC)**, and that *"formation of an intrachain disulfide bond is required for SPC-mediated cleavage and that SPC-mediated cleavage is essential to protein function."* Epitope mapping localizes key monoclonal-antibody epitopes to O-linked oligosaccharides on the mucin-domain KEPAPTTT motif ([PMID: 25642942](https://pubmed.ncbi.nlm.nih.gov/25642942/)).

### Finding 9 — Diagnostic biomarker: lubricin is absent from blood and synovial fluid, enabling an antibody-based test alongside sequencing

Epitope-specific anti-lubricin monoclonal antibodies (raised in *Prg4⁻/⁻* mice) detect lubricin in healthy individuals but not in CACP patients: *"the competition ELISA detected lubricin in blood samples from healthy individuals but not from patients with CACP, indicating blood can be used in a diagnostic test for patients suspected of having CACP"* ([PMID: 25642942](https://pubmed.ncbi.nlm.nih.gov/25642942/)). This provides a **blood-based screening/confirmation assay**. Definitive diagnosis remains *PRG4* sequencing (WES/WGS/single-gene) ([PMID: 38856641](https://pubmed.ncbi.nlm.nih.gov/38856641/)). Supporting distinguishing labs/imaging: normal ESR/CRP; non-inflammatory synovial fluid (gelatinous, viscous, low WBC, sterile — [PMID: 41637065](https://pubmed.ncbi.nlm.nih.gov/41637065/)); musculoskeletal ultrasound shows marked synovial effusion and circumferential synovial hypertrophy **without power Doppler activity** ([PMID: 41637065](https://pubmed.ncbi.nlm.nih.gov/41637065/)); radiographs show joint effusion/synovial debris without erosions, coxa vara, short femoral neck, and metaphyseal flaring ([PMID: 42074176](https://pubmed.ncbi.nlm.nih.gov/42074176/)).

### Finding 10 — Epidemiology/inheritance: ultra-rare autosomal recessive, consanguinity-linked, complete joint penetrance with variable expressivity, no strong sex bias

CACP is an ultra-rare monogenic autosomal recessive disorder (OMIM 208250) with **no established population prevalence**; only a few hundred cases and ~36 catalogued mutations are reported worldwide ([PMID: 36694203](https://pubmed.ncbi.nlm.nih.gov/36694203/)). Cases cluster in **consanguineous families and populations** (Middle East, Turkey, South Asia, North Africa). The 13-patient cohort derived from *"eight consanguineous Indian families"* with 7 females and 6 males ([PMID: 38856641](https://pubmed.ncbi.nlm.nih.gov/38856641/)), indicating **no strong sex predilection**. Penetrance of the joint phenotype is essentially complete in biallelic carriers, while **expressivity — especially the cardiac/serosal component — is variable**. Regionally, a Southeastern Turkey series identified CACP in 12 of 47 individuals evaluated for non-inflammatory musculoskeletal complaints mimicking rheumatic disease ([PMID: 40626694](https://pubmed.ncbi.nlm.nih.gov/40626694/)), underscoring its relative frequency among genetic JIA mimics in consanguineous populations.

### Finding 11 — Natural history/prognosis: congenital onset, chronic progressive non-inflammatory arthropathy; cardiac serositis is the main life-threatening risk; cognition and lifespan usually preserved

Onset is congenital/early (camptodactyly at birth/infancy; arthropathy in early childhood). The course is **chronic and progressive**: *"deficiency of PRG4 results in progressive worsening of joint deformity with age"* ([PMID: 38856641](https://pubmed.ncbi.nlm.nih.gov/38856641/)), producing large-joint contractures, coxa vara/short femoral neck, and *"precocious joint failure"* ([PMID: 15719068](https://pubmed.ncbi.nlm.nih.gov/15719068/)). Reduced bone mineral density has been reported as part of a broader phenotypic burden ([PMID: 42482035](https://pubmed.ncbi.nlm.nih.gov/42482035/)). Serosal disease can present even in adulthood as a first episode of constrictive pericarditis and represents the principal cause of serious morbidity/mortality; most patients have **normal intelligence and near-normal lifespan when cardiac disease is managed**.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic truncating mutation in *PRG4*** (frameshift/nonsense) **leads to** loss of full-length lubricin mRNA/protein via nonsense-mediated decay or non-functional truncated product *(demonstrated: lubricin undetectable in patient synovial fluid/synoviocytes, PMID 16000300)*.
2. Absent lubricin **results in** loss of boundary lubrication at articular cartilage and serosal surfaces, **and in parallel** loss of the normal inhibitory signal that restrains synovial intimal cell proliferation *(demonstrated in mouse/in vitro, PMID 15719068)*.

   **→ Branch A (cartilage/joint):**
   - 3a. Loss of lubrication **leads to** an elevated coefficient of friction at the cartilage surface *(demonstrated, PMID 23530215; 28604608)*.
   - 4a. Increased friction **results in** superficial-zone chondrocyte mitochondrial dysregulation and caspase-3–mediated apoptosis, **leading to** depletion of superficial-zone chondrocytes and surface protein deposition *(demonstrated, PMID 23530215, 26975998, 28604608)*.
   - 5a. In parallel, de-repressed synovial intimal cells **undergo hyperplasia**, producing non-inflammatory synovial thickening and effusion *(demonstrated, PMID 15719068)*.
   - 6a. Progressive cartilage failure + synovial hyperplasia **leads to** precocious large-joint arthropathy, contractures (camptodactyly, inferred from tendon/sheath involvement), and, at the hip, coxa vara with short femoral neck *(clinical, PMID 38856641, 15719068)*.

   **→ Branch B (serosa):**
   - 3b. Absent lubricin on pericardial/pleural serosal surfaces **leads to** non-inflammatory serosal effusion, **which can result in** fibrosis/constrictive pericarditis *(clinical, variable expressivity; PMID 40475173, 38955384)*.

### Upstream vs downstream

- **Upstream (initiating):** *PRG4*-null genotype → absent lubricin protein.
- **Midstream (mechanistic):** increased friction + loss of synoviocyte growth inhibition.
- **Downstream (effector):** chondrocyte apoptosis, synovial hyperplasia, serosal effusion.
- **Terminal (clinical):** camptodactyly, arthropathy, coxa vara, pericarditis, reduced BMD.

### Cell types, tissues, and compartments

| Level | Entities | Suggested ontology |
|---|---|---|
| Cells | Superficial-zone chondrocyte; synovial intimal cell (synoviocyte) | CL:0000138; CL:0000214 |
| Tissue | Articular cartilage, synovial membrane, tendon/sheath, pericardium, pleura | UBERON:0002418, 0002103, 0000043, 0002407, 0000977 |
| Organ/system | Joints (hip, knee, wrist, ankle, elbow, fingers, TMJ), heart (pericardium), lung (pleura), skeleton (femoral neck) | Musculoskeletal + cardiovascular + respiratory |
| Subcellular | Extracellular space (secreted lubricin); chondrocyte mitochondria (apoptotic signaling) | GO:0005615; GO:0005739 |
| Processes | Boundary lubrication, apoptotic process, negative regulation of cell proliferation | GO:0006915; GO:0008285 |

### Mechanistic nuances

- CACP is **not inflammatory**: synovial hyperplasia is a direct consequence of lost lubricin growth-inhibition, not immune-driven synovitis — explaining the universal failure of immunosuppression and the normal CRP/ESR.
- Mouse models reveal **downstream signaling perturbations** (ectopic hedgehog and excess BMP signaling driving ectopic cartilage/osteophytes in the TMJ; PMID 26945615, 26534931), which are candidate secondary pathways best characterized in the TMJ model rather than in human CACP tissue.

---

## Evidence Base

| PMID | Title (abbrev.) | Source type | Contribution |
|---|---|---|---|
| [10545950](https://pubmed.ncbi.nlm.nih.gov/10545950/) | *CACP, encoding a secreted proteoglycan, is mutated in CACP* | Human genetics | Establishes *PRG4* as causal gene (positional cloning) |
| [38856641](https://pubmed.ncbi.nlm.nih.gov/38856641/) | *Thirteen Indians with CACP syndrome* | Human cohort | Biallelic LOF; phenotype frequencies; 5 novel variants; progression |
| [15719068](https://pubmed.ncbi.nlm.nih.gov/15719068/) | *Lubricin protects cartilage and inhibits synovial overgrowth* | Mouse / in vitro | Dual mechanism; precocious joint failure; tendon pathology |
| [23530215](https://pubmed.ncbi.nlm.nih.gov/23530215/) | *Lubricin and prevention of chondrocyte apoptosis* | In vitro / mouse | Friction ↔ apoptosis causal link |
| [28604608](https://pubmed.ncbi.nlm.nih.gov/28604608/) | *Friction-induced mitochondrial dysregulation in Prg4 KO* | Mouse | Caspase-3/mitochondrial chondrocyte death |
| [16000300](https://pubmed.ncbi.nlm.nih.gov/16000300/) | *Consequences of disease-causing mutations on lubricin* | In vitro / human | Truncating mutations abolish protein; SPC/disulfide processing |
| [25642942](https://pubmed.ncbi.nlm.nih.gov/25642942/) | *Anti-lubricin monoclonal antibodies* | In vitro / human | Blood-based diagnostic assay (lubricin absent in CACP) |
| [28129516](https://pubmed.ncbi.nlm.nih.gov/28129516/) | *Intra-articular rhPRG4 in Yucatan minipig* | Large-animal | Preclinical rationale for rhPRG4 replacement |
| [40475173](https://pubmed.ncbi.nlm.nih.gov/40475173/) | *CACP caused by truncating mutations (JIA mimic)* | Human | Misdiagnosis as JIA; biologic exposure; pericarditis variable |
| [40830943](https://pubmed.ncbi.nlm.nih.gov/40830943/) | *First Iranian CACP case* | Human | Tetrad; failure of NSAIDs/MTX/steroids; pleural effusion |
| [38955384](https://pubmed.ncbi.nlm.nih.gov/38955384/) | *CACP syndrome review/cases* | Human | Constrictive pericarditis → pericardiectomy; TB misdiagnosis |
| [38523390](https://pubmed.ncbi.nlm.nih.gov/38523390/) | *CACP with mitral stenosis* | Human | Rare cardiac valve association |
| [36694203](https://pubmed.ncbi.nlm.nih.gov/36694203/) | *Novel PRG4 mutation, two sisters* | Human | Quantifies ~36 known mutations (rarity) |
| [26975998](https://pubmed.ncbi.nlm.nih.gov/26975998/) | *Superficial-zone cellularity deficient in lubricin-null mice* | Mouse | Stereological chondrocyte loss + caspase-3 |
| [24834922](https://pubmed.ncbi.nlm.nih.gov/24834922/) | *Lubricin required for TMJ integrity* | Mouse | TMJ hyperplasia model recapitulation |
| [26945615](https://pubmed.ncbi.nlm.nih.gov/26945615/) / [26534931](https://pubmed.ncbi.nlm.nih.gov/26534931/) | *Ectopic hedgehog / excess BMP in Prg4-null TMJ* | Mouse | Downstream signaling pathways |
| [41637065](https://pubmed.ncbi.nlm.nih.gov/41637065/) | *MSUS of CACP joints* | Human | Synovial hypertrophy/effusion without power Doppler; sterile fluid |
| [42482035](https://pubmed.ncbi.nlm.nih.gov/42482035/) | *CACP with bone-health emphasis* | Human | Novel variants; reduced BMD; JIA mimic |
| [40626694](https://pubmed.ncbi.nlm.nih.gov/40626694/) | *Genetic diseases mimicking rheumatic disorders (Turkey)* | Human | CACP among JIA mimics in consanguineous population |
| [25297354](https://pubmed.ncbi.nlm.nih.gov/25297354/) | *Novel PRG4 mutations in Indian families* | Human | Early frameshift variants from India |

**Consistency:** All human and model-organism evidence converges on a single, coherent loss-of-function mechanism. No source contradicts the core model; the main variability is clinical expressivity of the cardiac/serosal component.

---

## Section-by-Section Compendium

**1. Disease information.** CACP (MONDO:0008828; OMIM 208250; ORPHA:1236). Synonyms: Camptodactyly-arthropathy-coxa vara-pericarditis syndrome; CACP syndrome; arthropathy-camptodactyly syndrome; familial arthropathy. Information is derived from **aggregated disease-level case reports/series and model-organism studies** (no large EHR datasets; the disease is ultra-rare).

**2. Etiology.** Purely **genetic** — biallelic LOF of *PRG4*. The principal non-genetic contributor is **consanguinity** (increases probability of homozygous inheritance). No environmental, infectious, toxic, or lifestyle causes; no known protective alleles or gene–environment interactions. Not applicable: GWAS loci, common susceptibility SNPs.

**3. Phenotypes.** Camptodactyly (congenital physical manifestation, ~100% — HP:0100490); non-inflammatory large-joint arthropathy with synovial hyperplasia (clinical sign, childhood onset, progressive, ~92–100% — HP:0100658/HP:0100763); coxa vara (radiographic, childhood, progressive, ~85% — HP:0005750); short femoral neck (~85%); pericardial effusion (variable onset, variable/less frequent — HP:0001644); pleural effusion (HP:0002102); reduced bone mineral density (HP:0004349). Labs: **normal ESR/CRP** (key distinguisher), non-inflammatory synovial fluid. Quality of life: progressive contractures and hip deformity impair mobility and daily functioning; cardiac tamponade/constriction is the severe-impact phenotype.

**4. Genetic/molecular.** Causal gene *PRG4* (HGNC:9361; 1q31.1; OMIM 605602). Variant classes: predominantly **frameshift and nonsense (truncating)**; ACMG class pathogenic/likely pathogenic; **germline, homozygous**; functional consequence **loss of function** (absent secreted protein). Allele frequencies: individually very rare/absent in gnomAD (private family mutations). No established modifier genes, disease-specific epigenetic signatures, or large chromosomal abnormalities.

**5. Environmental.** None causal. No toxins, infectious agents, or lifestyle factors. (Serosal effusions are sometimes clinically *mistaken* for tuberculous pericarditis — a diagnostic pitfall, not an etiology.)

**6. Mechanism.** See causal chain above. Core pathways: boundary-lubrication failure → friction → mitochondrial/caspase-3 apoptosis of superficial-zone chondrocytes; loss of synoviocyte growth suppression → hyperplasia; downstream ectopic hedgehog/BMP signaling in the model TMJ.

**7. Anatomical structures.** Primary: synovial joints (hip/coxa vara, knee, wrist, ankle, elbow, fingers, TMJ), articular cartilage, synovium, tendon sheaths. Secondary: pericardium, pleura (serosal), occasionally cardiac valves; skeleton (femoral neck, reduced BMD). Bilateral/symmetrical joint involvement. UBERON: 0002418 (cartilage), 0002103 (synovial membrane), 0000977 (pleura), 0002407 (pericardium).

**8. Temporal development.** Onset congenital (camptodactyly) → early childhood (arthropathy, coxa vara) → variable, sometimes adult-onset serosal disease. Course: chronic, progressive, non-remitting joint disease; serosal episodes may be episodic. Lifelong. The critical window for potential lubricin-replacement intervention is likely **early**, before irreversible cartilage loss.

**9. Inheritance & population.** Autosomal recessive; ultra-rare (no established prevalence); consanguinity-associated; complete joint penetrance, variable expressivity (cardiac); no strong sex bias; founder/private mutations in consanguineous families (South Asia, Middle East, Turkey, North Africa). Carrier frequency not established.

**10. Diagnostics.** Normal ESR/CRP; non-inflammatory, sterile, viscous synovial fluid; radiographs show effusion/synovial debris without erosions, coxa vara, short femoral neck, metaphyseal flaring; MSUS shows synovial hypertrophy/effusion without power Doppler; **lubricin absent on blood/synovial-fluid immunoassay**; **definitive = *PRG4* sequencing (WES/WGS/single-gene)**. Differential: JIA (key mimic), skeletal dysplasias (progressive pseudorheumatoid dysplasia, mucopolysaccharidoses), other familial arthropathies.

**11. Prognosis.** Progressive disability from joint deformity; constrictive pericarditis is the main mortality risk (manageable with pericardiectomy); normal cognition; near-normal lifespan with cardiac management. Main prognostic factor: presence/severity of cardiac involvement.

**12. Treatment.** No cure. Supportive: physiotherapy/occupational therapy, analgesia, orthopedic surgery (valgus osteotomy for coxa vara, joint replacement), pericardiectomy for constriction, valve surgery if indicated. Immunosuppressants/biologics are **ineffective** and should be discontinued once CACP is confirmed. Investigational: **rhPRG4 replacement** (preclinical). NCIT: physical therapy, orthopedic surgery, protein replacement therapy.

**13. Prevention.** No primary prevention. **Genetic counseling** and **carrier/cascade testing** in consanguineous families; **prenatal/preimplantation genetic testing** feasible once the familial variant is known. Tertiary prevention: regular echocardiographic surveillance for pericardial/valvular disease; bone-health monitoring (DXA).

**14. Other species / natural disease.** Orthologous gene: mouse *Prg4* (NCBI Gene 56689). The *Prg4⁻/⁻* mouse is an engineered (not natural) model; no well-established spontaneous CACP-equivalent natural disease in companion animals is documented in this knowledge base. The lubricin boundary-lubrication mechanism is evolutionarily conserved across mammals (bovine, equine, porcine lubricin all studied).

**15. Model organisms.** Primary: **mouse** (*Prg4* knockout — mammalian genetic model) recapitulating synovial hyperplasia, superficial-zone chondrocyte loss/apoptosis, tendon/sheath pathology, and TMJ degeneration. Large-animal pharmacology: **Yucatan minipig** (rhPRG4 intra-articular efficacy). In vitro: bovine cartilage explants, synoviocyte cultures. Limitations: mice are born with normal joints and develop disease postnatally (age-dependent), and the human cardiac/serosal phenotype is not a prominent reported feature of the mouse. Resource: MGI (*Prg4*).

---

## Limitations and Knowledge Gaps

1. **No epidemiological denominator.** Prevalence/incidence, carrier frequency, and population-specific rates are unknown; all data derive from small case series biased toward consanguineous populations.
2. **Cardiac mechanism under-characterized.** Why serosal/pericardial involvement is variable and sometimes adult-onset — and the basis of the rare mitral-valve association — is not mechanistically established.
3. **Weak genotype–phenotype correlation.** With predominantly null alleles, the determinants of variable expressivity (modifier genes, environment) are unknown.
4. **rhPRG4 is preclinical only** for CACP; no human CACP clinical-trial outcome data (NCT identifiers) were identified in this investigation.
5. **Mouse-model gaps.** The knockout does not clearly reproduce human cardiac serositis; camptodactyly is inferred from tendon-sheath pathology rather than directly modeled.
6. **No omics in CACP patients.** Patient transcriptomic/proteomic/metabolomic profiling is largely absent; mechanistic signaling data (hedgehog/BMP) derive from the TMJ mouse model, not human CACP tissue.
7. **Bone-health phenotype newly emerging.** Reduced BMD is reported in isolated cases ([PMID: 42482035](https://pubmed.ncbi.nlm.nih.gov/42482035/)) but frequency and mechanism are undefined.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international CACP registry / natural-history cohort** to define prevalence, phenotype frequencies (especially cardiac penetrance by age), and progression rates.
2. **Advance rhPRG4 toward a first-in-human CACP trial** — intra-articular dosing informed by minipig data ([PMID: 28129516](https://pubmed.ncbi.nlm.nih.gov/28129516/)); define outcome measures (MSUS synovial hypertrophy, friction surrogates, joint function).
3. **Validate the lubricin blood immunoassay** ([PMID: 25642942](https://pubmed.ncbi.nlm.nih.gov/25642942/)) as a first-line, low-cost diagnostic screen to shorten the diagnostic odyssey and curb inappropriate biologic use.
4. **Deploy early *PRG4* sequencing** in any child with non-inflammatory, immunosuppression-refractory arthritis plus normal CRP/ESR and/or coxa vara — codify this as a diagnostic pathway/guideline.
5. **Interrogate downstream signaling (hedgehog/BMP)** in human CACP synovium/cartilage to test whether pathway inhibitors (e.g., BMP-receptor kinase inhibitors) could serve as adjunct therapies, building on TMJ-model findings ([PMID: 26534931](https://pubmed.ncbi.nlm.nih.gov/26534931/)).
6. **Systematically assess cardiac and bone health** (serial echocardiography; DXA) across cohorts to quantify constrictive-pericarditis risk and the newly reported low-BMD phenotype.
7. **Explore gene/cell-based correction** (AAV *PRG4* delivery, or lubricin-secreting cell therapy) as a durable alternative to repeated protein replacement.

---

*Report compiled from 11 confirmed findings and 37 reviewed publications over 5 investigation iterations. Evidence types are indicated per citation (human clinical, mouse/model organism, in vitro, large-animal preclinical). Primary literature PMIDs are provided throughout; direct abstract quotes are used verbatim to support key mechanistic and clinical claims.*


## Artifacts

- [OpenScientist final report](Camptodactyly-Arthropathy-Coxa_Vara-Pericarditis_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Camptodactyly-Arthropathy-Coxa_Vara-Pericarditis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0005750` (2 mentions) - the report calls it "coxa vara"; HP calls it **Lower-limb joint contracture**
- `HP:0001644` (2 mentions) - the report calls it "pericardial effusion"; HP calls it **Dilated cardiomyopathy**
- `HP:0100658` (2 mentions) - the report calls it "joint effusion"; HP calls it **Cellulitis**
- `HP:0100763` (2 mentions) - the report calls it "synovial hypertrophy"; HP calls it **Abnormality of the lymphatic system**
- `NCIT:C15431` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Hematopoietic Cell Transplantation**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (2 mentions) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005615` (2 mentions) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names
- `GO:0008285` (2 mentions) - the report calls it "negative regulation of cell proliferation"; GO calls it **negative regulation of cell population proliferation**, and lists "negative regulation of cell proliferation" among its other names
- `HP:0002102` (2 mentions) - the report calls it "pleural effusion"; HP calls it **Pleuritis**, and lists "Pleurisy" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.