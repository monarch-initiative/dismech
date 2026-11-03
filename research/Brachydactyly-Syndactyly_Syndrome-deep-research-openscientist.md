---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T23:25:25.411259'
end_time: '2026-10-15T23:34:12.497057'
duration_seconds: 527.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Brachydactyly-Syndactyly Syndrome
  mondo_id: MONDO:0012544
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
citation_count: 34
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 35
  on_topic: 27
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 31
  labels_matching: 17
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0012544
    reported_labels:
    - MONDO
    ontology_label: brachydactyly-syndactyly syndrome
  - term_id: HP:0009855
    reported_labels:
    - related
    ontology_label: Osteolytic defects of the proximal phalanges of the hand
  - term_id: CL:0000057
    reported_labels:
    - fibroblast / limb mesenchymal cell
    ontology_label: fibroblast
  - term_id: UBERON:0001436
    reported_labels:
    - metacarpal bone
    ontology_label: phalanx of manus
  - term_id: NCIT:C15277
    reported_labels:
    - physical therapy
    ontology_label: Mastectomy
  - term_id: NCIT:C15431
    reported_labels:
    - occupational therapy
    ontology_label: Hematopoietic Cell Transplantation
  - term_id: NCIT:C15215
    reported_labels:
    - skin graft
    ontology_label: Cryosurgery
  labels_variant: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Brachydactyly-Syndactyly_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Brachydactyly-Syndactyly_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brachydactyly-Syndactyly Syndrome
- **MONDO ID:** MONDO:0012544 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Brachydactyly-Syndactyly Syndrome** covering all of the
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

# Brachydactyly-Syndactyly Syndrome (MONDO:0012544): Comprehensive Disease Characteristics Report

## Summary

