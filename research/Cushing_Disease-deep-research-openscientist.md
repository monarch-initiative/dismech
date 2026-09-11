---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T21:31:41.357083'
end_time: '2026-08-28T21:50:01.796148'
duration_seconds: 1100.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cushing Disease
  mondo_id: ''
  category: Endocrine Disorder
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
citation_count: 45
reference_validation:
  total_references: 46
  verified: 46
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 46
  on_topic: 30
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 12
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0005479
    reported_labels:
    - Cushing disease
    ontology_label: atrial tachycardia
  - term_id: HP:0000858
    reported_labels:
    - Secondary amenorrhea
    ontology_label: Irregular menstruation
  labels_variant: 3
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
  path: Cushing_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cushing_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cushing Disease
- **MONDO ID:**  (if available)
- **Category:** Endocrine Disorder

## Research Objectives

Please provide a comprehensive research report on **Cushing Disease** covering all of the
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

# Cushing Disease: A Comprehensive Disease-Characteristics Report

**Disease Category:** Endocrine Disorder
**Suggested MONDO term:** MONDO:0005479 (Cushing disease) — ACTH-secreting pituitary corticotroph adenoma
**Report basis:** 16 confirmed findings across 5 investigation iterations, 70 papers reviewed.

---

## Summary

**Cushing disease (CD)** is a rare, life-threatening endocrine disorder caused by a benign adrenocorticotropic hormone (ACTH)-secreting pituitary **corticotroph adenoma** (a pituitary neuroendocrine tumor, PitNET, of the TPIT/TBX19 lineage). Autonomous ACTH hypersecretion drives bilateral adrenal cortisol overproduction and chronic endogenous hypercortisolism, producing a characteristic multisystem "cushingoid" phenotype. CD is the most common cause of endogenous Cushing syndrome (CS), accounting for roughly **48%** of cases, with a nationwide incidence of approximately **1.6 cases per million per year** and a marked female predominance (~3:1). At the molecular level, the disease is most commonly driven by **somatic gain-of-function mutations in *USP8*** (~31% of corticotroph tumors), with additional recurrent drivers in *USP48* and *BRAF* converging on enhanced pro-opiomelanocortin (POMC) transcription and ACTH secretion; aggressive tumors are enriched for *TP53* and *ATRX* alterations. A central pathophysiological feature is **partial resistance to glucocorticoid negative feedback**, which is exploited diagnostically in the dexamethasone suppression test.

The clinical burden of CD is severe. Chronic cortisol excess produces weight gain, centripetal obesity, proximal myopathy, hypertension (~80%), diabetes, osteoporosis, neuropsychiatric disturbance, reproductive dysfunction, and a **hypercoagulable state** that predisposes to venous thromboembolism. Untreated or persistent disease carries a **2- to 9-fold excess mortality**, driven principally by cardiovascular disease and infection. Even after biochemical remission, mortality risk, quality of life, and socioeconomic function may not fully normalize, underscoring the disease's lasting impact.

First-line treatment is **transsphenoidal adenomectomy**, which achieves initial remission in ~80% of patients but is complicated by recurrence in ~15–27%. Medical therapies — the 11β-hydroxylase inhibitor **osilodrostat**, the pituitary-directed somatostatin analog **pasireotide**, cabergoline, metyrapone, ketoconazole/levoketoconazole, and the glucocorticoid-receptor antagonist mifepristone — plus radiotherapy and bilateral adrenalectomy are used for persistent or recurrent disease. CD occurs naturally in dogs (pituitary-dependent hyperadrenocorticism), the leading spontaneous animal model, and is studied in vitro chiefly using the murine **AtT-20** corticotroph tumor cell line.

---

## 1. Disease Information

**Overview.** Cushing disease is defined as ACTH-dependent endogenous hypercortisolism caused specifically by a pituitary corticotroph adenoma. It is distinguished from the broader term *Cushing syndrome* (any cause of chronic glucocorticoid excess, including exogenous steroids, adrenal tumors, and ectopic ACTH secretion). CD is the single most common cause of endogenous CS.

**Key identifiers (suggested):**
- **MONDO:** MONDO:0005479 (Cushing disease)
- **OMIM:** 219090 (Cushing disease / pituitary ACTH-secreting adenoma phenotype); *USP8* somatic association
- **Orphanet:** ORPHA:96253 (Cushing disease)
- **ICD-10:** E24.0 (Pituitary-dependent Cushing disease); **ICD-11:** 5A70 (Cushing syndrome, pituitary-dependent subgrouping)
- **MeSH:** D047748 "Pituitary ACTH Hypersecretion"

**Synonyms / alternative names:** Pituitary-dependent Cushing syndrome; pituitary-dependent hypercortisolism; ACTH-secreting pituitary adenoma; corticotropinoma; Cushing disease of the pituitary; pituitary-dependent hyperadrenocorticism (veterinary term).

**Source of information.** This report is derived from **aggregated disease-level resources** — nationwide registry studies (Sweden, Denmark), tertiary-referral cohorts, systematic reviews/meta-analyses, and Phase III clinical trials — rather than from individual EHR-level patient records.

---

## 2. Etiology

**Primary causal factor.** CD is caused by a monoclonal, usually benign, ACTH-secreting pituitary corticotroph adenoma. The dominant molecular etiology is **somatic (tumor-restricted) gain-of-function mutation**, not germline inheritance in most cases.

