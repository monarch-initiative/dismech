---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-17T04:36:06.287719'
end_time: '2026-10-17T04:54:01.231481'
duration_seconds: 1074.94
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Achalasia-Progeroid Syndrome
  mondo_id: MONDO:0700300
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
citation_count: 6
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 53
  verified: 52
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 44
  labels_matching: 37
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0700300
    reported_labels:
    - MONDO
    ontology_label: achalasia-progeroid syndrome
  - term_id: CL:0000057
    reported_labels:
    - "fibroblast \u2014 the in vitro model cell"
    ontology_label: fibroblast
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Achalasia-progeroid_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Achalasia-progeroid_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Achalasia-Progeroid Syndrome
- **MONDO ID:** MONDO:0700300 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Achalasia-Progeroid Syndrome** covering all of the
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

# Achalasia-Progeroid Syndrome (ACHPS): A Comprehensive Disease Characteristics Report

**Disease:** Achalasia-Progeroid Syndrome (ACHPS)
**Identifiers:** OMIM #621123 · MONDO:0700300 · MedGen C6012702 (UID 1876522) · GARD 0027387 · UMLS C6012702
**Category:** Mendelian (ultra-rare, autosomal recessive spliceosomopathy)
**Causal gene:** *BUD13* (HGNC:28199; NCBI Gene 84811; Ensembl ENSG00000137656; chromosome 11q23.3)
**Prepared:** 2026-10-17

> **Evidence base & caveat.** ACHPS is an ultra-rare, newly delineated Mendelian disorder. Essentially all primary human clinical/molecular data derive from a **single defining study of five affected individuals** — Kornak et al., *Alternative splicing of BUD13 determines the severity of a developmental disorder with lipodystrophy and progeroid features* ([PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)). Mechanistic context is supplemented by zebrafish, yeast, and plant RES-complex studies. Clinical-management statements are, by necessity, extrapolated from the component phenotypes, as no disease-specific guidelines or trials exist. Where information is unavailable it is explicitly flagged.

---

## Summary

Achalasia-progeroid syndrome (ACHPS) is an ultra-rare, autosomal-recessive, multisystem Mendelian disorder caused by biallelic loss-of-function variants in **BUD13**, a subunit of the spliceosomal **RES (REtention and Splicing) complex**. The disease was defined in 2022 by Kornak and colleagues, who identified five affected individuals — all carrying an identical homozygous nonsense variant, **NM_032725.4:c.688C>T, p.(Arg230Ter)** — through exome sequencing ([PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)). The clinical phenotype combines childhood-onset generalized lipodystrophy with a progeroid (prematurely aged) facial appearance, achalasia (failure of the lower esophageal sphincter to relax), corneal clouding, cataracts, retinal dystrophy, progressive sensorineural hearing loss, demyelinating sensory neuropathy, and cardiac-valve regurgitation. In a severe subset, microcephaly, intellectual disability and death within the first decade of life also occur.

Mechanistically, BUD13 deficiency impairs pre-mRNA splicing. Patient-derived dermal fibroblasts show elevated intron retention, a global reduction of spliceosomal proteins, and nuclei with multiple nuclear-envelope invaginations. A striking feature is that the c.688C>T nonsense substitution does not simply trigger complete nonsense-mediated decay; instead it drives alternative splicing that produces a stable, truncated, **hypomorphic** BUD13 protein. The amount of this residual hypomorphic isoform positively correlates with milder disease and longer survival, explaining the strikingly **bimodal severity** observed across the five patients (three severe childhood-lethal cases versus two mildly affected adults with normal intellect).

There is no curative or gene-targeted therapy; management is entirely supportive and organ-directed (e.g., myotomy or pneumatic dilation for achalasia, cataract surgery, hearing aids, lipid-lowering therapy, cardiac surveillance). The disease is evolutionarily instructive: the RES complex is conserved from yeast through plants and zebrafish to humans, and **zebrafish bud13/RES-complex loss-of-function mutants** recapitulate a developmental neural phenotype, serving as the principal animal model. Because only five individuals have ever been reported, there are no population prevalence estimates, no registered clinical trials, and no Orphanet/ICD/MeSH codes assigned as of 2026.

---

## Section 1 — Disease Information

**Overview.** ACHPS is a **spliceosomopathy** — a disorder of the pre-mRNA splicing machinery — presenting as a developmental disorder with lipodystrophy and progeroid features. It is defined by the combination of generalized lipodystrophy, a characteristic facial gestalt, and achalasia, together with sensory (ophthalmologic and auditory) and neurological involvement.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #621123 |
| MONDO | MONDO:0700300 |
| MedGen | C6012702 (UID 1876522) |
| GARD | 0027387 |
| UMLS | C6012702 |
| Gene (HGNC) | *BUD13*, HGNC:28199 |
| Gene (NCBI) | 84811 |
| Ensembl | ENSG00000137656 |
| Orphanet / ICD-10 / ICD-11 / MeSH | No dedicated code assigned as of 2026 |

