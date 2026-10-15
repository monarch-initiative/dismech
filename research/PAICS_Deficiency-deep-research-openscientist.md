---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T22:35:26.950884'
end_time: '2026-09-01T23:06:17.661596'
duration_seconds: 1850.71
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: PAICS Deficiency
  mondo_id: ''
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
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 60
  verified: 53
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 42
  labels_matching: 37
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: GO:0034023
    reported_labels:
    - "purinosome \u2014 as protein complex/assembly context"
    ontology_label: 5-(carboxyamino)imidazole ribonucleotide mutase activity
  - term_id: NCBITaxon:4932
    reported_labels:
    - "note: yeast splits the bifunctional activity \u2014 ADE1 = SAICAR synthetase,\
      \ ADE2 = AIR carboxylase"
    ontology_label: Saccharomyces cerevisiae
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  - GARD
  - NC_000004.12
  - MGI
  - RGD
  - SGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PAICS_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PAICS_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PAICS Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PAICS Deficiency** covering all of the
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

# PAICS Deficiency — Comprehensive Disease Characterization Report

*Category: Mendelian (autosomal recessive inborn error of de novo purine synthesis)*
*Report compiled 2026-09-02. Evidence source types: human clinical case reports, in vitro/enzymatic studies, structural biology, and comparison with allied de novo purine synthesis (DNPS) disorders.*

> **Caveat on evidence base:** PAICS deficiency is an *ultra-rare* Mendelian disorder. As of 2025 only **three molecularly confirmed patients** (plus one antenatally suspected sibling) have been reported worldwide, all homozygous for the same recurrent variant. Consequently, most disease-level statements rest on 1–3 individual patients (individual-patient/case-report evidence, not aggregated registry data). Where information is absent, this is stated explicitly. Many entries are extrapolated from the better-characterized allied DNPS defects (ADSL deficiency, AICA-ribosiduria/ATIC deficiency) and are flagged as such.

---

## 1. Disease Information

**Overview.** PAICS deficiency is an autosomal recessive **inborn error of de novo purine synthesis (DNPS)** caused by biallelic loss-of-function variants in the *PAICS* gene. *PAICS* encodes a bifunctional enzyme — **phosphoribosylaminoimidazole carboxylase (AIR carboxylase, AIRC; EC 4.1.1.21)** and **phosphoribosylaminoimidazole-succinocarboxamide synthetase (SAICAR synthetase, SAICARS; EC 6.3.2.6)** — that catalyzes the sixth and seventh of the ten sequential steps that convert PRPP to inosine monophosphate (IMP). Clinically the disorder manifests as a **multiple congenital malformation (polymalformative) syndrome**. The two index cases died in the early neonatal period; the third reported patient survived with a milder, non-lethal course and normal neurodevelopment, indicating a broader phenotypic spectrum than originally recognized (PMID 31600779; PMID 39726239).

**Key identifiers.**
- **Gene:** *PAICS* — HGNC:8587; NCBI Gene ID 10606; UniProt **P22234**; OMIM gene **172439**; Ensembl ENSG00000128050. Genomic locus **chr4:56,435,741–56,464,578 (GRCh38)**, cytoband **4q12** *(verified via gnomAD)*.
- **Disease (phenotype) — VERIFIED IDENTIFIERS:** **MONDO:0859003**; OMIM **#619859** ("Phosphoribosylaminoimidazole carboxylase deficiency"); **Orphanet ORPHA:633099**; **GARD:0026646** *(all confirmed via OLS4/Monarch and HPO/JAX APIs)*. ICD-10: no specific code (closest E79.8 "Other specified disorders of purine and pyrimidine metabolism"); ICD-11: closest 5C55.2 (inborn errors of purine or pyrimidine metabolism). MeSH: no dedicated descriptor; indexed under "Purine-Pyrimidine Metabolism, Inborn Errors."
- *Note: an earlier draft cited OMIM #618121; the correct phenotype MIM is **#619859**.*
- **EC numbers:** 4.1.1.21 (AIRC) and 6.3.2.6 (SAICARS).

**Synonyms / alternative names.**
- Phosphoribosylaminoimidazole carboxylase deficiency
- SAICAR synthetase deficiency / AIR carboxylase deficiency
- Multiple malformations syndrome, lethal, due to PAICS deficiency
- Inborn error of de novo purine synthesis, PAICS type

**Data provenance.** Disease-level knowledge is derived from **individual patient case reports** (n=3), supporting enzymatic/cell-biology experiments in patient fibroblasts and recombinant protein, and CRISPR HeLa models — *not* from EHR-scale or registry aggregation.

---

## 2. Etiology