**Genetic risk / causal factors (somatic).**
- ***USP8*** (ubiquitin-specific peptidase 8): the most common driver, present in **~31%** of corticotroph tumors (pooled prevalence 31.1%, 95% CI 26.5–36.0%; [PMID: 40392165](https://pubmed.ncbi.nlm.nih.gov/40392165/)). Hotspot variants cluster in exon 14 (14-3-3 binding motif, codons 713–720; e.g., p.Ser718Pro, p.Pro720Arg).
- ***USP48*** and ***BRAF*** — additional recurrent drivers converging on POMC/ACTH ([PMID: 42236012](https://pubmed.ncbi.nlm.nih.gov/42236012/)).
- ***TP53*** and ***ATRX/DAXX*** — enriched in aggressive/silent corticotroph tumors and Crooke cell adenomas ([PMID: 42273717](https://pubmed.ncbi.nlm.nih.gov/42273717/); [PMID: 41047423](https://pubmed.ncbi.nlm.nih.gov/41047423/)).

**Germline predisposition (minority).** Rare familial/syndromic forms involve germline variants in *MEN1* (MEN1), *AIP* (familial isolated pituitary adenoma), *CDKN1B* (MEN4), *PRKAR1A* (Carney complex), and *CDKN2A* (reported in pediatric CD; [PMID: 40813536](https://pubmed.ncbi.nlm.nih.gov/40813536/)). Germline genetic testing is recommended in young/pediatric patients.

**Environmental risk factors.** No established environmental, toxic, occupational, or infectious cause. The strongest demographic risk factors are **female sex** and **age** (peak 3rd–5th decade). *USP8*-mutant tumors show strong female predominance (OR 4.52; [PMID: 40392165](https://pubmed.ncbi.nlm.nih.gov/40392165/)).

**Protective factors / gene-environment interactions.** No validated genetic or environmental protective factors are documented. Because the disease is driven by somatic mutation, classic gene-environment interaction models do not apply. *Not applicable / not available* for most subcategories.

---

## 3. Phenotypes

Cushing disease produces a highly prevalent, characteristic set of physical manifestations, clinical signs, and laboratory abnormalities. Frequencies below are from a large tertiary cohort (n=277; [PMID: 42572239](https://pubmed.ncbi.nlm.nih.gov/42572239/)) and a hypertension-focused review ([PMID: 31164868](https://pubmed.ncbi.nlm.nih.gov/31164868/)).

| Phenotype | Frequency | Type | Suggested HPO term |
|---|---|---|---|
| Weight gain | 79.4% | Physical manifestation | HP:0004324 (Increased body weight) |
| Centripetal (truncal) obesity | 62.5% | Physical manifestation | HP:0001956 (Truncal obesity) |
| Hyperpigmentation | 61.0% | Clinical sign | HP:0000953 (Hyperpigmentation of the skin) |
| Proximal myopathy | 60.6% | Clinical sign | HP:0003701 (Proximal muscle weakness) |
| Hypertension | ~80% | Clinical sign / lab | HP:0000822 (Hypertension) |
| Hyperglycemia / diabetes | common | Laboratory abnormality | HP:0003074 (Hyperglycemia) |
| Striae | common (younger) | Physical manifestation | HP:0001065 (Striae distensae) |
| Menstrual irregularity / reproductive dysfunction | highly prevalent | Clinical sign | HP:0000858 (Secondary amenorrhea) |
| Osteoporosis / fractures | common | Physical manifestation | HP:0000939 (Osteoporosis) |
| Neuropsychiatric change (depression, cognitive) | common | Behavioral | HP:0000716 (Depression) |
| Hypercortisolemia | universal | Laboratory abnormality | HP:0003118 (Abnormal circulating cortisol) |

**Characteristics.** Onset is typically **adult** (3rd–4th decades), **insidious/chronic** in progression. Severity is variable and tied to duration and intensity of cortisol excess. Age-stratified presentation: younger patients more often show striae, acne, and menstrual irregularities; older patients show more cardiometabolic comorbidity ([PMID: 42572239](https://pubmed.ncbi.nlm.nih.gov/42572239/)).

> *"The cohort demonstrated a marked female predominance (71.8%)... Classical cushingoid features were highly prevalent, including weight gain (79.4%), centripetal obesity (62.5%), hyperpigmentation (61.0%), and proximal myopathy (60.6%)."* — [PMID: 42572239](https://pubmed.ncbi.nlm.nih.gov/42572239/)

**Quality of life impact.** CD causes lasting QoL and socioeconomic impairment that persists years after surgical cure. In a Danish nationwide cohort, employment was permanently reduced (RR 0.66 at 10 years post-surgery), with elevated sick leave (RR 2.15) and disability pension (RR 2.60) a decade after treatment ([PMID: 35311897](https://pubmed.ncbi.nlm.nih.gov/35311897/)).

---

## 4. Genetic / Molecular Information

**Causal genes (somatic driver landscape).**

| Gene (HGNC) | Frequency in CD | Variant type | Consequence | Clinical correlate |
|---|---|---|---|---|
| ***USP8*** | ~31% (up to 48–50% some cohorts) | Missense, in-frame; exon 14 hotspots (codons 713–720) | Gain-of-function; disrupts 14-3-3 binding → constitutive deubiquitinase activity | Female, younger, higher remission but higher recurrence |
| ***USP48*** | recurrent (minority) | Missense | Enhanced POMC transcription | Favorable/low-CNV tumors |
| ***BRAF*** | rare | V600E | MAPK activation → POMC | Occasional aggressive |
| ***TP53*** | aggressive subset | Missense/LoF | Loss of tumor suppression | High CNV, invasion, silent/Crooke cell |
| ***ATRX/DAXX*** | aggressive subset | LoF | Chromatin/telomere instability | Aggressive behavior |

**USP8 mechanism (causal chain).** Exon-14 hotspot mutations disrupt the 14-3-3 protein binding motif → **constitutive USP8 activation** → reduced ubiquitination and degradation of EGFR → sustained EGFR signaling → increased POMC transcription and ACTH secretion.

> *"Activating mutation in Ubiquitin-specific peptidase (USP8) is identified to enhance cell proliferation and adrenocorticotropic hormone (ACTH) secretion from corticotroph pituitary adenoma."* — [PMID: 38862897](https://pubmed.ncbi.nlm.nih.gov/38862897/)

**Two divergent molecular pathways** ([PMID: 42273717](https://pubmed.ncbi.nlm.nih.gov/42273717/)): (1) *USP8/USP48*-mutant tumors — low copy-number variation (CNV), minimal invasion, favorable remission (10/21 CD tumors, 48%); (2) *TP53/ATRX/DAXX*-mutant tumors — high CNV, aggressive, more often clinically silent.

> *"USP8/USP48 mutations were present in 10 of 21 CD tumors (48%) and were associated with low CNV levels, minimal invasion, and favorable post-operative remission. In contrast, five of 13 SCAs harbored TP53/ATRX/DAXX mutations, all had markedly elevated CNV, and aggressive clinical features."* — [PMID: 42273717](https://pubmed.ncbi.nlm.nih.gov/42273717/)

**Somatic vs germline.** Overwhelmingly **somatic** (tumor-restricted). Germline variants (*MEN1*, *AIP*, *CDKN1B*, *PRKAR1A*, *CDKN2A*) account for a minority, particularly pediatric/familial cases.

**Allele frequency.** As somatic driver mutations, *USP8* hotspot variants are **absent from population germline databases** (gnomAD); they are tumor-specific and catalogued in COSMIC.

**Modifier genes / epigenetics / chromosomal abnormalities.** Aggressive tumors show elevated CNV burden and *ATRX*-linked chromatin instability. Detailed methylation atlases are still emerging; *not fully characterized*.

---

## 5. Environmental Information

- **Environmental factors:** None established. CD is not linked to documented toxin, radiation, or pollution exposures.
- **Lifestyle factors:** No causal lifestyle factor identified; obesity and metabolic features are *consequences* rather than causes.
- **Infectious agents:** *Not applicable* — CD has no infectious etiology.

This section is largely **not applicable** for Cushing disease, consistent with a somatically-driven neoplastic endocrine disorder.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

```
Somatic driver mutation (USP8 / USP48 / BRAF)
        │  (constitutive deubiquitinase / MAPK activation)
        ▼
Sustained EGFR signaling → ↑ POMC transcription (TPIT/TBX19 lineage)
        │
        ▼
Autonomous ACTH hypersecretion  ← PARTIAL glucocorticoid feedback resistance (GR/NR3C1)
        │
        ▼
Bilateral adrenal stimulation → chronic cortisol excess (hypercortisolism)
        │
        ├──► Mineralocorticoid receptor activation (11β-HSD2 saturation) → HYPERTENSION
        ├──► Insulin resistance / gluconeogenesis → DIABETES, visceral adiposity
        ├──► Protein catabolism → MYOPATHY, osteoporosis, thin skin/striae
        ├──► Procoagulant shift → VENOUS THROMBOEMBOLISM
        ├──► HPG axis suppression → reproductive/sexual dysfunction
        └──► CNS effects → depression, cognitive impairment
```

**Molecular pathways.** EGFR signaling (via USP8-mediated stabilization), MAPK (BRAF), and ubiquitin–proteasome deubiquitination converge on POMC transcription. Suggested GO terms: GO:0030518 (intracellular receptor signaling), GO:0016579 (protein deubiquitination), GO:0007173 (EGFR signaling), GO:0042446 (hormone biosynthetic process).

**Glucocorticoid-feedback resistance.** The glucocorticoid receptor (GR/*NR3C1*) is the principal mediator of HPA-axis negative feedback; CD tumors show **partial resistance**, which underlies the diagnostic dexamethasone suppression test.

> *"CD patients exhibit a partial resistance to the negative glucocorticoid (GC) feedback, which is of paramount clinical utility, as the lack of suppression after dexamethasone administration is one of the mainstays for the differential diagnosis of CD."* — [PMID: 35742910](https://pubmed.ncbi.nlm.nih.gov/35742910/)

**Hypertension mechanism.** Cortisol excess saturates renal 11β-HSD2, permitting cortisol to activate the mineralocorticoid receptor (mineralocorticoid mimetic activity), alongside altered vascular resistance and vascular remodeling.

> *"Glucocorticoid excess leads to hypertension via a variety of mechanisms including mineralocorticoid mimetic activity, alterations in peripheral and renovascular resistance, and vascular remodeling."* — [PMID: 31164868](https://pubmed.ncbi.nlm.nih.gov/31164868/)

**Single-cell / spatial biology.** snRNA-seq (419,874 cells) plus spatial transcriptomics show corticotroph adenomas exist along a transcriptional continuum with developmental plasticity, and that **perivascular niches enhance tumorigenicity via angiogenic and EMT programs** ([PMID: 40666832](https://pubmed.ncbi.nlm.nih.gov/40666832/)). scRNA-seq identified a novel GZMK-high TPIT-lineage subpopulation and validated PBK as an aggressiveness driver ([PMID: 38167466](https://pubmed.ncbi.nlm.nih.gov/38167466/)); alternative-splicing analysis defined an ESRP1-driven aggressive TPIT subtype ([PMID: 39934142](https://pubmed.ncbi.nlm.nih.gov/39934142/)).

**Cell types (suggested CL terms):** corticotroph / ACTH-secreting cell (corticotropic cell of pars distalis), adrenal cortical cell (CL:0002097). **Subcellular:** nucleus (GO:0005634), secretory granules (GO:0030141), endoplasmic reticulum (ER stress implicated via PCSK1N; [PMID: 39288010](https://pubmed.ncbi.nlm.nih.gov/39288010/)).

---

## 7. Anatomical Structures Affected

**Primary organ:** Anterior pituitary gland (adenohypophysis) — UBERON:0000007 (pituitary gland); specifically corticotroph cells of the pars distalis.

**Secondary organs (via cortisol excess):** Adrenal cortex (bilateral hyperstimulation; UBERON:0001235), cardiovascular system (UBERON:0004535), skeletal muscle (UBERON:0001134), bone/skeleton (UBERON:0002481), skin (UBERON:0002097), liver (metabolic; hepatic hemangioma association reported, [PMID: 42332692](https://pubmed.ncbi.nlm.nih.gov/42332692/)), gonads/HPG axis, and central nervous system.

**Body systems involved:** Endocrine (primary), cardiovascular, musculoskeletal, integumentary, reproductive, nervous/psychiatric, hematologic (hypercoagulability), and immune (infection susceptibility).

**Tissue/cell level:** Neuroendocrine epithelial (corticotroph) tumor tissue; adrenal cortical zona fasciculata; vascular endothelium (remodeling); adipose tissue (redistribution).

**Localization / lateralization:** The pituitary microadenoma is usually a small (<10 mm) intrasellar lesion; adrenal effects are **bilateral and symmetric** (diffuse hyperplasia). MRI localization of the corticotroph microadenoma is notoriously **reader-dependent**, and ~10% of cases are MRI-negative ([PMID: 42537231](https://pubmed.ncbi.nlm.nih.gov/42537231/); [PMID: 42517988](https://pubmed.ncbi.nlm.nih.gov/42517988/)).

---

## 8. Temporal Development

- **Onset:** Adult-onset typical (peak 3rd–5th decade); pediatric and geriatric cases occur. Pattern is **insidious/chronic**, often with diagnostic delay of months to years.
- **Progression:** Slowly progressive if untreated; cortisol excess drives cumulative cardiometabolic, skeletal, and vascular damage. Rare **cyclic/episodic** hypercortisolism complicates diagnosis.
- **Disease course pattern:** Chronic; treatment-induced remission is the goal. Recurrence occurs in ~15–27% after surgery (median ~38 months; [PMID: 40257708](https://pubmed.ncbi.nlm.nih.gov/40257708/)), so the course can be **relapsing**.
- **Lifespan variation:** Presentation differs across age — growth arrest with weight gain in children; pubertal/psychological disturbance in adolescents; classic cushingoid features in adults; frailty, sarcopenia, fractures, and cognitive decline in the elderly ([PMID: 42095775](https://pubmed.ncbi.nlm.nih.gov/42095775/)).

> *"In children, impaired growth coupled with weight gain is most prominent, whereas adolescents often present with pubertal disturbances and psychological or academic difficulties."* — [PMID: 42095775](https://pubmed.ncbi.nlm.nih.gov/42095775/)

- **Critical periods:** Early biochemical control is the key window to prevent irreversible cardiovascular and skeletal damage.

---

## 9. Inheritance and Population

**Epidemiology.**
- **Incidence:** ~**1.6 cases per million per year** (Sweden nationwide; rising to ~2.0/million in 2005–2013) ([PMID: 30799512](https://pubmed.ncbi.nlm.nih.gov/30799512/)).
- Endogenous CS incidence: 1.8–3.2 per million/year ([PMID: 33766428](https://pubmed.ncbi.nlm.nih.gov/33766428/)); CD comprises **~48%** of endogenous CS (~1.5/million/yr) ([PMID: 31094003](https://pubmed.ncbi.nlm.nih.gov/31094003/)).

> *"The incidence of CD in Sweden (1.6 cases per million)."* — [PMID: 30799512](https://pubmed.ncbi.nlm.nih.gov/30799512/)

**Inheritance.** Predominantly **sporadic/somatic** (not inherited). A minority are syndromic (MEN1, MEN4, Carney complex, FIPA) with autosomal dominant inheritance and incomplete, age-dependent penetrance.

**Demographics.**
- **Sex ratio:** Female predominance ~**3:1**; *USP8*-mutant tumors are almost exclusively female (OR 4.52).
- **Age distribution:** Peak onset 3rd–5th decade.
- **Race/ethnicity differences:** Black patients present younger, higher BMI, near-uniformly solid tumors, higher radiographic persistence (38% vs 21%) and reintervention (25% vs 4.5%); Hispanic patients present with milder disease; durable remission comparable across groups (79–88%) ([PMID: 42560567](https://pubmed.ncbi.nlm.nih.gov/42560567/)).

> *"Black patients were younger (p = 0.003), with higher BMI (p = 0.033) and near-uniformly solid tumors (94%; p = 0.040)."* — [PMID: 42560567](https://pubmed.ncbi.nlm.nih.gov/42560567/)

---

## 10. Diagnostics

**Screening / first-line biochemical tests** (Endocrine Society approach; [PMID: 28069628](https://pubmed.ncbi.nlm.nih.gov/28069628/)):
- 24-hour urinary free cortisol (UFC)
- Late-night salivary cortisol
- Overnight 1-mg dexamethasone suppression test (DST) / low-dose 48-hour DST

**Confirming ACTH-dependence and source:**
- Plasma ACTH (elevated/inappropriately normal → ACTH-dependent)
- High-dose DST; CRH stimulation test
- **Bilateral inferior petrosal sinus sampling (BIPSS)** — gold standard to distinguish pituitary from ectopic ACTH source

**Imaging:** Pituitary MRI (dynamic/3D spoiled gradient echo improves microadenoma detection), but localization is strongly **reader-dependent** with fair-to-moderate interrater agreement (κ = 0.34–0.44); consensus interpretation improves performance ([PMID: 42537231](https://pubmed.ncbi.nlm.nih.gov/42537231/)). ~10% are MRI-negative, raising the risk of misdiagnosed ectopic ACTH tumors ([PMID: 42517988](https://pubmed.ncbi.nlm.nih.gov/42517988/)).

**Pathology / IHC:** ACTH-positive, TPIT/TBX19-positive corticotroph adenoma; Crooke cell change indicates aggressive subtype.

**Genetic testing:** Somatic tumor sequencing (*USP8*, *USP48*, *BRAF*, *TP53*) for prognostication; germline panels (*MEN1*, *AIP*, *CDKN1B*, *PRKAR1A*, *CDKN2A*) recommended in pediatric/young patients ([PMID: 40813536](https://pubmed.ncbi.nlm.nih.gov/40813536/)).

**Differential diagnosis:** Ectopic ACTH syndrome, adrenal Cushing (ACTH-independent), pseudo-Cushing states, and mild autonomous cortisol secretion (MACS).

---

## 11. Outcome / Prognosis

**Mortality.** CD carries a **2- to 9-fold excess mortality**, driven principally by cardiovascular disease and infection.

| Cohort | SMR | Key detail | Source |
|---|---|---|---|
| Swedish nationwide (n=502) | 2.5 (95% CI 2.1–2.9) | CVD leading cause (SMR 3.3); remission SMR still 1.9 | [PMID: 30715394](https://pubmed.ncbi.nlm.nih.gov/30715394/) |
| Oxford/Athens (n=311 CD) | 9.3 (95% CI 6.2–13.4) | 10-yr survival 95.3%; 71.4% deaths CV/infection | [PMID: 23996696](https://pubmed.ncbi.nlm.nih.gov/23996696/) |
| Italian 20-yr (n=126) | Persistent 4.99; remission 1.66 (NS) | Remission status is key determinant | [PMID: 37495935](https://pubmed.ncbi.nlm.nih.gov/37495935/) |

> *"The observed number of deaths was 133 vs 54 expected, resulting in an overall SMR of 2.5... The commonest cause of death was cardiovascular diseases (SMR, 3.3)."* — [PMID: 30715394](https://pubmed.ncbi.nlm.nih.gov/30715394/)

**Morbidity & complications:** Hypertension, diabetes, osteoporosis/fractures, venous thromboembolism, infections/sepsis, neuropsychiatric disease, reproductive dysfunction, and (reported) hepatic hemangioma. **Venous thromboembolism** is a key preventable complication: pooled post-operative VTE incidence 2% (58/2997) with VTE-associated mortality 0.2% ([PMID: 39182834](https://pubmed.ncbi.nlm.nih.gov/39182834/)).

> *"Pooled postoperative VTE incidence in patients undergoing transsphenoidal surgery for CD was 2% (58 out of 2997)."* — [PMID: 39182834](https://pubmed.ncbi.nlm.nih.gov/39182834/)

**Prognostic factors:** Remission status is the strongest determinant of long-term survival. Post-operative nadir cortisol ≤3 µg/dL predicts durable remission (AUC 0.808); macroadenomas and *USP8*-mutant status predict higher recurrence ([PMID: 40257708](https://pubmed.ncbi.nlm.nih.gov/40257708/); [PMID: 40424186](https://pubmed.ncbi.nlm.nih.gov/40424186/)).

**Quality of life:** Persistently impaired years after cure ([PMID: 35311897](https://pubmed.ncbi.nlm.nih.gov/35311897/)).

---

## 12. Treatment

**First-line: Transsphenoidal surgery (TSS)** — adenomectomy. Initial remission ~**81%**, recurrence ~**27.4%** (median 38 months); nadir cortisol ≤3 µg/dL and microadenoma status predict durable remission (NCIT: Transsphenoidal Hypophysectomy).

> *"Surgical remission was achieved in 81% of patients, but recurrence occurred in 27.4% of cases after a median follow up period of 38 months."* — [PMID: 40257708](https://pubmed.ncbi.nlm.nih.gov/40257708/)

**Pharmacotherapy (for persistent/recurrent/inoperable disease):**

| Drug | Class / mechanism (NCIT) | Efficacy | Key toxicity | Source |
|---|---|---|---|---|
| **Osilodrostat** | 11β-hydroxylase (CYP11B1) inhibitor | 77% vs 8% placebo achieved mUFC ≤ULN at wk 12; 81% at wk 36; median time to control 35 days | Adrenal insufficiency, nausea, hypocortisolism, tumor enlargement | [PMID: 35325149](https://pubmed.ncbi.nlm.nih.gov/35325149/); [PMID: 32730798](https://pubmed.ncbi.nlm.nih.gov/32730798/); [PMID: 41052284](https://pubmed.ncbi.nlm.nih.gov/41052284/) |
| **Pasireotide** | Pituitary-directed SSTR5 somatostatin analog | ~50–53% mUFC control | Hyperglycemia (39.5%), nausea, cholelithiasis | [PMID: 37876540](https://pubmed.ncbi.nlm.nih.gov/37876540/); [PMID: 31465533](https://pubmed.ncbi.nlm.nih.gov/31465533/) |
| **Cabergoline** | Dopamine agonist (D2) | Adjunct, variable | Generally well tolerated | [PMID: 37876540](https://pubmed.ncbi.nlm.nih.gov/37876540/) |
| **Metyrapone / Ketoconazole / Levoketoconazole** | Steroidogenesis inhibitors | Effective cortisol lowering | Hepatotoxicity (keto), adrenal insufficiency | [PMID: 26133755](https://pubmed.ncbi.nlm.nih.gov/26133755/) |
| **Mifepristone** | Glucocorticoid receptor antagonist | Controls hypercortisolism effects | Hypokalemia, endometrial effects | [PMID: 42533758](https://pubmed.ncbi.nlm.nih.gov/42533758/) |

> *"At week 12, significantly more osilodrostat (77%) than placebo (8%) patients achieved mUFC ≤ ULN (odds ratio 43.4; 95% CI 7.1, 343.2; P < 0.0001)."* — [PMID: 35325149](https://pubmed.ncbi.nlm.nih.gov/35325149/)

> *"Thirty-four patients (50.0%; 95% CI 37.6-62.4) achieved the primary endpoint."* (pasireotide ± cabergoline) — [PMID: 37876540](https://pubmed.ncbi.nlm.nih.gov/37876540/)

**Second-line / other:** Pituitary radiotherapy (conventional or stereotactic; slow onset), repeat TSS, and **bilateral adrenalectomy** (definitive cortisol control but requires lifelong replacement and risks Nelson syndrome). Drug treatment is frequently discontinued long-term (only 38% of one cohort remained on it as final treatment; [PMID: 37962981](https://pubmed.ncbi.nlm.nih.gov/37962981/)).

**Supportive care:** Antihypertensives, glycemic control, osteoporosis management, and **VTE prophylaxis** — routine rivaroxaban (10 mg/day) was safe with no major/minor bleeding in ACTH-dependent CS ([PMID: 41540719](https://pubmed.ncbi.nlm.nih.gov/41540719/)).

**Pharmacogenomics / personalized medicine:** *USP8* status may guide expectations for recurrence; Asian patients require lower osilodrostat doses and show more hypocortisolism-related AEs than non-Asian patients ([PMID: 39183039](https://pubmed.ncbi.nlm.nih.gov/39183039/)).

---

## 13. Prevention

Because CD arises from sporadic somatic mutation, **primary prevention is not applicable** — there is no known modifiable risk factor or vaccine.

- **Secondary prevention (early detection):** Targeted case-finding using the overnight 1-mg DST in high-risk groups (resistant type 2 diabetes, resistant hypertension, adrenal incidentalomas) can uncover treatable hypercortisolism ([PMID: 42591054](https://pubmed.ncbi.nlm.nih.gov/42591054/); [PMID: 42533758](https://pubmed.ncbi.nlm.nih.gov/42533758/)). Population-wide screening is **not** recommended.
- **Tertiary prevention (complication prevention):** Aggressive control of hypertension, hyperglycemia, osteoporosis, and thromboprophylaxis; close post-surgical surveillance for recurrence.
- **Genetic counseling:** Indicated for syndromic/pediatric cases with germline predisposition (MEN1, Carney complex, FIPA).

---

## 14. Other Species / Natural Disease

**Cushing disease occurs naturally in dogs** as **pituitary-dependent hyperadrenocorticism (PDH)** — the leading spontaneous animal model, comprising ~80–85% of canine Cushing's.

> *"Hypercortisolism is well defined in dogs, with well established and extensively documented clinical signs, various diagnostic methods and treatment options available."* — [PMID: 42440375](https://pubmed.ncbi.nlm.nih.gov/42440375/)

- **Taxonomy:** *Canis lupus familiaris* (NCBI Taxon 9615); also reported in guinea pigs, *Cavia porcellus* (NCBI Taxon 10141).
- **Natural disease:** Canine PDH features defined clinical signs, validated diagnostics (low-dose dexamethasone suppression, urinary corticoid:creatinine ratio, endogenous ACTH), and medical therapy with **trilostane** (3β-HSD/steroidogenesis inhibitor). A naturally occurring ACTH-dependent **pituitary blastoma** (TBX19/TPIT+, ACTH+) was documented in a dog ([PMID: 42177605](https://pubmed.ncbi.nlm.nih.gov/42177605/)).
- **Comparative biology:** Corticotroph lineage markers (TPIT/TBX19) and ACTH-driven pathophysiology are conserved between dogs and humans, supporting cross-species mechanistic relevance.
- **Zoonotic potential:** *Not applicable* (non-communicable).

---

## 15. Model Organisms

**Principal in vitro model: AtT-20** — the murine (mouse) pituitary corticotroph adenoma cell line, the standard preclinical model for ACTH-secreting tumors, used both in culture and as nude-mouse xenografts.

- **HDAC inhibitor SAHA (vorinostat)** reduces POMC transcription and ACTH secretion in human and murine (AtT-20) cells and suppresses xenograft growth ([PMID: 28505327](https://pubmed.ncbi.nlm.nih.gov/28505327/)).
- **Romidepsin** (HDAC1/2 inhibitor) suppresses ACTH via PTTG1 downregulation in AtT-20 cells ([PMID: 33181265](https://pubmed.ncbi.nlm.nih.gov/33181265/)).
- Additional AtT-20 mechanistic studies implicate ER stress / PCSK1N ([PMID: 39288010](https://pubmed.ncbi.nlm.nih.gov/39288010/)) and FAF1 ([PMID: 38065537](https://pubmed.ncbi.nlm.nih.gov/38065537/)).

**Model types:** Cellular/in vitro (AtT-20; human primary corticotroph cultures), murine xenografts, and spontaneous canine disease (natural model). **Limitations:** AtT-20 cells do not carry the human *USP8* hotspot mutation; no widely-used genetically engineered mouse recapitulates human *USP8*-driven CD, limiting fidelity of driver-mechanism modeling. **Resources:** MGI (mouse), Cellosaurus (AtT-20).

---

## Mechanistic Model / Interpretation

Cushing disease is best understood as a **two-tier disorder**: (1) a **corticotroph tumor tier**, in which somatic driver mutations — chiefly *USP8*, with *USP48* and *BRAF* — converge on enhanced POMC/ACTH output, while a divergent aggressive subset defined by *TP53/ATRX/DAXX* drives invasion and silent phenotypes; and (2) a **systemic hypercortisolism tier**, in which autonomous ACTH escapes partial glucocorticoid feedback, chronically stimulates the adrenal cortex, and produces cortisol-mediated end-organ damage across cardiovascular, metabolic, skeletal, hematologic, reproductive, and neuropsychiatric systems.

The unifying diagnostic and therapeutic logic follows directly from this model: (a) **feedback resistance** underlies the dexamethasone suppression test; (b) **ACTH-dependence** localizes the lesion via BIPSS; (c) the tumor tier is addressed by **surgery/radiotherapy/pituitary-directed pasireotide**, while the hypercortisolism tier is addressed by **steroidogenesis inhibitors (osilodrostat, metyrapone, ketoconazole)**, **GR blockade (mifepristone)**, or **bilateral adrenalectomy**. Because cortisol-driven cardiovascular and thrombotic damage accumulates over time and does not fully reverse, **early biochemical control** is the dominant prognostic lever — remission converts a 5–9× mortality risk toward (though not fully to) baseline.

```
GENOTYPE                PHENOTYPE                      OUTCOME
USP8/USP48/BRAF  ──►  ↑POMC/ACTH ──► cortisol ──►  cushingoid multisystem disease
(favorable)          (feedback-resistant)          │
                                                    ├─ treated/remission → SMR ~1.7–1.9
TP53/ATRX/DAXX   ──►  aggressive/silent tumor       └─ persistent → SMR ~5–9 (CVD, infection)
(aggressive)
```

---

## Evidence Base

| PMID | Contribution | Type |
|---|---|---|
| [40392165](https://pubmed.ncbi.nlm.nih.gov/40392165/) | USP8 prevalence meta-analysis (31.1%), clinical associations | Meta-analysis |
| [38862897](https://pubmed.ncbi.nlm.nih.gov/38862897/) | USP8 gain-of-function → ACTH secretion mechanism | Review/experimental |
| [42273717](https://pubmed.ncbi.nlm.nih.gov/42273717/) | Two divergent molecular pathways (USP8/USP48 vs TP53/ATRX) | WES/CNV/transcriptome |
| [42236012](https://pubmed.ncbi.nlm.nih.gov/42236012/) | Recurrent driver convergence on POMC/ACTH | Molecular review |
| [35742910](https://pubmed.ncbi.nlm.nih.gov/35742910/) | Glucocorticoid-feedback resistance as core pathophysiology | Review |
| [31164868](https://pubmed.ncbi.nlm.nih.gov/31164868/) | Hypertension mechanism (mineralocorticoid mimicry) | Review |
| [30715394](https://pubmed.ncbi.nlm.nih.gov/30715394/) | Nationwide SMR 2.5, CVD leading cause | Registry cohort |
| [37495935](https://pubmed.ncbi.nlm.nih.gov/37495935/) | Remission status determines mortality | 20-yr cohort |
| [40257708](https://pubmed.ncbi.nlm.nih.gov/40257708/) | Surgical remission 81%, recurrence 27.4% | Tertiary cohort |
| [40424186](https://pubmed.ncbi.nlm.nih.gov/40424186/) | USP8 predicts recurrence | Cohort |
| [35325149](https://pubmed.ncbi.nlm.nih.gov/35325149/) | Osilodrostat Phase III (LINC 4) efficacy | RCT |
| [37876540](https://pubmed.ncbi.nlm.nih.gov/37876540/) / [31465533](https://pubmed.ncbi.nlm.nih.gov/31465533/) | Pasireotide efficacy (~50%) and hyperglycemia | Phase II/III |
| [39182834](https://pubmed.ncbi.nlm.nih.gov/39182834/) / [41540719](https://pubmed.ncbi.nlm.nih.gov/41540719/) | VTE burden and prophylaxis | Systematic review / cohort |
| [42572239](https://pubmed.ncbi.nlm.nih.gov/42572239/) | Phenotype frequencies, demographics | Tertiary cohort |
| [35311897](https://pubmed.ncbi.nlm.nih.gov/35311897/) | Persistent socioeconomic/QoL impairment | Nationwide cohort |
| [30799512](https://pubmed.ncbi.nlm.nih.gov/30799512/) / [31094003](https://pubmed.ncbi.nlm.nih.gov/31094003/) / [33766428](https://pubmed.ncbi.nlm.nih.gov/33766428/) | Incidence (~1.6/million; CD ~48% of CS) | Registry/epidemiology |
| [40666832](https://pubmed.ncbi.nlm.nih.gov/40666832/) / [38167466](https://pubmed.ncbi.nlm.nih.gov/38167466/) / [39934142](https://pubmed.ncbi.nlm.nih.gov/39934142/) | Single-cell/spatial tumor heterogeneity | scRNA/spatial-seq |
| [42095775](https://pubmed.ncbi.nlm.nih.gov/42095775/) | Lifespan-varying presentation | Clinical review |
| [42560567](https://pubmed.ncbi.nlm.nih.gov/42560567/) / [42445877](https://pubmed.ncbi.nlm.nih.gov/42445877/) | Race/ethnicity differences; HPG suppression | Cohorts |
| [42440375](https://pubmed.ncbi.nlm.nih.gov/42440375/) / [42177605](https://pubmed.ncbi.nlm.nih.gov/42177605/) | Canine natural disease model | Veterinary |
| [28505327](https://pubmed.ncbi.nlm.nih.gov/28505327/) / [33181265](https://pubmed.ncbi.nlm.nih.gov/33181265/) | AtT-20 preclinical model | In vitro/xenograft |

---

## Limitations and Knowledge Gaps

1. **Epidemiology skew:** Incidence estimates derive largely from Swedish/European registries; global and low-income-country data are sparse, and figures may underestimate mild/subclinical disease (MACS).
2. **Germline landscape under-characterized:** The genetic basis of most pediatric and sporadic corticotroph tumors remains unknown beyond the somatic drivers.
3. **Epigenetics:** DNA methylation/histone-modification atlases for CD are still emerging; mechanistic epigenetic drivers are not fully defined.
4. **Imaging limitation:** MRI microadenoma localization is reader-dependent and ~10% MRI-negative, contributing to misdiagnosis of ectopic ACTH tumors.
5. **Model fidelity:** No standard genetically engineered mouse recapitulates human *USP8*-driven CD; AtT-20 lacks the human hotspot mutation.
6. **Residual risk after cure:** Mechanisms of persistent excess mortality and QoL impairment despite biochemical remission are incompletely understood.
7. **Metabolomics/proteomics/lipidomics** signatures specific to CD were not deeply catalogued in this investigation — a genuine data gap.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-stratified outcome registries:** Prospectively link somatic driver status (*USP8/USP48/BRAF/TP53*) to remission, recurrence, and mortality to formalize molecular prognostication.
2. **USP8-mutant mouse model:** Engineer a corticotroph-specific *Usp8* hotspot knock-in to test targeted EGFR/USP8 inhibition in vivo.
3. **Residual cardiovascular risk trials:** Test whether intensified cardiometabolic and thromboprophylactic management after remission normalizes the residual SMR (~1.9).
4. **Multi-omics integration:** Deploy CD-specific metabolomics/lipidomics/proteomics (MetaboLights, PRIDE) to define circulating biomarkers for early detection and monitoring.
5. **Imaging enhancement:** Validate consensus/AI-assisted MRI reads and molecular PET tracers to reduce MRI-negative misclassification.
6. **Targeted therapy translation:** Advance EGFR-pathway and HDAC-inhibitor (SAHA/romidepsin) strategies from AtT-20/xenograft to early-phase human trials.

---

## Consensus Answer

Cushing disease is a rare endocrine disorder (incidence ~1.6 cases/million/year; ~48% of endogenous Cushing syndrome) caused by a benign ACTH-secreting pituitary corticotroph adenoma driving chronic cortisol excess — most commonly via somatic gain-of-function *USP8* mutations (~31%; also *USP48*, *BRAF*) that enhance POMC/ACTH output amid partial glucocorticoid-feedback resistance, while aggressive tumors carry *TP53/ATRX* alterations. It produces a multisystem cushingoid phenotype (central obesity, myopathy, hypertension, diabetes, osteoporosis, thromboembolism, neuropsychiatric and reproductive dysfunction) with 2–9× excess mortality driven chiefly by cardiovascular disease. First-line treatment is transsphenoidal adenomectomy (~80% remission, ~15–27% recurrence), with medical therapy (osilodrostat, pasireotide, cabergoline, metyrapone, ketoconazole, mifepristone), radiotherapy, and bilateral adrenalectomy for persistent or recurrent disease.


## Artifacts

- [OpenScientist final report](Cushing_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cushing_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 46 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 46 |
| On topic | 30 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005479` (2 mentions) - the report calls it "Cushing disease"; MONDO calls it **atrial tachycardia**
- `HP:0000858` (1 mention) - the report calls it "Secondary amenorrhea"; HP calls it **Irregular menstruation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003118` (1 mention) - the report calls it "Abnormal circulating cortisol"; HP calls it **Increased circulating cortisol level**
- `GO:0030518` (1 mention) - the report calls it "intracellular receptor signaling"; GO calls it **nuclear receptor-mediated steroid hormone signaling pathway**, and lists "intracellular steroid hormone receptor signaling pathway" among its other names
- `GO:0007173` (1 mention) - the report calls it "EGFR signaling"; GO calls it **epidermal growth factor receptor signaling pathway**, and lists "EGFR signaling pathway" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.