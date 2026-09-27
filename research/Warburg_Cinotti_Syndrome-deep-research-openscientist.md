---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-30T18:31:42.994570'
end_time: '2026-08-30T19:04:15.714839'
duration_seconds: 1952.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Warburg-Cinotti Syndrome
  mondo_id: ''
  category: Connective Tissue
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 55
  verified: 52
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 31
  labels_matching: 20
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0032579
    reported_labels:
    - MONDO
    ontology_label: warburg-cinotti syndrome
  - term_id: EFO:0010166
    reported_labels:
    - EFO
    ontology_label: Warburg-Cinotti syndrome
  - term_id: NCIT:C62035
    reported_labels:
    - 'Potent DDR1/2 inhibitor (PMID: 18938156)'
    ontology_label: Imatinib
  - term_id: NCIT:C48375
    reported_labels:
    - 'Potent DDR1/2 inhibitor (PMID: 18938156)'
    ontology_label: Nilotinib
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Warburg_Cinotti_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Warburg_Cinotti_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Warburg-Cinotti Syndrome
- **MONDO ID:**  (if available)
- **Category:** Connective Tissue

## Research Objectives

Please provide a comprehensive research report on **Warburg-Cinotti Syndrome** covering all of the
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

# Warburg-Cinotti Syndrome: Comprehensive Disease Characteristics Report

**Disease Name:** Warburg-Cinotti Syndrome (WCS)
**MONDO ID:** MONDO:0032579
**OMIM:** #618175
**Category:** Connective Tissue
**Report compiled:** 2026-08-30 (5-iteration autonomous investigation; 11 confirmed findings; 25 papers reviewed)

---

## Summary

Warburg-Cinotti syndrome (WCS; MONDO:0032579; OMIM #618175) is an **ultra-rare, autosomal-dominant connective-tissue disorder** caused by recurrent **activating (gain-of-function) germline missense variants** in the collagen receptor tyrosine kinase gene **DDR2** (discoidin domain receptor tyrosine kinase 2; OMIM 191311). Only two recurrent hotspot variants have been reported to date — **c.1829T>C (p.Leu610Pro)** and **c.2219A>G (p.Tyr740Cys)** — and both render the receptor **constitutively autophosphorylated independent of its collagen ligand**, bypassing the normal autoinhibitory constraints on kinase activity ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/); [PMID: 41259339](https://pubmed.ncbi.nlm.nih.gov/41259339/)).

Clinically, WCS is a **progressive fibro-proliferative disorder**. The classic tetrad comprises **progressive corneal neovascularization, keloid formation, chronic skin ulcers with wasting of subcutaneous tissue, finger flexion contractures, and acro-osteolysis** ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)). Curated Human Phenotype Ontology annotations (35 features derived from OMIM:618175 via the Monarch Initiative) reveal a much broader, multisystem picture involving craniofacial dysmorphism (narrow nose, long face, posteriorly rotated ears), the ocular surface (corneal neovascularization, symblepharon, limbal stem-cell deficiency), the ear (conductive hearing loss, cholesteatoma), the skin (thin skin, poor wound healing), the skeleton (osteolysis of phalanges, joint contractures), and the respiratory system (pneumothorax). Mechanistically, constitutively active DDR2 in **fibroblasts** hyperactivates **ERK1/2 and NF-κB signaling** and drives **matrix-metalloproteinase (MMP-1/2/9/13) and MT1-MMP (MMP-14)-mediated extracellular-matrix remodeling**, producing the fibrosis, neovascularization, and tissue destruction that characterize the disease ([PMID: 28270508](https://pubmed.ncbi.nlm.nih.gov/28270508/); [PMID: 25733533](https://pubmed.ncbi.nlm.nih.gov/25733533/)).

Because WCS is fundamentally a **kinase-activation disease**, DDR2-inhibiting tyrosine kinase inhibitors are a mechanistically rational therapeutic strategy. The BCR-ABL inhibitor **dasatinib abolishes mutant DDR2 autophosphorylation in patient fibroblasts** ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)), and **imatinib, nilotinib, and dasatinib are all potent DDR1/DDR2 inhibitors** ([PMID: 18938156](https://pubmed.ncbi.nlm.nih.gov/18938156/)), making them repurposing candidates — although no clinical trial and no gain-of-function animal model of WCS has yet been reported. Notably, DDR2 is **allelic to a mechanistically opposite disorder**: biallelic loss-of-function DDR2 variants cause the autosomal-recessive skeletal dysplasia SMED-SL (spondylo-meta-epiphyseal dysplasia, short limb–abnormal calcification type; OMIM 271665) ([PMID: 24725993](https://pubmed.ncbi.nlm.nih.gov/24725993/); [PMID: 36720430](https://pubmed.ncbi.nlm.nih.gov/36720430/)).

---

## Section 1 — Disease Information

**Overview.** Warburg-Cinotti syndrome is a progressive connective-tissue disorder defined by simultaneous fibro-proliferation (keloids, corneal pannus/neovascularization) and tissue destruction (chronic skin ulcers, subcutaneous wasting, acro-osteolysis). It is caused by gain-of-function activation of a collagen-sensing receptor tyrosine kinase, positioning it at the intersection of extracellular-matrix biology and kinase-signaling disease.

**Key identifiers (verified via EBI OLS4 MONDO ontology query; Finding F010):**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0032579 |
| OMIM | #618175 |
| UMLS | C5193019 |
| MedGen | 1677486 |
| GARD | 0015007 |
| EFO | EFO:0010166 |
| Orphanet | **No dedicated entry** (as of query) |
| ICD-10 / ICD-11 | No specific code identified |
| MeSH | No dedicated descriptor identified |

**Synonyms / alternative names:** Warburg-Cinotti syndrome; abbreviation **WRCN** (MONDO synonym).

**Information source type.** Given fewer than ~10 reported individuals worldwide, all information is derived from **aggregated disease-level resources** (OMIM, MONDO, HPO/Monarch) and **individual case reports/case series** — not from large EHR or registry datasets. The foundational cohort is 6 affected individuals from 4 families ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)).