**Brachydactyly-syndactyly syndrome** (OMIM 610713; MONDO:0012544) is a rare, congenital, autosomal dominant limb-malformation syndrome caused by heterozygous mutations in **HOXD13**, the homeodomain transcription factor on chromosome 2q31.1 that patterns the distal limb (autopod). The disorder combines short digits (**brachydactyly**, overlapping types A4, D, and E) with digit fusion (**syndactyly**, with mild syndactyly of toes 2–3), and was formally defined by Zhao et al. in 2007 through the study of two large Han Chinese families — one with syndactyly type V and the other with the overlapping brachydactyly-syndactyly phenotype ([PMID: 17236141](https://pubmed.ncbi.nlm.nih.gov/17236141/)). The syndrome sits on a continuous *HOXD13* allelic spectrum that also encompasses synpolydactyly type 1 (SPD1, OMIM 186000) and syndactyly type V (SDTY5, OMIM 186300).

The central mechanistic insight of this investigation is that **different classes of HOXD13 mutation act through distinct molecular mechanisms that converge on dysregulated autopod chondrogenesis**. Polyalanine-tract expansions in the N-terminal intrinsically disordered region act through a dominant-negative / gain-of-function mechanism now understood to involve altered **transcriptional condensate phase separation** ("unblending"), while truncating, frameshift, splice-site, and DNA-binding-domain missense variants act through **haploinsufficiency / loss of function**. These converge downstream onto a shared set of limb-patterning pathways: the EPHA7 receptor tyrosine kinase (a direct HOXD13 transcriptional target), retinoic-acid synthesis (RALDH2/Raldh2), WNT5A-planar-cell-polarity signaling controlling chondrocyte polarity, and the SHH/GREM1/FGF/BMP2 feedback network — all validated in *Spdh*, *Dyc*, and *Hoxd13*-Q50R mouse models.

Clinically, the syndrome shows **incomplete penetrance** and **highly variable, often asymmetric expressivity**, with phenotype severity correlating positively with alanine-repeat length. Lifespan is normal, morbidity is confined to hand and foot function and cosmesis, and management is entirely **surgical and supportive** (syndactyly release, polydactyly/brachydactyly correction, hand/occupational therapy) plus genetic counseling — there is no disease-modifying pharmacotherapy. Diagnosis is clinical/radiographic, confirmed by HOXD13 molecular testing including triplet-repeat-length analysis, and prenatal diagnosis is feasible by combined ultrasound and mutation analysis.

---

## Section 1: Disease Information

**Overview.** Brachydactyly-syndactyly syndrome is a Mendelian, congenital limb-malformation disorder of the distal limb (hands and feet). It is characterized by shortening of digits (brachydactyly) combined with incomplete separation/fusion of digits (syndactyly). It was defined as a novel clinical entity by Zhao et al. (2007) in a Han Chinese family whose limb features overlapped brachydactyly types A4, D, and E together with mild syndactyly of toes 2 and 3 ([PMID: 17236141](https://pubmed.ncbi.nlm.nih.gov/17236141/)): *"We describe two large Han Chinese families with different limb malformations, one with syndactyly type V and the other with limb features overlapping brachydactyly types A4, D, and E and mild syndactyly of toes 2 and 3."*

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0012544 |
| OMIM | 610713 (brachydactyly-syndactyly syndrome) |
| Related OMIM phenotypes | 186000 (Synpolydactyly type 1, SPD1); 186300 (Syndactyly type V) |
| Gene | HOXD13 (HGNC:5136; OMIM *142989); chromosome 2q31.1 |
| ICD-10 | Q70–Q74 range (congenital malformations of limbs); Q70 (syndactyly) |
| MeSH | Synpolydactyly / Syndactyly / Brachydactyly |

**Synonyms / alternative names.** Brachydactyly-syndactyly syndrome; HOXD13-related limb malformation; the broader allelic series is often referred to as the **HOXD13-associated synpolydactyly (SPD1) spectrum**. Related named allelic entities include syndactyly type V (SDTY5) and synpolydactyly type 1.

**Source of information.** The information is derived from **aggregated disease-level resources** (OMIM, Orphanet, primary literature) and detailed **individual-patient / family-level clinical-genetic reports** — notably large multigenerational pedigrees (Han Chinese, Pakistani, Polish, and others) and the recent 87-family cohort study of Gottschalk et al. (2023, [PMID: 37427568](https://pubmed.ncbi.nlm.nih.gov/37427568/)), which pooled 38 new and 49 published families.

---

## Section 2: Etiology

**Primary cause — genetic.** The disorder is a monogenic, autosomal dominant condition caused by **heterozygous mutations in HOXD13**. There is no known environmental, infectious, or toxic cause; it is a developmental (morphogenetic) disorder of embryonic limb patterning.

**Genetic risk factors (causal variants).** Causal lesions in HOXD13 fall into several classes:

- **Polyalanine-tract expansions** in the imperfect GCN-triplet-containing exon 1 (most common; e.g., +7 to +9 alanine additions) — the predominant cause of the synpolydactyly end of the spectrum.
- **Polyalanine contraction** — a 21-bp deletion producing a 7-residue polyalanine contraction defined the original brachydactyly-syndactyly family ([PMID: 17236141](https://pubmed.ncbi.nlm.nih.gov/17236141/)): *"we detected a deletion of 21 bp in the imperfect GCN...triplet-containing exon 1 of HOXD13, which results in a polyalanine contraction of seven residues."*
- **Homeodomain missense variants** (e.g., p.Q317R, p.I47L, p.Q50R, p.Thr313Arg) that abolish DNA binding and transactivation.
- **Truncating variants** — nonsense (p.Gln248Ter, p.Gln287Ter), frameshift (p.Gly237fs), and splice-donor-site mutations acting through haploinsufficiency.

**Modifier genes and susceptibility loci.** Beyond HOXD13 itself, other genes can produce overlapping phenotypes: **PTHLH** (brachydactyly type E, [PMID: 31283647](https://pubmed.ncbi.nlm.nih.gov/31283647/), [PMID: 26763883](https://pubmed.ncbi.nlm.nih.gov/26763883/)), **FBLN1** (rare SPD deletion), **TTC30B** (candidate SPD variant, [PMID: 31306809](https://pubmed.ncbi.nlm.nih.gov/31306809/)), and in broader congenital limb-anomaly cohorts **LMBR1, GJA1, TP63** ([PMID: 39639541](https://pubmed.ncbi.nlm.nih.gov/39639541/)). GLI3 (GLI3R) interacts with HOXD13 in limb pre-patterning and modulates the phenotype ([PMID: 22373878](https://pubmed.ncbi.nlm.nih.gov/22373878/)).

**Environmental / protective factors / gene-environment interactions.** None are established for this Mendelian disorder. No environmental toxins, lifestyle factors, maternal exposures, or protective alleles are implicated. The one notable experimental "environmental" modifier is **intrauterine retinoic acid supplementation**, which rescued the polydactyly phenotype in the mouse *spdh* model ([PMID: 19075394](https://pubmed.ncbi.nlm.nih.gov/19075394/)) — a laboratory finding, not a human exposure. **This category is largely not applicable** to a congenital Mendelian limb-patterning syndrome.

---

## Section 3: Phenotypes

The core phenotype is a combination of **physical/structural congenital malformations** of the autopod. All are **congenital (present at birth)**, **stable/non-progressive**, and affect bones and soft tissues of the hands and feet.

| Phenotype | HPO term (suggested) | Type | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Brachydactyly (short digits) | HP:0001156 | Physical/skeletal | Congenital | Mild–severe, variable | Core feature |
| Short metacarpal | HP:0010049 | Physical/skeletal | Congenital | Variable | Common |
| Short phalanx of finger | HP:0009803 | Physical/skeletal | Congenital | Variable | Common |
| Cutaneous syndactyly | HP:0010554 | Physical/soft tissue | Congenital | Mild (toes 2–3) to complex | Core feature |
| Finger syndactyly | HP:0006101 | Physical | Congenital | Variable | Common |
| Toe syndactyly | HP:0001770 | Physical | Congenital | Mild | Core feature |
| Synpolydactyly | HP:0009855 (related) | Physical | Congenital | Variable | Spectrum end |
| Clinodactyly | HP:0030084 | Physical | Congenital | Mild | Reported |
| Metacarpal-to-carpal transformation | — | Physical/skeletal | Congenital | Severe | Homozygotes |

**Phenotype characteristics.** Onset is uniformly **congenital/neonatal**; the malformations are **non-progressive and stable** across life. Severity ranges from **mild** (short 5th metacarpal, clinodactyly, subtle toe webbing) to **severe** (osseous synpolydactyly, metacarpal-to-carpal transformation in homozygotes). Gottschalk et al. documented the full breadth ([PMID: 37427568](https://pubmed.ncbi.nlm.nih.gov/37427568/)): *"Phenotypes ranged from unaffected heterozygotes to severe osseous synpolydactyly, with intra- and inter-familial heterogeneity and asymmetry."* A pathognomonic feature of homozygous SPD1 is a relatively long, medially deviated big toe with/without cupping of the forefoot ([PMID: 32509852](https://pubmed.ncbi.nlm.nih.gov/32509852/)).

**Quality-of-life impact.** Impact is confined to **hand and foot function and appearance** — manual dexterity, grip, fine motor development, footwear fit, and psychosocial/cosmetic concerns. There is no systemic, cognitive, or life-limiting impact in the non-syndromic HOXD13 form. (Syndromic brachydactyly+syndactyly phenotypes with intellectual disability, microcephaly, and short stature — e.g., [PMID: 21416592](https://pubmed.ncbi.nlm.nih.gov/21416592/) — are *distinct* entities and should not be conflated with HOXD13-related disease.)

---

## Section 4: Genetic / Molecular Information

**Causal gene.** **HOXD13** (Homeobox D13; HGNC:5136; OMIM *142989), the most 5′ gene of the HOXD cluster on **chromosome 2q31.1**. HOXD13 encodes a homeodomain transcription factor that, with HOXA13, is specifically expressed in the developing autopod ([PMID: 8898214](https://pubmed.ncbi.nlm.nih.gov/8898214/)): *"Only two genes from homology group 13 (Hoxa-13 and Hoxd-13) are specifically expressed in the developing distal region (the autopod), which displays the most complex and evolutionarily flexible pattern among limb 'segments'."*

**Pathogenic variant classes and functional consequences.**

| Variant (example) | Type | Mechanism | Phenotype | PMID |
|---|---|---|---|---|
| 21-bp deletion → polyAla −7 | In-frame deletion | Altered condensation | Brachydactyly-syndactyly | [17236141](https://pubmed.ncbi.nlm.nih.gov/17236141/) |
| polyAla expansion (+7 to +9 Ala) | In-frame expansion | Dominant-negative / phase separation | Synpolydactyly | [37427568](https://pubmed.ncbi.nlm.nih.gov/37427568/), [32386547](https://pubmed.ncbi.nlm.nih.gov/32386547/) |
| c.184_210dup (+9 Ala) | Expansion | Dominant-negative | SPD1 | [22161087](https://pubmed.ncbi.nlm.nih.gov/22161087/) |
| c.950A>G (p.Q317R) | Homeodomain missense | Loss of DNA binding; abolishes EPHA7 transactivation | Syndactyly type V | [17236141](https://pubmed.ncbi.nlm.nih.gov/17236141/) |
| p.I47L | Homeodomain missense | Loss of DNA binding / EphA7 transactivation | Brachydactyly-polydactyly | [16314414](https://pubmed.ncbi.nlm.nih.gov/16314414/) |
| c.938C>G (p.Thr313Arg), homozygous | DNA-binding missense | Abolishes DNA binding (EMSA); non-penetrant in heterozygotes | Severe brachydactyly, metacarpal-to-carpal transformation | [26581570](https://pubmed.ncbi.nlm.nih.gov/26581570/) |
| c.708_720del13 (p.Gly237fs) | Frameshift | Premature termination / LOF | BDA3 + atypical BDA4 | [32789964](https://pubmed.ncbi.nlm.nih.gov/32789964/) |
| c.859C>T (p.Gln287Ter) | Nonsense | Haploinsufficiency via NMD | SPD (mild) | [31611522](https://pubmed.ncbi.nlm.nih.gov/31611522/) |
| c.781+1G>A (p.G190fsX4) | Splice-donor | Truncated non-DNA-binding protein / LOF | SPD + cortical bone thinning | [24055421](https://pubmed.ncbi.nlm.nih.gov/24055421/) |
| p.G11A | N-terminal missense | Destabilizes GLI3R; alters protein half-life | SPD | [22373878](https://pubmed.ncbi.nlm.nih.gov/22373878/) |

**Variant classification (ACMG/AMP).** Recurrent polyalanine expansions and the homeodomain missense variants are classified **pathogenic**; truncating variants causing haploinsufficiency are **pathogenic/likely pathogenic**. Interpretation is complicated by incomplete penetrance.

**Allele frequency / origin.** Pathogenic HOXD13 variants are **germline**, private or recurrent within families, and essentially absent from population databases (gnomAD) given their severe developmental consequence. There is **no somatic contribution**. The polyalanine expansions arise by replication-based mechanisms — both **unequal crossover** (duplication; *spdh*) and **fork stalling and template switching (FoSTeS)** (*Dyc* model, [PMID: 19546318](https://pubmed.ncbi.nlm.nih.gov/19546318/)).

**Functional consequences.** Two divergent mechanisms (see Section 6): **dominant-negative/gain-of-function** (polyalanine expansions) versus **loss-of-function/haploinsufficiency** (truncating and DNA-binding missense). As summarized by Zhang et al., *"missense and out-of-frame deletion mutations in the HOXD13 gene are also known to cause SPD, and the mechanism responsible for the phenotype appears to be haploinsufficiency"* ([PMID: 21814222](https://pubmed.ncbi.nlm.nih.gov/21814222/)).

**Modifier genes, epigenetics, chromosomal abnormalities.** Modifiers include GLI3 (GLI3R), HOXA13 (partially redundant paralog), and PTHLH. Epigenetic contributions are not a primary feature. Large interstitial deletions at distinct loci (e.g., 12p11.22-12.1 encompassing PTHLH) can cause phenocopy brachydactyly type E ([PMID: 31283647](https://pubmed.ncbi.nlm.nih.gov/31283647/)).

---

## Section 5: Environmental Information

**Not applicable as a cause.** This is a Mendelian developmental disorder with no established environmental, lifestyle, or infectious etiology. No toxins, radiation, pollution, occupational exposures, dietary factors, or pathogens are implicated in causation or triggering. The sole experimental environmental modifier is **retinoic acid**, demonstrated only as an *in utero* pharmacological rescue in the mouse *spdh* model ([PMID: 19075394](https://pubmed.ncbi.nlm.nih.gov/19075394/)) — mechanistically informative but not a human environmental risk/protective factor.

---

## Section 6: Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous HOXD13 mutation** (polyalanine expansion/contraction in exon 1, OR a homeodomain/truncating loss-of-function variant) is present in the germline and expressed in autopod mesenchyme. *(demonstrated)*

2. **Branch A — polyalanine expansion:** The altered N-terminal intrinsically disordered region **changes the phase-separation / co-condensation behavior** of HOXD13, perturbing the composition of HOXD13-containing transcriptional condensates and **interfering with other HOXD proteins** (dominant-negative). *(demonstrated in vitro and in mouse; [PMID: 32386547](https://pubmed.ncbi.nlm.nih.gov/32386547/), [PMID: 11543619](https://pubmed.ncbi.nlm.nih.gov/11543619/))*

   **Branch B — truncating / DNA-binding missense:** The variant produces a **non-DNA-binding or NMD-degraded protein**, reducing functional HOXD13 dosage → **haploinsufficiency**. *(demonstrated; [PMID: 21814222](https://pubmed.ncbi.nlm.nih.gov/21814222/), [PMID: 24055421](https://pubmed.ncbi.nlm.nih.gov/24055421/))*

3. Both branches **dysregulate the HOXD13 transcriptional program** in digit-forming mesenchyme. *(demonstrated)*

4. This **leads to loss of direct activation of EPHA7**, a receptor tyrosine kinase target normally transactivated by HOXD13/HOXA13 at paralog-13 Hox binding sites. *(demonstrated; [PMID: 16314414](https://pubmed.ncbi.nlm.nih.gov/16314414/))*

5. In parallel, mutant HOXD13 **reduces RALDH2-dependent retinoic-acid synthesis** and promotes **ectopic interdigital chondrogenesis** (increased Sox9), **resulting in** extra/fused digits. *(demonstrated in spdh mouse; [PMID: 19075394](https://pubmed.ncbi.nlm.nih.gov/19075394/))*

6. Mutant HOXD13 also **fails to induce WNT5A/WNT5B**, **leading to** randomized chondrocyte polarity and mislocalized planar-cell-polarity components (DVL2, PRICKLE1) with perichondrial WNT/β-catenin upregulation → **metacarpal-to-carpal transformation** and loss of cortical bone/perichondrium. *(demonstrated in spdh mouse; [PMID: 24161848](https://pubmed.ncbi.nlm.nih.gov/24161848/))*

7. For homeodomain mutants, **disruption of the SHH/GREM1/AER-FGF8 feedback loop with BMP2 downregulation** occurs in the limb bud, **resulting in** combined syndactyly, brachydactyly, and polydactyly. *(demonstrated in Hoxd13-Q50R mouse; [PMID: 38561387](https://pubmed.ncbi.nlm.nih.gov/38561387/))*

8. Collectively, defective chondrocyte differentiation, reduced proliferation, abnormal joint patterning, and disrupted digit separation **produce the congenital brachydactyly-syndactyly phenotype**. *(demonstrated)*

### Molecular pathways and detail

- **Transcriptional condensate phase separation (upstream, dominant-negative branch).** Basu et al. (Cell 2020) showed that alanine-repeat expansions in the HOXD13 intrinsically disordered region *"alter its phase separation capacity and its capacity to co-condense with transcriptional co-activators"* and that *"HOXD13 repeat expansions perturb the composition of HOXD13-containing condensates in vitro and in vivo and alter the transcriptional program in a cell-specific manner in a mouse model of synpolydactyly"* ([PMID: 32386547](https://pubmed.ncbi.nlm.nih.gov/32386547/)). GO terms: GO:0006355 (regulation of DNA-templated transcription), GO:0032991 (protein-containing complex).

- **EPHA7 signaling (direct target).** Salsi & Zappavigna demonstrated *"HOXD13 and HOXA13 activate transcription from the EphA7 promoter"* and that the pathogenic I47L variant *"does not bind to in vivo, and fails to transactivate the EphA7 promoter"* ([PMID: 16314414](https://pubmed.ncbi.nlm.nih.gov/16314414/)). EphA7 governs differential cell affinity/sorting in the autopod.

- **SHH / ZRS / GREM1 / FGF / BMP2 (AP and feedback patterning).** HOXD13 cooperates with Hand2 at the ZRS enhancer to activate Shh ([PMID: 20386744](https://pubmed.ncbi.nlm.nih.gov/20386744/)): *"Hand2 is part of the protein complexes containing Hoxd13, another essential regulator of Shh activation in limb buds."* Hoxd13-Q50R mice showed *"ectopically expressed Shh, Grem1 and Fgf8 and down-regulated Bmp2 in the embryonic limb bud at E10.5 to E12.5"* ([PMID: 38561387](https://pubmed.ncbi.nlm.nih.gov/38561387/)).

- **Retinoic-acid pathway (downstream, chondrogenesis).** *"mutated Hoxd13 causes polydactyly in SPD by inducing extraneous interdigital chondrogenesis, both directly and indirectly, via a reduction in RA levels"* ([PMID: 19075394](https://pubmed.ncbi.nlm.nih.gov/19075394/)). CHEBI: retinoic acid (CHEBI:26536).

- **WNT5A / planar cell polarity (chondrocyte orientation).** *"Wnt5a and the closely related Wnt5b were downregulated in spdh handplates, and HOXD13 induced expression of both genes in vitro"* and *"mislocalization of core planar cell polarity (PCP) components DVL2 and PRICKLE1 in spdh metacarpals indicating a defect in the WNT/PCP pathway"* ([PMID: 24161848](https://pubmed.ncbi.nlm.nih.gov/24161848/)).

- **GLI3R interaction.** The N-terminal p.G11A variant destabilizes GLI3 repressor during limb pre-patterning ([PMID: 22373878](https://pubmed.ncbi.nlm.nih.gov/22373878/)).

**Cellular processes:** chondrocyte differentiation and proliferation (reduced; [PMID: 11850178](https://pubmed.ncbi.nlm.nih.gov/11850178/)), chondrocyte planar polarity, interdigital apoptosis (disrupted separation), cell sorting/differential affinity, and joint patterning. **Suggested GO terms:** GO:0048704 (embryonic skeletal system morphogenesis), GO:0035108 (limb morphogenesis), GO:0002063 (chondrocyte development), GO:0001501 (skeletal system development), GO:0060173 (limb development). **Suggested CL terms:** CL:0000138 (chondrocyte), CL:0000134 (mesenchymal stem cell), CL:0000057 (fibroblast / limb mesenchymal cell).

**Upstream vs downstream.** Upstream: the HOXD13 mutation and altered transcriptional output. Midstream: EPHA7, SHH/GREM1/FGF/BMP2, WNT5A-PCP, and RA pathways. Downstream: chondrocyte polarity/differentiation/proliferation defects, altered digit separation and condensation → gross skeletal malformation.

---

## Section 7: Anatomical Structures Affected

**Organ/system level.** The disorder affects the **musculoskeletal system**, specifically the **distal limbs (autopod)** — hands and feet. There is no primary involvement of cardiovascular, nervous, respiratory, digestive, or endocrine systems in the non-syndromic HOXD13 form.

- **Primary structures:** phalanges, metacarpals, metatarsals, carpal/tarsal bones, interdigital webbing (skin/soft tissue), phalangeal joints.
- **UBERON terms:** UBERON:0002398 (manus/hand), UBERON:0002387 (pes/foot), UBERON:0002544 (digit), UBERON:0001436 (metacarpal bone), UBERON:0003221 (phalanx), UBERON:0006048 (autopod region).

**Tissue and cell level.** **Cartilage and bone tissue** (endochondral skeleton) and **interdigital mesenchyme/skin** are affected. Key cell populations: **chondrocytes** (CL:0000138) in growth plates and perichondrium, **limb-bud mesenchymal cells** (CL:0000134), and perichondrial cells. Metacarpal-to-carpal transformation reflects a tissue-identity switch in cartilage elements ([PMID: 24161848](https://pubmed.ncbi.nlm.nih.gov/24161848/), [PMID: 26581570](https://pubmed.ncbi.nlm.nih.gov/26581570/)). Cortical bone thinning is seen with certain splice variants ([PMID: 24055421](https://pubmed.ncbi.nlm.nih.gov/24055421/)).

**Subcellular level.** The primary subcellular locus is the **nucleus** (GO:0005634), where HOXD13 functions as a transcription factor, and the associated **biomolecular condensates / nuclear bodies** (transcriptional condensates). GO cellular-component terms: GO:0005634 (nucleus), GO:0000785 (chromatin), GO:0032991 (protein-containing complex).

**Localization and lateralization.** Both **hands and feet** are affected, typically **bilateral** but frequently **asymmetric** between the two sides and between individuals ([PMID: 37427568](https://pubmed.ncbi.nlm.nih.gov/37427568/)). The feet (especially toes 2–3 webbing and the big-toe anomaly) and the fourth web space / 4th–5th digits are characteristically involved.

---

## Section 8: Temporal Development

**Onset.** **Congenital** — the malformations are established during embryonic limb patterning (approximately E10.5–E12.5 in mouse models; first trimester in humans) and are present at birth. Onset pattern is **developmental/static**, not acute or progressive.

**Progression.** The structural anomalies are **stable and non-progressive** across life; they do not worsen biologically, though functional/cosmetic consequences persist lifelong unless surgically corrected. There are **no disease stages** in the oncologic or neurodegenerative sense. Growth-plate and chondrocyte abnormalities in the *spdh* mouse persist postnatally and correlate with continued mutant Hoxd13 expression ([PMID: 11850178](https://pubmed.ncbi.nlm.nih.gov/11850178/)).

**Patterns and critical periods.** There is no remission. The **critical period of vulnerability** is embryonic autopod patterning. The **critical window of therapeutic opportunity** in experimental models is in utero (retinoic-acid rescue in mice, [PMID: 19075394](https://pubmed.ncbi.nlm.nih.gov/19075394/)); in humans, the practical intervention window is postnatal surgical correction, typically in infancy/early childhood.

---

## Section 9: Inheritance and Population

**Epidemiology.** This is a **rare disorder**. Synpolydactyly (the broader HOXD13 spectrum) has an estimated prevalence on the order of ~1 in 300,000 (Orphanet-level estimates); the specific brachydactyly-syndactyly syndrome is defined from individual large pedigrees and precise population prevalence/incidence figures are **not established**. Hand syndactyly overall (all causes) is the most common upper-extremity congenital malformation ([PMID: 40206497](https://pubmed.ncbi.nlm.nih.gov/40206497/)).

**Inheritance pattern.** **Autosomal dominant** (HOXD13 at 2q31.1). Severe forms (e.g., metacarpal-to-carpal transformation) can appear in **homozygotes**, with the heterozygous state non-penetrant ([PMID: 26581570](https://pubmed.ncbi.nlm.nih.gov/26581570/)).

**Penetrance and expressivity.** Characterized by **incomplete penetrance** and **highly variable expressivity**, including asymmetry and unaffected mutation carriers ([PMID: 37427568](https://pubmed.ncbi.nlm.nih.gov/37427568/), [PMID: 21814222](https://pubmed.ncbi.nlm.nih.gov/21814222/)). Severity correlates with **alanine-repeat length** ([PMID: 37427568](https://pubmed.ncbi.nlm.nih.gov/37427568/)): *"Computer-aided analysis only corroborated a positive correlation between alanine repeat length and phenotype severity."*

**Genetic anticipation, mosaicism, founder effects.** No genetic anticipation is established (polyalanine tracts are relatively stable compared with polyglutamine repeat disorders). Germline mosaicism is theoretically possible but not prominently documented. No strong founder effects; recurrent expansions arise independently via unequal crossover or FoSTeS ([PMID: 19546318](https://pubmed.ncbi.nlm.nih.gov/19546318/)). **Consanguinity** is relevant for the rare homozygous severe forms.

**Population demographics.** Families reported across diverse ancestries — Han Chinese ([PMID: 17236141](https://pubmed.ncbi.nlm.nih.gov/17236141/), [PMID: 22161087](https://pubmed.ncbi.nlm.nih.gov/22161087/)), Pakistani ([PMID: 39639541](https://pubmed.ncbi.nlm.nih.gov/39639541/)), Polish ([PMID: 26763883](https://pubmed.ncbi.nlm.nih.gov/26763883/)), and the pan-ancestry Gottschalk cohort. No strong geographic clustering. **Sex ratio** is approximately equal (autosomal). **Age distribution:** congenital, affecting all ages equally since the phenotype is lifelong.

---

## Section 10: Diagnostics

**Clinical/radiographic diagnosis.** Diagnosis begins with **clinical examination** (short and/or fused digits, extra digits) and **hand/foot radiographs** demonstrating short or fused metacarpals/metatarsals, abnormal/short phalanges, extra digits, and in severe cases metacarpal-to-carpal transformation and cortical bone thinning.

**Genetic/molecular confirmation.** Confirmed by **HOXD13 molecular testing**, including **Sanger/next-generation sequencing** of coding exons plus **triplet-repeat (polyalanine) length analysis** of exon 1 (standard sequencing may miss or misread the GCN repeat). Jin et al. illustrate the approach — STR linkage (D2S1238/D2S1245 flanking HOXD13) plus repeat-length detection of a 27-bp expansion ([PMID: 22161087](https://pubmed.ncbi.nlm.nih.gov/22161087/)): *"a heterozygous 27 bp expansion within the imperfect GCN triplet-repeat of exon 1, c.184_210dup, was identified."* Whole-exome sequencing (trio-WES) effectively identifies point/truncating variants ([PMID: 31611522](https://pubmed.ncbi.nlm.nih.gov/31611522/), [PMID: 39639541](https://pubmed.ncbi.nlm.nih.gov/39639541/)).

**Recommended testing hierarchy:** (1) targeted HOXD13 sequencing + repeat-length assay for classic phenotypes; (2) limb-malformation gene panel (HOXD13, GLI3, PTHLH, FBLN1, TP63, LMBR1, GJA1) for atypical/overlapping presentations; (3) WES/WGS for undiagnosed cases; (4) CMA/array-CGH when a contiguous-gene deletion is suspected (e.g., PTHLH-related BDE, [PMID: 31283647](https://pubmed.ncbi.nlm.nih.gov/31283647/)).

**Prenatal diagnosis.** Feasible by **combined ultrasound and molecular analysis** ([PMID: 22161087](https://pubmed.ncbi.nlm.nih.gov/22161087/)): *"Accurate prenatal diagnosis of SPD was achieved with combined ultrasound and molecular analysis."* Amniocentesis-based linkage/mutation analysis at ~18 weeks plus 16–21-week ultrasound of the digits was used successfully.

**Omics/other diagnostics.** Not routinely used. No specific laboratory biomarkers, metabolites, or circulating markers exist — diagnosis is radiographic and genetic.

**Differential diagnosis.** Other brachydactylies (BDA3, BDA4, BDE from PTHLH), isolated syndactyly/polydactyly syndromes, acrocephalosyndactyly syndromes (Apert/Pfeiffer — FGFR2, [PMID: 40620881](https://pubmed.ncbi.nlm.nih.gov/40620881/), [PMID: 42082645](https://pubmed.ncbi.nlm.nih.gov/42082645/)), amniotic band sequence ([PMID: 41215847](https://pubmed.ncbi.nlm.nih.gov/41215847/)), and syndromic forms with intellectual disability/microcephaly ([PMID: 21416592](https://pubmed.ncbi.nlm.nih.gov/21416592/)). Distinguishing features: the HOXD13 form is isolated (non-syndromic), affects the autopod with characteristic 4th-web and toe-2/3 involvement, and lacks craniofacial/cognitive/systemic features.

**Screening.** No population newborn screening (structural, non-metabolic). **Cascade genetic testing** of at-risk family members and **carrier counseling** are appropriate.

---

## Section 11: Outcome / Prognosis

**Survival and mortality.** **Normal life expectancy; no increased mortality.** This is a non-lethal structural malformation of the limbs with no systemic organ involvement.

**Morbidity and function.** Morbidity is limited to **hand/foot function** (grip, dexterity, fine motor skills), **footwear/ambulation** (for foot involvement), and **cosmetic/psychosocial** impact. Disability ranges from negligible (mild brachydactyly) to functionally significant (complex syndactyly/polydactyly requiring reconstruction).

**Disease course and complications.** Static and lifelong; complications are chiefly those of untreated digital fusion/duplication (impaired dexterity, asymmetric growth) and of surgery (web creep, scarring, need for revision). Early release in selected contexts reduces asymmetric finger growth ([PMID: 41215847](https://pubmed.ncbi.nlm.nih.gov/41215847/)).

**Recovery potential and prognostic factors.** Surgical correction generally yields good-to-excellent functional and cosmetic outcomes; e.g., first-web syndactyly series achieved favorable results with dorsal commissural flaps and grafts ([PMID: 41030430](https://pubmed.ncbi.nlm.nih.gov/41030430/)). Prognostic factors: severity/complexity of the malformation, number of digits involved, presence of osseous (vs cutaneous-only) fusion, and timing/quality of surgery. **Prognostic biomarkers:** none; alanine-repeat length is a genotypic severity correlate rather than a clinical-course biomarker.

*Note:* One retrospective database study reported an association between **nonsyndromic syndactyly** and increased rates of benign neoplasms and digestive malignancies ([PMID: 41797684](https://pubmed.ncbi.nlm.nih.gov/41797684/)); this is an epidemiologic signal requiring confirmation and is **not established as a feature of HOXD13-related disease specifically**.

---

## Section 12: Treatment

**No disease-modifying pharmacotherapy exists.** There is no approved pharmacological, RNA-based, cell, or gene therapy for HOXD13-related limb malformation. Retinoic-acid rescue is an *in utero* mouse finding only ([PMID: 19075394](https://pubmed.ncbi.nlm.nih.gov/19075394/)) and is **not a human therapy**.

**Surgical and interventional (mainstay).** Treatment targets the structural anomaly:

- **Syndactyly release** — Z-plasty for simple cases; dorsal commissural/advancement flaps and full-thickness skin grafts for complex/first-web cases ([PMID: 41030430](https://pubmed.ncbi.nlm.nih.gov/41030430/)): *"Dorsal commissural flaps were the initial operative approach in 100% of the complex/complicated cases, whereas Z-plasties were used in 64% of the simple cases. Full-thickness skin grafts were required in 12 (86%) of the complex/complicated cases."*
- **Polydactyly excision and brachydactyly correction** as indicated.
- Surgical management of syndactyly is well-established ([PMID: 40206497](https://pubmed.ncbi.nlm.nih.gov/40206497/)): *"Hand syndactyly is a congenital malformation resulting from the failure of differentiation between two or more digits, resulting in a subsequent fusion."*
- **Timing** is individualized; early release is favored in selected contexts to optimize growth and function ([PMID: 41215847](https://pubmed.ncbi.nlm.nih.gov/41215847/)).

**Supportive and rehabilitative.** Postoperative **hand therapy / occupational therapy**, splinting/bracing, and dressing care; attention to fine-motor development and psychosocial support.

**Experimental / advanced therapeutics.** None specific to this disorder. No gene-therapy, ASO, siRNA, or small-molecule programs are in clinical trials for HOXD13 limb malformation.

**Suggested NCIT intervention terms:** NCIT:C15329 (reconstructive surgery), surgical procedure/hand surgery, NCIT:C15277 (physical therapy), NCIT:C15431 (occupational therapy), NCIT:C15215 (skin graft).

**Pharmacogenomics / personalized medicine / combination therapy:** not applicable — management is anatomical/reconstructive, individualized to the malformation.

---

## Section 13: Prevention

**Primary prevention.** Not possible for a spontaneous/inherited Mendelian developmental disorder. **Genetic counseling** is the principal preventive tool: affected individuals have a 50% transmission risk (autosomal dominant), tempered by incomplete penetrance and variable expressivity.

**Secondary prevention / screening.** **Cascade genetic testing** of relatives and **prenatal diagnosis** (combined ultrasound + HOXD13 mutation analysis, [PMID: 22161087](https://pubmed.ncbi.nlm.nih.gov/22161087/)) enable informed reproductive decision-making. **Preimplantation genetic testing (PGT-M)** is applicable where the familial variant is known.

**Tertiary prevention.** Timely surgical correction and hand therapy to prevent functional disability, asymmetric growth, and contractures.

**Immunization, public-health, environmental, prophylactic, behavioral interventions:** **not applicable** — no infectious or environmental component.

---

## Section 14: Other Species / Natural Disease

**Model-species orthologs.** HOXD13 is deeply conserved. Mouse *Hoxd13* (NCBI Gene ID 15433) is the direct ortholog; chick and zebrafish orthologs exist. Zebrafish HoxD/HoxA cluster genes are expressed during fin development, and comparative studies of digit origin place Hoxd13 at the center of the fin-to-limb transition ([PMID: 7791900](https://pubmed.ncbi.nlm.nih.gov/7791900/)).

**Natural / spontaneous disease in other species.** Two **spontaneous mouse mutants** phenocopy human disease:
- ***spdh*** (synpolydactyly homolog) — a 21-bp in-frame duplication expanding the polyalanine tract from 15 to 22 residues; homozygotes show polydactyly, syndactyly, and brachydactyly ([PMID: 9580668](https://pubmed.ncbi.nlm.nih.gov/9580668/)).
- ***Dyc*** ("Digit in Y and Carpe") — a trinucleotide expansion (+7 Ala) via FoSTeS, with an SPD-like phenotype ([PMID: 19546318](https://pubmed.ncbi.nlm.nih.gov/19546318/)).

**Comparative biology / evolutionary conservation.** The autopod-patterning role of HOXA13/HOXD13 is conserved across tetrapods; the mechanism (homeodomain transcription factor controlling digit morphogenesis) is evolutionarily ancient ([PMID: 8898214](https://pubmed.ncbi.nlm.nih.gov/8898214/), [PMID: 7791900](https://pubmed.ncbi.nlm.nih.gov/7791900/)). **NCBI Taxon:** Homo sapiens (9606), Mus musculus (10090), Gallus gallus (9031), Danio rerio (7955).

**Transmission / zoonotic potential:** not applicable (non-infectious, genetic).

---

## Section 15: Model Organisms

**Mammalian models (mouse — primary).**

| Model | Type | Lesion | Phenotype recapitulation | PMID |
|---|---|---|---|---|
| *spdh* | Spontaneous | PolyAla +7 (21-bp dup) | Polydactyly, syndactyly, brachydactyly; defective chondrocyte differentiation/proliferation, joint patterning; dominant-negative | [9580668](https://pubmed.ncbi.nlm.nih.gov/9580668/), [11850178](https://pubmed.ncbi.nlm.nih.gov/11850178/), [11543619](https://pubmed.ncbi.nlm.nih.gov/11543619/) |
| *Dyc* | Spontaneous | PolyAla +7 (FoSTeS) | SPD-like limb patterning defect | [19546318](https://pubmed.ncbi.nlm.nih.gov/19546318/) |
| *Hoxd13* Q50R | Knock-in | Homeodomain missense | Dose-dependent brachydactyly + syndactyly (het) → severe syndactyly/brachydactyly/polydactyly (homo); SHH/GREM1/FGF8 up, BMP2 down | [38561387](https://pubmed.ncbi.nlm.nih.gov/38561387/) |
| *Hoxa13/Hoxd13* compound | Targeted null | LOF | Severe autopod patterning defects; partial redundancy, dosage control | [8898214](https://pubmed.ncbi.nlm.nih.gov/8898214/) |

The *Hoxd13* Q50R model faithfully reproduces the human dose-dependent phenotype ([PMID: 38561387](https://pubmed.ncbi.nlm.nih.gov/38561387/)): *"The mutant mice exhibited obvious limb malformations including slight brachydactyly and partial syndactyly between digits 2-4 in the heterozygotes, and severe syndactyly, brachydactyly and polydactyly in homozygotes."*

**Other systems.** The **chick embryo** is used for in vivo misexpression studies of HOXD13 variants (e.g., G11A, G11A/GLI3R; [PMID: 22373878](https://pubmed.ncbi.nlm.nih.gov/22373878/), [PMID: 21782042](https://pubmed.ncbi.nlm.nih.gov/21782042/)) and for studying differential cell affinity/sorting in recombinant limb buds ([PMID: 12376104](https://pubmed.ncbi.nlm.nih.gov/12376104/)). **In vitro** systems include luciferase/EMSA transactivation assays (EphA7, EMSA DNA-binding) and phase-separation/condensate assays ([PMID: 32386547](https://pubmed.ncbi.nlm.nih.gov/32386547/)).

**Model strengths and limitations.** Strengths: *spdh* and Q50R reproduce the full brachydactyly-syndactyly-polydactyly spectrum and allow dissection of SHH/GREM1/FGF/BMP2, RA, WNT5A-PCP, and EphA7 mechanisms, plus in utero RA rescue. Limitations: mouse homozygotes are more severe than typical human heterozygotes; incomplete penetrance and human condensate biology are harder to model; *spdh* males have reproductive-gland anomalies not seen in humans. **Resources:** MGI (Mouse Genome Informatics).

---

## Mechanistic Model / Interpretation

```
          HOXD13 MUTATION (germline, heterozygous)
                        │
         ┌──────────────┴───────────────┐
   BRANCH A                        BRANCH B
   polyAla expansion/              truncating / homeodomain
   contraction (exon 1)            missense (DNA-binding)
         │                              │
  altered phase separation        no DNA binding / NMD
  & co-condensation               → HAPLOINSUFFICIENCY
  → DOMINANT-NEGATIVE             (reduced HOXD13 dosage)
  (interferes w/ other HOXD)            │
         └──────────────┬───────────────┘
                        ▼
           DYSREGULATED HOXD13 TRANSCRIPTIONAL PROGRAM
                        │
     ┌──────────┬───────────────┬────────────────┐
     ▼          ▼               ▼                 ▼
  ↓ EphA7   ↓ RALDH2/RA   ↓ WNT5A/WNT5B     SHH/GREM1/FGF8↑
  (direct   (ectopic      (randomized         BMP2↓
  target)   interdigital  chondrocyte        (Q50R model)
            chondrogen.)  polarity; PCP
                          DVL2/PRICKLE1
                          mislocalized)
     └──────────┴───────────────┴────────────────┘
                        ▼
   DEFECTIVE CHONDROCYTE DIFFERENTIATION/PROLIFERATION,
   ABNORMAL JOINT PATTERNING, FAILED DIGIT SEPARATION,
   METACARPAL→CARPAL TRANSFORMATION
                        ▼
   CONGENITAL BRACHYDACTYLY + SYNDACTYLY (± POLYDACTYLY)
   severity ∝ alanine-repeat length; incomplete penetrance;
   variable, asymmetric expressivity
```

The unifying interpretation is **quantitative homeoprotein dosage control of digit morphogenesis**: HOXD13 output must be precisely tuned, and both too-little functional protein (haploinsufficiency) and a dominant-negative/condensation-altering mutant protein corrupt the same downstream patterning network, producing a graded phenotype.

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [17236141](https://pubmed.ncbi.nlm.nih.gov/17236141/) | Primary — defining | Defines brachydactyly-syndactyly syndrome; HOXD13 polyAla contraction & Q317R abolishing EPHA7 transactivation |
| [8898214](https://pubmed.ncbi.nlm.nih.gov/8898214/) | Foundational | HOXA13/HOXD13 autopod-specific expression; dosage control of digits |
| [20386744](https://pubmed.ncbi.nlm.nih.gov/20386744/) | Mechanism | HOXD13–Hand2 complex activates Shh via ZRS |
| [19075394](https://pubmed.ncbi.nlm.nih.gov/19075394/) | Mechanism (mouse) | Retinoic-acid reduction → ectopic interdigital chondrogenesis; in utero RA rescue |
| [21814222](https://pubmed.ncbi.nlm.nih.gov/21814222/) | Mechanism | Haploinsufficiency for missense/out-of-frame deletions |
| [37427568](https://pubmed.ncbi.nlm.nih.gov/37427568/) | Clinical cohort | 87 families; penetrance, expressivity, repeat-length/severity; condensation mechanism |
| [24161848](https://pubmed.ncbi.nlm.nih.gov/24161848/) | Mechanism (mouse) | WNT5A-PCP control of chondrocyte polarity; metacarpal→carpal |
| [38561387](https://pubmed.ncbi.nlm.nih.gov/38561387/) | Model | Hoxd13-Q50R knock-in; SHH/GREM1/FGF8↑, BMP2↓; dose-dependent phenotype |
| [32789964](https://pubmed.ncbi.nlm.nih.gov/32789964/) | Clinical/genetic | Frameshift → BDA3+BDA4 |
| [26581570](https://pubmed.ncbi.nlm.nih.gov/26581570/) | Clinical/genetic | Homozygous DNA-binding missense; non-penetrant heterozygotes |
| [16314414](https://pubmed.ncbi.nlm.nih.gov/16314414/) | Mechanism | EphA7 as direct HOXD13/HOXA13 target; I47L fails to transactivate |
| [22161087](https://pubmed.ncbi.nlm.nih.gov/22161087/) | Diagnostics | Prenatal diagnosis via ultrasound + repeat-length analysis |
| [41030430](https://pubmed.ncbi.nlm.nih.gov/41030430/) | Treatment | First-web syndactyly surgical techniques/outcomes |
| [40206497](https://pubmed.ncbi.nlm.nih.gov/40206497/) | Treatment | Systematic review of hand syndactyly |
| [32386547](https://pubmed.ncbi.nlm.nih.gov/32386547/) | Mechanism | Phase-separation/condensate "unblending" for polyAla expansions |
| [9580668](https://pubmed.ncbi.nlm.nih.gov/9580668/), [19546318](https://pubmed.ncbi.nlm.nih.gov/19546318/), [11850178](https://pubmed.ncbi.nlm.nih.gov/11850178/), [11543619](https://pubmed.ncbi.nlm.nih.gov/11543619/) | Models/mechanism | *spdh*/*Dyc* models; dominant-negative; expansion mechanisms |

**Evidence-type distribution:** human clinical-genetic (pedigrees, cohorts), mouse model organism (*spdh*, *Dyc*, Q50R, compound nulls), chick in vivo, and in vitro/biophysical (EMSA, luciferase, condensate assays). The mechanistic claims are strongly convergent across species and methods.

---

## Limitations and Knowledge Gaps

1. **Prevalence/incidence are not precisely quantified** for the specific brachydactyly-syndactyly syndrome; figures are inferred from the broader SPD1 spectrum.
2. **Genotype–phenotype correlation remains imperfect** — incomplete penetrance and asymmetric, variable expressivity (even within families) limit prediction; repeat length correlates with, but does not determine, severity.
3. The **phase-separation/condensate mechanism**, while demonstrated biophysically and in a mouse model, has not been translated into clinical biomarkers or therapeutic targets.
4. **Human therapeutic rescue** of the developmental lesion is not feasible (critical window is embryonic); RA rescue is mouse-only.
5. A reported **syndactyly–neoplasm association** ([PMID: 41797684](https://pubmed.ncbi.nlm.nih.gov/41797684/)) is from nonsyndromic syndactyly broadly and is **not validated for HOXD13 disease**; it should not be over-interpreted.
6. **Modifier genetics** (what determines penetrance/asymmetry) are essentially unknown.
7. Quality-of-life data are **anecdotal/surgical-series-based**, not systematically measured with validated instruments (EQ-5D, PROMIS).

---

## Proposed Follow-up Experiments / Actions

1. **Natural-history / registry study** of HOXD13-mutation carriers across the allelic spectrum to quantify penetrance, expressivity, asymmetry, and age-specific functional outcomes with validated QoL instruments.
2. **Condensate-targeted mechanistic work** — define how specific repeat lengths quantitatively shift HOXD13 condensate composition and downstream target expression (single-cell/spatial transcriptomics of developing autopod), building on [PMID: 32386547](https://pubmed.ncbi.nlm.nih.gov/32386547/).
3. **Modifier mapping** — WGS/GWAS within large pedigrees (and the Gottschalk cohort) to identify genetic modifiers of penetrance and laterality.
4. **Systematic genotype–phenotype database** linking variant class (expansion length, truncation position, homeodomain residue) to standardized HPO-coded phenotypes and surgical complexity.
5. **Functional screens** of VUS in HOXD13 using combined EMSA/EphA7-luciferase and condensate assays to improve ACMG classification.
6. **Surgical outcomes research** — prospective comparison of early vs delayed release and flap techniques for HOXD13-related complex syndactyly with standardized functional/cosmetic endpoints.
7. **Confirm or refute the neoplasm signal** specifically within genetically confirmed HOXD13 cohorts before any clinical surveillance recommendation.

---

*Report compiled from 11 confirmed findings and 44 reviewed papers over a 5-iteration autonomous investigation. All mechanistic and clinical claims are cited to primary literature (PMID). Evidence sources span human clinical-genetic, mouse/chick model-organism, and in vitro/biophysical studies.*


## Artifacts

- [OpenScientist final report](Brachydactyly-Syndactyly_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Brachydactyly-Syndactyly_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 35 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 31 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012544` (3 mentions) - the report calls it "MONDO"; MONDO calls it **brachydactyly-syndactyly syndrome**
- `HP:0009855` (1 mention) - the report calls it "related"; HP calls it **Osteolytic defects of the proximal phalanges of the hand**
- `CL:0000057` (1 mention) - the report calls it "fibroblast / limb mesenchymal cell"; CL calls it **fibroblast**
- `UBERON:0001436` (1 mention) - the report calls it "metacarpal bone"; UBERON calls it **phalanx of manus**
- `NCIT:C15277` (1 mention) - the report calls it "physical therapy"; NCIT calls it **Mastectomy**
- `NCIT:C15431` (1 mention) - the report calls it "occupational therapy"; NCIT calls it **Hematopoietic Cell Transplantation**
- `NCIT:C15215` (1 mention) - the report calls it "skin graft"; NCIT calls it **Cryosurgery**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001156` (1 mention) - the report calls it "Brachydactyly (short digits)"; HP calls it **Brachydactyly**
- `HP:0010554` (1 mention) - the report calls it "Cutaneous syndactyly"; HP calls it **Cutaneous finger syndactyly**
- `CL:0000134` (2 mentions) - the report calls it "mesenchymal stem cell", "limb-bud mesenchymal cells"; CL calls it **mesenchymal stem cell**
- `UBERON:0002398` (1 mention) - the report calls it "manus/hand"; UBERON calls it **manus**
- `UBERON:0002387` (1 mention) - the report calls it "pes/foot"; UBERON calls it **pes**, and lists "foot" among its other names
- `UBERON:0006048` (1 mention) - the report calls it "autopod region"; UBERON calls it **digit 1**, and lists "autopod digit 1" among its other names
- `NCIT:C15329` (1 mention) - the report calls it "reconstructive surgery"; NCIT calls it **Surgical Procedure**, and lists "Type of Surgery" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000138` - called "chondrocyte", "chondrocytes"
- `CL:0000134` - called "mesenchymal stem cell", "limb-bud mesenchymal cells"