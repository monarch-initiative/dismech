---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-27T22:12:55.797999'
end_time: '2026-09-27T22:27:43.498890'
duration_seconds: 887.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Flinders Island Spotted Fever
  mondo_id: MONDO:0000232
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
citation_count: 18
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 14
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0000232
    reported_labels:
    - MONDO ID
    ontology_label: Flinders island spotted fever
  obsolete_terms:
  - term_id: GO:0006928
    ontology_label: obsolete movement of cell or subcellular component
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Flinders_Island_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Flinders_Island_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Flinders Island Spotted Fever
- **MONDO ID:** MONDO:0000232 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Flinders Island Spotted Fever** covering all of the
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

# Flinders Island Spotted Fever (MONDO:0000232): Comprehensive Disease Characterization Report

*A tick-borne spotted fever group rickettsiosis of south-east Australia caused by* Rickettsia honei

---

## Summary

**Flinders Island Spotted Fever (FISF)** is a rare, acute, self-limited, tick-borne infectious disease caused by the obligate intracellular Gram-negative bacterium ***Rickettsia honei*** (spotted fever group, SFG). It is **not a genetic disease** — there are no human causal genes, no inheritance pattern, and no pathogenic germline variants. It is an **infectious/zoonotic rickettsiosis**, and every section of the standard disease-characteristics template must be read through that lens: the "genetic/molecular" and "inheritance" sections properly describe the *pathogen's* biology and ecology rather than host heritability.

FISF was first defined clinically by Stewart in 1991 as a spotted-fever-like illness affecting a small Bass Strait island community (~1000 people), with 26 cases identified over a 17-year period. The causal organism was isolated from a febrile patient's blood in 1991/1993 and formally described as the new species *Rickettsia honei* strain RB(T) in 1998. The bacterium is maintained transovarially (vertically) in reptile-associated ticks — chiefly *Bothriocroton* (formerly *Aponomma*) *hydrosauri* — whose vertebrate hosts are reptiles (blue-tongued lizards, tiger and copperhead snakes) rather than mammals, an ecologically unusual feature. Humans are incidental hosts infected by tick bite.

Clinically, FISF presents as an acute febrile illness with headache, maculopapular/petechial rash, arthralgia/myalgia, and frequently an inoculation eschar. Pathophysiologically, *R. honei* infects the **vascular endothelium**, using surface cell antigen autotransporters (Sca2, OmpB) to adhere and invade, actin-based motility (RickA/Arp2/3 early phase; Sca2/formin-mimic late phase) to spread cell-to-cell, and triggering NF-κB– and p38-MAPK–driven chemokine release (IL-8, MCP-1) that recruits leukocytes and produces **rickettsial vasculitis**. The disease responds rapidly to **doxycycline** and is generally self-limited with prompt treatment. Prevention rests on tick-bite avoidance; there is no vaccine.

---

## Disease Identity and Classification

| Attribute | Value |
|---|---|
| **Disease name** | Flinders Island Spotted Fever (FISF) |
| **MONDO ID** | MONDO:0000232 |
| **Category** | Infectious disease (zoonotic, tick-borne rickettsiosis) |
| **Causal organism** | *Rickettsia honei* strain RB(T) (= Thai tick typhus strain TT-118) |
| **Pathogen taxonomy** | Bacteria; Proteobacteria; Alphaproteobacteria; Rickettsiales; Rickettsiaceae; *Rickettsia*; spotted fever group |
| **Genome size** | ~1.27 Mb |
| **Synonyms** | Flinders Island spotted fever rickettsiosis; Australian tick typhus (Bass Strait focus); "marmionii" strain rickettsiosis (eastern Australian variant) |
| **Vector / reservoir** | *Bothriocroton (Aponomma) hydrosauri* reptile tick |
| **Vertebrate hosts** | Reptiles (lizards, snakes); humans are incidental |
| **Geography** | South-east Australia (Flinders Island, Tasmania, South Australia, Queensland/Torres Strait, Western Australia); related strain in Thailand and Texas |
| **Data source type** | Aggregated disease-level resources (case series, serosurveys, vector surveillance) — not EHR/individual-patient omics |

FISF is best understood as one of **Australia's four recognised rickettsioses**: murine typhus (*R. typhi*), Queensland tick typhus (*R. australis*), Flinders Island spotted fever (*R. honei*), and scrub typhus (*Orientia tsutsugamushi*) ([PMID: 17553271](https://pubmed.ncbi.nlm.nih.gov/17553271/)).

---

## Key Findings

### Finding 1 — The causal agent is *Rickettsia honei*, a distinct spotted fever group species (F001)

FISF is caused by *Rickettsia honei*, a genetically distinct member of the spotted fever group. Strain RB(T) was isolated from a febrile patient on Flinders Island in 1991/1993 and formally described as a new species in 1998. Phylogenetic comparison of the *16S rRNA*, *rompA* (*ompA*), *gltA* (citrate synthase) and *17-kDa antigen* genes confirmed its distinctness from other SFG rickettsiae; its genome is ~1.27 Mb. Its closest genetic relative is Thai tick typhus strain **TT-118**, now regarded as a strain of *R. honei*, establishing an intercontinental species identity.

