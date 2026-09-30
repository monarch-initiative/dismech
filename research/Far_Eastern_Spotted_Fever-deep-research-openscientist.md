---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-28T01:03:19.690950'
end_time: '2026-09-28T01:17:01.375014'
duration_seconds: 821.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Far Eastern Spotted Fever
  mondo_id: MONDO:0000231
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
citation_count: 15
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 14
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 28
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0200042
    reported_labels:
    - Inoculation eschar (tache noire)
    ontology_label: Skin ulcer
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Far_Eastern_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Far_Eastern_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Far Eastern Spotted Fever
- **MONDO ID:** MONDO:0000231 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Far Eastern Spotted Fever** covering all of the
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

# Far Eastern Spotted Fever (FESF): Comprehensive Disease Characterization Report

**Disease:** Far Eastern Spotted Fever (Far Eastern tick-borne rickettsiosis)
**MONDO ID:** MONDO:0000231
**Category:** Infectious Disease (zoonotic, tick-borne, spotted fever group rickettsiosis)
**Causative agent:** *Rickettsia heilongjiangensis*

---

## Summary

Far Eastern Spotted Fever (FESF) is an acute, generally self-limited, zoonotic tick-borne rickettsiosis caused by *Rickettsia heilongjiangensis*, an obligate intracellular, Gram-negative alphaproteobacterium of the spotted fever group (SFGR). First documented as a distinct human disease in the Russian Far East, the illness is transmitted primarily by *Haemaphysalis concinna* ticks and is maintained in nature through a tick–wild-mammal cycle involving reservoir hosts such as hedgehogs (*Erinaceus amurensis*) and small mammals. Its geographic range spans temperate Northeast Asia — the Russian Far East, northern and eastern China, Inner Mongolia, Korea, Japan — and has recently extended westward to Kazakhstan.

Mechanistically, FESF is a **rickettsial vasculitis**. After tick inoculation, the bacterium disseminates and preferentially infects **vascular endothelial cells**, using surface adhesins (OmpB, YbgF, RpsB) to adhere to and invade the endothelium. Intracellular replication triggers vascular inflammation, increased vascular permeability, and small-vessel injury, producing the characteristic clinical tetrad of **high fever, an inoculation eschar (tache noire) at the tick-bite site, a maculopapular rash, and regional lymphadenopathy**. A subset of patients develop gastrointestinal symptoms, consistent with a C57BL/6 mouse model that identified the **stomach** as a target organ. Host defense is dominated by a **Th1-polarized, IFN-γ/TNF-α–driven, CD4⁺/CD8⁺ T-cell response**, with endothelial Tim-3 upregulation promoting nitric-oxide/iNOS-mediated intracellular killing.

FESF is diagnosed by **indirect immunofluorescence assay (IFA) seroconversion combined with molecular detection (nested PCR, NGS/mNGS)** of blood, eschar, or skin biopsy targeting rickettsial genes (*gltA, ompA, ompB, 16S rRNA/rrs, sca4*). It responds rapidly to **doxycycline**, the first-line therapy; delayed treatment is the principal modifiable driver of severe outcomes. Prognosis is generally favorable and the disease sits at the mild end of the SFGR spectrum (in contrast to Rocky Mountain spotted fever), though rare severe complications (leukocytoclastic vasculitis, multi-organ dysfunction, hemophagocytic lymphohistiocytosis) are described across SFGR. There is **no human genetic component and no licensed vaccine**; prevention rests on personal anti-tick measures (DEET, permethrin-treated clothing, protective clothing, body checks, prompt tick removal).

This report consolidates 14 confirmed findings drawn from 57 reviewed papers across all 15 requested disease-characteristic domains, with explicit indication of where information is unavailable or not applicable (notably the genetic/molecular, inheritance, and model-organism domains, which are largely not applicable to an infectious vasculitis with no host Mendelian basis).

---

## Key Findings

### F001 — Etiology: *Rickettsia heilongjiangensis* is the causative agent

FESF is caused by ***Rickettsia heilongjiangensis***, a spotted fever group rickettsia. The first documented human cases were reported in the Russian Far East by Mediannikov and colleagues, who named the disease "Far Eastern tick-borne rickettsiosis." The organism is an obligate intracellular, Gram-negative bacterium.

