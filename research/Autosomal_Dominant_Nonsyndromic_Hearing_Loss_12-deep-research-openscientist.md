---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:46:02.288691'
end_time: '2026-08-31T17:16:08.382085'
duration_seconds: 1806.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 12
  mondo_id: ''
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
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 23
  on_topic: 16
  validator_version: 0.2.1
term_validation:
  total_terms: 20
  verified: 17
  not_found: 1
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.053
  labels_checked: 6
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000407
    reported_labels:
    - clinical sign
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0008619
    reported_labels:
    - clinical sign
    - Localization / lateralization:** **bilateral**, usually symmetric
    ontology_label: Bilateral sensorineural hearing impairment
  - term_id: HP:0008527
    reported_labels:
    - clinical sign
    ontology_label: Congenital sensorineural hearing impairment
  - term_id: HP:0000408
    reported_labels:
    - clinical sign
    ontology_label: Progressive sensorineural hearing impairment
  labels_variant: 2
  unresolved_terms:
  - HP:0008565
  obsolete_terms:
  - term_id: HP:0410007
    ontology_label: obsolete Abnormality of cartilage morphology
    replaced_by: HP:0002763
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Autosomal_Dominant_Nonsyndromic_Hearing_Loss_12-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Dominant_Nonsyndromic_Hearing_Loss_12-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 12
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 12** covering all of the
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

# Autosomal Dominant Nonsyndromic Hearing Loss 12 (DFNA12 / DFNA8/12) — Comprehensive Disease Report

**Evidence base:** synthesized from primary literature (human clinical, mouse model, in vitro, and computational studies). Evidence source type is annotated per claim. PMIDs are given for all key statements.

---

## Summary (Answer to the Research Question)

Autosomal Dominant Nonsyndromic Hearing Loss 12 (DFNA12), now unified with DFNA8 as **DFNA8/12**, is a Mendelian, autosomal-dominant, nonsyndromic sensorineural hearing loss caused by heterozygous, predominantly **missense** mutations in **TECTA** (gene for **α‑tectorin**, a major non‑collagenous glycoprotein of the cochlear **tectorial membrane**). Mutant α‑tectorin is incorporated into and structurally poisons the tectorial membrane (a **dominant‑negative** mechanism), degrading the mechanical coupling between the tectorial membrane and the outer‑hair‑cell stereocilia that drives cochlear amplification and frequency tuning, producing bilateral, usually mid‑ or high‑frequency, prelingual‑to‑childhood‑onset sensorineural hearing loss. The affected α‑tectorin **protein domain predicts the phenotype** (ZP domain → mid‑frequency, often stable; zonadhesin/ZA domain and cysteine‑substituting variants → high‑frequency, progressive). DFNA8/12 is one of the most commonly identified single‑gene causes of autosomal dominant nonsyndromic hearing loss; management is auditory rehabilitation (hearing aids, and cochlear implantation/electric‑acoustic stimulation with favorable outcomes), with no disease‑modifying drug.

---

## 1. Disease Information

**Overview.** DFNA12 is a hereditary, nonsyndromic (isolated) sensorineural hearing impairment inherited in an autosomal dominant pattern. The DFNA8 and DFNA12 loci were both mapped to chromosome **11q** and shown to result from mutations in the same gene, **TECTA**; the entity is therefore designated **DFNA8/12** (human clinical/linkage: PMID 9763681, 9503015, 9590290). α‑Tectorin is "one of the major non-collagenous components of the tectorial membrane" of the inner ear (PMID 9590290).

**Key identifiers.**
- **OMIM (phenotype):** 601543 (Deafness, autosomal dominant 12; encompassing DFNA8/12)
- **OMIM (gene TECTA):** 602574
- **Gene:** TECTA — HGNC:11720; NCBI Gene 7007; Ensembl ENSG00000109927; UniProt **O75443** (α‑tectorin, 2155 aa)
- **MONDO:** DFNA12 corresponds to MONDO "autosomal dominant nonsyndromic hearing loss 12" (also captured under the DFNA8/12 concept); TECTA‑related dominant deafness
- **Orphanet:** included within "Rare genetic deafness"/autosomal dominant nonsyndromic sensorineural deafness type DFNA
- **ICD‑10:** H90.5 (sensorineural hearing loss, unspecified) / H90.3 (bilateral). **ICD‑11:** AB52 (sensorineural hearing loss)
- **MeSH:** related terms "Hearing Loss, Sensorineural"; "Deafness"; gene "TECTA / tectorin alpha"