> *"The name Rickettsia honei, strain RBT, has been proposed for a unique spotted fever group (SFG) agent which is pathogenic for humans."* — [PMID: 9828442](https://pubmed.ncbi.nlm.nih.gov/9828442/)

> *"Rickettsia honei strain RB(T) was isolated from a febrile patient on Flinders Island, Australia, in 1991 and has been demonstrated to be the agent of Flinders Island spotted fever, a disease transmitted to humans by ticks."* — [PMID: 22815457](https://pubmed.ncbi.nlm.nih.gov/22815457/)

This finding anchors **Sections 1 (Disease Information), 2 (Etiology), and 5 (Infectious Agents)** of the template. The primary cause is infectious; there is no genetic host etiology.

### Finding 2 — Reptile-tick reservoir with transovarial maintenance (F002)

*R. honei* is maintained in nature within the reptile-associated tick *Aponomma (Bothriocroton) hydrosauri*, which is the arthropod reservoir on Flinders Island. In a survey, **29 of 46 (63%) ticks** were PCR-positive for SFG rickettsiae, with sequences 100% homologous to *R. honei*. Electron microscopy localised rickettsiae in tick salivary glands, malpighian tubules, and midgut epithelium, and — critically — within **oocytes and immature eggs**, indicating **transovarial (vertical) transmission**. The vertebrate hosts are reptiles (blue-tongued lizards, tiger and copperhead snakes) rather than mammals, an ecologically unusual arrangement.

> *"The tick Aponomma hydrosauri is associated with reptiles and is the arthropod reservoir for this rickettsia on Flinders Island. The rickettsia appears to be maintained in the tick via vertical transmission. Of 46 ticks examined, 29 (63%) were positive for spotted fever group rickettsiae"* — [PMID: 14628950](https://pubmed.ncbi.nlm.nih.gov/14628950/)

> *"The ecology of R. honei in this location is unusual in that reptiles, rather than mammals, are the vertebrate hosts."* — [PMID: 12860601](https://pubmed.ncbi.nlm.nih.gov/12860601/)

This underpins **Sections 9 (population/reservoir ecology), 13 (Prevention — vector control), and 14 (Other Species / zoonotic transmission)**. Transovarial maintenance means the tick is both vector and reservoir, so the pathogen persists independent of amplifying mammalian hosts.

### Finding 3 — Clinical phenotype: acute febrile illness with rash, arthralgia/myalgia, and eschar (F003)

Across a case series of the eastern-Australian "marmionii" strain (n = 7), the symptom frequencies were: **fever 100%, headache 71%, arthralgia 43%, myalgia 43%, cough 43%, maculopapular/petechial rash 43%, nausea 29%, pharyngitis 29%, lymphadenopathy 29%, and eschar 29%**. Onset is acute, most cases occur in autumn, and cases cluster in eastern Australia (Queensland, Tasmania, South Australia). A severe imported case in Nepal displayed clinical features typical of FISF, confirming the phenotype outside Australia.

> *"symptoms of fever (100%), headache (71%), arthralgia (43%), myalgia (43%), cough (43%), maculopapular/petechial rash (43%), nausea (29%), pharyngitis (29%), lymphadenopathy (29%), and eschar (29%)"* — [PMID: 17553271](https://pubmed.ncbi.nlm.nih.gov/17553271/)

> *"The patient had severe illness and many clinical features typical of Flinders Island spotted fever."* — [PMID: 22000356](https://pubmed.ncbi.nlm.nih.gov/22000356/)

**Suggested HPO terms:** Fever (HP:0001945); Headache (HP:0002315); Skin rash (HP:0000988) / Maculopapular exanthema; Arthralgia (HP:0002829); Myalgia (HP:0003326); Cough (HP:0012735); Nausea (HP:0002018); Pharyngitis (HP:0025439); Lymphadenopathy (HP:0002716); Skin ulcer / eschar (HP:0200042). This supports **Section 3 (Phenotypes)**.

### Finding 4 — Pathophysiology: endothelial tropism causing rickettsial vasculitis (F004)

Pathogenic *Rickettsia* are Gram-negative obligate intracellular bacteria with an affinity for the endothelium lining blood vessels. Infection causes vascular inflammation, insult to vascular integrity, and increased vascular permeability — collectively termed **"rickettsial vasculitis."** SFG rickettsiae activate host-cell transcriptional signalling upon adhesion and invasion. Related SFG rickettsioses (e.g., Mediterranean spotted fever) show **leucocytoclastic vasculitis** on skin biopsy and can involve multiple organs, providing histologic correlates for the FISF mechanism.

> *"a majority of sequelae associated with human rickettsioses are the outcome of the pathogen's affinity for endothelium lining the blood vessels, the consequences of which are vascular inflammation, insult to vascular integrity and compromised vascular permeability, collectively termed 'Rickettsial vasculitis'"* — [PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)

> *"Skin biopsy of the purpura confirmed leucocytoclastic vasculitis"* — [PMID: 33622746](https://pubmed.ncbi.nlm.nih.gov/33622746/)

This establishes the core of **Section 6 (Mechanism) and Section 7 (Anatomical Structures — vascular endothelium)**.

### Finding 5 — Geographic distribution across three continents (F005)

*R. honei* (= strain TT-118) has been detected on three continents: **Thailand** (isolated 1962, confirmed 2001; *Ixodes*/*Rhipicephalus*, including *I. granulatus* from *Rattus rattus*), **Australia** (Flinders Island 1993; also Tasmania, South Australia, Queensland/Torres Strait, and Western Australia), and **Texas, USA** (1998, *Amblyomma cajennense*). Within Australia, FISF extends across south-east Australia, matching the range of its reptile-tick vector; a human case reached Nepal in 2009.

> *"Rickettsia honei (also known as strain TT-118) has been detected on three continents. Originally isolated in Thailand in 1962 (and confirmed in 2001), it has also been detected on Flinders Island (Australia) in 1993 and in Texas (USA) in 1998."* — [PMID: 12860601](https://pubmed.ncbi.nlm.nih.gov/12860601/)

> *"These cases show that FISF extends beyond Flinders Island and most likely has the same distribution across south-east Australia as its vector, the reptile tick Aponomma hydrosauri."* — [PMID: 16175900](https://pubmed.ncbi.nlm.nih.gov/16175900/)

This informs **Section 9 (geographic distribution)**.

### Finding 6 — Co-circulation with other rickettsioses; serologic cross-reactivity complicates diagnosis (F006)

On Darnley Island (Torres Strait), FISF (*R. honei* "marmionii") was found alongside Queensland tick typhus (*R. australis*) and scrub typhus (a unique *Orientia tsutsugamushi* strain), demonstrating overlapping endemic ranges and a broad differential diagnosis. Serosurveys rely on indirect immunofluorescence assay (IFA) panels that **cross-react across SFG antigens** (*R. honei, R. conorii, R. sibirica, R. rickettsii, R. australis, R. akari*), so **species-level confirmation requires PCR/sequencing** (e.g., eschar swab or biopsy PCR).

> *"In addition to previously described cases of Flinders Island spotted fever (Rickettsia honei strain 'marmionii'), we describe 1 case of Queensland tick typhus (R. australis) and 2 cases of scrub typhus caused by a unique strain (Orientia tsutsugamushi)."* — [PMID: 18214193](https://pubmed.ncbi.nlm.nih.gov/18214193/)

> *"Australia has 4 rickettsial diseases: murine typhus, Queensland tick typhus, Flinders Island spotted fever, and scrub typhus."* — [PMID: 17553271](https://pubmed.ncbi.nlm.nih.gov/17553271/)

This is central to **Section 10 (Diagnostics — differential diagnosis and serology/PCR)**.

### Finding 7 — Emerging/expanding geography and multi-species tick carriage (F007)

The first reported case of SFG rickettsiosis in **Western Australia** included *R. honei* among identified agents, expanding the known Australian range beyond the south-east. Ongoing molecular surveillance of reptile ticks continues to detect *Rickettsia* spp. (e.g., in *Bothriocroton hydrosauri* and *Amblyomma moreliae* from reptiles in NSW/SA), refining vector/reservoir maps. Importantly, **not all *B. hydrosauri*-borne *Rickettsia* are *R. honei*** — multiple SFG species can share the same vector, complicating vector-based risk mapping.

> *"We describe the first reported case of spotted fever group rickettsiosis in Western Australia"* — [PMID: 30270856](https://pubmed.ncbi.nlm.nih.gov/30270856/)

> *"although we discovered Rickettsia in all tick samples, it was not Rickettsia honei"* — [PMID: 27338482](https://pubmed.ncbi.nlm.nih.gov/27338482/)

This informs **Sections 9 and 13 (surveillance, emerging foci)**.

### Finding 8 — Molecular mechanism: Sca2/OmpB invasion, actin-based motility, and NF-κB/p38 chemokine response (F008)

SFG rickettsiae adhere to and invade endothelium via **surface cell antigen (Sca) autotransporters**. In *R. conorii*, **Sca2 alone is sufficient** to mediate both adherence and invasion of human endothelial cells and to drive intracellular actin-based motility, with separable mammalian-association and actin-nucleation domains. Intracellular motility occurs in **two phases**: an early **RickA/Arp2/3-dependent** phase (slow, curved actin tails) and a late **Sca2/formin-mimic-dependent** phase (fast, straight tails), enabling cell-to-cell spread. Endothelial infection activates **NF-κB** (biphasic for *R. conorii*; RelA p65–p50 dimers) and **p38 MAPK**, inducing the chemokines **IL-8 and MCP-1** (5–28-fold), which recruit neutrophils and monocytes. NF-κB inhibition abrogates the chemokine response, and p38 inhibition reduces IL-8/MCP-1 secretion.

> *"Sca2, has been shown to be sufficient to mediate both adherence and invasion of human endothelial cells and to participate in intracellular actin-based motility"* — [PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/)

> *"Early motility requires RickA and Arp2/3 complex... Late motility is independent of Arp2/3 complex and RickA and requires Sca2"* — [PMID: 24361066](https://pubmed.ncbi.nlm.nih.gov/24361066/)

> *"Infection of endothelial cells (ECs) lining vessel walls, and the resultant vascular inflammation and haemostatic alterations are salient pathogenetic features of both of these rickettsial diseases"* — [PMID: 17577053](https://pubmed.ncbi.nlm.nih.gov/17577053/)

> *"increased mRNA expression of IL-8 and MCP-1 in R. rickettsii-infected EC was evident as early as 3 h ... synthetic peptide SN-50 to inhibit the nuclear translocation of nuclear factor-kappa B (NF-kappaB) resulted in significant inhibition of the chemokine response"* — [PMID: 16128401](https://pubmed.ncbi.nlm.nih.gov/16128401/)

*Note:* the detailed molecular mechanism is derived from closely related SFG species (*R. conorii*, *R. rickettsii*) and *Orientia*, and is **inferred** for *R. honei* by phylogenetic conservation rather than demonstrated directly in *R. honei*. This forms the mechanistic backbone of **Section 6**.

### Finding 9 — Original 1991 clinical/epidemiologic and serologic description (F009)

Stewart (1991) identified **26 cases** of a spotted-fever-like illness over a **17-year period** in the ~1000-person Flinders Island population. Usual features were high fever, headache, myalgia, slight cough, arthralgia without joint swelling, and a maculopapular rash unlike common exanthems; **12 of 26 (~46%)** had a focal skin lesion (eschar); ticks were implicated as vector. The companion serologic study (Graves et al., 1991) showed patients had higher seroprevalence than 335 healthy islanders to Weil-Felix OX2 (36% vs <1%) and OX19 (36% vs <1%), and to SFG microimmunofluorescence antigens *R. rickettsii* (42% vs 1%), *R. australis* (46% vs 1%), and *R. conorii* (42% vs 1%) but not *R. typhi* (4% vs 4%). **Seroconversion was demonstrated in 7 of 26 patients (27%)**, confirming recent SFG rickettsial infection (the agent had not yet been isolated at that time).

> *"Twenty six cases of a spotted-fever-like illness have been identified over a 17 year period in the population of about 1000 of Flinders Island, Tasmania. The usual features were high fever, headache, myalgia, slight cough, arthralgia without joint swelling and a maculopapular rash which did not resemble the common exanthems. Twelve cases had a focal skin lesions. Available evidence implicates ticks as the vector."* — [PMID: 1986207](https://pubmed.ncbi.nlm.nih.gov/1986207/)

> *"In seven of the 26 patients (27%) seroconversion was demonstrated by means of Weil-Felix tests, confirming recent infection."* — [PMID: 1898756](https://pubmed.ncbi.nlm.nih.gov/1898756/)

This is the founding evidence for **Sections 1, 3, 9, and 10**.

---

## Section-by-Section Characterization

### 1. Disease Information
FISF is an acute, tick-borne SFG rickettsiosis of south-east Australia caused by *R. honei*. Identifiers: **MONDO:0000232**. OMIM is not applicable (infectious, non-Mendelian). Orphanet does not maintain a dedicated FISF entry as a rare genetic disease; it is catalogued under rickettsioses/spotted fevers. ICD-10: **A77.8** (Other spotted fevers) / ICD-11: **1C30.2** (Spotted fever due to other/unspecified *Rickettsia*). MeSH: the disease maps under "Rickettsia Infections" / "Spotted Fever Group Rickettsiosis"; organism MeSH term *Rickettsia honei*. Synonyms: Flinders Island spotted fever rickettsiosis; the eastern-Australian variant is the "marmionii" strain. **Information source:** aggregated disease-level literature (case series, serosurveys, vector surveys), not individual EHR/omics.

### 2. Etiology
**Primary cause:** infectious — the obligate intracellular bacterium *R. honei* transmitted by tick bite (F001, F002). **Risk factors:** environmental/occupational and recreational exposure to reptile-tick habitat in endemic south-east Australia; seasonality (autumn predominance, F003); outdoor activity. **Genetic host risk factors:** none identified — this is not a heritable disease. **Protective factors:** tick-bite avoidance (clothing, repellents, tick checks); prompt doxycycline. **Gene-environment interactions:** not applicable to the human host; the key "interaction" is ecological — the pathogen–tick–reptile cycle.

### 3. Phenotypes
See Finding 3 and Finding 9 for symptom frequencies. **Phenotype type:** predominantly symptoms/clinical signs (fever, rash, eschar, lymphadenopathy) with associated laboratory abnormalities typical of SFG rickettsioses (mild thrombocytopenia, mild transaminitis, elevated CRP — inferred from the SFG class; not specifically quantified for FISF in the reviewed literature). **Onset:** adult and pediatric; acute. **Severity:** mild-to-moderate and generally self-limited; severe illness is documented (Nepal case). **Progression:** acute, self-limited with treatment. **Frequency among affected:** fever ~100%, rash ~43%, eschar ~29–46%. **QoL impact:** acute febrile disability lasting days-to-weeks; excellent recovery with doxycycline; no documented chronic sequelae.

### 4. Genetic/Molecular Information
**Not applicable to the human host.** FISF has **no causal human genes, no pathogenic germline/somatic variants, no modifier genes, no host epigenetic changes, and no chromosomal abnormalities.** The relevant molecular biology is that of the *pathogen*: *R. honei* genome ~1.27 Mb; key genetic/antigenic loci used for identification and phylogeny include *gltA* (citrate synthase), *ompA*/*rompA*, *ompB*, *16S rRNA*, and the *17-kDa antigen* gene (F001). Pathogen virulence loci include the **Sca autotransporters (Sca2, OmpB/Sca5)** and the actin-nucleator **RickA** (F008). Suggested gene/protein annotations pertain to the bacterium, not the host.

### 5. Environmental Information
**Infectious agent:** *Rickettsia honei* (NCBI Taxonomy: *Rickettsia honei*). **Vector:** *Bothriocroton (Aponomma) hydrosauri* (reptile tick); also implicated/related ticks include *Amblyomma* spp. and *Haemaphysalis* spp. in different foci. **Environmental/lifestyle factors:** exposure to tick habitat; outdoor/rural activity; contact with reptiles or their tick-laden environments. No toxin, radiation, or pollution etiology.

### 6. Mechanism / Pathophysiology — Causal Chain

```
1. Infected reptile tick (B. hydrosauri) bites human
        │  (rickettsiae in tick salivary glands, F002)
        ▼
2. R. honei is inoculated into dermis → local replication → ESCHAR forms
        │
        ▼
3. Bacteria adhere to & invade vascular ENDOTHELIAL CELLS
        │  via Sca2 / OmpB(Sca5) autotransporters (F008, inferred from R. conorii)
        ▼
4. Intracellular replication + ACTIN-BASED MOTILITY
        │  early: RickA/Arp2/3 (curved tails); late: Sca2/formin-mimic (straight tails)
        ▼  → cell-to-cell spread through the endothelium
5. Endothelial signalling activated: NF-κB (RelA p65-p50) + p38 MAPK
        │
        ▼
6. Chemokine induction: IL-8 & MCP-1 (5–28×) → recruit neutrophils & monocytes
        │
        ├──▼ 7a. Perivascular leukocyte infiltration → VASCULITIS
        │        (leucocytoclastic vasculitis histologically, F004)
        │
        └──▼ 7b. Increased vascular permeability + haemostatic alterations
                 → RASH (maculopapular/petechial), local edema
        ▼
8. Systemic inflammatory response → FEVER, HEADACHE, MYALGIA/ARTHRALGIA,
   LYMPHADENOPATHY (clinical manifestation, F003/F009)
        ▼
9. Doxycycline halts bacterial replication → rapid resolution (self-limited)
```

**Upstream vs downstream:** the initiating lesion is tick inoculation and endothelial invasion (upstream); NF-κB/p38 chemokine signalling and leukocyte recruitment are intermediate; vasculitis, increased permeability, rash, and systemic febrile illness are downstream. **Cell types:** vascular endothelial cells (CL:0000115), neutrophils (CL:0000775), monocytes/macrophages (CL:0000576/CL:0000235). **GO biological processes:** response to bacterium (GO:0009617); actin-based movement / actin nucleation (GO:0006928, GO:0045010); NF-κB signaling (GO:0038061 / GO:0007249); chemokine production (GO:0032602); inflammatory response (GO:0006954). **GO cellular components:** host cell cytoplasm/cytoskeleton (GO:0005856); bacterial cell surface. **Metabolic/immune notes:** disease is driven by innate immune activation and chemokine-mediated leukocyte recruitment rather than autoimmunity or immunodeficiency. No omics profiling (transcriptomics/proteomics/metabolomics) specific to FISF is available in the reviewed literature.

### 7. Anatomical Structures Affected
- **Primary:** vascular endothelium of small and medium blood vessels (systemic) — **UBERON:0001981 (blood vessel), UBERON:0001986 (endothelium)**; cell type **CL:0000115 (endothelial cell)**.
- **Skin** (rash, eschar) — UBERON:0002097; lymph nodes (lymphadenopathy) — UBERON:0000029.
- **Body systems:** cardiovascular (vasculature), integumentary (skin), lymphatic/immune, musculoskeletal (arthralgia/myalgia), respiratory (cough), and potentially multi-organ in severe SFG disease (by analogy to Mediterranean spotted fever, F004).
- **Subcellular:** host cell cytosol/cytoskeleton (site of replication and actin-based motility) — GO:0005829 (cytosol), GO:0015629 (actin cytoskeleton).
- **Lateralization:** rash is typically generalized/bilateral; eschar is focal at the bite site.

### 8. Temporal Development
- **Onset:** acute, following an incubation period of ~days after tick bite; adult and pediatric.
- **Progression:** self-limited acute course over days to ~2 weeks; rapid defervescence after doxycycline.
- **Course pattern:** monophasic acute illness; not relapsing or chronic.
- **Critical period:** early antibiotic initiation (empiric doxycycline before serologic confirmation) is the key therapeutic window; delay risks more severe SFG disease.
- **Remission:** treatment-induced; spontaneous resolution possible but treatment shortens illness and prevents complications.
- **Seasonality:** autumn predominance in eastern Australia (F003).

### 9. Inheritance and Population
- **Inheritance:** not applicable (infectious, non-heritable). No penetrance/expressivity/anticipation/founder-effect/carrier-frequency concepts apply to the human host. (These concepts apply, if at all, only to the *pathogen's* clonal population genetics.)
- **Epidemiology:** rare. Founding series: 26 cases over 17 years in a ~1000-person island population (F009), implying a locally appreciable but numerically small burden; broader Australian incidence is not precisely quantified. FISF is likely underdiagnosed due to serologic cross-reactivity (F006).
- **Geographic distribution:** south-east Australia (Flinders Island, Tasmania, South Australia, Queensland/Torres Strait, Western Australia), with related *R. honei*/TT-118 in Thailand and Texas (F005, F007). Distribution tracks the reptile-tick vector.
- **Sex ratio / age:** not robustly quantified for FISF; SFG rickettsioses generally affect outdoor-exposed individuals across ages.

### 10. Diagnostics
- **Serology:** indirect immunofluorescence assay (IFA) is the mainstay; a **≥4-fold rise** between acute and convalescent titres to *R. honei* (and cross-reacting SFG antigens) confirms infection. Weil-Felix (OX2/OX19) was used historically (F009). **Cross-reactivity across SFG antigens is substantial** (F006), so serology confirms SFG infection but not species.
- **Molecular:** PCR and sequencing (targeting *gltA*, *ompA*, *ompB*, *17-kDa*) from eschar swab/biopsy or blood provides **species-level confirmation** and is the preferred definitive test.
- **Culture:** *R. honei* can be isolated (as in the index case) but requires specialized biosafety facilities; not routine.
- **Laboratory abnormalities:** typical SFG findings (mild thrombocytopenia, mild transaminase elevation, elevated inflammatory markers) — inferred for FISF from the SFG class.
- **Differential diagnosis:** Queensland tick typhus (*R. australis*), scrub typhus (*Orientia tsutsugamushi*), murine typhus (*R. typhi*), and other SFG rickettsioses; also dengue and other acute febrile illnesses in the region (F006).
- **Genetic testing / omics diagnostics:** not applicable to the host.

### 11. Outcome / Prognosis
- **Prognosis:** excellent with prompt doxycycline; FISF is generally **self-limited and non-fatal**. No FISF-specific mortality rate is established in the reviewed literature; severe illness is documented (Nepal, F003) but recovery is the norm.
- **Complications:** by analogy to other SFG rickettsioses, untreated or severe cases can have multi-organ involvement and vasculitic complications (F004); these appear uncommon in FISF.
- **Recovery:** full recovery expected; no documented chronic sequelae.
- **Prognostic factors:** timeliness of antibiotic therapy; host age/comorbidity.

### 12. Treatment
- **First-line pharmacotherapy:** **doxycycline** (tetracycline-class antibiotic; inhibits bacterial 30S ribosomal protein synthesis). Empiric therapy is recommended for suspected SFG rickettsiosis before confirmation. Rapid clinical response is characteristic (NCIT: Doxycycline C561; Tetracycline Antibiotic C1364).
- **Alternatives:** other tetracyclines; macrolides (e.g., clarithromycin/azithromycin) have been used for SFG rickettsioses, particularly in young children and pregnancy (by analogy to Mediterranean spotted fever); chloramphenicol is a historical alternative.
- **Advanced/experimental/targeted/immuno/gene/cell therapies:** not applicable.
- **Supportive care:** antipyretics, hydration, symptom management.
- **Pharmacogenomics:** none established for FISF.
- **Treatment outcome:** high response rate; adverse events are those of doxycycline (GI upset, photosensitivity, dental staining in young children — the reason macrolides are considered in that group).

### 13. Prevention
- **Primary prevention:** **tick-bite avoidance** — protective clothing, repellents (DEET/picaridin), avoiding reptile-tick habitat, prompt tick removal, and tick checks after outdoor exposure in endemic areas.
- **Vector control / public health:** habitat awareness; surveillance of reptile ticks to map foci (F002, F007).
- **Secondary prevention:** early recognition of the fever-rash-eschar syndrome and prompt empiric doxycycline.
- **Immunization:** no vaccine exists.
- **Prophylaxis:** routine post-tick-bite antibiotic prophylaxis is not standard; treat if symptomatic.
- **Counseling / genetic screening:** not applicable.

### 14. Other Species / Natural Disease
- **Reservoir/host taxonomy:** reptile tick *Bothriocroton (Aponomma) hydrosauri*; vertebrate hosts are reptiles — blue-tongued lizards (*Tiliqua* spp.), tiger and copperhead snakes; also *Tiliqua rugosa* (shingleback) carrying related *Rickettsia* (F002, F007).
- **Zoonotic transmission:** humans are incidental hosts infected by tick bite; there is no human-to-human transmission. This is a **zoonotic, vector-borne disease**.
- **Comparative biology:** related *R. honei* strain TT-118 circulates in *Ixodes granulatus* from *Rattus rattus* in Thailand and in *Amblyomma cajennense* in Texas (F005), indicating a broad host-tick range for the species. Multiple SFG *Rickettsia* can share reptile-tick vectors (F007).
- **Natural disease in companion/wildlife species:** clinical rickettsiosis attributable to *R. honei* in animals is not documented; reptiles and ticks serve as asymptomatic reservoirs.

### 15. Model Organisms
No dedicated *R. honei*/FISF animal model is described in the reviewed literature. Mechanistic understanding derives from **in vitro** human endothelial cell infection models and cell-biology studies using related SFG species (*R. conorii*, *R. rickettsii*) and *Orientia tsutsugamushi*, plus tick-cell (*Dermacentor variabilis*) invasion models for *R. montanensis* (F008 and supporting literature). These systems recapitulate endothelial invasion, actin-based motility, and NF-κB/p38 chemokine responses but are surrogates, not FISF-specific models. Guinea pig and mouse models are standard for SFG rickettsiae generally but are not reported specifically for *R. honei* here.

---

## Mechanistic Model / Interpretation

FISF is a paradigmatic **vector-borne endothelial infection**. The disease's clinical signature — fever, rash, and eschar — maps directly onto its cellular pathology. The **eschar** is the histologic footprint of local *R. honei* replication and vasculitis at the inoculation site; the **rash** reflects disseminated endothelial infection with increased vascular permeability; and the **systemic febrile syndrome** is the downstream consequence of NF-κB/p38-driven chemokine release and innate immune activation.

The molecular engine (Finding 8) is conserved across the SFG and is therefore confidently *inferred* for *R. honei*, though it has been demonstrated principally in *R. conorii* and *R. rickettsii*. The pathogen uses a two-tool strategy: **Sca autotransporters** for endothelial adhesion/invasion and **actin-based motility** (RickA/Arp2/3 early; Sca2/formin-mimic late) for intercellular spread without leaving the protected intracellular niche. Host endothelial signalling (NF-κB, p38 MAPK) then converts infection into the inflammatory chemokine milieu (IL-8, MCP-1) that recruits the neutrophils and monocytes responsible for vasculitis.

The **ecology** (Findings 2, 5, 7) is what makes FISF distinctive among rickettsioses: a **reptile**-based enzootic cycle with **transovarial** maintenance in the tick, so the tick is simultaneously vector and reservoir. This decouples pathogen persistence from mammalian amplifying hosts and ties human risk tightly to reptile-tick habitat. The observation that a single reptile-tick species can carry multiple *Rickettsia* species complicates simple vector-based risk mapping and argues for molecular (species-level) confirmation in both surveillance and diagnosis.

---

## Evidence Base

| PMID | Role in report | Supports finding |
|---|---|---|
| [9828442](https://pubmed.ncbi.nlm.nih.gov/9828442/) | Formal species description of *R. honei* strain RBT | F001 |
| [22815457](https://pubmed.ncbi.nlm.nih.gov/22815457/) | Confirms etiologic agent, isolation history, 1.27-Mb genome | F001 |
| [14628950](https://pubmed.ncbi.nlm.nih.gov/14628950/) | Vector/reservoir identification; 63% tick positivity; vertical transmission | F002 |
| [12860601](https://pubmed.ncbi.nlm.nih.gov/12860601/) | Reptile vertebrate-host ecology; three-continent distribution | F002, F005 |
| [12860602](https://pubmed.ncbi.nlm.nih.gov/12860602/) | Ultrastructural/EM evidence of transovarial transmission in *A. hydrosauri* | F002 |
| [17553271](https://pubmed.ncbi.nlm.nih.gov/17553271/) | "marmionii" case series; symptom frequencies; Australia's 4 rickettsioses | F003, F006 |
| [22000356](https://pubmed.ncbi.nlm.nih.gov/22000356/) | Severe imported case, Nepal 2009 | F003 |
| [19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/) | Endothelial tropism → rickettsial vasculitis | F004 |
| [33622746](https://pubmed.ncbi.nlm.nih.gov/33622746/) | Leucocytoclastic vasculitis histology (SFG correlate) | F004 |
| [16175900](https://pubmed.ncbi.nlm.nih.gov/16175900/) | Geographic extension across south-east Australia | F005 |
| [18214193](https://pubmed.ncbi.nlm.nih.gov/18214193/) | Co-circulation with *R. australis* and scrub typhus | F006 |
| [30270856](https://pubmed.ncbi.nlm.nih.gov/30270856/) | First WA SFG rickettsiosis incl. *R. honei* | F007 |
| [27338482](https://pubmed.ncbi.nlm.nih.gov/27338482/) | *B. hydrosauri* carries non-*honei* *Rickettsia* | F007 |
| [22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/) | Sca2 mediates adhesion/invasion/motility | F008 |
| [24361066](https://pubmed.ncbi.nlm.nih.gov/24361066/) | Two-phase actin-based motility (RickA/Arp2/3 → Sca2) | F008 |
| [17577053](https://pubmed.ncbi.nlm.nih.gov/17577053/) | Endothelial infection, NF-κB/p38, vascular inflammation | F008 |
| [16128401](https://pubmed.ncbi.nlm.nih.gov/16128401/) | NF-κB regulation of IL-8/MCP-1 in infected EC | F008 |
| [16153249](https://pubmed.ncbi.nlm.nih.gov/16153249/) | p38 activation drives chemokine response | F008 |
| [1986207](https://pubmed.ncbi.nlm.nih.gov/1986207/) | Founding clinical/epidemiologic description (26 cases/17 yr) | F009 |
| [1898756](https://pubmed.ncbi.nlm.nih.gov/1898756/) | Founding serologic confirmation (seroconversion 27%) | F009 |
| [11716110](https://pubmed.ncbi.nlm.nih.gov/11716110/) | Thai tick typhus TT-118 = *R. honei* in *I. granulatus* | F005 |
| [38194190](https://pubmed.ncbi.nlm.nih.gov/38194190/) | Reptile-tick *Rickettsia* surveillance (NSW) | F007 |

**Evidence source types:** F001, F003, F005, F006, F007, F009 rest on **human clinical/epidemiologic and vector-surveillance** data specific to *R. honei*/FISF. F002 combines **field ecology, PCR, and EM**. F004 and F008 rest largely on **in vitro** endothelial/cell-biology studies of *related* SFG species and are **inferred** for *R. honei* by phylogenetic conservation.

---

## Limitations and Knowledge Gaps

1. **Mechanism is inferred, not demonstrated in *R. honei*.** The Sca2/OmpB invasion and NF-κB/p38 chemokine cascade come from *R. conorii*, *R. rickettsii*, and *Orientia* studies. Direct molecular studies of *R. honei* itself are lacking.
2. **No FISF-specific animal model or omics data.** There are no transcriptomic, proteomic, or metabolomic signatures reported for FISF, and no dedicated model organism.
3. **Imprecise epidemiology.** Incidence/prevalence beyond the original island series are not well quantified; underdiagnosis due to serologic cross-reactivity likely biases case counts.
4. **Sparse quantitative clinical/laboratory data.** Symptom frequencies come from small series (n = 7; n = 26). Laboratory abnormalities (thrombocytopenia, transaminitis) are inferred from the SFG class rather than measured in FISF cohorts.
5. **Prognosis data are qualitative.** No formal mortality/morbidity rates or quality-of-life instruments have been applied to FISF.
6. **Template mismatch.** Sections designed for genetic diseases (causal genes, inheritance, penetrance, model organisms, gene therapy) are largely not applicable; the report reinterprets these in terms of pathogen biology and ecology.

---

## Proposed Follow-up Actions

1. **Direct molecular validation in *R. honei*:** infect primary human dermal microvascular endothelial cells with *R. honei* and confirm Sca2/OmpB-dependent invasion, two-phase actin motility, and NF-κB/p38-driven IL-8/MCP-1 induction — closing the inference gap for F008.
2. **Prospective clinical cohort:** assemble a multi-centre south-east Australian FISF cohort with standardized PCR confirmation to quantify symptom frequencies, laboratory abnormalities, severity distribution, and outcomes.
3. **Seroepidemiology with species-specific assays:** develop and deploy *R. honei*-specific serologic/molecular tools to overcome SFG cross-reactivity and produce true prevalence/incidence estimates.
4. **Expanded vector/reservoir surveillance:** systematically genotype *Rickettsia* in reptile ticks across the Australian range (and WA foci) to map *R. honei* vs. co-circulating SFG species and refine human-risk geography.
5. **Comparative genomics:** leverage the 1.27-Mb *R. honei* genome against *R. conorii*/*R. rickettsii* to identify virulence-locus conservation/divergence that may explain FISF's generally milder course.
6. **Diagnostic algorithm formalization:** validate eschar-swab PCR as a rapid, species-level point-of-care confirmatory test and integrate into Australian febrile-illness guidelines alongside empiric doxycycline.

---

*Report compiled from 5 investigative iterations, 9 confirmed findings, and 42 reviewed papers. Evidence is drawn from primary literature; mechanistic claims specific to* R. honei *are flagged as inferred from closely related spotted fever group rickettsiae where direct data are unavailable.*


## Artifacts

- [OpenScientist final report](Flinders_Island_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Flinders_Island_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0000232` (3 mentions) - the report calls it "MONDO ID"; MONDO calls it **Flinders island spotted fever**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006928` (obsolete movement of cell or subcellular component) (1 mention)