**Synonyms / alternative names.** Achalasia-progeroid syndrome; developmental disorder with lipodystrophy and progeroid features; BUD13-related lipodystrophy syndrome. The gene alias "ACHPS" is listed for *BUD13*.

**Source of information.** The disease-level knowledge is derived almost entirely from a single aggregated primary study (Kornak et al. 2022) describing five individuals, supplemented by aggregated ontology/database resources (OMIM, MedGen, ClinVar, UniProt, GO). It is therefore based on a small individual-patient case series rather than large EHR cohorts.

---

## Section 2 — Etiology

**Primary cause (genetic).** ACHPS is a monogenic autosomal-recessive disorder. The cause is biallelic loss-of-function of *BUD13*. In the defining cohort, every affected individual carried the **identical homozygous nonsense variant** p.(Arg230Ter):

> *"All individuals harbored an identical homozygous nonsense variant affecting the retention and splicing complex component BUD13."* — [PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)

**Genetic risk factors.** The single causal determinant is homozygosity (or presumptively compound heterozygosity) for pathogenic *BUD13* loss-of-function alleles. The recurrence of one identical allele across all reported families is consistent with a **founder effect and/or consanguinity**. No susceptibility loci or validated modifier genes outside *BUD13* itself have been established.

**Environmental risk factors.** None identified. As a Mendelian disorder, environmental exposures are not causal. The only non-genetic contributors to outcome are supportive-care access and surgical management of complications.

**Protective factors.** No external protective factors are known. The key *intrinsic* modifier is molecular: the degree of residual **hypomorphic truncated BUD13 protein** produced by alternative splicing of the mutant allele acts as an endogenous protective modifier — higher residual activity correlates with milder disease and longer survival.

**Gene–environment interactions.** None demonstrated; the disorder is essentially fully genetically determined with an intrinsic (splicing-level) severity modifier rather than an environmental one.

---

## Section 3 — Phenotypes

ACHPS is a multisystem disorder. The MedGen clinical synopsis encodes **26 HPO features**. Core features are summarized below with suggested HPO terms. The defining cohort reported variable severity, and some frequencies derive from the small n=5 series (so are qualitative).

> *"We identified a lipodystrophy phenotype with a typical facial appearance, corneal clouding, achalasia, progressive hearing loss, and variable severity."* — [PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)

| Phenotype | HPO term | Type | Notes |
|---|---|---|---|
| Generalized lipodystrophy | HP:0009064 | Physical manifestation | Childhood-onset; core feature |
| Excessive wrinkled skin | HP:0007392 | Physical manifestation | Progeroid appearance |
| Dry skin | HP:0000958 | Physical manifestation | — |
| Achalasia | HP:0002571 | Clinical sign | Esophageal dysmotility |
| Corneal opacity (clouding) | HP:0007957 | Clinical sign | — |
| Cataract | HP:0000518 | Clinical sign | — |
| Retinal dystrophy | HP:0000556 | Clinical sign | — |
| Sensorineural hearing loss | HP:0000407 | Clinical sign | Progressive |
| Demyelinating sensory neuropathy | HP:0011402 | Clinical sign / lab | — |
| Hypotonia | HP:0001252 | Clinical sign | — |
| Intellectual disability | HP:0001249 | Behavioral/cognitive | Severe subset |
| Microcephaly | HP:0000252 | Physical manifestation | Severe subset |
| Short stature | HP:0004322 | Physical manifestation | — |
| Failure to thrive | HP:0001508 | Clinical sign | — |
| Feeding difficulties | HP:0011968 | Clinical sign | Related to achalasia |
| Triangular face | HP:0000325 | Physical manifestation | Facial gestalt |
| Broad forehead | HP:0000337 | Physical manifestation | Facial gestalt |
| Midface retrusion | HP:0011800 | Physical manifestation | Facial gestalt |
| Deeply set eye | HP:0000490 | Physical manifestation | Facial gestalt |
| Hypercholesterolemia | HP:0003124 | Laboratory abnormality | — |
| Abnormal circulating lipid concentration | HP:0003119 | Laboratory abnormality | — |
| Aortic regurgitation | HP:0001659 | Clinical sign | — |
| Mitral regurgitation | HP:0001653 | Clinical sign | — |
| Thickened aortic valve cusp | HP:0031568 | Clinical sign | — |
| Joint contracture | HP:0034392 | Physical manifestation | — |
| Short phalanx of finger | HP:0009803 | Physical manifestation | — |

