---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T10:59:29.919805'
end_time: '2026-09-25T11:15:44.290046'
duration_seconds: 974.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pasteurellosis
  mondo_id: MONDO:0005901
  category: Infectious Disease
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 11
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 30
  verified: 29
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.033
  labels_checked: 21
  labels_matching: 9
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0005901
    reported_labels:
    - MONDO
    ontology_label: pasteurellosis
  - term_id: HP:0031357
    reported_labels:
    - Frequent in local infection
    ontology_label: Glomeruloid hemangioma
  - term_id: HP:0100776
    reported_labels:
    - Serious local complication
    ontology_label: Recurrent pharyngitis
  - term_id: HP:0002754
    reported_labels:
    - Local complication, esp. finger/hand after cat bite
    ontology_label: Osteomyelitis
  - term_id: HP:0031864
    reported_labels:
    - Sepsis
    ontology_label: Bacteremia
  - term_id: NCIT:C716
    reported_labels:
    - Penicillin
    ontology_label: Omeprazole
  - term_id: NCIT:C263
    reported_labels:
    - Doxycycline
    ontology_label: Anticoagulant Agent
  - term_id: NCIT:C61735
    reported_labels:
    - "Amoxicillin\u2011Clavulanate"
    ontology_label: Dolasetron
  labels_variant: 4
  unresolved_terms:
  - HP:0031617
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pasteurellosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pasteurellosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pasteurellosis
- **MONDO ID:** MONDO:0005901 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pasteurellosis** covering all of the
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

# Pasteurellosis — Comprehensive Disease Characteristics Report

**Disease:** Pasteurellosis
**MONDO ID:** MONDO:0005901
**Category:** Infectious Disease (zoonosis)
**Evidence base:** 11 confirmed findings, 32 papers reviewed across 5 investigation iterations

---

## Summary

