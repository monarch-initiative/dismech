---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T20:50:05.166321'
end_time: '2026-10-14T21:31:44.522948'
duration_seconds: 2499.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Gordon Syndrome
  mondo_id: MONDO:0007252
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
citation_count: 18
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 12
  validator_version: 0.3.0
term_validation:
  total_terms: 23
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 5
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0007252
    reported_labels:
    - MONDO
    ontology_label: Gordon syndrome
  - term_id: GO:0005886
    reported_labels:
    - GO cellular component:** plasma membrane
    - Subcellular level:** Plasma membrane mechanosensitive channel
    ontology_label: plasma membrane
  labels_variant: 5
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
  path: Gordon_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Gordon_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gordon Syndrome
- **MONDO ID:** MONDO:0007252 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gordon Syndrome** covering all of the
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

# Gordon Syndrome (Distal Arthrogryposis Type 3): A Comprehensive Disease Characteristics Report

**Disease:** Gordon Syndrome (Distal Arthrogryposis type 3, DA3)
**MONDO ID:** MONDO:0007252 · **OMIM:** #114300 · **Category:** Mendelian (monogenic, autosomal dominant)
**Causal gene:** *PIEZO2* (HGNC:26270) · **Report date:** 2026-10-14 · Evidence base: 32 papers reviewed, 7 confirmed findings.

---

## Summary

Gordon Syndrome (GS), also called distal arthrogryposis type 3 (DA3), is a rare autosomal-dominant congenital contracture disorder. Its defining clinical triad is **camptodactyly** (permanently flexed fingers), **talipes equinovarus** (clubfoot), and **cleft palate**, usually accompanied by short stature and frequently by ptosis and a distinctive facies. GS is distinguished from the broader distal arthrogryposis family chiefly by the presence of cleft palate and short stature. The disease is caused by **heterozygous gain-of-function (GoF) missense variants in *PIEZO2*** (18p11.22), the gene encoding the principal mechanically activated cation channel for proprioception and touch. A single recurrent variant, **c.8057G>A / p.Arg2686His**, accounts for the majority of molecularly confirmed families and is statistically associated with the cleft-palate phenotype that defines GS.

Mechanistically, GS is a **channelopathy of mechanotransduction**. The GoF variants, concentrated in the C-terminal pore/inactivation module of PIEZO2, alter channel inactivation kinetics so that the channel carries excess mechanically activated current. In proprioceptive sensory neurons that innervate muscle spindles and tendons, this excessive mechanotransduction during fetal/postnatal development produces **neurogenic joint contractures**. This causal chain is directly demonstrated in mice: expressing a GoF *Piezo2* allele selectively in proprioceptors is sufficient to reproduce distal-arthrogryposis-like contractures, and the deficits are mitigated by botulinum toxin and by a PIEZO2-modulating dietary fatty acid. GS sits at one end of a **continuous dominant PIEZO2 clinical spectrum** that also includes distal arthrogryposis type 5 (DA5) and Marden-Walker syndrome (MWS); the same variant can produce different points on this spectrum, reflecting marked allelic heterogeneity and variable expressivity.

This report synthesizes evidence from exome-sequencing cohorts, biophysical electrophysiology, mouse and *C. elegans* models, and clinical case series to populate all 15 requested knowledge-base sections. Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, published cohorts) rather than EHR-level individual-patient data. Where evidence is absent or not applicable (e.g., infectious agents, somatic variants, cancer survival statistics), this is stated explicitly.

---

## Key Findings

### Finding 1 — *PIEZO2* is the causal gene; recurrent p.Arg2686His defines Gordon Syndrome