**Phenotype characteristics.**
- **Age of onset:** Childhood (some features congenital/infantile). Lipodystrophy and facial features appear early; hearing loss is progressive.
- **Severity:** Variable/bimodal. In Kornak 2022 (n=5), three individuals (A1–A3) were severe and two (A4–A5) were mild.
- **Progression:** Progressive for several features (hearing loss, neuropathy); multisystem accrual over time.
- **Frequency:** From n=5 — severe phenotype in 3/5; adult survival with normal intellect in 2/5.

> *"3 individuals showed stunted growth, intellectual disability, and died within the first decade of life (A1, A2, and A3), 2 are adults with normal intellectual development (A4 and A5)"* — [PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)

**Quality-of-life impact.** Severe multisystem burden: feeding difficulties and achalasia impair nutrition; hearing and visual loss impair communication and independence; neuropathy and contractures impair mobility; in the severe subset, intellectual disability and early death are profound. No formal EQ-5D/SF-36 data exist for this ultra-rare disease.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *BUD13* (HGNC:28199; NCBI Gene 84811; Ensembl ENSG00000137656), located at **11q23.3**. Gene aliases: *ACHPS*, *Cwc26*, *fSAP71*. Protein: UniProt Q9BRD0, a **619-amino-acid** subunit of the spliceosomal RES complex.

**Pathogenic variants.**

| Attribute | Detail |
|---|---|
| Defining variant | NM_032725.4:c.688C>T, **p.(Arg230Ter)** |
| ClinVar classification | Pathogenic (condition: Achalasia-progeroid syndrome) |
| Variant type | Nonsense (stop-gain) |
| Zygosity / origin | Homozygous, germline (recurrent allele) |
| Second listed variant | c.1693C>T p.(Arg565Cys) — conflicting classifications |
| Functional consequence | Loss of function converted to a **hypomorph** via alternative splicing |

**Population allele frequency and constraint.** *BUD13* loss-of-function alleles are rare in gnomAD. Importantly, gnomAD constraint metrics show *BUD13* is **not** haploinsufficient: pLI ≈ 0 (1.6e-12); LoF observed/expected = 0.75 (90% CI 0.60–0.96); LoF Z = 1.66. This LoF tolerance is fully consistent with healthy heterozygous carriers and an **autosomal-recessive** disease mechanism.

**Functional consequence — the splicing paradox.** Rather than triggering complete nonsense-mediated decay, the p.Arg230Ter allele promotes alternative splicing that yields a stable, truncated, partially functional protein:

> *"The nucleotide substitution caused alternative splicing of BUD13 leading to a stable truncated protein whose expression positively correlated with disease expression and life expectancy."* — [PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)

**Modifier genes.** No external modifier genes identified. The principal modifier is intrinsic — the quantity of the hypomorphic BUD13 isoform.

**Epigenetic information.** No disease-specific DNA-methylation or histone-modification data are available for ACHPS.

**Chromosomal abnormalities.** None; ACHPS is a single-nucleotide (nonsense) disorder, not a structural/aneuploidy syndrome.

---

## Section 5 — Environmental Information

- **Environmental factors:** None causal or contributory (monogenic disorder).
- **Lifestyle factors:** Not applicable to causation. Nutritional support is relevant to management but not etiology.
- **Infectious agents:** None. ACHPS is not infectious or trigger-associated.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic nonsense variant** *BUD13* c.688C>T p.(Arg230Ter) **→ leads to** loss of full-length BUD13 protein.
2. Loss of BUD13 **→ results in** a deficient/destabilized spliceosomal **RES complex** (BUD13–SNIP1/Pml1–RBMX2/Snu17) and **global reduction of spliceosomal proteins** (demonstrated in patient fibroblasts).
3. Impaired RES-complex function **→ leads to** defective pre-mRNA splicing, manifesting as **elevated intron retention** across many transcripts (demonstrated).
4. **Branch (severity modifier):** The mutant allele is **alternatively spliced** to a stable, truncated **hypomorphic** protein. *More* residual hypomorph **→ results in** milder disease / longer survival; *less* **→ results in** the severe, childhood-lethal phenotype (demonstrated: expression correlates with life expectancy).
5. Widespread mis-splicing/intron retention **→ leads to** altered expression of many downstream genes and **nuclear-envelope abnormalities** (nuclei with multiple invaginations; demonstrated, more pronounced in severe cases A1–A3).
6. Disrupted gene expression across tissues **→ results in** the multisystem clinical phenotype — adipose (lipodystrophy), esophageal/enteric (achalasia), ocular (corneal clouding, cataract, retinal dystrophy), auditory (sensorineural hearing loss), peripheral nerve (demyelinating neuropathy), cardiac valves (regurgitation), brain (microcephaly, intellectual disability in severe subset), and skin (progeroid wrinkling) — *inferred* tissue-level consequences of the global splicing defect.
7. Rescue evidence: **overexpression of BUD13 isoforms normalized nuclear morphology** in patient cells (demonstrated), confirming BUD13 loss as the proximal driver.