---

## Section 2 — Etiology

**Primary cause (genetic).** WCS is a **monogenic, autosomal-dominant** disorder caused by heterozygous activating missense variants in **DDR2**. Two recurrent variants account for all molecularly confirmed classic cases: **p.Leu610Pro** and **p.Tyr740Cys** ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)). A novel maternally inherited variant was reported in a neonatal case ([PMID: 41778429](https://pubmed.ncbi.nlm.nih.gov/41778429/)), indicating the mutational spectrum may be broader than the two original hotspots.

**Genetic risk factors.** The causal variants are themselves the risk determinant; there are no reported susceptibility loci or modifier genes. Both **de novo** and **inherited** transmission are documented — a proven de novo variant arose in a mother who then transmitted it to two children ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)).

**Environmental risk factors.** No environmental cause is required for disease. However, **local trauma appears to provoke and accelerate lesions**: a 7-year-old developed a gelatinous vascularized conjunctival mass after ocular trauma that recurrently regrew and invaded the entire cornea despite repeated surgery ([PMID: 39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/)). This mirrors the keloid biology of WCS, in which the skin overreacts to injury.

**Protective factors.** None identified (genetic or environmental). Given the trauma-provocation pattern, **avoidance of unnecessary trauma/surgery** to affected surfaces may be practically protective, though this is inferential.

**Gene-environment interaction.** The plausible model is that a constitutively active DDR2 receptor lowers the threshold for a pathological wound-healing/ECM-remodeling response, so that ordinary mechanical injury triggers exaggerated, self-perpetuating fibro-proliferation and neovascularization.

---

## Section 3 — Phenotypes

