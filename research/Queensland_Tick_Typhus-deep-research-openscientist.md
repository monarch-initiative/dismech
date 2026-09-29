---
provider: openscientist
model: openscientist-autonomous
cached: true
start_time: '2026-09-25T05:42:50.256414'
end_time: '2026-09-25T05:42:50.271391'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Queensland Tick Typhus
  mondo_id: MONDO:0001118
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
citation_count: 24
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 14
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 27
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 15
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0000465
    reported_labels:
    - Lymphatic system
    ontology_label: material anatomical entity
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Queensland_Tick_Typhus-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Queensland_Tick_Typhus-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Queensland Tick Typhus
- **MONDO ID:** MONDO:0001118 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Queensland Tick Typhus** covering all of the
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

# Queensland Tick Typhus (MONDO:0001118): A Comprehensive Disease-Characteristics Report

## Summary

**Queensland Tick Typhus (QTT)** is an acute, tick-borne **spotted fever group (SFG) rickettsiosis** caused by the obligate intracellular Gram-negative bacterium ***Rickettsia australis***. It is transmitted to humans by the bite of hard (ixodid) ticks — principally *Ixodes holocyclus* (the eastern paralysis tick) and *Ixodes tasmani* — along a ~3,200-km strip of eastern coastal Australia, from tropical North Queensland to temperate Tasmania/Victoria. It is a **non-genetic infectious disease**: there are no causal human genes, no inherited susceptibility loci of established clinical importance, and the dominant risk factor is simply environmental/occupational/recreational exposure to tick habitat.

Clinically, QTT is usually a **mild, self-limited eschar-associated febrile illness** characterized by fever, headache, a maculopapular or vesicular rash, an inoculation eschar at the tick-bite site, and regional (draining) lymphadenopathy. However, a clinically significant minority of patients develop **severe disease** requiring intensive-care admission, and death and permanent disability are documented. After tick inoculation the organism first replicates in **dermal/tissue macrophages**, then disseminates to and infects **vascular endothelial cells**, producing the hallmark **"rickettsial vasculitis"** that underlies the rash, eschar, and (in severe cases) increased vascular permeability and multi-organ dysfunction. Host control depends on **innate signaling (TLR4 → MyD88 → ASC inflammasome, dendritic-cell instruction, Th1/IFN-γ)** and, decisively, on **perforin-dependent, MHC class I-restricted CD8⁺ cytotoxic T lymphocytes (CTLs)**, which mouse-model gene-knockout studies show are even more critical to recovery than IFN-γ.

Diagnosis rests on **serology** (indirect immunofluorescence assay [IFA]: a ≥4-fold rise in paired sera or a single IgG titre ≥1:64) combined with **PCR** (real-time qPCR of whole blood, eschar swab, or skin biopsy). First-line treatment is **doxycycline**, which is highly effective and protective against progression to severe disease; **fluoroquinolones should be avoided** because they are associated with worse outcomes in SFG rickettsioses. There is **no licensed vaccine**; prevention is entirely based on tick-bite avoidance, prompt tick removal, and environmental/personal protective measures. This report synthesizes 11 confirmed findings from 42 reviewed papers into the 15-section disease-characteristics template requested.

---

## Section 1 — Disease Information