```
 BUD13 c.688C>T p.(Arg230Ter)  [homozygous, germline]
              │ loss of full-length BUD13
              ▼
   Deficient RES complex  ──►  global ↓ spliceosomal proteins
              │
              ▼
   Defective pre-mRNA splicing ──► INTRON RETENTION (many genes)
              │                                   │
              │                                   ▼
   (BRANCH) alt. splicing of mutant      nuclear-envelope invaginations
   allele → stable truncated HYPOMORPH            │
              │  more hypomorph = milder          ▼
              ▼                           multisystem dysfunction
   severity / survival set here   ──►  lipodystrophy, achalasia, corneal
                                       clouding, cataract, retinal dystrophy,
                                       hearing loss, neuropathy, valve disease,
                                       microcephaly/ID (severe subset)
```

### Supporting mechanistic detail

> *"In dermal fibroblasts, we found elevated intron retention, a global reduction of spliceosomal proteins, and nuclei with multiple invaginations, which were more pronounced in A1, A2, and A3."* — [PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)

> *"the alternative splice product converts a loss-of-function into a hypomorphic allele, thereby probably determining the sev[erity]..."* — [PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)

**Molecular pathways / cellular processes.** The core lesion is in **mRNA splicing via the spliceosome (GO:0000398)** and **U2-type prespliceosome assembly (GO:1903241)**. BUD13 functions in **RNA binding (GO:0003723)**. Downstream cellular processes (apoptosis/cell death, impaired neuronal differentiation) are inferred from the zebrafish model (see Section 15).

**Protein dysfunction.** BUD13 (UniProt Q9BRD0, 619 aa) is a RES-complex subunit; the truncating variant produces either loss of function (full NMD scenario) or a shortened hypomorph. RES is a heterotrimer with SNIP1 (Pml1) and RBMX2 (Snu17).