**Synonyms / alternative names:** DFNA8; DFNA12; DFNA8/12; TECTA‑related autosomal dominant nonsyndromic hearing loss; deafness, autosomal dominant 8/12; α‑tectorin–related dominant deafness.

**Information source:** aggregated disease-level resources (OMIM, published pedigrees/cohorts) and individual multigenerational family studies; not derived from population EHR.

---

## 2. Etiology

**Causal factors — genetic.** DFNA12 is a **monogenic** disorder. The sole established cause is a heterozygous pathogenic variant in **TECTA**. The initiating lesion is almost always a **missense** substitution (occasionally an in‑frame splice variant) affecting conserved residues of α‑tectorin (PMID 9590290, 40583560). "In both families, mutation analysis revealed missense mutations which replace conserved amino-acid residues within the zona pellucida domain of TECTA" (PMID 9590290).

**Genetic risk factors.** The causal variant itself is the risk factor; there are no separate susceptibility loci for the Mendelian form. The specific **domain** affected is the principal modifier of expression (see §4). No environmental modifiers are established.

**Environmental risk factors.** None established as causing DFNA12. As with any sensorineural hearing loss, generic aggravators (noise exposure, ototoxic drugs, aging) could additively worsen hearing; notably, in the Tecta^C1509G/+ mouse, noise exposure caused incomplete recovery and increased outer‑hair‑cell loss versus wild type (model organism: PMID 21567249), suggesting **gene–environment interaction** whereby a defective tectorial membrane increases vulnerability to noise. TECTA is also among genes implicated in age‑related (multifactorial) hearing loss (PMID 42379497).

**Protective factors.** None specifically identified. A single functional TECTA allele is sufficient for near‑normal hearing (DFNB21 heterozygous carriers are unaffected), which is why complete loss‑of‑function is only pathogenic when biallelic (PMID 9949200).

**Gene–environment interaction.** Inferred increased susceptibility to noise‑induced damage on a mutant‑TECTA background (model organism evidence: PMID 21567249); direct human data limited.

**Infectious agents:** not applicable.

---

## 3. Phenotypes

**Core phenotype:** bilateral, symmetric, nonsyndromic **sensorineural hearing loss** with no vestibular, visual, renal, or other systemic involvement.

| Phenotype | Type | HPO term | Characteristics / frequency |
|---|---|---|---|
| Sensorineural hearing impairment | clinical sign | **HP:0000407** | Defining feature, ~100% of affected |
| Bilateral sensorineural hearing impairment | clinical sign | **HP:0008619** | Bilateral, usually symmetric |
| Mid-frequency sensorineural hearing impairment ("cookie-bite"/U‑shaped audiogram) | clinical sign | **HP:0410007 / HP:0008542** | Typical of ZP‑domain variants (PMID 21520338, 37927186, 9763681) |
| High-frequency hearing impairment | clinical sign | **HP:0000399 / HP:0008565** | Typical of ZA‑domain variants (PMID 21520338, 24363064) |
| Congenital / prelingual sensorineural hearing impairment | clinical sign | **HP:0008527** | Many families prelingual/congenital (PMID 9763681) |
| Progressive sensorineural hearing impairment | clinical sign | **HP:0000408** | With cysteine‑substituting / ZA variants (PMID 21520338, 24363064) |

**Age of onset:** congenital/prelingual to childhood; some late‑onset/progressive forms present in adulthood (PMID 9763681, 42379497).
**Severity:** mild to severe (moderate‑to‑severe common); "moderate to severe... U-shaped form with maximum loss at 2,000 Hz" in the original DFNA8 family (PMID 9763681).
**Progression:** frequently **stable/nonprogressive** for ZP non‑cysteine variants; **progressive** for cysteine‑substituting and ZA‑domain variants (PMID 21520338, 24363064).
**Frequency among affected:** hearing loss is fully penetrant in most reported families; configuration/severity vary by genotype.