**Primary cause (genetic).** Biallelic (homozygous, in a consanguineous/founder context) pathogenic variants in *PAICS*, producing a hypomorphic bifunctional enzyme. All reported patients carry the **homozygous missense variant NM_006452.4:c.158A>G, p.(Lys53Arg)**, which reduces catalytic activity (patient fibroblasts ~10% of control; recombinant enzyme ~25% of wild-type; carriers ~50%) (PMID 31600779).

**Genetic risk factors.**
- *Causal variant:* PAICS c.158A>G p.(Lys53Arg) — recurrent across all reported families.
- *Consanguinity / recurrent European allele:* the two index patients were from a consanguineous **Faroe Islands** family. The recurrent p.(Lys53Arg) allele (rs192831239) is a **low-frequency pan-European variant** (gnomAD NFE AF 0.135%), so its appearance in the unrelated French third case reflects the allele's general European frequency rather than a private founder. Consanguinity remains a strong risk factor for homozygosity, as for most recessive DNPS defects.
- *Modifier genes:* none identified; the marked phenotypic difference (lethal vs. surviving with normal cognition) among patients homozygous for the *same* variant implies the existence of unknown genetic and/or environmental modifiers (PMID 39726239).

**Environmental / lifestyle risk factors.** None established. As a Mendelian congenital disorder, environmental exposure is not a primary driver. (Not applicable / no evidence.)

**Protective factors.** None documented. Heterozygous carriers (~50% residual activity) are asymptomatic, indicating ~50% enzyme activity is sufficient (haplosufficiency), consistent with recessive inheritance.

**Gene–environment interactions.** No data. Speculatively, dietary purine intake or salvage-pathway flux could modulate severity (as purine salvage can partly compensate for DNPS defects), but this is untested in PAICS deficiency.

---

## 3. Phenotypes

Phenotype data derive from three patients. The two Faroese siblings (PMID 31600779) had a **lethal neonatal multiple-malformation** presentation; the third patient (PMID 39726239) had a **non-lethal polymalformative syndrome with normal neurodevelopment**, expanding the spectrum.

