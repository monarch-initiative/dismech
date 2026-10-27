---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-14T20:46:30.655714'
end_time: '2026-09-14T21:32:25.079176'
duration_seconds: 2754.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Recessive Optic Atrophy OPA7 Type
  mondo_id: MONDO:0013069
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
citation_count: 12
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 17
  validator_version: 0.2.1
term_validation:
  total_terms: 16
  verified: 15
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 12
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0031604
    reported_labels:
    - auditory neuropathy
    ontology_label: Agenesis of the carotid canal
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Autosomal_Recessive_Optic_Atrophy_OPA7_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Recessive_Optic_Atrophy_OPA7_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Optic Atrophy OPA7 Type
- **MONDO ID:** MONDO:0013069 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Optic Atrophy OPA7 Type** covering all of the
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

# Autosomal Recessive Optic Atrophy, OPA7 Type (TMEM126A): A Comprehensive Disease Report

**MONDO:** MONDO:0013069 · **OMIM phenotype:** #612989 · **OMIM gene:** *612988 (TMEM126A) · **Locus:** 11q14.1 · **Category:** Mendelian (autosomal recessive)

---

## Summary

Autosomal recessive optic atrophy OPA7 type is an ultra-rare, early-onset, bilateral, progressive mitochondrial optic neuropathy caused by **biallelic loss-of-function variants in *TMEM126A*** on chromosome 11q14.1. It was the first gene identified for **nonsyndromic autosomal recessive optic atrophy**, discovered by homozygosity mapping and positional cloning in a large consanguineous Algerian family and additional families from the Maghreb, all carrying a recurrent nonsense founder allele, **c.163C>T; p.Arg55\*** (R55X) ([PMID: 19327736](https://pubmed.ncbi.nlm.nih.gov/19327736/)). Until this discovery the very existence of nonsyndromic recessive optic atrophy had been disputed ([PMID: 22815638](https://pubmed.ncbi.nlm.nih.gov/22815638/)).

Mechanistically, TMEM126A is an **inner mitochondrial membrane assembly factor** for the **ND4 distal membrane module of respiratory chain complex I (NADH:ubiquinone oxidoreductase)**. Its loss produces an **isolated complex I deficiency**, established by two independent 2021 studies ([PMID: 33879611](https://pubmed.ncbi.nlm.nih.gov/33879611/); [PMID: 33882309](https://pubmed.ncbi.nlm.nih.gov/33882309/)). The resulting bioenergetic failure and increased reactive oxygen species (ROS) selectively injure **retinal ganglion cells (RGCs)** and their optic-nerve axons — the cell type most vulnerable to perturbed mitochondrial homeostasis — producing the optic-atrophy phenotype shared across the hereditary optic neuropathies ([PMID: 36155660](https://pubmed.ncbi.nlm.nih.gov/36155660/)). Because the lesion is a complex I defect, OPA7 is bioenergetically analogous to Leber hereditary optic neuropathy (LHON), which is caused by mtDNA complex I subunit mutations.

Clinically, OPA7 presents in childhood (sometimes congenitally, occasionally in adolescence) with bilateral optic disc pallor, reduced visual acuity, central/centrocecal scotoma, and dyschromatopsia; a subset of patients have **auditory neuropathy** and/or **peripheral sensory-motor neuropathy**, defining a syndromic tail to the phenotype ([PMID: 20405026](https://pubmed.ncbi.nlm.nih.gov/20405026/); [PMID: 22815638](https://pubmed.ncbi.nlm.nih.gov/22815638/)). There is **no OPA7-specific therapy**; care is supportive (low-vision aids, hearing rehabilitation, genetic counseling), with idebenone and AAV gene therapy as mechanism-based prospects extrapolated — not yet validated — from LHON.

---

## Key Findings

### Finding 1 — TMEM126A is the causal gene, with a Maghreb founder mutation

Whole-genome homozygosity mapping combined with positional cloning in a large consanguineous Algerian family, followed by confirmation in three additional Maghreb families, identified *TMEM126A* (chr 11q14.1; OMIM gene *612988; phenotype OPA7 #612989) as **the first gene responsible for nonsyndromic autosomal recessive optic atrophy** ([PMID: 19327736](https://pubmed.ncbi.nlm.nih.gov/19327736/)). The authors state they *"identified the first gene, to our knowledge, responsible for this condition, TMEM126A, in a large multiplex inbred Algerian family and subsequently in three other families originating from the Maghreb."*

The recurrent founder allele is the nonsense variant **c.163C>T; p.Arg55\*** (R55X). An independent Moroccan family was later found to carry the identical R55X allele, and haplotype analysis was *"consistent with a single ancestral origin"* ([PMID: 22815638](https://pubmed.ncbi.nlm.nih.gov/22815638/)) — confirming a North-African (Maghreb) founder effect. This founder architecture explains why the disease clusters in consanguineous populations of North-African ancestry.

### Finding 2 — TMEM126A is a mitochondrial complex I assembly factor for the ND4 module

Two independent 2021 studies established the molecular function of TMEM126A. Formosa et al. showed that *"loss of TMEM126A results in an isolated complex I deficiency"* and that *"TMEM126A is involved in the assembly of the ND4 distal membrane module of complex I,"* associating with the newly synthesized mtDNA-encoded ND4 subunit ([PMID: 33879611](https://pubmed.ncbi.nlm.nih.gov/33879611/)). This is functionally distinct from its paralogue TMEM126B, which assembles the ND2 module.

In parallel, D'Angelo et al. demonstrated that during complex I disassembly *"the ND4 module remains stable and bound to TMEM126A,"* concluding that they *"uncover the function of TMEM126A, the product of a disease gene causing recessive optic atrophy, as a factor necessary for the correct assembly and function of CI"* ([PMID: 33882309](https://pubmed.ncbi.nlm.nih.gov/33882309/)). Earlier work had localized the protein to the **inner mitochondrial membrane cristae** ([PMID: 23500070](https://pubmed.ncbi.nlm.nih.gov/23500070/): *"encode an inner mitochondrial membrane associated cristae protein"*), consistent with a role at the site of oxidative phosphorylation.

Together these establish the **upstream molecular lesion**: TMEM126A loss → failure to assemble the ND4 distal membrane module → isolated complex I deficiency.

### Finding 3 — Phenotype: early-onset bilateral progressive optic atrophy with variable auditory and peripheral neuropathy

The core phenotype is **bilateral optic atrophy** — temporal or diffuse optic disc pallor, reduced visual acuity, central/centrocecal scotoma, and dyschromatopsia — with childhood onset. Meyer et al. reported a consanguineous R55X family in which *"both affected subjects had poor vision from birth and complained of progressive visual loss over time,"* with bilateral temporal optic nerve pallor, normal full-field ERG (excluding a primary photoreceptor process), and grossly abnormal pattern VEPs indicating RGC/optic-nerve dysfunction. Crucially, *"audiological investigation in both siblings revealed abnormalities falling within the auditory neuropathy/dysynchrony spectrum,"* defining a **syndromic (optic atrophy + auditory neuropathy)** form ([PMID: 20405026](https://pubmed.ncbi.nlm.nih.gov/20405026/)).

Expressivity is variable. Désir et al. described a Moroccan family with a *"relatively mild clinical course, with sudden onset in adolescence in the proband,"* and noted that *"the proband, but not the other affected siblings, had sensory-motor axonal neuropathy"* with demyelinating features — extending the syndromic spectrum to **peripheral neuropathy**. A heterozygous carrier in that family exhibited exercise-induced transient visual loss (Uhthoff's phenomenon) ([PMID: 22815638](https://pubmed.ncbi.nlm.nih.gov/22815638/)). Kloth et al. reported relatively mild, non-syndromic disease in Turkish and Iraqi families ([PMID: 30961538](https://pubmed.ncbi.nlm.nih.gov/30961538/)).

### Finding 4 — Mutation spectrum extends beyond the R55X founder allele

Beyond the recurrent R55X nonsense founder allele in Maghrebian families, Kloth et al. identified pathogenic/likely pathogenic variants in non-Maghreb individuals, noting: *"To date, all reports of pathogenic TMEM126A variants are from affected individuals of Maghrebian origin, who all carry an identical nonsense variant. Here we report two novel variants in the TMEM126A gene from non-Maghreb individuals"* ([PMID: 30961538](https://pubmed.ncbi.nlm.nih.gov/30961538/)). These are a homozygous **splice-donor variant c.86+2T>C** in a Turkish patient (producing an exon-2-skipped functional null transcript) and a homozygous **missense p.Ser36Leu (S36L)** in Iraqi siblings, affecting a highly conserved residue and ultra-rare in population databases. TMEM126A is among the top 10 nuclear genes accounting for hereditary optic neuropathy diagnoses in a 2,186-proband cohort ([PMID: 36317462](https://pubmed.ncbi.nlm.nih.gov/36317462/)).

### Finding 5 — OPA7 belongs to the mitochondrial optic neuropathies; RGCs are selectively vulnerable

Reviews of hereditary optic neuropathies establish a **unifying mitochondrial pathophysiology**: *"A unifying feature in the pathophysiology of these disorders appears to involve mitochondrial dysfunction, suggesting that the retinal ganglion cells and their axons are especially susceptible to perturbations in mitochondrial homoeostasis"* ([PMID: 36155660](https://pubmed.ncbi.nlm.nih.gov/36155660/)). OPA7/TMEM126A joins OPA1 (dominant optic atrophy), the mtDNA complex I genes of LHON (MT-ND1/4/6), ACO2, RTN4IP1, SPG7, AFG3L2, MFN2, WFS1, FDXR, and NR2F1 among nuclear-gene-panel causes; these 10 genes account for **~96%** of autosomal optic neuropathy diagnoses in the 2,186-proband cohort ([PMID: 36317462](https://pubmed.ncbi.nlm.nih.gov/36317462/)). Because TMEM126A loss causes isolated complex I deficiency, OPA7 shares the LHON-type complex-I bioenergetic lesion.

### Finding 6 — Ultra-rare AR disorder with complete penetrance, variable expressivity, and strong consanguinity/founder component

Nonsyndromic autosomal recessive optic atrophy is described as *"extremely rare and its existence was disputed"* ([PMID: 22815638](https://pubmed.ncbi.nlm.nih.gov/22815638/)); reports remain *"sparse"* with only a handful of families worldwide ([PMID: 30961538](https://pubmed.ncbi.nlm.nih.gov/30961538/)). Inheritance is autosomal recessive (biallelic TMEM126A); reported families are consanguineous (Algerian, Moroccan, Pakistani, Turkish, Iraqi). Affected homozygotes are **consistently symptomatic** (complete penetrance for optic atrophy), whereas heterozygous carriers are generally unaffected — with the noted exception of a single carrier showing transient exercise-induced visual loss. Expressivity is variable in age of onset (congenital to adolescence) and in syndromic features (isolated optic atrophy vs. added auditory/peripheral neuropathy).

### Finding 7 — No OPA7-specific therapy; supportive care with idebenone/gene therapy as mechanism-based prospects

There is **no approved disease-specific or curative treatment** for OPA7. Management is supportive: low-vision aids and visual rehabilitation, hearing aids or cochlear implantation where auditory neuropathy is present, and genetic counseling. Because OPA7 shares the complex-I bioenergetic lesion of LHON, **idebenone** — a synthetic CoQ10 analogue — is a plausible but not OPA7-validated candidate. Its mechanism is described as: *"Idebenone, a synthetic CoQ derivative, is a potent intramitochondrial antioxidant and can shuttle electrons directly to complex III of the respiratory chain, thereby bypassing complex I deficiency"* ([PMID: 39963374](https://pubmed.ncbi.nlm.nih.gov/39963374/)). In LHON, a meta-analysis found a favorable effect: *"The overall mean LogMAR difference was -0.32 (95% CI: -0.50 to -0.15), with a favorable effect of idebenone"* ([PMID: 40653811](https://pubmed.ncbi.nlm.nih.gov/40653811/)). AAV gene-replacement (e.g., lenadogene nolparvovec for MT-ND4 LHON) provides proof-of-concept for optic-neuropathy gene therapy, but no OPA7 program exists ([PMID: 39704163](https://pubmed.ncbi.nlm.nih.gov/39704163/)).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in *TMEM126A*** (most commonly p.Arg55\* nonsense; also splice-donor c.86+2T>C and missense p.Ser36Leu) → absence or dysfunction of the TMEM126A protein at the inner mitochondrial membrane cristae. *[Demonstrated — human genetics, PMID 19327736, 22815638, 30961538]*
2. **Loss of TMEM126A → failure to assemble the ND4 distal membrane module of complex I.** TMEM126A normally binds the newly synthesized mtDNA-encoded ND4 subunit and chaperones its incorporation. *[Demonstrated — cell biology, PMID 33879611, 33882309]*
3. **Failed ND4-module assembly → isolated complex I (NADH:ubiquinone oxidoreductase) deficiency.** *[Demonstrated — PMID 33879611]*
4. **Complex I deficiency → impaired oxidative phosphorylation (reduced NADH oxidation, reduced proton pumping, reduced ATP synthesis) and increased reactive oxygen species.** *[Inferred for OPA7 by analogy to LHON complex-I lesions; established for the shared mechanism class, PMID 36155660]*
5. **Bioenergetic failure + oxidative stress → selective injury of retinal ganglion cells and their long, energy-demanding pre-laminar axons.** *[Demonstrated as a unifying mechanism of mitochondrial optic neuropathies, PMID 36155660]*
6. **RGC/axonal degeneration → bilateral, progressive optic atrophy** (disc pallor, reduced acuity, central/centrocecal scotoma, dyschromatopsia). *[Demonstrated clinically, PMID 20405026]*
   - **Branch A:** In a subset, the same bioenergetic vulnerability of specialized neurons → **auditory neuropathy/dysynchrony**. *[Demonstrated, PMID 20405026]*
   - **Branch B:** In a subset, → **peripheral sensory-motor axonal neuropathy** with demyelinating features. *[Demonstrated, PMID 22815638]*

### Diagram

```
 TMEM126A biallelic LoF (R55X / c.86+2T>C / S36L)
                 │
                 ▼
 Loss of inner-membrane cristae assembly factor
                 │
                 ▼
 ND4 distal membrane module fails to assemble  ── (paralogue TMEM126B → ND2 module, unaffected)
                 │
                 ▼
 Isolated Complex I (NADH:ubiquinone oxidoreductase) deficiency
                 │
        ┌────────┴────────┐
        ▼                 ▼
   ↓ ATP synthesis     ↑ ROS / oxidative stress
        └────────┬────────┘
                 ▼
 Selective RGC + optic-nerve axon degeneration (high energy demand)
                 │
     ┌───────────┼───────────────┐
     ▼           ▼               ▼
 Optic atrophy  Auditory        Peripheral
 (core)         neuropathy      neuropathy
                (subset)        (subset)
```

### Upstream vs downstream

- **Upstream (genetic/molecular):** TMEM126A loss; failed ND4-module assembly; complex I deficiency.
- **Downstream (cellular/clinical):** ATP depletion, ROS accumulation, RGC apoptosis/axonal loss, optic atrophy, and the variable auditory/peripheral neuropathy branches.

### Ontology term suggestions

| Domain | Term | ID |
|---|---|---|
| Disease | autosomal recessive optic atrophy OPA7 type | MONDO:0013069 |
| Gene | TMEM126A | HGNC:25382 |
| Biological process | mitochondrial respiratory chain complex I assembly | GO:0032981 |
| Biological process | ATP synthesis coupled electron transport | GO:0042773 |
| Cellular component | mitochondrial inner membrane | GO:0005743 |
| Cellular component | mitochondrial crista | GO:0030061 |
| Cell type | retinal ganglion cell | CL:0000740 |
| Anatomy | optic nerve | UBERON:0000941 |
| Anatomy | retina | UBERON:0000966 |
| Phenotype | optic atrophy | HP:0000648 |
| Phenotype | reduced visual acuity | HP:0007663 |
| Phenotype | central scotoma | HP:0000603 |
| Phenotype | dyschromatopsia / color vision defect | HP:0000551 |
| Phenotype | auditory neuropathy | HP:0031604 |
| Phenotype | peripheral axonal neuropathy | HP:0003477 |
| Chemical (therapeutic) | idebenone | CHEBI:31687 |

---

## Section-by-Section Detail

### 1. Disease Information
OPA7 is a nonsyndromic (with a syndromic tail) autosomal recessive mitochondrial optic neuropathy characterized by early-onset, bilateral, progressive degeneration of retinal ganglion cells and the optic nerve. **Identifiers:** MONDO:0013069; OMIM phenotype #612989; OMIM gene *612988; locus 11q14.1; Orphanet lists it under nonsyndromic/recessive optic atrophy. **Synonyms:** OPA7; optic atrophy 7; TMEM126A-related optic atrophy; autosomal recessive optic atrophy, TMEM126A type. Information is derived from **aggregated disease-level resources** and small consanguineous-family case series (not EHR/individual-patient registries).

### 2. Etiology
**Primary cause:** biallelic (homozygous or compound heterozygous) loss-of-function variants in *TMEM126A* (genetic, Mendelian). **Genetic risk factors:** the R55X founder allele in Maghreb populations; consanguinity dramatically raises the risk of homozygosity. **Environmental risk/protective factors and gene–environment interactions:** none established for OPA7 specifically; by analogy to LHON, mitochondrial toxins (tobacco, alcohol) and oxidative stressors are theoretical exacerbators but unproven here. No protective alleles are documented.

### 3. Phenotypes
Core: bilateral optic atrophy (HP:0000648), reduced visual acuity (HP:0007663), central/centrocecal scotoma (HP:0000603), dyschromatopsia (HP:0000551), temporal/diffuse optic disc pallor. Onset ranges from congenital/childhood to occasionally adolescence; course is **progressive**; penetrance for optic atrophy is complete in homozygotes. Variable syndromic features: auditory neuropathy/dysynchrony (HP:0031604) and peripheral sensory-motor axonal neuropathy (HP:0003477). Quality-of-life impact is substantial and lifelong (low vision/legal blindness affecting central vision, education, employment, mobility); where hearing is involved, communication is additionally affected. Disease-specific QoL instruments have not been reported for OPA7.

### 4. Genetic/Molecular Information
**Causal gene:** *TMEM126A* (HGNC:25382; NCBI Gene 84233; 11q14.1). **Pathogenic variants:** c.163C>T p.(Arg55\*) nonsense (founder, Maghreb); c.86+2T>C splice-donor (Turkish); c.107C>T p.(Ser36Leu) missense (Iraqi). Classification: pathogenic/likely pathogenic per ACMG; nonsense and splice alleles are functional nulls; the missense affects a highly conserved residue and is ultra-rare in gnomAD. **Origin:** germline. **Functional consequence:** loss of function (failed complex I ND4-module assembly). No modifier genes, epigenetic changes, or chromosomal abnormalities are established for OPA7.

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are established. This is a monogenic disorder; environmental factors are, at most, theoretical modifiers extrapolated from mitochondrial optic-neuropathy biology.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above. Key pathway: **mitochondrial respiratory chain complex I assembly (GO:0032981)** at the **inner mitochondrial membrane/cristae (GO:0005743/GO:0030061)**; downstream **oxidative phosphorylation** failure and **oxidative stress**; cellular process is **RGC apoptosis/axonal degeneration**. Cell type: **retinal ganglion cell (CL:0000740)**.

### 7. Anatomical Structures Affected
**Primary organ:** eye — specifically retina (UBERON:0000966) and optic nerve (UBERON:0000941); body system: nervous/visual. **Secondary:** auditory nerve/spiral ganglion (auditory neuropathy) and peripheral nerves (peripheral neuropathy). **Tissue/cell:** neural tissue; retinal ganglion cells (CL:0000740). **Subcellular:** mitochondrial inner membrane/cristae (GO:0005743/GO:0030061). **Lateralization:** bilateral (typically symmetric).

### 8. Temporal Development
**Onset:** congenital/pediatric, occasionally adolescent; insidious to sometimes sudden. **Progression:** slowly progressive over years; chronic and lifelong; no spontaneous remission. **Critical period:** RGC loss is presumed irreversible once established, so any future neuroprotective/gene therapy would need early intervention (as demonstrated for idebenone in LHON, PMID 39704163).

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** complete in homozygotes. **Expressivity:** variable (onset age; syndromic features). **Founder effect:** North-African (Maghreb) R55X of single ancestral origin. **Consanguinity:** central to disease occurrence. **Epidemiology:** ultra-rare (no reliable prevalence/incidence; only a handful of families worldwide). **Populations:** Algerian, Moroccan, Turkish, Iraqi, Pakistani consanguineous families. **Sex ratio:** no sex bias expected (autosomal recessive), consistent with reported affected siblings of both sexes.

### 10. Diagnostics
**Clinical:** ophthalmologic exam (visual acuity, color vision, visual fields showing central/centrocecal scotoma, fundoscopy showing optic disc pallor), OCT (RNFL/ganglion cell layer thinning), pattern VEP (abnormal, indicating RGC/optic-nerve dysfunction), full-field ERG (typically normal, excluding retinopathy). Audiology (ABR/OAE pattern of auditory neuropathy) and nerve conduction studies where syndromic features are suspected. **Genetic testing is definitive:** targeted *TMEM126A* sequencing, hereditary-optic-neuropathy gene panels, WES/WGS; mtDNA LHON testing to exclude the main differential. **Differential diagnosis:** LHON (maternal inheritance, mtDNA complex I mutations), OPA1 dominant optic atrophy, ACO2, RTN4IP1, WFS1 (Wolfram), and syndromic causes.

### 11. Outcome/Prognosis
Vision loss is chronic, bilateral, and generally progressive, leading to significant permanent visual impairment; the disorder is **not life-limiting** by itself. Morbidity is driven by low vision (± hearing loss, ± peripheral neuropathy). No validated prognostic biomarkers exist; earlier onset and syndromic features suggest greater burden. Recovery potential is limited given irreversible RGC loss.

### 12. Treatment
No OPA7-specific or curative therapy. **Supportive/rehabilitative:** low-vision aids, visual and occupational rehabilitation, hearing aids/cochlear implantation for auditory neuropathy, physiotherapy for peripheral neuropathy, genetic counseling. **Mechanism-based prospects (extrapolated from LHON, not OPA7-validated):** idebenone (NCIT synthetic CoQ analogue; bypasses complex I to complex III, antioxidant), and AAV gene-replacement/allotopic-expression approaches. Personalized/genotype-guided therapy is not yet available.

### 13. Prevention
No primary prevention beyond **genetic counseling and carrier/cascade testing** in at-risk consanguineous families. Prenatal or preimplantation genetic testing is feasible once the familial variant is known. Secondary/tertiary prevention focuses on early rehabilitation and management of syndromic complications. No immunization or public-health measures apply.

### 14. Other Species / Natural Disease
*TMEM126A* is evolutionarily conserved with orthologues in mouse (*Tmem126a*), zebrafish, and other vertebrates, and functions in complex I assembly across species. No well-characterized naturally occurring animal disease has been reported for OPA7 specifically; comparative pathology draws on the broader mitochondrial-optic-neuropathy literature. Zoonotic/cross-species transmission is not applicable (monogenic disorder).

### 15. Model Organisms
Cellular models (patient fibroblasts, gene-edited/knockdown human cell lines) were central to defining TMEM126A's complex-I ND4-module assembly role (PMID 33879611, 33882309). For the disease class, iPSC-derived retinal organoids reproduce RGC/axonal loss and respond to idebenone in the related LHON context (PMID 41019299), providing a template platform adaptable to OPA7. Dedicated *Tmem126a* knockout animal models with full OPA7 phenotype recapitulation are not prominently reported; developing an RGC-degeneration model that also captures the auditory/peripheral branches is an open need.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [19327736](https://pubmed.ncbi.nlm.nih.gov/19327736/) | TMEM126A mutated in AR nonsyndromic optic atrophy | Human genetics | F1: gene identification, founder R55X |
| [22815638](https://pubmed.ncbi.nlm.nih.gov/22815638/) | TMEM126A in a Moroccan family | Human genetics/clinical | F1, F3, F6: single ancestral origin, variable/mild course, peripheral neuropathy, ultra-rarity |
| [20405026](https://pubmed.ncbi.nlm.nih.gov/20405026/) | Nonsense TMEM126A: optic + auditory neuropathy | Human clinical | F3: congenital progressive vision loss, auditory neuropathy |
| [30961538](https://pubmed.ncbi.nlm.nih.gov/30961538/) | Novel TMEM126A variants, non-syndromic | Human genetics | F4, F6: splice & missense alleles beyond founder, sparse reports |
| [33879611](https://pubmed.ncbi.nlm.nih.gov/33879611/) | TMEM126A assembly factor for ND4 module | Cell biology | F2: isolated CI deficiency, ND4-module assembly |
| [33882309](https://pubmed.ncbi.nlm.nih.gov/33882309/) | TMEM126A/OPA7 binds ND4-module intermediate | Cell biology | F2: independent confirmation of assembly-factor role |
| [23500070](https://pubmed.ncbi.nlm.nih.gov/23500070/) | TMEM126A inner-membrane cristae protein | Cell biology | F2: subcellular localization |
| [36155660](https://pubmed.ncbi.nlm.nih.gov/36155660/) | Molecular basis of hereditary optic neuropathies | Review | F5: unifying mitochondrial mechanism, RGC vulnerability |
| [36317462](https://pubmed.ncbi.nlm.nih.gov/36317462/) | Top 10 genes in hereditary optic neuropathies | Human cohort (n=2186) | F4, F5: TMEM126A among top genes; 96% by 10 genes |
| [40653811](https://pubmed.ncbi.nlm.nih.gov/40653811/) | Idebenone in LHON meta-analysis | Meta-analysis | F7: idebenone benefit (LogMAR −0.32) |
| [39963374](https://pubmed.ncbi.nlm.nih.gov/39963374/) | Idebenone & gene therapy in LHON | Review | F7: idebenone mechanism (bypasses complex I) |
| [39704163](https://pubmed.ncbi.nlm.nih.gov/39704163/) | LHON clinical trials | Review | F7: AAV gene therapy proof-of-concept, early treatment |

Supporting/contextual literature includes RTN4IP1-related recessive optic neuropathy (PMID 26593267), reviews of mitochondrial eye disease (PMID 28481993), dominant optic atrophy/OPA1 biology (PMID 33340656), advanced therapies for inherited optic neuropathies (PMID 41318849), and iPSC retinal-organoid LHON models (PMID 41019299).

---

## Limitations and Knowledge Gaps

- **Extreme rarity:** Only a handful of families worldwide; no population-based prevalence/incidence, natural-history, or QoL data exist. All clinical characterization derives from small consanguineous case series.
- **Genotype–phenotype correlations are underpowered:** Whether R55X, splice, or missense alleles differ systematically in severity or syndromic penetrance is unknown.
- **Mechanistic gap for OPA7 specifically:** The ATP-depletion/ROS/RGC-apoptosis steps are inferred by analogy to LHON; OPA7 patient-derived RGC/organoid studies quantifying bioenergetic and ROS phenotypes are lacking.
- **No OPA7 therapy evidence:** Idebenone and gene therapy benefits are extrapolated from LHON; no OPA7 trial or even case-level treatment outcome data are available.
- **No dedicated animal model** with full OPA7 (optic + auditory + peripheral) recapitulation is well established.
- **Modifiers, epigenetics, and environmental interactions** are entirely uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Build an OPA7 iPSC → retinal-organoid model** from patient fibroblasts (R55X and non-founder alleles), quantifying RGC number, axonal density, mitochondrial membrane potential, ATP, complex I activity, and ROS — mirroring the LHON-RO paradigm (PMID 41019299) — and test idebenone rescue.
2. **Genotype–phenotype registry:** Aggregate all known families to correlate allele type with onset, progression, and syndromic-feature penetrance (auditory/peripheral).
3. **Generate a *Tmem126a* knockout/knock-in mouse or zebrafish** and phenotype RGC loss, VEP/ABR, and nerve conduction to test whether the syndromic branches are recapitulated.
4. **Deep bioenergetic characterization** of patient fibroblasts (Seahorse respirometry, BN-PAGE complex I assembly intermediates) to confirm the ND4-module assembly defect across disease alleles beyond R55X.
5. **Compassionate-use / n-of-1 idebenone trials** in OPA7 patients with structured OCT/visual-acuity endpoints, given the shared complex-I lesion and favorable LHON meta-analysis effect size.
6. **Explore AAV-mediated TMEM126A gene replacement** as a preclinical program, leveraging the lenadogene-nolparvovec optic-neuropathy delivery precedent.
7. **Carrier-screening and cascade-testing programs** in high-consanguinity North-African/Middle-Eastern communities to enable early counseling and future early intervention.

---

*Report compiled from 7 confirmed findings and 35 reviewed papers over 5 investigation iterations. Evidence types span human genetics/clinical case series, cell-biology functional studies, cohort analyses, and LHON-derived therapeutic meta-analyses. Claims are attributed only to the abstracts/citation snippets verified during the investigation.*


## Artifacts

- [OpenScientist final report](Autosomal_Recessive_Optic_Atrophy_OPA7_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Recessive_Optic_Atrophy_OPA7_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 15 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031604` (2 mentions) - the report calls it "auditory neuropathy"; HP calls it **Agenesis of the carotid canal**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000941` (2 mentions) - the report calls it "optic nerve"; UBERON calls it **cranial nerve II**, and lists "optic nerve" among its other names
- `HP:0000551` (2 mentions) - the report calls it "dyschromatopsia / color vision defect"; HP calls it **Color vision defect**