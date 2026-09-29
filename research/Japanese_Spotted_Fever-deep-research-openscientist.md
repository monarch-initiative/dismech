---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-27T01:34:02.245294'
end_time: '2026-09-27T01:48:44.622550'
duration_seconds: 882.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Japanese Spotted Fever
  mondo_id: MONDO:0000233
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
citation_count: 34
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 34
  on_topic: 17
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 23
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 3
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0000233
    reported_labels:
    - Mondo
    ontology_label: Japanese spotted fever
  - term_id: HP:0000988
    reported_labels:
    - Systemic erythema / rash
    ontology_label: Skin rash
  - term_id: HP:0000979
    reported_labels:
    - Purpura / palmar-plantar rash
    ontology_label: Purpura
  - term_id: HP:0005521
    reported_labels:
    - DIC
    ontology_label: Disseminated intravascular coagulation
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Japanese_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Japanese_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Japanese Spotted Fever
- **MONDO ID:** MONDO:0000233 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Japanese Spotted Fever** covering all of the
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

# Japanese Spotted Fever (MONDO:0000233): A Comprehensive Disease Characteristics Report

## Summary

**Japanese Spotted Fever (JSF)** is an acute, tick-borne rickettsiosis caused by *Rickettsia japonica*, an obligate intracellular Gram-negative alpha-proteobacterium of the spotted fever group (SFG). First clinically described by Mahara in 1984, JSF is endemic to Japan, where it is now the **second most common acari-borne disease** after scrub typhus (32.9% of 18,295 cases in national surveillance 1999–2025). Its incidence is rising and its geographic range is expanding both eastward and northward across the Japanese archipelago. The disease is a classic **zoonosis**: humans are incidental dead-end hosts infected when bitten by *Haemaphysalis* and related ixodid ticks that maintain the pathogen enzootically with wild boars, deer, and rodents as amplifying blood-meal hosts.

Clinically, JSF presents with a **triad of fever, rash, and inoculation eschar (tache noire)**. The rash characteristically involves the palms and soles and may become petechial/purpuric — a feature that helps distinguish it from scrub typhus. The core pathophysiology is a **disseminated small-vessel vasculitis**: *R. japonica* infects and replicates within vascular endothelial cells, triggering a hypercytokinemic ("cytokine storm") inflammatory response that can escalate to disseminated intravascular coagulation (DIC), purpura fulminans, and multi-organ failure. Because JSF is an **acquired infectious disease, host genetic causation and Mendelian inheritance are Not Applicable**; there are no causal genes, pathogenic variants, or heritable risk loci.

The single most important prognostic lever is **early tetracycline therapy** (minocycline or doxycycline). Overall case-fatality is low (~1%) with prompt treatment but climbs to **14–16% in severe or delayed-treatment cohorts**. Independent risk factors for severe disease are advanced age (≥75 years), male sex, and treatment delay (≥4 days from onset). Adjunctive fluoroquinolones are used for fulminant cases but show **no nationwide mortality benefit** over tetracyclines alone. No vaccine exists; prevention rests entirely on tick-bite avoidance (permethrin-treated clothing, DEET, tick checks).

---

## Key Findings

### 1. Disease Information

Japanese Spotted Fever (synonyms: **Oriental Spotted Fever**) is an acute infectious tick-borne rickettsiosis. Key identifiers:

| Identifier system | Value |
|---|---|
| Mondo | **MONDO:0000233** |
| ICD-10 | **A77.8** (other spotted fevers) / A77.9 |
| NCBI Taxon (pathogen) | **txid35790** (*Rickettsia japonica*) |
| OMIM | Not applicable (acquired infection, not Mendelian) |
| Orphanet | Not a distinct Mendelian rare-disease entry |
| MeSH | Indexed under spotted fever / Rickettsia infections |

Information is derived overwhelmingly from **aggregated disease-level resources** — surveillance cohorts, multicenter case series, and autopsy reports — rather than individual EHR records. The disease was first clinically described in Japan in 1984 (Mahara). *(Finding F010)*

### 2. Etiology