Exome sequencing of five GS-affected families identified *PIEZO2* mutations in every family, establishing *PIEZO2* as the causal gene for Gordon syndrome ([PMID: 24726473](https://pubmed.ncbi.nlm.nih.gov/24726473/)). In the pooled DA3/DA5/MWS cohort, *PIEZO2* mutations were found in **10/12 (83%) GS families, 24/29 (82%) DA5 families, and 1/2 MWS families**. Nine GS families carried the **identical c.8057G>A (p.Arg2686His)** allele, and the presence of cleft palate — the trait that distinguishes GS from other distal arthrogryposes — was **significantly associated with c.8057G>A (Fisher's exact test, adjusted p < 0.0001)**. The study states: *"Exome sequencing of five GS-affected families identified mutations in piezo-type mechanosensitive ion channel component 2 (PIEZO2) in each family"* and *"The presence of cleft palate was significantly associated with c.8057G>A (Fisher's exact test, adjusted p value < 0.0001)."* This firmly links a specific recurrent allele to the GS phenotype.

### Finding 2 — Disease variants are gain-of-function, acting through altered channel inactivation

Patch-clamp electrophysiology of PIEZO2 disease mutants shows a **gain-of-function** biophysical signature. Both the E2727del and I802F mutations cause the PIEZO2-dependent mechanically activated currents to **recover faster from inactivation**, and E2727del additionally **slows inactivation** — net effect, more channel activity for a given mechanical stimulus ([PMID: 23487782](https://pubmed.ncbi.nlm.nih.gov/23487782/)): *"both E2727del and I802F mutations cause the PIEZO2-dependent, mechanically activated currents to recover faster from inactivation, while E2727del also causes a slowing of inactivation."* Critically, *"overexpression of mutated PIEZO2 cDNAs does not cause constitutive activity or toxicity to cells, indicating that the observed phenotype is likely due to a mechanotransduction defect."* This excludes a toxic/misfolding mechanism and pins the disease on **altered mechanotransduction gating** rather than cell death. A bioinformatics survey ([PMID: 30988732](https://pubmed.ncbi.nlm.nih.gov/30988732/)) corroborates that dominant mutations cluster in the C-terminal region and that GoF variants increase PIEZO2 channel activity, while recessive loss-of-function variants cluster N-terminally.

### Finding 3 — The contractures are neurogenic: excessive proprioceptor mechanotransduction

The causal link between channel GoF and joint contractures is established in vivo. Expressing a gain-of-function *Piezo2* mutation **specifically in proprioceptive sensory neurons** that innervate muscle spindles and tendons is **sufficient to induce DA5-like contractures in mice**, via increased peripheral nervous-system activity during postnatal development ([PMID: 36634173](https://pubmed.ncbi.nlm.nih.gov/36634173/)): *"expression of a gain-of-function PIEZO2 mutation in proprioceptive sensory neurons that mainly innervate muscle spindles and tendons is sufficient to induce DA5-like phenotypes in mice."* Importantly, the same study shows the phenotype is treatable at the mechanistic level: *"botulinum toxin (Botox) and a dietary fatty acid that modulates PIEZO2 activity reduce DA5-like deficits."* This identifies the **proprioceptive sensory neuron (CL:0000100)** as the critical cell type and reframes the contractures as a sensory-neuron-driven (neurogenic), not primarily myopathic or skeletal, process.

### Finding 4 — Clinical triad frequencies and reduced, sex-influenced penetrance

Clinical cohort data quantify the core phenotype. Gordon's syndrome presents with short stature, stiff spine, **camptodactyly (89%), cleft palate (27%), and club feet (73%)** ([PMID: 11718203](https://pubmed.ncbi.nlm.nih.gov/11718203/)). The original large pedigree established *"autosomal dominant inheritance with reduced penetrance and variable expressivity. Penetrance appears to be more reduced in females than in males, and cleft palate is the least frequently manifested trait"* ([PMID: 458832](https://pubmed.ncbi.nlm.nih.gov/458832/)). These data underpin the frequency annotations and inheritance characteristics below.

### Finding 5 — Allelic dichotomy: dominant GoF (C-terminal) vs. recessive LOF (N-terminal/central)

*PIEZO2* shows a clean **genotype–mechanism dichotomy**. Heterozygous **gain-of-function missense** mutations, mainly at the C terminus, cause dominant DA3 (Gordon)/DA5/MWS: *"heterozygous gain-of-function missense mutations, mainly localized at the C terminus, cause dominant distal arthrogryposis 3 (DA3), distal arthrogryposis 5 (DA5), or Marden-Walker syndrome (MWKS)"* ([PMID: 27843126](https://pubmed.ncbi.nlm.nih.gov/27843126/)). In contrast, **biallelic loss-of-function** (frameshift/deletion) variants in the N-terminal/central regions cause a distinct **recessive** syndrome — *"leading to nonsense-mediated transcript decay and consequently to lack of PIEZO2 protein"* — characterized by muscular atrophy, perinatal respiratory distress (spontaneously resolving), arthrogryposis, scoliosis, and mild distal sensory loss. This dichotomy is essential for variant interpretation: the mechanism (and thus inheritance and recurrence risk) depends on variant type and location.

### Finding 6 — Model organisms recapitulate the mechanism

Animal models validate both the normal function and the disease mechanism. Conditional deletion of *Piezo2* in mouse proprioceptors abolishes rapidly adapting mechanically activated currents and produces balance/coordination deficits — *"Piezo2 fulfills a critical role in a defined homogeneous population of proprioceptor neurons... demonstrating that this ion channel is essential for mammalian proprioceptive mechanotransduction"* ([PMID: 27184818](https://pubmed.ncbi.nlm.nih.gov/27184818/)). A GoF knock-in mouse reproduces contractures ([PMID: 36634173](https://pubmed.ncbi.nlm.nih.gov/36634173/)). In *C. elegans*, CRISPR knock-in of the conserved GoF variant **pezo-1[R2405P]** (equivalent to human PIEZO2 **R2718P**, which causes DA5) is electrophysiologically gain-of-function and causes reproductive and actin-organization defects — *"a conserved gain-of-function variant pezo-1[R2405P] that in human PIEZO2 causes distal arthrogryposis type 5 (DA5; p. R2718P)"* ([PMID: 38349741](https://pubmed.ncbi.nlm.nih.gov/38349741/)); the phenotype is suppressible by the F-actin regulator *gex-3/NCKAP1*, implicating the cytoskeleton in PIEZO2 gating.

### Finding 7 — Gordon Syndrome lies on a continuous PIEZO2 spectrum

GS is not a discrete entity but one pole of a continuum. A review of individuals sharing the recurrent p.Arg2686His variant and other alleles demonstrates *"marked phenotypic variability-from Gordon syndrome to distal arthrogryposis type 5-underscoring allelic heterogeneity and variable expressivity"* ([PMID: 41572728](https://pubmed.ncbi.nlm.nih.gov/41572728/)). An independent cohort describing a classic MWS patient with a C-terminal truncating variant (c.8237G>A/p.W2746*) alongside a GS girl with the prevalent c.8057G>A/p.R2686H further corroborates a dominant PIEZO2 continuum ([PMID: 36588752](https://pubmed.ncbi.nlm.nih.gov/36588752/)).

---

## Mechanistic Model / Causal Chain

### Ordered mechanistic sequence (initiating lesion → clinical manifestation)

1. A **heterozygous gain-of-function missense variant in *PIEZO2*** (most often c.8057G>A / p.Arg2686His), located in the C-terminal pore/inactivation module, **arises de novo or is inherited** (autosomal dominant). *[demonstrated — PMID 24726473]*
2. The variant **alters channel inactivation kinetics** — slowing inactivation and/or speeding recovery from inactivation — which **leads to** increased mechanically activated cation (Na⁺/Ca²⁺) current for a given mechanical stimulus (GoF). *[demonstrated in vitro — PMID 23487782]*
3. Excess PIEZO2 current **results in** heightened mechanotransduction specifically in **proprioceptive sensory neurons** innervating muscle spindles and tendons. *[demonstrated — PMID 36634173]*
4. Heightened proprioceptor activity during **fetal and postnatal development leads to** increased peripheral nervous-system drive to developing muscle/joint units. *[demonstrated in mouse — PMID 36634173]*
5. Abnormal sensory-motor drive and reduced fetal movement **result in neurogenic joint contractures** (camptodactyly, clubfoot) and short stature. *[inferred for human; demonstrated phenotype in mouse model]*

   **Branch A (GS-defining):** The p.Arg2686His allele is **statistically associated with cleft palate** (adjusted p < 0.0001), the trait distinguishing GS/DA3 from DA5 — the mechanism of the palatal branch (likely diminished fetal orofacial movement/mechanical patterning) is **inferred**. *[association demonstrated — PMID 24726473; mechanism inferred]*

   **Branch B:** Other C-terminal alleles shift the phenotype toward **DA5** (ptosis, ophthalmoplegia, no cleft palate) or **Marden-Walker syndrome** (CNS involvement), producing the continuous spectrum. *[demonstrated — PMID 27843126, 41572728]*

6. Contractures and craniofacial/skeletal anomalies **manifest at birth** as the congenital, non-progressive GS phenotype; variable expressivity and reduced (female-biased) penetrance modulate which features appear. *[demonstrated — PMID 458832]*

### Contrast with the recessive branch

```
PIEZO2 variant
│
├── C-terminal MISSENSE, heterozygous ─── GAIN of function ─── ↑ mechanotransduction
│     └── DOMINANT: DA3 (Gordon) / DA5 / Marden-Walker  (a continuous spectrum)
│
└── N-terminal/central FRAMESHIFT/DELETION, biallelic ─── NMD → NO protein ─── LOSS of function
      └── RECESSIVE: muscular atrophy, perinatal respiratory distress,
          arthrogryposis, scoliosis, distal sensory loss
```

### Pathways, processes, and ontology anchors

- **Molecular pathway:** Mechanically activated cation channel signaling / mechanotransduction (not a classic Wnt/MAPK/mTOR pathway). Gating is lipid-modulated — **phosphatidic acid and LPA are endogenous negative regulators of PIEZO2** ([PMID: 39147733](https://pubmed.ncbi.nlm.nih.gov/39147733/)) — and cytoskeleton/ECM-coupled ([PMID: 35586339](https://pubmed.ncbi.nlm.nih.gov/35586339/)).
- **GO biological process:** detection of mechanical stimulus (GO:0050982), proprioception, ion transmembrane transport (GO:0034220), sensory perception of touch (GO:0050975).
- **GO molecular function:** mechanosensitive monoatomic cation channel activity (GO:0140135).
- **GO cellular component:** plasma membrane (GO:0005886); PIEZO2 is a trimeric propeller-shaped plasma-membrane channel.
- **Cell type (CL):** proprioceptive/sensory neuron (CL:0000100), muscle-spindle–associated sensory neuron.
- **Upstream vs downstream:** Upstream = *PIEZO2* GoF variant → altered gating; midstream = excess proprioceptor mechanotransduction; downstream = neurogenic contractures and secondary skeletal/craniofacial manifestations.

---

## Section-by-Section Report

### 1. Disease Information

Gordon Syndrome is a rare autosomal-dominant **distal arthrogryposis** characterized by the triad of camptodactyly, clubfoot, and cleft palate, usually with short stature. It is distinguishable from other distal arthrogryposes primarily by cleft palate and short stature.

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0007252 |
| OMIM | #114300 |
| Orphanet | ORPHA:375 (Gordon syndrome / distal arthrogryposis type 3) |
| MeSH | Arthrogryposis (indexed via Distal Arthrogryposis / PIEZO2) |
| ICD-10 | Q74.3 (Arthrogryposis multiplex congenita) — no GS-specific code |
| ICD-11 | LD28.1 / arthrogryposis grouping (no GS-specific code) |
| Gene | *PIEZO2* (HGNC:26270), 18p11.22 |

**Synonyms / alternative names:** Distal arthrogryposis type 3 (DA3); Camptodactyly–cleft palate–clubfoot; Gordon's syndrome. **Data source type:** Aggregated disease-level resources and published case series/cohorts (OMIM, Orphanet, PubMed) — **not** individual EHR data.

### 2. Etiology

- **Primary cause — genetic:** Heterozygous gain-of-function missense variants in *PIEZO2* ([PMID: 24726473](https://pubmed.ncbi.nlm.nih.gov/24726473/)). No environmental, infectious, or toxic cause is implicated.
- **Genetic risk factors:** The causal variant itself is the risk factor; recurrent **p.Arg2686His** is by far the most common. No separate susceptibility loci or validated human modifier genes are known (the *C. elegans* suppressor *gex-3/NCKAP1* is an experimental modifier of a PIEZO2 GoF phenotype — [PMID: 38349741](https://pubmed.ncbi.nlm.nih.gov/38349741/)).
- **Environmental risk factors:** None established. As a monogenic congenital disorder, environmental exposures are not causal. Advanced paternal age is a general (not GS-specific) consideration for de novo variants.
- **Protective factors:** None genetic known. Experimentally, **phosphatidic acid/LPA** negatively regulate PIEZO2 ([PMID: 39147733](https://pubmed.ncbi.nlm.nih.gov/39147733/)) and a dietary fatty acid reduces the contracture phenotype in mice ([PMID: 36634173](https://pubmed.ncbi.nlm.nih.gov/36634173/)) — candidate protective/therapeutic modulators, not established human protective factors.
- **Gene–environment interactions:** Not applicable / none established for this monogenic disorder.

### 3. Phenotypes

| Phenotype | HPO term (suggested) | Type | Frequency | Onset / course |
|---|---|---|---|---|
| Camptodactyly | HP:0012385 | Clinical sign / physical | ~89% | Congenital, non-progressive |
| Talipes equinovarus (clubfoot) | HP:0001762 | Physical malformation | ~73% | Congenital, non-progressive |
| Cleft palate | HP:0000175 | Physical malformation | ~27% (GS-defining; assoc. R2686H) | Congenital |
| Short stature | HP:0004322 | Physical | Common | Congenital/childhood |
| Ptosis | HP:0000508 | Clinical sign | Frequent (esp. DA5 end) | Congenital |
| Scoliosis / stiff spine | HP:0002650 | Physical | Reported | Childhood, may progress |
| Distinctive facies | HP:0001999 | Physical | Variable | Congenital |
| Bifid uvula | HP:0000193 | Physical | Reported (mild palatal end) | Congenital |
| Mild intellectual disability / psychomotor delay | HP:0001256 / HP:0001263 | Behavioral/cognitive | Occasional (spectrum) | Childhood |

Frequencies from [PMID: 11718203](https://pubmed.ncbi.nlm.nih.gov/11718203/); psychomotor delay/ID occasionally reported ([PMID: 27714920](https://pubmed.ncbi.nlm.nih.gov/27714920/)). **Severity:** mild to moderate, variable. **Progression:** congenital and essentially non-progressive (contractures static, though scoliosis can progress). **Quality-of-life impact:** contractures affect fine motor function and ambulation; cleft palate affects feeding/speech; most distal-arthrogryposis patients achieve independent ambulation and self-care ([PMID: 33104047](https://pubmed.ncbi.nlm.nih.gov/33104047/)). No GS-specific EQ-5D/SF-36 data available.

### 4. Genetic / Molecular Information

- **Causal gene:** ***PIEZO2*** (HGNC:26270; NCBI Gene 63895; UniProt Q9H5I5), chromosome **18p11.22**; phenotype OMIM #114300.
- **Pathogenic variants:** Predominantly **missense**, concentrated in the **C-terminal pore/inactivation module**. Recurrent GS allele: **c.8057G>A, p.Arg2686His**. Other spectrum alleles include p.Arg2718Leu/Pro, p.Glu2727del, p.Thr2221Ile, p.Ser2690Arg, p.Met998Ile, and truncating C-terminal p.W2746*. Novel GS alleles continue to be reported (e.g., c.8576G>A/p.Trp2859* in a fetus — [PMID: 37587573](https://pubmed.ncbi.nlm.nih.gov/37587573/)).
- **Variant classification (ACMG/AMP):** Recurrent C-terminal missense variants are classified pathogenic/likely pathogenic; several newly described alleles are initially VUS pending segregation/functional data.
- **Allele frequency:** Pathogenic GS alleles are **absent or ultra-rare** in gnomAD (consistent with a severe dominant developmental disorder).
- **Somatic vs germline:** **Germline** (constitutional). De novo occurrence is common; germline mosaicism is possible but rarely documented ([PMID: 37587573](https://pubmed.ncbi.nlm.nih.gov/37587573/)).
- **Functional consequence:** **Gain of function** — altered inactivation increasing mechanically activated current ([PMID: 23487782](https://pubmed.ncbi.nlm.nih.gov/23487782/)). Contrast: biallelic N-terminal LOF → recessive disease ([PMID: 27843126](https://pubmed.ncbi.nlm.nih.gov/27843126/)).
- **Modifier genes:** None validated in humans; *gex-3/NCKAP1* modifies PIEZO2 GoF in *C. elegans* ([PMID: 38349741](https://pubmed.ncbi.nlm.nih.gov/38349741/)).
- **Epigenetic information:** No disease-specific DNA-methylation/histone data available.
- **Chromosomal abnormalities:** Not a feature of classic GS; rare intragenic *PIEZO2* duplications cause a distinct recessive phenotype ([PMID: 41531622](https://pubmed.ncbi.nlm.nih.gov/41531622/)).

### 5. Environmental Information

**Not applicable.** GS is a monogenic germline disorder. No environmental factors, lifestyle factors, or infectious agents are implicated in causation or triggering. (Note: congenital myopathy co-occurrence and **malignant hyperthermia** susceptibility have been reported in isolated GS cases, relevant to anesthetic exposure — [PMID: 24878349](https://pubmed.ncbi.nlm.nih.gov/24878349/).)

### 6. Mechanism / Pathophysiology

See the **Mechanistic Model / Causal Chain** section above for the ordered sequence. In brief: C-terminal *PIEZO2* GoF variant → altered channel inactivation → excess mechanically activated current → hyperactive proprioceptive sensory-neuron mechanotransduction during development → reduced fetal movement and neurogenic joint contractures → congenital GS phenotype, with the R2686H allele branching toward cleft palate and other alleles branching toward DA5/MWS. Key molecular detail: PIEZO2 gating is lipid-modulated (phosphatidic acid/LPA are negative regulators; [PMID: 39147733](https://pubmed.ncbi.nlm.nih.gov/39147733/)) and cytoskeleton/ECM-coupled ([PMID: 35586339](https://pubmed.ncbi.nlm.nih.gov/35586339/)). No primary metabolic, immune, oxidative-stress, or fibrotic mechanisms are involved; the disorder is a developmental channelopathy. GO/CL anchors as listed above.

### 7. Anatomical Structures Affected

- **Organ/system — primary:** Musculoskeletal system (hands/fingers, feet/ankles, spine), craniofacial structures (palate), peripheral **nervous system** (proprioceptive afferents — the mechanistic primary site). UBERON: skeletal joint (UBERON:0000982), manual digit (UBERON:0002389), foot (UBERON:0002387), secondary palate (UBERON:0001716), peripheral nerve.
- **Secondary involvement:** Extraocular muscles (ptosis/ophthalmoplegia at DA5 end), respiratory system (restrictive pulmonary function at the severe end, [PMID: 36317804](https://pubmed.ncbi.nlm.nih.gov/36317804/)), vertebral column (scoliosis).
- **Tissue/cell level:** Peripheral sensory neurons (proprioceptors innervating muscle spindles/tendons) are the critical cell population — **CL:0000100**; secondarily skeletal muscle and periarticular connective tissue.
- **Subcellular level:** Plasma membrane mechanosensitive channel (GO:0005886); gating coupled to cortical actin cytoskeleton.
- **Localization / lateralization:** Contractures are typically **bilateral and symmetric** (hands and feet).

### 8. Temporal Development

- **Onset:** **Congenital** — contractures detectable prenatally by ultrasound (as early as ~13 weeks gestation; [PMID: 27714920](https://pubmed.ncbi.nlm.nih.gov/27714920/)) and present at birth.
- **Onset pattern:** Developmental/congenital (not acute).
- **Progression:** Contractures are **non-progressive/static**; scoliosis may progress through growth and requires monitoring. No oncologic-style "stages."
- **Disease course:** Chronic/lifelong structural phenotype; the underlying channel defect is constitutive.
- **Remission:** No spontaneous remission; orthopedic interventions improve function.
- **Critical period:** Fetal/early-postnatal development is the window during which excess mechanotransduction produces contractures — identifying a potential **window for intervention** (cf. Botox/fatty-acid rescue in neonatal mice, [PMID: 36634173](https://pubmed.ncbi.nlm.nih.gov/36634173/)).

### 9. Inheritance and Population

- **Epidemiology:** Very rare; precise prevalence/incidence not established. Orphanet classes GS/DA3 as <1/1,000,000. No reliable incidence figures.
- **Inheritance:** **Autosomal dominant** ([PMID: 458832](https://pubmed.ncbi.nlm.nih.gov/458832/)); frequent de novo occurrence.
- **Penetrance:** **Reduced/incomplete**, and **more reduced in females than males** ([PMID: 458832](https://pubmed.ncbi.nlm.nih.gov/458832/)).
- **Expressivity:** **Variable**, including intrafamilial variability and overlap across GS/DA5/MWS with identical alleles ([PMID: 41572728](https://pubmed.ncbi.nlm.nih.gov/41572728/)).
- **Genetic anticipation:** Not a feature (not a repeat-expansion disorder).
- **Germline mosaicism:** Rarely documented but possible ([PMID: 37587573](https://pubmed.ncbi.nlm.nih.gov/37587573/)).
- **Founder effects / consanguinity:** Not applicable to the dominant form (consanguinity is relevant to the **recessive** biallelic-LOF PIEZO2 disorder, [PMID: 27843126](https://pubmed.ncbi.nlm.nih.gov/27843126/)).
- **Carrier frequency:** Not applicable (dominant).
- **Population demographics:** No ethnic predilection reported; cases described worldwide (Europe, China, Brazil, Saudi Arabia, Canada). Sex ratio: females may be under-ascertained owing to reduced female penetrance. Age distribution: diagnosed prenatally/at birth/in childhood.

### 10. Diagnostics

- **Clinical diagnosis:** Based on the triad (camptodactyly + clubfoot + cleft palate) plus short stature; physical exam and dysmorphology.
- **Imaging:** Prenatal **fetal ultrasound** detects contractures/clubfoot/micrognathia and can establish a prenatal diagnosis when combined with genetic testing ([PMID: 37587573](https://pubmed.ncbi.nlm.nih.gov/37587573/)); skeletal radiographs for contractures/scoliosis.
- **Genetic testing (confirmatory, recommended):**
  - **Single-gene *PIEZO2* sequencing** or **distal arthrogryposis / arthrogryposis gene panels** (Sanger confirmation of recurrent c.8057G>A is efficient when the phenotype is classic).
  - **Whole-exome sequencing (WES)** — the discovery and workhorse modality ([PMID: 24726473](https://pubmed.ncbi.nlm.nih.gov/24726473/), [PMID: 37587573](https://pubmed.ncbi.nlm.nih.gov/37587573/)).
  - **Whole-genome sequencing (WGS)** — useful when panels/WES negative.
  - **Chromosomal microarray** — not diagnostic for point-variant GS, but detects the rare duplication/CNV forms ([PMID: 41531622](https://pubmed.ncbi.nlm.nih.gov/41531622/)).
  - Karyotype/FISH/mtDNA/repeat-expansion testing: **not applicable**.
- **Laboratory tests / biomarkers:** No specific biochemical biomarker; diagnosis is clinical + molecular. (Creatine kinase and muscle biopsy occasionally relevant when congenital myopathy co-occurs — [PMID: 24878349](https://pubmed.ncbi.nlm.nih.gov/24878349/).)
- **Omics-based diagnostics:** Not routinely used.
- **Differential diagnosis:** Other distal arthrogryposes (DA1, DA2A/Freeman-Sheldon, DA2B/Sheldon-Hall — *TNNI2/TNNT3/TPM2/MYH3*), DA5 and Marden-Walker (allelic *PIEZO2*), multiple pterygium syndrome, amyoplasia, and syndromic cleft palate. Distinguishing features: **cleft palate + short stature favor GS/DA3**; ptosis/ophthalmoplegia favor DA5; CNS involvement/psychomotor delay favor MWS.
- **Screening:** No population newborn screen. **Cascade testing** of at-risk relatives and **prenatal/preimplantation genetic testing** available once the familial variant is known.

### 11. Outcome / Prognosis

- **Survival / life expectancy:** Generally **normal** for classic GS. Exception: the severe respiratory end of the PIEZO2 spectrum can cause lethal neonatal respiratory insufficiency ([PMID: 36317804](https://pubmed.ncbi.nlm.nih.gov/36317804/)).
- **Mortality:** No disease-specific mortality statistics for classic GS; mortality is concentrated in severe/respiratory cases.
- **Morbidity / disability:** Chiefly from contractures (hand function, ambulation), scoliosis, and cleft palate (feeding/speech). Most individuals with distal arthrogryposis achieve **independent ambulation and self-care** with orthopedic management ([PMID: 33104047](https://pubmed.ncbi.nlm.nih.gov/33104047/)).
- **Quality of life:** No GS-specific validated QoL instrument data.
- **Complications:** Progressive scoliosis; feeding/speech difficulty from cleft palate; anesthetic risk including reported **malignant hyperthermia** in a GS case with congenital myopathy ([PMID: 24878349](https://pubmed.ncbi.nlm.nih.gov/24878349/)).
- **Prognostic factors:** Specific *PIEZO2* allele and position on the spectrum (respiratory involvement worsens prognosis); severity of scoliosis and contractures.

### 12. Treatment

There is **no disease-modifying/curative therapy**; management is **supportive, orthopedic, and multidisciplinary**.

- **Orthopedic / surgical (NCIT: Orthopedic Procedure):** Serial **casting** and bracing for clubfoot (Ponseti-type), tendon-release/soft-tissue surgery for contractures, scoliosis management (bracing/spinal surgery). Distal-arthrogryposis orthopedic cohorts show good functional outcomes ([PMID: 33104047](https://pubmed.ncbi.nlm.nih.gov/33104047/)).
- **Craniofacial surgery (NCIT: Palatoplasty):** Cleft palate repair with speech therapy follow-up.
- **Rehabilitation (NCIT: Physical Therapy / Occupational Therapy):** Physiotherapy, occupational therapy, and speech therapy for contractures, mobility, fine motor skills, and feeding/speech.
- **Pharmacotherapy:** No approved drug. **Mechanism-targeted candidates (experimental, preclinical):** **botulinum toxin** (NCIT: Botulinum Toxin) and a **PIEZO2-modulating dietary fatty acid** reduced DA-like deficits in mice ([PMID: 36634173](https://pubmed.ncbi.nlm.nih.gov/36634173/)); **phosphatidic acid/LPA**-based PIEZO2 inhibition is a plausible future strategy ([PMID: 39147733](https://pubmed.ncbi.nlm.nih.gov/39147733/)). These are **not** established human treatments.
- **Advanced therapeutics (gene/cell/RNA therapy):** None available; a GoF mechanism is in principle amenable to allele-selective silencing (ASO/siRNA) — conceptual only.
- **Anesthetic caution:** Given reported malignant hyperthermia/congenital myopathy associations, anesthetic planning should consider MH precautions ([PMID: 24878349](https://pubmed.ncbi.nlm.nih.gov/24878349/)).
- **Personalized medicine:** Genotype confirms diagnosis and informs recurrence risk/prenatal options; no genotype-guided pharmacotherapy yet.

### 13. Prevention

- **Primary prevention:** Not possible (congenital genetic disorder). **Genetic counseling** is central: autosomal-dominant 50% transmission risk from an affected parent, with reduced (female-biased) penetrance and variable expressivity complicating counseling ([PMID: 458832](https://pubmed.ncbi.nlm.nih.gov/458832/)).
- **Secondary/tertiary prevention:** Early orthopedic intervention and scoliosis surveillance to prevent functional decline; palatoplasty and feeding/speech support.
- **Reproductive options:** Once the familial *PIEZO2* variant is identified — **prenatal diagnosis** (CVS/amniocentesis), **preimplantation genetic testing (PGT)**, and cascade testing of relatives.
- **Immunization / public-health / environmental interventions:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *PIEZO2* is evolutionarily conserved. Mouse ortholog *Piezo2* (*Mus musculus*, NCBI:txid10090); *C. elegans* ortholog *pezo-1* (*Caenorhabditis elegans*, NCBI:txid6239). Human variant positions map to conserved residues (e.g., human R2718P ≈ worm R2405P).
- **Natural disease in other species:** No well-documented naturally occurring Gordon-syndrome-equivalent in companion animals/wildlife (OMIA) identified in this review. Veterinary relevance: none established.
- **Comparative biology:** Disease mechanisms are evolutionarily conserved at the channel level — the worm GoF knock-in reproduces electrophysiological gain-of-function and physiological defects ([PMID: 38349741](https://pubmed.ncbi.nlm.nih.gov/38349741/)); mouse *Piezo2* is essential for proprioception ([PMID: 27184818](https://pubmed.ncbi.nlm.nih.gov/27184818/)).
- **Transmission / zoonosis:** Not applicable (non-infectious).

### 15. Model Organisms

| Model | Type | Construct | Phenotype recapitulation | Reference |
|---|---|---|---|---|
| Mouse (*Mus musculus*) | Mammalian, in vivo | Proprioceptor-specific *Piezo2* **GoF knock-in** | **High** — sufficient to induce DA5-like contractures; Botox + dietary fatty acid rescue | [PMID: 36634173](https://pubmed.ncbi.nlm.nih.gov/36634173/) |
| Mouse | Mammalian, in vivo | Conditional *Piezo2* **knockout** in proprioceptors | Validates normal function — loss abolishes RA mechanically activated currents, balance/coordination deficits | [PMID: 27184818](https://pubmed.ncbi.nlm.nih.gov/27184818/) |
| *C. elegans* | Invertebrate | *pezo-1[R2405P]* CRISPR knock-in (≈ human R2718P/DA5) | Moderate — GoF electrophysiology + reproductive/actin defects; suppressed by *gex-3/NCKAP1* | [PMID: 38349741](https://pubmed.ncbi.nlm.nih.gov/38349741/) |
| HEK/heterologous cells | In vitro | PIEZO2 mutant cDNA (E2727del, I802F) | Biophysical GoF (altered inactivation); no toxicity | [PMID: 23487782](https://pubmed.ncbi.nlm.nih.gov/23487782/) |

- **Applications:** Dissecting channel gating, the neurogenic origin of contractures, the developmental critical period, and therapeutic screening (Botox, lipids, dietary fatty acids).
- **Limitations:** Mouse GoF studies modeled the DA5 allele/phenotype rather than the GS-specific cleft-palate branch; the orofacial/palatal mechanism remains uncharacterized in models. Invertebrate models cannot capture craniofacial/skeletal features.
- **Resources:** MGI (mouse), WormBase (*C. elegans*), Cellosaurus/ATCC (cell lines).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [24726473](https://pubmed.ncbi.nlm.nih.gov/24726473/) | *Mutations in PIEZO2 cause GS, MWS, and DA5* | Human exome cohort | F1 — causal gene, recurrent R2686H, cleft-palate association |
| [23487782](https://pubmed.ncbi.nlm.nih.gov/23487782/) | *Gain-of-function PIEZO2 mutations cause a DA subtype* | In vitro electrophysiology | F2 — GoF via altered inactivation; no toxicity |
| [36634173](https://pubmed.ncbi.nlm.nih.gov/36634173/) | *Excessive mechanotransduction in sensory neurons causes joint contractures* | Mouse in vivo | F3 — neurogenic mechanism; Botox/fatty-acid rescue |
| [11718203](https://pubmed.ncbi.nlm.nih.gov/11718203/) | *Scoliosis in Gordon's syndrome* | Human clinical | F4 — triad frequencies |
| [458832](https://pubmed.ncbi.nlm.nih.gov/458832/) | *Gordon syndrome large pedigree* | Human pedigree | F4 — AD inheritance, reduced female penetrance, variable expressivity |
| [27843126](https://pubmed.ncbi.nlm.nih.gov/27843126/) | *Biallelic loss of PIEZO2...* | Human + mechanism | F5 — dominant GoF vs recessive LOF dichotomy |
| [27184818](https://pubmed.ncbi.nlm.nih.gov/27184818/) | *Critical role for Piezo2 in proprioceptive mechanotransduction* | Mouse in vivo | F6 — Piezo2 essential for proprioception |
| [38349741](https://pubmed.ncbi.nlm.nih.gov/38349741/) | *F-actin factor suppresses DA5 PIEZO2 variant in C. elegans* | Invertebrate model | F6 — conserved GoF model; cytoskeletal modifier |
| [41572728](https://pubmed.ncbi.nlm.nih.gov/41572728/) | *Expanding genotype-phenotype of MWS due to PIEZO2* | Human review | F7 — same variant → GS↔DA5 continuum |
| [36588752](https://pubmed.ncbi.nlm.nih.gov/36588752/) | *Continuum in dominant PIEZO2 spectrum* | Human cohort | F7 — dominant PIEZO2 continuum |
| [30988732](https://pubmed.ncbi.nlm.nih.gov/30988732/) | *Bioinformatics of PIEZO2 mutations* | Computational | F2/F5 — C-terminal dominant GoF vs N-terminal recessive LOF |
| [39147733](https://pubmed.ncbi.nlm.nih.gov/39147733/) | *Phosphatidic acid negatively regulates PIEZO2* | In vitro/mouse | Mechanism/therapeutics — lipid modulation |
| [37587573](https://pubmed.ncbi.nlm.nih.gov/37587573/) | *Novel PIEZO2 variant in a fetus (GS)* | Human case | Prenatal diagnosis; de novo/mosaicism |
| [36317804](https://pubmed.ncbi.nlm.nih.gov/36317804/) | *Lethal respiratory course in PIEZO2 DA5* | Human case | Severe end of spectrum / prognosis |
| [24878349](https://pubmed.ncbi.nlm.nih.gov/24878349/) | *GS with congenital myopathy / malignant hyperthermia* | Human cases | Anesthetic risk; comorbidity |
| [27714920](https://pubmed.ncbi.nlm.nih.gov/27714920/) | *Familial GS with PIEZO2 mutation* | Human family | Prenatal detection; psychomotor-delay spectrum |

**Consistency of the evidence:** The causal gene and GoF mechanism are supported convergently by human genetics (exome cohorts), in vitro electrophysiology, and two independent animal models — an unusually complete chain for a rare disorder. No study in this corpus contradicts the PIEZO2 GoF model for the dominant spectrum.

---

## Limitations and Knowledge Gaps

1. **The cleft-palate branch is unexplained mechanistically.** p.Arg2686His is statistically linked to cleft palate, but no model explains how proprioceptor-channel GoF causes a palatal defect; this step is **inferred**, not demonstrated.
2. **Models target DA5, not GS specifically.** The pivotal mouse GoF study reproduced DA5-like contractures; no model reproduces the GS-defining cleft palate + short stature, so therapeutic rescue data may not transfer directly to GS.
3. **No epidemiology.** Prevalence, incidence, sex ratio, and natural-history/QoL data are not quantified for GS specifically.
4. **Therapeutics are preclinical.** Botox and fatty-acid/lipid modulation are promising but unproven in humans; no GS clinical trials (NCT identifiers) were identified.
5. **Variant interpretation of novel alleles.** Several reported variants remain VUS; functional assays are not routinely performed clinically.
6. **No human omics data** (transcriptomics/proteomics/metabolomics) for GS tissue.
7. **Penetrance/expressivity modifiers** in humans are uncharacterized (only a worm suppressor is known).

---

## Proposed Follow-up Experiments / Actions

1. **Generate a GS-specific (R2686H) mouse knock-in** and assess craniofacial/palatal development to test whether proprioceptor GoF alone, or broader PIEZO2 expression (e.g., in cranial neural crest/orofacial tissues), produces cleft palate — resolving the unexplained branch.
2. **Test lipid/fatty-acid and Botox interventions during the fetal critical window** in GS-relevant models, defining dose, timing, and whether palatal and skeletal phenotypes (not just contractures) are modifiable.
3. **Develop allele-selective knockdown (ASO/siRNA)** against the recurrent R2686H allele as a mechanism-rational disease-modifying candidate.
4. **Assemble an international GS/PIEZO2 registry** to quantify prevalence, penetrance by sex, genotype–phenotype correlations across the GS–DA5–MWS continuum, natural history, and validated QoL outcomes.
5. **Systematic functional classification of VUS** (standardized patch-clamp inactivation assays) to accelerate ACMG reclassification and prenatal counseling.
6. **Clinical anesthesia study** of malignant-hyperthermia/myopathy risk in PIEZO2 patients to issue evidence-based peri-operative guidance.

---

*Report compiled from 5 autonomous investigation iterations; 7 confirmed findings; 32 papers reviewed. Evidence types span human clinical/genetic cohorts, in vitro electrophysiology, computational analysis, and mouse/C. elegans models. Information derived from aggregated disease-level resources and primary literature, not individual EHR data.*


## Artifacts

- [OpenScientist final report](Gordon_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Gordon_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 12 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007252` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Gordon syndrome**
- `GO:0005886` (2 mentions) - the report calls it "GO cellular component:** plasma membrane", "Subcellular level:** Plasma membrane mechanosensitive channel"; GO calls it **plasma membrane**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0050982` (1 mention) - the report calls it "GO biological process:** detection of mechanical stimulus"; GO calls it **detection of mechanical stimulus**
- `GO:0140135` (1 mention) - the report calls it "GO molecular function:** mechanosensitive monoatomic cation channel activity"; GO calls it **mechanosensitive monoatomic cation channel activity**
- `HP:0001762` (1 mention) - the report calls it "Talipes equinovarus (clubfoot)"; HP calls it **Talipes equinovarus**
- `HP:0002650` (1 mention) - the report calls it "Scoliosis / stiff spine"; HP calls it **Scoliosis**
- `HP:0001999` (1 mention) - the report calls it "Distinctive facies"; HP calls it **Abnormal facial shape**, and lists "Distinctive facies" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005886` - called "GO cellular component:** plasma membrane", "Subcellular level:** Plasma membrane mechanosensitive channel"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.