**Overview.** Queensland Tick Typhus is a zoonotic, vector-borne SFG rickettsiosis. It was first recognized clinically in Queensland, and its causative agent, *Rickettsia australis*, was isolated in Queensland in 1950 (type strain "Phillips") — over four decades before comprehensive case reviews consolidated it as a distinct endemic Australian rickettsiosis ([PMID: 22933759](https://pubmed.ncbi.nlm.nih.gov/22933759/); [PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0001118 (Queensland tick typhus) |
| Causative organism (NCBI Taxonomy) | *Rickettsia australis* (species) |
| MeSH concept | Spotted fever group rickettsiosis / *Rickettsia* infections (no unique QTT MeSH descriptor) |
| ICD-10 | A77.3 (Spotted fever due to *Rickettsia australis*) |
| ICD-11 | 1C30.2 / spotted fever group rickettsiosis category |
| OMIM / Orphanet | Not applicable (infectious, non-Mendelian; no OMIM entry) |

**Synonyms / alternative names.** Queensland tick typhus; Australian tick typhus; North Queensland tick typhus; *Rickettsia australis* infection; Australian spotted fever (in part — note that "Australian spotted fever" also encompasses Flinders Island spotted fever caused by *R. honei*, a distinct co-endemic agent).

**Source of information.** The knowledge base for QTT is derived from **aggregated disease-level resources** — published case series, hospital audits, serosurveys, microbiological/genomic characterizations, and animal-model immunology — rather than from individual-patient EHR data.

---

## Section 2 — Etiology

**Primary cause (infectious).** QTT is caused by infection with *Rickettsia australis*, an obligately intracellular SFG rickettsia, delivered into the skin during the blood meal of an infected ixodid tick ([PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/)). It is **not** a genetic, autoimmune, metabolic, or neoplastic disease.

**Risk factors.**
- **Genetic risk factors (human):** None of established clinical relevance. No causal variants, susceptibility loci, or modifier genes have been identified for human QTT. Innate-immunity genes (*MYD88*, *TLR4*, inflammasome components, MHC-I, perforin/*PRF1*) are mechanistically important in **animal models** (see Sections 4 and 6) but are not validated human susceptibility markers.
- **Environmental / behavioral risk factors:** Exposure to tick-infested vegetation in endemic eastern-coastal Australia is the principal risk factor — including bushwalking, gardening, camping, and outdoor occupations. Epidemiology shows a skew toward **older males** and a **late spring/early summer (November–December)** seasonal peak, reflecting exposure patterns and tick questing behavior ([PMID: 31268225](https://pubmed.ncbi.nlm.nih.gov/31268225/)).

**Protective factors.** No genetic protective variants are described in humans. The single most effective environmental protective factor is **tick-bite avoidance** (protective clothing, repellents, tick checks, prompt removal). Prompt **doxycycline** after infection is protective against severe disease progression ([PMID: 21642652](https://pubmed.ncbi.nlm.nih.gov/21642652/)).

**Gene–environment interactions.** Not characterized in humans. The relevant "gene–environment" axis is between the pathogen's virulence factors and the host's innate/adaptive immune genotype, demonstrated experimentally in mice (MyD88, TLR4/ASC, perforin, MHC-I).

---

## Section 3 — Phenotypes

QTT produces a stereotyped SFG-rickettsiosis phenotype. Sexton et al. summarized the classic presentation: *"QTT is usually a mild disease. Patients often have regional lymphadenopathy and eschars. Some have vesicular rashes."* ([PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/)).

| Phenotype | Type | HPO suggestion | Typical frequency / notes |
|---|---|---|---|
| Fever | Symptom/sign | HP:0001945 (Fever) | Near-universal; commonly reported ([PMID: 31268225](https://pubmed.ncbi.nlm.nih.gov/31268225/)) |
| Inoculation eschar (tache noire) | Clinical sign | HP:0200041 (Skin ulcer) / eschar | Frequent; hallmark at tick-bite site ([PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/)) |
| Maculopapular / vesicular rash | Physical manifestation | HP:0000988 (Skin rash); HP:0200037 (Vesicle) | Common; vesicular rash a distinctive QTT feature |
| Regional lymphadenopathy | Clinical sign | HP:0002716 (Lymphadenopathy) | Common (draining nodes) |
| Headache | Symptom | HP:0002315 (Headache) | Common |
| Lethargy / malaise | Symptom | HP:0001254 (Lethargy) | Common ([PMID: 31268225](https://pubmed.ncbi.nlm.nih.gov/31268225/)) |
| Myalgia | Symptom | HP:0003326 (Myalgia) | Common |
| Elevated transaminases | Lab abnormality | HP:0002910 (Elevated hepatic transaminase) | Frequent in SFG rickettsioses |
| Thrombocytopenia | Lab abnormality | HP:0001873 (Thrombocytopenia) | Variable; marks more severe disease |
| Severe disease (ICU / organ dysfunction) | Clinical course | critical illness | ~13–22% ICU in SFG hospital cohorts ([PMID: 31318873](https://pubmed.ncbi.nlm.nih.gov/31318873/); [PMID: 32959771](https://pubmed.ncbi.nlm.nih.gov/32959771/)) |

**Onset / severity / progression.** Adult-onset predominant (any age exposed can be affected). Severity is **variable** — mild in most, but severe/fatal in a minority. Course is **acute and self-limited** with appropriate therapy. In a 20-year North Queensland audit of 135 cases (95 scrub typhus, 37 SFG/QTT), 18/135 (13%) required ICU; the SFG subgroup had a **higher ICU rate (8/37, 22%)** and 3/37 (8%) had severe disease — *"1 died, 2 developed permanent disability"* — versus 0/95 scrub typhus (p = 0.02) ([PMID: 31318873](https://pubmed.ncbi.nlm.nih.gov/31318873/)). By contrast, paediatric rickettsial infection in tropical Australia has *"a relatively benign clinical course"* with no ICU admission or death among 15 children ([PMID: 32252063](https://pubmed.ncbi.nlm.nih.gov/32252063/)).

**Quality-of-life impact.** Not formally measured with instruments (EQ-5D/SF-36) for QTT. For most patients the illness is acute and fully reversible; the QoL burden concentrates in the severe subset who suffer prolonged hospitalization, ICU stay, or (rarely) permanent disability.

---

## Section 4 — Genetic/Molecular Information

**Human genetics.** QTT is an infectious disease with **no causal human genes, no pathogenic germline/somatic variants, no modifier genes, no epigenetic disease signatures, and no chromosomal abnormalities.** Sections requesting ClinVar/gnomAD/COSMIC variant data are **not applicable**.

**Pathogen genome (the relevant molecular biology).** The *R. australis* strain Phillips genome is a compact **1.29-Mb** chromosome accompanied by **two plasmids**, and is *"highly similar to that of Rickettsia akari"* ([PMID: 22933759](https://pubmed.ncbi.nlm.nih.gov/22933759/)). Phylogenetically, multiple independent gene analyses place *R. australis* firmly within the **"Rickettsia akari group"** of the SFG, alongside *R. akari* (rickettsialpox agent) and the ELB/*R. felis* agent (gene D: [PMID: 11491333](https://pubmed.ncbi.nlm.nih.gov/11491333/); citrate synthase *gltA*: [PMID: 9103608](https://pubmed.ncbi.nlm.nih.gov/9103608/)). Notably, *R. australis* is described as *"the most divergent rickettsia of the spotted fever group"* on the basis of its outer-membrane protein A and B genes ([PMID: 11034486](https://pubmed.ncbi.nlm.nih.gov/11034486/)). Key rickettsial virulence/antigen loci include *ompA*, *ompB* (surface cell antigens mediating adhesion/invasion), the 17-kDa antigen gene, and *gltA*.

**Host immune-gene involvement (model organism).** Genes shown experimentally to govern outcome are *Myd88*, *Tlr4*, inflammasome adaptor *Pycard*/ASC, MHC class I, and perforin (*Prf1*) — see Section 6.

---

## Section 5 — Environmental Information

**Environmental factors.** The disease is defined by an environmental exposure: contact with tick habitat in the humid sclerophyll forests, coastal scrub, and peri-urban bushland of eastern Australia. No chemical toxin, radiation, or pollutant is involved.

**Lifestyle factors.** Outdoor recreation and occupation (bushwalking, camping, gardening, forestry, field work) increase exposure. Seasonality (late spring–summer) reflects tick activity ([PMID: 31268225](https://pubmed.ncbi.nlm.nih.gov/31268225/)).

**Infectious agent.** *Rickettsia australis* — an obligately intracellular, cytosolically replicating, Gram-negative alphaproteobacterium (order Rickettsiales, SFG, *R. akari* group). It is a pathogen, not a chemical entity. Vectors *Ixodes holocyclus* and *Ixodes tasmani* maintain the organism; small native mammals (rodents, bandicoots, marsupials) serve as reservoir/amplifying hosts, with humans as **accidental dead-end hosts** ([PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/); [PMID: 25434042](https://pubmed.ncbi.nlm.nih.gov/25434042/)).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. An **infected ixodid tick** (*I. holocyclus* / *I. tasmani*) attaches and takes a blood meal, **inoculating** *R. australis* into the dermis at the bite site. → *(demonstrated)*
2. Local infection and replication in **dermal/tissue macrophages** — *"Macrophages are one of the initial targets for rickettsiae after inoculation by ticks"* — **leads to** an early intracellular replication niche and a localized inflammatory/necrotic focus that becomes the **eschar** ([PMID: 30297526](https://pubmed.ncbi.nlm.nih.gov/30297526/)). → *(demonstrated in mouse model)*
3. Rickettsiae disseminate (lymphatics → draining nodes, producing **regional lymphadenopathy**; and haematogenously) and **infect vascular endothelial cells**, the pathogen's principal target — *"the pathogen's affinity for endothelium lining the blood vessels"* — **resulting in** endothelial infection throughout small vessels ([PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)). → *(demonstrated)*
4. Endothelial infection **causes** *"vascular inflammation, insult to vascular integrity and compromised vascular permeability, collectively termed 'Rickettsial vasculitis'"* ([PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)). → *(demonstrated)*
5. Rickettsial vasculitis **produces** the clinical phenotype: perivascular mononuclear infiltrate → **maculopapular/vesicular rash**; microvascular injury → increased permeability. → *(inferred from SFG pathology, consistent across the group)*
6. **Branch (host innate immunity):** Pathogen-associated molecular patterns engage **TLR4 → MyD88** signaling and activate the **ASC inflammasome**, driving dendritic-cell instruction, macrophage/neutrophil recruitment, and a **Th1 cytokine milieu (IFN-γ, IL-6, IL-1β, IL-12p40)** that **restrains** bacterial burden ([PMID: 32014896](https://pubmed.ncbi.nlm.nih.gov/32014896/); [PMID: 26755162](https://pubmed.ncbi.nlm.nih.gov/26755162/)). → *(demonstrated in mouse model)*
7. **Branch (host adaptive immunity, decisive):** **MHC class I-restricted, perforin-dependent CD8⁺ CTLs** recognize and kill infected macrophages and endothelial cells, **clearing** the infection — this effector arm is *"more critical to recovery… than were the effects of IFN-gamma"* ([PMID: 11179362](https://pubmed.ncbi.nlm.nih.gov/11179362/)). → *(demonstrated in mouse model)*
8. **Outcome branch:** When innate + CD8 CTL immunity (aided by timely doxycycline) controls the organism → **mild, self-limited illness**. When bacterial dissemination outpaces immunity (older age, delayed treatment) → widespread endothelial injury, capillary leak, organ dysfunction → **severe disease / death** ([PMID: 31318873](https://pubmed.ncbi.nlm.nih.gov/31318873/)). → *(inferred, supported by clinical severity data)*

### Detail by category

- **Molecular pathways:** TLR4→MyD88→NF-κB innate signaling; ASC/NLR inflammasome → caspase-1 → IL-1β maturation; Th1/IFN-γ–STAT1 axis; MHC-I antigen-presentation and perforin/granzyme cytotoxicity pathway.
- **Cellular processes:** Intracellular bacterial invasion and cytosolic replication; inflammation; macrophage and endothelial infection; CTL-mediated cytotoxicity of infected cells; endothelial activation and increased permeability.
- **Protein dysfunction:** Not a protein-misfolding disease; pathology is driven by pathogen invasins (OmpA/OmpB) and host endothelial-barrier dysfunction.
- **Immune involvement:** Central and protective (innate TLR4/MyD88/ASC; adaptive CD8 CTL). Loss of MyD88 causes *"severely impaired bacterial clearance in vivo"* ([PMID: 26755162](https://pubmed.ncbi.nlm.nih.gov/26755162/)).
- **Tissue-damage mechanism:** Rickettsial vasculitis — immune-mediated and infection-mediated microvascular injury with increased permeability ([PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)).

**Suggested ontology terms.** GO: GO:0002224 (toll-like receptor signaling pathway), GO:0045087 (innate immune response), GO:0001913 (T cell-mediated cytotoxicity), GO:0006954 (inflammatory response), GO:0050830 (defense response to Gram-negative bacterium). CL: CL:0000235 (macrophage), CL:0000071 (blood vessel endothelial cell), CL:0000625 (CD8-positive, alpha-beta T cell), CL:0000451 (dendritic cell).

---

## Section 7 — Anatomical Structures Affected

- **Primary target:** systemic **small-vessel vascular endothelium** (UBERON:0001986 endothelium; UBERON:0000115 endothelial layer of blood vessel) — the unifying lesion of SFG rickettsiosis ([PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)).
- **Skin (UBERON:0002097):** eschar at inoculation site; maculopapular/vesicular rash.
- **Lymphatic system (UBERON:0000465):** regional draining **lymph nodes** (UBERON:0000029) — lymphadenopathy.
- **Body systems involved:** cardiovascular (microvasculature), integumentary, lymphoid/immune; in severe disease, potential secondary involvement of lung, liver, kidney, and CNS via generalized vasculitis/capillary leak.
- **Cell populations targeted:** vascular endothelial cells (CL:0000071) and macrophages (CL:0000235); CD8⁺ CTLs (CL:0000625) are the key effector population.
- **Subcellular level:** *R. australis* is a **cytosolic** pathogen — it replicates free in the host-cell cytoplasm (GO:0005829 cytosol), escaping the phagosome.
- **Lateralization:** the eschar/lymphadenopathy are **localized/unilateral** to the bite site; the rash and vasculitis are **generalized/bilateral**.

---

## Section 8 — Temporal Development

- **Onset:** **acute**, following an incubation period of roughly 7–10 days after the tick bite; patients in the ICU series presented a median of 7 (IQR 5–10) days after symptom onset ([PMID: 32959771](https://pubmed.ncbi.nlm.nih.gov/32959771/)).
- **Progression / course:** **self-limited** in most, resolving over days to ~1–2 weeks with therapy; **not** chronic, relapsing, or lifelong. A minority progress to severe multi-organ disease.
- **Treatment-response kinetics:** In hospitalized scrub typhus/QTT patients on anti-rickettsial therapy, **32/58 (56%) had delayed defervescence (>48 h)**; delayed defervescence was associated with older age (median 52 vs 40 y, p = 0.05), higher ICU admission (38% vs 12%, p = 0.02), and longer stay — challenging the dogma that persistent fever >48 h implies a wrong diagnosis ([PMID: 33075531](https://pubmed.ncbi.nlm.nih.gov/33075531/)).
- **Critical period for intervention:** early — doxycycline given *"prior to deterioration of disease… protected patients from development of severe"* disease in the analogous Mediterranean spotted fever cohort ([PMID: 21642652](https://pubmed.ncbi.nlm.nih.gov/21642652/)).
- **Remission:** treatment-induced (doxycycline) and, in mild cases, potentially spontaneous.

---

## Section 9 — Inheritance and Population

**Inheritance.** Not applicable — infectious, non-heritable. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier-frequency considerations.

**Epidemiology.**
- QTT/Australian SFG rickettsiosis is a **rare, notifiable, seasonally patterned** infection. In Tasmania (2012–2017), *"The mean number of cases per year was 3.0 (population rate 0.6 per 100,000 population/year); 60% of cases occurred in November and December. Cases were more commonly older males"* ([PMID: 31268225](https://pubmed.ncbi.nlm.nih.gov/31268225/)). (Note: Tasmanian SFG cases are predominantly Flinders Island spotted fever caused by *R. honei*, a co-endemic agent; true QTT/*R. australis* predominates on the mainland eastern seaboard.)
- Ascertainment/incidence is **rising**: in a North Queensland tertiary hospital, *"There were nine hospitalizations during the first 5 years of the study period and 81 in the last 5 years (p for trend = 0.003)"* ([PMID: 31318873](https://pubmed.ncbi.nlm.nih.gov/31318873/)).

**Population demographics.**
- **Geographic distribution:** eastern coastal Australia across a **~3,200-km span** *"from tropical to temperate climates"* — Queensland, New South Wales, Victoria, and Tasmania ([PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/)).
- **Sex / age:** skewed to **older males** ([PMID: 31268225](https://pubmed.ncbi.nlm.nih.gov/31268225/)); paediatric cases occur but run a milder course ([PMID: 32252063](https://pubmed.ncbi.nlm.nih.gov/32252063/)).

---

## Section 10 — Diagnostics

**Clinical/laboratory tests.**
- **Serology (mainstay):** indirect immunofluorescence assay (IFA); diagnosis by a **≥4-fold rise** in IgG between acute and convalescent sera, or a single **IgG titre ≥1:64** with a compatible illness ([PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/); titre convention as applied in SFG serosurveys, [PMID: 31288833](https://pubmed.ncbi.nlm.nih.gov/31288833/)). Limitation: antibodies are absent early in illness.
- **Molecular (PCR):** real-time qPCR targeting SFG/*R. australis*-specific genes (e.g., *gltA*, *ompA*, *ompB*, 17-kDa) on **whole blood, eschar swab, or skin biopsy**; validated *R. australis* real-time PCR assays are in routine reference use ([PMID: 22092999](https://pubmed.ncbi.nlm.nih.gov/22092999/)).
- **Recommended strategy:** *"the best strategy is to use a real-time quantitative polymerase chain reaction (qPCR) and immunofluorescence assay in tandem"* ([PMID: 31587667](https://pubmed.ncbi.nlm.nih.gov/31587667/)).
- **Supportive labs:** mild thrombocytopenia, leukopenia/leukocytosis, elevated transaminases, elevated CRP (non-specific).
- **Culture:** possible but hazardous/slow; restricted to reference labs.

**Genetic testing / omics diagnostics.** Human genetic testing is **not applicable**. Pathogen genomics (WGS/PCR) is used for organism identification and epidemiology, not for host diagnosis.

**Clinical criteria & differential diagnosis.** Because *"clinical features overlap, serologic tests are necessary to distinguish QTT from other endemic Australian rickettsial diseases (scrub and murine typhus)"* ([PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/)). Key differentials: **scrub typhus** (*Orientia tsutsugamushi*), **murine typhus** (*R. typhi*), and **Flinders Island spotted fever** (*R. honei*), which *"extends beyond Flinders Island"* across south-east Australia ([PMID: 16175900](https://pubmed.ncbi.nlm.nih.gov/16175900/)); also dengue, leptospirosis, and Q fever in the same region.

**Screening.** No population screening (acute, sporadic, environmentally acquired infection).

---

## Section 11 — Outcome / Prognosis

- **Overall prognosis:** Good with prompt doxycycline; usually mild and self-limited ([PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/)).
- **Severe disease / mortality:** A real minority. In the North Queensland audit, **3/37 (8%)** SFG patients had severe disease (1 death, 2 permanent disability) versus 0/95 scrub typhus (p = 0.02) ([PMID: 31318873](https://pubmed.ncbi.nlm.nih.gov/31318873/)); a 23-year ICU series included **9 QTT patients (median APACHE II 13)** ([PMID: 32959771](https://pubmed.ncbi.nlm.nih.gov/32959771/)).
- **Recovery:** Complete recovery is the norm with treatment; residual disability is rare.
- **Prognostic factors:** older age, ICU-level illness, and **delayed defervescence (>48 h)**, which is *"more common in patients with severe disease"* ([PMID: 33075531](https://pubmed.ncbi.nlm.nih.gov/33075531/)); paediatric age predicts a benign course ([PMID: 32252063](https://pubmed.ncbi.nlm.nih.gov/32252063/)).

---

## Section 12 — Treatment

**First-line pharmacotherapy — doxycycline (NCIT: C312; tetracycline-class antibiotic).** Doxycycline is the standard of care. In the analogous Mediterranean spotted fever cohort, *"Doxycycline administration prior to deterioration of disease (in 31 patients) protected patients from development of severe MSF"* (RR 0.248, 95% CI 0.08–0.76) with earlier defervescence (3.0 vs 7.1 days) ([PMID: 21642652](https://pubmed.ncbi.nlm.nih.gov/21642652/)).

**Avoid fluoroquinolones.** In the same analysis, *"fluoroquinolone treatment was associated with increased MSF disease severity"* (RR 2.53, 95% CI 1.40–4.55) — so fluoroquinolones should be avoided in SFG rickettsioses ([PMID: 21642652](https://pubmed.ncbi.nlm.nih.gov/21642652/)).

**Alternatives.** Macrolides (e.g., azithromycin) are considered for children/pregnancy in SFG rickettsioses, though experimental data (canine RMSF) suggest azithromycin is *less* efficacious than doxycycline ([PMID: 10103185](https://pubmed.ncbi.nlm.nih.gov/10103185/)); chloramphenicol is a historical alternative.

**Supportive care.** Antipyretics, fluids, and — for the severe/ICU subset — organ support (vasopressors, ventilation) as needed ([PMID: 32959771](https://pubmed.ncbi.nlm.nih.gov/32959771/)).

**Advanced/experimental therapeutics, pharmacogenomics, surgery, targeted/immuno/cell/gene therapy:** Not applicable — QTT is cured by a short antibiotic course.

**Treatment-response caveat.** Persistent fever >48 h after starting doxycycline does **not** necessarily indicate misdiagnosis; delayed defervescence occurs in ~56% and correlates with severity ([PMID: 33075531](https://pubmed.ncbi.nlm.nih.gov/33075531/)).

**Suggested NCIT term:** Doxycycline (NCIT:C312); Tetracycline antibiotic therapy.

---

## Section 13 — Prevention

- **Primary prevention:** No vaccine exists. Prevention relies on **tick-bite avoidance** — protective clothing, DEET/permethrin repellents, avoiding tick habitat during peak season, systematic tick checks, and **prompt, correct tick removal** after exposure in endemic eastern Australia.
- **Chemoprophylaxis:** Routine post-tick-bite antibiotic prophylaxis is **not** recommended; management is watchful waiting with early empiric doxycycline if symptoms develop.
- **Secondary prevention:** Early recognition and prompt doxycycline to prevent progression to severe disease ([PMID: 21642652](https://pubmed.ncbi.nlm.nih.gov/21642652/)).
- **Tertiary prevention:** Supportive/ICU care to prevent complications in severe cases.
- **Public health:** Clinician and public education (given rising ascertainment, [PMID: 31318873](https://pubmed.ncbi.nlm.nih.gov/31318873/)), notifiable-disease surveillance, and environmental/personal tick-control measures. Genetic counseling is not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Vectors (NCBI Taxonomy):** *Ixodes holocyclus* (paralysis tick) and *Ixodes tasmani* are the only two confirmed vectors of *R. australis* ([PMID: 1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/)). *I. holocyclus* is *"the cause of the neurotoxic disease tick paralysis in humans and mammals"* in densely populated eastern Australia ([PMID: 25434042](https://pubmed.ncbi.nlm.nih.gov/25434042/)).
- **Reservoir hosts:** native small mammals — rodents, bandicoots, and marsupials — maintain *R. australis* in nature; humans are accidental dead-end hosts.
- **Zoonotic transmission:** QTT is a **zoonosis** transmitted only via tick bite; there is no human-to-human transmission.
- **Comparative biology / cross-species susceptibility:** *R. australis* has been detected molecularly in *Ixodes ricinus* ticks in Europe, indicating a broader potential vector/host range than the Australian endemic cycle ([PMID: 18355299](https://pubmed.ncbi.nlm.nih.gov/18355299/)); DNA identical/very close to *R. australis* has been found in mite endosymbiont surveys ([PMID: 31549736](https://pubmed.ncbi.nlm.nih.gov/31549736/)). No significant naturally occurring clinical disease from *R. australis* is documented in companion animals (contrast *R. rickettsii*, which causes canine Rocky Mountain spotted fever, [PMID: 10103185](https://pubmed.ncbi.nlm.nih.gov/10103185/)).

---

## Section 15 — Model Organisms

- **Principal model — mouse (*Mus musculus*, NCBI Taxon 10090):** The C57BL/6 mouse is the workhorse for *R. australis* immunopathogenesis. Gene-knockout and adoptive-transfer studies established the protective hierarchy of host immunity:
  - **Perforin⁻/⁻** and **IFN-γ⁻/⁻** mice are *"more than 100-fold more susceptible"* and **MHC class I⁻/⁻** mice *">50,000-fold"* more susceptible to lethal *R. australis*; *"CTL activity was more critical to recovery from rickettsial infection than were the effects of IFN-gamma"* ([PMID: 11179362](https://pubmed.ncbi.nlm.nih.gov/11179362/)).
  - **MyD88⁻/⁻** mice show *"severely impaired bacterial clearance in vivo"* with blunted IFN-γ/IL-6/IL-1β and defective dendritic-cell maturation ([PMID: 26755162](https://pubmed.ncbi.nlm.nih.gov/26755162/)).
  - **TLR4/ASC-inflammasome** contributes to host immunity against *R. australis* ([PMID: 32014896](https://pubmed.ncbi.nlm.nih.gov/32014896/)).
  - Macrophage-tropism studies use *R. australis* in mice to show macrophages as an early target ([PMID: 30297526](https://pubmed.ncbi.nlm.nih.gov/30297526/)).
- **Model type:** mammalian *in vivo* (genetic knockouts: *Prf1*, *Ifng*, *B2m*/MHC-I, *Myd88*, *Pycard*/ASC); plus *in vitro* infection of macrophage-like and microvascular endothelial cells.
- **Phenotype recapitulation:** The mouse model faithfully reproduces disseminated rickettsial infection, endothelial/macrophage targeting, and lethal severe disease, making it well suited to dissect protective immunity.
- **Limitations:** Mouse studies emphasize immunology and lethality; they do not reproduce the human eschar/rash phenotype in detail, and inbred knockouts do not capture human genetic diversity.

---

## Mechanistic Model (synthesis)

```
 Infected Ixodes tick bite
          │  inoculation of R. australis into dermis
          ▼
 [1] DERMAL MACROPHAGES  ── early replication niche ──►  ESCHAR (inoculation site)
          │  lymphatic + haematogenous spread
          ├────────────────────────────►  DRAINING LYMPH NODES ─► regional lymphadenopathy
          ▼
 [2] VASCULAR ENDOTHELIAL CELLS (systemic small vessels)
          │  cytosolic replication, endothelial injury
          ▼
 [3] RICKETTSIAL VASCULITIS
        ├─ perivascular infiltrate ─► maculopapular / vesicular RASH
        └─ ↑ vascular permeability ─► (severe) capillary leak, organ dysfunction

   HOST DEFENSE (determines outcome)
     TLR4 → MyD88 → NF-κB / ASC inflammasome → IFN-γ, IL-6, IL-1β, IL-12  (innate restraint)
                                   │
                                   ▼
     MHC-I-restricted, PERFORIN-dependent CD8+ CTL  ──►  kill infected macrophages/endothelium
                                   │                       (decisive clearance > IFN-γ)
        ┌──────────────────────────┴───────────────────────────┐
   controlled (mild, self-limited)                    outpaced (severe / fatal:
   + timely DOXYCYCLINE                                older age, delayed Rx)
```

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [1962102](https://pubmed.ncbi.nlm.nih.gov/1962102/) | *Spotted fever group rickettsial infections in Australia* | Etiology, vectors, geography, mild phenotype, serologic diagnosis, differentials |
| [22933759](https://pubmed.ncbi.nlm.nih.gov/22933759/) | *Genome sequence of R. australis* | 1.29-Mb genome, 2 plasmids, *R. akari* similarity, 1950 isolation |
| [11034486](https://pubmed.ncbi.nlm.nih.gov/11034486/) | *ompA/ompB of R. australis* | "Most divergent" SFG rickettsia; SFG classification |
| [11491333](https://pubmed.ncbi.nlm.nih.gov/11491333/) | *Phylogeny via gene D* | Places R. australis in the *R. akari* group |
| [9103608](https://pubmed.ncbi.nlm.nih.gov/9103608/) | *gltA citrate synthase phylogeny* | Confirms SFG/*R. akari*-group placement |
| [19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/) | *Host-cell interactions with pathogenic Rickettsia* | Endothelial tropism → "rickettsial vasculitis" core mechanism |
| [30297526](https://pubmed.ncbi.nlm.nih.gov/30297526/) | *Rickettsial macrophage tropism* | Macrophages as early target preceding endothelium |
| [32014896](https://pubmed.ncbi.nlm.nih.gov/32014896/) | *ASC inflammasome / TLR4 vs R. australis* | Innate immune control of R. australis |
| [26755162](https://pubmed.ncbi.nlm.nih.gov/26755162/) | *MyD88 in dendritic cells* | MyD88-dependent protective Th1 immunity; impaired clearance in KO |
| [11179362](https://pubmed.ncbi.nlm.nih.gov/11179362/) | *Cytotoxic T lymphocytes in rickettsial clearance* | CD8/perforin/MHC-I decisive, > IFN-γ |
| [31318873](https://pubmed.ncbi.nlm.nih.gov/31318873/) | *Rickettsial diseases in North Queensland* | Severity (8% severe SFG; 1 death), rising incidence |
| [32959771](https://pubmed.ncbi.nlm.nih.gov/32959771/) | *ICU case series (QTT + scrub typhus)* | 9 ICU QTT cases; APACHE II 13; presentation timing |
| [32252063](https://pubmed.ncbi.nlm.nih.gov/32252063/) | *Rickettsial infection in children* | Benign paediatric course |
| [33075531](https://pubmed.ncbi.nlm.nih.gov/33075531/) | *Prompt defervescence dogma* | 56% delayed defervescence; links to severity |
| [21642652](https://pubmed.ncbi.nlm.nih.gov/21642652/) | *Risk factors for malignant MSF* | Doxycycline protective; fluoroquinolones deleterious |
| [31587667](https://pubmed.ncbi.nlm.nih.gov/31587667/) | *Diagnosis of SFG rickettsioses* | qPCR + IFA in tandem |
| [22092999](https://pubmed.ncbi.nlm.nih.gov/22092999/) | *Real-time PCR for rickettsial diagnosis* | Validated R. australis qPCR; eschar/blood samples |
| [31268225](https://pubmed.ncbi.nlm.nih.gov/31268225/) | *Tasmanian rickettsial hotspots* | Incidence 0.6/100,000/yr, seasonality, older males |
| [25434042](https://pubmed.ncbi.nlm.nih.gov/25434042/) | *Ixodes holocyclus as vector* | I. holocyclus human-biting tick / paralysis |
| [16175900](https://pubmed.ncbi.nlm.nih.gov/16175900/) | *Not only 'Flinders Island' spotted fever* | R. honei differential across SE Australia |
| [10103185](https://pubmed.ncbi.nlm.nih.gov/10103185/) | *Doxycycline vs azithromycin vs trovafloxacin (canine RMSF)* | Comparative antibiotic efficacy |
| [18355299](https://pubmed.ncbi.nlm.nih.gov/18355299/) | *Ixodes ricinus bacterial communities* | R. australis DNA detected in European ticks |

---

## Limitations and Knowledge Gaps

1. **Mechanistic data are largely from mouse models.** The pivotal immunology (perforin/CD8 CTL dominance, MyD88, TLR4/ASC) derives from *R. australis* mouse experiments ([PMID: 11179362](https://pubmed.ncbi.nlm.nih.gov/11179362/); [PMID: 26755162](https://pubmed.ncbi.nlm.nih.gov/26755162/); [PMID: 32014896](https://pubmed.ncbi.nlm.nih.gov/32014896/)); human immunopathology is inferred, not directly measured.
2. **Endothelial-injury step is cross-group inference.** The "rickettsial vasculitis" mechanism is established for SFG rickettsiae broadly ([PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)) and applied to *R. australis*; species-specific human histopathology of QTT is sparsely quantified.
3. **Epidemiology conflates agents.** The best incidence figure (0.6/100,000/yr, Tasmania) largely reflects *R. honei* (Flinders Island spotted fever), not pure *R. australis* ([PMID: 31268225](https://pubmed.ncbi.nlm.nih.gov/31268225/); [PMID: 16175900](https://pubmed.ncbi.nlm.nih.gov/16175900/)). Mainland *R. australis* incidence is not precisely quantified.
4. **Treatment evidence borrows from MSF.** The strongest doxycycline-benefit / fluoroquinolone-harm data come from *R. conorii* MSF ([PMID: 21642652](https://pubmed.ncbi.nlm.nih.gov/21642652/)); no QTT-specific randomized trial exists.
5. **No human host-genetics data.** Whether human innate-immunity polymorphisms modulate QTT severity is unknown.
6. **No quality-of-life or long-term-outcome studies** specific to QTT.

---

## Proposed Follow-up Experiments / Actions

1. **Species-resolved surveillance:** Report *R. australis* versus *R. honei* separately in Australian notifiable-disease data to obtain a true QTT incidence and geographic map.
2. **Prospective QTT cohort** capturing eschar/blood qPCR positivity, IFA kinetics, defervescence time, severity predictors, and QoL (EQ-5D/SF-36) at 30/90 days.
3. **Human immunogenetics/immunophenotyping:** Test whether *TLR4*/*MYD88*/inflammasome/*PRF1* variants or peripheral CD8 CTL responses correlate with QTT severity, to validate the mouse-derived model in humans.
4. **Diagnostic optimization:** Define the sensitivity/timing window of eschar-swab qPCR versus blood qPCR versus paired IFA in prospectively enrolled QTT patients ([PMID: 31587667](https://pubmed.ncbi.nlm.nih.gov/31587667/); [PMID: 22092999](https://pubmed.ncbi.nlm.nih.gov/22092999/)).
5. **Treatment-timing study:** Quantify the effect of early empiric doxycycline on progression to severe QTT specifically (mirroring the MSF analysis), and formally test avoidance of fluoroquinolones.
6. **Vector/reservoir ecology & One Health mapping** of *I. holocyclus*/*I. tasmani* infection prevalence and reservoir hosts to guide targeted public-health messaging in expanding peri-urban endemic zones ([PMID: 31318873](https://pubmed.ncbi.nlm.nih.gov/31318873/)).

---

*Evidence-source key: Human clinical (case series/audits/serosurveys — PMIDs 1962102, 31318873, 32959771, 32252063, 33075531, 21642652, 31587667, 22092999, 16175900); Model organism (mouse — PMIDs 11179362, 26755162, 32014896, 30297526); Microbiology/genomics (PMIDs 22933759, 11034486, 11491333, 9103608); In vitro/vector (PMIDs 25434042, 18355299, 10103185).*


## Artifacts

- [OpenScientist final report](Queensland_Tick_Typhus-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Queensland_Tick_Typhus-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 21 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0000465` (1 mention) - the report calls it "Lymphatic system"; UBERON calls it **material anatomical entity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0200041` (1 mention) - the report calls it "Skin ulcer"; HP calls it **Skin erosion**
- `HP:0002910` (1 mention) - the report calls it "Elevated hepatic transaminase"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated transaminases" among its other names
- `GO:0050830` (1 mention) - the report calls it "defense response to Gram-negative bacterium"; GO calls it **defense response to Gram-positive bacterium**
- `CL:0000071` (2 mentions) - the report calls it "blood vessel endothelial cell", "Cell populations targeted:** vascular endothelial cells"; CL calls it **blood vessel endothelial cell**
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000071` - called "blood vessel endothelial cell", "Cell populations targeted:** vascular endothelial cells"