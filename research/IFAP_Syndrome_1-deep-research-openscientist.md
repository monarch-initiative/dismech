---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-29T11:31:45.720780'
end_time: '2026-08-29T12:00:19.478626'
duration_seconds: 1713.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IFAP Syndrome 1
  mondo_id: MONDO:0100213
  category: Genetic
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
citation_count: 24
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 39
  not_found: 1
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.024
  labels_checked: 12
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0100213
    reported_labels:
    - MONDO
    ontology_label: IFAP syndrome 1, with or without BRESHECK syndrome
  - term_id: HP:0033052
    reported_labels:
    - Angular cheilitis / periorificial keratotic plaques
    ontology_label: Non-epileptic seizure
  labels_variant: 6
  unresolved_terms:
  - NCIT:C29496
  obsolete_terms:
  - term_id: GO:0016021
    ontology_label: GO_0016021
    replaced_by: GO:0016020
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
  path: IFAP_Syndrome_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: IFAP_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IFAP Syndrome 1
- **MONDO ID:** MONDO:0100213 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **IFAP Syndrome 1** covering all of the
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

# IFAP Syndrome 1 (MONDO:0100213): Comprehensive Disease Characteristics Report

## Summary

**IFAP Syndrome 1** (Ichthyosis Follicularis, Atrichia, and Photophobia syndrome; OMIM #308205; MONDO:0100213; Orphanet ORPHA:2273) is an ultra-rare X-linked recessive genodermatosis defined by a congenital clinical triad of **ichthyosis follicularis** (generalized spiny, keratotic follicular papules), **atrichia/alopecia** (near-total loss of scalp hair, eyebrows, and eyelashes), and **photophobia** arising from a progressive, vascularizing keratopathy. The disorder is caused by **hypomorphic (partial loss-of-function) missense and splice-site variants in *MBTPS2*** (membrane-bound transcription factor peptidase, site 2; Xp22.12), which encodes an intramembrane zinc metalloprotease known as **site-2 protease (S2P)**. Because *MBTPS2* is on the X chromosome, affected individuals are predominantly male; female carriers may show mosaic, Blaschko-linear cutaneous lesions due to lyonization.

Mechanistically, S2P performs **regulated intramembrane proteolysis (RIP)** — it makes the second, membrane-embedded cleavage that liberates the active transcription-factor domains of **SREBP** (sterol regulatory element-binding protein, master regulator of cholesterol and fatty-acid synthesis) and **ATF6** (the ER-stress/unfolded-protein-response arm). Partial loss of S2P activity therefore simultaneously **impairs epidermal barrier lipid synthesis** and **cripples the ER-stress response**, disrupting terminal differentiation of epidermis, hair follicles, and the corneal/limbal epithelium. A key genotype–phenotype principle emerges: the amount of **residual protease activity** correlates inversely with clinical severity, generating a continuum that extends from isolated IFAP to the lethal multisystem **BRESHECK syndrome**. *MBTPS2* is allelic with several other Mendelian disorders (KFSD, X-linked Olmsted syndrome, and X-linked osteogenesis imperfecta type XIX), and phenocopies of the ichthyosis-follicularis phenotype are produced by variants in *SREBF1* (autosomal-dominant IFAP/hereditary mucoepithelial dysplasia) and *GJB2*.

There is **no curative therapy**. Management is symptomatic and multidisciplinary: emollients/keratolytics (urea) for skin, aggressive ocular-surface protection (lubrication, prophylactic antibiotics, punctal occlusion, tarsorrhaphy, amniotic membrane transplantation), and, in several reports, **systemic acitretin (~1 mg/kg)**, which yields partial improvement of cutaneous and corneal features but does not reverse alopecia or photophobia. Genetic counseling is essential given X-linked inheritance. This report compiles nine confirmed findings across 28 reviewed papers into a structured knowledge-base entry.

---

## Key Findings

### Finding 1 — *MBTPS2* hypomorphic variants cause IFAP Syndrome 1

IFAP Syndrome 1 is caused by **hypomorphic missense variants in *MBTPS2***, an X-linked gene encoding site-2 protease. The seminal mapping and gene-identification study by **Oeffner et al. (2009)** localized the IFAP locus to **Xp22.11–p22.13** (a 5.4-Mb interval between markers DXS989 and DXS8019) and identified missense mutations that exchange highly conserved amino-acid residues. Critically, the authors demonstrated a **quantitative genotype–phenotype relationship**: using functional complementation in Chinese hamster **M19 cells** (which lack endogenous S2P), they showed that five patient mutations impaired SRE-regulated reporter induction and growth in cholesterol/lipid-free medium, and that the **degree of diminished protease activity correlated with clinical severity** in male patients.

> *"missense mutations exchanging highly conserved amino acids of membrane-bound transcription factor protease, site 2 (MBTPS2) are associated with this phenotype"* — [PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/)

> *"The degree of diminished activity correlated with clinical severity as noted in male patients"* — [PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/)

**Key identifiers:** MONDO:0100213 · OMIM #308205 (disease) · *MBTPS2* OMIM *300294 · HGNC:7375 · cytogenetic locus **Xp22.12**.

### Finding 2 — Dual mechanism: RIP of SREBP (cholesterol homeostasis) and ATF6 (ER stress)

MBTPS2/S2P is a membrane-embedded **zinc metalloprotease** that activates signaling substrates by cleaving them *within* the lipid bilayer (regulated intramembrane proteolysis). Its two best-characterized substrates are **SREBP** (SREBF; controls lipid biosynthesis) and **ATF6** (the ER-stress/UPR transcription factor). The pathogenicity of *MBTPS2* variants was directly demonstrated by **Strong et al. (2022)**, who studied a BRESHECK-associated variant, **c.766G>A (p.Val256Leu)**, and found it impaired growth in cholesterol-depleted medium, attenuated SREBP-pathway activation, and **abolished the ER-stress (UPR) response** in vitro — establishing that both arms of S2P signaling are compromised.

> *"impaired cell growth in cholesterol-depleted media, attenuated activation of the sterol regulatory element-binding protein pathway, and failure to activate the endoplasmic reticulum stress response pathway"* — [PMID: 34655156](https://pubmed.ncbi.nlm.nih.gov/34655156/)

> *"cleaves and activates several signaling and regulatory proteins from the membrane"* — [PMID: 33743732](https://pubmed.ncbi.nlm.nih.gov/33743732/)

### Finding 3 — Clinical triad, X-linked inheritance, and the allelic disorder spectrum

IFAP is defined by the triad of **ichthyosis follicularis** (follicular keratotic/spiny papules), **atrichia/alopecia** (scalp, eyebrows, eyelashes), and **photophobia**. Additional recurrent features include palmoplantar keratoderma, nail dystrophy, recurrent infections, xerosis, and angular cheilitis. Inheritance is **X-linked recessive**, so affected individuals are predominantly male; **female carriers** display mosaic, Blaschko-linear lesions attributable to X-chromosome inactivation (lyonization). At the severe end of the spectrum lies **BRESHECK syndrome** (the IFAP triad plus intellectual disability and multiple congenital anomalies). *MBTPS2* is **allelic** to Keratosis Follicularis Spinulosa Decalvans (KFSD), Olmsted syndrome (X-linked form), and Osteogenesis Imperfecta type XIX.

> *"IFAP) syndrome is a rare autosomal recessive, X-linked, genetic disorder that involves a triad of follicular ichthyosis, atrichia of the scalp, and photophobia"* — [PMID: 38089015](https://pubmed.ncbi.nlm.nih.gov/38089015/)

> *"BRESHECK syndrome, characterized by the IFAP triad plus intellectual disability and multiple congenital anomalies"* — [PMID: 34655156](https://pubmed.ncbi.nlm.nih.gov/34655156/)

> *"Ichthyosis Follicularis, Atrichia and Photophobia syndrome (IFAP) with or without BRESHECK syndrome, Keratosis Follicularis Spinulosa Decalvans (KFSD), Olmsted syndrome, and Osteogenesis Imperfecta type XIX"* — [PMID: 33743732](https://pubmed.ncbi.nlm.nih.gov/33743732/)

X-linked skin-disease mosaicism in female carriers is documented in [PMID: 16720460](https://pubmed.ncbi.nlm.nih.gov/16720460/).

### Finding 4 — Ophthalmic disease is a progressive keratopathy driven by limbal stem-cell dysfunction

The photophobia of IFAP reflects a serious, **progressive corneal disease**. In males, ocular features include severe photophobia, corneal erosions/epithelial defects, superficial and deep corneal (neo)vascularization, corneal scarring, and progressive vision loss (down to counting-fingers acuity) (**Traboulsi 2004**). **Basilious et al. (2020)** used anterior-segment OCT to document bilateral limbal thickening, peripheral corneal pannus, conjunctivalization, and abnormal hyperreflective epithelium — a constellation "highly suggestive of **limbal stem cell dysfunction**." Carrier mothers can show **retinal vascular tortuosity** as an ocular sign of carrier status.

> *"The progressive conjunctivalization, spontaneous epithelial defects, and anterior segment optical coherence tomography features are highly suggestive of limbal stem cell dysfunction in IFAP syndrome"* — [PMID: 32482964](https://pubmed.ncbi.nlm.nih.gov/32482964/)

> *"Males with IFAP have an inexorable progression of corneal vascularization and loss of vision. Retinal vascular tortuosity may be another clinical sign of carrier status in females"* — [PMID: 15370546](https://pubmed.ncbi.nlm.nih.gov/15370546/)

### Finding 5 — Management is symptomatic; systemic acitretin gives partial benefit

No curative therapy exists; care is **symptomatic and multidisciplinary**. The systemic retinoid **acitretin (~1 mg/kg)** produced moderate improvement in cutaneous features and corneal erosions but **no change in alopecia or photophobia** over 6 months (**Khandpur 2005**). A separate case reported significant improvement of photophobia, corneal erosions, and neuropsychomotor development with **acitretin plus amniotic membrane transplantation** (**Höpker 2011**). Ocular-surface optimization employs aggressive lubrication, prophylactic antibiotics, punctal occlusion, tarsorrhaphy, and amniotic membrane transplantation; skin care relies on emollients and urea-based keratolytics (**Bin Rubaian 2023**). Orthopedic surgery (soft-tissue release, tendon lengthening) may be required for contractures (**Ghaznavi 2025**).

> *"A moderate response to acitretin therapy (1 mg/kg) administered for 6 months was observed, with improvement in cutaneous features and corneal erosions and no change in alopecia or photophobia"* — [PMID: 16268889](https://pubmed.ncbi.nlm.nih.gov/16268889/)

> *"After three months using systemic retinoid (Acitretina) and posterior amniotic membrane transplantation in the left eye, there was a significant improvement of photophobia, corneal erosions and neuropsychomotor development"* — [PMID: 21670910](https://pubmed.ncbi.nlm.nih.gov/21670910/)

### Finding 6 — Epidemiology, diagnosis, and variable expressivity of identical variants

IFAP is **very rare** (Orphanet ORPHA:2273); approximately **40 male cases** had been reported by 2018, and no precise prevalence/incidence figures exist. Diagnosis rests on recognition of the clinical triad plus ***MBTPS2* sequencing** (single-gene testing or whole-exome sequencing). Both **missense and splice-site** variants are pathogenic. A striking example of **variable expressivity** is the recurrent intronic variant **c.671-9T>G**, which caused typical IFAP with Olmsted-like keratoderma in one patient but IFAP *without* keratoderma in two others (**Wang 2014**); the intronic variant **c.970+5G>A** causes exon-7 skipping (**Chen 2023**). The BRESHECK acronym expands to **B**rain anomalies, **R**etardation of mentality/growth, **E**ctodermal dysplasia, **S**keletal malformations, **H**irschsprung disease, **E**ar deformity/deafness, **E**ye hypoplasia, **C**left palate, **C**ryptorchidism, and **K**idney dysplasia/hypoplasia.

> *"this mutation was previously reported in two cases of IFAP without keratoderma, which suggests clinical heterogeneicity of the same mutation in MBTPS2"* — [PMID: 24313295](https://pubmed.ncbi.nlm.nih.gov/24313295/)

> *"BRESHECK (brain anomalies, retardation of mentality and growth, ectodermal dysplasia, skeletal malformations, Hirschsprung disease, ear deformity and deafness, eye hypoplasia, cleft palate, cryptorchidism, and kidney dysplasia/hypoplasia) syndrome"* — [PMID: 24313295](https://pubmed.ncbi.nlm.nih.gov/24313295/)

> *"A total of 40 cases has been reported"* — [PMID: 28654459](https://pubmed.ncbi.nlm.nih.gov/28654459/)

### Finding 7 — Molecular pathway placement: S2P is the second protease in sequential SCAP–SREBP and ATF6 cleavage, linking lipogenesis to immunity

The SREBP pathway operates as a two-cut cascade: **SCAP** escorts SREBP from the ER to the Golgi, where **site-1 protease (S1P/MBTPS1)** makes the first cut, then **site-2 protease (S2P/MBTPS2)** makes the intramembrane cut that releases the active transcription-factor domain, upregulating lipid-biosynthesis genes (**Ozdemir & Rawson 2011**). The identical S1P/S2P machinery cleaves **ATF6** during ER stress. Importantly, the Scap–SREBP1–S1P/S2P cascade also spatiotemporally controls **NF-κB**: upon LPS stimulation, SREBP1 cleavage at the Golgi liberates IκBα for IKK phosphorylation and NF-κB activation, and inhibiting S2P diminishes LPS-induced NF-κB and inflammatory responses (**Fei et al. 2023**). This connects S2P loss to the **recurrent infections** seen in IFAP.

> *"when demand for lipid rises, SREBP travels from the endoplasmic reticulum to the Golgi apparatus where it is cleaved by two distinct proteases"* — [PMID: 20935466](https://pubmed.ncbi.nlm.nih.gov/20935466/)

> *"Loss of Scap or inhibition of S1P or S2P diminishes, while SREBP1 deficiency augments, LPS-induced NF-κB activation and subsequent inflammatory responses"* — [PMID: 37267109](https://pubmed.ncbi.nlm.nih.gov/37267109/)

### Finding 8 — Model organisms and deep evolutionary conservation of S2P

Site-2 protease is **evolutionarily ancient and conserved**. In *Drosophila melanogaster*, **dS2P** null mutants (and *dSREBP*/*dScap* mutants) have been isolated and display **lipid-auxotrophy phenotypes** rescuable by dietary lipids (**Ozdemir & Rawson 2011**). Mammalian S2P function was originally defined using **Chinese hamster ovary M19 cells**, which lack S2P and therefore require exogenous cholesterol/lipids; wild-type human *MBTPS2* complements this defect, whereas **IFAP patient variants fail to fully complement** (**Oeffner 2009**). No dedicated *Mbtps2* mouse or zebrafish IFAP disease model was retrieved in this investigation; the **CHO-M19 complementation assay** remains the principal functional model used to classify *MBTPS2* variant pathogenicity.

> *"we isolated Drosophila mutants null for dsrebp and others lacking site-2 protease (ds2p), the second of two Golgi-resident proteases that cleave dSREBP"* — [PMID: 20935466](https://pubmed.ncbi.nlm.nih.gov/20935466/)

> *"Wild-type MBTPS2 was able to complement the protease deficiency in Chinese hamster M19 cells"* — [PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/)

### Finding 9 — Ichthyosis follicularis is genetically heterogeneous; S2P-mutant fibroblast omics reveal a lipid/collagen signature

The ichthyosis-follicularis phenotype is **not specific to *MBTPS2***. Biallelic ***GJB2*** (connexin-26) mutations cause a distinct autosomal-recessive syndrome of ichthyosis follicularis + severe sensorineural hearing loss + punctate palmoplantar keratoderma (**Youssefian 2019, 2022**), and ***SREBF1*** variants cause autosomal-dominant IFAP that overlaps hereditary mucoepithelial dysplasia (HMD) — both broaden the differential diagnosis. *MBTPS2* is also allelic to **X-linked Olmsted syndrome** (contrasting with autosomal-dominant *TRPV3* Olmsted; **Duchatelet 2014**). **Omics profiling of S2P-mutant patient fibroblasts** (studied in the allelic OI type XIX context) revealed perturbations in **fatty-acid metabolism and collagen production** as a molecular signature of *MBTPS2* deficiency (**Lim 2021, 2023**).

> *"association of a new syndrome of an autosomal recessive disorder of ichthyosis follicularis, bilateral severe sensorineural hearing loss and punctate palmoplantar keratoderma with mutations in GJB2"* — [PMID: 30431684](https://pubmed.ncbi.nlm.nih.gov/30431684/)

---

## Mechanistic Model / Interpretation

The unifying model of IFAP Syndrome 1 is a **dose-dependent partial failure of regulated intramembrane proteolysis**. Site-2 protease sits at a metabolic and stress-signaling nexus: it is required both to activate **SREBP** (governing membrane lipid supply) and to activate **ATF6** (governing the ER's adaptive response to folding stress). Tissues with the highest demand for barrier lipids and epithelial renewal — the epidermis, hair follicle, and corneal/limbal epithelium — are the most vulnerable when S2P output falls, explaining the specificity of the IFAP triad despite the gene's ubiquitous expression.

```
Low sterol / lipid demand
        │
        ▼
 SCAP escorts SREBP  ER ──▶ Golgi
        │
        ▼
 S1P (MBTPS1) cleaves SREBP (cut 1, luminal)
        │
        ▼
 S2P (MBTPS2) cleaves SREBP (cut 2, INTRAMEMBRANE)  ◀── DEFECTIVE IN IFAP
        │
        ▼
 Active SREBP transcription factor → nucleus
        │
        ▼
 ↑ Cholesterol + fatty-acid biosynthesis genes
        │
   (parallel arm)
 ER stress → ATF6 → same S1P/S2P cleavage → UPR target genes  ◀── ALSO DEFECTIVE
```

**Causal chain.** Hypomorphic *MBTPS2* → reduced intramembrane cleavage of SREBP and ATF6 → **(a) deficient cholesterol/fatty-acid synthesis** → defective epidermal barrier lipids and abnormal keratinization (ichthyosis follicularis, keratoderma), abnormal hair-follicle differentiation (atrichia), and corneal/limbal epithelial failure (keratopathy → photophobia); and **(b) failure of the ATF6/UPR ER-stress response** → impaired handling of ER protein-folding load, contributing to cellular dysfunction and (with NF-κB dysregulation) recurrent infection. Upstream = loss of S2P proteolytic activity; downstream = tissue-specific differentiation and stress-response failures.

Two features of this model are clinically important. First, **residual activity predicts severity** — a graded relationship rather than an all-or-none one ([PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/)), which is why the same gene yields disorders ranging from isolated KFSD/IFAP to lethal BRESHECK. Second, the **S2P–NF-κB link** ([PMID: 37267109](https://pubmed.ncbi.nlm.nih.gov/37267109/)) provides a mechanistic explanation for the recurrent infections that are otherwise puzzling in a "keratinization" disorder, integrating the barrier defect with an intrinsic innate-immune signaling defect.

```
                 MBTPS2 (S2P) activity  ───────────────────────────►  high
   BRESHECK ◄──── lethal multisystem      IFAP full triad     mild/atypical
   (little residual activity)         (intermediate)        (more residual)
```

---

## Comprehensive Section-by-Section Report

### 1. Disease Information

**Overview.** IFAP Syndrome 1 is a rare congenital ectodermal disorder defined by the triad of ichthyosis follicularis, atrichia (alopecia), and photophobia. It is a multisystem genodermatosis: beyond the diagnostic triad, patients commonly show palmoplantar keratoderma, nail dystrophy, recurrent skin/respiratory infections, growth impairment, and (in more severe cases) neurodevelopmental and multi-organ anomalies.

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0100213 |
| OMIM (disease) | #308205 |
| OMIM (gene *MBTPS2*) | *300294 |
| Orphanet | ORPHA:2273 |
| HGNC | HGNC:7375 (MBTPS2) |
| Gene / locus | *MBTPS2*, Xp22.12 |
| ICD-10 (approx.) | Q80.8 (other congenital ichthyosis) |
| MeSH | Indexed under Ichthyosis / Genetic Skin Diseases (no unique D-term) |

**Synonyms / alternative names.** IFAP syndrome; Ichthyosis Follicularis–Alopecia–Photophobia syndrome; Ichthyosis Follicularis with Atrichia and Photophobia. The severe multisystem extension is **BRESHECK syndrome**. *Note:* **IFAP2 (OMIM #619016)** is a distinct **autosomal-dominant** form caused by *SREBF1* and overlapping hereditary mucoepithelial dysplasia (HMD) — this report focuses on the *MBTPS2* (X-linked) form.

**Source of information.** The information base is **disease-level aggregated** (case reports, small case series, and functional/molecular studies) rather than large EHR/individual-patient cohorts — reflecting the disease's extreme rarity (~40 reported male cases as of 2018; [PMID: 28654459](https://pubmed.ncbi.nlm.nih.gov/28654459/)).

### 2. Etiology

**Causal factor.** The primary cause is **genetic**: hypomorphic (partial loss-of-function) **missense and splice-site variants in *MBTPS2*** ([PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/)). No environmental or infectious cause initiates the disease.

**Genetic risk factors.** The causal variants are germline *MBTPS2* variants; because the gene is X-linked, **male sex (hemizygosity)** is the principal risk determinant. Residual protease activity (an intrinsic property of the specific variant) determines severity. No independent susceptibility loci or common-variant risk factors are described. Complete loss of function is presumed embryonic-lethal; only partial-function alleles are viable.

**Environmental risk / protective factors.** None established. There is no known diet, exposure, or lifestyle factor that causes, worsens, or protects against IFAP. Heat, low humidity, and bright light exacerbate the *symptoms* (xerosis, photophobia) but are not disease-modifying. In carrier **females**, favorably skewed X-inactivation can reduce or abolish manifestations ([PMID: 16720460](https://pubmed.ncbi.nlm.nih.gov/16720460/)).

**Modifier genes / stochastic factors.** Variable expressivity of *identical* variants (e.g., c.671-9T>G with vs without keratoderma; [PMID: 24313295](https://pubmed.ncbi.nlm.nih.gov/24313295/)) implies genetic modifiers and/or stochastic X-inactivation influence severity, but no specific modifier gene is identified.

**Gene–environment interactions.** None formally demonstrated. Given the mechanistic link between S2P and NF-κB-mediated innate immunity ([PMID: 37267109](https://pubmed.ncbi.nlm.nih.gov/37267109/)), infectious exposures may plausibly interact with the immune-signaling defect to drive recurrent infections, but this is inferential.

### 3. Phenotypes

Onset is **congenital/neonatal** for cutaneous and hair features; the triad is highly penetrant in affected males with **variable expressivity**. Course is **chronic and lifelong**; the keratopathy is **progressive**.

| Phenotype | Suggested HPO | Type | Onset / course | Frequency (males) |
|---|---|---|---|---|
| Ichthyosis follicularis / follicular hyperkeratosis (spiny papules) | HP:0008064 (Ichthyosis); HP:0007502 (Follicular hyperkeratosis) | Physical/skin sign | Congenital, stable–progressive | ~100% (defining) |
| Atrichia/alopecia scalp, eyebrows, eyelashes (non-scarring) | HP:0001596 (Alopecia); HP:0100840; HP:0000561 | Physical sign | Congenital/first year | ~100% (defining) |
| Photophobia | HP:0000613 | Symptom | Infancy, progressive | Majority (defining; may be absent, esp. females) |
| Corneal vascularization/scarring → vision loss | HP:0011495; HP:0200020; HP:0000559; HP:0000505 | Clinical sign | Infancy→childhood, **progressive** | Common in males |
| Palmoplantar keratoderma | HP:0000982 | Skin sign | Childhood | Subset (Olmsted-like overlap) |
| Nail dystrophy / pachyonychia | HP:0008404 | Sign | Childhood | Subset |
| Xerosis / dry skin | HP:0000958 | Symptom | Congenital | Common |
| Angular cheilitis / periorificial keratotic plaques | HP:0033052 | Sign | Childhood | Subset |
| Recurrent infections (skin/respiratory) | HP:0002719 | Sign | Infancy | Subset (severe cases) |
| Growth retardation / short stature | HP:0001510 | Sign | Childhood | Subset |
| Intellectual disability / developmental delay | HP:0001249 | Behavioral/neuro | Childhood | Subset (more in BRESHECK) |
| Joint contractures (rare) | HP:0034392 | Sign | Childhood, progressive | Rare ([PMID: 41458897](https://pubmed.ncbi.nlm.nih.gov/41458897/)) |
| BRESHECK extras (brain, Hirschsprung, ear/hearing, cleft palate, cryptorchidism, kidney dysplasia) | multiple | Congenital malformations | Congenital | Severe end only |

**Quality-of-life impact.** Substantial — chronic scaly/pruritic skin, disfiguring universal alopecia (psychosocial burden), progressive visual impairment/blindness impairing education and mobility, recurrent infections, and (in severe cases) intellectual disability and organ malformations. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease.

### 4. Genetic / Molecular Information

- **Causal gene:** ***MBTPS2*** (HGNC:7375; NCBI Gene 51360; UniProt Q9UHC9), Xp22.12; a ~520-aa polytopic membrane zinc metalloprotease (site-2 protease, S2P; M50 peptidase family, HExxH…LDG zinc-binding motif).
- **Variant classification (ACMG/AMP):** Reported variants are **Pathogenic/Likely Pathogenic** when supported by functional assays; CHO-M19 complementation provides PS3-level evidence. Splice/intronic variants often require mini-gene/cDNA validation to upgrade from VUS.
- **Variant types:** Predominantly **missense** (exchanging highly conserved residues; [PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/)); also **splice-site/intronic** — c.671-9T>G ([PMID: 24313295](https://pubmed.ncbi.nlm.nih.gov/24313295/)), c.970+5G>A → exon-7 skipping ([PMID: 36539961](https://pubmed.ncbi.nlm.nih.gov/36539961/)), and c.766G>A/p.Val256Leu in BRESHECK ([PMID: 34655156](https://pubmed.ncbi.nlm.nih.gov/34655156/)).
- **Allele frequency:** Pathogenic variants are private/ultra-rare; essentially absent from gnomAD (consistent with X-linked reproductive selection).
- **Origin:** **Germline**, X-linked; transmitted by carrier mothers or de novo. No somatic/cancer role.
- **Functional consequence:** **Hypomorphic (partial loss of function)** — residual activity inversely correlated with severity; complete LOF presumed lethal.
- **Modifier genes:** None identified; variable expressivity implicates modifiers + X-inactivation.
- **Epigenetics:** No disease-specific methylation/histone data; **X-chromosome inactivation** is the key epigenetic determinant of the mosaic carrier-female phenotype ([PMID: 16720460](https://pubmed.ncbi.nlm.nih.gov/16720460/)).
- **Chromosomal abnormalities:** None (point/splice mutations only; no recurrent CNV/translocation).
- **Allelic disorders:** IFAP ± BRESHECK, KFSD (OMIM #308800), X-linked Olmsted syndrome, and OI type XIX ([PMID: 33743732](https://pubmed.ncbi.nlm.nih.gov/33743732/)).

### 5. Environmental Information

No environmental, lifestyle, or infectious **etiological** factors are known. IFAP is entirely genetically determined. Low humidity, heat, and mechanical trauma exacerbate xerosis and follicular hyperkeratosis; bright light exacerbates photophobia. Recurrent infections are a *consequence* of the disorder (barrier defect + impaired S2P/NF-κB innate immunity), not an environmental cause. One report links IFAP to Hodgkin lymphoma ([PMID: 28654459](https://pubmed.ncbi.nlm.nih.gov/28654459/)), raising but not establishing a possible malignancy predisposition.

### 6. Mechanism / Pathophysiology

**Molecular pathways.** SCAP–SREBP lipogenesis (S1P/MBTPS1 then **S2P/MBTPS2** cleave SREBP in the Golgi; [PMID: 20935466](https://pubmed.ncbi.nlm.nih.gov/20935466/)); ATF6 branch of the UPR (same S1P/S2P machinery); NF-κB innate-immune signaling ([PMID: 37267109](https://pubmed.ncbi.nlm.nih.gov/37267109/)). KEGG: SREBP/lipid biosynthesis; Protein processing in ER.

**Cellular processes.** Keratinocyte terminal differentiation and lamellar-body lipid secretion; corneal **limbal stem cell** maintenance; hair-follicle morphogenesis; ER-stress adaptation.

**Protein dysfunction.** Point/splice mutations reduce catalytic/structural function of the membrane metalloprotease (partial LOF; not aggregation). In vitro, p.Val256Leu produced *"impaired cell growth in cholesterol-depleted media, attenuated activation of the sterol regulatory element-binding protein pathway, and failure to activate the endoplasmic reticulum stress response pathway"* ([PMID: 34655156](https://pubmed.ncbi.nlm.nih.gov/34655156/)).

**Metabolic changes.** Deficient cholesterol/fatty-acid (barrier lipid) synthesis. **CHEBI:** cholesterol (CHEBI:16113), sterol (CHEBI:15889), fatty acid (CHEBI:35366), zinc(2+) (CHEBI:29105).

**Immune involvement.** Recurrent infections; mechanistic link via S2P→NF-κB ([PMID: 37267109](https://pubmed.ncbi.nlm.nih.gov/37267109/)) and barrier failure. Not autoimmune.

**Tissue-damage mechanisms.** Corneal neovascularization and conjunctivalization from **limbal stem cell dysfunction**; epidermal barrier disruption.

**GO / CL suggestions.** SREBP signaling GO:0032933; response to ER stress GO:0034976; metalloendopeptidase activity GO:0004222; cholesterol biosynthetic process GO:0006695; keratinocyte differentiation GO:0030216. Cells: keratinocyte (CL:0000312), corneal epithelial cell (CL:0000575), fibroblast (CL:0000057).

**Molecular profiling (omics).** No transcriptomic/proteomic/metabolomic dataset specific to IFAP itself. The nearest data are **omics of S2P-mutant patient fibroblasts** (allelic OI type XIX), revealing **perturbations in fatty-acid metabolism and collagen production** ([PMID: 34093655](https://pubmed.ncbi.nlm.nih.gov/34093655/); [PMID: 37305034](https://pubmed.ncbi.nlm.nih.gov/37305034/)) — consistent with the SREBP-lipogenesis mechanism. IHC in the *SREBF1* form showed reduced nuclear SREBP1 translocation with IL-17A/S100A8 upregulation ([PMID: 39912473](https://pubmed.ncbi.nlm.nih.gov/39912473/)).

### 7. Anatomical Structures Affected

| Level | Structure (UBERON/CL/GO) | Involvement |
|---|---|---|
| Organ | Skin (UBERON:0002097); hair (UBERON:0001037) | Primary — ichthyosis follicularis, atrichia |
| Organ | Cornea (UBERON:0000964) / limbus / conjunctiva | Primary — keratopathy, limbal stem-cell failure |
| Organ | Nail (UBERON:0001705) | Secondary — dystrophy |
| Organ (severe) | Brain (UBERON:0000955), kidney (UBERON:0002113), colon/ENS, ear, palate, gonads, skeleton | BRESHECK multisystem |
| Tissue | Stratified squamous epithelium | Primary target |
| Cell | Keratinocyte (CL:0000312); corneal epithelial cell (CL:0000575); limbal stem cell | Primary |
| Subcellular | ER (GO:0005783), Golgi (GO:0005794), integral membrane (GO:0016021) | Site of S2P dysfunction |

**Lateralization.** Cutaneous and ocular disease is **bilateral/symmetric** in affected males; **female carriers** show **asymmetric, Blaschko-linear (mosaic)** distribution due to lyonization.

### 8. Temporal Development

- **Onset:** **Congenital/neonatal** for skin/hair; **photophobia/keratopathy emerge in infancy** and progress. Onset pattern chronic/insidious.
- **Progression:** Cutaneous features relatively stable-to-slowly progressive; **ocular keratopathy is inexorably progressive** — *"Males with IFAP have an inexorable progression of corneal vascularization and loss of vision"* ([PMID: 15370546](https://pubmed.ncbi.nlm.nih.gov/15370546/)). Chronic/lifelong; no spontaneous remission. Rare progressive musculoskeletal contractures ([PMID: 41458897](https://pubmed.ncbi.nlm.nih.gov/41458897/)).
- **Critical periods:** Infancy/early childhood is the key window for ocular-surface protection to preserve vision; the neonatal period is critical in severe/BRESHECK cases (thermoregulation, infection, organ malformations).

### 9. Inheritance and Population

- **Inheritance:** **X-linked recessive** (*MBTPS2*, Xp22.12); affected males inherit from carrier mothers or de novo; no male-to-male transmission; all daughters of an affected male are obligate carriers.
- **Penetrance / expressivity:** High penetrance in hemizygous males; **markedly variable expressivity**, even for identical alleles ([PMID: 24313295](https://pubmed.ncbi.nlm.nih.gov/24313295/)).
- **Epidemiology:** Ultra-rare (Orphanet ORPHA:2273); **~40 reported male cases** by 2018 ([PMID: 28654459](https://pubmed.ncbi.nlm.nih.gov/28654459/)); no reliable prevalence/incidence.
- **Anticipation:** Not applicable (no repeat expansion). **Founder effects/consanguinity:** none established (recurrent variants reflect mutational hotspots, not founders). **Carrier frequency:** not estimable (private variants, absent from gnomAD). **Germline mosaicism:** plausible but not well documented; de novo variants reported.
- **Demographics:** Reported worldwide (Australia, China, India, Brazil, Saudi Arabia, Korea, etc.) with no ethnic clustering; **strongly male-predominant** sex ratio; rare, generally milder female cases (including an atypical female with severe contractures and no photophobia, [PMID: 41458897](https://pubmed.ncbi.nlm.nih.gov/41458897/)). A large Australian kindred clearly demonstrated X-linked transmission ([PMID: 19689518](https://pubmed.ncbi.nlm.nih.gov/19689518/)).

### 10. Diagnostics

- **Clinical diagnosis:** Recognition of the triad (follicular ichthyosis + congenital atrichia + photophobia).
- **Skin biopsy/histopathology:** Orthokeratotic hyperkeratosis, acanthosis, and **follicular plugging** ([PMID: 41458897](https://pubmed.ncbi.nlm.nih.gov/41458897/)); reduced/absent hair follicles.
- **Ophthalmology:** Slit-lamp (corneal vascularization, epithelial defects, pannus); **anterior-segment OCT** (abnormal hyperreflective epithelium indicating **limbal stem cell dysfunction**; [PMID: 32482964](https://pubmed.ncbi.nlm.nih.gov/32482964/)); carrier mothers may show retinal vascular tortuosity.
- **Genetic testing (confirmatory):** ***MBTPS2* single-gene sequencing** or **WES/WGS**; ichthyosis/ectodermal-dysplasia panels. Splice/intronic VUS require **cDNA/mini-gene assays** ([PMID: 36539961](https://pubmed.ncbi.nlm.nih.gov/36539961/)); CHO-M19 complementation assesses residual function ([PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/)). CMA/karyotype/FISH generally uninformative.
- **Clinical criteria:** No formal consensus criteria; diagnosis is triad + molecular confirmation.
- **Differential diagnosis (IF is genetically heterogeneous):** *SREBF1*-IFAP / HMD — **autosomal dominant** ([PMID: 33742461](https://pubmed.ncbi.nlm.nih.gov/33742461/); [PMID: 41492963](https://pubmed.ncbi.nlm.nih.gov/41492963/)); *GJB2* — **autosomal recessive** IF + **severe SNHL** + punctate PPK ([PMID: 30431684](https://pubmed.ncbi.nlm.nih.gov/30431684/); [PMID: 35396755](https://pubmed.ncbi.nlm.nih.gov/35396755/)); KFSD; Olmsted syndrome (X-linked *MBTPS2* vs AD *TRPV3*, [PMID: 24452206](https://pubmed.ncbi.nlm.nih.gov/24452206/)); other congenital ichthyoses/ectodermal dysplasias.
- **Screening:** No newborn/population screening. **Cascade carrier testing** of at-risk female relatives; prenatal/PGT when familial variant is known.

### 11. Outcome / Prognosis

- **Survival/mortality:** Isolated (non-BRESHECK) IFAP is compatible with near-normal life expectancy; **BRESHECK** carries high infant/childhood morbidity and mortality from brain/kidney anomalies, infections, and marrow involvement ([PMID: 34655156](https://pubmed.ncbi.nlm.nih.gov/34655156/)). No formal survival statistics.
- **Morbidity/disability:** Dominated by **progressive visual impairment/blindness**, chronic skin disease, recurrent infections, and, in severe cases, intellectual disability and organ dysfunction; rare disabling contractures.
- **Complications:** Corneal scarring/blindness, secondary infections, growth failure; possible malignancy (single Hodgkin lymphoma case, [PMID: 28654459](https://pubmed.ncbi.nlm.nih.gov/28654459/)).
- **Recovery potential:** No cure; features largely irreversible, though skin and corneal erosions can partially improve with therapy.
- **Prognostic factors:** **Residual MBTPS2 activity / genotype severity** is the principal determinant ([PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/)); BRESHECK features predict poor outcome. No validated prognostic biomarkers.

### 12. Treatment

No curative/disease-modifying therapy; **symptomatic, multidisciplinary** (dermatology, ophthalmology, genetics ±). Suggested NCIT terms in parentheses.

| Modality | Intervention | Evidence |
|---|---|---|
| Skin care | Emollients, urea keratolytics (NCIT: Emollient) | [PMID: 38089015](https://pubmed.ncbi.nlm.nih.gov/38089015/) |
| Systemic retinoid | **Acitretin ~1 mg/kg** (NCIT:C29496) — partial cutaneous/corneal benefit; no effect on alopecia/photophobia | [PMID: 16268889](https://pubmed.ncbi.nlm.nih.gov/16268889/); [PMID: 19689518](https://pubmed.ncbi.nlm.nih.gov/19689518/) |
| Ocular surface | Lubrication, prophylactic antibiotics, punctal occlusion, tarsorrhaphy | [PMID: 32482964](https://pubmed.ncbi.nlm.nih.gov/32482964/) |
| Ocular surgery | **Amniotic membrane transplantation** (+ acitretin) | [PMID: 21670910](https://pubmed.ncbi.nlm.nih.gov/21670910/) |
| Orthopedic | Soft-tissue release, Achilles lengthening for contractures | [PMID: 41458897](https://pubmed.ncbi.nlm.nih.gov/41458897/) |
| Supportive | Infection management, low-vision rehab, growth/nutrition, genetic counseling | Multiple |

**Advanced/experimental therapies.** No gene, cell, RNA, or targeted therapies are approved or in trials; no NCT-registered IFAP-specific interventional trials identified. Pharmacogenomics not applicable. Genotype (residual activity) may guide severity expectation/counseling, but no genotype-directed drug exists. Retinoid toxicity (mucocutaneous, hepatic, lipid, skeletal) and teratogenicity require monitoring.

### 13. Prevention

- **Primary prevention:** Not possible (monogenic germline). **Genetic counseling** and reproductive options (carrier testing, prenatal diagnosis, PGT-M) for at-risk families are the mainstay.
- **Secondary prevention:** Early ophthalmologic surveillance and **ocular-surface protection in infancy** to slow corneal vascularization and preserve vision; early skin care.
- **Tertiary prevention:** Infection prophylaxis/prompt treatment, vision rehabilitation, nutritional/growth support, management of BRESHECK complications.
- **Screening:** Cascade genetic testing of relatives; no population/newborn screening. Routine vaccination advisable given infection risk. Behavioral/public-health/environmental interventions are not applicable to causation.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** MBTPS2 is deeply conserved. Human *MBTPS2* (Taxon 9606); mouse *Mbtps2* (Taxon 10090; NCBI Gene 270669); *Drosophila* *S2P* (Taxon 7227); hamster ortholog underlies the classic M19 mutant cell line (Taxon 10029).
- **Natural disease in other species:** No naturally occurring IFAP-equivalent disease is catalogued in OMIA for companion animals or livestock; veterinary relevance is minimal.
- **Comparative biology / conservation:** The S2P–SREBP lipid-regulatory axis is conserved from insects to mammals; *Drosophila ds2p* nulls show lipid-auxotrophy phenotypes ([PMID: 20935466](https://pubmed.ncbi.nlm.nih.gov/20935466/)), underscoring conserved essentiality.
- **Transmission:** Not applicable (non-infectious, non-zoonotic).

### 15. Model Organisms

| Model | Type | Utility | Limitation |
|---|---|---|---|
| **CHO-M19 cells** | In vitro (mammalian) | **Principal functional assay** — complementation classifies variant pathogenicity/severity ([PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/); [PMID: 34655156](https://pubmed.ncbi.nlm.nih.gov/34655156/)) | Does not reproduce tissue-level phenotype |
| **Patient fibroblasts** | In vitro (human) | Omics reveal fatty-acid/collagen signature; splicing/expression studies ([PMID: 34093655](https://pubmed.ncbi.nlm.nih.gov/34093655/); [PMID: 37305034](https://pubmed.ncbi.nlm.nih.gov/37305034/)) | Not a whole-organism model |
| ***Drosophila* dS2P / dSREBP nulls** | Invertebrate genetic | Conserved lipid-auxotrophy; dietary-lipid rescue ([PMID: 20935466](https://pubmed.ncbi.nlm.nih.gov/20935466/)) | Does not model skin/eye phenotype |

**Gap:** No dedicated *Mbtps2* mouse or zebrafish **IFAP disease model** was identified; whole-animal null models are expected to be lethal. Mechanistic inference relies on cellular complementation and orthologous invertebrate genetics. **Resources:** MGI (Mbtps2), FlyBase (S2P), Cellosaurus (M19/CHO), plus patient-derived cells.

---

## Evidence Base

| PMID | Contribution | Role |
|---|---|---|
| [19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/) | Gene identification; CHO-M19 complementation; activity–severity correlation | **Foundational** (F001, F002, F008) |
| [34655156](https://pubmed.ncbi.nlm.nih.gov/34655156/) | BRESHECK variant impairs SREBP + abolishes UPR | Dual mechanism (F002, F003) |
| [33743732](https://pubmed.ncbi.nlm.nih.gov/33743732/) | *MBTPS2* allelic disorder spectrum; RIP function | Supports (F002, F003) |
| [38089015](https://pubmed.ncbi.nlm.nih.gov/38089015/) | Defines triad & inheritance; skin care | Supports (F003, F005) |
| [16720460](https://pubmed.ncbi.nlm.nih.gov/16720460/) | X-inactivation → carrier mosaicism | Supports (F003) |
| [32482964](https://pubmed.ncbi.nlm.nih.gov/32482964/) | Limbal stem-cell dysfunction (AS-OCT) | **Key ocular** (F004) |
| [15370546](https://pubmed.ncbi.nlm.nih.gov/15370546/) | Progressive corneal vascularization; carrier sign | Supports (F004) |
| [16268889](https://pubmed.ncbi.nlm.nih.gov/16268889/) | Acitretin partial response | **Key treatment** (F005) |
| [21670910](https://pubmed.ncbi.nlm.nih.gov/21670910/) | Acitretin + amniotic membrane benefit | Supports (F005) |
| [24313295](https://pubmed.ncbi.nlm.nih.gov/24313295/) | Variable expressivity; BRESHECK acronym | Supports (F006) |
| [28654459](https://pubmed.ncbi.nlm.nih.gov/28654459/) | ~40 cases; Hodgkin lymphoma report | Epidemiology (F006) |
| [36539961](https://pubmed.ncbi.nlm.nih.gov/36539961/) | Intronic splice variant → exon-7 skipping | Diagnostics (F006) |
| [20935466](https://pubmed.ncbi.nlm.nih.gov/20935466/) | Two-protease SREBP cascade; *Drosophila* dS2P | Pathway/model (F007, F008) |
| [37267109](https://pubmed.ncbi.nlm.nih.gov/37267109/) | S2P–NF-κB immune link | **Mechanistic** (F007) |
| [30431684](https://pubmed.ncbi.nlm.nih.gov/30431684/) | *GJB2* ichthyosis follicularis (DDx) | Differential (F009) |
| [34093655](https://pubmed.ncbi.nlm.nih.gov/34093655/); [37305034](https://pubmed.ncbi.nlm.nih.gov/37305034/) | S2P-mutant fibroblast omics (lipid/collagen) | Molecular signature (F009) |
| [33742461](https://pubmed.ncbi.nlm.nih.gov/33742461/); [41492963](https://pubmed.ncbi.nlm.nih.gov/41492963/); [39912473](https://pubmed.ncbi.nlm.nih.gov/39912473/) | *SREBF1*-IFAP / HMD overlap | Differential/heterogeneity |
| [24452206](https://pubmed.ncbi.nlm.nih.gov/24452206/) | *TRPV3* vs *MBTPS2* Olmsted | Differential |
| [19689518](https://pubmed.ncbi.nlm.nih.gov/19689518/) | Large Australian kindred; X-linked; acitretin | Inheritance/treatment |
| [41458897](https://pubmed.ncbi.nlm.nih.gov/41458897/) | Atypical female; contractures; orthopedic surgery | Phenotype expansion |
| [35396755](https://pubmed.ncbi.nlm.nih.gov/35396755/) | *GJB2* ichthyosis follicularis syndromes | Differential |

---

## Supported and Refuted Hypotheses

**Supported:**
1. IFAP1 is caused by partial LOF of *MBTPS2*, with residual activity inversely proportional to severity ([PMID: 19361614](https://pubmed.ncbi.nlm.nih.gov/19361614/); [PMID: 34655156](https://pubmed.ncbi.nlm.nih.gov/34655156/)).
2. Photophobia results from a progressive keratopathy due to **limbal stem-cell dysfunction**, not a primary retinal defect ([PMID: 15370546](https://pubmed.ncbi.nlm.nih.gov/15370546/); [PMID: 32482964](https://pubmed.ncbi.nlm.nih.gov/32482964/)).
3. Acitretin partially improves skin/corneal features but not alopecia/photophobia ([PMID: 16268889](https://pubmed.ncbi.nlm.nih.gov/16268889/); [PMID: 21670910](https://pubmed.ncbi.nlm.nih.gov/21670910/)).

**Refuted / not supported:**
- IFAP is **not** caused by environmental or infectious agents; no environmental or protective genetic modifiers are proven.
- No animal model fully recapitulates the triad; claims of a definitive mouse/zebrafish IFAP model are **not supported** by retrieved literature.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** With ~40 reported cases, all clinical claims derive from case reports/series; no controlled trials, no formal prevalence/incidence, and no validated QoL metrics exist.
2. **No animal disease model.** No *Mbtps2* mouse or zebrafish IFAP model was identified; mechanistic inference relies on CHO-M19 cells, patient fibroblasts, and *Drosophila* — none of which reproduce the skin/eye phenotype.
3. **Genotype–phenotype resolution is incomplete.** Although residual activity correlates with severity, identical variants can produce divergent phenotypes ([PMID: 24313295](https://pubmed.ncbi.nlm.nih.gov/24313295/)), implying unidentified modifiers or stochastic X-inactivation effects.
4. **Treatment evidence is anecdotal.** Acitretin benefit rests on individual cases; optimal dosing, long-term outcomes, and ocular-therapy standardization are undefined.
5. **Uncertain associations.** The single Hodgkin-lymphoma report does not establish a malignancy risk; the S2P–NF-κB immune link is mechanistically plausible but not clinically proven in IFAP patients.
6. **Citation caveat.** One omics snippet ([PMID: 34093655](https://pubmed.ncbi.nlm.nih.gov/34093655/)) was flagged as title-derived during validation; the omics conclusion should be treated as supported primarily by the paired [PMID: 37305034](https://pubmed.ncbi.nlm.nih.gov/37305034/).

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional *Mbtps2* hypomorphic mouse** (epidermis- and cornea-specific) to establish the first mammalian IFAP disease model and test whether residual-activity gradients recapitulate the human severity continuum.
2. **Single-cell / spatial transcriptomics of IFAP skin and limbus** to define cell-type-specific SREBP/ATF6 target-gene failure and confirm limbal stem-cell depletion at molecular resolution.
3. **Systematic variant-function mapping** in the CHO-M19 assay for all reported *MBTPS2* variants to build a quantitative activity-vs-severity calibration usable for prognostic counseling.
4. **Prospective natural-history registry** (multinational, given rarity) capturing standardized ophthalmic, dermatologic, and QoL endpoints.
5. **Pilot limbal stem-cell / amniotic-membrane protocols** with pre-specified visual-acuity endpoints to move ocular management beyond anecdote.
6. **Lipidomic/metabolomic profiling** of patient skin and serum to test whether topical lipid replacement (cholesterol/fatty-acid supplementation) can bypass the SREBP defect — a mechanistically rational, low-risk therapeutic hypothesis.
7. **Evaluate innate-immune function** (NF-κB responsiveness) in patient monocytes to determine whether recurrent infections warrant prophylactic strategies.

---

*Report compiled from 9 confirmed findings and 28 reviewed publications. Evidence classes: human clinical (case reports/series), in vitro (CHO-M19 complementation, mini-gene/splicing assays, IHC), invertebrate model (Drosophila), and computational/omics. PMIDs cited inline.*


## Artifacts

- [OpenScientist final report](IFAP_Syndrome_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](IFAP_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 12 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100213` (4 mentions) - the report calls it "MONDO"; MONDO calls it **IFAP syndrome 1, with or without BRESHECK syndrome**
- `HP:0033052` (1 mention) - the report calls it "Angular cheilitis / periorificial keratotic plaques"; HP calls it **Non-epileptic seizure**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C29496` (1 mention), reported as "Acitretin ~1 mg/kg" - NCIT does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016021` (GO_0016021) (1 mention) - replaced by `GO:0016020`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008404` (1 mention) - the report calls it "Nail dystrophy / pachyonychia"; HP calls it **Nail dystrophy**
- `HP:0000958` (1 mention) - the report calls it "Xerosis / dry skin"; HP calls it **Dry skin**
- `HP:0002719` (1 mention) - the report calls it "Recurrent infections (skin/respiratory)"; HP calls it **Recurrent infections**
- `HP:0001510` (1 mention) - the report calls it "Growth retardation / short stature"; HP calls it **Growth delay**, and lists "Growth retardation" among its other names
- `HP:0001249` (1 mention) - the report calls it "Intellectual disability / developmental delay"; HP calls it **Intellectual disability**
- `HP:0034392` (1 mention) - the report calls it "Joint contractures (rare)"; HP calls it **Joint contracture**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.