**Official curated HPO annotations with frequencies (from OMIM #619859 / HPO-JAX; frequencies reflect the 2 index siblings, n=2, unless noted).** These are the authoritative phenotype associations for knowledge-base ingestion:

| HPO term | Phenotype | System | Frequency |
|---|---|---|---|
| HP:0001561 | Polyhydramnios | prenatal | 2/2 |
| HP:0011461 | Fetal onset | clinical course | 2/2 |
| HP:0003811 | Neonatal death | clinical course | 2/2 |
| HP:0012368 | Flat face | craniofacial | 2/2 |
| HP:0000248 | Brachycephaly | craniofacial | 2/2 |
| HP:0003196 | Short nose | craniofacial | 2/2 |
| HP:0005280 | Depressed nasal bridge | craniofacial | 2/2 |
| HP:0000470 | Short neck | head/neck | 2/2 |
| HP:0000369 | Low-set ears | ear | 2/2 |
| HP:0002032 | Esophageal atresia | digestive/foregut | 2/2 |
| HP:0002575 | Tracheoesophageal fistula | digestive/foregut | 1/2 |
| HP:0000453 / HP:0000452 / HP:0004502 | Choanal atresia / stenosis / bilateral choanal atresia | head/neck | 1/2 |
| HP:0000463 | Anteverted nares | craniofacial | 1/2 |
| HP:0000316 | Hypertelorism | eye | 1/2 |
| HP:0004322 | Short stature | growth | 1/2 |
| HP:0001762 | Talipes equinovarus | limbs | 1/2 |
| HP:0004209 | Clinodactyly of the 5th finger | limbs | 1/2 |
| HP:0000921 | Missing ribs | skeletal | 1/2 |
| HP:0008439 | Lumbar hemivertebrae | skeletal | 1/2 |
| HP:0008743 | Coronal hypospadias | genitourinary | 1/1 (male) |
| HP:0008689 | Bilateral cryptorchidism | genitourinary | 1/1 (male) |
| HP:0000007 | Autosomal recessive inheritance | inheritance | — |

**Additional features from the third (surviving) patient (PMID 39726239), not in the OMIM/HPO n=2 curation:** congenital heart defect/cardiopathy (HP:0001627, newly described), plus **preserved/normal neurodevelopment** (distinguishing feature). The MONDO/OMIM narrative also lists nasal hypoplasia and lung malformations.

**Phenotype characteristics.**
- *Age of onset:* congenital/neonatal (prenatal in the antenatally diagnosed sibling).
- *Severity:* **variable** — lethal neonatal to survivable childhood form.
- *Progression:* congenital and largely static (malformations fixed); the survivor showed normal neurodevelopmental trajectory.
- *Frequency among affected:* with n=3, "frequencies" are indicative only — skeletal and oesophageal defects appear consistent (reported as a recurring theme); congenital heart disease in 1/3; early death in 2/3.

**Quality-of-life impact.** In the lethal form, QoL is dominated by neonatal demise. In the survivor, impact relates to surgical correction of malformations (cardiac, oesophageal, skeletal) with preserved cognition — a comparatively favourable functional outlook (PMID 39726239). No formal EQ-5D/SF-36/PROMIS data exist.

*Note:* Allied DNPS disorders (ADSL, ATIC) are dominated by **neurological** features (psychomotor retardation, epilepsy, autistic features, visual impairment) (PMID 25112391; PMID 32557644). Notably, PAICS deficiency in the survivor spared the CNS, distinguishing it phenotypically.

---

## 4. Genetic / Molecular Information

**Causal gene.** *PAICS* (HGNC:8587; OMIM 172439; Gene ID 10606; UniProt P22234), chromosome **4q12**. Encodes a **425-aa bifunctional polypeptide** that assembles into a homo-octamer (PMID 17224163).

**Pathogenic variant(s).**
- **NM_006452.4:c.158A>G, p.(Lys53Arg)** (= NM_001079524.2:c.158A>G) — missense; homozygous in all reported patients. **ClinVar: Likely pathogenic** (review status "criteria provided, multiple submitters, no conflicts", verified via NCBI eutils). Affects the structure of the enzyme's catalytic site (PMID 31600779).
- *PAICS* has **81 ClinVar entries**, overwhelmingly **VUS**; besides p.Lys53Arg, a truncating variant **c.843_844del (p.Cys281_Glu282delinsTer)** is also listed as Likely pathogenic (no published clinical report identified) — indicating additional candidate pathogenic alleles may exist beyond the recurrent founder missense.
- Variant type/class: **missense** (single-nucleotide substitution).
- Functional consequence: **loss of function (hypomorph)** — residual ~10–25% activity; reduces flux through both AIRC and SAICARS reactions; abolishes purinosome assembly.
- **Allele frequency (gnomAD v4, verified):** dbSNP **rs192831239**; SPDI NC_000004.12:56441803:A:G (**GRCh38 chr4:56,441,804 A>G**); OMIM allelic variant 172439.0001; ClinGen CA2930671. Exome **AC 1675 / AN 1,448,934, AF 0.116%**, **0 homozygotes**; genome AF 0.072%, 0 homozygotes. Ancestry: highest in **non-Finnish European (0.135%)**, then South Asian (0.079%), Admixed American (0.070%), Finnish (0.025%), African (0.018%); absent in Ashkenazi Jewish, East Asian, Middle Eastern. → The allele is a **recurrent low-frequency pan-European variant, NOT a private Faroese founder mutation**; the complete absence of homozygotes (despite carrier frequency ~1/370–1/740 in Europeans) is consistent with recessive prenatal/neonatal lethality removing homozygotes from population databases (and possible under-ascertainment/reduced penetrance).
- Somatic vs. germline: **germline** (congenital, biallelic).

**gnomAD gene-level constraint (verified).** *PAICS* is **not** loss-of-function-intolerant: **pLI ≈ 0** (5.8×10⁻⁷), **LOEUF 0.82** (oe_lof 0.61; observed/expected LoF 33/53.7), missense z = 1.92 (mild constraint). This lack of haploinsufficiency is fully consistent with **autosomal recessive** inheritance — a single functional allele suffices (heterozygotes are asymptomatic with ~50% activity).

**ACMG considerations.** p.(Lys53Arg) is classified **Likely pathogenic in ClinVar** (multiple submitters, no conflicts). Supporting criteria: strong functional evidence (PS3 — measured reduced enzyme activity and abolished purinosome assembly, rescued by wild-type PAICS), rarity (PM2), and recurrence across unrelated families. Beyond this founder missense, most *PAICS* ClinVar entries are VUS, with one additional Likely-pathogenic truncating allele (c.843_844del).

**Modifier genes.** None identified; presence strongly inferred from intra-genotype phenotypic variability (lethal vs. surviving).

**Epigenetic information.** No disease-specific methylation/chromatin data for PAICS deficiency. (In cancer biology, *PAICS* is subject to m6A-mediated and H3K9me3/HP1α-linked regulation of the ASB11 axis controlling purinosome assembly — PMID 37848033, PMID 42493545 — but this is oncologic, not germline-disease, context.)

**Chromosomal abnormalities.** None; PAICS deficiency is a single-gene point-mutation disorder. (In cancers, chromosome-4q loss reduces PAICS expression — PMID 33596246 — unrelated to the Mendelian disease.)

---

## 5. Environmental Information

- **Environmental factors / toxins / radiation:** none implicated. (Not applicable.)
- **Lifestyle factors:** none implicated; congenital genetic disorder.
- **Infectious agents:** none; not an infectious/triggered disease.

The only "environmental" dimension of theoretical relevance is dietary purine availability and salvage-pathway substrate supply, which could in principle modulate a DNPS defect, but no evidence exists in PAICS deficiency.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Homozygous PAICS c.158A>G (p.Lys53Arg)** alters the catalytic-site structure of the bifunctional AIRC/SAICARS enzyme → **leads to** reduced catalytic activity (~10–25% residual) [demonstrated: enzyme assays, PMID 31600779].
2. Reduced PAICS activity **results in** a block at steps 6–7 of de novo purine synthesis (AIR → CAIR → SAICAR) → impaired conversion toward IMP [demonstrated biochemically in DNPS defects; PMID 35323684].
3. The mutant PAICS **fails to nucleate the purinosome** (the multi-enzyme DNPS metabolon); purinosome assembly is abolished and is rescued only by wild-type PAICS [demonstrated in patient fibroblasts, PMID 31600779; PAICS is a hub of purinosome protein–protein interactions, PMID 35331738].
4. Loss of channeled DNPS **leads to** two downstream, non-exclusive insults:
   - **(4a) Purine nucleotide insufficiency** → reduced supply of AMP/GMP/ATP/GTP for nucleic-acid synthesis and energy/signaling → impaired proliferation during rapid embryonic morphogenesis → **congenital malformations** [inferred].
   - **(4b) Accumulation of upstream intermediates** (predicted AIR/CAIR; their dephosphorylated ribosides, e.g., AIr) → **cytotoxicity** (AIr shown cytotoxic to multiple cell lines) → cell death/dysmorphogenesis [partly demonstrated: AIr toxicity, PMID 31600779; analogous to SAICAr/S-Ado toxicity in ADSL and AICA-riboside toxicity in ATIC deficiency, PMID 25112391, PMID 32557644].
5. Tissue-level consequences during organogenesis **result in** structural defects of the **skeleton, oesophagus (foregut), and heart**, plus growth restriction and dysmorphism → the **polymalformative syndrome**; where the insult is severe, **early neonatal death** [observed, PMID 31600779; PMID 39726239].
6. **Branch point:** with only partial enzyme loss and/or protective modifiers, purine supply may be sufficient postnatally to permit **survival with normal neurodevelopment** (third patient) — the CNS may be relatively spared compared with ADSL/ATIC defects [observed, PMID 39726239; mechanism of sparing inferred].

**Molecular pathways.** De novo purine biosynthesis (KEGG hsa00230 purine metabolism; Reactome "Purine ribonucleoside monophosphate biosynthesis"). PAICS catalyzes: AIR + CO₂ → CAIR (AIRC, EC 4.1.1.21) and CAIR + L-aspartate + ATP → SAICAR (SAICARS, EC 6.3.2.6).

**Cellular processes.** Metabolon (purinosome) assembly/phase separation; nucleotide biosynthesis; cell proliferation; apoptosis (from intermediate cytotoxicity). GO suggestions: GO:0006189 ('de novo' IMP biosynthetic process), GO:0009152 (purine ribonucleotide biosynthetic process), GO:0034023 (purinosome — as protein complex/assembly context), GO:0004638 (phosphoribosylaminoimidazole carboxylase activity), GO:0004639 (phosphoribosylaminoimidazolesuccinocarboxamide synthase activity).

**Protein dysfunction.** p.Lys53Arg is a loss-of-function/hypomorphic substitution distorting the catalytic site; the enzyme normally functions only as an **octamer** with substrate-channeling tunnels between AIRC and SAICARS active sites (PMID 17224163; PMID 32571877; reaction mechanism, PMID 35914774). Loss of activity + loss of purinosome-nucleating protein–protein interactions (PMID 35331738). **Experimental structures (RCSB PDB):** 2H31 (octameric apo structure, PMID 17224163), 6YB8 / 6YB9 (substrate/product complexes, PMID 32571877), 7ALE; UniProt **P22234**; AlphaFold model **AF-P22234-F1**. Residue Lys53 lies in the AIR-carboxylase domain near the catalytic site.

**Metabolic changes.** Amino-acid/nucleotide metabolism: reduced IMP→AMP/GMP; predicted accumulation of AIR/CAIR/ SAICAR and their ribosides (CHEBI: aminoimidazole ribotide/AIR; SAICAR). Metabolomic profiling of DNPS-deficient HeLa cells shows accumulation of intermediates immediately upstream of the deficient enzyme (PMID 35323684).

**Immune involvement.** None described (not an immunologic disease).

**Tissue-damage mechanisms.** Cytotoxicity of accumulated dephosphorylated intermediates; nucleotide starvation of proliferating cells.

**Molecular profiling.** CRISPR-Cas9 PAICS-knockout/deficient HeLa cells provide targeted + untargeted metabolomic signatures of the DNPS block (PMID 35323684, PMID 35331738). No patient transcriptomic/proteomic/metabolomic datasets published beyond fibroblast enzymology.

**Cell types & GO/CL suggestions.** Fibroblasts used experimentally (CL:0000057). In vivo affected cell populations are rapidly proliferating embryonic progenitors of skeletal (CL:0000062 osteoblast; CL:0000138 chondrocyte), cardiac (CL:0000746 cardiac muscle cell), and foregut/oesophageal epithelium (CL:0000066 epithelial cell) — inferred from malformation pattern.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** skeleton (UBERON:0001434 skeletal system), oesophagus (UBERON:0001043), heart (UBERON:0000948). Growth (whole-body/UBERON multi-organ). **Secondary:** consequences of malformations (e.g., feeding/airway from oesophageal defects; circulatory from cardiac defects).

**Body systems:** musculoskeletal, digestive (foregut), cardiovascular; generalized growth. CNS **relatively spared** in the survivor (contrast with allied DNPS disorders that are CNS-dominant).

**Tissue/cell level:** connective/skeletal tissue (cartilage, bone), cardiac muscle, gut epithelium. CL terms as above.

**Subcellular level:** the purinosome is a **mitochondria-associated** cytoplasmic metabolon (PMID 35331738). GO cellular-component suggestions: GO:0005829 (cytosol), mitochondrial outer-membrane association; the purinosome itself is a dynamic, membraneless (phase-separated) body (PMID 37848033).

**Localization / lateralization:** malformations are congenital and can be midline/bilateral (skeletal, cardiac, oesophageal); no consistent lateralization reported (n too small).

---

## 8. Temporal Development

- **Onset:** congenital; detectable **antenatally** (a suspected sibling recurrence was diagnosed prenatally, PMID 39726239). Onset pattern: **chronic/congenital** (present from organogenesis).
- **Progression / course:** malformations are structurally fixed. In the lethal form, course is **acute neonatal deterioration → death within days** (PMID 31600779). In the surviving form, course is **stable** post-surgical correction with normal developmental trajectory to at least 7 years (PMID 39726239).
- **Disease duration:** lethal (self-limited by neonatal death) vs. chronic/lifelong in survivors.
- **Critical periods:** first-trimester organogenesis is the window of vulnerability (skeletal/foregut/cardiac morphogenesis). Prenatal detection offers a window for counseling; no fetal/neonatal metabolic intervention is established.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (biallelic *PAICS* variants; heterozygous parents asymptomatic).
- **Epidemiology:** ultra-rare; **prevalence/incidence unknown** (<1/1,000,000; only 3 reported cases). No registry data.
- **Penetrance:** appears complete for the malformation phenotype in homozygotes, but **expressivity is highly variable** (lethal neonatal vs. surviving with normal cognition) despite the identical genotype (PMID 39726239).
- **Expressivity:** variable (see above).
- **Genetic anticipation:** not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** not reported.
- **Founder effect / consanguinity (revised via gnomAD):** the recurrent p.(Lys53Arg)/rs192831239 allele is **not a private Faroese founder** but a **recurrent low-frequency pan-European variant** (gnomAD exome AF 0.116%; highest in non-Finnish Europeans, 0.135%). Its recurrence in an unrelated French patient is therefore expected. The index family was consanguineous (Faroe Islands), which brought two copies together; consanguinity remains a risk factor for homozygosity of this and other recessive alleles.
- **Carrier frequency (verified):** ~**1/370–1/740 in Europeans** (2×AF ≈ 0.23–0.27% NFE); rarer in African, absent in Ashkenazi/East Asian/Middle Eastern gnomAD samples. Notably **zero homozygotes** are observed in ~1.45 million gnomAD alleles, despite an expected homozygote birth frequency on the order of ~1/550,000 (NFE) — consistent with recessive prenatal/neonatal lethality (affected individuals excluded from gnomAD) and/or reduced penetrance; implies the disorder is likely **under-ascertained** (unrecognized fetal losses/neonatal deaths).
- **Population demographics / geography:** first cases Faroe Islands; third case reported from a European (French) centre — consistent with the allele's European distribution. No sex predilection evident (both sexes affected; third patient male). Age distribution: prenatal-to-childhood onset.

---

## 10. Diagnostics

**Diagnostic approach.** Because DNPS-intermediate biomarkers may be **undetectable** (AIR/AIr were not found in patient fibroblasts, PMID 31600779), diagnosis is primarily **molecular/genomic**.

- **Genetic testing (primary):** **whole-genome sequencing (WGS)** established the diagnosis in the third patient; **whole-exome sequencing (WES)** is equally appropriate; single-gene *PAICS* testing/targeted analysis of c.158A>G is useful where the founder allele is suspected. Purine-metabolism/inborn-error gene panels including *PAICS* are appropriate (GTR).
- **Biochemical/laboratory:** urine/plasma/CSF purine metabolite profiling (HPLC-MS) as used for ADSL (SAICAr, S-Ado) and ATIC (AICA-riboside) — but note **classic accumulating markers may be absent** in PAICS deficiency, limiting biochemical screening (PMID 31600779). Enzyme activity assay in cultured skin fibroblasts (reduced to ~10%) is confirmatory (LOINC/enzyme assay).
- **Functional/cellular:** purinosome-assembly assay in fibroblasts (absent, rescued by WT PAICS) — a research-grade functional confirmation.
- **Imaging:** prenatal/postnatal imaging (fetal ultrasound, echocardiography, skeletal survey, contrast oesophagram) to delineate malformations. RadLex terms as appropriate.
- **Histopathology:** no pathognomonic biopsy finding described.

**Clinical criteria / differential diagnosis.** No formal criteria. Differential includes other **DNPS defects** (ADSL deficiency, AICA-ribosiduria/ATIC, ADSS/ADSS1/2, ATIC, PRPS abnormalities) — distinguished by their **CNS-dominant** presentation and specific accumulating metabolites; also other polymalformative/VACTERL-spectrum syndromes (given vertebral, cardiac, oesophageal involvement) and chromosomal disorders (excluded by CMA/karyotype/sequencing).

**Screening.** Carrier/cascade testing for the familial p.(Lys53Arg) variant; prenatal molecular testing feasible (used in the suspected sibling). Not part of routine newborn screening.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** in the index family, **2/2 siblings died in the early neonatal period** (PMID 31600779). The third patient **survived to at least 7 years** with normal neurodevelopment (PMID 39726239). Thus prognosis is **bimodal/variable**, ranging from neonatal-lethal to survivable childhood disease.
- **Morbidity/function:** in survivors, morbidity is driven by structural malformations requiring surgical correction (cardiac, oesophageal, skeletal); **cognition may be preserved**, an important prognostic distinction from ADSL/ATIC deficiencies.
- **Complications:** those of congenital heart disease, oesophageal malformation (feeding/respiratory), and skeletal anomalies.
- **Prognostic factors:** severity/number of malformations and (inferred) residual enzyme function/modifiers determine lethality. The 2025 report explicitly **updated prognosis to include the possibility of survival with normal neurodevelopment** (PMID 39726239).
- **QoL measures:** none formally applied.

---

## 12. Treatment

**No disease-specific/curative therapy exists.** Management is **supportive and symptomatic** (NCIT: Supportive Care Therapy; NCIT:C15277 Supportive Care).

- **Pharmacotherapy:** none targeted; there is no established purine-replacement therapy for PAICS deficiency. (Theoretical strategies — dietary/purine salvage support, avoidance of intermediate accumulation — are unproven.)
- **Surgical/interventional:** correction of congenital malformations (cardiac surgery, oesophageal repair, orthopedic management) in survivors (NCIT clinical-intervention terms as applicable, e.g., Cardiac Surgery, Esophageal repair).
- **Supportive/rehabilitative:** neonatal intensive care; nutritional support; multidisciplinary follow-up.
- **Advanced/experimental therapeutics:** none in trials for PAICS deficiency. Gene therapy, enzyme replacement, or substrate-modulation approaches are conceptual only. *(Note: PAICS is being pursued as an oncology drug **target** — inhibitors to reduce purine synthesis in cancer — PMID 37673296, PMID 34344987 — the opposite therapeutic direction from this deficiency.)*
- **Pharmacogenomics:** not applicable.
- **Treatment outcomes / adverse events:** determined by surgical/critical-care outcomes; no drug outcome data.

---

## 13. Prevention

- **Primary prevention:** **genetic counseling** for consanguineous families and known carriers; **carrier/cascade screening** for the familial p.(Lys53Arg) allele; reproductive options including **preimplantation genetic testing (PGT)** and **prenatal molecular diagnosis** (feasible, as demonstrated antenatally in the suspected sibling, PMID 39726239).
- **Secondary prevention:** prenatal imaging + molecular testing enables early detection and delivery planning; early surgical correction of malformations in survivors.
- **Tertiary prevention:** management of complications of congenital malformations.
- **Immunization / public-health / environmental interventions:** not applicable (Mendelian disorder).
- **Counseling:** recurrence risk 25% per pregnancy for carrier couples (autosomal recessive); NSGC/ACMG genetic-counseling frameworks apply.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs (verified via Alliance of Genome Resources, stringent):** *PAICS* is deeply conserved across metazoa and fungi. One-to-one/many orthologs:
  - Mouse *Paics* — MGI:1914304; NCBI Gene 67054; NCBITaxon:10090
  - Rat *Paics* — RGD:620066; NCBITaxon:10116
  - Zebrafish *paics* — ZFIN:ZDB-GENE-030131-9762; NCBITaxon:7955
  - *Drosophila melanogaster* *Paics* — FB:FBgn0020513; NCBITaxon:7227
  - *Caenorhabditis elegans* *paic-1* — WB:WBGene00015116; NCBITaxon:6239
  - *Saccharomyces cerevisiae* *ADE1* — SGD:S000000070; NCBITaxon:4932 (note: yeast splits the bifunctional activity — ADE1 = SAICAR synthetase, ADE2 = AIR carboxylase)
  - *Xenopus tropicalis/laevis* *paics* — Xenbase
  - Bacterial functional homologs: PurC/PurE/PurK. DNPS is among the most conserved biosynthetic pathways.
- **Natural disease in other species:** no naturally occurring PAICS-deficiency disease is catalogued in OMIA for companion animals/livestock (none found — *verify*).
- **Comparative biology:** the octameric bifunctional vertebrate PAICS contrasts with separate monofunctional bacterial/yeast enzymes; substrate channeling and purinosome assembly are conserved features studied to understand human disease.
- **Zoonotic/cross-species transmission:** not applicable (genetic, non-transmissible).

---

## 15. Model Organisms

- **Cellular / in vitro models (principal):** **CRISPR-Cas9 PAICS-knockout / deficient HeLa cells** used for targeted + untargeted metabolomic profiling of the DNPS block (PMID 35323684) and for dissecting purinosome protein–protein interactions and metabolic channeling (crPAICS cells, PMID 35331738). **Patient skin fibroblasts** (primary) recapitulate reduced enzyme activity and absent purinosome assembly, rescued by wild-type PAICS transfection (PMID 31600779).
- **Recombinant enzyme:** E. coli-expressed wild-type and p.Lys53Arg PAICS for kinetic characterization (PMID 31600779); human PAICS crystal structures for mechanistic/structural study (PMID 17224163, PMID 32571877, PMID 35914774).
- **Genetic model types available:** knockout/knockdown cell lines (CRISPR, shRNA — the latter widely used in cancer studies, e.g., AML, PMID 34344987).
- **Mouse *Paics* knockout (IMPC, verified via IMPC solr):** homozygous null mice show **"preweaning lethality, complete penetrance"** and **"prenatal lethality prior to heart atrial septation"** (homozygote, complete penetrance) — i.e., *Paics* is an **essential gene** and complete loss is embryonically/prenatally lethal. No viable homozygous-null adults. Suggested MP terms: MP:0011100 (preweaning lethality, complete penetrance), prenatal-lethality MP terms. This is mechanistically important: it explains why **human patients carry a hypomorphic missense** (p.Lys53Arg, ~10–25% residual activity) rather than biallelic nulls, and the "prenatal lethality prior to heart atrial septation" parallels the **congenital cardiac defect** in the surviving human patient (PMID 39726239).
- **Phenotype recapitulation:** cell models reproduce the biochemical/purinosome defect well; the mouse null recapitulates lethality/essentiality but (being a complete null) does not model the *hypomorphic* human malformation syndrome. **Limitation:** no published hypomorphic/knock-in *Paics* animal model (e.g., p.Lys53Arg knock-in) recapitulating the human polymalformative phenotype exists (*gap / future direction*).
- **Resources:** Cellosaurus (HeLa derivatives), MGI/IMPC (mouse *Paics*), ZFIN (zebrafish *paics*) for reagents.

---

## Key Ontology Term Suggestions (summary)

- **Gene/protein:** *PAICS* (HGNC:8587, UniProt P22234); GO:0004638, GO:0004639, GO:0006189, GO:0009152.
- **Phenotypes (HPO):** HP:0002011/HP:0001263 (malformation), HP:0003811 (neonatal death), HP:0002032 (esophageal atresia), HP:0001627 (abnormal heart morphology), HP:0000924 (skeletal abnormality), HP:0001999 (facial dysmorphism), HP:0001511 (IUGR).
- **Cell types (CL):** CL:0000057 (fibroblast), CL:0000062 (osteoblast), CL:0000138 (chondrocyte), CL:0000746 (cardiomyocyte), CL:0000066 (epithelial cell).
- **Anatomy (UBERON):** UBERON:0001434 (skeletal system), UBERON:0001043 (esophagus), UBERON:0000948 (heart).
- **Chemicals (CHEBI):** AIR/aminoimidazole ribotide, CAIR, SAICAR, IMP; substrate CO₂, L-aspartate, ATP.
- **Disease (MONDO/OMIM):** **MONDO:0859003**; OMIM **#619859**; **Orphanet ORPHA:633099**; **GARD:0026646** (all verified).
- **Treatment (NCIT):** supportive care; surgical repair of congenital anomalies.

---

## Supported vs. Refuted Statements

**Supported (evidence-based):**
- PAICS deficiency is AR, caused by biallelic *PAICS* p.(Lys53Arg); loss-of-function reduces enzyme activity and abolishes purinosome assembly (PMID 31600779). *(Strong: enzymatic + cellular rescue.)*
- Phenotype = congenital multiple-malformation syndrome; spectrum spans neonatal-lethal to survivable-with-normal-cognition (PMID 31600779, PMID 39726239). *(Moderate: n=3.)*
- Accumulating intermediate ribosides (AIr) are cytotoxic; analogous to other DNPS defects (PMID 31600779; PMID 25112391; PMID 32557644). *(Moderate.)*

**Refuted / not supported:**
- That classic urinary DNPS metabolite markers reliably diagnose PAICS deficiency — **refuted**: predicted markers were undetectable in patient fibroblasts; molecular testing is required (PMID 31600779).
- That PAICS deficiency is uniformly CNS-degenerative like ADSL/ATIC — **not supported**: the survivor had normal neurodevelopment (PMID 39726239).

## Limitations & Future Directions

- Evidence rests on **3 patients** with the **same variant**; genotype–phenotype breadth, penetrance, carrier frequency, and epidemiology are essentially unknown.
- No validated whole-animal disease model; mechanism of malformation (nucleotide starvation vs. intermediate toxicity) not fully resolved for organogenesis.
- Priorities: identify additional patients/variants; establish biomarker(s); build animal models; test whether purine-salvage support alters outcome; clarify modifiers explaining lethal-vs-survivable divergence.

---

*Prepared for disease knowledge-base population. Verified against primary databases: disease identifiers (MONDO:0859003, OMIM #619859, ORPHA:633099, GARD:0026646) via OLS4/Monarch; HPO annotations via HPO-JAX; variant classification (ClinVar VCV001686821, Likely pathogenic) and coordinates (rs192831239, chr4:56,441,804 GRCh38) via NCBI eutils; allele frequency (gnomAD v4 exome AF 0.116%, 0 homozygotes) and gene constraint via gnomAD API; orthologs via Alliance of Genome Resources; mouse-knockout lethality via IMPC; PDB structures via RCSB. Remaining items to confirm before ingestion: exact OMIA status (no natural animal disease found), and any newer case reports post-2025.*


## Artifacts

- [OpenScientist final report](PAICS_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PAICS_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 42 |
| Terms named correctly | 37 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0034023` (1 mention) - the report calls it "purinosome — as protein complex/assembly context"; GO calls it **5-(carboxyamino)imidazole ribonucleotide mutase activity**
- `NCBITaxon:4932` (1 mention) - the report calls it "note: yeast splits the bifunctional activity — ADE1 = SAICAR synthetase, ADE2 = AIR carboxylase"; NCBITaxon calls it **Saccharomyces cerevisiae**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000746` (2 mentions) - the report calls it "cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names
- `HP:0001263` (1 mention) - the report calls it "malformation"; HP calls it **Global developmental delay**, and lists "Motormental retardation" among its other names
- `HP:0000924` (1 mention) - the report calls it "skeletal abnormality"; HP calls it **Abnormality of the skeletal system**, and lists "Skeletal abnormalities" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003811` - called "Neonatal death", "neonatal death"
- `HP:0002032` - called "Esophageal atresia", "esophageal atresia"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `GARD`, `NC_000004.12`, `MGI`, `RGD`, `SGD`.
