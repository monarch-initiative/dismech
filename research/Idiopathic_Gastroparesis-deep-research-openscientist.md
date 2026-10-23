---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T19:29:18.606669'
end_time: '2026-09-30T19:46:07.927489'
duration_seconds: 1009.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Idiopathic Gastroparesis
  mondo_id: MONDO:0034150
  category: Complex
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
citation_count: 30
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 32
  on_topic: 24
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 25
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 6
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0006909
    reported_labels:
    - muscularis propria/externa
    ontology_label: lumen of digestive tract
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Idiopathic_Gastroparesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Idiopathic_Gastroparesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Idiopathic Gastroparesis
- **MONDO ID:** MONDO:0034150 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Gastroparesis** covering all of the
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

# Idiopathic Gastroparesis: A Comprehensive Disease Characteristics Report

**Disease:** Idiopathic Gastroparesis (IGP)
**MONDO ID:** MONDO:0034150 · **ICD-10:** K31.84 · **MeSH:** D018589 (Gastroparesis)
**Category:** Complex / multifactorial gastric neuromuscular (sensorimotor) disorder
**Report type:** Multi-iteration literature synthesis (12 confirmed findings, 52 papers reviewed)

---

## Summary

Idiopathic gastroparesis (IGP) is a chronic, female-predominant gastric neuromuscular disorder defined by the presence of upper-gastrointestinal symptoms — cardinally **nausea and vomiting**, frequently accompanied by early satiation, postprandial fullness, bloating, and abdominal pain — in the setting of **objectively delayed gastric emptying without mechanical obstruction** and after exclusion of secondary causes (diabetic, post-surgical, medication-induced, connective-tissue, neurological). It is the single largest etiologic category of gastroparesis, accounting for roughly 58% of cases in tertiary series. The authoritative 2025 Rome Foundation/international consensus ([PMID: 39674226](https://pubmed.ncbi.nlm.nih.gov/39674226/)) codified this definition and requires demonstration of delayed emptying by 4-hour scintigraphy or gastric emptying breath test of a mixed-composition meal.

The hallmark cellular lesion, established through full-thickness gastric biopsy studies from the NIDDK Gastroparesis Clinical Research Consortium, is **loss of interstitial cells of Cajal (ICC)** — the pacemaker cells that generate gastric slow waves — accompanied by **depletion of anti-inflammatory CD206+ (M2) muscularis macrophages** and downregulation of smooth-muscle contractile genes. Animal-model evidence (largely diabetic but mechanistically shared) knits these observations into a coherent causal axis: loss of cytoprotective, **heme oxygenase-1 (HO-1)–expressing M2 macrophages** permits unchecked **oxidative stress**, which destroys ICC and **nitrergic (nNOS) enteric neurons**, degrading slow-wave activity, gastric accommodation, and antropyloric coordination — the functional substrate of delayed emptying. Macrophage-deficient mice are protected from the lesion, and HO-1/IL-10 induction reverses it, demonstrating that the macrophage–HO-1–oxidative-stress module is both necessary and sufficient in models.

IGP is **multifactorial, not Mendelian**: there is no established causal gene, no OMIM entry, and no pathogenic-variant classification; the strongest molecular-genetic lead is the **SCN5A/NaV1.5** sodium-channelopathy, a candidate susceptibility factor expressed by ICC and smooth muscle. A recognized **post-infectious subgroup** follows acute viral illness and is often self-limiting, while the majority of cases run a chronic, fluctuating course. Management remains largely symptomatic and only modestly effective — metoclopramide (the sole FDA-approved agent, boxed warning for tardive dyskinesia) and erythromycin are conditionally recommended, with G-POEM, gastric electrical stimulation, and intrapyloric botulinum toxin reserved for refractory disease — and roughly one-third of patients remain refractory. The strong ~4:1 to ~9:1 female predominance is biologically underpinned by the physiologically slower gastric emptying of healthy women and the inhibitory effects of estrogen and progesterone on gastric motility.

---

## Key Findings

### 1. Disease Definition, Cardinal Symptoms, and Diagnostic Criteria (F001)

The 2025 Rome Foundation/international neurogastroenterology consensus defined IGP as *"the presence of symptoms associated with delayed gastric emptying in the absence of mechanical obstruction,"* with **nausea and vomiting** as cardinal symptoms and early satiation/postprandial fullness frequently co-existing ([PMID: 39674226](https://pubmed.ncbi.nlm.nih.gov/39674226/)). Diagnosis requires these symptoms *plus* delayed gastric emptying demonstrated on **4-hour scintigraphy or a gastric emptying breath test of a mixed-composition meal**. Idiopathic disease is the largest category of gastroparesis — **149 of 256 patients (58.2%)** in a 2023 tertiary series were idiopathic, versus 23.4% diabetic and 11.3% postsurgical ([PMID: 36730846](https://pubmed.ncbi.nlm.nih.gov/36730846/)).

**Key identifiers:** MONDO:0034150 · ICD-10 **K31.84** · MeSH **D018589** (Gastroparesis). There is no OMIM entry (IGP is not monogenic). **Synonyms/alternative names:** idiopathic delayed gastric emptying; idiopathic gastric stasis; the disorder is increasingly reconceptualized as a **gastric sensorimotor disorder** on a spectrum with functional dyspepsia. Information is drawn from both **aggregated disease-level resources** (consensus guidelines, registries) and **individual-patient sources** (full-thickness biopsy cohorts, EHR/registry studies).

### 2. Core Cellular Pathophysiology: ICC Loss and CD206+ (M2) Macrophage Depletion (F002)

Full-thickness gastric biopsy studies remain the decisive evidence. Grover et al. 2017 ([PMID: 28066953](https://pubmed.ncbi.nlm.nih.gov/28066953/)) quantified ICC in the antral muscularis: counts were reduced in idiopathic (**2.53/hpf**) and diabetic (**2.28/hpf**) gastroparesis versus controls (**6.05/hpf**), *P = 0.004*. Anti-inflammatory **CD206+ (M2) macrophages** were lost in circular muscle (IG 4.16 vs control 6.59, *P = 0.04*) and myenteric plexus (IG 3.59 vs control 7.46, *P = 0.004*), while overall CD45+ immune cell counts were unchanged — implying a **shift in macrophage phenotype**, not a global immune depletion. Bernard et al. 2014 ([PMID: 25041465](https://pubmed.ncbi.nlm.nih.gov/25041465/)) confirmed ICC loss in the gastric body and found CD206+ counts correlated with ICC counts. Herring et al. 2018 ([PMID: 29052298](https://pubmed.ncbi.nlm.nih.gov/29052298/)) showed decreased muscularis-externa mRNA for contractile and regulatory genes — **MYH11, MYLK1, PDGFRA, PDGFB, and HMOX1 (HO-1)** — in IG, with preserved KIT/ANO1.

> *"Both diabetic and idiopathic gastroparesis patients showed loss of ICC as compared to controls (Mean/hpf: diabetic, 2.28; idiopathic, 2.53; controls, 6.05; P=.004)."* — [PMID: 28066953](https://pubmed.ncbi.nlm.nih.gov/28066953/)

**Suggested ontology terms:** ICC (CL:0002088); M2/muscularis macrophage (CL:0000235); smooth muscle cell (CL:0000192); GO: *macrophage activation* (GO:0042116), *regulation of smooth muscle contraction* (GO:0006940).

### 3. Demographics and Clinical Features — NIDDK GpCRC Registry (F003)

Parkman et al. 2011 ([PMID: 20965184](https://pubmed.ncbi.nlm.nih.gov/20965184/)) characterized 243 IG patients: **mean age 41 years; 88% female; 46% overweight; 50% acute symptom onset; 19% reported an initial infectious prodrome** (the post-viral subset). Severe emptying delay (>35% retention at 4 h) occurred in 28%. Predominant presenting symptoms were nausea (34%), abdominal pain (23%), and vomiting (19%); women had more severe nausea, satiety, and constipation. Psychiatric comorbidity was prominent — **severe anxiety in 36% and depression in 18%** — and **86% met criteria for functional dyspepsia** (predominantly postprandial distress syndrome), underscoring the overlap with FD.

> *"The mean age of 243 patients with IG studied was 41 years; 88% were female, 46% were overweight, 50% had acute onset of symptoms, and 19% reported an initial infectious prodrome."* — [PMID: 20965184](https://pubmed.ncbi.nlm.nih.gov/20965184/)

### 4. Epidemiology and Strong Female Predominance (F004)

The Olmsted County, Minnesota population study (Jung et al. 2009, [PMID: 19249393](https://pubmed.ncbi.nlm.nih.gov/19249393/)) provides the foundational epidemiology:

| Metric (per 100,000) | Men | Women | Ratio |
|---|---|---|---|
| Age-adjusted **incidence** (per person-year) | 2.4 (95% CI 1.2–3.8) | 9.8 (7.5–12.1) | ~4:1 F:M |
| Age-adjusted **prevalence** (Jan 1, 2007) | 9.6 (1.8–17.4) | 37.8 (23.3–52.4) | ~4:1 F:M |

Overall diagnosed prevalence was **≈24.2/100,000** (Rey et al. 2012, [PMID: 22323986](https://pubmed.ncbi.nlm.nih.gov/22323986/)), and community modeling suggested up to **~1.8% of adults** may harbor undiagnosed ("hidden") delayed gastric emptying — the gastroparesis "iceberg." Overall survival in the Olmsted cohort was reduced relative to the age- and sex-matched expected population.

### 5. Treatment Landscape — AGA 2025 Guideline (F005)

The AGA Clinical Practice Guideline on Management of Gastroparesis (2025, [PMID: 40976635](https://pubmed.ncbi.nlm.nih.gov/40976635/)) issued 12 GRADE recommendations: **conditionally FOR metoclopramide and erythromycin**, and **AGAINST domperidone, prucalopride, aprepitant, nortriptyline, buspirone, and cannabidiol as first-line therapies**; it favored 4-hour over 2-hour scintigraphy. **Metoclopramide** (dopamine D2 antagonist / 5-HT4 agonist) is the **only FDA-approved drug** ([PMID: 28721575](https://pubmed.ncbi.nlm.nih.gov/28721575/)) and carries a boxed warning for **tardive dyskinesia**, with risk elevated by continuous dosing (0.77% continuous vs 0.55% intermittent in a gastroparesis cohort; [PMID: 42702756](https://pubmed.ncbi.nlm.nih.gov/42702756/)). Refractory options include **gastric electrical stimulation, intrapyloric botulinum toxin, and endoscopic pyloromyotomy (G-POEM)** ([PMID: 36970885](https://pubmed.ncbi.nlm.nih.gov/36970885/)). Foundational care — dietary modification (small, low-fat, low-fiber meals), nutritional support, glycemic control, opioid cessation, and antiemetics — remains central ([PMID: 39674226](https://pubmed.ncbi.nlm.nih.gov/39674226/)).

> *"There are conditional recommendations for the use of metoclopramide and erythromycin in patients with gastroparesis. Conditional recommendations were issued against the use of domperidone, prucalopride, aprepitant, nortriptyline, buspirone, and cannabidiol as first-line therapies."* — [PMID: 40976635](https://pubmed.ncbi.nlm.nih.gov/40976635/)

**Suggested NCIT terms:** Metoclopramide (C62035); Erythromycin (C557); Domperidone; Botulinum Toxin; Gastric Electrical Stimulation.

### 6. Mechanistic Causal Axis — Macrophage Polarization, HO-1/Oxidative Stress, ICC and nNOS Loss (F006)

Mouse-model evidence establishes the neuromuscular-injury axis (largely from NOD/streptozotocin diabetic models but mechanistically shared with IGP, which exhibits the same ICC/CD206 lesions):

1. **Choi et al. 2008** ([PMID: 18926825](https://pubmed.ncbi.nlm.nih.gov/18926825/)): loss of HO-1 upregulation in gastric macrophages → increased reactive oxygen species → loss of Kit (ICC) and nNOS → delayed gastric emptying. HO-1 induction by hemin restored Kit/nNOS and normalized emptying; HO-1 inhibition *caused* gastroparesis in normal mice.
2. **Cipriani et al. 2018** ([PMID: 29501441](https://pubmed.ncbi.nlm.nih.gov/29501441/)): macrophage-deficient **Csf1op/op** mice do *not* develop delayed emptying or ICC damage when made diabetic — proving muscularis macrophages are **necessary** for the injury.
3. **Choi et al. 2016** ([PMID: 27795979](https://pubmed.ncbi.nlm.nih.gov/27795979/)): **IL-10** activates M2/cytoprotective macrophages and induces HO-1, restoring gastric emptying, slow-wave activity, and ICC networks in diabetic mice.

> *"Induction of HO-1 by hemin decreased reactive oxygen species, rapidly restored Kit and neuronal nitric oxide synthase expression, and completely normalized gastric emptying... Inhibition of HO-1 activity in mice with normal gastric emptying caused a loss of Kit expression and development of diabetic gastroparesis."* — [PMID: 18926825](https://pubmed.ncbi.nlm.nih.gov/18926825/)

**Suggested GO terms:** *response to oxidative stress* (GO:0006979), *heme oxygenase activity* (GO:0004392), *nitric oxide biosynthetic process* (GO:0006809), *macrophage activation* (GO:0042116). **CHEBI:** heme (CHEBI:30413), nitric oxide (CHEBI:16480), reactive oxygen species (CHEBI:26523).

### 7. Etiology and Risk Factors (F007)

IGP is a **diagnosis of exclusion** — of diabetic, post-surgical/iatrogenic, medication-induced, connective-tissue, neurological, and identifiable post-viral causes ([PMID: 30385743](https://pubmed.ncbi.nlm.nih.gov/30385743/); [PMID: 36970885](https://pubmed.ncbi.nlm.nih.gov/36970885/)). A recognized **post-infectious/post-viral subgroup (PIGP)** follows acute viral illness (CMV, EBV documented) and is typically self-limiting — **4 of 7 PIGP patients resolved spontaneously within 4 weeks–12 months** (Naftali et al. 2007, [PMID: 17716347](https://pubmed.ncbi.nlm.nih.gov/17716347/)); ~19% of registry patients reported an infectious prodrome. Key non-genetic risk associations: **female sex** (~4:1 to ~9:1), overweight status (46%), anxiety/depression (36%/18%), overlap with functional dyspepsia (86%), and a suggested bidirectional relationship with **eating disorders** (nondiabetic gastroparesis carries higher malnutrition/mortality; Fagan et al. 2026, [PMID: 41638531](https://pubmed.ncbi.nlm.nih.gov/41638531/)). There is **no established Mendelian cause**.

> *"Gastroparesis can have idiopathic, diabetic, iatrogenic, post-surgical or post-viral aetiologies."* — [PMID: 30385743](https://pubmed.ncbi.nlm.nih.gov/30385743/)

> *"Post-infectious gastroparesis (PIGP) is a subgroup of idiopathic gastroparesis."* — [PMID: 17716347](https://pubmed.ncbi.nlm.nih.gov/17716347/)

### 8. Diagnostic Evaluation (F008)

Diagnosis requires objective delayed gastric emptying without mechanical obstruction. **Gastric emptying scintigraphy (GES)** is the gold standard: a standardized **4-hour solid-meal** (low-fat egg-white "EggBeaters" meal) protocol, key threshold **>10% retention at 4 hours** (and/or >60% at 2 h); severe delay is **>35% at 4 h** (Rao et al. 2011 ANMS/ESNM position paper, [PMID: 21138500](https://pubmed.ncbi.nlm.nih.gov/21138500/)). AGA 2025 recommends 4-hour over 2-hour testing ([PMID: 40976635](https://pubmed.ncbi.nlm.nih.gov/40976635/)). Validated alternatives include the **¹³C-breath test** (spirulina/octanoate) and the **wireless motility capsule**, which correlate with scintigraphy but lack full standardization ([PMID: 41128532](https://pubmed.ncbi.nlm.nih.gov/41128532/)). Mechanical obstruction is excluded by upper endoscopy/imaging. Research/specialist tools: EndoFLIP (pyloric distensibility), electrogastrography, antroduodenal manometry, full-thickness gastric biopsy. **No blood biomarker or genetic test is diagnostic.**

> *"The tests include measurements of: gastric emptying with scintigraphy, wireless motility capsule, and (13)C breath tests."* — [PMID: 21138500](https://pubmed.ncbi.nlm.nih.gov/21138500/)

### 9. Prognosis, Quality of Life, and Disease Course (F009)

IGP is typically **chronic**; spontaneous remission is uncommon except in the post-viral subset. In a multicenter GpCRC registry (Parkman et al. 2026, [PMID: 41833524](https://pubmed.ncbi.nlm.nih.gov/41833524/); N=1013, 607 idiopathic), predominant symptoms were nausea (31%), vomiting (20%), abdominal pain (20%). **Abdominal pain was more often predominant in idiopathic** (vs vomiting in diabetic) and that group had the **lowest quality-of-life scores**. Over 48 weeks, GCSI improved by ≥1 point in only **26% overall** — more often with predominant nausea (32%) or bloating (35%), less often with fullness (13%) or abdominal pain (15%), indicating modest, symptom-dependent improvement. Complications include malnutrition, dehydration, electrolyte disturbance, weight loss, bezoar formation, impaired glycemic control, frequent hospitalization, and reduced QoL. Overall survival is reduced ([PMID: 19249393](https://pubmed.ncbi.nlm.nih.gov/19249393/)). QoL instruments: PAGI-SYM, GCSI, SF-12/SF-36, EQ-5D, GIQLI.

> *"Of 555 patients followed over 48 weeks, GCSI improved by ≥ 1 in 26% overall, more often in patients with initial PrS of nausea (32%) and bloating (35%) and less often for initial PrS of fullness (13%) or abdominal pain (15%)."* — [PMID: 41833524](https://pubmed.ncbi.nlm.nih.gov/41833524/)

### 10. Genetic/Molecular Basis — No Mendelian Cause; SCN5A/NaV1.5 as Candidate (F010)

IGP has **no established causal gene, OMIM entry, or pathogenic-variant classification** — it is complex/multifactorial and is not listed as monogenic in OMIM/ClinVar. The strongest molecular-genetic lead across GI neuromuscular motility disorders is **SCN5A**, encoding the voltage-gated sodium channel **NaV1.5** expressed by ICC and smooth muscle. Beyder et al. 2014 ([PMID: 24613995](https://pubmed.ncbi.nlm.nih.gov/24613995/)) found SCN5A missense mutations in **13/584 (2.2%)** IBS patients, 10/13 disrupting NaV1.5 function (9 loss-of-function, 1 gain-of-function); mexiletine restored function and normalized bowel habits in a p.A997T carrier. Verstraelen et al. 2015 ([PMID: 25898860](https://pubmed.ncbi.nlm.nih.gov/25898860/)) review NaV1.5 channelopathy in GI motility disorders. At the tissue level, IGP shows decreased muscularis-externa mRNA for **MYH11, MYLK1, PDGFRA, PDGFB, and HMOX1** ([PMID: 29052298](https://pubmed.ncbi.nlm.nih.gov/29052298/)) and macrophage-based immune-gene dysregulation on transcriptomic/proteomic profiling (Chikkamenahalli et al. 2020, [PMID: 32718570](https://pubmed.ncbi.nlm.nih.gov/32718570/); datasets GEO **GSE115601**, single-cell **GSE252126**). No recurrent chromosomal abnormality, epigenetic signature, or founder effect is established.

> *"Missense mutations were found in SCN5A in 13 of 584 patients (2.2%, probands)."* — [PMID: 24613995](https://pubmed.ncbi.nlm.nih.gov/24613995/)

**Suggested gene annotations:** SCN5A (HGNC:10593, candidate); HMOX1 (HGNC:5013); NOS1/nNOS (HGNC:7872); KIT (HGNC:6342); ANO1 (HGNC:21625); PDGFRA (HGNC:8803).

### 11. Animal/Model Systems and the Nitrergic-Oxidative-Stress Axis (F011)

Principal model systems (mostly mouse/rat):

| Model | Key feature | Reference |
|---|---|---|
| **nNOS-deficient (Nos1⁻/⁻) mice** | Established *genetic* model; delayed emptying, impaired pyloric relaxation. Neural stem cell transplant → nNOS+ neurons, improved emptying (49.7% vs 35.1%, *P<0.01*) | [PMID: 16344050](https://pubmed.ncbi.nlm.nih.gov/16344050/) |
| **NOD / streptozotocin diabetic mice** | Delayed emptying + ICC loss, reversible by HO-1/IL-10 | [PMID: 18926825](https://pubmed.ncbi.nlm.nih.gov/18926825/), [PMID: 27795979](https://pubmed.ncbi.nlm.nih.gov/27795979/) |
| **Csf1op/op macrophage-deficient mice** | Protected from delayed emptying/ICC damage | [PMID: 29501441](https://pubmed.ncbi.nlm.nih.gov/29501441/) |
| **Kit mutant (W/Wv) mice** | Model ICC deficiency | — |
| **ApoE-knockout mice** | Hyperlipidemia/oxidative-stress model; reduced nitrergic relaxation with decreased nNOS, GCH-1, NRF2 (NFE2L2) | [PMID: 22302246](https://pubmed.ncbi.nlm.nih.gov/22302246/) |

> *"nNOS-/- mice, a well-established genetic model of gastroparesis... Gastric emptying was significantly increased in mice that received NSCs as compared with vehicle-injected controls (49.67% vs 35.09%; P < .01)."* — [PMID: 16344050](https://pubmed.ncbi.nlm.nih.gov/16344050/)

In vitro/cellular models: isolated ICC, muscularis macrophage cultures, and human full-thickness gastric biopsy tissue. **Limitation:** most causal-mechanism models are diabetic; no dedicated, validated *idiopathic* genetic model exists.

### 12. Anatomy, Hormonal Basis of Female Predominance, and Temporal Features (F012)

**ANATOMY:** Primary organ is the **stomach** (UBERON:0000945), especially the **antrum** (UBERON:0001165) and **pylorus** (UBERON:0001166), within the digestive system (UBERON:0001007). The lesion localizes to the **muscularis propria/externa** (UBERON:0006909): circular/longitudinal smooth muscle (CL:0000192), **myenteric (Auerbach) plexus** (UBERON:0002439), ICC (CL:0002088), nitrergic/nNOS enteric neurons (CL:0000540), and muscularis macrophages (CL:0000235). Extrinsic vagal/autonomic innervation and the brain-gut axis are implicated.

**FEMALE PREDOMINANCE & HORMONES:** Healthy women physiologically empty solids and liquids more slowly than men ("postprandial physiologic gastroparesis"; Caballero-Plasencia et al. 1999, [PMID: 10499477](https://pubmed.ncbi.nlm.nih.gov/10499477/)); sex steroids (progesterone, estrogen) inhibit gastric emptying (Hutson et al. 1989, [PMID: 2909416](https://pubmed.ncbi.nlm.nih.gov/2909416/)) — a biological basis for the ~4:1–9:1 female predominance.

> *"These findings support the hypothesis that sex steroid hormones have variable inhibitory effects on gastric emptying of a mixed meal."* — [PMID: 2909416](https://pubmed.ncbi.nlm.nih.gov/2909416/)

**TEMPORAL:** Adult-onset (mean ~41 y), can be childhood-onset; onset acute in ~50% (often post-infectious) or insidious; course typically chronic and fluctuating/episodic, lifelong in most, but self-limiting in the post-viral subset over weeks–months.

---

## Mechanistic Model / Interpretation

### Ordered Causal Chain (initiating lesion → clinical manifestation)

```
[Initiating triggers — branch point]
  ├─ Acute viral infection (CMV/EBV) ─┐         (post-infectious subtype; ~19% of cases)
  ├─ Unknown idiopathic trigger ───────┤
  └─ Candidate SCN5A/NaV1.5 ───────────┘  (inferred susceptibility, not proven causal)
                    │
                    ▼
(1) Loss of cytoprotective CD206+ / HO-1+ (M2) muscularis macrophages
        │  (demonstrated in human IGP biopsy: CD206 IG 4.16 vs 6.59, P=0.04)
        ▼  "leads to"
(2) Failure of HO-1–mediated antioxidant defense
        │  (HMOX1 mRNA reduced in IGP muscularis; model-proven axis)
        ▼  "results in"
(3) Unchecked oxidative stress (↑ reactive oxygen species) in muscularis propria
        │  (direct in diabetic models; INFERRED in idiopathic)
        ▼  "causes"
(4) Injury/loss of interstitial cells of Cajal (ICC)  ──┐
    and loss of nitrergic (nNOS) enteric neurons  ──────┤  (ICC IG 2.53 vs 6.05/hpf, P=0.004)
        │                                                │
        ▼                                                ▼
(5) Impaired gastric slow-wave pacemaking     Loss of nitrergic pyloric relaxation
    + downregulated contractile genes          + impaired accommodation
    (MYH11, MYLK1, PDGFRA/B)                    (antropyloric dyscoordination)
        │                                                │
        └───────────────┬────────────────────────────────┘
                        ▼  "results in"
(6) Delayed gastric emptying + gastric sensorimotor dysfunction
                        ▼  "manifests as"
(7) Nausea, vomiting, early satiety, postprandial fullness, bloating, abdominal pain
    (modulated by visceral hypersensitivity, gut-brain axis, anxiety/depression)
```

**Upstream vs downstream.** The **macrophage phenotype shift** (M2/HO-1 depletion) is the most upstream demonstrable node; **oxidative stress** is the central effector; **ICC and nNOS loss** are the proximate lesions producing the **downstream** physiology of delayed emptying. The female-predominant epidemiology sits *alongside* this chain as a permissive modifier: hormonally slower baseline emptying lowers the threshold at which neuromuscular injury becomes symptomatic.

**Important caveat on evidence strength.** The *human* IGP data are strongest for the **static histological endpoints** (ICC loss, CD206 loss, contractile-gene downregulation). The **dynamic causal links** (macrophage → HO-1 → ROS → ICC/nNOS loss) are proven chiefly in **diabetic/oxidative-stress mouse models**; their application to idiopathic disease is a well-supported inference grounded in the shared histological lesion, not a directly demonstrated mechanism in humans. A parallel, increasingly emphasized view reframes IGP as a **sensorimotor disorder on a spectrum with functional dyspepsia** ([PMID: 33548234](https://pubmed.ncbi.nlm.nih.gov/33548234/); [PMID: 42235947](https://pubmed.ncbi.nlm.nih.gov/42235947/)), in which delayed emptying correlates poorly with symptoms and gut-brain/visceral-hypersensitivity mechanisms carry substantial weight.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [39674226](https://pubmed.ncbi.nlm.nih.gov/39674226/) | Rome Foundation consensus on IGP | Authoritative definition + diagnostic criteria (F001) |
| [36730846](https://pubmed.ncbi.nlm.nih.gov/36730846/) | Atypical causes of gastroparesis | IGP = 58.2% of cases (F001) |
| [28066953](https://pubmed.ncbi.nlm.nih.gov/28066953/) | CD206 macrophage loss in gastroparesis | Quantifies ICC + M2 macrophage loss (F002) |
| [29052298](https://pubmed.ncbi.nlm.nih.gov/29052298/) | Transcriptional changes in IGP muscularis | Contractile/HMOX1 gene downregulation (F002, F010) |
| [25041465](https://pubmed.ncbi.nlm.nih.gov/25041465/) | CD206 & ICC in gastric body | Confirms ICC loss + CD206 correlation (F002) |
| [20965184](https://pubmed.ncbi.nlm.nih.gov/20965184/) | Clinical features of IG (NIDDK) | Demographics, 88% female, prodrome (F003, F007) |
| [19249393](https://pubmed.ncbi.nlm.nih.gov/19249393/) | Olmsted County epidemiology | Incidence/prevalence, female predominance, survival (F004, F009) |
| [22323986](https://pubmed.ncbi.nlm.nih.gov/22323986/) | Hidden gastroparesis "iceberg" | Overall diagnosed prevalence 24.2/100k (F004) |
| [40976635](https://pubmed.ncbi.nlm.nih.gov/40976635/) | AGA 2025 guideline | Pharmacotherapy + 4-h scintigraphy (F005, F008) |
| [28721575](https://pubmed.ncbi.nlm.nih.gov/28721575/) | Gastroparesis therapeutic advances | Metoclopramide sole FDA-approved agent (F005) |
| [42702756](https://pubmed.ncbi.nlm.nih.gov/42702756/) | TD with metoclopramide | Continuous > intermittent TD risk (F005) |
| [36970885](https://pubmed.ncbi.nlm.nih.gov/36970885/) | 2023 clinical management update | Refractory interventions; etiologic categories (F005, F007) |
| [18926825](https://pubmed.ncbi.nlm.nih.gov/18926825/) | HO-1 protects ICC | Core HO-1/ROS/ICC/nNOS axis (F006) |
| [29501441](https://pubmed.ncbi.nlm.nih.gov/29501441/) | Macrophages & delayed emptying | Csf1op/op mice protected — macrophages necessary (F006) |
| [27795979](https://pubmed.ncbi.nlm.nih.gov/27795979/) | IL-10 restores gastric emptying | M2/HO-1 activation reverses lesion (F006) |
| [30385743](https://pubmed.ncbi.nlm.nih.gov/30385743/) | Gastroparesis (Nat Rev Dis Primers) | Etiologic classification (F007) |
| [17716347](https://pubmed.ncbi.nlm.nih.gov/17716347/) | Post-infectious gastroparesis | PIGP subgroup, self-limiting course (F007) |
| [21138500](https://pubmed.ncbi.nlm.nih.gov/21138500/) | ANMS/ESNM transit position paper | GES/breath test/WMC diagnostics (F008) |
| [41128532](https://pubmed.ncbi.nlm.nih.gov/41128532/) | Pediatric GES review | Breath test + WMC alternatives (F008) |
| [41833524](https://pubmed.ncbi.nlm.nih.gov/41833524/) | Predominant symptom & QoL | Modest, symptom-dependent improvement (F009) |
| [41638531](https://pubmed.ncbi.nlm.nih.gov/41638531/) | Nondiabetic gastroparesis diet review | Higher malnutrition/mortality (F007, F009) |
| [24613995](https://pubmed.ncbi.nlm.nih.gov/24613995/) | NaV1.5 channelopathy in IBS | SCN5A candidate susceptibility (F010) |
| [25898860](https://pubmed.ncbi.nlm.nih.gov/25898860/) | SCN5A channelopathy review | NaV1.5 in ICC/smooth muscle (F010) |
| [32718570](https://pubmed.ncbi.nlm.nih.gov/32718570/) | Gastric biopsies review | Macrophage immune dysregulation, omics (F010) |
| [16344050](https://pubmed.ncbi.nlm.nih.gov/16344050/) | NSC transplant in nNOS⁻/⁻ mice | nNOS⁻/⁻ genetic model; rescue (F011) |
| [22302246](https://pubmed.ncbi.nlm.nih.gov/22302246/) | ApoE-KO gastric nitrergic/NRF2 | Oxidative-stress model (F011) |
| [10499477](https://pubmed.ncbi.nlm.nih.gov/10499477/) | Gastric emptying & menstrual cycle | Physiologic slower emptying in women (F012) |
| [2909416](https://pubmed.ncbi.nlm.nih.gov/2909416/) | Gender/menopause & gastric emptying | Sex steroids inhibit emptying (F012) |
| [33548234](https://pubmed.ncbi.nlm.nih.gov/33548234/) | FD & gastroparesis interchangeable | Spectrum/sensorimotor reframing (interpretation) |
| [42235947](https://pubmed.ncbi.nlm.nih.gov/42235947/) | GESA position statement on IGP | Sensorimotor-disorder reconceptualization (interpretation) |

**Supporting vs challenging.** The biopsy and animal-model literature *support* the ICC/macrophage/oxidative-stress mechanistic core. The functional-dyspepsia-overlap and GESA sensorimotor papers *challenge* a purely "delayed-emptying" framing — noting that emptying rates correlate poorly with symptoms and are labile (37–42% of patients reclassify between FD and gastroparesis over a year; [PMID: 33548234](https://pubmed.ncbi.nlm.nih.gov/33548234/)). Both perspectives are integrated above.

---

## Sections With Limited or Not-Applicable Data

- **Causal genes / pathogenic variants / ACMG classification (Section 4):** None established. No OMIM entry; not in ClinVar as monogenic. SCN5A/NaV1.5 is a *candidate susceptibility* factor only.
- **Epigenetics, chromosomal abnormalities, founder effects, carrier frequency, inheritance pattern, penetrance, anticipation, consanguinity (Sections 4, 9):** Not applicable / none established — IGP is multifactorial, not Mendelian.
- **Infectious agents (Section 5):** Only the post-infectious subtype has documented triggers (CMV, EBV); no single causative pathogen.
- **Other species / natural disease / veterinary relevance / zoonosis (Section 14):** No naturally occurring idiopathic gastroparesis is described in companion animals or wildlife; relevant data are limited to induced laboratory rodent models (Section 15). Orthologous genes exist (e.g., mouse *Nos1*, *Hmox1*, *Kit*, *Scn5a*) but no OMIA natural-disease entry corresponds to human IGP.
- **Gene therapy, cell therapy, RNA-based therapy, immunotherapy, pharmacogenomics (Section 12):** No approved advanced therapeutics; IL-10/HO-1 induction and neural stem cell transplantation are experimental (model-stage only).

---

## Limitations and Knowledge Gaps

1. **Mechanism is inferred, not proven, in humans.** The macrophage→HO-1→ROS→ICC/nNOS causal chain is demonstrated primarily in **diabetic mouse models**; human IGP evidence is largely **cross-sectional histology**. The direction of causation and the initiating trigger in idiopathic disease remain unknown.
2. **Poor symptom–physiology correlation.** Gastric emptying rate correlates weakly with symptom severity and is labile over time, undermining delayed emptying as a unifying pathophysiological endpoint and blurring the boundary with functional dyspepsia.
3. **No molecular diagnostic or biomarker.** Diagnosis rests on a functional test (scintigraphy) with imperfect reproducibility; no blood/genetic biomarker exists.
4. **Heterogeneous entity.** IGP almost certainly aggregates several distinct pathophysiologies (post-viral, sensorimotor/FD-overlap, eating-disorder-associated, channelopathy-related), limiting the generalizability of any single mechanism.
5. **Modest, refractory treatment landscape.** Only ~26% achieve meaningful symptom improvement; ~one-third are refractory; the sole FDA-approved drug carries a serious neurological risk.
6. **No dedicated idiopathic animal model.** Existing genetic models (nNOS⁻/⁻, Kit-mutant) recapitulate *lesions* but not the idiopathic *etiology*.
7. **Sex-difference mechanism underexplored.** The estrogen/progesterone contribution is established physiologically but not mechanistically linked to the ICC/macrophage lesion.

---

## Proposed Follow-up Experiments / Actions

1. **Human muscularis single-cell + spatial transcriptomics** (extend GSE252126) comparing IGP, diabetic gastroparesis, FD, and controls to test whether the M2/HO-1 macrophage-depletion axis operates in *idiopathic* tissue and to resolve disease subtypes.
2. **Prospective post-viral cohort** with serial GES, biopsy, and viral serology to define which triggers produce self-limiting vs chronic disease and to capture the earliest cellular events.
3. **Targeted SCN5A/NaV1.5 sequencing** in a well-phenotyped IGP registry (mirroring the IBS 2.2% finding) with functional electrophysiology of variants, and a pilot of **mexiletine** in loss-of-function carriers.
4. **Translational HO-1/IL-10 or NRF2-activator trial** (e.g., dimethyl fumarate) targeting the oxidative-stress node validated in ApoE-KO and diabetic models.
5. **Sex-hormone mechanistic studies** linking estrogen/progesterone signaling to ICC survival and macrophage polarization, to explain female predominance.
6. **Biomarker discovery** (serum proteomics/metabolomics; circulating macrophage-phenotype or ICC-injury markers) to replace or complement scintigraphy.
7. **Redefinition initiative** — adopt the sensorimotor-spectrum framework ([PMID: 42235947](https://pubmed.ncbi.nlm.nih.gov/42235947/); [PMID: 39674226](https://pubmed.ncbi.nlm.nih.gov/39674226/)) with symptom-plus-physiology endpoints in future trials rather than emptying rate alone.

---

*Report compiled from 12 confirmed findings and 52 reviewed papers across 5 investigation iterations. Evidence source types are indicated throughout: human clinical (registry/biopsy), model organism (mouse/rat), in vitro (isolated ICC/macrophage), and computational (transcriptomic/proteomic datasets).*


## Artifacts

- [OpenScientist final report](Idiopathic_Gastroparesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Idiopathic_Gastroparesis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 32 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 10 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0006909` (1 mention) - the report calls it "muscularis propria/externa"; UBERON calls it **lumen of digestive tract**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004392` (1 mention) - the report calls it "heme oxygenase activity"; GO calls it **heme oxygenase (decyclizing) activity**, and lists "heme oxygenase activity" among its other names
- `UBERON:0001165` (1 mention) - the report calls it "antrum"; UBERON calls it **pyloric antrum**, and lists "antrum" among its other names
- `UBERON:0002439` (1 mention) - the report calls it "myenteric (Auerbach) plexus"; UBERON calls it **myenteric nerve plexus**