WCS is a multisystem disorder. The **classic clinical tetrad/pentad** ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/); [PMID: 41259339](https://pubmed.ncbi.nlm.nih.gov/41259339/)):

- **Progressive corneal neovascularization** (HP:0011496) — ocular surface; progressive; trauma-provoked
- **Keloid formation** — skin; progressive fibro-proliferation
- **Chronic skin ulcers / poor wound healing** (HP:0001058) — skin; chronic
- **Wasting of subcutaneous tissue** — skin/subcutis; progressive
- **Flexion contractures of the fingers** (HP:0012785) — musculoskeletal; progressive
- **Acro-osteolysis / osteolytic phalangeal defects** (HP:0009771) — skeletal; progressive

**Curated HPO spectrum with frequencies** (Monarch/HPOA, 35 annotations derived from OMIM:618175; Finding F011):

| Phenotype | HPO term | Frequency |
|-----------|----------|-----------|
| Narrow nose | HP:0000460 | 100% |
| Narrow palpebral fissure | HP:0045025 | 100% |
| Visual impairment | HP:0000505 | 75% |
| Joint swelling | HP:0001386 | 67% |
| Thin skin | HP:0000963 | 67% |
| Long face | HP:0000276 | 67% |
| Posteriorly rotated ears | HP:0000358 | 60% |
| Osteolytic defects of phalanges of hand | HP:0009771 | 60% |
| Underdeveloped nasal alae | HP:0000430 | 50% |
| Hypoplasia of ear cartilage | HP:0100720 | 40% |
| Conductive hearing impairment | HP:0000405 | 40% |
| High palate | HP:0000218 | 33% |
| Retinal dystrophy | HP:0000556 | 33% |
| Pneumothorax | HP:0002107 | 33% |
| Wrist flexion contracture | HP:0001239 | 33% |
| Cholesteatoma | HP:0009797 | 20% |
| Atresia of external auditory canal | HP:0000413 | 20% |
| Dental crowding / gingival overgrowth / follicular hyperkeratosis / sterile abscess / short chin / ankle & elbow contracture | (various) | ~17% each |
| Corneal neovascularization | HP:0011496 | (annotated, no freq) |
| Symblepharon | HP:0430007 | (annotated, no freq) |
| Limbal stem cell deficiency | HP:0032107 | (annotated, no freq) |
| Decreased corneal thickness | HP:0100689 | (annotated, no freq) |
| Poor wound healing | HP:0001058 | (annotated, no freq) |
| Erythema | HP:0010783 | (annotated, no freq) |
| Epicanthus / Blepharophimosis / Low-set ears / Midface retrusion | HP:0000286 / HP:0000581 / HP:0000369 / HP:0011800 | (annotated, no freq) |

**Onset, severity, progression.** Onset spans **childhood to adulthood**, with a documented **neonatal presentation** (respiratory distress from choanal abnormalities) at the earliest extreme ([PMID: 41778429](https://pubmed.ncbi.nlm.nih.gov/41778429/); [PMID: 39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/)). Most core features are **progressive**, and expressivity is **variable** even within families.

**Quality-of-life impact.** No formal EQ-5D/SF-36 data exist. Inferred impact is substantial: progressive corneal opacification/neovascularization threatens vision (visual impairment in 75%), finger contractures and acro-osteolysis impair hand function and dexterity, chronic non-healing ulcers cause pain and infection risk, and conductive hearing loss/cholesteatoma affect hearing.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** **DDR2** — discoidin domain receptor tyrosine kinase 2; HGNC:2731; NCBI Gene ID **4921**; OMIM 191311; chromosome 1q23.3. DDR2 is a **non-integrin, collagen-activated receptor tyrosine kinase**.

**Pathogenic variants (WCS, gain of function):**

| Variant (cDNA) | Protein | Type | Origin | Consequence |
|----------------|---------|------|--------|-------------|
| c.1829T>C | p.Leu610Pro | Missense | Germline (de novo or inherited, AD) | Gain of function — constitutive autophosphorylation |
| c.2219A>G | p.Tyr740Cys | Missense | Germline (AD) | Gain of function — constitutive autophosphorylation |
| Novel (neonatal) | (maternally inherited) | Missense | Germline | Reported; spectrum-expanding ([PMID: 41778429](https://pubmed.ncbi.nlm.nih.gov/41778429/)) |

**Classification.** The two recurrent variants are **pathogenic** (recurrent, functionally validated, segregating; consistent with ACMG PS1/PS3/PM1/PP1 lines of evidence). Allele frequency in population databases is effectively **absent** (private, disease-causing).

**Functional consequence — gain of function.** Patient fibroblasts show **increased DDR2 phosphorylation**, indicating reduced autoinhibition and ligand-independent activation ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)). Biochemical work shows **both variants exhibit ligand-independent constitutive autophosphorylation as full-length proteins**, and the p.Tyr740Cys kinase has enhanced autophosphorylation and substrate-phosphorylation rates with unchanged ATP affinity — the unphosphorylated mutant behaves kinetically like fully phosphorylated wild type, i.e., it **bypasses autoinhibitory constraints** ([PMID: 41259339](https://pubmed.ncbi.nlm.nih.gov/41259339/)).

**Allelic contrast (loss of function → distinct disorder).** Biallelic **loss-of-function** DDR2 variants (missense, nonsense, deletion, splice; e.g., p.S823Cfs*2) cause **SMED-SL** (spondylo-meta-epiphyseal dysplasia, short limb–abnormal calcification type; OMIM 271665), an autosomal-recessive skeletal dysplasia, via defective intracellular trafficking and loss of collagen-induced activation ([PMID: 24725993](https://pubmed.ncbi.nlm.nih.gov/24725993/); [PMID: 36720430](https://pubmed.ncbi.nlm.nih.gov/36720430/)). This is the **opposite functional mechanism** to WCS.

**Modifier genes / epigenetics / chromosomal abnormalities.** None reported. WCS is not associated with aneuploidy, translocations, or copy-number variants; no epigenetic signature has been described.

---

## Section 5 — Environmental Information

No **toxin, radiation, pollution, occupational, infectious, or lifestyle** cause is implicated in WCS — it is a monogenic disorder. The one clear environmental modifier is **mechanical/surgical trauma**, which provokes and accelerates ocular and cutaneous lesions and drives post-surgical recurrence ([PMID: 39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/)). No infectious agents cause or trigger the disease.

---

## Section 6 — Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

```
Germline activating DDR2 missense variant (p.Leu610Pro / p.Tyr740Cys)
        │  (reduced autoinhibition; bypass of autoinhibitory constraints)
        ▼
Ligand-INDEPENDENT constitutive DDR2 kinase autophosphorylation
        │  (does not require collagen binding)
        ▼
Sustained downstream signaling in fibroblasts: ERK1/2  +  NF-κB
        │
        ▼
Up-regulation of MMPs (MMP-1/2/9/13) and MT1-MMP (MMP-14)
   + DDR2 tethers active MT1-MMP to collagen fibers (sustained ECM degradation)
        │
        ▼
Dysregulated ECM remodeling → fibro-proliferation (keloids, corneal pannus/
neovascularization) AND tissue destruction (ulcers, subcutaneous wasting, acro-osteolysis)
        │
        ▼
Progressive multisystem clinical phenotype
```

**Molecular pathways.** DDR2 is a collagen-activated RTK that up-regulates matrix metalloproteinases. In murine melanoma cells, **DDR2 drives MMP-2/9 expression through the ERK/NF-κB pathway** — DDR2 siRNA suppresses ERK1/2 and NF-κB and down-regulates MMP-2/9 ([PMID: 25733533](https://pubmed.ncbi.nlm.nih.gov/25733533/)). Relevant GO/pathway terms: **transmembrane receptor protein tyrosine kinase signaling (GO:0007169)**, **positive regulation of ERK1/ERK2 cascade (GO:0070374)**, **extracellular matrix disassembly (GO:0022617)**, **collagen catabolic process (GO:0030574)**.

**Cellular processes / effector cell.** The **fibroblast** (CL:0000057) is the central effector cell. In **human fibroblasts, DDR2 mediates collagen-induced up-regulation of MT1-MMP and pro-MMP-2 activation** ([PMID: 28270508](https://pubmed.ncbi.nlm.nih.gov/28270508/)). DDR2 also **tethers active MT1-MMP to collagen fibers within "DDR2-containing remnants," sustaining pericellular ECM degradation** ([PMID: 33882324](https://pubmed.ncbi.nlm.nih.gov/33882324/)). DDR2 additionally governs fibroblast **proliferation** as an ECM sensor ([PMID: 11375938](https://pubmed.ncbi.nlm.nih.gov/11375938/)).

**Protein dysfunction.** The mutations act by **gain of function at the kinase**, not by misfolding/aggregation. p.Tyr740Cys increases catalytic activity and removes the autoinhibitory clamp; unphosphorylated mutant behaves like phosphorylated wild type ([PMID: 41259339](https://pubmed.ncbi.nlm.nih.gov/41259339/)).

**Tissue-damage / fibrosis mechanism.** DDRs are established **anti-fibrotic targets across liver, kidney, lung, cardiovascular, and skin (hypertrophic scar) fibrosis** ([PMID: 40796038](https://pubmed.ncbi.nlm.nih.gov/40796038/); [PMID: 24725424](https://pubmed.ncbi.nlm.nih.gov/24725424/)). DDR dysregulation after injury is detrimental and promotes inflammation and fibrosis ([PMID: 24361528](https://pubmed.ncbi.nlm.nih.gov/24361528/)). In WCS, constitutive DDR2 activity produces a chronic, injury-independent version of this fibrotic program.

**Immune involvement.** Not a primary autoimmune or immunodeficiency disorder, though NF-κB activation and secondary infection of chronic ulcers/skin fusion contribute to morbidity.

**Molecular profiling.** No transcriptomic, proteomic, metabolomic, or single-cell datasets specific to WCS patients are available; mechanistic inferences derive from DDR2 fibroblast and cancer-cell models.

---

## Section 7 — Anatomical Structures Affected

**Organ / system level:**

| System | Manifestation | UBERON (suggested) |
|--------|---------------|--------------------|
| Ocular surface | Corneal neovascularization, pannus, symblepharon, limbal stem-cell deficiency, thin cornea | cornea UBERON:0000964; conjunctiva UBERON:0001811 |
| Skin / integument | Keloids, chronic ulcers, thin skin, subcutaneous wasting | skin UBERON:0002097; subcutaneous tissue UBERON:0002072 |
| Skeleton (hands) | Acro-osteolysis, phalangeal osteolysis, contractures | manual digit bone UBERON:0004248; phalanx UBERON:0001449 |
| Joints | Flexion contractures (fingers, wrist, elbow, ankle), joint swelling | joint UBERON:0000982 |
| Craniofacial | Narrow nose, long face, midface retrusion, high palate, short chin | face UBERON:0001456; palate UBERON:0001716 |
| Ear | Conductive hearing loss, cholesteatoma, EAC atresia, ear-cartilage hypoplasia | ear UBERON:0001690; external acoustic meatus UBERON:0001352 |
| Respiratory | Pneumothorax; neonatal choanal abnormalities | lung UBERON:0002048; choana |

**Tissue and cell level.** Predominantly **connective tissue** and the **corneal/ocular-surface epithelium/stroma**. The key targeted cell is the **fibroblast (CL:0000057)**; corneal **limbal stem-cell deficiency** (HP:0032107) implicates limbal epithelial stem cells.

**Subcellular level.** Disease originates at the **plasma membrane** (GO:0005886) receptor; downstream effects converge on the **extracellular matrix / extracellular region** (GO:0005576) and involve **collagen-containing ECM (GO:0062023)**.

**Localization / lateralization.** Ocular and cutaneous lesions are typically **bilateral** but can be **asymmetric**, with lesion location influenced by sites of trauma.

---

## Section 8 — Temporal Development

- **Onset:** Ranges from **neonatal** ([PMID: 41778429](https://pubmed.ncbi.nlm.nih.gov/41778429/)) through **childhood** ([PMID: 39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/)) to **adulthood**; onset pattern is generally **chronic/insidious** and progressive.
- **Progression:** **Progressive** for most features (corneal neovascularization, acro-osteolysis, contractures, skin lesions). Ocular disease can be **stepwise/accelerated by trauma and surgery**, with rapid regrowth after intervention ([PMID: 39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/)).
- **Course / duration:** **Chronic, lifelong.** No spontaneous remission is described.
- **Critical periods:** Peri-traumatic and peri-surgical windows are periods of vulnerability (lesion provocation/recurrence) and represent the logical window for mechanism-based (kinase-inhibitor) intervention to blunt the fibro-proliferative response.

---

## Section 9 — Inheritance and Population

**Epidemiology.** WCS is **ultra-rare**: only **6 affected individuals from 4 families** were reported at initial description ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)); by 2024 the literature still described **~6 cases worldwide** ("Only six cases have been reported worldwide and our knowledge of this disease remained sparse") ([PMID: 39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/)), with additional single cases since ([PMID: 41778429](https://pubmed.ncbi.nlm.nih.gov/41778429/)). No prevalence/incidence figures are calculable; there is **no Orphanet epidemiology entry**.

**Inheritance genetics:**

- **Pattern:** **Autosomal dominant** (AD).
- **New vs inherited:** Both **de novo** and **inherited** — a de novo variant in a mother was transmitted to two children ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)).
- **Penetrance:** Appears high in reported carriers, but cohort too small to quantify.
- **Expressivity:** **Variable**, even intrafamilially.
- **Anticipation / mosaicism / founder effects / consanguinity / carrier frequency:** No evidence for anticipation; no founder effect (variants are private/recurrent hotspots, not population-restricted); consanguinity is **not** relevant (dominant, not recessive — in contrast to the allelic recessive SMED-SL). Carrier frequency not applicable for a dominant de-novo-capable disorder.

**Demographics.** No ethnic predilection, sex bias, or geographic clustering has been established given the tiny case count.

---

## Section 10 — Diagnostics

**Genetic testing is definitive.** Diagnosis rests on identifying a **heterozygous activating DDR2 missense variant** (p.Leu610Pro or p.Tyr740Cys, or a novel spectrum variant).

- **WES/WGS:** High utility — the original cohort and the neonatal case were solved by **whole-exome sequencing** ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/); [PMID: 41778429](https://pubmed.ncbi.nlm.nih.gov/41778429/)).
- **Single-gene / panel testing:** Targeted **DDR2** sequencing (or a connective-tissue/skeletal-dysplasia panel including DDR2) is appropriate once WCS is suspected clinically.
- **CMA / karyotype / FISH / mtDNA / repeat-expansion testing:** Not indicated (no structural, mitochondrial, or repeat-expansion mechanism).

**Functional / laboratory confirmation.** Patient-derived **fibroblasts show increased DDR2 autophosphorylation**, which can serve as a functional assay ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)).

**Imaging.** **Hand radiographs** demonstrate acro-osteolysis and phalangeal osteolytic defects; **ophthalmic examination/slit-lamp** documents corneal neovascularization, pannus, symblepharon, and corneal thinning; **CT** may characterize cholesteatoma/EAC atresia and choanal abnormalities.

**Biopsy/pathology.** Skin lesions show keloidal fibro-proliferation; ocular masses show vascularized fibrovascular tissue invading the cornea ([PMID: 39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/)).

**Differential diagnosis.** Multicentric osteolysis/nodulosis/arthropathy (MONA, MMP2), other acro-osteolysis syndromes (Hajdu-Cheney), scleroderma/fibrosing disorders, and — at the gene level — the **allelic recessive SMED-SL** (opposite mechanism, skeletal dysplasia phenotype) ([PMID: 36720430](https://pubmed.ncbi.nlm.nih.gov/36720430/)).

**Screening.** No population/newborn screening exists or is warranted given rarity. **Cascade genetic testing** of at-risk relatives in a known family is appropriate.

---

## Section 11 — Outcome / Prognosis

No survival, mortality, or formal QoL data exist for this ultra-rare disorder. The disease is **chronic, progressive, and lifelong**, with cumulative morbidity from:

- **Vision loss** — progressive corneal neovascularization/opacification (visual impairment in 75%), aggravated by recurrence after ocular surgery ([PMID: 39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/)).
- **Hand disability** — flexion contractures and acro-osteolysis.
- **Chronic wounds/infection** — non-healing ulcers, skin fusion, sterile/infected abscesses.
- **Hearing loss** — conductive impairment, cholesteatoma.
- **Respiratory events** — pneumothorax (33%); neonatal respiratory distress from choanal abnormalities.

**Prognostic factors** are not formally established; **degree of DDR2 hyperactivation** and **trauma burden** are plausible drivers of severity. **Recovery potential** is limited under current supportive-only management, but is the central rationale for mechanism-based therapy.

---

## Section 12 — Treatment

There is **no approved, disease-specific therapy**; management is currently **supportive** (wound care, ophthalmic surface management, contracture/hand therapy, hearing rehabilitation, treatment of infection). Surgery on ocular/skin lesions is complicated by **trauma-provoked recurrence** ([PMID: 39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/)), so surgical decisions should be cautious.

**Mechanism-based (experimental) pharmacotherapy — DDR2 tyrosine-kinase inhibition:**

| Agent | Class | Evidence for WCS relevance | NCIT (suggested) |
|-------|-------|----------------------------|------------------|
| **Dasatinib** | BCR-ABL/SRC TKI; potent DDR1/2 inhibitor | **Prevents mutant DDR2 autophosphorylation in patient fibroblasts** ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)); potent DDR inhibitor ([PMID: 18938156](https://pubmed.ncbi.nlm.nih.gov/18938156/)) | NCIT:C38713 |
| **Imatinib** | BCR-ABL TKI | Potent DDR1/2 inhibitor ([PMID: 18938156](https://pubmed.ncbi.nlm.nih.gov/18938156/)) | NCIT:C62035 |
| **Nilotinib** | BCR-ABL TKI | Potent DDR1/2 inhibitor ([PMID: 18938156](https://pubmed.ncbi.nlm.nih.gov/18938156/)) | NCIT:C48375 |
| **WRG-28** | Selective allosteric DDR2 inhibitor | Attenuates DDR2-driven matrix degradation/MMP13 in osteoarthritis models ([PMID: 41955962](https://pubmed.ncbi.nlm.nih.gov/41955962/)) — investigational, not yet tested in WCS | — |

Key supporting quote: *"we found that the protein kinase inhibitor dasatinib prevented DDR2 autophosphorylation in fibroblasts, suggesting an approach to treatment"* ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)); and *"all 3 compounds are potent inhibitors of the kinase activity of both DDR1 and DDR2"* ([PMID: 18938156](https://pubmed.ncbi.nlm.nih.gov/18938156/)).

**Personalized-medicine rationale.** Because WCS is driven by a single, well-defined activated kinase with **no evidence of other growth-pathway activation** ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)), it is a strong candidate for **genotype-guided kinase-inhibitor therapy**. No gene therapy, cell therapy, RNA therapy, or immunotherapy has been reported. **No completed or registered clinical trial (NCT) specific to WCS was identified.**

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable to a de-novo-capable germline disorder. **Genetic counseling** and **cascade/prenatal or preimplantation genetic testing** are options for known-variant families.
- **Secondary prevention:** Early molecular diagnosis (WES) and early ophthalmic/skin surveillance to intervene before irreversible damage.
- **Tertiary prevention:** **Minimize provocative trauma/surgery** to affected surfaces, aggressive wound-infection control, contracture-preventive physiotherapy, hearing/vision rehabilitation. Mechanism-based TKI therapy — if validated — would be a tertiary-preventive strategy to halt progression.
- **Immunization / public health / environmental interventions:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Orthologous gene:** DDR2 is conserved. **Mouse *Ddr2*** — NCBI Gene ID **18214** (*Mus musculus*, NCBI Taxon **10090**); zebrafish DDR2 orthologs (*Danio rerio*, NCBI Taxon **7955**).
- **Natural disease:** **No naturally occurring WCS-equivalent (gain-of-function DDR2) disease** has been described in companion animals or wildlife (no OMIA entry identified). Available animal data are **engineered loss-of-function** models (below), which model DDR2 deficiency, not WCS.
- **Comparative biology:** DDR2's role in chondrocyte proliferation, skin wound healing, and craniofacial/palate development is **evolutionarily conserved** from zebrafish to mouse to human ([PMID: 11375938](https://pubmed.ncbi.nlm.nih.gov/11375938/); [PMID: 42323896](https://pubmed.ncbi.nlm.nih.gov/42323896/)).
- **Transmission / zoonosis:** Not applicable (genetic disorder).

---

## Section 15 — Model Organisms

**Important caveat:** **All existing animal models are loss-of-function (Ddr2-null / knockdown), which model the allelic recessive SMED-SL rather than gain-of-function WCS.** No gain-of-function (knock-in p.Leu610Pro/p.Tyr740Cys) animal model has yet been reported (Findings F002/F007).

| Model | Type | Phenotype | Relevance / limitation |
|-------|------|-----------|------------------------|
| **Ddr2-null mouse** (*Mus musculus*, Taxon 10090; Gene 18214) | Knockout (LOF) | **Dwarfism and shortening of long bones from reduced chondrocyte proliferation**; **reduced proliferative response in skin wound healing**; DDR2−/− fibroblasts proliferate more slowly (rescued by WT but not kinase-dead DDR2) ([PMID: 11375938](https://pubmed.ncbi.nlm.nih.gov/11375938/)) | Establishes DDR2 as an ECM-sensing proliferation regulator; **models LOF (SMED-SL), not WCS GOF** |
| **Zebrafish ddr2 knockdown/knockout** (*Danio rerio*, Taxon 7955) | Morphant/KO (LOF) | **Craniofacial abnormalities resembling human cleft palate** ([PMID: 42323896](https://pubmed.ncbi.nlm.nih.gov/42323896/)) | Connects DDR2 to the palatal/craniofacial phenotype seen in WCS |
| **Patient-derived fibroblasts (in vitro)** | Human primary cells | Increased DDR2 autophosphorylation; dasatinib-responsive ([PMID: 30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/)) | Best available WCS-specific functional model and drug-testing platform |
| **Recombinant DDR2 kinase / mammalian expression** | In vitro / cell-based | Constitutive ligand-independent autophosphorylation; enhanced catalysis of Y740C ([PMID: 41259339](https://pubmed.ncbi.nlm.nih.gov/41259339/)) | Defines the biophysical GOF mechanism |

**Model databases:** MGI (mouse *Ddr2*), ZFIN (zebrafish *ddr2*), Alliance of Genome Resources.

Supporting quotes: *"These mice exhibit dwarfism and shortening of long bones... caused by reduced chondrocyte proliferation"* and *"In a skin wound healing model, DDR2-/- mice exhibit a reduced proliferative response"* ([PMID: 11375938](https://pubmed.ncbi.nlm.nih.gov/11375938/)); *"Knock-down and knock-out of DDR2-orthologs in zebrafish caused craniofacial abnormalities resembling CPO in humans"* ([PMID: 42323896](https://pubmed.ncbi.nlm.nih.gov/42323896/)).

---

## Mechanistic Model / Interpretation

WCS is best understood as a **"constitutive kinase" connective-tissue disease**. A single-nucleotide germline change removes the autoinhibitory brake on DDR2, so the receptor signals continuously **without needing to bind collagen**. In fibroblasts — the disease's effector cell — this locks in a chronic ERK/NF-κB → MMP/MT1-MMP program that simultaneously **builds abnormal matrix** (keloids, corneal pannus and neovascularization) and **destroys existing tissue** (chronic ulcers, subcutaneous wasting, acro-osteolysis). The apparent paradox of "too much scarring **and** too much destruction" is resolved by recognizing that both are outputs of dysregulated ECM remodeling driven by the same overactive receptor.

Two natural experiments frame the mechanism:

```
                DDR2 dosage/activity axis
LOSS of function  ◄──────────────────────────────►  GAIN of function
   SMED-SL (AR)        normal DDR2          Warburg-Cinotti (AD)
 skeletal dysplasia,   collagen-cued        constitutive kinase,
 short limbs,          ECM sensing          fibrosis + osteolysis +
 abnormal calcif.      & wound healing      neovascularization
 (trafficking defect,  (chondrocyte prolif, (ligand-independent
 loss of ligand        wound repair)         autophosphorylation)
 activation)
```

Both ends of this axis are pathological, and both are informative: the LOF mouse/zebrafish models reveal DDR2's normal developmental roles (chondrocyte proliferation, wound healing, palate formation) — roles that manifest as **skeletal/craniofacial** overlap features in WCS — while the GOF human disease shows what happens when the same receptor is unleashed.

The therapeutic corollary is unusually clean: **turn the kinase off**. Dasatinib already abolishes mutant DDR2 autophosphorylation in patient cells, and multiple approved TKIs plus selective allosteric DDR2 inhibitors are available for testing.

---

## Evidence Base

| PMID | Study | How it supports / challenges findings |
|------|-------|----------------------------------------|
| [30449416](https://pubmed.ncbi.nlm.nih.gov/30449416/) | *Recurrent, Activating Variants in DDR2 Cause WCS* (Xu et al. 2018) | **Foundational.** Defines gene, two recurrent variants, AD inheritance, core phenotype, GOF mechanism, and dasatinib rationale. |
| [41259339](https://pubmed.ncbi.nlm.nih.gov/41259339/) | *WCS variant p.Tyr740Cys enhances DDR2 kinase catalytic activity* (Hao & Leitinger 2025) | Confirms both variants are constitutively autophosphorylated and bypass autoinhibition; kinetic proof of GOF. |
| [39095787](https://pubmed.ncbi.nlm.nih.gov/39095787/) | *Progressive conjunctival invasion of cornea in a child with WCS* (Ben 2024) | Documents ultra-rarity (~6 cases), trauma-provoked progression, and surgical recurrence. |
| [41778429](https://pubmed.ncbi.nlm.nih.gov/41778429/) | *Novel mutation, neonatal WCS case* (Xiao 2025) | Expands mutational spectrum and onset to neonatal period (choanal/respiratory presentation). |
| [28270508](https://pubmed.ncbi.nlm.nih.gov/28270508/) | *DDR2 mediates collagen-induced MT1-MMP activation in human fibroblasts* (Majkowska 2017) | Links DDR2 to MT1-MMP/pro-MMP-2 in the effector cell of WCS. |
| [25733533](https://pubmed.ncbi.nlm.nih.gov/25733533/) | *DDR2 inhibition reduces MMP2/9 via ERK/NF-κB* (Poudel 2015) | Establishes the ERK/NF-κB → MMP signaling axis. |
| [33882324](https://pubmed.ncbi.nlm.nih.gov/33882324/) | *Active MT1-MMP tethered to collagen in DDR2 remnants* (Feng 2021) | Mechanism for sustained ECM degradation. |
| [40796038](https://pubmed.ncbi.nlm.nih.gov/40796038/) | *DDRs as anti-fibrotic target — review* (Gong 2025) | Positions DDR2 as a broad anti-fibrotic drug target. |
| [24725424](https://pubmed.ncbi.nlm.nih.gov/24725424/) / [24361528](https://pubmed.ncbi.nlm.nih.gov/24361528/) | *DDR function in physiology/disease* (Leitinger 2014; Vogel 2014) | Frame DDR2 biology, fibrosis, and inflammation roles. |
| [18938156](https://pubmed.ncbi.nlm.nih.gov/18938156/) | *Imatinib, nilotinib, dasatinib inhibit DDR1/2* (Day 2008) | Expands the repurposing pool of DDR2 inhibitors. |
| [41955962](https://pubmed.ncbi.nlm.nih.gov/41955962/) | *WRG-28 selective DDR2 inhibitor in OA* (2026) | Provides a selective allosteric DDR2 inhibitor candidate. |
| [11375938](https://pubmed.ncbi.nlm.nih.gov/11375938/) | *DDR2 regulates proliferation; elimination → dwarfism* (Labrador 2001) | LOF mouse model — skeletal + wound-healing roles. |
| [42323896](https://pubmed.ncbi.nlm.nih.gov/42323896/) | *DDR2 disruption → palate malformations* (Capecki 2026) | LOF zebrafish model — craniofacial/palate link. |
| [24725993](https://pubmed.ncbi.nlm.nih.gov/24725993/) / [36720430](https://pubmed.ncbi.nlm.nih.gov/36720430/) | *Biallelic LOF DDR2 → SMED-SL* (Al-Kindi 2014; Akalın 2023) | Define the allelic, mechanistically opposite recessive disorder. |

---

## Limitations and Knowledge Gaps

1. **Extreme rarity.** With fewer than ~10 reported individuals, no epidemiology (prevalence/incidence), penetrance, expressivity, survival, or QoL statistics can be calculated. Phenotype frequencies from HPOA rest on a very small denominator.
2. **No gain-of-function animal model.** Every available in-vivo model is LOF (Ddr2-null mouse, ddr2-knockdown zebrafish), which recapitulates SMED-SL, not WCS. A knock-in GOF model is the single biggest missing tool.
3. **No WCS-specific omics.** No transcriptomic, proteomic, metabolomic, single-cell, or spatial data exist for patient tissues; mechanistic inference relies on DDR2 cancer/fibroblast surrogates.
4. **Therapy is unproven in humans.** Dasatinib/imatinib/nilotinib efficacy is demonstrated at the level of kinase inhibition and patient-cell autophosphorylation only — **no clinical trial (NCT) has tested any DDR2 inhibitor in WCS**, and TKI toxicity in a chronic, pediatric-onset setting is a serious concern.
5. **Genotype–phenotype spectrum unclear.** Whether the novel neonatal variant behaves identically to the two hotspots, and what determines variable expressivity, is unknown.
6. **Ontology mapping incomplete.** No Orphanet, ICD, or MeSH code exists, complicating registry-based case finding.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in GOF model.** Create *Ddr2^L610P^* and *Ddr2^Y740C^* knock-in mice (and/or zebrafish) to test whether they recapitulate corneal neovascularization, keloids, and acro-osteolysis, and to serve as a preclinical drug-testing platform.
2. **Preclinical TKI dose-response.** Systematically compare dasatinib, imatinib, nilotinib, and selective allosteric inhibitors (e.g., WRG-28) in patient fibroblasts and the new GOF model for suppression of autophosphorylation, ERK/NF-κB, and MMP/MT1-MMP output, with careful attention to therapeutic index.
3. **N-of-1 / basket clinical evaluation.** Given mechanistic clarity and drug availability, pursue carefully monitored compassionate-use or n-of-1 trials of a DDR2 inhibitor (with local/topical formulation considered for the ocular surface to limit systemic toxicity), registering an NCT.
4. **Patient-tissue multi-omics.** Perform single-cell/spatial transcriptomics and proteomics on WCS keloid, ulcer margin, and corneal pannus tissue to map fibroblast subpopulations and confirm the ERK/NF-κB/MMP program in situ.
5. **International registry & GeneMatcher outreach.** Aggregate all known cases to define natural history, penetrance, expressivity, and genotype–phenotype correlations; seek an Orphanet/ICD-11 code.
6. **Biomarker development.** Validate DDR2 phosphorylation and circulating MMP-2/9/13 as pharmacodynamic biomarkers for future trials.

---

*Evidence-source key: human clinical (case reports/cohorts) — PMIDs 30449416, 39095787, 41778429, 35036505; in vitro / biochemical — 41259339, 28270508, 25733533, 33882324, 18938156, 41955962; model organism — 11375938, 42323896; review/synthesis — 40796038, 24725424, 24361528; allelic disorder — 24725993, 36720430; ontology cross-references verified via EBI OLS4 (MONDO) and Monarch/HPOA.*


## Artifacts

- [OpenScientist final report](Warburg_Cinotti_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Warburg_Cinotti_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 31 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032579` (3 mentions) - the report calls it "MONDO"; MONDO calls it **warburg-cinotti syndrome**
- `EFO:0010166` (1 mention) - the report calls it "EFO"; EFO calls it **Warburg-Cinotti syndrome**
- `NCIT:C62035` (1 mention) - the report calls it "Potent DDR1/2 inhibitor (PMID: 18938156)"; NCIT calls it **Imatinib**
- `NCIT:C48375` (1 mention) - the report calls it "Potent DDR1/2 inhibitor (PMID: 18938156)"; NCIT calls it **Nilotinib**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011496` (2 mentions) - the report calls it "Progressive corneal neovascularization", "Corneal neovascularization"; HP calls it **Corneal neovascularization**
- `HP:0001058` (2 mentions) - the report calls it "Chronic skin ulcers / poor wound healing", "Poor wound healing"; HP calls it **Poor wound healing**
- `HP:0012785` (1 mention) - the report calls it "Flexion contractures of the fingers"; HP calls it **Flexion contracture of finger**
- `HP:0009771` (2 mentions) - the report calls it "Acro-osteolysis / osteolytic phalangeal defects", "Osteolytic defects of phalanges of hand"; HP calls it **Osteolytic defects of the phalanges of the hand**, and lists "Acro-osteolysis" among its other names
- `HP:0100720` (1 mention) - the report calls it "Hypoplasia of ear cartilage"; HP calls it **Hypoplasia of the ear cartilage**
- `HP:0000413` (1 mention) - the report calls it "Atresia of external auditory canal"; HP calls it **Atresia of the external auditory canal**
- `GO:0005576` (1 mention) - the report calls it "extracellular matrix / extracellular region"; GO calls it **extracellular region**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0011496` - called "Progressive corneal neovascularization", "Corneal neovascularization"
- `HP:0001058` - called "Chronic skin ulcers / poor wound healing", "Poor wound healing"
- `HP:0009771` - called "Acro-osteolysis / osteolytic phalangeal defects", "Osteolytic defects of phalanges of hand"
- `HP:0032107` - called "Limbal stem cell deficiency", "limbal stem-cell deficiency"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.