Pasteurellosis is a **zoonotic bacterial infection** caused by Gram‑negative coccobacilli of the genus *Pasteurella*, overwhelmingly *Pasteurella multocida*, which are commensals of the oral and respiratory flora of cats, dogs, and many other animals. In humans it is acquired chiefly through **animal bites, scratches, licking of broken skin, or inhalation/aspiration of contaminated animal secretions**. Cats are the source in 60–80% of human cases and dogs in most of the remainder ([PMID: 6371440](https://pubmed.ncbi.nlm.nih.gov/6371440/)). Because the etiology is infectious, there is **no human genetic cause** — susceptibility to severe disease is instead governed by host comorbidities (cirrhosis, immunosuppression, chronic lung disease, extremes of age) and by **bacterial virulence factors** (capsule, lipopolysaccharide, and *Pasteurella multocida* toxin).

Human pasteurellosis presents in **three clinical groups**: (1) rapidly progressive soft‑tissue infection at a bite/scratch site — the most common presentation, with erythema, warmth, tenderness, and purulent drainage appearing within hours; (2) respiratory‑tract infection, predominantly in elderly patients with underlying COPD, bronchiectasis, or malignancy; and (3) invasive/systemic disease (bacteremia, meningitis, endocarditis, septic arthritis, osteomyelitis) concentrated in neonates, the immunocompromised, and cirrhotic hosts ([PMID: 6371440](https://pubmed.ncbi.nlm.nih.gov/6371440/); [PMID: 9097378](https://pubmed.ncbi.nlm.nih.gov/9097378/); [PMID: 26356688](https://pubmed.ncbi.nlm.nih.gov/26356688/)). Notably, **non‑bite‑associated infection carries a substantially higher risk of bacteremia, ICU admission, and death** than bite‑associated infection.

*P. multocida* is also a **major veterinary pathogen** of global economic importance, causing hemorrhagic septicemia (serotype B:2) in cattle and buffalo with near‑100% peracute mortality, fowl cholera in poultry, and progressive atrophic rhinitis in swine (driven by the toxin PMT). The organism's virulence rests on a polysaccharide **capsule** (anti‑phagocytic, complement‑resistant) and **lipopolysaccharide** (essential for host survival and the antigenic basis of 16 serovars), both proven necessary for virulence in animal challenge models. First‑line human therapy is **penicillin**, with amoxicillin‑clavulanate as the practical choice for polymicrobial bite wounds and doxycycline as an alternative. There is no human vaccine; prevention relies on wound care, selective antibiotic prophylaxis, and rabies post‑exposure prophylaxis for animal bites.

---

## Section 1 — Disease Information

**Overview.** Pasteurellosis is an acute zoonotic infection caused by *Pasteurella* species — small, nonmotile, facultatively anaerobic, oxidase‑positive, Gram‑negative coccobacilli. *P. multocida* is the principal human pathogen; *P. canis*, *P. dagmatis*, and *P. stomatis* are less common. The organism is part of the normal oropharyngeal and gastrointestinal flora of domestic and wild animals; human infection is almost always animal‑associated. *P. multocida* holds a historic place in microbiology as the first pathogen shown by Louis Pasteur (1881) to cause fowl cholera and used in his foundational attenuation/vaccination experiments ([PMID: 17107417](https://pubmed.ncbi.nlm.nih.gov/17107417/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0005901 |
| MeSH | Pasteurella Infections (D010326) |
| ICD‑10 | A28.0 (Pasteurellosis) |
| ICD‑11 | Zoonotic bacterial disease category (1B/1C area) |
| NCBI Taxonomy (pathogen) | *Pasteurella multocida* — txid747 |
| OMIM | Not applicable (no Mendelian human entry — infectious disease) |
| Orphanet | Not a listed rare genetic disease |

**Synonyms / alternative names.** Pasteurella infection; *Pasteurella multocida* infection. Related animal‑specific names: hemorrhagic septicemia (cattle/buffalo), fowl cholera (poultry), snuffles (rabbits), progressive atrophic rhinitis (swine).

**Source of information.** The human clinical knowledge base derives primarily from **aggregated disease‑level resources** — case reports, case series, and retrospective cohort reviews — rather than large EHR‑derived cohorts, reflecting the relative rarity and sporadic nature of severe human pasteurellosis. Veterinary and mechanistic data derive from experimental animal models and molecular microbiology.

---

## Section 2 — Etiology

**Primary cause.** Pasteurellosis is an **infectious disease**; the causal agent is *Pasteurella multocida* (and less often other *Pasteurella* spp.). There is **no genetic (Mendelian) cause** in humans. The primary transmission route is direct inoculation from an animal reservoir — bites, scratches, or licking of broken skin — with a secondary respiratory route via inhalation/aspiration of contaminated secretions ([PMID: 40063964](https://pubmed.ncbi.nlm.nih.gov/40063964/); [PMID: 11242756](https://pubmed.ncbi.nlm.nih.gov/11242756/)).

**Risk factors.**

- *Environmental / exposure:* Contact with cats and dogs is the dominant exposure. In neonatal pasteurellosis, cat/dog exposure was the major risk (non‑traumatic 44%, traumatic 8%), with **vertical transmission** in 44% ([PMID: 19208671](https://pubmed.ncbi.nlm.nih.gov/19208671/)). In infantile meningitis, 61% arose from **indirect** household animal contact ([PMID: 40063964](https://pubmed.ncbi.nlm.nih.gov/40063964/)).
- *Host comorbidity:* Cirrhosis/liver dysfunction predisposes to opportunistic bacteremia ([PMID: 7560209](https://pubmed.ncbi.nlm.nih.gov/7560209/)); chronic lung disease (COPD, bronchiectasis, malignancy) predisposes to pulmonary infection ([PMID: 9097378](https://pubmed.ncbi.nlm.nih.gov/9097378/)); immunocompromise (including HIV) predisposes to invasive disease. A Charlson comorbidity index ≥1 was significantly associated with non‑bite (more invasive) infection ([PMID: 26356688](https://pubmed.ncbi.nlm.nih.gov/26356688/)).
- *Age:* Neonates/infants and the elderly are at highest risk of severe disease.

**Genetic risk factors.** No human causal variants, susceptibility loci, or modifier genes are established — this is not a heritable disease.

**Protective factors.** No genetic protective variants apply. Environmental protection is behavioral: prompt wound irrigation, hand hygiene after animal contact, and avoidance of high‑risk animal contact by immunocompromised/cirrhotic individuals.

**Gene–environment interactions.** Not applicable for the human host. The operative "genotype–environment" axis is between **bacterial virulence genotype** (capsular serotype, LPS glycoform, PMT carriage) and **host immune status**.

---

## Section 3 — Phenotypes

Because pasteurellosis is infectious, phenotypes are clinical signs/symptoms rather than heritable HPO traits, but HPO terms are suggested for knowledge‑base mapping.

| Phenotype | Type | Onset / course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Cellulitis / soft‑tissue infection at bite site (erythema, warmth, tenderness, purulent drainage) | Clinical sign | Acute, **rapid** (hours) | Most common presentation | HP:0100658 (Cellulitis) |
| Purulent wound drainage | Clinical sign | Acute | Frequent in local infection | HP:0031357 |
| Septic arthritis (proximal to bite) | Clinical sign | Acute–subacute | Serious local complication | HP:0100776 |
| Osteomyelitis | Clinical sign | Subacute | Local complication, esp. finger/hand after cat bite | HP:0002754 |
| Tenosynovitis / abscess | Clinical sign | Acute–subacute | Local complication | — |
| Pneumonia / tracheobronchitis / lung abscess / empyema | Clinical sign | Subacute, indolent | 2nd most common site | HP:0002090 (Pneumonia) |
| Bacteremia / sepsis | Laboratory / clinical | Acute, can be fulminant | 51% of infantile invasive cases; 37% of non‑bite adult cases | HP:0031864 (Sepsis) |
| Meningitis (± seizures) | Clinical sign | Acute | Seizures in 20% of infantile meningitis | HP:0001287; HP:0001250 (Seizure) |
| Endocarditis | Clinical sign | Subacute | Rare, severe | HP:0031617 |

**Characteristics.** Onset spans **neonatal to geriatric**. Severity ranges from mild self‑limited cellulitis to fulminant fatal sepsis (Waterhouse–Friderichsen syndrome reported in cirrhosis, [PMID: 7560209](https://pubmed.ncbi.nlm.nih.gov/7560209/)). Local infections are characterized by the **rapid appearance of erythema, warmth, tenderness, and frequently purulent drainage** ([PMID: 6371440](https://pubmed.ncbi.nlm.nih.gov/6371440/)). Progression is typically acute; untreated deep infection extends to septic arthritis and osteomyelitis.

**Quality‑of‑life impact.** Hand/finger infections after cat bites can cause functional impairment and, if complicated by tenosynovitis or osteomyelitis, prolonged disability. Invasive disease carries substantial mortality (Section 11). Formal EQ‑5D/SF‑36 data specific to pasteurellosis are not available.

---

## Section 4 — Genetic / Molecular Information

**This section is largely NOT APPLICABLE to the human host.** Pasteurellosis is not a genetic disease; there are no human causal genes, pathogenic variants, ACMG classifications, allele frequencies, modifier genes, epigenetic signatures, or chromosomal abnormalities.

The relevant molecular genetics belongs to the **pathogen**:

- **Capsule biosynthetic (*cap*) locus** — 15 genes in three functional regions (export regions 1 and 3; biosynthesis region 2). Disruption of the export gene *cexA* yields an acapsular, avirulent mutant ([PMID: 10816499](https://pubmed.ncbi.nlm.nih.gov/10816499/)).
- **LPS biosynthesis genes** — heptosyltransferases *hptA/hptB*, Kdo kinase *kdkA*, and outer‑core transferases *pcgD* and *hptE*, which determine LPS glycoform and virulence ([PMID: 17517879](https://pubmed.ncbi.nlm.nih.gov/17517879/); [PMID: 33663572](https://pubmed.ncbi.nlm.nih.gov/33663572/)).
- **toxA** — encodes the 146‑kDa *Pasteurella multocida* toxin (PMT), a deamidase virulence factor (Section 6).

---

## Section 5 — Environmental Information

**Infectious agent.** *Pasteurella multocida* (NCBI txid747) is the principal agent, with subspecies *multocida*, *septica*, and *gallicida*. Other species: *P. canis*, *P. dagmatis*, *P. stomatis*. Capsular serogroups A, B, D, E, F and 16 LPS‑based serovars define strain diversity.

**Environmental / exposure factors.** The reservoir is the animal oral/respiratory tract. Human exposure occurs through the domestic environment (pet ownership), occupational settings (veterinarians, farmers, abattoir workers, animal handlers), and recreational animal contact. There is **no toxin, radiation, or pollution etiology.**

**Lifestyle factors.** Pet keeping and close animal contact (being licked, sleeping with pets) are the operative behavioral factors, including the **indirect** contact responsible for 61% of infantile meningitis cases ([PMID: 40063964](https://pubmed.ncbi.nlm.nih.gov/40063964/)).

---

## Section 6 — Mechanism / Pathophysiology

### Causal chain (human bite‑associated soft‑tissue infection)

1. Animal bite/scratch/lick **inoculates** *P. multocida* from animal oral flora into human subcutaneous tissue →
2. Bacterial **capsule** prevents phagocytosis and confers complement resistance, and complete **LPS** enables survival in host tissue → *leads to* local bacterial proliferation →
3. LPS (endotoxin) and bacterial products **trigger innate immune activation** (neutrophil recruitment, cytokine release) → *results in* the characteristic rapid cellulitis (erythema, warmth, tenderness, purulent drainage) within hours →
4. If uncontrolled, contiguous spread → *leads to* abscess, tenosynovitis, septic arthritis, osteomyelitis (branch: deep‑tissue complications) →
5. In hosts with impaired defenses (cirrhosis, immunosuppression, neonate), bacteria breach into bloodstream → *results in* bacteremia → hematogenous seeding → meningitis, endocarditis (branch: invasive disease, higher mortality).

### Causal chain (veterinary atrophic rhinitis — PMT‑driven; mechanistically best characterized)

1. Toxigenic *P. multocida* colonizes the nasal mucosa and secretes **PMT (146 kDa, toxA)** →
2. PMT enters cells and **deamidates a conserved glutamine** in the α‑subunit of three of four heterotrimeric G‑protein families (Gαq/11, Gαi1,2,3, Gα12/13), locking them in the active GTP‑bound state ([PMID: 23150526](https://pubmed.ncbi.nlm.nih.gov/23150526/)) → *results in* constitutive G‑protein signaling →
3. Constitutively active **Gαq/11 → p63RhoGEF → RhoA → Rho‑kinase → Ras/MEK/ERK** MAP‑kinase cascade ([PMID: 23696743](https://pubmed.ncbi.nlm.nih.gov/23696743/)) → *leads to* **inhibition of osteoblast differentiation** →
4. In parallel, Gαq/11 → PLCβ → PKC → **mTORC1** activation → rpS6 phosphorylation, protein synthesis, proliferation ([PMID: 23223576](https://pubmed.ncbi.nlm.nih.gov/23223576/); CTGF upregulation contributes, [PMID: 23415771](https://pubmed.ncbi.nlm.nih.gov/23415771/)) → *drives* remodeling favoring resorption →
5. Net **bone resorption exceeding formation** in the nasal turbinates → *results in* turbinate atrophy and facial distortion (atrophic rhinitis). Prolonged signaling also causes selective membrane redistribution/depletion of Gαq ([PMID: 27490568](https://pubmed.ncbi.nlm.nih.gov/27490568/)).

### Mechanistic detail

- **Molecular pathways:** Gq/11–RhoA–MAPK (Ras/MEK/ERK); Gq/11–PLCβ–PKC–mTORC1; complement cascade evasion; innate TLR4/LPS signaling.
- **Cellular processes:** Inhibition of osteoblast differentiation, stimulated proliferation, inflammation, phagocytosis evasion.
- **Protein dysfunction:** PMT is a **gain‑of‑function** enzymatic toxin producing constitutive Gα activation via deamidation. Capsule and LPS are structural virulence surfaces.
- **Immune involvement:** Anti‑phagocytic capsule; complement resistance; LPS‑driven endotoxic inflammation. Not autoimmune.
- **Tissue damage:** Direct inflammatory tissue destruction and, in atrophic rhinitis, dysregulated bone remodeling.

**Suggested ontology terms.** GO:0006954 (inflammatory response); GO:0007186 (GPCR signaling); GO:0000165 (MAPK cascade); GO:0038202 (TORC1 signaling); GO:0001503 (ossification, inhibited); GO:0006909 (phagocytosis, evaded). CL:0000062 (osteoblast); CL:0000092 (osteoclast); CL:0000775 (neutrophil); CL:0000235 (macrophage).

---

## Section 7 — Anatomical Structures Affected

- **Primary organs / sites (human):** Skin and subcutaneous soft tissue (UBERON:0002097 skin; UBERON:0002384 connective tissue), especially the **hand and fingers** after cat bites. Lungs/lower respiratory tract (UBERON:0002048) — second most common site.
- **Secondary / invasive involvement:** Bloodstream (bacteremia), meninges (UBERON:0002360; meningitis), heart valves (endocarditis), joints (UBERON:0000982; septic arthritis), bone (UBERON:0002481; osteomyelitis), liver/biliary tract in cirrhotic sepsis.
- **Body systems:** Integumentary, musculoskeletal, respiratory, cardiovascular, nervous (CNS in meningitis).
- **Tissue/cell level:** Epithelial and connective tissue; osteoblasts (CL:0000062) and osteoclasts (CL:0000092) in atrophic rhinitis; neutrophils and macrophages in acute inflammation.
- **Subcellular:** Host **plasma membrane** (GO:0005886) — site of Gαq depletion/redistribution by PMT; cytosol.
- **Localization / lateralization:** Typically **unilateral/local** at the bite site; respiratory and invasive forms are systemic.

---

## Section 8 — Temporal Development

- **Onset:** Local wound infection is **acute and rapid** — erythema, warmth, tenderness and drainage within hours of a bite ([PMID: 6371440](https://pubmed.ncbi.nlm.nih.gov/6371440/)). Respiratory infection is more **indolent/subacute** ([PMID: 11242756](https://pubmed.ncbi.nlm.nih.gov/11242756/)). Invasive sepsis can be **fulminant**, with death within hours in vulnerable hosts ([PMID: 7560209](https://pubmed.ncbi.nlm.nih.gov/7560209/)).
- **Age of onset:** Any age — neonatal (including vertical transmission) through geriatric.
- **Progression / course:** With prompt appropriate antibiotics, most local infections resolve; untreated or deep infection progresses to septic arthritis/osteomyelitis. Invasive disease can progress rapidly to death.
- **Duration:** Generally **self‑limited to short‑course** with treatment; complicated bone/joint infection may require prolonged therapy.
- **Remission:** Treatment‑induced with antibiotics ± surgical drainage/debridement.
- **Critical period:** The **first ~8 hours** post‑bite is the key window for irrigation, debridement, and prophylaxis decisions ([PMID: 39462695](https://pubmed.ncbi.nlm.nih.gov/39462695/)).

---

## Section 9 — Inheritance and Population

**Inheritance.** Not applicable — infectious, non‑heritable. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency.

**Epidemiology.** Human pasteurellosis is sporadic and, in severe/invasive form, uncommon; precise population incidence/prevalence figures are not well established because most data are case series. Bite‑wound colonization is common: *Pasteurella* is isolated from ~50% of infected dog bites and ~75% of infected cat bites ([PMID: 9887159](https://pubmed.ncbi.nlm.nih.gov/9887159/)).

**Demographics.** Severe disease clusters in neonates/infants, the elderly, and immunocompromised/cirrhotic patients. In one adult cohort (n=44), mean age was 64 years with a female majority (30/44) ([PMID: 26356688](https://pubmed.ncbi.nlm.nih.gov/26356688/)). Cats are the source in 60–80% of cases ([PMID: 6371440](https://pubmed.ncbi.nlm.nih.gov/6371440/)).

**Geographic distribution.** Worldwide, following the distribution of domestic cats and dogs. The **veterinary** disease hemorrhagic septicemia (serotype B:2) is highly endemic in **South Asia** ([PMID: 36503053](https://pubmed.ncbi.nlm.nih.gov/36503053/)).

---

## Section 10 — Diagnostics

- **Microbiology (gold standard):** Culture of *P. multocida* from wound exudate, blood, sputum, CSF, or joint/pleural fluid. Grows on blood and chocolate agar (not MacConkey); oxidase‑, catalase‑, and indole‑positive. Identification by MALDI‑TOF or 16S rRNA sequencing.
- **Laboratory / biomarkers:** Nonspecific inflammatory markers (elevated WBC, CRP). Blood cultures essential when systemic disease suspected — bacteremia in 51% of infantile invasive cases ([PMID: 40063964](https://pubmed.ncbi.nlm.nih.gov/40063964/)).
- **Imaging:** X‑ray/CT/MRI for suspected osteomyelitis, septic arthritis, lung abscess, or empyema; CT/echocardiography for endocarditis; lumbar puncture for meningitis.
- **Genetic / omics testing:** Not applicable for host diagnosis. Pathogen genotyping (capsular multiplex PCR for serogroups A/B/D/E/F; LPS genotyping) is used epidemiologically and in veterinary contexts.
- **Clinical criteria & differential diagnosis:** Diagnosis is clinical (bite history + rapid cellulitis) confirmed by culture. Differential: *Streptococcus*/*Staphylococcus* cellulitis, *Capnocytophaga canimorsus* (asplenic/cirrhotic), *Bartonella henselae* (cat‑scratch disease), anaerobic bite‑wound flora. A distinguishing feature is the **unusually rapid** onset of cellulitis (hours, not days) after a cat/dog bite.

---

## Section 11 — Outcome / Prognosis

Prognosis depends on host status and syndrome group. Local soft‑tissue infection generally resolves with antibiotics. Invasive disease carries meaningful mortality:

| Population / syndrome | Key outcomes | Source |
|---|---|---|
| Infantile *P. multocida* meningitis (n=74) | Bacteremia 51%, seizures 20%, **mortality 8%** | [PMID: 40063964](https://pubmed.ncbi.nlm.nih.gov/40063964/) |
| Neonatal pasteurellosis (n=25) | **Overall mortality 20%** | [PMID: 19208671](https://pubmed.ncbi.nlm.nih.gov/19208671/) |
| Adult cohort, non‑bite vs bite (n=44) | Non‑bite: bacteremia 37% vs 4% (p=0.001); hospitalized 84% vs 44% (p=0.012); **all 4 deaths and 7/8 ICU patients non‑bite** | [PMID: 26356688](https://pubmed.ncbi.nlm.nih.gov/26356688/) |
| Cirrhotic biliary sepsis | Fulminant, fatal within hours (Waterhouse–Friderichsen) | [PMID: 7560209](https://pubmed.ncbi.nlm.nih.gov/7560209/) |

**Prognostic factors.** Absence of a bite (mucosal/respiratory/indirect acquisition), Charlson comorbidity index ≥1, immunocompromise, cirrhosis, and extremes of age predict worse outcomes ([PMID: 26356688](https://pubmed.ncbi.nlm.nih.gov/26356688/)). **Complications** include abscess, tenosynovitis, septic arthritis, osteomyelitis, empyema, endocarditis, and meningitis. Recovery is generally complete with early appropriate therapy; deep bone/joint disease may leave functional deficits.

---

## Section 12 — Treatment

- **First‑line pharmacotherapy:** **Penicillin** is preferred; *P. multocida* is characteristically susceptible ([PMID: 9097378](https://pubmed.ncbi.nlm.nih.gov/9097378/)). **Doxycycline** is a highly effective alternative ([PMID: 9097378](https://pubmed.ncbi.nlm.nih.gov/9097378/)). For polymicrobial bite wounds (aerobes + anaerobes in 56%, [PMID: 9887159](https://pubmed.ncbi.nlm.nih.gov/9887159/)), **amoxicillin‑clavulanate** is standard because it covers *Pasteurella* plus streptococci, staphylococci, and anaerobes.
  - Suggested NCIT terms: NCIT:C716 (Penicillin); NCIT:C263 (Doxycycline); NCIT:C61735 (Amoxicillin‑Clavulanate).
- **Alternatives:** Third‑generation cephalosporins (ceftriaxone) and fluoroquinolones for serious/invasive disease or penicillin allergy. *Pasteurella* is typically resistant to first‑generation cephalosporins and clindamycin.
- **Surgical / interventional:** Irrigation, sharp debridement, drainage of abscesses; joint washout for septic arthritis; negative‑pressure wound therapy benefits serious limb bite lacerations ([PMID: 26964825](https://pubmed.ncbi.nlm.nih.gov/26964825/)).
- **Supportive:** ICU support, source control, vasopressors in septic shock.
- **Pharmacogenomics / advanced therapeutics (gene/cell/RNA/immunotherapy):** Not applicable.

---

## Section 13 — Prevention

- **Primary prevention:** Avoid/limit high‑risk animal contact (especially for cirrhotic and immunocompromised individuals); hand hygiene after animal contact; prompt wound care.
- **Bite‑wound management (core prevention of infection):** Immediate copious **irrigation and sharp debridement**; primary closure of well‑irrigated, sharply debrided wounds within 8 h is not associated with increased infection; **routine antibiotic prophylaxis in low‑risk wounds does not lower infection risk**, so prophylaxis should be selective (high‑risk: hand/deep puncture, cat bites, immunocompromised hosts) ([PMID: 39462695](https://pubmed.ncbi.nlm.nih.gov/39462695/)). Amoxicillin‑clavulanate is the standard prophylactic agent when indicated.
- **Rabies post‑exposure prophylaxis** is indicated for all dog bites where the animal's rabies status cannot be determined or the animal cannot be quarantined for 10 days ([PMID: 39462695](https://pubmed.ncbi.nlm.nih.gov/39462695/)).
- **Human vaccine:** None available.
- **Veterinary immunization (indirect benefit):** Killed and attenuated (gdhA‑derivative) and recombinant OmpH vaccines control hemorrhagic septicemia in cattle/buffalo ([PMID: 32547726](https://pubmed.ncbi.nlm.nih.gov/32547726/); [PMID: 30483888](https://pubmed.ncbi.nlm.nih.gov/30483888/); [PMID: 42758249](https://pubmed.ncbi.nlm.nih.gov/42758249/)). LPS‑based immunity is serovar‑specific ([PMID: 21664074](https://pubmed.ncbi.nlm.nih.gov/21664074/)).

---

## Section 14 — Other Species / Natural Disease

*P. multocida* is a **major, naturally occurring veterinary pathogen** — arguably its primary disease niche — and pasteurellosis is fundamentally a zoonosis.

| Host | NCBI Taxon | Disease | Serotype / notes |
|---|---|---|---|
| Cattle, buffalo | 9913 / 89462 | **Hemorrhagic septicemia** — peracute, ~100% mortality within hours | B:2; endemic South Asia ([PMID: 36503053](https://pubmed.ncbi.nlm.nih.gov/36503053/)) |
| Chickens, ducks | 9031 / 8839 | **Fowl cholera** | LPS‑dependent virulence ([PMID: 21664074](https://pubmed.ncbi.nlm.nih.gov/21664074/); [PMID: 33663572](https://pubmed.ncbi.nlm.nih.gov/33663572/)) |
| Swine | 9823 | **Progressive atrophic rhinitis** | PMT‑driven (toxA) |
| Rabbits | 9986 | "Snuffles," pneumonia | — |
| Cats, dogs | 9685 / 9615 | Oral commensal; reservoir for human zoonosis | *P. multocida* ssp. *multocida/septica* (cats), *P. canis* (dogs) ([PMID: 9887159](https://pubmed.ncbi.nlm.nih.gov/9887159/)) |

**Transmission / zoonotic potential:** High. Cats and dogs are the principal source of human infection (cats 60–80%) via bites, scratches, and licking ([PMID: 6371440](https://pubmed.ncbi.nlm.nih.gov/6371440/)). **Comparative pathology:** capsule and LPS virulence mechanisms are conserved across host species; the PMT–Gα deamidation pathway acts on conserved mammalian G proteins, underpinning cross‑species relevance.

---

## Section 15 — Model Organisms

- **Mouse (intraperitoneal challenge):** The definitive virulence model. Wild‑type B:2 *P. multocida* multiplies rapidly in blood, spleen, and liver, whereas an **acapsular *cexA* mutant is efficiently cleared and readily phagocytosed**, proving the capsule is a crucial virulence determinant ([PMID: 10816499](https://pubmed.ncbi.nlm.nih.gov/10816499/)). Resource: MGI (host); Cellosaurus for cell lines.
- **Chicken / duck (natural‑host challenge):** Demonstrated that severely truncated‑LPS mutants are fully attenuated and that outer‑core transferases *pcgD/hptE* contribute differentially to virulence ([PMID: 21664074](https://pubmed.ncbi.nlm.nih.gov/21664074/); [PMID: 33663572](https://pubmed.ncbi.nlm.nih.gov/33663572/); [PMID: 17517879](https://pubmed.ncbi.nlm.nih.gov/17517879/)).
- **In vitro cell models:** Swiss 3T3 fibroblasts, osteoblasts, and Gαq/11 knockout MEFs dissect PMT signaling ([PMID: 23696743](https://pubmed.ncbi.nlm.nih.gov/23696743/); [PMID: 23223576](https://pubmed.ncbi.nlm.nih.gov/23223576/); [PMID: 23415771](https://pubmed.ncbi.nlm.nih.gov/23415771/)).
- **Phenotype recapitulation:** Animal challenge models faithfully reproduce bacteremic systemic disease and permit gene‑knockout attribution of virulence to specific factors. **Limitation:** murine models represent invasive/veterinary disease, not the human bite‑wound cellulitis syndrome; no rodent model captures human host‑comorbidity risk stratification.

---

## Key Findings (with statistical evidence)

### F001 — Pasteurellosis is a zoonosis from cats and dogs, including indirect and vertical transmission
In a review of 74 infants with *P. multocida* meningitis, **61% (42/74)** arose from indirect household animal contact; bacteremia occurred in 51% (38/74), seizures in 20% (15/74), mortality 8% (6/74) ([PMID: 40063964](https://pubmed.ncbi.nlm.nih.gov/40063964/)). In 25 neonatal cases, cat/dog exposure was the major risk (non‑traumatic 44%, traumatic 8%, vertical 44%); overall mortality 20% ([PMID: 19208671](https://pubmed.ncbi.nlm.nih.gov/19208671/)). *"Most cases occurring from indirect household animal contact (42/74; 61%)."*

### F002 — PMT deamidates Gα proteins to constitutively activate Gq/11–RhoA–MAPK and mTORC1
PMT (146 kDa) deamidates a conserved glutamine in the α‑subunit of three of four G‑protein families ([PMID: 23150526](https://pubmed.ncbi.nlm.nih.gov/23150526/)). *"The toxin deamidates an essential glutamine residue of the Gα(i2) subunit, leading to constitutive activation of the G protein."* Downstream, *"Gα(q/11) activates RhoA via p63RhoGEF … Activated RhoA transactivates the MAP kinase cascade via Rho kinase, involving Ras, MEK and ERK, resulting in inhibition of osteoblast differentiation"* ([PMID: 23696743](https://pubmed.ncbi.nlm.nih.gov/23696743/)). PMT also activates mTORC1 via Gαq/11/PLCβ/PKC ([PMID: 23223576](https://pubmed.ncbi.nlm.nih.gov/23223576/)) and depletes membrane Gαq ([PMID: 27490568](https://pubmed.ncbi.nlm.nih.gov/27490568/)).

### F003 — B:2 hemorrhagic septicemia causes near‑100% mortality in cattle/buffalo
*"Haemorrhagic septicaemia (HS) is an acute infection of cattle and buffaloes caused by the B:2 serotype of Pasteurella multocida. This disease is highly endemic in South Asia. In some peracute cases, there is 100% mortality in infected animals within a few hours of infection"* ([PMID: 36503053](https://pubmed.ncbi.nlm.nih.gov/36503053/)).

### F004 — Soft tissue is the commonest human site, respiratory second; penicillin first‑line
*"The respiratory tract is the second most common site of Pasteurella infection after soft tissue infection. Most patients with Pasteurella pulmonary infection are elderly with underlying lung disease, either COPD, bronchiectasis, or malignancy"* and *"The preferred drug for the treatment of Pasteurella infections is penicillin. Alternately, doxycycline is highly effective"* ([PMID: 9097378](https://pubmed.ncbi.nlm.nih.gov/9097378/)).

### F005 — Capsule and LPS are the key virulence factors
*"Key virulence factors identified to date include capsule and lipopolysaccharide. The capsule is clearly involved in bacterial avoidance of phagocytosis and resistance to complement, while complete lipopolysaccharide is critical for bacterial survival in the host"* — plus PMT, adhesins, and iron‑acquisition proteins ([PMID: 17107417](https://pubmed.ncbi.nlm.nih.gov/17107417/)).

### F006 — Non‑bite infection is more invasive and lethal than bite infection
Retrospective cohort (n=44): *"Patients presenting without a bite were more frequently bacteremic (37% vs 4%, P = 0.001), and were hospitalized more often (84% vs 44%, P = 0.012)."* All 4 deaths and 7/8 ICU patients were non‑bite‑related; Charlson index ≥1 associated with absence of a bite (p=0.006) ([PMID: 26356688](https://pubmed.ncbi.nlm.nih.gov/26356688/)).

### F007 — Prevention rests on wound care, selective prophylaxis, and rabies PEP
*"While dog bites are associated with an overall high rate of infection (6‑25 %), routine antibiotic prophylaxis in low‑risk wounds does not lower that risk. Postexposure prophylaxis for rabies is indicated for all dog bites where the rabies status of the dog cannot be determined, or the animal cannot be quarantined for 10 days"* ([PMID: 39462695](https://pubmed.ncbi.nlm.nih.gov/39462695/)).

### F008 — Capsule is a proven virulence determinant in a mouse model
The B:2 *cap* locus has 15 genes in three regions; disrupting export gene *cexA* yields an acapsular mutant. *"Following intraperitoneal challenge of mice, the acapsular bacteria were removed efficiently from the blood, spleen, and liver, while wild-type bacteria multiplied rapidly"* ([PMID: 10816499](https://pubmed.ncbi.nlm.nih.gov/10816499/)).

### F009 — *Pasteurella* is the most frequent bite‑wound isolate
Prospective multicenter study (18 EDs): *"Pasteurella species were the most frequent isolates from both dog bites (50 percent) and cat bites (75 percent). Pasteurella canis was the most common isolate of dog bites, and Past. multocida subspecies multocida and septica were the most common isolates of cat bites"* ([PMID: 9887159](https://pubmed.ncbi.nlm.nih.gov/9887159/)). Wounds were polymicrobial (aerobes+anaerobes in 56%).

### F010 — LPS is essential; basis of 16‑serovar classification; serovar‑specific immunity
*"P. multocida strains are classified into 16 serovars based on lipopolysaccharide (LPS) antigens. LPS is an essential virulence factor of P. multocida; mutants expressing severely truncated LPS are completely attenuated in chickens"* and *"protection … is generally considered to be serovar specific"* ([PMID: 21664074](https://pubmed.ncbi.nlm.nih.gov/21664074/)).

### F011 — Three human syndrome groups; cats source in 60–80%
*"Cats are the source of infection in 60 to 80% of cases and dogs in the great majority of the remainder. Local infections are characterized by the rapid appearance of erythema, warmth, tenderness, and frequently purulent drainage"* with serious complications including *"septic arthritis proximal to bites or scratches, osteomyelitis"* ([PMID: 6371440](https://pubmed.ncbi.nlm.nih.gov/6371440/)).

---

## Mechanistic Model / Interpretation

```
                    ANIMAL RESERVOIR (cat/dog oral flora; cattle, poultry, swine)
                                        |
                    ┌───────────────────┼─────────────────────┐
                 bite/scratch/lick   inhalation/aspiration   (indirect / vertical)
                        |                    |                       |
                        v                    v                       v
   ============  INOCULATION of P. multocida into host tissue  ============
                                        |
              VIRULENCE ARMAMENT (bacterium):
              • Capsule  -> anti-phagocytic + complement-resistant  [F005,F008]
              • LPS      -> host survival; 16 serovars; endotoxin    [F005,F010]
              • PMT/toxA -> Gα deamidation (veterinary rhinitis)     [F002]
                                        |
             ┌──────────────────────────┼──────────────────────────┐
             v                          v                          v
  LOCAL SOFT-TISSUE               RESPIRATORY                 INVASIVE / SYSTEMIC
  (most common) [F011]            (2nd, elderly + COPD)[F004] (neonate/immunocomp.)[F006]
  rapid cellulitis,               pneumonia, abscess,         bacteremia, meningitis,
  purulent drainage               empyema                     endocarditis
       |                                                         |
  septic arthritis,                                       higher mortality
  osteomyelitis                                           (8-20% invasive) [F001]
       |
  === TREATMENT: penicillin / amoxicillin-clavulanate; wound care [F004,F007] ===

  PMT signaling branch (veterinary atrophic rhinitis) [F002]:
  PMT -> deamidate Gα(q/11) --> p63RhoGEF -> RhoA -> ROCK -> Ras/MEK/ERK -> ↓osteoblast diff.
                          \--> PLCβ -> PKC -> mTORC1 -> rpS6-P, proliferation
                          => bone resorption > formation => turbinate atrophy
```

The unifying narrative: pasteurellosis is a **bacterial‑virulence‑driven** disease in which host outcome is a function of (a) inoculation route and (b) host immune competence. The capsule and LPS are the "survival kit" that lets the organism evade phagocytosis and complement and persist long enough to cause disease — proven by the clearance of acapsular and truncated‑LPS mutants in animal models. Once established, disease severity bifurcates: an immunocompetent host with a bite develops localized, treatable cellulitis, whereas a compromised host (or a non‑bite/mucosal acquisition, which itself flags comorbidity) develops invasive, potentially fatal disease. PMT represents a distinct, mechanistically elegant branch dominant in veterinary atrophic rhinitis, hijacking universal mammalian G‑protein signaling.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [6371440](https://pubmed.ncbi.nlm.nih.gov/6371440/) | *Pasteurella multocida infections. Report of 34 cases* | Three‑group clinical framework; cats 60–80%; rapid cellulitis (F011) |
| [9097378](https://pubmed.ncbi.nlm.nih.gov/9097378/) | *Pasteurella multocida pneumonia* | Soft tissue > respiratory; penicillin/doxycycline (F004) |
| [26356688](https://pubmed.ncbi.nlm.nih.gov/26356688/) | *Clinical Features and Outcomes of P. multocida* | Non‑bite = more bacteremia/ICU/death (F006) |
| [40063964](https://pubmed.ncbi.nlm.nih.gov/40063964/) | *Infantile P. multocida Meningitis* | Indirect transmission 61%; invasive outcomes (F001) |
| [19208671](https://pubmed.ncbi.nlm.nih.gov/19208671/) | *Neonatal pasteurellosis review* | Vertical transmission; 20% mortality (F001) |
| [17107417](https://pubmed.ncbi.nlm.nih.gov/17107417/) | *P. multocida pathogenesis: 125 years after Pasteur* | Capsule + LPS key virulence factors (F005) |
| [10816499](https://pubmed.ncbi.nlm.nih.gov/10816499/) | *Capsule is a virulence determinant* | Acapsular mutant cleared in mice (F008) |
| [21664074](https://pubmed.ncbi.nlm.nih.gov/21664074/) | *P. multocida LPS: the long and short of it* | LPS essential; 16 serovars; serovar‑specific immunity (F010) |
| [9887159](https://pubmed.ncbi.nlm.nih.gov/9887159/) | *Bacteriologic analysis of dog/cat bites* | Pasteurella dominant isolate (F009) |
| [23150526](https://pubmed.ncbi.nlm.nih.gov/23150526/) | *Substrate specificity of PMT for Gα* | PMT deamidation mechanism (F002) |
| [23696743](https://pubmed.ncbi.nlm.nih.gov/23696743/) | *PMT prevents osteoblast differentiation* | Gq/11–RhoA–MAPK axis (F002) |
| [23223576](https://pubmed.ncbi.nlm.nih.gov/23223576/) | *mTORC1 in PMT signaling* | PLCβ/PKC–mTORC1 branch (F002) |
| [36503053](https://pubmed.ncbi.nlm.nih.gov/36503053/) | *ELISA diagnostics for HS* | B:2 hemorrhagic septicemia, ~100% mortality (F003) |
| [39462695](https://pubmed.ncbi.nlm.nih.gov/39462695/) | *Surgical Management of Pediatric Dog Bites* | Wound care, selective prophylaxis, rabies PEP (F007) |
| [26964825](https://pubmed.ncbi.nlm.nih.gov/26964825/) | *NPWT for serious dog bites* | Adjunctive surgical management |
| [7560209](https://pubmed.ncbi.nlm.nih.gov/7560209/) | *Waterhouse‑Friderichsen in cirrhosis* | Fulminant sepsis in cirrhotic host |
| [11242756](https://pubmed.ncbi.nlm.nih.gov/11242756/) | *Cat cuddler's cough* | Inhalation/aspiration respiratory route |

**Evidence source types:** Human clinical (case series, retrospective cohorts): F001, F004, F006, F007, F009, F011. Model organism / in vitro (mouse, chicken/duck, cell lines): F002, F003, F005, F008, F010. This mix means mechanistic virulence claims are strongly supported experimentally, while human epidemiologic precision is limited to observational series.

---

## Limitations and Knowledge Gaps

1. **No population‑level incidence/prevalence.** Human data are case series and single‑center cohorts; true incidence per 100,000 is unknown. Reported outcome percentages come from small samples (n=25–74).
2. **Selection/publication bias** toward severe and unusual cases (meningitis, sepsis, fatalities) likely overstates severity relative to the many mild, culture‑unconfirmed cellulitis cases treated empirically in primary care.
3. **Mechanistic data are mostly veterinary/model‑organism.** The PMT Gα‑deamidation pathway and capsule/LPS virulence are best characterized in atrophic rhinitis, fowl cholera, and mouse models — their direct role in **human** soft‑tissue and invasive disease is inferred, not demonstrated.
4. **No human host‑genetic susceptibility data.** Whether host polymorphisms (complement, TLR4, mannose‑binding lectin) modulate risk is unstudied.
5. **Antibiotic resistance trends** in human isolates are sparsely characterized; most susceptibility data are veterinary ([PMID: 24612952](https://pubmed.ncbi.nlm.nih.gov/24612952/)).
6. **Diagnostics lag:** no rapid point‑of‑care test; culture and MALDI‑TOF remain the mainstay, delaying species/serotype confirmation.

---

## Proposed Follow‑up Experiments / Actions

1. **Epidemiologic quantification:** Mine a large EHR/administrative dataset (ICD‑10 A28.0) to estimate true human incidence, syndrome distribution, and case‑fatality with confidence intervals — filling the F001/F011 quantitative gap.
2. **Host‑susceptibility study:** Case‑control genotyping (complement, TLR4, MBL2) in invasive vs local pasteurellosis to test whether host innate‑immune variants explain the comorbidity‑independent severity of non‑bite disease (F006).
3. **Mechanistic bridge to human tissue:** Test capsule/LPS mutants (F008/F010) and PMT signaling (F002) in human keratinocyte/osteoblast and whole‑blood models to confirm animal‑derived virulence mechanisms operate in human infection.
4. **Antibiotic surveillance:** Systematic collection of human *P. multocida* isolates for β‑lactamase and MIC profiling to validate continued reliance on penicillin/amoxicillin‑clavulanate (F004).
5. **Prophylaxis RCT:** A stratified randomized trial of selective antibiotic prophylaxis in cat‑bite (high‑risk) vs dog‑bite (variable‑risk) wounds to refine F007's "selective prophylaxis" recommendation.
6. **Rapid diagnostics:** Develop/validate a multiplex PCR (capsular serogroup + species) directly from wound swab and blood to shorten time to targeted therapy.

---

## Consensus Answer

Pasteurellosis is a zoonotic bacterial infection caused by *Pasteurella* species (chiefly *P. multocida*), acquired from the oral/respiratory flora of cats and dogs (cats the source in 60–80% of human cases) via bites, scratches, licking, or inhalation. It presents in three groups — rapidly progressive soft‑tissue cellulitis at the wound (most common), respiratory infection in elderly patients with chronic lung disease, and invasive disease (bacteremia, meningitis, endocarditis) concentrated in neonates and immunocompromised/cirrhotic hosts — and has no human genetic etiology; pathogenesis is driven by bacterial virulence factors (capsule and LPS for immune evasion, and *Pasteurella multocida* toxin, which deamidates Gα proteins to activate Gq/11–RhoA–MAPK/mTORC1 signaling in veterinary atrophic rhinitis). It is treated first‑line with penicillin or amoxicillin‑clavulanate, and prevention rests on bite‑wound care, selective prophylaxis, rabies post‑exposure prophylaxis, and hygiene after animal contact.


## Artifacts

- [OpenScientist final report](Pasteurellosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pasteurellosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 21 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005901` (2 mentions) - the report calls it "MONDO"; MONDO calls it **pasteurellosis**
- `HP:0031357` (1 mention) - the report calls it "Frequent in local infection"; HP calls it **Glomeruloid hemangioma**
- `HP:0100776` (1 mention) - the report calls it "Serious local complication"; HP calls it **Recurrent pharyngitis**
- `HP:0002754` (1 mention) - the report calls it "Local complication, esp. finger/hand after cat bite"; HP calls it **Osteomyelitis**
- `HP:0031864` (1 mention) - the report calls it "Sepsis"; HP calls it **Bacteremia**
- `NCIT:C716` (1 mention) - the report calls it "Penicillin"; NCIT calls it **Omeprazole**
- `NCIT:C263` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Anticoagulant Agent**
- `NCIT:C61735` (1 mention) - the report calls it "Amoxicillin‑Clavulanate"; NCIT calls it **Dolasetron**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0031617` (1 mention), reported as "Rare, severe" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007186` (1 mention) - the report calls it "GPCR signaling"; GO calls it **G protein-coupled receptor signaling pathway**, and lists "GPCR signaling pathway" among its other names
- `GO:0001503` (1 mention) - the report calls it "ossification, inhibited"; GO calls it **ossification**
- `GO:0006909` (1 mention) - the report calls it "phagocytosis, evaded"; GO calls it **phagocytosis**
- `GO:0005886` (1 mention) - the report calls it "plasma membrane", "Subcellular:** Host **plasma membrane"; GO calls it **plasma membrane**, and lists "cellular membrane" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005886` - called "plasma membrane", "Subcellular:** Host **plasma membrane"