**Quality-of-life impact:** hearing loss impairs speech perception, communication, and (for prelingual cases) spoken‑language acquisition and education; early amplification mitigates these effects. No disease‑specific QoL instrument data (EQ‑5D/SF‑36) are available specifically for DFNA12; general SNHL QoL literature applies.

---

## 4. Genetic / Molecular Information

**Causal gene:** **TECTA** (α‑tectorin), 11q23.3; OMIM 602574; HGNC:11720; NCBI Gene 7007; UniProt O75443. Encodes a large secreted, GPI‑anchored (during trafficking) modular glycoprotein of 2155 aa with an **entactin/nidogen‑G1‑like (NIDO) domain**, three **von Willebrand factor type D (vWFD1–3)** repeats within a **zonadhesin‑like (ZA)** region, and a C‑terminal **zona pellucida (ZP)** domain (PMID 9590290, 21520338).

**Pathogenic variants.**
- **Variant type/class:** predominantly **missense** in DFNA8/12; occasionally in‑frame/aberrant **splice** variants (e.g., c.5999G>A p.Gly2000Glu causing exon‑20 mis‑splicing; c.5383+6T>A causing exon‑16 skipping) (PMID 40583560). Truncating variants (nonsense/frameshift/splice/large deletions) instead cause **recessive DFNB21** (PMID 17431902, 18022253, 9949200).
- **Distribution across domains:** mutations occur in **all domains** — entactin/NIDO, vWFD1–3, D1–D2 and TIL2 connectors, and ZP (PMID 21520338).
- **Representative variants:** p.Cys1509Gly (C1509G), p.Cys1619Ser (ZA), p.Leu1820Phe+Gly1824Asp and p.Cys1837Gly (ZP), p.Thr1866Met, p.Arg1890Cys, p.Cys1036Tyr, p.Val317Glu, near‑ZP c.6183G>T (PMID 20947814, 21520338, 24363064, 37927186).
- **Classification (ACMG/AMP):** pathogenic/likely pathogenic when segregating and absent from controls; segregation analysis is often decisive for reclassifying VUS (e.g., c.6183G>T upgraded to likely pathogenic; PMID 37927186).
- **Allele frequency:** pathogenic DFNA8/12 missense alleles are rare/absent in gnomAD and matched controls (PMID 20947814, 21520338).
- **Origin:** **germline**; de novo cases possible but most are familial. Not somatic.
- **Functional consequence:** **dominant‑negative** for DFNA8/12 missense alleles (mutant α‑tectorin incorporated into TM disrupts its assembly); **loss‑of‑function** for recessive DFNB21 alleles (PMID 9949200).