> *"The retention and splicing (RES) complex is formed by three different proteins (Bud13p, Pml1p and Snu17p) and is involved in splicing in yeast."* — [PMID: 29969449](https://pubmed.ncbi.nlm.nih.gov/29969449/)

**Metabolic changes.** Secondary dyslipidemia (hypercholesterolemia; abnormal circulating lipids) accompanies the generalized lipodystrophy — a downstream metabolic consequence rather than a primary enzymatic defect.

**Subcellular localization.** Nucleus/nucleoplasm (GO:0005634 / GO:0005654); spliceosomal complex (GO:0005681); RES complex (GO:0070274); U2-type precatalytic spliceosome (GO:0071005); U2 snRNP (GO:0005686); also the minor/U12-type spliceosome (GO:0071018), indicating BUD13 participates in both major and minor splicing.

**GO / CL term suggestions.** Biological process: GO:0000398 (mRNA splicing, via spliceosome), GO:1903241 (U2-type prespliceosome assembly). Cellular component: GO:0070274 (RES complex), GO:0005681 (spliceosomal complex). Cell types involved: CL:0000136 (adipocyte), CL:0000057 (fibroblast — the in vitro model cell), CL:0002573 (Schwann cell — neuropathy), photoreceptor and enteric neuron populations (inferred).

---

## Section 7 — Anatomical Structures Affected

**Organ / system level (digestive, nervous, sensory, cardiovascular, integumentary, adipose, skeletal, craniofacial):**

| Structure | UBERON (suggested) | Manifestation |
|---|---|---|
| Adipose tissue | UBERON:0001013 | Generalized lipodystrophy |
| Esophagus / lower esophageal sphincter | UBERON:0001043 / UBERON:0004550 | Achalasia |
| Cornea | UBERON:0000964 | Corneal clouding |
| Lens | UBERON:0000965 | Cataract |
| Retina | UBERON:0000966 | Retinal dystrophy |
| Inner ear / cochlea | UBERON:0001844 | Sensorineural hearing loss |
| Peripheral nerve | UBERON:0001021 | Demyelinating sensory neuropathy |
| Aortic valve | UBERON:0002137 | Aortic regurgitation / thickened cusp |
| Mitral valve | UBERON:0002134 | Mitral regurgitation |
| Brain | UBERON:0000955 | Microcephaly, intellectual disability (severe subset) |
| Skin | UBERON:0002097 | Wrinkled, dry (progeroid) skin |

**Tissue / cell level.** Adipocytes (CL:0000136); Schwann cells (CL:0002573, demyelinating neuropathy); photoreceptors and enteric neurons (inferred); dermal fibroblasts (CL:0000057) are the principal in vitro model cell.

**Subcellular level.** Nucleus / nucleoplasm (GO:0005634 / GO:0005654) and the spliceosome / RES complex (GO:0005681 / GO:0070274). Patient fibroblasts characteristically show **nuclear-envelope invaginations**.

**Lateralization.** Involvement is systemic and bilateral/symmetric (e.g., bilateral ocular and auditory involvement).

---

## Section 8 — Temporal Development

- **Onset:** Childhood (some features congenital/infantile) — insidious, chronic onset of a developmental disorder.
- **Progression:** Progressive and multisystem; features such as sensorineural hearing loss are explicitly progressive.
- **Disease course:** Chronic, lifelong. Bimodal trajectory — severe cases decline and die within the first decade; mild cases survive into adulthood.
- **Critical period / intervention window:** Early development (as suggested by the zebrafish model showing RES requirement during early embryogenesis). The severity-setting step (amount of hypomorphic isoform) is fixed at the molecular level, implying any splice-modulating intervention would ideally act early.
- **Remission:** None; no spontaneous or treatment-induced remission of the underlying disorder.

---

## Section 9 — Inheritance and Population

**Epidemiology.** Ultra-rare. Only **5 affected individuals** have been reported worldwide (the Kornak 2022 defining cohort). No prevalence or incidence estimates exist.

**Inheritance.** Autosomal recessive (OMIM #621123; MONDO:0700300).

- **Penetrance:** Appears complete in biallelic carriers.
- **Expressivity:** Variable/bimodal, determined by the amount of hypomorphic truncated BUD13 isoform.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effect / consanguinity:** Strongly suggested — all reported cases carry one identical recurrent homozygous allele.
- **Carrier frequency:** Unknown; *BUD13* LoF alleles are rare in gnomAD, and heterozygotes are healthy (gene is LoF-tolerant).

> *"All individuals harbored an identical homozygous nonsense variant affecting the retention and splicing complex component BUD13."* — [PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)

**Population demographics.** No established ethnic predilection beyond the founder allele; geographic distribution unknown; sex ratio not established (n too small); age distribution spans affected children (severe) and adults (mild).

**Note on common *BUD13* variation.** Common non-coding variants at the *APOA1/C3/A4/A5–ZPR1–BUD13* locus are associated with cardiometabolic (lipid) and cognitive traits in GWAS (e.g., [PMID: 40665476](https://pubmed.ncbi.nlm.nih.gov/40665476/)). These are **distinct** from the rare biallelic coding LoF variants that cause ACHPS, but are mechanistically interesting given the lipid/dyslipidemia component of the syndrome.

---

## Section 10 — Diagnostics

**Primary diagnostic approach — molecular.** Diagnosis is established by identifying **biallelic pathogenic *BUD13* variants** via **whole-exome sequencing** (the method used in Kornak 2022) or whole-genome sequencing. Once ACHPS is suspected clinically, single-gene or targeted-panel testing for *BUD13* is appropriate. Chromosomal microarray, karyotyping, FISH, mtDNA and repeat-expansion testing are **not** indicated (not a structural/mitochondrial/repeat disorder).

**Organ-directed workup (mapped to phenotype):**

| Test | Target phenotype (HPO) |
|---|---|
| Esophageal manometry + barium swallow | Achalasia (HP:0002571) |
| Slit-lamp / ophthalmology exam | Corneal clouding (HP:0007957), cataract (HP:0000518), retinal dystrophy (HP:0000556) |
| Audiometry | Sensorineural hearing loss (HP:0000407) |
| Nerve conduction studies | Demyelinating sensory neuropathy (HP:0011402) |
| Echocardiography | Aortic/mitral regurgitation (HP:0001659 / HP:0001653) |
| Fasting lipid panel | Hypercholesterolemia (HP:0003124) |

**Research-grade / omics diagnostics.** Dermal-fibroblast RNA-seq demonstrating intron retention; proteomics showing reduced spliceosomal proteins; electron microscopy showing nuclear-envelope invaginations. These are confirmatory functional assays rather than routine clinical tests.

**Differential diagnosis** — other congenital generalized lipodystrophy / progeroid disorders that can include achalasia:

| Differential | Gene | Supporting evidence |
|---|---|---|
| CGL3 | *CAV1* | Achalasia reported ([PMID: 34643546](https://pubmed.ncbi.nlm.nih.gov/34643546/)) |
| CGL4 | *CAVIN1/PTRF* | Achalasia reported ([PMID: 40718185](https://pubmed.ncbi.nlm.nih.gov/40718185/)) |
| MDPL | *POLD1* | Progeroid lipodystrophy ([PMID: 40718185](https://pubmed.ncbi.nlm.nih.gov/40718185/)) |
| Berardinelli–Seip (CGL1/2) | *AGPAT2*, *BSCL2* | Generalized lipodystrophy |
| Mandibuloacral dysplasia | *LMNA*, *ZMPSTE24* | Progeroid + lipodystrophy |

> *"Two patients also presented at the age of 15 and 18 years with dysphagia due to achalasia"* — [PMID: 34643546](https://pubmed.ncbi.nlm.nih.gov/34643546/) (CAV1/CGL3)

> *"delayed puberty and achalasia cardia in the latter case"* — [PMID: 40718185](https://pubmed.ncbi.nlm.nih.gov/40718185/) (CAVIN1/CGL4)

**Screening.** No newborn or population carrier screening exists. Within affected families, **cascade carrier testing** and targeted testing for the familial *BUD13* allele are appropriate.

---

## Section 11 — Outcome / Prognosis

**Survival / mortality.** Bimodal. In the defining cohort (n=5): three severe individuals (A1–A3) had stunted growth and intellectual disability and **died within the first decade**; two (A4–A5) are living adults with normal intellect.

**Prognostic biomarker.** The single most important prognostic determinant is molecular — the **expression level of the hypomorphic truncated BUD13 splice isoform**, which positively correlates with milder disease and longer life expectancy:

> *"the alternative splice product converts a loss-of-function into a hypomorphic allele, thereby probably determining the severity of the disease and the survival of affected individuals."* — [PMID: 35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/)

**Morbidity.** High across all survivors: feeding difficulty/failure to thrive, visual and auditory impairment, neuropathy, joint contractures, cardiac-valve disease, and dyslipidemia. No standardized QoL instruments have been applied.

**Complications.** Nutritional compromise (achalasia/feeding difficulty), aspiration risk, progressive sensory loss, cardiac valve dysfunction.

**Recovery potential.** None at the disease level; supportive interventions mitigate individual complications but do not reverse the disorder.

---

## Section 12 — Treatment

**No curative or gene-targeted therapy exists.** Management is **supportive and organ-directed**. No clinical trials are registered (ultra-rare).

| Problem (HPO) | Intervention | Suggested NCIT concept |
|---|---|---|
| Achalasia (HP:0002571) | Laparoscopic Heller myotomy; per-oral endoscopic myotomy (POEM); pneumatic balloon dilation; botulinum toxin injection | Esophagomyotomy; Esophageal Dilation |
| Feeding difficulty / FTT (HP:0011968 / HP:0001508) | Nutritional support; gastrostomy | Nutritional Support; Gastrostomy |
| Cataract (HP:0000518) | Cataract extraction | Cataract Surgery |
| Corneal clouding (HP:0007957) | Ophthalmologic management | — |
| Sensorineural hearing loss (HP:0000407) | Hearing aids; cochlear implant | Cochlear Implantation |
| Hypercholesterolemia (HP:0003124) | Lipid-lowering diet; statins | Statin Therapy |
| Valve regurgitation (HP:0001659 / HP:0001653) | Cardiology surveillance; valve repair if indicated | — |
| Neuropathy / contractures | Physical therapy, occupational therapy | Physical Therapy |

**Pharmacogenomics / advanced therapeutics.** None established. The disease biology, however, points toward a rational experimental strategy: because residual hypomorphic BUD13 is protective, **splice-modulating therapy** (e.g., antisense oligonucleotides to bias splicing toward functional isoform, or read-through/stabilization approaches) is a biologically motivated but entirely hypothetical future direction.

---

## Section 13 — Prevention

- **Primary prevention:** Not possible at the population level (monogenic, non-environmental). **Genetic counseling** for at-risk/consanguineous families is the principal preventive tool.
- **Reproductive options:** For couples with a known familial *BUD13* allele, carrier testing, prenatal diagnosis, and preimplantation genetic testing (PGT-M) are applicable.
- **Secondary prevention:** Early multidisciplinary surveillance (ophthalmology, audiology, cardiology, nutrition) to detect and manage complications promptly.
- **Tertiary prevention:** Organ-directed management to prevent complications (e.g., nutritional support to prevent aspiration/failure to thrive; valve surveillance).
- **Immunization / public-health / environmental interventions:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy of relevant models:** Zebrafish (*Danio rerio*, NCBI Taxon 7955); *Saccharomyces cerevisiae* (yeast); *Arabidopsis thaliana* (plant).
- **Orthologous genes / complex:** The RES complex is **evolutionarily conserved** — yeast Bud13/Snu17/Pml1; Arabidopsis AtBUD13/GDS1/DDL; zebrafish bud13/rbmx2/snip1; human BUD13/RBMX2/SNIP1.

> *"The heterotrimeric retention and splicing (RES) complex plays vital roles in the growth and development of yeast, zebrafish, and humans by mediating pre-mRNA splicing of multiple genes."* — [PMID: 35640107](https://pubmed.ncbi.nlm.nih.gov/35640107/)

- **Naturally occurring disease in companion animals / wildlife:** No naturally occurring *BUD13*-related disease reported in OMIA for other species.
- **Comparative biology / conservation:** Deep conservation of the RES complex mechanism underscores that the splicing function is ancient and essential; the same molecular defect produces developmental phenotypes across phyla.
- **Zoonotic potential:** Not applicable (non-infectious genetic disorder).

---

## Section 15 — Model Organisms

**Zebrafish (principal disease model).** Fernandez et al. 2018 generated loss-of-function mutants for all three RES-complex components (*bud13*, *snip1/pml1*, *rbmx2/snu17*), demonstrating they are required during early development and produce a **marked neural phenotype** with increased brain cell death and reduced differentiated neurons, alongside global intron-splicing defects:

> *"we have generated loss-of-function mutants for the three components of the RES complex in zebrafish and showed that they are required during early development. The mutants showed a marked neural phenotype with increased cell death in the brain and a decrease in differentiated neurons"* — [PMID: 29969449](https://pubmed.ncbi.nlm.nih.gov/29969449/)

RES-dependent introns were found to be short, GC-rich, and intron-defined — consistent with the intron-retention phenotype seen in human ACHPS fibroblasts.

**Other systems.**
- **Yeast (*S. cerevisiae*):** Defines the minimal RES heterotrimer (Bud13p/Snu17p/Pml1p); foundational for mechanism.
- **Arabidopsis:** AtBUD13/GDS1/DDL RES orthologs regulate embryo and root development through splicing ([PMID: 35640107](https://pubmed.ncbi.nlm.nih.gov/35640107/)).
- **In vitro:** Patient-derived dermal fibroblasts (CL:0000057) are the key cellular model, reproducing intron retention, spliceosomal-protein reduction, and nuclear invaginations; rescue by BUD13 overexpression confirms causality.

**Model characteristics.**
- *Phenotype recapitulation:* Zebrafish captures the neurodevelopmental/CNS aspect (brain cell death, neuronal deficit) and the molecular splicing defect well; patient fibroblasts recapitulate the cellular/nuclear phenotype.
- *Limitations:* No reported mammalian (mouse) model of the specific hypomorphic human allele; zebrafish does not reproduce the full multisystem human gestalt (lipodystrophy, achalasia, progeroid features). A knock-in of the hypomorphic p.Arg230Ter allele would be needed to model the bimodal severity.

**Resources:** ZFIN (zebrafish), SGD (yeast), TAIR (Arabidopsis).

---

## Mechanistic Model / Interpretation

ACHPS is best understood as a **dosage-sensitive spliceosomopathy with a built-in severity rheostat.** A single recurrent homozygous nonsense allele in *BUD13* would, at face value, be predicted to abolish protein via nonsense-mediated decay. Instead, the exact position of the premature stop codon triggers alternative splicing that salvages a stable, truncated, partially functional protein. The quantity of this salvaged hypomorph behaves like a dial: more residual BUD13 activity keeps splicing fidelity high enough for survival into adulthood with preserved cognition; less tips the system into severe global intron retention, spliceosome collapse, nuclear-envelope distortion, developmental failure, and death in the first decade. This elegantly explains how an **identical genotype** produces a **bimodal phenotype** — the variation is epi-transcriptomic (splicing-level), not a second genetic hit.

The downstream tissue pattern (adipose, esophagus, eye, ear, nerve, heart valve, brain, skin) reflects the broad reach of a general splicing defect combined with tissue-specific vulnerability. The convergence with other lipodystrophy-with-achalasia syndromes (CAV1, CAVIN1, POLD1) at the clinical level — despite distinct molecular causes — suggests shared downstream pathways affecting adipocyte biology and esophageal/enteric neuromuscular function that merit cross-disorder study.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [35670808](https://pubmed.ncbi.nlm.nih.gov/35670808/) | *Alternative splicing of BUD13 determines the severity of a developmental disorder with lipodystrophy and progeroid features* | **Defining study.** Establishes causal gene, recurrent homozygous nonsense allele, multisystem phenotype, bimodal severity, splicing mechanism (intron retention, spliceosomal-protein loss, nuclear invaginations), and hypomorphic-isoform prognostic model |
| [29969449](https://pubmed.ncbi.nlm.nih.gov/29969449/) | *RES complex is associated with intron definition and required for zebrafish early embryogenesis* | Defines RES heterotrimer; principal **zebrafish model** with neural phenotype and intron-splicing defects |
| [35640107](https://pubmed.ncbi.nlm.nih.gov/35640107/) | *An Arabidopsis Retention and Splicing complex regulates root and embryo development* | Establishes **evolutionary conservation** of RES across yeast, zebrafish, humans, plants |
| [34643546](https://pubmed.ncbi.nlm.nih.gov/34643546/) | *Biallelic CAV1 null variants induce congenital generalized lipodystrophy with achalasia* | Key **differential diagnosis** (CGL3); documents achalasia in CAV1 lipodystrophy |
| [40718185](https://pubmed.ncbi.nlm.nih.gov/40718185/) | *Inherited Lipodystrophy Associated With POLD1 and CAVIN1 Mutations* | **Differential diagnoses** (CGL4, MDPL); achalasia in CAVIN1 lipodystrophy |
| [40665476](https://pubmed.ncbi.nlm.nih.gov/40665476/) | *Genome-wide study links cardiometabolic factors to cognition via APOA4-APOA5-ZPR1-BUD13...* | Context: common *BUD13*-locus variants and lipid/cognition traits (distinct from ACHPS coding LoF) |

**Evidence source types.** Human clinical/genetic: PMID 35670808 (n=5 case series + functional fibroblast studies), 34643546, 40718185. Model organism / in vitro: PMID 29969449 (zebrafish), 35640107 (Arabidopsis). Population genetics / computational: gnomAD constraint metrics, ClinVar classification, PMID 40665476 (GWAS).

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base (n=5).** All clinical knowledge derives from one cohort sharing a single recurrent allele. Phenotype frequencies, full spectrum, and penetrance/expressivity estimates are provisional.
2. **No epidemiology.** Prevalence, incidence, carrier frequency, geographic distribution, and sex ratio are all unknown.
3. **Single allele characterized.** Mechanism is defined for p.Arg230Ter only; whether other *BUD13* variants (e.g., the conflicting p.Arg565Cys) cause disease, and whether they produce the same hypomorphic-rescue behavior, is unestablished.
4. **No mammalian model of the human allele.** The zebrafish model captures CNS/splicing biology but not the full multisystem human phenotype (lipodystrophy, achalasia, progeroid features).
5. **No therapeutics or trials.** Management is supportive; splice-modulation is only a theoretical opportunity.
6. **Missing tissue-level mechanism.** Why specific tissues (esophagus, adipose, cornea) are vulnerable to a global splicing defect is not mechanistically resolved; the causal chain from mis-splicing to each organ phenotype is largely inferred.
7. **No epigenetic, metabolomic, or single-cell data** specific to ACHPS exist.
8. **No official Orphanet/ICD/MeSH codes** as of 2026, which limits registry-based ascertainment.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient registry via GeneMatcher/Matchmaker Exchange** to identify additional *BUD13* cases, define the full phenotype spectrum, establish frequencies, and test whether the founder allele is population-specific.
2. **Generate a knock-in mouse** carrying the hypomorphic p.Arg230Ter allele to model bimodal severity and the multisystem phenotype, and to quantify the hypomorph-dose/severity relationship in vivo.
3. **Characterize the hypomorphic isoform quantitatively** (patient fibroblast panels, RNA-seq + proteomics) to validate residual BUD13 level as a clinical prognostic biomarker, enabling genotype-independent severity prediction at diagnosis.
4. **Test splice-modulating ASOs** in patient fibroblasts to bias splicing toward the functional/hypomorphic isoform — a proof-of-concept for the rational therapeutic strategy implied by the disease biology.
5. **Map tissue-specific mis-splicing** (single-cell/organoid RNA-seq across adipose, esophageal/enteric, ocular, auditory lineages) to connect the global splicing defect to each organ phenotype.
6. **Functionally classify the conflicting c.1693C>T p.(Arg565Cys) variant** to clarify the ACHPS allelic series.
7. **Pursue formal disease-ontology coding** (Orphanet, ICD-11) to improve case ascertainment and knowledge-base integration.


## Artifacts

- [OpenScientist final report](Achalasia-progeroid_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Achalasia-progeroid_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 53 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 44 |
| Terms named correctly | 37 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0700300` (3 mentions) - the report calls it "MONDO"; MONDO calls it **achalasia-progeroid syndrome**
- `CL:0000057` (3 mentions) - the report calls it "fibroblast — the in vitro model cell"; CL calls it **fibroblast**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007957` (3 mentions) - the report calls it "Corneal opacity (clouding)", "Corneal clouding"; HP calls it **Corneal opacity**, and lists "Corneal clouding" among its other names
- `CL:0002573` (2 mentions) - the report calls it "Schwann cell — neuropathy"; CL calls it **Schwann cell**
- `UBERON:0001844` (1 mention) - the report calls it "Inner ear / cochlea"; UBERON calls it **cochlea**
- `UBERON:0002134` (1 mention) - the report calls it "Mitral valve"; UBERON calls it **tricuspid valve**
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0007957` - called "Corneal opacity (clouding)", "Corneal clouding"