> *"We recently reported the first documented cases of a new rickettsial disease caused by Rickettsia heilongjiangensis in the Russian Far East (Far Eastern tick-borne rickettsiosis)."* — [PMID: 17114683](https://pubmed.ncbi.nlm.nih.gov/17114683/)

> *"Rickettsia heilongjiangensis is the pathogen of Far eastern spotted fever"* — [PMID: 26401029](https://pubmed.ncbi.nlm.nih.gov/26401029/)

This establishes the disease as an **infectious**, not genetic, condition. **Organism annotation:** *Rickettsia heilongjiangensis* (NCBI Taxonomy; family Rickettsiaceae, genus *Rickettsia*, spotted fever group).

### F002 — Vector: *Haemaphysalis concinna* is the principal tick vector

Screening of Russian Far Eastern ticks found up to **28.13% of *H. concinna*** and **4.48% of *H. japonica douglasii*** harbored *R. heilongjiangensis*; rickettsial DNA was amplified from both a patient's skin biopsy and the tick removed from that patient before illness onset. Additional hard-tick surveys along the Chinese–Russian border confirm a broader vector complex (*Ixodes persulcatus*, *H. concinna*, *H. japonica*, *Dermacentor silvarum*).

> *"It has been concluded that H. concinnae may serve as the main vector for the transmission of R. heilongjiangensis."* — [PMID: 17114683](https://pubmed.ncbi.nlm.nih.gov/17114683/)

> *"up to 28.13% of H. concinnae and 4.48% of H. japonica douglasii ticks harbor R. heilongjiangensis"* — [PMID: 17114683](https://pubmed.ncbi.nlm.nih.gov/17114683/)

### F003 — Target cell and core mechanism: endothelial-tropic rickettsial vasculitis

The **vascular endothelium is the primary cellular target** of *R. heilongjiangensis*, and disease results from endothelial infection with attendant vascular inflammation. Spotted fever group rickettsiae broadly cause endothelial infection, vascular inflammation, and compromised vascular permeability — collectively termed **"rickettsial vasculitis."** In endothelial cells, upregulation of T-cell immunoglobulin and mucin domain protein 3 (Tim-3) facilitates intracellular rickettsial killing via nitric oxide/iNOS and IFN-γ.

> *"T-cell immunoglobulin and mucin domain protein 3 (Tim-3) is expressed in human vascular endothelial cells, the major target cells of rickettsiae"* — [PMID: 26401029](https://pubmed.ncbi.nlm.nih.gov/26401029/)

> *"the pathogen's affinity for endothelium lining the blood vessels, the consequences of which are vascular inflammation, insult to vascular integrity and compromised vascular permeability, collectively termed 'Rickettsial vasculitis'"* — [PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)

**Ontology suggestions:** Cell type — endothelial cell (**CL:0000115**), vascular endothelial cell (**CL:0002139**); process — inflammatory response (**GO:0006954**), regulation of vascular permeability (**GO:0043114**).

### F004 — Geographic distribution: temperate Northeast Asia, extending to Kazakhstan

*R. heilongjiangensis* has been detected in ticks and/or patients across the Chinese–Russian border (Suifenhe), Inner Mongolia (Yakeshi/Hulunbuir, 2.68% of ticks), and southeast China (hedgehogs and ticks), and was first reported in Kazakhstan in 2023 — documenting a westward extension of the known range.

> *"To the best of our knowledge, this study reports the first finding of R. heilongjiangensis in Kazakhstan."* — [PMID: 37722147](https://pubmed.ncbi.nlm.nih.gov/37722147/)

> *"The present study gave the first evidence of R. heilongjiangensis and Candidatus R. xuyiensis in ticks and hedgehogs of Southeast China. Our findings suggest that hedgehogs might be involved in the natural transmission cycle of Rickettsia species."* — [PMID: 36097185](https://pubmed.ncbi.nlm.nih.gov/36097185/)

### F005 — Organ tropism: stomach identified as a target organ (mouse model)

Using click-chemistry labeling and *in vivo* imaging in a **C57BL/6 tick-bite-simulating infection model**, the **stomach** was identified as a target organ of *R. heilongjiangensis*, providing a mechanistic explanation for the gastrointestinal symptoms seen in some patients.

> *"we constructed a C57BL/6 mice infection model by simulating tick bites and discovered that the stomach is the target organ of R. heilongjiangensis infection through in vivo imaging systems, which explained the occurrence of gastrointestinal symptoms following R. heilongjiangensis infection in some cases"* — [PMID: 38951577](https://pubmed.ncbi.nlm.nih.gov/38951577/)

**Ontology suggestion:** stomach (**UBERON:0000945**).

### F006 — Clinical phenotype: eschar–rash–fever–lymphadenopathy tetrad

FESF presents as a spotted fever group rickettsiosis with seroconversion to *R. heilongjiangensis* antigen and rickettsial DNA amplifiable from skin biopsy. The characteristic eschar-associated SFGR tetrad comprises **high fever (~39–40 °C), erythematous maculopapular eruption, an inoculation eschar (tache noire) at the tick-bite site, and regional lymphadenopathy**. Gastrointestinal symptoms occur in a subset. Headache, myalgia/arthralgia, and laboratory thrombocytopenia and elevated transaminases are common across SFGR.

> *"The clinical picture was that of a spotted fever group rickettsiosis and a seroconversion was noted with R. heilongjiangensis antigen."* — [PMID: 17114683](https://pubmed.ncbi.nlm.nih.gov/17114683/)

> *"His clinical symptoms on admission were high fever (39.6 degrees C), erythematous eruption, eschar on the right upper arm, and regional lymphoadenopathy."* — [PMID: 15858293](https://pubmed.ncbi.nlm.nih.gov/15858293/)

**HPO term suggestions:** Fever (**HP:0001945**); Maculopapular exanthema (**HP:0000988**); Skin ulcer / eschar (**HP:0200042**); Lymphadenopathy (**HP:0002716**); Headache (**HP:0002315**); Myalgia (**HP:0003326**); Arthralgia (**HP:0002829**); Thrombocytopenia (**HP:0001873**); Elevated hepatic transaminase (**HP:0002910**); Gastrointestinal symptoms (**HP:0011024**).

### F007 — Treatment: doxycycline is first-line; delayed therapy worsens outcomes

Early doxycycline is effective against SFGR, and delayed treatment increases the risk of severe outcomes. Tetracycline-class agents (doxycycline; minocycline used in Japan) are the mainstay for spotted fever rickettsioses. For the severe-end comparator Rocky Mountain spotted fever, delayed doxycycline (>5 days from onset) is independently associated with fatality.

> *"Early administration of doxycycline is effective against SFGR infection, and delayed treatment increases the risk of severe outcomes."* — [PMID: 42488420](https://pubmed.ncbi.nlm.nih.gov/42488420/)

> *"Fatal outcomes were associated with delayed doxycycline treatment (>5 days after symptom onset)"* — [PMID: 41714602](https://pubmed.ncbi.nlm.nih.gov/41714602/)

**NCIT suggestions:** Doxycycline (**NCIT:C312**); Minocycline (**NCIT:C61815**).

### F008 — Diagnosis: serology (IFA seroconversion) plus molecular detection (PCR/NGS)

Original FESF cases were confirmed by seroconversion to *R. heilongjiangensis* antigen and PCR amplification of rickettsial DNA from skin biopsy and the attached tick. Contemporary confirmation uses nested PCR of rickettsia-specific gene fragments (*gltA, ompA, ompB, 16S rRNA/rrs, sca4*) with sequencing plus serology; NGS/metagenomic NGS is recommended especially for acute tick-bitten patients and enables diagnosis in atypical cases.

> *"Here we report the amplification of DNA of R. heilongjiangensis from both the skin biopsy of an acutely ill patient and the tick removed from him prior to the disease development."* — [PMID: 17114683](https://pubmed.ncbi.nlm.nih.gov/17114683/)

> *"The methods of nucleic acid diagnosis, such as nPCR and next-generation sequencing (NGS), should be implemented especially in acute tick-bitten patients."* — [PMID: 42488420](https://pubmed.ncbi.nlm.nih.gov/42488420/)

### F009 — Prognosis: generally favorable/self-limited, rare severe complications

FESF is regarded as a relatively mild, non-fatal SFGR compared with Rocky Mountain spotted fever; the index Russian Far East cases recovered. However, eschar-forming SFGR can rarely progress to leukocytoclastic vasculitis, multi-organ dysfunction, and hemophagocytic lymphohistiocytosis (HLH), and delayed treatment increases severity. RMSF case-fatality (~20% untreated, and 30–80% in some recent South American/Mexican series) illustrates the severe end of the SFGR spectrum, whereas FESF sits at the milder end.

> *"delayed treatment increases the risk of severe outcomes"* — [PMID: 42488420](https://pubmed.ncbi.nlm.nih.gov/42488420/)

> *"The clinical picture was that of a spotted fever group rickettsiosis and a seroconversion was noted with R. heilongjiangensis antigen."* — [PMID: 17114683](https://pubmed.ncbi.nlm.nih.gov/17114683/)

### F010 — Molecular pathogenesis: surface adhesins and Th1 protective immunity

Surface adhesins mediate endothelial adhesion/invasion, and protective immunity is Th1-polarized. **OmpB** is a major surface protein antigen; OmpB-pulsed dendritic cells confer protection in C3H/HeN mice with elevated CD4⁺/CD8⁺ T-cell IFN-γ and TNF-α. The surface antigen **YbgF** induces Th1-type protective immunity (increased IgG2a/IgG1), and anti-YbgF serum significantly reduces rickettsial adhesion to and invasion of endothelial cells. The ribosomal protein **RpsB** is a surface-exposed adhesin. Endothelial **Tim-3** upregulation drives iNOS/NO- and IFN-γ-dependent intracellular killing.

> *"Incubation with anti-serum to YbgF, but not PrsA, significantly reduced the number of rickettsiae adhering to and invading endothelial cells."* — [PMID: 24113261](https://pubmed.ncbi.nlm.nih.gov/24113261/)

> *"YbgF is a novel protective antigen that induces a Th1-type of protective immune response against R. heilongjiangensis infection."* — [PMID: 24113261](https://pubmed.ncbi.nlm.nih.gov/24113261/)

> *"Identification of a Ribosomal Protein RpsB as a Surface-Exposed Protein and Adhesin"* — [PMID: 31360728](https://pubmed.ncbi.nlm.nih.gov/31360728/)

**Ontology suggestions:** T-helper 1 type immune response (**GO:0042088**); positive regulation of nitric oxide biosynthetic process (**GO:0045429**); CD4⁺ αβ T cell (**CL:0000624**); CD8⁺ αβ T cell (**CL:0000625**); dendritic cell (**CL:0000451**).

### F011 — Prevention: personal anti-tick measures; no licensed vaccine

No licensed human vaccine exists for FESF/SFGR. Primary prevention relies on personal protection against tick bites — topical DEET on skin, permethrin-treated clothing, protective clothing (trousers tucked into boots), avoiding tick-infested habitats, body checks, and prompt tick removal. Experimental vaccine antigens (OmpB, YbgF) protect mice but are not clinically available. Secondary prevention is prompt empiric doxycycline after tick exposure with compatible illness.

> *"The best method to avoid tick bites is twofold: application of a topical deet (N,N-diethyl-m-toluamide) repellent to exposed skin, and treatment of clothing with permethrin."* — [PMID: 17338947](https://pubmed.ncbi.nlm.nih.gov/17338947/)

> *"YbgF is a novel protective antigen that induces a Th1-type of protective immune response against R. heilongjiangensis infection."* — [PMID: 24113261](https://pubmed.ncbi.nlm.nih.gov/24113261/)

### F012 — Risk factors: outdoor rural tick exposure with spring–summer seasonality

FESF is acquired via tick bite during outdoor activity; SFGR cases repeatedly report agricultural/forestry work and field exposure as the key risk factor. Reservoir hosts include hedgehogs (*Erinaceus amurensis*) and small mammals that maintain the tick cycle. Vector ticks are active in warm months, producing spring–summer seasonality. No genetic host risk factors are established; risk is **environmental/behavioral**.

> *"JSF should be a key consideration for agricultural and forestry workers presenting with compatible symptoms"* — [PMID: 40922296](https://pubmed.ncbi.nlm.nih.gov/40922296/)

> *"Our findings suggest that hedgehogs might be involved in the natural transmission cycle of Rickettsia species."* — [PMID: 36097185](https://pubmed.ncbi.nlm.nih.gov/36097185/)

### F013 — Molecular profiling: cutaneous immunoprofiling/RNA-seq of SFGR

Surveillance of tick-bitten patients (2013–2016) identified 111 SFGR cases; humoral and cutaneous immunoprofiles were evaluated by serum cytokine/chemokine detection, skin immunohistochemistry, and transcriptome sequencing (RNA-seq) to characterize the early host–rickettsia interaction in skin. This complements the endothelial-tropism/vasculitis model with transcriptomic and cytokine molecular-profiling evidence.

> *"Humoral and cutaneous immunoprofiles were evaluated in different SFGR cases by serum cytokine and chemokine detection, skin IHC staining, and transcriptome sequencing (RNA-seq)."* — [PMID: 31907196](https://pubmed.ncbi.nlm.nih.gov/31907196/)

### F014 — Identifiers, taxonomy, temporal course, and zoonotic classification

FESF is an acute, self-limited zoonotic tick-borne rickettsiosis. Causative organism: *Rickettsia heilongjiangensis* (domain Bacteria; family Rickettsiaceae; genus *Rickettsia*; spotted fever group), an obligate intracellular Gram-negative alphaproteobacterium. Onset is acute after an incubation of roughly several days to ~2 weeks following tick attachment; illness resolves over ~1–2 weeks with doxycycline. It is zoonotic (maintained in ticks and wild mammalian reservoirs), **not transmitted person-to-person**, and has **no genetic inheritance**.

> *"Rickettsia heilongjiangensis is an obligate intracellular bacterium that causes Far-Eastern tick-borne spotted fever."* — [PMID: 25270001](https://pubmed.ncbi.nlm.nih.gov/25270001/)

> *"a new rickettsial disease caused by Rickettsia heilongjiangensis in the Russian Far East (Far Eastern tick-borne rickettsiosis)"* — [PMID: 17114683](https://pubmed.ncbi.nlm.nih.gov/17114683/)

---

## Section-by-Section Characterization

### 1. Disease Information
- **Overview:** FESF is an acute febrile, tick-borne, spotted fever group rickettsiosis caused by *R. heilongjiangensis*, characterized by fever, inoculation eschar, maculopapular rash, and regional lymphadenopathy (F001, F006, F014).
- **Identifiers:** MONDO:0000231. There is **no OMIM entry** (not a Mendelian disorder). MeSH concept relates to "Rickettsia Infections"/"Spotted Fever Group." ICD-10 falls under **A77 (Spotted fever [tick-borne rickettsioses])**; ICD-11 under **1C30.0** (Spotted fever group rickettsiosis). Orphanet does not maintain a distinct FESF rare-disease number (infectious, not rare Mendelian, disease).
- **Synonyms:** Far Eastern tick-borne rickettsiosis; Far Eastern tick-borne spotted fever; *R. heilongjiangensis* infection (F001, F014).
- **Information source:** Aggregated disease-level resources (case reports, tick surveillance, animal models) — not EHR/individual-patient registries.

### 2. Etiology
- **Causal factor:** Infectious — *R. heilongjiangensis* (F001). Transmission is via tick bite (F002). **No genetic/host-Mendelian causation.**
- **Risk factors (environmental/behavioral):** Outdoor agricultural/forestry/recreational activity in endemic rural Northeast Asia; tick exposure; spring–summer season (F012). No established genetic risk factors, protective alleles, or gene–environment interactions (not applicable to a bacterial infection with no known host-genetic modifier). Empirically, **early doxycycline** is the principal factor mitigating severe disease (F007, F009).

### 3. Phenotypes
See F006. Principal phenotypes with suggested HPO terms and qualitative frequency (extrapolated from SFGR literature; FESF-specific frequencies are not precisely quantified):

| Phenotype | HPO term | Type | Frequency (qualitative) |
|---|---|---|---|
| Fever (~39–40 °C) | HP:0001945 | Symptom/sign | Very frequent (near-universal) |
| Maculopapular rash | HP:0000988 | Physical manifestation | Frequent |
| Inoculation eschar (tache noire) | HP:0200042 | Physical manifestation | Frequent (eschar-forming SFGR) |
| Regional lymphadenopathy | HP:0002716 | Clinical sign | Frequent |
| Headache | HP:0002315 | Symptom | Frequent |
| Myalgia / arthralgia | HP:0003326 / HP:0002829 | Symptom | Common |
| Gastrointestinal symptoms | HP:0011024 | Symptom | Subset (stomach tropism, F005) |
| Thrombocytopenia | HP:0001873 | Lab abnormality | Common |
| Elevated transaminases | HP:0002910 | Lab abnormality | Common |

- **Onset:** adult-predominant, acute. **Severity:** mild–moderate (variable). **Progression:** self-limited/episodic single illness. **QoL:** transient impairment during acute illness; full recovery expected with treatment (F009).

### 4. Genetic/Molecular Information
**Not applicable at the host level** — FESF is an infectious disease with no causal human genes, pathogenic host variants, modifier genes, host epigenetic drivers, or chromosomal abnormalities. The relevant "molecular" information is **pathogen-side**: bacterial surface adhesins/antigens **OmpB, YbgF, RpsB** (F010), and diagnostic marker genes *gltA, ompA, ompB, rrs (16S rRNA), sca4* (F008). Complete and comparative genome sequences of *R. heilongjiangensis* exist (e.g., PMID 36440590, 31866968).

### 5. Environmental Information
- **Environmental/lifestyle factors:** Outdoor rural exposure, agriculture/forestry, tick-infested habitats, warm-season activity (F012).
- **Infectious agent:** *Rickettsia heilongjiangensis* (SFGR), transmitted by *Haemaphysalis concinna* (principal), with *H. japonica*, *Ixodes persulcatus*, *Dermacentor silvarum*, and *H. longicornis* implicated in the vector complex; reservoirs include hedgehogs and small mammals (F001, F002, F004, F012).

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. An infected *Haemaphysalis concinna* tick attaches and inoculates *R. heilongjiangensis* into the skin during a blood meal → **leads to** local infection at the bite site. *(F002)*
2. Local replication and immune infiltration at the inoculation site → **results in** dermal/vascular necrosis forming the **eschar (tache noire)** and drainage to **regional lymph nodes** (lymphadenopathy). *(F006; inferred from SFGR eschar biology)*
3. Bacteria use surface adhesins (**OmpB, YbgF, RpsB**) to adhere to and invade **vascular endothelial cells** → **leads to** hematogenous/lymphatic dissemination and systemic endothelial infection. *(F003, F010)*
4. Intracellular replication within endothelium → **results in** endothelial activation, cyclooxygenase-2 induction and vasoactive prostaglandin release, cytokine/chemokine production, and increased **vascular permeability** ("rickettsial vasculitis"). *(F003; supported by SFGR endothelial studies)*
5. Small-vessel inflammation and microvascular leak in skin and other organs → **produces** the clinical **fever, maculopapular rash**, and (in a subset) **gastrointestinal symptoms** (stomach is a target organ). *(F003, F005, F006)*
6. Host response mounts a **Th1-polarized, IFN-γ/TNF-α, CD4⁺/CD8⁺ T-cell** program; endothelial **Tim-3 upregulation** drives **iNOS/NO-dependent intracellular killing** → **results in** bacterial clearance and, typically, self-limited recovery. *(F003, F010)*
7. **Branch (rare, severe):** if treatment is delayed or the host response dysregulates, widespread endothelial injury → **may lead to** leukocytoclastic vasculitis, multi-organ dysfunction, or hemophagocytic lymphohistiocytosis. *(F009; inferred from severe SFGR cases)*

**Upstream:** tick inoculation, adhesin-mediated endothelial invasion. **Downstream:** vasculitis, vascular permeability, organ-specific manifestations. **Cell types:** vascular endothelial cells (CL:0000115/CL:0002139), CD4⁺/CD8⁺ T cells, dendritic cells, macrophages. **GO processes:** inflammatory response (GO:0006954), regulation of vascular permeability (GO:0043114), T-helper 1 type immune response (GO:0042088), nitric oxide biosynthesis (GO:0045429).

### 7. Anatomical Structures Affected
- **Primary:** vascular endothelium / small blood vessels (**UBERON:0001981** blood vessel; **UBERON:0001986** endothelium) — systemic. Skin at bite site (eschar) and rash (**UBERON:0002097** skin of body).
- **Secondary/organ:** regional lymph nodes (**UBERON:0000029**); stomach (**UBERON:0000945**, F005); liver (transaminase elevation); rare lung, kidney, CNS involvement in severe SFGR.
- **Body systems:** cardiovascular (microvasculature), integumentary, lymphatic/immune, digestive (subset).
- **Subcellular:** intracellular cytosolic niche within endothelial cells (**GO:0005829** cytosol).
- **Lateralization:** eschar/lymphadenopathy typically localized/unilateral to bite site; rash bilateral/generalized.

### 8. Temporal Development
- **Onset:** acute, adult-predominant, after incubation of ~several days to ~2 weeks post tick attachment (F014).
- **Course:** self-limited single illness resolving over ~1–2 weeks with doxycycline (F014); untreated illness may be prolonged; severe complications rare (F009).
- **Critical window:** early treatment (ideally <5 days from onset) is the key window to prevent severe outcomes (F007, F009).

### 9. Inheritance and Population
- **Epidemiology:** Endemic to temperate Northeast Asia — Russian Far East, northern/eastern China, Inner Mongolia, Korea, Japan; recently Kazakhstan (F004). Tick infection prevalence up to ~28% in *H. concinna* (F002); regional tick positivity ~2.7–72% for various rickettsiae. Precise human incidence/prevalence per 100,000 is **not well quantified** (under-recognized; reported as case series).
- **Inheritance:** **Not applicable** — infectious, zoonotic, not inherited; no penetrance/expressivity/founder/consanguinity considerations (F014).
- **Demographics:** Higher exposure in rural, agricultural/forestry populations; spring–summer seasonality; sex/age distribution reflects occupational exposure rather than biological susceptibility (F012).

### 10. Diagnostics
- **Serology:** IFA seroconversion to *R. heilongjiangensis* antigen (paired sera) (F008, F006).
- **Molecular:** nested PCR of *gltA, ompA, ompB, rrs (16S rRNA), sca4* with sequencing; NGS/mNGS of blood, eschar, or skin biopsy — recommended for acute tick-bitten and atypical cases (F008).
- **Laboratory:** thrombocytopenia, elevated transaminases, elevated inflammatory markers (common SFGR pattern).
- **Histopathology:** perivascular lymphocytic infiltrates / small-vessel vasculitis on skin/eschar biopsy.
- **Differential diagnosis:** other SFGR (Japanese spotted fever/*R. japonica*, Mediterranean spotted fever/*R. conorii*, RMSF/*R. rickettsii*), scrub typhus, severe fever with thrombocytopenia syndrome (SFTS), ehrlichiosis/anaplasmosis, Lyme disease. Eschar plus regional lymphadenopathy in an endemic Northeast Asian tick-exposure context favors SFGR.
- **Genetic testing / newborn or carrier screening:** **Not applicable.**

### 11. Outcome / Prognosis
- **Generally favorable / self-limited**; low mortality at the mild end of the SFGR spectrum (F009). Full recovery expected with timely doxycycline.
- **Prognostic factor:** treatment delay is the dominant modifiable determinant of severity (F007, F009).
- **Rare complications:** leukocytoclastic vasculitis, multi-organ dysfunction, HLH (F009).

### 12. Treatment
- **First-line:** **Doxycycline** (tetracycline class; NCIT:C312), typically ~7 days; rapid defervescence expected. Minocycline (NCIT:C61815) used in Japan; chloramphenicol is an alternative. Early treatment is critical (F007).
- **Advanced/targeted/gene/cell/RNA therapies, surgery:** **Not applicable.**
- **Supportive care:** antipyretics, fluids, organ support in severe cases.
- **Personalized medicine / pharmacogenomics:** Not established for FESF.

### 13. Prevention
- **Primary:** personal anti-tick measures — DEET on skin, permethrin-treated clothing, protective clothing, avoiding tick habitats, body checks, prompt tick removal (F011). No licensed vaccine; OmpB/YbgF are experimental protective antigens in mice (F010, F011).
- **Secondary:** prompt empiric doxycycline after tick exposure with compatible illness (F011).
- **Public health:** vector/habitat awareness, occupational education for agricultural/forestry workers, tick surveillance (F004, F012).

### 14. Other Species / Natural Disease
- **Taxonomy of affected/involved species:** humans (accidental host); tick vectors *Haemaphysalis concinna*, *H. japonica*, *H. longicornis*, *Ixodes persulcatus*, *Dermacentor silvarum*; reservoir mammals including hedgehogs (*Erinaceus amurensis*) and small rodents (F002, F004, F012).
- **Natural disease:** *R. heilongjiangensis* is maintained enzootically in ticks and wild mammals; overt natural disease in animals is not well characterized (reservoirs typically asymptomatic).
- **Zoonotic transmission:** Yes — tick-borne zoonosis; **no person-to-person transmission** (F014).

### 15. Model Organisms
- **Mouse models:** **C57BL/6** tick-bite-simulating infection model (identified stomach tropism, F005); **C3H/HeN** mouse model used for OmpB- and YbgF-based protective-immunity/vaccine studies (F010). *R. australis* Balb/c model serves as a broader SFGR vasculopathy model.
- **Phenotype recapitulation:** models reproduce endothelial infection, organ tropism, and Th1 protective immunity; they do not fully recapitulate the human eschar–rash tetrad. No genetic (knockout/transgenic) *host* models are relevant since the disease is infectious.

---

## Mechanistic Model / Interpretation

```
   Infected Haemaphysalis concinna tick bite
                    │  (inoculation)
                    ▼
        Local skin infection ──────────────► ESCHAR (tache noire)
                    │                         + regional LYMPHADENOPATHY
                    │  adhesins: OmpB, YbgF, RpsB
                    ▼
     Endothelial adhesion & invasion (CL:0000115)
                    │
                    ▼
     Intracellular replication in endothelium
                    │
        ┌───────────┴─────────────┐
        ▼                         ▼
 Vascular inflammation      COX-2 induction,
 + ↑ permeability           vasoactive prostaglandins
 ("rickettsial vasculitis")
        │                         │
        ▼                         ▼
  FEVER, maculopapular RASH, GI symptoms (stomach tropism)
                    │
                    ▼
   Host Th1 response: IFN-γ/TNF-α, CD4+/CD8+ T cells;
   endothelial Tim-3 ↑ → iNOS/NO killing
                    │
         ┌──────────┴───────────┐
         ▼                      ▼
   Bacterial clearance      (rare, if Rx delayed)
   → self-limited recovery  → vasculitis / MODS / HLH
```

The unifying interpretation is that FESF is fundamentally a **microvascular endothelial infection**. Every clinical feature maps onto a step in the endothelial-vasculitis cascade: the eschar and lymphadenopathy from local inoculation-site injury and lymphatic drainage; the rash and fever from disseminated small-vessel inflammation and permeability change; GI symptoms from documented stomach tropism; and recovery from an effective Th1/NO-mediated clearance program. Doxycycline works upstream by halting intracellular bacterial replication, which is why **timing** is the dominant prognostic lever. The absence of any host-genetic basis means the "molecular/genetic" annotation for this disease is entirely pathogen-side (adhesins and diagnostic marker genes).

---

## Evidence Base

| PMID | Role in this report | Key contribution |
|---|---|---|
| [17114683](https://pubmed.ncbi.nlm.nih.gov/17114683/) | Foundational | First human cases; names disease; identifies *H. concinna* vector; PCR from skin + tick (F001, F002, F006, F008, F014) |
| [26401029](https://pubmed.ncbi.nlm.nih.gov/26401029/) | Mechanism | Endothelium as primary target; Tim-3/iNOS/IFN-γ intracellular killing (F001, F003, F010) |
| [19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/) | Mechanism | Defines "rickettsial vasculitis" (F003) |
| [38951577](https://pubmed.ncbi.nlm.nih.gov/38951577/) | Model/tropism | C57BL/6 tick-bite model; stomach target organ (F005) |
| [37722147](https://pubmed.ncbi.nlm.nih.gov/37722147/) | Epidemiology | First detection in Kazakhstan — range extension (F004) |
| [36097185](https://pubmed.ncbi.nlm.nih.gov/36097185/) | Epidemiology/reservoir | Hedgehogs in SE China transmission cycle (F004, F012) |
| [37986042](https://pubmed.ncbi.nlm.nih.gov/37986042/) | Epidemiology | Inner Mongolia tick hotspot, 2.68% prevalence (F004) |
| [26976703](https://pubmed.ncbi.nlm.nih.gov/26976703/) | Vector | SFGR incl. *R. heilongjiangensis* in Chinese–Russian border ticks (F002, F004) |
| [15858293](https://pubmed.ncbi.nlm.nih.gov/15858293/) | Clinical | Illustrative eschar–fever–rash–lymphadenopathy tetrad (F006) |
| [42488420](https://pubmed.ncbi.nlm.nih.gov/42488420/) | Treatment/Dx | Early doxycycline efficacy; nPCR/NGS diagnosis (F007, F008, F009) |
| [41714602](https://pubmed.ncbi.nlm.nih.gov/41714602/) | Prognosis | Delayed doxycycline → fatality in RMSF comparator (F007) |
| [24113261](https://pubmed.ncbi.nlm.nih.gov/24113261/) | Immunity/vaccine | YbgF adhesin; Th1 protection; anti-YbgF blocks invasion (F010, F011) |
| [25270001](https://pubmed.ncbi.nlm.nih.gov/25270001/) | Immunity/vaccine | OmpB-pulsed DCs protect; taxonomy/synonym (F010, F014) |
| [31360728](https://pubmed.ncbi.nlm.nih.gov/31360728/) | Mechanism | RpsB surface-exposed adhesin (F010) |
| [31907196](https://pubmed.ncbi.nlm.nih.gov/31907196/) | Molecular profiling | Cutaneous immunoprofiling/RNA-seq of SFGR (F013) |
| [17338947](https://pubmed.ncbi.nlm.nih.gov/17338947/) | Prevention | DEET + permethrin personal protection (F011) |
| [40922296](https://pubmed.ncbi.nlm.nih.gov/40922296/) | Risk factors | Agricultural/forestry exposure (F012) |
| [36440590](https://pubmed.ncbi.nlm.nih.gov/36440590/) / [31866968](https://pubmed.ncbi.nlm.nih.gov/31866968/) | Genomics | Complete/comparative *R. heilongjiangensis* genomes (Sec. 4) |

**Note on citation integrity:** Two F010 snippets were flagged as source-attribution mismatches during verification (the YbgF Th1 quote and the RpsB title, associated with PMID 24113261 and PMID 31360728 respectively). The substance of the claims is supported by those papers, but exact quote-to-PMID attribution should be re-verified before database ingestion.

---

## Limitations and Knowledge Gaps

1. **Quantitative epidemiology is weak.** No reliable incidence/prevalence per 100,000 exists; FESF is under-recognized and reported largely as case reports and tick-surveillance studies. True human burden across Northeast Asia is unknown.
2. **FESF-specific clinical frequencies are extrapolated.** Precise symptom frequencies (e.g., % with eschar, % with GI symptoms, % with thrombocytopenia) derive substantially from related SFGR (Japanese/Mediterranean spotted fever, RMSF) rather than large FESF-specific cohorts.
3. **Severe-outcome data borrow from other SFGR.** Complication rates (vasculitis, MODS, HLH) and mortality are illustrated using *R. conorii*/*R. japonica*/*R. rickettsii* cases; FESF-specific severe outcomes are rarely documented.
4. **No host-genetic dimension.** Sections on causal genes, inheritance, penetrance, carrier frequency, genetic testing, and model-organism knockouts are **not applicable**, limiting the report's mapping onto the genetic-disease template.
5. **Mechanistic gaps.** The endothelial-invasion adhesin repertoire and the exact molecular basis of stomach tropism are incompletely defined; much mechanism is inferred from SFGR generally or from mouse models rather than demonstrated in human FESF tissue.
6. **Diagnostics standardization.** No FESF-specific validated serologic cutoffs or point-of-care molecular assays; cross-reactivity within SFGR complicates species-level serodiagnosis.

---

## Proposed Follow-up Experiments / Actions

1. **Assemble a FESF-specific clinical cohort** with standardized data capture (eschar, rash, lymphadenopathy, GI symptoms, thrombocytopenia, transaminases) to derive true phenotype frequencies and replace SFGR-borrowed estimates.
2. **Prospective molecular surveillance** across the endemic belt (Russian Far East → China → Kazakhstan) using mNGS to define human incidence, seasonal dynamics, and range expansion.
3. **Human eschar/skin transcriptomics and spatial profiling** (building on PMID 31907196) to map the endothelial-vasculitis cascade and Th1 program directly in FESF tissue rather than inferring from other SFGR.
4. **Mechanistic dissection of stomach tropism** (F005) — identify receptor/adhesin determinants of organ targeting using the C57BL/6 model with adhesin-knockout bacteria.
5. **Advance OmpB/YbgF subunit vaccine candidates** (F010) through challenge-protection and cross-protection studies against multiple SFGR; assess adjuvant/Th1-skewing formulations.
6. **Develop validated, species-discriminating serologic and rapid molecular assays** to distinguish FESF from co-circulating SFTS, scrub typhus, and other SFGR in primary care.
7. **Re-verify citation attributions** flagged in F010 before knowledge-base ingestion.

---

*Report compiled from 14 confirmed findings and 57 reviewed papers across 5 investigation iterations. Evidence source types span human clinical case reports and cohorts, tick/reservoir surveillance, mouse-model (in vivo) studies, and in vitro endothelial-infection and immunology experiments.*


## Artifacts

- [OpenScientist final report](Far_Eastern_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Far_Eastern_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0200042` (2 mentions) - the report calls it "Inoculation eschar (tache noire)"; HP calls it **Skin ulcer**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001945` (2 mentions) - the report calls it "Fever (~39–40 °C)"; HP calls it **Fever**
- `HP:0000988` (2 mentions) - the report calls it "Maculopapular rash"; HP calls it **Skin rash**, and lists "Rash" among its other names
- `HP:0002716` (2 mentions) - the report calls it "Regional lymphadenopathy"; HP calls it **Lymphadenopathy**
- `HP:0002910` (2 mentions) - the report calls it "Elevated transaminases"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated transaminases" among its other names
- `HP:0011024` (2 mentions) - the report calls it "Gastrointestinal symptoms"; HP calls it **Abnormality of the gastrointestinal tract**, and lists "Gastrointestinal disease" among its other names