**Modifier genes:** the affected α‑tectorin domain is the dominant determinant of expressivity (PMID 21520338). Interacting TM proteins (β‑tectorin/**TECTB**, **CEACAM16**, **OTOG/OTOGL**, collagen II) could theoretically modify phenotype; **CEACAM16** co‑immunoprecipitates with α‑tectorin and its mutation causes DFNA4 (PMID 21368133). No formal human modifier‑gene study for DFNA12.

**Epigenetic information:** none established for DFNA12.

**Chromosomal abnormalities:** point mutations, not aneuploidy/translocations. Large intragenic deletions (e.g., exon‑10 deletion) occur in the recessive form and require CNV‑aware analysis (PMID 17431902). Historically, TECTA haploinsufficiency was proposed to contribute to hearing loss in some Jacobsen‑syndrome (11q deletion) cases (PMID 9503015).

---

## 5. Environmental Information

DFNA12 is a purely genetic disorder; no environmental, lifestyle, or infectious agent causes it. Generic exacerbating exposures (loud noise, ototoxic aminoglycosides/cisplatin, aging) may additively worsen hearing, and mouse data indicate a defective tectorial membrane increases susceptibility to noise‑induced outer‑hair‑cell loss (model organism: PMID 21567249). No dietary/occupational protective or causal factors are established.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A heterozygous **TECTA missense (or in‑frame splice) mutation** alters a conserved residue in a specific α‑tectorin domain (entactin/NIDO, vWFD/ZA, or ZP) — **results in** a structurally abnormal α‑tectorin monomer (human genetics: PMID 9590290; splicing: PMID 40583560).
2. The mutant α‑tectorin is secreted by cochlear supporting/interdental cells and **incorporated into the assembling tectorial membrane**, where it **acts dominant‑negatively** on α‑tectorin self‑assembly and its interactions with β‑tectorin and type II collagen (inferred from unaffected DFNB21 heterozygotes vs affected DFNA8/12 heterozygotes: PMID 9949200; TM assembly: PMID 26806019).
3. This **leads to** a **domain‑specific structural defect** of the tectorial membrane — e.g., ZP‑domain mutations vs ZA‑domain mutations "generate distinctly different changes in the structure of the TM" (loss/disorganization of the striated‑sheet matrix, altered collagen crosslinking, shortening, or detachment) (model organism: PMID 24363064; PMID 25564867; PMID 26806019).
   - **Branch A (ZP domain):** predominantly disrupts the mid/apical TM → **mid‑frequency** loss, often **stable** (PMID 21520338, 24363064).
   - **Branch B (ZA/zonadhesin domain or cysteine substitution):** disrupts basal TM/covalent crosslinking → **high‑frequency** and/or **progressive** loss (PMID 21520338, 24363064).
4. The abnormal TM **results in** defective mechanical coupling to the **outer‑hair‑cell (OHC) stereocilia** — e.g., a shortened TM contacts only the first OHC row and **increases shear force on those stereocilia by ~50%** (computational + model organism: PMID 21567249).
5. This **impairs the cochlear amplifier**: the TM normally "ensures that outer hair cells can effectively respond to basilar membrane motion and that feedback is delivered with the appropriate gain and timing required for amplification"; when α‑tectorin is defective the cochlea is **~35 dB less sensitive** (model organism: PMID 11087000).
6. Loss of active amplification and frequency selectivity **results in elevated auditory thresholds** in the affected frequency band — clinically, **bilateral sensorineural hearing loss** (human: PMID 9763681, 37927186).
7. **Downstream/secondary (inferred):** increased OHC vulnerability to noise and altered prestin expression may add a slowly progressive component in some genotypes (model organism: PMID 21567249).

**Upstream vs downstream:** upstream = mutant protein + TM matrix defect (primary lesion in an acellular extracellular matrix); downstream = OHC mechanotransduction/amplification failure and threshold elevation. The **spiral ganglion/auditory nerve and hair‑cell bodies are largely preserved**, which is therapeutically important (basis for good cochlear‑implant outcomes).

**Molecular pathways / processes.** This is primarily an **extracellular‑matrix (ECM) assembly** disorder rather than a classical signaling‑cascade disease. Relevant GO biological processes: **sensory perception of sound (GO:0007605)**, **detection of mechanical stimulus involved in sensory perception of sound (GO:0050910)**, **inner ear morphogenesis (GO:0042472)**, **extracellular matrix organization (GO:0030198)**, **tectorial membrane development**. Cellular component: **extracellular matrix (GO:0031012)** / tectorial membrane. No apoptosis/inflammation/immune or metabolic pathway is centrally implicated; late OHC loss (model) would proceed via mechanical stress rather than a defined death pathway.

**Protein dysfunction.** Structural (dominant‑negative) rather than enzymatic; α‑tectorin has no catalytic activity — it is a structural ECM glycoprotein. Cysteine substitutions disrupt disulfide‑mediated crosslinking, correlating with progressive phenotypes (PMID 21520338).

**Immune involvement / metabolic / epigenetic:** not implicated.

**Cell types (CL):** outer hair cell (**CL:0000601**), inner hair cell (**CL:0000589**), cochlear supporting/interdental cells (tectorin‑secreting).

**Molecular profiling:** no human transcriptomic/proteomic/metabolomic disease signatures reported; mechanistic data derive from mouse cochlear physiology, immunogold/freeze‑etch ultrastructure (PMID 26806019), and atomic‑force microscopy of TM mechanics (PMID 25564867).

---

## 7. Anatomical Structures Affected

- **Organ level:** the **inner ear (UBERON:0001846)**, specifically the **cochlea (UBERON:0001844)** — the auditory (nervous/special‑sense) system. No secondary organ involvement; **vestibular function is spared** (nonsyndromic).
- **Primary structure:** the **tectorial membrane (UBERON:0002233)**, an acellular ECM within the **organ of Corti (UBERON:0002227)**, and its attachment to the **spiral limbus** (PMID 26806019).
- **Tissue/cell level:** sensory epithelium of the organ of Corti; **outer hair cells (CL:0000601)** and **inner hair cells (CL:0000589)** are functionally affected via the abnormal overlying TM; tectorin‑secreting **supporting/interdental cells** produce the defective matrix.
- **Subcellular (GO‑CC):** **extracellular matrix (GO:0031012)** / tectorial membrane; α‑tectorin is a secreted glycoprotein.
- **Localization / lateralization:** **bilateral**, usually symmetric (HP:0008619).

---

## 8. Temporal Development

- **Onset:** typically **congenital/prelingual to early childhood**; described as "congenital, nonprogressive" in the founder DFNA8 family (PMID 9763681). Some genotypes present later (adult/late‑onset), overlapping age‑related hearing loss (PMID 42379497).
- **Onset pattern:** insidious/chronic (not acute).
- **Progression:** **stable/nonprogressive** for many ZP non‑cysteine variants; **slowly progressive** for cysteine‑substituting and ZA‑domain variants (PMID 21520338, 24363064). Progression rate is slow when present.
- **Disease course:** chronic, lifelong; not episodic/relapsing.
- **Remission:** none spontaneously; only functional improvement with amplification/implantation.
- **Critical period:** the window for spoken‑language acquisition in prelingual cases makes **early identification (newborn screening) and early amplification** essential.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal dominant** (MONDO/OMIM 601543); recessive **DFNB21** (OMIM 603629) at the same locus from biallelic LOF alleles (PMID 9949200).
- **Penetrance:** generally **high/complete** in reported families (clear multigenerational segregation; e.g., 5‑generation pedigree, PMID 40583560).
- **Expressivity:** **variable and domain‑dependent** (frequency band, severity, progression) (PMID 21520338, 24363064).
- **Genetic anticipation:** none (not a repeat‑expansion disorder).
- **Germline mosaicism:** not specifically documented; de novo variants possible.
- **Founder effects:** confirmed for recurrent alleles — "four of them—p.Cys1036Tyr, p.Cys1837Gly, p.Thr1866Met, and p.Arg1890Cys—were observed in more than one unrelated family. For two of these mutations founder effects were also confirmed" (PMID 21520338).
- **Consanguinity:** relevant to recessive DFNB21, not to dominant DFNA12.
- **Carrier frequency:** pathogenic dominant alleles are rare; not a routine carrier‑screening target.
- **Epidemiology:** no precise prevalence figure exists for DFNA12 specifically. Background: hearing impairment affects **~1 in 500 newborns**, and ~80% of genetic hearing loss is nonsyndromic (PMID 25281338). DFNA8/12 is **"the most identified subtype of nonsyndromic autosomal dominant hearing loss"** (PMID 21520338) and a leading cause among molecularly solved **adult‑onset** dominant SNHL (top gene, 4/15 solved cases, PMID 36190904).
- **Population/geography:** reported worldwide (Spanish, Belgian, English, Austrian, French, Korean, Chinese, Iranian, Croatian, etc.); **no strong ethnic predilection**; specific founder alleles are population‑enriched.
- **Sex ratio:** ~1:1 (autosomal). **Age distribution:** all ages (onset childhood; diagnosis across the lifespan).

---

## 10. Diagnostics

- **Audiologic testing (clinical signs):** pure‑tone audiometry (mid‑frequency "cookie‑bite"/U‑shaped or high‑frequency SNHL), tympanometry (normal middle ear), otoacoustic emissions and auditory brainstem response (ABR) — abnormal, consistent with cochlear/OHC dysfunction; newborn OAE/ABR screening detects congenital cases.
- **Laboratory/biomarkers:** **none**; no blood/urine biomarker. Diagnosis is audiologic + genetic.
- **Imaging:** temporal‑bone CT/MRI is typically **normal** (no malformation) — used to exclude structural/other causes.
- **Genetic testing (definitive):** recommended approach is **NGS**. Comprehensive **hearing‑loss gene panels** or **whole‑exome/whole‑genome sequencing** including TECTA; single‑gene TECTA testing when the audiogram (mid‑frequency, dominant family history) is suggestive. **CNV/deletion analysis** needed to detect large intragenic deletions. Diagnostic yield of NGS panels/WES in bilateral SNHL is **~20–48%** (PMID 38224868: "48% (50/105) of patients were genetically diagnosed"; PMID 36804529: 39.5%; adult SNHL 23% with TECTA the top gene, PMID 36190904). Karyotype/CMA/FISH/mtDNA/repeat‑expansion testing are **not** indicated for isolated DFNA12.
- **Clinical criteria:** diagnosis = bilateral nonsyndromic SNHL + AD family history + a pathogenic/likely‑pathogenic heterozygous TECTA variant with segregation (ACMG/AMP).
- **Differential diagnosis:** other mid‑frequency dominant SNHL genes (**EYA4/DFNA10, COL11A2/DFNA13, CEACAM16/DFNA4, WFS1/DFNA6/14/38 [low‑frequency], DIAPH1, P2RX2/DFNA41, KCNQ4/DFNA2**) (PMID 25809937, 36190904, 37041640); exclude GJB2/GJB6, syndromic causes, noise/ototoxic/age‑related loss.
- **Screening/cascade:** newborn hearing screening; **cascade genetic testing** of at‑risk relatives once the familial variant is known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** DFNA12 is **not life‑limiting**; normal life expectancy; no disease‑specific mortality.
- **Morbidity/disability:** the burden is **communication disability** from bilateral SNHL; magnitude depends on severity/onset. For prelingual cases, untreated loss impairs language and educational attainment; early intervention markedly improves outcomes.
- **Disease course:** chronic and lifelong; often stable (ZP) or slowly progressive (ZA/cysteine variants).
- **Recovery:** no spontaneous recovery of hearing; functional recovery is achievable with hearing aids or cochlear implantation/EAS.
- **Prognostic factors:** the **affected α‑tectorin domain / variant type** is the key prognostic marker for audiometric configuration and progression (PMID 21520338, 24363064); preserved neural elements predict good CI outcomes (PMID 24130743). Quality‑of‑life outcomes track with device benefit; no molecular prognostic biomarker beyond genotype.

---

## 12. Treatment

**No pharmacological, gene, cell, RNA, or curative therapy exists for DFNA8/12.** Management is **auditory (re)habilitation**, genotype‑informed.

- **Amplification (first‑line, mild–severe):** **hearing aids** (NCIT: Hearing Aid) and assistive listening devices.
- **Cochlear implantation (severe–profound):** effective; because the primary lesion is in the acellular TM with **preserved spiral ganglion/auditory nerve**, implantation restores useful hearing. TECTA patients "showed relatively good auditory performance with CI including EAS" (PMID 24130743). **NCIT: Cochlear Implant (C50143).**
- **Electric‑acoustic stimulation (EAS):** appropriate where useful **residual low‑frequency hearing** remains (common with mid/high‑frequency‑predominant TECTA loss) (PMID 24130743).
- **Rehabilitation/supportive:** **speech‑language therapy**, auditory training, educational support, sign‑language/communication options as chosen (NCIT: Speech Therapy; Auditory Rehabilitation).
- **Pharmacogenomics:** not applicable.
- **Experimental/future:** no DFNA12‑specific trials; general inner‑ear **gene therapy / antisense (allele‑specific knockdown of a dominant‑negative allele)** are conceptual future directions but **not yet clinical** for TECTA.
- **Treatment strategy:** severity‑ and genotype‑guided algorithm — early amplification → CI/EAS if amplification insufficient → lifelong audiologic follow‑up. **CHEBI drug entities: none applicable.**

---

## 13. Prevention

- **Primary prevention:** the disorder cannot be prevented in mutation carriers; **genetic counseling** (50% offspring risk per affected heterozygote) and reproductive options—**preimplantation genetic testing (PGT‑M)** or **prenatal diagnosis** when the familial variant is known—can prevent transmission.
- **Secondary prevention:** **universal newborn hearing screening** (OAE/ABR) plus **cascade genetic testing** enables early diagnosis and early amplification during the critical language‑acquisition window.
- **Tertiary prevention:** early/optimal amplification or implantation to prevent secondary language, educational, and psychosocial complications; **avoid additive insults** (noise protection, avoid ototoxic drugs), supported by mouse evidence of heightened noise vulnerability (PMID 21567249).
- **Counseling:** genetic counseling per NSGC/ACMG; **immunization/public‑health/environmental** measures are not applicable to this genetic condition.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** **Mouse** *Mus musculus* (**NCBI Taxon 10090**), gene **Tecta** (NCBI Gene 21683), on chromosome 9 (syntenic to human 11q; PMID 9503015). Orthologs exist in rat, zebrafish, and other vertebrates; α‑tectorin and the tectorial membrane are evolutionarily conserved across mammals.
- **Natural disease:** no well‑characterized spontaneous companion‑animal or wildlife TECTA deafness is prominently reported in OMIA for DFNA12; the disease is studied via engineered mouse models rather than natural animal disease.
- **Comparative biology:** the mouse faithfully models human TM biology; the **genotype–phenotype correlation is conserved** (ZP vs ZA domain → distinct TM defects and audiometric configurations; PMID 24363064). A species‑specific incidental finding is **audiogenic seizure susceptibility** in Tecta knock‑in mice, not seen in humans (PMID 24363064).
- **Transmission:** not applicable (non‑infectious, non‑zoonotic).

---

## 15. Model Organisms

**Primary model: mouse (mammalian).** Faithful recapitulation of human DFNA8/12 mechanism and genotype–phenotype correlation.

- **Tecta knockout (targeted deletion):** TMs **detached** from the cochlear epithelium, lacking all non‑collagenous matrix; basilar membrane still tuned but **35 dB less sensitive**; abnormal cochlear microphonic phase/symmetry — established the TM's role in cochlear‑amplifier gain/timing (PMID 11087000). Models the recessive/LOF (DFNB21) situation and TM function.
- **Knock‑in point‑mutation lines (model dominant DFNA8/12):** **Tecta^L1820F,G1824D/+** and **Tecta^C1837G/+** (ZP‑domain; stable and progressive mid‑frequency loss, respectively) and **Tecta^C1619S/+** (ZA‑domain; progressive high‑frequency loss). "Mutations in the ZP and ZA domains generate distinctly different changes in the structure of the TM"; ABR thresholds elevated 30–40 dB (ZP) and 20–30 dB (ZA) over 8–40 kHz (PMID 24363064).
- **Tecta^C1509G/+:** shortened TM contacting only the first OHC row, ~50% increased stereocilia shear force, increased noise vulnerability/OHC loss (PMID 21567249).
- **Tecta/Tectb double mutant:** fully **detached** TM; used to show ECM regulation of OHC Ca²⁺, MET currents, and otoacoustic emissions (PMID 33559882).

**Model characteristics.** Strengths: reproduce domain‑specific TM ultrastructural defects, threshold elevations, and stability/progression matching human genotypes; enable cochlear micromechanics, OAE/ABR, and AFM studies. **Limitations:** murine hearing frequency range differs from human; incidental audiogenic seizures; long‑term human progression not fully captured. **Resources:** MGI (Tecta), IMPC/IMSR for strain availability.

---

## Supported and Refuted Hypotheses

**Supported:**
- H1: DFNA12 is caused by heterozygous (mostly missense) TECTA mutations — **supported** (PMID 9590290, 21520338).
- H2: The affected α‑tectorin domain predicts audiometric phenotype/progression — **supported** in humans and mice (PMID 21520338, 24363064).
- H3: DFNA8/12 missense alleles act by a dominant‑negative mechanism (vs LOF recessive DFNB21) — **supported** (PMID 9949200).
- H4: The tectorial‑membrane defect impairs cochlear amplification, elevating thresholds — **supported** (PMID 11087000, 21567249).
- H5: Neural elements are preserved, enabling good CI/EAS outcomes — **supported** (PMID 24130743).

**Refuted / not supported:**
- That TECTA haploinsufficiency alone causes dominant deafness — **refuted** for the classic form (heterozygous LOF carriers are unaffected; dominance requires a dominant‑negative missense allele) (PMID 9949200).
- That DFNA12 involves vestibular, systemic, immune, or metabolic dysfunction — **not supported** (strictly nonsyndromic/cochlear).

---

## Limitations and Future Directions

- **Epidemiology:** no precise prevalence/incidence for DFNA12 specifically; figures are inferred from ADNSHL cohorts.
- **Omics:** no human transcriptomic/proteomic/metabolomic disease signatures; mechanism rests on mouse physiology and ultrastructure.
- **Penetrance/modifiers:** quantitative penetrance and formal modifier‑gene studies are lacking.
- **Therapeutics:** no molecular therapy; **allele‑specific silencing or gene‑editing of dominant‑negative alleles** and inner‑ear gene therapy are logical but unproven future directions.
- **Human structural biology:** no experimental α‑tectorin structure; AlphaFold models (UniProt O75443) could refine variant‑effect prediction.

---

### Key References (PMID)
9590290 (gene discovery); 9763681, 9503015 (locus mapping); 21520338 (mutation spectrum & genotype–phenotype/founder effects); 24363064 (three knock‑in mouse models); 11087000 (Tecta KO – cochlear amplification); 21567249 (C1509G shortened TM mechanics); 26806019 (TM assembly/crosslinking); 33559882 (Tecta/Tectb detached TM); 25564867 (TM striated‑sheet mechanics); 9949200 (dominant‑negative vs DFNB21 LOF); 17431902, 18022253, 27368438, 28012541 (DFNB21 LOF alleles); 20947814, 37927186, 40583560 (human variants/segregation/splicing); 21368133 (CEACAM16–α‑tectorin/DFNA4); 36190904, 38224868, 36804529, 24130743 (diagnostics & CI/EAS); 25281338, 42379497 (epidemiology/ARHL context); 25809937 (mid‑frequency SNHL differential).


## Artifacts

- [OpenScientist final report](Autosomal_Dominant_Nonsyndromic_Hearing_Loss_12-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Dominant_Nonsyndromic_Hearing_Loss_12-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 23 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000407` (1 mention) - the report calls it "clinical sign"; HP calls it **Sensorineural hearing impairment**
- `HP:0008619` (2 mentions) - the report calls it "clinical sign", "Localization / lateralization:** **bilateral**, usually symmetric"; HP calls it **Bilateral sensorineural hearing impairment**
- `HP:0008527` (1 mention) - the report calls it "clinical sign"; HP calls it **Congenital sensorineural hearing impairment**
- `HP:0000408` (1 mention) - the report calls it "clinical sign"; HP calls it **Progressive sensorineural hearing impairment**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0008565` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0410007` (obsolete Abnormality of cartilage morphology) (1 mention) - replaced by `HP:0002763`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001846` (1 mention) - the report calls it "Organ level:** the **inner ear"; UBERON calls it **internal ear**, and lists "inner ear" among its other names
- `UBERON:0002233` (1 mention) - the report calls it "Primary structure:** the **tectorial membrane"; UBERON calls it **tectorial membrane of cochlea**, and lists "tectorial membrane" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0008619` - called "clinical sign", "Localization / lateralization:** **bilateral**, usually symmetric"