**Primary cause — infectious.** JSF is caused by *Rickettsia japonica*, a spotted fever group rickettsia. In a molecular survey of 4,549 questing ticks (747 pools) in Ibaraki Prefecture, 38.7% of pools were *Rickettsia*-positive, and *R. japonica* was detected **only in *Haemaphysalis hystricis***; nineteen nearby wild boars were heavily infested with this tick, implicating them as key blood-meal hosts/dispersers ([PMID: 42697132](https://pubmed.ncbi.nlm.nih.gov/42697132/)). Other Japanese ticks carrying SFG rickettsiae include *Amblyomma testudinarium*, *Haemaphysalis flava*, and *Ixodes* spp. ([PMID: 41720337](https://pubmed.ncbi.nlm.nih.gov/41720337/), [PMID: 40601071](https://pubmed.ncbi.nlm.nih.gov/40601071/)). *(Finding F001)*

> *"Among these positive samples, R. japonica was detected only in Haemaphysalis hystricis. Nineteen wild boars captured near the tick sampling sites exhibited heavy infestations with H. hystricis, suggesting that wild boars are important blood-meal hosts for this tick species"* — [PMID: 42697132](https://pubmed.ncbi.nlm.nih.gov/42697132/)

**Risk factors.**
- *Genetic:* **None identified.** JSF has no known causal variants, susceptibility loci, or modifier genes — consistent with an acquired infection.
- *Environmental / host:* Advanced age (≥75), male sex, rural/outdoor occupational exposure (farming, forestry, citrus cultivation), and seasonal activity April–October coinciding with tick questing. Treatment delay is the dominant modifiable determinant of severity. *(Findings F003, F011)*

**Protective factors.** No genetic protective alleles are known. Environmental protection is behavioral: avoiding tick bites and, critically, **early empirical tetracycline** on clinical suspicion. Gene–environment interactions are Not Applicable given the absence of a host-genetic component.

### 3. Phenotypes

The hallmark is the **clinical triad**: fever, rash, and eschar. Frequencies from Japanese surveillance cohorts:

| Phenotype (suggested HPO) | Frequency | Source |
|---|---|---|
| Fever (HP:0001945) | 87–100% | [PMID: 35545515](https://pubmed.ncbi.nlm.nih.gov/35545515/), [PMID: 39477520](https://pubmed.ncbi.nlm.nih.gov/39477520/) |
| Systemic erythema / rash (HP:0000988) | 48–100% | Same |
| Eschar / tache noire (HP:0200041 skin ulcer) | 79.4% | [PMID: 39477520](https://pubmed.ncbi.nlm.nih.gov/39477520/) |
| Tick-bite history | 73.6% | [PMID: 35545515](https://pubmed.ncbi.nlm.nih.gov/35545515/) |
| Liver dysfunction (HP:0001410) | ~69% | [PMID: 35545515](https://pubmed.ncbi.nlm.nih.gov/35545515/) |
| Purpura / palmar-plantar rash (HP:0000979) | Characteristic | [PMID: 30124190](https://pubmed.ncbi.nlm.nih.gov/30124190/) |
| DIC (HP:0005521) | 14.3% (overall); ~100% in severe ICU series | [PMID: 35545515](https://pubmed.ncbi.nlm.nih.gov/35545515/), [PMID: 36386421](https://pubmed.ncbi.nlm.nih.gov/36386421/) |
| Neurological symptoms (HP:0000707) | 11.0% | [PMID: 35545515](https://pubmed.ncbi.nlm.nih.gov/35545515/) |
| Hyponatremia (HP:0002902) | Characteristic | [PMID: 30124190](https://pubmed.ncbi.nlm.nih.gov/30124190/) |

> *"Clinical findings more frequently observed in JSF than in ST patients were purpura, palmar/plantar rash, hyponatremia, organ damage, and delayed defervescence after treatment"* — [PMID: 30124190](https://pubmed.ncbi.nlm.nih.gov/30124190/)

**Characteristics:** onset is **acute and adult/geriatric-skewed** (median ages in the 70s in Japanese cohorts); severity ranges from mild self-limited to fulminant; progression is monophasic but can escalate rapidly over days without treatment. Quality-of-life impact in survivors is generally full recovery, though residual hyperpigmentation and prolonged neurocognitive deficits (see MERS below) can occur. *(Findings F002, F011)*

### 4. Genetic / Molecular Information

**Not Applicable for host genetics.** JSF is an acquired bacterial infection with **no causal human genes, no pathogenic germline/somatic variants, no modifier genes, no disease-specific epigenetic signatures, and no chromosomal abnormalities.**

The relevant molecular biology is that of the **pathogen**. The complete genome of *R. japonica* strain YH has been sequenced (~1.28 Mb circular chromosome, low G+C ~37%) and characterized comparatively against other SFG rickettsiae ([PMID: 31866968](https://pubmed.ncbi.nlm.nih.gov/31866968/)). As an obligate intracellular organism, *R. japonica* invades and replicates free in the host endothelial cytosol; virulence involves **actin-based motility** and outer-membrane proteins (**rOmpA/rOmpB, sca family**) shared across SFG rickettsiae. *(Finding F010)*

### 5. Environmental Information

- **Environmental factors:** rural/wooded/agricultural exposure where questing ticks are present; seasonality April–October.
- **Lifestyle factors:** outdoor occupations (farming, forestry) and recreation increase tick contact.
- **Infectious agent:** ***Rickettsia japonica*** (NCBI:txid35790), SFG, family Rickettsiaceae. Transmitted by *Haemaphysalis hystricis*, *H. flava*, *H. longicornis*, *Amblyomma testudinarium*, and *Ixodes* spp. *(Findings F001, F010, F012)*

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Infected tick bite **inoculates** *R. japonica* into the dermis → local endothelial infection **produces** the eschar (tache noire) at the bite site.
2. *R. japonica* **invades** vascular endothelial cells and replicates in the cytosol (actin-based motility) → **causes** cell-to-cell spread and endothelial injury.
3. Endothelial infection **triggers** a local and systemic inflammatory/immune response → **results in** small-vessel **vasculitis** (lymphohistiocytic capillaritis/venulitis progressing to leukocytoclastic vasculitis; inferred from analogous RMSF histology).
4. Vasculitis + endothelial damage **drives** hypercytokinemia (elevated M-CSF, IL-1β, IL-10, IFN-γ, TNF-α) → **causes** the "cytokine storm."
5. Cytokine storm + endothelial injury **increases** vascular permeability and activates coagulation → **leads to** the maculopapular/petechial rash, hyponatremia, and (in severe cases) **DIC**.
6. DIC + microvascular thrombosis/hemorrhage **produce** multi-organ injury — hepatitis, acute renal failure (glomerular microhemorrhage), interstitial pneumonitis, CNS involvement, purpura fulminans → **culminating in** multi-organ failure and, if untreated/delayed, death.

**Branch:** With early tetracycline (step 2 interrupted), rapid defervescence (24–48 h) and full recovery follow. Without it, the chain proceeds to steps 5–6.

Autopsy of fatal JSF confirmed vasculitis with neutrophilic dermal, pulmonary-interstitial, and glomerular infiltrates plus microhemorrhage and multi-organ failure ([PMID: 38043152](https://pubmed.ncbi.nlm.nih.gov/38043152/)). The hypercytokinemia driver is demonstrated by a fulminant shock case in which elevated cytokines fell rapidly after minocycline + methylprednisolone ([PMID: 11376087](https://pubmed.ncbi.nlm.nih.gov/11376087/)). *(Finding F005)*

> *"Elevated levels of cytokines (macrophage colony-stimulating factor, interleukin 1 beta, interleukin 10, and gamma interferon) decreased rapidly after a combination treatment using an antibiotic (minocycline hydrochloride [MINO]) and methylprednisolone"* — [PMID: 11376087](https://pubmed.ncbi.nlm.nih.gov/11376087/)

**Suggested ontology terms:** biological processes — inflammatory response (**GO:0006954**), cytokine production (**GO:0001816**), blood coagulation (**GO:0007596**); cell type — **vascular endothelial cell (CL:0000115)**; chemical entities — TNF-α, IL-1β, IL-10, IFN-γ (CHEBI cytokine class).

### 7. Anatomical Structures Affected

JSF is a **systemic small-vessel disease** with multi-organ involvement:

| Level | Structures (suggested UBERON/CL) |
|---|---|
| Skin (primary) | Rash, eschar, purpura, palmar/plantar involvement; **skin (UBERON:0002097)**; purpura fulminans → gangrene/amputation in ~33% of critical cases |
| Liver | Dysfunction ~69% (**UBERON:0002107**) |
| Kidney | Acute renal failure, glomerular microhemorrhage (**UBERON:0002113**) |
| Lung | Interstitial pneumonitis, pleural effusion (91% in severe series) (**UBERON:0002048**) |
| CNS | Meningitis/encephalitis, altered consciousness; reversible splenial lesion (**UBERON:0000955**) |
| Blood/hematologic | Thrombocytopenia, leukopenia, DIC (**UBERON:0000178**) |
| Vasculature (core target) | Small-vessel endothelium; **blood vessel (UBERON:0001981)**, **endothelial cell (CL:0000115)** |

Involvement is generally **bilateral/systemic** rather than lateralized. In SFG rickettsioses broadly, CNS disease features microglial expansion and macrophage infiltration with perivascular T-cell infiltration ([PMID: 33091013](https://pubmed.ncbi.nlm.nih.gov/33091013/)). *(Findings F005, F009)*

> *"33.3% of whom developed purpura fulminans requiring amputation or skin graft, and 16.6% died two days after admission"* — [PMID: 36386421](https://pubmed.ncbi.nlm.nih.gov/36386421/)

### 8. Temporal Development

- **Onset:** acute, typically **2–8 days after tick bite** (incubation ~2–8 days); patients often note symptoms 1–2 days after the bite in some series ([PMID: 36386421](https://pubmed.ncbi.nlm.nih.gov/36386421/)).
- **Age:** adult/geriatric-skewed (medians in the 70s).
- **Course:** acute and **monophasic**. With early tetracycline, defervescence occurs within 24–48 h and recovery is usually complete. Without prompt treatment, the disease can progress to DIC and multi-organ failure within days; fatal cases may die ~2–3 days after admission ([PMID: 18411764](https://pubmed.ncbi.nlm.nih.gov/18411764/)).
- **Seasonality:** April–October, coinciding with tick activity ([PMID: 30124190](https://pubmed.ncbi.nlm.nih.gov/30124190/)).
- **Sequelae:** residual hyperpigmentation; prolonged neurocognitive deficits in MERS-type encephalopathy ([PMID: 35945027](https://pubmed.ncbi.nlm.nih.gov/35945027/)).

**Critical intervention window:** the first ~3–4 days from onset — beyond this, severity risk rises sharply. *(Finding F011)*

### 9. Inheritance and Population

**Inheritance: Not Applicable** (acquired infection — no inheritance pattern, penetrance, expressivity, anticipation, founder effects, consanguinity, or carrier frequency).

**Epidemiology.** JSF is the **second most common acari-borne disease in Japan**. National surveillance 1999–2025 recorded 18,295 acari-borne cases; JSF accounted for **32.9%** (scrub typhus 56.6%, SFTS 6.7%) ([PMID: 42518741](https://pubmed.ncbi.nlm.nih.gov/42518741/)). Incidence is rising: in Shimane Prefecture (2000–2022, 301 cases), a gradual significant increase (prevalence rate ratio 1.03/yr, 95% CI 1.01–1.05) was followed by rapid acceleration since 2020 (1.57, 95% CI 1.39–1.78) ([PMID: 38574815](https://pubmed.ncbi.nlm.nih.gov/38574815/)). The endemic zone, historically western Japan, is expanding eastward (Ibaraki now endemic) and into northern Japan. *(Finding F004)*

> *"scrub typhus (56.6%), Japanese spotted fever (32.9%) and severe fever with thrombocytopenia syndrome (6.7%) together accounted for more than 95% of all cases"* — [PMID: 42518741](https://pubmed.ncbi.nlm.nih.gov/42518741/)

**Demographics.** Predominantly older adults; male sex is over-represented among severe cases. Geographic distribution centers on Japan, with related *R. japonica*/near-relative detections reported in China and Southeast Asia. *(Findings F003, F004)*

### 10. Diagnostics

Diagnosis combines **clinical triad recognition** with laboratory confirmation:

| Modality | Detail | Source |
|---|---|---|
| PCR (17-kDa antigen gene) | Eschar and blood samples; confirms *R. japonica* | [PMID: 38043152](https://pubmed.ncbi.nlm.nih.gov/38043152/), [PMID: 41720337](https://pubmed.ncbi.nlm.nih.gov/41720337/) |
| Indirect immunofluorescence (IFA) | Paired sera ≥4-fold IgG rise = serological reference; negative early | [PMID: 31587667](https://pubmed.ncbi.nlm.nih.gov/31587667/) |
| qPCR + IFA in tandem | Recommended combined strategy | [PMID: 31587667](https://pubmed.ncbi.nlm.nih.gov/31587667/) |
| Metagenomic NGS (mNGS) | Diagnoses atypical/eschar-negative and non-endemic cases | [PMID: 40922296](https://pubmed.ncbi.nlm.nih.gov/40922296/), [PMID: 40082238](https://pubmed.ncbi.nlm.nih.gov/40082238/), [PMID: 39383151](https://pubmed.ncbi.nlm.nih.gov/39383151/) |
| Weil-Felix | Insensitive/nonspecific; often negative — not recommended | [PMID: 39383151](https://pubmed.ncbi.nlm.nih.gov/39383151/) |

**Common laboratory abnormalities:** elevated transaminases/liver dysfunction (~69%), thrombocytopenia, leukopenia/neutropenia, hyponatremia, elevated CRP. *(Finding F007)*

> *"Metagenomic sequencing (MetaCAP) technology enabled a definitive diagnosis by identifying Rickettsia japonica-specific DNA sequences in the patient's blood"* — [PMID: 40922296](https://pubmed.ncbi.nlm.nih.gov/40922296/)

**Differential diagnosis** is critical because treatment differs. A five-hospital Nagasaki study (23 SFTS, 38 JSF) found **leukopenia (WBC <4000/µL) and altered mental status** best separated SFTS from JSF (AUC 1.000, 100% sensitivity/specificity); JSF characteristically has rash, preserved consciousness, and higher WBC/CRP ([PMID: 36016429](https://pubmed.ncbi.nlm.nih.gov/36016429/)). JSF differs from scrub typhus by seasonality, palmar/plantar rash, purpura, and delayed defervescence ([PMID: 30124190](https://pubmed.ncbi.nlm.nih.gov/30124190/)). Rare mimics include SLE ([PMID: 41731438](https://pubmed.ncbi.nlm.nih.gov/41731438/)) and SFTSV co-infection ([PMID: 34407756](https://pubmed.ncbi.nlm.nih.gov/34407756/)). *(Finding F014)*

> *"Decision tree analysis revealed leukopenia (white blood cell [WBC] < 4000/μL) and altered mental status as the best differentiating factors (AUC 1.000) with 100% sensitivity and 100% specificity"* — [PMID: 36016429](https://pubmed.ncbi.nlm.nih.gov/36016429/)

**Genetic testing / omics screening / newborn screening:** Not Applicable (no host-genetic component).

### 11. Outcome / Prognosis

Overall case-fatality is **low with early treatment** but rises steeply with severity:

| Cohort | Severe outcome | Mortality | Source |
|---|---|---|---|
| Ehime surveillance (n=91) | — | **1.1%** | [PMID: 35545515](https://pubmed.ncbi.nlm.nih.gov/35545515/) |
| Nagasaki multicenter (n=65) | 33.3% | ~1.5% (1/65) | [PMID: 39477520](https://pubmed.ncbi.nlm.nih.gov/39477520/) |
| Eastern Hiroshima (n=42) | 31.0% | **14.3%** | [PMID: 42576956](https://pubmed.ncbi.nlm.nih.gov/42576956/) |
| Yichang, China ICU series | 100% DIC | **16.6%** | [PMID: 36386421](https://pubmed.ncbi.nlm.nih.gov/36386421/) |

**Prognostic factors:** age ≥75, male sex, treatment delay ≥4 days, DIC, altered mental status, hypotension, hypoxia. A nationwide Diagnosis Procedure Combination inpatient study (n=1,060, 2010–2021) found that **adding a fluoroquinolone to tetracycline on admission produced no significant difference** in in-hospital mortality, complications, cost, or length of stay after inverse-probability weighting ([PMID: 35987471](https://pubmed.ncbi.nlm.nih.gov/35987471/)). *(Findings F003, F013)*

> *"Inverse probability of treatment weighting showed no statistically significant differences between the groups in in-hospital mortality... This study did not show any significantly improved effectiveness using FQ antimicrobials in combination with TCs for treating JSF"* — [PMID: 35987471](https://pubmed.ncbi.nlm.nih.gov/35987471/)

Recovery potential is excellent with prompt treatment; complications (DIC, purpura fulminans → amputation, renal failure, MERS-type encephalopathy) drive morbidity in the severe minority.

### 12. Treatment

**First-line: tetracyclines** (minocycline or doxycycline) — NCIT clinical-intervention terms: Minocycline (NCIT:C61829), Doxycycline (NCIT:C513), Tetracycline (NCIT:C859). Fever typically resolves rapidly (e.g., within 36 h) after IV minocycline + levofloxacin ([PMID: 26630793](https://pubmed.ncbi.nlm.nih.gov/26630793/)); doxycycline achieves rapid resolution in typical cases ([PMID: 40922296](https://pubmed.ncbi.nlm.nih.gov/40922296/)).

**Severe/fulminant disease:**
- **Tetracycline + new quinolone** (ciprofloxacin, tosufloxacin, levofloxacin) is recommended for fulminant JSF where minocycline alone is insufficient ([PMID: 26630793](https://pubmed.ncbi.nlm.nih.gov/26630793/), [PMID: 11376087](https://pubmed.ncbi.nlm.nih.gov/11376087/)). Note the nationwide caveat that adjunctive fluoroquinolone shows no mortality benefit ([PMID: 35987471](https://pubmed.ncbi.nlm.nih.gov/35987471/)).
- **Corticosteroids** (methylprednisolone) suppress the cytokine storm in severe cases ([PMID: 39328670](https://pubmed.ncbi.nlm.nih.gov/39328670/), [PMID: 11376087](https://pubmed.ncbi.nlm.nih.gov/11376087/)).
- **Supportive care** for DIC/multi-organ failure (hemodialysis, mechanical ventilation, anticoagulation management).

> *"In the treatment of fulminant JSF (body temperature > 39 degrees C) the prompt administration of a combination of tetracycline and new quinolone has been recommended"* — [PMID: 26630793](https://pubmed.ncbi.nlm.nih.gov/26630793/)

**Mechanistic rationale for combination:** in vitro, minocycline + ciprofloxacin synergistically inhibit TNF-α and chemokine production in LPS-stimulated THP-1 monocytes — an anti-inflammatory effect beyond antimicrobial action ([PMID: 41341009](https://pubmed.ncbi.nlm.nih.gov/41341009/)).

> *"Combination therapy with MINO and CPFX enhanced the inhibitory effects on inflammatory cytokine and chemokine production"* — [PMID: 41341009](https://pubmed.ncbi.nlm.nih.gov/41341009/)

**Pharmacogenomics, gene/cell/RNA/targeted/immuno-therapies:** Not Applicable. *(Findings F006, F013)*

### 13. Prevention

- **Primary prevention (behavioral):** avoid tick bites — permethrin-treated clothing, DEET and other repellents, protective clothing, and prompt tick checks/removal. Against the vector *Haemaphysalis longicornis*, formulated repellents gave **93–97% repellency** and permethrin-treated garments dislodged **96% of nymphs within 3 min** ([PMID: 32073128](https://pubmed.ncbi.nlm.nih.gov/32073128/)). General tick-borne disease prevention endorses DEET/permethrin and prompt tick removal ([PMID: 38478946](https://pubmed.ncbi.nlm.nih.gov/38478946/)).
- **Secondary prevention:** early empirical tetracycline on clinical suspicion is the key measure — the disease's decisive intervention. Doxycycline **prophylaxis is not standard** for JSF ([PMID: 25527099](https://pubmed.ncbi.nlm.nih.gov/25527099/)), though prophylactic antibiotics after tick bite are commonly prescribed in Japanese practice (88.6% in one cohort); *R. tamurae*-positive bites remained asymptomatic without antibiotics ([PMID: 41720337](https://pubmed.ncbi.nlm.nih.gov/41720337/)).
- **Immunization: No vaccine exists.**
- **Genetic screening/counseling:** Not Applicable. *(Finding F008)*

> *"all tested product formulations were highly effective with estimated repellencies ranging from 93 to 97%... 96% of introduced ticks dislodging"* — [PMID: 32073128](https://pubmed.ncbi.nlm.nih.gov/32073128/)

### 14. Other Species / Natural Disease

JSF is maintained in an **enzootic tick–mammal cycle**; humans are incidental dead-end hosts. Ticks (*Haemaphysalis hystricis*, *H. flava*, *H. longicornis*, *Amblyomma testudinarium*, *Ixodes* spp.) serve as both vectors and reservoirs (transovarial maintenance is typical of SFG rickettsiae); **wild boars (*Sus scrofa*, NCBI:txid9823)** and rodents act as amplifying/blood-meal hosts ([PMID: 42697132](https://pubmed.ncbi.nlm.nih.gov/42697132/), [PMID: 40601071](https://pubmed.ncbi.nlm.nih.gov/40601071/)). No naturally occurring clinical JSF disease is well documented in companion animals, though dogs seroconvert to SFG rickettsiae and can serve as sentinels ([PMID: 28569177](https://pubmed.ncbi.nlm.nih.gov/28569177/)). **Zoonotic potential is central** to the disease's ecology. *(Findings F001, F012)*

> *"wild boars are important blood-meal hosts for this tick species"* — [PMID: 42697132](https://pubmed.ncbi.nlm.nih.gov/42697132/)

### 15. Model Organisms

There is no dedicated genetic disease model (the disease is infectious, not Mendelian). Mechanistic understanding derives from:
- **In vitro:** *R. japonica* is propagated in **Vero cells** and related cell lines, as for other SFG rickettsiae ([PMID: 30529423](https://pubmed.ncbi.nlm.nih.gov/30529423/)); THP-1 monocytic cells are used for cytokine/anti-inflammatory drug studies ([PMID: 41341009](https://pubmed.ncbi.nlm.nih.gov/41341009/)).
- **Murine models of related rickettsioses** (scrub typhus/SFR) reveal cerebral T-cell infiltration, endothelial infection, and vascular damage underlying neuropathogenesis ([PMID: 33091013](https://pubmed.ncbi.nlm.nih.gov/33091013/)).

**Model limitations:** most mechanistic inference is extrapolated from related rickettsioses (RMSF, scrub typhus) rather than *R. japonica*-specific in vivo models. *(Finding F012)*

> *"Animal models of scrub typhus have identified cerebral T-cell infiltration and vascular damage associated with endothelial infection and neuropathogenesis"* — [PMID: 33091013](https://pubmed.ncbi.nlm.nih.gov/33091013/)

---

## Mechanistic Model / Interpretation

```
   Infected Haemaphysalis tick bite
              │ inoculates R. japonica
              ▼
   Local endothelial infection ──────────► ESCHAR (tache noire)
              │ invades & replicates (actin-based motility)
              ▼
   Systemic endothelial infection
              │ triggers immune/inflammatory response
              ▼
   SMALL-VESSEL VASCULITIS ◄──── perivascular T-cell / neutrophil infiltrate
              │ drives
              ▼
   HYPERCYTOKINEMIA (M-CSF, IL-1β, IL-10, IFN-γ, TNF-α)
              │ ↑ vascular permeability + coagulation activation
      ┌───────┴─────────────────────────────┐
      ▼                                       ▼
   RASH (palms/soles,          DISSEMINATED INTRAVASCULAR
   petechiae, purpura),        COAGULATION (DIC)
   hyponatremia                        │
                                       ▼
                       MULTI-ORGAN FAILURE
             (liver, kidney, lung, CNS, skin/purpura fulminans)
                                       │
                                       ▼
                                    DEATH  (if untreated / delayed)

   ┌──────────────────────────────────────────────────────┐
   │ INTERVENTION: Early tetracycline halts step 2 →        │
   │ rapid defervescence (24–48h) → full recovery.          │
   │ Delay ≥4 d, age ≥75, male sex → severe branch.         │
   └──────────────────────────────────────────────────────┘
```

The unifying theme is **endothelium-centric vasculitis amplified by cytokine storm**. Upstream events (endothelial infection, vasculitis) are demonstrated by autopsy and cytokine kinetics; downstream events (DIC, multi-organ failure) are the clinical endpoints. The therapeutic model is elegantly simple: because the entire cascade depends on ongoing intracellular bacterial replication, an antibiotic that penetrates cells (tetracycline) and is given **early** can abort the whole chain — which is exactly why treatment timing dominates prognosis.

---

## Evidence Base

| PMID | Contribution |
|---|---|
| [42697132](https://pubmed.ncbi.nlm.nih.gov/42697132/) | Identifies *H. hystricis* as vector and wild boar as blood-meal host; documents eastward endemic expansion |
| [30124190](https://pubmed.ncbi.nlm.nih.gov/30124190/) | Distinguishing features vs scrub typhus (palmar/plantar rash, purpura, hyponatremia, seasonality) |
| [35545515](https://pubmed.ncbi.nlm.nih.gov/35545515/) | Phenotype frequencies and 1.1% mortality (n=91) |
| [39477520](https://pubmed.ncbi.nlm.nih.gov/39477520/) | Severe-disease risk factors: age ≥75, male sex, treatment delay ≥4 d |
| [42576956](https://pubmed.ncbi.nlm.nih.gov/42576956/) | Dose-response of minocycline delay; 14.3% mortality in endemic cohort |
| [42518741](https://pubmed.ncbi.nlm.nih.gov/42518741/) | National surveillance — JSF = 32.9% of acari-borne disease |
| [38574815](https://pubmed.ncbi.nlm.nih.gov/38574815/) | Rising incidence, acceleration since 2020 |
| [38043152](https://pubmed.ncbi.nlm.nih.gov/38043152/) | Autopsy evidence of vasculitis and multi-organ microvascular injury |
| [11376087](https://pubmed.ncbi.nlm.nih.gov/11376087/) | Hypercytokinemia as driver of fulminant shock; steroid response |
| [26630793](https://pubmed.ncbi.nlm.nih.gov/26630793/) | Tetracycline + new quinolone for fulminant JSF |
| [41341009](https://pubmed.ncbi.nlm.nih.gov/41341009/) | Anti-cytokine synergy of minocycline + ciprofloxacin (in vitro) |
| [31587667](https://pubmed.ncbi.nlm.nih.gov/31587667/) | qPCR + IFA tandem diagnostic strategy |
| [40922296](https://pubmed.ncbi.nlm.nih.gov/40922296/) | mNGS diagnosing atypical, eschar-negative JSF |
| [32073128](https://pubmed.ncbi.nlm.nih.gov/32073128/) | Efficacy of repellents/permethrin against vector tick |
| [36386421](https://pubmed.ncbi.nlm.nih.gov/36386421/) | Purpura fulminans, 100% DIC, 16.6% mortality in ICU series |
| [33091013](https://pubmed.ncbi.nlm.nih.gov/33091013/) | Cellular basis of CNS involvement in SFG rickettsioses |
| [35987471](https://pubmed.ncbi.nlm.nih.gov/35987471/) | Nationwide DB: adjunctive fluoroquinolone gives no mortality benefit |
| [36016429](https://pubmed.ncbi.nlm.nih.gov/36016429/) | Objective criteria differentiating JSF from SFTS |
| [31866968](https://pubmed.ncbi.nlm.nih.gov/31866968/) | Genomic characterization of *R. japonica* |

**Corroborating comparative literature** (RMSF/Mediterranean spotted fever) supports the vasculitis mechanism ([PMID: 9449487](https://pubmed.ncbi.nlm.nih.gov/9449487/)) and the caution that fluoroquinolones may worsen SFG rickettsiosis outcomes ([PMID: 21642652](https://pubmed.ncbi.nlm.nih.gov/21642652/)), reinforcing the tetracycline-first strategy.

---

## Limitations and Knowledge Gaps

1. **Extrapolated mechanism.** Much of the detailed cellular/immune pathogenesis (CNS T-cell infiltration, endothelial neuropathogenesis) is inferred from murine models of *related* rickettsioses (scrub typhus, RMSF), not *R. japonica*-specific in vivo experiments.
2. **No host-genetic dimension.** Sections on genetics, inheritance, genetic testing, gene/cell therapy, and genetic counseling are Not Applicable — a complete and expected gap for an acquired infection, not a research deficiency.
3. **Geographic bias.** Nearly all clinical cohorts are Japanese (plus a Chinese ICU series); prognostic estimates and risk-factor odds ratios may not generalize to the expanding/emerging range.
4. **Small severe-cohort sizes.** Severe-disease mortality (14–16%) derives from modest single-center/ICU cohorts with wide confidence intervals.
5. **Corticosteroid evidence is weak.** Steroid use rests on case reports and mechanistic plausibility, not randomized trials.
6. **Serology timing.** IFA is insensitive early, and Weil-Felix is unreliable — creating a diagnostic window where clinical suspicion alone must drive treatment.

---

## Proposed Follow-up Experiments / Actions

1. **Develop an *R. japonica*-specific animal model** (immunocompetent and aged/comorbid mice) to test whether age-related endothelial/immune changes explain the geriatric severity skew.
2. **Prospective multicenter RCT** of adjunctive corticosteroids in severe JSF with DIC, given the strong mechanistic rationale but weak clinical evidence.
3. **Biomarker study** correlating admission cytokine profiles (M-CSF, IL-1β, IL-10, IFN-γ, TNF-α) and coagulation markers with progression to DIC, to build a validated severity-prediction score.
4. **Deploy point-of-care mNGS/qPCR** in expanding endemic areas (eastern/northern Japan) to close the early-diagnosis window and quantify true incidence.
5. **One Health surveillance** integrating tick, wild-boar, deer, and rodent sampling across the expanding range to map emerging endemic foci and inform targeted vector control.
6. **Formal cost-effectiveness analysis** of empirical early tetracycline vs confirmatory-test-then-treat strategies, given that treatment delay is the dominant modifiable driver of mortality.

---

*Report prepared from a 5-iteration autonomous investigation: 14 confirmed findings, 61 papers reviewed. Evidence source types span human clinical cohorts, autopsy pathology, in vitro pharmacology, and comparative model-organism studies of related rickettsioses.*


## Artifacts

- [OpenScientist final report](Japanese_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Japanese_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 34 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0000233` (2 mentions) - the report calls it "Mondo"; MONDO calls it **Japanese spotted fever**
- `HP:0000988` (1 mention) - the report calls it "Systemic erythema / rash"; HP calls it **Skin rash**
- `HP:0000979` (1 mention) - the report calls it "Purpura / palmar-plantar rash"; HP calls it **Purpura**
- `HP:0005521` (1 mention) - the report calls it "DIC"; HP calls it **Disseminated intravascular coagulation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000707` (1 mention) - the report calls it "Neurological symptoms"; HP calls it **Abnormality of the nervous system**, and lists "Neurological abnormality" among its other names